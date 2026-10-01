#!/usr/bin/env python3
import json, sys
ent, sai = sys.argv[1], sys.argv[2]
P = json.load(open("ECO-Q_plano.json"))
H2 = {n["id"]: set(n["h2"]) for n in P["notas"]}
rids = [json.loads(l)["rid"] for l in open(ent) if l.strip()]
erros = []
try:
    out = [json.loads(l) for l in open(sai) if l.strip()]
except Exception as e:
    print("JSON inválido:", e); sys.exit(1)
if [o.get("rid") for o in out] != rids:
    falt = set(rids) - {o.get("rid") for o in out}
    erros.append(f"rids não batem com a entrada (faltam {len(falt)}: {sorted(falt)[:5]}…; ordem tem de ser a mesma)")
for o in out:
    r = o.get("rid")
    for k in ("nao_questao", "banca", "prova", "ano", "cacd", "errei", "itens", "figura_frente", "triagem", "obs"):
        if k not in o: erros.append(f"{r}: falta {k}")
    if o.get("figura_frente") not in ("nenhuma", "transcrita_ok", "transcrita_insuficiente", "ausente_deduzivel", "ausente_irrecuperavel"):
        erros.append(f"{r}: figura_frente inválida")
    if not o.get("nao_questao") and not o.get("itens"):
        erros.append(f"{r}: questão sem itens")
    for it in o.get("itens", []):
        if it.get("tipo") not in ("C/E", "ME", "EXERC", "DISC"): erros.append(f"{r}: tipo inválido {it.get('tipo')}")
        g = it.get("gabarito")
        if g not in ("CERTO", "ERRADO", "ANULADO", "RESPOSTA", "?", "A", "B", "C", "D", "E"): erros.append(f"{r}: gabarito inválido {g}")
        d = it.get("destino")
        if d != "TRIAGEM":
            if d not in H2: erros.append(f"{r}: destino inválido {d}")
            elif it.get("h2") not in H2[d]: erros.append(f"{r}: h2 '{it.get('h2')}' não pertence à nota {d}")
        if not it.get("resumo"): erros.append(f"{r}: item sem resumo")
for e in erros[:40]: print(e)
print("OK" if not erros else f"{len(erros)} erro(s)")
sys.exit(1 if erros else 0)
