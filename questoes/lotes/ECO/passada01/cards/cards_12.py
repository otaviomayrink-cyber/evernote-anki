"""Cards da passada 01 de ECO — lote de redação 12 (teoria do consumidor: preferências, utilidade,
restrição orçamentária, escolha ótima; dois itens de 04-A)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "pref": "🧠 Preferências e axiomas",
    "util": "🎯 Utilidade e curvas de indiferença",
    "ro": "💵 Restrição orçamentária",
    "otimo": "⚖️ Escolha ótima do consumidor",
    "dem": "📊 Demanda individual e de mercado",
    "giffen": "🥔 Bens inferiores e de Giffen",
    "ers": "🔀 Efeitos renda e substituição",
}

RT = {"banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023, "cacd": False}
NIDI_JUL = {"banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025, "cacd": False}
NIDI_MAR = {"banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025, "cacd": False}
NIDI_NOV = {"banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024, "cacd": False}
ANTT = {"banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False}

CMD_RT_SOBRE = "Sobre a teoria do consumidor, avalie os itens a seguir."
CMD_RT_RESP = "A respeito da teoria do consumidor, julgue os itens a seguir."
CMD_RT_AFIRM = "A respeito da teoria do consumidor, julgue as afirmações a seguir."
CMD_RT_CONC = "Acerca dos conceitos e teorias da microeconomia, julgue os itens a seguir."
CMD_NIDI = ("Os agentes microeconômicos fazem suas escolhas de forma racional em um cenário de informações "
            "completas e simetricamente distribuídas. A respeito da Teoria do Consumidor, julgue certo ou errado "
            "(C ou E) os itens a seguir.")
CMD_NIDI_NOV = "Considerando essa informação e a teoria econômica subjacente, julgue certo ou errado (C ou E) o item a seguir."
EXC_NIDI_NOV = ("<p><i>No estudo das preferências dos consumidores, é comum assumir que ‘quanto mais de um bem, "
                "melhor’. Esse pressuposto facilita a construção de modelos teóricos na economia, como a análise da "
                "teoria do consumidor e a formulação de curvas de demanda. Contudo, esse princípio nem sempre se "
                "aplica: há bens cujo consumo excessivo pode levar a uma redução na satisfação, ou até mesmo a uma "
                "insatisfação com a aquisição de unidades adicionais.</i></p>")
CMD_ANTT = "A partir da situação hipotética precedente, julgue o item seguinte."
EXC_ANTT = ("<p>Em um modelo simplificado para representar o comportamento esperado do consumidor padrão, dois "
            "bens, X e Y, são consumidos em x unidades e y unidades, respectivamente. Esses bens são adquiridos no "
            "mercado competitivo aos preços p<sub>x</sub> e p<sub>y</sub>, respectivamente, e o consumidor tem uma "
            "renda R a ser gastada no consumo desses bens. O comportamento padrão é que o consumidor deseja "
            "maximizar a função utilidade u(x, y), que representa sua satisfação obtida pelo consumo dos bens X e "
            "Y, limitado ao seu orçamento, dado pela relação p<sub>x</sub>·x + p<sub>y</sub>·y ≤ R.</p>")
FIG_ANTT = {"ref": "IMAGEM 151", "tipo_fonte": "TEXTO", "lado": "frente",
            "acao": "texto (situação hipotética transcrita no excerto; OCR de p<sub>x</sub> e da restrição corrigido)"}

CARDS = []

# ====================================================================== bloco 1
CARDS += [
    # ------------------------------------------------------------------ E2-L01424
    {
        "id": "ECO-E2-L01424-1", "fonte_ref": "E2-L01424", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": "A respeito dos conceitos e teorias da microeconomia, julgue os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Segundo o axioma da convexidade, o consumidor sempre prefere uma cesta equilibrada do que uma "
                      "concentrada em apenas um dos bens, exceto no caso dos bens substitutos perfeitos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o axioma da convexidade, o consumidor sempre prefere uma <u>cesta equilibrada</u> do "
                      "que uma concentrada em apenas um dos bens, <u>exceto no caso dos bens substitutos "
                      "perfeitos</u>."),
        "poucas": ("A " + azb("convexidade") + " é o “gosto pela diversidade”: médias de cestas indiferentes valem "
                   "pelo menos tanto quanto os extremos. Nos " + azb("substitutos perfeitos") + " a curva de "
                   "indiferença é reta e a média vale exatamente o mesmo — daí a exceção."),
        "destrinchando": [
            "Enunciado formal: se A ~ B, então qualquer média ponderada t·A + (1 − t)·B é " + vd("pelo menos tão "
            "boa") + " quanto A e B (convexidade fraca); na versão " + azb("estrita") + ", é <b>estritamente "
            "melhor</b>. Exemplo: indiferente entre (10 maçãs, 0 bananas) e (0, 10), o consumidor prefere (5, 5).",
            "Tradução gráfica: curvas de indiferença " + azb("convexas em relação à origem") + " e " + azb("TMS "
            "decrescente") + " — quanto mais x a pessoa já tem, menos y aceita entregar por mais uma unidade de x. "
            "Cestas balanceadas ficam “para dentro” da curva e, portanto, numa curva mais alta.",
            "Substitutos perfeitos (u = ax + by): curva reta, TMS constante. A média de duas cestas da mesma reta "
            "está <b>na mesma reta</b> — indiferente, não preferida. A convexidade vale só na forma fraca; por "
            "isso o consumidor não tem predileção por equilíbrio e costuma acabar numa solução de canto.",
            "Complementares perfeitos (u = mín{ax, by}) também são só fracamente convexos (ao longo de um mesmo "
            "braço do L a média é indiferente); o item não diz que os substitutos são a <i>única</i> exceção.",
            vm("Regra-âncora: convexidade ⇔ TMS decrescente ⇔ preferência pela média; reta = convexidade fraca."),
        ],
        "dissecando": (cz("[literalidade · exceção]") + " O item reproduz a definição de manual e acrescenta a "
                       "exceção correta. O “sempre” assusta, mas está amarrado à ressalva final; quem lê “exceto "
                       "substitutos perfeitos” como erro (achando que deveria ser complementares) marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…exceto no caso dos bens complementares perfeitos, cujas curvas de indiferença são retas.”</i> → "
            "ERRADO (troca de conceito: retas são dos substitutos)",
            "<i>“A convexidade das preferências implica taxa marginal de substituição decrescente ao longo da curva "
            "de indiferença.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "EXCECAO"], "moduladores": ["sempre", "exceto"], "dificuldade": 1,
        "comentario_fonte": ("Convexidade = preferência por diversidade; curvas convexas; média de duas cestas da "
                             "mesma curva é pelo menos tão boa; exceção: substitutos perfeitos, curvas retas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 335", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (lista de axiomas no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01460
    {
        "id": "ECO-E2-L01460-1", "fonte_ref": "E2-L01460", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_RT_SOBRE,
        "rotulo_item": "Item",
        "assertiva": ("As preferências dos consumidores são representadas por curvas de indiferença, em que cada uma "
                      "contém as possíveis combinações de bens e serviços que trazem a mesma satisfação. "
                      "Graficamente, as curvas de indiferença são positivamente inclinadas, o que significa dizer que "
                      "as combinações representadas mais à direita proporcionam mais satisfação aos consumidores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As preferências dos consumidores são representadas por curvas de indiferença, em que cada uma "
                      "contém as possíveis combinações de bens e serviços que trazem a mesma satisfação. "
                      "Graficamente, as curvas de indiferença são ") + vm("positivamente inclinadas, o que "
                      "significa dizer que") + az(" as combinações representadas mais à direita proporcionam mais "
                      "satisfação aos consumidores."),
        "poucas": ("Com dois “bens” (mais é melhor), a curva de indiferença é " + azb("negativamente inclinada") +
                   ": para manter a satisfação, ganhar x exige perder y. Que curvas mais afastadas valem mais é "
                   "verdade, mas não decorre da inclinação."),
        "destrinchando": [
            "Por que a inclinação é negativa: pela " + azb("monotonicidade") + ", mais de qualquer bem aumenta a "
            "utilidade. Se uma curva subisse para a direita, a cesta de cima teria mais x <b>e</b> mais y que a de "
            "baixo e não poderia ser indiferente a ela. Para ficar no mesmo nível, ganho de x precisa ser "
            "compensado por perda de y.",
            "A inclinação, em módulo, é a " + azb("taxa marginal de substituição") + ": TMS = UMg<sub>x</sub> / "
            "UMg<sub>y</sub>, quanto de y o consumidor cede por uma unidade extra de x. Com preferências convexas, "
            "ela cai ao longo da curva.",
            "O que gera mais satisfação é estar numa " + azb("curva mais afastada da origem") + " (mapa de "
            "indiferença: U₁ < U₂ < U₃) — consequência da monotonicidade, não de a curva ser crescente. Ao longo "
            "de uma <b>mesma</b> curva, ir para a direita não muda nada: a satisfação é constante por definição.",
            "Quando a curva é positivamente inclinada? Quando um dos itens é um " + azb("mal") + " (poluição, "
            "horas de trabalho, risco): para aceitar mais do mal, o consumidor exige mais do bem. É a exceção que "
            "a banca pode cobrar.",
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A 1ª frase é a definição correta; o erro foi "
                       "enxertado na geometria (“positivamente”) e amarrado, com “o que significa dizer que”, a uma "
                       "conclusão que soa certa. Pista: se a curva liga cestas de <b>mesma</b> satisfação, não pode "
                       "ao mesmo tempo indicar que pontos à direita satisfazem mais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se um dos bens for um mal, como a poluição, as curvas de indiferença serão positivamente "
            "inclinadas.”</i> → CERTO",
            "<i>“Curvas de indiferença mais afastadas da origem representam níveis menores de utilidade.”</i> → "
            "ERRADO (inversão: mais afastadas = mais utilidade)",
        ])],
        "reescrita": ("As preferências dos consumidores são representadas por curvas de indiferença, em que cada uma "
                      "contém as possíveis combinações de bens e serviços que trazem a mesma satisfação. "
                      "Graficamente, as curvas de indiferença são " + hl("negativamente inclinadas, e as curvas "
                      "mais afastadas da origem") + " proporcionam mais satisfação aos consumidores."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Curvas de indiferença são negativamente inclinadas (trade-off, TMS); curvas mais "
                             "afastadas da origem representam maior utilidade; a 1ª parte da assertiva está certa."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 351", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mapa de indiferença U₁ = 25, U₂ = 50, U₃ = 100 descrito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01461
    {
        "id": "ECO-E2-L01461-1", "fonte_ref": "E2-L01461", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_RT_SOBRE,
        "rotulo_item": "Item",
        "assertiva": ("Se um consumidor gosta de refrigerante, mas não faz nenhuma distinção entre as diferentes "
                      "marcas disponíveis no mercado, então, para esse consumidor, o mapa de indiferença entre duas "
                      "marcas quaisquer é formado por linhas retas paralelas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um consumidor gosta de refrigerante, mas <u>não faz nenhuma distinção</u> entre as "
                      "diferentes marcas disponíveis no mercado, então, para esse consumidor, o mapa de indiferença "
                      "entre duas marcas quaisquer é formado por <u>linhas retas paralelas</u>."),
        "poucas": ("Marcas indistinguíveis são " + azb("substitutos perfeitos") + ": u = x + y. Cada curva de "
                   "indiferença é x + y = k — retas de inclinação " + vd("−1") + ", paralelas entre si."),
        "destrinchando": [
            "“Não faz distinção” = um litro da marca A vale exatamente um litro da marca B. Só importa o total: "
            + vd("u(x, y) = x + y") + ". A curva de nível u = k é a reta y = k − x.",
            "Inclinação = −" + azb("TMS") + " = −UMg<sub>x</sub>/UMg<sub>y</sub> = −1/1 = " + vd("−1") + " em "
            "qualquer ponto e em qualquer curva: por isso as retas são <b>paralelas</b>; muda apenas o intercepto "
            "(k = 2, 4, 6…), e retas mais altas valem mais.",
            "Generalização: substitutos perfeitos não exigem troca 1 por 1. Se uma lata de 600 ml substitui duas "
            "de 300 ml, u = 2x + y: retas paralelas de inclinação −2. O que define o caso é a " + azb("TMS "
            "constante") + ", não a proporção 1:1.",
            "Contraste com " + azb("complementares perfeitos") + " (sapato esquerdo e direito, u = mín{x, y}): "
            "curvas em L, com vértice sobre o raio x = y. E com o caso usual: curvas convexas, TMS decrescente.",
            "Consequência para a escolha: com retas, a solução costuma ser de " + azb("canto") + " — o consumidor "
            "compra só a marca mais barata (por unidade de satisfação).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item descreve substitutos perfeitos sem dizer o nome, por meio "
                       "de um exemplo cotidiano. A pegadinha está em “paralelas”: quem pensa que cada curva poderia "
                       "ter inclinação diferente hesita. Com TMS constante, paralelismo é automático."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o mapa de indiferença entre duas marcas quaisquer é formado por curvas em formato de L.”</i> → "
            "ERRADO (troca de conceito: L é de complementares perfeitos)",
            "<i>“…as curvas de indiferença são retas, mas sua inclinação diminui à medida que o consumidor se afasta "
            "da origem.”</i> → ERRADO (a TMS é constante: retas paralelas)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["quaisquer"], "dificuldade": 1,
        "comentario_fonte": ("Marcas indistintas = substitutos perfeitos; TMS constante; u = x + y; curvas x + y = k, "
                             "retas paralelas de inclinação −1."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 352", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (substitutos × complementares perfeitos descritos no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01462
    {
        "id": "ECO-E2-L01462-1", "fonte_ref": "E2-L01462", "destino": "04", "subtema": H2["ro"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_RT_SOBRE,
        "rotulo_item": "Item",
        "assertiva": ("Os aumentos recentes do preço da energia elétrica deslocam a restrição orçamentária dos "
                      "consumidores para baixo, porém, não alteram a sua inclinação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os aumentos recentes do preço da energia elétrica ") + vm("deslocam") + az(" a restrição "
                      "orçamentária dos consumidores ") + vm("para baixo, porém, não alteram a sua inclinação")
                   + az("."),
        "poucas": ("Mudar o preço de <b>um</b> bem muda o " + azb("preço relativo") + " e, portanto, a inclinação "
                   "(−p<sub>E</sub>/p<sub>O</sub>): a reta " + azb("gira") + " para dentro em torno do intercepto "
                   "do outro bem. Deslocamento paralelo é efeito de renda ou de alta proporcional de todos os "
                   "preços."),
        "destrinchando": [
            "Restrição com energia (E) e “outros bens” (O): " + vd("p<sub>E</sub>·E + p<sub>O</sub>·O = R") + ". "
            "Interceptos: R/p<sub>O</sub> no eixo de O e R/p<sub>E</sub> no eixo de E. Inclinação: "
            + vd("−p<sub>E</sub>/p<sub>O</sub>") + " — o custo de oportunidade de 1 kWh em outros bens.",
            "Se p<sub>E</sub> sobe: o intercepto de O <b>não muda</b> (quem não consome energia compra o mesmo "
            "de outros bens); o de E encolhe; a reta fica mais " + azb("íngreme") + ". É uma " + azb("rotação") +
            " para dentro, não uma translação.",
            "Tabela de choques: ↑ ou ↓ da renda → " + azb("deslocamento paralelo") + "; ↑ do preço de um bem → "
            "rotação em torno do intercepto do outro; ↑ de todos os preços na mesma proporção ≡ ↓ da renda → "
            "paralelo; preços e renda multiplicados pelo mesmo fator → nada muda (a restrição é homogênea de grau "
            "zero).",
            "O conjunto orçamentário encolhe — nesse sentido frouxo a reta “desce” —, mas a parte decisiva do "
            "item, “não alteram a sua inclinação”, é falsa.",
            vm("Regra-âncora: renda move a reta em paralelo; preço relativo gira a reta."),
        ],
        "grafico_verso": "ECO-E2-L01462-1-V1",
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " O item atribui ao preço de um bem o efeito "
                       "típico de uma <b>queda de renda</b> (reta paralela para baixo). O “porém” cria a sensação de "
                       "ressalva técnica. Pista: preço de um só bem ⇒ preço relativo mudou ⇒ inclinação mudou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução da renda nominal dos consumidores desloca a restrição orçamentária para baixo, sem "
            "alterar sua inclinação.”</i> → CERTO",
            "<i>“Um aumento de 10% em todos os preços e de 10% na renda reduz o conjunto de cestas factíveis.”</i> → "
            "ERRADO (restrição homogênea de grau zero: nada muda)",
        ])],
        "reescrita": ("Os aumentos recentes do preço da energia elétrica " + hl("fazem girar") + " a restrição "
                      "orçamentária dos consumidores " + hl("para dentro, em torno do intercepto dos outros bens, "
                      "e alteram") + " a sua inclinação."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["porém"], "dificuldade": 1,
        "comentario_fonte": ("Inclinação = −p₁/p₂; alta de preço de um bem torna a reta mais íngreme e reduz o "
                             "poder de compra; o erro está em “não alteram a sua inclinação”."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 353", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01462-1-V1, rotação da restrição)"},
                          {"ref": "IMAGEM 354", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01463
    {
        "id": "ECO-E2-L01463-1", "fonte_ref": "E2-L01463", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_RT_SOBRE,
        "rotulo_item": "Item",
        "assertiva": ("A maximização da utilidade do consumidor requer que o benefício marginal decorrente do "
                      "consumo de um determinado bem seja igual ao seu preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A maximização da utilidade do consumidor requer que ") + vm("o benefício marginal decorrente "
                      "do consumo de um determinado bem seja igual ao seu preço") + az("."),
        "poucas": ("Na teoria da utilidade, a condição de ótimo é " + vd("UMg<sub>x</sub>/p<sub>x</sub> = "
                   "UMg<sub>y</sub>/p<sub>y</sub>") + " (igual utilidade por real em todos os bens), e não "
                   "“UMg = preço” — utilidade e reais não têm a mesma unidade."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "se “benefício marginal” for lido em <b>reais</b> (disposição a pagar pela última "
                          "unidade), a regra “compra-se até BMg = p” é a formulação de manual introdutório "
                          "(" + oc("Mankiw") + ", “pessoas racionais pensam na margem”) e o item seria CERTO. O "
                          "gabarito do professor (ERRADO) supõe benefício medido em utilidade; numa prova "
                          "CEBRASPE, a redação desse item seria recorrível.")],
        "destrinchando": [
            "Problema do consumidor: máx u(x, y) sujeito a p<sub>x</sub>x + p<sub>y</sub>y = R. Condição de 1ª "
            "ordem (Lagrange): UMg<sub>x</sub> = λp<sub>x</sub> e UMg<sub>y</sub> = λp<sub>y</sub>, em que "
            + azb("λ") + " é a utilidade marginal da renda.",
            "Daí as duas formas equivalentes do ótimo interior: " + vd("UMg<sub>x</sub>/p<sub>x</sub> = "
            "UMg<sub>y</sub>/p<sub>y</sub> = λ") + " (" + azb("lei da equimarginalidade") + ", de "
            + oc("Gossen") + ") e " + vd("TMS = UMg<sub>x</sub>/UMg<sub>y</sub> = p<sub>x</sub>/p<sub>y</sub>")
            + " (tangência entre curva de indiferença e reta orçamentária).",
            "“UMg = p” só valeria se λ = 1, isto é, se a utilidade fosse medida em reais. Por isso, quando a "
            "literatura fala em “benefício marginal = preço”, está medindo o benefício em dinheiro (disposição a "
            "pagar), não em útiles.",
            "Intuição da equimarginalidade: se o último real em x rende mais utilidade que o último real em y, "
            "vale tirar um real de y e pô-lo em x; a realocação para quando os retornos por real se igualam.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca a condição relativa (UMg por real igual entre "
                       "bens) por uma igualdade absoluta entre utilidade e preço. 🔥 Em itens de teoria do "
                       "consumidor, desconfie de qualquer condição de ótimo que olhe <b>um bem isolado</b>: o ótimo "
                       "é sempre comparação entre bens (ou com λ)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No ótimo interior, a utilidade marginal por unidade monetária gasta é a mesma para todos os "
            "bens.”</i> → CERTO",
            "<i>“No ótimo, a utilidade marginal de cada bem é igual para todos os bens consumidos.”</i> → ERRADO "
            "(faltou dividir pelos preços)",
        ])],
        "reescrita": ("A maximização da utilidade do consumidor requer que " + hl("a utilidade marginal por unidade "
                      "monetária gasta em um determinado bem seja igual à dos demais bens") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Condição correta: UMg₁/P₁ = UMg₂/P₂ (ou TMS = razão de preços); igualar benefício "
                             "marginal ao preço não é a condição de equilíbrio. Parte das respostas empilhadas "
                             "considerava a assertiva “fundamentalmente correta”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 355", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 356", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (tangência descrita no 📖)"},
                          {"ref": "IMAGEM 357", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 358", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (UMgₓ/Pₓ = UMgᵧ/Pᵧ no 📖)"}],
        "alertas": ["contestavel: lido em unidades monetárias (disposição a pagar), BMg = p é condição de ótimo de "
                    "manual; gabarito ERRADO mantido (fonte e professor), com ⚠️ no card",
                    "qualidade_fonte: respostas de IA empilhadas no verso davam a assertiva como correta; fundidas "
                    "pelo gabarito do professor"],
    },
]

# ====================================================================== bloco 2
CARDS += [
    # ------------------------------------------------------------------ E2-L01521
    {
        "id": "ECO-E2-L01521-1", "fonte_ref": "E2-L01521", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_RT_RESP,
        "rotulo_item": "Item",
        "assertiva": ("Se um consumidor que consome 2 bens normais está em equilíbrio, e estes bens são complementares "
                      "perfeitos, pode-se dizer que um aumento do preço de um dos bens levará o consumidor a reduzir "
                      "o consumo deste bem e elevar a quantidade consumida do outro bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um consumidor que consome 2 bens normais está em equilíbrio, e estes bens são complementares "
                      "perfeitos, pode-se dizer que um aumento do preço de um dos bens levará o consumidor a reduzir "
                      "o consumo deste bem e ") + vm("elevar") + az(" a quantidade consumida do outro bem."),
        "poucas": ("Complementares perfeitos são consumidos em " + azb("proporção fixa") + ": a alta do preço de um "
                   "encarece o “par” e o consumidor reduz <b>os dois</b> na mesma proporção. Aumentar o outro bem "
                   "seria comportamento de substitutos."),
        "destrinchando": [
            "Preferências de " + oc("Leontief") + ": u = mín{ax₁, bx₂}. Curvas de indiferença em " + azb("L") +
            ", com vértice sobre o raio ax₁ = bx₂. Unidades de um bem sem o par correspondente não acrescentam "
            "nada (sapato esquerdo sem o direito).",
            "O ótimo fica sempre no vértice: o consumidor compra x₁ = x₂ (no caso 1:1) e gasta toda a renda: "
            + vd("x₁ = x₂ = R/(p₁ + p₂)") + ". Se p₁ sobe, o denominador sobe e " + vd("ambos caem") + ".",
            "Decomposição: o " + azb("efeito substituição") + " é <b>nulo</b> (a curva em L não permite trocar um "
            "bem pelo outro mantendo a utilidade); toda a variação é " + azb("efeito renda") + ". Como os bens são "
            "normais, menos renda real ⇒ menos dos dois.",
            "Elasticidade-preço cruzada " + vd("negativa") + ": ↑p₁ ⇒ ↓x₂. É a marca dos complementares (carro e "
            "gasolina, café e açúcar para quem adoça sempre igual).",
        ],
        "grafico_verso": "ECO-E2-L01521-1-V1",
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " A 1ª consequência (reduzir o bem que encareceu) "
                       "está certa; o erro é o enxerto “e elevar a quantidade consumida do outro”, que descreve "
                       "substitutos. O “2 bens normais” é distração — na verdade reforça que o efeito renda reduz "
                       "os dois."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…um aumento do preço de um dos bens levará o consumidor a reduzir o consumo de ambos, mantendo a "
            "proporção entre eles.”</i> → CERTO",
            "<i>“…no caso de complementares perfeitos, o efeito substituição de uma variação de preço é negativo e "
            "de grande magnitude.”</i> → ERRADO (o efeito substituição é nulo)",
        ])],
        "reescrita": ("Se um consumidor que consome 2 bens normais está em equilíbrio, e estes bens são complementares "
                      "perfeitos, pode-se dizer que um aumento do preço de um dos bens levará o consumidor a reduzir "
                      "o consumo deste bem e " + hl("reduzir, na mesma proporção,") + " a quantidade consumida do "
                      "outro bem."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["pode-se dizer"], "dificuldade": 1,
        "comentario_fonte": ("Complementares perfeitos: proporções fixas; alta do preço de um reduz o consumo de "
                             "ambos na mesma proporção; trecho errado “elevar a quantidade consumida do outro bem”."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 405", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (painel de complementares em ECO-E2-L01521-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01523
    {
        "id": "ECO-E2-L01523-1", "fonte_ref": "E2-L01523", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_RT_RESP,
        "rotulo_item": "Item",
        "assertiva": ("Suponha um consumidor que consome 2 bens que são substitutos perfeitos. O bem 1 tem uma "
                      "utilidade marginal de 1, e o bem 2 tem uma utilidade marginal de 2. Se o preço do bem 2 for "
                      "maior que o dobro do preço do bem 1, o consumidor gastará toda sua renda no bem 1."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Suponha um consumidor que consome 2 bens que são substitutos perfeitos. O bem 1 tem uma "
                      "utilidade marginal de 1, e o bem 2 tem uma utilidade marginal de 2. Se o preço do bem 2 for "
                      "<u>maior que o dobro</u> do preço do bem 1, o consumidor gastará <u>toda sua renda no bem "
                      "1</u>."),
        "poucas": ("Com substitutos perfeitos vence o bem de maior " + azb("UMg por real") + ": 1/p₁ > 2/p₂ ⇔ "
                   + vd("p₂ > 2p₁") + " — exatamente a condição do item. Solução de canto no bem 1."),
        "destrinchando": [
            "Utilidade: " + vd("u = x₁ + 2x₂") + " (UMg constantes 1 e 2). Curvas de indiferença retas com "
            "inclinação −UMg₁/UMg₂ = −1/2: o consumidor troca 2 unidades do bem 1 por 1 do bem 2.",
            "Regra de decisão: compara-se UMg/p de cada bem. Bem 1 rende 1/p₁ útil por real; bem 2 rende 2/p₂. "
            "Se " + vd("1/p₁ > 2/p₂") + ", multiplicando por p₁p₂: " + vd("p₂ > 2p₁") + ". Todo real vai para o "
            "bem 1: x₁ = R/p₁, x₂ = 0.",
            "Leitura gráfica: inclinação da reta orçamentária (p₁/p₂ < 1/2) menor que a da curva de indiferença "
            "(1/2): a reta é mais “achatada” que as curvas, e a curva mais alta é tocada no intercepto do eixo do "
            "bem 1.",
            "Os outros dois casos: p₂ < 2p₁ → tudo no bem 2; " + vd("p₂ = 2p₁") + " → a reta orçamentária "
            "coincide com uma curva de indiferença e <b>qualquer</b> cesta sobre ela é ótima.",
            vm("Regra-âncora: substitutos perfeitos → compare UMg/p; ganha tudo quem rende mais por real."),
        ],
        "dissecando": (cz("[detalhe]") + " Item de conta: a banca aposta que o candidato compare só preços (bem 1 "
                       "é mais barato, ok) ou só utilidades (bem 2 “vale o dobro”, logo seria escolhido). A pista é "
                       "o “dobro”, que espelha a razão das UMg."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o preço do bem 2 for exatamente o dobro do preço do bem 1, o consumidor gastará toda sua renda "
            "no bem 1.”</i> → ERRADO (com p₂ = 2p₁ toda cesta da reta é ótima)",
            "<i>“Se o preço do bem 2 for 1,5 vez o do bem 1, o consumidor gastará toda sua renda no bem 2.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["toda"], "dificuldade": 1,
        "comentario_fonte": ("Substitutos perfeitos: escolhe o bem com maior UMg/p; 1/P₁ > 2/P₂ ⇔ P₂ > 2P₁; toda a "
                             "renda no bem 1."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 408", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01616
    {
        "id": "ECO-E2-L01616-1", "fonte_ref": "E2-L01616", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_RT_AFIRM,
        "rotulo_item": "Item",
        "assertiva": ("Bens que apresentam nível de quantidade consumida a partir da qual a utilidade marginal se "
                      "torna negativa são chamados de bens de consumo saciado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Bens que apresentam nível de quantidade consumida a partir da qual a <u>utilidade marginal se "
                      "torna negativa</u> são chamados de bens de consumo saciado."),
        "poucas": ("Há " + azb("saciedade") + " quando a utilidade total atinge um máximo: ali a UMg é " + vd("zero")
                   + " e, dali em diante, cada unidade extra " + vd("reduz") + " a satisfação (UMg < 0)."),
        "destrinchando": [
            azb("Utilidade marginal") + " = acréscimo de utilidade total (UT) trazido pela última unidade: UMg = "
            "ΔUT/Δq, a inclinação da curva de UT.",
            "Trajetória típica (lei da " + azb("utilidade marginal decrescente") + ", de " + oc("Gossen") + "): "
            "UMg positiva e caindo → UT cresce a taxas decrescentes; UMg = 0 → UT no " + azb("ponto de "
            "saciedade") + " (máximo); UMg < 0 → UT cai. A pizza é o exemplo de sala: a 1ª fatia é ótima, a 8ª "
            "faz mal.",
            "Esses bens violam a " + azb("monotonicidade") + " (“mais é melhor”) depois do ponto de saciedade: na "
            "margem, viram “males”. O consumidor racional nunca escolhe ficar além dele — nem de graça.",
            "Atenção à diferença: UMg <b>decrescente</b> (vale para quase todo bem e não implica saciedade) × UMg "
            "<b>negativa</b> (só depois do ponto de saciedade). Itens que confundem as duas aparecem com "
            "frequência.",
        ],
        "grafico_verso": "ECO-E2-L01616-1-V1",
        "dissecando": (cz("[literalidade]") + " Definição de manual com nome pouco usual (“bens de consumo "
                       "saciado”), o que gera insegurança. O núcleo — “UMg se torna negativa a partir de certa "
                       "quantidade” — é exatamente o que caracteriza o ponto de saciedade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens de consumo saciado são aqueles cuja utilidade marginal é decrescente.”</i> → ERRADO (troca de "
            "conceito: decrescente ≠ negativa)",
            "<i>“No ponto de saciedade, a utilidade total é máxima e a utilidade marginal é nula.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Bens saciados: UMg torna-se negativa após certo nível de consumo (pizza, alimentos, "
                             "remédios); UT máxima quando UMg = 0 (gráfico com saciação em Q = 6, UT = 150)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 457", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01616-1-V1, UT máxima 150 em Q = 6)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01617
    {
        "id": "ECO-E2-L01617-1", "fonte_ref": "E2-L01617", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_RT_AFIRM,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o axioma da transitividade, o consumidor é capaz de comparar todas as cestas de bens "
                      "disponíveis no mercado e ordená-las de acordo com suas preferências."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o axioma da ") + vm("transitividade") + az(", o consumidor é capaz de comparar todas "
                      "as cestas de bens disponíveis no mercado e ordená-las de acordo com suas preferências."),
        "poucas": ("Comparar quaisquer cestas é a " + azb("completude") + ". A " + azb("transitividade") + " é a "
                   "coerência da ordem: se A ≿ B e B ≿ C, então A ≿ C."),
        "destrinchando": [
            "Os axiomas de " + azb("racionalidade") + " das preferências: (1) " + azb("completude") + " — para "
            "quaisquer A e B, A ≿ B, B ≿ A ou ambos (indiferença): não há cestas incomparáveis; (2) "
            + azb("reflexividade") + " — A ≿ A; (3) " + azb("transitividade") + " — A ≿ B e B ≿ C ⇒ A ≿ C.",
            "Completude + transitividade = " + azb("ordenação") + " completa e coerente. Com continuidade, ela "
            "pode ser representada por uma função de utilidade (ordinal).",
            "Hipóteses de “bom comportamento”, que vêm depois: " + azb("monotonicidade") + " (mais é melhor) e "
            + azb("convexidade") + " (gosto pela diversidade).",
            "Por que a transitividade importa: sem ela haveria ciclos (A ≻ B ≻ C ≻ A) e o consumidor poderia ser "
            "explorado numa “bomba de dinheiro” (pagaria para trocar C por B, B por A, A por C…). Graficamente, "
            "é ela que impede curvas de indiferença de se cruzarem.",
            vm("Regra-âncora: completude = comparar; transitividade = ordenar sem contradição."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Descreve a completude e põe o nome da transitividade. A "
                       "palavra “ordená-las” ajuda o erro a passar, porque ordenar lembra coerência; o núcleo, porém, "
                       "é “capaz de comparar todas as cestas”. 🔥 Troca de rótulo entre axiomas é campeã em "
                       "simulados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o axioma da completude, o consumidor é capaz de comparar quaisquer duas cestas de "
            "bens.”</i> → CERTO",
            "<i>“A transitividade das preferências garante que curvas de indiferença tenham inclinação "
            "negativa.”</i> → ERRADO (troca de conceito: isso é a monotonicidade)",
        ])],
        "reescrita": ("Segundo o axioma da " + hl("completude") + ", o consumidor é capaz de comparar todas as cestas "
                      "de bens disponíveis no mercado e ordená-las de acordo com suas preferências."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["todas"], "dificuldade": 1,
        "comentario_fonte": ("O axioma descrito é a completude; transitividade: se A ≻ B e B ≻ C, então A ≻ C."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 458", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quatro axiomas no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01619
    {
        "id": "ECO-E2-L01619-1", "fonte_ref": "E2-L01619", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_RT_AFIRM,
        "rotulo_item": "Item",
        "assertiva": ("Se a utilidade marginal do bem A é de 2 e a do bem B é de 1, e os preços destes bens são "
                      "respectivamente $1 e $2, o consumidor deverá aumentar o consumo de A e diminuir o de B."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a utilidade marginal do bem A é de 2 e a do bem B é de 1, e os preços destes bens são "
                      "respectivamente $1 e $2, o consumidor deverá <u>aumentar o consumo de A e diminuir o de "
                      "B</u>."),
        "poucas": ("UMg<sub>A</sub>/p<sub>A</sub> = " + vd("2") + " útil por real; UMg<sub>B</sub>/p<sub>B</sub> = "
                   + vd("0,5") + ". O último real em A rende quatro vezes mais: realocar de B para A aumenta a "
                   "utilidade."),
        "destrinchando": [
            "Condição de ótimo interior: " + vd("UMg<sub>A</sub>/p<sub>A</sub> = UMg<sub>B</sub>/p<sub>B</sub>")
            + ". Aqui 2/1 = 2 > 1/2 = 0,5: o consumidor <b>não</b> está no ótimo.",
            "Experimento mental: tirar $1 de B custa 0,5 útil (meia unidade de B); pôr esse $1 em A rende 2 úteis. "
            "Ganho líquido de " + vd("1,5") + " útil sem gastar um centavo a mais.",
            "O ajuste se esgota sozinho: ao consumir mais A, UMg<sub>A</sub> cai; ao consumir menos B, "
            "UMg<sub>B</sub> sobe (utilidade marginal decrescente). A realocação para quando as razões se igualam.",
            "Leitura gráfica: TMS = UMg<sub>A</sub>/UMg<sub>B</sub> = 2 > p<sub>A</sub>/p<sub>B</sub> = 0,5. O "
            "consumidor valoriza A mais do que o mercado cobra por ele: a curva de indiferença corta a reta "
            "orçamentária, e o ótimo está mais adiante, na direção de mais A.",
        ],
        "dissecando": (cz("[detalhe]") + " Item numérico simples, mas com a armadilha clássica: quem compara só as "
                       "utilidades marginais (2 > 1) ou só os preços chega à resposta certa por acaso e erra a "
                       "variante seguinte. O que decide é a razão UMg/p."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a UMg de A é 4 e a de B é 1, e os preços são $4 e $1, o consumidor deverá aumentar o consumo de "
            "A.”</i> → ERRADO (4/4 = 1/1: já está no ótimo)",
            "<i>“Se UMg<sub>A</sub>/p<sub>A</sub> > UMg<sub>B</sub>/p<sub>B</sub>, a TMS de A por B supera a razão "
            "de preços p<sub>A</sub>/p<sub>B</sub>.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["deverá"], "dificuldade": 1,
        "comentario_fonte": ("UMgA/PA = 2 > UMgB/PB = 0,5; o consumidor deve realocar gasto de B para A até "
                             "igualar as razões."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 460", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 461", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (tangência descrita no 📖)"},
                          {"ref": "IMAGEM 462", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (TMS = razão de preços no 📖)"},
                          {"ref": "IMAGEM 463", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": [],
    },
]

# ====================================================================== bloco 3
CARDS += [
    # ------------------------------------------------------------------ E2-L01690
    {
        "id": "ECO-E2-L01690-1", "fonte_ref": "E2-L01690", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("Se a mudança no preço relativo de 2 bens leva a uma situação em que a utilidade marginal do bem "
                      "A dividida por seu preço é menor que a utilidade marginal do bem B dividida pelo preço de B, o "
                      "consumidor reduzirá a quantidade do bem A e aumentará a do bem B."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a mudança no preço relativo de 2 bens leva a uma situação em que a utilidade marginal do bem "
                      "A dividida por seu preço é <u>menor</u> que a utilidade marginal do bem B dividida pelo preço de "
                      "B, o consumidor <u>reduzirá a quantidade do bem A e aumentará a do bem B</u>."),
        "poucas": ("Se " + vd("UMg<sub>A</sub>/p<sub>A</sub> < UMg<sub>B</sub>/p<sub>B</sub>") + ", o último real "
                   "rende mais em B: o consumidor tira gasto de A e põe em B até as razões se igualarem."),
        "destrinchando": [
            "O ótimo interior exige " + vd("UMg<sub>A</sub>/p<sub>A</sub> = UMg<sub>B</sub>/p<sub>B</sub>") +
            " (" + azb("equimarginalidade") + "). Uma mudança de preços relativos quebra a igualdade e dispara a "
            "realocação.",
            "Exemplo: p<sub>A</sub> sobe de 1 para 2 com UMg<sub>A</sub> = UMg<sub>B</sub> = 4 e p<sub>B</sub> = "
            "2. Antes, 4/1 > 4/2 (já pendia para A); depois, 4/2 = 4/2. Se p<sub>A</sub> fosse a 4, viria 1 < 2: "
            "reduz A, aumenta B.",
            "Por que a realocação converge: com " + azb("utilidade marginal decrescente") + ", comprar menos A "
            "eleva UMg<sub>A</sub> e comprar mais B reduz UMg<sub>B</sub>; as razões caminham uma para a outra.",
            "Mesma ideia em linguagem gráfica: UMg<sub>A</sub>/UMg<sub>B</sub> = TMS < p<sub>A</sub>/p<sub>B</sub> "
            "— o consumidor valoriza A menos do que o mercado cobra; desloca-se ao longo da reta orçamentária em "
            "direção a mais B até a " + azb("tangência") + ".",
            "Ressalva teórica: vale para o caso usual (preferências convexas, solução interior). Em substitutos "
            "perfeitos a desigualdade persiste e leva a uma solução de canto (só B).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item reescreve a regra de equimarginalidade com a desigualdade "
                       "no sentido “menor” para testar se o candidato inverte a direção da realocação. Pista: segue o "
                       "real para onde ele rende mais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o consumidor aumentará a quantidade do bem A e reduzirá a do bem B, até igualar as utilidades "
            "marginais.”</i> → ERRADO (inversão; e o que se iguala são as UMg por real, não as UMg)",
            "<i>“Na situação descrita, a taxa marginal de substituição de A por B é inferior à razão "
            "p<sub>A</sub>/p<sub>B</sub>.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Equilíbrio em UMgA/PA = UMgB/PB; se UMgA/PA < UMgB/PB, reduz A e aumenta B até a "
                             "igualdade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 494", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 495", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (tangência descrita no 📖)"},
                          {"ref": "IMAGEM 496", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01691
    {
        "id": "ECO-E2-L01691-1", "fonte_ref": "E2-L01691", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("Se dois bens A e B são complementares perfeitos, o aumento do preço de A com o preço de B "
                      "constante, fará o consumidor reduzir seu consumo mais rapidamente o consumo de A que o de B."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se dois bens A e B são complementares perfeitos, o aumento do preço de A com o preço de B "
                      "constante, fará o consumidor reduzir seu consumo ") + vm("mais rapidamente o consumo de A que "
                      "o de B") + az("."),
        "poucas": ("Em " + azb("complementares perfeitos") + " a proporção é fixa: o consumidor reduz A e B "
                   + vd("na mesma proporção") + ". Cortar mais A que B deixaria unidades de B “sem par”, que não "
                   "geram utilidade."),
        "destrinchando": [
            "u = mín{A, B} (proporção 1:1). Curvas de indiferença em L; o consumidor sempre escolhe o vértice, "
            "A = B. Com renda R: " + vd("A = B = R/(p<sub>A</sub> + p<sub>B</sub>)") + ".",
            "Se p<sub>A</sub> sobe, o “pacote” A + B encarece e ambos caem juntos. Exemplo: R = 12, p<sub>A</sub> "
            "= p<sub>B</sub> = 1 → 6 de cada; p<sub>A</sub> = 2 → " + vd("4 de cada") + ".",
            "Decomposição de " + oc("Slutsky") + "/" + oc("Hicks") + ": " + azb("efeito substituição nulo") +
            " (não há como trocar A por B mantendo a utilidade) e toda a queda vem do " + azb("efeito renda") +
            ". Por isso não existe “substituir A por B” aqui.",
            "Comparação útil: com complementares <b>imperfeitos</b> (pão e manteiga) A poderia cair mais que B; "
            "com complementares <b>perfeitos</b>, nunca.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item aplica a complementares perfeitos "
                       "uma intuição de complementares comuns (o bem que encareceu cai mais). O “perfeitos” é a "
                       "palavra-gatilho: proporção fixa não admite ritmos diferentes de redução."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se A e B são complementares perfeitos, o aumento do preço de A reduz o consumo de A e de B na "
            "mesma proporção.”</i> → CERTO",
            "<i>“Se A e B são complementares perfeitos, o aumento do preço de A não altera o consumo de B.”</i> → "
            "ERRADO (B cai junto com A)",
        ])],
        "reescrita": ("Se dois bens A e B são complementares perfeitos, o aumento do preço de A com o preço de B "
                      "constante fará o consumidor reduzir " + hl("o consumo de A e o de B na mesma proporção") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Complementares perfeitos consumidos em proporções fixas; aumento de pA reduz A e B na "
                             "mesma proporção; u = mín{αA, βB}."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 497", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": ["observacao: assertiva com erro de redação na fonte (“reduzir seu consumo mais rapidamente o "
                    "consumo de A”); mantida fiel"],
    },
    # ------------------------------------------------------------------ E2-L01779
    {
        "id": "ECO-E2-L01779-1", "fonte_ref": "E2-L01779", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_RT_RESP,
        "rotulo_item": "Item",
        "assertiva": ("O equilíbrio do consumidor, no caso de dois bens substitutos perfeitos, implica que o "
                      "consumidor compre sempre aquele com preço mais baixo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O equilíbrio do consumidor, no caso de dois bens substitutos perfeitos, implica que o "
                      "consumidor compre ") + vm("sempre aquele com preço mais baixo") + az("."),
        "poucas": ("Com substitutos perfeitos o critério é a maior " + azb("UMg por real") + " (TMS × razão de "
                   "preços), não o menor preço; e, se UMg/p empatar, qualquer cesta da reta orçamentária é ótima."),
        "destrinchando": [
            "Utilidade linear: " + vd("u = ax + by") + ". Compara-se a/p<sub>x</sub> com b/p<sub>y</sub>: todo o "
            "gasto vai para o bem com maior utilidade por real (" + azb("solução de canto") + ").",
            "“Preço mais baixo” só coincide com o critério quando a troca é 1:1 (a = b). Contraexemplo: um "
            "pendrive de 8 GB (R$ 30) e um de 4 GB (R$ 20) para quem só quer armazenamento: u = 8x + 4y; 8/30 ≈ "
            "0,27 > 4/20 = 0,20 GB por real. O mais caro vence.",
            "Caso de empate: se " + vd("a/p<sub>x</sub> = b/p<sub>y</sub>") + " (ou, com troca 1:1, preços "
            "iguais), a reta orçamentária coincide com uma curva de indiferença e há infinitas cestas ótimas, "
            "inclusive interiores.",
            vm("Regra-âncora: substitutos perfeitos → compare UMg/p; o “mais barato” só vale com troca 1:1 e "
               "preços diferentes."),
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " “Sempre” + “preço mais baixo” é uma "
                       "simplificação que funciona no exemplo de manual (marcas idênticas, 1:1) e falha fora dele: "
                       "no empate de preços e quando as unidades não se trocam 1 por 1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No caso de substitutos perfeitos com taxa de troca de um por um e preços diferentes, o consumidor "
            "compra apenas o bem mais barato.”</i> → CERTO",
            "<i>“Com substitutos perfeitos, a cesta ótima é sempre uma solução de canto.”</i> → ERRADO (modulador "
            "absoluto: no empate há solução interior)",
        ])],
        "reescrita": ("O equilíbrio do consumidor, no caso de dois bens substitutos perfeitos, implica que o "
                      "consumidor compre " + hl("apenas aquele com maior utilidade marginal por unidade monetária, "
                      "sendo indiferente entre as cestas da reta orçamentária se essas razões forem iguais") + "."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["sempre"], "dificuldade": 2,
        "comentario_fonte": ("Compra só o mais barato se os preços forem diferentes; com preços iguais é indiferente "
                             "entre qualquer combinação; erro no “sempre”."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 539", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 540", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (solução de canto descrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01782
    {
        "id": "ECO-E2-L01782-1", "fonte_ref": "E2-L01782", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_RT_RESP,
        "rotulo_item": "Item",
        "assertiva": ("Quando dois bens são complementares perfeitos, o consumidor comprará ambos sempre na mesma "
                      "proporção, não importando a inclinação da restrição orçamentária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando dois bens são complementares perfeitos, o consumidor comprará ambos <u>sempre na mesma "
                      "proporção</u>, <u>não importando a inclinação</u> da restrição orçamentária."),
        "poucas": ("Nas preferências de " + oc("Leontief") + " o ótimo é sempre o " + azb("vértice do L") + ", "
                   "sobre o raio de proporção fixa. Preços relativos mudam a <b>quantidade</b> de “pares”, nunca a "
                   "proporção."),
        "destrinchando": [
            "u = mín{ax, by}: só há utilidade adicional com mais dos dois bens na proporção " + vd("y/x = a/b") +
            ". O excedente de um bem sem o par é desperdício, então o consumidor nunca compra fora do raio.",
            "Escolha ótima: x = R/(p<sub>x</sub> + (a/b)p<sub>y</sub>) e y = (a/b)x. Qualquer que seja a "
            "inclinação −p<sub>x</sub>/p<sub>y</sub> da reta, a cesta escolhida está no vértice; muda só a "
            "distância da origem.",
            "Por isso o " + azb("efeito substituição é nulo") + " e a curva preço-consumo é o próprio raio: toda "
            "variação de preço age como variação de renda real.",
            "Contraste: em substitutos perfeitos a inclinação da reta decide <b>tudo</b> (qual canto escolher); "
            "no caso convexo usual, ela altera a proporção pela tangência TMS = p<sub>x</sub>/p<sub>y</sub>.",
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Os moduladores absolutos (“sempre”, “não "
                       "importando”) levam a marcar ERRADO por reflexo; aqui eles são exatamente a propriedade "
                       "definidora dos complementares perfeitos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando dois bens são substitutos perfeitos, o consumidor comprará ambos sempre na mesma proporção, "
            "não importando a inclinação da restrição orçamentária.”</i> → ERRADO (troca de conceito: a inclinação "
            "decide o canto)",
            "<i>“Para complementares perfeitos, a alta do preço de um bem gera efeito substituição nulo.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["sempre", "não importando"], "dificuldade": 1,
        "comentario_fonte": ("Complementares perfeitos (Leontief): proporção fixa; curvas em L; mudança de preços "
                             "relativos altera a quantidade total, não a proporção."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00011
    {
        "id": "ECO-E3-L00011-1", "fonte_ref": "E3-L00011", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("Julgue os itens a seguir, a respeito de determinação das curvas de procura, elasticidade, "
                    "produtividade e custos de produção."),
        "rotulo_item": "Item",
        "assertiva": ("A cesta de mercado que maximiza a utilidade do consumidor situa-se sobre a linha de orçamento e "
                      "é tangente à curva de indiferença mais alta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A cesta de mercado que maximiza a utilidade do consumidor situa-se <u>sobre a linha de "
                      "orçamento</u> e é <u>tangente à curva de indiferença mais alta</u>."),
        "poucas": ("O ótimo (interior, preferências bem-comportadas) é o ponto em que a " + azb("reta "
                   "orçamentária") + " tangencia a " + azb("curva de indiferença mais alta alcançável") + ": gasta "
                   "toda a renda e " + vd("TMS = p<sub>x</sub>/p<sub>y</sub>") + "."),
        "destrinchando": [
            "Duas condições: (1) <b>sobre</b> a linha de orçamento — com monotonicidade, sobra de renda significa "
            "utilidade desperdiçada; (2) " + azb("tangência") + " — a inclinação da curva de indiferença (TMS = "
            "UMg<sub>x</sub>/UMg<sub>y</sub>) iguala a da reta (p<sub>x</sub>/p<sub>y</sub>).",
            "Por que não um ponto em que a curva <b>corta</b> a reta: ali a TMS difere da razão de preços e "
            "andar ao longo da reta leva a uma curva mais alta. Curvas acima da tangente são inalcançáveis com a "
            "renda dada.",
            "Equivalência: TMS = p<sub>x</sub>/p<sub>y</sub> ⇔ " + vd("UMg<sub>x</sub>/p<sub>x</sub> = "
            "UMg<sub>y</sub>/p<sub>y</sub>") + " (equimarginalidade).",
            "Exceções que a banca usa para inverter: " + azb("solução de canto") + " (substitutos perfeitos, ou "
            "quando a TMS supera a razão de preços em todo o trecho) e " + azb("complementares perfeitos") + " "
            "(ótimo no vértice do L, sem tangência definida). A redação “cesta… é tangente” é frouxa (quem "
            "tangencia é a reta), mas o sentido é o de manual.",
        ],
        "grafico_verso": "ECO-E3-L00011-1-V1",
        "dissecando": (cz("[literalidade]") + " Reproduz o vocabulário de " + oc("Pindyck e Rubinfeld") + " (“cesta de "
                       "mercado”, “linha de orçamento”) e a definição de manual. Quem busca pelo em ovo marca ERRADO pela redação imprecisa ou "
                       "pensando em soluções de canto, que o item não menciona."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A cesta que maximiza a utilidade situa-se abaixo da linha de orçamento, pois o consumidor racional "
            "preserva parte da renda.”</i> → ERRADO (com monotonicidade, gasta toda a renda)",
            "<i>“No ótimo interior, a taxa marginal de substituição iguala a razão entre os preços dos bens.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Equilíbrio do consumidor na tangência entre a restrição orçamentária e a curva de "
                             "indiferença mais alta atingível; TMS = razão de preços; toda a renda gasta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]

# ====================================================================== bloco 4
CARDS += [
    # ------------------------------------------------------------------ E3-L00076
    {
        "id": "ECO-E3-L00076-1", "fonte_ref": "E3-L00076", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", **NIDI_JUL, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Se um consumidor considera ordenar estas três cestas de bens A, B e C, de modo que, B seja mais "
                      "preferida do que A, C seja tão preferida quanto B e A seja tão preferida quanto C, podemos "
                      "dizer que às preferências deste consumidor se aplicam tanto o princípio da transitividade como "
                      "o da monotonicidade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um consumidor considera ordenar estas três cestas de bens A, B e C, de modo que, B seja mais "
                      "preferida do que A, C seja tão preferida quanto B e A seja tão preferida quanto C, podemos "
                      "dizer que às preferências deste consumidor ") + vm("se aplicam tanto o princípio da "
                      "transitividade como o da monotonicidade") + az("."),
        "poucas": ("A ordenação é " + azb("intransitiva") + ": de A ~ C e C ~ B segue A ~ B, o que contradiz B ≻ A. "
                   "E a monotonicidade nem pode ser avaliada, pois o item não diz o que há em cada cesta."),
        "destrinchando": [
            azb("Transitividade") + " vale também para a indiferença: A ~ C e C ~ B ⇒ " + vd("A ~ B") + ". O item "
            "afirma B ≻ A: contradição. Pelo outro caminho: B ≻ A e A ~ C ⇒ B ≻ C, mas o item diz C ~ B.",
            "Consequência prática: preferências intransitivas não podem ser representadas por uma função de "
            "utilidade (seria preciso u(B) > u(A) = u(C) = u(B)) e geram curvas de indiferença que se cruzariam.",
            azb("Monotonicidade") + " (“mais é melhor”) compara cestas pelo <b>conteúdo</b>: se B tem pelo menos "
            "tanto de cada bem que A e mais de algum, B ≻ A. O item só traz rótulos A, B, C, sem quantidades — "
            "nada permite afirmar que ela vale.",
            "Mapa dos axiomas: " + azb("completude") + " (comparar quaisquer cestas), " + azb("reflexividade") +
            ", " + azb("transitividade") + " (coerência da ordem) formam a racionalidade; " + azb("monotonicidade")
            + " e " + azb("convexidade") + " dão o formato “bem-comportado” das curvas.",
        ],
        "dissecando": (cz("[contradição · extrapolação]") + " Duas falhas empilhadas: a transitividade é desmentida "
                       "pelas próprias relações do enunciado, e a monotonicidade é afirmada sem dado algum sobre as "
                       "cestas. Truque de resolução: escreva as três relações em linha (B ≻ A ~ C ~ B) e veja o ciclo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se B ≻ A, B ~ C e C ≻ A, as preferências desse consumidor são compatíveis com a "
            "transitividade.”</i> → CERTO",
            "<i>“Se A ≻ B, B ≻ C e C ≻ A, as preferências violam a completude.”</i> → ERRADO (troca de conceito: "
            "violam a transitividade; todas as cestas foram comparadas)",
        ])],
        "reescrita": ("Se um consumidor considera ordenar estas três cestas de bens A, B e C, de modo que, B seja mais "
                      "preferida do que A, C seja tão preferida quanto B e A seja tão preferida quanto C, podemos "
                      "dizer que as preferências deste consumidor " + hl("violam o princípio da transitividade, e "
                      "nada se pode afirmar sobre a monotonicidade") + "."),
        "tipo_erro": ["CONTRADICAO", "EXTRAPOLACAO"], "moduladores": ["tanto… como"], "dificuldade": 2,
        "comentario_fonte": ("Viola a transitividade: A ~ C e C ~ B implicariam A ~ B, contra B ≻ A; monotonicidade "
                             "não pode ser avaliada sem as quantidades das cestas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 26", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 27-30", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (definições dos axiomas no 📖)"},
                          {"ref": "IMAGEM 31", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "irrecuperavel (ilegível)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00078
    {
        "id": "ECO-E3-L00078-1", "fonte_ref": "E3-L00078", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **NIDI_JUL, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Com exceção da relação entre bens substitutos, a taxa marginal de substituição entre dois bens "
                      "é geralmente expressa por uma taxa constante ao longo da curva de indiferença."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com exceção da relação entre bens ") + vm("substitutos") + az(", a taxa marginal de "
                      "substituição entre dois bens é geralmente expressa por uma taxa ") + vm("constante")
                   + az(" ao longo da curva de indiferença."),
        "poucas": ("O item inverte regra e exceção: em geral a " + azb("TMS é decrescente") + " (curvas convexas); "
                   "ela só é " + azb("constante") + " no caso de " + azb("substitutos perfeitos") + " (curvas "
                   "retas)."),
        "destrinchando": [
            azb("TMS") + " = quanto de y o consumidor cede por mais uma unidade de x, mantendo a utilidade: TMS = "
            "|Δy/Δx| = UMg<sub>x</sub>/UMg<sub>y</sub>, a inclinação (em módulo) da curva de indiferença.",
            "Caso usual: quem tem muito y e pouco x aceita ceder muito y por um x; à medida que x fica abundante e "
            "y escasso, cede cada vez menos. A TMS " + vd("cai") + " ao longo da curva — é a " + azb("convexidade")
            + " (relação de abundância e escassez).",
            "Exceção: " + azb("substitutos perfeitos") + " (u = ax + by): a taxa de troca é fixa em a/b, qualquer "
            "que seja a cesta — curva reta, TMS constante. Exemplo da fonte: para guardar 32 GB, tanto faz 4 "
            "pendrives de 8 GB ou 8 de 4 GB; a troca é sempre 2:1.",
            "Atenção ao adjetivo: substitutos <b>imperfeitos</b> (café e chá, manteiga e margarina) têm curvas "
            "convexas e TMS decrescente; só os <b>perfeitos</b> têm TMS constante. Complementares perfeitos: curva "
            "em L, TMS indefinida no vértice (zero ou infinita nos braços).",
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " A frase pega a exceção (TMS constante) e a apresenta "
                       "como regra, ressalvando justamente o caso em que ela vale. O “bens substitutos” sem "
                       "“perfeitos” é outro descuido proposital. O mesmo item caiu no Simulado Março/2025 "
                       "(ECO-E3-L00236-1)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com exceção da relação entre bens substitutos perfeitos, a taxa marginal de substituição é "
            "geralmente decrescente ao longo da curva de indiferença.”</i> → CERTO",
            "<i>“No caso de complementares perfeitos, a TMS é constante e igual à razão entre as proporções de "
            "consumo.”</i> → ERRADO (TMS é zero, infinita ou indefinida)",
        ])],
        "reescrita": ("Com exceção da relação entre bens " + hl("substitutos perfeitos") + ", a taxa marginal de "
                      "substituição entre dois bens é geralmente expressa por uma taxa " + hl("decrescente") +
                      " ao longo da curva de indiferença."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": ["geralmente", "com exceção"], "dificuldade": 1,
        "comentario_fonte": ("TMS decrescente em curvas convexas; constante apenas para substitutos perfeitos; item "
                             "inverte regra e exceção. Exemplo dos pendrives (troca 2:1)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 35", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (substitutos perfeitos e exemplo dos pendrives no 📖)"},
                          {"ref": "IMAGEM 36-37", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (ilegíveis)"}],
        "alertas": ["item_repetido: assertiva idêntica em ECO-E3-L00236-1 (Nidi, Simulado Março/2025); mantidos os "
                    "dois por serem provas diferentes (Folha -Q §8.6)"],
    },
    # ------------------------------------------------------------------ E3-L00146
    {
        "id": "ECO-E3-L00146-1", "fonte_ref": "E3-L00146", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **ANTT, "errei": True,
        "comando": CMD_ANTT,
        "excerto": EXC_ANTT,
        "rotulo_item": "Item",
        "assertiva": ("Se X e Y forem bens perfeitamente substitutos e as preferências do consumidor forem "
                      "estritamente monotônicas, é possível que u(20, 20) > u(19, 30)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se X e Y forem bens perfeitamente substitutos e as preferências do consumidor forem "
                      "estritamente monotônicas, <u>é possível</u> que u(20, 20) > u(19, 30)."),
        "poucas": ("Substitutos perfeitos: " + vd("u = ax + by") + " com a, b > 0, em qualquer proporção. "
                   "u(20, 20) > u(19, 30) ⇔ " + vd("a > 10b") + " — basta que X valha mais de dez vezes Y."),
        "destrinchando": [
            "O que define " + azb("substitutos perfeitos") + " é a " + azb("TMS constante") + " (curvas retas), "
            "não a troca 1 por 1. A forma geral é u(x, y) = ax + by; a TMS é a/b.",
            azb("Monotonicidade estrita") + " só exige a > 0 e b > 0 (mais de qualquer bem aumenta a utilidade). "
            "Não fixa o peso relativo dos bens.",
            "Conta: 20a + 20b > 19a + 30b ⇔ " + vd("a > 10b") + ". Exemplo: a = 11, b = 1 → u(20, 20) = "
            + vd("240") + " > u(19, 30) = " + vd("239") + ". Uma unidade de X vale mais que dez de Y; perder um X "
            "não é compensado por dez Y.",
            "A pegadinha: com u = x + y (1:1), viria 40 < 49 e a desigualdade seria impossível. Quem supõe "
            "troca 1:1 marca ERRADO. Note também que a cesta (19, 30) não domina (20, 20) — tem menos X —, então a "
            "monotonicidade não decide a comparação.",
            vm("Regra-âncora: “é possível” pede um exemplo; “pode-se garantir” pede uma regra que valha sempre."),
        ],
        "dissecando": (cz("[modulador relativo · contraintuitivo]") + " O “é possível” salva o item: basta um caso "
                       "(a > 10b). Contraintuitivo porque a cesta com mais unidades no total perde. Compare com o "
                       "item irmão (ECO-E3-L00148-1), que usa “pode-se garantir” numa cesta que domina a outra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se X e Y forem perfeitamente substitutos e as preferências estritamente monotônicas, pode-se "
            "garantir que u(19, 30) > u(20, 20).”</i> → ERRADO (depende de a e b: com a > 10b vale o contrário)",
            "<i>“Se as preferências forem estritamente monotônicas, é possível que u(20, 20) > u(20, 30).”</i> → "
            "ERRADO (a 2ª cesta domina a 1ª: nunca)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "CONTRAINTUITIVO"], "moduladores": ["é possível"], "dificuldade": 2,
        "comentario_fonte": ("Substitutos perfeitos = TMS constante, u = ax + by; u(20,20) > u(19,30) ⇔ a > 10b; ex. "
                             "a = 11, b = 1 dá 240 > 239; com u = x + y seria impossível."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_ANTT,
                          {"ref": "IMAGEM 152", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto (u = ax + by)"},
                          {"ref": "IMAGEM 153-154", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (demonstração a > 10b)"},
                          {"ref": "IMAGEM 155", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (três formatos de curva de indiferença, descritos no 📖)"},
                          {"ref": "IMAGEM 156-157", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvidas no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00147
    {
        "id": "ECO-E3-L00147-1", "fonte_ref": "E3-L00147", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", **ANTT, "errei": True,
        "comando": CMD_ANTT,
        "excerto": EXC_ANTT,
        "rotulo_item": "Item",
        "assertiva": ("Se X e Y forem bens perfeitamente substitutos e as preferências do consumidor forem "
                      "estritamente monotônicas, o equilíbrio do consumidor, dada a restrição orçamentária, será uma "
                      "solução de canto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se X e Y forem bens perfeitamente substitutos e as preferências do consumidor forem "
                      "estritamente monotônicas, o equilíbrio do consumidor, dada a restrição orçamentária, ")
                   + vm("será") + az(" uma solução de canto."),
        "poucas": ("Solução de canto é o caso <b>típico</b>, não o obrigatório: se " + vd("TMS = a/b = "
                   "p<sub>x</sub>/p<sub>y</sub>") + ", a reta orçamentária coincide com uma curva de indiferença e "
                   "todas as cestas dela — inclusive as interiores — são ótimas."),
        "destrinchando": [
            "Com u = ax + by, compara-se a/p<sub>x</sub> com b/p<sub>y</sub> (utilidade por real): "
            "a/p<sub>x</sub> > b/p<sub>y</sub> → só X (x = R/p<sub>x</sub>); a/p<sub>x</sub> < b/p<sub>y</sub> → só "
            "Y; " + vd("a/p<sub>x</sub> = b/p<sub>y</sub>") + " → qualquer cesta da reta.",
            "Gráfico: se a reta orçamentária é mais inclinada ou menos inclinada que as curvas de indiferença, a "
            "curva mais alta é alcançada num eixo (canto). Se as inclinações coincidem, a reta <b>é</b> uma curva de "
            "indiferença: há um segmento inteiro de ótimos (" + oc("Varian") + ", <i>Microeconomia: uma abordagem "
            "moderna</i>, cap. 5, mostra os três casos).",
            "A monotonicidade estrita garante só que a renda é toda gasta (o ótimo está na reta); não força o "
            "canto.",
            "Para o caso 1:1 (u = x + y), a regra vira: compra-se só o mais barato; preços iguais → indiferença "
            "entre todas as combinações que esgotam a renda.",
        ],
        "grafico_verso": "ECO-E3-L00147-1-V1",
        "dissecando": (cz("[modulador absoluto]") + " O “será” transforma o resultado típico em certeza e apaga o "
                       "caso de empate de inclinações. 🔥 A banca adora o caso-limite: a solução de canto é "
                       "<b>possível</b> (e típica) com substitutos perfeitos, não <b>necessária</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se a TMS for diferente da razão de preços, o equilíbrio do consumidor será uma solução de "
            "canto.”</i> → CERTO",
            "<i>“…se a TMS for igual à razão de preços, o equilíbrio será único e interior.”</i> → ERRADO (há "
            "infinitos ótimos, incluindo os cantos)",
        ])],
        "reescrita": ("Se X e Y forem bens perfeitamente substitutos e as preferências do consumidor forem "
                      "estritamente monotônicas, o equilíbrio do consumidor, dada a restrição orçamentária, "
                      + hl("poderá ser") + " uma solução de canto" + hl(", mas, se a TMS igualar a razão de preços, "
                      "qualquer cesta da reta orçamentária será ótima") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["será"], "dificuldade": 2,
        "comentario_fonte": ("Não necessariamente canto: depende de px/py frente à TMS; se iguais, qualquer cesta da "
                             "reta é ótima (Varian). Um comentário de fórum da fonte dava CERTO para item vizinho; "
                             "outro raciocínio de aluno sobre monotonicidade estava equivocado."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [FIG_ANTT,
                          {"ref": "IMAGEM 158", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (três casos de escolha)"},
                          {"ref": "IMAGEM 159", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00147-1-V1, canto × segmento de ótimos)"}],
        "alertas": ["qualidade_fonte: um dos comentários empilhados (aluno) argumentava que, por monotonicidade, uma "
                    "cesta mista seria preferível a um canto — raciocínio incorreto, descartado"],
    },
    # ------------------------------------------------------------------ E3-L00148
    {
        "id": "ECO-E3-L00148-1", "fonte_ref": "E3-L00148", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", **ANTT, "errei": False,
        "comando": CMD_ANTT,
        "excerto": EXC_ANTT,
        "rotulo_item": "Item",
        "assertiva": ("Se as preferências do consumidor forem estritamente monotônicas, pode-se garantir que "
                      "u(20, 30) > u(20, 25)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se as preferências do consumidor forem estritamente monotônicas, <u>pode-se garantir</u> que "
                      "u(20, 30) > u(20, 25)."),
        "poucas": ("(20, 30) tem o <b>mesmo</b> X e <b>mais</b> Y que (20, 25): pela " + azb("monotonicidade "
                   "estrita") + ", é estritamente preferida, qualquer que seja a função de utilidade."),
        "destrinchando": [
            azb("Monotonicidade estrita") + ": se a cesta A tem pelo menos tanto de cada bem quanto B e mais de "
            "pelo menos um, então A ≻ B, logo " + vd("u(A) > u(B)") + ". Aqui X = 20 nas duas e Y = 30 > 25.",
            azb("Monotonicidade fraca") + " exigiria mais de <b>todos</b> os bens para garantir preferência "
            "estrita; com mais de um só, garantiria apenas A ≿ B. É por isso que o item diz “estritamente”.",
            "Como a conclusão vem do axioma, ela não depende da forma de u (linear, Cobb-Douglas…): é uma "
            "<b>garantia</b>. Contraste com ECO-E3-L00146-1, em que as cestas não se dominam — (19, 30) tem menos X "
            "— e o resultado depende dos pesos.",
            "Graficamente: (20, 30) está diretamente acima de (20, 25), numa curva de indiferença mais alta. "
            "Monotonicidade estrita também implica curvas negativamente inclinadas e sem “faixas grossas”.",
        ],
        "dissecando": (cz("[literalidade]") + " Aplicação direta da definição. O “pode-se garantir” assusta quem vem "
                       "do item irmão (“é possível”); aqui a garantia existe porque uma cesta " + azb("domina") +
                       " a outra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se as preferências forem estritamente monotônicas, pode-se garantir que u(21, 24) > u(20, "
            "25).”</i> → ERRADO (as cestas não se dominam: depende de u)",
            "<i>“Se as preferências forem apenas fracamente monotônicas, pode-se garantir que u(21, 31) > u(20, "
            "30).”</i> → CERTO (mais de todos os bens)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["pode-se garantir"], "dificuldade": 1,
        "comentario_fonte": ("Monotonicidade estrita: mesma quantidade de X e mais Y ⇒ cesta estritamente preferida; "
                             "garantia independe de u; se X tivesse mudado não daria para garantir."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_ANTT,
                          {"ref": "IMAGEM 160", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (cestas (20,30) e (20,25) descritas no 📖)"},
                          {"ref": "IMAGEM 161-164", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (monotonicidade forte × fraca)"}],
        "alertas": [],
    },
]

# ====================================================================== bloco 5
CARDS += [
    # ------------------------------------------------------------------ E3-L00236
    {
        "id": "ECO-E3-L00236-1", "fonte_ref": "E3-L00236", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **NIDI_MAR, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Com exceção da relação entre bens substitutos, a taxa marginal de substituição entre dois bens "
                      "é geralmente expressa por uma taxa constante ao longo da curva de indiferença."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com exceção da relação entre bens ") + vm("substitutos") + az(", a taxa marginal de "
                      "substituição entre dois bens é geralmente expressa por uma taxa ") + vm("constante")
                   + az(" ao longo da curva de indiferença."),
        "poucas": ("Regra e exceção estão trocadas: a " + azb("TMS") + " é, em geral, " + vd("decrescente") +
                   " ao longo da curva; " + vd("constante") + " só para " + azb("substitutos perfeitos") + "."),
        "destrinchando": [
            "A TMS mede a disposição de trocar y por x mantendo a utilidade: TMS = UMg<sub>x</sub>/UMg<sub>y</sub> "
            "= |inclinação da curva de indiferença|. Ela reflete a relação entre abundância e escassez dos bens na "
            "cesta.",
            "Exemplo numérico com u = xy (Cobb-Douglas): TMS = y/x. Na cesta (2, 8), TMS = " + vd("4") + "; na "
            "cesta (4, 4), da mesma curva, TMS = " + vd("1") + "; em (8, 2), " + vd("0,25") + ". Andando para a "
            "direita, a TMS cai: curva " + azb("convexa") + ".",
            "Com u = 2x + y (substitutos perfeitos), TMS = 2 em qualquer ponto: a curva é uma " + azb("reta") +
            ". É o único formato com TMS constante.",
            "Dois desvios de vocabulário que a banca explora: “substitutos” sem “perfeitos” (substitutos comuns "
            "têm TMS decrescente) e “complementares perfeitos” (curva em L, sem TMS constante).",
            vm("Regra-âncora: convexa → TMS decrescente (regra); reta → TMS constante (exceção dos substitutos "
               "perfeitos)."),
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " O examinador mantém o vocabulário certo (TMS, curva de "
                       "indiferença, substitutos) e só inverte o papel de regra e exceção. Item idêntico ao do "
                       "Simulado Julho/2025 (ECO-E3-L00078-1): a banca recicla a pegadinha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para preferências convexas, a TMS diminui à medida que o consumidor substitui y por x ao longo de "
            "uma curva de indiferença.”</i> → CERTO",
            "<i>“Se a TMS é constante, os bens são complementares perfeitos.”</i> → ERRADO (troca de conceito: "
            "substitutos perfeitos)",
        ])],
        "reescrita": ("Com exceção da relação entre bens " + hl("substitutos perfeitos") + ", a taxa marginal de "
                      "substituição entre dois bens é geralmente expressa por uma taxa " + hl("decrescente") +
                      " ao longo da curva de indiferença."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": ["geralmente", "com exceção"], "dificuldade": 1,
        "comentario_fonte": ("TMS é a inclinação da curva; decrescente por utilidade marginal decrescente; constante "
                             "só para substitutos perfeitos; reescrita: “substitutos perfeitos… decrescente”. O verso "
                             "trazia ainda, por engano, o comentário do item seguinte (curvas que não se cruzam)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 322", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"},
                          {"ref": "IMAGEM 323", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (curva convexa com TMS decrescente, descrita no 📖)"},
                          {"ref": "IMAGEM 324", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (substitutos perfeitos, descritos no 📖)"}],
        "alertas": ["item_repetido: assertiva idêntica em ECO-E3-L00078-1 (Nidi, Simulado Julho/2025); mantidos os "
                    "dois por serem provas diferentes (Folha -Q §8.6)",
                    "fonte: o fim do verso traz um comentário “CERTO” sobre curvas que não se cruzam, pertencente a "
                    "E3-L00237; ignorado aqui"],
    },
    # ------------------------------------------------------------------ E3-L00237
    {
        "id": "ECO-E3-L00237-1", "fonte_ref": "E3-L00237", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", **NIDI_MAR, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Considerando curvas de indiferença que satisfaçam os axiomas de completude, reflexividade e "
                      "transitividade, bem como a existência de apenas dois bens, é impossível que as curvas de "
                      "indiferença de um consumidor que representem níveis distintos de preferência se cruzem."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando curvas de indiferença que satisfaçam os axiomas de completude, reflexividade e "
                      "<u>transitividade</u>, bem como a existência de apenas dois bens, é <u>impossível</u> que as "
                      "curvas de indiferença de um consumidor que representem níveis distintos de preferência se "
                      "cruzem."),
        "poucas": ("Se duas curvas de níveis distintos se cruzassem, a cesta do cruzamento seria indiferente a "
                   "cestas de níveis diferentes — e a " + azb("transitividade") + " tornaria essas cestas "
                   "indiferentes entre si, o que é contraditório."),
        "destrinchando": [
            "Prova por absurdo: U₁ e U₂ se cruzam em A. Tome B em U₁ e D em U₂. A ~ B (mesma curva) e A ~ D (mesma "
            "curva) ⇒, por " + azb("transitividade") + ", " + vd("B ~ D") + ". Mas B e D estão em curvas de "
            "níveis distintos, ou seja, uma é estritamente preferida à outra. Contradição.",
            "Com " + azb("monotonicidade") + " o absurdo fica visível: escolhendo D com o mesmo x e mais y que B, "
            "D ≻ B — e, ao mesmo tempo, B ~ D.",
            "Rigor: a contradição decisiva vem da transitividade (com a definição de “níveis distintos”); a "
            "monotonicidade só ilustra. Por isso o item lista completude, reflexividade e transitividade — os "
            "axiomas de " + azb("racionalidade") + " — e basta.",
            "Outras propriedades das curvas e de onde vêm: inclinação negativa ← monotonicidade; convexidade ← "
            "preferência pela diversidade; curvas “finas” ← monotonicidade estrita; não cruzamento ← "
            "transitividade.",
        ],
        "grafico_verso": "ECO-E3-L00237-1-V1",
        "dissecando": (cz("[literalidade]") + " Propriedade clássica com um “impossível” que "
                       "assusta. O absoluto está correto porque decorre de um axioma, não de evidência empírica. 🔥 "
                       "Variante frequente: atribuir o não cruzamento à convexidade ou à completude (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Curvas de indiferença não se cruzam porque as preferências são convexas.”</i> → ERRADO (troca de "
            "conceito: é a transitividade)",
            "<i>“Se as preferências de um consumidor forem intransitivas, suas curvas de indiferença podem se "
            "cruzar.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["impossível"], "dificuldade": 1,
        "comentario_fonte": ("Curvas de níveis distintos nunca se cruzam para não ferir a transitividade: se A ~ B e "
                             "A ~ D, D ≻ B é impossível."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 325", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00237-1-V1, curvas que se cruzam em A)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00270
    {
        "id": "ECO-E3-L00270-1", "fonte_ref": "E3-L00270", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Segundo a teoria microeconômica e os seus axiomas da racionalidade, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O axioma da convexidade expressa uma preferência por diversidade de bens na cesta de consumo e "
                      "esta convexidade pode ser compreendida pela taxa marginal de substituição (TMS) decrescente. "
                      "Existe, no entanto, um caso em que essa TMS é constante, quando os bens são complementares "
                      "perfeitos. Nesse caso, a curva de indiferença perde sua convexidade e se torna linear."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O axioma da convexidade expressa uma preferência por diversidade de bens na cesta de consumo e "
                      "esta convexidade pode ser compreendida pela taxa marginal de substituição (TMS) decrescente. "
                      "Existe, no entanto, um caso em que essa TMS é constante, quando os bens são ")
                   + vm("complementares") + az(" perfeitos. Nesse caso, a curva de indiferença perde sua convexidade "
                      "e se torna linear."),
        "poucas": ("TMS constante e curva linear são de " + azb("substitutos perfeitos") + ". Complementares "
                   "perfeitos têm curva em " + azb("L") + ", com TMS infinita no braço vertical, zero no "
                   "horizontal e indefinida no vértice."),
        "destrinchando": [
            "A 1ª frase é a definição correta: " + azb("convexidade") + " = gosto pela diversidade = " + azb("TMS "
            "decrescente") + " (quanto mais x se tem, menos y se aceita ceder por mais um x).",
            "Substitutos perfeitos (u = ax + by): troca a taxa fixa a/b → " + vd("TMS constante") + " → curva "
            "<b>reta</b>. Ex.: canetas azuis e pretas para quem só quer escrever.",
            "Complementares perfeitos (u = mín{ax, by}, " + oc("Leontief") + "): consumo em proporção fixa → curva "
            "em <b>L</b>. No braço vertical, mais y sem x não vale nada (TMS infinita); no horizontal, mais x sem y "
            "também não (TMS zero); no vértice, a TMS não é definida.",
            "Nuance de prova: uma reta ainda é <b>fracamente</b> convexa (a média de duas cestas indiferentes é "
            "indiferente), mas não estritamente; “perde sua convexidade” deve ser lido como “perde a convexidade "
            "estrita”. O erro decisivo do item é o nome do caso.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Tudo está certo, menos uma palavra: “complementares” no lugar "
                       "de “substitutos”. Como substitutos e complementares perfeitos aparecem sempre juntos nos "
                       "manuais (mesma figura, painéis a e b), a troca é a pegadinha natural."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No caso de complementares perfeitos, as curvas de indiferença têm formato de L e a TMS não é "
            "definida no vértice.”</i> → CERTO",
            "<i>“A convexidade das preferências implica TMS crescente ao longo da curva de indiferença.”</i> → "
            "ERRADO (inversão: decrescente)",
        ])],
        "reescrita": ("O axioma da convexidade expressa uma preferência por diversidade de bens na cesta de consumo e "
                      "esta convexidade pode ser compreendida pela taxa marginal de substituição (TMS) decrescente. "
                      "Existe, no entanto, um caso em que essa TMS é constante, quando os bens são "
                      + hl("substitutos") + " perfeitos. Nesse caso, a curva de indiferença perde sua convexidade e se "
                      "torna linear."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Se fossem substitutos perfeitos, o item estaria certo; complementares perfeitos têm "
                             "curva em L, TMS zero/infinita, indefinida no vértice."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 374", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (substitutos × complementares perfeitos, descritos no 📖)"},
                          {"ref": "IMAGEM 375", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (texto sobre TMS decrescente no 📖)"}],
        "alertas": ["comando_reconstruido: o comando da fonte estava truncado (“…os indivíduos buscam m…”); usado "
                    "comando neutro"],
    },
    # ------------------------------------------------------------------ E3-L00371
    {
        "id": "ECO-E3-L00371-1", "fonte_ref": "E3-L00371", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", **NIDI_NOV, "errei": True,
        "comando": CMD_NIDI_NOV,
        "excerto": EXC_NIDI_NOV,
        "rotulo_item": "Item",
        "assertiva": ("O pressuposto de que “quanto mais de um bem, melhor” é duplamente tratado nos axiomas da "
                      "plenitude e da monotonicidade das preferências."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O pressuposto de que “quanto mais de um bem, melhor” é ") + vm("duplamente tratado nos axiomas "
                      "da plenitude e") + az(" da monotonicidade das preferências."),
        "poucas": ("“Mais é melhor” é só a " + azb("monotonicidade") + " (não saciedade, dominância). A "
                   + azb("plenitude") + " (completude) garante apenas que o consumidor <b>consegue comparar</b> "
                   "quaisquer cestas — sem dizer qual prefere."),
        "destrinchando": [
            azb("Completude / plenitude / integralidade") + ": para quaisquer cestas A e B, A ≿ B, B ≿ A ou ambos. "
            "Não impõe direção: alguém pode ter preferências completas e preferir <b>menos</b> poluição, ou ter "
            "um ponto de saciedade.",
            azb("Monotonicidade / não saciedade / dominância") + ": se A tem pelo menos tanto de cada bem quanto B "
            "e mais de algum, A ≻ B. É ela que formaliza “quanto mais, melhor” e dá às curvas de indiferença "
            "inclinação negativa e ordem crescente a partir da origem.",
            "Lista completa para revisão: completude, reflexividade e transitividade (racionalidade); "
            "continuidade (permite representar por função de utilidade); monotonicidade e convexidade (“bom "
            "comportamento”).",
            "O texto motivador lembra a exceção: bens com saciedade violam a monotonicidade além de certo ponto "
            "(UMg < 0), mas continuam satisfazendo a completude — prova de que os dois axiomas são independentes.",
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " O item acerta a monotonicidade e enxerta a "
                       "plenitude, aproveitando a ambiguidade do nome (“plenitude” lembra “satisfação plena”). O "
                       "“duplamente” é o sinal de alerta: cada axioma tem uma função própria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O pressuposto de que ‘quanto mais, melhor’ corresponde ao axioma da monotonicidade, também chamado "
            "de não saciedade.”</i> → CERTO",
            "<i>“O axioma da completude estabelece que o consumidor prefere cestas com mais bens.”</i> → ERRADO "
            "(completude = comparabilidade)",
        ])],
        "reescrita": ("O pressuposto de que “quanto mais de um bem, melhor” é " + hl("tratado apenas no axioma") +
                      " da monotonicidade das preferências" + hl("; a plenitude garante somente que o consumidor "
                      "consegue comparar quaisquer cestas") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["duplamente"], "dificuldade": 1,
        "comentario_fonte": ("Plenitude = capacidade de comparar cestas; só a monotonicidade trata de “mais é "
                             "melhor”. Versos com comparação extensa entre teoria do consumidor e do produtor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 519", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (axiomas básicos no 📖)"},
                          {"ref": "IMAGEM 520", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (seleção, continuidade, convexidade no 📖)"},
                          {"ref": "IMAGEM 521", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 522-524", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortadas (tabelas consumidor × produtor, fora do ponto do item)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00372
    {
        "id": "ECO-E3-L00372-1", "fonte_ref": "E3-L00372", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", **NIDI_NOV, "errei": False,
        "comando": CMD_NIDI_NOV,
        "excerto": EXC_NIDI_NOV,
        "rotulo_item": "Item",
        "assertiva": ("A satisfação adicional a cada nova unidade consumida é reflexo da lei da utilidade marginal "
                      "decrescente e da renda excedente após a aquisição da cesta ótima do consumidor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A satisfação adicional a cada nova unidade consumida é reflexo da lei da utilidade marginal "
                      "decrescente ") + vm("e da renda excedente após a aquisição da cesta ótima do consumidor")
                   + az("."),
        "poucas": ("A " + azb("utilidade marginal") + " é propriedade das preferências, não do bolso. E não há "
                   + vd("renda excedente") + " no ótimo: com monotonicidade, a cesta ótima esgota a renda."),
        "destrinchando": [
            azb("Utilidade marginal") + " = satisfação trazida pela última unidade. A " + azb("lei da utilidade "
            "marginal decrescente") + " (" + oc("Gossen") + "; base do marginalismo de " + oc("Jevons") + ", "
            + oc("Menger") + " e " + oc("Walras") + ", década de 1870) diz que ela cai à medida que o consumo "
            "aumenta: o 1º copo d’água vale muito, o 10º quase nada.",
            "Cesta ótima: máx u sujeito a p<sub>x</sub>x + p<sub>y</sub>y = R. Com monotonicidade (e axioma da "
            "“seleção”, na nomenclatura da fonte), o consumidor " + vd("gasta toda a renda") + " — sobra de renda "
            "significaria utilidade desperdiçada. Na teoria estática não há poupança.",
            "A relação causal correta é a inversa: UMg decrescente + restrição orçamentária ⇒ cesta ótima "
            "(UMg<sub>x</sub>/p<sub>x</sub> = UMg<sub>y</sub>/p<sub>y</sub>). A cesta não “explica” a UMg.",
            "Possível origem da confusão: o " + azb("excedente do consumidor") + " (" + oc("Marshall") + ") — "
            "diferença entre disposição a pagar e preço pago — é medida de bem-estar, não renda que sobra.",
        ],
        "dissecando": (cz("[nexo indevido · meia-verdade]") + " A 1ª metade é verdadeira; o “e da renda "
                       "excedente…” cria uma causa inexistente e ainda pressupõe sobra de renda no ótimo. Basta "
                       "apagar o trecho final para o item ficar certo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A satisfação adicional decrescente a cada nova unidade consumida é reflexo da lei da utilidade "
            "marginal decrescente.”</i> → CERTO",
            "<i>“Na cesta ótima, o consumidor com preferências monotônicas mantém parte da renda como reserva.”</i> "
            "→ ERRADO (a renda é toda gasta)",
        ])],
        "reescrita": ("A satisfação adicional a cada nova unidade consumida é reflexo da lei da utilidade marginal "
                      "decrescente" + hl(", independentemente da renda; na cesta ótima, toda a renda é gasta") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("UMg decrescente é fenômeno de saciedade, sem relação com renda excedente; toda a renda é "
                             "gasta; possível confusão com excedente do consumidor (Marshall)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 525", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (UT e UMg dos copos d’água, descritas no 📖)"},
                          {"ref": "IMAGEM 526", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (função de produção em três fases, fora do tema; imagem de banco)"},
                          {"ref": "IMAGEM 527", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (UMgₓ/pₓ = UMgᵧ/pᵧ no 📖)"},
                          {"ref": "IMAGEM 528", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "irrecuperavel (ilegível)"}],
        "alertas": [],
    },
]
