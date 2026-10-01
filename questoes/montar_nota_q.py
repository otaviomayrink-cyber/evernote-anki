#!/usr/bin/env python3
"""Monta notas de questões (-Q) a partir da fonte dos cards: JSONL + HTML + ENEX, com figuras.

    python3 montar_nota_q.py FONTE --titulo "00-TESTE-GRAF-1 - Obj." --sigla ECO --passada 0 \
        --specs teste_graficos/specs -o teste_graficos/saida

FONTE: um .py com a lista CARDS (como teste_graficos/cards_teste.py) ou um .jsonl já gerado
(registros com os campos de origem). As figuras são renderizadas pelo qgraf a partir das specs
(pasta --specs) e embutidas no ENEX como <en-media> + <resource>.
Ordem do verso e marcação: Folha -Q v3 §3 e §10.
"""
import argparse
import base64
import datetime as dt
import hashlib
import html
import json
import os
import re
import runpy
import shutil
import struct
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(AQUI, "graficos"))
import qgraf  # noqa: E402

LARGURA = 1400
IMG_FRENTE, IMG_VERSO = 540, 660  # largura de exibição das figuras (px)
MIN_FRENTE_COM_FIG, MIN_VERSO_COM_FIG = 600, 720

CINZA = "rgb(160, 160, 160)"
GAB = {
    "CERTO": '<p><span style="color: rgb(0, 130, 0);"><b>✅ CERTO</b></span></p>',
    "ERRADO": '<p><span style="color: rgb(200, 0, 0);"><b>❌ ERRADO</b></span></p>',
    "ANULADO": '<p><span style="color: rgb(160, 160, 160);"><b>⚪ ANULADO</b></span></p>',
    "RESPOSTA": '<p><span style="color: rgb(0, 60, 200);"><b>🔵 RESPOSTA</b></span></p>',
}
BANCAS_PROVA = {"CEBRASPE", "FGV", "FCC", "VUNESP", "IADES", "Quadrix", "ESAF", "CESGRANRIO", "FUNDATEC"}
CODE = '<code style="font-family:monospace; color:#B3261E; background-color:#F6F1F0;">{}</code>'
TD = "border:1px solid #CCC; padding:8px; vertical-align:top; width:{}px;"


def esc(t):
    return html.escape(t, quote=False)


def sanear(h):
    """Escapa '<' e '&' soltos (ex.: "ε < 0", "P&D") e troca &nbsp; por &#160; — XML válido para o ENEX."""
    h = h.replace("&nbsp;", "&#160;")
    h = re.sub(r"&(?!#\d+;|#x[0-9a-fA-F]+;|[a-zA-Z]+;)", "&amp;", h)
    return re.sub(r"<(?![a-zA-Z/!?])", "&lt;", h)


# ------------------------------------------------------------------ figuras
class Figuras:
    """Renderiza as specs sob demanda e guarda png, md5 e dimensões."""

    def __init__(self, pasta_specs, saida):
        self.specs = {}
        if pasta_specs:
            for s in qgraf.carregar_specs([pasta_specs]):
                self.specs[s["id"]] = s
        self.dir = os.path.join(saida, "figuras")
        self.cache = {}
        self.erros = []

    def get(self, fid):
        if fid in self.cache:
            return self.cache[fid]
        if fid not in self.specs:
            raise SystemExit(f"figura {fid}: spec não encontrada")
        r = qgraf.renderizar(self.specs[fid], self.dir)
        for e in r["erros"]:
            self.erros.append(f"{fid}: {e}")
        with open(r["png"], "rb") as fh:
            dados = fh.read()
        w, h = struct.unpack(">II", dados[16:24])
        info = {"id": fid, "png": r["png"], "md5": hashlib.md5(dados).hexdigest(), "w": w, "h": h,
                "legenda": self.specs[fid].get("legenda", ""), "dados": dados,
                "fidelidade": self.specs[fid].get("fidelidade", "fiel" if self.specs[fid].get("uso") == "frente"
                                                  else "didatica"),
                "tipo": self.specs[fid].get("tipo", "modelo" if not self.specs[fid].get("paineis") else "paineis"),
                "spec": self.specs[fid]}
        self.cache[fid] = info
        return info


def tag_figura(info, largura, modo):
    if modo == "enex":
        return f'<div><en-media type="image/png" hash="{info["md5"]}" width="{largura}"/></div>'
    return f'<div><img src="figuras/{info["id"]}.png" width="{largura}"/></div>'


