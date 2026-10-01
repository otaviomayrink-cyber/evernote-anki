"""Cards da passada 01 de ECO — lote de redação 19 (nota 08 — Monopólio e monopsônio)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "eq": "👑 Equilíbrio do monopólio",
    "mk": "📊 Markup, elasticidade e poder de mercado",
    "disc": "🎟️ Discriminação de preços",
    "nat": "🏛️ Monopólio natural e regulação",
}

COM_MONO = "Acerca do monopólio, julgue o item a seguir."
COM_DISC = "Acerca da discriminação de preços praticada por um monopolista, julgue o item a seguir."
COM_NAT = "Acerca do monopólio natural e de sua regulação, julgue o item a seguir."
COM_CLIP25 = ("No estudo das estruturas de mercado, a concorrência perfeita e o monopólio representam extremos "
              "analíticos com implicações distintas sobre o bem-estar social e a eficiência alocativa. Com base "
              "nesse contexto, julgue os itens a seguir.")
COM_BOZAN = "Analise as assertivas abaixo com relação às características e maximização em um monopólio."
COM_CLIP26 = "Acerca das estruturas de mercado, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E1-0282
    {
        "id": "ECO-E1-0282-1", "fonte_ref": "E1-0282", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Clipping", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado de monopólio, a empresa monopolista enfrenta a curva de demanda do mercado, o "
                      "que significa que o preço é fixado pela empresa e a quantidade produzida é determinada pela "
                      "demanda a esse preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Em um mercado de monopólio, a empresa monopolista enfrenta a curva de demanda do mercado, o "
                      "que significa que ") + vm("o preço é fixado pela empresa e a quantidade produzida é "
                                                 "determinada pela demanda a esse preço") + az("."),
        "poucas": ("Na leitura da banca, o monopolista decide primeiro a " + azb("quantidade")
                   + " (onde " + vd("RMg = CMg") + ") e só depois “sobe” até a demanda para achar o preço; o item "
                   "descreve a sequência invertida."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Formalmente, escolher o preço e deixar a demanda definir a quantidade leva ao "
                          "<b>mesmo</b> ponto ótimo que escolher a quantidade e ler o preço na demanda: a curva "
                          "amarra as duas variáveis, e os manuais (" + oc("Pindyck e Rubinfeld") + ", "
                          + oc("Varian") + ") admitem as duas formulações. O item seria defensável como CERTO; mantém-se o ERRADO da fonte, que cobra a "
                          "sequência didática “quantidade primeiro, preço depois”.")],
        "destrinchando": [
            "O monopolista é o único vendedor, logo a demanda que ele enfrenta é a " + azb("demanda de mercado")
            + ", negativamente inclinada. Isso o torna " + azb("formador de preço") + " (<i>price maker</i>), ao "
            "contrário da firma competitiva, tomadora de preço.",
            "Mas ele não escolhe preço e quantidade de forma independente: escolhido um, a demanda dita o outro. "
            "Na exposição de manual, o roteiro é: (1) igualar " + vd("RMg = CMg") + " → quantidade q<sub>m</sub>; "
            "(2) subir de q<sub>m</sub> até a demanda → preço p<sub>m</sub>.",
            "Como a RMg fica abaixo da demanda, o resultado é " + vd("p<sub>m</sub> > CMg") + ": preço maior e "
            "quantidade menor que na concorrência perfeita, com peso morto.",
            "Por que a ordem importa na prova: a banca quer saber se o candidato sabe que a regra de decisão é "
            "marginal (RMg × CMg) e se aplica à quantidade; o preço é consequência.",
            vm("Regra-âncora: RMg = CMg define q; a demanda define p."),
        ],
        "dissecando": (cz("[inversão]") + " A primeira oração é verdadeira; o erro, para a banca, está na ordem "
                       "causal da segunda (preço → quantidade em vez de quantidade → preço). Itens assim são "
                       "frágeis: o mesmo ponto ótimo é alcançável pelas duas vias. 🔥 Simulados repetem essa "
                       "fórmula “o monopolista fixa o preço e a demanda define a quantidade”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopolista é formador de preço, pois enfrenta toda a demanda do mercado.”</i> → CERTO",
            "<i>“O monopolista pode cobrar o preço que quiser e vender a quantidade que quiser.”</i> → ERRADO "
            "(ignora a restrição da demanda)",
        ])],
        "reescrita": ("Em um mercado de monopólio, a empresa monopolista enfrenta a curva de demanda do mercado, o "
                      "que significa que " + hl("a quantidade é escolhida onde a receita marginal iguala o custo "
                                                "marginal e o preço é dado pela demanda para essa quantidade") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O correto seria o contrário: no cruzamento entre RMg e CMg se acha a quantidade e, a "
                             "partir dela, o preço. O monopolista é price maker e escolhe o ponto da demanda que "
                             "maximiza o lucro."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0291-1 (preço × quantidade como variável de decisão)", "contestavel: escolher o preço ou a quantidade é equivalente no monopólio; gabarito ERRADO da "
                    "fonte mantido pela leitura “quantidade primeiro”"],
    },
    # ------------------------------------------------------------------ E1-0284
    {
        "id": "ECO-E1-0284-1", "fonte_ref": "E1-0284", "destino": "08", "subtema": H2["eq"],
        "tipo": "EXERC", "banca": "Prof. Rodrigo Teixeira", "prova": "Micro – Aula 12", "ano": None,
        "cacd": False, "errei": False,
        "comando": ("Um determinado mercado, onde existe uma única firma ofertante, possui curva de custo total "
                    "dada por CT = 10 + Q², onde CT é o custo total e Q a quantidade produzida. A função de demanda "
                    "deste mercado é dada pela equação P = 300 − Q. A partir destas informações, responda:"),
        "rotulo_item": "Questão",
        "assertiva": ("a) Qual a quantidade que maximiza o lucro do monopolista?<br/>"
                      "b) Qual o preço do produto em monopólio? Qual a taxa de mark up?<br/>"
                      "c) Qual seria o preço caso um agente regulador obrigasse o monopolista a cobrar o preço "
                      "equivalente ao de um mercado competitivo?<br/>"
                      "d) Na situação do item c, qual seria a quantidade ofertada?<br/>"
                      "e) Comparando a situação em monopólio e o equilíbrio competitivo, qual seria o ganho de "
                      "bem-estar na hipótese do item c?<br/>"
                      "f) Qual seria o lucro da firma nas situações de monopólio e no preço de mercado "
                      "competitivo?<br/>"
                      "g) Qual a diferença no bem-estar dos consumidores entre as situações de monopólio e de "
                      "mercado competitivo?"),
        "gabarito": "RESPOSTA", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("a) Q = 75. b) P = 225; markup de 50% sobre o CMg (P = 1,5 × CMg; índice de Lerner = 1/3). "
                      "c) P = 200. d) Q = 100. e) ganho de 937,5 (peso morto eliminado). f) lucro de 11.240 no "
                      "monopólio e de 9.990 com preço competitivo. g) o excedente do consumidor sobe de 2.812,5 "
                      "para 5.000: diferença de 2.187,5."),
        "poucas": ("Monopólio: " + vd("RMg = CMg") + " → 300 − 2Q = 2Q → " + vd("Q = 75, P = 225")
                   + ". Regulação competitiva: " + vd("P = CMg") + " → 300 − Q = 2Q → " + vd("Q = 100, P = 200")
                   + ". A diferença de bem-estar é o triângulo de peso morto."),
        "destrinchando": [
            "Ingredientes: RT = P·Q = 300Q − Q² → " + azb("RMg") + " = " + vd("300 − 2Q") + " (mesmo "
            "intercepto da demanda, inclinação dobrada); CT = 10 + Q² → " + azb("CMg") + " = " + vd("2Q")
            + ". O 10 é custo fixo: não entra em nenhuma decisão marginal.",
            "<b>a) e b)</b> 300 − 2Q = 2Q → " + vd("Q = 75") + "; na demanda, " + vd("P = 225")
            + ". Nesse ponto CMg = 150, logo " + azb("markup") + " sobre o custo marginal = 225/150 − 1 = "
            + vd("50%") + ". Na outra medida usual, o " + azb("índice de Lerner") + " (P − CMg)/P = 75/225 = "
            + vd("1/3") + " — coerente com |ε| = (dQ/dP)·(P/Q) = 225/75 = 3, já que L = 1/|ε|.",
            "<b>c) e d)</b> Preço competitivo = preço igual ao CMg: 300 − Q = 2Q → " + vd("Q = 100, P = 200")
            + ".",
            "<b>e)</b> " + azb("Peso morto") + " eliminado = triângulo entre a demanda e o CMg, de Q = 75 a 100: "
            "(225 − 150) × 25 ÷ 2 = " + vd("937,5") + ".",
            "<b>f)</b> Monopólio: RT = 225 × 75 = 16.875; CT = 10 + 5.625 = 5.635 → " + vd("lucro = 11.240")
            + ". Preço competitivo: RT = 200 × 100 = 20.000; CT = 10 + 10.000 = 10.010 → " + vd("lucro = 9.990")
            + ". Com CMg crescente, a firma regulada ainda lucra.",
            "<b>g)</b> " + azb("Excedente do consumidor") + ": monopólio (300 − 225) × 75 ÷ 2 = 2.812,5; "
            "competitivo (300 − 200) × 100 ÷ 2 = 5.000 → ganho de " + vd("2.187,5") + ". Conferência: o "
            "consumidor ganha 2.187,5, a firma perde 1.250 (11.240 − 9.990) e o saldo é exatamente o peso morto, "
            + vd("937,5") + ".",
        ],
        "grafico_verso": "ECO-E1-0284-1-V1",
        "dissecando": (cz("[exercício aberto]") + " Em C/E, a banca recorta esse cálculo em itens como “o markup "
                       "é de 50% sobre o preço” (ERRADO: 50% é sobre o CMg; sobre o preço, o Lerner dá 1/3) ou "
                       "“o ganho de bem-estar da regulação é todo apropriado pelos consumidores” (ERRADO: parte "
                       "vem de transferência da firma)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A quantidade de monopólio é 100, onde a demanda cruza o custo marginal.”</i> → ERRADO (esse é o "
            "equilíbrio competitivo; o monopólio produz 75)",
            "<i>“O custo fixo de 10 não altera a quantidade ótima do monopolista.”</i> → CERTO",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Verso composto só de nove imagens de resolução, não preservadas.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (90)–(97), (99).png", "tipo_fonte": "TEXTO/GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (exercício resolvido de novo; gráfico didático em "
                                   "ECO-E1-0284-1-V1)"}],
        "alertas": ["figura_irrecuperavel: resolução original só em nove imagens de verso não preservadas; "
                    "respostas recalculadas (conferidas pela identidade ΔEC + Δlucro = peso morto)"],
    },
    # ------------------------------------------------------------------ E1-0285
    {
        "id": "ECO-E1-0285-1", "fonte_ref": "E1-0285", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("O peso morto ocorre quando o monopolista decide produzir e vender a quantidade em que as "
                      "curvas de receita marginal e custo marginal se cruzam."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O peso morto ocorre quando o monopolista decide produzir e vender a quantidade em que as "
                      "curvas de <u>receita marginal e custo marginal</u> se cruzam."),
        "poucas": ("Em " + vd("RMg = CMg") + " o monopolista maximiza o lucro, mas, como a RMg fica abaixo da "
                   "demanda, essa quantidade é menor que a eficiente (" + vd("P = CMg") + "): surge o "
                   + azb("peso morto") + "."),
        "destrinchando": [
            "O ótimo social está onde a disposição a pagar da última unidade (a demanda) iguala o custo de "
            "produzi-la (CMg): é o ponto C do gráfico, que a concorrência perfeita atingiria.",
            "O monopolista não para em C porque, para vender mais uma unidade, precisa baixar o preço de "
            "<b>todas</b>: sua receita marginal é menor que o preço. Ele produz q<sub>m</sub>, onde RMg = CMg, "
            "e cobra p<sub>m</sub>, lido na demanda (ponto M).",
            "Entre q<sub>m</sub> e q<sub>c</sub> há unidades que os consumidores valorizam mais do que custam "
            "e que não são produzidas. O triângulo entre a demanda e o CMg nesse intervalo é o "
            + azb("peso morto") + ": perda líquida, que ninguém captura.",
            "Já o retângulo entre p<sub>m</sub> e o CMg sobre as unidades vendidas é " + azb("transferência")
            + " do consumidor para o monopolista — não é perda para a sociedade.",
            vm("Regra-âncora: monopólio = P > CMg = RMg → q abaixo do eficiente → peso morto."),
        ],
        "grafico_verso": "ECO-E1-0285-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " O item amarra a regra de decisão (RMg = CMg) à sua "
                       "consequência de bem-estar. O risco é o candidato achar que “maximizar lucro” é "
                       "eficiente; a pista é lembrar que P > RMg no monopólio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O peso morto do monopólio corresponde ao lucro extraordinário apropriado pela firma.”</i> → "
            "ERRADO (troca de conceito: o lucro é transferência; o peso morto é o triângulo perdido)",
            "<i>“Sob discriminação perfeita de preços, o monopolista elimina o peso morto.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O monopolista maximiza lucro em RMg = CMg, mas produz menos que o ótimo social; "
                             "quantidade menor (Qm) e preço maior (Pm) que na concorrência perfeita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (63).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (redesenho didático em ECO-E1-0285-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0286
    {
        "id": "ECO-E1-0286-1", "fonte_ref": "E1-0286", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": "Para o monopolista, a curva de receita média é a curva de demanda do mercado.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para o monopolista, a curva de <u>receita média</u> é a curva de demanda do mercado."),
        "poucas": ("Receita média = RT/Q = P·Q/Q = " + vd("P") + ". Como o preço que o monopolista obtém por "
                   "cada quantidade é dado pela demanda de mercado, " + azb("RMe = demanda") + "."),
        "destrinchando": [
            "Identidade válida para qualquer firma que cobre preço único: " + vd("RMe = RT/Q = P")
            + ". O que muda entre estruturas de mercado é <b>qual curva</b> dá esse preço.",
            "No monopólio, a firma é a indústria: a demanda que ela enfrenta é a " + azb("demanda de mercado")
            + ", negativamente inclinada. Logo a RMe coincide com essa curva, e a " + azb("RMg")
            + " fica abaixo dela (na demanda linear P = a − bQ, RMg = a − 2bQ: mesmo intercepto, inclinação "
            "dobrada).",
            "Na concorrência perfeita, a firma individual enfrenta demanda horizontal ao preço de mercado: "
            "" + vd("P = RMe = RMg") + ". É por isso que lá a condição RMg = CMg vira P = CMg.",
            "Com discriminação de preços, a identidade RMe = P deixa de valer para um preço único — cada "
            "unidade ou grupo paga um preço diferente.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, cobrada para testar se o candidato confunde "
                       "receita média com receita marginal. A troca típica que tornaria o item ERRADO é "
                       "“receita marginal” no lugar de “receita média”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para o monopolista, a curva de receita marginal é a curva de demanda do mercado.”</i> → ERRADO "
            "(troca de conceito: a RMg fica abaixo da demanda)",
            "<i>“Para a firma em concorrência perfeita, receita média, receita marginal e preço coincidem.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "No monopólio, a receita média é igual ao preço, que corresponde à curva de demanda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (61).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0287
    {
        "id": "ECO-E1-0287-1", "fonte_ref": "E1-0287", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("O markup na fixação de preços do monopólio tende a se reduzir conforme a elasticidade-preço "
                      "da demanda diminui."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O markup na fixação de preços do monopólio tende a ") + vm("se reduzir")
                   + az(" conforme a elasticidade-preço da demanda diminui."),
        "poucas": ("Demanda menos elástica = consumidor menos sensível ao preço = " + azb("markup maior")
                   + ". O markup é inversamente proporcional à elasticidade: " + vd("(P − CMg)/P = 1/|ε|") + "."),
        "destrinchando": [
            "Da condição RMg = CMg, com RMg = P(1 − 1/|ε|), sai a " + azb("regra de precificação do "
            "monopolista") + ": " + vd("P = CMg / (1 − 1/|ε|)") + ", ou, em forma de margem, "
            + vd("(P − CMg)/P = 1/|ε|") + ".",
            "Exemplos: com |ε| = 4, P = CMg/0,75 ≈ " + vd("1,33 × CMg") + "; com |ε| = 2, P = "
            + vd("2 × CMg") + "; com |ε| = 1,25, P = " + vd("5 × CMg") + ". Elasticidade caindo → markup "
            "subindo.",
            "Intuição: se os consumidores quase não reduzem a compra quando o preço sobe (poucos substitutos, "
            "bem essencial), o monopolista pode afastar muito o preço do custo marginal sem perder vendas.",
            "Limite: o monopolista nunca opera com |ε| ≤ 1 (RMg seria nula ou negativa); o markup “explode” "
            "quando |ε| se aproxima de 1 por cima. No outro extremo, |ε| → ∞ (demanda horizontal) leva a "
            "P = CMg, o caso competitivo.",
            vm("Regra-âncora: elasticidade ↓ → markup ↑ → poder de mercado ↑."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sinal da relação entre markup e elasticidade. Quem "
                       "decorou a fórmula 1/|ε| resolve em segundos; quem pensa “menos elástico = mais "
                       "rígido = menos margem” cai. Pista: “diminui” × “se reduzir” na mesma frase — relação "
                       "direta afirmada onde ela é inversa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O markup do monopolista tende a aumentar conforme a demanda se torna mais elástica.”</i> → "
            "ERRADO (inversão: diminui)",
            "<i>“Se a demanda tiver elasticidade-preço igual a 2 no ponto ótimo, o preço será o dobro do custo "
            "marginal.”</i> → CERTO",
        ])],
        "reescrita": ("O markup na fixação de preços do monopólio tende a " + hl("aumentar")
                      + " conforme a elasticidade-preço da demanda diminui."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Quando a elasticidade diminui (demanda mais inelástica), o markup tende a "
                             "aumentar, pois o consumidor é menos sensível ao preço."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (64).jpeg, Untitled (65).jpeg", "tipo_fonte": "FÓRMULA/GRÁFICO",
                           "lado": "verso", "acao": "irrecuperavel (fórmula do markup reescrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0288
    {
        "id": "ECO-E1-0288-1", "fonte_ref": "E1-0288", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": "O Mark-up é um indicador do poder de monopólio.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Mark-up é um <u>indicador do poder de monopólio</u>."),
        "poucas": ("O markup mede quanto o preço supera o " + azb("custo marginal") + ". Em concorrência perfeita "
                   "ele é nulo (P = CMg); quanto maior, maior o " + azb("poder de mercado") + "."),
        "destrinchando": [
            azb("Poder de monopólio") + " = capacidade de cobrar preço acima do custo marginal. O markup é a "
            "medida direta disso: " + vd("P/CMg − 1") + " (margem sobre o custo) ou, normalizado pelo preço, o "
            + azb("índice de Lerner") + " " + vd("L = (P − CMg)/P") + ", entre 0 e 1.",
            "No ótimo do monopolista, L = 1/|ε|: o markup reflete a elasticidade da demanda que a firma enfrenta. "
            "Por isso uma firma pode ter markup alto e lucro baixo (custos fixos elevados) — o markup mede "
            "<b>poder</b>, não lucratividade.",
            "O conceito vale para qualquer firma com demanda inclinada (oligopólio, concorrência monopolística), "
            "não só para o monopólio puro: “poder de monopólio” é questão de grau.",
            "Na defesa da concorrência, a medida usa o CMg, que não se observa diretamente; na prática, "
            "trabalha-se com proxies (margens de preço sobre custo, participação de mercado, índice HHI).",
        ],
        "dissecando": (cz("[literalidade]") + " Afirmação de manual. A banca poderia torná-la ERRADA trocando o "
                       "denominador (“preço sobre o custo <b>médio</b>”) ou a conclusão (“indicador do lucro do "
                       "monopólio”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um markup elevado implica necessariamente lucro econômico elevado.”</i> → ERRADO (modulador "
            "absoluto: custos fixos podem absorver a margem)",
            "<i>“Em concorrência perfeita, o markup sobre o custo marginal é nulo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Mostra quanto o preço supera o CMg; markup alto indica maior poder de "
                             "monopólio."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (71).jpeg", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "irrecuperavel (fórmula reescrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0289
    {
        "id": "ECO-E1-0289-1", "fonte_ref": "E1-0289", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("A estrutura de mercado em monopólio pode ser caracterizada por apresentar fortes barreiras "
                      "que impedem o surgimento de competidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A estrutura de mercado em monopólio pode ser caracterizada por apresentar <u>fortes "
                      "barreiras</u> que impedem o surgimento de competidores."),
        "poucas": ("Sem " + azb("barreiras à entrada") + ", o lucro de monopólio atrairia concorrentes e o "
                   "monopólio desapareceria. As barreiras são o que o sustenta no longo prazo."),
        "destrinchando": [
            "Fontes clássicas de barreiras (" + oc("Mankiw") + "): (1) " + azb("recurso-chave") + " controlado "
            "por uma única firma; (2) " + azb("barreira legal") + " criada pelo governo — patente, direito "
            "autoral, concessão exclusiva; (3) " + azb("economias de escala") + " tais que uma só firma produz "
            "mais barato que várias (monopólio natural).",
            "Há ainda barreiras estratégicas: preço-limite, excesso de capacidade como ameaça, custos de troca "
            "para o cliente, efeitos de rede (plataformas digitais).",
            "Características do monopólio puro, em bloco: um único vendedor; produto " + azb("sem substitutos "
            "próximos") + "; barreiras fortes; firma formadora de preço; possibilidade de lucro extraordinário "
            "também no longo prazo.",
            "Contraste: na concorrência perfeita e na monopolística, a " + azb("livre entrada") + " zera o "
            "lucro econômico no longo prazo; é justamente a barreira que impede esse ajuste no monopólio.",
            rx("No Brasil") + ", exemplos de barreira legal ou natural: patentes de medicamentos (LPI, Lei "
            "9.279/1996), concessões de saneamento e distribuição de energia.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item conceitual, salvo pelo “pode ser "
                       "caracterizada”. A versão ERRADA típica nega as barreiras ou afirma que o lucro do "
                       "monopólio se dissipa no longo prazo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopólio caracteriza-se pela livre entrada, que zera o lucro econômico no longo "
            "prazo.”</i> → ERRADO (troca de conceito: é traço da concorrência perfeita)",
            "<i>“Patentes constituem barreira legal à entrada e podem originar monopólios temporários.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("O monopólio se sustenta por barreiras à entrada, legais, tecnológicas ou "
                             "econômicas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0290
    {
        "id": "ECO-E1-0290-1", "fonte_ref": "E1-0290", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("Em uma situação de monopólio, a firma maximiza o seu lucro quando o custo marginal é igual à "
                      "receita marginal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma situação de monopólio, a firma maximiza o seu lucro quando o custo marginal é igual "
                      "à <u>receita marginal</u>."),
        "poucas": (vd("RMg = CMg") + " é a condição de lucro máximo de <b>qualquer</b> firma. No monopólio ela "
                   "não equivale a P = CMg, porque a RMg fica abaixo do preço."),
        "destrinchando": [
            "Lucro π(Q) = RT(Q) − CT(Q). No máximo, a derivada é zero: " + vd("dRT/dQ = dCT/dQ")
            + ", isto é, " + azb("RMg = CMg") + ". Enquanto RMg > CMg, produzir mais aumenta o lucro; se "
            "RMg < CMg, produzir menos aumenta o lucro.",
            "Condição de segunda ordem: no ponto, o CMg deve cortar a RMg <b>por baixo</b> (inclinação do CMg "
            "maior que a da RMg). E a firma só produz se o preço cobrir o custo variável médio.",
            "O que muda entre estruturas é a RMg. Concorrência perfeita: " + vd("RMg = P")
            + " → regra vira P = CMg. Monopólio: " + vd("RMg < P") + " → P > CMg (markup).",
            "Achada a quantidade, o monopolista lê o preço na demanda. Erro clássico: tomar como preço o valor "
            "da interseção RMg = CMg (que é o custo marginal, não o preço).",
        ],
        "dissecando": (cz("[literalidade]") + " Regra de ouro da firma. A banca a torna ERRADA trocando a receita "
                       "marginal por “preço” ou “receita média” — aí o item descreve a concorrência perfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopolista maximiza o lucro quando o custo marginal é igual ao preço.”</i> → ERRADO (troca "
            "de conceito: regra da concorrência perfeita)",
            "<i>“No ponto de lucro máximo do monopolista, o preço supera o custo marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Regra de maximização de lucro, válida também no monopólio: CMg = RMg.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (66).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0291
    {
        "id": "ECO-E1-0291-1", "fonte_ref": "E1-0291", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": "Um monopolista estabelece o preço de mercado quando decide o quanto cobrar.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Um monopolista ") + vm("estabelece o preço de mercado quando decide o quanto cobrar")
                   + az("."),
        "poucas": ("Na leitura da fonte, o monopolista decide a " + azb("quantidade") + " (RMg = CMg); o preço "
                   "sai da " + azb("demanda") + " no ponto correspondente — ele não “escolhe o preço” à parte."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O monopolista é, por definição, formador de preço, e escolher o preço (deixando a "
                          "demanda fixar a quantidade) leva ao mesmo ótimo que escolher a quantidade. Lido "
                          "literalmente, o item seria CERTO. Mantém-se o ERRADO da fonte, cuja tese é que a "
                          "variável de decisão é a quantidade e o preço é consequência dela.")],
        "destrinchando": [
            "Roteiro gráfico: no cruzamento RMg × CMg (ponto E) define-se a " + vd("quantidade")
            + "; subindo de E até a demanda (ponto A), obtém-se o " + vd("preço") + " que o mercado aceita "
            "pagar por ela.",
            "O monopolista não pode fixar preço e quantidade ao mesmo tempo: a " + azb("demanda") + " é sua "
            "restrição. Se fixar um preço alto, vende pouco; se quiser vender muito, precisa baixar o preço de "
            "todas as unidades.",
            "Diferença para a concorrência perfeita: lá a firma é " + azb("tomadora de preço")
            + " e escolhe só a quantidade (P = CMg); no monopólio, a firma é " + azb("formadora de preço")
            + ", mas sempre ao longo da curva de demanda.",
            vm("Regra-âncora: o monopolista escolhe um ponto da demanda — na exposição padrão, pela quantidade "
               "(RMg = CMg)."),
        ],
        "dissecando": (cz("[inversão]") + " O gabarito depende da ordem de decisão (preço × quantidade), não de "
                       "erro conceitual grave — por isso o item é frágil. Em prova oficial, prefira a tese "
                       "“quantidade em RMg = CMg, preço na demanda”; desconfie de afirmações de que o "
                       "monopolista cobra “o preço que quiser”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopolista escolhe a quantidade em que RMg = CMg e cobra o preço que a demanda indica para "
            "ela.”</i> → CERTO",
            "<i>“O monopolista pode fixar livremente preço e quantidade, independentemente da demanda.”</i> → "
            "ERRADO (ignora a restrição da demanda)",
        ])],
        "reescrita": ("Um monopolista " + hl("escolhe a quantidade em que a receita marginal iguala o custo "
                                             "marginal, e o preço de mercado é dado pela demanda para essa "
                                             "quantidade") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O monopolista escolhe a quantidade (CMg = RMg); o preço é determinado pela demanda "
                             "naquele ponto (subindo de E até A)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (62).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (pontos E e A descritos no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0282-1 (preço × quantidade como variável de decisão)", "contestavel: o monopolista é formador de preço e a escolha de P ou de Q é equivalente; "
                    "gabarito ERRADO da fonte mantido pela leitura “quantidade primeiro”"],
    },
    # ------------------------------------------------------------------ E1-0292
    {
        "id": "ECO-E1-0292-1", "fonte_ref": "E1-0292", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("Um monopolista vende um produto visando maximizar seu lucro. Com esse objetivo, ele deve "
                      "produzir uma quantidade tal que o custo marginal seja igual ao preço de venda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um monopolista vende um produto visando maximizar seu lucro. Com esse objetivo, ele deve "
                      "produzir uma quantidade tal que o custo marginal seja igual ao ") + vm("preço de venda")
                   + az("."),
        "poucas": (vd("CMg = P") + " é a regra da " + azb("concorrência perfeita") + ". O monopolista iguala "
                   "o CMg à " + azb("receita marginal") + ", que fica abaixo do preço; resultado: P > CMg."),
        "destrinchando": [
            "Toda firma maximiza lucro em " + vd("RMg = CMg") + ". Na concorrência perfeita, RMg = P (cada "
            "unidade extra é vendida ao preço de mercado, sem afetá-lo), daí P = CMg.",
            "No monopólio, vender uma unidade a mais exige baixar o preço de todas: " + vd("RMg = P(1 − 1/|ε|) "
            "< P") + ". Logo, no ótimo, " + vd("P > RMg = CMg") + ".",
            "Se o monopolista produzisse onde P = CMg, estaria além do ponto de lucro máximo: as últimas "
            "unidades teriam RMg < CMg e reduziriam o lucro.",
            "P = CMg é, porém, o critério de " + azb("eficiência alocativa") + ": é o que um regulador tentaria "
            "impor (ver monopólio natural, onde essa regra pode gerar prejuízo).",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca “receita marginal” por “preço de venda”, importando a "
                       "regra da concorrência perfeita. 🔥 Erro recorrente em simulados e provas: P = CMg "
                       "atribuído ao monopolista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…ele deve produzir uma quantidade tal que o custo marginal seja igual à receita "
            "marginal.”</i> → CERTO",
            "<i>“…tal que o custo médio seja igual ao preço de venda.”</i> → ERRADO (troca de conceito: essa é "
            "a condição de lucro econômico nulo)",
        ])],
        "reescrita": ("Um monopolista vende um produto visando maximizar seu lucro. Com esse objetivo, ele deve "
                      "produzir uma quantidade tal que o custo marginal seja igual à " + hl("receita marginal")
                      + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": "No monopólio, preço > receita marginal; CMg = preço é regra da concorrência perfeita.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0693-1 (P = CMg atribuído ao monopolista, outra fonte)"],
    },
    # ------------------------------------------------------------------ E1-0293
    {
        "id": "ECO-E1-0293-1", "fonte_ref": "E1-0293", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": "No monopólio há produtos substitutos próximos.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No monopólio ") + vm("há") + az(" produtos substitutos próximos."),
        "poucas": ("O monopólio pressupõe produto " + azb("sem substitutos próximos") + ": se houvesse, os "
                   "consumidores migrariam ao menor aumento de preço e o poder de mercado sumiria."),
        "destrinchando": [
            "Monopólio puro, em quatro traços: " + vd("um único vendedor") + "; produto " + vd("sem "
            "substitutos próximos") + "; " + vd("barreiras à entrada") + " fortes; firma " + azb("formadora "
            "de preço") + ".",
            "A ausência de substitutos é o que torna a demanda do monopolista relativamente " + azb("inelástica")
            + " e permite cobrar P > CMg. Em linguagem de elasticidade, a " + azb("elasticidade-preço cruzada")
            + " entre o produto do monopolista e os demais é baixa.",
            "“Substituto próximo” é questão de grau: sempre há algum substituto distante (o metrô concorre com "
            "ônibus e carro). Por isso a defesa da concorrência começa definindo o " + azb("mercado relevante")
            + " pelo teste do monopolista hipotético.",
            "Contraste: na " + azb("concorrência monopolística") + " (" + oc("Chamberlin") + ", 1933) há muitos "
            "vendedores de produtos diferenciados, que <b>são</b> substitutos próximos entre si — cada firma "
            "tem pequeno poder de mercado, mas a livre entrada zera o lucro no longo prazo.",
            "Exemplos de monopólio citados em manuais: companhias de abastecimento de água, empresas com "
            "patentes exclusivas, serviços de metrô.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui ao monopólio um traço da concorrência monopolística. "
                       "Item curto e direto: a palavra decisiva é o verbo “há”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência monopolística, as firmas vendem produtos diferenciados que são substitutos "
            "próximos entre si.”</i> → CERTO",
            "<i>“O monopólio pressupõe a inexistência de qualquer substituto para o produto.”</i> → ERRADO "
            "(modulador absoluto: exige-se a ausência de substitutos <b>próximos</b>)",
        ])],
        "reescrita": "No monopólio " + hl("não há") + " produtos substitutos próximos.",
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Não existem substitutos próximos; monopolista controla preço e quantidade; "
                             "barreiras significativas; exemplos: abastecimento, patentes, metrô."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0294
    {
        "id": "ECO-E1-0294-1", "fonte_ref": "E1-0294", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("A curva de demanda individual do monopolista é igual à curva de demanda do mercado. Isso "
                      "porque o monopolista é o próprio mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de demanda individual do monopolista é igual à curva de demanda do mercado. Isso "
                      "porque o monopolista <u>é o próprio mercado</u>."),
        "poucas": ("Sendo o único vendedor, o monopolista atende sozinho toda a demanda: a demanda que ele "
                   "enfrenta é a " + azb("demanda de mercado") + ", " + vd("negativamente inclinada") + "."),
        "destrinchando": [
            "No monopólio, firma = indústria. Por isso a curva de demanda da firma coincide com a do mercado e "
            "tem inclinação negativa: para vender mais, o monopolista precisa baixar o preço.",
            "Na " + azb("concorrência perfeita") + ", a demanda de mercado também é negativamente inclinada, "
            "mas a firma individual, minúscula diante do mercado, enfrenta demanda " + vd("horizontal")
            + " ao preço vigente (perfeitamente elástica): se cobrar um centavo a mais, perde todos os "
            "clientes.",
            "Consequências da demanda inclinada: o monopolista tem poder de fixar preço (ao longo da curva), sua "
            "RMe é a própria demanda e sua RMg fica abaixo dela.",
            "Não confundir “controlar o preço” com “ignorar a demanda”: o monopolista não precisa se preocupar "
            "com concorrentes ao subir o preço, mas perde vendas conforme a elasticidade dos consumidores.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta, com justificativa correta. A versão ERRADA "
                       "clássica diria que a demanda do monopolista é “horizontal” ou “perfeitamente elástica”, "
                       "trocando-a pela da firma competitiva."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A firma em concorrência perfeita enfrenta curva de demanda negativamente inclinada, igual à "
            "do mercado.”</i> → ERRADO (troca de ator: a da firma competitiva é horizontal)",
            "<i>“Como enfrenta toda a demanda do mercado, o monopolista pode vender qualquer quantidade a "
            "qualquer preço.”</i> → ERRADO (nexo indevido: preço e quantidade estão amarrados pela demanda)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O monopolista atende sozinho toda a demanda do mercado; controla a quantidade; tem "
                             "poder de determinar o preço; curva negativamente inclinada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (73).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0295
    {
        "id": "ECO-E1-0295-1", "fonte_ref": "E1-0295", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": "O monopolista atua na parte inelástica da curva de demanda.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O monopolista atua na parte ") + vm("inelástica") + az(" da curva de demanda."),
        "poucas": ("Com CMg > 0, o ótimo RMg = CMg exige " + vd("RMg > 0") + ", o que só ocorre onde "
                   + vd("|ε| > 1") + ": o monopolista atua no trecho " + azb("elástico") + "."),
        "destrinchando": [
            "Relação-chave: " + vd("RMg = P(1 − 1/|ε|)") + ". Se |ε| > 1, RMg > 0; se |ε| = 1, RMg = 0; se "
            "|ε| < 1, RMg < 0.",
            "No trecho " + azb("inelástico") + ", reduzir a quantidade (subir o preço) <b>aumenta</b> a receita "
            "total e ainda poupa custos. Logo nenhum monopolista racional para ali: ele sempre ganharia "
            "produzindo menos.",
            "Na demanda linear P = a − bQ, a RMg zera no " + azb("ponto médio") + " (Q = a/2b), onde |ε| = 1. "
            "Acima dele (à esquerda no gráfico), a demanda é elástica; abaixo, inelástica. Quanto mais à "
            "esquerda, maior a elasticidade.",
            "Caso-limite: com " + vd("CMg = 0") + ", o monopolista maximiza a receita e opera exatamente em "
            "|ε| = 1.",
            vm("Regra-âncora: monopolista com CMg positivo → sempre no trecho elástico (|ε| > 1)."),
        ],
        "grafico_verso": "ECO-E1-0295-1-V1",
        "dissecando": (cz("[troca de conceito · contraintuitivo]") + " O item explora a intuição errada de que "
                       "o monopolista “prefere” consumidores insensíveis ao preço — confusão entre o poder de "
                       "mercado (maior com demanda menos elástica) e o ponto em que ele opera (sempre elástico). "
                       "🔥 Pergunta recorrente em simulados de micro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o custo marginal for nulo, o monopolista opera no ponto de elasticidade unitária da "
            "demanda.”</i> → CERTO",
            "<i>“O monopolista pode operar no trecho inelástico se o custo marginal for suficientemente "
            "alto.”</i> → ERRADO (com CMg > 0 a RMg precisa ser positiva: trecho elástico)",
        ])],
        "reescrita": "O monopolista atua na parte " + hl("elástica") + " da curva de demanda.",
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O monopolista atua no trecho elástico, não no inelástico; quanto mais à esquerda "
                             "na curva, maior a elasticidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (67).jpeg, Untitled (69).jpeg", "tipo_fonte": "GRÁFICO",
                           "lado": "verso", "acao": "irrecuperavel (redesenho didático em ECO-E1-0295-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0296
    {
        "id": "ECO-E1-0296-1", "fonte_ref": "E1-0296", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": "O poder de monopólio é maior quanto menor for a elasticidade-preço da demanda.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O poder de monopólio é maior quanto <u>menor</u> for a elasticidade-preço da demanda."),
        "poucas": ("Pelo " + azb("índice de Lerner") + ", " + vd("L = 1/|ε|") + ": demanda menos elástica → "
                   "margem preço–custo maior → mais poder de monopólio."),
        "destrinchando": [
            "Consumidores pouco sensíveis ao preço permitem elevar P bem acima do CMg perdendo poucas vendas. "
            "Formalmente: " + vd("(P − CMg)/P = 1/|ε|") + ".",
            "Determinantes do poder de monopólio (" + oc("Pindyck e Rubinfeld") + "): (1) a elasticidade da "
            "demanda de mercado; (2) o número de firmas; (3) a interação entre elas. O que importa é a "
            "elasticidade da demanda <b>da firma</b>, que no monopólio puro é a do mercado.",
            "Cuidado com a leitura conjunta: maior poder (|ε| baixo no mercado) não significa que o monopolista "
            "opere no trecho inelástico — no ótimo, a elasticidade é sempre |ε| > 1.",
            "Aplicações: bens com poucos substitutos (medicamentos patenteados, serviços essenciais) concentram "
            "poder de mercado; por isso entram na mira da regulação e da defesa da concorrência.",
        ],
        "dissecando": (cz("[literalidade]") + " Relação inversa correta. A banca inverteria com “maior for a "
                       "elasticidade” — mesma armadilha do markup."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O poder de monopólio é maior quanto mais elástica for a demanda.”</i> → ERRADO (inversão)",
            "<i>“Uma firma diante de demanda perfeitamente elástica não tem poder de monopólio.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Demanda inelástica: consumidores menos sensíveis ao preço, monopolista eleva "
                             "preços com menor perda de vendas, mais poder de mercado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0297
    {
        "id": "ECO-E1-0297-1", "fonte_ref": "E1-0297", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("O índice de Lerner (L) é um indicador usado para avaliar o grau de poder de mercado ou "
                      "monopólio que uma empresa possui. Quanto menor, menor será o poder de monopólio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O índice de Lerner (L) é um indicador usado para avaliar o grau de poder de mercado ou "
                      "monopólio que uma empresa possui. <u>Quanto menor, menor</u> será o poder de monopólio."),
        "poucas": (azb("L = (P − CMg)/P") + ", entre " + vd("0") + " (concorrência perfeita, P = CMg) e perto de "
                   + vd("1") + ": quanto menor L, menor o poder de monopólio."),
        "destrinchando": [
            "Proposto por " + oc("Abba Lerner") + " (1934), o índice mede a margem do preço sobre o custo "
            "marginal como fração do preço: " + vd("L = (P − CMg)/P") + ".",
            "Leitura: " + vd("L = 0") + " → P = CMg, sem poder de mercado; L próximo de " + vd("1")
            + " → preço muito acima do custo marginal. Não passa de 1, porque CMg ≥ 0.",
            "No ótimo do monopolista, " + vd("L = 1/|ε|") + ": o índice reflete a elasticidade da demanda que a "
            "firma enfrenta. Exemplo: |ε| = 4 → L = 0,25 (o preço é 25% acima do CMg, medido sobre o preço).",
            "Limites: L alto não implica lucro alto (custos fixos podem absorver a margem), e o CMg raramente é "
            "observável — na prática, usam-se estimativas.",
            vm("Regra-âncora: Lerner sobe com o poder de mercado e cai com a elasticidade."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição correta, com relação direta (L menor → poder menor). A "
                       "versão ERRADA inverteria a relação ou diria que L “é igual à elasticidade” (é o "
                       "<b>inverso</b> dela)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio do monopolista, o índice de Lerner é igual à elasticidade-preço da "
            "demanda.”</i> → ERRADO (é o inverso: L = 1/|ε|)",
            "<i>“Em concorrência perfeita, o índice de Lerner é nulo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito e duas imagens (fórmula do índice de Lerner).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "Untitled (70).jpeg, Untitled (74).jpeg", "tipo_fonte": "FÓRMULA",
                           "lado": "verso", "acao": "irrecuperavel (fórmula reescrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0298
    {
        "id": "ECO-E1-0298-1", "fonte_ref": "E1-0298", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_NAT,
        "rotulo_item": "Item",
        "assertiva": "No monopólio natural o custo fixo é baixo.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No monopólio natural o custo fixo é ") + vm("baixo") + az("."),
        "poucas": ("O monopólio natural nasce de " + azb("custo fixo alto") + " e custo marginal baixo: o custo "
                   "médio cai em toda a faixa da demanda, e uma só firma atende o mercado mais barato que várias."),
        "destrinchando": [
            "Custo médio = CF/Q + CVMe. Com " + vd("CF elevado") + " (rede de trilhos, adutoras, linhas de "
            "transmissão) e CVMe baixo, o termo CF/Q despenca à medida que Q cresce: " + azb("economias de "
            "escala") + " em toda a faixa relevante.",
            "Daí a " + azb("subaditividade de custos") + ": C(Q) < C(q₁) + C(q₂) para q₁ + q₂ = Q. Duas redes de "
            "água na mesma rua duplicariam o custo fixo sem ganho algum.",
            "Exemplos: ferrovias, tratamento e distribuição de água, distribuição de eletricidade e gás, metrô.",
            "Consequência regulatória: a entrada de concorrentes encareceria a produção; por isso o Estado "
            "concede e regula (tarifas), ou presta diretamente. " + rx("No Brasil") + ", esses serviços são "
            "concedidos e regulados por agências (ANEEL na energia, ANTT nas ferrovias; no saneamento, "
            "agências subnacionais, sob normas de referência da ANA).",
            vm("Regra-âncora: monopólio natural = CF alto + CMe decrescente em toda a demanda."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o atributo de custo que define o monopólio natural. Pista: "
                       "se o custo fixo fosse baixo, a entrada seria fácil e não haveria razão “natural” para "
                       "uma só firma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, o custo médio é decrescente na faixa relevante da demanda.”</i> → CERTO",
            "<i>“O monopólio natural decorre de barreiras legais, como patentes.”</i> → ERRADO (troca de "
            "conceito: decorre da estrutura de custos)",
        ])],
        "reescrita": "No monopólio natural o custo fixo é " + hl("alto") + ".",
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No monopólio natural o custo fixo é alto. Exemplos: ferrovias, água, "
                             "eletricidade, metrô."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (72).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0299
    {
        "id": "ECO-E1-0299-1", "fonte_ref": "E1-0299", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_DISC,
        "rotulo_item": "Item",
        "assertiva": ("Na discriminação de preços de terceiro grau, o monopolista atinge o preço máximo que os "
                      "consumidores estão dispostos a pagar."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na discriminação de preços de ") + vm("terceiro grau") + az(", o monopolista atinge o "
                                                                               "preço máximo que os "
                                                                               "consumidores estão dispostos a "
                                                                               "pagar."),
        "poucas": ("Cobrar de cada consumidor o seu " + azb("preço de reserva") + " é a discriminação de "
                   + vd("primeiro grau") + " (perfeita). A de terceiro grau cobra um preço por <b>grupo</b>."),
        "destrinchando": [
            "Classificação de " + oc("Pigou") + " (<i>The Economics of Welfare</i>, 1920), em três graus:",
            vd("1º grau") + " (perfeita): cada unidade é vendida ao preço máximo que o comprador aceita pagar. "
            "O monopolista captura " + azb("todo o excedente do consumidor") + "; a quantidade é a eficiente "
            "(sem peso morto). Exige conhecer a disposição a pagar de cada um — próximo disso: leilões, "
            "negociação individual, consultorias, bens raros e de coleção.",
            vd("2º grau") + ": o preço por unidade varia com a <b>quantidade</b> comprada (descontos por volume, "
            "tarifas em blocos, “leve 3, pague 2”). Os consumidores se autosselecionam.",
            vd("3º grau") + ": o mercado é dividido em <b>grupos</b> identificáveis (estudantes, idosos, "
            "regiões), cada um com um preço; o grupo de demanda menos elástica paga mais. Dentro do grupo, "
            "todos pagam o mesmo — logo sobra excedente para quem valoriza mais.",
            vm("Regra-âncora: 1º grau = cada um paga o seu máximo; 2º = por quantidade; 3º = por grupo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A definição (extrair o preço máximo) está certa, mas é do "
                       "1º grau, não do 3º. 🔥 Itens de discriminação quase sempre trocam o grau; vale decorar a "
                       "tríade “indivíduo – quantidade – grupo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação de preços de primeiro grau, o monopolista se apropria de todo o excedente do "
            "consumidor.”</i> → CERTO",
            "<i>“Na discriminação de terceiro grau, cobra-se preço maior do grupo de demanda mais "
            "elástica.”</i> → ERRADO (inversão: paga mais o grupo menos elástico)",
        ])],
        "reescrita": ("Na discriminação de preços de " + hl("primeiro grau") + ", o monopolista atinge o preço "
                      "máximo que os consumidores estão dispostos a pagar."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Característica da discriminação de primeiro grau (perfeita): o monopolista "
                             "apropria-se de todo o excedente do consumidor; ex.: bens de luxo, raros, de "
                             "coleção."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (68).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0300
    {
        "id": "ECO-E1-0300-1", "fonte_ref": "E1-0300", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_DISC,
        "rotulo_item": "Item",
        "assertiva": ("No monopólio, a discriminação de preços de segundo grau é famosa pela frase “leve 3, pague "
                      "2”."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No monopólio, a discriminação de preços de <u>segundo grau</u> é famosa pela frase “leve 3, "
                      "pague 2”."),
        "poucas": ("No " + vd("2º grau") + ", o preço por unidade depende da " + azb("quantidade comprada")
                   + ": quem leva mais paga menos por unidade — é a lógica do “leve 3, pague 2”."),
        "destrinchando": [
            "A firma não sabe quem é quem (se soubesse, faria 1º grau) nem separa grupos por característica "
            "observável (3º grau). Em vez disso, oferece um <b>cardápio</b> de preços por quantidade e deixa o "
            "consumidor se " + azb("autosselecionar") + ".",
            "Formas típicas: descontos por volume, embalagens econômicas, " + azb("tarifas em blocos")
            + " (energia e água cobradas por faixa de consumo), pacotes de dados, cartões de fidelidade "
            "progressivos.",
            "Efeito: captura parte do excedente do consumidor nas primeiras unidades (vendidas a preço alto) e "
            "expande as vendas nas seguintes (mais baratas) — em geral, a quantidade se aproxima da eficiente.",
            "Contraste rápido: 1º grau → preço por <b>pessoa</b> (preço de reserva); 3º grau → preço por "
            "<b>grupo</b> (meia-entrada, tarifa de idoso).",
        ],
        "dissecando": (cz("[literalidade]") + " Item de associação exemplo → grau. A banca o tornaria ERRADO "
                       "trocando o grau (“primeiro” ou “terceiro”) ou associando o 2º grau a “grupos de "
                       "consumidores”."),
        "modulos": [("🧠 Mnemônico", ["<b>1º</b> grau = <b>1</b> preço para cada pessoa; <b>2º</b> = "
                                      "quantidade (“leve <b>3</b>, pague <b>2</b>”); <b>3º</b> = <b>terceira</b> "
                                      "idade, estudantes: grupos."]),
                    ("😈 Para dificultar", [
                        "<i>“Tarifas de energia elétrica crescentes por faixa de consumo ilustram discriminação "
                        "de segundo grau.”</i> → CERTO",
                        "<i>“Descontos para estudantes ilustram discriminação de segundo grau.”</i> → ERRADO "
                        "(grau trocado: é de terceiro grau)",
                    ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Segundo grau = leve 3 pague 2: o foco é a quantidade adquirida; preços variados "
                             "por unidade conforme a quantidade comprada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0301
    {
        "id": "ECO-E1-0301-1", "fonte_ref": "E1-0301", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_DISC,
        "rotulo_item": "Item",
        "assertiva": ("No monopólio, a discriminação de preços de terceiro grau divide os compradores em grupos "
                      "baseados em suas características ou comportamento e cobra preços diferentes de cada "
                      "grupo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No monopólio, a discriminação de preços de <u>terceiro grau</u> divide os compradores em "
                      "grupos baseados em suas características ou comportamento e cobra preços diferentes de "
                      "cada grupo."),
        "poucas": ("No " + vd("3º grau") + ", o critério é o " + azb("grupo") + " (idade, condição de estudante, "
                   "região, horário), não a quantidade comprada: cada grupo paga um preço."),
        "destrinchando": [
            "Condições para funcionar: (1) poder de mercado; (2) grupos " + azb("identificáveis") + " com "
            "elasticidades diferentes; (3) impossibilidade de " + azb("revenda") + " entre grupos (arbitragem).",
            "Regra de ótimo: " + vd("RMg₁ = RMg₂ = CMg") + ". Como RMg = P(1 − 1/|ε|), o grupo de demanda "
            + vd("menos elástica paga mais") + " (executivos em passagens aéreas) e o mais elástico paga menos "
            "(estudantes, idosos, turistas que compram com antecedência).",
            "Diferença para os outros graus: no 2º, o preço depende de <b>quanto</b> se compra e o consumidor "
            "se autosseleciona; no 1º, cada pessoa paga seu preço de reserva.",
            "Bem-estar: ambíguo. Pode ampliar a quantidade total e atender grupos que, com preço único, "
            "ficariam de fora; mas transfere excedente ao monopolista e pode reduzir o bem-estar se a "
            "produção total não aumentar.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, reproduzida fielmente. A pegadinha "
                       "possível estaria em trocar “características” por “quantidade comprada” (2º grau) ou "
                       "afirmar que o grupo mais elástico paga mais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação de terceiro grau, o preço é maior no mercado em que a demanda é menos "
            "elástica.”</i> → CERTO",
            "<i>“A discriminação de terceiro grau dispensa a separação entre os mercados, pois a revenda entre "
            "grupos não a afeta.”</i> → ERRADO (a arbitragem anula a discriminação)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Divide os compradores em grupos segundo características ou comportamento e cobra "
                             "preços diferentes de cada grupo; exemplo: descontos para a terceira idade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0340
    {
        "id": "ECO-E1-0340-1", "fonte_ref": "E1-0340", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COM_MONO,
        "rotulo_item": "Item",
        "assertiva": ("Um monopólio irá sempre produzir um nível de produto que é igual ao nível socialmente "
                      "eficiente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um monopólio irá ") + vm("sempre produzir um nível de produto que é igual ao")
                   + az(" nível socialmente eficiente."),
        "poucas": ("O monopolista produz onde " + vd("RMg = CMg") + ", com P > CMg: a quantidade fica "
                   + azb("abaixo") + " da eficiente (P = CMg), e surge peso morto."),
        "destrinchando": [
            "Nível socialmente eficiente: produzir até que o benefício marginal (a demanda) iguale o custo "
            "marginal social. Sem externalidades, é o ponto " + vd("P = CMg") + ", o da concorrência perfeita.",
            "O monopolista para antes: como a RMg fica abaixo do preço, no seu ótimo ainda há unidades que os "
            "consumidores valorizam acima do custo e que não são produzidas — o " + azb("peso morto") + ".",
            "Exceção que derruba o “sempre” pelo outro lado: na " + azb("discriminação perfeita") + " (1º "
            "grau), o monopolista produz a quantidade eficiente, embora se aproprie de todo o excedente.",
            "Com " + azb("externalidade negativa") + " (poluição), o ótimo social fica abaixo do competitivo; "
            "a restrição de produção do monopólio pode até aproximá-lo desse ótimo, mas só por coincidência — "
            "o monopolista não internaliza o dano.",
        ],
        "dissecando": (cz("[modulador absoluto · inversão]") + " O “sempre” é o alarme, e o conteúdo inverte o "
                       "resultado padrão (subprodução). Quem lembra que maximizar lucro ≠ maximizar bem-estar "
                       "resolve na hora."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em geral, o monopólio produz menos e cobra mais do que um mercado competitivo com os mesmos "
            "custos.”</i> → CERTO",
            "<i>“Um monopolista com discriminação perfeita de preços produz quantidade inferior à "
            "eficiente.”</i> → ERRADO (com discriminação perfeita a quantidade é a eficiente)",
        ])],
        "reescrita": ("Um monopólio " + hl("tende a") + " produzir um nível de produto " + hl("inferior ao")
                      + " nível socialmente eficiente."),
        "tipo_erro": ["GENERALIZACAO", "INVERSAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("O monopólio tende a subproduzir; com externalidade negativa, também não a "
                             "internaliza por si só."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0435
    {
        "id": "ECO-E1-0435-1", "fonte_ref": "E1-0435", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Clipping", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COM_CLIP25,
        "rotulo_item": "Item",
        "assertiva": ("No monopólio, a receita marginal é sempre igual ao preço, o que implica que o monopolista "
                      "opera no ponto em que o custo marginal iguala o preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No monopólio, a receita marginal é sempre ") + vm("igual ao preço") + az(", o que implica "
                      "que o monopolista opera no ponto em que o custo marginal iguala ") + vm("o preço") + az("."),
        "poucas": ("No monopólio, " + vd("RMg < P") + " (para vender mais, baixa-se o preço de todas as "
                   "unidades). O ótimo é " + vd("RMg = CMg") + ", com " + vd("P > CMg") + ". RMg = P só na "
                   "concorrência perfeita."),
        "destrinchando": [
            "Diante da demanda negativamente inclinada, vender uma unidade a mais tem dois efeitos sobre a "
            "receita: " + azb("efeito-quantidade") + " (+ o preço da unidade extra) e " + azb("efeito-preço")
            + " (− a redução de preço aplicada a todas as unidades que já seriam vendidas). Logo a RMg fica "
            "abaixo do preço.",
            "Exemplo: 10 unidades a R$ 20 (RT = 200); para vender a 11ª, o preço cai a R$ 19 (RT = 209). A "
            "RMg da 11ª unidade é " + vd("R$ 9") + ", bem abaixo do preço de R$ 19.",
            "Na concorrência perfeita, a firma vende o quanto quiser ao preço de mercado: não há efeito-preço, "
            "e " + vd("RMg = P") + ". Daí a regra P = CMg.",
            "Como o monopolista iguala RMg = CMg e RMg < P, obtém " + vd("P > CMg") + ": a margem medida pelo "
            + azb("índice de Lerner") + " (P − CMg)/P, que se aproxima de 1 quanto maior o poder de mercado.",
            "Resultado de bem-estar: preço mais alto, quantidade menor e " + azb("peso morto") + " em relação "
            "ao mercado competitivo.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item transplanta para o monopólio a identidade RMg = P "
                       "da concorrência perfeita e deduz dela, com lógica impecável, a regra P = CMg. A premissa "
                       "falsa contamina a conclusão. O “sempre” reforça o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio, a receita marginal é inferior ao preço para toda quantidade positiva.”</i> → "
            "CERTO",
            "<i>“Na concorrência perfeita, a receita marginal da firma é igual ao preço, o que implica produção "
            "no ponto em que o custo marginal iguala o preço.”</i> → CERTO",
        ])],
        "reescrita": ("No monopólio, a receita marginal é sempre " + hl("inferior ao preço") + ", o que implica "
                      "que o monopolista opera no ponto em que o custo marginal iguala " + hl("a receita "
                      "marginal, com preço acima do custo marginal") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("RMg abaixo da demanda; ótimo em RMg = CMg com P > CMg; igualdade entre preço e "
                             "RMg só na concorrência perfeita; efeitos quantidade e preço; exemplos numéricos; "
                             "índice de Lerner. Duplicata E1-0537 com o mesmo comentário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (154).png", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "irrecuperavel (fórmula do índice de Lerner reescrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0437
    {
        "id": "ECO-E1-0437-1", "fonte_ref": "E1-0437", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Clipping", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COM_CLIP25,
        "rotulo_item": "Item",
        "assertiva": ("O poder de mercado do monopolista gera perda de eficiência alocativa, pois a produção "
                      "ocorre em quantidade inferior àquela que maximizaria o bem-estar social."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O poder de mercado do monopolista gera perda de eficiência alocativa, pois a produção "
                      "ocorre em quantidade <u>inferior</u> àquela que maximizaria o bem-estar social."),
        "poucas": ("Ao produzir onde RMg = CMg (com P > CMg), o monopolista deixa de realizar trocas "
                   "mutuamente vantajosas: é o " + azb("peso morto") + ", a perda de " + azb("eficiência "
                   "alocativa") + "."),
        "destrinchando": [
            azb("Eficiência alocativa") + ": produzir cada bem até que o valor da última unidade para o "
            "consumidor (preço) iguale seu custo marginal — " + vd("P = CMg") + ". O monopólio viola essa "
            "condição: " + vd("P > CMg") + ".",
            "Bem-estar comparado com a concorrência perfeita (mesmos custos): o consumidor perde excedente; "
            "parte dele vira lucro do monopolista (" + azb("transferência") + "); outra parte não vai para "
            "ninguém (" + azb("peso morto") + ", <i>deadweight loss</i>).",
            "O peso morto é maior quanto menos elástica a demanda e quanto mais o preço se afasta do CMg.",
            "Ineficiências adicionais discutidas na literatura: " + azb("ineficiência X") + " ("
            + oc("Leibenstein") + ": sem pressão competitiva, custos acima do mínimo) e gastos de "
            + azb("rent-seeking") + " para obter ou preservar o monopólio (" + oc("Tullock") + ", "
            + oc("Posner") + ").",
            "Contraponto: monopólio natural e patentes podem ser socialmente justificáveis (economias de escala, "
            "incentivo à inovação — " + oc("Schumpeter") + "), o que motiva regulação em vez de proibição.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Descrição padrão do custo social do monopólio. "
                       "A versão ERRADA trocaria “inferior” por “superior” ou diria que a perda de bem-estar "
                       "equivale ao lucro do monopolista (que é transferência)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A perda de bem-estar do monopólio corresponde integralmente ao lucro extraordinário da "
            "firma.”</i> → ERRADO (troca de conceito: o lucro é transferência; a perda é o peso morto)",
            "<i>“O monopólio gera ineficiência alocativa porque o preço supera o custo marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Definição do peso morto do monopólio: ao produzir menos e cobrar mais, o "
                             "monopolista impede trocas mutuamente vantajosas. Duplicata E1-0539 com o mesmo "
                             "comentário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0691
    {
        "id": "ECO-E1-0691-1", "fonte_ref": "E1-0691", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_CLIP26,
        "rotulo_item": "Item",
        "assertiva": ("Um monopólio natural, caracterizado por custos marginais crescentes, justifica a entrada de "
                      "múltiplas empresas para promover concorrência e eficiência alocativa no mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um monopólio natural, caracterizado por ") + vm("custos marginais crescentes")
                   + az(", ") + vm("justifica a entrada de múltiplas empresas") + az(" para promover "
                                                                                       "concorrência e "
                                                                                       "eficiência alocativa "
                                                                                       "no mercado."),
        "poucas": ("O monopólio natural se define por " + azb("custo médio decrescente") + " em toda a faixa da "
                   "demanda (economias de escala). Aí uma só firma produz mais barato que várias: a entrada "
                   + vd("elevaria") + " o custo, não o reduziria."),
        "destrinchando": [
            "Definição: há monopólio natural quando uma única firma atende toda a demanda a custo menor do que "
            "duas ou mais — " + azb("subaditividade de custos") + ". O caso típico: custo fixo alto e custo "
            "marginal baixo, constante ou decrescente, sempre " + vd("abaixo do custo médio") + ".",
            "Custos marginais crescentes apontariam o contrário: a partir de certo ponto, deseconomias de escala "
            "e espaço para várias firmas — característica de mercados competitivos, não de monopólio natural.",
            "Fragmentar o mercado duplicaria o custo fixo (duas redes de distribuição de água na mesma rua) e "
            "reduziria a escala de cada firma, perdendo " + azb("eficiência produtiva") + ".",
            "Por isso a resposta de política é " + azb("regular") + " o monopólio (tarifa, metas de qualidade, "
            "concessão por licitação — a “concorrência <b>pelo</b> mercado” de " + oc("Demsetz") + "), e não "
            "estimular a entrada.",
            vm("Regra-âncora: monopólio natural = CMe decrescente na faixa relevante → uma firma é o arranjo de "
               "menor custo."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Dois erros empilhados: a estrutura de custos "
                       "trocada (CMg crescente) e a política deduzida dela (entrada de várias firmas). Qualquer um "
                       "basta para o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, a entrada de novas firmas elevaria o custo médio de produção do "
            "setor.”</i> → CERTO",
            "<i>“O monopólio natural caracteriza-se por deseconomias de escala na faixa relevante da "
            "demanda.”</i> → ERRADO (inversão: economias de escala)",
        ])],
        "reescrita": ("Um monopólio natural, caracterizado por " + hl("custos médios decrescentes em toda a faixa "
                      "relevante da demanda") + ", " + hl("não justifica") + " a entrada de múltiplas empresas "
                      "para promover concorrência e eficiência alocativa no mercado" + hl(", mas sim a "
                      "regulação de uma única firma") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Monopólio natural: economias de escala em toda a faixa relevante, CMe decrescente, "
                             "CMg baixo e constante ou decrescente; mais eficiente uma única firma; a entrada "
                             "elevaria o custo médio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “eficiênciaalocativa” → “eficiência alocativa” (OCR)"],
    },
    # ------------------------------------------------------------------ E1-0693
    {
        "id": "ECO-E1-0693-1", "fonte_ref": "E1-0693", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_CLIP26,
        "rotulo_item": "Item",
        "assertiva": ("Em um monopólio, a maximização do lucro exige que o preço seja igual ao custo marginal, de "
                      "modo a expandir o consumo e aumentar o bem-estar social."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um monopólio, a maximização do lucro exige que ") + vm("o preço seja igual ao custo "
                      "marginal, de modo a expandir o consumo e aumentar o bem-estar social") + az("."),
        "poucas": ("O lucro do monopolista é máximo em " + vd("RMg = CMg") + ", com " + vd("P > CMg")
                   + ": ele restringe o consumo e gera peso morto. P = CMg é condição de eficiência, não de "
                   "lucro máximo do monopólio."),
        "destrinchando": [
            "Condição de lucro máximo de qualquer firma: " + vd("RMg = CMg") + ". Com demanda negativamente "
            "inclinada, " + vd("P > RMg") + ", logo no ótimo do monopolista " + vd("P > CMg") + ".",
            "O monopolista não tem interesse em expandir o consumo até P = CMg: as unidades entre q<sub>m</sub> "
            "e q<sub>c</sub> têm RMg < CMg e reduziriam seu lucro.",
            "Efeito sobre o bem-estar: menor quantidade, preço maior e " + azb("peso morto") + " em relação à "
            "concorrência perfeita. O item atribui ao monopolista o objetivo (bem-estar social) que é de um "
            "planejador ou regulador.",
            "Onde P = CMg aparece no monopólio: como " + azb("regra de regulação") + " (preço fixado pelo "
            "regulador) e como resultado da " + azb("discriminação perfeita") + " — em que a última unidade é "
            "vendida a P = CMg, mas sem ganho para o consumidor.",
        ],
        "dissecando": (cz("[troca de conceito · juízo indevido]") + " Troca a regra (RMg por P) e atribui ao "
                       "monopolista a motivação de “aumentar o bem-estar social”. Pista: lucro privado e "
                       "eficiência social só coincidem na concorrência perfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um monopólio, a maximização do lucro exige receita marginal igual ao custo marginal, com "
            "preço acima deste.”</i> → CERTO",
            "<i>“A regulação que impõe preço igual ao custo marginal reduz a quantidade produzida pelo "
            "monopolista.”</i> → ERRADO (inversão: aumenta a quantidade)",
        ])],
        "reescrita": ("Em um monopólio, a maximização do lucro exige que " + hl("a receita marginal seja igual ao "
                      "custo marginal, com preço acima do custo marginal, o que restringe o consumo e reduz o "
                      "bem-estar social") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "JUIZO_INDEVIDO"], "moduladores": ["exige"], "dificuldade": 1,
        "comentario_fonte": ("Condição de lucro máximo: RMg = CMg; P > RMg, logo P > CMg; peso morto e menor "
                             "bem-estar que na concorrência perfeita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0292-1 (P = CMg atribuído ao monopolista, outra fonte)", "texto_corrigido: “queo” → “que o” (OCR)"],
    },
    # ------------------------------------------------------------------ E2-L00040
    {
        "id": "ECO-E2-L00040-1", "fonte_ref": "E2-L00040", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Em um monopólio, a receita marginal é sempre superior à curva de demanda do mercado, o que "
                      "significa que o monopólio consegue reservar uma parte maior da demanda, aumentando assim "
                      "seu poder de discriminação de preços sobre os consumidores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um monopólio, a receita marginal é sempre ") + vm("superior") + az(" à curva de "
                      "demanda do mercado, ") + vm("o que significa que o monopólio consegue reservar uma parte "
                      "maior da demanda, aumentando assim seu poder de discriminação de preços sobre os "
                      "consumidores") + az("."),
        "poucas": ("A receita marginal do monopolista fica " + vd("abaixo") + " da demanda (RMg < P), porque "
                   "vender mais exige baixar o preço de todas as unidades. E isso nada tem a ver com "
                   "discriminação de preços."),
        "destrinchando": [
            "Demanda linear P = a − bQ → RT = aQ − bQ² → " + vd("RMg = a − 2bQ") + ": mesmo intercepto e "
            "inclinação " + vd("duas vezes maior") + " que a demanda. Para todo Q > 0, a RMg está abaixo da "
            "demanda; ela zera no ponto médio, onde |ε| = 1.",
            "O motivo é o " + azb("efeito-preço") + ": com preço único, a redução necessária para vender a "
            "unidade extra recai sobre todas as unidades anteriores.",
            "A segunda parte do item é " + azb("nexo indevido") + ": a posição da RMg não “reserva” demanda nem "
            "gera poder de discriminar. Discriminação de preços exige poder de mercado, identificação de "
            "consumidores ou grupos e impedimento da revenda.",
            "Curiosidade útil: sob discriminação " + azb("perfeita") + ", a RMg passa a coincidir com a demanda "
            "(cada unidade é vendida pelo seu preço sem baixar o das demais) — o oposto do que o item sugere.",
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " Inverte a posição da RMg (abaixo → acima) e ainda "
                       "pendura nela uma consequência sem relação (discriminação). Pista: “sempre superior” "
                       "contraria o primeiro gráfico de monopólio de qualquer manual."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na demanda linear, a curva de receita marginal do monopolista tem o mesmo intercepto e o dobro "
            "da inclinação da demanda.”</i> → CERTO",
            "<i>“A receita marginal do monopolista é menos inclinada que a curva de demanda.”</i> → ERRADO "
            "(inversão: é mais inclinada)",
        ])],
        "reescrita": ("Em um monopólio, a receita marginal é sempre " + hl("inferior") + " à curva de demanda do "
                      "mercado, o que significa que " + hl("o monopolista, para vender mais, precisa reduzir o "
                      "preço de todas as unidades") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("A RMg é inferior à demanda; o comentário acrescenta que o monopólio “atende apenas "
                             "uma reserva de mercado” e que a RMg tem “menor inclinação” que a demanda."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem afirma que a RMg tem inclinação menor que a "
                    "demanda (é o dobro, na demanda linear) e liga a RMg à discriminação de preços — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L00041
    {
        "id": "ECO-E2-L00041-1", "fonte_ref": "E2-L00041", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O monopólio é incapaz de alterar o custo marginal de produção, mesmo quando possui controle "
                      "total sobre o mercado, sendo, portanto, um tomador de custo que enfrenta as mesmas curvas "
                      "de custo de um mercado perfeito."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O monopólio é <u>incapaz de alterar o custo marginal</u> de produção, mesmo quando possui "
                      "controle total sobre o mercado, sendo, portanto, um <u>tomador de custo</u> que enfrenta "
                      "as mesmas curvas de custo de um mercado perfeito."),
        "poucas": ("O poder do monopolista está no lado da " + azb("demanda") + " (preço), não no dos "
                   + azb("custos") + ": suas curvas de custo vêm da tecnologia e dos preços dos insumos, como as "
                   "de qualquer firma."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "“Tomador de custo” não é termo consagrado, e a afirmação tem exceções: um monopolista "
                          "que também seja " + azb("monopsonista") + " no mercado de insumos altera o preço "
                          "destes (e, portanto, seus custos); e a tecnologia de um monopólio natural não é a de "
                          "uma firma competitiva. Mantém-se o CERTO da fonte, na leitura de que o poder de "
                          "monopólio, por si só, não desloca as curvas de custo.")],
        "destrinchando": [
            "Curvas de custo são derivadas da " + azb("função de produção") + " e dos " + azb("preços dos "
            "insumos") + ". Se o monopolista compra insumos em mercados competitivos, toma esses preços como "
            "dados — tal como a firma competitiva.",
            "O que distingue o monopólio é a receita: demanda inclinada, " + vd("RMg < P") + ". A regra de "
            "decisão RMg = CMg usa o mesmo CMg que uma firma competitiva teria com a mesma tecnologia; é isso "
            "que permite comparar monopólio e concorrência “com os mesmos custos”.",
            "O monopolista escolhe a quantidade e, com ela, o ponto da curva de CMg em que opera — mas não "
            "<b>desloca</b> a curva. Deslocá-la exigiria mudar tecnologia ou preços de insumos.",
            "Exceções que a banca pode explorar: " + azb("monopsônio") + " (poder de compra que reduz o preço do "
            "insumo); " + azb("ineficiência X") + " (sem concorrência, custos podem ficar acima do mínimo); "
            "economias de escala que só o monopólio aproveita.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " O item parece ERRADO porque “controle total sobre o mercado” "
                       "sugere poder ilimitado, inclusive sobre custos. A chave é separar receita (onde está o "
                       "poder) de custo (dado pela tecnologia). O jargão “tomador de custo” é invenção do "
                       "simulado — por isso o item é frágil."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por deter poder de mercado, o monopolista desloca para baixo sua curva de custo marginal.”</i> "
            "→ ERRADO (nexo indevido: poder de mercado atua sobre o preço do produto)",
            "<i>“Um monopsonista, ao reduzir o preço que paga pelo insumo, altera seus custos de "
            "produção.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["mesmo quando"], "dificuldade": 3,
        "comentario_fonte": ("O monopolista não altera o custo marginal; é tomador de custo; sujeito às mesmas "
                             "leis de produção e custos que uma empresa em mercado perfeito."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: “tomador de custo” é termo não consagrado; monopsônio e economias de escala "
                    "são exceções; gabarito CERTO da fonte mantido"],
    },
    # ------------------------------------------------------------------ E2-L00042
    {
        "id": "ECO-E2-L00042-1", "fonte_ref": "E2-L00042", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Embora o monopólio possa obter um lucro exorbitante no curto prazo, a entrada de novos "
                      "concorrentes devido à ausência de barreiras à entrada reduzirá gradualmente esse lucro, "
                      "similar ao que ocorre em um mercado de concorrência perfeita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Embora o monopólio possa obter um lucro exorbitante no curto prazo, ")
                   + vm("a entrada de novos concorrentes devido à ausência de barreiras à entrada reduzirá "
                        "gradualmente esse lucro, similar ao que ocorre em um mercado de concorrência perfeita")
                   + az("."),
        "poucas": ("O monopólio se define por " + azb("barreiras à entrada") + ": sem entrada, o "
                   + vd("lucro extraordinário persiste no longo prazo") + ", ao contrário da concorrência perfeita."),
        "destrinchando": [
            "Na " + azb("concorrência perfeita") + " (e na monopolística), lucro positivo atrai novas firmas, a "
            "oferta aumenta, o preço cai e o lucro econômico tende a " + vd("zero") + " no longo prazo.",
            "No monopólio, patentes, concessões exclusivas, controle de recurso-chave ou economias de escala "
            "bloqueiam esse ajuste. O lucro de monopólio pode durar enquanto durar a barreira.",
            "Lucro não é garantido: um monopolista com demanda fraca pode ter prejuízo e sair. O ponto é que, "
            "<b>havendo</b> lucro, a entrada não o dissipa.",
            "Barreiras temporárias mudam o quadro: com a expiração de uma patente (20 anos no regime da LPI "
            "brasileira), entram concorrentes — é o caso dos " + rx("medicamentos genéricos") + " no Brasil.",
        ],
        "dissecando": (cz("[troca de conceito · contradição]") + " O item enxerta no monopólio a dinâmica de "
                       "longo prazo da concorrência perfeita, apoiado numa premissa que contradiz a própria "
                       "definição (ausência de barreiras). A primeira oração, verdadeira, serve de isca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência monopolística, a livre entrada tende a eliminar o lucro econômico no longo "
            "prazo.”</i> → CERTO",
            "<i>“O monopolista sempre obtém lucro econômico positivo.”</i> → ERRADO (modulador absoluto: pode "
            "ter prejuízo se a demanda não cobrir o custo médio)",
        ])],
        "reescrita": ("Embora o monopólio possa obter um lucro exorbitante no curto prazo, " + hl("as barreiras à "
                      "entrada impedem a chegada de novos concorrentes, e esse lucro pode persistir no longo "
                      "prazo, ao contrário do") + " que ocorre em um mercado de concorrência perfeita."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": ["gradualmente"], "dificuldade": 1,
        "comentario_fonte": ("O monopólio tem barreiras à entrada (patentes, custos de entrada, controle de "
                             "recursos) e pode manter lucros no curto e no longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00043
    {
        "id": "ECO-E2-L00043-1", "fonte_ref": "E2-L00043", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A maximização do lucro em um monopólio ocorre quando a receita marginal se iguala ao custo "
                      "marginal, mas, diferentemente do mercado perfeito, o preço é significativamente mais alto "
                      "do que o custo marginal, o que leva a um mark-up elevado e a uma ineficiência alocativa no "
                      "mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A maximização do lucro em um monopólio ocorre quando a receita marginal se iguala ao custo "
                      "marginal, mas, diferentemente do mercado perfeito, o preço é <u>significativamente</u> mais "
                      "alto do que o custo marginal, o que leva a um mark-up elevado e a uma ineficiência "
                      "alocativa no mercado."),
        "poucas": (vd("RMg = CMg") + " com " + vd("P > CMg") + ": a distância entre preço e custo marginal é o "
                   + azb("markup") + ", e a produção abaixo da eficiente é a " + azb("ineficiência alocativa")
                   + " (peso morto)."),
        "destrinchando": [
            "Cadeia lógica completa: demanda inclinada → " + vd("RMg < P") + " → no ótimo RMg = CMg → "
            + vd("P > CMg") + " → quantidade menor que a competitiva → " + azb("peso morto") + ".",
            "Tamanho do markup: " + vd("(P − CMg)/P = 1/|ε|") + ". O “significativamente” depende da "
            "elasticidade: com |ε| = 1,5, o preço é o triplo do CMg; com |ε| = 10, só cerca de 11% acima.",
            "Contraste com o “mercado perfeito”: " + vd("P = RMg = CMg") + ", markup nulo, quantidade eficiente "
            "e nenhum peso morto.",
            "Eficiência alocativa (P = CMg) não se confunde com " + azb("eficiência produtiva") + " (produzir "
            "ao custo médio mínimo): o monopólio falha na primeira; na segunda, depende da escala e da pressão "
            "competitiva.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Síntese correta do equilíbrio de "
                       "monopólio. O único ponto discutível é o “significativamente”, que a banca tratou como "
                       "característico (o preço supera o CMg); a magnitude, a rigor, depende da elasticidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio, o lucro é máximo onde o preço iguala o custo marginal, o que assegura eficiência "
            "alocativa.”</i> → ERRADO (troca de conceito: regra da concorrência perfeita)",
            "<i>“Quanto mais elástica a demanda enfrentada pelo monopolista, menor o markup.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["significativamente"],
        "dificuldade": 1,
        "comentario_fonte": ("RMg = CMg; preço acima do CMg; mark-up elevado; ineficiência alocativa (peso "
                             "morto); bem-estar reduzido em relação à concorrência perfeita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “significatimente” → “significativamente” (OCR)"],
    },
    # ------------------------------------------------------------------ E2-L00237
    {
        "id": "ECO-E2-L00237-1", "fonte_ref": "E2-L00237", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_NAT,
        "rotulo_item": "Item",
        "assertiva": ("A fixação do preço igual ao custo marginal por parte de um regulador governamental em um "
                      "monopólio natural gera alocação eficiente de recursos e não compromete a sustentabilidade "
                      "financeira da empresa, dado que o custo marginal reflete o custo total médio decrescente "
                      "do setor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A fixação do preço igual ao custo marginal por parte de um regulador governamental em um "
                      "monopólio natural gera alocação eficiente de recursos e ") + vm("não compromete") + az(" a "
                      "sustentabilidade financeira da empresa, ") + vm("dado que o custo marginal reflete o custo "
                      "total médio decrescente do setor") + az("."),
        "poucas": ("Com " + azb("CMe decrescente") + ", o " + vd("CMg fica abaixo do CMe") + ". Preço = CMg é "
                   "eficiente, mas fica abaixo do custo médio: a empresa tem " + vd("prejuízo") + "."),
        "destrinchando": [
            "Matemática do custo médio: se o CMe cai com a quantidade, é porque a unidade adicional custa menos "
            "que a média — " + vd("CMg < CMe") + ". No caso típico (custo fixo F e CMg constante c), "
            "CMe = c + F/q, sempre acima de c.",
            "Preço = CMg → P < CMe → receita não cobre o custo total: prejuízo igual ao custo fixo (no "
            "exemplo do gráfico, " + vd("(4 − 2) × 100 = 200") + "). Sem subsídio, a firma sai do mercado.",
            "Alternativas regulatórias: (1) " + azb("preço = custo médio") + " (empate contábil, mas quantidade "
            "abaixo da eficiente — ponto A); (2) P = CMg com " + azb("subsídio") + " cobrindo o custo fixo; "
            "(3) " + azb("tarifa em duas partes") + " (assinatura fixa + preço por unidade = CMg); (4) "
            + azb("preços de Ramsey") + ", com margens maiores onde a demanda é menos elástica.",
            "O dilema eficiência alocativa × viabilidade financeira é o núcleo da regulação de " + rx("serviços "
            "públicos no Brasil") + " (energia, saneamento, ferrovias), em geral por tarifas baseadas no custo "
            "médio ou em incentivos (preço-teto).",
        ],
        "grafico_verso": "ECO-E2-L00237-1-V1",
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A primeira parte é verdadeira (P = CMg é "
                       "eficiente); o erro foi enxertado na consequência financeira e numa justificativa falsa "
                       "(“o CMg reflete o CMe”). Pista: custo médio decrescente implica CMg <b>abaixo</b> dele."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, a regulação pelo custo médio garante a viabilidade da firma, mas mantém "
            "a produção abaixo da eficiente.”</i> → CERTO",
            "<i>“No monopólio natural, a tarifa igual ao custo marginal gera lucro econômico à firma.”</i> → "
            "ERRADO (P = CMg < CMe gera prejuízo)",
        ])],
        "reescrita": ("A fixação do preço igual ao custo marginal por parte de um regulador governamental em um "
                      "monopólio natural gera alocação eficiente de recursos, " + hl("mas compromete") + " a "
                      "sustentabilidade financeira da empresa, " + hl("dado que, com custo total médio "
                      "decrescente, o custo marginal fica abaixo do custo médio") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("No monopólio natural, CMg < CTMe por economias de escala; P = CMg garante "
                             "eficiência alocativa, mas gera prejuízo (P < CTMe)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00238
    {
        "id": "ECO-E2-L00238-1", "fonte_ref": "E2-L00238", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_DISC,
        "rotulo_item": "Item",
        "assertiva": ("Em mercados com discriminação de preços de primeiro grau, o excedente do consumidor é "
                      "nulo, uma vez que o produtor captura integralmente o valor disposto a ser pago por cada "
                      "unidade, o que leva à mesma quantidade produzida que em concorrência perfeita, porém com "
                      "redistribuição do excedente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em mercados com discriminação de preços de primeiro grau, o <u>excedente do consumidor é "
                      "nulo</u>, uma vez que o produtor captura integralmente o valor disposto a ser pago por cada "
                      "unidade, o que leva à <u>mesma quantidade produzida que em concorrência perfeita</u>, "
                      "porém com redistribuição do excedente."),
        "poucas": ("Na " + azb("discriminação perfeita") + ", cada unidade é vendida pelo preço de reserva: "
                   + vd("EC = 0") + ", a RMg passa a ser a própria demanda e o monopolista produz até "
                   + vd("P = CMg") + " — a quantidade competitiva, sem peso morto."),
        "destrinchando": [
            "Por que a quantidade é a eficiente: vender uma unidade a mais não obriga a baixar o preço das "
            "anteriores, então a " + azb("RMg coincide com a demanda") + ". O monopolista produz enquanto o "
            "preço de reserva da próxima unidade cobrir o CMg — exatamente o ponto P = CMg.",
            "Consequência de bem-estar: o " + azb("excedente total") + " é o mesmo da concorrência perfeita "
            "(eficiência alocativa), mas todo ele vai para o produtor. O que muda é a " + azb("distribuição")
            + ", não o tamanho.",
            "Comparação com o monopólio de preço único: lá há peso morto e o consumidor retém parte do "
            "excedente; aqui o peso morto some e o excedente do consumidor também.",
            "Ressalva implícita no item: “mesma quantidade que em concorrência perfeita” supõe os mesmos custos. "
            "Na prática, a discriminação perfeita é um caso-limite (exige conhecer cada preço de reserva e "
            "impedir a revenda).",
            vm("Regra-âncora: 1º grau = eficiente na quantidade, extremo na distribuição."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " O item é verdadeiro, mas surpreende quem associa “mais poder "
                       "de monopólio” a “mais ineficiência”. A banca costuma explorar o par: eficiência alocativa "
                       "(CERTO) × bem-estar do consumidor (nulo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A discriminação de preços de primeiro grau gera peso morto maior que o do monopólio de preço "
            "único.”</i> → ERRADO (inversão: elimina o peso morto)",
            "<i>“Na discriminação de terceiro grau, o excedente do consumidor é necessariamente nulo.”</i> → "
            "ERRADO (grau trocado e modulador absoluto)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["integralmente"], "dificuldade": 2,
        "comentario_fonte": ("Na discriminação perfeita, o produtor cobra o preço máximo de cada unidade e se "
                             "apropria de todo o excedente; quantidade eficiente, como na concorrência perfeita, "
                             "com redistribuição total em favor do produtor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
