# Revisão C — passada 03 (cards_17, 18, 19, 20, 21, 23)

## 1. Amostra (revisao_amostra_C.json, 19 cards)

Conferido contra `brutos.jsonl` (rid = fonte_ref) e a classificação do lote: gabarito, fidelidade da assertiva, economia do comentário, dados de prova, autores e citações, marca ⏳.

| Card | Arquivo | Gabarito | Fidelidade | Conteúdo | Ação |
|---|---|---|---|---|---|
| ECO-E2-L00833-1 | 21 | ERRADO = fonte | ok | ok (conteúdo local; ⏳ nos percentuais) | — |
| ECO-E3-L00362-1 | 23 | ERRADO = fonte | ok | ok (corrige o erro do verso da fonte) | — |
| ECO-E1-0931-1 | 19 | CERTO = fonte, ⚠️ contestável presente | ok (tabela perdida registrada) | conta capital exemplificada com “marcas e patentes”: no BPM6, patente é ativo produzido (P&D, vai para serviços) | corrigido para “direitos de exploração de recursos naturais e marcas” |
| ECO-E1-0797-1 | 19 | ERRADO = fonte | ok | ok | — |
| ECO-E2-L00299-1 | 17 | ERRADO = fonte | ok | ok | — |
| ECO-E2-L00227-1 | 19 | CERTO = fonte | ok (“económicos” é da fonte) | ok (Hymer, Dunning, Buckley e Casson) | — |
| ECO-E3-L00255-1 | 19 | ERRADO = fonte | ok (“demais país” → “países”, registrado) | ok | — |
| ECO-E1-0981-1 | 23 | ERRADO = fonte | ok | ok (⏳ em membros e votos) | — |
| ECO-E2-L00576-1 | 18 | CERTO = fonte | ok | ok | — |
| ECO-E1-0902-1 | 19 | ANULADO = fonte, ⚠️ presente | ok | ok | — |
| ECO-E1-0922-1 | 17 | CERTO = fonte | ok (OCR “por pelo” corrigido, registrado) | ok (Tinbergen 1962, McCallum 1995, Anderson–van Wincoop 2003) | — |
| ECO-E2-L00368-1 | 23 | CERTO = fonte | ok | ok (⏳ no mBridge) | — |
| ECO-E2-L00553-1 | 21 | ERRADO = fonte | ok | 🧐 explicava o “20” com contas inconsistentes ((100−10)/4,5; “autarquia + excesso de demanda” dá 28) | corrigido: 20 = quantidade demandada a preço zero (100/5) |
| ECO-E2-L01669-1 | 18 | ERRADO = fonte | ok | ok | — |
| ECO-E2-L01155-1 | 21 | ERRADO (resolvido; o verso não tem gabarito escrito, registrado) | ok | ok | — |
| ECO-E2-L00644-1 | 18 | ERRADO = fonte | ok (`[...]` só em item > 600 caracteres) | ok | — |
| ECO-E2-L00575-1 | 18 | ERRADO = fonte | ok | ok | — |
| ECO-E2-L01670-1 | 18 | CERTO = fonte | ok | ok | — |
| ECO-E2-L00508-1 | 21 | ERRADO = fonte | ok | ok | — |

Banca, prova e ano conferidos com a classificação do lote (por exemplo, “Nidi/Jacqueline Bueno” e “Pré-TPS/2023” vêm de `classif`, não foram inventados pelo redator).

## 2. ERRADO: anotada × reescrita (todos os ERRADO dos 6 arquivos)

Conferência automática palavra a palavra (assertiva = anotada; todo `vm` muda ou é suprimido na reescrita; toda mudança está em `hl`/`<s>`; nada inalterado em vermelho; resto idêntico), seguida de releitura manual dos 97 pares.

Cards corrigidos:
- **ECO-E1-0958-1** (cards_23): a reescrita começava com `[…]` num item curto (~470 caracteres). Restaurado o texto integral da assertiva antes do trecho corrigido.
- **ECO-E1-0961-1** (cards_23): mesmo defeito (~560 caracteres). Restaurado o texto integral.

Nenhum outro par com vermelho sem correção, mudança sem realce ou texto divergente da assertiva. Não há cards ME nesses arquivos (só 2 DISC).

Referências entre cards: nenhuma ocorrência de “ECO-E…” no texto dos cards fora de id, fonte_ref, alertas e ids de figura. Nenhuma ocorrência de “item irmão”, “questão anterior” ou “texto acima”.

## 3. Totais

- Amostra: 19 cards. Problemas de gabarito: 0 (os dois casos contestáveis ou anulados já têm ⚠️). Problemas de fidelidade: 0. Problemas de conteúdo: 2, os dois corrigidos (E1-0931-1, E2-L00553-1).
- ERRADO: 97 conferidos (17: 16 · 18: 17 · 19: 15 · 20: 18 · 21: 23 · 23: 8), 2 corrigidos (E1-0958-1, E1-0961-1).
- Referências por id removidas: 0 (nenhuma encontrada).
- `checar_lote.py`: 0 violações em cards_19, 21 e 23, os arquivos editados. cards_17, 18 e 20 não foram alterados e já davam 0 violações.
