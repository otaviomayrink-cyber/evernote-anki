# ❓ Folha de Estilo das Notas de Questões — Caderno CACD — v3
*Documento normativo para criar, converter e consolidar as **notas de questões objetivas** (notas -Q) do caderno, em **qualquer matéria**. Complementa a Folha de Estilo v9: tudo o que a v9 fixa sobre HTML seguro, ENEX, cores e emojis vale aqui, salvo o que esta folha altera. Anexar a todo prompt que produza ou reorganize questões, junto com a Especificação do JSONL e do Relatório (v2) e, quando o lote tiver imagens, o Protocolo de Gráficos (v1).*

**Novidades da v3** — figuras e gráficos
- **§10 novo — Figuras e gráficos**: o que fazer com cada imagem do lote (redesenhar, transcrever, absorver, cortar), onde a figura entra no card, legenda, fidelidade, tamanhos e limites. O *como* (spec, script, lint, revisão visual) está no **Protocolo de Gráficos v1**.
- **§3.1**: figura, tabela ou fórmula do enunciado deixa de virar `[Imagem não reproduzida…]` — é redesenhada, transcrita ou, se irrecuperável, o item vai para a 🧹 Triagem. Enunciado reconstruído leva aviso cinza na frente.
- **§3.2/§3.3**: novo bloco **📈 No gráfico** no verso, entre 📖 e 🧐.
- **§9**: contrato ganha os itens 14 a 19 (figuras).
- Versão no JSONL: `versao_folha = "Q-v3"`.

**Novidades da v2**
- Verso reestruturado: **gabarito → assertiva anotada (azul/vermelho) → linha de separação → comentário**, com a **✍️ Reescrita correta sempre por último** (§3.2).
- Comentário em **núcleo fixo + módulos opcionais** (§3.3–3.4). Saem 🔎 Onde está o ponto, 💡 Por quê, 📐 Regra-âncora, 🚨 Pegadinha e 📎 Comentário da fonte; entram 🎯 Em poucas palavras, 📖 Destrinchando o tema, 🧐 Dissecando a redação do item e os módulos 🧭 📚 ⚖️ 🟣 🧠 😈 🃏 🏛️.
- **Taxonomia fechada de construção do item** (§4), registrada no card e no JSONL.
- **Padrão de qualidade** do comentário (§5), com calibragem de tamanho e ângulos por matéria.
- **Marca ❌ de "errei"** preservada, antes do cabeçalho (§3.1).
- **Título da nota no Evernote**: `{id}-1 - Obj.` (§2).
- **Tabelas sem linha de título** ("Enunciado | Resposta", "Frente | Verso"): toda linha vira flashcard (§7).

---

## 1. O que é uma nota -Q
- Cada nota de conteúdo `NN — Título` tem **uma** nota-irmã de questões, com título `NN-1 - Obj.` no Evernote (§2).
- Reúne **todas** as questões daquele tema, de qualquer origem: provas, apostilas, cadernos antigos, simulados, itens próprios.
- Unidade = **1 card por item julgável**. Uma questão com vários itens gera vários cards; a múltipla escolha (ME) continua ME, em um card.
- Todo card é **autossuficiente**: lido sozinho no NeuraCache, sem a nota e sem a prova, precisa bastar para responder e aprender.

## 2. Estrutura da nota -Q
**Título da nota (ENEX):** `{id}-1 - Obj.` — só isso, para o Evernote ordenar em sequência.
- Exemplos: `010-1 - Obj.` · `07-A-1 - Obj.` · `28-C-1 - Obj.`
- Nota de triagem do lote: `ZZ-Triagem-1 - Obj.` (cai no fim da lista).
- Sem tags.

