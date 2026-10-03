"""Cards do lote de redação 17 — ECO, passada 02 (notas 35 e 36: moeda, multiplicador, Banco Central e
instrumentos de política monetária)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "agr": "🪙 Funções e agregados monetários",
    "mult": "🏦 Criação de moeda e multiplicador",
    "dem": "📊 Demanda por moeda",
    "bc": "🏛️ Funções do Banco Central",
    "inst": "🛠️ Instrumentos de política monetária",
}

CMD_NIDI_J25 = ("Julgue certo ou errado os itens a seguir, acerca das políticas monetárias típicas conduzidas "
                "pelos bancos centrais e, em particular, o BCB.")
CMD_ANTT_CONTAS = "A respeito das contas do sistema monetário, julgue os itens que se seguem."
CMD_ANTT_MON = "Julgue os itens que se seguem, relativos à economia monetária."
CMD_NIDI_D24 = ("No que concerne à política monetária, seu papel, seus instrumentos e agentes, julgue (C ou E) os "
                "itens a seguir.")
CMD_NIDI_F26 = ("Sobre os instrumentos de política monetária e o papel do Banco Central do Brasil, julgue o item a "
                "seguir.")
CMD_CLIP = ("A política monetária moderna combina instrumentos de controle da oferta de moeda com metas de "
            "inflação, buscando estabilidade econômica. Com base nesse contexto, julgue os itens a seguir.")
CMD_BC = "Julgue o item a seguir, relativo às funções do Banco Central do Brasil."
CMD_INST = "Julgue o item a seguir, relativo aos instrumentos de política monetária."

PROV = lambda ano: (f"banca_provavel: CEBRASPE (item de {ano} no estilo da banca, possivelmente CACD; a fonte só "
                    "traz o ano, sem órgão) — não confirmada")

CARDS = [
    # ------------------------------------------------------------------ E3-L00112
    {
        "id": "ECO-E3-L00112-1", "fonte_ref": "E3-L00112", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_J25,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento pelo Banco Central da alíquota do depósito compulsório sobre os depósitos à vista "
                      "dos bancos comerciais amplia a capacidade de criação de moeda pelos bancos comerciais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um aumento pelo Banco Central da alíquota do depósito compulsório sobre os depósitos à "
                       "vista dos bancos comerciais ") + vm("amplia") + az(" a capacidade de criação de moeda "
                                                                          "pelos bancos comerciais.")),
        "poucas": ("Compulsório maior = mais reservas presas no BC a cada depósito = " + azb("multiplicador "
                   "menor") + ". A capacidade de criação de moeda escritural <b>cai</b>, não sobe."),
        "destrinchando": [
            "Os bancos criam " + azb("moeda escritural") + " ao emprestar: o crédito vira depósito à vista em "
            "outro banco, que reempresta uma parte, e assim por diante. O que “vaza” de cada rodada são as "
            + azb("reservas") + " (compulsórias e voluntárias) e o papel-moeda que o público retém.",
            "Multiplicador monetário: " + vd("m = (1 + c) / (c + r)") + ", em que c = PMPP/DV e r = reservas/DV. "
            "O compulsório entra em r, <b>no denominador</b>: r ↑ → m ↓.",
            "Exemplo sem retenção de papel-moeda (c = 0): com r = " + vd("20%") + ", m = 1/0,2 = " + vd("5")
            + "; com r = " + vd("25%") + ", m = 1/0,25 = " + vd("4") + ". Cada real de base passa a sustentar "
            "menos meios de pagamento.",
            "Por isso elevar o compulsório é medida " + azb("contracionista") + " (enxuga crédito e liquidez), e "
            "reduzi-lo é expansionista — como fez o " + rx("BCB") + " na crise de 2008, liberando compulsórios "
            "para irrigar o sistema.",
            vm("Regra-âncora: compulsório ↑ → multiplicador ↓ → menos moeda escritural."),
        ],
        "dissecando": (cz("[inversão]") + " O item descreve corretamente o instrumento e o agente, mas troca o "
                       "sentido do efeito (“amplia”). Pista: compulsório é dinheiro que o banco <b>não</b> pode "
                       "emprestar — mais dele só pode frear a criação de moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução da alíquota do compulsório eleva o multiplicador bancário, ceteris paribus.”</i> → "
            "CERTO",
            "<i>“O aumento do compulsório reduz a base monetária.”</i> → ERRADO (troca de conceito: a base não "
            "muda — as reservas continuam nela; cai o multiplicador)",
        ])],
        "reescrita": ("Um aumento pelo Banco Central da alíquota do depósito compulsório sobre os depósitos à vista "
                      "dos bancos comerciais " + hl("reduz") + " a capacidade de criação de moeda pelos bancos "
                      "comerciais."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Três comentários fundidos: compulsório maior reduz o multiplicador e a "
                            "criação de moeda escritural; exemplo de 20% para 30%/40%; reescrita com “reduz”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0526-1 e ECO-E1-0531-1 (efeito contracionista do compulsório)"],
    },
    # ------------------------------------------------------------------ E3-L00114
    {
        "id": "ECO-E3-L00114-1", "fonte_ref": "E3-L00114", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_J25,
        "rotulo_item": "Item",
        "assertiva": ("As inovações financeiras como a introdução de cartões de crédito tendem a aumentar a "
                      "elasticidade-renda da demanda por moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As inovações financeiras como a introdução de cartões de crédito tendem a ")
                    + vm("aumentar") + az(" a elasticidade-renda da demanda por moeda.")),
        "poucas": ("Cartões, débito automático e PIX permitem fazer as mesmas transações com " + azb("menos "
                   "saldos monetários") + ": a demanda por moeda cai e fica <b>menos</b> sensível à renda."),
        "destrinchando": [
            "A " + azb("demanda por moeda") + " (L) cresce com a renda (motivo transação) e cai com os juros "
            "(custo de oportunidade). A " + azb("elasticidade-renda") + " mede quanto L sobe, em %, quando a "
            "renda sobe 1%.",
            "Inovações financeiras atuam como substitutos da moeda no papel de meio de troca: o cartão concentra "
            "pagamentos numa data, e o resto do tempo o dinheiro pode ficar aplicado. Para cada nível de renda, "
            "retém-se menos moeda — e, à medida que a renda cresce, os saldos sobem menos do que subiriam sem "
            "essas tecnologias.",
            "Em termos de " + azb("velocidade-renda da moeda") + " (V = PY/M): menos moeda para o mesmo produto "
            "nominal → " + vd("V ↑") + ". É uma das razões pelas quais as metas de agregados monetários perderam "
            "espaço para as metas de juros e de inflação.",
            "No modelo de " + oc("Baumol") + " e " + oc("Tobin") + ", a demanda transacional é M/P = √(bY/2i): "
            "inovações que barateiam a gestão de caixa reduzem o saldo médio; os juros (i) passam a pesar "
            "relativamente mais na decisão de reter moeda.",
        ],
        "dissecando": (cz("[inversão]") + " O item acerta o fenômeno (inovação financeira afeta a demanda por "
                       "moeda) e inverte o sentido. A palavra técnica “elasticidade-renda” intimida, mas basta o "
                       "raciocínio: se é preciso menos moeda para transacionar, a moeda reage <b>menos</b> à "
                       "renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A difusão dos cartões de crédito tende a elevar a velocidade-renda da moeda.”</i> → CERTO",
            "<i>“Inovações financeiras deslocam a demanda por moeda para a direita.”</i> → ERRADO (inversão: "
            "a demanda por saldos cai, a curva vai para a esquerda)",
        ])],
        "reescrita": ("As inovações financeiras como a introdução de cartões de crédito tendem a " + hl("reduzir")
                      + " a elasticidade-renda da demanda por moeda."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tendem a"], "dificuldade": 2,
        "comentario_fonte": "ERRADO. Três comentários fundidos: inovações reduzem a demanda por moeda e a "
                            "sensibilidade à renda; menção a Baumol-Tobin e à gestão de caixa.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00142
    {
        "id": "ECO-E3-L00142-1", "fonte_ref": "E3-L00142", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_CONTAS,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento do PIB real aumenta a demanda por moeda na forma do M1 em decorrência do motivo "
                      "especulação de moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um aumento do PIB real aumenta a demanda por moeda na forma do M1 em decorrência do "
                       "motivo ") + vm("especulação") + az(" de moeda.")),
        "poucas": ("PIB real maior → mais transações → mais moeda demandada pelo " + azb("motivo transação")
                   + ". O " + azb("motivo especulação") + " depende dos juros, não da renda."),
        "destrinchando": [
            "Os três motivos de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) para reter moeda:",
            vd("Transação") + " — moeda como meio de troca, para os pagamentos do dia a dia; varia "
            "<b>diretamente com a renda</b>.",
            vd("Precaução") + " — reserva para imprevistos; também varia diretamente com a renda.",
            vd("Especulação") + " (ou portfólio) — moeda como reserva de valor, em vez de títulos, quando se "
            "espera alta dos juros (queda do preço dos títulos); varia <b>inversamente com a taxa de juros</b>.",
            "Por isso a função de demanda por moeda costuma ser escrita L = kY − hi: o termo kY reúne transação "
            "e precaução; o termo −hi, a especulação.",
            "O " + azb("M1") + " (papel-moeda em poder do público + depósitos à vista) é justamente o agregado "
            "de liquidez imediata, usado para transações — o que reforça a ligação PIB ↑ → M1 demandado ↑ pelo "
            "motivo transação.",
            vm("Regra-âncora: renda → transação e precaução; juros → especulação."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira metade é verdadeira (PIB real ↑ eleva a demanda "
                       "por M1); o erro está só no motivo atribuído. 🔥 A banca adora trocar o motivo: renda com "
                       "especulação, juros com transação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma elevação da taxa de juros reduz a demanda por moeda pelo motivo especulação.”</i> → CERTO",
            "<i>“A demanda por moeda pelo motivo precaução independe do nível de renda.”</i> → ERRADO (troca de "
            "conceito: precaução cresce com a renda)",
        ])],
        "reescrita": ("Um aumento do PIB real aumenta a demanda por moeda na forma do M1 em decorrência do motivo "
                      + hl("transação") + " de moeda."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "E. Comentários fundidos: três motivos de demanda por moeda; PIB eleva a demanda pelo "
                            "motivo transação; especulação ligada aos juros. Um dos comentários associa, sem "
                            "necessidade, aumento de demanda a “mais juros”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 137", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (motivo × variável × relação, no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00143
    {
        "id": "ECO-E3-L00143-1", "fonte_ref": "E3-L00143", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_CONTAS,
        "rotulo_item": "Item",
        "assertiva": "A base monetária é maior que o papel moeda em poder do público.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A base monetária é <u>maior</u> que o papel moeda em poder do público."),
        "poucas": (azb("Base monetária") + " = " + vd("PMPP + reservas bancárias") + ". Como as reservas são "
                   "positivas (há, no mínimo, o compulsório), a base supera o papel-moeda em poder do público."),
        "destrinchando": [
            "A " + azb("base monetária") + " (B, “moeda de alta potência”) é o passivo monetário do Banco "
            "Central: " + vd("B = PMPP + R") + ", em que R são as reservas dos bancos — o caixa em espécie nas "
            "agências mais os depósitos voluntários e compulsórios no BC.",
            "Os " + azb("meios de pagamento") + " (M1) são outra soma: " + vd("M1 = PMPP + DV") + " (depósitos à "
            "vista). O PMPP é a parcela comum às duas; o que as diferencia é R (na base) × DV (no M1).",
            "Como os bancos sempre mantêm reservas — o " + rx("BCB") + " exige recolhimento compulsório sobre "
            "depósitos à vista, e há ainda o caixa operacional —, B > PMPP.",
            "Relação entre os agregados: M1 = m × B, com " + vd("m = (1 + c) / (c + r)") + ". Em regra m > 1, "
            "porque os bancos emprestam parte dos depósitos.",
            "Objeção teórica levantada contra o item: se as reservas fossem zero, B seria igual ao PMPP. É um "
            "caso-limite fora da realidade institucional; a banca manteve o gabarito.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de definição: basta montar a soma da base e ver que o PMPP "
                       "é só uma parcela dela. O risco é confundir base monetária com meios de pagamento ou "
                       "achar que “maior” é absoluto demais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A base monetária inclui os depósitos à vista nos bancos comerciais.”</i> → ERRADO (troca de "
            "conceito: depósitos à vista estão no M1; na base entram as reservas)",
            "<i>“Os meios de pagamento (M1) são maiores que o papel-moeda em poder do público.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "C. Base = PMPP + encaixes (caixa, compulsório e voluntário no BC); um comentário "
                            "aponta possível recurso (reservas nulas tornariam B = PMPP).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 138", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (fórmula da base no 📖)"},
                          {"ref": "IMAGEM 139", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "cortada (esquema base × meios de pagamento descrito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00165
    {
        "id": "ECO-E3-L00165-1", "fonte_ref": "E3-L00165", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_MON,
        "rotulo_item": "Item",
        "assertiva": ("Se a razão entre o papel-moeda em poder do público e os depósitos à vista for igual a 0,6 e "
                      "a razão entre as reservas bancárias e os depósitos à vista for igual a 0,2, o multiplicador "
                      "monetário será igual a 2."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a razão entre o papel-moeda em poder do público e os depósitos à vista for igual a 0,6 "
                      "e a razão entre as reservas bancárias e os depósitos à vista for igual a 0,2, o "
                      "multiplicador monetário será igual a <u>2</u>."),
        "poucas": ("m = (1 + c) / (c + r) = (1 + 0,6) / (0,6 + 0,2) = 1,6 / 0,8 = " + vd("2") + "."),
        "destrinchando": [
            "Dedução: " + vd("M1 = PMPP + DV") + " e " + vd("B = PMPP + R") + ". O multiplicador é m = M1/B. "
            "Dividindo numerador e denominador por DV: " + vd("m = (c + 1) / (c + r)") + ", com c = PMPP/DV e "
            "r = R/DV.",
            "Atalho de prova — atribuir valores: DV = 10 → PMPP = 6 e R = 2. M1 = 6 + 10 = " + vd("16") + "; "
            "B = 6 + 2 = " + vd("8") + "; m = 16/8 = " + vd("2") + ".",
            "Leitura econômica: cada R$ 1 de base emitido pelo " + rx("BCB") + " sustenta R$ 2 de meios de "
            "pagamento. O valor é baixo porque c = 0,6 é alto: muito dinheiro fica na mão do público e não volta "
            "aos bancos para ser reemprestado.",
            "Estática comparativa: " + azb("r ↑ → m ↓") + " (r só está no denominador); " + azb("c ↑ → m ↓")
            + " (c está nos dois termos, mas, como r < 1, o denominador cresce proporcionalmente mais).",
            "Caso-limite: c = 0 → m = 1/r (o “multiplicador bancário simples”); r = 1 (reserva de 100%) → m = 1, "
            "não há criação de moeda escritural.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de cálculo direto; a armadilha é usar a fórmula simples 1/r "
                       "(daria 5) ou montar o denominador com DV em vez de R. Conferir sempre: base no "
                       "denominador, meios de pagamento no numerador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o multiplicador monetário será igual a 5.”</i> → ERRADO (usou 1/r, ignorando a retenção de "
            "papel-moeda)",
            "<i>“Mantido r, se c cair de 0,6 para 0,2, o multiplicador sobe para 3.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "C. Várias resoluções fundidas (fórmula m = (PMPP + DV)/(PMPP + R), atribuição de "
                            "valores 6/10/2, dedução por c e r, leitura econômica e efeito de c e r).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 192–202", "tipo_fonte": "TEXTO/FÓRMULA", "lado": "verso",
                           "acao": "absorvidas (dedução e conta no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00344
    {
        "id": "ECO-E3-L00344-1", "fonte_ref": "E3-L00344", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_D24,
        "rotulo_item": "Item",
        "assertiva": ("A oferta de meios de pagamento é aumentada quando um banco comercial entrega títulos, como "
                      "notas do Tesouro Nacional, ao Banco Central em troca de papel-moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A oferta de meios de pagamento ") + vm("é aumentada") + az(" quando um banco comercial "
                       "entrega títulos, como notas do Tesouro Nacional, ao Banco Central em troca de "
                       "papel-moeda.")),
        "poucas": ("A troca ocorre <b>dentro do setor bancário</b> (banco comercial ↔ BC): o papel-moeda vai para "
                   "o caixa do banco, vira " + azb("reserva") + " e aumenta a " + azb("base monetária")
                   + " — não o M1."),
        "destrinchando": [
            "Regra de ouro da criação de moeda: os meios de pagamento só se alteram em operações entre o "
            + azb("setor bancário") + " (BC e bancos comerciais) e o " + azb("setor não bancário") + " (famílias, "
            "empresas, governo). Trocas dentro de cada setor só mudam a composição dos ativos.",
            "M1 = " + vd("PMPP + DV") + ". Na operação do item, o público não ganha papel-moeda nem depósito: o "
            "banco troca um ativo (título) por outro (moeda em caixa). O PMPP e o DV ficam iguais → "
            + vd("M1 inalterado") + ".",
            "A base (B = PMPP + reservas) <b>sobe</b>, porque as reservas do banco aumentaram. É uma injeção de "
            "liquidez — típica de " + azb("operação de mercado aberto") + " ou de redesconto —, que só vira M1 "
            "quando o banco empresta e o crédito se transforma em depósito à vista do público.",
            "Na prática, o " + rx("BCB") + " não entrega cédulas: credita a conta de reservas do banco. O efeito "
            "contábil é o mesmo.",
            "Contraste: se o BC comprasse o título de uma <b>empresa ou família</b>, pagando-lhe em moeda, o M1 "
            "aumentaria de imediato.",
            vm("Regra-âncora: troca dentro do setor bancário mexe na base, não no M1."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O item confunde base monetária com meios "
                       "de pagamento: a operação injeta liquidez, e o candidato associa “entrou papel-moeda” a "
                       "“aumentou a moeda”. Pista: quem recebe o dinheiro é um banco, não o público."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A base monetária aumenta quando um banco comercial vende títulos ao Banco Central.”</i> → CERTO",
            "<i>“Os meios de pagamento aumentam quando o Banco Central compra títulos de uma empresa não "
            "financeira, pagando-lhe em moeda.”</i> → CERTO",
        ])],
        "reescrita": ("A oferta de meios de pagamento " + hl("não é alterada de imediato") + " quando um banco "
                      "comercial entrega títulos, como notas do Tesouro Nacional, ao Banco Central em troca de "
                      "papel-moeda" + hl(", porque a troca ocorre dentro do setor bancário e eleva apenas a base "
                                         "monetária") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "ERRADO. Quatro comentários fundidos: troca dentro do setor bancário não altera M1; "
                            "a operação aumenta a base (reservas); M1 só cresce com o crédito; o BC credita "
                            "reservas em vez de entregar cédulas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 487", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (setor bancário × não bancário, no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00345
    {
        "id": "ECO-E3-L00345-1", "fonte_ref": "E3-L00345", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_D24,
        "rotulo_item": "Item",
        "assertiva": ("A elevação na taxa de juros de mercado leva ao aumento na demanda por moeda pela população, "
                      "que preferirá pagar as próprias compras à vista e não fazer financiamentos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elevação na taxa de juros de mercado leva ") + vm("ao aumento") + az(" na demanda por "
                       "moeda pela população, que preferirá ") + vm("pagar as próprias compras à vista e não "
                                                                    "fazer financiamentos") + az(".")),
        "poucas": ("Os juros são o " + azb("custo de oportunidade") + " de reter moeda: se sobem, manter "
                   "dinheiro parado fica caro, e a demanda por moeda <b>cai</b>."),
        "destrinchando": [
            "Moeda (papel-moeda e depósito à vista) rende zero ou quase zero; títulos e aplicações rendem i. Cada "
            "real retido como moeda “custa” os juros que deixou de render. Logo, " + vd("i ↑ → L ↓") + ": a "
            "demanda por moeda é negativamente inclinada em relação aos juros.",
            "Em " + oc("Keynes") + ", o canal é o " + azb("motivo especulação") + ": com juros altos (preço dos "
            "títulos baixo), vale a pena trocar moeda por títulos. Em " + oc("Baumol") + "–" + oc("Tobin")
            + ", até a moeda para transações cai: com i alto, compensa ir mais vezes ao banco e manter saldo "
            "médio menor.",
            "O argumento do item confunde <b>decisão de financiamento</b> com <b>demanda por saldos "
            "monetários</b>. Juros altos desestimulam o crédito ao consumo, mas isso reduz compras financiadas; "
            "não faz as pessoas guardarem mais moeda — quem tem recursos prefere aplicá-los.",
            "No IS-LM, essa sensibilidade é o que dá inclinação à LM: L = kY − hi.",
            vm("Regra-âncora: juros ↑ → custo de reter moeda ↑ → demanda por moeda ↓."),
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " Inverte a relação juros × demanda por moeda e a "
                       "sustenta com uma história plausível do cotidiano (“pagar à vista para fugir dos "
                       "juros”). A justificativa intuitiva é a isca: em demanda por moeda, pense sempre em "
                       "custo de oportunidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação da taxa de juros reduz a demanda especulativa por moeda.”</i> → CERTO",
            "<i>“Na armadilha da liquidez, a demanda por moeda é totalmente insensível aos juros.”</i> → ERRADO "
            "(inversão: é infinitamente elástica aos juros)",
        ])],
        "reescrita": ("A elevação na taxa de juros de mercado leva " + hl("à redução") + " na demanda por moeda "
                      "pela população, que preferirá " + hl("aplicar seus recursos em ativos remunerados, pois "
                                                            "sobe o custo de oportunidade de reter moeda") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Cinco comentários fundidos: juros = custo de oportunidade de reter moeda; "
                            "juros ↑ reduzem a demanda; o argumento do pagamento à vista confunde financiamento "
                            "com demanda por saldos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 488", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mercado monetário e LM após contração da oferta de moeda; não "
                                   "testa o item)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00441
    {
        "id": "ECO-E3-L00441-1", "fonte_ref": "E3-L00441", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI_F26,
        "rotulo_item": "Item",
        "assertiva": ("A elevação da taxa de recolhimento compulsório sobre os depósitos à vista, acompanhada de um "
                      "aumento da base monetária em montante idêntico à elevação das reservas bancárias, não altera "
                      "os meios de pagamento, ceteris paribus."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elevação da taxa de recolhimento compulsório sobre os depósitos à vista, acompanhada de "
                      "um aumento da base monetária <u>em montante idêntico à elevação das reservas "
                      "bancárias</u>, não altera os meios de pagamento, <u>ceteris paribus</u>."),
        "poucas": ("O compulsório maior exige mais reservas; o BC fornece <b>exatamente</b> essas reservas. Os "
                   "bancos não precisam cortar crédito, e PMPP e DV — logo o " + azb("M1") + " — ficam iguais."),
        "destrinchando": [
            "Dois efeitos em sentidos opostos: (1) compulsório ↑ → coeficiente de reservas r ↑ → "
            + azb("multiplicador ↓") + " (efeito contracionista); (2) base ↑ (efeito expansionista). Como "
            + vd("M1 = m × B") + ", o resultado depende do tamanho de cada um.",
            "O item calibra a injeção: a base sobe no <b>mesmo valor</b> que as reservas exigidas. Exemplo: DV = "
            "100, PMPP = 50, compulsório de 10% → 20%. As reservas precisam ir de 10 para 20; o BC injeta 10 "
            "(comprando títulos dos bancos, por exemplo). B: 60 → 70; m: 150/60 = 2,5 → 150/70 ≈ 2,14; M1 = "
            + vd("150") + " nos dois casos.",
            "Leitura contábil: os 10 novos de base ficam “presos” como reserva compulsória — nenhum real chega "
            "ao público nem sai dele. É uma troca de ativos dentro do setor bancário.",
            "Uso real dessa combinação: elevar reservas por razão prudencial (colchão de liquidez) sem provocar "
            "contração do crédito — ou, ao contrário, esterilizar uma injeção de base com compulsório.",
            "Objeções levantadas contra o item: a base poderia crescer via PMPP, e não via reservas; e os bancos "
            "poderiam reagir elevando reservas voluntárias. Ambas saem do <i>ceteris paribus</i> e do “montante "
            "idêntico à elevação das reservas”, que o item fixa.",
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " Quem decorou “compulsório ↑ = contração” marca "
                       "ERRADO sem ler a segunda oração. O detalhe decisivo é “em montante idêntico à elevação "
                       "das reservas”: a nova base é totalmente absorvida pelo novo compulsório."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação da taxa de recolhimento compulsório sobre os depósitos à vista, mantida constante "
            "a base monetária, reduz os meios de pagamento.”</i> → CERTO",
            "<i>“…acompanhada de aumento da base em montante idêntico, eleva os meios de pagamento, pois a base "
            "cresceu.”</i> → ERRADO (ignora a queda do multiplicador)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["ceteris paribus"], "dificuldade": 3,
        "comentario_fonte": "CERTO. Comentários fundidos: M1 = PMPP + DV inalterado porque a injeção cobre "
                            "exatamente as novas reservas; resolução de origem (ANPEC) que fala em efeitos que se "
                            "compensam; discussão sobre não linearidade do multiplicador e possíveis recursos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 604", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (efeitos que se compensam, no 📖)"},
                          {"ref": "IMAGEM 605–610", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "cortadas (esquemas base × meios de pagamento descritos no 📖)"},
                          {"ref": "IMAGEM 611–614", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (resumo da dinâmica e objeções, no 📖)"}],
        "alertas": ["nota_redacao: a fonte cogita recurso; o gabarito CERTO foi mantido porque as objeções "
                    "violam as hipóteses do próprio item"],
    },
    # ------------------------------------------------------------------ E3-L00443
    {
        "id": "ECO-E3-L00443-1", "fonte_ref": "E3-L00443", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_F26,
        "rotulo_item": "Item",
        "assertiva": ("A compra de títulos no mercado aberto pelo Banco Central terá maior impacto sobre os meios de "
                      "pagamento quanto maior for a fração de moeda retida pelo público na forma manual, ceteris "
                      "paribus."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A compra de títulos no mercado aberto pelo Banco Central terá ") + vm("maior")
                    + az(" impacto sobre os meios de pagamento quanto maior for a fração de moeda retida pelo "
                         "público na forma manual, ceteris paribus.")),
        "poucas": ("Moeda retida na mão do público é " + azb("vazamento") + ": não volta aos bancos para ser "
                   "reemprestada. Quanto mais retenção manual, " + azb("menor o multiplicador") + " e menor o "
                   "efeito da compra de títulos sobre o M1."),
        "destrinchando": [
            "A compra de títulos pelo BC injeta base: " + vd("ΔM1 = m × ΔB") + ". O tamanho do efeito depende "
            "do multiplicador " + vd("m = (1 + c) / (c + r)") + ", que cai quando c (PMPP/DV) sobe.",
            "Formulação alternativa, com d = fração da moeda que o público deposita e R = fração dos depósitos "
            "retida como reserva: " + vd("m = 1 / [1 − d(1 − R)]") + ". Com R = 0,2: se o público deposita "
            "tudo (d = 1), m = " + vd("5") + "; se deposita metade (d = 0,5), m ≈ " + vd("1,67") + ". Com R = "
            "0,4 e d = 0,5, m ≈ " + vd("1,43") + ".",
            "A intuição é a da cadeia de empréstimos: cada real emprestado vira depósito só na parte que o "
            "público não guarda em espécie. Retenção alta corta a corrente logo nas primeiras rodadas.",
            "Por isso a " + azb("bancarização") + " e os meios eletrônicos de pagamento (cartões, PIX) tendem a "
            "elevar o multiplicador: menos papel-moeda retido, mais depósitos reemprestáveis.",
            vm("Regra-âncora: tudo o que fica fora dos bancos (papel-moeda retido, reservas) reduz o "
               "multiplicador."),
        ],
        "dissecando": (cz("[inversão]") + " Troca “menor” por “maior” numa relação proporcional. O "
                       "<i>ceteris paribus</i> e a linguagem técnica (“forma manual”) dão ar de rigor, mas o "
                       "sentido do efeito está invertido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a fração dos depósitos mantida como reserva pelos bancos, menor o efeito de uma "
            "compra de títulos sobre os meios de pagamento.”</i> → CERTO",
            "<i>“A compra de títulos no mercado aberto reduz a base monetária.”</i> → ERRADO (inversão: compra "
            "injeta base; venda enxuga)",
        ])],
        "reescrita": ("A compra de títulos no mercado aberto pelo Banco Central terá " + hl("menor") + " impacto "
                      "sobre os meios de pagamento quanto maior for a fração de moeda retida pelo público na forma "
                      "manual, ceteris paribus."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["ceteris paribus"], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Quatro comentários fundidos: retenção manual é vazamento e reduz o "
                            "multiplicador; fórmulas m = (1 + c)/(c + r) e m = 1/[1 − d(1 − R)] com exemplos "
                            "numéricos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 618–619", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (fórmula e exemplos numéricos no 📖)"},
                          {"ref": "IMAGEM 620–621", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (intuição no 📖)"},
                          {"ref": "IMAGEM 622", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (quadro dos agregados M1–M4, alheio ao item)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00444
    {
        "id": "ECO-E3-L00444-1", "fonte_ref": "E3-L00444", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_F26,
        "rotulo_item": "Item",
        "assertiva": ("Há destruição de meios de pagamento quando um indivíduo realiza um depósito à vista em um "
                      "banco comercial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Há destruição") + az(" de meios de pagamento quando um indivíduo realiza um depósito à "
                                             "vista em um banco comercial.")),
        "poucas": ("Depositar cédulas em conta corrente só troca a " + azb("forma") + " da moeda: PMPP ↓ e DV ↑ "
                   "no mesmo valor. M1 = PMPP + DV " + vd("não muda") + "."),
        "destrinchando": [
            "Exemplo: João deposita R$ 1.000 que guardava em casa. PMPP: −1.000; DV: +1.000; " + vd("ΔM1 = 0")
            + ". A moeda passa de manual a escritural, mas continua sendo do público e continua líquida.",
            "Criação ou destruição de M1 exige troca entre o " + azb("setor bancário") + " e o " + azb("setor "
            "não bancário") + " que altere o estoque de liquidez em poder do público.",
            "<b>Destroem</b> M1: quitação de empréstimo bancário; compra de títulos vendidos pelo BC (open market "
            "contracionista); pagamento de tributos que vai à Conta Única no BC; transferência da conta "
            "corrente para poupança ou CDB (o recurso sai do M1 e passa a M2).",
            "<b>Criam</b> M1: concessão de crédito (o banco credita a conta do tomador); compra de títulos ou de "
            "divisas pelo BC junto ao público.",
            "Efeito posterior: com mais depósitos, o banco pode emprestar mais — o depósito abre caminho para "
            "<b>criação</b>, não para destruição, de moeda via multiplicador.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Confunde o depósito à vista (que fica no M1) com o depósito "
                       "a prazo ou em poupança (que sai do M1). Pergunta-teste: o dinheiro continua do público "
                       "e com liquidez imediata? Se sim, M1 não mudou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Há destruição de meios de pagamento quando um indivíduo transfere recursos da conta corrente "
            "para a caderneta de poupança.”</i> → CERTO",
            "<i>“Há criação de meios de pagamento quando um banco comercial concede empréstimo creditando a "
            "conta corrente do tomador.”</i> → CERTO",
        ])],
        "reescrita": (hl("Não há criação nem destruição") + " de meios de pagamento quando um indivíduo realiza um "
                      "depósito à vista em um banco comercial" + hl(": muda apenas a composição do M1 (PMPP ↓, "
                                                                     "DV ↑)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Vários comentários fundidos: depósito à vista é fato permutativo em M1; "
                            "listas de operações que criam e destroem meios de pagamento.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 623–625", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (regra da troca entre setores, no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0308
    {
        "id": "ECO-E1-0308-1", "fonte_ref": "E1-0308", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_BC,
        "rotulo_item": "Item",
        "assertiva": ("Em sua função de “banco dos bancos”, cabe ao Banco Central do Brasil (BCB) formar um "
                      "“colchão de liquidez” para o sistema financeiro, de modo que, em momentos de incerteza e de "
                      "liquidez restrita, ele possa reduzir o montante dos recolhimentos compulsórios e liberar "
                      "recursos para as instituições financeiras, a exemplo do que fez para mitigar os efeitos da "
                      "crise de 2008 sobre a economia brasileira."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em sua função de <u>“banco dos bancos”</u>, cabe ao Banco Central do Brasil (BCB) formar "
                      "um “colchão de liquidez” para o sistema financeiro, de modo que, em momentos de incerteza e "
                      "de liquidez restrita, ele possa <u>reduzir o montante dos recolhimentos compulsórios</u> e "
                      "liberar recursos para as instituições financeiras, a exemplo do que fez para mitigar os "
                      "efeitos da crise de <u>2008</u> sobre a economia brasileira."),
        "poucas": ("Os " + azb("recolhimentos compulsórios") + " funcionam também como reserva de emergência: em "
                   "crise, o BC os reduz e devolve liquidez aos bancos — foi o que o " + rx("BCB") + " fez em "
                   + vd("2008") + "."),
        "destrinchando": [
            "Como " + azb("banco dos bancos") + ", o BC guarda as reservas das instituições financeiras, opera "
            "a liquidação entre elas e lhes empresta (redesconto). Daí o papel de " + azb("emprestador de "
            "última instância") + ": prover liquidez a bancos solventes quando o mercado interbancário trava.",
            "A lição vem da Grande Depressão: na leitura de " + oc("Friedman") + " e " + oc("Schwartz")
            + " (<i>A Monetary History of the United States</i>, 1963), o Fed deixou a onda de quebras bancárias "
            "de 1930–33 contrair a oferta de moeda. A doutrina do emprestador de última instância remonta a "
            + oc("Bagehot") + " (<i>Lombard Street</i>, 1873).",
            "O compulsório nasceu como instrumento de controle monetário (afeta o multiplicador), mas o "
            + rx("BCB") + " passou a tratá-lo também como " + azb("instrumento prudencial") + ": recolhe-se em "
            "tempos normais e libera-se nas crises.",
            "Em 2008, após a quebra do Lehman Brothers, o crédito externo e o interbancário secaram; o BCB "
            "reduziu alíquotas e criou deduções do compulsório para que os grandes bancos comprassem carteiras "
            "dos pequenos, irrigando o sistema. O mesmo recurso voltou a ser usado na pandemia, em 2020.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a explicação institucional do BCB sobre os "
                       "compulsórios. O risco é o candidato pensar só no uso contracionista do compulsório e "
                       "estranhar a ideia de “colchão”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…em momentos de liquidez restrita, o BCB eleva os recolhimentos compulsórios para proteger o "
            "sistema financeiro.”</i> → ERRADO (inversão: em crise de liquidez, reduz)",
            "<i>“A função de emprestador de última instância é exercida pelo BCB por meio do redesconto.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["possa"], "dificuldade": 1,
        "comentario_fonte": "Correto. Comentário sobre a máxima do emprestador de última instância derivada da "
                            "interpretação da crise de 1929 (fala pouco do compulsório).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [PROV(2017)],
    },
    # ------------------------------------------------------------------ E1-0313
    {
        "id": "ECO-E1-0313-1", "fonte_ref": "E1-0313", "destino": "36", "subtema": H2["bc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_BC,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central do Brasil é a instituição do país que desempenha as funções de monopólio de "
                      "emissão, banqueiro do governo, banco dos bancos, supervisor do sistema financeiro e executor "
                      "da política monetária. A formulação da política cambial e a responsabilidade pela "
                      "administração das reservas internacionais ficam a cargo do Ministério da Fazenda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Banco Central do Brasil é a instituição do país que desempenha as funções de monopólio "
                       "de emissão, banqueiro do governo, banco dos bancos, supervisor do sistema financeiro e "
                       "executor da política monetária. A formulação da política cambial e a responsabilidade "
                       "pela administração das reservas internacionais ficam a cargo ")
                    + vm("do Ministério da Fazenda") + az(".")),
        "poucas": ("A 1ª frase está certa; a 2ª, não: formular e executar a " + azb("política cambial") + " e "
                   "administrar as " + azb("reservas internacionais") + " são competências do " + rx("BCB")
                   + ", e não do Ministério da Fazenda."),
        "destrinchando": [
            "As funções clássicas de um banco central: " + azb("monopólio de emissão") + "; " + azb("banqueiro "
            "do governo") + " (guarda a Conta Única do Tesouro, CF art. 164, § 3º); " + azb("banco dos bancos")
            + " (reservas, redesconto, compulsório); " + azb("supervisor do sistema financeiro") + "; "
            + azb("executor da política monetária") + "; e " + azb("depositário das reservas internacionais")
            + " e executor da política cambial.",
            "A " + vd("Lei 4.595/1964") + " (art. 10, VIII) dá ao BC, privativamente, a função de ser "
            "depositário das reservas oficiais de ouro, moeda estrangeira e DES. É ele quem compra e vende "
            "divisas, faz swaps cambiais e aplica as reservas.",
            "Divisão de papéis: o " + azb("CMN") + " (órgão normativo) fixa diretrizes gerais da política "
            "monetária, creditícia e cambial; o BC formula, executa e acompanha. O Ministério da Fazenda preside "
            "o CMN, mas não administra as reservas.",
            "Desde a " + vd("LC 179/2021") + ", o BCB é autarquia de natureza especial, sem vinculação a "
            "ministério, com mandatos fixos para a diretoria.",
        ],
        "dissecando": (cz("[troca de ator · meia-verdade]") + " A 1ª frase, longa e correta, dá confiança; o "
                       "erro está no ator da 2ª. Pista: política cambial e reservas andam juntas — quem "
                       "intervém no câmbio usa as reservas, e quem as usa é o BC."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Cabe ao Conselho Monetário Nacional fixar as diretrizes da política cambial.”</i> → CERTO",
            "<i>“As reservas internacionais do Brasil são administradas pelo Tesouro Nacional.”</i> → ERRADO "
            "(troca de ator: BCB)",
        ])],
        "reescrita": ("O Banco Central do Brasil é a instituição do país que desempenha as funções de monopólio de "
                      "emissão, banqueiro do governo, banco dos bancos, supervisor do sistema financeiro e executor "
                      "da política monetária. A formulação da política cambial e a responsabilidade pela "
                      "administração das reservas internacionais ficam a cargo " + hl("do próprio Banco Central do "
                                                                                        "Brasil") + "."),
        "tipo_erro": ["TROCA_ATOR", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Errado. Vários comentários fundidos: BC formula e executa a política cambial e "
                            "administra as reservas; lista de atribuições da Lei 4.595/1964 e do site do BCB.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [PROV(2014)],
    },
    # ------------------------------------------------------------------ E1-0368
    {
        "id": "ECO-E1-0368-1", "fonte_ref": "E1-0368", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à política monetária em economia aberta.",
        "rotulo_item": "Item",
        "assertiva": ("Caso esteja vendendo divisas estrangeiras e reduzindo sua oferta de moeda nacional, o BACEN "
                      "poderá contrabalançar essa redução por meio de operações de venda de títulos no mercado, "
                      "visto que os recursos auferidos por tais operações aumentarão a oferta de moeda na "
                      "economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Caso esteja vendendo divisas estrangeiras e reduzindo sua oferta de moeda nacional, o "
                       "BACEN poderá contrabalançar essa redução por meio de operações de ") + vm("venda")
                    + az(" de títulos no mercado, visto que os recursos ") + vm("auferidos")
                    + az(" por tais operações aumentarão a oferta de moeda na economia.")),
        "poucas": ("Vender títulos <b>retira</b> moeda (o BC recebe reais). Para compensar o enxugamento "
                   "causado pela venda de divisas, o BC teria de " + azb("comprar") + " títulos — a "
                   + azb("esterilização") + "."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "a questão original, de múltipla escolha, foi " + azb("anulada") + " por motivo alheio "
                          "a esta alternativa (imprecisão, em outra opção, na definição de produto nacional "
                          "bruto). No mérito, esta afirmação é falsa, e o card a mantém como ERRADO.")],
        "destrinchando": [
            "Quando o BC <b>vende divisas</b> (para segurar a alta do dólar), recebe reais em troca: a base "
            "monetária cai. Quando <b>compra divisas</b>, emite reais: a base sobe.",
            azb("Esterilização") + " = neutralizar esse efeito monetário com operação de mercado aberto no "
            "sentido oposto. Venda de divisas (enxuga) → " + vd("compra de títulos") + " (injeta). Compra de "
            "divisas (injeta) → " + vd("venda de títulos") + " (enxuga) — foi o que o " + rx("BCB") + " fez "
            "na fase de acumulação de reservas dos anos 2000, à custa de dívida bruta maior.",
            "Na venda de títulos, os recursos são <b>pagos ao BC</b> pelo mercado e saem de circulação; a oferta "
            "de moeda cai. O item inverte o fluxo ao dizer que os recursos “auferidos” aumentariam a moeda.",
            "Por que esterilizar: manter a taxa de juros na meta. Sem esterilização, a venda de reservas "
            "elevaria os juros (menos liquidez); com ela, o BC separa a política cambial da monetária.",
            vm("Regra-âncora: divisas e títulos — compra injeta moeda, venda enxuga; esterilizar é fazer o "
               "contrário com títulos."),
        ],
        "dissecando": (cz("[inversão]") + " O item escolhe a operação certa (mercado aberto) e o sentido errado, "
                       "e “justifica” a escolha invertendo quem recebe o dinheiro. Pista: se o BC <b>aufere</b> "
                       "recursos, eles saíram do mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para esterilizar o efeito monetário da compra de divisas, o BACEN pode vender títulos públicos "
            "no mercado.”</i> → CERTO",
            "<i>“A venda de divisas pelo BACEN expande a base monetária.”</i> → ERRADO (inversão: retira reais "
            "de circulação)",
        ])],
        "reescrita": ("Caso esteja vendendo divisas estrangeiras e reduzindo sua oferta de moeda nacional, o BACEN "
                      "poderá contrabalançar essa redução por meio de operações de " + hl("compra") + " de "
                      "títulos no mercado, visto que os recursos " + hl("pagos") + " por tais operações aumentarão "
                      "a oferta de moeda na economia."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["poderá"], "dificuldade": 1,
        "comentario_fonte": "Incorreta: para contrabalançar, o BC deveria comprar títulos. Nota de que a questão "
                            "(ME) foi anulada por imprecisão na definição de PNB em outra alternativa.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: questão original (múltipla escolha) anulada por motivo alheio a esta "
                    "alternativa (definição de PNB); no mérito, a alternativa é falsa e o card mantém ERRADO",
                    PROV(2010)],
    },
    # ------------------------------------------------------------------ E1-0387
    {
        "id": "ECO-E1-0387-1", "fonte_ref": "E1-0387", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("Uma intensificação na venda de títulos públicos caracteriza um expansionismo monetário com "
                      "ampliação dos meios de pagamento e redução dos juros de mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma intensificação na venda de títulos públicos caracteriza ") + vm("um expansionismo")
                    + az(" monetário com ") + vm("ampliação") + az(" dos meios de pagamento e ")
                    + vm("redução") + az(" dos juros de mercado.")),
        "poucas": ("Vender títulos = o BC recebe moeda e a retira de circulação: política " + azb("contracionista")
                   + ", com menos meios de pagamento e " + vd("juros mais altos") + "."),
        "destrinchando": [
            "Nas " + azb("operações de mercado aberto") + " (open market), o BC compra ou vende títulos "
            "públicos. <b>Venda</b>: o comprador paga com reservas/depósitos → base e meios de pagamento caem. "
            "<b>Compra</b>: o BC paga com moeda nova → base e meios de pagamento sobem.",
            "Efeito sobre os juros: mais títulos ofertados derrubam seu preço, e preço do título e taxa de juros "
            "andam em sentidos opostos → " + vd("i ↑") + ". No IS-LM, a LM se desloca para a esquerda: i ↑ e "
            "Y ↓.",
            "No regime de metas do " + rx("BCB") + ", o open market (sobretudo as " + azb("operações "
            "compromissadas") + ") é o instrumento que mantém a taxa Selic efetiva na meta do Copom: se há "
            "excesso de reservas pressionando a Selic para baixo, o BC vende títulos para enxugar.",
            vm("Regra-âncora: BC vende título → enxuga moeda → juros sobem."),
        ],
        "dissecando": (cz("[inversão]") + " Todas as consequências foram invertidas de forma coerente entre si, "
                       "o que dá ao item aparência de lógica. Basta checar o ponto de partida: quem compra o "
                       "título paga ao BC com moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma intensificação na compra de títulos públicos pelo Banco Central caracteriza expansionismo "
            "monetário, com ampliação dos meios de pagamento e redução dos juros.”</i> → CERTO",
            "<i>“A venda de títulos pelo Banco Central desloca a curva IS para a esquerda.”</i> → ERRADO (curva "
            "trocada: é a LM)",
        ])],
        "reescrita": ("Uma intensificação na venda de títulos públicos caracteriza " + hl("um contracionismo")
                      + " monetário com " + hl("redução") + " dos meios de pagamento e " + hl("elevação")
                      + " dos juros de mercado."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Só o gabarito (ERRADO), uma imagem não preservada e o link do canal.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (132).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; conteúdo refeito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0445
    {
        "id": "ECO-E1-0445-1", "fonte_ref": "E1-0445", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": CMD_CLIP,
        "rotulo_item": "Item",
        "assertiva": ("O controle da base monetária pelo Banco Central é realizado exclusivamente por meio da "
                      "fixação da taxa de juros de referência."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O controle da base monetária pelo Banco Central é realizado ") + vm("exclusivamente por "
                       "meio da fixação da taxa de juros de referência") + az(".")),
        "poucas": ("O BC dispõe de um " + azb("conjunto de instrumentos") + " — mercado aberto, compulsório, "
                   "redesconto — além da taxa básica; o “exclusivamente” derruba o item."),
        "destrinchando": [
            "Instrumentos clássicos de política monetária: " + vd("operações de mercado aberto") + " (compra e "
            "venda de títulos), " + vd("recolhimentos compulsórios") + ", " + vd("redesconto") + " (empréstimos "
            "de liquidez aos bancos), além da emissão e da regulação do crédito.",
            "A taxa de juros de referência (a " + rx("Selic") + ", no Brasil) é uma <b>meta</b>, não um "
            "decreto: o Copom anuncia a meta, e a mesa do BC faz operações de mercado aberto (compromissadas) "
            "para que a Selic efetiva fique nela. Ou seja, até a fixação dos juros depende do open market.",
            "Quando o BC fixa os juros, a base monetária torna-se " + azb("endógena") + ": ela se ajusta à "
            "demanda por reservas compatível com a taxa escolhida. O BC pode mirar a quantidade (base) ou o "
            "preço (juros), não os dois ao mesmo tempo de forma independente.",
            "Em crises, entram ainda instrumentos de liquidez (redesconto ampliado, liberação de compulsório).",
        ],
        "dissecando": (cz("[modulador absoluto]") + " A taxa de juros é, de fato, o principal instrumento "
                       "moderno; o erro está no “exclusivamente”, que apaga os demais. 🔥 Em itens sobre "
                       "instrumentos, desconfie de “exclusivamente”, “apenas” e “somente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de metas, o BC usa operações de mercado aberto para manter a taxa básica de juros "
            "próxima da meta.”</i> → CERTO",
            "<i>“O BC consegue fixar, simultânea e independentemente, a taxa de juros e o volume da base "
            "monetária.”</i> → ERRADO (fixado o preço, a quantidade se ajusta à demanda)",
        ])],
        "reescrita": ("O controle da base monetária pelo Banco Central é realizado " + hl("por um conjunto de "
                      "instrumentos — operações de mercado aberto, recolhimentos compulsórios e redesconto —, ao "
                      "lado da fixação da taxa de juros de referência") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": "ERRADO. O BC usa um conjunto de instrumentos: mercado aberto, compulsórios, "
                            "redesconto, além da taxa básica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0447
    {
        "id": "ECO-E1-0447-1", "fonte_ref": "E1-0447", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": CMD_CLIP,
        "rotulo_item": "Item",
        "assertiva": ("O canal do crédito na transmissão da política monetária torna-se mais relevante quando as "
                      "instituições financeiras operam com alta liquidez e baixo risco de inadimplência."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O canal do crédito na transmissão da política monetária torna-se <u>mais relevante</u> "
                      "quando as instituições financeiras operam com <u>alta liquidez e baixo risco de "
                      "inadimplência</u>."),
        "poucas": ("Bancos líquidos e confiantes nos tomadores repassam a política monetária ao " + azb("volume "
                   "de crédito") + " com mais facilidade: o " + azb("canal do crédito") + " ganha força."),
        "destrinchando": [
            "Canais de transmissão da política monetária: " + azb("juros") + " (custo do capital → investimento "
            "e consumo), " + azb("câmbio") + ", " + azb("preços de ativos") + " (riqueza, q de Tobin), "
            + azb("expectativas") + " e " + azb("crédito") + ".",
            "O canal do crédito, associado a " + oc("Bernanke") + " e " + oc("Gertler") + ", tem duas vertentes: "
            "<b>empréstimos bancários</b> (a política altera a capacidade e a disposição dos bancos de emprestar) "
            "e <b>balanço</b> (juros e preços de ativos alteram o patrimônio e as garantias dos tomadores).",
            "Com liquidez farta e baixa inadimplência, um corte de juros vira oferta de crédito; com bancos "
            "descapitalizados ou avessos ao risco, o estímulo “empoça” nas reservas — situação do pós-2008, "
            "descrita como “empurrar uma corda”.",
            "No Brasil, a eficácia do canal é limitada pela segmentação do crédito: parte relevante é "
            + rx("crédito direcionado") + " (BNDES, rural, habitacional), menos sensível à Selic — tema "
            "recorrente nos " + rx("Relatórios de Política Monetária") + " do BCB.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Afirmação comparativa (“mais relevante”), "
                       "não absoluta. A dúvida possível é achar que bancos líquidos “não precisam” da política; "
                       "é o contrário: são eles que conseguem transformá-la em crédito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O canal do crédito ganha força quando os bancos enfrentam escassez de capital e alta "
            "inadimplência.”</i> → ERRADO (inversão: o estímulo empoça)",
            "<i>“A existência de crédito direcionado reduz a potência da política monetária no Brasil.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["mais relevante"],
        "dificuldade": 2,
        "comentario_fonte": "CERTO. Bancos líquidos e confiantes transformam corte de juros em expansão do "
                            "crédito (verso idêntico ao da linha duplicada E1-0549).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["duplicata: linha E1-0549 fundida neste card (mesmo item e mesmo comentário)"],
    },
    # ------------------------------------------------------------------ E1-0501
    {
        "id": "ECO-E1-0501-1", "fonte_ref": "E1-0501", "destino": "36", "subtema": H2["bc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_BC,
        "rotulo_item": "Item",
        "assertiva": ("Ao Banco Central do Brasil cabe decidir a meta para a inflação, as diretrizes para o câmbio "
                      "e as normas principais para o funcionamento das instituições financeiras, entre outras "
                      "atribuições."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Ao Banco Central do Brasil") + az(" cabe decidir a meta para a inflação, as diretrizes "
                       "para o câmbio e as normas principais para o funcionamento das instituições financeiras, "
                       "entre outras atribuições.")),
        "poucas": ("Quem <b>decide</b> é o " + azb("Conselho Monetário Nacional (CMN)") + ", órgão normativo; "
                   "o " + rx("BCB") + " executa e supervisiona."),
        "destrinchando": [
            "Arquitetura do Sistema Financeiro Nacional: " + azb("órgãos normativos") + " (CMN, CNSP, CNPC) "
            "fixam as regras; " + azb("supervisores") + " (BCB, CVM, Susep, Previc) as aplicam e fiscalizam; "
            "os " + azb("operadores") + " (bancos, corretoras etc.) atuam no mercado.",
            "O texto do item é quase literal do site do BCB — com o ator trocado: “É no CMN que se decide a meta "
            "para a inflação, as diretrizes para o câmbio e as normas principais para o funcionamento das "
            "instituições financeiras.”",
            "Composição do CMN ⏳ (out/2026): " + vd("ministro da Fazenda") + " (presidente), "
            + vd("ministro do Planejamento e Orçamento") + " e " + vd("presidente do BCB") + ".",
            "Meta de inflação ⏳ (out/2026): desde 2025 vigora a " + azb("meta contínua") + " de " + vd("3%")
            + " ao ano pelo IPCA, com tolerância de 1,5 p.p., aferida mês a mês em janela de 12 meses. Cabe ao "
            "BCB, via Copom, calibrar a Selic para cumpri-la.",
            "A " + vd("LC 179/2021") + " deu autonomia ao BCB (mandatos fixos, objetivo fundamental de "
            "estabilidade de preços), mas não lhe transferiu a definição da meta.",
        ],
        "dissecando": (cz("[troca de ator]") + " Copia a frase oficial que descreve o CMN e põe o BCB como "
                       "sujeito. Pista: o verbo “decidir” (normativo) × “executar/fiscalizar” (BCB). 🔥 Tema "
                       "recorrente: CMN fixa a meta, BCB persegue."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Compete ao Banco Central do Brasil, por meio do Copom, definir a meta para a taxa Selic com "
            "vistas a cumprir a meta de inflação fixada pelo CMN.”</i> → CERTO",
            "<i>“O presidente do Banco Central preside o Conselho Monetário Nacional.”</i> → ERRADO (troca de "
            "ator: preside o ministro da Fazenda)",
        ])],
        "reescrita": (hl("Ao Conselho Monetário Nacional") + " cabe decidir a meta para a inflação, as diretrizes "
                      "para o câmbio e as normas principais para o funcionamento das instituições financeiras, "
                      "entre outras atribuições."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Errado. Vários comentários fundidos: o CMN decide meta, diretrizes cambiais e normas; "
                            "BCB executa e fiscaliza; composição do CMN e metas 2021–2024 (já desatualizadas).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [PROV(2022)],
    },
    # ------------------------------------------------------------------ E1-0514
    {
        "id": "ECO-E1-0514-1", "fonte_ref": "E1-0514", "destino": "36", "subtema": H2["bc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às funções dos bancos centrais.",
        "rotulo_item": "Item",
        "assertiva": ("Como guardião da moeda, o banco central de um país é a instituição à qual se confia o dever "
                      "de regular o volume de dinheiro e de crédito da economia. Em que pesem as diferenças entre "
                      "bancos centrais, essa atribuição geralmente está associada ao objetivo de assegurar a "
                      "estabilidade do poder de compra da moeda nacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Como guardião da moeda, o banco central de um país é a instituição à qual se confia o "
                      "dever de regular o volume de dinheiro e de crédito da economia. Em que pesem as diferenças "
                      "entre bancos centrais, essa atribuição <u>geralmente</u> está associada ao objetivo de "
                      "assegurar a <u>estabilidade do poder de compra</u> da moeda nacional."),
        "poucas": ("É a definição do próprio " + rx("BCB") + ": o banco central regula moeda e crédito, em geral "
                   "com o objetivo de " + azb("estabilidade de preços") + " (poder de compra da moeda)."),
        "destrinchando": [
            "O item reproduz quase literalmente as “Perguntas mais frequentes” do BCB sobre as funções do banco "
            "central: regular o volume de dinheiro e de crédito, associado ao objetivo de assegurar a "
            "estabilidade do poder de compra da moeda.",
            "Para regular moeda e crédito, o BC controla a " + azb("base monetária") + " e influencia o "
            + azb("multiplicador") + " (compulsório, redesconto, mercado aberto) — hoje, sobretudo, fixando a "
            "taxa básica de juros.",
            "No Brasil, a " + vd("LC 179/2021") + " (art. 1º) fixa como objetivo fundamental do BCB “assegurar a "
            "estabilidade de preços” e, sem prejuízo dele, zelar pela estabilidade e eficiência do sistema "
            "financeiro, suavizar as flutuações da atividade e fomentar o pleno emprego.",
            "Por que “em que pesem as diferenças”: mandatos variam. O " + azb("Fed") + " tem mandato dual "
            "(preços estáveis e máximo emprego); o " + azb("BCE") + " tem a estabilidade de preços como "
            "objetivo primordial. O item usa “geralmente”, o que acomoda essa variação.",
            "Contexto brasileiro: a experiência da hiperinflação (anos 1980 e início dos 1990) explica o peso "
            "dado à âncora nominal desde o " + rx("Plano Real") + " e o regime de metas de 1999.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Texto institucional, protegido por "
                       "“geralmente” e “em que pesem as diferenças”. Desconfiança indevida pode vir do mandato "
                       "dual do Fed; o item não diz que estabilidade de preços é o objetivo único."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todos os bancos centrais têm a estabilidade de preços como objetivo único.”</i> → ERRADO "
            "(modulador absoluto: o Fed tem mandato dual)",
            "<i>“Pela LC 179/2021, o BCB deve, sem prejuízo da estabilidade de preços, fomentar o pleno "
            "emprego.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["geralmente", "em que pesem"],
        "dificuldade": 1,
        "comentario_fonte": "Correto. Vários comentários fundidos: missão de estabilidade do poder de compra, "
                            "trecho das FAQ do BCB, LC 179/2021, funções clássicas do BC (Vasconcellos).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [PROV(2018)],
    },
    # ------------------------------------------------------------------ E1-0515
    {
        "id": "ECO-E1-0515-1", "fonte_ref": "E1-0515", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("A política monetária influencia a evolução dos meios de pagamento e controla o processo de "
                      "criação da moeda e do crédito. Na função de executor da política monetária, o BCB, para "
                      "regular os meios de pagamentos, pode utilizar instrumentos clássicos, como encaixe legal, "
                      "recolhimentos compulsórios, redesconto, excetuando-se as operações de mercado aberto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A política monetária influencia a evolução dos meios de pagamento e controla o processo "
                       "de criação da moeda e do crédito. Na função de executor da política monetária, o BCB, "
                       "para regular os meios de pagamentos, pode utilizar instrumentos clássicos, como encaixe "
                       "legal, recolhimentos compulsórios, redesconto, ") + vm("excetuando-se as")
                    + az(" operações de mercado aberto.")),
        "poucas": ("As " + azb("operações de mercado aberto") + " não só são instrumento clássico como são o "
                   "<b>principal</b> deles; excluí-las torna o item falso."),
        "destrinchando": [
            "Os três instrumentos clássicos de controle monetário: " + vd("encaixe legal / recolhimento "
            "compulsório") + " (a mesma coisa — o item os lista como se fossem dois), " + vd("redesconto") + " e "
            + vd("operações de mercado aberto") + ".",
            "O open market é o mais usado porque é flexível, diário e reversível: o " + rx("BCB") + " compra ou "
            "vende títulos públicos, sobretudo em " + azb("operações compromissadas") + " (com recompra), para "
            "ajustar as reservas bancárias e levar a Selic efetiva à meta do Copom.",
            "O compulsório, mais “pesado”, mexe no multiplicador e hoje serve muito como instrumento "
            "prudencial; o redesconto atende necessidades de liquidez dos bancos.",
            "Lei 4.595/1964 (art. 10): compete ao BC receber os recolhimentos compulsórios, realizar operações de "
            "redesconto e efetuar operações de compra e venda de títulos públicos federais — os três "
            "instrumentos estão na lei.",
            vm("Regra-âncora: os clássicos são três — compulsório, redesconto e mercado aberto; o último é o "
               "principal."),
        ],
        "dissecando": (cz("[restrição indevida]") + " A primeira frase e a lista estão certas; o erro foi "
                       "plantado no fim, com “excetuando-se”. 🔥 Itens longos de definição escondem o erro na "
                       "última oração: leia até o ponto final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As operações de mercado aberto são o principal instrumento de política monetária do BCB.”</i> → "
            "CERTO",
            "<i>“O encaixe legal e o recolhimento compulsório são instrumentos distintos, com efeitos opostos "
            "sobre o multiplicador.”</i> → ERRADO (troca de conceito: são o mesmo instrumento)",
        ])],
        "reescrita": ("A política monetária influencia a evolução dos meios de pagamento e controla o processo de "
                      "criação da moeda e do crédito. Na função de executor da política monetária, o BCB, para "
                      "regular os meios de pagamentos, pode utilizar instrumentos clássicos, como encaixe legal, "
                      "recolhimentos compulsórios, redesconto, " + hl("além das") + " operações de mercado "
                      "aberto."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["excetuando-se"], "dificuldade": 1,
        "comentario_fonte": "Errado. Vários comentários fundidos (inclui Prof. Marcello Bolzan): o erro está em "
                            "excluir o open market, principal instrumento; encaixe legal = compulsório; "
                            "instrumentos clássicos × não clássicos; compulsório como colchão de liquidez.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [PROV(2018)],
    },
    # ------------------------------------------------------------------ E1-0520
    {
        "id": "ECO-E1-0520-1", "fonte_ref": "E1-0520", "destino": "36", "subtema": H2["bc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": ("Com relação ao conceito de meios de pagamento (M1), que corresponde ao estoque de moeda "
                    "disponível para uso da coletividade, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("As emissões de papel moeda pelo Tesouro Nacional são instrumento de política monetária à "
                      "disposição do Ministério da Fazenda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As emissões de papel moeda pelo ") + vm("Tesouro Nacional") + az(" são instrumento de "
                       "política monetária à disposição ") + vm("do Ministério da Fazenda") + az(".")),
        "poucas": ("A emissão de moeda é competência " + azb("exclusiva do Banco Central") + " (CF, art. 164); "
                   "o Tesouro e o Ministério da Fazenda não emitem papel-moeda."),
        "destrinchando": [
            vd("CF, art. 164, caput") + ": “A competência da União para emitir moeda será exercida exclusivamente "
            "pelo banco central.” O § 1º proíbe o BC de conceder empréstimos ao Tesouro — separação entre "
            "autoridade monetária e fiscal.",
            "O Tesouro Nacional financia o governo emitindo <b>títulos</b> (dívida pública), não moeda. Já o "
            + rx("BCB") + " não pode emitir títulos próprios desde a " + vd("LRF (LC 101/2000, art. 34)")
            + "; para fazer política monetária, usa títulos do Tesouro em sua carteira.",
            "A produção física das cédulas e moedas é da Casa da Moeda, sob encomenda do BCB — produzir não é "
            "emitir: emissão é pôr moeda em circulação como passivo do BC.",
            "Os manuais (" + oc("Vasconcellos") + ") listam as “emissões” entre os instrumentos clássicos de "
            "política monetária, sempre como prerrogativa do banco central; na prática, a emissão de cédulas "
            "acompanha a demanda do público, e o controle da liquidez é feito por mercado aberto, compulsório e "
            "redesconto.",
            "Antes de 1964 (SUMOC e Banco do Brasil) e até 1986 (conta movimento), as funções monetárias e "
            "fiscais se misturavam no Brasil; separá-las foi parte da construção institucional que culminou no "
            "Plano Real.",
        ],
        "dissecando": (cz("[troca de ator]") + " Troca o emissor (BC → Tesouro) e o titular do instrumento "
                       "(autoridade monetária → Ministério da Fazenda). Pista: no Brasil, quem emite moeda é só o "
                       "BC, por mandamento constitucional."),
        "modulos": [("😈 Para dificultar", [
            "<i>“É vedado ao Banco Central conceder, direta ou indiretamente, empréstimos ao Tesouro "
            "Nacional.”</i> → CERTO",
            "<i>“O Banco Central do Brasil financia suas operações de mercado aberto com a emissão de títulos "
            "próprios.”</i> → ERRADO (dado alterado: vedado desde a LRF; usa títulos do Tesouro)",
        ])],
        "reescrita": ("As emissões de papel moeda pelo " + hl("Banco Central do Brasil") + " são instrumento de "
                      "política monetária à disposição " + hl("da autoridade monetária") + "."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADA (letra E de questão de múltipla escolha). A instituição competente para "
                            "emitir papel-moeda é o Bacen (CF, art. 164); um comentário afirma, sem base, que no "
                            "Brasil a emissão não seria instrumento de política monetária.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (172).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; dispositivo constitucional no 📖)"},
                          {"ref": "image (168).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada)"}],
        "alertas": [PROV(2013)],
    },
    # ------------------------------------------------------------------ E1-0524
    {
        "id": "ECO-E1-0524-1", "fonte_ref": "E1-0524", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à política monetária e aos seus efeitos sobre a renda.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia fechada, que esteja operando abaixo do pleno emprego, o formulador de "
                      "política econômica que pretenda expandir o nível de renda deve resgatar títulos da dívida "
                      "pública."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia fechada, que esteja operando <u>abaixo do pleno emprego</u>, o formulador "
                      "de política econômica que pretenda expandir o nível de renda deve <u>resgatar títulos</u> "
                      "da dívida pública."),
        "poucas": ("Resgatar títulos = trocar títulos do público por " + azb("moeda") + ": injeta liquidez, "
                   "derruba os juros e estimula a demanda agregada — política monetária " + azb("expansionista")
                   + "."),
        "destrinchando": [
            "Quando o governo (ou o BC, no mercado aberto) recompra títulos, paga com moeda: a base monetária e os "
            "meios de pagamento sobem; há menos títulos em poder do público, seu preço sobe e os " + vd("juros "
            "caem") + ".",
            "No " + azb("IS-LM") + ": mais moeda desloca a LM para a direita → " + vd("i ↓, Y ↑") + ". Juros "
            "menores estimulam investimento e consumo de bens duráveis.",
            "“Abaixo do pleno emprego” é a condição que faz o estímulo virar <b>renda</b>, e não só preços: "
            "com capacidade ociosa, a oferta agregada responde. No pleno emprego, a expansão monetária tenderia "
            "a gerar inflação.",
            "“Economia fechada” afasta os efeitos do câmbio e dos fluxos de capital (Mundell-Fleming), que "
            "poderiam anular a política monetária em regimes de câmbio fixo.",
            "Exceção a lembrar: na " + azb("armadilha da liquidez") + " (LM horizontal), a política monetária "
            "perde eficácia; o item não traz essa hipótese.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " “Resgatar títulos” é um jeito menos usual de dizer "
                       "“comprar títulos/injetar moeda”; quem associa “dívida pública” a política fiscal se "
                       "confunde. As condições (economia fechada, ociosidade) são as do caso-padrão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…que pretenda expandir o nível de renda deve vender títulos da dívida pública no mercado "
            "aberto.”</i> → ERRADO (inversão: venda enxuga moeda)",
            "<i>“Em uma economia na armadilha da liquidez, o resgate de títulos eleva fortemente a renda.”</i> "
            "→ ERRADO (exceção ignorada: a política monetária é ineficaz)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": "CERTO. Resgatar títulos injeta liquidez: política monetária expansionista, renda e "
                            "emprego sobem.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (98).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; mecanismo IS-LM no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0525
    {
        "id": "ECO-E1-0525-1", "fonte_ref": "E1-0525", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("Um objetivo contracionista, tudo mais constante, pode ser alcançado por meio de uma política "
                      "monetária, que aumente a taxa de redesconto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um objetivo <u>contracionista</u>, tudo mais constante, pode ser alcançado por meio de uma "
                      "política monetária, que <u>aumente</u> a taxa de redesconto."),
        "poucas": ("Redesconto mais caro → bancos tomam menos liquidez do BC e guardam mais reservas → menos "
                   "crédito e menos moeda: medida " + azb("contracionista") + "."),
        "destrinchando": [
            "O " + azb("redesconto") + " é o empréstimo do banco central aos bancos comerciais. A " + azb("taxa "
            "de redesconto") + " é o preço dessa liquidez de última hora.",
            "Taxa ↑: socorrer-se no BC fica caro; os bancos passam a manter mais " + azb("reservas "
            "voluntárias") + " por precaução e emprestam menos. O multiplicador cai, o crédito encolhe → "
            "efeito " + vd("contracionista") + ". Taxa ↓: o contrário (expansionista).",
            "O redesconto também é a ferramenta da função de " + azb("emprestador de última instância") + ": em "
            "crises, o BC amplia prazos, garantias aceitas e volumes.",
            "No " + rx("BCB") + " atual, o redesconto tem papel secundário na política monetária (a Selic é "
            "conduzida por mercado aberto); serve sobretudo à gestão de liquidez das instituições financeiras.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Regra de manual, protegida por “pode” e "
                       "“tudo mais constante”. A vírgula antes de “que” é só ruído de redação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução da taxa de redesconto é medida contracionista.”</i> → ERRADO (inversão: barateia a "
            "liquidez, é expansionista)",
            "<i>“O redesconto é o instrumento por meio do qual o BC atua como emprestador de última "
            "instância.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "tudo mais constante"],
        "dificuldade": 1,
        "comentario_fonte": "CERTO. Redesconto mais caro restringe a oferta monetária: medida contracionista.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0527-1, ECO-E1-0528-1, ECO-E1-0529-1 e ECO-E1-0532-1 (redesconto)"],
    },
    # ------------------------------------------------------------------ E1-0526
    {
        "id": "ECO-E1-0526-1", "fonte_ref": "E1-0526", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": "O aumento do recolhimento compulsório provoca efeito contracionista no crédito.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O <u>aumento</u> do recolhimento compulsório provoca efeito <u>contracionista</u> no "
                      "crédito."),
        "poucas": ("Compulsório maior prende no BC uma fatia maior dos depósitos: sobra " + azb("menos para "
                   "emprestar") + ", e o multiplicador cai."),
        "destrinchando": [
            "O " + azb("recolhimento compulsório") + " é a parcela dos depósitos que os bancos são obrigados a "
            "manter no BC. Ela não pode ser emprestada.",
            "Com alíquota r maior, cada depósito gera menos crédito novo e, portanto, menos depósitos derivados: "
            "o multiplicador " + vd("m = (1 + c) / (c + r)") + " cai. Ex.: com c = 0, r de 20% para 25% leva m "
            "de " + vd("5") + " para " + vd("4") + ".",
            "Efeitos em cadeia: crédito ↓ → meios de pagamento ↓ → demanda agregada ↓ → pressão inflacionária "
            "↓. Também há canal de preço: os bancos repassam aos tomadores o custo do recurso “parado” "
            "(spread ↑).",
            "No Brasil, o compulsório é historicamente alto e também atua como " + azb("instrumento "
            "prudencial") + " — o " + rx("BCB") + " o eleva em tempos normais e o libera em crises (2008, "
            "2020).",
        ],
        "dissecando": (cz("[literalidade]") + " Regra direta, sem modulador. A única armadilha seria confundir o "
                       "sentido — compulsório ↑ é aperto, não estímulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução do recolhimento compulsório provoca efeito contracionista no crédito.”</i> → ERRADO "
            "(inversão: libera recursos, é expansionista)",
            "<i>“O aumento do compulsório eleva o multiplicador bancário.”</i> → ERRADO (inversão: r está no "
            "denominador)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. Compulsório maior reduz a liquidez dos bancos e restringe o crédito.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0531-1 e ECO-E3-L00112-1 (compulsório)"],
    },
    # ------------------------------------------------------------------ E1-0527
    {
        "id": "ECO-E1-0527-1", "fonte_ref": "E1-0527", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("A ampliação das operações de redesconto pelo Banco Central constitui política adequada para "
                      "combater elevados níveis de inflação e excesso de demanda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A ") + vm("ampliação") + az(" das operações de redesconto pelo Banco Central constitui "
                                                     "política adequada para combater elevados níveis de inflação "
                                                     "e excesso de demanda.")),
        "poucas": ("Ampliar o redesconto <b>injeta</b> liquidez nos bancos — é " + azb("expansionista")
                   + ". Inflação e excesso de demanda pedem o contrário: " + azb("restringir") + " o redesconto."),
        "destrinchando": [
            "Ampliar o redesconto (mais volume, prazos maiores, taxa menor, garantias mais flexíveis) facilita o "
            "acesso dos bancos a recursos do BC → mais reservas disponíveis → " + vd("mais crédito") + " e mais "
            "meios de pagamento.",
            "Inflação de demanda exige " + azb("política contracionista") + ": elevar a taxa básica, vender "
            "títulos no mercado aberto, elevar o compulsório, encarecer ou restringir o redesconto.",
            "Tabela de bolso — expansionistas: compra de títulos, compulsório ↓, redesconto ampliado/mais barato. "
            "Contracionistas: venda de títulos, compulsório ↑, redesconto restrito/mais caro.",
            "Em crises financeiras o BC amplia o redesconto mesmo com inflação controlada: o objetivo aí é "
            "estabilidade financeira (emprestador de última instância), não estimular a demanda.",
            vm("Regra-âncora: tudo o que dá liquidez aos bancos é expansionista."),
        ],
        "dissecando": (cz("[inversão]") + " Associa um instrumento expansionista a um objetivo contracionista. "
                       "O item é uma de várias versões do mesmo molde (ampliação do redesconto × objetivo): o "
                       "teste é sempre o sinal do instrumento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A restrição das operações de redesconto constitui política adequada para combater a inflação "
            "de demanda.”</i> → CERTO",
            "<i>“A elevação do compulsório é política adequada para combater o excesso de demanda.”</i> → CERTO",
        ])],
        "reescrita": ("A " + hl("restrição") + " das operações de redesconto pelo Banco Central constitui política "
                      "adequada para combater elevados níveis de inflação e excesso de demanda."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Ampliar o redesconto é expansionista; combate à inflação exige medidas "
                            "contracionistas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0528-1, ECO-E1-0529-1 e ECO-E1-0532-1 (ampliação do redesconto)"],
    },
    # ------------------------------------------------------------------ E1-0528
    {
        "id": "ECO-E1-0528-1", "fonte_ref": "E1-0528", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("A ampliação das operações de redesconto pelo Banco Central objetiva contrair o produto e o "
                      "nível de emprego na economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A ampliação das operações de redesconto pelo Banco Central objetiva ") + vm("contrair")
                    + az(" o produto e o nível de emprego na economia.")),
        "poucas": ("Ampliar o redesconto dá liquidez aos bancos para " + azb("manter ou expandir o crédito")
                   + ": o efeito esperado é sustentar ou elevar produto e emprego, não contraí-los."),
        "destrinchando": [
            "Mecanismo: redesconto ampliado → bancos com mais acesso a reservas → mais disposição para emprestar "
            "→ crédito ↑ → consumo e investimento ↑ → " + vd("produto e emprego ↑") + " (no curto prazo e com "
            "capacidade ociosa).",
            "Mesmo quando o redesconto é usado só para evitar uma crise de liquidez, o objetivo é <b>impedir</b> "
            "a contração do crédito e da atividade — nunca provocá-la.",
            "Para contrair a demanda agregada (combater inflação), o BC faria o inverso: restringir ou "
            "encarecer o redesconto, elevar o compulsório, vender títulos, subir a taxa básica.",
            "Observe que nenhum BC tem por “objetivo” contrair produto e emprego: mesmo a política "
            "contracionista mira a inflação; a queda de atividade é custo, não meta.",
        ],
        "dissecando": (cz("[inversão]") + " Inverte o efeito do instrumento. Pista adicional: “objetiva contrair "
                       "o produto e o emprego” é uma formulação estranha para qualquer política — sinal de item "
                       "fabricado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A ampliação das operações de redesconto pode estimular a expansão do crédito bancário.”</i> → "
            "CERTO",
            "<i>“A restrição do redesconto é medida expansionista.”</i> → ERRADO (inversão: é contracionista)",
        ])],
        "reescrita": ("A ampliação das operações de redesconto pelo Banco Central objetiva " + hl("expandir")
                      + " o produto e o nível de emprego na economia."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. O redesconto oferece liquidez e estimula o crédito, podendo elevar produto e "
                            "emprego.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0527-1, ECO-E1-0529-1 e ECO-E1-0532-1 (ampliação do redesconto)"],
    },
    # ------------------------------------------------------------------ E1-0529
    {
        "id": "ECO-E1-0529-1", "fonte_ref": "E1-0529", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("A ampliação das operações de redesconto pelo Banco Central pode estimular a expansão da "
                      "carteira de crédito dos bancos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A ampliação das operações de redesconto pelo Banco Central <u>pode estimular</u> a "
                      "expansão da carteira de crédito dos bancos."),
        "poucas": ("O redesconto é fonte de " + azb("liquidez") + " para os bancos; ampliá-lo dá segurança e "
                   "recursos para manter ou expandir os empréstimos."),
        "destrinchando": [
            "O banco empresta mais quando sabe que terá acesso a reservas se faltar caixa. O " + azb("redesconto")
            + " ampliado (mais volume, prazos maiores, garantias mais amplas, taxa menor) reduz a necessidade de "
            "reservas voluntárias de precaução → " + vd("crédito ↑") + ".",
            "Modalidades no " + rx("BCB") + ": redesconto intradia (para fechar a liquidação do dia) e redesconto "
            "de prazos curtos, com garantia em títulos; em crises, o BC aceitou garantias mais amplas, como "
            "carteiras de crédito.",
            "O “pode” é importante: o efeito depende da disposição dos bancos e da demanda por crédito. Em "
            "crises profundas, a liquidez extra pode ficar empoçada (canal do crédito fraco).",
            "Classificação: instrumento expansionista quando ampliado/barateado; contracionista quando "
            "restringido/encarecido.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Regra de manual protegida pelo “pode”. Itens "
                       "do mesmo molde trocam o objetivo (combater inflação, contrair produto) para virar "
                       "ERRADO; este mantém o sentido correto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A ampliação das operações de redesconto necessariamente expande a carteira de crédito dos "
            "bancos.”</i> → ERRADO (modulador absoluto: depende da disposição de bancos e tomadores)",
            "<i>“A ampliação do redesconto é adequada para conter a inflação de demanda.”</i> → ERRADO "
            "(inversão: é expansionista)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "CERTO. O redesconto é fonte emergencial de recursos que permite manter ou expandir "
                            "o crédito.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0532-1 (mesma tese: redesconto expandido abre espaço ao crédito)"],
    },
    # ------------------------------------------------------------------ E1-0530
    {
        "id": "ECO-E1-0530-1", "fonte_ref": "E1-0530", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("Se o Banco Central tiver a intenção de reduzir pressões inflacionárias existentes na "
                      "economia, poderá eliminar restrições quantitativas para a compra, pelo próprio Banco "
                      "Central, de operações da carteira de crédito dos bancos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o Banco Central tiver a intenção de ") + vm("reduzir pressões inflacionárias existentes "
                                                                       "na economia")
                    + az(", poderá eliminar restrições quantitativas para a compra, pelo próprio Banco Central, de "
                         "operações da carteira de crédito dos bancos.")),
        "poucas": ("Comprar carteiras de crédito dos bancos é pagar-lhes com " + azb("reservas") + ": injeta "
                   "liquidez, efeito " + azb("expansionista") + ". Não serve para conter inflação."),
        "destrinchando": [
            "Quando o BC compra um ativo — título público, divisa ou carteira de crédito —, paga com moeda que "
            "cria: as reservas bancárias e a base " + vd("sobem") + ". Remover limites a essas compras amplia a "
            "injeção potencial de liquidez.",
            "Com mais liquidez, os bancos podem emprestar mais → crédito ↑ → demanda agregada ↑ → pressão "
            "inflacionária ↑. O instrumento serve a objetivos de " + azb("liquidez e estabilidade financeira")
            + ", não ao combate à inflação.",
            "Para reduzir pressões inflacionárias, o BC enxuga liquidez: eleva juros e compulsório, vende "
            "títulos, restringe o redesconto.",
            "Contexto: em crises, BCs ampliam as compras ou as garantias aceitas para irrigar o sistema "
            "(o " + rx("BCB") + " em 2008 e, com a " + vd("EC 106/2020") + ", na pandemia, quando foi autorizado "
            "a comprar títulos privados e direitos creditórios no mercado secundário).",
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " Instrumento expansionista ligado a objetivo "
                       "contracionista. A linguagem técnica (“restrições quantitativas”, “operações da "
                       "carteira”) esconde a pergunta simples: o BC está dando ou tirando dinheiro dos bancos?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em situação de crise de liquidez, o Banco Central pode ampliar a compra de carteiras de crédito "
            "dos bancos para irrigar o sistema financeiro.”</i> → CERTO",
            "<i>“Para conter a inflação, o BC pode elevar o recolhimento compulsório.”</i> → CERTO",
        ])],
        "reescrita": ("Se o Banco Central tiver a intenção de " + hl("ampliar a liquidez do sistema bancário")
                      + ", poderá eliminar restrições quantitativas para a compra, pelo próprio Banco Central, de "
                      "operações da carteira de crédito dos bancos."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": ["poderá"], "dificuldade": 2,
        "comentario_fonte": "ERRADO. Eliminar restrições à compra de carteiras aumenta a liquidez dos bancos, "
                            "efeito expansionista que pode agravar a inflação.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0531
    {
        "id": "ECO-E1-0531-1", "fonte_ref": "E1-0531", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("Se o Banco Central tiver a intenção de reduzir pressões inflacionárias existentes na "
                      "economia, poderá elevar o percentual do recolhimento compulsório."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o Banco Central tiver a intenção de <u>reduzir pressões inflacionárias</u> existentes "
                      "na economia, poderá <u>elevar</u> o percentual do recolhimento compulsório."),
        "poucas": ("Elevar o compulsório retira liquidez dos bancos, reduz o " + azb("multiplicador") + " e o "
                   "crédito, freia a demanda e ajuda a conter a " + azb("inflação de demanda") + "."),
        "destrinchando": [
            "Cadeia: compulsório ↑ → reservas presas no BC ↑ → recursos emprestáveis ↓ → " + vd("crédito ↓")
            + " → consumo e investimento ↓ → demanda agregada ↓ → " + vd("inflação ↓") + ".",
            "Os três instrumentos clássicos no modo contracionista: vender títulos (mercado aberto), elevar o "
            "compulsório, restringir/encarecer o redesconto. Hoje, o principal é a alta da taxa básica (Selic), "
            "operada via mercado aberto.",
            "Ressalva: o compulsório é instrumento “pesado” (mexe no balanço de todos os bancos de uma vez) e "
            "eleva o spread; por isso o " + rx("BCB") + " o usa mais como medida macroprudencial — mas, como "
            "instrumento monetário, seu sentido é o do item.",
            "Funciona melhor contra " + azb("inflação de demanda") + "; diante de choque de oferta (alta de "
            "commodities, quebra de safra), a restrição de crédito derruba a atividade sem atacar a causa.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Regra direta, com o “poderá” a protegê-la. "
                       "É o espelho CERTO do molde em que se associa um instrumento expansionista (comprar "
                       "carteiras, ampliar redesconto) ao combate à inflação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…poderá reduzir o percentual do recolhimento compulsório.”</i> → ERRADO (inversão: reduzir é "
            "expansionista)",
            "<i>“Diante de inflação causada por choque de oferta, a elevação do compulsório elimina a causa da "
            "alta de preços.”</i> → ERRADO (nexo indevido: atua sobre a demanda, não sobre a oferta)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["poderá"], "dificuldade": 1,
        "comentario_fonte": "CERTO. Compulsório maior retira liquidez, reduz o crédito e ajuda a conter a "
                            "inflação.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0526-1 e ECO-E3-L00112-1 (compulsório)"],
    },
    # ------------------------------------------------------------------ E1-0532
    {
        "id": "ECO-E1-0532-1", "fonte_ref": "E1-0532", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("O redesconto é um instrumento clássico de política monetária que, se expandido, pode abrir "
                      "espaço para os bancos realizarem novas operações de crédito."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O redesconto é um <u>instrumento clássico</u> de política monetária que, se expandido, "
                      "<u>pode abrir espaço</u> para os bancos realizarem novas operações de crédito."),
        "poucas": ("O " + azb("redesconto") + " é empréstimo do BC aos bancos — um dos três instrumentos "
                   "clássicos. Expandido, fornece liquidez e libera espaço no balanço para novos empréstimos."),
        "destrinchando": [
            "Os três instrumentos clássicos: " + vd("mercado aberto") + ", " + vd("recolhimento compulsório")
            + " e " + vd("redesconto") + ". Este último é o mais antigo: nasce com os bancos centrais "
            "descontando títulos comerciais dos bancos.",
            "Expandir o redesconto (mais volume, prazo maior, taxa menor, garantias mais amplas) dá aos bancos "
            "acesso a reservas; com o risco de iliquidez coberto, eles podem manter menos reservas voluntárias e "
            "emprestar mais.",
            "Dupla função: instrumento de política monetária (expansionista se ampliado) e ferramenta do "
            + azb("emprestador de última instância") + " — no " + rx("BCB") + ", hoje, sobretudo a segunda.",
            "O “pode” preserva o item: a liquidez só vira crédito se houver bancos dispostos a emprestar e "
            "tomadores dispostos a se endividar.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Duas afirmações verdadeiras de manual "
                       "(“instrumento clássico” e “pode abrir espaço”). O “pode” afasta a objeção de que a "
                       "liquidez extra nem sempre vira crédito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O redesconto não é instrumento clássico de política monetária, mas mero mecanismo de "
            "socorro.”</i> → ERRADO (restrição indevida: é um dos três clássicos)",
            "<i>“A contração do redesconto pode abrir espaço para novas operações de crédito.”</i> → ERRADO "
            "(inversão: restringe a liquidez)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "CERTO. O redesconto é empréstimo do BC aos bancos; expandi-lo aumenta os recursos "
                            "disponíveis e pode estimular o crédito.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0529-1 (mesma tese: redesconto ampliado estimula o crédito)"],
    },
]
