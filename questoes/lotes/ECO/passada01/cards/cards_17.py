"""Cards do lote de redação 17 — ECO, passada 01 (nota 07-A, concorrência perfeita)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

HIP = "📐 Hipóteses e maximização de lucro"
CP = "⏱️ Curto prazo: oferta da firma"
LP = "⏳ Longo prazo e entrada/saída"

CMD_CP = "Julgue o item a seguir, relativo ao mercado em concorrência perfeita."
CMD_NAB_EST = "A respeito das estruturas de mercado, julgue (C ou E) o item a seguir."
CMD_NAB_23 = "Em relação a um mercado em concorrência perfeita, julgue (C ou E) o item a seguir."
CMD_NAB_EST2 = "Em relação às estruturas de mercado, julgue (C ou E) o item que se segue."
CMD_ARM = "Acerca da teoria da firma e da concorrência perfeita, julgue o item a seguir."
CMD_FCC = "Acerca da firma em concorrência perfeita, julgue o item a seguir."
CMD_TCE = "Acerca do mercado em concorrência perfeita, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E1-0266
    {
        "id": "ECO-E1-0266-1", "fonte_ref": "E1-0266", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CP,
        "rotulo_item": "Item",
        "assertiva": ("Em condições de competição perfeita, se houver o aumento da demanda por parte de um "
                      "comprador, o preço de mercado permanece inalterado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em condições de competição perfeita, se houver o aumento da demanda por parte de "
                      "<u>um comprador</u>, o preço de mercado permanece inalterado."),
        "poucas": ("Na concorrência perfeita cada comprador é " + azb("atomizado") + ": sua demanda é ínfima "
                   "diante do mercado, e uma variação individual não desloca de modo perceptível a demanda "
                   "agregada — o preço não se altera."),
        "destrinchando": [
            "Hipóteses clássicas do modelo: " + azb("muitos compradores e vendedores") + " (atomicidade), "
            + azb("produto homogêneo") + ", " + azb("livre entrada e saída") + " e "
            + azb("informação perfeita") + ". Delas decorre que ninguém, sozinho, tem poder de mercado.",
            "O preço é formado pelo encontro da " + azb("demanda de mercado") + " (soma horizontal das "
            "demandas individuais) com a oferta de mercado. Um único comprador que passa a querer mais "
            "acrescenta uma fração desprezível à soma: a curva de mercado praticamente não se move.",
            "Por isso, tanto compradores quanto vendedores são " + azb("tomadores de preço")
            + " (<i>price takers</i>): tratam o preço como um dado.",
            "Contraste: se o aumento for da demanda de <b>muitos</b> compradores (renda maior, gosto, preço de "
            "substituto), a demanda de mercado se desloca para a direita e o preço de equilíbrio sobe.",
            vm("Regra-âncora: agente individual não move o preço; só o mercado como um todo o faz."),
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " O item depende da palavra “um”: quem lê "
                       "“aumento da demanda” pensa logo em deslocamento da curva e preço maior. A pista está "
                       "no sujeito individual, que, por hipótese, não tem peso no mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se houver aumento da demanda de todos os compradores, o preço de mercado permanece "
            "inalterado.”</i> → ERRADO (troca de ator: a demanda de mercado se desloca e o preço sobe)",
            "<i>“…a redução da oferta de uma única firma não altera o preço de mercado.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Preço determinado pelo mercado como um todo; nenhum agente individual o altera.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0267
    {
        "id": "ECO-E1-0267-1", "fonte_ref": "E1-0267", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CP,
        "rotulo_item": "Item",
        "assertiva": "Na concorrência perfeita o preço é determinado pela interação entre oferta e demanda.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na concorrência perfeita o preço é determinado pela <u>interação entre oferta e "
                      "demanda</u>."),
        "poucas": ("Nenhum agente fixa o preço: ele resulta do " + azb("equilíbrio de mercado")
                   + ", onde a oferta da indústria cruza a demanda de mercado."),
        "destrinchando": [
            "Características do modelo: muitos compradores e vendedores; " + azb("produto homogêneo")
            + " (idêntico aos olhos do consumidor); " + azb("livre entrada e saída")
            + "; informação perfeita; ausência de poder de mercado.",
            "Consequência: o preço se forma no " + azb("mercado") + " (oferta agregada × demanda agregada) e é "
            "<b>tomado</b> por cada firma. A firma só decide <b>quanto</b> produzir, igualando P ao CMg.",
            "Distinga os dois planos: no gráfico do mercado, D é negativamente inclinada e O positivamente; "
            "no gráfico da firma, a demanda é horizontal ao nível do preço de equilíbrio.",
            "Nas demais estruturas a firma tem algum poder: o monopolista escolhe o ponto da demanda "
            "(RMg = CMg) e fixa P acima do CMg; na concorrência monopolística há diferenciação de produto.",
            "Exemplos usuais de mercados próximos do modelo: commodities agrícolas e minerais negociadas em "
            "bolsa (soja, trigo), ativos financeiros padronizados. Exemplos como padarias e farmácias são "
            "aproximações frouxas, porque há diferenciação por localização e marca.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, sem pegadinha. O risco é o candidato "
                       "desconfiar do óbvio por lembrar que “a firma não determina o preço” — e é justamente "
                       "por isso que quem o determina é o mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência perfeita, o preço é determinado por cada firma, que o iguala ao seu custo "
            "marginal.”</i> → ERRADO (inversão: a firma toma o preço e ajusta a quantidade)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Lista de características da concorrência perfeita; preço pela interação de oferta "
                            "e demanda; exemplos: lojas populares, padarias, farmácias.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0269
    {
        "id": "ECO-E1-0269-1", "fonte_ref": "E1-0269", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CP,
        "rotulo_item": "Item",
        "assertiva": "Na concorrência perfeita, a curva de demanda individual é uma reta inclinada.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na concorrência perfeita, a curva de demanda individual é uma reta ")
                   + vm("inclinada") + az("."),
        "poucas": ("A demanda que a firma individual enfrenta é " + azb("horizontal") + " ao preço de "
                   "mercado (perfeitamente elástica): ela vende o quanto quiser a P e nada acima de P."),
        "destrinchando": [
            "A firma competitiva é tomadora de preço. Se cobrar um centavo acima de P, os compradores — que "
            "veem produtos idênticos e conhecem todos os preços — migram para os concorrentes: a quantidade "
            "vendida cai a zero. Abaixo de P não há razão para vender, pois a esse preço já vende tudo.",
            "Isso é uma demanda com " + vd("elasticidade-preço infinita") + ": uma reta horizontal na altura "
            "de P, que coincide com a " + azb("receita média") + " e a " + azb("receita marginal") + ".",
            "Já a demanda <b>de mercado</b> é negativamente inclinada: soma das demandas dos consumidores, "
            "obedece à lei da demanda.",
            "Atenção ao termo “demanda individual”: no contexto da concorrência perfeita, significa a demanda "
            "dirigida à firma individual. A demanda de cada consumidor, isoladamente, continua "
            "negativamente inclinada — o que é horizontal é a curva que a <b>firma</b> enxerga.",
            vm("Regra-âncora: firma competitiva → demanda horizontal; mercado → demanda decrescente."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item aplica à firma o formato da demanda de mercado. "
                       "🔥 Tema recorrente: a banca alterna “firma” e “mercado” no mesmo bloco de itens, e o "
                       "gabarito muda só com essa palavra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência perfeita, a curva de demanda de mercado é negativamente inclinada.”</i> → CERTO",
            "<i>“A firma competitiva enfrenta demanda perfeitamente inelástica.”</i> → ERRADO (troca de "
            "conceito: é perfeitamente elástica)",
        ])],
        "reescrita": ("Na concorrência perfeita, a curva de demanda individual " + hl("da firma") + " é uma reta "
                      + hl("horizontal, ao nível do preço de mercado") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Demanda individual horizontal; preço dado pelo mercado; demanda perfeitamente "
                            "elástica; consumidores indiferentes às marcas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (56).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0270
    {
        "id": "ECO-E1-0270-1", "fonte_ref": "E1-0270", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CP,
        "rotulo_item": "Item",
        "assertiva": "Na concorrência perfeita a curva de demanda do mercado é uma reta negativamente inclinada.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na concorrência perfeita a curva de demanda <u>do mercado</u> é uma reta negativamente "
                      "inclinada."),
        "poucas": ("A demanda de mercado é a " + azb("soma horizontal") + " das demandas individuais dos "
                   "consumidores e segue a lei da demanda: preço maior, quantidade demandada menor."),
        "destrinchando": [
            "Somar horizontalmente = a cada preço, somar as quantidades que cada consumidor deseja. Como cada "
            "uma cai quando P sobe (efeitos substituição e renda), a soma também cai: inclinação negativa.",
            "O que é horizontal na concorrência perfeita é a demanda vista pela " + azb("firma")
            + " — que, minúscula diante do mercado, vende tudo ao preço vigente. As duas curvas convivem: a "
            "de mercado define P com a oferta; a da firma é a reta horizontal nesse P.",
            "“Reta” é simplificação didática: a curva de demanda pode ser curva (ex.: elasticidade constante, "
            "Q = A·P<sup>−ε</sup>). O que o item testa é o <b>sinal</b> da inclinação, não a forma funcional.",
            "Exceções teóricas à lei da demanda (bem de " + oc("Giffen") + ", bens de Veblen) são casos "
            "raros e não afetam a regra que a banca cobra aqui.",
        ],
        "dissecando": (cz("[detalhe]") + " A palavra decisiva é “do mercado”. Se fosse “da firma”, o item "
                       "seria ERRADO. O “reta” não é usado como armadilha: é a representação de manual."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência perfeita a curva de demanda da firma é negativamente inclinada.”</i> → ERRADO "
            "(troca de conceito: é horizontal)",
            "<i>“A demanda de mercado é obtida pela soma vertical das demandas individuais.”</i> → ERRADO "
            "(soma horizontal: somam-se quantidades a cada preço)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Demanda de mercado = soma das individuais; obedece à lei da demanda, inclinação "
                            "negativa.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (60).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0271
    {
        "id": "ECO-E1-0271-1", "fonte_ref": "E1-0271", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CP,
        "rotulo_item": "Item",
        "assertiva": ("Na concorrência perfeita, as curvas de demanda de Receita Média (RMe) e da Receita Marginal "
                      "(RMg) se equivalem, são horizontais e iguais ao Preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na concorrência perfeita, as curvas de demanda de Receita Média (RMe) e da Receita "
                      "Marginal (RMg) se equivalem, são <u>horizontais</u> e iguais ao Preço."),
        "poucas": ("Com P constante para a firma, RT = P·q: " + vd("RMe = RT/q = P") + " e "
                   + vd("RMg = ΔRT/Δq = P") + ". As três curvas (demanda da firma, RMe e RMg) são a mesma reta "
                   "horizontal."),
        "destrinchando": [
            azb("Receita total") + " RT = P × q. Na concorrência perfeita P não depende de q, então RT é uma "
            "reta que sai da origem com inclinação P.",
            azb("Receita média") + " = RT/q = P — vale para <b>qualquer</b> firma que cobre preço único; por "
            "isso a curva de demanda é sempre a curva de RMe.",
            azb("Receita marginal") + " = acréscimo de RT ao vender mais uma unidade. Como a firma competitiva "
            "não precisa baixar o preço para vender mais, cada unidade adicional rende exatamente P: "
            + vd("RMg = P") + ".",
            "Contraste com o monopólio: para vender mais, o monopolista baixa o preço de todas as unidades, "
            "e a RMg fica <b>abaixo</b> da demanda (com demanda linear P = a − bq, RMg = a − 2bq, com o dobro "
            "da inclinação).",
            "Graficamente, a RT da firma competitiva é o retângulo P × q sob a reta horizontal.",
            vm("Regra-âncora: na concorrência perfeita, d = RMe = RMg = P."),
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a identidade de manual. O que derruba candidatos é "
                       "levar a regra do monopólio (RMg abaixo da RMe) para o mercado competitivo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência perfeita, a receita marginal é decrescente e situa-se abaixo da receita "
            "média.”</i> → ERRADO (troca de conceito: isso é monopólio)",
            "<i>“Para qualquer firma que cobre preço único, a receita média é igual ao preço.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "RMe = RMg = P; curvas horizontais porque os ofertantes são tomadores de preço; RT = "
                            "P × q (área do retângulo).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (54).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0272
    {
        "id": "ECO-E1-0272-1", "fonte_ref": "E1-0272", "destino": "07-A", "subtema": CP,
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CP,
        "rotulo_item": "Item",
        "assertiva": ("Na Concorrência Perfeita, o equilíbrio de curto prazo é alcançado ao igualar as curvas de "
                      "receita e de custos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Na Concorrência Perfeita, o equilíbrio de curto prazo é alcançado ao igualar as curvas "
                      "de <u>receita</u> e de <u>custos</u>."),
        "poucas": ("Lido como o manual pretende — " + azb("receita marginal = custo marginal") + " —, o item "
                   "é certo: a firma maximiza lucro onde " + vd("P = RMg = CMg") + "."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O item não diz <b>quais</b> curvas. Se forem as marginais (RMg e CMg), está certo. "
                          "Se forem as totais (RT = CT) ou as médias (P = CTMe), descreve o ponto de "
                          "<b>lucro zero</b>, que só coincide com o ótimo no equilíbrio de longo prazo. "
                          "Mantém-se o CERTO da fonte, mas uma banca rigorosa poderia considerá-lo ERRADO.")],
        "destrinchando": [
            "Regra de ouro da firma (qualquer estrutura): produzir até que a última unidade acrescente à "
            "receita o mesmo que acrescenta ao custo — " + vm("RMg = CMg") + ", com o CMg cortando a RMg "
            "de baixo para cima.",
            "Na concorrência perfeita RMg = P, então a condição vira " + vd("P = CMg") + ". Graficamente: a "
            "reta horizontal do preço cruza o ramo ascendente do CMg na quantidade ótima q*.",
            "No curto prazo esse ótimo pode ter lucro positivo (P > CTMe), nulo (P = CTMe) ou negativo "
            "(CVMe ≤ P < CTMe). Se P < CVMe mínimo, a firma para de produzir.",
            "Em termos de totais, o ótimo é onde a <b>distância</b> RT − CT é máxima — ou seja, onde as "
            "inclinações de RT e CT se igualam (RMg = CMg), e não onde as curvas se cruzam (RT = CT é o "
            "ponto de nivelamento).",
            "No longo prazo, a livre entrada leva P ao mínimo do CTMe: aí P = CMg = CTMe e as duas leituras "
            "coincidem.",
        ],
        "dissecando": (cz("[literalidade]") + " Formulação frouxa de uma regra de manual: o gabarito supõe "
                       "curvas marginais. Na prova, desconfie de “receita e custo” sem adjetivo — a banca "
                       "costuma especificar “marginal”; quando troca por “médio”, o item fica ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o equilíbrio de curto prazo da firma é alcançado quando o preço iguala o custo total "
            "médio.”</i> → ERRADO (troca de conceito: P = CTMe é lucro zero, não o ótimo)",
            "<i>“…a firma maximiza o lucro onde a receita marginal iguala o custo marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Equilíbrio quando “as utilidades são igualadas”, sem excessos nem faltas; ponto "
                            "de lucro máximo.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "Untitled (59).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada)"}],
        "alertas": ["contestavel: “igualar as curvas de receita e de custos” não especifica marginais; lido como "
                    "RT = CT ou P = CTMe, o item seria ERRADO — mantido o CERTO da fonte",
                    "qualidade_fonte: o comentário de origem fala em “utilidades igualadas” e “sem excessos nem "
                    "faltas”, conceitos de equilíbrio de mercado e de consumidor, não da firma"],
    },
    # ------------------------------------------------------------------ E2-L00019
    {
        "id": "ECO-E2-L00019-1", "fonte_ref": "E2-L00019", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, sobre a aplicação da análise de custos e receitas em mercados.",
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado perfeitamente competitivo com alta rivalidade, a receita marginal apresenta "
                      "trajetória descendente em relação à quantidade vendida. Isso ocorre porque, em um ambiente "
                      "de alta concorrência, qualquer tentativa de aumentar o preço acima do mercado resultaria "
                      "na perda imediata de vendas para a concorrência, forçando as empresas a venderem ao preço "
                      "de equilíbrio para permanecerem competitivas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um mercado perfeitamente competitivo com alta rivalidade, a receita marginal ")
                    + vm("apresenta trajetória descendente") + az(" em relação à quantidade vendida. Isso "
                    "ocorre porque, em um ambiente de alta concorrência, qualquer tentativa de aumentar o preço "
                    "acima do mercado resultaria na perda imediata de vendas para a concorrência, forçando as "
                    "empresas a venderem ao preço de equilíbrio para permanecerem competitivas.")),
        "poucas": ("Na concorrência perfeita a RMg é " + azb("constante e igual ao preço") + ". A própria "
                   "justificativa do item (vende-se tudo ao preço de mercado) prova isso, e não uma RMg "
                   "decrescente."),
        "destrinchando": [
            azb("Receita marginal") + " = ΔRT/Δq. Se a firma vende qualquer quantidade ao mesmo P, cada "
            "unidade extra rende P: " + vd("RMg = P") + " para todo q — uma reta horizontal.",
            "RMg <b>descendente</b> é marca de firma com poder de mercado (monopólio, concorrência "
            "monopolística, oligopólio): para vender mais ela precisa baixar o preço de todas as unidades, "
            "e a RMg cai mais depressa que a demanda.",
            "A segunda frase do item está correta: acima do preço de mercado a firma não vende nada, abaixo "
            "dele não precisa vender. É exatamente a demanda horizontal (perfeitamente elástica) — que "
            "implica RMg constante. O item usa uma causa verdadeira para sustentar uma consequência oposta.",
            "Nota de vocabulário: na concorrência perfeita não há “rivalidade” estratégica — as firmas são "
            "atomizadas e impessoais; a concorrência é intensa, mas ninguém reage ao outro. Rivalidade é "
            "conceito de oligopólio.",
            vm("Regra-âncora: tomador de preço → RMg = P, horizontal; RMg decrescente → poder de mercado."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " A banca importa do monopólio a RMg "
                       "decrescente e cola uma justificativa verdadeira, mas que leva à conclusão contrária. "
                       "Pista: “forçando a vender ao preço de equilíbrio” = preço constante = RMg constante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio, a receita marginal é decrescente e inferior ao preço para q > 0.”</i> → CERTO",
            "<i>“Na concorrência perfeita, a receita total cresce a taxas decrescentes.”</i> → ERRADO (RT é "
            "linear: cresce à taxa constante P)",
        ])],
        "reescrita": ("Em um mercado perfeitamente competitivo com alta rivalidade, a receita marginal "
                      + hl("é constante e igual ao preço") + " em relação à quantidade vendida. Isso ocorre "
                      "porque […] qualquer tentativa de aumentar o preço acima do mercado resultaria na perda "
                      "imediata de vendas para a concorrência, forçando as empresas a venderem ao preço de "
                      "equilíbrio para permanecerem competitivas."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Receita marginal constante e igual ao preço; firmas não alteram preços sem perder "
                            "participação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00343
    {
        "id": "ECO-E2-L00343-1", "fonte_ref": "E2-L00343", "destino": "07-A", "subtema": CP,
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado perfeitamente competitivo com firmas idênticas, considere um choque negativo "
                      "de demanda que reduz o preço de P<sub>0</sub> para P<sub>1</sub>. Se P<sub>1</sub> < CTM, "
                      "toda firma sai imediatamente do mercado; se CVM < P<sub>1</sub> < CTM, as firmas seguem "
                      "produzindo no curto prazo, e a curva de oferta de cada firma no curto prazo é o trecho do "
                      "CMg acima do CTM. No longo prazo, com livre entrada e saída, o equilíbrio requer "
                      "P = CMg = CTM no mínimo do CTM (escala eficiente), e o lucro econômico é nulo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um mercado perfeitamente competitivo com firmas idênticas, considere um choque "
                       "negativo de demanda que reduz o preço de P<sub>0</sub> para P<sub>1</sub>. Se ")
                    + vm("P<sub>1</sub> < CTM, toda firma sai imediatamente do mercado") + az("; se CVM < "
                    "P<sub>1</sub> < CTM, as firmas seguem produzindo no curto prazo, e a curva de oferta de "
                    "cada firma no curto prazo é o trecho do CMg acima do ") + vm("CTM")
                    + az(". No longo prazo, com livre entrada e saída, o equilíbrio requer P = CMg = CTM no "
                         "mínimo do CTM (escala eficiente), e o lucro econômico é nulo.")),
        "poucas": ("Dois erros no curto prazo: P < CTM não faz a firma sair <b>imediatamente</b> (no curto "
                   "prazo ela só para se " + vd("P < CVM") + "), e a oferta de curto prazo é o CMg acima do "
                   + azb("mínimo do CVM") + ", não do CTM. A parte de longo prazo está certa."),
        "destrinchando": [
            "Curto prazo = há custo fixo, que se paga com ou sem produção (irrecuperável). A decisão relevante "
            "é <b>produzir ou paralisar</b>: produz se " + vd("P ≥ CVM") + " (cobre o variável e ainda abate "
            "parte do fixo); paralisa se P < CVM. Sair do mercado não é opção de curto prazo.",
            "Daí a " + azb("oferta de curto prazo") + " da firma = ramo ascendente do CMg a partir do "
            + azb("mínimo do CVM") + " (ponto de fechamento). Entre o mínimo do CVM e o mínimo do CTM a firma "
            "produz com prejuízo — trecho que pertence à oferta e que o item excluiu.",
            "Longo prazo = todos os custos são variáveis. A firma sai se P < CTM mínimo. Com livre entrada e "
            "saída, o preço converge para " + vd("P = CMg = CTMe mínimo") + ": escala eficiente, lucro "
            "econômico nulo (lucro contábil normal).",
            "Mapa das três faixas (curto prazo): P > CTM → lucro; CVM ≤ P < CTM → produz com prejuízo; "
            "P < CVM → paralisa (prejuízo = custo fixo).",
            vm("Regra-âncora: curto prazo olha o CVM (parar); longo prazo olha o CTM (sair)."),
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " Item longo, com a última frase "
                       "impecável para dar credibilidade. O erro está na troca CVM → CTM em dois lugares do "
                       "curto prazo e no “imediatamente”, que mistura paralisação (curto prazo) com saída "
                       "(longo prazo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se P<sub>1</sub> < CVM mínimo, as firmas paralisam a produção no curto prazo, arcando com "
            "prejuízo igual ao custo fixo.”</i> → CERTO",
            "<i>“No longo prazo, a firma permanece no mercado enquanto P cobrir o CVM.”</i> → ERRADO (no longo "
            "prazo não há custo fixo: exige P ≥ CTM)",
        ])],
        "reescrita": ("[…] Se " + hl("P<sub>1</sub> < CVM, toda firma paralisa a produção no curto prazo") + "; se "
                      "CVM < P<sub>1</sub> < CTM, as firmas seguem produzindo no curto prazo, e a curva de oferta "
                      "de cada firma no curto prazo é o trecho do CMg acima do " + hl("mínimo do CVM")
                      + ". No longo prazo, com livre entrada e saída, o equilíbrio requer P = CMg = CTM no "
                      "mínimo do CTM (escala eficiente), e o lucro econômico é nulo."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["toda", "imediatamente"],
        "dificuldade": 2,
        "comentario_fonte": "Shutdown no curto prazo se P < CVM; saída no longo prazo se P < CTM; LP: P = CMg = "
                            "CTM no mínimo do CTM, lucro zero.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_ajustado: retirados os parênteses de OCR em torno das siglas e o “E” solto no fim da "
                    "frente (gabarito vazado)"],
    },
    # ------------------------------------------------------------------ E2-L00344
    {
        "id": "ECO-E2-L00344-1", "fonte_ref": "E2-L00344", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Para qualquer firma (competitiva ou não), a receita média é sempre igual ao preço, e a "
                      "receita marginal é sempre igual ao preço; logo, a condição de primeira ordem para "
                      "maximização de lucro reduz-se universalmente a P = CMg."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para qualquer firma (competitiva ou não), a receita média é sempre igual ao preço, e a "
                       "receita marginal ") + vm("é sempre igual ao preço") + az("; logo, a condição de primeira "
                       "ordem para maximização de lucro ") + vm("reduz-se universalmente a P = CMg") + az(".")),
        "poucas": ("RMe = P vale para toda firma de preço único; " + azb("RMg = P") + " só vale para o "
                   + azb("tomador de preço") + ". Com poder de mercado, RMg < P, e o ótimo é RMg = CMg com "
                   + vd("P > CMg") + "."),
        "destrinchando": [
            "RMe = RT/q = (P·q)/q = P: identidade válida para qualquer firma que cobre um preço único — "
            "monopolista inclusive. É por isso que a curva de demanda é a curva de RMe. (Só deixa de valer "
            "com discriminação de preços.)",
            "RMg = d(P·q)/dq = " + vd("P + q·(dP/dq)") + ". Na concorrência perfeita dP/dq = 0 → RMg = P. "
            "Com demanda negativamente inclinada (dP/dq < 0), RMg < P.",
            "Condição de primeira ordem universal: " + vm("RMg = CMg") + ". Só na concorrência perfeita ela "
            "vira P = CMg. No monopólio: P(1 − 1/|ε|) = CMg → " + azb("markup") + " P/CMg = |ε|/(|ε| − 1); "
            "o índice de " + oc("Lerner") + " (P − CMg)/P = 1/|ε| mede o poder de mercado.",
            "Consequência de bem-estar: com P > CMg o monopolista produz menos que o socialmente eficiente "
            "(peso morto). Em concorrência perfeita, P = CMg garante eficiência alocativa.",
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " Os “sempre”, “qualquer” e "
                       "“universalmente” estendem a todas as estruturas uma igualdade exclusiva do tomador de "
                       "preço. A primeira afirmação (RMe = P) é verdadeira e funciona como isca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para qualquer firma que cobre preço único, a receita média é igual ao preço, mas a receita "
            "marginal só é igual ao preço se a firma for tomadora de preço.”</i> → CERTO",
            "<i>“A condição de primeira ordem RMg = CMg aplica-se apenas à concorrência perfeita.”</i> → ERRADO "
            "(restrição indevida: vale para toda firma maximizadora)",
        ])],
        "reescrita": ("Para qualquer firma (competitiva ou não), a receita média é sempre igual ao preço, mas a "
                      "receita marginal " + hl("só é igual ao preço para a firma tomadora de preço") + "; logo, a "
                      "condição de primeira ordem para maximização de lucro " + hl("é RMg = CMg, que só se reduz "
                      "a P = CMg na concorrência perfeita") + "."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["qualquer", "sempre", "universalmente"],
        "dificuldade": 2,
        "comentario_fonte": "RMg = P e RMe = P só para tomadores de preço; com poder de mercado RMg ≠ P e a CPO "
                            "não se reduz a P = CMg.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem restringe também RMe = P aos tomadores de preço; "
                    "RMe = P vale para toda firma que cobra preço único — só a parte da RMg está errada no item"],
    },
    # ------------------------------------------------------------------ E2-L00389
    {
        "id": "ECO-E2-L00389-1", "fonte_ref": "E2-L00389", "destino": "07-A", "subtema": LP,
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Em uma indústria competitiva de custos crescentes (onde os preços dos insumos sobem à medida "
                      "que a indústria se expande), a curva de oferta de mercado de longo prazo é positivamente "
                      "inclinada. Isso implica que, para induzir um aumento na quantidade ofertada agregada no "
                      "longo prazo, o preço de equilíbrio do produto deve necessariamente subir para cobrir os "
                      "custos médios mínimos mais elevados das empresas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma indústria competitiva de <u>custos crescentes</u> (onde os preços dos insumos sobem "
                      "à medida que a indústria se expande), a curva de oferta de mercado de longo prazo é "
                      "positivamente inclinada. Isso implica que, para induzir um aumento na quantidade ofertada "
                      "agregada no longo prazo, o preço de equilíbrio do produto deve <u>necessariamente</u> "
                      "subir para cobrir os custos médios mínimos mais elevados das empresas."),
        "poucas": ("No longo prazo P = " + azb("CTMe mínimo") + ". Se a expansão da indústria encarece os "
                   "insumos, o CTMe mínimo de todas as firmas sobe — e o preço de longo prazo também: oferta de "
                   "longo prazo " + vd("crescente") + "."),
        "destrinchando": [
            "Mecanismo: a demanda sobe → P sobe → lucro → entrada de firmas → a indústria demanda mais "
            "insumos → os preços dos insumos sobem (" + azb("deseconomias externas") + ") → as curvas de "
            "custo de todas as firmas se deslocam para cima. O novo equilíbrio de lucro zero ocorre num "
            "preço maior que o inicial.",
            "Unindo os equilíbrios de longo prazo (antes e depois), obtém-se a " + azb("oferta de longo prazo "
            "da indústria") + ", positivamente inclinada.",
            "Três casos: " + vd("custos constantes") + " (insumos com oferta perfeitamente elástica) → oferta de "
            "LP horizontal no CTMe mínimo; " + vd("custos crescentes") + " → positivamente inclinada; "
            + vd("custos decrescentes") + " (economias externas: polo especializado, fornecedores e mão de obra "
            "qualificada mais baratos) → negativamente inclinada.",
            "O “necessariamente” é seguro: com custos crescentes, cada ponto de equilíbrio de longo prazo "
            "com mais produção tem CTMe mínimo mais alto, e P = CTMe mínimo.",
            "Não confundir com rendimentos de escala da <b>firma</b>: aqui o que sobe é o preço dos insumos, "
            "efeito externo à firma e interno à indústria.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz o caso de manual. O “necessariamente” "
                       "assusta quem associa modulador forte a ERRADO, mas decorre da definição de indústria de "
                       "custos crescentes. 🔥 A banca alterna os três casos (constante, crescente, decrescente)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em indústria de custos constantes, a oferta de longo prazo é horizontal, e aumentos "
            "permanentes da demanda elevam apenas a quantidade.”</i> → CERTO",
            "<i>“Em indústria de custos decrescentes, a oferta de longo prazo é positivamente inclinada.”</i> "
            "→ ERRADO (troca de conceito: é negativamente inclinada)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["necessariamente"], "dificuldade": 2,
        "comentario_fonte": "Oferta de LP horizontal só em custos constantes; entrada eleva preço dos insumos, "
                            "custos sobem, preço de equilíbrio maior; oferta de LP positivamente inclinada.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00443
    {
        "id": "ECO-E2-L00443-1", "fonte_ref": "E2-L00443", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_EST,
        "rotulo_item": "Item",
        "assertiva": ("Em concorrência perfeita, uma firma individual enfrenta uma curva de demanda perfeitamente "
                      "elástica ao nível do preço de mercado, sendo, portanto, uma tomadora de preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em concorrência perfeita, uma firma individual enfrenta uma curva de demanda "
                      "<u>perfeitamente elástica</u> ao nível do preço de mercado, sendo, portanto, uma tomadora "
                      "de preços."),
        "poucas": ("A firma é ínfima diante do mercado: vende qualquer quantidade ao preço vigente e nada acima "
                   "dele. Demanda " + azb("horizontal") + " = " + vd("elasticidade infinita") + " = "
                   + azb("tomadora de preços") + "."),
        "destrinchando": [
            "Elasticidade-preço |ε| = |%Δq / %ΔP|. Na demanda horizontal, uma variação mínima de preço leva a "
            "quantidade de “tudo” para zero: |ε| → ∞. Por isso “perfeitamente elástica” e “horizontal” são "
            "sinônimos no gráfico.",
            "Os dois polos: " + vd("|ε| = ∞") + " → horizontal (firma competitiva); " + vd("|ε| = 0")
            + " → vertical (perfeitamente inelástica: a quantidade não reage ao preço).",
            "Por que a firma é tomadora de preços: produto homogêneo + muitos vendedores + informação "
            "perfeita. Subir o preço = perder todos os clientes; baixar = abrir mão de receita sem necessidade.",
            "Corolário: d = RMe = RMg = P. A firma escolhe só a quantidade, onde P = CMg.",
            "Cuidado com a ordem lógica: a demanda horizontal é <b>consequência</b> das hipóteses do modelo; "
            "o item a apresenta como causa da condição de tomadora — leitura aceita, porque as duas "
            "descrevem o mesmo fato.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. A armadilha possível seria trocar "
                       "“perfeitamente elástica” por “perfeitamente inelástica” — o candidato que associa "
                       "“horizontal” a “inelástica” (porque o preço não muda) erra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma firma individual enfrenta uma curva de demanda perfeitamente inelástica, pois o preço "
            "não se altera…”</i> → ERRADO (troca de conceito: horizontal = perfeitamente elástica)",
            "<i>“…a demanda de mercado também é perfeitamente elástica.”</i> → ERRADO (a demanda de mercado é "
            "negativamente inclinada)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Firma pequena demais para influenciar o preço; demanda horizontal (perfeitamente "
                            "elástica); vende qualquer quantidade ao preço de mercado.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00478
    {
        "id": "ECO-E2-L00478-1", "fonte_ref": "E2-L00478", "destino": "07-A", "subtema": CP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à teoria microeconômica, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Os custos fixos de empresas que operam em concorrência perfeita no curto prazo são "
                      "irrelevantes para a decisão de continuarem produzindo, pois só se produz quando o preço é "
                      "superior ao custo total médio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os custos fixos de empresas que operam em concorrência perfeita no curto prazo são "
                       "irrelevantes para a decisão de continuarem produzindo, pois só se produz quando o preço "
                       "é superior ao custo ") + vm("total médio") + az(".")),
        "poucas": ("A premissa está certa (custo fixo é " + azb("irrecuperável") + " no curto prazo); a "
                   "justificativa, errada: a firma produz se " + vd("P ≥ CVMe") + ", ainda que P < CTMe."),
        "destrinchando": [
            "No curto prazo o custo fixo é pago de qualquer jeito — produzindo ou não. Custo que não muda com "
            "a decisão não deve influenciá-la: por isso é " + azb("irrelevante") + " para produzir × paralisar.",
            "O que importa é se a receita cobre o custo que <b>só existe se produzir</b>: o variável. "
            "Regra: produz se " + vd("RT ≥ CV ⇔ P ≥ CVMe") + ".",
            "Faixas: P > CTMe → lucro; CVMe < P < CTMe → produz com prejuízo, menor que o custo fixo (cobre o "
            "variável e parte do fixo); P = CVMe → indiferente (prejuízo = CF nos dois casos); P < CVMe → "
            "paralisa (prejuízo = CF).",
            "A justificativa do item (P > CTMe) é a condição de <b>lucro</b>, ou de permanência no "
            + azb("longo prazo") + ", quando não há mais custo fixo. E, se valesse no curto prazo, os custos "
            "fixos seriam relevantes (estão dentro do CTMe) — o item se contradiz.",
            vm("Regra-âncora: produzir ou parar (curto prazo) → CVMe; ficar ou sair (longo prazo) → CTMe."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " 1ª oração correta; o erro foi enxertado "
                       "no “pois”, que traz o critério de longo prazo. Pista: a justificativa contradiz a "
                       "premissa, porque o CTMe embute o custo fixo que se disse irrelevante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…são irrelevantes para a decisão de continuarem produzindo, pois basta que o preço cubra o "
            "custo variável médio.”</i> → CERTO",
            "<i>“No curto prazo, a firma que paralisa a produção tem prejuízo nulo.”</i> → ERRADO (o prejuízo é "
            "igual ao custo fixo)",
        ])],
        "reescrita": ("Os custos fixos de empresas que operam em concorrência perfeita no curto prazo são "
                      "irrelevantes para a decisão de continuarem produzindo, pois " + hl("produz-se sempre que "
                      "o preço é igual ou superior ao custo variável médio") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["só"], "dificuldade": 2,
        "comentario_fonte": "Premissa correta, justificativa errada; produz se P ≥ CVMe, mesmo com P < CTMe; "
                            "P = CVMe indiferente (prejuízo = CF).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00630
    {
        "id": "ECO-E2-L00630-1", "fonte_ref": "E2-L00630", "destino": "07-A", "subtema": CP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito das estruturas de mercado, julgue (C ou E) o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado de concorrência perfeita, como existem livre entrada e livre saída de "
                      "empresas no mercado, o lucro de curto prazo de uma empresa nunca é negativo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um mercado de concorrência perfeita, como existem livre entrada e livre saída de "
                       "empresas no mercado, o lucro de curto prazo de uma empresa ") + vm("nunca é negativo")
                    + az(".")),
        "poucas": ("Livre entrada e saída é ajuste de " + azb("longo prazo") + ". No curto prazo a firma pode "
                   "ter " + vd("prejuízo") + " — e continua produzindo enquanto P ≥ CVMe."),
        "destrinchando": [
            "Curto prazo = número de firmas e planta fixos. Ninguém entra nem sai a tempo; cada firma só ajusta "
            "a quantidade (P = CMg). Se o preço cair abaixo do CTMe, há prejuízo.",
            "Com prejuízo, a firma compara: produzir dá prejuízo menor que o custo fixo se P ≥ CVMe; parar dá "
            "prejuízo exatamente igual ao custo fixo. O lucro mínimo de curto prazo, portanto, é " + vd("−CF")
            + ", nunca zero por definição.",
            "Longo prazo: prejuízo persistente faz firmas saírem; a oferta de mercado cai, o preço sobe até o "
            "mínimo do CTMe e o lucro econômico volta a " + vd("zero") + ". Lucro positivo atrai entrada e "
            "provoca o movimento inverso.",
            "Lembrete: lucro econômico zero ≠ lucro contábil zero. O custo econômico inclui o custo de "
            "oportunidade do capital; com lucro econômico nulo, o empresário recebe o retorno normal.",
            vm("Regra-âncora: entrada e saída zeram o lucro no longo prazo; no curto prazo, tudo pode."),
        ],
        "dissecando": (cz("[anacronismo · modulador absoluto]") + " O item aplica ao curto prazo um "
                       "mecanismo que só opera no longo prazo (erro de horizonte temporal) e fecha com "
                       "“nunca”. Pista: “lucro de curto prazo” + “livre entrada e saída” na mesma frase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…como existem livre entrada e livre saída, o lucro econômico de longo prazo é nulo.”</i> → "
            "CERTO",
            "<i>“No curto prazo, o prejuízo de uma firma que continua produzindo pode superar o seu custo "
            "fixo.”</i> → ERRADO (se superasse, ela pararia: prejuízo máximo = CF)",
        ])],
        "reescrita": ("Em um mercado de concorrência perfeita, " + hl("embora") + " existam livre entrada e "
                      "livre saída de empresas no mercado, o lucro de curto prazo de uma empresa "
                      + hl("pode ser negativo; só no longo prazo ele tende a zero") + "."),
        "tipo_erro": ["ANACRONISMO", "GENERALIZACAO"], "moduladores": ["nunca"], "dificuldade": 1,
        "comentario_fonte": "Entrada e saída são ajuste de longo prazo; no curto prazo pode haver prejuízo se "
                            "P cobre o CVMe; no longo prazo lucro econômico zero.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["item_repetido: mesmo enunciado de ECO-E2-L01189-1 (Nabuco, Pré-TPS/2023); mantidos os dois "
                    "por virem de provas diferentes"],
    },
    # ------------------------------------------------------------------ E2-L00631
    {
        "id": "ECO-E2-L00631-1", "fonte_ref": "E2-L00631", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito das estruturas de mercado, julgue (C ou E) o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("Na concorrência perfeita, a demanda da empresa individual pode ser representada por uma "
                      "curva negativamente inclinada com relação aos preços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na concorrência perfeita, a demanda da empresa individual pode ser representada por uma "
                       "curva ") + vm("negativamente inclinada") + az(" com relação aos preços.")),
        "poucas": ("A demanda da " + azb("empresa individual") + " é horizontal (perfeitamente elástica) ao "
                   "preço de mercado; negativamente inclinada é a demanda do " + azb("mercado") + "."),
        "destrinchando": [
            "Distinção fundamental: o mercado (indústria) enfrenta a demanda de todos os consumidores, que cai "
            "com o preço. A firma, uma entre milhares com produto idêntico, enfrenta só a fatia do mercado ao "
            "preço vigente — e essa fatia pode crescer à vontade sem mexer no preço.",
            "Por isso a demanda da firma é uma reta horizontal na altura de P: " + vd("d = RMe = RMg = P")
            + ". Acima de P, vendas zero; em P, qualquer quantidade.",
            "Por que a firma pequena “não sente” a inclinação da demanda de mercado: dobrar a produção de uma "
            "firma que tem 0,01% do mercado desloca a oferta total em 0,01% — efeito desprezível sobre P.",
            "Nas estruturas com poder de mercado (monopólio, concorrência monopolística, oligopólio), a demanda "
            "da firma é negativamente inclinada: para vender mais, ela precisa baixar o preço.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca a demanda da firma pela do mercado. O “pode” dá ar "
                       "de possibilidade, mas não há caso, dentro do modelo, em que a firma competitiva enfrente "
                       "demanda inclinada. 🔥 Item recorrente nos simulados (mesmo enunciado em várias provas)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência perfeita, a demanda de mercado pode ser representada por uma curva negativamente "
            "inclinada.”</i> → CERTO",
            "<i>“Na concorrência monopolística, a demanda da firma é horizontal.”</i> → ERRADO (troca de "
            "conceito: a diferenciação dá à firma demanda inclinada)",
        ])],
        "reescrita": ("Na concorrência perfeita, a demanda da empresa individual pode ser representada por uma "
                      + hl("reta horizontal (perfeitamente elástica) ao nível do preço de mercado") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Demanda de mercado negativamente inclinada; demanda da firma perfeitamente elástica "
                            "(horizontal) ao preço de mercado; firma price taker.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["item_repetido: mesmo enunciado de ECO-E2-L01190-1 (Nabuco, Pré-TPS/2023); mantidos os dois "
                    "por virem de provas diferentes"],
    },
    # ------------------------------------------------------------------ E2-L00632
    {
        "id": "ECO-E2-L00632-1", "fonte_ref": "E2-L00632", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito das estruturas de mercado, julgue (C ou E) o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": "Se o mercado operar em concorrência perfeita, o custo marginal será igual à receita média no ponto ótimo.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o mercado operar em concorrência perfeita, o custo marginal será igual à "
                      "<u>receita média</u> no ponto ótimo."),
        "poucas": ("Ótimo de qualquer firma: " + vd("RMg = CMg") + ". Na concorrência perfeita "
                   + vd("RMg = RMe = P") + "; logo, no ótimo, CMg = RMe."),
        "destrinchando": [
            "A condição de lucro máximo vale para toda firma: produzir até que a receita da última unidade "
            "(RMg) iguale o seu custo (CMg). Antes desse ponto, cada unidade extra aumenta o lucro; depois, "
            "reduz.",
            "Na concorrência perfeita o preço é constante para a firma: RT = P·q, então RMe = RT/q = P e "
            "RMg = P. As curvas de demanda, RMe e RMg são a mesma reta horizontal.",
            "Daí a cadeia completa: " + vm("CMg = RMg = RMe = P") + ". É essa igualdade P = CMg que torna a "
            "concorrência perfeita " + azb("alocativamente eficiente") + ": o valor que o consumidor dá à "
            "última unidade (P) é igual ao custo de produzi-la (CMg).",
            "No monopólio a cadeia se quebra: CMg = RMg < RMe = P. A diferença P − CMg é o " + azb("markup")
            + ", fonte do peso morto.",
            "Condição de segunda ordem: o CMg deve estar crescendo no ponto (cortar a RMg de baixo para "
            "cima); no ramo decrescente do CMg, a igualdade marca um mínimo de lucro.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " A banca troca “receita marginal” por “receita "
                       "média” para fazer o candidato desconfiar. Na concorrência perfeita a troca é inócua, "
                       "porque as duas coincidem; em qualquer outra estrutura, o item seria ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o mercado operar em monopólio, o custo marginal será igual à receita média no ponto "
            "ótimo.”</i> → ERRADO (troca de conceito: no monopólio CMg = RMg < RMe)",
            "<i>“Em concorrência perfeita, no ponto ótimo de curto prazo, o custo marginal é igual ao custo "
            "total médio.”</i> → ERRADO (generalização: só no equilíbrio de longo prazo)",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "P constante: P = RMg = RMe; ótimo em CMg = RMg; logo CMg = RMg = P = RMe. Comentário "
                            "da linha duplicada E2-L00866: curvas de demanda, RMe e RMg horizontais; CMg cruza "
                            "o preço no nível ótimo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 134 (linha duplicada E2-L00866)", "tipo_fonte": "TEXTO",
                           "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": ["duplicata_fundida: comentário de E2-L00866 fundido neste card",
                    "item_repetido: mesmo enunciado de ECO-E2-L01191-1 (Nabuco, Pré-TPS/2023); mantidos os dois "
                    "por virem de provas diferentes"],
    },
    # ------------------------------------------------------------------ E2-L00675
    {
        "id": "ECO-E2-L00675-1", "fonte_ref": "E2-L00675", "destino": "07-A", "subtema": LP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Sobre as estruturas de mercado, julgue (C ou E) o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("No equilíbrio de longo prazo em concorrência perfeita, as firmas operam no ponto mínimo de "
                      "suas curvas de custo médio de longo prazo, garantindo eficiência produtiva e lucro "
                      "econômico zero."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No equilíbrio de longo prazo em concorrência perfeita, as firmas operam no <u>ponto "
                      "mínimo</u> de suas curvas de custo médio de longo prazo, garantindo eficiência produtiva e "
                      "lucro econômico zero."),
        "poucas": ("A livre entrada e saída leva o preço a " + vd("P = CMg = CMeLP mínimo") + ": lucro "
                   "econômico nulo e produção ao menor custo unitário possível (" + azb("eficiência produtiva")
                   + ")."),
        "destrinchando": [
            "Lucro positivo atrai entrantes (a oferta de mercado aumenta, P cai); prejuízo expulsa firmas "
            "(oferta cai, P sobe). O processo só para quando " + vd("P = CMe") + ": lucro econômico zero.",
            "Ao mesmo tempo, cada firma maximiza lucro com " + vd("P = CMg") + ". Se P = CMg e P = CMe, então "
            "CMg = CMe — e o CMg só corta o CMe no <b>mínimo</b> deste. Logo a firma opera na "
            + azb("escala eficiente") + ".",
            azb("Eficiência produtiva") + ": produzir ao menor custo médio possível. "
            + azb("Eficiência alocativa") + ": P = CMg, o valor marginal para o consumidor iguala o custo "
            "marginal social. A concorrência perfeita de longo prazo garante as duas; o monopólio, nenhuma "
            "necessariamente.",
            "Contraste com a " + azb("concorrência monopolística") + " (" + oc("Chamberlin") + "): também há "
            "lucro zero no longo prazo, mas por tangência da demanda inclinada com o CMe, no ramo "
            "<b>decrescente</b> — a firma opera com capacidade ociosa, sem eficiência produtiva.",
            "Lucro econômico zero significa que o capital recebe exatamente seu custo de oportunidade "
            "(lucro normal), não que o empresário não ganhe nada.",
        ],
        "dissecando": (cz("[literalidade]") + " Resume o equilíbrio de longo prazo de manual. A armadilha usual "
                       "nesse tema é trocar “mínimo” por “ramo decrescente” (concorrência monopolística) ou "
                       "“lucro zero” por “lucro normal positivo” confundindo econômico e contábil."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio de longo prazo em concorrência monopolística, as firmas operam no mínimo do custo "
            "médio.”</i> → ERRADO (troca de conceito: operam no ramo decrescente, com capacidade ociosa)",
            "<i>“No longo prazo competitivo, o lucro contábil das firmas é nulo.”</i> → ERRADO (troca de "
            "conceito: nulo é o lucro econômico)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Livre entrada e saída elimina lucros e prejuízos; P = CMg = CMe no mínimo do CMe; "
                            "eficiência produtiva e alocativa.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00730
    {
        "id": "ECO-E2-L00730-1", "fonte_ref": "E2-L00730", "destino": "07-A", "subtema": CP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Considerando os conceitos de microeconomia, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No curto prazo, uma firma pode continuar operando mesmo se estiver incorrendo em prejuízo, "
                      "desde que a receita total cubra os custos variáveis totais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No curto prazo, uma firma pode continuar operando mesmo se estiver incorrendo em prejuízo, "
                      "desde que a receita total cubra os <u>custos variáveis</u> totais."),
        "poucas": ("Se " + vd("RT ≥ CV") + " (⇔ P ≥ CVMe), operar dá prejuízo <b>menor</b> que o custo fixo — "
                   "que seria pago mesmo parando. Operar minimiza a perda."),
        "destrinchando": [
            "Compare as duas opções de curto prazo: <b>parar</b> → lucro = −CF; <b>operar</b> → lucro = RT − CV "
            "− CF. Operar é melhor sempre que " + vd("RT − CV ≥ 0") + ".",
            "Dividindo por q: RT/q = P e CV/q = CVMe → a regra vira " + vd("P ≥ CVMe") + ". Daí a oferta de "
            "curto prazo ser o CMg a partir do " + azb("ponto de fechamento") + " (mínimo do CVMe).",
            "O excedente RT − CV é a " + azb("margem de contribuição") + ": ajuda a pagar o custo fixo. "
            "Exemplo: CF = 100, CV = 60, RT = 80 → operar dá −80; parar dá −100. Vale operar com prejuízo.",
            "No longo prazo não há custo fixo; a firma que não cobre o custo total (P < CTMe) sai do mercado.",
            vm("Regra-âncora: no curto prazo, a régua de operar é o custo variável, não o custo total."),
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Verdadeiro e contrário ao senso comum "
                       "(“com prejuízo, fecha”). A banca costuma inverter: “só continua operando se a receita "
                       "cobrir os custos totais” → ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, a firma só continua operando se a receita total cobrir os custos totais.”</i> → "
            "ERRADO (troca de conceito: basta cobrir os variáveis)",
            "<i>“No longo prazo, a firma permanece no mercado desde que cubra os custos variáveis.”</i> → ERRADO "
            "(anacronismo: no longo prazo todo custo é variável e a régua é o CTMe)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["pode", "desde que"], "dificuldade": 1,
        "comentario_fonte": "Regra de operação no curto prazo: RT > CV ⇔ P > CVMe; receita cobre o variável e "
                            "contribui para o fixo, irrecuperável. (Duplicata E2-L00785 com o mesmo texto.)",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata_fundida: E2-L00785 (comentário idêntico)"],
    },
    # ------------------------------------------------------------------ E2-L00848
    {
        "id": "ECO-E2-L00848-1", "fonte_ref": "E2-L00848", "destino": "07-A", "subtema": HIP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_EST2,
        "rotulo_item": "Item",
        "assertiva": ("Na concorrência perfeita, as curvas de demanda tanto da firma individual como da indústria "
                      "são negativamente inclinadas, confirmando, em ambos os casos, que as quantidades demandadas "
                      "variam inversamente aos preços de mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na concorrência perfeita, as curvas de demanda ") + vm("tanto da firma individual como")
                    + az(" da indústria são negativamente inclinadas, confirmando, ") + vm("em ambos os casos")
                    + az(", que as quantidades demandadas variam inversamente aos preços de mercado.")),
        "poucas": ("Só a demanda da " + azb("indústria") + " é negativamente inclinada. A da "
                   + azb("firma") + " é horizontal ao preço de mercado (perfeitamente elástica)."),
        "destrinchando": [
            "A indústria (mercado) responde à lei da demanda: preço maior, menos compras. Essa curva, cruzada "
            "com a oferta de mercado, determina P.",
            "A firma toma P como dado e vende qualquer quantidade a esse preço: sua demanda é uma reta "
            "horizontal, com " + vd("|ε| = ∞") + " e d = RMe = RMg = P.",
            "Não há contradição entre as duas: a firma é tão pequena que, no trecho em que ela opera, a "
            "demanda de mercado é praticamente plana. É uma questão de escala, não de comportamento diferente "
            "dos consumidores.",
            "Para o mercado, a quantidade demandada varia inversamente ao preço; para a firma, a quantidade "
            "vendida é escolhida por ela (onde P = CMg), sem efeito sobre o preço.",
        ],
        "grafico_verso": "ECO-E2-L00848-1-V1",
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " Parte verdadeira (indústria) + parte "
                       "falsa enxertada (firma), amarradas por “tanto… como” e “em ambos os casos”. 🔥 Quando o "
                       "item junta firma e mercado numa só afirmação, confira cada um separadamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência perfeita, a curva de demanda da indústria é negativamente inclinada, e a da firma "
            "individual, horizontal.”</i> → CERTO",
            "<i>“No monopólio, as curvas de demanda da firma e da indústria coincidem.”</i> → CERTO",
        ])],
        "reescrita": ("Na concorrência perfeita, " + hl("a curva de demanda da indústria é negativamente "
                      "inclinada, e a da firma individual é horizontal") + ", confirmando " + hl("apenas no "
                      "primeiro caso") + " que as quantidades demandadas variam inversamente aos preços de "
                      "mercado."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["tanto… como", "em ambos os casos"],
        "dificuldade": 1,
        "comentario_fonte": "Firmas tomadoras de preço vendem qualquer quantidade ao preço de mercado; demanda "
                            "individual horizontal; demanda de mercado negativamente inclinada.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00849
    {
        "id": "ECO-E2-L00849-1", "fonte_ref": "E2-L00849", "destino": "07-A", "subtema": CP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_EST2,
        "rotulo_item": "Item",
        "assertiva": ("Para produzir uma quantidade q de seu produto, uma firma em concorrência perfeita tem um "
                      "custo total C dado por C = 1.200 + 30q + 3q<sup>2</sup>. A respeito dessa situação "
                      "hipotética, para obter a curva de oferta da firma, basta dividir por q a expressão dada para "
                      "C e igualar o resultado obtido ao preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para produzir uma quantidade q de seu produto, uma firma em concorrência perfeita tem um "
                       "custo total C dado por C = 1.200 + 30q + 3q<sup>2</sup>. A respeito dessa situação "
                       "hipotética, para obter a curva de oferta da firma, basta ") + vm("dividir por q a "
                       "expressão dada para C") + az(" e igualar o resultado obtido ao preço.")),
        "poucas": ("Dividir C por q dá o " + azb("custo médio") + ". A oferta vem de " + vd("P = CMg")
                   + ": P = 30 + 6q (acima do mínimo do CVMe), isto é, q = (P − 30)/6."),
        "destrinchando": [
            "Decomposição: CF = " + vd("1.200") + "; CV = 30q + 3q²; CTMe = C/q = 1.200/q + 30 + 3q; "
            "CVMe = 30 + 3q; CMg = dC/dq = " + vd("30 + 6q") + ".",
            "Maximização de lucro na concorrência perfeita: RMg = P = CMg. Logo a oferta da firma é "
            + vd("P = 30 + 6q") + " ⇔ q = (P − 30)/6, válida para P ≥ mínimo do CVMe.",
            "Mínimo do CVMe: CVMe = 30 + 3q é crescente, mínimo em q → 0, com valor " + vd("30")
            + " (ponto de fechamento). Mínimo do CTMe: 1.200/q² = 3 → " + vd("q = 20") + ", CTMe = "
            + vd("150") + " — e aí CMg = 30 + 120 = 150, como deve ser (o CMg corta o CTMe no mínimo).",
            "O que o item propõe (P = CTMe) é a condição de " + azb("lucro zero") + " (nivelamento), não a "
            "de lucro máximo. Para P = 150 as duas coincidem (q = 20); para qualquer outro preço, não. Além "
            "disso, P = CTMe teria duas soluções para cada P > 150, o que não define uma oferta.",
        ],
        "grafico_verso": "ECO-E2-L00849-1-V1",
        "dissecando": (cz("[troca de conceito]") + " Troca custo marginal por custo médio. O “basta” sugere "
                       "atalho simples; a pista é que a oferta competitiva sempre vem da <b>derivada</b> do "
                       "custo total, não da divisão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…para obter a curva de oferta da firma, basta derivar C em relação a q e igualar o resultado "
            "ao preço, para preços a partir de R$ 30.”</i> → CERTO",
            "<i>“…a firma tem lucro econômico nulo ao preço de R$ 150.”</i> → CERTO (mínimo do CTMe)",
            "<i>“…ao preço de R$ 90, a firma paralisa a produção no curto prazo.”</i> → ERRADO (90 > CVMe "
            "mínimo de 30: produz q = 10, com prejuízo)",
        ])],
        "reescrita": ("[…] para obter a curva de oferta da firma, basta " + hl("derivar em relação a q") + " a "
                      "expressão dada para C e igualar o resultado obtido ao preço " + hl("(P = 30 + 6q, para "
                      "P acima do mínimo do custo variável médio)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["basta"], "dificuldade": 2,
        "comentario_fonte": "Oferta = CMg acima do CVMe; RMg = P = CMg; dividir C por q dá o custo médio, que "
                            "não gera a curva de oferta.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01188
    {
        "id": "ECO-E2-L01188-1", "fonte_ref": "E2-L01188", "destino": "07-A", "subtema": CP,
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23,
        "rotulo_item": "Item",
        "assertiva": ("A curva de oferta a curto prazo de uma firma em concorrência perfeita é igual à curva de "
                      "custo marginal para todos os níveis de produção iguais ou maiores do que o nível de "
                      "produção associado ao custo total médio mínimo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva de oferta a curto prazo de uma firma em concorrência perfeita é igual à curva de "
                       "custo marginal para todos os níveis de produção iguais ou maiores do que o nível de "
                       "produção associado ao custo ") + vm("total médio") + az(" mínimo.")),
        "poucas": ("No curto prazo a firma produz enquanto P ≥ " + azb("CVMe") + ". A oferta é o CMg a partir "
                   "do " + vd("mínimo do CVMe") + " (fechamento), não do mínimo do CTMe (nivelamento)."),
        "destrinchando": [
            "Dois pontos notáveis sobre o CMg: " + azb("ponto de fechamento") + " = mínimo do CVMe (abaixo "
            "dele a firma paralisa); " + azb("ponto de nivelamento") + " = mínimo do CTMe (lucro zero).",
            "Entre os dois a firma opera com prejuízo, porque cobre todo o custo variável e parte do fixo — "
            "melhor do que parar e perder o fixo inteiro. Esse trecho do CMg <b>faz parte</b> da oferta de "
            "curto prazo, e o item o exclui.",
            "Como o CVMe está sempre abaixo do CTMe (a diferença é o CFMe), o mínimo do CVMe ocorre num nível "
            "de produção <b>menor</b> que o do CTMe: a oferta de curto prazo começa antes.",
            "No longo prazo (sem custo fixo), a oferta da firma é o CMg de longo prazo acima do mínimo do "
            "CTMe — é daí que vem a confusão.",
            vm("Regra-âncora: oferta de curto prazo = CMg acima do mínimo do CVMe."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca CVMe por CTMe — o mesmo erro aparece em itens de "
                       "várias bancas. Pista: “curto prazo” na frase pede o custo variável. 🔥 Tema "
                       "recorrente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é igual à curva de custo marginal para todos os níveis de produção iguais ou maiores do que o "
            "nível associado ao custo variável médio mínimo.”</i> → CERTO",
            "<i>“…a oferta de longo prazo da firma é o CMg de longo prazo acima do mínimo do CVMe.”</i> → ERRADO "
            "(no longo prazo a referência é o CTMe mínimo)",
        ])],
        "reescrita": ("A curva de oferta a curto prazo de uma firma em concorrência perfeita é igual à curva de "
                      "custo marginal para todos os níveis de produção iguais ou maiores do que o nível de "
                      "produção associado ao custo " + hl("variável") + " médio mínimo."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["todos"], "dificuldade": 1,
        "comentario_fonte": "Oferta de curto prazo = CMg acima do CVMe mínimo; gráfico (CMg acima do CVMe).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 198", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo descrito no 📖; gráfico equivalente em ECO-E2-L00849-1-V1)"}],
        "alertas": [],
    },
]
