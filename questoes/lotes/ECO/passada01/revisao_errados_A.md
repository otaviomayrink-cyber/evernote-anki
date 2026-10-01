# Revisão dos ERRADO: lote A (cards_01 a cards_09)

Critérios (Folha -Q v3 §3.2 e §3.3):
- na assertiva anotada, só o falso fica vermelho;
- todo trecho vermelho é corrigido na reescrita;
- toda mudança na reescrita fica em `hl(...)`;
- o que não muda na reescrita não fica vermelho;
- a reescrita é fiel à assertiva no resto.

Além disso, foram tiradas dos campos de texto as referências a outros cards por id; o vínculo ficou só em `alertas` (`quase_duplicata:`).

## Totais
- **ERRADO conferidos:** 125 C/E, mais 1 ME (ECO-E2-L01377-1, sem ajuste).
- **Cards com anotada/reescrita corrigida:** 30.
- **Referências a id removidas de campos de texto:** 10 frases, com 11 ids, em 10 cards, todos de cards_04. Sete alertas `quase_duplicata` foram criados ou completados.
- `checar_lote.py`: 0 violações em cards_01 a cards_09.

## Task 1: anotada e reescrita

### cards_01
- **ECO-E1-0003-1**: o vermelho passou a ser só “ao longo”, porque “deslocamento” e “da curva” se mantêm. Na reescrita, a supressão aparece como `hl(<s>ao longo</s>)` e o acréscimo “para a direita” fica realçado; o texto que não muda saiu do realce.
- **ECO-E1-0015-1**: a reescrita reordenava o sujeito (“a economia americana aproximou-se…”). Agora mantém o original, “a curva de possibilidades de produção da economia americana”, seguido de `hl(não foi deslocada: a economia aproximou-se dela)`.
- **ECO-E1-0032-1**: no vermelho, “se ela imprimir a sua própria moeda” virou “se” + “imprimir”, e “a sua própria moeda” ficou azul. Na reescrita, “imprima” (mudança de modo verbal) passou a ter realce.
- **ECO-E1-0038-1**: o vermelho é “são de livre acesso” e a reescrita realça “são escassos e não são de livre acesso”. “A todos os agentes econômicos” não muda e ficou azul.
- **ECO-E1-0039-1**: o vermelho foi reduzido a “são destituídos de”, que a reescrita troca por “recebem”. “Atribuição de valor” se mantém e ficou azul.

### cards_02
- **ECO-E1-0059-1**: o vermelho é “da quantidade de equilíbrio” e a reescrita realça “a redução da quantidade de equilíbrio”. Antes, o realce cobria só “a redução” e deixava o trecho vermelho sem correção marcada.
- **ECO-E1-0067-1**: o vermelho virou “significa que ele vai necessariamente” e o realce da reescrita foi ampliado para “não significa que ele vá necessariamente”. “O que” e “adquirir/consumir” ficaram azuis.
- **ECO-E1-0079-1**: “uma redução” → “um aumento”. O artigo, que também muda, entrou no vermelho e no realce.

### cards_03
- **ECO-E1-0205-1**: o artigo “um” saiu do vermelho, porque não muda.
- **ECO-E1-0234-4**: o vermelho foi reduzido a “a mesma”, corrigido por `hl(menor que a)`. “Será” e “de antes da epidemia” ficaram azuis.
- **ECO-E2-L00746-1**: a assertiva tem cerca de 250 caracteres, e a Folha só admite `[…]` acima de cerca de 600. Por isso a anotada e a reescrita voltaram ao texto completo. A reescrita também havia cortado “é correto afirmar que” sem marcação, e o trecho foi reposto. O vermelho passou a ser “pode ser explicado”, corrigido por `hl(não pode ser explicado)`.
- **ECO-E2-L00747-1, ECO-E2-L00748-1, ECO-E2-L00749-1**: pelo mesmo motivo, a anotada e a reescrita voltaram ao texto completo, inclusive “é correto afirmar que”, que tinha sumido da anotada.
- **ECO-E3-L00378-1**: “<i>coeteris paribus</i>” não muda e saiu do vermelho. No 3º trecho, o vermelho foi reduzido a “avalia cada um deles de forma isolada”, porque “uma vez que o consumidor” se mantém.

### cards_04
- **ECO-E1-0091-1**: “auferida pelo vendedor” não muda e saiu do vermelho.

