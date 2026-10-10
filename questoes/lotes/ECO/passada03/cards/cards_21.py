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
    # ------------------------------------------------------------------ E2-L00553
    {
        "id": "ECO-E2-L00553-1", "fonte_ref": "E2-L00553", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MERC,
        "rotulo_item": "Item",
        "assertiva": ("Assumindo que o preço internacional do bem seja de 10 unidades monetárias, o país importará 20 "
                      "unidades desse bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Assumindo que o preço internacional do bem seja de 10 unidades monetárias, o país importará ")
                    + vm("20") + az(" unidades desse bem.")),
        "poucas": ("Ao preço 10: Q<sub>d</sub> = " + vd("18") + " e Q<sub>s</sub> = " + vd("0") + ". Importação = "
                   "18 − 0 = " + vd("18") + " unidades, não 20."),
        "destrinchando": [
            "Passo 1 — autarquia: 100 − 5Q = 10 + 4Q → " + vd("Q = 10, P = 50") + ". Como o preço internacional "
            "(10) está abaixo do preço de autarquia (50), o país abre-se como <b>importador</b>.",
            "Passo 2 — demanda ao preço mundial: 10 = 100 − 5Q<sub>d</sub> → " + vd("Q<sub>d</sub> = 18") + ".",
            "Passo 3 — oferta ao preço mundial: 10 = 10 + 4Q<sub>s</sub> → " + vd("Q<sub>s</sub> = 0") + ". O "
            "preço 10 é exatamente o intercepto da oferta inversa: abaixo dele nenhum produtor doméstico produz. "
            "Com livre comércio, a produção nacional desaparece.",
            "Passo 4 — importação = Q<sub>d</sub> − Q<sub>s</sub> = " + vd("18") + ". O consumo inteiro é "
            "atendido de fora.",
            "Cuidado com a forma das curvas: aqui elas vêm <b>inversas</b> (P em função de Q). Para achar "
            "quantidades a um preço dado, isole Q: Q<sub>d</sub> = (100 − P)/5 e Q<sub>s</sub> = (P − 10)/4.",
            vm("Regra-âncora: importação = Q<sub>d</sub>(P<sub>m</sub>) − Q<sub>s</sub>(P<sub>m</sub>), sempre ao "
               "preço que vigora internamente."),
        ],
        "dissecando": (cz("[dado alterado]") + " Item de cálculo: a banca oferece um número redondo próximo do "
                       "correto. O 20 é a quantidade demandada a preço zero (100/5): armadilha para quem confunde o "
                       "intercepto da demanda com o consumo ao preço mundial. Conferir sempre os dois lados (Q<sub>d</sub> e "
                       "Q<sub>s</sub>) separadamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao preço internacional de 10, a produção doméstica do bem será nula.”</i> → CERTO",
            "<i>“Ao preço internacional de 10, o país exportará o bem, pois o preço externo é menor que o de "
            "autarquia.”</i> → ERRADO (inversão: preço externo menor → importa)",
        ])],
        "reescrita": ("Assumindo que o preço internacional do bem seja de 10 unidades monetárias, o país importará "
                      + hl("18") + " unidades desse bem."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("100 − 5Q = 10 + 4Q → Q = 10, P = 50. Ao preço 10: Qd = 18, Qs = 0; importação = 18 "
                             "unidades."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 089", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00554
    {
        "id": "ECO-E2-L00554-1", "fonte_ref": "E2-L00554", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MERC,
        "rotulo_item": "Item",
        "assertiva": ("Caso seja imposta uma cota de 9 unidades de importação, o preço praticado no mercado doméstico "
                      "será de 30 unidades monetárias."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Caso seja imposta uma cota de 9 unidades de importação, o preço praticado no mercado "
                      "doméstico será de <u>30</u> unidades monetárias."),
        "poucas": ("Com a cota, o preço interno sobe até que " + vd("Q<sub>d</sub> − Q<sub>s</sub> = 9") + ": "
                   "(100 − P)/5 − (P − 10)/4 = 9 → " + vd("P = 30") + " (Q<sub>d</sub> = 14, Q<sub>s</sub> = 5)."),
        "destrinchando": [
            "Sem restrição (preço mundial 10), o país importaria " + vd("18") + " unidades. A cota de 9 "
            "<b>morde</b> (9 &lt; 18): a oferta disponível internamente passa a ser a oferta doméstica + 9, e o "
            "preço interno sobe acima do mundial.",
            "Conta: Q<sub>d</sub> = (100 − P)/5 e Q<sub>s</sub> = (P − 10)/4. Exigindo Q<sub>d</sub> − "
            "Q<sub>s</sub> = 9 e multiplicando por 20: 4(100 − P) − 5(P − 10) = 180 → 450 − 9P = 180 → "
            + vd("P = 30") + ". Conferência: Q<sub>d</sub> = 14, Q<sub>s</sub> = 5, diferença 9.",
            azb("Renda de cota") + ": (30 − 10) × 9 = " + vd("180") + ". Quem fica com ela depende da alocação "
            "das licenças (governo, se leiloadas; importadores, se distribuídas; exportadores estrangeiros, numa "
            "restrição voluntária).",
            azb("Tarifa equivalente") + ": uma tarifa específica de " + vd("20") + " levaria o preço a 30 e as "
            "importações a 9 — mesmo preço, mesma quantidade, mesmo peso morto (50 na produção + 40 no consumo "
            "= " + vd("90") + "). A diferença está só no destino do retângulo de 180.",
            vm("Regra-âncora: com cota que morde, o preço interno é o que faz o excesso de demanda doméstico igual "
               "à cota."),
        ],
        "dissecando": (cz("[detalhe]") + " Cálculo direto, mas exige montar a condição certa (excesso de demanda = "
                       "cota). Erro comum: somar a cota à oferta e igualar à demanda <b>ao preço mundial</b>, ou "
                       "esquecer que a cota só altera o preço se for menor que a importação livre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma cota de 20 unidades elevaria o preço doméstico acima de 10.”</i> → ERRADO (cota maior que a "
            "importação livre, 18, não morde)",
            "<i>“Uma tarifa específica de 20 produziria o mesmo preço doméstico que a cota de 9 unidades.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Sem restrição, importação de 18. Com cota de 9: Qd − Qs = 9 → 4(100 − P) − 5(P − 10) "
                             "= 180 → P = 30."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 090", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00889-1 (cota e novo preço doméstico, outro mercado)"],
    },
    # ------------------------------------------------------------------ E2-L00555
    {
        "id": "ECO-E2-L00555-1", "fonte_ref": "E2-L00555", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MERC,
        "rotulo_item": "Item",
        "assertiva": ("Assumindo que o preço internacional do bem seja de 10, caso seja imposta uma tarifa específica "
                      "no valor de 20 unidades monetárias, a quantidade importada no mercado doméstico será de 10 "
                      "unidades do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Assumindo que o preço internacional do bem seja de 10, caso seja imposta uma tarifa "
                       "específica no valor de 20 unidades monetárias, a quantidade importada no mercado doméstico "
                       "será de ") + vm("10") + az(" unidades do bem.")),
        "poucas": ("Com a tarifa, o preço interno vai a 10 + 20 = " + vd("30") + ": Q<sub>d</sub> = 14 e "
                   "Q<sub>s</sub> = 5. Importação = " + vd("9") + " unidades, não 10."),
        "destrinchando": [
            "País pequeno: a " + azb("tarifa específica") + " (valor fixo por unidade) soma-se integralmente ao "
            "preço mundial → " + vd("P interno = 10 + 20 = 30") + ".",
            "A 30: Q<sub>d</sub> = (100 − 30)/5 = " + vd("14") + "; Q<sub>s</sub> = (30 − 10)/4 = " + vd("5")
            + ". Importação = 14 − 5 = " + vd("9") + " (antes da tarifa eram 18).",
            "Efeitos: receita do governo = 20 × 9 = " + vd("180") + "; ganho do produtor = área entre 10 e 30 à "
            "esquerda da oferta = (0 + 5)/2 × 20 = " + vd("50") + "; perda do consumidor = (14 + 18)/2 × 20 = "
            + vd("320") + "; peso morto = 320 − 50 − 180 = " + vd("90") + " (50 de distorção na produção + 40 no "
            "consumo).",
            "Repare que a tarifa de 20 é a " + azb("tarifa equivalente") + " a uma cota de 9 unidades: ambas "
            "levam o preço a 30. A banca costuma explorar essa equivalência no mesmo bloco.",
        ],
        "dissecando": (cz("[dado alterado]") + " O 10 é isca dupla: coincide com o preço internacional e com a "
                       "quantidade de autarquia. Quem não recalcula Q<sub>s</sub> ao novo preço (ou usa a oferta "
                       "inversa sem isolar Q) cai nele."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com a tarifa de 20, a receita tributária será de 180 unidades monetárias.”</i> → CERTO",
            "<i>“Com a tarifa de 20, o preço doméstico subirá menos que o valor da tarifa.”</i> → ERRADO (país "
            "pequeno: sobe a tarifa inteira)",
        ])],
        "reescrita": ("Assumindo que o preço internacional do bem seja de 10, caso seja imposta uma tarifa específica "
                      "no valor de 20 unidades monetárias, a quantidade importada no mercado doméstico será de "
                      + hl("9") + " unidades do bem."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Preço com tarifa = 10 + 20 = 30; Qd = 14, Qs = 5; importação = 9.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 091", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00887-1 (tarifa específica e nova importação, outro mercado)"],
    },
    # ------------------------------------------------------------------ E2-L00556
    {
        "id": "ECO-E2-L00556-1", "fonte_ref": "E2-L00556", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MERC,
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia grande tanto a imposição de uma tarifa de importação quanto a concessão de um "
                      "subsídio à exportação podem levar a uma melhora no bem-estar. Isso ocorre devido ao ganho nos "
                      "termos de troca."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma economia grande ") + vm("tanto") + az(" a imposição de uma tarifa de importação ")
                    + vm("quanto a concessão de um subsídio à exportação podem")
                    + az(" levar a uma melhora no bem-estar. Isso ocorre devido ao ganho nos termos de troca.")),
        "poucas": ("Só a " + azb("tarifa") + " do país grande pode melhorar o bem-estar (ganho de termos de troca). "
                   "O " + vm("subsídio à exportação piora") + " os termos de troca de quem o concede."),
        "destrinchando": [
            vd("Tarifa no país grande") + ": a demanda mundial pelo bem importado cai, o preço mundial cai e o país "
            "passa a pagar menos pelo que importa — " + azb("ganho de termos de troca") + ". Se esse ganho superar "
            "as duas distorções (produção e consumo), o bem-estar nacional sobe. É o argumento da "
            + azb("tarifa ótima") + ".",
            vd("Subsídio à exportação no país grande") + ": a oferta mundial do bem exportado aumenta, o preço "
            "mundial cai e o país passa a receber menos pelo que vende — " + azb("perda de termos de troca") + ". "
            "Somam-se a ela o custo fiscal e as distorções de produção e consumo: perda de bem-estar "
            "<b>inequívoca</b>.",
            "Resumo em balanço (convenção de " + oc("Krugman e Obstfeld") + "): na tarifa, saldo = ganho de termos de "
            "troca − (distorção na produção + distorção no consumo), de sinal ambíguo; no subsídio, saldo = −(perda "
            "de termos de troca + distorções), sempre negativo.",
            "No país pequeno, ambos reduzem o bem-estar: não há efeito sobre o preço mundial para compensar as "
            "distorções.",
            vm("Regra-âncora: país grande — tarifa pode ganhar (termos de troca melhoram); subsídio à exportação "
               "sempre perde (termos de troca pioram)."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Junta um instrumento que pode ganhar (tarifa) "
                       "com outro que sempre perde (subsídio) sob o mesmo “tanto… quanto” e o mesmo motivo. O "
                       "“podem” relativiza, mas não salva o subsídio: para ele o efeito sobre os termos de troca tem "
                       "o sinal oposto. 🔥 Tarifa × subsídio em país grande é par recorrente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em uma economia grande, a imposição de uma tarifa de importação pode levar a uma melhora no "
            "bem-estar, devido ao ganho nos termos de troca.”</i> → CERTO",
            "<i>“Em uma economia pequena, a tarifa ótima é positiva.”</i> → ERRADO (no país pequeno a tarifa ótima "
            "é zero)",
        ])],
        "reescrita": ("Em uma economia grande <s>tanto</s> a imposição de uma tarifa de importação "
                      + hl("pode (mas a concessão de um subsídio à exportação, não)")
                      + " levar a uma melhora no bem-estar. Isso ocorre devido ao ganho nos termos de troca."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["tanto … quanto", "podem"],
        "dificuldade": 2,
        "comentario_fonte": ("Tarifa em economia grande pode elevar o bem-estar pelo ganho de termos de troca; "
                             "subsídio à exportação reduz o preço internacional, piora os termos de troca e reduz o "
                             "bem-estar."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00700-1 (subsídio à exportação e termos de troca do país grande)"],
    },
    # ------------------------------------------------------------------ E2-L00700
    {
        "id": "ECO-E2-L00700-1", "fonte_ref": "E2-L00700", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CAMB,
        "rotulo_item": "Item",
        "assertiva": ("Subsídios à exportação aumentam o bem-estar do país exportador “grande”, pois melhoram seus "
                      "termos de troca no mercado internacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Subsídios à exportação ") + vm("aumentam") + az(" o bem-estar do país exportador “grande”, "
                                                                          "pois ")
                    + vm("melhoram") + az(" seus termos de troca no mercado internacional.")),
        "poucas": ("O subsídio do país grande " + azb("derruba o preço mundial") + " do que ele exporta: os termos "
                   "de troca " + vm("pioram") + " e o bem-estar " + vm("cai") + " sem ambiguidade."),
        "destrinchando": [
            "Mecanismo: o subsídio torna exportar mais lucrativo → a oferta do país no mercado mundial aumenta → "
            "como o país é grande, o " + vd("preço internacional cai") + ". Ele passa a vender suas exportações "
            "mais barato: " + azb("termos de troca") + " (P<sub>X</sub>/P<sub>M</sub>) " + vd("pioram") + ".",
            "Balanço interno: o preço doméstico sobe (fica acima do novo preço mundial no valor do subsídio); "
            "consumidores perdem, produtores ganham, o governo arca com s × exportações. O gasto do governo mais a "
            "perda do consumidor superam o ganho do produtor: sobram as distorções de produção e consumo <b>mais</b> "
            "a perda de termos de troca.",
            "Quem ganha é o resto do mundo, em especial os importadores do bem, que compram mais barato — por isso "
            "subsídios à exportação são, ao mesmo tempo, ruins para quem concede e alvo de disputa por quem "
            "concorre com eles (na OMC, são subsídios proibidos pelo Acordo SMC, salvo regras próprias da "
            "agricultura).",
            "Contraste: a " + azb("tarifa") + " do país grande faz o oposto nos termos de troca (melhora) e pode "
            "elevar o bem-estar nacional.",
            vm("Regra-âncora: subsídio à exportação → preço mundial ↓ → termos de troca ↓ → bem-estar ↓ (sempre)."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sinal do efeito sobre os termos de troca e, por consequência, "
                       "sobre o bem-estar. A frase é sedutora porque transplanta para o subsídio o raciocínio da "
                       "tarifa ótima. Pista: subsidiar exportação = ofertar mais = preço de venda menor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Subsídios à exportação reduzem o bem-estar do país exportador grande, pois pioram seus termos de "
            "troca.”</i> → CERTO",
            "<i>“No país pequeno, o subsídio à exportação não altera o preço doméstico do bem.”</i> → ERRADO (o "
            "preço doméstico sobe no montante do subsídio)",
        ])],
        "reescrita": ("Subsídios à exportação " + hl("reduzem") + " o bem-estar do país exportador “grande”, pois "
                      + hl("pioram") + " seus termos de troca no mercado internacional."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O subsídio do país grande aumenta a oferta mundial, reduz o preço internacional e piora "
                             "os termos de troca; com o custo fiscal e as distorções, há perda inequívoca de "
                             "bem-estar."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00556-1 (tarifa × subsídio em país grande)"],
    },
    # ------------------------------------------------------------------ E2-L00701
    {
        "id": "ECO-E2-L00701-1", "fonte_ref": "E2-L00701", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CAMB,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de uma tarifa sobre a importação de um país sempre impõe uma perda líquida de "
                      "bem-estar (peso morto) composta por distorções tanto no consumo quanto na produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A imposição de uma tarifa sobre a importação de um país ") + vm("sempre")
                    + az(" impõe uma perda líquida de bem-estar (peso morto) composta por distorções tanto no "
                         "consumo quanto na produção.")),
        "poucas": ("O “" + vm("sempre") + "” falha no " + azb("país grande") + ": o ganho de termos de troca pode "
                   "superar as distorções, e o efeito líquido sobre o bem-estar pode ser positivo (" + azb("tarifa "
                                                                                                        "ótima")
                   + ")."),
        "destrinchando": [
            "As distorções existem em qualquer caso: a tarifa leva a produzir internamente unidades mais caras que "
            "as importadas (" + azb("distorção na produção") + ") e a deixar de consumir unidades que valiam mais "
            "que o preço mundial (" + azb("distorção no consumo") + "). São os dois triângulos de peso morto.",
            "No " + vd("país pequeno") + ", o saldo nacional é exatamente esse peso morto: a tarifa sempre reduz o "
            "bem-estar.",
            "No " + vd("país grande") + ", entra um terceiro termo: a queda do preço mundial do bem importado "
            "(" + azb("ganho de termos de troca") + ", o retângulo entre o preço mundial antigo e o novo, vezes as "
            "importações). Saldo = ganho de termos de troca − distorções; para tarifas pequenas o ganho domina, e "
            "existe uma " + azb("tarifa ótima") + " positiva que maximiza o bem-estar nacional.",
            "Ressalvas que a banca pode cobrar: o ganho é à custa dos parceiros (o mundo como um todo perde) e "
            "convida à retaliação, que pode anular o ganho — por isso o argumento é mais teórico que recomendação "
            "de política.",
            vm("Regra-âncora: tarifa em país pequeno → perda certa; em país grande → resultado ambíguo (tarifa "
               "ótima &gt; 0)."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " O conteúdo descreve bem o país pequeno; o “sempre” estende a "
                       "conclusão ao país grande, onde ela não vale. Observação: o item mistura “perda líquida” com "
                       "“peso morto” — os triângulos sempre existem, mas o saldo líquido pode ser positivo; o "
                       "gabarito lê “perda líquida” como saldo. 🔥 “Sempre” + tarifa = pensar no país grande."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A imposição de uma tarifa sobre a importação de um país pequeno sempre impõe uma perda líquida de "
            "bem-estar.”</i> → CERTO",
            "<i>“Para um país grande, quanto maior a tarifa, maior o ganho de bem-estar.”</i> → ERRADO (acima da "
            "tarifa ótima, as distorções dominam)",
        ])],
        "reescrita": ("A imposição de uma tarifa sobre a importação de um país " + hl("pequeno") + " <s>sempre</s> "
                      "impõe uma perda líquida de bem-estar (peso morto) composta por distorções tanto no "
                      "consumo quanto na produção."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 2,
        "comentario_fonte": ("O erro está em “sempre”: no país grande, a tarifa pode melhorar os termos de troca e, "
                             "se o ganho superar as perdas de eficiência, elevar o bem-estar (tarifa ótima)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00831
    {
        "id": "ECO-E2-L00831-1", "fonte_ref": "E2-L00831", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_IPC,
        "rotulo_item": "Item",
        "assertiva": ("As restrições voluntárias às exportações se referem à situação em que uma nação exportadora "
                      "induz uma outra a restringir suas importações de uma commodity voluntariamente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As restrições voluntárias às exportações se referem à situação em que uma nação ")
                    + vm("exportadora") + az(" induz uma outra a restringir suas ") + vm("importações")
                    + az(" de uma commodity voluntariamente.")),
        "poucas": ("Na " + azb("RVE") + " é a nação " + vm("importadora") + " que induz a exportadora a limitar "
                   "as próprias " + vm("exportações") + ": uma cota administrada pelo exportador."),
        "destrinchando": [
            "A " + azb("restrição voluntária às exportações") + " (RVE; em inglês, VER — <i>voluntary export "
            "restraint</i>) é uma cota de comércio aplicada pelo <b>país exportador</b>, em geral a pedido do "
            "importador, que a aceita para evitar barreiras piores (tarifas, cotas unilaterais, medidas "
            "antidumping).",
            "Exemplo clássico: a limitação das exportações de automóveis do " + vd("Japão") + " para os "
            + vd("EUA") + " a partir de " + vd("1981") + ". Outro: o Acordo Multifibras (têxteis), que vigorou de "
            "1974 até sua eliminação gradual no âmbito da OMC (concluída em 2005).",
            "Efeito econômico: igual ao de uma cota de importação — o preço no importador sobe —, com uma "
            "diferença decisiva: a " + azb("renda de cota") + " fica com os exportadores estrangeiros, que vendem "
            "menos unidades a preço mais alto. Para o importador, é mais custosa que a tarifa equivalente.",
            "O “voluntário” é eufemismo: a restrição é negociada sob ameaça. Por isso o Acordo sobre Salvaguardas da "
            "OMC (1994) proibiu novas RVEs e mandou eliminar as existentes.",
            vm("Regra-âncora: na RVE, o exportador restringe as próprias exportações, pressionado pelo importador."),
        ],
        "dissecando": (cz("[inversão · troca de ator]") + " Inverte os papéis: troca quem induz (importador → "
                       "exportador) e o que se restringe (exportações → importações). Pista no próprio nome do "
                       "instrumento: é restrição às <b>exportações</b>, logo quem a aplica é o exportador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na restrição voluntária às exportações, a renda de cota é apropriada pelos exportadores "
            "estrangeiros.”</i> → CERTO",
            "<i>“A restrição voluntária às exportações é instrumento estimulado pelo Acordo sobre Salvaguardas da "
            "OMC.”</i> → ERRADO (o acordo as proibiu)",
        ])],
        "reescrita": ("As restrições voluntárias às exportações se referem à situação em que uma nação "
                      + hl("importadora") + " induz uma outra a restringir suas " + hl("exportações")
                      + " de uma commodity voluntariamente."),
        "tipo_erro": ["INVERSAO", "TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A RVE é uma cota imposta pelo país exportador, em vez do importador, geralmente a pedido "
                             "deste; exemplo: automóveis japoneses para os EUA depois de 1981."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 126", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00202-1 (restrição voluntária às exportações e bem-estar)"],
    },
    # ------------------------------------------------------------------ E2-L00832
    {
        "id": "ECO-E2-L00832-1", "fonte_ref": "E2-L00832", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_IPC,
        "rotulo_item": "Item",
        "assertiva": ("Uma tarifa específica sobre importações reduz o excedente do consumidor, ao passo que a adoção "
                      "de um subsídio à exportação também diminui esse excedente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma tarifa específica sobre importações <u>reduz</u> o excedente do consumidor, ao passo que a "
                      "adoção de um subsídio à exportação <u>também diminui</u> esse excedente."),
        "poucas": ("Os dois instrumentos " + azb("elevam o preço doméstico") + ": a tarifa, para P<sub>m</sub> + t; "
                   "o subsídio, para P<sub>m</sub> + s. Preço maior → " + vd("consumidor perde") + " nos dois casos."),
        "destrinchando": [
            vd("Tarifa de importação") + " (país importador): o preço interno sobe do preço mundial para o preço "
            "mundial + tarifa. O consumidor paga mais e consome menos — perde o trapézio entre os dois preços, à "
            "esquerda da demanda. Produtores ganham; o governo arrecada; sobram dois triângulos de peso morto.",
            vd("Subsídio à exportação") + " (país exportador): por arbitragem, o preço interno sobe até o preço "
            "mundial + subsídio (ninguém vende dentro por menos do que ganharia exportando). O consumidor doméstico "
            "também paga mais e consome menos. Produtores ganham; o governo <b>gasta</b>; também sobram dois "
            "triângulos de peso morto.",
            "Paralelo útil: tarifa e subsídio à exportação são “primos” — ambos protegem o produtor elevando o "
            "preço interno e ambos têm o consumidor como perdedor. A diferença está no governo: na tarifa ele "
            "arrecada, no subsídio ele paga.",
            "O que muda no país grande: a tarifa reduz o preço mundial (o consumidor perde menos que t por "
            "unidade); o subsídio também reduz o preço mundial, mas o preço interno continua acima dele — o "
            "consumidor doméstico perde em qualquer caso.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " O “subsídio” soa como benefício a todos, e a leitura apressada "
                       "supõe que barateie o produto internamente. O item é CERTO porque o subsídio é à "
                       "<b>exportação</b>, não ao consumo. Pista: pergunte sempre o que acontece com o preço "
                       "interno."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…ao passo que a adoção de um subsídio à exportação aumenta o excedente do consumidor doméstico, "
            "por baratear o bem.”</i> → ERRADO (inversão: o preço interno sobe)",
            "<i>“Tanto a tarifa quanto o subsídio à exportação geram receita para o governo.”</i> → ERRADO (o "
            "subsídio é gasto)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["também"], "dificuldade": 1,
        "comentario_fonte": ("A tarifa eleva o preço doméstico e reduz o excedente do consumidor; o subsídio à "
                             "exportação também eleva o preço doméstico (preço mundial + subsídio) e igualmente reduz "
                             "esse excedente; produtores ganham e o governo gasta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 127", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (descrição incorporada ao 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00833
    {
        "id": "ECO-E2-L00833-1", "fonte_ref": "E2-L00833", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_IPC,
        "rotulo_item": "Item",
        "assertiva": ("O instrumento de política industrial mediante o qual o governo brasileiro, com o objetivo de "
                      "fomentar a inovação e a industrialização nas cadeias produtivas de petróleo e gás natural (P&amp;G) "
                      "no país, estabelece índices mínimos de participação dos fornecedores de máquinas e equipamentos "
                      "no valor da produção da indústria de P&amp;G é denominado política de quotas de importação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O instrumento de política industrial mediante o qual o governo brasileiro, com o objetivo de "
                       "fomentar a inovação e a industrialização nas cadeias produtivas de petróleo e gás natural "
                       "(P&amp;G) no país, estabelece índices mínimos de participação dos fornecedores de máquinas e "
                       "equipamentos no valor da produção da indústria de P&amp;G é denominado ")
                    + vm("política de quotas de importação") + az(".")),
        "poucas": ("Índice mínimo de participação nacional no valor da produção é " + azb("exigência de conteúdo "
                                                                                          "local")
                   + ", não cota de importação (que limita diretamente a quantidade importada)."),
        "destrinchando": [
            "Uma " + azb("exigência de conteúdo local") + " obriga que determinada fração do valor (ou das peças) "
            "de um bem final seja produzida domesticamente. Não fixa quantidade importada: fixa uma "
            "<b>proporção</b>, e o produtor escolhe a combinação.",
            "Diferenças em relação à cota, na linha de " + oc("Krugman e Obstfeld") + ": a exigência de conteúdo "
            "local não gera receita para o governo nem renda de cota; o custo maior dos insumos nacionais entra na "
            "média do custo e é repassado ao consumidor. Exemplo: com 50% de peças nacionais a US$ 10.000 e peças "
            "importadas a US$ 6.000, o custo médio vai a " + vd("US$ 8.000") + ".",
            rx("Brasil") + ": os contratos de exploração da ANP trazem cláusulas de conteúdo local desde as "
            "primeiras rodadas de licitação (fim dos anos 1990), e a política ganhou peso com o pré-sal; os "
            "percentuais foram reduzidos e simplificados a partir de 2017 ⏳ (out/2026).",
            "Na OMC, exigências de conteúdo local vinculadas a investimento colidem com o Acordo TRIMs e com o "
            "tratamento nacional do GATT; o " + rx("Brasil") + " foi condenado em painel sobre o Inovar-Auto e "
            "outros programas (2017-2018).",
            vm("Regra-âncora: cota = limite à quantidade importada; conteúdo local = proporção mínima de insumo "
               "nacional."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Descreve com precisão a política de conteúdo local e lhe dá o "
                       "nome de um instrumento vizinho (barreira não tarifária também, mas de outra natureza). "
                       "Pista: “índices mínimos de participação” no valor da produção indicam proporção, não teto de "
                       "importação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A exigência de conteúdo local, ao contrário da cota, não gera renda de cota nem receita "
            "tarifária.”</i> → CERTO",
            "<i>“A exigência de conteúdo local é uma barreira tarifária.”</i> → ERRADO (é não tarifária)",
        ])],
        "reescrita": ("O instrumento de política industrial mediante o qual o governo brasileiro, com o objetivo de "
                      "fomentar a inovação e a industrialização nas cadeias produtivas de petróleo e gás natural "
                      "(P&amp;G) no país, estabelece índices mínimos de participação dos fornecedores de máquinas e "
                      "equipamentos no valor da produção da indústria de P&amp;G é denominado "
                      + hl("política de conteúdo local") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Exigência de conteúdo local requer que fração do bem seja produzida domesticamente; não "
                             "gera receita nem renda de cota; exemplo do custo médio de autopeças (US$ 8.000)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 128", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00834
    {
        "id": "ECO-E2-L00834-1", "fonte_ref": "E2-L00834", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_IPC,
        "rotulo_item": "Item",
        "assertiva": ("Uma cota de importação constitui uma restrição indireta sobre a quantidade de algum bem que pode "
                      "ser importado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma cota de importação constitui uma restrição ") + vm("indireta")
                    + az(" sobre a quantidade de algum bem que pode ser importado.")),
        "poucas": ("A cota é a restrição " + vm("direta") + " por excelência: fixa a quantidade máxima importável, "
                   "em geral por meio de " + azb("licenças de importação") + "."),
        "destrinchando": [
            "Definição de " + oc("Krugman e Obstfeld") + ": “uma cota de importação é uma restrição direta sobre a "
            "quantidade de algum bem que pode ser importado”, normalmente aplicada pela emissão de licenças a "
            "grupos de pessoas ou empresas.",
            "Restrições <b>indiretas</b> são as que reduzem importações sem fixar quantidade: a " + azb("tarifa")
            + " (atua pelo preço), as " + azb("exigências de conteúdo local") + ", barreiras técnicas e "
            "sanitárias, compras governamentais preferenciais, burocracia aduaneira.",
            "Efeito da cota: com a quantidade importada limitada, o preço interno sobe até o excesso de demanda "
            "doméstico igualar a cota. Daí a " + azb("tarifa equivalente") + " (que produziria o mesmo preço) e a "
            + azb("renda de cota") + " (preço interno − preço mundial) × cota, que vai para quem detém as "
            "licenças.",
            "Diferença dinâmica: com a tarifa, um aumento de demanda eleva as importações; com a cota, eleva o "
            "preço interno (a quantidade importada não se move). Por isso a cota protege mais em mercado aquecido.",
        ],
        "dissecando": (cz("[inversão]") + " Troca um único adjetivo: direta → indireta. O item é curto e técnico, e "
                       "o erro está na palavra que qualifica o instrumento. Pista: a cota atua na própria "
                       "quantidade, sem intermediação do preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A tarifa de importação constitui uma restrição indireta à quantidade importada, por atuar via "
            "preço.”</i> → CERTO",
            "<i>“Com a cota, um aumento da demanda doméstica eleva a quantidade importada.”</i> → ERRADO (eleva o "
            "preço interno; a quantidade fica limitada)",
        ])],
        "reescrita": ("Uma cota de importação constitui uma restrição " + hl("direta") + " sobre a quantidade de "
                      "algum bem que pode ser importado."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Cota de importação é restrição direta na quantidade importada, aplicada com a emissão "
                             "de licenças."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01154-1 (natureza da cota de importação)"],
    },
    # ------------------------------------------------------------------ E2-L00886
    {
        "id": "ECO-E2-L00886-1", "fonte_ref": "E2-L00886", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_A,
        "rotulo_item": "Item",
        "assertiva": "Na hipótese de livre comércio, a quantidade importada será de 800 unidades.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na hipótese de livre comércio, a quantidade importada será de <u>800</u> unidades."),
        "poucas": ("A p = 10: Q<sub>d</sub> = 1600 − 200 = " + vd("1.400") + " e Q<sub>s</sub> = " + vd("600")
                   + ". Importação = " + vd("800") + "."),
        "destrinchando": [
            "Autarquia: 1600 − 20p = 60p → " + vd("p = 20, Q = 1.200") + ". O preço internacional (10) está "
            "abaixo do de autarquia: o país importa.",
            "Ao preço mundial: Q<sub>d</sub> = " + vd("1.400") + "; Q<sub>s</sub> = " + vd("600")
            + "; importação = Q<sub>d</sub> − Q<sub>s</sub> = " + vd("800") + ". A produção doméstica atende 600 "
            "e o resto vem de fora.",
            "Ganhos do comércio frente à autarquia: o consumidor ganha (paga 10 em vez de 20 e consome mais); o "
            "produtor perde (vende menos e mais barato); o ganho do consumidor supera a perda do produtor — o "
            "saldo é o triângulo entre as curvas de 1.200 até as quantidades de livre comércio: ½ × 800 × 10 = "
            + vd("4.000") + ".",
            "Se o governo instituir uma tarifa de R$ 5 por unidade, o preço interno vai a 15, a importação cai para "
            "400 (produção 900, consumo 1.300) e surge peso morto de R$ 1.000.",
        ],
        "dissecando": (cz("[detalhe]") + " Cálculo direto com curvas já na forma Q(p). O erro típico seria "
                       "confundir a quantidade importada (800) com a demandada (1.400) ou com a de autarquia "
                       "(1.200)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na hipótese de livre comércio, a produção doméstica será de 1.200 unidades.”</i> → ERRADO (1.200 "
            "é a quantidade de autarquia; com comércio, 600)",
            "<i>“Na ausência de comércio, o preço doméstico seria de R$ 20,00.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Ao preço 10: Qd = 1400, Qs = 600; importação = 800.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 142", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00887
    {
        "id": "ECO-E2-L00887-1", "fonte_ref": "E2-L00887", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_A,
        "rotulo_item": "Item",
        "assertiva": ("Se o governo passa a instituir uma tarifa de importação de R$ 5,00 por unidade importada, a "
                      "quantidade importada será igual a 200 unidades."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o governo passa a instituir uma tarifa de importação de R$ 5,00 por unidade importada, a "
                       "quantidade importada será igual a ") + vm("200") + az(" unidades.")),
        "poucas": ("Preço interno = 10 + 5 = " + vd("15") + ": Q<sub>d</sub> = " + vd("1.300") + ", Q<sub>s</sub> "
                   "= " + vd("900") + ". Importação = " + vd("400") + ", não 200."),
        "destrinchando": [
            "País pequeno (preço internacional dado): a " + azb("tarifa específica") + " de R$ 5 soma-se ao preço "
            "→ " + vd("p = 15") + ".",
            "Q<sub>d</sub> = 1600 − 20 × 15 = " + vd("1.300") + " (o consumo cai 100); Q<sub>s</sub> = 60 × 15 = "
            + vd("900") + " (a produção doméstica sobe 300). Importação = " + vd("400") + " (era 800).",
            "Repare na decomposição: a importação cai 400 = 300 de substituição por produção nacional + 100 de "
            "redução do consumo. A oferta é mais sensível ao preço (inclinação 60) que a demanda (20), por isso "
            "a maior parte do ajuste vem da produção.",
            "Bem-estar: receita = 5 × 400 = " + vd("R$ 2.000") + "; peso morto = ½ × 300 × 5 + ½ × 100 × 5 = "
            + vd("R$ 1.000") + ". E uma cota de 400 unidades levaria ao mesmo preço de R$ 15 (tarifa "
            "equivalente).",
        ],
        "dissecando": (cz("[dado alterado]") + " O 200 é metade do valor correto e sai de erros típicos: aplicar a "
                       "tarifa só à demanda, ou subtrair a variação da produção da variação do consumo. Recalcule as "
                       "duas quantidades ao novo preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com a tarifa de R$ 5,00, a receita do governo será de R$ 2.000,00.”</i> → CERTO",
            "<i>“Com a tarifa de R$ 5,00, a produção doméstica cairá para 300 unidades.”</i> → ERRADO (sobe para "
            "900)",
        ])],
        "reescrita": ("Se o governo passa a instituir uma tarifa de importação de R$ 5,00 por unidade importada, a "
                      "quantidade importada será igual a " + hl("400") + " unidades."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Com a tarifa, p = 15; Qd = 1300, Qs = 900; importação = 400.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 143", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00555-1 (tarifa específica e nova importação, outro mercado)"],
    },
    # ------------------------------------------------------------------ E2-L00888
    {
        "id": "ECO-E2-L00888-1", "fonte_ref": "E2-L00888", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_A + " Admita que o governo institua uma tarifa de importação de R$ 5,00 por unidade "
                               "importada.",
        "rotulo_item": "Item",
        "assertiva": "O peso morto da tarifa de importação será R$ 1.500.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O peso morto da tarifa de importação será ") + vm("R$ 1.500") + az("."),
        "poucas": ("Peso morto = dois triângulos de altura 5: ½ × 300 × 5 (produção) + ½ × 100 × 5 (consumo) = "
                   + vd("R$ 1.000") + "."),
        "destrinchando": [
            "Com a tarifa, p = 15: Q<sub>s</sub> sobe de 600 para " + vd("900") + " e Q<sub>d</sub> cai de 1.400 "
            "para " + vd("1.300") + ". A importação cai de 800 para " + vd("400") + ".",
            azb("Distorção na produção") + ": as 300 unidades a mais produzidas internamente custam entre 10 e 15, "
            "quando poderiam ser importadas a 10 → ½ × 300 × 5 = " + vd("750") + ".",
            azb("Distorção no consumo") + ": as 100 unidades que deixam de ser consumidas valiam para o consumidor "
            "entre 10 e 15 → ½ × 100 × 5 = " + vd("250") + ".",
            "Atalho: como as duas alturas são iguais à tarifa, peso morto = ½ × (queda das importações) × t = "
            "½ × 400 × 5 = " + vd("1.000") + ".",
            "Conferência pelo balanço completo: perda do consumidor = (1.300 + 1.400)/2 × 5 = 6.750; ganho do "
            "produtor = (600 + 900)/2 × 5 = 3.750; receita = 5 × 400 = 2.000. Saldo: 6.750 − 3.750 − 2.000 = "
            + vd("1.000") + ".",
            vm("Regra-âncora: peso morto da tarifa = ½ × t × (Δprodução + Δconsumo) = ½ × t × Δimportações."),
        ],
        "grafico_verso": "ECO-E2-L00888-1-V1",
        "dissecando": (cz("[dado alterado]") + " O 1.500 é 1,5 vez o correto — resultado de quem soma triângulos "
                       "errados (por exemplo, ½ × 600 × 5, usando a produção inicial como base). Item de cálculo: "
                       "localizar as duas bases (300 e 100) resolve."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O peso morto da tarifa decorre em maior parte da distorção na produção.”</i> → CERTO (750 de "
            "1.000)",
            "<i>“A receita tributária da tarifa corresponde a peso morto, por ser renda retirada dos "
            "consumidores.”</i> → ERRADO (receita é transferência, não perda)",
        ])],
        "reescrita": "O peso morto da tarifa de importação será " + hl("R$ 1.000") + ".",
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Peso morto = ½ × 400 × 5 = 1.000 (750 da produção + 250 do consumo). Comentários "
                             "empilhados com o mesmo resultado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 144", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (gráfico didático com os números do item)"}],
        "alertas": ["nota_redacao: a fonte omitia o valor da tarifa (R$ 5,00, dado em item do mesmo bloco); "
                    "acrescentado ao comando para o card ser autossuficiente"],
    },
    # ------------------------------------------------------------------ E2-L00889
    {
        "id": "ECO-E2-L00889-1", "fonte_ref": "E2-L00889", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_A,
        "rotulo_item": "Item",
        "assertiva": ("Partindo da hipótese de livre comércio e equilíbrio com importação, se o governo passa a "
                      "instituir uma quota de 400 unidades, o preço doméstico será R$ 20."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Partindo da hipótese de livre comércio e equilíbrio com importação, se o governo passa a "
                       "instituir uma quota de 400 unidades, o preço doméstico será ") + vm("R$ 20") + az(".")),
        "poucas": ("Com a quota, 1600 − 20p = 60p + 400 → " + vd("p = R$ 15") + ". R$ 20 é o preço de "
                   "<b>autarquia</b>, que só vigoraria com importação zero."),
        "destrinchando": [
            "A quota limita a importação a 400 (a livre importação era 800: a quota morde). A oferta disponível "
            "internamente vira " + vd("60p + 400") + "; igualando à demanda: 1600 − 20p = 60p + 400 → 80p = 1.200 "
            "→ " + vd("p = 15") + ".",
            "Conferência: Q<sub>d</sub> = 1.300, Q<sub>s</sub> = 900, diferença 400 = quota.",
            "É o mesmo preço da tarifa de R$ 5,00 por unidade: a quota de 400 e a tarifa de 5 são "
            + azb("equivalentes") + " (mesmo preço, mesma quantidade, mesmo peso morto de R$ 1.000). Muda o "
            "destino do retângulo (15 − 10) × 400 = " + vd("R$ 2.000") + ": receita do governo na tarifa, "
            + azb("renda de cota") + " de quem detém as licenças na quota.",
            "De onde vem o R$ 20? É o preço de equilíbrio sem comércio (1600 − 20p = 60p → p = 20). Com qualquer "
            "quota positiva, o preço fica entre o mundial (10) e o de autarquia (20).",
        ],
        "dissecando": (cz("[dado alterado]") + " A banca oferece um número que existe no problema — o preço de "
                       "autarquia —, para quem esquece de somar a quota à oferta doméstica. Pista: a quota é "
                       "positiva, logo o preço não pode chegar ao de economia fechada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma quota de 400 unidades e uma tarifa de R$ 5,00 por unidade levam ao mesmo preço "
            "doméstico.”</i> → CERTO",
            "<i>“Uma quota de zero unidades levaria o preço doméstico a R$ 20,00.”</i> → CERTO",
        ])],
        "reescrita": ("Partindo da hipótese de livre comércio e equilíbrio com importação, se o governo passa a "
                      "instituir uma quota de 400 unidades, o preço doméstico será " + hl("R$ 15") + "."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Oferta total = 60p + 400; 1600 − 20p = 60p + 400 → p = 15 (igual ao da tarifa de "
                             "R$ 5,00)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00554-1 (cota e novo preço doméstico, outro mercado)"],
    },
    # ------------------------------------------------------------------ E2-L01154
    {
        "id": "ECO-E2-L01154-1", "fonte_ref": "E2-L01154", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23A,
        "rotulo_item": "Item",
        "assertiva": ("As cotas de importação são um exemplo de instrumento tarifário cujo objetivo é o de proteger a "
                      "indústria local."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As cotas de importação são um exemplo de instrumento ") + vm("tarifário")
                    + az(" cujo objetivo é o de proteger a indústria local.")),
        "poucas": ("A cota é " + azb("barreira não tarifária") + ": limita a quantidade importada. Instrumento "
                   "tarifário é a tarifa (imposto de importação). O objetivo de proteção está correto."),
        "destrinchando": [
            azb("Instrumentos tarifários") + ": a tarifa de importação, " + vd("específica") + " (valor fixo por "
            "unidade) ou " + vd("ad valorem") + " (percentual do valor), e suas variantes (tarifa mista, cota "
            "tarifária — alíquota menor até certo volume, maior acima dele).",
            azb("Barreiras não tarifárias") + ": " + vd("cotas de importação") + ", restrições voluntárias às "
            "exportações, exigências de conteúdo local, subsídios, barreiras técnicas e sanitárias, licenciamento "
            "não automático, compras governamentais preferenciais.",
            "Embora a cota e a tarifa equivalente produzam o mesmo preço interno, a natureza é diferente: a tarifa "
            "atua pelo preço e gera receita; a cota atua na quantidade e gera " + azb("renda de cota") + " para "
            "quem detém as licenças.",
            "Na OMC, o GATT (art. XI) proíbe, como regra, restrições quantitativas — cotas inclusive —, admitindo "
            "exceções (balanço de pagamentos, salvaguardas, agricultura em casos específicos). A " + azb("tarifação")
            + " da Rodada Uruguai converteu barreiras não tarifárias agrícolas em tarifas equivalentes.",
            vm("Regra-âncora: tarifa = imposto (preço); cota = limite de quantidade (não tarifária)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item acerta o objetivo (proteger a indústria) e erra a "
                       "classificação. A meia-frase verdadeira dá credibilidade ao todo. Pista: “tarifário” "
                       "pressupõe imposto; a cota não tributa nada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As cotas de importação são barreiras não tarifárias e, como regra, são vedadas pelo "
            "GATT.”</i> → CERTO",
            "<i>“A cota tarifária é uma restrição quantitativa absoluta às importações.”</i> → ERRADO (é alíquota "
            "diferenciada por volume, não teto)",
        ])],
        "reescrita": ("As cotas de importação são um exemplo de instrumento " + hl("não tarifário")
                      + " cujo objetivo é o de proteger a indústria local."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Tarifas são instrumento tarifário; cotas são limitações quantitativas sobre o total "
                             "importado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00834-1 (natureza da cota de importação)"],
    },
    # ------------------------------------------------------------------ E2-L01155
    {
        "id": "ECO-E2-L01155-1", "fonte_ref": "E2-L01155", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23A,
        "rotulo_item": "Item",
        "assertiva": ("O subsídio à exportação eleva o excedente do produtor à custa somente da redução do excedente "
                      "do consumidor."),
        "gabarito": "ERRADO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": (az("O subsídio à exportação eleva o excedente do produtor à custa ") + vm("somente")
                    + az(" da redução do excedente do consumidor.")),
        "poucas": ("O ganho do produtor é pago pelo " + azb("consumidor") + " (preço interno maior) " + vm("e pelo "
                                                                                                         "governo")
                   + " (gasto com o subsídio); e ainda sobra perda líquida de bem-estar."),
        "destrinchando": [
            "Com o subsídio s por unidade exportada, o preço interno sobe para P<sub>m</sub> + s (arbitragem). Os "
            "produtores vendem mais e mais caro; os consumidores pagam mais e consomem menos; o governo paga s "
            "sobre cada unidade exportada.",
            "Balanço (país pequeno, letras do gráfico): consumidor perde " + vd("a + b") + "; produtor ganha "
            + vd("a + b + c") + "; governo gasta " + vd("b + c + d") + ". Saldo nacional: " + vd("−(b + d)")
            + " — as distorções no consumo (b) e na produção (d), análogas às da tarifa.",
            "No país grande (versão de " + oc("Krugman e Obstfeld") + "), o subsídio ainda derruba o preço "
            "estrangeiro: o gasto do governo cresce e há perda adicional de termos de troca. A conclusão se "
            "reforça: o subsídio à exportação sempre reduz o bem-estar de quem o concede.",
            "Comparação com a tarifa: nos dois casos o consumidor perde e o produtor ganha; mas na tarifa o governo "
            "<b>arrecada</b>, no subsídio ele <b>paga</b>.",
            vm("Regra-âncora: subsídio à exportação → produtor ganha à custa do consumidor E do Tesouro, com perda "
               "líquida."),
        ],
        "grafico_verso": "ECO-E2-L01155-1-V1",
        "dissecando": (cz("[restrição indevida]") + " O “somente” apaga um dos pagadores — o governo. Sem ele, o "
                       "subsídio pareceria mera transferência entre consumidores e produtores. Pista: subsídio é "
                       "sempre gasto público; se o item não o menciona entre os custos, desconfie."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O subsídio à exportação eleva o excedente do produtor à custa da redução do excedente do "
            "consumidor e do gasto do governo, gerando perda líquida.”</i> → CERTO",
            "<i>“O ganho dos produtores com o subsídio supera a soma das perdas dos consumidores e do "
            "governo.”</i> → ERRADO (inversão: é menor; a diferença é a perda líquida b + d)",
        ])],
        "reescrita": ("O subsídio à exportação eleva o excedente do produtor à custa <s>somente</s> da redução do "
                      "excedente do consumidor" + hl(" e do gasto do governo, com perda líquida de bem-estar")
                      + "."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["somente"], "dificuldade": 1,
        "comentario_fonte": ("Verso só com imagens: gráfico do subsídio à exportação (produtor ganha a + b + c, "
                             "consumidor perde a + b, governo gasta b + c + d + e + f + g) e nota de que b, d e e são "
                             "perdas de distorção."),
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 190", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (versão didática de país pequeno)"},
                          {"ref": "IMAGEM 191", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["nota_redacao: o verso da fonte não traz gabarito escrito; ERRADO resolvido pelo conteúdo (e "
                    "coincide com a classificação)"],
    },
    # ------------------------------------------------------------------ E2-L01156
    {
        "id": "ECO-E2-L01156-1", "fonte_ref": "E2-L01156", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23A,
        "rotulo_item": "Item",
        "assertiva": ("A desvalorização do yuan frente ao dólar norte-americano aumenta a competitividade da produção "
                      "chinesa frente à produção norte americana. A imposição unilateral, por parte dos EUA, de "
                      "tarifas de importação aos produtos chineses reduz esse ganho de competitividade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A desvalorização do yuan frente ao dólar norte-americano <u>aumenta</u> a competitividade da "
                      "produção chinesa frente à produção norte americana. A imposição unilateral, por parte dos "
                      "EUA, de tarifas de importação aos produtos chineses <u>reduz</u> esse ganho de "
                      "competitividade."),
        "poucas": ("O yuan desvalorizado " + azb("barateia em dólar") + " os produtos chineses; a tarifa dos EUA os "
                   + azb("encarece") + " no mercado norte-americano e compensa, no todo ou em parte, esse ganho."),
        "destrinchando": [
            "Preço em dólar de um bem chinês nos EUA ≈ (preço em yuan ÷ taxa de câmbio yuan/dólar) × (1 + "
            "tarifa). Uma " + azb("desvalorização") + " do yuan (mais yuans por dólar) reduz o primeiro termo; a "
            + azb("tarifa") + " eleva o segundo. Os dois efeitos vão em sentidos opostos.",
            "Equivalência aproximada: uma desvalorização de x% pode ser neutralizada, para o mercado "
            "norte-americano, por uma tarifa de cerca de x%. Por isso tarifas são às vezes defendidas como "
            "resposta a “manipulação cambial”.",
            "Limites: a tarifa só compensa no mercado dos EUA; nos demais mercados (e em terceiros países) a China "
            "segue mais competitiva. Além disso, a tarifa encarece insumos e bens finais para consumidores e "
            "empresas norte-americanos.",
            "Contexto: na guerra comercial de 2018-2019, os EUA impuseram tarifas sobre centenas de bilhões de "
            "dólares em importações chinesas; em agosto de 2019, o yuan ultrapassou 7 por dólar e o Tesouro "
            "norte-americano classificou a China como manipuladora cambial (designação retirada em janeiro de "
            "2020).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Duas orações de mecanismo simples, ambas corretas. O risco é o "
                       "candidato confundir desvalorização com valorização ou supor que a tarifa “reforça” a "
                       "competitividade chinesa. Pista: câmbio e tarifa atuam sobre o mesmo preço final em dólar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A valorização do yuan frente ao dólar aumenta a competitividade da produção chinesa nos "
            "EUA.”</i> → ERRADO (inversão: valorização encarece os produtos chineses em dólar)",
            "<i>“A tarifa dos EUA neutraliza o ganho de competitividade chinês em todos os mercados.”</i> → ERRADO "
            "(modulador absoluto: só no mercado norte-americano)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A desvalorização do yuan reduz o preço em dólar dos produtos chineses; as tarifas dos "
                             "EUA, ao elevarem esse preço, podem compensar em algum grau o efeito cambial."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01163
    {
        "id": "ECO-E2-L01163-1", "fonte_ref": "E2-L01163", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23B,
        "rotulo_item": "Item",
        "assertiva": ("As quotas à importação, contrariamente às tarifas, não alteram o preço relativo entre os "
                      "produtos domésticos e importados e, portanto, não afetam a distribuição de renda do país que "
                      "as impõe."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As quotas à importação, ") + vm("contrariamente às tarifas, não alteram")
                    + az(" o preço relativo entre os produtos domésticos e importados e, portanto, ")
                    + vm("não afetam") + az(" a distribuição de renda do país que as impõe.")),
        "poucas": ("Como a tarifa, a quota " + azb("eleva o preço interno") + " do bem importado: consumidores "
                   "perdem, produtores domésticos ganham e surge renda de quota. A distribuição de renda "
                   + vm("muda") + "."),
        "destrinchando": [
            "Ao limitar a quantidade importada, a quota cria escassez relativa: o preço interno sobe acima do "
            "mundial até o excesso de demanda igualar a quota. O preço do bem importável sobe em relação aos "
            "demais — exatamente o que faz uma tarifa.",
            "Efeitos distributivos idênticos aos da " + azb("tarifa equivalente") + ": " + vd("consumidores")
            + " perdem; " + vd("produtores domésticos") + " ganham; o retângulo (preço interno − mundial) × quota "
            "vai para os " + vd("detentores das licenças") + " (renda de quota), e não para o governo — salvo "
            "leilão das licenças.",
            "Em nível de fatores, vale o raciocínio de " + oc("Stolper-Samuelson") + ": a proteção que eleva o "
            "preço relativo de um bem aumenta a remuneração real do fator usado intensivamente nele — seja a "
            "proteção feita por tarifa ou por quota.",
            "Diferenças reais entre quota e tarifa: o destino do retângulo; a resposta a choques de demanda (com "
            "quota, o ajuste é todo no preço); e o incentivo a poder de mercado (a quota pode transformar um "
            "produtor doméstico em monopolista, o que a tarifa não faz).",
            vm("Regra-âncora: quota e tarifa equivalente elevam igualmente o preço interno; muda só quem fica com o "
               "retângulo."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Fabrica uma diferença inexistente entre os "
                       "instrumentos (“contrariamente”) e dela deduz uma consequência falsa (“portanto”). Pista: "
                       "qualquer restrição à oferta de importados eleva o preço interno."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As quotas à importação, assim como as tarifas, elevam o preço interno; a diferença é que a renda "
            "correspondente pode ficar com os detentores de licenças.”</i> → CERTO",
            "<i>“A quota não gera peso morto, porque não arrecada.”</i> → ERRADO (o peso morto é o mesmo da tarifa "
            "equivalente)",
        ])],
        "reescrita": ("As quotas à importação, " + hl("assim como as tarifas, alteram") + " o preço relativo entre "
                      "os produtos domésticos e importados e, portanto, " + hl("afetam") + " a distribuição de renda "
                      "do país que as impõe."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["contrariamente", "portanto"],
        "dificuldade": 1,
        "comentario_fonte": ("A cota tem os mesmos efeitos de uma tarifa (eleva o preço, reduz importações, prejudica "
                             "compradores e beneficia vendedores), exceto que a renda vai para os detentores de "
                             "licenças."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 194", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01164
    {
        "id": "ECO-E2-L01164-1", "fonte_ref": "E2-L01164", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23B,
        "rotulo_item": "Item",
        "assertiva": ("As perdas relativas a bem-estar decorrentes da imposição de uma tarifa sobre produtos "
                      "importados serão tanto maiores quanto mais inelástica for a curva de demanda por esses "
                      "produtos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As perdas relativas a bem-estar decorrentes da imposição de uma tarifa sobre produtos "
                       "importados serão tanto maiores quanto mais ") + vm("inelástica")
                    + az(" for a curva de demanda por esses produtos.")),
        "poucas": ("O peso morto do consumo é ½ × t × ΔQ<sub>d</sub>: quanto mais " + azb("elástica") + " a "
                   "demanda, maior a queda do consumo e " + vm("maior") + " a perda. Demanda inelástica → perda "
                   "menor."),
        "destrinchando": [
            "Peso morto da tarifa (país pequeno) = " + vd("½ × t × ΔQ<sub>s</sub>") + " (distorção na produção) + "
            + vd("½ × t × ΔQ<sub>d</sub>") + " (distorção no consumo). As alturas são fixas (= t); o que varia é "
            "a base, isto é, quanto as quantidades reagem ao preço.",
            "Demanda " + azb("inelástica") + ": o consumo quase não cai com a alta de preço → triângulo de consumo "
            "pequeno. No limite (demanda vertical), essa distorção é " + vd("zero") + " e a perda do consumidor "
            "vira quase toda transferência (receita e ganho do produtor).",
            "Demanda " + azb("elástica") + ": o consumo cai muito → triângulo grande. O mesmo vale para a oferta: "
            "oferta doméstica mais elástica amplia a distorção na produção.",
            "É a mesma lógica da tributação interna (regra de " + oc("Ramsey") + "): impostos sobre bases "
            "inelásticas distorcem menos. Com a ressalva de equidade: bens de demanda inelástica costumam pesar "
            "mais no orçamento dos pobres.",
            vm("Regra-âncora: peso morto cresce com as elasticidades (e com o quadrado da tarifa)."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte a relação entre elasticidade e peso morto. A confusão vem de "
                       "outra regra verdadeira: com demanda inelástica, o <b>consumidor arca</b> com mais do "
                       "imposto (incidência). Incidência ≠ eficiência — a banca explora essa troca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As perdas de eficiência decorrentes de uma tarifa serão tanto maiores quanto mais elástica for a "
            "oferta doméstica.”</i> → CERTO",
            "<i>“Com demanda perfeitamente inelástica, a tarifa não altera o excedente do consumidor.”</i> → ERRADO "
            "(o consumidor perde; só a distorção no consumo é nula)",
        ])],
        "reescrita": ("As perdas relativas a bem-estar decorrentes da imposição de uma tarifa sobre produtos "
                      "importados serão tanto maiores quanto mais " + hl("elástica") + " for a curva de demanda por "
                      "esses produtos."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tanto maiores quanto"], "dificuldade": 2,
        "comentario_fonte": ("Quanto mais inelástica a demanda, menores as perdas de bem-estar decorrentes da "
                             "tarifa."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 195", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01165
    {
        "id": "ECO-E2-L01165-1", "fonte_ref": "E2-L01165", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23B,
        "rotulo_item": "Item",
        "assertiva": ("As tarifas ad valorem são caracterizadas pela cobrança de um determinado valor por unidade "
                      "importada, independentemente do preço do produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As tarifas ") + vm("ad valorem") + az(" são caracterizadas pela cobrança de um determinado "
                                                              "valor por unidade importada, independentemente do "
                                                              "preço do produto.")),
        "poucas": ("A definição é a da " + azb("tarifa específica") + " (valor fixo por unidade). A "
                   + azb("ad valorem") + " é um " + vm("percentual do valor") + " do bem importado."),
        "destrinchando": [
            azb("Tarifa específica") + ": valor fixo por unidade física — ex.: " + vd("US$ 10 por bicicleta")
            + ", custe ela US$ 100 ou US$ 1.000. Pesa mais, proporcionalmente, sobre os produtos baratos.",
            azb("Tarifa ad valorem") + ": percentual do valor — ex.: " + vd("20%") + " sobre uma bicicleta de "
            "US$ 100 = " + vd("US$ 20") + ". Acompanha o preço: protege igual em termos proporcionais e se ajusta à "
            "inflação.",
            "Efeito da inflação: com tarifa específica, a alta de preços corrói a proteção (o valor fixo vira uma "
            "fração menor do preço); com ad valorem, a proteção se mantém. Há ainda a " + azb("tarifa mista")
            + " (combina as duas).",
            rx("Brasil") + ": a Tarifa Externa Comum do Mercosul (TEC) é expressa em alíquotas ad valorem sobre o "
            "valor aduaneiro.",
            vm("Regra-âncora: específica = R$ por unidade; ad valorem = % do valor."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Descrição correta de um instrumento com o nome do outro. O "
                       "“independentemente do preço” é a pista: ad valorem significa literalmente “conforme o "
                       "valor”."),
        "modulos": [("🧠 Mnemônico", ["<i>Ad valorem</i> = “ao valor” → percentual; <b>específica</b> = por "
                                      "<b>espécie</b> (unidade)."])],
        "reescrita": ("As tarifas " + hl("específicas") + " são caracterizadas pela cobrança de um determinado valor "
                      "por unidade importada, independentemente do preço do produto."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["independentemente"], "dificuldade": 1,
        "comentario_fonte": ("Tarifa específica: valor fixo por unidade (US$ 10 por bicicleta); ad valorem: "
                             "percentual do valor (20% de US$ 100 = US$ 20)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 196", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01657-1
    {
        "id": "ECO-E2-L01657-1", "fonte_ref": "E2-L01657", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ACO,
        "frente_figuras": ["ECO-E2-L01657-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Após a tarifa, o excedente dos ofertantes domésticos vai crescer no montante equivalente à soma "
                      "das áreas C e G."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Após a tarifa, o excedente dos ofertantes domésticos vai crescer no montante equivalente à ")
                    + vm("soma das áreas") + az(" C ") + vm("e G") + az(".")),
        "poucas": ("O excedente do produtor " + azb("cresce") + " só pela área " + vd("C") + ". A área G já era "
                   "excedente do produtor ao preço mundial: C + G é o excedente <b>final</b>, não o aumento."),
        "destrinchando": [
            "Leitura do gráfico (convenção de " + oc("Mankiw") + "): ao preço mundial, o consumidor tem "
            "A + B + C + D + E + F e o produtor doméstico tem G. Com a tarifa, o preço interno sobe para o preço "
            "com tarifa.",
            "Depois da tarifa: excedente do consumidor = " + vd("A + B") + "; excedente do produtor = " + vd("C + G")
            + "; receita do governo = " + vd("E") + "; peso morto = " + vd("D + F") + ".",
            "Variações: consumidor " + vd("−(C + D + E + F)") + "; produtor " + vd("+C") + "; governo "
            + vd("+E") + "; total " + vd("−(D + F)") + ". D é a " + azb("distorção na produção") + " (unidades "
            "produzidas internamente acima do custo de importá-las); F, a " + azb("distorção no consumo") + ".",
            "C é transferência do consumidor para o produtor: o trapézio entre o preço mundial e o preço com "
            "tarifa, à esquerda da oferta doméstica (de 0 a Qs2).",
            vm("Regra-âncora: “cresce” pede a variação (C), não o estoque final (C + G)."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A soma C + G existe no gráfico — é o excedente "
                       "<b>final</b> do produtor. O erro está no verbo: “crescer no montante” pede a "
                       "<b>variação</b>. 🔥 Gráficos com áreas em letra sempre testam estoque × variação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Após a tarifa, o excedente dos ofertantes domésticos passa a ser a soma das áreas C e G.”</i> → "
            "CERTO",
            "<i>“O peso morto da tarifa corresponde às áreas D, E e F.”</i> → ERRADO (E é receita do governo, não "
            "perda)",
        ])],
        "reescrita": ("Após a tarifa, o excedente dos ofertantes domésticos vai crescer no montante equivalente à "
                      + hl("área") + " C<s> e G</s>."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O aumento do excedente do produtor é só a área C; G não faz parte do ganho (a fonte a "
                             "descreve, erradamente, como “parcela do excedente do consumidor perdida”)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": FIG_480,
        "alertas": [ALERTA_480,
                    "qualidade_fonte: o comentário de origem descreve G como perda do consumidor; G é o excedente do "
                    "produtor anterior à tarifa"],
    },
    # ------------------------------------------------------------------ E2-L01657-2
    {
        "id": "ECO-E2-L01657-2", "fonte_ref": "E2-L01657", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ACO,
        "frente_figuras": ["ECO-E2-L01657-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Os consumidores, após a tarifa, terão redução do seu excedente que não será compensada pelo "
                      "aumento do excedente dos ofertantes e pela receita do governo, gerando uma redução do "
                      "excedente total conhecida como peso morto, dado pela soma das áreas E e F."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os consumidores, após a tarifa, terão redução do seu excedente que não será compensada pelo "
                       "aumento do excedente dos ofertantes e pela receita do governo, gerando uma redução do "
                       "excedente total conhecida como peso morto, dado pela soma das áreas ") + vm("E")
                    + az(" e F.")),
        "poucas": ("Todo o raciocínio está certo até a última palavra: o peso morto é " + vd("D + F") + ". A área "
                   + vm("E") + " é a " + azb("receita do governo") + " — transferência, não perda."),
        "destrinchando": [
            "Perda do consumidor com a tarifa: " + vd("C + D + E + F") + " (o trapézio entre o preço mundial e o "
            "preço com tarifa, à esquerda da demanda).",
            "Para onde vai cada pedaço: " + vd("C") + " → produtores domésticos (ganho de excedente); " + vd("E")
            + " → governo (tarifa × importações remanescentes, de Qs2 a QD2); " + vd("D") + " e " + vd("F")
            + " → ninguém. Por isso o peso morto é D + F.",
            azb("D (distorção na produção)") + ": entre Qs1 e Qs2, o país passa a produzir internamente, a custo "
            "acima do preço mundial, unidades que antes importava. " + azb("F (distorção no consumo)") + ": "
            "entre QD2 e QD1, deixam de ser consumidas unidades que os consumidores valorizavam acima do preço "
            "mundial.",
            "Forma de reconhecer no gráfico: as áreas de peso morto são os dois <b>triângulos</b> laterais; a "
            "receita é o <b>retângulo</b> central, cuja base são as importações após a tarifa.",
            vm("Regra-âncora: tarifa — receita é o retângulo (E); peso morto são os dois triângulos (D + F)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Item longo, quase todo verdadeiro, com o erro na última letra: "
                       "troca D (triângulo de distorção) por E (retângulo de receita). 🔥 Itens de tarifa com áreas "
                       "costumam embutir o erro no fim, depois de uma descrição correta que gera confiança."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…gerando uma redução do excedente total conhecida como peso morto, dado pela soma das áreas D e "
            "F.”</i> → CERTO",
            "<i>“A área E representa perda de eficiência associada à redução do consumo.”</i> → ERRADO (E é "
            "receita; a perda do consumo é F)",
        ])],
        "reescrita": ("Os consumidores, após a tarifa, terão redução do seu excedente que não será compensada pelo "
                      "aumento do excedente dos ofertantes e pela receita do governo, gerando uma redução do "
                      "excedente total conhecida como peso morto, dado pela soma das áreas " + hl("D") + " e F."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O peso morto é D + F, não E + F; E é a arrecadação do governo (transferência); D é a "
                             "perda produtiva e F a perda de consumo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_480,
        "alertas": [ALERTA_480,
                    "nota_redacao: item marcado com ❌ na fonte (errei = True), embora a classificação registrasse "
                    "errei = False para a questão"],
    },
    # ------------------------------------------------------------------ E2-L01657-3
    {
        "id": "ECO-E2-L01657-3", "fonte_ref": "E2-L01657", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ACO,
        "frente_figuras": ["ECO-E2-L01657-1-F1"],
        "rotulo_item": "Item",
        "assertiva": "A arrecadação do governo com a tarifa de importação é equivalente à soma das áreas E e R.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A arrecadação do governo com a tarifa de importação é equivalente à ") + vm("soma das áreas")
                    + az(" E") + vm(" e R") + az(".")),
        "poucas": ("A receita da tarifa é só a área " + vd("E") + ": tarifa × importações após a tarifa (de Qs2 a "
                   "QD2). Não existe área R no gráfico."),
        "destrinchando": [
            "Receita tarifária = " + vd("(preço com tarifa − preço mundial) × (QD2 − Qs2)") + ": o retângulo "
            "central, cuja altura é a tarifa e cuja base são as importações que continuam a entrar.",
            "As áreas vizinhas não são receita: " + vd("D") + " e " + vd("F") + " (triângulos laterais) são peso "
            "morto; " + vd("C") + " é ganho do produtor; " + vd("A + B") + " é o que resta do excedente do "
            "consumidor; " + vd("G") + " é o excedente do produtor ao preço mundial.",
            "Erro clássico em itens de receita: usar como base as importações <b>antes</b> da tarifa (QD1 − Qs1). "
            "Essa base incluiria D e F, que não arrecadam nada — são unidades que deixaram de ser importadas.",
            "Num país grande, a receita teria uma parte paga pelos estrangeiros (a queda do preço mundial × "
            "importações), que é o ganho de termos de troca; no gráfico, país pequeno, toda a receita sai do "
            "consumidor doméstico.",
        ],
        "dissecando": (cz("[extrapolação]") + " O item acrescenta à área correta (E) uma área que o gráfico não "
                       "tem (R). Pista: diante de rótulo desconhecido, confira a figura antes de julgar — a "
                       "receita da tarifa é sempre um retângulo único."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A arrecadação do governo com a tarifa equivale à área E.”</i> → CERTO",
            "<i>“A arrecadação do governo com a tarifa equivale às áreas D, E e F.”</i> → ERRADO (D e F são peso "
            "morto)",
        ])],
        "reescrita": ("A arrecadação do governo com a tarifa de importação é equivalente à " + hl("área")
                      + " E<s> e R</s>."),
        "tipo_erro": ["EXTRAPOLACAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A arrecadação é só a área E (tarifa × importações após a tarifa); não há área R no "
                             "gráfico."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_480,
        "alertas": [ALERTA_480],
    },
    # ------------------------------------------------------------------ E2-L01657-4
    {
        "id": "ECO-E2-L01657-4", "fonte_ref": "E2-L01657", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ACO,
        "frente_figuras": ["ECO-E2-L01657-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Se o governo optar por uma cota de importação equivalente à tarifa, será melhor para os "
                      "consumidores pois o preço pago por eles não subirá."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o governo optar por uma cota de importação equivalente à tarifa, ")
                    + vm("será melhor para os consumidores pois o preço pago por eles não subirá") + az(".")),
        "poucas": ("A cota equivalente limita as importações a QD2 − Qs2 e leva o preço interno ao " + vm("mesmo "
                                                                                                         "nível")
                   + " da tarifa: para o consumidor, nada muda. Muda só quem fica com a área E."),
        "destrinchando": [
            azb("Cota equivalente") + " = a que permite importar exatamente a quantidade que entraria com a tarifa "
            "(QD2 − Qs2). Com a oferta externa limitada a esse volume, o preço interno sobe até o mesmo preço "
            "com tarifa.",
            "Consumidor e produtor doméstico: efeitos idênticos (perda C + D + E + F; ganho C). Peso morto: o "
            "mesmo (D + F).",
            "A diferença está no retângulo " + vd("E") + ": com a tarifa, é receita do governo; com a cota, vira "
            + azb("renda de cota") + " — apropriada pelos importadores que recebem as licenças (ou pelos "
            "exportadores estrangeiros, numa restrição voluntária). Só se o governo " + vd("leiloar as licenças")
            + " recupera essa receita.",
            "Por isso, do ponto de vista nacional, a cota tende a ser pior que a tarifa equivalente: a mesma perda "
            "para o consumidor, sem a arrecadação correspondente. E, sob choque de demanda, a cota faz o preço "
            "subir ainda mais (as importações não acompanham).",
            vm("Regra-âncora: cota equivalente = mesmo preço, mesmo peso morto; E vira renda de cota."),
        ],
        "dissecando": (cz("[juízo indevido · nexo indevido]") + " Atribui à cota uma vantagem para o consumidor "
                       "que ela não tem e a justifica com um mecanismo falso (preço que não sobe). Pista: "
                       "“equivalente à tarifa” já significa “com o mesmo efeito sobre preço e quantidade”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o governo optar por uma cota de importação equivalente à tarifa, o preço doméstico será o "
            "mesmo, mas a receita E poderá ficar com os detentores das licenças.”</i> → CERTO",
            "<i>“A cota equivalente elimina o peso morto, pois não envolve cobrança de imposto.”</i> → ERRADO (o "
            "peso morto D + F permanece)",
        ])],
        "reescrita": ("Se o governo optar por uma cota de importação equivalente à tarifa, " + hl("o efeito para os "
                                                                                                  "consumidores "
                                                                                                  "será o mesmo, "
                                                                                                  "pois o preço "
                                                                                                  "pago por eles "
                                                                                                  "subirá igualmente")
                      + "."),
        "tipo_erro": ["JUIZO_INDEVIDO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A cota equivalente resulta no mesmo preço doméstico; muda a distribuição: a receita E "
                             "vai para os importadores com licença, salvo leilão."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_480,
        "alertas": [ALERTA_480],
    },
    # ------------------------------------------------------------------ E2-L01763
    {
        "id": "ECO-E2-L01763-1", "fonte_ref": "E2-L01763", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_TEO,
        "rotulo_item": "Item",
        "assertiva": ("A redução da tarifa de importação de arroz pelo governo brasileiro em 2020, diante do aumento "
                      "dos preços internos deste produto, pode ser explicado pela teoria econômica, sendo esperado "
                      "por esta um aumento da oferta interna e a redução de preços, aumentando o excedente dos "
                      "consumidores e mantendo inalterado o excedente dos produtores domésticos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A redução da tarifa de importação de arroz pelo governo brasileiro em 2020, diante do aumento "
                       "dos preços internos deste produto, pode ser explicado pela teoria econômica, sendo esperado "
                       "por esta um aumento da oferta interna e a redução de preços, aumentando o excedente dos "
                       "consumidores e ") + vm("mantendo inalterado") + az(" o excedente dos produtores domésticos.")),
        "poucas": ("Reduzir a tarifa " + azb("baixa o preço interno") + ": o consumidor ganha, mas o produtor "
                   "doméstico vende menos e mais barato — seu excedente " + vm("cai") + "."),
        "destrinchando": [
            "É o caminho inverso da tarifa: o preço interno cai de P<sub>m</sub> + t para perto de P<sub>m</sub>; "
            "as importações aumentam (a “oferta interna”, no sentido de oferta disponível no mercado doméstico, "
            "cresce), o consumo sobe e a produção nacional recua.",
            "Bem-estar: o consumidor recupera o trapézio entre os dois preços (" + vd("ganho") + "); o produtor "
            "perde o trapézio entre os dois preços à esquerda da oferta (" + vd("perda") + "); o governo perde "
            "receita; o país recupera os dois triângulos de peso morto. Saldo nacional positivo, com redistribuição "
            "de produtores para consumidores.",
            rx("Brasil") + ": em setembro de " + vd("2020") + ", com o arroz em alta (câmbio depreciado, demanda "
            "externa forte e consumo doméstico aquecido na pandemia), a Camex zerou temporariamente a tarifa de "
            "importação de arroz de fora do Mercosul para uma cota de " + vd("400 mil toneladas") + ", até o fim "
            "do ano — uma cota tarifária.",
            "Na prática o efeito foi limitado (o preço mundial também subia e o real estava desvalorizado), mas a "
            "direção prevista pela teoria é a do item, salvo pelo excedente do produtor.",
            vm("Regra-âncora: tarifa ↓ → preço interno ↓ → consumidor ganha, produtor doméstico perde, país ganha "
               "(peso morto recuperado)."),
        ],
        "dissecando": (cz("[meia-verdade]") + " Tudo é correto até o fim: o erro está em afirmar neutralidade para "
                       "o produtor. Pista: toda mudança no preço interno redistribui excedente entre os dois lados "
                       "do mercado — não há como baixar o preço sem afetar quem vende."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…aumentando o excedente dos consumidores e reduzindo o excedente dos produtores domésticos, com "
            "ganho líquido de bem-estar.”</i> → CERTO",
            "<i>“A redução da tarifa reduz o bem-estar total do país pequeno, pois os produtores perdem.”</i> → "
            "ERRADO (o ganho do consumidor supera a perda do produtor e da receita)",
        ])],
        "reescrita": ("A redução da tarifa de importação de arroz pelo governo brasileiro em 2020, diante do aumento "
                      "dos preços internos deste produto, pode ser explicado pela teoria econômica, sendo esperado "
                      "por esta um aumento da oferta interna e a redução de preços, aumentando o excedente dos "
                      "consumidores e " + hl("reduzindo") + " o excedente dos produtores domésticos."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Trecho errado: “mantendo inalterado o excedente dos produtores domésticos”. A redução "
                             "da tarifa beneficia consumidores e reduz o excedente dos produtores domésticos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 526", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico genérico de tarifa, absorvido no 📖)"}],
        "alertas": [],
    },
]