**Corpo (ordem fixa):**
1. `<h1>📍 Índice</h1>`: lista `<ul>` real com os H2 e a contagem de cards de cada um — ex.: "⚖️ CN × AA: critérios (18)". Sem anotações de progresso.
2. `<hr/>`
3. `<h1>❓ Questões</h1>`
   - **H2 = subtema** (emoji + 2 a 5 palavras), espelhando sempre que possível os H2/H3 da nota de conteúdo-irmã. Evite H2 com um único card quando der para agrupar.
   - Dentro de cada H2, **uma tabela de 2 colunas**, um card por `<tr>`; acima de 60 cards, parta em blocos.
   - **Ordem dentro do H2:** (1) CEBRASPE do CACD/IRBr, do mais recente ao mais antigo; (2) demais CEBRASPE, idem; (3) outras bancas; (4) simulados de curso e professores; (5) banca não identificada; (6) elaboração própria.
4. Na nota de triagem: H2 🧹 por matéria de destino sugerida; itens irrecuperáveis (ilegíveis) listados em `<ul>`, sem card.

⚠️ Não há Box nem Deck nas notas -Q. A tabela de 2 colunas **é** o deck.

## 3. O card

### 3.1 Coluna 1 — FRENTE
```
[❌ ][cabeçalho em código]
(linha em branco)
Comando da questão
Excerto/texto motivador (se houver)
(linha em branco)
Item: / Questão: / Enunciado:
Assertiva (ou enunciado + alternativas)
```
- **Marca ❌ (errei)**: se o item vinha marcado com ❌ na fonte, o card o **preserva**, sem trocar o emoji, **antes do cabeçalho**, na mesma linha: `❌ <code …>[…]</code>`. Nunca criar nem apagar essa marca.
- **Cabeçalho**: `<code style="font-family:monospace; color:#B3261E; background-color:#F6F1F0;">[TIPO - BANCA › Órgão/Cargo/Ano › Subtema]</code>` + `<p><br/></p>`.
  - `TIPO`: `C/E` · `ME` · `EXERC` (exercício aberto) · `DISC` (discursiva curta).
  - `BANCA` normalizada: `CEBRASPE` (CESPE, Cebraspe, UnB), `FGV`, `FCC`, `VUNESP`, `IADES`, `Quadrix`…; cursos/professores sem prova de origem pelo nome (`Campiti`, `Clipping`, `Gran`, `Prof. Fulano`); `Banca não identificada`; `Elaboração própria (padrão CEBRASPE)`. Banca pode ser confirmada por pesquisa quando a fonte traz órgão e ano; sem confirmação, não se preenche.
  - `Órgão/Cargo/Ano`: só o que a fonte informar (`IRBr/CACD/2026`, `TRF-6ª Região/Analista/2025`). Não invente; sem dado, omita.
  - `Subtema`: igual ao nome do H2 (sem emoji).
- **Comando**: sempre completo; se a fonte não traz, comando neutro compatível ("Julgue o item a seguir, relativo ao texto.", "Acerca da política externa do governo Geisel, julgue o item.").
- **Excerto motivador**: o necessário para julgar sem o original, até ~2.500 caracteres, cortes com `[...]`, referência em cinza. Se o item cita linha ou parágrafo, o recorte o contém (`[§3]`).
- **Figura, tabela ou fórmula do enunciado** (§10): gráfico e diagrama → **redesenhados** (PNG gerado, com legenda cinza logo abaixo); tabela → **tabela HTML aninhada** (≥ 3 colunas); fórmula e texto em imagem → **texto**. Entram depois do comando/excerto e antes do `Item:`. Se a figura é indispensável e irrecuperável, o item vai para a 🧹 Triagem — não existe card com `[Imagem não reproduzida]`.
- **Enunciado reconstruído** (a frente da fonte era só uma imagem perdida, §10.4): logo abaixo do comando, em cinza e itálico: `[Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.]`
- **Assertiva**: texto **fiel** (só se corrigem erros evidentes de OCR). Grifos da fonte → `<u><b>…</b></u>`. Na ME, uma alternativa por `<p>`: `(A) …`.
- 🚫 Nunca "o texto acima", "a questão anterior", "o trecho" sem dizer qual.

