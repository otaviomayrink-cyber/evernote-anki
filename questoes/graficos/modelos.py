"""Modelos prontos do qgraf: atalhos que se expandem em curvas, pontos e áreas.

Uma spec com "modelo": "oferta_demanda" (etc.) recebe os parâmetros em "params"
e é expandida antes do desenho. Tudo o que a spec trouxer além disso (pontos,
áreas, setas, textos, checar) é acrescentado ao que o modelo gera, e o que vier
em "substituir" troca campos de curvas do modelo pelo id (ex.: mudar um rótulo).

Modelos: oferta_demanda · tributo · tarifa · is_lm · solow · fpp · monopolio
Fora deles, escreve-se a spec com primitivas (ver Protocolo de Gráficos).
"""
import copy


def _seg(cid, p1, p2, fam, rot, **kw):
    d = {"id": cid, "tipo": "reta", "p1": p1, "p2": p2, "familia": fam, "rotulo": rot}
    d.update(kw)
    return d


def _desloca(p, dx, dy):
    return [p[0] + dx, p[1] + dy]


# ------------------------------------------------------------------ oferta e demanda
def oferta_demanda(p):
    """params: deslocar {"D": "direita|esquerda", "S": "direita|esquerda"}, passo (2),
    nome_oferta ("S" ou "O"), eixos {"x","y"}, excedentes (bool, só sem deslocamento)."""
    passo = p.get("passo", 2.0)
    o = p.get("nome_oferta", "O")
    D = p.get("D", [[1, 9], [9, 1]])
    S = p.get("S", [[1, 1], [9, 9]])
    desl = p.get("deslocar", {})
    curvas, pontos, deslocs, checar = [], [], [], []
    sub = "₁" if desl else ""
    curvas.append(_seg("D1", *D, "demanda", "D" + sub, estado="inicial" if "D" in desl else None))
    curvas.append(_seg("S1", *S, "oferta", o + sub, estado="inicial" if "S" in desl else None))
    dD = {"direita": passo, "esquerda": -passo}.get(desl.get("D"), 0)
    dS = {"direita": passo, "esquerda": -passo}.get(desl.get("S"), 0)
    Dfin, Sfin = "D1", "S1"
    if dD:
        curvas.append(_seg("D2", _desloca(D[0], dD, 0), _desloca(D[1], dD, 0), "demanda", "D₂"))
        deslocs.append({"de": "D1", "para": "D2", "sentido": desl["D"], "posicao": 0.3})
        Dfin = "D2"
    if dS:
        curvas.append(_seg("S2", _desloca(S[0], dS, 0), _desloca(S[1], dS, 0), "oferta", o + "₂"))
        deslocs.append({"de": "S1", "para": "S2", "sentido": desl["S"], "posicao": 0.75})
        Sfin = "S2"
    pontos.append({"id": "E1", "intersecao": ["D1", "S1"], "rotulo": "E" + sub, "projetar": True,
                   "rotulo_x": "q" + sub, "rotulo_y": "p" + sub})
    if desl:
        pontos.append({"id": "E2", "intersecao": [Dfin, Sfin], "rotulo": "E₂", "projetar": True,
                       "rotulo_x": "q₂", "rotulo_y": "p₂"})
        if dD and not dS:
            checar += ["E2.x > E1.x", "E2.y > E1.y"] if dD > 0 else ["E2.x < E1.x", "E2.y < E1.y"]
        if dS and not dD:
            checar += ["E2.x > E1.x", "E2.y < E1.y"] if dS > 0 else ["E2.x < E1.x", "E2.y > E1.y"]
    areas = []
    if p.get("excedentes") and not desl:
        areas = [
            {"tipo": "poligono", "vertices": [[0, "E1.y"], "E1", [0, "D1(D1.xs[0])"]],
             "papel": "excedente_consumidor", "rotulo": "EC"},
            {"tipo": "poligono", "vertices": [[0, "E1.y"], "E1", [0, "S1(S1.xs[0])"]],
             "papel": "excedente_produtor", "rotulo": "EP"},
        ]
    return {"eixos": p.get("eixos", {"x": "q", "y": "p"}), "curvas": curvas, "pontos": pontos,
            "deslocamentos": deslocs, "areas": areas, "checar": checar}


