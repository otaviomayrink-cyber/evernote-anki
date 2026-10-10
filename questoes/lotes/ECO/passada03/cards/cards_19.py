"""Cards do lote de redação 19 — ECO, passada 03 (notas 77, 78 e 79: investimento internacional,
globalização financeira e política comercial)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ied": "💼 IED e portfólio",
    "glob": "🌐 Globalização e vulnerabilidade",
    "tar": "🧾 Tarifas",
    "cota": "🚫 Cotas e barreiras não tarifárias",
    "sub": "💰 Subsídios e defesa comercial",
    "omc": "🏛️ Política comercial e OMC",
}

CMD_TPS24 = ("Em relação à macroeconomia internacional dos fluxos de bens e de capital, julgue (C ou E) o item a "
             "seguir.")

CMD_BOZAN_02 = "Acerca da teoria do investimento internacional, julgue o item a seguir."

CMD_MERC = ("O mercado doméstico de um bem internacionalmente comercializado é descrito por curvas de demanda e "
            "oferta inversas dadas, respectivamente, por P = 100 − 5Q e P = 10 + 4Q. O governo do país avalia "
            "diversas medidas de proteção comercial aos seus produtores. Com base nos conhecimentos acerca desse "
            "assunto, julgue (C ou E) o item a seguir.")

ALERTA_MERC = "banca_provavel: CEBRASPE (ano 2023 e formato C/E; órgão não informado)"

CMD_TPS25 = "Julgue o item a seguir, relativo a instrumentos de política comercial."

CMD_SUB = "Acerca dos instrumentos de política comercial, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E1-0794
    {
        "id": "ECO-E1-0794-1", "fonte_ref": "E1-0794", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": CMD_TPS24,
        "rotulo_item": "Item",
        "assertiva": ("A maioria dos países em desenvolvimento tem quase nenhum fluxo de capitais, devido à falta "
                      "de incentivos para investimento estrangeiro direto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A maioria dos países em desenvolvimento ")
                    + vm("tem quase nenhum fluxo de capitais, devido à falta de incentivos para")
                    + az(" investimento estrangeiro direto.")),
        "poucas": ("Os países em desenvolvimento recebem hoje " + vd("a maior parte do IED mundial") + " e "
                   "volumes expressivos de capital de portfólio e de empréstimos. O item contraria a evidência "
                   "e ainda inventa uma causa geral (“falta de incentivos”)."),
        "destrinchando": [
            "Dado de ordem de grandeza: segundo a " + azb("UNCTAD") + " (<i>World Investment Report 2024</i>), "
            "os fluxos de IED para economias em desenvolvimento somaram " + vd("US$ 867 bilhões em 2023") + ", "
            "cerca de " + vd("65% do total mundial") + " ⏳ (out/2026). Desde a virada dos anos 2000, mais da "
            "metade do IED global vai para fora da OCDE, com peso grande de China, Índia, Brasil, México e "
            "Sudeste Asiático.",
            "O que atrai capital para essas economias: mercado consumidor em expansão (" + azb("market-seeking")
            + "), recursos naturais (" + azb("resource-seeking") + "), mão de obra e insumos baratos para "
            "etapas de cadeias globais (" + azb("efficiency-seeking") + "), além de incentivos fiscais, "
            "privatizações e abertura regulatória.",
            "O problema dos emergentes não é a <b>ausência</b> de fluxos, e sim a sua " + azb("volatilidade")
            + ": o capital de portfólio entra em ondas de liquidez global e sai de forma abrupta em choques "
            "(" + azb("sudden stops") + " — 1982, 1997–98, 2008, março de 2020).",
            "A distribuição é desigual: poucos países concentram o grosso do IED, e os de menor renda (sobretudo "
            "na África Subsaariana) recebem pouco. Mesmo assim, “a maioria tem quase nenhum fluxo” não se "
            "sustenta.",
            vm("Regra-âncora: emergentes recebem muito capital; o risco característico deles é a volatilidade "
               "dos fluxos, não a falta deles."),
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " O item generaliza (“a maioria”, “quase "
                       "nenhum”) e cola uma causa única. Itens de economia internacional do CACD que negam um "
                       "fato estilizado conhecido (IED crescente nos emergentes) costumam ser ERRADO por "
                       "contrariar a evidência; a pista é o absoluto “quase nenhum”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os fluxos de capitais para países em desenvolvimento caracterizam-se por elevada volatilidade, "
            "sobretudo os de portfólio.”</i> → CERTO",
            "<i>“Os países de menor renda recebem a maior parte do IED destinado ao mundo em desenvolvimento.”</i> "
            "→ ERRADO (o IED concentra-se em poucos emergentes de renda média)",
        ])],
        "reescrita": ("A maioria dos países em desenvolvimento " + hl("recebe fluxos expressivos de capitais, "
                      "inclusive de") + " investimento estrangeiro direto."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["a maioria", "quase nenhum"],
        "dificuldade": 1,
        "comentario_fonte": ("Países em desenvolvimento recebem fluxos substanciais de IED e portfólio (UNCTAD, "
                             "WIR 2024: US$ 867 bi, 65% do IED global em 2023); fatores de atração: mercado, "
                             "recursos, mão de obra, incentivos; heterogeneidade entre países."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (270).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (quadro de modalidades de IED não preservado; conteúdo absorvido no "
                                   "📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0797
    {
        "id": "ECO-E1-0797-1", "fonte_ref": "E1-0797", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": CMD_TPS24,
        "rotulo_item": "Item",
        "assertiva": ("Na contabilização do investimento estrangeiro direto, incluem-se apenas os capitais que "
                      "tenham cruzado a fronteira para que se realizasse o investimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na contabilização do investimento estrangeiro direto, incluem-se ") + vm("apenas")
                    + az(" os capitais que tenham cruzado a fronteira para que se realizasse o investimento.")),
        "poucas": ("O IED também registra " + azb("lucros reinvestidos") + " e " + azb("operações "
                   "intercompanhia") + ", que não cruzam fronteira nenhuma. O critério é a relação de "
                   "investimento direto (≥ 10% do capital votante), não o trânsito do dinheiro."),
        "destrinchando": [
            "Pelo " + azb("BPM6") + " (FMI, adotado pelo " + rx("Banco Central do Brasil") + " desde 2015), "
            "investimento direto é a relação entre um investidor não residente e uma empresa residente em que "
            "ele detém " + vd("10% ou mais do capital votante") + " — sinal de interesse duradouro e influência "
            "significativa na gestão.",
            "Componentes do IED: (1) " + azb("participação no capital") + " — aportes novos, inclusive em bens "
            "(máquinas, tecnologia), conversão de dívida em capital e " + azb("lucros reinvestidos") + "; (2) "
            + azb("operações intercompanhia") + " — empréstimos entre matriz, filial e empresas irmãs.",
            "Lucro reinvestido: a filial lucra no Brasil e, em vez de remeter, retém o resultado. O BP registra "
            "como se o lucro tivesse sido remetido (débito em " + azb("renda primária") + " na conta corrente) "
            "e reaplicado (crédito em IED, participação no capital, na conta financeira). Nenhum dólar cruza a "
            "fronteira, mas o estoque de passivo externo cresce.",
            "Por isso o déficit em transações correntes gerado por lucros reinvestidos tem " + azb("financiamento "
            "automático") + " na conta financeira: os dois lançamentos nascem juntos.",
            vm("Regra-âncora: o que define IED é a relação de controle/influência (≥ 10%), não o "
               "movimento físico de recursos pela fronteira."),
        ],
        "dissecando": (cz("[restrição indevida]") + " O “apenas” transforma um caso típico (aporte vindo do "
                       "exterior) em requisito. 🔥 Lucros reinvestidos e intercompanhia são a pegadinha clássica "
                       "de IED em prova: sempre contam, mesmo sem entrada de divisas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os lucros reinvestidos por filiais de empresas estrangeiras são registrados simultaneamente na "
            "conta de renda primária e na conta financeira.”</i> → CERTO",
            "<i>“A aquisição, por não residente, de 5% das ações de uma empresa brasileira constitui investimento "
            "direto.”</i> → ERRADO (abaixo de 10% é investimento em carteira)",
        ])],
        "reescrita": ("Na contabilização do investimento estrangeiro direto, incluem-se " + hl("não apenas")
                      + " os capitais que tenham cruzado a fronteira para que se realizasse o investimento"
                      + hl(", mas também os lucros reinvestidos e as operações intercompanhia") + "."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("IED inclui lucros reinvestidos e operações intercompanhia, que não cruzam a "
                             "fronteira; lucros reinvestidos afetam renda primária e IED (financiamento "
                             "automático); critério de 10% do capital votante (BPM6)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (274).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"},
                          {"ref": "image (273).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0931
    {
        "id": "ECO-E1-0931-1", "fonte_ref": "E1-0931", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": True,
        "comando": "Com referência aos dados de um balanço de pagamentos, julgue (C ou E) o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("A aquisição de ações no mercado secundário e o reinvestimento de lucros não contribuem para "
                      "o aumento do estoque de capital da economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A aquisição de ações no <u>mercado secundário</u> e o <u>reinvestimento de lucros</u> não "
                      "contribuem para o aumento do estoque de capital da economia."),
        "poucas": ("Comprar ação já emitida só " + azb("troca o titular") + " de um capital que já existe; e o "
                   "lucro reinvestido, como lançamento do BP, é recurso que já estava na economia. Nenhum dos "
                   "dois, por si, cria máquina ou fábrica nova."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o gabarito CERTO vale para os <b>lançamentos</b> do balanço de pagamentos. Mas, se a "
                          "filial usa os lucros retidos para comprar equipamentos ou ampliar a planta, há "
                          + azb("formação bruta de capital fixo") + " financiada por esse reinvestimento — e o "
                          "estoque de capital cresce. Como o item não diz o destino do lucro reinvestido, a "
                          "resposta ERRADO também seria defensável para a segunda metade da frase; a primeira "
                          "(ações no secundário) é inequivocamente certa.")],
        "destrinchando": [
            azb("Mercado primário") + " × " + azb("secundário") + ": no primário a empresa emite ações e "
            "recebe os recursos (pode investir com eles); no secundário um investidor vende a outro, e a empresa "
            "não recebe nada. Se compro de Fulano uma ação da Petrobras, a Petrobras não investe um real a mais.",
            "No BP, a compra de ações por não residente entra na conta financeira: " + azb("investimento em "
            "carteira") + " se a participação for inferior a " + vd("10%") + " do capital votante; "
            + azb("investimento direto") + " se atingir esse limiar. Em qualquer caso, é transferência de "
            "propriedade de um ativo existente (e, se o vendedor for residente, há só troca de credores externos "
            "por internos).",
            azb("Lucro reinvestido") + ": a filial retém o lucro em vez de remetê-lo. O BP registra um débito em "
            "renda primária (como se o lucro saísse) e um crédito de igual valor em IED, participação no capital "
            "(como se voltasse). É um par de lançamentos contábeis, sem entrada de recursos novos.",
            "Estoque de capital da economia = capital físico (máquinas, edificações, infraestrutura). Ele só "
            "cresce com " + azb("investimento líquido") + " (FBCF acima da depreciação), qualquer que seja a "
            "fonte de financiamento — poupança doméstica ou externa.",
            "Distinção útil: a " + azb("conta capital") + " do BP (transferências de capital, ativos não "
            "financeiros não produzidos, como marcas e patentes) não tem relação com o “estoque de capital” "
            "da macroeconomia.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " O item parece falso porque ambas as operações aparecem como "
                       "“investimento” no BP; a banca explora a confusão entre investimento financeiro (troca de "
                       "ativos) e investimento econômico (formação de capital físico). A ressalva está no "
                       "reinvestimento, cujo uso real o item não especifica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A subscrição de ações recém-emitidas por uma empresa, quando os recursos financiam a compra de "
            "máquinas, contribui para o aumento do estoque de capital da economia.”</i> → CERTO",
            "<i>“A aquisição de ações no mercado secundário por não residentes não é registrada no balanço de "
            "pagamentos.”</i> → ERRADO (é registrada na conta financeira)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Ações no secundário só trocam de dono; lucro reinvestido é lançado em IED com "
                             "contrapartida em renda primária, sem novo capital. Um dos comentários contesta: o "
                             "reinvestimento pode ampliar a capacidade produtiva."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (306).png", "tipo_fonte": "TABELA", "lado": "frente",
                           "acao": "cortada (tabela de BP não preservada; dispensável para julgar o item)"},
                          {"ref": "image (309).png, image (310).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagens não preservadas)"}],
        "alertas": ["contestavel: reinvestimento de lucros aplicado em ampliação da planta eleva o estoque de "
                    "capital; o gabarito CERTO só vale para o lançamento contábil",
                    "texto_parcial: a frente trazia tabela de balanço de pagamentos (image (306).png), não "
                    "preservada; o item se julga sem ela e o comando foi neutralizado",
                    "banca_provavel: CEBRASPE (formato “julgue (C ou E)”; órgão não informado)"],
    },
    # ------------------------------------------------------------------ E2-L00187
    {
        "id": "ECO-E2-L00187-1", "fonte_ref": "E2-L00187", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("São fatores que incentivam o investimento externo direto (IED): elevada liquidez do mercado "
                      "internacional, processo de desregulamentação das economias nacionais e políticas "
                      "estratégicas de empresas multinacionais (ETN)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("São fatores que incentivam o investimento externo direto (IED): <u>elevada liquidez do "
                      "mercado internacional</u>, processo de <u>desregulamentação</u> das economias nacionais e "
                      "<u>políticas estratégicas</u> de empresas multinacionais (ETN)."),
        "poucas": ("Os três fatores combinam o nível " + azb("sistêmico") + " (liquidez global), o "
                   + azb("institucional") + " (desregulamentação dos países receptores) e o "
                   + azb("microeconômico") + " (estratégia das transnacionais)."),
        "destrinchando": [
            azb("Liquidez internacional") + ": juros baixos nos centros e crédito farto barateiam fusões, "
            "aquisições e projetos greenfield. As ondas de IED dos anos 1990 e de 2005–2007 coincidiram com "
            "liquidez abundante; as retrações (2001, 2009, 2020) com choques de liquidez.",
            azb("Desregulamentação e abertura") + ": privatizações, fim de restrições setoriais ao capital "
            "estrangeiro, liberdade de remessa de lucros, acordos de proteção de investimentos. No "
            + rx("Brasil") + ", a Emenda Constitucional nº 6/1995 extinguiu a distinção entre empresa brasileira "
            "e empresa brasileira de capital nacional, e as privatizações dos anos 1990 atraíram forte IED.",
            azb("Estratégia das ETN") + ": acesso a mercados (" + azb("market-seeking") + "), recursos naturais, "
            "eficiência (fragmentação em cadeias globais de valor) e ativos estratégicos (marcas, tecnologia). "
            "No " + azb("paradigma eclético OLI") + " de " + oc("John Dunning") + ", a firma investe no exterior "
            "quando reúne vantagens de propriedade (O), de localização (L) e de internalização (I).",
            "Fatores que <b>desestimulam</b> o IED: instabilidade macroeconômica e cambial, insegurança jurídica, "
            "risco de expropriação, carga tributária complexa, infraestrutura precária.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Lista de determinantes extraída da literatura de economia "
                       "internacional, sem modulador suspeito. Em listas assim, a banca costuma trocar um fator "
                       "pelo seu oposto (“regulamentação mais rígida”) ou atribuir ao IED o determinante típico "
                       "do portfólio (diferencial de juros de curto prazo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“São fatores que incentivam o IED a ampliação de controles sobre remessas de lucros e a "
            "restrição setorial ao capital estrangeiro.”</i> → ERRADO (inversão: são desincentivos)",
            "<i>“O principal determinante do IED é o diferencial de curto prazo entre juros domésticos e "
            "internacionais.”</i> → ERRADO (troca de conceito: é determinante do portfólio)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("IED responde a condições sistêmicas (liquidez), institucionais (desregulamentação) e "
                             "microeconômicas (estratégias de ETN: internalização, mercados, eficiência)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00188
    {
        "id": "ECO-E2-L00188-1", "fonte_ref": "E2-L00188", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("IED ocorrem quando há compras de ações ou cotas de empresas no exterior – no montante mínimo "
                      "de 50% do capital votante - com o propósito de exercer o controle sobre as decisões e "
                      "condução da organização."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("IED ocorrem quando há compras de ações ou cotas de empresas no exterior – no montante "
                       "mínimo de ") + vm("50%") + az(" do capital votante - com o propósito de exercer ")
                    + vm("o controle") + az(" sobre as decisões e condução da organização.")),
        "poucas": ("O limiar estatístico do IED é " + vd("10% do capital votante") + ", que indica "
                   + azb("influência significativa") + " e interesse duradouro — não necessariamente controle. "
                   "50% é o patamar de controle, não o de IED."),
        "destrinchando": [
            "Pelo " + azb("BPM6") + " (FMI) e pela " + azb("Definição de Referência da OCDE") + ", há relação "
            "de investimento direto quando o investidor detém " + vd("≥ 10%") + " do poder de voto. Abaixo "
            "disso, a compra de ações é " + azb("investimento em carteira") + " (portfólio).",
            "Graus da relação: " + vd("10% a 50%") + " → empresa " + azb("associada") + " (influência "
            "significativa); " + vd("acima de 50%") + " → " + azb("subsidiária") + " (controle). As duas são "
            "IED. Filial sem personalidade jurídica própria também.",
            "O que o critério capta é o " + azb("interesse duradouro") + ": o investidor quer participar da "
            "gestão, não apenas ganhar com dividendos ou valorização — diferença essencial em relação ao "
            "portfólio, mais líquido e volátil.",
            "Além da compra de ações, o IED inclui instalação de novas plantas (" + azb("greenfield") + "), "
            "fusões e aquisições (" + azb("brownfield") + "), lucros reinvestidos e empréstimos intercompanhia.",
            vm("Regra-âncora: IED começa em 10% do capital votante; controle (> 50%) é só uma das situações "
               "possíveis."),
        ],
        "dissecando": (cz("[dado alterado · troca de conceito]") + " O item troca o limiar (10% → 50%) e, "
                       "coerentemente com o número inflado, exige “controle”, quando basta influência "
                       "significativa. 🔥 O “10%” é o número mais cobrado de IED."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A aquisição, por não residente, de 15% do capital votante de uma empresa residente é "
            "classificada como investimento direto.”</i> → CERTO",
            "<i>“Participações inferiores a 10% do capital votante são registradas como investimento direto "
            "quando o investidor for pessoa jurídica.”</i> → ERRADO (critério não depende da natureza do "
            "investidor)",
        ])],
        "reescrita": ("IED ocorrem quando há compras de ações ou cotas de empresas no exterior – no montante mínimo "
                      "de " + hl("10%") + " do capital votante - com o propósito de exercer "
                      + hl("influência significativa") + " sobre as decisões e condução da organização."),
        "tipo_erro": ["DADO_ALTERADO", "TROCA_CONCEITO"], "moduladores": ["mínimo"], "dificuldade": 1,
        "comentario_fonte": ("IED é definido por interesse duradouro e influência significativa; critério usual "
                             "de 10% do capital votante; 50% é excessivo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00189
    {
        "id": "ECO-E2-L00189-1", "fonte_ref": "E2-L00189", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("São determinantes do investimento externo em portfolio: diferencial de taxas de juros para o "
                      "capital de empréstimo e diferencial de taxas de rentabilidade para o capital de risco."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("São determinantes do investimento externo em portfolio: diferencial de <u>taxas de "
                      "juros</u> para o capital de <u>empréstimo</u> e diferencial de <u>taxas de "
                      "rentabilidade</u> para o capital de <u>risco</u>."),
        "poucas": ("O portfólio busca " + azb("retorno financeiro ajustado ao risco") + ", sem controle da "
                   "empresa: em títulos de dívida, o motor é o diferencial de juros; em ações, o diferencial "
                   "de rentabilidade esperada."),
        "destrinchando": [
            azb("Investimento em carteira") + " = compra de títulos (renda fixa) e de ações abaixo de "
            + vd("10%") + " do capital votante. O investidor quer rendimento e liquidez, não participar da "
            "gestão.",
            azb("Capital de empréstimo") + " (bônus, notes, títulos públicos): o retorno é o juro. Aplica-se "
            "onde o juro, descontado o risco de crédito e o risco cambial, é maior — daí o peso do "
            + azb("diferencial de juros") + " e do prêmio de risco-país.",
            azb("Capital de risco") + " (ações): o retorno é dividendo mais valorização. Pesa o diferencial de "
            + azb("rentabilidade esperada") + " das empresas e das bolsas, ajustado ao risco.",
            "Nos dois casos entra a " + azb("expectativa cambial") + ": um ganho de juros de 5 pontos some se a "
            "moeda local se desvalorizar 5%. Por isso o portfólio é sensível a mudanças de humor e reage "
            "rápido a choques.",
            "Contraste: IED é guiado por estratégia produtiva de longo prazo (mercado, recursos, eficiência); "
            "capital especulativo de curtíssimo prazo, sobretudo pela expectativa de variação do câmbio.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item reproduz a classificação de manual (empréstimo → "
                       "juros; risco → rentabilidade). A banca costuma inverter os pares ou atribuir esses "
                       "determinantes ao IED."),
        "modulos": [("😈 Para dificultar", [
            "<i>“São determinantes do investimento em portfólio: diferencial de taxas de rentabilidade para o "
            "capital de empréstimo e diferencial de juros para o capital de risco.”</i> → ERRADO (pares "
            "invertidos)",
            "<i>“O investimento em portfólio é motivado pelo controle das decisões da empresa investida.”</i> "
            "→ ERRADO (isso caracteriza o IED)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Portfólio é guiado por retorno ajustado ao risco: juros e prêmio de risco nos "
                             "títulos; rentabilidade esperada nas ações; sem controle, mais sensível à "
                             "arbitragem."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00190
    {
        "id": "ECO-E2-L00190-1", "fonte_ref": "E2-L00190", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_02,
        "rotulo_item": "Item",
        "assertiva": ("Capitais especulativos possuem como determinantes as expectativas em relação ao diferencial "
                      "de taxas de juros doméstica e internacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Capitais especulativos possuem como determinantes as expectativas em relação ")
                    + vm("ao diferencial de taxas de juros doméstica e internacional") + az(".")),
        "poucas": ("O motor do capital " + azb("especulativo") + " é a expectativa de " + vd("variação "
                   "cambial") + " (desvalorização ou valorização da moeda). Diferencial de juros é o "
                   "determinante típico do " + azb("portfólio de empréstimo") + "."),
        "destrinchando": [
            "Na tipologia usual dos fluxos de capitais: " + azb("IED") + " → estratégia produtiva de longo "
            "prazo; " + azb("portfólio") + " → diferencial de juros (títulos) e de rentabilidade (ações); "
            + azb("capital especulativo") + " → expectativa de variação da taxa de câmbio.",
            "O especulador aposta no preço da moeda: se espera desvalorização do real, sai antes (ou vende real "
            "a termo); se espera valorização, entra para ganhar a apreciação. Movimentos assim são de "
            "curtíssimo prazo e altamente voláteis.",
            "A ponte entre juros e câmbio é a " + azb("paridade descoberta de juros") + ": i = i* + "
            "E(Δe)/e + prêmio de risco. Um diferencial de juros alto pode ser anulado por desvalorização "
            "esperada — por isso, para o especulador, o que decide é a expectativa cambial.",
            "Ataques especulativos contra regimes de câmbio fixo (libra em 1992, Ásia em 1997, " + rx("real")
            + " em 1998–99) ilustram: juros altíssimos não seguraram o capital quando a expectativa de "
            "desvalorização se generalizou.",
            vm("Regra-âncora: especulativo ↔ expectativa cambial; portfólio ↔ diferencial de juros e de "
               "rentabilidade; IED ↔ estratégia produtiva."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item transfere ao capital especulativo o determinante "
                       "do portfólio de empréstimo. A pegadinha funciona porque juros e câmbio andam juntos "
                       "(paridade de juros); mas, na tipologia cobrada, o especulativo é definido pela "
                       "expectativa cambial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Capitais especulativos possuem como determinante a expectativa de variação da taxa de "
            "câmbio.”</i> → CERTO",
            "<i>“Capitais especulativos caracterizam-se pela baixa sensibilidade a mudanças nas expectativas "
            "dos agentes.”</i> → ERRADO (inversão: são os mais sensíveis)",
        ])],
        "reescrita": ("Capitais especulativos possuem como determinantes as expectativas em relação "
                      + hl("à variação da taxa de câmbio") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Capitais especulativos dependem sobretudo de expectativas de câmbio e risco-país, "
                             "além do diferencial de juros (paridade descoberta)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00227
    {
        "id": "ECO-E2-L00227-1", "fonte_ref": "E2-L00227", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Julgue a afirmativa a seguir sobre investimentos internacionais e fluxos de capitais, "
                    "considerando o entendimento técnico de paridades de juros e riscos associados."),
        "rotulo_item": "Item",
        "assertiva": ("A internacionalização da produção em mercados imperfeitos ocorre quando existem vantagens "
                      "específicas à propriedade, permitindo que certos agentes económicos obtenham benefícios "
                      "únicos que não seriam possíveis em mercados perfeitos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A internacionalização da produção em <u>mercados imperfeitos</u> ocorre quando existem "
                      "<u>vantagens específicas à propriedade</u>, permitindo que certos agentes económicos "
                      "obtenham benefícios únicos que não seriam possíveis em mercados perfeitos."),
        "poucas": ("É a tese de " + oc("Hymer") + " e do " + azb("paradigma OLI") + ": em concorrência perfeita "
                   "não haveria multinacionais; a firma só produz no exterior se tiver uma " + azb("vantagem "
                   "de propriedade") + " (tecnologia, marca, gestão) que compense o custo de ser estrangeira."),
        "destrinchando": [
            oc("Stephen Hymer") + " (tese de doutorado no MIT, 1960, publicada em 1976) rompeu com a explicação "
            "do IED como simples arbitragem de juros: produzir em outro país tem custos (desconhecer leis, "
            "idioma, consumidores, redes locais). Só compensa se a firma tiver algo que as locais não têm.",
            "Essas " + azb("vantagens específicas à propriedade") + " (O, de <i>ownership</i>) — patentes, "
            "know-how, marcas, escala, acesso a capital, capacidade gerencial — só existem porque os mercados "
            "são " + azb("imperfeitos") + ": em concorrência perfeita, com informação e tecnologia livres, "
            "nenhuma firma teria vantagem duradoura.",
            "O " + azb("paradigma eclético") + " de " + oc("John Dunning") + " soma mais duas condições: "
            + azb("localização") + " (L: por que produzir naquele país — mercado, recursos, custos, barreiras "
            "comerciais) e " + azb("internalização") + " (I: por que explorar a vantagem dentro da própria "
            "firma, em vez de licenciar ou exportar — custos de transação, risco de perder o know-how).",
            "A teoria da internalização (" + oc("Buckley e Casson") + ", 1976) aprofunda o I: a multinacional "
            "substitui mercados imperfeitos de conhecimento e insumos por hierarquia interna.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Reproduz o núcleo da teoria de Hymer/Dunning. A banca costuma "
                       "inverter o pressuposto (“em mercados perfeitos”) ou dizer que a vantagem de propriedade "
                       "basta sozinha, esquecendo L e I."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em mercados perfeitamente competitivos, as vantagens de propriedade explicam a expansão das "
            "empresas multinacionais.”</i> → ERRADO (inversão: são as imperfeições que criam as vantagens)",
            "<i>“No paradigma OLI, a existência de vantagens de propriedade é condição suficiente para o "
            "IED.”</i> → ERRADO (restrição indevida: são necessárias também L e I)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Vantagens de propriedade em mercados imperfeitos (tecnologia, gestão, logística) "
                             "sustentam a internacionalização; em concorrência perfeita não haveria diferenciais."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00255
    {
        "id": "ECO-E3-L00255-1", "fonte_ref": "E3-L00255", "destino": "77", "subtema": H2["ied"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": "No que diz respeito à teoria do comércio internacional, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O processo decisório de uma firma entre verticalizar a produção em mais de um país ou "
                      "subcontratar terceiros é mais conveniente em setores cujos processos de produção são "
                      "contínuos. A decisão pela subcontratação dependerá da qualidade do serviço e da existência "
                      "de barreiras à operação nos demais países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O processo decisório de uma firma entre verticalizar a produção em mais de um país ou "
                       "subcontratar terceiros é mais conveniente em setores cujos processos de produção são ")
                    + vm("contínuos") + az(". A decisão pela subcontratação dependerá da qualidade do serviço e "
                                           "da existência de barreiras à operação nos demais países.")),
        "poucas": ("Espalhar etapas por vários países (por filial ou por terceiro) exige produção "
                   + azb("fragmentável") + " — processos " + vd("discretos") + ", montados a partir de "
                   "componentes. Processos " + azb("contínuos") + " (refino, siderurgia, química) ficam "
                   "concentrados num só local."),
        "destrinchando": [
            azb("Processo discreto") + ": o produto é montado a partir de peças fabricáveis separadamente "
            "(automóveis, eletrônicos, vestuário). Cada etapa pode ir para o país com vantagem naquela tarefa: "
            "projeto nos EUA, chip em Taiwan, tela na Coreia, montagem na China — a lógica das "
            + azb("cadeias globais de valor") + ".",
            azb("Processo contínuo") + ": fluxo ininterrupto, etapas física ou quimicamente integradas, medidas "
            "em volume ou peso (refino de petróleo, aço, celulose, petroquímica). Não se para o alto-forno para "
            "mandar o aço líquido a outro país; a produção tende a ser replicada inteira perto de matérias-primas "
            "ou mercados.",
            "Só depois de saber que a etapa é separável vem o dilema " + azb("make or buy") + ": "
            + azb("verticalizar") + " (IED vertical, filial própria — " + azb("captive offshoring") + ") ou "
            + azb("subcontratar") + " (" + azb("offshore outsourcing") + ", como a Nike com fábricas "
            "independentes no Vietnã). A qualidade do fornecedor e as barreiras locais pesam nessa escolha.",
            "A teoria dos " + azb("custos de transação") + " (" + oc("Coase") + "; " + oc("Williamson") + ") "
            "aprofunda: alta especificidade de ativos, incerteza contratual e risco de vazamento tecnológico "
            "(hold-up) empurram para a internalização; insumo padronizado e contrato fácil de fiscalizar, para "
            "a terceirização.",
            vm("Regra-âncora: fragmentar a produção entre países (com filial ou terceiro) pressupõe processo "
               "discreto; processo contínuo concentra a produção."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o tipo de processo que permite a fragmentação: o item diz "
                       "“contínuos” onde a lógica pede “discretos”. A segunda frase é verdadeira, mas simples "
                       "demais — serve de isca para quem julga só o final. Pista: pense se dá para separar as "
                       "etapas fisicamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A fragmentação internacional da produção é mais frequente em setores de manufatura discreta, "
            "como eletrônicos e automóveis.”</i> → CERTO",
            "<i>“Ativos altamente específicos e risco de apropriação de tecnologia favorecem a "
            "subcontratação.”</i> → ERRADO (inversão: favorecem a verticalização)",
        ])],
        "reescrita": ("O processo decisório de uma firma entre verticalizar a produção em mais de um país ou "
                      "subcontratar terceiros é mais conveniente em setores cujos processos de produção são "
                      + hl("discretos (fragmentáveis em etapas)") + ". A decisão pela subcontratação dependerá da "
                      "qualidade do serviço e da existência de barreiras à operação nos demais países."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["mais conveniente"], "dificuldade": 2,
        "comentario_fonte": ("Professora: verticalização ou terceirização são mais fáceis quando o processo pode "
                             "ser fragmentado; em processo contínuo, a horizontalização é mais efetiva. "
                             "Comentários de IA: processos discretos × contínuos; custos de transação "
                             "(Coase, Williamson), hold-up, offshoring × outsourcing."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 359", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (gabarito comentado da professora no 📖)"},
                          {"ref": "IMAGEM 360", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (processo discreto × contínuo; ativo específico × padronizado)"},
                          {"ref": "IMAGEM 361", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (fatores da decisão make or buy)"}],
        "alertas": ["texto_corrigido: “demais país” → “demais países” na assertiva"],
    },
    # ------------------------------------------------------------------ E3-L00256
    {
        "id": "ECO-E3-L00256-1", "fonte_ref": "E3-L00256", "destino": "77", "subtema": H2["ied"],
        "tipo": "DISC", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": "Responda à questão a seguir, sobre estratégias de internacionalização das empresas.",
        "rotulo_item": "Questão",
        "assertiva": ("Liste e explique as diferentes estratégias de internacionalização, incluindo "
                      "multinacionais, IDE e terceirização, além de conceitos como horizontalização e "
                      "verticalização e processos contínuos e discretos."),
        "gabarito": "RESPOSTA", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Multinacional: empresa com filiais em que detém 10% ou mais do capital (abaixo disso, "
                      "investimento em carteira). IDE horizontal: a filial replica a produção da matriz para "
                      "atender o mercado local (busca de mercado, salto de tarifas). IDE vertical: a matriz "
                      "fatia a cadeia e distribui etapas entre países conforme custos (busca de eficiência). "
                      "Terceirização estrangeira: contratar empresa independente no exterior para uma etapa — "
                      "alternativa ao IDE vertical, com menos investimento e menos controle. A fragmentação "
                      "pressupõe processo discreto (peças montáveis); o contínuo (refino, aço) concentra a "
                      "produção."),
        "poucas": ("A firma escolhe entre " + azb("exportar") + ", " + azb("licenciar") + ", "
                   + azb("joint venture") + ", " + azb("IDE") + " (horizontal ou vertical) e "
                   + azb("terceirizar") + " no exterior, trocando controle por investimento e risco."),
        "destrinchando": [
            azb("Escala de comprometimento") + ": exportação (baixo risco e controle) → contratos de "
            "licenciamento e franquia (royalties; risco de perder know-how) → " + azb("joint venture") + " "
            "(controle e risco compartilhados com sócio local) → " + azb("IDE") + " (greenfield ou aquisição; "
            "controle total, investimento alto). O modelo de " + azb("Uppsala") + " (" + oc("Johanson e "
            "Vahlne") + ") descreve esse avanço gradual por aprendizado.",
            azb("IDE horizontal") + " (" + azb("market-seeking") + "): ocorre quando os custos de comércio "
            "(frete, tarifas) são altos e o mercado externo é grande; tende a se dar entre países semelhantes "
            "em renda e consumo e a <b>substituir</b> exportações. Exemplo: montadora que abre fábrica no "
            + rx("Brasil") + " para vender no Mercosul e escapar da TEC.",
            azb("IDE vertical") + " (" + azb("efficiency-seeking") + "): ocorre quando há diferença de custo de "
            "fatores; cada etapa vai para o país com vantagem comparativa naquela tarefa e o comércio "
            "intrafirma <b>aumenta</b>. A filial que faz as duas coisas configura o " + azb("IDE complexo") + ".",
            azb("Offshoring") + " (mudança de país) × " + azb("outsourcing") + " (mudança de dono): filial "
            "própria no exterior é " + azb("captive offshoring") + " (IDE); fornecedor independente no exterior "
            "é " + azb("offshore outsourcing") + ". A escolha segue " + oc("Williamson") + " (custos de "
            "transação): ativo específico e tecnologia sensível → internalizar; insumo padronizado → terceirizar. "
            "O " + azb("paradigma OLI") + " de " + oc("Dunning") + " resume: propriedade, localização, "
            "internalização.",
            azb("Processo discreto") + " (carros, smartphones, contados em unidades) permite fragmentar e "
            "distribuir etapas; " + azb("processo contínuo") + " (químicos, aço, combustíveis, medidos em volume) "
            "é pouco flexível e fica perto de matérias-primas ou de logística especializada. Atenção à dupla "
            "acepção: em IDE, “horizontal” é replicar a produção; em organização industrial, “horizontalizar” "
            "é desverticalizar (terceirizar etapas).",
        ],
        "dissecando": (cz("[discursiva curta]") + " Em C/E, esses conceitos viram itens como “IDE horizontal "
                       "tende a substituir exportações” (CERTO), “IDE vertical reduz o comércio intrafirma” "
                       "(ERRADO) ou “fragmentação é típica de processos contínuos” (ERRADO)."),
        "modulos": [("🃏 Carta na manga", [
            "Para discursiva sobre política de atração de investimentos: IED horizontal responde a mercado "
            "interno e barreiras comerciais (tende a substituir importações); IED vertical responde a custos "
            "e integração em cadeias globais (eleva exportações e importações de insumos). Abrir a economia "
            "sem política de inserção em cadeias tende a atrair o primeiro tipo e perder o segundo."])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Slides da professora: subsidiária/matriz (10%), IDE horizontal × vertical × "
                             "complexo, terceirização estrangeira, integração vertical × terceirização; "
                             "comentários de IA: tipologias de multinacional (Bartlett e Ghoshal), OLI, "
                             "Uppsala, custos de transação, GVC (Gereffi), offshoring × outsourcing, processos "
                             "discretos × contínuos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 362-366", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (slides da professora no 📖)"},
                          {"ref": "IMAGEM 367", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (quadro de estratégias de entrada no 📖)"},
                          {"ref": "IMAGEM 368", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (manufatura discreta × contínua no 📖)"}],
        "alertas": ["nota_redacao: a frente era um pedido de estudo informal (“Liste e explique… etc.”); o "
                    "enunciado foi organizado sem alterar o pedido"],
    },
    # ------------------------------------------------------------------ E1-0372
    {
        "id": "ECO-E1-0372-1", "fonte_ref": "E1-0372", "destino": "78", "subtema": H2["glob"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Acerca dos fluxos internacionais de capitais, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Embora sejam determinantes expressivos do desempenho econômico dos países, as tendências, "
                      "flutuações e composição dos fluxos internacionais de capitais têm baixíssimo impacto nas "
                      "diretrizes ou escolhas de política econômica em uma economia aberta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Embora sejam determinantes expressivos do desempenho econômico dos países, as tendências, "
                       "flutuações e composição dos fluxos internacionais de capitais têm ") + vm("baixíssimo")
                    + az(" impacto nas diretrizes ou escolhas de política econômica em uma economia aberta.")),
        "poucas": ("Em economia aberta, os fluxos de capitais " + azb("condicionam") + " a política econômica: "
                   "afetam câmbio, juros, inflação, reservas e custo da dívida, e restringem a autonomia "
                   "monetária (" + azb("trilema") + ")."),
        "destrinchando": [
            "Contabilmente, o fluxo de capital é a " + azb("poupança externa") + " que financia o déficit em "
            "transações correntes: S + (M − X) = I. Quando o fluxo seca, o país precisa gerar superávit "
            "externo à força — com desvalorização e recessão.",
            azb("Trilema") + " (trindade impossível, a partir de " + oc("Mundell-Fleming") + "): não se têm, ao "
            "mesmo tempo, câmbio fixo, livre mobilidade de capitais e política monetária autônoma. Com capital "
            "livre, ou o câmbio flutua (e os fluxos movem o câmbio) ou os juros ficam presos aos externos.",
            "A " + azb("composição") + " importa: IED é estável; portfólio e dívida de curto prazo são voláteis "
            "e sujeitos a " + azb("sudden stops") + ". Muita dívida de curto prazo em moeda estrangeira "
            "aumenta a vulnerabilidade e exige mais reservas.",
            "Na prática, os governos reagem aos fluxos: juros altos para atrair ou reter capital, intervenções "
            "e swaps cambiais, acúmulo de reservas, medidas macroprudenciais, controles de capital (o "
            + rx("IOF sobre ingressos de 2009–2013, no Brasil") + "), comunicação com os mercados. O "
            + azb("fear of floating") + " (" + oc("Calvo e Reinhart") + ") mostra países que dizem flutuar mas "
            "intervêm por medo dos efeitos cambiais.",
            vm("Regra-âncora: com mobilidade de capitais, os fluxos externos restringem as escolhas de "
               "política monetária, cambial e fiscal."),
        ],
        "dissecando": (cz("[contradição · juízo indevido]") + " A concessiva inicial é verdadeira e prepara a "
                       "armadilha: se os fluxos determinam o desempenho econômico, não podem ser irrelevantes "
                       "para a política econômica. O superlativo “baixíssimo” entrega o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com livre mobilidade de capitais e câmbio fixo, a política monetária perde autonomia.”</i> → "
            "CERTO",
            "<i>“A composição dos fluxos de capitais é irrelevante para a vulnerabilidade externa, que depende "
            "apenas do volume total.”</i> → ERRADO (dívida de curto prazo é mais volátil que IED)",
        ])],
        "reescrita": ("Embora sejam determinantes expressivos do desempenho econômico dos países, as tendências, "
                      "flutuações e composição dos fluxos internacionais de capitais têm " + hl("elevado")
                      + " impacto nas diretrizes ou escolhas de política econômica em uma economia aberta."),
        "tipo_erro": ["CONTRADICAO", "JUIZO_INDEVIDO"], "moduladores": ["baixíssimo"], "dificuldade": 1,
        "comentario_fonte": ("Fluxos de capital proveem poupança externa e determinam câmbio e investimento; "
                             "autoridades se comunicam com os mercados e mantêm indicadores atraentes. Duplicata: "
                             "trilema de Mundell-Fleming, sudden stop, reservas, fear of floating."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 401 (duplicata E3-L00292)", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (repetia o enunciado)"}],
        "alertas": ["duplicata: comentário de E3-L00292 (mesmo item, “Questão 65 — Item 3”) fundido",
                    "banca_provavel: CEBRASPE, IRBr/CACD/2018 (marca ⌚ e numeração “Questão 65” na duplicata; "
                    "não confirmada)"],
    },
    # ------------------------------------------------------------------ E1-0373
    {
        "id": "ECO-E1-0373-1", "fonte_ref": "E1-0373", "destino": "78", "subtema": H2["glob"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Acerca dos fluxos internacionais de capitais, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Um dos problemas mais preocupantes do movimento internacional de capital ocorre quando a "
                      "saída dos fluxos se dá repentinamente, pressionando o câmbio e colocando em risco a "
                      "manutenção da estabilidade financeira. Em países que fizeram a liberalização financeira "
                      "com implementação de políticas para limitar o excesso de volatilidade, as regulações "
                      "prudenciais desempenham papel fundamental e preventivo na contenção desses riscos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um dos problemas mais preocupantes do movimento internacional de capital ocorre quando a "
                      "saída dos fluxos se dá <u>repentinamente</u>, pressionando o câmbio e colocando em risco a "
                      "manutenção da estabilidade financeira. Em países que fizeram a liberalização financeira "
                      "com implementação de políticas para limitar o excesso de volatilidade, as "
                      "<u>regulações prudenciais</u> desempenham papel fundamental e <u>preventivo</u> na "
                      "contenção desses riscos."),
        "poucas": ("A " + azb("parada súbita") + " (sudden stop) deprecia o câmbio e ameaça bancos e empresas "
                   "endividados em moeda estrangeira; a " + azb("regulação prudencial") + " reduz o acúmulo de "
                   "riscos no boom e amortece a reversão."),
        "destrinchando": [
            azb("Sudden stop") + " (" + oc("Guillermo Calvo") + "): interrupção abrupta dos ingressos, ou fuga, "
            "após uma onda de entrada. O câmbio dispara; quem tem dívida em dólar e receita em moeda local "
            "(" + azb("descasamento cambial") + ") vê o passivo crescer de uma vez; o crédito seca; bancos e "
            "empresas quebram.",
            "Canais para a estabilidade financeira: inflação pela desvalorização, balanços com dívida em moeda "
            "estrangeira, queda do preço dos ativos, aperto de liquidez. Exemplos: México (1994–95), Ásia "
            "(1997), Rússia (1998), " + rx("Brasil (1999)") + ", Argentina (2001).",
            azb("Regulação prudencial e macroprudencial") + ": limites à posição cambial dos bancos, "
            "requerimentos de capital e de liquidez (Basileia), compulsórios sobre captações externas, "
            "restrições ao descasamento, colchões contracíclicos. Atua <b>antes</b> da crise, contendo o "
            "endividamento arriscado nos anos de bonança.",
            "Casos citados: o " + azb("encaje") + " chileno dos anos 1990 (depósito não remunerado sobre "
            "ingressos de curto prazo); no " + rx("Brasil") + ", IOF sobre ingressos e compulsório sobre "
            "posições vendidas em câmbio dos bancos (2009–2011), além de swaps cambiais e reservas elevadas. "
            "Em 2012 o " + azb("FMI") + " passou a aceitar medidas de gestão de fluxos de capital em certas "
            "circunstâncias (<i>institutional view</i>).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item longo e descritivo, com moduladores moderados (“um dos "
                       "problemas”, “papel fundamental”). A banca costuma errar trocando “preventivo” por "
                       "“exclusivamente corretivo” ou dizendo que a liberalização eliminou o risco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma vez concluída a liberalização financeira, as regulações prudenciais tornam-se "
            "dispensáveis, pois o mercado disciplina a volatilidade.”</i> → ERRADO (juízo indevido)",
            "<i>“Descasamentos cambiais em balanços de bancos e empresas amplificam os efeitos de uma parada "
            "súbita de capitais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["um dos", "fundamental"], "dificuldade": 1,
        "comentario_fonte": ("Fuga súbita de capitais pressiona o câmbio e afeta a estabilidade financeira "
                             "(preços, contratos em moeda estrangeira); swaps cambiais; duplicata: sudden stops "
                             "(Calvo), macroprudenciais, encaje chileno, Brasil pós-2008."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: comentário de E3-L00293 (mesmo item, “Questão 65 — Item 4”) fundido",
                    "banca_provavel: CEBRASPE, IRBr/CACD/2018 (marca ⌚ e numeração “Questão 65” na duplicata; "
                    "não confirmada)",
                    "qualidade_fonte: o comentário de origem chama swaps cambiais de medida prudencial; são "
                    "intervenção cambial, não regulação prudencial"],
    },
    # ------------------------------------------------------------------ E1-0941
    {
        "id": "ECO-E1-0941-1", "fonte_ref": "E1-0941", "destino": "78", "subtema": H2["glob"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": "Acerca das crises financeiras internacionais, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Como o contágio que caracterizou as crises de câmbio do período 1980-2000 deveu-se ao canal "
                      "financeiro, não houve deterioração da balança comercial dos países afetados por esse "
                      "fenômeno."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Como") + az(" o contágio que caracterizou as crises de câmbio do período 1980-2000 ")
                    + vm("deveu-se ao canal financeiro, não houve") + az(" deterioração da balança comercial dos "
                                                                         "países afetados por esse fenômeno.")),
        "poucas": ("O contágio operou também pelo " + azb("canal comercial") + ": a desvalorização de um país "
                   "tira competitividade dos concorrentes e a recessão corta a demanda dos parceiros. Canal "
                   "financeiro e balança comercial não são compartimentos estanques."),
        "destrinchando": [
            azb("Contágio") + " = transmissão de uma crise de um país a outros. Canais: (1) "
            + azb("financeiro") + " — investidores vendem ativos de vários emergentes ao mesmo tempo, por "
            "perdas, falta de liquidez ou reavaliação do risco; (2) " + azb("comercial") + " — a "
            "desvalorização do país em crise barateia suas exportações e prejudica os concorrentes em terceiros "
            "mercados, e a recessão reduz as importações que ele fazia dos vizinhos; (3) preços de "
            "commodities.",
            "Exemplos: na crise asiática (1997), a desvalorização do baht tailandês pressionou as moedas e as "
            "exportações de Malásia, Indonésia, Filipinas e Coreia; a crise russa (1998) derrubou commodities e "
            "atingiu o " + rx("Brasil") + "; a desvalorização do real (1999) afetou as vendas da Argentina ao "
            "Mercosul.",
            "O BP amarra as contas: a reversão da conta financeira obriga um ajuste da conta corrente. Antes da "
            "crise, ingressos abundantes apreciam o câmbio e abrem déficits comerciais; depois, o país precisa "
            "gerar superávit (via desvalorização e recessão) para pagar o passivo externo.",
            vm("Regra-âncora: crise financeira e desequilíbrio comercial andam juntos; o contágio tem canal "
               "financeiro e canal comercial."),
        ],
        "dissecando": (cz("[nexo indevido · restrição indevida]") + " O “Como… deveu-se ao canal financeiro” "
                       "cria uma causa exclusiva e dela tira uma consequência falsa (“não houve deterioração "
                       "comercial”). Pista: conclusões absolutas tiradas de uma premissa causal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O contágio entre economias emergentes nas crises cambiais dos anos 1990 operou tanto por canais "
            "financeiros quanto comerciais.”</i> → CERTO",
            "<i>“A desvalorização cambial de um país em crise não afeta a competitividade de seus concorrentes "
            "comerciais.”</i> → ERRADO (é justamente o canal comercial do contágio)",
        ])],
        "reescrita": (hl("Embora") + " o contágio que caracterizou as crises de câmbio do período 1980-2000 "
                      + hl("tenha operado sobretudo pelo canal financeiro, também houve, pelo canal comercial,")
                      + " deterioração da balança comercial dos países afetados por esse fenômeno."),
        "tipo_erro": ["NEXO_INDEVIDO", "RESTRICAO"], "moduladores": ["como"], "dificuldade": 2,
        "comentario_fonte": ("Fenômenos financeiros e comerciais do BP são solidários; crises têm antecedentes de "
                             "ingressos abundantes, valorização cambial e déficits comerciais; o ajuste exige "
                             "desvalorização."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE (marca ⌚ e ano 2015; órgão não informado)"],
    },
    # ------------------------------------------------------------------ E1-0946
    {
        "id": "ECO-E1-0946-1", "fonte_ref": "E1-0946", "destino": "78", "subtema": H2["glob"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": True,
        "comando": "Acerca dos fluxos internacionais de capitais, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Os aumentos do imposto sobre operações financeiras incidente sobre os investimentos "
                      "estrangeiros constituem exemplos de controles de capitais de curto prazo, cujo objetivo é "
                      "neutralizar os impactos decorrentes da volatilidade dos fluxos desse tipo de capital sobre "
                      "os mercados cambial e de capitais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os aumentos do <u>imposto sobre operações financeiras</u> incidente sobre os investimentos "
                      "estrangeiros constituem exemplos de <u>controles de capitais de curto prazo</u>, cujo "
                      "objetivo é neutralizar os impactos decorrentes da volatilidade dos fluxos desse tipo de "
                      "capital sobre os mercados cambial e de capitais."),
        "poucas": ("O " + rx("IOF sobre ingressos estrangeiros (2009–2013)") + " foi um " + azb("controle de "
                   "capitais baseado em preço") + ": encarecia a entrada de capital de curto prazo para conter "
                   "a apreciação do real e a volatilidade."),
        "destrinchando": [
            "Contexto: após 2008, juros baixos nos países ricos e o " + azb("quantitative easing") + " empurraram "
            "capital para emergentes de juros altos (" + azb("carry trade") + "). O real se apreciou forte e o "
            "ministro " + oc("Guido Mantega") + " falou em “" + azb("guerra cambial") + "” (2010).",
            "Medidas no " + rx("Brasil") + ": IOF de " + vd("2%") + " sobre ingressos em renda fixa e ações "
            "(out/2009); alta para " + vd("6%") + " em renda fixa (out/2010); IOF sobre empréstimos externos de "
            "curto prazo (2011) e sobre derivativos cambiais (2011). Com a reversão dos fluxos, as alíquotas "
            "foram zeradas em 2013.",
            azb("Controles de capitais") + " podem ser " + azb("administrativos") + " (proibições, quotas, prazos "
            "mínimos) ou " + azb("baseados em preço") + " (impostos, depósitos compulsórios não remunerados, "
            "como o encaje chileno). O tributo diferencia por prazo e tipo: penaliza o capital de giro rápido "
            "e preserva o IED.",
            "Eficácia: a literatura indica efeito sobre a <b>composição</b> (alonga prazos) maior que sobre o "
            "volume e o câmbio; há evasão por derivativos e por canais não tributados. O " + azb("FMI") + " "
            "reconheceu, em 2012, as " + azb("medidas de gestão de fluxos de capital") + " como instrumento "
            "legítimo em surtos de ingresso.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item descreve corretamente a natureza (controle "
                       "via preço) e o objetivo (conter a volatilidade). O verbo “neutralizar” soa forte, mas "
                       "expressa o objetivo declarado, não o resultado. Quem errou provavelmente achou que "
                       "imposto não é “controle”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O IOF sobre ingressos de capital estrangeiro visava, sobretudo, desestimular o investimento "
            "estrangeiro direto.”</i> → ERRADO (o alvo era o capital de curto prazo)",
            "<i>“Controles de capitais podem assumir a forma de tributos ou de depósitos compulsórios sobre "
            "ingressos.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Fluxos de curto prazo × longo prazo; entrada desmedida de capital de curto prazo "
                             "aprecia o câmbio e prejudica exportações; o IOF disciplina essa entrada em favor do "
                             "capital produtivo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE (marca ⌚ e ano 2011; órgão não informado)"],
    },
    # ------------------------------------------------------------------ E2-L00503
    {
        "id": "ECO-E2-L00503-1", "fonte_ref": "E2-L00503", "destino": "78", "subtema": H2["glob"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Acerca de macroeconomia aberta e sistema monetário internacional, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O comércio internacional representa dimensão tradicional das relações internacionais, sendo "
                      "o principal responsável pelos movimentos financeiros internacionais, à frente dos fluxos "
                      "de investimento direto, dos empréstimos oficiais e dos demais fluxos do mercado "
                      "internacional de capitais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O comércio internacional representa dimensão tradicional das relações internacionais, "
                       "sendo ") + vm("o principal responsável pelos movimentos financeiros internacionais, à "
                                      "frente dos")
                    + az(" fluxos de investimento direto, dos empréstimos oficiais e dos demais fluxos do mercado "
                         "internacional de capitais.")),
        "poucas": ("Desde a " + azb("globalização financeira") + " (anos 1970–1990), os fluxos financeiros "
                   "superam em muito os comerciais: o mercado de câmbio gira em poucos dias o equivalente ao "
                   "comércio mundial de um ano."),
        "destrinchando": [
            "Ordem de grandeza: o comércio mundial de bens e serviços é da ordem de " + vd("US$ 30 trilhões por "
            "ano") + "; o mercado de câmbio movimentou cerca de " + vd("US$ 7,5 trilhões por dia") + " na "
            "pesquisa trienal do " + azb("BIS") + " de 2022 ⏳ (out/2026). A maior parte das transações "
            "cambiais é financeira, não comercial.",
            "Até Bretton Woods, com controles de capitais generalizados, os pagamentos internacionais eram "
            "dominados pelo comércio. A partir dos anos 1970 (fim da paridade ouro-dólar, euromercado, "
            "petrodólares) e da liberalização dos anos 1980–1990, os fluxos financeiros ganharam vida própria.",
            "Consequências: o câmbio passa a ser determinado sobretudo pela conta financeira (expectativas, "
            "diferencial de juros), não pela balança comercial; cresce a " + azb("volatilidade") + " e a "
            "vulnerabilidade dos emergentes a reversões de fluxo.",
            "A primeira oração (comércio como dimensão tradicional das relações internacionais) está correta; o "
            "erro está na hierarquia atribuída.",
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " Começa com uma obviedade verdadeira e enxerta uma "
                       "hierarquia invertida. Pista: “principal responsável… à frente de” — superlativos "
                       "comparativos sobre grandezas econômicas pedem conferência de ordem de grandeza."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O volume das transações financeiras internacionais supera largamente o valor do comércio "
            "mundial de bens e serviços.”</i> → CERTO",
            "<i>“Em regime de câmbio flutuante com mobilidade de capitais, a taxa de câmbio é determinada "
            "exclusivamente pela balança comercial.”</i> → ERRADO (modulador absoluto; a conta financeira pesa "
            "mais)",
        ])],
        "reescrita": ("O comércio internacional representa dimensão tradicional das relações internacionais, sendo "
                      + hl("hoje um responsável menor pelos movimentos financeiros internacionais que o conjunto "
                           "dos") + " fluxos de investimento direto, dos empréstimos oficiais e dos demais fluxos "
                      "do mercado internacional de capitais."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["principal"], "dificuldade": 1,
        "comentario_fonte": ("Os fluxos financeiros superam em muito os comerciais; a liberalização tornou os "
                             "movimentos financeiros a dimensão dominante."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0025
    {
        "id": "ECO-E1-0025-1", "fonte_ref": "E1-0025", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_MERC,
        "rotulo_item": "Item",
        "assertiva": ("Caso o preço praticado no mercado internacional seja de 50 unidades monetárias, o país "
                      "importará 150 unidades do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Caso o preço praticado no mercado internacional seja de 50 unidades monetárias, o país ")
                    + vm("importará 150 unidades") + az(" do bem.")),
        "poucas": ("O equilíbrio de autarquia é " + vd("P = 50, Q = 10") + ". Com preço mundial igual a 50, a "
                   "oferta doméstica cobre toda a demanda: " + vd("importação zero") + ". E 150 é impossível em "
                   "qualquer caso: a demanda máxima (com P = 0) é " + vd("20") + "."),
        "destrinchando": [
            "Autarquia: 100 − 5Q = 10 + 4Q → 9Q = 90 → " + vd("Q = 10") + " e " + vd("P = 50") + ".",
            "Importações = Qᴰ − Qˢ ao preço mundial. Reescrevendo em função de P: Qᴰ = (100 − P)/5 e "
            "Qˢ = (P − 10)/4. Com P = 50: Qᴰ = 10 e Qˢ = 10 → " + vd("M = 0") + ".",
            "Regra geral do país pequeno: preço mundial " + azb("abaixo") + " do de autarquia → o país "
            + azb("importa") + "; " + azb("acima") + " → " + azb("exporta") + "; igual → não comercializa. "
            "Exemplo: a 30, Qᴰ = 14 e Qˢ = 5, importa " + vd("9") + "; a 60, Qᴰ = 8 e Qˢ = 12,5, exporta 4,5.",
            "Teste de sanidade que mata o item em segundos: a demanda corta o eixo das quantidades em "
            + vd("Q = 20") + " (P = 0). Nenhum preço positivo faz o país consumir — muito menos importar — 150 "
            "unidades.",
        ],
        "grafico_verso": "ECO-E1-0025-1-V1",
        "dissecando": (cz("[dado alterado]") + " Número inventado sem relação com as curvas. Em itens de "
                       "cálculo, antes de resolver, confira os limites do mercado (interceptos): aqui a "
                       "quantidade máxima demandada é 20."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Caso o preço internacional seja de 30 unidades monetárias, o país importará 9 unidades do "
            "bem.”</i> → CERTO",
            "<i>“Caso o preço internacional seja de 60 unidades monetárias, o país importará 4,5 unidades.”</i> "
            "→ ERRADO (acima do preço de autarquia o país exporta)",
        ])],
        "reescrita": ("Caso o preço praticado no mercado internacional seja de 50 unidades monetárias, o país "
                      + hl("não importará nenhuma unidade") + " do bem."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Equilíbrio doméstico P = 50, Q = 10, igual ao preço internacional: não há "
                             "importação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (17), (18), (22), (19).png", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "cortada (contas não preservadas; refeitas no 📖)"}],
        "alertas": [ALERTA_MERC],
    },
    # ------------------------------------------------------------------ E1-0026
    {
        "id": "ECO-E1-0026-1", "fonte_ref": "E1-0026", "destino": "79", "subtema": H2["cota"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_MERC,
        "rotulo_item": "Item",
        "assertiva": ("Caso seja imposta uma cota de 9 unidades de importação, o preço praticado no mercado "
                      "internacional será de 70 unidades monetárias."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Caso seja imposta uma cota de 9 unidades de importação, o preço praticado no mercado "
                       "internacional ") + vm("será de 70 unidades monetárias") + az(".")),
        "poucas": ("A cota de um país pequeno " + azb("não altera o preço internacional") + "; se for "
                   "restritiva, eleva só o preço " + azb("interno") + ". Aqui, com cota de 9, o preço interno "
                   "iria no máximo a " + vd("30") + " — nunca 70, que fica acima até do preço de autarquia (50)."),
        "destrinchando": [
            "Com cota Q̄, o mercado interno fecha em Qᴰ(P) = Qˢ(P) + Q̄. Aqui: (100 − P)/5 = (P − 10)/4 + 9 → "
            "multiplicando por 20: 400 − 4P = 5P − 50 + 180 → " + vd("P = 30") + ", com Qᴰ = " + vd("14")
            + " e Qˢ = " + vd("5") + ".",
            "Esse preço só vale se a cota for " + azb("restritiva") + ": é preciso que, sem ela, se importasse "
            "mais de 9 — o que ocorre com preço mundial abaixo de 30. Se o preço mundial estiver entre 30 e 50, "
            "o país importa menos de 9 e a cota não morde.",
            "Com P = 70 o mercado nem importaria: a esse preço, Qᴰ = 6 e Qˢ = 15 (excesso de oferta). Cota de "
            "importação nunca leva o preço interno acima do de autarquia (50).",
            "Cota × tarifa: o efeito sobre preço e quantidades é o mesmo de uma " + azb("tarifa "
            "equivalente") + " (aqui, tarifa que eleve o preço de 20 a 30, por exemplo). A diferença: a área "
            "que seria receita tarifária vira " + azb("renda de cota") + " de quem detém as licenças de "
            "importação (ou do governo, se as leiloar).",
            vm("Regra-âncora: país pequeno não mexe no preço mundial; tarifa ou cota mudam só o preço "
               "doméstico."),
        ],
        "grafico_verso": "ECO-E1-0026-1-V1",
        "dissecando": (cz("[troca de conceito · dado alterado]") + " Troca o preço interno pelo internacional "
                       "e oferece um número impossível (acima da autarquia). Pista: instrumento de política "
                       "comercial de um país pequeno afetando o “preço do mercado internacional”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com preço mundial de 20, uma cota de 9 unidades elevaria o preço doméstico para 30.”</i> → "
            "CERTO",
            "<i>“A cota de importação gera para o governo, necessariamente, receita igual à de uma tarifa "
            "equivalente.”</i> → ERRADO (a renda fica com os detentores das licenças, salvo leilão)",
        ])],
        "reescrita": ("Caso seja imposta uma cota de 9 unidades de importação, o preço praticado no mercado "
                      "internacional " + hl("não se alterará; se a cota for restritiva, só o preço interno "
                                            "subirá, até 30 unidades monetárias") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "DADO_ALTERADO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Comentários divergentes: um calcula P = 55 inserindo a cota na demanda; outro diz "
                             "que a cota não alteraria o preço; outro mostra que P = 70 é incompatível com as "
                             "curvas."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (17), (18), (22), (19).png", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "cortada (contas não preservadas; refeitas no 📖)"}],
        "alertas": [ALERTA_MERC,
                    "qualidade_fonte: um comentário de origem calcula P = 55 substituindo Q = 9 na demanda; com "
                    "cota de 9, o preço interno é 30 (Qᴰ = Qˢ + 9)"],
    },
    # ------------------------------------------------------------------ E1-0027
    {
        "id": "ECO-E1-0027-1", "fonte_ref": "E1-0027", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": CMD_MERC,
        "rotulo_item": "Item",
        "assertiva": ("Caso seja imposta uma tarifa lump sum no valor de 50 unidades de importação, a quantidade "
                      "consumida no mercado doméstico será superior a 20 unidades do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Caso seja imposta uma tarifa lump sum no valor de 50 unidades de importação, a quantidade "
                       "consumida no mercado doméstico será ") + vm("superior") + az(" a 20 unidades do bem.")),
        "poucas": ("A demanda P = 100 − 5Q chega no máximo a " + vd("Q = 20") + " (com P = 0). Qualquer preço "
                   "positivo — com ou sem tarifa — dá consumo " + vd("abaixo de 20") + "."),
        "destrinchando": [
            "Teste do intercepto: P = 0 → 5Q = 100 → " + vd("Q = 20") + ". Como a demanda é decrescente, todo "
            "P > 0 dá Q < 20. O item cai sem conta nenhuma.",
            "Tarifa aumenta (ou mantém) o preço doméstico, nunca o reduz; logo, só pode diminuir o consumo em "
            "relação ao livre-comércio. Lida como tarifa " + azb("específica") + " de 50 por unidade, o importado "
            "passa a custar Pm + 50 ≥ 50, o preço de autarquia: a tarifa é " + azb("proibitiva") + ", as "
            "importações zeram e o país volta à autarquia (" + vd("Q = 10, P = 50") + ").",
            "Lida literalmente como " + azb("lump sum") + " (valor fixo, independente da quantidade), a tarifa "
            "não altera o preço na margem: o consumo fica no nível de livre-comércio — também abaixo de 20.",
            "Cuidado com erros comuns: somar a tarifa à oferta <b>doméstica</b> (os produtores nacionais não "
            "pagam tarifa; ela incide sobre o importado) ou multiplicar o preço pela tarifa.",
        ],
        "dissecando": (cz("[inversão · dado alterado]") + " O item embrulha um conceito exótico (“lump sum”) "
                       "para intimidar, mas se resolve pelo limite da demanda. 🔥 Em itens numéricos com "
                       "curvas lineares, confira primeiro os interceptos: muitos itens erram por propor valores "
                       "fora do domínio possível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Qualquer que seja a tarifa imposta, a quantidade consumida no mercado doméstico não superará "
            "20 unidades do bem.”</i> → CERTO",
            "<i>“Uma tarifa de importação reduz o preço pago pelo consumidor doméstico.”</i> → ERRADO "
            "(inversão: eleva ou mantém o preço)",
        ])],
        "reescrita": ("Caso seja imposta uma tarifa lump sum no valor de 50 unidades de importação, a quantidade "
                      "consumida no mercado doméstico será " + hl("inferior") + " a 20 unidades do bem."),
        "tipo_erro": ["INVERSAO", "DADO_ALTERADO"], "moduladores": ["superior"], "dificuldade": 1,
        "comentario_fonte": ("Comentários com contas divergentes (Q = 8 e P = 80; Q ≈ 4,44; “P + 50P”); "
                             "concordam que o consumo fica abaixo de 20; lump sum = valor fixo."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [ALERTA_MERC,
                    "qualidade_fonte: comentários de origem somam a tarifa à oferta doméstica, erram a álgebra "
                    "(100 − 5Q = 60 + 4Q dá Q = 40/9, não 8) ou tratam a tarifa como “50P”; resolvido pelo "
                    "intercepto da demanda"],
    },
    # ------------------------------------------------------------------ E1-0028
    {
        "id": "ECO-E1-0028-1", "fonte_ref": "E1-0028", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos das tarifas de importação sobre o bem-estar, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Quanto maior a tarifa imposta, maior a tendência de perda de eficiência e maior o ganho de "
                      "excedente do consumidor verificado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quanto maior a tarifa imposta, maior a tendência de perda de eficiência e ")
                    + vm("maior o ganho") + az(" de excedente do consumidor verificado.")),
        "poucas": ("A tarifa eleva o preço interno: o consumidor " + vm("perde") + " excedente, e perde mais "
                   "quanto maior a tarifa. A primeira metade (mais peso morto com tarifa maior) está certa."),
        "destrinchando": [
            "País pequeno, tarifa t: preço interno sobe de Pm para Pm + t; produção doméstica sobe, consumo cai, "
            "importações caem. Na notação de " + oc("Krugman e Obstfeld") + ": consumidor perde "
            + vd("a + b + c + d") + "; produtor ganha " + vd("a") + "; governo arrecada " + vd("c") + "; "
            + azb("perda de eficiência") + " = " + vd("b + d") + " (b: distorção na produção; d: distorção no "
            "consumo).",
            "Tarifa maior → faixa entre Pm e Pm + t mais alta → perda do consumidor maior. O peso morto cresce "
            "mais que proporcionalmente (aproximadamente com o " + azb("quadrado") + " da tarifa).",
            "Limite: a " + azb("tarifa proibitiva") + " (Pm + t ≥ preço de autarquia) zera as importações e a "
            "receita; daí em diante, aumentar t não muda mais nada.",
            "Exceção que a banca pode cobrar: no " + azb("país grande") + ", a tarifa derruba o preço mundial "
            "(ganho de termos de troca) e uma tarifa pequena pode elevar o bem-estar nacional — a "
            + azb("tarifa ótima") + ". Mesmo aí, o consumidor doméstico perde, e o mundo como um todo também.",
            vm("Regra-âncora: tarifa → consumidor perde; produtor e governo ganham; o país perde b + d."),
        ],
        "grafico_verso": "ECO-E1-0028-1-V1",
        "dissecando": (cz("[meia-verdade]") + " A 1ª metade é verdadeira (perda de eficiência cresce com a "
                       "tarifa) e dá credibilidade à 2ª, que inverte o sinal do efeito sobre o consumidor. "
                       "Pista: quem paga o preço mais alto não pode “ganhar” excedente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a tarifa imposta, maior a perda de excedente do consumidor.”</i> → CERTO",
            "<i>“Quanto maior a tarifa, maior a arrecadação do governo.”</i> → ERRADO (generalização: acima de "
            "certo ponto a base de importações encolhe e a tarifa proibitiva arrecada zero)",
        ])],
        "reescrita": ("Quanto maior a tarifa imposta, maior a tendência de perda de eficiência e "
                      + hl("maior a perda") + " de excedente do consumidor verificado."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["quanto maior"], "dificuldade": 1,
        "comentario_fonte": ("Tarifa eleva o preço e reduz o excedente do consumidor (de R + T para R, gráfico de "
                             "Varian); perda de eficiência; caso extremo em que o produtor arca com tudo e o EC "
                             "não muda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (23).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "substituída pelo redesenho didático ECO-E1-0028-1-V1"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0159
    {
        "id": "ECO-E1-0159-1", "fonte_ref": "E1-0159", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_SUB,
        "rotulo_item": "Item",
        "assertiva": ("Uma forma de se fazer política comercial se dá com o subsídio à exportação de um "
                      "determinado produto. Uma característica dessa política é que acarreta custo para o "
                      "Governo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma forma de se fazer política comercial se dá com o subsídio à exportação de um "
                      "determinado produto. Uma característica dessa política é que acarreta <u>custo para o "
                      "Governo</u>."),
        "poucas": ("O subsídio é um " + azb("pagamento") + " do governo por unidade exportada: gera " + vd("gasto "
                   "fiscal") + ", ao contrário da tarifa, que gera receita."),
        "destrinchando": [
            "Mecanismo (país pequeno): com subsídio s por unidade exportada, o produtor só vende no mercado "
            "interno se receber o mesmo que exportando — o " + azb("preço doméstico sobe") + " de Pm para "
            "Pm + s. Produção ↑, consumo interno ↓, exportações ↑.",
            "Bem-estar (notação de " + oc("Krugman e Obstfeld") + "): produtores ganham; consumidores perdem; "
            "o governo gasta s × exportações; o saldo é " + azb("perda líquida") + " (distorções de produção e "
            "de consumo). No " + azb("país grande") + ", a oferta extra derruba o preço mundial e há ainda "
            "perda de " + azb("termos de troca") + ": o país subsidia o consumidor estrangeiro.",
            "Regras da " + azb("OMC") + ": o Acordo sobre Subsídios e Medidas Compensatórias (SMC) "
            + vd("proíbe") + " subsídios condicionados à exportação para bens industriais (art. 3); na "
            "agricultura, a Conferência Ministerial de " + vd("Nairóbi (2015)") + " decidiu eliminar os "
            "subsídios à exportação. O país afetado pode recorrer ao sistema de solução de controvérsias ou "
            "aplicar " + azb("direitos compensatórios") + ".",
            rx("Brasil") + ": venceu os EUA no contencioso do algodão (DS267, aberto em 2002) e litigou com o Canadá sobre "
            "aviões regionais (Embraer × Bombardier, anos 1990–2000), em que o Proex brasileiro também foi "
            "questionado.",
        ],
        "dissecando": (cz("[literalidade]") + " Afirmação de manual, sem armadilha. A banca costuma explorar "
                       "o contraste com a tarifa (“o subsídio gera receita ao governo” → ERRADO) ou o efeito "
                       "sobre o preço doméstico (“reduz o preço ao consumidor nacional” → ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O subsídio à exportação eleva o preço doméstico do bem subsidiado.”</i> → CERTO",
            "<i>“O subsídio à exportação, por gerar receita, é preferível à tarifa do ponto de vista "
            "fiscal.”</i> → ERRADO (troca de conceito: quem gera receita é a tarifa)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Subsídio à exportação é pagamento por unidade exportada: custo fiscal direto; "
                             "tende a reduzir o bem-estar nacional."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0160
    {
        "id": "ECO-E1-0160-1", "fonte_ref": "E1-0160", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_SUB,
        "rotulo_item": "Item",
        "assertiva": ("Uma forma de se fazer política comercial se dá com o subsídio à exportação de um "
                      "determinado produto. Uma característica dessa política é que acarreta redução da produção "
                      "do produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma forma de se fazer política comercial se dá com o subsídio à exportação de um "
                       "determinado produto. Uma característica dessa política é que acarreta ")
                    + vm("redução") + az(" da produção do produto.")),
        "poucas": ("O subsídio eleva o preço recebido pelo produtor (Pm + s): a produção " + vd("aumenta")
                   + ". Quem cai é o " + azb("consumo interno") + "."),
        "destrinchando": [
            "Com subsídio s por unidade exportada, o produtor recebe Pm + s ao exportar; para vender no mercado "
            "interno, exige o mesmo. O preço doméstico sobe para Pm + s, e a empresa sobe ao longo da curva de "
            "oferta: " + vd("produção ↑") + ".",
            "Do lado da demanda, o preço maior reduz o " + vd("consumo interno ↓") + ". Exportações = produção "
            "− consumo → " + vd("sobem") + " pelos dois lados.",
            "Comparação com a tarifa: ambas elevam o preço doméstico e a produção nacional, e ambas reduzem o "
            "consumo interno. A diferença está no governo: tarifa arrecada; subsídio gasta. E a tarifa reduz o "
            "comércio, enquanto o subsídio o amplia.",
            vm("Regra-âncora: subsídio à exportação → preço interno ↑, produção ↑, consumo ↓, exportação ↑, "
               "gasto público ↑."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o efeito sobre a produção, talvez confundindo com o "
                       "consumo interno, que de fato cai. Pista: subsídio é incentivo — incentivo a produzir "
                       "não reduz a produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O subsídio à exportação acarreta redução do consumo doméstico do produto.”</i> → CERTO",
            "<i>“O subsídio à exportação reduz o preço pago pelos consumidores domésticos.”</i> → ERRADO "
            "(inversão: o preço interno sobe)",
        ])],
        "reescrita": ("Uma forma de se fazer política comercial se dá com o subsídio à exportação de um "
                      "determinado produto. Uma característica dessa política é que acarreta " + hl("aumento")
                      + " da produção do produto."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Subsídio à exportação torna as vendas externas mais lucrativas e estimula a produção.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0166
    {
        "id": "ECO-E1-0166-1", "fonte_ref": "E1-0166", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_SUB,
        "rotulo_item": "Item",
        "assertiva": ("Caso um país decida reduzir a tarifa ad valorem até então existente sobre uma mercadoria "
                      "específica, como resultado haverá redução da arrecadação do Governo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Caso um país decida reduzir a tarifa ad valorem até então existente sobre uma mercadoria "
                      "específica, como resultado <u>haverá</u> redução da arrecadação do Governo."),
        "poucas": ("Na leitura da banca: alíquota menor sobre a mesma base → " + vd("arrecada-se menos") + ". "
                   "Mas a base (o valor importado) cresce quando a tarifa cai, e o resultado depende da "
                   + azb("elasticidade") + " das importações."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "arrecadação = alíquota × valor importado, e o valor importado <b>aumenta</b> quando a "
                          "tarifa cai. Se a tarifa inicial for muito alta — no limite, " + azb("proibitiva")
                          + ", com arrecadação zero — reduzi-la eleva a receita (lógica da " + azb("curva de "
                          "Laffer") + "). O “haverá” categórico só vale com importações pouco elásticas ou "
                          "tarifas moderadas; seria mais defensável “tende a haver” ou ERRADO pela "
                          "generalização.")],
        "destrinchando": [
            azb("Tarifa ad valorem") + ": percentual sobre o valor aduaneiro (no " + rx("Brasil") + ", o "
            "Imposto de Importação incide em regra sobre o valor CIF, com alíquotas da TEC do Mercosul). "
            + azb("Tarifa específica") + ": valor fixo por unidade física (R$ por tonelada).",
            "Efeito da redução: preço interno cai, consumo ↑, produção doméstica ↓, importações ↑. A receita "
            "muda por dois efeitos opostos: " + vd("efeito alíquota") + " (menos por unidade) e "
            + vd("efeito base") + " (mais unidades).",
            "Quando a receita certamente cai: importações inelásticas, ou corte para zero (receita zero). "
            "Quando pode subir: tarifa inicial próxima da proibitiva, com demanda de importações elástica.",
            "Bem-estar: reduzir a tarifa diminui o peso morto (distorções de produção e consumo), aumenta o "
            "excedente do consumidor e reduz o do produtor doméstico — por isso a liberalização tem ganhadores "
            "difusos e perdedores concentrados.",
        ],
        "dissecando": (cz("[literalidade · modulador absoluto]") + " A banca considerou a leitura mecânica "
                       "(alíquota menor = menos receita). O risco está no “haverá”, que ignora o efeito base; "
                       "em prova, itens com “tende a” protegem o CERTO, e afirmações categóricas sobre receita "
                       "tributária costumam ser a armadilha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução de uma tarifa proibitiva aumenta a arrecadação do governo.”</i> → CERTO",
            "<i>“A redução da tarifa de importação eleva o excedente do produtor doméstico.”</i> → ERRADO "
            "(inversão: o preço interno cai e o produtor perde)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["haverá"], "dificuldade": 2,
        "comentario_fonte": "Tarifa ad valorem é proporcional ao valor; reduzir a alíquota reduz a receita por unidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: a redução da tarifa amplia a base importada; com tarifa inicial alta "
                    "(proibitiva ou próxima), a arrecadação pode subir"],
    },
    # ------------------------------------------------------------------ E1-0442
    {
        "id": "ECO-E1-0442-1", "fonte_ref": "E1-0442", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Clipping", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Conflitos comerciais entre países, conhecidos como guerras comerciais, têm se tornado eventos "
                    "recorrentes na economia global contemporânea. Geralmente caracterizadas pela imposição "
                    "recíproca de tarifas, essas disputas afetam tanto o fluxo de bens quanto as expectativas "
                    "dos agentes econômicos. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A imposição de tarifas eleva o preço dos bens importados, o que pode gerar efeitos "
                      "regressivos sobre o consumo das famílias, sobretudo nas camadas de menor renda, devido à "
                      "perda de poder de compra."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de tarifas eleva o preço dos bens importados, o que <u>pode</u> gerar efeitos "
                      "<u>regressivos</u> sobre o consumo das famílias, sobretudo nas camadas de menor renda, "
                      "devido à perda de poder de compra."),
        "poucas": ("A tarifa é um " + azb("imposto sobre o consumo") + " de bens comerciáveis; como os mais "
                   "pobres gastam fração maior da renda em bens, perdem proporcionalmente mais: efeito "
                   + azb("regressivo") + "."),
        "destrinchando": [
            azb("Regressivo") + " = onera proporcionalmente mais quem ganha menos (o peso no orçamento cai com a "
            "renda). " + azb("Progressivo") + " = o contrário.",
            "Por que a tarifa é regressiva: famílias de baixa renda consomem quase toda a renda (propensão "
            "média a consumir próxima de 1) e gastam parcela maior em bens comerciáveis (alimentos, vestuário, "
            "eletrodomésticos); as de alta renda poupam mais e gastam mais em serviços.",
            "A tarifa encarece não só o importado: o produtor nacional concorrente também eleva o preço até "
            "perto do preço com tarifa. A perda do consumidor supera a receita do governo — parte vira ganho "
            "do produtor protegido e parte é peso morto.",
            "Em guerras comerciais, as tarifas sobre insumos se propagam pelas cadeias e chegam ao preço final. "
            "Estudos sobre as tarifas dos EUA em 2018–2019 encontraram repasse quase integral aos preços "
            "domésticos (" + oc("Amiti, Redding e Weinstein") + ", 2019).",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “pode” e o “sobretudo” blindam o item. A banca "
                       "tornaria ERRADO dizendo que a tarifa é “progressiva” ou que “recai apenas sobre os "
                       "exportadores estrangeiros”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por incidir sobre bens importados, consumidos principalmente pelas camadas de maior renda, as "
            "tarifas têm efeito progressivo.”</i> → ERRADO (inversão: o efeito típico é regressivo)",
            "<i>“O ônus de uma tarifa recai integralmente sobre o exportador estrangeiro.”</i> → ERRADO "
            "(modulador absoluto: em país pequeno recai sobre o consumidor doméstico)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode", "sobretudo"], "dificuldade": 1,
        "comentario_fonte": ("Tarifas funcionam como imposto sobre o consumo de importados; famílias de baixa "
                             "renda gastam proporção maior em bens de consumo: efeito regressivo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0544 (mesmo item e mesmo comentário) fundido neste card"],
    },
]
