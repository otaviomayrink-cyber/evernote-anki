# Instruções — classificação da Fase 0 (ECO)

Você classifica linhas brutas de cadernos de questões objetivas de Economia (CACD/TPS, concursos). Cada linha do
arquivo de entrada é um card antigo: `frente` (questão; às vezes vários itens numerados), `verso` (gabarito +
comentário; truncado em 450 caracteres), `imgs` (imagens: lado, referência, tipo), `origem` (nota/seção antiga —
NÃO indica o tema; o caderno E1 tem notas numeradas que costumam bater com o índice, mas confira pelo conteúdo),
`dup` (outras linhas com texto muito parecido, com similaridade).

## O que produzir
Um arquivo JSONL com **exatamente uma linha por `rid` da entrada, na mesma ordem**, neste formato:

```json
{"rid": "E2-L00151", "nao_questao": false, "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026,
 "cacd": false, "errei": true,
 "itens": [{"k": 1, "tipo": "C/E", "gabarito": "ERRADO", "destino": "56", "h2": "🥇 Regra de ouro",
            "resumo": "regra de ouro ≠ investimento = depreciação", "dup_de": null}],
 "figura_frente": "nenhuma", "triagem": null, "obs": ""}
```

Campos:
- `nao_questao`: true se a linha não é questão julgável (dúvida pessoal, anotação, linha de título, comentário solto,
  "Indique graficamente…" NÃO conta como não-questão: é `EXERC`). Linha não-questão → `itens: []` e `obs` com o motivo.
- `banca`: normalizada. Provas: `CEBRASPE` (CESPE/Cebraspe/UnB), `FGV`, `FCC`, `ESAF`, `CESGRANRIO`, `VUNESP`… Cursos e
  professores pelo nome: `IDEG – Prof. Bozan`, `Armstrong`, `Nabuco`, `Intensivo MM`, `Prof. Rodrigo Teixeira`,
  `Nidi/Jacqueline Bueno`, `Simulado Sapientia`, etc. Sem identificação: `Banca não identificada`.
  Não invente: só preencha banca de prova se o texto disser (ex.: "CESPE 2015", "TJ/PA 25 CEBRASPE", "CACD 2012").
  Questões do CACD/IRBr (TPS) com ano → banca `CEBRASPE`, `cacd: true`, `prova: "IRBr/CACD/AAAA"`.
  Na seção "TJ/PA - CEBRASPE 2025": banca `CEBRASPE`, prova `TJ/PA/2025`.
- `prova`: Órgão/Cargo/Ano só com o que a fonte informa ("Pré-TPS/2026", "Intensivo Pré-TPS/2023"); senão "".
- `ano`: inteiro ou null.
- `errei`: true se a frente começa com ❌ (pode vir depois de `==` ou `**`).
- `itens`: um por item julgável. Questão com itens numerados (1., 2., I, II…) e gabarito por item → vários itens.
  Múltipla escolha (A–E) = **um** item `ME` com gabarito na letra. `tipo`: `C/E` · `ME` · `EXERC` · `DISC`.
  `gabarito`: `CERTO` · `ERRADO` · `ANULADO` · `A`–`E` · `RESPOSTA` · `?` (não dá para saber pelo verso truncado:
  tudo bem, quem redigir o card resolve).
- `destino`: o id da nota do índice abaixo cujo **conteúdo** o item testa (não a origem); se não couber em nenhuma
  nota, `TRIAGEM`. `h2`: um dos H2 da nota, **copiado exatamente** (com emoji); na TRIAGEM, `h2` = nota sugerida ou "".
- `resumo`: 4–12 palavras do que o item testa (para o mapa e para achar duplicatas).
- `dup_de`: se o item é a mesma assertiva de outra linha (veja `dup`, similaridade ≥ 0,85 e mesmo texto da
  assertiva), o `rid` (e `#k`, se aplicável) da **primeira** ocorrência, ex.: `"E1-0012#1"`; senão null.
  Itens quase iguais de provas diferentes NÃO são duplicata.
