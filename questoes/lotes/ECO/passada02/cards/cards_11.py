"""Cards do lote de redação 11 — ECO, passada 02 (nota 27: modelo IS-LM)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "is": "📉 Curva IS",
    "lm": "📈 Curva LM",
    "pol": "🏦 Política fiscal e monetária",
    "ext": "🕳️ Casos extremos",
}

CMD_BOZAN = ("Considerando o modelo IS-LM-BP e as inter-relações entre os mercados de bens, monetário e cambial, "
             "julgue a assertiva a seguir.")

CMD_NAB_3 = "Em relação ao modelo IS-LM, julgue o item a seguir."

CMD_NAB_4 = "Em relação aos modelos macroeconômicos, julgue o item a seguir."

CMD_NAB_KEY = ("Julgue o item a seguir, de acordo com o que a teoria keynesiana dispõe acerca da demanda efetiva e "
               "da oferta e demanda agregadas.")

CMD_NAB_MACRO = "Em relação à teoria macroeconômica, julgue o item a seguir."

CMD_GRAF = ("Considere o gráfico seguinte, em que Y* é o produto de equilíbrio e i* consiste na taxa de juros de "
            "equilíbrio. Com base no gráfico apresentado e no modelo IS-LM, julgue o item a seguir.")

CMD_RT = "Julgue o item a seguir, acerca dos modelos IS-LM e IS-LM-BP."

CMD_DANIEL = "Julgue o item a seguir, relativo ao modelo IS-LM."

FIG_233 = [{"ref": "IMAGEM 233", "tipo_fonte": "GRÁFICO", "lado": "frente", "acao": "redesenhada"}]

ALERTA_233 = ("figura_conjectural: ECO-E2-L01352-1-F1 redesenhada a partir da descrição da IMAGEM 233 (IS "
              "decrescente × LM crescente, equilíbrio em (Y*, i*)); inclinações e posições não preservadas")

EXCERTO_CACD = (
    "<p><i>Função de produção agregada: Y = F(K, N), com F<sub>K</sub> &gt; 0, F<sub>N</sub> &gt; 0, "
    "F<sub>KN</sub> &gt; 0, F<sub>NN</sub> &lt; 0, F<sub>KK</sub> &lt; 0, em que F<sub>i</sub> é a primeira "
    "derivada da função de produção com relação ao insumo i, e F<sub>ii</sub> é a segunda derivada da função de "
    "produção com relação ao insumo i.</i></p>"
    "<p><i>Demanda de trabalho em termos reais: [...]</i></p>"
    "<p><i>Função investimento: I = I(q(K, N, r − π) − 1), com I′ &lt; 0, em que I′ é a derivada do "
    "investimento em relação à taxa de juros.</i></p>"
    "<p><i>Função consumo: C = C(Y − T), com 0 &lt; C′ &lt; 1, em que C′ é a derivada do consumo em relação à "
    "renda disponível.</i></p>"
    "<p><i>Equilíbrio no mercado de bens: Y = C + I + G + δK (5)</i></p>"
    "<p><i>Equilíbrio monetário: M/P = m(Y, r) (6)</i></p>"
    "<p><i>Em que Y é o produto, N o emprego, K o estoque de capital, w o salário nominal, P o nível geral de "
    "preços, I o investimento, q o Q de Tobin, r a taxa nominal de juros, π a taxa de inflação, C o consumo, T "
    "os tributos autônomos, G os gastos autônomos do governo, m(Y, r) a demanda real por moeda, M o estoque "
    "nominal de moeda e δK a taxa de depreciação do estoque de capital.</i></p>"
    "<p><i>Considere, ainda, um regime em que o governo (via Banco Central) controla exogenamente a quantidade "
    "de moeda M e o estoque de capital é constante no tempo.</i></p>"
)

CARDS = [
    # ------------------------------------------------------------------ E1-0704
    {
        "id": "ECO-E1-0704-1", "fonte_ref": "E1-0704", "destino": "27", "subtema": H2["lm"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca do modelo IS-LM e dos efeitos da política monetária, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Uma política monetária expansionista desloca a curva LM para a esquerda, elevando a taxa de "
                      "juros e reduzindo o produto agregado, independentemente da mobilidade de capitais e do "
                      "regime cambial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma política monetária expansionista desloca a curva LM para a ") + vm("esquerda")
                    + az(", ") + vm("elevando") + az(" a taxa de juros e ") + vm("reduzindo")
                    + az(" o produto agregado, ") + vm("independentemente") + az(" da mobilidade de capitais e "
                                                                                    "do regime cambial.")),
        "poucas": ("A expansão monetária desloca a LM para a " + azb("direita (para baixo)") + ": os juros caem e o "
                   "produto sobe. E, em economia aberta, o resultado " + vm("depende") + " do regime cambial e da "
                   "mobilidade de capitais."),
        "destrinchando": [
            "A " + azb("curva LM") + " reúne os pares (Y, i) que equilibram o mercado monetário: M/P = L(Y, i), "
            "com L crescente na renda (motivos transação e precaução) e decrescente nos juros (motivo "
            "especulação). Com mais moeda real em circulação, o mercado só se reequilibra com juros menores a "
            "cada nível de renda, ou com renda maior a cada taxa de juros: a LM vai para " + vd("baixo/direita")
            + ".",
            "Mecanismo de transmissão: " + vd("M ↑ → i ↓ → I ↑ → Y ↑") + " (com o multiplicador amplificando "
            "a alta do investimento). A IS não se move: a economia desliza ao longo dela até o novo equilíbrio.",
            "O deslocamento para a esquerda, com juros maiores e produto menor, é o de uma política monetária "
            + azb("contracionista") + " (venda de títulos, alta do compulsório, redução de M).",
            "O “independentemente” é o segundo erro. No " + azb("IS-LM-BP") + " (Mundell-Fleming), com "
            "mobilidade perfeita de capitais: sob " + vd("câmbio flutuante") + ", a política monetária é muito "
            "eficaz (a queda de i deprecia o câmbio e soma exportações líquidas); sob " + vd("câmbio fixo")
            + ", é ineficaz, porque a saída de capitais obriga o Banco Central a vender reservas e a LM volta ao "
            "ponto de partida.",
            vm("Regra-âncora: expansão monetária → LM para a direita → i ↓ e Y ↑ (na economia fechada)."),
        ],
        "grafico_verso": "ECO-E1-0704-1-V1",
        "dissecando": (cz("[inversão · modulador absoluto]") + " O item descreve com coerência interna os efeitos "
                       "de uma contração (LM à esquerda → i↑, Y↓) e os atribui à expansão; depois acrescenta um "
                       "“independentemente” que apaga justamente o que o Mundell-Fleming ensina. Pista: “expansionista” "
                       "combinado com “reduzindo o produto”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma política monetária contracionista desloca a curva LM para a esquerda, elevando a taxa de "
            "juros e reduzindo o produto.”</i> → CERTO",
            "<i>“Sob câmbio fixo e perfeita mobilidade de capitais, a expansão monetária eleva o produto de forma "
            "duradoura.”</i> → ERRADO (inversão: nesse regime a política monetária é ineficaz)",
        ])],
        "reescrita": ("Uma política monetária expansionista desloca a curva LM para a " + hl("direita") + ", "
                      + hl("reduzindo") + " a taxa de juros e " + hl("elevando") + " o produto agregado, "
                      + hl("mas seu efeito final depende") + " da mobilidade de capitais e do regime cambial."),
        "tipo_erro": ["INVERSAO", "GENERALIZACAO"], "moduladores": ["independentemente"], "dificuldade": 1,
        "comentario_fonte": "Expansão monetária desloca a LM para a direita (e para baixo), reduz juros e estimula "
                            "investimento e produto; o deslocamento para a esquerda é de política contracionista.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01485-1, ECO-E2-L01353-1 (mesmo mecanismo: expansão monetária "
                    "desloca a LM para baixo/direita)"],
    },
    # ------------------------------------------------------------------ E1-0814
    {
        "id": "ECO-E1-0814-1", "fonte_ref": "E1-0814", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": ("Considere uma economia descrita pelo seguinte sistema de equações, em tempo contínuo. A "
                    "respeito dessa economia, julgue o item que se segue."),
        "excerto": EXCERTO_CACD,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento dos gastos autônomos do governo G desloca a curva IS, elevando o produto de "
                      "equilíbrio Y e a taxa de juros real r; a elevação de r reduz o investimento privado I(r), de "
                      "modo que parte do aumento de G é compensado por crowding-out sobre o investimento, e o "
                      "tamanho desse efeito depende da sensibilidade do investimento ao juro e da inclinação da "
                      "curva LM."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento dos gastos autônomos do governo G desloca a curva IS, elevando o produto de "
                      "equilíbrio Y e a taxa de juros real r; a elevação de r reduz o investimento privado I(r), de "
                      "modo que <u>parte</u> do aumento de G é compensado por crowding-out sobre o investimento, e o "
                      "tamanho desse efeito <u>depende da sensibilidade do investimento ao juro e da inclinação da "
                      "curva LM</u>."),
        "poucas": ("É o " + azb("crowding-out parcial") + " do IS-LM: G ↑ desloca a IS, Y e r sobem, e a alta de r "
                   "corta parte do investimento. Quanto mais I reage ao juro e mais inclinada a LM, maior a "
                   "expulsão."),
        "destrinchando": [
            "O sistema é um IS-LM com moeda exógena: a equação (5) é a IS (bens) e a (6) é a LM (moeda). Como "
            "M é fixado pelo Banco Central e K é constante, um choque em G mexe só na IS.",
            "Sequência: G ↑ → demanda por bens ↑ → Y ↑ → demanda por moeda m(Y, r) ↑ → com M/P fixo, r precisa "
            "subir para reequilibrar o mercado monetário → I ↓ (I′ &lt; 0). A renda sobe, mas menos do que "
            "subiria com juros constantes: parte do gasto público ocupa o lugar do investimento privado.",
            "Tamanho do multiplicador com juros endógenos: " + vd("ΔY/ΔG = 1 / [(1 − c) + b·k/h]") + ", em que "
            "c é a propensão marginal a consumir, b a sensibilidade do investimento ao juro, k a sensibilidade "
            "da demanda por moeda à renda e h a sensibilidade aos juros. O crowding-out cresce com " + vd("b")
            + " e com a inclinação da LM (" + vd("k/h") + ").",
            "Casos-limite: LM horizontal (h → ∞, armadilha da liquidez) → crowding-out nulo; LM vertical "
            "(h = 0, caso clássico) → crowding-out total; investimento insensível ao juro (b = 0, IS vertical) "
            "→ crowding-out nulo.",
            "Sobre a notação: no enunciado, r é a taxa <b>nominal</b> e o investimento depende de r − π (via "
            "Q de Tobin). Com π dado no curto prazo, a alta de r eleva também o juro real, e o raciocínio do "
            "item se mantém.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O item reproduz o roteiro do manual e se "
                       "protege com “parte do aumento” (crowding-out parcial, não total) e com os dois "
                       "determinantes certos do tamanho do efeito. A armadilha seria trocar “parte” por “todo” "
                       "ou citar a inclinação da IS como determinante independente do investimento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…de modo que todo o aumento de G é compensado por crowding-out sobre o investimento…”</i> → "
            "ERRADO (modulador absoluto: só com LM vertical)",
            "<i>“…e o tamanho desse efeito é tanto maior quanto mais sensível a demanda por moeda for à taxa de "
            "juros.”</i> → ERRADO (inversão: demanda por moeda mais sensível ao juro achata a LM e reduz o "
            "crowding-out)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["parte", "depende"], "dificuldade": 2,
        "comentario_fonte": "Verso sem comentário (só o gabarito CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: a equação da demanda de trabalho em termos reais não foi preservada na fonte "
                    "(substituída por [...]); não interfere no julgamento do item",
                    "quase_duplicata: ECO-E2-L00563-1 (mesmo mecanismo de crowding-out)"],
    },
    # ------------------------------------------------------------------ E1-0872
    {
        "id": "ECO-E1-0872-1", "fonte_ref": "E1-0872", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DANIEL,
        "rotulo_item": "Item",
        "assertiva": ("O caso da armadilha da liquidez ocorre quando a demanda por moeda é infinitamente elástica "
                      "com relação à taxa de juros. Nesse cenário, a curva LM encontra-se na horizontal e a política "
                      "monetária é inoperante pois a queda dos juros não leva a um aumento do nível de "
                      "investimentos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O caso da armadilha da liquidez ocorre quando a demanda por moeda é <u>infinitamente "
                      "elástica</u> com relação à taxa de juros. Nesse cenário, a curva LM encontra-se na "
                      "<u>horizontal</u> e a política monetária é inoperante <u>pois a queda dos juros não leva a um "
                      "aumento do nível de investimentos</u>."),
        "poucas": ("Definição e consequência estão certas: demanda por moeda " + azb("infinitamente elástica")
                   + " → LM horizontal → política monetária inoperante. A justificativa final, porém, é imprecisa: "
                   "na armadilha, os juros <b>não caem</b>."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá CERTO, e a leitura usual da banca aceita o item. Mas o motivo da ineficácia "
                          "na armadilha da liquidez é que a moeda nova é entesourada e " + vm("os juros não "
                          "caem") + "; “a queda dos juros não eleva o investimento” descreve outro caso extremo, o "
                          "da " + azb("IS vertical") + " (investimento insensível aos juros). Uma banca rigorosa "
                          "poderia dar ERRADO pelo nexo causal.")],
        "destrinchando": [
            "Na " + azb("armadilha da liquidez") + ", os juros estão tão baixos que todos esperam que subam — e, "
            "com isso, que os títulos percam valor. Reter moeda passa a ser a melhor aplicação: a demanda "
            "especulativa por moeda torna-se infinitamente elástica ao juro, e a LM fica horizontal.",
            "Expansão monetária nesse trecho: o Banco Central compra títulos, o público guarda a moeda recebida "
            "(entesouramento) e a taxa de juros não se move. Sem queda de juros, o canal " + vd("M ↑ → i ↓ → "
            "I ↑ → Y ↑") + " trava no primeiro elo.",
            "Os dois “casos keynesianos” de ineficácia monetária são distintos: (1) " + azb("armadilha da "
            "liquidez") + " — LM horizontal, os juros não caem; (2) " + azb("armadilha do investimento") + " — "
            "IS vertical, os juros caem, mas o investimento não reage. Nos dois, a política fiscal é plenamente "
            "eficaz.",
            "Origem: " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) admitiu a possibilidade; a formalização "
            "gráfica veio com o IS-LM de " + oc("Hicks") + " (1937).",
            vm("Regra-âncora: armadilha da liquidez = os juros não caem; IS vertical = os juros caem, mas o "
               "investimento não responde."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " As duas primeiras afirmações são de manual; o risco está "
                       "no “pois”, que empresta a justificativa do caso da IS vertical. O gabarito oficial "
                       "relevou a imprecisão, mas em prova vale desconfiar de explicações causais trocadas entre "
                       "os dois casos extremos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a política monetária é inoperante, pois a expansão da moeda não consegue reduzir a taxa de "
            "juros.”</i> → CERTO",
            "<i>“O caso da armadilha da liquidez ocorre quando a demanda por moeda é totalmente insensível à taxa "
            "de juros.”</i> → ERRADO (troca de conceito: esse é o caso clássico, LM vertical)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["infinitamente"], "dificuldade": 2,
        "comentario_fonte": "Verso só com o gabarito CERTO e uma imagem não preservada (link de canal do Telegram).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (288).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; conteúdo refeito no 📖)"}],
        "alertas": ["contestavel: a justificativa “a queda dos juros não leva a um aumento do investimento” é a do "
                    "caso da IS vertical; na armadilha da liquidez os juros não caem. Mantido o CERTO da fonte",
                    "texto_corrigido: “a a curva LM” → “a curva LM” (erro de digitação da fonte)",
                    "quase_duplicata: ECO-E2-L00295-1, ECO-E2-L00683-1, ECO-E2-L01027-1"],
    },
    # ------------------------------------------------------------------ E1-0873
    {
        "id": "ECO-E1-0873-1", "fonte_ref": "E1-0873", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DANIEL,
        "rotulo_item": "Item",
        "assertiva": ("Uma forte expansão fiscal, com redução de impostos e aumento de gastos, tem como "
                      "consequência uma redução dos juros. Esse movimento pode ser explicado pelo deslocamento da "
                      "curva IS para a esquerda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma forte expansão fiscal, com redução de impostos e aumento de gastos, tem como "
                       "consequência uma ") + vm("redução") + az(" dos juros. Esse movimento pode ser explicado "
                                                                   "pelo deslocamento da curva IS para a ")
                    + vm("esquerda") + az(".")),
        "poucas": ("Expansão fiscal desloca a IS para a " + azb("direita") + ": com a LM positivamente inclinada, "
                   "renda e " + vd("juros sobem") + ". IS para a esquerda é contração fiscal."),
        "destrinchando": [
            "A " + azb("curva IS") + " reúne os pares (Y, i) que equilibram o mercado de bens: Y = C(Y − T) + I(i) "
            "+ G. Mais G ou menos T elevam a demanda a cada taxa de juros, e a curva vai para a direita (para "
            "cima).",
            "Novo equilíbrio: a renda maior eleva a demanda por moeda para transações; com a oferta de moeda "
            "fixa, os juros precisam subir para reequilibrar o mercado monetário. Resultado: " + vd("Y ↑ e "
            "i ↑") + ", com algum " + azb("crowding-out") + " do investimento privado.",
            "Os juros só cairiam com expansão fiscal se alguém mexesse também na LM (expansão monetária "
            "simultânea, o chamado “mix” de políticas) — o que o item não menciona.",
            "IS para a esquerda (contração fiscal: menos gasto, mais imposto) produz o contrário: Y ↓ e i ↓.",
            vm("Regra-âncora: política fiscal mexe na IS; expansão fiscal com LM inclinada → Y ↑ e i ↑."),
        ],
        "dissecando": (cz("[inversão]") + " Dois sinais trocados que se apoiam: o efeito sobre os juros e o "
                       "sentido do deslocamento. Como “IS para a esquerda → juros menores” é verdade isolada, o "
                       "item parece coerente; a pista é que a causa (expansão) não combina com a curva indo para "
                       "a esquerda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma forte contração fiscal tem como consequência uma redução dos juros, explicada pelo "
            "deslocamento da IS para a esquerda.”</i> → CERTO",
            "<i>“Uma forte expansão fiscal eleva os juros, o que se explica pelo deslocamento da LM para a "
            "esquerda.”</i> → ERRADO (curva trocada: a fiscal desloca a IS)",
        ])],
        "reescrita": ("Uma forte expansão fiscal, com redução de impostos e aumento de gastos, tem como consequência "
                      "uma " + hl("elevação") + " dos juros. Esse movimento pode ser explicado pelo deslocamento da "
                      "curva IS para a " + hl("direita") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito ERRADO e uma imagem não preservada (link de canal do Telegram).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (284).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; conteúdo refeito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00139
    {
        "id": "ECO-E2-L00139-1", "fonte_ref": "E2-L00139", "destino": "27", "subtema": H2["is"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM-BP, um aumento da taxa de juros impacta diretamente o mercado de bens, já "
                      "que produz incentivos para que os agentes invistam valores nos bancos em busca de "
                      "rendimentos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo IS-LM-BP, um aumento da taxa de juros impacta diretamente o mercado de bens, já "
                       "que ") + vm("produz incentivos para que os agentes invistam valores nos bancos em busca de "
                                    "rendimentos") + az(".")),
        "poucas": ("O canal juros → mercado de bens é o " + azb("investimento produtivo") + " das firmas, que "
                   + vd("cai") + " quando o juro sobe. Aplicar dinheiro no banco é decisão de portfólio, não "
                   "investimento no sentido macroeconômico."),
        "destrinchando": [
            "Em macroeconomia, " + azb("investimento (I)") + " é formação de capital: máquinas, instalações, "
            "construção, estoques. Comprar título ou depositar no banco é " + azb("poupança financeira") + " — "
            "alocação de riqueza entre ativos.",
            "A firma investe enquanto a " + azb("eficiência marginal do capital") + " (" + oc("Keynes") + ") "
            "supera o juro, que é o custo do financiamento ou o rendimento que ela deixa de ganhar aplicando os "
            "recursos. Juro maior elimina projetos marginais: " + vd("I = I(i), com dI/di &lt; 0") + ".",
            "Daí a " + azb("curva IS") + " decrescente: i ↑ → I ↓ → demanda agregada ↓ → Y ↓ (ampliado pelo "
            "multiplicador). É movimento <b>ao longo</b> da IS, não deslocamento.",
            "A troca entre moeda e títulos conforme o juro existe, mas pertence ao mercado monetário: é o motivo "
            "especulação da " + azb("preferência pela liquidez") + ", que dá inclinação à LM.",
            "No IS-LM-BP há um canal adicional: juro doméstico maior atrai capital externo, aprecia o câmbio (sob "
            "flutuação) e reduz as exportações líquidas, reforçando a queda de Y.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item explora o sentido coloquial de “investir” (aplicar "
                       "dinheiro) e o encaixa no lugar do investimento macroeconômico. A primeira oração "
                       "(“impacta diretamente o mercado de bens”) é verdadeira; a armadilha está no “já que”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo IS-LM-BP, um aumento da taxa de juros reduz o investimento das firmas em bens de "
            "capital, o que se manifesta como movimento ao longo da IS.”</i> → CERTO",
            "<i>“Um aumento da taxa de juros desloca a curva IS para a esquerda.”</i> → ERRADO (troca de "
            "conceito: é movimento ao longo da IS)",
        ])],
        "reescrita": ("No modelo IS-LM-BP, um aumento da taxa de juros impacta diretamente o mercado de bens, já "
                      "que " + hl("eleva o custo de oportunidade do investimento produtivo, desestimulando a "
                                  "compra de bens de capital pelas firmas") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Juros maiores encarecem o capital e reduzem o investimento real; aplicar no banco é "
                            "poupança financeira, decisão de portfólio que pertence ao mercado monetário.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 010", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (quadro juros → investimento → demanda, transcrito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00140
    {
        "id": "ECO-E2-L00140-1", "fonte_ref": "E2-L00140", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Em uma política monetária expansiva, a redução da taxa de juros resulta em um aumento no "
                      "investimento, que, por sua vez, causa um deslocamento da curva IS, ao invés da LM, para a "
                      "direita, refletindo o aumento da demanda agregada e consequentemente do produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma política monetária expansiva, a redução da taxa de juros resulta em um aumento no "
                       "investimento, que, por sua vez, ") + vm("causa um deslocamento da curva IS, ao invés da "
                                                                 "LM, para a direita")
                    + az(", refletindo o aumento da demanda agregada e consequentemente do produto.")),
        "poucas": ("Na política monetária, quem se desloca é a " + azb("LM") + ". O investimento que cresce com a "
                   "queda dos juros é " + azb("movimento ao longo da IS") + ": o juro é variável do eixo, não "
                   "deslocador da curva."),
        "destrinchando": [
            "Regra de construção das curvas: tudo o que está nos eixos (i e Y) gera <b>movimento ao longo</b>; "
            "tudo o que fica fora deles gera <b>deslocamento</b>. A IS já incorpora a reação do investimento ao "
            "juro (I = I(i)): por isso ela é decrescente.",
            "Deslocam a " + azb("IS") + ": gastos do governo, impostos, consumo e investimento autônomos "
            "(confiança, expectativas), exportações líquidas autônomas. Deslocam a " + azb("LM") + ": oferta "
            "de moeda nominal, nível de preços (M/P) e mudanças autônomas na demanda por moeda.",
            "Sequência correta da expansão monetária: " + vd("M ↑ → LM para a direita → i ↓ → I ↑ → Y ↑")
            + ". A economia desliza sobre a IS fixa até o novo equilíbrio, com mais produto e juro menor.",
            "Contar o mesmo efeito duas vezes (LM e IS para a direita) superestimaria o resultado da política: "
            "o aumento de I já está no deslizamento sobre a IS.",
            vm("Regra-âncora: monetária desloca a LM; fiscal desloca a IS; juro mexendo no investimento é "
               "movimento ao longo da IS."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item acerta o mecanismo (i ↓ → I ↑ → Y ↑), mas o converte "
                       "em deslocamento da curva errada e ainda nega expressamente a LM (“ao invés da LM”). "
                       "🔥 Movimento × deslocamento é a pegadinha mais frequente em IS-LM."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em uma política monetária expansiva, a LM se desloca para a direita e a redução da taxa de juros "
            "eleva o investimento ao longo da curva IS.”</i> → CERTO",
            "<i>“Uma melhora autônoma das expectativas empresariais desloca a curva IS para a direita.”</i> → "
            "CERTO",
        ])],
        "reescrita": ("Em uma política monetária expansiva, a redução da taxa de juros resulta em um aumento no "
                      "investimento, que, por sua vez, " + hl("corresponde a um movimento ao longo da curva IS, e "
                                                              "não a um deslocamento dela; quem se desloca para a "
                                                              "direita é a LM")
                      + ", refletindo o aumento da demanda agregada e consequentemente do produto."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O deslocamento ocorre na LM, não na IS; a LM vai para a direita com mais moeda, o "
                            "juro cai e estimula o investimento, impactando o produto por meio da IS.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00940-1 (mesmo erro: IS deslocada pela nova taxa de juros)"],
    },
    # ------------------------------------------------------------------ E2-L00295
    {
        "id": "ECO-E2-L00295-1", "fonte_ref": "E2-L00295", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo a casos extremos do modelo IS-LM.",
        "rotulo_item": "Item",
        "assertiva": ("A “Armadilha da Liquidez” descreve uma situação em que a taxa de juros é tão baixa que a "
                      "demanda especulativa por moeda se torna infinitamente elástica (curva LM horizontal), "
                      "tornando a política monetária incapaz de reduzir ainda mais os juros ou estimular a "
                      "economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A “Armadilha da Liquidez” descreve uma situação em que a taxa de juros é <u>tão baixa</u> "
                      "que a <u>demanda especulativa</u> por moeda se torna <u>infinitamente elástica</u> (curva LM "
                      "horizontal), tornando a política monetária incapaz de reduzir ainda mais os juros ou "
                      "estimular a economia."),
        "poucas": ("Definição de manual: juro muito baixo → todos esperam alta do juro → " + azb("demanda "
                   "especulativa") + " por moeda infinitamente elástica → LM horizontal → moeda nova é "
                   "entesourada e os juros " + vd("não caem") + "."),
        "destrinchando": [
            "Por que o juro baixo produz isso: o preço de um título é inversamente ligado ao juro. Com o juro no "
            "piso, a única direção esperada é a alta, ou seja, perda de capital para quem tem títulos. Reter "
            "moeda passa a dominar, e qualquer moeda adicional é guardada (entesouramento).",
            "Na " + azb("preferência pela liquidez") + " de " + oc("Keynes") + ", a demanda por moeda soma os "
            "motivos transação e precaução (dependem da renda) e o motivo especulação (depende do juro). A "
            "armadilha é o caso-limite deste último.",
            "Consequências no IS-LM: política monetária " + vd("ineficaz") + " (LM se “desloca” sobre o trecho "
            "plano sem mudar i); política fiscal com " + vd("eficácia máxima") + " (sem alta de juros, sem "
            "crowding-out, multiplicador pleno).",
            "Exemplos usados pela literatura: Japão nos anos 1990 e economias avançadas após 2008, com juros "
            "próximos de zero. Os bancos centrais recorreram a instrumentos não convencionais, como o "
            + azb("afrouxamento quantitativo") + " e o " + azb("forward guidance") + ".",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição completa, com os três elos certos (juro "
                       "baixo, demanda especulativa, elasticidade infinita). Versões ERRADAS costumam trocar "
                       "“infinitamente elástica” por “inelástica” ou atribuir a ineficácia à política fiscal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a demanda especulativa por moeda se torna perfeitamente inelástica (curva LM vertical)…”</i> → "
            "ERRADO (troca de conceito: esse é o caso clássico)",
            "<i>“…tornando a política fiscal incapaz de estimular a economia.”</i> → ERRADO (inversão: a fiscal "
            "tem eficácia máxima)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["infinitamente"], "dificuldade": 1,
        "comentario_fonte": "Agentes preferem entesourar a liquidez adicional, pois esperam alta do juro e queda "
                            "do preço dos títulos; a política monetária perde potência.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00683-1, ECO-E1-0872-1, ECO-E2-L01027-1"],
    },
    # ------------------------------------------------------------------ E2-L00484
    {
        "id": "ECO-E2-L00484-1", "fonte_ref": "E2-L00484", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito de moeda e política monetária, julgue o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo IS-LM, se o Banco Central fixar a taxa básica de juros da economia, "
                      "então choques no multiplicador monetário não afetarão a economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando o modelo IS-LM, se o Banco Central <u>fixar a taxa básica de juros</u> da "
                      "economia, então choques no <u>multiplicador monetário</u> não afetarão a economia."),
        "poucas": ("Com " + azb("meta de juros") + ", a LM fica horizontal no juro-alvo: o Banco Central ajusta a "
                   "base monetária para absorver qualquer choque monetário, e Y e i não mudam."),
        "destrinchando": [
            "Oferta de moeda = " + vd("multiplicador × base monetária") + ". Choques no multiplicador (mudança "
            "na preferência do público por papel-moeda, nas reservas voluntárias dos bancos) alteram M mesmo "
            "sem ação do Banco Central e, com base fixa, deslocariam a LM.",
            "Se o instrumento é o juro, o Banco Central se compromete a ofertar ou retirar a moeda que for "
            "necessária para manter i no alvo. A LM torna-se horizontal no juro fixado, e a oferta de moeda "
            "passa a ser " + azb("endógena") + ": o choque no multiplicador é compensado por variação da base.",
            "O outro lado da moeda: com juro fixo, choques na " + azb("IS") + " (gasto, confiança, exportações) "
            "passam inteiros para a renda, sem o amortecimento da alta de juros.",
            "É a lição de " + oc("William Poole") + " (1970) sobre a escolha do instrumento: se predominam "
            "choques monetários (LM instável), meta de juros estabiliza melhor o produto; se predominam choques "
            "de demanda (IS instável), meta de agregado monetário é preferível.",
            "No " + rx("Brasil") + ", o Copom fixa a meta da Selic, e o Banco Central opera no mercado aberto "
            "para manter a taxa efetiva junto à meta — na prática, um regime de juro como instrumento.",
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Parece estranho dizer que um choque monetário "
                       "“não afeta a economia”, mas é exatamente o que a meta de juros garante no IS-LM. A banca "
                       "costuma cobrar o par: meta de juros neutraliza choques na LM e deixa passar choques na "
                       "IS."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se o Banco Central fixar a taxa básica de juros, então choques na demanda agregada não afetarão "
            "o produto.”</i> → ERRADO (troca de conceito: choques na IS passam inteiros para Y)",
            "<i>“…se o Banco Central fixar a oferta de moeda, choques no multiplicador monetário deslocarão a "
            "LM.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Com regra de juros, a LM é horizontal no juro-alvo; o BC ajusta a base monetária e "
                            "neutraliza choques no multiplicador; não há efeito sobre o produto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00561
    {
        "id": "ECO-E2-L00561-1", "fonte_ref": "E2-L00561", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("Uma política monetária expansionista tem efeito pequeno no modelo em que a IS é pouco "
                      "inclinada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma política monetária expansionista tem efeito ") + vm("pequeno")
                    + az(" no modelo em que a IS é pouco inclinada.")),
        "poucas": ("IS pouco inclinada (plana) = investimento " + azb("muito sensível aos juros") + ": a queda de "
                   "i gerada pela expansão monetária vira grande aumento de Y. O efeito é " + vd("grande") + "."),
        "destrinchando": [
            "A inclinação da IS mede quanto a demanda por bens reage ao juro. IS plana: pequena variação de i "
            "provoca grande variação de I e, via multiplicador, de Y. IS inclinada (no limite, vertical): o "
            "investimento quase não reage.",
            "A política monetária atua <b>pela</b> IS: desloca a LM, reduz i e depende da resposta do "
            "investimento para mover o produto. Por isso: " + vd("IS plana → monetária forte") + "; "
            + vd("IS inclinada → monetária fraca") + " (IS vertical → ineficaz).",
            "Para a política fiscal, a lógica se inverte: com IS plana, a alta dos juros após a expansão fiscal "
            "derruba muito o investimento (crowding-out grande), e a fiscal perde força.",
            "Tabela de bolso: monetária forte com " + azb("LM inclinada") + " e " + azb("IS plana")
            + "; fiscal forte com " + azb("LM plana") + " e " + azb("IS inclinada") + ".",
        ],
        "grafico_verso": "ECO-E2-L00561-1-V1",
        "dissecando": (cz("[inversão]") + " Inverte a relação entre a inclinação da IS e a eficácia monetária. "
                       "O vocabulário ajuda a errar: “pouco inclinada” soa como “pouco efeito”. Traduza sempre a "
                       "inclinação em sensibilidade: IS plana = investimento muito sensível ao juro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma política fiscal expansionista tem efeito pequeno no modelo em que a IS é pouco "
            "inclinada.”</i> → CERTO",
            "<i>“Se o investimento for insensível à taxa de juros, a política monetária terá eficácia "
            "máxima.”</i> → ERRADO (inversão: IS vertical anula a monetária)",
        ])],
        "reescrita": ("Uma política monetária expansionista tem efeito " + hl("grande") + " no modelo em que a IS "
                      "é pouco inclinada."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "IS plana indica investimento muito sensível ao juro; a pequena queda de juros gera "
                            "grande expansão do investimento e do produto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00562
    {
        "id": "ECO-E2-L00562-1", "fonte_ref": "E2-L00562", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": "No caso clássico, o aumento dos gastos do governo expande a renda.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No caso clássico, o aumento dos gastos do governo ") + vm("expande") + az(" a renda."),
        "poucas": ("No " + azb("caso clássico") + " a LM é vertical: a expansão fiscal só eleva os juros, o "
                   "investimento privado cai na mesma medida (" + vd("crowding-out total") + ") e a renda não "
                   "muda."),
        "destrinchando": [
            "Caso clássico = demanda por moeda " + azb("insensível ao juro") + " (só motivo transação, como na "
            "teoria quantitativa: M/P = kY). Com M/P fixo, só existe uma renda compatível com o equilíbrio "
            "monetário: a LM é vertical.",
            "Expansão fiscal: a IS vai para a direita, mas a renda está “travada” pela LM. O ajuste é todo no "
            "juro, que sobe até o investimento (e o consumo sensível ao juro) cair exatamente o que o governo "
            "passou a gastar: " + vd("ΔI = −ΔG") + ".",
            "Na versão de fundos emprestáveis, o governo disputa a mesma poupança com as empresas: o juro sobe e "
            "expulsa o gasto privado. A composição do produto muda (mais G, menos I); o nível, não.",
            "Espelho: no caso clássico, a " + azb("política monetária") + " tem eficácia máxima (desloca a LM "
            "vertical e move Y por inteiro). Na " + azb("armadilha da liquidez") + " (LM horizontal), vale o "
            "oposto.",
            vm("Regra-âncora: LM vertical → fiscal nula, monetária máxima; LM horizontal → fiscal máxima, "
               "monetária nula."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item aplica ao caso clássico a intuição keynesiana do "
                       "multiplicador. Item curto, sem moduladores: o julgamento depende só de saber o que o "
                       "rótulo “caso clássico” significa no IS-LM."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No caso clássico, o aumento dos gastos do governo eleva a taxa de juros e reduz o investimento "
            "privado no mesmo montante.”</i> → CERTO",
            "<i>“No caso clássico, a expansão monetária não altera a renda.”</i> → ERRADO (inversão: é a "
            "política mais eficaz nesse caso)",
        ])],
        "reescrita": "No caso clássico, o aumento dos gastos do governo " + hl("não expande") + " a renda.",
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "LM vertical; a expansão fiscal eleva o juro até o investimento cair na mesma "
                            "magnitude do gasto público: crowding-out completo, sem efeito sobre a renda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00684-1, ECO-E2-L01444-1 (LM vertical e crowding-out total)"],
    },
    # ------------------------------------------------------------------ E2-L00563
    {
        "id": "ECO-E2-L00563-1", "fonte_ref": "E2-L00563", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("O efeito crowding out ocorre quando o governo aumenta os gastos ou reduz impostos, o que "
                      "aumenta a demanda agregada e, consequentemente, a taxa de juros, levando a uma redução dos "
                      "investimentos privados."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O efeito crowding out ocorre quando o governo aumenta os gastos ou reduz impostos, o que "
                      "aumenta a demanda agregada e, <u>consequentemente, a taxa de juros</u>, levando a uma "
                      "<u>redução dos investimentos privados</u>."),
        "poucas": ("É a definição do " + azb("efeito deslocamento") + ": a expansão fiscal eleva a renda, a "
                   "demanda por moeda e os juros, e o juro maior " + vd("expulsa parte do investimento "
                   "privado") + "."),
        "destrinchando": [
            "Cadeia completa: G ↑ (ou T ↓) → demanda agregada ↑ → Y ↑ → demanda por moeda para transações ↑ → "
            "com oferta de moeda fixa, " + vd("i ↑") + " → " + vd("I ↓") + ". O produto final sobe menos do que "
            "o multiplicador simples prometeria.",
            "No gráfico, a distância entre o equilíbrio que haveria com juros constantes (multiplicador pleno) e "
            "o equilíbrio efetivo mede o " + azb("crowding-out") + ".",
            "Tamanho: maior quanto mais " + azb("inclinada a LM") + " (demanda por moeda pouco sensível ao "
            "juro) e quanto mais " + azb("plana a IS") + " (investimento sensível ao juro). Total no caso "
            "clássico (LM vertical); nulo na armadilha da liquidez (LM horizontal).",
            "Existem outras versões do conceito, fora do IS-LM básico: crowding-out por apreciação cambial no "
            "Mundell-Fleming e o efeito via expectativas de impostos futuros (" + oc("Barro") + ", "
            "equivalência ricardiana).",
        ],
        "grafico_verso": "ECO-E2-L00563-1-V1",
        "dissecando": (cz("[literalidade]") + " Definição de manual, com a cadeia causal na ordem certa (demanda → "
                       "juros → investimento). As versões ERRADAS costumam inverter um elo (“reduzindo a taxa de "
                       "juros”) ou dizer que o crowding-out anula sempre todo o estímulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O efeito crowding out faz com que a política fiscal expansionista seja sempre incapaz de elevar "
            "a renda.”</i> → ERRADO (modulador absoluto: só no caso clássico)",
            "<i>“O crowding out é tanto maior quanto mais sensível o investimento for à taxa de juros.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A expansão fiscal eleva a demanda agregada e os juros; o juro maior desestimula o "
                            "investimento privado, anulando parte do estímulo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0814-1"],
    },
    # ------------------------------------------------------------------ E2-L00615
    {
        "id": "ECO-E2-L00615-1", "fonte_ref": "E2-L00615", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação ao sistema monetário e à política monetária, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A armadilha da liquidez da economia monetária é verificada quando a demanda por moeda é "
                      "inelástica à taxa de juros."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A armadilha da liquidez da economia monetária é verificada quando a demanda por moeda é ")
                    + vm("inelástica") + az(" à taxa de juros.")),
        "poucas": ("Na armadilha da liquidez, a demanda por moeda é " + azb("infinitamente elástica") + " ao juro "
                   "(LM horizontal). Demanda " + azb("inelástica") + " ao juro é o caso clássico (LM vertical)."),
        "destrinchando": [
            "Elasticidade da demanda por moeda ao juro = quanto a moeda retida muda quando o juro varia. Ela "
            "define a inclinação da LM: quanto mais elástica, mais plana.",
            vd("Elasticidade infinita") + " → LM horizontal → " + azb("armadilha da liquidez") + ": com juro "
            "muito baixo, o público retém qualquer moeda adicional em vez de comprar títulos que rendem quase "
            "nada e tendem a perder valor.",
            vd("Elasticidade nula") + " → LM vertical → " + azb("caso clássico") + ": a moeda serve só para "
            "transações (teoria quantitativa), e a renda fica determinada pela oferta de moeda.",
            "Eficácia das políticas: armadilha → monetária nula, fiscal máxima; clássico → fiscal nula, "
            "monetária máxima.",
            vm("Regra-âncora: armadilha = elasticidade infinita (LM plana); clássico = elasticidade zero (LM "
               "vertical)."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Troca um extremo pelo outro: a definição "
                       "oferecida é a do caso clássico. 🔥 Item recorrente; o examinador só alterna as palavras "
                       "“elástica” e “inelástica”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A armadilha da liquidez ocorre quando a demanda por moeda é perfeitamente elástica à taxa de "
            "juros.”</i> → CERTO",
            "<i>“Quando a demanda por moeda é inelástica à taxa de juros, a política fiscal tem eficácia "
            "máxima.”</i> → ERRADO (inversão: nesse caso ela é nula)",
        ])],
        "reescrita": ("A armadilha da liquidez da economia monetária é verificada quando a demanda por moeda é "
                      + hl("infinitamente elástica") + " à taxa de juros."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Na armadilha, com juro próximo de zero, a demanda por moeda é perfeitamente "
                            "elástica, não inelástica; o público retém qualquer moeda adicional.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00683
    {
        "id": "ECO-E2-L00683-1", "fonte_ref": "E2-L00683", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_4,
        "rotulo_item": "Item",
        "assertiva": ("A armadilha da liquidez ocorre quando a demanda por moeda é perfeitamente elástica em "
                      "relação à taxa de juros, tornando a curva LM horizontal e a política monetária ineficaz."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A armadilha da liquidez ocorre quando a demanda por moeda é <u>perfeitamente elástica</u> "
                      "em relação à taxa de juros, tornando a curva LM <u>horizontal</u> e a política "
                      "<u>monetária</u> ineficaz."),
        "poucas": ("Os três elos certos: demanda por moeda " + azb("perfeitamente elástica") + " ao juro → "
                   + azb("LM horizontal") + " → política monetária " + vd("ineficaz") + " (a moeda nova é "
                   "entesourada e o juro não cai)."),
        "destrinchando": [
            "Com o juro em nível muito baixo, a expectativa dominante é de alta do juro e de queda do preço dos "
            "títulos. Ninguém quer títulos; qualquer moeda adicional é retida. A sensibilidade da demanda por "
            "moeda ao juro tende a infinito.",
            "Gráfico: a LM tem um trecho plano no juro mínimo. Uma expansão monetária alonga esse trecho, mas "
            "não reduz o juro onde a IS o cruza — o equilíbrio não se move.",
            "Política fiscal, ao contrário, tem " + vd("eficácia máxima") + ": a IS se desloca sobre o trecho "
            "plano, sem alta de juros e sem crowding-out.",
            "Termos sinônimos que a banca usa: “perfeitamente elástica”, “infinitamente elástica”, “demanda "
            "especulativa ilimitada”, “LM horizontal”, “preferência absoluta pela liquidez”.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual em sequência causal correta. O que poderia "
                       "derrubar o item — “inelástica”, “vertical” ou “fiscal” no lugar de “monetária” — não "
                       "aparece."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tornando a curva LM horizontal e a política fiscal ineficaz.”</i> → ERRADO (troca de conceito: "
            "a ineficaz é a monetária)",
            "<i>“…tornando a curva LM vertical e a política monetária ineficaz.”</i> → ERRADO (troca de "
            "conceito: LM vertical é o caso clássico)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["perfeitamente"], "dificuldade": 1,
        "comentario_fonte": "Juro tão baixo que o público retém qualquer liquidez adicional; sensibilidade da "
                            "demanda por moeda tende ao infinito; LM horizontal; monetária ineficaz.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00295-1, ECO-E2-L00615-1, ECO-E2-L00915-1"],
    },
    # ------------------------------------------------------------------ E2-L00684
    {
        "id": "ECO-E2-L00684-1", "fonte_ref": "E2-L00684", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_4,
        "rotulo_item": "Item",
        "assertiva": ("O efeito crowding-out (expulsão) do investimento privado é total quando a curva LM é "
                      "vertical (caso clássico), pois a política fiscal expansionista apenas eleva os juros sem "
                      "alterar o produto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O efeito crowding-out (expulsão) do investimento privado é <u>total</u> quando a curva LM é "
                      "<u>vertical</u> (caso clássico), pois a política fiscal expansionista apenas eleva os juros "
                      "sem alterar o produto."),
        "poucas": ("LM vertical → renda fixada pelo mercado monetário. A expansão fiscal só eleva o juro até o "
                   "investimento privado cair o mesmo que subiu o gasto: " + vd("crowding-out total") + "."),
        "destrinchando": [
            "Por que a LM é vertical: a demanda por moeda não depende do juro (M/P = kY). Dado M/P, só uma renda "
            "equilibra o mercado monetário, qualquer que seja o juro.",
            "Expansão fiscal: a IS se desloca para a direita, mas a interseção com a LM só pode subir. O juro "
            "maior reduz o investimento privado até " + vd("ΔI = −ΔG") + ", e Y fica onde estava.",
            "Note os qualificativos “total” e “apenas”: aqui são verdadeiros porque o caso é extremo. Com LM "
            "positivamente inclinada (caso intermediário), o crowding-out é parcial e Y sobe.",
            "Na mesma configuração, a política monetária tem " + vd("eficácia máxima") + ": deslocar a LM "
            "vertical move a renda por inteiro.",
            "O nome “clássico” vem da teoria quantitativa da moeda, em que a moeda é demandada só para "
            "transações e o juro é determinado por poupança e investimento.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Absolutos (“total”, “apenas”) costumam sinalizar "
                       "ERRADO, mas aqui descrevem corretamente um caso-limite. Antes de punir o modulador, "
                       "confira se o item especificou o caso extremo — aqui, “LM vertical (caso clássico)”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O efeito crowding-out é total quando a curva LM é horizontal.”</i> → ERRADO (inversão: com LM "
            "horizontal ele é nulo)",
            "<i>“Com LM positivamente inclinada, a política fiscal expansionista eleva o produto, mas provoca "
            "crowding-out parcial.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["total", "apenas"], "dificuldade": 1,
        "comentario_fonte": "Demanda por moeda insensível ao juro (teoria quantitativa) → LM vertical; a expansão "
                            "fiscal só eleva o juro até o investimento cair no mesmo montante do gasto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00562-1, ECO-E2-L01444-1"],
    },
    # ------------------------------------------------------------------ E2-L00727
    {
        "id": "ECO-E2-L00727-1", "fonte_ref": "E2-L00727", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação aos conceitos macroeconômicos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando-se um modelo IS-LM sem o caso clássico e sem armadilha da liquidez, uma "
                      "política fiscal expansionista reduz a demanda por moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando-se um modelo IS-LM sem o caso clássico e sem armadilha da liquidez, uma "
                       "política fiscal expansionista ") + vm("reduz a demanda por moeda") + az(".")),
        "poucas": ("A expansão fiscal eleva a renda e, com ela, a " + azb("demanda por moeda para transações")
                   + "; é essa pressão que, com oferta de moeda fixa, " + vd("faz os juros subirem") + ". Nada "
                   "nela reduz a demanda por moeda."),
        "destrinchando": [
            "Demanda por moeda keynesiana: L(Y, i) = kY − hi. Cresce com a renda (motivos transação e "
            "precaução) e cai com o juro (motivo especulação).",
            "Expansão fiscal com LM inclinada: IS para a direita → Y ↑ → a demanda por moeda para transações "
            "aumenta → como M/P é fixo, o juro sobe para reequilibrar o mercado → i ↑ reduz a demanda "
            "especulativa.",
            "No novo equilíbrio, a quantidade total demandada volta a igualar a oferta, que não mudou: o que se "
            "altera é a <b>composição</b> — mais moeda para transações, menos para especulação. O impulso "
            "inicial, porém, é sempre de " + vd("aumento") + " da demanda, nunca de redução.",
            "Por que o item exclui os casos extremos: no clássico (LM vertical), Y não muda e só o juro sobe; na "
            "armadilha (LM horizontal), o juro não sobe e a moeda adicional demandada é suprida pelo trecho "
            "plano. No caso intermediário, os dois efeitos (Y ↑ e i ↑) aparecem juntos.",
            vm("Regra-âncora: expansão fiscal → Y ↑ → demanda por moeda ↑ → i ↑ → crowding-out parcial."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sinal do efeito da renda sobre a demanda por moeda. A "
                       "menção aos dois casos extremos é distração: serve só para garantir o caso intermediário, "
                       "em que renda e juros sobem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política fiscal expansionista eleva a renda e a taxa de juros de equilíbrio.”</i> → CERTO",
            "<i>“…uma política fiscal expansionista eleva a renda sem alterar a taxa de juros.”</i> → ERRADO "
            "(caso trocado: só na armadilha da liquidez)",
        ])],
        "reescrita": ("Considerando-se um modelo IS-LM sem o caso clássico e sem armadilha da liquidez, uma "
                      "política fiscal expansionista " + hl("eleva a demanda por moeda para transações, o que, com "
                                                            "oferta de moeda fixa, eleva a taxa de juros") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A expansão fiscal desloca a IS para a direita e eleva a renda; a demanda por moeda "
                            "depende positivamente da renda e tende a aumentar, não a reduzir.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: comentário de E2-L00782 (mesmo item, mesma prova) fundido neste card"],
    },
    # ------------------------------------------------------------------ E2-L00914
    {
        "id": "ECO-E2-L00914-1", "fonte_ref": "E2-L00914", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_KEY,
        "rotulo_item": "Item",
        "assertiva": ("Considere o modelo IS-LM. Quando o público está disposto a reter qualquer quantidade de "
                      "moeda que o Banco Central coloque em circulação à taxa de juros vigente, denomina-se esse "
                      "caso como crowding-out."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considere o modelo IS-LM. Quando o público está disposto a reter qualquer quantidade de "
                       "moeda que o Banco Central coloque em circulação à taxa de juros vigente, denomina-se esse "
                       "caso como ") + vm("crowding-out") + az(".")),
        "poucas": ("Reter qualquer quantidade de moeda ao juro vigente é a " + azb("armadilha da liquidez")
                   + " (LM horizontal). " + azb("Crowding-out") + " é outra coisa: a expulsão do gasto privado "
                   "pela alta de juros após uma expansão fiscal."),
        "destrinchando": [
            azb("Armadilha da liquidez") + ": a demanda por moeda é infinitamente elástica ao juro; o Banco "
            "Central injeta moeda e o público a entesoura, sem que o juro caia. LM horizontal; política "
            "monetária ineficaz; política fiscal plenamente eficaz.",
            azb("Crowding-out") + " (efeito deslocamento): a expansão fiscal eleva a renda, a demanda por moeda "
            "e o juro; o juro maior reduz investimento e consumo privados. A magnitude depende da inclinação da "
            "LM: " + vd("total") + " no caso clássico (LM vertical), " + vd("parcial") + " no caso "
            "intermediário e " + vd("nulo") + " na armadilha.",
            "Ou seja, os dois conceitos são opostos: onde há armadilha da liquidez, não há crowding-out.",
            "Leitura por fundos emprestáveis: com a poupança das famílias como fonte limitada de recursos, o "
            "governo deficitário concorre com as empresas, eleva o juro e desloca o gasto privado.",
            vm("Regra-âncora: armadilha da liquidez descreve o mercado monetário (moeda retida); crowding-out "
               "descreve o efeito da política fiscal (gasto privado expulso)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A descrição é a definição exata da armadilha da liquidez; só "
                       "o nome foi trocado. A pista: “reter qualquer quantidade de moeda” fala de demanda por "
                       "moeda, não de investimento privado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…denomina-se esse caso como armadilha da liquidez, em que o crowding-out é nulo.”</i> → CERTO",
            "<i>“O crowding-out é máximo quando o público está disposto a reter qualquer quantidade de "
            "moeda.”</i> → ERRADO (inversão: nesse caso ele é nulo)",
        ])],
        "reescrita": ("Considere o modelo IS-LM. Quando o público está disposto a reter qualquer quantidade de "
                      "moeda que o Banco Central coloque em circulação à taxa de juros vigente, denomina-se esse "
                      "caso como " + hl("armadilha da liquidez") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Reter qualquer moeda injetada é a armadilha da liquidez (LM horizontal, monetária "
                            "ineficaz, fiscal eficaz); crowding-out é a expulsão do gasto privado pela alta de "
                            "juros, completo no modelo clássico.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00915
    {
        "id": "ECO-E2-L00915-1", "fonte_ref": "E2-L00915", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_KEY,
        "rotulo_item": "Item",
        "assertiva": ("A política monetária, no caso da chamada armadilha da liquidez, não tem nenhuma eficácia, "
                      "sendo a curva LM totalmente horizontal e sem nenhum efeito sobre a renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A política monetária, no caso da chamada armadilha da liquidez, não tem <u>nenhuma</u> "
                      "eficácia, sendo a curva LM <u>totalmente horizontal</u> e sem <u>nenhum</u> efeito sobre a "
                      "renda."),
        "poucas": ("No caso-limite da " + azb("armadilha da liquidez") + ", a LM é horizontal e a expansão "
                   "monetária não reduz o juro: o efeito sobre a renda é " + vd("nulo") + ". Os absolutos "
                   "estão corretos."),
        "destrinchando": [
            "Com a demanda por moeda infinitamente elástica ao juro, toda moeda nova é retida. O juro não cai, o "
            "investimento não reage e a renda não se move: eficácia nula da política monetária.",
            "A política fiscal, em compensação, tem " + vd("eficácia máxima") + ": a IS se desloca ao longo do "
            "trecho plano da LM sem pressionar o juro, e o multiplicador keynesiano opera por inteiro.",
            "Na prática, bancos centrais presos ao limite inferior dos juros recorreram a instrumentos não "
            "convencionais — " + azb("afrouxamento quantitativo") + ", " + azb("forward guidance") + " — que "
            "atuam sobre juros longos e expectativas, fora do canal do IS-LM básico.",
            "Quadro dos extremos: LM horizontal → monetária nula, fiscal máxima; LM vertical → fiscal nula, "
            "monetária máxima.",
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Três absolutos (“nenhuma”, “totalmente”, "
                       "“nenhum”) convidam a marcar ERRADO, mas descrevem com precisão o caso-limite do modelo. "
                       "Em itens sobre casos extremos do IS-LM, o modulador absoluto costuma ser exatamente o "
                       "que o modelo diz."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política fiscal, no caso da armadilha da liquidez, não tem nenhuma eficácia.”</i> → ERRADO "
            "(inversão: a fiscal tem eficácia máxima)",
            "<i>“No caso clássico, a política monetária não tem nenhum efeito sobre a renda.”</i> → ERRADO "
            "(inversão: no clássico ela tem eficácia máxima)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["nenhuma", "totalmente", "nenhum"],
        "dificuldade": 1,
        "comentario_fonte": "Verso remetia ao comentário do item vizinho da mesma questão: na armadilha da liquidez "
                            "a LM é horizontal, o Banco Central não consegue baixar o juro e a política monetária "
                            "é ineficaz; a fiscal é eficaz.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00683-1, ECO-E2-L00295-1"],
    },
    # ------------------------------------------------------------------ E2-L00939
    {
        "id": "ECO-E2-L00939-1", "fonte_ref": "E2-L00939", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("No modelo IS-LM, se, visando combater o déficit orçamentário, o governo decidir-se por uma "
                      "política fiscal de aumento dos impostos sem alteração dos gastos públicos, o efeito dessa "
                      "política será um deslocamento da curva IS para a esquerda, com a economia se movendo sobre a "
                      "curva LM, reduzindo a demanda de moeda e a taxa de juros. Nessa situação, a diminuição da "
                      "taxa de juros compensará integralmente o efeito do aumento dos impostos sobre a demanda por "
                      "bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo IS-LM, se, visando combater o déficit orçamentário, o governo decidir-se por "
                       "uma política fiscal de aumento dos impostos sem alteração dos gastos públicos, o efeito "
                       "dessa política será um deslocamento da curva IS para a esquerda, com a economia se movendo "
                       "sobre a curva LM, reduzindo a demanda de moeda e a taxa de juros. Nessa situação, a "
                       "diminuição da taxa de juros ") + vm("compensará integralmente")
                    + az(" o efeito do aumento dos impostos sobre a demanda por bens.")),
        "poucas": ("A descrição do mecanismo está certa, mas a queda de juros só " + azb("atenua") + " a "
                   "contração: com LM positivamente inclinada, a renda " + vd("cai") + ". Compensação integral "
                   "só existiria com LM vertical."),
        "destrinchando": [
            "Aumento de impostos: a renda disponível cai, o consumo cai e a IS se desloca para a esquerda. A "
            "economia desliza para baixo ao longo da LM: renda menor reduz a demanda por moeda para transações e, "
            "com oferta fixa, o juro cai.",
            "O juro menor recupera parte do investimento (é o " + azb("crowding-out ao contrário", ) + ", às "
            "vezes chamado de " + azb("crowding-in") + "), mas não todo: se recuperasse tudo, a renda não "
            "cairia, e então a demanda por moeda e o juro também não cairiam. A queda de juros só existe porque "
            "a renda caiu.",
            "Resultado no caso intermediário: " + vd("Y ↓ e i ↓") + ". O tamanho da queda de Y depende das "
            "inclinações: LM mais plana → juro cai pouco → contração maior; LM mais inclinada → juro cai mais → "
            "contração menor.",
            "Compensação integral só no " + azb("caso clássico") + " (LM vertical): a renda fica fixa e o "
            "investimento ocupa exatamente o espaço deixado pelo consumo. Na " + azb("armadilha da liquidez")
            + ", não há compensação nenhuma.",
            vm("Regra-âncora: com LM inclinada, a variação de juros amortece a política fiscal, mas não a anula."),
        ],
        "grafico_verso": "ECO-E2-L00939-1-V1",
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " Item longo, com toda a primeira parte "
                       "correta, para que o candidato baixe a guarda; o erro está no “integralmente” da última "
                       "oração, que transforma o caso geral no caso clássico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…Nessa situação, a diminuição da taxa de juros atenuará parcialmente o efeito do aumento dos "
            "impostos sobre a demanda por bens.”</i> → CERTO",
            "<i>“…o efeito dessa política será um deslocamento da curva LM para a esquerda…”</i> → ERRADO "
            "(curva trocada: imposto desloca a IS)",
        ])],
        "reescrita": ("No modelo IS-LM, se, visando combater o déficit orçamentário, o governo decidir-se por uma "
                      "política fiscal de aumento dos impostos sem alteração dos gastos públicos, o efeito dessa "
                      "política será um deslocamento da curva IS para a esquerda, com a economia se movendo sobre a "
                      "curva LM, reduzindo a demanda de moeda e a taxa de juros. Nessa situação, a diminuição da "
                      "taxa de juros " + hl("atenuará, mas não compensará integralmente,") + " o efeito do aumento "
                      "dos impostos sobre a demanda por bens."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["integralmente"], "dificuldade": 2,
        "comentario_fonte": "Com LM positivamente inclinada, a política fiscal contracionista reduz juros e renda; "
                            "a queda dos juros não compensa integralmente o aumento dos impostos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00940
    {
        "id": "ECO-E2-L00940-1", "fonte_ref": "E2-L00940", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo IS-LM, caso o Banco Central adote uma política monetária "
                      "expansionista por meio de operação no mercado aberto de títulos públicos e a moeda nominal "
                      "aumente na mesma magnitude que a moeda real, a curva LM se deslocará para baixo, provocando "
                      "uma diminuição da taxa de juros; e a curva IS se deslocará para a direita, em razão da nova "
                      "taxa de juros de equilíbrio. Nesse cenário, o resultado dessa política monetária será o "
                      "aumento da renda e do investimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando o modelo IS-LM, caso o Banco Central adote uma política monetária "
                       "expansionista por meio de operação no mercado aberto de títulos públicos e a moeda nominal "
                       "aumente na mesma magnitude que a moeda real, a curva LM se deslocará para baixo, provocando "
                       "uma diminuição da taxa de juros; e ") + vm("a curva IS se deslocará para a direita")
                    + az(", em razão da nova taxa de juros de equilíbrio. Nesse cenário, o resultado dessa "
                         "política monetária será o aumento da renda e do investimento.")),
        "poucas": ("Só a " + azb("LM") + " se desloca. A nova taxa de juros produz " + azb("movimento ao longo "
                   "da IS") + ", não deslocamento dela; o resultado (Y ↑ e I ↑) está certo."),
        "destrinchando": [
            "Compra de títulos no mercado aberto → base monetária ↑ → M ↑. Como a moeda nominal e a real sobem "
            "na mesma magnitude, o nível de preços está dado (curto prazo keynesiano): M/P ↑ e a LM desce para "
            "a direita.",
            "Na IS, o juro é variável do eixo: a queda de i eleva o investimento, e a economia desliza para baixo "
            "e para a direita ao longo da mesma IS, até o novo equilíbrio com " + vd("i ↓, I ↑ e Y ↑") + ".",
            "A IS só se desloca com mudança em variável exógena da demanda por bens: gasto público, impostos, "
            "consumo ou investimento autônomos, exportações líquidas autônomas.",
            "Se a IS também se deslocasse por causa do novo juro, o efeito da política seria contado duas vezes "
            "— o que torna a descrição internamente incoerente com a própria construção do modelo.",
            vm("Regra-âncora: monetária desloca só a LM; fiscal desloca só a IS."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Item longo e quase todo correto; o erro "
                       "está numa oração enxertada no meio, com um nexo (“em razão da nova taxa de juros”) que "
                       "confunde movimento com deslocamento. 🔥 Recorrente nas questões de IS-LM."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a curva LM se deslocará para baixo, provocando uma diminuição da taxa de juros e um movimento "
            "ao longo da curva IS…”</i> → CERTO",
            "<i>“…caso a moeda nominal aumente na mesma proporção que o nível de preços, a curva LM se deslocará "
            "para baixo…”</i> → ERRADO (dado alterado: M/P fica constante e a LM não se move)",
        ])],
        "reescrita": ("Considerando o modelo IS-LM, caso o Banco Central adote uma política monetária expansionista "
                      "por meio de operação no mercado aberto de títulos públicos e a moeda nominal aumente na "
                      "mesma magnitude que a moeda real, a curva LM se deslocará para baixo, provocando uma "
                      "diminuição da taxa de juros; e " + hl("a curva IS não se deslocará para a direita — a "
                                                             "economia apenas se moverá ao longo dela")
                      + ", em razão da nova taxa de juros de equilíbrio. Nesse cenário, o resultado dessa política "
                      "monetária será o aumento da renda e do investimento."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "A IS não se desloca em função da nova taxa de juros; só se desloca com mudança em "
                            "variáveis exógenas da demanda agregada. A política monetária desloca apenas a LM.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00140-1"],
    },
    # ------------------------------------------------------------------ E2-L01027
    {
        "id": "ECO-E2-L01027-1", "fonte_ref": "E2-L01027", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_4,
        "rotulo_item": "Item",
        "assertiva": ("A situação de armadilha da liquidez descreve o cenário no qual a política monetária perde a "
                      "sua capacidade de influenciar a economia por meio do canal tradicional da taxa de juros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A situação de armadilha da liquidez descreve o cenário no qual a política monetária perde "
                      "a sua capacidade de influenciar a economia <u>por meio do canal tradicional da taxa de "
                      "juros</u>."),
        "poucas": ("Na " + azb("armadilha da liquidez") + ", mais moeda não reduz o juro: trava o canal "
                   "tradicional " + vd("M ↑ → i ↓ → I ↑ → Y ↑") + ". O item é prudente ao restringir a perda a "
                   "esse canal."),
        "destrinchando": [
            "Com juros nominais próximos de zero (o " + azb("limite inferior efetivo") + "), os agentes preferem "
            "reter moeda a comprar títulos de retorno ínfimo e com risco de perda. A LM fica horizontal e a "
            "expansão monetária convencional não move o juro.",
            "O “canal tradicional” é o da taxa básica de curto prazo. Quando ele trava, os bancos centrais "
            "recorrem a canais alternativos: " + azb("afrouxamento quantitativo") + " (compra de ativos longos "
            "para reduzir juros longos e prêmios de risco), " + azb("credit easing") + " (compra de ativos de "
            "crédito privado) e " + azb("forward guidance") + " (compromisso com juros baixos por tempo "
            "prolongado, agindo sobre expectativas).",
            "Casos de referência: Japão a partir dos anos 1990; Estados Unidos, área do euro e Reino Unido após "
            "2008, com juros no piso. O diagnóstico de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) voltou "
            "ao centro do debate, e a política fiscal ganhou protagonismo.",
            "No IS-LM, a contrapartida é a eficácia máxima da política fiscal: sem alta de juros, não há "
            "crowding-out.",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " A ressalva “por meio do canal tradicional da "
                       "taxa de juros” protege o item: não diz que a política monetária fica inútil em qualquer "
                       "forma, só que perde o canal do juro. Versão mais arriscada seria “perde toda capacidade "
                       "de influenciar a economia”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na armadilha da liquidez, a política monetária perde sua capacidade de influenciar a economia, "
            "e a política fiscal também se torna ineficaz.”</i> → ERRADO (inversão: a fiscal tem eficácia "
            "máxima)",
            "<i>“Diante do limite inferior dos juros, bancos centrais recorreram a compras de ativos de longo "
            "prazo para afetar juros longos.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["canal tradicional"], "dificuldade": 1,
        "comentario_fonte": "Com juros nominais próximos de zero, a expansão monetária não reduz mais os juros; LM "
                            "horizontal; bancos centrais recorreram a QE, credit easing e forward guidance.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00295-1, ECO-E1-0872-1"],
    },
    # ------------------------------------------------------------------ E2-L01352
    {
        "id": "ECO-E2-L01352-1", "fonte_ref": "E2-L01352", "destino": "27", "subtema": H2["is"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_GRAF,
        "frente_figuras": ["ECO-E2-L01352-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Um aumento dos gastos autônomos deslocaria a curva de equilíbrio de bens e serviços para "
                      "cima, o que, consequentemente, aumentaria a taxa de juros e a renda de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento dos gastos autônomos deslocaria a <u>curva de equilíbrio de bens e serviços</u> "
                      "para cima, o que, consequentemente, aumentaria a taxa de juros e a renda de equilíbrio."),
        "poucas": ("A “curva de equilíbrio de bens e serviços” é a " + azb("IS") + ". Gasto autônomo maior a "
                   "desloca para cima/direita; com a LM positivamente inclinada, " + vd("Y e i sobem") + "."),
        "destrinchando": [
            "A IS é o lugar dos pares (Y, i) com o mercado de bens em equilíbrio: Y = C(Y − T) + I(i) + G + NX. "
            "Gastos autônomos são os componentes que não dependem da renda nem do juro: gasto público, consumo "
            "e investimento autônomos, exportações.",
            "Mais gasto autônomo eleva a demanda a cada juro: a IS se desloca horizontalmente em " + vd("ΔA / "
            "(1 − c)") + " (multiplicador simples × choque). “Para cima” e “para a direita” descrevem o mesmo "
            "deslocamento de uma curva decrescente.",
            "Novo equilíbrio: a renda maior eleva a demanda por moeda; com oferta de moeda fixa, o juro sobe e "
            "corta parte do investimento (" + azb("crowding-out parcial") + "). Por isso Y sobe menos que o "
            "deslocamento horizontal da IS.",
            "O efeito depende da LM: horizontal → Y sobe o deslocamento inteiro, i constante; vertical → só i "
            "sobe, Y constante.",
        ],
        "grafico_verso": "ECO-E2-L01352-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " O item evita a sigla e descreve a IS pelo que ela representa "
                       "(“curva de equilíbrio de bens e serviços”), apostando que o candidato a confunda com a "
                       "LM. Identificada a curva, o resultado é o padrão da expansão fiscal com LM inclinada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento dos gastos autônomos deslocaria a curva de equilíbrio do mercado monetário para "
            "baixo…”</i> → ERRADO (curva trocada: gasto autônomo desloca a IS)",
            "<i>“…o que aumentaria a renda de equilíbrio sem alterar a taxa de juros, qualquer que fosse a "
            "inclinação da LM.”</i> → ERRADO (modulador absoluto: só com LM horizontal)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Aumento de gastos autônomos desloca a IS para cima, elevando renda e juros.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 233 (não transcrita nesta linha; mesma figura da questão)",
                           "tipo_fonte": "GRÁFICO", "lado": "frente", "acao": "redesenhada"}],
        "alertas": [ALERTA_233],
    },
    # ------------------------------------------------------------------ E2-L01353
    {
        "id": "ECO-E2-L01353-1", "fonte_ref": "E2-L01353", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_GRAF,
        "frente_figuras": ["ECO-E2-L01352-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Uma compra de títulos, por parte da autoridade monetária, deslocaria a curva LM para cima "
                      "(esquerda), o que provocaria um aumento da taxa de juros de equilíbrio e uma redução da "
                      "renda da economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma compra de títulos, por parte da autoridade monetária, deslocaria a curva LM para ")
                    + vm("cima (esquerda)") + az(", o que provocaria ") + vm("um aumento") + az(" da taxa de "
                                                                                                 "juros de "
                                                                                                 "equilíbrio e ")
                    + vm("uma redução") + az(" da renda da economia.")),
        "poucas": ("Comprar títulos é " + azb("injetar moeda") + " (open market expansionista): a LM vai para "
                   "baixo/direita, os juros " + vd("caem") + " e a renda " + vd("sobe") + "."),
        "destrinchando": [
            "No " + azb("open market") + ", o Banco Central paga os títulos que compra com moeda nova: a base "
            "monetária e a oferta de moeda aumentam. A venda de títulos faz o contrário: retira moeda de "
            "circulação.",
            "Com mais moeda e a mesma demanda por moeda, o mercado monetário só se equilibra com juros menores a "
            "cada nível de renda: a LM se desloca para " + vd("baixo/direita") + ".",
            "Novo equilíbrio: " + vd("i ↓") + " estimula o investimento → " + vd("Y ↑") + ". A intensidade "
            "depende das inclinações: LM inclinada e IS plana → política monetária muito eficaz; LM horizontal "
            "(armadilha da liquidez) ou IS vertical → ineficaz.",
            "Pelo lado do mercado de títulos: o Banco Central comprando eleva o preço dos títulos, e preço maior "
            "de título é juro menor — a mesma conclusão, por outro caminho.",
            vm("Regra-âncora: compra de títulos = expansão monetária = LM para baixo/direita."),
        ],
        "dissecando": (cz("[inversão]") + " Descreve com coerência interna o efeito de uma <b>venda</b> de títulos "
                       "e o atribui à compra. Como tudo “fecha” (LM à esquerda → i↑, Y↓), a armadilha é não "
                       "checar o ponto de partida: quem compra título paga em moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma venda de títulos pela autoridade monetária deslocaria a LM para a esquerda, elevando os "
            "juros e reduzindo a renda.”</i> → CERTO",
            "<i>“Uma compra de títulos deslocaria a curva IS para a direita.”</i> → ERRADO (curva trocada: é a "
            "LM)",
        ])],
        "reescrita": ("Uma compra de títulos, por parte da autoridade monetária, deslocaria a curva LM para "
                      + hl("baixo (direita)") + ", o que provocaria " + hl("uma redução") + " da taxa de juros de "
                      "equilíbrio e " + hl("um aumento") + " da renda da economia."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Compra de títulos aumenta a liquidez: política monetária expansionista; LM para "
                            "baixo (direita), juros caem e a renda sobe, ceteris paribus.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_233,
        "alertas": [ALERTA_233,
                    "quase_duplicata: ECO-E2-L01485-1, ECO-E1-0704-1",
                    "nota_redacao: mesmo item usado no card de teste ECO-T06-1 (teste de gráficos), fora das "
                    "notas definitivas"],
    },
    # ------------------------------------------------------------------ E2-L01354
    {
        "id": "ECO-E2-L01354-1", "fonte_ref": "E2-L01354", "destino": "27", "subtema": H2["pol"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_GRAF,
        "frente_figuras": ["ECO-E2-L01352-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Uma diminuição da carga tributária deslocaria a curva IS para cima (direita) e provocaria um "
                      "aumento da taxa de juros de equilíbrio e da renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma diminuição da carga tributária deslocaria a curva IS para <u>cima (direita)</u> e "
                      "provocaria um aumento da taxa de juros de equilíbrio e da renda."),
        "poucas": ("Menos imposto → mais renda disponível → mais consumo: a " + azb("IS") + " vai para cima/"
                   "direita, e com a LM inclinada " + vd("Y e i sobem") + "."),
        "destrinchando": [
            "Corte de impostos é política fiscal expansionista: eleva a renda disponível (Y − T) e o consumo a "
            "cada nível de juros, deslocando a IS.",
            "Multiplicador dos impostos: " + vd("ΔY = −c·ΔT / (1 − c)") + ", menor em módulo que o dos gastos "
            "(" + vd("1 / (1 − c)") + "), porque parte do imposto devolvido é poupada. Daí o "
            + azb("multiplicador do orçamento equilibrado") + " igual a 1 (no modelo simples, com imposto "
            "autônomo).",
            "Com a LM positivamente inclinada, a renda maior eleva a demanda por moeda e o juro; o juro maior "
            "corta parte do investimento (crowding-out parcial).",
            "Efeito sobre as contas públicas: o corte de impostos piora o resultado primário no curto prazo, "
            "salvo se a renda crescer o bastante para recompor a arrecadação — hipótese otimista que a "
            "literatura raramente confirma.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de mecânica básica, com a curva certa, o sentido certo e os "
                       "efeitos certos. A versão ERRADA mais comum troca a curva (“LM”) ou o sinal dos juros "
                       "(“redução da taxa de juros”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma diminuição da carga tributária deslocaria a curva IS para a direita e provocaria redução da "
            "taxa de juros e aumento da renda.”</i> → ERRADO (sinal trocado: os juros sobem)",
            "<i>“Um aumento dos gastos públicos financiado por aumento igual de impostos autônomos eleva a "
            "renda.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Redução da carga tributária desloca a IS para a direita e para cima; aumentam renda e "
                            "juros.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_233,
        "alertas": [ALERTA_233],
    },
    # ------------------------------------------------------------------ E2-L01355
    {
        "id": "ECO-E2-L01355-1", "fonte_ref": "E2-L01355", "destino": "27", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_GRAF,
        "frente_figuras": ["ECO-E2-L01352-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("No curto prazo, em uma situação de armadilha da liquidez, a política fiscal é ineficaz para "
                      "alterar o nível de renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No curto prazo, em uma situação de armadilha da liquidez, a política ") + vm("fiscal")
                    + az(" é ineficaz para alterar o nível de renda.")),
        "poucas": ("Na " + azb("armadilha da liquidez") + " a LM é horizontal: a política <b>monetária</b> é "
                   "ineficaz e a <b>fiscal</b> tem " + vd("eficácia máxima") + " (sem crowding-out)."),
        "destrinchando": [
            "Com juros muito baixos, todos esperam que eles subam (e que os títulos percam valor): a demanda por "
            "moeda torna-se " + azb("infinitamente elástica aos juros") + ". Toda moeda adicional é "
            "entesourada, e a LM fica horizontal.",
            "Política monetária: mais moeda não reduz juros que já não caem → Y não muda. Política fiscal: a IS "
            "se desloca ao longo do trecho plano, os juros não sobem, não há " + azb("crowding-out") + " e o "
            + azb("multiplicador keynesiano") + " opera por inteiro.",
            "Origem: " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) descreveu a possibilidade; a formalização "
            "veio com o IS-LM de " + oc("Hicks") + " (1937). O tema voltou com o Japão dos anos 1990 e o "
            "pós-2008 (juros no piso).",
            "Espelho: no " + azb("caso clássico") + " (LM vertical), a fiscal é totalmente ineficaz "
            "(crowding-out completo) e a monetária, máxima.",
            vm("Regra-âncora: LM horizontal → fiscal manda; LM vertical → monetária manda."),
        ],
        "grafico_verso": "ECO-E2-L01355-1-V1",
        "dissecando": (cz("[troca de conceito · inversão]") + " Troca a política: a ineficácia na armadilha é da "
                       "<b>monetária</b>. 🔥 Itens sobre casos extremos do IS-LM quase sempre testam a tabela de "
                       "quatro casas (LM horizontal/vertical × fiscal/monetária)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na armadilha da liquidez, a política monetária é ineficaz para alterar a renda.”</i> → CERTO",
            "<i>“No caso clássico, a política fiscal expansionista eleva a renda sem efeito deslocamento.”</i> → "
            "ERRADO (inversão: no clássico o crowding-out é total)",
        ])],
        "reescrita": ("No curto prazo, em uma situação de armadilha da liquidez, a política " + hl("monetária")
                      + " é ineficaz para alterar o nível de renda."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "LM horizontal: monetária ineficaz, fiscal com eficácia máxima; sem alta de juros nem "
                            "crowding-out; multiplicador pleno.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_233,
        "alertas": [ALERTA_233,
                    "quase_duplicata: ECO-E2-L01443-1",
                    "nota_redacao: mesmo item usado no card de teste ECO-T07-1 (teste de gráficos), fora das "
                    "notas definitivas"],
    },
]
