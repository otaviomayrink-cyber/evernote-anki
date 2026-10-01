#!/usr/bin/env python3
"""qgraf — gráficos das notas de questões (-Q) a partir de uma especificação JSON.

A IA escreve o CONTEÚDO do gráfico (curvas, pontos, áreas, rótulos) num JSON;
este script cuida do ESTILO (paleta, fontes, eixos) e da GEOMETRIA (interseções,
projeções, áreas). Também confere o gráfico: rótulos sobrepostos, curvas sem
rótulo, pontos que não existem e as "checagens" econômicas declaradas na spec
(ex.: "E2.y > E1.y" = o preço de equilíbrio subiu).

Uso:
    python3 qgraf.py spec.json [spec2.json ...] -o saida/      # gera PNG
    python3 qgraf.py specs/ -o saida/ --galeria                # + galeria.html
    python3 qgraf.py spec.json --checar                        # só confere

Formato da spec: ver questoes/docs/Protocolo_de_Graficos_v1.md
"""
import argparse
import copy
import html
import json
import math
import os
import sys

import numpy as np
import matplotlib

matplotlib.use("Agg")
import matplotlib.pyplot as plt  # noqa: E402
from matplotlib.patches import FancyArrowPatch, Polygon  # noqa: E402

try:
    from modelos import expandir_modelo
except ImportError:  # chamado de outro diretório
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    from modelos import expandir_modelo

# ---------------------------------------------------------------- paleta
# Mesmos RGB da Folha v9 §5.1; nos gráficos, a cor marca a FAMÍLIA da curva.
COR = {
    "azul": "#003CC8",      # rgb(0, 60, 200)
    "vermelho": "#C80000",  # rgb(200, 0, 0)
    "verde": "#008200",     # rgb(0, 130, 0)
    "ocre": "#AA5500",      # rgb(170, 85, 0)
    "roxo": "#8200A0",      # rgb(130, 0, 160)
    "cinza": "#A0A0A0",     # rgb(160, 160, 160)
    "texto": "#222222",
    "eixo": "#333333",
}
FAMILIA = {
    "demanda": COR["azul"],      # D, IS, DA, RMe, Lorenz, f(k)
    "oferta": COR["ocre"],       # S/O, LM, OA, custos, sf(k)
    "terceira": COR["roxo"],     # BP, CMe, restrição orçamentária, (n+δ)k
    "quarta": COR["verde"],      # 4ª curva: CVMe, RMg, isocusto
    "destaque": COR["vermelho"], # a curva que "muda o resultado"
    "referencia": COR["cinza"],  # linhas-guia, preço mundial, 45°
}
AREA = {  # preenchimentos suaves
    "excedente_consumidor": "#CFE0FF",
    "excedente_produtor": "#F5DEC0",
    "receita_tributaria": "#CDEBC8",
    "peso_morto": "#F8C9C9",
    "gasto": "#FFEF9E",
    "ganho": "#CDEBC8",
    "perda": "#F8C9C9",
    "neutro": "#E6E6E6",
    "roxo": "#E8D0F0",
}
TAMANHO = {"card": (8.0, 5.0), "baixo": (8.0, 2.6), "quadrado": (6.4, 5.4), "largo": (10.0, 5.2), "alto": (7.0, 6.4)}
DPI = 140
FONTE = "DejaVu Sans"

plt.rcParams.update({
    "font.family": FONTE,
    "font.size": 13,
    "mathtext.fontset": "dejavusans",
    "svg.fonttype": "none",
})


class ErroSpec(Exception):
    pass


# ---------------------------------------------------------------- geometria
class Ponto:
    def __init__(self, x, y):
        self.x, self.y = float(x), float(y)

    def __iter__(self):
        return iter((self.x, self.y))


class Curva:
    """Curva amostrada como polilinha (xs, ys)."""

    def __init__(self, cid, xs, ys):
        self.id = cid
        self.xs = np.asarray(xs, float)
        self.ys = np.asarray(ys, float)

    def __call__(self, x):  # y em x
        ys = _cruzamentos(self.xs, self.ys, float(x))
        if not ys:
            raise ErroSpec(f"curva {self.id} não passa por x={x}")
        return ys[0]

    def inv(self, y):  # x em y
        xs = _cruzamentos(self.ys, self.xs, float(y))
        if not xs:
            raise ErroSpec(f"curva {self.id} não passa por y={y}")
        return xs[0]


