# 🎓 Lições do lote — ECO-Q (Economia)

*O que se aprende com os 2.213 cards de `ECO-Q_mestre.jsonl`, organizado para estudo. Números calculados sobre o mestre; todo exemplo é um id real do lote. Itens CACD (71) e CEBRASPE de outros concursos (99) vêm primeiro sempre que existem.*

**Base em uma linha:** 2.213 cards · 2.194 C/E · CERTO 1.098 × ERRADO 1.085 · 71 do CACD (34 CERTO, 33 ERRADO, 3 anulados, 1 ME) · **331 ❌ seus (15%)**. Desses 331, **144 eram itens CERTOS** que você julgou falsos e **181 eram ERRADOS** que você aceitou. Ou seja: quase metade das suas perdas vem de desconfiar demais, não só de ser enganado.

> 🔑 **Achado estrutural do lote:** cada código da taxonomia corresponde, na prática, a um único gabarito. LITERAL (568), PARAFRASE_FIEL (275), MODULADOR_RELATIVO (89), DETALHE (81), CONTRAINTUITIVO (76) e EXCECAO (3) são **100% CERTO**. INVERSAO (290), GENERALIZACAO (79), NEXO_INDEVIDO (65), TROCA_ATOR (38), CONTRADICAO (35), RESTRICAO (29), EXTRAPOLACAO (13), ANACRONISMO (12) e JUIZO_INDEVIDO (7) são **100% ERRADO**. TROCA_CONCEITO dá ERRADO em 373 de 374 casos e MEIA_VERDADE em 106 de 108. Na prática, julgar o item é descobrir **qual operação a banca fez sobre o enunciado de manual**.

---

## 1. Como a banca pensa nesta matéria

São 12 padrões, em ordem aproximada de frequência e de dano para você.

### P1 — Troca de conceito vizinho (17% dos itens · ERRADO)
**Padrão:** a frase descreve corretamente o conceito A, mas dá a ele o nome do conceito B, que fica ao lado no manual: balança comercial × transações correntes, Stolper-Samuelson × Heckscher-Ohlin, isoquanta × isocusto.
**Item real:** `ECO-E1-0782-1` (CACD 2024): “Quando as importações de um país superam suas exportações, diz-se que o país tem déficit em conta-corrente; portanto […] precisará financiar a diferença por meio da aquisição de empréstimos externos.” → **ERRADO** (status: alterado). M > X é déficit **comercial**, e o financiamento pode vir também de IED ou de reservas.
**Como reconhecer:** sublinhe o rótulo técnico e pergunte se a definição pertence a ele ou ao vizinho.
**Gabarito típico:** ERRADO (373 de 374). Taxa de ❌: 15% (55 itens).

### P2 — Inversão de sinal ou direção (13% · ERRADO)
**Padrão:** troca de sentido em um elo da cadeia causal: aprecia ↔ deprecia, sobe ↔ desce, maior ↔ menor, compra ↔ vende divisas.
**Item real:** `ECO-E1-0819-1` (CACD 2026): “Um aumento persistente do diferencial de juros tende a **desvalorizar** o câmbio e, por essa via, elevar a inflação doméstica […]” → **ERRADO**: o diferencial atrai capital e **aprecia** o câmbio, o que desinfla. Também `ECO-E1-0677-1` (CACD 2025): na banda, perto do limite de desvalorização o BC **vende** divisas, e não compra → ERRADO.
**Como reconhecer:** refaça a cadeia com setas (i↑ → entrada de K → E↓ → importados mais baratos → π↓) e compare seta por seta.
**Gabarito típico:** ERRADO (290 de 290). É o código em que você mais erra em volume: **56 ❌ (19%)**.

### P3 — Deslocamento da curva × movimento ao longo dela
**Padrão:** a banca troca “desloca a curva” por “movimento ao longo” (e vice-versa), ou aplica o deslocamento à curva errada (CPP, oferta, demanda, LM).
**Item real:** `ECO-E1-0015-1` (CACD 2003): a retomada dos EUA reduziu o desemprego; “como consequência, a curva de possibilidades de produção […] foi deslocada para cima e para a direita.” → **ERRADO** (❌ seu). Reduzir desemprego leva a economia de dentro **até** a CPP, sem deslocá-la. Em contraste, `ECO-E1-0029-1` (CACD 2004): menos IOF → mais poupança → mais capital → CPP se desloca → **CERTO** (❌ seu). E `ECO-E1-0205-1`: alta do preço de insumo **desloca** a oferta, e não gera “movimento ao longo” dela → ERRADO.
**Como reconhecer:** mudou o preço do próprio bem → movimento ao longo. Mudou qualquer outro determinante (insumo, renda, tecnologia, dotação de fatores) → deslocamento. CPP só se desloca com mais recursos ou com tecnologia.
**Gabarito típico:** os 67 itens com “desloca” dão 55% ERRADO, e você errou 16 deles.

### P4 — Absolutização (GENERALIZACAO · ERRADO)
**Padrão:** um resultado que vale sob hipóteses vira regra universal com “necessariamente”, “sempre”, “exclusivamente”, “independentemente”, “automaticamente”.
**Item real:** `ECO-E1-0817-1` (CACD 2026): “Se um país apresenta déficit em transações correntes, isso implica **necessariamente** que sua balança comercial também está em déficit.” → **ERRADO**: pode haver superávit comercial e déficit de renda primária maior. Também `ECO-E1-0813-1` (CACD 2026): a moeda seria “**necessariamente** neutra” com salário nominal dado → ERRADO.
**Como reconhecer:** procure o contraexemplo de uma linha. Se ele existir, o item cai.
**Gabarito típico (relatório):** “portanto” 93% ERRADO · “exclusivamente” 78% · “independentemente” 76% · “sempre” 73% · “necessariamente” 70%.

### P5 — Modulador relativo salva o item (MODULADOR_RELATIVO · CERTO)
**Padrão:** “pode”, “tende a”, “é possível” tornam verdadeira uma afirmação que, dita em termos absolutos, seria discutível.
**Item real:** `ECO-E1-0828-1` (CACD 2026): “A eventual introdução de uma CBDC **pode** alterar a estrutura de captação das instituições financeiras […]” → **CERTO**. Também `ECO-E3-L00031-1` (TJ/PA 2025, ❌ seu): gasto público com juro nominal constante “**pode** provocar aumento da atividade, pressão sobre preços e apreciação real” → CERTO.
**Como reconhecer:** com modulador fraco, o item só cai se for **impossível**, e não apenas incomum.
**Gabarito típico:** “podem” 10% ERRADO · “poderá” 20% · “pode” 28% · “é possível” 31%. Atenção: “tende a” fica perto do meio (47% ERRADO), então decida pelo mérito.

### P6 — Nexo causal indevido (NEXO_INDEVIDO · ERRADO)
**Padrão:** duas orações verdadeiras, ou uma verdadeira e uma plausível, ligadas por “pois”, “uma vez que”, “visto que” ou “portanto”, quando a causa apontada não é a verdadeira.
**Item real:** `ECO-E1-0783-1` (CACD 2024, ❌ seu): “As transferências unilaterais líquidas não são consideradas parte da conta-corrente, **visto que** […] não são resultado da compra e venda de nenhuma mercadoria, serviço ou ativo.” → **ERRADO**: elas integram a conta-corrente como renda secundária. Também `ECO-E1-0830-1` (CACD 2026): o BCB não supervisionaria fintechs “**uma vez que** operam exclusivamente por meio eletrônico” → ERRADO.
**Como reconhecer:** julgue separadamente (a) a tese, (b) a justificativa e (c) se a justificativa de fato explica a tese.
**Gabarito típico:** ERRADO (65 de 65). Taxa de ❌: 18%.