# ------------------------------------------------------------------ tributo específico
def tributo(p):
    """Imposto específico t sobre o vendedor: O sobe t; cunha entre pc e pv; receita e peso morto.
    params: t (2), D, S (retas), nome_oferta."""
    t = p.get("t", 2.0)
    o = p.get("nome_oferta", "O")
    D = p.get("D", [[1, 9], [9, 1]])
    S = p.get("S", [[1, 1], [9, 9]])
    curvas = [
        _seg("D", *D, "demanda", "D"),
        _seg("S", *S, "oferta", o, estado="inicial"),
        _seg("St", _desloca(S[0], 0, t), _desloca(S[1], 0, t), "oferta", o + " + t"),
    ]
    pontos = [
        {"id": "E0", "intersecao": ["D", "S"], "rotulo": "E₀", "projetar": True, "rotulo_x": "q₀",
         "rotulo_y": "p₀"},
        {"id": "Ec", "intersecao": ["D", "St"], "projetar": True, "rotulo_x": "qₜ", "rotulo_y": "pc",
         "marcar": True},
        {"id": "Ev", "sobre": "S", "x": "Ec.x", "projetar": "y", "rotulo_y": "pv"},
    ]
    areas = [
        {"tipo": "poligono", "vertices": [[0, "Ec.y"], "Ec", "Ev", [0, "Ev.y"]],
         "papel": "receita_tributaria", "rotulo": "Receita", "rotulo_xy": ["Ec.x*0.3", "(Ec.y+Ev.y)/2"]},
        {"tipo": "poligono", "vertices": ["Ec", "E0", "Ev"], "papel": "peso_morto",
         "rotulo": "PM", "rotulo_xy": ["(Ec.x+Ev.x+E0.x)/3+0.15", "(Ec.y+Ev.y+E0.y)/3"]},
    ]
    setas = [{"de": ["Ec.x-0.15", "Ev.y"], "para": ["Ec.x-0.15", "Ec.y"], "cor": "vermelho",
              "estilo": "<|-|>", "rotulo": "t", "rotulo_desloc": [-20, -8], "espessura": 1.8}]
    return {"eixos": p.get("eixos", {"x": "q", "y": "p"}), "curvas": curvas, "pontos": pontos,
            "areas": areas, "setas": setas,
            "checar": ["Ec.x < E0.x", "Ec.y > E0.y", "Ev.y < E0.y", "abs((Ec.y-Ev.y)-%s) < 0.05" % t]}


# ------------------------------------------------------------------ tarifa (pequena economia aberta)
def tarifa(p):
    """params: pw (3), t (2), D, S. Mostra importações antes/depois, receita e peso morto."""
    pw, t = p.get("pw", 2.5), p.get("t", 1.5)
    o = p.get("nome_oferta", "O")
    D = p.get("D", [[0.5, 9.5], [9.5, 0.5]])
    S = p.get("S", [[0.5, 0.5], [9.5, 9.5]])
    curvas = [
        _seg("D", *D, "demanda", "D"),
        _seg("S", *S, "oferta", o + " doméstica" if p.get("rotulo_longo") else o),
        {"id": "Pw", "tipo": "horizontal", "y": pw, "familia": "referencia", "rotulo": "Pm"},
        {"id": "Pt", "tipo": "horizontal", "y": pw + t, "familia": "destaque", "rotulo": "Pm + t",
         "tracejada": True},
    ]
    pontos = [
        {"id": "A", "intersecao": ["S", "Pw"], "marcar": False, "projetar": "x", "rotulo_x": "q₁ˢ"},
        {"id": "B", "intersecao": ["D", "Pw"], "marcar": False, "projetar": "x", "rotulo_x": "q₁ᵈ"},
        {"id": "C", "intersecao": ["S", "Pt"], "marcar": False, "projetar": "x", "rotulo_x": "q₂ˢ"},
        {"id": "F", "intersecao": ["D", "Pt"], "marcar": False, "projetar": "x", "rotulo_x": "q₂ᵈ"},
    ]
    areas = [
        {"tipo": "poligono", "vertices": ["A", "C", [ "C.x", "Pw.ys[0]"]], "papel": "peso_morto"},
        {"tipo": "poligono", "vertices": [["F.x", "Pw.ys[0]"], "F", "B"], "papel": "peso_morto"},
        {"tipo": "poligono", "vertices": ["C", "F", ["F.x", "Pw.ys[0]"], ["C.x", "Pw.ys[0]"]],
         "papel": "receita_tributaria", "rotulo": "Receita"},
    ]
    return {"eixos": p.get("eixos", {"x": "q", "y": "p"}), "curvas": curvas, "pontos": pontos,
            "areas": areas, "checar": ["C.x > A.x", "F.x < B.x"]}