def _cruzamentos(us, vs, u0):
    """Valores de v onde a polilinha (u, v) atravessa u = u0."""
    out = []
    for i in range(len(us) - 1):
        a, b = us[i], us[i + 1]
        if (a - u0) * (b - u0) <= 0 and a != b:
            t = (u0 - a) / (b - a)
            out.append(vs[i] + t * (vs[i + 1] - vs[i]))
        elif a == b == u0:
            out.append(vs[i])
    return out


def intersecoes(c1, c2):
    """Todas as interseções entre duas polilinhas, ordenadas por x."""
    p = np.stack([c1.xs[:-1], c1.ys[:-1]], 1)
    r = np.stack([c1.xs[1:] - c1.xs[:-1], c1.ys[1:] - c1.ys[:-1]], 1)
    q = np.stack([c2.xs[:-1], c2.ys[:-1]], 1)
    s = np.stack([c2.xs[1:] - c2.xs[:-1], c2.ys[1:] - c2.ys[:-1]], 1)
    P, R = p[:, None, :], r[:, None, :]
    Q, S = q[None, :, :], s[None, :, :]
    rxs = R[..., 0] * S[..., 1] - R[..., 1] * S[..., 0]
    qp = Q - P
    with np.errstate(divide="ignore", invalid="ignore"):
        t = (qp[..., 0] * S[..., 1] - qp[..., 1] * S[..., 0]) / rxs
        u = (qp[..., 0] * R[..., 1] - qp[..., 1] * R[..., 0]) / rxs
    ok = (np.abs(rxs) > 1e-12) & (t >= -1e-9) & (t <= 1 + 1e-9) & (u >= -1e-9) & (u <= 1 + 1e-9)
    ii, jj = np.nonzero(ok)
    pts = []
    for i, j in zip(ii, jj):
        x, y = p[i] + t[i, j] * r[i]
        if not any(abs(x - a) < 1e-6 and abs(y - b) < 1e-6 for a, b in pts):
            pts.append((x, y))
    return sorted(pts)


