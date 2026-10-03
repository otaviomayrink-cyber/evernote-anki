"""Cards do lote de redação 10 — ECO, passada 02 (notas 26: keynesiano simples e 27: IS-LM)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "dem": "📈 Demanda efetiva e cruz keynesiana",
    "mult": "✖️ Multiplicadores",
    "is": "📉 Curva IS",
    "lm": "📈 Curva LM",
    "pol": "🏦 Política fiscal e monetária",
    "ext": "🕳️ Casos extremos",
}

CMD_NAB_KEY = ("Julgue (C ou E) os itens a seguir, de acordo com o que a teoria keynesiana dispõe acerca da "
               "demanda efetiva e da oferta e demanda agregadas.")

CMD_PANDEMIA = ("O Brasil fez uso da política fiscal durante a pandemia, com o governo elevando gastos com saúde e "
                "educação, reduzindo ou adiando o pagamento de impostos, bem como pagando auxílio às famílias mais "
                "pobres. A este respeito, julgue o item a seguir.")

CMD_EFIC_MON = "Dentro do modelo IS-LM, no tocante à eficácia da política monetária, julgue o item a seguir."

CMD_ISLM = "Julgue o item a seguir, relativo ao modelo IS-LM."

CMD_SINTESE = "Com relação ao modelo IS-LM da síntese neoclássica, julgue o item a seguir."

CMD_EMPREGO = ("Um país de economia fechada que tenha por objetivo elevar o nível de emprego poderá utilizar "
               "instrumentos de política fiscal expansiva. Nesse contexto, julgue o item a seguir.")

FIG_PERDIDA = lambda ref: {"ref": ref, "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}

CARDS = [
    # ------------------------------------------------------------------ E2-L00837
    {
        "id": "ECO-E2-L00837-1", "fonte_ref": "E2-L00837", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação às políticas monetária e fiscal, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considere uma economia em que o governo está planejando implementar uma expansão fiscal para "
                      "estimular a atividade econômica. Se a propensão marginal a consumir for igual a 0,8, o "
                      "multiplicador fiscal será maior do que se a propensão marginal a consumir for igual a 0,5."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere uma economia em que o governo está planejando implementar uma expansão fiscal para "
                      "estimular a atividade econômica. Se a propensão marginal a consumir for igual a 0,8, o "
                      "multiplicador fiscal será <u>maior</u> do que se a propensão marginal a consumir for igual "
                      "a 0,5."),
        "poucas": ("No modelo keynesiano simples, o multiplicador é " + vd("1/(1 − c)") + ": com c = 0,8 vale "
                   + vd("5") + "; com c = 0,5 vale " + vd("2") + ". Quanto maior a " + azb("PMgC") + ", maior o "
                   "multiplicador."),
        "destrinchando": [
            "Na " + azb("cruz keynesiana") + " (economia fechada, sem tributação proporcional), Y = C₀ + cY + I + G "
            "→ Y = [1/(1 − c)] × (C₀ + I + G). O termo " + vd("1/(1 − c)") + " é o " + azb("multiplicador dos "
            "gastos autônomos") + ": ΔY = ΔG/(1 − c).",
            "Contas do item: c = 0,8 → 1/0,2 = " + vd("5") + "; c = 0,5 → 1/0,5 = " + vd("2") + ". Um gasto "
            "extra de 100 eleva a renda em 500 no primeiro caso e em 200 no segundo.",
            "Intuição da rodada: o gasto do governo vira renda de alguém, que consome a fração c; esse consumo vira "
            "renda de outro, que consome c de novo… A soma da progressão geométrica 1 + c + c² + … é 1/(1 − c). "
            "Quanto menos se " + azb("poupa") + " a cada rodada (menor PMgS = 1 − c), mais longa a cadeia.",
            "Com tributação proporcional (alíquota t) e importações (PMgM = m), o multiplicador encolhe para "
            "1/[1 − c(1 − t) + m]: impostos e importações são " + azb("vazamentos") + " que, como a poupança, "
            "interrompem a cadeia.",
            vm("Regra-âncora: multiplicador = 1/(PMgS + vazamentos); mais consumo marginal, mais multiplicador."),
        ],
        "dissecando": (cz("[literalidade]") + " Item de conta direta: aplica a fórmula de manual com dois "
                       "valores de c. A armadilha seria inverter a lógica e achar que consumir mais “gasta” o "
                       "estímulo; é o contrário — o que interrompe a cadeia é a poupança."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a propensão marginal a poupar for igual a 0,2, o multiplicador fiscal será igual a 5.”</i> → "
            "CERTO",
            "<i>“Se a propensão marginal a consumir for igual a 0,8, o multiplicador fiscal será igual a 1,25.”</i> → "
            "ERRADO (conta invertida: usou 1/c em vez de 1 sobre 1 − c; o certo é 5)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Multiplicador 1/(1 − c): c = 0,8 → 5; c = 0,5 → 2. Maior PMgC, maior multiplicador.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00912
    {
        "id": "ECO-E2-L00912-1", "fonte_ref": "E2-L00912", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_KEY,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com as ideias keynesianas, o governo aumentou seus gastos em $100 milhões. Sabendo "
                      "que a propensão a consumir da população corresponde ao número 0,75, o aumento esperado na "
                      "renda local será de $200 milhões."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com as ideias keynesianas, o governo aumentou seus gastos em $100 milhões. Sabendo "
                       "que a propensão a consumir da população corresponde ao número 0,75, o aumento esperado na "
                       "renda local será de ") + vm("$200 milhões") + az(".")),
        "poucas": ("Com c = 0,75, o multiplicador é " + vd("1/(1 − 0,75) = 4") + ": ΔY = 4 × 100 = "
                   + vd("$400 milhões") + ", não 200."),
        "destrinchando": [
            "Roteiro: (1) multiplicador " + vd("k = 1/(1 − c)") + " = 1/0,25 = " + vd("4") + "; (2) ΔY = k × ΔG = "
            "4 × 100 = " + vd("400") + ".",
            "Os 200 do item correspondem a um multiplicador 2, que só valeria com c = 0,5 — ou a quem confunde "
            "a PMgS (0,25) com outra coisa. Outro erro comum é usar 1/c = 1,33 (ΔY ≈ 133).",
            "Decomposição da cadeia: 100 (gasto inicial) + 75 + 56,25 + 42,19 + … = 100 × (1 + 0,75 + 0,75² + …) "
            "= 400. Desses 400, 300 são consumo induzido e 100 são a injeção original; a poupança induzida soma "
            + vd("0,25 × 400 = 100") + ", exatamente o gasto inicial — no novo equilíbrio, vazamentos = injeções.",
            "O resultado vale para o modelo simples: economia fechada, sem tributação proporcional à renda, preços "
            "e juros constantes. Com IS-LM, o " + azb("crowding out") + " reduz o efeito; com tributação e "
            "importações, o multiplicador encolhe.",
        ],
        "dissecando": (cz("[dado alterado]") + " O enunciado é armado para a conta; o erro está só no número "
                       "final. Itens de multiplicador quase sempre premiam quem calcula 1/(1 − c) e punem quem "
                       "estima de cabeça."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento esperado na renda será de $400 milhões, dos quais $300 milhões correspondem ao consumo "
            "induzido.”</i> → CERTO",
            "<i>“…se a mesma injeção fosse feita como transferência às famílias, o aumento da renda seria também "
            "de $400 milhões.”</i> → ERRADO (transferência tem multiplicador menor, c ÷ PMgS = 3: ΔY = 300)",
        ])],
        "reescrita": ("De acordo com as ideias keynesianas, o governo aumentou seus gastos em $100 milhões. Sabendo "
                      "que a propensão a consumir da população corresponde ao número 0,75, o aumento esperado na "
                      "renda local será de " + hl("$400 milhões") + "."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ΔG = 100; c = 0,75; multiplicador 1/(1 − 0,75) = 4; ΔY = 400 milhões.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 152", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (cálculo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00913
    {
        "id": "ECO-E2-L00913-1", "fonte_ref": "E2-L00913", "destino": "26", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_KEY,
        "rotulo_item": "Item",
        "assertiva": ("O volume de emprego será determinado pelo ponto de intersecção da oferta agregada e da demanda "
                      "agregada. A definição do volume de emprego é uma atribuição do governo e não dos empresários, "
                      "como no modelo clássico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O volume de emprego será determinado pelo ponto de intersecção da oferta agregada e da "
                       "demanda agregada. A definição do volume de emprego é uma atribuição ")
                    + vm("do governo e não dos empresários") + az(", como no modelo clássico.")),
        "poucas": ("Em " + oc("Keynes") + ", quem decide quanto produzir e quantos contratar são os "
                   + azb("empresários") + ", com base na " + azb("demanda efetiva") + " esperada. O governo pode "
                   "influir nessa demanda, mas não “define” o emprego."),
        "destrinchando": [
            "A 1ª frase está correta: é o " + azb("princípio da demanda efetiva") + " (<i>Teoria Geral</i>, cap. 3). "
            "O emprego se fixa no ponto em que a função de demanda agregada (receita que os empresários "
            "<b>esperam</b> obter) cruza a função de oferta agregada (receita mínima que justifica empregar N "
            "trabalhadores). Esse ponto é a demanda efetiva.",
            "Logo, o volume de emprego é decisão privada: o empresário contrata o que espera conseguir vender, "
            "olhando para o consumo (propensão a consumir) e para o investimento (eficiência marginal do capital × "
            "juros). Nada garante que esse ponto seja o pleno emprego.",
            "O papel do governo em Keynes é <b>indireto</b>: gastos públicos, tributos e política monetária "
            "deslocam a demanda efetiva e, com isso, mudam o emprego que os empresários decidem oferecer.",
            "Contraste com os " + azb("clássicos") + ": o emprego sai do mercado de trabalho (oferta e demanda de "
            "trabalho, salário real flexível) e a " + azb("lei de Say") + " garante que toda produção encontra "
            "demanda. Em Keynes, o emprego deixa de ser determinado no mercado de trabalho e passa a sê-lo no "
            "mercado de bens.",
            vm("Regra-âncora: em Keynes, o emprego é decidido pelos empresários segundo a demanda efetiva; o "
               "governo só a influencia."),
        ],
        "dissecando": (cz("[troca de ator · meia-verdade]") + " A 1ª frase reproduz o princípio da demanda "
                       "efetiva e dá credibilidade; o erro está na 2ª, que transfere ao governo uma decisão que "
                       "Keynes atribui aos empresários e ainda põe estes no “modelo clássico”. Pista: Keynes "
                       "defende intervenção, não planejamento do emprego."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Keynes, o governo pode elevar o volume de emprego ao ampliar a demanda efetiva por meio de "
            "política fiscal expansionista.”</i> → CERTO",
            "<i>“Para Keynes, o volume de emprego é determinado no mercado de trabalho, pela igualdade entre "
            "salário real e produtividade marginal do trabalho.”</i> → ERRADO (visão clássica)",
        ])],
        "reescrita": ("O volume de emprego será determinado pelo ponto de intersecção da oferta agregada e da demanda "
                      "agregada. A definição do volume de emprego é uma atribuição "
                      + hl("dos empresários, com base na demanda efetiva esperada, e não do mercado de trabalho")
                      + ", como no modelo clássico."),
        "tipo_erro": ["TROCA_ATOR", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "O governo influencia emprego e renda via política fiscal, mas Keynes não atribui ao "
                            "governo a definição do emprego; ela depende da propensão a consumir e das decisões de "
                            "investimento dos empresários.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00937
    {
        "id": "ECO-E2-L00937-1", "fonte_ref": "E2-L00937", "destino": "26", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": "Em relação à teoria macroeconômica, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A Teoria Geral do Emprego do Juro e da Moeda (1936), escrita por John Maynard Keynes, "
                      "redefiniu o debate sobre os determinantes do emprego, da renda e da produção agregados nos "
                      "anos 1930. De acordo com a abordagem de Keynes, o principal fator que explica a persistência "
                      "do elevado desemprego é falta de disposição dos trabalhadores desempregados para aceitar "
                      "redução dos salários reais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Teoria Geral do Emprego do Juro e da Moeda (1936), escrita por John Maynard Keynes, "
                       "redefiniu o debate sobre os determinantes do emprego, da renda e da produção agregados nos "
                       "anos 1930. De acordo com a abordagem de Keynes, o principal fator que explica a "
                       "persistência do elevado desemprego é ")
                    + vm("falta de disposição dos trabalhadores desempregados para aceitar redução dos salários "
                         "reais") + az(".")),
        "poucas": ("Para " + oc("Keynes") + ", o desemprego persistente vem da " + azb("insuficiência de demanda "
                   "efetiva") + ". Culpar a recusa dos trabalhadores em aceitar salários menores é a explicação "
                   + azb("clássica") + " que ele combateu."),
        "destrinchando": [
            "Na visão " + azb("clássica") + " (" + oc("Pigou") + " é o alvo explícito da <i>Teoria Geral</i>), "
            "todo desemprego duradouro é " + azb("voluntário") + " ou friccional: se os trabalhadores aceitassem "
            "salário real menor, as firmas contratariam mais até o mercado de trabalho se equilibrar.",
            oc("Keynes") + " inverte o diagnóstico: o desemprego é " + azb("involuntário") + " — há gente disposta a "
            "trabalhar pelo salário vigente (ou menos) sem encontrar vaga — porque os empresários só contratam o "
            "que esperam vender, e a demanda agregada (consumo + investimento) é insuficiente.",
            "Ele vai além: mesmo que os salários nominais caíssem, isso não curaria o desemprego. Salário menor "
            "reduz renda e consumo, derruba preços e pode piorar as expectativas; o salário <b>real</b> nem sequer "
            "está sob controle dos trabalhadores, que negociam o nominal. Por isso a rigidez salarial não é, em "
            "Keynes, a causa do problema.",
            "Atenção à nuance: Keynes reconhece que os trabalhadores resistem a cortes <b>nominais</b>, mas aceitam "
            "perda real via alta de preços. Isso é constatação, não a explicação do desemprego.",
            "A saída keynesiana é elevar a demanda efetiva — gasto público, juros baixos, estímulo ao investimento "
            "—, não flexibilizar salários.",
        ],
        "dissecando": (cz("[troca de conceito · troca de ator]") + " A 1ª frase é contexto verdadeiro sobre a "
                       "<i>Teoria Geral</i>; o erro está na causa atribuída a Keynes, que é a tese da escola que "
                       "ele criticava. 🔥 A banca adora pôr a explicação clássica na boca de Keynes."),
        "modulos": [("📚 Autores e teses", [
            oc("Pigou") + " (<i>The Theory of Unemployment</i>, 1933) → desemprego por salários reais acima do "
            "equilíbrio; cura: flexibilidade salarial.",
            oc("Keynes") + " (<i>Teoria Geral</i>, 1936) → desemprego involuntário por insuficiência de demanda "
            "efetiva; cura: sustentar a demanda.",
        ]), ("😈 Para dificultar", [
            "<i>“Para Keynes, a redução dos salários nominais não seria remédio eficaz para o desemprego, pois "
            "poderia deprimir ainda mais a demanda agregada.”</i> → CERTO",
            "<i>“Para Keynes, o desemprego persistente nos anos 1930 era essencialmente voluntário.”</i> → ERRADO "
            "(tese clássica: para Keynes é involuntário)",
        ])],
        "reescrita": ("A Teoria Geral do Emprego do Juro e da Moeda (1936), escrita por John Maynard Keynes, "
                      "redefiniu o debate sobre os determinantes do emprego, da renda e da produção agregados nos "
                      "anos 1930. De acordo com a abordagem de Keynes, o principal fator que explica a persistência "
                      "do elevado desemprego é " + hl("a insuficiência de demanda efetiva") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "TROCA_ATOR"], "moduladores": ["principal"], "dificuldade": 1,
        "comentario_fonte": "Para Keynes, a causa do desemprego é a insuficiência de demanda efetiva; salários "
                            "rígidos ou recusa de redução do salário real é explicação clássica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01243
    {
        "id": "ECO-E2-L01243-1", "fonte_ref": "E2-L01243", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Com base no modelo IS-LM-BP, julgue o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("Abertura econômica tende a aumentar o multiplicador dos gastos do governo sobre o produto da "
                      "economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Abertura econômica tende a ") + vm("aumentar") + az(" o multiplicador dos gastos do governo "
                                                                            "sobre o produto da economia.")),
        "poucas": ("Abrir a economia eleva a " + azb("propensão marginal a importar") + " (m), que entra como "
                   + azb("vazamento") + " no denominador do multiplicador " + vd("1/(1 − c + m)") + ": o "
                   "multiplicador <b>diminui</b>."),
        "destrinchando": [
            "Economia aberta: Y = C₀ + cY + I + G + X − (M₀ + mY). Isolando Y: " + vd("Y = [1/(1 − c + m)] × "
            "(C₀ + I + G + X − M₀)") + ". O multiplicador dos gastos é 1/(1 − c + m).",
            "Exemplo: c = 0,8. Fechada (m = 0): 1/0,2 = " + vd("5") + ". Aberta com m = 0,2: 1/0,4 = " + vd("2,5")
            + ". Metade do efeito sobre o produto doméstico some.",
            "Intuição: a cada rodada do multiplicador, parte da renda nova é gasta em bens estrangeiros. Esse gasto "
            "gera renda e emprego <b>lá fora</b>, não aqui — é a fração que “vaza” do fluxo circular, como a "
            "poupança e os impostos.",
            "O efeito vazado não desaparece do mundo: as importações de um país são exportações de outro, e a "
            "expansão pode voltar parcialmente como demanda por exportações (efeito-repercussão). No modelo de "
            "um país, porém, ele é tratado como perda.",
            "No IS-LM-BP com câmbio flutuante e mobilidade perfeita de capitais (" + oc("Mundell-Fleming")
            + "), a política fiscal fica ainda mais fraca: a apreciação cambial derruba as exportações líquidas "
            "e anula o efeito sobre o produto.",
            vm("Regra-âncora: mais abertura → maior m → menor multiplicador."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido do efeito. Quem associa “abertura” a "
                       "“crescimento” marca CERTO por intuição; o item cobra só a mecânica do denominador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a propensão marginal a importar, menor o impacto de um aumento dos gastos do governo "
            "sobre o produto doméstico.”</i> → CERTO",
            "<i>“Em economia aberta, o multiplicador dos gastos é 1/(1 − c − m).”</i> → ERRADO (sinal trocado: é "
            "1 − c + m)",
        ])],
        "reescrita": ("Abertura econômica tende a " + hl("reduzir") + " o multiplicador dos gastos do governo sobre "
                      "o produto da economia."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Maior abertura aumenta a propensão a importar, que reduz o multiplicador: parte da "
                            "renda vaza para importações. Y = [1/(1 − c + m)] × (C₀ + I + G + X).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 221", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (fórmula transcrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01310
    {
        "id": "ECO-E2-L01310-1", "fonte_ref": "E2-L01310", "destino": "26", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": ("Julgue o item a seguir, acerca dos fluxos internacionais de bens e capital em uma economia "
                    "aberta."),
        "rotulo_item": "Item",
        "assertiva": "As importações representam parte da renda gerada no país que “vaza” para o exterior.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As importações representam parte da renda gerada no país que <u>“vaza”</u> para o "
                      "exterior."),
        "poucas": ("No fluxo circular, " + azb("vazamento") + " é a renda recebida que não volta às empresas "
                   "nacionais como compra de bens domésticos: " + vd("poupança, impostos e importações") + "."),
        "destrinchando": [
            "Fluxo circular: as empresas pagam renda às famílias, que a devolvem comprando bens. Nem toda renda "
            "volta: uma parte é " + azb("poupada") + " (S), outra vai ao governo como " + azb("tributo") + " (T) e "
            "outra compra bens " + azb("importados") + " (M) — renda que remunera produtores estrangeiros.",
            "Do outro lado estão as " + azb("injeções") + ", gastos que não dependem da renda corrente das "
            "famílias: investimento (I), gasto do governo (G) e exportações (X).",
            "Equilíbrio keynesiano em economia aberta: " + vd("S + T + M = I + G + X") + " (vazamentos = "
            "injeções), versão expandida do S = I da economia fechada. Rearranjando: (S − I) + (T − G) = X − M — "
            "a identidade dos hiatos, que liga poupança privada, saldo fiscal e saldo externo.",
            "Consequência para o " + azb("multiplicador") + ": quanto mais a renda vaza a cada rodada, menor o "
            "efeito de uma injeção. Por isso a " + azb("propensão marginal a importar") + " (m) entra no "
            "denominador: k = 1/(1 − c + m).",
            vm("Regra-âncora: vazamentos = S, T, M; injeções = I, G, X."),
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição de manual; as aspas em “vaza” marcam o "
                       "termo técnico. Erraria quem associasse importação a “perda de divisas” ou a conta de "
                       "capital — o item fala só do fluxo de renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As exportações representam parte da renda gerada no país que vaza para o exterior.”</i> → ERRADO "
            "(exportação é injeção, não vazamento)",
            "<i>“No equilíbrio de uma economia aberta com governo, a soma de poupança, tributos e importações "
            "iguala a soma de investimento, gastos públicos e exportações.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Vazamentos são recursos que deixam de fluir para famílias e empresas: poupança, "
                            "impostos e importações.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01346
    {
        "id": "ECO-E2-L01346-1", "fonte_ref": "E2-L01346", "destino": "26", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": ("A publicação da obra A Teoria Geral do Emprego, do Juro e da Moeda, em 1936, por John Maynard "
                    "Keynes, foi fundamental para que os economistas se deparassem com duas das principais "
                    "abordagens acerca da relação entre investimento e poupança. As correntes do pensamento "
                    "econômico apresentam visões distintas sobre as relações entre o investimento (I) e a poupança "
                    "(S). Considerando o exposto, julgue o item seguinte."),
        "rotulo_item": "Item",
        "assertiva": ("De acordo com Keynes, a poupança era resultado do investimento. Ao estimular a demanda "
                      "agregada, o investimento induz um aumento na renda e na poupança."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com Keynes, a <u>poupança era resultado do investimento</u>. Ao estimular a "
                      "demanda agregada, o investimento induz um aumento na renda e na poupança."),
        "poucas": ("Em " + oc("Keynes") + ", a causalidade vai de " + vd("I → Y → S") + ": o investimento eleva a "
                   "renda pelo multiplicador, e a poupança, função da renda, cresce até igualar o investimento."),
        "destrinchando": [
            "Visão " + azb("clássica") + " (fundos emprestáveis): a poupança vem antes e financia o investimento; a "
            + azb("taxa de juros") + " é o preço que iguala S (oferta de fundos) e I (demanda). Mais poupança → "
            "juros menores → mais investimento.",
            "Visão de " + oc("Keynes") + ": poupança e consumo dependem da " + azb("renda") + " (S = −C₀ + sY), "
            "não dos juros. O investimento depende da eficiência marginal do capital e dos juros. Quando o "
            "investimento sobe, a renda cresce pelo multiplicador até que a poupança gerada iguale o novo "
            "investimento: " + vd("ΔS = s × ΔY = s × ΔI/s = ΔI") + ".",
            "Os juros, em Keynes, são fenômeno monetário: equilibram a " + azb("preferência pela liquidez") + " "
            "com a oferta de moeda, não a poupança com o investimento.",
            "Corolário famoso: o " + azb("paradoxo da parcimônia") + ". Se todos tentam poupar mais, o consumo cai, "
            "a renda cai e a poupança agregada final não aumenta (pode até cair, se o investimento depender da "
            "renda) — o que é virtude para o indivíduo vira problema para o agregado.",
            "Para o financiamento do investimento antes da renda gerada, os pós-keynesianos destacam o papel do "
            + azb("crédito") + " bancário (o “finance”): o banco cria o meio de pagamento, e a poupança aparece "
            "depois.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Reproduz a tese central, que contraria o "
                       "senso comum (“é preciso poupar para investir”). A pista é o verbo “induz”: a poupança é "
                       "consequência, e a banca cobra justamente essa inversão de causalidade."),
        "modulos": [("📚 Autores e teses", [
            "Clássicos/neoclássicos → poupança prévia financia o investimento; juros equilibram S e I.",
            oc("Keynes") + " (<i>Teoria Geral</i>, 1936) → o investimento determina a renda e, por ela, a poupança; "
            "juros são monetários (preferência pela liquidez).",
        ]), ("😈 Para dificultar", [
            "<i>“Para Keynes, um aumento da taxa de juros eleva a poupança e, por essa via, o investimento.”</i> → "
            "ERRADO (visão clássica dos fundos emprestáveis)",
            "<i>“Segundo o paradoxo da parcimônia, a tentativa de toda a sociedade de poupar mais pode reduzir a "
            "renda sem elevar a poupança agregada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Poupança e consumo são funções da renda em Keynes.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01349
    {
        "id": "ECO-E2-L01349-1", "fonte_ref": "E2-L01349", "destino": "26", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": "Em relação à teoria macroeconômica, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Segundo Keynes, o sistema econômico não pode estar em equilíbrio (com a oferta agregada igual "
                      "à demanda agregada) quando há desemprego involuntário da força de trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo Keynes, o sistema econômico ") + vm("não pode estar") + az(" em equilíbrio (com a "
                    "oferta agregada igual à demanda agregada) quando há desemprego involuntário da força de "
                    "trabalho.")),
        "poucas": ("A grande novidade de " + oc("Keynes") + " é justamente o " + azb("equilíbrio com desemprego "
                   "involuntário") + ": oferta e demanda agregadas se igualam num ponto (a demanda efetiva) que "
                   "pode ficar abaixo do pleno emprego."),
        "destrinchando": [
            "Equilíbrio, em Keynes, é a igualdade entre as funções de " + azb("oferta agregada") + " e de "
            + azb("demanda agregada") + " no mercado de bens: os empresários produzem exatamente o que esperam "
            "vender e não têm motivo para mudar a produção.",
            "Esse ponto define o emprego. Nada obriga que ele coincida com o pleno emprego: se consumo e "
            "investimento forem baixos, o equilíbrio se dá com gente querendo trabalhar ao salário vigente e sem "
            "vaga — " + azb("desemprego involuntário") + ". E a economia pode permanecer aí, porque não há força "
            "automática que a tire do lugar.",
            "Para os " + azb("clássicos") + ", ao contrário, equilíbrio implica pleno emprego: a flexibilidade de "
            "salários e juros e a " + azb("lei de Say") + " eliminariam qualquer excesso de oferta de trabalho; "
            "desemprego involuntário seria sinal de desequilíbrio passageiro.",
            "Por isso o título é <i>Teoria <b>Geral</b></i>: o pleno emprego clássico vira caso particular de uma "
            "teoria em que o equilíbrio pode estar em qualquer nível de emprego.",
            vm("Regra-âncora: em Keynes, equilíbrio não significa pleno emprego."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " Atribui a Keynes a tese clássica, negando "
                       "exatamente o que ele demonstrou. Pista: o parêntese define equilíbrio como OA = DA, que "
                       "é o critério keynesiano — e nesse critério cabe o desemprego."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Keynes, a economia pode permanecer em equilíbrio com desemprego involuntário, pois o "
            "nível de emprego depende da demanda efetiva.”</i> → CERTO",
            "<i>“Para os clássicos, o desemprego involuntário é compatível com o equilíbrio de longo prazo.”</i> → "
            "ERRADO (troca de escola: tese de Keynes)",
        ])],
        "reescrita": ("Segundo Keynes, o sistema econômico " + hl("pode estar") + " em equilíbrio (com a oferta "
                      "agregada igual à demanda agregada) quando há desemprego involuntário da força de trabalho."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["não pode"], "dificuldade": 1,
        "comentario_fonte": "Keynes mostrou a possibilidade de equilíbrio com desemprego involuntário; o emprego é "
                            "determinado pela demanda efetiva, independentemente do mercado de trabalho.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01480
    {
        "id": "ECO-E2-L01480-1", "fonte_ref": "E2-L01480", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_PANDEMIA,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria do multiplicador keynesiano, o impacto total, na renda agregada, do pagamento "
                      "do auxílio emergencial será positivo, mas menor que o valor do auxílio, visto que a propensão "
                      "a consumir é menor que 1."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a teoria do multiplicador keynesiano, o impacto total, na renda agregada, do "
                       "pagamento do auxílio emergencial será positivo") + vm(", mas menor que o valor do auxílio, "
                       "visto que a propensão a consumir é menor que 1") + az(".")),
        "poucas": ("PMgC menor que 1 é o que torna o multiplicador " + azb("finito") + ", não menor que 1. O "
                   "multiplicador das transferências é " + vd("c/(1 − c)") + ", que supera 1 sempre que "
                   + vd("c > 0,5") + " — caso típico das famílias pobres."),
        "destrinchando": [
            "Gasto do governo (G) entra inteiro na demanda: multiplicador " + vd("1/(1 − c)") + ". "
            + azb("Transferência") + " (auxílio) não é demanda; vira renda disponível, e só a fração c é gasta na "
            "1ª rodada. Multiplicador: " + vd("c/(1 − c)") + ", uma unidade menor que o do gasto direto.",
            "Contas: c = 0,8 → 0,8/0,2 = " + vd("4") + " (cada R$ 1 de auxílio gera R$ 4 de renda); c = 0,5 → "
            + vd("1") + "; só com c < 0,5 o impacto seria menor que o valor transferido. Famílias de baixa renda "
            "consomem quase tudo que recebem (c alto), o que torna o auxílio um estímulo forte.",
            "O raciocínio do item confunde a parcela gasta na 1ª rodada (c < 1) com o efeito total: cada rodada é "
            "menor que a anterior, mas a soma 1 + c + c² + … supera em muito a injeção inicial.",
            "Na prática, o efeito é menor que o do modelo simples: tributos, importações e juros (crowding out) "
            "reduzem o multiplicador. Ainda assim, as estimativas empíricas para transferências a famílias pobres "
            "costumam estar entre as mais altas dos instrumentos fiscais.",
            vm("Regra-âncora: c < 1 garante multiplicador finito; multiplicador maior que 1 depende de c."),
        ],
        "dissecando": (cz("[nexo indevido · inversão]") + " A premissa é verdadeira (c < 1) e o efeito "
                       "positivo também; o erro é o nexo: c < 1 não implica impacto menor que o auxílio. 🔥 Itens "
                       "de multiplicador gostam de usar uma condição verdadeira para tirar dela uma conclusão "
                       "que não decorre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O multiplicador das transferências é inferior ao dos gastos do governo em bens e serviços, pois "
            "parte da transferência é poupada já na primeira rodada.”</i> → CERTO",
            "<i>“Como a propensão a consumir é menor que 1, o multiplicador dos gastos do governo é inferior a "
            "1.”</i> → ERRADO (com 0 < c < 1, 1 ÷ PMgS é sempre maior que 1)",
        ])],
        "reescrita": ("Segundo a teoria do multiplicador keynesiano, o impacto total, na renda agregada, do pagamento "
                      "do auxílio emergencial será positivo" + hl(" e tende a superar o valor do auxílio, visto que "
                      "a propensão a consumir das famílias mais pobres é elevada (acima de 0,5)") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": ["mas", "visto que"], "dificuldade": 2,
        "comentario_fonte": "Multiplicador keynesiano maior que 1 com c > 0; impacto total maior que o auxílio. "
                            "Exemplo com 1/(1 − c) = 5 para c = 0,8; auxílio a famílias pobres, de alta PMgC, "
                            "tende a ter multiplicador maior.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 370", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 371", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (deslocamento da DA pelo multiplicador; não passa no teste do "
                                   "quadro-negro)"},
                          {"ref": "IMAGEM 372", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (fórmula no 📖)"},
                          {"ref": "IMAGEM 373", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": ["qualidade_fonte: os comentários de origem aplicam ao auxílio o multiplicador dos gastos, "
                    "1/(1 − c); para transferências é c/(1 − c), menor que 1 se c < 0,5 — o gabarito ERRADO se "
                    "mantém porque c < 1 não implica impacto menor que o auxílio",
                    "texto_corrigido: “auxilio” → “auxílio” na assertiva"],
    },
    # ------------------------------------------------------------------ E2-L01481
    {
        "id": "ECO-E2-L01481-1", "fonte_ref": "E2-L01481", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_PANDEMIA,
        "rotulo_item": "Item",
        "assertiva": ("O fato de os consumidores de baixa renda terem diversos itens importados em suas cestas de "
                      "consumo, por exemplo os eletrônicos comprados da China a preços mais baixos, tende a reduzir "
                      "o efeito de políticas fiscais expansionistas na renda doméstica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O fato de os consumidores de baixa renda terem diversos itens importados em suas cestas de "
                      "consumo, por exemplo os eletrônicos comprados da China a preços mais baixos, <u>tende a "
                      "reduzir</u> o efeito de políticas fiscais expansionistas na renda <u>doméstica</u>."),
        "poucas": ("Consumo de importados eleva a " + azb("propensão marginal a importar") + ": parte do "
                   "estímulo “vaza” para produtores estrangeiros, e o multiplicador doméstico, " + vd("1/(1 − c + m)")
                   + ", diminui."),
        "destrinchando": [
            "Cada real de auxílio gasto em eletrônico importado gera renda e emprego no país exportador, não no "
            "Brasil. Na cadeia do multiplicador, essa fração sai do " + azb("fluxo circular") + " doméstico — é um "
            + azb("vazamento") + ", como a poupança e os tributos.",
            "Em fórmula: com consumo c e propensão a importar m, o multiplicador dos gastos passa de 1/(1 − c) para "
            + vd("1/(1 − c + m)") + ". Exemplo: c = 0,8 e m = 0,2 → de 5 para " + vd("2,5") + ".",
            "Atenção ao objeto: o item fala da renda <b>doméstica</b>. O estímulo não se perde para a economia "
            "mundial — vira demanda na China —, e o consumidor brasileiro ganha bem-estar com produtos mais "
            "baratos. O que cai é o efeito sobre o PIB do país.",
            "O ponto vale para qualquer expansão fiscal, não só para transferências; mas pesa mais quando o "
            "público beneficiado tem cesta com muitos importados.",
            "Em economia aberta, a política fiscal ainda pode sofrer outro freio: no modelo de "
            + oc("Mundell-Fleming") + " com câmbio flutuante e mobilidade de capitais, a apreciação cambial "
            "derruba as exportações líquidas.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Traduz o conceito de vazamento por "
                       "importações para um exemplo concreto. O “tende a” protege o item, e “renda doméstica” "
                       "delimita o efeito. O contexto da pandemia é só moldura."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O consumo de bens importados pelas famílias beneficiadas anula o efeito da política fiscal "
            "expansionista sobre a renda doméstica.”</i> → ERRADO (modulador absoluto: reduz, não anula)",
            "<i>“Quanto maior a propensão marginal a importar, menor o multiplicador dos gastos do governo.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Importações geram vazamentos da renda para o exterior e reduzem o multiplicador fiscal "
                            "doméstico; quanto maior a PMgM, menor o multiplicador.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 374", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": ["quase_duplicata: ECO-E2-L01243-1 (abertura comercial reduz o multiplicador)"],
    },
    # ------------------------------------------------------------------ E3-L00172
    {
        "id": "ECO-E3-L00172-1", "fonte_ref": "E3-L00172", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "A partir da teoria macroeconômica, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo keynesiano simples, o efeito de um aumento dos gastos do governo sobre o produto "
                      "será tão maior quanto maior for a propensão marginal a consumir."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um modelo keynesiano simples, o efeito de um aumento dos gastos do governo sobre o produto "
                      "será <u>tão maior quanto maior</u> for a propensão marginal a consumir."),
        "poucas": ("ΔY = ΔG × " + vd("1/(1 − c)") + ": quanto maior c, menor o denominador e maior o "
                   + azb("multiplicador") + "."),
        "destrinchando": [
            "Modelo keynesiano simples: Y = C + I + G, com C = C₀ + cY (ou c(Y − T) com tributo fixo). "
            "Equilíbrio: Y = (C₀ + I + G)/(1 − c). Daí " + vd("ΔY/ΔG = 1/(1 − c)") + ".",
            "Tabela de bolso: c = 0,5 → " + vd("2") + "; c = 0,75 → " + vd("4") + "; c = 0,8 → " + vd("5")
            + "; c = 0,9 → " + vd("10") + ". O multiplicador cresce cada vez mais rápido quando c se aproxima de 1.",
            "Mecanismo: o gasto do governo vira renda; a renda induz consumo; o consumo vira renda de novo. Com "
            "c = 0,8 e ΔG = 100: 100 + 80 + 64 + 51,2 + … = 500. O que freia a cadeia é a " + azb("propensão "
            "marginal a poupar") + " (1 − c).",
            "Com tributação proporcional (alíquota t), o multiplicador vira 1/[1 − c(1 − t)]: impostos também "
            "freiam a cadeia. Mas a relação com c continua a mesma — mais consumo, mais multiplicador.",
            "Atenção: o tamanho do gasto não altera o multiplicador; ele apenas é multiplicado por ele. E a "
            "propensão é <b>marginal</b> (fração de cada real adicional consumida), não o consumo em nível.",
        ],
        "dissecando": (cz("[literalidade]") + " Enunciado de manual com a estrutura “tão maior quanto maior”, "
                       "que a CEBRASPE usa para cobrar relações diretas. Bastaria trocar “consumir” por “poupar” "
                       "para inverter o gabarito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…será tão maior quanto maior for a propensão marginal a poupar.”</i> → ERRADO (inversão: PMgS "
            "maior reduz o multiplicador)",
            "<i>“…será tão maior quanto maior for a alíquota do imposto de renda.”</i> → ERRADO (tributo "
            "proporcional é vazamento e reduz o multiplicador)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["tão maior quanto maior"], "dificuldade": 1,
        "comentario_fonte": "Multiplicador 1/(1 − c): maior c, menor denominador, maior multiplicador. Exemplos "
                            "c = 0,5 → 2 e c = 0,8 → 5; propensão a consumir é proporcional, não absoluta; "
                            "tributação reduz o multiplicador.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 211", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (anotação manuscrita ilegível; dedução absorvida no 📖)"},
                          {"ref": "IMAGEM 212", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"},
                          {"ref": "IMAGEM 213", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida no 📖"}],
        "alertas": ["quase_duplicata: ECO-E2-L00837-1 (multiplicador maior com PMgC maior)"],
    },
    # ------------------------------------------------------------------ E3-L00275
    {
        "id": "ECO-E3-L00275-1", "fonte_ref": "E3-L00275", "destino": "26", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Na década de 30, durante a Grande Depressão, a teoria econômica debatia, entre outros temas, os "
                    "determinantes do emprego agregado. A respeito desse debate, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Conforme Keynes, o nível de emprego agregado não se define meramente como um ponto de "
                      "equilíbrio parcial, dado no encontro de curvas agregadas de oferta e de demanda por trabalho. "
                      "Para ele, em uma dada estrutura produtiva, o nível de emprego resulta da decisão dos "
                      "empresários de empregar a força de trabalho em função das expectativas de consumo e de "
                      "investimento na economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Conforme Keynes, o nível de emprego agregado <u>não se define meramente</u> como um ponto de "
                      "equilíbrio parcial, dado no encontro de curvas agregadas de oferta e de demanda por trabalho. "
                      "Para ele, em uma dada estrutura produtiva, o nível de emprego resulta da <u>decisão dos "
                      "empresários</u> de empregar a força de trabalho em função das <u>expectativas</u> de consumo "
                      "e de investimento na economia."),
        "poucas": ("É o " + azb("princípio da demanda efetiva") + ": em " + oc("Keynes") + ", o emprego é decidido "
                   "pelos empresários conforme as vendas que esperam (consumo + investimento), e não no mercado de "
                   "trabalho."),
        "destrinchando": [
            "Visão " + azb("clássica") + ": o emprego sai do mercado de trabalho — a demanda por trabalho é a "
            "produtividade marginal; a oferta, a desutilidade do trabalho; o salário real flexível equilibra as "
            "duas. Desemprego persistente seria salário real alto demais.",
            "Ruptura de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936): o mercado de trabalho não determina "
            "sozinho o emprego. Os empresários, numa dada estrutura produtiva (capital, técnica), contratam o que "
            "é preciso para produzir o que esperam vender. A " + azb("demanda efetiva") + " — consumo, que depende "
            "da renda e da propensão a consumir, mais investimento, que depende da eficiência marginal do capital "
            "e dos juros — fixa o emprego.",
            "As " + azb("expectativas") + " são centrais: de curto prazo (vendas próximas, que guiam a produção) e "
            "de longo prazo (retorno de novos investimentos, sujeitas à incerteza e ao " + azb("<i>animal "
            "spirits</i>") + ").",
            "Daí o " + azb("desemprego involuntário") + " de equilíbrio: com demanda insuficiente, mesmo "
            "trabalhadores dispostos a aceitar o salário vigente não são contratados, e cortar salários não "
            "resolve.",
            "O “meramente” é importante: Keynes não nega a existência de oferta e demanda por trabalho, nega que "
            "esse encontro, isolado, determine o emprego agregado.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Reescreve com cuidado a tese da demanda efetiva. Os "
                       "moduladores “meramente” e “em uma dada estrutura produtiva” deixam o item preciso. Um "
                       "candidato apressado pode ver no 1º período uma negação absurda do mercado de trabalho."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Keynes, o nível de emprego agregado é determinado pelo equilíbrio entre oferta e demanda "
            "por trabalho, ajustado pela flexibilidade do salário real.”</i> → ERRADO (visão clássica)",
            "<i>“Para Keynes, a redução dos salários nominais seria suficiente para restabelecer o pleno "
            "emprego.”</i> → ERRADO (tese clássica: Keynes a rejeita)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["meramente"], "dificuldade": 2,
        "comentario_fonte": "Teoria da demanda efetiva: o emprego é determinado no mercado de bens pela expectativa "
                            "de demanda (C + I), não no mercado de trabalho; explica o desemprego involuntário.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0318
    {
        "id": "ECO-E1-0318-1", "fonte_ref": "E1-0318", "destino": "27", "subtema": H2["lm"],
        "tipo": "C/E", "banca": "IADES", "prova": "IRBr/CACD/2020", "ano": 2020, "cacd": True, "errei": True,
        "comando": "Acerca desse tema, no que se refere à moeda e à política monetária, julgue o item a seguir.",
        "excerto": ("<p><i>No início da pandemia do Sars-CoV-2 (novo Coronavírus), o Comitê de Política Monetária "
                    "(COPOM), órgão do Banco Central, reduziu algumas vezes a taxa básica de juros da economia, a "
                    "Selic. Essa taxa é um importante indicador para a economia como um todo e reflete a principal "
                    "articulação da política monetária no Brasil.</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("As quedas da taxa de juros descritas no enunciado são resultados de um deslocamento da curva "
                      "Liquidity Money (LM) para cima e para a esquerda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As quedas da taxa de juros descritas no enunciado são resultados de um deslocamento da curva "
                       "Liquidity Money (LM) para ") + vm("cima e para a esquerda") + az(".")),
        "poucas": ("Corte de juros pela autoridade monetária = " + azb("expansão monetária") + ": a LM se desloca "
                   "para " + vd("baixo e para a direita") + ", com juros menores para cada nível de renda."),
        "destrinchando": [
            "A " + azb("LM") + " reúne as combinações (Y, i) que equilibram o mercado monetário: demanda por moeda "
            "L(Y, i) = oferta real M/P. Para manter a Selic mais baixa, o " + rx("Banco Central") + " supre a "
            "liquidez que o mercado demanda a esse juro — na prática, amplia a oferta de moeda (compra títulos em "
            "operações compromissadas).",
            "Mais moeda com a mesma demanda: para cada nível de renda, o juro que equilibra o mercado monetário é "
            "menor → a LM desce, ou, o que dá no mesmo, vai para a " + vd("direita") + " (para cada juro, comporta "
            "renda maior).",
            "Novo equilíbrio IS-LM: " + vd("i ↓ e Y ↑") + ", pelo estímulo ao investimento e ao consumo. "
            "Deslocamento para cima/esquerda corresponde ao oposto: contração monetária (venda de títulos, alta "
            "do compulsório), com juros maiores.",
            "Curiosidade terminológica: “LM” vem de <i>Liquidity preference</i> (demanda por moeda, L) e "
            "<i>Money supply</i> (oferta de moeda, M), na formulação de " + oc("Hicks") + " (1937). “Liquidity "
            "Money” não é o nome técnico, mas não altera o julgamento.",
            "Contexto: em 2020 o COPOM levou a Selic à mínima histórica de " + vd("2% a.a.")
            + " (agosto de 2020); a partir de 2021, com a inflação em alta, iniciou um longo ciclo de aperto.",
            vm("Regra-âncora: expansão monetária → LM para baixo/direita; contração → para cima/esquerda."),
        ],
        "grafico_verso": "ECO-E1-0318-1-V1",
        "dissecando": (cz("[inversão]") + " Troca o sentido do deslocamento. 🔥 Em IS-LM, a banca alterna "
                       "“direita e para baixo” × “esquerda e para cima” e conta com o candidato que lembra que "
                       "“algo se moveu”, mas não para onde. Atalho: juro cai → LM desce."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As quedas da taxa de juros descritas são compatíveis com um deslocamento da curva LM para baixo "
            "e para a direita, com elevação da renda de equilíbrio.”</i> → CERTO",
            "<i>“As quedas da taxa de juros descritas resultam de um deslocamento da curva IS para a direita.”</i> "
            "→ ERRADO (curva trocada: IS à direita eleva os juros)",
        ])],
        "reescrita": ("As quedas da taxa de juros descritas no enunciado são resultados de um deslocamento da curva "
                      "Liquidity Money (LM) para " + hl("baixo e para a direita") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Expansão monetária desloca a LM para a direita e para baixo; para dado nível de renda, "
                            "juros menores.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0469
    {
        "id": "ECO-E1-0469-1", "fonte_ref": "E1-0469", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Nidi/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM, a partir do ponto de equilíbrio, uma política econômica de aumento dos "
                      "impostos desloca a curva IS para a esquerda, resultando em uma queda da taxa de juros e um "
                      "crescimento da renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo IS-LM, a partir do ponto de equilíbrio, uma política econômica de aumento dos "
                       "impostos desloca a curva IS para a esquerda, resultando em uma queda da taxa de juros e ")
                    + vm("um crescimento") + az(" da renda.")),
        "poucas": ("Alta de impostos é " + azb("política fiscal contracionista") + ": a IS vai para a esquerda e, "
                   "com a LM fixa, " + vd("juros e renda caem juntos") + "."),
        "destrinchando": [
            "Mais imposto → menos renda disponível → menos consumo → menor demanda agregada para cada juro: a "
            + azb("IS") + " se desloca para a " + vd("esquerda") + ". (Esse trecho do item está certo.)",
            "Com a renda menor, cai a " + azb("demanda por moeda para transações") + ". Como a oferta de moeda não "
            "mudou, sobra moeda ao juro antigo e o juro de equilíbrio cai — movimento <b>ao longo</b> da LM, para "
            "baixo. (Também certo.)",
            "Mas a renda não cresce: o novo equilíbrio está à esquerda do antigo. A queda dos juros estimula um "
            "pouco o investimento e amortece a contração (" + azb("crowding in") + " parcial), sem revertê-la.",
            "Regra de leitura: deslocamento da IS move juros e renda no " + vd("mesmo sentido") + "; deslocamento "
            "da LM move juros e renda em " + vd("sentidos opostos") + ". IS esquerda → i↓ e Y↓.",
            "Exceções: com LM vertical (caso clássico), a renda não cai e só os juros caem; com LM horizontal "
            "(armadilha da liquidez), a renda cai pelo multiplicador inteiro e os juros ficam parados.",
        ],
        "grafico_verso": "ECO-E1-0469-1-V1",
        "dissecando": (cz("[meia-verdade]") + " Duas afirmações certas (IS à esquerda, juros caem) e uma falsa "
                       "colada no fim. Quem lembra que juro baixo estimula a economia aceita o “crescimento da "
                       "renda”; mas o juro caiu <b>porque</b> a renda caiu."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política de redução dos gastos públicos desloca a IS para a esquerda, reduzindo a renda e a "
            "taxa de juros de equilíbrio.”</i> → CERTO",
            "<i>“…o aumento dos impostos desloca a curva LM para a esquerda, elevando a taxa de juros.”</i> → "
            "ERRADO (curva trocada: tributo mexe na IS)",
        ])],
        "reescrita": ("No modelo IS-LM, a partir do ponto de equilíbrio, uma política econômica de aumento dos "
                      "impostos desloca a curva IS para a esquerda, resultando em uma queda da taxa de juros e "
                      + hl("uma queda") + " da renda."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Política fiscal contracionista: IS à esquerda; menor renda reduz a demanda por "
                            "liquidez e os juros caem. O verso reproduz o enunciado sem destacar que a renda cai.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [FIG_PERDIDA("image (156).png")],
        "alertas": ["qualidade_fonte: o comentário de origem atribui a queda dos juros a uma intenção de “aquecer "
                    "a economia”; no IS-LM ela decorre da menor demanda por moeda, e a renda cai"],
    },
    # ------------------------------------------------------------------ E1-0470
    {
        "id": "ECO-E1-0470-1", "fonte_ref": "E1-0470", "destino": "27", "subtema": H2["lm"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "No escopo da economia monetária, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No escopo da Economia Monetária, a chamada relação LM sustenta que a taxa de juros deve ser "
                      "tal que, dado certo nível de renda, as pessoas estejam dispostas a ter um montante de moeda "
                      "igual à oferta de moeda existente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No escopo da Economia Monetária, a chamada relação LM sustenta que a taxa de juros deve ser "
                      "tal que, <u>dado certo nível de renda</u>, as pessoas estejam dispostas a ter um montante de "
                      "moeda <u>igual à oferta de moeda existente</u>."),
        "poucas": ("A " + azb("LM") + " é o lugar das combinações (Y, i) em que a " + azb("demanda por moeda")
                   + " iguala a " + azb("oferta real de moeda") + ": dada a renda, o juro se ajusta até o público "
                   "querer reter exatamente a moeda existente."),
        "destrinchando": [
            "Equação: " + vd("M/P = L(Y, i)") + ", com L crescente em Y (motivo transação e precaução) e "
            "decrescente em i (motivo especulação / custo de oportunidade de reter moeda).",
            "Lógica do item: fixe Y. Se o juro estivesse alto demais, o público quereria menos moeda do que a "
            "existente e compraria títulos, elevando seu preço e derrubando o juro; se estivesse baixo demais, "
            "ocorreria o contrário. O juro de equilíbrio é aquele em que a moeda demandada iguala a ofertada.",
            "Por que a LM é positivamente inclinada: renda maior → mais demanda por moeda para transações → com "
            "oferta fixa, só um juro maior reduz a demanda especulativa e restabelece o equilíbrio.",
            "Inclinação: quanto mais sensível a demanda por moeda aos juros, mais " + azb("horizontal") + " a LM "
            "(no limite, armadilha da liquidez); quanto menos sensível, mais " + azb("vertical") + " (caso "
            "clássico, TQM).",
            "Deslocamentos: ↑M (ou ↓P) → LM para a direita/baixo; ↓M (ou ↑P) → esquerda/cima.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Descreve a LM em linguagem corrente, sem fórmula. O item seria "
                       "ERRADO se atribuísse à LM o equilíbrio entre poupança e investimento, que é a IS — a "
                       "troca mais frequente nas provas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A relação LM sustenta que a taxa de juros é tal que, dado certo nível de renda, a poupança "
            "iguala o investimento.”</i> → ERRADO (troca de curva: isso é a IS)",
            "<i>“Ao longo da curva LM, um nível de renda mais alto está associado a uma taxa de juros mais "
            "alta.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A LM representa os pares (renda, juros) que equilibram o mercado monetário: demanda "
                            "por moeda (transação e especulação) igual à oferta real.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0471
    {
        "id": "ECO-E1-0471-1", "fonte_ref": "E1-0471", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EFIC_MON,
        "rotulo_item": "Item",
        "assertiva": ("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, o aumento da oferta de "
                      "moeda, mantendo os demais parâmetros constantes, em uma conformação econômica de baixa "
                      "elasticidade-juros do investimento, apresenta baixa eficácia da política, se comparada a uma "
                      "conformação em que a elasticidade-juros do investimento é alta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, o aumento da oferta de "
                      "moeda, mantendo os demais parâmetros constantes, em uma conformação econômica de <u>baixa "
                      "elasticidade-juros do investimento</u>, apresenta <u>baixa eficácia</u> da política, se "
                      "comparada a uma conformação em que a elasticidade-juros do investimento é alta."),
        "poucas": ("A política monetária age " + azb("via juros → investimento") + ". Se o investimento quase não "
                   "reage aos juros (IS íngreme), a queda do juro mexe pouco na renda: eficácia baixa."),
        "destrinchando": [
            "Canal de transmissão no IS-LM: ↑M → LM para a direita → " + vd("i ↓") + " → " + vd("I ↑") + " → "
            "multiplicador → " + vd("Y ↑") + ". O elo crítico é a resposta do investimento ao juro.",
            "Elasticidade-juros do investimento " + azb("baixa") + " → a IS é muito inclinada (quase vertical): a "
            "LM desliza para baixo, o juro cai bastante, mas a renda avança pouco.",
            "Elasticidade " + azb("alta") + " → a IS é pouco inclinada (plana): pequena queda do juro gera muito "
            "investimento, e a renda sobe muito — política monetária potente.",
            "Do lado da LM, o efeito é o inverso do da fiscal: a monetária é mais eficaz quanto <b>menos</b> "
            "sensível aos juros for a demanda por moeda (LM íngreme). Resumo: monetária forte = IS plana + LM "
            "íngreme; fiscal forte = IS íngreme + LM plana.",
            "Limites: IS vertical (investimento totalmente insensível) → monetária ineficaz; LM horizontal "
            "(armadilha da liquidez) → monetária ineficaz por outro motivo (o juro não cai).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item é longo e comparativo, mas a estrutura é simples: baixa "
                       "sensibilidade → baixa eficácia. O “mantendo os demais parâmetros constantes” isola a "
                       "inclinação da IS. A banca costuma trocar “baixa” por “alta” para fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…em uma conformação de baixa elasticidade-juros do investimento, a política monetária apresenta "
            "alta eficácia.”</i> → ERRADO (inversão: eficácia baixa)",
            "<i>“…a política monetária é tanto mais eficaz quanto menor for a elasticidade-juros da demanda por "
            "moeda.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["se comparada"], "dificuldade": 2,
        "comentario_fonte": "Investimento pouco sensível aos juros limita o efeito da política monetária sobre a "
                            "renda; com alta sensibilidade, a política é mais eficaz.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0477-1 (mesma relação, versão ERRADA)"],
    },
    # ------------------------------------------------------------------ E1-0472
    {
        "id": "ECO-E1-0472-1", "fonte_ref": "E1-0472", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EFIC_MON,
        "rotulo_item": "Item",
        "assertiva": ("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, a eficácia da política "
                      "independe da inclinação das curvas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, a eficácia da política ")
                    + vm("independe") + az(" da inclinação das curvas.")),
        "poucas": ("A eficácia da política monetária depende " + azb("das duas inclinações") + ": é maior com IS "
                   "plana (investimento sensível aos juros) e LM íngreme (demanda por moeda pouco sensível)."),
        "destrinchando": [
            "Uma expansão monetária desloca a LM para a direita. Quanto disso vira renda depende de onde a nova "
            "LM corta a IS — ou seja, das inclinações.",
            azb("Inclinação da IS") + " (sensibilidade do investimento aos juros): IS plana → a queda do juro "
            "gera muito investimento → " + vd("ΔY grande") + "; IS íngreme → " + vd("ΔY pequeno") + "; IS "
            "vertical → ΔY nulo.",
            azb("Inclinação da LM") + " (sensibilidade da demanda por moeda aos juros): LM íngreme → a moeda nova "
            "precisa de muita queda de juro para ser absorvida → efeito forte; LM plana → a moeda é retida "
            "(entesourada) com pouca queda do juro → efeito fraco; LM horizontal (armadilha da liquidez) → "
            "efeito nulo.",
            "Em fórmula (IS-LM linear, com I = I₀ − b·i e demanda por moeda kY − h·i), o efeito da política "
            "monetária é ΔY/Δ(M/P) = " + vd("b ÷ [h(1 − c) + b·k]") + " — cresce com b (sensibilidade do "
            "investimento aos juros) e cai com h (sensibilidade da demanda por moeda aos juros).",
            "Os casos extremos (clássico × keynesiano) são justamente comparações de inclinações: o debate "
            "monetaristas × keynesianos dos anos 1960 foi, em boa parte, sobre o tamanho de b e h.",
            vm("Regra-âncora: monetária forte = IS plana + LM íngreme; fiscal forte = IS íngreme + LM plana."),
        ],
        "grafico_verso": "ECO-E1-0472-1-V1",
        "dissecando": (cz("[contradição · modulador absoluto]") + " Nega a variável que decide o resultado. "
                       "“Independe” em item de IS-LM é quase sempre sinal de erro: todo o capítulo de eficácia "
                       "relativa é sobre inclinações."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A eficácia da política monetária é tanto maior quanto mais horizontal for a curva IS.”</i> → "
            "CERTO",
            "<i>“A eficácia da política monetária é tanto maior quanto mais horizontal for a curva LM.”</i> → "
            "ERRADO (inversão: LM plana enfraquece a monetária)",
        ])],
        "reescrita": ("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, a eficácia da política "
                      + hl("depende") + " da inclinação das curvas."),
        "tipo_erro": ["CONTRADICAO", "GENERALIZACAO"], "moduladores": ["independe"], "dificuldade": 1,
        "comentario_fonte": "A inclinação das curvas IS e LM afeta diretamente a eficácia da política monetária; "
                            "curvas mais inclinadas reduzem o impacto sobre a renda.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [FIG_PERDIDA("Untitled (96).jpeg"), FIG_PERDIDA("Untitled (94).jpeg")],
        "alertas": ["qualidade_fonte: o comentário de origem diz que curvas mais inclinadas reduzem a eficácia; "
                    "isso vale para a IS, mas LM mais inclinada aumenta a eficácia da política monetária"],
    },
    # ------------------------------------------------------------------ E1-0473
    {
        "id": "ECO-E1-0473-1", "fonte_ref": "E1-0473", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EFIC_MON,
        "rotulo_item": "Item",
        "assertiva": ("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, para uma curva IS "
                      "vertical teremos a maior eficácia possível, para este tipo de política, no caso de um aumento "
                      "da oferta de moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, para uma curva IS "
                       "vertical teremos ") + vm("a maior eficácia possível") + az(", para este tipo de política, no "
                       "caso de um aumento da oferta de moeda.")),
        "poucas": ("IS vertical = investimento " + azb("insensível aos juros") + ": a expansão monetária derruba o "
                   "juro, mas a renda não se move. Eficácia " + vd("nula") + ", não máxima."),
        "destrinchando": [
            "A IS fica vertical quando a demanda agregada não depende dos juros — tipicamente, " + azb("investimento "
            "com elasticidade-juros zero") + " (empresários pessimistas, capacidade ociosa, crise de "
            "expectativas, a “armadilha do investimento”).",
            "Política monetária expansionista: ↑M → LM para a direita → o juro cai ao longo da IS vertical. Como "
            "o investimento não reage, a demanda não aumenta e " + vd("Y fica parado") + ".",
            "Política fiscal no mesmo cenário: desloca a IS vertical para a direita, e a renda sobe o "
            "multiplicador inteiro; os juros sobem, mas não há " + azb("crowding out") + ", porque o investimento "
            "não reage a eles. Eficácia fiscal máxima.",
            "A eficácia máxima da monetária está no caso oposto: " + azb("IS horizontal") + " (investimento "
            "infinitamente sensível aos juros) ou " + azb("LM vertical") + " (caso clássico).",
            vm("Regra-âncora: IS vertical → monetária nula, fiscal máxima; LM vertical → monetária máxima, fiscal "
               "nula."),
        ],
        "grafico_verso": "ECO-E1-0473-1-V1",
        "dissecando": (cz("[inversão]") + " Troca o polo do caso extremo: atribui à IS vertical o resultado da "
                       "IS horizontal (ou da LM vertical). 🔥 Os casos-limite costumam vir em bateria — vale "
                       "memorizar a tabela de quatro casas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para uma curva IS vertical, um aumento da oferta de moeda reduz a taxa de juros sem alterar a "
            "renda.”</i> → CERTO",
            "<i>“Para uma curva IS vertical, a política fiscal expansionista é totalmente ineficaz.”</i> → ERRADO "
            "(inversão: eficácia fiscal máxima)",
        ])],
        "reescrita": ("Dentro do modelo IS-LM, no tocante à eficácia da política monetária, para uma curva IS "
                      "vertical teremos " + hl("eficácia nula") + ", para este tipo de política, no caso de um "
                      "aumento da oferta de moeda."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["maior eficácia possível"], "dificuldade": 1,
        "comentario_fonte": "IS vertical: investimento não responde aos juros; política monetária ineficaz — o "
                            "juro cai, a renda não muda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0474
    {
        "id": "ECO-E1-0474-1", "fonte_ref": "E1-0474", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": "No modelo IS-LM, o máximo efeito-deslocamento ocorre quando a curva LM é horizontal.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo IS-LM, o ") + vm("máximo") + az(" efeito-deslocamento ocorre quando a curva LM é "
                                                                    "horizontal.")),
        "poucas": ("Com LM " + azb("horizontal") + " os juros não sobem quando a IS se desloca: o "
                   + azb("efeito-deslocamento") + " (crowding out) é " + vd("nulo") + ". O máximo ocorre com a LM "
                   "vertical."),
        "destrinchando": [
            azb("Efeito-deslocamento") + " (<i>crowding out</i>): a expansão fiscal eleva a renda e a demanda por "
            "moeda; com oferta de moeda fixa, os juros sobem e expulsam parte do investimento privado. O tamanho "
            "dele depende de quanto o juro sobe.",
            "LM " + azb("horizontal") + " (armadilha da liquidez): a demanda por moeda é infinitamente elástica "
            "aos juros; a moeda adicional demandada é suprida sem alta de juro. " + vd("Crowding out nulo") + ", "
            "e a renda sobe o multiplicador keynesiano inteiro.",
            "LM " + azb("vertical") + " (caso clássico): a demanda por moeda não depende dos juros, a renda não "
            "pode subir sem mais moeda, e o juro sobe até que o investimento caia exatamente o que o governo "
            "gastou. " + vd("Crowding out total") + " — a política fiscal só muda a composição do produto.",
            "Casos intermediários (LM positivamente inclinada): crowding out parcial, maior quanto mais íngreme a "
            "LM e quanto mais sensível o investimento aos juros (IS plana).",
            vm("Regra-âncora: LM horizontal → crowding out zero; LM vertical → crowding out total."),
        ],
        "grafico_verso": "ECO-E1-0474-1-V1",
        "dissecando": (cz("[inversão]") + " Inverte os polos: atribui à LM horizontal o resultado da LM vertical. "
                       "Quem associa “horizontal” a “plano, sem efeito” troca os casos; o critério é o juro — se "
                       "ele não sobe, não há o que deslocar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo IS-LM, o efeito-deslocamento é total quando a curva LM é vertical.”</i> → CERTO",
            "<i>“O efeito-deslocamento é tanto maior quanto mais elástica aos juros for a demanda por moeda.”</i> "
            "→ ERRADO (inversão: demanda por moeda elástica = LM plana = menos crowding out)",
        ])],
        "reescrita": ("No modelo IS-LM, o " + hl("mínimo (nulo)") + " efeito-deslocamento ocorre quando a curva LM é "
                      "horizontal."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["máximo"], "dificuldade": 1,
        "comentario_fonte": "Crowding out é a redução do investimento privado pela alta dos juros após expansão "
                            "fiscal; com LM horizontal o juro não sobe e o efeito é mínimo ou nulo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_PERDIDA("Untitled (92).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0475
    {
        "id": "ECO-E1-0475-1", "fonte_ref": "E1-0475", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM, um caso limite é dado pela armadilha da liquidez, em que é máxima a eficácia "
                      "da política fiscal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo IS-LM, um caso limite é dado pela armadilha da liquidez, em que é <u>máxima</u> a "
                      "eficácia da política <u>fiscal</u>."),
        "poucas": ("Na " + azb("armadilha da liquidez") + " a LM é horizontal: a expansão fiscal eleva a renda sem "
                   "elevar os juros — sem " + azb("crowding out") + ", eficácia máxima."),
        "destrinchando": [
            "Armadilha da liquidez: juros tão baixos que todos esperam que subam (e que os títulos percam valor). "
            "A demanda por moeda fica " + azb("infinitamente elástica") + " aos juros: toda moeda adicional é "
            "retida, e a LM fica horizontal.",
            "Política fiscal: a IS se desloca ao longo da LM plana. Os juros não sobem, o investimento privado não "
            "é expulso, e a renda aumenta pelo " + azb("multiplicador keynesiano") + " completo, 1/(1 − c) no "
            "modelo simples.",
            "Política monetária: ineficaz. Mais moeda não reduz um juro que já não cai; a LM “se desloca sobre si "
            "mesma” no trecho plano.",
            "Origem: " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) descreveu a possibilidade; o nome e a "
            "formalização vieram com o IS-LM de " + oc("Hicks") + " (1937). " + oc("Krugman") + " recuperou o "
            "conceito para o Japão dos anos 1990 e para o pós-2008, com juros perto de zero.",
            "Outro caso de eficácia fiscal máxima: IS vertical (investimento insensível aos juros), em que os "
            "juros sobem mas não expulsam investimento.",
        ],
        "dissecando": (cz("[literalidade]") + " Afirmação de manual. A troca típica para o ERRADO é “fiscal” → "
                       "“monetária”. O “caso limite” confirma que se fala do extremo da LM horizontal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na armadilha da liquidez, é máxima a eficácia da política monetária.”</i> → ERRADO (troca de "
            "política: a monetária é ineficaz)",
            "<i>“Na armadilha da liquidez, a política fiscal expansionista não provoca efeito-deslocamento sobre o "
            "investimento privado.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["máxima"], "dificuldade": 1,
        "comentario_fonte": "LM horizontal: monetária não afeta a renda; fiscal totalmente eficaz, renda sobe com "
                            "juro constante.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0480-1 (armadilha da liquidez: fiscal preferível)"],
    },
    # ------------------------------------------------------------------ E1-0476
    {
        "id": "ECO-E1-0476-1", "fonte_ref": "E1-0476", "destino": "27", "subtema": H2["is"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM, a situação caracterizada por uma baixa sensibilidade-juros do investimento "
                      "indica uma curva IS mais próxima da vertical."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo IS-LM, a situação caracterizada por uma <u>baixa</u> sensibilidade-juros do "
                      "investimento indica uma curva IS <u>mais próxima da vertical</u>."),
        "poucas": ("Se o investimento reage pouco aos juros, uma grande variação de i muda pouco a demanda e a "
                   "renda: a " + azb("IS") + " fica " + vd("íngreme") + " (no limite, vertical)."),
        "destrinchando": [
            "A " + azb("IS") + " reúne os pares (Y, i) que equilibram o mercado de bens (I = S, ou Y = C + I + G). "
            "É negativamente inclinada: juro menor → mais investimento → mais renda.",
            "Em forma linear, com I = I₀ − b·i: Y = k(A − b·i), em que k é o multiplicador e A os gastos "
            "autônomos. A inclinação (no gráfico i × Y) é " + vd("−1/(k·b)") + ". Com b pequeno, a inclinação "
            "é grande em módulo: IS íngreme. Com " + vd("b = 0") + ", IS vertical.",
            "O multiplicador também pesa: multiplicador maior (c alto) deixa a IS mais plana, porque a mesma "
            "variação do investimento gera mais renda.",
            "Consequências de política: IS íngreme → política monetária fraca (o juro cai, o investimento não "
            "reage) e política fiscal forte (pouco crowding out, já que a alta do juro quase não expulsa "
            "investimento).",
            vm("Regra-âncora: menos sensibilidade do investimento aos juros → IS mais vertical."),
        ],
        "dissecando": (cz("[literalidade]") + " Relação direta de manual. A banca inverte com “mais próxima da "
                       "horizontal” — e quem confunde as sensibilidades da IS (investimento) com as da LM "
                       "(demanda por moeda) cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma baixa sensibilidade-juros do investimento torna a curva IS mais horizontal.”</i> → ERRADO "
            "(inversão: torna-a mais vertical)",
            "<i>“Uma baixa sensibilidade-juros da demanda por moeda torna a curva LM mais próxima da "
            "vertical.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["mais próxima"], "dificuldade": 1,
        "comentario_fonte": "Investimento pouco sensível ao juro: IS mais inclinada, próxima da vertical.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_PERDIDA("Untitled (95).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0477
    {
        "id": "ECO-E1-0477-1", "fonte_ref": "E1-0477", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM, a situação caracterizada por uma baixa sensibilidade-juros do investimento "
                      "indica uma alta eficácia da política monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo IS-LM, a situação caracterizada por uma baixa sensibilidade-juros do investimento "
                       "indica uma ") + vm("alta") + az(" eficácia da política monetária.")),
        "poucas": ("A política monetária só chega à renda se o investimento reagir aos juros. Com " + azb("baixa "
                   "sensibilidade") + ", a IS é íngreme e a eficácia monetária é " + vd("baixa") + "."),
        "destrinchando": [
            "Cadeia da política monetária: ↑M → " + vd("i ↓") + " → " + vd("I ↑") + " → multiplicador → "
            + vd("Y ↑") + ". Se o segundo elo é fraco (investimento pouco sensível), a cadeia se rompe: o juro "
            "cai, mas a renda quase não muda.",
            "Graficamente: baixa sensibilidade → " + azb("IS quase vertical") + ". O deslocamento da LM para a "
            "direita escorrega pela IS íngreme, produzindo grande queda do juro e pequeno ganho de renda.",
            "No mesmo cenário, a política " + azb("fiscal") + " é forte: a alta do juro que ela provoca quase não "
            "expulsa investimento (pouco crowding out).",
            "Situações reais com investimento pouco sensível aos juros: recessões profundas com capacidade ociosa "
            "e pessimismo, crises de "
            "confiança, incerteza elevada.",
            vm("Regra-âncora: investimento insensível aos juros → monetária fraca, fiscal forte."),
        ],
        "dissecando": (cz("[inversão]") + " Troca “baixa” por “alta” na consequência. A confusão vem de misturar "
                       "as duas sensibilidades: demanda por moeda pouco sensível (LM íngreme) dá monetária forte; "
                       "investimento pouco sensível (IS íngreme) dá monetária fraca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a situação caracterizada por uma baixa sensibilidade-juros da demanda por moeda indica uma alta "
            "eficácia da política monetária.”</i> → CERTO",
            "<i>“…a situação caracterizada por uma baixa sensibilidade-juros do investimento indica uma baixa "
            "eficácia da política fiscal.”</i> → ERRADO (inversão: a fiscal fica mais eficaz)",
        ])],
        "reescrita": ("No modelo IS-LM, a situação caracterizada por uma baixa sensibilidade-juros do investimento "
                      "indica uma " + hl("baixa") + " eficácia da política monetária."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Com baixa sensibilidade do investimento ao juro, a política monetária perde eficácia.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0471-1 (mesma relação, versão CERTA)"],
    },
    # ------------------------------------------------------------------ E1-0478
    {
        "id": "ECO-E1-0478-1", "fonte_ref": "E1-0478", "destino": "27", "subtema": H2["lm"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": "Na síntese neoclássica, a curva LM revela os pontos onde o investimento se iguala à poupança.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na síntese neoclássica, a curva ") + vm("LM") + az(" revela os pontos onde o investimento "
                                                                          "se iguala à poupança.")),
        "poucas": ("I = S é a condição do mercado de bens: define a " + azb("IS") + ". A " + azb("LM") + " é o "
                   "equilíbrio do mercado monetário (demanda por moeda = oferta de moeda)."),
        "destrinchando": [
            "O nome de cada curva já diz o que ela equilibra: " + azb("IS") + " = <i>Investment = Saving</i> "
            "(mercado de bens); " + azb("LM") + " = <i>Liquidity preference = Money supply</i> (mercado "
            "monetário).",
            "IS: pares (Y, i) em que " + vd("I(i) = S(Y)") + " — ou, com governo, Y = C + I + G. Negativamente "
            "inclinada: juro menor → mais investimento → mais renda.",
            "LM: pares (Y, i) em que " + vd("L(Y, i) = M/P") + ". Positivamente inclinada: renda maior → mais "
            "demanda por moeda → juro maior para equilibrar.",
            "A interseção dá o equilíbrio simultâneo dos dois mercados. Na " + azb("síntese neoclássica") + " ("
            + oc("Hicks") + ", 1937; " + oc("Hansen") + "), esse é o modelo de curto prazo com preços fixos; no "
            "longo prazo, a flexibilidade de preços leva ao pleno emprego.",
            vm("Regra-âncora: I = S → IS; L = M → LM."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca de curva pura: a definição está correta, mas pertence "
                       "à IS. Basta decodificar as siglas para resolver."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na síntese neoclássica, a curva IS revela os pontos onde o investimento se iguala à "
            "poupança.”</i> → CERTO",
            "<i>“A curva LM representa os pares de renda e juros que equilibram o mercado de bens.”</i> → ERRADO "
            "(troca de mercado: é o monetário)",
        ])],
        "reescrita": ("Na síntese neoclássica, a curva " + hl("IS") + " revela os pontos onde o investimento se "
                      "iguala à poupança."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "I = S é a curva IS (mercado de bens); a LM é o equilíbrio do mercado monetário.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0479
    {
        "id": "ECO-E1-0479-1", "fonte_ref": "E1-0479", "destino": "27", "subtema": H2["lm"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": ("Na síntese neoclássica, a curva LM se desloca para a esquerda quando ocorre uma redução da "
                      "oferta monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na síntese neoclássica, a curva LM se desloca para a <u>esquerda</u> quando ocorre uma "
                      "<u>redução</u> da oferta monetária."),
        "poucas": ("Menos moeda com a mesma demanda exige " + vd("juros maiores") + " para cada nível de renda: a "
                   + azb("LM") + " sobe, ou seja, vai para a esquerda."),
        "destrinchando": [
            "Equilíbrio monetário: M/P = L(Y, i). Se M cai, ao juro e à renda antigos há " + azb("excesso de "
            "demanda por moeda") + ": o público vende títulos para obter liquidez, o preço dos títulos cai e o "
            "juro sobe.",
            "Para cada Y, o juro de equilíbrio fica mais alto (LM para cima); para cada i, só uma renda menor "
            "equilibra o mercado monetário (LM para a esquerda) — é o mesmo deslocamento.",
            "Efeito no IS-LM: " + vd("i ↑, Y ↓") + ". Na prática, é a contração monetária: venda de títulos pelo "
            "Banco Central, alta do compulsório.",
            "Detalhe: o que importa é a oferta <b>real</b>, M/P. Alta do nível de preços com M constante tem o "
            "mesmo efeito de reduzir M — é assim que a LM gera a curva de demanda agregada negativamente "
            "inclinada (P ↑ → M/P ↓ → i ↑ → Y ↓).",
        ],
        "dissecando": (cz("[literalidade]") + " Relação de manual. A variante ERRADA mais comum troca a curva "
                       "(“a IS se desloca”) ou o sentido (“para a direita”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na síntese neoclássica, a curva LM se desloca para a esquerda quando ocorre um aumento do nível "
            "de preços, mantida a oferta nominal de moeda.”</i> → CERTO",
            "<i>“Uma redução da oferta monetária desloca a curva IS para a esquerda.”</i> → ERRADO (curva trocada: "
            "a moeda mexe na LM)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Redução da oferta de moeda gera excesso de demanda por moeda; juros mais altos "
                            "restabelecem o equilíbrio; LM para a esquerda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0480
    {
        "id": "ECO-E1-0480-1", "fonte_ref": "E1-0480", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Considere uma economia em que o Governo tem a intenção de expandir a renda. Julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo IS-LM, com demanda por moeda infinitamente elástica em relação à taxa de juros "
                      "que já está muito baixa será preferível uma política fiscal expansionista a uma política "
                      "monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um modelo IS-LM, com demanda por moeda <u>infinitamente elástica</u> em relação à taxa de "
                      "juros que já está muito baixa será preferível uma política <u>fiscal</u> expansionista a uma "
                      "política monetária."),
        "poucas": ("Demanda por moeda infinitamente elástica com juro muito baixo é a " + azb("armadilha da "
                   "liquidez") + " (LM horizontal): a monetária não reduz mais o juro; a " + vd("fiscal") + " eleva "
                   "a renda sem crowding out."),
        "destrinchando": [
            "O item descreve a armadilha sem nomeá-la: com juros já no piso, todos esperam alta futura (e perda "
            "de capital nos títulos) e preferem reter moeda. Qualquer moeda adicional é " + azb("entesourada") + ".",
            "Política monetária: ↑M não reduz o juro → não estimula o investimento → " + vd("Y não muda") + ". É "
            "o “empurrar uma corda”.",
            "Política fiscal: ↑G ou ↓T desloca a IS ao longo da LM plana; o juro não sobe, não há "
            + azb("crowding out") + ", e a renda cresce pelo multiplicador inteiro.",
            "No mundo real, bancos centrais presos no limite inferior de juros recorreram a instrumentos não "
            "convencionais (compra maciça de ativos, o " + azb("<i>quantitative easing</i>") + ", e orientação "
            "futura), além de estímulos fiscais — foi o debate pós-2008 e da pandemia.",
            vm("Regra-âncora: armadilha da liquidez → fiscal eficaz, monetária ineficaz."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Descreve a armadilha pela definição técnica (demanda por moeda "
                       "infinitamente elástica + juro baixo), sem citar o nome — o candidato precisa reconhecê-la. "
                       "Trocar “fiscal” por “monetária” daria o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com demanda por moeda totalmente inelástica em relação à taxa de juros, será preferível uma "
            "política fiscal expansionista.”</i> → ERRADO (caso clássico: LM vertical, fiscal ineficaz)",
            "<i>“…nessas condições, a expansão monetária eleva a renda sem alterar a taxa de juros.”</i> → ERRADO "
            "(a monetária não altera a renda)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["preferível"], "dificuldade": 1,
        "comentario_fonte": "Armadilha da liquidez, LM horizontal: monetária ineficaz; fiscal expansionista é a "
                            "única capaz de elevar a renda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0475-1 (armadilha da liquidez: fiscal com eficácia máxima)"],
    },
    # ------------------------------------------------------------------ E1-0481
    {
        "id": "ECO-E1-0481-1", "fonte_ref": "E1-0481", "destino": "27", "subtema": H2["lm"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_SINTESE,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento da oferta monetária leva a curva LM a se deslocar para a esquerda, em face do "
                      "aumento da renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um aumento da oferta monetária leva a curva LM a se deslocar para a ")
                    + vm("esquerda, em face do aumento da renda") + az(".")),
        "poucas": ("Mais moeda desloca a " + azb("LM") + " para a " + vd("direita") + " (para baixo): a cada nível "
                   "de renda corresponde um juro menor. A renda maior é <b>efeito</b> do novo equilíbrio, não causa "
                   "do deslocamento."),
        "destrinchando": [
            "Com ↑M, ao juro e à renda antigos sobra moeda: o público compra títulos, o preço deles sobe e o "
            + vd("juro cai") + ". Para cada Y, o juro de equilíbrio é menor → LM para baixo/direita.",
            "Novo equilíbrio IS-LM: " + vd("i ↓ e Y ↑") + ". A renda sobe porque o juro menor estimula o "
            "investimento.",
            "Dois erros no item: (1) o sentido (esquerda); (2) a causa. Variação da renda não desloca a LM — "
            "provoca " + azb("movimento ao longo") + " dela. Os deslocadores da LM são a oferta de moeda, o nível "
            "de preços e mudanças autônomas na demanda por moeda.",
            "Para fixar: LM se desloca com M/P (direita se M/P sobe); IS se desloca com os gastos autônomos e a "
            "política fiscal (direita se G sobe ou T cai). Renda e juros são as variáveis dos eixos: mudam por "
            "movimento ao longo das curvas.",
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " Inverte o sentido e cria um nexo causal falso: põe a "
                       "renda como causa de um deslocamento provocado pela moeda. A expressão “em face do” é a "
                       "pista do nexo enxertado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento da oferta monetária desloca a curva LM para a direita, reduzindo a taxa de juros de "
            "equilíbrio e elevando a renda.”</i> → CERTO",
            "<i>“Um aumento da renda desloca a curva LM para cima.”</i> → ERRADO (variável do eixo: movimento ao "
            "longo da LM)",
        ])],
        "reescrita": ("Um aumento da oferta monetária leva a curva LM a se deslocar para a "
                      + hl("direita, reduzindo os juros para cada nível de renda") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Aumento da oferta monetária desloca a LM para a direita: mais moeda a cada renda, "
                            "juros de equilíbrio menores.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0482
    {
        "id": "ECO-E1-0482-1", "fonte_ref": "E1-0482", "destino": "27", "subtema": H2["is"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ISLM,
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM, a curva IS é deslocada para a esquerda se, para uma dada taxa de juros, "
                      "houver redução do nível do produto de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo IS-LM, a curva IS é deslocada para a esquerda se, <u>para uma dada taxa de "
                      "juros</u>, houver redução do nível do produto de equilíbrio."),
        "poucas": ("Deslocar a " + azb("IS") + " para a esquerda é exatamente isso: a cada juro, o mercado de bens "
                   "passa a se equilibrar com " + vd("produto menor") + " — por queda de algum gasto autônomo."),
        "destrinchando": [
            "A IS dá, para cada juro, o produto que equilibra o mercado de bens: Y = k(A − b·i), com k o "
            "multiplicador e A os gastos autônomos (C₀, I₀, G, X, −T…).",
            "O “para uma dada taxa de juros” é a chave: se o produto de equilíbrio cai <b>com o juro "
            "constante</b>, o que mudou foi outra coisa que não o juro — e a curva inteira se desloca. Se o "
            "produto caísse por alta do juro, seria " + azb("movimento ao longo") + " da IS.",
            "Causas de IS para a esquerda: queda de G, alta de T, queda do consumo autônomo (pessimismo), queda "
            "do investimento autônomo, queda das exportações; também uma redução do multiplicador.",
            "Tamanho do deslocamento horizontal: " + vd("k × ΔA") + ". Com c = 0,8 e queda de 10 em G, a IS anda "
            "50 para a esquerda.",
            "No equilíbrio com a LM, a renda cai menos que esse deslocamento horizontal, porque os juros também "
            "caem e amortecem a contração.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição operacional do deslocamento da IS. A banca testa a "
                       "distinção deslocamento × movimento: sem o “para uma dada taxa de juros”, a frase ficaria "
                       "ambígua."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva IS se desloca para a esquerda quando a elevação da taxa de juros reduz o produto de "
            "equilíbrio.”</i> → ERRADO (movimento ao longo da IS, não deslocamento)",
            "<i>“Uma redução dos gastos do governo desloca a IS para a esquerda.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["para uma dada taxa de juros"], "dificuldade": 1,
        "comentario_fonte": "IS para a esquerda com redução da demanda agregada (gastos públicos, consumo): menor "
                            "renda de equilíbrio para o mesmo juro.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_PERDIDA("Untitled (93).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0483
    {
        "id": "ECO-E1-0483-1", "fonte_ref": "E1-0483", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EMPREGO,
        "rotulo_item": "Item",
        "assertiva": "A política fiscal será eficaz se a demanda por moeda for perfeitamente inelástica à taxa de juros.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A política fiscal será ") + vm("eficaz") + az(" se a demanda por moeda for perfeitamente "
                                                                     "inelástica à taxa de juros.")),
        "poucas": ("Demanda por moeda inelástica aos juros = " + azb("LM vertical") + " (caso clássico): a "
                   "expansão fiscal só eleva os juros e expulsa investimento na mesma medida — " + vd("crowding out "
                   "total") + ", política fiscal ineficaz."),
        "destrinchando": [
            "Se a demanda por moeda depende só da renda (L = kY), o equilíbrio monetário M/P = kY fixa a renda em "
            + vd("Y = M/(kP)") + ", qualquer que seja o juro: a LM é vertical. É a lógica da " + azb("teoria "
            "quantitativa da moeda") + ".",
            "A expansão fiscal desloca a IS para a direita, mas a renda não pode subir sem mais moeda. O juro "
            "sobe até que a queda do investimento compense exatamente o gasto adicional: ΔI = −ΔG.",
            "Resultado: a política fiscal muda só a " + azb("composição") + " do produto (mais gasto público, "
            "menos investimento privado) e eleva os juros. Para o emprego, ineficaz.",
            "No mesmo caso, a política monetária tem eficácia " + vd("máxima") + ": cada unidade de moeda "
            "adicional vira renda. Por isso o caso clássico é a bandeira dos monetaristas.",
            vm("Regra-âncora: LM vertical → fiscal ineficaz, monetária máxima; LM horizontal → o inverso."),
        ],
        "grafico_verso": "ECO-E1-0483-1-V1",
        "dissecando": (cz("[inversão]") + " Troca o polo do caso extremo: “perfeitamente inelástica” leva ao caso "
                       "clássico, não à armadilha da liquidez (infinitamente elástica). Pista: o item fala da "
                       "elasticidade da <b>demanda por moeda</b>, que mexe na LM."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política fiscal será eficaz se a demanda por moeda for infinitamente elástica à taxa de "
            "juros.”</i> → CERTO",
            "<i>“Com demanda por moeda perfeitamente inelástica à taxa de juros, a política monetária é "
            "ineficaz.”</i> → ERRADO (inversão: ela tem eficácia máxima)",
        ])],
        "reescrita": ("A política fiscal será " + hl("ineficaz") + " se a demanda por moeda for perfeitamente "
                      "inelástica à taxa de juros."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["perfeitamente"], "dificuldade": 1,
        "comentario_fonte": "Demanda por moeda inelástica: LM vertical; a política fiscal só eleva os juros, sem "
                            "impacto sobre a renda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0484
    {
        "id": "ECO-E1-0484-1", "fonte_ref": "E1-0484", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EMPREGO,
        "rotulo_item": "Item",
        "assertiva": ("Uma redução dos impostos indiretos será eficaz se a demanda por investimentos for "
                      "perfeitamente inelástica à taxa de juros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma redução dos impostos indiretos será <u>eficaz</u> se a demanda por investimentos for "
                      "<u>perfeitamente inelástica</u> à taxa de juros."),
        "poucas": ("Investimento insensível aos juros = " + azb("IS vertical") + ": a expansão fiscal (corte de "
                   "impostos) eleva os juros, mas não expulsa investimento — " + vd("sem crowding out") + ", eficácia "
                   "máxima."),
        "destrinchando": [
            "Corte de impostos é " + azb("política fiscal expansionista") + ": aumenta a renda disponível (ou "
            "reduz preços ao consumidor) e eleva o consumo → a IS se desloca para a direita.",
            "Com investimento perfeitamente inelástico aos juros, a demanda agregada não depende de i: a IS é "
            "vertical. O deslocamento leva a renda para a direita pelo multiplicador inteiro; o juro sobe (a LM "
            "positivamente inclinada exige isso), mas essa alta não reduz o investimento.",
            "Logo, o " + azb("crowding out") + " é nulo e a política fiscal tem eficácia máxima — o mesmo "
            "resultado da armadilha da liquidez, por outro caminho (lá o juro não sobe; aqui sobe sem efeito).",
            "Contraponto: com IS vertical, a política " + azb("monetária") + " é ineficaz, pois reduz juros que o "
            "investimento ignora.",
            "Ressalva fora do modelo: o efeito do corte de impostos é menor que o de um aumento equivalente de "
            "gasto, porque parte da renda liberada é poupada (multiplicador dos tributos = c/(1 − c), menor que "
            "1/(1 − c)).",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Junta dois conceitos (instrumento fiscal + "
                       "elasticidade do investimento) e pede a conclusão. Pode parecer estranho que “inelástico” "
                       "favoreça a política, mas é a sensibilidade do investimento que gera o crowding out."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução dos impostos indiretos será ineficaz se a demanda por moeda for perfeitamente "
            "inelástica à taxa de juros.”</i> → CERTO",
            "<i>“Uma expansão monetária será eficaz se a demanda por investimentos for perfeitamente inelástica à "
            "taxa de juros.”</i> → ERRADO (IS vertical: monetária ineficaz)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["perfeitamente"], "dificuldade": 2,
        "comentario_fonte": "Investimento inelástico ao juro: a alta dos juros provocada pela expansão fiscal não "
                            "reduz o investimento; política fiscal mais eficaz.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0485
    {
        "id": "ECO-E1-0485-1", "fonte_ref": "E1-0485", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Acerca da política fiscal em uma economia fechada, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia fechada, que esteja operando abaixo do pleno emprego, o formulador de "
                      "política econômica que pretenda expandir o nível de renda deve reduzir os gastos do "
                      "governo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma economia fechada, que esteja operando abaixo do pleno emprego, o formulador de "
                       "política econômica que pretenda expandir o nível de renda deve ") + vm("reduzir")
                    + az(" os gastos do governo.")),
        "poucas": ("Cortar gastos é " + azb("política fiscal contracionista") + ": desloca a IS para a esquerda e "
                   "reduz a renda. Para expandi-la, o caminho fiscal é " + vd("aumentar G") + " (ou reduzir "
                   "tributos)."),
        "destrinchando": [
            "No modelo keynesiano, abaixo do pleno emprego a renda é limitada pela " + azb("demanda efetiva") + ". "
            "G é componente direto da demanda: ↓G → ↓Y pelo multiplicador; ↑G → ↑Y.",
            "No IS-LM: ↑G desloca a IS para a direita → " + vd("Y ↑") + " e i ↑ (com algum crowding out). ↓G faz "
            "o oposto: Y ↓ e i ↓.",
            "Alternativas para expandir a renda: corte de tributos (multiplicador menor que o do gasto), aumento "
            "de transferências, ou política monetária expansionista (↑M, LM para a direita).",
            "Nuance de debate: a tese da " + azb("contração fiscal expansionista") + " (" + oc("Giavazzi") + " e "
            + oc("Pagano") + ", 1990; " + oc("Alesina") + ") sustenta que ajustes críveis podem estimular a "
            "economia via expectativas e juros. É hipótese contestada e fora do modelo keynesiano-padrão que o "
            "item pressupõe.",
            vm("Regra-âncora: abaixo do pleno emprego, expansão = ↑G, ↓T ou ↑M."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sinal do instrumento. O contexto (“abaixo do pleno emprego”, "
                       "“expandir a renda”) aponta claramente para política expansionista; o “deve reduzir” é o "
                       "enxerto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o formulador que pretenda expandir o nível de renda pode elevar os gastos do governo ou reduzir "
            "os tributos.”</i> → CERTO",
            "<i>“…o formulador que pretenda expandir a renda deve vender títulos públicos no mercado aberto.”</i> → "
            "ERRADO (venda de títulos é contracionista)",
        ])],
        "reescrita": ("Em uma economia fechada, que esteja operando abaixo do pleno emprego, o formulador de política "
                      "econômica que pretenda expandir o nível de renda deve " + hl("aumentar") + " os gastos do "
                      "governo."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": "Reduzir gastos públicos é contracionista: diminui a demanda agregada, a renda e o "
                            "emprego.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
