#!/usr/bin/env python3
"""Consolida a classificação: mapa de itens (CSV), plano de passadas (JSON) e relatório da Fase 0 (MD)."""
import collections, csv, glob, json

brutos = {json.loads(l)["rid"]: json.loads(l) for l in open("brutos.jsonl", encoding="utf-8")}
cls = {}
for f in sorted(glob.glob("classif/saida_*.jsonl")):
    for l in open(f, encoding="utf-8"):
        if l.strip():
            o = json.loads(l); cls[o["rid"]] = o
plano = json.load(open("ECO-Q_plano.json", encoding="utf-8"))
notas = {n["id"]: n for n in plano["notas"]}
faltam = [r for r in brutos if r not in cls]

itens = []
for rid, b in brutos.items():
    o = cls.get(rid)
    if not o:
        continue
    for it in o.get("itens", []):
        itens.append({
            "item": f"ECO-{rid}-{it['k']}", "rid": rid, "k": it["k"], "caderno": b["caderno"],
            "origem": (b["nota_origem"] + (" / " + b["secao"] if b["secao"] else ""))[:80],
            "destino": it["destino"], "h2": it.get("h2", ""), "tipo": it["tipo"], "banca": o["banca"],
            "prova": o["prova"], "ano": o["ano"], "cacd": o["cacd"], "errei": o["errei"],
            "gabarito": it["gabarito"], "resumo": it["resumo"], "dup_de": it.get("dup_de") or "",
            "figura_frente": o["figura_frente"], "triagem": o.get("triagem") or "", "obs": o.get("obs", "")})

with open("ECO-Q_mapa_de_itens.csv", "w", newline="", encoding="utf-8-sig") as fh:
    w = csv.DictWriter(fh, list(itens[0].keys()))
    w.writeheader(); w.writerows(itens)

uteis = [i for i in itens if not i["dup_de"] and i["destino"] != "TRIAGEM"
         and i["figura_frente"] != "ausente_irrecuperavel"]
por_nota = collections.Counter(i["destino"] for i in uteis)
# passadas: blocos do índice, 600–800 itens, sem quebrar nota
passadas, atual, n_atual = [], [], 0
ordem = [n["id"] for n in plano["notas"]]
for nid in ordem:
    q = por_nota.get(nid, 0)
    if not q:
        continue
    if n_atual and n_atual + q > 800 and n_atual >= 450:
        passadas.append((atual, n_atual)); atual, n_atual = [], 0
    atual.append(nid); n_atual += q
if atual:
    passadas.append((atual, n_atual))
plano["passadas"] = [{"n": k + 1, "notas": ns, "itens": q} for k, (ns, q) in enumerate(passadas)]
json.dump(plano, open("ECO-Q_plano.json", "w", encoding="utf-8"), ensure_ascii=False, indent=1)

# relatório
C = collections.Counter
nq = sum(1 for o in cls.values() if o.get("nao_questao"))
L = ["# 📋 ECO — Fase 0: diagnóstico e plano", "",
     f"Linhas brutas: **{len(brutos)}** (E1 {sum(1 for b in brutos.values() if b['caderno']=='E1')} · "
     f"E2 {sum(1 for b in brutos.values() if b['caderno']=='E2')} · E3 {sum(1 for b in brutos.values() if b['caderno']=='E3')})"
     + (f" — ⚠️ {len(faltam)} sem classificação" if faltam else ""),
     f"Não-questões: **{nq}** · itens julgáveis após desmembramento: **{len(itens)}**",
     f"Duplicatas (fundidas no 1º): **{sum(1 for i in itens if i['dup_de'])}** · Triagem: **{sum(1 for i in itens if i['destino']=='TRIAGEM')}**"
     f" · frente irrecuperável: **{sum(1 for i in itens if i['figura_frente']=='ausente_irrecuperavel')}**",
     f"**Itens a converter: {len(uteis)}**", "",
     "## (a) Inventário", "", "| Recorte | Itens |", "|---|---|"]
for k, v in C(i["tipo"] for i in itens).most_common(): L.append(f"| tipo {k} | {v} |")
for k, v in C(i["banca"] for i in itens).most_common(15): L.append(f"| {k} | {v} |")
L.append(f"| CACD | {sum(1 for i in itens if i['cacd'])} |")
L.append(f"| marcados ❌ | {sum(1 for i in itens if i['errei'])} |")
for k, v in C(i["gabarito"] for i in itens).most_common(): L.append(f"| gabarito {k} | {v} |")
for k, v in C(i["figura_frente"] for i in itens).most_common(): L.append(f"| figura na frente: {k} | {v} |")
L += ["", "## (b) Mapa de destino", "", "| Nota | Itens | H2 com itens |", "|---|---|---|"]
for nid in ordem:
    q = por_nota.get(nid, 0)
    h2 = C(i["h2"] for i in uteis if i["destino"] == nid)
    L.append(f"| {nid} — {notas[nid]['titulo'][:60]} | {q} | " + "; ".join(f"{h} ({c})" for h, c in h2.most_common()) + " |")
tri = [i for i in itens if i["destino"] == "TRIAGEM" and not i["dup_de"]]
L += ["", f"### 🧹 Triagem ({len(tri)})", ""]
for k, v in C((i["h2"] or "sem sugestão") for i in tri).most_common():
    L.append(f"- {k}: {v}")
L += ["", "## (c) Problemas", "",
      f"- Frente com imagem perdida e deduzível (E1): {sum(1 for i in itens if i['figura_frente']=='ausente_deduzivel')}",
      f"- Frente irrecuperável (fica de fora): {sum(1 for i in itens if i['figura_frente']=='ausente_irrecuperavel')}",
      f"- Transcrição de figura insuficiente: {sum(1 for i in itens if i['figura_frente']=='transcrita_insuficiente')}",
      f"- Gabarito a resolver na redação (`?`): {sum(1 for i in itens if i['gabarito']=='?')}", "",
      "## (d) Plano de passadas", "", "| Passada | Notas | Itens |", "|---|---|---|"]
for p in plano["passadas"]:
    L.append(f"| {p['n']:02d} | {', '.join(p['notas'])} | {p['itens']} |")
L += ["", "Notas sem nenhum item (lacunas): " + ", ".join(n for n in ordem if not por_nota.get(n))]
open("ECO-Q_fase0_relatorio.md", "w", encoding="utf-8").write("\n".join(L) + "\n")
print("\n".join(L[:12])); print("passadas:", [(p["n"], p["itens"]) for p in plano["passadas"]])
