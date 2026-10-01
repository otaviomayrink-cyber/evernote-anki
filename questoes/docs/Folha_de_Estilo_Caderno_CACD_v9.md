# 📐 Folha de Estilo do Caderno CACD — v9
*Documento normativo para conversão e criação de notas. Limites marcados como "recomendação" podem ser excedidos quando o conteúdo exigir. Anexar este documento a todo prompt de conversão/criação.*

**Novidades da v9** — todas decorrentes de teste de importação real no Evernote (set/2026):
- **§8 reescrito**: especificação de tabela validada empiricamente. O Evernote **descarta largura em porcentagem** e **descarta `text-align` na célula**. Larguras agora em **pixel**, obrigatoriamente em `<colgroup>` + `<table>` + cada `<td>`, com `table-layout:fixed` e `<tbody>` explícito. Centralização só sobrevive em `<div>` interno.
- **§8.9 — larguras canônicas**: tudo a **1400px**. Deck na proporção **1 : 2,4** (412 | 988); tabelas de conteúdo e C/E repartidas por peso de texto; Box em célula única de 1400px.
- **§1 Alinhamento** corrigido: centralização das tabelas de conteúdo via `<div style="text-align:center">` dentro da célula, nunca `text-align` na `<td>`.
- **§5 emoji do pulo do gato**: fixado em **👆🏻** (a v8 grafava ☝🏻 e havia notas com 🐱 — as três variantes convergem para 👆🏻).
- **§5 highlight**: fixado em **`#FFEF9E`** com `<b>` interno (dupla proteção), substituindo o `#FFE873` da v8.
- **§6 reescrito**: a IA agora **gera** diagramas e esquemas próprios em PNG, com especificação de estilo e de fonte versionável. A regra da v8 ("a IA não insere imagens") passa a valer só para **imagens de terceiros**.
- **§11 novo — Saída em ENEX**: o formato de entrega passa a ser `.enex`, individual e consolidado por lote.
- **§12 novo — Contrato de saída testável**: lista de invariantes verificáveis por script, que torna auditável um acervo de centenas de notas.
- **Emojis de bandeira são proibidos** (o Evernote não os renderiza) — §5.
- Entidade `&nbsp;` proibida no HTML gerado (quebra o parser de ENEX) — usar `&#160;`.

**Mini-glossário**: "canônico" = a versão oficial e única de referência. Card canônico: após fundir duplicatas, o único card que representa aquele fato no caderno. Ordenação canônica: a sequência de tópicos oficialmente adotada para a matéria.

---

## 1. Estrutura da nota (ordem fixa dos 4 blocos, cada um em H1)

1. 📍 **Índice**
2. 💯 **Caderno Estratégico**
3. ⚡ **Box de Revisão Relâmpago**
4. 👾 **Deck de Flashcards**

*(Bloco extra opcional, quando o lote previr: ❓ **Questões C/E**, ao final.)*

**REGRA DE OURO DAS TABELAS**: tabelas de ESTRUTURA são exclusivas do Deck (2 colunas: frente | verso) e do Box de Revisão Relâmpago (célula única). Índice e Caderno Estratégico são **texto solto**. Exceção: tabelas de CONTEÚDO (comparativos, quadros-síntese) podem existir dentro do Caderno Estratégico.

**🚨 REGRA ANTI-NEURACACHE (2 colunas = flashcard)**: o NeuraCache interpreta QUALQUER tabela de 2 colunas como deck de cards. Portanto, tabela de exatamente 2 colunas só existe no Deck de Flashcards e na tabela de Questões C/E. Tabela de conteúdo do Caderno Estratégico que "pediria" 2 colunas deve ganhar uma **terceira coluna** — a solução mínima é uma coluna de numeração (nº: 1, 2, 3…); melhor ainda se a terceira coluna for semântica (critério, período, exemplo).

**Alinhamento**: tabelas/quadros de conteúdo do Caderno Estratégico → conteúdo **CENTRALIZADO**, obrigatoriamente por `<div style="text-align:center;">` **dentro** da célula (ver §8.4 — `text-align` na `<td>` é descartado pelo Evernote). Box de Revisão Relâmpago e cards do Deck → **à esquerda**.

**Hierarquia de cabeçalhos**: H1 = os blocos · H2 = tópicos · H3 = subtópicos · H4/negrito = sub-subtópicos. Índice, Caderno Estratégico e Deck espelham a MESMA árvore.

