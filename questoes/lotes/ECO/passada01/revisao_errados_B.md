# Revisão dos itens ERRADO e das referências entre cards — cards_10.py a cards_18.py

Escopo: `lotes/ECO/passada01/cards/cards_10.py` … `cards_18.py`. Referência: Folha de Estilo -Q v3, §3.2 e §3.3.
Os lotes não têm cards ME; foram conferidos todos os itens com gabarito ERRADO.

## Totais

| Medida | Total |
|---|---|
| Itens ERRADO conferidos | 133 (10: 12 · 11: 22 · 12: 16 · 13: 13 · 14: 15 · 15: 14 · 16: 12 · 17: 17 · 18: 12) |
| Cards com anotada ou reescrita corrigida | 28 (anotada: 15 · reescrita: 17; 4 cards tiveram as duas) |
| Referências a id de outro card retiradas do texto | 24, em 23 cards (mais 1 menção a "item irmão" sem id) |
| `checar_lote.py` | 0 violações nos 9 arquivos |

## Task 1: anotada e reescrita

Critérios aplicados:
- trecho vermelho que fica igual na reescrita foi passado para azul;
- trecho alterado na reescrita sem realce recebeu `hl`;
- texto azul que a reescrita apagou ou mudou sem necessidade foi restaurado.

O conteúdo econômico das reescritas não foi alterado.

### cards_11.py
- **ECO-E1-0811-1** (anotada): "é" saiu do trecho vermelho, porque se mantém na reescrita; o vermelho ficou só em "maior do que o".
- **ECO-E1-0834-1** (reescrita): o realce passou a cobrir "substitutos perfeitos", e não só "perfeitos", porque "substitutos" estava vermelho e não tinha correção marcada.
- **ECO-E1-0837-1** (anotada): o bloco vermelho foi dividido. Ficaram vermelhos "sabemos", "um bem" e "provocará"; "que o aumento no consumo de" e "sempre", que não mudam, ficaram azuis.
- **ECO-E2-L00015-1** (anotada): ficaram vermelhos só "não é possível" e ", pois isso contrariaria"; "que uma curva de indiferença seja côncava" e "o princípio de monotonicidade", que não mudam, ficaram azuis.

### cards_12.py
- **ECO-E2-L01460-1** (reescrita): o texto azul "as combinações representadas mais à direita", que a reescrita tinha trocado, foi restaurado. A precisão "(em curvas mais afastadas da origem)" agora vem realçada.
- **ECO-E2-L01462-1** (anotada): "a sua inclinação", que não muda, saiu do vermelho.
- **ECO-E2-L01691-1** (reescrita): foram restaurados o azul "seu consumo" e a vírgula do original, que a reescrita tinha apagado sem marcar; o realce ficou em "de A e de B na mesma proporção".
- **ECO-E3-L00076-1** (reescrita): a troca "às" → "as" não estava realçada; recebeu `hl`.

### cards_13.py
- **ECO-E1-0193-1** (anotada): "ao efeito substituição", que não muda, saiu do vermelho.

### cards_14.py
- **ECO-E1-0228-1** (anotada e reescrita): a troca "no" → "na" não estava realçada. O vermelho passou a ser "no mesmo custo de produção" e o realce, "na mesma quantidade produzida".
- **ECO-E2-L01218-1** (reescrita): o realce passou a cobrir "não respeita", porque "respeita" estava vermelho e não tinha correção marcada.

### cards_15.py
- **ECO-E2-L01725-1** (anotada): "ter", que não muda, saiu do vermelho; o vermelho ficou em "não poderá".

### cards_16.py
- **ECO-E1-0009-1** (reescrita): foi retirado um "da" que tinha sido inserido sem realce ("e quantidade ofertada", como no original).
- **ECO-E1-0261-1** (reescrita): foi restaurado o azul "mesma", que a reescrita tinha apagado sem marcar.

### cards_17.py
- **ECO-E2-L00344-1** (reescrita): o "mas" sem realce voltou a ser o "e" do original.
- **ECO-E2-L00478-1** (reescrita): a reescrita mudava o trecho azul "só se produz quando o preço é superior ao custo". Agora o trecho fica intacto e só "total médio" é corrigido, para `hl("variável médio")`.
- **ECO-E2-L00630-1** e **ECO-E2-L01189-1** (reescrita): a troca "existem" → "existam" passou a ficar dentro do realce, que agora é `hl("embora existam")`.
- **ECO-E2-L00631-1** e **ECO-E2-L01190-1** (reescrita): foram restaurados o texto azul "pode ser representada por uma curva … com relação aos preços", que a reescrita tinha apagado ou trocado. A correção ficou em `hl("perfeitamente elástica (horizontal)")`.
- **ECO-E2-L00849-1** (anotada): "a expressão dada para C", que não muda, saiu do vermelho; o vermelho ficou em "dividir por q".
- **ECO-E2-L01188-1** (anotada): o vermelho ficou só em "total", porque "médio" se mantém.
- **ECO-E2-L01396-1** (reescrita): o realce passou a cobrir "variável médio", porque "médio" estava vermelho e não tinha correção marcada.
- **ECO-E2-L01425-1** (anotada e reescrita): "vai" saiu do vermelho. Foi restaurado o azul ", ainda que com prejuízo", que a reescrita tinha trocado, e o complemento "(limitado ao custo fixo)" veio realçado.

