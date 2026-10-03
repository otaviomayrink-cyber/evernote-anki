# Revisão A — ECO passada 02 (cards_01 a cards_10)

## 1. Amostra (`revisao_amostra_A.json`, 33 cards)

Conferido em cada card: gabarito × fonte (`brutos.jsonl`), fidelidade da assertiva, economia do comentário e dados de prova/autor/citação.

| Card | Arquivo | Gab. | Resultado |
|---|---|---|---|
| ECO-E2-L00423-1 | 02 | CERTO | OK (marca ❌ preservada) |
| ECO-E2-L00923-1 | 08 | CERTO | OK |
| ECO-E2-L00061-1 | 02 | ERRADO | OK |
| ECO-E1-0383-1 | 01 | CERTO | OK |
| ECO-E2-L01308-1 | 06 | CERTO | OK |
| ECO-E2-L00795-1 | 07 | ERRADO | OK |
| ECO-E2-L01335-1 | 04 | CERTO | OK |
| ECO-E2-L00739-1 | 07 | CERTO | OK (tabela NFSP: correção do sinal do nominal de 2022 confere com a identidade e consta nos alertas) |
| ECO-E2-L01334-1 | 04 | CERTO | OK (o erro de sinal do comentário-fonte foi corrigido e anotado) |
| ECO-E2-L01663-1 | 06 | CERTO | OK (convenção BPM5 × BPM6 do comentário-fonte corrigida) |
| ECO-E2-L01333-1 | 04 | CERTO | OK |
| ECO-E2-L00226-1 | 05 | ERRADO | OK |
| ECO-E2-L00560-1 | 05 | CERTO | OK |
| ECO-E2-L00060-1 | 02 | ERRADO | OK |
| ECO-E2-L01319-1 | 06 | CERTO | OK (tabela reconstruída, conforme alerta) |
| ECO-E2-L00935-1 | 06 | CERTO | OK (“7^{a}” → “7ª”, só OCR) |
| ECO-E1-0845-1 | 02 | ERRADO | OK |
| ECO-E1-0796-1 | 05 | ERRADO | OK |
| ECO-E2-L01517-1 | 08 | CERTO | OK |
| ECO-E2-L00056-1 | 09 | CERTO | OK (já traz ⚠️ contestável) |
| ECO-E1-0364-1 | 04 | ME (E) | OK (“tabela acima” → “dados apresentados”, anotado nos alertas) |
| ECO-E2-L01297-1 | 03 | ERRADO | OK |
| ECO-E2-L01317-1 | 06 | CERTO | OK. O item só fecha na convenção BPM5 (conta financeira sem as reservas), e o 📖 já explica isso. Gabarito defensável, sem ⚠️ |
| ECO-E2-L01319-4 | 06 | CERTO | OK |
| ECO-E3-L00416-1 | 04 | CERTO | OK |
| ECO-E2-L00738-1 | 07 | ERRADO | OK (“R 126” → “R$ 126”, só OCR) |
| ECO-E1-0463-1 | 08 | ERRADO | OK |
| ECO-E1-0663-1 | 07 | ERRADO | OK |
| ECO-E2-L01325-1 | 03 | ERRADO | OK |
| ECO-E2-L01344-1 | 09 | ERRADO | OK |
| ECO-E1-0361-1 | 07 | ERRADO | OK (banca provável só nos alertas) |
| ECO-E2-L01288-1 | 06 | CERTO | OK |
| ECO-E2-L00814-1 | 03 | ERRADO | OK (`ano` vazio, embora a seção da fonte seja de 09/2024: omissão, não invenção) |

Bancas, provas e anos conferidos com `nota_origem`, `secao` e `frente` da fonte. Por exemplo, “Nidi/Jacqueline Bueno” vem do nome das notas de origem e “Pré-TPS/2022” vem da data da lista. Não há autor, obra ou citação inventada.

## 2. ERRADO: anotada × reescrita (cards_01 a cards_10)

O diff palavra a palavra entre a anotada e a reescrita foi conferido em todos os ERRADO. Os critérios: vermelho mantido na reescrita, mudança sem `hl`, trecho apagado sem `<s>`/`hl`, `[...]` em item curto e anotada diferente da assertiva. Depois veio a leitura manual de cada par para o critério “só o falso em vermelho”. As 2 ME (E1-0364, E1-0422) também foram conferidas: as alternativas falsas têm o trecho falso em vermelho, e a E1-0422 pede a incorreta.

Cards corrigidos:
- **ECO-E2-L00062-1** (cards_02): o vermelho cobria “pelas receitas arrecadadas através de impostos”, que é verdadeiro. Agora só “apenas” e “sem considerar” estão em vermelho. A reescrita passa a usar `<s>apenas</s>` + `hl(contribuições e demais rendas que recebe, deduzidas)`, e o resto ficou idêntico à assertiva.
- **ECO-E2-L00403-1** (cards_02): “líquidos de subsídios” (verdadeiro) passou para azul. A reescrita destaca só “dos impostos sobre produtos” e “ sobre produtos”.
- **ECO-E2-L00929-1** (cards_03): “foram” estava em vermelho, mas só muda por concordância (“ainda que não tenham sido”). Passou para azul, e a mudança continua destacada na reescrita.
- **ECO-E2-L01326-1** (cards_03): “avaliam-se” estava em vermelho, mas só muda por concordância (→ “avalia-se”). Passou para azul, com a mudança ainda destacada.

Referências a outro card por id no texto dos cards: nenhuma. Os ids que aparecem estão só em `id`, `fonte_ref`, `alertas` e `grafico_verso`.

`checar_lote.py` dá 0 violações em cards_01 a cards_10.

## 3. Totais

- Amostra: 33 cards. Problemas de gabarito: 0. De fidelidade: 0 (só normalizações de OCR já previstas). De conteúdo econômico: 0. ⚠️ acrescentados: 0.
- ERRADO conferidos: 145 C/E + 2 ME (147). Corrigidos: 4.
- Referências por id removidas: 0.
