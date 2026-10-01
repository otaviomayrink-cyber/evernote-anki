#!/usr/bin/env python3
"""Inventário das imagens dos cadernos de questões (Fase 0 do Protocolo de Gráficos).

    python3 inventariar_figuras.py --md caderno2.md caderno3.md --html caderno1.html -o saida/

Entradas:
  .md   — cadernos já convertidos, com imagens transcritas em [[IMAGEM n · TIPO: X]]…[[/IMAGEM n]]
  .html — exportação HTML do Evernote cujas imagens NÃO vieram (só sobra o <img src=…>)
Saídas:
  {SIGLA}-Q_figuras_inventario.csv — uma linha por (card, imagem): lado, tipo, ação sugerida
  {SIGLA}-Q_imagens_a_reenviar.csv — imagens de FRENTE sem transcrição (questão ilegível sem elas)
"""
import argparse
import collections
import csv
import os
import re

ACAO = {  # (lado, tipo) → ação sugerida (Folha -Q v3 §10.2)
    ("frente", "GRÁFICO"): "redesenhar (essencial)",
    ("frente", "DIAGRAMA"): "redesenhar (essencial)",
    ("frente", "MAPA"): "descrever em texto ou triagem",
    ("frente", "TABELA"): "tabela HTML aninhada",
    ("frente", "TEXTO"): "transcrever como texto",
    ("frente", "FÓRMULA"): "transcrever como texto",
    ("frente", "DECORATIVA"): "cortar",
    ("verso", "GRÁFICO"): "redesenho didático se passar no teste do quadro-negro; senão cortar",
    ("verso", "DIAGRAMA"): "redesenho didático se passar no teste do quadro-negro; senão cortar",
    ("verso", "MAPA"): "cortar (absorver no 📖)",
    ("verso", "TABELA"): "absorver no 📖 (lista ou tabela ≥ 3 colunas)",
    ("verso", "TEXTO"): "absorver no 📖 e cortar",
    ("verso", "FÓRMULA"): "transcrever como texto no 📖",
    ("verso", "DECORATIVA"): "cortar",
}


def linhas_md(caminho):
    """Linhas de tabela (cards) do .md, com a nota (##) a que pertencem."""
    nota = ""
    for i, l in enumerate(open(caminho, encoding="utf-8"), 1):
        if l.startswith("## "):
            nota = l[3:].strip()
        elif l.startswith("| ") and not l.startswith("| ---") and l.strip() != "|  |  |":
            yield i, nota, l


def do_md(caminho, rotulo):
    out = []
    for i, nota, l in linhas_md(caminho):
        partes = l.split(" | ")
        for lado, txt in (("frente", partes[0]), ("verso", " | ".join(partes[1:]))):
            for m in re.finditer(r"\[\[IMAGEM (\d+) · TIPO: ([^\]]+)\]\](.*?)\[\[/IMAGEM", txt):
                tipo = m.group(2).strip()
                out.append({"caderno": rotulo, "linha": i, "nota": nota, "ref": f"IMAGEM {m.group(1)}",
                            "lado": lado, "tipo_fonte": tipo, "transcrita": "sim",
                            "descricao": re.sub(r"\s+", " ", m.group(3).replace("<br>", " "))[:220],
                            "acao": ACAO.get((lado, tipo), "avaliar")})
    return out


def do_html(caminho, rotulo):
    from bs4 import BeautifulSoup
    texto = open(caminho, encoding="utf-8").read()
    texto = re.sub(r"data:[^\"')]+", "", texto)  # descarta fontes e ícones embutidos
    soup = BeautifulSoup(texto, "lxml")
    out = []
    nota = ""
    for el in soup.find("en-note").descendants:
        if getattr(el, "name", None) is None:
            s = str(el).strip()
            if re.match(r"^\d{2}\.\d - +Obj\.", s):
                nota = s
            continue
        if el.name != "img":
            continue
        td = el.find_parent("td")
        lado, contexto = "fora de card", ""
        if td is not None:
            tds = td.find_parent("tr").find_all("td", recursive=False)
            lado = "frente" if tds and tds[0] is td else "verso"
            irmao = tds[1] if lado == "frente" and len(tds) > 1 else tds[0]
            contexto = re.sub(r"\s+", " ", irmao.get_text(" "))[:220]
            so_imagem = lado == "frente" and len(re.sub(r"\W+", "", td.get_text())) < 40
        arq = el.get("src", "").replace("\\", "/").split("/")[-1]
        acao = ("REENVIAR imagem (frente só com imagem: enunciado ilegível)" if lado == "frente" and so_imagem
                else "REENVIAR imagem ou reconstruir pelo comentário" if lado == "frente"
                else "deduzir pelo comentário; redesenhar só se passar no teste do quadro-negro")
        out.append({"caderno": rotulo, "linha": "", "nota": nota, "ref": arq, "lado": lado,
                    "tipo_fonte": "?", "transcrita": "não", "descricao": "",
                    "contexto_outro_lado": contexto, "hash": el.get("data-resource-hash", ""), "acao": acao})
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--md", nargs="*", default=[])
    ap.add_argument("--html", nargs="*", default=[])
    ap.add_argument("--sigla", default="ECO")
    ap.add_argument("-o", "--saida", default=".")
    a = ap.parse_args()
    regs = []
    for k, c in enumerate(a.html, 1):
        regs += do_html(c, f"caderno{k} (html)")
    for k, c in enumerate(a.md, len(a.html) + 1):
        regs += do_md(c, f"caderno{k} (md)")
    campos = ["caderno", "nota", "linha", "ref", "lado", "tipo_fonte", "transcrita", "acao", "descricao",
              "contexto_outro_lado", "hash"]
    os.makedirs(a.saida, exist_ok=True)
    with open(os.path.join(a.saida, f"{a.sigla}-Q_figuras_inventario.csv"), "w", newline="",
              encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, campos, extrasaction="ignore")
        w.writeheader()
        w.writerows(regs)
    reenviar = [r for r in regs if r["acao"].startswith("REENVIAR")]
    vistos, unicos = set(), []
    for r in reenviar:
        if r["ref"] not in vistos:
            vistos.add(r["ref"])
            unicos.append(r)
    with open(os.path.join(a.saida, f"{a.sigla}-Q_imagens_a_reenviar.csv"), "w", newline="",
              encoding="utf-8-sig") as fh:
        w = csv.DictWriter(fh, ["nota", "ref", "hash", "acao", "contexto_outro_lado"], extrasaction="ignore")
        w.writeheader()
        w.writerows(unicos)
    # resumo
    c = collections.Counter((r["caderno"], r["lado"], r["tipo_fonte"]) for r in regs)
    for k in sorted(c):
        print(f"{k[0]:<18} {k[1]:<13} {k[2]:<11} {c[k]:>5}")
    print(f"total {len(regs)} ocorrências · {len(unicos)} imagens de frente a reenviar")


if __name__ == "__main__":
    main()
