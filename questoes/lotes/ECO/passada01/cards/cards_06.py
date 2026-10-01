"""Cards do lote de redação 06 — ECO, passada 01 (notas 02 e 03)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "rec": "💰 Elasticidade, receita e gasto",
    "det": "⏳ Determinantes e prazos",
    "cruz": "🔗 Elasticidade-renda e cruzada",
    "of": "🏭 Elasticidade da oferta",
    "exc": "😊 Excedentes e eficiência",
    "trib": "💸 Tributos: incidência e peso morto",
    "teto": "🚧 Preços máximos e mínimos",
}

COM_NIDI_MAR25 = ("Os agentes microeconômicos fazem suas escolhas de forma racional em um cenário de informações "
                  "completas e simetricamente distribuídas. A respeito da Teoria do Consumidor, julgue certo ou "
                  "errado (C ou E) os itens a seguir.")
COM_2023 = ("Acerca da incidência de tributos sobre o consumo, e considerando que a questão se limita a mercados "
            "de concorrência perfeita, julgue (C ou E) o item a seguir.")
COM_RT_A4 = "A respeito dos mercados competitivos, responda C ou E."
COM_RT_A5 = "Acerca dos controles de preços e de seus efeitos sobre o equilíbrio de mercado, julgue o item."

CARDS = [
    # ------------------------------------------------------------------ E2-L00881
    {
        "id": "ECO-E2-L00881-1", "fonte_ref": "E2-L00881", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Com relação às intervenções governamentais no equilíbrio de mercado e ao conceito de "
                    "elasticidade, julgue (C ou E) os itens seguintes."),
        "rotulo_item": "Item",
        "assertiva": ("Considerando uma curva de demanda negativamente inclinada de determinado produtor, caso a "
                      "elasticidade da demanda seja maior que 1, em valor absoluto, a receita de vendas do produtor "
                      "aumenta quando o preço sobe."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando uma curva de demanda negativamente inclinada de determinado produtor, caso a "
                      "elasticidade da demanda seja maior que 1, em valor absoluto, a receita de vendas do produtor ")
                   + vm("aumenta") + az(" quando o preço sobe."),
        "poucas": ("Com " + azb("demanda elástica") + " (|ε| > 1), a quantidade cai proporcionalmente <b>mais</b> "
                   "do que o preço sobe: a receita p × q " + vd("diminui") + ". Receita sobe com o preço só na "
                   "demanda inelástica."),
        "destrinchando": [
            "Receita total RT = p × q. Em variações pequenas, " + vd("%ΔRT ≈ %Δp + %Δq") + ". Como %Δq = ε × %Δp, "
            "o sinal do efeito depende de |ε|: se |ε| > 1, o %Δq (negativo) supera o %Δp e a receita cai quando "
            "o preço sobe.",
            "Dois efeitos disputam: o " + azb("efeito preço") + " (ganha-se mais em cada unidade que continua "
            "vendida) e o " + azb("efeito quantidade") + " (perdem-se as unidades que deixam de ser vendidas). Na "
            "demanda elástica, vence o segundo; na inelástica, o primeiro; na unitária (|ε| = 1), empatam e a "
            "receita fica constante.",
            "Tabela de bolso — preço ↑: elástica → RT ↓; inelástica → RT ↑; unitária → RT constante. Preço ↓: "
            "tudo ao contrário.",
            "Na demanda <b>linear</b>, a elasticidade muda ao longo da reta: é elástica na metade superior, "
            "unitária no ponto médio (onde a receita é máxima) e inelástica na metade inferior. Por isso o "
            "monopolista opera sempre no trecho elástico: ali a receita marginal " + vd("RMg = p(1 − 1/|ε|)")
            + " é positiva.",
            vm("Regra-âncora: a receita anda no sentido da variável que reage mais — elástica, segue a "
               "quantidade; inelástica, segue o preço."),
        ],
        "grafico_verso": "ECO-E2-L00881-1-V1",
        "dissecando": (cz("[inversão]") + " O item aplica à demanda elástica o resultado da inelástica. Tudo o "
                       "mais (inclinação negativa, |ε| > 1, preço subindo) está correto, o que dá ar de "
                       "verdade. Teste rápido: elástica = consumidor “foge” do aumento → vende-se muito menos → "
                       "receita cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…caso a elasticidade da demanda seja menor que 1, em valor absoluto, a receita de vendas do "
            "produtor aumenta quando o preço sobe.”</i> → CERTO",
            "<i>“…caso a elasticidade da demanda seja igual a 1, em valor absoluto, a receita aumenta quando o "
            "preço cai.”</i> → ERRADO (unitária: receita constante)",
        ])],
        "reescrita": ("Considerando uma curva de demanda negativamente inclinada de determinado produtor, caso a "
                      "elasticidade da demanda seja maior que 1, em valor absoluto, a receita de vendas do produtor "
                      + hl("diminui") + " quando o preço sobe."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Demanda elástica: alta de preço reduz a quantidade mais que proporcionalmente e "
                             "reduz a receita; demanda inelástica: o inverso. Gráficos de receita P × Q nos dois "
                             "casos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 139", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 140", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00881-1-V1, só o caso elástico)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00972
    {
        "id": "ECO-E2-L00972-1", "fonte_ref": "E2-L00972", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": ("Em relação à microeconomia e à teoria do comércio internacional, julgue (C ou E) os seguintes "
                    "itens."),
        "rotulo_item": "Item",
        "assertiva": "A demanda será mais elástica quanto maior o horizonte temporal.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A demanda será mais elástica quanto <u>maior o horizonte temporal</u>."),
        "poucas": ("Com mais tempo, o consumidor descobre " + azb("substitutos") + ", troca equipamentos e muda "
                   "hábitos: a resposta da quantidade ao preço cresce. Demanda de " + vd("longo prazo")
                   + " é, em regra, mais elástica."),
        "destrinchando": [
            "Determinantes clássicos da " + azb("elasticidade-preço da demanda") + ": (1) disponibilidade de "
            "substitutos próximos; (2) bem necessário × supérfluo; (3) peso do bem no orçamento; (4) definição "
            "do mercado (“alimentos” é menos elástico que “sorvete de baunilha”); (5) " + azb("horizonte de "
            "tempo") + ".",
            "Mecanismo do tempo: no curto prazo, o consumidor está preso ao estoque de bens que já tem (carro, "
            "geladeira, chuveiro elétrico). Se a energia encarece, quase não dá para reduzir o consumo; com os "
            "meses, compram-se aparelhos eficientes, instala-se aquecimento solar, mudam-se hábitos — e a "
            "quantidade demandada cai bem mais.",
            "Exemplo histórico: nos choques do petróleo dos anos 1970, a gasolina subiu muito e o consumo quase "
            "não caiu de imediato; a queda veio anos depois, com carros mais econômicos.",
            "Exceção que a banca pode explorar: para " + azb("bens duráveis") + " (automóveis, eletrodomésticos), "
            "a demanda costuma ser <b>mais</b> elástica no curto prazo — diante de um aumento, o consumidor "
            "simplesmente adia a troca; no longo prazo, porém, a reposição se impõe "
            "(" + oc("Pindyck e Rubinfeld") + ", <i>Microeconomia</i>).",
            "O mesmo vale para a oferta: no longo prazo as firmas ajustam capacidade, entram e saem do mercado, "
            "e a oferta também se torna mais elástica.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz a regra de manual. O “será” soa "
                       "absoluto, mas a banca o trata como tendência geral; a exceção dos duráveis só derrubaria "
                       "um item que a citasse expressamente. Palavra-chave: <b>horizonte temporal</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda tende a ser menos elástica no longo prazo, pois os hábitos de consumo se "
            "cristalizam.”</i> → ERRADO (inversão: mais tempo, mais substituição)",
            "<i>“Para bens duráveis, como automóveis, a demanda pode ser mais elástica no curto prazo do que no "
            "longo prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["quanto maior"], "dificuldade": 1,
        "comentario_fonte": ("Com mais tempo, os consumidores reagem mais ao preço; ex.: energia elétrica, "
                             "consumidores buscam formas de economizar."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01375
    {
        "id": "ECO-E2-L01375-1", "fonte_ref": "E2-L01375", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "FGV", "prova": "DPE/RS/Analista/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às elasticidades da demanda.",
        "rotulo_item": "Item",
        "assertiva": "O valor da elasticidade-preço cruzada indica se um bem é de luxo ou essencial.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O valor da elasticidade-") + vm("preço cruzada") + az(" indica se um bem é de luxo ou "
                                                                            "essencial."),
        "poucas": ("Luxo × essencial se mede pela " + azb("elasticidade-renda") + ". A " + azb("cruzada")
                   + " classifica a <b>relação entre dois bens</b>: substitutos, complementares ou "
                   "independentes."),
        "destrinchando": [
            "Cada elasticidade responde a uma pergunta diferente — e classifica uma coisa diferente:",
            azb("Elasticidade-preço (própria)") + " = %Δq<sub>x</sub> / %Δp<sub>x</sub> → demanda elástica, "
            "inelástica ou unitária.",
            azb("Elasticidade-renda") + " = %Δq / %ΔR → " + vd("ε<sub>R</sub> > 1") + ": bem de luxo "
            "(superior); " + vd("0 < ε<sub>R</sub> < 1") + ": bem necessário/essencial; " + vd("ε<sub>R</sub> < 0")
            + ": bem inferior. Luxo e necessário são, ambos, bens normais.",
            azb("Elasticidade-preço cruzada") + " = %Δq<sub>x</sub> / %Δp<sub>y</sub> → positiva: "
            "substitutos (café × chá); negativa: complementares (impressora × cartucho); nula: independentes.",
            "Ligação com a " + oc("Lei de Engel") + " (" + oc("Ernst Engel") + ", séc. XIX): à medida que a renda "
            "cresce, a fatia do orçamento gasta com alimentos cai — alimentos têm elasticidade-renda entre 0 e 1.",
            vm("Regra-âncora: renda → luxo/necessário/inferior; cruzada → substituto/complementar."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca uma elasticidade por outra: a classificação "
                       "luxo × essencial é a da elasticidade-renda. Pista: “cruzada” sempre envolve <b>dois</b> "
                       "bens; luxo/essencial é atributo de <b>um</b> bem. 🔥 Itens de classificação de bens "
                       "costumam trocar as três elasticidades entre si."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O valor da elasticidade-renda da demanda indica se um bem é de luxo ou necessário.”</i> → CERTO",
            "<i>“Bem de luxo é aquele cuja elasticidade-renda é positiva.”</i> → ERRADO (incompleto: exige "
            "ε<sub>R</sub> > 1; entre 0 e 1 é necessário)",
        ])],
        "reescrita": ("O valor da elasticidade-" + hl("renda") + " indica se um bem é de luxo ou essencial."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A elasticidade-preço cruzada indica se um bem é complementar ou substituto.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["item adaptado na fonte (FGV, DPE/RS, Analista – Área de Apoio Especializado, Economia, "
                    "2023, adaptada)"],
    },
    # ------------------------------------------------------------------ E2-L01377
    {
        "id": "ECO-E2-L01377-1", "fonte_ref": "E2-L01377", "destino": "02", "subtema": H2["cruz"],
        "tipo": "ME", "banca": "Intensivo MM", "prova": "Intensivo Pré-TPS/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": "Leia o enunciado a seguir e assinale a opção correta.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Questão",
        "assertiva": ("Um consumidor recebe a renda mensal de 100 unidades monetárias (u.m.) e decide gastá-la "
                      "comprando 2 bens, X e Y. Gasta mensalmente 70 u.m. com X e 30 u.m. com Y. A partir de certo "
                      "mês, sua renda aumenta em 10 u.m., mas os preços de X e Y não se alteram. Em consequência, o "
                      "consumidor aumenta em 7 u.m. seus gastos com X e em 3 u.m. seus gastos com Y. Essas "
                      "informações indicam que a elasticidade-renda da demanda do consumidor por X é igual a"
                      "</p><p>(A) 10%</p><p>(B) 7/10 = 0,7</p><p>(C) zero</p><p>(D) 1</p><p>(E) 7 u.m."),
        "gabarito": "D", "gabarito_origem": "fonte", "status": "normal",
        "anotada": ("❌ " + az("(A) ") + vm("10%") + "</p><p>❌ " + az("(B) ") + vm("7/10 = 0,7")
                    + "</p><p>❌ " + az("(C) ") + vm("zero") + "</p><p>✅ " + az("(D) 1")
                    + "</p><p>❌ " + az("(E) ") + vm("7 u.m.")),
        "poucas": ("A renda subiu " + vd("10%") + " (100 → 110) e o gasto com X também " + vd("10%")
                   + " (70 → 77); com preço constante, a quantidade de X subiu 10%. " + azb("ε<sub>R</sub>")
                   + " = 10% ÷ 10% = " + vd("1") + "."),
        "destrinchando": [
            azb("Elasticidade-renda da demanda") + " = %Δq ÷ %ΔR. Ela é <b>adimensional</b> (razão entre duas "
            "variações percentuais) — não se mede em u.m. nem em %.",
            "Truque do enunciado: ele dá gastos, não quantidades. Mas, com p<sub>X</sub> constante, gasto = "
            "p × q varia na mesma proporção de q: %Δq<sub>X</sub> = %Δgasto<sub>X</sub> = 7/70 = " + vd("10%")
            + ".",
            "(A) ❌ 10% é a variação da renda (ou da quantidade), não a razão entre elas.",
            "(B) ❌ 7/10 = 0,7 é a " + azb("propensão marginal a gastar") + " em X (quanto de cada u.m. extra "
            "vai para X): ΔGasto/ΔR, em valores absolutos. Elasticidade compara variações <b>percentuais</b>.",
            "(C) ❌ Zero exigiria que o consumo de X não reagisse à renda.",
            "(D) ✅ ε<sub>R</sub> = 10% ÷ 10% = 1: elasticidade-renda unitária. Consequência: a fatia de X no "
            "orçamento fica constante (70% antes, 77/110 = 70% depois). O mesmo vale para Y (3/30 = 10%).",
            "(E) ❌ 7 u.m. é a variação absoluta do gasto, não uma elasticidade.",
            "Conferência útil: a média das elasticidades-renda ponderada pelas fatias do orçamento é sempre "
            + vd("1") + " (" + azb("agregação de Engel") + "): 0,7 × 1 + 0,3 × 1 = 1. Se um bem tiver "
            "ε<sub>R</sub> > 1 (luxo), outro precisa ter ε<sub>R</sub> < 1.",
        ],
        "dissecando": (cz("[troca de conceito · dado alterado]") + " Os distratores são as contas “quase certas”: "
                       "a razão de valores absolutos (0,7), a variação percentual isolada (10%) e a variação "
                       "absoluta (7 u.m.). Quem sabe que elasticidade é razão de <b>percentuais</b> elimina três "
                       "de cara."),
        "modulos": [("😈 Para dificultar", [
            "<i>Se, com o mesmo aumento de renda, o gasto com X subisse 14 u.m., a elasticidade-renda de X seria "
            "2, e X seria bem de luxo.</i> → CERTO (14/70 = 20%; 20% ÷ 10% = 2)",
            "<i>Com elasticidade-renda unitária, a participação de X no orçamento aumenta quando a renda "
            "sobe.</i> → ERRADO (fica constante)",
        ])],
        "tipo_erro": ["TROCA_CONCEITO", "DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Renda sobe 10% (100 → 110); gastos com X e Y sobem 10%; com preços constantes, "
                             "%ΔQ = 10%; elasticidade-renda = 1 (letra D). Tabela de classificação de bens pela "
                             "elasticidade-renda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 251", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto (enunciado e alternativas transcritos integralmente no verso da fonte)"},
                          {"ref": "IMAGEM 252", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_reconstruido: a frente era imagem com transcrição truncada; enunciado e alternativas "
                    "copiados da transcrição integral que o verso da fonte traz (alternativa B normalizada de "
                    "“07/10” para “7/10”)"],
    },
    # ------------------------------------------------------------------ E2-L01380
    {
        "id": "ECO-E2-L01380-1", "fonte_ref": "E2-L01380", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "FGV", "prova": "BADESC/Economista/2010", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às elasticidades da demanda.",
        "rotulo_item": "Item",
        "assertiva": "Para bens complementares, a elasticidade-preço cruzada da demanda é negativa.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para bens complementares, a elasticidade-preço cruzada da demanda é <u>negativa</u>."),
        "poucas": ("Complementares são consumidos juntos: se p<sub>Y</sub> sobe, cai a demanda por X. Sinais "
                   "opostos → " + vd("ε<sub>XY</sub> < 0") + "."),
        "destrinchando": [
            azb("Elasticidade-preço cruzada") + ": ε<sub>XY</sub> = %Δq<sub>X</sub> / %Δp<sub>Y</sub>. O sinal "
            "classifica a relação: " + vd("> 0") + " substitutos; " + vd("< 0") + " complementares; "
            + vd("= 0") + " independentes.",
            "Exemplos de complementares: carro × gasolina, impressora × cartucho, café × açúcar. Se a gasolina "
            "encarece, o “pacote” carro + gasolina fica mais caro e a demanda por carros cai.",
            "Sobre os " + azb("complementares perfeitos") + " (Leontief, consumo em proporção fixa, como pé "
            "esquerdo × pé direito do sapato): não há efeito substituição — a elasticidade cruzada "
            "<b>compensada</b> (de Hicks) é zero —, mas a elasticidade cruzada comum (marshalliana) continua "
            "negativa, porque o aumento de p<sub>Y</sub> reduz o poder de compra do pacote.",
            "Detalhe de nível avançado: elasticidades cruzadas brutas <b>não são simétricas</b>. ε<sub>XY</sub> "
            "e ε<sub>YX</sub> podem ter valores — e, por efeito renda, até sinais — diferentes; por isso a "
            "classificação rigorosa de substitutos/complementares líquidos usa a demanda compensada.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, sem modulador. O risco é a inversão "
                       "mental dos sinais (substituto ↔ complementar). Teste: “consumidos juntos → caem juntos → "
                       "sinal negativo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para bens substitutos, a elasticidade-preço cruzada da demanda é negativa.”</i> → ERRADO (sinal "
            "trocado: é positiva)",
            "<i>“Se a elasticidade cruzada de X em relação a Y é −0,5, a de Y em relação a X também é "
            "necessariamente −0,5.”</i> → ERRADO (elasticidades cruzadas não são simétricas)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Atenção: não se trata de complementares perfeitos, e sim de complementares.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 253", "tipo_fonte": "DECORATIVA", "lado": "verso",
                           "acao": "cortada (foto ilustrativa de café com bolinho)"}],
        "alertas": ["item adaptado na fonte (FGV, BADESC, Economista, 2010, adaptada)"],
    },
    # ------------------------------------------------------------------ E2-L01688
    {
        "id": "ECO-E2-L01688-1", "fonte_ref": "E2-L01688", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": "Acerca dos conceitos e teorias da microeconomia, julgue os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": "Se a elasticidade cruzada entre dois bens é negativa, estes bens são substitutos.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a elasticidade cruzada entre dois bens é negativa, estes bens são ") + vm("substitutos")
                   + az("."),
        "poucas": ("Elasticidade cruzada " + vd("negativa") + " = " + azb("complementares") + " (o preço de um "
                   "sobe, a demanda do outro cai). Substitutos têm cruzada " + vd("positiva") + "."),
        "destrinchando": [
            "ε<sub>XY</sub> = %Δq<sub>X</sub> / %Δp<sub>Y</sub>. Sinal negativo significa que p<sub>Y</sub> e "
            "q<sub>X</sub> andam em sentidos opostos: Y encarece e o consumo de X cai — os bens são consumidos "
            "<b>juntos</b> (pão × manteiga, impressora × cartucho).",
            "Substitutos competem pela mesma necessidade (café × chá, manteiga × margarina): se o chá encarece, "
            "parte do consumo migra para o café, e q<sub>café</sub> sobe — sinal " + vd("positivo") + ".",
            "Visto no gráfico de X: o preço de Y é <b>deslocador</b> da demanda de X. Complementar encarecendo → "
            "D<sub>X</sub> para a esquerda; substituto encarecendo → D<sub>X</sub> para a direita.",
            "Magnitude também informa: cruzada alta e positiva = substitutos próximos (mercados concorrentes); "
            "perto de zero = bens praticamente independentes.",
            vm("Regra-âncora: cruzada + → substitutos; cruzada − → complementares."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca o rótulo da relação mantendo o sinal. É o erro mais "
                       "frequente do tema. 🔥 O mesmo ponto, com os dois sinais invertidos de uma vez, caiu no "
                       "CEBRASPE (TJ/PA/2025)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade cruzada entre dois bens é positiva, eles são substitutos.”</i> → CERTO",
            "<i>“Se a elasticidade cruzada entre dois bens é nula, eles são complementares perfeitos.”</i> → "
            "ERRADO (nula = independentes)",
        ])],
        "reescrita": ("Se a elasticidade cruzada entre dois bens é negativa, estes bens são "
                      + hl("complementares") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Cruzada negativa indica complementares (café e açúcar; pão e manteiga; impressora e "
                             "cartucho); substitutos têm cruzada positiva (café e chá). Um dos comentários afirma, "
                             "por engano, que o gabarito estaria incorreto."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 491", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (esquema da fórmula da elasticidade cruzada)"}],
        "alertas": ["qualidade_fonte: um dos comentários empilhados diz que “este gabarito está incorreto”, em "
                    "contradição com a própria explicação; o gabarito ERRADO está correto"],
    },
]