### 1.1 📍 Índice
- Texto solto, lista hierárquica com tópicos E subtópicos (nunca aglutinar).
- É índice **do conteúdo** da nota (os tópicos da matéria), não das estruturas da nota (não listar "Caderno Estratégico", "Deck" etc. como itens).
- 🚨 **Sempre COMPLETO desde a primeira entrega**: em conversões fragmentadas, o índice integral vem já na primeira parte, SEM anotações de progresso ("[a converter]", "✅").

### 1.2 💯 Caderno Estratégico
- Texto solto, denso, claro e autossuficiente; leitura corrida deve bastar para dominar o essencial e ter repertório.
- **Formato: bullet points corridos** (frases completas, com conectivos), sob os H2/H3/H4.
- No topo de cada tópico H2: UM bullet **"Em poucas palavras:"** (sempre com dois-pontos).
  - Um único ponto → conteúdo na própria linha. Mais de um ponto → o rótulo fica sozinho e cada síntese entra como **subtópico recuado**.
  - ⚠️ O rótulo **"Síntese"** (usado até a v7) está extinto: normalizar para "Em poucas palavras:".
- Emojis liberados (§5). **Imagens e diagramas moram aqui** (§6). Tabelas de conteúdo centralizadas.

### 1.3 ⚡ Box de Revisão Relâmpago
O ÚNICO bloco em box (célula única, fundo **amarelo claro**, texto à esquerda). **Um único box por nota** — se a produção gerou boxes parciais por grupo de tópicos, eles são **empilhados numa só célula**, na ordem dos tópicos, separados por `---`, com as Partes renumeradas em sequência contínua. Formato "checklist de discursivas":
- **Partes numeradas espelhando os tópicos** (emoji temático + nome), separadas por `---`.
- Em cada Parte, **2 camadas**: 1º nível = pontos essenciais telegráficos (📐 definição-chave · 🧮 fórmula com leitura · mecanismo/regra central · ➡️ consequências); 2º nível recuado = linhas ✅ atômicas, UMA POR LINHA, "o que precisa aparecer numa resposta completa para pontuar".
- **Última Parte — Integração/Síntese**: cadeia lógica conectando os tópicos + 👆🏻 **"Pulo do Gato"**. Havendo empilhamento de boxes parciais, existe **um único** Pulo do Gato, ao final.
- **Blocos transversais** conforme a NATUREZA da matéria: 🚨 Confusões clássicas e 🧠 Mnemônicos (universais) · 🧮 fórmulas/modelos · 📅 datas-âncora e 📚 autor→tese (matérias históricas) · ⚖️ artigos-âncora (direito) · 🔤 estruturas/conectores (línguas). No empilhamento, os transversais vão **ao final, uma vez só**.

### 1.4 👾 Deck de Flashcards
- Tabelas de 2 colunas (frente | verso), **uma por subtópico (H3)**, precedidas do cabeçalho H3; alinhamento à esquerda.
- 🚨 **NUNCA criar linha de título/cabeçalho na tabela** ("Frente"/"Verso").
- Três velocidades: Box (30s–2min) → Caderno (10–15 min) → Deck (estudo ativo).

## 2. Cabeçalho do card
- Primeira linha da FRENTE, em **código inline**: `[HB › Colônia › Sociedade]` — sigla da matéria (sem número de nota) + trilha espelhando o índice, seguida de **uma linha em branco**.
- 🚨 **Teste de autossuficiência**: lido isolado, fora da nota, o cabeçalho deve permitir identificar matéria e assunto. Trilha genérica demais ("[PI › Panorâmica]") reprova.
- Siglas: HB, HM, PI, ECO, DIR, DIP, PORT, ING, ESP, GEO, HPEB, HECON, HBT, REP, D.CONST, D.ADMIN, D.ECON, RICD, RCCN, SEB.
- 3 níveis é o ideal; mais níveis permitidos. Contador (n) na pergunta quando a resposta for enumerada.

## 3. Tipos de card
| Tipo | Forma |
|---|---|
| Conceito/definição | Pergunta direta → resposta nuclear |
| Enumeração | Pergunta com contador (n) → lista, um item por linha |
| Cronologia | Pergunta → sequência de datas/eventos, um marco por linha |
| Cloze/lacuna | Frase com `______` na frente → gabarito no verso; múltiplas lacunas numeradas, cada uma em linha própria |
| Historiografia/autor | Autor → obra → tese → contestações |
| Discursivo ✍️ | Ver §3.1 |
| Panorâmico (abre tópico) | Fundo de célula **AMARELO**; dá a moldura ("quais são...") |

