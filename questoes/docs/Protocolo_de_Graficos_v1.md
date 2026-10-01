# 📈 Protocolo de Gráficos e Figuras — Notas de Questões (-Q) — v1
*Documento técnico e de processo. Diz **como** a IA trata as imagens dos cadernos de questões e **como** produz os próprios gráficos. As regras de **o quê** (onde a figura entra no card, legenda, limites) estão na Folha -Q v3 §10; este protocolo as operacionaliza. Anexar junto da Folha -Q v3, da Especificação v2 e do zip `questoes/` (scripts).*

---

## 0. Princípio
**A IA escreve o conteúdo do gráfico; o script cuida do desenho e confere a economia.**
- A IA nunca escreve código de plotagem nem calcula coordenadas de equilíbrio à mão. Ela escreve uma **spec JSON** curta (curvas, pontos, áreas, rótulos) — o que um professor diria ao desenhar no quadro.
- O `qgraf.py` aplica o estilo único do caderno (paleta da v9, fontes, eixos), **calcula** interseções, projeções e áreas, e **confere**: rótulos sobrepostos, curvas sem rótulo, pontos fora do quadro e as **checagens econômicas** declaradas na spec (ex.: `"E2.y > E1.y"` = o preço subiu).
- A spec é a **fonte versionável** exigida pela v9 §6.1: se a Folha mudar a paleta, re-renderiza-se tudo sem redesenhar nada.

## 1. Fluxo (7 etapas)
| # | Etapa | Quem | Saída |
|---|---|---|---|
| 1 | **Inventário** de todas as imagens do lote | script `inventariar_figuras.py` | `{SIGLA}-Q_figuras_inventario.csv` e `{SIGLA}-Q_imagens_a_reenviar.csv` |
| 2 | **Decisão** por imagem (§2) | IA | coluna `acao` final no mapa de itens |
| 3 | **Spec** de cada figura a desenhar (§4) | IA | `specs/{id}.json` |
| 4 | **Render + lint** até zerar erros | script `qgraf.py` | PNG + relatório de erros |
| 5 | **Revisão visual** (§6) | IA, olhando o PNG | ajustes na spec |
| 6 | **Montagem** no card (Folha -Q v3 §10) | script `montar_nota_q.py` | HTML, ENEX com `<en-media>`, JSONL com `figuras` |
| 7 | **Verificação** do contrato | script `verificar_q.py` | zero violações |

As etapas 4 e 5 são um laço: render → lint → olhar → ajustar → render. A etapa 5 **não é opcional**: o lint pega sobreposição e geometria, mas não pega um `\n` literal, uma área com fresta branca ou uma seta que atravessa um rótulo (casos reais do teste).

## 2. Decisão por imagem
### 2.1 Classificação
Toda imagem do lote recebe **lado** (frente/verso) e **tipo**: `GRÁFICO` · `DIAGRAMA` · `TABELA` · `FÓRMULA` · `TEXTO` · `MAPA` · `DECORATIVA` · `QUESTÃO EM IMAGEM` (frente que é só um print).

### 2.2 Ação
| Lado | Tipo | Ação | Observação |
|---|---|---|---|
| frente | GRÁFICO, DIAGRAMA | **redesenhar** (obrigatório) | sem a figura o item não se julga |
| frente | TABELA | **tabela HTML aninhada** (≥ 3 colunas) | alternativa: tabela PNG (§2.4) |
| frente | TEXTO, FÓRMULA | **transcrever** como texto | fórmula em Unicode/`<sub>`/`<sup>` |
| frente | QUESTÃO EM IMAGEM | **pedir reenvio**; senão reconstruir pelo comentário (§3) | alerta `texto_reconstruido` |
| frente | MAPA | descrever em texto; se indispensável, 🧹 Triagem | mapas não são gerados nesta versão |
| verso | GRÁFICO, DIAGRAMA | **redesenho didático** só se passar no teste do quadro-negro (§2.3) | senão, cortar |
| verso | TABELA, TEXTO | **absorver** no 📖 e cortar | tabela de conteúdo ≥ 3 colunas |
| verso | FÓRMULA | transcrever no 📖 | |
| qualquer | DECORATIVA | **cortar** | |

