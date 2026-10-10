"""Cards do lote de redação 01 — ECO, passada 03 (nota 56: modelo de Solow)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ee": "⚙️ Estado estacionário",
    "ouro": "🥇 Regra de ouro",
    "pop": "👥 População, tecnologia e convergência",
}

CMD_SOLOW = "Acerca do modelo de crescimento de Solow, julgue o item a seguir."

CMD_RT = "Com relação aos modelos de crescimento econômico de Solow, julgue o item a seguir."

CMD_BOZAN = "Com base nos modelos de crescimento econômico, julgue o item a seguir."

CMD_NAB = "A respeito das teorias de crescimento econômico, julgue o item a seguir."

CMD_DANIEL = "Julgue o item a seguir, relativo ao modelo de crescimento de Solow."

DINAMICA = ("Equação fundamental de " + oc("Solow") + " (1956), em termos por trabalhador: "
            + vd("Δk = s·f(k) − (n + δ)k") + ". O primeiro termo é o investimento (= poupança) por trabalhador; "
            "o segundo, o " + azb("investimento necessário") + " para repor o capital gasto (δk) e equipar os "
            "novos trabalhadores (nk).")

CARDS = [
    # ------------------------------------------------------------------ E1-0451
    {
        "id": "ECO-E1-0451-1", "fonte_ref": "E1-0451", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("O crescimento de longo prazo depende da acumulação de fatores e da produtividade total. Com "
                    "base nas teorias de crescimento, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("No modelo de crescimento exógeno de Solow, o aumento da taxa de poupança afeta o crescimento "
                      "do produto per capita apenas no longo prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de crescimento exógeno de Solow, o aumento da taxa de poupança afeta o "
                       "crescimento do produto per capita apenas ") + vm("no longo prazo") + az(".")),
        "poucas": ("É o contrário: a alta da poupança acelera o crescimento per capita só na " + azb("transição")
                   + " para o novo estado estacionário; no longo prazo, muda o " + azb("nível") + " do produto per "
                   "capita, e a taxa de crescimento volta a ser a do progresso técnico."),
        "destrinchando": [
            DINAMICA,
            "Partindo de um estado estacionário, uma alta permanente de s faz s·f(k) superar (n + δ)k: k passa a "
            "crescer, e y = f(k) cresce junto. Esse crescimento extra é " + vd("transitório") + ": com rendimentos "
            "marginais decrescentes do capital, cada unidade adicional de k rende menos, o investimento extra "
            "perde fôlego, e a economia chega a um novo k* mais alto.",
            "No novo estado estacionário, k e y por trabalhador param de crescer (sem progresso técnico) ou "
            "voltam a crescer à taxa " + vd("g") + " do progresso técnico (com ele). O ganho permanente é de "
            + azb("nível") + ": a trajetória fica paralela e mais alta.",
            "Por isso se diz que, em Solow, a poupança tem " + azb("efeito nível") + ", não "
            + azb("efeito crescimento") + ". Os modelos de " + azb("crescimento endógeno") + " (ex.: modelo AK) "
            "foram construídos justamente para que a poupança alterasse a taxa de longo prazo.",
            vm("Regra-âncora: poupança ↑ → crescimento ↑ só na transição; no longo prazo, só o nível sobe."),
        ],
        "grafico_verso": "ECO-E1-0451-1-V1",
        "dissecando": (cz("[inversão]") + " O item troca os prazos: atribui ao longo prazo o efeito que só existe "
                       "na transição. O “apenas” reforça a armadilha, porque o efeito de curto/médio prazo é "
                       "justamente o único que a poupança tem sobre a <b>taxa</b> de crescimento. Pista: em Solow, "
                       "“longo prazo” + “taxa de crescimento” remete sempre ao progresso técnico exógeno."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento da taxa de poupança eleva permanentemente o nível do produto per capita, mas só "
            "temporariamente a sua taxa de crescimento.”</i> → CERTO",
            "<i>“…o aumento da taxa de poupança eleva permanentemente a taxa de crescimento do produto per "
            "capita.”</i> → ERRADO (efeito nível tratado como efeito crescimento)",
        ])],
        "reescrita": ("No modelo de crescimento exógeno de Solow, o aumento da taxa de poupança afeta o "
                      "crescimento do produto per capita apenas " + hl("na transição para o novo estado "
                                                                "estacionário (no longo prazo, afeta só o nível)")
                      + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Alta da poupança eleva a taxa de crescimento só na transição; no longo prazo, a taxa "
                             "volta a depender do progresso técnico exógeno e o que sobe é o nível do produto per "
                             "capita (várias respostas de IA convergentes)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0553 (mesma prova, mesmo item; comentário fundido)"],
    },
    # ------------------------------------------------------------------ E1-0487
    {
        "id": "ECO-E1-0487-1", "fonte_ref": "E1-0487", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2017", "ano": 2017, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de Solow, um aumento na taxa de poupança é capaz de aumentar de forma "
                      "permanente a taxa de crescimento de um país. Logo, as baixas taxas de poupança registradas no "
                      "Brasil estão relacionadas com o seu baixo crescimento econômico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o modelo de Solow, um aumento na taxa de poupança ")
                    + vm("é capaz de aumentar de forma permanente") + az(" a taxa de crescimento de um país. Logo, "
                                                                         "as baixas taxas de poupança registradas no "
                                                                         "Brasil estão relacionadas com o seu baixo ")
                    + vm("crescimento econômico") + az(".")),
        "poucas": ("Em Solow, a poupança afeta o " + azb("nível") + " da renda per capita de estado estacionário, "
                   "não a taxa de crescimento de longo prazo. A premissa é falsa, e a conclusão sobre o "
                   + rx("Brasil") + " herda o erro."),
        "destrinchando": [
            "Uma alta de s eleva o capital por trabalhador de estado estacionário (k*) e, com ele, o produto por "
            "trabalhador (y*). Durante a transição, a economia cresce mais depressa; ao chegar ao novo k*, a taxa "
            "de crescimento per capita volta a ser a do progresso técnico " + vd("g") + " (ou zero, sem ele).",
            "O que Solow permite dizer sobre um país de poupança baixa é que ele tende a ter " + azb("renda per "
                                                                                                  "capita mais baixa")
            + " no longo prazo, não um crescimento permanentemente menor. Diferenças persistentes de taxa de "
            "crescimento só vêm de diferenças em g.",
            "Aplicação ao " + rx("Brasil") + ": a baixa taxa de poupança doméstica (historicamente perto de "
            + vd("15–18% do PIB") + " ⏳ (out/2026)) é argumento recorrente para explicar o investimento baixo e o "
            "hiato de renda em relação às economias asiáticas; pela lógica de Solow, porém, o efeito é de nível. "
            "Para explicar crescimento lento persistente, a literatura aponta a produtividade total dos fatores.",
            "Nos modelos de " + azb("crescimento endógeno") + " (" + oc("Romer") + ", " + oc("Lucas") + ", modelo "
            "AK), a poupança pode, sim, mudar a taxa de longo prazo; o item é falso porque atribui essa conclusão "
            "a Solow.",
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item troca “efeito nível” por “efeito "
                       "crescimento” na premissa e depois tira dela uma conclusão sobre o Brasil que parece "
                       "razoável no senso comum. O “Logo” só se sustenta se a premissa for verdadeira; quem aceita "
                       "a primeira frase marca CERTO por embalo. 🔥 Itens com “de forma permanente” + “taxa de "
                       "crescimento” + “poupança” são ERRADOS em Solow."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com o modelo de Solow, as baixas taxas de poupança registradas no Brasil ajudam a "
            "explicar seu nível de renda per capita relativamente baixo.”</i> → CERTO",
            "<i>“…um aumento na taxa de poupança eleva temporariamente a taxa de crescimento e permanentemente o "
            "nível do produto per capita.”</i> → CERTO",
        ])],
        "reescrita": ("De acordo com o modelo de Solow, um aumento na taxa de poupança " + hl("aumenta apenas "
                      "temporariamente (na transição)") + " a taxa de crescimento de um país. Logo, as baixas taxas "
                      "de poupança registradas no Brasil estão relacionadas com o seu baixo " + hl("nível de renda "
                      "per capita, e não com uma taxa de crescimento permanentemente menor") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["de forma permanente", "Logo"],
        "dificuldade": 1,
        "comentario_fonte": ("Errado: a poupança estabelece o limite ao crescimento; o crescimento é explicado por "
                             "população, progresso técnico e acumulação de capital (comentário impreciso: não "
                             "explicita o efeito nível × efeito crescimento)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0488
    {
        "id": "ECO-E1-0488-1", "fonte_ref": "E1-0488", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2017", "ano": 2017, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Uma das consequências do modelo de Solow é a sua rejeição de convergência de níveis de renda "
                      "para todos os países. Tal conclusão é uma implicação da hipótese de retornos marginais "
                      "crescentes do modelo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma das consequências do modelo de Solow é a sua ") + vm("rejeição")
                    + az(" de convergência de níveis de renda ") + vm("para todos os países")
                    + az(". Tal conclusão é uma implicação da hipótese de retornos marginais ") + vm("crescentes")
                    + az(" do modelo.")),
        "poucas": ("Solow supõe " + azb("rendimentos marginais decrescentes") + " do capital, e é isso que gera a "
                   "previsão de " + azb("convergência") + ": economias com pouco capital crescem mais depressa. Com "
                   "retornos crescentes, haveria divergência."),
        "destrinchando": [
            "Com f(k) côncava, o produto marginal do capital é alto quando k é baixo. Uma economia pobre (k abaixo "
            "do seu k*) investe mais do que precisa para manter k, e cada unidade nova rende muito: cresce mais "
            "rápido que uma economia rica. À medida que se aproxima de k*, desacelera.",
            "A convergência prevista é " + azb("condicional") + ": cada país converge para o <b>próprio</b> "
            "estado estacionário, definido por s, n, δ e tecnologia. Só países com os mesmos fundamentos "
            "convergem para o mesmo nível de renda. A " + azb("convergência absoluta") + " (todos para o mesmo "
            "nível) não é prevista nem observada na amostra mundial.",
            "Evidência: " + oc("Mankiw, Romer e Weil") + " (1992) mostraram que, controlando poupança e "
            "crescimento populacional (e capital humano), os dados confirmam a convergência condicional.",
            "Retornos marginais " + vm("crescentes") + " (ou constantes, como no modelo AK) eliminam a força de "
            "convergência: países ricos podem crescer tanto ou mais que os pobres. É a marca dos modelos de "
            "crescimento endógeno.",
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item inverte a conclusão (rejeição × previsão "
                       "de convergência) e a hipótese que a sustenta (crescentes × decrescentes). Um detalhe fino: "
                       "como a convergência de Solow é só condicional, ele de fato não prevê que <b>todos</b> os "
                       "países cheguem ao mesmo nível; mas o erro da 2ª frase basta para o ERRADO, porque retornos "
                       "crescentes não fazem parte do modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Solow prevê convergência condicional, implicação da hipótese de rendimentos marginais "
            "decrescentes do capital.”</i> → CERTO",
            "<i>“O modelo de Solow prevê que todos os países convergirão para o mesmo nível de renda per "
            "capita.”</i> → ERRADO (modulador absoluto: a convergência é condicional)",
        ])],
        "reescrita": ("Uma das consequências do modelo de Solow é a sua " + hl("previsão") + " de convergência de "

                      "níveis de renda " + hl("entre países com os mesmos fundamentos (convergência condicional)")
                      + ". Tal conclusão é uma implicação da hipótese de retornos marginais " + hl("decrescentes")
                      + " do modelo."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["todos"], "dificuldade": 2,
        "comentario_fonte": ("Errado: Solow é otimista quanto à convergência; rendimentos decrescentes reduzem a "
                             "rentabilidade nos países líderes e a poupança migraria aos atrasados (o comentário "
                             "mistura mobilidade de capitais, ausente no modelo básico, que é de economia fechada)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0523
    {
        "id": "ECO-E1-0523-1", "fonte_ref": "E1-0523", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Ago/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, o steady state é caracterizado por poupança per capita igual ao "
                      "alargamento do capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Solow, o steady state é caracterizado por poupança per capita igual ao "
                      "<u>alargamento do capital</u>."),
        "poucas": ("No estado estacionário, Δk = 0: a poupança por trabalhador, s·f(k), cobre exatamente o "
                   + azb("alargamento do capital") + " (n + δ)k, e não sobra nada para o "
                   + azb("aprofundamento") + "."),
        "destrinchando": [
            DINAMICA,
            "Vocabulário que a banca cobra: " + azb("aprofundamento do capital") + " (capital deepening) = "
            "aumento de k, a parcela da poupança que sobra depois de repor e equipar; " + azb("alargamento do "
                                                                                              "capital")
            + " (capital widening) = (n + δ)k, o investimento que só mantém k constante, dando aos novos "
            "trabalhadores o mesmo capital dos antigos e repondo o desgaste.",
            "Logo: " + vd("s·f(k) = Δk + (n + δ)k") + " — poupança = aprofundamento + alargamento. No "
            + azb("steady state") + ", o aprofundamento é zero e " + vd("s·f(k*) = (n + δ)k*") + ". Abaixo de "
            "k*, há aprofundamento (k cresce); acima, a poupança não cobre o alargamento e k cai.",
            "Como poupança = investimento na economia fechada do modelo, o item pode vir também com "
            "“investimento por trabalhador igual ao investimento de reposição/necessário”: mesma ideia.",
            "Atenção: alguns manuais reservam “alargamento” para a parcela nk e chamam δk de reposição; na "
            "linguagem das provas, porém, a soma (n + δ)k é tratada como o alargamento em sentido amplo.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " É a definição de estado estacionário com o vocabulário "
                       "“alargamento”, menos usual que “depreciação efetiva” ou “investimento necessário”. A "
                       "armadilha é confundir com aprofundamento: quem troca os termos marca ERRADO. 🔥 A dupla "
                       "aprofundamento × alargamento é cobrada com frequência nos simulados de CACD."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, o steady state é caracterizado por poupança per capita igual ao "
            "aprofundamento do capital.”</i> → ERRADO (troca de conceito: no steady state o aprofundamento é "
            "nulo)",
            "<i>“Quando a poupança per capita supera o alargamento do capital, o capital por trabalhador "
            "aumenta.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No steady state, k e y são constantes; a poupança (investimento) por trabalhador "
                             "iguala o investimento necessário para manter k, isto é, o alargamento do capital "
                             "(comentário de IA longo e repetitivo, e com uma imprecisão: diz que as variáveis per "
                             "capita “crescem a uma taxa igual à populacional”)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0727-1 (mesma assertiva, em outro simulado da Clipping)"],
    },
    # ------------------------------------------------------------------ E1-0707
    {
        "id": "ECO-E1-0707-1", "fonte_ref": "E1-0707", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Solow incorpora progresso tecnológico exógeno, permitindo que o crescimento de "
                      "longo prazo do produto per capita ocorra mesmo na ausência de aumento do estoque de capital "
                      "ou da força de trabalho."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo de Solow incorpora progresso tecnológico exógeno, permitindo que o crescimento de "
                      "longo prazo do produto per capita ocorra <u>mesmo na ausência de aumento do estoque de "
                      "capital ou da força de trabalho</u>."),
        "poucas": ("Com Y = F(K, A·L) e A crescendo à taxa " + vd("g") + ", o produto por trabalhador sobe mesmo "
                   "com K e L parados: a tecnologia multiplica a eficiência de cada trabalhador. É o "
                   + azb("progresso técnico") + ", e não o capital, que sustenta o crescimento per capita de longo "
                   "prazo."),
        "destrinchando": [
            "Sem progresso técnico, o crescimento per capita exige " + azb("aprofundamento do capital")
            + " (k ↑) e cessa no estado estacionário, por causa dos rendimentos decrescentes. Era esse o "
            "raciocínio de quem errou o item — correto, mas para a versão básica do modelo.",
            "Na versão com tecnologia, A entra como " + azb("trabalho efetivo") + " (A·L, progresso "
            "“poupador de trabalho”, à Harrod). Se K e L estão fixos e A cresce, A·L cresce, Y cresce e "
            "Y/L cresce. É exatamente o experimento mental do item.",
            "No estado estacionário dessa versão, o que fica constante é o capital por trabalhador efetivo "
            + vd("k̃ = K/(A·L)") + ". Como A cresce a g, K/L e Y/L crescem a " + vd("g") + "; K e Y agregados "
            "crescem a " + vd("n + g") + ".",
            "Detalhe: na trajetória de crescimento equilibrado o capital <b>acompanha</b> a tecnologia (K/L "
            "cresce a g), mas ele é consequência, não causa: o motor é A. Sem A, nenhuma acumulação sustenta "
            "crescimento per capita.",
            vm("Regra-âncora: em Solow, crescimento per capita de longo prazo = taxa de progresso técnico (g), "
               "exógena."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " Verdadeiro, mas choca quem associa crescimento per capita a "
                       "mais capital por trabalhador. A expressão “mesmo na ausência de” é um contrafactual: "
                       "isola o papel da tecnologia, não descreve a trajetória de equilíbrio (em que K também "
                       "cresce). A pista é “progresso tecnológico exógeno”, o único motor de longo prazo do "
                       "modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow sem progresso tecnológico, o produto per capita cresce indefinidamente "
            "enquanto houver poupança positiva.”</i> → ERRADO (sem tecnologia, o crescimento per capita cessa no "
            "estado estacionário)",
            "<i>“No estado estacionário com progresso técnico, o capital por trabalhador efetivo é "
            "constante.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["mesmo"], "dificuldade": 2,
        "comentario_fonte": ("Com progresso técnico exógeno à taxa g, o produto por trabalhador cresce a g no "
                             "longo prazo; no estado estacionário, constante é K/(A·L). Longa discussão (várias "
                             "respostas de IA) sobre aprofundamento × progresso técnico e a álgebra de y = A·f(k̃)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (207)–(229).png (20 imagens)", "tipo_fonte": "DIAGRAMA/FÓRMULA",
                           "lado": "verso", "acao": "irrecuperavel (não preservadas; conteúdo coberto pelo "
                                                    "texto do comentário)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0709
    {
        "id": "ECO-E1-0709-1", "fonte_ref": "E1-0709", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, aumentos na taxa de poupança levam a um nível de produto per capita de "
                      "estado estacionário mais elevado, mas não afetam a taxa de crescimento de longo prazo, que "
                      "depende exclusivamente do progresso tecnológico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Solow, aumentos na taxa de poupança levam a um nível de produto per capita de "
                      "estado estacionário mais elevado, mas não afetam a taxa de crescimento de longo prazo, que "
                      "depende <u>exclusivamente</u> do progresso tecnológico."),
        "poucas": ("É a síntese de Solow: poupança tem " + azb("efeito nível") + " (eleva k* e y*); a taxa de "
                   "crescimento per capita de longo prazo é a do " + azb("progresso tecnológico exógeno") + "."),
        "destrinchando": [
            DINAMICA,
            "Alta de s → s·f(k) sobe → novo k* maior → " + vd("y* = f(k*) maior") + ". Na transição, a economia "
            "cresce mais depressa (como explicam " + oc("Mankiw") + " e " + oc("Blanchard") + "); no novo "
            "equilíbrio, o crescimento de y volta à taxa " + vd("g") + ".",
            "O “exclusivamente” está correto porque, em estado estacionário, y = A·f(k̃) com k̃ constante: a única "
            "coisa que move y é A. Nem s, nem n, nem δ mudam a taxa de crescimento per capita de longo prazo — "
            "todos mudam apenas o nível.",
            "Leitura cuidadosa: a frase fala do crescimento <b>per capita</b> (o contexto é o produto per "
            "capita). O produto agregado cresce a n + g, e aí a população também conta.",
            "Contraste útil: a mesma frase com “progresso tecnológico <b>endógeno</b>” é ERRADA — em Solow ele é "
            "exógeno; endogenizá-lo é o programa de " + oc("Romer") + " (1990).",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Reproduz o resultado-padrão dos manuais. O "
                       "“exclusivamente” costuma assustar (modulador absoluto = ERRADO?), mas aqui é exato: em "
                       "Solow, só o progresso técnico gera crescimento per capita sustentado. A banca inverte o "
                       "item trocando “exógeno” por “endógeno” ou “nível” por “taxa”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…mas não afetam a taxa de crescimento de longo prazo, que é determinada exclusivamente pelo "
            "progresso tecnológico endógeno.”</i> → ERRADO (em Solow, o progresso técnico é exógeno)",
            "<i>“…aumentos na taxa de poupança elevam permanentemente a taxa de crescimento do produto per "
            "capita.”</i> → ERRADO (efeito nível tratado como efeito crescimento)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": ("Mankiw e Blanchard: alta da poupança leva a novo estado estacionário com k* e y* "
                             "maiores; crescimento temporariamente mais alto na transição; no longo prazo, taxa "
                             "determinada só pelo progresso tecnológico."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00525-1 (mesma frase com “progresso tecnológico endógeno”, "
                    "ERRADO)"],
    },
    # ------------------------------------------------------------------ E1-0714
    {
        "id": "ECO-E1-0714-1", "fonte_ref": "E1-0714", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2019", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Aumentos da taxa de poupança, no modelo de Solow, resultam em uma aceleração apenas "
                      "temporária do crescimento de uma economia, uma vez que a função de produção apresenta "
                      "retornos decrescentes de escala no capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Aumentos da taxa de poupança, no modelo de Solow, resultam em uma aceleração "
                      "<u>apenas temporária</u> do crescimento de uma economia, uma vez que a função de produção "
                      "apresenta <u>retornos decrescentes de escala no capital</u>."),
        "poucas": ("A aceleração é " + azb("temporária") + " porque o capital tem " + azb("rendimentos "
                   "marginais decrescentes") + ": cada unidade adicional rende menos, até que a poupança só cubra "
                   "o investimento necessário no novo k*."),
        "destrinchando": [
            "Mecanismo: s ↑ → investimento supera (n + δ)k → k cresce → y cresce. Mas, como f(k) é côncava, "
            "o produto extra de cada unidade de capital diminui, e o investimento gerado por ele também; a reta "
            "(n + δ)k, ao contrário, cresce proporcionalmente. As duas se reencontram num " + vd("k* mais "
                                                                                                "alto") + ".",
            "A expressão do item é imprecisa: “retornos de escala” se referem a aumentar <b>todos</b> os "
            "fatores na mesma proporção. A função neoclássica de Solow tem " + azb("retornos constantes de "
                                                                                  "escala") + " (dobrar K e L "
            "dobra Y) e " + azb("rendimentos marginais decrescentes") + " em cada fator isolado. É isso que a "
            "banca quis dizer com “decrescentes no capital”.",
            "Exemplo: na Cobb-Douglas Y = K<sup>α</sup>L<sup>1−α</sup>, os expoentes somam 1 (escala "
            "constante) e PMg<sub>K</sub> = αK<sup>α−1</sup>L<sup>1−α</sup> cai quando K sobe com L fixo.",
            "Se o capital tivesse rendimentos constantes (modelo AK, y = Ak), a poupança elevaria a taxa de "
            "crescimento para sempre — é o ponto de partida do crescimento endógeno.",
            vm("Regra-âncora: rendimentos marginais decrescentes do capital → efeito da poupança sobre o "
               "crescimento é só transitório."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " A ideia central está certa e a banca manteve CERTO "
                       "apesar do termo impreciso (“retornos decrescentes de escala no capital” no lugar de "
                       "“rendimentos marginais decrescentes do capital”). Quem conhece a distinção pode hesitar; "
                       "o critério é se o mecanismo descrito é o do modelo — e é."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma vez que a função de produção apresenta retornos crescentes de escala.”</i> → ERRADO (a "
            "função de Solow tem retornos constantes de escala)",
            "<i>“Aumentos da taxa de poupança resultam em aceleração permanente do crescimento per capita.”</i> → "
            "ERRADO (efeito apenas transitório)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas"], "dificuldade": 2,
        "comentario_fonte": ("Correto: a poupança eleva só o nível do capital per capita de estado estacionário, "
                             "por causa dos rendimentos decrescentes do capital (a fonte nota que “retornos "
                             "decrescentes de escala do capital” é expressão imprecisa) + pressupostos do modelo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "6c708528-1215-4d5b-9fea-81209e54b9a3", "tipo_fonte": "GRÁFICO",
                           "lado": "verso", "acao": "irrecuperavel (não preservada; mecanismo explicado no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0715
    {
        "id": "ECO-E1-0715-1", "fonte_ref": "E1-0715", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2019", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de Solow, quando a economia se encontra em crescimento balanceado, o "
                      "estoque de capital e o produto crescem à mesma taxa, o que implica que a relação "
                      "capital-produto permanece constante."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o modelo de Solow, quando a economia se encontra em crescimento balanceado, o "
                      "estoque de capital e o produto crescem <u>à mesma taxa</u>, o que implica que a relação "
                      "capital-produto permanece constante."),
        "poucas": ("Na " + azb("trajetória de crescimento balanceado") + ", K e Y crescem ambos a "
                   + vd("n + g") + " (ou a n, sem progresso técnico); se numerador e denominador crescem igual, "
                   "a razão " + vd("K/Y") + " é constante."),
        "destrinchando": [
            "Crescimento balanceado (ou equilibrado) = todas as variáveis crescem a taxas constantes. Em Solow, "
            "ele coincide com o " + azb("estado estacionário") + " em unidades efetivas: k̃ = K/(A·L) constante.",
            "Taxas no estado estacionário: K e Y crescem a " + vd("n + g") + "; K/L e Y/L, a " + vd("g")
            + "; k̃ e ỹ, a " + vd("zero") + ". Logo K/Y = k̃/ỹ é constante, e também a participação do capital "
            "na renda e a taxa de juros real.",
            "Esses são os " + azb("fatos estilizados") + " de " + oc("Kaldor") + " (1961): razão "
            "capital-produto aproximadamente estável, produto per capita crescendo a taxa estável, participações "
            "dos fatores estáveis. Uma das virtudes do modelo de Solow é reproduzi-los.",
            "Fora do estado estacionário (na transição), a razão muda: uma economia abaixo de k̃* acumula capital "
            "mais depressa que o produto, e K/Y sobe até estabilizar.",
        ],
        "dissecando": (cz("[literalidade]") + " É a definição de crescimento balanceado com a consequência "
                       "algébrica correta. A fonte aponta que o enunciado usa “crescimento balanceado” como "
                       "sinônimo de estado estacionário — no Solow com tecnologia, os dois se equivalem. A banca "
                       "inverteria trocando “mesma taxa” por taxas diferentes ou K/Y “crescente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…em crescimento balanceado, o estoque de capital cresce mais rápido que o produto, elevando a "
            "relação capital-produto.”</i> → ERRADO (no crescimento balanceado, K e Y crescem à mesma taxa)",
            "<i>“No estado estacionário com progresso técnico, o produto per capita cresce à taxa g.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Correto: crescimento balanceado = estado estacionário; capital, produto, consumo e "
                             "população crescem a taxas constantes, K e Y à mesma taxa, logo K/Y constante "
                             "(vários comentários convergentes, um da professora Michelle Miltons)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (258).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (não preservada; conteúdo coberto pelo comentário)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0718
    {
        "id": "ECO-E1-0718-1", "fonte_ref": "E1-0718", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("O resíduo de Solow representa quanto do crescimento econômico é explicado por outros fatores "
                      "que não sejam o crescimento do capital e do trabalho. Uma interpretação desse termo é que ele "
                      "corresponde ao progresso tecnológico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O resíduo de Solow representa quanto do crescimento econômico é explicado por outros fatores "
                      "que não sejam o crescimento do capital e do trabalho. <u>Uma interpretação</u> desse termo é "
                      "que ele corresponde ao progresso tecnológico."),
        "poucas": ("O " + azb("resíduo de Solow") + " é a parte do crescimento do produto que sobra depois de "
                   "descontada a contribuição de capital e trabalho; costuma ser lido como progresso técnico, ou "
                   + azb("produtividade total dos fatores") + " (PTF)."),
        "destrinchando": [
            azb("Contabilidade do crescimento") + " (" + oc("Solow") + ", 1957): com Y = A·K<sup>α</sup>"
            "L<sup>1−α</sup>, " + vd("g_Y = g_A + α·g_K + (1 − α)·g_L") + ". Mede-se g_Y, g_K, g_L e α (a "
            "participação do capital na renda); o g_A é obtido por diferença — daí “resíduo”.",
            "Achado de Solow para os EUA (1909–1949): cerca de " + vd("7/8") + " do crescimento do produto por "
            "hora trabalhada vinham do resíduo, e não da acumulação de capital. " + oc("Abramovitz") + " chamou "
            "o resíduo de “medida da nossa ignorância”.",
            "Por que “uma interpretação”: o resíduo capta tudo o que não é K nem L medidos — tecnologia, mas "
            "também capital humano, melhor alocação de recursos, instituições, economias de escala e erros de "
            "medida. Por isso o modulador relativo salva o item.",
            "Aplicação ao " + rx("Brasil") + ": a estagnação da PTF desde os anos 1980 é a explicação mais citada "
            "para o baixo crescimento do produto por trabalhador.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de manual, protegida por “uma "
                       "interpretação”. A banca inverteria afirmando que o resíduo mede <b>apenas</b> o progresso "
                       "tecnológico, ou que ele é explicado dentro do modelo (é exógeno). 🔥 Resíduo de Solow × "
                       "endogeneidade da tecnologia é dupla frequente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resíduo de Solow corresponde exclusivamente ao progresso tecnológico, que o modelo explica a "
            "partir das decisões de investimento em P&amp;D.”</i> → ERRADO (modulador absoluto e endogeneidade "
            "indevida)",
            "<i>“Na contabilidade do crescimento, o resíduo é obtido descontando-se do crescimento do produto as "
            "contribuições ponderadas do capital e do trabalho.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["uma interpretação"], "dificuldade": 1,
        "comentario_fonte": ("Certo: o resíduo é a “sobra” do crescimento não explicada pela expansão do capital "
                             "e do trabalho; a interpretação mais razoável é o progresso tecnológico (vários "
                             "comentários convergentes)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0719
    {
        "id": "ECO-E1-0719-1", "fonte_ref": "E1-0719", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Solow incorpora, de forma endógena, o progresso tecnológico, explicando como as "
                      "empresas tomam decisões que maximizam o retorno de investimentos em geração de "
                      "conhecimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo de Solow incorpora, de forma ") + vm("endógena") + az(", o progresso "
                                                                                     "tecnológico, ")
                    + vm("explicando") + az(" como as empresas tomam decisões que maximizam o retorno de "
                                            "investimentos em geração de conhecimento.")),
        "poucas": ("Em Solow, o progresso tecnológico é " + azb("exógeno") + ": entra como um dado (A cresce à "
                   "taxa g, “cai do céu”), sem nenhuma decisão de empresas sobre P&amp;D. Explicar essa decisão é o "
                   "programa do " + azb("crescimento endógeno") + "."),
        "destrinchando": [
            "No modelo de " + oc("Solow") + " (1956), as variáveis exógenas são a taxa de poupança s, o "
            "crescimento populacional n, a depreciação δ e a taxa de progresso técnico g. O modelo explica a "
            "acumulação de capital, não a criação de tecnologia.",
            "Por isso o progresso técnico aparece, na contabilidade do crescimento, como " + azb("resíduo")
            + ": a parcela do crescimento que capital e trabalho não explicam.",
            "Quem endogeniza a tecnologia: " + oc("Romer") + " (1990), em que firmas investem em P&amp;D para "
            "obter poder de monopólio temporário sobre ideias (bens não rivais); " + oc("Lucas") + " (1988), com "
            "acumulação de capital humano; " + oc("Arrow") + " (1962), com aprendizado pela prática "
            "(learning by doing). A descrição do item (“empresas que maximizam o retorno de investimentos em "
            "conhecimento”) é praticamente a de Romer.",
            "Consequência de política: em Solow, nenhuma política (salvo afetar g “de fora”) muda o crescimento "
            "de longo prazo; nos modelos endógenos, subsídios a P&amp;D, educação e propriedade intelectual "
            "podem fazê-lo.",
            vm("Regra-âncora: Solow = tecnologia exógena; Romer/Lucas = tecnologia endógena."),
        ],
        "dissecando": (cz("[troca de conceito · troca de ator]") + " O item atribui a Solow a tese central do "
                       "crescimento endógeno. A pista é o vocabulário microfundamentado (“empresas tomam "
                       "decisões”, “maximizam o retorno”), que não existe no Solow original. 🔥 Exógeno × "
                       "endógeno é a pegadinha mais frequente em itens sobre Solow."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Romer incorpora, de forma endógena, o progresso tecnológico, explicando como as "
            "empresas decidem investir em geração de conhecimento.”</i> → CERTO",
            "<i>“No modelo de Solow, o progresso técnico é exógeno e interpretado, empiricamente, pelo resíduo "
            "de Solow.”</i> → CERTO",
        ])],
        "reescrita": ("O modelo de Solow incorpora, de forma " + hl("exógena") + ", o progresso tecnológico, "
                      + hl("sem explicar") + " como as empresas tomam decisões que maximizam o retorno de "
                      "investimentos em geração de conhecimento."),
        "tipo_erro": ["TROCA_CONCEITO", "TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Errado: progresso tecnológico e crescimento populacional são exógenos em Solow; o "
                             "modelo não incorpora decisões de investimento em P&amp;D; a tecnologia aparece como "
                             "resíduo (comentários de Daniel Sousa e outros, convergentes)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0721
    {
        "id": "ECO-E1-0721-1", "fonte_ref": "E1-0721", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Nos parâmetros do modelo de Solow, o aumento da taxa de poupança é irrelevante para o nível "
                      "de renda per capita de longo prazo de uma sociedade, pois o estado estacionário é afetado "
                      "somente pelo nível de produtividade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nos parâmetros do modelo de Solow, o aumento da taxa de poupança ")
                    + vm("é irrelevante para") + az(" o nível de renda per capita de longo prazo de uma sociedade, "
                                                    "pois o estado estacionário é afetado ")
                    + vm("somente pelo nível de produtividade") + az(".")),
        "poucas": ("A poupança é justamente o que fixa o " + azb("nível") + " de renda per capita de longo prazo: "
                   "s maior → k* maior → y* maior. O que ela não muda é a <b>taxa</b> de crescimento de longo "
                   "prazo."),
        "destrinchando": [
            DINAMICA,
            "No estado estacionário, " + vd("s·f(k*) = (n + δ)k*") + ". Com Cobb-Douglas y = A·k<sup>α</sup>: "
            + vd("k* = [s·A/(n + δ)]<sup>1/(1−α)</sup>") + ". O k* — e com ele y* — depende de " + azb("s")
            + " (+), " + azb("n") + " (−), " + azb("δ") + " (−) e " + azb("A") + " (+). A produtividade é um "
            "determinante, não o único.",
            "Alta de s: a curva s·f(k) sobe, cruza (n + δ)k mais à direita, e a economia migra para um k* e um "
            "y* maiores. É o resultado que " + oc("Mankiw") + " usa para explicar por que países que poupam "
            "mais tendem a ser mais ricos.",
            "O item confunde " + azb("efeito nível") + " (que a poupança tem) com " + azb("efeito crescimento")
            + " (que ela não tem no longo prazo). A frase correta sobre a irrelevância seria: “o aumento da "
            "poupança é irrelevante para a taxa de crescimento per capita de longo prazo”.",
        ],
        "grafico_verso": "ECO-E1-0721-1-V1",
        "dissecando": (cz("[troca de conceito · restrição indevida]") + " Duas falhas: troca “taxa de "
                       "crescimento” (onde a poupança é irrelevante no longo prazo) por “nível de renda” (onde ela "
                       "é decisiva) e restringe os determinantes do estado estacionário com o “somente”. Pista: "
                       "“nível” + “poupança” em Solow = efeito positivo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento da taxa de poupança é irrelevante para a taxa de crescimento per capita de longo "
            "prazo.”</i> → CERTO",
            "<i>“…um aumento da taxa de crescimento populacional eleva a renda per capita de estado "
            "estacionário.”</i> → ERRADO (sinal trocado: n maior reduz k* e y*)",
        ])],
        "reescrita": ("Nos parâmetros do modelo de Solow, o aumento da taxa de poupança " + hl("eleva")
                      + " o nível de renda per capita de longo prazo de uma sociedade, pois o estado estacionário "
                      "é afetado " + hl("pela poupança, pelo crescimento populacional, pela depreciação e pela "
                                        "produtividade") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "RESTRICAO"], "moduladores": ["somente"], "dificuldade": 1,
        "comentario_fonte": ("Errado: é justamente a poupança que determina a renda per capita de longo prazo; "
                             "s → s′ leva k* a k** e eleva y (gráfico). Um dos comentários traz justificativa "
                             "confusa (poupança “mantém o equilíbrio” por reservas para a força de trabalho)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "2d1d6f3a-d472-443c-84f5-1bff155569fe", "tipo_fonte": "GRÁFICO",
                           "lado": "verso", "acao": "irrecuperavel (não preservada; redesenho didático em "
                                                    "ECO-E1-0721-1-V1 a partir da descrição)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0725
    {
        "id": "ECO-E1-0725-1", "fonte_ref": "E1-0725", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o modelo de Solow, a acumulação de capital ocorre por meio do investimento, que "
                      "aumenta a quantidade de máquinas, equipamentos e infraestrutura disponíveis na economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o modelo de Solow, a acumulação de capital ocorre <u>por meio do investimento</u>, "
                      "que aumenta a quantidade de máquinas, equipamentos e infraestrutura disponíveis na "
                      "economia."),
        "poucas": ("Em Solow, o capital cresce pelo " + azb("investimento") + " (financiado pela poupança, "
                   "I = s·Y) e diminui pela " + azb("depreciação") + ": ΔK = I − δK."),
        "destrinchando": [
            "Lei de movimento do capital agregado: " + vd("ΔK = s·Y − δK") + ". O investimento é o gasto com "
            "bens de capital — máquinas, equipamentos, construções, infraestrutura —, que se somam ao estoque.",
            "Na economia fechada do modelo, " + azb("poupança = investimento") + ": toda renda não consumida "
            "vira capital novo. É uma hipótese forte (não há problema de demanda efetiva, ao contrário dos "
            "modelos keynesianos e de " + oc("Harrod") + "-" + oc("Domar") + ").",
            "Em termos por trabalhador: " + vd("Δk = s·f(k) − (n + δ)k") + ". Se o investimento supera a "
            "reposição e o equipamento dos novos trabalhadores, há aprofundamento do capital; no estado "
            "estacionário, os dois se igualam.",
            "O que o investimento <b>não</b> faz em Solow: sustentar sozinho o crescimento per capita no longo "
            "prazo, por causa dos rendimentos decrescentes.",
        ],
        "dissecando": (cz("[literalidade]") + " Descrição direta do mecanismo de acumulação. Não há modulador "
                       "nem pegadinha; o risco é desconfiar por excesso (achar que “infraestrutura” ou "
                       "“máquinas” extrapolam o modelo). A banca inverteria atribuindo a acumulação ao consumo ou "
                       "dizendo que ela, sozinha, gera crescimento per capita permanente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o modelo de Solow, a acumulação contínua de capital por meio do investimento sustenta "
            "indefinidamente o crescimento do produto per capita.”</i> → ERRADO (rendimentos decrescentes: o "
            "efeito se esgota no estado estacionário)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Certo: o investimento i = s·f(k), financiado pela poupança, adiciona capital; a "
                             "depreciação o reduz; no estado estacionário se igualam."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0726
    {
        "id": "ECO-E1-0726-1", "fonte_ref": "E1-0726", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, um aumento da taxa de consumo faz a economia crescer até que ela alcance "
                      "um novo estado estacionário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow, um aumento da taxa de ") + vm("consumo")
                    + az(" faz a economia crescer até que ela alcance um novo estado estacionário.")),
        "poucas": ("Quem faz a economia crescer até um novo estado estacionário é a alta da taxa de "
                   + azb("poupança") + ". Mais consumo = menos poupança = menos investimento: k* e y* "
                   "<b>caem</b>."),
        "destrinchando": [
            "Em Solow, a renda se divide em consumo e poupança: c = (1 − s)·y. Aumentar a “taxa de consumo” "
            "(1 − s) é o mesmo que reduzir s.",
            "Com s menor, s·f(k) desce, o investimento fica abaixo de (n + δ)k, o capital por trabalhador "
            "diminui e a economia converge para um " + vd("k* e um y* menores") + ". Há uma fase de crescimento "
            "per capita <b>negativo</b> (ou abaixo de g), não acima.",
            "A frase só seria verdadeira com " + azb("poupança") + ": alta de s → investimento > (n + δ)k → k "
            "cresce → crescimento temporário até o novo k*, maior.",
            "Não confundir com a lógica keynesiana de curto prazo, em que mais consumo eleva a demanda agregada "
            "e o produto: Solow é modelo de oferta e de longo prazo, com pleno emprego e poupança igual a "
            "investimento.",
            "Exceção que a banca pode explorar: se a economia poupa acima da " + azb("regra de ouro") + ", "
            "consumir mais (poupar menos) <b>eleva o consumo</b> per capita em todas as datas — mas não o "
            "produto.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca de uma só palavra: “consumo” no lugar de “poupança”, "
                       "num enunciado que, fora isso, é a frase-padrão de Solow. A troca seduz quem raciocina com "
                       "o multiplicador keynesiano. Pista: em Solow, crescimento vem de acumulação de capital, que "
                       "vem da poupança."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, um aumento da taxa de poupança faz a economia crescer até que ela alcance um "
            "novo estado estacionário.”</i> → CERTO",
            "<i>“Em uma economia acima da regra de ouro, a redução da taxa de poupança eleva o consumo per "
            "capita.”</i> → CERTO",
        ])],
        "reescrita": ("No modelo de Solow, um aumento da taxa de " + hl("poupança") + " faz a economia crescer até "
                      "que ela alcance um novo estado estacionário."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Trocou consumo por poupança: é a poupança que permite acumular capital e gera "
                             "crescimento temporário até o novo estado estacionário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0727
    {
        "id": "ECO-E1-0727-1", "fonte_ref": "E1-0727", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, o steady state é caracterizado por poupança per capita igual ao "
                      "alargamento do capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Solow, o steady state é caracterizado por <u>poupança per capita igual ao "
                      "alargamento do capital</u>."),
        "poucas": ("É a própria definição de " + azb("steady state") + ": s·f(k*) = (n + δ)k*. Toda a poupança "
                   "vai para o " + azb("alargamento") + " (repor o desgaste e equipar os novos trabalhadores), e o "
                   "capital por trabalhador não muda."),
        "destrinchando": [
            DINAMICA,
            "Decomposição da poupança por trabalhador: " + vd("s·f(k) = aprofundamento (Δk) + alargamento "
                                                              "[(n + δ)k]") + ". " + azb("Aprofundamento")
            + " = mais capital para cada trabalhador; " + azb("alargamento") + " = manter o mesmo capital por "
            "trabalhador numa força de trabalho que cresce e num estoque que se desgasta.",
            "No steady state, Δk = 0: k, y e c por trabalhador ficam constantes (sem progresso técnico). Por "
            "isso o produto agregado cresce só à taxa " + vd("n") + ".",
            "Leitura gráfica: k* é a interseção da curva s·f(k) com a reta (n + δ)k. À esquerda de k*, a curva "
            "está acima da reta (há aprofundamento); à direita, abaixo (o capital por trabalhador encolhe).",
            "Com progresso técnico, a mesma condição vale em unidades efetivas: " + vd("s·f(k̃*) = (n + g + δ)k̃*")
            + ".",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição de estado estacionário com nome menos comum para o "
                       "investimento necessário. O erro do candidato costuma vir de confundir “alargamento” com "
                       "“aprofundamento” ou de achar que o termo vale só para a parcela da população (nk). A "
                       "mesma assertiva já apareceu em mais de um simulado: 🔥 tema recorrente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No steady state, a poupança per capita supera o alargamento do capital, garantindo o "
            "aprofundamento contínuo.”</i> → ERRADO (no steady state não há aprofundamento)",
            "<i>“Abaixo do capital de estado estacionário, a poupança per capita é maior que o alargamento do "
            "capital.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("É a própria definição de steady state: sf(k) = (n + δ)k; o investimento per capita "
                             "é a poupança per capita, e o termo de reposição é o alargamento do capital."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (249).png", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "irrecuperavel (não preservada; fórmula reescrita no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0523-1 (mesma assertiva, em outro simulado da Clipping)"],
    },
    # ------------------------------------------------------------------ E1-0728
    {
        "id": "ECO-E1-0728-1", "fonte_ref": "E1-0728", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": "No modelo de Solow, o PIB per capita é função crescente da razão capital / trabalho.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Solow, o PIB per capita é função <u>crescente</u> da razão capital / "
                      "trabalho."),
        "poucas": ("Com retornos constantes de escala, Y = F(K, L) vira " + vd("y = f(k)") + ", com "
                   + vd("f′(k) > 0") + ": mais capital por trabalhador, mais produto por trabalhador — a taxas "
                   "decrescentes (f″ &lt; 0)."),
        "destrinchando": [
            "Passagem para a forma intensiva: como F tem " + azb("retornos constantes de escala") + ", "
            "F(K, L)/L = F(K/L, 1), isto é, " + vd("y = f(k)") + ". O produto por trabalhador depende só do "
            "capital por trabalhador (dada a tecnologia).",
            "Propriedades de f: crescente (f′ > 0) e côncava (f″ &lt; 0, " + azb("rendimentos marginais "
                                                                                "decrescentes") + "); "
            "condições de Inada (f′ → ∞ quando k → 0; f′ → 0 quando k → ∞). Exemplo: y = k<sup>α</sup>, "
            "0 &lt; α &lt; 1.",
            "“Crescente” não significa “proporcional”: dobrar k aumenta y menos que o dobro. É essa concavidade "
            "que leva ao estado estacionário e à convergência.",
            "Simplificação de nomenclatura: o modelo fala em produto <b>por trabalhador</b>; o item usa “PIB per "
            "capita”, equivalente quando a participação da força de trabalho na população é constante.",
        ],
        "dissecando": (cz("[literalidade]") + " Propriedade básica da função de produção intensiva. A banca "
                       "costuma inverter trocando “crescente” por “crescente a taxas crescentes” ou "
                       "“proporcional”, ou dizendo que, por ser crescente, o acúmulo de capital sustenta "
                       "crescimento indefinido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, o PIB per capita cresce proporcionalmente à razão capital/trabalho.”</i> → "
            "ERRADO (rendimentos marginais decrescentes: cresce menos que proporcionalmente)",
            "<i>“No modelo de Solow, o produto marginal do capital diminui à medida que aumenta a razão "
            "capital/trabalho.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Certo: o produto per capita depende do capital por trabalhador; quanto maior k, "
                             "maior a produtividade e o produto per capita (aprofundamento do capital até o "
                             "estado estacionário)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0730
    {
        "id": "ECO-E1-0730-1", "fonte_ref": "E1-0730", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado 07/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Uma das críticas ao modelo de crescimento de Solow é que ele não é capaz de explicar a "
                      "relação entre as taxas de poupança e investimento e o crescimento econômico. Neste modelo, a "
                      "taxa de investimento não afeta a taxa de crescimento equilibrado, restringindo seu efeito ao "
                      "nível de renda de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma das críticas ao modelo de crescimento de Solow é que ele não é capaz de explicar a "
                      "relação entre as taxas de poupança e investimento e o crescimento econômico. Neste modelo, a "
                      "taxa de investimento <u>não afeta a taxa de crescimento equilibrado</u>, restringindo seu "
                      "efeito ao <u>nível de renda</u> de equilíbrio."),
        "poucas": ("Em Solow, a taxa de investimento (= poupança) tem só " + azb("efeito nível") + ". Os dados, "
                   "porém, mostram correlação entre investimento e crescimento de longo prazo — daí a crítica que "
                   "motivou os modelos de " + azb("crescimento endógeno") + "."),
        "destrinchando": [
            "Resultado do modelo: na trajetória de crescimento equilibrado, y cresce à taxa " + vd("g")
            + " (exógena), qualquer que seja s. Uma taxa de investimento maior leva a um k* e a um y* maiores, "
            "com crescimento mais rápido só durante a transição.",
            "A crítica: o crescimento de longo prazo fica explicado por uma variável que o próprio modelo não "
            "explica (g “cai do céu”), e a poupança — o que o modelo de fato modela — não influencia esse "
            "crescimento. Empiricamente, países com investimento alto por décadas (Leste Asiático) cresceram "
            "mais por décadas.",
            "Respostas teóricas: modelo " + azb("AK") + " (capital em sentido amplo, sem rendimentos "
            "decrescentes: g = s·A − δ, logo s afeta a taxa); " + oc("Romer") + " (1986 e 1990) e "
            + oc("Lucas") + " (1988), com externalidades, ideias e capital humano.",
            "Outra crítica de linhagem keynesiana, presente na fonte: Solow supõe que toda poupança vira "
            "investimento produtivo, sem problema de demanda efetiva — a hipótese que " + oc("Harrod") + " e "
            + oc("Domar") + " não faziam.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " A 1ª frase parece exagerada (“não é capaz de "
                       "explicar a relação”), mas a 2ª a delimita: a relação que falta é com a <b>taxa</b> de "
                       "crescimento equilibrado. Quem lê só a 1ª e lembra que Solow liga poupança a renda marca "
                       "ERRADO. A banca inverteria dizendo que o investimento afeta a taxa equilibrada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, a taxa de investimento eleva permanentemente a taxa de crescimento "
            "equilibrado.”</i> → ERRADO (efeito nível tratado como efeito crescimento)",
            "<i>“No modelo AK, a taxa de poupança afeta a taxa de crescimento de longo prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Certo: em Solow a poupança é exógena e toda poupança vira investimento; o "
                             "investimento não afeta a taxa de crescimento equilibrado, só o nível de renda; "
                             "crítica keynesiana sobre poupança × investimento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0732
    {
        "id": "ECO-E1-0732-1", "fonte_ref": "E1-0732", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DANIEL,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o modelo neoclássico de Solow, um aumento da taxa de poupança faz a economia crescer "
                      "até que alcance o novo estado estacionário. Logo, políticas que aumentem a taxa de poupança "
                      "são eficazes para ampliar o PIB per capita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o modelo neoclássico de Solow, um aumento da taxa de poupança faz a economia crescer "
                      "<u>até que alcance o novo estado estacionário</u>. Logo, políticas que aumentem a taxa de "
                      "poupança são eficazes para ampliar o <u>PIB per capita</u>."),
        "poucas": ("Alta de s → crescimento " + azb("transitório") + " até um k* maior → " + vd("PIB per capita "
                   "de estado estacionário maior") + ". A política funciona para o <b>nível</b>, não para a "
                   "taxa de crescimento de longo prazo."),
        "destrinchando": [
            DINAMICA,
            "Com s maior, s·f(k) supera (n + δ)k, o capital por trabalhador cresce e y cresce junto, até o novo "
            "estado estacionário. Ali, " + vd("y* = f(k*)") + " está mais alto, permanentemente.",
            "O “Logo” é válido porque a conclusão fala em <b>ampliar o PIB per capita</b> (nível), e não em "
            "elevar a taxa de crescimento de longo prazo — esta continua dada pelo progresso técnico e pelo "
            "crescimento populacional, exógenos.",
            "Ressalva útil: PIB per capita maior não é o mesmo que bem-estar maior. Se a economia já poupa acima "
            "da " + azb("regra de ouro") + ", elevar s aumenta y, mas reduz o " + azb("consumo") + " per capita "
            "de estado estacionário. E, na transição, o consumo cai primeiro.",
            "Exemplos de política de poupança discutidos no " + rx("Brasil") + ": previdência de capitalização, "
            "incentivos fiscais à poupança de longo prazo e redução do déficit público (poupança do governo).",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Frase-padrão do modelo seguida de uma "
                       "conclusão bem delimitada: “ampliar o PIB per capita” (nível). A armadilha seria ler "
                       "“eficazes” como efeito permanente sobre o crescimento. A banca inverteria com “elevar "
                       "permanentemente a taxa de crescimento”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…Logo, políticas que aumentem a taxa de poupança são eficazes para elevar permanentemente a "
            "taxa de crescimento do PIB per capita.”</i> → ERRADO (efeito apenas de nível)",
            "<i>“…Logo, políticas que aumentem a taxa de poupança sempre elevam o consumo per capita de longo "
            "prazo.”</i> → ERRADO (modulador absoluto: acima da regra de ouro, o consumo cai)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["Logo"], "dificuldade": 1,
        "comentario_fonte": ("Certo (verso com imagem não preservada e link para o canal do Telegram); nota: "
                             "tecnologia e crescimento da mão de obra são variáveis exógenas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (238).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (não preservada; comentário escrito a partir do conteúdo)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0734
    {
        "id": "ECO-E1-0734-1", "fonte_ref": "E1-0734", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DANIEL,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Solow é uma Teoria Neoclássica que descreve como a taxa de crescimento na "
                      "economia é instável e resultado de uma combinação de três forças principais: a tecnologia, o "
                      "capital e o trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo de Solow é uma Teoria Neoclássica que descreve como a taxa de crescimento na "
                       "economia é ") + vm("instável") + az(" e resultado de uma combinação de três forças "
                                                           "principais: a tecnologia, o capital e o trabalho.")),
        "poucas": ("Solow mostra exatamente o contrário: o crescimento é " + azb("estável") + " — a economia "
                   "converge automaticamente para o estado estacionário. Instabilidade (“fio da navalha”) é a "
                   "conclusão de " + oc("Harrod") + "-" + oc("Domar") + "."),
        "destrinchando": [
            "Em " + oc("Harrod") + " (1939) e " + oc("Domar") + " (1946), a produção usa capital e trabalho em "
            "proporções fixas. O crescimento equilibrado exige que a taxa garantida (s/v) coincida com a taxa "
            "natural (n): coincidência improvável, e qualquer desvio se acumula — o " + azb("fio da navalha")
            + ".",
            oc("Solow") + " (1956) e " + oc("Swan") + " (1956) introduzem " + azb("substituição entre fatores")
            + " e rendimentos marginais decrescentes. Se k está abaixo de k*, o investimento supera o necessário "
            "e k sobe; se está acima, k cai. O estado estacionário é " + vd("globalmente estável") + ".",
            "A segunda parte do item está certa: em Solow, o produto resulta de capital, trabalho e tecnologia "
            "(Y = F(K, A·L)) — os mesmos três componentes da contabilidade do crescimento.",
            vm("Regra-âncora: Harrod-Domar = instável (fio da navalha); Solow = estável (convergência para o "
               "estado estacionário)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Um adjetivo errado num item que, de resto, descreve bem o "
                       "modelo. A troca atribui a Solow a marca do modelo que ele veio corrigir. Pista: "
                       "“neoclássico” em crescimento evoca ajuste automático e estabilidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Harrod-Domar descreve uma trajetória de crescimento equilibrado instável, conhecida "
            "como fio da navalha.”</i> → CERTO",
            "<i>“O modelo de Solow supõe proporções fixas entre capital e trabalho.”</i> → ERRADO (troca de "
            "modelo: proporções fixas são de Harrod-Domar)",
        ])],
        "reescrita": ("O modelo de Solow é uma Teoria Neoclássica que descreve como a taxa de crescimento na "
                      "economia é " + hl("estável") + " e resultado de uma combinação de três forças principais: a "
                      "tecnologia, o capital e o trabalho."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Errado (verso com imagem não preservada e links para o canal do Telegram).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (241).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (não preservada; comentário escrito a partir do conteúdo)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0735
    {
        "id": "ECO-E1-0735-1", "fonte_ref": "E1-0735", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DANIEL,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, o aumento da taxa de poupança faz a economia crescer até que alcance o "
                      "novo estado estacionário. Assim, a acumulação de capital é a poupança descontada da taxa de "
                      "depreciação e a taxa de poupança é o principal determinante do estoque de capital no estado "
                      "estacionário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Solow, o aumento da taxa de poupança faz a economia crescer até que alcance o "
                      "novo estado estacionário. Assim, a acumulação de capital é <u>a poupança descontada da "
                      "taxa de depreciação</u> e a taxa de poupança é o <u>principal determinante</u> do estoque "
                      "de capital no estado estacionário."),
        "poucas": ("ΔK = s·Y − δK: a acumulação é a " + azb("poupança menos a depreciação") + ". E, no estado "
                   "estacionário, " + vd("k* = [s·A/(n + δ)]<sup>1/(1−α)</sup>") + ": a poupança é o parâmetro "
                   "que o modelo destaca como determinante de k*."),
        "destrinchando": [
            "Lei de movimento do capital: " + vd("ΔK = s·Y − δK") + " (agregado) ou " + vd("Δk = s·f(k) − "
                                                                                          "(n + δ)k")
            + " (por trabalhador, em que o crescimento populacional funciona como uma depreciação adicional). O "
            "item usa a versão simples, sem n: correta.",
            "No estado estacionário, s·f(k*) = (n + δ)k*. Com Cobb-Douglas, k* cresce com s e cai com n e δ. "
            "“Principal determinante” é a leitura didática de " + oc("Mankiw") + ": a poupança é o canal pelo qual "
            "as escolhas de uma sociedade mudam o capital (e a renda) de longo prazo.",
            "Exemplos usados nos manuais: Japão e Alemanha do pós-guerra, com poupança alta, convergiram para "
            "estados estacionários elevados; diferenças de taxa de investimento ajudam a explicar diferenças de "
            "renda per capita entre países.",
            "Limite do argumento: o efeito da poupança é sobre o " + azb("nível") + " de k* e y*; a taxa de "
            "crescimento de longo prazo continua dada pelo progresso técnico.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Três afirmações encadeadas, todas do manual. O ponto de "
                       "hesitação é o “principal determinante”, que soa como juízo de valor: no modelo, s é o "
                       "deslocador central de k* (ao lado de n e δ). A banca inverteria dizendo que a acumulação é "
                       "o consumo descontado da depreciação, ou que s é irrelevante para k*."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a taxa de poupança é irrelevante para o estoque de capital no estado estacionário, que depende "
            "apenas da tecnologia.”</i> → ERRADO (restrição indevida: s, n e δ também determinam k*)",
            "<i>“…um aumento da depreciação eleva o estoque de capital de estado estacionário.”</i> → ERRADO "
            "(sinal trocado: δ maior reduz k*)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["principal"], "dificuldade": 1,
        "comentario_fonte": "Certo (verso com imagem não preservada e link para o canal do Telegram).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (252).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (não preservada; comentário escrito a partir do conteúdo)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0737
    {
        "id": "ECO-E1-0737-1", "fonte_ref": "E1-0737", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow sem progresso tecnológico, uma vez que, no longo prazo, a taxa de "
                      "crescimento do produto per capita é igual à taxa de crescimento populacional, países com "
                      "maior crescimento da população tendem a ter maior nível de renda per capita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow sem progresso tecnológico, ") + vm("uma vez que")
                    + az(", no longo prazo, a taxa de crescimento do produto ") + vm("per capita é")
                    + az(" igual à taxa de crescimento populacional, países com maior crescimento da população "
                         "tendem a ter ") + vm("maior") + az(" nível de renda per capita.")),
        "poucas": ("Dois erros: no longo prazo, quem cresce à taxa n é o produto " + azb("agregado") + " (o per "
                   "capita fica constante); e n maior <b>reduz</b> o capital e a renda per capita de estado "
                   "estacionário."),
        "destrinchando": [
            "Sem progresso técnico, no estado estacionário k e y são constantes: " + vd("g(y) = 0") + ". Como "
            "Y = y·L e L cresce a n, " + vd("g(Y) = n") + ". A 1ª parte troca o agregado pelo per capita.",
            "Efeito de n sobre o nível: a reta de investimento necessário (n + δ)k fica mais inclinada, cruza "
            "s·f(k) num " + vd("k* menor") + " e, portanto, " + vd("y* menor") + ". Cada trabalhador novo "
            "precisa ser equipado, e a mesma poupança se espalha por mais gente (diluição do capital).",
            "Implicação empírica destacada por " + oc("Mankiw, Romer e Weil") + " (1992): países com crescimento "
            "populacional alto tendem a ser mais pobres, controlada a poupança.",
            "Resumo das taxas sem tecnologia: Y e K crescem a n; y, k e c, a zero. Com tecnologia: Y e K a "
            "n + g; y, k e c a g.",
            vm("Regra-âncora: n ↑ → k* ↓ e y* ↓ (nível per capita menor), mas crescimento agregado ↑."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " A 1ª oração parece certa “por um detalhe”: a "
                       "taxa n vale para o produto, não para o produto per capita. Sobre essa premissa trocada, o "
                       "item tira uma conclusão de sinal invertido. Pista: em Solow, “mais população” só pode "
                       "aparecer com sinal negativo no nível per capita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow sem progresso tecnológico, no longo prazo, o produto agregado cresce à taxa "
            "de crescimento populacional, e o produto per capita é constante.”</i> → CERTO",
            "<i>“Um aumento da taxa de crescimento populacional eleva o capital por trabalhador de estado "
            "estacionário.”</i> → ERRADO (sinal trocado: reduz k*)",
        ])],
        "reescrita": ("No modelo de Solow sem progresso tecnológico, " + hl("embora") + ", no longo prazo, a taxa "
                      "de crescimento do produto " + hl("agregado seja") + " igual à taxa de crescimento "
                      "populacional, países com maior crescimento da população tendem a ter " + hl("menor")
                      + " nível de renda per capita."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("É o contrário: n maior leva a estado estacionário com menos capital per capita; e a "
                             "taxa n é a do produto, não do produto per capita, que fica constante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00578-1 (mesmo mecanismo: n maior reduz k* e eleva o crescimento "
                    "agregado)"],
    },
    # ------------------------------------------------------------------ E1-0738
    {
        "id": "ECO-E1-0738-1", "fonte_ref": "E1-0738", "destino": "56", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("Se um país tem um estoque de capital per capita abaixo do nível da regra de ouro, então este "
                      "país precisa elevar sua taxa de poupança para elevar o consumo per capita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um país tem um estoque de capital per capita <u>abaixo</u> do nível da regra de ouro, "
                      "então este país precisa <u>elevar</u> sua taxa de poupança para elevar o consumo per "
                      "capita."),
        "poucas": ("Abaixo de k ouro, falta capital: elevar s leva a um k* maior, mais perto de k ouro, onde o "
                   + azb("consumo per capita de estado estacionário") + " é máximo. Poupa-se mais (propensão a "
                   "consumir menor), mas consome-se mais (nível de consumo maior)."),
        "destrinchando": [
            "Consumo de estado estacionário: " + vd("c* = f(k*) − (n + δ)k*") + ". Ele é máximo em "
            + vd("f′(k ouro) = n + δ") + " (regra de ouro de " + oc("Phelps") + ", 1961). À esquerda de k ouro, "
            "f′(k) > n + δ: uma unidade a mais de capital rende mais do que custa mantê-la, e c* sobe com k*.",
            "Logo, se k* &lt; k ouro, a única forma de aumentar c* é elevar k*, e a única forma de elevar k* (com "
            "n, δ e tecnologia dados) é " + azb("elevar s") + ". Com Cobb-Douglas, s ouro = α (a participação do "
            "capital na renda).",
            "Distinção que confunde: a " + azb("propensão a consumir") + " (1 − s) cai, mas o " + azb("consumo")
            + " por trabalhador sobe, porque y cresce mais que proporcionalmente à fatia perdida.",
            "Custo de transição: no momento da alta de s, o consumo <b>cai</b> (y ainda não mudou e a fatia "
            "consumida diminuiu); só depois, com a acumulação, supera o nível antigo. Por isso a decisão envolve "
            "sacrificar gerações presentes em favor das futuras.",
            "Simetria: acima de k ouro (" + azb("ineficiência dinâmica") + "), reduzir s eleva o consumo já e "
            "em todas as datas futuras.",
        ],
        "grafico_verso": "ECO-E1-0738-1-V1",
        "dissecando": (cz("[contraintuitivo]") + " “Poupar mais para consumir mais” parece paradoxal, e quem "
                       "pensa na propensão a consumir marca ERRADO. O verbo “precisa” é correto para o longo "
                       "prazo: abaixo de k ouro, não há outro caminho para aumentar c*. A banca inverteria com "
                       "“acima do nível da regra de ouro”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se um país tem estoque de capital per capita acima do nível da regra de ouro, ele precisa elevar "
            "sua taxa de poupança para elevar o consumo per capita.”</i> → ERRADO (inversão: acima de k ouro, "
            "deve reduzir a poupança)",
            "<i>“Ao elevar a poupança abaixo da regra de ouro, o consumo per capita aumenta já no período "
            "imediatamente seguinte.”</i> → ERRADO (o consumo cai primeiro e só depois supera o nível inicial)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["precisa"], "dificuldade": 2,
        "comentario_fonte": ("Para chegar à regra de ouro, é preciso subir a poupança de S1 para S2; reduz-se a "
                             "propensão a consumir, mas aumenta o consumo per capita, porque o produto per capita "
                             "cresce (com gráfico de aula)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "macro_aula_7-05.png, image (262).png", "tipo_fonte": "GRÁFICO",
                           "lado": "verso", "acao": "irrecuperavel (não preservadas; redesenho didático em "
                                                    "ECO-E1-0738-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0739
    {
        "id": "ECO-E1-0739-1", "fonte_ref": "E1-0739", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow com progresso tecnológico, o equilíbrio de longo prazo se dará com uma "
                      "taxa de crescimento do produto per capita igual à taxa de progresso tecnológico mais a taxa "
                      "de crescimento populacional, se não houver depreciação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow com progresso tecnológico, o equilíbrio de longo prazo se dará com uma "
                       "taxa de crescimento do produto per capita igual à taxa de progresso tecnológico ")
                    + vm("mais a taxa de crescimento populacional, se não houver depreciação") + az(".")),
        "poucas": ("O produto " + azb("per capita") + " cresce só a " + vd("g") + "; quem cresce a "
                   + vd("n + g") + " é o produto " + azb("agregado") + ". E a depreciação não altera taxas de "
                   "crescimento de longo prazo, só o nível de k̃*."),
        "destrinchando": [
            "Com Y = F(K, A·L), o estado estacionário fixa " + vd("k̃ = K/(A·L)") + " e ỹ = Y/(A·L). Como "
            "Y = ỹ·A·L, com ỹ constante: " + vd("g(Y) = g + n") + ". Dividindo por L: " + vd("g(Y/L) = g")
            + ".",
            "Quadro-resumo das taxas no estado estacionário: k̃ e ỹ → 0; K/L e Y/L → g; K e Y → n + g.",
            "A depreciação δ entra só na reta (n + g + δ)k̃: quanto maior δ, mais inclinada a reta e menor k̃* "
            "(efeito nível). Nenhuma taxa de crescimento de longo prazo depende de δ — por isso a condição “se "
            "não houver depreciação” é irrelevante e não salva o item.",
            "Erro clássico: somar n porque “mais gente produz mais”. Mais gente aumenta o produto total, mas, "
            "dividido por cabeça, o efeito se anula.",
            vm("Regra-âncora: per capita cresce a g; agregado cresce a n + g; δ não muda taxas, só níveis."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Erro “por um pequeno detalhe”: a taxa "
                       "n + g é verdadeira para o produto agregado e foi colada no per capita. A condição final "
                       "(“se não houver depreciação”) é um distrator que dá aparência de rigor técnico a algo que "
                       "não depende de δ."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow com progresso tecnológico, o equilíbrio de longo prazo se dará com uma taxa "
            "de crescimento do produto agregado igual à taxa de progresso tecnológico mais a taxa de crescimento "
            "populacional.”</i> → CERTO",
            "<i>“…uma taxa de depreciação mais alta reduz a taxa de crescimento de longo prazo do produto per "
            "capita.”</i> → ERRADO (δ afeta só o nível de k̃*)",
        ])],
        "reescrita": ("No modelo de Solow com progresso tecnológico, o equilíbrio de longo prazo se dará com uma "
                      "taxa de crescimento do produto per capita igual à taxa de progresso tecnológico"
                      + hl(", haja ou não depreciação") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["se"], "dificuldade": 2,
        "comentario_fonte": ("Errado por um detalhe: o produto agregado (Y) cresce a n + g; o per capita, só a g. A "
                             "depreciação não muda as taxas de longo prazo, só o nível do capital por trabalhador "
                             "(várias respostas de IA convergentes)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00151
    {
        "id": "ECO-E2-L00151-1", "fonte_ref": "E2-L00151", "destino": "56", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("No contexto do modelo de Solow, o ponto de ouro no estado estacionário é onde a economia "
                      "maximiza seu nível de consumo, sendo este ponto alcançado no ponto estacionário máximo, em "
                      "que a taxa de investimento per capita se iguala à taxa de depreciação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No contexto do modelo de Solow, o ponto de ouro no estado estacionário é onde a economia "
                       "maximiza seu nível de consumo, sendo este ponto alcançado ")
                    + vm("no ponto estacionário máximo, em que a taxa de investimento per capita se iguala à taxa "
                         "de depreciação") + az(".")),
        "poucas": ("Investimento = depreciação (efetiva) vale em <b>todo</b> estado estacionário. A regra de ouro "
                   "é o estado estacionário em que " + vd("f′(k) = n + δ") + " — e não o de capital "
                   "“máximo”."),
        "destrinchando": [
            "Dinâmica de " + oc("Solow") + " (1956): Δk = s·f(k) − (n + δ)k. No " + azb("estado estacionário")
            + " k*, o investimento por trabalhador cobre exatamente a depreciação e a diluição pelo crescimento "
            "populacional: " + vd("s·f(k*) = (n + δ)k*") + ". Há um k* para cada taxa de poupança s.",
            "Consumo de estado estacionário: c* = f(k*) − (n + δ)k*. Maximizando em k*: "
            + vd("f′(k ouro) = n + δ") + " (com progresso técnico, n + g + δ). É a " + azb("regra de ouro")
            + " de " + oc("Phelps") + " (1961): a inclinação da função de produção iguala a da reta de "
            "investimento necessário.",
            "O “ponto estacionário máximo” (s = 100%) é o pior possível: todo o produto vai para investimento e "
            "o consumo é zero. Poupar acima de s ouro leva à " + azb("ineficiência dinâmica") + ": capital "
            "demais, consumo de menos, e reduzir s elevaria o consumo em todas as datas.",
            "Na Cobb-Douglas f(k) = k<sup>α</sup>, a regra de ouro dá " + vd("s ouro = α") + " (a participação "
            "do capital na renda).",
        ],
        "grafico_verso": "ECO-E2-L00151-1-V1",
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A primeira oração é a definição correta "
                       "(maximiza o consumo); o erro foi enxertado na condição, que é a de <b>qualquer</b> estado "
                       "estacionário, e no “máximo”, que sugere mais capital = melhor. Pista: a condição oferecida "
                       "não envolve a inclinação de f(k)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No estado estacionário de regra de ouro, o produto marginal do capital iguala a soma das taxas "
            "de crescimento populacional e de depreciação.”</i> → CERTO",
            "<i>“Se a poupança supera a de regra de ouro, reduzi-la diminui o consumo no curto prazo.”</i> → "
            "ERRADO (inversão: aumenta o consumo já e no longo prazo)",
        ])],
        "reescrita": ("No contexto do modelo de Solow, o ponto de ouro no estado estacionário é onde a economia "
                      "maximiza seu nível de consumo, sendo este ponto alcançado " + hl("no estado estacionário em "
                      "que o produto marginal do capital se iguala à soma das taxas de depreciação e de "
                      "crescimento populacional") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["máximo"], "dificuldade": 2,
        "comentario_fonte": ("Investimento = depreciação efetiva vale em todo estado estacionário; a regra de ouro "
                             "exige f′(k) = n + g + δ (Phelps). O primeiro comentário da fonte erra ao dizer que, "
                             "no ponto de ouro, o investimento “é superior” à depreciação mais o crescimento "
                             "populacional."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 011", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00151-1-V1)"},
                          {"ref": "IMAGEM 012", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (ineficiência dinâmica, no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00152
    {
        "id": "ECO-E2-L00152-1", "fonte_ref": "E2-L00152", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo de Solow, a poupança, mesmo sendo uma ferramenta crucial para o "
                      "financiamento do capital, não é suficiente para sustentar o crescimento econômico no "
                      "longuíssimo prazo se não for acompanhada de outros elementos como o avanço tecnológico e o "
                      "controle do crescimento populacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando o modelo de Solow, a poupança, mesmo sendo uma ferramenta crucial para o "
                      "financiamento do capital, <u>não é suficiente</u> para sustentar o crescimento econômico no "
                      "longuíssimo prazo se não for acompanhada de outros elementos como o avanço tecnológico e o "
                      "controle do crescimento populacional."),
        "poucas": ("Por causa dos " + azb("rendimentos marginais decrescentes") + ", a poupança sozinha leva a "
                   "economia a um estado estacionário em que o crescimento per capita cessa. Só o "
                   + azb("progresso técnico") + " sustenta crescimento per capita indefinidamente."),
        "destrinchando": [
            "A poupança financia o investimento e eleva k* e y* (efeito nível). Mas, com f(k) côncava, cada "
            "unidade adicional de capital rende menos; em k*, a poupança só repõe o desgaste e equipa os novos "
            "trabalhadores, e y para de crescer.",
            "Para que y cresça sempre, é preciso deslocar a função de produção para cima continuamente — o que só "
            "o progresso técnico (A crescendo à taxa g) faz. No estado estacionário com tecnologia, "
            + vd("y cresce a g") + ".",
            "E a população? Em Solow, um crescimento populacional " + azb("menor") + " eleva k* e y* (menos "
            "diluição do capital), mas é efeito de nível, não fonte de crescimento sustentado. A menção a "
            "“controle do crescimento populacional” é, portanto, imprecisa como motor de longo prazo, embora "
            "ajude a renda per capita.",
            "O resultado é a principal conclusão de política do modelo: sem inovação, a acumulação de capital "
            "tem limite.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O núcleo (“não é suficiente”) é o "
                       "resultado central de Solow, e o “como” da lista (“outros elementos como…”) deixa a "
                       "enumeração aberta. A inclusão do controle populacional é frouxa (afeta nível, não taxa), "
                       "mas não inverte o item. A banca o tornaria ERRADO dizendo que a poupança <b>basta</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Considerando o modelo de Solow, a elevação contínua da poupança é suficiente para sustentar o "
            "crescimento do produto per capita no longuíssimo prazo.”</i> → ERRADO (rendimentos decrescentes "
            "esgotam o efeito)",
            "<i>“No modelo de Solow, uma taxa de crescimento populacional menor eleva a taxa de crescimento de "
            "longo prazo do produto per capita.”</i> → ERRADO (afeta só o nível de y*)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["não é suficiente", "como"],
        "dificuldade": 1,
        "comentario_fonte": ("No longuíssimo prazo, poupança não basta; são cruciais o avanço tecnológico e o "
                             "manejo do crescimento populacional para evitar a estagnação no estado "
                             "estacionário."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00153
    {
        "id": "ECO-E2-L00153-1", "fonte_ref": "E2-L00153", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Os resíduos do modelo de Solow, que incluem elementos como o crescimento populacional e o "
                      "avanço tecnológico. Estes elementos são determinados dentro do próprio modelo e diretamente "
                      "influenciam a criação de tecnologia e inovação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os resíduos do modelo de Solow, que incluem elementos como ")
                    + vm("o crescimento populacional e") + az(" o avanço tecnológico. Estes elementos são ")
                    + vm("determinados dentro do próprio modelo e diretamente influenciam a criação de tecnologia "
                         "e inovação") + az(".")),
        "poucas": ("Em Solow, o progresso técnico (e também o crescimento populacional) é " + azb("exógeno")
                   + ": dado de fora, não explicado pelo modelo. E o " + azb("resíduo") + " é a parte do "
                   "crescimento não explicada por capital e trabalho — a população, que é trabalho, não entra "
                   "nele."),
        "destrinchando": [
            "Variáveis exógenas de Solow: s, n, δ e g. O modelo explica a acumulação de capital e a trajetória "
            "de k e y, mas não por que as pessoas poupam, por que a população cresce ou de onde vem a "
            "tecnologia.",
            azb("Resíduo de Solow") + " (contabilidade do crescimento, 1957): " + vd("g_A = g_Y − α·g_K − "
                                                                                     "(1 − α)·g_L") + ". "
            "O crescimento da força de trabalho é um dos termos <b>descontados</b>; o resíduo é a "
            + azb("produtividade total dos fatores") + ", lida como progresso técnico.",
            "Criar tecnologia dentro do modelo é a proposta do " + azb("crescimento endógeno") + ": "
            + oc("Romer") + " (1990), com P&amp;D e ideias não rivais; " + oc("Lucas") + " (1988), com capital "
            "humano.",
            "A limitação apontada no item é real — Solow não diz nada sobre a origem da inovação —, mas o item a "
            "descreve como se fosse uma virtude do modelo.",
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " O núcleo do erro é exógeno × endógeno (“determinados "
                       "dentro do próprio modelo”). Há também um deslize conceitual: chamar o crescimento "
                       "populacional de “resíduo”. A redação truncada (oração sem verbo principal) é da fonte; "
                       "o julgamento se faz pela 2ª frase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, o progresso tecnológico e o crescimento populacional são exógenos.”</i> → "
            "CERTO",
            "<i>“O resíduo de Solow mede a contribuição do crescimento da força de trabalho para o crescimento "
            "do produto.”</i> → ERRADO (troca de conceito: o trabalho é descontado; o resíduo é a PTF)",
        ])],
        "reescrita": ("Os resíduos do modelo de Solow, que incluem elementos como " + hl("ganhos de eficiência e")
                      + " o avanço tecnológico. Estes elementos são " + hl("exógenos: o modelo não explica a "
                                                                           "criação de tecnologia e inovação")
                      + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": ["diretamente"], "dificuldade": 1,
        "comentario_fonte": ("Os resíduos, incluindo crescimento populacional e avanço tecnológico, são exógenos; "
                             "Solow não explica como são gerados — limitação do modelo (o comentário repete o "
                             "deslize de tratar a população como resíduo)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00154
    {
        "id": "ECO-E2-L00154-1", "fonte_ref": "E2-L00154", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O crescimento populacional pode aumentar o crescimento econômico absoluto; contudo, conforme "
                      "o próprio Solow analisa, ele pode levar a uma maior depreciação do parque industrial se não "
                      "for acompanhado por investimento correspondente em capital, devido ao desgaste das "
                      "máquinas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O crescimento populacional pode aumentar o crescimento econômico absoluto; contudo, conforme "
                      "o próprio Solow analisa, ele pode levar a uma <u>maior depreciação do parque industrial</u> "
                      "se não for acompanhado por investimento correspondente em capital, <u>devido ao desgaste "
                      "das máquinas</u>."),
        "poucas": ("A fonte dá CERTO pela ideia de que, em Solow, o crescimento populacional funciona como uma "
                   + azb("depreciação efetiva") + " do capital por trabalhador. Mas o mecanismo é a "
                   + azb("diluição") + " do capital entre mais trabalhadores, não o desgaste físico das "
                   "máquinas."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Mantido o CERTO da fonte. A primeira oração está correta (n maior → produto agregado "
                          "cresce mais depressa). A segunda, porém, descreve um mecanismo que Solow não propõe: no "
                          "modelo, a depreciação física δ é um parâmetro fixo, que não depende da população; o que "
                          "n faz é " + vm("diluir o capital por trabalhador") + " — por isso aparece somado a δ "
                          "em (n + δ)k e é chamado, por analogia, de “depreciação efetiva”. Atribuir a Solow um "
                          "“desgaste das máquinas” causado pela população é uma leitura literal indevida da "
                          "analogia; uma banca rigorosa daria ERRADO.")],
        "destrinchando": [
            DINAMICA,
            "O termo nk mede quanto capital é preciso para dar aos novos trabalhadores o mesmo k dos antigos. Se "
            "o investimento não cobre (n + δ)k, o capital <b>por trabalhador</b> cai, mesmo que nenhuma máquina "
            "se desgaste mais depressa: o mesmo estoque é dividido por mais gente.",
            "Por isso n e δ entram juntos na reta de investimento necessário e têm o mesmo efeito sobre o nível: "
            "n maior → reta mais inclinada → " + vd("k* e y* menores") + ". Daí a expressão “depreciação "
            "efetiva” (n + δ).",
            "Efeito sobre o crescimento: no estado estacionário, o produto agregado cresce a " + vd("n")
            + " (ou n + g); logo, n maior acelera o crescimento “absoluto”, enquanto o per capita depende só de g.",
            "Desgaste físico (δ) varia com o uso intensivo do capital no mundo real, mas no modelo é constante e "
            "independente de n.",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A 1ª oração é correta e a 2ª pega uma "
                       "analogia didática (n como “depreciação efetiva”) e a converte em mecanismo físico "
                       "(“desgaste das máquinas”), com o reforço de autoridade “conforme o próprio Solow analisa”. "
                       "O gabarito oficial aceitou a analogia; leia com cautela itens que dão causa física a um "
                       "termo de diluição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, o crescimento populacional reduz o capital por trabalhador de estado "
            "estacionário, pois dilui o estoque de capital entre mais trabalhadores.”</i> → CERTO",
            "<i>“No modelo de Solow, o crescimento populacional eleva o produto per capita de estado "
            "estacionário.”</i> → ERRADO (sinal trocado: n maior reduz y*)",
        ])],
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 3,
        "comentario_fonte": ("Solow argumenta que o crescimento populacional pode aumentar o PIB absoluto, mas, sem "
                             "investimento correspondente, sobrecarrega as máquinas e aumenta a depreciação do "
                             "parque industrial (mecanismo físico que o modelo não contém)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: em Solow, n dilui o capital por trabalhador (“depreciação efetiva” por "
                    "analogia); não há desgaste físico causado pela população — a resposta mais defensável seria "
                    "ERRADO; gabarito CERTO da fonte mantido"],
    },
    # ------------------------------------------------------------------ E2-L00524
    {
        "id": "ECO-E2-L00524-1", "fonte_ref": "E2-L00524", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Solow introduz a substitutibilidade entre capital e trabalho e a hipótese de "
                      "rendimentos marginais decrescentes para os fatores, o que cria um mecanismo de ajuste "
                      "automático que leva a economia a um estado estacionário de crescimento balanceado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo de Solow introduz a <u>substitutibilidade entre capital e trabalho</u> e a hipótese "
                      "de <u>rendimentos marginais decrescentes</u> para os fatores, o que cria um mecanismo de "
                      "ajuste automático que leva a economia a um estado estacionário de crescimento balanceado."),
        "poucas": ("É a inovação de Solow sobre " + oc("Harrod") + "-" + oc("Domar") + ": com "
                   + azb("substituição entre fatores") + " e " + azb("rendimentos decrescentes") + ", a relação "
                   "capital/trabalho se ajusta sozinha até o estado estacionário, que é estável."),
        "destrinchando": [
            "Em Harrod-Domar, a tecnologia é de " + azb("proporções fixas") + " (Leontief): a relação "
            "capital-produto v é constante. O crescimento equilibrado exige s/v = n, igualdade sem mecanismo que "
            "a garanta — o “fio da navalha”: um desvio gera desemprego crescente ou capital ocioso.",
            oc("Solow") + " (1956) usa uma função neoclássica, Y = F(K, L), com retornos constantes de escala, "
            "substituição entre K e L e PMg decrescentes. Agora v = K/Y é <b>endógena</b>: varia com k.",
            "Ajuste automático: se k &lt; k*, s·f(k) > (n + δ)k e k sobe; se k > k*, k cai. O estado "
            "estacionário é " + vd("globalmente estável") + ", e nele K, Y e L crescem à mesma taxa "
            "(crescimento balanceado).",
            "Pequeno reparo à fonte: no estado estacionário, o produto por trabalhador cresce à taxa do "
            "progresso técnico (g), e o produto agregado a n + g; sem tecnologia, y e k ficam constantes.",
        ],
        "dissecando": (cz("[literalidade]") + " Descrição de manual do que diferencia Solow de Harrod-Domar. "
                       "Todos os termos estão no lugar: substituição, rendimentos marginais (não de escala) "
                       "decrescentes, ajuste automático, crescimento balanceado. A banca inverteria com "
                       "“proporções fixas”, “rendimentos crescentes” ou “equilíbrio instável”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Solow supõe proporções fixas entre capital e trabalho, o que torna o crescimento "
            "equilibrado instável.”</i> → ERRADO (troca de modelo: isso é Harrod-Domar)",
            "<i>“O modelo de Solow supõe rendimentos decrescentes de escala.”</i> → ERRADO (troca de conceito: a "
            "escala é constante; os rendimentos marginais é que são decrescentes)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Solow difere de Harrod-Domar ao introduzir substituição entre capital e trabalho e "
                             "rendimentos marginais decrescentes, o que leva à convergência para o estado "
                             "estacionário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00525
    {
        "id": "ECO-E2-L00525-1", "fonte_ref": "E2-L00525", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, um aumento na taxa de poupança eleva o nível de produto por trabalhador "
                      "no estado estacionário, mas não afeta a taxa de crescimento de longo prazo da economia, que é "
                      "determinada exclusivamente pelo progresso tecnológico endógeno."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow, um aumento na taxa de poupança eleva o nível de produto por "
                       "trabalhador no estado estacionário, mas não afeta a taxa de crescimento de longo prazo da "
                       "economia, que é determinada exclusivamente pelo progresso tecnológico ")
                    + vm("endógeno") + az(".")),
        "poucas": ("Tudo certo até a última palavra: em Solow, o progresso tecnológico é " + azb("exógeno")
                   + ". Tecnologia endógena é a marca dos modelos de " + oc("Romer") + " e " + oc("Lucas") + "."),
        "destrinchando": [
            "Efeito da poupança: s ↑ → k* ↑ → " + vd("y* ↑") + " (efeito nível), com crescimento mais rápido só "
            "na transição. No longo prazo, y cresce à taxa " + vd("g") + ".",
            "Em Solow, g é um parâmetro: o modelo não explica de onde vem o progresso técnico. Empiricamente, ele "
            "aparece como o " + azb("resíduo de Solow") + " na contabilidade do crescimento.",
            azb("Crescimento endógeno") + ": " + oc("Romer") + " (1986, externalidades do conhecimento; 1990, "
            "P&amp;D e ideias não rivais), " + oc("Lucas") + " (1988, capital humano), modelo AK (sem "
            "rendimentos decrescentes do capital amplo). Nesses modelos, a própria poupança e as políticas podem "
            "alterar a taxa de longo prazo.",
            "Observação: a frase fala em “taxa de crescimento de longo prazo da economia”; no agregado, ela é "
            "n + g, e o “exclusivamente” só é exato para o per capita. Mas o erro que a banca quis cobrar está "
            "no adjetivo final.",
            vm("Regra-âncora: Solow = progresso técnico exógeno."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Clássica pegadinha de última palavra: um enunciado longo e "
                       "correto, com “endógeno” no lugar de “exógeno” no fim. Quem lê até “progresso "
                       "tecnológico” e já marca CERTO cai. 🔥 Exógeno × endógeno é a troca mais cobrada em "
                       "Solow."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…que é determinada exclusivamente pelo progresso tecnológico exógeno.”</i> → CERTO",
            "<i>“No modelo de Romer, a taxa de crescimento de longo prazo depende de decisões de investimento em "
            "P&amp;D.”</i> → CERTO",
        ])],
        "reescrita": ("No modelo de Solow, um aumento na taxa de poupança eleva o nível de produto por trabalhador "
                      "no estado estacionário, mas não afeta a taxa de crescimento de longo prazo da economia, que é "
                      "determinada exclusivamente pelo progresso tecnológico " + hl("exógeno") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": ("A taxa de crescimento de longo prazo é determinada pelo progresso tecnológico "
                             "exógeno, não endógeno."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0709-1 (mesma frase sem o adjetivo “endógeno”, CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L00526
    {
        "id": "ECO-E2-L00526-1", "fonte_ref": "E2-L00526", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Solow prevê a “convergência condicional”, ou seja, países com taxas de poupança, "
                      "crescimento populacional e progresso tecnológico semelhantes convergirão para o mesmo nível de "
                      "renda per capita de estado estacionário, independentemente de seu ponto de partida."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo de Solow prevê a “convergência condicional”, ou seja, países com taxas de poupança, "
                      "crescimento populacional e progresso tecnológico <u>semelhantes</u> convergirão para o mesmo "
                      "nível de renda per capita de estado estacionário, independentemente de seu ponto de "
                      "partida."),
        "poucas": ("Cada país converge para o " + azb("próprio") + " estado estacionário, definido por s, n, δ e "
                   "g. Mesmos fundamentos → mesmo destino, não importa de onde se parte: é a "
                   + azb("convergência condicional") + "."),
        "destrinchando": [
            "Mecanismo: com rendimentos decrescentes, quem tem pouco capital (longe do seu k*) cresce mais "
            "depressa; quem está perto do k* cresce devagar. Dois países com os mesmos parâmetros e pontos de "
            "partida diferentes acabam no mesmo k* e no mesmo y* (em unidades efetivas).",
            azb("Convergência absoluta") + " (incondicional): todos os países convergiriam para o mesmo nível, "
            "independentemente dos fundamentos. Solow <b>não</b> prevê isso, e os dados mundiais não a mostram — "
            "países pobres, em média, não crescem mais que os ricos.",
            "Evidência para a condicional: " + oc("Barro") + " e " + oc("Sala-i-Martin") + " (regiões dos EUA, "
            "Europa) e " + oc("Mankiw, Romer e Weil") + " (1992), que, controlando poupança, crescimento "
            "populacional e capital humano, encontram convergência entre países.",
            "Conceito vizinho: convergência " + azb("β") + " (pobres crescem mais rápido, condicionado ou não) × "
            "convergência " + azb("σ") + " (a dispersão das rendas cai ao longo do tempo).",
        ],
        "dissecando": (cz("[literalidade]") + " Definição correta, com a condição explícita (“semelhantes”). O "
                       "“independentemente de seu ponto de partida” assusta, mas está certo: o ponto de partida "
                       "afeta só a velocidade do caminho. A banca inverteria tirando a condição (“todos os "
                       "países”) — isso seria a convergência absoluta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Solow prevê que todos os países convergirão para o mesmo nível de renda per capita, "
            "independentemente de suas taxas de poupança e de crescimento populacional.”</i> → ERRADO "
            "(convergência absoluta, que o modelo não prevê)",
            "<i>“Entre dois países com os mesmos parâmetros, cresce mais rápido o que tem menor capital por "
            "trabalhador.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["independentemente"], "dificuldade": 1,
        "comentario_fonte": ("Países com características semelhantes (poupança, crescimento populacional, "
                             "depreciação, tecnologia) convergem para o mesmo estado estacionário, independentemente "
                             "do ponto de partida."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00578
    {
        "id": "ECO-E2-L00578-1", "fonte_ref": "E2-L00578", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": ("Em relação às teorias do crescimento econômico e às teorias do consumo, julgue o item a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Um aumento permanente na taxa de crescimento populacional, no Modelo de Solow, reduz o "
                      "estoque de capital por trabalhador no estado estacionário, mas pode aumentar a taxa de "
                      "crescimento do produto agregado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento permanente na taxa de crescimento populacional, no Modelo de Solow, "
                      "<u>reduz</u> o estoque de capital por trabalhador no estado estacionário, mas pode "
                      "<u>aumentar</u> a taxa de crescimento do produto <u>agregado</u>."),
        "poucas": ("n maior → reta " + vd("(n + δ)k") + " mais inclinada → " + vd("k* e y* menores")
                   + ". Mas, no estado estacionário, o produto agregado cresce a n (ou n + g): com n maior, "
                   "cresce mais depressa."),
        "destrinchando": [
            DINAMICA,
            "Alta de n: cada período chegam mais trabalhadores a equipar, e o investimento necessário sobe. A "
            "reta de investimento necessário gira para cima e cruza s·f(k) num " + vd("k* menor") + "; com ele, "
            "y* = f(k*) também cai.",
            "Taxas no novo estado estacionário: y e k per capita constantes (ou crescendo a g); " + vd("Y e K "
                                                                                                      "crescem a "
                                                                                                      "n + g")
            + ". Como n subiu, o agregado cresce mais rápido — com uma renda por pessoa menor.",
            "Na transição, há um efeito oposto passageiro: enquanto k cai em direção ao novo k*, y diminui, e o "
            "crescimento do agregado fica abaixo de n + g. Por isso o “pode” é prudente: o aumento vale para o "
            "novo estado estacionário.",
            "Implicação empírica: países com crescimento populacional alto tendem a ser mais pobres em renda per "
            "capita (" + oc("Mankiw, Romer e Weil") + ", 1992), ainda que seu PIB total cresça depressa.",
        ],
        "grafico_verso": "ECO-E2-L00578-1-V1",
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Combina dois efeitos de sinais opostos "
                       "(per capita ↓, agregado ↑), o que leva o candidato a achar que há contradição. A distinção "
                       "per capita × agregado e o “pode” resolvem. 🔥 A banca costuma trocar “agregado” por “per "
                       "capita” para tornar o item ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…reduz o estoque de capital por trabalhador no estado estacionário, mas aumenta a taxa de "
            "crescimento do produto per capita.”</i> → ERRADO (troca de conceito: o per capita cresce a g, "
            "independentemente de n)",
            "<i>“Um aumento permanente da taxa de poupança eleva o capital por trabalhador de estado "
            "estacionário.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("O aumento de n eleva a “depreciação efetiva”, desloca (n + δ)k para cima e reduz k* e "
                             "y*; no estado estacionário, Y cresce a n, então n maior implica crescimento maior "
                             "do agregado (com quatro gráficos do modelo de Solow)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 094", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (painel do aumento de n, em ECO-E2-L00578-1-V1; demais painéis "
                                   "absorvidos no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0737-1 (mesmo mecanismo: n maior reduz k* e y*)"],
    },
]