### 3.1 Card Discursivo ✍️
- **Frente**: "✍️ DISCURSIVA — {comando}". Aspectos enumerados viram **itens de lista**.
- **Verso, ACIMA da divisória — esqueleto decorável em TÓPICOS**: pontos numerados, um por linha, com **subtópicos recuados** desdobrando cada ponto. É a "aula que se vai dar", evocável em 3 minutos.
- **Verso, ABAIXO da divisória — desenvolvimento**: parágrafo corrido, objetivo, modelo de resposta enxuta.
- **Fecho opcional — 🃏 Cartas na manga**: 2–3 itens que elevam a nota (📚 autor-tese · dado forte · 👆🏻 pulo do gato do tema). ⚠️ O rótulo **"🎁 Ganchos de luxo"** (até a v7) está extinto.
- 🚫 Não existe card "esqueleto" avulso (o 🗺️ da v7).

Regras gerais:
- Itens de lista SEMPRE em linhas separadas.
- **Enumerações = listas, nunca "·" inline**.
- Geral-específico: repetir em níveis diferentes só se cada nível perguntar coisa diferente.
- Um fato testável = um card canônico.
- **Redação: privilegiar a melhor formulação existente.**

## 4. Tamanhos (recomendações)
- Frente: ~≤ 20 palavras (fora o cabeçalho). Parte decorável do verso: ~≤ 60 palavras ou ~≤ 7 itens. Abaixo da divisória: livre.

## 5. Semântica visual
**Cores de fundo** (só em células): Box = `#FFF9DB` · card panorâmico = `#FFF2A8` · demais cards = branco.

**Destaques de texto**: **negrito** = ênfase · **highlight `#FFEF9E` com `<b>` interno** = termo-chave · sublinhado = reforço secundário · ~~tachado~~ = afirmação falsa.

**Densidade de negrito**: alvo de **12% a 22%** dos caracteres do corpo. Abaixo disso a triagem visual não funciona; acima, o negrito deixa de destacar.

### 5.1 🎨 Convenção Semântica de Cores de Texto
**Princípio**: cor não é destaque, é METADADO. O negrito diz "isto é importante"; a cor diz "*que tipo* de informação é esta". Todo texto colorido é também negrito.
- **Negrito preto** = ênfase estrutural. NUNCA vira flashcard/ocultação.
- **Negrito colorido** = carga de conteúdo memorizável — o conjunto dos candidatos a cloze.

| Cor | Categoria | O que marca | RGB canônico |
|---|---|---|---|
| 🔴 Vermelho | **Tese/Ruptura** | conclusões, viradas, o "portanto", posição vencedora | `rgb(200, 0, 0)` |
| 🔵 Azul | **Conceito/Instituição** | termos técnicos, órgãos, tratados, modelos | `rgb(0, 60, 200)` |
| 🟢 Verde | **Dado verificável** | datas, números, percentuais, artigos de lei | `rgb(0, 130, 0)` |
| 🟤 Ocre | **Autor/Fonte** | historiografia, doutrina, teses nominadas | `rgb(170, 85, 0)` |
| 🟣 Roxo | **Posição do Brasil** | atuação brasileira em qualquer tema | `rgb(130, 0, 160)` |
| ⚪ Cinza | **Meta (nunca ocultável)** | marcadores, códigos, "ver também" | `rgb(160, 160, 160)` |

**Regras anti-degeneração**: uma cor por trecho · densidade máxima ≈ 1/3 da linha · na dúvida entre vermelho e azul → azul · roxo prevalece · dispositivos de lei em verde, o diploma como instituição em azul.

**Sintaxe canônica**: `<span style="color: rgb(200, 0, 0);"><b>texto</b></span>`

**Emojis funcionais** (significado fixo): 💡 conceito · 📐 definição-chave · 📅 data · 📚 tese/autor · 🔥 cai muito · 🚨 pegadinha · 🧠 mnemônico · ⚠️ exceção/nuance · ⚖️ lei/jurisprudência · 🧮 fórmula · ➡️ consequência · ✅ checklist · 👆🏻 pulo do gato · ✍️ discursiva · 🃏 carta na manga · 🔍 verificar · ⏳ dado perecível · 🧹 pendência para o autor resolver.
- **Regra do ⏳**: marcar toda informação que envelhece (vigências, ocupantes de cargo, composições, rankings, estatísticas), **sempre com data de referência**: `⏳ (set/2026)`. Distinção: 🔍 = "pode estar errado, conferir" (transitório); ⏳ = "está certo, mas expira" (permanente).
- 🚫 **Emojis de bandeira são proibidos** — o Evernote não os renderiza. Usar o nome do país em negrito.
- Emojis dos blocos: 📍 💯 ⚡ 👾 ❓.