### P7 — O verdadeiro que parece falso (CONTRAINTUITIVO · CERTO)
**Padrão:** a banca escolhe um resultado correto que contraria o senso comum: vantagem comparativa de quem é pior em tudo, crescimento que reduz o bem-estar, multiplicador que cai.
**Item real:** `ECO-E1-0790-1` (CACD 2024, ❌ seu): “Carlos tem vantagem comparativa em ser guitarrista.” → **CERTO**, porque vantagem comparativa depende do custo de oportunidade relativo, e não de produtividade absoluta. Também `ECO-E1-0671-1` (CACD 2025): no câmbio fixo é indispensável avaliar o nível adequado de reservas → CERTO.
**Como reconhecer:** se o item “soa errado”, mas você não consegue apontar a **regra** violada, a tendência é CERTO.
**Gabarito típico:** CERTO (76 de 76). É a **sua maior taxa de ❌: 34%** (26 itens).

### P8 — Resultado que depende do regime (Mundell-Fleming e câmbio)
**Padrão:** o item enuncia um resultado do IS-LM-BP, mas omite, troca ou mistura o regime cambial ou o grau de mobilidade de capital.
**Item real:** `ECO-E3-L00140-1` (CEBRASPE, ANTT 2023): “Se houver perfeita mobilidade de capitais, a expansão fiscal acarretará **queda** das reservas internacionais e da base monetária.” → **ERRADO**: sob câmbio fixo, o juro pressionado para cima atrai capital, o BC compra divisas e as reservas e a base **sobem**. Contraste: `ECO-E3-L00137-1` (mesma prova): com câmbio nominal fixado, o aumento de G aprecia o câmbio **real** (via preços) → CERTO.
**Como reconhecer:** antes de ler o resultado, escreva no rascunho o regime e a mobilidade. Se o item não os diz, verifique se o resultado vale em **todos** os casos.
**Gabarito típico:** misto. Os 83 itens com “mobilidade” dão 49% ERRADO, mas você errou 22 deles (27%). É o seu maior bloco de ❌.

### P9 — Restrição ou proibição institucional inexistente (RESTRICAO · ERRADO)
**Padrão:** a banca cria um “não pode” ou um “apenas” que a teoria ou a lei não impõem.
**Item real:** `ECO-E1-0669-1` (CACD 2025): no câmbio flutuante, “o Banco Central do Brasil **não pode** intervir no mercado para evitar movimentos desordenados” → **ERRADO**. Também `ECO-E1-0823-1` (CACD 2026): no câmbio fixo a autoridade monetária “**não pode** utilizar a taxa de juros” para defender a paridade → ERRADO. E `ECO-E1-0797-1` (CACD 2024): no IED se contabilizariam “**apenas** os capitais que tenham cruzado a fronteira” → ERRADO (o lucro reinvestido também entra).
**Como reconhecer:** flutuante não significa sem intervenção, e fixo não significa sem juros. Desconfie de toda proibição categórica.
**Gabarito típico:** ERRADO (29 de 29). O modulador “não” aparece em 13 itens, com 85% ERRADO.

### P10 — Bateria de cálculo sobre um enunciado (DETALHE × DADO_ALTERADO)
**Padrão:** a banca monta um caso numérico (consumidor Cobb-Douglas, PIB nominal × real, multiplicador, BP) e testa cada passo em itens separados. Os itens corretos reproduzem a conta (DETALHE, CERTO). Os errados trocam um número ou uma justificativa (DADO_ALTERADO ou NEXO, ERRADO).
**Item real:** bloco CACD 2026 do consumidor: `ECO-E1-0809-1`, ótimo (4, 10) com TMS = p₁/p₂ → **CERTO**; `ECO-E1-0810-1`, renda dobrada → (8, 20), homotético → **CERTO**; `ECO-E1-0808-1`, preços ×2 com renda constante: “o vetor de demanda ótima permanecerá o mesmo, pois a restrição se deslocará paralelamente” → **ERRADO** (❌ seu, 1º da lista dos mais instrutivos). Com preços dobrados e renda fixa, a reta se desloca para dentro e o consumo cai pela metade. CEBRASPE: `ECO-E3-L00165-1` (ANTT 2023), c = 0,6 e r = 0,2 → multiplicador = (1 + 0,6)/(0,6 + 0,2) = 2 → **CERTO**.
**Como reconhecer:** faça a conta uma vez e reaproveite-a nos itens do bloco. Verifique sempre a **justificativa** que acompanha o número.
**Gabarito típico:** DETALHE 81/81 CERTO; DADO_ALTERADO 34/34 ERRADO.

### P11 — Troca de ator, de instituição ou de época (TROCA_ATOR · ANACRONISMO)
**Padrão:** a banca atribui função, tese ou data ao órgão, acordo ou autor errado: FMI × Banco Mundial, Basileia I × II, Plano Keynes × White, CEPAL × UNCTAD, Vernon × Linder.
**Item real:** `ECO-E3-L00144-1` (CEBRASPE, ANTT 2023, ❌ seu): “O acordo de **Basileia II** implementou a exigência de capital […] para fazer frente ao risco de crédito.” → **ERRADO**: essa exigência veio de Basileia I. Também `ECO-E3-L00036-1` (TJ/PA 2025): o FMI teria por objetivo principal financiar infraestrutura → ERRADO (essa função é do Banco Mundial). E `ECO-E1-0789-1` (CACD 2024): “**Todas** as instituições do SFN são supervisionadas pelo BCB” → ERRADO.
**Como reconhecer:** monte um quadro “quem faz o quê, desde quando” para BCB/CMN/CVM, FMI/BIRD/OMC e CEPAL/UNCTAD.
**Gabarito típico:** ERRADO (TROCA_ATOR 38/38; ANACRONISMO 12/12).

### P12 — Curto prazo × longo prazo, nível × taxa
**Padrão:** um efeito de curto prazo é apresentado como permanente, ou um efeito sobre o **nível** é apresentado como efeito sobre a **taxa** de crescimento (Solow, Phillips, neutralidade).
**Item real:** `ECO-E1-0487-1` (❌ seu): “De acordo com o modelo de Solow, um aumento na taxa de poupança é capaz de aumentar de forma **permanente** a taxa de crescimento […]” → **ERRADO**. Também `ECO-E2-L01598-1` (❌ seu): pela versão aceleracionista, a Phillips **de longo prazo** seria negativamente inclinada → ERRADO (ela é vertical).
**Como reconhecer:** pergunte “isso é transição ou estado estacionário?” e “é nível ou taxa?”.
**Gabarito típico:** misto. Os 108 itens com “longo prazo” dão 45% ERRADO, e você errou 23 deles.

---

## 2. Checklist de resolução

Antes de marcar qualquer item de Economia:

