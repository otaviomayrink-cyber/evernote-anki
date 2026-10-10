# Revisão B — ECO passada 03 (cards_09 … cards_16)

Revisor independente. Checagem de cada card contra a linha bruta (`brutos.jsonl`, rid = `fonte_ref`) e a classificação (`lotes/redacao_*.jsonl`).
Depois de cada edição, `checar_lote.py` retornou 0 violação.

## 1. Amostra (`revisao_amostra_B.json`, 26 cards)

| # | Card | Arquivo | Gab. | Gabarito | Fidelidade | Conteúdo | Ação |
|---|---|---|---|---|---|---|---|
| 1 | ECO-E2-L01625-1 | 10 | C | ok | ok | ok: a nomenclatura “coberta” com prêmio de risco fica explicada no 📖 e em `nota_redacao` | — |
| 2 | ECO-E2-L00570-1 | 14 | E | ok | ok | ok | — |
| 3 | ECO-E2-L01244-1 | 12 | E | ok | ok | ok | — |
| 4 | ECO-E1-0309-1 | 10 | E | ok | ok | ok | — |
| 5 | ECO-E3-L00137-1 | 13 | C | ok | ok | ok | — |
| 6 | ECO-E2-L00145-1 | 11 | E | ok | ok | ok | — |
| 7 | ECO-E1-0771-1 | 09 | C | ok | ok | ok: os episódios do II PND e do Plano Real estão corretos | — |
| 8 | ECO-E2-L01544-1 | 16 | E | ok | ok | ok | — |
| 9 | ECO-E1-0938-1 | 14 | C | ok | ok | ok: o erro da fonte (tecnologia) foi corrigido e registrado | — |
| 10 | ECO-E2-L00495-1 | 14 | E | ok | ok | ok: custos de oportunidade e intervalo 3/7–2 conferidos | — |
| 11 | ECO-E2-L01513-1 | 12 | C | ok | ok | ok | — |
| 12 | ECO-E2-L00141-1 | 11 | C | ok | ok | ok | — |
| 13 | ECO-E2-L00573-1 | 15 | E | ok | ok | ok | — |
| 14 | ECO-E1-0864-1 | 09 | C | ok | ok: só o invólucro “É correto afirmar…?” foi retirado, com registro em alerta | ok | — |
| 15 | ECO-E1-0880-1 | 10 | C | ok | ok: a premissa passou da assertiva para o comando, sem perda | ok: o erro da fonte (base monetária) foi corrigido | — |
| 16 | ECO-E1-0876-1 | 10 | C | ok, com ⚠️ contestável (já presente e correto) | ok | ok | — |
| 17 | ECO-E2-L00564-1 | 11 | C | ok | ok | ok | — |
| 18 | ECO-E1-0450-1 | 10 | C | ok | ok | ok | — |
| 19 | ECO-E1-0703-1 | 10 | E | ok: oficial alterado de C para E, com 🏛️ | ok | ok | — |
| 20 | ECO-E1-0868-1 | 10 | C | ok, com ⚠️ contestável (já presente e correto) | ok | metalinguagem “Exemplo citado na fonte” | corrigido para “Exemplo:” |
| 21 | ECO-E1-0917-1 | 14 | C | ok, com ⚠️ contestável (já presente e correto) | ok | 🧐 remetia ao “contexto da série”, sem base na fonte | corrigido para “o modelo implícito (FPP côncava, produção diversificada)” |
| 22 | ECO-E2-L00146-1 | 11 | C | ok | ok | ok | — |
| 23 | ECO-E2-L01470-1 | 15 | C | ok | ok | ok | — |
| 24 | ECO-E2-L01554-1 | 09 | C | ok | ok | ok: a confusão coberta × descoberta fica explicada | — |
| 25 | ECO-E2-L00572-1 | 15 | E | ok | ok | ok | — |
| 26 | ECO-E1-0885-1 | 11 | E | ok | ok | ok: a nuance da LM* vertical de Mankiw está correta | — |

Metadados (banca, prova, ano, cacd, errei) conferem com a classificação nos 26. Nenhum autor, citação ou dado de prova inventado. Nenhum dado perecível sem ⏳.

## 2. Itens ERRADO (todos os arquivos 09–16)

A checagem foi automática, por alinhamento palavra a palavra entre assertiva, `anotada` e `reescrita`, com releitura manual de todos os pares.
Itens conferidos: 110 C/E ERRADO e as 4 alternativas erradas da ME ECO-E1-0926-1.

Corrigidos:
- **ECO-E1-0893-1** (cards_13): a reescrita começava com `[…]` numa assertiva curta (~330 caracteres). Agora reproduz a assertiva inteira, com realce só na correção.
- **ECO-E2-L00974-1** (cards_15): a reescrita tinha `[…]` no meio de uma assertiva curta (~370 caracteres). O trecho omitido foi restaurado.

Nos demais, todo vermelho é corrigido com `hl`/`<s>`, não há vermelho em trecho inalterado nem mudança sem realce. ECO-E1-0673-1 aparece no alinhamento automático, mas é falso positivo: a reescrita está correta.

Remissões entre cards:
- Nenhum texto cita outro card pelo id. Os ids aparecem só em `alertas` e em ids de figura (`figuras_fonte`).
- Não há “item irmão”, “questão anterior” nem “texto acima”.
- ECO-E2-L01446-1 e ECO-E2-L01487-1 (cards_12) mantêm “Na situação/No caso do item anterior” porque isso está na própria assertiva da fonte (fidelidade). O `excerto` de cada um transcreve a proposição anterior, então o card se lê sozinho.

## 3. Totais

- **Amostra (26 cards):** 0 problema de gabarito, 0 de fidelidade, 2 de conteúdo/redação (corrigidos: metalinguagem e remissão ao “contexto da série”). ⚠️ contestável já presente onde cabia (3 cards).
- **ERRADO:** 110 C/E + 1 ME conferidos, 2 corrigidos (reescrita com `[…]`).
- **Remissões por id removidas:** 0 (não havia nenhuma).
- **Arquivos editados:** cards_10, cards_13, cards_14, cards_15. `checar_lote.py` deu 0 violação em todos.