- `figura_frente`: `nenhuma` · `transcrita_ok` (a transcrição permite julgar) · `transcrita_insuficiente` ·
  `ausente_deduzivel` (imagem não veio, mas comando/verso permitem reconstruir) · `ausente_irrecuperavel`.
  Caderno E1: imagens `[[IMG: …]]` não vieram — se a frente é SÓ a imagem, decida entre `ausente_deduzivel`
  (o verso deixa claro o que se pedia: dá para reconstruir a assertiva) e `ausente_irrecuperavel`.
- `triagem`: null, ou motivo curto quando o item vai para TRIAGEM ou é irrecuperável.
- `obs`: curto; vazio se nada a dizer.

## Índice de ECO (destinos e H2 permitidos)

### I. MICROECONOMIA
- **01** — 🦋 Microeconomia: fundamentos, CPP, demanda e oferta, bens, equilíbrio
    - H2: `🧭 Fundamentos e escassez`
    - H2: `📐 Curva de possibilidades de produção`
    - H2: `📈 Demanda: determinantes e deslocamentos`
    - H2: `🏭 Oferta: determinantes e deslocamentos`
    - H2: `🏷️ Classificação dos bens`
    - H2: `⚖️ Equilíbrio e estática comparativa`
- **02** — 🍰 Elasticidades
    - H2: `📐 Elasticidade-preço da demanda`
    - H2: `💰 Elasticidade, receita e gasto`
    - H2: `🔗 Elasticidade-renda e cruzada`
    - H2: `🏭 Elasticidade da oferta`
    - H2: `⏳ Determinantes e prazos`
- **03** — 🍫 Intervenções do Estado na economia e economia do bem-estar
    - H2: `😊 Excedentes e eficiência`
    - H2: `💸 Tributos: incidência e peso morto`
    - H2: `🧾 Subsídios`
    - H2: `🚧 Preços máximos e mínimos`
    - H2: `🧮 Cotas e outras intervenções`
- **04** — 🍇 Teoria do consumidor, curvas preço-consumo e Engel, efeitos renda e substituição
    - H2: `🧠 Preferências e axiomas`
    - H2: `🎯 Utilidade e curvas de indiferença`
    - H2: `💵 Restrição orçamentária`
    - H2: `⚖️ Escolha ótima do consumidor`
    - H2: `📊 Demanda individual e de mercado`
- **04-A** — 🤑 Preço-consumo, Engel e efeitos renda/substituição
    - H2: `📈 Curva preço-consumo`
    - H2: `📉 Curva renda-consumo e Engel`
    - H2: `🔀 Efeitos renda e substituição`
    - H2: `🥔 Bens inferiores e de Giffen`
    - H2: `🧮 Slutsky e Hicks`
- **05** — ☂️ Teoria da firma I (produção — isoquanta)
    - H2: `🏭 Função de produção e curto prazo`
    - H2: `📉 Produto marginal e rendimentos`
    - H2: `🗺️ Isoquantas e TMST`
    - H2: `📏 Rendimentos de escala`
- **06** — 💧 Teoria da firma II (custos — isocusto)
    - H2: `💰 Custos de curto prazo`
    - H2: `📈 Custos de longo prazo e escala`
    - H2: `⚖️ Isocusto e combinação ótima`
    - H2: `🧾 Custo econômico × contábil`
- **07** — 🌈 Estruturas de mercado (panorama)
    - H2: `🗺️ Comparação entre estruturas`
- **07-A** — 🌈 Concorrência perfeita
    - H2: `📐 Hipóteses e maximização de lucro`
    - H2: `⏱️ Curto prazo: oferta da firma`
    - H2: `⏳ Longo prazo e entrada/saída`
