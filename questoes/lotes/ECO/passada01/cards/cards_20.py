"""Cards da redação ECO — passada 01 — lote 20 (nota 08 — Monopólio e monopsônio)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "eq": "👑 Equilíbrio do monopólio",
    "mk": "📊 Markup, elasticidade e poder de mercado",
    "disc": "🎟️ Discriminação de preços",
    "nat": "🏛️ Monopólio natural e regulação",
}

COM_ESTR_ITENS = "Sobre as estruturas de mercado, julgue (C ou E) os seguintes itens."
COM_ESTR_FALHAS = ("Em relação às estruturas de mercado e às falhas de mercado, julgue (C ou E) os seguintes "
                   "itens.")
COM_TEORIA_MICRO = "Em relação à teoria microeconômica, julgue (C ou E) os seguintes itens."
COM_MICRO_3 = "Em relação à microeconomia, julgue (C ou E) os seguintes itens."
COM_ESTR_SUBSEQ = "Em relação às estruturas de mercado, julgue (C ou E) os itens subsequentes."
COM_CP_MONOP = ("Em relação às estruturas de mercado de concorrência perfeita e de monopólio, julgue (C ou E) os "
                "itens que se seguem.")
COM_EMPRESAS_MONOP = "A respeito das empresas monopolistas, julgue (C ou E) os itens subsequentes."

CARDS = [
    # ------------------------------------------------------------------ E2-L00290
    {
        "id": "ECO-E2-L00290-1", "fonte_ref": "E2-L00290", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": "Acerca do monopólio e da discriminação de preços, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A discriminação de preços de primeiro grau (perfeita) permite ao monopolista capturar todo o "
                      "excedente do consumidor; contudo, essa prática resulta em uma perda de peso morto maior do "
                      "que a observada no monopólio simples (sem discriminação)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A discriminação de preços de primeiro grau (perfeita) permite ao monopolista capturar todo o "
                      "excedente do consumidor; contudo, essa prática resulta em uma perda de peso morto ")
                   + vm("maior do que") + az(" a observada no monopólio simples (sem discriminação)."),
        "poucas": ("A primeira oração está certa; a segunda inverte o efeito. Na discriminação perfeita o "
                   "monopolista vende até " + vd("P = CMg") + ": a quantidade é a eficiente e o "
                   + azb("peso morto é zero") + " — menor, e não maior, que no monopólio simples."),
        "destrinchando": [
            azb("Monopólio simples") + " (preço único): para vender uma unidade a mais, o monopolista precisa "
            "baixar o preço de <b>todas</b> as unidades, por isso RMg < P. Ele produz onde RMg = CMg, com "
            "P > CMg: ficam de fora consumidores que valorizam o bem acima do custo de produzi-lo. Essas trocas "
            "perdidas são o " + azb("peso morto") + " (o “triângulo de " + oc("Harberger") + "”).",
            azb("Discriminação de 1º grau") + " (perfeita): cada unidade é vendida pelo " + azb("preço de reserva")
            + " de quem a compra. Vender mais uma unidade não derruba o preço das anteriores, então "
            + vd("RMg = P") + " — a demanda vira a própria curva de receita marginal. O monopolista avança até "
            "que o preço de reserva do último comprador iguale o CMg: a quantidade da " + azb("concorrência "
            "perfeita") + ".",
            "Resultado: o excedente total é o máximo possível (" + azb("eficiência de Pareto") + "), mas todo ele "
            "vai para o produtor — " + vd("EC = 0") + ". A discriminação perfeita é péssima para a "
            "<b>distribuição</b> e ótima para a <b>eficiência</b>.",
            "Realismo: exige conhecer a disposição a pagar de cada um e impedir a revenda (arbitragem). Os casos "
            "reais são o 2º grau (preços por quantidade, menus de tarifas) e o 3º grau (segmentos observáveis, "
            "como meia-entrada), que capturam só parte do excedente e têm efeito ambíguo sobre o peso morto.",
            vm("Regra-âncora: extrair excedente (distribuição) ≠ gerar peso morto (eficiência)."),
        ],
        "grafico_verso": "ECO-E2-L00290-1-V1",
        "dissecando": (cz("[inversão · meia-verdade]") + " A 1ª oração é a definição correta e dá confiança; o erro "
                       "vem depois do “contudo”, que inverte o efeito sobre o peso morto. A armadilha é moral: "
                       "parece que “capturar tudo” do consumidor tem de ser “pior” — e é, mas na distribuição, não "
                       "na eficiência. 🔥 A banca alterna os dois lados (EC = 0 × peso morto = 0)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na discriminação perfeita, o excedente total é igual ao que se obteria em concorrência "
            "perfeita.”</i> → CERTO",
            "<i>“Na discriminação perfeita, o excedente do consumidor é igual ao do monopólio simples.”</i> → "
            "ERRADO (o EC cai a zero)",
        ])],
        "reescrita": ("A discriminação de preços de primeiro grau (perfeita) permite ao monopolista capturar todo o "
                      "excedente do consumidor; contudo, essa prática resulta em uma perda de peso morto " + hl("menor do que")
                      + " a observada no monopólio simples (sem discriminação)" + hl(" — na verdade, nula, pois a "
                      "produção vai até P = CMg") + "."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": ["maior do que"], "dificuldade": 2,
        "comentario_fonte": ("Quatro respostas convergentes: discriminação perfeita leva a P = CMg, quantidade de "
                             "concorrência perfeita, peso morto nulo; todo o excedente vai ao produtor; diferença "
                             "é distributiva, não alocativa. Contraste com 2º e 3º graus."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 027", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem de banco de terceiros; mecanismo redesenhado em "
                                   "ECO-E2-L00290-1-V1)"},
                          {"ref": "IMAGEM 028", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (quadro comparativo levado ao 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00332
    {
        "id": "ECO-E2-L00332-1", "fonte_ref": "E2-L00332", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Acerca do monopólio e da discriminação de preços, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A discriminação de preços de primeiro grau (ou discriminação perfeita) permite ao monopolista "
                      "extrair todo o excedente do consumidor, resultando em uma quantidade produzida que é "
                      "socialmente eficiente (onde o preço iguala o custo marginal), eliminando, portanto, o peso "
                      "morto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A discriminação de preços de primeiro grau (ou discriminação perfeita) permite ao monopolista "
                      "extrair todo o excedente do consumidor, resultando em uma quantidade produzida que é "
                      "<u>socialmente eficiente</u> (onde o preço iguala o custo marginal), <u>eliminando</u>, "
                      "portanto, o peso morto."),
        "poucas": ("Cobrando de cada um o " + azb("preço de reserva") + ", o monopolista tem " + vd("RMg = P")
                   + " e produz até " + vd("P = CMg") + ": quantidade de concorrência perfeita, sem peso morto — "
                   "com todo o excedente virando lucro."),
        "destrinchando": [
            "No monopólio de preço único, cada venda extra obriga a baixar o preço de todas as unidades, e "
            "RMg < P; o ótimo (RMg = CMg) fica com P > CMg e quantidade menor que a eficiente — daí o "
            + azb("peso morto") + ".",
            "Na " + azb("discriminação de 1º grau") + ", cada unidade sai pelo preço máximo que aquele comprador "
            "aceita pagar; vender mais uma não reduz o preço das outras. A curva de demanda passa a ser a curva de "
            "receita marginal, e a firma só para quando o preço de reserva do último comprador iguala o CMg.",
            "Essa é exatamente a condição de " + azb("eficiência alocativa") + " (P = CMg): todas as trocas que "
            "geram valor acima do custo acontecem. O bolo é máximo; o que muda é quem fica com ele — "
            + vd("excedente do consumidor = 0") + ", lucro = excedente total.",
            "Comparação de três regimes: concorrência perfeita (eficiente, EC positivo); monopólio simples "
            "(ineficiente, peso morto); discriminação perfeita (eficiente, EC nulo).",
            vm("Regra-âncora: discriminação perfeita = eficiência máxima com distribuição extrema."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " Item verdadeiro que contraria a intuição de que o monopólio "
                       "“mais agressivo” seria também o mais ineficiente. O “portanto” liga corretamente "
                       "P = CMg ao fim do peso morto. Item gêmeo, na versão errada: ECO-E2-L00290-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…resultando em uma quantidade produzida inferior à de concorrência perfeita…”</i> → ERRADO "
            "(é igual: P = CMg)",
            "<i>“…eliminando o peso morto, mas também o lucro econômico do monopolista.”</i> → ERRADO (o lucro é "
            "máximo: absorve todo o excedente)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["portanto"], "dificuldade": 1,
        "comentario_fonte": ("Preço de reserva de cada consumidor; RMg = demanda; produz até P = CMg; todo o "
                             "excedente vira lucro, sem peso morto."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00441
    {
        "id": "ECO-E2-L00441-1", "fonte_ref": "E2-L00441", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": True,
        "comando": "A respeito das estruturas de mercado, julgue (C ou E) os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Um monopolista, para maximizar seu lucro, sempre operará na porção inelástica da curva de "
                      "demanda, pois assim consegue impor preços mais elevados."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um monopolista, para maximizar seu lucro, sempre operará na porção ") + vm("inelástica")
                   + az(" da curva de demanda, ") + vm("pois assim consegue impor preços mais elevados") + az("."),
        "poucas": ("É o contrário: o monopolista opera sempre na porção " + azb("elástica") + " (|ε| > 1). No "
                   "trecho inelástico a " + vd("RMg é negativa") + " e não pode igualar um CMg positivo."),
        "destrinchando": [
            "Relação-chave: " + vd("RMg = P · (1 − 1/|ε|)") + ". Com |ε| > 1, RMg > 0; com |ε| = 1, RMg = 0; com "
            "|ε| < 1, RMg < 0.",
            "O lucro é máximo onde " + vd("RMg = CMg") + ". Como o CMg é positivo, a RMg também precisa ser — o "
            "que só acontece no trecho elástico.",
            "Intuição sem fórmula: se o monopolista estivesse no trecho inelástico, bastaria produzir menos. O "
            "preço subiria proporcionalmente mais do que a quantidade cairia, a receita total aumentaria e o custo "
            "total cairia: lucro maior. Logo, aquele ponto não era o ótimo — ele continua subindo o preço até "
            "entrar no trecho elástico.",
            "Na demanda linear, o ponto médio tem |ε| = 1: a metade de cima (preços altos) é elástica, a de "
            "baixo é inelástica. O monopolista fica na metade de cima — o que desmonta a justificativa do item: "
            "os preços altos ocorrem justamente no trecho <b>elástico</b>.",
            vm("Regra-âncora: monopolista com CMg > 0 nunca opera no trecho inelástico da demanda."),
        ],
        "grafico_verso": "ECO-E2-L00441-1-V1",
        "dissecando": (cz("[inversão · nexo indevido]") + " O item troca elástica por inelástica e cola uma "
                       "justificativa plausível (“impor preços mais elevados”), apoiada na ideia intuitiva de que "
                       "demanda inelástica = poder de mercado. Esse vínculo vale para o <b>markup</b> (Lerner), não "
                       "para o trecho da curva em que a firma opera. 🔥 Tema recorrente: monopólio × trecho elástico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com custo marginal nulo, o monopolista opera no ponto de elasticidade unitária.”</i> → CERTO "
            "(RMg = 0 ⇔ |ε| = 1)",
            "<i>“Quanto mais inelástica a demanda da firma, menor o seu markup.”</i> → ERRADO (inversão: maior)",
        ])],
        "reescrita": ("Um monopolista, para maximizar seu lucro, sempre operará na porção " + hl("elástica")
                      + " da curva de demanda, " + hl("pois só nela a receita marginal é positiva e pode igualar o "
                      "custo marginal") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": ["sempre"], "dificuldade": 2,
        "comentario_fonte": ("Respostas empilhadas convergentes: RMg = P(1 + 1/ε); RMg < 0 no trecho inelástico; "
                             "RMg = CMg > 0 exige |ε| > 1; seguidas de resumo genérico sobre monopólio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00480
    {
        "id": "ECO-E2-L00480-1", "fonte_ref": "E2-L00480", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à teoria microeconômica, julgue (C ou E) os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Sabendo-se que o índice de Lerner (L) tem sempre valor entre 0 e 1, então, para uma empresa "
                      "perfeitamente competitiva, L = 0, e quanto maior for L, maior será o grau de poder de "
                      "monopólio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sabendo-se que o índice de Lerner (L) tem sempre valor entre 0 e 1, então, para uma empresa "
                      "perfeitamente competitiva, <u>L = 0</u>, e quanto <u>maior</u> for L, maior será o grau de "
                      "poder de monopólio."),
        "poucas": ("O " + azb("índice de Lerner") + " é " + vd("L = (P − CMg)/P") + ". Na concorrência perfeita "
                   "P = CMg, logo L = 0; quanto maior a margem do preço sobre o CMg, maior o poder de mercado."),
        "destrinchando": [
            "Proposto por " + oc("Abba Lerner") + " (1934), o índice mede a margem do preço sobre o custo marginal "
            "como fração do preço. É a medida-padrão de " + azb("poder de mercado") + " nos manuais (Pindyck & "
            "Rubinfeld).",
            "Limites: L = 0 quando P = CMg (tomador de preço); L se aproxima de 1 quando o CMg é desprezível "
            "diante do preço. Com CMg ≥ 0 e P ≥ CMg, L fica entre 0 e 1.",
            "Ligação com a elasticidade: no ótimo do monopolista, " + vd("L = 1/|ε|") + " (ou −1/ε). Demanda "
            "da firma menos elástica → L maior. Como o monopolista opera no trecho elástico (|ε| > 1), L < 1.",
            "Atenção: L alto não significa lucro alto. Uma firma com custos fixos elevados pode ter L grande e "
            "lucro zero (P = CMe). O índice mede a <b>capacidade</b> de fixar preço acima do CMg, não a "
            "rentabilidade.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual reproduzida quase à letra. O risco está nos "
                       "extremos: quem confunde Lerner com markup P/CMg (que vale 1, e não 0, na concorrência "
                       "perfeita) marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para uma empresa perfeitamente competitiva, o markup P/CMg é igual a zero.”</i> → ERRADO "
            "(P/CMg = 1; quem vale zero é o Lerner)",
            "<i>“Um índice de Lerner elevado implica necessariamente lucro econômico elevado.”</i> → ERRADO "
            "(custos fixos podem zerar o lucro)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "L = (P − CMg)/P; concorrência perfeita P = CMg, L = 0; maior L, maior poder de monopólio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00534
    {
        "id": "ECO-E2-L00534-1", "fonte_ref": "E2-L00534", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação às estruturas de mercado, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("A imposição de um teto de preços pode aumentar o bem-estar da economia em mercados cuja "
                      "estrutura se caracteriza como um monopólio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de um teto de preços <u>pode</u> aumentar o bem-estar da economia em mercados "
                      "cuja estrutura se caracteriza como um monopólio."),
        "poucas": ("Um " + azb("teto") + " abaixo do preço de monopólio (mas não abaixo do ponto em que a demanda "
                   "cruza o CMg) faz o monopolista vender <b>mais</b>, e o " + vd("peso morto diminui") + "."),
        "destrinchando": [
            "Sem regulação, o monopolista escolhe qm (RMg = CMg) e cobra pm > CMg: há " + azb("peso morto")
            + ".",
            "Com um teto p̄ < pm, cada unidade até a demanda pode ser vendida a p̄: a receita marginal passa a ser "
            "<b>o próprio teto</b> (horizontal) nesse trecho. Se p̄ ≥ CMg, vale a pena vender até onde a demanda "
            "permitir, e a quantidade sobe de qm para q(p̄).",
            "O teto ótimo é aquele em que a demanda cruza o CMg (" + vd("P = CMg") + "): reproduz a quantidade "
            "de concorrência e elimina o peso morto. No monopólio natural, porém, isso gera prejuízo (P < CMe), "
            "e o regulador costuma escolher " + vd("P = CMe") + " (second best, lucro zero).",
            "Teto baixo demais (abaixo do cruzamento entre demanda e CMg) volta a reduzir a quantidade e cria "
            "escassez, como no mercado competitivo. Por isso o item usa “pode”.",
            vm("Regra-âncora: no monopólio, teto entre o CMg e o preço de monopólio aumenta a quantidade."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Quem traz do mercado competitivo a ideia "
                       "de que teto sempre gera escassez e peso morto marca ERRADO. O “pode” salva o item: o "
                       "ganho depende de onde o teto é fixado. Item vizinho, na versão errada: ECO-E2-L01195-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em mercado competitivo, um teto abaixo do preço de equilíbrio aumenta o excedente total.”</i> → "
            "ERRADO (gera escassez e peso morto)",
            "<i>“Qualquer teto inferior ao preço de monopólio aumenta o bem-estar.”</i> → ERRADO (modulador "
            "absoluto: teto baixo demais reduz a quantidade)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("Monopólio cobra P > CMg e gera peso morto; teto adequado (p. ex. no CMe, abaixo de "
                             "Pm) eleva a quantidade e reduz o peso morto."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 088", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo descrito no 📖; gráfico do teto em ECO-E2-L01195-1-V1)"}],
        "alertas": [],
    },
]
