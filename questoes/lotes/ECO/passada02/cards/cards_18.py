"""Cards do lote de redação 18 — ECO, passada 02 (nota 36: Banco Central e política monetária)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "func": "🏛️ Funções do Banco Central",
    "inst": "🛠️ Instrumentos de política monetária",
    "senh": "💸 Senhoriagem e imposto inflacionário",
}

CMD_INST = "Julgue o item a seguir, relativo aos instrumentos de política monetária."

CMD_BOZAN = "Com base na estrutura e no funcionamento dos mercados monetários, julgue o item a seguir."

CMD_NAB_26 = "A respeito de moeda e política monetária, julgue (C ou E) o item seguinte."

CMD_NAB_2 = "No que diz respeito à moeda e à política monetária, julgue (C ou E) o item a seguir."

CMD_NAB_23 = "A respeito de teoria monetária e política monetária, julgue (C ou E) o item a seguir."

CMD_RT_JUROS = ("Recentemente o Banco Central iniciou um ciclo de alta dos juros, tendo em vista as pressões "
                "inflacionárias na economia brasileira. Sobre este tema, avalie a proposição abaixo.")

CMD_RT_BC = "A respeito do papel do Banco Central e da teoria monetária, julgue o item a seguir."

CMD_NIDI_JUL = ("A respeito do Banco Central e suas atribuições enquanto gestor da política monetária, julgue "
                "certo ou errado o item a seguir.")

CMD_NIDI_JUN = ("Julgue certo ou errado o item a seguir, acerca das políticas monetárias típicas conduzidas pelos "
                "bancos centrais e, em particular, o BCB.")

CMD_NIDI_DEZ = ("No que concerne à política monetária, seu papel, seus instrumentos e agentes, julgue (C ou E) o "
                "item a seguir.")

CARDS = [
    # ------------------------------------------------------------------ E1-0533
    {
        "id": "ECO-E1-0533-1", "fonte_ref": "E1-0533", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central, para aumentar a oferta de moeda, deve implementar a política de redução da "
                      "reserva compulsória dos bancos comerciais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Banco Central, para aumentar a oferta de moeda, deve implementar a política de "
                      "<u>redução</u> da reserva compulsória dos bancos comerciais."),
        "poucas": ("Compulsório menor libera reservas para empréstimos e eleva o " + azb("multiplicador "
                   "monetário") + ": a oferta de moeda (M1) aumenta. É medida " + azb("expansionista") + "."),
        "destrinchando": [
            azb("Recolhimento compulsório") + " = fração dos depósitos que os bancos são obrigados a manter "
            "parada no Banco Central. Quanto maior a alíquota, menos sobra para emprestar.",
            "O mecanismo é o " + azb("multiplicador bancário") + ": cada empréstimo volta ao sistema como novo "
            "depósito, que é de novo parcialmente emprestado. Na versão simples, k = " + vd("1/r") + " (r = "
            "encaixe total). Com r = 25%, k = 4; com r = 20%, k = 5 — basta reduzir r para que a mesma base "
            "monetária sustente mais meios de pagamento.",
            "Na fórmula completa, M1 = k × B, com k = 1/[c + d(R/D)] (c = parcela da moeda mantida em "
            "papel-moeda; R/D = encaixes sobre depósitos). O compulsório mexe em R/D; a base B não muda, muda o "
            "multiplicador.",
            "Os três instrumentos clássicos e o sentido expansionista de cada um: " + vd("compra") + " de títulos "
            "no mercado aberto, " + vd("redução") + " do compulsório e " + vd("redução") + " da taxa de "
            "redesconto. As versões contracionistas são o inverso.",
            "No " + rx("Brasil") + ", o compulsório é usado mais como instrumento " + azb("macroprudencial") + " "
            "(liquidez do sistema em crises, como em 2008 e 2020) do que como alavanca rotineira de juros, papel "
            "que cabe à meta da Selic.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de manual: associa corretamente instrumento e direção. O "
                       "risco está só no sentido do verbo (“redução”); a banca costuma inverter para “elevação” "
                       "e manter o objetivo “aumentar a oferta de moeda”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…para aumentar a oferta de moeda, deve elevar a reserva compulsória…”</i> → ERRADO (inversão: "
            "elevar é contracionista)",
            "<i>“A redução do compulsório aumenta a base monetária.”</i> → ERRADO (troca de conceito: altera o "
            "multiplicador, não a base)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": "Reduzir o compulsório deixa mais recursos para os bancos emprestarem e aumenta a "
                            "oferta de moeda; instrumento clássico de política expansionista.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0700
    {
        "id": "ECO-E1-0700-1", "fonte_ref": "E1-0700", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("Uma política monetária expansionista conduzida por um banco central consiste em aumentar a "
                      "base monetária e elevar a taxa de juros simultaneamente, visando estimular o investimento "
                      "privado e o consumo agregado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma política monetária expansionista conduzida por um banco central consiste em aumentar a "
                       "base monetária e ") + vm("elevar") + az(" a taxa de juros simultaneamente, visando "
                       "estimular o investimento privado e o consumo agregado.")),
        "poucas": ("Expandir a moeda e <b>reduzir</b> os juros são as duas faces do mesmo movimento: mais liquidez "
                   "barateia o dinheiro. Juros em alta são marca da política " + azb("contracionista") + "."),
        "destrinchando": [
            "Os juros são o “preço” da liquidez. Se o banco central injeta reservas (comprando títulos, por "
            "exemplo), sobra dinheiro no interbancário e a taxa cai; se retira reservas, ela sobe. Por isso "
            + vd("M ↑ e i ↑") + " ao mesmo tempo, por ação do banco central, é incoerente.",
            "No " + azb("IS-LM") + ": política monetária expansionista desloca a LM para a direita → "
            + vd("i ↓, Y ↑") + ". A queda dos juros reduz o custo do capital e o custo de oportunidade de "
            "consumir hoje, estimulando investimento e consumo — o objetivo citado no item.",
            "Hoje a maioria dos bancos centrais opera fixando uma " + azb("meta para a taxa de juros") + " de "
            "curto prazo (no " + rx("Brasil") + ", a Selic) e ajusta a liquidez para que a taxa de mercado a "
            "acompanhe. Expansionista = cortar a meta; contracionista = elevá-la.",
            "Juros e moeda só sobem juntos por causas externas à política: por exemplo, quando a demanda por "
            "moeda cresce (renda ou preços maiores) e o banco central acomoda parcialmente.",
            vm("Regra-âncora: política monetária expansionista → mais moeda e juros menores; contracionista → "
               "menos moeda e juros maiores."),
        ],
        "dissecando": (cz("[meia-verdade · contradição]") + " Começa certo (aumentar a base) e termina certo "
                       "(estimular investimento e consumo); o erro foi enxertado no meio, num verbo que contradiz "
                       "as outras duas partes. Pista: juros altos não estimulam investimento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma política monetária contracionista consiste em reduzir a base monetária e elevar a taxa de "
            "juros, visando conter a demanda agregada.”</i> → CERTO",
            "<i>“A política monetária expansionista eleva a taxa de juros de curto prazo para estimular a "
            "poupança e, com ela, o investimento.”</i> → ERRADO (nexo indevido: juros sobem na contracionista)",
        ])],
        "reescrita": ("Uma política monetária expansionista conduzida por um banco central consiste em aumentar a "
                      "base monetária e " + hl("reduzir") + " a taxa de juros simultaneamente, visando estimular "
                      "o investimento privado e o consumo agregado."),
        "tipo_erro": ["MEIA_VERDADE", "CONTRADICAO"], "moduladores": ["simultaneamente"], "dificuldade": 1,
        "comentario_fonte": "Expansionista aumenta liquidez e reduz juros; juros em alta são típicos da "
                            "contracionista (Blanchard, Mankiw).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “porum” → “por um” (erro de digitação da fonte)"],
    },
    # ------------------------------------------------------------------ E1-0701
    {
        "id": "ECO-E1-0701-1", "fonte_ref": "E1-0701", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_INST,
        "rotulo_item": "Item",
        "assertiva": ("A redução da taxa de redesconto do banco central encarece o crédito bancário para o setor "
                      "privado, caracterizando uma medida expansionista."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A redução da taxa de redesconto do banco central ") + vm("encarece") + az(" o crédito "
                       "bancário para o setor privado, caracterizando uma medida expansionista.")),
        "poucas": ("Redesconto mais barato reduz o custo de captação dos bancos e tende a <b>baratear</b> o "
                   "crédito ao setor privado — por isso a medida é " + azb("expansionista") + "."),
        "destrinchando": [
            azb("Redesconto") + " = empréstimo do banco central aos bancos comerciais, com garantia em "
            "títulos, para cobrir faltas de reservas. A " + azb("taxa de redesconto") + " é o juro cobrado "
            "nessa operação.",
            "Cadeia da redução: taxa de redesconto ↓ → custo de obter liquidez de emergência ↓ → bancos podem "
            "operar com menos reservas ociosas e emprestar mais → oferta de crédito ↑ e juros do crédito ↓ → "
            "moeda ↑. É uma das três alavancas clássicas, ao lado do " + azb("open market") + " e do "
            + azb("compulsório") + ".",
            "Na prática do " + rx("Brasil") + ", o redesconto tem taxa punitiva (acima da Selic) e uso eventual; "
            "funciona sobretudo como rede de proteção do sistema (função de " + azb("emprestador de última "
            "instância") + "). O sentido econômico, porém, é o descrito: barateá-lo é expansionista.",
            vm("Regra-âncora: qualquer instrumento que barateie ou amplie a liquidez dos bancos é expansionista; "
               "o que a encarece ou restringe é contracionista."),
        ],
        "dissecando": (cz("[contradição]") + " O item fecha com a classificação certa (“expansionista”) e "
                       "contradiz a si mesmo no efeito (“encarece”). Medida que encarece o crédito não pode ser "
                       "expansionista: basta checar a coerência interna."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação da taxa de redesconto encarece a liquidez dos bancos e caracteriza uma medida "
            "contracionista.”</i> → CERTO",
            "<i>“A redução da taxa de redesconto barateia o crédito e reduz os meios de pagamento.”</i> → ERRADO "
            "(inversão: os meios de pagamento aumentam)",
        ])],
        "reescrita": ("A redução da taxa de redesconto do banco central " + hl("barateia") + " o crédito bancário "
                      "para o setor privado, caracterizando uma medida expansionista."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Reduzir o redesconto barateia a liquidez dos bancos e, por tabela, o crédito ao setor "
                            "privado; o erro está em “encarece”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “redes conto” e “centralencarece” → “redesconto” e “central encarece” "
                    "(erros de digitação da fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00126
    {
        "id": "ECO-E2-L00126-1", "fonte_ref": "E2-L00126", "destino": "36", "subtema": H2["func"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central do Brasil atua como banco dos bancos e é responsável por emitir a moeda "
                      "nacional, sendo o principal emissor da base monetária. Essa base monetária é composta pelo "
                      "papel-moeda em poder do público e pelo encaixe bancário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Banco Central do Brasil atua como banco dos bancos e é responsável por emitir a moeda "
                      "nacional, sendo o principal emissor da base monetária. Essa base monetária é composta pelo "
                      "<u>papel-moeda em poder do público e pelo encaixe bancário</u>."),
        "poucas": ("As duas partes estão certas: o BCB é " + azb("banco dos bancos") + " e emissor da moeda, e a "
                   + azb("base monetária") + " = " + vd("PMPP + encaixes dos bancos") + "."),
        "destrinchando": [
            azb("Base monetária") + " (B, “moeda de alta potência”) = passivo monetário do banco central: "
            + vd("B = PMPP + encaixes") + ". Encaixes = moeda guardada no caixa dos bancos + reservas "
            "bancárias depositadas no BC (voluntárias e compulsórias sobre depósitos à vista).",
            "Forma equivalente: B = " + azb("papel-moeda emitido") + " + reservas bancárias no BC, porque o "
            "papel-moeda emitido se reparte entre o público (PMPP) e o caixa dos bancos.",
            "Não confundir com " + azb("M1 (meios de pagamento)") + " = " + vd("PMPP + depósitos à vista") + ". "
            "A diferença está no segundo termo: na base entram os encaixes dos bancos; no M1, os depósitos do "
            "público. É a troca mais cobrada no tema.",
            "Funções do BCB citadas: " + azb("banco dos bancos") + " (guarda as reservas, liquida pagamentos "
            "interbancários, empresta via redesconto) e " + azb("banco emissor") + " (competência exclusiva, "
            + vd("CF, art. 164") + "). O “principal emissor” é até modesto: no " + rx("Brasil") + " ele é o "
            "único — a Casa da Moeda só fabrica as cédulas.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz a definição de manual. O risco é o "
                       "candidato confundir base com M1 e achar que faltam os depósitos à vista, ou estranhar o "
                       "“principal” (impreciso, mas não falso). 🔥 A banca alterna “encaixes” e “depósitos à "
                       "vista” para fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Essa base monetária é composta pelo papel-moeda em poder do público e pelos depósitos à vista "
            "nos bancos comerciais.”</i> → ERRADO (troca de conceito: essa é a definição de M1)",
            "<i>“A base monetária corresponde ao passivo monetário do Banco Central.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["principal"], "dificuldade": 1,
        "comentario_fonte": "O BC emite a moeda nacional; a base monetária soma papel-moeda em poder do público e "
                            "encaixes bancários.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00127
    {
        "id": "ECO-E2-L00127-1", "fonte_ref": "E2-L00127", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A política de redesconto é uma ferramenta utilizada pelo Banco Central para influenciar as "
                      "taxas de juros no mercado, facilitando empréstimos a bancos comerciais a uma taxa de "
                      "redesconto. Entretanto, diferentemente de modificar a taxa de compulsório, alterar a taxa "
                      "de redesconto altera juros, mas não impacta fortemente no comportamento da economia "
                      "monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A política de redesconto é uma ferramenta utilizada pelo Banco Central para influenciar as "
                       "taxas de juros no mercado, facilitando empréstimos a bancos comerciais a uma taxa de "
                       "redesconto. ") + vm("Entretanto, diferentemente de") + az(" modificar a taxa de "
                       "compulsório, alterar a taxa de redesconto altera juros, ") + vm("mas não impacta "
                       "fortemente") + az(" no comportamento da economia monetária.")),
        "poucas": ("O redesconto é um dos três instrumentos clássicos de controle da oferta de moeda: como o "
                   "compulsório, ele mexe na " + azb("liquidez") + " e no crédito, e não só “nos juros”."),
        "destrinchando": [
            "A primeira frase está certa: o banco central empresta aos bancos comerciais à " + azb("taxa de "
            "redesconto") + ", e esse custo influencia as taxas do mercado.",
            "O efeito vai além do preço: redesconto barato estimula os bancos a tomar reservas emprestadas do "
            "BC (" + vd("base monetária ↑") + ") e a operar com menos reservas ociosas, emprestando mais; "
            "redesconto caro faz o contrário. "
            "Liquidez, crédito e meios de pagamento mudam — é impacto sobre a “economia monetária”.",
            "Mais importante, o redesconto sustenta a função de " + azb("emprestador de última instância") + ": "
            "sem ele, uma falta momentânea de reservas num banco pode virar corrida bancária e crise "
            "sistêmica. Daí a ideia, desde " + oc("Walter Bagehot") + " (<i>Lombard Street</i>, 1873), de "
            "emprestar livremente, com boas garantias, a juros punitivos.",
            "Nuance: no " + rx("Brasil") + " o redesconto é o instrumento <b>menos usado</b> no dia a dia (a "
            "liquidez é regulada pelo open market e pela meta da Selic). Mas a afirmação do item é teórica e "
            "contrasta, sem fundamento, o redesconto com o compulsório — ambos afetam a oferta de moeda.",
        ],
        "dissecando": (cz("[meia-verdade · juízo indevido]") + " A 1ª frase é definição correta; o "
                       "“Entretanto” abre o enxerto falso, que cria uma hierarquia (“não impacta fortemente”) e "
                       "uma oposição com o compulsório que os manuais não fazem. Desconfie de “diferentemente "
                       "de” entre instrumentos que têm o mesmo efeito de fundo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Assim como a alteração do compulsório, a alteração da taxa de redesconto afeta a oferta de "
            "moeda.”</i> → CERTO",
            "<i>“Alterar a taxa de redesconto afeta apenas o custo do crédito, sem efeito sobre a liquidez do "
            "sistema bancário.”</i> → ERRADO (restrição indevida: as reservas emprestadas também mudam)",
        ])],
        "reescrita": ("A política de redesconto é uma ferramenta utilizada pelo Banco Central para influenciar as "
                      "taxas de juros no mercado, facilitando empréstimos a bancos comerciais a uma taxa de "
                      "redesconto. " + hl("Assim como") + " modificar a taxa de compulsório, alterar a taxa de "
                      "redesconto altera juros, " + hl("e também impacta") + " no comportamento da economia "
                      "monetária."),
        "tipo_erro": ["MEIA_VERDADE", "JUIZO_INDEVIDO"], "moduladores": ["fortemente"], "dificuldade": 2,
        "comentario_fonte": "O redesconto influencia o custo e a disposição dos bancos a emprestar, ampliando ou "
                            "reduzindo a liquidez; afeta a economia de modo significativo. A fonte fala em "
                            "“empréstimos interbancários”, impreciso: o redesconto é empréstimo do BC aos bancos.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00388
    {
        "id": "ECO-E2-L00388-1", "fonte_ref": "E2-L00388", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos canais de transmissão da política monetária.",
        "rotulo_item": "Item",
        "assertiva": ("O canal do crédito da política monetária sugere que a taxa de juros básica afeta a economia "
                      "não apenas pelo custo do capital, mas também pela disponibilidade de empréstimos. Uma "
                      "elevação da Selic piora os balanços das empresas e bancos (efeito balanço), aumentando a "
                      "assimetria de informação e o prêmio de risco, o que amplifica o efeito contracionista da "
                      "política monetária sobre o investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O canal do crédito da política monetária sugere que a taxa de juros básica afeta a economia "
                      "não apenas pelo custo do capital, mas também pela <u>disponibilidade de empréstimos</u>. "
                      "Uma elevação da Selic piora os balanços das empresas e bancos (efeito balanço), aumentando "
                      "a assimetria de informação e o prêmio de risco, o que <u>amplifica</u> o efeito "
                      "contracionista da política monetária sobre o investimento."),
        "poucas": ("É a tese do " + azb("canal do crédito") + " / " + azb("acelerador financeiro") + ": juros "
                   "altos deterioram balanços e garantias, encarecem e racionam o crédito e assim "
                   "<b>amplificam</b> o aperto monetário."),
        "destrinchando": [
            "No canal tradicional (" + azb("canal dos juros") + "), a Selic ↑ eleva o custo do capital e reduz o "
            "investimento. O canal do crédito acrescenta um " + azb("prêmio de financiamento externo") + ": a "
            "diferença entre o custo de captar fora e o custo de usar recursos próprios, que existe porque o "
            "credor conhece mal o tomador (" + azb("assimetria de informação") + ").",
            "Duas vias: (1) " + azb("canal de balanço") + " — juros altos reduzem o valor dos ativos dados em "
            "garantia e o fluxo de caixa das empresas; com menos colateral, o prêmio de risco sobe e o crédito "
            "encolhe; (2) " + azb("canal dos empréstimos bancários") + " — o aperto reduz reservas e captação dos "
            "bancos, e quem depende de banco (pequenas e médias empresas) perde acesso ao crédito.",
            "Resultado: o efeito final sobre investimento e produto é maior do que o canal dos juros explicaria "
            "sozinho. Na expansão, a lógica se inverte: balanços melhores baixam o prêmio e alimentam o boom.",
            "Referências: " + oc("Bernanke e Gertler") + " (<i>Inside the black box</i>, 1995) sistematizaram o "
            "canal do crédito; " + oc("Bernanke, Gertler e Gilchrist") + " (1999) formalizaram o "
            + azb("acelerador financeiro") + ". Os demais canais de transmissão: câmbio, preços de ativos "
            "(riqueza) e expectativas.",
            "No " + rx("Brasil") + ", a forte dependência do crédito bancário e o peso do crédito direcionado "
            "(BNDES, rural, habitacional) modulam essa transmissão — o direcionado reage pouco à Selic.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Reproduz a teoria com vocabulário técnico denso "
                       "(“efeito balanço”, “prêmio de risco”), que intimida. A palavra-chave é “amplifica”: o "
                       "canal do crédito não substitui o dos juros, soma-se a ele."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o que atenua o efeito contracionista da política monetária sobre o investimento.”</i> → "
            "ERRADO (inversão: o canal amplifica)",
            "<i>“Segundo o canal do crédito, a política monetária afeta a economia exclusivamente pelo custo do "
            "capital.”</i> → ERRADO (modulador absoluto: o canal acrescenta a disponibilidade de crédito)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["não apenas", "amplifica"],
        "dificuldade": 2,
        "comentario_fonte": "Explicação do canal de crédito (acelerador financeiro): juros altos reduzem colaterais "
                            "e fluxo de caixa; bancos racionam crédito ou aumentam o spread, potencializando o "
                            "choque.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00482
    {
        "id": "ECO-E2-L00482-1", "fonte_ref": "E2-L00482", "destino": "36", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_26,
        "rotulo_item": "Item",
        "assertiva": ("O Conselho Monetário Nacional define periodicamente, por meio de seu Comitê de Política "
                      "Monetária (COPOM), o valor da taxa básica de juros da economia — taxa SELIC."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O ") + vm("Conselho Monetário Nacional") + az(" define periodicamente, por meio de seu "
                       "Comitê de Política Monetária (COPOM), o valor da taxa básica de juros da economia — taxa "
                       "SELIC.")),
        "poucas": ("O " + azb("Copom") + " é órgão do " + azb("Banco Central do Brasil") + ", não do CMN. O CMN "
                   "fixa a <b>meta de inflação</b>; o Copom/BCB fixa a <b>meta da Selic</b> para cumpri-la."),
        "destrinchando": [
            azb("Conselho Monetário Nacional") + " (CMN): órgão normativo máximo do Sistema Financeiro Nacional "
            "(" + vd("Lei 4.595/1964") + "). Composição atual: ministro da Fazenda (preside), ministro do "
            "Planejamento e Orçamento e presidente do BCB. Fixa a " + azb("meta de inflação") + " e as diretrizes "
            "das políticas monetária, creditícia e cambial; regula o sistema.",
            azb("Comitê de Política Monetária") + " (Copom): criado em " + vd("1996") + " dentro do BCB, formado "
            "pelo presidente e pelos diretores do Banco Central. Reúne-se " + vd("8 vezes por ano") + " (a cada "
            "~45 dias) e define a <b>meta</b> da Selic e seu viés.",
            "A " + azb("Selic efetiva") + " (taxa média das operações compromissadas de um dia com títulos "
            "públicos) é mantida perto da meta pelas " + azb("operações de mercado aberto") + " da mesa do BCB.",
            "Divisão de tarefas do regime de metas: o CMN diz <b>aonde chegar</b> (meta de inflação, hoje "
            + vd("3%") + " em regime de meta contínua, com tolerância de 1,5 p.p. ⏳ (out/2026)); o BCB escolhe "
            "<b>como chegar</b> (Selic). É a " + azb("autonomia de instrumentos") + ", reforçada pela "
            + vd("LC 179/2021") + ".",
            vm("Regra-âncora: CMN → meta de inflação; Copom/BCB → meta da Selic."),
        ],
        "dissecando": (cz("[troca de ator]") + " O item mantém tudo certo (Copom, periodicidade, Selic como taxa "
                       "básica) e troca só o órgão a que o Copom pertence. O “seu” é a armadilha: soa natural e "
                       "faz o candidato aceitar a subordinação ao CMN."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Conselho Monetário Nacional fixa a meta para a inflação, cabendo ao Copom definir a meta "
            "para a taxa Selic.”</i> → CERTO",
            "<i>“O Copom é composto pelo ministro da Fazenda, pelo ministro do Planejamento e pelo presidente "
            "do Banco Central.”</i> → ERRADO (troca de ator: essa é a composição do CMN)",
        ])],
        "reescrita": ("O " + hl("Banco Central do Brasil") + " define periodicamente, por meio de seu Comitê de "
                      "Política Monetária (COPOM), o valor da taxa básica de juros da economia — taxa SELIC."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O Copom é órgão do BCB, não do CMN; o CMN define metas de inflação e diretrizes "
                            "gerais, e a decisão operacional sobre os juros cabe ao Copom/BCB.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00483
    {
        "id": "ECO-E2-L00483-1", "fonte_ref": "E2-L00483", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_26,
        "rotulo_item": "Item",
        "assertiva": "Ao comprar notas do Tesouro Nacional (NTN) do mercado, o Banco Central aumenta a oferta de moeda.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ao <u>comprar</u> notas do Tesouro Nacional (NTN) do mercado, o Banco Central "
                      "<u>aumenta</u> a oferta de moeda."),
        "poucas": ("Comprar títulos no " + azb("mercado aberto") + " é pagar com moeda nova: o BC credita "
                   "reservas aos vendedores, a base monetária cresce e, pelo multiplicador, a oferta de moeda "
                   "também."),
        "destrinchando": [
            azb("Operação de mercado aberto") + " (open market) = compra e venda de títulos públicos pelo BC no "
            "mercado <b>secundário</b>. Compra → injeta liquidez (expansionista); venda → enxuga liquidez "
            "(contracionista).",
            "Contabilidade: o título entra no <b>ativo</b> do BC; a contrapartida é crédito na conta de "
            + azb("reservas bancárias") + " do vendedor, que é <b>passivo</b> monetário. " + vd("Base ↑ no "
            "valor da compra") + ", e M1 ↑ em múltiplo disso (M1 = k × B).",
            "NTN (Notas do Tesouro Nacional) são títulos de emissão do Tesouro; quais títulos o BC compra não "
            "importa para o sinal do efeito — LTN, LFT ou NTN, comprar expande, vender contrai.",
            "Limite institucional no " + rx("Brasil") + ": o BC não pode financiar o Tesouro direto (" + vd("CF, "
            "art. 164, § 1º") + ") nem comprar títulos na emissão primária (" + vd("LRF, art. 39") + "); por isso "
            "opera “do mercado”, como diz o item. A carteira própria do BC serve para as "
            + azb("operações compromissadas") + ", principal forma de regular a liquidez diária.",
        ],
        "dissecando": (cz("[literalidade]") + " Item direto: verbo “comprar” + efeito “aumenta”. A sigla NTN "
                       "serve de distração — o examinador aposta que o candidato hesite por não conhecer o "
                       "título. Só o sentido da operação importa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao vender NTN ao mercado, o Banco Central aumenta a oferta de moeda.”</i> → ERRADO (inversão: "
            "a venda contrai)",
            "<i>“Ao comprar NTN diretamente do Tesouro, na emissão, o Banco Central financia o déficit "
            "público.”</i> → ERRADO (operação vedada pela CF, art. 164, § 1º, e pela LRF)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Compra de títulos no open market injeta moeda (crédito nas reservas dos bancos), "
                            "expande a base e, via multiplicador, a oferta de moeda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: o verso da fonte trazia, colado ao fim, o comentário de outro item da mesma "
                    "lista (definição de base monetária × M1, gabarito ERRADO); descartado aqui, pois esse item "
                    "é convertido em outro lote"],
    },
    # ------------------------------------------------------------------ E2-L00721
    {
        "id": "ECO-E2-L00721-1", "fonte_ref": "E2-L00721", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_2,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central do Brasil pode atuar na oferta monetária por meio, entre outras, das "
                      "operações de mercado aberto, nas quais a autoridade monetária altera a taxa de redesconto "
                      "dos seus empréstimos aos bancos comerciais, aumentando ou retirando estímulos à concessão "
                      "de empréstimos pelos bancos à população."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Banco Central do Brasil pode atuar na oferta monetária por meio, entre outras, das "
                       "operações de ") + vm("mercado aberto") + az(", nas quais a autoridade monetária altera a "
                       "taxa de redesconto dos seus empréstimos aos bancos comerciais, aumentando ou retirando "
                       "estímulos à concessão de empréstimos pelos bancos à população.")),
        "poucas": ("O item descreve a " + azb("política de redesconto") + " e a chama de " + azb("mercado "
                   "aberto") + ". Open market é compra e venda de títulos públicos, não fixação de taxa de "
                   "empréstimo."),
        "destrinchando": [
            "Os três instrumentos clássicos, cada um com sua “alavanca”: " + azb("open market") + " → "
            "quantidade de títulos comprados/vendidos (mexe na base); " + azb("redesconto") + " → taxa e "
            "condições dos empréstimos do BC aos bancos; " + azb("compulsório") + " → alíquota sobre depósitos "
            "(mexe no multiplicador).",
            "Redesconto: o BC empresta reservas a bancos com falta de liquidez, contra garantia em títulos. "
            "Taxa maior desestimula esses empréstimos e, com eles, o crédito ao público; taxa menor estimula. A "
            "descrição do item (estímulos à concessão de empréstimos) está certa — só o nome está trocado.",
            "Mercado aberto: o BC compra ou vende títulos (em geral em " + azb("operações compromissadas") + ", "
            "com recompra/revenda) para manter a Selic efetiva junto à meta. É o instrumento mais usado no "
            + rx("Brasil") + " no dia a dia.",
            "A primeira parte do item (o BCB atua na oferta monetária por vários instrumentos) é verdadeira.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Clássico de definição cruzada: nome de um instrumento + "
                       "mecanismo de outro. A pista é a expressão “taxa de redesconto” dentro da definição de "
                       "“mercado aberto” — termos que nunca andam juntos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…das operações de mercado aberto, nas quais a autoridade monetária compra ou vende títulos "
            "públicos, aumentando ou reduzindo a liquidez do sistema.”</i> → CERTO",
            "<i>“…da política de redesconto, na qual o BC compra títulos públicos dos bancos com deságio.”</i> → "
            "ERRADO (troca de conceito: redesconto é empréstimo com garantia)",
        ])],
        "reescrita": ("O Banco Central do Brasil pode atuar na oferta monetária por meio, entre outras, das "
                      "operações de " + hl("redesconto") + ", nas quais a autoridade monetária altera a taxa de "
                      "redesconto dos seus empréstimos aos bancos comerciais, aumentando ou retirando estímulos à "
                      "concessão de empréstimos pelos bancos à população."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "O item confunde open market (compra e venda de títulos) com redesconto (taxa dos "
                            "empréstimos de liquidez do BC aos bancos): descreve o redesconto e o chama de mercado "
                            "aberto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: linha E2-L00776 da fonte repete este item; comentário fundido aqui"],
    },
    # ------------------------------------------------------------------ E2-L00723
    {
        "id": "ECO-E2-L00723-1", "fonte_ref": "E2-L00723", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_2,
        "rotulo_item": "Item",
        "assertiva": ("Considere que o Banco Central atue no mercado de câmbio à vista por meio da venda de dólares "
                      "das reservas internacionais e, simultaneamente, faça uma operação de mercado aberto, no "
                      "mesmo valor, comprando títulos da dívida pública em poder do público. Nessa hipótese, não "
                      "haverá alteração da base monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere que o Banco Central atue no mercado de câmbio à vista por meio da <u>venda</u> de "
                      "dólares das reservas internacionais e, simultaneamente, faça uma operação de mercado aberto, "
                      "<u>no mesmo valor</u>, <u>comprando</u> títulos da dívida pública em poder do público. "
                      "Nessa hipótese, não haverá alteração da base monetária."),
        "poucas": ("Vender dólares <b>retira</b> reais (base ↓); comprar títulos <b>injeta</b> reais (base ↑). "
                   "No mesmo valor, os efeitos se anulam: é uma " + azb("intervenção esterilizada") + "."),
        "destrinchando": [
            "Toda operação do BC com o setor privado mexe na base, porque o BC paga ou recebe em moeda que ele "
            "mesmo emite. Pelo lado do ativo do BC: " + vd("ΔB = Δreservas internacionais + Δtítulos + "
            "Δredesconto + …") + ".",
            "Venda de US$ no mercado à vista: o comprador entrega reais ao BC → reservas internacionais ↓ e "
            + vd("base ↓") + ". Compra de títulos no open market: o BC paga em reais → carteira de títulos ↑ e "
            + vd("base ↑") + ". Mesmo valor → ΔB = 0; muda só a composição do ativo do BC.",
            azb("Esterilização") + " é exatamente isso: neutralizar, com o open market, o efeito monetário de "
            "uma intervenção cambial. O caso inverso é o mais comum no " + rx("Brasil") + " dos anos 2000: o BC "
            "comprava dólares (base ↑) e vendia títulos/fazia compromissadas para enxugar (base ↓) — o que "
            "inflou a dívida bruta.",
            "Atenção ao mercado <b>à vista</b>: o " + azb("swap cambial") + " (derivativo liquidado em reais) "
            "e as linhas com compromisso de recompra não movimentam reservas da mesma forma — por isso o item "
            "especifica a operação.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " Duas operações com sinais opostos e mesmo "
                       "valor: quem olha só para “compra de títulos” (expansionista) marca ERRADO. Resolva "
                       "sempre somando os efeitos sobre a base, operação por operação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…venda de dólares das reservas e, simultaneamente, venda de títulos no mesmo valor. Nessa "
            "hipótese, não haverá alteração da base monetária.”</i> → ERRADO (dado alterado: as duas contraem; "
            "a base cai o dobro)",
            "<i>“A compra de dólares pelo BC no mercado à vista, sem esterilização, expande a base "
            "monetária.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["simultaneamente", "no mesmo valor"],
        "dificuldade": 2,
        "comentario_fonte": "Venda de dólares contrai a base; compra de títulos a expande; no mesmo valor, os "
                            "efeitos se anulam (esterilização).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: linha E2-L00778 da fonte repete este item; comentário fundido aqui"],
    },
    # ------------------------------------------------------------------ E2-L00815
    {
        "id": "ECO-E2-L00815-1", "fonte_ref": "E2-L00815", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação à teoria macroeconômica, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A política de redesconto é utilizada pelo Banco Central para influenciar a oferta de moeda "
                      "através da alteração da taxa de juros de empréstimos aos bancos comerciais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A política de redesconto é utilizada pelo Banco Central para influenciar a oferta de moeda "
                      "através da alteração da <u>taxa de juros de empréstimos aos bancos comerciais</u>."),
        "poucas": ("Definição correta: o " + azb("redesconto") + " é o empréstimo do BC aos bancos, e a taxa "
                   "cobrada nele é uma das alavancas da oferta de moeda."),
        "destrinchando": [
            "Mecânica: um banco que fecha o dia sem reservas suficientes (para o compulsório ou para a "
            "compensação) toma recursos do BC dando títulos em garantia. A " + azb("taxa de redesconto") + " "
            "é o preço dessa liquidez.",
            "Direção do efeito: taxa " + vd("↓") + " → reservas emprestadas mais baratas → bancos emprestam com "
            "mais folga → " + vd("oferta de moeda ↑") + " (expansionista). Taxa " + vd("↑") + " → o oposto "
            "(contracionista).",
            "O redesconto também altera a quantidade e o prazo das linhas, as garantias aceitas e os limites "
            "por banco — não só a taxa. No " + rx("Brasil") + " há modalidades intradia, de um dia e de prazos "
            "maiores, com custo acima da Selic.",
            "Limitação clássica: é instrumento <b>passivo</b> — o BC fixa as condições, mas quem decide tomar o "
            "empréstimo é o banco. Por isso é menos preciso que o open market, em que a iniciativa é do BC.",
            "Funções do redesconto: regulação monetária e " + azb("emprestador de última instância") + " "
            "(socorro de liquidez para evitar crises sistêmicas).",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, sem modulador perigoso. O “influenciar” é "
                       "relativo e protege o item. A banca costuma errar a definição trocando o redesconto pela "
                       "compra de títulos ou pela “reemissão” de títulos com desconto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política de redesconto é utilizada pelo Banco Central para influenciar a oferta de moeda por "
            "meio da compra e venda de títulos públicos.”</i> → ERRADO (troca de conceito: isso é open market)",
            "<i>“A elevação da taxa de redesconto é medida expansionista.”</i> → ERRADO (inversão: é "
            "contracionista)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["influenciar"], "dificuldade": 1,
        "comentario_fonte": "O BC empresta aos bancos à taxa de redesconto; reduzi-la incentiva os bancos a "
                            "emprestar e aumenta a oferta de moeda; aumentá-la faz o oposto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00950
    {
        "id": "ECO-E2-L00950-1", "fonte_ref": "E2-L00950", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": "Em relação à teoria monetária, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Os depósitos voluntários remunerados são um novo instrumento de política monetária do Banco "
                      "Central do Brasil (BACEN) e contribuem para a gestão de liquidez na economia, sem gerar os "
                      "efeitos sobre a dívida bruta do governo federal que se observam quando da utilização de "
                      "operações compromissadas com títulos públicos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os depósitos voluntários remunerados são um novo instrumento de política monetária do Banco "
                      "Central do Brasil (BACEN) e contribuem para a gestão de liquidez na economia, <u>sem gerar "
                      "os efeitos sobre a dívida bruta</u> do governo federal que se observam quando da utilização "
                      "de operações compromissadas com títulos públicos."),
        "poucas": ("Desde a " + vd("Lei 14.185/2021") + ", o BCB pode acolher " + azb("depósitos voluntários "
                   "remunerados") + " dos bancos: enxugam liquidez como as compromissadas, mas não entram na "
                   + azb("dívida bruta") + "."),
        "destrinchando": [
            "Problema de origem: para retirar o excesso de reservas (por exemplo, após comprar dólares), o BC "
            "fazia " + azb("operações compromissadas") + " — vendia títulos do Tesouro da sua carteira com "
            "compromisso de recompra. Como são títulos públicos nas mãos do mercado, a metodologia brasileira "
            "conta as compromissadas na " + azb("dívida bruta do governo geral") + " (DBGG).",
            "Com o " + azb("depósito voluntário remunerado") + ", o banco deixa o excesso de reservas parado no "
            "BC e recebe juros. O efeito monetário é o mesmo (a liquidez sai de circulação), mas não há título "
            "público envolvido: o passivo é do BC, e a " + vd("DBGG não aumenta") + ".",
            "Antes da lei, o BC só recebia depósitos de bancos sob a forma de " + azb("compulsórios") + " (à "
            "vista e a prazo). O novo instrumento amplia o “cardápio” de gestão de liquidez, sem substituir "
            "as compromissadas.",
            "Peso das compromissadas: junto com a dívida mobiliária, formam a maior parte da DBGG, que fechou "
            "2023 em cerca de " + vd("74% do PIB") + " ⏳ (out/2026).",
            "Crítica comum: a mudança é sobretudo <b>contábil</b> — o custo de remunerar os depósitos continua "
            "existindo e afeta o resultado do BC (e, por ele, o Tesouro). O ganho está na leitura do indicador "
            "de dívida bruta, muito acompanhado pelo mercado.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item de atualidade institucional: exige saber que o "
                       "instrumento existe (2021) e por que foi criado. A trava é o “sem gerar os efeitos sobre a "
                       "dívida bruta” — que é exatamente a justificativa do projeto."),
        "modulos": [
            ("⚖️ Base normativa", [
                vd("Lei 14.185/2021, art. 1º") + ": o Banco Central do Brasil fica autorizado a acolher depósitos "
                "voluntários à vista ou a prazo das instituições financeiras.",
            ]),
            ("😈 Para dificultar", [
                "<i>“Os depósitos voluntários remunerados, ao retirarem liquidez, elevam a dívida bruta do "
                "governo geral, assim como as operações compromissadas.”</i> → ERRADO (contradição: não entram "
                "na DBGG)",
                "<i>“Os depósitos voluntários remunerados substituíram integralmente as operações "
                "compromissadas.”</i> → ERRADO (modulador absoluto: os dois instrumentos convivem)",
            ]),
        ],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": ["sem"], "dificuldade": 2,
        "comentario_fonte": "Lei 14.185/2021 autoriza o BCB a acolher depósitos voluntários; alternativa às "
                            "compromissadas, que reduz a moeda em circulação sem afetar a dívida bruta. DBGG de "
                            "R$ 8.079 bi (74,3% do PIB) no fim de 2023.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00990
    {
        "id": "ECO-E2-L00990-1", "fonte_ref": "E2-L00990", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Em relação aos agregados monetários e à política monetária, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "Uma compra de títulos públicos pelo Banco Central no mercado aberto causa um aumento da base monetária.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma <u>compra</u> de títulos públicos pelo Banco Central no mercado aberto causa um "
                      "<u>aumento</u> da base monetária."),
        "poucas": ("O BC paga os títulos com moeda que ele mesmo cria: o vendedor recebe reservas ou "
                   "papel-moeda e a " + azb("base monetária") + " cresce no valor da compra."),
        "destrinchando": [
            vd("Base monetária = PMPP + encaixes dos bancos") + " (caixa em moeda + reservas no BC). Para onde "
            "quer que vá o dinheiro pago pelo BC, cai dentro de uma das parcelas:",
            "Se o vendedor é um banco, o BC credita sua conta de " + azb("reservas bancárias") + " → encaixes ↑. "
            "Se o banco saca e guarda no cofre → continua encaixe. Se o vendedor é o público e fica com "
            "papel-moeda → PMPP ↑. Se deposita no banco → encaixes ↑. Em todos os casos, " + vd("B ↑") + ".",
            "Efeito sobre os meios de pagamento: M1 = k × B. Com k > 1, M1 cresce mais que a base, à medida que "
            "os bancos emprestam as novas reservas (" + azb("multiplicador bancário") + ").",
            "Espelho: venda de títulos pelo BC → o comprador paga em moeda, que sai de circulação → B ↓ "
            "(contracionista).",
            vm("Regra-âncora: BC compra qualquer ativo (título, dólar, empréstimo a banco) → base sobe; BC "
               "vende ou recebe → base cai."),
        ],
        "dissecando": (cz("[literalidade]") + " Relação direta entre operação e agregado. A pegadinha "
                       "possível seria o candidato pensar que o dinheiro “fica nos bancos” e não conta — mas "
                       "encaixe bancário é parte da base."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma compra de títulos públicos pelo BC no mercado aberto aumenta a base monetária, mas não "
            "altera os meios de pagamento.”</i> → ERRADO (meia-verdade: M1 também cresce, via multiplicador)",
            "<i>“Se o banco vendedor mantiver a moeda recebida em caixa, a base monetária não se altera.”</i> → "
            "ERRADO (caixa dos bancos integra os encaixes, logo a base)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O vendedor recebe moeda e a base se expande; mesmo que o banco retenha a moeda em "
                            "caixa, ela aumenta os encaixes e, portanto, a base.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00111-1 (mesma assertiva, em simulado Nidi de jun/2025)"],
    },
    # ------------------------------------------------------------------ E2-L01270
    {
        "id": "ECO-E2-L01270-1", "fonte_ref": "E2-L01270", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23,
        "rotulo_item": "Item",
        "assertiva": ("Para controlar a oferta de moeda, um dos instrumentos que o BC pode utilizar é a taxa de "
                      "redesconto: ao decidir aumentar essa taxa, o BC estará incentivando os bancos a não tomar "
                      "novos empréstimos junto ao BC, reduzindo o componente emprestado das reservas bancárias."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para controlar a oferta de moeda, um dos instrumentos que o BC pode utilizar é a taxa de "
                      "redesconto: ao decidir <u>aumentar</u> essa taxa, o BC estará incentivando os bancos a "
                      "<u>não tomar</u> novos empréstimos junto ao BC, reduzindo o <u>componente emprestado das "
                      "reservas bancárias</u>."),
        "poucas": ("Redesconto mais caro desestimula os bancos a tomar reservas do BC; as " + azb("reservas "
                   "emprestadas") + " caem, e com elas a base e a oferta de moeda (efeito contracionista)."),
        "destrinchando": [
            "Na contabilidade monetária, as reservas bancárias se dividem em " + azb("reservas emprestadas") + " "
            "(obtidas no redesconto) e " + azb("reservas não emprestadas") + " (vindas, sobretudo, do open "
            "market). O redesconto atua diretamente sobre a primeira parcela.",
            "Taxa de redesconto ↑ → tomar reservas do BC fica mais caro que obtê-las no interbancário ou "
            "manter folga própria → bancos reduzem esses empréstimos e fazem mais " + azb("reservas "
            "voluntárias") + " de precaução → crédito ao público ↓ → " + vd("oferta de moeda ↓") + ".",
            "Usos do redesconto no " + rx("Brasil") + ": (1) cobrir descasamentos de curtíssimo e curto prazo "
            "entre operações ativas e passivas dos bancos; (2) " + azb("prestamista de última instância") + " "
            "em crises de liquidez; (3) regulação monetária.",
            "Como o redesconto depende da iniciativa do banco, o controle do BC sobre a oferta de moeda por essa "
            "via é indireto — daí o “pode utilizar” e o “incentivando” do item.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Reescreve o mecanismo em linguagem técnica "
                       "(“componente emprestado das reservas”) que assusta quem só decorou “redesconto ↑ = "
                       "contracionista”. Os moduladores (“pode”, “incentivando”) são precisos e mantêm o item "
                       "verdadeiro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…ao decidir reduzir essa taxa, o BC estará incentivando os bancos a não tomar novos "
            "empréstimos…”</i> → ERRADO (inversão: redução estimula os empréstimos)",
            "<i>“…ao aumentar essa taxa, o BC reduz o componente não emprestado das reservas bancárias.”</i> → "
            "ERRADO (troca de conceito: o redesconto atinge as reservas emprestadas)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["pode", "incentivando"], "dificuldade": 2,
        "comentario_fonte": "Redesconto: crédito do BC aos bancos contra garantias em títulos, para descasamentos "
                            "de curto prazo e como prestamista de última instância; aumento da taxa leva os bancos "
                            "a reduzirem a oferta de moeda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01272
    {
        "id": "ECO-E2-L01272-1", "fonte_ref": "E2-L01272", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central realiza operações de mercado aberto vendendo títulos públicos quando deseja "
                      "aumentar a liquidez do sistema bancário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Banco Central realiza operações de mercado aberto ") + vm("vendendo") + az(" títulos "
                       "públicos quando deseja aumentar a liquidez do sistema bancário.")),
        "poucas": ("Para <b>aumentar</b> a liquidez, o BC <b>compra</b> títulos e paga com reservas; vender "
                   "títulos tira reservas dos bancos — é o movimento contracionista."),
        "destrinchando": [
            "Quem compra um título do BC paga com reservas bancárias, que “voltam” ao BC e deixam de "
            "circular: " + vd("liquidez ↓, juros ↑") + ". Quem vende um título ao BC recebe reservas novas: "
            + vd("liquidez ↑, juros ↓") + ".",
            "No dia a dia do " + rx("Brasil") + ", a mesa do BCB faz isso sobretudo por " + azb("operações "
            "compromissadas") + ": “compromissada tomadora” (BC vende com compromisso de recompra) enxuga "
            "liquidez; “compromissada doadora” (BC compra com compromisso de revenda) injeta.",
            "O objetivo operacional é manter a " + azb("Selic efetiva") + " colada na meta do Copom: sobrando "
            "reservas, a taxa do interbancário tende a cair abaixo da meta, e o BC vende títulos; faltando, ela "
            "sobe, e o BC compra.",
            vm("Regra-âncora: BC compra título → injeta moeda; BC vende título → enxuga moeda."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido da operação mantendo o objetivo. Para não cair, "
                       "pense no fluxo de dinheiro: quem vende títulos <b>recebe</b> dinheiro do comprador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Banco Central realiza operações de mercado aberto vendendo títulos públicos quando deseja "
            "reduzir a liquidez do sistema bancário.”</i> → CERTO",
            "<i>“A venda de títulos pelo BC eleva a base monetária porque aumenta o ativo do BC.”</i> → ERRADO "
            "(inversão: na venda o ativo e a base diminuem)",
        ])],
        "reescrita": ("O Banco Central realiza operações de mercado aberto " + hl("comprando") + " títulos "
                      "públicos quando deseja aumentar a liquidez do sistema bancário."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Para aumentar a liquidez, o Bacen compra títulos no mercado aberto, repassando moeda "
                            "aos vendedores.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01580
    {
        "id": "ECO-E2-L01580-1", "fonte_ref": "E2-L01580", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_JUROS,
        "rotulo_item": "Item",
        "assertiva": ("Para promover a elevação dos juros, um mecanismo que pode ser utilizado pelo BC são as "
                      "vendas de títulos nas operações de mercado aberto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para promover a <u>elevação</u> dos juros, um mecanismo que pode ser utilizado pelo BC são "
                      "as <u>vendas</u> de títulos nas operações de mercado aberto."),
        "poucas": ("Vendendo títulos, o BC recolhe reservas dos bancos; com menos liquidez no interbancário, a "
                   "taxa de juros de curto prazo " + vd("sobe") + ". É o braço operacional de um ciclo de "
                   "alta."),
        "destrinchando": [
            "Mecanismo de preço e quantidade: os bancos pagam os títulos com reservas → oferta de reservas ↓ → "
            "quem precisa de reservas paga mais no " + azb("mercado interbancário") + " → " + vd("i ↑") + ". "
            "Visto pelo lado do título: mais oferta de títulos → preço ↓ → rendimento ↑.",
            "Como funciona hoje no " + rx("Brasil") + ": o " + azb("Copom") + " anuncia a nova meta da Selic; "
            "a mesa do BCB faz as " + azb("operações compromissadas") + " necessárias para que a "
            + azb("Selic efetiva") + " acompanhe a meta. A venda de títulos é a ferramenta, não a decisão.",
            "Os juros mais altos se transmitem pelos canais do crédito, do câmbio (apreciação), dos preços de "
            "ativos e das expectativas, contendo a demanda e a inflação com defasagem de vários trimestres.",
            "Outros caminhos para a mesma direção: elevar compulsório ou redesconto (contracionistas), mas com "
            "efeito menos preciso sobre a taxa de curto prazo.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O “pode ser utilizado” e o “um mecanismo” "
                       "tornam o item seguro: não diz que é o único. Basta acertar o sentido (vender → juros "
                       "sobem)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para promover a elevação dos juros, um mecanismo que pode ser utilizado pelo BC são as compras "
            "de títulos nas operações de mercado aberto.”</i> → ERRADO (inversão: compras derrubam os juros)",
            "<i>“A venda de títulos pelo BC é o único mecanismo capaz de elevar os juros.”</i> → ERRADO "
            "(restrição indevida)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "um mecanismo"],
        "dificuldade": 1,
        "comentario_fonte": "Vendendo títulos, o BC retira moeda de circulação; a menor liquidez pressiona os "
                            "juros para cima — mecanismo básico da política contracionista.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01582
    {
        "id": "ECO-E2-L01582-1", "fonte_ref": "E2-L01582", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_JUROS,
        "rotulo_item": "Item",
        "assertiva": ("Para conter a inflação, além de subir a taxa básica de juros o BC também pode elevar a "
                      "alíquota do recolhimento compulsório, que reduziria a capacidade de o sistema bancário "
                      "criar moeda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para conter a inflação, além de subir a taxa básica de juros o BC também pode "
                      "<u>elevar</u> a alíquota do recolhimento compulsório, que <u>reduziria</u> a capacidade de o "
                      "sistema bancário criar moeda."),
        "poucas": ("Compulsório maior prende mais reservas no BC e reduz o " + azb("multiplicador bancário") + ": "
                   "os bancos criam menos moeda escritural, o crédito encolhe e a demanda esfria."),
        "destrinchando": [
            "Bancos comerciais " + azb("criam moeda") + " ao emprestar: o empréstimo vira depósito à vista em "
            "outro banco, que é de novo parcialmente emprestado. O limite do processo é dado pelos encaixes.",
            "Multiplicador simplificado: " + vd("k = 1/r") + ". Ex.: com encaixe de 20%, R$ 100 de reservas "
            "sustentam até R$ 500 de depósitos; elevando o encaixe para 25%, só R$ 400. É isso que “reduziria a "
            "capacidade de criar moeda”.",
            "Na versão completa, k = 1/[c + d(R/D)], em que c é a fração dos meios de pagamento mantida em "
            "papel-moeda e R/D a razão encaixes/depósitos: o compulsório eleva R/D e reduz k.",
            "Uso combinado com os juros: no " + rx("Brasil") + ", o compulsório já foi usado como reforço em "
            "ciclos de aperto (por exemplo, nas medidas macroprudenciais de 2010–2011) e afrouxado em crises "
            "(2008, 2020) para dar liquidez. Hoje o instrumento principal contra a inflação é a Selic.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item correto e protegido por “pode” e "
                       "pelo condicional “reduziria”. A armadilha comum seria trocar o efeito para a "
                       "<b>base</b> monetária: o compulsório não muda a base, muda o multiplicador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…elevar a alíquota do compulsório, que reduziria a base monetária.”</i> → ERRADO (troca de "
            "conceito: atua sobre o multiplicador)",
            "<i>“…reduzir a alíquota do recolhimento compulsório, que limitaria a criação de moeda.”</i> → ERRADO "
            "(inversão)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "reduziria"], "dificuldade": 1,
        "comentario_fonte": "Elevar o compulsório obriga os bancos a manter mais recursos no BC, reduz a "
                            "capacidade de emprestar e de criar moeda pelo multiplicador e contrai a oferta "
                            "monetária.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01636
    {
        "id": "ECO-E2-L01636-1", "fonte_ref": "E2-L01636", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BC,
        "rotulo_item": "Item",
        "assertiva": ("Se o Banco Central deseja fazer uma política monetária expansionista, algumas alternativas "
                      "são a compra de títulos no mercado aberto e a elevação dos recolhimentos compulsórios."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o Banco Central deseja fazer uma política monetária expansionista, algumas alternativas "
                       "são a compra de títulos no mercado aberto e a ") + vm("elevação") + az(" dos "
                       "recolhimentos compulsórios.")),
        "poucas": ("A compra de títulos é expansionista, mas " + azb("elevar o compulsório") + " é "
                   "contracionista: reduz o multiplicador e a criação de moeda. O correto seria " + vd("reduzir")
                   + " o compulsório."),
        "destrinchando": [
            "Quadro dos instrumentos clássicos — " + azb("expansionista") + ": compra de títulos, redução do "
            "compulsório, redução da taxa de redesconto. " + azb("Contracionista") + ": venda de títulos, "
            "elevação do compulsório, elevação do redesconto.",
            "Onde cada um atua na equação " + vd("M1 = k × B") + ": open market e redesconto mexem na "
            + azb("base") + " (B); o compulsório mexe no " + azb("multiplicador") + " (k).",
            "Limite do controle: o BC não decide quanto o público guarda em papel-moeda em vez de depósitos, "
            "nem quanto os bancos retêm além do exigido. Ele controla a base e a alíquota do compulsório, mas "
            "o multiplicador também depende dessas escolhas privadas — por isso a oferta de moeda é só "
            "<b>parcialmente</b> controlável.",
            "Por essa razão, os bancos centrais passaram a mirar a <b>taxa de juros</b> (no " + rx("Brasil") + ", "
            "a meta da Selic) em vez de agregados monetários; os instrumentos acima viraram meios de "
            "sustentar a taxa escolhida.",
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " Duas alternativas: a 1ª certa dá confiança, a 2ª "
                       "inverte o sentido. 🔥 Itens com listas de instrumentos quase sempre escondem um sentido "
                       "trocado: confira cada elemento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…algumas alternativas são a compra de títulos no mercado aberto e a redução da taxa de "
            "redesconto.”</i> → CERTO",
            "<i>“…algumas alternativas são a venda de títulos no mercado aberto e a redução dos recolhimentos "
            "compulsórios.”</i> → ERRADO (inversão: vender títulos é contracionista)",
        ])],
        "reescrita": ("Se o Banco Central deseja fazer uma política monetária expansionista, algumas alternativas "
                      "são a compra de títulos no mercado aberto e a " + hl("redução") + " dos recolhimentos "
                      "compulsórios."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["algumas"], "dificuldade": 1,
        "comentario_fonte": "Compra de títulos e redução do compulsório são expansionistas; elevar o compulsório "
                            "é contracionista. Slides: M1 = multiplicador × base; o BC não controla as escolhas do "
                            "público e dos bancos que formam o multiplicador.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 475", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "absorvida (M1 = k × B, no 📖)"},
                          {"ref": "IMAGEM 476", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (limites do controle do BC sobre o multiplicador, no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01637
    {
        "id": "ECO-E2-L01637-1", "fonte_ref": "E2-L01637", "destino": "36", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BC,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central é responsável por conduzir a política monetária de forma a preservar o poder "
                      "de compra da moeda, de acordo com as metas de inflação definidas pelo Conselho Monetário "
                      "Nacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Banco Central é responsável por conduzir a política monetária de forma a preservar o poder "
                      "de compra da moeda, de acordo com as metas de inflação definidas pelo <u>Conselho Monetário "
                      "Nacional</u>."),
        "poucas": ("É o arranjo do regime de metas: o " + azb("CMN") + " fixa a meta de inflação; o " + azb("BCB")
                   + " conduz a política monetária para cumpri-la. Estabilidade de preços = preservar o poder de "
                   "compra."),
        "destrinchando": [
            "Objetivo legal: pela " + vd("LC 179/2021") + ", o BCB tem por " + azb("objetivo fundamental") + " "
            "assegurar a estabilidade de preços; sem prejuízo dele, deve zelar pela estabilidade e eficiência "
            "do sistema financeiro, suavizar as flutuações da atividade econômica e fomentar o pleno emprego.",
            "Divisão de tarefas: as metas de política monetária são estabelecidas pelo " + azb("CMN") + " "
            "(ministro da Fazenda, ministro do Planejamento e Orçamento e presidente do BCB) e cabe "
            "privativamente ao BCB conduzir a política necessária para cumpri-las — é a "
            + azb("autonomia de instrumentos") + ", não de objetivos.",
            "Histórico: o regime de metas foi instituído em " + vd("1999") + " (Decreto 3.088), após a "
            "flutuação do real. Desde 2025 vigora a " + azb("meta contínua") + ": a inflação de 12 meses é "
            "acompanhada mês a mês, com meta de " + vd("3%") + " e tolerância de 1,5 p.p. ⏳ (out/2026).",
            "Se a meta é descumprida, o presidente do BCB explica as razões e as providências em "
            + azb("carta aberta") + " ao ministro da Fazenda; no regime contínuo, o descumprimento se configura "
            "quando a inflação fica fora do intervalo por seis meses seguidos.",
        ],
        "dissecando": (cz("[literalidade]") + " Descreve corretamente quem faz o quê. As trocas típicas que a "
                       "banca faria: atribuir a meta ao próprio BC ou ao Copom, ou dizer que o CMN conduz a "
                       "política monetária."),
        "modulos": [
            ("⚖️ Base normativa", [
                vd("LC 179/2021, art. 1º") + ": objetivo fundamental do BCB é assegurar a estabilidade de preços. "
                + vd("Art. 2º") + ": as metas de política monetária são estabelecidas pelo CMN, competindo "
                "privativamente ao BCB conduzir a política monetária necessária para cumpri-las.",
            ]),
            ("😈 Para dificultar", [
                "<i>“…de acordo com as metas de inflação definidas pelo Comitê de Política Monetária.”</i> → "
                "ERRADO (troca de ator: o Copom fixa a meta da Selic, não a de inflação)",
                "<i>“O BCB tem como objetivo exclusivo a estabilidade de preços, vedada qualquer consideração "
                "sobre o nível de atividade.”</i> → ERRADO (modulador absoluto: a lei inclui objetivos "
                "acessórios)",
            ]),
        ],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O BCB conduz a política monetária para atingir as metas de inflação fixadas pelo CMN "
                            "(Fazenda, Planejamento e presidente do BC); objetivo fundamental de estabilidade de "
                            "preços (LC 179/2021).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01638
    {
        "id": "ECO-E2-L01638-1", "fonte_ref": "E2-L01638", "destino": "36", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BC,
        "rotulo_item": "Item",
        "assertiva": ("A defesa de um banco central autônomo está ligada à ideia da credibilidade e estabilidade da "
                      "política monetária, independente de qual seja o governo eleito."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A defesa de um banco central autônomo está ligada à ideia da <u>credibilidade</u> e "
                      "estabilidade da política monetária, independente de qual seja o governo eleito."),
        "poucas": ("O argumento central da " + azb("autonomia") + " é a " + azb("credibilidade") + ": blindar a "
                   "política monetária do ciclo eleitoral reduz o " + azb("viés inflacionário") + " e ancora "
                   "expectativas."),
        "destrinchando": [
            "Base teórica: " + oc("Kydland e Prescott") + " (1977) mostraram o problema da "
            + azb("inconsistência temporal") + " — um governo que promete inflação baixa tem incentivo, depois "
            "que as expectativas se formam, a gerar surpresa inflacionária para reduzir o desemprego. Sabendo "
            "disso, os agentes não acreditam na promessa.",
            oc("Barro e Gordon") + " (1983) formalizaram o " + azb("viés inflacionário") + " da política "
            "discricionária: em equilíbrio, a inflação fica mais alta sem ganho de produto. "
            + oc("Rogoff") + " (1985) propôs delegar a política a um banqueiro central “conservador”, mais "
            "avesso à inflação que a sociedade.",
            "Com credibilidade, as " + azb("expectativas ficam ancoradas") + " e o custo de desinflação (perda "
            "de produto) diminui: o BC precisa de menos juros para obter o mesmo resultado.",
            "No " + rx("Brasil") + ": a " + vd("LC 179/2021") + " deu ao BCB autonomia formal — mandatos de "
            + vd("4 anos") + " para presidente e diretores, não coincidentes com o do presidente da República "
            "(o do presidente do BC começa no 3º ano do governo), e demissão só em hipóteses legais. Até então "
            "a autonomia era apenas operacional, de fato.",
            "Críticas: déficit democrático (decisões de grande impacto distributivo por dirigentes não eleitos) "
            "e risco de descoordenação com a política fiscal.",
        ],
        "dissecando": (cz("[literalidade]") + " Paráfrase da justificativa padrão. A banca poderia tornar o item "
                       "falso trocando o fundamento (ex.: “ligada à necessidade de financiar o Tesouro”) ou "
                       "afirmando que autonomia elimina a coordenação com a política fiscal."),
        "modulos": [
            ("📚 Autores e teses", [
                oc("Kydland e Prescott") + " (1977, <i>Rules rather than discretion</i>): inconsistência temporal; "
                "regras > discrição.",
                oc("Barro e Gordon") + " (1983): viés inflacionário da política discricionária.",
                oc("Rogoff") + " (1985): banqueiro central conservador.",
            ]),
            ("😈 Para dificultar", [
                "<i>“A autonomia do banco central elimina o viés inflacionário ao permitir que a política "
                "monetária acompanhe as prioridades de cada governo eleito.”</i> → ERRADO (inversão: o objetivo "
                "é isolar a política do ciclo eleitoral)",
            ]),
        ],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Autonomia (LC 179/2021) blinda a política monetária de pressões político-partidárias, "
                            "aumenta a credibilidade e ancora expectativas; base em Kydland e Prescott (1977) e "
                            "Barro e Gordon (1983).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00043
    {
        "id": "ECO-E3-L00043-1", "fonte_ref": "E3-L00043", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("Julgue o item que se segue, a respeito das políticas fiscal e monetária, do papel da dívida "
                    "pública como fonte de financiamento e da função reguladora do Estado na economia."),
        "rotulo_item": "Item",
        "assertiva": ("Um dos objetivos primários do Banco Central do Brasil é o controle da inflação, sendo a taxa "
                      "Selic utilizada como principal instrumento de política monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um dos objetivos primários do Banco Central do Brasil é o controle da inflação, sendo a taxa "
                      "Selic utilizada como <u>principal</u> instrumento de política monetária."),
        "poucas": ("No " + azb("regime de metas de inflação") + " (desde 1999), a estabilidade de preços é o "
                   "objetivo fundamental do BCB e a " + azb("meta da Selic") + ", definida pelo Copom, é o "
                   "instrumento principal."),
        "destrinchando": [
            "Objetivo: a " + vd("LC 179/2021, art. 1º") + " define como objetivo fundamental do BCB assegurar a "
            "estabilidade de preços; zelar pelo sistema financeiro, suavizar flutuações da atividade e fomentar "
            "o pleno emprego vêm “sem prejuízo” dele. “Um dos objetivos primários” é, portanto, até cauteloso.",
            "Instrumento: o " + azb("Copom") + " fixa a meta da Selic em " + vd("8 reuniões por ano") + " (cerca "
            "de 45 dias); a mesa de operações do BCB usa o mercado aberto (compromissadas) para manter a Selic "
            "efetiva na meta. Open market, compulsório e redesconto são <b>meios</b> para sustentar a taxa.",
            "Transmissão: Selic ↑ → crédito mais caro, consumo e investimento ↓, real apreciado (importados mais "
            "baratos), expectativas ancoradas → inflação ↓, com defasagem de vários trimestres. A Selic ↓ "
            "faz o caminho inverso.",
            "Contexto: a escolha de uma taxa de juros como instrumento (e não de agregados monetários) "
            "decorre da instabilidade da demanda por moeda; é a prática dos bancos centrais com metas de "
            "inflação.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de enunciado institucional. O risco é o candidato "
                       "implicar com “principal” (há outros instrumentos) ou com “um dos objetivos” (há "
                       "objetivo fundamental). Ambos estão corretos: a Selic é o instrumento principal e o "
                       "controle da inflação é objetivo primário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O único objetivo do Banco Central do Brasil é o controle da inflação, sendo-lhe vedado "
            "considerar o nível de emprego.”</i> → ERRADO (modulador absoluto: a LC 179/2021 prevê objetivos "
            "acessórios)",
            "<i>“A taxa Selic é fixada pelo Conselho Monetário Nacional.”</i> → ERRADO (troca de ator: Copom do "
            "BCB)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["um dos", "principal"], "dificuldade": 1,
        "comentario_fonte": "Regime de metas desde 1999; controle da inflação é objetivo primário do BCB; Selic "
                            "fixada pelo Copom a cada 45 dias é o principal instrumento. Uma das respostas cita "
                            "“Lei 10.803/2003”, que não trata do BCB; o fundamento correto é a LC 179/2021.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00064
    {
        "id": "ECO-E3-L00064-1", "fonte_ref": "E3-L00064", "destino": "36", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("Os Bancos Centrais exercem quatro funções consideradas típicas: emissor de papel-moeda, "
                      "banqueiro do Tesouro Nacional, banqueiro dos bancos comerciais e depositário das reservas "
                      "internacionais. Além dessas atribuições, sua principal função operacional é assegurar a "
                      "estabilidade de preços, por meio da implementação de estratégias de política monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os Bancos Centrais exercem quatro funções consideradas típicas: emissor de papel-moeda, "
                      "banqueiro do Tesouro Nacional, banqueiro dos bancos comerciais e depositário das reservas "
                      "internacionais. Além dessas atribuições, sua principal função operacional é assegurar a "
                      "<u>estabilidade de preços</u>, por meio da implementação de estratégias de política "
                      "monetária."),
        "poucas": ("As quatro funções clássicas estão certas (" + azb("emissor") + ", " + azb("banco do governo")
                   + ", " + azb("banco dos bancos") + ", " + azb("depositário das reservas") + "), e a "
                   "estabilidade de preços é o objetivo central da política monetária moderna."),
        "destrinchando": [
            azb("Banco emissor") + ": monopólio da emissão de papel-moeda e moeda metálica (no " + rx("Brasil")
            + ", " + vd("CF, art. 164") + "); a Casa da Moeda fabrica, o BC emite.",
            azb("Banqueiro do governo") + ": mantém a " + azb("Conta Única do Tesouro") + " e opera como seu "
            "agente financeiro — mas, no Brasil, sem poder emprestar-lhe diretamente (" + vd("CF, art. 164, "
            "§ 1º") + ").",
            azb("Banco dos bancos") + ": guarda as reservas bancárias (voluntárias e compulsórias), liquida os "
            "pagamentos interbancários e empresta via redesconto, como " + azb("emprestador de última "
            "instância") + ".",
            azb("Depositário das reservas internacionais") + ": administra as divisas do país e atua no "
            "mercado de câmbio.",
            "Manuais de economia monetária costumam acrescentar uma quinta função — " + azb("executor da "
            "política monetária") + " —, que o item trata à parte como função “operacional” voltada à "
            "estabilidade de preços. A classificação muda de autor para autor; o conteúdo é o mesmo.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Lista de funções reproduzida corretamente. A banca "
                       "costuma fabricar o ERRADO trocando uma função (ex.: “banqueiro das empresas”, “emissor "
                       "de títulos do Tesouro”) ou atribuindo ao BC a gestão fiscal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…banqueiro do Tesouro Nacional, ao qual pode conceder empréstimos diretos para cobrir "
            "déficits.”</i> → ERRADO (vedado no Brasil: CF, art. 164, § 1º)",
            "<i>“…quatro funções típicas: emissor de papel-moeda, emissor de títulos do Tesouro, banqueiro dos "
            "bancos e depositário das reservas.”</i> → ERRADO (troca de ator: títulos do Tesouro são emitidos "
            "pelo Tesouro)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["principal"], "dificuldade": 1,
        "comentario_fonte": "As quatro funções típicas estão corretas, e a estabilidade de preços é o objetivo "
                            "principal operacional, sobretudo após o regime de metas de 1999.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00067
    {
        "id": "ECO-E3-L00067-1", "fonte_ref": "E3-L00067", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("Uma operação de mercado aberto, na qual o Banco Central compra títulos da dívida e emite "
                      "moeda, aumenta os ativos e os passivos do balancete do Banco Central no mesmo montante."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma operação de mercado aberto, na qual o Banco Central compra títulos da dívida e emite "
                      "moeda, aumenta os <u>ativos e os passivos</u> do balancete do Banco Central <u>no mesmo "
                      "montante</u>."),
        "poucas": ("Partidas dobradas: o título entra no " + azb("ativo") + "; a moeda criada para pagá-lo "
                   "(reservas bancárias ou papel-moeda) é " + azb("passivo monetário") + ". O balancete cresce "
                   "dos dois lados, no mesmo valor."),
        "destrinchando": [
            "Lançamento de uma compra de R$ 100 em títulos: " + vd("Ativo: títulos públicos +100") + " | "
            + vd("Passivo: reservas bancárias +100") + ". Nada sai de um “cofre”: o BC paga criando um crédito "
            "na conta do banco vendedor.",
            "Estrutura simplificada do balancete do BC — ativo: reservas internacionais, créditos a instituições "
            "financeiras (redesconto), títulos públicos federais; " + azb("passivo monetário") + " (= base "
            "monetária): papel-moeda emitido e reservas bancárias; " + azb("passivo não monetário") + ": conta "
            "única do Tesouro, operações compromissadas, depósitos compulsórios em espécie fora da base, "
            "obrigações externas, patrimônio.",
            "Por isso a base monetária pode ser lida pelo lado do ativo: " + vd("ΔB = Δativos − Δpassivos não "
            "monetários") + ". Compra de dólares, redesconto e compra de títulos expandem a base; as operações "
            "inversas a contraem.",
            "“Emitir moeda” aqui é registro eletrônico; papel-moeda físico só é posto em circulação quando o "
            "público saca. Os bancos, ao emprestar, criam " + azb("moeda escritural") + " (M1), mas não base.",
            "Limite: o BC opera no mercado <b>secundário</b>; comprar títulos diretamente do Tesouro é vedado "
            "(" + vd("CF, art. 164, § 1º") + "; " + vd("LRF, art. 39") + ").",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " O senso comum imagina que o BC “gasta” algo para "
                       "comprar o título (ativo troca por ativo, balanço do mesmo tamanho). O item cobra a "
                       "lógica contábil da emissão: moeda é passivo do BC, então o balanço expande."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…aumenta os ativos do Banco Central e reduz seus passivos no mesmo montante.”</i> → ERRADO "
            "(inversão: a moeda emitida é passivo, que aumenta)",
            "<i>“A venda de títulos pelo BC reduz ativos e passivos monetários no mesmo montante.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["no mesmo montante"], "dificuldade": 2,
        "comentario_fonte": "A compra de títulos aumenta o ativo (títulos) e o passivo (reservas ou papel-moeda) "
                            "no mesmo valor; emissão é lançamento contábil eletrônico; balancete do BC; monopólio "
                            "de emissão (CF, art. 164) e vedação de financiar o Tesouro.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 3", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (estrutura do balancete do BC, no 📖)"},
                          {"ref": "IMAGEM 4", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (ilegível na fonte; lançamento reconstruído no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00111
    {
        "id": "ECO-E3-L00111-1", "fonte_ref": "E3-L00111", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUN,
        "rotulo_item": "Item",
        "assertiva": "Uma compra de títulos públicos pelo Banco Central no mercado aberto causa um aumento da base monetária.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma <u>compra</u> de títulos públicos pelo Banco Central no mercado aberto causa um "
                      "<u>aumento</u> da base monetária."),
        "poucas": ("Ao comprar títulos, o BC entrega reservas bancárias aos vendedores: o passivo monetário do BC "
                   "— a " + azb("base monetária") + " — cresce. É a operação expansionista típica."),
        "destrinchando": [
            "Dois blocos que a banca adora confundir: " + azb("meios de pagamento (M1)") + " = moeda corrente "
            "(papel-moeda em poder do público) + moeda escritural (depósitos à vista) — haveres do setor "
            "<b>não monetário</b>; " + azb("base monetária") + " = papel-moeda em poder do público + caixa em "
            "moeda dos bancos + depósitos dos bancos no BC (voluntários e compulsórios) — o que o BC deve ao "
            "público e aos bancos.",
            "A compra de títulos aumenta a base pelo lado das reservas; o M1 só cresce depois, quando os bancos "
            "transformam essas reservas em empréstimos (" + azb("multiplicador") + ").",
            "Efeito sobre juros: mais reservas no mercado interbancário → a taxa de curto prazo tende a "
            "<b>cair</b>. Por isso, num regime de meta para a Selic, a compra (ou a venda) de títulos é dosada "
            "para manter a taxa na meta — injeções e retiradas diárias de liquidez.",
            "Fluxo da operação: títulos vão do mercado para a carteira do BC; reservas vão do BC para o "
            "mercado. Venda de títulos: fluxo inverso, base ↓.",
        ],
        "dissecando": (cz("[literalidade]") + " Relação direta operação → agregado. A dúvida que o examinador "
                       "explora é confundir base com M1 ou achar que a reserva “parada no BC” não conta — mas "
                       "reserva bancária é justamente parte da base."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma compra de títulos públicos pelo Banco Central no mercado aberto aumenta imediatamente os "
            "depósitos à vista do público.”</i> → ERRADO (troca de conceito: aumenta reservas, parte da base; "
            "M1 cresce depois, via crédito)",
            "<i>“A compra de títulos pelo BC tende a reduzir as taxas de juros de curto prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O BC paga os títulos com reservas bancárias; a base (PMPP + reservas) cresce; "
                            "operação expansionista que tende a reduzir os juros de curto prazo. Diagrama de meios "
                            "de pagamento × caixa e depósitos dos bancos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 95", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "absorvida (M1 × base monetária, no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00990-1 (mesma assertiva, em prova Nabuco Pré-TPS/2023)"],
    },
    # ------------------------------------------------------------------ E3-L00113
    {
        "id": "ECO-E3-L00113-1", "fonte_ref": "E3-L00113", "destino": "36", "subtema": H2["inst"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUN,
        "rotulo_item": "Item",
        "assertiva": ("As operações de mercado aberto objetivam primordialmente contribuir para a aproximação entre "
                      "a taxa de juros do mercado de reservas bancárias e a taxa básica de juros anunciada pelas "
                      "autoridades monetárias, evitando que excesso ou falta de liquidez afaste a taxa básica "
                      "anunciada da taxa de mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As operações de mercado aberto objetivam <u>primordialmente</u> contribuir para a "
                      "aproximação entre a taxa de juros do mercado de reservas bancárias e a taxa básica de juros "
                      "anunciada pelas autoridades monetárias, evitando que excesso ou falta de liquidez afaste a "
                      "taxa básica anunciada da taxa de mercado."),
        "poucas": ("Num regime de meta para a taxa de juros, o open market serve para a " + azb("Selic efetiva")
                   + " (mercado de reservas) colar na " + azb("meta da Selic") + " anunciada pelo Copom: o BC "
                   "enxuga ou injeta liquidez diariamente."),
        "destrinchando": [
            "Duas Selic: a " + azb("meta") + " (decidida pelo Copom) e a " + azb("efetiva") + " (taxa média das "
            "operações de um dia entre instituições, lastreadas em títulos públicos e registradas no sistema "
            "Selic). A meta é um anúncio; a efetiva é o preço de mercado das reservas.",
            "O saldo de reservas oscila todo dia por fatores fora do controle direto do BC: pagamentos e "
            "recebimentos do Tesouro, saques de papel-moeda, compra e venda de dólares, recolhimentos "
            "compulsórios. Sem atuação, a taxa interbancária “dançaria” longe da meta.",
            "A mesa do BCB compensa: sobra de reservas → " + azb("compromissadas tomadoras") + " (vende títulos "
            "com recompra, enxuga); falta → " + azb("compromissadas doadoras") + " (compra com revenda, "
            "injeta). Resultado: Selic efetiva colada na meta (diferença de centésimos).",
            "Daí a mudança de perspectiva dos manuais: o open market deixou de ser visto como ferramenta para "
            "fixar a quantidade de moeda e passou a ser a " + azb("sintonia fina") + " que sustenta o preço — "
            "a taxa de juros.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Descreve o objetivo operacional moderno. O "
                       "“primordialmente” assusta quem decorou “open market controla a base monetária”; mas, "
                       "com meta de juros, o controle da liquidez é o meio e a taxa é o alvo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As operações de mercado aberto objetivam primordialmente financiar o déficit do Tesouro "
            "Nacional.”</i> → ERRADO (troca de conceito: financiamento direto é vedado)",
            "<i>“A meta da taxa Selic é fixada pelo mercado, cabendo ao BC apenas anunciá-la.”</i> → ERRADO "
            "(inversão: a meta é decisão do Copom; o mercado forma a taxa efetiva)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["primordialmente"], "dificuldade": 2,
        "comentario_fonte": "O Copom define a meta; o BC atua no open market (compromissadas) ajustando a "
                            "liquidez diária para que a Selic efetiva convirja para a meta — sintonia fina.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
