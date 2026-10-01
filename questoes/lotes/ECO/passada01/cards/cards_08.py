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
    # ------------------------------------------------------------------ E1-0436
    {
        "id": "ECO-E1-0436-1", "fonte_ref": "E1-0436", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("No estudo das estruturas de mercado, a concorrência perfeita e o monopólio representam "
                    "extremos analíticos com implicações distintas sobre o bem-estar social e a eficiência "
                    "alocativa. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A introdução de um imposto específico em um mercado competitivo afeta exclusivamente os "
                      "consumidores, visto que as firmas tomam o preço como dado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A introdução de um imposto específico em um mercado competitivo afeta ")
                    + vm("exclusivamente os consumidores") + az(", visto que ")
                    + vm("as firmas tomam o preço como dado") + az(".")),
        "poucas": ("O ônus se reparte conforme as " + azb("elasticidades") + " da oferta e da demanda "
                   + azb("de mercado") + ". Ser tomadora de preço é atributo da firma individual e não garante "
                   "repasse integral."),
        "destrinchando": [
            "Imposto específico t: a oferta de mercado sobe t; o comprador paga pc > p₀ e o vendedor recebe "
            "pv = pc − t < p₀. Os dois lados perdem excedente; parte vira receita, parte é " + azb("peso morto")
            + ".",
            "Quem paga mais é o lado menos elástico: parcela do consumidor = " + vd("εˢ / (εˢ + |εᴰ|)")
            + ". Demanda inelástica (gasolina no curto prazo) → consumidor paga mais; oferta inelástica (safra "
            "colhida) → produtor paga mais.",
            "A confusão que o item explora: a firma competitiva enfrenta demanda <b>horizontal</b> ao preço de "
            "mercado, mas a incidência se decide no <b>mercado</b>, onde a demanda é negativamente inclinada. "
            "O imposto muda o próprio preço de mercado, que cada firma depois toma como dado.",
            "Se o raciocínio “firma tomadora de preço” valesse para o mercado, levaria ao contrário do que o "
            "item diz: com demanda de mercado horizontal, o <b>produtor</b> pagaria tudo.",
            "O repasse integral ao consumidor só ocorre com demanda perfeitamente inelástica ou oferta "
            "perfeitamente elástica (indústria de custos constantes no longo prazo).",
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " “Exclusivamente” é o erro principal; a "
                       "justificativa (“visto que as firmas tomam o preço como dado”) é um fato verdadeiro sobre "
                       "a firma usado como causa de algo que não decorre dele. Pista: o item fala do mercado e "
                       "justifica com a firma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em mercado competitivo de custos constantes, no longo prazo, um imposto específico recai "
            "integralmente sobre os consumidores.”</i> → CERTO",
            "<i>“Como a firma competitiva enfrenta demanda horizontal, o imposto específico recai integralmente "
            "sobre os produtores do mercado.”</i> → ERRADO (confunde demanda da firma com demanda de mercado)",
        ])],
        "reescrita": ("A introdução de um imposto específico em um mercado competitivo afeta " + hl("tanto os "
                      "consumidores quanto os produtores") + ", " + hl("na proporção das elasticidades-preço da "
                      "demanda e da oferta de mercado") + "."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["exclusivamente"], "dificuldade": 2,
        "comentario_fonte": "Incidência depende das elasticidades relativas; ônus dividido; o erro está em "
                            "“exclusivamente”; demanda horizontal é da firma, não do mercado.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0538 (mesmo item e mesmo comentário) fundida neste card"],
    },
    # ------------------------------------------------------------------ E1-0957
    {
        "id": "ECO-E1-0957-1", "fonte_ref": "E1-0957", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo ao excedente do consumidor.",
        "rotulo_item": "Item",
        "assertiva": ("O aumento no preço de um bem normal provoca um aumento no excedente dos consumidores, que se "
                      "refere a toda a área abaixo da curva da demanda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O aumento no preço de um bem normal provoca ") + vm("um aumento") + az(" no excedente "
                    "dos consumidores, que se refere a ") + vm("toda a área abaixo da curva da demanda")
                    + az(".")),
        "poucas": ("Preço maior " + vd("reduz") + " o " + azb("excedente do consumidor") + ", que é só a área "
                   "<b>entre a demanda e a linha do preço</b> — não toda a área sob a demanda."),
        "destrinchando": [
            azb("Excedente do consumidor") + " = soma, sobre as unidades compradas, de (disposição a pagar − "
            "preço pago). A disposição a pagar está na altura da curva de demanda; o preço pago, na linha "
            "horizontal p. Logo, EC = área <b>abaixo da demanda e acima do preço</b>, de 0 até q.",
            "A área total sob a demanda até q é o " + azb("benefício bruto") + " (valor total atribuído às "
            "unidades); subtraindo o gasto p × q, sobra o EC.",
            "Quando p sobe de p₁ para p₂, o consumidor perde: (i) o retângulo (p₂ − p₁) × q₂ — paga mais pelas "
            "unidades que continua comprando; (ii) o triângulo entre q₂ e q₁ — o excedente das unidades que "
            "deixou de comprar.",
            "O “bem normal” é distrator: normal/inferior é classificação pela <b>renda</b>, não mexe no efeito "
            "de uma alta de preço sobre o EC.",
            vm("Regra-âncora: EC fica acima do preço e abaixo da demanda; preço sobe → EC cai."),
        ],
        "grafico_verso": "ECO-E1-0957-1-V1",
        "dissecando": (cz("[inversão · meia-verdade]") + " Duas falhas: o sentido do efeito (aumento × "
                       "redução) e a definição, que esquece o “acima do preço”. A segunda é a mais traiçoeira, "
                       "porque “área abaixo da demanda” é a metade verdadeira da definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento no preço de um bem reduz o excedente do consumidor, que corresponde à área entre a "
            "curva de demanda e a linha do preço.”</i> → CERTO",
            "<i>“Uma queda de preço aumenta o excedente do consumidor apenas pelas novas unidades "
            "compradas.”</i> → ERRADO (restrição indevida: também ganha nas unidades que já comprava)",
        ])],
        "reescrita": ("O aumento no preço de um bem normal provoca " + hl("uma redução") + " no excedente dos "
                      "consumidores, que se refere à área abaixo da curva da demanda " + hl("e acima da linha do "
                      "preço") + "."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": ["toda"], "dificuldade": 1,
        "comentario_fonte": "EC é a área abaixo da demanda; com aumento de preço o bem-estar do consumidor "
                            "diminui; as áreas novas seriam pesos mortos.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (315).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; redesenho didático em "
                                   "ECO-E1-0957-1-V1)"},
                          {"ref": "image (313).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}],
        "alertas": ["qualidade_fonte: o comentário de origem confirma o EC como “a área abaixo da curva de "
                    "demanda” (omite o “acima do preço”) e chama de peso morto a perda de EC numa simples alta de "
                    "preço — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L00032
    {
        "id": "ECO-E2-L00032-1", "fonte_ref": "E2-L00032", "destino": "03", "subtema": H2["piso"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("As políticas de preço mínimo estabelecem um valor superior ao preço de equilíbrio de "
                      "mercado com o objetivo de proteger os ofertantes, o que resulta em um aumento do excedente "
                      "do produtor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As políticas de preço mínimo estabelecem um valor <u>superior ao preço de equilíbrio</u> "
                      "de mercado com o objetivo de proteger os ofertantes, o que resulta em um <u>aumento do "
                      "excedente do produtor</u>."),
        "poucas": ("Descreve o " + azb("preço mínimo vinculante") + " do manual: piso acima do equilíbrio, para "
                   "proteger o produtor, que ganha excedente às custas do consumidor — com " + azb("peso morto")
                   + " e excesso de oferta."),
        "destrinchando": [
            "Um piso abaixo do equilíbrio é " + azb("não vinculante") + ": o mercado já paga mais que ele, nada "
            "muda. Por isso, quando se fala da <b>política</b> e de seus efeitos, subentende-se o piso efetivo, "
            "acima de p*.",
            "Efeitos do piso acima de p*: qᴰ cai, qˢ sobe, surge " + azb("excesso de oferta") + " (qˢ − qᴰ). "
            "O consumidor perde A + B (paga mais e compra menos); o produtor ganha A (preço maior nas unidades "
            "vendidas) e perde C (vende menos). Peso morto = " + vd("B + C") + ".",
            "Em geral A > C e o excedente do produtor aumenta; mas, sem compra do excedente pelo governo e com "
            "demanda muito elástica, A pode ser pequeno. E se o produtor fabricar qˢ sem conseguir vender tudo, "
            "o custo das sobras corrói o ganho. O item segue o caso-padrão de livro-texto.",
            rx("No Brasil") + ", a " + azb("Política de Garantia de Preços Mínimos (PGPM)") + ", executada pela "
            + rx("Conab") + ", sustenta o piso agrícola com compra direta de estoques (AGF) e prêmios de "
            "escoamento. Outro piso clássico é o salário mínimo, no mercado de trabalho.",
        ],
        "grafico_verso": "ECO-E2-L00032-1-V1",
        "dissecando": (cz("[literalidade · contraintuitivo]") + " A objeção “nem todo preço mínimo fica acima do "
                       "equilíbrio” é logicamente correta, mas o examinador descreve a política na sua forma "
                       "efetiva — a única que tem efeito a analisar. 🔥 Em C/E, “política de preço mínimo” = piso "
                       "vinculante, salvo menção expressa em contrário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política de preço mínimo acima do equilíbrio eleva o excedente total do mercado.”</i> → "
            "ERRADO (gera peso morto B + C)",
            "<i>“Um preço mínimo fixado abaixo do preço de equilíbrio não altera a quantidade "
            "transacionada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Piso acima do equilíbrio protege o ofertante; reduz EC e gera peso morto; discussão "
                            "sobre piso vinculante × não vinculante; em prova, assume-se o vinculante; PGPM.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 003", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (mecânica da PGPM no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00033
    {
        "id": "ECO-E2-L00033-1", "fonte_ref": "E2-L00033", "destino": "03", "subtema": H2["piso"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Quando uma política de preço mínimo é implementada, o excedente do consumidor é ampliado, o "
                      "que resulta em um aumento do bem-estar do consumidor. Isto ocorre porque a quantidade "
                      "demandada expande devido ao preço inferior ao de equilíbrio, incentivando uma maior "
                      "produção e consumo dentro do mercado regulado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quando uma política de preço mínimo é implementada, o excedente do consumidor é ")
                    + vm("ampliado") + az(", o que resulta em ") + vm("um aumento") + az(" do bem-estar do "
                    "consumidor. Isto ocorre porque a quantidade demandada ") + vm("expande") + az(" devido ao "
                    "preço ") + vm("inferior") + az(" ao de equilíbrio, incentivando uma maior produção")
                    + vm(" e consumo") + az(" dentro do mercado regulado.")),
        "poucas": ("O item descreve um " + azb("preço máximo") + ". O " + azb("preço mínimo") + " fica "
                   "<b>acima</b> do equilíbrio: a quantidade demandada cai e o excedente do consumidor "
                   + vd("diminui") + "."),
        "destrinchando": [
            "Piso vinculante (p<sub>mín</sub> > p*): o consumidor paga mais e compra menos — perde o retângulo "
            "transferido ao produtor e o triângulo das compras que deixou de fazer.",
            "A produção, essa sim, é estimulada: ao preço maior, qˢ > q*. Daí o " + azb("excesso de oferta")
            + " (qˢ − qᴰ), que o governo precisa comprar, estocar, exportar ou deixar encalhar.",
            "Quem ganha: o produtor (em regra, excedente maior). Quem perde: o consumidor. O mercado como um "
            "todo perde o " + azb("peso morto") + ", e o contribuinte ainda paga a compra de estoques, se "
            "houver.",
            "Espelho: o " + azb("preço máximo") + " (teto abaixo de p*) é que reduz o preço ao consumidor — mas "
            "também reduz a quantidade transacionada (os produtores ofertam menos), gerando escassez, não "
            "expansão do consumo.",
            vm("Regra-âncora: piso alto → produto sobrando e consumidor perdendo; teto baixo → fila e produtor "
               "perdendo."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " O item cola no preço mínimo os efeitos "
                       "imaginados de um preço baixo (“preço inferior ao de equilíbrio”). A frase é internamente "
                       "coerente, o que engana; basta checar o ponto de partida: piso = preço <b>acima</b> de "
                       "p*."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política de preço mínimo reduz o excedente do consumidor e estimula a produção, gerando "
            "excesso de oferta.”</i> → CERTO",
            "<i>“O preço máximo abaixo do equilíbrio amplia o consumo, pois o bem fica mais barato.”</i> → "
            "ERRADO (a quantidade transacionada é limitada pela oferta, que cai)",
        ])],
        "reescrita": ("Quando uma política de preço mínimo é implementada, o excedente do consumidor é "
                      + hl("reduzido") + ", o que resulta em " + hl("uma redução") + " do bem-estar do "
                      "consumidor. Isto ocorre porque a quantidade demandada " + hl("se contrai") + " devido ao "
                      "preço " + hl("superior") + " ao de equilíbrio, incentivando uma maior produção"
                      + hl(", mas menor consumo,") + " dentro do mercado regulado."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Preço mínimo reduz o EC: preço acima do equilíbrio reduz a quantidade demandada; o "
                            "EP é que se expande; há peso morto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00034
    {
        "id": "ECO-E2-L00034-1", "fonte_ref": "E2-L00034", "destino": "03", "subtema": H2["piso"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Complementar a política de preço mínimo com incentivos à exportação pode permitir que os "
                      "produtores alcancem um excedente exportável, deslocando a curva de demanda à direita e "
                      "aumentando a quantidade produzida. Isso pode ser uma estratégia eficaz para potencializar "
                      "os ganhos do ofertante, especialmente quando a demanda interna é insuficiente para absorver "
                      "a produção desejada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Complementar a política de preço mínimo com incentivos à exportação <u>pode</u> permitir "
                      "que os produtores alcancem um excedente exportável, deslocando a curva de demanda à direita "
                      "e aumentando a quantidade produzida. Isso <u>pode</u> ser uma estratégia eficaz para "
                      "potencializar os ganhos do ofertante, especialmente quando a demanda interna é insuficiente "
                      "para absorver a produção desejada."),
        "poucas": ("O piso gera " + azb("excesso de oferta") + "; a " + azb("demanda externa") + " soma-se à "
                   "interna (demanda total desloca-se à direita) e absorve as sobras ao preço garantido: o "
                   "produtor vende mais sem que o governo precise estocar tudo."),
        "destrinchando": [
            "Com piso acima do equilíbrio, a quantidade que os produtores querem ofertar (qˢ) supera a que o "
            "mercado interno compra (qᴰ). Sem destino para a diferença, ou o governo compra o estoque, ou o "
            "produto encalha.",
            "Abrir o mercado externo equivale a somar à demanda doméstica uma demanda de exportação: a "
            + azb("demanda total") + " desloca-se para a direita. A esse preço, vende-se mais e o excesso "
            "encolhe ou desaparece; a produção efetivamente vendida aumenta, e com ela o excedente do produtor.",
            "Os moduladores (“pode”, “especialmente”) tornam o item seguro: funciona se o preço externo, somado "
            "ao incentivo, cobrir o preço mínimo. O custo vai para o contribuinte (o incentivo) e, em regra, "
            "para o consumidor doméstico, que continua pagando o piso.",
            "Limite institucional: subsídios à exportação de produtos agrícolas foram proibidos na "
            + azb("OMC") + " pela decisão de " + vd("Nairóbi (2015)") + ", causa defendida pelo "
            + rx("Brasil") + ", grande exportador agrícola prejudicado pelos subsídios de países ricos. "
            "Incentivos à exportação hoje precisam caber nas regras multilaterais.",
            "Na " + rx("PGPM brasileira") + ", o governo pode, em vez de comprar o produto, pagar prêmios para que "
            "o setor privado o escoe para outras regiões a preço que respeite o mínimo — a mesma lógica de "
            "criar demanda adicional em vez de estocar.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O item é protegido por “pode” duas vezes e pelo "
                       "“especialmente”. A tentação de marcar ERRADO vem de achar que só a política de compra "
                       "sustenta o piso; o item apenas descreve um complemento possível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Complementar o preço mínimo com incentivos à exportação elimina necessariamente a perda de "
            "bem-estar do consumidor doméstico.”</i> → ERRADO (modulador absoluto: o consumidor continua pagando "
            "o piso)",
            "<i>“Os incentivos à exportação deslocam para a direita a curva de oferta doméstica.”</i> → ERRADO "
            "(curva trocada: desloca-se a demanda total)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode", "especialmente"], "dificuldade": 2,
        "comentario_fonte": "Exportações ampliam as vendas além do mercado interno; deslocam a demanda à "
                            "direita; ajudam o produtor a alcançar produção maior.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00035
    {
        "id": "ECO-E2-L00035-1", "fonte_ref": "E2-L00035", "destino": "03", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A implementação de um subsídio pelo governo, ao invés de compras diretas de estoque, pode ser "
                      "mais vantajosa em mercados onde a demanda apresenta baixa elasticidade preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A implementação de um subsídio pelo governo, ao invés de compras diretas de estoque, pode "
                       "ser mais vantajosa em mercados onde a demanda apresenta ") + vm("baixa")
                    + az(" elasticidade preço.")),
        "poucas": ("Com demanda " + azb("inelástica") + ", escoar toda a produção exige derrubar muito o preço de "
                   "mercado, e o subsídio (a diferença até o preço garantido, sobre toda a produção) fica caro. "
                   "Comprar o pequeno excedente sai mais barato."),
        "destrinchando": [
            "Mesmo objetivo — garantir ao produtor o preço pₛ, acima do equilíbrio — por dois caminhos:",
            "<b>Compra de estoques</b>: o governo fixa pₛ e compra a sobra. Custo = " + vd("pₛ × (qˢ − qᴰ)")
            + ". Com demanda inelástica, qᴰ quase não cai quando o preço sobe: a sobra é pequena.",
            "<b>Subsídio (pagamento da diferença)</b>: deixa-se o mercado absorver toda a produção qˢ ao preço "
            "pₘ que a demanda aceita, e paga-se ao produtor " + vd("(pₛ − pₘ) × qˢ") + ". Com demanda "
            "inelástica, pₘ precisa cair muito para vender qˢ — a diferença é enorme e incide sobre toda a "
            "produção.",
            "No exemplo do gráfico: compra = " + vd("≈ 9,4") + "; subsídio = " + vd("≈ 23,4") + ". Com demanda "
            "<b>elástica</b>, a lógica se inverte: pₘ cai pouco (subsídio barato) e a sobra a comprar é grande "
            "(estoque caro).",
            "Além do custo fiscal, há diferenças de bem-estar: o subsídio entrega ao consumidor preço baixo e "
            "consumo maior; a compra mantém o consumidor pagando pₛ e gera custos de armazenagem. "
            + rx("No Brasil") + ", a " + rx("PGPM") + " tem os dois tipos de instrumento: compra direta (AGF) e "
            "prêmios equalizadores pagos ao produtor (PEPRO).",
        ],
        "grafico_verso": "ECO-E2-L00035-1-V1",
        "dissecando": (cz("[inversão]") + " A comparação é real e cobrada; o item inverte a condição. Ajuda "
                       "lembrar qual área cresce com a rigidez da demanda: o retângulo do subsídio (pₛ − pₘ) × qˢ "
                       "explode quando a demanda é inclinada demais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A compra direta de estoques tende a ser menos onerosa para o governo que o pagamento da "
            "diferença de preço quando a demanda é inelástica.”</i> → CERTO",
            "<i>“O subsídio ao produtor eleva o preço pago pelo consumidor.”</i> → ERRADO (inversão: o consumidor "
            "paga pₘ, abaixo do equilíbrio)",
        ])],
        "reescrita": ("A implementação de um subsídio pelo governo, ao invés de compras diretas de estoque, pode ser "
                      "mais vantajosa em mercados onde a demanda apresenta " + hl("alta") + " elasticidade "
                      "preço."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["pode"], "dificuldade": 3,
        "comentario_fonte": "Com demanda inelástica, subsidiar cada unidade é mais caro; compras de estoque são "
                            "mais adequadas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00334
    {
        "id": "ECO-E2-L00334-1", "fonte_ref": "E2-L00334", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à incidência tributária.",
        "rotulo_item": "Item",
        "assertiva": ("A incidência econômica de um imposto específico sobre vendas depende da elasticidade-preço "
                      "relativa da oferta e da demanda. Se a demanda for perfeitamente inelástica, todo o ônus do "
                      "imposto recairá sobre o produtor, pois o consumidor não reduzirá a quantidade demandada "
                      "diante do aumento de preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A incidência econômica de um imposto específico sobre vendas depende da elasticidade-preço "
                       "relativa da oferta e da demanda. Se a demanda for perfeitamente inelástica, todo o ônus do "
                       "imposto recairá sobre o ") + vm("produtor") + az(", pois o consumidor não reduzirá a "
                       "quantidade demandada diante do aumento de preço.")),
        "poucas": ("Demanda " + azb("perfeitamente inelástica") + " = consumidor que compra a mesma quantidade a "
                   "qualquer preço: o imposto é repassado por inteiro e o ônus fica com o "
                   + vd("consumidor") + "."),
        "destrinchando": [
            "Demanda vertical (|εᴰ| = 0): a oferta sobe t, o preço ao consumidor sobe " + vd("exatamente t") + " e "
            "a quantidade não muda. O produtor continua recebendo o preço líquido de antes.",
            "Pela fórmula, parcela do consumidor = εˢ / (εˢ + |εᴰ|) = εˢ / εˢ = " + vd("1") + ", qualquer que "
            "seja a oferta (desde que εˢ > 0).",
            "Note a incoerência interna do item: a própria justificativa (“o consumidor não reduzirá a quantidade "
            "diante do aumento de preço”) é o motivo pelo qual <b>ele</b> paga tudo — quem não foge do preço "
            "maior absorve o imposto.",
            "Simetria para memorizar: quem é perfeitamente <b>inelástico</b> paga tudo; quem é perfeitamente "
            "<b>elástico</b> não paga nada. Para o produtor arcar com tudo, seria preciso oferta vertical ou "
            "demanda horizontal.",
            "Como a quantidade não cai, também não há peso morto: o imposto é pura transferência do consumidor "
            "para o governo.",
        ],
        "dissecando": (cz("[troca de ator]") + " A 1ª frase é a regra correta e a premissa (“perfeitamente "
                       "inelástica”) está certa; o erro é só o destinatário do ônus. Pista: a justificativa "
                       "descreve o comportamento de quem <b>paga</b> o imposto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a oferta for perfeitamente inelástica, todo o ônus do imposto recairá sobre o "
            "produtor.”</i> → CERTO",
            "<i>“Com demanda perfeitamente inelástica, o imposto gera peso morto elevado.”</i> → ERRADO (sem "
            "queda de quantidade, peso morto nulo)",
        ])],
        "reescrita": ("A incidência econômica de um imposto específico sobre vendas depende da elasticidade-preço "
                      "relativa da oferta e da demanda. Se a demanda for perfeitamente inelástica, todo o ônus do "
                      "imposto recairá sobre o " + hl("consumidor") + ", pois o consumidor não reduzirá a "
                      "quantidade demandada diante do aumento de preço."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": ["todo"], "dificuldade": 1,
        "comentario_fonte": "Demanda vertical: consumidor absorve todo o aumento; o produtor repassa todo o "
                            "imposto e a quantidade não muda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00337
    {
        "id": "ECO-E2-L00337-1", "fonte_ref": "E2-L00337", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à incidência tributária.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma indústria perfeitamente competitiva de custos constantes, a incidência de um imposto "
                      "ad valorem sobre o consumo recai integralmente sobre os consumidores no longo prazo, uma "
                      "vez que a curva de oferta de longo prazo da indústria é perfeitamente elástica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma indústria perfeitamente competitiva de <u>custos constantes</u>, a incidência de um "
                      "imposto ad valorem sobre o consumo recai integralmente sobre os consumidores <u>no longo "
                      "prazo</u>, uma vez que a curva de oferta de longo prazo da indústria é perfeitamente "
                      "elástica."),
        "poucas": ("Custos constantes → " + azb("oferta de longo prazo horizontal") + " no CMe mínimo. O preço "
                   "líquido do produtor não pode ficar abaixo dele, então o consumidor paga " + vd("todo") + " o "
                   "imposto."),
        "destrinchando": [
            "Longo prazo em concorrência perfeita: livre entrada e saída levam o lucro econômico a zero e o "
            "preço ao " + azb("mínimo do custo médio") + ". Em indústria de " + azb("custos constantes") + " "
            "(a expansão não encarece os insumos), esse mínimo não muda com a escala: a oferta de longo prazo é "
            "uma reta horizontal.",
            "Com o imposto, se o preço líquido caísse abaixo do CMe mínimo, as firmas teriam prejuízo e sairiam "
            "até o preço ao consumidor subir o suficiente para restaurar pv = CMe mín. Resultado: pv inalterado; "
            "pc sobe o valor inteiro do imposto.",
            "Ad valorem ou específico tanto faz aqui: com oferta horizontal, pc = (1 + τ) × CMe mín. A "
            "quantidade cai (a demanda é inclinada) e há peso morto, mas o ônus é todo do consumidor.",
            "No <b>curto prazo</b>, com a oferta inclinada (CMg crescente das firmas existentes), o ônus é "
            "repartido; o repasse integral é resultado de longo prazo. Em indústria de custos crescentes, a "
            "oferta de longo prazo inclina-se e o produtor também arca com parte.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Três qualificadores sustentam o CERTO: "
                       "“perfeitamente competitiva”, “custos constantes” e “longo prazo”. O “integralmente” "
                       "assusta, mas aqui é exato. Retire qualquer um dos três e o item vira ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a incidência recai integralmente sobre os consumidores no curto prazo…”</i> → ERRADO (dado "
            "alterado: no curto prazo a oferta é inclinada)",
            "<i>“Em indústria de custos crescentes, o imposto recai integralmente sobre os consumidores no longo "
            "prazo.”</i> → ERRADO (oferta de longo prazo inclinada: ônus repartido)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["integralmente", "no longo prazo"],
        "dificuldade": 2,
        "comentario_fonte": "Custos constantes: oferta de longo prazo horizontal no CMe mínimo; imposto eleva o "
                            "preço final no valor do imposto; produtor mantém lucro econômico zero.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00390
    {
        "id": "ECO-E2-L00390-1", "fonte_ref": "E2-L00390", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo aos efeitos de tributos sobre firmas competitivas.",
        "rotulo_item": "Item",
        "assertiva": ("A imposição de um imposto de montante fixo (lump-sum tax) sobre todas as empresas de um "
                      "mercado perfeitamente competitivo altera o custo marginal de produção de cada firma, "
                      "deslocando a curva de oferta de curto prazo do mercado para a esquerda e elevando o preço "
                      "de equilíbrio imediato."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A imposição de um imposto de montante fixo (lump-sum tax) sobre todas as empresas de um "
                       "mercado perfeitamente competitivo ") + vm("altera o custo marginal de produção de cada "
                       "firma, deslocando a curva de oferta de curto prazo do mercado para a esquerda e elevando "
                       "o preço de equilíbrio imediato") + az(".")),
        "poucas": ("Imposto de " + azb("montante fixo") + " é " + azb("custo fixo") + ": não depende de q, não "
                   "mexe no " + azb("CMg") + " e, portanto, não desloca a oferta de curto prazo. Só reduz o "
                   "lucro."),
        "destrinchando": [
            "A firma competitiva escolhe q onde " + vd("p = CMg") + ". O CMg é a derivada do custo total em "
            "relação a q; uma parcela fixa T some na derivada. Mesma curva de CMg → mesma oferta individual → "
            "mesma oferta de mercado no curto prazo.",
            "A decisão de produzir ou fechar no curto prazo também não muda: compara-se o preço com o "
            + azb("CVMe") + " mínimo, e o imposto fixo não entra no custo variável (é custo afundado no período).",
            "O que muda é o " + azb("CMe") + " (sobe) e o lucro (cai T). No <b>longo prazo</b>, firmas com lucro "
            "negativo saem; a oferta de mercado se contrai e o preço sobe até o novo mínimo do CMe — aí sim o "
            "preço muda, por saída de firmas.",
            "Contraste: um imposto <b>específico</b> (por unidade) soma-se ao CMg e desloca a oferta já no curto "
            "prazo. É essa a diferença que o item apaga.",
            vm("Regra-âncora: custo fixo afeta lucro e entrada/saída (longo prazo); custo marginal afeta "
               "quantidade e preço (curto prazo)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui a um custo fixo o efeito de um custo variável. A "
                       "cadeia causal que segue (CMg ↑ → oferta ← → preço ↑) é coerente, o que engana; o elo "
                       "falso é o primeiro. Pista: “montante fixo” e “custo marginal” na mesma frase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto de montante fixo sobre as firmas competitivas reduz seus lucros sem alterar a "
            "quantidade ofertada no curto prazo.”</i> → CERTO",
            "<i>“Um imposto de montante fixo jamais afeta o preço de mercado.”</i> → ERRADO (modulador absoluto: "
            "no longo prazo, via saída de firmas, afeta)",
        ])],
        "reescrita": ("A imposição de um imposto de montante fixo (lump-sum tax) sobre todas as empresas de um "
                      "mercado perfeitamente competitivo " + hl("não altera o custo marginal de produção de cada "
                      "firma nem desloca a curva de oferta de curto prazo do mercado, mantendo o preço de "
                      "equilíbrio imediato") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Lump-sum é custo fixo; não altera o CMg; oferta de curto prazo não se desloca; "
                            "efeito só no lucro e na saída de firmas no longo prazo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00391
    {
        "id": "ECO-E2-L00391-1", "fonte_ref": "E2-L00391", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo ao excedente do produtor.",
        "rotulo_item": "Item",
        "assertiva": ("O excedente do produtor de uma firma individual em curto prazo é equivalente ao seu lucro "
                      "econômico somado ao custo fixo total. Graficamente, pode ser mensurado pela área acima da "
                      "curva de Custo Marginal e abaixo do preço de mercado, até o nível de produção escolhido."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O excedente do produtor de uma firma individual em curto prazo é equivalente ao seu lucro "
                      "econômico <u>somado ao custo fixo total</u>. Graficamente, pode ser mensurado pela área "
                      "acima da curva de Custo Marginal e abaixo do preço de mercado, até o nível de produção "
                      "escolhido."),
        "poucas": ("EP = RT − " + azb("CVT") + "; lucro = RT − CVT − CF. Logo " + vd("EP = lucro + CF") + ". E "
                   "somar (p − CMg) unidade a unidade dá exatamente RT − CVT."),
        "destrinchando": [
            "Contas: " + vd("lucro = RT − CVT − CF") + " e " + vd("EP = RT − CVT") + " ⇒ EP = lucro + CF. O "
            "excedente do produtor ignora o custo fixo porque, no curto prazo, ele é pago de qualquer jeito.",
            "Por que a área sob o CMg é o CVT: o CMg é o acréscimo de custo de cada unidade; somando os "
            "acréscimos de 0 a q* obtém-se o custo variável total (" + vd("∫CMg dq = CVT") + "). A área sob o "
            "preço é RT = p × q*. A diferença é a área entre p e o CMg.",
            "Forma equivalente: " + vd("EP = (p − CVMe) × q*") + " — retângulo entre o preço e o custo variável "
            "médio. Mesmo valor, outro desenho.",
            "Consequência: pode haver EP positivo com lucro negativo (se 0 < EP < CF). É o caso da firma que "
            "opera com prejuízo no curto prazo porque p > CVMe: produzindo, perde menos que o CF.",
            "No longo prazo não há custo fixo, e EP de longo prazo coincide com o lucro (mais as rendas de "
            "fatores escassos, no mercado).",
        ],
        "grafico_verso": "ECO-E2-L00391-1-V1",
        "dissecando": (cz("[detalhe · literalidade]") + " Item técnico em duas partes, ambas corretas. O "
                       "tropeço comum é achar que EP = lucro (esquecendo o CF) ou que a área deveria ser entre o "
                       "preço e o CMe. Note “curto prazo”: é ele que dá sentido ao custo fixo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O excedente do produtor de curto prazo equivale ao lucro econômico da firma.”</i> → ERRADO "
            "(falta somar o custo fixo)",
            "<i>“O excedente do produtor pode ser medido por (p − CVMe) × q*.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Lucro = RT − (CV + CF); EP = RT − CVT; logo EP = lucro + CF; área entre preço e CMg.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00392
    {
        "id": "ECO-E2-L00392-1", "fonte_ref": "E2-L00392", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à incidência tributária.",
        "rotulo_item": "Item",
        "assertiva": ("Se a elasticidade-preço da demanda de mercado for perfeitamente inelástica, a introdução de "
                      "um imposto específico sobre a produção recairá integralmente sobre os consumidores, e não "
                      "haverá peso morto (deadweight loss) associado a esse tributo, pois a quantidade transacionada "
                      "no equilíbrio permanecerá inalterada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a elasticidade-preço da demanda de mercado for <u>perfeitamente inelástica</u>, a "
                      "introdução de um imposto específico sobre a produção recairá integralmente sobre os "
                      "consumidores, e não haverá peso morto (deadweight loss) associado a esse tributo, pois a "
                      "<u>quantidade transacionada</u> no equilíbrio permanecerá inalterada."),
        "poucas": ("Demanda vertical: o preço sobe o valor inteiro do imposto (" + vd("ônus 100% do "
                   "consumidor") + ") e a quantidade não muda — sem queda de quantidade, " + vd("peso morto "
                   "zero") + "."),
        "destrinchando": [
            "Imposto sobre a produção: a oferta sobe t. Com demanda vertical em q₀, o novo equilíbrio continua "
            "em q₀, a um preço " + vd("p₀ + t") + ". O produtor segue recebendo p₀.",
            "O " + azb("peso morto") + " mede as trocas mutuamente vantajosas que deixam de ocorrer: é o "
            "triângulo entre qₜ e q₀. Se " + vd("qₜ = q₀") + ", o triângulo tem base zero.",
            "Todo o excedente perdido pelo consumidor (t × q₀) vira receita do governo: é transferência pura, "
            "não destruição de valor. É o fundamento da regra de " + oc("Ramsey") + ": tributar bases "
            "inelásticas minimiza a ineficiência.",
            "Pequena imprecisão de redação: quem é “perfeitamente inelástica” é a demanda, não a elasticidade "
            "(que vale zero). A banca usa a forma coloquial; não muda o julgamento.",
            "Simétrico: com <b>oferta</b> perfeitamente inelástica, também não há peso morto, mas o ônus é todo "
            "do produtor.",
        ],
        "grafico_verso": "ECO-E2-L00392-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " Junta três conclusões corretas do mesmo caso-limite "
                       "(repasse integral, quantidade constante, peso morto nulo) e liga-as pela causa certa. O "
                       "“integralmente” assusta, mas é exato neste extremo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com demanda perfeitamente inelástica, o imposto não gera peso morto, mas é suportado "
            "integralmente pelos produtores.”</i> → ERRADO (troca de ator: pelos consumidores)",
            "<i>“Com demanda perfeitamente elástica, o imposto específico não gera peso morto.”</i> → ERRADO "
            "(a quantidade cai: há peso morto)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["integralmente"], "dificuldade": 1,
        "comentario_fonte": "Demanda vertical: preço sobe exatamente o imposto; quantidade não muda; peso morto "
                            "zero (dQ = 0).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00421
    {
        "id": "ECO-E2-L00421-1", "fonte_ref": "E2-L00421", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à incidência tributária.",
        "rotulo_item": "Item",
        "assertiva": ("Com oferta muito elástica, qualquer imposto indireto necessariamente recai integralmente "
                      "sobre consumidores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Com oferta muito elástica, ") + vm("qualquer") + az(" imposto indireto ")
                    + vm("necessariamente recai integralmente") + az(" sobre consumidores.")),
        "poucas": ("Oferta " + azb("muito") + " elástica faz o consumidor pagar " + vd("a maior parte") + ", "
                   "não tudo. Repasse integral só com oferta " + azb("perfeitamente") + " elástica (εˢ = ∞)."),
        "destrinchando": [
            "Parcela do consumidor = " + vd("εˢ / (εˢ + |εᴰ|)") + ". Com εˢ grande, a fração se aproxima de 1, "
            "mas só a atinge no limite εˢ → ∞ (oferta horizontal). Exemplo: εˢ = 9 e |εᴰ| = 1 → consumidor paga "
            + vd("90%") + "; o produtor, 10%.",
            "Além disso, a parcela depende também da demanda: se ela for igualmente muito elástica, a divisão "
            "fica perto de metade. O item ignora a demanda por completo.",
            "Diferença de vocabulário que a banca explora: “muito elástica” (elasticidade alta, curva achatada) "
            "≠ “perfeitamente elástica” (curva horizontal, elasticidade infinita). O mesmo vale para “pouco” × "
            "“perfeitamente inelástica”.",
            "Caso real de repasse total: indústria competitiva de custos constantes no longo prazo, cuja oferta "
            "é horizontal no CMe mínimo.",
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " Três absolutos (“qualquer”, "
                       "“necessariamente”, “integralmente”) apoiados num grau (“muito”) que não basta. Sempre "
                       "que o item disser “muito/pouco” e concluir “integralmente”, desconfie."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com oferta perfeitamente elástica, um imposto específico recai integralmente sobre os "
            "consumidores.”</i> → CERTO",
            "<i>“Com oferta muito elástica, a maior parte do imposto tende a recair sobre os produtores.”</i> → "
            "ERRADO (inversão: tende a recair sobre os consumidores)",
        ])],
        "reescrita": ("Com oferta muito elástica, " + hl("um") + " imposto indireto " + hl("tende a recair "
                      "majoritariamente") + " sobre consumidores" + hl("; o repasse integral só ocorre com oferta "
                      "perfeitamente elástica") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"],
        "moduladores": ["qualquer", "necessariamente", "integralmente", "muito"], "dificuldade": 1,
        "comentario_fonte": "Incidência depende das elasticidades relativas; repasse total só no limite teórico "
                            "da oferta horizontal.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00438
    {
        "id": "ECO-E2-L00438-1", "fonte_ref": "E2-L00438", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": True,
        "comando": "A respeito dos conceitos e aplicações da elasticidade, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando um mercado de concorrência perfeita com uma curva de demanda decrescente, o "
                      "produtor consegue repassar a totalidade de um tributo aos consumidores quando a "
                      "elasticidade-preço da oferta do bem tributado é infinita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando um mercado de concorrência perfeita com uma curva de demanda decrescente, o "
                      "produtor consegue repassar a totalidade de um tributo aos consumidores quando a "
                      "elasticidade-preço da <u>oferta</u> do bem tributado é <u>infinita</u>."),
        "poucas": ("Oferta com " + azb("elasticidade infinita") + " é horizontal: o produtor não aceita receber "
                   "um centavo a menos que p₀. Com demanda decrescente, o preço ao consumidor sobe " + vd("t "
                   "inteiro") + "."),
        "destrinchando": [
            "Oferta horizontal em p₀ = custo marginal constante: a qualquer preço líquido abaixo de p₀ a "
            "produção vai a zero. Com o imposto, a oferta passa a p₀ + t; o equilíbrio desliza pela demanda até "
            + vd("pc = p₀ + t") + ", com " + vd("pv = p₀") + ".",
            "Fórmula: parcela do consumidor = εˢ / (εˢ + |εᴰ|) → " + vd("1") + " quando εˢ → ∞, desde que |εᴰ| "
            "seja finita — e a hipótese “demanda decrescente” garante isso.",
            "O consumidor paga tudo, mas a quantidade cai (de q₀ para qₜ): há " + azb("peso morto") + ". Repasse "
            "integral não significa ausência de distorção; isso só ocorre com curva vertical.",
            "Quadro-resumo: oferta εˢ = ∞ → consumidor paga 100%; oferta εˢ = 0 → produtor paga 100%; nos casos "
            "intermediários, a divisão depende <b>das duas</b> elasticidades (oferta com elasticidade unitária "
            "não implica divisão meio a meio).",
            "Exemplo: indústria competitiva de custos constantes no longo prazo.",
        ],
        "grafico_verso": "ECO-E2-L00438-1-V1",
        "dissecando": (cz("[detalhe]") + " O item mexe com o reflexo condicionado “elasticidade infinita → "
                       "quem é elástico não paga… mas o produtor perde tudo?”. Leia de quem é a elasticidade: é "
                       "da <b>oferta</b>. Oferta infinitamente elástica protege o produtor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o produtor consegue repassar a totalidade do tributo quando a elasticidade-preço da demanda é "
            "infinita.”</i> → ERRADO (troca de curva: aí o produtor paga tudo)",
            "<i>“Com oferta infinitamente elástica, o tributo não gera peso morto.”</i> → ERRADO (a quantidade "
            "cai)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Oferta perfeitamente elástica: imposto integralmente repassado; fórmula "
                            "ΔPc/t = Es/(Es + |Ed|); paga mais o lado menos elástico; incidência legal irrelevante.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 068", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (quadro-resumo no 📖)"}],
        "alertas": ["qualidade_fonte: a tabela da fonte diz que oferta de elasticidade unitária implica ônus "
                    "“dividido proporcionalmente”, como se bastasse a oferta; a divisão depende também da "
                    "demanda — corrigido"],
    },
]