### 3.2 Coluna 2 — VERSO: esqueleto
```
① Gabarito
(linha em branco)
② Assertiva anotada
③ Linha de separação
④ 🎯 Em poucas palavras
⑤ ⚠️ / ⏳ / 🏛️ (só quando houver)
⑥ 📖 Destrinchando o tema
⑥-bis 📈 No gráfico (só quando houver — §10)
⑦ 🧐 Dissecando a redação do item
⑧ Módulos opcionais (0 a 3): 🧭 📚 ⚖️ 🟣 🧠 😈 🃏
⑨ ✍️ Reescrita correta (sempre por último)
```

**① Gabarito** — primeira linha, sempre:
| Valor | Marcação |
|---|---|
| CERTO | `<p><span style="color: rgb(0, 130, 0);"><b>✅ CERTO</b></span></p>` |
| ERRADO | `<p><span style="color: rgb(200, 0, 0);"><b>❌ ERRADO</b></span></p>` |
| ANULADO | `<p><span style="color: rgb(160, 160, 160);"><b>⚪ ANULADO</b></span></p>` |
| ME | `<p><span style="color: rgb(0, 60, 200);"><b>🔵 Letra C</b></span></p>` |
| EXERC/DISC | `<p><span style="color: rgb(0, 60, 200);"><b>🔵 RESPOSTA</b></span></p>` |

Gabarito oficial sempre prevalece. Se a fonte do caderno diverge do oficial comprovado, vale o oficial, com ⚠️ explicando a troca.

**② Assertiva anotada** — depois de `<p><br/></p>`, a assertiva reproduzida **sem rótulo**, com:
- trechos **corretos** em **azul normal** (sem negrito): `<span style="color: rgb(0, 60, 200);">…</span>`;
- trechos **errados** em **vermelho e negrito**: `<span style="color: rgb(200, 0, 0);"><b>…</b></span>`.

Regras:
- **ERRADO**: só o que é falso fica vermelho; o resto, azul. Numa meia-verdade, a parte verdadeira fica azul.
- **CERTO**: tudo azul; a palavra ou o dado decisivo pode vir sublinhado (`<u>…</u>`) para mostrar onde estava o risco.
- **ANULADO**: vermelho no trecho que gerou a anulação (ambiguidade, erro material).
- **ME**: todas as alternativas, uma por `<p>`, com prefixo `✅` na correta (inteira azul) e `❌` nas erradas (azul + trecho falso em vermelho). O enunciado não se repete.
- **EXERC/DISC**: no lugar da assertiva, a resposta-modelo curta em azul.
- Assertiva muito longa (> ~600 caracteres): pode ser reproduzida com `[...]` nos trechos neutros, preservando todo trecho vermelho.
- ⚠️ Exceção declarada à v9 §5.1 ("todo colorido é negrito"): o azul da assertiva anotada é **sem negrito**, porque ali marca "trecho correto", não conteúdo memorizável.

**③ Linha de separação** — `<hr/>` dentro da célula.
- Se o teste de importação da Fase 0.5 mostrar que o Evernote descarta `<hr/>` em célula, usar: `<p><span style="color: rgb(160, 160, 160);">━━━━━━━━━━━━━━━━━━━━━━━━</span></p>`.