# ------------------------------------------------------------------ frente
def cabecalho(c):
    partes = [f'{c["tipo"]} - {c["banca"]}']
    if c.get("prova"):
        partes.append(c["prova"])
    partes.append(re.sub(r"^\W+\s*", "", c["subtema"]))
    return "[" + " › ".join(partes) + "]"


def tabela_aninhada(t, largura):
    n = len(t["cabecalho"])
    primeira = max(140, int(largura * 0.32)) if n > 2 else largura // 2
    resto = (largura - primeira) // (n - 1)
    ws = [primeira] + [resto] * (n - 1)
    ws[-1] = largura - sum(ws[:-1])
    td = "border:1px solid #CCC; padding:4px; width:{}px;"
    out = ['<div><table style="border-collapse:collapse; table-layout:fixed; width:%dpx;">' % largura,
           "<colgroup>" + "".join(f'<col style="width:{w}px;"/>' for w in ws) + "</colgroup><tbody>"]
    out.append("<tr>" + "".join(f'<td style="{td.format(w)}"><b>{esc(x)}</b></td>'
                                for w, x in zip(ws, t["cabecalho"])) + "</tr>")
    for linha in t["linhas"]:
        out.append("<tr>" + "".join(f'<td style="{td.format(w)}">{esc(x)}</td>' for w, x in zip(ws, linha))
                   + "</tr>")
    out.append("</tbody></table></div>")
    if t.get("titulo"):
        out.insert(0, f'<p><b>{esc(t["titulo"])}</b></p>')
    if t.get("fonte"):
        out.append(f'<p><span style="color: {CINZA};">{esc(t["fonte"])}</span></p>')
    return "".join(out)


def frente(c, figs, larg_frente, modo):
    p = []
    marca = "❌ " if c.get("errei") else ""
    p.append(marca + CODE.format(esc(cabecalho(c))) + "<p><br/></p>")
    p.append(f'<p><b>{esc(c["comando"])}</b></p>')
    if c.get("aviso_frente"):
        p.append(f'<p><span style="color: {CINZA};"><i>[{esc(c["aviso_frente"])}]</i></span></p>')
    if c.get("excerto"):
        p.append(c["excerto"])
    if c.get("excerto_tabela"):
        p.append(tabela_aninhada(c["excerto_tabela"], min(560, larg_frente - 40)))
    for fid in c.get("frente_figuras", []):
        info = figs.get(fid)
        p.append(tag_figura(info, min(IMG_FRENTE, larg_frente - 40), modo))
        leg = esc(info["legenda"])
        if info["fidelidade"] == "conjectural":
            leg += " (figura redesenhada; traçado aproximado)"
        p.append(f'<p><span style="color: {CINZA};"><i>{leg}</i></span></p>')
    p.append("<p><br/></p>")
    p.append(f'<p><b>{c.get("rotulo_item", "Item")}:</b> {c["assertiva"]}</p>')
    return "".join(p)


# ------------------------------------------------------------------ verso
def bloco_lista(rotulo, itens):
    return f"<p><b>{rotulo}:</b></p><ul>" + "".join(f"<li>{i}</li>" for i in itens) + "</ul>"


def verso(c, figs, larg_verso, modo):
    g = c["gabarito"]
    v = [GAB.get(g) or f'<p><span style="color: rgb(0, 60, 200);"><b>🔵 Letra {g}</b></span></p>']
    v.append("<p><br/></p>")
    v.append(f'<p>{c["anotada"]}</p>')
    v.append("<hr/>")
    v.append(f'<p><b>🎯 Em poucas palavras:</b> {c["poucas"]}</p>')
    for cond in c.get("condicionais", []):  # (rótulo, html)
        v.append(f"<p><b>{cond[0]}:</b> {cond[1]}</p>")
    v.append(bloco_lista("📖 Destrinchando o tema", c["destrinchando"]))
    gv = c.get("grafico_verso")
    for fid in ([gv] if isinstance(gv, str) else (gv or [])):
        info = figs.get(fid)
        v.append("<p><b>📈 No gráfico:</b></p>")
        v.append(tag_figura(info, min(IMG_VERSO, larg_verso - 40), modo))
        v.append(f'<p><span style="color: {CINZA};"><i>{esc(info["legenda"])}</i></span></p>')
    v.append(f'<p><b>🧐 Dissecando a redação do item:</b> {c["dissecando"]}</p>')
    for rot, itens in c.get("modulos", []):
        v.append(bloco_lista(rot, itens) if isinstance(itens, list) else f"<p><b>{rot}:</b> {itens}</p>")
    if c.get("reescrita"):
        v.append(f'<p><b>✍️ Reescrita correta:</b> <i>{c["reescrita"]}</i></p>')
    return "".join(v)