### 2.3 Teste do quadro-negro (gráfico didático no verso)
Um gráfico novo entra no verso **só se as três respostas forem sim**:
1. Um bom professor **desenharia** isso no quadro para explicar este item?
2. O gabarito depende de um **mecanismo gráfico** — deslocamento de curva, interseção, área (excedente, peso morto, receita), inclinação, distância entre curvas?
3. O gráfico mostra algo que o 📖 **explica mal em palavras**?

**Limites:** no máximo **1 gráfico por verso** (2 só em comparação antes × depois que não caiba em um painel — prefira `paineis`). Itens irmãos (mesmo texto motivador) **compartilham** a figura da frente; o verso de cada um só ganha gráfico próprio se o mecanismo for diferente.

Em ECO, passam tipicamente: oferta e demanda com deslocamentos; excedentes, tributos, tarifas, cotas, tabelamento; elasticidade × gasto; custos e mercado (CMg, CMe, monopólio); IS-LM e IS-LM-BP; OA-DA; Solow; curva de Phillips; FPP e vantagens comparativas; cruz keynesiana; Lorenz. Não passam: definições, classificações, listas de causas, contas de identidade (melhor uma linha de conta no 📖).

### 2.4 Tabelas
- **Frente:** tabela HTML **aninhada** na célula, com ≥ 3 colunas (a regra anti-NeuraCache vale também aqui), largura em px, `<colgroup>` e cabeçalho em `<td><b>` (nunca `<th>`). Fonte em cinza abaixo.
- **Alternativa** (se o teste de importação mostrar que a tabela aninhada quebra no NeuraCache): tabela como **PNG gerado** (`"tipo": "tabela"`), com a mesma legenda. Fica decidido pelo teste (§7).
- Toda tabela transcrita passa pela **checagem de coerência**: identidades contábeis (nominal = primário + juros; BP fecha), somas, sinais. Incoerência da transcrição → corrige-se pela identidade e registra-se `transcricao_incoerente`.

## 3. Imagens que não vieram (caderno exportado sem a pasta de imagens)
1. **Frente**: rode o inventário; ele lista em `{SIGLA}-Q_imagens_a_reenviar.csv` o **nome do arquivo** de cada imagem de frente (ex.: `image (4).png`) e o começo do verso, para você localizar e reenviar só essas — dezenas de arquivos pequenos, não a pasta inteira.
2. **Sem reenvio**:
   - Questão inteira em imagem: reconstrua o enunciado **só** se o comentário o permitir com segurança (o comentário reproduz a assertiva ou a refuta ponto a ponto); pesquise o item em bancos de questões; marque `texto_reconstruido` e escreva na frente, em cinza: *[Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.]* Sem segurança → 🧹 Triagem como irrecuperável.
   - Gráfico da frente: redesenhe pelo que o enunciado e o comentário dizem (rótulos de curvas, áreas, pontos citados) e pela convenção do livro-texto (ex.: áreas A–G do Mankiw na tarifa). Fidelidade `conjectural` + alerta `figura_conjectural` dizendo o que foi deduzido.
3. **Verso**: as imagens do verso nunca se reenviam; aplica-se §2.3.

## 4. A spec
Um objeto JSON por figura, em `specs/{id}.json`. **Id da figura** = `{id do item}-F{n}` (frente) ou `-V{n}` (verso); figura compartilhada por itens irmãos leva o id do primeiro.

