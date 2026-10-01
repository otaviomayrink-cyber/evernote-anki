"""Cards da redação ECO — passada 01 — lote 21 (notas 08 — Monopólio e monopsônio; 09 — Concorrência monopolística)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "eq": "👑 Equilíbrio do monopólio",
    "mk": "📊 Markup, elasticidade e poder de mercado",
    "disc": "🎟️ Discriminação de preços",
    "nat": "🏛️ Monopólio natural e regulação",
    "cham": "🧩 Modelo de Chamberlin",
}

COM_FIRMA_CUSTOS = ("A teoria da firma permite analisar a relação entre os custos de produção e as estruturas de "
                    "mercado. A respeito deste tema, julgue o item a seguir.")
COM_TEORIA_FIRMA = "A respeito da teoria da firma, julgue o item a seguir."
COM_ANTT = ("Apesar de o modelo de concorrência perfeita ser o fundamento para os estudos de equilíbrio de mercado, o "
            "estudo de mercados reais apresenta outras estruturas, em geral envolvendo a fuga de um ou mais "
            "pressupostos da concorrência perfeita. Acerca dessas estruturas de mercado, julgue o item a seguir.")
COM_DISCRIM = ("A discriminação de preços refere-se à prática de cobrar preços diferentes para o mesmo bem ou serviço, "
               "com base em características específicas dos consumidores ou em condições de mercado. Essa estratégia "
               "permite às empresas maximizarem seus lucros, adaptando os preços às diferentes disposições a pagar "
               "dos consumidores. A respeito desta prática, julgue o item a seguir.")
COM_BOZAN = ("Considerando as características e as condições de lucro na concorrência monopolística, julgue o item a "
             "seguir.")
COM_CONC_MONOP = "Acerca da concorrência monopolística, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01405
    {
        "id": "ECO-E2-L01405-1", "fonte_ref": "E2-L01405", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "FEPESE", "prova": "Celesc/Economista/2019", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Acerca do equilíbrio da firma monopolista, julgue o item a seguir (questão adaptada).",
        "rotulo_item": "Item",
        "assertiva": "No ponto de equilíbrio do monopolista, o preço é igual à receita marginal.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No ponto de equilíbrio do monopolista, o preço é ") + vm("igual à") + az(" receita marginal."),
        "poucas": ("No monopólio com preço único, " + vd("RMg < P") + " para toda quantidade positiva: no "
                   "equilíbrio (RMg = CMg), o preço fica <b>acima</b> da receita marginal e do custo marginal."),
        "destrinchando": [
            "O monopolista enfrenta a demanda do mercado, negativamente inclinada. Para vender uma unidade a mais, "
            "precisa baixar o preço de <b>todas</b> as unidades. A receita marginal tem duas parcelas: o preço da "
            "unidade extra (+P) menos a perda nas unidades que já vendia (q·ΔP). Logo, " + vd("RMg = P + q·(ΔP/Δq) < P") + ".",
            "Com demanda linear P = a − bq, a receita total é aq − bq² e " + vd("RMg = a − 2bq") + ": mesmo "
            "intercepto, o <b>dobro</b> da inclinação. A RMg corta o eixo das quantidades na metade do caminho da "
            "demanda.",
            "Equilíbrio: a firma escolhe q onde " + azb("RMg = CMg") + " e lê o preço na demanda, acima desse ponto. "
            "Resultado: " + vd("P > RMg = CMg") + " — é essa distância que gera o " + azb("markup") + " e o "
            + azb("peso morto") + ".",
            "Em termos de elasticidade: " + vd("RMg = P·(1 − 1/|ε|)") + ". Como o monopolista só opera no trecho "
            "elástico (|ε| > 1), a RMg é positiva, mas sempre menor que P.",
            "Contraste: na " + azb("concorrência perfeita") + " a firma é tomadora de preço, a demanda que ela "
            "enfrenta é horizontal e " + vd("P = RMe = RMg") + ". A igualdade do item é a da firma competitiva.",
            vm("Regra-âncora: monopólio de preço único → P > RMg = CMg; concorrência perfeita → P = RMg = CMg."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item transplanta para o monopólio a igualdade P = RMg, que "
                       "vale para a firma tomadora de preço. A condição de equilíbrio do monopolista é RMg = CMg; o "
                       "preço vem da demanda e fica acima. Pista: no monopólio, qualquer frase com “preço igual” a "
                       "RMg ou a CMg é suspeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No ponto de equilíbrio do monopolista, a receita marginal é igual ao custo marginal.”</i> → CERTO",
            "<i>“No ponto de equilíbrio do monopolista, o preço é igual ao custo marginal.”</i> → ERRADO (é a "
            "condição de concorrência perfeita; no monopólio P > CMg)",
            "<i>“Na discriminação perfeita de preços, a receita marginal do monopolista coincide com o preço.”</i> "
            "→ CERTO",
        ])],
        "reescrita": ("No ponto de equilíbrio do monopolista, o preço é " + hl("maior que a")
                      + " receita marginal" + hl(", que se iguala ao custo marginal") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "No monopólio, a receita marginal é sempre menor que o preço (verso só com o gabarito e "
                            "uma imagem decorativa com essa frase).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 322", "tipo_fonte": "DECORATIVA", "lado": "verso",
                           "acao": "cortada (frase “RMg sempre menor que o preço” absorvida no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01406
    {
        "id": "ECO-E2-L01406-1", "fonte_ref": "E2-L01406", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "FEPESE", "prova": "Celesc/Economista/2019", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Acerca do monopólio natural, julgue o item a seguir (questão adaptada).",
        "rotulo_item": "Item",
        "assertiva": ("A empresa detentora de um monopólio natural oferta um bem a um custo médio menor do que duas "
                      "ou mais empresas."),
        "gabarito": "CERTO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("A empresa detentora de um monopólio natural oferta um bem a um <u>custo médio menor</u> do "
                      "que duas ou mais empresas."),
        "poucas": ("É a própria definição de " + azb("monopólio natural") + ": a tecnologia faz com que uma única "
                   "firma atenda o mercado a custo médio menor do que se a produção fosse repartida entre várias "
                   "(" + azb("subaditividade de custos") + ")."),
        "destrinchando": [
            "Origem do fenômeno: " + azb("custos fixos altíssimos") + " (rede elétrica, adutoras, trilhos, dutos) e "
            + azb("custo marginal baixo") + " para atender mais um usuário. O custo médio = CF/q + CVMe cai à medida "
            "que o custo fixo se dilui — " + azb("economias de escala") + " em toda a faixa relevante da demanda.",
            "Por que duas firmas custariam mais: cada uma teria de bancar a própria rede e produziria só parte do "
            "mercado, num ponto mais alto da curva de CMe. Duplicar adutoras numa mesma rua é desperdício social.",
            "Formalmente, C(q₁ + q₂) < C(q₁) + C(q₂): " + azb("subaditividade") + ". Economias de escala bastam "
            "para gerá-la, mas o conceito é mais amplo (pode haver subaditividade mesmo com CMe já subindo um pouco).",
            "Consequência gráfica: com CMe decrescente, o " + vd("CMg fica abaixo do CMe") + ". Daí o dilema "
            "regulatório: preço = CMg é eficiente, mas não cobre o custo médio e gera prejuízo; preço = CMe dá "
            "lucro zero, com alguma perda de eficiência.",
            "Exemplos: distribuição de energia, saneamento, gás canalizado, transmissão. No " + rx("Brasil") + ", "
            "esses segmentos são regulados por agências (ANEEL, ANP, e a ANA nas normas de referência do "
            "saneamento).",
            vm("Regra-âncora: monopólio natural = um produtor sai mais barato que vários (CMe decrescente)."),
        ],
        "dissecando": (cz("[literalidade]") + " O item reproduz a definição de manual (" + oc("Pindyck e Rubinfeld")
                       + ", " + oc("Mankiw") + "). O risco está em confundir “custo médio menor” com “preço menor” ou "
                       "“lucro menor”: o monopolista natural produz barato, mas, sem regulação, cobra caro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por ofertar a custo médio menor, o monopolista natural não regulado pratica preços próximos ao "
            "custo marginal.”</i> → ERRADO (sem regulação, maximiza lucro com RMg = CMg e P > CMg)",
            "<i>“No monopólio natural, o custo marginal situa-se abaixo do custo médio na faixa relevante de "
            "produção.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso composto só de três imagens: definição de monopólio natural (uma empresa supre o "
                            "mercado a custo menor que várias), gráfico de CTMe decrescente e nota sobre a falta de "
                            "fixação de preço pelo custo marginal permitir lucros altos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 323", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 324", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (CMe decrescente descrito no 📖)"},
                          {"ref": "IMAGEM 325", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["nota_redacao: gabarito resolvido — a fonte não traz gabarito escrito (verso só com imagens que definem "
                    "monopólio natural nos termos da assertiva); resolvido como CERTO"],
    },
    # ------------------------------------------------------------------ E2-L01412
    {
        "id": "ECO-E2-L01412-1", "fonte_ref": "E2-L01412", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "FCC", "prova": "ManausPrev/Analista Previdenciário/2021", "ano": 2021,
        "cacd": False, "errei": True,
        "comando": "Acerca da regulação de monopólios naturais, julgue o item a seguir (questão adaptada).",
        "rotulo_item": "Item",
        "assertiva": ("A regulação do preço cobrado por um monopólio natural leva a uma redução do bem-estar dos "
                      "consumidores se for equiparado ao seu custo marginal de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A regulação do preço cobrado por um monopólio natural leva a ") + vm("uma redução")
                   + az(" do bem-estar dos consumidores se for equiparado ao seu custo marginal de produção."),
        "poucas": ("Preço = CMg é o regime <b>mais favorável</b> ao consumidor: preço mais baixo e quantidade maior "
                   "que no monopólio livre. O " + azb("excedente do consumidor aumenta") + "; o problema é da firma, "
                   "que passa a ter prejuízo."),
        "destrinchando": [
            "Sem regulação, o monopolista escolhe RMg = CMg: quantidade q<sub>m</sub> baixa e preço p<sub>m</sub> "
            "alto, lido na demanda. Fica de fora quem valoriza o bem acima do custo de produzi-lo — "
            + azb("peso morto") + ".",
            "Com o preço tabelado no CMg, a firma vende onde a demanda cruza o CMg: " + vd("preço cai, quantidade "
            "sobe") + ". O consumidor ganha duas vezes: paga menos pelas unidades que já comprava (retângulo) e passa "
            "a comprar unidades novas (triângulo). O peso morto desaparece: é a " + azb("eficiência alocativa") + ".",
            "O nó do " + azb("monopólio natural") + ": como o CMe é decrescente, " + vd("CMg < CMe") + ". Com "
            "P = CMg, o preço não cobre o custo médio e a firma tem prejuízo. Só se sustenta com " + azb("subsídio")
            + " (pago pelo contribuinte) ou com " + azb("tarifa em duas partes") + " (assinatura fixa + preço por "
            "unidade igual ao CMg).",
            "Alternativa prática: " + azb("preço = CMe") + " (segundo melhor): lucro econômico zero, quantidade "
            "entre a do monopólio e a eficiente, peso morto menor que o do monopólio livre. Na prática regulatória "
            "brasileira, a tarifa é calculada para cobrir custos eficientes e remunerar o capital (revisões "
            "tarifárias da ANEEL, por exemplo), combinada com " + azb("price cap") + " e incentivos à eficiência.",
            vm("Regra-âncora: P = CMg é ótimo para o consumidor e para a eficiência; o problema é a viabilidade da "
               "firma."),
        ],
        "grafico_verso": "ECO-E2-L01412-1-V1",
        "dissecando": (cz("[inversão]") + " O item troca o sinal do efeito sobre o consumidor, apostando que o "
                       "candidato confunda o dano à <b>firma</b> (prejuízo com P = CMg &lt; CMe) com dano ao "
                       "<b>consumidor</b>. Pergunte sempre: bem-estar de quem? 🔥 FCC e CEBRASPE alternam as duas "
                       "perspectivas no mesmo tema."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A regulação do preço de um monopólio natural ao nível do custo marginal leva a firma a operar com "
            "prejuízo, exigindo subsídio para manter a produção.”</i> → CERTO",
            "<i>“A fixação do preço ao nível do custo médio elimina integralmente o peso morto do monopólio "
            "natural.”</i> → ERRADO (P = CMe reduz, mas não elimina: P continua acima do CMg)",
        ])],
        "reescrita": ("A regulação do preço cobrado por um monopólio natural leva a " + hl("um aumento")
                      + " do bem-estar dos consumidores se for equiparado ao seu custo marginal de produção"
                      + hl(", embora imponha prejuízo à firma") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "P = CMg aumenta a quantidade, maximiza o excedente do consumidor e elimina o peso "
                            "morto; como CMg < CMe, a firma pode ter prejuízo e precisar de subsídio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “bemestar” → “bem-estar” (OCR)"],
    },
    # ------------------------------------------------------------------ E2-L01503
    {
        "id": "ECO-E2-L01503-1", "fonte_ref": "E2-L01503", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_FIRMA_CUSTOS,
        "rotulo_item": "Item",
        "assertiva": ("Um monopolista que consegue cobrar um preço diferente de cada consumidor (discriminação de "
                      "preços de primeiro grau) pode levar a uma situação eficiente no sentido de Pareto, com a "
                      "inexistência de peso morto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um monopolista que consegue cobrar um preço diferente de cada consumidor (discriminação de "
                      "preços de primeiro grau) pode levar a uma situação <u>eficiente no sentido de Pareto</u>, com "
                      "a <u>inexistência de peso morto</u>."),
        "poucas": ("Na " + azb("discriminação perfeita") + ", cada unidade sai pelo preço de reserva: " + vd("RMg = P")
                   + ", e a firma produz até " + vd("P = CMg") + " — a quantidade da concorrência perfeita. Não há "
                   "peso morto; todo o excedente vira lucro."),
        "destrinchando": [
            "Monopólio de preço único: vender mais exige baixar o preço de todas as unidades, então RMg < P e o "
            "ótimo (RMg = CMg) deixa P > CMg. Consumidores dispostos a pagar mais que o custo ficam sem o bem: "
            + azb("peso morto") + ".",
            azb("Discriminação de 1º grau") + ": o monopolista conhece a disposição a pagar de cada comprador e "
            "cobra exatamente esse valor. Vender uma unidade extra não derruba o preço das anteriores — a demanda "
            "vira a curva de receita marginal. Ele avança até o comprador cujo preço de reserva iguala o CMg.",
            "Resultado: excedente total máximo (o mesmo da concorrência perfeita), mas " + vd("EC = 0") + ". "
            + azb("Eficiência de Pareto") + " não fala de justiça: diz só que não dá para melhorar alguém sem "
            "piorar outro. A discriminação perfeita é eficiente e muito concentradora.",
            "Requisitos: informação completa sobre cada consumidor e ausência de revenda (arbitragem). Por isso "
            "é um caso-limite; aproximações reais são leilões, negociação de preço caso a caso e precificação "
            "personalizada em plataformas digitais.",
            "Comparação: 2º grau (menus e descontos por quantidade, autosseleção) e 3º grau (grupos observáveis, "
            "como meia-entrada) capturam só parte do excedente e têm efeito ambíguo sobre o peso morto.",
            vm("Regra-âncora: 1º grau = eficiente (sem peso morto) e distributivamente extremo (EC = 0)."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Parece absurdo chamar de “eficiente” um "
                       "arranjo em que o consumidor perde tudo; o item cobra justamente a separação entre "
                       "eficiência e distribuição. O “pode levar” suaviza e protege o item. 🔥 Tema recorrente: a "
                       "banca alterna “sem peso morto” (CERTO) e “não Pareto-ótimo porque o consumidor perde o "
                       "excedente” (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação de primeiro grau, a alocação não é Pareto-ótima, pois os consumidores perdem "
            "todo o seu excedente.”</i> → ERRADO (confunde distribuição com eficiência)",
            "<i>“Na discriminação de primeiro grau, a quantidade produzida é igual à de concorrência perfeita.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Duas respostas convergentes: discriminação perfeita captura todo o EC, produz até "
                            "P = CMg (quantidade competitiva), elimina o peso morto; eficiência paretiana com "
                            "distribuição concentrada no monopolista.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01540
    {
        "id": "ECO-E2-L01540-1", "fonte_ref": "E2-L01540", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": COM_TEORIA_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("O poder de monopólio pode ser medido pelo <i>mark up</i>, que é a diferença entre o preço e o "
                      "custo médio de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O poder de monopólio pode ser medido pelo <i>mark up</i>, que é a diferença entre o preço e "
                      "o ") + vm("custo médio") + az(" de produção."),
        "poucas": ("O poder de monopólio se mede pela distância entre preço e " + azb("custo marginal") + ", em "
                   "geral relativa ao preço: " + vd("índice de Lerner L = (P − CMg)/P") + ". P − CMe é lucro por "
                   "unidade, não poder de mercado."),
        "destrinchando": [
            azb("Poder de monopólio") + " = capacidade de cobrar acima do " + azb("custo marginal") + ". Em "
            "concorrência perfeita P = CMg; quanto mais o preço se afasta do CMg, mais poder de mercado a firma "
            "exerce.",
            "Medida padrão: " + oc("Abba Lerner") + " (1934) — " + vd("L = (P − CMg)/P") + ", entre 0 "
            "(concorrência perfeita) e 1. No ótimo do monopolista, " + vd("L = 1/|ε|") + ": quanto mais inelástica "
            "a demanda, maior o markup.",
            "Por que não o custo médio: P − CMe mede o " + azb("lucro por unidade") + ", que depende de custos fixos "
            "e do tamanho do mercado. Uma firma pode ter grande poder de mercado e lucro zero (custo fixo alto, como "
            "na concorrência monopolística de longo prazo, em que P = CMe e P > CMg) ou lucro positivo sem poder "
            "de mercado (firma competitiva no curto prazo com P > CMe).",
            "Vocabulário: o " + azb("markup") + " pode aparecer como diferença relativa (P − CMg)/P ou como "
            "multiplicador " + vd("P = CMg · |ε|/(|ε| − 1)") + ". Em ambos, a referência é o CMg.",
            vm("Regra-âncora: poder de mercado → P contra CMg (Lerner); lucro → P contra CMe."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A 1ª parte é verdadeira e dá confiança; o erro está numa "
                       "palavra: “médio” no lugar de “marginal”. Pista: sempre que o item definir markup ou poder "
                       "de mercado, confira qual custo é a referência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O índice de Lerner é igual ao inverso do valor absoluto da elasticidade-preço da demanda no ponto "
            "de equilíbrio do monopolista.”</i> → CERTO",
            "<i>“Firma com lucro econômico nulo não tem poder de mercado.”</i> → ERRADO (na concorrência "
            "monopolística de longo prazo há lucro zero e P > CMg)",
        ])],
        "reescrita": ("O poder de monopólio pode ser medido pelo <i>mark up</i>, que é a diferença entre o preço e o "
                      + hl("custo marginal") + " de produção" + hl(", em geral relativa ao preço (índice de Lerner)")
                      + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Várias respostas convergentes (incluindo a linha duplicada E2-L01714): o markup que "
                            "mede poder de monopólio é sobre o custo marginal, via Lerner (P − CMg)/P = 1/|ε|; "
                            "P − CMe indica lucro por unidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 413", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
]
