"""Cards do lote de redação 16 — ECO, passada 02 (nota 35: moeda, criação, multiplicador, demanda por moeda)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "agr": "🪙 Funções e agregados monetários",
    "mult": "🏦 Criação de moeda e multiplicador",
    "dem": "📊 Demanda por moeda",
}

CMD_NAB_DEF = ("Em relação ao sistema monetário e ao conceito de déficit público, julgue (C ou E) o item a "
               "seguir.")
CMD_NAB_CN = ("A respeito das contas nacionais, do balanço de pagamentos e da teoria monetária, julgue (C ou E) o "
              "item a seguir.")
CMD_NAB_TM = "Em relação à teoria monetária, julgue (C ou E) o item a seguir."
CMD_NAB_AGR = "Em relação aos agregados monetários e à política monetária, julgue (C ou E) o item a seguir."
CMD_NAB_MAC = "Sobre as teorias macroeconômicas, julgue (C ou E) o item a seguir."
CMD_NAB_TPM = "A respeito de teoria monetária e política monetária, julgue (C ou E) o item a seguir."
CMD_NAB_MSM = "Em relação à moeda e ao sistema monetário, julgue (C ou E) o item a seguir."
CMD_RT_BC = "A respeito do papel do Banco Central e da teoria monetária, julgue o item a seguir."
CMD_RT_BASE = ("Avalie a proposição abaixo sobre criação de base monetária, meios de pagamento e taxa de "
               "juros.")
CMD_RT_OFM = "A respeito do processo de oferta de moeda, julgue o item a seguir."
CMD_TJPA_1 = ("Considerando uma economia em que o Banco Central mantenha a taxa de juros constante por meio de "
              "política monetária ativa, e diante de uma política fiscal expansionista, julgue o item a seguir, a "
              "respeito do impacto sobre o agregado monetário M1.")
CMD_TJPA_2 = ("Acerca dos instrumentos utilizados pelo Banco Central e de conceitos relacionados aos principais "
              "agregados monetários, julgue o item subsequente.")
CMD_NIDI = ("A respeito do Banco Central e suas atribuições enquanto gestor da política monetária, julgue certo "
            "ou errado o item a seguir.")

FORM_MULT = ("Duas formas equivalentes do " + azb("multiplicador") + ": " + vd("m = (1 + c) / (c + r)")
             + ", com c = PMPP/DV e r = reservas/DV; ou, na notação de muitos cursos, "
             + vd("m = 1 / [1 − d(1 − R)]") + ", com d = DV/M1 e R = reservas/DV.")

CARDS = [
    # ------------------------------------------------------------------ E2-L00793
    {
        "id": "ECO-E2-L00793-1", "fonte_ref": "E2-L00793", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_DEF,
        "rotulo_item": "Item",
        "assertiva": ("O multiplicador dos meios de pagamento reflete a capacidade do sistema bancário de aumentar a "
                      "oferta de moeda a partir da base monetária inicial. Considere a fórmula M = mB, em que M é o "
                      "saldo dos meios de pagamento, B é a base monetária e m é o multiplicador. O multiplicador dos "
                      "meios de pagamento é diretamente proporcional à taxa de reservas mantidas pelos bancos "
                      "comerciais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O multiplicador dos meios de pagamento reflete a capacidade do sistema bancário de aumentar "
                       "a oferta de moeda a partir da base monetária inicial. Considere a fórmula M = mB, em que M é "
                       "o saldo dos meios de pagamento, B é a base monetária e m é o multiplicador. O multiplicador "
                       "dos meios de pagamento é ") + vm("diretamente") + az(" proporcional à taxa de reservas "
                       "mantidas pelos bancos comerciais.")),
        "poucas": ("Reserva é dinheiro que o banco <b>não empresta</b>: quanto maior a taxa de reservas, menos "
                   "rodadas de crédito e depósito, e " + azb("menor o multiplicador") + ". A relação é inversa."),
        "destrinchando": [
            "O processo: o público deposita, o banco guarda uma fração r como reserva e empresta o resto; o "
            "empréstimo volta ao sistema como novo depósito, que de novo é parcialmente emprestado. A soma dessas "
            "rodadas é a " + azb("moeda escritural") + " criada a partir da " + azb("base monetária") + ".",
            "No modelo mais simples (o público não retém papel-moeda), o multiplicador é " + vd("m = 1/r")
            + ": com r = " + vd("20%") + ", m = " + vd("5") + "; com r = " + vd("50%") + ", m = " + vd("2")
            + ". Dobrar a taxa de reservas reduz m — é proporcionalidade <b>inversa</b>.",
            FORM_MULT + " Em qualquer das duas, r (ou R) está no denominador de forma que aumentá-lo reduz m.",
            "As reservas incluem as " + azb("compulsórias") + " (fixadas pelo Banco Central) e as "
            + azb("voluntárias") + " (encaixes por precaução). Por isso o compulsório é instrumento de política "
            "monetária: elevá-lo contrai os meios de pagamento sem mexer na base.",
            vm("Regra-âncora: ↑ reservas ou ↑ papel-moeda retido pelo público → ↓ multiplicador; ↑ depósitos → "
               "↑ multiplicador."),
        ],
        "dissecando": (cz("[inversão]") + " As duas primeiras frases são definição correta e servem de isca; o "
                       "erro está numa palavra só, “diretamente”, que inverte o sinal da relação. Em itens de "
                       "multiplicador, confira sempre o sentido (↑ ou ↓) de cada parâmetro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o multiplicador é inversamente relacionado à taxa de reservas mantidas pelos bancos.”</i> → "
            "CERTO",
            "<i>“…o multiplicador é diretamente proporcional à parcela dos meios de pagamento mantida como "
            "depósitos à vista.”</i> → CERTO (d maior → m maior)",
            "<i>“…o multiplicador independe da preferência do público por papel-moeda.”</i> → ERRADO (c também "
            "entra na fórmula e reduz m)",
        ])],
        "reescrita": ("O multiplicador dos meios de pagamento reflete a capacidade do sistema bancário de aumentar a "
                      "oferta de moeda a partir da base monetária inicial. Considere a fórmula M = mB, em que M é o "
                      "saldo dos meios de pagamento, B é a base monetária e m é o multiplicador. O multiplicador dos "
                      "meios de pagamento é " + hl("inversamente") + " proporcional à taxa de reservas mantidas pelos bancos "
                      "comerciais."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["diretamente"], "dificuldade": 1,
        "comentario_fonte": ("Multiplicador inversamente proporcional à taxa de reservas; m = 1/r no caso simples; "
                             "fórmula m = 1/[1 − d(1 − R)]: quanto maior R, menor m."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 115", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00796
    {
        "id": "ECO-E2-L00796-1", "fonte_ref": "E2-L00796", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_DEF,
        "rotulo_item": "Item",
        "assertiva": ("O multiplicador dos meios de pagamento é maior quando o público prefere manter uma maior "
                      "proporção de seus recursos na forma de moeda manual (papel-moeda)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O multiplicador dos meios de pagamento é ") + vm("maior") + az(" quando o público prefere "
                       "manter uma maior proporção de seus recursos na forma de moeda manual (papel-moeda).")),
        "poucas": ("Papel-moeda retido pelo público é um " + azb("vazamento") + ": não volta ao banco como depósito "
                   "e não alimenta novas rodadas de crédito. Mais moeda manual → " + azb("multiplicador menor") + "."),
        "destrinchando": [
            "Os " + azb("meios de pagamento") + " (M1) somam " + vd("PMPP + DV") + ": papel-moeda em poder do "
            "público (moeda manual) e depósitos à vista (moeda escritural). Só a parte depositada entra no "
            "processo de criação de moeda pelos bancos.",
            FORM_MULT,
            "Com c maior (ou d menor), m cai. Exemplo com r = " + vd("0,2") + ": se c = " + vd("0,25") + ", m = "
            "1,25/0,45 ≈ " + vd("2,8") + "; se c sobe para " + vd("1") + ", m = 2/1,2 ≈ " + vd("1,7") + ".",
            "No limite em que o público guarda <b>tudo</b> em papel-moeda (d = 0), m = " + vd("1") + ": os "
            "meios de pagamento se reduzem à própria base, porque não há depósito a multiplicar.",
            "É o mecanismo das " + azb("corridas bancárias") + ": a desconfiança faz o público sacar, c sobe, o "
            "multiplicador despenca e M1 se contrai mesmo com base constante.",
        ],
        "dissecando": (cz("[inversão]") + " O item descreve o parâmetro certo (preferência por papel-moeda), mas "
                       "troca o sentido do efeito: “maior” no lugar de “menor”. Pista: tudo o que tira dinheiro do "
                       "circuito bancário reduz o multiplicador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é maior quando o público mantém maior proporção de seus recursos como depósitos à vista.”</i> → "
            "CERTO",
            "<i>“Uma corrida bancária eleva o multiplicador, pois aumenta o papel-moeda em circulação.”</i> → "
            "ERRADO (inversão: o multiplicador cai)",
        ])],
        "reescrita": ("O multiplicador dos meios de pagamento é " + hl("menor") + " quando o público prefere manter "
                      "uma maior proporção de seus recursos na forma de moeda manual (papel-moeda)."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Mais papel-moeda retido reduz depósitos e a criação de moeda escritural; m = "
                             "(1 + c)/(c + r) ou m = 1/[1 − d(1 − R)]; ↑c reduz m."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 118", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00936
    {
        "id": "ECO-E2-L00936-1", "fonte_ref": "E2-L00936", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_CN,
        "rotulo_item": "Item",
        "assertiva": ("A demanda por moeda está relacionada positivamente com a taxa de juros, ou seja, quanto maior "
                      "a taxa de juros, maior a demanda por moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A demanda por moeda está relacionada ") + vm("positivamente") + az(" com a taxa de juros, "
                       "ou seja, quanto maior a taxa de juros, ") + vm("maior") + az(" a demanda por moeda.")),
        "poucas": ("O juro é o " + azb("custo de oportunidade") + " de reter moeda: quanto mais alto, mais caro "
                   "ficar líquido e " + azb("menor") + " a demanda por moeda. A relação é negativa."),
        "destrinchando": [
            "Na " + oc("Teoria Geral") + " (" + vd("1936") + "), " + oc("Keynes") + " separa três motivos para "
            "reter moeda: " + azb("transação") + " (cobrir o intervalo entre receitas e despesas), "
            + azb("precaução") + " (reserva contra imprevistos) e " + azb("especulação") + ".",
            "Os dois primeiros dependem sobretudo da " + azb("renda") + ": L₁(Y), crescente em Y. O motivo "
            "especulação depende dos " + azb("juros") + ": L₂(i), decrescente em i. Daí "
            + vd("L = L₁(Y) + L₂(i)") + ".",
            "Lógica da especulação: o agente compara o juro corrente com o juro que considera “normal”. Juro "
            "corrente alto → espera queda → prevê alta no preço dos títulos → troca moeda por títulos (demanda "
            "menos moeda). Juro baixo → espera alta → prefere ficar em moeda para comprar títulos mais baratos "
            "depois.",
            "Abordagens posteriores chegam ao mesmo sinal: no modelo de " + oc("Baumol-Tobin") + ", até a "
            "demanda para transações cai com o juro, porque ele encarece manter saldos ociosos.",
            "No limite, a " + azb("armadilha da liquidez") + ": com juro muito baixo, todos esperam alta, e a "
            "demanda por moeda fica infinitamente elástica (L horizontal).",
            vm("Regra-âncora: demanda por moeda — positiva com a renda, negativa com os juros."),
        ],
        "grafico_verso": "ECO-E2-L00936-1-V1",
        "dissecando": (cz("[inversão]") + " O item inverte o sinal da relação e, para reforçar, repete a "
                       "inversão na paráfrase (“ou seja, quanto maior…, maior…”). A paráfrase redundante não salva "
                       "nada: ela só confirma o erro. Cuidado com a confusão com a <b>oferta</b> de fundos "
                       "emprestáveis, que sim é crescente nos juros."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda por moeda está relacionada positivamente com o nível de renda.”</i> → CERTO",
            "<i>“Na armadilha da liquidez, a demanda por moeda é perfeitamente inelástica à taxa de juros.”</i> → "
            "ERRADO (inversão: é infinitamente elástica)",
        ])],
        "reescrita": ("A demanda por moeda está relacionada " + hl("negativamente") + " com a taxa de juros, ou "
                      "seja, quanto maior a taxa de juros, " + hl("menor") + " a demanda por moeda."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Três motivos keynesianos (transação, precaução, especulação); especulação depende "
                             "dos juros em relação ao juro normal; quanto maior o juro, menor a demanda por "
                             "moeda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00951
    {
        "id": "ECO-E2-L00951-1", "fonte_ref": "E2-L00951", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_TM,
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia tradicional, o multiplicador monetário é calculado a partir da razão entre "
                      "depósitos à vista em bancos comerciais e reservas bancárias."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma economia tradicional, o multiplicador monetário é calculado a partir da razão entre ")
                    + vm("depósitos à vista em bancos comerciais e reservas bancárias") + az(".")),
        "poucas": ("O multiplicador monetário mede quantas vezes os " + azb("meios de pagamento") + " superam a "
                   + azb("base monetária") + ": " + vd("m = M1/B") + ". A razão DV/reservas é outra coisa."),
        "destrinchando": [
            "Definição: " + vd("M1 = m · B") + ", logo " + vd("m = M1/B") + ". No numerador, "
            + vd("M1 = PMPP + DV") + " (papel-moeda em poder do público + depósitos à vista); no denominador, "
            + vd("B = PMPP + R") + " (papel-moeda em poder do público + reservas bancárias).",
            "A razão DV/R é o " + azb("multiplicador dos depósitos") + " (= 1/r): diz quantos reais de depósito "
            "cada real de reserva sustenta. Ela ignora o papel-moeda retido pelo público, que está nos dois "
            "agregados e não se multiplica.",
            "As duas razões só coincidem num caso-limite: se o público não guarda papel-moeda (PMPP = 0), M1 = DV "
            "e B = R, e então m = DV/R = 1/r.",
            "Com papel-moeda, o multiplicador completo fica " + vd("m = (1 + c)/(c + r)") + ", menor que 1/r. "
            "Ex.: c = " + vd("0,25") + ", r = " + vd("0,2") + " → m ≈ " + vd("2,8") + ", enquanto DV/R = "
            + vd("5") + ".",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca o multiplicador monetário (M1/B) pelo "
                       "multiplicador dos depósitos (DV/R). Pista: um multiplicador é sempre “agregado final ÷ "
                       "agregado de origem”; se o numerador não é M1 e o denominador não é B, desconfie."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o público não retém papel-moeda, o multiplicador monetário é igual à razão entre depósitos à "
            "vista e reservas bancárias.”</i> → CERTO",
            "<i>“O multiplicador monetário é a razão entre a base monetária e os meios de pagamento.”</i> → "
            "ERRADO (inversão: M1/B, e não B/M1)",
        ])],
        "reescrita": ("Em uma economia tradicional, o multiplicador monetário é calculado a partir da razão entre "
                      + hl("meios de pagamento (M1) e base monetária") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Multiplicador bancário: m = M1/B, razão entre meios de pagamento e base monetária.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00952
    {
        "id": "ECO-E2-L00952-1", "fonte_ref": "E2-L00952", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_TM,
        "rotulo_item": "Item",
        "assertiva": ("Se a parcela dos meios de pagamentos que os agentes mantêm como depósitos à vista aumentar e "
                      "se a proporção de reservas bancárias em relação ao depósito à vista diminuir, então o "
                      "multiplicador da base monetária aumentará."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a parcela dos meios de pagamentos que os agentes mantêm como depósitos à vista "
                      "<u>aumentar</u> e se a proporção de reservas bancárias em relação ao depósito à vista "
                      "<u>diminuir</u>, então o multiplicador da base monetária <u>aumentará</u>."),
        "poucas": ("Os dois movimentos empurram para o mesmo lado: mais " + azb("depósitos") + " (d ↑) e menos "
                   + azb("reservas") + " (R ↓) significam mais dinheiro girando no crédito — o multiplicador "
                   "sobe."),
        "destrinchando": [
            "O multiplicador depende de dois comportamentos: do <b>público</b> (quanto de M1 fica em depósito, "
            "d = DV/M1; o resto, 1 − d, fica em papel-moeda) e dos <b>bancos</b> (quanto dos depósitos "
            "fica parado como reserva, R = reservas/DV).",
            "Fórmula do curso: " + vd("m = 1 / [1 − d(1 − R)]") + ". O termo d(1 − R) é a fração de cada real "
            "de M1 que volta ao banco <b>e</b> é reemprestada; quanto maior, menor o denominador e maior m.",
            "Conta: d = " + vd("0,5") + " e R = " + vd("0,2") + " → m = 1/(1 − 0,4) ≈ " + vd("1,67") + ". Com "
            "d = " + vd("0,6") + " e R = " + vd("0,1") + " → m = 1/(1 − 0,54) ≈ " + vd("2,17") + ".",
            vm("Regra-âncora: d ↑ → m ↑; R ↑ → m ↓ (e vice-versa)."),
            "Como os dois choques têm o mesmo sinal, o item é seguro. A banca costuma complicar combinando "
            "choques de sinais <b>opostos</b> (d ↑ e R ↑), em que o resultado fica indeterminado sem números.",
        ],
        "dissecando": (cz("[literalidade]") + " Aplicação direta da regra do multiplicador, com dois parâmetros "
                       "no sentido favorável. O risco é a leitura apressada de “reservas… diminuir” como "
                       "contração; a pista é lembrar que reserva é o que o banco <b>deixa de emprestar</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a parcela de depósitos à vista aumentar e a proporção de reservas também aumentar, o "
            "multiplicador necessariamente aumentará.”</i> → ERRADO (efeitos opostos: resultado "
            "indeterminado)",
            "<i>“Se o público passar a reter mais papel-moeda e os bancos reduzirem reservas, o multiplicador "
            "pode tanto subir quanto cair.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("m = 1/[1 − d(1 − R)]; R ↑ → m ↓; d ↑ → m ↑; d aumenta e R cai → m aumenta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 154", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 155", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "texto"}],
        "alertas": ["quase_duplicata: ECO-E2-L01269-1 (mesma assertiva, Pré-TPS/2023)"],
    },
    # ------------------------------------------------------------------ E2-L00953
    {
        "id": "ECO-E2-L00953-1", "fonte_ref": "E2-L00953", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_TM,
        "rotulo_item": "Item",
        "assertiva": ("Há criação de meios de pagamento quando uma empresa saca recursos de sua conta de depósitos à "
                      "vista em um banco comercial e realiza, com esses recursos, o pagamento de seus funcionários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Há criação") + az(" de meios de pagamento quando uma empresa saca recursos de sua conta de "
                                          "depósitos à vista em um banco comercial e realiza, com esses recursos, o "
                                          "pagamento de seus funcionários.")),
        "poucas": ("O saque troca um " + azb("haver monetário") + " por outro (depósito à vista → papel-moeda), e o "
                   "pagamento só passa o papel-moeda de mão dentro do público. M1 muda de " + azb("composição")
                   + ", não de tamanho."),
        "destrinchando": [
            "Meios de pagamento: " + vd("M1 = PMPP + DV") + " — moeda manual (papel-moeda e moedas metálicas em "
            "poder do público não bancário) + moeda escritural (depósitos à vista).",
            vm("Regra-âncora: só há criação de moeda quando o setor bancário entrega um haver monetário ao público "
               "em troca de um haver não monetário; há destruição no caminho inverso."),
            "Criação: banco concede empréstimo, desconta duplicata, compra título ou imóvel do público, BC compra "
            "dólares de um exportador. Destruição: público quita empréstimo, compra título do banco, BC vende "
            "divisas ao importador.",
            "No item: (1) o saque reduz DV e aumenta PMPP no mesmo valor; (2) o pagamento de salários transfere o "
            "PMPP da empresa para os funcionários, todos fora do sistema bancário. Nenhuma das etapas envolve "
            "troca de haver não monetário com banco → " + vd("ΔM1 = 0") + ".",
            "Também não altera a base: PMPP sobe e o caixa do banco cai; o que muda é a composição.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item chama de “criação” uma simples " + azb("mudança de "
                       "composição") + " de M1. A pista é que nenhum banco adquire ativo não monetário: "
                       "quando todos os envolvidos são do público (empresa, funcionários), M1 não se altera."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Há criação de meios de pagamento quando um banco comercial concede empréstimo a uma empresa, "
            "creditando o valor em sua conta de depósitos à vista.”</i> → CERTO",
            "<i>“Há destruição de meios de pagamento quando uma empresa quita empréstimo junto a um banco "
            "comercial.”</i> → CERTO",
            "<i>“Há destruição de meios de pagamento quando o funcionário deposita o salário recebido em "
            "espécie.”</i> → ERRADO (troca de conceito: só muda a composição)",
        ])],
        "reescrita": (hl("Não há criação nem destruição") + " de meios de pagamento quando uma empresa saca recursos "
                      "de sua conta de depósitos à vista em um banco comercial e realiza, com esses recursos, o "
                      "pagamento de seus funcionários."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Criação exige troca de haver não monetário do público por haver monetário do setor "
                             "bancário; aqui houve troca de DV por PMPP — mera substituição de moeda escritural "
                             "por manual."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00988-1 (mesma assertiva, Pré-TPS/2023)"],
    },
    # ------------------------------------------------------------------ E2-L00988
    {
        "id": "ECO-E2-L00988-1", "fonte_ref": "E2-L00988", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_AGR,
        "rotulo_item": "Item",
        "assertiva": ("Há criação de meios de pagamento quando uma empresa saca recursos de sua conta de depósitos à "
                      "vista em um banco comercial e realiza, com esses recursos, o pagamento de seus funcionários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Há criação") + az(" de meios de pagamento quando uma empresa saca recursos de sua conta de "
                                          "depósitos à vista em um banco comercial e realiza, com esses recursos, o "
                                          "pagamento de seus funcionários.")),
        "poucas": ("É transação entre haveres <b>monetários</b> e entre agentes do " + azb("setor não bancário")
                   + ": DV vira PMPP, que passa da empresa aos empregados. O total de M1 fica igual."),
        "destrinchando": [
            "Contabilize em M1 = PMPP + DV. Saque de 100: DV " + vd("−100") + ", PMPP " + vd("+100") + " → M1 "
            "inalterado. Pagamento dos salários: o PMPP sai da empresa e vai para os funcionários → PMPP e M1 "
            "inalterados.",
            "Se a empresa pagasse por transferência para as contas dos funcionários, seria a mesma coisa: DV de "
            "um titular vira DV de outro. Transferência entre agentes do público nunca cria moeda.",
            "Para haver " + azb("criação") + ", o setor bancário (BC + bancos comerciais) precisa entregar um "
            "haver monetário em troca de um <b>não monetário</b> do público (crédito, título, bem, divisa). Para "
            "haver " + azb("destruição") + ", o inverso.",
            "Mesma lógica para os agregados amplos: aplicar o salário em poupança tira de M1 e põe em M2 — muda "
            "o M1, mas não cria moeda no conceito amplo.",
            vm("Regra-âncora: quem são as partes? Público com público → nada; banco com público, trocando "
               "monetário por não monetário → cria ou destrói."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Descreve um movimento <b>dentro</b> de M1 (moeda escritural → "
                       "manual) e o rotula como criação. 🔥 Item recorrente da banca, em versões com saque, "
                       "depósito e transferência — em todas a resposta é a mesma: só muda a composição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A conversão de depósitos à vista em papel-moeda pelo público altera a composição, mas não o "
            "montante, dos meios de pagamento.”</i> → CERTO",
            "<i>“Há criação de meios de pagamento quando um banco comercial adquire um imóvel de uma empresa, "
            "pagando com crédito em conta.”</i> → CERTO",
            "<i>“O saque reduz os meios de pagamento, pois diminui os depósitos à vista.”</i> → ERRADO (meia-"
            "verdade: o PMPP sobe no mesmo valor)",
        ])],
        "reescrita": (hl("Não há criação nem destruição") + " de meios de pagamento quando uma empresa saca recursos "
                      "de sua conta de depósitos à vista em um banco comercial e realiza, com esses recursos, o "
                      "pagamento de seus funcionários."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("M1 = PMPP + DV; o saque apenas transfere DV para PMPP — muda a composição de M1. "
                             "Linha duplicada (E2-L01232): transferência entre agentes do setor não bancário; "
                             "criação exige que o setor bancário entregue haver monetário por haver não "
                             "monetário."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L01232 (mesma assertiva e mesma prova) fundida neste card",
                    "quase_duplicata: ECO-E2-L00953-1 (mesma assertiva, Pré-TPS/2024)"],
    },
    # ------------------------------------------------------------------ E2-L00989
    {
        "id": "ECO-E2-L00989-1", "fonte_ref": "E2-L00989", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_AGR,
        "rotulo_item": "Item",
        "assertiva": "M3 inclui depósitos de poupança, mas não inclui operações compromissadas registradas no Selic.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("M3 inclui depósitos de poupança") + vm(", mas não inclui") + az(" operações compromissadas "
                                                                                    "registradas no Selic.")),
        "poucas": ("As " + azb("operações compromissadas") + " com títulos registradas no Selic são justamente o que "
                   "o M3 acrescenta ao M2 (com as quotas de fundos de renda fixa); a poupança já vem do M2."),
        "destrinchando": [
            "Os agregados são " + azb("encaixados") + ": cada um contém o anterior e acrescenta haveres de "
            "liquidez decrescente.",
            "<b>M1</b> = " + vd("PMPP + depósitos à vista") + " (moeda em sentido estrito, emitida pelo BC e "
            "pelos bancos comerciais).",
            "<b>M2</b> = M1 + " + vd("depósitos especiais remunerados + depósitos de poupança + títulos emitidos "
                                     "por instituições depositárias") + " (CDB, letras de câmbio etc.).",
            "<b>M3</b> = M2 + " + vd("quotas de fundos de renda fixa + operações compromissadas registradas no "
                                     "Selic") + ".",
            "<b>M4</b> = M3 + " + vd("títulos públicos de alta liquidez") + " em poder do público.",
            "Lógica: quanto mais alto o índice, mais amplo o agregado e menor a liquidez do item acrescentado. "
            "A poupança, por estar em M2, está automaticamente em M3 e M4 — por isso a primeira metade do item é "
            "verdadeira.",
        ],
        "condicionais": [("⏳ Desatualizado (out/2026)",
                          "a composição acima é a da metodologia do Banco Central adotada no início dos anos "
                          "2000 e cobrada pelas bancas; o BCB revisa periodicamente a classificação dos agregados, "
                          "de modo que vale conferir a nota metodológica vigente antes de usar números atuais.")],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A 1ª metade é verdadeira (poupança está em M2, "
                       "logo em M3); o erro foi enxertado no “mas não inclui”, deslocando as compromissadas para "
                       "fora do agregado em que elas entram. Para itens de agregados, memorize o que cada nível "
                       "<b>acrescenta</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“M2 inclui depósitos de poupança, mas não inclui quotas de fundos de renda fixa.”</i> → CERTO",
            "<i>“Os títulos públicos federais em poder do público integram o M3.”</i> → ERRADO (dado alterado: "
            "entram no M4)",
        ])],
        "reescrita": ("M3 inclui depósitos de poupança" + hl(" e também") + " operações compromissadas registradas "
                      "no Selic."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["mas não"], "dificuldade": 2,
        "comentario_fonte": ("M3 = M2 + títulos de renda fixa + operações compromissadas registradas no Selic; "
                             "M2 = M1 + depósitos especiais remunerados + poupança + títulos de instituições "
                             "depositárias."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00991
    {
        "id": "ECO-E2-L00991-1", "fonte_ref": "E2-L00991", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_AGR,
        "rotulo_item": "Item",
        "assertiva": "Se o papel moeda em poder do público for zero, o multiplicador monetário será igual a um.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o papel moeda em poder do público for zero, o multiplicador monetário será ")
                    + vm("igual a um") + az(".")),
        "poucas": ("Sem papel-moeda com o público, todo M1 é depósito e o multiplicador passa a depender só das "
                   + azb("reservas") + ": " + vd("m = 1/R") + ", que é maior que 1 sempre que R < 1."),
        "destrinchando": [
            "Na fórmula " + vd("m = 1 / [1 − d(1 − R)]") + ", PMPP = 0 significa d = DV/M1 = " + vd("1") + ". "
            "Então m = 1/[1 − (1 − R)] = " + vd("1/R") + ". Com R = " + vd("0,2") + ", m = " + vd("5") + ".",
            "Pela outra forma, " + vd("m = (1 + c)/(c + r)") + " com c = PMPP/DV = 0: m = " + vd("1/r")
            + " — o mesmo resultado. É o " + azb("multiplicador bancário simples") + " dos livros-texto.",
            "Quando o multiplicador vale 1? Em dois casos-limite opostos ao do item: (a) o público guarda "
            + "<b>tudo</b> em papel-moeda (d = 0), e não há depósito a multiplicar; (b) os bancos mantêm "
            + vd("100%") + " de reservas (R = 1), como no " + azb("“narrow banking”") + ", e não emprestam nada.",
            "Intuição: PMPP é vazamento do processo de criação de moeda. Zerar o vazamento <b>maximiza</b> o "
            "multiplicador, dado R; não o reduz a 1.",
        ],
        "dissecando": (cz("[dado alterado · inversão]") + " Troca o resultado (1/R) por 1, o valor do caso-limite "
                       "oposto (d = 0 ou R = 1). Pista: eliminar o papel-moeda retido tira um freio do "
                       "multiplicador — o valor só pode subir."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o público retiver todos os seus meios de pagamento em papel-moeda, o multiplicador será igual "
            "a um.”</i> → CERTO",
            "<i>“Se os bancos mantiverem reservas de 100% dos depósitos à vista, o multiplicador será igual a "
            "zero.”</i> → ERRADO (dado alterado: será 1)",
        ])],
        "reescrita": ("Se o papel moeda em poder do público for zero, o multiplicador monetário será "
                      + hl("igual a 1/R, o inverso da taxa de reservas bancárias") + "."),
        "tipo_erro": ["DADO_ALTERADO", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Com PMPP = 0, DV/M1 = 100% e o multiplicador depende apenas das reservas: m = 1/R."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01008
    {
        "id": "ECO-E2-L01008-1", "fonte_ref": "E2-L01008", "destino": "35", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MAC,
        "rotulo_item": "Item",
        "assertiva": "Na teoria keynesiana, taxa de juros é o preço que iguala poupança e investimento.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na teoria keynesiana, taxa de juros é o preço que iguala ") + vm("poupança e investimento")
                    + az(".")),
        "poucas": ("Juro que iguala poupança e investimento é o da " + azb("teoria clássica (fundos "
                   "emprestáveis)") + ". Para Keynes, o juro é " + azb("fenômeno monetário") + ": iguala oferta "
                   "e demanda de moeda."),
        "destrinchando": [
            "<b>Clássicos / neoclássicos</b>: o juro real é o " + azb("prêmio pela espera") + " (renúncia ao "
            "consumo presente). Poupança (oferta de fundos) cresce com o juro; investimento (demanda de fundos) "
            "cai com ele; o juro de equilíbrio iguala " + vd("S = I") + ". Juro é variável <b>real</b>.",
            "<b>" + oc("Keynes") + "</b>, na " + oc("Teoria Geral") + " (" + vd("1936") + "): o juro é o "
            + azb("prêmio por renunciar à liquidez") + " — o custo de oportunidade de reter moeda. Ele se forma "
            "no mercado monetário, no cruzamento da " + azb("preferência pela liquidez") + " (L) com a oferta de "
            "moeda (Mˢ), fixada pela autoridade monetária.",
            "E a igualdade S = I? Em Keynes ela continua valendo, mas é ajustada pela <b>renda</b> (via "
            "multiplicador), não pelo juro. A poupança depende da renda; o investimento depende do juro e da "
            + azb("eficiência marginal do capital") + ".",
            "Consequência de política: para os clássicos, poupar mais baixa o juro e estimula o investimento; "
            "para Keynes, poupar mais pode reduzir a renda (" + azb("paradoxo da parcimônia") + ") sem baixar o "
            "juro.",
            "A síntese neoclássica (" + oc("Hicks") + ", IS-LM) junta as duas pontas: IS (mercado de bens, S = I) e "
            "LM (mercado monetário, L = Mˢ) determinam juntos juro e renda.",
        ],
        "grafico_verso": "ECO-E2-L01008-1-V1",
        "dissecando": (cz("[troca de ator · troca de conceito]") + " Atribui a Keynes a teoria que ele criticou. "
                       "Pista: “preço que iguala poupança e investimento” é a assinatura dos fundos emprestáveis; "
                       "em Keynes, a palavra-chave é “liquidez”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na teoria clássica, a taxa de juros é o preço que iguala poupança e investimento.”</i> → CERTO",
            "<i>“Para Keynes, a taxa de juros é a recompensa pela abstinência do consumo presente.”</i> → ERRADO "
            "(troca de ator: é a visão clássica; em Keynes, recompensa pela renúncia à liquidez)",
        ])],
        "reescrita": ("Na teoria keynesiana, taxa de juros é o preço que iguala " + hl("a oferta e a demanda de "
                      "moeda (preferência pela liquidez)") + "."),
        "tipo_erro": ["TROCA_ATOR", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Fundos emprestáveis: juro é prêmio de espera, iguala poupança e investimento. "
                             "Keynes: juro é custo de reter moeda, determinado pela preferência pela liquidez e "
                             "pela oferta de moeda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01269
    {
        "id": "ECO-E2-L01269-1", "fonte_ref": "E2-L01269", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_TPM,
        "rotulo_item": "Item",
        "assertiva": ("Se a parcela dos meios de pagamentos que os agentes mantêm como depósitos à vista aumentar e "
                      "se a proporção de reservas bancárias em relação ao depósito à vista diminuir, então o "
                      "multiplicador da base monetária aumentará."),
        "gabarito": "CERTO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("Se a parcela dos meios de pagamentos que os agentes mantêm como <u>depósitos à vista "
                      "aumentar</u> e se a proporção de <u>reservas bancárias</u> em relação ao depósito à vista "
                      "<u>diminuir</u>, então o multiplicador da base monetária aumentará."),
        "poucas": ("Mais depósitos e menos reservas = menos " + azb("vazamentos") + " no circuito de crédito. "
                   "Os dois efeitos elevam o " + azb("multiplicador") + "."),
        "destrinchando": [
            "Pense no multiplicador como uma corrente de rodadas: cada real de base vira depósito, o banco "
            "empresta a parte que não fica em reserva, o empréstimo volta como depósito… Cada rodada perde dois "
            "“vazamentos”: o papel-moeda que o público retém e a reserva que o banco guarda.",
            FORM_MULT,
            "Mais depósitos à vista na composição de M1 = menos papel-moeda retido (c ↓ ou d ↑). Menos reservas "
            "por depósito = r ↓ (ou R ↓). Ambos reduzem vazamentos: " + vm("m sobe") + ".",
            "Conta com a forma (1 + c)/(c + r): c = " + vd("0,5") + " e r = " + vd("0,2") + " → m = 1,5/0,7 ≈ "
            + vd("2,1") + ". Com c = " + vd("0,3") + " e r = " + vd("0,1") + " → m = 1,3/0,4 = " + vd("3,25")
            + ".",
            "Na prática, o BC age sobre r pelo " + azb("compulsório") + "; o público age sobre c conforme a "
            "confiança nos bancos, a inflação e a difusão de meios eletrônicos.",
        ],
        "dissecando": (cz("[literalidade]") + " Combina dois choques no mesmo sentido, o que torna o item "
                       "seguro. O risco está em ler “reservas diminuir” como algo contracionista; reserva menor é "
                       "<b>mais</b> crédito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o público aumentar a parcela de M1 mantida em papel-moeda e os bancos reduzirem as reservas, "
            "o multiplicador necessariamente aumentará.”</i> → ERRADO (efeitos opostos: resultado "
            "indeterminado)",
            "<i>“A redução da alíquota do compulsório, mantido o comportamento do público, eleva o multiplicador "
            "da base monetária.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Verso sem gabarito explícito; só a descrição de um slide sobre o multiplicador "
                             "(M1/B, dependente da retenção de papel-moeda e das reservas)."),
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 223", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00952-1 (mesma assertiva, Pré-TPS/2024, gabarito CERTO)",
                    "nota_redacao: verso sem gabarito; resolvido CERTO pela regra do multiplicador"],
    },
    # ------------------------------------------------------------------ E2-L01271
    {
        "id": "ECO-E2-L01271-1", "fonte_ref": "E2-L01271", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_TPM,
        "rotulo_item": "Item",
        "assertiva": ("Há criação de meios de pagamento quando um banco comercial adquire um bem pertencente a uma "
                      "empresa não financeira, pagando em moeda corrente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Há criação de meios de pagamento quando um <u>banco comercial</u> adquire um <u>bem</u> "
                      "pertencente a uma empresa não financeira, pagando em moeda corrente."),
        "poucas": ("O banco (setor bancário) entrega " + azb("haver monetário") + " (papel-moeda que estava no "
                   "seu caixa) e recebe um " + azb("haver não monetário") + " (o bem) do público: M1 aumenta."),
        "destrinchando": [
            vm("Regra-âncora: cria moeda a troca em que o setor bancário entrega haver monetário ao público e "
               "recebe haver não monetário; destrói moeda o caminho inverso."),
            "No item, o papel-moeda sai do " + azb("caixa do banco") + " (que não é M1, porque o encaixe dos "
            "bancos não está em poder do público) e vai para a empresa, virando " + azb("PMPP") + ": M1 sobe "
            "pelo valor do bem.",
            "O mesmo vale se o banco pagasse creditando a conta da empresa (DV ↑) ou comprasse títulos, imóveis "
            "ou dólares do público. Empréstimo é o caso mais comum: o banco recebe uma promessa de pagamento "
            "(não monetária) e entrega depósito à vista.",
            "Contraste: quando o próprio banco <b>vende</b> um bem ao público e recebe em moeda, há destruição; "
            "quando dois agentes do público negociam entre si, nada acontece com M1.",
            "Na base monetária, a compra paga com papel-moeda do caixa não muda B (encaixe ↓, PMPP ↑); o que "
            "cresce é M1, porque parte da base migrou dos bancos para o público.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Parece estranho que comprar um bem “crie "
                       "dinheiro”, mas é a definição contábil. Pista: um dos lados é banco e o outro é público, e o "
                       "banco recebe algo que não é moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Há criação de meios de pagamento quando uma empresa não financeira adquire um bem de outra "
            "empresa não financeira, pagando em moeda corrente.”</i> → ERRADO (troca de ator: as duas partes são "
            "do público)",
            "<i>“Há destruição de meios de pagamento quando um banco comercial vende um imóvel a uma família, "
            "recebendo à vista.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Troca de ativo monetário por não monetário entre agente do sistema bancário e do "
                             "público; aquisição do bem aumenta os ativos do sistema monetário → criação de "
                             "moeda."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01298
    {
        "id": "ECO-E2-L01298-1", "fonte_ref": "E2-L01298", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MSM,
        "rotulo_item": "Item",
        "assertiva": ("A base monetária consiste na soma do papel moeda emitido com os encaixes (reservas) totais "
                      "dos bancos comerciais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A base monetária consiste na soma do ") + vm("papel moeda emitido") + az(" com os encaixes "
                       "(reservas) totais dos bancos comerciais.")),
        "poucas": ("O papel-moeda emitido já inclui o dinheiro no caixa dos bancos; somá-lo aos " + azb("encaixes "
                   "totais") + " conta esse caixa duas vezes. Com encaixes totais, a parcela certa é o "
                   + azb("papel-moeda em poder do público") + "."),
        "destrinchando": [
            "Decomposição do " + azb("papel-moeda emitido") + " (PME): " + vd("PME = PMPP + caixa dos bancos "
                                                                               "comerciais") + ".",
            "Os " + azb("encaixes totais") + " dos bancos = " + vd("caixa em moeda corrente + reservas bancárias "
                                                                    "no BC") + " (voluntárias e compulsórias).",
            "Daí as duas fórmulas equivalentes da base: " + vd("B = PME + reservas bancárias no BC") + " ou "
            + vd("B = PMPP + encaixes totais") + ". Em ambas, o caixa dos bancos aparece uma só vez.",
            "A fórmula do item (PME + encaixes totais) = PMPP + " + vm("2 × caixa") + " + reservas no BC: dupla "
            "contagem.",
            "A base é o " + azb("passivo monetário do Banco Central") + " — a “moeda de alto poder”, sobre a qual "
            "o multiplicador opera para gerar M1.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mistura as duas fórmulas corretas: pega o PME de uma e os "
                       "encaixes totais da outra. Pista: confira sempre se a soma conta o caixa dos bancos uma única "
                       "vez."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A base monetária consiste na soma do papel-moeda emitido com as reservas bancárias depositadas "
            "no Banco Central.”</i> → CERTO",
            "<i>“A base monetária consiste na soma do papel-moeda em poder do público com os depósitos à vista.”</i> "
            "→ ERRADO (troca de conceito: isso é M1)",
        ])],
        "reescrita": ("A base monetária consiste na soma do " + hl("papel-moeda em poder do público") + " com os "
                      "encaixes (reservas) totais dos bancos comerciais."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("B = PME + reservas bancárias (no BC) = PMPP + encaixes totais dos bancos "
                             "comerciais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 229", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 230", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01299
    {
        "id": "ECO-E2-L01299-1", "fonte_ref": "E2-L01299", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MSM,
        "rotulo_item": "Item",
        "assertiva": ("Aos haveres plenamente líquidos – isto é, que estão imediatamente disponíveis para liquidar "
                      "dívidas – possuídos pelo público não-bancário dá-se o nome de base monetária. Este agregado é "
                      "dado pela soma do papel moeda em poder do público com os depósitos à vista dos bancos "
                      "comerciais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Aos haveres plenamente líquidos – isto é, que estão imediatamente disponíveis para liquidar "
                       "dívidas – possuídos pelo público não-bancário dá-se o nome de ") + vm("base monetária")
                    + az(". Este agregado é dado pela soma do papel moeda em poder do público com os depósitos à "
                         "vista dos bancos comerciais.")),
        "poucas": ("Definição e fórmula estão corretas — mas são de " + azb("meios de pagamento (M1)")
                   + ", não de base monetária. A base soma PMPP e " + azb("reservas") + ", não depósitos."),
        "destrinchando": [
            azb("M1") + ": haveres de liquidez plena do " + azb("público não bancário") + " — "
            + vd("PMPP + depósitos à vista") + ". É a moeda que o público usa para pagar.",
            azb("Base monetária") + " (B): passivo monetário do Banco Central — " + vd("PMPP + reservas "
                                                                                      "bancárias") + ". Inclui "
            "dinheiro que <b>não</b> está com o público (encaixes e reservas dos bancos).",
            "As duas compartilham o PMPP; a diferença é a segunda parcela. Depósitos à vista são passivo dos "
            "bancos comerciais; reservas são passivo do BC.",
            "Relação: " + vd("M1 = m · B") + ". Como os depósitos são um múltiplo das reservas, em regra "
            + vm("M1 > B") + ".",
            "Um teste rápido para distinguir: “quem deve esse dinheiro?” Se é o BC, é base; se é o banco "
            "comercial, é depósito (M1 ou agregados mais amplos).",
        ],
        "dissecando": (cz("[troca de conceito]") + " Descreve M1 com perfeição e troca só o nome. Pista: "
                       "“possuídos pelo público não-bancário” e “depósitos à vista” são marcas de M1; a base "
                       "sempre fala em reservas bancárias."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Aos haveres plenamente líquidos possuídos pelo público não bancário dá-se o nome de meios de "
            "pagamento.”</i> → CERTO",
            "<i>“A base monetária corresponde ao passivo monetário do Banco Central.”</i> → CERTO",
        ])],
        "reescrita": ("Aos haveres plenamente líquidos – isto é, que estão imediatamente disponíveis para liquidar "
                      "dívidas – possuídos pelo público não-bancário dá-se o nome de " + hl("meios de pagamento "
                      "(M1)") + ". Este agregado é dado pela soma do papel moeda em poder do público com os "
                      "depósitos à vista dos bancos comerciais."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Trata-se da definição de meios de pagamento (M1), não da base monetária.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01300
    {
        "id": "ECO-E2-L01300-1", "fonte_ref": "E2-L01300", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MSM,
        "rotulo_item": "Item",
        "assertiva": "Os meios de pagamento são um múltiplo da base monetária.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os meios de pagamento são um <u>múltiplo</u> da base monetária."),
        "poucas": ("Por definição, " + vd("M1 = m · B") + "; como os bancos emprestam parte dos depósitos, o "
                   + azb("multiplicador") + " é maior que 1 e M1 supera a base."),
        "destrinchando": [
            "A base monetária (" + vd("B = PMPP + reservas") + ") é a moeda emitida pelo BC. Os bancos, mantendo "
            "só uma fração dos depósitos como reserva, emprestam o resto e geram " + azb("moeda escritural") + ".",
            "Na forma " + vd("m = (1 + c)/(c + r)") + ", m > 1 sempre que r < 1, isto é, sempre que os bancos não "
            "guardem 100% dos depósitos. Com c = " + vd("0,25") + " e r = " + vd("0,2") + ", m ≈ " + vd("2,8")
            + ": cada real de base sustenta R$ 2,80 de M1.",
            "O valor de m não é fixo: cai com mais reservas (compulsório ↑) e com mais papel-moeda retido pelo "
            "público; sobe no sentido contrário.",
            "Por isso o BC controla diretamente a base (via operações de mercado aberto, redesconto, compra de "
            "divisas), mas só indiretamente os meios de pagamento — a ponte é o multiplicador, que depende do "
            "comportamento de bancos e público.",
            "Casos-limite em que m = 1: reservas de 100% ou público que retém tudo em papel-moeda. Fora deles, "
            "M1 é um múltiplo da base, maior que ela.",
        ],
        "dissecando": (cz("[literalidade]") + " Enunciado curto e literal da relação M1 = m · B. O risco é "
                       "achar que “múltiplo” exige m inteiro ou constante; no jargão monetário, quer dizer apenas "
                       "que M1 é a base multiplicada por m > 1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A base monetária é um múltiplo dos meios de pagamento.”</i> → ERRADO (inversão)",
            "<i>“O Banco Central controla diretamente os meios de pagamento, e só indiretamente a base "
            "monetária.”</i> → ERRADO (inversão: controla a base e, via multiplicador, influencia M1)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "M1 = multiplicador × base; com multiplicador maior que 1, M1 é múltiplo da base.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01301
    {
        "id": "ECO-E2-L01301-1", "fonte_ref": "E2-L01301", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MSM,
        "rotulo_item": "Item",
        "assertiva": ("Quanto menor a razão entre as reservas bancárias totais e os depósitos à vista maior será o "
                      "multiplicador bancário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto <u>menor</u> a razão entre as reservas bancárias totais e os depósitos à vista "
                      "<u>maior</u> será o multiplicador bancário."),
        "poucas": ("Reserva é a parte do depósito que o banco " + azb("não empresta") + ". Menos reserva por "
                   "depósito → mais crédito por rodada → " + azb("multiplicador maior") + "."),
        "destrinchando": [
            "Montagem do multiplicador a partir das identidades: " + vd("B = PMPP + R") + " e "
            + vd("M1 = PMPP + DV") + ". Dividindo as duas por DV, com c = PMPP/DV e r = R/DV: "
            + vd("m = M1/B = (c + 1)/(c + r)") + ".",
            "r está só no denominador: r ↓ → denominador ↓ → m ↑. Ex.: c = " + vd("0,25") + "; com r = "
            + vd("0,2") + ", m ≈ " + vd("2,8") + "; com r = " + vd("0,1") + ", m ≈ " + vd("3,6") + ".",
            "r é a soma das reservas " + azb("compulsórias") + " (decididas pelo BC) e " + azb("voluntárias")
            + " (decididas pelos bancos, por precaução). Em crises, os bancos elevam as voluntárias, e o "
            "multiplicador cai mesmo sem mudança do compulsório.",
            vm("Regra-âncora: r e c no denominador — qualquer aumento deles reduz m."),
        ],
        "dissecando": (cz("[literalidade]") + " Regra direta do multiplicador, na formulação “quanto menor…, "
                       "maior…”. O risco é a inversão de leitura: confira o par de sinais (menor reserva ↔ maior "
                       "multiplicador)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a razão entre reservas bancárias e depósitos à vista, maior será o multiplicador "
            "bancário.”</i> → ERRADO (inversão)",
            "<i>“O aumento das reservas voluntárias dos bancos, mantido o compulsório, reduz o multiplicador.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["quanto menor", "maior"], "dificuldade": 1,
        "comentario_fonte": ("Menor taxa de reservas → bancos emprestam mais → maior multiplicador; slide com "
                             "PMPP + ETbc = B e PMPP + DV = M1."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 231", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01639
    {
        "id": "ECO-E2-L01639-1", "fonte_ref": "E2-L01639", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BC,
        "rotulo_item": "Item",
        "assertiva": ("Diante de uma crise de desconfiança com relação ao sistema bancário, o aumento do papel moeda "
                      "em poder do público relativamente aos depósitos bancários tende a contrair os meios de "
                      "pagamento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Diante de uma crise de desconfiança com relação ao sistema bancário, o aumento do papel moeda "
                      "em poder do público relativamente aos depósitos bancários <u>tende a contrair</u> os meios de "
                      "pagamento."),
        "poucas": ("Com mais papel-moeda retido (c ↑), o " + azb("multiplicador") + " cai; para uma mesma base, "
                   + vd("M1 = m · B") + " se contrai — mesmo que o PMPP, sozinho, aumente."),
        "destrinchando": [
            "Na corrida bancária, o público saca depósitos e guarda papel-moeda: c = PMPP/DV sobe. Na fórmula "
            + vd("m = (1 + c)/(c + r)") + ", c aumenta mais o denominador (proporcionalmente) do que o "
            "numerador, e m cai.",
            "Mecânica: cada real sacado sai do caixa do banco; para manter a razão de reservas, o banco precisa "
            "<b>encolher</b> empréstimos, o que destrói depósitos em várias rodadas. O ganho de PMPP é menor que a "
            "perda de DV.",
            "Agravante: em crises, os próprios bancos elevam as " + azb("reservas voluntárias") + " (r ↑), "
            "reforçando a queda de m.",
            "Episódio clássico: a " + azb("Grande Depressão") + " nos EUA (" + vd("1930–1933") + "). "
            + oc("Friedman e Schwartz") + ", em <i>A Monetary History of the United States</i> (" + vd("1963")
            + "), atribuem à onda de falências bancárias a forte contração da oferta de moeda e a deflação "
            "do período.",
            "Remédio típico: o BC atua como " + azb("emprestador de última instância") + " e expande a base para "
            "compensar a queda do multiplicador.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O item parece paradoxal (mais papel-moeda "
                       "contrai a moeda?) porque o PMPP é parte de M1. O “tende a” protege a afirmação, e a "
                       "chave é o efeito sobre o multiplicador, não sobre o componente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Numa crise bancária, o aumento do papel-moeda em poder do público eleva os meios de pagamento, "
            "pois o PMPP integra o M1.”</i> → ERRADO (meia-verdade: o PMPP integra o M1, mas o multiplicador "
            "cai)",
            "<i>“Numa corrida bancária, a base monetária constante é compatível com queda dos meios de "
            "pagamento.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": ("Crise de confiança: c ↑ reduz o multiplicador m = (1 + c)/(c + r) e contrai M1 para "
                             "uma mesma base; exemplo da Grande Depressão."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01700
    {
        "id": "ECO-E2-L01700-1", "fonte_ref": "E2-L01700", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BASE,
        "rotulo_item": "Item",
        "assertiva": ("Empréstimos do Banco Central aos bancos comerciais determinam aumento de igual montante nos "
                      "meios de pagamento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Empréstimos do Banco Central aos bancos comerciais determinam aumento ")
                    + vm("de igual montante") + az(" nos meios de pagamento.")),
        "poucas": ("O empréstimo do BC aumenta, no mesmo valor, a " + azb("base monetária") + " (reservas); o "
                   "efeito sobre M1 passa pelo " + azb("multiplicador") + " e tende a ser " + vm("maior")
                   + " que o empréstimo."),
        "destrinchando": [
            "Contabilidade do " + azb("redesconto") + ": o BC credita a conta de reservas do banco. No balanço do "
            "BC, sobe o ativo (crédito a bancos) e o passivo monetário (reservas): " + vd("ΔB = empréstimo") + ".",
            "Efeito imediato sobre M1: " + vd("nenhum") + " — reservas bancárias não são moeda em poder do "
            "público. M1 só cresce quando o banco usa as reservas para emprestar ao público, gerando depósitos.",
            "Efeito final: " + vd("ΔM1 = m · ΔB") + ". Com m = " + vd("2,5") + ", um redesconto de " + vd("100")
            + " pode elevar M1 em até " + vd("250") + ".",
            "Só haveria aumento de igual montante no caso-limite m = 1 (reservas de 100% ou público que retém "
            "tudo em papel-moeda); e, se os bancos apenas guardarem as novas reservas, o aumento de M1 pode ser "
            "até nulo.",
            "Outras fontes de criação de base: compra de títulos no mercado aberto, compra de divisas, "
            "financiamento ao Tesouro (vedado no Brasil pela LRF e pela Constituição). Em todas, o efeito sobre "
            "M1 é mediado pelo multiplicador.",
        ],
        "dissecando": (cz("[troca de conceito · dado alterado]") + " Confunde o impacto sobre a base (igual ao "
                       "empréstimo) com o impacto sobre M1 (multiplicado). A pista é o verbo “determinam” com "
                       "“igual montante”: entre o BC e os meios de pagamento sempre há o multiplicador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Empréstimos do Banco Central aos bancos comerciais aumentam a base monetária em igual "
            "montante.”</i> → CERTO",
            "<i>“O pagamento de um empréstimo de redesconto pelos bancos comerciais expande a base "
            "monetária.”</i> → ERRADO (inversão: contrai)",
        ])],
        "reescrita": ("Empréstimos do Banco Central aos bancos comerciais determinam aumento " + hl("multiplicado (via "
                      "multiplicador bancário)") + " nos meios de pagamento."),
        "tipo_erro": ["TROCA_CONCEITO", "DADO_ALTERADO"], "moduladores": ["igual montante"], "dificuldade": 2,
        "comentario_fonte": ("Redesconto aumenta reservas e a base; via multiplicador, M1 aumenta em montante "
                             "tipicamente maior que o empréstimo (ex.: m = 2,5 → 250 para 100)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 503", "tipo_fonte": "DIAGRAMA", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01701
    {
        "id": "ECO-E2-L01701-1", "fonte_ref": "E2-L01701", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BASE,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central cria moeda quando, tomando empréstimos externos, aumenta as suas reservas "
                      "internacionais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Banco Central ") + vm("cria moeda") + az(" quando, tomando empréstimos externos, aumenta "
                                                                    "as suas reservas internacionais.")),
        "poucas": ("Quando o BC toma empréstimo externo, o aumento das reservas (ativo) tem como contrapartida uma "
                   + azb("dívida externa") + " (passivo " + vm("não monetário") + "): a base monetária não "
                   "muda."),
        "destrinchando": [
            "O BC cria base monetária quando adquire um ativo e paga com " + azb("passivo monetário") + " "
            "(papel-moeda ou reservas bancárias). O que decide não é o ativo que sobe, mas o passivo que o "
            "financia.",
            "Compra de divisas de um exportador ou de um banco no mercado interno: ativo (reservas "
            "internacionais) ↑ e passivo monetário (reais creditados) ↑ → " + vm("cria base") + ".",
            "Empréstimo externo tomado pelo próprio BC: ativo (reservas) ↑ e passivo externo ↑. Nenhum real é "
            "entregue ao público ou aos bancos → " + vd("ΔB = 0") + ".",
            "Exemplo brasileiro: os saques nos " + rx("acordos com o FMI") + " (fim dos anos 1990 e início dos "
            "2000) reforçaram as reservas do BC sem emissão de moeda, porque a contrapartida era dívida com o "
            "Fundo.",
            "Contraste útil: se o BC compra dólares e depois vende títulos para retirar os reais emitidos "
            "(" + azb("esterilização") + "), a base volta ao nível inicial, e o custo aparece na dívida "
            "pública.",
        ],
        "dissecando": (cz("[nexo indevido]") + " Liga corretamente “reservas ↑” ao balanço do BC, mas infere "
                       "criação de moeda sem passivo monetário em contrapartida. Pista: pergunte sempre “com o "
                       "quê o BC pagou?” — se não foi com reais, não há criação de moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Banco Central cria moeda quando compra divisas de exportadores, aumentando suas reservas "
            "internacionais.”</i> → CERTO",
            "<i>“Toda elevação das reservas internacionais do Banco Central expande a base monetária.”</i> → "
            "ERRADO (modulador absoluto: depende da contrapartida)",
        ])],
        "reescrita": ("O Banco Central " + hl("não cria moeda") + " quando, tomando empréstimos externos, aumenta "
                      "as suas reservas internacionais" + hl(", pois a contrapartida é um passivo externo, e não "
                                                              "monetário") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("BC cria base quando compra ativos pagando com moeda nacional; empréstimo externo "
                             "aumenta reservas e passivo externo, sem expansão da base. Uma das respostas afirmava "
                             "que o BC não toma empréstimos externos — incorreto."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01703
    {
        "id": "ECO-E2-L01703-1", "fonte_ref": "E2-L01703", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BASE,
        "rotulo_item": "Item",
        "assertiva": ("Quanto maior for o coeficiente de reservas dos bancos comerciais e menor for a preferência do "
                      "público por papel moeda (proporção da moeda em poder do público em relação aos meios de "
                      "pagamento), maior será o multiplicador da base monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quanto ") + vm("maior") + az(" for o coeficiente de reservas dos bancos comerciais e menor "
                       "for a preferência do público por papel moeda (proporção da moeda em poder do público em "
                       "relação aos meios de pagamento), maior será o multiplicador da base monetária.")),
        "poucas": ("Metade certa, metade errada: menor preferência por papel-moeda eleva o multiplicador, mas "
                   + azb("maior coeficiente de reservas") + " o " + vm("reduz") + "."),
        "destrinchando": [
            FORM_MULT,
            "Os dois parâmetros são " + azb("vazamentos") + ": reservas (o banco não empresta) e papel-moeda "
            "retido (não volta ao banco). Vazamento maior → multiplicador menor.",
            "Logo: reservas ↑ → m ↓; preferência por papel-moeda ↓ → m ↑. O item combina um efeito contrário e "
            "outro favorável e afirma o resultado favorável como certo.",
            "Quando os choques têm sinais opostos, o efeito líquido é indeterminado sem números. Ex. com c = "
            "PMPP/DV: (c, r) = (" + vd("0,5") + "; " + vd("0,1") + ") → m = " + vd("2,5") + "; (" + vd("0,25")
            + "; " + vd("0,3") + ") → m ≈ " + vd("2,3") + " (caiu, apesar de c menor).",
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 2ª condição está certa e dá credibilidade ao item; o "
                       "erro está no sentido do coeficiente de reservas. Em frases com duas condições, avalie "
                       "cada uma separadamente — basta uma errada para o item ser ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto menor o coeficiente de reservas e menor a preferência do público por papel-moeda, maior "
            "será o multiplicador.”</i> → CERTO",
            "<i>“Se o coeficiente de reservas aumentar e a preferência por papel-moeda diminuir, o "
            "multiplicador necessariamente cairá.”</i> → ERRADO (efeitos opostos: resultado indeterminado)",
        ])],
        "reescrita": ("Quanto " + hl("menor") + " for o coeficiente de reservas dos bancos comerciais e menor for a "
                      "preferência do público por papel moeda (proporção da moeda em poder do público em relação "
                      "aos meios de pagamento), maior será o multiplicador da base monetária."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["quanto maior", "maior será"],
        "dificuldade": 1,
        "comentario_fonte": ("m = (1 + c)/(c + r); maior coeficiente de reservas reduz o multiplicador; maior c "
                             "também reduz."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 505", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01747
    {
        "id": "ECO-E2-L01747-1", "fonte_ref": "E2-L01747", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_OFM,
        "rotulo_item": "Item",
        "assertiva": ("Numa crise de confiança no sistema bancário, em que ocorre um aumento da preferência do "
                      "público por papel moeda em relação aos depósitos à vista, ocorre um aumento do multiplicador "
                      "bancário e dos meios de pagamento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Numa crise de confiança no sistema bancário, em que ocorre um aumento da preferência do "
                       "público por papel moeda em relação aos depósitos à vista, ocorre ") + vm("um aumento")
                    + az(" do multiplicador bancário e dos meios de pagamento.")),
        "poucas": ("Na corrida bancária, c = PMPP/DV sobe e o " + azb("multiplicador cai") + "; com a base "
                   "constante, os " + azb("meios de pagamento") + " também caem. É " + vm("contração") + ", não "
                   "expansão."),
        "destrinchando": [
            "Fórmula: " + vd("m = (1 + c)/(r + c)") + ". Como r < 1, um aumento de c sobe mais o denominador do "
            "que o numerador em termos relativos, e m diminui. Ex.: r = " + vd("0,2") + "; c de " + vd("0,25")
            + " para " + vd("0,5") + " → m de " + vd("2,8") + " para " + vd("2,1") + ".",
            "Mecanismo: o depósito sacado sai do caixa do banco; para respeitar a razão de reservas, o banco "
            "corta empréstimos, e os depósitos se reduzem em cadeia. O PMPP sobe, mas DV cai mais — M1 encolhe.",
            "Os bancos reforçam o efeito: com medo de saques, elevam as reservas voluntárias (r ↑), reduzindo m "
            "ainda mais.",
            "É a contração monetária típica das crises bancárias — o caso de manual é a " + azb("Grande "
            "Depressão") + " nos EUA, em que " + oc("Friedman e Schwartz") + " apontam o colapso do "
            "multiplicador como motor da queda da oferta de moeda.",
        ],
        "dissecando": (cz("[inversão]") + " Descreve corretamente a causa (preferência por papel-moeda ↑) e "
                       "inverte o efeito. O apelo enganoso é que “mais papel-moeda” parece “mais moeda”; o que "
                       "conta é o multiplicador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Numa crise de confiança bancária, o aumento da preferência por papel-moeda tende a contrair os "
            "meios de pagamento.”</i> → CERTO",
            "<i>“Numa crise de confiança bancária, a base monetária necessariamente se contrai.”</i> → ERRADO "
            "(modulador absoluto: a base pode ficar constante; cai o multiplicador)",
        ])],
        "reescrita": ("Numa crise de confiança no sistema bancário, em que ocorre um aumento da preferência do "
                      "público por papel moeda em relação aos depósitos à vista, ocorre " + hl("uma redução")
                      + " do multiplicador bancário e dos meios de pagamento."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Preferência por papel-moeda ↑ → m = (1 + c)/(r + c) ↓ → M1 ↓. O verso trazia ainda "
                             "um comentário alheio (gabarito “Certo” sobre compra de dólares e esterilização), "
                             "descartado."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: verso continha comentário de outro item (esterilização, gabarito Certo), "
                    "descartado; gabarito ERRADO mantido"],
    },
    # ------------------------------------------------------------------ E3-L00022
    {
        "id": "ECO-E3-L00022-1", "fonte_ref": "E3-L00022", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_1,
        "rotulo_item": "Item",
        "assertiva": ("O aumento do PIB real eleva a demanda por moeda para transações; se os bancos estiverem "
                      "dispostos a reduzir sua preferência por liquidez, essa maior demanda será atendida por meio da "
                      "expansão do crédito, o que pressiona o crescimento do M1."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento do PIB real eleva a demanda por moeda para transações; <u>se os bancos estiverem "
                      "dispostos</u> a reduzir sua preferência por liquidez, essa maior demanda será atendida por "
                      "meio da expansão do crédito, o que <u>pressiona</u> o crescimento do M1."),
        "poucas": ("Com juros fixados pelo BC, a moeda se ajusta à demanda: a renda maior pede mais moeda para "
                   + azb("transações") + ", e bancos dispostos a emprestar criam os " + azb("depósitos à vista")
                   + " que expandem o M1."),
        "destrinchando": [
            "Expansão fiscal → PIB real ↑ → demanda por moeda pelo " + azb("motivo transação") + " ↑ (L₁ depende "
            "da renda). Sem acomodação, isso elevaria os juros (LM positivamente inclinada).",
            "Mas o enunciado fixa o juro: o BC opera com " + azb("meta de taxa de juros") + " e, para impedir "
            "a alta, fornece as reservas que o sistema pedir. A oferta de moeda torna-se " + azb("endógena")
            + " — na IS-LM, a LM fica horizontal no juro-meta.",
            "A ponte até o M1 são os bancos: se aceitam ficar menos líquidos (reduzir reservas voluntárias, "
            "aplicar menos em títulos), ampliam o crédito, e cada empréstimo cria " + azb("depósito à vista")
            + " — componente de " + vd("M1 = PMPP + DV") + ".",
            "A ideia de que o crédito puxa os depósitos (e não o contrário) é cara aos " + oc("pós-keynesianos")
            + " (" + oc("Kaldor") + ", " + oc("Basil Moore") + "): “os empréstimos criam depósitos”, e o BC "
            "acomoda via reservas.",
            "As condicionais protegem o item: “se os bancos estiverem dispostos” e “pressiona” não afirmam "
            "aumento automático nem de valor definido.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Encadeia três elos verdadeiros (renda → "
                       "demanda transacional; bancos menos líquidos → crédito; crédito → depósitos/M1) sob uma "
                       "condição. Itens assim só caem se algum elo for absoluto ou invertido — aqui nenhum é."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento do PIB real reduz a demanda por moeda para transações.”</i> → ERRADO (inversão)",
            "<i>“Com juros constantes, o aumento da demanda por moeda é necessariamente atendido pela emissão de "
            "papel-moeda, sem participação dos bancos.”</i> → ERRADO (restrição indevida: a expansão se dá "
            "sobretudo via crédito e depósitos)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["se", "pressiona"],
        "dificuldade": 2,
        "comentario_fonte": ("Seis respostas concordantes: PIB ↑ → demanda transacional ↑; BC acomoda para manter "
                             "juros; bancos com menor preferência pela liquidez expandem crédito e depósitos à "
                             "vista → M1 ↑."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00023
    {
        "id": "ECO-E3-L00023-1", "fonte_ref": "E3-L00023", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_1,
        "rotulo_item": "Item",
        "assertiva": ("O impacto da política fiscal sobre os meios de pagamento é ampliado quando os bancos reduzem "
                      "sua retenção de liquidez e ampliam os depósitos à vista."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O impacto da política fiscal sobre os meios de pagamento é <u>ampliado</u> quando os bancos "
                      "<u>reduzem sua retenção de liquidez</u> e ampliam os depósitos à vista."),
        "poucas": ("Menos liquidez retida pelos bancos = menor taxa de " + azb("reservas") + " = "
                   + azb("multiplicador maior") + ": o mesmo impulso inicial vira mais depósitos à "
                   "vista e mais M1."),
        "destrinchando": [
            "Retenção de liquidez pelos bancos = " + azb("reservas voluntárias") + " (e aplicações muito "
            "líquidas no lugar de crédito). Ela entra no coeficiente r do multiplicador "
            + vd("m = (1 + c)/(c + r)") + ".",
            "r ↓ → m ↑. Ex.: c = " + vd("0,25") + "; r de " + vd("0,2") + " para " + vd("0,1") + " → m de "
            + vd("2,8") + " para " + vd("3,6") + ".",
            "Na cadeia do enunciado, a expansão fiscal eleva renda e demanda por moeda; o BC, para manter o "
            "juro, supre reservas (ΔB). O efeito sobre M1 é " + vd("ΔM1 = m · ΔB") + ": com m maior, o mesmo "
            "impulso gera expansão maior dos meios de pagamento.",
            "“Ampliam os depósitos à vista” é a consequência do crédito maior: cada empréstimo é creditado como "
            "depósito, componente do M1.",
            "Ao contrário, bancos que entesouram liquidez (como nas crises) amortecem o impacto da política "
            "sobre a moeda — é a versão bancária da " + azb("preferência pela liquidez") + ".",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Reescreve a regra “r ↓ → m ↑” em vocabulário de "
                       "comportamento bancário (“retenção de liquidez”). Traduza o jargão para o parâmetro da "
                       "fórmula e o item se resolve."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O impacto da política fiscal sobre os meios de pagamento é ampliado quando os bancos elevam suas "
            "reservas voluntárias.”</i> → ERRADO (inversão)",
            "<i>“O impacto sobre os meios de pagamento é reduzido quando o público passa a reter mais "
            "papel-moeda.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Seis respostas concordantes: menor retenção de liquidez → multiplicador maior → "
                             "efeito ampliado sobre depósitos à vista e M1."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00024
    {
        "id": "ECO-E3-L00024-1", "fonte_ref": "E3-L00024", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_1,
        "rotulo_item": "Item",
        "assertiva": "A política fiscal expansionista aumenta automaticamente o M1.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A política fiscal expansionista ") + vm("aumenta automaticamente") + az(" o M1.")),
        "poucas": ("Gasto público não cria moeda por si só: o efeito sobre M1 depende do " + azb("financiamento")
                   + " do déficit, da reação do " + azb("Banco Central") + " e do comportamento dos bancos e do "
                   "público. Nada é automático."),
        "destrinchando": [
            "Gasto financiado por <b>tributos</b>: o governo tira depósitos de uns e os devolve a outros — "
            "transferência dentro do público, M1 inalterado.",
            "Gasto financiado por <b>títulos vendidos ao público</b>: o público troca moeda por título, o governo "
            "devolve a moeda ao gastar. Sem criação líquida; pode subir o juro e haver " + azb("crowding out")
            + ".",
            "Gasto financiado por <b>emissão</b> (BC comprando títulos do Tesouro): aí sim a base cresce — mas a "
            "operação é monetária, não fiscal, e no Brasil o financiamento direto do Tesouro pelo BC é "
            + rx("vedado") + " (" + vd("art. 164, §1º, CF") + ").",
            "No cenário do comando (juros constantes), o M1 tende a crescer porque o BC " + azb("acomoda")
            + " a maior demanda por moeda e os bancos expandem crédito. O aumento decorre da <b>combinação</b> "
            "fiscal + monetária + bancária, e o item, ao dizer “automaticamente”, apaga essas condições.",
            vm("Regra-âncora: política fiscal mexe na demanda por moeda; quem mexe na oferta é o BC (base) e o "
               "sistema bancário (multiplicador)."),
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " O “automaticamente” transforma um efeito "
                       "condicional em mecânico. 🔥 CEBRASPE costuma pôr no mesmo bloco itens CERTO com "
                       "condicionais (“se os bancos…”, “pressiona”) e um ERRADO com absoluto — o contraste é a "
                       "pista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com o Banco Central mantendo o juro constante, a política fiscal expansionista tende a elevar o "
            "M1.”</i> → CERTO",
            "<i>“Financiado por venda de títulos ao público, o déficit eleva o M1 no mesmo montante do gasto.”</i> → "
            "ERRADO (nexo indevido: não há criação líquida de moeda)",
        ])],
        "reescrita": ("A política fiscal expansionista " + hl("pode aumentar") + " o M1" + hl(", mas não "
                      "automaticamente: depende da acomodação do Banco Central e do comportamento dos bancos")
                      + "."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["automaticamente"], "dificuldade": 2,
        "comentario_fonte": ("Seis respostas concordantes: o efeito sobre M1 depende do financiamento do déficit, "
                             "da reação do BC (acomodação × esterilização) e dos bancos; não é automático."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00025
    {
        "id": "ECO-E3-L00025-1", "fonte_ref": "E3-L00025", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA_2,
        "rotulo_item": "Item",
        "assertiva": ("Se o público decide substituir parte dos depósitos à vista por papel-moeda e a base monetária "
                      "se mantenha constante, o multiplicador monetário será reduzido."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o público decide <u>substituir parte dos depósitos à vista por papel-moeda</u> e a base "
                      "monetária se mantenha constante, o multiplicador monetário <u>será reduzido</u>."),
        "poucas": ("Trocar depósito por papel-moeda eleva c = PMPP/DV; papel-moeda fora do banco não alimenta "
                   "crédito, então o " + azb("multiplicador cai") + " — e, com base constante, o M1 também."),
        "destrinchando": [
            "Fórmula: " + vd("m = (1 + c)/(c + r)") + ". dm/dc = (r − 1)/(c + r)², negativo sempre que "
            + vd("r < 1") + ": c ↑ → m ↓.",
            "Ex.: r = " + vd("0,2") + ". c = " + vd("0,25") + " → m ≈ " + vd("2,8") + "; c = " + vd("0,5")
            + " → m ≈ " + vd("2,1") + ". Com B = " + vd("100") + ", M1 cai de ≈ 280 para ≈ 210.",
            "Intuição: cada real sacado deixa de ser reserva e passa a circular como moeda manual. O banco, com "
            "menos reservas, corta crédito, e depósitos somem em cadeia. O PMPP sobe, mas DV cai mais.",
            "Por que a base não muda: o saque converte caixa do banco em PMPP — as duas parcelas estão em "
            + vd("B = PMPP + reservas") + ". Muda a composição da base, não seu total.",
            "Primeiro efeito × efeito final: o saque, em si, não altera M1 (DV ↓, PMPP ↑). A contração vem "
            "<b>depois</b>, pela queda do multiplicador sobre a mesma base.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Aplicação direta de c ↑ → m ↓. Engana quem "
                       "pensa “o saque não muda M1” — verdadeiro para o impacto imediato, mas o item pergunta pelo "
                       "<b>multiplicador</b>, que cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A conversão de depósitos à vista em papel-moeda, por si só, reduz imediatamente o M1.”</i> → "
            "ERRADO (troca de conceito: o impacto imediato só muda a composição)",
            "<i>“Se o público substituir papel-moeda por depósitos à vista, mantida a base, o M1 tende a "
            "crescer.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Seis respostas concordantes: c ↑ reduz m = (1 + c)/(c + r); com base constante, M1 = "
                             "m · B diminui."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00026
    {
        "id": "ECO-E3-L00026-1", "fonte_ref": "E3-L00026", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_2,
        "rotulo_item": "Item",
        "assertiva": ("O aumento da alíquota de depósito compulsório sobre depósitos à vista, mantidas constantes a "
                      "base monetária e a demanda por moeda, tende a provocar contração no M1."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento da alíquota de depósito compulsório sobre depósitos à vista, <u>mantidas "
                      "constantes a base monetária</u> e a demanda por moeda, <u>tende a provocar contração</u> no "
                      "M1."),
        "poucas": ("Compulsório maior eleva r, reduz o " + azb("multiplicador") + " e, com a base fixa, contrai "
                   + vd("M1 = m · B") + "."),
        "destrinchando": [
            "O " + azb("recolhimento compulsório") + " é a fração dos depósitos que os bancos são obrigados a "
            "manter parada no BC. É um dos três instrumentos clássicos de política monetária, ao lado do "
            + azb("redesconto") + " e das " + azb("operações de mercado aberto") + ".",
            "Elevá-lo aumenta r em " + vd("m = (1 + c)/(c + r)") + ": menos crédito por real depositado, menos "
            "rodadas de criação de depósitos. Ex.: c = " + vd("0,25") + ", r de " + vd("0,1") + " para "
            + vd("0,2") + " → m de ≈ " + vd("3,6") + " para ≈ " + vd("2,8") + ".",
            "O compulsório não altera a base: reservas compulsórias já fazem parte de B. O efeito é todo via "
            "multiplicador — por isso o item fixa a base.",
            "Instrumento potente, mas pouco usado para sintonia fina: muda o custo de toda a intermediação e "
            "afeta bancos de forma desigual. No " + rx("Brasil") + ", o BC o usa sobretudo de forma "
            + azb("macroprudencial") + " (liberou compulsórios em " + vd("2008") + " e em " + vd("2020")
            + " para irrigar a liquidez nas crises).",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Regra direta (r ↑ → m ↓ → M1 ↓), protegida "
                       "por “mantidas constantes” e “tende a”. A cláusula ceteris paribus fecha a porta a "
                       "objeções (o BC compensar com mais base, por exemplo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento do compulsório contrai a base monetária e, por isso, o M1.”</i> → ERRADO (nexo indevido: "
            "a base não muda; cai o multiplicador)",
            "<i>“A redução do compulsório, mantida a base, tende a expandir o M1.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a", "mantidas constantes"],
        "dificuldade": 1,
        "comentario_fonte": ("Seis respostas concordantes: compulsório ↑ → r ↑ → multiplicador ↓ → M1 ↓, com base "
                             "constante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00027
    {
        "id": "ECO-E3-L00027-1", "fonte_ref": "E3-L00027", "destino": "35", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_2,
        "rotulo_item": "Item",
        "assertiva": ("A base monetária será sempre maior que o M1, dado que esta inclui papel-moeda em poder do "
                      "público, reservas bancárias e depósitos a prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A base monetária será ") + vm("sempre maior") + az(" que o M1, dado que esta inclui "
                       "papel-moeda em poder do público, reservas bancárias") + vm(" e depósitos a prazo")
                    + az(".")),
        "poucas": ("Dois erros: a base " + azb("não inclui depósitos a prazo") + " (que estão em M2) e, em regra, é "
                   + azb("menor") + " que o M1, porque os depósitos à vista são um múltiplo das reservas."),
        "destrinchando": [
            vd("B = PMPP + reservas bancárias") + " (passivo monetário do BC). " + vd("M1 = PMPP + depósitos à "
                                                                                    "vista") + " (haveres "
            "plenamente líquidos do público).",
            "As duas partilham o PMPP; a comparação se decide entre reservas e depósitos à vista. Como os bancos "
            "guardam só uma fração dos depósitos (r < 1), " + vd("DV > reservas") + " e, portanto, "
            + vm("M1 > B") + " — o multiplicador é maior que 1.",
            "Só haveria B = M1 no caso-limite de reservas de 100% (ou de público que retém tudo em papel-moeda); "
            "B > M1 exigiria reservas superiores aos próprios depósitos — situação anômala.",
            "Depósitos a prazo (CDB) são passivo dos bancos comerciais, não do BC, e têm liquidez menor: entram "
            "em " + azb("M2") + ", nunca na base nem no M1.",
            "Ordem habitual dos agregados: " + vd("B < M1 < M2 < M3 < M4") + ".",
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O “sempre” inverte a relação usual, e a "
                       "justificativa enxerta um componente (depósitos a prazo) de outro agregado. Itens com "
                       "“dado que” e justificativa errada caem pela justificativa mesmo que a conclusão "
                       "pareça plausível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A base monetária inclui papel-moeda em poder do público e reservas bancárias.”</i> → CERTO",
            "<i>“O M1 tende a superar a base monetária porque os depósitos à vista são um múltiplo das reservas "
            "bancárias.”</i> → CERTO",
        ])],
        "reescrita": ("A base monetária será " + hl("em regra menor") + " que o M1, dado que esta inclui papel-moeda "
                      "em poder do público, reservas bancárias" + hl(", mas não os depósitos à vista, que no M1 "
                                                                     "são um múltiplo das reservas") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("Seis respostas concordantes: base = PMPP + reservas; M1 = PMPP + DV, em geral maior "
                             "que a base; depósitos a prazo integram M2/M3, não a base."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00065
    {
        "id": "ECO-E3-L00065-1", "fonte_ref": "E3-L00065", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Há destruição de meios de pagamento quando um indivíduo realiza um depósito à vista em um "
                      "banco comercial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Há destruição") + az(" de meios de pagamento quando um indivíduo realiza um depósito à vista "
                                             "em um banco comercial.")),
        "poucas": ("O depósito troca " + azb("moeda manual") + " (PMPP) por " + azb("moeda escritural")
                   + " (DV), as duas dentro de M1: muda a composição, " + vm("não o total") + "."),
        "destrinchando": [
            "Quadro de " + oc("Paulani e Braga") + " (<i>A nova contabilidade social</i>): papel-moeda emitido = "
            "moeda emitida com autorização do BC; papel-moeda em poder do público = papel-moeda emitido − caixa "
            "das sociedades depositárias monetárias; " + vd("meios de pagamento = PMPP + depósitos à vista") + ".",
            "Depósito de 100: PMPP " + vd("−100") + " (a cédula vai para o caixa do banco, que não é M1) e DV "
            + vd("+100") + " → " + vd("ΔM1 = 0") + ".",
            "Destruição exige que o público entregue um haver monetário ao setor bancário em troca de um haver "
            "<b>não monetário</b>: quitar empréstimo, comprar título do banco, comprar dólares do BC.",
            "Efeito de segunda ordem: com mais depósitos e mais caixa, o banco pode emprestar mais — o depósito "
            "tende a <b>elevar</b> o multiplicador (c ↓) e, depois, M1. Destruição, nunca.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Chama de destruição o que é mudança de composição. A "
                       "armadilha é contábil: o PMPP de fato cai, e quem olha só para ele vê “moeda sumindo”. "
                       "Pista: o banco recebeu moeda e entregou moeda (depósito) — nada não monetário mudou de "
                       "mãos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Há destruição de meios de pagamento quando um indivíduo quita, em espécie, um empréstimo junto a "
            "um banco comercial.”</i> → CERTO",
            "<i>“O depósito à vista de papel-moeda reduz o papel-moeda em poder do público sem alterar os meios "
            "de pagamento.”</i> → CERTO",
        ])],
        "reescrita": (hl("Não há destruição nem criação") + " de meios de pagamento quando um indivíduo realiza um "
                      "depósito à vista em um banco comercial."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Depósito converte PMPP em DV, ambos em M1; não há destruição, só mudança de "
                             "composição (A nova contabilidade social, seção 8.2.3, Quadro 8.1)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 1", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00066
    {
        "id": "ECO-E3-L00066-1", "fonte_ref": "E3-L00066", "destino": "35", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("O aumento da taxa de recolhimento compulsório dos bancos comerciais junto ao Banco Central não "
                      "afeta a base monetária, mas reduz a quantidade de meios de pagamento na economia por meio de "
                      "seu efeito sobre o multiplicador bancário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento da taxa de recolhimento compulsório dos bancos comerciais junto ao Banco Central "
                      "<u>não afeta a base monetária</u>, mas reduz a quantidade de meios de pagamento na economia "
                      "<u>por meio de seu efeito sobre o multiplicador</u> bancário."),
        "poucas": ("O compulsório só reclassifica reservas que já estão na " + azb("base") + "; o que muda é o "
                   + azb("multiplicador") + " (r ↑ → m ↓), e por ele cai o M1."),
        "destrinchando": [
            "Composição da base: " + vd("B = PMPP + caixa dos bancos + reservas no BC") + " (voluntárias + "
            "compulsórias). É a " + azb("liquidez sob controle do BC") + ".",
            "Elevar a alíquota obriga os bancos a transferir parte dos recursos de reservas livres (ou caixa) "
            "para a conta de compulsório. Tudo continua dentro da base: " + vd("ΔB = 0") + ".",
            "Mas a fração dos depósitos que fica imobilizada cresce: r ↑ em " + vd("m = (1 + c)/(c + r)")
            + ", m ↓ e " + vd("M1 = m · B") + " cai.",
            "Diferença entre instrumentos: " + azb("open market") + " e " + azb("redesconto") + " atuam sobre a "
            "<b>base</b>; o " + azb("compulsório") + " atua sobre o <b>multiplicador</b>. É a distinção que a "
            "banca mais cobra nesse tema.",
            "Na prática, se faltarem reservas aos bancos para cumprir o novo compulsório, eles podem recorrer ao "
            "redesconto — e aí a base cresce. O item trata do efeito direto, como nos livros-texto.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Separa corretamente o canal (multiplicador) do "
                       "agregado que não se altera (base). Engana quem associa todo instrumento do BC a mudança "
                       "na base. Pista: compulsório = “quanto dos depósitos fica parado”, ou seja, parâmetro do "
                       "multiplicador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento do compulsório reduz a base monetária e, por consequência, os meios de pagamento.”</i> "
            "→ ERRADO (nexo indevido: a base não muda)",
            "<i>“A venda de títulos pelo Banco Central no mercado aberto reduz a base monetária.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Compulsórios fazem parte da base (liquidez sob controle do BC); taxa maior reduz o "
                             "multiplicador e os meios de pagamento; diagrama de composição de M1 e da base."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 2", "tipo_fonte": "DIAGRAMA", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
]
