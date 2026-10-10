"""Cards do lote de redação 17 — ECO, passada 03 (notas 74: CEPAL e termos de troca; 75: novas teorias do comércio)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "cepal": "🌎 CEPAL e termos de troca",
    "novas": "🔬 Novas teorias do comércio",
}

CMD_CEPAL_2010 = "Acerca da CEPAL e do pensamento de Raúl Prebisch, julgue o item a seguir."

CMD_NAB_CEPAL = "Sobre o pensamento da CEPAL e a industrialização brasileira, julgue o item a seguir."

CMD_RT = "Acerca das teorias do comércio internacional, julgue o item a seguir."

CMD_BOZAN_06 = "Sobre as teorias de comércio contemporâneas, julgue o item a seguir."

CMD_BOZAN_02 = "Julgue o item a seguir, sobre a diferenciação de produtos e o comércio internacional."

CMD_NAB_COM = "A respeito das teorias do comércio, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E1-0910
    {
        "id": "ECO-E1-0910-1", "fonte_ref": "E1-0910", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": CMD_CEPAL_2010,
        "rotulo_item": "Item",
        "assertiva": ("A criação, pela ONU, da CEPAL — que depois inclui também a região do Caribe — contou, desde o "
                      "início, com o decidido apoio dos EUA."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A criação, pela ONU, da CEPAL — que depois inclui também a região do Caribe — contou, "
                       "desde o início, com ") + vm("o decidido apoio") + az(" dos EUA.")),
        "poucas": ("Os EUA foram " + vm("contrários") + " à criação da CEPAL: viam na comissão uma duplicação do "
                   "sistema interamericano (OEA) e uma ameaça à sua liderança regional. A proposta foi latino-"
                   "americana, liderada pelo " + azb("Chile") + "."),
        "destrinchando": [
            "A " + azb("Comissão Econômica para a América Latina") + " foi criada em " + vd("1948") + " por "
            "resolução do " + azb("ECOSOC") + ", a partir de proposta do delegado chileno Hernán Santa Cruz. É "
            "uma das cinco " + azb("comissões regionais") + " da ONU, subordinada ao ECOSOC, com sede em "
            "Santiago — e não uma agência especializada (como FAO ou OIT, que têm tratado constitutivo próprio).",
            "Os EUA resistiram: preferiam tratar a economia regional no âmbito da recém-criada OEA (1948), sob "
            "sua influência, e desconfiavam de um foro que pudesse questionar o livre-comércio. Mesmo assim, "
            "integraram a comissão como membros, ao lado de potências com territórios na região (Reino Unido, "
            "França, Países Baixos). A sobrevivência da CEPAL foi posta em xeque no início dos anos 1950 e "
            "garantida com apoio latino-americano, inclusive do " + rx("Brasil") + ".",
            "O primeiro secretário-executivo foi o mexicano Gustavo Martínez Cabañas; " + oc("Raúl Prebisch")
            + " chegou em 1949, com o texto que ficou conhecido como “manifesto latino-americano” (<i>O "
            "desenvolvimento econômico da América Latina e seus principais problemas</i>), e dirigiu a "
            "comissão a partir de 1950.",
            "O Caribe entrou no nome em " + vd("1984") + ": Comissão Econômica para a América Latina e o "
            "Caribe (a sigla CEPAL se manteve).",
        ],
        "dissecando": (cz("[inversão · juízo indevido]") + " O item inverte a posição norte-americana: de "
                       "opositor a patrocinador “decidido”. O aposto sobre o Caribe é verdadeiro e serve de isca "
                       "de credibilidade. Pista: a CEPAL nasceu para pensar a periferia a partir dela mesma, "
                       "agenda que Washington via com desconfiança."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A CEPAL, criada em 1948, é uma comissão regional vinculada ao ECOSOC.”</i> → CERTO",
            "<i>“A CEPAL é uma agência especializada da ONU, com tratado constitutivo próprio.”</i> → ERRADO "
            "(troca de conceito: é comissão regional do ECOSOC)",
        ])],
        "reescrita": ("A criação, pela ONU, da CEPAL — que depois inclui também a região do Caribe — contou, "
                      "desde o início, com " + hl("a oposição") + " dos EUA."),
        "tipo_erro": ["INVERSAO", "JUIZO_INDEVIDO"], "moduladores": ["desde o início", "decidido"],
        "dificuldade": 2,
        "comentario_fonte": ("Criada em 1948, com liderança de Prebisch; os EUA não apoiaram o projeto no início, "
                             "embora tenham aderido depois; atrelada ao ECOSOC, seria agência especializada da "
                             "ONU."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem chama a CEPAL de “agência especializada” (é comissão "
                    "regional do ECOSOC), atribui a Prebisch a liderança na criação (ele chegou em 1949) e diz "
                    "que os EUA aderiram depois (foram membros fundadores, embora contrários à criação)"],
    },
    # ------------------------------------------------------------------ E1-0911
    {
        "id": "ECO-E1-0911-1", "fonte_ref": "E1-0911", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": CMD_CEPAL_2010,
        "rotulo_item": "Item",
        "assertiva": ("As ideias de Raul Prebisch — o grande mentor da CEPAL — tiveram grande influência e "
                      "contribuíram decisivamente para a convocação da Conferência das Nações Unidas sobre "
                      "Comércio e Desenvolvimento (UNCTAD, na sigla em inglês)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As ideias de Raul Prebisch — o grande mentor da CEPAL — tiveram grande influência e "
                      "<u>contribuíram decisivamente</u> para a convocação da Conferência das Nações Unidas sobre "
                      "Comércio e Desenvolvimento (UNCTAD, na sigla em inglês)."),
        "poucas": ("A " + azb("UNCTAD") + " (" + vd("1964") + ") institucionalizou a crítica cepalina ao "
                   "comércio Norte-Sul, e " + oc("Prebisch") + " foi seu primeiro secretário-geral, autor do "
                   "relatório-base da conferência."),
        "destrinchando": [
            "A tese de " + oc("Prebisch") + " (e de " + oc("Hans Singer") + "): o comércio entre "
            + azb("centro") + " industrial e " + azb("periferia") + " primário-exportadora não distribui "
            "igualmente os frutos do progresso técnico, porque os " + azb("termos de troca") + " da periferia "
            "tendem a se deteriorar. Logo, o livre-comércio, sozinho, não leva à convergência de rendas.",
            "Nos anos 1960, os países em desenvolvimento queriam um foro próprio para essa agenda, já que o "
            "GATT era visto como clube dos países ricos. A " + azb("I UNCTAD") + " (Genebra, " + vd("1964")
            + ") virou órgão permanente da Assembleia Geral; Prebisch foi o secretário-geral de 1964 a 1969, e "
            "seu relatório <i>Por uma nova política comercial em prol do desenvolvimento</i> pautou a "
            "conferência.",
            "Na mesma conferência nasceu o " + azb("G-77") + ". Frutos da agenda UNCTAD: o "
            + azb("Sistema Geral de Preferências") + " (SGP, 1968/1971), acordos de produtos de base e a "
            "Parte IV do GATT (1965), sobre comércio e desenvolvimento, com o princípio de não reciprocidade.",
            rx("Brasil") + ": participou ativamente da criação da UNCTAD e do G-77, coerente com a "
            "Política Externa Independente (1961–1964).",
        ],
        "dissecando": (cz("[literalidade]") + " Fato histórico direto. O “decisivamente” poderia assustar, mas "
                       "aqui é seguro: a UNCTAD é a tradução institucional do pensamento de Prebisch, que a "
                       "dirigiu. 🔥 A banca alterna CEPAL (1948) e UNCTAD (1964) em itens de data e de autoria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Raúl Prebisch foi o primeiro secretário-geral da UNCTAD, criada em 1964.”</i> → CERTO",
            "<i>“A UNCTAD foi criada em 1948, junto com a CEPAL, sob a direção de Prebisch.”</i> → ERRADO (data "
            "trocada: 1964)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["decisivamente"], "dificuldade": 1,
        "comentario_fonte": ("Prebisch, teórico da deterioração dos termos de troca, dividiu o mundo em centro e "
                             "periferia e contestou que o livre-comércio levaria à convergência — argumento "
                             "ratificado pela UNCTAD."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0912
    {
        "id": "ECO-E1-0912-1", "fonte_ref": "E1-0912", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": CMD_CEPAL_2010,
        "rotulo_item": "Item",
        "assertiva": ("Prebisch advogou para a América Latina um modelo de industrialização agressivamente voltado "
                      "para a exportação, de modo a corrigir a deterioração dos termos de troca entre os países do "
                      "Norte e do Sul."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Prebisch advogou para a América Latina um modelo de industrialização ")
                    + vm("agressivamente voltado para a exportação") + az(", de modo a corrigir a deterioração "
                                                                         "dos termos de troca entre os países do "
                                                                         "Norte e do Sul.")),
        "poucas": ("A CEPAL de Prebisch defendeu a " + azb("industrialização por substituição de importações")
                   + " (ISI), voltada ao " + vm("mercado interno") + " e conduzida pelo Estado — não um modelo "
                   "exportador à moda asiática."),
        "destrinchando": [
            "Diagnóstico: a periferia exporta primários de preço declinante e baixa elasticidade-renda e importa "
            "manufaturas; com o crescimento, as importações sobem mais que as exportações → "
            + azb("estrangulamento externo") + " e deterioração dos termos de troca.",
            "Remédio: produzir internamente o que se importava, com proteção tarifária, controle cambial, "
            "crédito público e planejamento estatal — a " + azb("ISI") + ". O motor do crescimento passa a ser o "
            "mercado interno; a pauta exportadora continuaria primária no curto prazo, financiando as "
            "importações de bens de capital.",
            "Fundamento teórico: " + oc("Prebisch") + " criticava a “falsa universalidade” da teoria "
            "econômica do centro (as vantagens comparativas de " + oc("Ricardo") + " aplicadas a estruturas "
            "diferentes) e pedia um Estado com corpo técnico capaz de planejar o desenvolvimento.",
            "Nuance: nos anos 1960, o próprio Prebisch reconheceu os limites da ISI (mercados nacionais "
            "pequenos, viés antiexportador) e passou a defender a " + azb("integração regional") + " e a "
            "exportação de manufaturas para a região — mas como complemento, nunca como modelo “agressivamente "
            "exportador”, que é a marca dos tigres asiáticos (" + azb("export-led growth") + ").",
            vm("Regra-âncora: CEPAL clássica = industrialização para dentro (ISI); Ásia = industrialização para "
               "fora (export-led)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O objetivo (corrigir a deterioração dos termos de troca) "
                       "está certo; o erro está no modelo, trocado pelo do Leste Asiático. O advérbio "
                       "“agressivamente” é a pista: nada mais distante da ISI protecionista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Prebisch defendeu a industrialização por substituição de importações, apoiada na proteção do "
            "mercado interno e no planejamento estatal.”</i> → CERTO",
            "<i>“Para a CEPAL, o aprofundamento das vantagens comparativas na produção primária corrigiria a "
            "deterioração dos termos de troca.”</i> → ERRADO (inversão: a especialização primária é a causa do "
            "problema)",
        ])],
        "reescrita": ("Prebisch advogou para a América Latina um modelo de industrialização "
                      + hl("voltado para o mercado interno, por substituição de importações") + ", de modo a "
                      "corrigir a deterioração dos termos de troca entre os países do Norte e do Sul."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["agressivamente"], "dificuldade": 1,
        "comentario_fonte": ("Prebisch criticou a falsa universalidade da ciência econômica; a CEPAL defendeu a "
                             "atuação do Estado e a industrialização voltada ao mercado interno por substituição "
                             "de importações, com corpo técnico eficiente."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0913
    {
        "id": "ECO-E1-0913-1", "fonte_ref": "E1-0913", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": CMD_CEPAL_2010,
        "rotulo_item": "Item",
        "assertiva": ("No Brasil, entre os economistas que trabalharam na CEPAL e foram influenciados por "
                      "Prebisch, cabe mencionar Celso Furtado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No Brasil, entre os economistas que <u>trabalharam na CEPAL</u> e foram influenciados por "
                      "Prebisch, cabe mencionar <u>Celso Furtado</u>."),
        "poucas": (oc("Celso Furtado") + " trabalhou na CEPAL de " + vd("1949 a 1957") + " e é, com "
                   + oc("Prebisch") + ", o nome central do " + azb("estruturalismo latino-americano") + "."),
        "destrinchando": [
            oc("Furtado") + " chegou a Santiago em 1949 e chefiou a Divisão de Desenvolvimento da CEPAL; em "
            "1953–1955 presidiu o Grupo Misto CEPAL-BNDE, cujo estudo sobre a economia brasileira influenciou o "
            + rx("Plano de Metas") + " de JK.",
            "Obra-chave: <i>Formação Econômica do Brasil</i> (" + vd("1959") + "), que relê a história "
            "brasileira com as categorias cepalinas (centro-periferia, deslocamento do centro dinâmico para o "
            "mercado interno a partir de 1930, “socialização das perdas” na defesa do café). Também "
            "<i>Desenvolvimento e Subdesenvolvimento</i> (1961): o subdesenvolvimento como processo histórico "
            "autônomo, não etapa anterior ao desenvolvimento.",
            "Atuação no " + rx("Brasil") + ": criou a " + azb("SUDENE") + " (1959) e foi o primeiro ministro do "
            "Planejamento (Plano Trienal, 1962–1963).",
            "Outros nomes ligados à CEPAL e ao pensamento cepalino no Brasil: " + oc("Maria da Conceição "
            "Tavares") + " (<i>Auge e declínio do processo de substituição de importações</i>, 1964) e "
            + oc("Ignácio Rangel") + " (heterodoxo próximo do estruturalismo). Entre os não brasileiros, "
            + oc("Aníbal Pinto") + " e " + oc("Osvaldo Sunkel") + ".",
        ],
        "dissecando": (cz("[literalidade]") + " Item de associação autor–instituição, sem armadilha. A banca "
                       "costuma testar a troca de nome (atribuir a Furtado obra de Prebisch, ou o contrário) ou "
                       "datas (CEPAL 1948 × <i>Formação Econômica do Brasil</i> 1959)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Celso Furtado é o autor de <i>O desenvolvimento econômico da América Latina e seus principais "
            "problemas</i> (1949), o “manifesto” da CEPAL.”</i> → ERRADO (troca de ator: é de Prebisch)",
            "<i>“Em <i>Formação Econômica do Brasil</i>, Furtado analisa o deslocamento do centro dinâmico da "
            "economia para o mercado interno após 1930.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Furtado, contemporâneo de Prebisch, debateu suas ideias e com ele formou a dupla "
                             "mais original do pensamento latino-americano."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0921
    {
        "id": "ECO-E1-0921-1", "fonte_ref": "E1-0921", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Julho/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Acerca do pensamento da CEPAL sobre o comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O modelo da CEPAL de comércio internacional argumenta que as relações comerciais entre "
                      "países desenvolvidos e em desenvolvimento não são mutuamente benéficas, mas sim "
                      "caracterizadas por uma estrutura de dependência, em que os países em desenvolvimento são "
                      "obrigados a exportar matérias-primas e commodities a preços baixos e importar produtos "
                      "manufaturados a preços elevados dos países desenvolvidos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo da CEPAL de comércio internacional argumenta que as relações comerciais entre "
                      "países desenvolvidos e em desenvolvimento <u>não são mutuamente benéficas</u>, mas sim "
                      "caracterizadas por uma <u>estrutura de dependência</u>, em que os países em desenvolvimento "
                      "são obrigados a exportar matérias-primas e commodities a preços baixos e importar produtos "
                      "manufaturados a preços elevados dos países desenvolvidos."),
        "poucas": ("O item resume, em linguagem solta, a visão " + azb("centro-periferia") + ": a divisão "
                   "internacional do trabalho concentra os ganhos no centro industrial, porque os "
                   + azb("termos de troca") + " da periferia primário-exportadora tendem a piorar."),
        "destrinchando": [
            "Contra a teoria clássica (" + oc("Ricardo") + ") e neoclássica (Heckscher-Ohlin), para as quais "
            "o comércio beneficia todos os que se especializam segundo suas vantagens comparativas, a CEPAL "
            "(" + oc("Prebisch") + ", 1949) sustentou que os ganhos são " + azb("desiguais") + ": o progresso "
            "técnico do centro fica no centro (salários e lucros maiores), e o da periferia escoa para o centro "
            "via queda de preços dos primários.",
            "Mecanismos da " + azb("deterioração dos termos de troca") + " (P<sub>X</sub>/P<sub>M</sub> da "
            "periferia): (1) " + azb("elasticidade-renda") + " baixa da demanda por primários e alta por "
            "manufaturas (lei de Engel em escala mundial); (2) mercados de manufaturas oligopolizados e com "
            "sindicatos fortes, que não repassam produtividade aos preços; (3) nos ciclos, preços primários caem "
            "mais na baixa do que sobem na alta.",
            "Consequência: a periferia precisa exportar cada vez mais para importar o mesmo volume de "
            "manufaturas, o que gera " + azb("estrangulamento externo") + " — daí a defesa da industrialização "
            "por substituição de importações, conduzida pelo Estado.",
            "Precisão de vocabulário: “dependência” é termo da " + azb("teoria da dependência") + " ("
            + oc("Cardoso e Faletto") + ", 1969; versões marxistas de " + oc("Ruy Mauro Marini") + " e "
            + oc("Gunder Frank") + "), herdeira e crítica da CEPAL. O estruturalismo cepalino fala em "
            "centro-periferia e em vulnerabilidade externa; “obrigados” e “preços baixos × elevados” são "
            "simplificações aceitas em itens de simulado.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O item afirma que o comércio “não é "
                       "mutuamente benéfico”, o que contraria a intuição ricardiana — e é exatamente a tese "
                       "cepalina. A linguagem forte (“dependência”, “obrigados”) parece exagero, mas a banca "
                       "aceitou como paráfrase. Em prova CEBRASPE, desconfie quando o item atribui à CEPAL "
                       "vocabulário marxista específico (exploração, imperialismo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para a CEPAL, a especialização segundo as vantagens comparativas distribui igualmente os ganhos "
            "do comércio entre centro e periferia.”</i> → ERRADO (contradição: é o que a CEPAL nega)",
            "<i>“A teoria da dependência, de Cardoso e Faletto, foi formulada por Prebisch no manifesto de "
            "1949.”</i> → ERRADO (anacronismo e troca de ator: 1969, outros autores)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["obrigados"], "dificuldade": 1,
        "comentario_fonte": ("Visão da CEPAL (1948): crítica à teoria clássica do comércio; heterogeneidade "
                             "estrutural, diferenciação de preços, deterioração dos termos de troca e estrutura de "
                             "dependência; requer industrialização planejada, diversificação e integração."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem usa “heterogeneidade estrutural” no sentido de "
                    "especialização centro-periferia (o conceito designa a coexistência interna de setores de "
                    "produtividades díspares) e atribui aos primários “alta elasticidade-preço da oferta”, "
                    "argumento que não é de Prebisch"],
    },
    # ------------------------------------------------------------------ E2-L00299
    {
        "id": "ECO-E2-L00299-1", "fonte_ref": "E2-L00299", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca do pensamento estruturalista latino-americano, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A teoria estruturalista da CEPAL, formulada por Prebisch e Singer, defende que a divisão "
                      "internacional do trabalho beneficia equitativamente centro e periferia, desde que a "
                      "periferia foque em suas vantagens comparativas estáticas na agricultura e mineração."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A teoria estruturalista da CEPAL, formulada por Prebisch e Singer, defende que a divisão "
                       "internacional do trabalho ") + vm("beneficia equitativamente") + az(" centro e periferia, ")
                    + vm("desde que a periferia foque em suas vantagens comparativas estáticas na agricultura e "
                         "mineração") + az(".")),
        "poucas": ("É o oposto: para a tese " + azb("Prebisch-Singer") + ", a especialização primária "
                   + vm("prejudica") + " a periferia, cujos termos de troca se deterioram; a saída é a "
                   + azb("industrialização") + "."),
        "destrinchando": [
            "Em " + vd("1949–1950") + ", " + oc("Raúl Prebisch") + " (CEPAL) e " + oc("Hans Singer") + " (ONU, "
            "Nova York) chegaram, de forma independente, à mesma conclusão empírica: os preços dos primários "
            "vinham caindo, no longo prazo, em relação aos das manufaturas. A dupla autoria dá nome à "
            + azb("tese Prebisch-Singer") + ".",
            "Implicação: seguir as " + azb("vantagens comparativas estáticas") + " (a dotação atual de terra e "
            "recursos) condena a periferia a exportar bens de preço relativo declinante. A CEPAL propõe "
            "construir vantagens " + azb("dinâmicas") + " pela industrialização (substituição de importações, "
            "proteção e planejamento estatal).",
            "Por que a deterioração: baixa elasticidade-renda da demanda por primários; mercados de "
            "manufaturas oligopolizados e trabalhadores organizados no centro (a produtividade vira salário e "
            "lucro, não preço menor); excedente de mão de obra na periferia (a produtividade vira preço menor).",
            vm("Regra-âncora: CEPAL = ganhos do comércio desiguais; especialização primária perpetua o "
               "subdesenvolvimento."),
        ],
        "dissecando": (cz("[inversão]") + " O item atribui à CEPAL a tese ricardiana que ela combate. A autoria "
                       "(Prebisch e Singer) está certa e funciona como isca. Pista: “beneficia equitativamente” "
                       "e “vantagens comparativas estáticas” são vocabulário do adversário teórico da CEPAL."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Prebisch e Singer, a especialização da periferia em bens primários tende a deteriorar seus "
            "termos de troca no longo prazo.”</i> → CERTO",
            "<i>“Hans Singer foi o primeiro secretário-executivo da CEPAL.”</i> → ERRADO (troca de ator: Singer "
            "trabalhava na sede da ONU, em Nova York)",
        ])],
        "reescrita": ("A teoria estruturalista da CEPAL, formulada por Prebisch e Singer, defende que a divisão "
                      "internacional do trabalho " + hl("não beneficia equitativamente") + " centro e periferia, "
                      + hl("pois a especialização da periferia em vantagens comparativas estáticas na agricultura "
                           "e mineração deteriora seus termos de troca") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["equitativamente", "desde que"], "dificuldade": 1,
        "comentario_fonte": ("A tese central é a deterioração dos termos de troca: a especialização em primários "
                             "prejudica a periferia; por isso defendiam a industrialização."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00704
    {
        "id": "ECO-E2-L00704-1", "fonte_ref": "E2-L00704", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CEPAL,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de “heterogeneidade estrutural” refere-se ao fato de que os países periféricos "
                      "eram especializados em produtos de baixa elasticidade-renda enquanto os países do centro "
                      "possuíam uma economia diversificada, produzindo e exportando bens manufaturados de alta "
                      "elasticidade-renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O conceito de “heterogeneidade estrutural” refere-se ") + vm("ao fato de que os países "
                    "periféricos eram especializados em produtos de baixa elasticidade-renda enquanto os países do "
                    "centro possuíam uma economia diversificada, produzindo e exportando bens manufaturados de alta "
                    "elasticidade-renda") + az(".")),
        "poucas": ("A descrição é da " + azb("especialização centro-periferia") + " (contraste " + vm("entre")
                   + " países). " + azb("Heterogeneidade estrutural") + " é o contraste " + vd("dentro")
                   + " da periferia: setores modernos de alta produtividade convivendo com setores de "
                   "subsistência."),
        "destrinchando": [
            "A CEPAL descreve a periferia com dois adjetivos: " + azb("especializada") + " (pauta exportadora "
            "concentrada em poucos primários, em contraste com o centro diversificado) e "
            + azb("heterogênea") + " (internamente, convivem ilhas de alta produtividade — enclaves exportadores, "
            "indústria moderna — e um vasto setor de baixíssima produtividade — agricultura de subsistência, "
            "informalidade).",
            "Consequências da heterogeneidade: " + azb("subemprego estrutural") + ", desigualdade de renda "
            "elevada e persistente, e salários contidos pelo excedente de mão de obra — o que ajuda a explicar "
            "por que os ganhos de produtividade da periferia não viram salários e escoam via preços.",
            "Autores: a ideia está em " + oc("Prebisch") + " desde 1949; o termo foi sistematizado por "
            + oc("Aníbal Pinto") + " (1970), e retomado por " + oc("Maria da Conceição Tavares") + " e, na "
            "CEPAL dos anos 1990, pelo neoestruturalismo.",
            "Centro × periferia: o centro é " + azb("homogêneo") + " (produtividade parecida entre setores) e "
            + azb("diversificado") + "; a periferia, " + azb("heterogênea") + " e " + azb("especializada")
            + ".",
            vm("Regra-âncora: especialização = entre países (pauta); heterogeneidade = dentro do país "
               "(produtividade)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O conteúdo descrito é verdadeiro, mas pertence a outro "
                       "conceito cepalino. É o tipo “definição certa, rótulo errado”: quem reconhece as ideias "
                       "de Prebisch marca CERTO sem checar a qual termo elas correspondem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Heterogeneidade estrutural designa a coexistência, nas economias periféricas, de setores de "
            "alta produtividade com setores de produtividade muito baixa.”</i> → CERTO",
            "<i>“Para a CEPAL, as economias centrais são heterogêneas e especializadas.”</i> → ERRADO (inversão: "
            "homogêneas e diversificadas)",
        ])],
        "reescrita": ("O conceito de “heterogeneidade estrutural” refere-se " + hl("à coexistência, nos países "
                      "periféricos, de setores de altíssima produtividade com setores de subsistência e baixíssima "
                      "produtividade") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A descrição é da tese centro-periferia; heterogeneidade estrutural é a coexistência, "
                             "na periferia, de setores de altíssima produtividade com setores de subsistência."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00705
    {
        "id": "ECO-E2-L00705-1", "fonte_ref": "E2-L00705", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CEPAL,
        "rotulo_item": "Item",
        "assertiva": ("A tese da deterioração dos termos de troca baseia-se na observação de que os ganhos de "
                      "produtividade no centro são repassados aos preços, enquanto na periferia resultam em "
                      "aumento de salários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A tese da deterioração dos termos de troca baseia-se na observação de que os ganhos de "
                       "produtividade ") + vm("no centro") + az(" são repassados aos preços, enquanto ")
                    + vm("na periferia") + az(" resultam em aumento de salários.")),
        "poucas": ("Inverteu os polos: no " + azb("centro") + ", a produtividade vira " + vd("salários e "
                   "lucros") + " (preços rígidos); na " + azb("periferia") + ", vira " + vd("queda de preços")
                   + " — e o ganho é exportado ao centro."),
        "destrinchando": [
            "Lado da oferta da tese de " + oc("Prebisch") + ": no centro, mercados de manufaturas "
            + azb("oligopolizados") + " (preço por mark-up) e " + azb("sindicatos fortes") + " permitem que "
            "trabalhadores e empresas se apropriem do progresso técnico; os preços não caem.",
            "Na periferia, mercados de primários " + azb("concorrenciais") + " e " + azb("excedente de mão de "
            "obra") + " (heterogeneidade estrutural) impedem altas de salário; o aumento de produtividade "
            "derruba o preço do primário, e quem ganha é o consumidor do centro.",
            "Resultado: P<sub>X</sub>/P<sub>M</sub> da periferia cai — " + azb("deterioração dos termos de "
            "troca") + ". Se o progresso técnico fosse repassado aos preços em toda parte, como supõe a teoria "
            "clássica, os termos de troca se moveriam a favor dos primários (de progresso técnico mais lento) e "
            "a periferia ganharia.",
            "Lado da demanda (complementar): baixa elasticidade-renda dos primários × alta das manufaturas. E "
            "um argumento cíclico: na alta, salários do centro sobem; na baixa, resistem a cair, e o ajuste "
            "recai sobre os preços primários.",
            vm("Regra-âncora: centro retém (salário e lucro); periferia repassa (preço)."),
        ],
        "dissecando": (cz("[inversão]") + " Mecanismo correto com os sujeitos trocados. Teste rápido: se a "
                       "periferia transformasse produtividade em salário e o centro baixasse preços, os termos "
                       "de troca da periferia <b>melhorariam</b> — a tese perderia o sentido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Prebisch, a organização sindical dos países centrais ajuda a explicar a rigidez dos preços "
            "das manufaturas.”</i> → CERTO",
            "<i>“A deterioração decorre de os produtos primários terem alta elasticidade-renda da demanda.”</i> "
            "→ ERRADO (dado invertido: baixa)",
        ])],
        "reescrita": ("A tese da deterioração dos termos de troca baseia-se na observação de que os ganhos de "
                      "produtividade " + hl("na periferia") + " são repassados aos preços, enquanto " + hl("no "
                      "centro") + " resultam em aumento de salários."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No centro, sindicatos e oligopólios convertem produtividade em salários e lucros; "
                             "na periferia, excedente de mão de obra faz a produtividade virar queda de preços."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01576-1 (mesmo mecanismo: estruturas de mercado e repasse de "
                    "produtividade)"],
    },
    # ------------------------------------------------------------------ E2-L00847
    {
        "id": "ECO-E2-L00847-1", "fonte_ref": "E2-L00847", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Com relação às teorias do desenvolvimento e do comércio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Nos anos 1950 e 1960, os economistas com tradição cepalina acreditavam que a oferta "
                      "agropecuária não respondia a preços, tendo sido o Brasil, à época, prisioneiro da "
                      "inelasticidade-preço da demanda internacional."),
        "gabarito": "ERRADO", "gabarito_origem": "resolvido", "status": "contestavel",
        "anotada": (az("Nos anos 1950 e 1960, os economistas com tradição cepalina acreditavam que a oferta "
                       "agropecuária não respondia a preços, tendo sido o Brasil, à época, prisioneiro da inelasticidade")
                    + vm("-preço da demanda internacional") + az(".")),
        "poucas": ("A 1ª parte é a tese estruturalista da " + azb("inelasticidade da oferta agrícola") + " "
                   "(interna). O erro está na conclusão: o gargalo apontado era da " + vm("oferta") + " "
                   "doméstica — e, no comércio exterior, a CEPAL enfatizava a baixa " + azb("elasticidade-renda")
                   + ", não a elasticidade-preço, da demanda."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte não traz gabarito; ERRADO é a resposta resolvida pelo conteúdo, e o comentário "
                          "de origem só explica a inelasticidade da <b>oferta</b>. Uma leitura benevolente daria "
                          "CERTO, porque a demanda mundial de café era de fato pouco sensível a preço, e isso "
                          "sustentou as políticas de valorização. Mas o nexo “tendo sido…” troca a oferta pela "
                          "demanda, e a CEPAL ligava a demanda externa à <b>elasticidade-renda</b>. Por isso, "
                          "ERRADO é a resposta mais defensável.")],
        "destrinchando": [
            "Os " + azb("estruturalistas") + " (" + oc("Juan Noyola") + ", " + oc("Osvaldo Sunkel") + ", "
            "CEPAL; no " + rx("Brasil") + ", " + oc("Celso Furtado") + ") explicavam a inflação latino-americana "
            "por " + azb("pontos de estrangulamento") + ". O principal era a " + azb("inelasticidade da oferta "
            "agrícola") + ": a produção de alimentos para o mercado interno não crescia nem se diversificava "
            "no ritmo da urbanização.",
            "A causa era a " + azb("estrutura agrária") + ": latifúndios pouco capitalistas, cujos donos não "
            "maximizavam lucro, e minifúndios de subsistência fora do mercado. Por isso a oferta “não respondia "
            "a preços”: a alta dos alimentos não gerava produção e virava inflação estrutural. Daí a defesa da "
            + azb("reforma agrária") + ".",
            "Contestação: estudos econométricos dos anos 1970, como os de " + oc("Affonso Celso Pastore") + " "
            "(1971), mostraram que a oferta agrícola brasileira respondia, sim, a preços relativos.",
            "No setor externo, o argumento cepalino era outro: a " + azb("baixa elasticidade-renda") + " da "
            "demanda mundial por primários. Com ela, as exportações crescem menos que as importações de "
            "manufaturas (elasticidade-renda alta), o que causa o " + azb("estrangulamento externo") + " e a "
            "deterioração dos termos de troca.",
            vm("Regra-âncora: inelasticidade da OFERTA agrícola (interna) → inflação estrutural; baixa "
               "elasticidade-RENDA da demanda externa → deterioração dos termos de troca."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " A 1ª oração reproduz o manual "
                       "estruturalista; a 2ª, ligada por “tendo sido”, cola uma consequência que não decorre "
                       "dela (oferta interna → demanda externa) e troca a elasticidade-renda pela "
                       "elasticidade-preço. Em itens de CEPAL, pergunte sempre: oferta ou demanda? preço ou "
                       "renda?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os estruturalistas atribuíam a inelasticidade da oferta agrícola à estrutura agrária "
            "latifúndio-minifúndio.”</i> → CERTO",
            "<i>“Para a CEPAL, a deterioração dos termos de troca decorria da alta elasticidade-renda da demanda "
            "por produtos primários.”</i> → ERRADO (dado invertido: baixa)",
        ])],
        "reescrita": ("Nos anos 1950 e 1960, os economistas com tradição cepalina acreditavam que a oferta "
                      "agropecuária não respondia a preços, tendo sido o Brasil, à época, prisioneiro da "
                      "inelasticidade" + hl(" da oferta agrícola interna, causada pela estrutura agrária")
                      + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Inelasticidade da oferta = incapacidade da produção agrícola para o mercado interno "
                             "de crescer e se diversificar, por causa da estrutura agrária (latifúndios não "
                             "capitalistas e minifúndios de subsistência). Sem gabarito explícito."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: fonte sem gabarito; resolvido como ERRADO (troca de oferta por demanda e de "
                    "elasticidade-renda por elasticidade-preço); leitura alternativa CERTO pela demanda "
                    "inelástica de café"],
    },
    # ------------------------------------------------------------------ E2-L01471
    {
        "id": "ECO-E2-L01471-1", "fonte_ref": "E2-L01471", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("Uma das críticas da Comissão Econômica para a América Latina (CEPAL) à teoria clássica é que "
                      "a sua análise do comércio internacional não leva em conta a dinâmica do comércio "
                      "internacional, de modo que baixas elasticidades-renda dos produtos básicos tendem a produzir "
                      "deterioração nos termos de intercâmbio dos países exportadores destes produtos ao longo do "
                      "tempo, tornando desigual a distribuição dos ganhos de comércio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma das críticas da Comissão Econômica para a América Latina (CEPAL) à teoria clássica é que "
                      "a sua análise do comércio internacional <u>não leva em conta a dinâmica</u> do comércio "
                      "internacional, de modo que <u>baixas</u> elasticidades-renda dos produtos básicos tendem a "
                      "produzir deterioração nos termos de intercâmbio dos países exportadores destes produtos ao "
                      "longo do tempo, tornando desigual a distribuição dos ganhos de comércio."),
        "poucas": ("A teoria clássica é " + azb("estática") + " (ganhos de uma especialização dada); a CEPAL "
                   "olha a " + azb("dinâmica") + ": com a renda mundial crescendo, a demanda por primários "
                   "(elasticidade-renda " + vd("< 1") + ") cresce menos e seus preços relativos caem."),
        "destrinchando": [
            azb("Elasticidade-renda da demanda") + " = %Δq / %ΔY. Alimentos e matérias-primas têm "
            + vd("ε<sub>Y</sub> < 1") + " (lei de " + oc("Engel") + ": a fatia da renda gasta com comida cai "
            "quando a renda sobe); manufaturas e bens de capital, " + vd("ε<sub>Y</sub> > 1") + ".",
            "Com o crescimento mundial, a demanda por manufaturas acelera e a por primários se arrasta. Se a "
            "oferta de primários continua crescendo (ou cresce com a produtividade), seu " + azb("preço "
            "relativo") + " cai: P<sub>X</sub>/P<sub>M</sub> da periferia se deteriora.",
            "A crítica de " + oc("Prebisch") + " e " + oc("Singer") + " a " + oc("Ricardo") + ": a vantagem "
            "comparativa mostra que o comércio é melhor que a autarquia <i>num dado momento</i>, mas cala sobre "
            "como os ganhos se repartem ao longo do tempo. Se os termos de troca pioram sistematicamente, quem "
            "exporta primários fica com fatia cada vez menor dos ganhos.",
            "Contraparte formal: a " + azb("regra de Thirlwall") + " (" + oc("A. P. Thirlwall") + ", 1979), "
            "que limita o crescimento compatível com o equilíbrio externo à razão entre as elasticidades-renda "
            "das exportações e das importações.",
            vm("Regra-âncora: periferia exporta ε-renda baixa e importa ε-renda alta → termos de troca pioram."),
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Reproduz a crítica de manual: estática × "
                       "dinâmica e elasticidade-renda baixa. O ponto de risco é a palavra “baixas”: as versões "
                       "ERRADAS do item trocam por “altas” ou trocam renda por preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…de modo que altas elasticidades-renda dos produtos básicos tendem a produzir deterioração nos "
            "termos de intercâmbio…”</i> → ERRADO (dado invertido: baixas)",
            "<i>“A CEPAL concordava com a teoria clássica quanto à distribuição equitativa dos ganhos de "
            "comércio.”</i> → ERRADO (contradição)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["tendem"], "dificuldade": 1,
        "comentario_fonte": ("CEPAL (Prebisch-Singer) critica a teoria clássica por estática; produtos primários "
                             "têm baixa elasticidade-renda; com o crescimento da renda mundial, os termos de troca "
                             "dos exportadores de commodities se deterioram."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01694-1 (mesma tese da elasticidade-renda)"],
    },
    # ------------------------------------------------------------------ E2-L01576
    {
        "id": "ECO-E2-L01576-1", "fonte_ref": "E2-L01576", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Sobre os conceitos e teorias do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Segundo Prebisch, diferenças entre as estruturas de mercado dos bens industrializados e "
                      "primários, sendo os primeiros oligopolizados e os últimos mais concorrenciais, "
                      "contribuiriam para que os ganhos do progresso tecnológico ficassem retidos nos países "
                      "industrializados, ao passo que avanços tecnológicos na produção primária reduziriam os "
                      "preços de seus produtos, contribuindo para a deterioração dos termos de troca dos países "
                      "primário-exportadores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo Prebisch, diferenças entre as estruturas de mercado dos bens industrializados e "
                      "primários, sendo os primeiros <u>oligopolizados</u> e os últimos <u>mais concorrenciais</u>, "
                      "contribuiriam para que os ganhos do progresso tecnológico ficassem <u>retidos nos países "
                      "industrializados</u>, ao passo que avanços tecnológicos na produção primária "
                      "<u>reduziriam os preços</u> de seus produtos, contribuindo para a deterioração dos termos "
                      "de troca dos países primário-exportadores."),
        "poucas": ("É o " + azb("lado da oferta") + " da tese de " + oc("Prebisch") + ": no centro "
                   "oligopolizado, a produtividade vira " + vd("lucro e salário") + "; na periferia "
                   "concorrencial, vira " + vd("preço menor") + " — e o ganho migra para o centro."),
        "destrinchando": [
            "Centro: estruturas com " + azb("poder de mercado") + " (oligopólios, preço por " + azb("mark-up")
            + " sobre o custo) e trabalhadores qualificados com " + azb("sindicatos fortes") + ". Quando o custo "
            "cai, o preço não cai: a diferença é dividida entre lucros e salários. O progresso técnico eleva a "
            "renda interna do centro.",
            "Periferia: mercados de commodities " + azb("concorrenciais") + " (tomadores de preço) e "
            + azb("excedente de mão de obra") + " que contém os salários. A redução de custo vira redução de "
            "preço, e o benefício vai para quem compra — os países centrais.",
            "Resultado: P<sub>X</sub>/P<sub>M</sub> da periferia cai. Pela teoria clássica deveria ocorrer o "
            "contrário: como a produtividade cresce mais rápido na indústria, os preços industriais deveriam "
            "cair relativamente, distribuindo o progresso técnico para o mundo todo.",
            "Esse argumento de oferta soma-se ao de demanda (elasticidade-renda baixa dos primários) e ao "
            "cíclico (salários rígidos para baixo no centro).",
            vm("Regra-âncora: oligopólio + sindicato no centro retêm o progresso técnico; concorrência + "
               "excedente de mão de obra na periferia o repassam aos preços."),
        ],
        "dissecando": (cz("[literalidade]") + " Descrição fiel do mecanismo. O que a banca troca nas versões "
                       "ERRADAS: os polos (centro concorrencial, periferia oligopolizada), o destino do ganho "
                       "(“retidos na periferia”) ou o efeito sobre preços (“elevariam os preços dos "
                       "primários”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…sendo os bens primários oligopolizados e os industrializados mais concorrenciais…”</i> → "
            "ERRADO (inversão das estruturas de mercado)",
            "<i>“Para Prebisch, o progresso técnico mais rápido na indústria levaria, pela queda dos preços "
            "industriais, à melhora dos termos de troca da periferia.”</i> → ERRADO (é a previsão clássica que "
            "ele refuta)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["contribuiriam"], "dificuldade": 1,
        "comentario_fonte": ("Mercados oligopolizados convertem produtividade em lucros e salários; mercados "
                             "concorrenciais de primários, em queda de preços, beneficiando os importadores. "
                             "Slides sobre países centrais (mark-up, sindicatos fortes) e sobre a elasticidade-"
                             "renda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 435", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 436", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00705-1 (mesmo mecanismo, versão invertida)"],
    },
    # ------------------------------------------------------------------ E2-L01694
    {
        "id": "ECO-E2-L01694-1", "fonte_ref": "E2-L01694", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Sobre os conceitos e teorias do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Segundo Prebisch, as diferenças nas elasticidades-renda de produtos primários e "
                      "industrializados era um dos fatores que contribuíam para a tendência de deterioração dos "
                      "termos de troca dos países da América Latina, o que reforçava os argumentos favoráveis à "
                      "proteção da indústria local destes países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo Prebisch, as diferenças nas elasticidades-renda de produtos primários e "
                      "industrializados era <u>um dos fatores</u> que contribuíam para a tendência de deterioração "
                      "dos termos de troca dos países da América Latina, o que reforçava os argumentos favoráveis "
                      "à <u>proteção da indústria local</u> destes países."),
        "poucas": ("Diferença de " + azb("elasticidades-renda") + " (primários baixa, manufaturas alta) → "
                   "deterioração dos termos de troca e estrangulamento externo → argumento para "
                   + azb("industrializar com proteção") + " (ISI)."),
        "destrinchando": [
            "Lado da demanda da tese de " + oc("Prebisch") + ": a periferia exporta bens de "
            + vd("baixa") + " elasticidade-renda e importa bens de " + vd("alta") + " elasticidade-renda. "
            "Quando a renda cresce (no mundo e no próprio país), as importações sobem mais que as exportações.",
            "Duas consequências: (1) preços relativos dos primários tendem a cair (termos de troca); (2) a "
            "periferia esbarra em " + azb("déficits externos crônicos") + " — o " + azb("estrangulamento "
            "externo") + " que limita o crescimento.",
            "Daí a política: produzir internamente as manufaturas importadas, com " + azb("tarifas") + ", "
            "câmbio múltiplo, crédito público e empresas estatais — a " + azb("industrialização por substituição "
            "de importações") + ". A proteção é justificada como resposta a uma assimetria estrutural, não como "
            "fim em si (um parente do argumento da " + azb("indústria nascente") + ", de " + oc("List") + ").",
            "No " + rx("Brasil") + ", a ISI orientou o Plano de Metas (1956–1961) e, mais tarde, o II PND "
            "(1974–1979).",
            "O “um dos fatores” é exato: a tese tem também o lado da oferta (oligopólios e sindicatos no centro "
            "× concorrência e excedente de mão de obra na periferia) e o argumento cíclico.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item de manual, protegido por “um dos "
                       "fatores”. A versão perigosa diria “o único fator” (modulador absoluto) ou ligaria a tese "
                       "ao livre-comércio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as diferenças nas elasticidades-renda eram o único fator a explicar a deterioração…”</i> → "
            "ERRADO (restrição indevida: havia também o lado da oferta)",
            "<i>“…o que reforçava os argumentos favoráveis à abertura comercial unilateral…”</i> → ERRADO "
            "(inversão: a conclusão era protecionista)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["um dos fatores"], "dificuldade": 1,
        "comentario_fonte": ("Primários têm baixa elasticidade-renda e manufaturas, alta; isso explica a "
                             "deterioração dos termos de troca e embasou a industrialização protegida nos anos "
                             "1950/60. Slide sobre o tema."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 498", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01471-1 (mesma tese da elasticidade-renda)"],
    },
    # ------------------------------------------------------------------ E3-L00107
    {
        "id": "ECO-E3-L00107-1", "fonte_ref": "E3-L00107", "destino": "74", "subtema": H2["cepal"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": ("A globalização do espaço econômico torna o estudo da economia internacional cada vez mais "
                    "relevante para o entendimento das relações de comércio entre as nações. A esse respeito, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a visão de Prebisch, as recorrentes crises, nas nações periféricas, causadas "
                      "pelo desequilíbrio dos balanços de pagamentos, decorreram, em parte, do fato de as baixas "
                      "elasticidades-renda da demanda de importações terem-se contraposto às altas "
                      "elasticidades-renda das exportações da periferia, o que contribuía para a deterioração dos "
                      "termos de trocas desses países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a visão de Prebisch, as recorrentes crises, nas nações periféricas, causadas "
                       "pelo desequilíbrio dos balanços de pagamentos, decorreram, em parte, do fato de as ")
                    + vm("baixas") + az(" elasticidades-renda da demanda de importações terem-se contraposto às ")
                    + vm("altas") + az(" elasticidades-renda das exportações da periferia, o que contribuía para "
                                       "a deterioração dos termos de trocas desses países.")),
        "poucas": ("Elasticidades invertidas: a periferia " + azb("importa") + " manufaturas de elasticidade-"
                   "renda " + vd("alta") + " e " + azb("exporta") + " primários de elasticidade-renda "
                   + vd("baixa") + ". Por isso suas importações crescem mais que as exportações."),
        "destrinchando": [
            "Exportações da periferia = alimentos e matérias-primas: quando o mundo enriquece, não passa a "
            "comer proporcionalmente mais (" + oc("Engel") + "); a demanda cresce menos que a renda → "
            + vd("ε<sub>Y</sub> baixa") + ".",
            "Importações da periferia = máquinas, bens duráveis, tecnologia: quando a periferia cresce, sua "
            "demanda por esses bens dispara → " + vd("ε<sub>Y</sub> alta") + ".",
            "Combinação: para um mesmo crescimento da renda, M cresce mais que X → " + azb("déficit externo "
            "estrutural") + ", crises cambiais recorrentes e pressão para baixo sobre os preços relativos "
            "exportados (" + azb("deterioração dos termos de troca") + "). É o " + azb("estrangulamento "
            "externo") + " cepalino.",
            "Formalização posterior: " + azb("lei de Thirlwall") + " — a taxa de crescimento compatível com o "
            "equilíbrio externo é " + vd("y = ε<sub>X</sub>·z / π") + " (z = crescimento mundial; "
            "ε<sub>X</sub> e π = elasticidades-renda das exportações e das importações). Com ε<sub>X</sub> "
            "baixa e π alta, o crescimento da periferia fica abaixo do mundial.",
            vm("Regra-âncora: periferia exporta ε-renda BAIXA e importa ε-renda ALTA."),
        ],
        "dissecando": (cz("[inversão]") + " Todo o resto do item é verdadeiro (crises de balanço, “em parte”, "
                       "deterioração); só as elasticidades foram trocadas de lugar. Teste de coerência: com "
                       "exportações de elasticidade alta, o crescimento mundial <b>melhoraria</b> o balanço da "
                       "periferia, e não haveria crise."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…do fato de as altas elasticidades-renda da demanda de importações terem-se contraposto às "
            "baixas elasticidades-renda das exportações da periferia…”</i> → CERTO",
            "<i>“…do fato de as altas elasticidades-preço da demanda por exportações primárias…”</i> → ERRADO "
            "(troca de conceito: o argumento é de elasticidade-renda)",
        ])],
        "reescrita": ("De acordo com a visão de Prebisch, as recorrentes crises, nas nações periféricas, causadas "
                      "pelo desequilíbrio dos balanços de pagamentos, decorreram, em parte, do fato de as "
                      + hl("altas") + " elasticidades-renda da demanda de importações terem-se contraposto às "
                      + hl("baixas") + " elasticidades-renda das exportações da periferia, o que contribuía para "
                      "a deterioração dos termos de trocas desses países."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["em parte"], "dificuldade": 2,
        "comentario_fonte": ("Prebisch diz o oposto: exportações primárias com baixa elasticidade-renda e "
                             "importações de manufaturas com alta; o descompasso gera déficit externo "
                             "estrutural. Reescrita: altas para importações, baixas para exportações."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0643
    {
        "id": "ECO-E1-0643-1", "fonte_ref": "E1-0643", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Simulado Setembro/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": "Acerca das teorias do comércio internacional, julgue o item a seguir.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria de Linder, a produção de bens para exportação independe da "
                      "existência de demanda doméstica por esses bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a teoria de Linder, a produção de bens para exportação ")
                    + vm("independe") + az(" da existência de demanda doméstica por esses bens.")),
        "poucas": ("Para " + oc("Linder") + ", é o contrário: um bem só se torna exportação potencial se antes "
                   "houver " + azb("demanda representativa") + " por ele no mercado interno."),
        "destrinchando": [
            oc("Staffan Burenstam Linder") + " (<i>An Essay on Trade and Transformation</i>, " + vd("1961")
            + ") desloca a explicação do comércio de manufaturas para o " + azb("lado da demanda") + ". As "
            "empresas inovam para o mercado que conhecem, o doméstico; só depois, já com escala e produto "
            "testado, exportam.",
            "Logo, a pauta exportadora de manufaturas espelha a " + azb("demanda representativa") + " interna. E "
            "o destino natural dessas exportações são países com estrutura de demanda parecida, que depende "
            "sobretudo da " + azb("renda per capita") + ": a " + azb("hipótese da sobreposição de demandas") + " "
            "(<i>overlapping demand</i>).",
            "Previsão: o comércio de manufaturas é mais intenso entre países de renda semelhante — o oposto de "
            "Heckscher-Ohlin, que prevê mais comércio entre países com dotações diferentes. Explica o peso do "
            "comércio Norte-Norte e ajuda a explicar o " + azb("comércio intraindustrial") + ".",
            "Escopo: a teoria vale para " + azb("manufaturas diferenciadas") + "; o comércio de primários "
            "continua explicado por dotações de fatores (H-O). Crítica: difícil de testar, porque a renda per "
            "capita semelhante também se correlaciona com proximidade geográfica e cultural.",
            vm("Regra-âncora: Linder = demanda interna primeiro, exportação depois; países de renda parecida "
               "comerciam mais."),
        ],
        "dissecando": (cz("[contradição]") + " O item nega o núcleo da teoria. Quem associa “comércio” a "
                       "“oferta e custos” (Ricardo, H-O) aceita a ideia de que exportar independe do mercado "
                       "doméstico. 🔥 Linder costuma vir em contraste com H-O: renda semelhante × dotações "
                       "diferentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Linder, o comércio de manufaturas tende a ser mais intenso entre países com níveis de "
            "renda per capita semelhantes.”</i> → CERTO",
            "<i>“A hipótese de Linder explica sobretudo o comércio de bens primários entre países com dotações "
            "de fatores distintas.”</i> → ERRADO (troca de conceito: manufaturas e países semelhantes)",
        ])],
        "reescrita": ("De acordo com a teoria de Linder, a produção de bens para exportação " + hl("depende")
                      + " da existência de demanda doméstica por esses bens."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Linder defende que a produção para exportação é fortemente influenciada pela "
                             "demanda doméstica (demanda representativa); países com renda e preferências "
                             "semelhantes comerciam mais; aplica-se a manufaturados; ajuda a explicar o comércio "
                             "intraindústria. Críticas: dificuldade de teste empírico."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (193).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto reconstruído pelo comentário"}],
        "alertas": ["texto_reconstruido: frente original era só imagem (image (193).png); assertiva reconstruída "
                    "pelo comentário (“A teoria de Linder defende justamente que a produção de bens para "
                    "exportação é fortemente influenciada pela demanda doméstica”), que refuta a negação desse "
                    "núcleo; redação exata do item não recuperada — conferir com a imagem"],
    },
    # ------------------------------------------------------------------ E1-0644
    {
        "id": "ECO-E1-0644-1", "fonte_ref": "E1-0644", "destino": "75", "subtema": H2["novas"],
        "tipo": "DISC", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Responda à questão a seguir, sobre as teorias do comércio internacional.",
        "rotulo_item": "Questão",
        "assertiva": "O que é o comércio intra-indústria e como foi abordado por teorias do comércio internacional?",
        "gabarito": "RESPOSTA", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Comércio intraindústria é a exportação e a importação simultâneas, por um mesmo país, de "
                      "bens do mesmo setor (carros por carros), em geral entre países de renda e dotações "
                      "semelhantes. Ricardo e Heckscher-Ohlin não o explicam, porque preveem especialização "
                      "interindustrial. As novas teorias o explicam por economias de escala, diferenciação de "
                      "produtos e concorrência monopolística (Krugman, Helpman), com o reforço da demanda "
                      "representativa de Linder e da diferenciação vertical. Mede-se pelo índice de Grubel-Lloyd."),
        "poucas": ("Comércio " + azb("intraindústria") + " = trocar bens do " + vd("mesmo setor") + ". As teorias "
                   "clássicas não o explicam; a " + azb("nova teoria do comércio") + " o explica por "
                   + azb("escala") + " + " + azb("diferenciação") + " + " + azb("gosto pela variedade") + "."),
        "destrinchando": [
            "<b>Definição</b>: fluxos bilaterais de produtos da mesma indústria — a Alemanha exporta e importa "
            "automóveis da França. Contrasta com o " + azb("comércio interindustrial") + " (vinho por tecido), "
            "explicado por vantagens comparativas. Cresceu muito no pós-guerra, sobretudo entre países "
            "desenvolvidos e dentro de blocos (CEE).",
            "<b>Medida</b>: índice de " + oc("Grubel e Lloyd") + " (1975): " + vd("GL = 1 − |X − M| / (X + M)")
            + ". Vale 0 quando o comércio no setor é só num sentido (interindustrial) e 1 quando X = M "
            "(intraindustrial puro).",
            "<b>Teorias clássicas</b>: " + oc("Ricardo") + " (produtividade) e " + oc("Heckscher-Ohlin")
            + " (dotações) supõem concorrência perfeita, retornos constantes e bens homogêneos: preveem "
            "especialização em setores diferentes e mais comércio entre países diferentes. Não explicam o "
            "comércio intraindustrial nem o fato de o grosso do comércio ocorrer entre países parecidos.",
            "<b>Nova teoria do comércio</b> (" + oc("Krugman") + ", 1979–1980; " + oc("Helpman") + "; base em "
            + oc("Dixit-Stiglitz") + "): com " + azb("economias de escala internas") + ", cada firma produz "
            "poucas variedades em grande escala; com " + azb("concorrência monopolística") + " e consumidores "
            "que valorizam a " + azb("variedade") + ", cada país se especializa em variedades diferentes e "
            "troca-as. Ganhos: mais variedade e preços menores (custo médio menor). Krugman ganhou o Nobel de "
            + vd("2008") + ".",
            "<b>Complementos</b>: " + oc("Linder") + " (1961) — países de renda parecida têm demandas "
            "parecidas e trocam manufaturas semelhantes; " + azb("diferenciação vertical") + " (qualidade) e "
            + azb("horizontal") + " (atributos e gostos); fragmentação da produção em cadeias globais de valor. "
            "O " + azb("ciclo do produto") + " de " + oc("Vernon") + " (1966) explica a migração da produção "
            "no tempo, não propriamente o comércio intraindustrial.",
            "<b>Implicação de política</b>: o ajuste à abertura é menos custoso que no comércio "
            "interindustrial (as firmas se realocam dentro do setor, sem fechar setores inteiros) — um dos "
            "motivos do sucesso da integração europeia.",
        ],
        "dissecando": (cz("[exercício aberto]") + " Em C/E, a banca transforma isso em itens como: “o modelo "
                       "ricardiano explica o comércio intrassetorial” (ERRADO), “a nova teoria descarta as "
                       "vantagens comparativas” (ERRADO: complementa) e “o comércio intraindustrial predomina "
                       "entre países de renda semelhante” (CERTO)."),
        "modulos": [("🃏 Carta na manga", [
            "A nova teoria mostra que vantagens podem ser " + azb("criadas") + " (escala, história, aprendizado) "
            "e não só herdadas (dotações) — argumento útil para discutir política industrial e integração "
            "regional, como o " + rx("Mercosul") + ", em discursivas.",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Três respostas empilhadas: definição (troca simultânea de produtos similares da "
                             "mesma indústria), insuficiência de Ricardo e H-O, nova teoria (Krugman/Helpman: "
                             "escala, diferenciação, concorrência monopolística), Linder, Vernon, índice de "
                             "Grubel-Lloyd e implicações de política."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0858
    {
        "id": "ECO-E1-0858-1", "fonte_ref": "E1-0858", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Maio/2026", "ano": 2026,
        "cacd": False, "errei": False,
        "comando": ("No que diz respeito à Teoria do Comércio Internacional, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Quando um país apresenta economias de escala em determinado setor, nem os preços dos "
                      "produtos nem a remuneração dos fatores são suficientes para prever o padrão de comércio com "
                      "seus parceiros comerciais. Isso ocorre porque a presença de rendimentos crescentes de escala "
                      "permite ao país reduzir os custos médios ao aumentar o volume produzido e isso fará com que "
                      "passe a ser exportador líquido dos produtos desse setor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando um país apresenta economias de escala em determinado setor, <u>nem os preços dos "
                      "produtos nem a remuneração dos fatores são suficientes</u> para prever o padrão de comércio "
                      "com seus parceiros comerciais. Isso ocorre porque a presença de rendimentos crescentes de "
                      "escala permite ao país reduzir os custos médios ao aumentar o volume produzido e isso fará "
                      "com que passe a ser exportador líquido dos produtos desse setor."),
        "poucas": ("Com " + azb("rendimentos crescentes") + ", quem produz mais tem custo médio menor: a "
                   "especialização pode ser decidida por " + vd("história, tamanho do mercado e pioneirismo")
                   + ", e não só por preços autárquicos ou dotações de fatores."),
        "destrinchando": [
            "Nos modelos clássicos (" + oc("Ricardo") + ", " + oc("Heckscher-Ohlin") + "), basta comparar "
            "preços relativos de autarquia (ou dotações e remunerações de fatores) para prever quem exporta "
            "o quê. Isso supõe " + azb("retornos constantes") + ".",
            "Com " + azb("economias de escala") + ", o custo médio cai com o volume. Quem sai na frente — por "
            "acaso histórico, mercado interno grande ou política industrial — ganha escala, barateia o produto "
            "e consolida a liderança (" + azb("vantagem do pioneiro") + ", " + azb("path dependence") + "). "
            "Dois países idênticos podem especializar-se de modos diferentes, e o padrão resultante não se "
            "deduz dos fundamentos iniciais.",
            "Exemplos clássicos: a indústria de relógios na Suíça, o polo de semicondutores no Vale do Silício, "
            "a disputa Airbus × Boeing — vantagens " + azb("criadas") + ", e não herdadas.",
            "Base teórica: " + oc("Paul Krugman") + " (1979, 1980; Nobel " + vd("2008") + "), com escala "
            "interna e concorrência monopolística; " + azb("economias externas") + " (clusters) produzem o mesmo "
            "efeito de travamento. É também o fundamento da " + azb("política comercial estratégica") + ".",
            "Leitura do “fará com que passe a ser exportador líquido”: é a tendência do modelo para o país que "
            "obtém a escala no setor; o essencial do item é a imprevisibilidade a partir de preços e fatores.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O item afirma que os determinantes clássicos "
                       "“não bastam”, o que soa como heresia para quem estudou só H-O — e é a tese da nova "
                       "teoria. O “nem… nem…” não é modulador absoluto aqui: diz que não são suficientes, não "
                       "que são irrelevantes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com economias de escala, o padrão de comércio é integralmente determinado pela dotação relativa "
            "de fatores.”</i> → ERRADO (contradição: a escala e a história também decidem)",
            "<i>“Na presença de rendimentos crescentes, países com dotações idênticas podem ter ganhos com o "
            "comércio ao se especializarem em produtos diferentes.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["nem… nem…", "suficientes"],
        "dificuldade": 2,
        "comentario_fonte": ("Quatro comentários fundidos (inclui duplicatas E3-L00219 e E3-L00257): com "
                             "rendimentos crescentes, custos médios caem com a produção; história, tamanho de "
                             "mercado e pioneirismo podem determinar o comércio; base da nova teoria do comércio "
                             "(Krugman, 1979)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00219-1, ECO-E3-L00257-1 (mesmo item em outra prova)"],
    },
    # ------------------------------------------------------------------ E1-0898
    {
        "id": "ECO-E1-0898-1", "fonte_ref": "E1-0898", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": "Acerca das economias de escala e do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na existência de economias de escala na produção de um bem, a fronteira de possibilidades "
                      "de produção de um país é linear."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na existência de economias de escala na produção de um bem, a fronteira de "
                       "possibilidades de produção de um país é ") + vm("linear") + az(".")),
        "poucas": ("FPP " + azb("linear") + " = custo de oportunidade " + vd("constante") + " (rendimentos "
                   "constantes, como em Ricardo). Com economias de escala, o custo de oportunidade "
                   + vd("cai") + " com a especialização, e a FPP fica " + vm("convexa em relação à origem") + "."),
        "destrinchando": [
            "A inclinação da " + azb("FPP") + " é o " + azb("custo de oportunidade") + " de um bem em termos do "
            "outro. Seu formato resume a tecnologia: " + vd("reta") + " (custo constante: um fator, retornos "
            "constantes — o modelo ricardiano); " + vd("côncava") + " (custo crescente: fatores específicos ou "
            "intensidades diferentes — H-O); " + vd("convexa") + " em relação à origem (custo decrescente: "
            + azb("rendimentos crescentes") + ").",
            "Com economias de escala, cada unidade a mais de X fica mais barata em termos de Y quanto mais X se "
            "produz: concentrar recursos num bem rende mais do que dividi-los. A FPP se curva para dentro, e os "
            "pontos interiores da curva (produção diversificada) são relativamente ineficientes.",
            "Implicação para o comércio: a " + azb("especialização completa") + " é vantajosa mesmo entre "
            "países idênticos — cada um concentra a produção num bem, explora a escala e troca. É o argumento "
            "da nova teoria do comércio (" + oc("Krugman") + ") para o ganho de comércio sem diferença de "
            "tecnologia ou de dotação.",
            "Cuidado: com FPP convexa, o equilíbrio de autarquia pode ser instável e há múltiplos padrões de "
            "especialização possíveis — qual país fica com qual setor depende da história.",
            vm("Regra-âncora: reta = custo constante; côncava = custo crescente; convexa = economias de escala."),
        ],
        "grafico_verso": "ECO-E1-0898-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item associa à escala o formato que pertence aos "
                       "rendimentos constantes. Quem decorou “FPP ricardiana é reta” e liga Ricardo a "
                       "especialização completa pode transferir a reta para o caso da escala. Pista: escala "
                       "muda o custo conforme o volume — nada de constante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, com um único fator e retornos constantes, a FPP é linear.”</i> → CERTO",
            "<i>“Com economias de escala, a FPP é côncava em relação à origem.”</i> → ERRADO (troca de conceito: "
            "côncava indica custos crescentes)",
        ])],
        "reescrita": ("Na existência de economias de escala na produção de um bem, a fronteira de possibilidades "
                      "de produção de um país é " + hl("convexa em relação à origem") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A FPP linear resulta de rendimentos constantes de escala, não de rendimentos "
                             "crescentes."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0920
    {
        "id": "ECO-E1-0920-1", "fonte_ref": "E1-0920", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Julho/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Acerca das teorias do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Um dos aspectos positivos do modelo de vantagens comparativas de David Ricardo é que ele "
                      "consegue explicar de forma adequada a dinâmica do comércio intrassetorial entre os países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um dos aspectos ") + vm("positivos") + az(" do modelo de vantagens comparativas de David "
                                                                  "Ricardo é que ele ")
                    + vm("consegue") + az(" explicar de forma adequada a dinâmica do comércio intrassetorial "
                                          "entre os países.")),
        "poucas": ("O modelo ricardiano explica o comércio " + azb("interindustrial") + " (vinho por tecido). O "
                   "comércio " + azb("intrassetorial") + " é justamente a sua maior lacuna, preenchida pela "
                   + azb("nova teoria do comércio") + "."),
        "destrinchando": [
            oc("Ricardo") + " (<i>Princípios</i>, " + vd("1817") + "): um fator (trabalho), produtividades "
            "diferentes entre países, retornos constantes, bens homogêneos e concorrência perfeita. Cada país "
            "se especializa no bem de menor custo de oportunidade — e o importa do outro. Por construção, um "
            "país não exporta e importa o mesmo bem.",
            "O comércio " + azb("intrassetorial") + " (intraindustrial) — carros alemães por carros franceses — "
            "exige bens " + azb("diferenciados") + " e " + azb("economias de escala") + ", ausentes do modelo. "
            "Explicação: " + oc("Krugman") + " e " + oc("Helpman") + " (concorrência monopolística, gosto pela "
            "variedade), com contribuições de " + oc("Linder") + " (demanda representativa).",
            "O que Ricardo explica bem: que há ganho de comércio mesmo quando um país é mais produtivo em tudo "
            "(vantagem comparativa × absoluta); e o padrão Norte-Sul de troca de bens diferentes.",
            "Heckscher-Ohlin tem a mesma limitação: dotações diferentes → setores diferentes. Por isso nenhum "
            "dos dois explica que o grosso do comércio mundial ocorra entre países ricos e parecidos.",
            vm("Regra-âncora: clássicos → interindustrial; nova teoria → intraindustrial."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui ao modelo clássico o fenômeno que motivou as "
                       "teorias que o sucederam. O elogio inicial (“aspectos positivos”) baixa a guarda. 🔥 A "
                       "banca repete o padrão com H-O e com o ciclo do produto de Vernon."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma das limitações do modelo ricardiano é não explicar o comércio intrassetorial.”</i> → CERTO",
            "<i>“O modelo de Heckscher-Ohlin explica o comércio intraindustrial entre países com dotações "
            "semelhantes.”</i> → ERRADO (troca de conceito: H-O explica o interindustrial)",
        ])],
        "reescrita": ("Um dos aspectos " + hl("negativos") + " do modelo de vantagens comparativas de David "
                      "Ricardo é que ele " + hl("não consegue") + " explicar de forma adequada a dinâmica do "
                      "comércio intrassetorial entre os países."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O modelo ricardiano baseia-se em especialização e vantagens comparativas entre bens "
                             "diferentes; o comércio intrassetorial é explicado por diferenciação, economias de "
                             "escala e concorrência monopolística (Krugman)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0922
    {
        "id": "ECO-E1-0922-1", "fonte_ref": "E1-0922", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Acerca das teorias modernas do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Entre as diversas teorias modernas do comércio internacional, existe uma que enfatiza, como "
                      "fatores explicativos do comércio, o tamanho das economias, mensurado pelo PIB e pela "
                      "renda, e a distância entre os países. Essa teoria ficou conhecida como Modelo "
                      "Gravitacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Entre as diversas teorias modernas do comércio internacional, existe uma que enfatiza, como "
                      "fatores explicativos do comércio, <u>o tamanho das economias</u>, mensurado pelo PIB e pela "
                      "renda, e <u>a distância</u> entre os países. Essa teoria ficou conhecida como "
                      "<u>Modelo Gravitacional</u>."),
        "poucas": ("No " + azb("modelo gravitacional") + ", o comércio entre dois países cresce com o "
                   + vd("tamanho") + " das duas economias (PIB) e diminui com a " + vd("distância") + " entre "
                   "elas — por analogia com a gravitação de Newton."),
        "destrinchando": [
            "Forma básica, proposta por " + oc("Jan Tinbergen") + " (" + vd("1962") + "): "
            + vd("T<sub>ij</sub> = A · Y<sub>i</sub> · Y<sub>j</sub> / D<sub>ij</sub>") + ", em que T é o "
            "comércio bilateral, Y os PIBs e D a distância. Em logaritmos, vira uma regressão linear "
            "estimável.",
            "Por que funciona: economias grandes produzem mais variedades para vender e têm mais renda para "
            "comprar; a distância representa custos de transporte, de informação e diferenças culturais. Com "
            "variáveis extras (fronteira comum, idioma, passado colonial, acordos de comércio), é um dos "
            "resultados empíricos mais robustos da economia.",
            "Usos: medir o efeito de acordos (o comércio “a mais” gerado por um bloco), o " + azb("efeito "
            "fronteira") + " (estudo de " + oc("McCallum") + ", 1995: províncias canadenses comerciavam muito "
            "mais entre si do que com estados americanos equivalentes) e o comércio potencial entre parceiros.",
            "Fundamentação teórica posterior (" + oc("Anderson") + ", 1979; " + oc("Anderson e van Wincoop")
            + ", 2003, com a “resistência multilateral”): a equação gravitacional decorre de modelos com bens "
            "diferenciados, inclusive os de concorrência monopolística.",
            "Para o " + rx("Brasil") + ": a distância ajuda a explicar o peso relativamente modesto do comércio "
            "com a Ásia até a ascensão chinesa, e o tamanho da China explica por que ela virou o principal "
            "parceiro comercial brasileiro (desde 2009).",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. As versões ERRADAS costumam inverter o sinal "
                       "da distância (“o comércio aumenta com a distância”) ou trocar o nome (atribuir a "
                       "Linder ou a H-O)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o modelo gravitacional, o comércio bilateral tende a crescer com a distância entre os "
            "países.”</i> → ERRADO (inversão: diminui com a distância)",
            "<i>“O modelo gravitacional foi aplicado pioneiramente ao comércio por Jan Tinbergen, nos anos "
            "1960.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só repete a assertiva com o gabarito CERTO.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “mensurado por pelo PIB” corrigido para “mensurado pelo PIB”"],
    },
    # ------------------------------------------------------------------ E2-L00203
    {
        "id": "ECO-E2-L00203-1", "fonte_ref": "E2-L00203", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_06,
        "rotulo_item": "Item",
        "assertiva": ("Modelos comerciais como de Kemp indicam que há diversas fontes para a economia de escala no "
                      "comércio internacional. Tais economias podem ocorrer dentro da firma, fora dela ou entre "
                      "países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Modelos comerciais como de Kemp indicam que há <u>diversas fontes</u> para a economia de "
                      "escala no comércio internacional. Tais economias podem ocorrer <u>dentro da firma, fora "
                      "dela ou entre países</u>."),
        "poucas": ("As economias de escala podem ser " + azb("internas") + " à firma, " + azb("externas")
                   + " à firma mas internas à indústria nacional, ou " + azb("internacionais") + " (externas à "
                   "indústria de um país, ligadas ao tamanho do mercado mundial)."),
        "destrinchando": [
            azb("Internas à firma") + ": o custo médio cai com a produção da própria empresa (custos fixos "
            "diluídos, especialização de plantas). Levam a mercados de " + azb("concorrência imperfeita")
            + " (monopolística, oligopólio) — base do modelo de " + oc("Krugman") + ".",
            azb("Externas à firma") + " (marshallianas): o custo de cada empresa cai com o tamanho da "
            + azb("indústria") + " local — fornecedores especializados, mercado de trabalho qualificado, "
            "transbordamento de conhecimento (clusters). Compatíveis com concorrência perfeita. " + oc("Murray "
            "Kemp") + " (anos 1960) estudou o comércio com essas economias externas.",
            azb("Internacionais") + ": dependem do tamanho da indústria " + azb("mundial") + ", não da nacional "
            "— a divisão do trabalho em insumos intermediários negociados entre países (" + oc("Wilfred Ethier")
            + ", 1982). Ajudam a explicar ganhos de integração comercial e cadeias de valor.",
            "Consequências comuns: o comércio pode surgir sem diferenças de tecnologia ou dotação; o padrão de "
            "especialização depende da história; e há espaço teórico para política industrial e comercial "
            "estratégica.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item de classificação, protegido por "
                       "“podem ocorrer”. O nome de Kemp intimida, mas o conteúdo é a tipologia padrão "
                       "(interna, externa, internacional)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As economias de escala relevantes para o comércio ocorrem exclusivamente dentro da firma.”</i> "
            "→ ERRADO (restrição indevida: também externas e internacionais)",
            "<i>“Economias externas à firma são compatíveis com concorrência perfeita na indústria.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["podem"], "dificuldade": 2,
        "comentario_fonte": ("Escala interna à firma (custos médios caem com a produção), externa (spillovers, "
                             "aglomeração) e por integração entre países; o comércio pode surgir sem diferenças "
                             "tecnológicas ou fatoriais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00204
    {
        "id": "ECO-E2-L00204-1", "fonte_ref": "E2-L00204", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_06,
        "rotulo_item": "Item",
        "assertiva": ("Para certas economias com grande quantidade de monopólios que ofertam produtos essenciais à "
                      "população e que operam em parte elástica da curva de demanda, o fechamento econômico é uma "
                      "alternativa viável."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Para <u>certas</u> economias com grande quantidade de monopólios que ofertam produtos "
                      "essenciais à população e que operam em parte elástica da curva de demanda, o fechamento "
                      "econômico é uma alternativa <u>viável</u>."),
        "poucas": ("A fonte dá CERTO: em mercados imperfeitos, os resultados de bem-estar do comércio são "
                   + azb("contingentes") + ", e restringir o comércio “pode” ser defensável em casos "
                   "particulares. Mas a lição-padrão vai no sentido oposto: a abertura " + vm("disciplina")
                   + " monopólios."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Mantido o CERTO da fonte, mas a resposta mais defensável é ERRADO. (1) O "
                          + azb("efeito pró-competitivo") + " do comércio (Krugman e Obstfeld): com a abertura, "
                          "o monopolista doméstico enfrenta concorrência importada, cobra preço menor e produz "
                          "mais; fechar a economia faz o contrário e eleva o peso morto. (2) O enunciado é "
                          "internamente frágil: produto “essencial” sugere demanda inelástica, e todo "
                          "monopolista já opera no trecho elástico da demanda (onde RMg > 0), de modo que essa "
                          "condição nada acrescenta. O próprio comentário de origem fala em demanda "
                          "“relativamente inelástica”, ao contrário do item, e admite tratar-se de resultado "
                          "contingente, não de regra.")],
        "destrinchando": [
            "Monopólio: maximiza lucro onde " + vd("RMg = CMg") + ". Como RMg = P(1 − 1/|ε|), RMg > 0 exige "
            + vd("|ε| > 1") + ": o monopolista sempre produz no " + azb("trecho elástico") + " da demanda. Quanto "
            "menos elástica a demanda, maior o " + azb("mark-up") + " (índice de Lerner = 1/|ε|).",
            "Abertura comercial com monopólio doméstico: o preço mundial vira teto efetivo. O monopolista "
            "deixa de restringir a oferta, o preço cai, a quantidade sobe e o peso morto encolhe — ganho "
            "adicional ao da vantagem comparativa. Por isso a abertura é recomendada como " + azb("política de "
            "concorrência") + " em economias pequenas e concentradas.",
            "Onde a teoria admite proteção: argumento da " + azb("indústria nascente") + " (" + oc("List")
            + "), " + azb("política comercial estratégica") + " em oligopólios internacionais (" + oc("Brander e "
            "Spencer") + ": subsídio ou tarifa que transfere renda de monopólio estrangeiro para o nacional), "
            "tarifa ótima de país grande (termos de troca) e falhas de mercado domésticas. Em todos, a "
            "restrição é seletiva, e nunca “fechamento econômico”.",
            "Moral para a prova: em concorrência imperfeita, “pode” e “em certos casos” abrem espaço para CERTO; "
            "mas itens que recomendam autarquia como resposta a monopólios contrariam o resultado de manual.",
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " A banca se apoia em “certas economias” e "
                       "“alternativa viável” para sustentar o CERTO, como resultado excepcional de concorrência "
                       "imperfeita. A combinação de “essenciais” com “parte elástica” é ruído técnico: não há "
                       "modelo-padrão em que ela justifique autarquia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A abertura comercial tende a reduzir o poder de mercado de monopólios domésticos, ao expô-los à "
            "concorrência importada.”</i> → CERTO",
            "<i>“Um monopolista maximizador de lucro opera no trecho inelástico da curva de demanda.”</i> → "
            "ERRADO (inversão: opera no trecho elástico, onde RMg > 0)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["certas", "viável"], "dificuldade": 3,
        "comentario_fonte": ("Com monopólios de bens essenciais e demanda relativamente inelástica, a abertura "
                             "pode elevar preços internos e deteriorar termos de troca; alguns modelos admitem "
                             "que restrição comercial eleve o bem-estar; resultado contingente, não regra geral."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: gabarito CERTO da fonte mantido, mas o efeito pró-competitivo da abertura "
                    "sustenta ERRADO; enunciado combina bens essenciais com trecho elástico da demanda, e o "
                    "comentário de origem fala em demanda inelástica"],
    },
    # ------------------------------------------------------------------ E2-L00205
    {
        "id": "ECO-E2-L00205-1", "fonte_ref": "E2-L00205", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_06,
        "rotulo_item": "Item",
        "assertiva": ("As diferenciações dos produtos no comércio internacional podem ser vertical (atributos "
                      "associados à qualidade dos produtos com finalidades semelhantes) e/ou horizontal (atributos "
                      "associados às características dos produtos)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As diferenciações dos produtos no comércio internacional podem ser <u>vertical (atributos "
                      "associados à qualidade</u> dos produtos com finalidades semelhantes) e/ou <u>horizontal "
                      "(atributos associados às características</u> dos produtos)."),
        "poucas": (azb("Vertical") + " = mesma função, " + vd("qualidades") + " diferentes (há um “melhor” "
                   "objetivo). " + azb("Horizontal") + " = qualidade parecida, " + vd("características") + " "
                   "diferentes (cor, design, marca, sabor), escolhidas por gosto."),
        "destrinchando": [
            azb("Diferenciação vertical") + ": a preço igual, todos os consumidores escolheriam a mesma "
            "variedade (a de maior qualidade). Quem compra a pior o faz por restrição de renda. Ex.: carro "
            "popular × sedã de luxo da mesma marca. Ligada a diferenças de renda e de dotação (capital, "
            "tecnologia) entre países.",
            azb("Diferenciação horizontal") + ": a preço igual, consumidores diferentes escolheriam variedades "
            "diferentes — não há ordem objetiva. Ex.: refrigerante de cola × guaraná; carros compactos de "
            "marcas distintas. Base do " + azb("gosto pela variedade") + " no modelo de " + oc("Krugman") + " "
            "(" + oc("Dixit-Stiglitz") + ").",
            "Ambas sustentam o " + azb("comércio intraindustrial") + ": a horizontal explica trocas entre "
            "países semelhantes (carros alemães por franceses); a vertical, trocas de variedades de qualidade "
            "diferente, muitas vezes entre países de renda distinta (exportar o modelo topo de linha e importar "
            "o básico).",
            "O “e/ou” é exato: um mesmo produto pode diferir nas duas dimensões (um smartphone pode ser melhor "
            "e também de outra marca e design).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definições de manual. A armadilha está na "
                       "proximidade dos parênteses: “qualidade” × “características” parece distinção vaga, e "
                       "o candidato desconfia. As versões ERRADAS trocam os rótulos (vertical = características; "
                       "horizontal = qualidade)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na diferenciação horizontal, os produtos têm qualidades distintas e a mesma finalidade.”</i> → "
            "ERRADO (troca de conceito: isso é a vertical)",
            "<i>“A diferenciação horizontal está associada à preferência dos consumidores pela variedade.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["e/ou"], "dificuldade": 1,
        "comentario_fonte": ("Vertical = qualidade (mesma finalidade, níveis distintos); horizontal = variedades "
                             "de qualidade similar e atributos distintos (marca, design, sabor); ambas sustentam o "
                             "comércio intrassetorial."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00216-1 (mesma definição de diferenciação vertical)"],
    },
    # ------------------------------------------------------------------ E2-L00206
    {
        "id": "ECO-E2-L00206-1", "fonte_ref": "E2-L00206", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_06,
        "rotulo_item": "Item",
        "assertiva": ("O comércio intrassetorial é definido como o intercâmbio entre dois países com exportações e "
                      "importações simultâneas de produtos pertencentes a uma mesma indústria, por exemplo, quando "
                      "a matriz de uma montadora automobilística francesa importa de sua filial posicionada na "
                      "Argentina."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O comércio intrassetorial é definido como o intercâmbio entre dois países com exportações e "
                       "importações simultâneas de produtos pertencentes a uma mesma indústria, por exemplo, quando ")
                    + vm("a matriz de uma montadora automobilística francesa importa de sua filial posicionada na "
                         "Argentina") + az(".")),
        "poucas": ("A definição está certa; o " + vm("exemplo") + " não: matriz importando da filial é "
                   + azb("comércio intrafirma") + " (critério societário), e num só sentido. Intrassetorial é "
                   "França exportar e importar automóveis, quem quer que sejam as empresas."),
        "destrinchando": [
            azb("Comércio intrassetorial") + " (intraindustrial): critério " + azb("setorial") + " e "
            + azb("bilateral") + " — o país exporta e importa bens da mesma indústria. Mede-se com dados "
            "agregados por setor (índice de Grubel-Lloyd), sem olhar quem são as empresas.",
            azb("Comércio intrafirma") + ": critério " + azb("societário") + " — transações entre unidades da "
            "mesma " + azb("empresa transnacional") + " em países diferentes (matriz ↔ filial, filial ↔ "
            "filial). Estima-se que responda por fatia relevante do comércio mundial; envolve " + azb("preços "
            "de transferência") + " e tem implicações tributárias.",
            "Os conceitos se cruzam, mas não coincidem: o comércio intrafirma pode ser interindustrial "
            "(filial mineradora vende minério à matriz siderúrgica) ou intraindustrial (montadora troca peças "
            "entre fábricas). E o comércio intraindustrial pode ocorrer entre empresas independentes (Renault "
            "× Volkswagen).",
            "No exemplo do item há só um fluxo (importação da França), sem a simultaneidade de exportações e "
            "importações setoriais que a definição exige.",
            vm("Regra-âncora: intrassetorial = mesmo setor; intrafirma = mesma empresa."),
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " A 1ª parte é a definição exata; o erro foi "
                       "enxertado no exemplo, que ilustra outro conceito. 🔥 Em itens com “por exemplo”, teste "
                       "sempre se o exemplo cabe na definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…por exemplo, quando a França exporta automóveis para a Alemanha e importa automóveis "
            "alemães.”</i> → CERTO",
            "<i>“O comércio intrafirma é sempre intraindustrial.”</i> → ERRADO (modulador absoluto: pode ser "
            "interindustrial)",
        ])],
        "reescrita": ("O comércio intrassetorial é definido como o intercâmbio entre dois países com exportações e "
                      "importações simultâneas de produtos pertencentes a uma mesma indústria, por exemplo, quando "
                      + hl("a França exporta automóveis para a Argentina e importa automóveis argentinos") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["por exemplo"], "dificuldade": 2,
        "comentario_fonte": ("A definição está correta, mas o exemplo descreve comércio intrafirma (matriz-"
                             "filial); a definição exige simultaneidade bilateral por indústria."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00219-1 (comércio intrafirma)"],
    },
    # ------------------------------------------------------------------ E2-L00216
    {
        "id": "ECO-E2-L00216-1", "fonte_ref": "E2-L00216", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("Na diferenciação vertical de produtos, a principal característica considerada é a "
                      "qualidade, em que dois produtos oferecem a mesma funcionalidade, mas apresentam diferenças "
                      "de qualidade significativas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na diferenciação <u>vertical</u> de produtos, a principal característica considerada é a "
                      "<u>qualidade</u>, em que dois produtos oferecem a <u>mesma funcionalidade</u>, mas "
                      "apresentam diferenças de qualidade significativas."),
        "poucas": (azb("Diferenciação vertical") + " = mesma função, " + vd("qualidade") + " diferente: a "
                   "preço igual, todos prefeririam a mesma versão. É a definição de manual."),
        "destrinchando": [
            "Teste prático para distinguir: <b>se os dois produtos custassem o mesmo, todos escolheriam o "
            "mesmo?</b> Sim → " + azb("vertical") + " (há ordem de qualidade: processador mais rápido, carro "
            "mais seguro). Não, cada um escolheria por gosto → " + azb("horizontal") + " (cor, design, sabor, "
            "marca).",
            "No comércio: a diferenciação vertical se associa a diferenças de " + azb("renda") + " e de "
            + azb("tecnologia") + " entre países — os mais ricos e intensivos em capital exportam as versões "
            "de alta qualidade e importam as básicas. Por isso o comércio intraindustrial vertical também "
            "ocorre entre países de renda diferente, e parte da literatura o liga a Heckscher-Ohlin "
            "(qualidade intensiva em capital).",
            "A horizontal sustenta o modelo de " + oc("Krugman") + " (gosto pela variedade): países "
            "semelhantes trocam variedades equivalentes.",
            "Na prática, a maioria dos produtos combina as duas dimensões, e a separação é analítica.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição pura. O risco é a troca de rótulos (vertical ↔ "
                       "horizontal), mais frequente quando a banca cobra as duas no mesmo bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na diferenciação vertical, os produtos se distinguem por atributos como cor e design, "
            "escolhidos segundo as preferências pessoais.”</i> → ERRADO (troca de conceito: isso é a "
            "horizontal)",
            "<i>“O comércio intraindustrial com diferenciação vertical pode ocorrer entre países de níveis de "
            "renda distintos.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Diferenciação vertical ligada à qualidade (tecnologia, segurança), distinta da "
                             "horizontal (cor, design); exemplo da indústria automotiva."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00205-1 (mesma definição, outra questão da mesma prova)"],
    },
    # ------------------------------------------------------------------ E2-L00217
    {
        "id": "ECO-E2-L00217-1", "fonte_ref": "E2-L00217", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("O comércio intrasetorial envolve a troca de produtos entre países dentro do mesmo setor onde "
                      "tanto exportação quanto importação ocorrem simultaneamente. Adicionalmente, a diferenciação "
                      "horizontal não interfere nas transações, pois estas são baseadas em diferenciação "
                      "qualitativa, sem levar em consideração as preferências dos consumidores que podem afetar o "
                      "comércio internacional bilateralmente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O comércio intrasetorial envolve a troca de produtos entre países dentro do mesmo setor "
                       "onde tanto exportação quanto importação ocorrem simultaneamente. Adicionalmente, a "
                       "diferenciação horizontal ") + vm("não interfere nas transações, pois estas são baseadas "
                    "em diferenciação qualitativa, sem levar em consideração") + az(" as preferências dos "
                    "consumidores que podem afetar o comércio internacional bilateralmente.")),
        "poucas": ("A 1ª frase está certa. A 2ª, não: a " + azb("diferenciação horizontal") + " é justamente "
                   "a baseada nas " + vm("preferências") + " dos consumidores, e é uma das bases do comércio "
                   "intrassetorial."),
        "destrinchando": [
            "Definição (correta no item): " + azb("comércio intrassetorial") + " = exportações e importações "
            "simultâneas de bens do mesmo setor.",
            "O erro: o item atribui à diferenciação horizontal a natureza “qualitativa” (que é da "
            + azb("vertical") + ") e nega o papel das preferências. Na verdade, a horizontal = variedades de "
            "qualidade semelhante que se distinguem por atributos (design, cor, marca, sabor), escolhidas por "
            + azb("gosto") + ".",
            "Por que ela gera comércio: consumidores valorizam a " + azb("variedade") + " (" + oc("Dixit-"
            "Stiglitz") + ", 1977); com economias de escala, cada país produz poucas variedades em grande "
            "escala e importa as demais. É o núcleo do modelo de " + oc("Krugman") + " (1979–1980), que "
            "explica o comércio intraindustrial entre países semelhantes.",
            "As duas diferenciações coexistem: a vertical explica trocas de qualidades distintas; a horizontal, "
            "trocas de variedades equivalentes.",
            vm("Regra-âncora: vertical = qualidade; horizontal = preferências e atributos."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A 1ª frase é definição de manual; a 2ª "
                       "inverte o conceito de diferenciação horizontal e nega o papel das preferências. O "
                       "“Adicionalmente” é o ponto de enxerto típico de meia-verdade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A diferenciação horizontal, baseada nas preferências dos consumidores por atributos distintos, "
            "é uma das explicações do comércio intrassetorial.”</i> → CERTO",
            "<i>“O comércio intrassetorial ocorre apenas quando há diferenciação vertical.”</i> → ERRADO "
            "(restrição indevida)",
        ])],
        "reescrita": ("O comércio intrasetorial envolve a troca de produtos entre países dentro do mesmo setor onde "
                      "tanto exportação quanto importação ocorrem simultaneamente. Adicionalmente, a diferenciação "
                      "horizontal " + hl("interfere nas transações, pois se baseia em atributos distintos de "
                      "produtos de qualidade semelhante, levando em consideração") + " as preferências dos "
                      "consumidores que podem afetar o comércio internacional bilateralmente."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O comércio intrassetorial não ignora a diferenciação horizontal, que trata de "
                             "diferenças estéticas e culturais capazes de alterar preferências e o comércio "
                             "bilateral."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00218
    {
        "id": "ECO-E2-L00218-1", "fonte_ref": "E2-L00218", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("Economias de escala internas à firma ocorrem quando uma empresa reduz seus custos de "
                      "produção à medida que aumenta sua produção total. Já as economias externas à firma são "
                      "aquelas em que é o crescimento da indústria como um todo que possibilita a redução de custos "
                      "de todas as empresas individuais desse setor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Economias de escala <u>internas</u> à firma ocorrem quando uma empresa reduz seus custos de "
                      "produção à medida que aumenta <u>sua</u> produção total. Já as economias <u>externas</u> à "
                      "firma são aquelas em que é o crescimento da <u>indústria como um todo</u> que possibilita a "
                      "redução de custos de todas as empresas individuais desse setor."),
        "poucas": ("Interna: o custo médio cai com o tamanho da " + azb("firma") + ". Externa: cai com o "
                   "tamanho da " + azb("indústria") + " (local), mesmo que cada firma seja pequena."),
        "destrinchando": [
            azb("Economias internas") + ": custos fixos altos diluídos, especialização de tarefas, compras em "
            "grande escala. Favorecem firmas grandes e mercados de " + azb("concorrência imperfeita") + " "
            "(monopólio, oligopólio, concorrência monopolística). No comércio: modelo de " + oc("Krugman")
            + " (variedades diferenciadas).",
            azb("Economias externas") + " (" + oc("Alfred Marshall") + ", <i>Princípios</i>, 1890): três "
            "fontes clássicas — " + vd("fornecedores especializados") + ", " + vd("mercado de trabalho "
            "comum") + " e " + vd("transbordamento de conhecimento") + ". Compatíveis com muitas firmas "
            "pequenas e concorrência perfeita. Explicam " + azb("clusters") + ": Vale do Silício, relógios "
            "suíços, calçados em Franca (SP) e no Vale dos Sinos (RS).",
            "Consequências para o comércio com economias externas: o padrão de especialização pode ser "
            "“travado” pela história (quem começou primeiro), mesmo que outro país pudesse produzir mais "
            "barato se tivesse a mesma escala; e os ganhos de comércio não são garantidos para todos.",
            "Na curva de custo: internas → custo médio de longo prazo decrescente da firma; externas → a curva "
            "de custo de cada firma desce quando a indústria cresce (curva de oferta da indústria decrescente "
            "no longo prazo).",
        ],
        "dissecando": (cz("[literalidade]") + " Definições de manual (" + oc("Krugman e Obstfeld") + "). A "
                       "versão ERRADA usual troca os sujeitos: “internas = crescimento da indústria”, "
                       "“externas = crescimento da firma”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Economias externas à firma exigem que o setor seja dominado por poucas empresas "
            "grandes.”</i> → ERRADO (troca de conceito: compatíveis com muitas firmas pequenas)",
            "<i>“Economias de escala internas tendem a gerar mercados de concorrência imperfeita.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Internas: custos médios menores pelo aumento da produção da própria empresa. "
                             "Externas: beneficiam todas as empresas quando a indústria cresce (clusters)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00219
    {
        "id": "ECO-E2-L00219-1", "fonte_ref": "E2-L00219", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de comércio intrafirma refere-se ao comércio de bens e insumos entre subsidiárias "
                      "da mesma corporação, localizadas em diferentes países. No entanto, a transferência de bens "
                      "entre subsidiárias da mesma empresa tende, invariavelmente, a ser limitada quando há "
                      "significativas diferenças tecnológicas entre elas, gerando desafios para manter a "
                      "competitividade no mercado internacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O conceito de comércio intrafirma refere-se ao comércio de bens e insumos entre "
                       "subsidiárias da mesma corporação, localizadas em diferentes países. No entanto, a "
                       "transferência de bens entre subsidiárias da mesma empresa ") + vm("tende, invariavelmente, "
                    "a ser limitada") + az(" quando há significativas diferenças tecnológicas entre elas, gerando "
                                           "desafios para manter a competitividade no mercado internacional.")),
        "poucas": ("A definição está certa; o erro é o " + vm("“invariavelmente”") + ". Diferenças tecnológicas "
                   "entre unidades costumam " + azb("motivar") + " o comércio intrafirma (cada filial faz a "
                   "etapa que lhe cabe), em vez de limitá-lo."),
        "destrinchando": [
            azb("Comércio intrafirma") + ": transações entre matriz e filiais (ou entre filiais) da mesma "
            + azb("empresa transnacional") + " em países diferentes. É a face comercial do " + azb("investimento "
            "estrangeiro direto") + " e das " + azb("cadeias globais de valor") + ": cada unidade se "
            "especializa numa etapa (P&amp;D na matriz, montagem onde a mão de obra é barata, componentes onde "
            "há escala).",
            "Por isso, diferenças tecnológicas e de custos entre as unidades são, com frequência, a " + vd("razão")
            + " da divisão do trabalho dentro da empresa — a matriz envia componentes de alta tecnologia e "
            "recebe produtos montados. Quando a diferença atrapalha, a empresa transfere " + azb("know-how")
            + ", padroniza processos ou investe na filial.",
            "Por que internalizar em vez de comprar no mercado: " + azb("teoria da internalização") + " e "
            "paradigma eclético OLI de " + oc("John Dunning") + " (propriedade, localização, internalização) — "
            "proteger tecnologia, reduzir custos de transação, controlar qualidade.",
            "Tema sensível: os " + azb("preços de transferência") + " (preços internos entre unidades) podem "
            "deslocar lucros para jurisdições de imposto baixo; daí regras da OCDE e da Receita Federal.",
            vm("Regra-âncora: em itens de definição, desconfie do modulador absoluto enxertado na 2ª frase."),
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " 1ª frase: definição correta. 2ª frase: "
                       "“tende, invariavelmente” — combinação contraditória (tendência não é invariável) que "
                       "denuncia o enxerto. E a ideia de fundo também é falsa: diferença tecnológica é motor, "
                       "não freio, do comércio intrafirma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O comércio intrafirma está associado à atuação de empresas transnacionais e à fragmentação "
            "internacional da produção.”</i> → CERTO",
            "<i>“O comércio intrafirma, por definição, só envolve bens da mesma indústria.”</i> → ERRADO "
            "(restrição indevida: pode ser interindustrial)",
        ])],
        "reescrita": ("O conceito de comércio intrafirma refere-se ao comércio de bens e insumos entre subsidiárias "
                      "da mesma corporação, localizadas em diferentes países. No entanto, a transferência de bens "
                      "entre subsidiárias da mesma empresa " + hl("pode ser dificultada, em alguns casos,")
                      + " quando há significativas diferenças tecnológicas entre elas, gerando desafios para "
                      "manter a competitividade no mercado internacional."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["invariavelmente"], "dificuldade": 1,
        "comentario_fonte": ("O comércio intrafirma preserva tecnologia e otimiza lucros entre subsidiárias; não é "
                             "invariavelmente limitado por diferenças tecnológicas, que se contornam com "
                             "transferência de know-how e padronização."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00206-1 (intrassetorial × intrafirma)"],
    },
    # ------------------------------------------------------------------ E2-L00297
    {
        "id": "ECO-E2-L00297-1", "fonte_ref": "E2-L00297", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("A Teoria do Ciclo de Vida do Produto (Vernon) explica o comércio intraindustrial entre "
                      "países desenvolvidos, argumentando que a diferenciação de produtos e as economias de escala "
                      "são mais relevantes que as vantagens comparativas tradicionais para explicar esse fluxo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A ") + vm("Teoria do Ciclo de Vida do Produto (Vernon)") + az(" explica o comércio "
                    "intraindustrial entre países desenvolvidos, argumentando que a diferenciação de produtos e as "
                    "economias de escala são mais relevantes que as vantagens comparativas tradicionais para "
                    "explicar esse fluxo.")),
        "poucas": ("Fenômeno e mecanismo certos, " + vm("teoria errada") + ": quem explica o comércio "
                   "intraindustrial por escala e diferenciação é a " + azb("Nova Teoria do Comércio") + " ("
                   + oc("Krugman") + ", " + oc("Helpman") + "). " + oc("Vernon") + " explica a "
                   + azb("migração") + " da produção ao longo da vida do produto."),
        "destrinchando": [
            oc("Raymond Vernon") + " (" + vd("1966") + ") — " + azb("ciclo de vida do produto") + ": "
            "(1) " + vd("produto novo") + ": inventado e produzido no país inovador (os EUA no pós-guerra), "
            "perto do mercado de alta renda e da P&amp;D; exportado para o mundo; (2) " + vd("maturidade") + ": "
            "a tecnologia se difunde, outros países desenvolvidos passam a produzir; o inovador começa a "
            "importar e investe no exterior (IED); (3) " + vd("padronização") + ": o produto vira commodity, "
            "o custo da mão de obra decide, e a produção migra para países em desenvolvimento; o inovador "
            "vira importador líquido.",
            "O que Vernon explica: a " + azb("dinâmica") + " do comércio interindustrial e do IED no tempo — "
            "uma versão dinâmica de H-O, em que a vantagem passa do capital tecnológico ao trabalho barato. "
            "Também ajuda a explicar o " + azb("paradoxo de Leontief") + " (os EUA exportando bens intensivos "
            "em trabalho qualificado).",
            "O que a " + azb("Nova Teoria do Comércio") + " explica: o comércio " + azb("intraindustrial")
            + " entre países semelhantes, por " + azb("economias de escala internas") + ", "
            + azb("diferenciação de produtos") + " e " + azb("concorrência monopolística") + " (modelo "
            + oc("Dixit-Stiglitz") + "-Krugman). Krugman: Nobel de " + vd("2008") + ". Complemento pela "
            "demanda: " + oc("Linder") + " (1961).",
            "Outras peças do mapa: " + oc("Melitz") + " (2003, firmas heterogêneas: só as mais produtivas "
            "exportam); Nova Geografia Econômica (" + oc("Krugman") + ", 1991: aglomeração × custos de "
            "transporte); " + oc("Porter") + " (vantagem competitiva, “diamante”).",
            vm("Regra-âncora: Vernon = migração no tempo (inovador → imitador); Krugman = intraindustrial entre "
               "iguais."),
        ],
        "dissecando": (cz("[troca de ator]") + " Erro de atribuição: o item descreve corretamente a Nova Teoria "
                       "do Comércio e põe o nome de Vernon. Como o ciclo do produto também é “nova teoria” "
                       "(anos 1960, pós-Leontief), a confusão é natural. 🔥 A banca adora trocar os rótulos "
                       "entre Vernon, Linder, Krugman e Melitz."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Vernon, à medida que o produto se padroniza, sua produção tende a migrar para países "
            "de menor custo de mão de obra.”</i> → CERTO",
            "<i>“A Nova Teoria do Comércio explica o comércio intraindustrial com base nas diferenças de "
            "dotações de fatores entre os países.”</i> → ERRADO (troca de conceito: escala e diferenciação)",
        ])],
        "reescrita": ("A " + hl("Nova Teoria do Comércio (Krugman)") + " explica o comércio intraindustrial entre "
                      "países desenvolvidos, argumentando que a diferenciação de produtos e as economias de escala "
                      "são mais relevantes que as vantagens comparativas tradicionais para explicar esse fluxo."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Erro de atribuição: o comércio intraindustrial por escala e diferenciação é "
                             "explicado pela Nova Teoria do Comércio (Krugman/Helpman); Vernon explica a migração "
                             "da produção do inovador para os imitadores. Panorama de Ricardo, H-O, Vernon, "
                             "Krugman, Linder, Melitz, Nova Geografia Econômica e Porter, com duas tabelas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 031", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 032", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00499
    {
        "id": "ECO-E2-L00499-1", "fonte_ref": "E2-L00499", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_COM,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a nova teoria do comércio internacional, a existência de economias de escala e "
                      "de marcas globais são uma explicação mais convincente para o comércio internacional, "
                      "descartando as teorias tradicionais baseadas em vantagens comparativas ou diferenças na "
                      "abundância de fatores de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a nova teoria do comércio internacional, a existência de economias de escala "
                       "e de marcas globais são uma explicação mais convincente para o comércio internacional, ")
                    + vm("descartando") + az(" as teorias tradicionais baseadas em vantagens comparativas ou "
                                             "diferenças na abundância de fatores de produção.")),
        "poucas": ("A nova teoria " + azb("complementa") + ", não " + vm("descarta") + ", as tradicionais: "
                   "Ricardo e H-O seguem explicando o comércio " + azb("interindustrial") + "; escala e "
                   "diferenciação explicam o " + azb("intraindustrial") + "."),
        "destrinchando": [
            "Divisão de trabalho entre as teorias: " + oc("Ricardo") + " (produtividade) e "
            + oc("Heckscher-Ohlin") + " (dotações) → comércio entre países " + azb("diferentes") + ", de bens "
            "diferentes (Norte-Sul, primários × manufaturas). " + oc("Krugman") + " e " + oc("Helpman")
            + " (escala, diferenciação, concorrência monopolística) → comércio entre países "
            + azb("semelhantes") + ", de bens do mesmo setor.",
            "O próprio " + oc("Helpman e Krugman") + " (<i>Market Structure and Foreign Trade</i>, 1985) "
            "integraram os dois mundos: num modelo com dotações diferentes e escala, o comércio "
            "interindustrial reflete as vantagens comparativas e o intraindustrial reflete a escala. Quanto "
            "mais parecidas as dotações, maior a fatia intraindustrial (o que se mede com o índice de "
            "Grubel-Lloyd).",
            "Sobre “mais convincente”: só para os fluxos entre economias parecidas. Para o comércio do "
            + rx("Brasil") + " com a China (soja e minério por manufaturas), a explicação continua sendo de "
            "vantagens comparativas e dotações.",
            vm("Regra-âncora: nova teoria + teorias tradicionais = complementares."),
        ],
        "dissecando": (cz("[extrapolação · modulador absoluto]") + " O item parte de algo verdadeiro (a nova "
                       "teoria explica bem parte do comércio) e extrapola para o descarte das clássicas. "
                       "“Descartando” é a palavra-gatilho: teorias econômicas novas raramente “descartam”; em "
                       "prova, “complementam”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A nova teoria do comércio complementa as teorias tradicionais, explicando sobretudo o comércio "
            "intraindustrial.”</i> → CERTO",
            "<i>“Segundo a nova teoria, países com dotações de fatores idênticas não têm motivos para "
            "comerciar.”</i> → ERRADO (contradição: a escala gera comércio mesmo entre iguais)",
        ])],
        "reescrita": ("De acordo com a nova teoria do comércio internacional, a existência de economias de escala e "
                      "de marcas globais são uma explicação mais convincente para o comércio internacional, "
                      + hl("complementando") + " as teorias tradicionais baseadas em vantagens comparativas ou "
                      "diferenças na abundância de fatores de produção."),
        "tipo_erro": ["EXTRAPOLACAO", "GENERALIZACAO"], "moduladores": ["descartando"], "dificuldade": 1,
        "comentario_fonte": ("A nova teoria complementa as tradicionais: Ricardo e H-O explicam o comércio "
                             "interindustrial; a nova teoria, o intraindustrial, por escala e diferenciação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00500
    {
        "id": "ECO-E2-L00500-1", "fonte_ref": "E2-L00500", "destino": "75", "subtema": H2["novas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_COM,
        "rotulo_item": "Item",
        "assertiva": ("As economias de escala fornecem um incentivo ao comércio internacional porque cada país "
                      "especializa-se em produzir produtos diversificados, usando a mesma escala das plantas, "
                      "fazendo uso das mesmas operações e/ou insumos de forma mais eficiente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As economias de escala fornecem um incentivo ao comércio internacional porque cada país "
                       "especializa-se em produzir ") + vm("produtos diversificados, usando a mesma escala das "
                    "plantas") + az(", fazendo uso das mesmas operações e/ou insumos de forma mais eficiente.")),
        "poucas": ("Com escala, compensa " + azb("concentrar") + ": cada país produz uma " + vm("gama limitada")
                   + " de bens em plantas " + vd("maiores") + " e obtém a variedade pelo comércio. "
                   "“Diversificar com a mesma escala” anula o ganho."),
        "destrinchando": [
            "Lógica de " + oc("Krugman") + ": com custo fixo por variedade, o custo médio cai com o volume. Um "
            "país isolado, para ter variedade, precisa produzir muitas variedades em pequena escala, com custo "
            "médio alto. Com o comércio, cada país " + azb("especializa-se em poucas variedades") + ", produz "
            "em grande escala e importa as outras.",
            "Resultado: o mercado integrado sustenta " + vd("mais variedades") + " a " + vd("custo médio "
            "menor") + " do que cada mercado nacional sozinho — ganho de comércio que não depende de diferença "
            "de tecnologia ou de dotação.",
            "O item inverte a direção: “produtos diversificados” é o que o consumidor ganha com o comércio "
            "(variedade no consumo), não o que cada país produz. E “mesma escala das plantas” contradiz a "
            "própria ideia de economias de escala (plantas maiores, custo menor).",
            "Exemplo: o " + azb("Acordo Automotivo EUA-Canadá") + " (" + vd("1965") + ") — antes, fábricas "
            "canadenses produziam muitos modelos em escala pequena; com o livre-comércio setorial, "
            "especializaram-se em poucos modelos para todo o mercado norte-americano, e a produtividade "
            "subiu.",
            vm("Regra-âncora: escala → especializar a produção; comércio → diversificar o consumo."),
        ],
        "dissecando": (cz("[inversão · contradição]") + " Troca “especializar-se em poucos produtos” por "
                       "“produzir produtos diversificados” e acrescenta “mesma escala”, que nega a premissa. O "
                       "item soa plausível porque “diversificação” e “eficiência” aparecem juntas nos manuais "
                       "— mas a diversificação é do consumo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com economias de escala, o comércio permite a cada país produzir uma gama limitada de bens em "
            "maior escala, enquanto o consumidor tem acesso a maior variedade.”</i> → CERTO",
            "<i>“As economias de escala só geram ganhos de comércio entre países com dotações de fatores "
            "diferentes.”</i> → ERRADO (restrição indevida: geram também entre países idênticos)",
        ])],
        "reescrita": ("As economias de escala fornecem um incentivo ao comércio internacional porque cada país "
                      "especializa-se em produzir " + hl("uma gama limitada de produtos, em plantas de maior "
                      "escala") + ", fazendo uso das mesmas operações e/ou insumos de forma mais eficiente."),
        "tipo_erro": ["INVERSAO", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O incentivo vem da especialização numa gama limitada de bens, com maior escala e "
                             "menores custos médios; a variedade se obtém pelo comércio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