### 4.1 Campos gerais
| Campo | Obrigatório | Valor |
|---|---|---|
| `id` | sim | `ECO-R0746-F1` |
| `uso` | sim | `frente` · `verso` |
| `legenda` | sim | Frente: o título/legenda da prova (“Gráfico 1 — …”). Verso: **o que o gráfico demonstra**, em uma ou duas frases — não repete o título |
| `fidelidade` | frente | `fiel` (redesenho com todos os dados da fonte) · `conjectural` (deduzida) — verso é sempre `didatica` |
| `tamanho` | não | `card` (padrão) · `largo` (2 painéis) · `quadrado` · `alto` · `baixo` (tabela) |
| `modelo` + `params` | não | atalho pronto (§4.4) |
| `eixos` | sim | `{"x": "q", "y": "p", "xmax": 10, "ymax": 10, "numeros": false}` — rótulos **curtos** (1–3 caracteres); `numeros: true` só quando os valores importam |
| `curvas`, `pontos`, `areas`, `deslocamentos`, `setas`, `textos` | — | §4.2 |
| `checar` | **sim no verso** | lista de expressões que precisam dar verdadeiro (§4.3) |
| `paineis` | não | lista de specs de painel (antes × depois; movimento × deslocamento) |
| `tipo` | não | `modelo` (padrão) · `dados` (séries reais) · `tabela` · `formula` |

### 4.2 Primitivas
**Curvas** (`id`, `tipo`, `familia`, `rotulo`, opcionais `estado: "inicial"`, `tracejada`, `rotulo_em`, `rotulo_desloc`, `rotulo_xy`):
| `tipo` | Definição |
|---|---|
| `reta` | `p1`, `p2` (pontos; `estender: true` estica até a borda) |
| `funcao` | `expr` em x (`"10 - x/30"`, `"3*x**0.5"`, `"2 + 0.3*maximum(0, x-5)**2"`), `dominio` |
| `pontos` | lista de pontos; `suave: true` passa uma curva suave por eles |
| `horizontal` / `vertical` | `y` (ou `x`) e o intervalo |

**Famílias e cores** (a cor marca a família; a mesma paleta da v9):
| `familia` | Cor | Uso |
|---|---|---|
| `demanda` | 🔵 azul | D, IS, DA, RMe, f(k), FPP, isoquanta |
| `oferta` | 🟤 ocre | O/S, LM, OA, CMg, s·f(k) |
| `terceira` | 🟣 roxo | BP, CMe, restrição orçamentária, (n+δ)k |
| `quarta` | 🟢 verde | RMg, CVMe, isocusto |
| `destaque` | 🔴 vermelho | a curva que muda o resultado (teto, nova curva crítica) |
| `referencia` | ⚪ cinza tracejado | preço mundial, 45°, linhas-guia |

`estado: "inicial"` desenha a curva antes do choque em tom esmaecido; a curva final vem cheia. **Setas de deslocamento são sempre vermelhas.**

**Pontos** — `xy` (fixo), `intersecao: ["D1", "S1"]` (o script calcula; `indice` escolhe a 2ª interseção) ou `sobre: "D", "x": 3`. Opções: `rotulo`, `projetar` (`true` · `"x"` · `"y"`), `rotulo_x`/`rotulo_y` (marcas nos eixos: `q₁`, `p*`), `marcar`.

**Áreas** — `poligono` com `vertices` (ids de pontos ou `[x, y]`) ou `entre` (`sup`, `inf`, `x`). `papel` define a cor: `excedente_consumidor` · `excedente_produtor` · `receita_tributaria` · `peso_morto` · `gasto` · `ganho` · `perda` · `neutro` · `roxo`.

**Deslocamentos** — `{"de": "D1", "para": "D2", "sentido": "direita", "em_y": 5}` (ou `em_x`, ou `posicao` 0–1 ao longo da curva de origem). O `sentido` é **conferido**.

**Setas** e **textos** — `de`/`para`, `rotulo`, `estilo` (`"-|>"`, `"<|-|>"`), `cor`; textos com `xy`, `cor`, `negrito`, `tamanho`.

