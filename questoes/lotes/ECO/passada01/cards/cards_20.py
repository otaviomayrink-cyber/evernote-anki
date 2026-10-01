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
                       "P = CMg ao fim do peso morto. Na versão errada, a banca diz que a discriminação perfeita gera "
                       "peso morto “maior” que o do monopólio simples."),
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
        "alertas": ["quase_duplicata: ECO-E2-L00290-1 (versão ERRADA: peso morto “maior”)"],
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
                       "ganho depende de onde o teto é fixado. Na versão errada, a banca diz que o teto “deve "
                       "necessariamente” reduzir a quantidade e gerar excesso de demanda."),
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
        "alertas": ["quase_duplicata: ECO-E2-L01195-1 (teto de preços no monopólio, versão ERRADA)"],
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
                       "produz menos que a concorrência. 🔥 Tema recorrente: a banca o cobra também pelo lado errado, "
                       "dizendo que a discriminação perfeita gera peso morto “maior” que o monopólio simples (ERRADO)."),
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
        "alertas": ["quase_duplicata: ECO-E2-L00332-1 (CERTO) e ECO-E2-L00290-1 (ERRADO) — discriminação perfeita"],
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
                       "roupagens: “sempre operará na porção inelástica” (ERRADO) e “sempre atua na parte "
                       "elástica” (CERTO)."),
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
        "alertas": ["quase_duplicata: ECO-E2-L00441-1 (ERRADO) e ECO-E2-L01192-1 (CERTO) — parte elástica da demanda"],
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
                       "gabarito é discutível. A banca cobra o mesmo ponto como “uma boa forma de regular é fixar o "
                       "preço no custo marginal” (ERRADO) e como “o preço igual ao custo marginal causaria prejuízo "
                       "ao monopolista” (CERTO)."),
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
        "alertas": ["quase_duplicata: ECO-E2-L01019-1 (ERRADO) e ECO-E2-L01196-1 (CERTO) — P = CMg no monopólio natural", "contestavel: P = CMg é a condição de eficiência alocativa; o item seria CERTO se admitido "
                    "subsídio ou tarifa em duas partes — gabarito ERRADO mantido"],
    },
    # ------------------------------------------------------------------ E2-L00811
    {
        "id": "ECO-E2-L00811-1", "fonte_ref": "E2-L00811", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_TEORIA_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("Para empresas monopolistas, ocorrerá um ótimo de produção sempre que suas receitas marginais "
                      "forem iguais aos seus custos marginais, pois, nesse ponto, os excedentes serão máximos e, "
                      "portanto, não haverá peso morto nesse mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para empresas monopolistas, ocorrerá um ótimo de produção sempre que suas receitas "
                      "marginais forem iguais aos seus custos marginais, ") + vm("pois, nesse ponto, os excedentes "
                      "serão máximos e, portanto, não haverá peso morto") + az(" nesse mercado."),
        "poucas": ("RMg = CMg maximiza o <b>lucro</b>, não o excedente total. Como " + vd("P > RMg = CMg")
                   + ", o monopolista produz menos que o eficiente e gera " + azb("peso morto") + "."),
        "destrinchando": [
            "A regra " + vd("RMg = CMg") + " vale para <b>qualquer</b> firma maximizadora de lucro: enquanto a "
            "receita da unidade adicional supera o custo dela, vale produzir mais; quando fica abaixo, vale "
            "produzir menos. Até aqui o item está certo.",
            "Na concorrência perfeita, RMg = P, então o ótimo privado coincide com o social (P = CMg). No "
            + azb("monopólio") + ", a demanda é negativamente inclinada e RMg < P: no ótimo, " + vd("P > CMg")
            + ".",
            "Entre a quantidade de monopólio (qm) e a eficiente (qc), há consumidores dispostos a pagar mais do "
            "que o custo de produzir e que ficam sem o bem. Essas trocas perdidas formam o " + azb("peso morto")
            + " (triângulo PM).",
            "Repartição do bem-estar: parte do antigo excedente do consumidor vira lucro (transferência); outra "
            "parte simplesmente desaparece (peso morto). Excedente total máximo só com P = CMg — ou na "
            "discriminação perfeita.",
            vm("Regra-âncora: ótimo privado do monopolista (RMg = CMg) ≠ ótimo social (P = CMg)."),
        ],
        "grafico_verso": "ECO-E2-L00811-1-V1",
        "dissecando": (cz("[nexo indevido · meia-verdade]") + " A 1ª parte (RMg = CMg) é verdadeira; o erro foi "
                       "colado no “pois”, que atribui ao ótimo privado uma propriedade do ótimo social. 🔥 O mesmo "
                       "texto foi cobrado de novo no Pré-TPS/2023."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No ótimo do monopolista, o preço supera o custo marginal, o que gera perda de peso morto.”</i> → "
            "CERTO",
            "<i>“Somente as firmas competitivas maximizam lucro igualando receita marginal e custo "
            "marginal.”</i> → ERRADO (restrição indevida: vale para todas)",
        ])],
        "reescrita": ("Para empresas monopolistas, ocorrerá um ótimo de produção sempre que suas receitas "
                      "marginais forem iguais aos seus custos marginais, " + hl("mas, como nesse ponto o preço "
                      "supera o custo marginal, os excedentes não serão máximos e haverá peso morto") + " nesse "
                      "mercado."),
        "tipo_erro": ["NEXO_INDEVIDO", "MEIA_VERDADE"], "moduladores": ["sempre", "portanto"], "dificuldade": 1,
        "comentario_fonte": ("RMg = CMg vale para toda estrutura de mercado; no monopólio, porém, os excedentes "
                             "não são máximos: parte do EC vira lucro e parte é peso morto; P > CMg."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: mesma assertiva de ECO-E2-L01020-1 (Nabuco Pré-TPS/2023); mantidos os dois por serem de provas diferentes"],
    },
    # ------------------------------------------------------------------ E2-L00812
    {
        "id": "ECO-E2-L00812-1", "fonte_ref": "E2-L00812", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_TEORIA_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("Se o monopolista consegue discriminar perfeitamente o preço do seu produto, então se diz que "
                      "o mercado é eficiente no sentido de Pareto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o monopolista consegue discriminar <u>perfeitamente</u> o preço do seu produto, então se "
                      "diz que o mercado é <u>eficiente no sentido de Pareto</u>."),
        "poucas": ("Na discriminação perfeita, a firma vende até " + vd("P = CMg") + ": todas as trocas "
                   "mutuamente vantajosas acontecem, e ninguém pode melhorar sem que outro piore — "
                   + azb("ótimo de Pareto") + "."),
        "destrinchando": [
            azb("Eficiência de Pareto") + " (" + oc("Vilfredo Pareto") + "): situação em que não é possível "
            "melhorar alguém sem piorar outro. Num mercado, equivale a esgotar as trocas em que a disposição a "
            "pagar supera o custo marginal — ou seja, produzir até P = CMg.",
            "Na " + azb("discriminação de 1º grau") + ", cada unidade é vendida pelo preço de reserva do "
            "comprador, a RMg coincide com a demanda e o monopolista produz até a demanda cruzar o CMg. O "
            "excedente total é máximo; " + vd("peso morto = 0") + ".",
            "Qualquer mudança que aumentasse o excedente do consumidor reduziria o lucro (é só transferência); "
            "e o lucro já é o máximo possível. Logo, não há melhoria de Pareto disponível.",
            "Pareto não é justiça: a alocação é eficiente com " + vd("EC = 0") + ". O critério não julga a "
            "distribuição — por isso a discriminação perfeita é eficiente e, ao mesmo tempo, extremamente "
            "desigual.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " A palavra “monopolista” induz a associar ineficiência; o "
                       "advérbio “perfeitamente” é o que muda o gabarito. Troque por “com preço único” e o item "
                       "vira ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopolista que cobra preço único produz uma alocação eficiente no sentido de Pareto.”</i> → "
            "ERRADO (P > CMg: há peso morto)",
            "<i>“Na discriminação perfeita, a alocação é Pareto-eficiente, embora o excedente do consumidor seja "
            "nulo.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["perfeitamente"], "dificuldade": 1,
        "comentario_fonte": ("Discriminação de 1º grau: vende cada unidade ao preço de reserva, extrai todo o EC; "
                             "resultado Pareto-eficiente, pois o lucro já é máximo e o EC só aumentaria reduzindo-o."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00867
    {
        "id": "ECO-E2-L00867-1", "fonte_ref": "E2-L00867", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação às estruturas de mercado, julgue (C ou E) os itens que se seguem.",
        "rotulo_item": "Item",
        "assertiva": ("Quanto menor a elasticidade-preço da demanda pelo produto produzido por uma empresa "
                      "monopolista, maior será o índice de Lerner."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto <u>menor</u> a elasticidade-preço da demanda pelo produto produzido por uma empresa "
                      "monopolista, <u>maior</u> será o índice de Lerner."),
        "poucas": ("No ótimo, " + vd("L = (P − CMg)/P = 1/|ε|") + ": elasticidade menor (em módulo) → "
                   + azb("índice de Lerner") + " maior → mais poder de monopólio."),
        "destrinchando": [
            "O " + azb("índice de Lerner") + " (" + oc("Abba Lerner") + ", 1934) mede a distância entre o preço "
            "praticado e o preço concorrencial (o CMg), como fração do preço. Varia de 0 (concorrência perfeita) "
            "a perto de 1.",
            "Da condição RMg = CMg e de RMg = P(1 − 1/|ε|) sai " + vd("L = −1/ε") + ". Como ε é negativo, isso é "
            "o mesmo que 1/|ε|.",
            "Números: |ε| = 4 → L = 0,25; |ε| = 2 → L = 0,5; |ε| = 1,25 → L = 0,8. Menos elástica, maior a "
            "margem que a firma consegue sustentar.",
            "Leitura de “menor elasticidade”: sempre em <b>valor absoluto</b>. Quem lê ε = −4 como “menor” que "
            "ε = −2 inverte a conclusão. Na dúvida, pense em “menos sensível ao preço”.",
            vm("Regra-âncora: Lerner = 1/|ε| — menos elástica, mais poder."),
        ],
        "dissecando": (cz("[literalidade]") + " Aplicação direta da fórmula. A armadilha é de sinal: a banca "
                       "escreve “menor elasticidade” sem dizer “em módulo”. 🔥 O mesmo item foi cobrado "
                       "de novo no Pré-TPS/2023."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a elasticidade-preço da demanda, em valor absoluto, maior o índice de Lerner.”</i> "
            "→ ERRADO (inversão)",
            "<i>“Se a demanda da firma for perfeitamente elástica, o índice de Lerner será nulo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("L = (P − CMg)/P = −1/Ed; quanto menos elástica a demanda, maior a diferença entre "
                             "preço e custo marginal e maior o poder de mercado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 135", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (definição do Lerner no 📖)"}],
        "alertas": ["quase_duplicata: mesma assertiva de ECO-E2-L01018-1 (Nabuco Pré-TPS/2023); mantidos os dois por serem de provas diferentes"],
    },
    # ------------------------------------------------------------------ E2-L00993
    {
        "id": "ECO-E2-L00993-1", "fonte_ref": "E2-L00993", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_MICRO_3,
        "rotulo_item": "Item",
        "assertiva": ("A Teoria do Consumidor se refere às tentativas do monopolista de cobrar preços diferentes a "
                      "grupos distintos de pessoas como discriminação de preços. Em relação a essa prática, a "
                      "discriminação de 1º grau levará a uma solução ótima de Pareto e a discriminação de 3º grau "
                      "se baseia em características observáveis dos consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A Teoria do Consumidor se refere às tentativas do monopolista de cobrar preços diferentes a "
                      "grupos distintos de pessoas como discriminação de preços. Em relação a essa prática, a "
                      "discriminação de <u>1º grau</u> levará a uma solução ótima de Pareto e a discriminação de "
                      "<u>3º grau</u> se baseia em características observáveis dos consumidores."),
        "poucas": ("Os dois pontos julgáveis estão certos: o " + vd("1º grau") + " leva a P = CMg (ótimo de "
                   "Pareto) e o " + vd("3º grau") + " segmenta por características " + azb("observáveis")
                   + " (idade, condição de estudante, região)."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A abertura atribui à “Teoria do Consumidor” um tema que os manuais tratam na teoria da "
                          "<b>firma</b>/monopólio. A banca do curso desconsiderou a imprecisão; numa prova "
                          "CEBRASPE, ela poderia render ERRADO ou anulação. O conteúdo econômico do item está "
                          "correto.")],
        "destrinchando": [
            "Classificação de " + oc("Pigou") + " (1920), sistematizada por " + oc("Varian") + ": "
            + vd("1º grau") + " — cada unidade ao preço de reserva de quem a compra (discriminação perfeita); "
            + vd("2º grau") + " — preço por unidade varia com a <b>quantidade</b> comprada (descontos por volume, "
            "pacotes), e o consumidor se autosseleciona; " + vd("3º grau") + " — preços diferentes para "
            "<b>grupos</b> identificáveis, cada um pagando preço uniforme.",
            "1º grau: a RMg é o próprio preço da última unidade; o monopolista produz até a demanda cruzar o "
            "CMg (P = CMg). Excedente total máximo → " + azb("ótimo de Pareto") + ", com EC = 0.",
            "3º grau: a firma separa mercados por traços observáveis (idosos, estudantes, residentes) "
            "associados a elasticidades diferentes, e cobra " + vd("mais do grupo menos elástico") + " (regra "
            "do markup aplicada a cada mercado: RMg₁ = RMg₂ = CMg).",
            "Efeito de bem-estar do 3º grau: ambíguo. Condição necessária para aumentar o excedente total é a "
            "discriminação <b>expandir a produção</b> total (por exemplo, abrindo um mercado que o preço único "
            "deixava sem atendimento).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " As duas afirmações finais são definições de manual. O "
                       "ruído está na 1ª frase (“Teoria do Consumidor”), redigida de forma truncada: em item "
                       "longo, julgue cada oração e pondere se a imprecisão é material — aqui a banca entendeu que "
                       "não era."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A discriminação de 2º grau baseia-se em características observáveis dos consumidores.”</i> → "
            "ERRADO (troca de conceito: 2º grau = quantidade/autosseleção; observáveis = 3º grau)",
            "<i>“Na discriminação de 3º grau, cobra-se preço maior no mercado de demanda mais elástica.”</i> → "
            "ERRADO (inversão: maior no menos elástico)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Definições de 1º grau (preço de reserva, extrai todo o EC, P = CMg, eficiente de "
                             "Pareto) e de 3º grau (características observáveis, elasticidades diferentes); "
                             "discriminação só eleva o bem-estar se expandir a produção."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: a 1ª frase situa a discriminação de preços na “Teoria do Consumidor” "
                    "(imprecisão); gabarito CERTO da fonte mantido"],
    },
    # ------------------------------------------------------------------ E2-L00995
    {
        "id": "ECO-E2-L00995-1", "fonte_ref": "E2-L00995", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_MICRO_3,
        "rotulo_item": "Item",
        "assertiva": ("Em setores caracterizados como monopólios naturais, o nível de produção competitivo, embora "
                      "eficiente no sentido de Pareto, não é lucrativo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em setores caracterizados como monopólios naturais, o nível de produção competitivo, embora "
                      "eficiente no sentido de Pareto, <u>não é lucrativo</u>."),
        "poucas": ("O nível competitivo é onde " + vd("P = CMg") + " (eficiente). No " + azb("monopólio natural")
                   + " o CMe é decrescente e fica acima do CMg; logo, nesse ponto " + vd("P < CMe") + " — "
                   "prejuízo."),
        "destrinchando": [
            "Monopólio natural surge de " + azb("economias de escala") + " na faixa relevante: o CMe cai até "
            "quantidades que atendem todo o mercado, e uma firma produz mais barato do que duas.",
            "Relação marginal × média: se o CMe está caindo, o CMg está <b>abaixo</b> dele (cada unidade extra "
            "custa menos que a média e a puxa para baixo).",
            "A demanda cruza o CMg (ponto de " + azb("eficiência alocativa") + ") num trecho em que o CMe ainda "
            "está acima: preço = CMg não paga os custos fixos. A firma teria prejuízo igual a (CMe − CMg) × q e "
            "sairia do mercado sem subsídio.",
            "Por isso o regulador escolhe entre: preço = CMe (lucro zero, quantidade abaixo da eficiente), preço "
            "= CMg com subsídio, ou tarifa em duas partes (parte fixa cobre o custo fixo).",
            vm("Regra-âncora: monopólio natural → CMg < CMe → P = CMg dá prejuízo."),
        ],
        "dissecando": (cz("[literalidade]") + " Afirmação de manual, com “embora” separando eficiência (verdadeira) "
                       "de viabilidade (o ponto decisivo). Trocar “não é lucrativo” por “gera lucro normal” "
                       "tornaria o item ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, a fixação do preço no custo médio produz o nível de produção eficiente no "
            "sentido de Pareto.”</i> → ERRADO (P = CMe dá quantidade menor que a eficiente)",
            "<i>“No monopólio natural, o custo marginal situa-se abaixo do custo médio na faixa relevante de "
            "produção.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["embora"], "dificuldade": 1,
        "comentario_fonte": ("Monopólio natural: retornos crescentes de escala, CTMe decrescente, CMg abaixo do "
                             "CMe; P = CMg < CTMe causa prejuízo e saída da firma."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 165", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo redesenhado em ECO-E2-L00743-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01018
    {
        "id": "ECO-E2-L01018-1", "fonte_ref": "E2-L01018", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ESTR_SUBSEQ,
        "rotulo_item": "Item",
        "assertiva": ("Quanto menor a elasticidade-preço da demanda pelo produto produzido por uma empresa "
                      "monopolista, maior será o índice de Lerner."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto <u>menor</u> a elasticidade-preço da demanda pelo produto produzido por uma empresa "
                      "monopolista, <u>maior</u> será o índice de Lerner."),
        "poucas": ("Pela " + azb("regra do markup") + ", " + vd("L = (P − CMg)/P = −1/ε") + ". Elasticidade "
                   "menor em módulo → o inverso é maior → Lerner maior."),
        "destrinchando": [
            "Derivação em uma linha: lucro máximo ⇒ RMg = CMg; como RMg = P(1 + 1/ε), vem P(1 + 1/ε) = CMg ⇒ "
            + vd("(P − CMg)/P = −1/ε") + ".",
            "Interpretação: o " + azb("poder de monopólio") + " vem da falta de substitutos próximos. Quem "
            "enfrenta clientes pouco sensíveis ao preço consegue preço bem acima do custo marginal.",
            "Mercado × firma: a elasticidade que importa é a da demanda <b>que a firma enfrenta</b>. No "
            "monopólio, coincide com a do mercado; em oligopólio, é maior que a do mercado, e o Lerner de cada "
            "firma é menor.",
            "Limites: firma competitiva (|ε| infinito) → L = 0; monopolista sempre com |ε| > 1 → L < 1. Lerner "
            "mede a margem, não o lucro (custos fixos podem anulá-lo).",
        ],
        "dissecando": (cz("[literalidade]") + " O mesmo item aparece, idêntico, em outra prova: sinal de tema "
                       "recorrente 🔥. A única forma de errar é ler “menor elasticidade” com sinal (−4 < −2) em vez "
                       "de módulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O índice de Lerner é igual ao inverso da elasticidade-preço da demanda do mercado, qualquer que "
            "seja a estrutura de mercado.”</i> → ERRADO (generalização: vale a elasticidade da demanda da firma)",
            "<i>“Quanto menos elástica a demanda pelo produto de um monopolista, maior o seu poder de "
            "monopólio.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("L = (P − CMg)/P = −1/Epd; demanda menos elástica em valor absoluto implica Lerner e "
                             "poder de monopólio maiores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 173", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (fórmula no 📖)"}],
        "alertas": ["quase_duplicata: mesma assertiva de ECO-E2-L00867-1 (Nabuco, sem ano); mantidos os dois por serem de provas diferentes"],
    },
    # ------------------------------------------------------------------ E2-L01019
    {
        "id": "ECO-E2-L01019-1", "fonte_ref": "E2-L01019", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ESTR_SUBSEQ,
        "rotulo_item": "Item",
        "assertiva": ("Uma boa forma de regular um monopolista natural é exigir que ele fixe seu preço igual aos "
                      "custos marginais oriundos de determinada atividade econômica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma boa forma de regular um monopolista natural é exigir que ele fixe seu preço igual aos ")
                   + vm("custos marginais") + az(" oriundos de determinada atividade econômica."),
        "poucas": ("No monopólio natural, " + vd("CMg < CMe") + ": preço = CMg gera prejuízo e a firma sai do "
                   "mercado sem subsídio. A regra usual é " + vd("preço = custo médio") + "."),
        "destrinchando": [
            "O " + azb("monopólio natural") + " tem CMe decrescente em toda a faixa relevante (custos fixos "
            "altos, custo marginal baixo). Com CMe caindo, o CMg está abaixo dele.",
            "Exigir P = CMg reproduz a quantidade eficiente, mas com P < CMe: a receita não cobre o custo fixo. "
            "A firma acumula prejuízo, deixa de investir e, no limite, abandona o serviço.",
            "Alternativas: " + vd("P = CMe") + " (" + azb("second best") + ": lucro zero, pequena perda de "
            "eficiência); P = CMg mais " + azb("subsídio") + " público; " + azb("tarifa em duas partes") + " "
            "(assinatura fixa + preço = CMg por unidade); e regimes de incentivo, como o " + azb("price cap")
            + " (preço-teto reajustado por inflação menos um fator de produtividade).",
            "Problemas práticos da regulação pelo custo: assimetria de informação (o regulador não conhece os "
            "custos reais) e baixo incentivo à eficiência quando o preço acompanha o custo.",
            vm("Regra-âncora: monopólio natural → regulação pelo custo médio, não pelo marginal."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Transporta a regra de eficiência do mercado competitivo "
                       "para um setor com custos médios decrescentes. A expressão “boa forma de regular” exige "
                       "viabilidade, que P = CMg não oferece. A versão certa do mesmo ponto: “no monopólio natural, o "
                       "preço igual ao custo marginal causaria prejuízo ao monopolista”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma forma de regular um monopolista natural é fixar o preço no custo médio, o que lhe garante "
            "lucro econômico nulo.”</i> → CERTO",
            "<i>“No monopólio natural, a regulação pelo custo médio leva à quantidade socialmente ótima.”</i> → "
            "ERRADO (a quantidade ótima é a de P = CMg)",
        ])],
        "reescrita": ("Uma boa forma de regular um monopolista natural é exigir que ele fixe seu preço igual aos "
                      + hl("custos médios") + " oriundos de determinada atividade econômica" + hl(", pois o preço "
                      "igual ao custo marginal geraria prejuízo") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["boa forma"], "dificuldade": 1,
        "comentario_fonte": ("CMe decrescente implica CMg < CMe; P = CMg gera prejuízo sem subsídio; alternativa "
                             "comum é P = CMe."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01196-1 (versão CERTA: P = CMg causa prejuízo)"],
    },
    # ------------------------------------------------------------------ E2-L01020
    {
        "id": "ECO-E2-L01020-1", "fonte_ref": "E2-L01020", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ESTR_SUBSEQ,
        "rotulo_item": "Item",
        "assertiva": ("Para empresas monopolistas, ocorrerá um ótimo de produção sempre que suas receitas marginais "
                      "forem iguais aos seus custos marginais, pois, nesse ponto, os excedentes serão máximos e, "
                      "portanto, não haverá peso morto nesse mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para empresas monopolistas, ocorrerá um ótimo de produção sempre que suas receitas "
                      "marginais forem iguais aos seus custos marginais, ") + vm("pois, nesse ponto, os excedentes "
                      "serão máximos e, portanto, não haverá peso morto") + az(" nesse mercado."),
        "poucas": ("Como a RMg fica abaixo da demanda, no ótimo " + vd("RMg = CMg < P") + ": a firma maximiza o "
                   "lucro, mas produz menos que o eficiente — há " + azb("peso morto") + "."),
        "destrinchando": [
            "Para vender mais, o monopolista baixa o preço de todas as unidades: por isso a curva de "
            + azb("receita marginal") + " fica abaixo da demanda (na demanda linear, com o dobro da "
            "inclinação).",
            "No ótimo privado (RMg = CMg), o preço lido na demanda é maior que o CMg. Toda unidade entre a "
            "quantidade de monopólio e a eficiente valeria mais para o consumidor do que custa produzir — e não "
            "é produzida.",
            "Excedente total máximo exige " + vd("P = CMg") + " (concorrência perfeita ou discriminação "
            "perfeita). No monopólio simples, o excedente total encolhe: parte do EC vira lucro, parte vira "
            + azb("peso morto") + ".",
            "Consequência para política pública: a ineficiência do monopólio justifica a " + azb("defesa da "
            "concorrência") + " (no " + rx("Brasil") + ", o CADE, Lei 12.529/2011) e a regulação de preços nos "
            "monopólios naturais.",
        ],
        "dissecando": (cz("[nexo indevido]") + " Mesma assertiva de uma prova anterior (Nabuco, sem ano), cobrada de "
                       "novo no Pré-TPS/2023 🔥. O conector “pois” liga a regra de lucro máximo a uma conclusão de "
                       "bem-estar que ela não sustenta; desconfie de “portanto, não haverá peso morto” em "
                       "monopólio de preço único."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para empresas monopolistas, ocorrerá um ótimo de produção sempre que suas receitas marginais "
            "forem iguais aos seus custos marginais.”</i> → CERTO",
            "<i>“No ótimo do monopolista, preço e receita marginal coincidem.”</i> → ERRADO (P > RMg; só na "
            "concorrência perfeita ou na discriminação perfeita P = RMg)",
        ])],
        "reescrita": ("Para empresas monopolistas, ocorrerá um ótimo de produção sempre que suas receitas "
                      "marginais forem iguais aos seus custos marginais, " + hl("mas, nesse ponto, o preço supera o "
                      "custo marginal, os excedentes não serão máximos e haverá peso morto") + " nesse mercado."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["sempre", "portanto"], "dificuldade": 1,
        "comentario_fonte": ("RMg abaixo da demanda: RMg = CMg < P; P > CMg, bem-estar não maximizado, peso "
                             "morto; quantidade menor e preço maior que na concorrência perfeita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: mesma assertiva de ECO-E2-L00811-1 (Nabuco, sem ano); mantidos os dois por serem de provas diferentes"],
    },
    # ------------------------------------------------------------------ E2-L01021
    {
        "id": "ECO-E2-L01021-1", "fonte_ref": "E2-L01021", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ESTR_SUBSEQ,
        "rotulo_item": "Item",
        "assertiva": ("Permitir que as empresas discriminem preços leva a ganhos de bem-estar dos consumidores e "
                      "maiores lucros dos empresários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Permitir que as empresas discriminem preços leva a ") + vm("ganhos de bem-estar") + az(" dos "
                      "consumidores e maiores lucros dos empresários."),
        "poucas": ("O lucro tende a subir (a firma captura " + azb("excedente do consumidor") + "), mas o efeito "
                   "sobre os consumidores é " + vd("ambíguo") + ": uns pagam menos, outros mais; no 1º grau, o "
                   "excedente do consumidor chega a zero."),
        "destrinchando": [
            "Lucro: discriminar nunca reduz o lucro de quem pode fazê-lo, porque a firma sempre poderia voltar ao "
            "preço único. A discriminação existe justamente para transformar " + azb("excedente do consumidor")
            + " em receita.",
            "Consumidores, por grau: " + vd("1º grau") + " — EC = 0 (todo o excedente vai para a firma); "
            + vd("3º grau") + " — o grupo menos elástico paga mais e perde; o mais elástico paga menos e pode "
            "ganhar; o saldo para os consumidores como um todo pode ser negativo.",
            "Bem-estar total (EC + lucro): pode aumentar se a discriminação <b>expandir a quantidade</b> — por "
            "exemplo, atendendo um grupo que o preço único excluía (meia-entrada que lota sessões vazias, "
            "remédios mais baratos em países pobres). Se apenas redistribui a mesma quantidade, tende a reduzir.",
            "Por isso o tratamento antitruste é caso a caso: a discriminação não é ilícita em si, mas pode ser "
            "abusiva quando usada para excluir concorrentes.",
            vm("Regra-âncora: discriminação → lucro ↑; consumidores → efeito ambíguo."),
        ],
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " A metade sobre o lucro é verdadeira; a "
                       "metade sobre os consumidores generaliza um efeito que é, no máximo, possível. O verbo "
                       "“leva a” afirma resultado certo, sem “pode”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A discriminação de preços pode elevar o excedente total, se permitir atender consumidores "
            "excluídos pelo preço único.”</i> → CERTO",
            "<i>“Na discriminação de preços de primeiro grau, o excedente do consumidor é máximo.”</i> → ERRADO "
            "(inversão: é nulo)",
        ])],
        "reescrita": ("Permitir que as empresas discriminem preços leva a " + hl("efeito ambíguo sobre o bem-estar")
                      + " dos consumidores e maiores lucros dos empresários."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["leva a"], "dificuldade": 1,
        "comentario_fonte": ("Lucro maior em geral; efeito ambíguo sobre consumidores (mercados elásticos pagam "
                             "menos, outros mais); bem-estar total só aumenta se a quantidade se expandir."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01192
    {
        "id": "ECO-E2-L01192-1", "fonte_ref": "E2-L01192", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_CP_MONOP,
        "rotulo_item": "Item",
        "assertiva": "Uma empresa monopolista sempre atua na parte elástica da curva de demanda.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma empresa monopolista <u>sempre</u> atua na parte <u>elástica</u> da curva de demanda."),
        "poucas": ("O ótimo exige " + vd("RMg = CMg > 0") + ", e a RMg só é positiva onde " + vd("|ε| > 1")
                   + ". No trecho inelástico, RMg < 0: reduzir a produção elevaria a receita e o lucro."),
        "destrinchando": [
            "Fórmula de ligação: " + vd("RMg = P(1 − 1/|ε|)") + ". Trecho elástico → RMg > 0; elasticidade "
            "unitária → RMg = 0; trecho inelástico → RMg < 0.",
            "Prova por absurdo: suponha o monopolista no trecho inelástico. Se ele cortar a produção, o preço sobe "
            "proporcionalmente mais do que a quantidade cai, a receita total sobe e o custo total cai. O lucro "
            "aumenta — logo o ponto inicial não era ótimo.",
            "Na demanda linear p = a − bq, a RMg = a − 2bq corta o eixo na metade da quantidade máxima, "
            "exatamente onde |ε| = 1. O monopolista fica sempre à esquerda desse ponto.",
            "Limite: com " + vd("CMg = 0") + " (custo marginal desprezível, como em bens digitais), o ótimo é "
            "RMg = 0, no ponto de elasticidade unitária. Fora desse caso-limite, a regra é estrita.",
            "Não confundir com a regra do markup: demanda menos elástica dá markup maior <i>entre firmas</i> "
            "(" + vd("L = 1/|ε|") + "), mas cada monopolista escolhe, na sua própria curva, um ponto do trecho "
            "elástico — por isso L fica sempre abaixo de 1.",
        ],
        "dissecando": (cz("[literalidade · modulador absoluto]") + " O “sempre” assusta, mas aqui é a regra de "
                       "manual (o único caso-limite, CMg nulo, não é cobrado). 🔥 O tema volta em versões "
                       "invertidas: “sempre operará na porção inelástica” → ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma empresa monopolista sempre atua na parte inelástica da curva de demanda, onde consegue "
            "preços mais altos.”</i> → ERRADO (inversão: RMg < 0 no trecho inelástico)",
            "<i>“Com custo marginal nulo, o monopolista maximiza lucro onde a elasticidade-preço da demanda é "
            "unitária.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Demanda inelástica → RMg negativa; o monopólio nunca produz na parte inelástica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 202", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo redesenhado em ECO-E2-L00441-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00441-1 (versão ERRADA: “porção inelástica”)"],
    },
    # ------------------------------------------------------------------ E2-L01193
    {
        "id": "ECO-E2-L01193-1", "fonte_ref": "E2-L01193", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_CP_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("Quanto mais elástica a curva de demanda pelo produto de um monopolista, maior é o seu poder "
                      "de monopólio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto mais elástica a curva de demanda pelo produto de um monopolista, ") + vm("maior")
                   + az(" é o seu poder de monopólio."),
        "poucas": ("O " + azb("índice de Lerner") + " é " + vd("L = 1/|ε|") + ": demanda mais elástica → markup "
                   "<b>menor</b> → menos poder de monopólio."),
        "destrinchando": [
            "Poder de monopólio = capacidade de fixar preço acima do custo marginal, medida por "
            + vd("L = (P − CMg)/P") + " (entre 0 e 1). No ótimo, " + vd("L = −1/Ed") + ".",
            "Se Ed é grande em módulo, o markup é pequeno: os consumidores trocam de produto ao menor aumento. "
            "Se Ed é pequena, o markup é grande: os consumidores pouco reagem.",
            "A elasticidade relevante é a da demanda da <b>empresa individual</b>, não a do mercado. A regra vale "
            "para qualquer empresa com poder de mercado (monopólio, oligopólio, concorrência monopolística).",
            "Determinantes da elasticidade da firma: elasticidade da demanda de mercado, número de concorrentes e "
            "forma de interação entre eles (conluio reduz a elasticidade percebida; guerra de preços a aumenta).",
            vm("Regra-âncora: mais elástica → menos poder; menos elástica → mais poder."),
        ],
        "dissecando": (cz("[inversão]") + " Inversão pura do sentido da relação. Par espelhado na mesma bateria "
                       "de questões: “menos elástica… maior” → CERTO. Teste-limite: demanda "
                       "infinitamente elástica = firma competitiva = poder nulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade da demanda da firma for −5, o índice de Lerner será 0,2.”</i> → CERTO",
            "<i>“O poder de monopólio depende da elasticidade da demanda de mercado, e não da demanda da "
            "empresa.”</i> → ERRADO (inversão: é a da empresa)",
        ])],
        "reescrita": ("Quanto mais elástica a curva de demanda pelo produto de um monopolista, " + hl("menor")
                      + " é o seu poder de monopólio."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Lerner L = (P − CMg)/P = −1/Ed; Ed da empresa individual; Ed grande, markup pequeno; "
                             "Ed pequena, markup grande."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01197-1 (par espelhado, CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L01194
    {
        "id": "ECO-E2-L01194-1", "fonte_ref": "E2-L01194", "destino": "08", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_CP_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("Uma empresa em concorrência perfeita maximiza lucros quando iguala o preço de determinado "
                      "produto ao seu custo marginal. Uma empresa monopolista maximiza lucros quando sua receita "
                      "marginal é maior que o custo marginal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma empresa em concorrência perfeita maximiza lucros quando iguala o preço de determinado "
                      "produto ao seu custo marginal. Uma empresa monopolista maximiza lucros quando sua receita "
                      "marginal é ") + vm("maior que o") + az(" custo marginal."),
        "poucas": ("Qualquer firma maximiza lucro onde " + vd("RMg = CMg") + ". Na concorrência perfeita, RMg = P, "
                   "por isso a regra vira P = CMg; o monopolista também iguala RMg e CMg — só que com P acima "
                   "deles."),
        "destrinchando": [
            "Lógica marginal: enquanto " + vd("RMg > CMg") + ", cada unidade extra acrescenta mais à receita do "
            "que ao custo — o lucro ainda cresce e vale produzir mais. Se " + vd("RMg < CMg") + ", vale "
            "produzir menos. O máximo está na igualdade.",
            azb("Concorrência perfeita") + ": a firma é tomadora de preço; vender mais uma unidade rende "
            "exatamente P. Logo RMg = P, e a condição é P = CMg (no trecho crescente do CMg).",
            azb("Monopólio") + ": a demanda é negativamente inclinada; RMg < P. A condição continua RMg = CMg; o "
            "preço é lido na demanda, acima do CMg (markup).",
            "Condição de segunda ordem: o CMg deve cortar a RMg <b>de baixo para cima</b>. E condição de "
            "operação no curto prazo: P ≥ CVMe (senão, fecha).",
            vm("Regra-âncora: RMg = CMg é universal; P = CMg é o caso particular da concorrência."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A 1ª frase é verdadeira e cria a impressão de "
                       "que cada estrutura tem uma regra própria. O erro está no “maior que”: RMg > CMg descreve "
                       "um ponto em que ainda vale expandir, não o ótimo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Tanto a firma competitiva quanto o monopolista maximizam lucro igualando receita marginal e "
            "custo marginal.”</i> → CERTO",
            "<i>“No ótimo, o monopolista iguala o preço ao custo marginal.”</i> → ERRADO (troca de conceito: "
            "iguala RMg a CMg, com P > CMg)",
        ])],
        "reescrita": ("Uma empresa em concorrência perfeita maximiza lucros quando iguala o preço de determinado "
                      "produto ao seu custo marginal. Uma empresa monopolista maximiza lucros quando sua receita "
                      "marginal é " + hl("igual ao") + " custo marginal."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Enquanto RMg > CMg o lucro aumenta; quando RMg < CMg, diminui; máximo em "
                             "RMg = CMg para monopolista e firma competitiva."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01195
    {
        "id": "ECO-E2-L01195-1", "fonte_ref": "E2-L01195", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_CP_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("A fixação de um preço máximo para o produto de um monopolista deve necessariamente implicar a "
                      "redução da quantidade produzida por esse monopolista e, portanto, um excesso de demanda no "
                      "mercado desse produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A fixação de um preço máximo para o produto de um monopolista ") + vm("deve necessariamente "
                      "implicar a redução da quantidade produzida") + az(" por esse monopolista e, portanto, ")
                   + vm("um excesso de demanda") + az(" no mercado desse produto."),
        "poucas": ("O monopólio não tem curva de oferta. Um " + azb("teto") + " abaixo do preço de monopólio, mas "
                   "acima do CMg, faz a firma vender <b>mais</b> (até a demanda), sem escassez."),
        "destrinchando": [
            "No mercado competitivo, o teto abaixo do equilíbrio reduz a quantidade ofertada (anda-se para baixo "
            "na curva de oferta) e cria " + azb("excesso de demanda") + ". O item transporta esse raciocínio "
            "para o monopólio.",
            "O monopolista não tem curva de oferta: escolhe a quantidade em que RMg = CMg e lê o preço na "
            "demanda. Com um teto p̄ < pm, cada unidade até a demanda é vendida a p̄; a " + azb("receita "
            "marginal") + " passa a ser o próprio teto (horizontal) nesse trecho.",
            "Se p̄ ≥ CMg, compensa vender tudo o que a demanda absorve a esse preço: a quantidade sobe de qm para "
            "q(p̄), o preço cai e o " + azb("peso morto") + " encolhe. Não há fila: a firma atende toda a "
            "demanda ao preço-teto.",
            "Só um teto <b>abaixo</b> do ponto em que a demanda cruza o CMg reproduz o resultado competitivo: a "
            "firma produz onde CMg = p̄, a quantidade cai e aparece escassez. Daí o erro do “necessariamente”.",
            vm("Regra-âncora: no monopólio, teto bem calibrado aumenta a quantidade."),
        ],
        "grafico_verso": "ECO-E2-L01195-1-V1",
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " Aplica ao monopólio a análise de teto do "
                       "mercado competitivo e a blinda com “necessariamente”. Pista: “quantidade produzida por esse "
                       "monopolista” pressupõe uma curva de oferta que o monopólio não tem. Na versão certa, "
                       "a banca diz que um teto de preços “pode aumentar o bem-estar” num monopólio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A fixação de um preço máximo entre o custo marginal e o preço de monopólio pode elevar a "
            "quantidade produzida pelo monopolista.”</i> → CERTO",
            "<i>“Em mercado competitivo, o preço máximo abaixo do equilíbrio gera excesso de oferta.”</i> → "
            "ERRADO (gera excesso de demanda)",
        ])],
        "reescrita": ("A fixação de um preço máximo para o produto de um monopolista " + hl("pode implicar o "
                      "aumento da quantidade produzida") + " por esse monopolista e, portanto, " + hl("a redução do "
                      "peso morto, sem excesso de demanda,") + " no mercado desse produto" + hl(", se o teto ficar "
                      "entre o custo marginal e o preço de monopólio") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["necessariamente", "portanto"],
        "dificuldade": 2,
        "comentario_fonte": ("Monopólio não tem curva de oferta; com preço máximo abaixo do preço de monopólio, a "
                             "quantidade é determinada pela demanda e aumenta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00534-1 (versão CERTA: teto pode aumentar o bem-estar)"],
    },
    # ------------------------------------------------------------------ E2-L01196
    {
        "id": "ECO-E2-L01196-1", "fonte_ref": "E2-L01196", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_EMPRESAS_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("No monopólio natural, o preço socialmente ótimo (igual ao custo marginal) causaria prejuízo "
                      "ao monopolista."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No monopólio natural, o preço socialmente ótimo (igual ao custo marginal) <u>causaria "
                      "prejuízo</u> ao monopolista."),
        "poucas": ("Com CMe decrescente, " + vd("CMg < CMe") + ". O preço eficiente (P = CMg) fica abaixo do custo "
                   "médio: a receita não cobre os custos fixos — " + azb("prejuízo") + "."),
        "destrinchando": [
            azb("Monopólio natural") + ": " + azb("economias de escala") + " em toda a faixa relevante — uma "
            "firma atende o mercado a custo menor que várias. Típico de redes: energia, água, gás, ferrovia.",
            "Matemática da média: quando a média cai, a unidade marginal está abaixo dela. Logo, na interseção "
            "demanda × CMg, o CMe ainda está acima: " + vd("prejuízo = (CMe − CMg) × q") + ".",
            "Saídas: preço = CMe (" + azb("second best") + ", lucro zero), preço = CMg com subsídio, ou tarifa "
            "em duas partes (assinatura cobre o custo fixo; preço unitário = CMg).",
            "Sem regulação, o monopolista escolhe RMg = CMg: preço alto, quantidade baixa e peso morto — razão "
            "da regulação tarifária desses setores.",
        ],
        "dissecando": (cz("[literalidade]") + " Conclusão-padrão do gráfico de monopólio natural. Itens vizinhos "
                       "cobram o mesmo ponto pelo lado errado (ERRADO): “uma boa forma de regular é fixar o preço no "
                       "custo marginal” e “a eficiência pode ser obtida com preço igual ao custo marginal”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, o preço igual ao custo médio gera lucro econômico positivo.”</i> → ERRADO "
            "(gera lucro zero)",
            "<i>“No monopólio natural, o preço socialmente ótimo exige subsídio para que a firma permaneça no "
            "mercado.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Preço igual ao CMg gera produção eficiente com preço abaixo do custo médio: "
                             "prejuízo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 203", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo redesenhado em ECO-E2-L00743-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01019-1 e ECO-E2-L00743-1 (versões ERRADAS: P = CMg)"],
    },
    # ------------------------------------------------------------------ E2-L01197
    {
        "id": "ECO-E2-L01197-1", "fonte_ref": "E2-L01197", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_EMPRESAS_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("Quanto menos elástica a curva de demanda pelo produto de um monopolista, maior é o seu poder "
                      "de monopólio no mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto <u>menos elástica</u> a curva de demanda pelo produto de um monopolista, "
                      "<u>maior</u> é o seu poder de monopólio no mercado."),
        "poucas": ("Pela regra do markup, " + vd("(P − CMg)/P = 1/|ε|") + ": demanda menos elástica permite preço "
                   "mais distante do custo marginal — mais " + azb("poder de monopólio") + "."),
        "destrinchando": [
            "O " + azb("índice de Lerner") + " L = (P − CMg)/P varia de 0 a 1; quanto maior, maior o poder de "
            "monopólio. Expresso pela elasticidade: " + vd("L = −1/Ed") + ".",
            "Se Ed for grande (em módulo), o markup será pequeno; se Ed for pequena, o markup será grande. Ex.: "
            "|Ed| = 1,5 → L ≈ 0,67; |Ed| = 3 → L ≈ 0,33.",
            "Fontes de demanda pouco elástica: ausência de substitutos próximos (patentes, marcas fortes), "
            "custos de troca, essencialidade do bem, peso pequeno no orçamento.",
            "Usos práticos: autoridades de concorrência (no " + rx("Brasil") + ", o CADE) olham elasticidades "
            "para delimitar o mercado relevante e avaliar o poder de mercado em fusões.",
        ],
        "dissecando": (cz("[literalidade]") + " Espelho de “mais elástica… maior” (ERRADO), "
                       "na mesma bateria de questões. A banca alterna o par para testar se o candidato guardou o "
                       "<b>sentido</b> da relação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto menos elástica a demanda, menor o markup do monopolista sobre o custo marginal.”</i> → "
            "ERRADO (inversão)",
            "<i>“O poder de monopólio pode ser medido pelo índice de Lerner, que é nulo em concorrência "
            "perfeita.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Lerner L = (P − CMg)/P = −1/Ed; Ed da empresa individual; Ed pequena, markup "
                             "grande."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01193-1 (par espelhado, ERRADO)"],
    },
    # ------------------------------------------------------------------ E2-L01198
    {
        "id": "ECO-E2-L01198-1", "fonte_ref": "E2-L01198", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_EMPRESAS_MONOP,
        "rotulo_item": "Item",
        "assertiva": ("Um monopólio natural decorre da posse por parte de uma empresa da única fonte de um insumo "
                      "natural que é necessário para a produção de determinado bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um monopólio natural decorre ") + vm("da posse por parte de uma empresa da única fonte de "
                                                           "um insumo natural que é necessário para a "
                                                           "produção de determinado bem") + az("."),
        "poucas": ("O " + azb("monopólio natural") + " decorre de " + vd("economias de escala") + " na faixa "
                   "relevante (CMe decrescente), não da posse de um recurso. Controle de insumo único é outra "
                   "barreira: o " + azb("monopólio de recurso") + "."),
        "destrinchando": [
            "Na tipologia de " + oc("Mankiw") + " (<i>Introdução à Economia</i>), os monopólios nascem de três "
            "fontes: (1) " + azb("recurso-chave") + " controlado por uma só firma (o caso descrito no item; ex. "
            "clássico, a De Beers nos diamantes); (2) " + azb("monopólio criado pelo governo") + " (patentes, "
            "direitos autorais, concessões exclusivas); (3) " + azb("monopólio natural") + ", quando uma firma "
            "atende o mercado inteiro a custo menor que duas ou mais.",
            "No monopólio natural, a barreira é tecnológica: com custos fixos altos (redes de água, energia, "
            "gás) e custo marginal baixo, o CMe cai ao longo de toda a demanda relevante. O incumbente tem custo "
            "médio menor que qualquer entrante pequeno.",
            "Formalmente, há " + azb("subaditividade de custos") + ": C(q) < C(q₁) + C(q₂) para q₁ + q₂ = q. "
            "Economias de escala em toda a faixa são condição suficiente para isso.",
            "O adjetivo “natural” confunde: não se refere a recursos naturais, mas ao fato de o monopólio surgir "
            "“naturalmente” da estrutura de custos, sem proteção legal.",
            vm("Regra-âncora: monopólio natural = custos (escala); monopólio de recurso = posse do insumo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item explora a palavra “natural” para descrever o "
                       "monopólio de recurso (“insumo natural”). Pista: a causa apontada é a posse, e não os "
                       "custos — o critério que define o monopólio natural."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um monopólio natural surge quando uma única empresa pode abastecer todo o mercado a custo menor "
            "do que duas ou mais empresas.”</i> → CERTO",
            "<i>“O monopólio natural depende de proteção legal contra a entrada de concorrentes.”</i> → ERRADO "
            "(a barreira é de custo, não legal)",
        ])],
        "reescrita": ("Um monopólio natural decorre " + hl("de economias de escala na faixa relevante de produção, "
                      "que permitem a uma única empresa abastecer todo o mercado a custo menor do que duas ou "
                      "mais; a posse da única fonte de um insumo necessário caracteriza o monopólio de recurso") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Monopólio natural: uma firma abastece o mercado a custo menor; retornos crescentes de "
                             "escala; CTMe decrescente; barreira à entrada pelo custo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01404
    {
        "id": "ECO-E2-L01404-1", "fonte_ref": "E2-L01404", "destino": "08", "subtema": H2["mk"],
        "tipo": "C/E", "banca": "FGV", "prova": "Senado Federal/Consultor Legislativo/2022", "ano": 2022,
        "cacd": False, "errei": False,
        "comando": ("Julgue o item a seguir, adaptado de questão da FGV, relativo ao mark-up do monopolista e à "
                    "elasticidade-preço da demanda."),
        "rotulo_item": "Item",
        "assertiva": ("O mark-up do monopolista tende a ser menor quanto mais elástica for a demanda, sendo que se "
                      "essa for perfeitamente elástica, o preço será igual à solução de concorrência perfeita."),
        "gabarito": "CERTO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("O mark-up do monopolista tende a ser <u>menor</u> quanto <u>mais elástica</u> for a demanda, "
                      "sendo que se essa for <u>perfeitamente elástica</u>, o preço será igual à solução de "
                      "concorrência perfeita."),
        "poucas": ("Markup: " + vd("(P − CMg)/P = 1/|ε|") + ". Se |ε| cresce, o markup cai; com |ε| → ∞, "
                   "1/|ε| = 0 e " + vd("P = CMg") + " — o preço de concorrência perfeita."),
        "destrinchando": [
            azb("Regra do markup") + ": do ótimo RMg = CMg e de RMg = P(1 − 1/|ε|), obtém-se "
            + vd("P = CMg / (1 − 1/|ε|)") + " ou, no formato de Lerner, " + vd("(P − CMg)/P = 1/|ε|") + ".",
            "Quanto mais elástica a demanda, menor a margem: |ε| = 2 → P = 2·CMg; |ε| = 5 → P = 1,25·CMg; "
            "|ε| = 20 → P ≈ 1,05·CMg.",
            "No limite da demanda " + azb("perfeitamente elástica") + " (horizontal, |ε| = ∞), qualquer aumento "
            "de preço zera as vendas: a firma é tomadora de preço, RMg = P e o ótimo é " + vd("P = CMg")
            + ". É a situação da firma em concorrência perfeita.",
            "Lição: o “monopólio” sem demanda inclinada não tem poder de mercado. O poder vem da inclinação da "
            "demanda que a firma enfrenta, não do número de vendedores em si.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz a regra do markup e o seu caso-limite. "
                       "O “tende a” suaviza a primeira oração; a segunda é o teste de extremo que a FGV gosta de "
                       "usar. Se a banca trocasse “perfeitamente elástica” por “perfeitamente inelástica”, o item "
                       "viraria ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a demanda for perfeitamente inelástica, o mark-up do monopolista será nulo.”</i> → ERRADO "
            "(inversão: o nulo é no perfeitamente elástico; no inelástico não há ótimo)",
            "<i>“Com elasticidade-preço da demanda igual a −4, o preço do monopolista supera o custo marginal em "
            "cerca de 33%.”</i> → CERTO (P = CMg × 4/3)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Verso só com imagens: markup (P − CMg)/P cai com a elasticidade; com ε = ∞, 1/ε = 0, "
                             "markup nulo e P = CMg (concorrência perfeita)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 320", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (regra do markup no 📖)"},
                          {"ref": "IMAGEM 321", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (caso ε = ∞ no 📖)"}],
        "alertas": ["nota_redacao: gabarito resolvido — a fonte não traz gabarito explícito; as imagens do verso e o conteúdo "
                    "indicam CERTO"],
    },
]
