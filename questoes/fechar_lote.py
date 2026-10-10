#!/usr/bin/env python3
"""Fase 2 — fecha o lote: une os JSONL das passadas no mestre, verifica e gera o Relatório do lote
(Especificação v2 §4.2, seções 1–6 e 6-bis) com todos os números calculados aqui.

    python3 fechar_lote.py --lote lotes/ECO --sigla ECO

Saídas em {lote}/fechamento/: {SIGLA}-Q_mestre.jsonl, {SIGLA}-Q_relatorio_do_lote.md (seções numéricas;
a seção 7 e as Lições são redigidas à parte a partir destes números) e {SIGLA}-Q_numeros.json.
"""
import argparse
import collections
import glob
import json
import os
import re
import sys

AQUI = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, AQUI)
import verificar_q  # noqa: E402

C = collections.Counter
BANCAS_PROVA = {"CEBRASPE", "FGV", "FCC", "ESAF", "CESGRANRIO", "VUNESP", "IADES", "Quadrix", "FEPESE", "ACEP"}


def limpo(h, n=110):
    t = re.sub(r"<[^>]+>", "", h or "")
    t = re.sub(r"\s+", " ", t).strip()
    return t[:n] + ("…" if len(t) > n else "")


def origem(r):
    if r.get("cacd"):
        return "CACD"
    if r["banca"] == "CEBRASPE":
        return "CEBRASPE (outros)"
    if r["banca"] in BANCAS_PROVA:
        return "outras bancas"
    if r["banca"] == "Banca não identificada":
        return "banca não identificada"
    return "cursos e professores"


def tabela(cab, linhas):
    out = ["| " + " | ".join(cab) + " |", "|" + "---|" * len(cab)]
    out += ["| " + " | ".join(str(x) for x in l) + " |" for l in linhas]
    return out