**Expressões** — onde cabe número, cabe expressão: `"E1.y"`, `"(E1.x+E2.x)/2"`, `"D(3)"` (y da curva D em x = 3), `"D.inv(5)"` (x da curva D em y = 5).

### 4.3 Checagens (`checar`)
Cada gráfico de verso declara o que precisa ser verdade para ele ensinar o que o comentário diz:
- direção: `"E2.y > E1.y"`, `"E2.x < E1.x"`;
- números do comentário: `"abs(E.x - 90) < 0.01"`, `"abs((10 - E.y) * E.x / 2 - 135) < 0.01"`;
- relações: `"E2.x*E2.y > E1.x*E1.y"` (o gasto aumentou).
Se a checagem falha, ou o desenho está errado ou **o comentário está errado** — investigar antes de mexer na spec. É a ponte entre o gráfico e o gabarito.

### 4.4 Modelos prontos (`modelos.py`)
| `modelo` | `params` principais | Gera |
|---|---|---|
| `oferta_demanda` | `deslocar: {"D": "direita", "S": "esquerda"}`, `passo`, `excedentes`, `nome_oferta` | D, O, equilíbrios E₁/E₂ projetados, setas, checagens de direção |
| `tributo` | `t`, `D`, `S` | O + t, pc, pv, receita, peso morto, checagem da cunha |
| `tarifa` | `pw`, `t` | preço mundial, preço com tarifa, Qˢ/Qᴰ antes e depois, receita, peso morto |
| `is_lm` | `deslocar: {"IS": …, "LM": …}`, `passo` | IS, LM, E₁/E₂, Y e i nos eixos |
| `solow` | `A`, `alfa`, `s`, `n_delta`, `ouro` | f(k), s·f(k), (n+δ)k, k*, k ouro e seta do c* máximo |
| `fpp` | `expandir` | FPP côncava, expansão |
| `monopolio` | `a`, `b`, `c` | D = RMe, RMg, CMg = CMe, ponto de monopólio, peso morto |

Ajustes finos sem reescrever o modelo: `"substituir": {"E1": {"rotulo_x": "Y*"}}` e `"remover": ["E2"]`. Tudo o que a spec trouxer em `curvas`, `pontos`, `areas`, `setas`, `textos`, `checar` é **somado** ao modelo. Modelo novo entra em `modelos.py` quando o mesmo desenho aparecer em **3 ou mais** itens do lote.

### 4.5 Dados reais (`"tipo": "dados"`)
Barras ou linhas com `categorias`, `series` (`nome`, `valores`), `unidade`, `fonte` (**obrigatória**), `casas`, `sufixo`. Números **só** da fonte do item ou de fonte oficial citada; nunca estimados. Dado perecível → ⏳ no 📖.

### 4.6 Exemplo completo
```json
{"id": "ECO-R1037-V1", "uso": "verso",
 "legenda": "Com o preço tabelado em 6 (abaixo do equilíbrio de 7), demanda-se 120 e oferta-se 80: excesso de DEMANDA de 40.",
 "eixos": {"x": "Q", "y": "p", "xmax": 150, "ymax": 11, "numeros": true},
 "curvas": [
   {"id": "D", "tipo": "funcao", "expr": "10 - x/30", "familia": "demanda", "rotulo": "D"},
   {"id": "S", "tipo": "funcao", "expr": "(x - 20)/10", "dominio": [20, 125], "familia": "oferta", "rotulo": "O"},
   {"id": "Pmax", "tipo": "horizontal", "y": 6, "x": [0, 135], "familia": "destaque", "rotulo": "preço tabelado = 6"}],
 "pontos": [
   {"id": "Qs", "intersecao": ["S", "Pmax"], "projetar": "x"},
   {"id": "Qd", "intersecao": ["D", "Pmax"], "projetar": "x"}],
 "setas": [{"de": ["Qs.x", 4.6], "para": ["Qd.x", 4.6], "estilo": "<|-|>", "rotulo": "falta 40"}],
 "checar": ["abs(Qs.x - 80) < 0.01", "abs(Qd.x - 120) < 0.01"]}
```

