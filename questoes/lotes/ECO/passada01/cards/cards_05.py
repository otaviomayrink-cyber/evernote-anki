"""Cards do lote de redação 05 — ECO, passada 01 (nota 02 — Elasticidades)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "epd": "📐 Elasticidade-preço da demanda",
    "rec": "💰 Elasticidade, receita e gasto",
    "rc": "🔗 Elasticidade-renda e cruzada",
    "of": "🏭 Elasticidade da oferta",
    "det": "⏳ Determinantes e prazos",
}

CMD_ELAS = "Julgue o item a seguir, relativo ao conceito de elasticidade."
CMD_BOZAN = ("Com base na elasticidade e suas tipologias, julgue as assertivas a seguir acerca de bens duráveis e "
             "não duráveis em diferentes prazos.")
CMD_ARMS = "Acerca dos determinantes e das aplicações da elasticidade, julgue o item a seguir."
CMD_NAB_ELAS = "A respeito dos conceitos e aplicações da elasticidade, julgue os itens a seguir."
CMD_NAB_MICRO3 = "Em relação à microeconomia, julgue os seguintes itens."
CMD_NAB_INTERV = ("Com relação às intervenções governamentais no equilíbrio de mercado e o conceito de elasticidade, "
                  "julgue os seguintes itens.")

FIG_E1_PERDIDA = "irrecuperavel (verso; imagem do caderno E1 não preservada — conteúdo coberto pelo comentário)"

CARDS = [
    # ------------------------------------------------------------------ E1-0118
    {
        "id": "ECO-E1-0118-1", "fonte_ref": "E1-0118", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à curva de demanda linear.",
        "rotulo_item": "Item",
        "assertiva": "Na fórmula da demanda Q = a – bP, o coeficiente angular é o b.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na fórmula da demanda Q = a – bP, o coeficiente angular é <u>o b</u>."),
        "poucas": ("Na demanda linear Q = a − bP, " + azb("a") + " é o intercepto (coeficiente linear) e "
                   + azb("b") + " é o parâmetro de inclinação (coeficiente angular), que entra com sinal "
                   "negativo pela lei da demanda."),
        "destrinchando": [
            "Forma geral de uma reta: y = (coeficiente linear) + (coeficiente angular)·x. Em Q = a − bP, a "
            "variável dependente é Q e a independente é P: " + vd("a") + " é a quantidade demandada com preço "
            "zero; " + vd("b") + " diz quantas unidades de Q se perdem a cada R$ 1 de aumento no preço "
            "(ΔQ/ΔP = −b).",
            "Sinal: o coeficiente angular, a rigor, é <b>−b</b>; quando se diz que “o coeficiente angular é o "
            "b”, fala-se do parâmetro b > 0, já sabendo que a relação é inversa (lei da demanda).",
            "Cuidado com o eixo: os economistas põem o <b>preço no eixo vertical</b> (convenção de "
            + oc("Marshall") + "). Reescrevendo, P = a/b − (1/b)Q: no gráfico usual, a inclinação visível da "
            "reta é " + vd("−1/b") + ". Quanto <b>maior</b> o b, mais <b>deitada</b> fica a curva desenhada.",
            azb("Inclinação ≠ elasticidade") + ": a elasticidade-preço é ε = (ΔQ/ΔP)·(P/Q) = −b·P/Q. Com b "
            "constante, ε muda ao longo da reta, porque a razão P/Q muda.",
            vm("Regra-âncora: na demanda linear, a inclinação é constante; a elasticidade, não."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item de definição: reproduz a leitura escolar da "
                       "equação. O risco está em dois deslizes vizinhos que a banca costuma explorar: confundir "
                       "o coeficiente angular com a <b>elasticidade</b> e esquecer que, com P no eixo vertical, a "
                       "inclinação do desenho é −1/b."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na demanda Q = a − bP, o coeficiente b mede a elasticidade-preço da demanda, constante ao longo "
            "da curva.”</i> → ERRADO (troca de conceito: inclinação ≠ elasticidade)",
            "<i>“No gráfico com o preço no eixo vertical, a inclinação da demanda Q = a − bP é −1/b.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Coeficiente angular é b, com sinal negativo; informa o quão inclinada é a curva "
                            "de demanda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota: em sentido estrito o coeficiente angular de Q em P é −b; gabarito CERTO mantido "
                    "pela leitura usual (parâmetro b da relação inversa)"],
    },
    # ------------------------------------------------------------------ E1-0119
    {
        "id": "ECO-E1-0119-1", "fonte_ref": "E1-0119", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo aos casos extremos de elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Para uma curva de demanda completamente horizontal, os consumidores irão adquirir toda a "
                      "quantidade disponível a um preço específico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para uma curva de demanda <u>completamente horizontal</u>, os consumidores irão adquirir "
                      "toda a quantidade disponível <u>a um preço específico</u>."),
        "poucas": ("Demanda horizontal = " + azb("perfeitamente elástica") + " (|ε| = ∞): ao preço p* os "
                   "compradores absorvem qualquer quantidade; acima dele, não compram nada."),
        "destrinchando": [
            "|ε| = |%ΔQ / %ΔP|. Na horizontal, uma variação de preço ínfima leva a quantidade de “tudo” a "
            "“nada”: a razão tende ao " + vd("infinito") + ". Abaixo de p*, a quantidade demandada seria "
            "ilimitada.",
            "Onde aparece: a " + azb("firma em concorrência perfeita") + " enfrenta demanda horizontal ao preço "
            "de mercado (é tomadora de preço: vende o que quiser a p*, nada acima). O mesmo vale para um "
            + azb("país pequeno") + " no comércio internacional, que importa o quanto quiser ao preço mundial.",
            "Note a diferença entre a demanda <b>da firma</b> (horizontal) e a demanda <b>do mercado</b> "
            "(negativamente inclinada): a horizontalidade decorre de haver substitutos perfeitos — os produtos "
            "idênticos dos concorrentes.",
            "Extremo oposto: demanda " + azb("vertical") + " (|ε| = 0, perfeitamente inelástica), em que a "
            "quantidade não reage ao preço.",
            vm("Regra-âncora: horizontal = |ε| infinito; vertical = ε zero."),
        ],
        "grafico_verso": "ECO-E1-0119-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " O item descreve com outras palavras a demanda perfeitamente "
                       "elástica. A armadilha é inverter mentalmente os extremos: quem associa “horizontal” a "
                       "“o preço não importa” tende a marcar ERRADO. 🔥 Par clássico de itens: horizontal × "
                       "vertical."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma curva de demanda horizontal indica demanda perfeitamente inelástica.”</i> → ERRADO (troca "
            "de conceito: é perfeitamente elástica)",
            "<i>“A firma em concorrência perfeita enfrenta curva de demanda horizontal ao preço de mercado.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Demanda horizontal é perfeitamente elástica: compra-se qualquer quantidade ao "
                            "preço dado; se o preço sobe minimamente, a quantidade cai a zero.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (24).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (verso; substituída por ECO-E1-0119-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0120
    {
        "id": "ECO-E1-0120-1", "fonte_ref": "E1-0120", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo aos casos extremos de elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma curva de demanda estritamente vertical, o interesse dos consumidores por um produto "
                      "permanece constante, independentemente das variações no preço. A demanda é perfeitamente "
                      "inelástica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma curva de demanda <u>estritamente vertical</u>, o interesse dos consumidores por um "
                      "produto permanece constante, independentemente das variações no preço. A demanda é "
                      "<u>perfeitamente inelástica</u>."),
        "poucas": ("Curva vertical: a quantidade demandada é a mesma a qualquer preço, logo %ΔQ = 0 e "
                   + vd("ε = 0") + " — " + azb("demanda perfeitamente inelástica") + "."),
        "destrinchando": [
            "Com ε = %ΔQ / %ΔP e %ΔQ sempre nulo, a elasticidade é zero em todos os pontos. Toda a variação de "
            "preço se traduz em variação de gasto: se p dobra, o gasto dobra.",
            "Exemplos de livro (aproximações): insulina para diabéticos, medicamentos sem substituto, "
            "tratamentos vitais. Na prática, nenhuma demanda é vertical em todo o intervalo de preços — acima de "
            "certo ponto, a restrição orçamentária obriga a reduzir o consumo.",
            "Consequência em incidência tributária: com demanda vertical, o imposto recai <b>inteiramente</b> "
            "sobre o consumidor, e não há " + azb("peso morto") + " (a quantidade não muda).",
            "Não confundir com demanda de " + azb("elasticidade unitária") + " (hipérbole, gasto constante) nem "
            "com a horizontal (|ε| = ∞).",
            "“Interesse constante” é linguagem imprecisa: o que fica constante é a <b>quantidade demandada</b>, "
            "não a disposição a pagar (que é ilimitada no trecho vertical).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item usa “interesse dos consumidores” no lugar de "
                       "“quantidade demandada”, mas a segunda frase fecha o sentido sem ambiguidade. Pista: "
                       "“independentemente das variações no preço” é a definição de ε = 0."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com demanda perfeitamente inelástica, um imposto sobre o vendedor é suportado integralmente "
            "pelo produtor.”</i> → ERRADO (inversão: recai todo sobre o consumidor)",
            "<i>“Em uma curva de demanda vertical, a elasticidade-preço é igual a 1 em todos os pontos.”</i> → "
            "ERRADO (dado alterado: é zero)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["estritamente", "independentemente"], "dificuldade": 1,
        "comentario_fonte": "Sensibilidade ao preço totalmente ausente: compradores mantêm o mesmo nível de "
                            "compra, não importa o quanto o preço flutue.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (28).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": FIG_E1_PERDIDA}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0121
    {
        "id": "ECO-E1-0121-1", "fonte_ref": "E1-0121", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Quando a curva de demanda é uma reta, ou seja, linear, há várias elasticidades ao longo "
                      "dela."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando a curva de demanda é uma reta, ou seja, linear, há <u>várias elasticidades</u> ao "
                      "longo dela."),
        "poucas": ("Na reta a inclinação é constante, mas ε = (ΔQ/ΔP)·(P/Q) depende de " + azb("P/Q")
                   + ", que muda a cada ponto: |ε| vai de " + vd("∞") + " a " + vd("0") + ", passando por "
                   + vd("1") + " no ponto médio."),
        "destrinchando": [
            "Para Q = a − bP: ε = −b·P/Q. No intercepto do preço (Q = 0, P máximo), |ε| → " + vd("∞")
            + "; no intercepto da quantidade (P = 0), " + vd("ε = 0") + "; no " + azb("ponto médio")
            + " (Q = a/2), " + vd("|ε| = 1") + ".",
            "Metade superior da reta (preços altos, quantidades baixas): " + azb("trecho elástico")
            + " (|ε| > 1). Metade inferior: " + azb("trecho inelástico") + " (|ε| < 1).",
            "Ligação com a receita: RT = P·Q é máxima no ponto médio. Acima dele, baixar o preço aumenta a "
            "receita; abaixo, diminui. Por isso o monopolista nunca opera no trecho inelástico.",
            "Curvas com elasticidade <b>constante</b> em todos os pontos são as do tipo Q = A·P<sup>−ε</sup> "
            "(isoelásticas), além dos casos extremos horizontal (∞) e vertical (0).",
            vm("Regra-âncora: inclinação é ΔQ/ΔP; elasticidade é inclinação × P/Q — reta não tem elasticidade "
               "única."),
        ],
        "grafico_verso": "ECO-E1-0121-1-V1",
        "dissecando": (cz("[contraintuitivo]") + " Contraria a intuição de que “reta = comportamento constante”. "
                       "O item cobra a distinção entre inclinação e elasticidade. 🔥 Variação frequente: “a "
                       "demanda linear tem elasticidade constante” → ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em uma demanda linear, a elasticidade-preço é unitária no ponto médio e maior que 1, em módulo, "
            "acima dele.”</i> → CERTO",
            "<i>“Como a inclinação de uma demanda linear é constante, sua elasticidade-preço também o é.”</i> → "
            "ERRADO (troca de conceito: inclinação ≠ elasticidade)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["várias"], "dificuldade": 1,
        "comentario_fonte": "A elasticidade varia ao longo da reta: no ponto de preço zero, Ed = 0; no de "
                            "quantidade zero, Ed infinita; no ponto médio, Ed = 1.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (25).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (verso; substituída por ECO-E1-0121-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0122
    {
        "id": "ECO-E1-0122-1", "fonte_ref": "E1-0122", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-renda da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-renda da demanda (ERD) mede como a quantidade demandada responde a "
                      "alterações do preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elasticidade-renda da demanda (ERD) mede como a quantidade demandada responde a "
                       "alterações ") + vm("do preço") + az(".")),
        "poucas": ("A " + azb("elasticidade-renda") + " mede a resposta da quantidade demandada a variações "
                   "da <b>renda</b> do consumidor; a resposta ao preço é medida pela elasticidade-preço."),
        "destrinchando": [
            "Fórmula: " + vd("η = %ΔQ / %ΔR") + ". Compare: elasticidade-preço = %ΔQ<sub>x</sub> / "
            "%ΔP<sub>x</sub>; cruzada = %ΔQ<sub>x</sub> / %ΔP<sub>y</sub>. O denominador diz qual elasticidade "
            "é.",
            "Classificação pelo sinal e tamanho de η: " + vd("η < 0") + " → " + azb("bem inferior") + "; "
            + vd("η > 0") + " → " + azb("bem normal") + ", subdividido em " + azb("bem necessário")
            + " (0 < η < 1) e " + azb("bem de luxo/superior") + " (η > 1).",
            "Base empírica: a " + oc("lei de Engel") + " — à medida que a renda cresce, a parcela gasta com "
            "alimentação cai (alimentos têm η < 1). A curva de Engel relaciona renda e quantidade, mantidos os "
            "preços.",
            "Graficamente, a renda é um " + azb("deslocador") + " da demanda: muda a renda, a curva inteira se "
            "move (direita para normal, esquerda para inferior); não há movimento ao longo da curva.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mantém o nome correto (“elasticidade-renda”) e troca só a "
                       "variável explicativa. Pista: o nome da elasticidade é sempre o nome do denominador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um bem com elasticidade-renda entre 0 e 1 é classificado como inferior.”</i> → ERRADO (troca de "
            "conceito: é normal necessário)",
            "<i>“A elasticidade-renda da demanda mede a variação percentual da quantidade demandada decorrente "
            "da variação percentual da renda, mantidos constantes os preços.”</i> → CERTO",
        ])],
        "reescrita": ("A elasticidade-renda da demanda (ERD) mede como a quantidade demandada responde a "
                      "alterações " + hl("da renda do consumidor") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A ERD mede como a quantidade demandada responde a alterações de renda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (26).jpeg", "tipo_fonte": "TEXTO/GRÁFICO", "lado": "verso",
                           "acao": FIG_E1_PERDIDA},
                          {"ref": "Untitled (30).jpeg", "tipo_fonte": "TEXTO/GRÁFICO", "lado": "verso",
                           "acao": FIG_E1_PERDIDA}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0123
    {
        "id": "ECO-E1-0123-1", "fonte_ref": "E1-0123", "destino": "02", "subtema": H2["of"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da oferta.",
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-preço da oferta mede a variação percentual da quantidade ofertada de um bem "
                      "em decorrência de uma variação percentual em seu preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elasticidade-preço da oferta mede a variação percentual da <u>quantidade ofertada</u> de "
                      "um bem em decorrência de uma variação percentual em <u>seu preço</u>."),
        "poucas": ("Definição literal: " + vd("εˢ = %ΔQˢ / %ΔP") + ". Pela lei da oferta, o sinal é "
                   "positivo — preço e quantidade ofertada andam juntos."),
        "destrinchando": [
            "Classificação: " + vd("εˢ > 1") + " oferta elástica; " + vd("εˢ < 1") + " inelástica; εˢ = 1 "
            "unitária; εˢ = 0 perfeitamente inelástica (vertical: oferta fixa, como terrenos numa área ou "
            "ingressos de um estádio); εˢ → ∞ perfeitamente elástica (horizontal).",
            "Determinantes: (1) " + azb("tempo") + " — no muito curto prazo a produção não se ajusta (oferta "
            "quase vertical); no longo prazo, firmas entram, ampliam plantas, e a oferta fica mais elástica; "
            "(2) " + azb("capacidade ociosa") + " e estoques; (3) mobilidade dos fatores e facilidade de "
            "aumentar a produção sem elevar muito o custo marginal.",
            "Curiosidade de reta: toda oferta linear que parte da <b>origem</b> tem εˢ = 1 em todos os pontos; "
            "se corta o eixo do preço (intercepto positivo), εˢ > 1; se corta o eixo da quantidade, εˢ < 1.",
            "Diferença-chave para a demanda: na oferta, P e Q sobem juntos, então a receita do vendedor sempre "
            "cresce quando o preço sobe ao longo da curva de oferta — o “teste da receita” é coisa da demanda.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição de manual. O risco seria uma troca "
                       "sutil — “quantidade demandada” no lugar de “ofertada” ou “variação absoluta” no lugar de "
                       "“percentual” —, que aqui não ocorre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-preço da oferta tende a ser menor no longo prazo, quando as firmas já ajustaram "
            "a capacidade.”</i> → ERRADO (inversão: é maior no longo prazo)",
            "<i>“Uma oferta linear que parte da origem tem elasticidade unitária em todos os pontos.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Repete a definição da assertiva.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (27).jpeg", "tipo_fonte": "TEXTO/GRÁFICO", "lado": "verso",
                           "acao": FIG_E1_PERDIDA},
                          {"ref": "Untitled (29).jpeg", "tipo_fonte": "TEXTO/GRÁFICO", "lado": "verso",
                           "acao": FIG_E1_PERDIDA}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0189
    {
        "id": "ECO-E1-0189-1", "fonte_ref": "E1-0189", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda e à classificação dos bens.",
        "rotulo_item": "Item",
        "assertiva": ("Se o aumento do preço de um bem deixar o consumo inalterado, esse bem deverá ser um bem "
                      "normal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o aumento do preço de um bem deixar o consumo inalterado, esse bem ")
                    + vm("deverá ser um bem normal") + az(".")),
        "poucas": ("Consumo que não reage ao preço revela " + vd("elasticidade-preço nula") + " (demanda "
                   "perfeitamente inelástica). “Bem normal” é classificação pela <b>renda</b>: nada se conclui "
                   "sobre ela a partir de uma reação ao preço."),
        "destrinchando": [
            "Duas réguas diferentes: " + azb("elasticidade-preço") + " (resposta de Q ao preço do próprio bem) "
            "classifica a demanda em elástica, inelástica, unitária; " + azb("elasticidade-renda")
            + " (resposta de Q à renda) classifica o bem em normal (η > 0) ou inferior (η < 0).",
            "Consumo inalterado após alta de preço → %ΔQ = 0 → " + vd("ε = 0") + ": típico de bens essenciais "
            "sem substitutos (medicamentos de uso contínuo, por exemplo).",
            "Esse bem pode ser normal <b>ou</b> inferior: um remédio pode ter η ≈ 0 ou levemente positiva; um "
            "genérico pode ter η < 0 (com mais renda, troca-se pela marca). A informação dada não decide.",
            "Pela decomposição de " + oc("Slutsky") + ": efeito total = substituição (sempre contrário ao preço) "
            "+ renda. Consumo inalterado significa que os dois efeitos somaram zero — o que, se o efeito "
            "substituição for não nulo, exige efeito renda que o compense, indício de bem <b>inferior</b>, e não "
            "de bem normal.",
            vm("Regra-âncora: normal/inferior se decide pela renda; elástico/inelástico, pelo preço."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O item cria uma ligação lógica entre "
                       "dois eixos independentes (preço e renda) e a reforça com o modal “deverá”. Pista: a "
                       "premissa só fala de preço; a conclusão, de renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o aumento do preço de um bem deixar o consumo inalterado, a demanda por esse bem é "
            "perfeitamente inelástica naquele intervalo.”</i> → CERTO",
            "<i>“Se o aumento da renda reduzir o consumo de um bem, ele é um bem de Giffen.”</i> → ERRADO "
            "(generalização: é inferior; Giffen é caso extremo de inferior)",
        ])],
        "reescrita": ("Se o aumento do preço de um bem deixar o consumo inalterado, " + hl("a demanda por") + " esse "
                      "bem " + hl("terá elasticidade-preço nula (perfeitamente inelástica), sem que isso permita "
                              "classificá-lo como normal ou inferior") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": ["deverá"], "dificuldade": 1,
        "comentario_fonte": "Consumo inalterado com alta de preço indica bem essencial com elasticidade-preço "
                            "zero; bem normal se refere à relação renda × consumo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_nao_identificada: a fonte traz só “C/E (2018)”"],
    },
    # ------------------------------------------------------------------ E1-0197
    {
        "id": "ECO-E1-0197-1", "fonte_ref": "E1-0197", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Simulado Clipping", "prova": "07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-preço da demanda é uma medida da sensibilidade da quantidade ofertada de um "
                      "bem ou serviço em relação às mudanças em seu preço, e é influenciada pela disponibilidade "
                      "de substitutos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elasticidade-preço da demanda é uma medida da sensibilidade da quantidade ")
                    + vm("ofertada") + az(" de um bem ou serviço em relação às mudanças em seu preço, e é "
                                         "influenciada pela disponibilidade de substitutos.")),
        "poucas": ("A elasticidade-preço da <b>demanda</b> mede a sensibilidade da quantidade "
                   + azb("demandada") + " ao preço. A segunda parte (substitutos) está certa."),
        "destrinchando": [
            "Definição: " + vd("ε = %ΔQᴰ / %ΔP") + ", negativa pela lei da demanda (costuma-se trabalhar em "
            "módulo). Sensibilidade da quantidade <b>ofertada</b> ao preço é a " + azb("elasticidade-preço da "
            "oferta") + ", positiva.",
            "Determinantes da elasticidade-preço da demanda (lista de " + oc("Mankiw") + "): (1) "
            + azb("substitutos próximos") + " — quanto mais, mais elástica; (2) necessidade × luxo — "
            "necessidades são inelásticas; (3) " + azb("definição do mercado") + " — mercados estreitos "
            "(sorvete de baunilha) são mais elásticos que amplos (alimentos); (4) " + azb("horizonte de tempo")
            + " — mais elástica no longo prazo. Muitos manuais acrescentam o " + azb("peso no orçamento") + ".",
            "Por que substitutos importam: se o preço sobe e há alternativa próxima, o consumidor migra; a "
            "quantidade cai muito em relação ao preço.",
            "Determinantes da elasticidade da oferta são outros: flexibilidade da produção, capacidade ociosa, "
            "tempo de ajuste.",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Uma palavra trocada (“ofertada” por "
                       "“demandada”) no meio de uma frase que, de resto, é definição de manual — e a segunda "
                       "oração verdadeira dá ar de correção ao conjunto. Leitura palavra a palavra resolve."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-preço da demanda tende a ser maior quanto mais substitutos próximos o bem "
            "tiver.”</i> → CERTO",
            "<i>“A elasticidade-preço da demanda independe da disponibilidade de substitutos, dependendo apenas "
            "do peso do bem no orçamento.”</i> → ERRADO (restrição indevida)",
        ])],
        "reescrita": ("A elasticidade-preço da demanda é uma medida da sensibilidade da quantidade "
                      + hl("demandada") + " de um bem ou serviço em relação às mudanças em seu preço, e é "
                      "influenciada pela disponibilidade de substitutos."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Confunde elasticidade-preço da demanda com a da oferta; a influência dos "
                            "substitutos está correta.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0203
    {
        "id": "ECO-E1-0203-1", "fonte_ref": "E1-0203", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "MPE/TO/Analista Ministerial/2006", "ano": 2006,
        "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Se a elasticidade da demanda de serviços jurídicos for unitária, então, um aumento de "
                      "preços elevará a receita total com esses serviços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se a elasticidade da demanda de serviços jurídicos for unitária, então, um aumento de "
                       "preços ") + vm("elevará") + az(" a receita total com esses serviços.")),
        "poucas": ("Com " + vd("|ε| = 1") + ", a queda percentual da quantidade iguala a alta percentual do "
                   "preço: a " + azb("receita total fica constante") + "."),
        "destrinchando": [
            "RT = P × Q. Em termos percentuais (variações pequenas): %ΔRT ≈ %ΔP + %ΔQ = %ΔP·(1 − |ε|). Com "
            + vd("|ε| = 1") + ", %ΔRT = 0.",
            "Tabela do " + azb("teste da receita total") + ": |ε| > 1 (elástica) → P e RT em sentidos "
            "<b>opostos</b>; |ε| < 1 (inelástica) → P e RT no <b>mesmo</b> sentido; |ε| = 1 → RT não muda.",
            "A demanda com |ε| = 1 em todos os pontos é a hipérbole equilátera P·Q = constante: qualquer "
            "retângulo sob a curva tem a mesma área. Numa demanda <b>linear</b>, |ε| = 1 só vale no ponto "
            "médio, onde a RT é máxima — ali, uma pequena alta de preço deixa a receita praticamente igual "
            "(e não a eleva).",
            "Exemplo: P de 5 para 10 (+100%) e Q de 4 para 2 (−50%) na hipérbole P·Q = 20: receita 20 nos dois "
            "casos. (Em variações grandes, use a fórmula do ponto médio para a elasticidade.)",
            vm("Regra-âncora: só a demanda inelástica faz a receita subir com o preço."),
        ],
        "grafico_verso": "ECO-E1-0203-1-V1",
        "dissecando": (cz("[troca de conceito]") + " Atribui à demanda unitária o comportamento da inelástica. "
                       "🔥 O CEBRASPE cobra a tabela de três casas do teste da receita com contextos variados "
                       "(serviços jurídicos, transporte, medicamentos): basta localizar o caso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a demanda por serviços jurídicos for inelástica, um aumento de preços elevará a receita "
            "total com esses serviços.”</i> → CERTO",
            "<i>“Se a demanda for elástica, uma redução de preços reduzirá a receita total.”</i> → ERRADO "
            "(inversão: a receita aumenta)",
        ])],
        "reescrita": ("Se a elasticidade da demanda de serviços jurídicos for unitária, então, um aumento de "
                      "preços " + hl("manterá inalterada") + " a receita total com esses serviços."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A receita permanece constante; só aumenta se a demanda for inelástica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (53).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (verso; substituída por ECO-E1-0203-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0278
    {
        "id": "ECO-E1-0278-1", "fonte_ref": "E1-0278", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda e à receita.",
        "rotulo_item": "Item",
        "assertiva": ("Quando o módulo da elasticidade preço da demanda de um produto for inferior a um, um "
                      "aumento no seu preço tenderá a reduzir a receita do monopolista."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quando o módulo da elasticidade preço da demanda de um produto for inferior a um, um "
                       "aumento no seu preço tenderá a ") + vm("reduzir") + az(" a receita do monopolista.")),
        "poucas": ("Com " + vd("|ε| < 1") + " (demanda inelástica), a quantidade cai proporcionalmente menos "
                   "do que o preço sobe: a receita <b>aumenta</b>."),
        "destrinchando": [
            "%ΔRT ≈ %ΔP·(1 − |ε|). Se |ε| < 1, o parêntese é positivo: preço e receita andam no " + azb("mesmo "
            "sentido") + ". Ex.: |ε| = 0,4 e preço +10% → quantidade −4% → receita ≈ +6%.",
            "Ligação com a " + azb("receita marginal") + ": RMg = P·(1 − 1/|ε|). Com |ε| < 1, RMg < 0 — vender "
            "uma unidade a mais (baixando o preço) <b>reduz</b> a receita; vender uma a menos (subindo o preço) "
            "a aumenta.",
            "Consequência: um monopolista maximizador de lucro " + vm("nunca opera no trecho inelástico")
            + " da demanda. Lá, subir o preço aumenta a receita e reduz a quantidade (e o custo): o lucro sobe "
            "com certeza. Ele só para onde RMg = CMg > 0, isto é, onde |ε| > 1.",
            "Origem da inelasticidade: poucos substitutos, fidelidade à marca, bem essencial — fatores que dão "
            "ao vendedor " + azb("poder de mercado") + ". O índice de " + oc("Lerner") + " mede esse poder: "
            "(P − CMg)/P = 1/|ε|.",
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido do efeito na receita. A menção ao “monopolista” é "
                       "distração: o teste da receita total vale para qualquer vendedor. Pista: “inferior a um” "
                       "= inelástica = preço e receita juntos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopolista maximizador de lucro opera sempre no trecho elástico da curva de demanda.”</i> → "
            "CERTO",
            "<i>“Quando |ε| > 1, um aumento de preço eleva a receita do monopolista.”</i> → ERRADO (inversão: "
            "na demanda elástica a receita cai)",
        ])],
        "reescrita": ("Quando o módulo da elasticidade preço da demanda de um produto for inferior a um, um "
                      "aumento no seu preço tenderá a " + hl("elevar") + " a receita do monopolista."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tenderá"], "dificuldade": 1,
        "comentario_fonte": "|ε| < 1 indica bem pouco sensível ao preço; elevar o preço aumenta a receita, pois "
                            "a quantidade cai pouco.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_nao_identificada: a fonte traz só “C/E (2018)”"],
    },
    # ------------------------------------------------------------------ E1-0630
    {
        "id": "ECO-E1-0630-1", "fonte_ref": "E1-0630", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Simulado Set/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-renda da demanda.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("Se um consumidor gasta toda a sua renda em apenas dois bens, é possível que ambos sejam "
                      "bens de luxo, isto é, que ambos tenham elasticidade-renda da demanda maior que um."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se um consumidor gasta toda a sua renda em apenas dois bens, ") + vm("é possível")
                    + az(" que ambos sejam bens de luxo, isto é, que ambos tenham elasticidade-renda da demanda "
                         "maior que um.")),
        "poucas": ("Da restrição orçamentária sai a " + azb("condição de agregação de Engel") + ": "
                   + vd("s₁η₁ + s₂η₂ = 1") + ", com s = parcela da renda gasta em cada bem. Se os dois η "
                   "fossem maiores que 1, a soma passaria de 1."),
        "destrinchando": [
            "Dedução: se toda a renda é gasta, p₁x₁ + p₂x₂ = R. Derivando em relação a R (preços fixos) e "
            "multiplicando por R/R: " + vd("Σ sᵢ·ηᵢ = 1") + ", em que sᵢ = pᵢxᵢ/R e Σ sᵢ = 1. A média "
            "ponderada das elasticidades-renda é exatamente 1.",
            "Consequências: (1) " + vm("nem todos os bens podem ser de luxo") + " (η > 1) — nem todos podem "
            "ser inferiores ou necessários; (2) com dois bens, se um é inferior (η < 0), o outro tem de ser "
            "de luxo; (3) se um tem η = 1, o outro também tem.",
            "Intuição: um aumento de 10% na renda aumenta o gasto total em exatamente 10%. Se ambos os bens "
            "crescessem mais de 10%, o consumidor gastaria mais do que ganhou.",
            "Classificação: η < 0 inferior; 0 < η < 1 normal necessário; η > 1 de luxo (superior). A "
            + oc("lei de Engel") + " — alimentação com η < 1 — é o exemplo empírico clássico.",
        ],
        "dissecando": (cz("[outro: impossibilidade lógica]") + " O item parece plausível porque cada bem, "
                       "isoladamente, pode ser de luxo; o erro está no “ambos”, que viola a restrição "
                       "orçamentária. Pista: sempre que a banca disser que <b>todos</b> os bens de uma cesta "
                       "têm a mesma classificação-limite, verifique a agregação de Engel."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o consumidor gasta toda a renda em dois bens e um deles é inferior, o outro é "
            "necessariamente de luxo.”</i> → CERTO",
            "<i>“A soma simples das elasticidades-renda de todos os bens consumidos é igual a 1.”</i> → ERRADO "
            "(falta a ponderação pela parcela da renda)",
        ])],
        "reescrita": ("Se um consumidor gasta toda a sua renda em apenas dois bens, " + hl("não é possível")
                      + " que ambos sejam bens de luxo, isto é, que ambos tenham elasticidade-renda da demanda "
                      "maior que um" + hl(", pois a média das elasticidades-renda, ponderada pelas parcelas da "
                                          "renda, é igual a um") + "."),
        "tipo_erro": ["OUTRO", "GENERALIZACAO"], "moduladores": ["ambos", "é possível"], "dificuldade": 2,
        "comentario_fonte": "A soma das elasticidades-renda ponderadas pela participação dos gastos na renda é "
                            "1; não seria possível ter dois bens de luxo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (179).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto reconstruído pelo comentário"}],
        "alertas": ["texto_reconstruido: frente original era só imagem (image (179).png); assertiva "
                    "reconstruída a partir do comentário, que refuta a possibilidade de dois bens de luxo pela "
                    "agregação de Engel — redação exata do simulado não localizada; conferir com a imagem",
                    "tipo_erro OUTRO: impossibilidade lógica (agregação de Engel)"],
    },
    # ------------------------------------------------------------------ E1-0956
    {
        "id": "ECO-E1-0956-1", "fonte_ref": "E1-0956", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço cruzada da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("A capacidade de um país produtor de uma commodity controlar o preço desse bem no mercado "
                      "internacional é menor, quanto menor for a elasticidade preço cruzada da demanda entre o "
                      "produto oferecido por ele e o produto oferecido pelos demais países ofertantes desse "
                      "mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A capacidade de um país produtor de uma commodity controlar o preço desse bem no mercado "
                       "internacional é ") + vm("menor") + az(", quanto menor for a elasticidade preço cruzada "
                                                              "da demanda entre o produto oferecido por ele e o "
                                                              "produto oferecido pelos demais países ofertantes "
                                                              "desse mercado.")),
        "poucas": ("Elasticidade cruzada " + azb("baixa") + " = o produto do país é mal substituído pelo dos "
                   "concorrentes = " + azb("mais") + " poder de fixar preço. A relação é inversa."),
        "destrinchando": [
            azb("Elasticidade-preço cruzada") + ": " + vd("ε<sub>AB</sub> = %ΔQ<sub>A</sub> / %ΔP<sub>B</sub>")
            + ". Positiva → substitutos; negativa → complementares; quanto maior (positiva), mais próximos "
            "os substitutos.",
            "Raciocínio: se o país eleva o preço da sua soja e a demanda pela soja dos concorrentes dispara "
            "(cruzada alta), os compradores fogem — ele é " + azb("tomador de preço") + ". Se a demanda pelos "
            "concorrentes quase não reage (cruzada baixa), os compradores ficam — ele tem "
            + azb("poder de mercado") + ".",
            "Commodities homogêneas (soja, minério padronizado) tendem a ter cruzada altíssima entre "
            "origens: por isso a maioria dos exportadores, inclusive o " + rx("Brasil") + ", é tomadora de "
            "preço nesses mercados. Diferenciação (qualidade, certificação, logística) reduz a cruzada.",
            "Em defesa da concorrência, a cruzada ajuda a delimitar o " + azb("mercado relevante") + ": "
            "produtos com cruzada alta disputam o mesmo mercado.",
            vm("Regra-âncora: mais substituível → menos poder de preço."),
        ],
        "dissecando": (cz("[inversão]") + " A frase mantém a estrutura “quanto menor…, menor…”, que soa "
                       "natural, mas a relação correta é inversa (“quanto menor a cruzada, maior o controle”). "
                       "🔥 Correlações do tipo “quanto mais/menos” pedem que se confira o sentido de cada "
                       "ponta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a elasticidade-preço cruzada entre a commodity de um país e a dos concorrentes, "
            "mais competitivo é o mercado e menor o poder de preço desse país.”</i> → CERTO",
            "<i>“Elasticidade-preço cruzada negativa entre os produtos de dois países indica que são "
            "substitutos.”</i> → ERRADO (troca de conceito: negativa = complementares)",
        ])],
        "reescrita": ("A capacidade de um país produtor de uma commodity controlar o preço desse bem no mercado "
                      "internacional é " + hl("maior") + ", quanto menor for a elasticidade preço cruzada da "
                      "demanda entre o produto oferecido por ele e o produto oferecido pelos demais países "
                      "ofertantes desse mercado."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["quanto menor"], "dificuldade": 2,
        "comentario_fonte": "É o contrário: cruzada baixa → produto pouco substituível → maior controle do "
                            "preço; cruzada alta → mercado competitivo, menor controle.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (314).png", "tipo_fonte": "TEXTO/GRÁFICO", "lado": "verso",
                           "acao": FIG_E1_PERDIDA}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00011
    {
        "id": "ECO-E2-L00011-1", "fonte_ref": "E2-L00011", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade renda da demanda para bens duráveis é maior no curto prazo, pois ao receber "
                      "um aumento de renda, os consumidores tendem a alocar parte significativa de seus ganhos na "
                      "aquisição desses bens, uma vez que representam uma proporção elevada em seus orçamentos. "
                      "Isso pode resultar em um aumento mais acentuado na demanda, mesmo frente a elevações "
                      "consideráveis nos preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elasticidade renda da demanda para <u>bens duráveis é maior no curto prazo</u>, pois ao "
                      "receber um aumento de renda, os consumidores tendem a alocar parte significativa de seus "
                      "ganhos na aquisição desses bens, uma vez que representam uma proporção elevada em seus "
                      "orçamentos. Isso pode resultar em um aumento mais acentuado na demanda, mesmo frente a "
                      "elevações consideráveis nos preços."),
        "poucas": ("Para " + azb("duráveis") + " (carros, geladeiras), a resposta da demanda à renda é "
                   "<b>maior no curto prazo</b>: quem enriquece antecipa a compra para ajustar o estoque desejado; "
                   "depois, as compras voltam ao ritmo de reposição."),
        "destrinchando": [
            "Mecanismo de " + oc("Pindyck e Rubinfeld") + " (<i>Microeconomia</i>): o consumidor deseja um "
            + azb("estoque") + " de bens duráveis proporcional à renda. Um aumento de renda eleva o estoque "
            "desejado e provoca um <b>pico</b> de compras (troca do carro, segundo carro); ajustado o estoque, a "
            "demanda anual volta a ser só reposição. Por isso a elasticidade-renda de curto prazo é maior.",
            "Para a " + azb("maioria dos bens não duráveis") + " (e serviços) vale o oposto: o consumo se "
            "ajusta aos poucos ao novo padrão de vida, e a elasticidade-renda é maior no longo prazo.",
            "O mesmo raciocínio vale para a elasticidade-<b>preço</b> de duráveis: uma alta de preço faz "
            "adiar a troca (queda forte no curto prazo), mas, como o estoque se deprecia, a reposição volta — "
            "demanda mais elástica no curto que no longo prazo, ao contrário dos não duráveis (gasolina).",
            "Ressalvas de redação: a justificativa do item (“proporção elevada no orçamento”) não é o "
            "mecanismo central, e a cauda “mesmo frente a elevações consideráveis nos preços” mistura efeito "
            "preço com efeito renda. O núcleo julgado — duráveis com elasticidade-renda maior no curto prazo — "
            "está correto.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " Contraria a regra geral “elasticidades crescem com "
                       "o tempo”: duráveis são a exceção clássica. Pista: o par de itens do bloco (duráveis × "
                       "não duráveis) testa exatamente esse contraste."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-renda da demanda por automóveis tende a ser maior no longo prazo do que no "
            "curto prazo.”</i> → ERRADO (inversão: é maior no curto prazo, pelo ajuste de estoque)",
            "<i>“Para a maioria dos bens não duráveis, a elasticidade-renda da demanda é maior no longo "
            "prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["tendem", "pode"], "dificuldade": 2,
        "comentario_fonte": "Em duráveis, o aumento de renda leva a alocar mais rendimento na compra no curto "
                            "prazo; a elasticidade-renda é mais alta no curto prazo.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem atribui o efeito ao alto valor dos bens; o "
                    "mecanismo do manual é o ajuste do estoque desejado — corrigido no 📖"],
    },
    # ------------------------------------------------------------------ E2-L00012
    {
        "id": "ECO-E2-L00012-1", "fonte_ref": "E2-L00012", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Com relação aos bens não duráveis, a elasticidade renda da demanda tende a ser maior no "
                      "longo prazo, pois ao decorrer do tempo, os consumidores ajustam seus padrões de consumo e "
                      "exploram opções que maximizam sua utilidade, aumentando a proporção de consumo desses bens "
                      "em seus orçamentos conforme a renda cresce."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com relação aos bens não duráveis, a elasticidade renda da demanda <u>tende a ser maior "
                      "no longo prazo</u>, pois ao decorrer do tempo, os consumidores ajustam seus padrões de "
                      "consumo e exploram opções que maximizam sua utilidade, aumentando a proporção de consumo "
                      "desses bens em seus orçamentos conforme a renda cresce."),
        "poucas": ("Para não duráveis e serviços, o consumo se adapta à nova renda <b>gradualmente</b>: a "
                   "elasticidade-renda de " + azb("longo prazo") + " supera a de curto prazo."),
        "destrinchando": [
            "Por que a resposta é lenta: hábitos, informação e decisões complementares (mudar de bairro, "
            "comprar carro maior) levam tempo. Exemplo de " + oc("Pindyck e Rubinfeld") + ": com renda maior, "
            "o consumo de gasolina cresce pouco no início e mais depois, quando as famílias compram carros "
            "maiores e passam a rodar mais.",
            "Contraste com " + azb("duráveis") + ": ali a elasticidade-renda é maior no curto prazo, porque o "
            "aumento de renda dispara compras para ajustar o estoque desejado; depois, só reposição.",
            "Regra geral de prazos: para a maioria dos bens, " + vd("elasticidades (preço e renda) crescem com o "
            "horizonte") + "; as exceções clássicas são os duráveis.",
            "Ressalva de redação: “aumentando a proporção desses bens no orçamento” só vale para bens com "
            "elasticidade-renda maior que 1; para necessidades (alimentos), a parcela cai com a renda (lei de "
            "Engel), ainda que o ajuste de longo prazo seja maior que o de curto. O núcleo do item (maior no "
            "longo prazo) é o que decide.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " “Tende a ser” protege o item de "
                       "contraexemplos. Quem decorou só “duráveis: curto prazo” pode inverter e marcar ERRADO — "
                       "foi o erro registrado nesta questão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para bens não duráveis, a elasticidade-renda da demanda é necessariamente igual no curto e no "
            "longo prazo.”</i> → ERRADO (modulador absoluto e conteúdo trocado)",
            "<i>“Bens duráveis constituem exceção à regra de que as elasticidades crescem com o prazo.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": "Não duráveis mostram elasticidade-renda mais alta no longo prazo, à medida que "
                            "os consumidores ajustam as despesas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00013
    {
        "id": "ECO-E2-L00013-1", "fonte_ref": "E2-L00013", "destino": "02", "subtema": H2["of"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade preço da oferta unitária implica que a quantidade ofertada varia na mesma "
                      "proporção que o preço do produto. Assim, um aumento de 20% no preço geraria um aumento de "
                      "20% na quantidade ofertada, não alterando a receita total do vendedor, já que o aumento na "
                      "quantidade ofertada compensa exatamente o aumento no preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elasticidade preço da oferta unitária implica que a quantidade ofertada varia na mesma "
                       "proporção que o preço do produto. Assim, um aumento de 20% no preço geraria um aumento de "
                       "20% na quantidade ofertada, ") + vm("não alterando a receita total do vendedor, já que o "
                                                           "aumento na quantidade ofertada compensa exatamente o "
                                                           "aumento no preço") + az(".")),
        "poucas": ("Na oferta, P e Q sobem <b>juntos</b>: com +20% em cada, a receita vai a 1,2 × 1,2 = "
                   + vd("1,44") + " — alta de 44%. “Receita constante” é propriedade da " + azb("demanda "
                   "unitária") + ", onde P e Q andam em sentidos opostos."),
        "destrinchando": [
            "RT = P × Q. Se P → 1,2P e Q → 1,2Q, RT → " + vd("1,44·PQ") + ". Ex.: P de 10 para 12 e Q de 100 "
            "para 120: receita de 1.000 para 1.440. “Compensar” exigiria que um fator subisse e o outro caísse.",
            "O " + azb("teste da receita total") + " é da demanda: |ε| > 1 → P e RT em sentidos opostos; |ε| < 1 "
            "→ mesmo sentido; " + vd("|ε| = 1 → RT constante") + ".",
            "Sutileza: a receita depende da quantidade <b>vendida</b>, não só da ofertada. Ao longo da curva de "
            "oferta (por exemplo, quando a demanda se desloca e eleva o preço), a quantidade transacionada sobe "
            "com o preço; o tamanho do efeito sobre a receita depende de como a demanda se move — a "
            "elasticidade da oferta, sozinha, não garante receita constante.",
            "Primeira frase do item está certa: " + vd("εˢ = 1") + " ⇔ %ΔQˢ = %ΔP. Toda oferta linear que "
            "passa pela origem tem εˢ = 1 em todos os pontos.",
            vm("Regra-âncora: efeitos preço e quantidade se anulam na demanda unitária; na oferta, se somam."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A definição de oferta unitária está "
                       "correta; o erro foi enxertado na conclusão, que transplanta para a oferta o teste da "
                       "receita da demanda. Pista: “compensa” supõe sentidos opostos, mas o próprio item diz que "
                       "os dois aumentam."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com demanda de elasticidade unitária, um aumento de 20% no preço reduz a quantidade em cerca "
            "de 20% e deixa a receita praticamente inalterada.”</i> → CERTO",
            "<i>“Com oferta unitária, um aumento de 20% no preço eleva a receita do vendedor em 20%.”</i> → "
            "ERRADO (dado alterado: ≈ 44%)",
        ])],
        "reescrita": ("A elasticidade preço da oferta unitária implica que a quantidade ofertada varia na mesma "
                      "proporção que o preço do produto. Assim, um aumento de 20% no preço geraria um aumento de "
                      "20% na quantidade ofertada, " + hl("elevando a receita total do vendedor (vendidas essas "
                                                          "quantidades, em cerca de 44%), já que preço e "
                                                          "quantidade aumentam juntos") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["exatamente"], "dificuldade": 2,
        "comentario_fonte": "Várias respostas empilhadas: receita constante com elasticidade unitária é "
                            "propriedade da demanda; na oferta, P e Q sobem juntos (1,2 × 1,2 = 1,44); a receita "
                            "depende da quantidade vendida, governada pela demanda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 001", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 002", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00014
    {
        "id": "ECO-E2-L00014-1", "fonte_ref": "E2-L00014", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade renda da demanda para bens não duráveis diminui no curto prazo, uma vez que, "
                      "apesar de um aumento de renda, os consumidores não têm a necessidade imediata de aumentar "
                      "seu consumo desses bens, sendo que a proporção dotada para estes bens nos orçamentos tende "
                      "a se estabilizar rapidamente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elasticidade renda da demanda para bens não duráveis ") + vm("diminui")
                    + az(" no curto prazo, uma vez que, apesar de um aumento de renda, os consumidores não têm a "
                         "necessidade imediata de aumentar seu consumo desses bens, ")
                    + vm("sendo que a proporção dotada para estes bens nos orçamentos tende a se estabilizar "
                         "rapidamente") + az(".")),
        "poucas": ("A elasticidade-renda dos não duráveis não “diminui” no curto prazo: ela é " + azb("menor")
                   + " no curto que no longo prazo porque o ajuste é <b>lento</b>, não porque a parcela no "
                   "orçamento se estabilize rápido."),
        "destrinchando": [
            "Leitura correta: elasticidade de curto prazo < elasticidade de longo prazo. É uma comparação entre "
            "horizontes, não um movimento de queda ao longo do tempo.",
            "Mecanismo: hábitos, contratos e decisões complementares demoram a mudar. Com mais renda, o consumo "
            "de não duráveis cresce pouco de imediato e mais depois — se a parcela no orçamento se estabilizasse "
            "rapidamente, não haveria diferença entre curto e longo prazo.",
            "Contraste com " + azb("duráveis") + ": elasticidade-renda maior no curto prazo (pico de compras para "
            "ajustar o estoque desejado) e menor no longo (" + oc("Pindyck e Rubinfeld") + ").",
            "Mesma lógica para a elasticidade-preço: não duráveis (gasolina) são mais inelásticos no curto "
            "prazo e mais elásticos no longo.",
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " Parte verdadeira — a resposta de curto prazo "
                       "é baixa — com dois enxertos: o verbo “diminui” (sugere queda, quando o certo é ser "
                       "menor que no longo prazo) e a causa (estabilização rápida), que contradiz o próprio "
                       "mecanismo de ajuste lento. 🔥 Itens de Bozan costumam errar pela justificativa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-renda da demanda por bens não duráveis é, em regra, menor no curto prazo do que "
            "no longo prazo, porque os consumidores levam tempo para ajustar seus padrões de consumo.”</i> → "
            "CERTO",
            "<i>“A elasticidade-renda dos bens não duráveis é maior no curto prazo, como ocorre com os "
            "duráveis.”</i> → ERRADO (inversão: só os duráveis têm curto prazo maior)",
        ])],
        "reescrita": ("A elasticidade renda da demanda para bens não duráveis " + hl("é menor") + " no curto prazo "
                      + hl("do que no longo") + ", uma vez que, apesar de um aumento de renda, os consumidores "
                      "não têm a necessidade imediata de aumentar seu consumo desses bens, " + hl("e o ajuste "
                                                                                                 "do padrão de "
                                                                                                 "consumo à nova "
                                                                                                 "renda é "
                                                                                                 "gradual") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": ["tende a", "rapidamente"],
        "dificuldade": 3,
        "comentario_fonte": "No curto prazo a elasticidade-renda de não duráveis é baixa, mas não “diminui” por "
                            "estabilização orçamentária; é naturalmente menor que no longo prazo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["gabarito de fronteira: o item é ERRADO pela redação (“diminui”) e pela justificativa; o "
                    "fato de a elasticidade de curto prazo ser baixa é verdadeiro"],
    },
    # ------------------------------------------------------------------ E2-L00415
    {
        "id": "ECO-E2-L00415-1", "fonte_ref": "E2-L00415", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARMS,
        "rotulo_item": "Item",
        "assertiva": ("Mesmo que muitos consumidores classifiquem um bem como “necessário”, a demanda agregada "
                      "pode ser inelástica se, no mercado relevante, houver muitos substitutos próximos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Mesmo que muitos consumidores classifiquem um bem como “necessário”, a demanda agregada "
                       "pode ser ") + vm("inelástica") + az(" se, no mercado relevante, houver muitos substitutos "
                                                            "próximos.")),
        "poucas": ("Muitos " + azb("substitutos próximos") + " tornam a demanda <b>elástica</b>, ainda que a "
                   "categoria seja vista como necessária: a necessidade é da categoria, não da marca ou da "
                   "variedade."),
        "destrinchando": [
            "Substitutos próximos são o determinante mais forte da elasticidade-preço: se o preço de um item "
            "sobe, o consumidor troca por outro quase igual, e a quantidade cai muito.",
            "Necessário × substituível: “comida” é necessária e inelástica; “arroz da marca X” é necessário "
            "para quem o consome, mas tem dezenas de substitutos — demanda elástica. O que decide é o "
            + azb("escopo do mercado") + " em que a elasticidade é medida.",
            "A estrutura correta seria concessiva: <i>mesmo</i> sendo necessário, o bem pode ter demanda "
            "<b>elástica</b> se houver muitos substitutos. O item usa a concessão (“mesmo que”) e conclui no "
            "sentido que dispensaria a concessão.",
            "Outros determinantes (" + oc("Mankiw") + "): necessidade × luxo, definição do mercado, horizonte "
            "temporal; e peso no orçamento.",
        ],
        "dissecando": (cz("[inversão]") + " O conector concessivo “mesmo que” anuncia um resultado contrário ao "
                       "esperado de um bem necessário (inelástico) — o certo seria “elástica”. A palavra "
                       "trocada é justamente a conclusão. Pista: conferir se a conclusão faz sentido com a "
                       "concessão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Mesmo que muitos consumidores classifiquem um bem como necessário, a demanda pode ser elástica "
            "se, no mercado relevante, houver muitos substitutos próximos.”</i> → CERTO",
            "<i>“Bens necessários têm, sempre, demanda inelástica.”</i> → ERRADO (modulador absoluto)",
        ])],
        "reescrita": ("Mesmo que muitos consumidores classifiquem um bem como “necessário”, a demanda agregada "
                      "pode ser " + hl("elástica") + " se, no mercado relevante, houver muitos substitutos "
                      "próximos."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["mesmo que", "pode"], "dificuldade": 2,
        "comentario_fonte": "Determinantes centrais: substitutos próximos e definição do mercado (escopo).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00416
    {
        "id": "ECO-E2-L00416-1", "fonte_ref": "E2-L00416", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARMS,
        "rotulo_item": "Item",
        "assertiva": ("Quanto mais estreita a definição do mercado, menor tende a ser a elasticidade-preço da "
                      "demanda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quanto mais estreita a definição do mercado, ") + vm("menor") + az(" tende a ser a "
                                                                                          "elasticidade-preço da "
                                                                                          "demanda.")),
        "poucas": ("Mercado " + azb("estreito") + " (uma marca, uma variedade) tem muitos substitutos próximos "
                   "fora dele: a demanda é <b>mais</b> elástica. Mercado amplo (alimentos, energia) tem poucos "
                   "substitutos: menos elástica."),
        "destrinchando": [
            "Exemplo de " + oc("Mankiw") + ": “alimentos” → demanda inelástica; “sorvete” → mais elástica; "
            "“sorvete de baunilha” → muito elástica (os outros sabores são substitutos quase perfeitos).",
            "A elasticidade é sempre de um " + azb("mercado definido") + ": ao estreitar o recorte, os "
            "substitutos que antes estavam “dentro” passam a estar “fora” e competem pela demanda.",
            "Aplicação em " + azb("defesa da concorrência") + ": no teste do monopolista hipotético, delimita-se "
            "o menor conjunto de produtos em que um aumento de preço pequeno e duradouro seria lucrativo — "
            "mercados estreitos demais falham no teste justamente por serem muito elásticos. No " + rx("Brasil")
            + ", a metodologia é usada pelo CADE.",
            vm("Regra-âncora: mercado estreito → mais substitutos → mais elástico."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido da relação (“menor” por “maior”). O modulador "
                       "“tende a” é legítimo e não salva o item. Pista: imaginar o caso extremo — uma única "
                       "marca entre dezenas iguais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda por alimentos em geral tende a ser menos elástica que a demanda por uma marca "
            "específica de biscoito.”</i> → CERTO",
            "<i>“A elasticidade-preço da demanda independe de como o mercado é delimitado.”</i> → ERRADO "
            "(contradição com o determinante “definição do mercado”)",
        ])],
        "reescrita": ("Quanto mais estreita a definição do mercado, " + hl("maior") + " tende a ser a "
                      "elasticidade-preço da demanda."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "É o oposto: recortes mais restritos têm mais substitutos próximos e maior "
                            "elasticidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00417
    {
        "id": "ECO-E2-L00417-1", "fonte_ref": "E2-L00417", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARMS,
        "rotulo_item": "Item",
        "assertiva": ("A mesma demanda pode parecer inelástica no curto prazo e mais elástica no longo, o que "
                      "implica que choques de preço podem exigir respostas de política diferentes ao longo do "
                      "tempo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A mesma demanda pode parecer <u>inelástica no curto prazo e mais elástica no longo</u>, "
                      "o que implica que choques de preço podem exigir respostas de política diferentes ao longo "
                      "do tempo."),
        "poucas": ("Com tempo, o consumidor encontra " + azb("substitutos") + " e muda hábitos e "
                   "equipamentos: a elasticidade-preço cresce com o horizonte, e a política deve considerar "
                   "efeitos distintos no curto e no longo prazo."),
        "destrinchando": [
            "Exemplo clássico: combustíveis. Num choque de preço, quase não se reduz o uso no curto prazo (o "
            "carro e o trajeto são os mesmos); no longo, compram-se carros econômicos, muda-se de casa, "
            "migra-se para transporte público ou etanol.",
            "Implicações de política: (1) " + azb("tributos") + " sobre bens inelásticos arrecadam bem no "
            "curto prazo, mas a base encolhe com o tempo; (2) choques de oferta (como os do petróleo nos anos "
            "1970) geram alta forte de preço e receita no curto prazo, que se atenua quando a demanda se "
            "ajusta; (3) " + azb("subsídios temporários") + " a preços amortecem o curto prazo, mas adiam o "
            "ajuste.",
            "Exceção a lembrar: bens " + azb("duráveis") + " (carros, eletrodomésticos) costumam ser mais "
            "elásticos no curto prazo — adiar a troca é fácil, mas a reposição volta.",
            "“Pode parecer” e “podem exigir” são moduladores relativos que tornam o item seguro.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Reproduz o determinante “horizonte de "
                       "tempo” e acrescenta uma consequência prudente. Os “pode” blindam o item contra a exceção "
                       "dos duráveis."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-preço da demanda por gasolina tende a ser maior no curto prazo do que no longo "
            "prazo.”</i> → ERRADO (inversão)",
            "<i>“Toda demanda é mais elástica no longo prazo do que no curto prazo.”</i> → ERRADO (modulador "
            "absoluto: duráveis são exceção)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode", "podem"],
        "dificuldade": 1,
        "comentario_fonte": "A elasticidade aumenta com o horizonte temporal (ex.: combustíveis).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00418
    {
        "id": "ECO-E2-L00418-1", "fonte_ref": "E2-L00418", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_ARMS,
        "rotulo_item": "Item",
        "assertiva": ("A máxima “demanda elástica significa que uma queda de preço aumenta receita” é universal, "
                      "inclusive para grandes variações, dispensando qualquer cuidado de mensuração."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A máxima “demanda elástica significa que uma queda de preço aumenta receita” ")
                    + vm("é universal, inclusive para grandes variações, dispensando qualquer cuidado de "
                         "mensuração") + az(".")),
        "poucas": ("A regra vale <b>localmente</b>, no trecho em que a demanda é elástica. Em variações grandes a "
                   "elasticidade muda ao longo da curva e precisa ser medida com a " + azb("elasticidade-arco")
                   + " (método do ponto médio)."),
        "destrinchando": [
            "Numa demanda linear, a metade superior é elástica e a inferior, inelástica. Uma queda de preço "
            "<b>grande</b> que atravesse o ponto médio pode primeiro aumentar e depois reduzir a receita — o "
            "resultado líquido depende do trecho percorrido.",
            "Assimetria da fórmula simples: de P = 10 para 8 é −20%; de 8 para 10 é +25%. A mesma mudança dá "
            "elasticidades diferentes conforme o sentido. O " + azb("método do ponto médio") + " resolve: "
            + vd("ε = [ΔQ/((Q₁+Q₂)/2)] / [ΔP/((P₁+P₂)/2)]") + ".",
            "Elasticidade-" + azb("ponto") + " (dQ/dP · P/Q) vale para variações infinitesimais; "
            "elasticidade-" + azb("arco") + " é uma média entre dois pontos. Para decisões com mudanças grandes, "
            "o mais seguro é calcular a receita diretamente (P × Q antes e depois).",
            "A regra local continua correta: no ponto em que |ε| > 1, a receita marginal é positiva e uma "
            "pequena queda de preço eleva a receita.",
        ],
        "dissecando": (cz("[modulador absoluto]") + " A regra é verdadeira; o erro está em blindá-la com "
                       "“universal”, “inclusive para grandes variações” e “dispensando qualquer cuidado”. 🔥 "
                       "Moduladores empilhados quase sempre sinalizam ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para variações discretas de preço, recomenda-se o método do ponto médio, que evita que a "
            "elasticidade dependa do sentido da variação.”</i> → CERTO",
            "<i>“Na elasticidade-arco, a variação percentual é calculada sempre em relação ao preço "
            "inicial.”</i> → ERRADO (troca de conceito: usa a média dos dois pontos)",
        ])],
        "reescrita": ("A máxima “demanda elástica significa que uma queda de preço aumenta receita” " + hl("vale "
                      "localmente; para grandes variações, exige cuidado de mensuração, como o uso da "
                      "elasticidade-arco (método do ponto médio)") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["universal", "inclusive", "qualquer"],
        "dificuldade": 1,
        "comentario_fonte": "A regra é local; para variações discretas usa-se elasticidade-arco/ponto médio.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00420
    {
        "id": "ECO-E2-L00420-1", "fonte_ref": "E2-L00420", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": CMD_ARMS,
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-preço cruzada dispensa avaliar delimitação de mercado: positiva indica bens "
                      "substitutos; negativa indica bens complementares, sem ressalvas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elasticidade-preço cruzada ") + vm("dispensa")
                    + az(" avaliar delimitação de mercado: positiva indica bens substitutos; negativa indica bens complementares, ")
                    + vm("sem ressalvas") + az(".")),
        "poucas": ("O " + azb("sinal") + " está certo (positiva → substitutos; negativa → complementares), mas a "
                   "interpretação depende do " + azb("mercado relevante") + " e do contexto da medida: não se "
                   "dispensa delimitação nem ressalvas."),
        "destrinchando": [
            vd("ε<sub>xy</sub> = %ΔQ<sub>x</sub> / %ΔP<sub>y</sub>") + ": > 0 substitutos (etanol × gasolina); "
            "< 0 complementares (carro × gasolina); ≈ 0 independentes.",
            "Por que há ressalvas: (1) o valor depende de quais bens se comparam — a cruzada entre duas marcas "
            "de cerveja é alta; entre “cerveja” e “bebidas” não faz sentido; (2) a cruzada mistura " + azb("efeito "
            "substituição") + " e " + azb("efeito renda") + ": um bem que pesa muito no orçamento pode, ao "
            "encarecer, reduzir a compra de outro mesmo sem complementaridade técnica; (3) a cruzada não é "
            "necessariamente simétrica (ε<sub>xy</sub> ≠ ε<sub>yx</sub>).",
            "Uso prático: em " + azb("defesa da concorrência") + ", cruzadas altas indicam que dois produtos "
            "estão no mesmo mercado relevante — a medida serve para <b>delimitar</b> o mercado, não para "
            "dispensar a delimitação.",
            "Classificação rigorosa (substitutos/complementares <b>líquidos</b> × brutos) usa a demanda "
            "compensada, de " + oc("Hicks") + ", que isola o efeito substituição.",
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " A regra de sinais é verdadeira; o erro "
                       "está nos absolutos “dispensa” e “sem ressalvas”. Quem reconhece a regra de sinais e "
                       "para de ler marca CERTO — foi o erro registrado aqui."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-preço cruzada positiva entre dois bens indica, em regra, que são substitutos, "
            "e é usada na delimitação do mercado relevante.”</i> → CERTO",
            "<i>“Elasticidade-preço cruzada negativa indica que os bens são substitutos.”</i> → ERRADO "
            "(inversão)",
        ])],
        "reescrita": ("A elasticidade-preço cruzada " + hl("não dispensa") + " avaliar delimitação de mercado: "
                      "positiva indica bens substitutos; negativa indica bens complementares, " + hl("mas a "
                      "interpretação depende do escopo do mercado relevante") + "."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["dispensa", "sem ressalvas"],
        "dificuldade": 2,
        "comentario_fonte": "O sinal é esse, mas a interpretação depende do escopo (mercado relevante).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00436
    {
        "id": "ECO-E2-L00436-1", "fonte_ref": "E2-L00436", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_ELAS,
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-preço da demanda por um bem X será maior quanto menor for o número de bens "
                      "substitutos próximos disponíveis no mercado e quanto menor for o peso desse bem no "
                      "orçamento do consumidor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elasticidade-preço da demanda por um bem X será maior quanto ") + vm("menor")
                    + az(" for o número de bens substitutos próximos disponíveis no mercado e quanto ")
                    + vm("menor") + az(" for o peso desse bem no orçamento do consumidor.")),
        "poucas": ("Os dois determinantes estão invertidos: a demanda é " + azb("mais elástica") + " quanto "
                   "<b>mais</b> substitutos próximos houver e quanto <b>maior</b> o peso do bem no orçamento."),
        "destrinchando": [
            azb("Substitutos") + ": com alternativas próximas, uma alta de preço desvia o consumo (manteiga × "
            "margarina). Sem elas, o consumidor fica preso ao bem (sal, insulina).",
            azb("Peso no orçamento") + ": se o bem consome fatia grande da renda (aluguel, carro), uma alta de "
            "preço corrói o poder de compra e força ajuste — demanda mais elástica. Se o peso é ínfimo (sal, "
            "fósforo, palito), dobrar o preço quase não se nota — demanda inelástica.",
            "Lista completa dos determinantes: substitutos, necessidade × luxo, definição do mercado, "
            "horizonte de tempo e peso no orçamento. Todos com o mesmo sentido: tudo o que facilita ou torna "
            "mais vantajoso fugir do bem aumenta a elasticidade.",
            vm("Regra-âncora: mais substitutos, mais peso no orçamento, mais tempo → mais elástica."),
        ],
        "dissecando": (cz("[inversão]") + " Dupla inversão: os dois “menor” deveriam ser “maior”. A estrutura "
                       "“quanto menor…, maior” soa técnica e passa despercebida. Basta testar com um exemplo "
                       "concreto (sal: sem substitutos, peso ínfimo → inelástico)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda por sal tende a ser inelástica, entre outras razões, pelo pequeno peso do bem no "
            "orçamento.”</i> → CERTO",
            "<i>“Quanto maior o peso de um bem no orçamento, menos elástica tende a ser sua demanda.”</i> → "
            "ERRADO (inversão)",
        ])],
        "reescrita": ("A elasticidade-preço da demanda por um bem X será maior quanto " + hl("maior") + " for o "
                      "número de bens substitutos próximos disponíveis no mercado e quanto " + hl("maior") + " for "
                      "o peso desse bem no orçamento do consumidor."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Elasticidade maior quanto MAIOR o número de substitutos e quanto MAIOR o peso no "
                            "orçamento.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00437
    {
        "id": "ECO-E2-L00437-1", "fonte_ref": "E2-L00437", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_ELAS,
        "rotulo_item": "Item",
        "assertiva": ("Se a demanda por um serviço é elástica, uma redução no seu preço resultará em uma queda na "
                      "receita total auferida pelos prestadores desse serviço, pois a variação percentual na "
                      "quantidade demandada será maior que a variação percentual no preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se a demanda por um serviço é elástica, uma redução no seu preço resultará em ")
                    + vm("uma queda") + az(" na receita total auferida pelos prestadores desse serviço, pois a "
                                           "variação percentual na quantidade demandada será maior que a "
                                           "variação percentual no preço.")),
        "poucas": ("Com demanda " + azb("elástica") + ", preço e receita andam em sentidos <b>opostos</b>: "
                   "baixar o preço <b>aumenta</b> a receita. A justificativa do item está certa e leva à "
                   "conclusão contrária."),
        "destrinchando": [
            "|ε| > 1 → %ΔQ > %ΔP, em módulo. Exemplo: preço −10%, quantidade +25% → receita ≈ 0,9 × 1,25 = "
            + vd("1,125") + " (alta de 12,5%).",
            "Resumo do " + azb("teste da receita total") + ": elástica → P↓ Q↑↑ RT↑ e P↑ Q↓↓ RT↓; "
            "inelástica → P↓ Q↑ RT↓ e P↑ Q↓ RT↑; unitária → RT constante.",
            "Aplicação: promoções e tarifas reduzidas fazem sentido para serviços de demanda elástica (lazer, "
            "viagens de turismo, passagens fora de pico); em serviços de demanda inelástica (energia, "
            "transporte essencial), aumentos de tarifa elevam a receita.",
            "Na linguagem da firma: com |ε| > 1, a " + azb("receita marginal") + " é positiva — vender mais "
            "(baixando o preço) aumenta a receita.",
        ],
        "dissecando": (cz("[contradição · inversão]") + " O item traz a premissa correta (variação da "
                       "quantidade maior que a do preço) e tira dela a conclusão oposta. Pista: se Q sobe "
                       "proporcionalmente mais do que P cai, o produto P × Q tem de subir."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a demanda por um serviço é inelástica, uma redução no seu preço resultará em queda da "
            "receita total.”</i> → CERTO",
            "<i>“Se a demanda é elástica, um aumento de preço elevará a receita total.”</i> → ERRADO "
            "(inversão)",
        ])],
        "reescrita": ("Se a demanda por um serviço é elástica, uma redução no seu preço resultará em "
                      + hl("um aumento") + " na receita total auferida pelos prestadores desse serviço, pois a "
                      "variação percentual na quantidade demandada será maior que a variação percentual no "
                      "preço."),
        "tipo_erro": ["CONTRADICAO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Demanda elástica: redução de preço aumenta a receita, porque o aumento percentual "
                            "da quantidade supera a redução percentual do preço.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 067", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00439
    {
        "id": "ECO-E2-L00439-1", "fonte_ref": "E2-L00439", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_ELAS,
        "rotulo_item": "Item",
        "assertiva": ("Se a elasticidade-preço cruzada da demanda entre os bens A e B é negativa, um aumento no "
                      "preço do bem A levará a uma redução na quantidade demandada do bem B, indicando que A e B "
                      "são bens complementares."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a elasticidade-preço cruzada da demanda entre os bens A e B é <u>negativa</u>, um "
                      "aumento no preço do bem A levará a uma <u>redução</u> na quantidade demandada do bem B, "
                      "indicando que A e B são bens <u>complementares</u>."),
        "poucas": ("Cruzada " + vd("negativa") + " = preço de um e quantidade do outro em sentidos opostos = "
                   + azb("complementares") + " (consumidos juntos)."),
        "destrinchando": [
            vd("ε<sub>BA</sub> = %ΔQ<sub>B</sub> / %ΔP<sub>A</sub>") + ". Se P<sub>A</sub> sobe e Q<sub>B</sub> "
            "cai, numerador e denominador têm sinais opostos → ε < 0.",
            "Complementares: café × açúcar, carro × gasolina, impressora × cartucho. Encarecer um torna o "
            "“pacote” mais caro e reduz a compra dos dois. No gráfico do bem B, a demanda se desloca para a "
            "<b>esquerda</b>.",
            "Substitutos: cruzada " + vd("positiva") + " (etanol × gasolina) — encarecer um desvia consumo para "
            "o outro. Independentes: cruzada ≈ 0.",
            "Note que o preço de A aparece no gráfico de B como " + azb("deslocador") + " da curva, e não como "
            "movimento ao longo dela.",
            "Item vizinho (mesma ideia, outra redação): “Um bem é denominado bem complementar se a "
            "elasticidade-preço cruzada da demanda desse bem for negativa” — também CERTO.",
        ],
        "dissecando": (cz("[literalidade]") + " Encadeia definição → mecanismo → classificação, tudo "
                       "coerente. O risco é ler “negativa” e associar a “substitutos” por pressa. 🔥 Regra de "
                       "sinais é cobrada em quase todo bloco de elasticidades."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade-preço cruzada entre A e B é positiva, um aumento no preço de A reduz a "
            "quantidade demandada de B.”</i> → ERRADO (inversão: aumenta; são substitutos)",
            "<i>“Elasticidade-preço cruzada nula indica bens independentes.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Cruzada negativa: aumento do preço de A reduz a quantidade de B; bens "
                            "complementares (café e açúcar).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: o verso da fonte traz, colado ao fim, o enunciado de outra questão (“2. A "
                    "respeito das estruturas de mercado…”) — descartado"],
    },
    # ------------------------------------------------------------------ E2-L00599
    {
        "id": "ECO-E2-L00599-1", "fonte_ref": "E2-L00599", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MICRO3,
        "rotulo_item": "Item",
        "assertiva": "Um bem normal apresenta elasticidade-renda nula.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um bem normal apresenta elasticidade-renda ") + vm("nula") + az("."),
        "poucas": ("Bem " + azb("normal") + " é aquele cujo consumo sobe com a renda: " + vd("η > 0")
                   + ". Elasticidade-renda nula indica consumo insensível à renda."),
        "destrinchando": [
            vd("η = %ΔQ / %ΔR") + ". Normal: η > 0, dividido em " + azb("necessário") + " (0 < η < 1 — a "
            "quantidade cresce, mas menos que a renda; ex.: alimentos básicos) e " + azb("de luxo/superior")
            + " (η > 1 — cresce mais que a renda; ex.: viagens internacionais).",
            azb("Inferior") + ": η < 0 — com mais renda, compra-se menos (ônibus intermunicipal, carne de "
            "segunda, marcas mais baratas).",
            "η = 0: consumo que não responde à renda — fronteira entre normal e inferior (às vezes chamado de "
            "bem “neutro” ou de consumo saciado, como sal).",
            "Graficamente: aumento de renda desloca a demanda para a direita (normal), para a esquerda "
            "(inferior) ou a deixa parada (η = 0). A " + oc("curva de Engel") + " é positivamente inclinada "
            "para bens normais.",
        ],
        "dissecando": (cz("[dado alterado · troca de conceito]") + " Troca o sinal que define a categoria "
                       "(positivo → nulo). Pista: a palavra “normal” não sugere “neutro”; a classificação é "
                       "sempre pelo sinal de η."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um bem de luxo apresenta elasticidade-renda maior que um.”</i> → CERTO",
            "<i>“Todo bem normal tem elasticidade-renda maior que um.”</i> → ERRADO (generalização: só os de "
            "luxo)",
        ])],
        "reescrita": "Um bem normal apresenta elasticidade-renda " + hl("positiva") + ".",
        "tipo_erro": ["DADO_ALTERADO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Bem normal: consumo aumenta com a renda, elasticidade-renda positiva; nula "
                            "caracteriza consumo que não se altera com a renda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00600
    {
        "id": "ECO-E2-L00600-1", "fonte_ref": "E2-L00600", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MICRO3,
        "rotulo_item": "Item",
        "assertiva": "Um bem inferior apresenta elasticidade-renda negativa.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um bem inferior apresenta elasticidade-renda <u>negativa</u>."),
        "poucas": ("Bem " + azb("inferior") + ": a renda sobe e o consumo cai — numerador e denominador de "
                   "η com sinais opostos, logo " + vd("η < 0") + "."),
        "destrinchando": [
            "Por que existem: com mais renda, o consumidor troca o bem por versões de melhor qualidade (pão "
            "comum → pão especial; transporte coletivo → carro próprio). “Inferior” não é juízo de qualidade "
            "física, é classificação pela reação à renda.",
            "Inferioridade é " + azb("relativa à faixa de renda") + ": o mesmo bem pode ser normal para os "
            "pobres e inferior para os ricos (a curva de Engel “volta para trás”).",
            azb("Bem de Giffen") + " é um caso extremo de inferior: o efeito renda (positivo, quando o preço "
            "sobe) supera o efeito substituição, e a demanda passa a ter inclinação positiva. Todo Giffen é "
            "inferior; nem todo inferior é Giffen.",
            "Não confundir com bem " + azb("necessário") + " (0 < η < 1): é normal, só que com resposta "
            "menos que proporcional à renda.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. O risco é a confusão inferior × necessário "
                       "(η < 1) ou inferior × Giffen. 🔥 Itens vizinhos do mesmo bloco testam “normal = nula” e "
                       "“inferior = menor que 1” (ambos ERRADOS)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todo bem inferior é um bem de Giffen.”</i> → ERRADO (inversão: todo Giffen é inferior)",
            "<i>“Um bem pode ser normal em baixos níveis de renda e inferior em níveis elevados.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Bem inferior: consumo diminui quando a renda aumenta; elasticidade-renda "
                            "negativa.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00650
    {
        "id": "ECO-E2-L00650-1", "fonte_ref": "E2-L00650", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à microeconomia, julgue os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-preço cruzada da demanda é negativa para bens substitutos e positiva para "
                      "bens complementares."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elasticidade-preço cruzada da demanda é ") + vm("negativa") + az(" para bens substitutos "
                                                                                          "e ")
                    + vm("positiva") + az(" para bens complementares.")),
        "poucas": ("Sinais invertidos: " + azb("substitutos") + " → cruzada " + vd("positiva") + "; "
                   + azb("complementares") + " → cruzada " + vd("negativa") + "."),
        "destrinchando": [
            vd("ε<sub>xy</sub> = %ΔQ<sub>x</sub> / %ΔP<sub>y</sub>") + ".",
            "Substitutos: gasolina encarece → demanda por etanol <b>sobe</b>. Numerador e denominador com o "
            "mesmo sinal → ε > 0.",
            "Complementares: café encarece → demanda por açúcar <b>cai</b>. Sinais opostos → ε < 0.",
            "Teste rápido: pergunte “o preço de y sobe — a quantidade de x sobe ou cai?”. Sobe = substituto "
            "(sinal +); cai = complementar (sinal −). O sinal da cruzada é o sinal do “sentimento” entre os "
            "bens: concorrentes ganham com a alta do rival.",
            vm("Regra-âncora: substituto +, complementar −."),
        ],
        "dissecando": (cz("[inversão]") + " Inversão pura dos dois sinais, mantendo a estrutura da definição. "
                       "Quem associa “complementar” a “positivo” (sentido de “somar”) cai. 🔥 A Nabuco repete "
                       "essa troca em vários blocos."),
        "modulos": [("🧠 Mnemônico", ["<b>S</b>ubstituto <b>S</b>obe junto com o preço do rival (+); "
                                      "<b>C</b>omplementar <b>C</b>ai (−)."])],
        "reescrita": ("A elasticidade-preço cruzada da demanda é " + hl("positiva") + " para bens substitutos e "
                      + hl("negativa") + " para bens complementares."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Inverteu: cruzada positiva para substitutos (gasolina × etanol) e negativa para "
                            "complementares (café × açúcar).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00674
    {
        "id": "ECO-E2-L00674-1", "fonte_ref": "E2-L00674", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito da teoria do consumidor e dos conceitos de elasticidade, julgue os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("Se a demanda por um produto é inelástica em relação ao preço, um aumento no preço do "
                      "produto levará a uma redução na receita total dos vendedores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se a demanda por um produto é inelástica em relação ao preço, um aumento no preço do "
                       "produto levará a ") + vm("uma redução") + az(" na receita total dos vendedores.")),
        "poucas": ("Demanda " + azb("inelástica") + " (|ε| < 1): a quantidade cai proporcionalmente menos que o "
                   "preço sobe, e a receita total <b>aumenta</b>."),
        "destrinchando": [
            "%ΔRT ≈ %ΔP·(1 − |ε|). Com |ε| = 0,5 e preço +10%: quantidade −5%, receita ≈ 1,10 × 0,95 = "
            + vd("1,045") + " (+4,5%).",
            "Preço e receita andam no <b>mesmo sentido</b> na demanda inelástica; em sentidos opostos na "
            "elástica; na unitária, a receita não muda.",
            "Exemplos de demanda inelástica: combustíveis no curto prazo, energia elétrica, medicamentos, "
            "cigarro. Por isso tributos e reajustes sobre esses bens arrecadam/faturam mais.",
            "Aplicação clássica (" + oc("Mankiw") + "): quebra de safra ou cartel que restringe a oferta (como "
            "a " + azb("OPEP") + " nos anos 1970) eleva o preço e, com demanda inelástica, a receita dos "
            "produtores sobe.",
        ],
        "dissecando": (cz("[inversão]") + " Atribui à demanda inelástica o efeito da elástica. Pista: "
                       "“inelástica” = consumidor reage pouco = o vendedor ganha ao subir o preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a demanda por um produto é elástica, um aumento no preço levará a uma redução na receita "
            "total.”</i> → CERTO",
            "<i>“Com demanda inelástica, uma safra recorde eleva a receita total dos agricultores.”</i> → "
            "ERRADO (inversão: o preço despenca e a receita cai)",
        ])],
        "reescrita": ("Se a demanda por um produto é inelástica em relação ao preço, um aumento no preço do "
                      "produto levará a " + hl("um aumento") + " na receita total dos vendedores."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Demanda inelástica: queda na quantidade proporcionalmente pequena; RT aumenta. Só "
                            "cairia se a demanda fosse elástica.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00879
    {
        "id": "ECO-E2-L00879-1", "fonte_ref": "E2-L00879", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_INTERV,
        "rotulo_item": "Item",
        "assertiva": "Um bem inferior é um bem com elasticidade-renda da demanda menor que 1.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um bem inferior é um bem com elasticidade-renda da demanda ") + vm("menor que 1") + az("."),
        "poucas": ("Bem inferior tem " + vd("η < 0") + ". Elasticidade-renda entre 0 e 1 caracteriza bem "
                   + azb("normal necessário") + ", não inferior."),
        "destrinchando": [
            "Régua completa: " + vd("η < 0") + " inferior; " + vd("η = 0") + " consumo insensível à renda; "
            + vd("0 < η < 1") + " normal necessário; " + vd("η > 1") + " normal de luxo (superior).",
            "“Menor que 1” abarca tanto inferiores quanto necessários: um bem com η = 0,4 tem consumo "
            "<b>crescente</b> com a renda — não é inferior. A definição do item é ampla demais.",
            "O limite 1 importa para a <b>parcela no orçamento</b>: com η < 1, a fatia da renda gasta com o bem "
            "cai quando a renda sobe (lei de " + oc("Engel") + "), mas a quantidade pode estar subindo.",
            "Bem inferior: a quantidade cai em termos absolutos com a renda. Bem necessário: a quantidade sobe, "
            "mas a fatia do orçamento cai.",
        ],
        "dissecando": (cz("[troca de conceito · dado alterado]") + " Troca o limiar que define a categoria (0 "
                       "→ 1), confundindo inferior com necessário. Pista: “inferior” fala da direção da "
                       "resposta (sinal); “necessário × luxo” fala da intensidade (maior ou menor que 1)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Todo bem inferior tem elasticidade-renda menor que 1, mas nem todo bem com elasticidade-renda "
            "menor que 1 é inferior.”</i> → CERTO",
            "<i>“Bens necessários têm elasticidade-renda negativa.”</i> → ERRADO (troca de conceito: entre 0 e "
            "1)",
        ])],
        "reescrita": "Um bem inferior é um bem com elasticidade-renda da demanda " + hl("negativa (menor que 0)")
                     + ".",
        "tipo_erro": ["TROCA_CONCEITO", "DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Bem inferior: renda aumenta, quantidade diminui; elasticidade-renda negativa, não "
                            "“menor que um”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00880
    {
        "id": "ECO-E2-L00880-1", "fonte_ref": "E2-L00880", "destino": "02", "subtema": H2["rc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_INTERV,
        "rotulo_item": "Item",
        "assertiva": ("Um bem é denominado bem complementar se a elasticidade-preço cruzada da demanda desse bem "
                      "for negativa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um bem é denominado bem complementar se a elasticidade-preço cruzada da demanda desse bem "
                      "for <u>negativa</u>."),
        "poucas": ("Complementares são consumidos juntos: a alta do preço de um reduz a quantidade do outro, e a "
                   + azb("elasticidade-preço cruzada") + " é " + vd("negativa") + "."),
        "destrinchando": [
            vd("ε<sub>xy</sub> = %ΔQ<sub>x</sub> / %ΔP<sub>y</sub>") + " — variação percentual na quantidade de "
            "um bem diante de variação de 1% no preço de <b>outro</b>.",
            "Negativa → " + azb("complementares") + " (pão × manteiga, impressora × cartucho); positiva → "
            + azb("substitutos") + " (manteiga × margarina); nula → independentes.",
            "Precisão de linguagem: a cruzada é sempre <b>entre dois bens</b>; “a cruzada desse bem” "
            "subentende o par em análise. Ser complementar não é atributo absoluto do bem, mas da relação "
            "com outro.",
            "Para classificação rigorosa (complementares líquidos), a teoria usa a demanda compensada de "
            + oc("Hicks") + "; em provas objetivas, vale a regra do sinal da cruzada.",
            "Mesmo conteúdo em outra redação: “se a cruzada entre A e B é negativa, um aumento no preço de A "
            "reduz a quantidade de B, indicando complementares” — também CERTO.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual pelo sinal. A imprecisão (“desse bem”, sem "
                       "dizer em relação a qual) não basta para tornar o item errado. 🔥 O mesmo bloco cobra "
                       "“inferior = menor que 1” (ERRADO), para testar se o candidato distingue sinal de "
                       "intensidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um bem é denominado substituto se a elasticidade-preço cruzada da demanda for negativa.”</i> → "
            "ERRADO (inversão: positiva)",
            "<i>“A elasticidade-preço cruzada mede a variação percentual da quantidade de um bem diante da "
            "variação percentual da renda.”</i> → ERRADO (troca de conceito: é o preço de outro bem)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Complementares são consumidos conjuntamente; cruzada positiva para substitutos e "
                            "negativa para complementares.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 138", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
]