# ------------------------------------------------------------------ IS-LM
def is_lm(p):
    """params: deslocar {"IS": "direita|esquerda", "LM": ...}, passo (2), eixos (Y, i)."""
    passo = p.get("passo", 2.0)
    desl = p.get("deslocar", {})
    sub = "₁" if desl else ""
    IS = [[1.5, 9], [9, 1.5]]
    LM = [[1.5, 1.5], [9, 9]]
    curvas = [_seg("IS1", *IS, "demanda", "IS" + sub, estado="inicial" if "IS" in desl else None),
              _seg("LM1", *LM, "oferta", "LM" + sub, estado="inicial" if "LM" in desl else None)]
    deslocs, checar = [], []
    fin = {"IS": "IS1", "LM": "LM1"}
    for nome, base, pos in (("IS", IS, 0.3), ("LM", LM, 0.75)):
        if nome in desl:
            dx = passo if desl[nome] == "direita" else -passo
            fam = "demanda" if nome == "IS" else "oferta"
            curvas.append(_seg(nome + "2", _desloca(base[0], dx, 0), _desloca(base[1], dx, 0), fam,
                               nome + "₂"))
            deslocs.append({"de": nome + "1", "para": nome + "2", "sentido": desl[nome], "posicao": pos})
            fin[nome] = nome + "2"
    pontos = [{"id": "E1", "intersecao": ["IS1", "LM1"], "rotulo": "E" + sub, "projetar": True,
               "rotulo_x": "Y" + sub, "rotulo_y": "i" + sub}]
    if desl:
        pontos.append({"id": "E2", "intersecao": [fin["IS"], fin["LM"]], "rotulo": "E₂", "projetar": True,
                       "rotulo_x": "Y₂", "rotulo_y": "i₂"})
    return {"eixos": p.get("eixos", {"x": "Y", "y": "i"}), "curvas": curvas, "pontos": pontos,
            "deslocamentos": deslocs, "checar": checar}


# ------------------------------------------------------------------ Solow
def solow(p):
    """f(k) = A·k^α; investimento s·f(k); reta (n+δ)k. params: A, alfa, s, n_delta, ouro (bool)."""
    A, a = p.get("A", 3.0), p.get("alfa", 0.5)
    s, nd = p.get("s", 0.3), p.get("n_delta", 0.2)
    kstar = (s * A / nd) ** (1 / (1 - a))
    kg = (nd / (A * a)) ** (1 / (a - 1))
    xmax = p.get("xmax", round(max(kstar, kg if p.get("ouro") else 0) * 1.3, 1))
    ymax = p.get("ymax", A * xmax ** a * 1.08)
    f = f"{A}*x**{a}"
    curvas = [
        {"id": "f", "tipo": "funcao", "expr": f, "dominio": [0, xmax], "familia": "demanda", "rotulo": "f(k)"},
        {"id": "sf", "tipo": "funcao", "expr": f"{s}*{f}", "dominio": [0, xmax], "familia": "oferta",
         "rotulo": "s·f(k)"},
        {"id": "dep", "tipo": "funcao", "expr": f"{nd}*x", "dominio": [0, xmax], "familia": "terceira",
         "rotulo": "(n+δ)k"},
    ]
    pontos = [{"id": "E", "intersecao": ["sf", "dep"], "indice": 1, "rotulo": "", "projetar": "x",
               "rotulo_x": "k*"}]
    out = {"eixos": {"x": "k", "y": "y", "xmax": xmax, "ymax": ymax},
           "curvas": curvas, "pontos": pontos, "checar": []}
    if p.get("ouro"):
        # k_ouro: f'(k) = n+δ  →  A·α·k^(α−1) = nδ
        out["pontos"].append({"id": "G", "sobre": "f", "x": kg, "projetar": "x", "rotulo_x": "k*ouro",
                              "marcar": True})
        out["pontos"].append({"id": "Gd", "sobre": "dep", "x": kg, "marcar": True})
        out["setas"] = [{"de": "Gd", "para": "G", "cor": "vermelho", "rotulo": "c* máximo",
                         "estilo": "<|-|>", "rotulo_desloc": [6, 0]}]
        out["checar"].append("abs(G.x - %f) < 1e-6" % kg)
    return out


