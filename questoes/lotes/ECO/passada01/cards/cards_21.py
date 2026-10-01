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
    # ------------------------------------------------------------------ E2-L01662
    {
        "id": "ECO-E2-L01662-1", "fonte_ref": "E2-L01662", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "A respeito dos conceitos e teorias da microeconomia, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "Num monopólio, o <i>mark up</i> é maior quanto mais inelástica ao preço for a demanda.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Num monopólio, o <i>mark up</i> é <u>maior</u> quanto mais <u>inelástica</u> ao preço for a "
                      "demanda."),
        "poucas": ("Pela " + azb("regra de Lerner") + ", no ótimo do monopolista " + vd("(P − CMg)/P = 1/|ε|")
                   + ": quanto menor |ε| (demanda mais inelástica), maior o markup."),
        "destrinchando": [
            "Derivação em uma linha: o monopolista iguala RMg = CMg, e " + vd("RMg = P·(1 − 1/|ε|)") + ". Logo "
            "P·(1 − 1/|ε|) = CMg, o que dá " + vd("(P − CMg)/P = 1/|ε|") + " — o " + azb("índice de Lerner") + " ("
            + oc("Abba Lerner") + ", 1934).",
            "Na forma de multiplicador: " + vd("P = CMg · |ε|/(|ε| − 1)") + ". Com |ε| = 2, P = 2·CMg (markup de "
            "100% sobre o custo); com |ε| = 5, P = 1,25·CMg; com |ε| → ∞ (firma competitiva), P → CMg.",
            "Intuição: demanda inelástica significa consumidor pouco sensível ao preço (poucos substitutos, bem "
            "essencial, hábito). O monopolista sobe o preço e perde poucas vendas — por isso pode cobrar margem alta.",
            "Detalhe que a banca explora: o monopolista <b>nunca</b> opera no trecho inelástico da demanda "
            "(|ε| < 1), pois ali a RMg é negativa e reduzir a quantidade aumentaria a receita e cortaria custos. "
            "“Mais inelástica” quer dizer |ε| menor, mas ainda maior que 1 no ponto escolhido.",
            "Aplicações: é a mesma lógica da " + azb("discriminação de 3º grau") + " (preço maior no grupo de "
            "demanda menos elástica) e da " + azb("regra de Ramsey") + " na tarifação de monopólios regulados "
            "(margens maiores onde a demanda é menos elástica).",
            vm("Regra-âncora: markup de Lerner = 1/|ε| — elasticidade e markup andam em sentidos opostos."),
        ],
        "dissecando": (cz("[literalidade]") + " Item que reproduz a regra de Lerner em palavras. O risco é a "
                       "inversão mental: quem associa “mais elástica” a “mais reação” pode achar que a margem cresce "
                       "com a elasticidade. Pista: elasticidade alta = concorrência próxima = margem pequena."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Num monopólio, o mark up é maior quanto mais elástica ao preço for a demanda.”</i> → ERRADO "
            "(inversão: Lerner = 1/|ε|)",
            "<i>“O monopolista maximizador de lucro pode operar no trecho inelástico da curva de demanda.”</i> → "
            "ERRADO (ali a RMg é negativa)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["quanto mais"], "dificuldade": 1,
        "comentario_fonte": "Duas respostas convergentes: (P − CMg)/P = 1/|ε|; demanda mais inelástica → |ε| "
                            "menor → markup maior; consumidores menos sensíveis permitem elevar o preço.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01759
    {
        "id": "ECO-E2-L01759-1", "fonte_ref": "E2-L01759", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_FIRMA_CUSTOS,
        "rotulo_item": "Item",
        "assertiva": ("Por possuir elevados custos fixos em laboratórios e pagamento de pesquisadores, porém baixos "
                      "custos marginais de produção após a descoberta da fórmula de uma vacina, a produção de "
                      "vacinas tende a apresentar estrutura de mercado com poder de monopólio, sujeita a patentes e "
                      "ganhos de monopólio que garantem o pagamento dos custos fixos e irrecuperáveis aos seus "
                      "produtores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Por possuir <u>elevados custos fixos</u> em laboratórios e pagamento de pesquisadores, porém "
                      "<u>baixos custos marginais</u> de produção após a descoberta da fórmula de uma vacina, a "
                      "produção de vacinas <u>tende a</u> apresentar estrutura de mercado com poder de monopólio, "
                      "sujeita a patentes e ganhos de monopólio que garantem o pagamento dos custos fixos e "
                      "irrecuperáveis aos seus produtores."),
        "poucas": ("Custo fixo e " + azb("irrecuperável") + " alto + custo marginal baixo: se o preço caísse ao CMg "
                   "(cópia livre), ninguém recuperaria a pesquisa. A " + azb("patente") + " cria monopólio "
                   "temporário para que o preço acima do CMg pague o investimento."),
        "destrinchando": [
            "Estrutura de custos da inovação: a P&amp;D é um " + azb("custo fixo e irrecuperável") + " (sunk cost) — "
            "uma vez gasto, não volta, haja ou não produção. Depois da fórmula, cada dose custa pouco: "
            + vd("CMg baixo") + " e " + vd("CMe decrescente") + ", como no monopólio natural.",
            "Problema de " + azb("apropriabilidade") + ": conhecimento é não rival e, sem proteção, pouco "
            "excludente. Com cópia livre, a concorrência levaria o preço ao CMg, abaixo do CMe, e o inovador nunca "
            "cobriria o custo da pesquisa — subinvestimento em inovação.",
            "A " + azb("patente") + " é um " + azb("monopólio legal") + " temporário (no " + rx("Brasil") + ", "
            + vd("20 anos") + " contados do depósito, pela Lei 9.279/1996, alinhada ao acordo TRIPS da OMC). O "
            "preço acima do CMg gera receita para pagar o custo fixo — e também peso morto enquanto dura a "
            "proteção.",
            "Trade-off clássico: " + azb("ineficiência estática") + " (P > CMg, menos acesso) × "
            + azb("eficiência dinâmica") + " (incentivo a novas descobertas, na linha de " + oc("Schumpeter")
            + "). Por isso a proteção é temporária e admite flexibilidades, como a licença compulsória — usada "
            "pelo " + rx("Brasil") + " em 2007 para o antirretroviral efavirenz.",
            "Atenção à nomenclatura: o item fala em “poder de monopólio” e “tende a”, não em monopólio natural "
            "estrito; o mercado de vacinas tem poucos grandes produtores, e o poder de mercado vem sobretudo da "
            "patente e da escala.",
            vm("Regra-âncora: patente = monopólio temporário que paga o custo fixo da inovação (eficiência "
               "dinâmica) ao preço de peso morto (ineficiência estática)."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item descreve a justificativa econômica "
                       "padrão das patentes, com o modulador “tende a” protegendo a generalização. O risco é o "
                       "candidato reagir ao tom (“ganhos de monopólio” soa negativo) e marcar ERRADO. 🔥 O par "
                       "patente × peso morto é recorrente: veja o item gêmeo sobre “perda líquida sempre”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como os custos marginais são baixos, a fixação do preço da vacina no custo marginal garantiria a "
            "recuperação dos custos de pesquisa.”</i> → ERRADO (P = CMg &lt; CMe não cobre o custo fixo)",
            "<i>“A patente cria um monopólio legal temporário que gera peso morto enquanto vigora.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Duas respostas convergentes: custos fixos de P&amp;D como barreira, CMg baixo após a "
                            "fórmula, patentes como monopólio legal temporário que permite recuperar os custos "
                            "irrecuperáveis e incentiva a inovação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 524", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (regulação de monopólio natural por Pc e Pr; mecanismo descrito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01760
    {
        "id": "ECO-E2-L01760-1", "fonte_ref": "E2-L01760", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_FIRMA_CUSTOS,
        "rotulo_item": "Item",
        "assertiva": ("Uma patente de medicamentos introduz um monopólio que sempre trará uma perda líquida para a "
                      "sociedade, pois os ganhos do avanço científico certamente não compensam as perdas para os "
                      "consumidores, que pagarão preços acima do custo marginal de produção, gerando peso morto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma patente de medicamentos introduz um monopólio que ") + vm("sempre trará uma perda líquida")
                   + az(" para a sociedade, pois os ganhos do avanço científico ") + vm("certamente não compensam")
                   + az(" as perdas para os consumidores, que pagarão preços acima do custo marginal de produção, "
                        "gerando peso morto."),
        "poucas": ("O peso morto da patente é real, mas o saldo social é um " + azb("trade-off") + ": sem a "
                   "proteção, muitos medicamentos nem existiriam. “Sempre” e “certamente” transformam uma questão "
                   "empírica em certeza."),
        "destrinchando": [
            azb("Perda estática") + ": durante a patente, o laboratório é monopolista, cobra P > CMg e restringe a "
            "quantidade. Pacientes dispostos a pagar acima do custo de fabricação ficam sem o remédio — "
            + azb("peso morto") + ". Essa parte do item está correta.",
            azb("Ganho dinâmico") + ": o desenvolvimento de um medicamento envolve custos de P&amp;D enormes e "
            "irrecuperáveis. Sem a perspectiva de lucro de monopólio, a cópia imediata levaria o preço ao CMg e "
            "ninguém investiria. O excedente gerado por um remédio novo (que antes não existia) pode superar em "
            "muito o peso morto do período protegido.",
            "O saldo depende de parâmetros: duração e amplitude da patente, elasticidade da demanda, custo da "
            "pesquisa, existência de substitutos. A teoria do " + azb("desenho ótimo de patentes") + " ("
            + oc("Nordhaus") + ", 1969) busca justamente o prazo que equilibra incentivo e peso morto.",
            "Instrumentos que reduzem a perda sem destruir o incentivo: prazo limitado (" + vd("20 anos") + " no "
            "TRIPS), " + azb("licença compulsória") + " em emergências de saúde pública, compras governamentais em "
            "grande escala, prêmios à inovação e entrada de genéricos após a expiração.",
            vm("Regra-âncora: patente = peso morto estático × inovação dinâmica; o saldo é empírico, nunca "
               "“sempre”."),
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " A parte final (P > CMg, peso morto) é verdadeira "
                       "e dá credibilidade; o erro está nos absolutos “sempre” e “certamente”, que negam o ganho "
                       "dinâmico. 🔥 Em economia, “sempre” e “certamente” sobre saldo de bem-estar quase sempre "
                       "indicam ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Durante sua vigência, a patente de medicamentos permite preços acima do custo marginal, gerando "
            "peso morto.”</i> → CERTO",
            "<i>“A patente de medicamentos é eficiente do ponto de vista estático, pois iguala o preço ao custo "
            "marginal.”</i> → ERRADO (a ineficiência estática é justamente P > CMg)",
        ])],
        "reescrita": ("Uma patente de medicamentos introduz um monopólio que " + hl("pode trazer") + " uma perda "
                      "líquida para a sociedade " + hl("se") + " os ganhos do avanço científico não "
                      + hl("compensarem") + " as perdas para os consumidores, que pagarão preços acima do custo "
                      "marginal de produção, gerando peso morto."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["sempre", "certamente"], "dificuldade": 1,
        "comentario_fonte": "Duas respostas convergentes: o erro está em “sempre” e “certamente”; patentes "
                            "envolvem trade-off entre perda estática (peso morto) e ganho dinâmico (incentivo à "
                            "inovação).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00018
    {
        "id": "ECO-E3-L00018-1", "fonte_ref": "E3-L00018", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("No que se refere a estruturas de mercado, cadeias e redes produtivas, competitividade e "
                    "estratégia empresarial, julgue o item seguinte."),
        "rotulo_item": "Item",
        "assertiva": ("Empresas com poder de mercado buscam capturar o excedente do consumidor por meio de "
                      "estratégias de diferenciação de preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Empresas com <u>poder de mercado</u> buscam capturar o excedente do consumidor por meio de "
                      "estratégias de <u>diferenciação de preços</u>."),
        "poucas": ("“Diferenciação de preços” = " + azb("discriminação de preços") + ": cobrar valores distintos "
                   "conforme a disposição a pagar, convertendo " + vd("excedente do consumidor em lucro") + ". Só é "
                   "possível com poder de mercado."),
        "destrinchando": [
            "Com preço único, o monopolista deixa excedente com todo consumidor que pagaria mais que o preço. "
            "Discriminar é a forma de se apropriar dessa diferença.",
            "Três graus (classificação de " + oc("Pigou") + ", 1920): " + azb("1º grau") + " — preço de reserva de "
            "cada um, captura todo o EC; " + azb("2º grau") + " — menus, pacotes, descontos por quantidade, em que o "
            "consumidor se autosseleciona; " + azb("3º grau") + " — grupos observáveis (estudantes, idosos, "
            "regiões), com preço maior para a demanda menos elástica.",
            "Condições: (i) " + azb("poder de mercado") + " — a firma competitiva é tomadora de preço e não "
            "discrimina; (ii) capacidade de " + azb("segmentar") + " os consumidores; (iii) impedir a "
            + azb("revenda") + " (arbitragem) entre quem paga barato e quem paga caro.",
            "Exemplos: passagens aéreas (antecedência, tarifas flexíveis), meia-entrada, cupons, planos de "
            "telefonia e streaming, precificação por região em plataformas digitais.",
            vm("Regra-âncora: discriminação de preços = conversão de excedente do consumidor em lucro; exige poder "
               "de mercado, segmentação e ausência de revenda."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item usa “diferenciação de preços” no lugar do termo técnico "
                       "“discriminação”. O risco é confundir com " + azb("diferenciação de produto") + " (a marca da "
                       "concorrência monopolística), que também gera poder de mercado, mas não é o mecanismo de "
                       "captura de excedente descrito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Empresas em concorrência perfeita podem capturar o excedente do consumidor por meio de "
            "discriminação de preços.”</i> → ERRADO (tomadora de preço não discrimina)",
            "<i>“A discriminação de preços de primeiro grau converte todo o excedente do consumidor em "
            "excedente do produtor.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Seis respostas convergentes: firmas com poder de mercado usam discriminação de preços "
                            "(1º, 2º e 3º graus) para extrair excedente do consumidor; exige segmentação e "
                            "limitação da revenda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00157
    {
        "id": "ECO-E3-L00157-1", "fonte_ref": "E3-L00157", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": COM_ANTT,
        "rotulo_item": "Item",
        "assertiva": ("A administração de uma rodovia federal sob concessão é um monopólio, pois tem apenas um "
                      "provedor do serviço, apesar de ser livre a entrada de concorrentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A administração de uma rodovia federal sob concessão é um monopólio, pois tem apenas um "
                      "provedor do serviço, ") + vm("apesar de ser livre a entrada de concorrentes") + az("."),
        "poucas": ("Monopólio pressupõe " + azb("barreiras à entrada") + ". Na rodovia concedida, elas são legais "
                   "(o contrato dá exclusividade) e econômicas (ninguém duplica uma estrada): a entrada "
                   "<b>não</b> é livre."),
        "destrinchando": [
            "Monopólio = um único vendedor, sem substitutos próximos e com " + azb("barreiras à entrada") + ". "
            "Sem barreiras, lucros extraordinários atrairiam concorrentes e o monopólio não se sustentaria. Por "
            "isso “monopólio com entrada livre” é contradição em termos.",
            "Fontes de barreiras: (i) " + azb("legais") + " — concessão exclusiva, patentes, licenças; (ii) "
            + azb("controle de insumo essencial") + "; (iii) " + azb("economias de escala") + " que tornam um "
            "único produtor mais barato (monopólio natural); (iv) custos irrecuperáveis elevados.",
            "Na " + rx("rodovia federal concedida") + " (contratos da " + rx("ANTT") + "), duas barreiras se somam: "
            "a jurídica (a concessionária detém por contrato a exploração daquele trecho) e a técnica (a estrada "
            "é infraestrutura de rede, com custo fixo enorme e custo marginal baixo — traço de "
            + azb("monopólio natural") + ").",
            "Por isso a tarifa de pedágio é fixada no leilão e corrigida pelo contrato, com regras de reajuste e "
            "revisão: o regulador substitui a disciplina que a concorrência não oferece. A competição possível é "
            + azb("pelo mercado") + " (no leilão), não " + azb("no mercado") + ".",
            "Concorrência indireta existe (outras rodovias, ferrovia, transporte aéreo), mas são substitutos "
            "imperfeitos e não anulam a barreira na exploração daquele trecho.",
            vm("Regra-âncora: sem barreira à entrada não há monopólio duradouro."),
        ],
        "dissecando": (cz("[contradição · meia-verdade]") + " A 1ª parte (monopólio, um só provedor) está certa; o "
                       "erro foi enxertado na concessiva “apesar de ser livre a entrada”, que contradiz o próprio "
                       "conceito de monopólio e a natureza da concessão. Pista: “sob concessão” já anuncia barreira "
                       "legal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A administração de uma rodovia federal sob concessão configura monopólio, sustentado por barreira "
            "legal à entrada de concorrentes.”</i> → CERTO",
            "<i>“Em mercados contestáveis, a ameaça de entrada disciplina o monopolista mesmo sem concorrentes "
            "efetivos.”</i> → CERTO",
        ])],
        "reescrita": ("A administração de uma rodovia federal sob concessão é um monopólio, pois tem apenas um "
                      "provedor do serviço" + hl(" e não há livre") + " entrada de concorrentes."),
        "tipo_erro": ["CONTRADICAO", "MEIA_VERDADE"], "moduladores": ["apesar de"], "dificuldade": 1,
        "comentario_fonte": "Monopólio puro sem possibilidade de entrada; a concessão é barreira legal e duplicar "
                            "a infraestrutura é inviável. Uma das respostas fala em “ferrovia” e chama a concessão de "
                            "“monopólio natural devido à permissão do governo”, confundindo barreira legal com "
                            "monopólio natural.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 167", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "absorvida (características do monopólio e barreiras à entrada no 📖)"},
                          {"ref": "IMAGEM 168", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (quadro comparativo de estruturas, ilegível na transcrição)"}],
        "alertas": ["qualidade_fonte: uma resposta da fonte chama a concessão de monopólio natural por causa da "
                    "permissão do governo (barreira legal ≠ monopólio natural) e troca rodovia por ferrovia — "
                    "corrigido"],
    },
]
