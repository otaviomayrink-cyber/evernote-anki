"""Cards do lote de redação 08 — ECO, passada 01 (nota 03: intervenções do Estado e bem-estar)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "exc": "😊 Excedentes e eficiência",
    "trib": "💸 Tributos: incidência e peso morto",
    "sub": "🧾 Subsídios",
    "piso": "🚧 Preços máximos e mínimos",
}

CMD_INC = "Julgue o item a seguir, relativo à incidência de tributos em mercados competitivos."

CMD_2013 = ("Supondo que o governo adote um novo imposto específico sobre a venda de um bem em um mercado de "
            "concorrência perfeita e considerando a distribuição da incidência tributária entre vendedores e "
            "consumidores, julgue o item a seguir.")

CMD_BOZAN = "Julgue o item a seguir, sobre políticas de preço mínimo e suas implicações econômicas."

CMD_NAB_EQ = ("Em um mercado competitivo, as curvas de demanda e de oferta de um produto são Qᴰ = 300 − 30p e "
              "Qˢ = 10p + 20, em que p é o preço do produto, em reais. Julgue o item.")

CMD_NAB_4 = "Considerando os conceitos de microeconomia, julgue o item a seguir."

FIG_E1 = lambda ref: [{"ref": ref, "tipo_fonte": "GRÁFICO", "lado": "verso",
                       "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}]

CARDS = [
    # ------------------------------------------------------------------ E1-0173
    {
        "id": "ECO-E1-0173-1", "fonte_ref": "E1-0173", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INC,
        "rotulo_item": "Item",
        "assertiva": ("A incidência de um imposto sobre vendas em um mercado de concorrência perfeita é "
                      "integralmente suportada pelos consumidores, independentemente da elasticidade-preço da "
                      "demanda do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A incidência de um imposto sobre vendas em um mercado de concorrência perfeita é ")
                    + vm("integralmente suportada pelos consumidores, independentemente da elasticidade-preço da "
                         "demanda do bem") + az(".")),
        "poucas": ("A " + azb("incidência econômica") + " de um imposto se reparte entre compradores e vendedores "
                   "conforme as " + azb("elasticidades") + " da demanda e da oferta; o repasse integral ao "
                   "consumidor é caso-limite, não regra."),
        "destrinchando": [
            "Um imposto sobre vendas abre uma " + azb("cunha") + " entre o preço pago pelo comprador (pc) e o "
            "recebido pelo vendedor (pv): pc − pv = t. A pergunta da incidência é quanto de t vem de alta de pc e "
            "quanto vem de queda de pv.",
            "Fórmula de bolso: fração paga pelo consumidor = " + vd("εˢ / (εˢ + |εᴰ|)") + "; fração paga pelo "
            "produtor = " + vd("|εᴰ| / (εˢ + |εᴰ|)") + ". Quem é <b>menos elástico</b> arca com mais.",
            "Os únicos casos de repasse integral ao consumidor são os extremos: " + vd("|εᴰ| = 0") + " (demanda "
            "vertical) ou " + vd("εˢ = ∞") + " (oferta horizontal). No extremo oposto — demanda infinitamente "
            "elástica — o consumidor não paga nada.",
            "A incidência <b>legal</b> (quem recolhe o tributo ao fisco) não decide nada: cobrado do vendedor ou do "
            "comprador, o equilíbrio final é o mesmo.",
            vm("Regra-âncora: o ônus do imposto cai sobre o lado menos elástico do mercado."),
        ],
        "dissecando": (cz("[modulador absoluto · contradição]") + " Dois absolutos empilhados — "
                       "“integralmente” e “independentemente da elasticidade” — negam justamente a variável que "
                       "decide a incidência. Em itens de tributo, “independentemente da elasticidade” é quase "
                       "sempre o sinal do erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é integralmente suportada pelos consumidores se a demanda do bem for perfeitamente "
            "inelástica.”</i> → CERTO",
            "<i>“…é integralmente suportada pelos consumidores se a demanda for infinitamente elástica.”</i> → "
            "ERRADO (inversão: nesse caso quem paga tudo é o vendedor)",
        ])],
        "reescrita": ("A incidência de um imposto sobre vendas em um mercado de concorrência perfeita é "
                      + hl("repartida entre consumidores e vendedores, conforme as elasticidades-preço da demanda "
                           "e da oferta") + " do bem."),
        "tipo_erro": ["GENERALIZACAO", "CONTRADICAO"], "moduladores": ["integralmente", "independentemente"],
        "dificuldade": 1,
        "comentario_fonte": "A incidência depende das elasticidades da demanda e da oferta; o lado menos elástico "
                            "suporta a maior parte; não há repasse integral automático.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0177
    {
        "id": "ECO-E1-0177-1", "fonte_ref": "E1-0177", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INC,
        "rotulo_item": "Item",
        "assertiva": ("Com relação à incidência de um imposto sobre vendas de um bem X num mercado em concorrência "
                      "perfeita, é correto afirmar que o ônus do imposto recai mais fortemente sobre os vendedores "
                      "ou consumidores dependendo do valor das respectivas elasticidades-preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com relação à incidência de um imposto sobre vendas de um bem X num mercado em concorrência "
                      "perfeita, é correto afirmar que o ônus do imposto recai <u>mais fortemente</u> sobre os "
                      "vendedores ou consumidores <u>dependendo do valor das respectivas elasticidades-preço</u>."),
        "poucas": ("É a regra geral da incidência: o ônus pesa mais sobre o lado " + azb("menos elástico")
                   + " — vendedores, se a oferta for mais rígida; consumidores, se a demanda for."),
        "destrinchando": [
            "Com o imposto t, o preço pago sobe e o recebido cai; a soma das duas variações é t. A divisão "
            "depende da capacidade de cada lado de <b>fugir</b> do mercado: quem tem alternativas (substitutos, "
            "outros usos para os fatores) reduz a quantidade e empurra o ônus para o outro.",
            "Em fórmula: parcela do consumidor = " + vd("εˢ / (εˢ + |εᴰ|)") + ". Se |εᴰ| < εˢ, o consumidor "
            "paga mais da metade; se |εᴰ| > εˢ, o vendedor paga mais.",
            "Exemplos típicos: combustíveis e cigarros (demanda inelástica) → a maior parte vai para o "
            "consumidor; produtos agrícolas já plantados ou imóveis (oferta rígida no curto prazo) → a maior "
            "parte vai para o produtor.",
            "Por isso a incidência legal é irrelevante: o que importa são as inclinações das curvas, não quem "
            "assina a guia de recolhimento.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz a regra do manual. O "
                       "“mais fortemente” protege o item: não diz que um lado paga tudo, só que pesa mais sobre um "
                       "deles conforme as elasticidades."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o ônus recai mais fortemente sobre o lado de maior elasticidade-preço.”</i> → ERRADO "
            "(inversão: recai sobre o de menor elasticidade)",
            "<i>“…o ônus recai mais fortemente sobre quem recolhe o imposto ao fisco.”</i> → ERRADO (troca de "
            "conceito: incidência legal × econômica)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["mais fortemente", "dependendo"],
        "dificuldade": 1,
        "comentario_fonte": "O ônus depende das elasticidades relativas; o lado mais inelástico suporta a maior "
                            "parte.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0178
    {
        "id": "ECO-E1-0178-1", "fonte_ref": "E1-0178", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à eficiência dos tributos.",
        "rotulo_item": "Item",
        "assertiva": ("Do ponto de vista econômico, impostos eficientes são aqueles que incidem com uma carga maior "
                      "sobre produtos com demanda ou oferta inelástica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Do ponto de vista econômico, impostos <u>eficientes</u> são aqueles que incidem com uma "
                      "carga maior sobre produtos com demanda ou oferta <u>inelástica</u>."),
        "poucas": ("Imposto eficiente é o que gera pouco " + azb("peso morto") + ", e o peso morto nasce da queda "
                   "da quantidade. Onde demanda ou oferta é " + azb("inelástica") + ", a quantidade quase não "
                   "reage: tributa-se sem distorcer."),
        "destrinchando": [
            "Na economia do bem-estar, " + azb("eficiência") + " = não destruir excedente. O imposto só destrói "
            "excedente porque faz deixar de existir trocas que valiam a pena (qₜ < q₀). Se a quantidade não muda, "
            "o imposto é pura <b>transferência</b> para o governo.",
            "Aproximação útil: peso morto ≈ ½ · t² · (sensibilidade da quantidade ao preço). Ele cresce com as "
            "elasticidades e com o <b>quadrado</b> da alíquota — por isso bases amplas com alíquotas baixas "
            "distorcem menos que bases estreitas com alíquotas altas.",
            azb("Regra de Ramsey") + " (" + oc("Frank Ramsey") + ", 1927): para arrecadar um montante dado com o "
            "menor peso morto, as alíquotas devem ser <b>inversamente proporcionais</b> às elasticidades — mais "
            "imposto onde a base é rígida.",
            "Caso-limite do lado da oferta: a terra, de oferta fixa. " + oc("Henry George") + " (<i>Progresso e "
            "Pobreza</i>, 1879) defendeu um imposto único sobre a terra justamente porque não reduziria a "
            "quantidade ofertada.",
            "O contraponto é a " + azb("equidade") + ": bens de demanda inelástica (alimentos básicos, energia, "
            "remédios) pesam mais no orçamento dos pobres. Eficiência e justiça tributária frequentemente "
            "puxam para lados opostos.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " Soa injusto “carregar” mais nos bens essenciais, e o "
                       "candidato tende a marcar ERRADO por equidade. Mas o item restringe o critério: “do ponto "
                       "de vista econômico” e “eficientes” — eficiência, não justiça."),
        "modulos": [
            ("😈 Para dificultar", [
                "<i>“Impostos eficientes são aqueles que incidem com carga maior sobre bens de demanda "
                "elástica.”</i> → ERRADO (inversão: maximiza o peso morto)",
                "<i>“A regra de Ramsey garante simultaneamente eficiência e progressividade.”</i> → ERRADO "
                "(extrapolação: costuma sacrificar a equidade)",
            ]),
            ("🃏 Carta na manga", [
                "Tributar bases inelásticas minimiza o peso morto (regra de " + oc("Ramsey") + "), mas tende a "
                "ser regressivo: o desenho tributário ótimo combina eficiência na base com progressividade na "
                "renda.",
            ]),
        ],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Um imposto eficiente influencia minimamente a decisão do agente.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("Untitled (39).jpeg"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0179
    {
        "id": "ECO-E1-0179-1", "fonte_ref": "E1-0179", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos efeitos dos impostos sobre o equilíbrio de mercado.",
        "rotulo_item": "Item",
        "assertiva": ("Os impostos desencorajam a atividade do mercado pois quando um bem é tributado, a quantidade "
                      "vendida desse bem é menor no novo equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os impostos desencorajam a atividade do mercado pois quando um bem é tributado, a "
                      "<u>quantidade vendida</u> desse bem é <u>menor</u> no novo equilíbrio."),
        "poucas": ("O imposto cria uma " + azb("cunha") + " entre o preço do comprador e o do vendedor: o "
                   "primeiro sobe, o segundo cai, e ambos reduzem a quantidade — o mercado " + vd("encolhe") + "."),
        "destrinchando": [
            "Imposto específico t cobrado do vendedor: a oferta sobe t (O → O + t). Novo equilíbrio: "
            + vd("pc > p₀") + ", " + vd("pv = pc − t < p₀") + " e " + vd("qₜ < q₀") + ".",
            "Os dois lados dividem o ônus (a divisão depende das elasticidades) e o mercado diminui. É a "
            "conclusão de " + oc("Mankiw") + " (<i>Introdução à Economia</i>): impostos desestimulam a atividade "
            "de mercado.",
            "Bem-estar: parte do excedente perdido vira " + azb("receita") + " (t × qₜ, transferência); a outra "
            "parte, o triângulo entre qₜ e q₀, é " + azb("peso morto") + " — trocas que geravam valor e deixaram "
            "de acontecer.",
            "Exceção: se a demanda ou a oferta for perfeitamente inelástica (curva vertical), a quantidade não "
            "muda e não há peso morto. Fora desses extremos, a quantidade sempre cai.",
        ],
        "grafico_verso": "ECO-E1-0179-1-V1",
        "dissecando": (cz("[literalidade]") + " Paráfrase direta do manual. O risco é a desconfiança com o "
                       "“desencorajam a atividade”, que soa opinativo: tecnicamente, é só outra forma de dizer "
                       "que qₜ < q₀."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando um bem é tributado, a quantidade vendida diminui, salvo se a demanda for perfeitamente "
            "inelástica.”</i> → CERTO",
            "<i>“O imposto reduz a quantidade porque desloca a curva de demanda do bem para a esquerda, qualquer "
            "que seja o lado que o recolha.”</i> → ERRADO (cobrado do vendedor, desloca a oferta)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Imposto cria cunha entre preço do consumidor e do produtor, reduz a quantidade "
                            "transacionada e o excedente total; oferta desloca-se para a esquerda; ônus "
                            "compartilhado.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_E1("Untitled (44).jpeg"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0180
    {
        "id": "ECO-E1-0180-1", "fonte_ref": "E1-0180", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos efeitos dos impostos sobre o equilíbrio de mercado.",
        "rotulo_item": "Item",
        "assertiva": ("Quando o governo impõe um imposto sobre os consumidores, a curva de demanda se move para a "
                      "esquerda e para baixo, indicando uma retração."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando o governo impõe um imposto sobre os <u>consumidores</u>, a curva de "
                      "<u>demanda</u> se move para a esquerda e para baixo, indicando uma retração."),
        "poucas": ("Cobrado do comprador, o imposto reduz em t o que ele aceita pagar <b>ao vendedor</b>: a "
                   + azb("demanda") + " desce t (D → D − t), para baixo e para a esquerda."),
        "destrinchando": [
            "Se o comprador aceitava pagar p por certa quantidade, agora só entrega ao vendedor p − t (o resto "
            "vai ao fisco). A curva de demanda <b>vista pelo vendedor</b> desce verticalmente t em cada "
            "quantidade.",
            "Novo equilíbrio: o vendedor recebe " + vd("pv < p₀") + "; o comprador paga " + vd("pc = pv + t > p₀")
            + "; a quantidade cai para qₜ. Os dois lados perdem excedente.",
            azb("Equivalência") + ": o mesmo t cobrado do vendedor deslocaria a <b>oferta</b> para cima — e o "
            "resultado seria idêntico (mesmos pc, pv e qₜ). Só muda qual curva se desenha deslocada.",
            "A divisão do ônus entre comprador e vendedor continua sendo decidida pelas elasticidades, não por "
            "quem recolhe.",
        ],
        "grafico_verso": "ECO-E1-0180-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " O item testa qual curva se move conforme o lado "
                       "tributado. A pegadinha clássica é trocar a curva (“a oferta se desloca”) ou concluir que, "
                       "por ser cobrado do consumidor, só ele perde."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando o governo impõe um imposto sobre os consumidores, a curva de oferta se desloca para a "
            "esquerda.”</i> → ERRADO (curva trocada: desloca-se a demanda)",
            "<i>“Por ser cobrado dos consumidores, o imposto é suportado integralmente por eles.”</i> → ERRADO "
            "(incidência legal ≠ econômica)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Demanda desloca-se para a esquerda e para baixo; vendedores recebem menos, "
                            "compradores pagam mais; ambos compartilham as perdas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("Untitled (48).jpeg"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0235 (1)
    {
        "id": "ECO-E1-0235-1", "fonte_ref": "E1-0235", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": True,
        "comando": CMD_2013,
        "rotulo_item": "Item",
        "assertiva": "Se a elasticidade-preço da demanda for infinita, os vendedores abandonarão o mercado.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se a elasticidade-preço da demanda for infinita, os vendedores ")
                    + vm("abandonarão o mercado") + az(".")),
        "poucas": ("Com demanda " + azb("infinitamente elástica") + " (horizontal), o preço ao consumidor não "
                   "sobe: o vendedor arca com " + vd("todo o imposto") + " e a quantidade cai — mas o mercado "
                   "continua existindo."),
        "destrinchando": [
            "Demanda horizontal ao preço p₀: a qualquer preço acima de p₀, os compradores somem (substitutos "
            "perfeitos, ou o preço é dado pelo mercado mundial). O consumidor continua pagando " + vd("pc = p₀")
            + ".",
            "Como o comprador não aceita nenhum aumento, o vendedor passa a receber " + vd("pv = p₀ − t")
            + ": toda a cunha sai do seu preço líquido. Pela fórmula, parcela do produtor = |εᴰ| / (εˢ + |εᴰ|) "
            "→ 1 quando |εᴰ| → ∞.",
            "Com preço líquido menor, os vendedores andam <b>ao longo</b> da curva de oferta: produzem menos "
            "(qₜ < q₀). Saem apenas as unidades (e as firmas) cujo custo marginal fica acima de p₀ − t. O mercado "
            "só desapareceria se p₀ − t ficasse abaixo do menor custo de qualquer produtor — hipótese que o item "
            "não traz.",
            "Exemplo: pequena economia aberta exportadora de uma commodity com preço internacional dado; um "
            "imposto sobre a venda reduz a receita do produtor doméstico sem mexer no preço mundial.",
            vm("Regra-âncora: demanda infinitamente elástica → produtor paga tudo; demanda perfeitamente "
               "inelástica → consumidor paga tudo."),
        ],
        "grafico_verso": "ECO-E1-0235-1-V1",
        "dissecando": (cz("[extrapolação]") + " O ponto de partida é certo (o vendedor fica com todo o ônus), "
                       "mas o item salta para uma consequência extrema que não decorre do modelo. Quem lembra "
                       "que “o produtor perde tudo” confunde ônus integral com saída do mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade-preço da demanda for infinita, os vendedores arcarão com todo o ônus do "
            "imposto.”</i> → CERTO",
            "<i>“Se a elasticidade-preço da demanda for infinita, o preço pago pelos consumidores subirá no valor "
            "do imposto.”</i> → ERRADO (inversão: pc fica constante)",
        ])],
        "reescrita": ("Se a elasticidade-preço da demanda for infinita, os vendedores " + hl("arcarão com todo o "
                      "peso do imposto, e a quantidade transacionada diminuirá") + "."),
        "tipo_erro": ["EXTRAPOLACAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Demanda horizontal: toda a cunha recai sobre o excedente do produtor, que não "
                            "consegue repassar; consumidores pagam o mesmo preço; receita do produtor cai.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: errei — na fonte, os itens (1), (3) e (4) vêm com ❌; como o (4) é CERTO, a marca foi lida "
                    "como “errei”, não como gabarito",
                    "banca_provavel: CEBRASPE/CACD 2013 (a fonte só traz “C/E (2013)”; não confirmada)"],
    },
    # ------------------------------------------------------------------ E1-0235 (2)
    {
        "id": "ECO-E1-0235-2", "fonte_ref": "E1-0235", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_2013,
        "rotulo_item": "Item",
        "assertiva": ("Vendedores e consumidores arcarão com o peso do imposto, conforme a sensibilidade das curvas "
                      "de oferta e demanda às variações de preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Vendedores e consumidores arcarão com o peso do imposto, <u>conforme a sensibilidade</u> "
                      "das curvas de oferta e demanda às variações de preço."),
        "poucas": ("É a definição de " + azb("incidência econômica") + ": o imposto se divide entre os dois "
                   "lados na proporção inversa das " + azb("elasticidades") + " (a “sensibilidade às variações "
                   "de preço”)."),
        "destrinchando": [
            "“Sensibilidade das curvas às variações de preço” é a " + azb("elasticidade-preço") + ". Parcela do "
            "consumidor = " + vd("εˢ / (εˢ + |εᴰ|)") + "; do vendedor = " + vd("|εᴰ| / (εˢ + |εᴰ|)") + ".",
            "Leitura intuitiva: paga mais quem tem menos opções de fuga. Consumidor sem substitutos aceita preço "
            "maior; produtor com capital imobilizado aceita preço líquido menor.",
            "O item é regra geral e admite os casos extremos como limites da mesma fórmula: com |εᴰ| = 0 ou "
            "εˢ = ∞, o consumidor paga tudo; com εˢ = 0 ou |εᴰ| = ∞, o vendedor paga tudo.",
            "Irrelevância da incidência legal: o resultado não muda se a lei mandar o vendedor ou o comprador "
            "recolher o tributo.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Reescreve a regra trocando “elasticidade” "
                       "por “sensibilidade às variações de preço”. A paráfrase é o único obstáculo: quem procura "
                       "a palavra técnica pode estranhar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Vendedores e consumidores sempre dividirão igualmente o peso do imposto.”</i> → ERRADO "
            "(modulador absoluto: a divisão depende das elasticidades)",
            "<i>“O lado do mercado mais sensível às variações de preço arcará com a maior parte do "
            "imposto.”</i> → ERRADO (inversão: arca com a menor parte)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["conforme"], "dificuldade": 1,
        "comentario_fonte": "Correto; afirmação exaustiva sobre o tema.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE/CACD 2013 (a fonte só traz “C/E (2013)”; não confirmada)"],
    },
    # ------------------------------------------------------------------ E1-0235 (3)
    {
        "id": "ECO-E1-0235-3", "fonte_ref": "E1-0235", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": True,
        "comando": CMD_2013,
        "rotulo_item": "Item",
        "assertiva": ("Vendedores irão transferir aos compradores o valor relativo a toda incidência do novo "
                      "imposto, o que aumentará o preço do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Vendedores irão transferir aos compradores o valor relativo a ")
                    + vm("toda incidência") + az(" do novo imposto, o que aumentará o preço do bem.")),
        "poucas": ("Repasse " + azb("integral") + " só ocorre em casos-limite (demanda perfeitamente inelástica "
                   "ou oferta perfeitamente elástica). Sem essa hipótese, o preço sobe <b>menos</b> que o "
                   "imposto e o vendedor absorve parte."),
        "destrinchando": [
            "Com curvas de inclinação normal, o novo equilíbrio tem pc subindo e pv caindo: " + vd("ΔPc + |ΔPv| "
            "= t") + ", e cada parcela depende das elasticidades.",
            "Repasse total exige que o comprador não reaja ao preço — " + vd("|εᴰ| = 0") + ", demanda vertical "
            "— ou que o vendedor não aceite nenhuma redução do preço líquido — " + vd("εˢ = ∞") + ", oferta "
            "horizontal (indústria de custos constantes no longo prazo).",
            "A metade verdadeira do item é a segunda oração: o preço ao consumidor <b>aumenta</b>, salvo no caso "
            "de demanda infinitamente elástica. O erro está no “toda”.",
            "Detalhe de redação: o comando trata de um imposto genérico, sem informar elasticidades. Faltando "
            "a hipótese extrema, vale a regra geral de partilha.",
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " O preço sobe (verdade), mas não no valor "
                       "inteiro do imposto. O absoluto “toda” transforma um caso-limite em regra. 🔥 Itens de "
                       "incidência sem elasticidade informada quase sempre pedem a regra geral de partilha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a oferta for perfeitamente elástica, os vendedores transferirão aos compradores todo o "
            "imposto.”</i> → CERTO",
            "<i>“Só se a demanda for perfeitamente inelástica os vendedores transferirão todo o imposto.”</i> → "
            "ERRADO (restrição indevida: também com oferta perfeitamente elástica)",
        ])],
        "reescrita": ("Vendedores irão transferir aos compradores " + hl("apenas parte do") + " novo imposto, "
                      "o que aumentará o preço do bem " + hl("em montante inferior ao do tributo") + "."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["toda"], "dificuldade": 1,
        "comentario_fonte": "Só ocorreria com demanda de elasticidade nula (vertical); nesse caso o consumidor "
                            "absorve toda a elevação de preço.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: errei — marca ❌ da fonte preservada (ver ECO-E1-0235-1)",
                    "qualidade_fonte: o comentário de origem diz que o repasse integral “apenas” ocorre com "
                    "demanda vertical; também ocorre com oferta perfeitamente elástica — corrigido",
                    "banca_provavel: CEBRASPE/CACD 2013 (a fonte só traz “C/E (2013)”; não confirmada)"],
    },
    # ------------------------------------------------------------------ E1-0235 (4)
    {
        "id": "ECO-E1-0235-4", "fonte_ref": "E1-0235", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": True,
        "comando": CMD_2013,
        "rotulo_item": "Item",
        "assertiva": ("Quanto menor for a elasticidade-preço da demanda, maior será a incidência do tributo para "
                      "os consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto <u>menor</u> for a elasticidade-preço da demanda, <u>maior</u> será a incidência "
                      "do tributo para os consumidores."),
        "poucas": ("Demanda menos elástica = consumidor com menos alternativas: ele aceita pagar mais, e a "
                   "parcela do imposto que recai sobre ele " + vd("aumenta") + "."),
        "destrinchando": [
            "Parcela do consumidor = " + vd("εˢ / (εˢ + |εᴰ|)") + ". Mantida a oferta, reduzir |εᴰ| diminui o "
            "denominador e eleva a fração; no limite |εᴰ| = 0, ela vale 1 (o consumidor paga tudo).",
            "A elasticidade-preço da demanda é baixa quando o bem é necessário, tem poucos substitutos, pesa "
            "pouco no orçamento ou o horizonte é curto (combustível na semana seguinte ao aumento).",
            "Por isso tributos sobre combustíveis, energia, bebidas e cigarros são, em boa parte, pagos pelo "
            "consumidor final, ainda que recolhidos pelo produtor ou distribuidor.",
            "Cuidado com o sinal: a elasticidade-preço da demanda é negativa; “menor elasticidade” significa "
            "menor <b>em módulo</b> (mais próxima de zero).",
        ],
        "dissecando": (cz("[literalidade]") + " Relação monotônica correta (menos elástico → paga mais). O "
                       "risco é a inversão mental de “menor”, ou o tropeço no sinal negativo da "
                       "elasticidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior for a elasticidade-preço da oferta, maior será a incidência do tributo para os "
            "consumidores.”</i> → CERTO",
            "<i>“Quanto menor for a elasticidade-preço da oferta, maior será a incidência do tributo para os "
            "consumidores.”</i> → ERRADO (inversão: oferta rígida joga o ônus no produtor)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["quanto menor… maior"], "dificuldade": 1,
        "comentario_fonte": "Correto: com poucas alternativas, o consumidor absorve o custo via preço; a empresa "
                            "repassa parte do fardo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: errei — marca ❌ da fonte preservada (ver ECO-E1-0235-1)",
                    "banca_provavel: CEBRASPE/CACD 2013 (a fonte só traz “C/E (2013)”; não confirmada)"],
    },
]