- **08** — 🍒 Monopólio e monopsônio
    - H2: `👑 Equilíbrio do monopólio`
    - H2: `📊 Markup, elasticidade e poder de mercado`
    - H2: `🎟️ Discriminação de preços`
    - H2: `🏛️ Monopólio natural e regulação`
    - H2: `🛒 Monopsônio`
- **09** — ⚔️ Concorrência monopolística
    - H2: `🧩 Modelo de Chamberlin`
- **10** — 🦑 Oligopólios
    - H2: `🧮 Cournot e Bertrand`
    - H2: `🥇 Stackelberg e liderança`
    - H2: `🤝 Cartel e conluio`
    - H2: `📏 Concentração e outras teorias`
- **11** — 🎲 Teoria dos jogos
    - H2: `♟️ Equilíbrio de Nash e dominância`
    - H2: `🔁 Jogos sequenciais e repetidos`
- **12** — ⚖️ Falhas de mercado, externalidades, tipos de bens e informações assimétricas
    - H2: `🌫️ Externalidades e Coase`
    - H2: `🏞️ Bens públicos e comuns`
    - H2: `🕵️ Informação assimétrica`
    - H2: `🏛️ Falhas de governo e regulação`

### II. MACROECONOMIA E CONTAS NACIONAIS
- **15** — ⚡ Macroeconomia: panorama histórico (genealogia das ideias)
    - H2: `📜 Escolas do pensamento macroeconômico`
- **16** — 🌅 Conceitos básicos da teoria macroeconômica
    - H2: `🧭 Agregados e conceitos básicos`
- **17** — 🏺 Contas Nacionais
    - H2: `🔄 Identidades e óticas do produto`
    - H2: `📏 PIB, PNB, RNB e conceitos derivados`
    - H2: `💲 Preços de mercado × custo de fatores`
    - H2: `📊 Nominal × real e deflator`
    - H2: `🧾 SCN e tabelas`
- **18** — 🌊 Balanço de Pagamentos: estrutura e lançamentos
    - H2: `🏗️ Estrutura do BP (BPM6)`
    - H2: `✍️ Lançamentos`
    - H2: `🔗 BP e contas nacionais`
- **19** — 📿 Indicadores fiscais e de liquidez/solvência externa
    - H2: `💰 Resultados fiscais (NFSP)`
    - H2: `🌐 Indicadores externos`

### III. MODELOS MACROECONÔMICOS E FLUTUAÇÕES
- **25** — ❄️ Modelo clássico de determinação da renda + TQM clássica (moeda e preços no longo prazo)
    - H2: `⚙️ Modelo clássico`
    - H2: `💵 Teoria quantitativa da moeda`
- **26** — 🏔️ Modelo keynesiano simples: demanda efetiva, multiplicador
    - H2: `📈 Demanda efetiva e cruz keynesiana`
    - H2: `✖️ Multiplicadores`
- **27** — 🎭 Modelo IS-LM (keynesiano generalizado / Hicks-Hansen)
    - H2: `📉 Curva IS`
    - H2: `📈 Curva LM`
    - H2: `🏦 Política fiscal e monetária`
    - H2: `🕳️ Casos extremos`
- **28** — 🌍 Modelo OA-DA
    - H2: `📈 Demanda agregada`
    - H2: `🏭 Oferta agregada e choques`
- **29** — 🐦 Curva de Phillips: inflação × desemprego, expectativas (adaptativas × racionais)
    - H2: `📉 Phillips original e aceleracionista`
    - H2: `🔮 Expectativas e NAIRU`
- **30** — 🧵 Síntese neoclássica e o debate macroeconômico contemporâneo
    - H2: `🗣️ Debate contemporâneo`

### IV. ECONOMIA MONETÁRIA E SISTEMA FINANCEIRO
- **35** — 🎵 Economia monetária: moeda, criação, multiplicador, demanda por moeda
    - H2: `🪙 Funções e agregados monetários`
    - H2: `🏦 Criação de moeda e multiplicador`
    - H2: `📊 Demanda por moeda`
