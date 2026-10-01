"""Cards da redação 14 — ECO, passada 01 (notas 04-A e 05)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "engel": "📉 Curva renda-consumo e Engel",
    "giffen": "🥔 Bens inferiores e de Giffen",
    "cp": "🏭 Função de produção e curto prazo",
    "pmg": "📉 Produto marginal e rendimentos",
    "iso": "🗺️ Isoquantas e TMST",
    "escala": "📏 Rendimentos de escala",
}

COM_BOZAN = ("Considere as características da produção no curto e no longo prazo, bem como as escolhas do produtor "
             "em diferentes cenários. Julgue o item a seguir conforme esse contexto.")
COM_NAB_FIRMA = "Com relação à teoria da firma, julgue o item a seguir."
COM_NAB_ISO = ("Considere uma função de produção que utilize capital (K) e trabalho (L), estando as isoquantas dessa "
               "produção (Q) descritas na figura apresentada. A partir desses dados, julgue o item.")
COM_NAB_CP = ("Em relação à teoria da produção e dos custos e aos conceitos de curto prazo e longo prazo, julgue o "
              "item a seguir.")

CARDS = [
    # ------------------------------------------------------------------ E3-L00077
    {
        "id": "ECO-E3-L00077-1", "fonte_ref": "E3-L00077", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": ("Os agentes microeconômicos fazem suas escolhas de forma racional em um cenário de informações "
                    "completas e simetricamente distribuídas. A respeito da teoria do consumidor, julgue o item."),
        "rotulo_item": "Item",
        "assertiva": ("Dependendo do formato da curva de indiferença de um consumidor para dois bens, um "
                      "deslocamento paralelo de sua restrição orçamentária para cima e para a direita poderá "
                      "provocar queda no consumo de um dos bens."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Dependendo do formato</u> da curva de indiferença de um consumidor para dois bens, um "
                      "deslocamento paralelo de sua restrição orçamentária para cima e para a direita "
                      "<u>poderá</u> provocar queda no consumo de <u>um dos bens</u>."),
        "poucas": ("Deslocamento paralelo da restrição = " + azb("aumento de renda") + " com preços constantes. Se "
                   "o consumo de um bem cai quando a renda sobe, ele é um " + azb("bem inferior")
                   + " — possibilidade compatível com os axiomas, que depende do mapa de indiferença."),
        "destrinchando": [
            "A inclinação da restrição orçamentária é −p<sub>x</sub>/p<sub>y</sub>. Se ela se desloca "
            "<b>paralelamente</b> para fora, os preços relativos não mudaram: só a renda (nominal e real) "
            "aumentou.",
            "Ligando as tangências obtidas a cada nível de renda, tem-se a " + azb("curva renda-consumo")
            + "; relacionando renda e quantidade de um bem, a " + azb("curva de Engel")
            + ". Bem normal: Engel positivamente inclinada (elasticidade-renda " + vd("η > 0") + "). Bem "
            "inferior: Engel negativamente inclinada naquele trecho de renda (" + vd("η < 0") + ").",
            "Os axiomas (completude, transitividade, monotonicidade, convexidade) fixam que as curvas de "
            "indiferença são negativamente inclinadas, convexas e não se cruzam, mas <b>não</b> dizem como a "
            "inclinação muda de uma curva para a outra. É esse “formato do mapa” que decide se a nova tangência "
            "fica à esquerda (bem inferior) ou à direita (bem normal) da antiga.",
            "O item fala em “um dos bens”, e não em ambos, por boa razão: com dois bens e toda a renda gasta, "
            "os dois não podem ser inferiores ao mesmo tempo — gastar mais comprando menos de tudo é impossível "
            "(" + azb("agregação de Engel") + ").",
            "Exemplos típicos de inferioridade: transporte coletivo, cortes de carne mais baratos, produtos de "
            "segunda linha — que perdem espaço quando o consumidor enriquece.",
            vm("Regra-âncora: renda sobe e consumo cai → bem inferior; nada nos axiomas proíbe isso."),
        ],
        "grafico_verso": "ECO-E3-L00077-1-V1",
        "dissecando": (cz("[modulador relativo · contraintuitivo]") + " O item é salvo por “dependendo do formato” "
                       "e “poderá”: afirma uma possibilidade, não uma regra. A intuição apressada (“mais renda, "
                       "mais consumo de tudo”) leva a marcar ERRADO. Atenção: a definição de bem inferior olha a "
                       "renda; a de bem de Giffen olha o preço — aqui só a renda mudou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…um deslocamento paralelo da restrição para cima e para a direita provocará, necessariamente, "
            "aumento no consumo de ambos os bens.”</i> → ERRADO (modulador absoluto: só se ambos forem normais)",
            "<i>“…poderá provocar queda no consumo dos dois bens.”</i> → ERRADO (agregação de Engel: ao menos "
            "um bem precisa absorver a renda extra)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "CONTRAINTUITIVO"], "moduladores": ["dependendo", "poderá"],
        "dificuldade": 1,
        "comentario_fonte": ("Aumento de renda (deslocamento paralelo) pode reduzir o consumo de bens inferiores; "
                             "curvas de indiferença convexas permitem isso sem violar axiomas. Um dos comentários "
                             "empilhados fala em curvas de indiferença “côncavas” e em efeito substituição, "
                             "irrelevantes para uma variação pura de renda."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 32", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00077-1-V1)"},
                          {"ref": "IMAGEM 33", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "irrecuperavel"},
                          {"ref": "IMAGEM 34", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "irrecuperavel"}],
        "alertas": ["qualidade_fonte: um comentário de origem atribui o resultado a curvas de indiferença "
                    "“côncavas” e ao efeito substituição; corrigido (curvas convexas, variação pura de renda)"],
    },
    # ------------------------------------------------------------------ E3-L00273
    {
        "id": "ECO-E3-L00273-1", "fonte_ref": "E3-L00273", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": ("Segundo a teoria microeconômica e os seus axiomas da racionalidade, julgue o item a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Se a demanda por um bem diminui quando a renda aumenta, então a demanda por esse bem "
                      "também diminui quando seu preço aumenta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a demanda por um bem diminui quando a renda aumenta, ") + vm("então")
                   + az(" a demanda por esse bem também diminui quando seu preço aumenta."),
        "poucas": ("Demanda que cai com a renda define um " + azb("bem inferior") + ", mas isso não <b>garante</b> "
                   "demanda decrescente no preço: no " + azb("bem de Giffen") + " (inferior extremo), a "
                   "quantidade sobe quando o preço sobe."),
        "destrinchando": [
            "Pela decomposição de " + oc("Slutsky") + ", o efeito de uma alta de preço sobre a quantidade = "
            + azb("efeito substituição") + " + " + azb("efeito renda") + ". O efeito substituição é "
            "<b>sempre</b> contrário ao preço (preço sobe → quantidade cai).",
            "O efeito renda vem da perda de poder de compra: para o bem normal, renda real menor → compra "
            "menos (reforça o ES); para o bem inferior, renda real menor → compra <b>mais</b> (contraria o ES).",
            "Bem inferior comum: o ES domina e a demanda continua negativamente inclinada — é o caso típico. "
            "Bem de Giffen: o ER positivo supera o ES e a curva de demanda fica " + vd("positivamente "
            "inclinada") + " naquele trecho. Para isso, o bem precisa ser muito inferior, pesar muito no "
            "orçamento e ter poucos substitutos (o exemplo clássico são alimentos básicos de famílias pobres; "
            + oc("Jensen e Miller") + ", 2008, acharam comportamento Giffen no arroz em domicílios pobres da "
            "China).",
            vm("Regra-âncora: todo Giffen é inferior; nem todo inferior é Giffen."),
            "Não confundir com o " + azb("bem de Veblen") + " (consumo ostentatório), cuja demanda também pode "
            "subir com o preço, mas por efeito de status, não por efeito renda.",
        ],
        "dissecando": (cz("[nexo indevido · modulador absoluto]") + " A conclusão “também diminui” descreve o "
                       "caso mais comum, por isso parece verdadeira; o erro está no “então”, que transforma a "
                       "inferioridade em <b>garantia</b> da lei da demanda. Uma única exceção (Giffen) derruba a "
                       "implicação. 🔥 Renda e preço são classificações independentes: inferior/normal olha a "
                       "renda; Giffen/comum olha o preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todo bem de Giffen é necessariamente um bem inferior.”</i> → CERTO",
            "<i>“Se o preço de um bem inferior aumenta, a quantidade demandada desse bem necessariamente "
            "aumenta.”</i> → ERRADO (generalização: só no Giffen)",
        ])],
        "reescrita": ("Se a demanda por um bem diminui quando a renda aumenta, " + hl("isso não garante que")
                      + " a demanda por esse bem também " + hl("diminua") + " quando seu preço aumenta"
                      + hl(": se for um bem de Giffen, ela aumenta") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["então"], "dificuldade": 2,
        "comentario_fonte": ("Bem inferior não garante demanda decrescente no preço: no bem de Giffen o efeito "
                             "renda supera o substituição. Uma imagem do verso afirma que, para bens inferiores, "
                             "“quando o preço aumenta, esperamos que o consumo também aumente”; um dos comentários "
                             "descreve o sinal do efeito renda de forma confusa."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 379", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (corrigida no 📖)"}],
        "alertas": ["qualidade_fonte: a IMAGEM 379 generaliza para todo bem inferior o comportamento do bem de "
                    "Giffen (consumo sobe quando o preço sobe); corrigido"],
    },
    # ------------------------------------------------------------------ E3-L00450
    {
        "id": "ECO-E3-L00450-1", "fonte_ref": "E3-L00450", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026,
        "cacd": False, "errei": False,
        "comando": "Com base na teoria microeconômica, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considere que um consumidor gaste toda a sua renda com a compra de bens e serviços. Nessa "
                      "hipótese, é preciso que pelo menos um dos bens da cesta de consumo desse consumidor seja um "
                      "bem não inferior."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere que um consumidor <u>gaste toda a sua renda</u> com a compra de bens e serviços. "
                      "Nessa hipótese, é preciso que <u>pelo menos um</u> dos bens da cesta de consumo desse "
                      "consumidor seja um bem não inferior."),
        "poucas": ("Se a renda sobe e toda ela é gasta, o gasto total sobe; não dá para gastar mais comprando "
                   "menos de tudo. Logo, ao menos um bem tem " + azb("elasticidade-renda positiva") + " ("
                   + azb("agregação de Engel") + ")."),
        "destrinchando": [
            "Restrição orçamentária ativa: Σ p<sub>i</sub>·x<sub>i</sub> = R. Com preços constantes, se R "
            "aumenta, Σ p<sub>i</sub>·Δx<sub>i</sub> = ΔR > 0 — ao menos um Δx<sub>i</sub> precisa ser "
            "positivo.",
            "Em elasticidades, a mesma ideia vira a " + azb("agregação de Engel") + ": "
            + vd("Σ s<sub>i</sub>·η<sub>i</sub> = 1") + ", em que s<sub>i</sub> é a participação do bem no "
            "gasto e η<sub>i</sub> a elasticidade-renda. A média ponderada das elasticidades-renda é 1; se "
            "todas fossem negativas, a soma seria negativa — impossível.",
            "Corolário útil: se existe um bem inferior (η < 1), algum outro precisa ter " + vd("η > 1")
            + " (bem de luxo) para a média dar 1. Sem bem inferior, todos podem ter η = 1 (preferências "
            "homotéticas).",
            "A hipótese “gaste toda a renda” vem da " + azb("não saciedade local") + " (monotonicidade): "
            "sempre há uma cesta próxima melhor, então sobra de renda não é ótima.",
            "Agregação vizinha, cobrada no mesmo bloco: a de " + oc("Cournot") + ", Σ s<sub>i</sub>·"
            "ε<sub>ij</sub> = −s<sub>j</sub>, que amarra as elasticidades-preço.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item reproduz uma propriedade formal da demanda; "
                       "a pista é a premissa “gaste toda a sua renda”, que ativa a restrição. “Não inferior” "
                       "inclui normal e de luxo — a banca não exige que seja de luxo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é preciso que pelo menos um dos bens da cesta seja um bem de luxo.”</i> → ERRADO (troca de "
            "conceito: com preferências homotéticas, todos têm η = 1)",
            "<i>“Se a cesta contiver um bem inferior, pelo menos um outro bem terá elasticidade-renda maior que "
            "1.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["pelo menos um", "é preciso"], "dificuldade": 2,
        "comentario_fonte": ("Agregação de Engel: se todos os bens fossem inferiores, mais renda reduziria o "
                             "consumo de tudo e sobraria renda, contrariando o gasto total; a soma ponderada das "
                             "elasticidades-renda é 1. Um comentário chama a hipótese de “saciedade local” (é a "
                             "não saciedade local)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 651", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (axiomas, no 📖)"},
                          {"ref": "IMAGEM 652", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["qualidade_fonte: “princípio da saciedade local” corrigido para não saciedade local"],
    },
    # ------------------------------------------------------------------ E1-0002
    {
        "id": "ECO-E1-0002-1", "fonte_ref": "E1-0002", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2012", "ano": 2012, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à teoria da produção.",
        "rotulo_item": "Item",
        "assertiva": ("Sabendo-se que a função de serviços administrativos de determinado órgão público exige um "
                      "computador para cada funcionário, conclui-se que as isoquantas entre esses dois insumos "
                      "são formadas por linhas retas paralelas, cuja inclinação é igual a −1."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sabendo-se que a função de serviços administrativos de determinado órgão público exige um "
                      "computador para cada funcionário, conclui-se que as isoquantas entre esses dois insumos "
                      "são formadas por ") + vm("linhas retas paralelas, cuja inclinação é igual a −1") + az("."),
        "poucas": ("Um computador <b>por</b> funcionário = " + azb("proporções fixas") + " (complementares "
                   "perfeitos): q = mín(K, L), com isoquantas em <b>L</b>. Retas de inclinação −1 seriam "
                   + azb("substitutos perfeitos") + " na razão 1 por 1."),
        "destrinchando": [
            azb("Isoquanta") + " = todas as combinações de insumos que geram a mesma quantidade de produto.",
            "Funcionário sem computador não produz; computador sem funcionário também não. Com 5 funcionários e "
            "8 computadores, saem os mesmos serviços que com 5 e 5: os 3 computadores extras têm "
            + vd("produto marginal zero") + ". Daí o formato em L, com vértice na combinação eficiente.",
            "Na " + azb("função de Leontief") + " q = mín(K, L): " + azb("TMST") + " nula no trecho "
            "horizontal, infinita no vertical e indefinida no vértice; " + vd("elasticidade de substituição "
            "= 0") + ". Os vértices ficam sobre o raio K = L, que é também o " + azb("caminho de expansão")
            + ": para produzir mais, contrata-se um funcionário <b>e</b> um computador.",
            "Retas paralelas de inclinação −1 descrevem q = K + L: um computador a mais permitiria dispensar um "
            "funcionário mantendo a produção — e até produzir só com computadores, o que contradiz o "
            "enunciado.",
            vm("Regra-âncora: proporção fixa → L (σ = 0); troca à taxa constante → reta (σ = ∞)."),
        ],
        "grafico_verso": "ECO-E1-0002-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item converte a proporção “1 para 1” em inclinação −1, "
                       "confundindo a <b>razão de uso</b> (o raio K = L, de inclinação +1) com a <b>taxa de "
                       "troca</b> ao longo da isoquanta. Pista: “exige … para cada” = complementaridade, nunca "
                       "substituição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as isoquantas têm formato de L, e o caminho de expansão é uma reta que parte da origem.”</i> "
            "→ CERTO",
            "<i>“…a elasticidade de substituição entre computadores e funcionários é infinita.”</i> → ERRADO "
            "(é nula: proporções fixas)",
        ])],
        "reescrita": ("Sabendo-se que a função de serviços administrativos de determinado órgão público exige um "
                      "computador para cada funcionário, conclui-se que as isoquantas entre esses dois insumos "
                      "são formadas por " + hl("ângulos retos (formato de L), com vértices sobre o raio de um "
                      "computador por funcionário") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Insumos complementares em proporção fixa: isoquantas em L (Leontief, q = mín(K, L)); "
                             "retas paralelas indicariam substitutos perfeitos. Vários comentários empilhados, "
                             "com exemplo numérico e figura de Leontief com caminho de expansão."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (36).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (substituída por ECO-E1-0002-1-V1)"},
                          {"ref": "00020.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (Leontief com caminho de expansão, redesenhada em "
                                   "ECO-E1-0002-1-V1)"}],
        "alertas": ["ocr: “exije” corrigido para “exige”",
                    "banca_provavel: CEBRASPE (não confirmada: a fonte só traz o ano, 2012)"],
    },
    # ------------------------------------------------------------------ E1-0220
    {
        "id": "ECO-E1-0220-1", "fonte_ref": "E1-0220", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às isoquantas e à taxa marginal de substituição técnica.",
        "rotulo_item": "Item",
        "assertiva": ("A taxa marginal de substituição técnica, TMST, mede a inclinação da isoquanta. Se os "
                      "insumos são complementares perfeitos, as isoquantas são lineares."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A taxa marginal de substituição técnica, TMST, mede a inclinação da isoquanta. Se os "
                      "insumos são complementares perfeitos, as isoquantas ") + vm("são lineares") + az("."),
        "poucas": ("A 1ª frase está certa. Complementares perfeitos têm isoquantas em " + azb("L")
                   + "; isoquantas lineares são as dos " + azb("substitutos perfeitos") + "."),
        "destrinchando": [
            azb("TMST") + " = quanto de capital se pode retirar ao acrescentar uma unidade de trabalho, "
            "mantida a produção: TMST = −ΔK/ΔL = " + vd("PMg<sub>L</sub>/PMg<sub>K</sub>") + ". "
            "Geometricamente, é o módulo da inclinação da isoquanta.",
            "Três formatos que a banca alterna: " + azb("retas") + " → substitutos perfeitos (q = aK + bL), "
            "TMST constante; " + azb("L") + " → complementares perfeitos (q = mín(aK, bL)), sem substituição; "
            + azb("convexas") + " → caso usual (Cobb-Douglas), TMST decrescente ao longo da curva.",
            "Complementares perfeitos são usados em proporção fixa (motorista e caminhão, funcionário e "
            "computador): acrescentar só um deles não muda a produção, e o produto marginal do fator "
            "excedente é zero. A TMST é nula no trecho horizontal e infinita no vertical.",
            vm("Regra-âncora: complementar → L; substituto → reta."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Frase 1 correta para dar confiança; o erro está no "
                       "formato atribuído aos complementares, trocado com o dos substitutos. Pista: "
                       "“complementares perfeitos” e “lineares” nunca andam juntos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se os insumos são substitutos perfeitos, a TMST é constante ao longo de cada isoquanta.”</i> "
            "→ CERTO",
            "<i>“Ao longo de uma isoquanta convexa, a TMST é crescente à medida que se usa mais trabalho.”</i> "
            "→ ERRADO (inversão: é decrescente)",
        ])],
        "reescrita": ("A taxa marginal de substituição técnica, TMST, mede a inclinação da isoquanta. Se os "
                      "insumos são complementares perfeitos, as isoquantas " + hl("têm formato de L") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito e uma imagem não preservada.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (73).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": [],
    },
]