### 3.3 Núcleo do comentário (obrigatório)
| Bloco | Rótulo exato | O que é |
|---|---|---|
| ④ | `<p><b>🎯 Em poucas palavras:</b> …</p>` | O veredito numa frase: por que é certo ou errado. É a linha que se lê em 5 segundos na revisão. |
| ⑥ | `<p><b>📖 Destrinchando o tema:</b></p><ul><li>…</li></ul>` | **A aula.** Justifica o gabarito, mas sobretudo ensina o conteúdo que o item testa: conceito, contexto, casos vizinhos, exemplo e contraexemplo. Quando houver uma regra ou tese reutilizável, ela aparece aqui como uma linha em negrito colorido. Na ME, um `<li>` por alternativa: `(A) ❌ …` / `(C) ✅ …`. |
| ⑥-bis | `<p><b>📈 No gráfico:</b></p>` + figura + legenda | **Opcional.** O gráfico didático que mostra o mecanismo do 📖 (deslocamento, área, interseção), seguido de legenda em cinza e itálico dizendo **o que ele demonstra**. Só quando passa no teste do quadro-negro (§10.2); no máximo um por card. |
| ⑦ | `<p><b>🧐 Dissecando a redação do item:</b> …</p>` | **Pensar como o examinador.** Rótulo(s) da taxonomia (§4) em cinza; moduladores e palavras-gatilho; como o item foi fabricado (o que foi trocado, generalizado ou invertido); a pista que entrega o gabarito; e, quando útil, o padrão recorrente da banca (🔥). 1 a 4 linhas. |
| ⑨ | `<p><b>✍️ Reescrita correta:</b> <i>…</i></p>` | **Obrigatória em todo ERRADO** e **sempre o último bloco**. A menor alteração que torna o item verdadeiro por inteiro — todos os trechos vermelhos da assertiva anotada precisam ter sido corrigidos. O que mudou em `<span style="background-color:#FFEF9E;"><b>…</b></span>`; o trecho falso, se útil, em `<s>…</s>`. Na ME e no ANULADO, opcional. |

Exemplo do bloco:: `<p><b>🧐 Dissecando a redação do item:</b> <span style="color: rgb(160, 160, 160);">[meia-verdade · modulador absoluto]</span> A 1ª oração reproduz o manual; o erro foi enxertado no "exclusivamente" …</p>`

### 3.4 Blocos condicionais e módulos opcionais
**Condicionais** (entram logo após 🎯, porque mudam a leitura do resto):
| Bloco | Quando |
|---|---|
| `⚠️ Gabarito contestável:` | O gabarito oficial é discutível: mantenha-o e explique a divergência e qual resposta seria mais defensável. No ANULADO: motivo provável da anulação e a resposta que seria correta. |
| `⏳ Desatualizado (mês/ano):` | Mudança normativa, factual ou estatística posterior à prova. Se ela inverte o gabarito, diga isso com destaque: `⚠️ Desatualizada: à luz de …, o item hoje seria ERRADO porque…`. |
| `🏛️ Justificativa da banca:` | Existe justificativa oficial de alteração ou anulação (CEBRASPE publica). Reproduzir em cinza, íntegra ou resumida — é fonte primária. |

**Módulos opcionais** — de 0 a 3 por card, só quando acrescentam algo real; nesta ordem:
| Módulo | Rótulo | Para quê | Onde costuma render |
|---|---|---|---|
| 🧭 | `🧭 Panorama:` | Onde o item se encaixa no tema maior: linha do tempo, classificação, conceitos irmãos, antes/depois. | HB, HM, PI, GEO, ECO |
| 📚 | `📚 Autores e teses:` | Autor → obra → tese; correntes historiográficas ou doutrinárias; contestações. Em ocre. | HB, HM, PI, ECO, Direito, PORT (gramáticos) |
| ⚖️ | `⚖️ Base normativa:` | Artigo, tratado, súmula, jurisprudência, com dispositivo em verde. | D.CONST, D.ADMIN, DIP, ECO (normas) |
| 🟣 | `🟣 Posição do Brasil:` | Como o Brasil atuou, votou ou se posicionou. Em roxo. | PI, DIP, PEB, GEO |
| 🧠 | `🧠 Mnemônico:` | Só quando existir um bom. | PORT, Direito |
| 😈 | `😈 Para dificultar:` | Como a banca inverteria o gabarito ou tornaria o item mais difícil: 1 a 3 versões, cada uma com o gabarito que teria. **Toda versão ERRADA traz, entre parênteses e de forma brevíssima, o erro feito** — ex.: *"…exclusivamente pela via diplomática…" → ERRADO (modulador absoluto)*; *"…em 1824…" → ERRADO (data trocada: 1822)*. Muito útil em itens CERTO. | Todas |
| 🃏 | `🃏 Carta na manga:` | Frase, dado ou argumento reaproveitável numa discursiva sobre o tema. | HB, HM, PI, ECO, PEB |

