"""Cards do lote de redação 14 — ECO, passada 03 (nota 73: teorias clássicas e neoclássicas do comércio)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "vant": "⛵ Vantagens absolutas e comparativas",
    "ho": "🧪 Heckscher-Ohlin e teoremas",
    "leo": "❓ Paradoxo de Leontief e termos de troca",
}

CMD_TEORIAS = "Julgue o item a seguir, relativo às teorias do comércio internacional."

CMD_BOZAN_04 = "Sobre as teorias clássicas e neoclássicas de comércio, julgue o item a seguir."

CMD_BOZAN_01 = ("Considere os postulados das teorias clássicas do comércio internacional e julgue a assertiva a "
                "seguir.")

CMD_NAB_TAB = ("Considere os coeficientes técnicos de produção de dois países, em horas de trabalho por unidade "
               "produzida, e suponha custos de transporte nulos. Com base na teoria das vantagens absolutas (Adam "
               "Smith) e comparativas (David Ricardo), julgue o item.")

CMD_NAB_2 = "A respeito das teorias do comércio, julgue o item subsequente."

CMD_NAB_1 = "Em relação às teorias do comércio, julgue o item a seguir."

TAB_086 = {
    "titulo": "Coeficientes técnicos de produção (horas de trabalho por unidade produzida)",
    "cabecalho": ["Produto", "Brasil", "México"],
    "linhas": [["Calçados", "1/7", "1"], ["Vestuário", "1/3", "1/2"]],
    "fonte": "Nabuco, 2026.",
}

FIG_086 = [{"ref": "IMAGEM 086", "tipo_fonte": "TABELA", "lado": "frente",
            "acao": "transcrita_html (tabela aninhada, 3 colunas)"}]

CARDS = [
    # ------------------------------------------------------------------ E1-0915
    {
        "id": "ECO-E1-0915-1", "fonte_ref": "E1-0915", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("A Fronteira de Possibilidade de produção no modelo de fatores específicos é representada por "
                      "uma linha reta, uma vez que a produtividade marginal do trabalho é decrescente e constante."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Fronteira de Possibilidade de produção no modelo de fatores específicos é representada "
                       "por ") + vm("uma linha reta") + az(", uma vez que a produtividade marginal do trabalho é "
                                                          "decrescente") + vm(" e constante") + az(".")),
        "poucas": ("No modelo de " + azb("fatores específicos") + ", a produtividade marginal do trabalho é "
                   + vd("decrescente") + " em cada setor; por isso o custo de oportunidade cresce e a FPP é "
                   + azb("côncava") + ". FPP reta é a do modelo ricardiano. E “decrescente e constante” se "
                   "contradiz."),
        "destrinchando": [
            "O " + azb("modelo de fatores específicos") + " (" + oc("Viner") + ", " + oc("Samuelson")
            + ", " + oc("Jones") + "; a versão de manual é a de " + oc("Krugman e Obstfeld") + ") tem dois "
            "setores. Cada um usa um fator próprio, imóvel (capital num setor, terra no outro), e ambos usam o "
            + azb("trabalho") + ", que se move livremente entre eles.",
            "Como o fator específico de cada setor é fixo, cada trabalhador adicional rende menos que o anterior: "
            + vd("PMgL decrescente") + ". Ao tirar trabalho do setor Y para pôr no X, ganha-se cada vez menos X "
            "e perde-se cada vez mais Y. O " + azb("custo de oportunidade crescente") + " dá à FPP o formato "
            "côncavo (curvada para fora).",
            "No " + azb("modelo ricardiano") + ", ao contrário, há um único fator (trabalho) com produtividade "
            + vd("constante") + ": cada hora rende sempre o mesmo. O custo de oportunidade é constante e a FPP é "
            "uma reta.",
            "A justificativa do item é incoerente em si: uma grandeza não pode ser ao mesmo tempo decrescente e "
            "constante. Uma justifica a curva, a outra a reta.",
            vm("Regra-âncora: PMg constante → custo de oportunidade constante → FPP reta (Ricardo); PMg "
               "decrescente → custo crescente → FPP côncava (fatores específicos, H-O)."),
        ],
        "grafico_verso": "ECO-E1-0915-1-V1",
        "dissecando": (cz("[troca de conceito · contradição]") + " O item cola na FPP de fatores específicos o "
                       "formato da FPP ricardiana e tenta justificá-lo com duas propriedades incompatíveis. Pista: "
                       "“decrescente” já basta para afastar a reta. 🔥 A banca costuma cobrar o formato da FPP "
                       "como marca de cada modelo de comércio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, a FPP é linear porque a produtividade do trabalho é constante.”</i> → CERTO",
            "<i>“No modelo de fatores específicos, a FPP é côncava porque o trabalho é imóvel entre setores.”</i> "
            "→ ERRADO (o trabalho é o fator móvel; imóveis são os específicos)",
        ])],
        "reescrita": ("A Fronteira de Possibilidade de produção no modelo de fatores específicos é representada por "
                      + hl("uma curva côncava") + ", uma vez que a produtividade marginal do trabalho é "
                      "decrescente<s> e constante</s>."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("FPP no modelo de fatores específicos é côncava, não reta: a PMg do trabalho é "
                             "decrescente, não constante; aumentar um bem exige sacrificar cada vez mais do outro."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0916
    {
        "id": "ECO-E1-0916-1", "fonte_ref": "E1-0916", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de Hecksher-Ohlin, uma economia tende a se especializar na produção do "
                      "bem cuja função de produção seja intensiva no fator de produção escasso no país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o modelo de Hecksher-Ohlin, uma economia tende a se especializar na produção "
                       "do bem cuja função de produção seja intensiva no fator de produção ") + vm("escasso")
                    + az(" no país.")),
        "poucas": ("O " + azb("teorema de Heckscher-Ohlin") + " diz o contrário: o país exporta (e se especializa "
                   "relativamente) no bem intensivo no fator " + vd("relativamente abundante") + ", que é o fator "
                   "relativamente barato antes do comércio."),
        "destrinchando": [
            "Lógica do H-O em três passos: (1) países diferem na " + azb("dotação relativa de fatores") + " (K/L); "
            "(2) bens diferem na " + azb("intensidade fatorial") + "; (3) em autarquia, o fator abundante é "
            "relativamente barato, de modo que o bem que o usa intensivamente sai relativamente barato. Aí está a "
            "vantagem comparativa.",
            "Com a abertura, o país exporta o bem intensivo no fator abundante e importa o intensivo no fator "
            "escasso. Exemplo de manual: país com muita mão de obra e pouca terra exporta têxteis e calçados e "
            "importa alimentos e matérias-primas.",
            "Abundância é sempre <b>relativa</b>: compara-se K/L de um país com o K/L do outro, não estoques "
            "absolutos. Um país pode ter mais trabalhadores que outro e, ainda assim, ser relativamente abundante "
            "em capital.",
            "No modelo com FPP côncava, a especialização costuma ser <b>incompleta</b>: o país expande o setor "
            "intensivo no fator abundante sem abandonar o outro (diferente do Ricardo, em que ela tende a ser "
            "completa).",
            vm("Regra-âncora: H-O → exporta o bem intensivo no fator abundante; importa o intensivo no fator "
               "escasso."),
        ],
        "dissecando": (cz("[inversão]") + " Troca de uma palavra só: “escasso” no lugar de “abundante”. Tudo o mais "
                       "reproduz o teorema, o que induz à leitura apressada. 🔥 É a inversão mais cobrada do "
                       "tema, ao lado de trocar “abundante” por “produtivo” (que é Ricardo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tende a importar o bem intensivo no fator de produção escasso no país.”</i> → CERTO",
            "<i>“…tende a se especializar no bem em que sua mão de obra é relativamente mais produtiva.”</i> → "
            "ERRADO (troca de modelo: isso é Ricardo)",
        ])],
        "reescrita": ("De acordo com o modelo de Hecksher-Ohlin, uma economia tende a se especializar na produção do "
                      "bem cuja função de produção seja intensiva no fator de produção " + hl("abundante")
                      + " no país."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("H-O: especialização no bem intensivo no fator abundante; exporta o que usa o fator "
                             "abundante e barato e importa o que usa o escasso."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0917
    {
        "id": "ECO-E1-0917-1", "fonte_ref": "E1-0917", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": True,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("Para qualquer alteração nos preços relativos de dois bens, haverá mudança na composição da "
                      "produção doméstica entre tais bens."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Para <u>qualquer</u> alteração nos preços relativos de dois bens, haverá mudança na "
                      "composição da produção doméstica entre tais bens."),
        "poucas": ("Com " + azb("FPP côncava") + " (modelos neoclássicos), a economia produz onde a reta de preços "
                   "relativos tangencia a fronteira. Qualquer mudança na inclinação dessa reta move o ponto de "
                   "tangência e altera o " + vd("mix de produção") + "."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá CERTO, e o item vale no arcabouço neoclássico (FPP côncava e lisa, produção "
                          "diversificada). Mas o “qualquer” não resiste a dois casos de manual: na FPP " + vm("reta")
                          + " de Ricardo, uma variação de preços que não cruze o custo de oportunidade interno "
                          "mantém o país no mesmo ponto (especializado ou não); e uma economia já completamente "
                          "especializada num canto da FPP côncava não reage a pequenas variações. Sem o modelo "
                          "explicitado, ERRADO seria igualmente defensável.")],
        "destrinchando": [
            "Na FPP côncava, a inclinação da fronteira em cada ponto é o " + azb("custo de oportunidade")
            + " (taxa marginal de transformação). A firma competitiva maximiza o valor da produção "
            "p<sub>X</sub>X + p<sub>Y</sub>Y, o que leva ao ponto em que " + vd("TMT = p<sub>X</sub>/p<sub>Y</sub>")
            + ".",
            "Se p<sub>X</sub>/p<sub>Y</sub> sobe, a reta de preços fica mais inclinada e a tangência desliza "
            "pela fronteira: produz-se mais X e menos Y. Como a curvatura é contínua, por menor que seja a "
            "variação de preço, o ponto ótimo muda. É o que sustenta o “qualquer” do item.",
            "Contraste com " + oc("Ricardo") + ": na FPP reta o custo de oportunidade é constante. Se o preço "
            "relativo fica acima dele, o país produz só X; abaixo, só Y; e, enquanto não cruzar esse limiar, "
            "variações de preço não mudam nada na produção. O item seria falso nesse modelo.",
            "Esse mecanismo é o que faz a abertura comercial realocar a produção: o preço mundial difere do "
            "preço de autarquia e a economia se move na direção do bem que ficou relativamente mais caro.",
        ],
        "grafico_verso": "ECO-E1-0917-1-V1",
        "dissecando": (cz("[contraintuitivo · detalhe]") + " O “qualquer” soa como modulador absoluto e convida "
                       "a marcar ERRADO. No modelo de FPP côncava, porém, ele é literal: a tangência reage a toda "
                       "variação de preços. A pista é o modelo implícito (FPP côncava, produção diversificada); "
                       "fora dele, o absoluto é o ponto fraco do item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, qualquer alteração nos preços relativos muda a composição da produção.”</i> "
            "→ ERRADO (FPP reta: só muda se o preço cruzar o custo de oportunidade interno)",
            "<i>“Com FPP côncava, a alta do preço relativo de X leva a economia a produzir mais X e menos Y.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["qualquer"], "dificuldade": 3,
        "comentario_fonte": ("Mudança de preços relativos altera o custo de oportunidade e incentiva o país a "
                             "produzir mais do bem que encareceu e menos do outro; logo, muda a composição da "
                             "produção."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: o “qualquer” só vale com FPP côncava e produção diversificada; na FPP reta "
                    "ricardiana ou com especialização completa, variações de preço podem não alterar a produção",
                    "qualidade_fonte: o comentário de origem diz que a alta do preço de A reduz o custo de "
                    "oportunidade de produzir A; o custo de oportunidade é dado pela FPP, o que muda é o incentivo "
                    "(preço relativo × custo) — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0919
    {
        "id": "ECO-E1-0919-1", "fonte_ref": "E1-0919", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado jul/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria Heckscher-Ohlin, os países com uma abundância relativa de capital "
                      "tendem a se especializar na produção de bens intensivos em trabalho, enquanto os países com "
                      "uma abundância relativa de trabalho tendem a se especializar na produção de bens intensivos "
                      "em capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a teoria Heckscher-Ohlin, os países com uma abundância relativa de capital "
                       "tendem a se especializar na produção de bens intensivos em ") + vm("trabalho")
                    + az(", enquanto os países com uma abundância relativa de trabalho tendem a se especializar na "
                         "produção de bens intensivos em ") + vm("capital") + az(".")),
        "poucas": ("Inversão dupla: no " + azb("H-O") + ", o país abundante em " + vd("capital") + " exporta bens "
                   + vd("intensivos em capital") + ", e o abundante em trabalho exporta bens intensivos em "
                   "trabalho."),
        "destrinchando": [
            "O fator relativamente abundante é o relativamente barato em autarquia. O bem que usa esse fator "
            "com intensidade sai relativamente barato e vira a " + azb("vantagem comparativa") + " do país. É "
            "o " + azb("teorema de Heckscher-Ohlin") + " (" + oc("Heckscher") + ", 1919; " + oc("Ohlin")
            + ", 1933).",
            "Exemplo típico: EUA e Alemanha (K/L alto) exportam máquinas e aviões; Bangladesh e Vietnã (L/K "
            "alto) exportam vestuário e calçados.",
            "Ressalva empírica: " + oc("Leontief") + " (1953) encontrou nos EUA o padrão que o item descreve: "
            "exportações relativamente intensivas em trabalho. Foi o " + azb("paradoxo de Leontief") + ", "
            "justamente por contrariar o teorema. Não é o que a teoria prevê.",
            "Desdobramentos do mesmo arcabouço: " + azb("Stolper-Samuelson") + " (o comércio eleva a remuneração "
            "do fator abundante), " + azb("equalização dos preços dos fatores") + " e " + azb("Rybczynski")
            + " (mais dotação de um fator expande o setor que o usa intensivamente).",
            vm("Regra-âncora: fator abundante → bem intensivo nele → exportação."),
        ],
        "dissecando": (cz("[inversão]") + " As duas metades foram trocadas em espelho, o que mantém a frase "
                       "simétrica e “bem construída”. Pista: o par abundância × intensidade tem de ser o mesmo "
                       "fator dos dois lados (capital-capital, trabalho-trabalho)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os países com abundância relativa de capital tendem a importar bens intensivos em trabalho.”</i> "
            "→ CERTO",
            "<i>“O fato de os EUA exportarem bens intensivos em trabalho confirma o teorema de Heckscher-Ohlin.”"
            "</i> → ERRADO (contrariou o teorema: é o paradoxo de Leontief)",
        ])],
        "reescrita": ("De acordo com a teoria Heckscher-Ohlin, os países com uma abundância relativa de capital "
                      "tendem a se especializar na produção de bens intensivos em " + hl("capital") + ", enquanto "
                      "os países com uma abundância relativa de trabalho tendem a se especializar na produção de "
                      "bens intensivos em " + hl("trabalho") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tendem a"], "dificuldade": 1,
        "comentario_fonte": ("Houve inversão: o país abundante em capital se especializa em bens intensivos em "
                             "capital; o abundante em trabalho, em bens intensivos em trabalho."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0923
    {
        "id": "ECO-E1-0923-1", "fonte_ref": "E1-0923", "destino": "73", "subtema": H2["leo"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado jul/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("O Paradoxo de Leontief recebeu esse nome porque Wassily Leontief, o economista que o "
                      "enunciou, percebeu que a economia americana era exportadora de bens intensivos em mão de "
                      "obra, mesmo sendo um país abundante em capital, fato que contradizia o teorema de "
                      "Hecksher-Ohlin."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Paradoxo de Leontief recebeu esse nome porque Wassily Leontief, o economista que o "
                      "enunciou, percebeu que a economia americana era exportadora de bens <u>intensivos em mão de "
                      "obra</u>, mesmo sendo um país <u>abundante em capital</u>, fato que contradizia o teorema de "
                      "Hecksher-Ohlin."),
        "poucas": ("" + oc("Leontief") + " (" + vd("1953") + "), com a matriz insumo-produto dos EUA de "
                   + vd("1947") + ", achou exportações americanas relativamente " + azb("intensivas em trabalho")
                   + " e importações intensivas em capital: o contrário do que o H-O previa para o país mais "
                   "capitalizado do mundo."),
        "destrinchando": [
            "Método: em vez de olhar as importações em si, " + oc("Leontief") + " calculou quanto capital e "
            "trabalho seriam necessários para produzir nos EUA US$ 1 milhão de exportações e US$ 1 milhão de "
            "substitutos de importação. A razão K/L dos substitutos de importação saiu cerca de "
            + vd("30% maior") + " que a das exportações.",
            "Explicações propostas, que alimentaram novas teorias: (1) o próprio Leontief: o trabalhador "
            "americano seria muito mais produtivo, de modo que os EUA seriam abundantes em trabalho "
            "<b>efetivo</b>; (2) " + azb("capital humano") + " (" + oc("Kenen") + ", " + oc("Keesing")
            + "): as exportações eram intensivas em trabalho qualificado; (3) recursos naturais complementares "
            "ao capital nas importações (petróleo, minérios); (4) " + azb("reversão de intensidade fatorial")
            + "; (5) preferências viesadas para bens intensivos em capital; (6) estrutura tarifária protegendo "
            "setores intensivos em trabalho.",
            "O paradoxo abriu caminho para modelos com mais fatores (H-O-Vanek) e para explicações fora do H-O: "
            "ciclo do produto (" + oc("Vernon") + "), hiato tecnológico (" + oc("Posner") + ") e as novas "
            "teorias do comércio (" + oc("Krugman") + ").",
            vm("Regra-âncora: paradoxo de Leontief = EUA abundantes em capital exportando bens intensivos em "
               "trabalho; contradiz o teorema H-O, não o refuta de vez."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, com os três elementos na ordem certa (país "
                       "abundante em capital, exportação intensiva em trabalho, contradição com H-O). A banca "
                       "costuma errar o item trocando as intensidades ou dizendo que o paradoxo “confirmou” "
                       "o teorema."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Leontief constatou que os EUA exportavam bens intensivos em capital, confirmando o teorema H-O.”"
            "</i> → ERRADO (inversão: exportavam bens intensivos em trabalho)",
            "<i>“Uma das explicações do paradoxo é a maior qualificação da mão de obra americana, que tornaria o "
            "país abundante em capital humano.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso apenas repete a assertiva com o gabarito CERTO.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: razão K/L dos substitutos de importação cerca de 30% maior que a das "
                    "exportações (Leontief, 1953)"],
    },
    # ------------------------------------------------------------------ E1-0924
    {
        "id": "ECO-E1-0924-1", "fonte_ref": "E1-0924", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado jul/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("Suponha que a produção de soja no Brasil seja intensiva em mão de obra e que o país imponha "
                      "uma barreira tarifária sobre a soja americana, segundo o Teorema Stolper-Samuelson, a renda "
                      "do fator trabalho no Brasil se reduz."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Suponha que a produção de soja no Brasil seja intensiva em mão de obra e que o país imponha "
                       "uma barreira tarifária sobre a soja americana, segundo o Teorema Stolper-Samuelson, a renda "
                       "do fator trabalho no Brasil ") + vm("se reduz") + az(".")),
        "poucas": ("A tarifa eleva o preço interno da soja; pelo " + azb("teorema de Stolper-Samuelson")
                   + ", sobe a remuneração real do fator usado intensivamente nela (" + vd("trabalho")
                   + ") e cai a do outro fator."),
        "destrinchando": [
            "Cadeia: tarifa sobre a soja importada → " + vd("preço doméstico da soja ↑") + " → o setor de soja "
            "se expande e demanda relativamente mais do fator que usa com intensidade → " + vd("salário real ↑")
            + "; o fator usado intensivamente no outro setor tem a remuneração real reduzida.",
            azb("Stolper-Samuelson") + " (" + oc("Stolper e Samuelson") + ", 1941): a alta do preço relativo de "
            "um bem eleva, mais que proporcionalmente, a remuneração real do fator intensivo nele (" + azb("efeito "
            "ampliação") + ", de " + oc("Jones") + ") e reduz a do outro. O fator ganha em termos de <b>ambos</b> os "
            "bens.",
            "Aplicação clássica: a proteção beneficia o " + azb("fator escasso") + " de um país, cujos bens "
            "competem com importações; o livre-comércio beneficia o fator abundante. Daí a economia política do "
            "protecionismo (o fator escasso faz lobby por tarifas).",
            "A hipótese do item é didática: na realidade, a soja brasileira é intensiva em terra e capital, e o "
            + rx("Brasil") + " é exportador líquido do grão. Mas a questão manda supor a intensidade em trabalho, "
            "e o julgamento é pela lógica do teorema.",
            vm("Regra-âncora: ↑ preço do bem → ↑ remuneração real do fator intensivo nele e ↓ a do outro."),
        ],
        "dissecando": (cz("[inversão]") + " O item descreve o cenário correto e inverte só o efeito final. Pista: "
                       "a tarifa protege o setor intensivo em trabalho, e quem ganha com a proteção é o fator "
                       "usado nesse setor. 🔥 A banca também cobra a versão com o livre-comércio (beneficia o fator "
                       "abundante)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…segundo o Teorema Stolper-Samuelson, a renda real do fator usado intensivamente no outro setor "
            "se reduz.”</i> → CERTO",
            "<i>“…a renda do fator trabalho aumenta na mesma proporção que o preço da soja.”</i> → ERRADO (efeito "
            "ampliação: aumenta mais que proporcionalmente)",
        ])],
        "reescrita": ("Suponha que a produção de soja no Brasil seja intensiva em mão de obra e que o país imponha "
                      "uma barreira tarifária sobre a soja americana, segundo o Teorema Stolper-Samuelson, a renda "
                      "do fator trabalho no Brasil " + hl("aumenta") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Stolper-Samuelson: em cenário protecionista, a remuneração do fator protegido "
                             "aumenta; a tarifa sobre a soja americana aumenta a demanda pela soja nacional."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “mãode-obra” → “mão de obra”; “barreira tarifaria sofre” → “barreira "
                    "tarifária sobre” (erros de digitação da fonte)",
                    "quase_duplicata: ECO-E3-L00222-1 (mesmo item, simulado Nidi de abril/2025)"],
    },
    # ------------------------------------------------------------------ E1-0926
    {
        "id": "ECO-E1-0926-1", "fonte_ref": "E1-0926", "destino": "73", "subtema": H2["ho"],
        "tipo": "ME", "banca": "FGV", "prova": "Senado Federal/Consultor Legislativo/2022", "ano": 2022,
        "cacd": False, "errei": False,
        "comando": "Acerca das teorias neoclássicas de comércio internacional, resolva a questão a seguir.",
        "rotulo_item": "Questão",
        "assertiva": ("Assinale a opção que apresenta uma característica das teorias neoclássicas de comércio "
                      "internacional."
                      "</p><p>(A) As vantagens comparativas se originam de diferenças tecnológicas, culminando em "
                      "diferenças de produtividade do trabalho."
                      "</p><p>(B) Utilizam formulações tecnológicas lineares, sem diferenças intersetoriais de "
                      "alocação e de distribuição de renda nos países."
                      "</p><p>(C) Em cada país, os detentores dos fatores mais abundantes são menos beneficiados pela "
                      "abertura comercial e pela especialização."
                      "</p><p>(D) Em uma pequena economia aberta, as demandas por fatores são infinitamente "
                      "elásticas."
                      "</p><p>(E) Uma elevação do preço do bem intensivo em um determinado fator causa a elevação "
                      "tanto do preço desse fator e como do preço do outro fator."),
        "gabarito": "D", "gabarito_origem": "fonte", "status": "normal",
        "anotada": ("❌ " + az("(A) As vantagens comparativas se originam de ") + vm("diferenças tecnológicas, "
                    "culminando em diferenças de produtividade do trabalho") + az(".")
                    + "</p><p>❌ " + az("(B) Utilizam ") + vm("formulações tecnológicas lineares, sem diferenças "
                    "intersetoriais de alocação e de distribuição de renda") + az(" nos países.")
                    + "</p><p>❌ " + az("(C) Em cada país, os detentores dos fatores mais abundantes são ")
                    + vm("menos") + az(" beneficiados pela abertura comercial e pela especialização.")
                    + "</p><p>✅ " + az("(D) Em uma pequena economia aberta, as demandas por fatores são "
                                       "infinitamente elásticas.")
                    + "</p><p>❌ " + az("(E) Uma elevação do preço do bem intensivo em um determinado fator causa "
                                       "a elevação tanto do preço desse fator e como ") + vm("do preço do outro "
                                                                                              "fator") + az(".")),
        "poucas": ("No H-O com produção diversificada, os preços dos fatores ficam presos aos " + azb("preços dos "
                   "bens") + ", que o pequeno país toma do mercado mundial. Mudanças de dotação são absorvidas pela "
                   "composição da produção, não pelos salários: é a " + azb("insensibilidade dos preços dos "
                   "fatores") + ", ou demanda por fatores infinitamente elástica."),
        "destrinchando": [
            "(A) ❌ Vantagem comparativa por diferença de tecnologia e produtividade do trabalho é a marca da "
            "teoria <b>clássica</b> (" + oc("Ricardo") + "). Nas neoclássicas (H-O), a tecnologia é igual entre "
            "países e a vantagem nasce da " + azb("dotação relativa de fatores") + ".",
            "(B) ❌ É o oposto: as neoclássicas abandonam a tecnologia linear de Ricardo e usam funções com "
            "rendimentos marginais decrescentes (FPP côncava). Por isso têm efeitos intersetoriais de alocação "
            "e, sobretudo, " + azb("distributivos") + " (há ganhadores e perdedores dentro do país).",
            "(C) ❌ Pelo " + azb("teorema de Stolper-Samuelson") + ", a abertura eleva a remuneração real do fator "
            "<b>abundante</b> e reduz a do escasso: os detentores do fator abundante são os <b>mais</b> "
            "beneficiados.",
            "(D) ✅ Com dois bens, dois fatores e produção dos dois bens, as condições preço = custo unitário "
            "determinam w e r só a partir de p<sub>1</sub> e p<sub>2</sub>. Numa economia pequena, esses preços "
            "são dados pelo mundo; logo, um aumento da oferta de trabalho não derruba o salário: a economia "
            "expande o setor intensivo em trabalho (" + azb("Rybczynski") + ") e absorve o fator ao mesmo preço. "
            "Graficamente, a demanda por fator é horizontal. O resultado é associado a " + oc("Edward Leamer")
            + " (<i>factor price insensitivity</i>).",
            "(E) ❌ Stolper-Samuelson: o preço do fator intensivo sobe <b>mais</b> que o do bem, e o preço do outro "
            "fator <b>cai</b>. Os dois não sobem juntos em termos reais.",
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Os distratores alternam confusão de escola "
                       "(clássica × neoclássica em A e B) e inversão de teoremas (C e E). A correta é a menos "
                       "intuitiva: quem não conhece a insensibilidade dos preços dos fatores elimina as outras "
                       "quatro e chega a ela por exclusão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nas teorias neoclássicas, a abertura comercial beneficia o fator abundante e prejudica o fator "
            "escasso.”</i> → CERTO",
            "<i>“Nas teorias neoclássicas, a vantagem comparativa decorre de diferenças de produtividade do "
            "trabalho.”</i> → ERRADO (troca de escola: é Ricardo)",
        ])],
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": ["infinitamente"], "dificuldade": 3,
        "comentario_fonte": ("Gabarito do professor: D. A é clássica (Ricardo); B: neoclássicas usam funções não "
                             "lineares com efeitos distributivos; C: fator abundante é mais beneficiado; D: "
                             "insensibilidade dos preços dos fatores (Leamer); E: Stolper-Samuelson reduz o preço "
                             "do outro fator."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_confirmada: Senado Federal 2022 (Consultor Legislativo) — concurso organizado pela FGV; "
                    "a fonte não nomeia a banca",
                    "nota_redacao: gabarito D pela indicação “gabarito do professor” do verso"],
    },
    # ------------------------------------------------------------------ E1-0928
    {
        "id": "ECO-E1-0928-1", "fonte_ref": "E1-0928", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None,
        "cacd": False, "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("A teoria das vantagens comparativas introduz a idéia de que, independente da eficiência "
                      "absoluta, os países podem ganhar com o comércio internacional. Na prática, em um ambiente de "
                      "livre comércio, são exportados os bens para os quais os países têm vantagem comparativa, em "
                      "troca de bens para os quais os países são relativamente ineficientes na produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria das vantagens comparativas introduz a idéia de que, <u>independente da eficiência "
                      "absoluta</u>, os países podem ganhar com o comércio internacional. Na prática, em um ambiente "
                      "de livre comércio, são exportados os bens para os quais os países têm vantagem comparativa, em "
                      "troca de bens para os quais os países são <u>relativamente</u> ineficientes na produção."),
        "poucas": ("É a tese de " + oc("Ricardo") + " (" + vd("1817") + "): o que decide o comércio é o "
                   + azb("custo de oportunidade") + ", não a produtividade absoluta. Até o país menos eficiente em "
                   "tudo ganha ao exportar o bem em que sua desvantagem é menor."),
        "destrinchando": [
            "Exemplo de " + oc("Ricardo") + " (<i>Princípios de Economia Política e Tributação</i>): "
            + "<b>Portugal</b> precisava de menos homens-ano que a Inglaterra tanto para vinho (80 × 120) quanto "
            "para tecido (90 × 100). Tinha " + azb("vantagem absoluta") + " nos dois, mas sua vantagem era "
            "<b>relativamente maior</b> no vinho. Especializando-se em vinho e trocando por tecido inglês, os dois "
            "países consumiam mais do que em autarquia.",
            "Por isso o item fala em bens para os quais o país é <b>relativamente</b> ineficiente: a Inglaterra "
            "importava vinho não por ser incapaz de produzi-lo, mas porque cada barril custava, em tecido "
            "sacrificado, mais lá do que em Portugal.",
            "Contraste com " + oc("Adam Smith") + " (" + vd("1776") + "): na " + azb("vantagem absoluta") + ", "
            "cada país exporta o que produz com menos trabalho que o outro. Se um país for melhor em tudo, a "
            "teoria de Smith não explica o comércio; a de Ricardo, sim.",
            "Condição para o ganho mútuo: os termos de troca devem ficar <b>entre</b> os custos de oportunidade "
            "dos dois países. Fora desse intervalo, um deles prefere a autarquia.",
            vm("Regra-âncora: vantagem comparativa = menor custo de oportunidade; independe da vantagem "
               "absoluta."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Paráfrase do princípio ricardiano, salvaguardada pelos termos "
                       "“independente da eficiência absoluta” e “relativamente”. A banca costuma errar o item "
                       "trocando “relativamente” por “absolutamente” ou dizendo que o país sem vantagem absoluta "
                       "“não ganha” com o comércio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…em troca de bens para os quais os países são absolutamente ineficientes na produção.”</i> → "
            "ERRADO (troca de conceito: o critério é relativo)",
            "<i>“Um país sem vantagem absoluta em nenhum bem não obtém ganhos de comércio.”</i> → ERRADO "
            "(contradiz Ricardo)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito CERTO, uma imagem não preservada e um link do Telegram.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (303).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; comentário redigido a partir do conteúdo)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0935
    {
        "id": "ECO-E1-0935-1", "fonte_ref": "E1-0935", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": True,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("A hipótese de tecnologia semelhante entre países, adotada pelo modelo tradicional de dotação "
                      "relativa de fatores de Heckscher-Ohlin, não é compatível com um cenário em que a tecnologia "
                      "seja considerada um bem público."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A hipótese de tecnologia semelhante entre países, adotada pelo modelo tradicional de "
                       "dotação relativa de fatores de Heckscher-Ohlin, ") + vm("não é compatível")
                    + az(" com um cenário em que a tecnologia seja considerada um bem público.")),
        "poucas": ("Se a tecnologia é " + azb("bem público") + " (não rival e não excludente), todos os países têm "
                   "acesso a ela: é justamente o que justifica supor " + vd("funções de produção idênticas")
                   + " no H-O. As duas ideias são compatíveis."),
        "destrinchando": [
            "Premissas do H-O tradicional (2 × 2 × 2): dois países, dois bens, dois fatores; " + azb("tecnologia "
            "idêntica") + " entre países; rendimentos constantes de escala; concorrência perfeita; fatores móveis "
            "entre setores e imóveis entre países; preferências idênticas e homotéticas; sem custos de comércio.",
            "Por que supor tecnologia igual? Para isolar a única fonte de vantagem comparativa que o modelo quer "
            "estudar: a " + azb("dotação relativa de fatores") + ". Se as tecnologias diferissem, voltaríamos a "
            "uma explicação ricardiana.",
            "Um " + azb("bem público") + " é não rival (o uso de um não reduz o dos outros) e não excludente "
            "(ninguém pode ser impedido de usar). Conhecimento técnico livremente difundido entre países é o caso "
            "típico. Se todos acessam a mesma técnica, as funções de produção tendem a ser iguais: a hipótese do "
            "H-O ganha fundamento, não perde.",
            "O que contraria a premissa é o oposto: tecnologia " + azb("excludente") + " (patentes, segredo "
            "industrial, conhecimento tácito), que gera diferenças tecnológicas persistentes. É a base das teorias "
            "do " + azb("hiato tecnológico") + " (" + oc("Posner") + ") e do ciclo do produto (" + oc("Vernon")
            + ").",
            vm("Regra-âncora: tecnologia como bem público → acesso igual → funções de produção idênticas → "
               "coerente com o H-O."),
        ],
        "dissecando": (cz("[inversão]") + " O item nega uma relação que, na verdade, é de reforço. Quem associa "
                       "“bem público” a algo que “atrapalha o mercado” marca CERTO. Pista: pergunte o que a premissa "
                       "exige (todos com a mesma técnica) e o que o bem público garante (todos podem usar)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A existência de patentes que restringem a difusão tecnológica entre países tensiona a hipótese de "
            "tecnologia idêntica do modelo H-O.”</i> → CERTO",
            "<i>“No modelo H-O, o comércio decorre de diferenças tecnológicas entre países.”</i> → ERRADO (troca "
            "de modelo: é Ricardo)",
        ])],
        "reescrita": ("A hipótese de tecnologia semelhante entre países, adotada pelo modelo tradicional de dotação "
                      "relativa de fatores de Heckscher-Ohlin, " + hl("é compatível") + " com um cenário em que a "
                      "tecnologia seja considerada um bem público."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("H-O supõe que todos os países têm acesso à mesma tecnologia; a tecnologia como bem "
                             "público, não rival e não excludente, é compatível com o modelo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0936
    {
        "id": "ECO-E1-0936-1", "fonte_ref": "E1-0936", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo de dotação relativa de fatores em que os fatores modelados sejam o trabalho "
                      "qualificado e o não qualificado, o aumento salarial provocado por uma intensa demanda "
                      "relativa por trabalho não qualificado e associado a baixos níveis de produtividade poderia "
                      "explicar a chamada armadilha da renda média em países relativamente abundantes em trabalho "
                      "não qualificado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um modelo de dotação relativa de fatores em que os fatores modelados sejam o trabalho "
                      "qualificado e o não qualificado, o aumento salarial provocado por uma intensa demanda "
                      "relativa por trabalho não qualificado e associado a baixos níveis de produtividade "
                      "<u>poderia</u> explicar a chamada armadilha da renda média em países relativamente abundantes "
                      "em trabalho não qualificado."),
        "poucas": ("O país cresce exportando bens intensivos em " + azb("trabalho não qualificado") + "; a demanda "
                   "por esse fator eleva os salários sem que a produtividade acompanhe. Ele perde competitividade "
                   "para países mais baratos sem ter qualificação para competir nos setores sofisticados: a "
                   + azb("armadilha da renda média") + "."),
        "destrinchando": [
            "Releitura moderna do H-O: no lugar de capital e trabalho, os fatores são " + azb("trabalho "
            "qualificado") + " e " + azb("não qualificado") + ". O país abundante em trabalho não qualificado tem "
            "vantagem comparativa em bens intensivos nele (manufatura leve, montagem, agricultura intensiva em mão "
            "de obra).",
            "Pelo " + azb("Stolper-Samuelson") + ", a abertura eleva a remuneração do fator abundante. No início, "
            "isso é bom: salários sobem e a renda per capita sai da faixa baixa. Mas, se o salário sobe "
            "<b>sem ganho de produtividade</b>, o custo unitário do trabalho aumenta.",
            "Resultado: o país fica “espremido” entre economias de salário mais baixo, que tomam os setores "
            "intensivos em trabalho simples, e economias avançadas, que dominam os setores intensivos em "
            "qualificação e inovação. Estaciona na renda média.",
            "O conceito de " + azb("armadilha da renda média") + " ganhou força com " + oc("Gill e Kharas")
            + " (Banco Mundial, 2007). O " + rx("Brasil") + " é citado com frequência como caso, ao lado de "
            "outros latino-americanos, em contraste com Coreia do Sul e Taiwan, que investiram em educação e "
            "tecnologia e passaram à renda alta.",
            "Saída sugerida pela literatura: elevar a dotação de " + azb("capital humano") + " e a produtividade "
            "(educação, inovação, infraestrutura), mudando a vantagem comparativa em direção a setores mais "
            "intensivos em qualificação.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O item é longo e técnico, mas a construção é prudente: "
                       "“poderia explicar”. Para errá-lo, a banca precisaria afirmar que o mecanismo “explica "
                       "necessariamente” a armadilha ou trocar o fator (qualificado × não qualificado)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento salarial provocado por intensa demanda relativa por trabalho qualificado poderia "
            "explicar a armadilha da renda média em países abundantes em trabalho não qualificado.”</i> → ERRADO "
            "(fator trocado)",
            "<i>“A elevação da dotação relativa de trabalho qualificado é uma das estratégias para superar a "
            "armadilha da renda média.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["poderia"], "dificuldade": 2,
        "comentario_fonte": ("A concentração em setores intensivos em mão de obra não qualificada pode prender o "
                             "país na armadilha, por não abrir fronteiras produtivas em setores dinâmicos ligados "
                             "à inovação."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0938
    {
        "id": "ECO-E1-0938-1", "fonte_ref": "E1-0938", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("No modelo ricardiano das vantagens comparativas, os ganhos do comércio são explicados pelas "
                      "diferenças da produtividade marginal relativa do fator trabalho entre os países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo ricardiano das vantagens comparativas, os ganhos do comércio são explicados pelas "
                      "diferenças da produtividade marginal <u>relativa</u> do fator trabalho entre os países."),
        "poucas": ("Em " + oc("Ricardo") + ", o único fator é o " + azb("trabalho") + ", e o comércio nasce de "
                   "diferenças na produtividade <b>relativa</b> (tecnologia) entre países. Como a produtividade "
                   "é constante, a marginal coincide com a média."),
        "destrinchando": [
            "No modelo ricardiano, cada bem i exige a<sub>Li</sub> horas por unidade, fixas. A produtividade do "
            "trabalho é 1/a<sub>Li</sub>, " + vd("constante") + ": a última hora rende o mesmo que a primeira. "
            "Logo, produtividade marginal = produtividade média, e falar em “marginal” não muda o sentido.",
            "O que gera vantagem comparativa é a razão a<sub>LX</sub>/a<sub>LY</sub> (custo de oportunidade de X "
            "em Y) diferir entre países. Ou seja, produtividade <b>relativa</b>, não absoluta: um país pode ser "
            "mais produtivo em tudo e ainda assim ganhar com o comércio.",
            "Por trás das diferenças de produtividade estão diferenças de " + azb("tecnologia") + " (clima, "
            "técnica, organização). É exatamente o que distingue Ricardo do " + azb("H-O") + ", em que a "
            "tecnologia é igual e o que difere é a dotação de fatores.",
            "Ganho do comércio: cada país se especializa no bem de menor custo de oportunidade, a produção mundial "
            "aumenta e ambos consomem além da própria FPP, desde que os termos de troca fiquem entre os custos de "
            "oportunidade dos dois.",
            vm("Regra-âncora: Ricardo → um fator, produtividade relativa do trabalho, diferenças tecnológicas."),
        ],
        "dissecando": (cz("[detalhe]") + " O “marginal” pode assustar, porque lembra modelos neoclássicos. Como "
                       "a produtividade ricardiana é constante, marginal = média, e o item continua certo. O "
                       "termo decisivo é “relativa”: se fosse “absoluta”, o item seria ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os ganhos do comércio são explicados pelas diferenças de produtividade absoluta do trabalho "
            "entre os países.”</i> → ERRADO (absoluta × relativa: isso é Smith)",
            "<i>“…os ganhos do comércio são explicados pelas diferenças na dotação relativa de fatores.”</i> → "
            "ERRADO (troca de modelo: é H-O)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Especialização nos bens que custam menos horas de trabalho; custos comparativos; "
                             "um país pode ter custos absolutos menores em tudo e ainda ganhar com a especialização. "
                             "Afirma que a falha do modelo é desconsiderar a tecnologia."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "00046.jpeg", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "irrecuperavel (esquema não preservado; conteúdo coberto no 📖)"}],
        "alertas": ["qualidade_fonte: o comentário de origem diz que a falha do modelo ricardiano é desconsiderar a "
                    "tecnologia; ao contrário, as diferenças de produtividade do modelo são diferenças "
                    "tecnológicas — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0942
    {
        "id": "ECO-E1-0942-1", "fonte_ref": "E1-0942", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("A ausência de barreiras, em prol da liberalização das trocas externas, promove, entre outros "
                      "benefícios, o aumento da autossuficiência dos países no que concerne à disponibilidade de "
                      "bens e serviços e a redução dos riscos associados às oscilações nas quantidades produzidas e "
                      "nos preços praticados."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A ausência de barreiras, em prol da liberalização das trocas externas, promove, entre "
                       "outros benefícios, ") + vm("o aumento da autossuficiência dos países") + az(" no que "
                       "concerne à disponibilidade de bens e serviços")
                    + vm(" e a redução dos riscos") + az(" associados às oscilações nas quantidades produzidas e "
                                                         "nos preços praticados.")),
        "poucas": ("O livre-comércio leva à " + azb("especialização") + ", que é o contrário da autossuficiência: "
                   "cada país passa a depender de importações e aumenta a " + azb("interdependência") + ", com "
                   "maior exposição a choques de oferta e de preços externos."),
        "destrinchando": [
            "Pela lógica das " + azb("vantagens comparativas") + ", o ganho do comércio vem de cada país produzir "
            "<b>menos</b> variedade e trocar mais: concentra-se no que faz relativamente melhor e importa o resto. "
            "A disponibilidade de bens aumenta, mas via comércio, não via produção própria.",
            "Autossuficiência (autarquia) é o ponto de partida que a abertura abandona. Em autarquia, consumo = "
            "produção; com comércio, o consumo pode ficar fora da FPP justamente porque o país deixou de produzir "
            "tudo sozinho.",
            "Especialização concentra riscos: o país fica exposto às oscilações do preço do que exporta e à oferta "
            "do que importa. Daí a preocupação com a segurança de abastecimento de energia, alimentos e minérios e "
            "com a coordenação internacional. Para a " + azb("CEPAL") + " (" + oc("Prebisch") + "), a "
            "especialização em produtos primários expunha a periferia à instabilidade e à deterioração dos termos "
            "de troca.",
            "Nuance: diversificar <b>fornecedores</b> externos pode amortecer choques locais (uma quebra de safra "
            "doméstica é compensada por importações). Mas isso decorre da interdependência, não de mais "
            "autossuficiência, e não elimina a exposição a choques globais.",
            vm("Regra-âncora: livre-comércio → especialização → interdependência (não autossuficiência)."),
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " O item lista “benefícios” da abertura e enxerta o "
                       "oposto do que ela produz (autossuficiência) e uma promessa de menor risco que a "
                       "especialização não entrega. Pista: liberalizar é abrir mão de produzir tudo internamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A liberalização comercial tende a elevar a especialização produtiva e a interdependência entre os "
            "países.”</i> → CERTO",
            "<i>“A especialização elimina os riscos de crises de abastecimento.”</i> → ERRADO (modulador absoluto; "
            "na verdade os amplia)",
        ])],
        "reescrita": ("A ausência de barreiras, em prol da liberalização das trocas externas, promove, entre outros "
                      "benefícios, " + hl("a ampliação das opções dos países") + " no que concerne à "
                      "disponibilidade de bens e serviços" + hl(", mas aprofunda a interdependência entre eles e a "
                      "exposição aos riscos") + " associados às oscilações nas quantidades produzidas e nos preços "
                      "praticados."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O comércio tende a elevar a especialização e a interdependência, exigindo "
                             "coordenação para evitar crises de abastecimento (energia, alimentos, minérios)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0949
    {
        "id": "ECO-E1-0949-1", "fonte_ref": "E1-0949", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("Por elevar o custo de oportunidade do consumo, a especialização constitui uma das bases do "
                      "comércio internacional, o que contradiz a lei das vantagens comparativas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Por elevar o custo de oportunidade do consumo") + az(", a especialização constitui uma das "
                    "bases do comércio internacional, ") + vm("o que contradiz") + az(" a lei das vantagens "
                                                                                     "comparativas.")),
        "poucas": ("A " + azb("especialização") + " segundo as vantagens comparativas <b>reduz</b> o custo de "
                   "obter os bens e amplia as possibilidades de consumo; e ela não contradiz, mas " + vd("decorre")
                   + " da lei das vantagens comparativas."),
        "destrinchando": [
            "Cada país passa a produzir o bem em que tem " + azb("menor custo de oportunidade") + " e obtém o outro "
            "pelo comércio, a um preço relativo melhor do que o custo de produzi-lo internamente. Resultado: "
            "consome uma combinação <b>fora</b> da própria FPP. O custo de obter cada bem cai.",
            "Por isso a especialização é o canal pelo qual a " + azb("lei das vantagens comparativas") + " ("
            + oc("Ricardo") + ") gera ganhos: aumenta a produção mundial com os mesmos recursos e permite que "
            "todos consumam mais. Há coerência, não contradição.",
            "“Custo de oportunidade do consumo”, em sentido estrito, é um conceito intertemporal: consumir hoje "
            "custa a renda de juros que se deixa de ganhar poupando. Ele sobe com a " + azb("taxa de juros")
            + ", não com a especialização produtiva.",
            "A especialização também pode trazer ganhos dinâmicos (" + oc("Adam Smith") + ": divisão do trabalho, "
            "aprendizado, escala), reforçando o argumento.",
            vm("Regra-âncora: especialização por vantagem comparativa → menor custo de obter os bens → ganhos de "
               "comércio; ela é aplicação da lei, não contradição."),
        ],
        "dissecando": (cz("[nexo indevido · contradição]") + " Uma oração verdadeira (a especialização é base do "
                       "comércio) entre duas falsas: uma causa inventada (elevar custo de oportunidade) e uma "
                       "relação lógica invertida (“contradiz”). Pista: especialização e vantagem comparativa são "
                       "faces da mesma tese ricardiana."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao permitir que cada país produza o bem de menor custo de oportunidade, a especialização eleva o "
            "consumo possível, como prevê a lei das vantagens comparativas.”</i> → CERTO",
            "<i>“A especialização pelas vantagens comparativas exige que o país tenha vantagem absoluta no bem "
            "exportado.”</i> → ERRADO (confunde comparativa com absoluta)",
        ])],
        "reescrita": (hl("Por ampliar as possibilidades de consumo") + ", a especialização constitui uma das bases "
                      "do comércio internacional, " + hl("o que confirma") + " a lei das vantagens comparativas."),
        "tipo_erro": ["NEXO_INDEVIDO", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Dois erros: a especialização não eleva o custo de oportunidade do consumo (isso é "
                             "feito pela taxa de juros) e, nas vantagens comparativas, é a especialização que "
                             "gera ganhos de produtividade e bem-estar."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00195
    {
        "id": "ECO-E2-L00195-1", "fonte_ref": "E2-L00195", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_04,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o modelo Heckscher-Ohlin (H-O), o comércio internacional ocorre devido à diferença "
                      "entre a abundância relativa de recursos entre os países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o modelo Heckscher-Ohlin (H-O), o comércio internacional ocorre devido à diferença "
                      "entre a <u>abundância relativa</u> de recursos entre os países."),
        "poucas": ("É o núcleo do " + azb("H-O") + ": com tecnologia e preferências iguais, o que gera vantagem "
                   "comparativa é a diferença de " + vd("dotação relativa de fatores") + " (K/L, terra/L) entre "
                   "países."),
        "destrinchando": [
            oc("Eli Heckscher") + " (1919) e " + oc("Bertil Ohlin") + " (1933, <i>Interregional and "
            "International Trade</i>) perguntaram de onde vem a vantagem comparativa que " + oc("Ricardo")
            + " tomava como dada. A resposta: das diferenças de " + azb("abundância relativa de fatores")
            + ".",
            "Mecanismo: o fator relativamente abundante é relativamente barato em autarquia → o bem que o usa "
            "intensivamente sai relativamente barato → o país o exporta. Por isso o modelo também é chamado de "
            + azb("teoria das proporções de fatores") + ".",
            "Para isolar esse canal, o modelo supõe " + vd("tecnologias idênticas") + " e preferências iguais e "
            "homotéticas entre países. Se as tecnologias diferissem, a explicação voltaria a ser ricardiana.",
            "Abundância é sempre relativa: compara-se a razão K/L de um país com a do outro. Os EUA têm muito "
            "trabalho em termos absolutos, mas são relativamente abundantes em capital.",
            vm("Regra-âncora: Ricardo → diferença de tecnologia; H-O → diferença de dotação relativa de fatores."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Reescreve o teorema com “recursos” no lugar de “fatores”. O "
                       "risco está na palavra “relativa”: trocá-la por “absoluta” ou atribuir o comércio a "
                       "diferenças tecnológicas tornaria o item ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o modelo H-O, o comércio internacional ocorre devido às diferenças tecnológicas entre os "
            "países.”</i> → ERRADO (troca de modelo: é Ricardo)",
            "<i>“No modelo H-O, a abundância de um fator é avaliada em termos absolutos.”</i> → ERRADO "
            "(abundância é relativa)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No H-O, o padrão de comércio deriva das diferenças na dotação relativa de fatores; "
                             "cada país exporta bens intensivos no fator relativamente abundante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00196
    {
        "id": "ECO-E2-L00196-1", "fonte_ref": "E2-L00196", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_04,
        "rotulo_item": "Item",
        "assertiva": ("A equalização dos preços dos fatores não se manterá se os países tiverem tecnologias "
                      "diferentes no modelo H-O."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A equalização dos preços dos fatores <u>não se manterá</u> se os países tiverem tecnologias "
                      "diferentes no modelo H-O."),
        "poucas": ("O " + azb("teorema da equalização dos preços dos fatores") + " depende de " + vd("tecnologia "
                   "idêntica") + ": só assim os mesmos preços de bens implicam os mesmos salários e aluguéis. Com "
                   "técnicas diferentes, os preços dos fatores podem divergir mesmo com livre-comércio."),
        "destrinchando": [
            "O teorema (" + oc("Samuelson") + ", 1948–1949; intuição em " + oc("Heckscher") + " e "
            + oc("Ohlin") + "): o livre-comércio de bens iguala, entre países, os preços dos bens e, por meio "
            "deles, as remunerações absolutas e relativas dos fatores, mesmo sem migração. O comércio de bens "
            "funciona como substituto do movimento de fatores.",
            "Como funciona: com tecnologia igual e produção diversificada, as condições preço = custo unitário "
            "ligam (p<sub>1</sub>, p<sub>2</sub>) a um único par (w, r). Preços de bens iguais → (w, r) iguais. "
            "Se a função de produção difere, o mesmo preço é compatível com salários diferentes: o país mais "
            "produtivo paga mais.",
            "Outras condições exigidas: concorrência perfeita, rendimentos constantes, ausência de custos de "
            "transporte e tarifas, " + azb("produção diversificada") + " (os dois países produzem os dois bens) e "
            "ausência de " + azb("reversão de intensidade fatorial") + ".",
            "Na prática, a equalização plena não se observa: salários reais diferem muito entre países, em parte "
            "por diferenças tecnológicas e de produtividade, exatamente o que o item aponta. O teorema ilumina "
            "uma tendência à convergência, não um resultado literal.",
            vm("Regra-âncora: sem tecnologia idêntica (e sem as demais hipóteses), não há equalização dos preços "
               "dos fatores."),
        ],
        "dissecando": (cz("[literalidade]") + " Item de hipótese do teorema, com a negação na posição certa. A "
                       "banca o tornaria ERRADO dizendo que a equalização “independe” da tecnologia ou que exige "
                       "mobilidade internacional dos fatores (é o contrário: ocorre sem ela)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A equalização dos preços dos fatores exige a livre mobilidade internacional de capital e "
            "trabalho.”</i> → ERRADO (o comércio de bens substitui essa mobilidade)",
            "<i>“Tarifas e custos de transporte impedem a plena equalização dos preços dos fatores.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O teorema exige mesma tecnologia, concorrência perfeita e ausência de custos de "
                             "comércio; com tecnologias diferentes, salários e aluguéis podem divergir mesmo com "
                             "comércio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00197
    {
        "id": "ECO-E2-L00197-1", "fonte_ref": "E2-L00197", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_04,
        "rotulo_item": "Item",
        "assertiva": ("O país tem vantagem comparativa na produção de um bem quando o custo de oportunidade deste "
                      "bem em comparação com outro bem é menor do que o do outro país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O país tem vantagem comparativa na produção de um bem quando o <u>custo de oportunidade</u> "
                      "deste bem em comparação com outro bem é <u>menor</u> do que o do outro país."),
        "poucas": ("Definição ricardiana: " + azb("vantagem comparativa") + " = menor " + azb("custo de "
                   "oportunidade") + " (quanto do outro bem se sacrifica para produzir uma unidade) em relação ao "
                   "outro país."),
        "destrinchando": [
            "Custo de oportunidade de X em termos de Y = a<sub>LX</sub>/a<sub>LY</sub> (horas para fazer X ÷ "
            "horas para fazer Y). Exemplo: se o Brasil gasta 1/3 h no vestuário e 1/7 h no calçado, cada "
            "unidade de vestuário custa " + vd("7/3 calçados") + "; se o México gasta 1/2 h e 1 h, custa "
            + vd("1/2 calçado") + ". A vantagem comparativa em vestuário é do México.",
            "A comparação é <b>dentro</b> de cada país (razão entre bens) e depois <b>entre</b> países. Nunca se "
            "comparam horas diretamente entre países; isso é vantagem absoluta (" + oc("Adam Smith") + ").",
            "Consequência: com dois bens, cada país sempre tem vantagem comparativa em um deles (a menos que os "
            "custos de oportunidade sejam iguais, caso em que não há ganho de comércio). Até o país menos "
            "eficiente em tudo tem algo a exportar.",
            "Os termos de troca que permitem ganho mútuo ficam entre os dois custos de oportunidade.",
            vm("Regra-âncora: comparativa = custo de oportunidade menor; absoluta = menos insumo por unidade."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. A banca costuma errar o item trocando "
                       "“custo de oportunidade” por “custo de produção” ou “horas de trabalho”, que levam à "
                       "vantagem absoluta, ou invertendo para “maior”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O país tem vantagem comparativa na produção de um bem quando o produz com menos horas de trabalho "
            "do que o outro país.”</i> → ERRADO (troca de conceito: isso é vantagem absoluta)",
            "<i>“Um país pode ter vantagem comparativa em um bem no qual tem desvantagem absoluta.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Vantagem comparativa = menor custo de oportunidade (custo relativo); mesmo com "
                             "desvantagem absoluta em ambos os bens, o país ganha ao se especializar onde a "
                             "desvantagem relativa é menor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00198
    {
        "id": "ECO-E2-L00198-1", "fonte_ref": "E2-L00198", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_04,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o modelo Hecksher – Ohlim – Samuelson, a utilização intensa do fator abundante "
                      "aumenta a demanda do fator e eleva a remuneração do mesmo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o modelo Hecksher – Ohlim – Samuelson, a utilização intensa do fator abundante "
                      "aumenta a demanda do fator e <u>eleva a remuneração</u> do mesmo."),
        "poucas": ("Com a abertura, o país expande o setor intensivo no " + azb("fator abundante") + "; a demanda "
                   "por esse fator sobe e, pelo " + azb("teorema de Stolper-Samuelson") + ", sua remuneração "
                   "real " + vd("aumenta") + " (e a do fator escasso cai)."),
        "destrinchando": [
            "Cadeia: abertura → o preço relativo do bem exportável (intensivo no fator abundante) sobe "
            "internamente → o setor exportador se expande e o importador se contrai → o setor que cresce demanda "
            "muito do fator abundante e o que encolhe libera pouco dele → " + vd("remuneração real do fator "
            "abundante ↑") + "; a do escasso ↓.",
            "O modelo " + azb("Heckscher-Ohlin-Samuelson (HOS)") + " é a formalização de " + oc("Samuelson")
            + " do H-O, que inclui o " + azb("Stolper-Samuelson") + " (1941), a " + azb("equalização dos preços "
            "dos fatores") + " (1948) e, na mesma tradição, o " + azb("teorema de Rybczynski") + " (1955).",
            "Implicação distributiva: o comércio gera ganhos agregados, mas com ganhadores (donos do fator "
            "abundante) e perdedores (donos do fator escasso). Daí a economia política do protecionismo: o fator "
            "escasso pede tarifas.",
            "Aplicação: num país abundante em trabalho pouco qualificado, a abertura tenderia a elevar os salários "
            "desse grupo; num país abundante em capital, a elevar o retorno do capital.",
            vm("Regra-âncora: livre-comércio → fator abundante ganha, fator escasso perde (Stolper-Samuelson)."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Formulação informal (sem citar preços relativos) do resultado de "
                       "Stolper-Samuelson. Os erros de grafia dos nomes não alteram o conteúdo. A banca o tornaria "
                       "ERRADO trocando “abundante” por “escasso” ou dizendo que “ambos os fatores ganham”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o modelo HOS, o livre-comércio eleva a remuneração real de todos os fatores de "
            "produção.”</i> → ERRADO (o fator escasso perde)",
            "<i>“Segundo o modelo HOS, a proteção tarifária tende a beneficiar o fator escasso.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Stolper-Samuelson: aumento do preço relativo do bem intensivo no fator abundante "
                             "eleva a remuneração real desse fator e reduz a do escasso."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00212
    {
        "id": "ECO-E2-L00212-1", "fonte_ref": "E2-L00212", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_01,
        "rotulo_item": "Item",
        "assertiva": ("A teoria das vantagens absolutas de Adam Smith propõe que cada país deve se especializar em "
                      "produzir e exportar o bem que pode ser produzido ao menor custo de trabalho, ou seja, onde a "
                      "economia tenha a vantagem absoluta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria das vantagens absolutas de Adam Smith propõe que cada país deve se especializar em "
                      "produzir e exportar o bem que pode ser produzido ao <u>menor custo de trabalho</u>, ou seja, "
                      "onde a economia tenha a vantagem absoluta."),
        "poucas": ("Para " + oc("Adam Smith") + " (<i>A Riqueza das Nações</i>, " + vd("1776") + "), cada país deve "
                   "exportar o que produz com " + azb("menos trabalho") + " por unidade que os demais e importar o "
                   "que os outros fazem mais barato."),
        "destrinchando": [
            "Contexto: Smith escreve contra o " + azb("mercantilismo") + ", que via o comércio como jogo de soma "
            "zero e a riqueza como acúmulo de metais. Para ele, a riqueza é a capacidade produtiva, ampliada pela "
            + azb("divisão do trabalho") + ", e o comércio estende essa divisão ao plano internacional.",
            "Critério da " + azb("vantagem absoluta") + ": compara-se diretamente o custo em trabalho do mesmo bem "
            "entre países. Quem precisa de menos horas tem a vantagem. Cada país se especializa onde é absolutamente "
            "mais eficiente e ambos ganham.",
            "Limite: se um país for mais eficiente em <b>todos</b> os bens, a teoria de Smith não explica o "
            "comércio. " + oc("David Ricardo") + " (" + vd("1817") + ") resolve com a " + azb("vantagem "
            "comparativa") + ": o que importa é o custo de oportunidade.",
            "Smith usa a teoria do valor-trabalho em versão simples: o custo relevante é o trabalho. Daí a "
            "expressão “menor custo de trabalho” do item.",
            vm("Regra-âncora: Smith → vantagem absoluta (menos trabalho por unidade); Ricardo → vantagem "
               "comparativa (menor custo de oportunidade)."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, coerente nas duas orações. A versão ERRADA "
                       "clássica atribui a Smith o critério do custo de oportunidade ou diz que ele explicava o "
                       "comércio mesmo sem vantagem absoluta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Adam Smith, mesmo um país sem vantagem absoluta em nenhum bem ganha com o comércio.”</i> → "
            "ERRADO (troca de autor: é a tese de Ricardo)",
            "<i>“A teoria das vantagens absolutas rompe com a visão mercantilista do comércio como jogo de soma "
            "zero.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Smith: especialização nos bens com vantagem de custo absoluto; comércio livre, todos "
                             "ganham com a troca do que produzem de forma mais eficiente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00213
    {
        "id": "ECO-E2-L00213-1", "fonte_ref": "E2-L00213", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_01,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Heckscher-Ohlin sugere que uma economia deveria se especializar na produção de "
                      "bens que fazem uso intensivo de seus fatores de produção mais abundantes. Porém, ele não "
                      "considera variáveis como a tecnologia, o que o limita significativamente em contextos "
                      "modernos e o impede de fundamentar modelos neoclássicos desenvolvidos posteriormente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo de Heckscher-Ohlin sugere que uma economia deveria se especializar na produção de "
                       "bens que fazem uso intensivo de seus fatores de produção mais abundantes. Porém, ele ")
                    + vm("não considera variáveis como a tecnologia") + az(", o que o limita significativamente em "
                                                                            "contextos modernos")
                    + vm(" e o impede de fundamentar") + az(" modelos neoclássicos desenvolvidos posteriormente.")),
        "poucas": ("A 1ª frase é o teorema H-O. O erro está na 2ª: o modelo não ignora a tecnologia (supõe-na "
                   + vd("idêntica") + " entre países) e é justamente a " + azb("base") + " dos teoremas "
                   "neoclássicos posteriores (Stolper-Samuelson, equalização, Rybczynski)."),
        "destrinchando": [
            "Tecnologia no H-O: as funções de produção são <b>iguais</b> entre países. É uma escolha deliberada "
            "para isolar a dotação de fatores como fonte da vantagem comparativa. Tecnologia constante e simétrica "
            "não é tecnologia ignorada.",
            "A limitação é real: quando há diferenças tecnológicas grandes (semicondutores, aviação) ou economias "
            "de escala, o H-O explica pouco. O " + azb("paradoxo de Leontief") + " (1953) foi o primeiro grande "
            "teste empírico desfavorável.",
            "Mas o H-O é o alicerce da teoria neoclássica do comércio. " + oc("Samuelson") + " o formalizou no "
            "modelo " + azb("HOS") + " e dele derivou o " + azb("Stolper-Samuelson") + " (1941) e a "
            + azb("equalização dos preços dos fatores") + " (1948); " + oc("Rybczynski") + " (1955) acrescentou o "
            "efeito da dotação sobre a produção. Depois vieram o H-O-Vanek (muitos fatores) e as extensões com "
            "capital humano.",
            "As críticas posteriores (ciclo do produto de " + oc("Vernon") + ", novas teorias de " + oc("Krugman")
            + ") complementam o H-O e partem dele como referência; não o substituem.",
            vm("Regra-âncora: H-O supõe tecnologia idêntica e é a base, não um obstáculo, dos modelos "
               "neoclássicos."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 1ª frase, correta, dá credibilidade; o “Porém” "
                       "enxerta uma crítica com dois exageros: “não considera” (em vez de “supõe idêntica”) e "
                       "“impede de fundamentar” (quando fundamentou). Pista: H-O e HOS são a mesma linhagem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo H-O supõe tecnologias idênticas entre países, o que limita seu poder explicativo quando "
            "há grandes diferenças tecnológicas.”</i> → CERTO",
            "<i>“O teorema de Stolper-Samuelson foi desenvolvido para refutar o modelo H-O.”</i> → ERRADO (é "
            "desdobramento do próprio H-O)",
        ])],
        "reescrita": ("O modelo de Heckscher-Ohlin sugere que uma economia deveria se especializar na produção de "
                      "bens que fazem uso intensivo de seus fatores de produção mais abundantes. Porém, ele "
                      + hl("supõe tecnologia idêntica entre os países") + ", o que o limita significativamente em "
                      "contextos modernos" + hl(", mas não o impediu de fundamentar") + " modelos neoclássicos "
                      "desenvolvidos posteriormente."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A 1ª parte está certa; a 2ª erra ao dizer que o H-O não considera a tecnologia (supõe "
                             "tecnologia idêntica) e que o impede de fundamentar modelos neoclássicos (é o "
                             "alicerce do HOS: Stolper-Samuelson, equalização, Rybczynski). Vários comentários "
                             "empilhados, com comparação H-O × HOS."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 020", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (comparação H-O × HOS no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00214
    {
        "id": "ECO-E2-L00214-1", "fonte_ref": "E2-L00214", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_01,
        "rotulo_item": "Item",
        "assertiva": ("Na teoria do comércio de David Ricardo, são as vantagens comparativas que determinam em que "
                      "setor uma nação deve se especializar. Esta teoria baseia-se na eficiência relativa do fator "
                      "trabalho e propõe que mesmo que um país não tenha vantagem absoluta em nenhum produto, pode "
                      "beneficiar-se do comércio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na teoria do comércio de David Ricardo, são as vantagens comparativas que determinam em que "
                      "setor uma nação deve se especializar. Esta teoria baseia-se na <u>eficiência relativa</u> do "
                      "fator trabalho e propõe que <u>mesmo que um país não tenha vantagem absoluta em nenhum "
                      "produto, pode beneficiar-se</u> do comércio."),
        "poucas": ("Resumo exato de " + oc("Ricardo") + " (" + vd("1817") + "): especialização pela " + azb("vantagem "
                   "comparativa") + ", medida pela produtividade <b>relativa</b> do trabalho; o país sem vantagem "
                   "absoluta alguma ainda ganha exportando o bem em que sua desvantagem é menor."),
        "destrinchando": [
            "Hipóteses do modelo ricardiano: um único fator (" + azb("trabalho") + "), produtividade constante, "
            "trabalho móvel entre setores e imóvel entre países, concorrência perfeita, diferenças de "
            + azb("tecnologia") + " entre países. A FPP é reta e a especialização tende a ser completa.",
            "Exemplo de " + oc("Ricardo") + ": Portugal fazia vinho e tecido com menos trabalho que a Inglaterra, "
            "mas sua vantagem era relativamente maior no vinho. A Inglaterra, sem vantagem absoluta em nada, tinha "
            "vantagem comparativa no tecido. Especializando-se e trocando, os dois consumiam mais.",
            "Por que o país menos eficiente ganha? Porque produzir o bem importado lhe custaria mais, em termos do "
            "outro bem sacrificado, do que comprá-lo no exterior. O critério é o " + azb("custo de oportunidade")
            + ".",
            "A tese responde ao limite de " + oc("Adam Smith") + ", cuja vantagem absoluta não explicava o comércio "
            "de um país mais eficiente em tudo.",
            vm("Regra-âncora: vantagem comparativa basta para haver ganho de comércio; vantagem absoluta não é "
               "necessária."),
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Reúne a definição e a conclusão mais "
                       "contraintuitiva de Ricardo (ganho sem vantagem absoluta). Marca ERRADO quem acha que "
                       "“sem vantagem absoluta, não há o que exportar”. O “pode” mantém o item prudente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…esta teoria baseia-se na dotação relativa de capital e trabalho de cada país.”</i> → ERRADO "
            "(troca de modelo: é H-O)",
            "<i>“…o país sem vantagem absoluta só ganha com o comércio se os termos de troca lhe forem "
            "favoráveis além do custo de oportunidade do parceiro.”</i> → ERRADO (basta ficarem entre os custos "
            "dos dois)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Ricardo mostrou que o comércio beneficia mesmo o país sem vantagem absoluta, pela "
                             "especialização onde a eficiência relativa é maior."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00215
    {
        "id": "ECO-E2-L00215-1", "fonte_ref": "E2-L00215", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_01,
        "rotulo_item": "Item",
        "assertiva": ("A teoria do valor trabalho propõe que o valor de um bem é determinado inteiramente pelo total "
                      "de trabalho incorporado em sua produção, ignorando outros fatores como o capital e a inovação "
                      "tecnológica. Esta abordagem explícita favorece a análise de produção em economias homogêneas, "
                      "mas reconhece implicitamente que em contextos mais modernos e complexos, essa visão pode ser "
                      "restringida e, portanto, integrada com percepções sobre a inovação tecnológica e capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A teoria do valor trabalho propõe que o valor de um bem é determinado inteiramente pelo "
                       "total de trabalho incorporado em sua produção, ")
                    + vm("ignorando outros fatores como o capital e a inovação tecnológica")
                    + az(". Esta abordagem explícita ")
                    + vm("favorece a análise de produção em economias homogêneas, mas reconhece implicitamente que "
                         "em contextos mais modernos e complexos, essa visão pode ser restringida e, portanto, "
                         "integrada com percepções sobre a inovação tecnológica e capital") + az(".")),
        "poucas": ("A " + azb("teoria do valor-trabalho") + " não ignora o capital: trata-o como " + vd("trabalho "
                   "pretérito") + " incorporado nos meios de produção. E foi aplicada a economias capitalistas "
                   "complexas; as críticas à sua insuficiência vieram de fora da tradição, com os "
                   + azb("marginalistas") + "."),
        "destrinchando": [
            oc("Adam Smith") + " distinguiu trabalho incorporado e trabalho comandado. Reconheceu que o valor pelo "
            "trabalho valia de forma pura no “estado primitivo” e, com capital e terra apropriados, passou a "
            "decompor o preço em salário + lucro + renda.",
            oc("David Ricardo") + " (" + vd("1817") + ") fixou o valor na quantidade de trabalho necessária, "
            + azb("direta e indireta") + ": o trabalho gasto antes em ferramentas e máquinas entra no valor. O "
            "capital aparece como trabalho acumulado. Ricardo admitiu desvios quando a proporção de capital fixo "
            "varia entre setores.",
            oc("Karl Marx") + " refinou a teoria com o " + azb("tempo de trabalho socialmente necessário") + " e a "
            "divisão entre capital constante (máquinas, insumos: transfere valor) e capital variável (força de "
            "trabalho: cria mais-valia). A inovação é central: eleva a " + azb("composição orgânica do capital")
            + " e barateia as mercadorias. É a base da lei da tendência à queda da taxa de lucro.",
            "As críticas que levaram à superação da teoria vieram dos " + azb("marginalistas") + " (" + oc("Jevons")
            + ", " + oc("Menger") + ", " + oc("Walras") + ", década de " + vd("1870") + "): valor pela utilidade "
            "marginal e pela escassez, com o paradoxo da água e do diamante, além do problema da transformação de "
            "valores em preços.",
            "Ligação com o comércio: os coeficientes de horas do modelo ricardiano das vantagens comparativas são "
            "aplicação direta do valor-trabalho.",
        ],
        "dissecando": (cz("[juízo indevido · extrapolação]") + " Item prolixo, com aparência de síntese "
                       "equilibrada. Atribui à teoria uma omissão que ela não tem (o capital é trabalho "
                       "pretérito) e uma autocrítica “implícita” que nenhum clássico fez. Pista: “ignorando” e "
                       "“reconhece implicitamente” são juízos sem base nos autores."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Ricardo, o valor de uma mercadoria depende do trabalho direto e também do trabalho "
            "incorporado nos meios de produção utilizados.”</i> → CERTO",
            "<i>“Para Marx, o capital constante é a fonte da mais-valia.”</i> → ERRADO (troca de conceito: a "
            "mais-valia vem do capital variável)",
        ])],
        "reescrita": ("A teoria do valor trabalho propõe que o valor de um bem é determinado inteiramente pelo total "
                      "de trabalho incorporado em sua produção, " + hl("tratando o capital como trabalho pretérito e "
                      "a inovação tecnológica como redução do trabalho necessário") + ". Esta abordagem explícita "
                      + hl("foi aplicada a economias capitalistas complexas, e as críticas à sua suficiência vieram "
                           "sobretudo de fora da tradição clássica, com os marginalistas") + "."),
        "tipo_erro": ["JUIZO_INDEVIDO", "EXTRAPOLACAO"], "moduladores": ["inteiramente"], "dificuldade": 3,
        "comentario_fonte": ("A TVT não ignora o capital (trabalho pretérito, capital constante) nem a tecnologia "
                             "(tempo socialmente necessário, composição orgânica); foi aplicada a economias "
                             "complexas; as críticas vieram dos marginalistas. Vários comentários empilhados com "
                             "reescritas."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 021", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (análise da TVT no 📖)"}],
        "alertas": ["qualidade_fonte: um comentário de origem chama o paradoxo da água e do diamante de "
                    "“paradoxo de Jevons”; é o paradoxo do valor (Smith), e o paradoxo de Jevons trata de "
                    "eficiência e consumo de recursos — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L00296
    {
        "id": "ECO-E2-L00296-1", "fonte_ref": "E2-L00296", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("O Modelo Heckscher-Ohlin (H-O) pressupõe que as diferenças de produtividade do trabalho "
                      "(tecnologia) entre os países são a principal causa do comércio internacional, prevendo que "
                      "cada país exportará o bem em que sua mão de obra é relativamente mais produtiva."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Modelo Heckscher-Ohlin (H-O) pressupõe que ")
                    + vm("as diferenças de produtividade do trabalho (tecnologia) entre os países")
                    + az(" são a principal causa do comércio internacional, prevendo que cada país exportará o bem ")
                    + vm("em que sua mão de obra é relativamente mais produtiva") + az(".")),
        "poucas": ("O item descreve o " + azb("modelo ricardiano") + ". O " + azb("H-O") + " supõe "
                   + vd("tecnologia idêntica") + " e explica o comércio pela diferença de " + azb("dotação relativa "
                   "de fatores") + ": cada país exporta o bem intensivo no fator relativamente abundante."),
        "destrinchando": [
            "Quadro comparativo que a banca adora: " + oc("Ricardo") + " → um fator (trabalho), tecnologias "
            "diferentes, FPP reta, vantagem pela produtividade relativa do trabalho. " + oc("Heckscher-Ohlin")
            + " → dois fatores (capital e trabalho), tecnologia igual, FPP côncava, vantagem pela abundância "
            "relativa de fatores.",
            "O H-O nasce justamente para explicar o comércio <b>mesmo sem</b> diferença tecnológica: por que "
            "países com acesso às mesmas técnicas ainda trocam? Porque o fator abundante é barato e barateia os "
            "bens que o usam com intensidade.",
            "Consequências que só o H-O tem: efeitos distributivos internos (" + azb("Stolper-Samuelson") + "), "
            + azb("equalização dos preços dos fatores") + " e efeito das dotações sobre a produção ("
            + azb("Rybczynski") + "). No Ricardo, com um só fator, não há conflito distributivo entre fatores.",
            "O " + azb("paradoxo de Leontief") + " (EUA abundantes em capital exportando bens intensivos em "
            "trabalho) foi lido por alguns como sinal de que a produtividade, isto é, um elemento ricardiano, "
            "importava, o que estimulou modelos híbridos.",
            vm("Regra-âncora: produtividade/tecnologia → Ricardo; dotação de fatores → H-O."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item atribui ao H-O a premissa e a previsão do modelo "
                       "ricardiano, com linguagem técnica (“relativamente mais produtiva”) que soa correta. Pista: "
                       "a palavra “tecnologia” entre parênteses denuncia Ricardo, já que o H-O a supõe igual."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo ricardiano prevê que cada país exportará o bem em que sua mão de obra é relativamente "
            "mais produtiva.”</i> → CERTO",
            "<i>“O modelo H-O supõe que os países têm tecnologias idênticas e dotações de fatores diferentes.”</i> "
            "→ CERTO",
        ])],
        "reescrita": ("O Modelo Heckscher-Ohlin (H-O) pressupõe que " + hl("as diferenças de dotação relativa de "
                      "fatores entre os países") + " são a principal causa do comércio internacional, prevendo que "
                      "cada país exportará o bem " + hl("intensivo em seu fator relativamente abundante") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A descrição é do modelo ricardiano; o H-O supõe tecnologias idênticas e explica o "
                             "comércio pela dotação de fatores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00298
    {
        "id": "ECO-E2-L00298-1", "fonte_ref": "E2-L00298", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o Teorema de Stolper-Samuelson, derivado do modelo Heckscher-Ohlin, a abertura "
                      "comercial tende a aumentar a desigualdade de renda em países desenvolvidos (abundantes em "
                      "capital/trabalho qualificado) e a reduzi-la em países em desenvolvimento (abundantes em "
                      "trabalho não qualificado)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o Teorema de Stolper-Samuelson, derivado do modelo Heckscher-Ohlin, a abertura "
                      "comercial <u>tende a</u> aumentar a desigualdade de renda em países desenvolvidos (abundantes "
                      "em capital/trabalho qualificado) e a reduzi-la em países em desenvolvimento (abundantes em "
                      "trabalho não qualificado)."),
        "poucas": ("O " + azb("Stolper-Samuelson") + " diz que a abertura favorece o " + azb("fator abundante")
                   + ". No país rico, esse fator é capital ou qualificação (já no topo da distribuição): a "
                   "desigualdade sobe. No país pobre, é o trabalho não qualificado (na base): a desigualdade cai."),
        "destrinchando": [
            "Cadeia: abertura → o preço relativo do bem exportável sobe internamente → a remuneração real do fator "
            "intensivo nele sobe mais que proporcionalmente e a do outro fator cai (" + oc("Stolper e Samuelson")
            + ", " + vd("1941") + ").",
            "País desenvolvido: exporta bens intensivos em capital e qualificação (máquinas, serviços "
            "sofisticados) e importa bens intensivos em trabalho simples. Sobem os retornos do capital e o "
            + azb("prêmio de qualificação") + "; caem os salários dos menos qualificados. A distribuição se abre.",
            "País em desenvolvimento: exporta manufaturas leves e agrícolas intensivas em trabalho simples. O "
            "salário desse grupo sobe relativamente e a desigualdade cai, <b>na previsão teórica</b>.",
            "Ressalva empírica, que o “tende a” acomoda: na América Latina dos anos 1990, incluindo o " + rx("Brasil")
            + ", a abertura veio acompanhada de mais desigualdade salarial em vários países. Explicações: "
            + azb("mudança tecnológica viesada para qualificação") + ", cadeias globais de valor (a tarefa “não "
            "qualificada” transferida do Norte é relativamente qualificada no Sul), entrada da China com trabalho "
            "ainda mais barato e especialização em commodities intensivas em terra e capital.",
            "A leitura com trabalho qualificado × não qualificado é uma adaptação moderna do H-O, que originalmente "
            "usa capital × trabalho.",
        ],
        "dissecando": (cz("[modulador relativo]") + " Item longo que aplica o teorema aos dois tipos de país. O "
                       "“tende a” salva a proposição diante da evidência mista. Quem pensa na experiência latino-"
                       "americana marca ERRADO, mas o item pergunta o que diz o teorema, não o que a empiria "
                       "mostrou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com o Teorema de Stolper-Samuelson, a abertura comercial beneficia todos os fatores de "
            "produção, reduzindo a desigualdade em todos os países.”</i> → ERRADO (modulador absoluto; o fator "
            "escasso perde)",
            "<i>“A evidência empírica confirma integralmente que a abertura reduziu a desigualdade nos países em "
            "desenvolvimento.”</i> → ERRADO (evidência mista)",
        ]), ("🃏 Carta na manga", [
            "O Stolper-Samuelson explica por que a globalização gera ganhos agregados e, ao mesmo tempo, perdedores "
            "concentrados, o que alimenta a reação protecionista no Norte. Argumento útil para discutir políticas "
            "compensatórias (requalificação, seguro-desemprego) como condição da sustentabilidade política da "
            "abertura.",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": ("O teorema prevê ganho do fator abundante: países ricos (capital/qualificação) veem "
                             "desigualdade subir; países pobres, cair. Vários comentários empilhados, com evolução "
                             "das teorias e ressalvas empíricas (tecnologia viesada, cadeias de valor)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 033", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (síntese das teorias no 📖)"}],
        "alertas": ["texto_parcial: verso da fonte truncado no limite de caracteres; o conteúdo preservado basta "
                    "para o comentário"],
    },
    # ------------------------------------------------------------------ E2-L00494
    {
        "id": "ECO-E2-L00494-1", "fonte_ref": "E2-L00494", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_TAB,
        "excerto_tabela": TAB_086,
        "rotulo_item": "Item",
        "assertiva": "México detém vantagem absoluta na produção de ambos os bens.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": vm("México") + az(" detém vantagem absoluta na produção de ambos os bens."),
        "poucas": ("Vantagem absoluta = menos horas por unidade. O " + rx("Brasil") + " gasta menos nos dois bens: "
                   + vd("1/7 < 1") + " (calçados) e " + vd("1/3 < 1/2") + " (vestuário). A vantagem absoluta "
                   "em ambos é brasileira."),
        "destrinchando": [
            "A tabela dá " + azb("coeficientes técnicos") + " (horas por unidade). Quanto <b>menor</b> o "
            "coeficiente, mais produtivo o país. Cuidado para não ler como produção por hora, que inverteria tudo.",
            "Calçados: Brasil " + vd("1/7 h") + " × México " + vd("1 h") + " → o Brasil é 7 vezes mais "
            "produtivo. Vestuário: Brasil " + vd("1/3 h") + " × México " + vd("1/2 h") + " → 1,5 vez mais "
            "produtivo.",
            "Na teoria de " + oc("Adam Smith") + ", com vantagem absoluta do Brasil em tudo, não haveria comércio. "
            "Em " + oc("Ricardo") + ", há: a vantagem brasileira é relativamente maior em calçados (7× contra "
            "1,5×). O Brasil tem " + azb("vantagem comparativa") + " em calçados (custo de 3/7 de vestuário, contra "
            "2 no México) e o México, em vestuário (1/2 calçado, contra 7/3 no Brasil).",
            "Ganho mútuo com termos de troca entre 3/7 e 2 vestuários por calçado.",
            vm("Regra-âncora: absoluta → compare horas do mesmo bem entre países; comparativa → compare a razão "
               "entre bens dentro de cada país."),
        ],
        "dissecando": (cz("[troca de ator]") + " Troca o país detentor. Funciona com quem lê os números maiores do "
                       "México (1 e 1/2) como “mais produção”, quando são mais horas. 🔥 Tabelas de coeficientes "
                       "sempre testam a leitura horas × produtividade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Brasil detém vantagem absoluta em ambos os bens e, ainda assim, há base para comércio "
            "mutuamente vantajoso.”</i> → CERTO",
            "<i>“O México detém vantagem comparativa em calçados.”</i> → ERRADO (troca de bem: é em vestuário)",
        ])],
        "reescrita": hl("Brasil") + " detém vantagem absoluta na produção de ambos os bens.",
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O Brasil precisa de menos horas nos dois bens (1/7 < 1 e 1/3 < 1/2); a vantagem "
                             "absoluta é do Brasil."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_086,
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00495
    {
        "id": "ECO-E2-L00495-1", "fonte_ref": "E2-L00495", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_TAB,
        "excerto_tabela": TAB_086,
        "rotulo_item": "Item",
        "assertiva": "Brasil detém vantagem comparativa em vestuário.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": vm("Brasil") + az(" detém vantagem comparativa em vestuário."),
        "poucas": ("Vantagem comparativa = menor " + azb("custo de oportunidade") + ". Em vestuário, ele é "
                   + vd("7/3 de calçado") + " no Brasil e " + vd("1/2 calçado") + " no México: a vantagem é "
                   "mexicana. O Brasil a tem em calçados."),
        "destrinchando": [
            "Custo de oportunidade de 1 unidade de vestuário = horas no vestuário ÷ horas no calçado. "
            + rx("Brasil") + ": (1/3) ÷ (1/7) = " + vd("7/3 ≈ 2,33 calçados") + ". México: (1/2) ÷ 1 = "
            + vd("0,5 calçado") + ".",
            "Para fazer uma roupa, o Brasil abre mão de mais de dois pares de calçados; o México, de meio par. Logo "
            "o México tem vantagem comparativa em <b>vestuário</b>, e o Brasil em <b>calçados</b> (custo de 3/7 "
            "de vestuário por par, contra 2 no México).",
            "Armadilha: o Brasil tem " + azb("vantagem absoluta") + " também no vestuário (1/3 h < 1/2 h). Mas a "
            "pergunta é comparativa, e a vantagem brasileira no vestuário (1,5×) é bem menor que em calçados "
            "(7×).",
            "Com dois bens e dois países, se um país tem vantagem comparativa num bem, o outro necessariamente a "
            "tem no outro bem. Os custos de oportunidade de um bem são o inverso dos do outro.",
            vm("Regra-âncora: na comparativa, compara-se a razão entre os bens dentro de cada país, nunca as horas "
               "entre países."),
        ],
        "dissecando": (cz("[troca de ator · troca de conceito]") + " O item troca o país detentor e se apoia na "
                       "confusão absoluta × comparativa: quem olha só as horas vê o Brasil “melhor em tudo” e "
                       "marca CERTO. 🔥 Tabela de coeficientes com um país absolutamente superior nos dois bens é "
                       "a montagem preferida da banca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Brasil detém vantagem absoluta em vestuário.”</i> → CERTO",
            "<i>“Com termos de troca de 1 calçado por 3 unidades de vestuário, ambos ganham com o comércio.”</i> "
            "→ ERRADO (fora do intervalo 3/7–2)",
        ])],
        "reescrita": hl("México") + " detém vantagem comparativa em vestuário.",
        "tipo_erro": ["TROCA_ATOR", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Custo de oportunidade do vestuário: México 1/2 calçado; Brasil 7/3. México tem "
                             "vantagem comparativa em vestuário; Brasil, em calçados."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_086,
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00496
    {
        "id": "ECO-E2-L00496-1", "fonte_ref": "E2-L00496", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_TAB,
        "excerto_tabela": TAB_086,
        "rotulo_item": "Item",
        "assertiva": ("Os dois países, caso pratiquem livre-comércio, terão ganhos recíprocos de comércio, se o "
                      "preço relativo internacional for igual a 1."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os dois países, caso pratiquem livre-comércio, terão ganhos recíprocos de comércio, se o "
                      "preço relativo internacional for <u>igual a 1</u>."),
        "poucas": ("Há ganho mútuo quando os " + azb("termos de troca") + " ficam entre os custos de oportunidade "
                   "dos dois países. Em calçados por vestuário: " + vd("3/7 < 1 < 2") + ". Em vestuário por "
                   "calçado: " + vd("1/2 < 1 < 7/3") + ". Nas duas leituras, 1 está dentro."),
        "destrinchando": [
            "Custos de oportunidade de 1 calçado (em vestuário): " + rx("Brasil") + " (1/7) ÷ (1/3) = "
            + vd("3/7") + "; México 1 ÷ (1/2) = " + vd("2") + ". O Brasil tem vantagem comparativa em calçados, "
            "e o México, em vestuário.",
            "Com p = 1 (1 calçado = 1 roupa): o Brasil produz um par por 3/7 de roupa sacrificada e o troca por 1 "
            "roupa inteira, ganhando 4/7. O México produz uma roupa por 1/2 par sacrificado e a troca por 1 par, "
            "ganhando 1/2. Ambos consomem além de suas FPPs.",
            "Fora do intervalo, um lado perde: com p < 3/7, nem o Brasil quer exportar calçados; com p > 2, nem o "
            "México quer exportar vestuário. Nos extremos (p = 3/7 ou p = 2), todo o ganho fica com um país só.",
            "Onde o preço cai dentro do intervalo depende da demanda: é a " + azb("demanda recíproca") + " de "
            + oc("John Stuart Mill") + ". O país cujo produto é mais demandado pelo outro capta uma parte maior "
            "dos ganhos.",
            vm("Regra-âncora: ganho mútuo ⇔ termos de troca estritamente entre os custos de oportunidade dos dois "
               "países."),
        ],
        "grafico_verso": "ECO-E2-L00496-1-V1",
        "dissecando": (cz("[detalhe]") + " O item não diz em que unidade está o preço relativo, mas 1 é o inverso "
                       "de si mesmo: cai no intervalo nas duas leituras (calçado/vestuário ou vestuário/calçado). "
                       "Se a banca desse 2,5 ou 0,4, a unidade passaria a importar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…terão ganhos recíprocos se o preço relativo internacional for de 3 vestuários por calçado.”</i> "
            "→ ERRADO (fora do intervalo 3/7–2: o México não exportaria vestuário)",
            "<i>“Com o preço relativo igual a 2 vestuários por calçado, todo o ganho do comércio fica com o "
            "Brasil.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("1 calçado = 1 vestuário está no intervalo 3/7 < 1 < 2; Brasil exporta calçados e "
                             "México exporta vestuário, com ganhos mútuos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_086,
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00497
    {
        "id": "ECO-E2-L00497-1", "fonte_ref": "E2-L00497", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_TAB,
        "excerto_tabela": TAB_086,
        "rotulo_item": "Item",
        "assertiva": "Não há base para existir o comércio mutuamente vantajoso entre Brasil e México.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": vm("Não há") + az(" base para existir o comércio mutuamente vantajoso entre Brasil e México."),
        "poucas": ("A base do comércio vantajoso é a diferença de " + azb("custos de oportunidade") + ", não de "
                   "vantagem absoluta. Como " + vd("3/7 ≠ 2") + " (custo do calçado no Brasil e no México), há "
                   "espaço para especialização e ganho mútuo."),
        "destrinchando": [
            "O item explora a intuição de " + oc("Adam Smith") + ": como o " + rx("Brasil") + " tem vantagem "
            "absoluta nos dois bens (1/7 < 1 e 1/3 < 1/2), não precisaria comprar nada do México.",
            oc("Ricardo") + " mostra o contrário. O que importa é que a produtividade relativa difere: o Brasil é "
            "7 vezes mais produtivo em calçados e só 1,5 vez em vestuário. Custo de 1 calçado: Brasil "
            + vd("3/7 de vestuário") + "; México " + vd("2 vestuários") + ".",
            "O Brasil se especializa em calçados e o México em vestuário; com termos de troca entre 3/7 e 2 "
            "vestuários por calçado (por exemplo, 1 por 1), ambos consomem mais do que em autarquia.",
            "Só não haveria base para comércio se os custos de oportunidade fossem <b>iguais</b>, isto é, se a "
            "vantagem absoluta de um país fosse da mesma proporção nos dois bens.",
            vm("Regra-âncora: custos de oportunidade diferentes → há comércio mutuamente vantajoso, mesmo com "
               "vantagem absoluta de um país em tudo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item condiciona o comércio à vantagem absoluta (Smith) e "
                       "ignora a comparativa (Ricardo). Pista: quando a tabela mostra um país superior em tudo, a "
                       "banca quase sempre testa se o candidato ainda enxerga o ganho comparativo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Mesmo tendo vantagem absoluta nos dois bens, o Brasil ganha ao importar vestuário do México.”</i> "
            "→ CERTO",
            "<i>“Haveria base para comércio ainda que os custos de oportunidade fossem iguais nos dois países.”</i> "
            "→ ERRADO (sem diferença de custos de oportunidade, não há ganho de especialização)",
        ])],
        "reescrita": hl("Há") + " base para existir o comércio mutuamente vantajoso entre Brasil e México.",
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A base do comércio mutuamente vantajoso é a diferença nos custos de oportunidade, que "
                             "existe entre os dois países."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_086,
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00498
    {
        "id": "ECO-E2-L00498-1", "fonte_ref": "E2-L00498", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_2,
        "rotulo_item": "Item",
        "assertiva": ("No Modelo de Ricardo, a tecnologia difere entre os países, e as preferências dos "
                      "consumidores entre os países são idênticas. Já o Modelo de Heckscher-Ohlin pressupõe a "
                      "igualdade entre a tecnologia e a preferência dos consumidores entre os países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No Modelo de Ricardo, a tecnologia <u>difere</u> entre os países, e as preferências dos "
                      "consumidores entre os países são idênticas. Já o Modelo de Heckscher-Ohlin pressupõe a "
                      "<u>igualdade</u> entre a tecnologia e a preferência dos consumidores entre os países."),
        "poucas": ("Ricardo: " + vd("tecnologias diferentes") + " (é a fonte da vantagem comparativa). H-O: "
                   + vd("tecnologias iguais") + " e preferências iguais, para que só a " + azb("dotação de "
                   "fatores") + " explique o comércio."),
        "destrinchando": [
            "No " + azb("modelo ricardiano") + ", as diferenças de produtividade do trabalho (coeficientes "
            "a<sub>L</sub>) entre países refletem diferenças de tecnologia, e é delas que nasce a vantagem "
            "comparativa. Preferências são tratadas como iguais (ou irrelevantes para o padrão de "
            "especialização).",
            "No " + azb("H-O") + ", a hipótese de tecnologia idêntica serve para eliminar a explicação "
            "ricardiana. Preferências idênticas e homotéticas impedem que o padrão de comércio seja ditado por "
            "gostos: se um país abundante em capital preferisse muito bens intensivos em capital, poderia "
            "acabar importando-os (" + azb("reversão de demanda") + ", uma das explicações do paradoxo de "
            "Leontief).",
            "Demais hipóteses do H-O: dois fatores móveis entre setores e imóveis entre países, rendimentos "
            "constantes, concorrência perfeita, ausência de reversão de intensidade fatorial e de custos de "
            "comércio.",
            vm("Regra-âncora: Ricardo → tecnologia diferente; H-O → tecnologia e preferências iguais, dotações "
               "diferentes."),
        ],
        "dissecando": (cz("[literalidade]") + " Item de quadro comparativo de hipóteses, correto nos dois "
                       "modelos. A versão ERRADA clássica inverte a tecnologia (igual em Ricardo, diferente no H-O) "
                       "ou dá ao H-O preferências diferentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Heckscher-Ohlin, o comércio decorre de diferenças de tecnologia e de preferências "
            "entre os países.”</i> → ERRADO (o H-O supõe ambas iguais)",
            "<i>“No modelo de Ricardo, há um único fator de produção, o trabalho.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Ricardo baseia a vantagem comparativa na diferença de tecnologia; H-O supõe tecnologia "
                             "idêntica para focar na dotação de fatores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00501
    {
        "id": "ECO-E2-L00501-1", "fonte_ref": "E2-L00501", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_2,
        "rotulo_item": "Item",
        "assertiva": ("No Modelo Ricardiano, a Fronteira de Possibilidade de Produção é côncava, existem dois "
                      "fatores e pressupõe-se a lei dos rendimentos marginais decrescentes dos fatores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No Modelo Ricardiano, a Fronteira de Possibilidade de Produção é ") + vm("côncava")
                    + az(", ") + vm("existem dois fatores") + az(" e pressupõe-se ")
                    + vm("a lei dos rendimentos marginais decrescentes dos fatores") + az(".")),
        "poucas": ("O " + azb("modelo ricardiano") + " tem " + vd("um único fator") + " (trabalho) com "
                   "produtividade " + vd("constante") + ". O custo de oportunidade é constante e a FPP é uma "
                   + azb("reta") + ". O item descreve o modelo neoclássico (H-O)."),
        "destrinchando": [
            "Com um fator e coeficientes fixos (a<sub>LX</sub>, a<sub>LY</sub>), a restrição de recursos é "
            "a<sub>LX</sub>X + a<sub>LY</sub>Y = L, que é uma reta. A inclinação a<sub>LX</sub>/a<sub>LY</sub> "
            "é o custo de oportunidade de X, igual em qualquer ponto.",
            "Consequência: a especialização tende a ser " + azb("completa") + ". Se o preço relativo mundial "
            "supera o custo de oportunidade interno, o país produz só o bem em que tem vantagem comparativa.",
            "Já no " + azb("H-O") + " e no modelo de fatores específicos há dois ou mais fatores e rendimentos "
            "marginais decrescentes: o custo de oportunidade é crescente, a FPP é côncava e a especialização "
            "costuma ser parcial.",
            "Os três erros do item são, na verdade, as três marcas do modelo neoclássico. Basta um para marcar "
            "ERRADO.",
            vm("Regra-âncora: Ricardo = 1 fator + produtividade constante + FPP reta."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item transplanta para Ricardo as três características do "
                       "modelo neoclássico (FPP côncava, dois fatores, rendimentos decrescentes). Pista: “dois "
                       "fatores” já denuncia H-O."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Heckscher-Ohlin, a FPP é côncava, existem dois fatores e há rendimentos marginais "
            "decrescentes.”</i> → CERTO",
            "<i>“No modelo ricardiano, o custo de oportunidade é crescente ao longo da FPP.”</i> → ERRADO (é "
            "constante)",
        ])],
        "reescrita": ("No Modelo Ricardiano, a Fronteira de Possibilidade de Produção é " + hl("linear") + ", "
                      + hl("existe um único fator (trabalho)") + " e pressupõe-se " + hl("produtividade constante "
                      "do trabalho") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Ricardo: um fator (trabalho), custos de oportunidade constantes, FPP reta, sem "
                             "rendimentos decrescentes."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0915-1 (mesmo contraste FPP reta × côncava, cobrado pelo lado dos "
                    "fatores específicos)"],
    },
    # ------------------------------------------------------------------ E2-L00570
    {
        "id": "ECO-E2-L00570-1", "fonte_ref": "E2-L00570", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_1,
        "rotulo_item": "Item",
        "assertiva": "No Modelo Ricardiano, a mobilidade dos fatores de produção é assumida como perfeita entre os países.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No Modelo Ricardiano, a mobilidade dos fatores de produção é assumida como ")
                    + vm("perfeita entre os países") + az(".")),
        "poucas": ("Em " + oc("Ricardo") + ", o trabalho é " + vd("móvel entre setores") + " dentro do país e "
                   + vd("imóvel entre países") + ". É essa imobilidade que sustenta salários e custos diferentes e, "
                   "portanto, a vantagem comparativa."),
        "destrinchando": [
            "Se o trabalho migrasse livremente, os trabalhadores iriam para o país de maior produtividade e "
            "salário, e a produção se concentraria ali. O raciocínio de vantagem comparativa entre nações perderia "
            "o sentido. " + oc("Ricardo") + " justificava a imobilidade pela preferência das pessoas por "
            "permanecer em seu país e pela insegurança do capital no exterior.",
            "Por isso, na economia clássica, o comércio internacional tinha teoria própria: dentro do país, a "
            "mobilidade de fatores iguala os lucros e vale a vantagem absoluta (custos); entre países, sem essa "
            "mobilidade, vale a vantagem comparativa.",
            "Mobilidade interna perfeita garante que o trabalho se desloque para o setor de vantagem comparativa "
            "quando o país se abre: a especialização é completa e sem custo de ajuste.",
            "A mesma hipótese (fatores móveis entre setores, imóveis entre países) se repete no " + azb("H-O")
            + ". Lá, o comércio de bens funciona como substituto da mobilidade internacional de fatores "
            "(equalização dos preços dos fatores).",
            vm("Regra-âncora: modelos clássico e neoclássico de comércio → fatores móveis dentro do país, imóveis "
               "entre países."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Troca o âmbito da mobilidade: a perfeita é a "
                       "<b>interna</b>; a internacional é nula. Pista: se os fatores se movessem livremente entre "
                       "países, não haveria custos de oportunidade nacionais distintos a comparar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, o trabalho é perfeitamente móvel entre os setores de um mesmo país.”</i> → "
            "CERTO",
            "<i>“No modelo de Heckscher-Ohlin, o capital é perfeitamente móvel entre os países.”</i> → ERRADO "
            "(fatores imóveis entre países)",
        ])],
        "reescrita": ("No Modelo Ricardiano, a mobilidade dos fatores de produção é assumida como "
                      + hl("perfeita entre setores dentro de cada país, mas nula entre os países") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O trabalho é móvel entre setores dentro do país e imóvel entre países; essa "
                             "imobilidade justifica salários relativos diferentes e vantagens comparativas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