- **36** — 🌀 Banco Central e política monetária: funções, instrumentos, TQM operacional, senhoriagem e imposto inflacionário
    - H2: `🏛️ Funções do Banco Central`
    - H2: `🛠️ Instrumentos de política monetária`
    - H2: `💸 Senhoriagem e imposto inflacionário`
- **37** — 💥 Inflação: conceitos e correntes
    - H2: `🔥 Tipos e teorias da inflação`
- **38** — 🎯 Sistema de metas, ancoragem, forward guidance, regra de Taylor
    - H2: `🎯 Metas de inflação e regras`
- **39** — 🐉 Dominância fiscal, TFNP, coordenação fiscal-monetária
    - H2: `🐉 Dominância fiscal`
- **40** — 🚀 Políticas monetárias não convencionais: QE, tapering, QT, crises de 2008 e 2023
    - H2: `🖨️ QE, tapering e QT`
    - H2: `💥 Crises financeiras`
- **41** — 🏛️ Regulação do sistema bancário, financeiro e mercado de capitais, Basileia
    - H2: `🏛️ Regulação e Basileia`
- **42** — 💳 Bancos digitais, meios de pagamento, economia digital
    - H2: `💳 Pagamentos e economia digital`

### V. SETOR PÚBLICO E POLÍTICA FISCAL
- **47** — 🌱 Setor público e funções do Estado, política fiscal, equivalência ricardiana
    - H2: `🏛️ Funções do Estado`
    - H2: `💸 Tributação: princípios e incidência`
    - H2: `📊 Política fiscal e multiplicadores`
    - H2: `🔮 Equivalência ricardiana`
- **48** — 🐘 Déficit e dívida públicos: financiamento, Wagner, Laffer, sustentabilidade, dívida/PIB
    - H2: `📏 Conceitos de déficit e dívida`
    - H2: `🧮 Financiamento e sustentabilidade`
    - H2: `📈 Wagner e Laffer`
- **49** — 🌕 Orçamento público: PPA/LDO/LOA, responsabilidade fiscal
    - H2: `📒 Ciclo orçamentário`
    - H2: `⚖️ Responsabilidade fiscal`
- **50** — 🌶️ Trajetória da dívida pública, teto de gastos, novo arcabouço fiscal
    - H2: `📈 Trajetória da dívida`
    - H2: `🧱 Regras fiscais: teto e arcabouço`

### VI. CRESCIMENTO, DESENVOLVIMENTO E MERCADO DE TRABALHO
- **55** — ⭐ Teorias do consumo e investimento
    - H2: `🛒 Teorias do consumo`
    - H2: `🏗️ Teorias do investimento`
- **56** — 📈 Modelo de Solow: estado estacionário, regra de ouro, população e tecnologia
    - H2: `⚙️ Estado estacionário`
    - H2: `🥇 Regra de ouro`
    - H2: `👥 População, tecnologia e convergência`
- **57** — 💡 Crescimento endógeno (Romer, Lucas, Arrow), Schumpeter, Harrod-Domar
    - H2: `💡 Teorias do crescimento`
- **58** — 🌾 Desenvolvimento econômico
    - H2: `🌾 Teorias do desenvolvimento`
- **59** — 🐎 Mercado de trabalho, Lei de Okun
    - H2: `👷 Desemprego e mercado de trabalho`
    - H2: `📏 Lei de Okun`
- **60** — 🏭 Precarização, reforma trabalhista de 2017, conjuntura do trabalho
    - H2: `🏭 Conjuntura do trabalho`

### VII. MACROECONOMIA ABERTA E FINANÇAS INTERNACIONAIS
- **65** — 🕰️ Sistema Financeiro Internacional: padrão-ouro, Bretton Woods, crises
    - H2: `🥇 Padrão-ouro`
    - H2: `🏦 Bretton Woods`
    - H2: `💥 Crises e pós-Bretton Woods`
