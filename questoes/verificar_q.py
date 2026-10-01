#!/usr/bin/env python3
"""Confere notas -Q (ENEX) e o JSONL contra o contrato da Folha -Q v3 (§9) e a Especificação v2 (§5).

    python3 verificar_q.py saida/*.enex --jsonl saida/ECO-Q_passada00.jsonl

Sai com código 1 se houver qualquer violação.
"""
import argparse
import hashlib
import base64
import json
import re
import sys
import xml.etree.ElementTree as ET

TAXONOMIA = {"MEIA_VERDADE", "TROCA_CONCEITO", "TROCA_ATOR", "DADO_ALTERADO", "GENERALIZACAO", "RESTRICAO",
             "INVERSAO", "NEXO_INDEVIDO", "ANACRONISMO", "EXTRAPOLACAO", "CONTRADICAO", "JUIZO_INDEVIDO",
             "NORMA_VIOLADA", "SENTIDO_ALTERADO", "OUTRO", "PARAFRASE_FIEL", "LITERAL", "CONTRAINTUITIVO",
             "MODULADOR_RELATIVO", "EXCECAO", "DETALHE"}
ROTULOS_TAX = ["meia-verdade", "troca de conceito", "troca de ator", "dado alterado", "modulador absoluto",
               "restrição indevida", "inversão", "nexo indevido", "anacronismo", "extrapolação", "contradição",
               "juízo indevido", "norma violada", "sentido alterado", "outro:", "paráfrase fiel", "literalidade",
               "contraintuitivo", "modulador relativo", "exceção", "detalhe"]
AZUL, VERM = "rgb(0, 60, 200)", "rgb(200, 0, 0)"
MODULOS = ["🧭", "📚", "⚖️ Base", "🟣", "🧠", "😈", "🃏"]
BANDEIRA = re.compile("[\U0001F1E6-\U0001F1FF]{2}")
PROIBIDOS = ["o texto acima", "questão anterior", "[[IMAGEM", "[Imagem não", "caderno-fonte", "na conversão"]
ALERTAS = ("contestavel", "texto_parcial", "texto_irrecuperavel", "texto_reconstruido", "banca_confirmada",
           "banca_provavel", "destino_sugerido", "redirecionado", "duplicata", "figura_conjectural",
           "figura_irrecuperavel", "transcricao_incoerente", "teste_importacao", "qualidade_fonte",
           "quase_duplicata", "texto_corrigido", "dado_aproximado", "nota_redacao")


def serial(el):
    return ET.tostring(el, encoding="unicode")


def tabelas_topo(el, dentro_td=False):
    """Tabelas que não estão dentro de outra célula (as de cards)."""
    out = []
    for f in el:
        if f.tag == "table" and not dentro_td:
            out.append(f)
            continue
        out += tabelas_topo(f, dentro_td or f.tag == "td")
    return out


