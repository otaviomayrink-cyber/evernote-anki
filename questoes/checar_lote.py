#!/usr/bin/env python3
"""Confere um arquivo de cards de redação antes da montagem da passada.

    python3 checar_lote.py lotes/ECO/passada01/cards/cards_03.py --plano lotes/ECO/ECO-Q_plano.json \
        --specs lotes/ECO/passada01/specs

Renderiza as figuras citadas, monta uma nota temporária e roda o contrato (verificar_q.py).
"""
import argparse
import json
import os
import runpy
import subprocess
import sys
import tempfile

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import montar_nota_q as M  # noqa: E402
from verificar_q import ALERTAS  # noqa: E402

OBRIG = ["id", "fonte_ref", "destino", "subtema", "tipo", "banca", "prova", "ano", "cacd", "errei", "comando",
         "rotulo_item", "assertiva", "gabarito", "gabarito_origem", "status", "anotada", "poucas", "destrinchando",
         "dissecando", "modulos", "tipo_erro", "moduladores", "dificuldade", "comentario_fonte", "qualidade_fonte",
         "figuras_fonte", "alertas"]

ap = argparse.ArgumentParser()
ap.add_argument("cards")
ap.add_argument("--plano", required=True)
ap.add_argument("--specs", required=True)
a = ap.parse_args()
plano = json.load(open(a.plano, encoding="utf-8"))
notas = {n["id"]: n for n in plano["notas"]}
cards = runpy.run_path(a.cards)["CARDS"]
erros = []
for c in cards:
    for k in OBRIG:
        if k not in c:
            erros.append(f"{c.get('id')}: falta o campo {k}")
    n = notas.get(c.get("destino"))
    if not n:
        erros.append(f"{c.get('id')}: destino inválido")
    elif c.get("subtema") not in n["h2"]:
        erros.append(f"{c.get('id')}: subtema fora do plano da nota {c.get('destino')}")
    if c.get("gabarito") == "ERRADO" and not c.get("reescrita"):
        erros.append(f"{c.get('id')}: ERRADO sem reescrita")
    for al in c.get("alertas", []):
        if not al.startswith(ALERTAS):
            print(f"aviso {c.get('id')}: alerta fora da lista vira 'nota_redacao:' na montagem: {al[:40]}")
    if len(c.get("modulos", [])) > 3:
        erros.append(f"{c.get('id')}: mais de 3 módulos")
for e in erros:
    print("✗", e)
if erros:
    sys.exit(1)
tmp = tempfile.mkdtemp()
figs = M.Figuras(a.specs, tmp)
corpo = M.corpo_nota(cards, figs, "enex")
for e in figs.erros:
    print("✗ figura", e)
arq = os.path.join(tmp, "teste.enex")
open(arq, "w", encoding="utf-8").write(M.enex("99-TESTE-1 - Obj.", corpo, list(figs.cache.values())))
r = subprocess.run([sys.executable, os.path.join(AQUI, "verificar_q.py"), arq], capture_output=True, text=True)
print(r.stdout.replace(arq + ": ", ""))
print(f"PNG das figuras para revisão visual: {os.path.join(tmp, 'figuras')}")
sys.exit(1 if (r.returncode or figs.erros) else 0)
