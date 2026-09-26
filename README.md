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
python3 enex2anki.py entrada/ --config regimentos.json -o saida/regimentos.apkg
```

- `secao_h1`: só usa as tabelas que ficam abaixo do título H1 com esse texto (ex.: "flashcards")
- `sub_baralho_por_nota`: cada nota vira um sub-baralho (`Regimentos::01-A — …`)
- `tags_por_numero`: tag temática pelo número do título da nota (01, 02, …)
- `prioritarios` / `tag_prioritario`: tag de prioridade (também aplicada se o título tiver ⭐)
- `manter_tags_evernote`: se `true`, também copia as tags da nota no Evernote
