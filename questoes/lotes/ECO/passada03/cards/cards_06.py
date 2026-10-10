"""Cards do lote de redação 06 — ECO, passada 03 (nota 66: câmbio e política cambial)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "reg": "💱 Regimes cambiais",
    "real": "📏 Câmbio nominal × real e PPC",
    "det": "📈 Determinantes do câmbio",
}

CMD_JUROS = ("Acerca dos determinantes da taxa de câmbio e de seus efeitos sobre o comércio exterior, julgue o item "
             "a seguir.")

CMD_REG = "Acerca dos regimes cambiais, julgue o item a seguir."

CMD_CACD26 = ("Acerca de macroeconomia aberta, regime cambial e determinação da taxa de câmbio, julgue o item "
              "subsequente, considerando o texto a seguir.")

EXCERTO_CACD26 = (
    "<p><i>Em economias abertas, choques de confiança e alterações no prêmio de risco podem afetar fluxos de "
    "capitais e pressionar a taxa de câmbio. A resposta de política econômica — incluindo-se o uso de juros, "
    "intervenção e reservas — depende, entre outros fatores, do regime cambial vigente e das restrições impostas "
    "pelo grau de mobilidade de capitais. Ademais, distinções conceituais entre taxa de câmbio nominal e taxa de "
    "câmbio real são relevantes para analisar preços relativos e competitividade, assim como para discutir "
    "mecanismos de transmissão do câmbio para a inflação.</i></p>"
)

ALERTA_JUROS = "quase_duplicata: ECO-E1-0426-1, ECO-E1-0427-1, ECO-E1-0428-1 (mesmo enunciado com variações de sentido)"

ALERTA_CLIP = ("quase_duplicata: ECO-E1-0763-1, ECO-E1-0764-1, ECO-E1-0765-1, ECO-E1-0766-1 (mesmo simulado; "
               "troca fixo × flutuante)")

CARDS = [
    # ------------------------------------------------------------------ E1-0369
    {
        "id": "ECO-E1-0369-1", "fonte_ref": "E1-0369", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos da taxa de câmbio sobre o comércio exterior, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A desvalorização da moeda acarreta necessariamente a melhora da balança comercial, tanto no "
                      "longo quanto no curto prazos."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("A desvalorização da moeda ") + vm("acarreta necessariamente") + az(" a melhora da balança "
                    "comercial") + vm(", tanto no longo quanto no curto prazos") + az(".")),
        "poucas": ("Item anulado por vagueza, mas a resposta mais defensável seria ERRADO: a melhora "
                   "<b>não é necessária</b> (depende da " + azb("condição de Marshall-Lerner") + ") e, no curto "
                   "prazo, o saldo costuma <b>piorar</b> antes de melhorar (" + azb("curva J") + ")."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o item foi anulado sem justificativa preservada na fonte. Motivo provável: o efeito da "
                          "desvalorização depende de elasticidades, da pauta de comércio e do horizonte, e a banca "
                          "considerou a redação imprecisa demais para um julgamento único. Pelo conteúdo, o "
                          "“necessariamente” e o “curto prazo” tornam a frase ERRADA.")],
        "destrinchando": [
            "Uma desvalorização (alta de E, mais moeda nacional por divisa) tem dois efeitos opostos sobre o saldo "
            "medido em moeda nacional: o " + azb("efeito-preço") + " (cada unidade importada fica mais cara, "
            "o que piora o saldo) e o " + azb("efeito-quantidade") + " (exporta-se mais e importa-se menos, o que "
            "melhora o saldo).",
            azb("Condição de Marshall-Lerner") + ": partindo do equilíbrio comercial, a desvalorização real "
            "melhora o saldo se " + vd("|η<sub>X</sub>| + |η<sub>M</sub>| &gt; 1") + " (soma das elasticidades-"
            "preço da demanda por exportações e importações). Se as demandas forem muito inelásticas, o "
            "efeito-preço vence e o saldo piora — daí o “necessariamente” ser falso.",
            azb("Curva J") + ": no curto prazo, contratos já fechados e hábitos de consumo fazem as quantidades "
            "reagirem devagar; o efeito-preço domina e o saldo cai. Com o tempo, as elasticidades aumentam e o "
            "saldo melhora. Logo, a melhora “no curto prazo” é justamente o que a teoria <b>não</b> garante.",
            "No longo prazo também há ressalvas: se a desvalorização nominal for corroída por inflação doméstica, "
            "o câmbio <b>real</b> volta ao ponto de partida e o ganho de competitividade some; e, pela "
            + azb("abordagem da absorção") + " (" + oc("Alexander") + "), o saldo só melhora se a absorção "
            "interna cair em relação ao produto.",
            "Correção de um comentário da fonte: a curva J não diz que o saldo “volta aos níveis anteriores” no "
            "longo prazo; diz que ele piora primeiro e depois <b>supera</b> o nível inicial.",
            vm("Regra-âncora: desvalorização melhora o saldo só sob Marshall-Lerner, e geralmente depois de uma "
               "piora inicial (curva J)."),
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " A ideia geral (desvalorizar tende a melhorar "
                       "a balança) é verdadeira; o examinador a blindou com “necessariamente” e estendeu-a ao curto "
                       "prazo, que é exatamente onde mora a exceção da curva J. Itens com “necessariamente” sobre "
                       "efeitos do câmbio quase sempre são ERRADOS."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A desvalorização real da moeda melhora a balança comercial se a soma das elasticidades-preço das "
            "exportações e das importações, em módulo, for maior que um.”</i> → CERTO",
            "<i>“Pela curva J, a desvalorização melhora imediatamente o saldo comercial, que depois se "
            "deteriora.”</i> → ERRADO (inversão: primeiro piora, depois melhora)",
        ])],
        "reescrita": ("A desvalorização da moeda " + hl("tende a acarretar") + " a melhora da balança comercial"
                      + hl(" no longo prazo, se atendida a condição de Marshall-Lerner, mas pode piorá-la no curto "
                           "prazo (curva J)") + "."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["necessariamente", "tanto … quanto"],
        "dificuldade": 2,
        "comentario_fonte": ("“Inconclusiva”; item anulado por vagueza (depende de elasticidades, pauta e termos de "
                             "troca); comentário sobre curva J (piora no curto prazo); outro comentário afirma, "
                             "erroneamente, que pela curva J o saldo voltaria aos níveis anteriores no longo prazo."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: item anulado; pelo conteúdo, a resposta mais defensável seria ERRADO",
                    "quase_duplicata: ECO-E1-0772-1 (curva J)"],
    },
    # ------------------------------------------------------------------ E1-0426
    {
        "id": "ECO-E1-0426-1", "fonte_ref": "E1-0426", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_JUROS,
        "rotulo_item": "Item",
        "assertiva": ("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                      "uma depreciação cambial e redução da balança comercial (X − M)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                       "uma depreciação cambial e ") + vm("redução") + az(" da balança comercial (X − M).")),
        "poucas": ("A primeira metade está certa (juros ↓ → saída de capitais → " + azb("depreciação") + "), mas "
                   "a depreciação <b>aumenta</b> o saldo X − M, não o reduz."),
        "destrinchando": [
            "Cadeia de transmissão com alta mobilidade de capitais: " + vd("i ↓ → ativos domésticos rendem menos → "
            "saída de capitais (ou menor entrada) → demanda por divisas ↑ → E ↑ (depreciação)") + ".",
            "Efeito comercial: com a moeda nacional mais barata, o produto doméstico fica mais competitivo lá fora "
            "e o importado fica mais caro aqui → exportações ↑, importações ↓ → " + vd("X − M ↑") + ".",
            "A queda dos juros também estimula consumo e investimento, o que puxa importações para cima. Mesmo "
            "assim, o efeito-câmbio sobre o saldo, no modelo-padrão (" + azb("Mundell-Fleming") + ", câmbio "
            "flutuante), é positivo: é por isso que a política monetária é tão potente nesse regime.",
            "“País grande” significa que ele influencia a taxa de juros internacional: parte da queda de i se "
            "transmite ao resto do mundo, o que <b>atenua</b> a depreciação, mas não muda o sentido dos efeitos.",
            "Ressalva de prazo: logo após a depreciação, o saldo pode piorar (" + azb("curva J") + "); o item, "
            "porém, cobra o efeito-padrão, sob a condição de Marshall-Lerner.",
            vm("Regra-âncora: juros ↓ → câmbio ↑ (depreciação) → X − M ↑."),
        ],
        "dissecando": (cz("[inversão]") + " O item acerta o primeiro elo (depreciação) e inverte o segundo "
                       "(saldo). A banca fabrica variações do mesmo enunciado trocando “depreciação/apreciação” e "
                       "“aumento/redução”; só a combinação depreciação + aumento é CERTA."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o efeito de uma queda das taxas de juros é uma depreciação cambial e aumento da balança comercial "
            "(X − M).”</i> → CERTO",
            "<i>“…o efeito de uma queda das taxas de juros é uma apreciação cambial e redução da balança comercial "
            "(X − M).”</i> → ERRADO (sentido do câmbio trocado: juros menores depreciam)",
        ])],
        "reescrita": ("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                      "uma depreciação cambial e " + hl("aumento") + " da balança comercial (X − M)."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO: a depreciação estimula exportações e desestimula importações, aumentando X − M.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [ALERTA_JUROS],
    },
    # ------------------------------------------------------------------ E1-0427
    {
        "id": "ECO-E1-0427-1", "fonte_ref": "E1-0427", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_JUROS,
        "rotulo_item": "Item",
        "assertiva": ("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                      "uma depreciação cambial e aumento da balança comercial (X − M)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                      "uma <u>depreciação</u> cambial e <u>aumento</u> da balança comercial (X − M)."),
        "poucas": ("Juros menores afastam capitais, a moeda se " + azb("deprecia") + " e a competitividade-preço "
                   "melhora: exportações sobem, importações caem e o saldo " + vd("X − M aumenta") + "."),
        "destrinchando": [
            "Com intenso fluxo de capitais, o diferencial de juros comanda o câmbio. Pela " + azb("paridade "
            "descoberta de juros") + " (i = i* + depreciação esperada), se i cai abaixo de i*, os investidores "
            "migram para fora até que o câmbio se ajuste: " + vd("E ↑") + ".",
            "Depreciação real → bens nacionais mais baratos no exterior e importados mais caros internamente → "
            "exportações ↑ e importações ↓ → saldo comercial ↑ (supondo a " + azb("condição de Marshall-Lerner")
            + ": |η<sub>X</sub>| + |η<sub>M</sub>| &gt; 1).",
            "No " + azb("Mundell-Fleming") + " com câmbio flutuante, esse é o canal que torna a política monetária "
            "eficaz: a expansão monetária reduz i, deprecia a moeda e a demanda agregada sobe também pelas "
            "exportações líquidas. Sob câmbio fixo, o canal se bloqueia, porque o Banco Central vende reservas "
            "para segurar a paridade.",
            "“País grande”: sua queda de juros puxa para baixo também os juros mundiais, o que suaviza a saída de "
            "capitais e a depreciação. O sentido dos efeitos não muda.",
            "Prazo: imediatamente após a depreciação o saldo pode piorar (" + azb("curva J") + "); a afirmação "
            "descreve o efeito final.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Resume a cadeia-padrão juros → câmbio → comércio. A pegadinha "
                       "está nas versões vizinhas do mesmo enunciado, que trocam “depreciação” por “apreciação” ou "
                       "“aumento” por “redução”: confira cada elo separadamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma depreciação cambial e redução da balança comercial (X − M).”</i> → ERRADO (inversão: a "
            "depreciação aumenta o saldo)",
            "<i>“…sob câmbio fixo e perfeita mobilidade de capitais, a queda dos juros pelo Banco Central se "
            "sustenta e deprecia a moeda.”</i> → ERRADO (no câmbio fixo, o BC precisa defender a paridade e a "
            "política monetária perde autonomia)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO: juros menores reduzem a atratividade de capitais, depreciam a moeda e elevam "
                             "o saldo comercial."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [ALERTA_JUROS],
    },
    # ------------------------------------------------------------------ E1-0428
    {
        "id": "ECO-E1-0428-1", "fonte_ref": "E1-0428", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_JUROS,
        "rotulo_item": "Item",
        "assertiva": ("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                      "uma apreciação cambial e redução da balança comercial (X − M)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                       "uma ") + vm("apreciação") + az(" cambial e ") + vm("redução") + az(" da balança comercial "
                                                                                          "(X − M).")),
        "poucas": ("Juros menores provocam saída de capitais e " + azb("depreciação") + ", não apreciação; e a "
                   "depreciação <b>eleva</b> o saldo X − M."),
        "destrinchando": [
            "Quem sustenta o câmbio, com capitais muito móveis, é o diferencial de juros. Juros domésticos menores "
            "→ aplicar no país rende menos → capitais saem → sobe a procura por divisas → " + vd("E ↑") + " "
            "(mais moeda nacional por dólar = depreciação).",
            "A apreciação é o efeito de uma <b>alta</b> de juros: o país atrai capitais, sobram dólares e a moeda "
            "nacional se fortalece — o que barateia importados e prejudica exportadores (X − M ↓).",
            "Note a coerência interna do item: “apreciação” combinada com “redução de X − M” é uma dupla "
            "consistente, só que ligada ao choque errado. Ele descreve o efeito de uma <b>alta</b> de juros e o "
            "atribui à queda.",
            "Com depreciação, e sob a " + azb("condição de Marshall-Lerner") + ", o saldo comercial melhora "
            "(possivelmente após a piora inicial da " + azb("curva J") + ").",
            vm("Regra-âncora: i ↓ → capitais saem → depreciação → X − M ↑; i ↑ → capitais entram → apreciação → "
               "X − M ↓."),
        ],
        "dissecando": (cz("[inversão]") + " O item é o espelho exato do efeito de uma alta de juros. Como os dois "
                       "elos “fecham” entre si, quem confere só a coerência marca CERTO; é preciso conferir o elo "
                       "inicial: juros menores <b>espantam</b> capitais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o efeito de uma elevação das taxas de juros é uma apreciação cambial e redução da balança "
            "comercial (X − M).”</i> → CERTO",
            "<i>“…o efeito de uma queda das taxas de juros é uma depreciação cambial e redução da balança comercial "
            "(X − M).”</i> → ERRADO (saldo invertido: a depreciação aumenta X − M)",
        ])],
        "reescrita": ("Em um país grande com intenso fluxo de capitais, o efeito de uma queda das taxas de juros é "
                      "uma " + hl("depreciação") + " cambial e " + hl("aumento") + " da balança comercial (X − M)."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO: a queda dos juros reduz a entrada de capitais e tende a desvalorizar a moeda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (91).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; comentário coberto pelo texto)"}],
        "alertas": [ALERTA_JUROS],
    },
    # ------------------------------------------------------------------ E1-0670
    {
        "id": "ECO-E1-0670-1", "fonte_ref": "E1-0670", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True,
        "errei": False,
        "comando": "Acerca da política cambial e de seus efeitos sobre a economia, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A condução da política cambial em um regime de câmbio flutuante ou administrado não tem "
                      "impacto no dia a dia do cidadão comum."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A condução da política cambial em um regime de câmbio flutuante ou administrado ")
                    + vm("não tem impacto") + az(" no dia a dia do cidadão comum.")),
        "poucas": ("O câmbio chega ao cotidiano por vários canais — " + azb("preços de importados e insumos") + ", "
                   "combustíveis, inflação, juros e emprego —, qualquer que seja o regime."),
        "destrinchando": [
            azb("Repasse cambial (pass-through)") + ": uma depreciação encarece importados, insumos industriais e "
            "bens cotados em dólar (petróleo, trigo, fertilizantes) e pressiona a inflação, reduzindo o poder de "
            "compra. Uma apreciação faz o contrário: barateia importados e viagens, mas tira competitividade de "
            "exportadores e de setores que concorrem com importações, com efeito sobre o emprego.",
            "Canal dos juros: movimentos bruscos do câmbio podem levar o Banco Central a mexer na taxa básica "
            "para conter a inflação, o que afeta crédito, prestações e investimento.",
            "No " + azb("câmbio flutuante") + ", a política cambial se manifesta pela ausência (ou pela raridade) "
            "de intervenção e pela escolha do regime; no " + azb("administrado") + " (flutuação suja, bandas), "
            "pelas intervenções do Banco Central. Nos dois casos, as decisões mudam o nível e a volatilidade do "
            "câmbio — e, portanto, preços relativos.",
            rx("No Brasil") + ", o regime é de câmbio flutuante desde 1999, com intervenções pontuais (swaps "
            "cambiais, leilões de linha e à vista), e o câmbio é um dos principais componentes da inflação de "
            "alimentos e combustíveis.",
            vm("Regra-âncora: o câmbio é um preço-chave da economia; nenhum regime o torna irrelevante para o "
               "cidadão."),
        ],
        "dissecando": (cz("[contradição · modulador absoluto]") + " A negativa absoluta (“não tem impacto”) choca "
                       "com o senso econômico mais básico. A menção a dois regimes serve para sugerir que, por "
                       "serem “de mercado”, eles isolariam o cidadão da política cambial — não isolam."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio flutuante, uma depreciação da moeda nacional tende a pressionar a inflação, "
            "pelo encarecimento de bens e insumos importados.”</i> → CERTO",
            "<i>“Somente em regime de câmbio fixo a política cambial afeta os preços internos.”</i> → ERRADO "
            "(restrição indevida: o repasse ocorre em qualquer regime)",
        ])],
        "reescrita": ("A condução da política cambial em um regime de câmbio flutuante ou administrado "
                      + hl("tem impacto") + " no dia a dia do cidadão comum."),
        "tipo_erro": ["CONTRADICAO", "GENERALIZACAO"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": ("Gabarito ERRADO; o câmbio afeta preço de importados, insumos, combustíveis, turismo, "
                             "inflação e até os juros, em qualquer regime."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: o texto motivador da prova não veio na fonte (frente: “A partir do texto "
                    "apresentado…”); comando neutralizado — o item se julga sem ele"],
    },
    # ------------------------------------------------------------------ E1-0677
    {
        "id": "ECO-E1-0677-1", "fonte_ref": "E1-0677", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True,
        "errei": False,
        "comando": "A respeito de regimes cambiais, julgue o próximo item.",
        "rotulo_item": "Item",
        "assertiva": ("No regime de bandas cambiais, quando a taxa de câmbio se aproxima do limite de desvalorização "
                      "da moeda nacional, a autoridade monetária deve ingressar no mercado, comprando divisas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime de bandas cambiais, quando a taxa de câmbio se aproxima do limite de "
                       "desvalorização da moeda nacional, a autoridade monetária deve ingressar no mercado, ")
                    + vm("comprando") + az(" divisas.")),
        "poucas": ("No " + azb("teto da banda") + " (moeda nacional fraca, dólar caro), o Banco Central "
                   + vm("vende") + " divisas para aumentar a oferta de dólares e conter a depreciação. Comprar "
                   "divisas é a defesa do <b>piso</b>."),
        "destrinchando": [
            "Na " + azb("banda cambial") + ", a autoridade anuncia um intervalo para a taxa (cotada como R$/US$): "
            "um " + azb("piso") + " (limite de valorização da moeda nacional) e um " + azb("teto") + " (limite de "
            "desvalorização). Dentro da faixa, o câmbio flutua; nas bordas, o Banco Central intervém.",
            "Perto do teto, há excesso de demanda por dólares. Para segurar a taxa, o BC <b>vende</b> divisas das "
            "reservas e recebe moeda nacional em troca: aumenta a oferta de dólares, enxuga reais e o preço do "
            "dólar recua. Comprar dólares nesse momento faria o contrário — injetaria reais, aumentaria a procura "
            "por divisas e empurraria o câmbio para fora da banda.",
            "Perto do piso, o problema é o oposto (sobra de dólares, real forte demais): o BC <b>compra</b> "
            "divisas, acumula reservas e emite moeda nacional.",
            "A defesa do teto tem limite: depende do estoque de reservas e costuma vir acompanhada de alta de "
            "juros. " + rx("O Brasil") + " operou bandas cambiais de 1995 a janeiro de 1999; diante da fuga de "
            "capitais após as crises asiática (1997) e russa (1998), queimou reservas defendendo o teto e acabou "
            "migrando para o câmbio flutuante.",
            vm("Regra-âncora: teto da banda (moeda fraca) → BC vende divisas; piso (moeda forte) → BC compra."),
        ],
        "dissecando": (cz("[inversão]") + " Troca a operação: “comprando” no lugar de “vendendo”. O termo "
                       "“limite de desvalorização” confunde quem pensa que, para “desvalorizar menos”, o BC precisa "
                       "“comprar algo”. Pergunte sempre: <b>de que lado está o excesso?</b> No teto falta dólar; "
                       "logo, o BC entrega dólar ao mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de bandas cambiais, quando a taxa de câmbio se aproxima do limite de valorização da "
            "moeda nacional, a autoridade monetária deve ingressar no mercado, comprando divisas.”</i> → CERTO",
            "<i>“A defesa do teto da banda tende a ampliar as reservas internacionais do país.”</i> → ERRADO "
            "(inversão: vender divisas reduz as reservas)",
        ])],
        "reescrita": ("No regime de bandas cambiais, quando a taxa de câmbio se aproxima do limite de desvalorização "
                      "da moeda nacional, a autoridade monetária deve ingressar no mercado, " + hl("vendendo")
                      + " divisas."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": ("Vários comentários (professor e IAs) convergentes: no limite de desvalorização (teto), "
                             "o BC vende divisas; no de valorização (piso), compra. Quadro-resumo de regimes "
                             "cambiais em imagem; alguns exemplos históricos imprecisos (Argentina “com bandas”)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (200).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "irrecuperavel (quadro-resumo de regimes cambiais não preservado; tema coberto "
                                   "no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0694
    {
        "id": "ECO-E1-0694-1", "fonte_ref": "E1-0694", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Em regimes de câmbio flutuante puro, a taxa de câmbio é determinada unicamente pelo mercado, "
                      "sem qualquer possibilidade de intervenção do banco central, mesmo diante de flutuações "
                      "extremas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "alterado",
        "anotada": az("Em regimes de câmbio flutuante <u>puro</u>, a taxa de câmbio é determinada unicamente pelo "
                      "mercado, sem qualquer possibilidade de intervenção do banco central, mesmo diante de "
                      "flutuações extremas."),
        "poucas": ("Pela definição, " + azb("flutuação pura (limpa)") + " é a que não tem intervenção nenhuma: "
                   "se o banco central intervém, ainda que em crise, o regime passa a ser de " + azb("flutuação "
                   "suja") + ". Daí o gabarito final CERTO."),
        "condicionais": [("🏛️ Justificativa da banca", cz(
            "Gabarito preliminar ERRADO, alterado para CERTO. Em síntese: se o regime é realmente puro, por "
            "definição não há intervenção do banco central."))],
        "destrinchando": [
            "Espectro dos regimes: " + azb("flutuação pura") + " (o mercado forma a taxa, zero intervenção) → "
            + azb("flutuação suja/administrada") + " (o mercado forma a taxa, com intervenções ocasionais ou "
            "frequentes) → " + azb("bandas") + " → " + azb("câmbio fixo") + " (paridade defendida pelo BC) → "
            + azb("currency board") + " e dolarização.",
            "O adjetivo “puro” é o que decide: ele descreve um tipo ideal em que a intervenção está excluída por "
            "definição. A frase não fala de um país real, mas do regime conceitual; nele, “mesmo diante de "
            "flutuações extremas” continua sem intervenção — se houver, o regime deixa de ser puro.",
            "Por que o gabarito preliminar era ERRADO: na prática, todo banco central conserva a <b>prerrogativa</b> "
            "de intervir em condições desordenadas de mercado, e mesmo países classificados pelo " + azb("FMI")
            + " como de flutuação livre fazem intervenções raras. Lida como afirmação sobre a realidade "
            "institucional, a frase seria absoluta demais.",
            "Na prática, quase nenhum país flutua de forma totalmente limpa. " + rx("O Brasil") + " adota "
            "flutuação suja desde 1999, com intervenções por swaps cambiais e leilões.",
            vm("Regra-âncora: “puro/limpo” = intervenção zero por definição; intervenção ocasional = flutuação "
               "suja."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O item empilha absolutos (“unicamente”, “sem "
                       "qualquer possibilidade”, “mesmo diante de”) que, por reflexo, levam a marcar ERRADO. Mas "
                       "o qualificador “puro” transforma a frase numa definição. 🔥 Antes de punir um absoluto, "
                       "veja se ele não está apenas descrevendo um tipo ideal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regimes de câmbio flutuante, a taxa de câmbio é determinada unicamente pelo mercado, sem "
            "qualquer possibilidade de intervenção do banco central.”</i> → ERRADO (sem o “puro”, a frase ignora "
            "a flutuação suja, que também é regime flutuante)",
            "<i>“Na flutuação suja, o banco central intervém ocasionalmente no mercado de câmbio, sem se "
            "comprometer com uma paridade.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"],
        "moduladores": ["unicamente", "sem qualquer possibilidade", "mesmo diante de"], "dificuldade": 3,
        "comentario_fonte": ("“De ERRADO foi alterado para CERTO” (se for realmente puro, não há intervenção; "
                             "“polêmico”); seguem várias respostas de IA que defendem ERRADO pelo absolutismo de "
                             "“sem qualquer possibilidade de intervenção”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (205).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada)"}],
        "alertas": ["nota_redacao: gabarito alterado pela banca de ERRADO para CERTO; os comentários de IA da "
                    "fonte defendiam ERRADO e foram descartados nesse ponto",
                    "quase_duplicata: ECO-E1-0775-1 (câmbio flutuante não requer intervenção)"],
    },
    # ------------------------------------------------------------------ E1-0744
    {
        "id": "ECO-E1-0744-1", "fonte_ref": "E1-0744", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("No sistema conhecido como crawling band, fixa-se uma faixa dentro da qual a cotação da moeda "
                      "pode flutuar livremente; o piso e o teto não podem ser alterados durante todo o período em "
                      "que o sistema for adotado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No sistema conhecido como crawling band, fixa-se uma faixa dentro da qual a cotação da "
                       "moeda pode flutuar livremente; o piso e o teto ") + vm("não podem ser alterados durante "
                       "todo o período") + az(" em que o sistema for adotado.")),
        "poucas": ("<i>Crawling</i> = “rastejante”: na " + azb("banda móvel") + ", piso e teto são "
                   + vm("ajustados gradualmente") + " ao longo do tempo. Banda que nunca muda é banda fixa."),
        "destrinchando": [
            "A primeira parte está certa: em qualquer " + azb("banda cambial") + ", define-se uma faixa dentro da "
            "qual a taxa flutua livremente, com intervenção nas bordas.",
            "O que distingue a " + azb("crawling band") + " é o movimento da faixa: piso e teto se deslocam "
            "periodicamente, em pequenos passos (por exemplo, acompanhando o diferencial de inflação entre o país "
            "e seus parceiros), para evitar que a inflação doméstica aprecie o câmbio real e corroa a "
            "competitividade.",
            "Família de regimes: " + azb("crawling peg") + " (paridade única reajustada em minidesvalorizações "
            "frequentes, como " + rx("o Brasil") + " praticou de 1968 a meados dos anos 1980) × "
            + azb("crawling band") + " (faixa que se desloca) × " + azb("banda fixa") + " (faixa constante) × "
            + azb("peg ajustável") + " (paridade fixa com realinhamentos esporádicos, como em Bretton Woods).",
            "No Plano Real, " + rx("o Brasil") + " adotou bandas cambiais de 1995 a janeiro de 1999, com "
            "ajustes periódicos dos limites e minibandas internas — um arranjo próximo da banda deslizante.",
            vm("Regra-âncora: “crawling” = limites (ou paridade) que se movem aos poucos e de forma pré-anunciada."),
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " A 1ª oração define corretamente uma banda; a "
                       "2ª descreve a banda <b>fixa</b> e a cola no nome “crawling”. A pista está no próprio termo "
                       "em inglês: <i>crawl</i> é mover-se devagar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No crawling peg, a paridade cambial é reajustada em pequenas desvalorizações frequentes, "
            "em geral com base no diferencial de inflação.”</i> → CERTO",
            "<i>“Na crawling band, a autoridade monetária não intervém em nenhuma hipótese.”</i> → ERRADO "
            "(intervém nas bordas da faixa)",
        ])],
        "reescrita": ("No sistema conhecido como crawling band, fixa-se uma faixa dentro da qual a cotação da moeda "
                      "pode flutuar livremente; o piso e o teto " + hl("são ajustados gradualmente ao longo de "
                      "todo o período") + " em que o sistema for adotado."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["não podem", "todo"], "dificuldade": 1,
        "comentario_fonte": ("Errado: a banda é móvel (“crawling”) porque teto e piso se deslocam gradualmente "
                             "conforme a média da taxa no período."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0745
    {
        "id": "ECO-E1-0745-1", "fonte_ref": "E1-0745", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Ao se adotar como moeda local uma moeda comum com outros países, abre-se mão da política "
                      "cambial própria. Nesse caso, a administração monetária e cambial passa a ser exercida "
                      "conjuntamente, como no caso da união monetária europeia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ao se adotar como moeda local uma moeda comum com outros países, abre-se mão da política "
                      "cambial própria. Nesse caso, a administração <u>monetária e cambial</u> passa a ser exercida "
                      "conjuntamente, como no caso da união monetária europeia."),
        "poucas": ("Na " + azb("união monetária") + ", o país perde o câmbio próprio e também a política "
                   "monetária própria: ambas passam a um banco central comum (no euro, o " + azb("BCE") + "). "
                   "Resta-lhe a política fiscal."),
        "destrinchando": [
            "Com moeda comum, não existe mais taxa de câmbio entre os membros; em relação ao resto do mundo, o "
            "câmbio da moeda comum (euro × dólar, por exemplo) é decidido no nível da união.",
            "A política monetária também é centralizada: o " + azb("Banco Central Europeu") + " fixa os juros "
            "para toda a área do euro (moeda escritural desde " + vd("1999") + ", cédulas desde "
            + vd("2002") + "). O item menciona as duas dimensões ao dizer que a administração “monetária e "
            "cambial” passa a ser conjunta — por isso é CERTO, ainda que a 1ª frase cite só a cambial.",
            "Consequência: diante de um choque assimétrico (recessão só num membro), o país não pode desvalorizar "
            "nem baixar juros por conta própria; sobra a " + azb("política fiscal") + ", limitada pelas regras "
            "comuns, como ficou claro na crise da Grécia e da periferia europeia a partir de 2010.",
            "Teoria das " + azb("zonas monetárias ótimas") + " (" + oc("Robert Mundell") + ", 1961): a moeda "
            "comum compensa quando há mobilidade de trabalho, flexibilidade de preços e salários, integração "
            "comercial e mecanismos fiscais de transferência entre os membros.",
            "Leitura pelo " + azb("trilema") + ": com livre mobilidade de capitais e câmbio “fixo” entre os "
            "membros (o caso extremo é a moeda única), abre-se mão da autonomia monetária nacional.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O risco está na 1ª frase, que fala só da política "
                       "cambial e induz a pensar “incompleto, logo errado”. Mas incompleto não é falso, e a 2ª frase "
                       "completa com a dimensão monetária. 🔥 Em itens que omitem algo sem usar “apenas”, a omissão "
                       "não torna o item errado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao aderir à união monetária europeia, o país abre mão apenas da política cambial, conservando "
            "a autonomia para fixar seus próprios juros.”</i> → ERRADO (restrição indevida: perde também a "
            "monetária)",
            "<i>“Na união monetária, o principal instrumento nacional que resta para enfrentar choques "
            "assimétricos é a política fiscal.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("“Correto”, mas teoricamente impreciso: na união monetária o país abre mão também da "
                             "política monetária, gerida em conjunto; resta a política fiscal."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0746
    {
        "id": "ECO-E1-0746-1", "fonte_ref": "E1-0746", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("O chamado currency board, considerado muito severo, foi bastante utilizado no final do século "
                      "XX, associado aos planos de estabilização, como no caso argentino, e caracteriza-se por uma "
                      "vinculação com a política monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O chamado currency board, considerado muito severo, foi bastante utilizado no final do século "
                      "XX, associado aos planos de estabilização, como no caso argentino, e caracteriza-se por uma "
                      "<u>vinculação com a política monetária</u>."),
        "poucas": ("No " + azb("currency board") + " (conselho da moeda), cada unidade de moeda emitida tem de ter "
                   "lastro em divisas a uma paridade fixada em lei: a " + azb("política monetária fica amarrada") +
                   " ao câmbio e ao fluxo de reservas."),
        "destrinchando": [
            "Regra de funcionamento: a autoridade monetária só emite moeda nacional contra entrada de divisas, "
            "à paridade legal, e recolhe moeda quando divisas saem. A " + azb("base monetária") + " passa a ser "
            "endógena ao balanço de pagamentos — sem emissão discricionária e, em regra, sem papel de emprestador "
            "de última instância.",
            "Por isso é chamado de regime “severo” (" + azb("hard peg") + "): é a forma mais rígida de câmbio fixo "
            "antes da dolarização plena, e mudar a paridade exige mudar a lei.",
            rx("Argentina") + ": a " + azb("Lei de Conversibilidade") + " (" + vd("1991") + ", plano Cavallo) "
            "fixou 1 peso = 1 dólar e derrubou a hiperinflação. O custo veio na forma de câmbio sobrevalorizado, "
            "juros altos para atrair capitais e vulnerabilidade a choques externos (México 1994, Ásia 1997, "
            "desvalorização brasileira de 1999), até o colapso em " + vd("2001–2002") + ".",
            "Outros casos: Hong Kong (desde 1983), Estônia e Lituânia (anos 1990, antes do euro), Bulgária "
            "(1997).",
            "Pelo " + azb("trilema") + ": com câmbio fixo e livre mobilidade de capitais, a política monetária "
            "perde autonomia; o currency board torna essa renúncia institucional.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item soma características verdadeiras (severo, anos "
                       "1990, Argentina). “Vinculação com a política monetária” pode soar vago, mas é exatamente a "
                       "essência do regime: a oferta de moeda fica atrelada às reservas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No currency board, a autoridade monetária pode emitir moeda livremente para financiar o Tesouro, "
            "desde que mantenha a paridade.”</i> → ERRADO (contradição: a emissão é limitada pelo lastro em "
            "divisas)",
            "<i>“A conversibilidade argentina fixou a paridade de um peso por dólar.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Correto: o currency board conduzia a política monetária num país com plena "
                             "conversibilidade; sistema quase bimonetário (dólar com livre curso na Argentina); "
                             "exigia juros elevados, que agravavam o câmbio sobrevalorizado sobre a indústria."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0748
    {
        "id": "ECO-E1-0748-1", "fonte_ref": "E1-0748", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos da política cambial sobre o comércio exterior, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A política de desvalorização da moeda nacional, que cria a necessidade de mais unidades de "
                      "moeda nacional para manter a equivalência com uma unidade de moeda estrangeira, resulta em "
                      "aumento das exportações, diminuição das importações e proteção do mercado interno contra a "
                      "competição externa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A política de desvalorização da moeda nacional, que cria a necessidade de <u>mais unidades de "
                      "moeda nacional</u> para manter a equivalência com uma unidade de moeda estrangeira, resulta em "
                      "aumento das exportações, diminuição das importações e proteção do mercado interno contra a "
                      "competição externa."),
        "poucas": ("Desvalorizar = " + azb("E ↑") + " (mais reais por dólar): o exportador recebe mais em moeda "
                   "nacional e o importado fica mais caro — mais exportação, menos importação e uma "
                   + azb("proteção cambial") + " à produção doméstica."),
        "destrinchando": [
            "Definição correta no item: com a taxa cotada em moeda nacional por estrangeira (R$/US$), "
            "desvalorizar é <b>aumentar</b> E. Um dólar passa a “custar” mais reais.",
            "Exportações: o mesmo preço em dólar rende mais reais ao exportador, que pode baixar o preço externo "
            "ou ampliar a margem → volume exportado ↑. Importações: o bem estrangeiro fica mais caro em reais → "
            "importações ↓ e consumo migra para o similar nacional. O câmbio desvalorizado funciona como uma "
            "tarifa sobre importações somada a um subsídio às exportações.",
            "Ressalvas (por isso o item é “certo com qualificações”): o que move o comércio é o " + azb("câmbio "
            "real") + " (E·P*/P): se a inflação doméstica subir na mesma proporção, o ganho some. E, no curto "
            "prazo, o saldo pode piorar antes de melhorar (" + azb("curva J") + "), com melhora dependente da "
            "condição de " + azb("Marshall-Lerner") + ".",
            "Efeitos colaterais: pressão inflacionária (repasse cambial), aumento do peso da dívida em moeda "
            "estrangeira e encarecimento de insumos e máquinas importados.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Descreve o efeito-padrão de manual. A tentação de marcar ERRADO "
                       "vem do “resulta em” sem ressalvas e da lembrança da curva J; mas a banca cobra aqui o "
                       "mecanismo, não as exceções. A definição de desvalorização (“mais unidades de moeda "
                       "nacional”) também está certa — confira sempre a convenção de cotação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A desvalorização da moeda nacional reduz o número de unidades de moeda nacional necessárias para "
            "adquirir uma unidade de moeda estrangeira.”</i> → ERRADO (inversão: isso é valorização)",
            "<i>“Uma desvalorização nominal acompanhada de inflação doméstica de mesma magnitude preserva o ganho "
            "de competitividade.”</i> → ERRADO (o câmbio real não muda)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Correto no curto prazo; mas é o câmbio real que rege o comércio — uma desvalorização "
                             "de 10% não compensa bens domésticos muito mais caros; validade geral exige "
                             "qualificações."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0749
    {
        "id": "ECO-E1-0749-1", "fonte_ref": "E1-0749", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("A vantagem do regime de taxas de câmbio fixas é a de ajustar automaticamente a economia, o que "
                      "facilita as transações internacionais e desonera o Banco Central do Brasil dessa "
                      "incumbência."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A vantagem do regime de taxas de câmbio fixas é a de ") + vm("ajustar automaticamente a "
                    "economia") + az(", o que facilita as transações internacionais")
                    + vm(" e desonera o Banco Central do Brasil dessa incumbência") + az(".")),
        "poucas": ("Ajuste automático e Banco Central desonerado são atributos do " + azb("câmbio flutuante")
                   + ". No " + azb("câmbio fixo") + ", o BC é obrigado a intervir sempre para sustentar a "
                   "paridade; a vantagem é a " + vd("previsibilidade") + "."),
        "destrinchando": [
            "No câmbio fixo, o preço da divisa não se move; quem absorve os desequilíbrios do mercado de câmbio é "
            "o " + azb("estoque de reservas") + ". Entrada líquida de dólares → o BC compra o excesso e emite "
            "moeda; saída líquida → vende reservas e enxuga moeda. A política monetária fica a reboque do balanço "
            "de pagamentos.",
            "A vantagem real do regime é a " + azb("estabilidade da taxa") + ": reduz incerteza e risco cambial, "
            "facilita contratos e comércio e serve de " + azb("âncora nominal") + " contra a inflação (o Plano "
            "Real usou uma âncora cambial de 1994 a 1999).",
            "A desvantagem: perde-se a autonomia monetária (" + azb("trilema") + ") e o regime fica exposto a "
            "ataques especulativos quando as reservas parecem insuficientes.",
            "O “ajuste automático” do balanço de pagamentos pelo câmbio é o argumento clássico a favor do câmbio "
            "flexível, defendido por " + oc("Milton Friedman") + " (“The Case for Flexible Exchange Rates”, 1953): "
            "o preço da divisa se move e reequilibra o mercado sem gasto de reservas.",
            vm("Regra-âncora: câmbio fixo = BC intervém sempre; câmbio flutuante = o preço ajusta e o BC fica "
               "livre."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui ao câmbio fixo as virtudes do flutuante (ajuste "
                       "automático, BC liberado). Só a “facilitação das transações internacionais” pertence ao "
                       "fixo. Pergunta-teste: <b>quem compra e vende divisas para a taxa não mudar?</b> O BC — logo, "
                       "ele não fica desonerado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de câmbio flutuante, o próprio preço da divisa ajusta o mercado de câmbio, dispensando o "
            "Banco Central de intervir para sustentar uma paridade.”</i> → CERTO",
            "<i>“No câmbio fixo, entradas líquidas de capital forçam o Banco Central a comprar divisas, o que "
            "expande a base monetária se não houver esterilização.”</i> → CERTO",
        ])],
        "reescrita": ("A vantagem do regime de taxas de câmbio fixas é a de " + hl("reduzir a incerteza cambial")
                      + ", o que facilita as transações internacionais" + hl(", mas obriga o Banco Central do "
                      "Brasil a intervir continuamente no mercado de câmbio") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["automaticamente"], "dificuldade": 1,
        "comentario_fonte": ("Errado: no câmbio fixo a política monetária depende da entrada de divisas e nada é "
                             "automático; o BC compra o excesso de divisas e emite moeda; vantagem: controle da "
                             "inflação; desvantagem: dependência do fluxo de capitais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0750-1 (ônus do Banco Central no câmbio fixo × flutuante)"],
    },
    # ------------------------------------------------------------------ E1-0750
    {
        "id": "ECO-E1-0750-1", "fonte_ref": "E1-0750", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": True,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("A adoção do câmbio flutuante apresenta a desvantagem de ficar o câmbio condicionado à "
                      "movimentação especulativa dos capitais externos, que são muito voláteis e implicam excessivo "
                      "ônus para a autoridade reguladora da estabilidade econômica do país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A adoção do câmbio flutuante apresenta a desvantagem de ficar o câmbio condicionado à "
                       "movimentação especulativa dos capitais externos, que são muito voláteis")
                    + vm(" e implicam excessivo ônus para a autoridade reguladora da estabilidade econômica do "
                         "país") + az(".")),
        "poucas": ("A 1ª parte é verdadeira (volatilidade e especulação são o custo do flutuante). O erro é o "
                   + vm("ônus para o Banco Central") + ": esse ônus — gastar reservas para defender a taxa — é "
                   "típico do " + azb("câmbio fixo") + "."),
        "destrinchando": [
            "No " + azb("câmbio flutuante") + ", o mercado forma a taxa; o BC não tem paridade a defender e não é "
            "obrigado a vender ou comprar divisas quando os capitais entram ou saem. Os choques se descarregam no "
            "<b>preço</b> (a taxa oscila), não nas reservas.",
            "Desvantagens do flutuante (" + oc("Vasconcellos") + ", <i>Economia Micro e Macro</i>): câmbio muito "
            "dependente da volatilidade do mercado financeiro e maior dificuldade de controlar pressões "
            "inflacionárias nas desvalorizações. Vantagens: política monetária mais independente e reservas "
            "protegidas de ataques especulativos.",
            "No " + azb("câmbio fixo") + ", a fuga de capitais pressiona a paridade, e o BC precisa vender "
            "reservas (e muitas vezes subir juros) para sustentá-la. Esse é o “excessivo ônus” — e é por isso que "
            "ataques especulativos derrubam regimes fixos, não flutuantes.",
            "Nuance: mesmo no flutuante, uma depreciação forte pode levar o BC a reagir com juros, por causa da "
            "inflação; mas isso é escolha de política monetária, não obrigação imposta pelo regime.",
            vm("Regra-âncora: no fixo, o choque cai nas reservas (ônus do BC); no flutuante, cai na taxa "
               "(volatilidade)."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A frase começa com uma desvantagem real do "
                       "flutuante e emenda, com um “e”, uma desvantagem do fixo. A emenda tardia é o padrão "
                       "clássico da meia-verdade CEBRASPE: leia até o fim antes de marcar CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A adoção do câmbio fixo implica ônus para a autoridade monetária, que deve usar reservas para "
            "defender a paridade diante de movimentos especulativos.”</i> → CERTO",
            "<i>“No câmbio flutuante, as reservas internacionais ficam mais expostas a ataques especulativos do que "
            "no câmbio fixo.”</i> → ERRADO (inversão: ficam mais protegidas)",
        ])],
        "reescrita": ("A adoção do câmbio flutuante apresenta a desvantagem de ficar o câmbio condicionado à "
                      "movimentação especulativa dos capitais externos, que são muito voláteis"
                      + hl(", sem, porém, impor à autoridade reguladora da estabilidade econômica do país o ônus de "
                           "defender uma paridade") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["excessivo"], "dificuldade": 2,
        "comentario_fonte": ("Errado: a 1ª parte é correta (volatilidade, especulação), a 2ª errada — o flutuante "
                             "desonera o BACEN; o ônus é do câmbio fixo; quadro de Vasconcellos (vantagens e "
                             "desvantagens de cada regime). O verso traz ainda respostas de IA sobre outro item "
                             "(expansão monetária e curva J), descartadas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0749-1 (ônus do Banco Central no câmbio fixo × flutuante)",
                    "nota_redacao: o verso da fonte mistura comentários de outro item (expansão monetária em câmbio "
                    "flutuante); não aproveitados"],
    },
    # ------------------------------------------------------------------ E1-0763
    {
        "id": "ECO-E1-0763-1", "fonte_ref": "E1-0763", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("No regime cambial fixo, a flexibilidade da taxa de câmbio pode favorecer o ajuste de "
                      "desequilíbrios comerciais, além de permitir a adoção de políticas monetárias independentes. "
                      "No entanto, a volatilidade da taxa de câmbio pode criar incerteza e aumentar o risco cambial "
                      "para as empresas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime cambial ") + vm("fixo") + az(", a flexibilidade da taxa de câmbio pode favorecer o "
                    "ajuste de desequilíbrios comerciais, além de permitir a adoção de políticas monetárias "
                    "independentes. No entanto, a volatilidade da taxa de câmbio pode criar incerteza e aumentar o "
                    "risco cambial para as empresas.")),
        "poucas": ("Tudo o que vem depois do rótulo descreve o " + azb("câmbio flutuante") + " (flexibilidade, "
                   "autonomia monetária, volatilidade). Trocando “fixo” por “flutuante”, o item fica certo."),
        "destrinchando": [
            azb("Câmbio flutuante") + ": a taxa se move com oferta e demanda de divisas. Vantagens: ajuda a "
            "corrigir desequilíbrios externos (um déficit deprecia a moeda e estimula exportações) e, com livre "
            "mobilidade de capitais, preserva a " + azb("autonomia monetária") + ". Desvantagem: volatilidade, "
            "incerteza e risco cambial para quem exporta, importa ou deve em moeda estrangeira.",
            azb("Câmbio fixo") + ": a taxa é sustentada pelo BC. Vantagens: previsibilidade e âncora nominal. "
            "Desvantagens: com capitais livres, a política monetária fica subordinada à paridade; ajustes de "
            "competitividade têm de vir por preços e salários (lentos e dolorosos) ou por desvalorizações "
            "bruscas.",
            "O " + azb("trilema") + " (trindade impossível, " + oc("Mundell-Fleming") + ") organiza a escolha: não "
            "se tem ao mesmo tempo câmbio fixo, livre mobilidade de capitais e política monetária autônoma. "
            "Quem quer juros independentes com capitais livres precisa deixar o câmbio flutuar.",
            vm("Regra-âncora: flexibilidade, autonomia monetária e volatilidade = flutuante; previsibilidade, "
               "âncora e perda de autonomia = fixo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Item fabricado com a descrição completa e correta de um "
                       "regime e o rótulo do outro. A pista está na contradição interna: “regime fixo” e "
                       "“flexibilidade da taxa” não convivem. 🔥 Padrão recorrente da banca: o mesmo simulado "
                       "trocou fixo × flutuante em quatro itens seguidos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime cambial flutuante, a flexibilidade da taxa de câmbio pode favorecer o ajuste de "
            "desequilíbrios comerciais e permitir políticas monetárias independentes.”</i> → CERTO",
            "<i>“No regime cambial fixo, com livre mobilidade de capitais, o país mantém plena autonomia de "
            "política monetária.”</i> → ERRADO (trilema violado)",
        ])],
        "reescrita": ("No regime cambial " + hl("flutuante") + ", a flexibilidade da taxa de câmbio pode favorecer o "
                      "ajuste de desequilíbrios comerciais, além de permitir a adoção de políticas monetárias "
                      "independentes. No entanto, a volatilidade da taxa de câmbio pode criar incerteza e aumentar o "
                      "risco cambial para as empresas."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Começa falando de câmbio fixo, mas descreve o flutuante; trocando “fixo” por "
                             "“flutuante” fica certo; menção ao trilema."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_CLIP],
    },
    # ------------------------------------------------------------------ E1-0764
    {
        "id": "ECO-E1-0764-1", "fonte_ref": "E1-0764", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Um regime cambial flutuante é caracterizado pela fixação da taxa de câmbio em relação a uma "
                      "moeda ou a um grupo de moedas. Esse regime implica que o Banco Central do país intervenha no "
                      "mercado cambial para manter a taxa de câmbio constante, comprando ou vendendo moeda "
                      "estrangeira conforme necessário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um regime cambial ") + vm("flutuante") + az(" é caracterizado pela fixação da taxa de câmbio "
                    "em relação a uma moeda ou a um grupo de moedas. Esse regime implica que o Banco Central do país "
                    "intervenha no mercado cambial para manter a taxa de câmbio constante, comprando ou vendendo "
                    "moeda estrangeira conforme necessário.")),
        "poucas": ("Fixar a taxa contra uma moeda ou uma cesta e intervir para mantê-la constante é a definição de "
                   + azb("câmbio fixo") + ". No flutuante, quem forma a taxa é o mercado."),
        "destrinchando": [
            "O câmbio fixo pode ter como referência uma " + azb("moeda única") + " (o dólar, como na "
            "conversibilidade argentina; o marco alemão, para vários europeus antes do euro) ou uma "
            + azb("cesta de moedas") + " ponderada pelo comércio (para reduzir a dependência de um só parceiro; o "
            "DES do FMI é um exemplo de cesta).",
            "A mecânica descrita está correta para o fixo: se sobra divisa, o BC compra (e emite moeda); se falta, "
            "vende das reservas (e enxuga moeda). O compromisso com a paridade exige reservas e subordina a "
            "política monetária.",
            "No " + azb("câmbio flutuante") + ", não há paridade a defender. Em flutuação suja, o BC pode até "
            "intervir para suavizar a volatilidade, mas não para manter a taxa constante.",
            "Escala de rigidez: dolarização → currency board → câmbio fixo convencional → bandas → crawling peg → "
            "flutuação suja → flutuação pura.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Descrição perfeita do câmbio fixo com o rótulo trocado. A "
                       "contradição interna (“flutuante” × “fixação”, “taxa constante”) entrega o erro já na 1ª "
                       "linha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um regime cambial fixo pode ter como referência uma cesta de moedas, e não apenas uma moeda "
            "única.”</i> → CERTO",
            "<i>“Na flutuação suja, o Banco Central intervém para manter a taxa de câmbio constante.”</i> → ERRADO "
            "(intervém só para suavizar oscilações, sem meta de taxa)",
        ])],
        "reescrita": ("Um regime cambial " + hl("fixo") + " é caracterizado pela fixação da taxa de câmbio em relação "
                      "a uma moeda ou a um grupo de moedas. Esse regime implica que o Banco Central do país intervenha "
                      "no mercado cambial para manter a taxa de câmbio constante, comprando ou vendendo moeda "
                      "estrangeira conforme necessário."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Descreveu o câmbio fixo e o chamou de flutuante.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_CLIP],
    },
    # ------------------------------------------------------------------ E1-0765
    {
        "id": "ECO-E1-0765-1", "fonte_ref": "E1-0765", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Uma vantagem do regime cambial flutuante é a previsibilidade da taxa de câmbio, o que permite "
                      "planejamento de longo prazo para empresas que atuam no comércio internacional. Porém, a "
                      "rigidez do regime pode levar a desequilíbrios na balança comercial e a necessidade de ajustes "
                      "econômicos dolorosos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma vantagem do regime cambial ") + vm("flutuante") + az(" é a previsibilidade da taxa de "
                    "câmbio, o que permite planejamento de longo prazo para empresas que atuam no comércio "
                    "internacional. Porém, a rigidez do regime pode levar a desequilíbrios na balança comercial e a "
                    "necessidade de ajustes econômicos dolorosos.")),
        "poucas": ("Previsibilidade (vantagem) e rigidez que gera ajustes dolorosos (desvantagem) são o retrato do "
                   + azb("câmbio fixo") + ". O flutuante traz o oposto: volatilidade, mas ajuste pelo preço."),
        "destrinchando": [
            "Vantagem do fixo: taxa previsível, menor risco cambial, contratos e investimentos de longo prazo mais "
            "fáceis de planejar, âncora contra a inflação.",
            "Desvantagem do fixo: se o câmbio fica sobrevalorizado (por exemplo, porque a inflação interna supera "
            "a externa), acumulam-se déficits comerciais. Como a taxa não se move, o ajuste vem por "
            + azb("deflação de preços e salários") + " e recessão (a “desvalorização interna”) ou por uma "
            "desvalorização brusca quando as reservas acabam — os “ajustes dolorosos” do item.",
            "Exemplos: " + rx("o Brasil") + " em 1999 (fim da âncora cambial após perda de reservas), a "
            "Argentina em 2002 (colapso da conversibilidade) e a periferia do euro depois de 2010, que, sem "
            "câmbio próprio, ajustou-se por cortes de salários e desemprego.",
            "No " + azb("câmbio flutuante") + ", a taxa se ajusta continuamente: déficit → depreciação → "
            "melhora do saldo. O custo é a " + azb("volatilidade") + ", que dificulta o planejamento (mitigada "
            "por instrumentos de hedge, como contratos futuros e swaps).",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mesma fábrica de itens do simulado: descrição coerente do fixo "
                       "com o rótulo “flutuante”. Pista: “rigidez do regime” não combina com um regime que "
                       "<b>flutua</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma desvantagem do regime cambial flutuante é a volatilidade da taxa, que dificulta o planejamento "
            "de longo prazo das empresas.”</i> → CERTO",
            "<i>“No câmbio fixo, desequilíbrios comerciais são corrigidos automaticamente pela variação da taxa de "
            "câmbio.”</i> → ERRADO (contradição: no fixo a taxa não varia)",
        ])],
        "reescrita": ("Uma vantagem do regime cambial " + hl("fixo") + " é a previsibilidade da taxa de câmbio, o que "
                      "permite planejamento de longo prazo para empresas que atuam no comércio internacional. Porém, "
                      "a rigidez do regime pode levar a desequilíbrios na balança comercial e a necessidade de ajustes "
                      "econômicos dolorosos."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Inversão: descreveu-se o câmbio fixo; previsibilidade é associada ao fixo, "
                             "volatilidade ao flutuante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_CLIP],
    },
    # ------------------------------------------------------------------ E1-0766
    {
        "id": "ECO-E1-0766-1", "fonte_ref": "E1-0766", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Em um regime cambial fixo, a taxa de câmbio é determinada pelo mercado, ou seja, a oferta e a "
                      "demanda por moeda estrangeira determinam a taxa de câmbio em cada momento. Nesse regime, o "
                      "Banco Central pode intervir no mercado cambial para evitar volatilidade excessiva ou "
                      "mudanças abruptas na taxa de câmbio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um regime cambial ") + vm("fixo") + az(", a taxa de câmbio é determinada pelo mercado, ou "
                    "seja, a oferta e a demanda por moeda estrangeira determinam a taxa de câmbio em cada momento. "
                    "Nesse regime, o Banco Central pode intervir no mercado cambial para evitar volatilidade "
                    "excessiva ou mudanças abruptas na taxa de câmbio.")),
        "poucas": ("Taxa formada pelo mercado, com intervenções ocasionais contra a volatilidade, é o "
                   + azb("câmbio flutuante") + " (na versão de " + azb("flutuação suja") + "). No fixo, quem "
                   "determina a taxa é a autoridade monetária."),
        "destrinchando": [
            "No " + azb("câmbio fixo") + ", a oferta e a demanda de divisas continuam existindo, mas não movem a "
            "taxa: o BC compra ou vende quanto for preciso ao preço anunciado. O que varia são as "
            + azb("reservas") + ", não o câmbio.",
            "No " + azb("câmbio flutuante") + ", a taxa reflete, a cada momento, o equilíbrio entre oferta e "
            "demanda de divisas. A intervenção “para evitar volatilidade excessiva ou mudanças abruptas”, sem "
            "meta de nível, caracteriza a " + azb("flutuação suja") + " (managed float).",
            "Diferença-chave entre as intervenções: no fixo, o BC intervém para <b>manter um nível</b> (é "
            "obrigação); no flutuante sujo, para <b>suavizar a trajetória</b> (é opção).",
            rx("No Brasil") + ", o BC declara intervir apenas para dar liquidez e conter disfuncionalidades, sem "
            "meta de taxa — por isso o regime brasileiro é classificado como flutuante.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item descreve com precisão a flutuação suja e a rotula de "
                       "“fixo”. A contradição “fixo” × “determinada pelo mercado em cada momento” é a pista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um regime cambial flutuante, o Banco Central pode intervir no mercado de câmbio para evitar "
            "volatilidade excessiva, sem que isso descaracterize o regime.”</i> → CERTO",
            "<i>“No câmbio fixo, choques de oferta e demanda de divisas se refletem na variação da taxa de "
            "câmbio.”</i> → ERRADO (refletem-se na variação das reservas)",
        ])],
        "reescrita": ("Em um regime cambial " + hl("flutuante") + ", a taxa de câmbio é determinada pelo mercado, ou "
                      "seja, a oferta e a demanda por moeda estrangeira determinam a taxa de câmbio em cada momento. "
                      "Nesse regime, o Banco Central pode intervir no mercado cambial para evitar volatilidade "
                      "excessiva ou mudanças abruptas na taxa de câmbio."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Inversão: descreveu-se o câmbio flutuante; no fixo, a autoridade monetária determina "
                             "e mantém a taxa, intervindo com reservas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_CLIP],
    },
    # ------------------------------------------------------------------ E1-0767
    {
        "id": "ECO-E1-0767-1", "fonte_ref": "E1-0767", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos determinantes da taxa de câmbio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Uma das causas mais importantes da queda do euro em relação ao dólar americano é a diferença "
                      "da política monetária do Federal Reserve dos Estados Unidos e do Banco Central Europeu. "
                      "Políticas monetárias expansionistas proporcionam a valorização das moedas que a praticam."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma das causas mais importantes da queda do euro em relação ao dólar americano é a diferença "
                       "da política monetária do Federal Reserve dos Estados Unidos e do Banco Central Europeu. "
                       "Políticas monetárias expansionistas proporcionam a ") + vm("valorização")
                    + az(" das moedas que a praticam.")),
        "poucas": ("A 1ª frase é plausível (divergência Fed × BCE move o euro-dólar). O erro está na 2ª: política "
                   "monetária expansionista " + vm("desvaloriza") + " a moeda, porque reduz juros e afasta "
                   "capitais."),
        "destrinchando": [
            "Mecanismo: expansão monetária → " + vd("i ↓") + " → os ativos daquela moeda rendem menos que os "
            "estrangeiros → capitais migram → a moeda se " + azb("deprecia") + ". Pela " + azb("paridade "
            "descoberta de juros") + ", o diferencial i − i* é um dos principais determinantes do câmbio entre "
            "moedas com capitais livres.",
            "Há ainda o canal da oferta relativa de moeda (" + azb("abordagem monetária do câmbio") + "): mais "
            "moeda em circulação, mantida a demanda, reduz seu preço relativo — inclusive em termos de outras "
            "moedas.",
            "Aplicação ao euro: quando o " + azb("BCE") + " afrouxa enquanto o " + azb("Fed") + " aperta (ou "
            "afrouxa menos), o diferencial de juros favorece o dólar e o euro cai. Foi o que se viu em "
            + vd("2014–2015") + " (fim das compras de ativos nos EUA e início do quantitative easing do BCE) e em "
            + vd("2022") + " (Fed subindo juros mais cedo e mais rápido; o euro chegou a ficar abaixo da paridade "
            "com o dólar).",
            vm("Regra-âncora: afrouxamento monetário → juros menores → moeda mais fraca; aperto → moeda mais "
               "forte."),
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " A 1ª frase, correta e contextualizada, dá credibilidade; "
                       "a 2ª inverte o sentido do efeito. Note que a própria 1ª frase só faz sentido se a política "
                       "mais expansionista (a do BCE) <b>enfraquece</b> a moeda — o item se contradiz."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Políticas monetárias contracionistas tendem a valorizar as moedas que as praticam.”</i> → CERTO",
            "<i>“A elevação dos juros pelo Federal Reserve, mantidos os juros do BCE, tende a valorizar o euro "
            "frente ao dólar.”</i> → ERRADO (inversão: tende a valorizar o dólar)",
        ])],
        "reescrita": ("Uma das causas mais importantes da queda do euro em relação ao dólar americano é a diferença "
                      "da política monetária do Federal Reserve dos Estados Unidos e do Banco Central Europeu. "
                      "Políticas monetárias expansionistas proporcionam a " + hl("desvalorização")
                      + " das moedas que a praticam."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Só o gabarito (ERRADO), uma imagem não preservada e o link do canal no Telegram.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (264).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0770
    {
        "id": "ECO-E1-0770-1", "fonte_ref": "E1-0770", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Sob um sistema de taxas de câmbio fixas, um banco central permanece sempre de sobreaviso, "
                      "pronto para comprar ou vender a moeda corrente interna em troca de moedas estrangeiras a um "
                      "preço predeterminado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sob um sistema de taxas de câmbio fixas, um banco central permanece <u>sempre</u> de "
                      "sobreaviso, pronto para comprar ou vender a moeda corrente interna em troca de moedas "
                      "estrangeiras a um preço predeterminado."),
        "poucas": ("É a definição de manual de " + azb("câmbio fixo") + ": o BC se compromete a trocar moeda "
                   "nacional por estrangeira, nos dois sentidos, à " + vd("paridade anunciada") + "."),
        "destrinchando": [
            "A frase reproduz a definição de " + oc("Mankiw") + " (<i>Macroeconomia</i>): sob câmbio fixo, o "
            "banco central fica pronto para comprar ou vender a moeda doméstica por moedas estrangeiras a um "
            "preço predeterminado.",
            "Mecânica: se o mercado quer mais divisas do que há à paridade, o BC <b>vende</b> divisas (e retira "
            "moeda nacional); se sobra divisa, <b>compra</b> (e emite moeda nacional). É essa disposição "
            "ilimitada de trocar nos dois sentidos que impede a taxa de se mover.",
            "Consequência monetária: a oferta de moeda passa a responder ao balanço de pagamentos. No modelo de "
            + oc("Mundell-Fleming") + " com capitais livres, uma expansão monetária é desfeita pela venda de "
            "reservas; a política fiscal, ao contrário, ganha força.",
            "Ponto fraco: o compromisso só é crível enquanto houver " + azb("reservas") + " para vender. Se o "
            "mercado duvida disso, vem o ataque especulativo (modelos de crise cambial de " + oc("Krugman") + ", "
            "1979).",
        ],
        "dissecando": (cz("[literalidade]") + " Tradução da definição clássica. O “sempre” parece absoluto, mas é "
                       "exatamente a natureza do compromisso: se o BC não estiver sempre pronto, o câmbio deixa de "
                       "ser fixo. Moduladores absolutos podem fazer parte da própria definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio fixo, o banco central compra moeda estrangeira quando há excesso de oferta de divisas "
            "ao preço fixado, expandindo a base monetária.”</i> → CERTO",
            "<i>“Sob câmbio fixo, o banco central intervém apenas para vender divisas, nunca para comprá-las.”</i> "
            "→ ERRADO (restrição indevida: atua nos dois sentidos)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("CERTO: no câmbio fixo, o BC compra ou vende moeda estrangeira para manter a taxa no "
                             "valor preestabelecido."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0772
    {
        "id": "ECO-E1-0772-1", "fonte_ref": "E1-0772", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos da taxa de câmbio sobre a balança comercial, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A hipótese do Efeito da Curva J preconiza que no curto prazo o saldo da balança comercial de "
                      "um país pode piorar frente a um choque de desvalorização do câmbio, aumentando após certo "
                      "período de tempo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A hipótese do Efeito da Curva J preconiza que no curto prazo o saldo da balança comercial de "
                      "um país <u>pode piorar</u> frente a um choque de desvalorização do câmbio, aumentando após "
                      "certo período de tempo."),
        "poucas": ("Na " + azb("curva J") + ", a desvalorização primeiro <b>piora</b> o saldo (efeito-preço) e só "
                   "depois o <b>melhora</b> (efeito-quantidade), desenhando um J ao longo do tempo."),
        "destrinchando": [
            "Por que piora primeiro: no curtíssimo prazo, os volumes de exportação e importação estão presos a "
            "contratos e hábitos; as quantidades quase não mudam, mas cada importação passa a custar mais em "
            "moeda nacional. O " + azb("efeito-preço") + " domina e o saldo cai.",
            "Por que melhora depois: com o tempo, consumidores trocam importados por similares nacionais, "
            "exportadores conquistam mercados e as elasticidades crescem. O " + azb("efeito-quantidade") + " passa "
            "a dominar e o saldo supera o nível inicial.",
            "A melhora final exige a " + azb("condição de Marshall-Lerner") + ": " + vd("|η<sub>X</sub>| + "
            "|η<sub>M</sub>| &gt; 1") + ". A curva J é justamente a constatação de que essas elasticidades são "
            "baixas no curto prazo e maiores no longo.",
            "Cuidado com o objeto: a curva J trata do <b>saldo comercial</b>, não do PIB. E ela supõe que a "
            "desvalorização seja real (não anulada por inflação doméstica).",
        ],
        "grafico_verso": "ECO-E1-0772-1-V1",
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Definição correta, ainda protegida pelo "
                       "“pode piorar”. A banca costuma inverter a ordem (melhora primeiro, piora depois) ou trocar "
                       "o saldo comercial pelo produto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a curva J, a desvalorização melhora o saldo comercial no curto prazo, mas o deteriora no "
            "longo prazo.”</i> → ERRADO (inversão da sequência)",
            "<i>“A curva J decorre de as elasticidades-preço das exportações e importações serem menores no curto "
            "prazo do que no longo prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("CERTO: a desvalorização piora inicialmente o saldo e o melhora depois, formando um J; "
                             "imagem ilustrativa da curva no verso."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (119).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (curva J didática; original não preservado)"}],
        "alertas": ["quase_duplicata: ECO-E1-0369-1 (desvalorização e balança no curto e no longo prazo)"],
    },
    # ------------------------------------------------------------------ E1-0773
    {
        "id": "ECO-E1-0773-1", "fonte_ref": "E1-0773", "destino": "66", "subtema": H2["real"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca da teoria da paridade do poder de compra, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A teoria da paridade do poder de compra pode ser útil na análise do comércio internacional se "
                      "focar no longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria da paridade do poder de compra pode ser útil na análise do comércio internacional se "
                      "focar no <u>longo prazo</u>."),
        "poucas": ("A " + azb("PPC") + " falha no curto prazo (câmbio volátil, preços rígidos), mas descreve bem a "
                   "tendência de " + vd("longo prazo") + ": moedas de países com inflação mais alta se "
                   "depreciam."),
        "destrinchando": [
            azb("PPC absoluta") + ": E = P/P* — uma mesma cesta custa o mesmo nos dois países, convertida pelo "
            "câmbio (lei do preço único aplicada ao nível de preços). " + azb("PPC relativa") + ": a variação "
            "do câmbio iguala o diferencial de inflação, " + vd("ΔE/E ≈ π − π*") + ". Sob a PPC, o "
            + azb("câmbio real") + " é constante.",
            "A ideia foi sistematizada por " + oc("Gustav Cassel") + " após a Primeira Guerra Mundial, para "
            "pensar as novas paridades depois da inflação do período de guerra.",
            "Por que falha no curto prazo: o câmbio nominal reage em minutos a juros, risco e expectativas, "
            "enquanto os preços se ajustam devagar; há custos de transporte, tarifas, bens não comercializáveis "
            "e concorrência imperfeita.",
            "Desvios persistentes conhecidos: o " + azb("efeito Balassa-Samuelson") + " (países mais ricos têm "
            "nível de preços mais alto por causa da produtividade maior nos comercializáveis) — e o "
            + azb("Índice Big Mac") + ", da revista <i>The Economist</i>, que popularizou a comparação.",
            "Mesmo assim, os estudos empíricos mostram que os desvios da PPC se corrigem lentamente, ao longo de "
            "anos — por isso ela é uma referência de longo prazo para o câmbio e para avaliar sobrevalorização.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " “Pode ser útil” + “se focar no longo prazo” "
                       "tornam o item difícil de ser falso. A versão ERRADA típica afirma que a PPC explica as "
                       "oscilações de curto prazo do câmbio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A paridade do poder de compra explica adequadamente as flutuações diárias da taxa de câmbio "
            "nominal.”</i> → ERRADO (a PPC é uma teoria de longo prazo)",
            "<i>“Pela PPC relativa, um país com inflação 5 pontos percentuais acima da de seu parceiro tende a ver "
            "sua moeda depreciar cerca de 5% ao ano.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode", "se"], "dificuldade": 1,
        "comentario_fonte": ("CERTO: no longo prazo, o câmbio tende a refletir o diferencial de preços; a moeda do "
                             "país com mais inflação se desvaloriza."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0775
    {
        "id": "ECO-E1-0775-1", "fonte_ref": "E1-0775", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("No domínio dos regimes cambiais o regime de câmbio flutuante não requer a intervenção do Banco "
                      "Central."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No domínio dos regimes cambiais o regime de câmbio flutuante <u>não requer</u> a intervenção do "
                      "Banco Central."),
        "poucas": ("No " + azb("câmbio flutuante") + ", o mercado forma a taxa; o BC não tem paridade a defender, "
                   "logo a intervenção não é <b>necessária</b> — pode ocorrer, mas por opção."),
        "destrinchando": [
            "A taxa de câmbio flutuante é o preço que equilibra oferta e demanda de divisas. Se sobra dólar, o "
            "preço cai (apreciação); se falta, sobe (depreciação). O ajuste vem pelo preço, sem necessidade de o "
            "BC comprar ou vender reservas.",
            "Isso não quer dizer que o BC esteja proibido de intervir. Na " + azb("flutuação suja") + ", ele atua "
            "para conter volatilidade excessiva ou disfunções de liquidez, sem meta de taxa. Na "
            + azb("flutuação pura") + ", por definição, não intervém.",
            "Contraste com o " + azb("câmbio fixo") + ": ali a intervenção é <b>requisito</b> do regime — sem ela, "
            "a paridade não se sustenta.",
            rx("No Brasil") + ", sob flutuação desde 1999, o BC intervém de forma pontual (swaps cambiais, leilões "
            "de linha e à vista) e declara não ter meta para a taxa.",
            vm("Regra-âncora: no flutuante a intervenção é facultativa; no fixo, obrigatória."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O verbo decide: “não requer” (não é necessária) ≠ "
                       "“não admite” (é proibida). Quem lembra da flutuação suja e lê “não requer” como “nunca "
                       "ocorre” marca ERRADO por engano."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de câmbio flutuante, é vedada qualquer intervenção do Banco Central no mercado de "
            "câmbio.”</i> → ERRADO (modulador absoluto: a flutuação suja admite intervenções)",
            "<i>“No regime de câmbio fixo, a intervenção do Banco Central é condição para a manutenção da "
            "paridade.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["não requer"], "dificuldade": 1,
        "comentario_fonte": ("CERTO: no flutuante puro, a taxa é determinada pela oferta e demanda de divisas, sem "
                             "necessidade de intervenção."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0694-1 (flutuante puro sem intervenção)"],
    },
    # ------------------------------------------------------------------ E1-0776
    {
        "id": "ECO-E1-0776-1", "fonte_ref": "E1-0776", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Uma taxa de câmbio ajustável (com flutuação suja) significa que a autoridade monetária pode "
                      "intervir no mercado de câmbio para impor limites à flutuação da taxa de câmbio. No Brasil, o "
                      "Banco Central costuma intervir no mercado de contratos futuros de câmbio com os chamados swaps "
                      "cambiais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma taxa de câmbio ajustável (com flutuação suja) significa que a autoridade monetária "
                      "<u>pode</u> intervir no mercado de câmbio para impor limites à flutuação da taxa de câmbio. No "
                      "Brasil, o Banco Central costuma intervir no mercado de contratos futuros de câmbio com os "
                      "chamados <u>swaps cambiais</u>."),
        "poucas": ("Na " + azb("flutuação suja") + ", o mercado forma a taxa, mas o BC pode intervir para conter "
                   "oscilações. " + rx("No Brasil") + ", o instrumento típico é o " + azb("swap cambial") + ", "
                   "derivativo liquidado em reais."),
        "destrinchando": [
            azb("Flutuação suja (managed float)") + ": não há paridade nem banda anunciada, mas o BC intervém, de "
            "forma ocasional ou frequente, para suavizar movimentos bruscos, dar liquidez ou conter "
            "disfuncionalidades.",
            azb("Swap cambial tradicional") + ": contrato no mercado de derivativos (B3) em que o BC paga ao "
            "investidor a variação cambial mais um cupom e recebe a taxa de juros DI. Funciona como uma venda de "
            "dólares no mercado futuro: oferece proteção (hedge) contra a depreciação e alivia a pressão sobre o "
            "câmbio à vista, sem gastar reservas, porque a liquidação é em reais. O " + azb("swap reverso") + " "
            "tem efeito oposto (equivale a compra de dólares futuros).",
            "Outros instrumentos do " + rx("BCB") + ": venda de dólares à vista (consome reservas), "
            + azb("leilões de linha") + " (venda com compromisso de recompra, para prover liquidez temporária) e "
            "compras para recompor reservas. Um marco foi o programa diário de leilões de swap lançado em "
            + vd("2013") + ".",
            "⏳ (out/2026) O BCB segue declarando que suas intervenções visam a conter disfuncionalidades, sem meta "
            "para o nível da taxa; os swaps continuam entre os instrumentos usuais.",
        ],
        "dissecando": (cz("[detalhe · modulador relativo]") + " O “pode intervir” protege a 1ª frase, e a 2ª "
                       "depende de um detalhe institucional brasileiro (swap = derivativo, não venda de reservas). "
                       "A expressão “impor limites à flutuação” pode sugerir banda, mas aqui é sinônimo de "
                       "suavizar a trajetória."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nas operações de swap cambial tradicional, o Banco Central do Brasil entrega dólares de suas "
            "reservas internacionais aos investidores no vencimento.”</i> → ERRADO (a liquidação é financeira, em "
            "reais)",
            "<i>“A flutuação suja é incompatível com o regime de câmbio flutuante.”</i> → ERRADO (é uma modalidade "
            "dele)",
        ])],
        "tipo_erro": ["DETALHE", "MODULADOR_RELATIVO"], "moduladores": ["pode", "costuma"], "dificuldade": 2,
        "comentario_fonte": ("CERTO: na flutuação suja, o BC intervém pontualmente; no Brasil, o swap cambial influi "
                             "no câmbio sem mexer nas reservas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0777
    {
        "id": "ECO-E1-0777-1", "fonte_ref": "E1-0777", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_REG,
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta com taxas de câmbio flutuantes há uma massiva entrada de capitais. "
                      "Nesse caso, a taxa de juros que é fixada pelo Banco Central permanece inalterada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia aberta com taxas de câmbio <u>flutuantes</u> há uma massiva entrada de "
                      "capitais. Nesse caso, a taxa de juros que é fixada pelo Banco Central permanece inalterada."),
        "poucas": ("No " + azb("câmbio flutuante") + ", a entrada de capitais é absorvida pela " + vd("apreciação")
                   + " da moeda; o BC não precisa comprar dólares nem emitir moeda, e mantém a "
                   + azb("autonomia") + " sobre os juros."),
        "destrinchando": [
            "Flutuante: a entrada de dólares aumenta a oferta de divisas → a moeda nacional se aprecia → as "
            "exportações líquidas caem até reequilibrar o balanço de pagamentos. A base monetária não muda, e a "
            "taxa de juros continua sendo decisão do BC.",
            "Fixo (contraste): para impedir a apreciação, o BC compra os dólares que entram e emite moeda "
            "nacional. A base monetária se expande e os juros tendem a cair — a menos que o BC "
            + azb("esterilize") + " a operação vendendo títulos (o que tem custo fiscal, porque os juros internos "
            "costumam superar o rendimento das reservas).",
            "É o " + azb("trilema") + ": com livre mobilidade de capitais, o câmbio flutuante é o que preserva a "
            "política monetária autônoma.",
            "Ressalva: o BC <b>pode</b> escolher mudar os juros (por exemplo, se a apreciação derrubar a inflação "
            "abaixo da meta), mas não é <b>obrigado</b> a isso pelo fluxo de capitais.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Quem pensa “entrou dinheiro, os juros caem” "
                       "aplica a lógica do câmbio fixo. A palavra decisiva é “flutuantes”: o ajuste vai para o "
                       "câmbio, não para a moeda em circulação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio fixo, uma massiva entrada de capitais, não esterilizada, expande a base "
            "monetária e tende a reduzir a taxa de juros.”</i> → CERTO",
            "<i>“Em regime de câmbio flutuante, a massiva entrada de capitais obriga o Banco Central a comprar "
            "divisas, o que expande a base monetária.”</i> → ERRADO (troca de regime: essa obrigação é do câmbio "
            "fixo)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("CERTO: no câmbio flutuante, o BC mantém os juros; o ajuste vem pela apreciação "
                             "cambial, não pela política monetária."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0821
    {
        "id": "ECO-E1-0821-1", "fonte_ref": "E1-0821", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": CMD_CACD26,
        "excerto": EXCERTO_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("A elevação do risco de um país, provocada por uma crise de confiança, leva à saída de capitais "
                      "e aumenta a pressão de depreciação cambial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elevação do risco de um país, provocada por uma crise de confiança, leva à <u>saída de "
                      "capitais</u> e aumenta a pressão de <u>depreciação</u> cambial."),
        "poucas": ("Mais " + azb("prêmio de risco") + " = ativos do país menos atraentes ao mesmo juro → capitais "
                   "saem → demanda por divisas sobe → " + vd("E ↑") + " (pressão de depreciação)."),
        "destrinchando": [
            "Paridade de juros com prêmio de risco: " + vd("i = i* + (Eᵉ − E)/E + ρ") + ". Se o risco ρ sobe e "
            "os juros domésticos i não mudam, o retorno ajustado ao risco de aplicar no país cai; os investidores "
            "vendem ativos locais e compram divisas.",
            "Efeito no câmbio: com câmbio flutuante, a moeda se deprecia; com câmbio fixo, a pressão aparece como "
            + azb("perda de reservas") + " — o BC vende divisas para segurar a paridade, e pode ter de subir juros.",
            "Respostas de política (como o texto lembra): elevar juros para compensar o prêmio, intervir com "
            "reservas ou swaps, ou deixar o câmbio absorver o choque. A eficácia depende do regime e do grau de "
            "mobilidade de capitais.",
            rx("Brasil") + ": na eleição de " + vd("2002") + ", a crise de confiança levou o risco-país a mais de "
            "2.000 pontos e o real a forte depreciação; em " + vd("2015") + ", a deterioração fiscal e a perda do "
            "grau de investimento produziram movimento semelhante.",
            vm("Regra-âncora: risco ↑ → saída de capitais → depreciação (ou perda de reservas, no câmbio fixo)."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Cadeia causal direta, ancorada no próprio texto (“choques de "
                       "confiança e alterações no prêmio de risco podem afetar fluxos de capitais e pressionar a "
                       "taxa de câmbio”). O “aumenta a pressão” é cuidadoso: não diz que a depreciação ocorrerá "
                       "sempre, o que protege o item no câmbio fixo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação do risco-país tende a apreciar a moeda doméstica, pois eleva os juros exigidos pelos "
            "investidores.”</i> → ERRADO (inversão: o efeito imediato é saída de capitais e depreciação)",
            "<i>“Sob câmbio fixo, uma crise de confiança tende a se manifestar em perda de reservas "
            "internacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Só o gabarito (CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0822-1, ECO-E1-0823-1 (mesmo texto motivador, CACD 2026)"],
    },
    # ------------------------------------------------------------------ E1-0822
    {
        "id": "ECO-E1-0822-1", "fonte_ref": "E1-0822", "destino": "66", "subtema": H2["real"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": CMD_CACD26,
        "excerto": EXCERTO_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("Uma taxa de câmbio real definida por q = EP*/P (em que E = moeda nacional por moeda "
                      "estrangeira, P = nível de preços doméstico e P* = nível de preços externo) em trajetória "
                      "ascendente ao longo do tempo indica, ceteris paribus, aumento da competitividade-preço das "
                      "exportações do país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma taxa de câmbio real definida por q = EP*/P (em que E = moeda nacional por moeda "
                      "estrangeira, P = nível de preços doméstico e P* = nível de preços externo) em trajetória "
                      "<u>ascendente</u> ao longo do tempo indica, ceteris paribus, <u>aumento</u> da "
                      "competitividade-preço das exportações do país."),
        "poucas": ("Com q = EP*/P, " + vd("q ↑") + " significa que os bens estrangeiros ficaram mais caros em "
                   "relação aos nacionais (" + azb("depreciação real") + "): os produtos do país ganham "
                   "competitividade-preço."),
        "destrinchando": [
            "Leitura da fórmula: EP* é o preço da cesta estrangeira convertido em moeda nacional; P é o preço da "
            "cesta nacional. Logo q = quantas cestas nacionais compra-se com uma cesta estrangeira — o "
            + azb("preço relativo") + " dos bens externos.",
            "q sobe quando: E sobe (depreciação nominal), P* sobe (inflação externa) ou P cai/sobe menos "
            "(inflação doméstica menor). Em todos os casos, o bem nacional fica relativamente mais barato → "
            "exportações mais competitivas e importações menos atraentes.",
            "Atenção à convenção: alguns textos definem o câmbio real ao contrário (P/EP*); aí, alta significa "
            + azb("apreciação real") + " e perda de competitividade. O item resolve a ambiguidade ao dar a "
            "fórmula — sempre leia a definição antes de julgar a direção.",
            "Distinção cobrada no texto: a variação do " + azb("câmbio nominal") + " só melhora a competitividade "
            "se não for anulada pela inflação. Exemplo: depreciação nominal de 10% com inflação doméstica 10% "
            "acima da externa deixa q praticamente inalterado.",
            vm("Regra-âncora: com q = EP*/P, q ↑ = depreciação real = ganho de competitividade-preço."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item depende inteiramente da convenção dada. O risco "
                       "é o candidato associar “subir” a “valorizar” (como no preço de um ativo) e marcar ERRADO. "
                       "O “ceteris paribus” afasta objeções sobre qualidade, tarifas ou demanda externa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com q definido como P/(EP*), uma trajetória ascendente de q indica ganho de competitividade-preço "
            "das exportações.”</i> → ERRADO (convenção invertida: aí a alta é apreciação real)",
            "<i>“Uma depreciação nominal de 10%, acompanhada de inflação doméstica 10 pontos acima da externa, "
            "deixa a taxa de câmbio real aproximadamente constante.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["ceteris paribus"], "dificuldade": 2,
        "comentario_fonte": "Só o gabarito (CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0821-1, ECO-E1-0823-1 (mesmo texto motivador, CACD 2026)",
                    "quase_duplicata: ECO-E1-0867-1 (inflação doméstica e câmbio real)"],
    },
    # ------------------------------------------------------------------ E1-0823
    {
        "id": "ECO-E1-0823-1", "fonte_ref": "E1-0823", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": CMD_CACD26,
        "excerto": EXCERTO_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("Em regime de câmbio fixo, a autoridade monetária não pode utilizar a taxa de juros como "
                      "instrumento de defesa da paridade cambial previamente estabelecida."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em regime de câmbio fixo, a autoridade monetária ") + vm("não pode") + az(" utilizar a taxa "
                    "de juros como instrumento de defesa da paridade cambial previamente estabelecida.")),
        "poucas": ("Os " + azb("juros") + " são uma das principais armas de defesa da paridade: subir i atrai "
                   "capitais e encarece apostas contra a moeda. No câmbio fixo, a política monetária fica "
                   "<b>a serviço</b> do câmbio."),
        "destrinchando": [
            "Sob câmbio fixo e mobilidade de capitais, se o mercado aposta numa desvalorização, capitais saem e "
            "as reservas caem. O BC pode (1) vender reservas e (2) " + vd("elevar os juros") + ", aumentando o "
            "retorno de manter ativos em moeda nacional e o custo de tomar emprestado nela para comprar divisas.",
            "Pelo " + azb("trilema") + ", o país com câmbio fixo e capitais livres perde a autonomia monetária — "
            "mas isso significa justamente que os juros passam a ser usados para sustentar o câmbio, e não que "
            "ficam proibidos.",
            "Casos clássicos: a Suécia elevou sua taxa marginal a " + vd("500%") + " em setembro de 1992, na "
            "crise do Sistema Monetário Europeu; " + rx("o Brasil") + " levou a taxa básica a mais de 40% na "
            "crise asiática (1997) e na russa (1998) para defender a âncora cambial do Plano Real.",
            "Limite: juros muito altos agravam a recessão e a dívida pública; se o mercado duvidar de que o país "
            "aguenta esse custo, o ataque continua e a paridade cai (modelos de crise de " + oc("Obstfeld") + ").",
            vm("Regra-âncora: no câmbio fixo, os juros não são livres — são o instrumento de defesa da paridade."),
        ],
        "dissecando": (cz("[inversão · restrição indevida]") + " Confunde “perder autonomia monetária” (não poder "
                       "usar os juros para objetivos internos) com “não poder usar os juros” de forma alguma. O "
                       "próprio texto lista “juros, intervenção e reservas” como respostas de política."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio fixo com livre mobilidade de capitais, a política monetária perde autonomia "
            "para perseguir objetivos internos, como o nível de emprego.”</i> → CERTO",
            "<i>“A defesa de uma paridade fixa pode exigir tanto a venda de reservas quanto a elevação dos "
            "juros.”</i> → CERTO",
        ])],
        "reescrita": ("Em regime de câmbio fixo, a autoridade monetária " + hl("pode") + " utilizar a taxa de juros "
                      "como instrumento de defesa da paridade cambial previamente estabelecida."),
        "tipo_erro": ["INVERSAO", "RESTRICAO"], "moduladores": ["não pode"], "dificuldade": 1,
        "comentario_fonte": "Só o gabarito (ERRADO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0821-1, ECO-E1-0822-1 (mesmo texto motivador, CACD 2026)"],
    },
    # ------------------------------------------------------------------ E1-0867
    {
        "id": "ECO-E1-0867-1", "fonte_ref": "E1-0867", "destino": "66", "subtema": H2["real"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à taxa de câmbio real.",
        "rotulo_item": "Item",
        "assertiva": "O aumento da inflação doméstica terá como efeito uma depreciação da taxa de câmbio real.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O aumento da inflação doméstica terá como efeito uma ") + vm("depreciação")
                    + az(" da taxa de câmbio real.")),
        "poucas": ("Com q = EP*/P, " + vd("P ↑") + " (mantidos E e P*) " + vd("reduz q") + ": é "
                   + azb("apreciação real") + " — os bens nacionais ficam mais caros em relação aos "
                   "estrangeiros."),
        "destrinchando": [
            "Taxa de câmbio real: " + vd("q = E·P*/P") + " (E = moeda nacional por estrangeira). Ela mede o "
            "preço dos bens estrangeiros em termos dos nacionais. q ↑ = depreciação real; q ↓ = apreciação real.",
            "Inflação doméstica maior, sem depreciação nominal que a compense, eleva P e derruba q: o país "
            "perde competitividade-preço — exporta menos e importa mais. É a " + azb("apreciação real") + " pela "
            "via dos preços.",
            "Exemplo: E constante, inflação doméstica de 10% e externa de 2% → q cai cerca de " + vd("8%") + ". "
            "Para manter q constante, o câmbio nominal teria de se depreciar uns 8% (é o que prevê a "
            + azb("PPC relativa") + ").",
            "Caso histórico: na âncora cambial do Plano Real (1994–1998), a inflação residual acima da externa, "
            "com câmbio nominal quase estável, produziu apreciação real e déficits comerciais crescentes.",
            "Correção de um comentário da fonte, que descreve a fórmula ao contrário (“nominal × inflação "
            "doméstica ÷ inflação externa”): os preços externos vão no numerador e os domésticos no denominador.",
            vm("Regra-âncora: inflação doméstica ↑ (com E fixo) → câmbio real ↓ → apreciação real."),
        ],
        "dissecando": (cz("[inversão]") + " Troca apreciação por depreciação. A armadilha é associar inflação a "
                       "“moeda fraca”: a inflação de fato tende a depreciar o câmbio <b>nominal</b> ao longo do "
                       "tempo, mas, mantido o nominal, ela <b>aprecia</b> o câmbio real."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento da inflação externa, mantidos o câmbio nominal e os preços domésticos, deprecia a taxa "
            "de câmbio real.”</i> → CERTO",
            "<i>“Pela paridade do poder de compra relativa, a inflação doméstica mais alta tende a apreciar o "
            "câmbio nominal.”</i> → ERRADO (tende a depreciá-lo)",
        ])],
        "reescrita": ("O aumento da inflação doméstica terá como efeito uma " + hl("apreciação")
                      + " da taxa de câmbio real."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO: a inflação doméstica aprecia o câmbio real; mas um dos comentários descreve a "
                             "fórmula invertida (nominal × inflação doméstica ÷ externa) e outro inventa uma "
                             "apreciação nominal pela via do déficit comercial."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0822-1 (câmbio real q = EP*/P)"],
    },
    # ------------------------------------------------------------------ E1-0879
    {
        "id": "ECO-E1-0879-1", "fonte_ref": "E1-0879", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos regimes de câmbio e dos determinantes da taxa de câmbio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Uma redução da taxa de juros doméstica, coeteris paribus, aumenta a taxa de câmbio flutuante, "
                      "se houver mobilidade de capitais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma redução da taxa de juros doméstica, coeteris paribus, <u>aumenta</u> a taxa de câmbio "
                      "flutuante, se houver mobilidade de capitais."),
        "poucas": ("Juros menores → capitais saem → mais procura por divisas → " + vd("E sobe") + ": mais moeda "
                   "nacional por unidade de moeda estrangeira, ou seja, " + azb("depreciação") + "."),
        "destrinchando": [
            "Convenção: a taxa de câmbio E é o preço da moeda estrangeira em moeda nacional (R$/US$). “Aumentar "
            "a taxa de câmbio” = depreciar a moeda nacional.",
            "Mecanismo, pela " + azb("paridade descoberta de juros") + " (i = i* + depreciação esperada): com "
            "i abaixo de i*, aplicar no país rende menos; os investidores migram para fora e compram divisas até "
            "que o câmbio suba.",
            "As duas condições do item são essenciais: " + azb("câmbio flutuante") + " (no fixo, o BC venderia "
            "reservas e a taxa não subiria; aliás, ele nem conseguiria sustentar juros abaixo dos externos por "
            "muito tempo) e " + azb("mobilidade de capitais") + " (sem ela, o diferencial de juros pouco afeta "
            "o fluxo financeiro).",
            "O “coeteris paribus” isola o efeito: se ao mesmo tempo os juros externos caíssem ou o risco-país "
            "diminuísse, o câmbio poderia não subir.",
            vm("Regra-âncora: i ↓ → E ↑ (depreciação); i ↑ → E ↓ (apreciação), com capitais móveis e câmbio "
               "flutuante."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A dificuldade é de vocabulário: “aumenta a taxa de "
                       "câmbio” soa como “fortalece a moeda” para quem não domina a convenção R$/US$. As condições "
                       "(flutuante, mobilidade, coeteris paribus) estão todas no lugar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução da taxa de juros doméstica, coeteris paribus, aprecia a moeda nacional sob câmbio "
            "flutuante e mobilidade de capitais.”</i> → ERRADO (inversão: deprecia)",
            "<i>“Sem mobilidade de capitais, variações na taxa de juros doméstica têm efeito reduzido sobre a "
            "taxa de câmbio pelo canal financeiro.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["coeteris paribus", "se"], "dificuldade": 1,
        "comentario_fonte": ("CERTO: juros menores reduzem a atratividade dos ativos nacionais, geram saída de "
                             "capital e depreciação (aumento da taxa de câmbio)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0427-1 (queda de juros e depreciação)"],
    },
    # ------------------------------------------------------------------ E1-0886
    {
        "id": "ECO-E1-0886-1", "fonte_ref": "E1-0886", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos regimes cambiais, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na presença de uma crise interna com deterioração fiscal: o regime de câmbio flutuante pode "
                      "acelerar os benefícios das rendas geradas com as exportações."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na presença de uma crise interna com deterioração fiscal: o regime de câmbio flutuante "
                      "<u>pode</u> acelerar os benefícios das rendas geradas com as exportações."),
        "poucas": ("No " + azb("câmbio flutuante") + ", a crise deprecia a moeda de imediato; cada dólar exportado "
                   "passa a render mais em moeda nacional e as exportações ganham competitividade, o que amortece "
                   "o choque."),
        "destrinchando": [
            "Uma crise fiscal eleva o risco-país e provoca saída de capitais. No flutuante, isso se traduz logo "
            "em " + azb("depreciação") + ": o exportador recebe mais reais por dólar (renda maior em moeda "
            "nacional) e o produto nacional fica mais barato lá fora.",
            "O câmbio funciona como " + azb("amortecedor de choques") + ": a demanda externa compensa parte da "
            "queda da demanda interna. No câmbio fixo, esse alívio não vem — o ajuste recai sobre reservas, juros "
            "e atividade, e pode terminar numa desvalorização desordenada.",
            "O “pode” é necessário, porque há custos: a depreciação pressiona a inflação (repasse cambial), "
            "aumenta o peso das dívidas em moeda estrangeira (risco de " + azb("efeito balanço") + ") e leva "
            "tempo para elevar volumes exportados (curva J).",
            rx("Brasil") + ": na recessão de 2015–2016, marcada por deterioração fiscal, a forte depreciação do "
            "real ajudou a reverter o déficit comercial e a reduzir o déficit em transações correntes.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “pode” salva uma formulação vaga (“acelerar os "
                       "benefícios das rendas”). Itens com potencial sem garantia, sobre canais conhecidos (câmbio → "
                       "exportações), tendem a ser CERTOS; a versão ERRADA costuma trocar o “pode” por "
                       "“garante” ou atribuir o efeito ao câmbio fixo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em uma crise fiscal, o regime de câmbio fixo permite ajuste imediato da competitividade das "
            "exportações pela variação da taxa de câmbio.”</i> → ERRADO (troca de regime: no fixo a taxa não "
            "varia)",
            "<i>“Em uma crise fiscal, a depreciação no câmbio flutuante garante a recuperação do produto no curto "
            "prazo.”</i> → ERRADO (modulador absoluto)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("CERTO: em crise fiscal, o câmbio flutuante permite desvalorizar, barateando as "
                             "exportações e gerando entrada de divisas que mitiga a crise."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
