# Evernote → Anki

Converte notas do Evernote (`.enex`) que têm **tabelas de 2 colunas** em cards do Anki (`.apkg`).

- 1ª coluna = **frente**, 2ª coluna = **verso**
- mantém negrito, cores de texto, realces, cor de fundo da célula e imagens
- **tags**: as tags da nota no Evernote + `evernote::<nome do caderno>`
- **baralhos**: `Evernote::<nome do caderno>` (um sub-baralho por arquivo `.enex`)
- cada card mostra de qual nota veio (rodapé do verso)
- reimportar o mesmo material **atualiza** os cards em vez de duplicá-los

## Como usar

1. No Evernote, exporte cada caderno como `.enex` (o nome do arquivo vira o nome do baralho).
2. Instale as dependências: `pip install -r requirements.txt`
3. Rode:

```
python3 enex2anki.py entrada/ -o saida/evernote.apkg --pular-cabecalho
```

Opções:
- `--pular-cabecalho` — ignora a 1ª linha de cada tabela (se ela for só "Pergunta | Resposta")
- `--baralho "CACD"` — muda o nome do baralho-mãe
- `--baralho-unico` — tudo num baralho só

4. No Anki: **Arquivo → Importar** → escolha o `.apkg`.

Ao final, o script lista as notas em que não encontrou nenhuma tabela.

## Regras por caderno (`--config`)

Um arquivo `.json` define baralhos e tags de um caderno específico. Exemplo: `regimentos.json`:

```
python3 enex2anki.py entrada/teoria.html entrada/questoes.html --config regimentos.json -o saida/regimentos.apkg
```

- `secao_h1`: só usa as tabelas que ficam abaixo do título H1 com esse texto (ex.: "flashcards")
- `sub_baralho_por_nota`: cada nota vira um sub-baralho (`Regimentos::01-A — …`)
- `tags_por_numero`: tag temática pelo número do título da nota (01, 02, …)
- `prioritarios` / `tag_prioritario`: tag de prioridade (também aplicada se o título tiver ⭐)
- `manter_tags_evernote`: se `true`, também copia as tags da nota no Evernote
- `estilo_trilha`: aparência da linha `[REG › …]` no topo da frente: `original`, `A`, `B`, `C` ou `D` (escondida)
- `cloze`: frentes com lacunas `______` e verso numerado (`1. …`, `2. …`) viram cards Cloze;
  dicas como `______ [quando, 2]` viram dica do cloze
- `cloze_um_card_por_lacuna`: `false` = um card com todas as lacunas; `true` = um card por lacuna
- `tag_fundo_colorido`: tag para os cards cuja frente tem fundo colorido (ex.: `REG-CARD-GERAL`)

Também aceita notas exportadas como `.html` (sem imagens), no lugar do `.enex`, inclusive um único
`.html` com o caderno inteiro (o script separa as notas pelo título).

Outras opções do `.json`:
- `secao_h1` pode ser uma lista (ex.: `["flashcards", "👾 deck"]`)
- `blocos`: nível intermediário de baralho pelo número da nota (ex.: `"01": "1. Disposições preliminares…"`)
- `questoes`: notas de questões (título casando com `padrao_titulo`, ex.: `01-A-1 - Obj.`) viram o
  sub-baralho `sub_baralho` dentro da nota de teoria de mesmo código, com a tag `tag`
- `encurtar_nome_baralho`: expressões regulares removidas só do nome do sub-baralho (ex.: `(Pop)`, parênteses longos)
- `tags_por_numero` aceita uma lista de tags por número de nota
- `questoes.tag_fonte`: prefixo de tag para a fonte da questão, lida do cabeçalho `[C/E - Fonte › …]`
- `remover_sufixos_titulo`: textos a cortar do fim do título das notas (restos de títulos de bloco)

## Cadernos configurados

| Caderno | Config | Comando |
|---|---|---|
| Regimentos (RICD/RCCN) | `regimentos.json` | `python3 enex2anki.py entrada/geral/ entrada/questoes/ --config regimentos.json -o saida/regimentos.apkg` |
| Geografia | `geografia.json` | `python3 enex2anki.py entrada/geo/ --config geografia.json -o saida/geografia.apkg` |
| História Mundial | `historia_mundial.json` | `python3 enex2anki.py entrada/hm/ --config historia_mundial.json -o saida/historia_mundial.apkg` |

Arquivos `.7z` podem ser extraídos com `pip install py7zr` e `python3 -c "import py7zr; py7zr.SevenZipFile('arq.7z').extractall('entrada/x')"`.