def conferir_enex(caminho, erros):
    def err(msg):
        erros.append(f"{caminho}: {msg}")

    bruto = open(caminho, encoding="utf-8").read()
    try:
        raiz = ET.fromstring(bruto.encode("utf-8"))
    except ET.ParseError as e:
        err(f"ENEX não é XML válido: {e}")
        return 0
    n_cards = 0
    for note in raiz.findall("note"):
        titulo = note.findtext("title", "")
        if not re.fullmatch(r"[\w-]+-1 - Obj\.", titulo):
            err(f"título fora do padrão {{id}}-1 - Obj.: {titulo!r}")
        if note.findall("tag"):
            err(f"{titulo}: nota com tags")
        cont = note.findtext("content", "")
        if "&nbsp;" in cont or "<style" in cont or "class=" in cont or "<mark" in cont or "<img" in cont:
            err(f"{titulo}: marcação proibida (&nbsp;/<style>/class=/<mark>/<img>)")
        if "<th" in cont or "<thead" in cont:
            err(f"{titulo}: <th>/<thead> na nota")
        if BANDEIRA.search(cont):
            err(f"{titulo}: emoji de bandeira")
        xml = re.sub(r"^<\?xml[^>]*\?>\s*<!DOCTYPE[^>]*>", "", cont.strip())
        try:
            en = ET.fromstring(xml.encode("utf-8"))
        except ET.ParseError as e:
            err(f"{titulo}: conteúdo não é XML válido: {e}")
            continue
        # recursos ↔ en-media
        hashes = set()
        for r in note.findall("resource"):
            dados = base64.b64decode(r.findtext("data", ""))
            hashes.add(hashlib.md5(dados).hexdigest())
        medias = [m.get("hash") for m in en.iter("en-media")]
        for h in medias:
            if h not in hashes:
                err(f"{titulo}: en-media {h} sem <resource>")
        for h in hashes - set(medias):
            err(f"{titulo}: <resource> {h} não usado")
        # blocos
        filhos = list(en)
        tags = [f.tag for f in filhos]
        h1 = [f for f in filhos if f.tag == "h1"]
        if len(h1) < 2 or "Índice" not in "".join(h1[0].itertext()) or "Questões" not in "".join(h1[1].itertext()):
            err(f"{titulo}: H1 fora da ordem 📍 Índice → ❓ Questões")
        if "hr" not in tags[tags.index("h1"):tags.index("h1", 1) + 1 if tags.count("h1") > 1 else None]:
            err(f"{titulo}: falta <hr/> entre Índice e Questões")
        # índice × H2
        h2s, contagem, atual = [], {}, None
        for f in filhos:
            if f.tag == "h2":
                atual = "".join(f.itertext())
                h2s.append(atual)
                contagem[atual] = 0
            elif f.tag in ("div", "table"):
                tabs = [f] if f.tag == "table" else tabelas_topo(f)
                for t in tabs:
                    if atual is None:
                        err(f"{titulo}: tabela fora de H2")
                    else:
                        contagem[atual] += len(t.find("tbody").findall("tr"))
        indice = [ "".join(li.itertext()) for li in filhos[tags.index("ul")].findall("li")] if "ul" in tags else []
        for h in h2s:
            if f"{h} ({contagem[h]})" not in indice:
                err(f"{titulo}: índice não traz '{h} ({contagem[h]})'")
        # tabelas e cards
        for t in tabelas_topo(en):
            st = t.get("style", "")
            if "table-layout:fixed" not in st.replace(" ", "") or "width:1400px" not in st.replace(" ", ""):
                err(f"{titulo}: tabela sem table-layout:fixed/1400px")
            cg = t.find("colgroup")
            if cg is None:
                err(f"{titulo}: tabela sem <colgroup>")
                continue
            ws = [int(re.search(r"width:(\d+)px", c.get("style")).group(1)) for c in cg.findall("col")]
            if len(ws) != 2 or sum(ws) != 1400:
                err(f"{titulo}: colgroup {ws} (precisa 2 colunas somando 1400)")
            tb = t.find("tbody")
            if tb is None:
                err(f"{titulo}: tabela sem <tbody>")
                continue
            for i, tr in enumerate(tb.findall("tr")):
                n_cards += 1
                tds = tr.findall("td")
                if len(tds) != 2:
                    err(f"{titulo}: linha {i + 1} com {len(tds)} células")
                    continue
                for td, w in zip(tds, ws):
                    if f"width:{w}px" not in td.get("style", "").replace(" ", ""):
                        err(f"{titulo}: td sem largura {w}px")
                conferir_card(titulo, i + 1, serial(tds[0]), serial(tds[1]), ws, err)
    return n_cards


