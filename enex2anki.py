#!/usr/bin/env python3
"""Converte tabelas de 2 colunas de notas do Evernote (.enex) em um baralho do Anki (.apkg).

Cada linha de tabela vira um card: 1ª coluna = frente, 2ª coluna = verso.
Formatação (negrito, cores, realces, cor de fundo da célula) e imagens são preservadas.

Uso:
    python3 enex2anki.py ARQUIVO_OU_PASTA [...] -o saida/meu_baralho.apkg

Exemplos:
    python3 enex2anki.py entrada/Historia.enex
    python3 enex2anki.py entrada/ --baralho "CACD" --pular-cabecalho
"""
import argparse
import base64
import hashlib
import html
import mimetypes
import re
import sys
import tempfile
import warnings
from pathlib import Path
from xml.etree import ElementTree as ET

import genanki
from bs4 import BeautifulSoup, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

# IDs fixos: permitem reimportar no Anki e ATUALIZAR os cards em vez de duplicá-los.
MODEL_ID = 1607392319
DECK_ID_BASE = 2059400110

CSS = """
.card { font-family: Arial, sans-serif; font-size: 20px; text-align: left;
        color: black; background-color: white; }
.nightMode.card { color: #eee; background-color: #2f2f31; }
.celula { padding: 8px; border-radius: 4px; }
.origem { margin-top: 18px; font-size: 12px; color: #888; }
table { border-collapse: collapse; }
td, th { border: 1px solid #bbb; padding: 4px; }
img { max-width: 100%; }
"""

MODELO = genanki.Model(
    MODEL_ID,
    "Evernote (Frente/Verso)",
    fields=[{"name": "Frente"}, {"name": "Verso"}, {"name": "Origem"}],
    templates=[{
        "name": "Card 1",
        "qfmt": "{{Frente}}",
        "afmt": '{{FrontSide}}<hr id="answer">{{Verso}}'
                '<div class="origem">{{Origem}}</div>',
    }],
    css=CSS,
)

# Estilos da célula que valem a pena levar para o card (o resto é layout do Evernote).
ESTILOS_CELULA = ("background-color", "background", "color", "text-align", "font-weight")


def limpar_tag(texto):
    """Tags do Anki não aceitam espaços."""
    return re.sub(r"\s+", "_", texto.strip())


def estilo_da_celula(td):
    partes = []
    for decl in (td.get("style") or "").split(";"):
        if ":" in decl:
            prop, val = decl.split(":", 1)
            if prop.strip().lower() in ESTILOS_CELULA:
                partes.append(f"{prop.strip()}:{val.strip()}")
    if td.get("bgcolor"):
        partes.append(f"background-color:{td['bgcolor']}")
    return ";".join(partes)


def conteudo_da_celula(td, midias):
    """HTML interno da célula, com <en-media> trocado por <img> e cor de fundo preservada."""
    for m in td.find_all("en-media"):
        nome = midias.get(m.get("hash", ""))
        if nome:
            img = BeautifulSoup(f'<img src="{html.escape(nome)}">', "html.parser").img
            m.replace_with(img)
        else:
            m.decompose()
    for cb in td.find_all("en-todo"):
        cb.replace_with("☑ " if cb.get("checked") == "true" else "☐ ")
    interno = td.decode_contents().strip()
    estilo = estilo_da_celula(td)
    if estilo:
        interno = f'<div class="celula" style="{html.escape(estilo)}">{interno}</div>'
    return interno


def texto_vazio(fragmento):
    s = BeautifulSoup(fragmento, "html.parser")
    return not s.get_text(strip=True) and not s.find("img")


def linhas_de_tabelas(soup):
    """Gera (td_frente, td_verso) de todas as tabelas de 2+ colunas (ignora tabelas aninhadas)."""
    for tabela in soup.find_all("table"):
        if tabela.find_parent("table"):
            continue
        linhas = [tr for tr in tabela.find_all("tr") if tr.find_parent("table") is tabela]
        for i, tr in enumerate(linhas):
            celulas = [c for c in tr.find_all(["td", "th"]) if c.find_parent("tr") is tr]
            if len(celulas) >= 2:
                yield i, celulas[0], celulas[1]