### cards_05
- **ECO-E1-0630-1**: a reescrita havia apagado sem marcação a glosa “isto é, que ambos tenham elasticidade-renda da demanda maior que um”, que foi reposta. O realce agora cobre o trecho vermelho inteiro, “não é possível”.
- **ECO-E2-L00420-1**: o vermelho virou “dispensa” e a reescrita realça “não dispensa”. “Avaliar delimitação de mercado” ficou azul.

### cards_06
- **ECO-E3-L00272-1**: a assertiva tem cerca de 440 caracteres. A anotada e a reescrita voltaram ao texto completo, sem `[…]`.
- **ECO-E1-0130-1**: a reescrita voltou ao texto completo, sem `[…]`.
- **ECO-E1-0134-1**: o vermelho é “é um fenômeno exclusivo” e a reescrita realça “não é um fenômeno exclusivo”. “Dos mercados em concorrência perfeita” ficou azul.

### cards_07
- **ECO-E1-0153-1**: o vermelho foi reduzido a “garante”, corrigido por `hl(não garante, por si só,)`. “Maior equidade social” ficou azul.
- **ECO-E1-0164-1**: a vírgula acrescentada na reescrita entrou no realce.

### cards_08
- **ECO-E1-0173-1**: “do bem” não muda e saiu do vermelho.
- **ECO-E1-0235-3**: a reescrita havia apagado sem marcação “o valor relativo a”, que foi reposto. A correção ficou `hl(apenas parte da incidência)`.
- **ECO-E2-L00729-1**: a vírgula acrescentada na reescrita entrou no realce.
- **ECO-E2-L01037-1**: o vermelho “oferta de 50” foi dividido em “oferta” e “50”, porque o “de” não muda.

### cards_09
- **ECO-E2-L01392-1**: “excesso de oferta” se mantém na reescrita e saiu do vermelho.
- **ECO-E3-L00008-1**: o vermelho foi reduzido a “corrige”, corrigido por `hl(em regra não corrige)`. “Falhas de mercado” ficou azul.
- **ECO-E3-L00017-1**: o vermelho foi reduzido a “pressupõe”, corrigido por `hl(não pressupõe)`. “A equidade” ficou azul.

## Task 2: referências a outros cards (todas em cards_04, campo `dissecando`)
- **ECO-E1-0011-1**: a frase “Item-irmão, quase idêntico: ECO-E1-0114-1.” foi apagada; o alerta `quase_duplicata` já existia.
- **ECO-E1-0100-1**: agora diz “A banca também cobra a versão mais precisa (…), igualmente ERRADO.” O alerta já existia.
- **ECO-E1-0101-1**: agora diz “A banca também cobra a versão com “mais elástica”, que é ERRADO.” Ganhou o alerta `quase_duplicata: ECO-E1-0110-1`.
- **ECO-E1-0106-1**: a frase “Itens-irmãos: ECO-E1-0101-1, ECO-E1-0104-1.” foi apagada. Ganhou o alerta `quase_duplicata` com os dois ids.
- **ECO-E1-0107-1**: agora diz “A banca também cobra a versão vaga (…), igualmente ERRADO.” O alerta já existia.
- **ECO-E1-0108-1**: agora compara com a versão modalizada citada por extenso. Ganhou o alerta `quase_duplicata: ECO-E1-0102-1`.
- **ECO-E1-0109-1**: a versão CERTO passou a ser citada por extenso. Ganhou o alerta `quase_duplicata: ECO-E1-0088-1`.
- **ECO-E1-0110-1**: agora diz “a banca também cobra a mesma frase com “mais inelástica” (CERTO)”. Ganhou o alerta `quase_duplicata: ECO-E1-0101-1`.
- **ECO-E1-0114-1**: as duas referências viraram “A banca também cobra o espelho com sinal negativo (…), igualmente CERTO.” Ganhou o alerta `quase_duplicata: ECO-E1-0115-1`.
- **ECO-E1-0115-1**: agora diz “Espelho do item com sinal positivo (positiva → substitutos, também CERTO).” Ganhou o alerta `quase_duplicata: ECO-E1-0114-1`.

Os outros `ECO-E…` encontrados pelo grep ficam em `figuras_fonte`, `alertas`, `grafico_verso` e `frente_figuras` e foram mantidos.
