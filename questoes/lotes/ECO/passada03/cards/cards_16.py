"""Cards do lote de redação 16 — ECO, passada 03 (notas 73: teorias clássicas e neoclássicas do comércio;
74: crítica da CEPAL)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "va": "⛵ Vantagens absolutas e comparativas",
    "ho": "🧪 Heckscher-Ohlin e teoremas",
    "leo": "❓ Paradoxo de Leontief e termos de troca",
    "cepal": "🌎 CEPAL e termos de troca",
}

RT = "Prof. Rodrigo Teixeira"
RT_PROVA = "Intensivo Pré-TPS/2023"
NIDI = "Nidi/Jacqueline Bueno"

CMD_RT_NEO = "Sobre a teoria neoclássica do comércio internacional, julgue a afirmação a seguir."
CMD_RT_CONC = "Sobre os conceitos e teorias do comércio internacional, julgue a afirmação a seguir."
CMD_RT_TEO = "A respeito das teorias do comércio internacional, julgue o item a seguir."
CMD_RT_JUL = "Julgue a afirmação abaixo acerca das teorias do comércio internacional."
CMD_NIDI_RIC = ("O modelo de vantagens comparativas de David Ricardo é um dos principais modelos de teoria econômica e "
                "é amplamente utilizado para explicar relações de trocas em diferentes contextos. No que se refere a "
                "esse modelo, julgue (C ou E) o item a seguir.")
CMD_NIDI_GLOB = ("A globalização do espaço econômico torna o estudo da economia internacional cada vez mais relevante "
                 "para o entendimento das relações de comércio entre as nações. A esse respeito, julgue como certo ou "
                 "errado o item a seguir.")
CMD_NIDI_TCI = "Julgue o item a seguir, relativo à teoria do comércio internacional."
CMD_JB_OUT = ("A partir da interpretação das teorias clássicas de comércio, a abertura ao comércio internacional leva "
              "a um aumento do bem-estar social [...]. Considerando as diferentes estruturas de mercado e as "
              "interpretações das teorias de comércio mais modernas, avalie como certo ou errado (C ou E) o item a "
              "seguir.")
CMD_CEPAL = "A respeito da crítica da CEPAL e das ideias de Raúl Prebisch, julgue o item que se segue."

CARDS = [
    # ------------------------------------------------------------------ E2-L01542
    {
        "id": "ECO-E2-L01542-1", "fonte_ref": "E2-L01542", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_RT_NEO,
        "rotulo_item": "Item",
        "assertiva": ("Supondo que a produção de tecidos usa dois fatores, capital e trabalho, sendo intensiva neste "
                      "último, o aumento no preço dos tecidos, tudo o mais constante, tende a elevar a remuneração do "
                      "capital e reduzir a remuneração do trabalho, de acordo com o teorema de Stolper-Samuelson."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Supondo que a produção de tecidos usa dois fatores, capital e trabalho, sendo intensiva neste "
                       "último, o aumento no preço dos tecidos, tudo o mais constante, tende a elevar a remuneração "
                       "do ") + vm("capital") + az(" e reduzir a remuneração do ") + vm("trabalho")
                    + az(", de acordo com o teorema de Stolper-Samuelson.")),
        "poucas": ("Pelo " + azb("teorema de Stolper-Samuelson") + ", a alta do preço de um bem eleva a remuneração "
                   "real do fator usado <b>intensivamente</b> nele (aqui, o trabalho) e reduz a do outro (o capital). "
                   "O item inverteu os dois fatores."),
        "destrinchando": [
            "Enunciado do teorema (" + oc("Stolper e Samuelson") + ", " + vd("1941") + "), no modelo "
            + azb("Heckscher-Ohlin") + " 2 × 2 × 2: um aumento no preço relativo de um bem " + vd("aumenta") + " o "
            "retorno real do fator usado intensivamente na sua produção e " + vd("reduz") + " o retorno real do "
            "outro fator.",
            "Mecanismo: tecido mais caro → o setor têxtil se expande e o outro setor encolhe. Como o têxtil usa "
            "muito trabalho e pouco capital, a economia passa a demandar mais trabalho do que o setor em contração "
            "libera; com dotações fixas e pleno emprego, o salário (w) sobe e o aluguel do capital (r) cai. Com o "
            "trabalho mais caro, as firmas dos dois setores passam a usar mais capital por trabalhador, o que eleva "
            "a produtividade marginal do trabalho em ambos.",
            "Há " + azb("efeito de magnificação") + ": w sobe proporcionalmente <b>mais</b> que o preço do tecido, "
            "e r cai em termos absolutos. Por isso o ganho do trabalhador é <b>real</b> (compra mais dos dois "
            "bens), não só nominal.",
            "Uso típico do teorema: explicar os " + azb("efeitos distributivos do comércio") + " e da proteção — a "
            "abertura beneficia o fator abundante (cujo bem é exportado e encarece) e prejudica o escasso; uma "
            "tarifa faz o inverso.",
            vm("Regra-âncora: preço do bem ↑ → fator intensivo nesse bem ganha; o outro perde."),
        ],
        "dissecando": (cz("[inversão]") + " Premissas e nome do teorema corretos; a conclusão troca o ganhador "
                       "pelo perdedor. Pista: “intensiva neste último” amarra o tecido ao trabalho — é o trabalho "
                       "que tem de ganhar. 🔥 Stolper-Samuelson é cobrado quase sempre por inversão de sentido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento no preço dos tecidos tende a elevar a remuneração do trabalho em proporção maior que a "
            "alta do preço…”</i> → CERTO (magnificação)",
            "<i>“…tende a elevar a remuneração de ambos os fatores, já que a economia como um todo ganha…”</i> → "
            "ERRADO (o outro fator perde em termos reais)",
        ])],
        "reescrita": ("Supondo que a produção de tecidos usa dois fatores, capital e trabalho, sendo intensiva neste "
                      "último, o aumento no preço dos tecidos, tudo o mais constante, tende a elevar a remuneração "
                      "do " + hl("trabalho") + " e reduzir a remuneração do " + hl("capital") + ", de acordo com o "
                      "teorema de Stolper-Samuelson."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a", "tudo o mais constante"], "dificuldade": 1,
        "comentario_fonte": ("Stolper-Samuelson: alta do preço relativo de um bem eleva a remuneração real do fator "
                             "usado intensivamente nele e reduz a do outro; tecido intensivo em trabalho → salário "
                             "sobe, remuneração do capital cai. A assertiva inverte os efeitos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 415", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (enunciado do teorema no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01621-1, ECO-E3-L00222-1 (Stolper-Samuelson com sentido invertido)"],
    },
    # ------------------------------------------------------------------ E2-L01543
    {
        "id": "ECO-E2-L01543-1", "fonte_ref": "E2-L01543", "destino": "73", "subtema": H2["leo"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_NEO,
        "rotulo_item": "Item",
        "assertiva": ("O paradoxo de Leontief levou a uma reformulação do modelo básico de dois fatores para versões "
                      "que incorporavam a diferenciação do fator trabalho em níveis de qualificação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O paradoxo de Leontief levou a uma <u>reformulação</u> do modelo básico de dois fatores para "
                      "versões que incorporavam a <u>diferenciação do fator trabalho em níveis de qualificação</u>."),
        "poucas": ("O paradoxo não derrubou o " + azb("Heckscher-Ohlin") + ": estimulou versões com mais fatores, "
                   "sobretudo o trabalho dividido por qualificação (" + azb("capital humano") + "), em que os EUA "
                   "aparecem abundantes em trabalho qualificado."),
        "destrinchando": [
            "O teste: " + oc("Wassily Leontief") + " (" + vd("1953") + ", dados de 1947) usou a matriz "
            "insumo-produto dos EUA — o país mais abundante em capital — e calculou o capital e o trabalho contidos "
            "em US$ 1 milhão de exportações e de substitutos de importações. Resultado: as exportações eram "
            "<b>menos</b> intensivas em capital que as importações, o contrário do previsto pelo H-O.",
            "O padrão persistiu em estudos posteriores. Com dados de 1962 (" + oc("Baldwin") + ", 1971, citado por "
            + oc("Krugman e Obstfeld") + "), a relação capital/trabalho era de " + vd("US$ 17.916") + " por "
            "trabalhador nas importações e de " + vd("US$ 14.321") + " nas exportações; mas as exportações tinham "
            "mais anos de estudo por trabalhador (" + vd("10,1 × 9,9") + ") e mais engenheiros e cientistas na "
            "força de trabalho (" + vd("0,0255 × 0,0189") + ").",
            "Daí a reformulação: o fator trabalho não é homogêneo. Separando " + azb("trabalho qualificado")
            + " e não qualificado (ou somando o capital humano ao capital físico), os EUA exportam bens intensivos "
            "no fator em que são de fato abundantes — trabalho qualificado e tecnologia.",
            "Outras explicações do paradoxo: recursos naturais complementares ao capital (importações de "
            "minérios e petróleo são intensivas em capital), proteção americana às indústrias trabalho-intensivas, "
            "reversão de intensidade fatorial e preferências enviesadas para bens intensivos em capital.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item descreve com precisão a consequência teórica do "
                       "paradoxo: reformulação, não abandono. Quem guarda só a palavra “paradoxo” tende a imaginar "
                       "que a teoria caiu e marca ERRADO. 🔥 A banca alterna “refinamento” (CERTO) e “abandono” "
                       "(ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O paradoxo de Leontief levou ao abandono da teoria baseada na dotação de fatores.”</i> → ERRADO "
            "(houve refinamento, não abandono)",
            "<i>“Leontief constatou que as exportações dos EUA eram mais intensivas em capital que as "
            "importações.”</i> → ERRADO (inversão: eram menos)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Leontief (1953): EUA, abundantes em capital, exportavam bens intensivos em trabalho; o "
                             "paradoxo levou a modelos com trabalho qualificado × não qualificado (capital humano)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 416", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (dados de Baldwin no 📖)"},
                          {"ref": "IMAGEM 417", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (explicações do paradoxo no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01577-1, ECO-E2-L01623-1 (consequências do paradoxo de Leontief)"],
    },
    # ------------------------------------------------------------------ E2-L01544
    {
        "id": "ECO-E2-L01544-1", "fonte_ref": "E2-L01544", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_RT_NEO,
        "rotulo_item": "Item",
        "assertiva": ("O teorema da equalização dos preços dos fatores mostra que os proprietários de fatores de "
                      "produção menos abundantes de um país terão ganhos com a abertura comercial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O teorema da equalização dos preços dos fatores mostra que os proprietários de fatores de "
                       "produção ") + vm("menos") + az(" abundantes de um país terão ganhos com a abertura "
                                                         "comercial.")),
        "poucas": ("Com a abertura, cada país exporta o bem intensivo no seu fator " + azb("abundante") + ": a "
                   "demanda por esse fator sobe e a do fator escasso cai. Ganham os donos do fator abundante; "
                   "perdem os do " + vm("escasso") + "."),
        "destrinchando": [
            "Na autarquia, o fator abundante é barato e o escasso é caro. Num país abundante em trabalho, w/r é "
            "baixo; num país abundante em capital, w/r é alto. É essa diferença de preços dos fatores que gera os "
            "custos relativos diferentes dos bens e, portanto, o comércio (" + azb("teorema de Heckscher-Ohlin")
            + ").",
            "Aberto o comércio, o país abundante em trabalho expande o bem trabalho-intensivo e contrai o "
            "capital-intensivo: w sobe e r cai. No parceiro ocorre o inverso. Os preços relativos dos fatores "
            "<b>convergem</b> — no limite, sob hipóteses fortes, igualam-se: é o " + azb("teorema da equalização "
            "dos preços dos fatores") + " (" + oc("Samuelson") + ", 1948–1949), em que o comércio de bens funciona "
            "como substituto da mobilidade internacional dos fatores.",
            "A face distributiva dessa convergência é o " + azb("teorema de Stolper-Samuelson") + ": o fator "
            "abundante ganha em termos reais e o fator escasso perde. O país como um todo ganha (os ganhadores "
            "poderiam compensar os perdedores), mas a abertura cria conflito interno — base da economia política "
            "do protecionismo.",
            "Exemplo de manual: num país abundante em terra, como o " + rx("Brasil") + ", a abertura tende a "
            "favorecer os donos de terra (agronegócio exportador) e a pressionar a remuneração dos fatores "
            "escassos usados nos setores que competem com importações.",
            vm("Regra-âncora: abertura comercial → fator abundante ganha; fator escasso perde."),
        ],
        "dissecando": (cz("[inversão]") + " O item troca “mais” por “menos” abundantes. A banca costuma pendurar a "
                       "inversão num teorema vizinho (equalização em vez de Stolper-Samuelson) para distrair; o "
                       "decisivo é o sentido: o fator escasso perde."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os proprietários de fatores de produção menos abundantes de um país terão perdas com a abertura "
            "comercial.”</i> → CERTO",
            "<i>“…a abertura comercial beneficia todos os proprietários de fatores, pois o país como um todo "
            "ganha.”</i> → ERRADO (modulador absoluto: o fator escasso perde)",
        ])],
        "reescrita": ("O teorema da equalização dos preços dos fatores mostra que os proprietários de fatores de "
                      "produção " + hl("mais") + " abundantes de um país terão ganhos com a abertura comercial."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Abertura eleva a demanda pelos fatores abundantes e reduz a dos escassos: donos dos "
                             "abundantes ganham, donos dos escassos perdem. A assertiva inverte a conclusão."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 418", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (mecanismo de convergência de w/r no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00431-1 (fator abundante ganha, escasso perde)"],
    },
    # ------------------------------------------------------------------ E2-L01545
    {
        "id": "ECO-E2-L01545-1", "fonte_ref": "E2-L01545", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_NEO,
        "rotulo_item": "Item",
        "assertiva": ("Uma economia aberta que produz 2 bens e encontra grandes reservas de um recurso natural, tende "
                      "a aumentar mais que proporcionalmente a produção do bem que usa intensivamente este recurso e "
                      "reduzir, em termos absolutos, a produção do outro bem, de acordo com o teorema de "
                      "Rybczynski."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma economia aberta que produz 2 bens e encontra grandes reservas de um recurso natural, "
                      "tende a aumentar <u>mais que proporcionalmente</u> a produção do bem que usa intensivamente "
                      "este recurso e reduzir, <u>em termos absolutos</u>, a produção do outro bem, de acordo com o "
                      "teorema de Rybczynski."),
        "poucas": ("É o enunciado do " + azb("teorema de Rybczynski") + ": a preços dos bens constantes, o aumento "
                   "da dotação de um fator expande <b>mais que proporcionalmente</b> o bem intensivo nele e "
                   "<b>reduz em termos absolutos</b> a produção do outro."),
        "destrinchando": [
            oc("Tadeusz Rybczynski") + " (" + vd("1955") + "): num modelo 2 × 2 com pleno emprego, retornos "
            "constantes e preços dos bens dados, um aumento na oferta de um fator altera a <b>composição</b> da "
            "produção, não os preços dos fatores.",
            "Por que o outro setor encolhe? Se os preços dos bens não mudam, os preços dos fatores também não "
            "mudam (Stolper-Samuelson ao contrário), e cada setor mantém sua razão entre fatores. A única forma de "
            "empregar o recurso extra com essas proporções fixas é deslocar para o setor intensivo nele parte dos "
            "<b>outros</b> fatores, retirados do segundo setor — que, por isso, cai em termos absolutos.",
            "“Mais que proporcionalmente”: o setor beneficiado cresce com o recurso novo <b>e</b> com os fatores "
            "que recebe do outro setor, de modo que sua produção cresce percentualmente mais que a dotação do "
            "fator (" + azb("efeito de magnificação") + ").",
            "“Economia aberta” não é detalhe: num país pequeno que toma os preços do mercado mundial, a hipótese "
            "de preços constantes é natural. O teorema dá a base do " + azb("efeito-deslocamento de recursos")
            + " da doença holandesa: o setor do recurso cresce e a indústria encolhe.",
            vm("Regra-âncora: dotação de um fator ↑ (a preços dados) → bem intensivo nele ↑ mais que "
               "proporcionalmente; o outro bem ↓ em termos absolutos."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Reproduz o enunciado do manual. Assusta porque "
                       "parece paradoxal que uma economia com <b>mais</b> recursos produza <b>menos</b> de algum "
                       "bem, e porque “mais que proporcionalmente” e “em termos absolutos” soam como exageros "
                       "fabricados — aqui são exatamente o teorema."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tende a aumentar a produção de ambos os bens, ainda que em proporções diferentes…”</i> → ERRADO "
            "(o outro bem cai em termos absolutos)",
            "<i>“…eleva a remuneração do recurso natural, que se torna abundante…”</i> → ERRADO (a preços dos bens "
            "constantes, os preços dos fatores não mudam)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": ("Rybczynski: a preços constantes, aumento da dotação de um fator eleva mais que "
                             "proporcionalmente a produção do bem intensivo nele e reduz em termos absolutos a do "
                             "outro; ligação com a doença holandesa."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01578-1, ECO-E2-L01693-1 (Rybczynski e doença holandesa)"],
    },
    # ------------------------------------------------------------------ E2-L01577
    {
        "id": "ECO-E2-L01577-1", "fonte_ref": "E2-L01577", "destino": "73", "subtema": H2["leo"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("O paradoxo de Leontief levou a revisões da teoria neoclássica da dotação de fatores como "
                      "explicação para o padrão de comércio, como por exemplo a divisão do fator trabalho em "
                      "qualificado e não qualificado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O paradoxo de Leontief levou a <u>revisões</u> da teoria neoclássica da dotação de fatores "
                      "como explicação para o padrão de comércio, como por exemplo a divisão do fator trabalho em "
                      "qualificado e não qualificado."),
        "poucas": ("A evidência de " + oc("Leontief") + " contrariou o " + azb("Heckscher-Ohlin") + " e gerou "
                   + azb("revisões") + " — entre elas, tratar o trabalho como fator heterogêneo (qualificado × não "
                   "qualificado)."),
        "destrinchando": [
            "O paradoxo: nos anos 1950, " + oc("Wassily Leontief") + " mostrou, com a matriz insumo-produto, que "
            "os EUA — o país mais abundante em capital — exportavam bens relativamente intensivos em "
            "<b>trabalho</b> e importavam bens intensivos em capital. Pelo H-O, deveria ser o contrário.",
            "Revisões propostas: (1) " + azb("trabalho qualificado") + " como fator distinto — o trabalhador "
            "americano incorpora capital humano, e os EUA são abundantes nesse fator; (2) " + azb("recursos "
            "naturais") + " como terceiro fator, complementares ao capital; (3) proteção comercial americana às "
            "indústrias intensivas em trabalho; (4) tecnologia e inovação (ciclo do produto, de " + oc("Vernon")
            + "); (5) reversão de intensidade fatorial.",
            "O resultado não foi abandonar a teoria da dotação de fatores, mas ampliá-la: o modelo de "
            "Heckscher-Ohlin-Vanek (conteúdo fatorial do comércio, com muitos fatores) é o herdeiro dessas "
            "revisões e continua sendo testado empiricamente.",
            vm("Regra-âncora: Leontief → revisão e ampliação do H-O, não abandono."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item descritivo e correto. O “como por exemplo” é seguro: a "
                       "divisão do trabalho por qualificação é a revisão mais citada. A pegadinha da banca, nesse "
                       "tema, costuma estar em “abandono da teoria” ou na inversão do achado (exportações mais "
                       "intensivas em capital)."),
        "modulos": [("🃏 Carta na manga", [
            "O paradoxo de Leontief é o exemplo clássico de que um teste empírico negativo leva a refinar uma "
            "teoria, não a descartá-la: ele empurrou a teoria do comércio para o capital humano e a tecnologia."])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["como por exemplo"], "dificuldade": 1,
        "comentario_fonte": ("Leontief testou o H-O nos anos 1950 e encontrou EUA exportando bens "
                             "trabalho-intensivos; o paradoxo levou a refinamentos como trabalho qualificado × não "
                             "qualificado, recursos naturais, políticas comerciais e tecnologia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01543-1 (mesma ideia, outra lista do mesmo curso)"],
    },
    # ------------------------------------------------------------------ E2-L01578
    {
        "id": "ECO-E2-L01578-1", "fonte_ref": "E2-L01578", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("O teorema de Rybczynski não é compatível com o fenômeno conhecido como “doença holandesa” e a "
                      "desindustrialização que se segue num país que descobre grandes reservas de recursos "
                      "naturais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O teorema de Rybczynski ") + vm("não é") + az(" compatível com o fenômeno conhecido como "
                                                                      "“doença holandesa” e a desindustrialização "
                                                                      "que se segue num país que descobre grandes "
                                                                      "reservas de recursos naturais.")),
        "poucas": ("O " + azb("teorema de Rybczynski") + " é justamente uma das bases teóricas da "
                   + azb("doença holandesa") + ": mais recurso natural expande o setor que o usa intensivamente e "
                   "contrai, em termos absolutos, o outro setor (a indústria)."),
        "destrinchando": [
            "Rybczynski (1955): a preços dos bens constantes, o aumento da dotação de um fator eleva mais que "
            "proporcionalmente a produção do bem intensivo nesse fator e <b>reduz em termos absolutos</b> a "
            "produção do outro bem. Descobrir petróleo ou gás equivale a aumentar a dotação do fator “recurso "
            "natural”.",
            "Doença holandesa: o nome vem da " + azb("Holanda") + " após a descoberta das grandes jazidas de gás "
            "de Groningen (" + vd("1959") + "), seguida de perda de competitividade da indústria nos anos 1960–70. "
            "A formalização clássica (" + oc("Corden e Neary") + ", " + vd("1982") + ") separa dois canais:",
            "(1) " + azb("Efeito-deslocamento de recursos") + ": capital e trabalho migram para o setor do "
            "recurso em expansão — é o mecanismo de Rybczynski; (2) " + azb("efeito-gasto") + ": a renda extra "
            "eleva a demanda por não comercializáveis (serviços), cujo preço sobe, o que equivale a uma "
            + azb("apreciação do câmbio real") + " que tira competitividade da indústria.",
            "Logo, o teorema não explica a doença holandesa sozinho (falta o canal cambial), mas é plenamente "
            "<b>compatível</b> com ela e ajuda a explicá-la.",
            vm("Regra-âncora: Rybczynski + recurso natural = setor extrativo ↑ e indústria ↓ → compatível com a "
               "doença holandesa."),
        ],
        "dissecando": (cz("[contradição]") + " O item nega uma relação que os manuais afirmam. A versão CERTA, que "
                       "a banca também cobra, diz que o teorema “é compatível” com a doença holandesa. Pista: a "
                       "própria descrição do fenômeno no item (descoberta de recursos → desindustrialização) é a "
                       "previsão do teorema."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O teorema de Rybczynski é compatível com a doença holandesa, pois prevê a redução absoluta da "
            "produção do bem que não usa intensivamente o recurso descoberto.”</i> → CERTO",
            "<i>“Pelo teorema de Rybczynski, a descoberta de recursos naturais eleva a produção de todos os setores "
            "da economia.”</i> → ERRADO (o outro setor encolhe)",
        ])],
        "reescrita": ("O teorema de Rybczynski " + hl("é") + " compatível com o fenômeno conhecido como “doença "
                      "holandesa” e a desindustrialização que se segue num país que descobre grandes reservas de "
                      "recursos naturais."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Rybczynski é compatível com a doença holandesa: o aumento do fator recurso natural "
                             "expande o setor extrativo e contrai a indústria; a doença holandesa soma a isso a "
                             "apreciação cambial."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01693-1 (mesmo tema em versão CERTA), ECO-E2-L01545-1"],
    },
    # ------------------------------------------------------------------ E2-L01620
    {
        "id": "ECO-E2-L01620-1", "fonte_ref": "E2-L01620", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_TEO,
        "rotulo_item": "Item",
        "assertiva": ("A teoria clássica de Smith e Ricardo defendia a especialização com base nas diferenças da "
                      "produtividade do fator trabalho entre os países, o primeiro destacando as vantagens absolutas "
                      "e o segundo as vantagens relativas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria clássica de Smith e Ricardo defendia a especialização com base nas diferenças da "
                      "<u>produtividade do fator trabalho</u> entre os países, o primeiro destacando as vantagens "
                      "<u>absolutas</u> e o segundo as vantagens <u>relativas</u>."),
        "poucas": ("Na teoria clássica, o comércio nasce de diferenças de " + azb("produtividade do trabalho")
                   + ": " + oc("Smith") + " fala em vantagem " + azb("absoluta") + "; " + oc("Ricardo")
                   + ", em vantagem " + azb("comparativa (relativa)") + "."),
        "destrinchando": [
            oc("Adam Smith") + " (<i>A Riqueza das Nações</i>, " + vd("1776") + "): cada país deve se "
            "especializar no bem que produz com <b>menos trabalho</b> que o parceiro (vantagem absoluta) e "
            "importar o resto — extensão internacional da divisão do trabalho e argumento contra o mercantilismo.",
            "Limite de Smith: um país sem vantagem absoluta em nada ficaria fora do comércio. " + oc("David "
            "Ricardo") + " (<i>Princípios de Economia Política e Tributação</i>, " + vd("1817") + ") resolve: "
            "basta a vantagem " + azb("comparativa") + " — produzir o bem em que a desvantagem é menor (menor "
            "custo de oportunidade). No exemplo clássico, Portugal produz vinho e tecido com menos trabalho que a "
            "Inglaterra, e mesmo assim ambos ganham se Portugal se especializar em vinho e a Inglaterra em tecido.",
            "Base comum: a " + azb("teoria do valor-trabalho") + " — o trabalho é o único fator, e o custo de um "
            "bem é medido em horas. Por isso a diferença de produtividade do trabalho (tecnologia) explica o "
            "padrão de comércio.",
            "Contraste com a teoria " + azb("neoclássica") + " (Heckscher-Ohlin): tecnologia idêntica entre "
            "países e comércio explicado por diferenças de <b>dotação relativa de fatores</b>.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de definição: autor certo para cada vantagem e base certa "
                       "(produtividade do trabalho). “Relativas” é sinônimo aceito de “comparativas”. A banca "
                       "costuma errar o item trocando os autores ou atribuindo a Ricardo custos absolutos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o primeiro destacando as vantagens comparativas e o segundo as vantagens absolutas.”</i> → "
            "ERRADO (troca de ator)",
            "<i>“…com base nas diferenças de dotação relativa de capital e trabalho entre os países…”</i> → ERRADO "
            "(troca de conceito: isso é Heckscher-Ohlin)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Smith: vantagem absoluta (menos trabalho); Ricardo: vantagem comparativa (custo de "
                             "oportunidade); ambos baseados na produtividade do trabalho."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00465-1, ECO-E2-L01622-1 (clássicos × neoclássicos)"],
    },
    # ------------------------------------------------------------------ E2-L01621
    {
        "id": "ECO-E2-L01621-1", "fonte_ref": "E2-L01621", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_TEO,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o teorema de Stolper-Samuelson, o aumento no preço de um bem que usa intensivamente o "
                      "trabalho, deverá levar à redução relativa da remuneração deste fator de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo o teorema de Stolper-Samuelson, o aumento no preço de um bem que usa intensivamente "
                       "o trabalho, deverá levar à ") + vm("redução") + az(" relativa da remuneração deste fator de "
                                                                         "produção.")),
        "poucas": ("Stolper-Samuelson: o preço do bem trabalho-intensivo sobe → a remuneração do " + azb("trabalho")
                   + " <b>sobe</b> (mais que o preço) e a do capital cai."),
        "destrinchando": [
            "Enunciado (" + oc("Stolper e Samuelson") + ", " + vd("1941") + "): um aumento no preço relativo de "
            "um bem eleva o retorno real do fator usado intensivamente na sua produção e reduz o retorno real do "
            "outro fator.",
            "Cadeia: p do bem trabalho-intensivo ↑ → o setor se expande e demanda muito trabalho; o outro setor "
            "encolhe e libera mais capital do que trabalho → excesso de demanda por trabalho → " + vd("w ↑")
            + " e " + vd("r ↓") + ".",
            "Magnificação: em variações percentuais, ŵ > p̂ > 0 > r̂. O salário sobe mais que o preço do bem, "
            "por isso o trabalhador ganha em termos reais, medido em qualquer dos dois bens.",
            "O teorema é a ponte entre preços dos bens e distribuição de renda: explica por que a abertura "
            "favorece o fator abundante (seu bem é exportado e encarece) e por que donos do fator escasso pedem "
            "proteção (a tarifa encarece o bem intensivo nele).",
            vm("Regra-âncora: o fator intensivo acompanha o preço do seu bem — e com lupa (magnificação)."),
        ],
        "dissecando": (cz("[inversão]") + " Troca “aumento” por “redução” na conclusão. O “relativa” é ruído: "
                       "mesmo em termos relativos (w/r), a remuneração do trabalho sobe. A vírgula entre sujeito e "
                       "verbo (“…o trabalho, deverá…”) está na fonte e não afeta o julgamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…deverá levar à elevação da remuneração real do trabalho e à redução da remuneração real do "
            "capital.”</i> → CERTO",
            "<i>“…deverá elevar o salário nominal na mesma proporção do aumento do preço do bem.”</i> → ERRADO "
            "(magnificação: sobe mais que proporcionalmente)",
        ])],
        "reescrita": ("Segundo o teorema de Stolper-Samuelson, o aumento no preço de um bem que usa intensivamente o "
                      "trabalho, deverá levar à " + hl("elevação") + " relativa da remuneração deste fator de "
                      "produção."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["deverá"], "dificuldade": 1,
        "comentario_fonte": ("O teorema afirma o oposto: o aumento do preço de um bem eleva a remuneração do fator "
                             "usado intensivamente; se o bem usa trabalho, o salário aumenta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01542-1, ECO-E3-L00222-1 (Stolper-Samuelson invertido)"],
    },
    # ------------------------------------------------------------------ E2-L01622
    {
        "id": "ECO-E2-L01622-1", "fonte_ref": "E2-L01622", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_TEO,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Heckscher e Ohlin difere do modelo clássico de Ricardo, entre outras hipóteses, "
                      "por considerar outros fatores de produção e não apenas o trabalho, de maneira que o padrão de "
                      "comércio será definido pelas diferentes dotações relativas dos fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo de Heckscher e Ohlin difere do modelo clássico de Ricardo, <u>entre outras "
                      "hipóteses</u>, por considerar outros fatores de produção e não apenas o trabalho, de maneira "
                      "que o padrão de comércio será definido pelas diferentes <u>dotações relativas</u> dos fatores "
                      "de produção."),
        "poucas": ("Ricardo: um fator (trabalho) e tecnologias diferentes. " + azb("Heckscher-Ohlin") + ": dois ou "
                   "mais fatores, tecnologia igual, e o comércio explicado pelas " + azb("dotações relativas")
                   + " de fatores."),
        "destrinchando": [
            "Quadro comparativo — <b>Ricardo</b>: um fator (trabalho); tecnologias diferentes entre países; FPP "
            "linear (custo de oportunidade constante); especialização completa; sem efeitos distributivos internos "
            "(só há trabalhadores). <b>Heckscher-Ohlin</b>: dois fatores (capital e trabalho, ou terra); "
            "tecnologias <b>idênticas</b>; FPP côncava; especialização em geral incompleta; ganhadores e "
            "perdedores internos.",
            oc("Eli Heckscher") + " (" + vd("1919") + ") e " + oc("Bertil Ohlin") + " (" + vd("1933") + "): como "
            "a tecnologia é a mesma, o que diferencia os custos relativos é a abundância de fatores. País "
            "abundante em capital tem capital barato e exporta bens " + azb("capital-intensivos") + "; o abundante "
            "em trabalho exporta bens trabalho-intensivos (" + azb("teorema de Heckscher-Ohlin") + ").",
            "“Entre outras hipóteses” é preciso: além do número de fatores, mudam a hipótese tecnológica, o formato "
            "da FPP e a mobilidade (fatores móveis entre setores, imóveis entre países).",
            "Do H-O derivam três teoremas cobrados em conjunto: " + azb("Stolper-Samuelson") + " (preço dos bens → "
            "renda dos fatores), " + azb("equalização dos preços dos fatores") + " e " + azb("Rybczynski")
            + " (dotação → composição da produção).",
            vm("Regra-âncora: Ricardo = produtividade (tecnologia); H-O = dotação relativa de fatores."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de comparação entre modelos, sem armadilha: o "
                       "“entre outras hipóteses” protege contra a acusação de reducionismo. O risco é o candidato "
                       "achar que o H-O “também” se baseia em diferenças tecnológicas — não: supõe tecnologia "
                       "idêntica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…de maneira que o padrão de comércio será definido pelas diferenças tecnológicas entre os "
            "países.”</i> → ERRADO (troca de conceito: isso é Ricardo)",
            "<i>“…difere do modelo de Ricardo por supor tecnologias de produção idênticas entre os países.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["entre outras hipóteses"], "dificuldade": 1,
        "comentario_fonte": ("Ricardo: diferenças de produtividade do trabalho; H-O: mesma tecnologia, dois fatores, "
                             "comércio pelas dotações relativas — exporta o bem intensivo no fator abundante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00465-1, ECO-E2-L01620-1 (clássicos × neoclássicos)"],
    },
    # ------------------------------------------------------------------ E2-L01623
    {
        "id": "ECO-E2-L01623-1", "fonte_ref": "E2-L01623", "destino": "73", "subtema": H2["leo"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_TEO,
        "rotulo_item": "Item",
        "assertiva": ("O paradoxo de Leontief levou ao abandono da teoria do comércio baseada na dotação de fatores, "
                      "dado que mostrou sua falta de aderência à realidade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O paradoxo de Leontief ") + vm("levou ao abandono") + az(" da teoria do comércio baseada na "
                                                                                  "dotação de fatores, ")
                    + vm("dado que mostrou sua falta de aderência à realidade") + az(".")),
        "poucas": ("O paradoxo " + azb("não") + " levou ao abandono do " + azb("Heckscher-Ohlin") + ", mas a "
                   + azb("refinamentos") + " (capital humano, recursos naturais, tecnologia) que buscaram "
                   "reconciliar a teoria com os dados."),
        "destrinchando": [
            "O achado de " + oc("Leontief") + " (" + vd("1953") + "): as exportações dos EUA, país abundante em "
            "capital, eram menos intensivas em capital que as importações. Foi um choque, porque o H-O era a "
            "teoria dominante — mas um único teste não derruba um modelo cujas hipóteses (dois fatores homogêneos, "
            "tecnologia idêntica, sem proteção) eram sabidamente simplificadoras.",
            "Reação da literatura: em vez de abandonar a dotação de fatores, multiplicaram-se os fatores e as "
            "qualificações — trabalho qualificado × não qualificado, recursos naturais complementares ao capital, "
            "proteção às indústrias trabalho-intensivas, reversão de intensidade, diferenças tecnológicas.",
            "Desenvolvimentos posteriores: o modelo de " + azb("Heckscher-Ohlin-Vanek") + " (conteúdo fatorial do "
            "comércio com muitos fatores) e os testes de " + oc("Trefler") + " (1995) — que encontram desempenho "
            "fraco da versão pura, mas bem melhor quando se admitem diferenças de produtividade entre países.",
            "Hoje a dotação de fatores convive com as " + azb("novas teorias do comércio") + " (escala, "
            "diferenciação, " + oc("Krugman") + "): explica bem o comércio Norte-Sul e o interindustrial; as "
            "novas teorias explicam melhor o intraindustrial entre países semelhantes.",
            vm("Regra-âncora: paradoxo de Leontief → refinamento, nunca abandono."),
        ],
        "dissecando": (cz("[extrapolação · nexo indevido]") + " O item parte de um fato certo (o paradoxo "
                       "contrariou o H-O) e extrapola a consequência: “abandono”. O “dado que” cria um nexo "
                       "conclusivo que a literatura não autoriza. 🔥 Par clássico: “reformulação/refinamento” "
                       "(CERTO) × “abandono” (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O paradoxo de Leontief levou a reformulações da teoria da dotação de fatores, como a distinção "
            "entre trabalho qualificado e não qualificado.”</i> → CERTO",
            "<i>“O paradoxo de Leontief consistiu na constatação de que os EUA exportavam bens intensivos em "
            "capital.”</i> → ERRADO (inversão do achado)",
        ])],
        "reescrita": ("O paradoxo de Leontief " + hl("não levou ao abandono") + " da teoria do comércio baseada na "
                      "dotação de fatores, " + hl("mas a refinamentos que buscaram restaurar sua aderência à "
                                                  "realidade") + "."),
        "tipo_erro": ["EXTRAPOLACAO", "NEXO_INDEVIDO"], "moduladores": ["dado que"], "dificuldade": 1,
        "comentario_fonte": ("O paradoxo desafiou o H-O, mas não levou ao abandono da teoria, e sim a refinamentos "
                             "(capital humano, heterogeneidade do trabalho, reversão de intensidade, demanda)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 464", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (descrição genérica da tabela de Leontief; dados no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01543-1, ECO-E2-L01577-1 (consequências do paradoxo)"],
    },
    # ------------------------------------------------------------------ E2-L01667
    {
        "id": "ECO-E2-L01667-1", "fonte_ref": "E2-L01667", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_JUL,
        "rotulo_item": "Item",
        "assertiva": ("No modelo Heckscher-Ohlin a fronteira de possibilidades de produção é uma linha reta, levando "
                      "à especialização completa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo Heckscher-Ohlin a fronteira de possibilidades de produção é ") + vm("uma linha reta")
                    + az(", levando à especialização ") + vm("completa") + az(".")),
        "poucas": ("FPP reta e especialização completa são do modelo " + azb("ricardiano") + ". No "
                   + azb("Heckscher-Ohlin") + ", a FPP é " + azb("côncava") + " (custo de oportunidade crescente) "
                   "e a especialização é, em regra, <b>incompleta</b>."),
        "destrinchando": [
            "<b>Ricardo</b>: um só fator, com produtividade constante → cada unidade de X custa sempre as mesmas "
            "unidades de Y → " + azb("FPP linear") + ". Se o preço mundial difere do custo interno, compensa "
            "deslocar <b>todo</b> o trabalho para o bem de vantagem comparativa: a produção vai ao canto da FPP "
            "(especialização completa).",
            "<b>Heckscher-Ohlin</b>: dois fatores combinados em proporções diferentes nos dois setores. Ao "
            "expandir X, a economia transfere fatores que são cada vez menos adequados a X (o setor Y libera "
            "relativamente mais do fator de que X precisa menos) → " + azb("custo de oportunidade crescente")
            + " → " + azb("FPP côncava") + " (abaulada para fora).",
            "Com FPP côncava, o país produz onde a FPP tangencia a linha de preços mundiais: expande o bem "
            "intensivo no fator abundante, mas, em geral, continua produzindo um pouco do outro — "
            + azb("especialização incompleta") + ". A especialização completa só ocorre se os preços mundiais "
            "forem muito distantes dos de autarquia.",
            "A diversificação importa para os teoremas: a equalização completa dos preços dos fatores pressupõe "
            "que ambos os países continuem produzindo os dois bens.",
            vm("Regra-âncora: Ricardo → FPP reta, especialização completa; H-O → FPP côncava, especialização "
               "incompleta."),
        ],
        "grafico_verso": "ECO-E2-L01667-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item transplanta para o H-O duas características do modelo "
                       "ricardiano (FPP reta e especialização completa). Como as duas são coerentes entre si, a "
                       "frase “fecha” — o teste é perguntar: quantos fatores? Dois fatores com intensidades "
                       "diferentes → curvatura."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, a FPP é uma linha reta, o que tende a levar à especialização "
            "completa.”</i> → CERTO",
            "<i>“No modelo Heckscher-Ohlin, a FPP côncava reflete custos de oportunidade decrescentes.”</i> → "
            "ERRADO (são crescentes)",
        ])],
        "reescrita": ("No modelo Heckscher-Ohlin a fronteira de possibilidades de produção é " + hl("côncava")
                      + ", levando à especialização " + hl("incompleta") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No H-O a FPP é côncava (custos de oportunidade crescentes) e a especialização é "
                             "incompleta; FPP linear e especialização completa são do modelo ricardiano."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 485", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (descrição genérica de slide; conteúdo coberto no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01668
    {
        "id": "ECO-E2-L01668-1", "fonte_ref": "E2-L01668", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_JUL,
        "rotulo_item": "Item",
        "assertiva": ("No modelo ricardiano das vantagens comparativas, os países tenderão a concentrar-se na "
                      "produção e exportação de bens cujos custos absolutos de produção sejam menores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo ricardiano das vantagens comparativas, os países tenderão a concentrar-se na "
                       "produção e exportação de bens cujos custos ") + vm("absolutos") + az(" de produção sejam "
                                                                                           "menores.")),
        "poucas": ("Custo absoluto menor é a regra de " + oc("Smith") + ". Em " + oc("Ricardo") + ", o critério "
                   "é o custo " + azb("comparativo") + " (de oportunidade): um país pode ter custos absolutos "
                   "maiores em tudo e ainda exportar."),
        "destrinchando": [
            "Exemplo de " + oc("Ricardo") + " (1817), em horas de trabalho por unidade: Portugal — vinho "
            + vd("80") + ", tecido " + vd("90") + "; Inglaterra — vinho " + vd("120") + ", tecido " + vd("100")
            + ". Portugal tem custo absoluto menor nos <b>dois</b> bens.",
            "Custos comparativos: em Portugal, 1 vinho custa 80/90 ≈ " + vd("0,89 tecido") + "; na Inglaterra, "
            "120/100 = " + vd("1,2 tecido") + ". Portugal tem vantagem comparativa em vinho; a Inglaterra, em "
            "tecido (custa-lhe 100/120 ≈ 0,83 vinho, contra 90/80 ≈ 1,13 em Portugal).",
            "Pela regra do item (custos absolutos), Portugal deveria produzir e exportar tudo, e a Inglaterra "
            "nada — o comércio não se sustentaria. Ricardo mostra que ambos ganham com a especialização segundo o "
            "custo <b>relativo</b>, desde que os termos de troca fiquem entre 0,89 e 1,2 tecido por vinho.",
            "O que limita a vantagem absoluta é o equilíbrio do comércio: salários se ajustam (no país mais "
            "produtivo, são mais altos), de modo que o preço em moeda de cada bem reflete a produtividade "
            "relativa, não a absoluta.",
            vm("Regra-âncora: Smith → custo absoluto; Ricardo → custo comparativo (de oportunidade)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca “comparativos” por “absolutos” dentro de uma frase que "
                       "anuncia “vantagens comparativas” — a contradição interna é a pista. 🔥 Erro recorrente: "
                       "atribuir a Ricardo o critério de Smith."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, um país sem vantagem absoluta em nenhum bem ainda pode ganhar com o "
            "comércio.”</i> → CERTO",
            "<i>“No modelo de Adam Smith, os países se especializam nos bens de menor custo de oportunidade.”</i> "
            "→ ERRADO (troca de ator: isso é Ricardo)",
        ])],
        "reescrita": ("No modelo ricardiano das vantagens comparativas, os países tenderão a concentrar-se na "
                      "produção e exportação de bens cujos custos " + hl("comparativos") + " de produção sejam "
                      "menores."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["tenderão"], "dificuldade": 1,
        "comentario_fonte": ("Ricardo: especialização pela vantagem comparativa (menor custo de oportunidade), não "
                             "absoluta; país com desvantagem absoluta em tudo ainda ganha com o comércio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01620-1 (Smith × Ricardo)"],
    },
    # ------------------------------------------------------------------ E2-L01693
    {
        "id": "ECO-E2-L01693-1", "fonte_ref": "E2-L01693", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("O teorema de Rybczynski, que relaciona o aumento da dotação de um fator com o aumento da "
                      "produção absoluta do bem que utiliza este fator intensivamente e redução da produção do outro "
                      "bem, é compatível com o fenômeno conhecido como “doença holandesa” e a desindustrialização "
                      "que se segue num país que descobre grandes reservas de recursos naturais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O teorema de Rybczynski, que relaciona o aumento da dotação de um fator com o aumento da "
                      "produção absoluta do bem que utiliza este fator intensivamente e redução da produção do "
                      "outro bem, <u>é compatível</u> com o fenômeno conhecido como “doença holandesa” e a "
                      "desindustrialização que se segue num país que descobre grandes reservas de recursos "
                      "naturais."),
        "poucas": ("Descobrir recursos naturais = aumentar a dotação desse fator. Pelo " + azb("Rybczynski")
                   + ", o setor extrativo cresce e a indústria encolhe — exatamente o " + azb("efeito-deslocamento "
                   "de recursos") + " da doença holandesa."),
        "destrinchando": [
            "Teorema de " + oc("Rybczynski") + " (" + vd("1955") + "), a preços dos bens constantes: dotação de "
            "um fator ↑ → produção do bem intensivo nele ↑ mais que proporcionalmente; produção do outro bem ↓ "
            "em termos absolutos. A descrição do item está correta (só omite o “mais que proporcionalmente”, o que "
            "não a torna falsa).",
            "Doença holandesa: a Holanda descobriu as jazidas de gás de Groningen em " + vd("1959") + " e, nas "
            "décadas seguintes, viu a indústria perder competitividade. No modelo de " + oc("Corden e Neary") + " "
            "(" + vd("1982") + "), há dois canais: o " + azb("efeito-deslocamento de recursos") + " (fatores "
            "migram para o setor em boom — Rybczynski) e o " + azb("efeito-gasto") + " (a renda extra encarece "
            "os não comercializáveis, o câmbio real se aprecia e a indústria perde mercado).",
            "Por isso o teorema é <b>compatível</b> com a doença holandesa e ajuda a explicá-la, ainda que não "
            "esgote o fenômeno (o canal cambial vem de fora do modelo 2 × 2 de preços dados).",
            "Aplicação ao " + rx("Brasil") + ": o boom de commodities dos anos 2000 reacendeu o debate sobre "
            "doença holandesa e desindustrialização (" + oc("Bresser-Pereira") + " é o autor mais associado à "
            "tese no país); a questão é empiricamente controversa.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Versão correta de um item que a banca também cobra negado "
                       "(“não é compatível” → ERRADO). O item é longo, mas cada pedaço confere com o teorema; a "
                       "dúvida comum é achar que a doença holandesa é “só cambial” e, portanto, alheia ao modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O teorema de Rybczynski não é compatível com a doença holandesa.”</i> → ERRADO (contradição)",
            "<i>“Pelo teorema de Rybczynski, a descoberta de recursos naturais aumenta proporcionalmente a produção "
            "de todos os setores.”</i> → ERRADO (o outro setor encolhe)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Rybczynski: aumento de um fator eleva a produção do setor que o usa intensivamente e "
                             "reduz a do outro; na doença holandesa, a descoberta de recursos desloca fatores para o "
                             "setor primário e causa desindustrialização."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01578-1 (mesmo tema em versão ERRADA), ECO-E2-L01545-1"],
    },
    # ------------------------------------------------------------------ E2-L01695
    {
        "id": "ECO-E2-L01695-1", "fonte_ref": "E2-L01695", "destino": "73", "subtema": H2["leo"],
        "tipo": "C/E", "banca": RT, "prova": RT_PROVA, "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_RT_CONC,
        "rotulo_item": "Item",
        "assertiva": ("O paradoxo de Leontief se refere ao fato de que a maior parte do comércio mundial se dá entre "
                      "países com dotações de fatores semelhantes, ao contrário do esperado pelo modelo "
                      "Heckscher-Ohlin."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O paradoxo de Leontief se refere ao fato de que ")
                    + vm("a maior parte do comércio mundial se dá entre países com dotações de fatores semelhantes")
                    + az(", ao contrário do esperado pelo modelo Heckscher-Ohlin.")),
        "poucas": ("O paradoxo de " + oc("Leontief") + " é o achado de que os " + azb("EUA") + ", abundantes em "
                   "capital, exportavam bens relativamente " + azb("intensivos em trabalho") + ". O comércio entre "
                   "países semelhantes é outro fato estilizado, explicado pelas novas teorias do comércio."),
        "destrinchando": [
            "O paradoxo é sobre a <b>composição</b> do comércio de um país: " + oc("Wassily Leontief") + " ("
            + vd("1953") + ") calculou, com a matriz insumo-produto, o capital e o trabalho incorporados nas "
            "exportações e nas importações dos EUA e viu que as exportações eram menos intensivas em capital. "
            "Dados de 1962 confirmaram: " + vd("US$ 14.321") + " de capital por trabalhador nas exportações contra "
            + vd("US$ 17.916") + " nas importações.",
            "O fato descrito no item — grande parte do comércio ocorre entre países ricos, de dotações parecidas, "
            "e muitas vezes dentro da mesma indústria (" + azb("comércio intraindustrial") + ") — também desafia "
            "o H-O, mas tem outro nome e outra explicação: " + azb("economias de escala") + " e "
            + azb("diferenciação de produtos") + " (" + oc("Krugman") + ", 1979; " + oc("Linder") + ", 1961, "
            "com a hipótese da demanda representativa).",
            "Explicações do paradoxo de Leontief: trabalho heterogêneo (os EUA são abundantes em trabalho "
            "qualificado), recursos naturais complementares ao capital, proteção às indústrias trabalho-intensivas, "
            "reversão de intensidade fatorial.",
            vm("Regra-âncora: Leontief = EUA exportando bens trabalho-intensivos; comércio entre iguais = "
               "intraindustrial (novas teorias)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item cola o nome “paradoxo de Leontief” em outra anomalia "
                       "empírica do H-O. As duas contrariam o modelo, o que torna o “ao contrário do esperado” "
                       "verdadeiro e dá aparência de acerto; o erro está na definição do paradoxo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O comércio intraindustrial entre países com dotações semelhantes é melhor explicado por economias "
            "de escala e diferenciação de produtos do que pelo modelo Heckscher-Ohlin.”</i> → CERTO",
            "<i>“O paradoxo de Leontief consistiu em constatar que os EUA importavam bens intensivos em "
            "trabalho.”</i> → ERRADO (inversão: importavam bens intensivos em capital)",
        ])],
        "reescrita": ("O paradoxo de Leontief se refere ao fato de que " + hl("os EUA, abundantes em capital, "
                      "exportavam bens relativamente intensivos em trabalho") + ", ao contrário do esperado pelo "
                      "modelo Heckscher-Ohlin."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O paradoxo é a constatação de que os EUA exportavam bens trabalho-intensivos e "
                             "importavam capital-intensivos; comércio entre países semelhantes é tema da nova teoria "
                             "do comércio (intraindustrial)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 499", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (descrição genérica da tabela de Leontief; dados no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00010
    {
        "id": "ECO-E3-L00010-1", "fonte_ref": "E3-L00010", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": "Acerca dos conceitos fundamentais de microeconomia, julgue o item que se segue.",
        "rotulo_item": "Item",
        "assertiva": ("O livre-comércio internacional pode expandir as possibilidades de consumo de um país para além "
                      "de sua própria fronteira de possibilidades de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O livre-comércio internacional pode expandir as possibilidades de <u>consumo</u> de um país "
                      "para além de sua própria fronteira de possibilidades de <u>produção</u>."),
        "poucas": ("Com comércio, o país " + azb("produz num ponto e consome em outro") + ": especializa-se segundo "
                   "a vantagem comparativa, troca ao preço mundial e alcança cestas de consumo fora da sua FPP."),
        "destrinchando": [
            "A " + azb("FPP") + " mostra o máximo que o país consegue <b>produzir</b> com seus recursos e sua "
            "tecnologia. Na autarquia, consumo = produção, e a FPP é também o limite do consumo.",
            "Com livre-comércio, o país desloca a produção para o bem de " + azb("vantagem comparativa") + " "
            "(ponto P) e troca parte dela ao " + azb("preço mundial") + ". A linha de comércio que passa por P "
            "fica, exceto no próprio P, por fora da FPP: o país pode consumir uma cesta C com mais dos dois bens "
            "do que tinha na autarquia (ponto A).",
            "O ganho vem de dois efeitos: " + azb("ganho de troca") + " (comprar ao preço mundial, mais "
            "vantajoso que o custo interno) e " + azb("ganho de especialização") + " (realocar a produção para "
            "onde o custo de oportunidade é menor).",
            "Atenção ao objeto: a FPP <b>não</b> se desloca com o comércio — os recursos e a tecnologia são os "
            "mesmos. O que se expande é a fronteira de possibilidades de <b>consumo</b>. Afirmar que o comércio "
            "“desloca a FPP para fora” é o erro que a banca costuma plantar.",
            vm("Regra-âncora: comércio amplia o conjunto de consumo, não o de produção."),
        ],
        "grafico_verso": "ECO-E3-L00010-1-V1",
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Item de conceito, protegido pelo “pode”. "
                       "O ponto delicado é a distinção consumo × produção: a frase fala em possibilidades de "
                       "consumo indo além da fronteira de produção, que é exatamente o ganho do comércio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O livre-comércio internacional desloca para fora a fronteira de possibilidades de produção do "
            "país.”</i> → ERRADO (troca de conceito: expande o consumo, não a produção)",
            "<i>“Com livre-comércio, o país passa a consumir mais de ambos os bens, qualquer que seja o preço "
            "mundial.”</i> → ERRADO (se o preço mundial igualar o custo interno, não há ganho)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Com comércio, o país se especializa pela vantagem comparativa e troca, alcançando "
                             "combinações de consumo além da FPP; a FPP continua limitando a produção, não o "
                             "consumo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00085-1 (consumo além da FPP com comércio)"],
    },
    # ------------------------------------------------------------------ E3-L00083
    {
        "id": "ECO-E3-L00083-1", "fonte_ref": "E3-L00083", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": NIDI, "prova": "Simulado Julho/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_NIDI_RIC,
        "rotulo_item": "Item",
        "assertiva": ("No modelo ricardiano das vantagens comparativas, o papel desempenhado pelas economias de escala "
                      "na produção é fundamental para o entendimento das razões do comércio entre países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo ricardiano das vantagens comparativas, o papel desempenhado pelas ")
                    + vm("economias de escala") + az(" na produção é fundamental para o entendimento das razões do "
                                                       "comércio entre países.")),
        "poucas": ("O modelo ricardiano supõe " + azb("rendimentos constantes de escala") + ": o comércio nasce de "
                   "diferenças de " + azb("produtividade relativa do trabalho") + ". Economias de escala são o "
                   "motor das " + azb("novas teorias do comércio") + "."),
        "destrinchando": [
            "Hipóteses de " + oc("Ricardo") + ": um fator (trabalho), coeficientes técnicos fixos — cada unidade "
            "de vinho custa sempre as mesmas horas, produza-se pouco ou muito. Por isso a FPP é uma reta e o custo "
            "de oportunidade é constante.",
            "Com rendimentos constantes, o tamanho da produção não muda a eficiência: a única razão para trocar "
            "são as diferenças de tecnologia entre países, que geram custos comparativos distintos.",
            "Os modelos neoclássicos (Heckscher-Ohlin) também supõem rendimentos constantes de escala e "
            "concorrência perfeita. As economias de escala entram na teoria do comércio com a " + azb("teoria do "
            "ciclo do produto") + " (" + oc("Vernon") + ", " + vd("1966") + ") e, de forma formal, com "
            + oc("Paul Krugman") + " (" + vd("1979") + "), que une rendimentos crescentes, concorrência "
            "monopolística e gosto por variedade para explicar o " + azb("comércio intraindustrial") + " entre "
            "países semelhantes.",
            "Diferença de lógica: em Ricardo, países diferentes trocam por serem diferentes; em Krugman, países "
            "iguais podem trocar porque a escala torna vantajoso concentrar cada variedade num lugar.",
            vm("Regra-âncora: Ricardo = produtividade relativa com rendimentos constantes; escala = novas teorias "
               "(Krugman)."),
        ],
        "dissecando": (cz("[anacronismo · troca de conceito]") + " Atribui a um modelo de 1817 um mecanismo que "
                       "só entrou na teoria do comércio no século XX. O “fundamental” agrava: escala não tem "
                       "<b>nenhum</b> papel em Ricardo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nos modelos da nova teoria do comércio, como o de Krugman, as economias de escala explicam o "
            "comércio entre países com dotações e tecnologias semelhantes.”</i> → CERTO",
            "<i>“O modelo ricardiano supõe rendimentos crescentes de escala, o que explica a especialização "
            "completa.”</i> → ERRADO (rendimentos constantes)",
        ])],
        "reescrita": ("No modelo ricardiano das vantagens comparativas, o papel desempenhado pelas " + hl("diferenças "
                      "de produtividade do trabalho") + " na produção é fundamental para o entendimento das razões "
                      "do comércio entre países."),
        "tipo_erro": ["ANACRONISMO", "TROCA_CONCEITO"], "moduladores": ["fundamental"], "dificuldade": 1,
        "comentario_fonte": ("Ricardo supõe custos constantes; o comércio surge de diferenças de produtividade. "
                             "Economias de escala entram com o ciclo do produto (Vernon, 1966) e com Krugman "
                             "(1979)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 39", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "irrecuperavel"},
                          {"ref": "IMAGEM 40", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "irrecuperavel"}],
        "alertas": ["quase_duplicata: ECO-E2-L01668-1 (hipóteses do modelo ricardiano)"],
    },
    # ------------------------------------------------------------------ E3-L00085
    {
        "id": "ECO-E3-L00085-1", "fonte_ref": "E3-L00085", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": NIDI, "prova": "Simulado Julho/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_NIDI_RIC,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de comércio de David Ricardo descreve como é possível alcançar pontos acima e à "
                      "direita na fronteira de possibilidades de consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo de comércio de David Ricardo descreve como é possível alcançar pontos <u>acima e à "
                      "direita</u> na fronteira de possibilidades de <u>consumo</u>."),
        "poucas": ("Com especialização e troca, a " + azb("fronteira de possibilidades de consumo") + " (FPC) gira "
                   "para fora a partir do ponto de especialização: o país alcança cestas acima e à direita da "
                   "FPP, com mais dos dois bens."),
        "destrinchando": [
            "Na autarquia, a FPC coincide com a FPP. No modelo ricardiano, a FPP é uma " + azb("reta") + ": "
            "custo de oportunidade constante, dado pela produtividade relativa do trabalho.",
            "Aberto o comércio, o país se especializa <b>completamente</b> no bem de vantagem comparativa e troca "
            "aos " + azb("termos de troca") + " internacionais, que precisam estar entre os custos de "
            "oportunidade dos dois países. A nova FPC parte do ponto de especialização com a inclinação dos termos "
            "de troca e fica por fora da FPP.",
            "Exemplo do gráfico: o país produz 1 X ou 2 Y com o mesmo trabalho (custo de 1 X = " + vd("2 Y") + ") "
            "e o mercado mundial paga " + vd("3 Y") + " por X. Especializado em X (P), cada X exportado rende 3 Y, "
            "e não 2: a cesta C tem mais X e mais Y que a cesta de autarquia A.",
            "O comércio funciona como uma " + azb("tecnologia indireta") + ": obter Y exportando X custa menos "
            "trabalho do que produzi-lo em casa. A FPP não muda; muda o que se pode consumir.",
            vm("Regra-âncora: comércio desloca a fronteira de consumo, não a de produção."),
        ],
        "grafico_verso": "ECO-E3-L00085-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " A expressão “acima e à direita na fronteira de possibilidades de "
                       "consumo” soa estranha, mas descreve a FPC com comércio situada além da FPP. O risco é ler "
                       "“fronteira de possibilidades de produção” e marcar ERRADO por achar que o comércio "
                       "expande a produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Ricardo descreve como o comércio desloca para fora a fronteira de possibilidades de "
            "produção dos países.”</i> → ERRADO (troca de conceito: é a de consumo)",
            "<i>“Para que ambos os países ganhem, os termos de troca devem situar-se entre os custos de "
            "oportunidade autárquicos de cada um.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["é possível"], "dificuldade": 1,
        "comentario_fonte": ("Comércio por vantagens comparativas expande a FPC além da FPP autárquica; na "
                             "autarquia FPC = FPP; com especialização e termos de troca favoráveis, alcançam-se "
                             "cestas com mais de ambos os bens."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 43", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quadro FPP × FPC no 📖)"},
                          {"ref": "IMAGEM 44", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (conteúdo coberto no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00010-1 (consumo além da FPP com comércio)"],
    },
    # ------------------------------------------------------------------ E3-L00106
    {
        "id": "ECO-E3-L00106-1", "fonte_ref": "E3-L00106", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": NIDI, "prova": "Simulado Junho/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_NIDI_GLOB,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o princípio das vantagens comparativas, a produção mundial total será maximizada "
                      "se cada bem for produzido pelo país capaz de fazê-lo com os menores custos de oportunidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o princípio das vantagens comparativas, a produção mundial total será "
                      "maximizada se cada bem for produzido pelo país capaz de fazê-lo com os menores <u>custos de "
                      "oportunidade</u>."),
        "poucas": ("É o núcleo do princípio de " + oc("Ricardo") + ": alocar cada bem ao país de menor "
                   + azb("custo de oportunidade") + " economiza recursos e permite produzir mais de tudo com os "
                   "mesmos fatores."),
        "destrinchando": [
            "Custo de oportunidade = quanto de outro bem se deixa de produzir para fazer uma unidade deste. "
            "Vantagem " + azb("comparativa") + " = menor custo de oportunidade; vantagem " + azb("absoluta")
            + " = menos insumo por unidade.",
            "Exemplo numérico: o país A produz, com uma hora, 6 trigo ou 3 tecido (1 tecido custa 2 trigo); o país "
            "B, 1 trigo ou 1 tecido (1 tecido custa 1 trigo). A tem vantagem absoluta nos dois, mas o custo de "
            "oportunidade do tecido é menor em B. Se B desloca 1 hora do trigo para o tecido (−1 trigo, +1 tecido) e A "
            "desloca 1/3 de hora do tecido para o trigo (−1 tecido, +2 trigo), o mundo produz " + vd("1 trigo a "
            "mais") + " sem perder nenhum tecido.",
            "Ou seja: deslocar a produção para quem tem menor custo de oportunidade expande a "
            + azb("FPP mundial") + " efetiva. Ricardo demonstrou isso em 1817 com vinho e tecido entre Portugal "
            "e Inglaterra, mesmo com Portugal mais eficiente nos dois bens.",
            "Hipóteses por trás do “será maximizada”: rendimentos constantes, pleno emprego, concorrência perfeita, "
            "custos de transporte nulos e fatores móveis dentro de cada país. Com custos de transporte ou "
            "rendimentos crescentes, o resultado precisa ser qualificado.",
            vm("Regra-âncora: especializar-se pelo menor custo de oportunidade maximiza a produção conjunta."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. O “será” parece absoluto, mas, dentro das "
                       "hipóteses do modelo, o resultado é exato. A armadilha seria trocar “custos de "
                       "oportunidade” por “custos absolutos”, o que tornaria o item ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se cada bem for produzido pelo país capaz de fazê-lo com a menor quantidade absoluta de "
            "trabalho.”</i> → ERRADO (troca de conceito: vantagem absoluta)",
            "<i>“Um país que não tem vantagem absoluta em nenhum bem não tem como ganhar com o comércio.”</i> → "
            "ERRADO (contradiz o princípio)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["será"], "dificuldade": 1,
        "comentario_fonte": ("Definição de Ricardo: especialização pelo menor custo relativo (de oportunidade), "
                             "não absoluto; recursos mundiais mais bem alocados, FPP global expandida."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 77", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (FPP genérica de livro-texto, sem relação direta com o item)"},
                          {"ref": "IMAGEM 78", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 79", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 80", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 81", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 82", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00109
    {
        "id": "ECO-E3-L00109-1", "fonte_ref": "E3-L00109", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": NIDI, "prova": "Simulado Junho/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_NIDI_GLOB,
        "rotulo_item": "Item",
        "assertiva": ("O modelo clássico de comércio internacional, formulado no começo do século XIX, não era "
                      "adequado à avaliação do comércio de serviços, que só se tornou relevante após a segunda "
                      "guerra mundial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo clássico de comércio internacional, formulado no começo do século XIX, ")
                    + vm("não era adequado") + az(" à avaliação do comércio de serviços, que só se tornou "
                                                   "relevante após a segunda guerra mundial.")),
        "poucas": ("A lógica ricardiana — especializar-se onde o " + azb("custo de oportunidade") + " é menor — "
                   "vale para qualquer atividade transacionável, bens ou " + azb("serviços") + ". O modelo foi "
                   "pensado com vinho e tecido, mas não se restringe a eles."),
        "destrinchando": [
            "O princípio das vantagens comparativas depende só de custos relativos diferentes entre países. Um "
            "país relativamente mais eficiente em desenvolvimento de software pode especializar-se nesse serviço "
            "e importar outros (tradução, contabilidade), com o mesmo ganho mútuo do comércio de bens.",
            "A limitação real do modelo clássico não é o tipo de produto, mas as hipóteses: um único fator "
            "(trabalho), rendimentos constantes, ausência de custos de transporte e de diferenciação.",
            "Sobre a parte histórica: o comércio de serviços ganhou peso e regulação próprios no pós-guerra, "
            "culminando no " + azb("GATS") + " (Acordo Geral sobre o Comércio de Serviços, " + vd("1994")
            + ", Rodada Uruguai). Mas já no século XIX serviços como fretes marítimos, seguros e finanças eram "
            "receitas expressivas da Grã-Bretanha (os “invisíveis” do balanço de pagamentos). O decisivo para o "
            "gabarito é a adequação do modelo, não a cronologia.",
            "Na prática, a teoria das vantagens comparativas foi usada justamente para pensar a liberalização "
            "dos serviços no sistema GATT/OMC.",
            vm("Regra-âncora: vantagem comparativa vale para qualquer bem ou serviço transacionável."),
        ],
        "dissecando": (cz("[restrição indevida · nexo indevido]") + " O item limita o alcance do modelo ao tipo de "
                       "produto e amarra essa limitação a um dado histórico (“só após a segunda guerra”). A lógica "
                       "do custo de oportunidade não depende de o produto ser tangível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O princípio das vantagens comparativas, embora formulado com bens tangíveis, aplica-se também ao "
            "comércio de serviços.”</i> → CERTO",
            "<i>“O modelo ricardiano só se aplica a bens agrícolas, pois supõe rendimentos decrescentes da "
            "terra.”</i> → ERRADO (restrição indevida; supõe custos constantes)",
        ])],
        "reescrita": ("O modelo clássico de comércio internacional, formulado no começo do século XIX, "
                      + hl("já era adequado") + " à avaliação do comércio de serviços, que só se tornou relevante "
                      "após a segunda guerra mundial."),
        "tipo_erro": ["RESTRICAO", "NEXO_INDEVIDO"], "moduladores": ["só"], "dificuldade": 2,
        "comentario_fonte": ("O modelo funciona para serviços (ex.: software × tradução); embora formulado para bens "
                             "tangíveis, o ganho mútuo da especialização não se restringe a bens físicos; a "
                             "limitação estava no fator único. Respostas de IA acrescentam que serviços (fretes, "
                             "seguros) já eram relevantes no século XIX."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 90", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (exemplo do software no 📖)"},
                          {"ref": "IMAGEM 91", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (limitação do fator único no 📖)"}],
        "alertas": ["nota_redacao: a explicação da professora aceita que o comércio de serviços “só se tornou "
                    "relevante” no pós-guerra; o card mantém esse trecho em azul (não é o erro decisivo) e "
                    "registra no 📖 que serviços já pesavam no século XIX"],
    },
    # ------------------------------------------------------------------ E3-L00220
    {
        "id": "ECO-E3-L00220-1", "fonte_ref": "E3-L00220", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": NIDI, "prova": "Simulado Abril/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_NIDI_TCI,
        "rotulo_item": "Item",
        "assertiva": ("A teoria neoclássica do comércio internacional, conhecida como Teorema de Hecksher-Ohlin, "
                      "demonstra como a oferta relativa de fatores de produção e o emprego desses fatores em "
                      "diferentes intensidades na produção explicam os padrões de especialização e as possibilidades "
                      "do comércio internacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria neoclássica do comércio internacional, conhecida como Teorema de Hecksher-Ohlin, "
                      "demonstra como a <u>oferta relativa de fatores</u> de produção e o emprego desses fatores em "
                      "<u>diferentes intensidades</u> na produção explicam os padrões de especialização e as "
                      "possibilidades do comércio internacional."),
        "poucas": ("O " + azb("Heckscher-Ohlin") + " combina dois ingredientes: " + azb("abundância relativa")
                   + " de fatores (entre países) e " + azb("intensidade fatorial") + " (entre bens). Cada país "
                   "exporta o bem intensivo no fator que tem em abundância."),
        "destrinchando": [
            oc("Eli Heckscher") + " (" + vd("1919") + ") e " + oc("Bertil Ohlin") + " (" + vd("1933") + ", "
            "Nobel de 1977) supõem tecnologia idêntica entre países. O que muda são as dotações: o país A é "
            "abundante em capital se (K/L)<sub>A</sub> > (K/L)<sub>B</sub>.",
            "Intensidade fatorial: o bem X é capital-intensivo se usa mais capital por trabalhador que Y, a "
            "quaisquer preços dos fatores (aviões, química × vestuário, calçados). Terra também é fator: soja e "
            "minério são intensivos em terra/recursos naturais.",
            "Mecanismo: abundância → fator barato na autarquia → custo baixo do bem que o usa intensivamente → "
            "vantagem comparativa nesse bem. O " + rx("Brasil") + ", abundante em terra, exporta soja e carne sem "
            "precisar de tecnologia superior: seus insumos é que são relativamente baratos.",
            "A estrutura H-O reúne quatro resultados: o teorema " + azb("Heckscher-Ohlin") + " (padrão de "
            "comércio), " + azb("Stolper-Samuelson") + " (distribuição de renda), " + azb("equalização dos "
            "preços dos fatores") + " e " + azb("Rybczynski") + " (efeito do crescimento de um fator).",
            vm("Regra-âncora: H-O = dotação relativa (país) × intensidade fatorial (bem)."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição correta, com os dois elementos exigidos. A grafia "
                       "“Hecksher” (sem o c) está na fonte e não pesa no julgamento. Erro típico da banca nesse "
                       "tema: atribuir ao H-O diferenças tecnológicas ou produtividade do trabalho."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…demonstra como as diferenças de produtividade do trabalho entre os países explicam os padrões de "
            "especialização.”</i> → ERRADO (troca de conceito: isso é Ricardo)",
            "<i>“…um país abundante em capital tende a exportar bens intensivos em trabalho.”</i> → ERRADO "
            "(inversão)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Definição correta do H-O: país exporta o bem intensivo no fator abundante; dotação "
                             "relativa (terra, trabalho, capital) e intensidade fatorial explicam o comércio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 313", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto ((K/L)A > (K/L)B no 📖)"},
                          {"ref": "IMAGEM 314", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E3-L00258-1 (mesma assertiva, em outro simulado do mesmo curso)"],
    },
    # ------------------------------------------------------------------ E3-L00222
    {
        "id": "ECO-E3-L00222-1", "fonte_ref": "E3-L00222", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": NIDI, "prova": "Simulado Abril/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_NIDI_TCI,
        "rotulo_item": "Item",
        "assertiva": ("Suponha que a produção de soja no Brasil seja intensiva em mão de obra e que o país imponha uma "
                      "barreira tarifária sobre a soja americana, segundo o Teorema Stolper-Samuelson, a renda do "
                      "fator trabalho no Brasil se reduz."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Suponha que a produção de soja no Brasil seja intensiva em mão de obra e que o país imponha "
                       "uma barreira tarifária sobre a soja americana, segundo o Teorema Stolper-Samuelson, a renda "
                       "do fator trabalho no Brasil ") + vm("se reduz") + az(".")),
        "poucas": ("A tarifa eleva o preço interno da soja; se a soja é " + azb("trabalho-intensiva") + ", pelo "
                   + azb("Stolper-Samuelson") + " a remuneração real do trabalho <b>sobe</b> (e a do capital cai)."),
        "destrinchando": [
            "Cadeia: tarifa sobre a soja importada → preço interno da soja ↑ → produção nacional de soja se expande "
            "→ demanda por trabalho (fator intensivo) ↑ → " + vd("salário real ↑") + "; o setor que encolhe libera "
            "capital → " + vd("remuneração do capital ↓") + ".",
            "Enunciado do teorema (" + oc("Stolper e Samuelson") + ", " + vd("1941") + "): o aumento no preço "
            "relativo de um bem eleva o retorno real do fator usado intensivamente na sua produção e reduz o do "
            "outro — com magnificação (o salário sobe mais que o preço da soja).",
            "Origem histórica: o artigo de 1941 nasceu justamente da pergunta “a proteção pode beneficiar o "
            "trabalho?”. Num país em que o trabalho é o fator <b>escasso</b> e os importados são "
            "trabalho-intensivos, a tarifa aumenta o salário real — o que explica o apoio de sindicatos ao "
            "protecionismo em países ricos.",
            "Premissa contrafactual: na realidade, a soja brasileira é intensiva em terra e capital, e o Brasil é "
            "exportador líquido, não importador. O item pede para <b>supor</b> o contrário; julga-se a lógica, "
            "não o fato.",
            vm("Regra-âncora: tarifa → preço do bem protegido ↑ → fator intensivo nele ganha."),
        ],
        "dissecando": (cz("[inversão]") + " Premissas bem montadas e conclusão invertida. O “Suponha” sinaliza "
                       "que não importa se a soja é de fato trabalho-intensiva: basta aplicar a regra. A pista é "
                       "lembrar que tarifa = preço interno maior."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a renda do fator trabalho no Brasil se eleva, e a do capital se reduz.”</i> → CERTO",
            "<i>“…a renda de ambos os fatores se eleva, pois a produção de soja aumenta.”</i> → ERRADO (o outro "
            "fator perde)",
        ])],
        "reescrita": ("Suponha que a produção de soja no Brasil seja intensiva em mão de obra e que o país imponha "
                      "uma barreira tarifária sobre a soja americana, segundo o Teorema Stolper-Samuelson, a renda "
                      "do fator trabalho no Brasil " + hl("se eleva") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A tarifa eleva o preço da soja; sendo a soja intensiva em trabalho, o salário real "
                             "sobe, e não cai; o capital perde."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 315", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetição do enunciado)"},
                          {"ref": "IMAGEM 316", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (cadeia da tarifa no 📖)"},
                          {"ref": "IMAGEM 317", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_corrigido: OCR da assertiva — “pais” → “país”, “tarifaria” → “tarifária”, “sofre” → "
                    "“sobre”",
                    "quase_duplicata: ECO-E2-L01542-1, ECO-E2-L01621-1 (Stolper-Samuelson invertido)"],
    },
    # ------------------------------------------------------------------ E3-L00258
    {
        "id": "ECO-E3-L00258-1", "fonte_ref": "E3-L00258", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": NIDI, "prova": "Simulado Março/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": "No que diz respeito à Teoria do Comércio Internacional, julgue certo ou errado (C ou E) o item "
                   "a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A teoria neoclássica do comércio internacional, conhecida como Teorema de Hecksher-Ohlin, "
                      "demonstra como a oferta relativa de fatores de produção e o emprego desses fatores em "
                      "diferentes intensidades na produção explicam os padrões de especialização e as possibilidades "
                      "do comércio internacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria neoclássica do comércio internacional, conhecida como Teorema de Hecksher-Ohlin, "
                      "demonstra como a <u>oferta relativa de fatores</u> de produção e o emprego desses fatores em "
                      "<u>diferentes intensidades</u> na produção explicam os padrões de especialização e as "
                      "possibilidades do comércio internacional."),
        "poucas": ("É a máxima do " + azb("Heckscher-Ohlin") + ": um país exporta os bens que usam "
                   "intensivamente o fator que ele tem em " + azb("abundância relativa") + " e importa os que usam "
                   "o fator escasso."),
        "destrinchando": [
            "Duas premissas, e o item menciona as duas: (1) " + azb("diferença de dotação") + " — os países têm "
            "abundâncias relativas distintas (compara-se K/L entre países: o Japão tem muito capital por "
            "trabalhador, o " + rx("Brasil") + ", muita terra); (2) " + azb("diferença de intensidade") + " — os "
            "bens usam fatores em proporções distintas (agricultura intensiva em terra, indústria pesada em "
            "capital, confecção em trabalho).",
            "Por que é “neoclássica”: tecnologia dada e igual entre países, retornos constantes, concorrência "
            "perfeita, fatores móveis entre setores e imóveis entre países — e o comércio decorre de preços "
            "relativos de fatores que diferem na autarquia.",
            "Abundância pode ser definida por quantidades físicas (K/L) ou por preços dos fatores na autarquia "
            "(w/r): país abundante em capital tem r/w baixo. As duas definições coincidem se as preferências forem "
            "idênticas e homotéticas.",
            "Desdobramentos cobrados junto: Stolper-Samuelson (quem ganha e quem perde), equalização dos preços dos "
            "fatores e Rybczynski; e o teste empírico mais famoso, o " + azb("paradoxo de Leontief") + ".",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " A banca reaproveita esta mesma redação em mais de um simulado. "
                       "Não há armadilha; o candidato erra quando desconfia de “demonstra” (forte, mas correto para "
                       "um teorema dentro das suas hipóteses) ou confunde H-O com Ricardo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O teorema de Heckscher-Ohlin explica o comércio pelas diferenças de tecnologia entre os "
            "países.”</i> → ERRADO (troca de conceito: é Ricardo)",
            "<i>“Pelo H-O, um país abundante em trabalho exporta bens trabalho-intensivos.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Transcrição da máxima do modelo: país exporta bens intensivos no fator abundante e "
                             "importa os intensivos no fator escasso; dotação × intensidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00220-1 (mesma assertiva, em outro simulado do mesmo curso)"],
    },
    # ------------------------------------------------------------------ E3-L00431
    {
        "id": "ECO-E3-L00431-1", "fonte_ref": "E3-L00431", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": NIDI, "prova": "Outubro/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_JB_OUT,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o teorema de Stolper-Samuelson, a abertura comercial beneficia o fator de produção "
                      "relativamente abundante em um país, aumentando sua remuneração, e pode prejudicar o fator "
                      "relativamente escasso, o que implica em uma redistribuição dos ganhos do comércio entre os "
                      "agentes econômicos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o teorema de Stolper-Samuelson, a abertura comercial beneficia o fator de produção "
                      "relativamente <u>abundante</u> em um país, aumentando sua remuneração, e <u>pode</u> "
                      "prejudicar o fator relativamente <u>escasso</u>, o que implica em uma redistribuição dos "
                      "ganhos do comércio entre os agentes econômicos."),
        "poucas": ("Com a abertura, sobe o preço do bem exportado (intensivo no fator " + azb("abundante")
                   + ") e cai o do importado (intensivo no " + azb("escasso") + "): pelo " + azb("Stolper-Samuelson")
                   + ", o abundante ganha e o escasso perde — conflito distributivo."),
        "destrinchando": [
            "Teorema de " + oc("Wolfgang Stolper") + " e " + oc("Paul Samuelson") + " (" + vd("1941") + "): a "
            "alta do preço relativo de um bem eleva a remuneração real do fator usado intensivamente nele e reduz a "
            "do outro. A abertura é exatamente uma mudança de preços relativos: o bem exportável encarece "
            "internamente, o importável barateia.",
            "Daí a leitura distributiva: o país como um todo ganha (os ganhadores poderiam compensar os "
            "perdedores), mas há " + azb("ganhadores e perdedores internos") + ". Por isso a abertura gera "
            "coalizões políticas a favor (donos do fator abundante) e contra (donos do fator escasso).",
            "Exemplos: num país abundante em terra, como o " + rx("Brasil") + ", a abertura favorece o "
            "agronegócio exportador; nos EUA, abundantes em capital e trabalho qualificado, a concorrência com "
            "importações trabalho-intensivas pressiona o salário do trabalhador pouco qualificado.",
            "O “pode prejudicar” é até cauteloso: no modelo, o fator escasso <b>perde</b> em termos reais. A "
            "única forma de proteger sua remuneração é a tarifa sobre o bem que compete com as importações.",
            vm("Regra-âncora: Stolper-Samuelson = comércio redistribui renda entre fatores dentro de cada país."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição exata do teorema, protegida pelo "
                       "“pode”. A regência “implica em” é coloquial (a norma prefere “implica”), mas não altera o "
                       "julgamento de conteúdo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o teorema de Stolper-Samuelson, a abertura comercial beneficia todos os fatores de "
            "produção, pois amplia o bem-estar do país.”</i> → ERRADO (modulador absoluto)",
            "<i>“…a abertura beneficia o fator relativamente escasso, que passa a ser importado indiretamente.”</i> "
            "→ ERRADO (inversão)",
        ]), ("🃏 Carta na manga", [
            "Stolper-Samuelson é o argumento padrão para defender que a liberalização comercial venha acompanhada "
            "de políticas compensatórias (requalificação, seguro, transferências) aos grupos perdedores."])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Definição exata do Stolper-Samuelson: abertura altera preços relativos; dono do fator "
                             "abundante ganha, dono do escasso perde, gerando conflito distributivo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 597", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (autores, data e papel da tarifa no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01544-1 (fator abundante ganha, escasso perde)"],
    },
    # ------------------------------------------------------------------ E3-L00433
    {
        "id": "ECO-E3-L00433-1", "fonte_ref": "E3-L00433", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": NIDI, "prova": "Outubro/2024", "ano": 2024, "cacd": False, "errei": True,
        "comando": CMD_JB_OUT,
        "rotulo_item": "Item",
        "assertiva": ("No contexto de concorrência perfeita, o modelo de Heckscher-Ohlin prevê que os países tendem "
                      "a exportar bens que utilizam intensivamente os fatores de produção nos quais são relativamente "
                      "abundantes, resultando em uma completa equalização dos preços dos fatores de produção entre "
                      "os países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("No contexto de concorrência perfeita, o modelo de Heckscher-Ohlin prevê que os países tendem "
                       "a exportar bens que utilizam intensivamente os fatores de produção nos quais são "
                       "relativamente abundantes, ")
                    + vm("resultando em uma completa equalização dos preços dos fatores de produção entre os países")
                    + az(".")),
        "poucas": ("A 1ª parte é o " + azb("teorema de Heckscher-Ohlin") + ". A “completa equalização” não decorre "
                   "automaticamente dele: é outro resultado (" + azb("teorema da equalização dos preços dos "
                   "fatores") + ", de " + oc("Samuelson") + "), que exige hipóteses adicionais muito restritivas."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "no modelo canônico 2 × 2 × 2 de Heckscher-Ohlin-Samuelson (tecnologias idênticas, "
                          "retornos constantes, sem custos de transporte nem tarifas, sem reversão de intensidade e "
                          "com os dois países produzindo os dois bens), a equalização completa é resultado padrão, e "
                          "muitos manuais a apresentam como previsão do modelo. O ERRADO se sustenta na leitura de que "
                          "o item trata como consequência automática, “no contexto de concorrência perfeita”, um "
                          "resultado que depende de várias outras hipóteses — e que " + oc("Ohlin") + " via apenas "
                          "como tendência parcial. Numa prova CEBRASPE, a versão sem ressalvas tende a ser julgada "
                          "ERRADA, mas a questão admitiria recurso.")],
        "destrinchando": [
            "Teorema de Heckscher-Ohlin (padrão de comércio): cada país exporta o bem intensivo no fator "
            "relativamente abundante. Essa parte do item está correta.",
            azb("Teorema da equalização dos preços dos fatores") + " (" + oc("Samuelson") + ", " + vd("1948–1949")
            + "): com livre-comércio, preços dos bens iguais entre países e tecnologias idênticas, a igualdade dos "
            "preços dos bens leva à igualdade dos preços dos fatores (salários e aluguel do capital), em termos "
            "absolutos e relativos — o comércio de bens substitui a mobilidade dos fatores.",
            "Hipóteses exigidas para a equalização <b>completa</b>: ausência de custos de transporte e barreiras; "
            "mesma tecnologia; " + azb("diversificação") + " (os dois países continuam produzindo os dois bens — "
            "com especialização completa, a ligação entre preços dos bens e dos fatores se rompe); ausência de "
            + azb("reversão de intensidade fatorial") + "; número de bens pelo menos igual ao de fatores.",
            "Na realidade, quase nenhuma vale: há tarifas, custos de transporte, tecnologias muito distintas — e "
            "salários de trabalhadores comparáveis diferem enormemente entre países com comércio intenso. O que se "
            "observa é, no máximo, uma " + azb("tendência à convergência") + ".",
            vm("Regra-âncora: H-O prevê o padrão de comércio; a equalização completa é um teorema à parte, "
               "condicionado a hipóteses fortes."),
        ],
        "dissecando": (cz("[extrapolação · modulador absoluto]") + " A 1ª metade é literal e verdadeira; o erro "
                       "foi enxertado no gerúndio “resultando em”, que transforma um resultado condicional em "
                       "consequência necessária, reforçado por “completa”. Pista: “tendem a exportar” (cauteloso) "
                       "contrasta com “completa equalização” (absoluto)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o que tende a aproximar os preços dos fatores de produção entre os países.”</i> → CERTO",
            "<i>“Pelo teorema da equalização, o livre-comércio iguala os preços dos fatores mesmo que um dos "
            "países se especialize completamente.”</i> → ERRADO (exige diversificação)",
        ])],
        "reescrita": ("No contexto de concorrência perfeita, o modelo de Heckscher-Ohlin prevê que os países tendem "
                      "a exportar bens que utilizam intensivamente os fatores de produção nos quais são relativamente "
                      "abundantes, " + hl("o que tende a aproximar os preços dos fatores de produção entre os "
                      "países, cuja equalização completa só ocorre sob as hipóteses restritivas do teorema de "
                      "Samuelson") + "."),
        "tipo_erro": ["EXTRAPOLACAO", "GENERALIZACAO"], "moduladores": ["tendem a", "completa"], "dificuldade": 3,
        "comentario_fonte": ("A 1ª parte (padrão de comércio) está certa; a “completa equalização” é outro "
                             "resultado (Samuelson), contingente a hipóteses restritivas que não se verificam; o "
                             "slide da professora data o teorema de Samuelson de 1971 e fala em imobilidade dos "
                             "fatores entre setores."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 602", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (com correção da data do teorema)"},
                          {"ref": "IMAGEM 603", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["contestavel: no modelo HOS canônico a equalização completa é resultado padrão; ERRADO "
                    "depende de ler o item como generalização sem as hipóteses do teorema de Samuelson",
                    "qualidade_fonte: slide da fonte data o teorema de Samuelson de 1971 (é de 1948–1949) e cita "
                    "“imobilidade dos fatores entre setores” como hipótese (o modelo supõe mobilidade "
                    "intersetorial); corrigido no card"],
    },
    # ------------------------------------------------------------------ E3-L00465
    {
        "id": "ECO-E3-L00465-1", "fonte_ref": "E3-L00465", "destino": "73", "subtema": H2["va"],
        "tipo": "C/E", "banca": NIDI, "prova": "Fevereiro/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "No que se refere à economia internacional e suas teorias de comércio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("As teorias clássicas do comércio internacional baseiam-se na produtividade relativa da mão de "
                      "obra, e a teoria neoclássica do comércio internacional, na diferença relativa de dotação dos "
                      "fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As teorias <u>clássicas</u> do comércio internacional baseiam-se na <u>produtividade relativa "
                      "da mão de obra</u>, e a teoria <u>neoclássica</u> do comércio internacional, na <u>diferença "
                      "relativa de dotação dos fatores</u> de produção."),
        "poucas": ("Clássicos (" + oc("Smith") + ", " + oc("Ricardo") + "): comércio por diferenças de "
                   + azb("produtividade do trabalho") + ". Neoclássicos (" + oc("Heckscher-Ohlin") + "): comércio "
                   "por diferenças de " + azb("dotação relativa de fatores") + ", com tecnologia igual."),
        "destrinchando": [
            "<b>Clássicos</b> — " + oc("Adam Smith") + " (" + vd("1776") + ", vantagem absoluta) e " + oc("David "
            "Ricardo") + " (" + vd("1817") + ", vantagem comparativa): um só fator, o trabalho (teoria do "
            "valor-trabalho); o que difere entre países é a tecnologia, medida pela produtividade do trabalho. Em "
            "Ricardo, o que conta é a produtividade <b>relativa</b> (custo de oportunidade).",
            "<b>Neoclássicos</b> — " + oc("Heckscher") + " (" + vd("1919") + ") e " + oc("Ohlin") + " ("
            + vd("1933") + "), depois " + oc("Samuelson") + ": dois ou mais fatores, tecnologia idêntica entre "
            "países; o comércio nasce das diferenças de <b>abundância relativa</b> de capital, trabalho e terra, "
            "combinadas com a intensidade fatorial dos bens.",
            "Consequência que a banca explora: no modelo clássico não há conflito distributivo interno (só existe "
            "trabalho); no neoclássico, o comércio cria ganhadores (fator abundante) e perdedores (fator escasso).",
            "Depois vieram as " + azb("novas teorias do comércio") + " (" + oc("Krugman") + ", anos 1970–80): "
            "escala, concorrência imperfeita e comércio intraindustrial entre países semelhantes.",
            vm("Regra-âncora: clássicos = produtividade do trabalho; neoclássicos = dotação relativa de fatores."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Síntese correta das duas tradições, com o adjetivo “relativa” "
                       "bem empregado nas duas metades. A armadilha usual seria inverter as bases (clássicos com "
                       "dotação, neoclássicos com produtividade) ou trocar “relativa” por “absoluta” em Ricardo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As teorias clássicas baseiam-se na diferença de dotação de fatores, e a neoclássica, na "
            "produtividade do trabalho.”</i> → ERRADO (inversão)",
            "<i>“A teoria neoclássica supõe tecnologias de produção idênticas entre os países.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Clássicos (Smith, Ricardo): produtividade do trabalho; neoclássicos (H-O): dotação "
                             "relativa de fatores combinada com intensidade fatorial."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01620-1, ECO-E2-L01622-1 (clássicos × neoclássicos)"],
    },
]
