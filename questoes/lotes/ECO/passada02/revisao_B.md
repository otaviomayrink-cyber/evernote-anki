# Revisão B — ECO passada 02 (cards_11 … cards_20, cards_27)

## 1. Amostra (revisao_amostra_B.json, 33 cards)

Cada card foi conferido contra `brutos.jsonl`. Itens verificados: gabarito, fidelidade da assertiva, economia do comentário e dados da prova, autores e citações.

| Card | Arquivo | Gab. | Resultado |
|---|---|---|---|
| ECO-E2-L01476-1 | 14 | C | OK |
| ECO-E3-L00133-1 | 12 | C | OK (alerta de ano ANTT 2023/2024 já registrado) |
| ECO-E2-L01701-1 | 16 | E | OK |
| ECO-E2-L00310-1 | 19 | E | OK |
| ECO-E2-L00130-1 | 15 | C | OK |
| ECO-E2-L00319-1 | 20 | E | OK |
| ECO-E2-L01340-1 | 12 | C | OK (⚠️ contestável já presente e justificado) |
| ECO-E2-L00585-1 | 15 | E | **corrigido**: 📖 rotulava como “paradoxo da parcimônia” a queda do investimento; o rótulo agora fica com a tentativa de poupar mais |
| ECO-E2-L00482-1 | 18 | E | OK |
| ECO-E1-0524-1 | 17 | C | OK |
| ECO-E1-0169-1 | 20 | E | OK |
| ECO-E2-L00150-1 | 12 | E | OK |
| ECO-E2-L00919-1 | 14 | E | OK |
| ECO-E2-L00539-1 | 15 | C | OK |
| ECO-E3-L00349-1 | 12 | C | OK |
| ECO-E1-0812-1 | 12 | C | OK (CEBRASPE confirmada como banca do CACD desde 2024) |
| ECO-E1-0830-1 | 20 | E | OK |
| ECO-E2-L01230-1 | 19 | C | OK |
| ECO-E2-L00721-1 | 18 | E | OK |
| ECO-E3-L00173-1 | 12 | E | OK |
| ECO-E2-L00317-1 | 19 | C | OK |
| ECO-E1-0511-1 | 14 | E | OK |
| ECO-E2-L00838-1 | 14 | E | OK |
| ECO-E2-L00940-1 | 11 | E | OK |
| ECO-E2-L01602-1 | 13 | C | OK |
| ECO-E2-L00989-1 | 16 | E | OK |
| ECO-E2-L00387-1 | 19 | C | OK |
| ECO-E2-L01006-1 | 12 | C | OK |
| ECO-E1-0787-1 | 20 | E | OK (CEBRASPE/CACD 2024 confirmada) |
| ECO-E2-L00727-1 | 11 | E | OK |
| ECO-E2-L01676-1 | 13 | E | OK |
| ECO-E3-L00132-1 | 13 | C | OK |
| ECO-E3-L00025-1 | 16 | C | OK |

Gabaritos: os 33 batem com a fonte. Nenhum gabarito oficial é economicamente insustentável sem ⚠️; o único discutível (L01340) já traz o bloco.

Marca ❌ (errei): o campo `errei` foi conferido com a frente da fonte em todos os 297 cards dos arquivos. Não há divergência.

## 2. ERRADO: anotada × reescrita (todos os ERRADO dos arquivos)

Os arquivos não têm cards ME. A conferência automática passou por todos os 149 cards ERRADO. Ela verificou cinco pontos:
- o texto da anotada é igual à assertiva;
- só há trechos az/vm;
- todo trecho vermelho cai numa parte alterada da reescrita (hl ou `<s>`);
- o texto fora de hl/`<s>` é idêntico à assertiva, na mesma ordem e sem `[…]`;
- não há hl sobre texto que não mudou.

Depois, os 149 pares foram lidos um a um, para conferir se o vermelho marca só o que é falso.

Card corrigido:
- **ECO-E2-L01339-1** (cards_12): a inserção “adverso” deixava fora do realce um espaço acrescentado (“impacto ” fora do hl). O espaço passou para dentro do `hl(" adverso")`, e o texto fora do realce agora é idêntico à assertiva.

## 3. Referências a outro card por id

Busca por `ECO-E[0-9]` em todos os campos de texto do card, excluídos id, fonte_ref, alertas, ids de figura e comentario_fonte: 0 ocorrências. Nada foi removido.

## 4. Totais

- Amostra: 33 cards. Gabarito: 0 problemas. Fidelidade da assertiva: 0. Conteúdo: 1 (L00585, rótulo indevido, corrigido). Dados da prova, autores e citações inventados: 0.
- ERRADO: 149 conferidos, 1 corrigido (L01339, espaço fora do realce).
- Referências a id removidas: 0.
- Arquivos editados: cards_12.py e cards_15.py. `checar_lote.py` dá 0 violações em todos os arquivos (11–20 e 27).
