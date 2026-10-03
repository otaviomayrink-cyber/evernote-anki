"""Cards do lote de redação 20 — ECO, passada 02 (notas 40, 41, 42 e 47: políticas não convencionais,
regulação e Basileia, bancos digitais e pagamentos, princípios da tributação)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "qe": "🖨️ QE, tapering e QT",
    "bas": "🏛️ Regulação e Basileia",
    "dig": "💳 Pagamentos e economia digital",
    "trib": "💸 Tributação: princípios e incidência",
}

CMD_ARM_QE = "Julgue o item a seguir, relativo às políticas monetárias não convencionais adotadas após a crise de 2008."

CMD_NAB_23 = "Em relação ao sistema monetário e à política monetária, julgue (C ou E) o item seguinte."

CMD_RT = "A respeito do processo de oferta de moeda, julgue o item a seguir."

CMD_CACD24 = ("Frente à crise internacional nos anos de 2007 e 2008, o Comitê da Basileia (Basileia III), do qual o "
              "Brasil faz parte, buscou fomentar boas práticas nas instituições financeiras. Considerando o objetivo "
              "do Brasil de garantir a eficiência da intermediação de recursos e a promoção da estabilidade do "
              "Sistema Financeiro Nacional, julgue (C ou E) o item subsequente.")

CMD_BDIG = "Acerca dos bancos digitais no Sistema Financeiro Nacional, julgue o item a seguir."

CMD_CACD26 = ("Considere o texto a seguir. A respeito desse assunto e dos múltiplos aspectos a ele relacionados, "
              "julgue o item.")

EXC_CACD26 = ("<p><i>A digitalização dos serviços financeiros transformou, nas últimas décadas, a forma de provisão "
              "de serviços bancários e a arquitetura dos sistemas de pagamento. A expansão de instituições "
              "financeiras digitais e de plataformas de pagamento elevou a eficiência, ao reduzir custos de "
              "transação e ampliar o acesso a instrumentos eletrônicos de transferência de recursos. Ao mesmo "
              "tempo, essas inovações intensificaram desafios relacionados à supervisão prudencial, à segurança "
              "operacional, à concorrência e à estabilidade financeira, além de reacenderem o debate sobre o "
              "potencial papel de moedas digitais emitidas por bancos centrais e seus possíveis efeitos sobre a "
              "intermediação financeira e a transmissão da política monetária.</i></p>")

CMD_TRIB = "Julgue o item a seguir, relativo aos princípios da tributação."

SO_GAB = "Só o gabarito, sem comentário."

CARDS = [
    # ------------------------------------------------------------------ E2-L00316
    {
        "id": "ECO-E2-L00316-1", "fonte_ref": "E2-L00316", "destino": "40", "subtema": H2["qe"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": CMD_ARM_QE,
        "rotulo_item": "Item",
        "assertiva": ("Uma implicação empírica documentada em estudos do Federal Reserve é que programas de QE "
                      "tendem a reduzir spreads bancários, uma vez que ampliam a liquidez no sistema, diminuindo "
                      "aversão ao risco e incentivando o repasse imediato para crédito."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma implicação empírica documentada em estudos do Federal Reserve é que programas de QE "
                       "tendem a ") + vm("reduzir spreads bancários") + az(", uma vez que ampliam a liquidez no "
                       "sistema, diminuindo aversão ao risco") + vm(" e incentivando o repasse imediato para "
                                                                     "crédito") + az(".")),
        "poucas": ("O QE comprime " + azb("prêmios de risco e juros longos de mercado") + ", mas a evidência do "
                   "pós-2008 mostra repasse " + vm("lento e incompleto") + " ao crédito bancário: os bancos "
                   "empoçaram reservas e os " + azb("spreads bancários") + " pouco caíram."),
        "destrinchando": [
            azb("Spread bancário") + " = taxa cobrada no empréstimo − custo de captação do banco. Remunera "
            "inadimplência esperada, custos administrativos, tributos, compulsório e margem (poder de mercado). "
            "Não confundir com " + azb("credit spread de mercado") + " (rendimento de um título corporativo − "
            "rendimento do título público de mesmo prazo).",
            "O que o QE fez, segundo os estudos do Fed: comprou Treasuries e MBS em larga escala e reduziu os "
            "rendimentos longos e os prêmios de risco de mercado — o trabalho clássico do Fed de Nova York é "
            + oc("Gagnon, Raskin, Remache e Sack (2011)") + ". Os canais: rebalanceamento de portfólio, "
            "sinalização e liquidez de mercado.",
            "O que o QE <b>não</b> fez: transformar reservas em crédito de forma automática. Com a economia em "
            "recessão e o risco de calote alto, os bancos acumularam " + vd("reservas excedentes") + " no próprio "
            "Fed, que passou a remunerá-las a partir de " + vd("2008") + ". O multiplicador monetário despencou.",
            "Há ainda um efeito na direção oposta: ao " + azb("achatar a curva de juros") + ", o QE comprime a "
            "margem líquida de juros dos bancos (que captam curto e emprestam longo). Para preservar a "
            "rentabilidade, o banco tende a segurar o spread cobrado do tomador final.",
            vm("Regra-âncora: QE baixa juros de mercado; não garante crédito bancário mais barato nem imediato."),
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A cadeia “mais liquidez → menos aversão ao risco” é "
                       "defensável; o erro foi enxertado nas pontas: a conclusão (spread bancário cai) e o "
                       "advérbio “imediato”. 🔥 Itens sobre QE costumam confundir spread de mercado com spread "
                       "bancário e prometer efeitos automáticos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Programas de QE tendem a reduzir rendimentos de títulos de longo prazo, por meio do canal de "
            "rebalanceamento de portfólio.”</i> → CERTO",
            "<i>“Após o QE1, a liquidez injetada converteu-se integralmente em novos empréstimos bancários.”</i> → "
            "ERRADO (os bancos acumularam reservas excedentes)",
        ])],
        "reescrita": ("Uma implicação empírica documentada em estudos do Federal Reserve é que programas de QE "
                      "tendem a " + hl("comprimir prêmios de risco e juros longos, com efeito limitado sobre os "
                                       "spreads bancários") + ", uma vez que ampliam a liquidez no sistema, "
                      "diminuindo aversão ao risco" + hl(", sem garantir o repasse imediato para crédito") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": ["tendem a", "imediato"], "dificuldade": 3,
        "comentario_fonte": ("Gabarito ERRADO; três respostas de IA (Claude, Gemini, GPT) fundidas: QE reduz "
                             "prêmios de risco e yields longos, mas o repasse ao crédito bancário é lento e "
                             "incompleto; bancos acumularam reservas excedentes; achatamento da curva comprime a "
                             "margem dos bancos; spread de mercado ≠ spread bancário. Uma das respostas atribui "
                             "ao Fed estudo do BIS (Borio, Gambacorta e Hofmann)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 040", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (resumo dos erros incorporado ao 📖)"},
                          {"ref": "IMAGEM 041", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (tabela sobre spread como indicador; fora do ponto do item)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00318
    {
        "id": "ECO-E2-L00318-1", "fonte_ref": "E2-L00318", "destino": "40", "subtema": H2["qe"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARM_QE,
        "rotulo_item": "Item",
        "assertiva": ("A literatura pós-crise identifica que políticas não convencionais operam principalmente "
                      "pelos mesmos canais de transmissão da política monetária tradicional, não havendo efeitos "
                      "específicos via composição de portfólio ou via sinalização."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A literatura pós-crise identifica que políticas não convencionais operam ")
                    + vm("principalmente pelos mesmos canais de transmissão da política monetária tradicional, "
                         "não havendo") + az(" efeitos específicos via composição de portfólio ou via "
                                             "sinalização.")),
        "poucas": ("É o contrário: as políticas não convencionais foram justificadas justamente por canais "
                   "próprios — " + azb("rebalanceamento de portfólio") + " e " + azb("sinalização") + " —, "
                   "que funcionam mesmo com a taxa básica travada perto de zero."),
        "destrinchando": [
            "Na política <b>convencional</b>, o banco central fixa a taxa de curtíssimo prazo (Fed funds, Selic) "
            "e o efeito se propaga pelas taxas de mercado, câmbio, preço de ativos e crédito. No " + azb("limite "
            "inferior zero") + ", esse instrumento se esgota: é aí que entram as medidas não convencionais.",
            azb("Canal de rebalanceamento de portfólio") + ": como títulos de prazos e riscos diferentes não são "
            "substitutos perfeitos (ideia que remonta a " + oc("James Tobin") + "), o BC, ao retirar do mercado "
            "títulos longos e MBS, eleva seus preços, reduz seus rendimentos e empurra os investidores para "
            "ativos mais arriscados (ações, crédito corporativo).",
            azb("Canal de sinalização") + ": comprar ativos em massa (e anunciar orientação futura, o "
            "<i>forward guidance</i>) compromete o BC com juros baixos por longo tempo, derrubando a parte longa "
            "da curva via expectativas.",
            azb("Canal de liquidez / funcionamento de mercado") + ": o BC compra onde o mercado travou e "
            "restabelece a negociação, reduzindo prêmios de liquidez.",
            vm("Regra-âncora: QE age sobre preços e composição de carteiras, não sobre a taxa básica."),
        ],
        "dissecando": (cz("[contradição · troca de conceito]") + " O item nega exatamente o que a literatura "
                       "afirma, com o reforço “não havendo efeitos específicos”. Pista: se as medidas operassem "
                       "pelos mesmos canais da taxa básica, seriam inúteis no juro zero — e não haveria razão "
                       "para adotá-las."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O anúncio de compras de ativos pode reduzir juros longos ao sinalizar a manutenção de juros "
            "básicos baixos por período prolongado.”</i> → CERTO",
            "<i>“O canal de rebalanceamento de portfólio pressupõe que títulos de diferentes prazos sejam "
            "substitutos perfeitos.”</i> → ERRADO (pressupõe substituição imperfeita)",
        ])],
        "reescrita": ("A literatura pós-crise identifica que políticas não convencionais operam "
                      + hl("também por canais próprios, distintos dos da política monetária tradicional, havendo")
                      + " efeitos específicos via composição de portfólio ou via sinalização."),
        "tipo_erro": ["CONTRADICAO", "TROCA_CONCEITO"], "moduladores": ["principalmente", "não havendo"],
        "dificuldade": 2,
        "comentario_fonte": ("ERRADO. Há consenso de que as PMNC têm canais adicionais: composição de portfólio, "
                             "sinalização e liquidez."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00319
    {
        "id": "ECO-E2-L00319-1", "fonte_ref": "E2-L00319", "destino": "40", "subtema": H2["qe"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARM_QE,
        "rotulo_item": "Item",
        "assertiva": ("A expansão do balanço dos bancos centrais decorrente do QE é, por si só, inflacionária no "
                      "curto prazo, uma vez que aumenta automaticamente a demanda agregada e pressiona preços, "
                      "conforme previsões do modelo monetarista tradicional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A expansão do balanço dos bancos centrais decorrente do QE ")
                    + vm("é, por si só, inflacionária no curto prazo, uma vez que aumenta automaticamente")
                    + az(" a demanda agregada ") + vm("e pressiona") + az(" preços, ") + vm("conforme")
                    + az(" previsões do modelo monetarista tradicional.")),
        "poucas": ("A base monetária explodiu depois de 2008, mas a " + azb("inflação ficou baixa") + " por anos: "
                   "a moeda nova virou " + azb("reserva excedente") + " parada nos bancos, a velocidade caiu e a "
                   "demanda agregada não respondeu como previa o monetarismo."),
        "destrinchando": [
            "Na " + azb("teoria quantitativa") + " (MV = PY), com V estável e Y no potencial, mais moeda vira "
            "mais preço — é a previsão monetarista tradicional (" + oc("Milton Friedman") + "). O item descreve "
            "bem o modelo; erra ao dizer que o QE confirmou essa previsão.",
            "O que houve nos EUA, no Reino Unido, no Japão e na zona do euro: base monetária multiplicada várias "
            "vezes, inflação " + vd("abaixo da meta de 2%") + " durante a maior parte da década de 2010.",
            "Por quê: (1) o QE troca um ativo (título) por outro (reserva) no balanço dos bancos — não põe renda "
            "na mão das famílias; (2) com hiato do produto amplo e incerteza alta, os bancos não emprestaram e o "
            + azb("multiplicador monetário") + " desabou; (3) a " + azb("velocidade da moeda") + " caiu; (4) no "
            "juro zero, moeda e título viram quase substitutos perfeitos — o cenário de " + azb("armadilha de "
            "liquidez") + " de " + oc("Keynes") + ", retomado por " + oc("Paul Krugman") + " para o Japão.",
            "Ressalva útil: a inflação de 2021–2022 reacendeu o debate, mas ali o QE veio junto de forte "
            "expansão fiscal, choques de oferta e economia perto do pleno emprego — não “por si só”.",
            vm("Regra-âncora: base monetária maior não é inflação automática; depende de crédito, velocidade e "
               "hiato."),
        ],
        "dissecando": (cz("[nexo indevido · modulador absoluto]") + " “Por si só” e “automaticamente” "
                       "eliminam as condições de que a inflação depende. A citação do monetarismo é verdadeira "
                       "como descrição do modelo, e é ela que dá credibilidade ao item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Apesar da forte expansão da base monetária, o QE pós-2008 não gerou inflação relevante no curto "
            "prazo, em parte pela queda do multiplicador monetário.”</i> → CERTO",
            "<i>“O QE não gerou inflação porque não aumentou a base monetária.”</i> → ERRADO (a base aumentou; "
            "o que caiu foi o multiplicador)",
        ])],
        "reescrita": ("A expansão do balanço dos bancos centrais decorrente do QE "
                      + hl("não foi, por si só, inflacionária no curto prazo, pois não aumentou automaticamente")
                      + " a demanda agregada " + hl("nem pressionou") + " preços, " + hl("ao contrário das")
                      + " previsões do modelo monetarista tradicional."),
        "tipo_erro": ["NEXO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["por si só", "automaticamente"],
        "dificuldade": 2,
        "comentario_fonte": ("ERRADO. A experiência pós-2008 mostra que o QE não gerou inflação relevante no "
                             "curto prazo: incerteza, hiato amplo, baixa velocidade da moeda e entesouramento "
                             "bancário."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00320
    {
        "id": "ECO-E2-L00320-1", "fonte_ref": "E2-L00320", "destino": "40", "subtema": H2["qe"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARM_QE,
        "rotulo_item": "Item",
        "assertiva": ("O aumento da liquidez como política não convencional implica que bancos centrais atuem como "
                      "emprestadores de última instância de forma ampliada, muitas vezes oferecendo garantias e "
                      "linhas especiais mesmo para instituições não bancárias, como fundos de investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento da liquidez como política não convencional implica que bancos centrais atuem como "
                      "emprestadores de última instância de forma <u>ampliada</u>, muitas vezes oferecendo "
                      "garantias e linhas especiais <u>mesmo para instituições não bancárias</u>, como fundos de "
                      "investimento."),
        "poucas": ("Nas crises de 2008 e de 2020, o " + azb("emprestador de última instância") + " saiu do "
                   "perímetro bancário: Fed e BCE abriram linhas para dealers, fundos de money market e mercados "
                   "de papéis comerciais."),
        "destrinchando": [
            "A doutrina clássica é de " + oc("Walter Bagehot") + " (<i>Lombard Street</i>, 1873): em pânico, o "
            "BC deve emprestar livremente, a instituições solventes, contra boas garantias e a juros punitivos. "
            "O cliente tradicional era o <b>banco</b>, via redesconto.",
            "Em 2008, o sistema que travou foi o " + azb("bancário-sombra") + " (dealers, fundos de money market, "
            "veículos de securitização). O Fed criou, entre outras, a " + vd("Primary Dealer Credit Facility")
            + " e linhas para o mercado de commercial paper; em " + vd("2020") + ", a " + vd("Money Market "
            "Mutual Fund Liquidity Facility") + ". O BCE ampliou prazos e garantias aceitas.",
            "Essa ampliação levou à ideia de “" + azb("dealer de última instância") + "” (" + oc("Perry Mehrling")
            + "): o BC passa a sustentar o preço de ativos, não só a liquidez de bancos.",
            "Custo conhecido: " + azb("risco moral") + " — instituições que não pagam pelo seguro (não recolhem "
            "compulsório nem se submetem à mesma regulação) passam a contar com o socorro.",
            rx("No Brasil") + ", a EC 106/2020 autorizou temporariamente o BCB a comprar títulos privados no "
            "mercado secundário, na mesma lógica de ampliação do perímetro.",
        ],
        "dissecando": (cz("[detalhe · modulador relativo]") + " O item é verdadeiro por um pormenor histórico: "
                       "socorro a não bancos. O “muitas vezes” protege-o da generalização. A tentação de marcar "
                       "ERRADO vem da definição de livro-texto, que fala só em bancos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela doutrina de Bagehot, o emprestador de última instância deve socorrer instituições "
            "insolventes, a juros subsidiados.”</i> → ERRADO (solventes, a juros punitivos)",
            "<i>“Na crise de 2008, o Fed limitou-se ao redesconto a bancos comerciais.”</i> → ERRADO (criou linhas "
            "para dealers e mercados de papéis)",
        ])],
        "tipo_erro": ["DETALHE", "MODULADOR_RELATIVO"], "moduladores": ["muitas vezes", "mesmo para"],
        "dificuldade": 2,
        "comentario_fonte": ("CERTO. Foi o caso do Fed (Primary Dealer Credit Facility, Money Market Mutual Fund "
                             "Liquidity Facility) e do BCE, ampliando o escopo do LOLR tradicional."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01229
    {
        "id": "ECO-E2-L01229-1", "fonte_ref": "E2-L01229", "destino": "40", "subtema": H2["qe"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23,
        "rotulo_item": "Item",
        "assertiva": ("O afrouxamento monetário, também conhecido como quantitative easing, é um instrumento de "
                      "política monetária não convencional que costuma ser utilizado quando o Banco Central não "
                      "consegue estimular a economia por meio de quedas adicionais da taxa de juros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O afrouxamento monetário, também conhecido como quantitative easing, é um instrumento de "
                      "política monetária <u>não convencional</u> que <u>costuma</u> ser utilizado quando o Banco "
                      "Central <u>não consegue estimular a economia por meio de quedas adicionais da taxa de "
                      "juros</u>."),
        "poucas": ("O " + azb("QE") + " é a resposta típica ao " + azb("limite inferior zero") + ": esgotado o "
                   "corte da taxa básica, o BC compra ativos em larga escala para baixar os juros longos e "
                   "irrigar o sistema."),
        "destrinchando": [
            "Política " + azb("convencional") + ": o BC fixa a taxa de curtíssimo prazo (Selic, Fed funds) e "
            "deixa o mercado propagar. Quando essa taxa chega perto de " + vd("zero") + " (EUA e Reino Unido "
            "após 2008; Japão desde o fim dos anos 1990), cortar mais é inviável ou ineficaz — o público "
            "prefere guardar papel-moeda a aceitar juros muito negativos.",
            azb("Quantitative easing") + ": compras em massa de títulos públicos e, muitas vezes, privados "
            "(MBS, debêntures, ações no caso do Japão), pagas com reservas criadas pelo BC. O balanço do BC "
            "cresce — por isso também se fala em “política de balanço”.",
            "Objetivos: derrubar os rendimentos longos (que balizam hipotecas e investimento), reduzir prêmios "
            "de risco, sinalizar juros baixos por muito tempo e evitar deflação.",
            "Ciclo completo: " + azb("QE") + " (compra) → " + azb("tapering") + " (redução do ritmo de compras, "
            "como o anúncio do Fed em " + vd("2013") + ") → " + azb("QT") + " (encolhimento do balanço, deixando "
            "títulos vencerem sem reinvestir).",
            vm("Regra-âncora: QE entra quando a taxa básica já não tem para onde cair."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de manual. O “costuma” protege o "
                       "item: houve QE com juros positivos (o próprio BCE iniciou o seu com taxa baixa, mas não "
                       "nula), e ninguém afirma que seja o único cenário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O quantitative easing consiste na elevação dos depósitos compulsórios para conter a inflação.”"
            "</i> → ERRADO (troca de instrumento e de sentido)",
            "<i>“O tapering corresponde à venda imediata de todos os títulos adquiridos no QE.”</i> → ERRADO "
            "(é só a redução do ritmo de compras)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["costuma"], "dificuldade": 1,
        "comentario_fonte": ("CERTO. O QE é usado quando a taxa de juros já é muito baixa e o BC eleva a liquidez "
                             "com compra massiva de títulos públicos e privados, para baixar as taxas do crédito "
                             "e reaquecer a economia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01748
    {
        "id": "ECO-E2-L01748-1", "fonte_ref": "E2-L01748", "destino": "40", "subtema": H2["qe"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("As trocas de títulos de curto prazo por títulos de longo prazo pelo Federal Reserve, como "
                      "uma das reações à crise que se iniciou em 2007/2008, visando reduzir as taxas de juros de "
                      "longo prazo, constituem-se em exemplo das chamadas políticas monetárias "
                      "não-convencionais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As <u>trocas de títulos de curto prazo por títulos de longo prazo</u> pelo Federal "
                      "Reserve, como uma das reações à crise que se iniciou em 2007/2008, visando reduzir as "
                      "taxas de juros de <u>longo prazo</u>, constituem-se em exemplo das chamadas políticas "
                      "monetárias não-convencionais."),
        "poucas": ("É a " + azb("Operation Twist") + " (Maturity Extension Program, " + vd("2011–2012") + "): o "
                   "Fed vendeu títulos curtos e comprou longos, mudando a <b>composição</b> do balanço, não o "
                   "tamanho, para achatar a curva de juros."),
        "destrinchando": [
            "Em " + vd("setembro de 2011") + ", com a taxa básica já perto de zero, o Fed anunciou a compra de "
            + vd("US$ 400 bilhões") + " em Treasuries longos, financiada pela venda de títulos curtos; o "
            "programa foi estendido em 2012. O nome “twist” (torção) vem do efeito desejado sobre a curva: "
            "segurar a ponta curta e derrubar a longa.",
            "Diferença para o " + azb("QE") + ": no QE o BC cria reservas e o balanço cresce; na Twist o balanço "
            "fica do mesmo tamanho — muda só o prazo médio da carteira. Os dois atuam pelo mesmo "
            + azb("canal de rebalanceamento de portfólio") + ": tirar duration do mercado reduz o prêmio de "
            "prazo dos títulos longos.",
            "Por que é “não convencional”: a política convencional mira a taxa de curtíssimo prazo; aqui o alvo "
            "é a taxa longa, que baliza hipotecas e investimento.",
            "O nome não é novo: houve uma Operation Twist em " + vd("1961") + ", no governo Kennedy, com a mesma "
            "lógica.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Descreve corretamente o mecanismo sem dizer o nome. "
                       "A dúvida que a banca tenta plantar: “se o balanço não cresceu, é mesmo não convencional?”. "
                       "É — o critério é o alvo (juro longo), não o tamanho do balanço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na Operation Twist, o Fed ampliou seu balanço ao comprar títulos longos com reservas recém-"
            "criadas.”</i> → ERRADO (troca de conceito: isso é QE; a Twist manteve o tamanho)",
            "<i>“A Operation Twist buscou elevar os juros de longo prazo para conter a inflação.”</i> → ERRADO "
            "(sentido invertido: buscou reduzi-los)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["visando"], "dificuldade": 2,
        "comentario_fonte": ("Certo. Operation Twist / Maturity Extension Program: venda de Treasuries curtos e "
                             "compra de longos, sem alterar o tamanho do balanço, para reduzir os juros longos "
                             "com a taxa curta no limite zero."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01749
    {
        "id": "ECO-E2-L01749-1", "fonte_ref": "E2-L01749", "destino": "40", "subtema": H2["qe"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("A recente autorização recebida pelo Banco Central do Brasil para comprar títulos privados no "
                      "mercado financeiro nacional (Emenda Constitucional 106) vai ao encontro das políticas "
                      "monetárias não-convencionais, adotadas por diversos países especialmente após a crise de "
                      "2007/2008."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A recente autorização recebida pelo Banco Central do Brasil para comprar <u>títulos "
                      "privados</u> no mercado financeiro nacional (Emenda Constitucional 106) <u>vai ao "
                      "encontro</u> das políticas monetárias não-convencionais, adotadas por diversos países "
                      "especialmente após a crise de 2007/2008."),
        "poucas": ("A " + rx("EC 106/2020") + " (“Orçamento de Guerra”) autorizou o BCB a comprar títulos "
                   "privados no mercado secundário durante a pandemia — o mesmo tipo de " + azb("credit easing")
                   + " que Fed, BCE e BoE adotaram."),
        "condicionais": [("⏳ Desatualizado (out/2026)",
                          "a autorização era " + vm("temporária") + ": a EC 106 previa sua revogação automática "
                          "com o fim do estado de calamidade da Covid-19 (" + vd("31/12/2020") + "). O item "
                          "continua CERTO quanto à natureza da medida.")],
        "destrinchando": [
            rx("EC 106, de maio de 2020") + ": criou um regime fiscal extraordinário para a calamidade e permitiu "
            "ao BCB comprar e vender títulos do Tesouro nos mercados secundários e, no mercado secundário "
            "doméstico, " + azb("títulos privados de crédito") + " com boa classificação de risco.",
            "Por que é não convencional: o BC não age pela taxa Selic, e sim pelo seu " + azb("balanço") + ", "
            "comprando ativos de risco para destravar mercados e reduzir " + azb("spreads de crédito") + ". É a "
            "variante chamada " + azb("credit easing") + " (compra de ativos privados), vizinha do QE (compra de "
            "títulos públicos).",
            "Paralelos externos: o Fed comprou MBS desde 2008 e, em 2020, títulos corporativos; o BCE tem "
            "programas de compra de títulos corporativos; o Banco do Japão chegou a comprar fundos de ações.",
            "Diferença de contexto: em 2020 a Selic ainda tinha espaço de corte (chegou a " + vd("2%") + "); a "
            "medida brasileira foi pensada sobretudo como ferramenta de " + azb("estabilidade financeira") + ", "
            "não por esgotamento do juro.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Exige saber o conteúdo da EC 106 e classificá-lo. "
                       "“Vai ao encontro” = está de acordo (não confundir com “de encontro a”, que significa "
                       "contrariar)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A EC 106/2020 autorizou o BCB a financiar diretamente o Tesouro Nacional, comprando títulos no "
            "mercado primário.”</i> → ERRADO (só mercado secundário; o financiamento direto segue vedado pela CF, "
            "art. 164)",
            "<i>“A compra de títulos privados pelo BCB, prevista na EC 106, vai de encontro às políticas não "
            "convencionais adotadas após 2008.”</i> → ERRADO (troca de expressão: “de encontro a” = contra)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Certo. A EC 106/2020 permitiu ao BCB, durante a calamidade, comprar títulos privados "
                             "de crédito no mercado secundário doméstico, alinhando-se ao credit easing / QE de "
                             "Fed, BCE, BoE e BoJ."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0513
    {
        "id": "ECO-E1-0513-1", "fonte_ref": "E1-0513", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à supervisão do sistema financeiro.",
        "rotulo_item": "Item",
        "assertiva": ("A estabilidade, a eficiência e o desenvolvimento do sistema financeiro requerem esquemas de "
                      "normas e procedimentos apropriados e a sua observância. Nesse caso, a supervisão das "
                      "instituições financeiras cabe tanto ao BCB quanto a organismos independentes, podendo estes "
                      "últimos exercer a fiscalização de forma exógena ao BCB, pautados em normas próprias de suas "
                      "áreas de competência."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A estabilidade, a eficiência e o desenvolvimento do sistema financeiro requerem esquemas de "
                       "normas e procedimentos apropriados e a sua observância. Nesse caso, a supervisão das "
                       "instituições financeiras cabe tanto ao BCB quanto a organismos independentes, ")
                    + vm("podendo estes últimos exercer a fiscalização de forma exógena ao BCB, pautados em normas "
                         "próprias de suas áreas de competência") + az(".")),
        "poucas": ("A fiscalização das instituições financeiras " + vm("compete privativamente ao BCB") + " (Lei "
                   "4.595/1964, art. 10, IX). Mesmo onde outros órgãos supervisionam segmentos, a atuação nunca "
                   "é <b>exógena</b> ao banco central, a quem cabe normatizar e ser o prestamista de última "
                   "instância."),
        "destrinchando": [
            "Na lição clássica de manual: em muitos países a supervisão é responsabilidade direta e exclusiva do "
            "banco central; em outros, cabe também a organismos especializados. " + azb("Em nenhum caso, porém, "
            "a fiscalização é totalmente exógena ao banco central") + ", que edita normas e é o emprestador de "
            "última instância — quem socorre precisa enxergar o socorrido.",
            rx("No Brasil") + ", a " + vd("Lei 4.595/1964, art. 10, IX") + " dá ao BCB, " + vd("privativamente")
            + ", a fiscalização das instituições financeiras e a aplicação de penalidades; o inciso X reserva-lhe "
            "a autorização para funcionar, fundir-se, transferir controle etc.",
            "Os outros supervisores do SFN — " + azb("CVM") + " (valores mobiliários), " + azb("Susep") + " "
            "(seguros, capitalização, previdência aberta) e " + azb("Previc") + " (fundos de pensão) — cuidam de "
            "segmentos próprios e seguem normas do CMN, do CNSP e do CNPC, todos dentro do mesmo arcabouço. "
            "Entidades privadas (Anbima, B3) fazem autorregulação, que não substitui a supervisão pública.",
            "O modelo de supervisão do BCB é " + azb("baseado em risco") + ", com duas vertentes: "
            + azb("prudencial") + " (solvência e liquidez de cada instituição) e " + azb("de conduta") + " "
            "(relação com clientes, prevenção à lavagem de dinheiro).",
        ],
        "dissecando": (cz("[meia-verdade · extrapolação]") + " A primeira frase é verdadeira e de tom genérico; "
                       "a segunda começa defensável (outros órgãos também supervisionam) e extrapola ao admitir "
                       "fiscalização “exógena ao BCB” com “normas próprias”. O ponto decisivo é a palavra "
                       "“exógena”."),
        "modulos": [("⚖️ Base normativa", [
            vd("Lei 4.595/1964, art. 10") + ": “Compete privativamente ao Banco Central [...] IX – exercer a "
            "fiscalização das instituições financeiras e aplicar as penalidades previstas.”",
            vd("Lei 6.385/1976, art. 8º, III") + ": compete à CVM fiscalizar permanentemente o mercado de valores "
            "mobiliários.",
        ]), ("😈 Para dificultar", [
            "<i>“A fiscalização das instituições financeiras compete privativamente ao Banco Central do "
            "Brasil.”</i> → CERTO",
            "<i>“Entidades de autorregulação, como a Anbima, substituem a supervisão do BCB sobre os bancos que "
            "a elas aderem.”</i> → ERRADO (autorregulação complementa, não substitui)",
        ])],
        "reescrita": ("A estabilidade, a eficiência e o desenvolvimento do sistema financeiro requerem esquemas de "
                      "normas e procedimentos apropriados e a sua observância. Nesse caso, a supervisão das "
                      "instituições financeiras cabe tanto ao BCB quanto a organismos independentes, "
                      + hl("mas em nenhum caso estes últimos exercem a fiscalização de forma exógena ao BCB, a "
                           "quem cabe editar as normas do sistema") + "."),
        "tipo_erro": ["MEIA_VERDADE", "EXTRAPOLACAO"], "moduladores": ["podendo"], "dificuldade": 2,
        "comentario_fonte": ("Gabarito ERRADO, com várias justificativas: Lei 4.595/1964, art. 10, IX "
                             "(fiscalização privativa do BCB); lição de manual de que a fiscalização nunca é "
                             "totalmente exógena ao banco central; modelo de supervisão do BCB (prudencial e de "
                             "conduta). Um dos comentários afirma, sem base, que a supervisão não pode ser "
                             "compartilhada com nenhum outro órgão."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE, prova de 2018 (a fonte só informa “C/E (2018)”; não confirmada)"],
    },
    # ------------------------------------------------------------------ E1-0786
    {
        "id": "ECO-E1-0786-1", "fonte_ref": "E1-0786", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("A regulação prudencial consiste em um tipo de regulação que estabelece requisitos para as "
                      "instituições financeiras com foco no gerenciamento de riscos e nos requerimentos mínimos de "
                      "capital para fazer frente aos riscos decorrentes das atividades financeiras."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A <u>regulação prudencial</u> consiste em um tipo de regulação que estabelece requisitos "
                      "para as instituições financeiras com foco no <u>gerenciamento de riscos</u> e nos "
                      "<u>requerimentos mínimos de capital</u> para fazer frente aos riscos decorrentes das "
                      "atividades financeiras."),
        "poucas": ("O item reproduz a definição do " + rx("BCB") + ": " + azb("regulação prudencial") + " = "
                   "requisitos de gestão de riscos, capital mínimo e limites operacionais, para que a quebra de "
                   "uma instituição não vire " + azb("risco sistêmico") + "."),
        "destrinchando": [
            "Definição do BCB: a regulação prudencial “estabelece requisitos para as instituições financeiras com "
            "foco no gerenciamento de riscos e nos requerimentos mínimos de capital para fazer face aos riscos "
            "decorrentes de suas atividades e nos limites operacionais”. O objetivo declarado é evitar o "
            + azb("efeito dominó") + " — o risco sistêmico.",
            "Distinção cobrada: regulação " + azb("prudencial") + " (solidez: capital, liquidez, alavancagem, "
            "gestão de riscos) × regulação " + azb("de conduta") + " (relação com clientes, transparência, "
            "prevenção à lavagem de dinheiro).",
            "O padrão internacional vem de " + azb("Basileia") + ". Basileia III, resposta à crise de 2008, "
            "elevou a qualidade e a quantidade do capital (capital principal mínimo de " + vd("4,5%") + " dos "
            "ativos ponderados pelo risco, mais " + vd("2,5%") + " de colchão de conservação e até "
            + vd("2,5%") + " de colchão contracíclico), criou a razão de alavancagem (" + vd("3%") + ") e os "
            "índices de liquidez LCR e NSFR.",
            rx("No Brasil") + ", as normas são do CMN e do BCB, aplicadas de forma " + azb("proporcional") + ": "
            "as instituições são segmentadas de S1 a S5 conforme porte e atividade internacional, e as maiores "
            "seguem as regras mais completas.",
        ],
        "dissecando": (cz("[literalidade]") + " Cópia quase literal do site do BCB. O CEBRASPE usa esse texto "
                       "institucional com frequência: quem conhece a fonte responde em segundos; quem não conhece "
                       "desconfia da definição “fácil demais”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A regulação prudencial tem como foco principal a proteção do consumidor de serviços financeiros "
            "e a transparência na oferta de produtos.”</i> → ERRADO (troca de conceito: isso é regulação de "
            "conduta)",
            "<i>“A regulação prudencial brasileira aplica as mesmas exigências a todas as instituições, "
            "independentemente do porte.”</i> → ERRADO (há segmentação proporcional, S1 a S5)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO, com várias respostas: definição literal do BCB; detalhamento de Basileia III "
                             "(capital principal, colchões, alavancagem, LCR, NSFR, Pilares 2 e 3, G-SIBs) e das "
                             "normas brasileiras de implementação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0787
    {
        "id": "ECO-E1-0787-1", "fonte_ref": "E1-0787", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("Em cumprimento às recomendações do Comitê da Basileia (Basileia III), o governo brasileiro "
                      "tem buscado reduzir os requerimentos de liquidez e de alavancagem das instituições "
                      "financeiras de grande porte para a melhoria da oferta de recursos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em cumprimento às recomendações do Comitê da Basileia (Basileia III), o governo brasileiro "
                       "tem buscado ") + vm("reduzir") + az(" os requerimentos de liquidez e de alavancagem das "
                                                            "instituições financeiras de grande porte ")
                    + vm("para a melhoria da oferta de recursos") + az(".")),
        "poucas": ("Basileia III " + vm("endureceu") + " as exigências: mais e melhor capital, limite de "
                   "alavancagem e índices de liquidez (LCR e NSFR). O objetivo é a " + azb("resiliência") + " do "
                   "sistema, não a expansão do crédito."),
        "destrinchando": [
            "O " + azb("Comitê de Basileia") + " (criado em " + vd("1974") + ", no âmbito do BIS) reagiu à crise "
            "de 2007–2008 com Basileia III, porque a crise revelou bancos com pouco capital de qualidade, "
            "alavancagem excessiva e dependência de financiamento de curtíssimo prazo.",
            "Respostas: " + azb("capital") + " — mais capital principal e colchões de conservação, contracíclico "
            "e para instituições sistemicamente importantes; " + azb("alavancagem") + " — razão mínima de "
            + vd("3%") + " entre capital e exposição total, sem ponderação por risco; " + azb("liquidez") + " — "
            "LCR (ativos líquidos para " + vd("30 dias") + " de estresse) e NSFR (financiamento estável para o "
            "horizonte de " + vd("1 ano") + ").",
            rx("No Brasil") + ", CMN e BCB implementaram o pacote a partir de " + vd("2013") + ", com LCR e NSFR "
            "exigidos dos bancos de maior porte (segmento S1). A direção foi sempre a de <b>elevar</b> "
            "exigências, com cronogramas de transição.",
            "Há, sim, um custo: capital e liquidez mais exigentes encarecem a intermediação e podem conter o "
            "crédito no curto prazo. É o preço aceito pela estabilidade — o oposto do que o item atribui ao "
            "governo.",
            vm("Regra-âncora: Basileia III = mais capital, menos alavancagem, mais liquidez."),
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " O verbo foi invertido (“reduzir” no lugar de "
                       "“elevar”) e a finalidade foi trocada (oferta de recursos no lugar de estabilidade). O "
                       "próprio comando entrega a pista: Basileia III nasceu da crise para “fomentar boas "
                       "práticas”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Basileia III introduziu um índice de alavancagem não baseado em risco como complemento aos "
            "requisitos de capital ponderados pelo risco.”</i> → CERTO",
            "<i>“As exigências de Basileia III aplicam-se no Brasil com a mesma intensidade a todas as "
            "instituições financeiras.”</i> → ERRADO (segmentação proporcional; LCR e NSFR para o S1)",
        ])],
        "reescrita": ("Em cumprimento às recomendações do Comitê da Basileia (Basileia III), o governo brasileiro "
                      "tem buscado " + hl("ampliar") + " os requerimentos de liquidez e de alavancagem das "
                      "instituições financeiras de grande porte " + hl("para o reforço da estabilidade do sistema "
                                                                        "financeiro") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. Basileia III aumenta requisitos de capital e liquidez e limita a "
                             "alavancagem; o foco é a estabilidade, não a oferta de recursos. Inclui comentário do "
                             "Clipping (histórico Basileia I, II e III; citação de Leite e Reis) e notícia do BCB "
                             "sobre aumento de exigência de capital."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "3083070-debf4034-35f7-4b0c-a09b-fc9e77ad532a.png", "tipo_fonte": "desconhecido",
                           "lado": "verso", "acao": "irrecuperavel (print de notícia do BCB, não preservado; "
                                                    "cortada)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0788
    {
        "id": "ECO-E1-0788-1", "fonte_ref": "E1-0788", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("O Sistema Financeiro Nacional deve obedecer às regras estabelecidas por colegiado composto "
                      "pelo Conselho Monetário Nacional, pelo Banco Central do Brasil e pela Comissão de Valores "
                      "Mobiliários."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O Sistema Financeiro Nacional deve obedecer às regras estabelecidas por <u>colegiado "
                      "composto pelo</u> Conselho Monetário Nacional, pelo Banco Central do Brasil e pela Comissão "
                      "de Valores Mobiliários."),
        "poucas": ("O CEBRASPE manteve CERTO com base no site do " + rx("BCB") + ": “as regras que disciplinam "
                   "o SFN são estabelecidas segundo " + azb("decisão colegiada") + " do CMN, do BC e da CVM”."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "não existe um colegiado único formado pelos três órgãos. “Decisão colegiada” "
                          "significa que " + azb("cada um") + " decide por órgão colegiado próprio (o plenário "
                          "do CMN, a Diretoria Colegiada do BCB, o Colegiado da CVM), cada qual em sua "
                          "competência. A banca indeferiu os recursos; a leitura rigorosa seria ERRADO.")],
        "destrinchando": [
            "Estrutura do SFN em três camadas: " + azb("órgãos normativos") + " (CMN, CNSP, CNPC), "
            + azb("supervisores") + " (BCB, CVM, Susep, Previc) e " + azb("operadores") + " (bancos, "
            "cooperativas, corretoras, bolsas, seguradoras, fundos de pensão…).",
            azb("CMN") + ": órgão máximo da área de moeda e crédito, composto pelo " + vd("Ministro da Fazenda")
            + " (presidente), pelo " + vd("Ministro do Planejamento e Orçamento") + " e pelo " + vd("Presidente "
            "do BCB") + " ⏳ (out/2026). Expede diretrizes e normas gerais (resoluções CMN).",
            azb("BCB") + " e " + azb("CVM") + " também editam normas — resoluções e circulares do BCB, resoluções "
            "da CVM —, por isso o BCB fala em regras estabelecidas pelos três. Mas cada um é colegiado em si: o "
            "CMN delibera em plenário, o BCB por sua Diretoria Colegiada, a CVM pelo seu Colegiado.",
            "O mesmo texto do BCB lembra que a regulação é aplicada de forma " + azb("segmentada") + " (S1 a S5), "
            "proporcional ao risco e à relevância internacional de cada instituição.",
        ],
        "dissecando": (cz("[literalidade · outro: paráfrase imprecisa]") + " O item reescreve o site do BCB e, ao "
                       "trocar “decisão colegiada do CMN, do BC e da CVM” por “colegiado composto pelo CMN, BC e "
                       "CVM”, cria um órgão que não existe. 🔥 O CEBRASPE costuma manter itens tirados de textos "
                       "oficiais mesmo com ruído de paráfrase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Conselho Monetário Nacional é integrado pelos presidentes do BCB e da CVM.”</i> → ERRADO "
            "(a CVM não integra o CMN)",
            "<i>“O CMN, o CNSP e o CNPC são os órgãos normativos do Sistema Financeiro Nacional.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "OUTRO"], "moduladores": ["deve"], "dificuldade": 3,
        "comentario_fonte": ("CERTO, mantido apesar de recursos. Clipping aponta releitura equivocada do site do BCB "
                             "(“decisão colegiada do CMN, do BC e da CVM”: cada órgão opera de forma colegiada); "
                             "outros comentários aceitam por interpretação ampla e distinguem órgãos normativos "
                             "(CMN, CNSP, CNPC) e supervisores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: não existe colegiado único formado por CMN, BCB e CVM; o item parafraseia mal o "
                    "site do BCB (“decisão colegiada”); recursos indeferidos e gabarito CERTO mantido",
                    "nota_redacao: comando do CACD 2024 (Basileia III) replicado a partir dos itens irmãos; a "
                    "frente da fonte trazia só a assertiva"],
    },
    # ------------------------------------------------------------------ E1-0789
    {
        "id": "ECO-E1-0789-1", "fonte_ref": "E1-0789", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("Todas as instituições integrantes do Sistema Financeiro Nacional são supervisionadas pelo "
                      "Banco Central do Brasil."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": vm("Todas") + az(" as instituições integrantes do Sistema Financeiro Nacional são "
                                    "supervisionadas pelo Banco Central do Brasil."),
        "poucas": ("O BCB é um de " + vd("quatro") + " supervisores do SFN: ao lado dele estão a " + azb("CVM")
                   + ", a " + azb("Susep") + " e a " + azb("Previc") + ", cada uma com seu segmento."),
        "destrinchando": [
            azb("BCB") + ": bancos (comerciais, múltiplos, de investimento), caixas econômicas, cooperativas de "
            "crédito, financeiras, administradoras de consórcio, instituições de pagamento, sociedades de crédito "
            "direto etc. Base: " + vd("Lei 4.595/1964, art. 10, IX") + ".",
            azb("CVM") + ": mercado de valores mobiliários — bolsas, companhias abertas, fundos de investimento, "
            "auditores, analistas (" + vd("Lei 6.385/1976") + "). Corretoras e distribuidoras respondem ao BCB "
            "(como instituições) e à CVM (como participantes do mercado de valores).",
            azb("Susep") + ": seguros, resseguros, capitalização e previdência complementar " + vd("aberta")
            + ", sob normas do CNSP. " + azb("Previc") + ": previdência complementar " + vd("fechada") + " "
            "(fundos de pensão), sob normas do CNPC (" + vd("Lei 12.154/2009") + ").",
            "Pegadinha frequente: o CNPC é <b>normativo</b>; quem supervisiona os fundos de pensão é a Previc.",
            vm("Regra-âncora: no SFN, cada segmento tem seu supervisor; o BCB não supervisiona tudo."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " Um só “Todas” faz o item. O BCB é o supervisor mais "
                       "importante, e é isso que torna a generalização plausível. Em SFN, desconfie de “todas”, "
                       "“exclusivamente” e “único”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os fundos de pensão são supervisionados pelo Conselho Nacional de Previdência Complementar.”</i> → "
            "ERRADO (troca de ator: a supervisora é a Previc; o CNPC é normativo)",
            "<i>“As cooperativas de crédito são supervisionadas pelo Banco Central do Brasil.”</i> → CERTO",
        ])],
        "reescrita": (hl("Nem todas") + " as instituições integrantes do Sistema Financeiro Nacional são "
                      "supervisionadas pelo Banco Central do Brasil" + hl(": há também a CVM, a Susep e a "
                                                                          "Previc") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["todas"], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. Supervisão dividida entre BCB, CVM, Susep e Previc, com dispositivos legais "
                             "de cada um. O primeiro comentário atribui ao CNPC a supervisão dos fundos de pensão "
                             "(é a Previc)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (271).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (quadro da estrutura do SFN, não preservado; conteúdo coberto "
                                   "pelo 📖)"}],
        "alertas": ["nota_redacao: comando do CACD 2024 (Basileia III) replicado a partir dos itens irmãos; a "
                    "frente da fonte trazia só a assertiva"],
    },
    # ------------------------------------------------------------------ E2-L00313
    {
        "id": "ECO-E2-L00313-1", "fonte_ref": "E2-L00313", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo aos Acordos de Basileia.",
        "rotulo_item": "Item",
        "assertiva": ("O Acordo de Basileia III, ao contrário de Basileia II, introduziu exigências de liquidez de "
                      "curto e de longo prazo com o objetivo de reduzir riscos de financiamento e de "
                      "transformações de maturidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Acordo de Basileia III, <u>ao contrário de Basileia II</u>, introduziu exigências de "
                      "<u>liquidez de curto e de longo prazo</u> com o objetivo de reduzir riscos de financiamento "
                      "e de transformações de maturidade."),
        "poucas": ("Basileia I e II tratavam de " + azb("capital") + "; a novidade de Basileia III foi pôr a "
                   + azb("liquidez") + " no centro, com o " + vd("LCR") + " (curto prazo) e o " + vd("NSFR")
                   + " (longo prazo)."),
        "destrinchando": [
            vd("LCR") + " (<i>Liquidity Coverage Ratio</i>): estoque de ativos líquidos de alta qualidade ≥ saídas "
            "líquidas de caixa em " + vd("30 dias") + " de estresse. Protege contra corridas e perda súbita de "
            "funding.",
            vd("NSFR") + " (<i>Net Stable Funding Ratio</i>): financiamento estável disponível ≥ financiamento "
            "estável requerido no horizonte de " + vd("1 ano") + ". Ataca o " + azb("descasamento de prazos") + " "
            "— financiar empréstimos longos com captação que pode sumir amanhã.",
            "Por que veio só em 2010: a crise de 2008 mostrou bancos <b>solventes</b> quebrando por falta de "
            "caixa (Northern Rock, Bear Stearns), dependentes de repo e papéis de curtíssimo prazo. Basileia II "
            "tinha três pilares (capital, supervisão, disciplina de mercado), mas nenhum padrão quantitativo "
            "global de liquidez.",
            rx("No Brasil") + ", o LCR vigora desde " + vd("2015") + " e o NSFR desde " + vd("2018") + ", ambos "
            "para as instituições do segmento S1.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " O item testa a cronologia das inovações: liquidez é "
                       "marca de Basileia III. O “ao contrário de Basileia II” é o ponto de risco — verdadeiro, "
                       "porque Basileia II não tinha índice de liquidez obrigatório."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Basileia II introduziu o LCR e o NSFR, posteriormente reforçados por Basileia III.”</i> → ERRADO "
            "(anacronismo: ambos são de Basileia III)",
            "<i>“O LCR exige ativos líquidos suficientes para cobrir saídas de caixa em um horizonte de um ano.”"
            "</i> → ERRADO (30 dias; um ano é o NSFR)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": ["ao contrário de"], "dificuldade": 1,
        "comentario_fonte": "CERTO. É uma inovação de Basileia III, ausente do desenho de Basileia II.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00536
    {
        "id": "ECO-E2-L00536-1", "fonte_ref": "E2-L00536", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Sobre moeda, política monetária e sistema financeiro, julgue (C ou E) o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("Na abordagem de supervisão microprudencial, o Banco Central do Brasil foca a saúde "
                      "financeira de cada instituição individualmente, analisando seu comportamento, a qualidade "
                      "de sua gestão de riscos e sua capacidade de enfrentar crises internas; na abordagem "
                      "macroprudencial, adota-se uma visão voltada para o sistema financeiro como um todo, "
                      "observando-se a interconectividade entre as instituições e os riscos sistêmicos que podem "
                      "surgir."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na abordagem de supervisão <u>microprudencial</u>, o Banco Central do Brasil foca a saúde "
                      "financeira de <u>cada instituição individualmente</u>, analisando seu comportamento, a "
                      "qualidade de sua gestão de riscos e sua capacidade de enfrentar crises internas; na "
                      "abordagem <u>macroprudencial</u>, adota-se uma visão voltada para o <u>sistema financeiro "
                      "como um todo</u>, observando-se a interconectividade entre as instituições e os riscos "
                      "sistêmicos que podem surgir."),
        "poucas": (azb("Micro") + " = solvência e liquidez de cada instituição; " + azb("macro") + " = risco "
                   "sistêmico, que nasce da interconexão e do ciclo. O item descreve as duas corretamente."),
        "destrinchando": [
            "A distinção ganhou força após 2008: bancos individualmente sólidos podem, juntos, gerar crise — por "
            "exposições cruzadas, vendas forçadas de ativos e crédito pró-cíclico. É a " + azb("falácia da "
            "composição") + " aplicada à regulação.",
            "Dimensões do risco sistêmico: " + azb("transversal") + " (interconexão, concentração, instituições "
            "grandes demais para quebrar) e " + azb("temporal") + " (pró-ciclicidade: crédito e alavancagem "
            "crescem juntos na euforia e desabam juntos na crise).",
            "Instrumentos macroprudenciais: colchão de capital " + azb("contracíclico") + ", adicional para "
            "instituições sistemicamente importantes, limites de LTV em crédito imobiliário, testes de estresse "
            "do sistema.",
            rx("No Brasil") + ", o BCB monitora o SFN nas duas vertentes, e o " + azb("Comitê de Estabilidade "
            "Financeira (Comef)") + " define a política macroprudencial; o Relatório de Estabilidade Financeira "
            "é semestral.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Reproduz a descrição institucional do BCB. "
                       "Itens desse tipo erram, quando erram, pela troca dos rótulos (micro ↔ macro) — "
                       "conferir a quem se atribui o “sistema como um todo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O colchão de capital contracíclico é instrumento típico da supervisão microprudencial.”</i> → "
            "ERRADO (troca de conceito: é macroprudencial)",
            "<i>“A abordagem macroprudencial parte da premissa de que a solidez de cada instituição isoladamente "
            "garante a estabilidade do sistema.”</i> → ERRADO (falácia da composição)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. Definição correta: a microprudencial foca o risco individual; a "
                             "macroprudencial, o risco que emerge da interação entre as instituições e do "
                             "sistema."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00144
    {
        "id": "ECO-E3-L00144-1", "fonte_ref": "E3-L00144", "destino": "41", "subtema": H2["bas"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": "Julgue os itens subsequentes, em relação aos principais acordos e organismos internacionais.",
        "rotulo_item": "Item",
        "assertiva": ("O acordo de Basileia II implementou a exigência de capital, por parte dos bancos comerciais, "
                      "para fazer frente ao risco de crédito."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O acordo de ") + vm("Basileia II") + az(" implementou a exigência de capital, por parte "
                                                                  "dos bancos comerciais, para fazer frente ao "
                                                                  "risco de crédito.")),
        "poucas": ("Quem " + azb("implementou") + " o capital mínimo contra o risco de crédito foi "
                   + vm("Basileia I (1988)") + ", com o índice de " + vd("8%") + " sobre ativos ponderados pelo "
                   "risco. Basileia II (2004) refinou o cálculo e acrescentou outros riscos."),
        "destrinchando": [
            azb("Basileia I (1988)") + ": capital mínimo de " + vd("8% dos ativos ponderados pelo risco") + " "
            "(o “Índice de Basileia”), com pesos simples por categoria (0% para soberano da OCDE, 50% para "
            "hipoteca, 100% para empresas). Foco quase exclusivo no " + azb("risco de crédito") + "; a emenda de "
            + vd("1996") + " incluiu o risco de mercado.",
            azb("Basileia II (2004)") + ": manteve os 8%, mas com cálculo sensível ao risco (abordagem "
            "padronizada com ratings ou modelos internos, IRB), acrescentou o " + azb("risco operacional") + " e "
            "organizou tudo em " + azb("três pilares") + ": requisitos mínimos de capital, revisão pela "
            "supervisão e disciplina de mercado (divulgação).",
            azb("Basileia III (2010)") + ": resposta a 2008 — capital de mais qualidade, colchões "
            "(conservação, contracíclico, sistêmico), razão de alavancagem e liquidez (LCR, NSFR).",
            rx("No Brasil") + ", Basileia I foi adotado em " + vd("1994") + " (Resolução CMN 2.099), e o índice "
            "mínimo brasileiro foi depois elevado acima dos 8%; Basileia II começou a ser implantado a partir de 2007.",
            vm("Regra-âncora: I = crédito (1988); II = três pilares + operacional (2004); III = liquidez + "
               "alavancagem + colchões (2010)."),
        ],
        "dissecando": (cz("[anacronismo · troca de ator]") + " Atribui a Basileia II a inovação de Basileia I. "
                       "O item é traiçoeiro porque Basileia II também exige capital para risco de crédito (Pilar "
                       "1); o erro está no verbo “implementou”, que aponta a origem da exigência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O acordo de Basileia II incorporou o risco operacional ao cálculo do capital mínimo e estruturou "
            "a regulação em três pilares.”</i> → CERTO",
            "<i>“O acordo de Basileia I instituiu índices mínimos de liquidez de curto prazo.”</i> → ERRADO "
            "(anacronismo: o LCR é de Basileia III)",
        ])],
        "reescrita": ("O acordo de " + hl("Basileia I") + " implementou a exigência de capital, por parte dos "
                      "bancos comerciais, para fazer frente ao risco de crédito."),
        "tipo_erro": ["ANACRONISMO", "TROCA_ATOR"], "moduladores": ["implementou"], "dificuldade": 2,
        "comentario_fonte": ("E. Reescrita com Basileia I; várias tabelas comparativas transcritas de Basileia I, "
                             "II e III (foco, capital, riscos, pilares, inovações), em parte com OCR ilegível; "
                             "resumo do site do BCB sobre as recomendações de Basileia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 140", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 141", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 142", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 143", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 144", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 145", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 146", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (OCR ilegível; conteúdo coberto pelas demais)"},
                          {"ref": "IMAGEM 147", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "cortada"},
                          {"ref": "IMAGEM 148", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "cortada"},
                          {"ref": "IMAGEM 149", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "cortada"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0563
    {
        "id": "ECO-E1-0563-1", "fonte_ref": "E1-0563", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_BDIG,
        "rotulo_item": "Item",
        "assertiva": ("Uma das características dos bancos digitais é a isenção de acompanhamento regulatório pelo "
                      "Banco Central do Brasil."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma das características dos bancos digitais é ") + vm("a isenção") + az(" de "
                    "acompanhamento regulatório pelo Banco Central do Brasil.")),
        "poucas": ("“Banco digital” é " + azb("modelo de negócio") + ", não categoria regulatória: a instituição "
                   "tem uma licença do BCB (banco, financeira, instituição de pagamento…) e segue as " + vm("mesmas "
                   "normas") + " de qualquer outra com aquela licença."),
        "destrinchando": [
            "Não há norma específica para “banco digital”. O BCB aplica a regra pela " + azb("atividade") + ", "
            "não pelo canal: quem capta depósitos e concede crédito é instituição financeira e precisa de "
            "autorização e supervisão do BCB (" + vd("Lei 4.595/1964") + "), atenda pela agência ou pelo "
            "aplicativo.",
            "Isso inclui exigências " + azb("prudenciais") + " (capital, liquidez, gestão de riscos, conforme o "
            "segmento S1 a S5) e de " + azb("conduta") + " (transparência de tarifas, atendimento, prevenção à "
            "lavagem de dinheiro, segurança cibernética).",
            "O que muda para os digitais é a escala de exigência: instituições menores ficam em segmentos com "
            "regras mais simples (" + azb("proporcionalidade") + "), o que reduz barreiras de entrada — mas não "
            "as isenta.",
            "Fintechs de crédito e de pagamento têm licenças próprias, também do BCB: " + azb("sociedade de "
            "crédito direto (SCD)") + ", " + azb("sociedade de empréstimo entre pessoas (SEP)") + " (" + vd("Res. "
            "CMN 4.656/2018") + ") e " + azb("instituição de pagamento") + " (" + vd("Lei 12.865/2013") + ").",
            vm("Regra-âncora: o BCB regula a atividade, não o canal."),
        ],
        "dissecando": (cz("[contradição]") + " O item transforma uma característica de marketing em privilégio "
                       "jurídico inexistente. Pista: isenção regulatória exigiria norma expressa, e nenhuma "
                       "instituição que capta recursos do público fica fora do perímetro do BCB."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os bancos digitais estão sujeitos às mesmas normas aplicáveis às instituições bancárias "
            "tradicionais com a mesma licença.”</i> → CERTO",
            "<i>“As instituições de pagamento, por não captarem depósitos, estão fora da regulação do BCB.”</i> "
            "→ ERRADO (são autorizadas e supervisionadas pelo BCB)",
        ])],
        "reescrita": ("Uma das características dos bancos digitais é " + hl("o atendimento predominantemente "
                      "remoto, sem isenção") + " de acompanhamento regulatório pelo Banco Central do Brasil."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. Bancos digitais estão sujeitos à regulamentação e supervisão do BCB como os "
                             "tradicionais; não há normativo específico, mas aplicam-se as mesmas normas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0564
    {
        "id": "ECO-E1-0564-1", "fonte_ref": "E1-0564", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_BDIG,
        "rotulo_item": "Item",
        "assertiva": "Um banco digital necessariamente deverá ser constituído como um banco comercial.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um banco digital ") + vm("necessariamente deverá") + az(" ser constituído como um banco "
                                                                                "comercial.")),
        "poucas": ("Sem regime próprio, o banco digital escolhe " + azb("qualquer licença") + " compatível com o "
                   "que pretende fazer: banco comercial, múltiplo, de investimento, financeira — ou nem é banco "
                   "(instituição de pagamento, SCD)."),
        "destrinchando": [
            "O BCB não tem um tipo jurídico “banco digital”: a instituição se enquadra nas espécies já "
            "existentes e segue as regras de autorização daquela espécie.",
            "Espécies possíveis: " + azb("banco comercial") + " (depósitos à vista, crédito de curto prazo), "
            + azb("banco múltiplo") + " (reúne carteiras — comercial, investimento, crédito imobiliário, "
            "financeira etc. —, com ao menos uma comercial ou de investimento), " + azb("banco de investimento")
            + ", " + azb("sociedade de crédito, financiamento e investimento") + ".",
            "Muitas empresas conhecidas do público como “bancos digitais” começaram, na verdade, como "
            + azb("instituições de pagamento") + " (conta de pagamento, cartão) combinadas com uma financeira "
            "ou uma SCD para o crédito — sem licença bancária.",
            "Na prática, quem quer captar depósitos à vista precisa de licença de banco comercial ou de banco "
            "múltiplo com carteira comercial — daí a confusão do item.",
        ],
        "dissecando": (cz("[restrição indevida · modulador absoluto]") + " “Necessariamente deverá” fecha uma "
                       "escolha que a regulação deixa aberta. Em itens sobre fintechs e bancos digitais, a banca "
                       "explora a ideia de que não existe licença “digital”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Não há regime de autorização específico para bancos digitais, que se enquadram nas espécies de "
            "instituição já existentes.”</i> → CERTO",
            "<i>“Para captar depósitos à vista, basta a autorização como instituição de pagamento.”</i> → ERRADO "
            "(conta de pagamento não é depósito à vista)",
        ])],
        "reescrita": ("Um banco digital " + hl("não precisa necessariamente") + " ser constituído como um banco "
                      "comercial" + hl(": pode ser banco múltiplo, de investimento ou outra espécie autorizada")
                      + "."),
        "tipo_erro": ["RESTRICAO", "GENERALIZACAO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. Aplica-se aos bancos digitais a mesma legislação dos tradicionais; podem ser "
                             "constituídos como qualquer espécie bancária autorizada (comercial, múltiplo, de "
                             "investimento etc.). Um dos comentários descreve banco múltiplo como operando seguros "
                             "e previdência."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0565
    {
        "id": "ECO-E1-0565-1", "fonte_ref": "E1-0565", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_BDIG,
        "rotulo_item": "Item",
        "assertiva": ("A categoria de banco digital reflete decisões operacionais e mercadológicas de cada banco, "
                      "como o acesso exclusivamente remoto e a busca por redução de tarifas. Dessa forma, bancos "
                      "tradicionais também podem se inserir nesse segmento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A categoria de banco digital reflete <u>decisões operacionais e mercadológicas</u> de cada "
                      "banco, como o acesso exclusivamente remoto e a busca por redução de tarifas. Dessa forma, "
                      "<u>bancos tradicionais também podem</u> se inserir nesse segmento."),
        "poucas": ("Como “digital” é " + azb("estratégia") + " e não licença, qualquer banco pode adotá-la — e os "
                   "grandes bancos tradicionais criaram suas próprias marcas e operações 100% digitais."),
        "destrinchando": [
            "O BCB descreve o banco digital como uma designação da própria instituição: atendimento remoto, "
            "estrutura enxuta, sem rede de agências, foco em experiência do usuário e tarifas menores.",
            "A " + azb("digitalização bancária") + " atinge todo o sistema: os grandes conglomerados migraram "
            "a maior parte das transações para o celular e lançaram operações digitais com marca própria para "
            "competir com as fintechs.",
            "As operações não diferem das de um banco comum: conta de depósito, investimentos, transferências, "
            "crédito. O que muda é o " + azb("canal") + " e a estrutura de custos.",
            "Vantagens: custo operacional menor, escala rápida, dados para análise de crédito. Dificuldades: "
            "confiança do público, falta de rede física (saques, atendimento presencial), concorrência com a "
            "base de clientes já instalada dos grandes bancos.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Paráfrase do texto do BCB. O "
                       "“exclusivamente remoto” assusta, mas é só exemplo de decisão operacional; o "
                       "“também podem” mantém a conclusão no campo da possibilidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bancos tradicionais estão impedidos de atuar no segmento digital, reservado às instituições de "
            "pagamento.”</i> → ERRADO (restrição indevida)",
            "<i>“A designação banco digital corresponde a uma espécie própria de instituição financeira, com "
            "regime de autorização específico.”</i> → ERRADO (é modelo de negócio, sem regime próprio)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["também podem"], "dificuldade": 1,
        "comentario_fonte": ("CERTO. Banco digital é designação da própria instituição (atendimento remoto, custos "
                             "menores); a digitalização atinge também os grandes conglomerados, que lançaram "
                             "operações digitais próprias."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0566
    {
        "id": "ECO-E1-0566-1", "fonte_ref": "E1-0566", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_BDIG,
        "rotulo_item": "Item",
        "assertiva": ("O advento de bancos digitais no mercado financeiro brasileiro levou a um aumento de "
                      "concentração e redução da concorrência no segmento bancário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O advento de bancos digitais no mercado financeiro brasileiro levou a ")
                    + vm("um aumento de concentração e redução da concorrência") + az(" no segmento bancário.")),
        "poucas": ("A entrada de bancos digitais e fintechs " + vm("ampliou a concorrência") + " e contribuiu "
                   "para " + azb("desconcentrar") + " um mercado historicamente dominado por poucos grandes "
                   "bancos."),
        "destrinchando": [
            "O " + rx("sistema bancário brasileiro") + " é tradicionalmente " + azb("concentrado") + ": poucos "
            "conglomerados detêm a maior parte de ativos, depósitos e crédito. Concentração alta e spreads altos "
            "andam juntos no diagnóstico do BCB.",
            "Os entrantes digitais têm custo de aquisição de cliente baixo, não pagam rede de agências e "
            "competiram sobretudo em contas sem tarifa, cartões e crédito pessoal. O resultado foi queda de "
            "tarifas e reação dos incumbentes, que lançaram suas próprias operações digitais.",
            "A política pública empurrou nessa direção: a agenda do BCB incluiu licenças para fintechs (SCD e "
            "SEP, " + vd("2018") + "), o " + azb("Pix") + " (" + vd("2020") + "), o " + azb("Open Finance") + " "
            "(desde " + vd("2021") + ") e o Cadastro Positivo — todos reduzem custos de troca e assimetria de "
            "informação.",
            "Ressalva honesta: o crédito continua relativamente concentrado e os efeitos sobre o spread são "
            "graduais. Mas a direção é de <b>mais</b> concorrência, não menos ⏳ (out/2026).",
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o efeito: entrada de concorrentes reduz "
                       "concentração. A pista é microeconômica — mais firmas e menor barreira de entrada, mais "
                       "contestabilidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Open Finance, ao permitir o compartilhamento de dados com consentimento do cliente, tende a "
            "reduzir custos de troca entre instituições e a estimular a concorrência.”</i> → CERTO",
            "<i>“A entrada dos bancos digitais eliminou a concentração do mercado de crédito brasileiro.”</i> → "
            "ERRADO (modulador absoluto: reduziu, não eliminou)",
        ])],
        "reescrita": ("O advento de bancos digitais no mercado financeiro brasileiro levou a "
                      + hl("uma redução da concentração e um aumento da concorrência") + " no segmento bancário."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A entrada de bancos digitais e fintechs aumentou a concorrência e reduziu a "
                             "concentração; benefícios listados pelo BCB (eficiência, concorrência no crédito, "
                             "redução de burocracia e de custo, inovação, acesso)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0828
    {
        "id": "ECO-E1-0828-1", "fonte_ref": "E1-0828", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": CMD_CACD26, "excerto": EXC_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("A eventual introdução de uma moeda digital de banco central (CBDC) pode alterar a estrutura "
                      "de captação das instituições financeiras, ao possibilitar que agentes econômicos mantenham "
                      "ativos diretamente junto ao banco central, o que pode afetar a transmissão da política "
                      "monetária e a estabilidade financeira."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A eventual introdução de uma moeda digital de banco central (CBDC) <u>pode</u> alterar a "
                      "estrutura de captação das instituições financeiras, ao possibilitar que agentes econômicos "
                      "mantenham ativos <u>diretamente junto ao banco central</u>, o que <u>pode</u> afetar a "
                      "transmissão da política monetária e a estabilidade financeira."),
        "poucas": ("Uma " + azb("CBDC de varejo") + " compete com o depósito bancário: se o público migra para "
                   "ela, os bancos perdem " + azb("funding") + " barato — é o risco de " + vm("desintermediação")
                   + ", com efeitos sobre crédito, política monetária e corridas."),
        "destrinchando": [
            "Hoje, o público só tem passivo do BC na forma de " + azb("papel-moeda") + "; o dinheiro eletrônico "
            "é depósito em banco comercial. Uma CBDC de varejo daria a todos um passivo <b>digital</b> do BC, "
            "sem risco de crédito.",
            azb("Captação") + ": parte dos depósitos à vista migraria para a CBDC. Os bancos teriam de "
            "substituir esse funding por fontes mais caras e menos estáveis (CDB, mercado), ou encolher o "
            "crédito.",
            azb("Transmissão monetária") + ": com menos depósitos, muda o canal do crédito bancário; se a CBDC "
            "for remunerada, sua taxa vira um novo instrumento (e um piso) para as taxas de mercado.",
            azb("Estabilidade") + ": em pânico, migrar do banco para o BC seria instantâneo — uma "
            + vm("corrida digital") + ". Por isso os desenhos discutidos incluem limites de posse por usuário "
            "e remuneração escalonada (proposta debatida para o euro digital).",
            rx("No Brasil") + ", o projeto " + azb("Drex") + " do BCB foi concebido para o atacado e para "
            "infraestrutura de ativos tokenizados, liquidando via instituições do sistema, e não como CBDC de "
            "varejo que substitua depósitos ⏳ (out/2026).",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Dois “pode” protegem o item, que "
                       "descreve o risco discutido em toda a literatura de bancos centrais. A pegadinha seria "
                       "trocar “pode” por “necessariamente reduzirá”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A introdução de uma CBDC de varejo reduzirá necessariamente o volume de crédito bancário.”</i> → "
            "ERRADO (modulador absoluto: depende do desenho e da reação dos bancos)",
            "<i>“Limites de posse por usuário são propostos para reduzir o risco de desintermediação e de "
            "corridas bancárias digitais.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode", "eventual"],
        "dificuldade": 2,
        "comentario_fonte": SO_GAB,
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0829
    {
        "id": "ECO-E1-0829-1", "fonte_ref": "E1-0829", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": True,
        "comando": CMD_CACD26, "excerto": EXC_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("Sistemas de pagamento digitais caracterizam-se por externalidades de rede, de modo que o "
                      "valor econômico da plataforma para cada usuário tende a aumentar à medida que cresce o "
                      "número de participantes no sistema."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sistemas de pagamento digitais caracterizam-se por <u>externalidades de rede</u>, de modo "
                      "que o valor econômico da plataforma para cada usuário <u>tende a aumentar</u> à medida que "
                      "cresce o número de participantes no sistema."),
        "poucas": ("É a definição de " + azb("externalidade de rede") + " (positiva, direta): cada novo usuário "
                   "aumenta o valor do sistema para todos os outros — um meio de pagamento vale pelo número de "
                   "pessoas que o aceitam."),
        "destrinchando": [
            azb("Externalidade de rede") + ": o benefício de usar um bem depende de quantos outros o usam. "
            "Telefone, redes sociais e meios de pagamento são os exemplos clássicos. O efeito não passa pelo "
            "preço — por isso é externalidade.",
            "Pagamentos são " + azb("mercados de dois lados") + " (" + oc("Rochet e Tirole") + "): o valor para "
            "o pagador depende de quantos recebedores aceitam, e vice-versa. Por isso as plataformas subsidiam "
            "um lado (cartões sem anuidade, Pix gratuito para pessoa física) para atrair o outro.",
            "Consequências econômicas: retornos crescentes de escala, " + azb("massa crítica") + " (abaixo dela a "
            "plataforma não decola), tendência a " + azb("concentração") + " (o vencedor leva quase tudo) e "
            "custos de troca — o que justifica regulação de interoperabilidade e acesso.",
            rx("No Brasil") + ", o " + azb("Pix") + " (lançado em " + vd("novembro de 2020") + ") ilustra o "
            "efeito: participação obrigatória das instituições maiores e uso gratuito para pessoas físicas "
            "garantiram a massa crítica em poucos meses, e o valor para cada usuário cresceu com a adesão "
            "de comerciantes.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de livro-texto aplicada a "
                       "pagamentos. O “tende a” protege contra exceções (congestionamento, fraude). Quem erra "
                       "costuma confundir externalidade de rede com economia de escala do lado da oferta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Externalidades de rede tendem a favorecer a fragmentação do mercado de pagamentos em muitas "
            "plataformas de porte semelhante.”</i> → ERRADO (inversão: tendem a concentrar)",
            "<i>“Como mercados de dois lados, plataformas de pagamento podem cobrar preços abaixo do custo de um "
            "dos lados para atrair o outro.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": SO_GAB,
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0830
    {
        "id": "ECO-E1-0830-1", "fonte_ref": "E1-0830", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": CMD_CACD26, "excerto": EXC_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("A atuação do Banco Central do Brasil na supervisão e na regulação do sistema financeiro não "
                      "se estende às instituições financeiras digitais, uma vez que tais instituições operam "
                      "exclusivamente por meio eletrônico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A atuação do Banco Central do Brasil na supervisão e na regulação do sistema financeiro ")
                    + vm("não se estende") + az(" às instituições financeiras digitais, ")
                    + vm("uma vez que tais instituições operam exclusivamente por meio eletrônico") + az(".")),
        "poucas": ("O BCB regula a " + azb("atividade") + " (captar, emprestar, fazer pagamentos), não o "
                   + azb("canal") + ": instituição digital autorizada a operar é supervisionada como qualquer "
                   "outra da mesma espécie."),
        "destrinchando": [
            "Toda instituição que capta recursos do público, concede crédito ou presta serviço de pagamento "
            "precisa de " + azb("autorização do BCB") + " (" + vd("Lei 4.595/1964") + "; " + vd("Lei 12.865/2013")
            + " para os arranjos e instituições de pagamento) e fica sujeita à sua supervisão.",
            "As exigências se aplicam em duas frentes: " + azb("prudencial") + " (capital, liquidez, gestão de "
            "riscos, proporcional ao segmento) e " + azb("de conduta") + " (transparência, atendimento, "
            "prevenção à lavagem de dinheiro). Instituições digitais acrescentam riscos que o BCB também "
            "regula: " + azb("segurança cibernética") + ", computação em nuvem, fraude em pagamentos "
            "instantâneos.",
            "O próprio texto do comando aponta o contrário do item: a digitalização “intensificou desafios "
            "relacionados à supervisão prudencial, à segurança operacional”. Mais risco operacional pede mais, "
            "não menos, supervisão.",
            vm("Regra-âncora: mesmo risco, mesma regulação — independentemente do canal."),
        ],
        "dissecando": (cz("[contradição · nexo indevido]") + " Afirma uma exclusão inexistente e a justifica por "
                       "um fato irrelevante (o canal eletrônico). A conexão “opera por meio eletrônico, logo não "
                       "é supervisionada” é o nexo fabricado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As instituições de pagamento estão sujeitas à autorização e à supervisão do Banco Central do "
            "Brasil.”</i> → CERTO",
            "<i>“Por operarem em ambiente digital, as fintechs de crédito estão sujeitas exclusivamente à "
            "regulação da CVM.”</i> → ERRADO (troca de ator: SCD e SEP são autorizadas pelo BCB)",
        ])],
        "reescrita": ("A atuação do Banco Central do Brasil na supervisão e na regulação do sistema financeiro "
                      + hl("estende-se") + " às instituições financeiras digitais, " + hl("pois operar por meio "
                      "eletrônico não altera a natureza das atividades que elas exercem") + "."),
        "tipo_erro": ["CONTRADICAO", "NEXO_INDEVIDO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": SO_GAB,
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0831
    {
        "id": "ECO-E1-0831-1", "fonte_ref": "E1-0831", "destino": "42", "subtema": H2["dig"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": CMD_CACD26, "excerto": EXC_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("A expansão dos meios de pagamento digitais implica, necessariamente, redução do papel das "
                      "instituições bancárias na intermediação de crédito na economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A expansão dos meios de pagamento digitais ") + vm("implica, necessariamente,")
                    + az(" redução do papel das instituições bancárias na intermediação de crédito na economia.")),
        "poucas": ("Pagamento e crédito são " + azb("funções distintas") + ": digitalizar os pagamentos não tira, "
                   "por si, o crédito dos bancos — que, aliás, também operam os pagamentos digitais. O "
                   + vm("“necessariamente”") + " derruba o item."),
        "destrinchando": [
            "Funções do sistema financeiro: " + azb("meio de pagamento") + " (transferir recursos), "
            + azb("intermediação") + " (captar de quem poupa e emprestar a quem investe), gestão de riscos. "
            "Uma inovação pode transformar a primeira sem deslocar a segunda.",
            azb("Instituições de pagamento") + " não podem conceder empréstimos com os recursos das contas de "
            "pagamento, que ficam segregados. Para emprestar, a fintech precisa de outra licença (SCD, SEP, "
            "financeira, banco).",
            "Os bancos tradicionais são grandes operadores dos pagamentos digitais (Pix, carteiras, cartões) e "
            "usam os dados de transações para conceder <b>mais</b> crédito, com melhor avaliação de risco.",
            "Há, sim, pressão competitiva: fintechs de crédito e o mercado de capitais disputam espaço, e "
            "receitas de tarifas dos bancos caem. Mas o efeito é contingente — pode haver mais crédito "
            "bancário, não menos.",
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " O CEBRASPE usa o “necessariamente” para "
                       "transformar uma possibilidade em lei. O texto do comando fala de desafios e debate, nunca "
                       "de consequência inevitável."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A expansão dos meios de pagamento digitais pode intensificar a concorrência na intermediação "
            "financeira.”</i> → CERTO",
            "<i>“Instituições de pagamento podem emprestar livremente os saldos mantidos pelos clientes em contas "
            "de pagamento.”</i> → ERRADO (os recursos são segregados e não financiam crédito)",
        ])],
        "reescrita": ("A expansão dos meios de pagamento digitais " + hl("não implica, necessariamente,")
                      + " redução do papel das instituições bancárias na intermediação de crédito na economia."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": SO_GAB,
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
]
