#!/usr/bin/env python3
"""Fase 0: extrai todas as linhas (cards) dos cadernos de ECO para brutos.jsonl.

Uso: python3 extrair_brutos.py "eco 1.html" eco2.md eco3.md -o brutos.jsonl
Cada registro: rid, caderno, nota_origem, secao, linha, frente, verso, errei, imagens.
"""
import argparse, json, re


def limpar(t):
    t = t.replace(" ", " ")
    t = re.sub(r"[ \t]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n", t)
    return t.strip()


def do_html(caminho, cad):
    from bs4 import BeautifulSoup
    s = open(caminho, encoding="utf-8").read()
    s = re.sub(r"data:[^\"')]+", "", s)
    soup = BeautifulSoup(s, "lxml")
    note = soup.find("en-note")
    for t in note(["style", "script", "icons", "svg"]):
        t.decompose()
    regs = []
    nota = ""
    n = 0
    # títulos de nota: textos soltos "NN.1 - Obj." fora de tabelas
    for el in note.find_all(["table", "h1", "h2", "div", "p"], recursive=True):
        if el.name != "table":
            if el.find_parent("table") is None and el.find("table") is None:
                tx = el.get_text(" ").strip()
                if re.match(r"^\d{2}\.\d+ - +Obj\.", tx):
                    nota = tx
            continue
        if el.find_parent("table") is not None:
            continue
        tb = el.find("tbody") or el
        for tr in tb.find_all("tr", recursive=False):
            tds = tr.find_all("td", recursive=False)
            if len(tds) < 2:
                continue
            lados = []
            imgs = []
            for k, td in enumerate(tds[:2]):
                td = BeautifulSoup(str(td), "lxml")
                for img in td.find_all("img"):
                    nome = img.get("src", "").replace("\\", "/").split("/")[-1]
                    imgs.append({"lado": "frente" if k == 0 else "verso", "ref": nome})
                    img.replace_with(f" [[IMG: {nome}]] ")
                for br in td.find_all("br"):
                    br.replace_with("\n")
                for b in td.find_all(["p", "div", "li", "h1", "h2", "h3", "h4"]):
                    b.insert_after("\n")
                lados.append(limpar(td.get_text()))
            n += 1
            regs.append({"rid": f"{cad}-{n:04d}", "caderno": cad, "nota_origem": nota, "secao": "",
                         "linha": n, "frente": lados[0], "verso": lados[1],
                         "errei": lados[0].lstrip("=* _").startswith("❌"), "imagens": imgs})
    return regs


def do_md(caminho, cad):
    regs = []
    nota = secao = ""
    for i, l in enumerate(open(caminho, encoding="utf-8"), 1):
        l = l.rstrip("\n")
        if l.startswith("## "):
            if re.match(r"## \d+ — ", l):
                nota, secao = l[3:].strip(), ""
            else:
                secao = l[3:].strip()
            continue
        if not l.startswith("| ") or l.startswith("| ---") or l.strip() == "|  |  |":
            continue
        corpo = l.strip()[2:]
        if corpo.endswith(" |"):
            corpo = corpo[:-2]
        partes = re.split(r"(?<!\\) \| ", corpo)
        frente, verso = partes[0], " | ".join(partes[1:])
        imgs = []
        for lado, txt in (("frente", frente), ("verso", verso)):
            for m in re.finditer(r"\[\[IMAGEM (\d+) · TIPO: ([^\]]+)\]\]", txt):
                imgs.append({"lado": lado, "ref": f"IMAGEM {m.group(1)}", "tipo": m.group(2).strip()})
        conv = lambda t: limpar(t.replace("<br>", "\n").replace("\\|", "|").replace("\\$", "$"))
        f, v = conv(frente), conv(verso)
        regs.append({"rid": f"{cad}-L{i:05d}", "caderno": cad, "nota_origem": nota, "secao": secao,
                     "linha": i, "frente": f, "verso": v,
                     "errei": f.lstrip("=*_ ").startswith("❌"), "imagens": imgs})
    return regs


ap = argparse.ArgumentParser()
ap.add_argument("html")
ap.add_argument("md", nargs=2)
ap.add_argument("-o", default="brutos.jsonl")
a = ap.parse_args()
regs = do_html(a.html, "E1") + do_md(a.md[0], "E2") + do_md(a.md[1], "E3")
with open(a.o, "w", encoding="utf-8") as fh:
    for r in regs:
        fh.write(json.dumps(r, ensure_ascii=False) + "\n")
import collections
print(len(regs), collections.Counter(r["caderno"] for r in regs), sum(r["errei"] for r in regs), "errei")