1. **Qual o modelo e quais as hipóteses?** Economia fechada ou aberta? Curto ou longo prazo? País pequeno ou grande? Concorrência perfeita ou não?
2. **Se é macro aberta: qual o regime cambial e qual o grau de mobilidade de capital?** Escreva no rascunho “fixo/flutuante × nula/imperfeita/perfeita” antes de ler o resultado (P8).
3. **A curva se desloca ou há movimento ao longo dela?** A variável que mudou está nos eixos ou fora deles (P3)?
4. **Há absoluto?** “Sempre”, “necessariamente”, “exclusivamente”, “independentemente”, “automaticamente”, “todos”, “qualquer”. Procure um contraexemplo de uma linha (P4).
5. **Há modulador fraco?** “Pode”, “tende a”, “é possível”. Então o item só cai se for impossível (P5).
6. **Há “pois/uma vez que/portanto”?** Julgue tese, justificativa e nexo separadamente (P6).
7. **Refaça a cadeia causal com setas.** Algum sinal está invertido (P2)? Confira de modo especial o câmbio: “aumento de E” é **depreciação** na cotação do incerto.
8. **O rótulo técnico corresponde à definição?** Comercial × corrente, nominal × operacional × primário, DBGG × DLSP, economias × rendimentos de escala (P1).
9. **É nível ou taxa? Transição ou estado estacionário?** (P12)
10. **O ator, órgão, acordo ou data está certo?** FMI/BIRD, Basileia I/II/III, CEPAL 1948/UNCTAD 1964, CMN/Copom (P11).
11. **Se é cálculo: a conta fecha *e* a justificativa é a correta?** (P10)
12. **Antes de marcar ERRADO num item que “soa estranho”: qual regra exata ele viola?** Se você não sabe dizer, lembre que CONTRAINTUITIVO é sempre CERTO e é onde você mais erra (34%). 144 dos seus 331 ❌ foram itens certos julgados falsos.

---

## 3. Os conceitos mais cobrados

| # | Conceito | Linha de revisão | Itens |
|---|---|---|---|
| 1 | **Custo de oportunidade e vantagem comparativa** | Vantagem comparativa = menor custo de oportunidade **relativo**. Quem é pior em tudo ainda tem vantagem comparativa em algo. | `ECO-E1-0016-1` `ECO-E1-0790-1` `ECO-E1-0791-1` `ECO-E1-0792-1` `ECO-E2-L00197-1` |
| 2 | **CPP** | É côncava por rendimentos decrescentes (custo de oportunidade crescente). Desloca-se só com mais recursos ou com tecnologia. Reduzir desemprego leva a economia **até** a fronteira. | `ECO-E3-L00009-1` `ECO-E1-0015-1` `ECO-E1-0029-1` `ECO-E1-0211-1` |
| 3 | **Incidência tributária e peso morto** (47 itens, 2º subtema mais cobrado) | O lado **mais inelástico** paga mais. Quem paga legalmente não importa. O peso morto cresce com a elasticidade, e a arrecadação não. | `ECO-E1-0235-4` `ECO-E2-L00392-1` `ECO-E2-L00673-1` `ECO-E2-L01401-1` `ECO-E2-L00618-1` |
| 4 | **Externalidades: Pigou × Coase** | Pigou corrige com **imposto** sobre a externalidade negativa (o subsídio serve para a positiva). Coase exige custos de transação nulos e direitos **bem definidos**, e o resultado eficiente independe de a quem se atribuem os direitos. | `ECO-E3-L00175-1` `ECO-E2-L00333-1` `ECO-E2-L00515-1` `ECO-E2-L01761-1` `ECO-E3-L00158-1` |
| 5 | **Bens públicos e comuns** | Público = não rival + não excludente. Comum = rival + não excludente (tragédia dos comuns). Avenida congestionada torna-se rival. Para o bem público, a provisão ótima é Σ BMg = CMg (soma vertical). | `ECO-E3-L00159-1` `ECO-E3-L00160-1` `ECO-E2-L00518-1` `ECO-E3-L00266-1` |
| 6 | **Contas nacionais: PIB × PNB, deflator** | PNB = PIB − RLEE. Se a RLEE é positiva, PNB < PIB. O deflator é PIB **nominal ÷ real**, e não real ÷ nominal. Preço de importado não entra no deflator do PIB. | `ECO-E1-0860-1` `ECO-E3-L00163-1` `ECO-E2-L00401-1` `ECO-E1-0367-1` `ECO-E3-L00415-1` |
| 7 | **BP (BPM6) e poupança externa** | TC = comercial + serviços + renda primária + renda secundária. Déficit em TC = poupança externa **positiva**. TC + conta capital = conta financeira. | `ECO-E1-0782-1` `ECO-E1-0783-1` `ECO-E1-0817-1` `ECO-E1-0818-1` `ECO-E2-L01590-1` |
| 8 | **Base monetária e multiplicador** | m = (1 + c)/(c + r). O multiplicador cai se o público retém mais papel-moeda ou se o compulsório sobe. O compulsório não altera a base, mas reduz M1. | `ECO-E3-L00165-1` `ECO-E3-L00025-1` `ECO-E3-L00066-1` `ECO-E3-L00027-1` `ECO-E1-0316-1` |
| 9 | **Instrumentos de política monetária** | Compra de títulos expande a base, e venda contrai. Redesconto mais barato é expansionista. Open market aproxima a taxa do mercado de reservas da Selic-meta. | `ECO-E3-L00169-1` `ECO-E2-L00483-1` `ECO-E1-0701-1` `ECO-E3-L00445-1` `ECO-E3-L00419-1` |
| 10 | **IS-LM: eficácia e casos extremos** | A política fiscal é mais eficaz quanto **menos** o investimento reage ao juro e quanto mais plana é a LM. Na armadilha da liquidez, a LM é horizontal e a fiscal é plena. No caso clássico, a LM é vertical e o crowding-out é total. | `ECO-E3-L00173-1` `ECO-E3-L00174-1` `ECO-E1-0814-1` `ECO-E2-L00684-1` `ECO-E2-L00615-1` |
| 11 | **Mundell-Fleming** (94 itens, 24 ❌) | Mobilidade perfeita: no câmbio **fixo** a fiscal é eficaz e a monetária ineficaz (a oferta de moeda é endógena); no **flutuante** a monetária é eficaz e a fiscal ineficaz (a apreciação anula). | `ECO-E2-L01513-1` `ECO-E2-L00143-1` `ECO-E1-0877-1` `ECO-E2-L00144-1` `ECO-E1-0769-1` |
| 12 | **Phillips e expectativas** | Phillips original: inflação **cai** com o desemprego (relação inversa). Na aceleracionista (Friedman-Phelps), a de longo prazo é vertical na taxa natural. Em Lucas, só a moeda **não antecipada** afeta o produto. Expectativas racionais não excluem erro, apenas erro sistemático. | `ECO-E1-0491-1` `ECO-E2-L01598-1` `ECO-E2-L01674-1` `ECO-E2-L00456-1` `ECO-E1-0500-1` |
| 13 | **Solow** | A poupança muda o **nível** do produto per capita em estado estacionário, e não a taxa de longo prazo, que é g (exógeno). O produto per capita cresce a g, e não a g + n. Regra de ouro: PMgK = n + δ. Convergência **condicional**. | `ECO-E1-0709-1` `ECO-E1-0487-1` `ECO-E2-L01730-1` `ECO-E2-L01253-1` `ECO-E2-L00526-1` |
| 14 | **Heckscher-Ohlin e teoremas** (49 itens, subtema nº 1) | O país exporta o bem intensivo no fator **abundante**. Stolper-Samuelson: o aumento do preço do bem eleva a remuneração do fator usado intensivamente nele (a proteção favorece o fator **escasso**). Leontief (1953) achou os EUA exportando bens trabalho-intensivos, o que levou a revisões da teoria, e não ao seu abandono. | `ECO-E1-0674-1` `ECO-E1-0673-1` `ECO-E2-L01542-1` `ECO-E2-L01544-1` `ECO-E2-L00699-1` `ECO-E2-L01623-1` |
| 15 | **Tarifa × cota × subsídio** | País pequeno: a tarifa gera perda líquida, ganho do produtor e receita do governo. Na cota, a receita vira renda de quota (com RVE, vai para o exterior). Só o país grande ganha termos de troca com a **tarifa**, enquanto o subsídio à exportação **piora** os termos de troca. | `ECO-E3-L00327-1` `ECO-E2-L00507-1` `ECO-E2-L00556-1` `ECO-E1-0952-1` `ECO-E3-L00035-1` |