## 5. Estilo (fixado pelo script — a IA não mexe)
- PNG de 1120 × 700 px (card), 1400 × 728 (largo), fundo branco, fonte DejaVu Sans, 96 cores, ~7–20 KB por figura.
- Eixos só à esquerda e embaixo, com seta; sem números salvo `numeros: true`; rótulo do eixo y no topo, do x na ponta.
- Exibição no card: **540 px** na frente e **660 px** no verso; colunas mínimas de 600 px (frente com figura ou tabela) e 720 px (verso com figura).
- Rótulos com subíndice Unicode (D₁, q₂, E*) nas figuras de verso; nas de frente, os rótulos **da prova** (“D1”, “Gráfico 1”).

## 6. Revisão visual (etapa 5)
A IA **abre cada PNG** e confere:
1. O gráfico mostra exatamente o mecanismo do 📖 e a **legenda** descreve o que se vê?
2. Toda curva, ponto e área citados no comentário ou na assertiva **aparecem com o mesmo nome**?
3. Nenhum rótulo cortado, sobreposto, atravessado por curva ou colado na borda; nenhum `\n` literal.
4. Áreas sem frestas; setas não atravessam rótulos; a seta de deslocamento aponta para a curva certa.
5. Na frente: o desenho não **entrega o gabarito** além do que a figura original mostrava (nada de equilíbrio novo, seta de resposta ou área destacada que a prova não tinha).
Cobertura: **100%** das figuras de frente; **100%** das de verso nas duas primeiras passadas de cada matéria, depois amostra de 30%.

## 7. Teste de importação (Fase 0.5-G — uma vez por caderno, antes da 1ª passada)
Importar `00-TESTE-GRAF-1 - Obj.enex` e conferir no Evernote **e** no NeuraCache:
- [ ] as imagens aparecem na frente e no verso, na largura definida (540/660 px), sem estourar a coluna;
- [ ] a legenda cinza fica logo abaixo da imagem;
- [ ] a `<hr/>` dentro da célula sobrevive;
- [ ] **tabela HTML aninhada** (card de NFSP) × **tabela PNG** (card de vantagem comparativa): qual sobrevive no NeuraCache sem virar cards extras? A que sobreviver vira a regra (§2.4);
- [ ] no celular, a imagem é legível ou permite zoom;
- [ ] tamanho do ENEX aceitável para importação.
Resultado registrado numa linha no plano do lote (`{SIGLA}-Q_plano.json`, campo `teste_importacao`).

## 8. Fora do escopo desta versão (registrar como alerta quando aparecer)
- Mapas (GEO): descrição em texto; geração de mapa fica para uma v2 do protocolo.
- Linhas do tempo e esquemas institucionais (HB, HM, PI, DIP): o `qgraf` não os gera ainda; quando forem pedidos, entram como `tipo: "diagrama"` numa próxima versão, com a mesma lógica de spec + lint.
- Gráficos 3D, superfícies, diagramas de caixa de Edgeworth (fazer como primitivas, se aparecerem em 3+ itens).

## 9. Comandos
```bash
pip install matplotlib numpy pillow beautifulsoup4 lxml
# 1. inventário
python3 questoes/inventario/inventariar_figuras.py --html "eco 1.html" --md eco2.md eco3.md -o saida/
# 4. render + lint (+ galeria para a revisão visual)
python3 questoes/graficos/qgraf.py specs/ -o saida/figuras --galeria
# 6. montagem
python3 questoes/montar_nota_q.py cards.py --titulo "07-A-1 - Obj." --sigla ECO --passada 1 --specs specs/ -o saida/
# 7. verificação
python3 questoes/verificar_q.py saida/*.enex --jsonl saida/ECO-Q_passada01.jsonl
```