# ------------------------------------------------------------------ nota
def ordem_banca(c):
    b = c["banca"]
    if c.get("cacd"):
        k = 0
    elif b == "CEBRASPE":
        k = 1
    elif b in BANCAS_PROVA:
        k = 2
    elif b == "Banca não identificada":
        k = 4
    elif b.startswith("Elaboração própria"):
        k = 5
    else:
        k = 3  # cursos e professores
    return (k, -(c.get("ano") or 0))


def larguras(cards, figs):
    def peso(t):
        return len(re.sub(r"<[^>]+>", "", t))
    pf = sum(peso(c["_frente_txt"]) for c in cards) / len(cards)
    pv = sum(peso(c["_verso_txt"]) for c in cards) / len(cards)
    a, b = pf ** 0.75, pv ** 0.75
    wf = int(round(LARGURA * a / (a + b)))
    wf = max(wf, int(LARGURA * 0.30))
    wf = min(wf, int(LARGURA * 0.70))
    if any(c.get("frente_figuras") or c.get("excerto_tabela") for c in cards):
        wf = max(wf, MIN_FRENTE_COM_FIG)
    if any(c.get("grafico_verso") for c in cards):
        wf = min(wf, LARGURA - MIN_VERSO_COM_FIG)
    return wf, LARGURA - wf


def tabela(cards, figs, modo):
    for c in cards:  # versão preliminar só para pesar o texto
        c["_frente_txt"] = frente(c, figs, 600, "html")
        c["_verso_txt"] = verso(c, figs, 800, "html")
    wf, wv = larguras(cards, figs)
    out = ['<div><table style="border-collapse:collapse; table-layout:fixed; width:1400px;">',
           f'<colgroup><col style="width:{wf}px;"/><col style="width:{wv}px;"/></colgroup>', "<tbody>"]
    for c in cards:
        out.append(f'<tr><td style="{TD.format(wf)}">{frente(c, figs, wf, modo)}</td>'
                   f'<td style="{TD.format(wv)}">{verso(c, figs, wv, modo)}</td></tr>')
    out.append("</tbody></table></div>")
    return "".join(out), wf, wv


def corpo_nota(cards, figs, modo):
    grupos = {}
    for c in cards:
        grupos.setdefault(c["subtema"], []).append(c)
    ordem = list(dict.fromkeys(c["subtema"] for c in cards))
    p = ["<h1>📍 Índice</h1><ul>"]
    for h2 in ordem:
        p.append(f"<li>{esc(h2)} ({len(grupos[h2])})</li>")
    p.append("</ul><hr/><h1>❓ Questões</h1>")
    for h2 in ordem:
        cs = sorted(grupos[h2], key=ordem_banca)
        p.append(f"<h2>{esc(h2)}</h2>")
        for i in range(0, len(cs), 60):
            t, _, _ = tabela(cs[i:i + 60], figs, modo)
            p.append(t)
    return sanear("".join(p))


def enex(titulo, corpo, figs_usadas):
    agora = dt.datetime.now(dt.timezone.utc).strftime("%Y%m%dT%H%M%SZ")
    conteudo = ('<?xml version="1.0" encoding="UTF-8" standalone="no"?>'
                '<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">'
                f"<en-note>{corpo}</en-note>")
    rec = []
    vistos = set()
    for info in figs_usadas:
        if info["md5"] in vistos:
            continue
        vistos.add(info["md5"])
        b64 = base64.encodebytes(info["dados"]).decode("ascii")
        rec.append(f'<resource><data encoding="base64">\n{b64}</data><mime>image/png</mime>'
                   f'<width>{info["w"]}</width><height>{info["h"]}</height>'
                   f'<resource-attributes><file-name>{info["id"]}.png</file-name></resource-attributes>'
                   f"</resource>")
    return ('<?xml version="1.0" encoding="UTF-8"?>\n'
            '<!DOCTYPE en-export SYSTEM "http://xml.evernote.com/pub/evernote-export4.dtd">\n'
            f'<en-export export-date="{agora}" application="montar_nota_q" version="1">\n'
            f"<note><title>{esc(titulo)}</title><created>{agora}</created><updated>{agora}</updated>"
            f"<content><![CDATA[{conteudo}]]></content>{''.join(rec)}</note>\n</en-export>\n")


