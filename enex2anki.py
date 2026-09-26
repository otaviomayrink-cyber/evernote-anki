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
import json
import mimetypes
import re
import sys
import tempfile
import unicodedata
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
    # Cor de texto sem cor de fundo some no modo noturno do Anki: só a mantém junto do fundo.
    if not any(p.startswith("background") for p in partes):
        partes = [p for p in partes if not p.startswith("color")]
    return ";".join(partes)


def conteudo_da_celula(td, midias, usadas):
    """HTML interno da célula, com <en-media> trocado por <img> e cor de fundo preservada.

    Os arquivos de imagem usados são acrescentados a `usadas`.
    """
    for m in td.find_all("en-media"):
        nome = midias.get(m.get("hash", ""))
        if nome:
            usadas.add(nome)
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


def normalizar(texto):
    sem_acento = unicodedata.normalize("NFKD", texto)
    return "".join(c for c in sem_acento if not unicodedata.combining(c)).lower()


def secao_da_tabela(tabela):
    """Texto do último <h1> antes da tabela (ou None se não houver)."""
    h1 = tabela.find_previous("h1")
    return normalizar(h1.get_text(" ", strip=True)) if h1 else None


def codigo_da_nota(titulo):
    """Extrai o código do título: '⭐ 01-A — 🤝 Partidos...' -> ('01', '01-A')."""
    m = re.search(r"\b(\d{2})(?:\s*-\s*([A-Z]))?\b", titulo)
    if not m:
        return None, None
    return m.group(1), m.group(1) + (f"-{m.group(2)}" if m.group(2) else "")


def nome_sub_baralho(titulo, remover):
    for r in remover:
        titulo = titulo.replace(r, "")
    titulo = titulo.replace("::", ":")
    return re.sub(r"\s+", " ", titulo).strip() or "Sem título"


def tags_da_nota(nota, caderno, cfg):
    tags = []
    if cfg.get("manter_tags_evernote", True):
        tags.append(f"evernote::{limpar_tag(caderno)}")
        tags += [limpar_tag(t) for t in nota["tags"]]
    tags += cfg.get("tags_fixas", [])
    numero, codigo = codigo_da_nota(nota["titulo"])
    tema = cfg.get("tags_por_numero", {}).get(numero or "")
    if tema:
        tags.append(tema)
    if cfg.get("tag_prioritario") and ("⭐" in nota["titulo"] or codigo in cfg.get("prioritarios", [])):
        tags.append(cfg["tag_prioritario"])
    return list(dict.fromkeys(limpar_tag(t) for t in tags))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("entradas", nargs="+", help="arquivos .enex ou pastas contendo .enex")
    ap.add_argument("-o", "--saida", default="saida/evernote.apkg", help="arquivo .apkg de saída")
    ap.add_argument("--config", help="arquivo .json com regras de baralhos/tags (ex.: regimentos.json)")
    ap.add_argument("--baralho", help="nome do baralho-mãe (padrão: Evernote)")
    ap.add_argument("--pular-cabecalho", action="store_true",
                    help="ignora a 1ª linha de cada tabela (use se ela for só 'Pergunta | Resposta')")
    ap.add_argument("--baralho-unico", action="store_true",
                    help="põe tudo num baralho só, sem sub-baralhos")
    args = ap.parse_args()

    cfg = json.loads(Path(args.config).read_text(encoding="utf-8")) if args.config else {}
    raiz = args.baralho or cfg.get("baralho", "Evernote")
    secao = normalizar(cfg["secao_h1"]) if cfg.get("secao_h1") else None
    por_nota = cfg.get("sub_baralho_por_nota", False)
    remover = cfg.get("remover_do_nome_do_baralho", [])
    pular_cab = args.pular_cabecalho or cfg.get("pular_cabecalho", False)

    pasta_midia = Path(tempfile.mkdtemp(prefix="enex_midia_"))
    baralhos, arquivos_midia = {}, set()
    total_cards, sem_secao, sem_cards = 0, [], []

    def baralho(nome):
        if nome not in baralhos:
            deck_id = DECK_ID_BASE + int(hashlib.md5(nome.encode()).hexdigest()[:8], 16)
            baralhos[nome] = genanki.Deck(deck_id, nome)
        return baralhos[nome]

    for enex in arquivos_enex(args.entradas):
        caderno = enex.stem
        notas = ler_enex(enex, pasta_midia)
        for nota in notas:
            if args.baralho_unico:
                nome_baralho = raiz
            elif por_nota:
                nome_baralho = f"{raiz}::{nome_sub_baralho(nota['titulo'], remover)}"
            else:
                nome_baralho = f"{raiz}::{caderno}"
            soup = BeautifulSoup(nota["html"], "html.parser")
            tags = tags_da_nota(nota, caderno, cfg)
            ref = nota["titulo"] if por_nota else f"{caderno} › {nota['titulo']}"
            if secao and not any(secao in normalizar(h.get_text()) for h in soup.find_all("h1")):
                sem_secao.append(ref)
                continue
            n_nota = 0
            for i, td_f, td_v in linhas_de_tabelas(soup):
                if secao and secao not in (secao_da_tabela(td_f.find_parent("table")) or ""):
                    continue
                if pular_cab and i == 0:
                    continue
                usadas = set()
                frente = conteudo_da_celula(td_f, nota["midias"], usadas)
                verso = conteudo_da_celula(td_v, nota["midias"], usadas)
                if texto_vazio(frente) or texto_vazio(verso):
                    continue
                # GUID estável: mesma nota + mesma frente => mesmo card ao reimportar,
                # mesmo que o .enex tenha outro nome (exportações em partes).
                guid = genanki.guid_for(nota["titulo"], frente)
                assunto = td_f.find_parent("table").find_previous(["h2", "h3"])
                origem = ref + (f" › {assunto.get_text(' ', strip=True)}" if assunto else "")
                baralho(nome_baralho).add_note(genanki.Note(
                    model=MODELO, fields=[frente, verso, html.escape(origem)], tags=tags, guid=guid))
                arquivos_midia.update(str(pasta_midia / n) for n in usadas)
                n_nota += 1
            if n_nota == 0:
                sem_cards.append(ref)
            total_cards += n_nota
        print(f"{enex.name}: {len(notas)} nota(s) lidas")

    if not baralhos:
        sys.exit("Nenhum card gerado (confira os arquivos .enex e as regras do --config).")

    saida = Path(args.saida)
    saida.parent.mkdir(parents=True, exist_ok=True)
    pacote = genanki.Package(list(baralhos.values()))
    pacote.media_files = sorted(arquivos_midia)
    pacote.write_to_file(saida)

    print(f"\n{total_cards} cards gerados em {len(baralhos)} baralho(s) -> {saida}")
    if sem_secao:
        print(f"\n{len(sem_secao)} nota(s) sem o título H1 '{cfg['secao_h1']}' (ignoradas):")
        for n in sem_secao:
            print(f"  - {n}")
    if sem_cards:
        print(f"\n{len(sem_cards)} nota(s) sem tabela de 2 colunas na parte certa (nenhum card gerado):")
        for n in sem_cards:
            print(f"  - {n}")


if __name__ == "__main__":
    main()