---

## 4. Confusões clássicas

| Par que a banca troca | Distinção em uma linha | Exemplo |
|---|---|---|
| Deslocamento × movimento ao longo da curva | Preço do próprio bem → movimento; qualquer outro determinante → deslocamento. | `ECO-E1-0205-1` (E) |
| CPP: desemprego × capacidade | Ocupar recursos ociosos leva a economia até a CPP; mais capital ou tecnologia desloca a CPP. | `ECO-E1-0015-1` (E) × `ECO-E1-0029-1` (C) |
| Balança comercial × transações correntes | TC inclui serviços e rendas primária e secundária, então os saldos podem ter sinais opostos. | `ECO-E1-0817-1` (E) |
| Poupança externa × superávit em TC | Poupança externa positiva = **déficit** em TC. | `ECO-E1-0818-1` (E) |
| Substitutos × complementares | Elasticidade cruzada **positiva** = substitutos; negativa = complementares. | `ECO-E3-L00012-1` (E) |
| Curva de Engel × curva de demanda (Giffen) | Engel relaciona **renda** e quantidade. O Giffen é inferior, então tem Engel **negativa**. A anomalia está na demanda. | `ECO-E2-L01522-1` (E) |
| Rendimentos de escala × economias de escala | Rendimentos = tecnologia (insumos ×k). Economias = custo médio de longo prazo. Pode haver economias com rendimentos constantes. | `ECO-E3-L00013-1` (C) |
| Isoquanta × isocusto | Isoquanta = mesmo **produto**; isocusto = mesmo **custo**. | `ECO-E1-0228-1` (E) |
| Câmbio fixo × flutuante (mobilidade perfeita) | Fixo: fiscal eficaz, juro volta a i*, reservas e base sobem. Flutuante: fiscal anulada pela apreciação. | `ECO-E2-L00144-1` (E) × `ECO-E2-L01513-1` (C) |
| Expansão fiscal no fixo: mobilidade alta × nula | Com mobilidade alta, entra capital, as reservas sobem e a política é eficaz. Com mobilidade nula, a renda maior gera déficit comercial, o BC vende reservas, a base contrai e a renda volta ao nível inicial. | `ECO-E3-L00140-1` (E) × `ECO-E2-L00167-1` (C) |
| Trilema: o que é impossível | Impossível é **fixo + capital livre + autonomia monetária**. Flutuante + capital livre + autonomia é a escolha brasileira desde 1999. | `ECO-E2-L00485-1` (E) |
| Câmbio real sobe × cai (q = EP*/P) | P doméstico ↑ com E e P* constantes → q **cai** (apreciação real), o que prejudica as exportações líquidas. | `ECO-E3-L00029-1` (E) |
| PPC: inflação alta → aprecia × deprecia | Pela PPC relativa, inflação mais alta → **depreciação** nominal. | `ECO-E2-L01627-1` (E) |
| Heckscher-Ohlin × Stolper-Samuelson | HO: comércio favorece o fator abundante. SS: proteção favorece o fator **escasso**. A banca troca qual fator ganha. | `ECO-E1-0673-1` (E) × `ECO-E1-0674-1` (C) |
| Prebisch: qual elasticidade é alta | Periferia: exportações (primários) de **baixa** elasticidade-renda e importações (manufaturas) de **alta**. | `ECO-E3-L00107-1` (E, ❌) |
| CEPAL × UNCTAD | CEPAL 1948 (ECOSOC); UNCTAD 1964, com Prebisch como 1º secretário-geral. | `ECO-E1-0911-1` (C) |
| Vernon × Linder × Krugman | Vernon = ciclo do produto (inovação → padronização). Linder = demanda representativa. Krugman = escala + diferenciação (intraindustrial). | `ECO-E2-L00297-1` (E) · `ECO-E2-L01428-1` (E) |
| Plano Keynes × Plano White | Bancor e International Clearing Union eram de **Keynes**. Venceu White. | `ECO-E2-L00486-1` (E) · `ECO-E2-L00361-1` (E) |
| Phillips curto × longo prazo | Curto prazo: inclinada (com expectativas dadas). Longo prazo: vertical na taxa natural. | `ECO-E2-L01598-1` (E, ❌) |
| Lucas: moeda antecipada × não antecipada | Só a **surpresa** monetária afeta o produto. | `ECO-E2-L00456-1` (E, ❌) |
| Solow: nível × taxa | A poupança eleva o nível de y*; a taxa de longo prazo do per capita é g. | `ECO-E2-L00686-1` (E) |
| Solow (exógeno) × crescimento endógeno | Em Solow o progresso técnico é exógeno; em Romer e Lucas, P&D e capital humano o endogeneízam. | `ECO-E1-0719-1` (E, ❌) |
| Harrod-Domar × Solow | O “fio da navalha” (instabilidade) é de **Harrod-Domar**; Solow é estável. | `ECO-E2-L00765-1` (E) |
| Déficit nominal × operacional × primário | Primário sem juros; operacional = primário + juros **reais**; nominal = primário + juros nominais. Déficit nominal não implica operacional. | `ECO-E3-L00040-1` (E) · `ECO-E2-L00068-1` (E) |
| DBGG × DLSP | A DLSP abrange mais entes (inclui o BC e as estatais), e a DBGG não desconta ativos. | `ECO-E2-L01633-1` (E) |
| QE × aperto monetário | O QE compra ativos longos para **reduzir** juros de longo prazo. | `ECO-E1-0667-1` (E) |
| Basileia I × II | Basileia I (1988) criou o capital mínimo de 8% contra risco de crédito; Basileia II (2004) refinou o cálculo, acrescentou risco operacional e organizou três pilares. | `ECO-E3-L00144-1` (E, ❌) |
| FMI × Banco Mundial | FMI: estabilidade do BP e do câmbio. BIRD: projetos de desenvolvimento. | `ECO-E3-L00036-1` (E) |

---

## 5. Lições para a discursiva

