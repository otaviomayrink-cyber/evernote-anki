"""Cards da redação 13 — ECO, passada 01 (nota 04-A: preço-consumo, Engel, efeitos renda/substituição)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "pc": "📈 Curva preço-consumo",
    "engel": "📉 Curva renda-consumo e Engel",
    "ers": "🔀 Efeitos renda e substituição",
    "giffen": "🥔 Bens inferiores e de Giffen",
    "slutsky": "🧮 Slutsky e Hicks",
}

CMD_GIFFEN = "Acerca dos bens inferiores e dos bens de Giffen, julgue o item a seguir."
CMD_ARM = "Com relação à teoria do consumidor, julgue o item a seguir."
CMD_NAB_3 = "Em relação à microeconomia, julgue (C ou E) os seguintes itens."
CMD_RT_CONS = "A respeito da teoria do consumidor, julgue os itens a seguir."
CMD_RT_MICRO = "Acerca dos conceitos e teorias da microeconomia, julgue os itens a seguir."
CMD_RT_MICRO2 = "A respeito dos conceitos e teorias da microeconomia, julgue os itens a seguir."
CMD_QUEST_0422 = "Julgue o item a seguir, relativo à teoria do consumidor."

CARDS = [
    # ------------------------------------------------------------------ E1-0013
    {
        "id": "ECO-E1-0013-1", "fonte_ref": "E1-0013", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_GIFFEN,
        "rotulo_item": "Item",
        "assertiva": ("O bem de Giffen é um tipo de bem muito específico na economia. A sua existência é estudada "
                      "pela microeconomia. É um tipo de bem no qual a demanda aumenta quando o preço aumenta, ou "
                      "seja, apresenta uma elasticidade-preço da demanda negativa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O bem de Giffen é um tipo de bem muito específico na economia. A sua existência é estudada "
                      "pela microeconomia. É um tipo de bem no qual a demanda aumenta quando o preço aumenta, ou "
                      "seja, apresenta uma elasticidade-preço da demanda ") + vm("negativa") + az("."),
        "poucas": ("Se a quantidade sobe quando o preço sobe, preço e quantidade andam juntos: a "
                   + azb("elasticidade-preço") + " do bem de Giffen é " + vd("positiva") + ", não negativa."),
        "destrinchando": [
            azb("Elasticidade-preço da demanda") + " = %Δq ÷ %Δp. Pela lei da demanda, p e q variam em sentidos "
            "opostos, e o sinal é " + vd("negativo") + " (muitos livros o reportam em módulo, |ε|, mas o sinal "
            "subjacente continua negativo).",
            "No " + azb("bem de Giffen") + ", p ↑ → q ↑: numerador e denominador têm o mesmo sinal, logo "
            + vd("ε > 0") + ". A curva de demanda é <b>positivamente inclinada</b> — a exceção à lei da demanda.",
            "Por quê: o bem é " + azb("inferior") + " e pesa tanto no orçamento que o " + azb("efeito renda")
            + " da alta de preço (o consumidor fica mais pobre e compra mais do bem barato) supera o "
            + azb("efeito substituição") + " (que sempre reduz a quantidade do bem que encareceu).",
            "Exemplo de manual: a batata na Irlanda do século XIX, atribuído a " + oc("Robert Giffen")
            + " por " + oc("Alfred Marshall") + "; evidência moderna com arroz e trigo em famílias muito pobres "
            "da China (" + oc("Jensen e Miller") + ", 2008).",
            vm("Regra-âncora: Giffen → elasticidade-preço positiva e elasticidade-renda negativa."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " Tudo está certo até o “ou seja”: a banca descreve "
                       "corretamente o comportamento (q sobe com p) e, na conclusão, troca o sinal da elasticidade. "
                       "Pista: o próprio item diz que p e q sobem juntos — razão de dois números positivos não "
                       "pode ser negativa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O bem de Giffen apresenta elasticidade-renda da demanda negativa.”</i> → CERTO",
            "<i>“O bem de Giffen apresenta elasticidade-preço da demanda negativa e elasticidade-renda "
            "positiva.”</i> → ERRADO (os dois sinais invertidos)",
        ])],
        "reescrita": ("O bem de Giffen […] é um tipo de bem no qual a demanda aumenta quando o preço aumenta, ou "
                      "seja, apresenta uma elasticidade-preço da demanda " + hl("positiva") + "."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO, com imagem não preservada e link para t.me/cacdeconomia/112.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (6).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0077
    {
        "id": "ECO-E1-0077-1", "fonte_ref": "E1-0077", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_GIFFEN,
        "rotulo_item": "Item",
        "assertiva": ("Bem de Giffen é o bem para o qual a curva de demanda sobe da esquerda para a direita. A "
                      "quantidade demandada pode variar na mesma direção da variação dos preços, e é isso que "
                      "ocasiona uma inclinação ascendente na curva de demanda individual."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Bem de Giffen é o bem para o qual a curva de demanda <u>sobe da esquerda para a direita</u>. "
                      "A quantidade demandada pode variar na <u>mesma direção</u> da variação dos preços, e é isso "
                      "que ocasiona uma inclinação ascendente na curva de demanda individual."),
        "poucas": ("É a definição do " + azb("bem de Giffen") + ": p e q variam no mesmo sentido, e a curva de "
                   "demanda (p no eixo vertical, q no horizontal) é " + vd("positivamente inclinada") + "."),
        "destrinchando": [
            "“Subir da esquerda para a direita” = inclinação positiva: mais preço, mais quantidade. É a única "
            "exceção teórica à " + azb("lei da demanda") + " dentro do modelo do consumidor racional.",
            "Mecanismo (Slutsky): alta de p → " + azb("efeito substituição") + " sempre reduz q; se o bem é "
            + azb("inferior") + ", a perda de renda real <b>aumenta</b> q (" + azb("efeito renda")
            + " oposto). Giffen = efeito renda maior, em módulo, que o substituição.",
            "Condições típicas: bem fortemente inferior, grande peso no orçamento, consumidor pobre, poucos "
            "substitutos. Por isso é raro e aparece em bens básicos de subsistência.",
            vm("Regra-âncora: todo bem de Giffen é inferior, mas nem todo bem inferior é de Giffen."),
            "Não confundir com o " + azb("bem de Veblen") + " (" + oc("Thorstein Veblen") + "), cuja demanda "
            "sobe com o preço por ostentação — fenômeno de preferências (o preço entra na utilidade), não de "
            "efeito renda.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de manual, salva pelo “pode "
                       "variar”. O risco é o candidato achar que “curva de demanda ascendente” é impossível e "
                       "marcar ERRADO por reflexo da lei da demanda. O “individual” também é preciso: a curva de "
                       "mercado só herda o formato se o efeito for forte entre os consumidores."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todo bem inferior tem curva de demanda que sobe da esquerda para a direita.”</i> → ERRADO "
            "(modulador absoluto: só os de Giffen)",
            "<i>“A inclinação ascendente da demanda do bem de Giffen decorre do predomínio do efeito "
            "substituição.”</i> → ERRADO (é o efeito renda que predomina)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Giffen: exceção à lei da demanda; bem inferior essencial em que o efeito renda supera "
                            "o substituição. Bem de Giffen é inferior, mas nem todo inferior é Giffen.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (12).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0084
    {
        "id": "ECO-E1-0084-1", "fonte_ref": "E1-0084", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2017", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_GIFFEN,
        "rotulo_item": "Item",
        "assertiva": "Um bem de Giffen é um bem com elasticidade-renda da demanda maior que 1.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um bem de Giffen é um bem com elasticidade-renda da demanda ") + vm("maior que 1") + az("."),
        "poucas": ("Elasticidade-renda " + vd("> 1") + " define o " + azb("bem de luxo") + ". O bem de Giffen "
                   "é inferior: elasticidade-renda " + vd("< 0") + " (e elasticidade-preço positiva)."),
        "destrinchando": [
            azb("Elasticidade-renda") + " η = %Δq ÷ %ΔR classifica os bens pela reação à <b>renda</b>: "
            + vd("η < 0") + " → inferior; " + vd("0 < η < 1") + " → normal de necessidade; " + vd("η > 1")
            + " → normal de luxo (superior).",
            "O " + azb("bem de Giffen") + " se define pela reação ao <b>preço</b>: q sobe quando p sobe "
            "(elasticidade-preço positiva). Isso só acontece se o efeito renda da variação de preço for oposto ao "
            "substituição e maior que ele — o que exige bem " + azb("inferior") + ". Logo, η do Giffen é "
            "necessariamente negativa.",
            "Os dois eixos de classificação não se confundem: luxo × necessidade × inferior olha a renda (curva de "
            "Engel); comum × Giffen olha o preço (curva de demanda). Um bem de luxo é o oposto do Giffen no eixo "
            "da renda.",
            vm("Regra-âncora: Giffen ⇒ inferior ⇒ η < 0; η > 1 ⇒ luxo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item cola no Giffen o critério de outro bem (luxo). A "
                       "banca aposta na associação vaga “Giffen = bem estranho / especial”. Pista: o item fala em "
                       "<b>renda</b> e um número (1) — a definição de Giffen fala em <b>preço</b> e sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um bem de Giffen é necessariamente um bem com elasticidade-renda negativa.”</i> → CERTO",
            "<i>“Todo bem com elasticidade-renda negativa é de Giffen.”</i> → ERRADO (generalização: nem todo "
            "inferior é Giffen)",
        ]), ("🧠 Mnemônico", ["Renda decide <b>inferior/normal/luxo</b>; preço decide <b>comum/Giffen</b>."])],
        "reescrita": ("Um bem de Giffen é um bem com elasticidade-renda da demanda " + hl("menor que zero")
                      + " " + hl("(bem inferior)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Vários comentários fundidos (inclusive da linha duplicada E1-0212): Giffen tem "
                            "elasticidade-renda negativa e elasticidade-preço positiva; η > 1 é bem de luxo. Um "
                            "dos comentários confundia Giffen com a curva de oferta de trabalho que se curva para "
                            "trás.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "531877-0cbcc8a3-…png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"},
                          {"ref": "531877-b875050b-…png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"},
                          {"ref": "image (67).png (duplicata E1-0212)", "tipo_fonte": "desconhecido",
                           "lado": "verso", "acao": "irrecuperavel"}],
        "alertas": ["qualidade_fonte: um dos comentários da fonte define Giffen pela oferta de trabalho que se "
                    "curva para trás (lazer × salário) — exemplo de efeito renda, não definição de Giffen; "
                    "descartado",
                    "duplicata fundida: comentário de E1-0212 incorporado"],
    },
    # ------------------------------------------------------------------ E2-L00326
    {
        "id": "ECO-E2-L00326-1", "fonte_ref": "E2-L00326", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A Equação de Slutsky demonstra que, para um bem de Giffen, o efeito renda deve ser "
                      "necessariamente negativo (considerando o bem como inferior) e sua magnitude, em termos "
                      "absolutos, deve ser superior à magnitude do efeito substituição."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Equação de Slutsky demonstra que, para um bem de Giffen, o efeito renda deve ser "
                      "necessariamente negativo (considerando o bem como inferior) e sua magnitude, "
                      "<u>em termos absolutos</u>, deve ser <u>superior</u> à magnitude do efeito substituição."),
        "poucas": ("Giffen exige as duas condições: bem " + azb("inferior") + " (efeito renda contrário ao "
                   "substituição) e efeito renda " + vd("maior em módulo") + " — só assim Δq/Δp fica positivo."),
        "destrinchando": [
            azb("Equação de Slutsky") + ": ∂x/∂p = ∂h/∂p − x·∂x/∂R. O 1º termo é o " + azb("efeito substituição")
            + " (variação compensada), sempre ≤ 0; o 2º é o " + azb("efeito renda") + ", com o sinal de −x·∂x/∂R.",
            "Bem normal (∂x/∂R > 0): o efeito renda também é negativo e reforça o substituição → ∂x/∂p < 0. "
            "Bem inferior (∂x/∂R < 0): o termo renda fica positivo e se opõe ao substituição.",
            "Giffen (∂x/∂p > 0) só ocorre se o termo renda positivo superar o substituição em valor absoluto: "
            + vd("|x·∂x/∂R| > |∂h/∂p|") + ". Daí a receita: bem muito inferior (∂x/∂R muito negativo) e com "
            "grande consumo x (peso no orçamento).",
            "Sobre o sinal: o item chama de “negativo” o efeito renda no sentido de a <b>renda</b> e a quantidade "
            "variarem em sentidos opostos (bem inferior). Na fórmula, o termo −x·∂x/∂R aparece positivo — "
            "mesma ideia, convenção diferente; o parêntese do item deixa claro o sentido.",
            vm("Regra-âncora: Giffen = inferior + efeito renda dominante (em módulo)."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Reprodução fiel da condição de Giffen. A armadilha está "
                       "nos sinais: quem pensa no termo da fórmula (positivo para inferior) pode marcar ERRADO "
                       "pelo “negativo”; o parêntese “considerando o bem como inferior” desfaz a dúvida. Em "
                       "itens de Slutsky, leia o sinal pela relação descrita, não pelo símbolo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para um bem de Giffen, basta que o efeito renda seja de sentido oposto ao efeito "
            "substituição.”</i> → ERRADO (falta a dominância em módulo: isso define só o inferior)",
            "<i>“Para um bem de Giffen, o efeito substituição tem o mesmo sinal da variação do preço.”</i> → "
            "ERRADO (o substituição é sempre de sinal oposto ao preço)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["necessariamente"], "dificuldade": 2,
        "comentario_fonte": "Slutsky decompõe o efeito total; Giffen exige bem inferior e efeito renda forte o "
                            "bastante para superar o substituição.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00347
    {
        "id": "ECO-E2-L00347-1", "fonte_ref": "E2-L00347", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Em bens inferiores, o efeito renda é negativo; se ele domina o efeito substituição "
                      "(positivo), o preço e a quantidade demandada movem-se na mesma direção, caracterizando bem "
                      "de Giffen - fenômeno que só pode ocorrer quando as preferências são não convexas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em bens inferiores, o efeito renda é negativo; se ele domina o efeito substituição "
                      "(positivo), o preço e a quantidade demandada movem-se na mesma direção, caracterizando bem "
                      "de Giffen - fenômeno que ") + vm("só pode ocorrer quando as preferências são não convexas")
                   + az("."),
        "poucas": ("O Giffen nasce da " + azb("dominância do efeito renda") + " num bem inferior e é "
                   "plenamente compatível com " + vd("preferências convexas") + " (curvas de indiferença bem "
                   "comportadas). O “só pode” é falso."),
        "destrinchando": [
            "Leitura dos sinais do item (para uma <b>queda</b> de preço): o " + azb("efeito substituição")
            + " aumenta q (positivo); no bem " + azb("inferior") + ", o ganho de renda real reduz q (efeito "
            "renda negativo). Se o renda vence, p ↓ → q ↓: preço e quantidade na mesma direção = "
            + azb("Giffen") + ". Até aqui, correto.",
            azb("Convexidade das preferências") + " = gosto por cestas médias (TMS decrescente). Ela garante que "
            "o efeito substituição seja não positivo e que a tangência seja um ótimo, mas <b>não diz nada</b> "
            "sobre o sinal ou o tamanho do efeito renda. Logo, não impede Giffen.",
            "Os exemplos de manual (batata irlandesa; arroz em famílias pobres de Hunan, " + oc("Jensen e Miller")
            + ", 2008) usam curvas de indiferença convexas comuns: basta que o bem seja muito inferior e pese "
            "muito no orçamento.",
            "Não convexidade leva a outra coisa: ótimos de canto e saltos na demanda — comportamento estranho, "
            "mas não o mecanismo de Giffen.",
            vm("Regra-âncora: Giffen é questão de efeito renda (sinal e tamanho), não de convexidade."),
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A primeira parte é uma descrição correta do "
                       "Giffen; o erro foi enxertado no final, com a restrição “só pode” e uma condição técnica "
                       "que soa sofisticada. 🔥 Itens longos e corretos que terminam com “só/somente/apenas” "
                       "pedem atenção redobrada à cauda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…caracterizando bem de Giffen, fenômeno compatível com preferências convexas.”</i> → CERTO",
            "<i>“Em bens inferiores, o efeito renda sempre domina o efeito substituição.”</i> → ERRADO "
            "(generalização: isso é só o Giffen)",
        ])],
        "reescrita": ("Em bens inferiores, o efeito renda é negativo; se ele domina o efeito substituição "
                      "(positivo), o preço e a quantidade demandada movem-se na mesma direção, caracterizando bem "
                      "de Giffen - fenômeno que " + hl("pode ocorrer mesmo com preferências convexas") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": ["só"], "dificuldade": 2,
        "comentario_fonte": "Várias respostas de IA concordantes: Giffen não exige preferências não convexas; "
                            "decorre de bem inferior com efeito renda dominante; condições típicas (bem básico, "
                            "grande peso no orçamento, consumidor pobre).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00419
    {
        "id": "ECO-E2-L00419-1", "fonte_ref": "E2-L00419", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": "Todo bem inferior pode apresentar curva de demanda positivamente inclinada.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": vm("Todo") + az(" bem inferior pode apresentar curva de demanda positivamente inclinada."),
        "poucas": ("Demanda positivamente inclinada é o " + azb("bem de Giffen") + ", um subconjunto raro dos "
                   "inferiores. Na maioria dos " + azb("bens inferiores") + " o efeito substituição prevalece "
                   "e a demanda continua decrescente."),
        "destrinchando": [
            "Bem " + azb("inferior") + " = elasticidade-renda negativa (renda ↑ → consumo ↓). Isso fixa só o "
            "<b>sentido</b> do efeito renda (oposto ao substituição), não o tamanho dele.",
            "Para a curva subir, o efeito renda precisa vencer o substituição. O tamanho do efeito renda depende "
            "de x·∂x/∂R: só é grande se o bem tiver " + vd("peso alto no orçamento") + " e for fortemente "
            "inferior. Um bem inferior barato e marginal na cesta (margarina, ônibus para quem também usa táxi) "
            "tem efeito renda pequeno demais.",
            "Conjuntos: Giffen ⊂ inferiores ⊂ todos os bens. " + vm("Todo Giffen é inferior; nem todo inferior "
            "é Giffen.") + "",
            "Daí o veredito: o item, com “todo”, estende a todos os inferiores uma possibilidade que só existe "
            "para os que reúnem as condições de Giffen.",
        ],
        "dissecando": (cz("[modulador absoluto · inversão]") + " O “todo” transforma a relação de inclusão "
                       "(Giffen ⇒ inferior) na recíproca (inferior ⇒ pode ser Giffen). O “pode” tenta "
                       "suavizar e induzir CERTO; a banca considerou que o peso orçamentário pequeno impede a "
                       "maioria dos inferiores de ter demanda ascendente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todo bem de Giffen é inferior.”</i> → CERTO",
            "<i>“Um bem inferior pode apresentar curva de demanda positivamente inclinada.”</i> → CERTO",
        ])],
        "reescrita": (hl("Nem todo") + " bem inferior pode apresentar curva de demanda positivamente "
                      "inclinada" + hl(": só o de Giffen") + "."),
        "tipo_erro": ["GENERALIZACAO", "INVERSAO"], "moduladores": ["todo", "pode"], "dificuldade": 2,
        "comentario_fonte": "Esse é o caso do Giffen, excepcional: efeito renda supera o substituição, com alto "
                            "peso no orçamento.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00672
    {
        "id": "ECO-E2-L00672-1", "fonte_ref": "E2-L00672", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito da teoria do consumidor e dos conceitos de elasticidade, julgue (C ou E) os "
                   "seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("Se um bem é considerado inferior, a sua curva de demanda marshalliana será necessariamente "
                      "positivamente inclinada, caracterizando o Paradoxo de Giffen."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um bem é considerado inferior, a sua curva de demanda marshalliana ")
                   + vm("será necessariamente") + az(" positivamente inclinada, caracterizando o Paradoxo de "
                                                      "Giffen."),
        "poucas": ("Ser inferior é " + azb("necessário") + ", mas não " + azb("suficiente") + " para Giffen: "
                   "na maioria dos inferiores o efeito substituição prevalece e a demanda marshalliana segue "
                   + vd("decrescente") + "."),
        "destrinchando": [
            azb("Demanda marshalliana") + " x(p, R): renda nominal constante; capta o efeito total (substituição "
            "+ renda). " + azb("Demanda hicksiana") + " h(p, U): utilidade constante; só o efeito substituição, "
            "e por isso é <b>sempre</b> não crescente — nem Giffen a faz subir.",
            "Bem inferior: o efeito renda tem sentido oposto ao substituição. Três casos para p ↑: (1) "
            "substituição domina → q ↓ (inferior comum); (2) empate → q constante; (3) renda domina → q ↑ "
            "(" + azb("Giffen") + ").",
            "Logo, inferioridade ⇒ só abre a <b>possibilidade</b> de Giffen. A implicação correta é a inversa: "
            + vm("Giffen ⇒ inferior.") + "",
            "“Paradoxo de Giffen” é o nome tradicional, dado por " + oc("Marshall") + " nos <i>Principles</i>, "
            "porque contraria a lei da demanda.",
        ],
        "dissecando": (cz("[modulador absoluto · inversão]") + " Troca condição necessária por suficiente, com "
                       "o “necessariamente” como alavanca. 🔥 A dupla inferior/Giffen é das mais cobradas: "
                       "sempre que o item partir de “se é inferior” e concluir Giffen, desconfie."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se um bem é de Giffen, ele é necessariamente inferior.”</i> → CERTO",
            "<i>“Para um bem de Giffen, a curva de demanda hicksiana é positivamente inclinada.”</i> → ERRADO "
            "(a hicksiana é sempre não crescente)",
        ])],
        "reescrita": ("Se um bem é considerado inferior, a sua curva de demanda marshalliana "
                      + hl("poderá ser") + " positivamente inclinada, caracterizando o Paradoxo de Giffen, "
                      + hl("se o efeito renda superar o efeito substituição") + "."),
        "tipo_erro": ["GENERALIZACAO", "INVERSAO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": "Todo Giffen é inferior, mas nem todo inferior é Giffen; na maioria dos inferiores o "
                            "substituição prevalece.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01522
    {
        "id": "ECO-E2-L01522-1", "fonte_ref": "E2-L01522", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_CONS,
        "rotulo_item": "Item",
        "assertiva": "A curva de Engel para bens de Giffen tem inclinação positiva, contrariando a lei da demanda.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A ") + vm("curva de Engel") + az(" para bens de Giffen tem inclinação positiva, "
                                                         "contrariando a lei da demanda."),
        "poucas": ("Quem sobe no Giffen é a " + azb("curva de demanda") + " (q × p). A " + azb("curva de Engel")
                   + " (q × renda) do Giffen é " + vd("negativamente inclinada") + ", porque todo Giffen é "
                   "inferior."),
        "destrinchando": [
            azb("Curva de Engel") + ": quantidade consumida em função da <b>renda</b>, com preços constantes "
            "(" + oc("Ernst Engel") + ", século XIX). Inclinação positiva → bem normal; negativa → bem inferior. "
            "Côncava (cresce menos que a renda) → necessidade; convexa → luxo.",
            azb("Curva de demanda") + ": quantidade em função do <b>preço do próprio bem</b>, com renda e demais "
            "preços constantes. É ela que a " + azb("lei da demanda") + " diz ser decrescente — e é ela que o "
            "Giffen viola.",
            "No Giffen, os dois gráficos “sobem” em sentidos opostos: Engel " + vd("decrescente") + " (bem "
            "inferior: renda ↑ → q ↓) e demanda " + vd("crescente") + " (efeito renda da alta de preço supera o "
            "substituição: p ↑ → q ↑).",
            vm("Regra-âncora: Engel olha a renda (normal × inferior); demanda olha o preço (comum × Giffen)."),
        ],
        "grafico_verso": "ECO-E2-L01522-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item troca a curva: a afirmação “inclinação positiva, "
                       "contrariando a lei da demanda” é verdadeira para a <b>demanda</b> do Giffen e falsa para "
                       "a Engel. A própria cauda denuncia o erro: lei da demanda fala de preço, e a Engel não tem "
                       "preço no eixo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de demanda dos bens de Giffen tem inclinação positiva, contrariando a lei da "
            "demanda.”</i> → CERTO",
            "<i>“A curva de Engel dos bens de Giffen tem inclinação negativa.”</i> → CERTO",
        ])],
        "reescrita": ("A " + hl("curva de demanda") + " para bens de Giffen tem inclinação positiva, "
                      "contrariando a lei da demanda."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Engel relaciona quantidade e renda; Giffen é inferior, então sua Engel é "
                            "negativamente inclinada; é a curva de demanda que contraria a lei da demanda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 406", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "texto (curvas de Engel de necessidade e de luxo descritas no 📖)"},
                          {"ref": "IMAGEM 407", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01522-1-V1, painel da Engel)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01689
    {
        "id": "ECO-E2-L01689-1", "fonte_ref": "E2-L01689", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("Para um bem inferior, os efeitos renda e substituição vão em direções contrárias, de forma "
                      "que para uma redução do preço do bem, o efeito renda fará a demanda aumentar."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para um bem inferior, os efeitos renda e substituição vão em direções contrárias, de forma "
                      "que para uma redução do preço do bem, o efeito renda fará a demanda ") + vm("aumentar")
                   + az("."),
        "poucas": ("Preço cai → " + azb("renda real sobe") + " → num bem " + azb("inferior") + " o consumo "
                   + vd("cai") + ". Quem aumenta a demanda é o efeito substituição."),
        "destrinchando": [
            "Decomponha a <b>queda</b> de p em dois passos. " + azb("Efeito substituição") + ": o bem ficou "
            "relativamente mais barato → q ↑ (vale para qualquer bem). " + azb("Efeito renda") + ": com o mesmo "
            "dinheiro, o consumidor ficou mais rico.",
            "O que ele faz com a renda extra depende da " + azb("elasticidade-renda") + ": bem normal (η > 0) → "
            "compra mais (renda reforça substituição); bem inferior (η < 0) → compra <b>menos</b> (renda se "
            "opõe ao substituição).",
            "Resultado no inferior comum: substituição (+) > renda (−) → q ainda sobe, porém menos que num bem "
            "normal. No " + azb("Giffen") + ", renda (−) > substituição (+) → q cai quando p cai.",
            vm("Regra-âncora: no inferior, o efeito renda empurra q no mesmo sentido do preço."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 1ª oração (direções contrárias) está certa; a "
                       "conclusão atribui ao efeito renda o sinal que é do substituição. O “de forma que” "
                       "simula uma dedução que, na verdade, contradiz a premissa: se os efeitos são contrários "
                       "e o substituição aumenta q, o renda tem de reduzi-la."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…para uma redução do preço do bem, o efeito substituição fará a demanda aumentar.”</i> → CERTO",
            "<i>“Para um bem inferior, a redução do preço sempre reduz a quantidade demandada.”</i> → ERRADO "
            "(só no Giffen)",
        ])],
        "reescrita": ("Para um bem inferior, os efeitos renda e substituição vão em direções contrárias, de forma "
                      "que para uma redução do preço do bem, o efeito renda fará a demanda " + hl("diminuir")
                      + "."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Primeira parte correta; queda de preço eleva a renda real, que reduz a demanda do "
                            "bem inferior; o trecho errado é “o efeito renda fará a demanda aumentar”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 492", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (elasticidade-renda no 📖)"},
                          {"ref": "IMAGEM 493", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (bem inferior com curvas de indiferença; mecanismo explicado no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01780
    {
        "id": "ECO-E2-L01780-1", "fonte_ref": "E2-L01780", "destino": "04-A", "subtema": H2["giffen"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_CONS,
        "rotulo_item": "Item",
        "assertiva": ("A curva de Engel para bens inferiores tem inclinação negativa, excetuando-se os bens de "
                      "Giffen, para os quais esta inclinação será positiva."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de Engel para bens inferiores tem inclinação negativa, ")
                   + vm("excetuando-se os bens de Giffen, para os quais esta inclinação será positiva") + az("."),
        "poucas": ("O " + azb("Giffen") + " é um bem inferior, não uma exceção a eles: sua curva de Engel também "
                   "é " + vd("negativa") + ". O que é positiva no Giffen é a curva de " + azb("demanda") + "."),
        "destrinchando": [
            "A inclinação da " + azb("curva de Engel") + " (q × renda) é a própria definição de bem normal × "
            "inferior. Dizer que um bem inferior tem Engel positiva é contradição em termos.",
            "Como " + vm("todo Giffen é inferior") + " (o efeito renda precisa ser oposto ao substituição), a "
            "Engel do Giffen é decrescente — em geral fortemente, já que o efeito renda tem de ser grande.",
            "A peculiaridade do Giffen está em outro gráfico: a " + azb("curva de demanda") + " (q × p) "
            "positivamente inclinada. O item transplanta essa peculiaridade para a Engel.",
            "Quadro de bolso: normal → Engel ↗, demanda ↘; inferior comum → Engel ↘, demanda ↘; Giffen → "
            "Engel ↘, demanda ↗.",
        ],
        "grafico_verso": "ECO-E2-L01522-1-V1",
        "dissecando": (cz("[troca de conceito · inversão]") + " A 1ª oração é correta; o erro está na exceção "
                       "inventada, que confunde as duas curvas. 🔥 A banca gosta de “excetuando-se o Giffen” "
                       "justamente porque o Giffen é exceção — mas à lei da demanda, não à inferioridade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de demanda dos bens inferiores é negativamente inclinada, excetuando-se os bens de "
            "Giffen, para os quais é positiva.”</i> → CERTO",
            "<i>“A curva de Engel dos bens de luxo é positivamente inclinada e côncava.”</i> → ERRADO "
            "(luxo: convexa)",
        ])],
        "reescrita": ("A curva de Engel para bens inferiores tem inclinação negativa, " + hl("inclusive para os "
                      "bens de Giffen, que são inferiores") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Giffen é subconjunto dos inferiores; sua Engel também é negativa; a confusão é com "
                            "a curva de demanda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 541", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (curvas de Engel de bens normais; descritas no 📖)"},
                          {"ref": "IMAGEM 542", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01522-1-V1, painel da Engel)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0810
    {
        "id": "ECO-E1-0810-1", "fonte_ref": "E1-0810", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": ("Considere um consumidor com função utilidade U = x₁x₂, em que x₁ e x₂ representam, "
                    "respectivamente, as quantidades consumidas dos bens 1 e 2. Considere, ainda, que o preço do "
                    "bem 1 seja p₁ = 10, o preço do bem 2 seja p₂ = 4, o rendimento do consumidor seja r = 80 e "
                    "que o consumidor seja racional, prefira mais a menos (monotonicidade) e gaste toda a sua "
                    "renda em x₁ e x₂. Com base nessas informações, e considerando que TMS seja a taxa marginal "
                    "de substituição, julgue os itens a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Se a renda do consumidor dobrar para r = 160, mantidos constantes p₁ e p₂, o novo consumo "
                      "ótimo será (x₁, x₂) = (8, 20), preservando-se as proporções consumidas entre os dois bens, "
                      "de modo a confirmar que as preferencias são homotéticas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a renda do consumidor dobrar para r = 160, mantidos constantes p₁ e p₂, o novo consumo "
                      "ótimo será <u>(x₁, x₂) = (8, 20)</u>, preservando-se as proporções consumidas entre os dois "
                      "bens, de modo a confirmar que as preferencias são <u>homotéticas</u>."),
        "poucas": ("Com U = x₁x₂ (" + azb("Cobb-Douglas") + "), gasta-se metade da renda em cada bem: x₁ = r/20 "
                   "e x₂ = r/8. Com r = 80, " + vd("(4, 10)") + "; com r = 160, " + vd("(8, 20)") + ". A razão "
                   "x₂/x₁ = 2,5 se mantém: preferências " + azb("homotéticas") + "."),
        "destrinchando": [
            "Ótimo interior: " + azb("TMS") + " = UMg₁/UMg₂ = x₂/x₁ igual à razão de preços p₁/p₂ = 10/4 = 2,5 → "
            + vd("x₂ = 2,5·x₁") + ". Na restrição 10x₁ + 4x₂ = r: 10x₁ + 10x₁ = r → " + vd("x₁ = r/20") + " e "
            + vd("x₂ = r/8") + ".",
            "Atalho da Cobb-Douglas U = x₁^a·x₂^b: a fração da renda gasta em cada bem é fixa, a/(a+b) e "
            "b/(a+b). Aqui, 50% e 50%: p₁x₁ = r/2 e p₂x₂ = r/2. Para r = 80: x₁ = 40/10 = 4 e x₂ = 40/4 = 10. "
            "Para r = 160: " + vd("x₁ = 8 e x₂ = 20") + ".",
            azb("Preferências homotéticas") + ": a TMS depende só da proporção x₂/x₁, não da escala. Com preços "
            "fixos, a " + azb("curva renda-consumo") + " é uma reta que sai da origem e as " + azb("curvas de "
            "Engel") + " também são retas pela origem: " + vd("elasticidade-renda = 1") + " para os dois bens.",
            "Consequência: nenhum bem é inferior nem de luxo; dobrar a renda dobra todas as quantidades. Toda "
            "Cobb-Douglas (e toda CES) é homotética; a quase-linear não é.",
            "Precisão conceitual: o ótimo calculado é <b>compatível</b> com homoteticidade; quem a garante é a "
            "forma funcional (U = x₁x₂ é homogênea de grau 2).",
        ],
        "grafico_verso": "ECO-E1-0810-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " Item de cálculo com conclusão conceitual. A banca "
                       "testa se o candidato acha o ótimo (TMS = p₁/p₂) e reconhece a homoteticidade da "
                       "Cobb-Douglas. O erro típico seria inverter os preços (x₁ = r/8) e chegar a (20, 8), ou "
                       "achar que “confirmar” exigiria mais pontos — para a Cobb-Douglas, basta a forma funcional."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com r = 80, o consumo ótimo é (x₁, x₂) = (10, 4).”</i> → ERRADO (preços invertidos: o ótimo é 4 e 10)",
            "<i>“No ótimo, a TMS é igual a 2,5.”</i> → CERTO",
            "<i>“Se p₁ cair para 5, o consumo de x₂ aumenta.”</i> → ERRADO (na Cobb-Douglas, x₂ = r ÷ 2p₂ não "
            "depende de p₁)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Só o gabarito (CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0188
    {
        "id": "ECO-E1-0188-1", "fonte_ref": "E1-0188", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2018", "ano": 2018, "cacd": False,
        "errei": True,
        "comando": "Acerca das preferências do consumidor e das curvas de indiferença, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Dependendo do formato da curva de indiferença de um consumidor para dois bens, um "
                      "deslocamento paralelo de sua restrição orçamentária para cima e para a direita poderá "
                      "provocar queda no consumo de um dos bens em questão."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Dependendo do formato</u> da curva de indiferença de um consumidor para dois bens, um "
                      "deslocamento paralelo de sua restrição orçamentária para cima e para a direita "
                      "<u>poderá</u> provocar queda no consumo de um dos bens em questão."),
        "poucas": ("Deslocamento paralelo para fora = " + azb("aumento de renda") + " com preços constantes. Se "
                   "as preferências fizerem de um dos bens um " + azb("bem inferior") + ", o consumo dele "
                   + vd("cai") + " quando a renda sobe."),
        "destrinchando": [
            "Restrição orçamentária p₁x₁ + p₂x₂ = R. Mudar R desloca a reta paralelamente (a inclinação −p₁/p₂ "
            "não muda); mudar um preço gira a reta. Logo, o item descreve um puro " + azb("choque de renda") + ".",
            "Ligando os ótimos para rendas crescentes obtém-se a " + azb("curva renda-consumo") + ". Se ela "
            "sobe para a direita, os dois bens são normais. Se ela se inclina para trás (ou para baixo), um dos "
            "bens é " + azb("inferior") + ": mais renda, menos consumo dele (ex.: carne de segunda, ônibus).",
            "É o formato do mapa de indiferença — as preferências — que decide onde ficam as tangências. Por "
            "isso o item diz “dependendo do formato”: com Cobb-Douglas (homotética) os dois bens sobem; com "
            "outros mapas, a nova tangência pode ficar à esquerda da antiga num dos eixos.",
            "Com só dois bens, no máximo um pode ser inferior: se os dois caíssem, a renda maior não seria "
            "gasta, contrariando a monotonicidade.",
            "Na " + azb("curva de Engel") + " do bem inferior, a inclinação é negativa no trecho relevante.",
        ],
        "dissecando": (cz("[modulador relativo · contraintuitivo]") + " “Dependendo do formato” e “poderá” "
                       "salvam o item: basta um caso possível (bem inferior). A intuição “mais renda = mais de "
                       "tudo” leva ao ERRADO. 🔥 O mesmo item foi reaproveitado pelo simulado Nidi/2026 (ver "
                       "ECO-E1-0836-1)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um deslocamento paralelo da restrição para cima e para a direita sempre provoca aumento no "
            "consumo de ambos os bens.”</i> → ERRADO (modulador absoluto: há bens inferiores)",
            "<i>“…poderá provocar queda no consumo de ambos os bens.”</i> → ERRADO (com dois bens e "
            "monotonicidade, ao menos um aumenta)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "CONTRAINTUITIVO"], "moduladores": ["dependendo", "poderá"],
        "dificuldade": 2,
        "comentario_fonte": "Vários comentários concordantes (inclusive citando Pindyck e Rubinfeld): basta que "
                            "um dos bens seja inferior; deslocamento paralelo = aumento de renda. Um comentário "
                            "atribuía o resultado a curvas de indiferença convexas “representarem” bem inferior.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (62).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"},
                          {"ref": "00034.jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"},
                          {"ref": "image (69).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"},
                          {"ref": "image (71).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": ["qualidade_fonte: um dos comentários diz que a convexidade da curva de indiferença "
                    "“representa” um bem inferior — falso (convexidade não define inferioridade); descartado",
                    "quase_duplicata: ECO-E1-0836-1 (Nidi/2026), mesma assertiva em prova diferente"],
    },
    # ------------------------------------------------------------------ E1-0836
    {
        "id": "ECO-E1-0836-1", "fonte_ref": "E1-0836", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Os agentes microeconômicos fazem suas escolhas de forma racional em um cenário de "
                    "informações completas e simetricamente distribuídas. A respeito da Teoria do Consumidor, "
                    "julgue certo ou errado (C ou E) os itens a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Dependendo do formato da curva de indiferença de um consumidor para dois bens, um "
                      "deslocamento paralelo de sua restrição orçamentária para cima e para a direita poderá "
                      "provocar queda no consumo de um dos bens."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Dependendo do formato da curva de indiferença de um consumidor para dois bens, um "
                      "<u>deslocamento paralelo</u> de sua restrição orçamentária para cima e para a direita "
                      "<u>poderá</u> provocar queda no consumo de um dos bens."),
        "poucas": ("Restrição que se desloca em paralelo = " + azb("mais renda") + ", preços iguais. Se um dos "
                   "bens for " + azb("inferior") + " para esse consumidor, seu consumo " + vd("diminui") + "."),
        "destrinchando": [
            "Paralelo = mesma inclinação −p₁/p₂ = preços relativos inalterados. Só a " + azb("renda") + " mudou; "
            "portanto não há efeito substituição, só efeito renda.",
            "A reação de cada bem à renda é a sua " + azb("elasticidade-renda") + ": positiva (normal) ou "
            "negativa (" + azb("inferior") + "). Quem decide o sinal são as preferências, isto é, o formato do "
            "mapa de curvas de indiferença.",
            "Graficamente: se a nova tangência fica à esquerda da antiga (para o bem do eixo horizontal), esse "
            "bem é inferior, e a " + azb("curva renda-consumo") + " se inclina para trás; a " + azb("curva de "
            "Engel") + " dele é decrescente.",
            "Limite lógico: com dois bens e renda toda gasta, não podem cair os dois ao mesmo tempo.",
        ],
        "dissecando": (cz("[modulador relativo]") + " Mesmo item de prova de 2018 (ver ECO-E1-0188-1), "
                       "reaproveitado pelo simulado. “Dependendo” e “poderá” pedem apenas um caso possível — o "
                       "bem inferior. O preâmbulo sobre informação completa é neutro para o julgamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um deslocamento paralelo da restrição para a direita, decorrente da queda do preço de um dos "
            "bens, …”</i> → ERRADO (troca de conceito: queda de preço gira a reta, não a desloca em paralelo)",
            "<i>“…poderá provocar queda no consumo de um dos bens, desde que esse bem seja inferior.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["dependendo", "poderá"], "dificuldade": 1,
        "comentario_fonte": "Deslocamento paralelo para fora = aumento de renda com preços constantes; se um bem "
                            "for inferior, o consumo dele cai.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0188-1 (prova de 2018), mesma assertiva"],
    },
    # ------------------------------------------------------------------ E1-0192
    {
        "id": "ECO-E1-0192-1", "fonte_ref": "E1-0192", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_QUEST_0422,
        "rotulo_item": "Item",
        "assertiva": ("As curvas de renda consumo indicam as combinações de consumo entre 2 bens que maximizam o "
                      "bem estar dos consumidores para aumentos no nível de renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As curvas de renda consumo indicam as combinações de consumo entre 2 bens que "
                      "<u>maximizam o bem estar</u> dos consumidores para <u>aumentos no nível de renda</u>."),
        "poucas": ("A " + azb("curva renda-consumo") + " liga as cestas ótimas (tangências) obtidas quando a renda "
                   "varia e os " + vd("preços ficam constantes") + "."),
        "destrinchando": [
            "Construção: fixe p₁ e p₂; desenhe restrições orçamentárias paralelas para rendas crescentes; marque "
            "em cada uma a tangência com a curva de indiferença mais alta (cesta que maximiza a utilidade); ligue "
            "os pontos. Esse caminho de expansão é a " + azb("curva renda-consumo") + ".",
            "Da renda-consumo se derivam as " + azb("curvas de Engel") + " (q de cada bem × renda). Inclinação "
            "positiva nos dois eixos → dois bens normais; curva que se dobra para trás ou para baixo → um bem "
            + azb("inferior") + ".",
            "Irmã: a " + azb("curva preço-consumo") + " liga os ótimos quando varia o <b>preço</b> de um bem "
            "(renda e outro preço fixos); dela sai a curva de demanda.",
            "Detalhe: “para aumentos” não restringe a curva — ela vale para quaisquer níveis de renda; o item só "
            "descreve o sentido em que normalmente se lê.",
            vm("Regra-âncora: renda varia → renda-consumo → Engel; preço varia → preço-consumo → demanda."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição de manual. O risco é a confusão com a curva "
                       "preço-consumo ou achar que a renda-consumo só existe para bens normais. Como o item não "
                       "fala em sinal, a definição geral basta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As curvas de renda-consumo indicam as combinações ótimas entre dois bens para variações no "
            "preço de um deles.”</i> → ERRADO (troca de conceito: é a preço-consumo)",
            "<i>“A curva renda-consumo é sempre positivamente inclinada.”</i> → ERRADO (com bem inferior, não)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Renda-consumo: combinações ótimas para diferentes rendas, preços constantes; com bem "
                            "inferior, inclinação negativa. Comentário com marcas de citação de chatbot.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0217
    {
        "id": "ECO-E1-0217-1", "fonte_ref": "E1-0217", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca da curva de Engel, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Curva de Engel é a função que relaciona a quantidade de equilíbrio adquirida de um dado bem "
                      "para um dado nível de renda monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Curva de Engel é a função que relaciona a quantidade de equilíbrio adquirida de um dado bem "
                      "para um dado nível de <u>renda monetária</u>."),
        "poucas": ("A " + azb("curva de Engel") + " dá, para cada nível de " + vd("renda") + " (preços "
                   "constantes), a quantidade ótima consumida de um bem."),
        "destrinchando": [
            "“Quantidade de equilíbrio” aqui = quantidade escolhida no ótimo do consumidor (tangência), não "
            "equilíbrio de mercado. Variando a renda, cada ótimo dá um ponto (R, q).",
            "Nome: " + oc("Ernst Engel") + ", estatístico alemão do século XIX, que observou que a fração da "
            "renda gasta com alimentação cai à medida que a renda sobe (" + azb("lei de Engel") + ").",
            "Formatos: crescente e côncava → " + azb("necessidade") + " (0 < η < 1); crescente e convexa → "
            + azb("luxo") + " (η > 1); decrescente → " + azb("inferior") + " (η < 0); reta pela origem → η = 1 "
            "(preferências homotéticas).",
            "A Engel se obtém da " + azb("curva renda-consumo") + " projetando-se as quantidades de cada bem; "
            "a curva de demanda, da preço-consumo.",
            "Mudança de preço <b>desloca</b> a curva de Engel (outro nível de q para cada renda); mudança de "
            "renda é movimento <b>ao longo</b> dela — o espelho do que ocorre com a curva de demanda.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição direta. O item poderia confundir quem associa "
                       "“equilíbrio” a preço de mercado, mas a variável independente é a renda, o que basta "
                       "para a Engel."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Curva de Engel é a função que relaciona a quantidade adquirida de um bem com o seu preço.”</i> → "
            "ERRADO (troca de conceito: é a curva de demanda)",
            "<i>“Pela lei de Engel, a proporção da renda gasta com alimentos aumenta com a renda.”</i> → ERRADO "
            "(diminui)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Engel: renda × quantidade com preços constantes; identifica normal (positiva) e "
                            "inferior (negativa).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (51).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01383
    {
        "id": "ECO-E2-L01383-1", "fonte_ref": "E2-L01383", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "ACEP", "prova": "BNB/Economista/2006", "ano": 2006, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à teoria do consumidor (questão adaptada).",
        "rotulo_item": "Item",
        "assertiva": "As curvas de Engel relacionam quantidade consumida com o nível de preço.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As curvas de Engel relacionam quantidade consumida com o ") + vm("nível de preço") + az("."),
        "poucas": ("As " + azb("curvas de Engel") + " relacionam quantidade consumida e " + vd("renda") + ", "
                   "com preços constantes. Quantidade × preço é a curva de " + azb("demanda") + "."),
        "destrinchando": [
            "Família de curvas da teoria do consumidor, pelo que varia: <b>renda</b> → curva renda-consumo "
            "(no espaço dos bens) e " + azb("curva de Engel") + " (q × R); <b>preço</b> de um bem → curva "
            "preço-consumo e " + azb("curva de demanda") + " (q × p).",
            "A Engel classifica os bens pela " + azb("elasticidade-renda") + ": inclinação positiva → normal "
            "(côncava: necessidade; convexa: luxo); negativa → inferior.",
            "“Nível de preço”, além disso, sugere nível geral de preços (inflação), outro conceito; mesmo lido "
            "como preço do bem, o item descreve a demanda.",
            vm("Regra-âncora: Engel = renda; demanda = preço."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca a variável independente da Engel pela da demanda. "
                       "Item curto, de definição, que só exige não confundir as duas curvas derivadas do "
                       "consumidor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As curvas de Engel relacionam quantidade consumida com o nível de renda, mantidos os preços "
            "constantes.”</i> → CERTO",
        ])],
        "reescrita": ("As curvas de Engel relacionam quantidade consumida com o " + hl("nível de renda") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Relacionam renda e consumo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 268", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (ilustração decorativa, repetida)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01618
    {
        "id": "ECO-E2-L01618-1", "fonte_ref": "E2-L01618", "destino": "04-A", "subtema": H2["engel"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "A respeito da teoria do consumidor, julgue as afirmações a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Os bens inferiores tem curva de Engel negativamente inclinada, enquanto para os bens normais "
                      "a inclinação é positiva."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os bens inferiores tem curva de Engel <u>negativamente</u> inclinada, enquanto para os bens "
                      "normais a inclinação é <u>positiva</u>."),
        "poucas": ("A inclinação da " + azb("curva de Engel") + " é o sinal da " + azb("elasticidade-renda")
                   + ": negativa no " + vd("inferior") + " (renda ↑ → q ↓), positiva no " + vd("normal") + "."),
        "destrinchando": [
            "Curva de Engel: q do bem no eixo vertical, renda no horizontal (convenção mais comum; alguns livros "
            "invertem os eixos, o que não muda o sinal da inclinação).",
            azb("Bem normal") + " (η > 0): curva crescente. Se côncava, " + azb("necessidade") + " (0 < η < 1: "
            "alimentos básicos em geral); se convexa, " + azb("luxo") + " (η > 1: viagens, joias).",
            azb("Bem inferior") + " (η < 0): curva decrescente — a pessoa troca o bem por versões melhores "
            "quando enriquece (carne de segunda, transporte coletivo em certas faixas de renda).",
            "Um mesmo bem pode mudar de classe ao longo da renda: normal para quem é muito pobre e inferior "
            "depois de certo nível — a Engel sobe e depois desce. A classificação vale no trecho considerado.",
        ],
        "grafico_verso": "ECO-E2-L01618-1-V1",
        "dissecando": (cz("[literalidade]") + " Definição direta, sem pegadinha de redação. A banca costuma "
                       "trocar o par por demanda × Engel (ver os itens sobre Giffen) ou por côncava × convexa "
                       "(necessidade × luxo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os bens de luxo têm curva de Engel côncava.”</i> → ERRADO (convexa: q cresce mais que a renda)",
            "<i>“Os bens de Giffen têm curva de Engel positivamente inclinada.”</i> → ERRADO (são inferiores: "
            "negativa)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Normal: Engel positiva; inferior: negativa (elasticidade-renda negativa).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 459", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01618-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0193
    {
        "id": "ECO-E1-0193-1", "fonte_ref": "E1-0193", "destino": "04-A", "subtema": H2["ers"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_QUEST_0422,
        "rotulo_item": "Item",
        "assertiva": ("Dado o aumento no preço do bem A, a redução na demanda por esse bem é resultado dos efeitos "
                      "renda e efeito substituição, onde o efeito renda sempre será superior ao efeito "
                      "substituição."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Dado o aumento no preço do bem A, a redução na demanda por esse bem é resultado dos efeitos "
                      "renda e efeito substituição, ") + vm("onde o efeito renda sempre será superior ao efeito "
                                                            "substituição") + az("."),
        "poucas": ("A decomposição em " + azb("efeito substituição") + " + " + azb("efeito renda") + " está certa; "
                   "não existe regra de que o renda " + vd("sempre") + " supere o substituição — isso só ocorre "
                   "em casos particulares."),
        "destrinchando": [
            "Pela " + azb("equação de Slutsky") + ", <b>todo</b> o efeito de uma variação de preço sobre a "
            "quantidade demandada (efeito total) se divide em substituição (mudança de preços relativos, poder "
            "de compra compensado) e renda (mudança do poder de compra). A primeira parte do item é exata.",
            "Tamanho relativo: depende do bem. O substituição é grande quando há bons substitutos; o renda é "
            "grande quando o bem pesa muito no orçamento (efeito ≈ participação no gasto × elasticidade-renda). "
            "Para a maioria dos bens, que têm peso pequeno, o " + vd("substituição predomina") + ".",
            "Bem normal: os dois reduzem q, e a queda ocorre seja qual for o maior. Bem inferior: o renda se "
            "opõe; se ele fosse sempre maior, todo inferior seria " + azb("Giffen") + " e a quantidade "
            "<b>aumentaria</b> — o que contradiz a própria “redução na demanda” do item.",
            vm("Regra-âncora: substituição sempre na direção oposta ao preço; renda depende de normal × "
               "inferior; tamanho relativo depende do bem."),
        ],
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " Começa com a decomposição correta e enxerta "
                       "um ranking universal (“sempre será superior”). Pista: não há bem especificado — sem saber "
                       "se A é normal ou inferior, nenhum “sempre” sobre o tamanho dos efeitos se sustenta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Dado o aumento no preço de um bem normal, os efeitos renda e substituição atuam no mesmo "
            "sentido, reduzindo a quantidade demandada.”</i> → CERTO",
            "<i>“O efeito substituição sempre atua no sentido oposto ao da variação do preço.”</i> → CERTO",
        ])],
        "reescrita": ("Dado o aumento no preço do bem A, a redução na demanda por esse bem é resultado dos efeitos "
                      "renda e efeito substituição, " + hl("sem que o efeito renda seja necessariamente superior")
                      + " ao efeito substituição."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Resposta de IA: o efeito renda não é sempre superior; afirmava também, sem razão, que "
                            "a redução da demanda não resulta apenas dos efeitos renda e substituição.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a fonte afirmava que a redução da demanda dependeria de “outros fatores” "
                    "além dos efeitos renda e substituição (elasticidade, substitutos etc.) — a decomposição de "
                    "Slutsky é exaustiva; trecho descartado"],
    },
    # ------------------------------------------------------------------ E1-0199
    {
        "id": "ECO-E1-0199-1", "fonte_ref": "E1-0199", "destino": "04-A", "subtema": H2["ers"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos renda e substituição, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Se dois bens A e B são complementares perfeitos e o preço do bem A cresce, então o Efeito "
                      "substituição é nulo e o Efeito Total é igual ao Efeito renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se dois bens A e B são <u>complementares perfeitos</u> e o preço do bem A cresce, então o "
                      "Efeito substituição é <u>nulo</u> e o Efeito Total é igual ao Efeito renda."),
        "poucas": ("Com " + azb("complementares perfeitos") + " (curvas de indiferença em L), o consumidor nunca "
                   "troca um bem pelo outro: o efeito substituição é " + vd("zero") + " e toda a variação vem do "
                   + azb("efeito renda") + "."),
        "destrinchando": [
            "Preferências de " + azb("Leontief") + ": U = min{aA, bB} (sapato esquerdo e direito; café e açúcar "
            "em proporção fixa). A cesta ótima está sempre no vértice do L, na proporção fixa, qualquer que seja "
            "a razão de preços.",
            "Efeito substituição (Slutsky ou Hicks): gira-se a restrição em torno da cesta inicial (ou da curva "
            "de indiferença inicial) com os novos preços. No vértice do L, a nova tangência é o <b>mesmo "
            "ponto</b>: Δq = " + vd("0") + ".",
            "Efeito renda: o aumento de p<sub>A</sub> reduz o poder de compra; o consumidor desce para um L mais "
            "baixo e reduz A e B na mesma proporção. Efeito total = efeito renda.",
            "Contraste com " + azb("substitutos perfeitos") + " (isoquantas/indiferença retas): o efeito "
            "substituição é máximo — o consumidor pode migrar inteiramente para o outro bem.",
            vm("Regra-âncora: L → ES = 0; reta → ES máximo (solução de canto)."),
        ],
        "dissecando": (cz("[literalidade]") + " Resultado-padrão de manual. O item tenta assustar com a ideia de "
                       "que “sempre há efeito substituição”; nos complementares perfeitos não há, porque a "
                       "proporção de consumo é fixa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se A e B são substitutos perfeitos, o efeito substituição de um aumento de p<sub>A</sub> é "
            "nulo.”</i> → ERRADO (troca de conceito: é nos complementares perfeitos)",
            "<i>“Com complementares perfeitos, o aumento de p<sub>A</sub> reduz também o consumo de B.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO, com imagem não preservada e link para t.me/cacdeconomia/18.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (49).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0631
    {
        "id": "ECO-E1-0631-1", "fonte_ref": "E1-0631", "destino": "04-A", "subtema": H2["ers"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Set/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos renda e substituição, julgue o item a seguir.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("O efeito substituição é a modificação no consumo de um bem associada a uma variação em seu "
                      "preço, mantendo-se constante o nível de utilidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O efeito substituição é a modificação no consumo de um bem associada a uma variação em seu "
                      "preço, mantendo-se constante o <u>nível de utilidade</u>."),
        "poucas": ("É a definição de " + azb("efeito substituição") + " no sentido de " + oc("Hicks") + ": "
                   "variação de q causada só pela mudança de preço relativo, sobre a " + vd("mesma curva de "
                   "indiferença") + "."),
        "destrinchando": [
            "A variação de preço faz duas coisas: altera o preço relativo e altera o poder de compra. Para "
            "isolar a primeira, compensa-se a renda do consumidor.",
            "Compensação de " + oc("Hicks") + ": dá-se renda suficiente para manter a " + vd("utilidade") + " "
            "inicial (o consumidor desliza sobre a mesma curva de indiferença). Compensação de " + oc("Slutsky")
            + ": dá-se renda para que ele possa comprar a " + vd("cesta inicial") + " (poder de compra "
            "constante). Para variações pequenas, os dois coincidem.",
            "Propriedade: o efeito substituição é sempre de sinal oposto à variação do preço (ou nulo, nos "
            "complementares perfeitos), por causa da convexidade das curvas de indiferença.",
            "O restante da variação de q é o " + azb("efeito renda") + ": mudança de consumo pelo poder de compra, "
            "com preços relativos constantes.",
            "A redação é a de " + oc("Pindyck e Rubinfeld") + " (<i>Microeconomia</i>), que a ilustram com "
            "vestuário e alimento.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. O que a banca pode trocar é o que fica "
                       "constante: utilidade (Hicks) × poder de compra da cesta inicial (Slutsky) × renda nominal "
                       "(efeito total, demanda marshalliana)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O efeito substituição é a modificação no consumo de um bem associada à variação do poder "
            "aquisitivo, mantendo-se constantes os preços relativos.”</i> → ERRADO (troca de conceito: é o efeito "
            "renda)",
            "<i>“O efeito substituição é a modificação no consumo associada à variação do preço, mantendo-se "
            "constante a renda nominal.”</i> → ERRADO (isso é o efeito total)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Certo: o efeito substituição é a modificação no consumo de um bem associada a uma "
                            "variação em seu preço, mantendo-se constante o nível de utilidade (renda).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (194).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto reconstruído pelo comentário"}],
        "alertas": ["texto_reconstruido: frente original era só imagem (image (194).png); assertiva reconstruída "
                    "a partir do comentário “Certo: …”, que reproduz a definição de Pindyck e Rubinfeld; o "
                    "parêntese “(renda)” do comentário foi omitido por ambíguo — conferir com a imagem"],
    },
    # ------------------------------------------------------------------ E2-L00335
    {
        "id": "ECO-E2-L00335-1", "fonte_ref": "E2-L00335", "destino": "04-A", "subtema": H2["ers"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Para um agente que é poupador líquido no primeiro período, um aumento na taxa de juros real "
                      "gera um efeito renda que incentiva o aumento do consumo presente, opondo-se ao efeito "
                      "substituição, o que torna o efeito final sobre a poupança ambíguo sem o conhecimento das "
                      "preferências específicas do agente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para um agente que é <u>poupador líquido</u> no primeiro período, um aumento na taxa de "
                      "juros real gera um efeito renda que incentiva o aumento do consumo presente, opondo-se ao "
                      "efeito substituição, o que torna o efeito final sobre a poupança <u>ambíguo</u> sem o "
                      "conhecimento das preferências específicas do agente."),
        "poucas": ("Juros maiores encarecem o consumo presente (" + azb("efeito substituição") + ": poupar mais), "
                   "mas enriquecem o " + azb("poupador") + " (" + azb("efeito renda") + ": consumir mais hoje). "
                   "Sinais opostos → efeito sobre a poupança " + vd("ambíguo") + "."),
        "destrinchando": [
            "Modelo de dois períodos de " + oc("Irving Fisher") + ": restrição intertemporal "
            + vd("C₁ + C₂/(1+r) = Y₁ + Y₂/(1+r)") + ". O “preço” do consumo presente, em unidades de consumo "
            "futuro, é " + vd("(1 + r)") + ": a reta orçamentária gira em torno do ponto de dotação (Y₁, Y₂) "
            "quando r muda.",
            azb("Efeito substituição") + ": r ↑ → C₁ fica relativamente mais caro → C₁ ↓ e poupança ↑. Vale "
            "para todos.",
            azb("Efeito renda") + ": depende da posição do agente. " + azb("Poupador") + " (C₁ < Y₁) empresta "
            "ao mercado e ganha com juros maiores → fica mais rico → com C₁ e C₂ normais, C₁ ↑ e poupança ↓. "
            + azb("Tomador") + " (C₁ > Y₁) paga mais juros → fica mais pobre → C₁ ↓; aí os dois efeitos se "
            "somam e a poupança sobe sem ambiguidade.",
            "Como para o poupador os efeitos se opõem, o resultado depende das preferências (em especial da "
            + azb("elasticidade de substituição intertemporal") + "): se alta, domina a substituição e a poupança "
            "sobe; se baixa, domina a renda e a poupança pode cair. A curva de oferta de poupança pode até se "
            "curvar para trás.",
            "Paralelo útil: é o mesmo dilema da oferta de trabalho (salário ↑: substituição → mais trabalho; "
            "renda → mais lazer).",
            vm("Regra-âncora: r ↑ — tomador: poupança sobe (efeitos somam); poupador: ambíguo (efeitos opostos)."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item correto e longo, cujo risco é a condição "
                       "“poupador líquido”: se fosse tomador, a ambiguidade desapareceria. Quem decora “juros "
                       "maiores → mais poupança” (só substituição) marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para um agente tomador líquido no primeiro período, um aumento na taxa de juros real torna "
            "ambíguo o efeito sobre o consumo presente.”</i> → ERRADO (troca de ator: para o tomador, os dois "
            "efeitos reduzem C₁)",
            "<i>“Um aumento da taxa de juros real eleva necessariamente a poupança do poupador líquido.”</i> → "
            "ERRADO (modulador absoluto: o efeito é ambíguo)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["sem o conhecimento"], "dificuldade": 2,
        "comentario_fonte": "Várias respostas de IA concordantes (modelo de Fisher, restrição intertemporal, "
                            "efeitos substituição e renda opostos para o poupador, resultado ambíguo).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 046", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (restrição intertemporal no 📖)"},
                          {"ref": "IMAGEM 047", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00602
    {
        "id": "ECO-E2-L00602-1", "fonte_ref": "E2-L00602", "destino": "04-A", "subtema": H2["ers"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("A decomposição do impacto de uma variação de preço sobre a quantidade demandada mostra que o "
                      "efeito renda e o efeito substituição sempre atuam na mesma direção, ou seja, ambos "
                      "contribuem para reduzir o consumo quando o preço de um bem aumenta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A decomposição do impacto de uma variação de preço sobre a quantidade demandada mostra que o "
                      "efeito renda e o efeito substituição ") + vm("sempre") + az(" atuam na mesma direção, ou "
                      "seja, ambos contribuem para reduzir o consumo quando o preço de um bem aumenta."),
        "poucas": ("Só nos " + azb("bens normais") + " os dois efeitos se somam. Nos " + azb("bens inferiores")
                   + ", o efeito renda atua em " + vd("sentido oposto") + " ao substituição."),
        "destrinchando": [
            "Alta de preço → " + azb("efeito substituição") + ": o bem ficou relativamente mais caro, o "
            "consumidor o troca por outros → q ↓. Isso vale para <b>todo</b> bem (com curvas de indiferença "
            "convexas).",
            azb("Efeito renda") + ": o consumidor ficou mais pobre em termos reais. Bem normal → compra menos "
            "(q ↓, reforça). Bem inferior → compra <b>mais</b> (q ↑, contraria).",
            "Por isso a curva de demanda de um bem normal é sempre decrescente, enquanto a de um inferior só é "
            "decrescente se o substituição vencer; se o renda vencer, surge o " + azb("Giffen") + ".",
            vm("Regra-âncora: normal → efeitos somam; inferior → efeitos se opõem."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " O item descreve corretamente o bem normal e o generaliza "
                       "com “sempre”. Pista: a decomposição de Slutsky existe justamente para mostrar que os "
                       "efeitos <b>podem</b> se opor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para bens normais, o efeito renda e o efeito substituição atuam na mesma direção.”</i> → CERTO",
            "<i>“Para bens inferiores, o efeito substituição de um aumento de preço eleva o consumo.”</i> → ERRADO "
            "(o substituição sempre reduz; é o renda que eleva)",
        ])],
        "reescrita": ("A decomposição do impacto de uma variação de preço sobre a quantidade demandada mostra que o "
                      "efeito renda e o efeito substituição " + hl("só") + " atuam na mesma direção " + hl("nos "
                      "bens normais") + ", ou seja, ambos contribuem para reduzir o consumo quando o preço de um "
                      "bem " + hl("normal") + " aumenta."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Verdade para bens normais; nos inferiores, os efeitos atuam em direções opostas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00617
    {
        "id": "ECO-E2-L00617-1", "fonte_ref": "E2-L00617", "destino": "04-A", "subtema": H2["ers"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("Para um bem normal, um aumento de preço provoca um efeito renda que se contrapõe ao efeito "
                      "substituição, pois a redução do poder de compra leva a um aumento do consumo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para um bem normal, um aumento de preço provoca um efeito renda que ")
                   + vm("se contrapõe ao") + az(" efeito substituição, pois a redução do poder de compra leva a ")
                   + vm("um aumento") + az(" do consumo."),
        "poucas": ("No " + azb("bem normal") + ", menos poder de compra = " + vd("menos consumo") + ": o efeito "
                   "renda " + azb("reforça") + " o substituição. A descrição do item é a do bem inferior."),
        "destrinchando": [
            azb("Bem normal") + ": elasticidade-renda positiva — renda real ↓ → consumo ↓. A alta de preço reduz "
            "q pelos dois canais: substituição (bem relativamente mais caro) e renda (consumidor mais pobre).",
            "A frase “a redução do poder de compra leva a um aumento do consumo” define o " + azb("bem inferior")
            + " (elasticidade-renda negativa); só nele o renda se contrapõe ao substituição.",
            "Consequência: a demanda de um bem normal é necessariamente decrescente (lei da demanda garantida); "
            "a de um inferior, em regra também, salvo no " + azb("Giffen") + ".",
            vm("Regra-âncora: normal → renda reforça; inferior → renda contraria."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Atribui ao bem normal o mecanismo do inferior. "
                       "A justificativa (“pois…”) é coerente com a conclusão, o que dá aparência de raciocínio; "
                       "o teste é a premissa: o que um bem normal faz quando a renda cai?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para um bem inferior, um aumento de preço provoca um efeito renda que se contrapõe ao efeito "
            "substituição.”</i> → CERTO",
        ])],
        "reescrita": ("Para um bem normal, um aumento de preço provoca um efeito renda que " + hl("reforça o")
                      + " efeito substituição, pois a redução do poder de compra leva a " + hl("uma redução")
                      + " do consumo."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Para bem normal, os dois efeitos reduzem o consumo e se reforçam.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00870
    {
        "id": "ECO-E2-L00870-1", "fonte_ref": "E2-L00870", "destino": "04-A", "subtema": H2["ers"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação aos diferentes tipos de bens, julgue (C ou E) os itens que se seguem.",
        "rotulo_item": "Item",
        "assertiva": ("Suponha que um indivíduo consuma apenas dois bens, sendo o primeiro um bem normal e o "
                      "segundo, um bem inferior. Nessa situação, caso haja um aumento de preço do bem normal, o "
                      "consumo do bem inferior aumentará em decorrência do efeito-renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Suponha que um indivíduo consuma apenas dois bens, sendo o primeiro um bem normal e o "
                      "segundo, um bem inferior. Nessa situação, caso haja um aumento de preço do bem normal, o "
                      "consumo do bem inferior aumentará <u>em decorrência do efeito-renda</u>."),
        "poucas": ("O aumento do preço do bem normal " + azb("reduz a renda real") + "; como o segundo bem é "
                   + azb("inferior") + ", o efeito-renda " + vd("eleva") + " o consumo dele."),
        "destrinchando": [
            "O efeito-renda de uma variação de preço atinge <b>todos</b> os bens da cesta, não só o que "
            "encareceu: ao subir p₁, o consumidor fica mais pobre e revê o consumo de tudo conforme a "
            + azb("elasticidade-renda") + " de cada bem.",
            "Bem inferior (η < 0): renda real ↓ → consumo ↑. Daí o item: o efeito-renda da alta de p₁ faz subir "
            "o consumo do bem 2.",
            "O efeito substituição sobre o bem 2 vai no mesmo sentido: com dois bens, eles são necessariamente "
            + azb("substitutos líquidos") + " (de Hicks), e o encarecimento do bem 1 desloca consumo para o 2. "
            "Assim, o consumo do bem inferior sobe por <b>ambos</b> os canais.",
            "O item, contudo, só afirma o efeito-renda, e isso basta: a pergunta é sobre o canal, não sobre o "
            "efeito total.",
            vm("Regra-âncora: o efeito-renda de um preço vale para toda a cesta; o sinal depende de cada bem."),
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " Muitos associam “efeito-renda” só ao bem cujo preço "
                       "mudou e marcam ERRADO. O item cobra o efeito cruzado: a alta de um preço é uma perda de "
                       "renda real que afeta também o outro bem, e o sinal se lê pela inferioridade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…caso haja um aumento de preço do bem normal, o consumo do bem inferior diminuirá em "
            "decorrência do efeito-renda.”</i> → ERRADO (inversão: inferior sobe quando a renda real cai)",
            "<i>“Com apenas dois bens, ambos podem ser inferiores.”</i> → ERRADO (a renda adicional teria de ser "
            "gasta em algum deles)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Aumento do preço do bem normal reduz a renda real; bem inferior tem demanda que sobe "
                            "quando a renda cai.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01423
    {
        "id": "ECO-E2-L01423-1", "fonte_ref": "E2-L01423", "destino": "04-A", "subtema": H2["pc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_MICRO2,
        "rotulo_item": "Item",
        "assertiva": ("O aumento do preço do gás de cozinha, supondo que os consumidores comprem apenas gás e "
                      "feijão, e que estes são bens complementares, leva a uma mudança da inclinação da restrição "
                      "orçamentária e à redução do consumo de gás e aumento do consumo de feijão."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento do preço do gás de cozinha, supondo que os consumidores comprem apenas gás e "
                      "feijão, e que estes são bens complementares, leva a uma mudança da inclinação da restrição "
                      "orçamentária e à redução do consumo de gás e ") + vm("aumento do consumo de feijão")
                   + az("."),
        "poucas": ("Se gás e feijão são " + azb("complementares") + ", encarecer o gás reduz o consumo " + vd("dos "
                   "dois") + ". Aumento do feijão só ocorreria se fossem substitutos."),
        "destrinchando": [
            "Mudança de um preço <b>gira</b> a restrição orçamentária em torno do intercepto do outro bem: com "
            "gás no eixo horizontal, o intercepto R/p<sub>gás</sub> recua e a reta fica mais inclinada. Essa "
            "parte do item está correta.",
            azb("Complementares") + " (consumidos juntos — feijão precisa de gás para cozinhar): "
            + vd("elasticidade-preço cruzada negativa") + ". p<sub>gás</sub> ↑ → q<sub>gás</sub> ↓ → "
            "q<sub>feijão</sub> ↓. " + azb("Substitutos") + ": cruzada positiva, e o outro bem aumentaria.",
            "Ligando as cestas ótimas para diferentes p<sub>gás</sub> obtém-se a " + azb("curva preço-consumo")
            + ". Com complementares, ela tem inclinação positiva: quando o gás encarece, o consumidor recua nos "
            "dois eixos ao mesmo tempo. Com substitutos, tem inclinação negativa.",
            "Leitura por Slutsky: o efeito renda da alta do gás reduz o feijão (bem normal); com "
            "complementaridade forte, ele prevalece sobre qualquer substituição entre os dois.",
            vm("Regra-âncora: complementar → caem juntos; substituto → um cai, o outro sobe."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Duas primeiras consequências corretas "
                       "(inclinação muda, gás cai) e a terceira com o comportamento de substitutos. O item até "
                       "declara a relação (“complementares”) — o erro é contradição interna."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…leva a um deslocamento paralelo da restrição orçamentária…”</i> → ERRADO (troca de conceito: "
            "deslocamento paralelo é variação de renda)",
            "<i>“…supondo que estes sejam bens substitutos, leva à redução do consumo de gás e ao aumento do "
            "consumo de feijão.”</i> → CERTO",
        ])],
        "reescrita": ("O aumento do preço do gás de cozinha, supondo que os consumidores comprem apenas gás e "
                      "feijão, e que estes são bens complementares, leva a uma mudança da inclinação da restrição "
                      "orçamentária e à redução do consumo de gás e " + hl("também do consumo de feijão") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Três comentários concordantes: complementares têm demanda conjunta; a alta do gás "
                            "reduz o consumo dos dois; a inclinação da restrição muda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0216
    {
        "id": "ECO-E1-0216-1", "fonte_ref": "E1-0216", "destino": "04-A", "subtema": H2["slutsky"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca das funções de demanda do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na função Hicksiana ou Compensada a quantidade demandada é função do preço e do nível de "
                      "utilidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na função Hicksiana ou Compensada a quantidade demandada é função do preço e do "
                      "<u>nível de utilidade</u>."),
        "poucas": ("A " + azb("demanda hicksiana") + " h(p, U) sai da " + azb("minimização do gasto") + " para "
                   "atingir uma utilidade U dada: depende dos " + vd("preços e da utilidade") + ", não da renda."),
        "destrinchando": [
            azb("Demanda marshalliana") + " (ou ordinária) x(p, R): maximiza a utilidade dada a renda R. "
            "Argumentos: preços e " + vd("renda") + ".",
            azb("Demanda hicksiana") + " (ou compensada) h(p, U): minimiza o gasto p·x para alcançar a utilidade "
            "U. Argumentos: preços e " + vd("utilidade") + ". Variando p, a renda é “compensada” para manter o "
            "consumidor na mesma curva de indiferença.",
            "Dualidade: h(p, U) = x(p, e(p, U)), em que e(p, U) é a " + azb("função gasto") + "; e x(p, R) = "
            "h(p, v(p, R)), com v a " + azb("utilidade indireta") + ". Pelo " + azb("lema de Shephard") + ", "
            "∂e/∂p<sub>i</sub> = h<sub>i</sub>.",
            "Como só capta o efeito substituição, a hicksiana é sempre " + vd("não crescente") + " no próprio "
            "preço — mesmo para bens de Giffen. A diferença entre as inclinações das duas curvas é o efeito "
            "renda (equação de " + oc("Slutsky") + ").",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. A troca típica da banca é “preço e renda” "
                       "(marshalliana) no lugar de “preço e utilidade” (hicksiana), ou atribuir à hicksiana o "
                       "efeito renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na função de demanda hicksiana, a quantidade demandada é função dos preços e da renda "
            "monetária.”</i> → ERRADO (troca de conceito: é a marshalliana)",
            "<i>“A curva de demanda compensada de um bem de Giffen é positivamente inclinada.”</i> → ERRADO "
            "(a compensada é sempre não crescente)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Hicksiana: quantidade demandada quando os preços variam e a renda é compensada para "
                            "manter a utilidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01524
    {
        "id": "ECO-E2-L01524-1", "fonte_ref": "E2-L01524", "destino": "04-A", "subtema": H2["slutsky"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CONS,
        "rotulo_item": "Item",
        "assertiva": ("A equação de Slutsky mostra a decomposição do efeito preço total em efeito renda e efeito "
                      "substituição. Para um bem inferior, os efeitos renda e substituição sempre terão sinais "
                      "opostos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A equação de Slutsky mostra a decomposição do efeito preço total em efeito renda e efeito "
                      "substituição. Para um bem inferior, os efeitos renda e substituição <u>sempre</u> terão "
                      "sinais opostos."),
        "poucas": ("Pela " + azb("equação de Slutsky") + ", o efeito substituição é sempre de sinal contrário ao "
                   "preço; no " + azb("bem inferior") + ", o efeito renda tem o sinal oposto ao do substituição. "
                   "Aqui o “sempre” é " + vd("verdadeiro") + "."),
        "destrinchando": [
            "Equação: " + vd("∂x/∂p = ∂h/∂p − x·∂x/∂R") + ". Efeito total = efeito substituição (∂h/∂p ≤ 0) + "
            "efeito renda (−x·∂x/∂R).",
            "Bem inferior ⇔ ∂x/∂R < 0 ⇔ termo renda > 0. Como o substituição é ≤ 0, os sinais são "
            "<b>sempre</b> opostos — é a própria definição de inferioridade aplicada à decomposição.",
            "O que <b>não</b> é fixo é o tamanho: se o substituição vencer, inferior comum (demanda "
            "decrescente); se o renda vencer, " + azb("Giffen") + " (demanda crescente).",
            "Bem normal: termo renda < 0, mesmo sinal do substituição; o efeito total é inequivocamente "
            "negativo.",
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Item CERTO com “sempre” — o modulador "
                       "absoluto aqui é legítimo, porque decorre da definição. Treina a não marcar ERRADO por "
                       "reflexo: o “sempre” é falso quando se fala de <b>tamanho</b> (quem domina), não de "
                       "<b>sinal</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para um bem inferior, o efeito renda sempre supera o efeito substituição.”</i> → ERRADO "
            "(modulador absoluto: só no Giffen)",
            "<i>“Para um bem normal, os efeitos renda e substituição sempre terão sinais opostos.”</i> → ERRADO "
            "(têm o mesmo sinal)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["sempre"], "dificuldade": 2,
        "comentario_fonte": "Slutsky: ES sempre não positivo; ER positivo para inferiores; sinais opostos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01781
    {
        "id": "ECO-E2-L01781-1", "fonte_ref": "E2-L01781", "destino": "04-A", "subtema": H2["slutsky"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_CONS,
        "rotulo_item": "Item",
        "assertiva": ("A equação de Slutsky mostra a separação entre efeito renda e efeito substituição. No caso de "
                      "bens normais, ambos efeitos vão na mesma direção, porém no caso dos bens inferiores, estes "
                      "efeitos terão sinais contrários, porém com predomínio do efeito substituição."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A equação de Slutsky mostra a separação entre efeito renda e efeito substituição. No caso de "
                      "bens normais, ambos efeitos vão na mesma direção, porém no caso dos bens inferiores, estes "
                      "efeitos terão sinais contrários, porém <u>com predomínio do efeito substituição</u>."),
        "poucas": ("Normal: efeitos no " + azb("mesmo sentido") + "; inferior: " + azb("sentidos opostos")
                   + ", e, no caso típico, o " + vd("substituição predomina") + " (a exceção é o Giffen). A banca "
                   "leu o item pelo caso típico."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o predomínio do efeito substituição não vale para <b>todo</b> bem inferior: nos bens "
                          "de " + azb("Giffen") + " (que são inferiores) predomina o efeito renda. O item, sem "
                          "ressalva, generaliza o caso típico; a leitura mais rigorosa daria ERRADO, como em itens "
                          "do tipo “se o bem é inferior, sua demanda será necessariamente…”. O gabarito da fonte "
                          "(CERTO) foi mantido por tratar do inferior comum, que é a regra.")],
        "destrinchando": [
            azb("Slutsky") + ": efeito total = substituição (sempre contrário ao preço) + renda (sinal dado pela "
            "elasticidade-renda).",
            "Bem normal: renda real ↓ (preço ↑) → q ↓ pelos dois canais. Bem inferior: renda real ↓ → q ↑, "
            "contra o substituição.",
            "Inferior comum: substituição > renda → a demanda continua decrescente, só que menos elástica que a "
            "de um normal equivalente. Inferior de " + azb("Giffen") + ": renda > substituição → demanda "
            "crescente.",
            "Por que o caso típico é o predomínio do substituição: o efeito renda é proporcional ao peso do bem "
            "no orçamento (x·∂x/∂R), em geral pequeno; Giffen exige bem muito inferior <b>e</b> de grande peso "
            "na cesta.",
            vm("Regra-âncora: inferior → sinais opostos sempre; quem domina, só em regra (o substituição)."),
        ],
        "dissecando": (cz("[meia-verdade · detalhe]") + " Duas primeiras orações irretocáveis; a última "
                       "acrescenta o predomínio do substituição sem o “em regra”. Em prova CEBRASPE, compare com "
                       "o enunciado: se o item fala de “todo” ou “necessariamente”, o Giffen derruba; se descreve "
                       "o comportamento usual, tende a ser CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…no caso dos bens inferiores, estes efeitos terão sinais contrários, podendo predominar "
            "qualquer um deles.”</i> → CERTO",
            "<i>“…no caso dos bens inferiores, estes efeitos terão o mesmo sinal.”</i> → ERRADO (inversão: sinais "
            "opostos)",
        ])],
        "tipo_erro": ["MEIA_VERDADE", "DETALHE"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": "Certa: descreve Slutsky para normais e inferiores (que não sejam de Giffen); nos "
                            "inferiores, o substituição domina, exceto no Giffen.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 543", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "cortada (decomposição de Hicks para bem inferior; mecanismo explicado no 📖)"}],
        "alertas": ["contestavel: “predomínio do efeito substituição” para bens inferiores sem ressalva ao Giffen; "
                    "gabarito da fonte (CERTO) mantido"],
    },
]
