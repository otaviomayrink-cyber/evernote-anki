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
        "alertas": ["nota_redacao: item adaptado na fonte (FGV, DPE/RS, Analista – Área de Apoio Especializado, Economia, "
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
        "alertas": ["nota_redacao: item adaptado na fonte (FGV, BADESC, Economista, 2010, adaptada)"],
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
    # ------------------------------------------------------------------ E2-L01762
    {
        "id": "ECO-E2-L01762-1", "fonte_ref": "E2-L01762", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("A teoria da firma permite analisar a relação entre os custos de produção e as estruturas de "
                    "mercado. A respeito desse tema, julgue as afirmações a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Pode-se dizer que a introdução da lei dos medicamentos genéricos no Brasil, ao ampliar o "
                      "número de produtos substitutos à disposição dos consumidores neste mercado, promoveu uma "
                      "redução da elasticidade-preço da demanda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Pode-se dizer que a introdução da lei dos medicamentos genéricos no Brasil, ao ampliar o "
                      "número de produtos substitutos à disposição dos consumidores neste mercado, promoveu ")
                   + vm("uma redução") + az(" da elasticidade-preço da demanda."),
        "poucas": ("Mais " + azb("substitutos") + " = consumidor com mais rotas de fuga quando o preço sobe = "
                   "demanda " + vd("mais elástica") + ". O item inverte o sentido."),
        "destrinchando": [
            "O principal determinante da " + azb("elasticidade-preço da demanda") + " é a disponibilidade de "
            "substitutos próximos. Se o remédio de marca encarece e existe um genérico com o mesmo princípio "
            "ativo, o consumidor troca de produto: a quantidade demandada da marca cai muito.",
            rx("Brasil") + ": a " + vd("Lei nº 9.787/1999") + " (Lei dos Genéricos) criou o medicamento "
            "genérico, intercambiável com o de referência e vendido mais barato. O efeito econômico foi "
            "justamente aumentar a sensibilidade da demanda de cada marca ao preço e disciplinar os preços dos "
            "laboratórios.",
            "Nuance útil: o que fica mais elástico é a demanda dirigida a <b>cada produto</b> (a marca de "
            "referência). A demanda pelo <b>tratamento</b> em si (o princípio ativo, como categoria) continua "
            "pouco elástica — quem precisa do remédio não deixa de tomá-lo. Elasticidade depende de como se "
            "define o mercado.",
            "Ligação com poder de mercado: demanda mais elástica → menor margem sobre o custo (índice de "
            + oc("Lerner") + ": (p − CMg)/p = 1/|ε|). Genéricos reduziram o poder de preço das marcas.",
            vm("Regra-âncora: mais substitutos → demanda mais elástica → menos poder de preço."),
        ],
        "dissecando": (cz("[inversão]") + " Premissa verdadeira (genéricos ampliaram os substitutos) e "
                       "conclusão invertida (redução da elasticidade). O “ao ampliar…” é a pista que entrega o "
                       "gabarito: substituto a mais só pode <b>aumentar</b> a elasticidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A entrada dos genéricos tornou mais elástica a demanda pelos medicamentos de referência, "
            "reduzindo o poder de mercado de seus fabricantes.”</i> → CERTO",
            "<i>“Ao ampliar os substitutos, os genéricos tornaram perfeitamente elástica a demanda por "
            "medicamentos.”</i> → ERRADO (modulador absoluto: mais elástica não é infinitamente elástica)",
        ])],
        "reescrita": ("Pode-se dizer que a introdução da lei dos medicamentos genéricos no Brasil, ao ampliar o "
                      "número de produtos substitutos à disposição dos consumidores neste mercado, promoveu "
                      + hl("um aumento") + " da elasticidade-preço da demanda."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["pode-se dizer"], "dificuldade": 1,
        "comentario_fonte": ("Genéricos ampliaram os substitutos; mais substitutos tornam o consumidor mais "
                             "sensível ao preço e aumentam a elasticidade-preço da demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00012
    {
        "id": "ECO-E3-L00012-1", "fonte_ref": "E3-L00012", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("Julgue os itens a seguir, a respeito de determinação das curvas de procura, elasticidade, "
                    "produtividade e custos de produção."),
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-preço cruzada da demanda é negativa para bens substitutos e positiva para "
                      "bens complementares."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elasticidade-preço cruzada da demanda é ") + vm("negativa") + az(" para bens substitutos "
                                                                                          "e ") + vm("positiva")
                   + az(" para bens complementares."),
        "poucas": ("Sinais invertidos: " + azb("substitutos") + " → cruzada " + vd("positiva") + "; "
                   + azb("complementares") + " → cruzada " + vd("negativa") + "."),
        "destrinchando": [
            "ε<sub>XY</sub> = %Δq<sub>X</sub> / %Δp<sub>Y</sub>. Substitutos (carne bovina × frango): o boi "
            "encarece 10%, o consumo de frango sobe, digamos, 4% → ε = +0,4. Complementares (carro × "
            "gasolina): a gasolina encarece 10%, a venda de carros cai 2% → ε = −0,2.",
            "Bens " + azb("independentes") + " (sal × sapato) têm cruzada próxima de zero.",
            "Uso prático: a cruzada é a ferramenta para delimitar o " + azb("mercado relevante") + " em defesa "
            "da concorrência. O " + rx("CADE") + " pergunta se, diante de um pequeno aumento de preço "
            "(teste do monopolista hipotético), os consumidores migrariam para outro produto — se sim, os dois "
            "estão no mesmo mercado.",
            "Atenção ao objeto: a cruzada fala de <b>dois</b> bens; a elasticidade-preço própria e a "
            "elasticidade-renda falam de um bem só.",
            vm("Regra-âncora: substituto sobe junto (+); complementar cai junto (−)."),
        ],
        "dissecando": (cz("[inversão]") + " Os dois sinais trocados ao mesmo tempo deixam a frase "
                       "internamente coerente, o que engana quem lê rápido. Basta checar <b>um</b> dos pares "
                       "com um exemplo concreto para derrubar o item. 🔥 Variante do mesmo ponto em simulados: "
                       "“cruzada negativa → substitutos” (só um rótulo trocado)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-preço cruzada da demanda é positiva para bens substitutos e negativa para bens "
            "complementares.”</i> → CERTO",
            "<i>“A elasticidade-preço cruzada negativa indica que os bens são inferiores.”</i> → ERRADO (troca "
            "de conceito: bem inferior se mede pela elasticidade-renda)",
        ])],
        "reescrita": ("A elasticidade-preço cruzada da demanda é " + hl("positiva") + " para bens substitutos e "
                      + hl("negativa") + " para bens complementares."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Seis comentários concordantes: a assertiva inverte os sinais; substitutos têm "
                             "cruzada positiva e complementares, negativa (carne × frango; carro × gasolina)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00234
    {
        "id": "ECO-E3-L00234-1", "fonte_ref": "E3-L00234", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_NIDI_MAR25,
        "rotulo_item": "Item",
        "assertiva": ("O sinal esperado da elasticidade-renda da demanda depende do tipo de bem que está sendo "
                      "avaliado. Sendo assim, espera-se que, na avaliação de um bem normal, a elasticidade-renda "
                      "da demanda apresente sinal positivo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O sinal esperado da elasticidade-renda da demanda depende do tipo de bem que está sendo "
                      "avaliado. Sendo assim, espera-se que, na avaliação de um bem <u>normal</u>, a "
                      "elasticidade-renda da demanda apresente sinal <u>positivo</u>."),
        "poucas": ("Bem " + azb("normal") + " é, por definição, aquele cujo consumo sobe quando a renda sobe: "
                   "renda e quantidade no mesmo sentido → " + vd("ε<sub>R</sub> > 0") + "."),
        "destrinchando": [
            azb("Elasticidade-renda") + ": ε<sub>R</sub> = %Δq / %ΔR. A classificação sai do sinal e do tamanho:",
            vd("ε<sub>R</sub> < 0") + " → " + azb("bem inferior") + " (a renda sobe e o consumo cai: ônibus "
            "lotado trocado por carro, carne de segunda trocada por cortes nobres).",
            vd("ε<sub>R</sub> > 0") + " → " + azb("bem normal") + ", que se subdivide em " + azb("necessário")
            + " (0 < ε<sub>R</sub> < 1: consumo cresce menos que a renda — alimentos básicos) e "
            + azb("de luxo/superior") + " (ε<sub>R</sub> > 1: cresce mais que a renda — viagens internacionais).",
            "Ser inferior não é atributo físico do bem, mas da relação com a renda <b>de quem consome</b> e da "
            "faixa de renda: o mesmo bem pode ser normal para famílias pobres e inferior para as ricas.",
            "Não confundir com o " + azb("bem de Giffen") + ": todo Giffen é inferior (efeito renda negativo e "
            "forte o bastante para vencer o efeito substituição), mas quase nenhum inferior é Giffen.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. A primeira frase (“depende do tipo de bem”) "
                       "prepara o terreno e é verdadeira; o “espera-se” suaviza, mas para bem normal o sinal "
                       "positivo é definicional. Risco: confundir normal com necessário e achar que o sinal "
                       "dependeria de |ε| > 1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…na avaliação de um bem normal, a elasticidade-renda da demanda é necessariamente maior que "
            "1.”</i> → ERRADO (só no bem de luxo; necessário fica entre 0 e 1)",
            "<i>“Na avaliação de um bem inferior, espera-se elasticidade-renda negativa.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["espera-se"], "dificuldade": 1,
        "comentario_fonte": ("Bem normal: renda e consumo crescem juntos, sinal positivo; inferior: sinal "
                             "negativo; necessário 0 < ε < 1; luxo ε > 1."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00235
    {
        "id": "ECO-E3-L00235-1", "fonte_ref": "E3-L00235", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_NIDI_MAR25,
        "rotulo_item": "Item",
        "assertiva": ("Quanto menor for a elasticidade-preço cruzada da demanda entre um bem e seu substituto, "
                      "maior será a capacidade da empresa ofertante deste bem controlar o preço prevalecente no "
                      "mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto <u>menor</u> for a elasticidade-preço cruzada da demanda entre um bem e seu "
                      "substituto, <u>maior</u> será a capacidade da empresa ofertante deste bem controlar o preço "
                      "prevalecente no mercado."),
        "poucas": ("Cruzada baixa = o substituto é <b>distante</b>: quando a empresa sobe o preço, o consumidor "
                   "não migra. Isso é " + azb("poder de mercado") + "."),
        "destrinchando": [
            "A cruzada mede o grau de substituibilidade. Cruzada alta (substitutos próximos, como duas marcas de "
            "açúcar refinado): um aumento de preço de uma desvia a clientela para a outra — a empresa é quase "
            "tomadora de preço. Cruzada baixa: a clientela fica, e a empresa pode elevar o preço sem grande "
            "perda de vendas.",
            "Elo com a elasticidade própria: sem substitutos próximos, a demanda dirigida à empresa é menos "
            "elástica. E o " + azb("índice de Lerner") + " (" + oc("Abba Lerner") + ") liga as duas coisas: "
            + vd("(p − CMg)/p = 1/|ε|") + " — quanto menos elástica a demanda da firma, maior a margem.",
            "Por isso as empresas investem em " + azb("diferenciação") + " (marca, design, ecossistema "
            "fechado): reduzir a substituibilidade percebida é ganhar poder de preço — a lógica da concorrência "
            "monopolística de " + oc("Chamberlin") + ".",
            "Em defesa da concorrência, cruzadas altas entre produtos indicam que estão no mesmo "
            + azb("mercado relevante") + "; cruzadas baixas, que a empresa pode ter posição dominante no seu "
            "nicho.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " A relação é inversa (menor cruzada → maior "
                       "controle), e itens com “quanto menor… maior…” costumam ser montados para pegar quem "
                       "espera relação direta. Raciocine pelo extremo: cruzada zero = nenhum substituto de "
                       "verdade = monopólio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior for a elasticidade-preço cruzada entre um bem e seu substituto, maior será o poder "
            "de mercado da empresa ofertante.”</i> → ERRADO (inversão)",
            "<i>“Em concorrência perfeita, a elasticidade cruzada entre os produtos das diferentes firmas tende "
            "ao infinito.”</i> → CERTO (produtos homogêneos: substitutos perfeitos)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["quanto menor", "maior"],
        "dificuldade": 2,
        "comentario_fonte": ("Cruzada baixa: consumidor não migra para o substituto; empresa tem mais poder de "
                             "mercado (marcas diferenciadas). Um dos comentários marca ERRADO, mas a explicação e a "
                             "reescrita dele confirmam o item."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: um dos comentários empilhados diz ERRADO, mas a própria justificativa "
                    "dele sustenta o CERTO; mantido o gabarito da fonte"],
    },
    # ------------------------------------------------------------------ E3-L00272
    {
        "id": "ECO-E3-L00272-1", "fonte_ref": "E3-L00272", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": True,
        "comando": ("Segundo a teoria microeconômica e os seus axiomas da racionalidade, julgue o item a seguir, "
                    "relativo ao comportamento do consumidor."),
        "rotulo_item": "Item",
        "assertiva": ("Ao se deparar com a redução de preço do quilo de arroz, o consumidor percebe que realiza "
                      "uma economia de gastos em relação à quantidade que usualmente comprava ao preço inicial. Se "
                      "esse consumidor decide usar parte dessa economia para comprar mais unidades desse bem, mas "
                      "também aproveita outra parte dela para comprar outros bens para sua cesta básica de "
                      "alimentação, então, para esse consumidor, a demanda por arroz é preço-elástica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ao se deparar com a redução de preço do quilo de arroz, […] Se esse consumidor decide usar "
                      "parte dessa economia para comprar mais unidades desse bem, mas também aproveita outra parte "
                      "dela para comprar outros bens […], então, para esse consumidor, a demanda por arroz é ")
                   + vm("preço-elástica") + az("."),
        "poucas": ("Se só <b>parte</b> da economia volta para o arroz, o " + azb("gasto com arroz cai") + " "
                   "quando o preço cai. Gasto e preço no mesmo sentido = demanda " + vd("inelástica") + "."),
        "destrinchando": [
            "Conta do gasto. Antes: p₀q₀. A queda do preço gera a economia (p₀ − p₁)q₀. O consumidor devolve ao "
            "arroz só uma parte dela: p₁(q₁ − q₀) < (p₀ − p₁)q₀. Rearranjando: " + vd("p₁q₁ < p₀q₀") + " — o "
            "gasto com arroz <b>diminuiu</b>.",
            "Pela relação elasticidade × gasto: preço cai e gasto cai ⇔ a quantidade subiu proporcionalmente "
            "<b>menos</b> que a queda do preço ⇔ " + azb("|ε| < 1") + ". Se toda a economia (ou mais) voltasse "
            "para o arroz, o gasto ficaria igual (|ε| = 1) ou subiria (|ε| > 1).",
            "Exemplo numérico: arroz a R$ 2 o quilo, 10 kg (gasto " + vd("R$ 20") + "). O preço cai 20%, para "
            "R$ 1,60: economia de R$ 4. Metade (R$ 2) vai para mais arroz → 1,25 kg a mais → 11,25 kg (+12,5%). "
            "Gasto novo: " + vd("R$ 18") + ". ε ≈ 12,5% ÷ 20% = " + vd("0,625") + " → inelástica.",
            "O enunciado descreve também um " + azb("efeito renda") + " (a queda do preço aumenta o poder de "
            "compra e parte dele vai para outros bens). Isso não impede a conclusão: o que decide é para onde vai "
            "a economia, e ela foi repartida.",
            vm("Regra-âncora: preço ↓ e gasto ↓ → inelástica; preço ↓ e gasto ↑ → elástica."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item narra uma situação que caracteriza demanda "
                       "inelástica e conclui “elástica”. A narrativa longa (economia, cesta básica) disfarça um "
                       "teste simples de gasto. Pista: “<b>parte</b> dessa economia” — é o que garante que o gasto "
                       "com arroz caiu."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se o consumidor gastasse toda a economia, e ainda mais, em arroz, sua demanda por arroz seria "
            "preço-elástica.”</i> → CERTO",
            "<i>“…se o consumidor gastasse exatamente toda a economia em arroz, a demanda seria "
            "preço-inelástica.”</i> → ERRADO (gasto constante: elasticidade unitária)",
        ])],
        "reescrita": ("Ao se deparar com a redução de preço do quilo de arroz, […] então, para esse consumidor, a "
                      "demanda por arroz é " + hl("preço-inelástica") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["parte"], "dificuldade": 3,
        "comentario_fonte": ("Professora: é preço-inelástica — a economia é usada só em parte para mais arroz, "
                             "aumento do consumo menos que proporcional à queda do preço (exemplo 20 + 80 = 100 → "
                             "15 + 85 = 100). Comentários de IA divergem: alguns dizem que a elasticidade não "
                             "poderia ser determinada pelo enunciado."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 377", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 378", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["qualidade_fonte: parte dos comentários empilhados afirma que o enunciado não permitiria "
                    "determinar a elasticidade; está errado — se só parte da economia volta ao arroz, o gasto "
                    "com arroz cai, logo |ε| < 1",
                    "texto_parcial: comando truncado na fonte (“os indivíduos buscam m…”): completado de forma neutra"],
    },
    # ------------------------------------------------------------------ E3-L00452
    {
        "id": "ECO-E3-L00452-1", "fonte_ref": "E3-L00452", "destino": "02", "subtema": H2["of"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Com base na teoria microeconômica, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("Se a oferta de um bem tiver elasticidade zero em relação ao preço, a demanda determinará "
                      "unicamente o preço de equilíbrio da transação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a oferta de um bem tiver elasticidade zero em relação ao preço, a demanda determinará "
                      "<u>unicamente</u> o preço de equilíbrio da transação."),
        "poucas": ("Oferta com " + vd("ε = 0") + " é " + azb("vertical") + ": a quantidade está fixada. Onde a "
                   "demanda cortar essa vertical, ali estará o preço — a demanda o determina sozinha."),
        "destrinchando": [
            "Oferta " + azb("perfeitamente inelástica") + ": a quantidade ofertada não reage ao preço (um quadro "
            "de Leonardo, os lugares de um estádio num dia de jogo, a terra numa localização específica, no curto "
            "prazo a safra já colhida).",
            "Divisão de tarefas no equilíbrio: a oferta fixa a <b>quantidade</b>; a demanda, ao se posicionar, "
            "fixa o <b>preço</b>. Deslocamentos da demanda mexem só no preço; a quantidade não muda.",
            "Leitura do “unicamente”: refere-se ao preço. Dada a quantidade, nenhuma condição de custo do "
            "ofertante interfere — o preço é o que os consumidores se dispõem a pagar por aquela quantidade.",
            "Aplicações: (1) " + azb("renda da terra") + " — " + oc("David Ricardo") + ": o trigo não é caro "
            "porque se paga renda; paga-se renda porque o trigo é caro; (2) " + azb("tributação") + ": imposto "
            "sobre bem de oferta vertical recai inteiro sobre o ofertante e não gera peso morto (a quantidade "
            "não muda) — base da proposta de imposto único sobre a terra de " + oc("Henry George") + ".",
            "Espelho: oferta " + azb("perfeitamente elástica") + " (horizontal) faz o contrário — fixa o preço, "
            "e a demanda determina só a quantidade.",
        ],
        "grafico_verso": "ECO-E3-L00452-1-V1",
        "dissecando": (cz("[detalhe · contraintuitivo]") + " O “unicamente” parece modulador absoluto e induz "
                       "o candidato a marcar ERRADO por reflexo; aqui ele é verdadeiro, porque a oferta vertical "
                       "não tem papel nenhum na formação do preço. Lição: modulador absoluto não é erro "
                       "automático — teste-o no caso extremo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a oferta tiver elasticidade zero, um aumento da demanda elevará o preço e a quantidade "
            "transacionada.”</i> → ERRADO (a quantidade não muda)",
            "<i>“Se a oferta for perfeitamente elástica, a demanda determinará unicamente a quantidade "
            "transacionada.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["unicamente"], "dificuldade": 2,
        "comentario_fonte": ("Gabarito preliminar CERTO. Oferta com elasticidade zero é vertical; quantidade "
                             "fixa; deslocamentos da demanda alteram só o preço (obras de arte, estádio, terra)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 655", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00452-1-V1)"}],
        "alertas": ["nota_redacao: gabarito preliminar — a fonte indica “gabarito preliminar: CERTO”"],
    },
    # ------------------------------------------------------------------ E1-0005
    {
        "id": "ECO-E1-0005-1", "fonte_ref": "E1-0005", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2010", "ano": 2010, "cacd": False,
        "errei": True,
        "comando": "Acerca da intervenção do governo em mercados agrícolas, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("A fixação de um preço mínimo para determinado produto agrícola resulta em excedentes "
                      "agrícolas, que serão tanto mais elevados quanto mais inelástica for a curva de oferta de "
                      "mercado do produto beneficiado por esse tipo de política."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A fixação de um preço mínimo para determinado produto agrícola resulta em excedentes "
                      "agrícolas, que serão tanto mais elevados quanto mais ") + vm("inelástica")
                   + az(" for a curva de oferta de mercado do produto beneficiado por esse tipo de política."),
        "poucas": ("O excedente é a distância entre o que se oferta e o que se demanda ao preço mínimo. Quanto "
                   "mais " + azb("elástica") + " a oferta, mais os produtores expandem a produção em resposta ao "
                   "preço alto — e " + vd("maior") + " o excedente."),
        "destrinchando": [
            "Um " + azb("preço mínimo") + " só tem efeito (“morde”) se fixado <b>acima</b> do equilíbrio. Ali, a "
            "quantidade demandada cai (o consumidor compra menos) e a ofertada sobe (o produtor quer vender "
            "mais): " + vd("excedente = Qˢ − Qᴰ") + ".",
            "Os dois lados contribuem: o excedente é tanto maior quanto mais elásticas forem a oferta (expansão "
            "da produção) e a demanda (retração do consumo). Com oferta perfeitamente inelástica (vertical), a "
            "produção nem reagiria ao preço — o excedente viria só da retração da demanda.",
            "No exemplo do gráfico, com a mesma demanda e o mesmo preço mínimo (7 > 5 de equilíbrio), a demanda "
            "cai para 4; a oferta mais elástica leva a produção a " + vd("10") + " (excedente de 6), a menos "
            "elástica, a " + vd("8") + " (excedente de 4).",
            "Para o preço se sustentar, alguém precisa absorver o excedente — em regra o governo, que compra e "
            "estoca. " + rx("Brasil") + ": a " + azb("Política de Garantia de Preços Mínimos (PGPM)") + ", "
            "executada pela " + rx("Conab") + " com compras diretas (AGF) e prêmios de escoamento, é o exemplo "
            "clássico.",
            vm("Regra-âncora: excedente de um preço mínimo cresce com as elasticidades — de oferta e de "
               "demanda."),
        ],
        "grafico_verso": "ECO-E1-0005-1-V1",
        "dissecando": (cz("[inversão]") + " Troca “elástica” por “inelástica”. Atenção à palavra "
                       "“excedentes”: aqui é <b>excesso de oferta</b> (sobras físicas), não “excedente do "
                       "produtor” (área de bem-estar) — quem mistura os dois raciocina sobre a coisa errada. "
                       "A primeira oração (“resulta em excedentes”) pressupõe preço mínimo acima do equilíbrio, "
                       "que é o caso relevante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…excedentes que serão tanto mais elevados quanto mais elástica for a curva de demanda do "
            "produto.”</i> → CERTO (o consumo se retrai mais)",
            "<i>“A fixação de um preço mínimo abaixo do preço de equilíbrio gera excedentes agrícolas.”</i> → "
            "ERRADO (piso abaixo do equilíbrio é inócuo)",
        ])],
        "reescrita": ("A fixação de um preço mínimo para determinado produto agrícola resulta em excedentes "
                      "agrícolas, que serão tanto mais elevados quanto mais " + hl("elástica") + " for a curva "
                      "de oferta de mercado do produto beneficiado por esse tipo de política."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tanto mais… quanto mais"], "dificuldade": 2,
        "comentario_fonte": ("Quanto mais inelástica a oferta, menor o excesso de oferta; preço mínimo eficaz fica "
                             "acima do equilíbrio. Gráfico: Qᴰ = 4; Qˢ = 10 com a oferta mais elástica e 8 com a "
                             "menos elástica. Um comentário diz que o preço poderia estar abaixo do equilíbrio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "00021.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0005-1-V1, com os números citados no comentário)"},
                          {"ref": "image (35).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada; conteúdo descrito no comentário)"}],
        "alertas": ["banca_provavel: possível CACD/CEBRASPE 2010; a fonte só traz o ano"],
    },
    # ------------------------------------------------------------------ E1-0090
    {
        "id": "ECO-E1-0090-1", "fonte_ref": "E1-0090", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": True,
        "comando": "Acerca dos efeitos da tributação sobre o bem-estar, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("Tributos mais altos em bens que causam vício, como cigarros e bebidas alcoólicas, têm a "
                      "quase-totalidade de seu efeito sobre o bem-estar do consumidor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Tributos mais altos em bens que causam vício, como cigarros e bebidas alcoólicas, têm a "
                      "<u>quase-totalidade</u> de seu efeito sobre o bem-estar do <u>consumidor</u>."),
        "poucas": ("Vício = " + azb("demanda muito inelástica") + ". O ônus do tributo recai sobre o lado "
                   "<b>menos elástico</b> do mercado: o consumidor."),
        "destrinchando": [
            "Regra da " + azb("incidência econômica") + ": quem paga o imposto não é quem o recolhe, e sim quem "
            "tem menos condição de fugir dele. A parcela do consumidor é aproximadamente "
            + vd("ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|)") + "; a do produtor, "
            "|ε<sub>D</sub>| / (ε<sub>O</sub> + |ε<sub>D</sub>|).",
            "Bens que causam dependência têm |ε<sub>D</sub>| muito baixo: o consumidor continua comprando mesmo "
            "com o preço maior. Com ε<sub>D</sub> perto de zero, a fração do consumidor tende a 1 — o preço "
            "final sobe quase no valor do imposto, e o preço líquido do produtor quase não cai.",
            "Efeito colateral: com demanda inelástica, a quantidade cai pouco, então o " + azb("peso morto")
            + " é pequeno e a arrecadação é alta e estável — por isso esses bens são bases tributárias "
            "preferidas (" + oc("Mankiw") + ", <i>Introdução à Economia</i>, capítulo sobre os custos da "
            "tributação).",
            "Há também a função " + azb("extrafiscal") + ": o tributo encarece o hábito para desestimulá-lo "
            "(lógica de imposto corretivo sobre externalidades e “internalidades” do vício). " + rx("Brasil")
            + ": cigarros e bebidas sempre tiveram IPI elevado e são alvo do Imposto Seletivo criado pela "
            "reforma tributária do consumo (EC 132/2023).",
        ],
        "grafico_verso": "ECO-E1-0090-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item não menciona elasticidade: a banca espera que "
                       "o candidato traduza “vício” em “demanda inelástica”. O “quase-totalidade” é modulador "
                       "<b>relativo</b> — admite que o produtor arca com um pouco —, e por isso o item se "
                       "sustenta. 🔥 Par recorrente: bens viciantes × incidência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…têm a totalidade de seu efeito sobre o bem-estar do consumidor.”</i> → ERRADO (modulador "
            "absoluto: só com demanda perfeitamente inelástica)",
            "<i>“…geram elevado peso morto, pois a quantidade consumida cai muito.”</i> → ERRADO (demanda "
            "inelástica: a quantidade cai pouco)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["quase-totalidade"], "dificuldade": 2,
        "comentario_fonte": ("Bens viciantes têm demanda inelástica; o ônus recai sobre os consumidores (Mankiw); "
                             "função extrafiscal do tributo (Prof. Jetro Coutinho). Gabarito: Certo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "1edabab1-7344-4b7b-ae78-ee575825b656", "tipo_fonte": "GRÁFICO",
                           "lado": "verso", "acao": "redesenhada (ECO-E1-0090-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0093
    {
        "id": "ECO-E1-0093-1", "fonte_ref": "E1-0093", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, acerca de elasticidade, receita total e incidência tributária.",
        "rotulo_item": "Item",
        "assertiva": ("O ônus de um imposto recai mais intensamente no lado do mercado que é mais elástico. Quando "
                      "a demanda é elástica, um aumento de preço leva a uma diminuição proporcionalmente menor da "
                      "quantidade demandada, portanto a Receita Total aumenta. Quando a demanda é inelástica, um "
                      "aumento de preço leva a uma diminuição proporcionalmente maior da quantidade demandada, "
                      "portanto a Receita Total diminui."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O ônus de um imposto recai mais intensamente no lado do mercado que é ")
                   + vm("mais elástico") + az(". Quando a demanda é elástica, um aumento de preço leva a uma "
                                              "diminuição proporcionalmente ") + vm("menor")
                   + az(" da quantidade demandada, portanto a Receita Total ") + vm("aumenta")
                   + az(". Quando a demanda é inelástica, um aumento de preço leva a uma diminuição "
                        "proporcionalmente ") + vm("maior") + az(" da quantidade demandada, portanto a Receita "
                                                                 "Total ") + vm("diminui") + az("."),
        "poucas": ("As três frases estão invertidas: o ônus recai no lado " + azb("menos elástico")
                   + "; na demanda elástica a quantidade cai <b>mais</b> que o preço sobe e a receita "
                   + vd("cai") + "; na inelástica, ao contrário."),
        "destrinchando": [
            azb("Incidência") + ": paga mais quem tem menos alternativas. Se a demanda é rígida, o consumidor "
            "absorve o aumento; se a oferta é rígida, o produtor aceita receber menos. O lado elástico “foge” "
            "(reduz a quantidade) e transfere o ônus ao outro.",
            azb("Elasticidade e receita") + ": |ε| > 1 significa que a quantidade reage <b>mais</b> que "
            "proporcionalmente ao preço. Logo, preço ↑ → quantidade ↓ muito → " + vd("RT ↓") + ". Com "
            "|ε| < 1, a quantidade reage menos que proporcionalmente → preço ↑ → " + vd("RT ↑") + ".",
            "Os dois temas se conectam: o lado que “foge” do imposto é o mesmo cujo gasto cai com o aumento "
            "de preço. Por isso governos tributam pesadamente bens de demanda inelástica (combustíveis, energia, "
            "cigarros): a arrecadação é alta e a base não encolhe.",
            vm("Regra-âncora: imposto e receita seguem a mesma lógica — quem não consegue reagir paga."),
        ],
        "dissecando": (cz("[inversão]") + " Item “espelhado”: cada frase é a versão invertida de uma regra "
                       "correta, e a coerência interna entre elas (“proporcionalmente menor… portanto aumenta”) "
                       "dá falsa segurança. Basta checar a definição de elástica (reação <b>maior</b>) para "
                       "desmontar o conjunto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O ônus de um imposto recai mais intensamente no lado do mercado que é menos elástico.”</i> → "
            "CERTO",
            "<i>“Quando a demanda tem elasticidade unitária, um aumento de preço reduz a receita total.”</i> → "
            "ERRADO (unitária: receita constante)",
        ])],
        "reescrita": ("O ônus de um imposto recai mais intensamente no lado do mercado que é "
                      + hl("menos elástico") + ". Quando a demanda é elástica, um aumento de preço leva a uma "
                      "diminuição proporcionalmente " + hl("maior") + " da quantidade demandada, portanto a "
                      "Receita Total " + hl("diminui") + ". Quando a demanda é inelástica, um aumento de preço "
                      "leva a uma diminuição proporcionalmente " + hl("menor") + " da quantidade demandada, "
                      "portanto a Receita Total " + hl("aumenta") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas “ERRADO”, uma imagem não preservada e o link do canal (t.me/cacdeconomia/100).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (40).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada; comentário escrito a partir da teoria)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0094
    {
        "id": "ECO-E1-0094-1", "fonte_ref": "E1-0094", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COM_2023,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento no imposto sobre o consumo de um bem com demanda perfeitamente preço-elástica e "
                      "oferta preço-inelástica terá incidência apenas sobre o bem-estar dos produtores, pois os "
                      "consumidores somente adquirem o bem a um preço único de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento no imposto sobre o consumo de um bem com demanda <u>perfeitamente</u> "
                      "preço-elástica e oferta preço-inelástica terá incidência <u>apenas</u> sobre o bem-estar "
                      "dos produtores, pois os consumidores somente adquirem o bem a um preço único de "
                      "equilíbrio."),
        "poucas": ("Demanda " + azb("perfeitamente elástica") + " é horizontal: os consumidores não aceitam "
                   "pagar um centavo a mais. O preço ao consumidor não muda, e " + vd("todo o imposto") + " sai "
                   "do preço líquido do produtor."),
        "destrinchando": [
            "Pela fórmula de incidência, a parcela do consumidor é ε<sub>O</sub> / (ε<sub>O</sub> + "
            "|ε<sub>D</sub>|). Com " + vd("|ε<sub>D</sub>| → ∞") + ", ela vai a zero, qualquer que seja a "
            "oferta. A oferta inelástica do item só reforça o resultado.",
            "Intuição: há substitutos perfeitos ao preço p₀ (pense numa pequena região que vende a um mercado "
            "maior a preço dado). Se o vendedor tentar repassar o imposto, perde toda a clientela. Resta "
            "aceitar receber " + vd("p₀ − t") + ".",
            "Bem-estar: o " + azb("excedente do consumidor") + " já é nulo com demanda horizontal (todos pagam "
            "exatamente o que valorizam) e continua nulo. A receita do governo e o " + azb("peso morto")
            + " saem inteiros do excedente do produtor.",
            "Espelho: com demanda perfeitamente <b>inelástica</b> (vertical), o imposto recai inteiro sobre o "
            "consumidor e não há peso morto.",
        ],
        "grafico_verso": "ECO-E1-0094-1-V1",
        "dissecando": (cz("[literalidade · exceção]") + " Dois moduladores fortes (“perfeitamente”, “apenas”) "
                       "que, juntos, tornam o item verdadeiro: é o caso-limite da regra de incidência. A "
                       "justificativa final (“preço único de equilíbrio”) é uma forma simples de dizer que a "
                       "demanda é horizontal. Lição: “apenas” só é suspeito quando o caso não é extremo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com demanda preço-elástica (não perfeitamente) e oferta preço-inelástica, o imposto incidirá "
            "apenas sobre os produtores.”</i> → ERRADO (modulador absoluto: os consumidores arcam com uma parte)",
            "<i>“…com demanda perfeitamente preço-elástica, o imposto elevará o preço pago pelo consumidor no "
            "valor integral do tributo.”</i> → ERRADO (inversão: o preço ao consumidor não muda)",
        ])],
        "tipo_erro": ["LITERAL", "EXCECAO"], "moduladores": ["perfeitamente", "apenas", "somente"],
        "dificuldade": 2,
        "comentario_fonte": ("Demanda perfeitamente elástica: qualquer aumento de preço leva ao abandono do "
                             "consumo; com oferta inelástica, todo o peso recai sobre o produtor. Um dos "
                             "comentários afirma, por engano, que a quantidade demandada não muda e que o "
                             "consumidor perde bem-estar."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (42).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (não preservada; conteúdo de incidência absorvido no 📖)"}],
        "alertas": ["qualidade_fonte: um dos comentários confunde demanda perfeitamente elástica com "
                    "perfeitamente inelástica (diz que a quantidade não muda e que o consumidor arca com o "
                    "imposto)",
                    "banca_provavel: possível CACD 2023; a fonte só traz o ano"],
    },
    # ------------------------------------------------------------------ E1-0095
    {
        "id": "ECO-E1-0095-1", "fonte_ref": "E1-0095", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COM_2023,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento no imposto sobre o consumo de um bem cuja demanda e oferta tenham elasticidades "
                      "unitárias incidirá apenas sobre o bem-estar do consumidor, pois as firmas conseguem "
                      "repassar o tributo totalmente no novo preço de equilíbrio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento no imposto sobre o consumo de um bem cuja demanda e oferta tenham elasticidades "
                      "unitárias incidirá ") + vm("apenas sobre o bem-estar do consumidor, pois as firmas "
                                                  "conseguem repassar o tributo totalmente")
                   + az(" no novo preço de equilíbrio."),
        "poucas": ("Elasticidades iguais (em módulo) → " + azb("ônus repartido igualmente") + ": cerca de "
                   + vd("metade") + " do imposto para cada lado. Repasse total exigiria demanda perfeitamente "
                   "inelástica ou oferta perfeitamente elástica."),
        "destrinchando": [
            "Parcela do consumidor ≈ " + vd("ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|)") + ". Com "
            "ε<sub>O</sub> = |ε<sub>D</sub>| = 1: 1 / (1 + 1) = " + vd("½") + ". O preço pago sobe metade do "
            "imposto; o preço recebido cai a outra metade.",
            "Os dois perdem " + azb("excedente") + ": o consumidor paga mais e compra menos; o produtor recebe "
            "menos e vende menos. Além da receita transferida ao governo, surge " + azb("peso morto") + ".",
            "O que importa é a elasticidade <b>relativa</b>, não o valor absoluto: com ε<sub>O</sub> = 3 e "
            "|ε<sub>D</sub>| = 1, o consumidor arca com 3/4; com ε<sub>O</sub> = 1 e |ε<sub>D</sub>| = 3, com "
            "1/4. Repasse integral (100%) só nos extremos: |ε<sub>D</sub>| = 0 ou ε<sub>O</sub> → ∞.",
            "Não confundir “elasticidade unitária” com “sem efeito”: ela só diz que a receita do vendedor "
            "ficaria constante diante de variações de preço ao longo da demanda — nada diz sobre ausência de "
            "ônus.",
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " “Apenas” e “totalmente” transformam uma "
                       "repartição em transferência integral, e a justificativa (“as firmas conseguem repassar”) "
                       "cria um nexo que o dado do item (elasticidades iguais) não autoriza. Pista: curvas "
                       "<b>igualmente</b> elásticas sugerem divisão, não concentração."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com elasticidades unitárias, o ônus do imposto será repartido em partes aproximadamente iguais "
            "entre consumidores e produtores.”</i> → CERTO",
            "<i>“…com elasticidades unitárias, o imposto não altera o bem-estar de consumidores nem de "
            "produtores.”</i> → ERRADO (ambos perdem excedente)",
        ])],
        "reescrita": ("Um aumento no imposto sobre o consumo de um bem cuja demanda e oferta tenham elasticidades "
                      "unitárias incidirá " + hl("sobre o bem-estar de consumidores e de produtores, em partes "
                      "aproximadamente iguais, pois as firmas conseguem repassar apenas cerca de metade do "
                      "tributo") + " no novo preço de equilíbrio."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["apenas", "totalmente"],
        "dificuldade": 2,
        "comentario_fonte": ("Elasticidades idênticas: o peso do imposto é distribuído igualmente entre "
                             "produtores e consumidores. Comentários empilhados trazem erros: um fala em demanda "
                             "“altamente inelástica” (de outro item); outro diz que o imposto não altera o "
                             "bem-estar de ninguém."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (44).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada)"},
                          {"ref": "image (45).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada)"}],
        "alertas": ["qualidade_fonte: dois comentários empilhados estão errados (demanda “altamente "
                    "inelástica”, de outro item; “não altera o bem-estar”); prevaleceu o que divide o ônus "
                    "igualmente",
                    "banca_provavel: possível CACD 2023; a fonte só traz o ano"],
    },
    # ------------------------------------------------------------------ E1-0096
    {
        "id": "ECO-E1-0096-1", "fonte_ref": "E1-0096", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COM_2023,
        "rotulo_item": "Item",
        "assertiva": ("Um imposto sobre o consumo de produtos viciantes tem redução pequena no bem-estar dos "
                      "consumidores, uma vez que a demanda desses produtos é altamente elástica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um imposto sobre o consumo de produtos viciantes tem redução ") + vm("pequena")
                   + az(" no bem-estar dos consumidores, uma vez que a demanda desses produtos é ")
                   + vm("altamente elástica") + az("."),
        "poucas": ("Produto viciante tem demanda " + azb("altamente inelástica") + ": o consumidor não "
                   "consegue reduzir o consumo e absorve a maior parte do imposto — a perda de bem-estar dele "
                   "é " + vd("grande") + "."),
        "destrinchando": [
            "Dependência química e hábito reduzem a sensibilidade ao preço: |ε<sub>D</sub>| pequeno. Pela "
            "regra de incidência, o lado menos elástico paga mais — aqui, o consumidor.",
            "Perda do consumidor = preço mais alto em cada unidade que continua comprando (quase todas) + o "
            "pouco que deixa de consumir. Com demanda inelástica, a primeira parcela domina e é grande.",
            "O que é <b>pequeno</b> nesse caso é outra coisa: o " + azb("peso morto") + ". Como a quantidade "
            "quase não cai, quase todo o excedente perdido pelo consumidor vira " + azb("receita do governo")
            + " (transferência), e pouco se desperdiça. Daí a combinação “boa arrecadação, baixa distorção” "
            "que torna esses bens alvo preferido da tributação.",
            "Lógica do item inteiro invertida: se a demanda fosse altamente elástica, o consumidor escaparia do "
            "imposto trocando de produto — e então, sim, sua perda seria pequena. A frase descreve um bem "
            "comum, não um viciante.",
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " O item atribui a bens viciantes a elasticidade "
                       "oposta à verdadeira e tira dela a conclusão coerente — mas falsa. Vício → "
                       "<b>inelástica</b> é associação automática que a banca testa nos dois sentidos. 🔥 Mesmo "
                       "tema, com gabarito CERTO, em item de 2022 sobre cigarros e bebidas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto sobre o consumo de produtos viciantes gera peso morto relativamente pequeno, uma vez "
            "que a demanda desses produtos é inelástica.”</i> → CERTO",
            "<i>“…tem redução grande no bem-estar dos produtores, pois a demanda é inelástica.”</i> → ERRADO "
            "(troca de ator: o ônus recai sobre os consumidores)",
        ])],
        "reescrita": ("Um imposto sobre o consumo de produtos viciantes tem redução " + hl("grande") + " no "
                      "bem-estar dos consumidores, uma vez que a demanda desses produtos é "
                      + hl("altamente inelástica") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": ["altamente"], "dificuldade": 1,
        "comentario_fonte": ("Reescrita: redução grande no bem-estar dos consumidores, pois a demanda é altamente "
                             "inelástica."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (39).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada)"},
                          {"ref": "image (46).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada)"}],
        "alertas": ["banca_provavel: possível CACD 2023; a fonte só traz o ano"],
    },
    # ------------------------------------------------------------------ E1-0097
    {
        "id": "ECO-E1-0097-1", "fonte_ref": "E1-0097", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COM_2023,
        "rotulo_item": "Item",
        "assertiva": ("Uma redução no imposto sobre o consumo de um bem com demanda preço-inelástica e oferta "
                      "preço-elástica terá incidência maior sobre o bem-estar dos consumidores do que sobre o "
                      "bem-estar das firmas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma <u>redução</u> no imposto sobre o consumo de um bem com demanda preço-inelástica e "
                      "oferta preço-elástica terá incidência <u>maior sobre o bem-estar dos consumidores</u> do "
                      "que sobre o bem-estar das firmas."),
        "poucas": ("A regra de incidência vale nos dois sentidos: o lado " + azb("menos elástico") + " arca com "
                   "a maior parte de um aumento e se apropria da maior parte de uma " + vd("redução") + ". "
                   "Aqui, o consumidor."),
        "destrinchando": [
            "Parcela do consumidor ≈ ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|). Com oferta elástica "
            "(ε<sub>O</sub> grande) e demanda inelástica (|ε<sub>D</sub>| pequeno), a fração é próxima de 1: o "
            "preço ao consumidor cai quase no valor do corte.",
            "Intuição: a oferta elástica significa que as firmas ofertam qualquer quantidade a um preço líquido "
            "praticamente dado (próximo do custo). Quando o imposto cai, a concorrência empurra o preço final para "
            "baixo, e o ganho escoa para quem compra.",
            "Simetria útil: se o mesmo bem tivesse o imposto <b>aumentado</b>, o consumidor arcaria com a maior "
            "parte. Incidência descreve quem absorve a variação, para cima ou para baixo.",
            "Aplicação: em desonerações de bens de demanda inelástica e oferta competitiva (combustíveis, "
            "alimentos básicos), espera-se repasse elevado ao preço final; quando a oferta é inelástica ou "
            "concentrada, parte do corte vira margem das empresas.",
            vm("Regra-âncora: incidência segue a inelasticidade — no aumento e na redução do imposto."),
        ],
        "dissecando": (cz("[contraintuitivo · paráfrase fiel]") + " O item troca o habitual “aumento” por "
                       "“redução” e fala em “incidência” de um benefício, o que causa estranheza; quem lembra "
                       "que a regra é simétrica julga rápido. Os dois dados (demanda inelástica, oferta "
                       "elástica) apontam para o mesmo lado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução no imposto sobre o consumo de um bem com demanda preço-elástica e oferta "
            "preço-inelástica beneficiará principalmente os consumidores.”</i> → ERRADO (inversão: beneficia as "
            "firmas)",
            "<i>“Uma redução de imposto sobre bem de demanda inelástica e oferta elástica será integralmente "
            "apropriada pelas firmas.”</i> → ERRADO (troca de ator e modulador absoluto)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "PARAFRASE_FIEL"], "moduladores": ["maior"], "dificuldade": 2,
        "comentario_fonte": ("Com demanda inelástica, o consumidor mantém o consumo e se beneficia da queda do "
                             "preço; a oferta elástica ajusta a quantidade sem elevar o preço recebido; a "
                             "incidência afeta mais a curva menos elástica."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (43).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada)"},
                          {"ref": "image (41).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não preservada)"}],
        "alertas": ["banca_provavel: possível CACD 2023; a fonte só traz o ano"],
    },
    # ------------------------------------------------------------------ E1-0124
    {
        "id": "ECO-E1-0124-1", "fonte_ref": "E1-0124", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A4,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o primeiro teorema do bem-estar, o mercado sempre leva a alocações eficientes de "
                      "Pareto, mesmo se houver externalidades."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o primeiro teorema do bem-estar, o mercado sempre leva a alocações eficientes de "
                      "Pareto") + vm(", mesmo se houver externalidades") + az("."),
        "poucas": ("O " + azb("1º teorema do bem-estar") + " garante eficiência de Pareto do equilíbrio "
                   "competitivo <b>sob hipóteses</b> — entre elas, a " + vd("ausência de externalidades")
                   + ". Externalidade é falha de mercado."),
        "destrinchando": [
            azb("Primeiro teorema") + ": todo equilíbrio de mercados competitivos é eficiente no sentido de "
            "Pareto. Formalização de " + oc("Arrow") + " e " + oc("Debreu") + " (anos 1950) para a “mão "
            "invisível” de " + oc("Adam Smith") + ".",
            "Hipóteses: mercados completos e competitivos (agentes tomadores de preço), informação perfeita, "
            "preferências não saciadas localmente e <b>nenhuma externalidade nem bem público</b>. Quebrou "
            "uma, quebrou a garantia.",
            "Com " + azb("externalidade") + ", o custo (ou benefício) privado difere do social: a fábrica que "
            "polui não paga o dano e produz demais; quem se vacina não é remunerado pela proteção que dá aos "
            "outros, e há vacinação de menos. O equilíbrio de mercado deixa de ser ótimo.",
            "Correções clássicas: imposto ou subsídio de " + oc("Pigou") + " (internaliza a diferença entre "
            "custo privado e social) e negociação de " + oc("Coase") + " (com direitos de propriedade bem "
            "definidos e custos de transação baixos, as partes chegam ao ótimo).",
            azb("Segundo teorema") + ": qualquer alocação eficiente pode ser alcançada como equilíbrio "
            "competitivo, com redistribuição prévia da renda por transferências lump-sum (exige convexidade).",
        ],
        "dissecando": (cz("[meia-verdade]") + " A primeira parte é o enunciado do teorema (o “sempre” vale dentro de suas "
                       "hipóteses); "
                       "o erro foi enxertado na ressalva final, que anula uma de suas hipóteses. 🔥 Banca adora "
                       "o padrão “teorema + mesmo se houver [falha de mercado]”: externalidade, bem público, "
                       "poder de mercado, informação assimétrica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o primeiro teorema do bem-estar, o equilíbrio competitivo é eficiente de Pareto, desde "
            "que não haja externalidades nem bens públicos.”</i> → CERTO",
            "<i>“O primeiro teorema do bem-estar garante que o equilíbrio competitivo é justo do ponto de vista "
            "distributivo.”</i> → ERRADO (eficiência não é equidade)",
        ])],
        "reescrita": ("Segundo o primeiro teorema do bem-estar, o mercado sempre leva a alocações eficientes de "
                      "Pareto, " + hl("desde que não haja externalidades") + "."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["sempre", "mesmo se"], "dificuldade": 1,
        "comentario_fonte": ("O erro está no final: externalidades são falha de mercado e rompem os pressupostos "
                             "da eficiência de Pareto."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0125
    {
        "id": "ECO-E1-0125-1", "fonte_ref": "E1-0125", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A4,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria do bem-estar, tirar dos pobres para dar aos ricos não gera uma melhora no "
                      "sentido de Pareto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a teoria do bem-estar, tirar dos pobres para dar aos ricos <u>não</u> gera uma "
                      "melhora no sentido de Pareto."),
        "poucas": ("" + azb("Melhoria de Pareto") + " exige melhorar alguém <b>sem piorar ninguém</b>. Tirar de "
                   "um grupo piora esse grupo — não é melhoria de Pareto, em qualquer direção."),
        "destrinchando": [
            "Critério de " + oc("Vilfredo Pareto") + ": uma mudança é " + azb("melhoria de Pareto") + " se "
            "ao menos um agente melhora e nenhum piora. Uma alocação é " + azb("eficiente de Pareto") + " quando "
            "não resta nenhuma melhoria desse tipo.",
            "Transferência pura (tirar de A para dar a B) sempre piora A. Logo, nem “tirar dos pobres para dar "
            "aos ricos” nem “tirar dos ricos para dar aos pobres” é melhoria de Pareto. O critério é "
            + vd("neutro") + " quanto à distribuição.",
            "Consequência: há infinitas alocações eficientes de Pareto, inclusive muito desiguais (um agente "
            "com tudo, os demais com nada, é eficiente). Eficiência não é justiça.",
            "Para comparar mudanças com ganhadores e perdedores, usa-se o critério de " + azb("Kaldor-Hicks")
            + " (melhoria potencial): os ganhadores <b>poderiam</b> compensar os perdedores e ainda ficar "
            "melhor. É a base da análise custo-benefício.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Item verdadeiro por definição. O “pobres → "
                       "ricos” provoca rejeição moral e leva a pensar em julgamento distributivo; mas o critério "
                       "de Pareto nem entra nesse mérito — ele só não aprova transferências."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o critério de Pareto, tirar dos ricos para dar aos pobres gera melhora, pois a utilidade "
            "marginal da renda dos pobres é maior.”</i> → ERRADO (Pareto não compara utilidades entre pessoas)",
            "<i>“Uma alocação em que um único indivíduo detém todos os bens pode ser eficiente de Pareto.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Melhoria de Pareto só se melhora alguém sem piorar ninguém; a transferência piora "
                             "o rico (ou o pobre). O texto da fonte diz, por lapso, “se piorou para alguém, então "
                             "foi uma melhora no sentido de Pareto”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: lapso no comentário de origem (“se piorou pra alguém então foi uma "
                    "melhora”); o correto é “não foi”"],
    },
    # ------------------------------------------------------------------ E1-0126
    {
        "id": "ECO-E1-0126-1", "fonte_ref": "E1-0126", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A4,
        "rotulo_item": "Item",
        "assertiva": ("O imposto traz receita para o governo, mas esta receita não supera a perda de bem-estar de "
                      "consumidores e ofertantes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O imposto traz receita para o governo, mas esta receita <u>não supera</u> a perda de "
                      "bem-estar de consumidores e ofertantes."),
        "poucas": ("Perda de excedentes = " + vd("receita + peso morto") + ". Como o " + azb("peso morto")
                   + " é ≥ 0, a receita nunca supera a perda dos agentes privados."),
        "destrinchando": [
            "Com o imposto t, o consumidor paga pc > p₀ e o produtor recebe pv < p₀; a quantidade cai de q₀ "
            "para qₜ. Perda conjunta de excedentes = faixa entre pc e pv, de 0 até q₀.",
            "Parte dessa faixa (o retângulo " + vd("t × qₜ") + ") vai para o governo: é " + azb("transferência")
            + ", não destruição. O restante — o triângulo entre qₜ e q₀ — não vai para ninguém: são trocas que "
            "geravam valor e deixaram de ocorrer. É o " + azb("peso morto") + " (ou perda de eficiência).",
            "Caso-limite: com oferta ou demanda perfeitamente inelástica, a quantidade não muda e o peso morto "
            "é zero — receita = perda. Mesmo aí a receita <b>não supera</b> a perda; por isso o item se mantém.",
            "O peso morto cresce com as elasticidades e com o quadrado da alíquota (triângulo de "
            + oc("Harberger") + "). Daí a recomendação de bases amplas e alíquotas baixas.",
        ],
        "grafico_verso": "ECO-E1-0126-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " A formulação “não supera” (em vez de “é menor que”) "
                       "deixa o item verdadeiro inclusive nos casos sem peso morto. Variante perigosa: trocar por "
                       "“é sempre inferior” — aí o caso-limite derrubaria o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A receita do imposto é sempre estritamente inferior à perda de excedentes, qualquer que seja a "
            "elasticidade das curvas.”</i> → ERRADO (modulador absoluto: com curva perfeitamente inelástica, são "
            "iguais)",
            "<i>“A receita tributária representa uma perda líquida de bem-estar para a sociedade.”</i> → ERRADO "
            "(é transferência; a perda líquida é o peso morto)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["não supera"], "dificuldade": 1,
        "comentario_fonte": "A receita não supera a perda de bem-estar; é daí que vem o peso morto.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0127
    {
        "id": "ECO-E1-0127-1", "fonte_ref": "E1-0127", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A4,
        "rotulo_item": "Item",
        "assertiva": "O peso morto cresce com o aumento do imposto, mas menos que proporcionalmente.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O peso morto cresce com o aumento do imposto, ") + vm("mas menos que proporcionalmente")
                   + az("."),
        "poucas": ("O peso morto é um triângulo cuja base e altura crescem com t: ele cresce com o "
                   + azb("quadrado") + " do imposto — " + vd("dobrar t quadruplica o peso morto") + "."),
        "destrinchando": [
            "Geometria: altura do triângulo = t (a cunha pc − pv); base = queda da quantidade, que, com curvas "
            "lineares, é proporcional a t. Área = ½ × base × altura ∝ " + vd("t²") + ".",
            "Triângulo de " + oc("Harberger") + ": PM ≈ ½ · t · Δq; como Δq é proporcional a t, PM cresce com "
            "t². Para a mesma alíquota, cresce também com as elasticidades de oferta e de demanda (quanto mais "
            "as quantidades reagem, maior a base do triângulo).",
            "Receita, ao contrário, cresce <b>menos</b> que proporcionalmente (t sobe, mas a base qₜ encolhe) e, "
            "a partir de certo ponto, cai — é a lógica da " + azb("curva de Laffer") + ". Impostos altos "
            "arrecadam relativamente pouco e distorcem muito.",
            "Lição de política tributária: muitas alíquotas baixas sobre bases amplas geram menos peso morto do "
            "que poucas alíquotas altas sobre bases estreitas, para a mesma arrecadação.",
            vm("Regra-âncora: peso morto ∝ t² — mais que proporcional."),
        ],
        "grafico_verso": "ECO-E1-0127-1-V1",
        "dissecando": (cz("[inversão]") + " A 1ª parte (cresce com o imposto) é verdadeira; o erro está na "
                       "forma do crescimento, que é a oposta. O item pode confundir quem pensa na "
                       "<b>receita</b>, que, essa sim, cresce menos que proporcionalmente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Dobrar a alíquota de um imposto quadruplica, aproximadamente, o peso morto.”</i> → CERTO",
            "<i>“Dobrar a alíquota de um imposto dobra a receita tributária.”</i> → ERRADO (a base encolhe: a "
            "receita cresce menos que o dobro)",
        ])],
        "reescrita": ("O peso morto cresce com o aumento do imposto, " + hl("e mais que proporcionalmente (com "
                      "o quadrado da alíquota)") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["menos que proporcionalmente"], "dificuldade": 1,
        "comentario_fonte": "O peso morto cresce “exponencialmente” (mais do que proporcionalmente) com o imposto.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a fonte diz que o peso morto cresce “exponencialmente”; o crescimento é "
                    "quadrático"],
    },
    # ------------------------------------------------------------------ E1-0129
    {
        "id": "ECO-E1-0129-1", "fonte_ref": "E1-0129", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A4,
        "rotulo_item": "Item",
        "assertiva": ("A incidência jurídica do imposto, se é sobre consumidores ou ofertantes, pode mudar o "
                      "resultado da distribuição do ônus do imposto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A incidência jurídica do imposto, se é sobre consumidores ou ofertantes, ") + vm("pode mudar")
                   + az(" o resultado da distribuição do ônus do imposto."),
        "poucas": ("A " + azb("incidência econômica") + " depende só das " + vd("elasticidades") + ". Cobrar do "
                   "comprador ou do vendedor leva ao mesmo pc, ao mesmo pv e à mesma divisão do ônus."),
        "destrinchando": [
            azb("Incidência legal (jurídica)") + ": quem a lei manda recolher. " + azb("Incidência econômica")
            + ": quem efetivamente perde renda. Elas não coincidem, e a segunda não depende da primeira.",
            "No gráfico: imposto sobre o vendedor desloca a oferta para cima em t; imposto sobre o comprador "
            "desloca a demanda para baixo em t. Nos dois casos abre-se a mesma cunha t entre pc e pv, na "
            "mesma quantidade qₜ — resultado idêntico.",
            "Quem paga mais é o lado " + azb("menos elástico") + ": parcela do consumidor ≈ ε<sub>O</sub> / "
            "(ε<sub>O</sub> + |ε<sub>D</sub>|).",
            rx("Brasil") + ": a distinção aparece como " + azb("contribuinte de direito") + " (quem recolhe, "
            "como o comerciante no ICMS) × " + azb("contribuinte de fato") + " (quem suporta o encargo). E na "
            "folha de pagamentos: dividir a contribuição previdenciária entre empregador e empregado, em tese, "
            "não altera quem a suporta.",
            "Ressalva acadêmica: o resultado supõe mercado competitivo, sem custos de cumprimento e com "
            "consumidores atentos ao imposto; evidências de saliência tributária mostram que, na prática, a "
            "forma de cobrança pode influenciar o comportamento.",
        ],
        "dissecando": (cz("[nexo indevido]") + " O “pode” (modulador relativo) costuma salvar itens; aqui não "
                       "salva, porque na teoria padrão a incidência legal <b>não tem</b> efeito algum sobre a "
                       "divisão do ônus. 🔥 Clássico de Mankiw cobrado em toda banca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto cobrado dos compradores e um cobrado dos vendedores são equivalentes quanto à "
            "divisão do ônus.”</i> → CERTO",
            "<i>“O ônus de um imposto recai integralmente sobre quem tem a obrigação legal de recolhê-lo.”</i> → "
            "ERRADO (incidência legal ≠ econômica)",
        ])],
        "reescrita": ("A incidência jurídica do imposto, se é sobre consumidores ou ofertantes, "
                      + hl("não muda") + " o resultado da distribuição do ônus do imposto" + hl(", que depende "
                      "das elasticidades da oferta e da demanda") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Não faz diferença se o imposto é sobre o consumidor ou o vendedor; o que afeta a "
                             "distribuição do ônus é a elasticidade; quem é mais inelástico paga a conta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0130
    {
        "id": "ECO-E1-0130-1", "fonte_ref": "E1-0130", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A5,
        "rotulo_item": "Item",
        "assertiva": ("O governo decide impor um preço máximo para certo medicamento, por julgar que o preço ao "
                      "qual era vendido no equilíbrio de livre mercado era muito alto. Isto terá como resultado um "
                      "excedente de produção deste medicamento no mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O governo decide impor um preço máximo para certo medicamento, por julgar que o preço ao "
                      "qual era vendido no equilíbrio de livre mercado era muito alto. Isto terá como resultado ")
                   + vm("um excedente de produção") + az(" deste medicamento no mercado."),
        "poucas": ("Teto fixado " + azb("abaixo do equilíbrio") + " (o objetivo era baixar o preço): a quantidade "
                   "demandada sobe, a ofertada cai — " + vd("escassez") + " (excesso de demanda), não excedente."),
        "destrinchando": [
            "Primeira pergunta em todo controle de preços: ele está acima ou abaixo do equilíbrio? Aqui, o "
            "governo achou o preço de mercado “muito alto” — logo, o teto é <b>inferior</b> ao equilíbrio e "
            "efetivo.",
            "Ao preço tabelado, os consumidores querem comprar mais e os produtores querem vender menos: "
            + vd("Qᴰ > Qˢ") + ". O mercado não fecha pelo preço e passa a fechar por outros mecanismos: filas, "
            "racionamento, critérios de favorecimento, mercado paralelo (ágio), queda da qualidade.",
            "Bem-estar: transaciona-se só Qˢ (o lado curto do mercado); surge " + azb("peso morto") + ". Parte "
            "dos consumidores ganha (os que conseguem comprar mais barato); outros ficam sem o produto.",
            rx("Brasil") + ": o congelamento do " + azb("Plano Cruzado") + " (1986) produziu desabastecimento e "
            "cobrança de ágio. Em medicamentos, o Brasil regula preços-teto pela " + rx("CMED") + ", com "
            "reajustes anuais — teto pensado para conter abusos, não para ficar abaixo do custo.",
            vm("Regra-âncora: teto abaixo do equilíbrio → escassez; piso acima do equilíbrio → excedente."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item atribui ao preço máximo o efeito do preço mínimo. "
                       "A motivação (“muito alto”) é a pista que posiciona o teto abaixo do equilíbrio — sem "
                       "ela, um teto acima do equilíbrio seria apenas inócuo, e nunca geraria excedente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…Isto terá como resultado um excesso de demanda pelo medicamento.”</i> → CERTO",
            "<i>“Se o preço máximo fosse fixado acima do preço de equilíbrio, haveria excedente de "
            "produção.”</i> → ERRADO (teto acima do equilíbrio é inócuo)",
        ])],
        "reescrita": ("O governo decide impor um preço máximo para certo medicamento, […]. Isto terá como "
                      "resultado " + hl("uma escassez (excesso de demanda)") + " deste medicamento no mercado."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Ver se o teto está acima ou abaixo do equilíbrio; pela redação, abaixo; há excesso "
                             "de demanda e redução da oferta: escassez, não excedente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0131
    {
        "id": "ECO-E1-0131-1", "fonte_ref": "E1-0131", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": COM_RT_A5,
        "rotulo_item": "Item",
        "assertiva": ("Os efeitos de controles de preços sobre o equilíbrio de mercado tendem a ser maiores no "
                      "curto prazo, mas se dissipam no longo prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os efeitos de controles de preços sobre o equilíbrio de mercado tendem a ser ")
                   + vm("maiores no curto prazo, mas se dissipam no longo prazo") + az("."),
        "poucas": ("No longo prazo, oferta e demanda ficam " + azb("mais elásticas") + ": as quantidades "
                   "reagem mais ao preço controlado, e a escassez (ou o excedente) " + vd("aumenta") + "."),
        "destrinchando": [
            "O tamanho do desequilíbrio criado por um controle (Qᴰ − Qˢ no teto; Qˢ − Qᴰ no piso) depende de "
            "quanto as quantidades reagem ao preço fixado — isto é, das elasticidades.",
            "No curto prazo, curvas inelásticas: o estoque de imóveis é dado, os inquilinos não mudam de casa de "
            "um dia para o outro. O teto de aluguel gera pouca falta. No longo prazo, os proprietários deixam de "
            "construir e de manter imóveis para alugar, e mais famílias procuram aluguel barato: a falta "
            "cresce.",
            "Exemplo clássico de " + oc("Mankiw") + " (<i>Introdução à Economia</i>): o controle de aluguéis, "
            "cujos danos — escassez, deterioração do estoque, filas e discriminação de inquilinos — se "
            "acumulam com os anos. Ele cita o economista " + oc("Assar Lindbeck") + ", para quem o controle de "
            "aluguéis seria a técnica mais eficiente para destruir uma cidade, depois do bombardeio.",
            "Corolário político: controles de preço parecem funcionar logo após a adoção, o que estimula sua "
            "manutenção; o custo aparece depois.",
            vm("Regra-âncora: mais tempo → curvas mais elásticas → distorções maiores."),
        ],
        "grafico_verso": "ECO-E1-0131-1-V1",
        "dissecando": (cz("[inversão]") + " Inverte a dinâmica temporal. A frase soa plausível porque “o "
                       "mercado se ajusta no longo prazo” — mas o ajuste ocorre nas quantidades, e é justamente "
                       "ele que amplia o desequilíbrio quando o preço está travado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A escassez provocada por um teto de aluguéis tende a se agravar com o tempo, à medida que oferta "
            "e demanda se tornam mais elásticas.”</i> → CERTO",
            "<i>“No longo prazo, a oferta se torna menos elástica, o que amplia os efeitos do controle.”</i> → "
            "ERRADO (conclusão certa, mecanismo invertido)",
        ])],
        "reescrita": ("Os efeitos de controles de preços sobre o equilíbrio de mercado tendem a ser "
                      + hl("menores no curto prazo e a se ampliar no longo prazo") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tendem"], "dificuldade": 2,
        "comentario_fonte": ("No curto prazo, curvas menos elásticas, distorções menores; no longo prazo, "
                             "elasticidade maior, distorções maiores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0132
    {
        "id": "ECO-E1-0132-1", "fonte_ref": "E1-0132", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A5,
        "rotulo_item": "Item",
        "assertiva": ("A garantia, pelo governo, de um preço mínimo para o café, no início do século XX, era uma "
                      "política eficaz para garantir uma oferta e demanda em equilíbrio no longo prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A garantia, pelo governo, de um preço mínimo para o café, no início do século XX, ")
                   + vm("era uma política eficaz para garantir uma oferta e demanda em equilíbrio no longo prazo")
                   + az("."),
        "poucas": ("Preço mínimo " + azb("acima do equilíbrio") + " gera excesso de oferta — e, ao garantir "
                   "rentabilidade, estimula ainda mais plantio. O resultado foi " + vd("superprodução crônica")
                   + ", não equilíbrio."),
        "destrinchando": [
            "Mecânica do piso: para sustentar um preço acima do equilíbrio, o governo precisa comprar a sobra. "
            "No longo prazo a oferta é mais elástica (o cafeeiro leva alguns anos para produzir, mas produz por "
            "décadas): com o preço garantido, os fazendeiros plantam mais, e o excedente cresce.",
            rx("Brasil") + ": o " + azb("Convênio de Taubaté") + " (" + vd("1906") + "), de São Paulo, Minas "
            "Gerais e Rio de Janeiro, inaugurou a “valorização”: compra dos excedentes com empréstimos externos "
            "e estocagem para sustentar o preço internacional. A defesa tornou-se permanente nos anos 1920.",
            "Com a crise de 1929, a superprodução explodiu. O governo " + rx("Vargas") + " comprou e "
            + vd("destruiu") + " estoques enormes de café ao longo dos anos 1930.",
            oc("Celso Furtado") + " (<i>Formação Econômica do Brasil</i>, 1959): a defesa do café "
            + azb("socializava as perdas") + " do setor e induzia novos investimentos na própria cultura, "
            "perpetuando o desequilíbrio; nos anos 1930, porém, a compra e destruição dos estoques sustentou a "
            "renda interna e funcionou, sem intenção, como política anticíclica.",
            vm("Regra-âncora: preço mínimo efetivo nunca equilibra o mercado — ele cria um excedente que alguém "
               "tem de absorver."),
        ],
        "dissecando": (cz("[juízo indevido · troca de conceito]") + " O item atribui ao preço mínimo uma "
                       "função (equilibrar o mercado) que é o oposto do que ele faz. A expressão “eficaz para "
                       "garantir… equilíbrio” é o juízo a desconfiar: piso efetivo existe <b>justamente</b> "
                       "para manter o preço fora do equilíbrio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política de valorização do café, ao sustentar preços elevados, estimulou a expansão do plantio "
            "e agravou a superprodução.”</i> → CERTO",
            "<i>“O Convênio de Taubaté previa a fixação de um preço máximo para o café, a fim de baratear o "
            "produto no mercado interno.”</i> → ERRADO (troca de conceito: era sustentação de preço)",
        ])],
        "reescrita": ("A garantia, pelo governo, de um preço mínimo para o café, no início do século XX, "
                      + hl("gerava excedentes crescentes de oferta, que o governo precisava comprar e estocar — "
                      "e não um equilíbrio de longo prazo") + "."),
        "tipo_erro": ["JUIZO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Os preços mínimos “abaixo do equilíbrio” geravam excedente de oferta, e o governo "
                             "tinha de comprar e queimar o café."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a fonte diz que os preços mínimos ficavam “abaixo do equilíbrio”; para "
                    "gerar excedente, ficavam acima"],
    },
    # ------------------------------------------------------------------ E1-0133
    {
        "id": "ECO-E1-0133-1", "fonte_ref": "E1-0133", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_RT_A5,
        "rotulo_item": "Item",
        "assertiva": "Uma elevação do salário mínimo sempre trará ganhos aos trabalhadores.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma elevação do salário mínimo ") + vm("sempre") + az(" trará ganhos aos trabalhadores."),
        "poucas": ("No modelo competitivo, o " + azb("salário mínimo") + " acima do equilíbrio é um "
                   + azb("preço mínimo") + " no mercado de trabalho: ganha quem segue empregado, perde quem fica "
                   "" + vd("desempregado") + ". Nem sempre há ganho para todos."),
        "destrinchando": [
            "Mercado de trabalho competitivo: oferta de trabalho (famílias) × demanda (firmas). Um piso salarial "
            "acima do equilíbrio eleva a quantidade ofertada de trabalho e reduz a demandada: "
            + vd("desemprego involuntário") + " (excesso de oferta de trabalho).",
            "Distribuição: os trabalhadores que mantêm o emprego ganham; os que perdem (ou não conseguem) o "
            "emprego formal perdem — em geral os menos qualificados e os jovens. Parte migra para a "
            "informalidade, onde o mínimo não alcança.",
            "Exceção teórica: em " + azb("monopsônio") + " (empregador com poder de fixar salários, "
            + oc("Joan Robinson") + "), um mínimo moderado pode elevar salário <b>e</b> emprego. A evidência de "
            + oc("Card e Krueger") + " (1994), com redes de fast-food em Nova Jersey e na Pensilvânia, não "
            "encontrou queda de emprego após um aumento do mínimo e reabriu o debate.",
            rx("Brasil") + ": a política de valorização do salário mínimo (reajuste pela inflação mais o "
            "crescimento do PIB) elevou o seu poder de compra desde os anos 2000 e é associada à queda da "
            "desigualdade de renda; o efeito sobre o emprego formal depende do nível do mínimo em relação ao "
            "salário mediano. ⏳ (out/2026)",
        ],
        "dissecando": (cz("[modulador absoluto]") + " O “sempre” é o erro: o efeito depende de onde o mínimo é "
                       "fixado e da estrutura do mercado de trabalho. Mesmo em versões mais brandas, lembre que "
                       "“trabalhadores” não é um grupo homogêneo: empregados × desempregados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo competitivo, um salário mínimo fixado acima do salário de equilíbrio gera "
            "desemprego.”</i> → CERTO",
            "<i>“Em mercado de trabalho monopsonista, qualquer elevação do salário mínimo reduz o emprego.”</i> → "
            "ERRADO (modulador absoluto: um mínimo moderado pode até elevá-lo)",
        ])],
        "reescrita": ("Uma elevação do salário mínimo " + hl("nem sempre") + " trará ganhos aos trabalhadores"
                      + hl(": acima do equilíbrio, beneficia quem mantém o emprego e prejudica quem fica "
                      "desempregado") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("Se o salário mínimo estiver acima do equilíbrio, será bom para quem conseguir "
                             "emprego e ruim para quem ficar desempregado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0134
    {
        "id": "ECO-E1-0134-1", "fonte_ref": "E1-0134", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca de excedentes, eficiência e estruturas de mercado, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": "Peso morto é um fenômeno exclusivo dos mercados em concorrência perfeita.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Peso morto é um fenômeno ") + vm("exclusivo dos mercados em concorrência perfeita")
                   + az("."),
        "poucas": ("É quase o contrário: a " + azb("concorrência perfeita") + " sem intervenção não gera peso "
                   "morto (maximiza o excedente total). Peso morto é típico de " + vd("monopólio")
                   + ", tributos, controles de preços e externalidades."),
        "destrinchando": [
            azb("Peso morto") + " = perda de excedente total que não é apropriada por ninguém: trocas "
            "mutuamente vantajosas (valor para o comprador > custo do vendedor) que deixam de ocorrer.",
            "Em concorrência perfeita, o equilíbrio ocorre onde p = CMg: toda unidade que vale mais do que custa "
            "é produzida. Excedente total máximo, " + vd("peso morto zero") + ".",
            "No " + azb("monopólio") + ", a firma produz onde RMg = CMg, com p > CMg: unidades que valeriam "
            "mais do que custam deixam de ser produzidas. O triângulo entre a demanda e o CMg, da quantidade de "
            "monopólio à competitiva, é o peso morto do monopólio.",
            "Em mercados competitivos, o peso morto aparece quando há <b>distorção</b>: tributos (cunha entre "
            "pc e pv), tetos e pisos efetivos, cotas, subsídios (produção além do ótimo) e externalidades não "
            "corrigidas.",
            vm("Regra-âncora: peso morto nasce de distorção — poder de mercado ou intervenção —, não da "
               "concorrência."),
        ],
        "dissecando": (cz("[restrição indevida · inversão]") + " “Exclusivo” restringe o fenômeno ao único "
                       "ambiente em que, sem intervenção, ele <b>não</b> ocorre. Dica: qualquer “exclusivo” "
                       "colado a um conceito transversal (peso morto aparece em vários contextos) é forte "
                       "candidato a ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopólio gera peso morto porque produz quantidade inferior à que igualaria preço e custo "
            "marginal.”</i> → CERTO",
            "<i>“Em concorrência perfeita, um imposto sobre o produto não gera peso morto.”</i> → ERRADO (só "
            "não gera com oferta ou demanda perfeitamente inelástica)",
        ])],
        "reescrita": ("Peso morto " + hl("não") + " é um fenômeno exclusivo dos mercados em concorrência perfeita"
                      + hl(": surge no monopólio e em mercados competitivos distorcidos por tributos, controles "
                      "de preços ou externalidades") + "."),
        "tipo_erro": ["RESTRICAO", "INVERSAO"], "moduladores": ["exclusivo"], "dificuldade": 1,
        "comentario_fonte": ("O peso morto geralmente está ausente na concorrência perfeita, que tende ao ótimo de "
                             "Pareto; é comum em estruturas não competitivas, como o monopólio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