O lote tem só 9 itens DISC (todos de cursos, sobre micro e comércio). Os temas abaixo foram escolhidos pela **recorrência nas objetivas** e pela presença no CACD recente. Autores, datas e dados vêm dos versos dos cards citados. ⏳ marca dado perecível (referência: out/2026).

### 5.1 Política macroeconômica em economia aberta: Mundell-Fleming, trilema e regimes
*Recorrência:* nota 70 tem 94 itens (câmbio flutuante 43, fixo 41) e é a nota com mais ❌ seus (24). Somam-se a ela as notas 66, 67 e 69: mais 123 itens, 12 deles do CACD.

**Tese central:** a eficácia das políticas fiscal e monetária não é absoluta. Ela depende do regime cambial e da mobilidade de capital. Com capital livre, cada país escolhe qual instrumento sacrifica (trilema de Mundell), e a opção brasileira desde 1999 foi preservar a política monetária.

**Argumentos:**
1. **Mobilidade perfeita + fixo:** a política monetária é ineficaz porque a oferta de moeda vira endógena para defender a paridade. A fiscal é plenamente eficaz, com entrada de capital e reservas e base em alta (`ECO-E1-0877-1`, `ECO-E1-0754-1`, `ECO-E3-L00140-1`).
2. **Mobilidade perfeita + flutuante:** a monetária é eficaz via depreciação e exportações líquidas. A fiscal é anulada pela apreciação, que reduz NX na mesma magnitude (`ECO-E2-L00143-1`, `ECO-E2-L01513-1`, `ECO-E2-L00505-1`). Leitura histórica dos cards: os “déficits gêmeos” dos EUA nos anos 1980 (`ECO-E2-L00906-1`).
3. **Trilema:** é impossível combinar câmbio fixo, capital livre e autonomia monetária. Controles de capital reabrem a margem (`ECO-E2-L00485-1`, `ECO-E2-L01238-1`). O FMI passou a admitir medidas de gestão de fluxos desde 2012 (a “visão institucional”), o que deu respaldo ao IOF sobre capital estrangeiro no Brasil em 2009–2013 (`ECO-E2-L01238-1`, `ECO-E1-0946-1`).
4. **Limites do fixo:** com reservas finitas, a defesa da paridade termina em crise. Os cards citam o currency board argentino (1991–2001) e a banda do Real, abandonada em jan./1999 após perda de reservas (`ECO-E2-L00161-1`, `ECO-E2-L01486-1`, `ECO-E1-0892-1`). Mesmo no flutuante, o BC pode intervir (`ECO-E1-0669-1`, CACD 2025) e precisa dimensionar reservas (`ECO-E1-0671-1`).
5. **Nuance contemporânea:** Hélène Rey (2013) argumenta que o ciclo financeiro global reduz a autonomia mesmo com câmbio flutuante, e o trilema viraria “dilema” (`ECO-E2-L00485-1`). Também há custos que o modelo ignora: repasse inflacionário e efeito patrimonial da depreciação ⏳ (`ECO-E2-L01516-1`).

**Autores e dados utilizáveis:** Mundell e Fleming (anos 1960; Mundell, Nobel de 1999); Hélène Rey (2013); tripé de 1999 (metas de inflação, câmbio flutuante e metas fiscais); flutuação em jan./1999 e metas em jun./1999.

**Esqueleto:** (i) introdução com o trilema e a pergunta: qual instrumento funciona sob qual regime? (ii) modelo IS-LM-BP e a hipótese de pequena economia aberta; (iii) quadro 2×2 de regime × política, com mecanismo de cada célula (juro → fluxo de capital → câmbio ou reservas → NX ou base); (iv) mobilidade imperfeita como caso intermediário; (v) Brasil: banda até 1999 e tripé depois; (vi) limites (ciclo financeiro global, repasse, reservas); (vii) conclusão: a escolha de regime é a escolha do instrumento que se preserva.

### 5.2 CEPAL, deterioração dos termos de troca e industrialização
*Recorrência:* nota 74 tem 19 itens (11% CACD). O CACD 2025 cobrou dois itens sobre Prebisch-Singer (`ECO-E1-0675-1`, `ECO-E1-0676-1`). O tema conversa com a nota 79 (política comercial) e com a nota 65 (SMI).

**Tese central:** para o estruturalismo cepalino, a divisão internacional do trabalho centro-periferia não distribui igualmente os frutos do progresso técnico. A especialização primária impõe uma tendência à deterioração dos termos de troca e à restrição externa, o que justificaria a industrialização deliberada.

**Argumentos:**
1. **Elasticidades-renda:** os primários da periferia têm baixa elasticidade-renda e as manufaturas do centro têm alta. O crescimento mundial amplia a demanda por manufaturas mais que por primários (`ECO-E2-L01694-1`, `ECO-E2-L01471-1`). A inversão disso é a pegadinha clássica (`ECO-E3-L00107-1`, ❌ seu).
2. **Estruturas de mercado:** os mercados industriais oligopolizados retêm os ganhos de produtividade em salários e lucros. Nos primários, mais concorrenciais, esses ganhos viram queda de preço (`ECO-E2-L01576-1`). Atenção à inversão em `ECO-E2-L00705-1` (E).
3. **Hipóteses do CACD 2025:** a periferia é tomadora de preços (`ECO-E1-0676-1`) e a demanda por primários é inelástica a preço (`ECO-E1-0675-1`).
4. **Crítica à estática clássica:** a vantagem comparativa ricardiana é estática e não incorpora a dinâmica das elasticidades. Daí o argumento a favor da substituição de importações (`ECO-E1-0921-1`, `ECO-E2-L00299-1`, E: a CEPAL **não** defende benefício equitativo). A versão moderna é a restrição de Thirlwall (1979) (`ECO-E2-L01471-1`).
5. **Institucionalização e Brasil:** as ideias de Prebisch levaram à UNCTAD (1964), de que foi o primeiro secretário-geral (1964–1969). Os frutos dessa agenda foram o SGP e a Parte IV do GATT (1965) (`ECO-E1-0911-1`). No Brasil, Celso Furtado trabalhou na CEPAL (1949–1957) e escreveu *Formação Econômica do Brasil* (1959) (`ECO-E1-0913-1`). A ISI orientou o Plano de Metas (1956–1961) e o II PND (1974–1979) (`ECO-E2-L01694-1`).

**Autores e dados (dos cards):** Prebisch, “manifesto” de 1949, e Singer, 1950, com dados britânicos de 1876–1938 (`ECO-E1-0277-1`); CEPAL criada em 1948 pelo ECOSOC, com o Caribe incluído em 1984 (`ECO-E1-0910-1`); Aníbal Pinto (1970) e a heterogeneidade estrutural (`ECO-E2-L00704-1`); Cardoso e Faletto (1969) e a teoria da dependência, que é outra corrente (`ECO-E1-0921-1`); a crítica de Pastore (1971) sobre a resposta da oferta agrícola a preços (`ECO-E2-L00847-1`); Maria da Conceição Tavares (1964) (`ECO-E1-0913-1`).

**Cuidados de cronologia (os cards insistem):** a guinada de 1930 veio do choque da Depressão, e a tese de Prebisch é de **1949** (`ECO-E1-0277-1`, E). Prebisch defendeu ISI voltada ao **mercado interno**, e não industrialização “agressivamente voltada para a exportação” (`ECO-E1-0912-1`, E). Os EUA **não** apoiaram a criação da CEPAL (`ECO-E1-0910-1`, E).

