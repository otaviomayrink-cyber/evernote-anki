"""Cards da redação ECO — passada 01 — lote 22 (notas 09 — Concorrência monopolística e 10 — Oligopólios)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "cham": "🧩 Modelo de Chamberlin",
    "cb": "🧮 Cournot e Bertrand",
    "stack": "🥇 Stackelberg e liderança",
    "cartel": "🤝 Cartel e conluio",
    "conc": "📏 Concentração e outras teorias",
}

COM_RT_MICRO = "A respeito dos conceitos e teorias da microeconomia, julgue os itens a seguir."
COM_RT_FIRMA = "A respeito da teoria da firma, julgue os itens a seguir."
COM_RT_ESTR = "Sobre as diferentes estruturas de mercado, julgue as afirmações a seguir."
COM_ARM = "Acerca dos modelos de oligopólio, julgue o item a seguir."
COM_NAB_OLIG = "Em relação aos modelos de oligopólio, julgue (C ou E) os seguintes itens."
COM_NAB_ESTR_1 = "Em relação às estruturas de mercado, julgue (C ou E) os seguintes itens."
COM_E1_OLIG = "Acerca das estruturas de mercado oligopolistas e da defesa da concorrência, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01658
    {
        "id": "ECO-E2-L01658-1", "fonte_ref": "E2-L01658", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_RT_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("O equilíbrio de competição monopolística no longo prazo caracteriza-se por produção abaixo da "
                      "escala eficiente, porém a livre entrada e saída de firmas levará ao resultado idêntico ao da "
                      "competição perfeita, com preço igual ao custo marginal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O equilíbrio de competição monopolística no longo prazo caracteriza-se por produção abaixo da "
                      "escala eficiente, porém a livre entrada e saída de firmas levará ao ")
                   + vm("resultado idêntico ao da competição perfeita, com preço igual ao custo marginal") + az("."),
        "poucas": ("A livre entrada zera o " + azb("lucro econômico") + " (P = CMe), como na concorrência perfeita, "
                   "mas não iguala preço e custo marginal: com demanda inclinada, " + vd("P > RMg = CMg") + "."),
        "destrinchando": [
            "No modelo de " + oc("Chamberlin") + " (<i>The Theory of Monopolistic Competition</i>, 1933), cada "
            "firma vende um produto " + azb("diferenciado") + " e enfrenta demanda negativamente inclinada; por "
            "isso a receita marginal fica abaixo do preço (RMg < P), como no monopólio.",
            "Curto prazo: a firma produz onde RMg = CMg e pode ter lucro. Longo prazo: o lucro atrai entrantes "
            "com substitutos próximos, a demanda de cada firma recua até ficar " + azb("tangente ao CMe")
            + ". No ponto de tangência, " + vd("P = CMe") + " (lucro zero) e, como a firma continua "
            "maximizando lucro, RMg = CMg < P.",
            "Consequências que distinguem as duas estruturas: (1) " + azb("ineficiência alocativa") + " — P > CMg, "
            "há um <i>markup</i> e um pequeno peso morto; (2) " + azb("excesso de capacidade") + " — a tangência "
            "ocorre no trecho <b>descendente</b> do CMe, à esquerda do custo médio mínimo (a parte do item que "
            "está certa).",
            "Na concorrência perfeita de longo prazo vale a tripla igualdade " + vd("P = CMg = CMe mínimo")
            + ": eficiência alocativa e produtiva ao mesmo tempo. Na monopolística, só sobra a igualdade P = CMe.",
            "Contrapartida usual: a ineficiência é o “preço” da " + azb("variedade") + " de produtos que o "
            "consumidor valoriza.",
            vm("Regra-âncora: concorrência monopolística no longo prazo = lucro zero (P = CMe) com P > CMg e "
               "capacidade ociosa."),
        ],
        "grafico_verso": "ECO-E2-L01658-1-V1",
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A 1ª oração (produção abaixo da escala "
                       "eficiente) é verdadeira e dá confiança; depois do “porém”, o item transporta para a "
                       "monopolística a condição P = CMg, que é exclusiva da concorrência perfeita. Pista: lucro "
                       "zero (P = CMe) não implica P = CMg. 🔥 A banca alterna “lucro zero” (CERTO) e “P = CMg” "
                       "(ERRADO) no mesmo bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a livre entrada leva as firmas monopolisticamente competitivas ao lucro econômico "
            "nulo, como na concorrência perfeita.”</i> → CERTO",
            "<i>“No longo prazo, a firma em competição monopolística produz no ponto mínimo do custo médio.”</i> → "
            "ERRADO (a tangência ocorre no trecho descendente do CMe)",
        ])],
        "reescrita": ("O equilíbrio de competição monopolística no longo prazo caracteriza-se por produção abaixo da "
                      "escala eficiente, porém a livre entrada e saída de firmas levará ao " + hl("lucro econômico "
                      "nulo, como na competição perfeita, mas com preço superior ao custo marginal") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["idêntico"], "dificuldade": 2,
        "comentario_fonte": ("Três explicações convergentes: lucro zero com P = CMe e tangência no trecho "
                             "descendente do CMe; porém P > CMg por causa da demanda inclinada; quadro comparativo "
                             "concorrência perfeita × monopolística."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 483", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico de terceiros; mecanismo redesenhado em ECO-E2-L01658-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01659
    {
        "id": "ECO-E2-L01659-1", "fonte_ref": "E2-L01659", "destino": "09", "subtema": H2["cham"],
        "tipo": "DISC", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Responda à questão a seguir, sobre estruturas de mercado.",
        "rotulo_item": "Questão",
        "assertiva": ("Caracterize e diferencie o mercado de competição perfeita do mercado de competição "
                      "monopolística, inclusive em seu equilíbrio."),
        "gabarito": "RESPOSTA", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Semelhanças: muitas firmas, livre entrada e saída e lucro econômico nulo no longo prazo. "
                      "Diferenças: na competição perfeita o produto é homogêneo, a firma é tomadora de preço "
                      "(demanda horizontal) e o equilíbrio de longo prazo tem P = CMg = CMe mínimo; na "
                      "monopolística o produto é diferenciado, a demanda da firma é negativamente inclinada e o "
                      "equilíbrio de longo prazo é a tangência da demanda com o CMe, com P = CMe > CMg e produção "
                      "abaixo da escala eficiente (capacidade ociosa)."),
        "poucas": ("As duas estruturas têm muitas firmas, livre entrada e " + vd("lucro zero no longo prazo")
                   + "; o que muda é a " + azb("diferenciação do produto") + ", que dá à firma monopolística demanda "
                   "inclinada e, daí, P > CMg e capacidade ociosa."),
        "destrinchando": [
            azb("Concorrência perfeita") + ": muitos compradores e vendedores, produto homogêneo, informação "
            "perfeita, livre entrada e saída. A firma é " + azb("tomadora de preço") + ": sua demanda é horizontal "
            "e P = RMe = RMg.",
            azb("Concorrência monopolística") + " (" + oc("Chamberlin") + ", 1933): muitas firmas e livre entrada, "
            "mas produto " + azb("diferenciado") + " (marca, qualidade, design, localização). Cada firma tem um "
            "“pequeno monopólio” da sua variedade: demanda negativamente inclinada e RMg < P. Concorre também por "
            "publicidade e atributos, não só por preço.",
            "Curto prazo: ambas podem ter lucro ou prejuízo. A perfeita produz onde " + vd("P = CMg")
            + "; a monopolística, onde " + vd("RMg = CMg") + ", cobrando o preço lido na demanda.",
            "Longo prazo: a entrada (ou saída) zera o lucro nas duas. Perfeita: " + vd("P = CMg = CMe mínimo")
            + " — eficiência alocativa e produtiva. Monopolística: a demanda da firma recua até tangenciar o CMe "
            "no trecho descendente: " + vd("P = CMe > CMg") + " — " + azb("markup") + ", pequeno peso morto e "
            + azb("excesso de capacidade") + ".",
            "Balanço de bem-estar: a monopolística é menos eficiente, mas entrega " + azb("variedade") + "; boa "
            "parte da literatura vê a ineficiência como o custo dessa diversidade.",
            vm("Regra-âncora: as duas zeram o lucro no longo prazo; só a perfeita tem P = CMg e CMe mínimo."),
        ],
        "dissecando": (cz("[exercício aberto]") + " Em C/E, a banca recorta essa comparação em itens como "
                       "“no longo prazo, a firma monopolisticamente competitiva tem lucro zero” (CERTO), “produz no "
                       "CMe mínimo” (ERRADO) ou “cobra preço igual ao custo marginal” (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Tanto na concorrência perfeita quanto na monopolística, o equilíbrio de longo prazo apresenta "
            "lucro econômico nulo.”</i> → CERTO",
            "<i>“A concorrência monopolística distingue-se da perfeita pela existência de barreiras à "
            "entrada.”</i> → ERRADO (a entrada é livre nas duas; a diferença é o produto diferenciado)",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Resposta longa de IA: características das duas estruturas, equilíbrio de curto e "
                             "de longo prazo (P = CMg = CMe mínimo × tangência com P > CMg), eficiência alocativa "
                             "e produtiva; quadro comparativo em imagem."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 484", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quadro comparativo levado ao 📖)"}],
        "alertas": ["texto_corrigido: comando da fonte com erros de digitação (“pro mercado de competição "
                    "monopolítica”) corrigidos para “do mercado de competição monopolística”"],
    },
    # ------------------------------------------------------------------ E2-L01716
    {
        "id": "ECO-E2-L01716-1", "fonte_ref": "E2-L01716", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_RT_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Num mercado em que a concorrência entre as firmas ocorre pela diferenciação de produto, a taxa "
                      "de <i>markup</i> será menor quanto mais firmas houver neste mercado e quanto menor for o grau "
                      "de diferenciação do produto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Num mercado em que a concorrência entre as firmas ocorre pela diferenciação de produto, a taxa "
                      "de <i>markup</i> será <u>menor</u> quanto <u>mais firmas</u> houver neste mercado e quanto "
                      "<u>menor</u> for o grau de diferenciação do produto."),
        "poucas": ("O " + azb("markup") + " depende da elasticidade da demanda da firma: mais concorrentes e "
                   "produtos mais parecidos = mais substitutos próximos = demanda " + vd("mais elástica")
                   + " = margem menor."),
        "destrinchando": [
            "Na concorrência monopolística, a firma maximiza lucro com RMg = CMg. Como RMg = P(1 − 1/|ε|), o "
            "preço ótimo é " + vd("P = CMg × |ε| / (|ε| − 1)") + ": o <i>markup</i> sobre o custo marginal "
            "cai quando |ε| sobe.",
            "Forma equivalente: o " + azb("índice de Lerner") + " (" + oc("Lerner") + ", 1934) " + vd("L = (P − "
            "CMg)/P = 1/|ε|") + " mede o poder de mercado. Exemplo: |ε| = 2 → L = 0,5 (preço = 2 × CMg); "
            "|ε| = 5 → L = 0,2 (preço = 1,25 × CMg).",
            "O que torna a demanda de cada firma mais elástica: (1) " + azb("mais firmas") + " — mais opções para o "
            "consumidor fugir de um aumento de preço; (2) " + azb("menos diferenciação") + " — os produtos ficam "
            "mais substituíveis entre si. As duas forças empurram para baixo a margem.",
            "Caso-limite: muitas firmas e produto homogêneo → |ε| → ∞ (demanda horizontal), L = 0 e P = CMg — "
            "a concorrência perfeita. No outro extremo, diferenciação forte (marca de luxo) sustenta margens "
            "altas mesmo com muitos concorrentes.",
            vm("Regra-âncora: markup ↑ com poder de mercado; poder de mercado ↓ com mais rivais e menos "
               "diferenciação."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item reescreve a relação markup × elasticidade sem citar a "
                       "elasticidade: a dupla condição (“mais firmas” e “menor diferenciação”) aponta no mesmo "
                       "sentido. Armadilha possível: ler “menor grau de diferenciação” como aumento de poder de "
                       "mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a taxa de markup será maior quanto menor for o grau de diferenciação do produto.”</i> → ERRADO "
            "(inversão: menos diferenciação → demanda mais elástica → markup menor)",
            "<i>“O índice de Lerner é igual ao inverso do valor absoluto da elasticidade-preço da demanda "
            "enfrentada pela firma.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["quanto mais", "quanto menor"], "dificuldade": 1,
        "comentario_fonte": "Gabarito Certo; justificativa limitada a dizer que o item descreve a concorrência "
                            "monopolística.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01726
    {
        "id": "ECO-E2-L01726-1", "fonte_ref": "E2-L01726", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_RT_ESTR,
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, a competição monopolística caracteriza-se por lucros zero, ainda que persista "
                      "o poder de monopólio, pois a livre entrada e saída de firmas faz cessar os lucros. Porém, "
                      "permanece o problema da escala de produção não ser eficiente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No longo prazo, a competição monopolística caracteriza-se por <u>lucros zero</u>, <u>ainda que "
                      "persista o poder de monopólio</u>, pois a livre entrada e saída de firmas faz cessar os "
                      "lucros. Porém, permanece o problema da <u>escala de produção não ser eficiente</u>."),
        "poucas": ("Entrada livre zera o lucro (" + vd("P = CMe") + "), mas a diferenciação mantém a demanda "
                   "inclinada — poder de mercado com " + vd("P > CMg") + " — e a tangência ocorre antes do CMe "
                   "mínimo: " + azb("escala ineficiente") + "."),
        "destrinchando": [
            "Poder de monopólio ≠ lucro. O " + azb("poder de mercado") + " é a capacidade de cobrar acima do custo "
            "marginal, e vem da diferenciação (demanda inclinada). O " + azb("lucro econômico") + " depende da "
            "posição do preço em relação ao custo <b>médio</b>. A entrada de rivais derruba o segundo, não o "
            "primeiro.",
            "Mecanismo: lucro no curto prazo → entrada de firmas com substitutos próximos → a demanda de cada "
            "firma recua (e fica mais elástica) → o processo para quando a demanda tangencia o CMe. Ali, "
            + vd("P = CMe") + " (lucro zero) e " + vd("RMg = CMg < P") + ".",
            "Como a demanda é descendente, a tangência com um CMe em U só pode ocorrer no trecho "
            + azb("descendente") + " do CMe: a firma produz menos que a escala de custo mínimo — "
            + azb("excesso de capacidade") + " (o “restaurante meio vazio”).",
            "Ineficiências que sobram: " + azb("alocativa") + " (P > CMg) e " + azb("produtiva") + " (CMe acima "
            "do mínimo). Na concorrência perfeita de longo prazo, nenhuma das duas existe.",
            vm("Regra-âncora: na monopolística de longo prazo, lucro zero convive com poder de mercado e "
               "capacidade ociosa."),
        ],
        "dissecando": (cz("[contraintuitivo · paráfrase fiel]") + " O item junta duas ideias que parecem "
                       "contraditórias (“lucros zero” e “poder de monopólio”) para induzir o ERRADO. A chave é "
                       "separar lucro (P × CMe) de poder de mercado (P × CMg). O “Porém” final está certo: a escala "
                       "continua ineficiente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a livre entrada elimina o poder de monopólio das firmas monopolisticamente "
            "competitivas.”</i> → ERRADO (elimina o lucro, não o poder de mercado)",
            "<i>“No equilíbrio de longo prazo, a firma monopolisticamente competitiva opera na parte descendente "
            "da curva de custo médio.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "PARAFRASE_FIEL"], "moduladores": ["ainda que", "Porém"],
        "dificuldade": 1,
        "comentario_fonte": ("Duas respostas convergentes: lucro zero por livre entrada, P = CMe, P > CMg, "
                             "ineficiência alocativa e produtiva, produção na parte descendente do CMe."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 517", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo mecanismo de ECO-E2-L01658-1-V1; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00019
    {
        "id": "ECO-E3-L00019-1", "fonte_ref": "E3-L00019", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("No que se refere a estruturas de mercado, cadeias e redes produtivas, competitividade e "
                    "estratégia empresarial, julgue o item seguinte."),
        "rotulo_item": "Item",
        "assertiva": ("Um mercado monopolisticamente competitivo é caracterizado pela dificultação da entrada de "
                      "novos competidores e pela diferenciação de produtos altamente substituíveis uns pelos "
                      "outros."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um mercado monopolisticamente competitivo é caracterizado pela ")
                   + vm("dificultação da entrada") + az(" de novos competidores e pela diferenciação de produtos "
                                                         "altamente substituíveis uns pelos outros."),
        "poucas": ("A concorrência monopolística tem " + azb("livre entrada e saída") + "; barreiras à entrada são "
                   "traço de " + azb("oligopólio") + " e " + azb("monopólio") + ". O resto do item (produtos "
                   "diferenciados e substitutos próximos) está certo."),
        "destrinchando": [
            "Os quatro traços da " + azb("concorrência monopolística") + ": muitas firmas; produto "
            + azb("diferenciado") + ", mas com " + azb("substitutos próximos") + " (restaurantes, roupas, "
            "salões de beleza); algum poder sobre o preço; " + vd("entrada e saída livres") + ".",
            "É a entrada livre que produz o resultado de longo prazo do modelo: lucro atrai entrantes, a demanda de "
            "cada firma recua até tangenciar o CMe e o " + vd("lucro econômico vai a zero") + ". Com barreiras, "
            "o lucro persistiria — o que é típico do monopólio e de muitos oligopólios.",
            "Quadro de barreiras: concorrência perfeita e monopolística → nenhuma relevante; " + azb("oligopólio")
            + " → economias de escala, capital inicial alto, patentes, marcas consolidadas; " + azb("monopólio")
            + " → barreiras bloqueiam totalmente a entrada (legais, naturais, controle de insumo).",
            "Sobre “altamente substituíveis”: os produtos são substitutos próximos, mas <b>não perfeitos</b> — "
            "se fossem perfeitos, a demanda de cada firma seria horizontal e o mercado seria de concorrência "
            "perfeita.",
            vm("Regra-âncora: monopolística = diferenciação + entrada livre; barreira à entrada aponta para "
               "oligopólio ou monopólio."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item mantém o traço verdadeiro (diferenciação) e troca a "
                       "condição de entrada pela de outra estrutura. Pista: “dificultação da entrada” é incompatível "
                       "com o lucro nulo de longo prazo que define o modelo. 🔥 CEBRASPE costuma testar a "
                       "monopolística pela entrada livre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mercado monopolisticamente competitivo, há muitas firmas, livre entrada e produtos "
            "diferenciados, mas substitutos próximos entre si.”</i> → CERTO",
            "<i>“No mercado monopolisticamente competitivo, os produtos são substitutos perfeitos entre "
            "si.”</i> → ERRADO (isso seria concorrência perfeita)",
        ])],
        "reescrita": ("Um mercado monopolisticamente competitivo é caracterizado pela " + hl("livre entrada")
                      + " de novos competidores e pela diferenciação de produtos altamente substituíveis uns pelos "
                      "outros."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Seis respostas convergentes: a concorrência monopolística tem livre entrada e saída; "
                             "barreiras são de oligopólio e monopólio; produtos são substitutos próximos, não "
                             "perfeitos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00103
    {
        "id": "ECO-E3-L00103-1", "fonte_ref": "E3-L00103", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": ("A partir dos conceitos e das teorias usuais de concorrência perfeita, monopólio e oligopólio, "
                    "julgue (C ou E) o item que se segue."),
        "rotulo_item": "Item",
        "assertiva": ("Quando uma nova empresa entra em um mercado monopolisticamente competitivo buscando lucros "
                      "positivos, a curva de demanda para cada uma das empresas estabelecidas se desloca para dentro, "
                      "reduzindo o preço e a quantidade recebida por essas empresas. Ou seja, o lançamento de um novo "
                      "produto por uma empresa reduzirá o preço recebido e a quantidade vendida dos produtos já "
                      "existentes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando uma nova empresa entra em um mercado monopolisticamente competitivo buscando lucros "
                      "positivos, a curva de demanda para cada uma das empresas estabelecidas <u>se desloca para "
                      "dentro</u>, reduzindo o preço e a quantidade recebida por essas empresas. Ou seja, o "
                      "lançamento de um novo produto por uma empresa <u>reduzirá o preço recebido e a quantidade "
                      "vendida</u> dos produtos já existentes."),
        "poucas": ("O entrante tira clientes das firmas já instaladas: a demanda de cada uma " + azb("recua para a "
                   "esquerda") + " e, no novo ótimo (RMg = CMg), elas vendem " + vd("menos e a preço menor")
                   + " — é o ajuste que leva o lucro a zero."),
        "destrinchando": [
            "Na " + azb("concorrência monopolística") + ", a demanda de cada firma é uma fatia da demanda do "
            "mercado. Um produto novo, substituto próximo, divide essa fatia com mais um concorrente: a cada "
            "preço, a firma estabelecida vende menos — " + azb("deslocamento para dentro") + " (esquerda) da "
            "sua curva.",
            "Com a demanda menor (e, em geral, mais elástica, porque há mais substitutos), a receita marginal "
            "também recua; o novo cruzamento RMg = CMg ocorre em quantidade menor, e o preço lido na nova "
            "demanda é mais baixo.",
            "O processo se repete enquanto houver " + azb("lucro econômico") + ": as entradas param quando a "
            "demanda de cada firma apenas " + azb("tangencia o CMe") + " (" + vd("P = CMe") + ", lucro zero). "
            "Se houvesse prejuízo, o movimento seria o inverso: saída de firmas e demanda das remanescentes "
            "deslocando-se para fora.",
            "Exemplo: uma nova hamburgueria no bairro reduz o movimento e a margem das que já existiam. Por isso "
            "o equilíbrio de longo prazo tem preço acima do CMg, mas sem lucro extraordinário — e "
            + azb("capacidade ociosa") + ".",
            vm("Regra-âncora: entrada → demanda das incumbentes para dentro → p e q caem até P = CMe."),
        ],
        "grafico_verso": "ECO-E3-L00103-1-V1",
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O item é uma descrição de manual (modelo de "
                       + oc("Chamberlin") + ") com reformulação na 2ª frase. A dúvida que derruba o candidato: "
                       "achar que só a quantidade cai, ou que o preço deveria subir para compensar. Como ambas as "
                       "curvas (demanda e RMg) recuam, p e q caem juntos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A entrada de novas empresas desloca a demanda das empresas estabelecidas para fora, elevando "
            "seus lucros no longo prazo.”</i> → ERRADO (inversão: desloca para dentro e zera o lucro)",
            "<i>“O processo de entrada cessa quando a curva de demanda de cada firma tangencia sua curva de custo "
            "médio.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentário do simulado (perda de market share com a mesma demanda dividida por mais "
                             "uma firma) e respostas de IA: deslocamento da demanda para a esquerda, demanda mais "
                             "elástica, queda de p e q até a tangência com o CTMe; exemplo do streaming."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 66", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (comentário do simulado levado ao 📖)"},
                          {"ref": "IMAGEM 67", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico de terceiros; mecanismo redesenhado em ECO-E3-L00103-1-V1)"},
                          {"ref": "IMAGEM 68", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico de terceiros, em inglês)"},
                          {"ref": "IMAGEM 69", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00156
    {
        "id": "ECO-E3-L00156-1", "fonte_ref": "E3-L00156", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": ("Apesar de o modelo de concorrência perfeita ser o fundamento para os estudos de equilíbrio de "
                    "mercado, o estudo de mercados reais apresenta outras estruturas, em geral envolvendo a fuga de "
                    "um ou mais pressupostos da concorrência perfeita. Acerca dessas estruturas de mercado, julgue o "
                    "item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O mercado de calçados é um caso de concorrência imperfeita, podendo o diferencial de preços "
                      "entre calçados ser motivado pela qualidade e pela marca."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O mercado de calçados é um caso de <u>concorrência imperfeita</u>, <u>podendo</u> o "
                      "diferencial de preços entre calçados ser motivado pela qualidade e pela marca."),
        "poucas": ("Calçados são " + azb("produtos diferenciados") + " (marca, qualidade, design): falha o "
                   "pressuposto de homogeneidade, e o mercado é de " + azb("concorrência monopolística")
                   + " — uma forma de concorrência imperfeita, com preços diferentes entre marcas."),
        "destrinchando": [
            azb("Concorrência imperfeita") + " é o gênero: toda estrutura em que falta ao menos um pressuposto "
            "da perfeita (muitos agentes, produto homogêneo, informação completa, entrada livre). Espécies: "
            + azb("concorrência monopolística") + ", " + azb("oligopólio") + " e " + azb("monopólio") + ".",
            "O mercado de calçados tem muitos produtores e entrada relativamente fácil, mas cada marca vende uma "
            "versão diferente do bem. A " + azb("diferenciação") + " (real — material, conforto — ou percebida — "
            "marca, status, publicidade) faz o consumidor não ver os pares como substitutos perfeitos.",
            "Consequência: cada firma enfrenta demanda inclinada e tem algum " + azb("poder de mercado")
            + "; marcas fortes sustentam preços mais altos sem perder todos os clientes. Na concorrência perfeita, "
            "haveria um único preço de mercado, e quem cobrasse acima dele não venderia nada.",
            "Segmentos de grandes marcas globais podem ter traços de " + azb("oligopólio") + "; o item não exige "
            "decidir isso — basta ser imperfeita, e o “podendo” deixa a motivação do diferencial em aberto.",
            vm("Regra-âncora: diferencial de preço sustentado por marca ou qualidade = produto diferenciado = "
               "concorrência imperfeita."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Item de classificação: a banca usa o "
                       "termo genérico (“concorrência imperfeita”), que abrange monopolística e oligopólio, e o "
                       "modulador “podendo”, que torna a segunda parte difícil de falsear. Quem procura erro em "
                       "“imperfeita” por pensar em “muitas firmas” cai no ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O mercado de calçados é um caso de concorrência perfeita, pois há muitos produtores.”</i> → "
            "ERRADO (muitos produtores não bastam: o produto é diferenciado)",
            "<i>“Na concorrência monopolística, a diferenciação dá a cada firma algum poder sobre o preço do seu "
            "produto.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["podendo"], "dificuldade": 1,
        "comentario_fonte": ("Comentário em imagem e duas respostas: concorrência monopolística por diferenciação "
                             "de qualidade, design e marca; diferencial de preço reflete a diferenciação; "
                             "classificação das estruturas imperfeitas."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 165", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (comentário levado ao 📖)"},
                          {"ref": "IMAGEM 166", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "absorvida (fluxograma perfeita → imperfeita → monopólio levado ao 📖)"}],
        "alertas": ["qualidade_fonte: uma das respostas da fonte define concorrência imperfeita por “poucos "
                    "vendedores” e “barreiras à entrada”, o que não vale para a concorrência monopolística; "
                    "corrigido no 📖"],
    },
    # ------------------------------------------------------------------ E3-L00308
    {
        "id": "ECO-E3-L00308-1", "fonte_ref": "E3-L00308", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": True,
        "comando": ("Considerando as diversas estruturas de mercado, suas semelhanças e diferenças, julgue (C ou E) "
                    "o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O modelo de competição monopolística está entre os dois modelos extremos: concorrência perfeita "
                      "e monopólio. Isso porque os produtos são heterogêneos, mas são substitutos próximos; cada "
                      "empresa tem o monopólio da sua marca ou sobre uma característica do seu produto, mas todos "
                      "competem acirradamente. Assim, o equilíbrio não ocorre como no mercado de concorrência "
                      "perfeita, no qual preço é igual a custo marginal, mas no ponto onde preço se iguala ao custo "
                      "médio."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": az("O modelo de competição monopolística está entre os dois modelos extremos: concorrência perfeita "
                      "e monopólio. Isso porque os produtos são heterogêneos, mas são substitutos próximos; cada "
                      "empresa tem o monopólio da sua marca ou sobre uma característica do seu produto, mas todos "
                      "competem acirradamente. Assim, o equilíbrio não ocorre como no mercado de concorrência "
                      "perfeita, no qual preço é igual a custo marginal, mas ")
                   + vm("no ponto onde preço se iguala ao custo médio") + az("."),
        "poucas": ("Tudo está certo, exceto que " + vd("P = CMe") + " só vale no " + azb("longo prazo")
                   + "; no curto prazo a firma pode ter lucro ou prejuízo. Sem o horizonte temporal, o item foi "
                   "anulado (gabarito preliminar: CERTO)."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Anulação. O gabarito preliminar era CERTO; foi alterado para ANULADO porque o item não "
                          "especifica o prazo: no curto prazo, a firma monopolisticamente competitiva produz onde "
                          "RMg = CMg e pode cobrar P > CMe (lucro) ou P < CMe (prejuízo). Com “no longo prazo” "
                          "inserido, o item seria " + vd("CERTO") + ".")],
        "destrinchando": [
            "A primeira parte é a caracterização de " + oc("Chamberlin") + " (1933) e de " + oc("Joan Robinson")
            + " (<i>The Economics of Imperfect Competition</i>, 1933): produtos " + azb("diferenciados") + " mas "
            "substitutos próximos; cada firma é “monopolista” da sua marca, mas disputa clientes com muitas "
            "outras; entrada livre.",
            "Curto prazo: como no monopólio, " + vd("RMg = CMg") + " e o preço é lido na demanda. P pode ficar "
            "acima, igual ou abaixo do CMe — lucro, lucro normal ou prejuízo.",
            "Longo prazo: lucro atrai entrantes (prejuízo expulsa firmas) até a demanda de cada firma "
            + azb("tangenciar o CMe") + ". Aí " + vd("P = CMe") + " (lucro zero), mas " + vd("P > CMg")
            + " — porque a demanda é inclinada e a tangência ocorre no trecho descendente do CMe (excesso de "
            "capacidade).",
            "Note que, mesmo no longo prazo, o “ponto de equilíbrio” continua sendo definido por RMg = CMg; "
            "P = CMe é uma <b>propriedade</b> desse ponto, garantida pela livre entrada — não a regra de decisão "
            "da firma.",
            vm("Regra-âncora: P = CMe na monopolística é resultado de longo prazo; no curto prazo, só RMg = CMg."),
        ],
        "dissecando": (cz("[outro: omissão do horizonte temporal]") + " O item é uma paráfrase correta do manual "
                       "que perdeu a qualificação “no longo prazo”. Ao julgar, desconfie de afirmações sobre "
                       "lucro zero ou P = CMe sem prazo explícito: em C/E isso pode bastar para ERRADO ou, como "
                       "aqui, para anulação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, o equilíbrio da competição monopolística ocorre no ponto em que o preço se iguala "
            "ao custo médio, mas supera o custo marginal.”</i> → CERTO",
            "<i>“No curto prazo, a firma em competição monopolística sempre obtém lucro econômico nulo.”</i> → "
            "ERRADO (modulador absoluto: pode ter lucro ou prejuízo)",
        ])],
        "reescrita": ("[...] Assim, o equilíbrio " + hl("de longo prazo") + " não ocorre como no mercado de "
                      "concorrência perfeita, no qual preço é igual a custo marginal, mas no ponto onde preço se "
                      "iguala ao custo médio."),
        "tipo_erro": ["OUTRO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Anotação “CERTO > ANULADO (não especificou curto/longo prazo)”, correção manuscrita "
                             "“(no longo prazo)” e três respostas de IA sobre curto × longo prazo, tangência, markup "
                             "e excesso de capacidade, com quadros-resumo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 419", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (correção “no longo prazo” levada à ⚠️)"},
                          {"ref": "IMAGEM 420-422, 430", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (gráficos de terceiros; mecanismo já redesenhado em "
                                   "ECO-E2-L01658-1-V1)"},
                          {"ref": "IMAGEM 423-424", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvidas (quadros-resumo curto × longo prazo levados ao 📖)"},
                          {"ref": "IMAGEM 425-429, 431", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas"}],
        "alertas": ["contestavel: item de simulado anulado (gabarito preliminar CERTO) por não especificar o prazo; "
                    "a anulação consta só da anotação da fonte"],
    },
    # ------------------------------------------------------------------ E1-0236
    {
        "id": "ECO-E1-0236-1", "fonte_ref": "E1-0236", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False, "errei": True,
        "comando": "Acerca dos cartéis e das condições que favorecem a colusão, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A cartelização de determinado mercado é facilitada quando as firmas que o compõem são do mesmo "
                      "tamanho e se confrontam com demandas elásticas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A cartelização de determinado mercado é facilitada quando as firmas que o compõem são do mesmo "
                      "tamanho e se confrontam com demandas ") + vm("elásticas") + az("."),
        "poucas": ("Firmas de porte semelhante facilitam o acordo (certo), mas o cartel só compensa se puder subir o "
                   "preço sem perder muitas vendas: precisa de demanda " + vd("inelástica") + "."),
        "destrinchando": [
            "Um " + azb("cartel") + " tenta reproduzir o monopólio: restringe a produção conjunta para elevar o "
            "preço. O ganho dessa estratégia depende de quanto a quantidade cai quando o preço sobe — isto é, da "
            + azb("elasticidade-preço da demanda de mercado") + ".",
            "Demanda " + vd("inelástica") + " (|ε| < 1): subir o preço aumenta a receita e reduz custos — o "
            "lucro conjunto cresce muito. Demanda elástica: os consumidores fogem para substitutos e o ganho do "
            "conluio é pequeno; sem ganho grande, cada membro tem pouco a perder trapaceando.",
            "Condições que facilitam o cartel (" + oc("Pindyck e Rubinfeld") + "): " + azb("poucas firmas")
            + "; " + azb("porte e custos semelhantes") + " (interesses parecidos na cota e no preço); "
            + azb("produto homogêneo") + " (fácil monitorar preços); demanda estável e pouco elástica; barreiras "
            "à entrada; e controle da maior parte da oferta (ou oferta inelástica das firmas de fora).",
            "Exemplo clássico: a " + azb("OPEP") + " nos anos 1970 — petróleo com demanda de curto prazo muito "
            "inelástica permitiu quadruplicar o preço em 1973–1974.",
            vm("Regra-âncora: cartel prospera com demanda inelástica; demanda elástica corrói o ganho do conluio."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 1ª condição (firmas do mesmo tamanho) é verdadeira; "
                       "o erro está numa palavra: “elásticas” no lugar de “inelásticas”. Itens de cartel quase sempre "
                       "testam o sentido da elasticidade. Mesmo item, com a forma correta, aparece em "
                       "ECO-E1-0303-1; com variação, em ECO-E1-0247-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A cartelização é facilitada quando as firmas têm custos semelhantes e enfrentam demanda pouco "
            "elástica.”</i> → CERTO",
            "<i>“Produtos fortemente diferenciados facilitam a manutenção do cartel.”</i> → ERRADO (dificultam "
            "monitorar preços e fixar cotas)",
        ])],
        "reescrita": ("A cartelização de determinado mercado é facilitada quando as firmas que o compõem são do mesmo "
                      "tamanho e se confrontam com demandas " + hl("inelásticas") + "."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Poder de mercado depende de baixa substituição, isto é, demanda pouco elástica; o "
                             "cartel depende da baixa elasticidade para elevar o preço acima do competitivo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE (estilo do item; a fonte traz só o ano, 2012, sem órgão)",
                    "quase_duplicata: ECO-E1-0247-1 e ECO-E1-0303-1 cobram a mesma condição (elasticidade da "
                    "demanda do cartel) com redação diferente"],
    },
    # ------------------------------------------------------------------ E1-0242
    {
        "id": "ECO-E1-0242-1", "fonte_ref": "E1-0242", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": False,
        "comando": COM_E1_OLIG,
        "rotulo_item": "Item",
        "assertiva": ("Órgãos de defesa da concorrência veem de forma positiva a prática costumeira de venda de "
                      "produtos a preços abaixo do custo de produção sob um mercado oligopolista, pois isso favorece "
                      "os consumidores e a competição entre as empresas do setor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Órgãos de defesa da concorrência ") + vm("veem de forma positiva") + az(" a prática "
                      "costumeira de venda de produtos a preços abaixo do custo de produção sob um mercado "
                      "oligopolista, ") + vm("pois isso favorece os consumidores e a competição entre as empresas do "
                                             "setor") + az("."),
        "poucas": ("Vender sistematicamente abaixo do custo é o padrão do " + azb("preço predatório") + ": sacrifica "
                   "lucro hoje para eliminar rivais e cobrar caro depois. As autoridades antitruste o reprimem."),
        "destrinchando": [
            azb("Preço predatório") + ": a firma (em geral com fôlego financeiro e poder de mercado) fixa preços "
            "abaixo do custo — o teste usual é o " + azb("custo variável médio") + ", critério de "
            + oc("Areeda e Turner") + " (1975) — para expulsar concorrentes ou desestimular entrantes. "
            "Eliminada a rivalidade, recupera as perdas com preços de monopólio (" + azb("recoupment") + ").",
            "O ganho do consumidor é só de curto prazo; no longo prazo o mercado fica mais concentrado e o "
            + azb("excedente do consumidor") + " é capturado pela firma vencedora. Por isso a prática é tratada "
            "como infração à ordem econômica, e não como “competição saudável”.",
            "Em oligopólio, a conduta é ainda mais suspeita: poucas firmas grandes, interdependência estratégica e "
            "barreiras à entrada tornam crível a recuperação do prejuízo.",
            "Nuance: preço baixo não é ilícito em si. Promoções pontuais, liquidação de estoques, lançamento de "
            "produto ou custos menores por eficiência são legítimos; o que se reprime é o preço abaixo do custo "
            "<b>injustificado</b>, com potencial de excluir rivais.",
            vm("Regra-âncora: preço abaixo do custo + poder de mercado + possibilidade de recuperação = preço "
               "predatório (infração)."),
        ],
        "dissecando": (cz("[juízo indevido · nexo indevido]") + " O item atribui às autoridades uma avaliação "
                       "positiva e a justifica com o efeito imediato (preço baixo ao consumidor), ignorando o efeito "
                       "de longo prazo. Pistas: “prática costumeira” (sistemática, não pontual) e “abaixo do custo” "
                       "em mercado oligopolista."),
        "modulos": [("⚖️ Base normativa", [
            rx("Brasil") + ": a " + vd("Lei 12.529/2011") + " (Lei de Defesa da Concorrência), art. 36, § 3º, "
            "inciso XV, lista como infração “vender mercadoria ou prestar serviços injustificadamente abaixo do "
            "preço de custo”, desde que a conduta possa produzir os efeitos do caput (limitar a concorrência, "
            "dominar mercado, aumentar lucros arbitrariamente, abusar de posição dominante). Quem julga é o "
            + rx("CADE") + ".",
        ]), ("😈 Para dificultar", [
            "<i>“A fixação de preços abaixo do custo com o objetivo de eliminar concorrentes caracteriza prática "
            "predatória, passível de punição pelos órgãos de defesa da concorrência.”</i> → CERTO",
            "<i>“Toda venda abaixo do custo de produção configura, por si só, infração à ordem econômica.”</i> → "
            "ERRADO (modulador absoluto: exige ausência de justificativa e potencial anticompetitivo)",
        ])],
        "reescrita": ("Órgãos de defesa da concorrência veem " + hl("com desconfiança") + " a prática costumeira de "
                      "venda de produtos a preços abaixo do custo de produção sob um mercado oligopolista, pois "
                      + hl("ela pode configurar preço predatório, destinado a eliminar concorrentes e a elevar "
                           "preços depois") + "."),
        "tipo_erro": ["JUIZO_INDEVIDO", "NEXO_INDEVIDO"], "moduladores": ["costumeira"], "dificuldade": 1,
        "comentario_fonte": ("Guerra de preços para remover concorrentes leva a maior concentração; agências "
                             "tentam inibir a prática porque, no longo prazo, as vencedoras capturam o excedente do "
                             "consumidor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE (estilo do item; a fonte traz só o ano, 2018, sem órgão)"],
    },
    # ------------------------------------------------------------------ E1-0244
    {
        "id": "ECO-E1-0244-1", "fonte_ref": "E1-0244", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": False,
        "comando": COM_E1_OLIG,
        "rotulo_item": "Item",
        "assertiva": ("Um mercado com apenas dois ofertantes que seja contestável com base nos pressupostos de Baumol "
                      "tem, apesar do pequeno número e grande tamanho das firmas, eficiência e preço de equilíbrio "
                      "iguais aos do mercado sob concorrência perfeita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um mercado com apenas dois ofertantes que seja <u>contestável</u> com base nos pressupostos de "
                      "Baumol tem, <u>apesar do pequeno número e grande tamanho das firmas</u>, eficiência e preço de "
                      "equilíbrio iguais aos do mercado sob concorrência perfeita."),
        "poucas": ("Num " + azb("mercado perfeitamente contestável") + " (entrada e saída livres, sem custos "
                   "irrecuperáveis), a " + azb("ameaça de entrada") + " disciplina os incumbentes: mesmo um "
                   "duopólio cobra preço competitivo e não tem lucro extraordinário."),
        "destrinchando": [
            "Teoria de " + oc("Baumol, Panzar e Willig") + " (<i>Contestable Markets and the Theory of Industry "
            "Structure</i>, 1982): o que disciplina o preço não é o número de firmas, mas a " + azb("concorrência "
            "potencial") + ". Se entrar e sair não custa nada, qualquer lucro extraordinário atrai uma entrada "
            "relâmpago (" + azb("hit-and-run") + "): o entrante vende um pouco abaixo, embolsa o lucro e sai "
            "antes que o incumbente reaja.",
            "Pressupostos: entrantes com a mesma tecnologia e acesso aos mesmos custos; " + vd("ausência de custos "
            "irrecuperáveis (sunk costs)") + "; preços dos incumbentes que não se ajustam instantaneamente à "
            "entrada.",
            "Resultado: preço igual ao custo médio (lucro zero) e, com duas ou mais firmas, " + vd("P = CMg")
            + " — o desempenho de concorrência perfeita, mesmo com firmas grandes e economias de escala.",
            "Implicação de política: o foco regulatório passa da estrutura (concentração) para as "
            + azb("barreiras à entrada e à saída") + ". Foi argumento para desregulamentar setores como a aviação "
            "nos EUA — e a experiência mostrou que custos irrecuperáveis (slots, frota, marca) tornam poucos "
            "mercados realmente contestáveis.",
            vm("Regra-âncora: contestabilidade perfeita = entrada e saída sem custo → resultado competitivo com "
               "poucas firmas."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " O item aposta no reflexo “duopólio = poder de mercado” e reforça "
                       "com “pequeno número e grande tamanho”. A palavra-chave é “contestável”: com ela, a estrutura "
                       "deixa de determinar o resultado. Variantes do mesmo tema em ECO-E1-0256-1, ECO-E2-L00291-1 e "
                       "ECO-E2-L00533-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um mercado contestável exige a presença de grande número de firmas para alcançar o resultado "
            "competitivo.”</i> → ERRADO (o número de firmas é irrelevante; importa a ameaça de entrada)",
            "<i>“Custos irrecuperáveis elevados tornam um mercado contestável.”</i> → ERRADO (inversão: são a "
            "principal barreira à contestabilidade)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["apesar de"], "dificuldade": 2,
        "comentario_fonte": ("Duas respostas: teoria de Baumol, Panzar e Willig (1982); competição potencial leva "
                             "a comportamento de concorrência perfeita mesmo com poucas firmas; mercado concentrado "
                             "que tende ao preço e custo de equilíbrio competitivo por ameaça externa."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a fonte diz que tais mercados podem ser desregulamentados “na medida em que a "
                    "entrada envolver elevados custos perdidos”; é o contrário — a contestabilidade exige ausência "
                    "de custos irrecuperáveis",
                    "banca_provavel: CEBRASPE (estilo do item; a fonte traz só o ano, 2018, sem órgão)",
                    "duplicata: comentário da linha E1-0283 (mesmo item) fundido neste card"],
    },
    # ------------------------------------------------------------------ E1-0247
    {
        "id": "ECO-E1-0247-1", "fonte_ref": "E1-0247", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False, "errei": True,
        "comando": "Acerca dos cartéis e das condições que favorecem a colusão, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O êxito de um cartel depende não apenas das similaridades — considerando-se tamanho e poder de "
                      "mercado — entre as diferentes firmas que o compõem, mas também da demanda do mercado em que o "
                      "cartel opera, a qual deve ser elástica em relação ao preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O êxito de um cartel depende não apenas das similaridades — considerando-se tamanho e poder de "
                      "mercado — entre as diferentes firmas que o compõem, mas também da demanda do mercado em que o "
                      "cartel opera, a qual deve ser ") + vm("elástica") + az(" em relação ao preço."),
        "poucas": ("A estrutura do item está certa (similaridade das firmas e demanda importam), mas o sentido está "
                   "trocado: o cartel precisa de demanda " + vd("inelástica") + " para que a alta de preço "
                   "compense a perda de vendas."),
        "destrinchando": [
            "O cartel age como um monopolista coletivo: reduz a oferta conjunta para elevar o preço. O potencial "
            "de lucro desse aumento é tanto maior quanto " + azb("menos elástica") + " for a demanda de mercado: "
            "com |ε| < 1, preço maior significa receita maior com menos produção (e menos custo).",
            "Com demanda elástica, o consumidor migra para substitutos; o preço quase não pode subir, o ganho do "
            "acordo é pequeno e não compensa o risco (multas, leniência) nem o esforço de coordenação.",
            "Similaridade entre as firmas: custos e portes parecidos geram interesses parecidos sobre preço e "
            "cotas; firmas muito diferentes discordam (a mais eficiente prefere preço mais baixo e mais "
            "mercado) e o acordo é mais difícil.",
            "Instabilidade: cada membro tem incentivo a " + azb("trapacear") + " (vender mais ao preço alto), "
            "como no dilema dos prisioneiros. Ajudam a sustentar o cartel: poucas firmas, produto homogêneo "
            "(fácil monitorar), demanda estável, barreiras à entrada e interação repetida com punição crível.",
            vm("Regra-âncora: demanda inelástica → o conluio rende muito → cartel mais provável e mais estável."),
        ],
        "dissecando": (cz("[inversão]") + " Troca de uma palavra (“elástica” por “inelástica”) num período longo "
                       "e correto no resto — pegadinha clássica de releitura. A mesma frase, com “inelástica”, é "
                       "CERTO em ECO-E1-0303-1; a mesma ideia, mais curta, aparece em ECO-E1-0236-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a demanda do mercado em que o cartel opera, a qual deve ser inelástica em relação ao preço.”</i> → "
            "CERTO",
            "<i>“O êxito do cartel independe da elasticidade da demanda, pois depende apenas da coordenação da "
            "oferta.”</i> → ERRADO (restrição indevida: a demanda determina o ganho do conluio)",
        ])],
        "reescrita": ("O êxito de um cartel depende não apenas das similaridades — considerando-se tamanho e poder de "
                      "mercado — entre as diferentes firmas que o compõem, mas também da demanda do mercado em que o "
                      "cartel opera, a qual deve ser " + hl("inelástica") + " em relação ao preço."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["deve ser"], "dificuldade": 1,
        "comentario_fonte": ("Comentário da fonte (oligopólio, coordenação da oferta, incentivo a “passar a perna”) e, "
                             "da linha duplicada, lista de Pindyck: grande diferença de lucro cartel × não "
                             "cooperação, poder de monopólio, demanda estável e não muito elástica, controle da maior "
                             "parte da produção, homogeneidade do produto."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário da fonte afirma que “a demanda de mercado do cartel não importa "
                    "para o sucesso do cartel”; a elasticidade da demanda de mercado é condição central — corrigido",
                    "duplicata: comentário da linha E2-L01201 (mesmo item) fundido neste card",
                    "quase_duplicata: ECO-E1-0303-1 traz a mesma frase com “inelástica” (CERTO); ECO-E1-0236-1 "
                    "cobra a mesma condição",
                    "banca_provavel: CEBRASPE (estilo do item; a fonte traz só o ano, 2010, sem órgão)"],
    },
    # ------------------------------------------------------------------ E1-0256
    {
        "id": "ECO-E1-0256-1", "fonte_ref": "E1-0256", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Acerca da teoria dos mercados contestáveis, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "Um mercado perfeitamente contestável é aquele em que a entrada e saída de empresas é livre e sem custos.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um mercado perfeitamente contestável é aquele em que a entrada e saída de empresas é "
                      "<u>livre e sem custos</u>."),
        "poucas": ("É a definição de " + oc("Baumol") + ": " + azb("contestabilidade perfeita") + " = entrada e "
                   "saída livres e " + vd("sem custos irrecuperáveis") + ", de modo que a ameaça de entrada "
                   "disciplina os incumbentes."),
        "destrinchando": [
            "A teoria dos " + azb("mercados contestáveis") + " (" + oc("Baumol, Panzar e Willig") + ", 1982) "
            "desloca a análise do número de firmas para as condições de entrada e saída.",
            "“Sem custos” refere-se sobretudo aos " + azb("custos irrecuperáveis") + " (<i>sunk costs</i>): "
            "investimentos que não se recuperam na saída (publicidade, ativos específicos). Custo fixo não é "
            "problema se puder ser revendido — um avião pode ser realocado para outra rota; um túnel, não.",
            "Com saída sem perdas, vale a " + azb("entrada relâmpago") + " (<i>hit-and-run</i>): qualquer preço "
            "acima do custo médio atrai um entrante que vende mais barato e sai antes de o incumbente reagir. "
            "Resultado: lucro zero e preços competitivos mesmo em monopólio ou oligopólio.",
            "Contestabilidade é um <b>contínuo</b>: quanto maiores os custos irrecuperáveis e o tempo de reação "
            "dos incumbentes, menos contestável o mercado e mais poder de mercado sobrevive.",
            vm("Regra-âncora: contestável = entrar e sair sem perder nada; o freio ao preço vem do entrante "
               "potencial."),
        ],
        "dissecando": (cz("[literalidade]") + " Item-definição. A banca costuma errar a definição trocando "
                       "“sem custos irrecuperáveis” por “com muitas firmas” ou exigindo produto homogêneo e "
                       "atomização. Ver também ECO-E1-0244-1 (duopólio contestável)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um mercado perfeitamente contestável requer grande número de firmas atuando.”</i> → ERRADO "
            "(o número de firmas é irrelevante)",
            "<i>“Em mercado perfeitamente contestável, mesmo um monopolista é levado a praticar preço igual ao "
            "custo médio.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Entrada e saída livres e sem custos irreversíveis permitem concorrência efetiva com "
                             "as estabelecidas, mesmo com poucas firmas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0303
    {
        "id": "ECO-E1-0303-1", "fonte_ref": "E1-0303", "destino": "10", "subtema": H2["cartel"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Nidi", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": "Acerca dos cartéis e das condições que favorecem a colusão, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O êxito de um cartel depende não apenas das similaridades — considerando-se tamanho e poder de "
                      "mercado — entre as diferentes firmas que o compõem, mas também da demanda do mercado em que o "
                      "cartel opera, a qual deve ser inelástica em relação ao preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O êxito de um cartel depende não apenas das similaridades — considerando-se tamanho e poder de "
                      "mercado — entre as diferentes firmas que o compõem, mas também da demanda do mercado em que o "
                      "cartel opera, a qual deve ser <u>inelástica</u> em relação ao preço."),
        "poucas": ("As duas condições estão certas: firmas parecidas coordenam-se melhor, e demanda "
                   + vd("inelástica") + " permite subir o preço perdendo poucas vendas — o que torna o conluio "
                   "lucrativo."),
        "destrinchando": [
            azb("Similaridade") + " (porte, custos, poder de mercado): interesses alinhados sobre o preço e as "
            "cotas; divisão do mercado mais simples; monitoramento recíproco mais fácil. Firmas assimétricas "
            "brigam pela cota, e a mais eficiente prefere preços menores.",
            azb("Demanda inelástica") + ": como |ε| < 1, a alta de preço aumenta a receita total e reduz o custo "
            "(produz-se menos) — o lucro conjunto dá um salto. Com demanda elástica, o ganho é pequeno, e o "
            "incentivo a manter o acordo também.",
            "Mesmo nas condições favoráveis, o cartel é instável: ao preço combinado, cada membro lucraria mais "
            "vendendo além da cota (" + azb("trapaça") + "). Sustentam o acordo a interação repetida, punições "
            "críveis e a facilidade de detectar desvios (produto homogêneo, preços públicos).",
            "Exemplos de mercados com demanda pouco elástica e histórico de cartéis: combustíveis, cimento, "
            "petróleo (" + azb("OPEP") + ").",
            vm("Regra-âncora: firmas semelhantes + demanda inelástica = terreno fértil para cartel."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Período longo com uma palavra decisiva no fim "
                       "(“inelástica”). A mesma frase, com “elástica”, é ERRADO em ECO-E1-0247-1 — o simulado "
                       "inverteu o item para testar a releitura."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a demanda do mercado em que o cartel opera, a qual deve ser elástica em relação ao preço.”</i> → "
            "ERRADO (inversão)",
            "<i>“Diferenças acentuadas de custo entre as firmas facilitam o êxito do cartel.”</i> → ERRADO "
            "(dificultam o acordo sobre preço e cotas)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["deve ser"], "dificuldade": 1,
        "comentario_fonte": ("Respostas de IA convergentes: similaridade facilita acordo e fiscalização; demanda "
                             "inelástica permite preço acima do CMg sem perder clientes; exemplo de combustíveis."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0247-1 traz a mesma frase com “elástica” (ERRADO); ECO-E1-0236-1 cobra "
                    "a mesma condição"],
    },
    # ------------------------------------------------------------------ E1-0304
    {
        "id": "ECO-E1-0304-1", "fonte_ref": "E1-0304", "destino": "10", "subtema": H2["stack"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Nidi", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": "Acerca dos modelos de oligopólio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A estratégia oligopolista associada ao equilíbrio de Stackelberg utiliza, no processo de "
                      "decisão, curvas de reação dadas pela quantidade de produção que maximiza os lucros da empresa "
                      "em relação às quantidades que ela imagina que seus concorrentes produzirão, sendo as decisões "
                      "divulgadas simultaneamente por todas as empresas participantes do mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A estratégia oligopolista associada ao equilíbrio de Stackelberg utiliza, no processo de "
                      "decisão, curvas de reação dadas pela quantidade de produção que maximiza os lucros da empresa "
                      "em relação às quantidades que ela imagina que seus concorrentes produzirão, sendo as decisões ")
                   + vm("divulgadas simultaneamente por todas as empresas") + az(" participantes do mercado."),
        "poucas": ("Stackelberg é um jogo " + azb("sequencial") + ": a líder decide primeiro e a seguidora reage. "
                   "Decisões simultâneas em quantidade são o modelo de " + azb("Cournot") + "."),
        "destrinchando": [
            "Quatro modelos clássicos de duopólio, por variável e timing: " + azb("Cournot") + " — quantidade, "
            "simultâneo; " + azb("Stackelberg") + " — quantidade, sequencial; " + azb("Bertrand") + " — preço, "
            "simultâneo; " + azb("liderança de preço") + " — preço, sequencial.",
            "Em " + oc("Stackelberg") + " (1934), a " + azb("seguidora") + " observa a produção efetiva da líder "
            "e responde pela sua " + azb("curva de reação") + " q₂ = R₂(q₁). A " + azb("líder") + " antecipa essa "
            "reação e a embute na própria maximização: escolhe q₁ sabendo que q₂ = R₂(q₁).",
            "Essa ordem dá à líder a " + azb("vantagem do primeiro a jogar") + ": comprometida com produção "
            "maior, ela força a seguidora a produzir menos. Com demanda linear e custos iguais, a líder produz "
            + vd("o dobro") + " da seguidora e lucra mais que em Cournot.",
            "A primeira parte do item (curvas de reação, quantidade que maximiza lucro dada a produção esperada "
            "da rival) descreve bem a lógica de " + oc("Cournot") + " (1838) e serve de isca: a curva de reação "
            "existe nos dois modelos; o que muda é o timing.",
            vm("Regra-âncora: simultâneo em quantidade = Cournot; sequencial em quantidade = Stackelberg."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item descreve o equilíbrio de Cournot e o rotula de "
                       "Stackelberg. Pista: “simultaneamente” e “quantidades que ela imagina” — em Stackelberg a "
                       "seguidora não imagina, ela <b>observa</b> a quantidade da líder. 🔥 A tabela "
                       "variável × timing é o tema mais cobrado de oligopólio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Stackelberg, a empresa líder incorpora a curva de reação da seguidora à sua decisão "
            "de produção.”</i> → CERTO",
            "<i>“No modelo de Cournot, uma empresa decide sua produção após observar a decisão da rival.”</i> → "
            "ERRADO (Cournot é simultâneo)",
        ])],
        "reescrita": ("A estratégia oligopolista associada ao equilíbrio de Stackelberg utiliza, no processo de "
                      "decisão, curvas de reação dadas pela quantidade de produção que maximiza os lucros da empresa "
                      "em relação às quantidades que ela imagina que seus concorrentes produzirão, sendo as decisões "
                      + hl("tomadas sequencialmente: a líder decide primeiro e a seguidora reage") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["simultaneamente"], "dificuldade": 1,
        "comentario_fonte": ("No equilíbrio de Stackelberg as decisões são encadeadas, não simultâneas (oligopólio "
                             "mais assimétrico); decisões simultâneas são de Cournot."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (112), (113), (116)-(118), (120), (121), (123).png", "tipo_fonte": "",
                           "lado": "verso", "acao": "irrecuperavel (imagens do verso não preservadas; o texto do "
                                                    "verso basta para o comentário)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0306
    {
        "id": "ECO-E1-0306-1", "fonte_ref": "E1-0306", "destino": "10", "subtema": H2["stack"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos modelos de oligopólio com empresa líder, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma estrutura de mercado oligopolista, a empresa líder escolhe um nível de produção em que a "
                      "sua receita marginal é superior ao custo marginal. O preço de mercado é o preço ao qual é "
                      "vendida a quantidade que maximiza os lucros da empresa líder. A esse preço, as seguidoras "
                      "abastecem o resto do mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma estrutura de mercado oligopolista, a empresa líder escolhe um nível de produção em que a "
                      "sua receita marginal é ") + vm("superior ao") + az(" custo marginal. O preço de mercado é o "
                      "preço ao qual é vendida a quantidade que maximiza os lucros da empresa líder. A esse preço, as "
                      "seguidoras abastecem o resto do mercado."),
        "poucas": ("No modelo da " + azb("firma dominante") + " (liderança de preço), a líder maximiza lucro como "
                   "qualquer firma: produz onde " + vd("RMg = CMg") + ", sobre a sua demanda residual. Com RMg > CMg "
                   "ainda valeria produzir mais."),
        "destrinchando": [
            "Estrutura: uma firma grande (líder) e uma franja de pequenas firmas " + azb("tomadoras de preço")
            + " (seguidoras). As seguidoras ofertam ao longo da sua curva de oferta (P = CMg de cada uma).",
            "A líder calcula a sua " + azb("demanda residual") + ": D<sub>L</sub>(P) = D(P) − S<sub>F</sub>(P), "
            "a demanda de mercado menos o que a franja oferta a cada preço. Dessa demanda tira a RMg e escolhe "
            + vd("q<sub>L</sub> tal que RMg<sub>L</sub> = CMg<sub>L</sub>") + ".",
            "O preço é o que a demanda residual associa a q<sub>L</sub>; a esse preço, as seguidoras produzem "
            "S<sub>F</sub>(P) e completam o mercado — as duas últimas frases do item estão certas.",
            "Por que não RMg > CMg: se a receita de uma unidade a mais supera o seu custo, produzi-la aumenta o "
            "lucro; a firma só para quando os dois se igualam (condição de primeira ordem de qualquer firma "
            "maximizadora, em qualquer estrutura).",
            "Não confundir com " + azb("Stackelberg") + ": lá a liderança é em quantidade e a seguidora também é "
            "estratégica; aqui as seguidoras são tomadoras de preço.",
            vm("Regra-âncora: toda firma maximizadora produz onde RMg = CMg; muda só a curva de RMg."),
        ],
        "dissecando": (cz("[dado alterado]") + " O item copia a descrição correta do modelo de firma dominante e "
                       "altera só a condição de otimização (“superior” no lugar de “igual”). Pista: nenhuma firma "
                       "maximizadora para de produzir com RMg > CMg."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de liderança de preço pela firma dominante, a demanda da líder é a demanda de mercado "
            "menos a oferta das seguidoras.”</i> → CERTO",
            "<i>“No modelo da firma dominante, as seguidoras fixam o preço e a líder abastece o resto do "
            "mercado.”</i> → ERRADO (inversão de papéis)",
        ])],
        "reescrita": ("Em uma estrutura de mercado oligopolista, a empresa líder escolhe um nível de produção em que a "
                      "sua receita marginal é " + hl("igual ao") + " custo marginal. O preço de mercado é o preço ao "
                      "qual é vendida a quantidade que maximiza os lucros da empresa líder. A esse preço, as "
                      "seguidoras abastecem o resto do mercado."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": ["superior"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito (ERRADO), uma imagem não preservada e o link do canal.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (115).png", "tipo_fonte": "", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; comentário escrito a partir do "
                                   "conteúdo)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0690
    {
        "id": "ECO-E1-0690-1", "fonte_ref": "E1-0690", "destino": "10", "subtema": H2["cb"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca dos modelos de oligopólio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo de oligopólio de Cournot, cada firma escolhe sua quantidade de produção levando em "
                      "consideração a reação esperada das concorrentes, e o equilíbrio ocorre quando nenhuma empresa "
                      "deseja alterar unilateralmente sua produção, resultando em quantidades e preços estáveis."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("No modelo de oligopólio de Cournot, cada firma escolhe sua <u>quantidade</u> de produção "
                      "levando em consideração a <u>reação esperada das concorrentes</u>, e o equilíbrio ocorre quando "
                      "<u>nenhuma empresa deseja alterar unilateralmente</u> sua produção, resultando em quantidades e "
                      "preços estáveis."),
        "poucas": ("Em " + azb("Cournot") + " as firmas escolhem " + vd("quantidades") + " simultaneamente, cada "
                   "uma dando a melhor resposta à produção esperada da rival; o equilíbrio é um "
                   + azb("equilíbrio de Nash") + ": ninguém ganha mudando sozinho."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A rigor, a firma de Cournot toma a <b>produção</b> esperada da rival como dada e supõe "
                          "que ela <b>não reage</b> (variação conjectural nula); quem antecipa a reação da rival é "
                          "a líder de Stackelberg. O CERTO se sustenta lendo “reação esperada” como a quantidade "
                          "que a rival escolherá (a sua função de reação). Numa prova CEBRASPE, a expressão "
                          "poderia ser usada para tornar o item ERRADO.")],
        "destrinchando": [
            "Modelo de " + oc("Cournot") + " (1838): duopólio, produto homogêneo, decisões " + azb("simultâneas")
            + " sobre quantidade; o preço sai da demanda de mercado para a produção total.",
            "Cada firma tem uma " + azb("função de reação") + ": a quantidade que maximiza seu lucro para cada "
            "produção possível da rival, q₁ = R₁(q₂). Quanto mais a rival produz, menos vale a pena produzir.",
            "O " + azb("equilíbrio de Cournot-Nash") + " é o cruzamento das duas funções de reação: as expectativas "
            "se confirmam e nenhuma firma quer mudar sozinha. Exemplo: P = 14 − Q, CMg = 2 → "
            + vd("q₁ = q₂ = 4") + ", Q = 8, P = 6 — entre o monopólio (Q = 6, P = 8) e a concorrência (Q = 12, "
            "P = 2).",
            "Com n firmas iguais, a produção total é " + vd("n/(n + 1)") + " da competitiva: o resultado converge "
            "para a concorrência perfeita quando n cresce.",
            vm("Regra-âncora: Cournot = quantidade + simultâneo + Nash no cruzamento das funções de reação."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Item-definição com três peças certas (quantidade, "
                       "simultaneidade implícita, Nash). O detalhe arriscado é “reação esperada”, que lembra "
                       "Stackelberg. 🔥 As bancas trocam “quantidade” por “preço” (Bertrand) ou “simultânea” por "
                       "“sequencial” (Stackelberg)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Cournot, as firmas escolhem simultaneamente os preços.”</i> → ERRADO (troca de "
            "conceito: isso é Bertrand)",
            "<i>“No equilíbrio de Cournot, cada firma está sobre a sua função de reação.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["unilateralmente"], "dificuldade": 2,
        "comentario_fonte": ("Competição por quantidades; equilíbrio de Cournot-Nash com funções de melhor resposta; "
                             "expectativas confirmadas e nenhum incentivo a desvio unilateral."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: “levando em consideração a reação esperada das concorrentes” é impreciso para "
                    "Cournot (variação conjectural nula); gabarito CERTO mantido"],
    },
    # ------------------------------------------------------------------ E2-L00240
    {
        "id": "ECO-E2-L00240-1", "fonte_ref": "E2-L00240", "destino": "10", "subtema": H2["stack"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_ARM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de duopólio de Stackelberg, a empresa seguidora, por reagir estrategicamente à "
                      "produção da líder, obtém maior lucro do que obteria em um equilíbrio de Cournot, pois "
                      "internaliza a ação da concorrente e ajusta sua produção em um nível superior."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de duopólio de Stackelberg, a empresa seguidora, por reagir estrategicamente à "
                      "produção da líder, obtém ") + vm("maior") + az(" lucro do que obteria em um equilíbrio de "
                      "Cournot, pois internaliza a ação da concorrente e ajusta sua produção em um nível ")
                   + vm("superior") + az("."),
        "poucas": ("Quem ganha com a ordem das jogadas é a " + azb("líder") + ". A seguidora produz " + vd("menos")
                   + " e lucra " + vd("menos") + " que em Cournot."),
        "destrinchando": [
            "Em " + oc("Stackelberg") + " a líder escolhe q₁ antecipando a função de reação da seguidora; ao se "
            "comprometer com uma produção grande, “ocupa” o mercado. A seguidora, diante de q₁ já fixado, só pode "
            "dar a melhor resposta — que é produzir pouco.",
            "Exemplo (P = 14 − Q, CMg = 2): Cournot → " + vd("4 + 4") + ", P = 6, lucro de " + vd("16")
            + " para cada uma. Stackelberg → líder " + vd("6") + " e seguidora " + vd("3") + ", P = 5; lucros de "
            + vd("18") + " (líder) e " + vd("9") + " (seguidora).",
            "Comparação com Cournot: a líder produz e lucra mais; a seguidora produz e lucra menos; a produção "
            "total é maior (9 > 8) e o preço menor (5 < 6) — o consumidor ganha.",
            "Reagir não dá vantagem: no jogo sequencial em quantidades, a " + azb("vantagem do primeiro a jogar")
            + " vem do compromisso. (Em jogos de preço com produtos diferenciados pode valer o contrário — "
            "vantagem do segundo a jogar —, mas não no Stackelberg clássico.)",
            vm("Regra-âncora: Stackelberg em quantidade → líder ↑ (q e lucro), seguidora ↓ (q e lucro)."),
        ],
        "dissecando": (cz("[inversão]") + " O item atribui à seguidora a vantagem que é da líder e cria um "
                       "nexo plausível (“reagir estrategicamente”, “internalizar a ação da concorrente”). Pista: "
                       "quem internaliza a função de reação da rival é a líder; a seguidora apenas reage."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Stackelberg, a seguidora produz menos do que produziria no equilíbrio de "
            "Cournot.”</i> → CERTO",
            "<i>“No modelo de Stackelberg, o lucro conjunto das duas empresas supera o de Cournot.”</i> → ERRADO "
            "(com mais produção total e preço menor, o lucro conjunto cai: 27 < 32 no exemplo)",
        ])],
        "reescrita": ("No modelo de duopólio de Stackelberg, a empresa seguidora, por reagir estrategicamente à "
                      "produção da líder, obtém " + hl("menor") + " lucro do que obteria em um equilíbrio de Cournot, "
                      "pois internaliza a ação da concorrente e ajusta sua produção em um nível " + hl("inferior")
                      + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A líder antecipa a reação da seguidora e maximiza seu lucro; a seguidora, reativa, "
                             "produz menos e lucra menos que em Cournot."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00289
    {
        "id": "ECO-E2-L00289-1", "fonte_ref": "E2-L00289", "destino": "10", "subtema": H2["stack"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_ARM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de duopólio de Stackelberg, a empresa líder, ao antecipar a função de reação da "
                      "seguidora, produz uma quantidade superior à que produziria no equilíbrio de Cournot, enquanto "
                      "a seguidora é forçada a produzir menos, resultando em um lucro maior para a líder."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de duopólio de Stackelberg, a empresa líder, <u>ao antecipar a função de reação da "
                      "seguidora</u>, produz uma quantidade <u>superior</u> à que produziria no equilíbrio de Cournot, "
                      "enquanto a seguidora é forçada a produzir <u>menos</u>, resultando em um lucro <u>maior</u> "
                      "para a líder."),
        "poucas": ("A líder usa a " + azb("vantagem do primeiro a jogar") + ": compromete-se com mais produção, a "
                   "seguidora reage produzindo menos, e a líder lucra mais que em Cournot."),
        "destrinchando": [
            "A líder resolve o problema da seguidora antes dela: sabendo que q₂ = R₂(q₁), maximiza o lucro "
            "escolhendo q₁ sobre essa curva. É um " + azb("jogo sequencial") + ", resolvido por "
            + azb("indução retroativa") + " (equilíbrio de Nash perfeito em subjogos).",
            "Como q₂ cai quando q₁ sobe (as quantidades são " + azb("substitutos estratégicos") + "), a líder tem "
            "incentivo a produzir mais do que produziria se as decisões fossem simultâneas.",
            "Números (P = 14 − Q, CMg = 2): Cournot " + vd("4 e 4") + ", lucros 16 e 16; Stackelberg "
            + vd("6 e 3") + ", lucros " + vd("18 e 9") + ". Com demanda linear e custos iguais, a líder produz a "
            "quantidade de monopólio e o dobro da seguidora.",
            "O compromisso precisa ser crível (capacidade instalada, produção já feita): se a líder pudesse "
            "rever a decisão depois, o jogo voltaria a ser simultâneo e o resultado, Cournot.",
            vm("Regra-âncora: líder de Stackelberg produz mais e lucra mais; seguidora, menos e menos."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item com quatro comparações (q da líder, q da seguidora, lucro "
                       "da líder, mecanismo) e todas no sentido certo. A banca costuma inverter uma delas — "
                       "geralmente o lucro da seguidora ou o da líder. Ver ECO-E2-L00240-1 e ECO-E2-L00678-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…resultando em lucro maior também para a seguidora.”</i> → ERRADO (a seguidora lucra menos que "
            "em Cournot)",
            "<i>“No Stackelberg com demanda linear e custos iguais, a líder produz a mesma quantidade que um "
            "monopolista produziria.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["forçada"], "dificuldade": 1,
        "comentario_fonte": ("Jogo sequencial de quantidades; vantagem de mover primeiro permite à líder escolher "
                             "o ponto da curva de reação da seguidora que maximiza seu lucro."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00291
    {
        "id": "ECO-E2-L00291-1", "fonte_ref": "E2-L00291", "destino": "10", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Acerca das estruturas de mercado e da teoria dos mercados contestáveis, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A teoria dos Mercados Contestáveis (Baumol) sugere que, na ausência de custos irrecuperáveis "
                      "(<i>sunk costs</i>) e com livre entrada e saída, mesmo um mercado oligopolista ou monopolista "
                      "pode apresentar preços próximos aos de concorrência perfeita devido à ameaça de entrada "
                      "(<i>hit-and-run entry</i>)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria dos Mercados Contestáveis (Baumol) sugere que, <u>na ausência de custos "
                      "irrecuperáveis</u> (<i>sunk costs</i>) e com livre entrada e saída, mesmo um mercado "
                      "oligopolista ou monopolista <u>pode</u> apresentar preços próximos aos de concorrência perfeita "
                      "devido à <u>ameaça de entrada</u> (<i>hit-and-run entry</i>)."),
        "poucas": ("Sem " + azb("custos irrecuperáveis") + ", entrar e sair é grátis; a " + azb("ameaça de entrada "
                   "relâmpago") + " impede o incumbente de cobrar acima do custo, mesmo sendo monopolista."),
        "destrinchando": [
            oc("Baumol") + " (com " + oc("Panzar e Willig") + ", 1982) inverteu a pergunta da organização "
            "industrial: em vez de “quantas firmas há?”, “quão fácil é entrar e sair?”.",
            "Mecanismo " + azb("hit-and-run") + ": se o incumbente cobra acima do custo médio, um entrante com a "
            "mesma tecnologia vende um pouco mais barato, captura o mercado, realiza o lucro e sai antes que o "
            "incumbente reaja. Antecipando isso, o incumbente cobra o " + vd("preço de lucro zero") + ".",
            "Condição decisiva: " + vd("custos irrecuperáveis nulos") + ". Custo fixo recuperável (revenda do "
            "ativo) não impede a contestação; o que trava a entrada é o gasto que se perde na saída "
            "(publicidade, ativos específicos, P&D).",
            "Usos e limites: a teoria apoiou desregulamentações (aviação, transporte rodoviário) e a ênfase "
            "antitruste nas barreiras à entrada; críticos apontam que custos irrecuperáveis são a regra e que "
            "incumbentes reagem rápido via preço, o que torna rara a contestabilidade perfeita.",
            vm("Regra-âncora: contestabilidade depende de entrada e saída sem custo, não do número de firmas."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Definição completa e correta, com "
                       "“pode” e “próximos” atenuando a conclusão. Itens errados do tema costumam exigir “grande "
                       "número de firmas” ou dizer que sunk costs altos favorecem a contestabilidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Baumol, a presença de elevados custos irrecuperáveis reforça a contestabilidade do "
            "mercado.”</i> → ERRADO (inversão: custos irrecuperáveis são barreira à entrada)",
            "<i>“Em mercado contestável, a estrutura concentrada não implica, por si só, poder de mercado.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "próximos"],
        "dificuldade": 1,
        "comentario_fonte": ("Estrutura de mercado é menos relevante que a facilidade de entrada e saída; lucro "
                             "extraordinário atrai entrantes que realizam o lucro e saem, disciplinando o preço."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00330
    {
        "id": "ECO-E2-L00330-1", "fonte_ref": "E2-L00330", "destino": "10", "subtema": H2["stack"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": COM_ARM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de duopólio de Stackelberg, a firma líder (que decide primeiro) incorpora a função de "
                      "reação da firma seguidora em sua maximização de lucro, resultando em uma quantidade total "
                      "produzida no mercado superior àquela observada no equilíbrio de Cournot."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de duopólio de Stackelberg, a firma líder (que decide primeiro) incorpora a função de "
                      "reação da firma seguidora em sua maximização de lucro, resultando em uma quantidade "
                      "<u>total</u> produzida no mercado <u>superior</u> àquela observada no equilíbrio de "
                      "Cournot."),
        "poucas": ("A líder aumenta mais a produção do que a seguidora a reduz: a " + vd("quantidade total sobe")
                   + " e o " + vd("preço cai") + " em relação a Cournot."),
        "destrinchando": [
            "Na função de reação linear da seguidora, cada unidade a mais da líder reduz a produção da seguidora "
            "em só " + vd("meia unidade") + " (q₂ = (a − c − q₁)/2). Logo, quando a líder expande, o total cresce.",
            "Exemplo (P = 14 − Q, CMg = 2): Cournot " + vd("4 + 4 = 8") + ", P = 6. Stackelberg " + vd("6 + 3 = 9")
            + ", P = 5. O aumento de 2 da líder só tira 1 da seguidora.",
            "Escada clássica (demanda linear, custos iguais e constantes): " + vd("Q monopólio < Q Cournot < Q "
            "Stackelberg < Q Bertrand = Q concorrência perfeita") + " — com os preços na ordem inversa. Em "
            "frações da quantidade competitiva: 1/2, 2/3, 3/4 e 1.",
            "Bem-estar: mais produção e preço menor → consumidor ganha e o peso morto diminui; o lucro conjunto "
            "das firmas cai (27 em Stackelberg contra 32 em Cournot, no exemplo).",
            vm("Regra-âncora: Stackelberg é mais competitivo que Cournot — mais quantidade, menor preço."),
        ],
        "grafico_verso": "ECO-E2-L00330-1-V1",
        "dissecando": (cz("[contraintuitivo]") + " Quem lembra só que a seguidora “é forçada a produzir menos” "
                       "conclui que o total cai. O item testa o efeito líquido: a expansão da líder supera a "
                       "contração da seguidora. Pista: “total”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio de Stackelberg, o preço de mercado é superior ao de Cournot.”</i> → ERRADO "
            "(inversão: mais quantidade → preço menor)",
            "<i>“A quantidade total de Stackelberg é inferior à de concorrência perfeita.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A líder antecipa a reação do seguidor, produz mais que em Cournot e o seguidor menos; "
                             "no agregado, quantidade maior e preço menor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00440
    {
        "id": "ECO-E2-L00440-1", "fonte_ref": "E2-L00440", "destino": "10", "subtema": H2["cb"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito das estruturas de mercado, julgue (C ou E) os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Cournot, as empresas competem escolhendo simultaneamente os níveis de preço, e o "
                      "equilíbrio ocorre quando nenhuma empresa tem incentivo para alterar seu preço, dada a decisão "
                      "da outra."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Cournot, as empresas competem escolhendo simultaneamente os níveis de ")
                   + vm("preço") + az(", e o equilíbrio ocorre quando nenhuma empresa tem incentivo para alterar seu ")
                   + vm("preço") + az(", dada a decisão da outra."),
        "poucas": ("Em " + azb("Cournot") + " a variável estratégica é a " + vd("quantidade") + "; escolha "
                   "simultânea de preços é o modelo de " + azb("Bertrand") + ". A noção de equilíbrio (Nash) está "
                   "certa."),
        "destrinchando": [
            "Quadro dos duopólios: " + azb("Cournot") + " — quantidade, simultâneo; " + azb("Bertrand")
            + " — preço, simultâneo; " + azb("Stackelberg") + " — quantidade, sequencial; "
            + azb("liderança de preço") + " — preço, sequencial. Em todos, o equilíbrio é de " + azb("Nash")
            + " (no sequencial, perfeito em subjogos).",
            "Por que a variável importa: com produto homogêneo, a competição em preço (Bertrand) derruba o preço "
            "até o custo marginal; em quantidade (Cournot), o preço fica acima do CMg, entre o de monopólio e o "
            "competitivo. Exemplo (P = 14 − Q, CMg = 2): Cournot " + vd("P = 6") + "; Bertrand " + vd("P = 2")
            + ".",
            "Interpretação de " + oc("Kreps e Scheinkman") + " (1983): quando as firmas primeiro escolhem a "
            "capacidade e depois competem em preço, o resultado é o de Cournot — por isso Cournot descreve bem "
            "setores com capacidade rígida (aço, cimento) e Bertrand, setores com capacidade flexível.",
            vm("Regra-âncora: Cournot = Quantidade; Bertrand = preço (B de “baixa o preço”)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A banca copia a definição de Bertrand e troca o nome do "
                       "modelo — ou, o que dá no mesmo, troca “quantidade” por “preço” na de Cournot. Como a lógica "
                       "de equilíbrio é idêntica nos dois, só a variável denuncia o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Bertrand, as empresas escolhem simultaneamente os preços.”</i> → CERTO",
            "<i>“No modelo de Cournot, o equilíbrio de Nash resulta em preço igual ao custo marginal.”</i> → "
            "ERRADO (isso é Bertrand com produto homogêneo; em Cournot, P > CMg)",
        ])],
        "reescrita": ("No modelo de Cournot, as empresas competem escolhendo simultaneamente os níveis de "
                      + hl("produção") + ", e o equilíbrio ocorre quando nenhuma empresa tem incentivo para alterar "
                      "sua " + hl("quantidade") + ", dada a decisão da outra."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["simultaneamente"], "dificuldade": 1,
        "comentario_fonte": ("Cournot escolhe níveis de produção, não preços; quadro dos cinco modelos (Stackelberg, "
                             "liderança de preço, Cournot, Bertrand, cartel); gráfico comparando p e Q de cada "
                             "modelo; discussão sobre equilíbrio de Nash em cada um e cartel como não-Nash."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 069", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quadro dos modelos levado ao 📖)"},
                          {"ref": "IMAGEM 070", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo gráfico redesenhado em ECO-E2-L00330-1-V1)"},
                          {"ref": "IMAGEM 071", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 072", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00479
    {
        "id": "ECO-E2-L00479-1", "fonte_ref": "E2-L00479", "destino": "10", "subtema": H2["cb"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à teoria microeconômica, julgue (C ou E) os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Bertrand, as empresas produzem uma mercadoria homogênea; cada uma delas considera "
                      "fixo o preço das suas concorrentes, e todas decidem simultaneamente qual preço será cobrado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Bertrand, as empresas produzem uma mercadoria <u>homogênea</u>; cada uma delas "
                      "considera <u>fixo o preço</u> das suas concorrentes, e todas decidem <u>simultaneamente</u> "
                      "qual preço será cobrado."),
        "poucas": ("São as três premissas de " + azb("Bertrand") + ": " + vd("produto homogêneo") + ", "
                   + vd("variável estratégica = preço") + " (com o preço rival tomado como dado) e "
                   + vd("decisão simultânea") + "."),
        "destrinchando": [
            oc("Joseph Bertrand") + " (1883) criticou " + oc("Cournot") + ": firmas reais fixam preços, não "
            "quantidades. Mantidos produto homogêneo e simultaneidade, trocou a variável estratégica.",
            "Consequência das premissas: o consumidor compra de quem cobra menos (produto idêntico). Se a rival "
            "cobra acima do custo, compensa cobrar um centavo a menos e levar o mercado todo. A guerra só para em "
            + vd("P = CMg") + " — o " + azb("paradoxo de Bertrand") + ": duas firmas bastam para o resultado "
            "competitivo, com lucro zero.",
            "O resultado depende de custos marginais iguais e constantes e de capacidade ilimitada. Se os custos "
            "diferem, a firma mais eficiente leva o mercado cobrando um pouco abaixo do custo da rival.",
            "Saídas do paradoxo: " + azb("diferenciação de produto") + " (Bertrand diferenciado: P > CMg), "
            + azb("restrição de capacidade") + " (Edgeworth; Kreps-Scheinkman → resultado de Cournot) e "
            + azb("interação repetida") + " (conluio tácito).",
            vm("Regra-âncora: Bertrand = homogêneo + preço + simultâneo → P = CMg."),
        ],
        "dissecando": (cz("[literalidade]") + " Item-definição. Para errá-lo, a banca trocaria uma das três "
                       "premissas: “quantidade” (Cournot), “sequencialmente” (liderança de preço) ou “produtos "
                       "diferenciados” (Bertrand diferenciado, cujo resultado não é P = CMg)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Bertrand, cada empresa considera fixa a quantidade produzida pela concorrente.”</i> → "
            "ERRADO (troca de conceito: essa é a conjectura de Cournot)",
            "<i>“No modelo de Bertrand com custos marginais iguais e constantes, o lucro econômico das empresas "
            "é nulo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["simultaneamente"], "dificuldade": 1,
        "comentario_fonte": ("Premissas de Bertrand (preço, produto homogêneo, decisão simultânea, preço da rival "
                             "tomado como fixo); preço igual ao custo marginal; paradoxo de Bertrand."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00532
    {
        "id": "ECO-E2-L00532-1", "fonte_ref": "E2-L00532", "destino": "10", "subtema": H2["cb"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NAB_ESTR_1,
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado em que duas empresas operam produzindo produtos homogêneos, o modelo que consegue "
                      "reproduzir resultado mais próximo ao resultado do modelo de concorrência perfeita, isto é preço "
                      "= custo marginal, é o modelo de Bertrand."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um mercado em que duas empresas operam produzindo produtos <u>homogêneos</u>, o modelo que "
                      "consegue reproduzir resultado mais próximo ao resultado do modelo de concorrência perfeita, "
                      "isto é preço = custo marginal, é o modelo de <u>Bertrand</u>."),
        "poucas": ("Com produto homogêneo e custos iguais, a competição em " + azb("preço") + " leva a "
                   + vd("P = CMg") + " com apenas duas firmas — exatamente o resultado competitivo."),
        "destrinchando": [
            "Ranking dos duopólios com produto homogêneo, demanda linear e CMg constante (P = 14 − Q, CMg = 2): "
            "monopólio/cartel " + vd("Q = 6, P = 8") + "; Cournot " + vd("Q = 8, P = 6") + "; Stackelberg "
            + vd("Q = 9, P = 5") + "; Bertrand " + vd("Q = 12, P = 2 = CMg") + ".",
            "Por que Bertrand chega lá: produto idêntico → todo cliente vai para o preço mais baixo → qualquer "
            "preço acima do CMg é atacado pela rival com um corte mínimo → o único equilíbrio de Nash é P = CMg "
            "(" + azb("paradoxo de Bertrand") + ").",
            "Cournot e Stackelberg ficam no meio do caminho porque, competindo em quantidade, cada firma internaliza "
            "que produzir mais derruba o preço das próprias vendas — e se contém.",
            "O resultado de Bertrand é frágil: com produtos diferenciados, restrição de capacidade ou custos "
            "distintos, o preço fica acima do CMg.",
            vm("Regra-âncora: Bertrand homogêneo = concorrência perfeita com duas firmas."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item explicita a condição decisiva (“produtos "
                       "homogêneos”). Sem ela — ou com produtos diferenciados —, a afirmação seria falsa. 🔥 A banca "
                       "testa a escada monopólio > Cournot > Stackelberg > Bertrand em preços."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com produtos homogêneos, o modelo de Stackelberg reproduz o resultado de concorrência "
            "perfeita.”</i> → ERRADO (troca de ator: em Stackelberg P > CMg)",
            "<i>“No modelo de Bertrand com produtos diferenciados, o preço de equilíbrio supera o custo "
            "marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["mais próximo"], "dificuldade": 1,
        "comentario_fonte": ("Competição simultânea em preço com produtos homogêneos e custos iguais leva a "
                             "P = CMg; gráfico comparando monopólio, Cournot, Stackelberg e Bertrand."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 087", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo gráfico redesenhado em ECO-E2-L00330-1-V1; ranking levado ao 📖)"}],
        "alertas": [],
    },
]
