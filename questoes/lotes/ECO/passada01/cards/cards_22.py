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
]