Todos os rótulos em `<p><b>emoji Rótulo:</b> …</p>`; conteúdo longo em `<ul><li>`.

## 4. Taxonomia de construção do item
Todo item C/E e ME recebe **1 ou 2 rótulos** (o principal primeiro), no 🧐 Dissecando a redação e no campo `tipo_erro` do JSONL. Lista fechada; `OUTRO` exige descrição.

**Itens ERRADOS (ou alternativas erradas) — como o erro foi fabricado**
| Código | Rótulo no card | Descrição |
|---|---|---|
| `MEIA_VERDADE` | meia-verdade | Parte verdadeira + parte falsa enxertada |
| `TROCA_CONCEITO` | troca de conceito | Conceito, classificação ou instituto trocado por um vizinho |
| `TROCA_ATOR` | troca de ator | Sujeito, autor, país, órgão ou personagem trocado |
| `DADO_ALTERADO` | dado alterado | Data, número, prazo, artigo ou quórum trocado |
| `GENERALIZACAO` | modulador absoluto | Generalização indevida: sempre, todos, nunca, exclusivamente, qualquer |
| `RESTRICAO` | restrição indevida | Limitação falsa: apenas, somente, única, só |
| `INVERSAO` | inversão | Causa × efeito, regra × exceção, antes × depois, sujeito × objeto invertidos |
| `NEXO_INDEVIDO` | nexo indevido | Relação causal ou lógica inexistente entre dois fatos verdadeiros |
| `ANACRONISMO` | anacronismo | Fato, conceito ou instituição fora do seu tempo |
| `EXTRAPOLACAO` | extrapolação | Afirma além do que o texto ou a fonte autoriza |
| `CONTRADICAO` | contradição | Contraria o texto ou a fonte |
| `JUIZO_INDEVIDO` | juízo indevido | Atribui intenção, valoração ou certeza que a fonte não tem |
| `NORMA_VIOLADA` | norma violada | Reescrita ou construção que fere a norma culta (PORT) |
| `SENTIDO_ALTERADO` | sentido alterado | Reescrita correta na forma, mas que muda o sentido (PORT) |
| `OUTRO` | outro: … | Descrever |

**Itens CERTOS — como o item tenta induzir ao erro**
| Código | Rótulo no card | Descrição |
|---|---|---|
| `PARAFRASE_FIEL` | paráfrase fiel | Reescreve a fonte com sinônimos e ordem diferente |
| `LITERAL` | literalidade | Reproduz a letra da lei, do texto ou do manual |
| `CONTRAINTUITIVO` | contraintuitivo | Verdadeiro, mas contraria o senso comum ou a leitura apressada |
| `MODULADOR_RELATIVO` | modulador relativo | Salvo por "pode", "em regra", "tende a", "em parte" |
| `EXCECAO` | exceção | Cobra justamente a exceção à regra geral |
| `DETALHE` | detalhe | Verdadeiro por um pormenor pouco estudado |

## 5. Padrão de qualidade do comentário
**As três perguntas.** Todo comentário responde:
1. **Por que** o gabarito é esse? (🎯 e 📖)
2. **Que conteúdo** está por trás do item? (📖 e módulos)
3. **Como reconhecer** um item desses da próxima vez? (🧐 e 😈)

**Recheio.** O comentário ensina o tema, não só o gabarito: conceito, contexto, relação com temas vizinhos, exemplo e contraexemplo, e o que a banca costuma cobrar sobre isso. O comentário da fonte é **insumo**: aproveite a melhor formulação, corrija o que estiver errado, amplie o raso e **funda** comentários empilhados (versos com várias respostas de IA repetidas ou contraditórias). Não se preserva o comentário da fonte em bloco próprio; ele fica no JSONL (`comentario_fonte`).