**Esqueleto:** (i) contexto: a teoria clássica das vantagens comparativas e o pós-guerra latino-americano; (ii) a tese de Prebisch-Singer e seus dois mecanismos (elasticidades e estruturas de mercado); (iii) implicações: restrição externa e ISI; (iv) desdobramentos: UNCTAD, SGP, Furtado e o Brasil; (v) críticas e atualizações (Pastore, Thirlwall, regionalismo aberto dos anos 1990, citado em `ECO-E3-L00395-1`); (vi) conclusão sobre a atualidade do debate (inserção primária e CGVs, `ECO-E2-L00244-1`).

### 5.3 Comércio internacional, política comercial e OMC
*Recorrência:* notas 73 (104), 75 (39) e 79 (97) somam 240 itens. Heckscher-Ohlin é o subtema mais cobrado do lote (49), seguido por vantagens comparativas (47) e tarifas (41). O CACD tem 6 itens na nota 73 e 2 na 79.

**Tese central:** o livre comércio gera ganhos agregados, mas com perdedores identificáveis (Stolper-Samuelson). Os instrumentos de proteção diferem em custo de bem-estar e em quem fica com a renda. O sistema multilateral (GATT/OMC) busca disciplinar esses instrumentos sem eliminar o espaço legítimo de defesa comercial e de regulação.

**Argumentos:**
1. **Ganhos e distribuição:** o comércio expande o consumo além da CPP (`ECO-E3-L00010-1`). Em HO, ele eleva a remuneração do fator abundante (`ECO-E1-0674-1`, CACD 2025), e a proteção beneficia o fator escasso (`ECO-E1-0673-1`, CACD 2025). Em países desenvolvidos, a abertura tende a ampliar a desigualdade (`ECO-E2-L00298-1`).
2. **Além de HO:** o paradoxo de Leontief (1953) motivou revisões da teoria, e não o seu abandono (`ECO-E2-L01577-1`, `ECO-E2-L01623-1`). As novas teorias (Krugman, 1979–1980, Nobel de 2008) explicam o comércio intraindustrial por escala e diferenciação (`ECO-E1-0858-1`, `ECO-E1-0644-1`).
3. **Instrumentos:** no país pequeno, a tarifa gera perda líquida e a cota equivalente gera o mesmo preço sem arrecadação (Bhagwati, 1965) (`ECO-E3-L00327-1`). Com RVE, a renda vai ao exterior, como na limitação das exportações japonesas de automóveis para os EUA a partir de 1981 (`ECO-E1-0952-1`, `ECO-E2-L00831-1`). O subsídio à exportação piora os termos de troca até do país grande (`ECO-E2-L00700-1`, E). A tarifa sozinha não garante melhora do saldo comercial (simetria de Lerner, 1936) (`ECO-E3-L00035-1`).
4. **Regras multilaterais:** o GATT vigorou sem ser organismo formal até a OMC (`ECO-E1-0972-1`). A Rodada Uruguai trouxe o primeiro acordo agrícola e o GATS (1994) (`ECO-E3-L00324-1`, `ECO-E3-L00109-1`). Avanços foram maiores em manufaturas que na agricultura (`ECO-E1-0964-1`). Os subsídios agrícolas à exportação foram eliminados em Nairóbi (2015) (`ECO-E1-0159-1`). Barreiras técnicas são admitidas pelo Acordo SPS (1995) se tiverem base científica e não discriminarem (`ECO-E1-0943-1`, `ECO-E1-0678-1`).
5. **Brasil e conjuntura:** o contencioso do algodão contra os EUA (DS267, 2002) e Embraer × Bombardier (`ECO-E1-0159-1`, `ECO-E3-L00397-1`); o Mercosul como união aduaneira imperfeita, com TEC desde 1995 (`ECO-E3-L00034-1`). ⏳ As tarifas norte-americanas de 2025 e a sobretaxa de até 50% sobre o Brasil a partir de ago./2025 (`ECO-E1-0697-1`). ⏳ A conclusão política do acordo Mercosul-UE em dez./2024 (`ECO-E3-L00361-1`).

**Autores (versos das notas 73, 75 e 79):** Heckscher (1919), Ohlin (1933), Stolper-Samuelson (1941), Leontief (1953), Vernon (1966), Linder (1961), Krugman, Melitz (2003), Tinbergen (1962), Viner (1923) e Amiti, Redding e Weinstein (2019).

**Esqueleto:** (i) por que comerciar: Ricardo → HO → novas teorias; (ii) quem ganha e quem perde: Stolper-Samuelson; (iii) instrumentos e custos (tarifa, cota, RVE, subsídio), com gráfico de excedentes; (iv) país grande × pequeno: termos de troca e retaliação; (v) o marco GATT/OMC e a defesa comercial; (vi) inserção brasileira e conjuntura ⏳; (vii) conclusão.

### 5.4 Crescimento: Solow × Harrod-Domar × crescimento endógeno × Schumpeter
*Recorrência:* notas 56 (65) e 57 (33). Você errou 16 itens da nota 56 (25%), concentrados em estado estacionário (7) e em população, tecnologia e convergência (7).

**Tese central:** acumular capital físico não sustenta o crescimento per capita de longo prazo por causa dos rendimentos decrescentes (Solow). O crescimento sustentado depende do progresso técnico, que as teorias endógenas explicam por decisões econômicas (P&D, capital humano, transbordamentos) e que Schumpeter associa à destruição criadora.

**Argumentos:**
1. **Harrod-Domar:** g = s/v com relação capital-produto fixa. O equilíbrio é instável (“fio da navalha”) e o modelo serviu ao planejamento e ao “hiato de poupança” dos anos 1950–60 (`ECO-E1-0706-1`, `ECO-E1-0740-1`, `ECO-E2-L00523-1`).
2. **Solow (1956):** com substituição entre fatores e rendimentos decrescentes, a economia converge ao estado estacionário. A poupança muda o nível, e não a taxa (`ECO-E1-0709-1`, `ECO-E2-L00623-1`). Há uma regra de ouro (`ECO-E2-L01253-1`, `ECO-E2-L01589-1`) e convergência condicional (`ECO-E2-L00526-1`).
3. **Resíduo:** na contabilidade do crescimento (Solow, 1957), cerca de 7/8 do crescimento do produto por hora nos EUA de 1909 a 1949 ficou no resíduo, “uma medida da nossa ignorância” (Abramovitz) (`ECO-E2-L00172-1`, `ECO-E1-0718-1`).
4. **Endógeno:** Arrow (1962), com o learning by doing; Romer (1986), com transbordamentos; Lucas (1988), com capital humano; Romer (1990), com ideias não rivais e P&D; Aghion e Howitt (1992), com a destruição criadora formalizada. Com retornos constantes no fator acumulável (AK, Rebelo, 1991), a poupança afeta a **taxa** de longo prazo (`ECO-E2-L01261-1`, `ECO-E2-L00766-1`, `ECO-E3-L00449-1`). Poupança externa **não** é o motor desses modelos, e sim dos modelos de hiato de Chenery e Strout (1966) (`ECO-E3-L00448-1`).
5. **Schumpeter:** *Teoria do Desenvolvimento Econômico* (1911): o empresário inovador e o crédito rompem o fluxo circular, e a moeda não é neutra. *Capitalismo, Socialismo e Democracia* (1942): destruição criadora (`ECO-E1-0741-1`, `ECO-E1-0452-1`, `ECO-E2-L00175-1`). Aghion e Howitt receberam o Nobel de 2025, com Joel Mokyr (`ECO-E1-0452-1`). Complemento institucionalista: Douglass North e as instituições como “regras do jogo” (`ECO-E1-0722-1`).