def conferir_card(titulo, n, f, v, ws, err):
    tag = f"{titulo} card {n}"
    fi = re.sub(r"^<td[^>]*>", "", f)
    if not re.match(r"(❌ )?<code[^>]*>\[(C/E|ME|EXERC|DISC) - ", fi):
        err(f"{tag}: frente não começa pelo cabeçalho <code>[TIPO - …]")
    if "<p><br /></p>" not in fi[:fi.find("</code>") + 30].replace("<br/>", "<br />"):
        err(f"{tag}: cabeçalho sem <p><br/></p>")
    vi = re.sub(r"^<td[^>]*>", "", v)
    m = re.match(r"<p><span style=\"color: rgb\([^)]*\);\"><b>(✅ CERTO|❌ ERRADO|⚪ ANULADO|🔵 [^<]+)</b>", vi)
    if not m:
        err(f"{tag}: verso não começa pelo gabarito")
        return
    gab = m.group(1)
    hr = vi.find("<hr />")
    if hr < 0:
        err(f"{tag}: falta a linha de separação <hr/>")
        return
    anot = vi[:hr]
    if AZUL not in anot:
        err(f"{tag}: assertiva anotada sem trecho azul")
    vermelho_anot = anot.count(VERM) > (1 if gab == "❌ ERRADO" else 0)
    if gab == "✅ CERTO" and vermelho_anot:
        err(f"{tag}: CERTO com trecho vermelho na assertiva anotada")
    pos = [vi.find(x) for x in ("🎯 Em poucas palavras:", "📖 Destrinchando o tema:", "🧐 Dissecando a redação do item:")]
    if -1 in pos or pos != sorted(pos) or pos[0] < hr:
        err(f"{tag}: núcleo fora de ordem (🎯 → 📖 → 🧐 depois da separação)")
    if gab == "❌ ERRADO":
        if not vermelho_anot:
            err(f"{tag}: ERRADO sem trecho vermelho na assertiva anotada")
        ult = re.findall(r"<p><b>([^<]+)</b>", vi)
        if not ult or not ult[-1].startswith("✍️ Reescrita correta"):
            err(f"{tag}: ERRADO sem ✍️ Reescrita correta como último bloco")
    if gab in ("✅ CERTO", "❌ ERRADO") or gab.startswith("🔵 Letra"):
        dis = vi[pos[2]:] if pos[2] >= 0 else ""
        cinza = re.search(r"rgb\(160, 160, 160\);\">\[([^\]]+)\]", dis)
        if not cinza or not any(r in cinza.group(1) for r in ROTULOS_TAX):
            err(f"{tag}: 🧐 sem rótulo da taxonomia em cinza")
    n_mod = sum(vi.count(f"<p><b>{m}") for m in MODULOS)
    if n_mod > 3:
        err(f"{tag}: {n_mod} módulos opcionais (máx. 3)")
    if "😈 Para dificultar" in vi:
        bloco = vi[vi.find("😈 Para dificultar"):]
        bloco = bloco[:bloco.find("</ul>")]
        for li in re.findall(r"<li>(.*?)</li>", bloco):
            if "ERRADO" in li and not re.search(r"ERRADO \([^)]+\)\s*$", re.sub(r"<[^>]+>", "", li).strip()):
                err(f"{tag}: versão ERRADA do 😈 sem o erro entre parênteses")
    for x in PROIBIDOS:
        if x in f or x in v:
            err(f"{tag}: expressão proibida '{x}'")
    if re.search(r"ECO-E\d|[A-Z]{2,6}-E\d-L?\d{4}", re.sub(r"<en-media[^>]*>|<img[^>]*>", "", f + v)):
        err(f"{tag}: o texto cita outro card pelo id (o card é lido sozinho; ligação vai no alerta quase_duplicata)")
    for m in re.finditer(r"⏳([^<]{0,25})", f + v):
        if not re.search(r"\((jan|fev|mar|abr|mai|jun|jul|ago|set|out|nov|dez)/\d{4}\)", m.group(1)):
            err(f"{tag}: ⏳ sem data entre parênteses")
    # ---- figuras (Folha -Q v3 §10)
    for lado, txt, w in (("frente", f, ws[0]), ("verso", v, ws[1])):
        midias = list(re.finditer(r"<en-media[^>]*width=\"(\d+)\"[^>]*/>", txt))
        if len(midias) > 2:
            err(f"{tag}: {len(midias)} figuras na {lado} (máx. 2)")
        for m in midias:
            if int(m.group(1)) > w - 30:
                err(f"{tag}: figura de {m.group(1)}px numa coluna de {w}px")
            depois = txt[m.end():m.end() + 120]
            if not re.match(r"</div><p><span style=\"color: rgb\(160, 160, 160\);\"><i>.+", depois):
                err(f"{tag}: figura na {lado} sem legenda cinza em itálico logo abaixo")
        if "<en-media" in txt and "width=" not in txt[txt.find("<en-media"):txt.find("/>", txt.find("<en-media"))]:
            err(f"{tag}: en-media sem width")
    if "<en-media" in v:
        p_graf, p_dest, p_dis = v.find("📈 No gráfico:"), v.find("📖 Destrinchando"), v.find("🧐 Dissecando")
        if p_graf < 0:
            err(f"{tag}: figura no verso fora do bloco 📈 No gráfico")
        elif not (p_dest < p_graf < p_dis):
            err(f"{tag}: 📈 No gráfico fora do lugar (entre 📖 e 🧐)")


