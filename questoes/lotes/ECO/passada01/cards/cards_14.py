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
            "Corolário útil: se existe um bem inferior (η < 0, abaixo da média 1), algum outro precisa ter " + vd("η > 1")
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
        "alertas": ["texto_corrigido: “exije” corrigido para “exige”",
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
    # ------------------------------------------------------------------ E1-0226
    {
        "id": "ECO-E1-0226-1", "fonte_ref": "E1-0226", "destino": "05", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, acerca dos horizontes de curto e de longo prazo na teoria da produção.",
        "rotulo_item": "Item",
        "assertiva": ("Curto prazo é o período em que pelo menos um dos fatores de produção permanece constante "
                      "ou fixo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Curto prazo é o período em que <u>pelo menos um</u> dos fatores de produção permanece "
                      "constante ou fixo."),
        "poucas": ("É a definição de manual: no " + azb("curto prazo") + " há ao menos um " + azb("fator fixo")
                   + "; no " + azb("longo prazo") + ", todos são variáveis."),
        "destrinchando": [
            "A distinção é <b>analítica</b>, não de calendário: curto prazo é o horizonte em que a firma ainda "
            "não consegue ajustar algum insumo (em geral a planta, o capital). Para uma barraca de feira, isso "
            "dura dias; para uma hidrelétrica, anos.",
            "Consequências que a banca cobra em seguida: só no curto prazo existem " + azb("custos fixos")
            + " (no longo prazo todo custo é variável); só no curto prazo vale a " + azb("lei dos rendimentos "
            "marginais decrescentes") + ", que pressupõe um fator fixo; no longo prazo, fala-se em "
            + azb("rendimentos de escala") + ".",
            "Na representação gráfica, o curto prazo com capital fixo é uma reta horizontal (K = K̄) no mapa de "
            "isoquantas: a firma só anda ao longo dela, variando o trabalho.",
            "A divisão em períodos (mercado, curto e longo) foi sistematizada por " + oc("Alfred Marshall")
            + " nos <i>Princípios de Economia</i> (1890).",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição, e o ponto de risco é o “pelo menos um”: "
                       "a banca costuma trocá-lo por “todos” (ERRADO) ou por um prazo em meses."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Curto prazo é o período em que todos os fatores de produção permanecem fixos.”</i> → ERRADO "
            "(modulador absoluto: basta um fator fixo)",
            "<i>“Curto prazo é o período inferior a um ano em que a firma não altera sua planta.”</i> → ERRADO "
            "(não é prazo de calendário)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["pelo menos um"], "dificuldade": 1,
        "comentario_fonte": ("Curto prazo: pelo menos um fator fixo. Longo prazo: todos os fatores variáveis."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0227
    {
        "id": "ECO-E1-0227-1", "fonte_ref": "E1-0227", "destino": "05", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, acerca dos horizontes de curto e de longo prazo na teoria da produção.",
        "rotulo_item": "Item",
        "assertiva": "No longo prazo, uma firma pode variar seu insumo capital mas não seu insumo mão de obra.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No longo prazo, uma firma pode variar seu insumo capital ")
                   + vm("mas não seu insumo mão de obra") + az("."),
        "poucas": ("No " + azb("longo prazo") + " <b>todos</b> os insumos são variáveis — capital e mão de obra. "
                   "O item cria uma restrição que não existe."),
        "destrinchando": [
            "Longo prazo é, por definição, o horizonte em que a firma ajusta <b>qualquer</b> insumo: muda de "
            "planta, compra máquinas, contrata ou demite, e pode até entrar ou sair do mercado.",
            "O item ainda inverte a figura típica do " + azb("curto prazo") + ": nos manuais, o fator fixo "
            "costuma ser o <b>capital</b> (a planta), e o variável, o <b>trabalho</b> — contratar horas de "
            "trabalho é mais rápido do que erguer uma fábrica.",
            "Por isso a função de produção de curto prazo se escreve q = f(K̄, L), e a de longo prazo, "
            "q = f(K, L), com os dois insumos livres. No longo prazo, a escolha é o ponto de tangência entre "
            "isoquanta e isocusto: " + vd("TMST = w/r") + ".",
            vm("Regra-âncora: longo prazo não tem fator fixo — nem capital, nem trabalho."),
        ],
        "dissecando": (cz("[restrição indevida · inversão]") + " A restrição “mas não seu insumo mão de obra” é "
                       "falsa em qualquer leitura: no longo prazo nada é fixo e, no curto prazo usual, o fixo é o "
                       "capital, não o trabalho. Pista: qualquer limitação a insumos no “longo prazo” é ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, uma firma pode variar seu insumo mão de obra, mas não seu insumo "
            "capital.”</i> → CERTO",
            "<i>“No longo prazo, os custos fixos da firma tendem a zero, mas não desaparecem.”</i> → ERRADO "
            "(no longo prazo todo custo é variável)",
        ])],
        "reescrita": ("No longo prazo, uma firma pode variar seu insumo capital " + hl("e também seu insumo mão de "
                      "obra") + "."),
        "tipo_erro": ["RESTRICAO", "INVERSAO"], "moduladores": ["mas não"], "dificuldade": 1,
        "comentario_fonte": "No longo prazo, todos os fatores de produção são variáveis, inclusive capital e mão de obra.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0228
    {
        "id": "ECO-E1-0228-1", "fonte_ref": "E1-0228", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo às isoquantas e à taxa marginal de substituição técnica.",
        "rotulo_item": "Item",
        "assertiva": ("Uma isoquanta representa todas as possíveis combinações de insumos que resultam no mesmo "
                      "custo de produção. Sua inclinação descendente pode ser explicada pela taxa marginal de "
                      "substituição técnica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma isoquanta representa todas as possíveis combinações de insumos que resultam no mesmo ")
                   + vm("custo de produção") + az(". Sua inclinação descendente pode ser explicada pela taxa "
                                                  "marginal de substituição técnica."),
        "poucas": ("Isoquanta = mesma <b>quantidade</b> produzida. A curva de mesmo <b>custo</b> é a "
                   + azb("isocusto") + ". A 2ª frase está certa."),
        "destrinchando": [
            azb("Isoquanta") + ": combinações (K, L) com o mesmo produto q. É o análogo, na firma, da curva de "
            "indiferença do consumidor — com a vantagem de o nível (q) ser mensurável.",
            azb("Isocusto") + ": combinações com o mesmo gasto C = wL + rK; reta de inclinação "
            + vd("−w/r") + ". Ela é a “restrição orçamentária” da firma.",
            "A inclinação negativa da isoquanta decorre de os produtos marginais serem positivos: para manter q "
            "ao tirar capital, é preciso pôr trabalho. Essa taxa de troca é a " + azb("TMST") + " = "
            + vd("PMg<sub>L</sub>/PMg<sub>K</sub>") + " — por isso a 2ª frase é aceitável.",
            "As duas curvas se encontram na escolha ótima de longo prazo: minimizar o custo de produzir q (ou "
            "maximizar q com custo C) leva à tangência " + vd("TMST = w/r") + ", ou seja, "
            "PMg<sub>L</sub>/w = PMg<sub>K</sub>/r.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca isoquanta por isocusto, curvas que aparecem juntas no "
                       "mesmo gráfico. A 2ª frase, correta, serve de isca. Pista: o próprio nome entrega o "
                       "conceito."),
        "modulos": [("🧠 Mnemônico", ["ISO = mesmo; QUANTA = <b>quantidade</b>. ISO + CUSTO = mesmo "
                                      "<b>custo</b>."]),
                    ("😈 Para dificultar", [
            "<i>“A isocusto representa as combinações de insumos de mesmo custo, e sua inclinação é dada pela "
            "razão entre os preços dos insumos.”</i> → CERTO",
            "<i>“No ponto ótimo, a TMST iguala a razão entre os produtos médios dos insumos.”</i> → ERRADO "
            "(é a razão entre os preços, w/r)",
        ])],
        "reescrita": ("Uma isoquanta representa todas as possíveis combinações de insumos que resultam na "
                      + hl("mesma quantidade produzida") + ". Sua inclinação descendente pode ser explicada pela "
                      "taxa marginal de substituição técnica."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A curva de combinações de mesmo custo é a isocusto. ISO = mesmo; QUANTA = quantidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (76).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0245
    {
        "id": "ECO-E1-0245-1", "fonte_ref": "E1-0245", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2010", "ano": 2010, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo à teoria da produção.",
        "rotulo_item": "Item",
        "assertiva": ("Se, para determinada empresa, trabalhadores sem qualificação específica e máquinas executam "
                      "exatamente o mesmo tipo de tarefa, então, para essa empresa, as isoquantas entre esses dois "
                      "insumos podem ser representadas como linhas retas paralelas."),
        "gabarito": "CERTO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("Se, para determinada empresa, trabalhadores sem qualificação específica e máquinas executam "
                      "<u>exatamente o mesmo tipo de tarefa</u>, então, para essa empresa, as isoquantas entre "
                      "esses dois insumos <u>podem ser</u> representadas como linhas retas paralelas."),
        "poucas": ("Insumos que fazem exatamente a mesma tarefa são " + azb("substitutos perfeitos")
                   + ": q = aL + bM, com isoquantas " + vd("retas e paralelas") + " (TMST constante)."),
        "destrinchando": [
            "Se trabalhador e máquina fazem o mesmo serviço, a empresa troca um pelo outro a uma taxa fixa — "
            "digamos, uma máquina substitui dois trabalhadores — em qualquer ponto da produção. Função: "
            "q = aL + bM.",
            "Daí a isoquanta reta, com inclinação " + vd("−a/b") + " (não necessariamente −1), e a "
            + azb("TMST constante") + ". Como a inclinação é a mesma para todo nível de produto, as isoquantas "
            "são <b>paralelas</b>. Elasticidade de substituição: " + vd("infinita") + ".",
            "Consequência para o custo: com isoquanta reta, a firma tende a uma " + azb("solução de canto")
            + " — usa só o insumo relativamente mais barato (compara TMST com w/r).",
            "Contraste com a complementaridade: “um computador para cada funcionário” (proporção fixa) gera "
            "isoquantas em L, sem substituição possível.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " “Exatamente o mesmo tipo de tarefa” é a "
                       "descrição verbal de substitutos perfeitos; “podem ser” torna o item ainda mais seguro. "
                       "🔥 A banca alterna este par: mesma tarefa → reta; uso conjunto obrigatório → L."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as isoquantas entre esses dois insumos são, necessariamente, retas com inclinação −1.”</i> → "
            "ERRADO (a inclinação depende da produtividade relativa: −a/b)",
            "<i>“…a empresa usará sempre os dois insumos em proporção fixa.”</i> → ERRADO (troca de conceito: "
            "isso é complementaridade)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["podem ser", "exatamente"],
        "dificuldade": 1,
        "comentario_fonte": "Verso só com uma imagem não preservada; gabarito ausente na fonte.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (77).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": ["nota_redacao: gabarito resolvido — a fonte não traz gabarito (verso só com imagem perdida); resolvido como "
                    "CERTO pelo conteúdo (substitutos perfeitos → isoquantas retas paralelas)",
                    "banca_provavel: CEBRASPE (não confirmada: a fonte só traz o ano, 2010)"],
    },
    # ------------------------------------------------------------------ E2-L00036
    {
        "id": "ECO-E2-L00036-1", "fonte_ref": "E2-L00036", "destino": "05", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("No curto prazo, a empresa pode aumentar sua produção aumentando proporcionalmente todos os "
                      "seus fatores de produção, levando a um aumento proporcional na produção total, sem "
                      "interferir nos rendimentos decrescentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No curto prazo, a empresa pode aumentar sua produção ")
                   + vm("aumentando proporcionalmente todos os seus fatores de produção, levando a um aumento "
                        "proporcional na produção total, sem interferir nos rendimentos decrescentes") + az("."),
        "poucas": ("No " + azb("curto prazo") + " há ao menos um fator fixo: não dá para aumentar <b>todos</b> "
                   "os fatores. A produção sobe só pelo fator variável, sujeita aos " + azb("rendimentos "
                   "marginais decrescentes") + "."),
        "destrinchando": [
            "O item descreve um experimento de " + azb("longo prazo") + " — variar todos os fatores na mesma "
            "proporção — e o situa no curto prazo, quando ao menos um insumo (em geral, o capital) está fixo.",
            "No curto prazo, q = f(K̄, L): mais produto exige mais trabalho sobre a mesma planta. Cada "
            "trabalhador adicional dispõe de menos capital, e, a partir de certo ponto, o " + azb("produto "
            "marginal") + " do trabalho cai — é a lei dos rendimentos decrescentes, que existe justamente "
            "<b>por causa</b> do fator fixo.",
            "Mesmo no longo prazo, o “aumento proporcional na produção” não é automático: depende dos "
            + azb("rendimentos de escala") + ", que podem ser crescentes, constantes ou decrescentes. O item "
            "pressupõe, sem dizer, rendimentos constantes.",
            vm("Regra-âncora: curto prazo → um fator varia, PMg decrescente; longo prazo → todos variam, "
               "rendimentos de escala."),
        ],
        "dissecando": (cz("[troca de conceito · anacronismo]") + " O item transplanta para o curto prazo a "
                       "definição de rendimentos de escala, que é de longo prazo. O fecho “sem interferir nos "
                       "rendimentos decrescentes” é a pista: no curto prazo, eles são inevitáveis."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a empresa pode aumentar proporcionalmente todos os seus fatores de "
            "produção.”</i> → CERTO",
            "<i>“No longo prazo, aumentar proporcionalmente todos os fatores leva sempre a aumento proporcional "
            "da produção.”</i> → ERRADO (modulador absoluto: depende dos rendimentos de escala)",
        ])],
        "reescrita": ("No curto prazo, a empresa pode aumentar sua produção " + hl("apenas aumentando os fatores "
                      "variáveis, pois ao menos um fator permanece fixo, o que a sujeita, a partir de certo "
                      "ponto, aos rendimentos marginais decrescentes") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "ANACRONISMO"], "moduladores": ["todos", "proporcionalmente"],
        "dificuldade": 1,
        "comentario_fonte": ("No curto prazo um fator é fixo; não se aumentam proporcionalmente todos os fatores, "
                             "e o fator variável enfrenta rendimentos decrescentes."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00037
    {
        "id": "ECO-E2-L00037-1", "fonte_ref": "E2-L00037", "destino": "05", "subtema": H2["pmg"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A lei dos rendimentos decrescentes, observada no curto prazo, implica que, adicionando mais "
                      "unidades de um fator variável enquanto outros são mantidos fixos, a produtividade marginal "
                      "desse fator diminui eventualmente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A lei dos rendimentos decrescentes, observada no curto prazo, implica que, adicionando mais "
                      "unidades de um fator variável <u>enquanto outros são mantidos fixos</u>, a produtividade "
                      "<u>marginal</u> desse fator diminui <u>eventualmente</u>."),
        "poucas": ("É o enunciado da " + azb("lei dos rendimentos marginais decrescentes") + ": com fatores "
                   "fixos, o " + azb("produto marginal") + " do fator variável cai <b>a partir de certo "
                   "ponto</b>."),
        "destrinchando": [
            "Três condições no enunciado, todas presentes no item: (1) um fator varia; (2) os demais ficam "
            "fixos (curto prazo); (3) é o produto <b>marginal</b> — o acréscimo de produção da última unidade — "
            "que cai.",
            "“Eventualmente” está no sentido técnico de “a partir de certo ponto”: o PMg pode <b>subir</b> no "
            "início (especialização, melhor uso da planta ociosa) e só depois cair. A lei não diz que cai desde "
            "a primeira unidade.",
            "Rendimento marginal decrescente não significa produto total caindo: enquanto PMg > 0, a produção "
            "total cresce, só que a taxas menores. O produto total só cai quando " + vd("PMg < 0") + ".",
            "A ideia é antiga: " + oc("David Ricardo") + " (1817) a usou na teoria da renda da terra — cultivar "
            "terras piores ou aplicar mais trabalho à mesma terra rende cada vez menos.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O item é a definição de manual. O risco está "
                       "no “eventualmente” (leia-se “a partir de certo ponto”) e em “marginal”: a banca costuma "
                       "trocar por “total” ou “desde a primeira unidade” para fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a produção total desse fator diminui à medida que ele é adicionado.”</i> → ERRADO (troca de "
            "conceito: cai o marginal, não o total)",
            "<i>“…a produtividade marginal desse fator diminui desde a primeira unidade adicionada.”</i> → "
            "ERRADO (o PMg pode crescer no início)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["eventualmente"], "dificuldade": 1,
        "comentario_fonte": ("Com fatores fixos, adicionar unidades de um fator variável reduz, após certo ponto, "
                             "sua produtividade marginal: cada unidade nova tem menos capital com que trabalhar."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00038
    {
        "id": "ECO-E2-L00038-1", "fonte_ref": "E2-L00038", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("As isoquantas, no longo prazo, representam combinações de fatores de produção que resultam "
                      "no mesmo nível de produção, permitindo ao produtor variar capital e trabalho na busca de "
                      "eficiência de custos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As isoquantas, no longo prazo, representam combinações de fatores de produção que resultam "
                      "no <u>mesmo nível de produção</u>, permitindo ao produtor variar capital e trabalho na "
                      "busca de eficiência de custos."),
        "poucas": ("Isoquanta = combinações de K e L com o " + azb("mesmo produto") + ". No longo prazo, com os "
                   "dois fatores livres, a firma escolhe, sobre ela, a combinação de " + azb("menor custo")
                   + "."),
        "destrinchando": [
            "O mapa de isoquantas descreve a tecnologia inteira: cada curva é um nível de produto; curvas mais "
            "afastadas da origem = mais produção; elas não se cruzam e, no caso usual, são convexas (TMST "
            "decrescente).",
            "No " + azb("longo prazo") + " "
            "todos os fatores variam, então a firma pode deslizar ao longo da isoquanta trocando capital por "
            "trabalho. No curto prazo, com K fixo, ela fica presa a uma linha horizontal desse mapa.",
            azb("Minimização de custos") + ": entre as combinações que produzem q, escolhe-se a que toca a "
            "isocusto mais baixa (C = wL + rK). No ótimo interior, " + vd("TMST = PMg<sub>L</sub>/PMg<sub>K</sub>"
            " = w/r") + " — o último real gasto em cada fator rende o mesmo produto.",
            "Ligando os pontos ótimos para níveis crescentes de q, obtém-se o " + azb("caminho de expansão")
            + ", base da curva de custo total de longo prazo.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Junta a definição de isoquanta com sua função no longo prazo; "
                       "nada a corrigir. A troca típica da banca é “mesmo custo” no lugar de “mesmo nível de "
                       "produção” — aí seria a isocusto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As isoquantas representam combinações de fatores que resultam no mesmo custo de "
            "produção.”</i> → ERRADO (troca de conceito: isso é a isocusto)",
            "<i>“No ponto de mínimo custo, a TMST iguala a razão entre os preços dos fatores.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No longo prazo todos os fatores variam; isoquantas mostram combinações de K e L com o "
                             "mesmo nível de produção e auxiliam a otimização de custos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00039
    {
        "id": "ECO-E2-L00039-1", "fonte_ref": "E2-L00039", "destino": "05", "subtema": H2["escala"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Os rendimentos de escala crescentes no longo prazo indicam que o aumento proporcional de "
                      "todos os fatores de produção leva a um aumento menos que proporcional na produção total."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os rendimentos de escala crescentes no longo prazo indicam que o aumento proporcional de "
                      "todos os fatores de produção leva a um aumento ") + vm("menos que proporcional")
                   + az(" na produção total."),
        "poucas": ("Rendimentos " + azb("crescentes") + " de escala: dobrar todos os insumos <b>mais que "
                   "dobra</b> o produto. “Menos que proporcional” define os " + azb("decrescentes") + "."),
        "destrinchando": [
            "Teste: multiplique todos os insumos por t > 1 e compare f(tK, tL) com t·f(K, L). "
            + vd("Maior") + " → crescentes; " + vd("igual") + " → constantes; " + vd("menor")
            + " → decrescentes.",
            "Na Cobb-Douglas q = A·K<sup>α</sup>L<sup>β</sup>, basta somar os expoentes: α + β > 1, = 1 ou < 1. "
            "Ex.: q = K<sup>0,6</sup>L<sup>0,6</sup> → dobrar K e L multiplica q por 2<sup>1,2</sup> ≈ "
            + vd("2,3") + ".",
            "Fontes de rendimentos crescentes: especialização e divisão do trabalho, indivisibilidades (uma "
            "linha de montagem só compensa em grande escala), relações geométricas (dobrar o diâmetro de um "
            "duto mais que dobra sua capacidade). Fontes de decrescentes: dificuldade de coordenar e "
            "gerenciar organizações muito grandes.",
            "Ponte com custos: com preços dos insumos constantes, rendimentos crescentes ↔ "
            + azb("economias de escala") + " (custo médio de longo prazo decrescente) — raiz dos monopólios "
            "naturais.",
        ],
        "dissecando": (cz("[inversão]") + " Troca a definição de crescentes pela de decrescentes, mantendo todo o "
                       "resto correto (“longo prazo”, “aumento proporcional de todos os fatores”). Pista: "
                       "“crescente” combina com “mais que proporcional”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os rendimentos de escala decrescentes indicam que o aumento proporcional de todos os fatores "
            "leva a um aumento menos que proporcional na produção.”</i> → CERTO",
            "<i>“Rendimentos de escala crescentes pressupõem que pelo menos um fator permaneça fixo.”</i> → "
            "ERRADO (escala é longo prazo: todos variam)",
        ])],
        "reescrita": ("Os rendimentos de escala crescentes no longo prazo indicam que o aumento proporcional de "
                      "todos os fatores de produção leva a um aumento " + hl("mais que proporcional")
                      + " na produção total."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Rendimentos crescentes: aumento proporcional dos insumos gera aumento mais que "
                             "proporcional do produto (economias de escala, automação, grandes operações)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00327
    {
        "id": "ECO-E2-L00327-1", "fonte_ref": "E2-L00327", "destino": "05", "subtema": H2["escala"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à teoria da produção.",
        "rotulo_item": "Item",
        "assertiva": ("Uma função de produção pode apresentar, simultaneamente, retornos crescentes de escala e "
                      "produtividades marginais decrescentes para cada fator de produção isoladamente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma função de produção <u>pode</u> apresentar, simultaneamente, retornos crescentes de "
                      "escala e produtividades marginais decrescentes para cada fator de produção "
                      "<u>isoladamente</u>."),
        "poucas": ("Escala e produtividade marginal medem experimentos diferentes (todos os fatores × um só). "
                   "Ex.: q = K<sup>0,75</sup>L<sup>0,75</sup> tem " + vd("retornos crescentes") + " e "
                   + vd("PMg decrescentes") + " ao mesmo tempo."),
        "destrinchando": [
            azb("Retornos de escala") + ": todos os insumos crescem na mesma proporção (longo prazo). "
            + azb("Produtividade marginal") + ": um insumo cresce, os demais ficam fixos (curto prazo). Como "
            "as perguntas são diferentes, as respostas são independentes.",
            "Na Cobb-Douglas q = K<sup>α</sup>L<sup>β</sup>: a escala depende da " + vd("soma α + β")
            + "; o PMg de cada fator é decrescente se o " + vd("expoente individual < 1") + " (PMg<sub>L</sub> "
            "= β·K<sup>α</sup>L<sup>β−1</sup> cai com L quando β < 1).",
            "Com α = β = 0,75: soma 1,5 > 1 → retornos crescentes; cada expoente < 1 → PMg decrescentes. "
            "Dobrar K e L multiplica q por 2<sup>1,5</sup> ≈ " + vd("2,8") + ", mas dobrar só L multiplica q "
            "por 2<sup>0,75</sup> ≈ " + vd("1,7") + ".",
            "Intuição: quando só o trabalho aumenta, cada trabalhador tem menos máquina; quando tudo aumenta "
            "junto, a proporção se mantém e entram os ganhos de especialização.",
            vm("Regra-âncora: PMg olha um fator; escala olha todos — um não determina o outro."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Parece contraditório “crescer com tudo” e "
                       "“decrescer com cada um”, mas não é. O “pode” e o “isoladamente” são a pista. 🔥 Tema "
                       "recorrente: a banca já cobrou as três combinações (crescentes, constantes e "
                       "decrescentes de escala com PMg decrescente)."),
        "modulos": [("📚 Autores e teses", [
            oc("Pindyck e Rubinfeld") + " (<i>Microeconomia</i>, capítulo de produção) apresentam os dois "
            "conceitos lado a lado justamente para separar o curto do longo prazo.",
        ]), ("😈 Para dificultar", [
            "<i>“Se a produtividade marginal de cada fator é decrescente, os retornos de escala são "
            "necessariamente decrescentes.”</i> → ERRADO (nexo indevido: a escala depende da soma dos "
            "expoentes)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode", "simultaneamente"],
        "dificuldade": 2,
        "comentario_fonte": ("Retornos de escala: todos os insumos variam; produtividade marginal: um só. Há "
                             "retornos crescentes com fatores cuja “produtividade marginal individual é menor "
                             "que 1” (critério impreciso: o que importa é o expoente de cada fator, não o valor do "
                             "PMg). Referência: Pindyck e Rubinfeld."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a fonte diz “produtividade marginal individual menor que 1”; o critério "
                    "correto é o expoente de cada fator menor que 1 (PMg decrescente)"],
    },
    # ------------------------------------------------------------------ E2-L00813
    {
        "id": "ECO-E2-L00813-1", "fonte_ref": "E2-L00813", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação à teoria microeconômica, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na função de produção do tipo Leontief, os fatores de produção são complementos perfeitos e "
                      "não podem ser substituídos um pelo outro, independentemente do preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na função de produção do tipo Leontief, os fatores de produção são complementos perfeitos e "
                      "não podem ser substituídos um pelo outro, <u>independentemente do preço</u>."),
        "poucas": ("Leontief = " + azb("proporções fixas") + ": q = mín(K/a, L/b). Isoquantas em L, "
                   + vd("elasticidade de substituição zero") + " — mudar preços relativos não muda a "
                   "combinação usada."),
        "destrinchando": [
            "Na " + azb("função de Leontief") + " cada unidade de produto exige a unidades de capital e b de "
            "trabalho. As proporções são fixas, mas não precisam ser 1 para 1: uma tecnologia pode exigir, por "
            "exemplo, 20 de capital para cada 10 de trabalho.",
            "Isoquantas em L com vértices sobre um raio a partir da origem. Fora do vértice, o insumo excedente "
            "tem produto marginal zero.",
            "“Independentemente do preço”: com isoquanta em L, a isocusto mais baixa sempre toca o vértice, "
            "qualquer que seja w/r. Se o trabalho encarece, a firma <b>não</b> o troca por capital — só passa a "
            "pagar mais pela mesma combinação. É isso que " + vd("σ = 0") + " significa.",
            "Contraponto: nos " + azb("substitutos perfeitos") + " (isoquantas retas paralelas), σ = ∞ e a firma "
            "troca totalmente de insumo quando os preços relativos cruzam a TMST.",
            "O nome homenageia " + oc("Wassily Leontief") + " (Nobel de 1973), cuja matriz insumo-produto usa "
            "coeficientes técnicos fixos.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. O trecho final (“independentemente do preço”) "
                       "parece exagero, mas é exatamente o que distingue a Leontief: nenhuma variação de preço "
                       "relativo induz substituição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na função de Leontief, os fatores devem ser usados sempre na proporção de um para um.”</i> → "
            "ERRADO (restrição indevida: a proporção é fixa, mas qualquer)",
            "<i>“Na função de Leontief, um aumento do salário leva a firma a substituir trabalho por capital ao "
            "longo da isoquanta.”</i> → ERRADO (σ = 0: não há substituição)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["independentemente"], "dificuldade": 1,
        "comentario_fonte": ("Leontief: isoquantas em L, proporções fixas (não necessariamente 1 para 1, ex.: 20 K e "
                             "10 L); não há substituição entre fatores, que ocorre com substitutos perfeitos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 123", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (isoquantas em L descritas no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00861
    {
        "id": "ECO-E2-L00861-1", "fonte_ref": "E2-L00861", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_NAB_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("A taxa marginal de substituição técnica em cada ponto da isoquanta corresponde à quantidade "
                      "de capital que pode ser substituída por determinada quantidade de trabalho com o objetivo "
                      "de aumentar a produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A taxa marginal de substituição técnica em cada ponto da isoquanta corresponde à quantidade "
                      "de capital que pode ser substituída por determinada quantidade de trabalho ")
                   + vm("com o objetivo de aumentar a produção") + az("."),
        "poucas": ("A " + azb("TMST") + " mede a troca entre insumos <b>mantendo a produção constante</b> — "
                   "toda a isoquanta tem o mesmo nível de produto. Aumentar a produção exige mudar de "
                   "isoquanta."),
        "destrinchando": [
            "TMST do trabalho pelo capital = quanto capital se pode retirar ao acrescentar uma unidade de "
            "trabalho, de modo que q fique igual: " + vd("TMST = −ΔK/ΔL (q constante)") + ".",
            "Ao longo da isoquanta, o ganho de produção do trabalho adicionado compensa exatamente a perda do "
            "capital retirado: PMg<sub>L</sub>·ΔL + PMg<sub>K</sub>·ΔK = 0, de onde " + vd("TMST = "
            "PMg<sub>L</sub>/PMg<sub>K</sub>") + ".",
            "Na isoquanta convexa, a TMST é " + azb("decrescente") + ": quanto mais trabalho e menos capital a "
            "firma usa, menos capital ela aceita ceder por trabalhador adicional (o trabalho fica relativamente "
            "abundante e menos produtivo na margem).",
            "É o análogo exato da " + azb("TMS") + " do consumidor, que troca bens mantendo a utilidade "
            "constante.",
            vm("Regra-âncora: “iso” = constante — sobre a isoquanta, o produto não muda."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A primeira parte é a definição correta; o "
                       "erro foi enxertado no objetivo da troca. 🔥 O mesmo item reaparece em outro simulado "
                       "Nabuco, com um gráfico de isoquantas retas — o gabarito não muda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…corresponde à quantidade de capital que pode ser substituída por determinada quantidade de "
            "trabalho, mantendo-se constante a produção.”</i> → CERTO",
            "<i>“A TMST é igual à razão entre os produtos médios do trabalho e do capital.”</i> → ERRADO "
            "(troca de conceito: razão entre produtos marginais)",
        ])],
        "reescrita": ("A taxa marginal de substituição técnica em cada ponto da isoquanta corresponde à quantidade "
                      "de capital que pode ser substituída por determinada quantidade de trabalho "
                      + hl("mantendo-se constante a produção") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("TMST do trabalho por capital: quanto se reduz de capital com uma unidade extra de "
                             "trabalho, mantendo a produção constante; análoga à TMS do consumidor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: assertiva idêntica à de ECO-E2-L01219-1 (outro bloco Nabuco, com figura); "
                    "mantidos os dois"],
    },
    # ------------------------------------------------------------------ E2-L00862
    {
        "id": "ECO-E2-L00862-1", "fonte_ref": "E2-L00862", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_NAB_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Considere que determinada firma tenha a função de produção de proporções fixas e que cada "
                      "nível de produção exija uma combinação específica de trabalho e capital. Nessa situação, a "
                      "taxa marginal de substituição técnica é constante em todos os pontos da isoquanta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere que determinada firma tenha a função de produção de proporções fixas e que cada "
                      "nível de produção exija uma combinação específica de trabalho e capital. Nessa situação, a "
                      "taxa marginal de substituição técnica ") + vm("é constante em todos os pontos")
                   + az(" da isoquanta."),
        "poucas": ("TMST constante em toda a isoquanta é marca dos " + azb("substitutos perfeitos")
                   + " (retas). Em " + azb("proporções fixas") + " a isoquanta é um L: TMST nula num braço, "
                   "infinita no outro e indefinida no vértice."),
        "destrinchando": [
            "Isoquanta de Leontief: trecho <b>horizontal</b> (sobra trabalho; mais L não substitui nenhum K → "
            + vd("TMST = 0") + "), trecho <b>vertical</b> (sobra capital; mais L permitiria liberar capital "
            "“infinito” → " + vd("TMST = ∞") + ") e o vértice, onde a TMST não é definida.",
            "Logo, a TMST muda de valor de um ponto a outro da isoquanta — não é constante. O que é fixo na "
            "Leontief é a <b>proporção</b> K/L no ponto eficiente, e não a taxa de troca.",
            "TMST constante (mesma inclinação em todos os pontos) só ocorre quando a isoquanta é uma "
            + azb("reta") + ": q = aK + bL, TMST = b/a.",
            "Quadro-resumo: retas → TMST constante, σ = ∞; L → sem substituição, σ = 0; convexas (Cobb-"
            "Douglas) → TMST decrescente, σ = 1.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item confunde “proporção fixa” com “taxa de "
                       "substituição constante”: fixa é a combinação; a TMST nem existe no vértice. Pista: "
                       "“constante em todos os pontos” descreve uma reta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na função de produção de proporções fixas, as isoquantas têm formato de L.”</i> → CERTO",
            "<i>“Se os insumos são substitutos perfeitos, a TMST é constante em todos os pontos da "
            "isoquanta.”</i> → CERTO",
        ])],
        "reescrita": ("Considere que determinada firma tenha a função de produção de proporções fixas e que cada "
                      "nível de produção exija uma combinação específica de trabalho e capital. Nessa situação, a "
                      "taxa marginal de substituição técnica " + hl("não é constante: é nula no trecho "
                      "horizontal, infinita no trecho vertical e indefinida no vértice") + " da isoquanta."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["todos"], "dificuldade": 2,
        "comentario_fonte": ("TMST constante em todos os pontos caracteriza substitutos perfeitos (isoquantas "
                             "retas paralelas); proporções fixas geram isoquantas em L."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 131", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (isoquantas em L descritas no 📖)"},
                          {"ref": "IMAGEM 132", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (isoquantas retas descritas no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00863
    {
        "id": "ECO-E2-L00863-1", "fonte_ref": "E2-L00863", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_NAB_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Supondo-se que, na produção de serviços de proteção ao meio ambiente, funcionários e "
                      "material de escritório sejam fatores complementares, então, as isoquantas entre esses dois "
                      "insumos são formadas por ângulos retos paralelos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Supondo-se que, na produção de serviços de proteção ao meio ambiente, funcionários e "
                      "material de escritório sejam fatores <u>complementares</u>, então, as isoquantas entre "
                      "esses dois insumos são formadas por <u>ângulos retos</u> paralelos."),
        "poucas": ("Fatores " + azb("complementares") + " (proporções fixas) → isoquantas em <b>L</b>, ou "
                   "seja, ângulos retos, um para cada nível de produção, com vértices alinhados."),
        "destrinchando": [
            "Na " + azb("função de proporções fixas") + " (Leontief), cada nível de produção exige uma "
            "combinação específica dos insumos. Produção adicional só vem com mais funcionários <b>e</b> mais "
            "material, na proporção da tecnologia.",
            "Acrescentar só um dos fatores não aumenta a produção: o excedente fica ocioso (produto marginal "
            "zero). Graficamente, a isoquanta forma um " + azb("ângulo reto") + ", com vértice na combinação "
            "eficiente.",
            "“Paralelos”: os Ls de níveis crescentes são cópias deslocadas umas das outras, com braços "
            "paralelos aos eixos e vértices sobre um mesmo raio que parte da origem — o " + azb("caminho de "
            "expansão") + ".",
            "Paralelo com o consumidor: bens complementares perfeitos (sapato esquerdo e direito) geram "
            + azb("curvas de indiferença") + " também em L.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " A redação estranha (“ângulos retos paralelos”) assusta, mas "
                       "descreve o mapa de Leontief. O contexto (serviços ambientais) é irrelevante: o que "
                       "decide é “complementares”. 🔥 A banca alterna o exemplo (funcionário e computador, "
                       "motorista e caminhão) e o formato (retas × L)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as isoquantas entre esses dois insumos são formadas por retas paralelas negativamente "
            "inclinadas.”</i> → ERRADO (troca de conceito: retas são substitutos perfeitos)",
            "<i>“…um funcionário adicional, sem material de escritório adicional, eleva a produção.”</i> → "
            "ERRADO (o PMg do fator isolado é zero)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Proporções fixas (Leontief): nenhuma substituição; mais produção só com mais dos dois "
                             "insumos; isoquantas em L, como as curvas de indiferença de complementares."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 133", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (isoquantas em L descritas no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00864
    {
        "id": "ECO-E2-L00864-1", "fonte_ref": "E2-L00864", "destino": "05", "subtema": H2["escala"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_NAB_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Se uma firma apresenta tecnologia de produção com rendimentos constantes de escala, então "
                      "ela não poderá apresentar produto marginal decrescente para cada fator."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se uma firma apresenta tecnologia de produção com rendimentos constantes de escala, então "
                      "ela ") + vm("não poderá") + az(" apresentar produto marginal decrescente para cada fator."),
        "poucas": ("Escala (todos os fatores) e produto marginal (um fator) são independentes. A Cobb-Douglas "
                   "q = K<sup>0,5</sup>L<sup>0,5</sup> tem " + vd("rendimentos constantes") + " e "
                   + vd("PMg decrescente") + " em cada fator."),
        "destrinchando": [
            azb("Produto marginal") + " = acréscimo de produção com uma unidade a mais de um insumo, "
            "<b>mantidos fixos</b> os demais. Ele cai porque o fator variável passa a dispor de menos do fator "
            "fixo — fenômeno tão difundido que virou “lei”.",
            azb("Rendimentos de escala") + " = efeito de aumentar <b>todos</b> os insumos na mesma proporção; "
            "nenhum fica fixo, e a produção pode crescer em proporção igual, maior ou menor.",
            "Exemplo: q = K<sup>0,5</sup>L<sup>0,5</sup>. Dobrar K e L dobra q (" + vd("α + β = 1") + "), "
            "mas, com K fixo, PMg<sub>L</sub> = 0,5·K<sup>0,5</sup>/L<sup>0,5</sup> cai à medida que L "
            "cresce. Esse é, aliás, o caso-padrão dos livros: constantes de escala com PMg decrescentes.",
            "Na Cobb-Douglas, PMg decrescente de cada fator exige expoente individual < 1; a escala depende da "
            "soma. Com α = β = 0,5, os dois critérios convivem.",
            vm("Regra-âncora: PMg decrescente é compatível com qualquer tipo de rendimento de escala."),
        ],
        "dissecando": (cz("[nexo indevido]") + " Cria uma incompatibilidade inexistente entre dois conceitos "
                       "de horizontes diferentes. O “não poderá” é a pista: basta um contraexemplo (Cobb-Douglas "
                       "com α + β = 1) para derrubar o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma função com rendimentos constantes de escala pode apresentar produto marginal decrescente "
            "para cada fator.”</i> → CERTO",
            "<i>“Rendimentos constantes de escala implicam produto marginal constante de cada fator.”</i> → "
            "ERRADO (confunde escala com rendimento marginal)",
        ])],
        "reescrita": ("Se uma firma apresenta tecnologia de produção com rendimentos constantes de escala, então ela "
                      + hl("pode") + " apresentar produto marginal decrescente para cada fator"
                      + hl(", como na Cobb-Douglas com α + β = 1") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["não poderá"], "dificuldade": 2,
        "comentario_fonte": ("Produto marginal decrescente decorre de manter os demais insumos fixos; rendimentos "
                             "de escala aumentam todos os insumos na mesma proporção e podem ser constantes, "
                             "crescentes ou decrescentes mesmo com PMg decrescente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01216
    {
        "id": "ECO-E2-L01216-1", "fonte_ref": "E2-L01216", "destino": "05", "subtema": H2["escala"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_ISO,
        "frente_figuras": ["ECO-E2-L01216-1-F1"],
        "rotulo_item": "Item",
        "assertiva": "A referida função de produção apresenta rendimentos constantes à escala.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A referida função de produção apresenta rendimentos <u>constantes</u> à escala."),
        "poucas": ("Isoquantas retas igualmente espaçadas ao longo de qualquer raio (Q1, Q2 = 2Q1, Q3 = 3Q1): "
                   "dobrar K e L leva da isoquanta Q1 à Q2, isto é, " + vd("dobra o produto") + " — "
                   + azb("rendimentos constantes de escala") + "."),
        "destrinchando": [
            "Rendimentos de escala se leem no mapa de isoquantas pelo <b>espaçamento</b> ao longo de um raio "
            "a partir da origem: se dobrar a distância à origem dobra o nível de produto, são constantes.",
            "Na figura, a isoquanta Q2 está ao dobro da distância de Q1, e Q3 ao triplo. Com níveis de produto "
            "na mesma progressão (por exemplo, 10, 20 e 30), multiplicar todos os insumos por t multiplica a "
            "produção por t: " + vd("f(tK, tL) = t·f(K, L)") + ".",
            "Forma funcional compatível: q = aK + bL (substitutos perfeitos), homogênea de grau 1. Se as "
            "isoquantas de níveis igualmente crescentes fossem ficando <b>mais próximas</b> entre si, os "
            "rendimentos seriam crescentes; se <b>mais distantes</b>, decrescentes.",
            "Cuidado: o formato da isoquanta (reta, L, convexa) informa sobre a <b>substituição</b> entre "
            "insumos; o espaçamento informa sobre a <b>escala</b>. São leituras independentes.",
        ],
        "dissecando": (cz("[detalhe]") + " O item exige ler o gráfico pelo espaçamento das isoquantas, não pelo "
                       "formato. 🔥 No mesmo bloco, a banca pergunta escala (CERTO), substituição (CERTO) e "
                       "rendimento marginal (ERRADO) sobre a mesma figura."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como as isoquantas são retas, a função apresenta necessariamente rendimentos crescentes de "
            "escala.”</i> → ERRADO (nexo indevido: o formato não define a escala)",
            "<i>“Se as isoquantas de níveis 10, 20 e 30 fossem cada vez mais próximas, haveria rendimentos "
            "crescentes de escala.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Um aumento dos insumos aumenta a produção na mesma proporção.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 209", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (ECO-E2-L01216-1-F1)"}],
        "alertas": ["figura_conjectural: ECO-E2-L01216-1-F1 redesenhada a partir da descrição (três isoquantas "
                    "retas negativamente inclinadas, K no eixo horizontal e L no vertical); a transcrição não "
                    "traz os níveis de produto, e o espaçamento uniforme foi deduzido do gabarito (rendimentos "
                    "constantes = CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L01217
    {
        "id": "ECO-E2-L01217-1", "fonte_ref": "E2-L01217", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_ISO,
        "frente_figuras": ["ECO-E2-L01216-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("As isoquantas apresentadas representam o capital e o trabalho como substitutos perfeitos na "
                      "produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As isoquantas apresentadas representam o capital e o trabalho como <u>substitutos "
                      "perfeitos</u> na produção."),
        "poucas": ("Isoquanta reta = " + azb("TMST constante") + ": capital e trabalho se trocam sempre à mesma "
                   "taxa, qualquer que seja a combinação — definição de " + azb("substitutos perfeitos") + "."),
        "destrinchando": [
            "A " + azb("TMST") + " é o módulo da inclinação da isoquanta. Numa reta, a inclinação é a mesma em "
            "todos os pontos: abrir mão de uma unidade de capital exige sempre a mesma quantidade adicional de "
            "trabalho, esteja a firma usando muito ou pouco de cada fator.",
            "Forma funcional: q = aK + bL, com TMST = a/b (na figura, com L no eixo vertical). Produtos "
            "marginais constantes: PMg<sub>K</sub> = a e PMg<sub>L</sub> = b.",
            "Implicações: " + vd("elasticidade de substituição infinita") + "; a firma pode produzir só com "
            "capital ou só com trabalho (intercepto em cada eixo); na minimização de custos, a regra é usar só "
            "o insumo cujo produto marginal por real gasto for maior — " + azb("solução de canto") + ".",
            "Contraste: isoquantas em L → complementares perfeitos (σ = 0); convexas → substituição imperfeita, "
            "com TMST decrescente.",
        ],
        "dissecando": (cz("[literalidade]") + " Leitura direta do formato: reta = substitutos perfeitos. A "
                       "banca costuma inverter para “complementares perfeitos” (ERRADO) ou cobrar a TMST "
                       "“decrescente” (ERRADO: é constante)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As isoquantas apresentadas indicam que capital e trabalho devem ser usados em proporções "
            "fixas.”</i> → ERRADO (troca de conceito: isso seria isoquanta em L)",
            "<i>“A taxa marginal de substituição técnica é a mesma em todos os pontos de cada isoquanta.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Isoquantas retas: TMST constante, a mesma qualquer que seja o nível de insumos; "
                             "capital e trabalho são substitutos perfeitos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 209", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (ECO-E2-L01216-1-F1)"}],
        "alertas": ["figura_conjectural: ECO-E2-L01216-1-F1 (mesma figura do item 1)"],
    },
    # ------------------------------------------------------------------ E2-L01218
    {
        "id": "ECO-E2-L01218-1", "fonte_ref": "E2-L01218", "destino": "05", "subtema": H2["pmg"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_ISO,
        "frente_figuras": ["ECO-E2-L01216-1-F1"],
        "rotulo_item": "Item",
        "assertiva": "A função de produção em questão respeita a lei dos rendimentos marginais decrescentes.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função de produção em questão ") + vm("respeita") + az(" a lei dos rendimentos "
                                                                                "marginais decrescentes."),
        "poucas": ("Isoquantas retas e igualmente espaçadas = " + azb("substitutos perfeitos") + " (Q = aK + "
                   "bL): o produto marginal de cada fator é <b>constante</b>, não decrescente."),
        "destrinchando": [
            "Isoquanta reta → " + azb("TMST constante") + ": troca-se K por L sempre à mesma taxa. Forma "
            "funcional típica: Q = aK + bL. Daí PMg<sub>K</sub> = a e PMg<sub>L</sub> = b, constantes.",
            "Fixe o capital (uma linha horizontal no gráfico, digamos K = 2) e aumente o trabalho: cada unidade "
            "extra de L acrescenta sempre b unidades de produto — " + azb("rendimentos marginais constantes")
            + ". A lei dos rendimentos decrescentes exigiria PMg caindo com o uso do fator.",
            "Espaçamento uniforme (Q2 = 2Q1, Q3 = 3Q1 a distâncias iguais da origem) indica "
            + azb("rendimentos constantes de escala") + ": dobrar K e L dobra Q.",
            "Não confundir: <b>rendimento marginal</b> = um fator varia, o outro fixo (curto prazo); "
            "<b>rendimento de escala</b> = todos os fatores na mesma proporção (longo prazo). Uma Cobb-Douglas "
            "com α + β = 1 tem rendimentos constantes de escala <i>e</i> marginais decrescentes.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item empresta uma “lei” geral da microeconomia e a "
                       "aplica a uma tecnologia que é justamente a exceção. Pista visual: retas. 🔥 A banca "
                       "pede no mesmo bloco escala (CERTO aqui) e rendimento marginal (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função apresenta rendimentos constantes de escala.”</i> → CERTO",
            "<i>“A taxa marginal de substituição técnica é decrescente ao longo de cada isoquanta.”</i> → "
            "ERRADO (é constante: isoquanta reta)",
        ])],
        "reescrita": ("A função de produção em questão " + hl("não") + " respeita a lei dos rendimentos "
                      "marginais decrescentes" + hl(": os produtos marginais de K e de L são constantes") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Rendimentos marginais constantes: fixado o capital (ex.: K = 2), cada unidade "
                             "adicional de trabalho gera acréscimo constante de produção."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 209", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (ECO-E2-L01216-1-F1)"},
                          {"ref": "IMAGEM 210", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (repetia a figura da frente)"}],
        "alertas": ["figura_conjectural: ECO-E2-L01216-1-F1 (mesma figura do item 1)"],
    },
    # ------------------------------------------------------------------ E2-L01219
    {
        "id": "ECO-E2-L01219-1", "fonte_ref": "E2-L01219", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_ISO,
        "frente_figuras": ["ECO-E2-L01216-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("A taxa marginal de substituição técnica em cada ponto da isoquanta corresponde à quantidade "
                      "de capital que pode ser substituída por determinada quantidade de trabalho com o objetivo "
                      "de aumentar a produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A taxa marginal de substituição técnica em cada ponto da isoquanta corresponde à quantidade "
                      "de capital que pode ser substituída por determinada quantidade de trabalho ")
                   + vm("com o objetivo de aumentar a produção") + az("."),
        "poucas": ("Sobre uma isoquanta (Q1, Q2 ou Q3) o produto é <b>constante</b>. A " + azb("TMST")
                   + " mede a troca entre K e L que mantém a produção; para aumentá-la, é preciso passar a uma "
                   "isoquanta mais alta."),
        "destrinchando": [
            "Definição: TMST = decréscimo máximo de um insumo quando se usa uma unidade adicional do outro, "
            + vd("mantido o produto constante") + ". Geometricamente, é o módulo da inclinação da isoquanta "
            "naquele ponto.",
            "Na figura, as isoquantas são retas: a TMST é a mesma em todos os pontos de cada uma. Deslizar "
            "sobre Q1 troca capital por trabalho sem alterar a produção; aumentá-la significa sair de Q1 para Q2 "
            "ou Q3 — usar mais insumos, não trocá-los.",
            "Relação com os produtos marginais: ao longo da isoquanta, PMg<sub>L</sub>·ΔL + PMg<sub>K</sub>·ΔK "
            "= 0, logo " + vd("TMST = PMg<sub>L</sub>/PMg<sub>K</sub>") + ". Com isoquantas retas, os dois "
            "PMg são constantes, e a razão também.",
            vm("Regra-âncora: movimento ao longo da isoquanta = mesma produção; mudança de isoquanta = outra "
               "produção."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A definição está certa até “trabalho”; o "
                       "erro é o objetivo enxertado no fim. 🔥 Assertiva idêntica aparece em outro bloco Nabuco "
                       "sobre teoria da firma — mesmo gabarito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nas isoquantas apresentadas, a taxa marginal de substituição técnica é a mesma em todos os "
            "pontos de cada isoquanta.”</i> → CERTO",
            "<i>“Passar da isoquanta Q1 para Q2 mantendo a mesma razão K/L aumenta a TMST.”</i> → ERRADO "
            "(isoquantas paralelas: a TMST não muda)",
        ])],
        "reescrita": ("A taxa marginal de substituição técnica em cada ponto da isoquanta corresponde à quantidade "
                      "de capital que pode ser substituída por determinada quantidade de trabalho "
                      + hl("mantendo-se constante a produção") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("TMST é a inclinação em cada ponto da isoquanta; ao longo dela o produto não muda; "
                             "substitui-se um insumo pelo outro para manter a produção constante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 209", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (ECO-E2-L01216-1-F1)"}],
        "alertas": ["figura_conjectural: ECO-E2-L01216-1-F1 (mesma figura do item 1)",
                    "quase_duplicata: assertiva idêntica à de ECO-E2-L00861-1 (outro bloco Nabuco, sem figura); "
                    "mantidos os dois"],
    },
    # ------------------------------------------------------------------ E2-L01220
    {
        "id": "ECO-E2-L01220-1", "fonte_ref": "E2-L01220", "destino": "05", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_CP,
        "rotulo_item": "Item",
        "assertiva": ("O curto prazo é um período de tempo no qual pelo menos um fator de produção é fixo. No longo "
                      "prazo a empresa pode alterar a quantidade de qualquer fator utilizado na produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O curto prazo é um período de tempo no qual <u>pelo menos um</u> fator de produção é fixo. "
                      "No longo prazo a empresa pode alterar a quantidade de <u>qualquer</u> fator utilizado na "
                      "produção."),
        "poucas": ("As duas definições estão corretas: " + azb("curto prazo") + " = ao menos um fator fixo; "
                   + azb("longo prazo") + " = tempo suficiente para que todos os fatores se tornem variáveis."),
        "destrinchando": [
            "O critério é a possibilidade de ajuste, não o calendário: longo prazo é o tempo necessário para "
            "que <b>todos</b> os insumos possam variar — construir outra fábrica, mudar a tecnologia, entrar ou "
            "sair do mercado.",
            "Reflexo nos custos: no curto prazo, CT = " + azb("CF") + " + " + azb("CV") + " (o fator fixo "
            "gera custo fixo, que existe mesmo com produção zero); no longo prazo, todo custo é variável, e a "
            "curva de custo médio de longo prazo é a “envoltória” das curvas de curto prazo.",
            "Reflexo na produção: o curto prazo é o domínio da " + azb("lei dos rendimentos marginais "
            "decrescentes") + "; o longo prazo, dos " + azb("rendimentos de escala") + ".",
            "Reflexo na concorrência perfeita: lucro econômico pode persistir no curto prazo; no longo prazo, a "
            "livre entrada e saída o leva a zero.",
        ],
        "dissecando": (cz("[literalidade]") + " Duas definições de manual encadeadas; os moduladores “pelo "
                       "menos um” e “qualquer” são os pontos que a banca costuma adulterar (“todos os fatores "
                       "fixos”, “apenas o capital varia”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a empresa pode alterar a quantidade de capital, mas a de trabalho permanece "
            "fixa.”</i> → ERRADO (restrição indevida: no longo prazo todos variam)",
            "<i>“No curto prazo, a firma pode ter custos fixos mesmo que nada produza.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["pelo menos um", "qualquer"], "dificuldade": 1,
        "comentario_fonte": ("Curto prazo: um ou mais fatores não podem ser modificados. Longo prazo: tempo "
                             "necessário para que todos os insumos se tornem variáveis."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01221
    {
        "id": "ECO-E2-L01221-1", "fonte_ref": "E2-L01221", "destino": "05", "subtema": H2["pmg"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_CP,
        "rotulo_item": "Item",
        "assertiva": ("Em uma firma que opera com capital constante no curto prazo, aumento na quantidade de "
                      "trabalho faz que o produto marginal e o produto médio do trabalho cresçam e depois tendam a "
                      "cair. Nesse processo, enquanto o produto médio cresce, o produto marginal é maior que o "
                      "médio; e, enquanto o produto médio diminui, o produto marginal é menor que o produto "
                      "médio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma firma que opera com capital constante no curto prazo, aumento na quantidade de "
                      "trabalho faz que o produto marginal e o produto médio do trabalho cresçam e depois tendam a "
                      "cair. Nesse processo, enquanto o produto médio cresce, o produto marginal é <u>maior</u> "
                      "que o médio; e, enquanto o produto médio diminui, o produto marginal é <u>menor</u> que o "
                      "produto médio."),
        "poucas": ("É a relação " + azb("marginal × média") + ": se a unidade nova rende mais que a média, puxa "
                   "a média para cima; se rende menos, puxa para baixo. Por isso o " + azb("PMg corta o PMe no "
                   "máximo do PMe") + "."),
        "destrinchando": [
            "Definições, com K fixo: " + azb("produto médio") + " PMe = q/L; " + azb("produto marginal")
            + " PMg = Δq/ΔL. Ambos costumam subir no início (especialização, uso da planta ociosa) e cair "
            "depois (rendimentos decrescentes).",
            "A relação é aritmética, como a média de notas: tirar uma nota acima da média sobe a média; abaixo, "
            "derruba. Formalmente, " + vd("dPMe/dL = (PMg − PMe)/L") + ": o PMe cresce quando PMg > PMe, cai "
            "quando PMg < PMe e é máximo quando " + vd("PMg = PMe") + ".",
            "Exemplo: q = 6L² − 0,5L³ → PMe = 6L − 0,5L² e PMg = 12L − 1,5L². O PMg é máximo em L = 4; o PMe é "
            "máximo em " + vd("L = 6") + ", onde PMg = PMe = " + vd("18") + "; o produto total é máximo onde "
            "PMg = 0 (L = 8).",
            "Os três estágios da produção: I (até o máximo do PMe), II (do máximo do PMe até PMg = 0) e III "
            "(PMg < 0). A firma racional opera no estágio II.",
            "A mesma lógica vale nos custos, espelhada: o " + azb("CMg corta o CMe no mínimo do CMe") + ".",
        ],
        "grafico_verso": "ECO-E2-L01221-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz o resultado de manual. O risco está na "
                       "ordem das comparações: a banca inverte “maior” e “menor” ou afirma que o PMg corta o PMe "
                       "no máximo do <b>PMg</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O produto marginal intercepta o produto médio no ponto de máximo do produto marginal.”</i> → "
            "ERRADO (troca: é no máximo do PMe)",
            "<i>“Enquanto o produto marginal for positivo, o produto total cresce, ainda que o produto médio "
            "esteja caindo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["tendam a"], "dificuldade": 2,
        "comentario_fonte": ("Verso só com o gráfico de produção total (máximo de 112 com 8 trabalhadores) e de "
                             "produto médio e marginal."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 211", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01221-1-V1, didática, com função própria)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01222
    {
        "id": "ECO-E2-L01222-1", "fonte_ref": "E2-L01222", "destino": "05", "subtema": H2["pmg"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_CP,
        "rotulo_item": "Item",
        "assertiva": ("A lei dos retornos marginais decrescentes afirma que o produto total cai à medida que mais do "
                      "insumo é adicionado à produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A lei dos retornos marginais decrescentes afirma que o ") + vm("produto total")
                   + az(" cai à medida que mais do insumo é adicionado à produção."),
        "poucas": ("O que decresce é o " + azb("produto marginal") + " (o acréscimo de produção de cada nova "
                   "unidade), não o produto total, que continua subindo enquanto PMg > 0."),
        "destrinchando": [
            "Enunciado correto: aumentando-se o uso de um insumo, com os demais fixos, a " + azb("produção "
            "adicional") + " obtida a cada unidade acaba diminuindo.",
            "Exemplo: com uma máquina fixa, o 1º operário acrescenta 10 unidades; o 2º, 8; o 3º, 5. O produto "
            "total vai de 10 a " + vd("18") + " e a " + vd("23") + " — sobe, só que cada vez menos. O PMg "
            "caiu; o total, não.",
            "O produto total só cai quando o PMg fica " + vd("negativo") + " (operários demais atrapalhando-se "
            "na mesma planta) — o estágio III da produção, que nenhuma firma racional escolhe.",
            "Graficamente: rendimentos decrescentes = a curva de produto total fica <b>côncava</b> (inclinação "
            "diminuindo), não descendente.",
            vm("Regra-âncora: rendimento decrescente = o marginal cai; total cai só com PMg < 0."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca marginal por total — o mesmo erro de quem confunde "
                       "“crescer menos” com “diminuir”. Pista: a palavra “marginais” está no nome da lei."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela lei dos rendimentos decrescentes, o produto total cresce a taxas decrescentes a partir "
            "de certo ponto.”</i> → CERTO",
            "<i>“A lei dos rendimentos decrescentes aplica-se ao longo prazo, quando todos os insumos "
            "variam.”</i> → ERRADO (anacronismo: pressupõe fator fixo, curto prazo)",
        ])],
        "reescrita": ("A lei dos retornos marginais decrescentes afirma que o " + hl("produto marginal")
                      + " cai à medida que mais do insumo é adicionado à produção."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O produto adicional é que decresce, não necessariamente a produção; com outros "
                             "insumos constantes, a produção adicional diminui."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01223
    {
        "id": "ECO-E2-L01223-1", "fonte_ref": "E2-L01223", "destino": "05", "subtema": H2["escala"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_CP,
        "rotulo_item": "Item",
        "assertiva": ("Em um processo produtivo, se existir produto marginal decrescente em relação a um insumo, "
                      "então os retornos de escala serão decrescentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um processo produtivo, se existir produto marginal decrescente em relação a um insumo, ")
                   + vm("então os retornos de escala serão decrescentes") + az("."),
        "poucas": ("PMg decrescente (um insumo varia) não determina " + azb("retornos de escala")
                   + " (todos variam): eles podem ser crescentes, constantes ou decrescentes."),
        "destrinchando": [
            azb("Produto marginal") + ": produção adicional com uma unidade a mais de um insumo, mantidos fixos "
            "os demais. Cai porque o insumo variável dispõe de cada vez menos dos fixos.",
            azb("Retornos de escala") + ": todos os insumos crescem na mesma proporção, nenhum fica fixo — a "
            "causa da queda do PMg desaparece. O resultado depende da tecnologia.",
            "Contraexemplos na Cobb-Douglas q = K<sup>α</sup>L<sup>β</sup>, todos com PMg decrescentes (α, β "
            "< 1): " + vd("0,7 + 0,7 = 1,4") + " → crescentes; " + vd("0,5 + 0,5 = 1") + " → constantes; "
            + vd("0,3 + 0,3 = 0,6") + " → decrescentes.",
            vm("Regra-âncora: do PMg não se deduz a escala; da escala não se deduz o PMg."),
        ],
        "dissecando": (cz("[nexo indevido]") + " Liga dois conceitos de horizontes diferentes por um “então” que "
                       "não existe. 🔥 Família de itens recorrente: “rendimentos constantes ⇒ PMg constante”, "
                       "“PMg decrescente ⇒ escala decrescente” — todos ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma função com produto marginal decrescente em cada insumo pode apresentar retornos crescentes "
            "de escala.”</i> → CERTO",
        ])],
        "reescrita": ("Em um processo produtivo, se existir produto marginal decrescente em relação a um insumo, "
                      + hl("nada se pode concluir sobre os retornos de escala, que podem ser crescentes, "
                           "constantes ou decrescentes") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["então"], "dificuldade": 2,
        "comentario_fonte": ("PMg decresce porque os demais insumos ficam fixos; nos rendimentos de escala todos "
                             "variam, e a produção pode crescer em proporção igual, maior ou menor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
