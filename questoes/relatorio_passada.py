#!/usr/bin/env python3
"""Mini-relatório de passada (Especificação v2 §4.1) — todos os números saem do JSONL e dos pulados.

    python3 relatorio_passada.py --jsonl X.jsonl --pulados dir/ --plano plano.json --passada 1 -o relatorio.md
"""
import argparse, collections, glob, json, re

ap = argparse.ArgumentParser()
ap.add_argument("--jsonl", required=True)
ap.add_argument("--pulados", required=True)
ap.add_argument("--plano", required=True)
ap.add_argument("--passada", type=int, required=True)
ap.add_argument("--verificacao", default="")
ap.add_argument("-o", required=True)
a = ap.parse_args()
R = [json.loads(l) for l in open(a.jsonl, encoding="utf-8") if l.strip()]
P = []
for f in sorted(glob.glob(a.pulados + "/pulados_*.json")):
    P += json.load(open(f, encoding="utf-8"))
plano = json.load(open(a.plano, encoding="utf-8"))
notas = {n["id"]: n for n in plano["notas"]}
C = collections.Counter
L = [f"# 📋 ECO-Q — Passada {a.passada:02d}: mini-relatório", ""]
L += [f"**Cards: {len(R)}** em {len(set(r['nota_destino'] for r in R))} notas · "
      f"figuras: {len({f['md5'] for r in R for f in r.get('figuras', [])})} únicas, "
      f"{sum(len(r.get('figuras', [])) for r in R)} usos "
      f"(frente {sum(1 for r in R for f in r.get('figuras', []) if f['lado']=='frente')}, "
      f"verso {sum(1 for r in R for f in r.get('figuras', []) if f['lado']=='verso')}) · "
      f"itens não convertidos: {len(P)}", ""]
L += ["## Cards por nota", "", "| Nota | Cards | ❌ errei | Figuras |", "|---|---|---|---|"]
for nid in [n["id"] for n in plano["notas"]]:
    rs = [r for r in R if r["nota_destino"] == nid]
    if rs:
        L.append(f"| {nid} — {notas[nid]['titulo'][:55]} | {len(rs)} | {sum(r['errei'] for r in rs)} | "
                 f"{sum(len(r.get('figuras', [])) for r in rs)} |")
L += ["", "## Por banca e tipo", "", "| Banca | Cards |", "|---|---|"]
for k, v in C(r["banca"] for r in R).most_common():
    L.append(f"| {k} | {v} |")
L += ["", "| Tipo / gabarito | Cards |", "|---|---|"]
for k, v in sorted(C(r["tipo"] for r in R).items()):
    L.append(f"| {k} | {v} |")
for k, v in C(r["gabarito"] for r in R).most_common():
    L.append(f"| gabarito {k} | {v} |")
L += ["", "## Taxonomia (código principal)", "", "| Código | Cards |", "|---|---|"]
for k, v in C((r.get("tipo_erro") or ["—"])[0] for r in R).most_common():
    L.append(f"| {k} | {v} |")


def lista(titulo, filtro, campo=None):
    rs = [r for r in R if filtro(r)]
    L.extend(["", f"## {titulo} ({len(rs)})", ""])
    for r in rs:
        extra = ""
        if campo:
            al = [x for x in r.get("alertas", []) if x.startswith(campo)]
            extra = " — " + re.sub(r"\s+", " ", al[0])[:180] if al else ""
        L.append(f"- `{r['id']}` ({r['nota_destino']}, {r['banca']}) gabarito {r['gabarito']}{extra}")


lista("⚠️ Contestáveis / anulados", lambda r: r["status"] in ("contestavel", "anulado"), "contestavel")
lista("🔧 Gabaritos resolvidos (fonte sem gabarito)", lambda r: r["gabarito_origem"] == "resolvido")
lista("📄 Enunciados reconstruídos", lambda r: any(x.startswith("texto_reconstruido") for x in r.get("alertas", [])),
      "texto_reconstruido")
lista("📈 Figuras conjecturais (conferir com a prova)", lambda r: any(f["fidelidade"] == "conjectural" for f in r.get("figuras", [])),
      "figura_conjectural")
lista("⏳ Desatualizados", lambda r: r["status"] == "desatualizado")
L += ["", "## Qualidade da fonte", "", "| Qualidade | Cards |", "|---|---|"]
for k, v in C(r["qualidade_fonte"] for r in R).most_common():
    L.append(f"| {k} | {v} |")
L += ["", "## Alertas por tipo", "", "| Tipo | Ocorrências |", "|---|---|"]
for k, v in C(x.split(":")[0] for r in R for x in r.get("alertas", [])).most_common():
    L.append(f"| {k} | {v} |")
L += ["", f"## 🧹 Itens não convertidos ({len(P)})", ""]
mot = C(re.sub(r"\s.*", "", p["motivo"]).rstrip(":") for p in P)
for k, v in mot.most_common():
    L.append(f"- {k}: {v}")
L += [""] + [f"  - `{p['rid']}#{p['k']}` — {p['motivo'][:160]}" for p in P if not p["motivo"].startswith("duplicata")]
if a.verificacao:
    L += ["", "## Verificação", "", a.verificacao]
rest = [p for p in plano["passadas"] if p["n"] > a.passada]
L += ["", "## O que falta", ""] + [f"- Passada {p['n']:02d}: notas {', '.join(p['notas'])} ({p['itens']} itens)" for p in rest]
open(a.o, "w", encoding="utf-8").write("\n".join(L) + "\n")
print(f"relatório: {len(R)} cards, {len(P)} pulados → {a.o}")