## 6. Imagens, diagramas e tabelas de conteúdo
- Imagens e diagramas moram no **Caderno Estratégico**; no card, só quando a imagem É o conteúdo a memorizar.
- **Diagramas próprios (gerados pela IA)**: permitidos e desejáveis. Especificação em §6.1.
- **Imagens de terceiros**: proibidas — substituir por versão própria ou por tabela/estrutura HTML. Nunca manter tabela como imagem. Decorativas: cortar.
- Tabelas de conteúdo: centralizadas, **nunca com exatamente 2 colunas**.

### 6.1 Especificação do diagrama próprio
- **Quando cabe**: só quando o diagrama mostra um **mecanismo, uma sequência ou uma relação** que o texto explica mal — fluxo de processo, linha do tempo com ramificações, arquitetura institucional, comparação de dois ou mais eixos, cadeia causal. **Não cabe** para ilustrar, decorar ou repetir uma lista que já está no texto. Máximo recomendado: **1 a 3 por nota**.
- **Formato de entrega**: **PNG**, largura **1400px**, fundo branco, fonte sans-serif.
- **Fonte versionável obrigatória**: o diagrama é escrito primeiro em **HTML/SVG** e renderizado para PNG. O arquivo-fonte é entregue junto do PNG, para permitir re-renderização quando a folha de estilo mudar, sem refazer o desenho.
- **Paleta**: a mesma de §5.1 — vermelho para a tese/resultado, azul para instituições e conceitos, verde para dados e datas, ocre para autores, roxo para o Brasil. Fundos suaves; texto sempre legível em cinza-escuro ou preto.
- **Legenda**: uma linha abaixo da imagem, em itálico, dizendo o que o diagrama demonstra — não repetindo o título.
- **Colocação**: dentro do H2 a que se refere, depois do bullet "Em poucas palavras:".

## 7. Checagens obrigatórias na conversão
0. **Insumo multi-nota — BLOCÃO ÚNICO**: conteúdo de todas as notas de origem tratado como um único blocão; as fronteiras de saída são as do esqueleto da matéria, não as do arquivo. **Escopo da realocação = o CONJUNTO**: conteúdo que pertence a outra nota do mesmo lote é redistribuição interna, não realocação.
1. **Triagem**: classificar cada card (ok / redundante / textão→discursivo / C-E→nota de questões / cloze) e propor fusões canônicas.
1-bis. **Mineração de mega-cards importados**: dissolver no Caderno Estratégico e minerar cards novos, sinalizados como "🆕 card minerado de {fonte}".
2. **Cards fora de escopo**: listar com destino sugerido — a IA não move.
3. **Matriz de cobertura**: tópico sem card? Card sem ancoragem? Conteúdo ausente?
4. **Checagem factual**: 🔍 + correção para suspeitas de erro; ⏳ + data para dados perecíveis.
5. **Redação e PI**: manter boas redações; reescrever fontes proprietárias; citações literais em bloco.
6. **Fragmentação** e **7. Divisão da nota** quando couber.
8. **Sugestões gerais**: encerrar com "💬 Sugestões da IA".

## 8. 🧷 HTML seguro para Evernote
O Evernote tem **dois analisadores diferentes**: o da colagem (sanitizador de área de transferência, que descarta quase todo CSS) e o da importação de `.enex` (permissivo). **A via canônica é sempre o `.enex`** — colar HTML grande perde fundo de célula, largura e estilo de cabeçalho de card.

1. **Zero blocos `<style>` e zero classes CSS**: toda formatação em `style="..."` inline.
2. **Highlight**: NUNCA `<mark>` → `<span style="background-color:#FFEF9E;"><b>texto</b></span>`.
3. **Cabeçalho do card**: `<code style="font-family:monospace; color:#B3261E; background-color:#F6F1F0;">[SIGLA › ...]</code>` seguido de `<p><br/></p>`.
4. **Tabelas — especificação obrigatória** (validada por importação real; não alterar sem novo teste):
   - Largura **só em pixel**. Porcentagem é descartada e a tabela colapsa.
   - A largura tem de aparecer em **três lugares**: `<colgroup><col style="width:Npx"/>`, no `style` da `<table>` e no `style` de **cada** `<td>`. Sem o `<colgroup>`, o Evernote recalcula tudo pelo conteúdo.
   - `table-layout:fixed` obrigatório. `<tbody>` explícito.
   - **`text-align` na `<td>` é descartado.** Centralizar exige `<div style="text-align:center;">` dentro da célula.
   - Envolver a tabela num `<div>`.
