#!/usr/bin/env python3
"""Prepara os lotes de redação de uma passada: redacao_XX.jsonl (≤ N itens, sem partir linha bruta)
e pulados_auto.json (duplicatas e irrecuperáveis já decididos na Fase 0).

    python3 preparar_passada.py --passada 1 --tam 30
"""
import argparse, collections, glob, json, os

ap = argparse.ArgumentParser()
ap.add_argument("--passada", type=int, required=True)
ap.add_argument("--tam", type=int, default=30)
a = ap.parse_args()
plano = json.load(open("ECO-Q_plano.json", encoding="utf-8"))
notas_passada = next(p["notas"] for p in plano["passadas"] if p["n"] == a.passada)
ordem = {n: i for i, n in enumerate(notas_passada)}
brutos = {json.loads(l)["rid"]: json.loads(l) for l in open("brutos.jsonl", encoding="utf-8")}
cls = {}
for f in sorted(glob.glob("classif/saida_*.jsonl")):
    for l in open(f, encoding="utf-8"):
        if l.strip():
            o = json.loads(l); cls[o["rid"]] = o

dir_ = f"passada{a.passada:02d}"
for d in ("lotes", "cards", "specs", "pulados"):
    os.makedirs(os.path.join(dir_, d), exist_ok=True)

# versos das duplicatas, para fundir no item-alvo
dup_versos = collections.defaultdict(list)
pulados = []
linhas = collections.OrderedDict()  # rid -> itens a converter nesta passada
for rid, o in cls.items():
    for it in o.get("itens", []):
        if it["destino"] not in ordem:
            continue
        if it.get("dup_de"):
            alvo = it["dup_de"].split("#")[0]
            dup_versos[alvo].append({"rid": rid, "verso": brutos[rid]["verso"][:6000]})
            pulados.append({"rid": rid, "k": it["k"], "motivo": f"duplicata de {it['dup_de']}"})
            continue
        if o["figura_frente"] == "ausente_irrecuperavel":
            pulados.append({"rid": rid, "k": it["k"], "motivo": "irrecuperável: frente era imagem não preservada"})
            continue
        linhas.setdefault(rid, []).append(it)

regs = []
for rid, its in linhas.items():
    b, o = brutos[rid], cls[rid]
    regs.append({"rid": rid, "frente": b["frente"], "verso": b["verso"][:20000], "imgs": b["imagens"],
                 "classif": {k: o[k] for k in ("banca", "prova", "ano", "cacd", "errei", "figura_frente", "obs")}
                 | {"itens": its},
                 "versos_duplicatas": dup_versos.get(rid, []),
                 "_ordem": (min(ordem[i["destino"]] for i in its), rid)})
regs.sort(key=lambda r: r["_ordem"])
lotes, atual, n = [], [], 0
for r in regs:
    q = len(r["classif"]["itens"])
    if atual and n + q > a.tam:
        lotes.append(atual); atual, n = [], 0
    atual.append(r); n += q
if atual:
    lotes.append(atual)
for k, lote in enumerate(lotes, 1):
    with open(f"{dir_}/lotes/redacao_{k:02d}.jsonl", "w", encoding="utf-8") as fh:
        for r in lote:
            r = dict(r); r.pop("_ordem")
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
json.dump(pulados, open(f"{dir_}/pulados/pulados_auto.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)
print(len(regs), "linhas,", sum(len(r["classif"]["itens"]) for r in regs), "itens em", len(lotes), "lotes;",
      len(pulados), "pulados automáticos")
for k, lote in enumerate(lotes, 1):
    ds = collections.Counter(i["destino"] for r in lote for i in r["classif"]["itens"])
    print(f"  {k:02d}: {sum(ds.values())} itens {dict(ds)}")
