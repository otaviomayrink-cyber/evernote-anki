"""Cards do lote de redação 02 — ECO, passada 03 (nota 56: modelo de Solow)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ee": "⚙️ Estado estacionário",
    "ouro": "🥇 Regra de ouro",
    "pop": "👥 População, tecnologia e convergência",
}

CMD_NAB_CRESC_CONS = ("Em relação às teorias do crescimento econômico e às teorias do consumo, julgue o item a "
                      "seguir.")
CMD_NAB_MOD_CRESC = "Em relação aos modelos de crescimento, julgue o item a seguir."
CMD_NAB_MACRO = "Em relação à macroeconomia, julgue o item a seguir."
CMD_NAB_MODELOS = "Em relação aos modelos macroeconômicos, julgue o item a seguir."
CMD_NAB_INTERTEMP = ("A respeito dos modelos de crescimento e da economia intertemporal, julgue o item a seguir.")
CMD_NAB_TEORIA_MACRO = "Em relação à teoria macroeconômica, julgue o item a seguir."
CMD_NAB_COM_REL = "Com relação às teorias do crescimento econômico, julgue o item a seguir."
CMD_NAB_TPS24 = "Em relação às teorias de crescimento econômico, julgue o item a seguir."
CMD_NAB_SOBRE = "Sobre teorias do crescimento econômico, julgue o item a seguir."
CMD_NAB_SOLOW = "Com base no modelo de Solow, julgue o item a seguir."
CMD_NAB_BASE_TEORIAS = "Com base nas teorias do crescimento econômico, julgue o item a seguir."
CMD_RT_POUP = ("Acerca da relação entre poupança e investimento e dos modelos de crescimento econômico, julgue o "
               "item a seguir.")
CMD_RT_CONSUMO = ("A respeito das relações entre consumo, poupança e crescimento econômico, julgue o item a "
                  "seguir.")
CMD_RT_DESENV = ("Com relação aos modelos e teorias de crescimento e desenvolvimento econômico, julgue o item a "
                 "seguir.")
CMD_RT_SOLOW = "Com base no modelo de Solow, julgue o item a seguir."

# trechos de aula reaproveitados (mesma regra-âncora em vários cards)
ANCORA_NIVEL = vm("Regra-âncora: no Solow, poupança, população e depreciação mudam o NÍVEL de longo prazo; só o "
                  "progresso técnico muda a TAXA de crescimento per capita de longo prazo.")
TAXAS_EE = ("Taxas de crescimento no estado estacionário com progresso técnico g (A cresce a g, L a n): "
            + vd("k = K/AL e y = Y/AL → 0") + "; " + vd("K/L e Y/L → g") + "; " + vd("K e Y → n + g")
            + ". Sem progresso técnico (g = 0): " + vd("K/L e Y/L → 0") + "; " + vd("K e Y → n") + ".")

CARDS = [
    # ------------------------------------------------------------------ E2-L00579
    {
        "id": "ECO-E2-L00579-1", "fonte_ref": "E2-L00579", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_CRESC_CONS,
        "rotulo_item": "Item",
        "assertiva": ("A acumulação de capital físico, por si só, é capaz de produzir um aumento permanente da renda "
                      "per capita no Modelo de Solow, dada a hipótese de rendimentos marginais crescentes sobre o "
                      "fator capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A acumulação de capital físico, por si só, ") + vm("é capaz") + az(" de produzir um ")
                    + vm("aumento permanente") + az(" da renda per capita no Modelo de Solow, dada a hipótese de "
                                                    "rendimentos marginais ") + vm("crescentes")
                    + az(" sobre o fator capital.")),
        "poucas": ("O Solow supõe rendimentos marginais " + azb("decrescentes") + " do capital — e é justamente por "
                   "isso que acumular capital, sozinho, " + vm("não sustenta") + " o crescimento da renda per "
                   "capita: a economia para no estado estacionário."),
        "destrinchando": [
            "Hipóteses de " + oc("Robert Solow") + " (1956): função de produção agregada Y = F(K, L) com "
            + azb("retornos constantes de escala") + " e " + azb("rendimentos marginais decrescentes") + " de cada "
            "fator. Em termos por trabalhador, y = f(k) é crescente e " + vd("côncava") + ": cada unidade extra de "
            "capital acrescenta menos produto que a anterior (f′ &gt; 0, f″ &lt; 0).",
            "Dinâmica: Δk = s·f(k) − (n + δ)k. Com k baixo, o investimento s·f(k) supera a reposição (n + δ)k e k "
            "cresce; mas, como f(k) se achata e a reposição é uma reta, chega-se a " + vd("k*") + ", onde "
            "investimento = reposição. Ali k e y param de crescer.",
            "Por isso a acumulação de capital gera crescimento só <b>na transição</b>. Crescimento per capita "
            "contínuo exige " + azb("progresso técnico exógeno") + " (taxa g), que desloca f(k) para cima "
            "continuamente.",
            "Cuidado com o vocabulário: elevar a poupança eleva o <b>nível</b> de k* e de y* de forma permanente; "
            "o que a acumulação não produz é <b>crescimento</b> permanente. O item usa “aumento permanente” no "
            "sentido de crescimento sustentado e o ancora numa hipótese falsa.",
            "Se o PMgK fosse crescente (ou constante, como no " + azb("modelo AK") + " do crescimento endógeno), "
            "acumular capital manteria o crescimento indefinidamente — é exatamente o que o Solow nega.",
            vm("Regra-âncora: rendimentos decrescentes do capital → estado estacionário → sem progresso técnico, "
               "crescimento per capita nulo no longo prazo."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item troca “decrescentes” por “crescentes” "
                       "e tira daí uma conclusão coerente com a hipótese falsa. A pista é o “por si só”: no Solow, "
                       "nada além do progresso técnico sustenta o crescimento per capita. 🔥 A banca alterna "
                       "“crescentes”, “constantes” e “decrescentes” nesse mesmo esqueleto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A acumulação de capital físico, por si só, não sustenta o crescimento da renda per capita no "
            "modelo de Solow, dada a hipótese de rendimentos marginais decrescentes do capital.”</i> → CERTO",
            "<i>“…dada a hipótese de rendimentos constantes de escala, que leva a economia ao estado "
            "estacionário.”</i> → ERRADO (nexo indevido: quem gera o estado estacionário são os rendimentos "
            "marginais decrescentes)",
        ])],
        "reescrita": ("A acumulação de capital físico, por si só, " + hl("não é capaz") + " de produzir um "
                      + hl("crescimento contínuo") + " da renda per capita no Modelo de Solow, dada a hipótese de "
                      "rendimentos marginais " + hl("decrescentes") + " sobre o fator capital."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["por si só"], "dificuldade": 1,
        "comentario_fonte": ("O Modelo de Solow assume rendimentos marginais decrescentes do capital; por isso a "
                             "acumulação de capital, por si só, não gera crescimento permanente da renda per capita, "
                             "levando a economia a um estado estacionário."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00622-1, ECO-E2-L00896-1 (mesma hipótese de rendimentos marginais "
                    "decrescentes do capital)"],
    },
    # ------------------------------------------------------------------ E2-L00622
    {
        "id": "ECO-E2-L00622-1", "fonte_ref": "E2-L00622", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MOD_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, a função de produção exibe rendimentos marginais crescentes para o "
                      "capital, o que garante o crescimento contínuo do produto per capita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow, a função de produção exibe rendimentos marginais ") + vm("crescentes")
                    + az(" para o capital, o que ") + vm("garante") + az(" o crescimento contínuo do produto per "
                                                                         "capita.")),
        "poucas": ("No Solow o PMgK é " + azb("decrescente") + " (f(k) côncava). É essa hipótese que leva ao estado "
                   "estacionário e " + vm("impede") + " o crescimento per capita contínuo sem progresso técnico."),
        "destrinchando": [
            "A função de produção por trabalhador y = f(k) é crescente e côncava: a inclinação (o "
            + azb("produto marginal do capital") + ", PMgK = f′(k)) diminui à medida que k aumenta. Uma máquina "
            "a mais para quem tem poucas rende muito; para quem já tem muitas, rende pouco.",
            "Consequência gráfica: a curva de investimento s·f(k) também é côncava e acaba cortando a reta de "
            "reposição (n + δ)k em " + vd("k*") + ". À esquerda de k*, k cresce; à direita, encolhe; em k*, fica "
            "parado — e com ele y = f(k*).",
            "Logo, no estado estacionário sem progresso técnico, o produto per capita " + vd("não cresce")
            + "; o produto agregado cresce à taxa n, a mesma da força de trabalho. Com progresso técnico, y/L "
            "cresce a " + vd("g") + ", taxa exógena.",
            "Se os rendimentos fossem crescentes, s·f(k) ficaria cada vez mais acima da reposição e o crescimento "
            "seria explosivo, sem convergência. Rendimentos constantes no capital (modelo " + azb("AK") + ", "
            "crescimento endógeno) dão crescimento contínuo a taxa constante sA − (n + δ).",
            "Não confundir com " + azb("retornos de escala") + ": o Solow tem retornos <b>constantes</b> de escala "
            "(dobrar K e L dobra Y) e rendimentos marginais <b>decrescentes</b> em cada fator isolado.",
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Troca “decrescentes” por “crescentes” e "
                       "acrescenta um “garante” que só seria consequência da hipótese falsa. Em Solow, toda "
                       "conclusão de crescimento per capita contínuo sem progresso técnico é ERRADA."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, a função de produção exibe rendimentos marginais decrescentes para o "
            "capital, o que leva a economia a um estado estacionário.”</i> → CERTO",
            "<i>“No modelo de Solow, a função de produção exibe retornos decrescentes de escala.”</i> → ERRADO "
            "(troca de conceito: os retornos de escala são constantes)",
        ])],
        "reescrita": ("No modelo de Solow, a função de produção exibe rendimentos marginais " + hl("decrescentes")
                      + " para o capital, o que " + hl("impede") + " o crescimento contínuo do produto per capita"
                      + hl(" sem progresso técnico") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["garante"], "dificuldade": 1,
        "comentario_fonte": ("Premissa fundamental do Solow: rendimentos marginais decrescentes do capital; leva ao "
                             "estado estacionário, onde o crescimento per capita cessa sem progresso tecnológico. "
                             "Rendimentos crescentes levariam a crescimento explosivo. Imagem com a função de "
                             "produção e o diagrama de convergência a k*."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 095", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (função de produção côncava e convergência a k* descritas no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00579-1, ECO-E2-L00896-1"],
    },
    # ------------------------------------------------------------------ E2-L00623
    {
        "id": "ECO-E2-L00623-1", "fonte_ref": "E2-L00623", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MOD_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento na taxa de poupança provoca uma aceleração apenas temporária na taxa de crescimento "
                      "do produto per capita; no longo prazo, a economia converge para um novo estado estacionário "
                      "com um nível de produto e capital per capita mais elevado, mas a taxa de crescimento volta a "
                      "ser determinada pelo progresso tecnológico exógeno."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento na taxa de poupança provoca uma aceleração <u>apenas temporária</u> na taxa de "
                      "crescimento do produto per capita; no longo prazo, a economia converge para um novo estado "
                      "estacionário com um <u>nível</u> de produto e capital per capita mais elevado, mas a taxa de "
                      "crescimento volta a ser determinada pelo <u>progresso tecnológico exógeno</u>."),
        "poucas": ("É o " + azb("efeito nível × efeito crescimento") + " do Solow: mais poupança acelera o "
                   "crescimento só na transição e deixa um nível de k* e y* permanentemente maior; a taxa de longo "
                   "prazo volta a ser " + vd("g") + "."),
        "destrinchando": [
            "Mecanismo: s sobe → a curva de investimento s·f(k) se desloca para cima → em k₁*, o investimento passa "
            "a superar a reposição (n + δ)k (ou (n + g + δ)k com progresso técnico) → k volta a crescer.",
            "Mas, como o PMgK é " + azb("decrescente") + ", cada acréscimo de k rende menos produto; a folga entre "
            "investimento e reposição vai sumindo até o novo estado estacionário " + vd("k₂* &gt; k₁*") + ". Ali "
            "k e y (por trabalhador efetivo) param de crescer de novo.",
            "Trajetória no tempo: a taxa de crescimento de y/L dá um salto, decai gradualmente e retorna a g; o "
            "<b>nível</b> de y/L fica permanentemente numa trajetória mais alta, paralela à antiga (em escala "
            "logarítmica).",
            TAXAS_EE,
            "Contraste com o " + azb("crescimento endógeno") + " (" + oc("Romer") + ", " + oc("Lucas") + ", modelo "
            "AK): ali a poupança pode alterar a taxa de crescimento de longo prazo, porque não há rendimentos "
            "decrescentes no fator acumulável.",
            ANCORA_NIVEL,
        ],
        "grafico_verso": "ECO-E2-L00623-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz a conclusão-padrão do manual, com três "
                       "marcadores certos: “apenas temporária”, “nível” e “exógeno”. A versão errada típica troca "
                       "“temporária” por “permanente” ou diz que a nova taxa de longo prazo é maior."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento na taxa de poupança eleva permanentemente a taxa de crescimento do produto per "
            "capita.”</i> → ERRADO (troca nível × taxa)",
            "<i>“Um aumento da taxa de crescimento populacional também gera aceleração temporária do produto per "
            "capita.”</i> → ERRADO (inversão: n maior reduz k* e y*, o crescimento per capita na transição é "
            "negativo)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Mais poupança eleva o investimento e acelera o crescimento na transição; no novo estado "
                             "estacionário o nível de produto e capital per capita é maior, e a taxa de crescimento "
                             "volta a ser a do progresso tecnológico exógeno. Duas imagens: aumento de s e aumento "
                             "de n no diagrama de Solow."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 096", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00623-1-V1, didática)"},
                          {"ref": "IMAGEM 097", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (aumento de n; fora do ponto do item)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00827-1, ECO-E2-L01252-1, ECO-E2-L01732-1 (poupança: nível × "
                    "taxa)"],
    },
    # ------------------------------------------------------------------ E2-L00634
    {
        "id": "ECO-E2-L00634-1", "fonte_ref": "E2-L00634", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo de Solow com progresso técnico, o produto per capita cresce no estado "
                      "estacionário à taxa (g + n), em que g é a taxa de progresso tecnológico e n é a taxa de "
                      "crescimento populacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um modelo de Solow com progresso técnico, o produto per capita cresce no estado "
                       "estacionário à taxa ") + vm("(g + n)") + az(", em que g é a taxa de progresso tecnológico e "
                                                                    "n é a taxa de crescimento populacional.")),
        "poucas": ("(g + n) é a taxa do produto " + azb("agregado") + " Y. O produto " + azb("per capita") + " Y/L "
                   "cresce só a " + vd("g") + ": o n entra no numerador e sai pelo denominador."),
        "destrinchando": [
            "Com progresso técnico aumentador de trabalho, Y = F(K, A·L); A cresce a g e L a n. O modelo se "
            "resolve em unidades de " + azb("trabalho efetivo") + ": k = K/AL e y = Y/AL, que são constantes no "
            "estado estacionário, com s·f(k*) = (n + g + δ)k*.",
            "Daí, por decomposição em taxas: Y = y·A·L → " + vd("gY = 0 + g + n") + ". E Y/L = y·A → "
            + vd("gY/L = 0 + g = g") + ". A população aumenta o tamanho da economia, não o produto de cada "
            "pessoa.",
            TAXAS_EE,
            "Esse é o resultado central do Solow: só o " + azb("progresso técnico exógeno") + " explica o "
            "crescimento sustentado do padrão de vida; poupança e população afetam níveis.",
            vm("Regra-âncora: per capita → g; agregado → n + g; por trabalhador efetivo → zero."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui ao per capita a taxa do agregado. 🔥 Item recorrente: "
                       "a banca só troca a variável (per capita × agregado × por trabalhador efetivo) e mantém a "
                       "taxa, ou o contrário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o produto agregado cresce no estado estacionário à taxa (g + n)…”</i> → CERTO",
            "<i>“…o produto por trabalhador efetivo cresce no estado estacionário à taxa g…”</i> → ERRADO (troca "
            "de conceito: por trabalhador efetivo, a taxa é zero)",
        ])],
        "reescrita": ("Em um modelo de Solow com progresso técnico, o produto per capita cresce no estado "
                      "estacionário à taxa " + hl("g (é o produto agregado que cresce a g + n)") + ", em que g é a "
                      "taxa de progresso tecnológico e n é a taxa de crescimento populacional."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O produto agregado cresce a (n + g) no estado estacionário; o produto per capita, só "
                             "a g, porque n dilui o produto entre mais trabalhadores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01250-1, ECO-E2-L01730-1 (mesmo item em outras provas)"],
    },
    # ------------------------------------------------------------------ E2-L00686
    {
        "id": "ECO-E2-L00686-1", "fonte_ref": "E2-L00686", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MODELOS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o Modelo de Crescimento de Solow, no estado estacionário, a taxa de crescimento "
                      "do produto per capita é determinada pela taxa de poupança; quanto maior a poupança, maior o "
                      "crescimento permanente da renda per capita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o Modelo de Crescimento de Solow, no estado estacionário, a taxa de "
                       "crescimento do produto per capita ") + vm("é determinada pela") + az(" taxa de poupança; "
                                                                                              "quanto maior a "
                                                                                              "poupança, maior o ")
                    + vm("crescimento") + az(" permanente da renda per capita.")),
        "poucas": ("A poupança determina o " + azb("nível") + " de k* e de y*, não a " + azb("taxa") + " de "
                   "crescimento de longo prazo, que é " + vd("g") + " (zero sem progresso técnico)."),
        "destrinchando": [
            "No estado estacionário, s·f(k*) = (n + g + δ)k*. A poupança aparece na condição que <b>localiza</b> "
            "k*: s maior → k* maior → y* = f(k*) maior. Mas, uma vez em k*, k e y por trabalhador efetivo ficam "
            "constantes, e y/L cresce a g, qualquer que seja s.",
            "Por quê? Rendimentos marginais " + azb("decrescentes") + ": para crescer sempre por acumulação, seria "
            "preciso investir uma fração cada vez maior do produto — e s &lt; 1 é um teto. A poupança maior compra "
            "um degrau, não uma rampa.",
            "Na transição de k₁* para k₂*, o crescimento per capita fica temporariamente acima de g; depois "
            "volta. Países com s maior são mais <b>ricos</b>, não crescem mais rápido para sempre.",
            "Evidência associada: " + oc("Mankiw, Romer e Weil") + " (1992) mostraram que o Solow ampliado com "
            "capital humano explica boa parte das diferenças de <b>nível</b> de renda entre países a partir de "
            "poupança e crescimento populacional.",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito]") + " Confusão clássica nível × taxa. A primeira metade "
                       "(“no estado estacionário”) é o gatilho: no estado estacionário nada de s, n ou δ mexe na "
                       "taxa per capita. 🔥 Um dos itens mais repetidos sobre Solow."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…quanto maior a poupança, maior o nível de renda per capita do estado estacionário.”</i> → CERTO",
            "<i>“…quanto maior a poupança, maior o crescimento da renda per capita durante a transição para o novo "
            "estado estacionário.”</i> → CERTO",
        ])],
        "reescrita": ("De acordo com o Modelo de Crescimento de Solow, no estado estacionário, a taxa de crescimento "
                      "do produto per capita " + hl("não é determinada pela") + " taxa de poupança; quanto maior a "
                      "poupança, maior o " + hl("nível") + " permanente da renda per capita."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["quanto maior"], "dificuldade": 1,
        "comentario_fonte": ("A poupança afeta o nível do produto per capita no estado estacionário, não a taxa de "
                             "crescimento de longo prazo, determinada exclusivamente pelo progresso tecnológico "
                             "exógeno (zero sem tecnologia)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “De cordo” → “De acordo” (erro de digitação da fonte)",
                    "quase_duplicata: ECO-E2-L01252-1, ECO-E2-L01441-1, ECO-E2-L01653-1"],
    },
    # ------------------------------------------------------------------ E2-L00763
    {
        "id": "ECO-E2-L00763-1", "fonte_ref": "E2-L00763", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_INTERTEMP,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, a taxa de crescimento é sustentável no longo prazo, porque a função de "
                      "produção agregada funciona sob condições de retornos crescentes de escala."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow, a taxa de crescimento ") + vm("é sustentável no longo prazo, porque")
                    + az(" a função de produção agregada funciona sob condições de retornos ") + vm("crescentes")
                    + az(" de escala.")),
        "poucas": ("O Solow supõe " + azb("retornos constantes de escala") + " e rendimentos marginais decrescentes; "
                   "o crescimento per capita só se sustenta com " + vd("progresso técnico exógeno") + "."),
        "destrinchando": [
            "Hipóteses da função de produção neoclássica F(K, L): " + vd("F(λK, λL) = λF(K, L)") + " (retornos "
            "constantes de escala) e PMg de cada fator positivo e decrescente. Os retornos constantes permitem "
            "escrever tudo por trabalhador: y = f(k).",
            "Com rendimentos marginais decrescentes do capital, a acumulação leva a um " + azb("estado "
            "estacionário") + " em que k e y param. Sem progresso técnico, o crescimento per capita de longo "
            "prazo é " + vd("zero") + "; o produto agregado cresce só a n.",
            "Crescimento per capita sustentado, no Solow, vem de fora do modelo: a taxa " + vd("g") + " de "
            "progresso técnico. Por isso se diz que é um modelo de " + azb("crescimento exógeno") + ".",
            "Retornos crescentes (ou, mais precisamente, ausência de rendimentos decrescentes no fator "
            "acumulável) são marca dos modelos de " + azb("crescimento endógeno") + ": externalidades do "
            "conhecimento em " + oc("Romer") + " (1986, 1990), capital humano em " + oc("Lucas") + " (1988), "
            "<i>learning by doing</i> em " + oc("Arrow") + " (1962), modelo AK.",
            "Atenção à distinção: <b>retornos de escala</b> (todos os fatores juntos, longo prazo) × "
            "<b>rendimentos marginais</b> (um fator varia, o outro fixo). O Solow combina retornos constantes de "
            "escala com rendimentos marginais decrescentes.",
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Duas falhas encadeadas: atribui ao Solow a "
                       "hipótese do crescimento endógeno (retornos crescentes) e, a partir dela, conclui um "
                       "crescimento sustentável que o modelo só obtém com tecnologia exógena. O “porque” é o elo "
                       "fabricado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, a função de produção agregada apresenta retornos constantes de escala e "
            "rendimentos marginais decrescentes dos fatores.”</i> → CERTO",
            "<i>“No modelo de Romer, o crescimento de longo prazo é sustentável porque o conhecimento gera "
            "externalidades que afastam os rendimentos decrescentes.”</i> → CERTO",
        ])],
        "reescrita": ("No modelo de Solow, a taxa de crescimento " + hl("per capita só é sustentável no longo prazo "
                      "com progresso técnico exógeno, pois") + " a função de produção agregada funciona sob "
                      "condições de retornos " + hl("constantes") + " de escala" + hl(", com rendimentos marginais "
                      "decrescentes") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["porque"], "dificuldade": 1,
        "comentario_fonte": ("Dois comentários convergentes: o Solow assume retornos constantes de escala e "
                             "rendimentos marginais decrescentes; sem progresso tecnológico, o crescimento per "
                             "capita no estado estacionário é zero; retornos crescentes são de modelos de "
                             "crescimento endógeno."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00816
    {
        "id": "ECO-E2-L00816-1", "fonte_ref": "E2-L00816", "destino": "56", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_TEORIA_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo de Solow, no estado estacionário, o nível de consumo por trabalhador é "
                      "sempre maximizado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando o modelo de Solow, no estado estacionário, o nível de consumo por trabalhador ")
                    + vm("é sempre maximizado") + az(".")),
        "poucas": ("Há um estado estacionário para cada taxa de poupança, e só um deles maximiza o consumo: o da "
                   + azb("regra de ouro") + ", em que " + vd("PMgK = n + δ") + "."),
        "destrinchando": [
            "Estado estacionário = k constante: s·f(k*) = (n + δ)k*. Qualquer s entre 0 e 1 gera um k* próprio — "
            "é uma condição de <b>estabilidade</b>, não de otimalidade.",
            "Consumo por trabalhador no estado estacionário: " + vd("c* = f(k*) − (n + δ)k*") + ". É a distância "
            "vertical entre a curva de produção e a reta de reposição. Ela cresce com k* enquanto f′(k) &gt; n + δ "
            "e cai depois.",
            "O máximo ocorre em " + azb("k ouro") + ", onde " + vd("f′(k) = n + δ") + " (com progresso técnico, "
            "n + g + δ). Essa é a " + azb("regra de ouro da acumulação de capital") + ", formulada por "
            + oc("Edmund Phelps") + " (1961).",
            "Se k* &lt; k ouro, a economia poupa de menos: elevar s reduz o consumo agora e o eleva no longo prazo. "
            "Se k* &gt; k ouro, poupa demais (" + azb("ineficiência dinâmica") + "): reduzir s aumenta o consumo "
            "já e no longo prazo.",
            "Com Cobb-Douglas y = k<sup>α</sup>, a poupança da regra de ouro é " + vd("s ouro = α") + " (a "
            "participação do capital na renda).",
        ],
        "dissecando": (cz("[modulador absoluto]") + " O “sempre” transforma uma propriedade de um único estado "
                       "estacionário (o da regra de ouro) em propriedade de todos. Pista: o estado estacionário "
                       "depende de s, e o item não fixa s."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No estado estacionário da regra de ouro, o produto marginal do capital iguala a soma das taxas "
            "de crescimento populacional e de depreciação.”</i> → CERTO",
            "<i>“A regra de ouro maximiza o produto por trabalhador do estado estacionário.”</i> → ERRADO (troca "
            "de conceito: maximiza o consumo; o produto cresce sempre com s)",
        ])],
        "reescrita": ("Considerando o modelo de Solow, no estado estacionário, o nível de consumo por trabalhador "
                      + hl("só é maximizado quando k* coincide com o capital da regra de ouro (PMgK = n + δ)")
                      + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("O estado estacionário ocorre quando k é constante; o k que maximiza o consumo por "
                             "trabalhador é o da regra de ouro, em que PMgK = δ + n."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01253-1, ECO-E2-L01589-1 (regra de ouro)"],
    },
    # ------------------------------------------------------------------ E2-L00817
    {
        "id": "ECO-E2-L00817-1", "fonte_ref": "E2-L00817", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_TEORIA_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Em relação ao modelo de crescimento de Solow, se o estoque de capital por trabalhador for "
                      "inferior ao estoque de capital por trabalhador de estado estacionário, então o capital per "
                      "capita crescerá ao longo do tempo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em relação ao modelo de crescimento de Solow, se o estoque de capital por trabalhador for "
                      "<u>inferior</u> ao estoque de capital por trabalhador de estado estacionário, então o capital "
                      "per capita <u>crescerá</u> ao longo do tempo."),
        "poucas": ("Com k &lt; k*, o investimento " + vd("s·f(k)") + " supera a reposição " + vd("(n + δ)k")
                   + ": Δk &gt; 0, e k sobe até k*. É a " + azb("estabilidade") + " do estado estacionário."),
        "destrinchando": [
            "Equação fundamental: " + vd("Δk = s·f(k) − (n + δ)k") + ". O primeiro termo é o investimento por "
            "trabalhador; o segundo, o " + azb("investimento de manutenção") + " — o que é preciso para repor o "
            "capital depreciado (δk) e equipar os novos trabalhadores (nk).",
            "À esquerda de k*, como f(k) é côncava, s·f(k) fica acima da reta (n + δ)k: sobra investimento, e o "
            "capital por trabalhador aumenta (" + azb("aprofundamento do capital") + "). À direita, ocorre o "
            "inverso, e k diminui.",
            "O crescimento é mais rápido quanto mais longe de k* a economia começa, porque o PMgK é maior com "
            "pouco capital. Essa é a base da " + azb("convergência condicional") + ": economias com os mesmos "
            "parâmetros (s, n, δ, tecnologia) tendem ao mesmo k*, e as mais pobres crescem mais rápido.",
            "A convergência é <b>condicional</b>, não absoluta: países com s ou n diferentes têm k* diferentes, "
            "e um país pobre pode estar perto do seu próprio k* (baixo) e crescer pouco.",
            "Com progresso técnico, o raciocínio é o mesmo em k = K/AL, com reposição (n + g + δ)k.",
        ],
        "dissecando": (cz("[literalidade]") + " Descreve a dinâmica de transição do manual, com a direção certa. "
                       "A versão errada troca “inferior” por “superior” ou diz que k cresceria indefinidamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se o estoque de capital por trabalhador for superior ao de estado estacionário, o capital per "
            "capita crescerá ao longo do tempo.”</i> → ERRADO (inversão: acima de k*, k diminui)",
            "<i>“…então o capital per capita crescerá indefinidamente.”</i> → ERRADO (modulador absoluto: para "
            "em k*)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["se", "então"], "dificuldade": 1,
        "comentario_fonte": ("Abaixo de k*, sf(k) &gt; (δ + n)k: a economia acumula mais que o necessário para "
                             "repor depreciação e equipar novos trabalhadores, e k cresce até o estado "
                             "estacionário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01056-1 (mesma dinâmica, lado acima de k*)"],
    },
    # ------------------------------------------------------------------ E2-L00827
    {
        "id": "ECO-E2-L00827-1", "fonte_ref": "E2-L00827", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_COM_REL,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de crescimento de Solow, uma explicação para o diferencial de nível de "
                      "renda per capita, no longo prazo, seria a diferença nas taxas de poupança dos países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o modelo de crescimento de Solow, uma explicação para o diferencial de "
                      "<u>nível</u> de renda per capita, no longo prazo, seria a diferença nas taxas de poupança dos "
                      "países."),
        "poucas": ("A poupança determina o " + azb("nível") + " de k* e y*: países com s maior convergem para "
                   "estados estacionários mais ricos. O item fala de nível, não de taxa — por isso é CERTO."),
        "destrinchando": [
            "Na condição s·f(k*) = (n + δ)k*, um s maior desloca a curva de investimento para cima e leva a um k* "
            "maior; como " + vd("y* = f(k*)") + ", a renda per capita de longo prazo também é maior.",
            "Com Cobb-Douglas y = k<sup>α</sup>: " + vd("y* = [s/(n + δ)]<sup>α/(1−α)</sup>") + ". Renda de longo "
            "prazo cresce com s e cai com n e δ.",
            "Aplicação clássica: as diferenças de poupança e de crescimento populacional explicam boa parte do "
            "fosso de renda entre países — " + oc("Mankiw, Romer e Weil") + " (1992), com o Solow ampliado por "
            "capital humano. O resíduo é atribuído à produtividade (tecnologia, instituições).",
            "O que a poupança <b>não</b> explica no Solow é diferença permanente de <b>taxa</b> de crescimento: "
            "no estado estacionário todos crescem a g (o mesmo para todos, no modelo básico).",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item parece pegadinha de “poupança não importa no "
                       "longo prazo”, mas a palavra-chave é <b>nível</b>. 🔥 A banca alterna “nível” (CERTO) e "
                       "“taxa de crescimento” (ERRADO) nesse mesmo esqueleto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma explicação para o diferencial das taxas de crescimento da renda per capita, no longo prazo, "
            "seria a diferença nas taxas de poupança.”</i> → ERRADO (troca nível × taxa)",
            "<i>“…uma explicação para o diferencial de nível de renda per capita seria a diferença nas taxas de "
            "crescimento populacional.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["uma explicação"], "dificuldade": 1,
        "comentario_fonte": ("A poupança não afeta o crescimento da renda per capita do estado estacionário, mas "
                             "afeta o nível de longo prazo; logo explica diferenças de nível entre países. Imagem do "
                             "aumento da taxa de poupança no diagrama de Solow."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 124", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (deslocamento de s₁f(k) para s₂f(k) descrito no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01259-1 (mesma assertiva, em outra prova), ECO-E2-L00623-1"],
    },
    # ------------------------------------------------------------------ E2-L00828
    {
        "id": "ECO-E2-L00828-1", "fonte_ref": "E2-L00828", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_COM_REL,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de crescimento de Solow, o crescimento contínuo do volume de "
                      "investimento por trabalhador contribui para a determinação da taxa de crescimento da renda "
                      "per capita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o modelo de crescimento de Solow, o crescimento contínuo do volume de "
                       "investimento por trabalhador ") + vm("contribui para a determinação da")
                    + az(" taxa de crescimento da renda per capita.")),
        "poucas": ("No Solow, investimento e poupança afetam a taxa de crescimento per capita só " + azb("na "
                   "transição") + ". A taxa de longo prazo é dada pelo " + vd("progresso técnico exógeno")
                   + "."),
        "destrinchando": [
            "Investimento por trabalhador = s·f(k). Ele cresce enquanto k cresce, isto é, na transição para k*. "
            "Ao chegar ao estado estacionário, para de crescer (sem progresso técnico) ou cresce a g (com "
            "progresso técnico) — sempre como <b>consequência</b>, não causa, do crescimento.",
            "Um “crescimento contínuo” do investimento por trabalhador sustentado pela acumulação esbarra nos "
            + azb("rendimentos marginais decrescentes") + ": cada unidade de capital rende menos produto, e a "
            "fração investida não pode passar de 100% da renda.",
            "Elevar s eleva o crescimento per capita apenas durante a transição de k₁* para k₂*; depois a taxa "
            "volta a g. O efeito duradouro é sobre o <b>nível</b> de k e de y.",
            "Contraste: nos modelos de " + azb("crescimento endógeno") + " (AK, " + oc("Romer") + "), o "
            "investimento — em capital físico, humano ou em P&amp;D — determina a taxa de crescimento de longo "
            "prazo. No Solow, não.",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item empresta ao Solow a lógica do "
                       "crescimento endógeno (investimento → taxa de crescimento). O “contínuo” é a pista: no "
                       "Solow, nada movido pela acumulação é contínuo sem tecnologia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo AK, a taxa de poupança e investimento determina a taxa de crescimento de longo prazo "
            "da renda per capita.”</i> → CERTO",
            "<i>“No modelo de Solow, uma alta da taxa de investimento eleva o crescimento da renda per capita "
            "durante a transição para o novo estado estacionário.”</i> → CERTO",
        ])],
        "reescrita": ("De acordo com o modelo de crescimento de Solow, o crescimento contínuo do volume de "
                      "investimento por trabalhador " + hl("não determina a") + " taxa de crescimento "
                      + hl("de longo prazo") + " da renda per capita" + hl(", dada pelo progresso técnico "
                      "exógeno") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["contínuo"], "dificuldade": 2,
        "comentario_fonte": ("Poupança e investimento não afetam a taxa de crescimento da renda per capita de longo "
                             "prazo; aumentam o crescimento de k e y apenas transitoriamente."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00830
    {
        "id": "ECO-E2-L00830-1", "fonte_ref": "E2-L00830", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_COM_REL,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de crescimento de Solow, na ausência de progresso tecnológico, a "
                      "economia converge para uma taxa de crescimento estável, em que é zero o crescimento da renda "
                      "per capita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o modelo de crescimento de Solow, <u>na ausência de progresso tecnológico</u>, "
                      "a economia converge para uma taxa de crescimento estável, em que é <u>zero</u> o crescimento "
                      "da renda per capita."),
        "poucas": ("Sem progresso técnico, Y e L crescem à mesma taxa " + vd("n") + " no estado estacionário: Y/L "
                   "fica constante, e o crescimento per capita é " + vd("zero") + "."),
        "destrinchando": [
            "Estado estacionário (g = 0): s·f(k*) = (n + δ)k*. Como k = K/L e y = Y/L são constantes, K e Y "
            "precisam crescer exatamente à taxa de L: " + vd("gK = gY = n") + ".",
            "A “taxa de crescimento estável” do item é essa: a economia como um todo cresce a n (crescimento "
            "equilibrado, ou " + azb("balanced growth") + "), mas cada trabalhador não fica mais rico.",
            TAXAS_EE,
            "A razão de fundo são os " + azb("rendimentos marginais decrescentes") + " do capital: acumular mais "
            "k por trabalhador rende cada vez menos, até o investimento apenas repor a depreciação e equipar os "
            "novos trabalhadores.",
            "O progresso técnico é o único motor do crescimento per capita de longo prazo — por isso " + oc("Solow")
            + " (1957) mediu o “resíduo” (a produtividade total dos fatores) e atribuiu a ele a maior parte do "
            "crescimento por trabalhador dos EUA na primeira metade do século XX.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Tudo depende da condição “na ausência de progresso "
                       "tecnológico”. A versão errada diria que o produto <b>agregado</b> não cresce (cresce a n) "
                       "ou que a renda per capita cresce a n."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…na ausência de progresso tecnológico, o produto agregado deixa de crescer no estado "
            "estacionário.”</i> → ERRADO (troca de conceito: o agregado cresce a n)",
            "<i>“…com progresso tecnológico à taxa g, a renda per capita cresce a g no estado "
            "estacionário.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Sem progresso tecnológico, renda e força de trabalho crescem à taxa n; renda per capita "
                             "e capital por trabalhador ficam constantes no estado estacionário. Imagem com tabelas "
                             "de taxas de crescimento com e sem progresso técnico."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 125", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (taxas de estado estacionário listadas no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00895
    {
        "id": "ECO-E2-L00895-1", "fonte_ref": "E2-L00895", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_TPS24,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de crescimento de Solow, quanto maior o crescimento da força de "
                      "trabalho, tudo o mais constante, menor o PIB por trabalhador."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o modelo de crescimento de Solow, quanto maior o <u>crescimento</u> da força de "
                      "trabalho, <u>tudo o mais constante</u>, <u>menor</u> o PIB por trabalhador."),
        "poucas": ("n maior eleva o " + azb("investimento de manutenção") + " (n + δ)k: a mesma poupança precisa "
                   "equipar mais trabalhadores novos, e o estado estacionário recua para " + vd("k* e y* "
                   "menores") + "."),
        "destrinchando": [
            "Condição de estado estacionário: " + vd("s·f(k*) = (n + δ)k*") + ". O termo nk é o capital necessário "
            "para dar aos trabalhadores que chegam o mesmo k dos que já estão — o " + azb("alargamento do "
            "capital") + " (<i>capital widening</i>). O que sobra vai para o " + azb("aprofundamento") + " "
            "(<i>capital deepening</i>).",
            "Com n maior, a reta (n + δ)k fica mais inclinada e corta s·f(k) mais cedo: " + vd("k₂* &lt; k₁*")
            + " e, como y = f(k), também " + vd("y₂* &lt; y₁*") + ".",
            "Com Cobb-Douglas: " + vd("y* = [s/(n + δ)]<sup>α/(1−α)</sup>") + " — a renda por trabalhador de "
            "longo prazo cai com n.",
            "O que n <b>não</b> muda no estado estacionário é a taxa de crescimento per capita (zero sem "
            "progresso técnico, g com ele). Já o produto agregado passa a crescer mais rápido (n + g).",
            "Leitura empírica: países com crescimento demográfico alto tendem a ter renda per capita menor — "
            "um dos resultados que " + oc("Mankiw, Romer e Weil") + " (1992) confirmaram no Solow ampliado.",
        ],
        "grafico_verso": "ECO-E2-L00895-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item de manual protegido pelo “tudo o mais "
                       "constante”. O risco é ler “menor crescimento do PIB por trabalhador” onde está escrito "
                       "“menor PIB por trabalhador”: o efeito de n é sobre o <b>nível</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…quanto maior o crescimento da força de trabalho, menor a taxa de crescimento do PIB por "
            "trabalhador no estado estacionário.”</i> → ERRADO (troca nível × taxa)",
            "<i>“…quanto maior o crescimento da força de trabalho, maior a taxa de crescimento do PIB agregado no "
            "estado estacionário.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tudo o mais constante"],
        "dificuldade": 1,
        "comentario_fonte": ("Com crescimento populacional, o investimento necessário para manter k constante é "
                             "(δ + n)k; n maior eleva a reta de manutenção e reduz k*, logo y*. Países com maior "
                             "crescimento populacional tendem a ter menor capital e renda per capita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 145", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (explicação transcrita no 📖; gráfico refeito como "
                                   "ECO-E2-L00895-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01026-1 (efeito de n sobre k*)"],
    },
    # ------------------------------------------------------------------ E2-L00896
    {
        "id": "ECO-E2-L00896-1", "fonte_ref": "E2-L00896", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_TPS24,
        "rotulo_item": "Item",
        "assertiva": "No modelo de crescimento econômico de Solow, supõe-se rendimentos marginais constantes do capital.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de crescimento econômico de Solow, supõe-se rendimentos marginais ")
                    + vm("constantes") + az(" do capital.")),
        "poucas": ("No Solow, os rendimentos marginais do capital são " + azb("decrescentes") + " (f(k) côncava). "
                   "Rendimento marginal constante do capital é a hipótese do " + azb("modelo AK") + "."),
        "destrinchando": [
            "Premissas da função de produção do Solow: " + azb("retornos constantes de escala") + " (dobrar K e "
            "L dobra Y) e " + azb("rendimentos marginais decrescentes") + " de cada insumo (f′(k) &gt; 0 e "
            "f″(k) &lt; 0). Também as condições de Inada: PMgK muito alto com k → 0 e tendendo a zero com "
            "k → ∞.",
            "É a concavidade que gera o estado estacionário: s·f(k) se achata e encontra a reta (n + δ)k. Sem "
            "progresso técnico, o crescimento per capita de longo prazo é zero.",
            "No " + azb("modelo AK") + " (crescimento endógeno), Y = A·K: o PMgK é constante e igual a A. Aí "
            "s·A·k − (n + δ)k nunca se anula se sA &gt; n + δ, e a economia cresce indefinidamente à taxa "
            + vd("sA − (n + δ)") + " — a poupança passa a determinar a taxa de crescimento.",
            "Rendimentos marginais constantes do capital com retornos constantes de escala implicam que o "
            "trabalho não contribui na margem (ou que “capital” inclui capital humano e conhecimento, a "
            "interpretação ampla do AK).",
            "Lembrete de vocabulário: “retornos <b>de escala</b> constantes” (Solow, CERTO) × “rendimentos "
            "<b>marginais</b> constantes” (AK, ERRADO para o Solow).",
        ],
        "dissecando": (cz("[troca de conceito]") + " A banca aproveita a palavra “constantes”, que de fato aparece "
                       "no Solow — mas nos retornos de <b>escala</b>. Trocar o adjetivo de lugar é o truque "
                       "inteiro. 🔥 Muito cobrado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de crescimento econômico de Solow, supõe-se retornos constantes de escala.”</i> → "
            "CERTO",
            "<i>“No modelo AK, supõe-se produtividade marginal do capital constante, o que permite crescimento "
            "sustentado sem progresso técnico exógeno.”</i> → CERTO",
        ])],
        "reescrita": ("No modelo de crescimento econômico de Solow, supõe-se rendimentos marginais "
                      + hl("decrescentes") + " do capital."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Premissas do Solow: retornos constantes de escala e rendimentos marginais "
                             "decrescentes de capital e trabalho. Imagem compara Solow (PMgK decrescente) e modelo "
                             "AK (PMgK constante)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 146", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (comparação Solow × AK no 📖)"}],
        "alertas": ["texto_corrigido: “contantes” → “constantes” (erro de digitação da fonte)",
                    "quase_duplicata: ECO-E2-L00579-1, ECO-E2-L00622-1"],
    },
    # ------------------------------------------------------------------ E2-L00897
    {
        "id": "ECO-E2-L00897-1", "fonte_ref": "E2-L00897", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_TPS24,
        "rotulo_item": "Item",
        "assertiva": ("Nos parâmetros do modelo de Solow, o aumento da taxa de poupança é irrelevante para o nível de "
                      "renda per capita de longo prazo de uma sociedade, pois o estado estacionário é afetado "
                      "somente pelo progresso tecnológico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nos parâmetros do modelo de Solow, o aumento da taxa de poupança ") + vm("é irrelevante para")
                    + az(" o nível de renda per capita de longo prazo de uma sociedade, pois o estado estacionário é "
                         "afetado ") + vm("somente pelo progresso tecnológico") + az(".")),
        "poucas": ("É o contrário: a poupança é irrelevante para a " + azb("taxa") + " de crescimento de longo "
                   "prazo, mas " + vm("eleva o nível") + " de k* e y*. O estado estacionário depende de s, n, δ e "
                   "da tecnologia."),
        "destrinchando": [
            "A condição " + vd("s·f(k*) = (n + δ)k*") + " mostra os parâmetros que localizam o estado "
            "estacionário: " + vd("s") + " (sobe k*), " + vd("n") + " e " + vd("δ") + " (descem k*) e o nível "
            "de tecnologia A em f(k) (sobe k*).",
            "Com Cobb-Douglas: " + vd("k* = [sA/(n + δ)]<sup>1/(1−α)</sup>") + ". Dobrar s eleva k* e y* de forma "
            "permanente — os países com taxa de poupança mais alta são mais ricos, tudo o mais constante.",
            "O que o progresso técnico determina com exclusividade é a <b>taxa</b> de crescimento per capita de "
            "longo prazo (g). A poupança acelera o crescimento só na transição para o novo estado estacionário.",
            "O item inverte a frase correta “a poupança é irrelevante para a <b>taxa</b> de crescimento de longo "
            "prazo” trocando a taxa pelo nível.",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito · restrição indevida]") + " Troca “taxa” por “nível” e fecha com um "
                       "“somente” que exclui s, n e δ do estado estacionário. A justificativa (“pois…”) soa "
                       "familiar porque copia a conclusão certa sobre a taxa de crescimento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento da taxa de poupança é irrelevante para a taxa de crescimento da renda per capita de "
            "longo prazo, determinada somente pelo progresso tecnológico.”</i> → CERTO",
            "<i>“…o aumento da taxa de depreciação reduz o nível de renda per capita de longo prazo.”</i> → CERTO",
        ])],
        "reescrita": ("Nos parâmetros do modelo de Solow, o aumento da taxa de poupança " + hl("eleva")
                      + " o nível de renda per capita de longo prazo de uma sociedade, pois o estado estacionário é "
                      "afetado " + hl("também pela poupança, e não somente pelo progresso tecnológico") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "RESTRICAO"], "moduladores": ["somente"], "dificuldade": 1,
        "comentario_fonte": ("Poupança e crescimento demográfico não afetam a taxa de crescimento do produto por "
                             "trabalhador no estado estacionário, mas a poupança determina o nível de k e de y do "
                             "estado estacionário; países com poupança mais alta são mais ricos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00827-1, ECO-E2-L01732-1"],
    },
    # ------------------------------------------------------------------ E2-L00898
    {
        "id": "ECO-E2-L00898-1", "fonte_ref": "E2-L00898", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_TPS24,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Solow incorpora, de forma endógena, o progresso tecnológico, explicando como as "
                      "empresas tomam decisões que maximizam o retorno de investimentos em geração de "
                      "conhecimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo de Solow incorpora, de forma ") + vm("endógena") + az(", o progresso tecnológico, ")
                    + vm("explicando") + az(" como as empresas tomam decisões que maximizam o retorno de "
                                            "investimentos em geração de conhecimento.")),
        "poucas": ("No Solow o progresso técnico é " + azb("exógeno") + ": a taxa g cai do céu, sem explicação "
                   "econômica. Decisões de investir em conhecimento são o objeto do " + azb("crescimento "
                   "endógeno") + " (Romer)."),
        "destrinchando": [
            "No Solow, Y = F(K, A·L) e A cresce a uma taxa g dada. O modelo mostra que g determina o crescimento "
            "per capita de longo prazo, mas não diz de onde g vem: há causalidade da tecnologia para a economia, "
            "não da economia para a tecnologia.",
            "Daí a crítica que motivou a " + azb("teoria do crescimento endógeno") + " (anos 1980–90): o principal "
            "motor do crescimento ficava fora do modelo — o “resíduo de Solow” (produtividade total dos fatores) "
            "era chamado de “medida da nossa ignorância”.",
            oc("Paul Romer") + " (1990) endogeneizou a tecnologia: firmas investem em P&amp;D em busca de lucros "
            "de monopólio temporário (patentes); ideias são " + azb("não rivais") + " e parcialmente excludentes, o "
            "que gera rendimentos crescentes agregados. Romer recebeu o Nobel de 2018 por isso (dividido com "
            + oc("William Nordhaus") + ").",
            "Outras vias endógenas: " + oc("Lucas") + " (1988, capital humano), " + oc("Arrow") + " (1962, "
            "<i>learning by doing</i>), " + oc("Aghion e Howitt") + " (1992, destruição criadora schumpeteriana).",
            vm("Regra-âncora: Solow = crescimento exógeno (g dado); Romer/Lucas = crescimento endógeno (g "
               "explicado por decisões dos agentes)."),
        ],
        "dissecando": (cz("[troca de conceito · troca de ator]") + " Atribui ao Solow a característica definidora "
                       "do modelo de Romer. A descrição da segunda metade é precisa — só que de outro modelo. "
                       "Palavra-gatilho: “endógena” associada a Solow é sempre ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Romer incorpora, de forma endógena, o progresso tecnológico, explicando decisões das "
            "empresas de investir em geração de conhecimento.”</i> → CERTO",
            "<i>“No modelo de Solow, o progresso técnico é o determinante do crescimento da renda per capita no "
            "longo prazo, embora seja tratado como exógeno.”</i> → CERTO",
        ])],
        "reescrita": ("O modelo de Solow incorpora, de forma " + hl("exógena") + ", o progresso tecnológico, "
                      + hl("sem explicar") + " como as empresas tomam decisões que maximizam o retorno de "
                      "investimentos em geração de conhecimento."),
        "tipo_erro": ["TROCA_CONCEITO", "TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No Solow, a taxa de progresso tecnológico é determinada fora do sistema econômico; ela "
                             "determina o crescimento da renda per capita no longo prazo, mas não é explicada pelo "
                             "modelo (causalidade da tecnologia para a economia, não o inverso)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01026
    {
        "id": "ECO-E2-L01026-1", "fonte_ref": "E2-L01026", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MODELOS,
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo de Solow, o aumento da taxa de crescimento populacional aumenta a taxa "
                      "de crescimento do produto, porém reduz o estoque de capital por trabalhador de longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando o modelo de Solow, o aumento da taxa de crescimento populacional aumenta a taxa "
                      "de crescimento do <u>produto</u>, porém <u>reduz o estoque de capital por trabalhador</u> de "
                      "longo prazo."),
        "poucas": ("n maior: o produto " + azb("agregado") + " passa a crescer a " + vd("n + g") + " (mais "
                   "rápido), mas o " + azb("capital por trabalhador") + " de estado estacionário cai, porque mais "
                   "investimento vai para equipar os novos trabalhadores."),
        "destrinchando": [
            "Taxa do agregado: no estado estacionário, k = K/AL e y = Y/AL são constantes, então " + vd("gY = gK = "
            "n + g") + ". Um n maior acelera o crescimento do PIB total. O per capita continua a g (zero sem "
            "progresso técnico).",
            "Nível por trabalhador: " + vd("s·f(k*) = (n + δ)k*") + ". Com n maior, a reta de reposição fica mais "
            "inclinada e corta s·f(k) antes: k* e y* caem.",
            "Intuição: parte maior do investimento vira " + azb("alargamento do capital") + " (dar máquinas aos "
            "recém-chegados) e sobra menos para o " + azb("aprofundamento") + " (mais máquinas por trabalhador).",
            "O item combina corretamente os dois efeitos opostos de n: <b>taxa</b> do agregado sobe; <b>nível</b> "
            "por trabalhador desce. A taxa per capita de longo prazo não muda.",
            "Na transição de um estado estacionário para o outro, o produto por trabalhador cai (crescimento per "
            "capita temporariamente negativo).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Parece contraditório (“aumenta… porém reduz”), e é aí que "
                       "o candidato erra. A chave é “produto” sem “per capita”: o agregado cresce mais rápido. Se o "
                       "item dissesse “produto per capita”, seria ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento da taxa de crescimento populacional aumenta a taxa de crescimento do produto per capita "
            "no estado estacionário.”</i> → ERRADO (troca agregado × per capita)",
            "<i>“…o aumento da taxa de crescimento populacional eleva o capital por trabalhador de longo "
            "prazo.”</i> → ERRADO (inversão: k* cai)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["porém"], "dificuldade": 2,
        "comentario_fonte": ("Dois comentários convergentes: no estado estacionário Y cresce a n + g (n se g = 0); "
                             "n maior eleva o crescimento do produto total, mas exige mais investimento para equipar "
                             "novos trabalhadores, reduzindo k* e y*; o per capita não cresce mais rápido."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00895-1"],
    },
    # ------------------------------------------------------------------ E2-L01056
    {
        "id": "ECO-E2-L01056-1", "fonte_ref": "E2-L01056", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_SOBRE,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de Solow, se o capital por unidades efetivas de trabalho supera o seu "
                      "valor de estado estacionário, a poupança do produto médio também supera a taxa de "
                      "depreciação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o modelo de Solow, se o capital por unidades efetivas de trabalho supera o seu "
                       "valor de estado estacionário, a poupança do produto médio ") + vm("também supera a")
                    + az(" taxa de depreciação.")),
        "poucas": ("Acima de k*, a poupança por unidade de capital " + vd("s·f(k)/k") + " fica " + vm("abaixo")
                   + " da depreciação efetiva " + vd("n + g + δ") + ": por isso k encolhe de volta ao estado "
                   "estacionário."),
        "destrinchando": [
            "Equação em unidades de trabalho efetivo (k = K/AL): " + vd("Δk = s·f(k) − (n + g + δ)k") + ". "
            "Dividindo por k: " + vd("Δk/k = s·f(k)/k − (n + g + δ)") + ". O termo s·f(k)/k é a “poupança do "
            "produto médio” do item (s vezes o produto médio do capital, y/k).",
            "Como f é côncava, o produto médio y/k " + azb("cai") + " quando k sobe. Em k*, s·f(k*)/k* = n + g + δ. "
            "Logo, para k &gt; k*, " + vd("s·f(k)/k &lt; n + g + δ") + " e Δk &lt; 0: o capital por trabalhador "
            "efetivo diminui. Para k &lt; k*, ocorre o inverso.",
            "Exemplo numérico: y = k<sup>0,5</sup>, s = 0,2 e n + g + δ = 0,10 → k* = (0,2/0,1)² = " + vd("4")
            + ". Com k = 9: s·y/k = 0,2 × 3 / 9 ≈ " + vd("0,067 &lt; 0,10") + " → k cai.",
            "A “taxa de depreciação” do item deve ser lida como a " + azb("depreciação efetiva") + " (n + g + δ): "
            "ela inclui o desgaste físico (δ) e a diluição do capital por mais trabalhadores (n) e por mais "
            "eficiência (g). Lida literalmente como δ, a comparação nem sequer é conclusiva logo acima de k* — e "
            "a implicação “também supera” continua falsa em geral.",
            "É essa autocorreção dos dois lados que torna o estado estacionário " + azb("estável") + ".",
        ],
        "grafico_verso": "ECO-E2-L01056-1-V1",
        "dissecando": (cz("[inversão]") + " O item inverte a desigualdade que garante a convergência: acima de k*, "
                       "investimento &lt; reposição. O “também” sugere um paralelo (k alto → poupança alta) que a "
                       "concavidade desmente: com mais capital, o produto médio cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se o capital por unidade efetiva de trabalho é inferior ao seu valor de estado estacionário, a "
            "poupança do produto médio supera a depreciação efetiva (n + g + δ).”</i> → CERTO",
            "<i>“…se o capital por unidade efetiva de trabalho supera o de estado estacionário, ele continuará a "
            "crescer à taxa n + g.”</i> → ERRADO (inversão: k por trabalhador efetivo cai)",
        ])],
        "reescrita": ("De acordo com o modelo de Solow, se o capital por unidades efetivas de trabalho supera o seu "
                      "valor de estado estacionário, a poupança do produto médio " + hl("fica abaixo da")
                      + " taxa de depreciação" + hl(" efetiva (n + g + δ)") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["também"], "dificuldade": 2,
        "comentario_fonte": ("Vários comentários convergentes: acima de k*, o capital por trabalhador efetivo tende "
                             "a cair; para isso, s·f(k) &lt; (n + g + δ)k, isto é, s·f(k)/k &lt; n + g + δ; a "
                             "comparação correta é com a depreciação efetiva. Exemplo: y = k^0,5, s = 0,2, "
                             "n + g + δ = 0,10 → k* = 4."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "IMAGEM 183", "tipo_fonte": "DIAGRAMA", "lado": "verso",
             "acao": "cortada (diagrama genérico; substituído por ECO-E2-L01056-1-V1)"},
            {"ref": "IMAGEM 184", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada (genérica)"},
            {"ref": "IMAGEM 185", "tipo_fonte": "GRÁFICO", "lado": "verso",
             "acao": "cortada (trecho de texto genérico)"},
            {"ref": "IMAGEM 186", "tipo_fonte": "TEXTO", "lado": "verso",
             "acao": "absorvida (exemplo numérico no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00817-1 (mesma dinâmica, lado abaixo de k*)"],
    },
    # ------------------------------------------------------------------ E2-L01057
    {
        "id": "ECO-E2-L01057-1", "fonte_ref": "E2-L01057", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_SOBRE,
        "rotulo_item": "Item",
        "assertiva": ("No modelo básico de Solow, uma elevação na taxa de crescimento populacional implica uma "
                      "elevação da taxa de crescimento per capita no estado estacionário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo básico de Solow, uma elevação na taxa de crescimento populacional ")
                    + vm("implica uma elevação da") + az(" taxa de crescimento per capita no estado "
                                                          "estacionário.")),
        "poucas": ("n não mexe na " + azb("taxa") + " per capita de estado estacionário (zero no modelo básico); "
                   "mexe no " + azb("nível") + ": k* e y* caem."),
        "destrinchando": [
            "No modelo básico (sem progresso técnico), o estado estacionário tem k e y por trabalhador constantes: "
            "crescimento per capita " + vd("zero") + ", qualquer que seja n. K e Y crescem a n.",
            "Elevar n aumenta a reposição (n + δ)k: a economia passa a precisar de mais investimento só para "
            "manter k. O novo estado estacionário tem " + vd("k* e y* menores") + ".",
            "Na transição, o produto por trabalhador <b>cai</b> até o novo nível — o oposto do que o item afirma. "
            "Depois, volta a crescer a zero (ou a g, se houver progresso técnico).",
            "O que de fato sobe com n é a taxa de crescimento do produto <b>agregado</b> (n, ou n + g).",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Transfere para o per capita o efeito que n tem "
                       "sobre o agregado. Em “estado estacionário” + “per capita”, só g importa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo básico de Solow, uma elevação na taxa de crescimento populacional implica uma elevação "
            "da taxa de crescimento do produto agregado no estado estacionário.”</i> → CERTO",
            "<i>“…implica uma redução da taxa de crescimento per capita no estado estacionário.”</i> → ERRADO "
            "(a taxa per capita segue nula; cai o nível)",
        ])],
        "reescrita": ("No modelo básico de Solow, uma elevação na taxa de crescimento populacional "
                      + hl("não altera a") + " taxa de crescimento per capita no estado estacionário"
                      + hl(", mas reduz o nível de renda per capita") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["implica"], "dificuldade": 1,
        "comentario_fonte": ("No estado estacionário, a taxa de crescimento per capita é dada pelo progresso "
                             "tecnológico, não por n; n maior reduz k e y por trabalhador, sem alterar a taxa per "
                             "capita de longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01251-1, ECO-E2-L01731-1"],
    },
    # ------------------------------------------------------------------ E2-L01250
    {
        "id": "ECO-E2-L01250-1", "fonte_ref": "E2-L01250", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo com progresso técnico, o produto per capita cresce no estado estacionário à taxa "
                      "(g + n), em que g é a taxa de progresso tecnológico e n é a taxa de crescimento "
                      "populacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um modelo com progresso técnico, o produto per capita cresce no estado estacionário à "
                       "taxa ") + vm("(g + n)") + az(", em que g é a taxa de progresso tecnológico e n é a taxa de "
                                                     "crescimento populacional.")),
        "poucas": ("No estado estacionário: produto " + azb("per capita") + " → " + vd("g") + "; produto "
                   + azb("total") + " → " + vd("g + n") + "; força de trabalho → " + vd("n") + "."),
        "destrinchando": [
            "Regra das taxas: a taxa de crescimento de um quociente é a diferença das taxas. Y/L cresce a "
            + vd("gY − gL = (n + g) − n = g") + ".",
            "Por que Y cresce a n + g? O modelo com progresso técnico aumentador de trabalho (Y = F(K, AL)) se "
            "estabiliza em k = K/AL constante; com retornos constantes de escala, y = Y/AL também fica constante. "
            "Então Y cresce como AL, isto é, a n + g, e K acompanha.",
            TAXAS_EE,
            "Implicação: duas economias com o mesmo g crescem per capita no mesmo ritmo no longo prazo, ainda "
            "que tenham populações crescendo a taxas distintas; diferem no nível de renda por trabalhador "
            "(n maior → nível menor).",
            vm("Regra-âncora: per capita → g; agregado → n + g; por trabalhador efetivo → zero."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A taxa (g + n) existe no modelo, mas pertence ao agregado. "
                       "🔥 Este mesmo enunciado circula em vários simulados; a variante CERTA troca “per capita” "
                       "por “total” ou a taxa por g."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um modelo com progresso técnico, o produto per capita cresce no estado estacionário à taxa "
            "g.”</i> → CERTO",
            "<i>“Em um modelo com progresso técnico, o capital por trabalhador efetivo cresce no estado "
            "estacionário à taxa g.”</i> → ERRADO (troca de conceito: por trabalhador efetivo, taxa zero)",
        ])],
        "reescrita": ("Em um modelo com progresso técnico, o produto per capita cresce no estado estacionário à taxa "
                      + hl("g (é o produto total que cresce a g + n)") + ", em que g é a taxa de progresso "
                      "tecnológico e n é a taxa de crescimento populacional."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "No estado estacionário, o produto per capita cresce a g; o total, a g + n; a força de "
                            "trabalho, a n.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00634-1, ECO-E2-L01730-1 (mesmo item em outras provas)"],
    },
    # ------------------------------------------------------------------ E2-L01251
    {
        "id": "ECO-E2-L01251-1", "fonte_ref": "E2-L01251", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo sem progresso técnico, um aumento da taxa de crescimento populacional aumenta a "
                      "taxa de crescimento do produto per capita no estado estacionário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um modelo sem progresso técnico, um aumento da taxa de crescimento populacional ")
                    + vm("aumenta") + az(" a taxa de crescimento do produto per capita no estado estacionário.")),
        "poucas": ("Sem progresso técnico, Y e L crescem ambos a " + vd("n") + ": Y/L é constante, e a taxa per "
                   "capita é " + vd("zero") + " para qualquer n. O que n maior aumenta é a taxa do produto "
                   "<b>total</b>."),
        "destrinchando": [
            "Estado estacionário sem progresso técnico: k = K/L e y = Y/L constantes. Numerador e denominador "
            "crescem à mesma taxa n, logo " + vd("g(Y/L) = n − n = 0") + ".",
            "Um n maior muda o estado estacionário de outro modo: a reposição (n + δ)k fica mais inclinada, e "
            + vd("k* e y* caem") + " — efeito de <b>nível</b>, negativo.",
            "Durante a transição, o produto per capita cai (crescimento per capita negativo) até o novo nível; "
            "depois volta a zero. Em momento algum a taxa per capita de longo prazo sobe.",
            "Já o produto agregado passa a crescer mais rápido (n maior). É essa a confusão que o item explora.",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca o efeito de n sobre o agregado (taxa sobe) pelo efeito "
                       "sobre o per capita (taxa não muda). A condição “sem progresso técnico” já entrega: taxa per "
                       "capita de estado estacionário = 0, sempre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um modelo sem progresso técnico, um aumento da taxa de crescimento populacional aumenta a "
            "taxa de crescimento do produto total no estado estacionário.”</i> → CERTO",
            "<i>“…uma redução da taxa de crescimento populacional aumenta o nível do produto per capita no "
            "estado estacionário.”</i> → CERTO",
        ])],
        "reescrita": ("Em um modelo sem progresso técnico, um aumento da taxa de crescimento populacional "
                      + hl("não altera") + " a taxa de crescimento do produto per capita no estado estacionário"
                      + hl(", que permanece nula") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Sem progresso técnico, no estado estacionário Y cresce a n, como L; por isso Y/L é "
                             "constante e sua taxa de crescimento é zero."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01057-1, ECO-E2-L01731-1"],
    },
    # ------------------------------------------------------------------ E2-L01252
    {
        "id": "ECO-E2-L01252-1", "fonte_ref": "E2-L01252", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Quanto maior a taxa de poupança de uma economia, maior será o crescimento da renda per capita "
                      "em estado estacionário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quanto maior a taxa de poupança de uma economia, maior será o ") + vm("crescimento")
                    + az(" da renda per capita em estado estacionário.")),
        "poucas": ("Poupança maior → " + azb("nível") + " de renda per capita maior no estado estacionário; a "
                   + azb("taxa") + " de crescimento ali não muda (zero sem progresso técnico, g com ele)."),
        "destrinchando": [
            "Condição de estado estacionário: s·f(k*) = (n + δ)k*. Um s maior desloca a curva de investimento para "
            "cima e leva a " + vd("k* e y* maiores") + ". Mas, em k*, k e y voltam a ficar constantes.",
            "Trajetória após uma alta de s: crescimento per capita acima do normal durante a transição, que vai "
            "se reduzindo à medida que os rendimentos decrescentes atuam, até voltar à taxa de longo prazo. "
            "Resultado final: degrau no nível, mesma inclinação.",
            "Tudo o mais constante, países com taxa de poupança mais alta são mais ricos — não crescem mais "
            "rápido para sempre.",
            "A banca cobra a mesma frase com “maior será a renda per capita em estado estacionário” — aí o item é "
            "CERTO. A única palavra que muda o gabarito é “crescimento”.",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito]") + " Uma palavra só (“crescimento” no lugar de “nível”) inverte o "
                       "gabarito. 🔥 Par clássico de simulados: a mesma frase aparece nas duas versões."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a taxa de poupança de uma economia, maior será a renda per capita em estado "
            "estacionário.”</i> → CERTO",
            "<i>“Quanto maior a taxa de poupança, maior o consumo per capita em estado estacionário.”</i> → ERRADO "
            "(modulador absoluto: só até a poupança da regra de ouro)",
        ])],
        "reescrita": ("Quanto maior a taxa de poupança de uma economia, maior será o " + hl("nível")
                      + " da renda per capita em estado estacionário."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["quanto maior"], "dificuldade": 1,
        "comentario_fonte": ("A poupança não altera a taxa de crescimento da renda per capita no estado estacionário "
                             "(zero sem progresso técnico), mas determina o nível de renda e de capital por "
                             "trabalhador; o crescimento maior é só transitório."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01732-1 (versão CERTA com “renda per capita”), ECO-E2-L00686-1"],
    },
    # ------------------------------------------------------------------ E2-L01253
    {
        "id": "ECO-E2-L01253-1", "fonte_ref": "E2-L01253", "destino": "56", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo sem progresso técnico, o consumo per capita será maximizado quando a "
                      "produtividade marginal do capital for igual à soma da taxa de crescimento populacional com a "
                      "taxa de depreciação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um modelo sem progresso técnico, o consumo per capita será maximizado quando a "
                      "produtividade marginal do capital for <u>igual à soma da taxa de crescimento populacional com "
                      "a taxa de depreciação</u>."),
        "poucas": ("É a " + azb("regra de ouro") + " (" + oc("Phelps") + "): no estado estacionário, c* = f(k) − "
                   "(n + δ)k é máximo quando " + vd("f′(k) = n + δ") + "."),
        "destrinchando": [
            "Consumo de estado estacionário: c* = y* − i* = " + vd("f(k*) − (n + δ)k*") + " (o investimento só "
            "repõe a depreciação e equipa os novos trabalhadores).",
            "Maximizando em k*: dc*/dk* = f′(k*) − (n + δ) = 0 → " + vd("PMgK = n + δ") + ". Graficamente, é o "
            "ponto em que a tangente a f(k) fica paralela à reta (n + δ)k — a maior distância vertical entre as "
            "duas.",
            "Com progresso técnico, a condição vira " + vd("f′(k) = n + g + δ") + " (em unidades de trabalho "
            "efetivo). Formas equivalentes: PMgK − δ = n + g (juro real líquido igual à taxa de crescimento da "
            "economia).",
            "Com Cobb-Douglas y = k<sup>α</sup>, a poupança que leva a k ouro é " + vd("s ouro = α") + ". Poupar "
            "acima disso é " + azb("ineficiência dinâmica") + ": reduzir s elevaria o consumo em todas as datas.",
            "O nome vem da “regra de ouro” ética (fazer às gerações futuras o que gostaríamos que fizessem "
            "conosco): o k que dá a cada geração o mesmo consumo máximo.",
        ],
        "dissecando": (cz("[literalidade]") + " Enuncia a condição exata, com a soma correta e o recorte “sem "
                       "progresso técnico”. Versões erradas trocam a soma por só δ, invertem para “produto "
                       "maximizado” ou somam g sem estar no modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o produto per capita será maximizado quando a produtividade marginal do capital for igual a "
            "n + δ.”</i> → ERRADO (troca de conceito: maximiza o consumo, não o produto)",
            "<i>“Em um modelo com progresso técnico à taxa g, a regra de ouro exige PMgK = n + g + δ.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Regra de ouro: o capital que maximiza o consumo per capita satisfaz f′(k) = n + d, "
                             "igualando a produtividade marginal do capital à soma de crescimento populacional e "
                             "depreciação."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00816-1, ECO-E2-L01589-1"],
    },
    # ------------------------------------------------------------------ E2-L01259
    {
        "id": "ECO-E2-L01259-1", "fonte_ref": "E2-L01259", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_BASE_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de crescimento de Solow, uma explicação para o diferencial de nível de "
                      "renda per capita, no longo prazo seria a diferença nas taxas de poupança dos países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o modelo de crescimento de Solow, uma explicação para o diferencial de "
                      "<u>nível</u> de renda per capita, no longo prazo seria a diferença nas taxas de poupança dos "
                      "países."),
        "poucas": ("Controlando os demais fatores, países com " + azb("poupança") + " maior convergem para "
                   "estados estacionários com mais capital por trabalhador e " + vd("renda per capita maior")
                   + ". É diferença de nível — exatamente o que o item diz."),
        "destrinchando": [
            "Estado estacionário: s·f(k*) = (n + δ)k*. Com Cobb-Douglas, " + vd("y* = [s/(n + δ)]<sup>α/(1−α)"
            "</sup>") + ": a renda de longo prazo depende de s (+), n (−) e δ (−).",
            "Assim, o Solow prevê " + azb("convergência condicional") + ": cada país converge para o <b>seu</b> "
            "estado estacionário. Países que poupam pouco ou têm crescimento demográfico alto ficam "
            "permanentemente mais pobres — sem crescer mais devagar no longo prazo.",
            "Teste empírico: " + oc("Mankiw, Romer e Weil") + " (1992) acharam que poupança e crescimento "
            "populacional explicam parte relevante das diferenças de renda; ao incluir capital humano, a "
            "explicação chega perto de 80% da variância entre países.",
            "Limites: diferenças de produtividade (tecnologia, instituições) explicam o resto e, para muitos "
            "autores, a maior parte do fosso — tema da “contabilidade do desenvolvimento”.",
            "O que a poupança não explica no Solow: diferenças permanentes de <b>taxa</b> de crescimento.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " A palavra “nível” é o que torna o item CERTO; “taxas de "
                       "crescimento” o tornaria ERRADO. 🔥 A banca repete esta frase em mais de uma prova."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma explicação para o diferencial das taxas de crescimento de longo prazo da renda per capita "
            "seria a diferença nas taxas de poupança.”</i> → ERRADO (troca nível × taxa)",
            "<i>“No modelo de Solow, países pobres com os mesmos parâmetros dos ricos tendem a crescer mais "
            "rápido.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["uma explicação"], "dificuldade": 1,
        "comentario_fonte": ("Controlando para outros fatores, diferenças de poupança explicam diferenças de capital "
                             "por trabalhador e de renda per capita; afetam o nível, não a taxa de crescimento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “De acordo como” → “De acordo com” (erro de digitação da fonte)",
                    "quase_duplicata: ECO-E2-L00827-1 (mesma assertiva, em outra prova)"],
    },
    # ------------------------------------------------------------------ E2-L01441
    {
        "id": "ECO-E2-L01441-1", "fonte_ref": "E2-L01441", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_POUP,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, países com níveis baixos de poupança como o Brasil tendem a apresentar "
                      "menores taxas de crescimento do produto no estado estacionário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow, países com níveis baixos de poupança como o Brasil tendem a apresentar "
                       "menores ") + vm("taxas de crescimento do produto") + az(" no estado estacionário.")),
        "poucas": ("Poupança baixa → " + azb("nível") + " menor de renda per capita no estado estacionário; a "
                   + azb("taxa") + " de crescimento ali (per capita g, total n + g) independe de s."),
        "destrinchando": [
            "No estado estacionário, o produto per capita cresce a " + vd("g") + " (zero sem progresso técnico) e "
            "o total a " + vd("n + g") + ". A taxa de poupança não aparece em nenhuma dessas taxas.",
            "Onde s aparece: na condição " + vd("s·f(k*) = (n + δ)k*") + ", que fixa o nível de k* e de y*. "
            "Poupança baixa → k* baixo → renda per capita de longo prazo baixa.",
            "Na transição, um país abaixo do seu estado estacionário pode até crescer mais rápido que os ricos "
            "(" + azb("convergência condicional") + "): o que importa é a distância até o próprio k*, não o "
            "nível de s.",
            "Aplicação ao " + rx("Brasil") + ": a taxa de poupança doméstica é historicamente baixa para padrões "
            "asiáticos (na casa de 15% a 18% do PIB nas últimas décadas, contra 30% a 45% em economias como China "
            "e Coreia) " + vd("⏳ (out/2026)") + ". No Solow, isso ajuda a explicar uma renda per capita mais "
            "baixa, não um crescimento permanentemente menor.",
            "Erro presente em parte dos comentários-fonte: dizer que “a taxa de crescimento no estado "
            "estacionário é zero” sem qualificar. É zero a do produto <b>per capita</b> sem progresso técnico; o "
            "produto total cresce a n (ou n + g).",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito]") + " Confusão nível × taxa, com um apelo ao Brasil para dar "
                       "verossimilhança. O exemplo brasileiro é verdadeiro (poupança baixa), mas o efeito previsto "
                       "pelo Solow é sobre o nível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, países com níveis baixos de poupança como o Brasil tendem a apresentar "
            "menores níveis de renda per capita no estado estacionário.”</i> → CERTO",
            "<i>“No modelo AK, países com poupança baixa tendem a crescer menos no longo prazo.”</i> → CERTO",
        ])],
        "reescrita": ("No modelo de Solow, países com níveis baixos de poupança como o Brasil tendem a apresentar "
                      "menores " + hl("níveis de produto per capita") + " no estado estacionário"
                      + hl(", e não menores taxas de crescimento") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["tendem"], "dificuldade": 1,
        "comentario_fonte": ("Vários comentários convergentes: a poupança afeta o nível de produto per capita no "
                             "estado estacionário, não a taxa de crescimento, determinada pelo progresso técnico "
                             "exógeno. Alguns afirmam, sem qualificar, que a taxa de crescimento no estado "
                             "estacionário é “sempre zero” e que todos convergem para crescimento zero."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: faixas da taxa de poupança do Brasil e de economias asiáticas são ordens de "
                    "grandeza, não dados de um ano específico",
                    "quase_duplicata: ECO-E2-L00686-1, ECO-E2-L01252-1"],
    },
    # ------------------------------------------------------------------ E2-L01589
    {
        "id": "ECO-E2-L01589-1", "fonte_ref": "E2-L01589", "destino": "56", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CONSUMO,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, é possível que uma taxa de poupança elevada que corresponde a maior "
                      "produto per capita no equilíbrio de longo prazo, não seja a que traz maior consumo per "
                      "capita. Assim, a regra de ouro corresponde à taxa de poupança que maximiza o consumo per "
                      "capita no longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Solow, <u>é possível</u> que uma taxa de poupança elevada que corresponde a "
                      "maior produto per capita no equilíbrio de longo prazo, não seja a que traz maior consumo per "
                      "capita. Assim, a regra de ouro corresponde à taxa de poupança que <u>maximiza o consumo per "
                      "capita</u> no longo prazo."),
        "poucas": ("Mais poupança sempre eleva y*, mas também a parcela do produto que não é consumida. O consumo "
                   "de estado estacionário é máximo num ponto intermediário: a " + azb("regra de ouro") + ", em que "
                   + vd("PMgK = n + δ") + "."),
        "destrinchando": [
            "Consumo de estado estacionário: " + vd("c* = f(k*) − (n + δ)k*") + ". Elevar s tem dois efeitos: "
            "eleva k* e, com ele, y* (efeito positivo); mas exige repor e equipar um estoque maior de capital "
            "(efeito negativo). Enquanto f′(k*) &gt; n + δ, o primeiro domina; depois, o segundo.",
            "Por isso a relação entre s e c* tem forma de " + azb("U invertido") + ": com s = 0, não há capital "
            "nem produto; com s = 1, tudo é investido e c* = 0. O máximo está em " + vd("s ouro") + ", que leva a "
            "k ouro, onde " + vd("f′(k ouro) = n + δ") + " (n + g + δ com progresso técnico).",
            "Exemplo didático comum (Cobb-Douglas com α = 0,4): com s₁ = 0,25, s₂ = 0,40 e s₃ = 0,80, o produto "
            "per capita é maior em s₃, mas o consumo per capita é maior em " + vd("s₂ = 0,40 = α") + " — a "
            "poupança da regra de ouro.",
            "Se s &gt; s ouro, a economia é " + azb("dinamicamente ineficiente") + ": reduzir s aumenta o consumo "
            "já e no longo prazo. Se s &lt; s ouro, elevar s exige sacrificar consumo presente em favor das "
            "gerações futuras.",
            "Precisão sobre a fonte: igualar o PMgK apenas à depreciação δ só vale se n = g = 0; no caso geral, "
            "a condição é PMgK = n + g + δ.",
        ],
        "grafico_verso": "ECO-E2-L01589-1-V1",
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Contraria a intuição de que “mais poupança é "
                       "sempre melhor”, protegida pelo “é possível”. A segunda frase define a regra de ouro "
                       "corretamente (maximiza <b>consumo</b>, não produto)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a regra de ouro corresponde à taxa de poupança que maximiza o produto per capita no longo "
            "prazo.”</i> → ERRADO (troca de conceito: maximiza o consumo)",
            "<i>“No modelo de Solow, uma taxa de poupança acima da regra de ouro pode ser reduzida com ganho de "
            "consumo em todas as datas.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["é possível"], "dificuldade": 2,
        "comentario_fonte": ("Comentários convergentes: maior poupança eleva k e y no estado estacionário, mas reduz "
                             "a fração consumida; a regra de ouro maximiza c* = f(k) − δk e ocorre quando o PMgK "
                             "iguala a depreciação (simplificação que ignora n e g). Imagem com s = 0,25, 0,40 e "
                             "0,80; regra de ouro em 0,40."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 444", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (exemplo numérico no 📖; mecanismo refeito em ECO-E2-L01589-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00816-1, ECO-E2-L01253-1"],
    },
    # ------------------------------------------------------------------ E2-L01653
    {
        "id": "ECO-E2-L01653-1", "fonte_ref": "E2-L01653", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_DESENV,
        "rotulo_item": "Item",
        "assertiva": ("Aumentos da taxa de poupança, no modelo de Solow, resultam em um aumento da taxa de "
                      "crescimento de longo prazo de uma economia, enquanto a redução da taxa de crescimento "
                      "populacional eleva a taxa de crescimento de longo prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Aumentos da taxa de poupança, no modelo de Solow, ") + vm("resultam em um aumento da")
                    + az(" taxa de crescimento de longo prazo de uma economia, enquanto a redução da taxa de "
                         "crescimento populacional ") + vm("eleva a taxa de crescimento de longo prazo") + az(".")),
        "poucas": ("Poupança e população mudam o " + azb("nível") + " de renda per capita de longo prazo, não a "
                   + azb("taxa") + " de crescimento per capita, que é " + vd("g") + ". E n menor ainda "
                   + vm("reduz") + " o crescimento do produto total."),
        "destrinchando": [
            "Alta de s: desloca s·f(k) para cima, eleva k* e y*; acelera o crescimento só na transição. No novo "
            "estado estacionário, a renda per capita volta a crescer a g.",
            "Queda de n: torna a reta (n + δ)k menos inclinada, eleva k* e y*; também é efeito de nível. A taxa "
            "per capita de longo prazo segue g.",
            "Sutileza: o produto <b>total</b> cresce a n + g. Reduzir n, portanto, <b>reduz</b> a taxa de "
            "crescimento de longo prazo do agregado — a segunda oração é errada nas duas leituras (per capita: "
            "não muda; total: cai).",
            TAXAS_EE,
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Duas orações com o mesmo erro (nível lido como "
                       "taxa), e a segunda ainda inverte o efeito sobre o agregado. Pista: “taxa de crescimento de "
                       "longo prazo” no Solow só responde a g."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Aumentos da taxa de poupança, no modelo de Solow, elevam o nível de renda per capita de longo "
            "prazo, e a redução da taxa de crescimento populacional também.”</i> → CERTO",
            "<i>“No modelo de Solow, a redução da taxa de crescimento populacional reduz a taxa de crescimento de "
            "longo prazo do produto agregado.”</i> → CERTO",
        ])],
        "reescrita": ("Aumentos da taxa de poupança, no modelo de Solow, " + hl("não alteram a") + " taxa de "
                      "crescimento de longo prazo de uma economia, enquanto a redução da taxa de crescimento "
                      "populacional " + hl("eleva apenas o nível de renda per capita, sem elevar essa taxa") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": ["enquanto"], "dificuldade": 1,
        "comentario_fonte": ("Comentários convergentes: aumentos de s e reduções de n elevam o nível de renda per "
                             "capita de estado estacionário, mas não a taxa de crescimento de longo prazo, dada pelo "
                             "progresso tecnológico exógeno; a taxa do produto total (n + g) seria afetada por n. "
                             "Imagem com as taxas de crescimento do Solow com progresso técnico."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 478", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (taxas de crescimento listadas no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00686-1, ECO-E2-L01252-1"],
    },
    # ------------------------------------------------------------------ E2-L01655
    {
        "id": "ECO-E2-L01655-1", "fonte_ref": "E2-L01655", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_DESENV,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de Solow, na versão com progresso tecnológico, a economia apresentará "
                      "crescimento da renda per capita no longo prazo, o que não ocorre na versão sem progresso "
                      "tecnológico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o modelo de Solow, na versão <u>com</u> progresso tecnológico, a economia "
                      "apresentará crescimento da renda per capita no longo prazo, o que <u>não ocorre</u> na versão "
                      "<u>sem</u> progresso tecnológico."),
        "poucas": ("Sem tecnologia, os rendimentos decrescentes levam a renda per capita a " + vd("parar") + " no "
                   "estado estacionário. Com progresso técnico à taxa g, ela cresce a " + vd("g") + " para "
                   "sempre."),
        "destrinchando": [
            "Versão básica: s·f(k*) = (n + δ)k*; k e y por trabalhador constantes → crescimento per capita "
            + vd("zero") + " no longo prazo. O agregado cresce a n.",
            "Versão com progresso técnico aumentador de trabalho (Y = F(K, AL), A crescendo a g): o estado "
            "estacionário é definido em k = K/AL; como y = Y/AL é constante, " + vd("Y/L = y·A cresce a g")
            + ".",
            "Intuição: o progresso técnico desloca f(k) continuamente para cima e contrabalança os rendimentos "
            "decrescentes do capital — cada trabalhador fica mais produtivo ano após ano.",
            TAXAS_EE,
            "Ressalva conceitual: no Solow, g é " + azb("exógeno") + " — o modelo diz que a tecnologia é o motor "
            "do crescimento per capita, mas não explica de onde ela vem. Explicá-la é o programa do "
            + azb("crescimento endógeno") + " (" + oc("Romer") + ", " + oc("Lucas") + ").",
        ],
        "dissecando": (cz("[literalidade]") + " Contraste correto entre as duas versões do modelo. A versão "
                       "errada típica diria que, sem progresso técnico, a renda per capita cresce a n, ou que, com "
                       "ele, cresce a n + g."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…na versão sem progresso tecnológico, a renda per capita cresce, no longo prazo, à taxa de "
            "crescimento populacional.”</i> → ERRADO (troca de conceito: quem cresce a n é a renda total)",
            "<i>“No modelo de Solow, o progresso tecnológico é explicado pelas decisões de investimento em P&amp;D "
            "das empresas.”</i> → ERRADO (troca de conceito: é exógeno)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Sem progresso tecnológico, o produto per capita fica constante no estado estacionário; "
                             "com progresso tecnológico exógeno, cresce à taxa g, porque a eficiência do trabalho "
                             "contrabalança os retornos decrescentes do capital."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01730
    {
        "id": "ECO-E2-L01730-1", "fonte_ref": "E2-L01730", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Na versão com progresso técnico, o produto per capita cresce no estado estacionário à taxa "
                      "(g + n), em que g é a taxa de progresso tecnológico e n é a taxa de crescimento "
                      "populacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na versão com progresso técnico, o produto per capita cresce no estado estacionário à taxa ")
                    + vm("(g + n)") + az(", em que g é a taxa de progresso tecnológico e n é a taxa de crescimento "
                                         "populacional.")),
        "poucas": ("Per capita (Y/L) → " + vd("g") + ". (g + n) é a taxa do produto " + azb("agregado") + "; por "
                   "trabalhador efetivo (Y/AL), a taxa é " + vd("zero") + "."),
        "destrinchando": [
            "Três medidas de produto, três taxas no estado estacionário: " + vd("Y/AL → 0") + " (é a variável que "
            "fica constante e define o estado estacionário); " + vd("Y/L → g") + " (padrão de vida); "
            + vd("Y → n + g") + " (tamanho da economia).",
            "Derivação em uma linha: Y/L = (Y/AL)·A → taxa = 0 + g. Y = (Y/AL)·A·L → taxa = 0 + g + n.",
            "O mesmo vale para o capital: K/AL constante, K/L cresce a g, K a n + g. E também para o consumo: C a "
            "n + g, C/L a g.",
            "Por que a população não entra no per capita: mais trabalhadores produzem mais, mas o produto se "
            "divide entre mais pessoas — o efeito no numerador e no denominador se cancela.",
            vm("Regra-âncora: per capita → g; agregado → n + g; por trabalhador efetivo → zero."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Soma n a uma taxa per capita. É o tipo de item que pega quem "
                       "decorou “n + g” sem associar a qual variável. 🔥 Enunciado repetido em vários "
                       "simulados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na versão com progresso técnico, o produto agregado cresce no estado estacionário à taxa "
            "(g + n).”</i> → CERTO",
            "<i>“Na versão com progresso técnico, o consumo per capita cresce no estado estacionário à taxa "
            "g.”</i> → CERTO",
        ])],
        "reescrita": ("Na versão com progresso técnico, o produto per capita cresce no estado estacionário à taxa "
                      + hl("g (é o produto agregado que cresce a g + n)") + ", em que g é a taxa de progresso "
                      "tecnológico e n é a taxa de crescimento populacional."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentários convergentes: com progresso técnico, Y/L cresce a g; Y/AL é constante; "
                             "(g + n) é a taxa do produto agregado. Imagens com o resumo das taxas do Solow com "
                             "progresso técnico."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 518", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"},
                          {"ref": "IMAGEM 519", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (resumo de taxas no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00634-1, ECO-E2-L01250-1 (mesmo item em outras provas)"],
    },
    # ------------------------------------------------------------------ E2-L01731
    {
        "id": "ECO-E2-L01731-1", "fonte_ref": "E2-L01731", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("No modelo sem progresso técnico, uma redução da taxa de crescimento populacional aumenta a "
                      "taxa de crescimento do produto per capita no estado estacionário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo sem progresso técnico, uma redução da taxa de crescimento populacional aumenta ")
                    + vm("a taxa de crescimento") + az(" do produto per capita no estado estacionário.")),
        "poucas": ("Reduzir n eleva o " + azb("nível") + " do produto per capita (k* maior), mas a " + azb("taxa")
                   + " de crescimento per capita no estado estacionário continua " + vd("zero") + "."),
        "destrinchando": [
            "Sem progresso técnico, no estado estacionário k = K/L e y = Y/L são constantes: crescimento per "
            "capita " + vd("zero") + " para qualquer n.",
            "n menor → reta de reposição (n + δ)k menos inclinada → corta s·f(k) mais à direita → " + vd("k* e y* "
            "maiores") + ". Menos investimento é gasto equipando trabalhadores novos, sobra mais para aprofundar "
            "o capital.",
            "Na transição para o novo k*, o produto per capita cresce temporariamente; ao chegar lá, o "
            "crescimento per capita volta a zero.",
            "O produto agregado, por sua vez, passa a crescer mais devagar (taxa n menor).",
            ANCORA_NIVEL,
        ],
        "dissecando": (cz("[troca de conceito]") + " É a versão espelhada do item “n maior aumenta o crescimento "
                       "per capita”: a direção do efeito (n menor → melhor) está certa, mas recai sobre o nível, "
                       "não sobre a taxa. O sinal “certo” é o que engana."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo sem progresso técnico, uma redução da taxa de crescimento populacional aumenta o nível "
            "do produto per capita no estado estacionário.”</i> → CERTO",
            "<i>“…uma redução da taxa de crescimento populacional aumenta a taxa de crescimento do produto "
            "agregado no estado estacionário.”</i> → ERRADO (inversão: o agregado passa a crescer menos)",
        ])],
        "reescrita": ("No modelo sem progresso técnico, uma redução da taxa de crescimento populacional aumenta "
                      + hl("o nível") + " do produto per capita no estado estacionário" + hl(", mas não sua taxa "
                      "de crescimento, que segue nula") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentários convergentes: sem progresso técnico, o produto per capita é constante no "
                             "estado estacionário; reduzir n eleva seu nível, não sua taxa de crescimento. Um dos "
                             "blocos traz “Gabarito: Errado” seguido de um “C” solto, sem justificativa."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 520", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (resumo do Solow sem progresso técnico no 📖)"}],
        "alertas": ["nota_redacao: um bloco do verso traz “Gabarito: Errado **C**”; prevaleceu o ERRADO indicado "
                    "pela fonte e por todos os comentários",
                    "quase_duplicata: ECO-E2-L01057-1, ECO-E2-L01251-1"],
    },
    # ------------------------------------------------------------------ E2-L01732
    {
        "id": "ECO-E2-L01732-1", "fonte_ref": "E2-L01732", "destino": "56", "subtema": H2["ee"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_SOLOW,
        "rotulo_item": "Item",
        "assertiva": ("Quanto maior a taxa de poupança de uma economia, maior será a renda per capita em estado "
                      "estacionário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto maior a taxa de poupança de uma economia, maior será a <u>renda per capita</u> em "
                      "estado estacionário."),
        "poucas": ("s maior → curva de investimento mais alta → " + vd("k* maior") + " → " + vd("y* = f(k*) "
                   "maior") + ". Efeito de " + azb("nível") + ", permanente."),
        "destrinchando": [
            "Condição de estado estacionário: s·f(k*) = (n + δ)k*. Um s maior desloca s·f(k) para cima; o "
            "cruzamento com a reta de reposição vai para a direita.",
            "Com Cobb-Douglas: " + vd("y* = [s/(n + δ)]<sup>α/(1−α)</sup>") + " — cresce com s. Com α = 1/3, "
            "dobrar s eleva y* em cerca de 41% (2<sup>0,5</sup>).",
            "O que <b>não</b> cresce com s: a taxa de crescimento per capita no estado estacionário (zero sem "
            "progresso técnico, g com ele). Na transição, sim, o crescimento fica temporariamente maior.",
            "Também não é verdade que mais poupança traga sempre mais <b>consumo</b>: acima da poupança da "
            + azb("regra de ouro") + " (PMgK = n + δ), o consumo de estado estacionário cai.",
            "A banca cobra a mesma frase com “maior será o crescimento da renda per capita em estado "
            "estacionário”, que é ERRADO.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item cobra a palavra exata: “renda per capita” (nível). "
                       "Quem leu muitos itens “poupança não afeta o longo prazo” tende a marcar ERRADO por "
                       "reflexo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a taxa de poupança de uma economia, maior será o crescimento da renda per capita em "
            "estado estacionário.”</i> → ERRADO (troca nível × taxa)",
            "<i>“Quanto maior a taxa de poupança, maior o consumo per capita em estado estacionário.”</i> → "
            "ERRADO (modulador absoluto: só até a regra de ouro)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["quanto maior"], "dificuldade": 1,
        "comentario_fonte": ("Maior poupança eleva o capital por trabalhador e a renda per capita do estado "
                             "estacionário; não afeta a taxa de crescimento de longo prazo, mas eleva "
                             "permanentemente o nível."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 521", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (deslocamento da curva de investimento descrito no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01252-1 (versão ERRADA com “crescimento da renda per capita”), "
                    "ECO-E2-L00897-1"],
    },
]