### cards_18.py
- **ECO-E2-L01465-1** (anotada e reescrita): "deve" saiu do vermelho. A reescrita "suspender a fabricação desse bem" trocava "esse" por "desse" sem realce; passou a ser `hl("deixar de fabricar")` + " esse bem".
- **ECO-E2-L01501-1** (anotada): "condição que", que não muda, saiu do vermelho.
- **ECO-E2-L01593-1** (anotada): o vermelho ficou só em "longo" ("No … prazo" não muda).
- **ECO-E1-0241-1** (reescrita): a troca "é" → "seja" não estava realçada; recebeu `hl`.

Pontos conferidos e mantidos como estavam:
- [...] usado para resumir a assertiva na reescrita (ECO-E1-0202-1, ECO-E1-0013-1, ECO-E2-L00019-1, ECO-E2-L00343-1, ECO-E2-L00849-1).
- "[...]" em vermelho para marcar a assertiva truncada (ECO-E1-0195-1).
- Correção de crase "a" → "à" (ECO-E2-L01387-1), por ser correção de erro evidente.
- Reestruturações em que todo o texto alterado já estava realçado (por exemplo ECO-E1-0006-1, ECO-E2-L00848-1, ECO-E3-L00407-1).

## Task 2: referências a id de outro card

Cada frase foi reescrita sem o id, mantendo o contraste útil, ou apagada quando não acrescentava nada. Onde o outro item é quase duplicata, o vínculo continua em `alertas` como `quase_duplicata: …`. Isso já existia em todos esses pares: 0432/0687, 0434/0688, L00078/L00236, 0188/0836, L00535/L00865 e 0231/0305.

- **cards_10.py**:
  - ECO-E1-0191-1 (dissecando): "Itens irmãos: … (“inferior”)" virou "A banca também cobra a versão com “inferior” no lugar de “igual”, igualmente ERRADO."
  - ECO-E1-0201-1 (dissecando): "Item espelho: …" virou "A banca também cobra a utilidade como “medida objetiva”, que é ERRADO."
  - ECO-E1-0202-1 (dissecando): "Item espelho: …" virou uma frase com a versão CERTO (a utilidade ordinal só permite comparações relativas).
  - ECO-E1-0207-1 (dissecando) e ECO-E1-0209-1 (dissecando): "Ver …" apagado.
  - ECO-E1-0432-1 (dissecando): "Itens irmãos: …" virou "A banca recicla a construção em outros simulados, inclusive com “estritamente superior” no lugar de “igual” — sempre ERRADO."
  - ECO-E1-0433-1 (destrinchando): "Ver …" apagado.
  - ECO-E1-0434-1 (dissecando, 2 referências): "— ver ECO-E1-0632-1" virou ", que é ERRADO"; "Item irmão: …" apagado.
  - ECO-E1-0687-1 (dissecando): "Mesma construção de ECO-E1-0432-1 (Clipping, 2025)" virou "Construção recorrente nos simulados Clipping".
  - ECO-E1-0688-1 (dissecando): "Item irmão: …" apagado.
  - ECO-E1-0807-1 (destrinchando): "(ver …)" apagado.
- **cards_11.py**: ECO-E2-L00671-1 (destrinchando): "(ver ECO-E1-0841-1)" apagado.
- **cards_12.py**:
  - ECO-E3-L00078-1 (dissecando): o id foi retirado e ficou "O mesmo item caiu também no Simulado Março/2025."
  - ECO-E3-L00236-1 (dissecando): o id foi retirado e mantido "Item idêntico ao do Simulado Julho/2025".
  - ECO-E3-L00146-1 (dissecando): "item irmão (…)" virou "a versão que usa “pode-se garantir” numa cesta que domina a outra: aí a garantia vem da monotonicidade, e o item é CERTO."
  - ECO-E3-L00148-1 (destrinchando): "Contraste com ECO-E3-L00146-1" virou "Contraste com a versão"; no dissecando, "do item irmão (“é possível”)" virou "da versão com “é possível”".
  - ECO-E3-L00373-1 (dissecando): "(ver …)" apagado.
- **cards_13.py**: ECO-E1-0188-1 e ECO-E1-0836-1 (dissecando): os ids foram retirados e a menção ao reaproveitamento do item foi mantida.
- **cards_15.py**: ECO-E2-L00535-1 e ECO-E2-L00865-1 (destrinchando): o item "Item quase idêntico … : ECO-…" foi apagado (o vínculo já está em alertas).
- **cards_16.py**: ECO-E1-0231-1 e ECO-E1-0305-1 (destrinchando): o texto virou "A banca também cobra a versão com “…” no lugar de “…”, também CERTO."

Ficaram como estavam:
- ids em `id`, `fonte_ref`, `alertas`, `grafico_verso`, `frente_figuras`, `figuras_fonte[].acao` e `comentario_fonte`, que são metadados e não aparecem no card;
- a menção "cf. ECO-E2-L00671-1" em um alerta de ECO-E1-0841-1, porque está em `alertas`.
