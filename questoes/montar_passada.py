#!/usr/bin/env python3
"""Monta uma passada inteira: uma nota -Q por destino + ENEX consolidado + JSONL + mini-relatório.

    python3 montar_passada.py --plano lotes/ECO/ECO-Q_plano.json --cards lotes/ECO/passada01/cards \
        --specs lotes/ECO/passada01/specs --passada 1 -o lotes/ECO/passada01/entrega

Cada card traz "destino" (id da nota) e "subtema" (H2 exato do plano).
"""
import argparse
import collections
import glob
import json
import os
import re
import runpy
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import montar_nota_q as M  # noqa: E402


def carregar_cards(pasta):
    cards = []
    for f in sorted(glob.glob(os.path.join(pasta, "cards_*.py"))):
        cs = runpy.run_path(f)["CARDS"]
        for c in cs:
            c["_arquivo"] = os.path.basename(f)
        cards += cs
    return cards


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--plano", required=True)
    ap.add_argument("--cards", required=True)
    ap.add_argument("--specs", required=True)
    ap.add_argument("--passada", type=int, required=True)
    ap.add_argument("--sigla", default="ECO")
    ap.add_argument("-o", "--saida", required=True)
    a = ap.parse_args()

    plano = json.load(open(a.plano, encoding="utf-8"))
    notas = {n["id"]: n for n in plano["notas"]}
    cards = carregar_cards(a.cards)
    ids = collections.Counter(c["id"] for c in cards)
    dup = [i for i, n in ids.items() if n > 1]
    if dup:
        raise SystemExit(f"ids duplicados: {dup[:10]}")
    from verificar_q import ALERTAS
    for c in cards:  # alertas fora da lista fechada viram nota_redacao (Especificação v2 §2)
        c["alertas"] = [a if a.startswith(ALERTAS) else "nota_redacao: " + a for a in c.get("alertas", [])]
    erros = []
    for c in cards:
        n = notas.get(c.get("destino"))
        if not n:
            erros.append(f"{c['id']}: destino inválido {c.get('destino')}")
        elif c["subtema"] not in n["h2"]:
            erros.append(f"{c['id']}: H2 '{c['subtema']}' fora do plano da nota {c['destino']}")
    if erros:
        print("\n".join(erros))
        raise SystemExit(1)

    os.makedirs(os.path.join(a.saida, "notas"), exist_ok=True)
    figs = M.Figuras(a.specs, a.saida)
    por_nota = collections.defaultdict(list)
    for c in cards:
        por_nota[c["destino"]].append(c)
    ordem_notas = [n["id"] for n in plano["notas"] if n["id"] in por_nota]
    xmls, regs = [], []
    for nid in ordem_notas:
        n = notas[nid]
        cs = sorted(por_nota[nid], key=lambda c: (n["h2"].index(c["subtema"]), M.ordem_banca(c)))
        corpo_e = M.corpo_nota(cs, figs, "enex")
        corpo_h = M.corpo_nota(cs, figs, "html")
        usadas = list(figs.cache.values())
        titulo = n["titulo_q"]
        base = titulo.replace(" - Obj.", "-Obj").replace(" ", "_")
        xml = M.nota_xml(titulo, corpo_e, usadas)
        xmls.append(xml)
        with open(os.path.join(a.saida, "notas", base + ".enex"), "w", encoding="utf-8") as fh:
            fh.write(M.enex_export([xml]))
        with open(os.path.join(a.saida, "notas", base + ".html"), "w", encoding="utf-8") as fh:
            fh.write(M.html_preview(titulo, corpo_h).replace('src="figuras/', 'src="../figuras/'))
        _, wf, wv = M.tabela(cs, figs, "enex")
        for c in cs:
            regs.append(M.registro(c, figs, a.sigla, a.passada, nid, wv))
    with open(os.path.join(a.saida, f"{a.sigla}-Q_passada{a.passada:02d}.enex"), "w", encoding="utf-8") as fh:
        fh.write(M.enex_export(xmls))
    with open(os.path.join(a.saida, f"{a.sigla}-Q_passada{a.passada:02d}.jsonl"), "w", encoding="utf-8") as fh:
        for r in regs:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    for e in figs.erros:
        print("ERRO figura:", e)
    print(f"{len(cards)} cards em {len(ordem_notas)} notas · {len(figs.cache)} figuras → {a.saida}")
    return 1 if figs.erros else 0


if __name__ == "__main__":
    sys.exit(main())
