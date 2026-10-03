# Revisão C — ECO passada02 (cards_21 … cards_26)

## 1. Amostra (revisao_amostra_C.json, 17 cards)

Checado: gabarito = fonte · assertiva fiel · economia/legislação do comentário · nada inventado · anotada/reescrita (ERRADO).

| Card | Arquivo | Gab. | Resultado |
|---|---|---|---|
| ECO-E3-L00074-1 | cards_24 | C | OK (Barro 1974 e a ressalva de Ricardo estão corretos) |
| ECO-E1-0606-1 | cards_22 | C | OK |
| ECO-E1-0568-1 | cards_21 | C | OK (Musgrave / Giambiagi e Além: processo político como substituto do mercado) |
| ECO-E3-L00384-1 | cards_24 | C | OK |
| ECO-E3-L00209-1 | cards_24 | E | OK (vermelho só em "promove uma elevação do"; reescrita "não altera o") |
| ECO-E1-0628-1 | cards_23 | C | OK (Evans, Amsden, Chang, MRW 1992, Lucas 1988) |
| ECO-E1-0602-1 | cards_22 | C | OK (EC 132/2023, transição 2026–2033, com ⏳) |
| ECO-E1-0320-1 | cards_21 | C | OK |
| ECO-E1-0609-1 | cards_22 | C | OK |
| ECO-E2-L01254-1 | cards_23 | E | OK (o "não" vermelho está riscado com `<s>` na reescrita; acréscimo "privada…" com hl) |
| ECO-E2-L01587-1 | cards_26 | C | OK (Friedman 1957) |
| ECO-E3-L00075-1 | cards_24 | C | OK |
| ECO-E3-L00052-1 | cards_25 | C | OK (CF art. 165, § 5º; Lei 4.320, art. 34 — citações corretas) |
| ECO-E1-0176-1 | cards_21 | E | OK |
| ECO-E2-L00764-1 | cards_25 | C | OK |
| ECO-E3-L00044-1 | cards_25 | E | OK (LRF art. 1º, § 1º; art. 35; Res. SF 40/2001: 2 × RCL para estados e 1,2 × RCL para municípios; Lei 9.496/1997; PROES — tudo correto) |
| ECO-E2-L00314-1 | cards_25 | E | OK (motivo *finance*, 1937) |

Amostra: 17/17 OK, nenhuma edição. Nenhum gabarito diverge da fonte.

## 2. Todos os ERRADO + ME (82 C/E ERRADO + 1 ME)

Verificação automática (alinhamento por palavra entre assertiva, anotada e reescrita) e depois leitura manual de cada par anotada/reescrita.

- Anotada = assertiva em todos os 82, sem lacunas.
- Todo trecho vermelho foi corrigido com hl/`<s>` na reescrita; nenhum trecho vermelho ficou igual; toda mudança está realçada.
- ME ECO-E1-0319-1: (A) toda azul; (B)/(C)/(D)/(E) com vermelho só nos números trocados. OK.
- Nenhuma referência a outro card por id no texto (os ids só aparecem em `alertas`, `fonte_ref` e ids de figura).
- Os ERRADO de gabarito discutível (ECO-E2-L00656-1 e ECO-E3-L00033-1, emissão de dívida × DLSP) já trazem ⚠️ Gabarito contestável.

### ERRADO corrigidos
| Card | Arquivo | Correção |
|---|---|---|
| ECO-E2-L00836-1 | cards_25 | Na reescrita, o "[…]" foi trocado pelo texto completo da 1ª frase. O item é curto (cerca de 420 caracteres), então a reescrita precisa ser idêntica à assertiva fora do trecho corrigido. |

## 3. Totais
- Amostra: 17 cards revisados, 17 OK, 0 editados.
- ERRADO/ME: 83 verificados (82 C/E + 1 ME), 1 corrigido, 82 OK.
- Gabaritos alterados: 0. ⚠️ acrescentados: 0 (os 2 casos discutíveis já tinham ⚠️).
- checar_lote.py: 0 violações em cards_21 … cards_26 (30 + 30 + 30 + 30 + 30 + 7 = 157 cards).
