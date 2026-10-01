"""Atalhos de marcação HTML para os cards -Q (Folha v9 §5.1 / Folha -Q v3 §3.2).

Uso nos arquivos de cards:  from marcacao import az, vm, azb, vd, oc, rx, cz, hl
"""


def az(t):
    """Trecho correto da assertiva anotada (azul, sem negrito)."""
    return f'<span style="color: rgb(0, 60, 200);">{t}</span>'


def vm(t):
    """Trecho errado da assertiva anotada; regra decisiva no comentário (vermelho, negrito)."""
    return f'<span style="color: rgb(200, 0, 0);"><b>{t}</b></span>'


def azb(t):
    """Conceito/instituição (azul, negrito)."""
    return f'<span style="color: rgb(0, 60, 200);"><b>{t}</b></span>'


def vd(t):
    """Dado verificável: data, número, artigo (verde, negrito)."""
    return f'<span style="color: rgb(0, 130, 0);"><b>{t}</b></span>'


def oc(t):
    """Autor/obra/escola (ocre, negrito)."""
    return f'<span style="color: rgb(170, 85, 0);"><b>{t}</b></span>'


def rx(t):
    """Posição/atuação do Brasil (roxo, negrito)."""
    return f'<span style="color: rgb(130, 0, 160);"><b>{t}</b></span>'


def cz(t):
    """Meta: rótulos da taxonomia, justificativa da banca (cinza)."""
    return f'<span style="color: rgb(160, 160, 160);">{t}</span>'


def hl(t):
    """Correção na reescrita / termo-chave (realce amarelo + negrito)."""
    return f'<span style="background-color:#FFEF9E;"><b>{t}</b></span>'