**Calibragem de tamanho** (texto depois da linha de separação):
| Item | Alvo |
|---|---|
| Simples (fato pontual, regra direta) | 150–250 palavras |
| Denso (tema com contexto, tese, polêmica) | 300–500 palavras |
| Teto | ~600 palavras; o excedente pertence à nota de conteúdo |

**Ângulos por matéria** (checklist do redator — escolher os que rendem, não todos):
| Matéria | Ângulos típicos |
|---|---|
| PORT | regra gramatical e gramático; teste prático; efeito de sentido; pegadinha de reescritura |
| HB / HM | contexto e cronologia; causa e consequência; historiografia (autor/tese); comparação entre períodos |
| PEB / PI | posição do Brasil; paradigma ou doutrina de política externa; foro e instrumento; contexto sistêmico |
| DIP | fonte normativa (tratado, costume, CIJ); jurisprudência; posição brasileira; conceito × exceção |
| D.CONST / D.ADMIN | dispositivo; jurisprudência do STF/STJ; exceção; distinção entre institutos |
| ECO | mecanismo (modelo, gráfico mental); dado e ordem de grandeza; escola de pensamento; aplicação ao Brasil |
| GEO | conceito geográfico; escala; dado regional; relação sociedade–natureza |

**Autores e obras.** Cite com segurança. Se o lote trouxer uma **ficha de bibliografia**, cite prioritariamente as obras dela; fora dela, só autores e teses que você conheça sem margem de dúvida. Nunca invente título, data ou citação.

**Dados perecíveis.** Toda informação que envelhece leva `⏳ (mês/ano)` de referência.

**Linguagem.** Português do Brasil, norma culta, tom de professor claro e direto. Sem "Olá", sem "Vamos analisar", sem metalinguagem de edição ("o caderno-fonte diz", "na conversão").

## 6. Semântica visual (herdada da v9, com a exceção de §3.2)
- **Cores** (sempre com `<b>` interno, exceto o azul da assertiva anotada): 🔴 `rgb(200, 0, 0)` erro, regra decisiva, ERRADO · 🔵 `rgb(0, 60, 200)` conceito · 🟢 `rgb(0, 130, 0)` dado, artigo, CERTO · 🟤 `rgb(170, 85, 0)` autor/doutrina · 🟣 `rgb(130, 0, 160)` posição do Brasil · ⚪ `rgb(160, 160, 160)` meta, rótulos da taxonomia, justificativa da banca.
- Highlight `#FFEF9E` com `<b>` interno: termo-chave e correções da reescrita.
- Exemplos linguísticos em `<i>`; afirmação falsa em `<s>`.
- Pelo menos uma cor semântica no comentário (além da assertiva anotada).
- **Emojis de significado fixo nas -Q**: ✅ ❌ ⚪ 🔵 · 🎯 📖 📈 🧐 ✍️ · ⚠️ ⏳ 🏛️ · 🧭 📚 ⚖️ 🟣 🧠 😈 🃏 · 🔥 (tema recorrente) · 🧹 (triagem). Emoji de bandeira proibido.

## 7. Tabela (especificação validada por importação real)
- Exatamente **2 colunas** (frente | verso).
- 🚫 **Nenhuma linha de título na tabela.** Não existe primeira linha com "Enunciado | Resposta", "Frente | Verso", "Questão | Gabarito" nem nada parecido, e nenhum `<th>` ou `<thead>`. No NeuraCache **toda linha vira flashcard**: a tabela começa direto pelo primeiro card, e todo `<tr>` é uma questão.
- `width:1400px` com largura em px nos três lugares: `<colgroup><col/>`, `style` da `<table>` e cada `<td>`; `table-layout:fixed`, `<tbody>` explícito e `<div>` envolvendo a tabela.
- Repartição por peso médio de texto (expoente 0,75, piso 30% por coluna). Célula: `border:1px solid #CCC; padding:8px; vertical-align:top;`. Sem fundo colorido.