# ------------------------------------------------------------------ FPP
def fpp(p):
    """Fronteira de possibilidades de produção côncava. params: expandir (bool), pontos extras."""
    curvas = [{"id": "F1", "tipo": "funcao", "expr": "sqrt(maximum(0, 64 - x**2))", "dominio": [0, 8],
               "familia": "demanda", "rotulo": "FPP" + ("₁" if p.get("expandir") else ""),
               "rotulo_em": 5.6, "rotulo_desloc": [6, 6], "estado": "inicial" if p.get("expandir") else None}]
    desl = []
    if p.get("expandir"):
        curvas.append({"id": "F2", "tipo": "funcao", "expr": "sqrt(maximum(0, 90 - x**2))",
                       "dominio": [0, 9.4868], "familia": "demanda", "rotulo": "FPP₂", "rotulo_em": 7,
                       "rotulo_desloc": [6, 6]})
        desl.append({"de": "F1", "para": "F2", "em_x": 4})
    return {"eixos": p.get("eixos", {"x": "bem X", "y": "bem Y"}), "curvas": curvas,
            "deslocamentos": desl, "pontos": [], "checar": []}


# ------------------------------------------------------------------ monopólio
def monopolio(p):
    """Demanda linear P = a − b·q; RMg = a − 2b·q; CMg constante c."""
    a, b, c = p.get("a", 9.0), p.get("b", 1.0), p.get("c", 3.0)
    curvas = [
        {"id": "D", "tipo": "funcao", "expr": f"{a}-{b}*x", "dominio": [0, a / b], "familia": "demanda",
         "rotulo": "D = RMe", "rotulo_em": a / b * 0.82, "rotulo_desloc": [6, 10]},
        {"id": "RMg", "tipo": "funcao", "expr": f"{a}-{2 * b}*x", "dominio": [0, a / (2 * b)],
         "familia": "quarta", "rotulo": "RMg"},
        {"id": "CMg", "tipo": "horizontal", "y": c, "familia": "oferta", "rotulo": "CMg = CMe"},
    ]
    pontos = [
        {"id": "Q", "intersecao": ["RMg", "CMg"], "projetar": "x", "rotulo_x": "qm", "marcar": False},
        {"id": "M", "sobre": "D", "x": "Q.x", "rotulo": "M", "projetar": True, "rotulo_y": "pm"},
        {"id": "C", "intersecao": ["D", "CMg"], "rotulo": "C", "projetar": "x", "rotulo_x": "qc",
         "rotulo_desloc": [6, 12]},
    ]
    areas = [{"tipo": "poligono", "vertices": ["M", ["Q.x", c], "C"], "papel": "peso_morto", "rotulo": "PM",
              "rotulo_xy": ["(M.x+Q.x+C.x)/3", "(M.y+%f+C.y)/3" % c]}]
    return {"eixos": p.get("eixos", {"x": "q", "y": "p"}), "curvas": curvas, "pontos": pontos,
            "areas": areas, "checar": ["M.y > C.y", "Q.x < C.x"],
            "_xmax": a / b * 1.05}


MODELOS = {"oferta_demanda": oferta_demanda, "tributo": tributo, "tarifa": tarifa, "is_lm": is_lm,
           "solow": solow, "fpp": fpp, "monopolio": monopolio}


def expandir_modelo(spec):
    """Expande spec['modelo'] (também dentro de spec['paineis'])."""
    if spec.get("paineis"):
        spec["paineis"] = [expandir_modelo(p) for p in spec["paineis"]]
        return spec
    nome = spec.get("modelo")
    if not nome:
        return spec
    if nome not in MODELOS:
        raise ValueError(f"modelo desconhecido: {nome} (disponíveis: {', '.join(MODELOS)})")
    base = MODELOS[nome](spec.get("params", {}))
    xmax = base.pop("_xmax", None)
    out = copy.deepcopy(spec)
    eixos = dict(base.get("eixos", {}))
    if xmax:
        eixos["xmax"] = xmax
    eixos.update(spec.get("eixos", {}))
    out["eixos"] = eixos
    for campo in ("curvas", "pontos", "areas", "setas", "deslocamentos", "textos", "checar"):
        out[campo] = base.get(campo, []) + spec.get(campo, [])
    # substituições pontuais por id (rótulos, posições)
    for cid, mud in spec.get("substituir", {}).items():
        for campo in ("curvas", "pontos"):
            for el in out[campo]:
                if el.get("id") == cid:
                    el.update(mud)
    # remoções por id
    for cid in spec.get("remover", []):
        for campo in ("curvas", "pontos", "areas"):
            out[campo] = [el for el in out[campo] if el.get("id") != cid]
    return out