def _spline(pts, n=300):
    """Catmull-Rom passando pelos pontos (curvas 'à mão livre' suaves)."""
    pts = np.asarray(pts, float)
    if len(pts) < 3:
        return pts[:, 0], pts[:, 1]
    ext = np.vstack([2 * pts[0] - pts[1], pts, 2 * pts[-1] - pts[-2]])
    out = []
    seg = max(8, n // (len(pts) - 1))
    for i in range(1, len(ext) - 2):
        p0, p1, p2, p3 = ext[i - 1], ext[i], ext[i + 1], ext[i + 2]
        for t in np.linspace(0, 1, seg, endpoint=False):
            t2, t3 = t * t, t * t * t
            out.append(0.5 * ((2 * p1) + (-p0 + p2) * t + (2 * p0 - 5 * p1 + 4 * p2 - p3) * t2
                              + (-p0 + 3 * p1 - 3 * p2 + p3) * t3))
    out.append(pts[-1])
    out = np.asarray(out)
    return out[:, 0], out[:, 1]


# ---------------------------------------------------------------- avaliação de expressões
_FUNCS = {k: getattr(np, k) for k in ("sqrt", "log", "exp", "sin", "cos", "abs", "minimum", "maximum")}
_FUNCS.update({"min": min, "max": max, "pi": math.pi})


class Contexto:
    def __init__(self, xmax, ymax):
        self.nomes = {"xmax": xmax, "ymax": ymax}

    def ev(self, v):
        if isinstance(v, (int, float)):
            return float(v)
        if isinstance(v, str):
            try:
                r = eval(v, {"__builtins__": {}}, {**_FUNCS, **self.nomes})
            except ErroSpec:
                raise
            except Exception as e:
                raise ErroSpec(f"expressão inválida '{v}': {e}")
            if isinstance(r, Ponto):
                raise ErroSpec(f"'{v}' é um ponto; use {v}.x ou {v}.y")
            return float(r)
        raise ErroSpec(f"valor inválido: {v!r}")

    def pt(self, v):
        """Ponto a partir de 'E1' ou [x, y] (cada coordenada pode ser expressão)."""
        if isinstance(v, str):
            r = self.nomes.get(v)
            if not isinstance(r, Ponto):
                raise ErroSpec(f"ponto '{v}' não definido")
            return r
        if isinstance(v, (list, tuple)) and len(v) == 2:
            return Ponto(self.ev(v[0]), self.ev(v[1]))
        raise ErroSpec(f"ponto inválido: {v!r}")


# ---------------------------------------------------------------- desenho de um painel
def _construir_curva(c, ctx, xmax, ymax):
    t = c.get("tipo", "reta")
    if t == "reta":
        p1, p2 = ctx.pt(c["p1"]), ctx.pt(c["p2"])
        xs, ys = np.array([p1.x, p2.x]), np.array([p1.y, p2.y])
        if c.get("estender"):
            dx, dy = p2.x - p1.x, p2.y - p1.y
            ts = np.linspace(-50, 50, 2001)
            xs, ys = p1.x + ts * dx, p1.y + ts * dy
            m = (xs >= 0) & (xs <= xmax) & (ys >= 0) & (ys <= ymax)
            xs, ys = xs[m], ys[m]
        else:
            xs, ys = np.linspace(p1.x, p2.x, 800), np.linspace(p1.y, p2.y, 800)
    elif t == "funcao":
        a, b = (ctx.ev(v) for v in c.get("dominio", [0, xmax]))
        xs = np.linspace(a, b, 600)
        with np.errstate(all="ignore"):
            ys = eval(c["expr"], {"__builtins__": {}}, {**_FUNCS, **ctx.nomes, "x": xs})
        ys = np.broadcast_to(np.asarray(ys, float), xs.shape).copy()
        lim = ctx.ev(c.get("ylim", ymax * 1.02))
        m = np.isfinite(ys) & (ys >= -1e-9) & (ys <= lim)
        xs, ys = xs[m], ys[m]
    elif t == "pontos":
        pts = [tuple(ctx.pt(p)) for p in c["pontos"]]
        if c.get("suave", True):
            xs, ys = _spline(pts)
        else:
            xs, ys = np.array([p[0] for p in pts]), np.array([p[1] for p in pts])
    elif t == "horizontal":
        y = ctx.ev(c["y"])
        a, b = (ctx.ev(v) for v in c.get("x", [0, xmax]))
        xs, ys = np.linspace(a, b, 200), np.full(200, y)
    elif t == "vertical":
        x = ctx.ev(c["x"])
        a, b = (ctx.ev(v) for v in c.get("y", [0, ymax]))
        xs, ys = np.full(200, x), np.linspace(a, b, 200)
    else:
        raise ErroSpec(f"curva {c.get('id')}: tipo desconhecido '{t}'")
    # recorta ao quadro (o que passa do quadro some, e o rótulo vai para a ponta visível)
    m = (xs >= -1e-9) & (xs <= xmax + 1e-9) & (ys >= -1e-9) & (ys <= ymax + 1e-9)
    xs, ys = np.asarray(xs)[m], np.asarray(ys)[m]
    if len(xs) < 2:
        raise ErroSpec(f"curva {c.get('id')} fica fora do quadro")
    return Curva(c["id"], xs, ys)


def _seta(ax, a, b, cor, lw=2.2, estilo="-|>", ms=18, z=6, tracejada=False):
    ax.add_patch(FancyArrowPatch(tuple(a), tuple(b), arrowstyle=estilo, mutation_scale=ms,
                                 color=cor, lw=lw, zorder=z, shrinkA=0, shrinkB=0,
                                 linestyle="--" if tracejada else "-"))


def desenhar_painel(ax, spec, aviso):
    """Desenha um painel; devolve (contexto, textos [(artista, dono)], curvas)."""
    eixos = spec.get("eixos", {})
    xmax, ymax = float(eixos.get("xmax", 10)), float(eixos.get("ymax", 10))
    ctx = Contexto(xmax, ymax)
    textos = []  # (artist, id do dono ou None)
    curvas = {}

    ax.set_xlim(0, xmax * 1.04)
    ax.set_ylim(0, ymax * 1.04)
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    for s in ("left", "bottom"):
        ax.spines[s].set_color(COR["eixo"])
        ax.spines[s].set_linewidth(1.4)
    # setas nas pontas dos eixos
    ax.plot(1, 0, ">", transform=ax.get_yaxis_transform(), clip_on=False, color=COR["eixo"], ms=7)
    ax.plot(0, 1, "^", transform=ax.get_xaxis_transform(), clip_on=False, color=COR["eixo"], ms=7)
    if eixos.get("numeros"):
        ax.tick_params(colors=COR["eixo"], labelsize=11)
    else:
        ax.set_xticks([])
        ax.set_yticks([])
    if not eixos.get("x") or not eixos.get("y"):
        aviso("erro", "eixos sem rótulo (eixos.x e eixos.y são obrigatórios)")
    tx = ax.annotate(eixos.get("x", ""), xy=(1, 0), xycoords="axes fraction", xytext=(0, -26),
                     textcoords="offset points", ha="right", va="center", fontsize=14, color=COR["texto"])
    ty = ax.annotate(eixos.get("y", ""), xy=(0, 1), xycoords="axes fraction", xytext=(10, 4),
                     textcoords="offset points", ha="left", va="bottom", fontsize=14, color=COR["texto"])
    textos += [(tx, "#eixo"), (ty, "#eixo")]
    if spec.get("titulo"):
        ax.set_title(spec["titulo"], fontsize=14, color=COR["texto"], loc="center", pad=14)

    # -- pontos fixos primeiro (curvas podem usá-los), em ordem
    pend_pontos = []
    for p in spec.get("pontos", []):
        if "xy" in p:
            try:
                ctx.nomes[p["id"]] = ctx.pt(p["xy"])
                continue
            except ErroSpec:
                pass
        pend_pontos.append(p)

    # -- curvas
    for c in spec.get("curvas", []):
        cv = _construir_curva(c, ctx, xmax, ymax)
        curvas[c["id"]] = (cv, c)
        ctx.nomes[c["id"]] = cv
        # pontos que dependem desta curva
        for p in list(pend_pontos):
            try:
                _resolver_ponto(p, ctx)
                pend_pontos.remove(p)
            except ErroSpec:
                pass
    for p in pend_pontos:
        _resolver_ponto(p, ctx)  # erro definitivo, se houver

    # -- áreas (por baixo de tudo)
    for a in spec.get("areas", []):
        cor = AREA.get(a.get("papel", "neutro"), a.get("cor", AREA["neutro"]))
        if a.get("tipo", "poligono") == "poligono":
            vs = [tuple(ctx.pt(v)) for v in a["vertices"]]
            ax.add_patch(Polygon(vs, closed=True, facecolor=cor, edgecolor="none", zorder=1,
                                 alpha=a.get("opacidade", 1.0)))
            cx, cy = np.mean([v[0] for v in vs]), np.mean([v[1] for v in vs])
        else:  # "entre": preenche entre duas curvas/constantes no intervalo x
            x0, x1 = (ctx.ev(v) for v in a["x"])
            xs = np.linspace(x0, x1, 300)
            sup = _valores(a["sup"], xs, ctx)
            inf = _valores(a.get("inf", 0), xs, ctx)
            ax.fill_between(xs, inf, sup, facecolor=cor, edgecolor="none", zorder=1)
            cx = (x0 + x1) / 2
            cy = float(np.mean((sup + inf) / 2))
        if a.get("rotulo"):
            if a.get("rotulo_xy"):
                cx, cy = ctx.pt(a["rotulo_xy"])
            t = ax.text(cx, cy, a["rotulo"], ha="center", va="center", fontsize=12.5,
                        color=COR["texto"], zorder=7, fontweight="bold")
            textos.append((t, None))

    # -- curvas desenhadas
    for cid, (cv, c) in curvas.items():
        fam = c.get("familia", "demanda")
        cor = c.get("cor_hex") or FAMILIA.get(fam, COR["texto"])
        inicial = c.get("estado") == "inicial"
        ls = "--" if (fam == "referencia" or c.get("tracejada")) else "-"
        lw = 1.6 if fam == "referencia" else 2.8
        ax.plot(cv.xs, cv.ys, color=cor, lw=lw, ls=ls, alpha=0.5 if inicial else 1.0, zorder=3,
                solid_capstyle="round")
        rot = c.get("rotulo")
        if not rot:
            if fam != "referencia" and not c.get("sem_rotulo"):
                aviso("erro", f"curva {cid} sem rótulo")
            continue
        if "rotulo_xy" in c:
            lx, ly = ctx.pt(c["rotulo_xy"])
            ha, va = "center", "center"
            off = (0, 0)
        else:
            if "rotulo_em" in c:  # x onde o rótulo encosta na curva
                lx = ctx.ev(c["rotulo_em"])
                ly = cv(lx)
            else:  # ponta "final" da curva (a de maior x; empate → maior y)
                k = int(np.lexsort((cv.ys, cv.xs))[-1])
                lx, ly = cv.xs[k], cv.ys[k]
            off = tuple(c.get("rotulo_desloc", (8, 0)))
            ha, va = "left", "center"
        t = ax.annotate(rot, xy=(lx, ly), xytext=off, textcoords="offset points", ha=ha, va=va,
                        fontsize=14, color=cor, fontweight="bold", zorder=8,
                        alpha=0.75 if inicial else 1.0)
        textos.append((t, cid))

    # -- deslocamentos de curva (seta vermelha entre as curvas)
    for d in spec.get("deslocamentos", []):
        if d["de"] not in curvas or d["para"] not in curvas:
            aviso("erro", f"deslocamento {d['de']}→{d['para']}: curva inexistente")
            continue
        c1, c2 = curvas[d["de"]][0], curvas[d["para"]][0]
        if "em_y" in d:
            y = ctx.ev(d["em_y"])
            a, b = Ponto(c1.inv(y), y), Ponto(c2.inv(y), y)
        elif "em_x" in d:
            x = ctx.ev(d["em_x"])
            a, b = Ponto(x, c1(x)), Ponto(x, c2(x))
        else:
            # meio da curva de origem, horizontal se possível
            k = len(c1.xs) // 2 if d.get("posicao") is None else int(len(c1.xs) * d["posicao"])
            a = Ponto(c1.xs[k], c1.ys[k])
            try:
                b = Ponto(c2.inv(a.y), a.y)
            except ErroSpec:
                b = Ponto(a.x, c2(a.x))
        _seta(ax, a, b, COR["vermelho"], lw=2.4, ms=20)
        sentido = d.get("sentido")
        if sentido:
            ok = {"direita": b.x > a.x, "esquerda": b.x < a.x, "cima": b.y > a.y, "baixo": b.y < a.y}[sentido]
            if not ok:
                aviso("erro", f"deslocamento {d['de']}→{d['para']} não vai para a {sentido}")

    # -- setas livres
    for s in spec.get("setas", []):
        a, b = ctx.pt(s["de"]), ctx.pt(s["para"])
        cor = COR.get(s.get("cor", "vermelho"), COR["vermelho"])
        _seta(ax, a, b, cor, lw=s.get("espessura", 2.0), estilo=s.get("estilo", "-|>"),
              tracejada=s.get("tracejada", False))
        if s.get("rotulo"):
            t = ax.annotate(s["rotulo"], xy=((a.x + b.x) / 2, (a.y + b.y) / 2),
                            xytext=tuple(s.get("rotulo_desloc", (6, 6))), textcoords="offset points",
                            fontsize=12.5, color=cor, fontweight="bold", zorder=8)
            textos.append((t, None))

    # -- pontos, projeções e rótulos nos eixos
    for p in spec.get("pontos", []):
        P = ctx.nomes[p["id"]]
        if not (0 <= P.x <= xmax * 1.04 and 0 <= P.y <= ymax * 1.04):
            aviso("erro", f"ponto {p['id']} fora do quadro ({P.x:.2f}, {P.y:.2f})")
        proj = p.get("projetar", False)
        if proj:
            if proj in (True, "xy", "x"):
                ax.plot([P.x, P.x], [0, P.y], ls=":", lw=1.5, color="#777777", zorder=2)
            if proj in (True, "xy", "y"):
                ax.plot([0, P.x], [P.y, P.y], ls=":", lw=1.5, color="#777777", zorder=2)
        if p.get("marcar", True):
            ax.plot([P.x], [P.y], "o", ms=7.5, color=COR["texto"], zorder=9,
                    markeredgecolor="white", markeredgewidth=1.2)
        if p.get("rotulo"):
            t = ax.annotate(p["rotulo"], xy=(P.x, P.y), xytext=tuple(p.get("rotulo_desloc", (11, 0))),
                            textcoords="offset points", fontsize=13.5, color=COR["texto"], va="center",
                            fontweight="bold", zorder=10)
            textos.append((t, "#ponto"))
        if p.get("rotulo_x"):
            t = ax.annotate(p["rotulo_x"], xy=(P.x, 0), xytext=(0, -8), textcoords="offset points",
                            ha="center", va="top", fontsize=13, color=COR["texto"], annotation_clip=False)
            textos.append((t, "#eixo_x"))
        if p.get("rotulo_y"):
            t = ax.annotate(p["rotulo_y"], xy=(0, P.y), xytext=(-8, 0), textcoords="offset points",
                            ha="right", va="center", fontsize=13, color=COR["texto"], annotation_clip=False)
            textos.append((t, "#eixo_y"))

    # -- textos livres
    for tx in spec.get("textos", []):
        P = ctx.pt(tx["xy"])
        cor = COR.get(tx.get("cor", "texto"), COR["texto"])
        t = ax.text(P.x, P.y, tx["texto"], fontsize=tx.get("tamanho", 12.5), color=cor,
                    ha=tx.get("ha", "left"), va=tx.get("va", "center"), zorder=8,
                    fontweight="bold" if tx.get("negrito") else "normal")
        textos.append((t, None))

    # -- checagens declaradas
    for chk in spec.get("checar", []):
        try:
            ok = eval(chk, {"__builtins__": {}}, {**_FUNCS, **ctx.nomes})
        except Exception as e:
            aviso("erro", f"checagem '{chk}' não pôde ser avaliada: {e}")
            continue
        if not ok:
            aviso("erro", f"checagem falhou: {chk}")
    return ctx, textos, curvas


def _resolver_ponto(p, ctx):
    if "intersecao" in p:
        a, b = p["intersecao"]
        ca, cb = ctx.nomes.get(a), ctx.nomes.get(b)
        if not isinstance(ca, Curva) or not isinstance(cb, Curva):
            raise ErroSpec(f"ponto {p['id']}: curva {a} ou {b} não definida")
        pts = intersecoes(ca, cb)
        i = p.get("indice", 0)
        if len(pts) <= i:
            raise ErroSpec(f"ponto {p['id']}: {a} e {b} não se cruzam no quadro")
        ctx.nomes[p["id"]] = Ponto(*pts[i])
    elif "sobre" in p:
        c = ctx.nomes.get(p["sobre"])
        if not isinstance(c, Curva):
            raise ErroSpec(f"ponto {p['id']}: curva {p['sobre']} não definida")
        if "x" in p:
            x = ctx.ev(p["x"])
            ctx.nomes[p["id"]] = Ponto(x, c(x))
        else:
            y = ctx.ev(p["y"])
            ctx.nomes[p["id"]] = Ponto(c.inv(y), y)
    elif "xy" in p:
        ctx.nomes[p["id"]] = ctx.pt(p["xy"])
    else:
        raise ErroSpec(f"ponto {p.get('id')}: defina xy, intersecao ou sobre")


def _valores(v, xs, ctx):
    if isinstance(v, str) and isinstance(ctx.nomes.get(v), Curva):
        c = ctx.nomes[v]
        return np.array([c(x) for x in xs])
    return np.full(xs.shape, ctx.ev(v))


# ---------------------------------------------------------------- outros tipos
def desenhar_dados(ax, spec, aviso):
    """Gráfico de dados reais (barras ou linhas). Números só da fonte."""
    cats = spec["categorias"]
    series = spec["series"]
    cores = [COR["azul"], COR["ocre"], COR["verde"], COR["roxo"], COR["cinza"]]
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.grid(axis="y", color="#E3E3E3", lw=0.8, zorder=0)
    ax.tick_params(colors=COR["eixo"], labelsize=12)
    xs = np.arange(len(cats))
    if spec.get("grafico", "barras") == "barras":
        n = len(series)
        w = 0.8 / n
        for i, s in enumerate(series):
            vals = np.array(s["valores"], float)
            pos = xs - 0.4 + w * (i + 0.5)
            ax.bar(pos, vals, w * 0.92, color=s.get("cor_hex", cores[i % 5]), zorder=2, label=s["nome"])
            if spec.get("valores", True):
                for x, v in zip(pos, vals):
                    # negativos: rótulo logo acima do zero, longe dos nomes das categorias
                    ax.annotate(_num(v, spec), xy=(x, max(v, 0)), xytext=(0, 4),
                                textcoords="offset points", ha="center", va="bottom",
                                fontsize=11.5, color=COR["texto"])
        ax.axhline(0, color=COR["eixo"], lw=1.2)
    else:
        for i, s in enumerate(series):
            ax.plot(xs, s["valores"], color=s.get("cor_hex", cores[i % 5]), lw=2.6, marker="o",
                    label=s["nome"], zorder=3)
    ax.set_xticks(xs, cats)
    if spec.get("unidade"):
        ax.set_ylabel(spec["unidade"], fontsize=12.5, color=COR["texto"])
    if len(series) > 1:
        ax.legend(frameon=False, fontsize=12, loc=spec.get("legenda_pos", "best"))
    if spec.get("titulo"):
        ax.set_title(spec["titulo"], fontsize=14, color=COR["texto"], pad=12)
    if spec.get("fonte"):
        ax.annotate("Fonte: " + spec["fonte"], xy=(0, 0), xycoords="figure fraction", xytext=(10, 6),
                    textcoords="offset points", fontsize=10.5, color="#777777")
    else:
        aviso("erro", "gráfico de dados sem fonte")
    return None, [], {}


def _num(v, spec):
    casas = spec.get("casas", 1)
    s = f"{v:,.{casas}f}".replace(",", "X").replace(".", ",").replace("X", ".").replace("-", "−")
    return s + spec.get("sufixo", "")


def desenhar_tabela(ax, spec, aviso):
    """Tabela como imagem — só como alternativa, se a tabela HTML aninhada não sobreviver."""
    ax.axis("off")
    cab, linhas = spec["cabecalho"], spec["linhas"]
    t = ax.table(cellText=linhas, colLabels=cab, loc="center", cellLoc="center")
    t.auto_set_font_size(False)
    t.set_fontsize(spec.get("corpo", 15))
    t.scale(1, 2.2)
    for (r, c), cel in t.get_celld().items():
        cel.set_edgecolor("#BBBBBB")
        if r == 0:
            cel.set_facecolor("#F0F0F0")
            cel.set_text_props(fontweight="bold", color=COR["texto"])
    if spec.get("fonte"):
        ax.annotate("Fonte: " + spec["fonte"], xy=(0, 0), xycoords="axes fraction", fontsize=11,
                    color="#777777")
    return None, [], {}


def desenhar_formula(ax, spec, aviso):
    ax.axis("off")
    linhas = spec["linhas"]
    for i, l in enumerate(linhas):
        ax.text(0.02, 1 - (i + 0.6) / len(linhas), l, fontsize=spec.get("corpo", 22),
                color=COR["texto"], ha="left", va="center", transform=ax.transAxes)
    return None, [], {}


# ---------------------------------------------------------------- conferência visual
def conferir_sobreposicao(fig, textos, curvas, aviso, painel=""):
    fig.canvas.draw()
    r = fig.canvas.get_renderer()
    caixas = []
    W, H = fig.canvas.get_width_height()
    for art, dono in textos:
        if not art.get_text().strip():
            continue
        bb = art.get_window_extent(r)
        caixas.append((bb, art.get_text(), dono))
        if bb.x0 < 4 or bb.y0 < 4 or bb.x1 > W - 4 or bb.y1 > H - 4:
            aviso("erro", f"{painel}rótulo '{art.get_text()}' sai da imagem")
    for i in range(len(caixas)):
        for j in range(i + 1, len(caixas)):
            a, b = caixas[i][0], caixas[j][0]
            ix = min(a.x1, b.x1) - max(a.x0, b.x0)
            iy = min(a.y1, b.y1) - max(a.y0, b.y0)
            if ix > 2 and iy > 2:
                aviso("erro", f"{painel}rótulos sobrepostos: '{caixas[i][1]}' × '{caixas[j][1]}'")
    # rótulo cortado por curva alheia
    for bb, txt, dono in caixas:
        if dono in ("#eixo",):
            continue
        b = bb.expanded(0.9, 0.8)
        for cid, (cv, c) in curvas.items():
            if cid == dono:
                continue
            ax = c.get("_ax")
            pts = ax.transData.transform(np.stack([cv.xs, cv.ys], 1))
            dentro = (pts[:, 0] > b.x0) & (pts[:, 0] < b.x1) & (pts[:, 1] > b.y0) & (pts[:, 1] < b.y1)
            if dentro.any():
                aviso("aviso", f"{painel}rótulo '{txt}' é cortado pela curva {cid}")


# ---------------------------------------------------------------- orquestração
def renderizar(spec, saida_dir=None, so_checar=False):
    """Renderiza uma spec. Devolve dict com id, png, erros, avisos."""
    spec = expandir_modelo(copy.deepcopy(spec))
    gid = spec.get("id") or "grafico"
    problemas = []

    def aviso(nivel, msg):
        problemas.append((nivel, msg))

    if not spec.get("legenda"):
        aviso("erro", "spec sem 'legenda' (frase em itálico que acompanha a figura no card)")
    paineis = spec.get("paineis") or [spec]
    tam = spec.get("tamanho", "card" if len(paineis) == 1 else "largo")
    fig, axs = plt.subplots(1, len(paineis), figsize=TAMANHO.get(tam, TAMANHO["card"]), dpi=DPI)
    axs = np.atleast_1d(axs)
    fig.patch.set_facecolor("white")
    for k, (ax, p) in enumerate(zip(axs, paineis)):
        rotulo = f"[painel {k + 1}] " if len(paineis) > 1 else ""
        try:
            tipo = p.get("tipo", spec.get("tipo", "modelo"))
            if tipo == "dados":
                _, textos, curvas = desenhar_dados(ax, p, aviso)
            elif tipo == "tabela":
                _, textos, curvas = desenhar_tabela(ax, p, aviso)
            elif tipo == "formula":
                _, textos, curvas = desenhar_formula(ax, p, aviso)
            else:
                _, textos, curvas = desenhar_painel(ax, p, lambda n, m, r=rotulo: aviso(n, r + m))
                for cv, c in curvas.values():
                    c["_ax"] = ax
        except (ErroSpec, KeyError, ValueError, TypeError) as e:
            aviso("erro", rotulo + f"{type(e).__name__}: {e}")
            textos, curvas = [], {}
        fig.tight_layout(pad=1.6)
        conferir_sobreposicao(fig, textos, curvas, aviso, rotulo)
    png = None
    if not so_checar and saida_dir:
        os.makedirs(saida_dir, exist_ok=True)
        png = os.path.join(saida_dir, gid + ".png")
        fig.savefig(png, dpi=DPI, facecolor="white")
        _compactar_png(png)
    plt.close(fig)
    erros = [m for n, m in problemas if n == "erro"]
    avisos = [m for n, m in problemas if n == "aviso"]
    return {"id": gid, "png": png, "erros": erros, "avisos": avisos, "legenda": spec.get("legenda", "")}


def _compactar_png(caminho):
    try:
        from PIL import Image
    except ImportError:
        return
    im = Image.open(caminho).convert("RGB")
    im.quantize(colors=96, method=Image.Quantize.MEDIANCUT, dither=Image.Dither.NONE).save(
        caminho, optimize=True)


def carregar_specs(caminhos):
    specs = []
    for c in caminhos:
        if os.path.isdir(c):
            for f in sorted(os.listdir(c)):
                if f.endswith(".json"):
                    specs += carregar_specs([os.path.join(c, f)])
        elif c.endswith(".jsonl"):
            with open(c, encoding="utf-8") as fh:
                for linha in fh:
                    if linha.strip():
                        reg = json.loads(linha)
                        for g in reg.get("figuras", []):
                            if g.get("spec"):
                                specs.append(g["spec"])
        else:
            with open(c, encoding="utf-8") as fh:
                d = json.load(fh)
            specs += d if isinstance(d, list) else [d]
    return specs


def galeria(resultados, saida_dir):
    linhas = ["<!doctype html><meta charset='utf-8'><title>Galeria de gráficos</title>",
              "<body style='font-family:sans-serif;max-width:1000px;margin:20px auto;background:#fff;color:#222'>",
              "<h1>Galeria de gráficos</h1>"]
    for r in resultados:
        st = "✅" if not r["erros"] else "❌"
        linhas.append(f"<h3>{st} {html.escape(r['id'])}</h3>")
        if r["png"]:
            linhas.append(f"<img src='{os.path.basename(r['png'])}' style='width:640px;border:1px solid #ddd'/>")
        linhas.append(f"<p><i>{html.escape(r['legenda'])}</i></p>")
        for e in r["erros"]:
            linhas.append(f"<p style='color:#C80000'>erro: {html.escape(e)}</p>")
        for a in r["avisos"]:
            linhas.append(f"<p style='color:#AA5500'>aviso: {html.escape(a)}</p>")
    with open(os.path.join(saida_dir, "galeria.html"), "w", encoding="utf-8") as fh:
        fh.write("\n".join(linhas))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entradas", nargs="+", help="specs .json (um objeto ou lista), pastas ou .jsonl")
    ap.add_argument("-o", "--saida", default="figuras")
    ap.add_argument("--checar", action="store_true", help="só confere, não grava PNG")
    ap.add_argument("--galeria", action="store_true", help="gera galeria.html para revisão visual")
    a = ap.parse_args()
    resultados = [renderizar(s, a.saida, a.checar) for s in carregar_specs(a.entradas)]
    n_err = 0
    for r in resultados:
        st = "OK " if not r["erros"] else "ERR"
        print(f"[{st}] {r['id']}")
        for e in r["erros"]:
            print("      erro:", e)
            n_err += 1
        for w in r["avisos"]:
            print("      aviso:", w)
    if a.galeria and not a.checar:
        galeria(resultados, a.saida)
    print(f"{len(resultados)} gráfico(s), {n_err} erro(s)")
    sys.exit(1 if n_err else 0)


if __name__ == "__main__":
    main()
