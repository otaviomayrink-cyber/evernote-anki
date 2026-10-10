# Revisão D — passada 03 (cards_22.py e cards_24.py)

## 1. Amostra (revisao_amostra_D.json)

| Card | Arquivo | Gabarito (fonte → card) | Assertiva fiel | Economia | Dados/autores | ⏳ | Resultado |
|---|---|---|---|---|---|---|---|
| ECO-E3-L00201-1 | cards_22 | CERTO → CERTO | sim | ok (abertura em país pequeno: EP cai, ET sobe; ressalva de país grande correta) | ok | n/a | OK, sem alteração |
| ECO-E3-L00328-1 | cards_22 | ERRADO → ERRADO | sim (só “sem” → “ser”, registrado em alerta) | ok (cota eleva o preço como a tarifa equivalente; diferença está na renda da cota) | ok | n/a | Corrigido: o vermelho cobria “as quotas”, que não muda na reescrita (ver §3) |
| ECO-E1-0969-1 | cards_22 | CERTO → CERTO | sim | ok (petróleo bruto ≈ 7% das importações em 2013; pico perto da metade no início dos anos 1980) | ok, valores aproximados marcados como alerta | sim | OK, sem alteração |
| ECO-E2-L01234-1 | cards_24 | ERRADO → ERRADO | sim | ok (paridade descoberta: ΔEe = 5% − 6% = −1%, A se aprecia) | ok | n/a | OK, sem alteração |
| ECO-E1-0983-1 | cards_22 | ERRADO → ERRADO | sim (“plástiva” → “plásticas”, registrado) | ok (Letec é instrumento do Mercosul; tarifa menor → efeito desinflacionário pontual) | ok, cronologia de 2021–2022 coincide com a fonte | sim | OK, sem alteração |

## 2. cards_24.py: os 10 cards conferidos com a própria linha da fonte

Banca, prova e ano batem com `nota_origem` e com a frente de cada linha: listas Nabuco de 2023 → `Pré-TPS/2023`; Nidi/Jacqueline Bueno → Simulado Abril/2025, Simulado Março/2025, Fevereiro/2025 e Fevereiro/2026. Isso segue a convenção usada em todas as passadas. A marca errei aparece só em E3-L00466 e corresponde ao ❌ da fonte. Os 10 gabaritos são iguais aos da fonte. As assertivas são fiéis: em E3-L00219, o OCR “economías”/“liquido” foi corrigido e há alerta registrando a correção. Não há resto de dados das provas irmãs no texto dos cards: as ligações com outros cards ficam só em `alertas` (`quase_duplicata`). Nenhum erro de economia encontrado. **0 correções.**

| Card | Gabarito | Metadados | Assertiva | Resultado |
|---|---|---|---|---|
| ECO-E2-L01045-1 | ERRADO = fonte | ok | fiel | OK |
| ECO-E2-L01159-1 | CERTO = fonte | ok | fiel | OK |
| ECO-E2-L01234-1 | ERRADO = fonte | ok | fiel | OK |
| ECO-E3-L00219-1 | CERTO = fonte | ok | fiel (OCR corrigido) | OK |
| ECO-E3-L00257-1 | CERTO = fonte | ok | fiel | OK |
| ECO-E3-L00274-1 | ERRADO = fonte | ok | fiel | OK |
| ECO-E3-L00292-1 | ERRADO = fonte | ok | fiel | OK |
| ECO-E3-L00293-1 | CERTO = fonte | ok | fiel | OK |
| ECO-E3-L00466-1 | ERRADO = fonte | ok (errei ✓) | fiel | OK |
| ECO-E3-L00467-1 | ERRADO = fonte | ok | fiel | OK |

## 3. ERRADO: anotada × reescrita (20 cards: 14 em cards_22 e 6 em cards_24; não há ME)

Em todos os 20, a anotada sem as tags é igual à assertiva, e a reescrita, com os trechos em `hl` substituídos, é idêntica à anotada com os trechos em `vm` substituídos. Não há `[…]` e a ordem é a mesma.

Corrigidos (cards_22.py):
- **ECO-E3-L00328-1**: `vm("Apesar de as quotas imporem")` / `hl("Como as quotas impõem")` foi dividido em `vm("Apesar de")` + az(" as quotas ") + `vm("imporem")`, com `hl("Como")` / `hl("impõem")`. “as quotas” não muda na reescrita e deixou de ficar em vermelho.
- **ECO-E3-L00361-1**: o vermelho ficou só em “limita a possibilidade”, e a correção em hl ficou só em “preserva o direito”. O trecho “de aplicação de” não muda e passou para o azul.
- **ECO-E3-L00396-1**: a reescrita mostrava `hl("costuma representar")`, que não altera o texto. Ela passou a mostrar a supressão: `hl("<s>não</s> costuma representar")`.

Sem defeito: E2-L01764, E3-L00035, E3-L00145 (com ⚠️ contestável), E3-L00325, E3-L00398, E3-L00432, E3-L00464, E1-0966, E1-0967, E1-0983, E2-L00349; e, em cards_24, E2-L01045, E2-L01234, E3-L00274, E3-L00292, E3-L00466, E3-L00467.

Observação, sem alteração: em ECO-E2-L00349-1, a primeira frase (“ancorando expectativas… convergência… 3,8% em 2025”) é discutível. Ela ficou em azul porque o gabarito da fonte se decide na segunda frase. O card já explica isso no 📖, com ⏳, e em `nota_redacao`.

Ids de outros cards e expressões como “item irmão”, “questão anterior” e “texto acima”: nenhuma ocorrência fora de `id`, `alertas` e ids de figura.

## 4. Totais
- Amostra: 5 cards revisados. 4 OK e 1 corrigido (anotada/reescrita). Gabaritos alterados: 0. ⚠️ acrescentados: 0. Erros de economia: 0. Dados inventados: 0.
- cards_24: 10/10 conferidos com a fonte, 0 correções.
- ERRADO revisados: 20, dos quais 3 foram corrigidos (E3-L00328, E3-L00361, E3-L00396).
- checar_lote: cards_22.py, 30 cards, 0 violações; cards_24.py, 10 cards, 0 violações.