## 8. Direcionamento: em qual nota o card entra
1. O destino é a nota cujo **conteúdo** o item testa — não a disciplina da prova nem a posição no arquivo antigo.
2. Item com dois temas: vale o que decide o gabarito; se os dois decidem, fica na nota principal e o subtema menciona o outro.
3. PORT: se o gabarito depende de regra (regência, concordância, conectivo), vai para a nota da regra; se depende do sentido global, para Interpretação.
4. Item de outra disciplina: se o índice fornecido a contém, direcione; se não, 🧹 Triagem com destino sugerido.
5. Sem nota adequada no índice: 🧹 Triagem com sugestão de nota nova.
6. Duplicatas: mesma assertiva e mesma prova = um card só, com o melhor comentário fundido. Itens quase iguais de provas diferentes ficam os dois e se referem um ao outro.

## 9. Contrato de saída testável (por nota -Q)
1. Título `{id}-1 - Obj.`; blocos `📍 Índice` → `<hr/>` → `❓ Questões`.
2. O índice lista todos os H2 com a contagem correta.
3. Toda tabela: 2 colunas, `<colgroup>`, `table-layout:fixed`, `<tbody>`, px em toda `<td>`, soma 1400.
3-bis. Nenhuma linha de título: zero `<th>` e `<thead>`, e o primeiro `<tr>` de cada tabela já é um card (a frente começa pelo cabeçalho `<code>`).
4. Frente: começa por `<code …>[TIPO - …]</code>` (precedido de `❌ ` se e somente se o item vinha marcado) + `<p><br/></p>`.
5. Verso: começa pelo gabarito (✅/❌/⚪/🔵); em seguida, assertiva anotada com ao menos um trecho azul; depois a separação; depois 🎯, 📖 e 🧐, nessa ordem.
6. ERRADO: ao menos um trecho vermelho na assertiva anotada **e** `✍️ Reescrita correta` como último bloco.
7. CERTO: nenhum trecho vermelho na assertiva anotada.
8. 🧐 com ao menos um rótulo da taxonomia (§4) em C/E e ME.
9. No máximo 3 módulos opcionais por card. No 😈 Para dificultar, toda versão ERRADA termina com o erro entre parênteses.
10. Zero "o texto acima", "questão anterior" ou "(ℓ." sem excerto correspondente.
11. Zero `<style>`, `class=`, `<mark>`, `&nbsp;`, emoji de bandeira. XML válido.
12. Todo ⏳ com data entre parênteses.
13. Nenhum card fora de H2.
14. Toda figura é `<en-media type="image/png" … width="N"/>` com `<resource>` correspondente (md5) no ENEX; nenhum `<img>`, nenhum `<resource>` sobrando; `N` ≤ largura da coluna − 30.
15. Toda figura é seguida, na linha de baixo, da legenda em cinza e itálico.
16. No máximo 2 figuras por lado do card; no verso, a figura fica dentro de `📈 No gráfico`, entre 📖 e 🧐.
17. Zero `[[IMAGEM`, `[Imagem não reproduzida`, tabela como imagem de terceiros ou print da fonte.
18. Toda figura `conjectural` tem alerta `figura_conjectural` no JSONL; todo enunciado reconstruído tem alerta `texto_reconstruido` e o aviso cinza na frente.
19. Toda figura de verso passou pelas `checar` da spec (zero erros no `qgraf.py`).

## 10. Figuras e gráficos
*O **como** — spec JSON, script `qgraf.py`, modelos prontos, lint e revisão visual — está no Protocolo de Gráficos v1. Aqui ficam as regras que o card precisa cumprir.*