def html_preview(titulo, corpo):
    return ("<!doctype html><html><head><meta charset='utf-8'><title>" + esc(titulo) + "</title></head>"
            "<body style='font-family:sans-serif; background:#fff; color:#222;'>" + corpo + "</body></html>")


# ------------------------------------------------------------------ JSONL
CAMPOS_ORIGEM = ["id", "subtema", "tipo", "banca", "prova", "ano", "cacd", "errei", "comando", "assertiva",
                 "gabarito", "gabarito_origem", "status", "tipo_erro", "moduladores", "dificuldade",
                 "comentario_fonte", "qualidade_fonte", "alertas", "figuras_fonte"]

MODULO_CHAVE = {"🧭": "panorama", "📚": "autores", "⚖️": "base_normativa", "🟣": "brasil", "🧠": "mnemonico",
                "😈": "para_dificultar", "🃏": "carta_manga"}


def registro(c, figs, sigla, passada, nota, wv):
    r = {k: c.get(k) for k in CAMPOS_ORIGEM}
    r.update({"materia": sigla, "passada": passada, "versao_folha": "Q-v3", "nota_destino": nota,
              "subtema": re.sub(r"^\W+\s*", "", c["subtema"]),
              "excerto": (tabela_aninhada(c["excerto_tabela"], 560) if c.get("excerto_tabela")
                          else c.get("excerto", "")),
              "modulos": [MODULO_CHAVE.get(rot.split()[0], rot) for rot, _ in c.get("modulos", [])],
              "autores": sorted(set(re.findall(r"rgb\(170, 85, 0\);\"><b>([^<]+)</b>",
                                               verso(c, figs, wv, "enex")))),
              "normas": c.get("normas", []), "temas_discursiva": c.get("temas_discursiva", []),
              "verso_html": sanear(verso(c, figs, wv, "enex"))})
    figuras = []
    for lado, ids in (("frente", c.get("frente_figuras", [])), ("verso", c.get("grafico_verso") or [])):
        for fid in ([ids] if isinstance(ids, str) else ids):
            info = figs.get(fid)
            figuras.append({"id": fid, "lado": lado, "tipo": info["tipo"], "fidelidade": info["fidelidade"],
                            "legenda": info["legenda"], "md5": info["md5"], "png": os.path.basename(info["png"]),
                            "spec": info["spec"]})
    r["figuras"] = figuras
    return r


def carregar_fonte(caminho):
    if caminho.endswith(".py"):
        return runpy.run_path(caminho)["CARDS"]
    with open(caminho, encoding="utf-8") as fh:
        return [json.loads(x) for x in fh if x.strip()]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("fonte")
    ap.add_argument("--titulo", required=True, help="ex.: 07-A-1 - Obj.")
    ap.add_argument("--nota", help="id da nota de destino (padrão: tirado do título)")
    ap.add_argument("--sigla", required=True)
    ap.add_argument("--passada", type=int, default=0)
    ap.add_argument("--specs", help="pasta com as specs das figuras")
    ap.add_argument("-o", "--saida", required=True)
    a = ap.parse_args()

    os.makedirs(a.saida, exist_ok=True)
    cards = carregar_fonte(a.fonte)
    figs = Figuras(a.specs, a.saida)
    nota = a.nota or a.titulo.split("-1 - Obj.")[0]
    base = re.sub(r"[^\w.-]+", "_", a.titulo.replace(" - Obj.", "-Obj"))

    corpo_enex = corpo_nota(cards, figs, "enex")
    corpo_html = corpo_nota(cards, figs, "html")
    usadas = [figs.cache[k] for k in figs.cache]
    with open(os.path.join(a.saida, base + ".enex"), "w", encoding="utf-8") as fh:
        fh.write(enex(a.titulo, corpo_enex, usadas))
    with open(os.path.join(a.saida, base + ".html"), "w", encoding="utf-8") as fh:
        fh.write(html_preview(a.titulo, corpo_html))
    _, wf, wv = tabela(cards, figs, "enex")
    with open(os.path.join(a.saida, f"{a.sigla}-Q_passada{a.passada:02d}.jsonl"), "w", encoding="utf-8") as fh:
        for c in cards:
            fh.write(json.dumps(registro(c, figs, a.sigla, a.passada, nota, wv), ensure_ascii=False) + "\n")
    for e in figs.erros:
        print("ERRO figura:", e)
    print(f"{len(cards)} cards · {len(usadas)} figuras · colunas {wf}|{wv} px → {a.saida}")
    return 1 if figs.erros else 0


if __name__ == "__main__":
    sys.exit(main())
