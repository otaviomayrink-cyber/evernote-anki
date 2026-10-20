"""Junta os ENEX consolidados das passadas num único ENEX do lote, na ordem das notas do plano.

    python3 juntar_enex.py --plano lotes/ECO/ECO-Q_plano.json lotes/ECO/passada0*/entrega/ECO-Q_passada0*.enex \
        -o lotes/ECO/fechamento/ECO-Q_objetivas_consolidadas.enex
"""
import argparse, json, re
from montar_nota_q import enex_export

ap = argparse.ArgumentParser()
ap.add_argument("enex", nargs="+")
ap.add_argument("--plano", required=True)
ap.add_argument("-o", required=True)
a = ap.parse_args()

notas = {}
for f in a.enex:
    for n in re.findall(r"<note>.*?</note>", open(f, encoding="utf-8").read(), re.S):
        t = re.search(r"<title>(.*?)</title>", n).group(1)
        if t in notas:
            raise SystemExit(f"nota repetida entre passadas: {t}")
        notas[t] = n
ordem = [n["id"] for n in json.load(open(a.plano, encoding="utf-8"))["notas"]]
chave = lambda t: ordem.index(t.split("-1 - Obj.")[0]) if t.split("-1 - Obj.")[0] in ordem else len(ordem)
tit = sorted(notas, key=chave)
open(a.o, "w", encoding="utf-8").write(enex_export([notas[t] for t in tit]))
print(f"{len(tit)} notas → {a.o}")
