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
        "anotada": (az("Se, em determinado ano, um país registrar déficit nominal, ") + vm("consequentemente")
                    + az(", ele também registrará déficit operacional.")),
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
            "primário seja igual aos juros reais.”</i> → ERRADO (cairia: bastaria (r − g)·d)",
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
    # FIM
]