### 10.1 O que fazer com cada imagem do lote
| Imagem | Na frente | No verso |
|---|---|---|
| Gráfico, diagrama | **redesenhar** (obrigatório) | redesenho **didático** só se passar no teste do quadro-negro; senão, cortar |
| Tabela | **tabela HTML aninhada** (≥ 3 colunas, `<td><b>` no cabeçalho, nunca `<th>`) | absorver no 📖 |
| Fórmula | texto (Unicode, `<sub>`, `<sup>`) | texto no 📖 |
| Texto em imagem | transcrever | absorver no 📖 |
| Questão inteira em imagem | pedir reenvio; senão reconstruir (§10.4) | — |
| Mapa | descrever em texto; se indispensável, 🧹 Triagem | cortar |
| Decorativa, print de site, “Getty Images” | cortar | cortar |

Imagens de terceiros **nunca** entram (v9 §6): tudo o que entra é redesenho próprio, com spec versionável.

### 10.2 Teste do quadro-negro (gráfico didático no verso)
Entra se **as três** forem sim: (1) um professor desenharia isso no quadro para explicar este item; (2) o gabarito depende de um mecanismo gráfico (deslocamento, interseção, área, inclinação); (3) o desenho mostra algo que o 📖 explica mal em palavras. **No máximo um gráfico por verso** (painéis lado a lado contam como um). Itens irmãos compartilham a figura da frente.

### 10.3 Posição, legenda e tamanho
- **Frente**: depois do comando e do excerto, antes do `Item:`. Legenda = a da prova (“Gráfico 1 — …”); se a figura foi deduzida, acrescentar *(figura redesenhada; traçado aproximado)*. Rótulos iguais aos da prova.
- **Verso**: no bloco `📈 No gráfico:`, entre 📖 e 🧐. Legenda = **o que o gráfico demonstra** (1–2 frases), não um título.
- Legenda sempre em `<p><span style="color: rgb(160, 160, 160);"><i>…</i></span></p>` logo abaixo da figura.
- Exibição: **540 px** na frente, **660 px** no verso. Com figura ou tabela na frente, a 1ª coluna tem no mínimo **600 px**; com figura no verso, a 2ª tem no mínimo **720 px** (a soma continua 1400).
- **A figura da frente não entrega o gabarito**: só mostra o que a prova mostrava — nada de equilíbrio novo, seta-resposta ou área destacada que não estava lá.

### 10.4 Fidelidade
| Valor | Quando | Marcação |
|---|---|---|
| `fiel` | redesenho com todos os dados da fonte (valores, rótulos, áreas) | — |
| `conjectural` | figura deduzida de descrição, comentário ou convenção de livro-texto | legenda com *(figura redesenhada; traçado aproximado)* + alerta `figura_conjectural: o que foi deduzido` |
| `didatica` | gráfico novo do verso | — |

**Enunciado reconstruído** (frente que era só imagem, sem reenvio): só se o comentário permitir reconstruir a assertiva com segurança; alerta `texto_reconstruido` e aviso cinza na frente (§3.1). Sem segurança → 🧹 Triagem, listado como irrecuperável.

### 10.5 Cores e convenções do gráfico
Mesma paleta da v9, com a cor marcando a **família** da curva: 🔵 demanda/IS/DA · 🟤 oferta/LM/OA · 🟣 terceira curva (BP, CMe, (n+δ)k) · 🟢 quarta (RMg) · 🔴 seta de deslocamento e curva que muda o resultado · ⚪ referência tracejada. Curva antes do choque esmaecida; depois, cheia. Áreas em tons suaves: azul (EC), ocre (EP), verde (receita), vermelho (peso morto), amarelo `#FFEF9E` (gasto). O estilo é aplicado pelo script; a IA não escolhe cor nem fonte.

### 10.6 Coerência com o comentário
Todo gráfico de verso declara, na spec, as **checagens** do que o comentário afirma (direção do preço, valores de equilíbrio, áreas). Checagem que falha é tratada como possível erro do **comentário**, não só do desenho. Toda tabela transcrita confere identidades (nominal = primário + juros; BP fecha); incoerência da transcrição → correção pela identidade + alerta `transcricao_incoerente`.

