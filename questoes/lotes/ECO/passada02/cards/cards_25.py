"""Cards do lote de redação 25 — ECO, passada 02 (notas 48, 49, 50 e 55: déficit e dívida, orçamento,
regras fiscais, teorias do consumo e do investimento)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "conc": "📏 Conceitos de déficit e dívida",
    "fin": "🧮 Financiamento e sustentabilidade",
    "ciclo": "📒 Ciclo orçamentário",
    "lrf": "⚖️ Responsabilidade fiscal",
    "traj": "📈 Trajetória da dívida",
    "regras": "🧱 Regras fiscais: teto e arcabouço",
    "cons": "🛒 Teorias do consumo",
    "inv": "🏗️ Teorias do investimento",
}

CMD_RT_DIV = "A respeito da política fiscal e da dívida pública, julgue o item a seguir."
CMD_TJPA_76 = "Julgue os próximos itens, acerca dos conceitos de déficit e dívida pública."
CMD_TJPA_83 = "Acerca da contabilidade do setor público e de suas métricas, julgue os itens subsequentes."
CMD_TJPA_88 = ("Julgue os itens que se seguem, a respeito das políticas fiscal e monetária, do papel da dívida "
               "pública como fonte de financiamento e da função reguladora do Estado na economia.")
CMD_TJPA_96 = ("No que concerne à estrutura do orçamento público no Brasil e ao tratamento da dívida pública, "
               "julgue os itens subsecutivos.")
CMD_NIDI_JUL = ("Sobre os conceitos pertencentes ao ramo da Economia que se dedica ao estudo do Setor Público e seu "
                "orçamento e sobre o princípio da Equivalência Ricardiana, julgue certo ou errado os itens a "
                "seguir.")
CMD_NIDI_ABR_IND = "Acerca dos indicadores orçamentários e da equivalência ricardiana, julgue o item a seguir."
CMD_NIDI_ABR_90 = ("Acerca da economia do setor público e das políticas fiscais no Brasil (1990-2000), julgue o item "
                   "a seguir.")
CMD_BOZAN = ("Julgue as assertivas a seguir sobre a estrutura de planejamento orçamentário no Brasil, considerando "
             "os tipos e a evolução dos orçamentos.")
CMD_NAB_POL = "Em relação às políticas monetárias e fiscais, julgue (C ou E) os itens que se seguem."
CMD_NAB_MODELOS = "Em relação aos modelos macroeconômicos, julgue (C ou E) os seguintes itens."
CMD_RT_FHC = ("A respeito do tema da política fiscal e dívida pública nos diferentes momentos da economia "
              "brasileira, julgue o item a seguir.")
CMD_ARM_INV = "Julgue o item a seguir, relativo às relações entre poupança, investimento e crédito."
CMD_NAB_CRESC = ("Em relação às teorias do crescimento econômico e às teorias do consumo, julgue (C ou E) os seguintes "
                 "itens.")
CMD_NAB_INTERT = ("A respeito dos modelos de crescimento e da economia intertemporal, julgue (C ou E) os seguintes "
                  "itens.")
CMD_NAB_CONS_INV = ("Em relação às teorias de consumo, investimento e dívida pública, julgue (C ou E) os itens a "
                    "seguir.")
CMD_NAB_CONS_2023 = "No que se refere às teorias do consumo e do investimento, julgue (C ou E) os itens subsequentes."

CARDS = [
    # ------------------------------------------------------------------ E2-L01776
    {
        "id": "ECO-E2-L01776-1", "fonte_ref": "E2-L01776", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_DIV,
        "rotulo_item": "Item",
        "assertiva": ("As operações compromissadas do Banco Central entram no estoque da Dívida Bruta do Governo "
                      "Geral (DBGG), de maneira que o crescimento destas operações em período recente, associadas à "
                      "necessidade de esterilização da aquisição de reservas internacionais, tem elevado a dívida "
                      "pública."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As <u>operações compromissadas do Banco Central entram no estoque da Dívida Bruta do Governo "
                      "Geral (DBGG)</u>, de maneira que o crescimento destas operações em período recente, "
                      "associadas à necessidade de <u>esterilização da aquisição de reservas internacionais</u>, tem "
                      "elevado a dívida pública."),
        "poucas": ("Pela metodologia do " + rx("Banco Central do Brasil") + ", a " + azb("DBGG") + " inclui as "
                   + azb("operações compromissadas") + "; ao esterilizar a compra de reservas, o BC as ampliou e, "
                   "com elas, a dívida bruta."),
        "destrinchando": [
            "Mecânica da " + azb("esterilização") + ": o BC compra dólares e paga em reais, o que expande a base "
            "monetária. Para não derrubar a Selic abaixo da meta, ele recolhe o excesso de liquidez vendendo "
            "títulos do Tesouro de sua carteira com compromisso de recompra — as " + azb("compromissadas") + ".",
            "A " + azb("DBGG") + " (governo federal, INSS, estados e municípios) soma a dívida mobiliária do Tesouro "
            "em mercado e as compromissadas do BC: estas funcionam, na prática, como dívida de curtíssimo prazo "
            "do setor público. Por isso o acúmulo de reservas dos anos 2000 e 2010 inflou a dívida bruta.",
            "Contraste decisivo: na " + azb("dívida líquida (DLSP)") + " a operação quase se anula — entra um "
            "ativo (reservas) e um passivo (compromissadas) de mesmo valor. O que pesa na DLSP ao longo do tempo é "
            "o " + azb("custo de carregamento") + ": paga-se Selic nas compromissadas e recebe-se juro baixo nas "
            "reservas.",
            "O " + oc("FMI") + " usa conceito ainda mais amplo de dívida bruta, que inclui toda a carteira de "
            "títulos do Tesouro em poder do BC; por isso a dívida bruta brasileira medida pelo FMI é maior que a "
            "divulgada pelo BCB.",
            vm("Regra-âncora: reservas financiadas por compromissadas elevam a dívida bruta, não a líquida."),
        ],
        "dissecando": (cz("[detalhe]") + " Item CERTO por um pormenor metodológico: quem só conhece a DBGG como "
                       "“dívida do governo” tende a achar que operação do BC fica de fora. A frase traz também o "
                       "nexo causal correto (esterilização → compromissadas → DBGG)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tem elevado, na mesma proporção, a dívida líquida do setor público.”</i> → ERRADO (troca de "
            "conceito: na DLSP, o ativo em reservas compensa o passivo)",
            "<i>“A DBGG, na metodologia do BCB, exclui as operações compromissadas, que são instrumento de "
            "política monetária.”</i> → ERRADO (contradição: elas entram)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("As compromissadas entram na DBGG; a esterilização da compra de reservas aumentou o "
                             "estoque dessas operações e, portanto, a dívida bruta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00032
    {
        "id": "ECO-E3-L00032-1", "fonte_ref": "E3-L00032", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_76,
        "rotulo_item": "Item",
        "assertiva": ("A dívida pública bruta representa o total de obrigações financeiras assumidas pelo setor "
                      "público, independentemente da existência de ativos financeiros correspondentes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A dívida pública bruta representa o total de obrigações financeiras assumidas pelo setor "
                      "público, <u>independentemente da existência de ativos financeiros correspondentes</u>."),
        "poucas": ("Dívida " + azb("bruta") + " = só o passivo, sem abater ativos; a " + azb("líquida")
                   + " desconta reservas, créditos e disponibilidades do setor público."),
        "destrinchando": [
            azb("Dívida bruta") + " responde a “quanto o setor público deve?”. No " + rx("Brasil") + ", o "
            "conceito-padrão é a " + azb("DBGG") + ": dívidas do governo federal, INSS, estados e municípios com o "
            "setor privado, o setor público financeiro e o resto do mundo, inclusive as compromissadas do BC.",
            azb("Dívida líquida (DLSP)") + " responde a “quanto deve, descontado o que tem a receber?”: passivos "
            "menos ativos financeiros — reservas internacionais, créditos junto ao BNDES e a fundos, depósitos. "
            "Abrange também o Banco Central e as estatais não financeiras (exceto Petrobras e Eletrobras).",
            "Por que a diferença importa: o Brasil acumulou ativos volumosos (reservas, créditos ao BNDES), de "
            "modo que a bruta fica bem acima da líquida — em 2024, cerca de " + vd("76% × 61% do PIB")
            + " ⏳ (out/2026). A bruta é a mais usada em comparações internacionais e pelas agências de risco; a "
            "líquida capta a solvência patrimonial.",
            "Ressalva: ativos não são todos igualmente líquidos nem rendem o que a dívida custa; por isso olhar só "
            "a líquida pode subestimar o risco de rolagem.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Reproduz a definição de manual. O "
                       "“independentemente” soa como modulador absoluto e induz o ERRADO, mas aqui é justamente o "
                       "traço que define o conceito “bruto”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A dívida pública líquida representa o total de obrigações financeiras do setor público, "
            "independentemente da existência de ativos financeiros correspondentes.”</i> → ERRADO (troca de "
            "conceito: isso é a bruta)",
            "<i>“A DLSP desconta da dívida bruta os ativos financeiros do setor público, como as reservas "
            "internacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["independentemente"], "dificuldade": 1,
        "comentario_fonte": ("Dívida bruta = total de passivos sem deduzir ativos; dívida líquida = bruta menos "
                             "ativos financeiros (reservas, créditos do BNDES)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00033
    {
        "id": "ECO-E3-L00033-1", "fonte_ref": "E3-L00033", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA_76,
        "rotulo_item": "Item",
        "assertiva": ("O financiamento do déficit primário por meio da emissão de dívida pública ocasiona, "
                      "automaticamente, o aumento da dívida líquida do setor público."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("O financiamento do déficit primário por meio da emissão de dívida pública ocasiona, "
                       "automaticamente, o aumento da dívida ") + vm("líquida") + az(" do setor público.")),
        "poucas": ("Emitir título eleva " + azb("automaticamente") + " a dívida " + azb("bruta") + "; a "
                   + azb("líquida") + " desconta os ativos e ainda depende de juros e ajustes patrimoniais — por "
                   "isso o “automaticamente” derruba o item."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "mantido o ERRADO da fonte. Pela identidade do BCB, ΔDLSP = NFSP + ajustes (cambial, "
                          "patrimoniais); como o déficit primário entra nas NFSP, gastá-lo com recursos de dívida "
                          "tende, sim, a elevar a dívida líquida. O ERRADO se sustenta só pela leitura estrita do "
                          "“automaticamente”: no ato da emissão, caixa e passivo sobem juntos, e o efeito final "
                          "sobre a DLSP ainda pode ser compensado por ajustes (ex.: valorização das reservas numa "
                          "depreciação do real).")],
        "destrinchando": [
            "Emissão de dívida é operação " + azb("abaixo da linha") + ": no instante em que o Tesouro vende o "
            "título, entra caixa (ativo) e surge o título (passivo). A " + vd("dívida bruta sobe na hora")
            + "; a " + azb("líquida") + " (passivos − ativos) fica igual até o dinheiro ser gasto.",
            "É o " + azb("déficit") + ", e não a emissão, que move a DLSP: quando o governo paga despesas acima "
            "das receitas, o caixa sai e a dívida líquida cresce. A emissão é só a forma de financiar.",
            "Mesmo com déficit, a variação da DLSP soma outros fatores: " + azb("juros nominais") + ", "
            + azb("ajuste cambial") + " (o " + rx("Brasil") + " é credor líquido em dólar: depreciação do real "
            "<b>reduz</b> a DLSP), reconhecimento de dívidas, privatizações. Daí não haver relação mecânica.",
            "Outras formas de financiar o mesmo déficit — venda de ativos, uso de caixa acumulado (como a Conta "
            "Única), senhoriagem — mexem de modo diferente na bruta e na líquida.",
            vm("Regra-âncora: emitir título → bruta sobe já; líquida depende do uso dos recursos e dos ajustes."),
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " O item cola o efeito certo (emissão → "
                       "aumento de dívida) no conceito errado (líquida em vez de bruta) e reforça com "
                       "“automaticamente”. 🔥 CEBRASPE explora a dupla bruta × líquida em quase todo bloco de "
                       "dívida pública."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…ocasiona, automaticamente, o aumento da dívida bruta do setor público.”</i> → CERTO",
            "<i>“A acumulação de reservas internacionais financiada por emissão de títulos eleva a dívida "
            "líquida na mesma medida.”</i> → ERRADO (ativo e passivo sobem juntos)",
        ])],
        "reescrita": ("O financiamento do déficit primário por meio da emissão de dívida pública ocasiona, "
                      "automaticamente, o aumento da dívida " + hl("bruta") + " do setor público."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["automaticamente"], "dificuldade": 3,
        "comentario_fonte": ("A emissão eleva a dívida bruta; a líquida não sobe automaticamente, pois os recursos "
                             "captados ficam, de início, como ativo do Tesouro e a DLSP depende de outros ajustes."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: pela identidade ΔDLSP = NFSP + ajustes, déficit primário financiado por dívida "
                    "tende a elevar a dívida líquida; o ERRADO da fonte só se sustenta pela leitura estrita de "
                    "“automaticamente” (no ato da emissão a DLSP não muda e ajustes podem compensar)"],
    },
    # ------------------------------------------------------------------ E3-L00039
    {
        "id": "ECO-E3-L00039-1", "fonte_ref": "E3-L00039", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA_83,
        "rotulo_item": "Item",
        "assertiva": ("A necessidade de financiamento do setor público pode ser entendida como a variação da dívida "
                      "pública líquida."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A necessidade de financiamento do setor público <u>pode ser entendida</u> como a variação da "
                      "dívida pública líquida."),
        "poucas": ("O " + rx("BCB") + " mede as " + azb("NFSP") + " pelo critério " + azb("abaixo da linha")
                   + ": é a variação da dívida líquida no período, descontados os ajustes que não decorrem de "
                   "fluxo fiscal."),
        "destrinchando": [
            "Dois jeitos de medir o mesmo resultado fiscal. " + azb("Acima da linha") + ": receitas − despesas "
            "(é como o Tesouro apura o resultado do governo central). " + azb("Abaixo da linha")
            + ": quanto o setor público precisou se financiar, visto pela variação do endividamento líquido — "
            "o critério oficial das NFSP, apurado pelo BCB.",
            "Lógica: todo déficit tem de ser coberto por mais dívida ou menos ativos; logo, o déficit do período "
            "aparece como " + vd("ΔDLSP") + ". NFSP nominal positiva = déficit nominal.",
            "Refino que a banca pode cobrar: a variação da DLSP inclui também " + azb("ajustes patrimoniais")
            + " (privatizações, reconhecimento de dívidas) e o " + azb("ajuste cambial") + ", que não são "
            "resultado fiscal. Rigorosamente, NFSP = variação da " + azb("dívida fiscal líquida")
            + " (DLSP sem esses ajustes). O “pode ser entendida” abriga essa simplificação.",
            "As NFSP se desdobram em " + azb("primária") + " (sem juros), " + azb("nominal") + " (com juros "
            "nominais) e " + azb("operacional") + " (com juros reais).",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Quem conhece o refino da dívida fiscal "
                       "líquida é tentado a marcar ERRADO; o “pode ser entendida” torna a aproximação aceitável. "
                       "Em CEBRASPE, modulador relativo diante de definição correta em linhas gerais = CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A NFSP corresponde exatamente à variação da dívida líquida, inclusive dos efeitos de "
            "privatizações e da variação cambial.”</i> → ERRADO (esses ajustes patrimoniais ficam fora)",
            "<i>“Pelo critério acima da linha, a NFSP é apurada pela variação do endividamento.”</i> → ERRADO "
            "(inversão: isso é abaixo da linha)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode ser entendida"],
        "dificuldade": 2,
        "comentario_fonte": ("Pelo critério abaixo da linha, a NFSP equivale à variação da dívida líquida no "
                             "período; acima da linha, à diferença entre receitas e despesas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00040
    {
        "id": "ECO-E3-L00040-1", "fonte_ref": "E3-L00040", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_83,
        "rotulo_item": "Item",
        "assertiva": ("Se, em determinado ano, um país registrar déficit nominal, consequentemente, ele também "
                      "registrará déficit operacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se, em determinado ano, um país registrar déficit nominal, ") + vm("consequentemente,")
                    + az(" ele também registrará déficit operacional.")),
        "poucas": ("O " + azb("operacional") + " exclui a " + azb("correção monetária") + " dos juros; com "
                   "inflação, pode haver " + vd("déficit nominal e superávit operacional") + " ao mesmo tempo."),
        "destrinchando": [
            "As três medidas do resultado fiscal: " + azb("primário") + " = receitas − despesas não financeiras; "
            + azb("operacional") + " = primário − " + vd("juros reais") + "; " + azb("nominal") + " = primário − "
            + vd("juros nominais") + " (juros reais + correção monetária).",
            "Como juros nominais ≥ juros reais quando há inflação positiva, o resultado nominal é sempre o pior "
            "dos dois. Exemplo (% do PIB): superávit primário 3, juros reais 2, correção monetária 4 → operacional "
            "= " + vd("+1 (superávit)") + "; nominal = " + vd("−3 (déficit)") + ".",
            "A implicação válida corre no sentido contrário: com inflação positiva, " + vm("déficit operacional "
            "⇒ déficit nominal") + "; o inverso não vale.",
            "O conceito operacional nasceu na " + rx("alta inflação brasileira") + " dos anos 1980: a correção "
            "monetária inflava o déficit nominal sem representar esforço fiscal real, e os acordos com o FMI "
            "passaram a olhar o operacional. Com o Plano Real, perdeu relevância, e a meta fiscal brasileira "
            "passou a ser de resultado primário.",
        ],
        "dissecando": (cz("[nexo indevido · inversão]") + " O conector “consequentemente” cria uma implicação "
                       "que só existe no sentido oposto (operacional ⇒ nominal). Item de implicação entre medidas "
                       "fiscais se resolve perguntando qual delas inclui mais componentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se, em determinado ano, com inflação positiva, um país registrar déficit operacional, ele "
            "também registrará déficit nominal.”</i> → CERTO",
            "<i>“O resultado operacional difere do nominal por excluir os juros reais.”</i> → ERRADO (exclui a "
            "correção monetária; os juros reais ficam)",
        ])],
        "reescrita": ("Se, em determinado ano, um país registrar déficit nominal, " + hl("não necessariamente")
                      + " ele também registrará déficit operacional."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": ["consequentemente"], "dificuldade": 2,
        "comentario_fonte": ("O nominal inclui juros nominais (com correção monetária); o operacional, só juros "
                             "reais. Pode haver déficit nominal com superávit operacional, sobretudo com inflação "
                             "alta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00041
    {
        "id": "ECO-E3-L00041-1", "fonte_ref": "E3-L00041", "destino": "48", "subtema": H2["fin"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_83,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o Tesouro Nacional, incluem-se entre as diretrizes qualitativas da dívida "
                      "pública federal o aumento do prazo médio da dívida e a substituição de títulos prefixados por "
                      "títulos de taxas flutuantes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o Tesouro Nacional, incluem-se entre as diretrizes qualitativas da dívida "
                       "pública federal o aumento do prazo médio da dívida e a substituição de títulos ")
                    + vm("prefixados por títulos de taxas flutuantes") + az(".")),
        "poucas": ("O " + azb("PAF") + " do Tesouro manda o contrário: trocar títulos de " + azb("taxa flutuante")
                   + " (LFT, Selic) por " + azb("prefixados") + " e indexados a preços, e alongar o prazo."),
        "destrinchando": [
            "Diretrizes do " + azb("Plano Anual de Financiamento") + " (PAF): alongamento do prazo médio; "
            "suavização da estrutura de vencimentos; " + vm("substituição gradual dos títulos remunerados por "
            "taxas flutuantes por títulos prefixados ou vinculados a índices de preços") + "; substituição da "
            "dívida externa por instrumentos com prazo e custo adequados; ampliação da base de investidores.",
            "Os títulos: " + vd("LFT") + " (Selic, flutuante); " + vd("LTN e NTN-F") + " (prefixados); "
            + vd("NTN-B") + " (IPCA + juro real). Flutuantes deixam o custo da dívida colado à política "
            "monetária: cada alta da Selic encarece o estoque na hora e reduz a potência do canal monetário.",
            "Prefixados e indexados a preços dão previsibilidade ao Tesouro, mas custam mais (prêmio de risco) "
            "e o mercado só os compra em prazos longos quando confia na estabilidade. Por isso a composição é "
            "trade-off entre " + azb("custo e risco") + ".",
            "⏳ (out/2026) Nos anos 2020, a fatia de LFT voltou a crescer com a Selic alta e a demanda do mercado "
            "por pós-fixados — afastamento da diretriz que o próprio PAF registra.",
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " A 1ª diretriz (prazo médio) está certa e dá "
                       "credibilidade; o erro foi enxertado na 2ª, que inverte origem e destino da troca. Em item "
                       "com “substituição de X por Y”, confira sempre qual lado sai e qual entra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento do prazo médio e a redução da participação de títulos remunerados pela Selic.”</i> "
            "→ CERTO",
            "<i>“…a redução do prazo médio da dívida, para diminuir o custo de rolagem.”</i> → ERRADO (inversão: "
            "busca-se alongar)",
        ])],
        "reescrita": ("De acordo com o Tesouro Nacional, incluem-se entre as diretrizes qualitativas da dívida "
                      "pública federal o aumento do prazo médio da dívida e a substituição de títulos "
                      + hl("de taxas flutuantes por títulos prefixados ou vinculados a índices de preços") + "."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O PAF prevê alongar o prazo médio e substituir títulos flutuantes (LFT) por "
                             "prefixados e indexados ao IPCA; o item inverte a substituição."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00072
    {
        "id": "ECO-E3-L00072-1", "fonte_ref": "E3-L00072", "destino": "48", "subtema": H2["fin"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("Estoques elevados de dívida pública exigem déficits primários e nominais menores para que, "
                      "assim, seja possível manter a razão dívida/PIB constante, garantindo a sustentabilidade da "
                      "dívida pública."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Estoques elevados de dívida pública exigem ") + vm("déficits primários e nominais menores")
                    + az(" para que, assim, seja possível manter a razão dívida/PIB constante, garantindo a "
                         "sustentabilidade da dívida pública.")),
        "poucas": ("Com juros acima do crescimento, dívida alta exige " + azb("superávit primário maior")
                   + "; e o " + azb("déficit nominal") + " compatível com dívida/PIB estável é " + vd("maior")
                   + ", não menor, quanto maior a dívida."),
        "destrinchando": [
            "Dinâmica da dívida (d = dívida/PIB, s = superávit primário/PIB, r = juro real, g = crescimento "
            "real): " + vd("Δd ≈ (r − g)·d − s") + ". Para manter d constante: " + vm("s* = (r − g)·d") + ".",
            "Primário: se " + vd("r > g") + ", s* é positivo e cresce com d — dívida maior pede " + azb("superávit")
            + " maior, não apenas “déficit menor”. Ex.: r − g = 3 p.p. → d = 40% exige s = 1,2% do PIB; d = 80% "
            "exige 2,4%. Se " + vd("r < g") + ", o crescimento dilui a dívida e até um déficit primário pode ser "
            "compatível com d estável.",
            "Nominal: d constante significa que a dívida cresce à mesma taxa do PIB nominal (n). O déficit nominal "
            "que a mantém estável é " + vd("≈ n·d") + " — cresce com d. Com d = 80% e PIB nominal crescendo 8%, um "
            "déficit nominal de 6,4% do PIB estabiliza a razão; com d = 40%, só 3,2%.",
            "Por isso a sustentabilidade se discute pelo " + azb("primário requerido") + " e pelo diferencial "
            + azb("r − g") + " (o “efeito bola de neve”), não pelo resultado nominal, que já embute os juros "
            "sobre o estoque.",
        ],
        "dissecando": (cz("[meia-verdade · generalização]") + " A intuição “dívida alta pede mais esforço "
                       "fiscal” é correta para o primário, mas o item a estende ao nominal — onde vale o oposto — e "
                       "omite a condição r > g. Quando a frase junta “primários e nominais” no mesmo verbo, teste "
                       "cada um separadamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando a taxa real de juros supera o crescimento do PIB, quanto maior a dívida/PIB, maior o "
            "superávit primário necessário para estabilizá-la.”</i> → CERTO",
            "<i>“Se o crescimento do PIB supera os juros reais, a dívida/PIB só se estabiliza com superávit "
            "primário.”</i> → ERRADO (com g > r cabe até déficit primário)",
        ])],
        "reescrita": ("Estoques elevados de dívida pública exigem " + hl("superávits primários maiores, quando a "
                      "taxa real de juros supera o crescimento do PIB,") + " para que, assim, seja possível manter a "
                      "razão dívida/PIB constante, garantindo a sustentabilidade da dívida pública."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Superávit primário necessário = (r − g)·d; com d alto e r > g, exige-se superávit, "
                             "não déficit menor; o déficit nominal tende a ser maior com dívida alta. Comentários "
                             "empilhados de várias IAs, com quadros de indicadores de fluxo e estoque."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 19", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (indicadores de fluxo no 📖)"},
                          {"ref": "IMAGEM 20", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a IMAGEM 19)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00073
    {
        "id": "ECO-E3-L00073-1", "fonte_ref": "E3-L00073", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("O resultado nominal, seja ele positivo ou negativo, exclui do seu cálculo a correção monetária "
                      "e cambial que incide sobre a dívida pública."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O resultado nominal, seja ele positivo ou negativo, ") + vm("exclui do")
                    + az(" seu cálculo a correção monetária e cambial que incide sobre a dívida pública.")),
        "poucas": ("O resultado " + azb("nominal") + " é o mais abrangente: soma ao primário os " + azb("juros "
                   "nominais") + ", que contêm a correção monetária. Quem a exclui é o " + azb("operacional") + "."),
        "destrinchando": [
            "Escada dos conceitos: " + azb("primário") + " (sem juros) → " + azb("operacional") + " (+ juros "
            "reais) → " + azb("nominal") + " (+ juros nominais = juros reais + " + vd("correção monetária")
            + "). Na versão de manual (" + oc("Giambiagi e Além") + "), a atualização cambial da dívida também "
            "integra os encargos nominais.",
            "Identidade: " + vd("NFSP nominal = NFSP primária + juros nominais") + ". As NFSP nominais equivalem "
            "à variação da dívida líquida e por isso servem para ler a dinâmica do endividamento.",
            "Detalhe técnico das estatísticas do " + rx("BCB") + ": o efeito da variação cambial sobre o "
            "<b>estoque</b> da dívida externa e da interna indexada ao câmbio é registrado à parte, como "
            + azb("ajuste cambial") + " nos condicionantes da DLSP. O item cai de todo modo, porque a correção "
            "monetária está, sem discussão, dentro do nominal.",
            "Para que serve cada um: primário = esforço fiscal sob controle do governo (base das metas "
            "brasileiras); operacional = útil em inflação alta; nominal = impacto total sobre a dívida e o "
            "conceito usado nas comparações internacionais (déficit de 3% do PIB de Maastricht, por exemplo).",
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Descreve o operacional e o rotula de nominal, "
                       "trocando “inclui” por “exclui”. O “seja ele positivo ou negativo” é enchimento para dar "
                       "ar técnico. Pista: “nominal” é justamente o conceito sem expurgo inflacionário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado operacional exclui do seu cálculo a correção monetária que incide sobre a dívida "
            "pública.”</i> → CERTO",
            "<i>“O resultado primário inclui os juros reais da dívida, mas não a correção monetária.”</i> → "
            "ERRADO (o primário exclui todos os juros)",
        ])],
        "reescrita": ("O resultado nominal, seja ele positivo ou negativo, " + hl("inclui no") + " seu cálculo a "
                      "correção monetária e cambial que incide sobre a dívida pública."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O item descreve o resultado operacional; o nominal inclui juros nominais, com correção "
                             "monetária e cambial. Comentários extensos de várias IAs, com exemplos numéricos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00208
    {
        "id": "ECO-E3-L00208-1", "fonte_ref": "E3-L00208", "destino": "48", "subtema": H2["fin"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_IND,
        "rotulo_item": "Item",
        "assertiva": ("O estoque total de dívida pública, em termos reais, permanecerá constante, caso o superávit "
                      "primário seja igual ao pagamento dos juros reais da dívida."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O estoque total de dívida pública, <u>em termos reais</u>, permanecerá constante, caso o "
                      "superávit primário seja igual ao <u>pagamento dos juros reais</u> da dívida."),
        "poucas": ("Superávit primário = juros reais ⇔ " + azb("resultado operacional zero") + ": o governo paga "
                   "o custo real de carregar a dívida e o principal real não muda."),
        "destrinchando": [
            "Restrição orçamentária do governo em termos reais: " + vd("B<sub>t</sub> = (1 + r)·B<sub>t−1</sub> "
            "− SP<sub>t</sub>") + ". Logo ΔB = r·B<sub>t−1</sub> − SP. Com " + vm("SP = r·B") + ", ΔB = 0.",
            "Exemplo: dívida real de 100, juro real de 5% → juros reais de 5. Superávit primário de 5 → dívida "
            "real termina em 100. Superávit de 3 → sobe para 102; de 7 → cai para 98.",
            "Em linguagem de indicadores: primário − juros reais = " + azb("resultado operacional") + ". O item "
            "diz, em outras palavras, que operacional nulo mantém constante a dívida real.",
            "Não confundir com a razão " + azb("dívida/PIB") + ": para estabilizá-la basta " + vd("s = (r − g)·d")
            + ". Com PIB crescendo (g > 0), o superávit necessário é <b>menor</b> que os juros reais; se o governo "
            "pagar todos os juros reais, a dívida/PIB cai.",
            "Ressalva empírica: no mundo real, a dívida também se move por ajustes patrimoniais (reconhecimento de "
            "passivos, privatizações, câmbio) — a frase vale como identidade.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz a condição de estabilidade da dívida real. O "
                       "risco está na palavra decisiva: “em termos reais” e “estoque”, não “dívida/PIB”. Troque o "
                       "objeto e o item vira ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A razão dívida/PIB permanecerá constante, em uma economia em crescimento, caso o superávit "
            "primário seja igual aos juros reais.”</i> → ERRADO (cairia: bastaria superávit igual a [r − g]·d)",
            "<i>“O estoque nominal da dívida permanecerá constante caso o superávit primário iguale os juros "
            "reais.”</i> → ERRADO (com inflação, o estoque nominal cresce pela correção monetária)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Superávit primário igual aos juros reais (SP = r·B) mantém a dívida real constante; "
                             "para a razão dívida/PIB, a condição é s = (r − g)·d. Comentários de três IAs em "
                             "imagens de texto."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 293-300", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (equação da dinâmica da dívida e exemplos no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00088
    {
        "id": "ECO-E2-L00088-1", "fonte_ref": "E2-L00088", "destino": "49", "subtema": H2["ciclo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O orçamento predominante até 1964 limitava-se à simples contabilização das receitas e despesas "
                      "governamentais, sem função de planejamento, diferentemente do orçamento-programa que foi "
                      "instituído posteriormente pela Lei 4.320."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O orçamento predominante até 1964 limitava-se à <u>simples contabilização das receitas e "
                      "despesas governamentais, sem função de planejamento</u>, diferentemente do orçamento-programa "
                      "que foi instituído posteriormente pela <u>Lei 4.320</u>."),
        "poucas": ("O " + azb("orçamento tradicional") + " era mero inventário de receitas e despesas; a "
                   + vd("Lei 4.320/1964") + " abriu caminho ao " + azb("orçamento-programa") + ", que liga o "
                   "gasto a objetivos e metas."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "mantido o CERTO da fonte. Com rigor, a Lei 4.320 (17/3/1964) trouxe o “programa de "
                          "trabalho” e elementos do orçamento-programa, mas este só foi formalmente adotado com o "
                          + vd("Decreto-Lei 200/1967") + " (art. 16: “em cada ano, será elaborado um "
                          "orçamento-programa”) e consolidado pela classificação funcional-programática de 1974. "
                          "Uma banca exigente poderia julgar ERRADO o “instituído pela Lei 4.320”.")],
        "destrinchando": [
            "Tipos de orçamento em ordem histórica: (1) " + azb("tradicional ou clássico") + " — controle político "
            "do gasto, classificado por objeto (pessoal, material), sem metas; (2) " + azb("de desempenho")
            + " — passa a mostrar o que o governo faz (realizações), mas ainda sem vínculo com o planejamento; "
            "(3) " + azb("orçamento-programa") + " — integra planejamento e orçamento por programas com objetivos, "
            "metas e custos; depois vieram o base zero e o participativo.",
            "No " + rx("Brasil") + ": a " + vd("Lei 4.320/1964") + " fixou normas gerais de direito financeiro e "
            "o “programa de trabalho” do governo; o " + vd("DL 200/1967") + " fez do planejamento princípio da "
            "administração e exigiu o orçamento-programa anual; a " + vd("CF/1988") + " criou o tripé PPA–LDO–LOA, "
            "que amarra o orçamento ao plano.",
            "Marca do orçamento-programa: a pergunta deixa de ser “quanto se gasta com quê” e passa a ser “para "
            "quê se gasta e com que resultado”.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O contraste tradicional × programa é o núcleo e está "
                       "certo; o risco mora no detalhe legal (“instituído pela Lei 4.320”), simplificação que o "
                       "professor aceitou. Em banca rigorosa, desconfie de atribuições normativas taxativas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O orçamento de desempenho, por enfatizar as realizações do governo, já integrava plenamente "
            "planejamento e orçamento.”</i> → ERRADO (faltava o vínculo com o planejamento)",
            "<i>“A Constituição de 1988 instituiu o PPA, a LDO e a LOA como instrumentos integrados de "
            "planejamento e orçamento.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O orçamento clássico era controle contábil, sem planejamento; o orçamento-programa, "
                             "associado à Lei 4.320/64 e ao PAEG, incorporou objetivos e metas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: o orçamento-programa foi formalmente adotado pelo DL 200/1967 (art. 16); a Lei "
                    "4.320/1964 trouxe só o programa de trabalho — o CERTO da fonte simplifica a atribuição"],
    },
    # ------------------------------------------------------------------ E2-L00089
    {
        "id": "ECO-E2-L00089-1", "fonte_ref": "E2-L00089", "destino": "49", "subtema": H2["lrf"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A Lei de Responsabilidade Fiscal (LRF) proíbe, entre outras coisas, que as receitas de capital "
                      "sejam usadas para o pagamento de despesas correntes, reforçando o princípio de planejamento "
                      "orçamentário saudável e garantindo a sustentabilidade das finanças públicas ao longo do "
                      "tempo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A Lei de Responsabilidade Fiscal (LRF) proíbe, entre outras coisas, que <u>as receitas de "
                      "capital</u> sejam usadas para o pagamento de despesas correntes, reforçando o princípio de "
                      "planejamento orçamentário saudável e garantindo a sustentabilidade das finanças públicas ao "
                      "longo do tempo."),
        "poucas": ("A ideia é a do " + azb("equilíbrio entre capital e corrente") + ": receita que não se repete "
                   "não deve bancar gasto permanente. A LRF a aplica à " + vd("receita de alienação de bens")
                   + " (art. 44)."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "mantido o CERTO da fonte, mas a vedação legal é mais estreita que a frase: o "
                          + vd("art. 44 da LRF") + " proíbe usar a receita de capital <b>derivada da alienação de "
                          "bens e direitos</b> para despesa corrente (salvo se destinada por lei à previdência). "
                          "Para operações de crédito, outra receita de capital, vale a “regra de ouro” (CF, art. "
                          "167, III; LRF, art. 12, § 2º), que compara o total delas com as despesas de capital. "
                          "Lido literalmente, “as receitas de capital” generaliza.")],
        "destrinchando": [
            azb("Receitas de capital") + " (Lei 4.320, art. 11): operações de crédito, alienação de bens, "
            "amortização de empréstimos concedidos, transferências de capital. São, em regra, eventuais ou "
            "geram passivo; " + azb("despesas correntes") + " (pessoal, custeio, juros) se repetem todo ano.",
            "Daí duas travas: " + vm("LRF, art. 44") + " — venda de patrimônio não paga despesa corrente (vender "
            "a casa para pagar o supermercado); " + vm("regra de ouro") + " — o governo não pode tomar "
            "emprestado mais do que investe, salvo crédito suplementar ou especial aprovado por maioria absoluta "
            "do Congresso.",
            "A regra de ouro ficou famosa a partir de 2019, quando a União passou a precisar dessa autorização "
            "especial para cumpri-la — sinal de que se tomava dívida para pagar despesa corrente.",
            "Outros pilares da LRF (LC 101/2000): metas fiscais na LDO, limites de pessoal e de dívida, "
            "compensação para despesa obrigatória de caráter continuado, vedações em fim de mandato e "
            "transparência.",
        ],
        "dissecando": (cz("[paráfrase fiel · generalização]") + " Gabarito de professor que lê a regra em "
                       "linhas gerais. Em CEBRASPE, “as receitas de capital” sem qualificação seria um ponto de "
                       "ataque: a vedação da LRF é da receita de <b>alienação</b>; a de crédito tem regra própria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A LRF veda a aplicação da receita de capital derivada da alienação de bens e direitos para "
            "financiar despesa corrente, salvo se destinada por lei aos regimes de previdência.”</i> → CERTO",
            "<i>“A regra de ouro proíbe operações de crédito que excedam as despesas correntes.”</i> → ERRADO "
            "(o teto são as despesas de capital)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "GENERALIZACAO"], "moduladores": ["entre outras coisas"],
        "dificuldade": 2,
        "comentario_fonte": ("A LRF proíbe que receitas de capital, não recorrentes, cubram despesas correntes, "
                             "contínuas (o comentário chama isso de regra de ouro)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: a vedação da LRF (art. 44) restringe-se à receita de capital de alienação de bens "
                    "e direitos; operações de crédito seguem a regra de ouro (CF, art. 167, III) — o CERTO da fonte "
                    "generaliza",
                    "qualidade_fonte: o comentário de origem chama de “regra de ouro” a vedação do art. 44; a regra "
                    "de ouro é a da CF, art. 167, III (operações de crédito × despesas de capital)"],
    },
    # ------------------------------------------------------------------ E2-L00090
    {
        "id": "ECO-E2-L00090-1", "fonte_ref": "E2-L00090", "destino": "49", "subtema": H2["ciclo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Entre as estruturas de controle do orçamento brasileiro, destaca-se o princípio da "
                      "exclusividade que determina que a Lei Orçamentária Anual (LOA) deve tratar apenas de assuntos "
                      "econômicos, proibindo a inclusão de qualquer outra matéria não vinculada diretamente às "
                      "finanças públicas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Entre as estruturas de controle do orçamento brasileiro, destaca-se o <u>princípio da "
                      "exclusividade</u> que determina que a Lei Orçamentária Anual (LOA) deve tratar apenas de "
                      "assuntos econômicos, proibindo a inclusão de qualquer outra matéria não vinculada diretamente "
                      "às finanças públicas."),
        "poucas": ("O " + azb("princípio da exclusividade") + " (CF, art. 165, § 8º) impede “caudas "
                   "orçamentárias”: a LOA só trata de " + vd("previsão da receita e fixação da despesa") + ", com "
                   "duas ressalvas."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "mantido o CERTO da fonte, que lê a frase pelo espírito do princípio. A letra da CF é "
                          "mais precisa: a LOA “não conterá dispositivo estranho à previsão da receita e à fixação "
                          "da despesa” — e não “assuntos econômicos” em geral —, <b>ressalvadas</b> a autorização "
                          "para créditos suplementares e para operações de crédito, inclusive por antecipação de "
                          "receita. O “qualquer outra matéria” ignora essas exceções.")],
        "destrinchando": [
            "Origem: o princípio entrou no direito brasileiro com a " + vd("reforma constitucional de 1926") + " "
            "para acabar com as " + azb("caudas orçamentárias") + " (ou “orçamentos rabilongos”) — dispositivos "
            "alheios ao orçamento que o Congresso pendurava na lei de meios para aprová-los sem debate.",
            "Texto vigente (" + vm("CF, art. 165, § 8º") + "): a LOA não conterá dispositivo estranho à previsão "
            "da receita e à fixação da despesa, " + vm("ressalvadas") + " (1) a autorização para abertura de "
            + azb("créditos suplementares") + " e (2) a contratação de " + azb("operações de crédito")
            + ", ainda que por antecipação de receita (ARO).",
            "Vizinhos que a banca mistura: " + azb("unidade") + " (uma só lei para cada ente), "
            + azb("universalidade") + " (todas as receitas e despesas), " + azb("anualidade") + ", "
            + azb("não afetação") + " de impostos (art. 167, IV) e " + azb("orçamento bruto") + " (valores "
            "sem deduções).",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador absoluto]") + " Item de professor que parafraseia o "
                       "princípio em termos amplos. Os pontos frágeis são “assuntos econômicos” (impreciso) e o "
                       "“qualquer” que apaga as ressalvas constitucionais — exatamente onde o CEBRASPE costuma "
                       "atacar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo princípio da exclusividade, a LOA não pode conter autorização para abertura de créditos "
            "suplementares.”</i> → ERRADO (é ressalva expressa da CF)",
            "<i>“O princípio da exclusividade veda dispositivos estranhos à previsão da receita e à fixação da "
            "despesa, ressalvadas a autorização para créditos suplementares e para operações de crédito.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "GENERALIZACAO"], "moduladores": ["apenas", "qualquer"], "dificuldade": 2,
        "comentario_fonte": ("A exclusividade assegura que a LOA trate só de matéria orçamentária, sem dispositivos "
                             "estranhos às finanças públicas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: a CF (art. 165, § 8º) fala em previsão da receita e fixação da despesa, com "
                    "ressalvas (créditos suplementares e operações de crédito); “assuntos econômicos” e “qualquer "
                    "outra matéria” tornam o CERTO da fonte discutível",
                    "texto_corrigido: “destaca -se” → “destaca-se” (erro de digitação da fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00091
    {
        "id": "ECO-E2-L00091-1", "fonte_ref": "E2-L00091", "destino": "49", "subtema": H2["ciclo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O Plano Plurianual (PPA) é o documento mais abrangente do planejamento orçamentário no Brasil "
                      "e define de maneira detalhada e inflexível as ações e programas a serem realizados pelo "
                      "governo nos quatro anos subsequentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Plano Plurianual (PPA) é o documento mais abrangente do planejamento orçamentário no "
                       "Brasil e define de maneira ") + vm("detalhada e inflexível") + az(" as ações e programas a "
                       "serem realizados pelo governo nos quatro anos subsequentes.")),
        "poucas": ("O " + azb("PPA") + " é plano " + azb("estratégico") + " de médio prazo: fixa diretrizes, "
                   "objetivos e metas de forma regionalizada e pode ser revisto. O detalhe fica na " + azb("LOA")
                   + "."),
        "destrinchando": [
            vm("CF, art. 165, § 1º") + ": a lei do PPA estabelece, " + azb("de forma regionalizada") + ", as "
            + azb("diretrizes, objetivos e metas") + " da administração pública para as despesas de capital e "
            "outras delas decorrentes e para os programas de duração continuada.",
            "Divisão de trabalho do tripé: " + azb("PPA") + " (4 anos, estratégico) → " + azb("LDO") + " (metas "
            "e prioridades do ano seguinte, metas fiscais, orienta a LOA) → " + azb("LOA") + " (anual, "
            "operacional: estima a receita e fixa a despesa em detalhe).",
            "Flexibilidade: o PPA é alterado por lei de revisão quando mudam as condições, e nenhum investimento "
            "que ultrapasse um exercício pode começar sem estar nele ou em lei que autorize sua inclusão (CF, "
            "art. 167, § 1º) — é uma moldura, não um cronograma rígido.",
            "Vigência: do " + vd("2º ano do mandato ao 1º ano do mandato seguinte") + " (ADCT, art. 35, § 2º, I), "
            "o que garante continuidade na transição de governo.",
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " A 1ª metade (documento mais "
                       "abrangente) é aceitável; o erro está nos adjetivos “detalhada e inflexível”, que descrevem "
                       "melhor a LOA e contradizem a natureza estratégica do PPA."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A LOA detalha, para o exercício seguinte, a estimativa de receitas e a fixação de "
            "despesas.”</i> → CERTO",
            "<i>“O PPA estabelece, de forma centralizada, as metas de resultado primário do exercício "
            "seguinte.”</i> → ERRADO (troca de instrumento: metas fiscais anuais estão na LDO)",
        ])],
        "reescrita": ("O Plano Plurianual (PPA) é o documento mais abrangente do planejamento orçamentário no Brasil "
                      "e define de maneira " + hl("regionalizada, e revisável ao longo da vigência,") + " as ações e "
                      "programas a serem realizados pelo governo nos quatro anos subsequentes."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["inflexível"], "dificuldade": 1,
        "comentario_fonte": ("O PPA estabelece diretrizes amplas e estratégicas para quatro anos e pode ser "
                             "adaptado; não vincula o governo de forma inflexível."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00044
    {
        "id": "ECO-E3-L00044-1", "fonte_ref": "E3-L00044", "destino": "49", "subtema": H2["lrf"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_88,
        "rotulo_item": "Item",
        "assertiva": ("O principal objetivo da Lei de Responsabilidade Fiscal é permitir que estados e municípios "
                      "brasileiros emitam títulos de dívida livremente, a fim de fomentar o desenvolvimento "
                      "regional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O principal objetivo da Lei de Responsabilidade Fiscal é ")
                    + vm("permitir que estados e municípios brasileiros emitam títulos de dívida livremente, a fim "
                         "de fomentar o desenvolvimento regional") + az(".")),
        "poucas": ("A " + azb("LRF") + " (LC 101/2000) faz o oposto: estabelece normas de " + azb("gestão fiscal "
                   "responsável") + " e limita o endividamento de todos os entes."),
        "destrinchando": [
            vm("LRF, art. 1º, § 1º") + ": a responsabilidade na gestão fiscal pressupõe " + azb("ação planejada e "
            "transparente") + ", que previne riscos e corrige desvios capazes de afetar o equilíbrio das contas, "
            "com cumprimento de metas e obediência a limites (pessoal, dívida, operações de crédito, restos a "
            "pagar).",
            "Contexto: nos anos 1980 e 1990, estados financiavam déficits com bancos estaduais e emissão de "
            "títulos, e a União acabava socorrendo. A " + vd("Lei 9.496/1997") + " refinanciou as dívidas "
            "estaduais em troca de ajuste; o PROES privatizou ou liquidou bancos estaduais; a " + vd("LRF (2000)")
            + " fechou o desenho.",
            "Travas ao endividamento: limites globais de dívida consolidada fixados pelo " + azb("Senado") + " "
            "(Resolução 40/2001: " + vd("2 × RCL") + " para estados e " + vd("1,2 × RCL") + " para municípios); "
            "vedação de operações de crédito entre entes, mesmo como refinanciamento (art. 35); regras e prazos de recondução ao limite, "
            "com sanções (bloqueio de transferências voluntárias e de novas operações).",
            "A emissão de títulos por estados e municípios ficou praticamente restrita ao refinanciamento da "
            "dívida mobiliária existente.",
        ],
        "dissecando": (cz("[contradição]") + " Inverte por completo a finalidade da lei e lhe dá uma motivação "
                       "simpática (“desenvolvimento regional”) para soar plausível. Pista: “livremente” é "
                       "incompatível com qualquer lei de “responsabilidade”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A LRF vedou operações de crédito entre entes da Federação, ainda que sob a forma de novação ou "
            "refinanciamento de dívida contraída anteriormente.”</i> → CERTO",
            "<i>“Os limites globais da dívida consolidada de estados e municípios estão fixados no próprio texto "
            "da LRF.”</i> → ERRADO (são fixados por resolução do Senado Federal)",
        ])],
        "reescrita": ("O principal objetivo da Lei de Responsabilidade Fiscal é " + hl("estabelecer normas de "
                      "finanças públicas voltadas para a responsabilidade na gestão fiscal, limitando o endividamento "
                      "de estados e municípios") + "."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": ["livremente"], "dificuldade": 1,
        "comentario_fonte": ("A LRF busca equilíbrio e transparência fiscal e limita gastos com pessoal, dívida e "
                             "operações de crédito; não libera a emissão de títulos por estados e municípios."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00052
    {
        "id": "ECO-E3-L00052-1", "fonte_ref": "E3-L00052", "destino": "49", "subtema": H2["ciclo"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_96,
        "rotulo_item": "Item",
        "assertiva": ("A lei orçamentária anual, aprovada por cada ente da Federação, detalha o planejamento de curto "
                      "prazo relativo às receitas e despesas previstas para o ano seguinte."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A lei orçamentária anual, <u>aprovada por cada ente da Federação</u>, detalha o planejamento "
                      "de <u>curto prazo</u> relativo às receitas e despesas previstas para o ano seguinte."),
        "poucas": ("A " + azb("LOA") + " é o elo operacional do tripé: cada ente aprova a sua, que " + vd("estima "
                   "a receita e fixa a despesa") + " do exercício seguinte, em linha com a LDO e o PPA."),
        "destrinchando": [
            "Horizonte de cada instrumento: " + azb("PPA") + " = médio prazo (4 anos); " + azb("LDO") + " = "
            "ponte anual (metas e prioridades, metas fiscais, regras para elaborar a LOA); " + azb("LOA") + " = "
            "curto prazo (o exercício financeiro, que coincide com o ano civil — Lei 4.320, art. 34).",
            "Conteúdo da LOA federal (" + vm("CF, art. 165, § 5º") + "): " + azb("orçamento fiscal") + ", "
            + azb("orçamento de investimento das estatais") + " e " + azb("orçamento da seguridade social")
            + ".",
            "Autonomia federativa: União, estados, DF e municípios têm cada qual o seu PPA, a sua LDO e a sua "
            "LOA, de iniciativa privativa do chefe do Executivo e aprovados pelo respectivo Legislativo.",
            "Tecnicamente a LOA " + azb("estima") + " receitas (podem vir a mais ou a menos) e " + azb("fixa")
            + " despesas (teto de autorização, não obrigação de gastar — salvo as emendas impositivas e despesas "
            "obrigatórias).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição de manual com vocabulário trocado (“planejamento de "
                       "curto prazo” em vez de “estima a receita e fixa a despesa”). A pegadinha possível seria "
                       "atribuir a LOA só à União; a frase acerta ao dizer “cada ente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A lei orçamentária anual, aprovada exclusivamente pela União, vincula estados e "
            "municípios.”</i> → ERRADO (cada ente aprova a sua)",
            "<i>“A LOA fixa as receitas e estima as despesas do exercício.”</i> → ERRADO (inversão: estima "
            "receitas e fixa despesas)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A LOA é o instrumento de curto prazo, aprovado por cada ente, que estima receitas e "
                             "fixa despesas do exercício seguinte, compatível com LDO e PPA."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00053
    {
        "id": "ECO-E3-L00053-1", "fonte_ref": "E3-L00053", "destino": "49", "subtema": H2["ciclo"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_96,
        "rotulo_item": "Item",
        "assertiva": ("O plano plurianual, aprovado a cada quatro anos, é vigente a partir do primeiro ano de cada "
                      "mandato do chefe do Poder Executivo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O plano plurianual, aprovado a cada quatro anos, é vigente a partir do ") + vm("primeiro")
                    + az(" ano de cada mandato do chefe do Poder Executivo.")),
        "poucas": ("O " + azb("PPA") + " é elaborado no 1º ano do mandato e vige do " + vd("2º ano do mandato "
                   "até o fim do 1º ano do mandato seguinte") + "."),
        "destrinchando": [
            "Regra (" + vm("ADCT, art. 35, § 2º, I") + ", na falta da lei complementar do art. 165, § 9º): o "
            "projeto do PPA é enviado até " + vd("31 de agosto") + " do 1º ano do mandato (quatro meses antes do "
            "fim do exercício), devolvido para sanção até o encerramento da sessão legislativa e vigora até o "
            "fim do 1º exercício do mandato seguinte.",
            "Exemplo: governo empossado em 2023 executa, nesse ano, o PPA 2020–2023 herdado e aprova o "
            + vd("PPA 2024–2027") + ", que valerá até o 1º ano do próximo mandato.",
            "Razão do descasamento: o eleito precisa de tempo para transformar o programa de governo em plano, e "
            "o defasamento garante " + azb("continuidade") + " — nenhum ano fica sem plano na troca de governo.",
            "Prazos irmãos: " + azb("LDO") + " — envio até 15 de abril, devolução até 17 de julho (o Congresso não "
            "entra em recesso sem aprová-la); " + azb("LOA") + " — envio até 31 de agosto, devolução até o "
            "encerramento da sessão legislativa (22 de dezembro).",
        ],
        "dissecando": (cz("[dado alterado]") + " Troca um único ordinal (primeiro × segundo). O resto — "
                       "quadrienal, ligado ao mandato — está certo e embala o erro. 🔥 Prazos e vigência do PPA são "
                       "clássicos de CEBRASPE em orçamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PPA é elaborado no primeiro ano do mandato e vigora até o final do primeiro exercício "
            "financeiro do mandato subsequente.”</i> → CERTO",
            "<i>“O PPA tem vigência coincidente com o mandato presidencial, para assegurar a responsabilização do "
            "governante pelo plano.”</i> → ERRADO (vigência defasada de um ano)",
        ])],
        "reescrita": ("O plano plurianual, aprovado a cada quatro anos, é vigente a partir do " + hl("segundo")
                      + " ano de cada mandato do chefe do Poder Executivo" + hl(" até o fim do primeiro ano do "
                      "mandato seguinte") + "."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O PPA é aprovado no 1º ano do mandato e vigora do 2º ano até o 1º ano do mandato "
                             "seguinte, para garantir continuidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00217
    {
        "id": "ECO-E3-L00217-1", "fonte_ref": "E3-L00217", "destino": "49", "subtema": H2["lrf"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_90,
        "rotulo_item": "Item",
        "assertiva": ("A Lei de Responsabilidade Fiscal, aprovada no final da década de 1980, impôs limite para as "
                      "despesas com pessoal de estados e municípios, mas não incluía nessa restrição a União, o que "
                      "viria ocorrer no Governo de Fernando Henrique Cardoso."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Lei de Responsabilidade Fiscal, aprovada no ") + vm("final da década de 1980")
                    + az(", impôs limite para as despesas com pessoal de estados e municípios")
                    + vm(", mas não incluía nessa restrição a União, o que viria ocorrer no Governo de Fernando "
                         "Henrique Cardoso") + az(".")),
        "poucas": ("A " + azb("LRF") + " é a " + vd("LC 101, de maio de 2000") + " (governo FHC) e já nasceu "
                   "valendo para " + azb("todos os entes") + ", inclusive a União (limite de " + vd("50% da RCL")
                   + ")."),
        "destrinchando": [
            "Linha do tempo dos limites de pessoal: " + vd("CF/1988") + ", art. 169 — despesa com pessoal não pode "
            "exceder limites de lei complementar (o ADCT fixou 65% das receitas correntes provisoriamente); "
            + vd("Lei Camata I") + " (LC 82/1995) e " + vd("Lei Camata II") + " (LC 96/1999) — tetos em % da "
            "receita corrente líquida, mas sem sanções eficazes; " + vd("LRF") + " (LC 101/2000) — limites por ente e por "
            "Poder, com punições.",
            "Limites globais da LRF (" + vm("art. 19") + "), em % da " + azb("receita corrente líquida") + ": "
            + vd("União 50%") + ", " + vd("estados 60%") + ", " + vd("municípios 60%") + ". O art. 20 reparte "
            "entre os Poderes — na União, por exemplo, 40,9% para o Executivo.",
            "Mecanismos: limite prudencial (95% do teto) com vedações automáticas; excesso a eliminar em dois "
            "quadrimestres; sanções como suspensão de transferências voluntárias. A Lei 10.028/2000 (crimes "
            "fiscais) reforçou a responsabilização.",
            "Contexto: a LRF integra o ajuste pós-1999 (acordo com o FMI, metas de superávit primário) e o "
            "fecho da renegociação das dívidas estaduais.",
        ],
        "dissecando": (cz("[anacronismo · restrição indevida]") + " Dois erros empilhados: desloca a lei para o "
                       "fim dos anos 1980 (confusão com a CF/1988, que só previu a lei complementar) e restringe "
                       "sua abrangência aos entes subnacionais, inventando uma extensão posterior à União."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela LRF, o limite global de despesa com pessoal da União é inferior ao dos estados e "
            "municípios.”</i> → CERTO (50% × 60% da RCL)",
            "<i>“A Lei Camata, de 1995, foi a primeira norma a prever sanções efetivas pelo descumprimento dos "
            "limites de pessoal.”</i> → ERRADO (a falta de sanções eficazes é justamente o que a LRF corrigiu)",
        ])],
        "reescrita": ("A Lei de Responsabilidade Fiscal, aprovada no " + hl("ano 2000, no Governo de Fernando "
                      "Henrique Cardoso") + ", impôs limite para as despesas com pessoal de estados e municípios"
                      + hl(" e também da União") + "."),
        "tipo_erro": ["ANACRONISMO", "RESTRICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A LRF é de 2000 (governo FHC) e incluiu todos os entes desde a aprovação; limites de "
                             "pessoal: União 50%, estados e municípios 60% da RCL."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 309", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"},
                          {"ref": "IMAGEM 310", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (análise dos erros no 🧐)"},
                          {"ref": "IMAGEM 311", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (limites de pessoal no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00218
    {
        "id": "ECO-E3-L00218-1", "fonte_ref": "E3-L00218", "destino": "49", "subtema": H2["lrf"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_90,
        "rotulo_item": "Item",
        "assertiva": ("Promulgada em 2000, a Lei de Responsabilidade Fiscal impôs às unidades subnacionais tetos bem "
                      "definidos de endividamento, que estabeleceram limites à capacidade de tais entes fazerem uma "
                      "política autônoma de investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Promulgada em <u>2000</u>, a Lei de Responsabilidade Fiscal impôs às unidades subnacionais "
                      "<u>tetos bem definidos de endividamento</u>, que estabeleceram limites à capacidade de tais "
                      "entes fazerem uma política autônoma de investimento."),
        "poucas": ("Com a " + azb("LRF") + ", estados e municípios passaram a ter " + azb("limites de dívida e de "
                   "operações de crédito") + ": o investimento deixou de poder ser financiado à vontade com dívida."),
        "destrinchando": [
            "A LRF (art. 30) mandou fixar " + azb("limites globais de dívida consolidada") + "; o Senado o fez "
            "pela Resolução 40/2001 — " + vd("2 × RCL") + " para estados e " + vd("1,2 × RCL") + " para "
            "municípios —, e a Resolução 43/2001 disciplinou as operações de crédito.",
            "Somam-se a regra de ouro, a exigência de metas fiscais na LDO e a " + azb("compensação") + " para "
            "despesa obrigatória de caráter continuado (mais de dois exercícios): só se cria com fonte de "
            "receita ou corte de outra despesa.",
            "Leitura econômica: o desenho trocou autonomia por " + azb("disciplina") + ". Antes, estados usavam "
            "bancos estaduais e títulos próprios e transferiam o custo à União; depois, investimento subnacional "
            "passou a depender de espaço fiscal, aval do Tesouro e transferências.",
            "Crítica recorrente: em recessão, o ajuste recai sobre o investimento (a despesa mais fácil de cortar), "
            "o que torna a regra " + azb("pró-cíclica") + " para os entes subnacionais.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Data e conteúdo corretos. O risco é o juízo final "
                       "(“limites à capacidade… de política autônoma de investimento”), que parece crítica "
                       "opinativa, mas é consequência direta dos tetos de endividamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Promulgada em 2000, a LRF impôs tetos de endividamento apenas à União, preservando a autonomia "
            "dos entes subnacionais.”</i> → ERRADO (restrição indevida: vale para todos os entes)",
            "<i>“Pela LRF, nenhuma despesa obrigatória de caráter continuado pode ser criada sem indicação da "
            "fonte de custeio ou compensação.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A lei fixa limites para despesas com pessoal e para a dívida e exige metas; nenhuma "
                             "despesa continuada pode ser criada sem fonte ou compensação."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 312", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00836
    {
        "id": "ECO-E2-L00836-1", "fonte_ref": "E2-L00836", "destino": "50", "subtema": H2["regras"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_POL,
        "rotulo_item": "Item",
        "assertiva": ("A fragilidade fiscal é aspecto marcante ao longo da história da economia brasileira, mesmo com "
                      "inúmeros dispositivos legais que visam a controlar a despesa pública e, por conseguinte, o "
                      "endividamento. Entre tais dispositivos, destaca-se o Novo Arcabouço Fiscal, também conhecido "
                      "como Regime Fiscal Sustentável (PLP 93/2023), que limita, em termos reais, o crescimento do "
                      "déficit público a 2,5%."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A fragilidade fiscal é aspecto marcante ao longo da história da economia brasileira, mesmo "
                       "com inúmeros dispositivos legais que visam a controlar a despesa pública e, por conseguinte, "
                       "o endividamento. Entre tais dispositivos, destaca-se o Novo Arcabouço Fiscal, também "
                       "conhecido como Regime Fiscal Sustentável (PLP 93/2023), que limita, em termos reais, o "
                       "crescimento ") + vm("do déficit público") + az(" a 2,5%.")),
        "poucas": ("O " + azb("arcabouço") + " (LC 200/2023) limita o crescimento real da " + azb("despesa "
                   "primária") + " — entre " + vd("0,6% e 2,5%") + " ao ano —, não o do déficit."),
        "destrinchando": [
            "Regra de despesa: a despesa primária da União cresce, em termos reais, " + vd("70%") + " do "
            "crescimento real da receita primária (" + vd("50%") + " se a meta de primário do ano anterior não "
            "for cumprida), dentro de uma banda de " + vm("0,6% a 2,5% ao ano") + ". O piso evita arrocho em "
            "anos de receita fraca; o teto impede expansão forte em anos de bonança.",
            "Regra de resultado: " + azb("meta de resultado primário") + " na LDO, com intervalo de tolerância "
            "de ±0,25 p.p. do PIB; descumprimento aciona gatilhos de contenção. Há ainda piso para investimentos "
            "e destinação de parte do excesso de primário a investimento.",
            "Lógica: como a despesa cresce menos que a receita, o primário melhora gradualmente e a dívida/PIB "
            "tende a se estabilizar — o controle do déficit é <b>consequência</b>, não o objeto direto do limite.",
            "Histórico: o PLP 93/2023 virou a " + vd("Lei Complementar 200, de agosto de 2023") + ", substituindo "
            "o teto de gastos da EC 95/2016, que congelava a despesa em termos reais (só corrigida pelo IPCA). "
            "⏳ (out/2026) Parâmetros conforme a LC 200/2023; conferir alterações posteriores.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mantém o número certo (2,5%) e troca o objeto "
                       "(déficit × despesa). O preâmbulo longo e verdadeiro sobre fragilidade fiscal distrai do "
                       "único termo errado, no fim. 🔥 Arcabouço fiscal: a banca troca despesa, receita, déficit e "
                       "dívida entre si."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…que limita o crescimento real da despesa primária a 70% do crescimento real da receita, "
            "observada a banda de 0,6% a 2,5%.”</i> → CERTO",
            "<i>“…que, a exemplo do teto de gastos, mantém a despesa primária constante em termos reais.”</i> → "
            "ERRADO (o arcabouço permite crescimento real de até 2,5%)",
        ])],
        "reescrita": ("A fragilidade fiscal é aspecto marcante […]. Entre tais dispositivos, destaca-se o Novo "
                      "Arcabouço Fiscal, também conhecido como Regime Fiscal Sustentável (PLP 93/2023), que limita, "
                      "em termos reais, o crescimento " + hl("da despesa primária") + " a 2,5%."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O arcabouço limita o crescimento real da despesa a 70% do crescimento da receita, "
                             "entre 0,6% e 2,5%; não há limite para o crescimento do déficit."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01028
    {
        "id": "ECO-E2-L01028-1", "fonte_ref": "E2-L01028", "destino": "50", "subtema": H2["regras"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MODELOS,
        "rotulo_item": "Item",
        "assertiva": ("O regime fiscal conhecido como teto de gastos, estabelecido em 2016, tomava como premissa que a "
                      "raiz do problema fiscal brasileiro era o acelerado crescimento da despesa primária, que "
                      "assumia trajetória contracíclica, crescendo em períodos de retração econômica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O regime fiscal conhecido como teto de gastos, estabelecido em 2016, tomava como premissa que "
                       "a raiz do problema fiscal brasileiro era o acelerado crescimento da despesa primária, que "
                       "assumia trajetória ") + vm("contracíclica, crescendo em períodos de retração econômica")
                    + az(".")),
        "poucas": ("O diagnóstico do " + azb("teto") + " era de despesa primária em " + azb("alta estrutural")
                   + ": crescia acima do PIB em qualquer fase do ciclo, inclusive nas expansões — não só nas "
                   "recessões."),
        "destrinchando": [
            "A " + vd("EC 95/2016") + " limitou, por 20 exercícios (com revisão possível após 10), a despesa "
            "primária federal ao valor do ano anterior corrigido pelo " + vd("IPCA") + ": crescimento real "
            "zero, de modo que a despesa cairia como proporção do PIB à medida que a economia crescesse.",
            "Premissa: desde a CF/1988, a despesa primária do governo central subia de forma contínua — de "
            "cerca de " + vd("14% do PIB em 1997") + " para perto de " + vd("20% em 2016") + " —, puxada por "
            "previdência, vinculações e despesas obrigatórias indexadas, e não por resposta ao ciclo.",
            "Por que não “contracíclica”: nos anos de crescimento forte (2004–2010), a despesa também acelerou, "
            "acompanhando a receita. Política " + azb("contracíclica") + " exige poupar na expansão e gastar na "
            "recessão; o padrão brasileiro era " + azb("pró-cíclico") + " ou acíclico, sempre expansivo.",
            "Críticas ao teto: rigidez (despesas obrigatórias comprimindo as discricionárias e o investimento) e "
            "sucessivas exceções (2020–2022). Foi substituído pelo arcabouço da LC 200/2023.",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A 1ª parte (despesa primária acelerada como "
                       "raiz) é o diagnóstico oficial; o erro foi enxertado na qualificação “contracíclica”. Pista: "
                       "se a despesa só crescesse em recessões, o problema seria do ciclo, e não justificaria um "
                       "teto de 20 anos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O teto de gastos limitava o crescimento da despesa primária federal à inflação do ano "
            "anterior, sem prever crescimento real.”</i> → CERTO",
            "<i>“O teto de gastos limitava o crescimento do resultado nominal do governo central.”</i> → ERRADO "
            "(o objeto era a despesa primária)",
        ])],
        "reescrita": ("O regime fiscal conhecido como teto de gastos, estabelecido em 2016, tomava como premissa que "
                      "a raiz do problema fiscal brasileiro era o acelerado crescimento da despesa primária, que "
                      "assumia trajetória " + hl("de alta estrutural, crescendo acima do PIB tanto em períodos de "
                      "expansão quanto de retração econômica") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A premissa era de despesa primária crescente e persistente, acima da receita e do PIB; "
                             "crescia também nas expansões — trajetória pró-cíclica, não contracíclica."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: despesa primária do governo central de cerca de 14% (1997) para cerca de "
                    "20% do PIB (2016), série do Tesouro Nacional, em valores arredondados"],
    },
    # ------------------------------------------------------------------ E2-L01438
    {
        "id": "ECO-E2-L01438-1", "fonte_ref": "E2-L01438", "destino": "50", "subtema": H2["traj"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_FHC,
        "rotulo_item": "Item",
        "assertiva": ("Durante os dois mandatos de Fernando H. Cardoso, as receitas obtidas com as privatizações de "
                      "empresas estatais, bem como o sucesso em reduzir a inflação de forma duradoura, contribuíram "
                      "para a redução da dívida pública em porcentagem do PIB."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Durante os dois mandatos de Fernando H. Cardoso, as receitas obtidas com as privatizações de "
                       "empresas estatais, bem como o sucesso em reduzir a inflação de forma duradoura, ")
                    + vm("contribuíram para a redução") + az(" da dívida pública em porcentagem do PIB.")),
        "poucas": ("Apesar das privatizações e do Real, a " + azb("DLSP") + " subiu de cerca de " + vd("30% para "
                   "cerca de 60% do PIB") + " entre 1994 e 2002, puxada por juros altos, esqueletos e câmbio."),
        "destrinchando": [
            "Os dois fatos da frase são verdadeiros — " + rx("privatizações") + " (Vale, sistema Telebrás, "
            "elétricas, bancos estaduais) e inflação baixa e duradoura —, mas o resultado afirmado é falso: a "
            "dívida líquida praticamente " + vd("dobrou") + " em proporção do PIB.",
            "Por que subiu: (1) " + azb("juros reais muito altos") + " para sustentar a âncora cambial e enfrentar "
            "as crises do México, da Ásia e da Rússia; (2) " + azb("resultados primários") + " nulos ou deficitários "
            "em 1995–1998 (superávits expressivos só a partir de 1999, com o acordo com o FMI); (3) reconhecimento de "
            + azb("esqueletos") + " (FCVS, dívidas antigas) e custos do saneamento bancário (PROER, PROES); (4) "
            + azb("desvalorizações") + " de 1999 e 2001–2002 sobre a dívida indexada ao dólar.",
            "O próprio fim da alta inflação pesou: deixou de haver a corrosão inflacionária de passivos e o "
            "imposto inflacionário que ajudavam a fechar as contas, e despesas antes “comidas” pela inflação "
            "passaram a aparecer.",
            "Privatizações abateram dívida, mas eram receitas únicas, pequenas diante da conta de juros — "
            "estoque × fluxo.",
        ],
        "dissecando": (cz("[nexo indevido · meia-verdade]") + " Junta dois fatos verdadeiros do período a uma "
                       "consequência que não ocorreu. 🔥 Em história econômica, a banca adora o “paradoxo FHC”: "
                       "estabilização e privatização com dívida/PIB em alta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Durante os governos FHC, a dívida líquida do setor público cresceu em proporção do PIB, apesar "
            "das receitas de privatização.”</i> → CERTO",
            "<i>“O setor público consolidado gerou superávits primários expressivos desde 1995.”</i> → "
            "ERRADO (dado alterado: só a partir de 1999)",
        ])],
        "reescrita": ("Durante os dois mandatos de Fernando H. Cardoso, as receitas obtidas com as privatizações de "
                      "empresas estatais, bem como o sucesso em reduzir a inflação de forma duradoura, "
                      + hl("não impediram o aumento") + " da dívida pública em porcentagem do PIB."),
        "tipo_erro": ["NEXO_INDEVIDO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A dívida/PIB cresceu nos anos FHC (de cerca de 30% para cerca de 60% do PIB) por juros "
                             "altos, esqueletos, PROER e desvalorização cambial; privatizações não compensaram."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 340", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (série de DLSP/PIB 1995–2012 sem valores transcritos; trajetória "
                                   "absorvida no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00314
    {
        "id": "ECO-E2-L00314-1", "fonte_ref": "E2-L00314", "destino": "55", "subtema": H2["inv"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARM_INV,
        "rotulo_item": "Item",
        "assertiva": ("Na visão keynesiana, a poupança antecede o investimento: sem aumento de poupança ex-ante, não "
                      "é possível expandir o crédito bancário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na visão keynesiana, ")
                    + vm("a poupança antecede o investimento: sem aumento de poupança ex-ante, não é possível "
                         "expandir o crédito bancário") + az(".")),
        "poucas": ("Para " + oc("Keynes") + ", o " + azb("investimento vem primeiro") + ", financiado por "
                   + azb("crédito") + " bancário; a poupança é gerada " + azb("ex post") + ", pelo multiplicador."),
        "destrinchando": [
            "Visão " + azb("clássica/neoclássica") + " (fundos emprestáveis): a poupança das famílias é a fonte "
            "dos recursos; a taxa de juros equilibra oferta de poupança e demanda de investimento. Sem poupar "
            "antes, não se investe.",
            "Visão de " + oc("Keynes") + ": o banco cria crédito (moeda) sem depósito prévio de poupança; o "
            "empresário investe; a renda cresce pelo " + azb("multiplicador") + " até que a poupança gerada iguale "
            "o investimento — " + vd("S = I ex post") + ". O que limita o investimento é a " + azb("liquidez")
            + " (finance), não a poupança.",
            "O " + azb("motivo finance") + " (1937) e, depois, o circuito " + azb("finance–funding")
            + " dos pós-keynesianos: o crédito de curto prazo financia o gasto; a poupança gerada permite depois "
            "consolidar a dívida em prazos longos (funding).",
            "Corolário: o " + azb("paradoxo da parcimônia") + " — se todos tentam poupar mais, a renda cai e a "
            "poupança agregada não aumenta.",
        ],
        "dissecando": (cz("[inversão · troca de ator]") + " Atribui a Keynes a tese dos fundos emprestáveis, "
                       "que ele combateu. Pista: “poupança ex-ante” como pré-condição é marca neoclássica; em "
                       "Keynes, a sequência é crédito → investimento → renda → poupança."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na visão keynesiana, o investimento pode ser financiado por crédito bancário, e a poupança "
            "correspondente surge ex post, pela expansão da renda.”</i> → CERTO",
            "<i>“Na teoria dos fundos emprestáveis, a taxa de juros é determinada pela preferência pela "
            "liquidez.”</i> → ERRADO (troca de teoria: é pela poupança e pelo investimento)",
        ])],
        "reescrita": ("Na visão keynesiana, " + hl("o investimento antecede a poupança: o crédito bancário pode ser "
                      "expandido sem aumento prévio de poupança, que surge ex post pela expansão da renda") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Na visão keynesiana o investimento é financiado pelo crédito e a poupança surge ex "
                             "post, como resultado da expansão da renda."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00580
    {
        "id": "ECO-E2-L00580-1", "fonte_ref": "E2-L00580", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a Hipótese do Ciclo de Vida (HCV) indivíduos mais jovens, em sua fase de trabalho, "
                      "tendem a praticar “poupança negativa”, utilizando seus patrimônios acumulados para financiar o "
                      "consumo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a Hipótese do Ciclo de Vida (HCV) indivíduos mais ")
                    + vm("jovens, em sua fase de trabalho,") + az(" tendem a praticar “poupança negativa”, "
                         "utilizando seus patrimônios acumulados para financiar o consumo.")),
        "poucas": ("No " + azb("ciclo de vida") + " quem trabalha " + azb("poupa") + "; quem consome o patrimônio "
                   "acumulado (" + azb("despoupança") + ") é o " + vd("aposentado") + ". O item troca as fases."),
        "destrinchando": [
            oc("Modigliani") + " (com Brumberg e Ando, anos 1950–1960): o indivíduo planeja o consumo para a vida "
            "inteira e, com renda que varia por fases, " + azb("suaviza o consumo") + ". Versão simples: renda "
            "constante enquanto trabalha, zero na aposentadoria, consumo constante do início ao fim.",
            "Fase ativa: renda > consumo → " + vd("poupança positiva") + ", que forma o patrimônio. Aposentadoria: "
            "renda ≈ 0 < consumo → " + vd("poupança negativa") + ", financiada justamente pelo patrimônio "
            "acumulado. Por isso a riqueza segue uma “corcova”: sobe até a aposentadoria e depois cai.",
            "Nuance: na versão com renda em formato de corcova, o jovem em início de carreira pode consumir acima da "
            "renda — mas tomando <b>crédito</b>, não usando patrimônio, que ainda não tem. A frase do item só "
            "funciona para o idoso.",
            "Função consumo resultante (Ando–Modigliani): " + vd("C = αW + βY") + " — o consumo depende da "
            + azb("riqueza") + " (W) e da renda do trabalho (Y).",
        ],
        "grafico_verso": "ECO-E2-L00580-1-V1",
        "dissecando": (cz("[troca de ator · inversão]") + " Troca o grupo etário: a despoupança com uso do "
                       "patrimônio é do aposentado. Pista interna: “patrimônios acumulados” não combina com "
                       "“jovens” — só tem patrimônio a gastar quem já poupou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a HCV, indivíduos aposentados tendem a despoupar, utilizando o patrimônio acumulado na "
            "fase ativa para financiar o consumo.”</i> → CERTO",
            "<i>“Segundo a HCV, o consumo acompanha a trajetória da renda corrente em cada fase da vida.”</i> → "
            "ERRADO (o consumo é suavizado; quem acompanha a renda corrente é o consumo keynesiano)",
        ])],
        "reescrita": ("Segundo a Hipótese do Ciclo de Vida (HCV) indivíduos mais " + hl("idosos, já aposentados,")
                      + " tendem a praticar “poupança negativa”, utilizando seus patrimônios acumulados para "
                      "financiar o consumo."),
        "tipo_erro": ["TROCA_ATOR", "INVERSAO"], "moduladores": ["tendem"], "dificuldade": 1,
        "comentario_fonte": ("Na HCV, o indivíduo poupa quando jovem, na fase ativa, e despoupa na aposentadoria, "
                             "mantendo o consumo estável."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “(HCV) Indivíduos” → “(HCV) indivíduos” (maiúscula indevida da fonte)",
                    "quase_duplicata: ECO-E2-L00685-1 e ECO-E2-L00900-1 (ciclo de vida: propensão média a "
                    "consumir)"],
    },
    # ------------------------------------------------------------------ E2-L00581
    {
        "id": "ECO-E2-L00581-1", "fonte_ref": "E2-L00581", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("A Hipótese da Renda Permanente (HRP) sugere que um corte de impostos temporário teria um "
                      "efeito de estímulo muito menor na demanda do que um corte permanente, devido ao comportamento "
                      "de suavização do consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Hipótese da Renda Permanente (HRP) sugere que um corte de impostos <u>temporário</u> teria "
                      "um efeito de estímulo <u>muito menor</u> na demanda do que um corte permanente, devido ao "
                      "comportamento de suavização do consumo."),
        "poucas": ("Na " + azb("renda permanente") + ", o consumo responde ao que a pessoa espera ganhar ao longo do "
                   "tempo; um corte " + vd("temporário") + " mexe pouco nisso e é, em boa parte, poupado."),
        "destrinchando": [
            oc("Milton Friedman") + " (<i>A Theory of the Consumption Function</i>, 1957): renda corrente = "
            + azb("renda permanente") + " (Y<sup>P</sup>, a média esperada) + " + azb("renda transitória")
            + " (Y<sup>T</sup>, desvios passageiros). O consumo é " + vd("C = αY<sup>P</sup>") + ".",
            "Corte permanente de impostos → eleva Y<sup>P</sup> por inteiro → consumo sobe quase um a um. Corte "
            "temporário → vira renda transitória → a " + azb("propensão marginal a consumir") + " dela é pequena; "
            "a maior parte é poupada e o consumo é espalhado ao longo dos anos.",
            "Aplicação: pacotes de estímulo com devolução única de impostos tendem a ter multiplicador baixo; já "
            "mudanças de alíquota vistas como duradouras mexem no consumo.",
            "Limites: famílias com " + azb("restrição de liquidez") + " (sem acesso a crédito) gastam o corte "
            "temporário quase todo — por isso, na prática, o efeito não é nulo e depende do público atingido.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Reproduz a implicação clássica da HRP. O "
                       "“muito menor” (e não “nulo”) e o “sugere” protegem o item; a pista é a causa citada, "
                       "suavização do consumo, que é o mecanismo correto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela HRP, um corte temporário de impostos não tem efeito algum sobre o consumo corrente.”</i> → "
            "ERRADO (modulador absoluto: o efeito é pequeno, não nulo)",
            "<i>“Na função keynesiana, cortes temporários e permanentes de impostos de mesmo valor têm o mesmo "
            "efeito imediato sobre o consumo.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["sugere", "muito menor"],
        "dificuldade": 1,
        "comentario_fonte": ("Na HRP o consumo depende da renda permanente; corte temporário afeta pouco essa renda "
                             "e é em grande parte poupado; corte permanente eleva mais o consumo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00685
    {
        "id": "ECO-E2-L00685-1", "fonte_ref": "E2-L00685", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MODELOS,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a hipótese do Ciclo de Vida de Modigliani, a propensão média a consumir tende a ser "
                      "constante ao longo da vida do indivíduo, independentemente de sua idade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a hipótese do Ciclo de Vida de Modigliani, a propensão média a consumir ")
                    + vm("tende a ser constante ao longo da vida do indivíduo, independentemente de sua idade")
                    + az(".")),
        "poucas": ("Constante é o " + azb("consumo") + ", não a razão C/Y. Como a renda muda com a idade, a "
                   + azb("PMeC") + " " + vd("varia") + ": é baixa na fase ativa e alta na aposentadoria."),
        "destrinchando": [
            "Propensão média a consumir: " + vd("PMeC = C/Y") + ". No ciclo de vida, C é suavizado e Y segue as "
            "fases: na fase ativa, Y alto → C/Y abaixo de 1 (poupa); na aposentadoria, Y baixo → C/Y acima de 1 "
            "(despoupa); no início da carreira, com renda ainda baixa, C/Y também tende a ser alto.",
            "Onde a constância aparece: no " + azb("agregado de longo prazo") + ". Com C = αW + βY, a PMeC "
            "agregada = α(W/Y) + β; no longo prazo riqueza e renda crescem juntas, W/Y fica estável e a PMeC "
            "também — o que reconcilia a teoria com as séries longas de " + oc("Kuznets") + ".",
            "No curto prazo, quando a renda sobe e a riqueza não, W/Y cai e a PMeC agregada diminui — padrão "
            "das regressões de corte transversal e de séries curtas.",
            vm("Regra-âncora: ciclo de vida = consumo suave, PMeC variável no indivíduo e constante só no longo "
               "prazo agregado."),
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " Troca “consumo constante” por "
                       "“propensão média constante” e reforça com “independentemente de sua idade” — justamente a "
                       "variável que move a PMeC na teoria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na HCV, a propensão média a consumir do indivíduo é maior na aposentadoria do que na fase "
            "ativa.”</i> → CERTO",
            "<i>“Na HCV, a propensão média a consumir agregada é constante no curto prazo.”</i> → ERRADO (é "
            "constante só no longo prazo)",
        ])],
        "reescrita": ("Segundo a hipótese do Ciclo de Vida de Modigliani, a propensão média a consumir "
                      + hl("varia ao longo da vida do indivíduo, conforme sua idade: é menor na fase ativa, quando ele "
                           "poupa, e maior na aposentadoria, quando despoupa") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["independentemente"], "dificuldade": 2,
        "comentario_fonte": ("O consumo é estável, a renda varia com a idade; a PMeC varia ao longo da vida e só é "
                             "estável no agregado de longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00900-1 (PMeC no ciclo de vida, curto × longo prazo) e "
                    "ECO-E2-L00580-1"],
    },
    # ------------------------------------------------------------------ E2-L00764
    {
        "id": "ECO-E2-L00764-1", "fonte_ref": "E2-L00764", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_INTERT,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a Teoria da Renda Permanente, uma redução de impostos correntes do tipo "
                      "lump-sum compensada por um aumento futuro de impostos corrigidos pela taxa de juros aumenta a "
                      "poupança corrente e não provoca variações nos níveis de consumo corrente e futuro."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a Teoria da Renda Permanente, uma redução de impostos correntes do tipo "
                      "lump-sum <u>compensada por um aumento futuro de impostos corrigidos pela taxa de juros</u> "
                      "aumenta a poupança corrente e <u>não provoca variações</u> nos níveis de consumo corrente e "
                      "futuro."),
        "poucas": ("O corte compensado não muda o " + azb("valor presente") + " dos impostos, logo não muda a "
                   + azb("renda permanente") + ": o consumo fica igual e o alívio de hoje é " + vd("poupado")
                   + " para pagar o imposto de amanhã."),
        "destrinchando": [
            "Restrição orçamentária intertemporal da família: o que importa é o valor presente da renda líquida "
            "de impostos. Corte de T hoje e aumento de T(1 + r) amanhã → " + vd("valor presente inalterado")
            + " → Y<sup>P</sup> igual → consumo igual em todas as datas.",
            "Contabilidade: a renda disponível sobe hoje, o consumo não → a " + azb("poupança privada")
            + " sobe exatamente o valor do corte. A " + azb("poupança pública") + " cai o mesmo valor (déficit "
            "financiado por dívida): a " + vd("poupança nacional não muda") + ".",
            "É a " + azb("equivalência ricardiana") + ", formalizada por " + oc("Robert Barro") + " (1974, "
            "<i>Are Government Bonds Net Wealth?</i>): títulos públicos não são riqueza líquida, porque "
            "embutem impostos futuros. A ideia remonta a " + oc("David Ricardo") + ", que a enunciou e duvidou de "
            "sua validade prática.",
            "Quando falha: restrição de liquidez, miopia, horizonte finito sem altruísmo entre gerações (o "
            "imposto futuro cai sobre outros), impostos distorcivos (não lump-sum) e incerteza.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Parece contradizer o senso comum (“corte de "
                       "imposto estimula consumo”), mas as premissas — lump-sum, compensado com juros, renda "
                       "permanente — levam direto à neutralidade. O “aumenta a poupança corrente” é consequência, "
                       "não pegadinha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…aumenta a poupança nacional e não provoca variações no consumo.”</i> → ERRADO (troca de "
            "conceito: sobe a poupança privada; a nacional fica igual)",
            "<i>“Se as famílias enfrentam restrição de liquidez, o mesmo corte compensado eleva o consumo "
            "corrente.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A redução compensada por imposto futuro de igual valor presente não altera a renda "
                             "permanente; o corte é poupado e o consumo não muda (equivalência ricardiana)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00899
    {
        "id": "ECO-E2-L00899-1", "fonte_ref": "E2-L00899", "destino": "55", "subtema": H2["inv"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONS_INV,
        "rotulo_item": "Item",
        "assertiva": ("Um Q de Tobin maior que 1 sinaliza que o valor de mercado dos ativos da empresa supera o seu "
                      "custo de reposição, incentivando a empresa a investir mais, pois cada unidade de investimento "
                      "adicional tem um custo inferior ao seu valor de mercado esperado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um Q de Tobin <u>maior que 1</u> sinaliza que o valor de mercado dos ativos da empresa "
                      "<u>supera o seu custo de reposição</u>, incentivando a empresa a investir mais, pois cada "
                      "unidade de investimento adicional tem um custo inferior ao seu valor de mercado esperado."),
        "poucas": (vd("q = valor de mercado do capital ÷ custo de reposição") + ". Com " + vd("q > 1")
                   + ", instalar uma máquina custa menos do que o mercado acionário paga por ela: vale investir."),
        "destrinchando": [
            oc("James Tobin") + " (1969) ligou investimento e mercado financeiro: o preço das ações resume as "
            "expectativas sobre os lucros futuros do capital instalado. Se o mercado avalia a empresa acima do "
            "custo de repor seus ativos, criar capital novo " + azb("gera valor") + " para os acionistas.",
            vd("q > 1") + " → investir (expande o estoque de capital); " + vd("q < 1") + " → não repor o capital "
            "que se deprecia, e pode ser mais barato comprar empresas existentes na bolsa do que construir "
            "(fusões e aquisições); " + vd("q = 1") + " → equilíbrio de longo prazo.",
            "Ponte com a teoria neoclássica: no ótimo, o q marginal iguala a razão entre o valor presente do "
            "produto marginal do capital e seu custo; juros mais baixos elevam o valor das ações, o q e o "
            "investimento — um canal de transmissão da " + azb("política monetária") + ".",
            "Limite empírico: o que importa é o " + azb("q marginal") + " (da unidade adicional), mas só se observa "
            "o " + azb("q médio") + "; e bolhas ou pessimismo da bolsa podem afastar q dos fundamentos.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição correta com a justificativa certa (custo da unidade "
                       "adicional < valor de mercado). A armadilha usual seria inverter o limiar (q < 1 → investir) "
                       "ou trocar custo de reposição por valor contábil."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um q de Tobin menor que 1 indica que é mais vantajoso para a empresa expandir sua capacidade "
            "produtiva do que adquirir empresas já existentes.”</i> → ERRADO (inversão: com q < 1, comprar "
            "empresas é mais barato)",
            "<i>“Uma queda na taxa de juros, ao valorizar as ações, tende a elevar o q de Tobin e o "
            "investimento.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("q = valor de mercado do capital instalado ÷ custo de reposição; q > 1 → vale investir; "
                             "q < 1 → não há incentivo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00900
    {
        "id": "ECO-E2-L00900-1", "fonte_ref": "E2-L00900", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONS_INV,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo do Ciclo de Vida, a propensão média a consumir é aproximadamente "
                      "constante tanto no curto como no longo prazo, dado que a expectativa de renda do indivíduo é "
                      "constante ao longo do seu ciclo de vida."),
        "gabarito": "ERRADO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": (az("De acordo com o modelo do Ciclo de Vida, a propensão média a consumir é aproximadamente "
                       "constante ") + vm("tanto no curto como") + az(" no longo prazo, dado que ")
                    + vm("a expectativa de renda do indivíduo é constante") + az(" ao longo do seu ciclo de vida.")),
        "poucas": ("No ciclo de vida a " + azb("renda varia") + " por fases e o " + azb("consumo é suavizado")
                   + "; por isso a PMeC " + vd("oscila no curto prazo") + " e só é estável no longo prazo."),
        "destrinchando": [
            "A premissa do item está invertida: o que o indivíduo mantém estável é o " + azb("consumo") + "; a "
            + azb("renda") + " muda sistematicamente (baixa no início, alta na maturidade, baixa na "
            "aposentadoria). A poupança é o amortecedor.",
            "Curto prazo: uma alta de renda corrente sem alta proporcional da riqueza ou da renda esperada "
            "reduz C/Y. Na versão de " + oc("Friedman") + ", " + vd("PMeC = C/Y = αY<sup>P</sup>/Y") + ": "
            "quando Y fica acima de Y<sup>P</sup> (renda transitória positiva), a PMeC cai; abaixo, sobe.",
            "Longo prazo: de década em década, a variação da renda é quase toda permanente (e a riqueza cresce "
            "com ela), de modo que " + vd("Y<sup>P</sup>/Y ≈ constante") + " e a PMeC agregada fica estável.",
            "É assim que ciclo de vida e renda permanente resolvem o " + azb("enigma do consumo") + ": funções "
            "de curto prazo e de corte transversal com PMeC decrescente (como a keynesiana) convivem com séries "
            "longas de PMeC constante (" + oc("Kuznets") + ").",
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A estabilidade no longo prazo é verdadeira; o erro está "
                       "em estendê-la ao curto prazo e em justificá-la com renda constante, quando a teoria parte "
                       "de renda <b>variável</b>. Pista: “tanto… como” costuma esconder a metade falsa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela HRP, em anos de renda transitoriamente alta, a propensão média a consumir tende a "
            "cair.”</i> → CERTO",
            "<i>“Pela HCV, a propensão média a consumir de longo prazo é decrescente com a renda, como na função "
            "keynesiana.”</i> → ERRADO (no longo prazo ela é constante)",
        ])],
        "reescrita": ("De acordo com o modelo do Ciclo de Vida, a propensão média a consumir é aproximadamente "
                      "constante " + hl("só") + " no longo prazo, dado que " + hl("o indivíduo suaviza o consumo, "
                      "embora sua renda varie") + " ao longo do seu ciclo de vida."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["tanto… como", "aproximadamente"],
        "dificuldade": 2,
        "comentario_fonte": ("A renda varia nas fases do ciclo de vida e o consumo é mantido; a PMeC varia no curto "
                             "prazo e tende a ser constante no longo prazo (PMeC = αY<sup>P</sup>/Y)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 147", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (PMeC = αYP/Y no 📖)"}],
        "alertas": ["nota_redacao: o verso da fonte não traz gabarito explícito; ERRADO resolvido pelo conteúdo do "
                    "comentário (PMeC varia no curto prazo)",
                    "quase_duplicata: ECO-E2-L00685-1 (PMeC constante ao longo da vida, ERRADO)"],
    },
    # ------------------------------------------------------------------ E2-L00901
    {
        "id": "ECO-E2-L00901-1", "fonte_ref": "E2-L00901", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONS_INV,
        "rotulo_item": "Item",
        "assertiva": ("A hipótese do Ciclo de Vida sugere que a distribuição etária da população e a taxa de "
                      "crescimento da economia são fatores determinantes da poupança agregada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A hipótese do Ciclo de Vida sugere que a <u>distribuição etária da população</u> e a <u>taxa "
                      "de crescimento da economia</u> são fatores determinantes da poupança agregada."),
        "poucas": ("Poupança agregada = poupança dos ativos − despoupança dos aposentados. O saldo depende do "
                   + azb("peso de cada grupo") + " (estrutura etária) e de quanto a renda dos jovens supera a "
                   "dos velhos (" + azb("crescimento") + ")."),
        "destrinchando": [
            "Estrutura etária: mais pessoas em idade ativa em relação a aposentados → mais gente poupando do que "
            "despoupando → " + vd("poupança agregada maior") + ". O " + azb("bônus demográfico") + " eleva a "
            "poupança; o envelhecimento a reduz.",
            "Crescimento: numa economia estacionária (sem crescimento da população nem da renda), a poupança dos "
            "ativos é exatamente gasta pelos aposentados e a " + vd("poupança líquida agregada é zero")
            + ". Se a economia cresce, cada geração ativa é mais numerosa ou mais rica que a aposentada, e a "
            "poupança agregada fica positiva — maior quanto maior o crescimento.",
            "Por isso a taxa de poupança, na previsão de " + oc("Modigliani") + ", depende do " + azb("crescimento")
            + " e não do nível de renda per capita — uma diferença notável em relação à função keynesiana, em que "
            "países mais ricos poupariam fração maior.",
            "Aplicação: países que envelhecem rápido tendem a ver a poupança doméstica cair; o tema entra nos "
            "debates sobre previdência e sobre a poupança baixa do " + rx("Brasil") + ".",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz uma implicação macro pouco lembrada da HCV, que "
                       "costuma ser estudada só no plano individual. O “sugere” protege o item; a pista é que "
                       "ambos os fatores mexem na proporção entre quem poupa e quem despoupa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a HCV, em uma economia sem crescimento populacional nem de renda, a poupança agregada "
            "líquida tende a zero.”</i> → CERTO",
            "<i>“Segundo a HCV, o envelhecimento da população tende a elevar a taxa de poupança agregada.”</i> → "
            "ERRADO (inversão: mais aposentados despoupando reduzem a poupança)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["sugere"], "dificuldade": 2,
        "comentario_fonte": ("A poupança varia com a idade (ativos poupam, inativos despoupam); assim, a "
                             "distribuição etária influencia a poupança agregada."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01001
    {
        "id": "ECO-E2-L01001-1", "fonte_ref": "E2-L01001", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONS_2023,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria de consumo de Milton Friedman, crises econômicas como a da pandemia da "
                      "Covid-19 devem provocar quedas bruscas no consumo, acompanhando o movimento da renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a teoria de consumo de Milton Friedman, crises econômicas como a da pandemia da "
                       "Covid-19 devem provocar ") + vm("quedas bruscas no consumo, acompanhando o movimento da renda")
                    + az(".")),
        "poucas": ("Na " + azb("renda permanente") + ", choque visto como " + vd("transitório") + " mexe pouco no "
                   "consumo: as famílias " + azb("suavizam") + ", usando poupança e crédito. Consumo colado à renda "
                   "corrente é a visão keynesiana."),
        "destrinchando": [
            oc("Friedman") + " (1957): C = αY<sup>P</sup>. Uma recessão que derruba a renda corrente por pouco "
            "tempo reduz pouco a renda permanente; o consumo cai bem menos que a renda, e a " + azb("poupança")
            + " absorve o choque (cai ou fica negativa).",
            "Contraste: na função keynesiana " + vd("C = C₀ + cY") + ", o consumo segue a renda corrente; uma queda "
            "de renda derruba o consumo na proporção da propensão marginal.",
            "Quando o consumo cai muito mesmo assim: se o choque é visto como " + azb("permanente") + " (perda de "
            "emprego duradoura, revisão de expectativas) ou se as famílias têm " + azb("restrição de liquidez")
            + ".",
            "O caso da Covid tem um traço peculiar: o consumo de serviços caiu por " + azb("restrições sanitárias")
            + " (não por queda de renda), e transferências como o auxílio emergencial sustentaram a renda — a "
            "poupança das famílias subiu. A frase atribui a Friedman um mecanismo (consumo acompanha renda) "
            "que não é o dele.",
        ],
        "dissecando": (cz("[troca de ator · troca de conceito]") + " Atribui a Friedman a previsão da função "
                       "keynesiana. Pista: “acompanhando o movimento da renda” descreve consumo dependente da renda "
                       "corrente — exatamente o que a renda permanente veio contestar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a HRP, uma crise vista como passageira tende a reduzir mais a poupança do que o "
            "consumo.”</i> → CERTO",
            "<i>“Segundo a HRP, uma perda de renda considerada permanente não altera o consumo.”</i> → ERRADO "
            "(choque permanente muda a renda permanente e o consumo)",
        ])],
        "reescrita": ("Segundo a teoria de consumo de Milton Friedman, crises econômicas como a da pandemia da "
                      "Covid-19 devem provocar " + hl("quedas pequenas no consumo, menores que as da renda, se "
                      "percebidas como transitórias") + "."),
        "tipo_erro": ["TROCA_ATOR", "TROCA_CONCEITO"], "moduladores": ["devem"], "dificuldade": 1,
        "comentario_fonte": ("Na HRP o consumo reage mais à renda permanente que à transitória; choques passageiros, "
                             "como a pandemia, não derrubam muito o consumo. Consumo dependente da renda corrente é "
                             "a visão keynesiana."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