5. **Listas**: `<ul>/<ol>` com `<li>` reais — nunca linhas separadas por `<br>`.
6. **Cabeçalhos**: `<h1>`–`<h4>` nativos.
7. **Negrito/itálico/sublinhado/tachado**: `<b>/<i>/<u>/<s>`.
8. **`&nbsp;` é proibido** (quebra o parser XML na geração do ENEX) — usar `&#160;`.

### 8.9 Larguras canônicas — 1400px em tudo
| Tabela | Largura | Repartição |
|---|---|---|
| Deck de flashcards | 1400px | fixa, **1 : 2,4** → 412 \| 988 |
| Box de Revisão | 1400px | célula única |
| Conteúdo (Caderno) | 1400px | por peso de texto (expoente 0,75, piso 12%) |
| Questões C/E | 1400px | por peso de texto |

**Modelo de tabela do Deck:**
```html
<div>
<table style="border-collapse:collapse; table-layout:fixed; width:1400px;">
<colgroup><col style="width:412px;"/><col style="width:988px;"/></colgroup>
<tbody>
<tr>
<td style="border:1px solid #CCC; padding:8px; vertical-align:top; width:412px;">…</td>
<td style="border:1px solid #CCC; padding:8px; vertical-align:top; width:988px;">…</td>
</tr>
</tbody>
</table>
</div>
```

## 9. Atalhos úteis do Evernote
| Efeito | Como |
|---|---|
| Código inline | \`texto\` |
| Bloco de código | \`\`\` + Enter |
| Cabeçalhos | `#`, `##`, `###` + espaço |
| Divisor | `---` + Enter |
| Tabela n×m | `[][][]` + `x` + nº de linhas |
| Lista | `*` ou `-` + espaço |

## 10. Regras de processo
- Conversão acoplada ao ciclo de revisão; o autor SEMPRE valida.
- A estrutura geral da matéria (ementa, numeração com folgas, tags) precede a conversão em massa.
- Nota muito longa → fragmentar a tarefa.
- **A IA nunca regenera uma nota inteira para corrigir formatação** — emite apenas o trecho substituído (§12).

## 11. 📦 Saída em ENEX
- Formato de entrega: **`.enex`**, um por nota, mais um **consolidado por lote**.
- Várias `<note>` podem conviver num mesmo `<en-export>`.
- Cada nota leva `<title>` no padrão do esqueleto e tags de disciplina.
- Conteúdo em CDATA, com `<!DOCTYPE en-note SYSTEM "http://xml.evernote.com/pub/enml2.dtd">`.
- Auto-fechamento obrigatório em `<br/>`, `<hr/>`, `<img/>`, `<col/>`; `&` solto escapado.
- **Imagens**: `<en-media type="image/png" hash="{md5}"/>` no corpo + bloco `<resource>` com `<data encoding="base64">`. O base64 infla o arquivo em 33% — consolidados por bloco de disciplina, nunca um único arquivo para o acervo inteiro.
- Validar o XML antes de entregar.

## 12. ✅ Contrato de saída testável
Invariantes verificáveis por script. Toda nota entregue deve satisfazer:

**Estrutura**
1. Blocos H1 na ordem: 📍 Índice · 💯 Caderno Estratégico · ⚡ Box de Revisão Relâmpago · 👾 Deck de Flashcards (+ ❓ Questões C/E, se previsto).
2. Exatamente **um** Box de Revisão, com exatamente **um** 👆🏻 Pulo do Gato.
3. O Índice espelha os H2/H3 do Caderno Estratégico.
4. Todo H3 do Deck corresponde a um H3 do Caderno.

**Marcação**
5. Zero `<style>`, zero `class=`, zero `<mark>`, zero `&nbsp;`.
6. Toda tabela tem `<colgroup>`, `table-layout:fixed`, `<tbody>` e largura em px em todas as `<td>`.
7. Nenhuma tabela de conteúdo do Caderno com exatamente 2 colunas.
8. Nenhuma tabela do Deck com linha de cabeçalho.
9. Todo card do Deck começa por `<code …>[SIGLA › …]</code>` seguido de `<p><br/></p>`.

**Conteúdo**
10. Zero ocorrências de: 🐱 · ☝🏻 · "Ganchos de luxo" · "Síntese:" como abridor de H2 · emoji de bandeira · `[IMAGEM` · "caderno-fonte" · "fonte original" · "que você forneceu".
11. Todo ⏳ acompanhado de data de referência entre parênteses.
12. Densidade de negrito no corpo entre 12% e 22%.
13. Pelo menos uma cor semântica por H2 do Caderno Estratégico.
