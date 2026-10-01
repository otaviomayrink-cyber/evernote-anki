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
    # ------------------------------------------------------------------ E2-L00619
    {
        "id": "ECO-E2-L00619-1", "fonte_ref": "E2-L00619", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à microeconomia, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a regra de mark-up, o poder de mercado de um monopolista é diretamente "
                      "relacionado à elasticidade-preço da demanda; quanto mais elástica for a demanda, maior será o "
                      "mark-up do preço sobre o custo marginal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a regra de mark-up, o poder de mercado de um monopolista é ")
                   + vm("diretamente") + az(" relacionado à elasticidade-preço da demanda; quanto mais elástica for "
                                            "a demanda, ") + vm("maior") + az(" será o mark-up do preço sobre o "
                                                                             "custo marginal."),
        "poucas": ("A relação é " + azb("inversa") + ": " + vd("(P − CMg)/P = 1/|ε|") + ". Demanda mais "
                   "elástica → consumidores fogem do aumento de preço → markup <b>menor</b>."),
        "destrinchando": [
            "Partindo de RMg = CMg e de RMg = P(1 − 1/|ε|), chega-se à " + azb("regra de markup") + ": "
            + vd("(P − CMg)/P = 1/|ε|") + " ou, na forma de multiplicador, " + vd("P = CMg · |ε|/(|ε| − 1)")
            + ".",
            "Exemplos: |ε| = 2 → P = 2 × CMg (Lerner 0,5); |ε| = 5 → P = 1,25 × CMg (Lerner 0,2); |ε| → ∞ "
            "(firma competitiva) → P = CMg, Lerner 0.",
            "Intuição: a elasticidade mede quanto os clientes reagem ao preço. Se reagem muito, cada real acima "
            "do custo marginal custa muitas vendas, e a firma não sustenta margem alta. O " + azb("poder de "
            "mercado") + " nasce justamente da demanda pouco sensível (poucos substitutos próximos).",
            "Detalhe que a banca cobra: a elasticidade relevante é a da demanda <b>da firma</b>, não a do "
            "mercado. Num oligopólio, cada firma enfrenta demanda mais elástica que a do mercado.",
            vm("Regra-âncora: markup e elasticidade andam em sentidos opostos."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sinal da relação duas vezes, de modo coerente "
                       "(“diretamente” e “maior”), o que lhe dá aparência de raciocínio fechado. Basta testar o "
                       "extremo: demanda perfeitamente elástica = concorrência perfeita = markup nulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com elasticidade-preço da demanda igual a −2, o preço de monopólio é o dobro do custo "
            "marginal.”</i> → CERTO",
            "<i>“Com elasticidade-preço da demanda igual a −0,5, o markup ótimo é de 200%.”</i> → ERRADO (com "
            "|ε| < 1 não há ótimo: o monopolista não opera no trecho inelástico)",
        ])],
        "reescrita": ("De acordo com a regra de mark-up, o poder de mercado de um monopolista é "
                      + hl("inversamente") + " relacionado à elasticidade-preço da demanda; quanto mais elástica "
                      "for a demanda, " + hl("menor") + " será o mark-up do preço sobre o custo marginal."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["diretamente"], "dificuldade": 1,
        "comentario_fonte": ("Relação inversa: (P − CMg)/P = −1/Ed; demanda mais elástica, menor markup, pois a "
                             "firma perde muitos clientes ao elevar o preço."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00652
    {
        "id": "ECO-E2-L00652-1", "fonte_ref": "E2-L00652", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à microeconomia, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("Empresas com poder de mercado buscam capturar o excedente do consumidor por meio de "
                      "estratégias de diferenciação de preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Empresas com <u>poder de mercado</u> buscam capturar o excedente do consumidor por meio de "
                      "estratégias de <u>diferenciação de preços</u>."),
        "poucas": ("A " + azb("discriminação de preços") + " (aqui chamada “diferenciação”) serve exatamente para "
                   "converter excedente do consumidor em receita da firma — e exige " + azb("poder de mercado")
                   + "."),
        "destrinchando": [
            "Com preço único, quem estaria disposto a pagar mais que o preço fica com um " + azb("excedente do "
            "consumidor") + ". Cobrar preços diferentes conforme a disposição a pagar transfere parte dessa área "
            "para a firma.",
            "Condições para discriminar: (1) poder de mercado (o tomador de preço não escolhe preço); (2) "
            "identificar ou separar grupos com disposições a pagar diferentes; (3) impedir a " + azb("revenda")
            + " (arbitragem) entre eles.",
            "Os três graus (" + oc("Pigou") + ", 1920): " + vd("1º grau") + " — preço de reserva de cada "
            "unidade, captura todo o EC; " + vd("2º grau") + " — preço depende da quantidade comprada (descontos "
            "por volume, tarifas em blocos), com autosseleção; " + vd("3º grau") + " — preços diferentes para "
            "grupos observáveis (estudantes, idosos, mercados regionais), maior preço no grupo menos elástico.",
            "Efeito sobre a eficiência: no 1º grau, peso morto zero. No 2º e no 3º, ambíguo — melhora se a "
            "discriminação expandir a quantidade total (atendendo grupos que o preço único excluía), piora se "
            "apenas redistribuir a mesma produção.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item troca o termo técnico “discriminação” por "
                       "“diferenciação de preços” — que não deve ser confundido com diferenciação de "
                       "<b>produto</b> (concorrência monopolística). O verbo “buscam” descreve o objetivo, não "
                       "promete sucesso nem ganho de eficiência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A discriminação de preços de terceiro grau sempre aumenta a eficiência alocativa.”</i> → ERRADO "
            "(modulador absoluto: o efeito é ambíguo)",
            "<i>“Firmas em concorrência perfeita praticam discriminação de preços para capturar o excedente do "
            "consumidor.”</i> → ERRADO (sem poder de mercado não há discriminação)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["buscam"], "dificuldade": 1,
        "comentario_fonte": ("Discriminação transforma excedente do consumidor em excedente do produtor; a fonte "
                             "acrescenta que isso aumenta a eficiência alocativa em relação ao preço único."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem afirma que a discriminação aumenta a eficiência "
                    "alocativa; isso só é garantido no 1º grau — no 2º e no 3º o efeito é ambíguo (corrigido)"],
    },
    # ------------------------------------------------------------------ E2-L00676
    {
        "id": "ECO-E2-L00676-1", "fonte_ref": "E2-L00676", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_ESTR_ITENS,
        "rotulo_item": "Item",
        "assertiva": ("Um monopolista que pratica discriminação de preços de primeiro grau (perfeita) extrai todo o "
                      "excedente do consumidor, resultando em uma quantidade produzida socialmente eficiente, "
                      "idêntica à de concorrência perfeita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um monopolista que pratica discriminação de preços de primeiro grau (perfeita) extrai todo o "
                      "excedente do consumidor, resultando em uma quantidade produzida socialmente eficiente, "
                      "<u>idêntica</u> à de concorrência perfeita."),
        "poucas": ("Com o preço de reserva de cada comprador, a " + vd("RMg coincide com a demanda") + " e o "
                   "monopolista vende até " + vd("P = CMg") + " — a mesma quantidade da concorrência perfeita."),
        "destrinchando": [
            "Na " + azb("discriminação perfeita") + ", vender uma unidade a mais não exige baixar o preço das "
            "anteriores. A receita marginal da última unidade é o próprio preço dela.",
            "A firma expande a produção enquanto o preço de reserva do próximo comprador superar o CMg; para "
            "onde a demanda cruza o CMg — o ponto da " + azb("concorrência perfeita") + ". Resultado: "
            + azb("eficiência alocativa") + ", sem peso morto.",
            "A diferença em relação à concorrência é só distributiva: lá o consumidor fica com o triângulo acima "
            "do preço; aqui " + vd("EC = 0") + " e o produtor fica com tudo.",
            "Ressalva técnica: “idêntica à de concorrência perfeita” supõe as mesmas curvas de custo — a "
            "quantidade em que a demanda corta o CMg da firma.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " Verdadeiro, mas contraria a ideia de que monopólio sempre "
                       "produz menos que a concorrência. 🔥 Itens gêmeos no mesmo lote: ECO-E2-L00332-1 (CERTO) e "
                       "ECO-E2-L00290-1 (versão ERRADA, com peso morto “maior”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…resultando em quantidade socialmente eficiente, mas a um preço único superior ao de concorrência "
            "perfeita.”</i> → ERRADO (não há preço único: cada unidade tem o seu)",
            "<i>“Na discriminação de terceiro grau, a quantidade é sempre idêntica à de concorrência "
            "perfeita.”</i> → ERRADO (troca de conceito: isso vale para o 1º grau)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Preço de reserva de cada consumidor; RMg = demanda; produz até P = CMg; mesma "
                             "quantidade da concorrência perfeita; excedente apropriado como lucro."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00677
    {
        "id": "ECO-E2-L00677-1", "fonte_ref": "E2-L00677", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_ESTR_ITENS,
        "rotulo_item": "Item",
        "assertiva": ("O mark-up de um monopolista é inversamente proporcional à elasticidade-preço da demanda; "
                      "portanto, quanto mais inelástica for a demanda, menor será o poder de mercado da firma."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O mark-up de um monopolista é inversamente proporcional à elasticidade-preço da demanda; "
                      "portanto, quanto mais inelástica for a demanda, ") + vm("menor") + az(" será o poder de "
                                                                                             "mercado da firma."),
        "poucas": ("A premissa está certa (" + vd("L = 1/|ε|") + "), mas a conclusão a inverte: demanda mais "
                   + azb("inelástica") + " (|ε| menor) dá markup e poder de mercado <b>maiores</b>."),
        "destrinchando": [
            "O " + azb("índice de Lerner") + " mede o poder de mercado: " + vd("L = (P − CMg)/P = −1/ε = 1/|ε|")
            + ". É literalmente o inverso da elasticidade (em módulo).",
            "Se |ε| cai (demanda mais inelástica), 1/|ε| sobe: a firma sustenta preço mais distante do CMg sem "
            "perder muitas vendas. Exemplos: medicamento patenteado sem substituto, insumo essencial, serviço "
            "com alto custo de troca.",
            "Se |ε| sobe (demanda mais elástica), 1/|ε| cai; no limite |ε| → ∞, L → 0: a firma é tomadora de "
            "preço.",
            "Cuidado com o limite oposto: a regra vale no ótimo, que fica no trecho elástico (|ε| > 1). Por isso "
            "L fica entre 0 e 1 — “demanda mais inelástica” compara firmas ou mercados, não autoriza o "
            "monopolista a operar com |ε| < 1.",
            vm("Regra-âncora: menos elástica → mais poder de mercado."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 1ª oração é verdadeira e o “portanto” sugere que a "
                       "conclusão decorre dela; mas a dedução foi feita com o sinal trocado. Teste rápido: se "
                       "“inversamente”, então elasticidade baixa → markup alto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto mais inelástica a demanda com que se defronta a firma, maior o índice de Lerner.”</i> → "
            "CERTO",
            "<i>“O índice de Lerner é diretamente proporcional à elasticidade-preço da demanda.”</i> → ERRADO "
            "(inversão: é o inverso de |ε|)",
        ])],
        "reescrita": ("O mark-up de um monopolista é inversamente proporcional à elasticidade-preço da demanda; "
                      "portanto, quanto mais inelástica for a demanda, " + hl("maior") + " será o poder de "
                      "mercado da firma."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["portanto"], "dificuldade": 1,
        "comentario_fonte": ("Lerner L = (P − CMg)/P = −1/Ed; relação inversa correta, conclusão invertida: "
                             "demanda mais inelástica, maior poder de mercado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 103", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (fórmula do Lerner no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00731
    {
        "id": "ECO-E2-L00731-1", "fonte_ref": "E2-L00731", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Considerando os conceitos de microeconomia, julgue (C ou E) os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo de monopólio, o lucro econômico é positivo tanto no curto quanto no longo prazo, "
                      "sendo o preço, no longo prazo, igual ao custo médio de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de monopólio, o lucro econômico ") + vm("é") + az(" positivo tanto no curto "
                      "quanto no longo prazo, sendo o preço, no longo prazo, ") + vm("igual ao") + az(" custo médio "
                                                                                                     "de produção."),
        "poucas": ("Dois erros: o lucro de monopólio <b>pode</b> ser positivo (não é garantido) e, se for positivo, "
                   "o preço fica " + vd("acima do CMe") + ". P = CMe significa lucro zero — e a frase se "
                   "contradiz."),
        "destrinchando": [
            "Lucro econômico por unidade = " + vd("P − CMe") + ". Lucro positivo ⇔ P > CMe; lucro nulo ⇔ "
            "P = CMe. As duas orações do item são, portanto, incompatíveis entre si.",
            "No longo prazo, as " + azb("barreiras à entrada") + " (legais, patentes, controle de recurso, "
            "economias de escala) impedem que novos concorrentes eliminem o lucro: o monopólio <b>pode</b> manter "
            "lucro extraordinário indefinidamente, ao contrário da concorrência perfeita.",
            "Mas monopólio não é garantia de lucro: se a demanda for fraca em relação aos custos, o melhor ponto "
            "(RMg = CMg) pode ter P < CMe — prejuízo no curto prazo; no longo prazo, a firma sai do mercado.",
            "P = CMe no longo prazo é a marca da " + azb("concorrência perfeita") + " (livre entrada, no mínimo "
            "do CMe) e da " + azb("concorrência monopolística") + " (Chamberlin: tangência entre demanda e CMe, "
            "lucro zero).",
            vm("Regra-âncora: monopólio = lucro possível no longo prazo; P = CMe = lucro zero."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " “É positivo” transforma possibilidade "
                       "em certeza, e “igual ao custo médio” importa a condição de longo prazo da concorrência. A "
                       "pista é a contradição interna: lucro positivo com P = CMe é impossível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em razão das barreiras à entrada, o monopolista pode auferir lucro econômico positivo no longo "
            "prazo.”</i> → CERTO",
            "<i>“Na concorrência monopolística, o preço de longo prazo iguala o custo médio, e o lucro econômico "
            "é nulo.”</i> → CERTO",
        ])],
        "reescrita": ("No modelo de monopólio, o lucro econômico " + hl("pode ser") + " positivo tanto no curto "
                      "quanto no longo prazo, sendo o preço, no longo prazo, " + hl("superior ao") + " custo médio "
                      "de produção " + hl("sempre que houver lucro") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["é", "tanto…quanto"], "dificuldade": 2,
        "comentario_fonte": ("Barreiras permitem lucro positivo no longo prazo, mas ele não é necessário; lucro "
                             "positivo exige P > CMe; P = CMe implicaria lucro zero (comentário repetido em linha "
                             "duplicada)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00742
    {
        "id": "ECO-E2-L00742-1", "fonte_ref": "E2-L00742", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_ESTR_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("O monopólio é considerado uma estrutura de mercado imperfeita, na qual apenas uma empresa "
                      "atua nesse segmento. Uma característica do nível ótimo de produção (que maximiza lucro) do "
                      "monopolista é que a empresa nunca opera na parte inelástica da curva de demanda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O monopólio é considerado uma estrutura de mercado imperfeita, na qual apenas uma empresa "
                      "atua nesse segmento. Uma característica do nível ótimo de produção (que maximiza lucro) do "
                      "monopolista é que a empresa <u>nunca</u> opera na parte <u>inelástica</u> da curva de "
                      "demanda."),
        "poucas": ("No trecho " + azb("inelástico") + " a " + vd("RMg é negativa") + ": reduzir a produção "
                   "aumentaria a receita e cortaria custos. O ótimo (RMg = CMg > 0) está sempre no trecho elástico."),
        "destrinchando": [
            "Fórmula: " + vd("RMg = P(1 − 1/|ε|)") + ". Se |ε| < 1, o parêntese é negativo e a RMg também.",
            "Um ponto com RMg < 0 não pode ser ótimo: vendendo menos, a firma ganharia receita (o preço sobe mais "
            "que a quantidade cai) e gastaria menos (produz menos). Ela recua até a RMg voltar a ser positiva.",
            "Com " + vd("CMg > 0") + ", a igualdade RMg = CMg exige RMg > 0 → |ε| > 1. Só no caso-limite de "
            "CMg = 0 o ótimo cai exatamente em |ε| = 1 (maximizar receita).",
            "A 1ª frase também está correta: monopólio é a estrutura de concorrência imperfeita com " + azb("um "
            "único vendedor") + ", produto sem substitutos próximos e barreiras à entrada.",
        ],
        "dissecando": (cz("[literalidade · modulador absoluto]") + " O “nunca” costuma ser sinal de ERRADO, mas "
                       "aqui é exato: com CMg positivo não há exceção. 🔥 A banca repete o tema em várias "
                       "roupagens: ECO-E2-L00441-1 (versão errada) e ECO-E2-L01192-1 (“sempre na parte "
                       "elástica”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopolista maximiza lucro no ponto de elasticidade unitária da demanda.”</i> → ERRADO (isso "
            "só ocorre com CMg nulo; em regra, |ε| > 1)",
            "<i>“No trecho inelástico da demanda, a receita marginal do monopolista é negativa.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "GENERALIZACAO"], "moduladores": ["nunca", "apenas"], "dificuldade": 1,
        "comentario_fonte": ("Demanda inelástica → RMg negativa; reduzir a quantidade eleva preço, receita e "
                             "lucro."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 106", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo redesenhado em ECO-E2-L00441-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00743
    {
        "id": "ECO-E2-L00743-1", "fonte_ref": "E2-L00743", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_ESTR_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("Na regulação de um monopólio natural relativo à prestação de um serviço público, a "
                      "eficiência econômica pode ser obtida por meio da fixação do preço da prestação do serviço "
                      "em patamar equivalente ao seu custo marginal de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Na regulação de um monopólio natural relativo à prestação de um serviço público, a "
                      "eficiência econômica ") + vm("pode ser obtida") + az(" por meio da fixação do preço da "
                      "prestação do serviço em patamar equivalente ao seu custo marginal de produção."),
        "poucas": ("No " + azb("monopólio natural") + " o CMe cai em toda a faixa relevante, logo "
                   + vd("CMg < CMe") + ". Preço = CMg não cobre o custo médio: a empresa tem prejuízo e, sem "
                   "subsídio, sai do mercado."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "P = CMg é, por definição, a regra de " + azb("eficiência alocativa") + " (first best); "
                          "o que falha é a viabilidade financeira. Com subsídio ou tarifa em duas partes, a "
                          "eficiência <b>pode</b> ser obtida — o que torna o item defensável como CERTO. O gabarito "
                          "ERRADO lê “eficiência econômica” como solução regulatória sustentável sem transferência.")],
        "destrinchando": [
            azb("Monopólio natural") + ": uma única firma abastece o mercado a custo menor do que duas ou mais, "
            "graças a " + azb("economias de escala") + " (altos custos fixos de rede, custo marginal baixo): "
            "distribuição de energia, saneamento, gás canalizado, ferrovias.",
            "Se o CMe é decrescente, o CMg fica abaixo dele. No ponto C (demanda = CMg), a quantidade é a "
            "eficiente, mas " + vd("P = CMg < CMe") + ": a receita não paga o custo fixo.",
            "Saídas regulatórias: (1) " + vd("P = CMe") + " (ponto R, " + azb("second best") + "): lucro zero, "
            "quantidade menor que a eficiente, mas sem subsídio; (2) P = CMg com " + azb("subsídio") + " igual ao "
            "prejuízo, pago pelo Tesouro; (3) " + azb("tarifa em duas partes") + ": parcela fixa (assinatura) "
            "cobre o custo fixo e o preço por unidade = CMg.",
            "Sem regulação, o monopolista escolhe RMg = CMg (ponto M): preço alto, quantidade baixa, peso morto.",
            rx("No Brasil") + ", as agências reguladoras (ANEEL, ANP, ANA) usam variantes de preço-teto e "
            "revisão tarifária justamente para conciliar modicidade e equilíbrio econômico-financeiro.",
        ],
        "grafico_verso": "ECO-E2-L00743-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item aplica ao monopólio natural a regra de eficiência do "
                       "mercado competitivo sem considerar o custo fixo. O “pode” deixa a porta aberta — por isso o "
                       "gabarito é discutível. Itens vizinhos: ECO-E2-L01019-1 (ERRADO) e ECO-E2-L01196-1 "
                       "(CERTO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, o preço igual ao custo marginal causaria prejuízo à empresa.”</i> → CERTO",
            "<i>“A regulação pelo custo médio elimina o peso morto do monopólio natural.”</i> → ERRADO (reduz, "
            "mas a quantidade ainda fica abaixo da eficiente)",
        ])],
        "reescrita": ("Na regulação de um monopólio natural relativo à prestação de um serviço público, a "
                      "eficiência econômica " + hl("não pode ser obtida, sem subsídio,") + " por meio da fixação "
                      "do preço da prestação do serviço em patamar equivalente ao seu custo marginal de produção"
                      + hl(", pois esse preço fica abaixo do custo médio e gera prejuízo") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("P = CMg maximiza a eficiência alocativa, mas é insustentável: CMg < CMe gera "
                             "prejuízo; o governo costuma fixar o preço no custo médio (comentário fundido com a "
                             "linha duplicada E2-L00850)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 107", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00743-1-V1)"},
                          {"ref": "IMAGEM 129 (linha duplicada E2-L00850)", "tipo_fonte": "GRÁFICO",
                           "lado": "verso", "acao": "cortada (igual à IMAGEM 107)"}],
        "alertas": ["contestavel: P = CMg é a condição de eficiência alocativa; o item seria CERTO se admitido "
                    "subsídio ou tarifa em duas partes — gabarito ERRADO mantido"],
    },
]