def ler_enex(caminho, pasta_midia):
    """Lê um .enex e devolve lista de notas: {titulo, tags, html, midias{hash: nome_arquivo}}."""
    notas = []
    for _, el in ET.iterparse(caminho, events=("end",)):
        if el.tag != "note":
            continue
        midias = {}
        for res in el.findall("resource"):
            dados_el = res.find("data")
            if dados_el is None or not (dados_el.text or "").strip():
                continue
            dados = base64.b64decode(dados_el.text)
            md5 = hashlib.md5(dados).hexdigest()
            mime = res.findtext("mime") or ""
            ext = mimetypes.guess_extension(mime) or ""
            nome = f"evernote_{md5}{ext}"
            (pasta_midia / nome).write_bytes(dados)
            midias[md5] = nome
        notas.append({
            "titulo": (el.findtext("title") or "").strip(),
            "tags": [t.text for t in el.findall("tag") if t.text],
            "html": el.findtext("content") or "",
            "midias": midias,
        })
        el.clear()
    return notas


def arquivos_enex(entradas):
    for e in entradas:
        p = Path(e)
        if p.is_dir():
            yield from sorted(p.rglob("*.enex"))
        elif p.suffix.lower() == ".enex":
            yield p
        else:
            print(f"Aviso: ignorando {p} (não é .enex nem pasta)", file=sys.stderr)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entradas", nargs="+", help="arquivos .enex ou pastas contendo .enex")
    ap.add_argument("-o", "--saida", default="saida/evernote.apkg", help="arquivo .apkg de saída")
    ap.add_argument("--baralho", default="Evernote",
                    help="nome do baralho-mãe; cada .enex vira um sub-baralho (padrão: Evernote)")
    ap.add_argument("--pular-cabecalho", action="store_true",
                    help="ignora a 1ª linha de cada tabela (use se ela for só 'Pergunta | Resposta')")
    ap.add_argument("--baralho-unico", action="store_true",
                    help="põe tudo num baralho só, sem sub-baralhos por arquivo")
    args = ap.parse_args()

    pasta_midia = Path(tempfile.mkdtemp(prefix="enex_midia_"))
    baralhos, arquivos_midia = {}, set()
    total_cards, notas_sem_tabela = 0, []

    for enex in arquivos_enex(args.entradas):
        caderno = enex.stem
        nome_baralho = args.baralho if args.baralho_unico else f"{args.baralho}::{caderno}"
        if nome_baralho not in baralhos:
            deck_id = DECK_ID_BASE + int(hashlib.md5(nome_baralho.encode()).hexdigest()[:8], 16)
            baralhos[nome_baralho] = genanki.Deck(deck_id, nome_baralho)
        baralho = baralhos[nome_baralho]

        for nota in ler_enex(enex, pasta_midia):
            soup = BeautifulSoup(nota["html"], "html.parser")
            tags = [f"evernote::{limpar_tag(caderno)}"] + [limpar_tag(t) for t in nota["tags"]]
            n_nota = 0
            for i, td_f, td_v in linhas_de_tabelas(soup):
                if args.pular_cabecalho and i == 0:
                    continue
                frente = conteudo_da_celula(td_f, nota["midias"])
                verso = conteudo_da_celula(td_v, nota["midias"])
                if texto_vazio(frente) or texto_vazio(verso):
                    continue
                origem = html.escape(f"{caderno} › {nota['titulo']}")
                # GUID estável: mesmo caderno + nota + frente => mesmo card ao reimportar.
                guid = genanki.guid_for(caderno, nota["titulo"], frente)
                baralho.add_note(genanki.Note(model=MODELO, fields=[frente, verso, origem],
                                              tags=tags, guid=guid))
                n_nota += 1
            for nome in nota["midias"].values():
                arquivos_midia.add(str(pasta_midia / nome))
            if n_nota == 0:
                notas_sem_tabela.append(f"{caderno} › {nota['titulo']}")
            total_cards += n_nota
        print(f"{enex.name}: ok")

    if not baralhos:
        sys.exit("Nenhum arquivo .enex encontrado.")

    saida = Path(args.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    pacote = genanki.Package(list(baralhos.values()))
    pacote.media_files = sorted(arquivos_midia)
    pacote.write_to_file(saida)

    print(f"\n{total_cards} cards gerados em {len(baralhos)} baralho(s) -> {saida}")
    if notas_sem_tabela:
        print(f"\n{len(notas_sem_tabela)} nota(s) sem tabela de 2 colunas (nenhum card gerado):")
        for n in notas_sem_tabela:
            print(f"  - {n}")


if __name__ == "__main__":
    main()