- **66** — 💱 Câmbio e política cambial: regimes, nominal × real, PPC
    - H2: `💱 Regimes cambiais`
    - H2: `📏 Câmbio nominal × real e PPC`
    - H2: `📈 Determinantes do câmbio`
- **67** — 📘 Reservas internacionais e política cambial ativa
    - H2: `📘 Reservas e intervenção`
- **68** — 🧂 Poupança externa e crescimento econômico
    - H2: `🧂 Poupança externa`
    - H2: `🔗 Hiatos e restrição externa`
- **69** — 🔗 Relação câmbio-juros-inflação
    - H2: `🔗 Paridades e repasse cambial`
- **70** — 📍 Modelo IS-LM-BP (Mundell-Fleming)
    - H2: `📍 Curva BP e mobilidade de capital`
    - H2: `🔒 Câmbio fixo`
    - H2: `🌊 Câmbio flutuante`

### VIII. COMÉRCIO E ECONOMIA INTERNACIONAL
- **73** — ⛵ Teorias clássicas e neoclássicas do comércio: Smith, Ricardo, Heckscher-Ohlin (H-O), teoremas, Leontief
    - H2: `⛵ Vantagens absolutas e comparativas`
    - H2: `🧪 Heckscher-Ohlin e teoremas`
    - H2: `❓ Paradoxo de Leontief e termos de troca`
- **74** — 🌎 Crítica da CEPAL: Prebisch, deterioração dos termos de troca
    - H2: `🌎 CEPAL e termos de troca`
- **75** — 🔬 Novas teorias do comércio: escala, concorrência imperfeita, comércio intraindustrial, intrafirma
    - H2: `🔬 Novas teorias do comércio`
- **76** — ⭐ Cadeias globais de valor: fluxos internacionais de bens e serviços
    - H2: `⭐ Cadeias globais de valor`
- **77** — 💼 Investimento internacional: portfólio × IED, internacionalização da produção
    - H2: `💼 IED e portfólio`
- **78** — 🌐 Globalização financeira e produtiva: volatilidade, riscos e vulnerabilidade externa
    - H2: `🌐 Globalização e vulnerabilidade`
- **79** — 🎪 Políticas comerciais e de comércio exterior: tarifas, cotas, subsídios
    - H2: `🧾 Tarifas`
    - H2: `🚫 Cotas e barreiras não tarifárias`
    - H2: `💰 Subsídios e defesa comercial`
    - H2: `🏛️ Política comercial e OMC`

### IX. CONJUNTURA E ECONOMIA BRASILEIRA CONTEMPORÂNEA
- **83** — 🌋 Conjuntura econômica do Brasil
    - H2: `🌋 Conjuntura brasileira`
- **84** — 🌐 Conjuntura econômica internacional
    - H2: `🌐 Conjuntura internacional`
- **85** — 🧭 Raio-X e diagnósticos da economia brasileira: perspectivas em disputa
    - H2: `🧭 Diagnósticos em disputa`

- `TRIAGEM` — itens fora de Economia (ex.: História econômica pura, Direito) ou ilegíveis.

## Regras
- Classifique pelo conteúdo testado. Ex.: elasticidade e gasto → 02; tributo e peso morto → 03; IS-LM-BP → 70;
  tarifa → 79; vantagem comparativa → 73; NFSP → 19 (indicador) ou 48 (conceito de déficit/dívida);
  BP lançamentos → 18; contas nacionais → 17; Solow → 56; Phillips → 29.
- História econômica do Brasil (PAEG, Plano Real como história, Sumoc 113) é de outra matéria → TRIAGEM com
  `h2: "HECON"` salvo se o item testar teoria econômica do índice ou conjuntura (83/85).
- Não escreva nada além do arquivo JSONL. Valide com:
  `python3 validar_classif.py classif/lote_XX.jsonl classif/saida_XX.jsonl` até sair "OK".