def conferir_jsonl(caminho, erros, n_cards):
    def err(msg):
        erros.append(f"{caminho}: {msg}")
    ids = set()
    regs = [json.loads(x) for x in open(caminho, encoding="utf-8") if x.strip()]
    obrig = ["id", "materia", "passada", "versao_folha", "nota_destino", "subtema", "tipo", "banca", "comando",
             "assertiva", "gabarito", "gabarito_origem", "status", "qualidade_fonte", "verso_html"]
    for r in regs:
        rid = r.get("id")
        if rid in ids:
            err(f"id duplicado {rid}")
        ids.add(rid)
        for k in obrig:
            if r.get(k) in (None, ""):
                err(f"{rid}: campo obrigatório vazio: {k}")
        if r["tipo"] not in ("C/E", "ME", "EXERC", "DISC"):
            err(f"{rid}: tipo inválido")
        if r["gabarito_origem"] not in ("fonte", "oficial", "resolvido"):
            err(f"{rid}: gabarito_origem inválido")
        if r["status"] not in ("normal", "contestavel", "anulado", "alterado", "desatualizado"):
            err(f"{rid}: status inválido")
        if r["qualidade_fonte"] not in ("bom", "raso", "com_erro", "ausente"):
            err(f"{rid}: qualidade_fonte inválida")
        if r["tipo"] in ("C/E", "ME"):
            te = r.get("tipo_erro") or []
            if not 1 <= len(te) <= 2 or any(t not in TAXONOMIA for t in te):
                err(f"{rid}: tipo_erro ausente ou fora da taxonomia: {te}")
        if r["status"] == "contestavel" and not any(a.startswith("contestavel") for a in r.get("alertas", [])):
            err(f"{rid}: status contestavel sem alerta")
        for a in r.get("alertas", []):
            if not a.startswith(ALERTAS):
                err(f"{rid}: alerta fora da lista: {a[:40]}")
        for fg in r.get("figuras", []):
            for k in ("id", "lado", "tipo", "fidelidade", "legenda", "md5", "spec"):
                if not fg.get(k):
                    err(f"{rid}: figura {fg.get('id')} sem {k}")
            if fg.get("fidelidade") not in ("fiel", "conjectural", "didatica"):
                err(f"{rid}: figura {fg.get('id')} com fidelidade inválida")
            if fg.get("fidelidade") == "conjectural" and not any(
                    a.startswith("figura_conjectural") for a in r.get("alertas", [])):
                err(f"{rid}: figura conjectural {fg['id']} sem alerta figura_conjectural")
            if fg.get("md5") and fg["md5"] not in r["verso_html"] and fg["lado"] == "verso":
                err(f"{rid}: figura de verso {fg['id']} não aparece no verso_html")
    if n_cards and len(regs) != n_cards:
        err(f"JSONL tem {len(regs)} registros e as notas têm {n_cards} cards")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("enex", nargs="+")
    ap.add_argument("--jsonl")
    a = ap.parse_args()
    erros = []
    n = sum(conferir_enex(e, erros) for e in a.enex)
    if a.jsonl:
        conferir_jsonl(a.jsonl, erros, n)
    for e in erros:
        print("✗", e)
    print(f"{n} cards conferidos · {len(erros)} violação(ões)")
    sys.exit(1 if erros else 0)


if __name__ == "__main__":
    main()
