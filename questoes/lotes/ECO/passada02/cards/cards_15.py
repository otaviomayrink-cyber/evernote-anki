"""Cards do lote de redação 15 — ECO, passada 02 (nota 35: moeda, criação, multiplicador, demanda por moeda)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "agr": "🪙 Funções e agregados monetários",
    "mult": "🏦 Criação de moeda e multiplicador",
    "dem": "📊 Demanda por moeda",
}

CMD_M1_2013 = ("Com relação ao conceito de meios de pagamento (M1), que corresponde ao estoque de moeda disponível "
               "para uso da coletividade, julgue o item a seguir.")

CMD_BOZ_MULT = "Sobre a dinâmica de multiplicação monetária, julgue o item a seguir."
CMD_BOZ_KEY = ("Julgue o item a seguir como certo ou errado, com base nos conceitos de política econômica e de "
               "intervenção governamental nos contextos keynesiano e clássico.")
CMD_BOZ_MERC = "Com base na estrutura e no funcionamento dos mercados monetários, julgue o item a seguir."
CMD_BOZ_AGR = ("Considerando o impacto dos agregados monetários e das instituições financeiras sobre a economia, "
               "julgue o item a seguir.")

CMD_ARM = "Julgue o item a seguir, relativo à oferta de moeda e ao multiplicador bancário."

CMD_NAB_CN = ("A respeito das contas nacionais, do balanço de pagamentos, das contas públicas e do sistema "
              "monetário, julgue o item seguinte.")
CMD_NAB_MOEDA = "Sobre moeda, política monetária e sistema financeiro, julgue o item seguinte."
CMD_NAB_MODELOS = "Em relação aos modelos macroeconômicos, julgue o item seguinte."
CMD_NAB_CONC = "Em relação aos conceitos macroeconômicos, julgue o item seguinte."
CMD_NAB_SIST = "Em relação ao sistema monetário e à política monetária, julgue o item seguinte."
CMD_NAB_MACRO = "Em relação à macroeconomia, julgue o item seguinte."
CMD_NAB_POL = "No que diz respeito à moeda e à política monetária, julgue o item seguinte."
CMD_NAB_CN2 = ("Em relação às contas nacionais, ao balanço de pagamentos e ao sistema monetário, julgue o item "
               "seguinte.")

FIG_E1 = lambda ref: [{"ref": ref, "tipo_fonte": "IMAGEM", "lado": "verso",
                       "acao": "irrecuperavel (imagem do verso não preservada; conteúdo do texto absorvido no 📖)"}]

BANCA_2013 = ("banca_provavel: CEBRASPE (formato C/E de 2013 com itens A–D sobre M1 sugere a prova do CACD/2013; "
              "a fonte não traz órgão)")

CARDS = [
    # ------------------------------------------------------------------ E1-0516
    {
        "id": "ECO-E1-0516-1", "fonte_ref": "E1-0516", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_M1_2013,
        "rotulo_item": "Item",
        "assertiva": ("O valor do multiplicador da base monetária varia na razão inversa da taxa de reservas dos "
                      "bancos comerciais e na razão direta da taxa de retenção da moeda pelo público."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O valor do multiplicador da base monetária varia na razão inversa da taxa de reservas dos "
                       "bancos comerciais e na razão ") + vm("direta") + az(" da taxa de retenção da moeda pelo "
                                                                             "público.")),
        "poucas": ("O multiplicador cai tanto quando os bancos retêm mais " + azb("reservas") + " quanto quando o "
                   "público retém mais " + azb("papel-moeda") + ": as duas relações são <b>inversas</b>."),
        "destrinchando": [
            "Fórmula de referência: " + vd("m = M1 / B = 1 / [c + r(1 − c)]") + ", em que c = PMPP/M1 (fração "
            "dos meios de pagamento que o público guarda em espécie) e r = reservas/depósitos à vista (encaixe "
            "dos bancos). Versão equivalente com c′ = PMPP/DV: " + vd("m = (1 + c′) / (c′ + r)") + ".",
            azb("Reservas (r)") + ": cada real que o banco deixa parado em caixa ou no Banco Central é um real "
            "que não vira empréstimo e, portanto, não volta ao sistema como novo depósito. r ↑ → m ↓.",
            azb("Retenção pelo público (c)") + ": o papel-moeda que fica no bolso “vaza” do circuito "
            "empréstimo → depósito → novo empréstimo. Só a parcela depositada é multiplicada. c ↑ → m ↓.",
            "Exemplo numérico: com c = 0,2 e r = 0,1, m = 1 / (0,2 + 0,08) ≈ " + vd("3,6") + "; se c sobe para "
            "0,4, m = 1 / (0,4 + 0,06) ≈ " + vd("2,2") + ".",
            "Casos-limite que ajudam a fixar: c = 1 (ninguém deposita) → m = 1; c = 0 → m = 1/r, o "
            + azb("multiplicador bancário simples") + ".",
            vm("Regra-âncora: tudo o que fica fora do circuito de crédito — no cofre do banco ou no bolso do "
               "público — reduz o multiplicador."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 1ª metade (reservas, razão inversa) está certa e "
                       "dá credibilidade; o erro foi enxertado na 2ª, invertendo o sinal da retenção pelo "
                       "público. 🔥 A banca alterna as duas variáveis e os sinais: decore que <b>ambas</b> são "
                       "inversas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O multiplicador varia na razão inversa tanto da taxa de reservas bancárias quanto da preferência "
            "do público por papel-moeda.”</i> → CERTO",
            "<i>“Se o público não retiver papel-moeda, o multiplicador será igual ao inverso da taxa de "
            "reservas.”</i> → CERTO",
            "<i>“A elevação do compulsório aumenta o multiplicador da base monetária.”</i> → ERRADO (sinal "
            "invertido)",
        ])],
        "reescrita": ("O valor do multiplicador da base monetária varia na razão inversa da taxa de reservas dos "
                      "bancos comerciais e na razão " + hl("inversa") + " da taxa de retenção da moeda pelo "
                      "público."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Multiplicador varia na razão inversa das reservas e também da retenção de moeda pelo "
                             "público; um dos comentários empilhados rotulava a retenção como “relação direta”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": FIG_E1("image (170).png"),
        "alertas": [BANCA_2013,
                    "qualidade_fonte: um dos comentários da fonte anota “relação direta” para a retenção pelo "
                    "público, contradizendo a própria explicação; corrigido"],
    },
    # ------------------------------------------------------------------ E1-0517
    {
        "id": "ECO-E1-0517-1", "fonte_ref": "E1-0517", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_M1_2013,
        "rotulo_item": "Item",
        "assertiva": ("O saldo de M1 é composto pelo saldo da moeda em poder do público somado ao saldo dos "
                      "depósitos à vista e aos depósitos de poupança."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O saldo de M1 é composto pelo saldo da moeda em poder do público somado ao saldo dos "
                       "depósitos à vista") + vm(" e aos depósitos de poupança") + az(".")),
        "poucas": (vd("M1 = PMPP + depósitos à vista") + ". Os " + azb("depósitos de poupança") + " rendem "
                   "juros e entram no " + vd("M2") + ", não no M1."),
        "destrinchando": [
            azb("M1 (meios de pagamento restritos)") + " reúne os haveres de liquidez imediata e "
            "<b>sem remuneração</b>: papel-moeda em poder do público (PMPP) e depósitos à vista nos bancos "
            "comerciais (moeda escritural).",
            "Os agregados seguintes ampliam o conceito em ordem decrescente de liquidez (metodologia do "
            + rx("Banco Central do Brasil") + ", pelo critério do emissor): " + vd("M2") + " = M1 + depósitos "
            "de poupança + títulos privados emitidos por instituições depositárias (CDB, LCI, LCA…); "
            + vd("M3") + " = M2 + cotas de fundos de renda fixa + operações compromissadas com títulos "
            "federais; " + vd("M4") + " = M3 + títulos públicos de alta liquidez.",
            "Critério que separa M1 do resto: a poupança é muito líquida, mas é um " + azb("quase-moeda") + ": "
            "para pagar com ela é preciso antes convertê-la em depósito à vista ou papel-moeda.",
            "A " + azb("base monetária") + " (PMPP + reservas bancárias) é outro conceito: é o passivo "
            "monetário do Banco Central, não um agregado de meios de pagamento do público.",
        ],
        "dissecando": (cz("[meia-verdade]") + " Os dois primeiros componentes estão certos; o item acrescenta um "
                       "terceiro que pertence ao agregado seguinte. Pista: “depósitos de poupança” rendem juros "
                       "— e M1 é, por definição, moeda que não rende."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os depósitos de poupança integram o M2, mas não o M1.”</i> → CERTO",
            "<i>“O M1 inclui os depósitos a prazo nos bancos comerciais.”</i> → ERRADO (depósito a prazo/CDB "
            "está no M2)",
        ])],
        "reescrita": ("O saldo de M1 é composto pelo saldo da moeda em poder do público somado ao saldo dos "
                      "depósitos à vista" + hl(", excluídos os depósitos de poupança") + "."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "M1 = PMPP + depósitos à vista; os depósitos de poupança compõem o M2.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_E1("image (167).png"),
        "alertas": [BANCA_2013],
    },
    # ------------------------------------------------------------------ E1-0518
    {
        "id": "ECO-E1-0518-1", "fonte_ref": "E1-0518", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_M1_2013,
        "rotulo_item": "Item",
        "assertiva": ("Em processos inflacionários, tende a diminuir a razão entre o volume de moeda em poder do "
                      "público e o volume de moeda bancária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em processos inflacionários, tende a ") + vm("diminuir") + az(" a razão entre o volume "
                    "de moeda em poder do público e o volume de moeda bancária.")),
        "poucas": ("Com inflação alta, os " + azb("depósitos à vista") + " migram para aplicações remuneradas "
                   "mais depressa que o papel-moeda, ainda indispensável nas compras do dia a dia: a razão "
                   + vd("PMPP/DV tende a aumentar") + "."),
        "destrinchando": [
            "Os dois componentes do M1 — papel-moeda em poder do público (PMPP) e depósitos à vista (moeda "
            "bancária ou escritural) — não rendem juros. Com inflação alta, ambos perdem poder de compra e o "
            "público reduz a demanda real pelos dois (" + azb("fuga da moeda") + ").",
            "A fuga, porém, é assimétrica. O saldo em conta corrente pode ser transferido com um clique para uma "
            "aplicação indexada (no " + rx("Brasil") + " dos anos 1980 e início dos 1990, o "
            + azb("overnight") + " e as contas remuneradas faziam isso automaticamente). Já o papel-moeda "
            "continua necessário nas transações miúdas e na economia informal. Resultado: DV encolhe mais que "
            "PMPP e a razão " + vd("c′ = PMPP/DV sobe") + ".",
            "Consequência para a oferta de moeda: c′ maior → " + azb("multiplicador monetário") + " menor "
            "(m = (1 + c′)/(c′ + r)). Inflação alta convive com M1 baixo em proporção do PIB "
            "(desmonetização); a estabilização do Plano Real, em 1994, foi seguida de forte "
            + azb("remonetização") + ".",
            "Distinga as duas razões que a banca mistura: a de " + vd("PMPP/DV") + " (dentro do M1) tende a "
            "subir; a de " + vd("M1/agregados amplos") + " (M1 sobre M2, M3, M4) tende a <b>cair</b>, porque o "
            "público troca moeda que não rende por quase-moedas remuneradas.",
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sentido da razão dentro do M1. A armadilha é "
                       "raciocinar só pela “fuga da moeda” (as duas parcelas caem) e esquecer que a moeda "
                       "bancária foge mais rápido. Pista: “volume de moeda em poder do público” fica no "
                       "<b>numerador</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em processos inflacionários, tende a diminuir a razão entre os meios de pagamento (M1) e os "
            "agregados monetários mais amplos.”</i> → CERTO",
            "<i>“Em processos inflacionários, o multiplicador monetário tende a aumentar, pois o público deposita "
            "mais nos bancos.”</i> → ERRADO (inversão: depósitos à vista encolhem e o multiplicador cai)",
        ])],
        "reescrita": ("Em processos inflacionários, tende a " + hl("aumentar") + " a razão entre o volume de moeda "
                      "em poder do público e o volume de moeda bancária."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 3,
        "comentario_fonte": ("Fonte com três justificativas divergentes: (1) inflação = mais moeda, o numerador "
                             "cresce mais; (2) M1 migra para aplicações remuneradas, caindo M1/aplicações; "
                             "(3) o público demanda mais papel-moeda, elevando PMPP/DV."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": FIG_E1("image (169).png"),
        "alertas": [BANCA_2013,
                    "qualidade_fonte: um comentário da fonte justifica o gabarito definindo inflação como "
                    "“aumento da quantidade de dinheiro”, raciocínio que não explica a razão PMPP/DV; substituído "
                    "pelo mecanismo da fuga assimétrica dos depósitos à vista"],
    },
    # ------------------------------------------------------------------ E1-0519
    {
        "id": "ECO-E1-0519-1", "fonte_ref": "E1-0519", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_M1_2013,
        "rotulo_item": "Item",
        "assertiva": "O resgate de um empréstimo bancário representa destruição de moeda.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O <u>resgate de um empréstimo bancário</u> representa <u>destruição de moeda</u>."),
        "poucas": ("Ao quitar o empréstimo, o público entrega ao banco um " + azb("haver monetário") + " (depósito "
                   "à vista ou papel-moeda) e recebe de volta um haver não monetário (a nota promissória): os "
                   "meios de pagamento " + vd("diminuem") + "."),
        "destrinchando": [
            "Regra de bolso dos manuais de economia monetária (" + oc("Lopes e Rossetti") + "): há "
            + azb("criação ou destruição de meios de pagamento") + " quando a operação ocorre entre o "
            "<b>setor bancário</b> (Banco Central + bancos comerciais) e o <b>setor não bancário</b> (público) "
            "e muda a quantidade de haveres monetários em poder do público.",
            "Criação: o público entrega um haver não monetário e recebe moeda — concessão de empréstimo, venda "
            "de dólares ou de títulos ao sistema bancário, desconto de duplicata. Destruição: o inverso — "
            + vd("resgate de empréstimo") + ", compra de títulos ou de dólares do sistema bancário, pagamento "
            "de tarifas e juros ao banco.",
            "Contabilmente, no pagamento do empréstimo o banco baixa o ativo (empréstimo) e o passivo "
            "(depósito à vista do devedor) ao mesmo tempo. O depósito sumiu e não reapareceu em conta de "
            "ninguém do público: M1 cai.",
            "Operações que <b>não</b> alteram M1: entre dois agentes do público (João paga Maria), entre "
            "bancos, ou trocas dentro do M1 (sacar papel-moeda de um depósito à vista apenas troca a forma da "
            "moeda).",
            "Precisão terminológica: o que se destrói é <b>meio de pagamento</b> (M1). O item diz “moeda”, uso "
            "consagrado na banca para M1.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz um exemplo da lista clássica de destruição de meios de "
                       "pagamento. O risco é achar que “devolver dinheiro ao banco” é neutro, porque o dinheiro "
                       "“continua existindo”. Teste rápido: o público ficou com mais ou menos moeda?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“A concessão de um empréstimo bancário a uma empresa representa criação de meios de "
            "pagamento.”</i> → CERTO",
            "<i>“O saque de papel-moeda de uma conta corrente representa destruição de meios de "
            "pagamento.”</i> → ERRADO (troca dentro do M1: DV → PMPP)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Empréstimo cria moeda; seu pagamento a destrói (baixa simultânea de ativo e passivo "
                             "do banco). Condições: operação entre setor bancário e não bancário e entrega de "
                             "haver monetário pelo público."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_E1("image (171).png"),
        "alertas": [BANCA_2013],
    },
    # ------------------------------------------------------------------ E1-0780
    {
        "id": "ECO-E1-0780-1", "fonte_ref": "E1-0780", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às funções da moeda no plano internacional.",
        "rotulo_item": "Item",
        "assertiva": ("A moeda de curso internacional deve ser capaz de desempenhar as funções de meio de "
                      "liquidação das transações e dos contratos, unidade de conta e reserva de valor; assim, a "
                      "confiança em uma moeda como reserva de valor pode ser medida pelo seu uso em reservas "
                      "oficiais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A moeda de curso internacional deve ser capaz de desempenhar as funções de meio de "
                      "liquidação das transações e dos contratos, unidade de conta e reserva de valor; assim, a "
                      "confiança em uma moeda como reserva de valor <u>pode ser medida</u> pelo seu uso em "
                      "<u>reservas oficiais</u>."),
        "poucas": ("Moeda internacional cumpre, no plano global, as " + azb("três funções clássicas") + "; a "
                   "fatia que ocupa nas " + azb("reservas oficiais") + " dos bancos centrais é o termômetro "
                   "usual da confiança nela como reserva de valor."),
        "destrinchando": [
            "Funções da moeda: " + azb("meio de troca") + " (liquidar transações e contratos), "
            + azb("unidade de conta") + " (medir e comparar valores) e " + azb("reserva de valor") + " (levar "
            "poder de compra para o futuro). O item chama o meio de troca de “meio de liquidação”, sinônimo "
            "aceito.",
            "No plano internacional, cada função tem um uso privado e um oficial (matriz de " + oc("Kenen")
            + " e " + oc("Cohen") + "): meio de troca → moeda-veículo do comércio e do câmbio / moeda de "
            "intervenção dos BCs; unidade de conta → faturamento de exportações e de commodities / âncora "
            "cambial; reserva de valor → aplicações financeiras privadas / " + vd("reservas oficiais") + ".",
            "Por que reservas medem confiança: um banco central só guarda reservas em moeda que preserve valor, "
            "tenha mercado profundo e líquido e emissor estável. Por isso o FMI acompanha a composição das "
            "reservas (base COFER) para avaliar a dominância do dólar e a ascensão de moedas não tradicionais.",
            "Ordem de grandeza ⏳ (out/2026): o " + vd("dólar") + " responde por cerca de " + vd("57–58%")
            + " das reservas alocadas (COFER, 2024–2025), seguido do " + vd("euro (~20%)") + "; iene, libra, "
            "dólar canadense, dólar australiano e renminbi têm fatias de um dígito.",
            rx("Brasil") + ": as reservas internacionais (perto de US$ 350 bilhões ⏳ (out/2026)) concentram-se "
            "em ativos em dólar, com parcelas em euro, renminbi e ouro, conforme o relatório de gestão de "
            "reservas do BCB.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item é dedutivo: as três funções estão "
                       "certas e o “assim” liga a reserva de valor ao uso em reservas oficiais, com o modulador "
                       "brando “pode ser medida”. A banca testaria o contrário trocando a função ligada às "
                       "reservas (“unidade de conta”) ou dizendo que basta uma das funções."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a confiança em uma moeda como unidade de conta pode ser medida pelo seu uso em reservas "
            "oficiais.”</i> → ERRADO (troca de função: reservas medem a reserva de valor)",
            "<i>“Para ter curso internacional, basta que a moeda funcione como meio de troca nas transações "
            "comerciais.”</i> → ERRADO (restrição indevida: as três funções)",
        ]), ("🃏 Carta na manga", [
            "Desdolarização é processo lento: o uso do dólar como reserva cai gradualmente desde 2000 (de cerca "
            "de 70% para menos de 60%), mas a perda se dispersa por várias moedas não tradicionais, não para "
            "um rival único — tema útil para discursivas sobre BRICS e sistema monetário internacional."])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "deve"],
        "dificuldade": 1,
        "comentario_fonte": ("Moeda internacional deve cumprir as três funções (meio de troca, unidade de conta, "
                             "reserva de valor); uso em reservas oficiais mede a confiança como reserva de valor "
                             "(FMI, blog sobre dominância do dólar, 2022)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_E1("image (276).png"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00082
    {
        "id": "ECO-E2-L00082-1", "fonte_ref": "E2-L00082", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_KEY,
        "rotulo_item": "Item",
        "assertiva": ("Dentro do pensamento keynesiano, a moeda não é considerada um elemento neutro, pois ela "
                      "possui um papel especulativo no sistema econômico, influenciando as taxas de juros e, "
                      "consequentemente, o investimento e a demanda agregada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Dentro do pensamento keynesiano, a moeda <u>não é considerada um elemento neutro</u>, pois "
                      "ela possui um <u>papel especulativo</u> no sistema econômico, influenciando as taxas de "
                      "juros e, consequentemente, o investimento e a demanda agregada."),
        "poucas": ("Para " + oc("Keynes") + ", a moeda é também " + azb("ativo") + " (reserva de valor): a "
                   "demanda especulativa faz os juros dependerem do mercado monetário, e os juros afetam "
                   "investimento, demanda agregada e renda — moeda " + vd("não neutra") + "."),
        "destrinchando": [
            azb("Neutralidade da moeda") + " (clássicos, " + azb("teoria quantitativa") + "): MV = PY, com V e "
            "Y dados pelo lado real; mais moeda só eleva preços. Juros se formam no mercado de fundos "
            "emprestáveis (poupança × investimento) e a moeda é um “véu”.",
            oc("Keynes") + " (<i>Teoria Geral</i>, 1936) acrescenta três motivos para reter moeda: transação, "
            "precaução e " + azb("especulação") + ". O especulativo depende inversamente dos juros: quem "
            "espera alta dos juros (queda no preço dos títulos) prefere ficar líquido.",
            "Canal de transmissão: oferta de moeda × " + azb("preferência pela liquidez") + " → taxa de juros "
            "→ investimento (comparado à " + azb("eficiência marginal do capital") + ") → demanda agregada → "
            "renda e emprego. A moeda mexe em variáveis reais.",
            "Limite do canal: na " + azb("armadilha da liquidez") + " a demanda especulativa é infinitamente "
            "elástica e mais moeda não reduz os juros — a política monetária perde eficácia.",
            "Na tradição pós-keynesiana, Keynes descreve uma " + azb("economia monetária de produção") + ": a "
            "moeda é ativo de segurança num mundo de incerteza radical, e não apenas meio de troca.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Resume a ruptura de Keynes com a teoria quantitativa. A "
                       "cadeia causal (especulação → juros → investimento → DA) é a do manual, sem "
                       "modulador absoluto. 🔥 O par neutralidade (clássicos) × não neutralidade (Keynes) é "
                       "recorrente; a banca costuma inverter os autores."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, a moeda não é neutra, pois a demanda especulativa determina a taxa de "
            "juros.”</i> → ERRADO (troca de ator: é a visão de Keynes)",
            "<i>“Para Keynes, a taxa de juros é determinada pelo equilíbrio entre poupança e "
            "investimento.”</i> → ERRADO (troca de conceito: é a teoria clássica dos fundos emprestáveis)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Keynes: moeda tem papel especulativo e afeta juros e investimento; difere da visão "
                             "clássica de neutralidade."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00107
    {
        "id": "ECO-E2-L00107-1", "fonte_ref": "E2-L00107", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_MULT,
        "rotulo_item": "Item",
        "assertiva": ("A base monetária é formada apenas pelo papel moeda em poder do público e não inclui o "
                      "encaixe bancário, uma vez que este representa apenas uma retenção temporária de depósitos "
                      "pelos bancos comerciais, sem integrar efetivamente o conceito de base monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A base monetária é formada ") + vm("apenas") + az(" pelo papel moeda em poder do público ")
                    + vm("e não inclui o encaixe bancário, uma vez que este representa apenas uma retenção "
                         "temporária de depósitos pelos bancos comerciais, sem integrar efetivamente o conceito "
                         "de base monetária") + az(".")),
        "poucas": (vd("Base monetária = PMPP + reservas bancárias") + " (encaixe em moeda corrente + depósitos "
                   "dos bancos no Banco Central). Excluir o encaixe é o erro."),
        "destrinchando": [
            azb("Base monetária") + " (B) é a " + azb("moeda de alta potência") + ": o passivo monetário do "
            "Banco Central. Pela ótica dos usos: " + vd("B = PMPP + R") + ", em que R = encaixe dos bancos em "
            "moeda corrente (caixa) + reservas compulsórias e voluntárias em espécie depositadas no BC.",
            "Pela ótica das fontes, B varia com as operações do BC: compra de títulos ou de divisas e "
            "redesconto a expandem; venda de títulos ou de divisas a contraem.",
            "Por que as reservas entram: elas são o “combustível” do multiplicador. O BC controla B; o sistema "
            "bancário e o público determinam quanto de B vira M1: " + vd("M1 = m · B") + ".",
            "Contraste com o M1: os encaixes <b>não</b> entram no M1 (não estão com o público), mas entram na "
            "base. Já os depósitos à vista entram no M1 e não na base. É essa assimetria que permite m > 1.",
            vm("Regra-âncora: base = PMPP + reservas; M1 = PMPP + depósitos à vista."),
        ],
        "dissecando": (cz("[restrição indevida · troca de conceito]") + " O “apenas” amputa metade da "
                       "definição, e a justificativa inventa um critério (“retenção temporária”) para excluir "
                       "as reservas. Pista: justificativa longa para uma definição contábil costuma esconder "
                       "o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A base monetária compreende o papel-moeda em poder do público e as reservas bancárias.”</i> → "
            "CERTO",
            "<i>“Os depósitos à vista integram tanto a base monetária quanto os meios de pagamento.”</i> → "
            "ERRADO (depósitos à vista estão no M1, não na base)",
        ])],
        "reescrita": ("A base monetária é formada " + "<s>apenas</s>" + " pelo papel moeda em poder do público "
                      + hl("e pelo encaixe bancário (caixa dos bancos e reservas no Banco Central), que integra "
                           "efetivamente o conceito de base monetária") + "."),
        "tipo_erro": ["RESTRICAO", "TROCA_CONCEITO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": "Base monetária = PMPP + encaixe bancário (reservas); o encaixe integra a base.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00108
    {
        "id": "ECO-E2-L00108-1", "fonte_ref": "E2-L00108", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_MULT,
        "rotulo_item": "Item",
        "assertiva": "O efeito multiplicador bancário é diretamente influenciado pelo volume de depósitos à vista.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O efeito multiplicador bancário é <u>diretamente</u> influenciado pelo volume de depósitos "
                      "à vista."),
        "poucas": ("Só a parte do M1 que fica nos bancos como " + azb("depósito à vista") + " pode ser "
                   "reemprestada e multiplicada: quanto maior essa parcela, " + vd("maior o multiplicador") + "."),
        "destrinchando": [
            "Mecanismo: o depósito vira reserva; o banco guarda a fração R e empresta o resto; o tomador gasta, "
            "o recebedor deposita parte do que recebeu, e o ciclo recomeça. Cada rodada gera nova "
            + azb("moeda escritural") + ".",
            "Fórmula com d = DV/M1 (fração dos meios de pagamento mantida em depósitos à vista) e R = "
            "encaixe/DV: " + vd("m = 1 / [1 − d(1 − R)]") + ". O multiplicador cresce com d e cai com R.",
            "Exemplo: R = 0,2. Com d = 0,5, m = 1 / (1 − 0,4) ≈ " + vd("1,67") + "; com d = 0,8, m = "
            "1 / (1 − 0,64) ≈ " + vd("2,78") + ".",
            "Precisão: o que pesa no multiplicador é a <b>proporção</b> de depósitos no M1 (o hábito do público), "
            "não o volume absoluto; mais depósitos com a mesma proporção aumentam o M1, não o m. O item usa "
            "“volume” no sentido corrente de cursinho, e o gabarito CERTO se sustenta pela relação direta.",
            vm("Regra-âncora: depósitos à vista alimentam o multiplicador; encaixes e papel-moeda em poder do "
               "público o drenam."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de sinal: a única coisa a decidir é se a relação é direta "
                       "ou inversa. A banca costuma montar a série trocando o sinal de uma das três variáveis "
                       "(depósitos +, encaixe −, papel-moeda −)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O efeito multiplicador bancário é inversamente influenciado pelo volume de depósitos à "
            "vista.”</i> → ERRADO (sinal invertido)",
            "<i>“Mantida a base monetária, a migração de papel-moeda para depósitos à vista eleva os meios de "
            "pagamento.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Mais depósitos à vista → mais recursos para empréstimos → multiplicador maior.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00109
    {
        "id": "ECO-E2-L00109-1", "fonte_ref": "E2-L00109", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_MULT,
        "rotulo_item": "Item",
        "assertiva": ("A quantidade de papel moeda em poder do público impacta o efeito multiplicador bancário "
                      "negativamente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A quantidade de papel moeda em poder do público impacta o efeito multiplicador bancário "
                      "<u>negativamente</u>."),
        "poucas": ("O " + azb("papel-moeda em poder do público") + " é um “vazamento”: fica fora dos bancos e não "
                   "vira empréstimo. Mais PMPP em relação ao M1 → " + vd("multiplicador menor") + "."),
        "destrinchando": [
            "Com c = PMPP/M1 e r = reservas/DV: " + vd("m = 1 / [c + r(1 − c)]") + ". Derivando, m cai quando c "
            "sobe (para qualquer r < 1).",
            "Intuição: um real sacado e guardado na carteira para de circular pelo sistema bancário; um real "
            "depositado vira reserva, e parte dele é reemprestada várias vezes.",
            "Exemplo: r = 0,1. Com c = 0,2, m ≈ " + vd("3,6") + "; com c = 0,5, m = 1 / (0,5 + 0,05) ≈ "
            + vd("1,8") + ".",
            "Determinantes de c: hábitos de pagamento, informalidade, bancarização, custo de usar bancos, "
            "inflação e tecnologia. A digitalização dos pagamentos (no " + rx("Brasil") + ", o Pix, desde "
            "2020) tende a reduzir c.",
            "Os três parâmetros: o " + azb("Banco Central") + " controla a base e o compulsório; os "
            + azb("bancos") + " decidem as reservas voluntárias; o " + azb("público") + " decide c. Por isso "
            "o multiplicador não é inteiramente controlável pela autoridade monetária.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de sinal, sem modulador. Leitura atenta: “quantidade” de "
                       "papel-moeda, tecnicamente, é a preferência do público por papel-moeda (razão c), não o "
                       "estoque absoluto — a banca usa os termos como sinônimos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a preferência do público por manter papel-moeda, maior o multiplicador "
            "bancário.”</i> → ERRADO (sinal invertido)",
            "<i>“Se o público não retém papel-moeda, o multiplicador é o inverso da taxa de reservas.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Mais PMPP → menos recursos nos bancos → menor multiplicação.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00110
    {
        "id": "ECO-E2-L00110-1", "fonte_ref": "E2-L00110", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_MULT,
        "rotulo_item": "Item",
        "assertiva": ("O R maiúsculo, representando o percentual dos depósitos à vista que é retido como encaixe "
                      "bancário na fórmula do multiplicador monetário (m = 1 / 1 − d (1 − R)), aumenta a "
                      "multiplicação monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O R maiúsculo, representando o percentual dos depósitos à vista que é retido como encaixe "
                       "bancário na fórmula do multiplicador monetário (m = 1 / 1 − d (1 − R)), ")
                    + vm("aumenta") + az(" a multiplicação monetária.")),
        "poucas": ("R é o " + azb("encaixe") + ": quanto mais os bancos retêm, menos emprestam. R ↑ → (1 − R) ↓ → "
                   "denominador ↑ → " + vd("m ↓") + "."),
        "destrinchando": [
            "Leitura da fórmula " + vd("m = 1 / [1 − d(1 − R)]") + ": d = DV/M1 é a fração dos meios de "
            "pagamento mantida como depósito à vista; R = encaixe/DV (reservas compulsórias + voluntárias). "
            "O termo d(1 − R) é a fração de cada real que “volta” ao banco e pode ser reemprestada.",
            "Exemplo com d = 0,8: R = 0,2 → m = 1 / (1 − 0,64) ≈ " + vd("2,78") + "; R = 0,4 → m = "
            "1 / (1 − 0,48) ≈ " + vd("1,92") + ". O encaixe subiu e o multiplicador caiu.",
            "Casos-limite: R = 1 (banco guarda tudo, “100% reserve banking”) → m = 1 / (1 − 0) = " + vd("1")
            + ", não há multiplicação; R = 0 → m = 1/(1 − d), máximo dado o hábito do público.",
            "Instrumento: o " + azb("recolhimento compulsório") + " é a parte de R fixada pelo Banco Central. "
            "Elevá-lo é política monetária contracionista: reduz m e, com a base dada, o M1.",
            vm("Regra-âncora: encaixe e retenção pelo público reduzem o multiplicador; depósitos à vista o "
               "ampliam."),
        ],
        "dissecando": (cz("[inversão]") + " O item define R corretamente e inverte só o efeito. A fórmula na "
                       "frente intimida, mas basta testar dois valores de R. 🔥 A banca adora pôr a fórmula na "
                       "frente para quem não conhece a intuição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na fórmula m = 1 / [1 − d(1 − R)], a elevação de d aumenta o multiplicador.”</i> → CERTO",
            "<i>“A redução do compulsório sobre depósitos à vista reduz o multiplicador monetário.”</i> → ERRADO "
            "(sinal invertido: aumenta)",
        ])],
        "reescrita": ("O R maiúsculo, representando o percentual dos depósitos à vista que é retido como encaixe "
                      "bancário na fórmula do multiplicador monetário (m = 1 / 1 − d (1 − R)), " + hl("reduz")
                      + " a multiplicação monetária."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Quanto maior R, menos os bancos emprestam e menor o multiplicador.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00124
    {
        "id": "ECO-E2-L00124-1", "fonte_ref": "E2-L00124", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_MERC,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de curso forçado da moeda implica que apenas o governo pode determinar sua "
                      "validade como meio de troca em um país, garantindo que a moeda nacional seja a única "
                      "utilizada para transações comerciais dentro do território nacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O conceito de curso forçado da moeda implica que <u>apenas o governo</u> pode determinar sua "
                      "validade como meio de troca em um país, garantindo que a moeda nacional seja <u>a única</u> "
                      "utilizada para transações comerciais dentro do território nacional."),
        "poucas": ("A banca leu " + azb("curso forçado") + " como monopólio estatal da moeda de pagamento: o "
                   "Estado define a moeda que liquida obrigações no país, e ninguém pode recusá-la."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "na terminologia técnica, " + azb("curso forçado") + " é a " + vm("inconversibilidade")
                          + " (o emissor não troca a nota por ouro), e a aceitação obrigatória é o "
                          + azb("curso legal") + ". Além disso, “a única utilizada” é forte: a lei admite "
                          "pagamentos em moeda estrangeira em hipóteses especiais (comércio exterior, por "
                          "exemplo). O CERTO só se sustenta na acepção corrente, que funde os dois conceitos.")],
        "destrinchando": [
            azb("Curso legal") + ": a moeda tem " + azb("poder liberatório") + " — o credor não pode recusá-la "
            "para quitar dívidas no território. " + azb("Curso forçado") + ": a moeda circula sem "
            "conversibilidade em metal; seu valor repousa na lei e na confiança (" + azb("moeda fiduciária")
            + "). Hoje as duas características andam juntas, e muitos manuais tratam os termos como sinônimos.",
            "Histórico: o curso forçado nasce como medida de emergência (suspensão da conversibilidade em "
            "guerras e crises) e se generaliza no século XX, com o fim do padrão-ouro e, em 1971, da "
            "conversibilidade do dólar em ouro.",
            rx("Brasil") + ": o Real tem curso legal em todo o território nacional (" + vd("Lei 9.069/1995")
            + "); o Código Civil exige que dívidas em dinheiro sejam pagas em moeda corrente pelo valor "
            "nominal (" + vd("art. 315") + ") e anula, salvo legislação especial, cláusulas de pagamento em "
            "ouro ou moeda estrangeira (" + vd("art. 318") + ").",
            "Exceções reais ao “única”: contratos de importação e exportação, operações de câmbio e outras "
            "hipóteses previstas na legislação cambial. Fora delas, prevalece o Real.",
            "Ligação com as funções da moeda: o curso legal garante a função de " + azb("meio de pagamento")
            + " e de " + azb("unidade de conta") + "; a função de reserva de valor depende da credibilidade "
            "do emissor, que a lei não garante.",
        ],
        "dissecando": (cz("[literalidade · outro: conceito usado em sentido lato]") + " O item usa a acepção "
                       "corrente de curso forçado (aceitação obrigatória) e dois absolutos (“apenas”, “a "
                       "única”). Em cursinho, o CERTO prevalece; numa prova do CEBRASPE, o par curso legal × "
                       "curso forçado pode ser cobrado com rigor — guarde a distinção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Curso forçado significa que a moeda não é conversível em ouro por seu emissor.”</i> → CERTO",
            "<i>“O curso legal do Real impede, sem exceção, contratos em moeda estrangeira no Brasil.”</i> → "
            "ERRADO (modulador absoluto: há exceções legais)",
        ])],
        "tipo_erro": ["LITERAL", "OUTRO"], "moduladores": ["apenas", "única"], "dificuldade": 2,
        "comentario_fonte": ("Curso forçado garante aceitação do Real em todo o território e impede o uso de "
                             "outras moedas nas transações diárias."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: o item descreve o curso legal (poder liberatório) sob o nome de curso forçado "
                    "(inconversibilidade) e afirma exclusividade que a legislação cambial excepciona; mantido "
                    "o CERTO da fonte"],
    },
    # ------------------------------------------------------------------ E2-L00125
    {
        "id": "ECO-E2-L00125-1", "fonte_ref": "E2-L00125", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_MERC,
        "rotulo_item": "Item",
        "assertiva": ("A demanda de moeda pelo público não bancário é influenciada por variáveis como renda, taxa "
                      "de juros e inflação. Aumentos na renda elevam a demanda por moeda, pois os indivíduos "
                      "tendem a gastar mais à medida que seu poder aquisitivo cresce. Da mesma forma, quando a "
                      "taxa de juros aumenta, a demanda por moeda aumenta porque as pessoas preferem manter moeda "
                      "em vez de gastá-la ou aplicá-la em outras opções que ofereçam maior rendimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A demanda de moeda pelo público não bancário é influenciada por variáveis como renda, taxa "
                       "de juros e inflação. Aumentos na renda elevam a demanda por moeda, pois os indivíduos "
                       "tendem a gastar mais à medida que seu poder aquisitivo cresce. ") + vm("Da mesma forma")
                    + az(", quando a taxa de juros aumenta, a demanda por moeda ") + vm("aumenta porque as "
                    "pessoas preferem manter moeda em vez de gastá-la ou aplicá-la em outras opções que "
                    "ofereçam maior rendimento") + az(".")),
        "poucas": ("Renda e demanda por moeda andam juntas (" + azb("motivo transação") + "); juros e demanda "
                   "por moeda andam em " + vd("sentido oposto") + ": juro é o " + azb("custo de oportunidade")
                   + " de ficar com moeda."),
        "destrinchando": [
            "Função demanda por moeda: " + vd("Mᵈ/P = L(Y, i)") + ", crescente em Y e decrescente em i. Em "
            + oc("Keynes") + ": transação e precaução dependem da renda; especulação, dos juros.",
            "Renda ↑ → mais transações a liquidar → mais moeda retida. Essa parte do item está certa.",
            "Juros ↑ → títulos e depósitos remunerados rendem mais; reter moeda (que não rende) custa mais → "
            "o público " + vd("reduz") + " a demanda por moeda. Na versão especulativa, juros altos também "
            "sinalizam que tendem a cair, e quem espera queda de juros compra títulos (que se valorizarão).",
            "Inflação esperada também eleva o custo de reter moeda e, em termos reais, reduz a demanda (efeito "
            "estudado por " + oc("Cagan") + " nas hiperinflações).",
            "Graficamente: a curva L(i) é negativamente inclinada no plano (M/P, i); renda maior a desloca para a "
            "direita. Esse é o lado de demanda da curva LM.",
            vm("Regra-âncora: Y ↑ → Mᵈ ↑; i ↑ → Mᵈ ↓."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " As duas primeiras frases estão certas; o “da mesma "
                       "forma” prepara a inversão do sinal dos juros. A própria justificativa se contradiz: "
                       "ninguém prefere ficar com moeda justamente quando as outras opções rendem mais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação da taxa de juros reduz a demanda por moeda, por aumentar o custo de oportunidade de "
            "retê-la.”</i> → CERTO",
            "<i>“Na armadilha da liquidez, a demanda por moeda é totalmente insensível à taxa de juros.”</i> → "
            "ERRADO (é infinitamente elástica aos juros)",
        ])],
        "reescrita": ("A demanda de moeda pelo público não bancário é influenciada por variáveis como renda, taxa "
                      "de juros e inflação. Aumentos na renda elevam a demanda por moeda, pois os indivíduos "
                      "tendem a gastar mais à medida que seu poder aquisitivo cresce. " + hl("Em sentido oposto")
                      + ", quando a taxa de juros aumenta, a demanda por moeda " + hl("diminui porque as pessoas "
                      "preferem aplicá-la em outras opções que ofereçam maior rendimento em vez de mantê-la")
                      + "."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Alta dos juros reduz a demanda por moeda; relação inversa com a taxa de juros.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “aplicála” → “aplicá-la” (erro de digitação da fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00128
    {
        "id": "ECO-E2-L00128-1", "fonte_ref": "E2-L00128", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_AGR,
        "rotulo_item": "Item",
        "assertiva": ("M3 inclui instituições como fundos de investimento, e sua especialização é crucial para a "
                      "dinâmica bancária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("M3 inclui <u>instituições como fundos de investimento</u>, e sua especialização é crucial "
                      "para a dinâmica bancária."),
        "poucas": ("Pelo critério do " + azb("emissor") + " adotado pelo Banco Central, o " + vd("M3")
                   + " acrescenta ao M2 os haveres emitidos pelos " + azb("fundos de renda fixa") + " (cotas) e "
                   "as operações compromissadas com títulos federais."),
        "destrinchando": [
            "Os agregados do " + rx("Banco Central do Brasil") + " (metodologia de 2001) se organizam pelo "
            "<b>sistema emissor</b> do haver: " + vd("M1") + " = haveres das instituições emissoras de haveres "
            "monetários (PMPP + depósitos à vista); " + vd("M2") + " = M1 + depósitos de poupança e títulos "
            "privados das instituições depositárias; " + vd("M3") + " = M2 + cotas de fundos de renda fixa e "
            "operações compromissadas registradas no Selic; " + vd("M4") + " = M3 + títulos públicos de alta "
            "liquidez.",
            "Por isso a frase “M3 inclui instituições como fundos” é aceitável: o agregado inclui os haveres "
            "<b>emitidos</b> por elas. Rigorosamente, agregado é soma de haveres financeiros, não de "
            "instituições.",
            "Por que os fundos interessam à política monetária: as cotas de fundos de renda fixa são "
            + azb("quase-moedas") + " de alta liquidez (resgate em D+0 ou D+1). Se o público migra de "
            "depósitos para fundos, o M1 encolhe, mas a liquidez total da economia pouco muda.",
            "A ordem M1 → M4 é de " + azb("liquidez decrescente") + " e de remuneração crescente.",
        ],
        "dissecando": (cz("[paráfrase fiel · outro: redação imprecisa]") + " A 1ª oração vem do critério do emissor; "
                       "a 2ª (“especialização crucial”) é genérica e não tem como ser falsa. Itens assim, de "
                       "cursinho, raramente são ERRADO; o risco seria a banca trocar o agregado (M2 ou M4)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As cotas de fundos de renda fixa integram o M2.”</i> → ERRADO (dado alterado: integram o M3)",
            "<i>“Os títulos públicos federais de alta liquidez em poder do público só aparecem no M4.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "OUTRO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O M3 engloba fundos de investimento e instituições de gestão de fundos, "
                             "especializadas em produtos mais sofisticados que os bancários tradicionais."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00129
    {
        "id": "ECO-E2-L00129-1", "fonte_ref": "E2-L00129", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_AGR,
        "rotulo_item": "Item",
        "assertiva": ("A demanda por moeda é bastante influenciada pela renda, pela inflação e pelas taxas de "
                      "juros, de modo que uma elevação na inflação tende a diminuir a demanda por moeda ao "
                      "incentivar a população a poupar para proteger seu poder de compra."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("A demanda por moeda é bastante influenciada pela renda, pela inflação e pelas taxas de "
                       "juros, de modo que uma elevação na inflação tende a ") + vm("diminuir a demanda por moeda "
                       "ao incentivar a população a poupar para proteger seu poder de compra") + az(".")),
        "poucas": ("Pela leitura da banca, preços em alta exigem " + vd("mais moeda nominal") + " para as mesmas "
                   "compras: a demanda <b>nominal</b> por moeda sobe com a inflação, e o mecanismo de “poupar” "
                   "não descreve o efeito."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "em termos <b>reais</b>, a teoria diz o contrário: inflação esperada maior eleva o "
                          "custo de reter moeda e " + vm("reduz a demanda real por moeda") + " (" + oc("Cagan")
                          + ", hiperinflações; “fuga da moeda”). Lido assim, o “tende a diminuir” é defensável; "
                          "o que continua impreciso é o motivo: o público não “poupa” mais, troca moeda por "
                          "ativos reais ou indexados. Mantido o ERRADO da fonte.")],
        "destrinchando": [
            "Separe dois efeitos. " + azb("Nível de preços") + ": Mᵈ = P · L(Y, i). Se P sobe, a demanda "
            + vd("nominal") + " sobe na mesma proporção, para comprar a mesma cesta (é o raciocínio da fonte).",
            azb("Taxa de inflação esperada") + ": é parte do custo de reter moeda, pois i ≈ r + πᵉ (" + oc("Fisher")
            + "). πᵉ ↑ → a moeda perde valor mais depressa → o público reduz os " + vd("saldos reais") + " "
            "(M/P), gasta mais rápido e foge para ativos reais, moeda estrangeira ou aplicações indexadas.",
            "Consequência do 2º efeito: a " + azb("velocidade de circulação") + " sobe. Nas hiperinflações, os "
            "saldos reais despencam; no " + rx("Brasil") + " da alta inflação, isso apareceu como "
            "desmonetização da economia e uso maciço de aplicações indexadas de curtíssimo prazo.",
            "Leitura da assertiva: ela fala de “demanda por moeda” sem dizer nominal ou real e oferece um "
            "mecanismo fraco (“poupar”). O gabarito ERRADO da fonte só se sustenta pela ótica nominal.",
            vm("Regra-âncora: P ↑ → demanda nominal ↑; πᵉ ↑ → demanda real ↓."),
        ],
        "dissecando": (cz("[inversão · outro: ambiguidade nominal × real]") + " O item mistura o efeito sobre a "
                       "demanda real (que cai) com a justificativa de “poupar” (que não é o mecanismo). Diante "
                       "de “demanda por moeda” e “inflação”, pergunte sempre: <b>nominal ou real?</b> — é aí que "
                       "o gabarito se decide."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma elevação da inflação esperada tende a reduzir a demanda por saldos monetários reais.”</i> → "
            "CERTO",
            "<i>“Uma elevação do nível de preços reduz a demanda nominal por moeda.”</i> → ERRADO (inversão: a "
            "demanda nominal sobe com P)",
        ])],
        "reescrita": ("A demanda por moeda é bastante influenciada pela renda, pela inflação e pelas taxas de "
                      "juros, de modo que uma elevação na inflação tende a " + hl("elevar a demanda nominal por "
                      "moeda, pois a população precisa de mais unidades monetárias para realizar as mesmas "
                      "transações") + "."),
        "tipo_erro": ["INVERSAO", "OUTRO"], "moduladores": ["tende a"], "dificuldade": 3,
        "comentario_fonte": ("Inflação eleva a demanda por moeda: com preços mais altos, a população precisa de "
                             "mais dinheiro para as mesmas compras."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: pela ótica real (Cagan; custo de oportunidade da inflação esperada) a demanda "
                    "por moeda cai com a inflação; o ERRADO da fonte depende da leitura nominal"],
    },
    # ------------------------------------------------------------------ E2-L00130
    {
        "id": "ECO-E2-L00130-1", "fonte_ref": "E2-L00130", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_AGR,
        "rotulo_item": "Item",
        "assertiva": ("O M2 diferencia-se do M1 principalmente pela inclusão de depósitos a prazo, como poupanças e "
                      "CDBs, e incorpora instituições como sociedades de crédito imobiliário, que são fundamentais "
                      "no financiamento habitacional e não apenas bancos comerciais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O M2 diferencia-se do M1 principalmente pela inclusão de <u>depósitos a prazo, como "
                      "poupanças e CDBs</u>, e incorpora instituições como <u>sociedades de crédito "
                      "imobiliário</u>, que são fundamentais no financiamento habitacional e não apenas bancos "
                      "comerciais."),
        "poucas": (vd("M2 = M1 + depósitos de poupança + títulos privados") + " (CDB, letras de câmbio, letras "
                   "imobiliárias…) emitidos pelas " + azb("instituições depositárias") + " — bancos e também "
                   "SCI, APE, financeiras."),
        "destrinchando": [
            "O M1 só tem haveres das " + azb("instituições emissoras de haveres monetários") + " (BC e bancos "
            "que captam depósito à vista). O M2 alarga o círculo para as " + azb("instituições depositárias")
            + ": bancos múltiplos e comerciais, caixas econômicas, " + azb("sociedades de crédito imobiliário")
            + ", associações de poupança e empréstimo, sociedades de crédito, financiamento e investimento.",
            "Componentes acrescentados: depósitos de " + vd("poupança") + " (recursos que lastreiam o "
            "financiamento habitacional do SBPE) e títulos privados como " + vd("CDB, RDB, LCI, LCA e letras de "
            "câmbio") + ".",
            "Precisão: a poupança não é tecnicamente “depósito a prazo” (não tem prazo fixo, rende por "
            "aniversário mensal); o item a agrupa com o CDB no sentido de aplicação remunerada. A ideia central "
            "— M2 = M1 + quase-moedas bancárias — está correta.",
            "Lógica dos agregados: cada degrau acrescenta haveres <b>menos líquidos e remunerados</b>. M1 não "
            "rende; do M2 em diante, tudo rende juros.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Item longo, mas certo: a 1ª parte dá a composição do "
                       "M2 e a 2ª, o critério do emissor (instituições depositárias). A “poupança como depósito "
                       "a prazo” é imprecisão tolerada. A banca inverteria pondo esses itens no M1 ou no M3."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O M2 difere do M1 pela inclusão das cotas de fundos de renda fixa.”</i> → ERRADO (dado alterado: "
            "cotas de fundos estão no M3)",
            "<i>“Os depósitos de poupança integram o M2.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["principalmente"], "dificuldade": 1,
        "comentario_fonte": ("M2 engloba poupança e CDB e inclui sociedades de crédito imobiliário, importantes no "
                             "financiamento habitacional."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00131
    {
        "id": "ECO-E2-L00131-1", "fonte_ref": "E2-L00131", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_AGR,
        "rotulo_item": "Item",
        "assertiva": ("A oferta monetária é uma variável endógena na visão keynesiana, uma vez que depende "
                      "diretamente da política monetária do Banco Central, que ajusta a base monetária de acordo "
                      "com mudanças na taxa de juros para alcançar o equilíbrio desejado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A oferta monetária é uma variável ") + vm("endógena") + az(" na visão keynesiana, uma vez "
                    "que depende diretamente da política monetária do Banco Central, que ajusta a base monetária ")
                    + vm("de acordo com mudanças na taxa de juros") + az(" para alcançar o equilíbrio desejado.")),
        "poucas": ("No modelo keynesiano de manual (" + oc("Keynes") + ", IS-LM), a oferta de moeda é "
                   + vd("exógena") + ": o Banco Central a fixa, e os juros resultam dela. Moeda "
                   + azb("endógena") + " é tese " + azb("pós-keynesiana") + "."),
        "destrinchando": [
            azb("Exógena") + " = determinada fora do modelo, por decisão da autoridade monetária; a curva de "
            "oferta de moeda é vertical no plano (M/P, i). É assim na <i>Teoria Geral</i> (1936) e no IS-LM de "
            + oc("Hicks") + ": o BC fixa M, a preferência pela liquidez dá a demanda, e o cruzamento dá os "
            "juros.",
            azb("Endógena") + " = determinada pela própria economia: a demanda por crédito cria depósitos "
            "(“empréstimos criam depósitos”), e o BC, que fixa a <b>taxa de juros</b>, acomoda a demanda por "
            "reservas. É a tese de " + oc("Kaldor") + " e " + oc("Moore") + " (horizontalistas), e a descrição "
            "operacional dos BCs modernos com meta de juros.",
            "Contradição interna do item: “depende diretamente da política monetária do BC” é argumento de "
            "<b>exogeneidade</b>; “ajusta a base de acordo com a taxa de juros” já é endogeneidade. Só a "
            "rotulagem keynesiana + exógena fecha.",
            "Na prática do " + rx("Brasil") + ": o Copom fixa a meta da Selic, e o BC ajusta a liquidez por "
            "operações compromissadas para manter a taxa na meta. A quantidade de moeda vira consequência — "
            "por isso o debate exógena × endógena é cobrado em CACD.",
        ],
        "dissecando": (cz("[troca de conceito · troca de ator]") + " O item cola o rótulo pós-keynesiano "
                       "(endógena) na visão keynesiana tradicional e justifica com o mecanismo oposto. Pista: "
                       "“depende do Banco Central” é a definição de exógena."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para os pós-keynesianos horizontalistas, a oferta de moeda é endógena, determinada pela "
            "demanda por crédito.”</i> → CERTO",
            "<i>“No modelo IS-LM, a oferta de moeda depende da taxa de juros.”</i> → ERRADO (troca de conceito: "
            "é exógena, curva vertical)",
        ])],
        "reescrita": ("A oferta monetária é uma variável " + hl("exógena") + " na visão keynesiana, uma vez que "
                      "depende diretamente da política monetária do Banco Central, que ajusta a base monetária "
                      + hl("de forma autônoma, determinando a taxa de juros") + " para alcançar o equilíbrio "
                      "desejado."),
        "tipo_erro": ["TROCA_CONCEITO", "TROCA_ATOR"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Oferta monetária é exógena, determinada unilateralmente pelo Banco Central; a "
                             "política monetária influencia os juros, mas a quantidade de moeda não depende deles."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00309
    {
        "id": "ECO-E2-L00309-1", "fonte_ref": "E2-L00309", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A instituição do PIX aumenta o efeito do multiplicador bancário, uma vez que a menor "
                      "retenção de papel moeda pelo público eleva a capacidade dos bancos de conceder crédito."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("A instituição do PIX ") + vm("aumenta") + az(" o efeito do multiplicador bancário, uma vez "
                    "que a menor retenção de papel moeda pelo público eleva a capacidade dos bancos de conceder "
                    "crédito.")),
        "poucas": ("Para a banca, o efeito é " + azb("ambíguo") + ": o Pix reduz a retenção de papel-moeda (c ↓, "
                   "m ↑), mas eleva a necessidade de " + azb("reservas") + " para liquidar pagamentos "
                   "instantâneos (r ↑, m ↓). Por isso o “aumenta” categórico seria ERRADO."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "no modelo-padrão do multiplicador, a assertiva é " + vm("mais defensável como CERTA")
                          + ": c ↓ eleva m com r dado (ceteris paribus). O aumento de r é hipótese "
                          "operacional — liquidez intradia para o SPI — e não consequência necessária: um Pix "
                          "apenas transfere reservas de um banco para outro, sem elevar a razão "
                          "reservas/depósitos do sistema. Gabarito oficial do curso mantido.")],
        "destrinchando": [
            "Fórmula: " + vd("m = 1 / [c + r(1 − c)]") + " (c = PMPP/M1; r = reservas/DV), ou na forma "
            + vd("m = (1 + c′)/(c′ + r)") + " com c′ = PMPP/DV. m cai com c e com r.",
            "Canal a favor da assertiva: pagamento instantâneo, gratuito e 24/7 substitui dinheiro vivo nas "
            "compras miúdas. Menos papel-moeda “vazando” do sistema → mais depósitos → maior capacidade de "
            "expansão do crédito e da moeda escritural.",
            "Canal contrário (o do gabarito): o Pix liquida em tempo real na conta Reservas Bancárias ou na conta "
            "PI do Banco Central. Bancos podem querer manter mais saldo para honrar picos de saídas, inclusive à "
            "noite e nos fins de semana — r voluntário ↑ → m ↓. O efeito líquido depende da magnitude de cada "
            "canal.",
            "Diferença entre “pode aumentar” e “aumenta”: a 1ª formulação seria incontestável; a 2ª exige que o "
            "efeito líquido seja positivo. É essa a brecha usada pelo curso para marcar ERRADO.",
            "Ressalva moderna: bancos não emprestam “depósitos recebidos”; o crédito depende de demanda, risco, "
            "capital regulatório e da taxa de juros fixada pelo BC. O multiplicador é identidade contábil, não "
            "lei de comportamento.",
            rx("Brasil") + ": o Pix foi lançado pelo BCB em " + vd("novembro de 2020") + " e tornou-se o meio "
            "de pagamento mais usado do país, com queda da participação do papel-moeda nas transações.",
        ],
        "dissecando": (cz("[outro: efeito ambíguo afirmado como certo · nexo indevido]") + " A justificativa "
                       "(c ↓ → m ↑) é a do manual, o que leva a marcar CERTO; o curso cobra a outra metade do "
                       "mecanismo (reservas de liquidação). Em prova do CEBRASPE, o “aumenta” seria lido pelo "
                       "modelo-padrão — a polêmica é de cursinho."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A difusão do Pix pode ampliar o multiplicador bancário, na medida em que reduz a preferência do "
            "público por papel-moeda.”</i> → CERTO",
            "<i>“O Pix eleva o multiplicador porque reduz o recolhimento compulsório sobre depósitos à "
            "vista.”</i> → ERRADO (nexo indevido: o compulsório é fixado pelo BC)",
        ])],
        "reescrita": ("A instituição do PIX " + hl("pode aumentar") + " o efeito do multiplicador bancário, uma vez "
                      "que a menor retenção de papel moeda pelo público eleva a capacidade dos bancos de conceder "
                      "crédito."),
        "tipo_erro": ["OUTRO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Gabarito do curso ERRADO (efeito ambíguo: c ↓ mas reservas ↑); o verso registra "
                             "discordância própria e de três IAs, que marcam CERTO pelo modelo-padrão do "
                             "multiplicador."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 034", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 035", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 036", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 037", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 038", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 039", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": ["contestavel: gabarito do curso ERRADO (efeito ambíguo via reservas de liquidação); pelo "
                    "modelo-padrão do multiplicador, CERTO é mais defensável"],
    },
    # ------------------------------------------------------------------ E2-L00311
    {
        "id": "ECO-E2-L00311-1", "fonte_ref": "E2-L00311", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Na abordagem heterodoxa, o multiplicador bancário é considerado instável porque a oferta de "
                      "moeda é endógena e responde às decisões de crédito dos bancos, que dependem, entre outros "
                      "fatores, do nível de incerteza predominante na economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na <u>abordagem heterodoxa</u>, o multiplicador bancário é considerado <u>instável</u> "
                      "porque a oferta de moeda é <u>endógena</u> e responde às decisões de crédito dos bancos, "
                      "que dependem, entre outros fatores, do nível de incerteza predominante na economia."),
        "poucas": ("Para os " + azb("pós-keynesianos") + ", os bancos decidem quanto emprestar segundo sua "
                   + azb("preferência pela liquidez") + " e a incerteza: a moeda é " + vd("endógena") + " e a "
                   "relação M1/base não é uma constante estável."),
        "destrinchando": [
            "Visão ortodoxa (multiplicador de manual): o BC controla a base; com c e r estáveis, M1 = m · B é "
            "previsível. Moeda exógena; o BC controla a quantidade.",
            "Visão heterodoxa: a causalidade se inverte — " + azb("empréstimos criam depósitos") + ", e o BC, "
            "que mira a taxa de juros, fornece as reservas demandadas. A base se ajusta ao crédito, não o "
            "contrário (" + oc("Kaldor") + ", " + oc("Moore") + ").",
            "Por que o multiplicador fica instável: c (público) e r (bancos) mudam com o ciclo e o humor. Em "
            "crises, bancos acumulam reservas excedentes e o público entesoura — o multiplicador desaba. Em "
            "booms, o crédito se expande além do “previsto”.",
            "Evidência: após 2008, os EUA quase quintuplicaram a base monetária com o " + azb("QE") + ", mas o "
            "multiplicador M1/base caiu fortemente, porque as reservas ficaram paradas nos bancos.",
            "Raiz teórica: " + oc("Keynes") + " e a preferência pela liquidez aplicada aos bancos; "
            + oc("Minsky") + " e a fragilidade financeira (crédito pró-cíclico).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item reúne três ideias heterodoxas coerentes: endogeneidade, "
                       "instabilidade, incerteza. A banca erraria o item atribuindo isso aos monetaristas ou "
                       "dizendo que, para os heterodoxos, o BC controla a quantidade de moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para os monetaristas, o multiplicador é instável e a oferta de moeda, endógena.”</i> → ERRADO "
            "(troca de ator: monetaristas tratam m como estável e a moeda como exógena)",
            "<i>“Na abordagem heterodoxa, os empréstimos bancários criam depósitos.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["entre outros fatores"], "dificuldade": 2,
        "comentario_fonte": ("Multiplicador instável: depende da demanda por moeda e do comportamento dos bancos, "
                             "sensíveis à incerteza."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00445
    {
        "id": "ECO-E2-L00445-1", "fonte_ref": "E2-L00445", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CN,
        "rotulo_item": "Item",
        "assertiva": ("O multiplicador monetário é diretamente proporcional à preferência do público por manter "
                      "moeda em espécie (papel-moeda) em relação a depósitos à vista."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O multiplicador monetário é ") + vm("diretamente proporcional") + az(" à preferência do "
                    "público por manter moeda em espécie (papel-moeda) em relação a depósitos à vista.")),
        "poucas": ("Papel-moeda retido é " + azb("vazamento") + " do circuito de crédito. Quanto maior a "
                   "preferência c = PMPP/DV, " + vd("menor o multiplicador") + ": relação inversa."),
        "destrinchando": [
            "Fórmula: " + vd("m = (1 + c)/(c + r)") + ", c = PMPP/DV, r = reservas/DV. Como r < 1, o "
            "denominador cresce mais (em proporção) que o numerador quando c sobe: m cai.",
            "Exemplo: r = 0,1. c = 0,25 → m = 1,25/0,35 ≈ " + vd("3,57") + "; c = 0,5 → m = 1,5/0,6 = "
            + vd("2,5") + ".",
            "Precisão: “inversamente proporcional” também é linguagem frouxa (m não é k/c); o rigor é dizer "
            "“varia na razão inversa” ou “decresce com c”. O que decide o item é o sinal.",
            "Determinantes de c: confiança nos bancos (corrida bancária → c dispara), custo das tarifas, "
            "informalidade, inflação, tecnologia de pagamento.",
            "Mesma lógica para as reservas: o multiplicador decresce com r. Só os depósitos à vista o "
            "alimentam.",
        ],
        "dissecando": (cz("[inversão]") + " Troca de sinal pura, sem outra alteração. Pista: tudo o que fica "
                       "<b>fora</b> do circuito banco → crédito → depósito reduz m."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma corrida bancária tende a reduzir o multiplicador monetário.”</i> → CERTO",
            "<i>“O multiplicador cresce com a taxa de reservas bancárias.”</i> → ERRADO (sinal invertido)",
        ])],
        "reescrita": ("O multiplicador monetário é " + hl("inversamente relacionado") + " à preferência do "
                      "público por manter moeda em espécie (papel-moeda) em relação a depósitos à vista."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Relação inversa: mais moeda fora dos bancos → menos depósitos a multiplicar.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00537
    {
        "id": "ECO-E2-L00537-1", "fonte_ref": "E2-L00537", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MOEDA,
        "rotulo_item": "Item",
        "assertiva": ("Papel-moeda em poder do público é definido como o papel-moeda em circulação deduzido o caixa "
                      "em moeda do BACEN e do sistema bancário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Papel-moeda em poder do público é definido como o papel-moeda em circulação deduzido o "
                       "caixa em moeda ") + vm("do BACEN e") + az(" do sistema bancário.")),
        "poucas": (vd("PMPP = papel-moeda em circulação − caixa dos bancos comerciais") + ". O caixa do Banco "
                   "Central já foi descontado antes, na passagem de papel-moeda <b>emitido</b> para papel-moeda "
                   "<b>em circulação</b>."),
        "destrinchando": [
            "A escada contábil tem três degraus: " + vd("papel-moeda emitido") + " (tudo o que o BC pôs em "
            "existência) − caixa do próprio BC = " + vd("papel-moeda em circulação") + " (fora do BC) − caixa "
            "dos bancos comerciais (encaixe em moeda corrente) = " + vd("PMPP") + ".",
            "Descontar o caixa do BC do papel-moeda em circulação seria contá-lo duas vezes: as cédulas no "
            "cofre do BC <b>não estão</b> em circulação.",
            "Uso no M1: " + vd("M1 = PMPP + depósitos à vista") + ". O caixa dos bancos fica fora do M1 (não "
            "está com o público), mas entra na " + azb("base monetária") + " como parte das reservas.",
            "Base pela mesma escada: B = papel-moeda em circulação + depósitos dos bancos no BC = PMPP + caixa "
            "dos bancos + reservas no BC.",
            vm("Regra-âncora: emitido − caixa do BC = em circulação; em circulação − caixa dos bancos = PMPP."),
        ],
        "dissecando": (cz("[dado alterado · meia-verdade]") + " A definição é quase literal; o item enxertou o "
                       "BACEN na dedução. Pista: o ponto de partida já é “em circulação”, conceito que exclui o "
                       "que está no BC. 🔥 A banca alterna “emitido” e “em circulação” para testar a escada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O papel-moeda em poder do público corresponde ao papel-moeda emitido deduzidos os caixas do "
            "Banco Central e dos bancos comerciais.”</i> → CERTO",
            "<i>“O caixa dos bancos comerciais em moeda corrente integra o M1.”</i> → ERRADO (integra a base, não "
            "o M1)",
        ])],
        "reescrita": ("Papel-moeda em poder do público é definido como o papel-moeda em circulação deduzido o caixa "
                      "em moeda " + "<s>do BACEN e</s>" + " do sistema bancário."),
        "tipo_erro": ["DADO_ALTERADO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "PMPP = papel-moeda em circulação − caixa do sistema bancário em moeda corrente.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00538
    {
        "id": "ECO-E2-L00538-1", "fonte_ref": "E2-L00538", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MOEDA,
        "rotulo_item": "Item",
        "assertiva": ("O multiplicador monetário aumenta quando aumenta a razão papel-moeda em poder do público "
                      "dividido pelo volume de depósitos à vista do público nos bancos comerciais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O multiplicador monetário ") + vm("aumenta") + az(" quando aumenta a razão papel-moeda em "
                    "poder do público dividido pelo volume de depósitos à vista do público nos bancos "
                    "comerciais.")),
        "poucas": ("Com " + vd("m = (1 + c)/(c + r)") + " e c = PMPP/DV, c ↑ → " + vd("m ↓") + ": mais dinheiro "
                   "no bolso e menos no banco reduz a multiplicação."),
        "destrinchando": [
            "Derivação rápida: M1 = PMPP + DV = (c + 1)DV; B = PMPP + R = (c + r)DV. Logo " + vd("m = M1/B = "
            "(1 + c)/(c + r)") + ".",
            "Sinal: dm/dc = (r − 1)/(c + r)², negativo sempre que r < 1. Só com r = 1 (reserva integral) c "
            "deixaria de importar, porque m = 1.",
            "Exemplo: r = 0,2. c = 0,2 → m = 1,2/0,4 = " + vd("3") + "; c = 0,6 → m = 1,6/0,8 = " + vd("2")
            + ".",
            "Quando c sobe na prática: corrida bancária, perda de confiança no sistema, aumento da "
            "informalidade, feriados e fim de ano (sazonalidade da demanda por cédulas).",
        ],
        "dissecando": (cz("[inversão]") + " Troca de sinal com a variável escrita por extenso para cansar a "
                       "leitura (“razão papel-moeda em poder do público dividido pelo volume de depósitos”). "
                       "Traduza para c e aplique a regra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O multiplicador monetário diminui quando aumenta a razão entre papel-moeda em poder do público "
            "e depósitos à vista.”</i> → CERTO",
            "<i>“Com reserva integral (r = 1), o multiplicador é igual a 1, qualquer que seja c.”</i> → CERTO",
        ])],
        "reescrita": ("O multiplicador monetário " + hl("diminui") + " quando aumenta a razão papel-moeda em poder "
                      "do público dividido pelo volume de depósitos à vista do público nos bancos comerciais."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "c = PMPP/DV ↑ → multiplicador ↓; m = (1 + c)/(c + r).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00445-1 (mesma regra, redação diferente)"],
    },
    # ------------------------------------------------------------------ E2-L00539
    {
        "id": "ECO-E2-L00539-1", "fonte_ref": "E2-L00539", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MOEDA,
        "rotulo_item": "Item",
        "assertiva": ("O agregado monetário básico, do qual decorrem todos os demais agregados monetários, "
                      "denomina-se base monetária. Este agregado inclui o papel-moeda emitido pelo governo em "
                      "poder do público e o volume de reservas mantidos pelos bancos comerciais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O agregado monetário básico, do qual decorrem todos os demais agregados monetários, "
                      "denomina-se <u>base monetária</u>. Este agregado inclui o papel-moeda emitido pelo governo "
                      "em poder do público e o <u>volume de reservas</u> mantidos pelos bancos comerciais."),
        "poucas": (vd("B = PMPP + reservas bancárias") + " (caixa dos bancos + depósitos no BC). É a "
                   + azb("moeda de alta potência") + ", que o multiplicador transforma em M1 e demais "
                   "agregados."),
        "destrinchando": [
            "A base é o " + azb("passivo monetário do Banco Central") + ": as cédulas e moedas fora dele e os "
            "saldos dos bancos em sua conta de reservas. É o que o BC controla diretamente.",
            "“Do qual decorrem os demais”: o sistema bancário multiplica a base em depósitos à vista (M1 = m · "
            "B), e os agregados mais amplos (M2 a M4) somam quase-moedas sobre o M1.",
            "Reservas = encaixe em moeda corrente nos cofres + " + azb("compulsório") + " em espécie + reservas "
            "voluntárias no BC. Compulsórios remunerados em títulos ou sobre depósitos a prazo, em geral, ficam "
            "fora da base restrita.",
            "Imprecisão tolerada: “papel-moeda emitido pelo governo” — quem emite é o " + rx("Banco Central do "
            "Brasil") + " (monopólio de emissão, CF art. 164), não o Tesouro. A banca usa “governo” em sentido "
            "amplo.",
            vm("Regra-âncora: base = PMPP + reservas; M1 = PMPP + depósitos à vista."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual com duas expressões que assustam: "
                       "“do qual decorrem todos os demais” (certo, pela lógica do multiplicador) e “emitido pelo "
                       "governo” (sentido lato). A banca erraria trocando reservas por depósitos à vista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A base monetária inclui o papel-moeda em poder do público e os depósitos à vista nos bancos "
            "comerciais.”</i> → ERRADO (troca de conceito: essa soma é o M1)",
            "<i>“A compra de títulos públicos pelo Banco Central no mercado aberto expande a base "
            "monetária.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["todos"], "dificuldade": 1,
        "comentario_fonte": ("Base monetária = PMPP + encaixes totais dos bancos (caixa em moeda corrente + "
                             "depósitos compulsórios e voluntários no BC)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00585
    {
        "id": "ECO-E2-L00585-1", "fonte_ref": "E2-L00585", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MODELOS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria proposta por Keynes, as taxas de juros de mercado são fortemente "
                      "condicionadas pelo equilíbrio entre a poupança e o investimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a teoria proposta por Keynes, as taxas de juros de mercado são fortemente "
                       "condicionadas pelo equilíbrio entre ") + vm("a poupança e o investimento") + az(".")),
        "poucas": ("Para " + oc("Keynes") + ", o juro é " + azb("fenômeno monetário") + ": nasce do encontro "
                   "entre a " + azb("oferta de moeda") + " e a " + azb("preferência pela liquidez") + ". Poupança "
                   "× investimento é a teoria " + azb("clássica") + "."),
        "destrinchando": [
            azb("Teoria clássica (fundos emprestáveis)") + ": o juro é o preço que equilibra a oferta de "
            "poupança e a demanda por investimento; é variável real, e a moeda é neutra.",
            "Ruptura de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936): o juro é a recompensa por "
            + azb("abrir mão da liquidez") + ", não por poupar. Ele se forma no mercado de moeda: oferta fixada "
            "pela autoridade monetária × demanda (transação, precaução, especulação).",
            "Na ótica keynesiana, poupança e investimento se igualam pela variação da " + vd("renda") + ", não "
            "dos juros: se o investimento cai, a renda cai até que a poupança gerada iguale o novo "
            "investimento; pela mesma lógica, a tentativa de poupar mais reduz a renda sem elevar a poupança "
            "agregada (paradoxo da parcimônia).",
            "Os juros entram no lado real como " + azb("variável de transmissão") + ": comparados à "
            "eficiência marginal do capital, determinam o investimento. No IS-LM de " + oc("Hicks") + ", os "
            "dois mercados se resolvem juntos — a síntese, não Keynes puro.",
            vm("Regra-âncora: clássicos → juro real, S = I; Keynes → juro monetário, Mˢ = L(Y, i)."),
        ],
        "grafico_verso": "ECO-E2-L00585-1-V1",
        "dissecando": (cz("[troca de ator · troca de conceito]") + " O item atribui a Keynes a teoria que ele "
                       "combateu. O “fortemente condicionadas” dá ar de nuance, mas a determinação keynesiana é "
                       "monetária. 🔥 Keynes × clássicos em juros, moeda e emprego é par de opostos recorrente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na teoria clássica, a taxa de juros equilibra poupança e investimento.”</i> → CERTO",
            "<i>“Para Keynes, a poupança é função principalmente da taxa de juros.”</i> → ERRADO (troca de "
            "conceito: é função da renda)",
        ])],
        "reescrita": ("De acordo com a teoria proposta por Keynes, as taxas de juros de mercado são fortemente "
                      "condicionadas pelo equilíbrio entre " + hl("a oferta de moeda e a demanda por moeda "
                      "(preferência pela liquidez)") + "."),
        "tipo_erro": ["TROCA_ATOR", "TROCA_CONCEITO"], "moduladores": ["fortemente"], "dificuldade": 1,
        "comentario_fonte": ("Poupança × investimento é a teoria clássica dos fundos emprestáveis; em Keynes, o juro "
                             "é monetário (oferta de moeda × preferência pela liquidez)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00595
    {
        "id": "ECO-E2-L00595-1", "fonte_ref": "E2-L00595", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONC,
        "rotulo_item": "Item",
        "assertiva": ("Há destruição de meios de pagamento quando um indivíduo realiza um depósito à vista em um "
                      "banco comercial e, em seguida, aplica o dinheiro em um fundo de investimentos em renda "
                      "fixa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Há destruição de meios de pagamento quando um indivíduo realiza um depósito à vista em um "
                      "banco comercial e, <u>em seguida, aplica o dinheiro em um fundo</u> de investimentos em "
                      "renda fixa."),
        "poucas": ("O depósito só troca a forma da moeda (PMPP → DV, M1 igual); a aplicação no fundo troca um "
                   "haver monetário por uma " + azb("cota") + " (M3): " + vd("M1 cai") + "."),
        "destrinchando": [
            "Passo 1 — depósito à vista: o papel-moeda vira depósito. PMPP ↓ e DV ↑ no mesmo valor; " + vd("M1 "
            "inalterado") + ". (A base também não muda: o papel-moeda passa a ser caixa do banco.)",
            "Passo 2 — aplicação no fundo de renda fixa: o depósito à vista do indivíduo é debitado e ele "
            "recebe cotas, um haver não monetário de alta liquidez. O dinheiro vai para ativos do fundo "
            "(títulos públicos, compromissadas, CDB). O M1 diminui; o " + vd("M3") + ", que inclui as cotas, "
            "não se altera.",
            "Regra geral: M1 cai quando haveres monetários do público são trocados por " + azb("quase-moedas")
            + " ou entregues ao sistema bancário (resgate de empréstimo, compra de títulos do BC ou de bancos).",
            "Leitura macroeconômica: migrações M1 → M2/M3 em ambiente de juros altos (no " + rx("Brasil") + ", "
            "Selic elevada) explicam por que o M1 brasileiro é pequeno em relação ao PIB e por que o BC observa "
            "também os agregados amplos.",
        ],
        "dissecando": (cz("[detalhe]") + " Item em duas etapas: a 1ª (depósito) é neutra e serve de distração; o "
                       "gabarito se decide na 2ª. Quem vê “depósito” e pensa “moeda continua no banco” marca "
                       "ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Há destruição de meios de pagamento quando um indivíduo deposita papel-moeda em sua conta "
            "corrente.”</i> → ERRADO (troca dentro do M1)",
            "<i>“O resgate de cotas de fundo de renda fixa, creditado em conta corrente, cria meios de "
            "pagamento.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Depósito à vista está no M1; ao aplicar em fundo de renda fixa (fora do M1), o M1 "
                             "se reduz: destruição de meios de pagamento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00612
    {
        "id": "ECO-E2-L00612-1", "fonte_ref": "E2-L00612", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_SIST,
        "rotulo_item": "Item",
        "assertiva": ("Se o encaixe monetário dos bancos comerciais (reservas voluntárias e compulsórias) for nulo, "
                      "o multiplicador monetário dependerá apenas da preferência do público por papel-moeda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o encaixe monetário dos bancos comerciais (reservas voluntárias e compulsórias) for "
                      "<u>nulo</u>, o multiplicador monetário dependerá <u>apenas</u> da preferência do público "
                      "por papel-moeda."),
        "poucas": ("Com r = 0, " + vd("m = (1 + c)/(c + r)") + " vira " + vd("m = (1 + c)/c") + ": sobra só c, "
                   "a preferência do público por papel-moeda."),
        "destrinchando": [
            "O multiplicador tem dois parâmetros de comportamento: " + azb("c") + " (público: PMPP/DV) e "
            + azb("r") + " (bancos: reservas/DV, compulsórias + voluntárias). Zerado um, o outro determina m "
            "sozinho.",
            "Com r = 0, o único vazamento do circuito de crédito é o papel-moeda retido. Exemplo: c = 0,25 → "
            "m = 1,25/0,25 = " + vd("5") + "; c = 0,5 → m = " + vd("3") + ".",
            "Espelho: com c = 0 (ninguém retém cédulas), " + vd("m = 1/r") + " — o "
            + azb("multiplicador bancário simples") + ", que depende só do encaixe.",
            "Os dois zeros ao mesmo tempo (c = 0 e r = 0) fariam m tender ao infinito: sem vazamento algum, "
            "um real de base sustentaria depósitos ilimitados. Por isso os casos-limite são só didáticos.",
            "No mundo real, mesmo sem compulsório (caso de EUA, Canadá e Reino Unido para depósitos à vista), "
            "os bancos mantêm reservas voluntárias para liquidação de pagamentos: r nunca é zero.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O “apenas”, que costuma denunciar ERRADO, aqui é "
                       "verdadeiro por construção: com r = 0 só resta c na fórmula. Antes de reagir ao "
                       "modulador, substitua na fórmula."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o público não retiver papel-moeda, o multiplicador dependerá apenas da taxa de "
            "reservas.”</i> → CERTO",
            "<i>“Se o encaixe for nulo, o multiplicador será igual a 1.”</i> → ERRADO (m = 1 ocorre com reserva "
            "integral, r = 1, ou com c → ∞)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas"], "dificuldade": 2,
        "comentario_fonte": "m = (1 + c)/(r + c); com r = 0, m = (1 + c)/c: depende só de c.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00613
    {
        "id": "ECO-E2-L00613-1", "fonte_ref": "E2-L00613", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_SIST,
        "rotulo_item": "Item",
        "assertiva": ("A elevação da taxa de juros de mercado tende a reduzir a demanda por moeda para fins de "
                      "especulação, uma vez que o custo de oportunidade de reter moeda em vez de aplicá-la em "
                      "ativos rentáveis aumenta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elevação da taxa de juros de mercado tende a <u>reduzir</u> a demanda por moeda para fins "
                      "de especulação, uma vez que o <u>custo de oportunidade</u> de reter moeda em vez de "
                      "aplicá-la em ativos rentáveis aumenta."),
        "poucas": ("O juro é o " + azb("preço de ficar líquido") + ": juros maiores tornam mais caro reter moeda e "
                   "reduzem a " + azb("demanda especulativa") + " (" + oc("Keynes") + ")."),
        "destrinchando": [
            "Os três motivos de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936): " + azb("transação") + " e "
            + azb("precaução") + ", ligados à renda; " + azb("especulação") + ", ligado inversamente aos juros.",
            "Mecanismo especulativo: preço do título e juros andam em sentido oposto. Com juros altos, o agente "
            "espera que caiam (títulos vão se valorizar) e compra títulos — reduz a moeda retida. Com juros "
            "baixos, espera alta (perda de capital nos títulos) e prefere ficar líquido.",
            "Leitura de " + oc("Tobin") + " (1958): mesmo sem expectativa de reversão, a escolha de carteira "
            "entre moeda (sem risco, sem rendimento) e títulos (com risco e rendimento) faz a demanda por "
            "moeda cair com os juros, pelo custo de oportunidade.",
            "Caso-limite: a " + azb("armadilha da liquidez") + " — com juros muito baixos, todos esperam alta, "
            "a demanda especulativa fica infinitamente elástica e a LM, horizontal.",
            vm("Regra-âncora: L = L₁(Y) + L₂(i), com L₁ crescente na renda e L₂ decrescente nos juros."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Relação de manual, com o “tende a” e o "
                       "mecanismo certo (custo de oportunidade). A banca inverteria o sinal ou trocaria o motivo "
                       "(“transação” no lugar de “especulação”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação da renda reduz a demanda por moeda para transações.”</i> → ERRADO (sinal invertido)",
            "<i>“Na armadilha da liquidez, a demanda especulativa por moeda é infinitamente elástica em relação "
            "aos juros.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Demanda especulativa: escolha entre reter moeda e aplicar em títulos; juros maiores "
                             "elevam o custo de oportunidade e reduzem a demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00655
    {
        "id": "ECO-E2-L00655-1", "fonte_ref": "E2-L00655", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Se o público decide substituir parte dos depósitos à vista por papel-moeda e a base "
                      "monetária se mantenha constante, o multiplicador monetário será reduzido."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o público decide substituir parte dos depósitos à vista por papel-moeda e a base "
                      "monetária se mantenha <u>constante</u>, o multiplicador monetário será <u>reduzido</u>."),
        "poucas": ("Sacar depósitos para guardar cédulas eleva " + vd("c = PMPP/DV") + "; com r dado, "
                   + vd("m = (1 + c)/(c + r) cai") + " e, com a base constante, o M1 também cai."),
        "destrinchando": [
            "Efeito imediato do saque: PMPP ↑ e DV ↓ no mesmo valor — o M1 não muda no primeiro instante. Mas o "
            "banco perdeu reservas (o caixa saiu com o cliente).",
            "Efeito em cadeia: com menos reservas, o banco precisa recompor o encaixe e reduz empréstimos; os "
            "depósitos que nasceriam desses empréstimos não nascem. No novo equilíbrio, " + vd("M1 = m · B")
            + " é menor, porque m caiu e B ficou igual.",
            "Exemplo: r = 0,1; B = 100. Com c = 0,25: m ≈ 3,57 e M1 ≈ " + vd("357") + ". Com c = 0,5: m = 2,5 "
            "e M1 = " + vd("250") + ".",
            "Caso histórico: nas corridas bancárias da Grande Depressão (EUA, 1930–1933), c disparou e o M1 "
            "despencou, mesmo com a base crescendo — análise clássica de " + oc("Friedman e Schwartz") + ".",
            "Por isso o BC reage a pânicos com " + azb("prestamista de última instância") + ": injeta base para "
            "compensar a queda do multiplicador.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " A cláusula “base constante” isola o efeito sobre m. Armadilha: "
                       "achar que trocar depósito por cédula é neutro porque o M1 inicial não muda — o "
                       "multiplicador, não o estoque instantâneo, é o que o item pergunta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o público substitui depósitos à vista por papel-moeda, os meios de pagamento permanecem "
            "constantes após o ajuste do sistema bancário, pois o M1 inclui ambos.”</i> → ERRADO (só no instante "
            "do saque; após o ajuste, M1 cai)",
            "<i>“Uma corrida bancária tende a reduzir o multiplicador monetário.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Mais papel-moeda retido → menos recursos nos bancos para emprestar → multiplicador "
                             "menor."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “papel- moeda” → “papel-moeda” (quebra de linha da fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00722
    {
        "id": "ECO-E2-L00722-1", "fonte_ref": "E2-L00722", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_POL,
        "rotulo_item": "Item",
        "assertiva": ("A moeda escritural, também chamada de papel-moeda, tem seu curso forçado por lei e não "
                      "possui lastro em ouro ou em qualquer outro ativo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A moeda ") + vm("escritural, também chamada de papel-moeda,") + az(" tem seu curso forçado "
                    "por lei e não possui lastro em ouro ou em qualquer outro ativo.")),
        "poucas": (azb("Moeda escritural") + " = depósitos à vista (registro contábil nos bancos). "
                   + azb("Papel-moeda") + " = cédulas emitidas pelo Banco Central. O item funde as duas; a "
                   "descrição (curso forçado, sem lastro) é a da " + azb("moeda fiduciária") + "."),
        "destrinchando": [
            "Tipos de moeda pela forma: " + azb("metálica") + " (valor intrínseco), " + azb("papel-moeda")
            + " (cédulas; historicamente conversível, hoje inconversível), " + azb("moeda escritural ou "
            "bancária") + " (saldos em conta corrente movimentáveis por cheque, cartão de débito, TED, Pix).",
            "Quem cria cada uma: o papel-moeda é emitido pelo " + rx("Banco Central do Brasil") + " "
            "(monopólio de emissão); a moeda escritural é criada pelos bancos comerciais ao conceder crédito "
            "(multiplicador).",
            azb("Moeda fiduciária") + ": vale pela confiança e pela lei, não por lastro. Desde o fim de "
            "Bretton Woods (" + vd("1971") + "), nenhuma grande moeda é conversível em ouro.",
            "Curso legal e forçado se aplicam ao papel-moeda; a moeda escritural não tem curso forçado próprio "
            "— é um direito contra o banco, conversível em papel-moeda à vista, e o credor pode recusar cheque.",
            vm("Regra-âncora: M1 = papel-moeda em poder do público (manual) + depósitos à vista (escritural)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O aposto “também chamada de papel-moeda” iguala os dois "
                       "componentes do M1; o resto da frase está certo para o papel-moeda e distrai. Pista: "
                       "“escritural” vem de escrita, registro contábil."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A moeda escritural corresponde aos depósitos à vista nos bancos comerciais.”</i> → CERTO",
            "<i>“O papel-moeda brasileiro é lastreado nas reservas internacionais do país.”</i> → ERRADO "
            "(moeda fiduciária, sem lastro)",
        ])],
        "reescrita": ("A moeda " + hl("fiduciária, como o papel-moeda,") + " tem seu curso forçado por lei e não "
                      "possui lastro em ouro ou em qualquer outro ativo."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Moeda escritural = depósitos à vista; papel-moeda = cédulas e moedas. O papel-moeda é "
                             "que tem curso forçado e é fiduciário. Comentário fundido com o da duplicata "
                             "E2-L00777."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L00777 (mesmo item, comentário fundido)"],
    },
    # ------------------------------------------------------------------ E2-L00724
    {
        "id": "ECO-E2-L00724-1", "fonte_ref": "E2-L00724", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_POL,
        "rotulo_item": "Item",
        "assertiva": ("O multiplicador dos meios de pagamento reflete a capacidade do sistema bancário de aumentar "
                      "a oferta de moeda a partir de uma base monetária inicial. Considere a fórmula M = mB, onde M "
                      "é o saldo dos meios de pagamento, B é a base monetária e m é o multiplicador. O "
                      "funcionamento do multiplicador dos meios de pagamento é diretamente proporcional à taxa de "
                      "reservas mantidas pelos bancos comerciais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O multiplicador dos meios de pagamento reflete a capacidade do sistema bancário de aumentar "
                       "a oferta de moeda a partir de uma base monetária inicial. Considere a fórmula M = mB, onde "
                       "M é o saldo dos meios de pagamento, B é a base monetária e m é o multiplicador. O "
                       "funcionamento do multiplicador dos meios de pagamento é ") + vm("diretamente proporcional")
                    + az(" à taxa de reservas mantidas pelos bancos comerciais.")),
        "poucas": ("Reserva é dinheiro que o banco " + azb("não empresta") + ": quanto maior a taxa de reservas, "
                   "menor a expansão de depósitos — " + vd("m varia na razão inversa de r") + "."),
        "destrinchando": [
            "Na forma simples (sem papel-moeda retido), " + vd("m = 1/r") + ": r = 10% → m = 10; r = 20% → "
            "m = 5. Dobrar as reservas corta o multiplicador pela metade.",
            "Na forma completa, " + vd("m = (1 + c)/(c + r)") + " (c = PMPP/DV): m continua decrescente em r "
            "para qualquer c.",
            "Taxa de reservas = compulsório (fixado pelo BC) + reservas voluntárias (prudência dos bancos). O "
            + azb("compulsório") + " é instrumento de política monetária: elevá-lo contrai o crédito e o M1 "
            "sem mexer na base.",
            "As duas primeiras frases do item são definições corretas: M = m · B, e o multiplicador mede quanto "
            "o sistema bancário amplia a base.",
            vm("Regra-âncora: reservas ↑ → multiplicador ↓; papel-moeda retido ↑ → multiplicador ↓."),
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " Duas frases de definição corretas preparam a "
                       "terceira, que inverte o sinal. Em itens longos, o erro costuma estar na última oração."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução da alíquota do compulsório sobre depósitos à vista eleva o multiplicador dos meios de "
            "pagamento.”</i> → CERTO",
            "<i>“O multiplicador é inversamente proporcional aos depósitos à vista.”</i> → ERRADO (sinal "
            "invertido: depósitos ampliam m)",
        ])],
        "reescrita": ("O multiplicador dos meios de pagamento reflete a capacidade do sistema bancário de aumentar a "
                      "oferta de moeda a partir de uma base monetária inicial. Considere a fórmula M = mB, onde M é "
                      "o saldo dos meios de pagamento, B é a base monetária e m é o multiplicador. O funcionamento "
                      "do multiplicador dos meios de pagamento é " + hl("inversamente relacionado") + " à taxa de "
                      "reservas mantidas pelos bancos comerciais."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Quanto maior a taxa de reservas, menor a capacidade de criar moeda escritural: relação "
                             "inversa. Comentário fundido com o da duplicata E2-L00779."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L00779 (mesmo item, comentário fundido)"],
    },
    # ------------------------------------------------------------------ E2-L00758
    {
        "id": "ECO-E2-L00758-1", "fonte_ref": "E2-L00758", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_CN2,
        "rotulo_item": "Item",
        "assertiva": ("Os agregados monetários são uma medida importante no sistema monetário, pois estão "
                      "relacionados à liquidez na economia. Nesse caso, os meios de pagamento (M1) correspondem à "
                      "soma do papel moeda em circulação e dos depósitos à vista nos bancos comerciais, deduzido os "
                      "valores em seu caixa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os agregados monetários são uma medida importante no sistema monetário, pois estão "
                      "relacionados à liquidez na economia. Nesse caso, os meios de pagamento (M1) correspondem à "
                      "soma do papel moeda <u>em circulação</u> e dos depósitos à vista nos bancos comerciais, "
                      "<u>deduzido os valores em seu caixa</u>."),
        "poucas": (vd("M1 = PMPP + DV") + " e " + vd("PMPP = papel-moeda em circulação − caixa dos bancos") + "; "
                   "logo " + vd("M1 = papel-moeda em circulação + DV − caixa dos bancos") + ", que é o que o "
                   "item diz."),
        "destrinchando": [
            "Escada: papel-moeda emitido − caixa do BC = " + azb("papel-moeda em circulação") + "; em "
            "circulação − caixa (encaixe em moeda corrente) dos bancos comerciais = " + azb("PMPP") + ".",
            "Substituindo no M1: M1 = (PMC − caixa dos bancos) + DV = " + vd("PMC + DV − caixa dos bancos")
            + ". A dedução final é exatamente o “deduzido os valores em seu caixa”.",
            "Por que o caixa sai: cédulas nos cofres dos bancos não estão à disposição do público para "
            "pagamentos. Contá-las e contar também os depósitos que elas lastreiam seria dupla contagem.",
            "Os agregados medem a " + azb("liquidez") + " disponível ao público: M1 (liquidez imediata, sem "
            "rendimento), M2, M3 e M4 (sucessivamente menos líquidos e mais remunerados).",
            "Detalhe de português: o correto seria “deduzidos os valores” (concordância com “valores”); a "
            "falha é da redação original e não afeta o julgamento.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " O item parece errado à primeira vista — “papel-moeda "
                       "em circulação” não é PMPP —, mas a dedução no fim da frase corrige a diferença. Leia "
                       "até o último termo antes de julgar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O M1 corresponde à soma do papel-moeda em circulação e dos depósitos à vista.”</i> → ERRADO "
            "(falta deduzir o caixa dos bancos)",
            "<i>“O M1 corresponde ao papel-moeda emitido mais os depósitos à vista, deduzidos os caixas do BC e "
            "dos bancos comerciais.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "PME = PMC = PMPP + caixa dos bancos; M1 = PMPP + DV = PMC + DV − caixa dos bancos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 112", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
]