def pct(a, b):
    return f"{100 * a / b:.0f}%" if b else "—"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--lote", required=True)
    ap.add_argument("--sigla", required=True)
    a = ap.parse_args()
    plano = json.load(open(os.path.join(a.lote, f"{a.sigla}-Q_plano.json"), encoding="utf-8"))
    notas = {n["id"]: n for n in plano["notas"]}
    ordem = [n["id"] for n in plano["notas"]]
    out_dir = os.path.join(a.lote, "fechamento")
    os.makedirs(out_dir, exist_ok=True)

    R, pul = [], []
    for p in plano["passadas"]:
        d = os.path.join(a.lote, f"passada{p['n']:02d}")
        f = os.path.join(d, "entrega", f"{a.sigla}-Q_passada{p['n']:02d}.jsonl")
        R += [json.loads(l) for l in open(f, encoding="utf-8") if l.strip()]
        for g in glob.glob(os.path.join(d, "pulados", "*.json")):
            pul += json.load(open(g, encoding="utf-8"))
    mestre = os.path.join(out_dir, f"{a.sigla}-Q_mestre.jsonl")
    with open(mestre, "w", encoding="utf-8") as fh:
        for r in R:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    erros = []
    verificar_q.conferir_jsonl(mestre, erros, 0)
    # pulados únicos por item
    pk = {}
    for p in pul:
        pk.setdefault(f"{p['rid']}#{p['k']}", p["motivo"])

    N = len(R)
    L = [f"# 📊 Relatório do lote — {a.sigla}-Q", "",
         f"*Gerado por `fechar_lote.py` a partir de `{a.sigla}-Q_mestre.jsonl` ({N} cards, "
         f"{len(plano['passadas'])} passadas). Todos os números saem do script.*", ""]
    L += ["**Verificação do mestre (Especificação §5):** " + ("sem erros." if not erros else
                                                            f"{len(erros)} erro(s): " + "; ".join(erros[:5])), ""]

    # 1. Panorama
    L += ["## 1. Panorama", "", f"- Cards: **{N}** · itens não convertidos: **{len(pk)}** "
          f"(duplicatas {sum(1 for m in pk.values() if m.startswith('duplicata'))}, "
          f"irrecuperáveis {sum(1 for m in pk.values() if m.startswith('irrecup'))}) · "
          f"notas com cards: {len(set(r['nota_destino'] for r in R))} de {len(notas)}", ""]
    L += tabela(["Gabarito", "Cards", "%"], [(k, v, pct(v, N)) for k, v in C(r["gabarito"] for r in R).most_common()])
    L += [""] + tabela(["Tipo", "Cards"], sorted(C(r["tipo"] for r in R).items()))
    L += [""] + tabela(["Origem", "Cards", "%"], [(k, v, pct(v, N)) for k, v in C(origem(r) for r in R).most_common()])
    L += [""] + tabela(["Banca", "Cards"], C(r["banca"] for r in R).most_common(15))
    anos = C(r["ano"] for r in R if r.get("ano"))
    L += ["", "**Por ano** (cards com ano informado: " + str(sum(anos.values())) + "): " +
          " · ".join(f"{k}: {v}" for k, v in sorted(anos.items()))]
    cacd = [r for r in R if r.get("cacd")]
    L += ["", f"**CACD por edição** ({len(cacd)} cards): " +
          " · ".join(f"{k}: {v}" for k, v in sorted(C(r.get("ano") for r in cacd).items(), key=lambda x: str(x[0])))]

    # 2. Mapa temático
    L += ["", "## 2. Mapa temático", ""]
    linhas = []
    for nid in ordem:
        rs = [r for r in R if r["nota_destino"] == nid]
        if rs:
            linhas.append((f"{nid} — {notas[nid]['titulo'][:50]}", len(rs), sum(r["errei"] for r in rs),
                           pct(sum(1 for r in rs if r.get("cacd")), len(rs))))
    L += tabela(["Nota", "Cards", "❌ errei", "% CACD"], linhas)
    sub = C((r["nota_destino"], r["subtema"]) for r in R)
    L += ["", "**🔥 Os 15 subtemas mais cobrados**", ""]
    L += tabela(["#", "Nota", "Subtema", "Cards"], [(i + 1, n, s, v) for i, ((n, s), v) in enumerate(sub.most_common(15))])
    sem_nota = [n for n in ordem if not any(r["nota_destino"] == n for r in R)]
    L += ["", "**⬜ Lacunas — notas sem nenhum item:** " + (", ".join(f"{n} ({notas[n]['titulo'][:40]})" for n in sem_nota) or "nenhuma")]
    lac = []
    for nid in ordem:
        if nid in sem_nota:
            continue
        usados = {s for (n, s) in sub if n == nid}
        for h in notas[nid]["h2"]:
            if re.sub(r"^\W+\s*", "", h) not in usados:
                lac.append(f"{nid} › {h}")
    L += ["", "**⬜ H2 do plano sem nenhum item:** " + ("; ".join(lac) or "nenhum")]

    # 3. Como os itens são fabricados
    ce = [r for r in R if r["tipo"] in ("C/E", "ME")]
    L += ["", "## 3. Como os itens são fabricados", ""]
    cod = C((r.get("tipo_erro") or ["—"])[0] for r in ce)
    cod_c = C((r.get("tipo_erro") or ["—"])[0] for r in ce if r.get("cacd"))
    ex = {}
    for r in ce:
        k = (r.get("tipo_erro") or ["—"])[0]
        if k not in ex or (r.get("cacd") and not ex[k].get("cacd")):
            ex[k] = r
    L += tabela(["Código", "Cards", "% (C/E+ME)", "No CACD", "Exemplo"],
                [(k, v, pct(v, len(ce)), cod_c.get(k, 0), f"`{ex[k]['id']}` — {limpo(ex[k]['assertiva'], 90)}")
                 for k, v in cod.most_common()])
    mods = C(m.lower().strip() for r in ce for m in (r.get("moduladores") or []))
    L += ["", "**Moduladores mais frequentes e o gabarito associado** (C/E)", ""]
    linhas = []
    for m, v in mods.most_common(20):
        rs = [r for r in ce if m in [x.lower().strip() for x in (r.get("moduladores") or [])] and r["gabarito"] in ("CERTO", "ERRADO")]
        er = sum(1 for r in rs if r["gabarito"] == "ERRADO")
        linhas.append((f"“{m}”", v, f"ERRADO em {pct(er, len(rs))}"))
    L += tabela(["Modulador", "Ocorrências", "Gabarito típico"], linhas)

    # 4. Desempenho
    err = [r for r in R if r["errei"]]
    L += ["", "## 4. Seu desempenho (itens marcados ❌)", "",
          f"- Itens ❌: **{len(err)}** de {N} ({pct(len(err), N)})", ""]
    L += tabela(["Código (principal)", "❌", "Total", "Taxa de ❌"],
                sorted(((k, sum(1 for r in err if (r.get('tipo_erro') or ['—'])[0] == k), v,
                         pct(sum(1 for r in err if (r.get('tipo_erro') or ['—'])[0] == k), v))
                        for k, v in cod.items() if v >= 5), key=lambda x: -x[1] / x[2]))
    L += ["", "**Subtemas com mais ❌**", ""]
    L += tabela(["Nota", "Subtema", "❌", "Total"],
                [(n, s, v, sub[(n, s)]) for (n, s), v in C((r["nota_destino"], r["subtema"]) for r in err).most_common(12)])
    inst = sorted(err, key=lambda r: (-(r.get("cacd") or 0), -(r.get("dificuldade") or 1), r["gabarito"] != "ERRADO"))[:20]
    L += ["", "**Os 20 itens ❌ mais instrutivos para revisar** (CACD e difíceis primeiro)", ""]
    L += [f"{i + 1}. `{r['id']}` ({r['nota_destino']}, {r['gabarito']}, {', '.join(r.get('tipo_erro') or [])}) — "
          f"{limpo(r['assertiva'], 130)}" for i, r in enumerate(inst)]

    # 5. Polêmicos
    pol = [r for r in R if r["status"] in ("contestavel", "anulado", "alterado", "desatualizado")]
    L += ["", f"## 5. Polêmicos ({len(pol)})", ""]
    for st in ("anulado", "alterado", "desatualizado", "contestavel"):
        rs = [r for r in pol if r["status"] == st]
        if not rs:
            continue
        L += [f"**{st}** ({len(rs)})", ""]
        for r in rs:
            al = next((x for x in r.get("alertas", []) if x.startswith("contestavel")), "")
            L.append(f"- `{r['id']}` ({r['nota_destino']}, {r['banca']}{', ' + r['prova'] if r.get('prova') else ''}) "
                     f"gabarito {r['gabarito']}" + (f" — {limpo(al[12:], 170)}" if al else ""))
        L.append("")

    # 6. Qualidade da fonte
    L += ["## 6. Qualidade da fonte", ""]
    L += tabela(["Qualidade", "Cards", "%"], [(k, v, pct(v, N)) for k, v in C(r["qualidade_fonte"] for r in R).most_common()])
    L += [""] + tabela(["Origem do gabarito", "Cards"], C(r["gabarito_origem"] for r in R).most_common())
    L += [""] + tabela(["Alerta", "Ocorrências"], C(x.split(":")[0].strip() for r in R for x in r.get("alertas", [])).most_common())
    ce_err = C(r["banca"] for r in R if r["qualidade_fonte"] == "com_erro")
    L += ["", "**Comentários de origem com erro, por banca/curso:** " +
          " · ".join(f"{k}: {v} de {sum(1 for r in R if r['banca'] == k)}" for k, v in ce_err.most_common(8))]

    # 6-bis. Figuras
    fig = [(r, f) for r in R for f in r.get("figuras", [])]
    uniq = {f["md5"] for _, f in fig}
    L += ["", "## 6-bis. Figuras", "",
          f"- Figuras únicas: **{len(uniq)}** · usos em cards: {len(fig)} "
          f"(frente {sum(1 for _, f in fig if f['lado'] == 'frente')}, verso {sum(1 for _, f in fig if f['lado'] == 'verso')})",
          f"- Cards com figura na frente: {len({r['id'] for r, f in fig if f['lado'] == 'frente'})} · "
          f"conjecturais a conferir: {len({r['id'] for r, f in fig if f['fidelidade'] == 'conjectural'})}", ""]
    L += tabela(["Nota", "Cards com figura", "% da nota"],
                [(n, v, pct(v, sum(1 for r in R if r['nota_destino'] == n)))
                 for n, v in C(r["nota_destino"] for r in R if r.get("figuras")).most_common(12)])
    modelos = C((f["spec"].get("modelo") or ("dados" if f["spec"].get("tipo") == "dados" else
                ("paineis" if f["spec"].get("paineis") else "primitivas"))) for _, f in fig if f["lado"] == "verso")
    L += ["", "**Como os gráficos de verso foram feitos:** " + " · ".join(f"{k}: {v}" for k, v in modelos.most_common())]
    L += ["", "## 7. Sugestões para o prompt", "", "<!-- redigida à parte -->", ""]

    rel = os.path.join(out_dir, f"{a.sigla}-Q_relatorio_do_lote.md")
    open(rel, "w", encoding="utf-8").write("\n".join(L) + "\n")
    json.dump({"cards": N, "pulados": len(pk), "errei": len(err), "cacd": len(cacd), "polemicos": len(pol),
               "figuras_unicas": len(uniq), "codigos": dict(cod), "lacunas_notas": sem_nota},
              open(os.path.join(out_dir, f"{a.sigla}-Q_numeros.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=1)
    print(f"mestre: {N} cards → {mestre}\nrelatório → {rel}\nerros de verificação: {len(erros)}")
    for e in erros[:10]:
        print(" ", e)
    return 1 if erros else 0


if __name__ == "__main__":
    sys.exit(main())
