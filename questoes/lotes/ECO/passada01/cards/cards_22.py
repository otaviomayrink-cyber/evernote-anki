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
]