**Esqueleto:** (i) a pergunta: por que uns países são ricos e outros crescem? (ii) Harrod-Domar e a instabilidade; (iii) Solow: estado estacionário, nível × taxa, convergência condicional; (iv) o resíduo como limite; (v) respostas endógenas e schumpeterianas; (vi) implicações de política (educação, P&D, instituições, e não apenas poupança); (vii) conclusão sobre o Brasil sem dados inventados: usar só a lógica dos modelos (cf. `ECO-E2-L01441-1`, E: baixa poupança **não** reduz a taxa de estado estacionário em Solow).

### 5.5 Política monetária: metas de inflação, expectativas e instrumentos não convencionais
*Recorrência:* notas 35, 36, 38 e 40 somam 153 itens. O CACD 2025 cobrou forward guidance, QE e juros negativos (`ECO-E1-0665-1`, `ECO-E1-0666-1`, `ECO-E1-0667-1`, `ECO-E1-0668-1`).

**Tese central:** a política monetária moderna atua pelo juro de curto prazo e, sobretudo, pela gestão de expectativas. Quando o juro bate no limite inferior, os BCs recorrem à comunicação e ao balanço. A credibilidade, sustentada por regras e autonomia, é o ativo central.

**Argumentos:**
1. **Metas:** o instrumento é o juro de curto prazo, e não o controle de agregados (`ECO-E1-0702-1`, `ECO-E2-L00614-1`, E). A Nova Zelândia inaugurou o regime em 1990 e o Brasil o adotou em jun./1999 (Decreto 3.088) (`ECO-E2-L00614-1`). O CMN fixa a meta e o Copom define a Selic (`ECO-E2-L01039-1`, E por atribuir a meta ao Copom). ⏳ Meta contínua de 3% desde 2025 (`ECO-E1-0562-1`, `ECO-E2-L01039-1`).
2. **Credibilidade:** pela inconsistência temporal de Kydland e Prescott (1977) e Barro e Gordon (1983), o BC discricionário gera viés inflacionário. As respostas são o banqueiro central conservador (Rogoff, 1985) e a autonomia, no Brasil formalizada pela LC 179/2021 (`ECO-E2-L00385-1`, `ECO-E1-0561-1`). Políticas sobre expectativas **são** efetivas (`ECO-E1-0560-1`, E).
3. **Regra de Taylor (1993):** princípio de Taylor, com juro nominal subindo mais que a inflação (`ECO-E2-L01230-1`). Clarida, Galí e Gertler (2000) estimaram coeficiente menor que 1 nos anos 1970 e maior que 1 na era Volcker-Greenspan.
4. **Choques de oferta:** acomodar reduz a perda de produto, mas aumenta a inflação (`ECO-E2-L01559-1`, `ECO-E2-L01601-1`). A acomodação **integral** não é a resposta ótima (`ECO-E2-L00386-1`, E). O canal cambial afeta os preços diretamente: o card cita 2002, com depreciação forte e IPCA de 12,5% (`ECO-E2-L00312-1`).
5. **Não convencional:** o QE compra ativos longos para reduzir juros de longo prazo no limite inferior zero (`ECO-E2-L00315-1`, `ECO-E1-0667-1`). Forward guidance: o Copom o adotou em ago./2020 e o retirou em jan./2021 (`ECO-E1-0666-1`). Há ainda juros negativos (`ECO-E1-0665-1`, ⚠️ contestável quanto à data) e a autorização ao BCB para comprar títulos privados (EC 106) (`ECO-E2-L01749-1`). O QE não é “por si só” inflacionário (`ECO-E2-L00319-1`, E).

**Esqueleto:** (i) do controle de agregados às metas; (ii) o arcabouço brasileiro (CMN, Copom, LC 179/2021, meta ⏳); (iii) credibilidade e expectativas (Kydland-Prescott, Barro-Gordon, Taylor); (iv) choques de oferta e o dilema da acomodação; (v) o pós-2008: QE, FG, juros negativos; (vi) riscos (dominância fiscal, coordenação, que é a nota 39, com apenas 2 itens); (vii) conclusão.

> **Tema emergente (CACD 2024–2026):** sistema monetário internacional e hegemonia do dólar. Os cards cobrem o dilema de Triffin (`ECO-E2-L00362-1`), o fim da conversibilidade em 1971 (`ECO-E2-L00367-1`), a multipolaridade monetária (`ECO-E1-0779-1`, `ECO-E1-0781-1`, ambos CACD 2024), o renminbi na cesta do DES desde 2016 (`ECO-E2-L00363-1`), a “inércia institucional” e os efeitos de rede (`ECO-E2-L00365-1`) e o NDB, criado em jul./2015 com capital autorizado de US$ 100 bi (`ECO-E1-0980-1`). Vale um esqueleto próprio se sobrar tempo.

### 5.6 Erros conceituais das objetivas que também derrubam a nota na discursiva
- **Esquecer o regime.** Escrever “a política fiscal é ineficaz numa economia aberta” sem qualificar câmbio e mobilidade (P8; 22 ❌ seus em itens com “mobilidade”).
- **Confundir nível e taxa.** Dizer que mais poupança acelera permanentemente o crescimento em Solow (`ECO-E1-0487-1`, ❌).
- **Inverter o câmbio.** “Juro alto deprecia” (`ECO-E1-0819-1`). Defina sempre a convenção (E = R$/US$) e diga se fala do câmbio nominal ou do real.
- **Trocar agregados.** Comercial por corrente (`ECO-E1-0782-1`), poupança externa positiva por superávit (`ECO-E1-0818-1`), nominal por operacional (`ECO-E3-L00040-1`), DBGG por DLSP (`ECO-E2-L01633-1`).
- **Atribuir a tese ao autor errado.** Bancor a White (`ECO-E2-L00486-1`), fio da navalha a Solow (`ECO-E2-L00765-1`), endogeneidade tecnológica a Solow (`ECO-E1-0719-1`), “dependência” à CEPAL (`ECO-E1-0921-1`, a dependência é de Cardoso e Faletto).
- **Errar a cronologia cepalina.** A ISI de 1930 como fruto de Prebisch (`ECO-E1-0277-1`).
- **Absolutizar.** “Tarifa garante saldo comercial” (`ECO-E3-L00035-1`), “QE é inflacionário por si só” (`ECO-E2-L00319-1`), “oligopólios são, em geral, prejudiciais porque não geram externalidades positivas” (`ECO-E3-L00413-1`). Na discursiva, a banca premia a qualificação (“sob as hipóteses de…”, “tende a…”).
- **Juízo normativo sem base.** Controle de preços “corrige falhas e melhora o bem-estar de todos” (`ECO-E3-L00008-1`, JUIZO_INDEVIDO).

