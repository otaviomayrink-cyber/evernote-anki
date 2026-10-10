"""Cards do lote de redação 21 — ECO, passada 03 (nota 79: políticas comerciais — tarifas, cotas, subsídios)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "tar": "🧾 Tarifas",
    "cot": "🚫 Cotas e barreiras não tarifárias",
    "sub": "💰 Subsídios e defesa comercial",
}

CMD_BOZAN = "Sobre os instrumentos de proteção ao comércio, julgue o item a seguir (certo ou errado)."

CMD_NAB_PC = "Acerca dos instrumentos de política comercial, julgue (C ou E) o item a seguir."

CMD_NAB_MERC = ("O mercado doméstico de um bem internacionalmente comercializado é descrito por curvas de demanda e "
                "oferta inversas dadas, respectivamente, por P = 100 − 5Q e P = 10 + 4Q. O governo do país avalia "
                "diversas medidas de proteção comercial aos seus produtores. Com base nos conhecimentos acerca desse "
                "assunto, julgue (C ou E) o item a seguir.")

CMD_NAB_CAMB = "A respeito dos instrumentos de política comercial e dos regimes cambiais, julgue (C ou E) o item a seguir."

CMD_NAB_IPC = "Em relação aos instrumentos de política comercial, julgue (C ou E) o item que se segue."

CMD_NAB_A = ("Suponha um mercado competitivo pelo bem A em que a demanda e a oferta doméstica são dadas por "
             "Q<sub>d</sub> = 1600 − 20p e Q<sub>s</sub> = 60p, respectivamente, e a importação do bem A é livre e "
             "sem custos, com preço internacional igual a R$ 10,00. Diante dessa situação, considere que a economia "
             "inicialmente se encontrasse em equilíbrio com importação, e julgue o item a seguir.")

CMD_NAB_23A = ("Com relação ao comércio internacional e aos instrumentos de política comercial, julgue (C ou E) o "
               "item a seguir.")

CMD_NAB_23B = ("Com relação às teorias do comércio internacional e aos instrumentos de política comercial, julgue "
               "(C ou E) o item a seguir.")

CMD_RT_ACO = ("O gráfico a seguir ilustra a imposição de uma tarifa de importação de aço num dado país. Com base "
              "nele, julgue a afirmação.")

CMD_RT_TEO = "A respeito da teoria do comércio internacional, julgue o item a seguir."

FIG_480 = [{"ref": "IMAGEM 480", "tipo_fonte": "GRÁFICO", "lado": "frente", "acao": "redesenhada"},
           {"ref": "IMAGEM 480", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada (repetia a frente)"},
           {"ref": "IMAGEM 481", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "absorvida"},
           {"ref": "IMAGEM 482", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}]

ALERTA_480 = ("figura_conjectural: ECO-E2-L01657-1-F1 redesenhada com as áreas A–G na convenção de Mankiw (A e B: "
              "excedente do consumidor acima do preço com tarifa; C: ganho do produtor; D e F: peso morto; E: "
              "receita; G: excedente do produtor ao preço mundial), coerente com os quatro comentários da fonte; a "
              "transcrição da IMAGEM 480 não traz a posição das letras")

CARDS = [
    # ------------------------------------------------------------------ E2-L00202
    {
        "id": "ECO-E2-L00202-1", "fonte_ref": "E2-L00202", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A adoção de cotas de importação não altera as receitas do governo, ao passo que a adoção de "
                      "restrições voluntárias à exportação tende a diminuir o bem-estar nacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A adoção de cotas de importação ") + vm("não altera as receitas do governo")
                    + az(", ao passo que a adoção de restrições voluntárias à exportação tende a diminuir o "
                         "bem-estar nacional.")),
        "poucas": ("A cota cria uma " + azb("renda de cota") + " (diferença entre o preço interno e o mundial sobre "
                   "as unidades importadas); se o governo " + vm("leiloa as licenças") + ", essa renda vira receita "
                   "pública. A segunda oração (RVE reduz o bem-estar do importador) está correta."),
        "destrinchando": [
            "Uma " + azb("cota de importação") + " limita a quantidade importada; com oferta externa restrita, o "
            "preço interno sobe acima do mundial, exatamente como com uma tarifa. A diferença está em <b>quem fica "
            "com o retângulo</b> (preço interno − preço mundial) × importações: na tarifa, o governo; na cota, o "
            "detentor da licença.",
            "Destino da renda de cota: " + vd("licenças leiloadas") + " → o governo arrecada (a cota passa a "
            "equivaler, inclusive na receita, à tarifa equivalente); " + vd("licenças distribuídas gratuitamente")
            + " → a renda fica com importadores privados; " + vd("cota administrada pelo exportador") + " → a "
            "renda vai para o estrangeiro.",
            "A " + azb("restrição voluntária à exportação") + " (RVE, ou VER) é esse último caso: o país "
            "exportador limita suas vendas, em geral a pedido do importador. O preço no importador sobe e a renda "
            "de cota é capturada por exportadores estrangeiros, de modo que a perda nacional do importador é "
            "<b>maior</b> que a de uma tarifa equivalente: ao peso morto soma-se a renda transferida ao exterior.",
            "Exemplo clássico: a limitação “voluntária” das exportações de automóveis do Japão para os EUA a partir "
            "de 1981, analisada por " + oc("Krugman e Obstfeld") + " como caso de alto custo para o consumidor "
            "norte-americano.",
            vm("Regra-âncora: cota e tarifa equivalente têm o mesmo efeito no preço; muda quem leva o retângulo."),
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " A segunda oração é verdadeira e serve de "
                       "isca; o erro está na negativa categórica da primeira (“não altera”), que ignora o leilão de "
                       "licenças. Pista: em política comercial, afirmação taxativa sobre a <b>destinação</b> da "
                       "renda de cota quase sempre é falsa, porque depende de como as licenças são alocadas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Cotas de importação cujas licenças são leiloadas pelo governo podem gerar receita equivalente à de "
            "uma tarifa.”</i> → CERTO",
            "<i>“A restrição voluntária à exportação é menos custosa para o país importador do que a tarifa "
            "equivalente, pois não gera peso morto.”</i> → ERRADO (inversão: é mais custosa, e há peso morto)",
        ])],
        "reescrita": ("A adoção de cotas de importação " + hl("pode gerar receita ao governo, se as licenças forem "
                                                               "leiloadas")
                      + ", ao passo que a adoção de restrições voluntárias à exportação tende a diminuir o "
                        "bem-estar nacional."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["não altera", "tende a"], "dificuldade": 2,
        "comentario_fonte": ("Cotas podem gerar receita ao governo se licenças forem leiloadas; se distribuídas, a "
                             "renda de cota fica com privados/estrangeiros. VER reduzem o bem-estar do importador."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00831-1 (restrição voluntária às exportações)"],
    },
    # ------------------------------------------------------------------ E2-L00506
    {
        "id": "ECO-E2-L00506-1", "fonte_ref": "E2-L00506", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_PC,
        "rotulo_item": "Item",
        "assertiva": ("Quando os países são grandes exportadores ou importadores de um bem (relativo ao tamanho do "
                      "mercado mundial), as mudanças de preço causadas pelas tarifas aduaneiras e pelos subsídios "
                      "alteram tanto a oferta quanto a demanda relativa nos mercados mundiais. O resultado é uma "
                      "mudança nos termos de comércio, tanto do país que impõe a política de mudança quanto do resto "
                      "do mundo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando os países são <u>grandes</u> exportadores ou importadores de um bem (relativo ao "
                      "tamanho do mercado mundial), as mudanças de preço causadas pelas tarifas aduaneiras e pelos "
                      "subsídios alteram tanto a oferta quanto a demanda relativa nos mercados mundiais. O resultado é "
                      "uma <u>mudança nos termos de comércio</u>, tanto do país que impõe a política de mudança quanto "
                      "do resto do mundo."),
        "poucas": ("Só o " + azb("país grande") + " move o preço mundial: sua tarifa ou subsídio desloca a oferta e "
                   "a demanda relativas mundiais e muda os " + azb("termos de troca") + " dele e dos parceiros."),
        "destrinchando": [
            "É a formulação de " + oc("Krugman, Obstfeld e Melitz") + " no modelo-padrão de comércio: o "
            + azb("país pequeno") + " é tomador de preço (sua política muda só o preço interno); o "
            + azb("país grande") + " pesa o suficiente no mercado mundial para que sua política altere o preço "
            "internacional.",
            "Termos de troca = preço das exportações ÷ preço das importações. Como o ganho de um país em termos de "
            "troca é a perda do parceiro, a mudança é necessariamente <b>dos dois lados</b>, como diz o item.",
            "Direções que a banca cobra: " + vd("tarifa do país grande") + " → reduz a demanda mundial pelo bem "
            "importado → o preço mundial cai → os termos de troca do país que tarifa <b>melhoram</b> (e pioram os "
            "do exportador). " + vd("Subsídio à exportação do país grande") + " → aumenta a oferta mundial do bem "
            "→ o preço mundial cai → os termos de troca do país que subsidia <b>pioram</b>.",
            "Daí a assimetria de bem-estar: a tarifa do país grande pode elevar o bem-estar nacional (argumento da "
            + azb("tarifa ótima") + "), enquanto o subsídio à exportação o reduz sem ambiguidade.",
            vm("Regra-âncora: país pequeno → só o preço interno muda; país grande → o preço mundial e os termos de "
               "troca também mudam."),
        ],
        "dissecando": (cz("[literalidade]") + " O item parafraseia o manual e não traz modulador falso; o risco é "
                       "o leitor procurar uma direção (melhora/piora) que o item não afirma. Ele diz apenas que os "
                       "termos de troca <b>mudam</b>, o que vale tanto para a tarifa quanto para o subsídio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…O resultado é uma melhora nos termos de comércio do país que impõe a política, seja ela tarifa ou "
            "subsídio à exportação.”</i> → ERRADO (o subsídio piora os termos de troca de quem o concede)",
            "<i>“Quando o país é pequeno, a tarifa reduz o preço mundial do bem importado.”</i> → ERRADO (país "
            "pequeno não altera o preço mundial)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["tanto … quanto"], "dificuldade": 1,
        "comentario_fonte": ("País grande: tarifas ou subsídios afetam o preço mundial e, assim, os termos de troca "
                             "do país e dos demais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00507
    {
        "id": "ECO-E2-L00507-1", "fonte_ref": "E2-L00507", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_PC,
        "rotulo_item": "Item",
        "assertiva": ("Como formalizado em Krugman, Obstfeld e Melitz (2015), é consequência da adoção de uma tarifa "
                      "sobre a importação do bem X em um país pequeno, ou seja, tomador de preço, o aumento do "
                      "excedente dos produtores domésticos do bem X."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Como formalizado em Krugman, Obstfeld e Melitz (2015), é consequência da adoção de uma tarifa "
                      "sobre a importação do bem X em um país pequeno, ou seja, tomador de preço, o <u>aumento</u> do "
                      "excedente dos <u>produtores</u> domésticos do bem X."),
        "poucas": ("No país pequeno, o preço interno sobe de P<sub>m</sub> para P<sub>m</sub> + t: os "
                   + azb("produtores domésticos ganham") + " (vendem mais e mais caro), os consumidores perdem e o "
                   "governo arrecada."),
        "destrinchando": [
            "Como o país pequeno não mexe no preço mundial, a tarifa recai inteira sobre o preço interno: "
            + vd("P interno = P mundial + t") + ". A produção doméstica sobe (q<sub>1</sub><sup>s</sup> → "
            "q<sub>2</sub><sup>s</sup>) e o consumo cai.",
            "Balanço de bem-estar (convenção de " + oc("Krugman e Obstfeld") + "): consumidores perdem "
            + vd("a + b + c + d") + "; produtores ganham " + vd("a") + " (o trapézio entre os dois preços, à "
            "esquerda da oferta); o governo arrecada " + vd("c") + " (t × importações); saldo nacional: perda "
            + vd("b + d") + " — os dois triângulos de " + azb("distorção na produção") + " e "
            + azb("distorção no consumo") + ".",
            "No país pequeno não há ganho de termos de troca para compensar: a tarifa <b>sempre</b> reduz o "
            "bem-estar nacional, embora redistribua renda a favor dos produtores do bem protegido.",
            "Por isso a proteção tem defensores organizados: o ganho é concentrado em poucos produtores, e a perda, "
            "diluída entre muitos consumidores (argumento de economia política).",
        ],
        "dissecando": (cz("[literalidade]") + " Item de manual, com a autoridade citada para dar segurança. O risco é "
                       "confundir o efeito sobre os <b>produtores</b> (ganham) com o efeito sobre o <b>país</b> "
                       "(perde) ou sobre os consumidores (perdem). 🔥 A banca alterna os agentes no mesmo bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é consequência da adoção da tarifa em um país pequeno o aumento do bem-estar nacional.”</i> → "
            "ERRADO (troca de agente: o país pequeno sempre perde)",
            "<i>“…a tarifa reduz o preço recebido pelos exportadores estrangeiros.”</i> → ERRADO (só no país "
            "grande)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A tarifa eleva o preço do bem no mercado doméstico; produtores nacionais vendem mais "
                             "caro e produzem mais, aumentando seu excedente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00508
    {
        "id": "ECO-E2-L00508-1", "fonte_ref": "E2-L00508", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_PC,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de tarifa aduaneira por parte de um grande consumidor mundial de determinado "
                      "produto, segundo Krugman e Obstfeld (2014), tem como consequência o aumento do preço do "
                      "produto nos países que o exportam."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A imposição de tarifa aduaneira por parte de um grande consumidor mundial de determinado "
                       "produto, segundo Krugman e Obstfeld (2014), tem como consequência ") + vm("o aumento")
                    + az(" do preço do produto nos países que o exportam.")),
        "poucas": ("A tarifa do país grande " + azb("reduz a demanda mundial") + " pelo produto: o preço mundial — "
                   "e, portanto, o preço nos países exportadores — " + vm("cai") + "."),
        "destrinchando": [
            "Mecanismo: com a tarifa, o preço interno do importador sobe e ele passa a importar menos. Como é um "
            "comprador grande, essa retração derruba a demanda mundial; o mercado internacional só se reequilibra "
            "com " + vd("preço mundial menor") + ". O preço interno no importador sobe <b>menos</b> que a tarifa "
            "(P<sub>interno</sub> = P<sub>mundial</sub>′ + t, com P<sub>mundial</sub>′ &lt; P<sub>mundial</sub>).",
            "Nos países exportadores o efeito é o inverso: o preço cai, a produção cai e o consumo sobe; seus "
            + azb("termos de troca") + " pioram. Parte da tarifa é, na prática, “paga” pelos estrangeiros.",
            "Para o país que tarifa, esse ganho de termos de troca pode superar o peso morto: é o argumento da "
            + azb("tarifa ótima") + " — positiva, mas pequena. O ganho, contudo, é à custa do resto do mundo e "
            "convida à retaliação.",
            "Em " + azb("país pequeno") + ", nada disso acontece: o preço mundial é dado, e a tarifa só eleva o "
            "preço interno.",
            vm("Regra-âncora: tarifa de país grande → preço mundial (e do exportador) cai; preço interno do "
               "importador sobe menos que t."),
        ],
        "dissecando": (cz("[inversão]") + " Troca a direção do preço no exterior. A pegadinha funciona porque o "
                       "preço <b>no país importador</b> de fato sobe; o item transfere essa alta para os "
                       "exportadores. Pista: “grande consumidor” anuncia efeito sobre o preço mundial — e a tarifa "
                       "reduz demanda, logo reduz preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tem como consequência o aumento do preço do produto no próprio país que impõe a tarifa, em "
            "montante inferior ao da tarifa.”</i> → CERTO",
            "<i>“…tem como consequência a piora dos termos de troca do país que impõe a tarifa.”</i> → ERRADO "
            "(inversão: os termos de troca dele melhoram)",
        ])],
        "reescrita": ("A imposição de tarifa aduaneira por parte de um grande consumidor mundial de determinado "
                      "produto, segundo Krugman e Obstfeld (2014), tem como consequência " + hl("a redução")
                      + " do preço do produto nos países que o exportam."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Ocorre o oposto: a tarifa do país grande reduz sua demanda no mercado mundial, o preço "
                             "mundial cai e o preço recebido pelos exportadores diminui."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00509
    {
        "id": "ECO-E2-L00509-1", "fonte_ref": "E2-L00509", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_PC,
        "rotulo_item": "Item",
        "assertiva": ("Na presença do subsídio, os exportadores vão vender até o ponto em que o preço local exceda o "
                      "preço estrangeiro no montante do subsídio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na presença do subsídio, os exportadores vão vender até o ponto em que o preço local "
                      "<u>exceda</u> o preço estrangeiro <u>no montante do subsídio</u>."),
        "poucas": ("Com o " + azb("subsídio à exportação") + " s, exportar rende P<sub>estrangeiro</sub> + s; por "
                   "arbitragem, o preço local sobe até " + vd("P<sub>local</sub> = P<sub>estrangeiro</sub> + s") + "."),
        "destrinchando": [
            "É a frase de " + oc("Krugman e Obstfeld") + " sobre o subsídio à exportação: o governo paga ao "
            "exportador um valor fixo (ou percentual) por unidade vendida no exterior. Enquanto vender fora render "
            "mais que vender dentro, os produtores desviam mercadoria para o exterior; o preço local sobe até "
            "igualar o que se obtém exportando.",
            "Efeitos no país que subsidia (pequeno): preço interno ↑ → " + vd("consumidores perdem") + ", "
            + vd("produtores ganham") + ", " + vd("governo gasta") + " s × exportações. O gasto supera o ganho "
            "líquido do setor: há perda de bem-estar (distorções na produção e no consumo).",
            "Se o país for grande, há um custo adicional: a oferta mundial maior derruba o preço estrangeiro, "
            "piorando os " + azb("termos de troca") + ". O preço local fica acima do novo preço estrangeiro em s, "
            "mas sobe menos que s em relação à situação inicial.",
            "Espelho da tarifa: a tarifa faz P<sub>local</sub> = P<sub>mundial</sub> + t no país importador; o "
            "subsídio faz P<sub>local</sub> = P<sub>estrangeiro</sub> + s no país exportador. Ambos elevam o preço "
            "interno e prejudicam o consumidor doméstico.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Parece estranho que um benefício ao exportador "
                       "<b>encareça</b> o produto no mercado interno — e é aí que muitos marcam ERRADO. A pista é "
                       "pensar como arbitragem: ninguém vende dentro por menos do que ganharia vendendo fora."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na presença do subsídio, o preço local cai abaixo do preço estrangeiro, beneficiando os "
            "consumidores domésticos.”</i> → ERRADO (inversão: o preço local sobe e o consumidor perde)",
            "<i>“Num país grande, o subsídio à exportação reduz o preço estrangeiro do bem.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Condição de arbitragem: só se vende no mercado interno a preço igual ao obtido "
                             "exportando (preço estrangeiro + subsídio)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
