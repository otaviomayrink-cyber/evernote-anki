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
    # ------------------------------------------------------------------ E3-L00176
    {
        "id": "ECO-E3-L00176-1", "fonte_ref": "E3-L00176", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": "Acerca da teoria da regulação e das estruturas de mercado, julgue o item subsequente.",
        "rotulo_item": "Item",
        "assertiva": ("Na regulação de um monopólio natural relativo à prestação de um serviço público, a eficiência "
                      "econômica pode ser obtida por meio da fixação do preço da prestação do serviço em patamar "
                      "equivalente ao seu custo marginal de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Na regulação de um monopólio natural relativo à prestação de um serviço público, ")
                   + vm("a eficiência econômica") + az(" pode ser obtida por meio da fixação do preço da prestação "
                   "do serviço em patamar equivalente ao seu ") + vm("custo marginal") + az(" de produção."),
        "poucas": ("No monopólio natural " + vd("CMg < CMe") + ": com P = CMg a firma tem " + azb("prejuízo")
                   + " e, sem subsídio, sai do mercado. A regulação viável fixa o preço no " + azb("custo médio")
                   + " (lucro zero) — foi essa a leitura da banca."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "No sentido estrito, P = CMg é a condição de " + azb("eficiência alocativa") + " (o "
                          "“primeiro melhor”), e o “pode ser obtida” admitiria essa solução se acompanhada de "
                          "subsídio ou de tarifa em duas partes. O ERRADO se sustenta na leitura de “eficiência "
                          "econômica” como resultado sustentável da regulação: sem cobrir o custo médio, o serviço "
                          "não se mantém. Em prova, siga a banca: monopólio natural + P = CMg → prejuízo → ERRADO.")],
        "destrinchando": [
            azb("Monopólio natural") + ": custo fixo altíssimo e custo marginal baixo fazem o " + vd("CMe cair") + " "
            "em toda a faixa relevante. Se a média cai, a unidade marginal custa menos que a média: "
            + vd("CMg < CMe") + ".",
            "Três regimes possíveis: (1) " + azb("sem regulação") + " — RMg = CMg, preço alto, quantidade baixa, "
            "peso morto; (2) " + azb("P = CMg") + " — quantidade eficiente, mas P &lt; CMe: prejuízo igual a "
            "(CMe − CMg) × q, que exige subsídio público; (3) " + azb("P = CMe") + " — lucro econômico zero, "
            "firma viável, quantidade menor que a eficiente e algum peso morto (" + azb("segundo melhor") + ").",
            "Por isso a regulação de serviços públicos em monopólio natural costuma ancorar a tarifa no custo "
            "médio (custo de serviço, com remuneração do capital) ou em " + azb("price cap") + " revisto "
            "periodicamente. Outras saídas para chegar perto do CMg sem prejuízo: " + azb("tarifa em duas partes")
            + " (assinatura cobre o custo fixo, tarifa por uso = CMg) e " + azb("preços de Ramsey") + " (margens "
            "maiores onde a demanda é menos elástica).",
            "No " + rx("Brasil") + ", agências como " + rx("ANTT") + ", ANEEL e ANTAQ fazem esse papel em concessões "
            "de rodovias, ferrovias, energia e portos; a competição se dá " + azb("pelo mercado") + " (leilão pela "
            "menor tarifa ou maior outorga).",
            vm("Regra-âncora: monopólio natural → P = CMg dá prejuízo; regulação viável → P = CMe."),
        ],
        "grafico_verso": "ECO-E3-L00176-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item aplica ao monopólio natural a regra de eficiência válida "
                       "para firmas com custos crescentes (P = CMg), ignorando que ali o CMg está abaixo do CMe. A "
                       "palavra-gatilho é “monopólio natural”: ela anuncia custo médio decrescente. 🔥 A CEBRASPE "
                       "cobra o dilema P = CMg × P = CMe com frequência em provas de agências reguladoras."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, a fixação do preço no custo marginal exige subsídio para que a firma "
            "permaneça no mercado.”</i> → CERTO",
            "<i>“No monopólio natural, a fixação do preço no custo médio elimina o peso morto.”</i> → ERRADO "
            "(reduz, mas P = CMe > CMg mantém algum peso morto)",
        ])],
        "reescrita": ("Na regulação de um monopólio natural relativo à prestação de um serviço público, "
                      + hl("a solução viável, com lucro econômico nulo e sem subsídio,") + " pode ser obtida por meio "
                      "da fixação do preço da prestação do serviço em patamar equivalente ao seu "
                      + hl("custo médio") + " de produção."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": "Várias respostas convergentes: em monopólio natural CMg < CMe; com P = CMg a firma "
                            "opera com prejuízo e precisaria de subsídio; regulação usual pelo custo médio. Gráfico "
                            "com LRAC, LRMC, MR e demanda (Pu, Qu, Pc, Qe).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 222", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00176-1-V1)"},
                          {"ref": "IMAGEM 223", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (regulação P = CMg em monopólio comum; absorvida no 📖)"},
                          {"ref": "IMAGEM 230", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo mecanismo de ECO-E3-L00176-1-V1)"},
                          {"ref": "IMAGEM 224-229, 231-236", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas"}],
        "alertas": ["contestavel: P = CMg é a condição de eficiência alocativa (primeiro melhor) e o “pode” "
                    "admitiria a solução com subsídio; gabarito ERRADO da fonte mantido pela leitura de viabilidade "
                    "(CMg < CMe gera prejuízo)"],
    },
    # ------------------------------------------------------------------ E3-L00200
    {
        "id": "ECO-E3-L00200-1", "fonte_ref": "E3-L00200", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": "No que se refere à intervenção pública no equilíbrio dos mercados, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em condições de monopólio, a imposição de um imposto sobre os lucros irá acarretar aumento "
                      "do preço e queda da quantidade produzida pela firma monopolista."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em condições de monopólio, a imposição de um imposto sobre os lucros ")
                   + vm("irá acarretar aumento do preço e queda da quantidade produzida") + az(" pela firma "
                   "monopolista."),
        "poucas": ("Um imposto proporcional sobre o " + azb("lucro econômico") + " não muda RMg nem CMg: o q que "
                   "maximiza π também maximiza (1 − t)·π. " + vd("Preço e quantidade não mudam") + "; só cai o "
                   "lucro líquido."),
        "destrinchando": [
            "O monopolista escolhe q onde " + azb("RMg = CMg") + " e lê o preço na demanda. Um imposto à alíquota t "
            "sobre o lucro transforma o objetivo em (1 − t)·π(q). Multiplicar uma função por uma constante "
            "positiva não muda o ponto de máximo: a condição de primeira ordem continua (1 − t)·(RMg − CMg) = 0.",
            "Por isso o imposto sobre lucro puro é " + azb("neutro") + " (não distorce a decisão marginal) e "
            "transfere renda de monopólio para o governo " + vd("sem peso morto adicional") + ". É um argumento "
            "clássico a favor de tributar rendas econômicas.",
            "Contraste com " + azb("impostos sobre a produção ou as vendas") + " (específico por unidade ou ad "
            "valorem): eles entram no custo marginal (ou reduzem a RMg líquida), o ótimo se desloca para "
            + vd("q menor e P maior") + " — o efeito que o item atribui ao imposto sobre lucro. Um "
            + azb("imposto fixo") + " (lump-sum) também não altera P e q no curto prazo, desde que a firma "
            "continue operando.",
            "Ressalva de manual: a neutralidade vale para o lucro <b>econômico</b>. Tributos sobre o lucro "
            "<b>contábil</b>, que não deduzem o custo de oportunidade do capital, podem afetar decisões de "
            "investimento e de longo prazo (como IRPJ e CSLL na prática).",
            vm("Regra-âncora: imposto sobre lucro → P e q inalterados; imposto por unidade → P ↑ e q ↓."),
        ],
        "grafico_verso": "ECO-E3-L00200-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item atribui ao imposto sobre o lucro o efeito típico do "
                       "imposto sobre a quantidade. O “irá acarretar” dá tom de certeza a um resultado que só vale "
                       "para tributos que mexem na margem. Pista: pergunte se o imposto altera RMg ou CMg; se não "
                       "altera, nada muda no ponto ótimo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em condições de monopólio, um imposto específico por unidade vendida tende a elevar o preço e "
            "reduzir a quantidade produzida.”</i> → CERTO",
            "<i>“Um imposto de montante fixo sobre o monopolista reduz a quantidade ofertada no curto prazo.”</i> → "
            "ERRADO (custo fixo não altera o CMg)",
        ])],
        "reescrita": ("Em condições de monopólio, a imposição de um imposto sobre os lucros " + hl("não altera o "
                      "preço nem a quantidade produzida") + " pela firma monopolista" + hl(", reduzindo apenas o "
                      "lucro líquido") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["irá"], "dificuldade": 2,
        "comentario_fonte": "Imposto sobre lucro econômico puro é neutro: o Q que maximiza 100% do lucro maximiza "
                            "70% dele; impostos sobre vendas aumentam o CMg e elevam P; gráfico de monopólio com "
                            "área de lucro.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 260", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repete a assertiva)"},
                          {"ref": "IMAGEM 261", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo redesenhado em ECO-E3-L00200-1-V1)"},
                          {"ref": "IMAGEM 262", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (condição de primeira ordem no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00230
    {
        "id": "ECO-E3-L00230-1", "fonte_ref": "E3-L00230", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": COM_DISCRIM,
        "rotulo_item": "Item",
        "assertiva": ("Diferente da discriminação perfeita de primeiro grau, a aplicação da discriminação de preços "
                      "de segundo grau pressupõe que a empresa não consiga identificar diretamente as demandas "
                      "individuais dos consumidores antes das compras."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Diferente da discriminação perfeita de primeiro grau, a aplicação da discriminação de preços "
                      "de segundo grau pressupõe que a empresa <u>não consiga identificar diretamente</u> as "
                      "demandas individuais dos consumidores antes das compras."),
        "poucas": ("No 2º grau a firma " + azb("não observa") + " quem é quem: oferece um menu (preços por "
                   "quantidade, pacotes, versões) e deixa o consumidor se " + azb("autosselecionar") + ". No 1º "
                   "grau, ela conhece a disposição a pagar de cada um."),
        "destrinchando": [
            "Classificação de " + oc("Pigou") + " (1920) pelo tipo de informação: " + azb("1º grau") + " — a firma "
            "conhece o preço de reserva de cada consumidor e cobra exatamente esse valor; " + azb("2º grau")
            + " — a firma não distingue os consumidores e cobra preços diferentes por " + vd("quantidade ou "
            "versão") + "; " + azb("3º grau") + " — a firma identifica " + vd("grupos") + " por característica "
            "observável (idade, estudante, região) e cobra um preço por grupo.",
            "No 2º grau o preço depende do <b>que</b> se compra, não de <b>quem</b> compra: todos enfrentam o "
            "mesmo menu (“pague 2, leve 3”, tarifa em blocos de energia, plano básico × premium, primeira classe × "
            "econômica). Quem valoriza mais escolhe a opção desenhada para ele.",
            "É um problema de " + azb("informação assimétrica") + " (" + azb("screening") + "): o menu precisa ser "
            "compatível com incentivos — cada tipo deve preferir o pacote pensado para si. Por isso a firma deixa "
            "algum excedente com os consumidores de alta disposição a pagar (renda informacional) e distorce a "
            "oferta ao tipo baixo.",
            "Consequência: o 2º grau captura apenas parte do excedente; o 1º grau, todo ele.",
            vm("Regra-âncora: 1º grau = sabe quem é cada um; 2º grau = não sabe e oferece menu; 3º grau = sabe o "
               "grupo."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item define o 2º grau pelo contraste informacional com o 1º, "
                       "sem citar o mecanismo (menu, quantidade). O risco é confundir com o 3º grau, em que a firma "
                       "identifica grupos — mas nem ali enxerga a demanda individual."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação de terceiro grau, a empresa identifica diretamente a disposição a pagar de cada "
            "consumidor.”</i> → ERRADO (identifica grupos, não indivíduos)",
            "<i>“Descontos por quantidade e tarifas em blocos são exemplos de discriminação de segundo grau.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Várias respostas convergentes: 1º grau = preço de reserva individual; 2º grau = "
                            "autosseleção por menu (quantidade, versões) porque a firma não observa o tipo; 3º grau "
                            "= segmentação por grupos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 318", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00231
    {
        "id": "ECO-E3-L00231-1", "fonte_ref": "E3-L00231", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_DISCRIM,
        "rotulo_item": "Item",
        "assertiva": ("A condição para o sucesso da discriminação de preços de segundo grau, por meio de descontos "
                      "de acordo com a quantidade adquirida, é a de que os consumidores que compram grandes "
                      "quantidades tenham demandas relativamente mais elásticas do que os consumidores que compram "
                      "pequenas quantidades."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A condição para o sucesso da discriminação de preços de segundo grau, por meio de descontos "
                      "de acordo com a quantidade adquirida, é a de que os consumidores que compram grandes "
                      "quantidades tenham demandas relativamente <u>mais elásticas</u> do que os consumidores que "
                      "compram pequenas quantidades."),
        "poucas": ("Pela lógica do markup inverso, preço unitário menor (desconto) vai para quem é " + azb("mais "
                   "sensível ao preço") + ". Se os grandes compradores fossem inelásticos, dar-lhes desconto só "
                   "reduziria a receita."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A justificativa é a da regra de " + oc("Lerner") + " aplicada a segmentos; na teoria do "
                          + azb("preço não linear") + " (menus de autosseleção), o grande comprador costuma ser o "
                          "de <b>maior</b> disposição a pagar, e o desconto marginal serve para induzir a "
                          "autosseleção, não por ele ser “mais elástico”. Uma das respostas da fonte marca ERRADO "
                          "por isso. Mantido o CERTO da fonte, que segue a formulação dos manuais introdutórios.")],
        "destrinchando": [
            "Princípio geral da discriminação: " + vd("(P − CMg)/P = 1/|ε|") + " em cada segmento. Preço mais alto "
            "onde a demanda é menos elástica; mais baixo onde é mais elástica.",
            "No desconto por quantidade (" + azb("2º grau") + "), o preço por unidade cai nas unidades adicionais. "
            "Faz sentido oferecer esse desconto quando quem compra muito reage ao preço: revendedores, empresas, "
            "consumidores que planejam e comparam. A redução de preço é compensada pelo aumento do volume.",
            "Quem compra pouco (compra por conveniência, urgência, sem comparar) tende a ser menos sensível ao "
            "preço e paga o preço cheio por unidade.",
            "Outra forma de ver o 2º grau: a firma não sabe quem é cada consumidor e desenha um " + azb("menu")
            + " (tarifa em blocos, embalagem família × individual) para que cada tipo escolha a opção pensada "
            "para ele (" + azb("compatibilidade de incentivos") + ").",
            vm("Regra-âncora: desconto (preço menor) vai para a demanda mais elástica; preço cheio para a menos "
               "elástica."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item aplica a regra do markup inverso ao desconto por "
                       "quantidade. A armadilha está em pensar que quem compra muito “precisa” do bem (inelástico) "
                       "e por isso pagaria mais. 🔥 Itens de discriminação quase sempre se decidem pela relação "
                       "preço maior ↔ demanda menos elástica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação de terceiro grau, o preço mais alto é cobrado do grupo com demanda mais "
            "elástica.”</i> → ERRADO (inversão: vai para o menos elástico)",
            "<i>“Na discriminação de segundo grau, o preço unitário depende da quantidade adquirida, e não da "
            "identidade do comprador.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": "Quatro respostas CERTO (desconto para quem é mais sensível ao preço; volume compensa a "
                            "redução) e uma ERRADO (grandes compradores teriam demanda menos elástica, com maior "
                            "valorização das unidades adicionais).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 319", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["contestavel: respostas da fonte divergem (4 CERTO × 1 ERRADO); na teoria do preço não linear o "
                    "grande comprador costuma ter maior disposição a pagar — mantido o CERTO da fonte"],
    },
    # ------------------------------------------------------------------ E3-L00232
    {
        "id": "ECO-E3-L00232-1", "fonte_ref": "E3-L00232", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_DISCRIM,
        "rotulo_item": "Item",
        "assertiva": ("Quando o monopolista faz discriminação de preços de primeiro grau, a alocação final de mercado "
                      "não é uma solução ótima no sentido de Pareto, pois os consumidores perdem todo seu excedente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando o monopolista faz discriminação de preços de primeiro grau, a alocação final de mercado ")
                   + vm("não é") + az(" uma solução ótima no sentido de Pareto, ") + vm("pois")
                   + az(" os consumidores perdem todo seu excedente."),
        "poucas": ("A discriminação perfeita leva a produção até " + vd("P = CMg") + ": sem peso morto, a alocação "
                   "<b>é</b> " + azb("Pareto-ótima") + ". Os consumidores perdem o excedente, mas isso é questão de "
                   "distribuição, não de eficiência."),
        "destrinchando": [
            azb("Ótimo de Pareto") + ": alocação em que não se pode melhorar ninguém sem piorar alguém. O critério "
            "é cego à distribuição — uma alocação em que um agente fica com tudo pode ser Pareto-ótima.",
            "Na " + azb("discriminação de 1º grau") + ", cada unidade é vendida pelo preço de reserva do comprador. "
            "A RMg coincide com a demanda, e o monopolista produz até o CMg cruzar a demanda: a "
            + vd("quantidade de concorrência perfeita") + ", maior que a do monopólio de preço único.",
            "Toda troca que gera valor acima do custo acontece: " + vd("peso morto = 0") + ", excedente total "
            "máximo. Há uma transferência integral (" + vd("EC = 0") + ", lucro = excedente total), mas nenhuma "
            "perda líquida.",
            "Paradoxo útil: em termos de eficiência, a discriminação perfeita é <b>melhor</b> que o monopólio de "
            "preço único; em termos distributivos, é pior para o consumidor.",
            vm("Regra-âncora: perder excedente (distribuição) ≠ alocação ineficiente (Pareto)."),
        ],
        "dissecando": (cz("[nexo indevido · inversão]") + " O fato citado é verdadeiro (EC = 0), mas não sustenta a "
                       "conclusão: o “pois” cria um nexo entre distribuição e eficiência que não existe. Pista: "
                       "sempre que o item justificar ineficiência com “o consumidor perde excedente”, verifique se há "
                       "peso morto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação de primeiro grau, a alocação é Pareto-ótima, embora os consumidores percam todo o "
            "excedente.”</i> → CERTO",
            "<i>“A discriminação de terceiro grau sempre elimina o peso morto do monopólio.”</i> → ERRADO "
            "(efeito ambíguo; só o 1º grau garante)",
        ])],
        "reescrita": ("Quando o monopolista faz discriminação de preços de primeiro grau, a alocação final de mercado "
                      + hl("é") + " uma solução ótima no sentido de Pareto, " + hl("embora") + " os consumidores "
                      "percam todo seu excedente."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": ["pois"], "dificuldade": 2,
        "comentario_fonte": "Mini-aula: eficiência de Pareto não se confunde com equidade; na discriminação perfeita "
                            "cada unidade é vendida ao preço de reserva, q vai até CMg = demanda, sem peso morto; "
                            "a alocação é Pareto-eficiente.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 320", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (texto sobre Pareto absorvido no 📖)"},
                          {"ref": "IMAGEM 321", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (texto absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00233
    {
        "id": "ECO-E3-L00233-1", "fonte_ref": "E3-L00233", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_DISCRIM,
        "rotulo_item": "Item",
        "assertiva": ("Na discriminação de preços de terceiro grau, o preço mais elevado será cobrado dos "
                      "consumidores com demanda mais elástica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na discriminação de preços de terceiro grau, o preço mais elevado será cobrado dos "
                      "consumidores com demanda ") + vm("mais elástica") + az("."),
        "poucas": ("O monopolista iguala a RMg dos grupos e aplica " + vd("(P − CMg)/P = 1/|ε|") + " em cada um: "
                   "o " + azb("preço mais alto") + " vai para o grupo de demanda " + azb("menos elástica") + "."),
        "destrinchando": [
            azb("3º grau") + ": a firma separa o mercado em grupos identificáveis (estudantes × demais, turistas × "
            "executivos, mercado interno × externo) e cobra um preço por grupo.",
            "Condição de ótimo: " + vd("RMg₁ = RMg₂ = CMg") + ". Se a RMg de um grupo fosse maior, valeria a pena "
            "deslocar vendas para ele. Como RMg = P·(1 − 1/|ε|), igualar as RMg exige " + vd("P₁·(1 − 1/|ε₁|) = "
            "P₂·(1 − 1/|ε₂|)") + ": o grupo com |ε| menor tem de ter P maior.",
            "Intuição: quem tem poucas alternativas (executivo que precisa viajar amanhã) aceita pagar mais; quem "
            "pode desistir ou trocar (turista com datas flexíveis, estudante) só compra com preço baixo. Exemplo "
            "numérico: CMg = 10, |ε₁| = 2 → P₁ = 20; |ε₂| = 4 → P₂ ≈ 13,3.",
            "Requisitos: segmentação observável e ausência de revenda entre os grupos (meia-entrada exige "
            "carteirinha; passagem é nominal).",
            vm("Regra-âncora: preço alto ↔ demanda inelástica; preço baixo ↔ demanda elástica."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte a regra do markup inverso. A armadilha é associar "
                       "“elástica” a “aguenta variação” e, daí, a “aguenta preço alto”. Pista: elasticidade alta = "
                       "consumidor que foge do aumento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação de terceiro grau, o monopolista iguala as receitas marginais dos diferentes "
            "grupos ao custo marginal.”</i> → CERTO",
            "<i>“Na discriminação de terceiro grau, o monopolista iguala os preços dos grupos ao custo "
            "marginal.”</i> → ERRADO (iguala as RMg, não os preços)",
        ])],
        "reescrita": ("Na discriminação de preços de terceiro grau, o preço mais elevado será cobrado dos "
                      "consumidores com demanda " + hl("menos elástica") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Várias respostas convergentes: regra da elasticidade inversa; preço maior para a "
                            "demanda mais inelástica (executivos), menor para a elástica (turistas, estudantes); "
                            "RMg iguais entre mercados.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00304
    {
        "id": "ECO-E3-L00304-1", "fonte_ref": "E3-L00304", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": ("Sobre os diferentes tipos de bens, as falhas de mercado e o papel do Estado no ajuste da oferta "
                    "e correções de problemas decorrentes da livre flutuação dos mercados, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Numa situação de monopólio natural, caso a empresa opere em um nível em que o preço de mercado "
                      "se iguale ao custo marginal, ela poderia ofertar uma quantidade eficiente de bens, mas não "
                      "seria capaz de cobrir seus custos médios. Por isso, argumenta-se em favor da estatização dos "
                      "bens e serviços que apresentam esta característica, uma vez que a privatização envolve um "
                      "custo de negociação e regulamentação que pode ser evitado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Numa situação de monopólio natural, caso a empresa opere em um nível em que o preço de "
                      "mercado se iguale ao custo marginal, ela poderia ofertar uma quantidade eficiente de bens, mas "
                      "<u>não seria capaz de cobrir seus custos médios</u>. Por isso, <u>argumenta-se</u> em favor da "
                      "estatização dos bens e serviços que apresentam esta característica, uma vez que a "
                      "privatização envolve um custo de negociação e regulamentação que pode ser evitado."),
        "poucas": ("Com " + vd("CMg < CMe") + ", P = CMg é eficiente mas dá prejuízo. Uma das respostas ao dilema é "
                   "a " + azb("provisão estatal") + " (o Estado absorve o prejuízo e evita custos de contratar e "
                   "regular um operador privado). O item diz “argumenta-se”: descreve um argumento, não o "
                   "endossa como único."),
        "destrinchando": [
            "1ª frase — o dilema: no " + azb("monopólio natural") + " o CMe é decrescente, logo o CMg fica abaixo "
            "dele. P = CMg gera a quantidade eficiente (" + azb("eficiência alocativa") + "), mas a receita "
            "(P × q) não cobre o custo total (CMe × q).",
            "Respostas possíveis: (i) " + azb("P = CMe") + " — empresa viável, lucro zero, algum peso morto; "
            "(ii) " + azb("P = CMg com subsídio") + " — eficiente, mas financiado por tributos que também "
            "distorcem; (iii) " + azb("tarifa em duas partes") + "; (iv) " + azb("estatização") + " — o Estado "
            "produz, pode praticar P = CMg e cobre o déficit pelo orçamento.",
            "2ª frase — o argumento a favor da estatização vem da " + azb("economia dos custos de transação") + " ("
            + oc("Coase") + ", " + oc("Williamson") + "): concessões exigem contratos complexos, agências, "
            "fiscalização, revisões tarifárias; há " + azb("assimetria de informação") + " sobre custos, risco de "
            + azb("captura") + " do regulador e de " + azb("hold-up") + ". Internalizar a atividade no Estado "
            "evitaria esses custos.",
            "Contrapontos (por isso o “argumenta-se”): estatais têm problemas de agência, uso político de tarifas "
            "e " + azb("restrição orçamentária branda") + " (" + oc("Kornai") + "). O " + rx("Brasil") + " "
            "alternou os modelos: estatais no setor elétrico e de telecomunicações até os anos 1990, depois "
            "privatizações e concessões reguladas (ANEEL, Anatel, ANTT).",
            vm("Regra-âncora: monopólio natural → P = CMg dá prejuízo → subsídio, P = CMe, tarifa em duas partes "
               "ou estatização."),
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " A 1ª frase é a definição técnica do dilema; a "
                       "2ª apresenta um argumento com “argumenta-se”, que protege o item de ser lido como "
                       "prescrição. Quem acha que “privatizar é sempre melhor” marca ERRADO por ideologia. O que se "
                       "julga é se o argumento existe e é coerente — e é."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, a fixação do preço no custo marginal permite à empresa cobrir integralmente "
            "seus custos médios.”</i> → ERRADO (CMg &lt; CMe gera prejuízo)",
            "<i>“A teoria econômica demonstra que a estatização é sempre a solução mais eficiente para monopólios "
            "naturais.”</i> → ERRADO (modulador absoluto: há custos de agência na estatal)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["argumenta-se", "poderia"],
        "dificuldade": 2,
        "comentario_fonte": "Respostas extensas e convergentes: CMe decrescente, CMg < CMe, P = CMg gera prejuízo; "
                            "soluções (P = CMe, subsídio, estatização); argumento de custos de transação "
                            "(Coase, Williamson) a favor da estatização e contrapontos (agência, captura, Kornai).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 407", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (definição e características do monopólio natural)"},
                          {"ref": "IMAGEM 408", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico de monopólio natural; mecanismo descrito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00411
    {
        "id": "ECO-E3-L00411-1", "fonte_ref": "E3-L00411", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": ("Considerando a relação entre o Estado e diferentes estruturas de mercado existentes numa "
                    "economia mista, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O monopólio natural é uma situação onde um único fornecedor pode atender toda a demanda de "
                      "mercado a um custo inferior do que dois ou mais concorrentes e, portanto, é capaz de "
                      "maximizar a eficiência econômica cobrando baixos preços sem que haja necessidade de "
                      "intervenção estatal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O monopólio natural é uma situação onde um único fornecedor pode atender toda a demanda de "
                      "mercado a um custo inferior do que dois ou mais concorrentes e, portanto, ")
                   + vm("é capaz de maximizar a eficiência econômica cobrando baixos preços sem que haja "
                        "necessidade de intervenção estatal") + az("."),
        "poucas": ("A definição está certa; a conclusão, não. Custo baixo não vira preço baixo: o monopolista "
                   "natural " + azb("maximiza lucro") + " (RMg = CMg, P > CMg) e gera peso morto. Daí a "
                   + azb("regulação") + "."),
        "destrinchando": [
            "1ª parte, correta: no " + azb("monopólio natural") + " há " + azb("economias de escala") + " em toda "
            "a faixa relevante; um só produtor atende o mercado a custo médio menor que vários "
            "(" + azb("eficiência produtiva") + ").",
            "O salto indevido: eficiência produtiva (produzir barato) não implica " + azb("eficiência alocativa")
            + " (produzir a quantidade em que P = CMg). Sem concorrência nem regulação, a firma escolhe a "
            "quantidade de monopólio: preço alto, produção restrita, " + azb("peso morto") + ". O ganho de custo "
            "fica com o produtor como lucro.",
            "Por isso monopólios naturais são, em regra, " + azb("regulados") + " (tarifa, metas de qualidade e "
            "investimento, revisão periódica) ou providos pelo Estado. A intervenção não elimina o monopólio — "
            "que é desejável pela escala —, mas disciplina o preço.",
            "Exceção teórica: a " + azb("teoria dos mercados contestáveis") + " (" + oc("Baumol, Panzar e Willig")
            + ", 1982) mostra que, sem custos irrecuperáveis, a ameaça de entrada levaria o monopolista a cobrar "
            "P = CMe. Mas infraestrutura de rede tem custos afundados enormes — justamente o que torna esses "
            "mercados pouco contestáveis.",
            vm("Regra-âncora: monopólio natural = eficiência produtiva + necessidade de regulação."),
        ],
        "dissecando": (cz("[nexo indevido · meia-verdade]") + " A definição da 1ª oração é literal e verdadeira; o "
                       "“e, portanto,” cria um nexo falso entre custo baixo e preço baixo, e o “sem necessidade de "
                       "intervenção estatal” nega a principal implicação de política. 🔥 Padrão recorrente: "
                       "definição correta + conclusão de política invertida."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopólio natural ocorre quando um único fornecedor atende toda a demanda a custo inferior ao "
            "de dois ou mais concorrentes, o que justifica, em geral, a regulação estatal de seus preços.”</i> → "
            "CERTO",
            "<i>“No monopólio natural, a eficiência produtiva recomenda a fragmentação do mercado entre várias "
            "empresas.”</i> → ERRADO (inversão: dividir o mercado eleva o custo médio)",
        ])],
        "reescrita": ("O monopólio natural é uma situação onde um único fornecedor pode atender toda a demanda de "
                      "mercado a um custo inferior do que dois ou mais concorrentes e, portanto, " + hl("tende a "
                      "exigir regulação estatal, pois, livre, cobraria preços acima do custo marginal e geraria peso "
                      "morto") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "MEIA_VERDADE"], "moduladores": ["portanto", "sem que haja"],
        "dificuldade": 1,
        "comentario_fonte": "Primeira parte correta (CMe decrescente, um produtor mais barato); erro na conclusão: o "
                            "monopolista privado maximiza lucro, cobra acima do CMg e gera peso morto; monopólios "
                            "naturais exigem regulação ou provisão pública.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 577", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico de monopólio natural com a assertiva sobreposta)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0302
    {
        "id": "ECO-E1-0302-1", "fonte_ref": "E1-0302", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Nidi", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COM_CONC_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado de concorrência monopolística não ocorre ineficiência no cenário de longo "
                      "prazo, dado que o preço se iguala ao custo médio e, portanto, as empresas não operam com "
                      "excesso de capacidade ociosa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um mercado de concorrência monopolística ") + vm("não ocorre ineficiência") + az(" no "
                      "cenário de longo prazo, dado que o preço se iguala ao custo médio e, portanto, as empresas ")
                   + vm("não operam") + az(" com excesso de capacidade ociosa."),
        "poucas": ("P = CMe no longo prazo é verdade, mas a igualdade se dá na " + azb("tangência") + " da demanda "
                   "com o CMe na parte <b>descendente</b>, antes do mínimo: há " + azb("capacidade ociosa")
                   + " e " + vd("P > CMg") + "."),
        "destrinchando": [
            "Modelo de " + oc("Chamberlin") + " (<i>The Theory of Monopolistic Competition</i>, 1933): muitas "
            "firmas, " + azb("produto diferenciado") + " (marca, localização, qualidade) e " + azb("livre entrada")
            + ". Cada firma enfrenta uma demanda própria negativamente inclinada e age como um pequeno monopolista.",
            "Curto prazo: RMg = CMg, com P > CMe possível (lucro). O lucro atrai entrantes, que roubam clientela: a "
            "demanda de cada firma desloca-se para a esquerda e fica mais elástica.",
            "Longo prazo: a entrada para quando " + vd("lucro = 0") + ", ou seja, quando a demanda apenas "
            + azb("tangencia") + " a curva de CMe. Como a demanda é inclinada, a tangência só pode ocorrer onde o "
            "CMe também cai — à esquerda do mínimo.",
            "Duas ineficiências: (i) " + azb("produtiva") + " — a firma produz abaixo da escala eficiente "
            "(" + azb("excesso de capacidade") + "): poderia baixar o custo médio produzindo mais; (ii) "
            + azb("alocativa") + " — P > CMg (markup positivo), com peso morto.",
            "Contrapartida: a ineficiência é o “preço da variedade”. Consumidores valorizam a diversidade de "
            "produtos, e parte da capacidade ociosa é o custo de ter muitas marcas e pontos de venda.",
            vm("Regra-âncora: concorrência monopolística no longo prazo → lucro zero (P = CMe), mas P > CMg e CMe "
               "acima do mínimo."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " A premissa (P = CMe) é verdadeira; o “dado que” "
                       "e o “portanto” tiram dela uma conclusão que só valeria se o preço igualasse o CMe "
                       "<b>mínimo</b>, como na concorrência perfeita. Pista: lucro zero não é sinônimo de "
                       "eficiência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a firma em concorrência monopolística obtém lucro econômico nulo, mas opera à "
            "esquerda do ponto de custo médio mínimo.”</i> → CERTO",
            "<i>“No longo prazo, a firma em concorrência monopolística iguala preço e custo marginal.”</i> → ERRADO "
            "(P > CMg: mantém markup)",
        ])],
        "reescrita": ("Em um mercado de concorrência monopolística " + hl("ocorre ineficiência") + " no cenário de "
                      "longo prazo: " + hl("embora") + " o preço se iguale ao custo médio, " + hl("isso ocorre "
                      "acima do custo médio mínimo, e") + " as empresas " + hl("operam") + " com excesso de "
                      "capacidade ociosa."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": ["portanto"], "dificuldade": 2,
        "comentario_fonte": "P = CMe só é eficiente com custo médio mínimo; na concorrência monopolística a "
                            "diferenciação faz o equilíbrio de longo prazo ficar longe do mínimo do CMe; a distância "
                            "até a escala eficiente representa a ineficiência.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (122).png, (119).png, (114).png, (111).png", "tipo_fonte": "GRÁFICO",
                           "lado": "verso",
                           "acao": "irrecuperavel (imagens do verso não preservadas; mecanismo descrito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0692
    {
        "id": "ECO-E1-0692-1", "fonte_ref": "E1-0692", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_CONC_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("A concorrência monopolística permite a entrada livre de novas empresas, combinada com "
                      "diferenciação de produtos; no longo prazo, os lucros econômicos tendem a zero devido à entrada "
                      "de competidores que diluem o poder de mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A concorrência monopolística permite a <u>entrada livre</u> de novas empresas, combinada com "
                      "diferenciação de produtos; no longo prazo, os lucros econômicos <u>tendem a zero</u> devido à "
                      "entrada de competidores que diluem o poder de mercado."),
        "poucas": ("Livre entrada + produto diferenciado: o lucro de curto prazo atrai entrantes, que deslocam a "
                   "demanda de cada firma para a esquerda até a " + azb("tangência com o CMe") + " — "
                   + vd("lucro econômico zero") + "."),
        "destrinchando": [
            "As duas marcas do modelo de " + oc("Chamberlin") + " estão no item: " + azb("diferenciação") + " (dá "
            "a cada firma uma demanda negativamente inclinada e algum poder de preço) e " + azb("livre entrada")
            + " (impede que esse poder renda lucro duradouro).",
            "Mecânica do ajuste, como descrevem " + oc("Pindyck e Rubinfeld") + ": lucro positivo → entram firmas "
            "com substitutos próximos → cada firma perde clientes (demanda para a esquerda) e enfrenta demanda "
            "mais elástica → o processo para quando " + vd("P = CMe") + ". Com prejuízo, o movimento é o inverso "
            "(saída).",
            "“Diluir o poder de mercado” não é eliminá-lo: no longo prazo a demanda continua inclinada e "
            + vd("P > CMg") + " (markup positivo). O que zera é o <b>lucro</b>, não o poder de mercado.",
            "Por isso o equilíbrio de longo prazo combina lucro zero (como na concorrência perfeita) com "
            + azb("capacidade ociosa") + " e markup (resíduos do monopólio).",
            "Exemplos típicos: restaurantes, salões de beleza, padarias, marcas de roupa, cervejas artesanais.",
            vm("Regra-âncora: livre entrada zera o lucro; diferenciação mantém o markup."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item descreve o modelo padrão e se "
                       "protege com “tendem a zero”. O risco é ler “diluem o poder de mercado” como “eliminam” e "
                       "concluir que P = CMg — o que o item não diz. 🔥 Banca costuma trocar “lucro zero” por "
                       "“eficiência” ou “P = CMg” para gerar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a entrada de competidores elimina o poder de mercado das firmas em concorrência "
            "monopolística, que passam a cobrar preço igual ao custo marginal.”</i> → ERRADO (o markup "
            "permanece)",
            "<i>“Na concorrência monopolística, a entrada de novas firmas torna a demanda de cada firma mais "
            "elástica.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tendem a"], "dificuldade": 1,
        "comentario_fonte": "Lucro de curto prazo atrai entrantes; segundo Pindyck e Rubinfeld, a demanda das firmas "
                            "instaladas desloca-se para a esquerda até P = CMe; seguida de ficha-síntese do modelo "
                            "em resposta de IA.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (227).png, (230).png, (228).png", "tipo_fonte": "GRÁFICO",
                           "lado": "verso",
                           "acao": "irrecuperavel (imagens do verso não preservadas; conteúdo descrito no 📖)"}],
        "alertas": ["texto_corrigido: “tendem azero” → “tendem a zero” (OCR)"],
    },
    # ------------------------------------------------------------------ E2-L00023
    {
        "id": "ECO-E2-L00023-1", "fonte_ref": "E2-L00023", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Na concorrência monopolística, os agentes possuem uma capacidade ilimitada de determinar o "
                      "preço dos produtos, semelhante ao monopólio, o que lhes permite ter lucros elevados tanto no "
                      "curto quanto no longo prazo, independentemente da entrada de novos concorrentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na concorrência monopolística, os agentes possuem uma capacidade ") + vm("ilimitada")
                   + az(" de determinar o preço dos produtos, ") + vm("semelhante ao monopólio") + az(", o que lhes "
                   "permite ter lucros elevados ") + vm("tanto no curto quanto no longo prazo, independentemente da "
                   "entrada de novos concorrentes") + az("."),
        "poucas": ("O poder de preço é " + azb("limitado") + " (há muitos substitutos próximos) e a " + azb("livre "
                   "entrada") + " zera o lucro econômico no longo prazo. Lucro elevado só no curto prazo."),
        "destrinchando": [
            "A diferenciação dá a cada firma uma demanda negativamente inclinada, mas " + azb("muito elástica")
            + ": se o restaurante sobe demais o preço, o cliente vai ao vizinho. O poder de preço existe, mas é "
            "pequeno — nada parecido com o do monopolista, que não enfrenta substitutos próximos.",
            "Diferença estrutural decisiva: no " + azb("monopólio") + " há " + azb("barreiras à entrada") + " e o "
            "lucro pode persistir no longo prazo; na " + azb("concorrência monopolística") + " a entrada é livre, e "
            "o lucro atrai concorrentes até que " + vd("P = CMe") + " (lucro econômico zero).",
            "Curto prazo: lucro positivo, nulo ou prejuízo, conforme a posição da demanda em relação ao CMe. Longo "
            "prazo: lucro zero por tangência, com capacidade ociosa e P > CMg.",
            "Quadro-resumo de longo prazo: concorrência perfeita (P = CMg = CMe mínimo); concorrência "
            "monopolística (P = CMe > CMg, acima do mínimo); monopólio (P > CMe possível, lucro persistente).",
            vm("Regra-âncora: sem barreira à entrada, não há lucro econômico no longo prazo."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " Três exageros encadeados: “ilimitada”, "
                       "“semelhante ao monopólio” e “independentemente da entrada”. O item empresta ao modelo as "
                       "propriedades do monopólio e ignora a livre entrada, que é a peça-chave. Pista: qualquer "
                       "“ilimitado” sobre poder de preço é suspeito — nem o monopolista o tem (está preso à "
                       "demanda)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência monopolística, as firmas têm algum poder de preço, mas a livre entrada elimina os "
            "lucros extraordinários no longo prazo.”</i> → CERTO",
            "<i>“Mesmo o monopolista tem capacidade limitada de fixar preços, pois está restrito pela curva de "
            "demanda.”</i> → CERTO",
        ])],
        "reescrita": ("Na concorrência monopolística, os agentes possuem uma capacidade " + hl("limitada") + " de "
                      "determinar o preço dos produtos, " + hl("menor que a do monopólio") + ", o que lhes permite "
                      "ter lucros elevados " + hl("apenas no curto prazo, pois a entrada de novos concorrentes os "
                      "elimina no longo prazo") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["ilimitada", "independentemente"],
        "dificuldade": 1,
        "comentario_fonte": "Capacidade de determinação de preço limitada; a entrada de concorrentes nivela os "
                            "lucros para perto de zero no longo prazo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00024
    {
        "id": "ECO-E2-L00024-1", "fonte_ref": "E2-L00024", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Diferentemente de mercados de monopólio, na concorrência monopolística a entrada de novos "
                      "concorrentes em um mercado sem barreiras tende a rebaixar os lucros exorbitantes de curto "
                      "prazo, aproximando as condições de mercado de uma concorrência perfeita no longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Diferentemente de mercados de monopólio, na concorrência monopolística a entrada de novos "
                      "concorrentes em um mercado <u>sem barreiras</u> <u>tende a</u> rebaixar os lucros exorbitantes "
                      "de curto prazo, <u>aproximando</u> as condições de mercado de uma concorrência perfeita no "
                      "longo prazo."),
        "poucas": ("A " + azb("livre entrada") + " é o que separa a concorrência monopolística do monopólio: ela "
                   "dissipa o lucro de curto prazo até " + vd("P = CMe") + ", como na concorrência perfeita — "
                   "“aproximando”, não igualando."),
        "destrinchando": [
            "Monopólio: barreiras (legais, de escala, de insumo) protegem o lucro, que pode durar indefinidamente. "
            "Concorrência monopolística: sem barreiras, o lucro sinaliza oportunidade e atrai entrantes.",
            "A entrada desloca a demanda de cada firma para a esquerda e a torna mais elástica. O ajuste termina na "
            + azb("tangência demanda–CMe") + ": " + vd("lucro econômico zero") + ", tal como na concorrência "
            "perfeita.",
            "Por que “aproximando” e não “igualando”: no longo prazo ainda há " + vd("P > CMg") + " (markup) e "
            "produção abaixo da escala eficiente (" + azb("capacidade ociosa") + "). A semelhança com a "
            "concorrência perfeita está no lucro zero e na pressão competitiva, não na eficiência.",
            "Quanto mais firmas e menos diferenciação, mais elástica a demanda de cada uma e mais o resultado se "
            "aproxima do competitivo.",
            vm("Regra-âncora: concorrência monopolística ≈ concorrência perfeita no lucro (zero), ≠ na eficiência "
               "(P > CMg, capacidade ociosa)."),
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " O item é salvo por “tende a” e "
                       "“aproximando”. Uma versão com “igualando as condições de concorrência perfeita” ou "
                       "“eliminando a ineficiência” seria ERRADA. O adjetivo “exorbitantes” é retórico e não altera "
                       "o julgamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a concorrência monopolística reproduz integralmente o equilíbrio da concorrência "
            "perfeita, inclusive a produção no custo médio mínimo.”</i> → ERRADO (há capacidade ociosa)",
            "<i>“No monopólio, as barreiras à entrada permitem que o lucro extraordinário persista no longo "
            "prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["tende a", "aproximando"],
        "dificuldade": 1,
        "comentario_fonte": "A facilidade de entrada distingue a concorrência monopolística do monopólio; lucros de "
                            "curto prazo se dissipam com a entrada, como na concorrência perfeita.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00025
    {
        "id": "ECO-E2-L00025-1", "fonte_ref": "E2-L00025", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("No curto prazo, as empresas em mercados de concorrência monopolística podem obter lucros "
                      "extraordinários, pois têm a capacidade de discriminar preços, mesmo com a presença de muitos "
                      "concorrentes com produtos substitutos próximos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("No curto prazo, as empresas em mercados de concorrência monopolística <u>podem</u> obter "
                      "lucros extraordinários, pois têm a <u>capacidade de discriminar preços</u>, mesmo com a "
                      "presença de muitos concorrentes com produtos substitutos próximos."),
        "poucas": ("Lucro extraordinário no curto prazo é possível, porque a " + azb("diferenciação") + " dá a cada "
                   "firma algum " + azb("poder de preço") + " (demanda inclinada). A fonte lê “discriminar preços” "
                   "como esse poder de fixar o próprio preço."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Em sentido técnico, " + azb("discriminar preços") + " é cobrar preços diferentes pelo "
                          "mesmo bem, e não é isso que explica o lucro de curto prazo no modelo de "
                          + oc("Chamberlin") + ": a causa é o poder de mercado gerado pela diferenciação. Uma banca "
                          "rigorosa poderia dar ERRADO pelo nexo. O CERTO da fonte se sustenta lendo a expressão "
                          "como “capacidade de fixar preço acima do custo marginal” — firmas com algum poder de "
                          "mercado também podem, de fato, discriminar.")],
        "destrinchando": [
            "Curto prazo: o número de firmas está dado. Cada uma escolhe q onde RMg = CMg e lê o preço na sua "
            "demanda; se esse preço superar o CMe, há " + vd("lucro extraordinário") + " (se ficar abaixo, "
            "prejuízo).",
            "A origem do poder de preço é a " + azb("diferenciação do produto") + ": marca, localização, qualidade, "
            "atendimento. Mesmo com muitos concorrentes e substitutos próximos, o cliente fiel não troca de "
            "fornecedor por qualquer centavo — a demanda é inclinada, ainda que elástica.",
            "Firmas com algum poder de mercado podem, além disso, " + azb("discriminar") + " (happy hour, "
            "fidelidade, cupons), o que reforça a captura de excedente. Mas isso é ferramenta adicional, não a "
            "condição do lucro.",
            "No longo prazo, o lucro atrai entrantes, a demanda de cada firma recua e fica mais elástica até a "
            "tangência com o CMe: " + vd("lucro zero") + ".",
            vm("Regra-âncora: lucro de curto prazo na concorrência monopolística vem do poder de preço dado pela "
               "diferenciação; a livre entrada o elimina no longo prazo."),
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " A conclusão (lucro no curto prazo) está certa e "
                       "protegida pelo “podem”; o ponto frágil é a justificativa (“discriminar preços”), usada em "
                       "sentido amplo. Ao julgar itens de curso, confira se a banca usa o termo técnico ou o "
                       "coloquial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, as empresas em concorrência monopolística podem obter lucros extraordinários "
            "graças ao poder de mercado conferido pela diferenciação de seus produtos.”</i> → CERTO",
            "<i>“No longo prazo, as empresas em concorrência monopolística mantêm lucros extraordinários graças à "
            "diferenciação.”</i> → ERRADO (a livre entrada zera o lucro)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["podem", "mesmo com"], "dificuldade": 2,
        "comentario_fonte": "No curto prazo as firmas obtêm lucros extraordinários por terem algum poder de preço "
                            "devido à diferenciação, o que permitiria praticar discriminação de preços apesar da "
                            "rivalidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: “discriminar preços” não é a causa técnica do lucro de curto prazo (é o poder de "
                    "mercado da diferenciação); CERTO da fonte mantido na leitura ampla da expressão"],
    },
    # ------------------------------------------------------------------ E2-L00026
    {
        "id": "ECO-E2-L00026-1", "fonte_ref": "E2-L00026", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A concorrência monopolística, apesar de compartilhar características com o monopólio em "
                      "termos de capacidade de preço, permite a mobilidade de entrada de novos agentes, o que no "
                      "longo prazo faz com que o mercado se aproxime da estrutura de concorrência perfeita, "
                      "eliminando os lucros extraordinários."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A concorrência monopolística, apesar de compartilhar características com o monopólio em "
                      "termos de capacidade de preço, permite a <u>mobilidade de entrada</u> de novos agentes, o que "
                      "no longo prazo faz com que o mercado <u>se aproxime</u> da estrutura de concorrência perfeita, "
                      "eliminando os lucros extraordinários."),
        "poucas": ("Estrutura " + azb("híbrida") + ": do monopólio herda o poder de preço (demanda inclinada); da "
                   "concorrência perfeita, a " + azb("livre entrada") + ", que zera o lucro no longo prazo."),
        "destrinchando": [
            "O nome resume o modelo: “monopolística” pela " + azb("diferenciação") + " — cada firma é a única "
            "vendedora da <b>sua</b> marca e tem demanda inclinada (P > RMg); “concorrência” pelo " + azb("grande "
            "número de firmas") + " e pela " + azb("livre entrada e saída") + ".",
            "Longo prazo: a entrada desloca a demanda de cada firma até a tangência com o CMe → "
            + vd("lucro extraordinário = 0") + ". Nesse ponto o resultado se parece com o da concorrência "
            "perfeita (lucro normal).",
            "O que permanece de monopólio: " + vd("P > CMg") + " (markup) e produção à esquerda do CMe mínimo "
            "(" + azb("capacidade ociosa") + "). Por isso o item diz “se aproxime”, e não “se iguale”.",
            "Comparação útil com o " + azb("oligopólio") + ": lá há poucas firmas, interdependência estratégica e, "
            "em geral, barreiras; aqui, muitas firmas pequenas que não reagem umas às outras individualmente.",
            vm("Regra-âncora: monopólio no curto prazo (poder de preço), concorrência no longo prazo (lucro zero)."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Mais uma variação do mesmo bloco: o item "
                       "repete a lógica de lucro zero por livre entrada e se protege com “se aproxime”. O verbo "
                       "decisivo é “eliminando os lucros extraordinários” — e não “eliminando as ineficiências”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A mobilidade de entrada faz com que, no longo prazo, a concorrência monopolística elimine o "
            "markup e produza no custo médio mínimo.”</i> → ERRADO (só o lucro some; markup e capacidade ociosa "
            "ficam)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["se aproxime"], "dificuldade": 1,
        "comentario_fonte": "Combina elementos de monopólio e de concorrência perfeita; a mobilidade de entrada reduz "
                            "os lucros extraordinários e o lucro econômico tende a zero no longo prazo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00239
    {
        "id": "ECO-E2-L00239-1", "fonte_ref": "E2-L00239", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_CONC_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, empresas em concorrência monopolística operam com capacidade plenamente "
                      "utilizada, de forma que o preço se iguala tanto ao custo marginal quanto ao custo total "
                      "médio, como na concorrência perfeita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No longo prazo, empresas em concorrência monopolística operam com ")
                   + vm("capacidade plenamente utilizada") + az(", de forma que o preço se iguala ")
                   + vm("tanto ao custo marginal quanto") + az(" ao custo total médio, ")
                   + vm("como na concorrência perfeita") + az("."),
        "poucas": ("No longo prazo, " + vd("P = CTMe") + " (lucro zero), mas " + vd("P > CMg") + " e a produção "
                   "fica abaixo da escala que minimiza o CTMe: há " + azb("capacidade ociosa") + "."),
        "destrinchando": [
            "Equilíbrio de longo prazo de " + oc("Chamberlin") + ": duas condições ao mesmo tempo — "
            + vd("RMg = CMg") + " (a firma maximiza lucro) e " + vd("P = CTMe") + " (a entrada zerou o lucro). "
            "Geometricamente, a demanda tangencia o CTMe.",
            "Como a demanda da firma é inclinada, P > RMg = CMg. E a tangência de uma reta descendente com o CTMe "
            "só pode ocorrer onde o CTMe também desce — à esquerda do mínimo. Logo: " + vd("P = CTMe > CMg")
            + ".",
            azb("Capacidade ociosa") + " (ou excesso de capacidade): a firma produz menos que a quantidade de custo "
            "médio mínimo. Se aumentasse a produção, o custo unitário cairia, mas teria de baixar o preço de todas "
            "as unidades, e a receita marginal não compensaria.",
            "Na " + azb("concorrência perfeita") + ", a demanda da firma é horizontal; a tangência ocorre no "
            "mínimo do CTMe e vale " + vd("P = CMg = CTMe mínimo") + " — as três igualdades que o item atribui, "
            "por engano, à concorrência monopolística.",
            vm("Regra-âncora: concorrência monopolística de longo prazo → P = CTMe > CMg, com capacidade ociosa."),
        ],
        "grafico_verso": "ECO-E2-L00239-1-V1",
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " O item copia o equilíbrio de longo prazo da "
                       "concorrência perfeita. Há um pedaço verdadeiro (P = CTMe), cercado de dois enxertos falsos "
                       "(capacidade plena e P = CMg). Pista: “como na concorrência perfeita” em item de concorrência "
                       "monopolística costuma ser a armadilha. 🔥 Recorrente em CEBRASPE e simulados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, empresas em concorrência monopolística têm lucro econômico nulo, mas operam com "
            "capacidade ociosa e preço superior ao custo marginal.”</i> → CERTO",
            "<i>“No longo prazo, a firma em concorrência monopolística produz no ponto de mínimo do custo total "
            "médio.”</i> → ERRADO (produz à esquerda do mínimo)",
        ])],
        "reescrita": ("No longo prazo, empresas em concorrência monopolística operam com " + hl("capacidade ociosa")
                      + ", de forma que o preço se iguala ao custo total médio" + hl(", mas supera o custo "
                      "marginal") + ", " + hl("diferentemente do que ocorre") + " na concorrência perfeita."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["plenamente", "tanto… quanto"],
        "dificuldade": 1,
        "comentario_fonte": "No longo prazo o lucro é zero, mas as firmas operam com capacidade ociosa, abaixo da "
                            "escala que minimiza o CTM, e o preço permanece acima do custo marginal.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00288
    {
        "id": "ECO-E2-L00288-1", "fonte_ref": "E2-L00288", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": COM_CONC_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("Diferentemente da concorrência perfeita, onde o equilíbrio de longo prazo ocorre no ponto de "
                      "escala eficiente mínima (custo total médio mínimo), na concorrência monopolística as firmas "
                      "operam com excesso de capacidade (capacidade ociosa) no longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Diferentemente da concorrência perfeita, onde o equilíbrio de longo prazo ocorre no ponto de "
                      "escala eficiente mínima (custo total médio mínimo), na concorrência monopolística as firmas "
                      "operam com <u>excesso de capacidade</u> (capacidade ociosa) no longo prazo."),
        "poucas": ("É o " + azb("teorema do excesso de capacidade") + ": a demanda inclinada tangencia o CTMe na "
                   "parte descendente, antes do mínimo. A firma produz menos do que a " + vd("escala eficiente")
                   + "."),
        "destrinchando": [
            azb("Concorrência perfeita") + ": demanda da firma horizontal; a entrada e a saída levam o preço ao "
            "mínimo do CTMe → " + vd("P = CMg = CTMe mínimo") + ". Cada firma produz na " + azb("escala eficiente "
            "mínima") + ".",
            azb("Concorrência monopolística") + ": a demanda da firma é inclinada (produto diferenciado). A entrada "
            "a empurra para baixo até tocar o CTMe sem cruzá-lo; uma reta descendente só tangencia uma curva em U "
            "no trecho em que ela também desce. Resultado: q de longo prazo " + vd("à esquerda do mínimo") + ".",
            "A distância entre a quantidade de longo prazo e a de CTMe mínimo é o " + azb("excesso de capacidade")
            + ": a firma poderia reduzir o custo unitário produzindo mais, mas não o faz porque teria de baixar "
            "o preço.",
            "Leitura de bem-estar: parte dessa ineficiência é o custo da " + azb("variedade") + " — muitos "
            "restaurantes meio vazios significam mais opções e menos deslocamento para o consumidor. Não há "
            "consenso de que menos firmas, mais eficientes, seriam melhores.",
            vm("Regra-âncora: tangência no trecho descendente do CTMe = capacidade ociosa."),
        ],
        "dissecando": (cz("[literalidade]") + " O item enuncia o teorema do excesso de capacidade em linguagem de "
                       "manual. O risco é o candidato achar que lucro zero implica escala eficiente e marcar "
                       "ERRADO. Pista: só a demanda horizontal toca o CTMe no mínimo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência monopolística, a firma de longo prazo opera à direita do ponto de custo total "
            "médio mínimo.”</i> → ERRADO (opera à esquerda)",
            "<i>“Na concorrência perfeita, o equilíbrio de longo prazo ocorre no mínimo do custo total médio.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Demanda inclinada tangencia o CTMe na parte declinante, antes do mínimo (teorema do "
                            "excesso de capacidade); a firma poderia reduzir o custo médio produzindo mais, mas não o "
                            "faz para não reduzir o preço.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00328
    {
        "id": "ECO-E2-L00328-1", "fonte_ref": "E2-L00328", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": COM_CONC_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de concorrência monopolística, o equilíbrio de longo prazo caracteriza-se pelo lucro "
                      "econômico nulo e pela eficiência produtiva, uma vez que a livre entrada de firmas força o "
                      "preço a se igualar ao custo médio em seu ponto de mínimo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de concorrência monopolística, o equilíbrio de longo prazo caracteriza-se pelo lucro "
                      "econômico nulo e ") + vm("pela eficiência produtiva") + az(", uma vez que a livre entrada de "
                      "firmas força o preço a se igualar ao custo médio ") + vm("em seu ponto de mínimo") + az("."),
        "poucas": ("Lucro nulo, sim; " + azb("eficiência produtiva") + ", não. A livre entrada leva P ao CMe, mas no "
                   "ponto de " + azb("tangência") + " com a demanda inclinada — no trecho descendente do CMe, acima "
                   "do mínimo."),
        "destrinchando": [
            azb("Eficiência produtiva") + " = produzir ao menor custo médio possível (mínimo do CMe). "
            + azb("Eficiência alocativa") + " = P = CMg. A concorrência perfeita de longo prazo tem as duas; a "
            "concorrência monopolística não tem nenhuma.",
            "A livre entrada garante só uma coisa: " + vd("lucro econômico zero") + " (P = CMe). Onde essa "
            "igualdade ocorre depende do formato da demanda da firma. Horizontal (concorrência perfeita) → toca o "
            "CMe no mínimo. Inclinada (produto diferenciado) → toca o CMe antes do mínimo.",
            "Consequências da tangência à esquerda do mínimo: " + azb("capacidade ociosa") + " (q abaixo da escala "
            "eficiente) e " + vd("P > CMg") + " (markup, peso morto).",
            "Ficha-síntese do modelo: muitas firmas, produto diferenciado, livre entrada; curto prazo com lucro ou "
            "prejuízo; longo prazo com lucro zero, P = CMe > CMg e excesso de capacidade.",
            vm("Regra-âncora: livre entrada zera o lucro, mas só a demanda horizontal leva ao CMe mínimo."),
        ],
        "grafico_verso": "ECO-E2-L00328-1-V1",
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " “Lucro econômico nulo” é verdadeiro e funciona "
                       "como isca; o erro está em importar da concorrência perfeita a eficiência produtiva e o “ponto "
                       "de mínimo”. Pista: a justificativa (“livre entrada força P = CMe mínimo”) mistura a causa "
                       "certa (livre entrada) com o resultado de outro modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de concorrência monopolística, o equilíbrio de longo prazo caracteriza-se pelo lucro "
            "econômico nulo e pela produção em escala inferior à eficiente.”</i> → CERTO",
            "<i>“No modelo de concorrência monopolística, o equilíbrio de longo prazo caracteriza-se pela "
            "eficiência alocativa, com preço igual ao custo marginal.”</i> → ERRADO (P > CMg)",
        ])],
        "reescrita": ("No modelo de concorrência monopolística, o equilíbrio de longo prazo caracteriza-se pelo lucro "
                      "econômico nulo e pela " + hl("ineficiência produtiva (capacidade ociosa)") + ", uma vez que a "
                      "livre entrada de firmas força o preço a se igualar ao custo médio " + hl("no trecho "
                      "descendente da curva, à esquerda de seu ponto de mínimo") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Lucro nulo, mas sem eficiência produtiva: a demanda tangencia o custo médio na parte "
                            "descendente (teorema da capacidade ociosa) e P > CMg; uma resposta escreve “custo médio "
                            "(CMg)” por engano; ficha-síntese do modelo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 042", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 043-044", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvidas (ficha-síntese no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01504
    {
        "id": "ECO-E2-L01504-1", "fonte_ref": "E2-L01504", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_FIRMA_CUSTOS,
        "rotulo_item": "Item",
        "assertiva": ("A competição monopolística é uma estrutura de mercado caracterizada por lucro zero e nível de "
                      "produção abaixo da escala eficiente, no longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A competição monopolística é uma estrutura de mercado caracterizada por <u>lucro zero</u> e "
                      "nível de produção <u>abaixo da escala eficiente</u>, no longo prazo."),
        "poucas": ("No longo prazo, a entrada empurra a demanda da firma até " + azb("tangenciar o CMe") + ": "
                   + vd("lucro zero") + ", num ponto à esquerda do CMe mínimo — " + azb("capacidade ociosa") + "."),
        "destrinchando": [
            "Curto prazo (painel a): a firma escolhe q₁ onde RMg = CMg e cobra P₁ na demanda. Se P₁ > CMe, há "
            "lucro — o retângulo (P₁ − CMe) × q₁.",
            "Ajuste: o lucro atrai entrantes com produtos parecidos. A demanda de cada firma recua para a esquerda "
            "e fica mais elástica, até que não haja mais lucro a disputar.",
            "Longo prazo (painel b): a demanda apenas toca o CMe em q₂, onde também RMg = CMg. " + vd("P₂ = CMe")
            + " (lucro zero) e " + vd("P₂ > CMg") + " (markup). Como a tangência ocorre no trecho descendente, q₂ "
            "fica abaixo da " + azb("escala eficiente mínima") + " (mínimo do CMe).",
            "As duas ineficiências apontadas por " + oc("Pindyck e Rubinfeld") + ": " + azb("capacidade ociosa")
            + " (custo médio acima do mínimo) e " + azb("markup") + " (preço acima do CMg, peso morto). Em troca, "
            "variedade de produtos.",
            vm("Regra-âncora: longo prazo de Chamberlin = lucro zero + capacidade ociosa + P > CMg."),
        ],
        "grafico_verso": "ECO-E2-L01504-1-V1",
        "dissecando": (cz("[literalidade]") + " Item-síntese que combina as duas marcas do longo prazo. O risco é "
                       "achar que “lucro zero” obriga a produzir na escala eficiente, como na concorrência perfeita. "
                       "“Competição monopolística” é só outro nome para concorrência monopolística."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A competição monopolística é caracterizada, no longo prazo, por lucro zero e produção na escala "
            "eficiente mínima.”</i> → ERRADO (troca de modelo: é o resultado da concorrência perfeita)",
            "<i>“Na competição monopolística, a firma pode ter lucro econômico positivo no curto prazo.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Duas respostas convergentes: lucro zero por livre entrada (P = CMe) e excesso de "
                            "capacidade porque a tangência ocorre à esquerda do CMe mínimo; gráfico de Pindyck "
                            "comparando curto e longo prazo; quadro sobre capacidade ociosa e markup.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 383", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01504-1-V1)"},
                          {"ref": "IMAGEM 384", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01541
    {
        "id": "ECO-E2-L01541-1", "fonte_ref": "E2-L01541", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_TEORIA_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Num mercado em que a concorrência entre as firmas ocorre pela diferenciação de produto, a taxa "
                      "de <i>mark up</i> será menor quanto mais firmas houver neste mercado e quanto menor for o grau "
                      "de diferenciação do produto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Num mercado em que a concorrência entre as firmas ocorre pela diferenciação de produto, a "
                      "taxa de <i>mark up</i> será <u>menor</u> quanto <u>mais firmas</u> houver neste mercado e "
                      "quanto <u>menor</u> for o grau de diferenciação do produto."),
        "poucas": ("Markup = " + vd("1/|ε|") + " (Lerner). Mais firmas e produtos mais parecidos tornam a demanda de "
                   "cada firma " + azb("mais elástica") + " — e o markup encolhe."),
        "destrinchando": [
            "Regra de " + oc("Lerner") + ": " + vd("(P − CMg)/P = 1/|ε|") + ", em que ε é a elasticidade da "
            "demanda <b>da firma</b> (não a do mercado). Tudo o que aumenta |ε| reduz o markup.",
            azb("Mais firmas") + ": cada uma tem mais concorrentes próximos; uma alta de preço desvia clientes com "
            "mais facilidade → |ε| maior.",
            azb("Menos diferenciação") + ": os produtos ficam mais parecidos, mais próximos de " + azb("substitutos "
            "perfeitos") + "; no limite (produto homogêneo, muitas firmas), a demanda da firma é horizontal, "
            + vd("|ε| → ∞") + " e " + vd("P → CMg") + ": concorrência perfeita.",
            "Na direção oposta: marcas fortes, fidelidade e poucos rivais tornam a demanda inelástica e permitem "
            "margens altas. Por isso firmas investem em publicidade e diferenciação — para reduzir a elasticidade "
            "da própria demanda.",
            vm("Regra-âncora: mais substitutos (mais firmas, menos diferenciação) → |ε| maior → markup menor."),
        ],
        "dissecando": (cz("[literalidade]") + " O item aplica Lerner à concorrência monopolística com duas "
                       "variáveis no mesmo sentido. O risco é inverter uma delas (“menor diferenciação → markup "
                       "maior”). Pista: tudo que aproxima o mercado da concorrência perfeita reduz o markup."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A taxa de mark up será menor quanto maior for o grau de diferenciação do produto.”</i> → ERRADO "
            "(inversão: diferenciação reduz a elasticidade e eleva o markup)",
            "<i>“O índice de Lerner relevante para a firma depende da elasticidade da demanda que ela enfrenta, "
            "e não da demanda de mercado.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["quanto mais", "quanto menor"], "dificuldade": 1,
        "comentario_fonte": "Mais firmas e menor diferenciação elevam a elasticidade da demanda percebida pela firma "
                            "e reduzem o markup (P − CMg)/P; o verso também traz, por engano, comentário sobre outro "
                            "item (markup sobre custo médio × marginal).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 414", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (regra de Lerner no 📖)"}],
        "alertas": [],
    },
]