### 5.7 Estrutura e vocabulário técnico
**Estrutura que funciona em Economia:**
1. **Delimitar o modelo** na introdução: hipóteses, horizonte (CP/LP), economia pequena ou grande, regime.
2. **Mecanismo em cadeia:** escreva a transmissão como sequência causal (choque → variável intermediária → resultado). É o que separa a resposta técnica da opinativa.
3. **Um gráfico descrito em palavras**, se não puder desenhar: “a IS desloca-se para a direita; com BP horizontal, …”.
4. **Caso brasileiro ou histórico** retirado só dos cards (1999, CEPAL/Furtado, OMC/algodão). Marque o que for perecível com o ano de referência.
5. **Limites e controvérsias** (Rey, Pastore, Leontief, contestáveis), seguidos de uma conclusão que responda exatamente ao comando.

**Vocabulário a usar com precisão:** “deslocamento” × “movimento ao longo”; “apreciação/depreciação” (flutuante) × “valorização/desvalorização” (decisão oficial no fixo); “câmbio real (q = EP*/P)”; “mobilidade perfeita (BP horizontal)”; “oferta de moeda endógena”; “esterilização”; “crowding-out”; “estado estacionário”; “regra de ouro”; “convergência condicional”; “resíduo de Solow/PTF”; “termos de troca”; “elasticidade-renda”; “restrição externa”; “fator abundante/escasso”; “renda de quota”; “salvaguarda × antidumping × medida compensatória”; “inconsistência temporal”; “ancoragem de expectativas”; “limite inferior zero”. Evite “juros” sem qualificar se são nominais ou reais, e “câmbio subiu” sem indicar a convenção.

---

## 6. Plano de revisão

### 6.1 Onde estão os seus ❌
Os 331 ❌ se distribuem assim: microeconomia (notas 01–12) 118 de 763 · macro fechada, crescimento e trabalho (15–59) 98 de 569 · internacional (65–79) 82 de 530 · fiscal (47–50) 16 de 148 · moeda e bancos (35–42) 14 de 176 · conjuntura (83–84) 3 de 27.

| Prioridade | Nota | ❌ / total | Taxa | Por quê |
|---|---|---|---|---|
| 1 | 70 Mundell-Fleming | 24 / 94 | 26% | Maior volume de ❌. Flutuante 13/43, fixo 10/41. É também o principal tema de discursiva. |
| 2 | 10 Oligopólios | 12 / 38 | 32% | Maior taxa entre as notas com volume. Cartel e conluio: 6/13. |
| 3 | 28 OA-DA · 29 Phillips | 9/30 · 10/39 | 30% · 26% | Choques de oferta (8/22) e CP × LP. |
| 4 | 56 Solow | 16 / 65 | 25% | Nível × taxa, g × g + n, regra de ouro. |
| 5 | 17 Contas Nacionais · 18 BP | 23/114 · 9/74 | 20% · 12% | O BP é a nota com mais itens CACD (8). Comercial × corrente, PIB × PNB, deflator. |
| 6 | 04 / 04-A Consumidor · 05 Produção | 18/91 · 8/33 · 9/36 | 20% · 24% · 25% | Axiomas, Engel × Giffen, isoquanta. O 1º item mais instrutivo (`ECO-E1-0808-1`) é daqui. |
| 7 | 66 Câmbio · 69 Câmbio-juros | 12/79 · 4/31 | 15% · 13% | PPC, câmbio real, bandas: base da nota 70. |
| 8 | 73 Comércio clássico · 79 Política comercial | 14/104 · 11/97 | 13% · 11% | HO/SS (7/49), tarifas. É tema de discursiva. |
| 9 | 07-A · 08 · 03 · 12 | 11/60 · 12/92 · 12/104 · 10/96 | 18% · 13% · 12% · 10% | Oferta da firma (CMg acima do CVMe, e não do CTMe), monopólio, incidência, Coase. |
| 10 | 47 · 48 Fiscal | 10/104 · 6/32 | 10% · 19% | Equivalência ricardiana, resultados nominal × operacional. |

**Ordem sugerida (3 ciclos):**
1. **Ciclo 1, economia aberta:** 66 → 69 → 70, com o quadro 2×2 de Mundell-Fleming e o trilema. Feche com 18 (BP) e 67 (reservas, 38% CACD). Redija o esqueleto 5.1.
2. **Ciclo 2, macro de curto e longo prazo:** 27 → 28 → 29 (expectativas) → 56 → 57. Redija os esqueletos 5.4 e 5.5. Inclua 38 e 40 (pouco erro, mas alta presença no CACD 2025).
3. **Ciclo 3, micro e comércio:** 04/04-A → 05 → 07-A → 08 → 10, depois 73 → 74 → 79. Redija os esqueletos 5.2 e 5.3.

**Transversal, em todos os ciclos:** releia primeiro os itens CONTRAINTUITIVO que você errou (26 ❌, 34%) e depois os de INVERSAO (56 ❌). Antes de cada sessão, refaça o checklist da seção 2. Revise os 12 ❌ do CACD: `ECO-E1-0029-1`, `ECO-E1-0015-1`, `ECO-E1-0808-1`, `ECO-E1-0860-1`, `ECO-E1-0783-1`, `ECO-E1-0364-1`, `ECO-E1-0318-1`, `ECO-E1-0815-1`, `ECO-E1-0829-1`, `ECO-E1-0779-1`, `ECO-E1-0795-1`, `ECO-E1-0790-1`.

### 6.2 Lacunas: estudar pela teoria, sem itens no lote
- ⬜ **Nota 60 (🏭 Precarização, reforma trabalhista de 2017, conjuntura do trabalho):** 0 itens. Estude pela nota-mãe, ligando com a nota 59 (desemprego e Okun, 7 ❌ em 29 itens). É candidata natural a discursiva de conjuntura.
- ⬜ **Nota 85 (🧭 Raio-X e diagnósticos da economia brasileira: perspectivas em disputa):** 0 itens. Junto com as notas 83 e 84 (só 27 itens no total), é a parte mais fraca do lote em volume. Na discursiva, trate dados de conjuntura como ⏳ e cite apenas o que estiver nas notas.
- ⬜ **Nota 03 › “🧮 Cotas e outras intervenções”:** H2 vazio. A lógica de cota aparece na nota 79 (cota de importação e equivalência com a tarifa, `ECO-E3-L00327-1`, `ECO-E1-0952-1`). Revise por analogia: a cota cria renda de escassez, e não arrecadação.
- ⬜ **Nota 08 › “🛒 Monopsônio”:** H2 vazio. O único eco no lote é a contestação de `ECO-E2-L00041-1` (monopsônio como exceção à ideia de “tomador de custo”). Estude o caso-espelho do monopólio: o comprador único iguala o valor do produto marginal ao custo marginal do fator, contrata menos e paga menos que no competitivo. É também o gancho para o debate sobre salário mínimo, que no lote aparece só no caso competitivo (`ECO-E1-0505-1`).
- Notas com volume baixo e peso relativo alto no CACD: 37 (5 itens, 20% CACD), 40 (12, 25%), 41 (8, 50%), 42 (8, 50%), 67 (13, 38%). São poucas questões, mas a banca do CACD vem cobrando esses temas. Revise-os pelos itens CACD listados nas seções 1 e 5.5.
