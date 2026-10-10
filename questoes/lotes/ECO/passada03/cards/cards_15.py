"""Cards do lote de redação 15 — ECO, passada 03 (nota 73: teorias clássicas e neoclássicas do comércio)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "vac": "⛵ Vantagens absolutas e comparativas",
    "ho": "🧪 Heckscher-Ohlin e teoremas",
    "leo": "❓ Paradoxo de Leontief e termos de troca",
}

CMD_TC = "Em relação às teorias do comércio, julgue o item a seguir."
CMD_EI = "Em relação à economia internacional, julgue o item a seguir."
CMD_CN = "Considerando as teorias clássicas e neoclássicas do comércio internacional, julgue o item a seguir."
CMD_DC = "Com relação às teorias do desenvolvimento e do comércio, julgue o item a seguir."
CMD_AB = ("Suponha que dois países, A e B, produzam os bens x e y utilizando, para tanto, o fator trabalho como único "
          "insumo de produção. Considere as duas situações apresentadas na tabela e que o país A seja uma economia "
          "muito maior que o país B, de modo que a economia de B não consiga suprir o mercado mundial de nenhum dos "
          "produtos. A respeito do caso hipotético apresentado, julgue o item a seguir.")
CMD_MICRO = "Em relação à microeconomia e à teoria do comércio internacional, julgue o item a seguir."
CMD_MACRO = "Sobre teorias do comércio e macroeconomia aberta, julgue o item a seguir."
CMD_TCI = "Com relação às teorias do comércio internacional, julgue o item a seguir."
CMD_RT1 = "Acerca dos temas de economia internacional, julgue o item a seguir."
CMD_RT2 = "Acerca das teorias do comércio internacional, julgue o item a seguir."
CMD_RT3 = "A respeito das teorias do comércio internacional, julgue o item a seguir."

TAB_AB = {
    "titulo": "Unidades produzidas por unidade de trabalho",
    "cabecalho": ["Bem", "Situação 1 — país A", "Situação 1 — país B", "Situação 2 — país A",
                  "Situação 2 — país B"],
    "linhas": [["x", "4", "1", "4", "1"],
               ["y", "8", "6", "8", "2"]],
    "fonte": "Tabela reconstruída a partir dos valores citados na resolução do item.",
}

AVISO_AB = ("Tabela reconstruída: na fonte, os dados vinham numa imagem não preservada; valores deduzidos da "
            "resolução.")

FIG_160 = [{"ref": "IMAGEM 160", "tipo_fonte": "TEXTO", "lado": "frente",
            "acao": "transcrita_html (tabela aninhada reconstruída pelos números do comentário)"}]

ALERTA_160 = ("texto_reconstruido: a IMAGEM 160 (tabela de produtividades) não foi transcrita; valores deduzidos do "
              "comentário da fonte — situação 1: A 4x ou 8y, B 1x ou 6y; situação 2: A 4x ou 8y, B 1x ou 2y")

CARDS = [
    # ------------------------------------------------------------------ E2-L00571
    {
        "id": "ECO-E2-L00571-1", "fonte_ref": "E2-L00571", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_TC,
        "rotulo_item": "Item",
        "assertiva": ("O Modelo Heckscher-Ohlin assume que as tecnologias de produção são idênticas entre os países, "
                      "diferentemente do Modelo Ricardiano."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Modelo Heckscher-Ohlin assume que as tecnologias de produção são <u>idênticas</u> entre os "
                      "países, <u>diferentemente do Modelo Ricardiano</u>."),
        "poucas": ("Em " + azb("Heckscher-Ohlin") + " a tecnologia é a mesma em todos os países e o comércio nasce da "
                   + azb("dotação relativa de fatores") + "; em " + azb("Ricardo") + ", nasce justamente da "
                   "diferença de tecnologia (produtividade do trabalho)."),
        "destrinchando": [
            "Os dois modelos explicam o comércio por " + azb("vantagem comparativa") + ", mas a <b>fonte</b> da "
            "vantagem é diferente. Em " + oc("David Ricardo") + " (1817), há um só fator (trabalho), e os países "
            "diferem nos requisitos de trabalho por unidade de cada bem: a vantagem vem da " + vd("tecnologia") + ".",
            "Em " + oc("Heckscher") + " (1919) e " + oc("Ohlin") + " (1933), formalizado depois por "
            + oc("Samuelson") + ", há dois fatores (capital e trabalho), funções de produção " + vd("idênticas")
            + " entre países, preferências idênticas, retornos constantes de escala e concorrência perfeita. Se a "
            "tecnologia é igual, só sobra uma diferença possível: a " + vd("abundância relativa de fatores") + ".",
            "Daí o " + azb("teorema de H-O") + ": cada país exporta o bem que usa intensivamente o fator que lhe "
            "é relativamente abundante (país rico em capital exporta bem capital-intensivo).",
            "A hipótese de tecnologia idêntica é deliberada: ela “desliga” o canal ricardiano para isolar o papel "
            "das dotações. Por isso o paradoxo de " + oc("Leontief") + " levou a releituras que reintroduzem "
            "diferenças de produtividade e capital humano.",
            vm("Regra-âncora: Ricardo → tecnologia diferente; H-O → tecnologia igual, dotações diferentes."),
        ],
        "dissecando": (cz("[literalidade]") + " Item de manual, sem pegadinha de modulador. O risco é inverter os "
                       "modelos ou achar que “tecnologia idêntica” impediria o comércio. 🔥 A banca alterna a "
                       "mesma frase com os papéis trocados (Ricardo com tecnologia igual) para gerar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Modelo Ricardiano assume tecnologias idênticas entre os países, diferentemente do modelo "
            "Heckscher-Ohlin.”</i> → ERRADO (modelos trocados)",
            "<i>“No modelo Heckscher-Ohlin, o comércio se explica por diferenças na dotação relativa de "
            "fatores.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "H-O assume tecnologias idênticas e explica o comércio pela dotação de fatores; Ricardo "
                            "usa só o trabalho e explica pela diferença de tecnologia.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00697-1, ECO-E2-L01022-1 (mesma distinção tecnologia × dotações)"],
    },
    # ------------------------------------------------------------------ E2-L00572
    {
        "id": "ECO-E2-L00572-1", "fonte_ref": "E2-L00572", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_TC,
        "rotulo_item": "Item",
        "assertiva": ("O Teorema de Stolper-Samuelson descreve como mudanças nas dotações de fatores afetam as "
                      "quantidades produzidas dos bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Teorema de ") + vm("Stolper-Samuelson") + az(" descreve como mudanças nas dotações de "
                                                                        "fatores afetam as quantidades produzidas "
                                                                        "dos bens.")),
        "poucas": ("Dotação → produção é o " + azb("teorema de Rybczynski") + ". " + azb("Stolper-Samuelson")
                   + " liga outra dupla: preço dos bens → remuneração real dos fatores."),
        "destrinchando": [
            "O modelo H-O tem quatro teoremas, e a banca troca os pares “causa → efeito” entre eles:",
            "<b>Heckscher-Ohlin</b>: dotação relativa → padrão de comércio (exporta o bem intensivo no fator "
            "abundante).",
            "<b>" + oc("Stolper") + "-" + oc("Samuelson") + "</b> (1941): " + vd("preço relativo de um bem ↑")
            + " → a remuneração real do fator usado intensivamente nele sobe, e a do outro fator cai (efeito "
            "ampliação). Base da conclusão “comércio favorece o fator abundante”.",
            "<b>" + oc("Rybczynski") + "</b> (1955): " + vd("dotação de um fator ↑") + ", com preços dos bens "
            "constantes → a produção do bem intensivo nesse fator cresce mais que proporcionalmente, e a do outro "
            "bem cai em termos absolutos. Ex.: descoberta de recursos naturais e “doença holandesa”.",
            "<b>Equalização dos preços dos fatores</b> (Samuelson, 1948): com livre comércio de bens, as "
            "remunerações dos fatores convergem entre países, mesmo sem mobilidade internacional deles.",
            vm("Regra-âncora: preços → fatores = Stolper-Samuelson; dotações → produção = Rybczynski."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A descrição é a definição exata de Rybczynski, com o nome "
                       "trocado. Pista: Stolper-Samuelson sempre fala de <b>remuneração</b> (salário, renda do "
                       "capital); quando o item fala em <b>quantidades produzidas</b>, o teorema é outro."),
        "modulos": [("🧠 Mnemônico", ["<b>R</b>ybczynski = <b>R</b>ecursos (dotação) → produção; "
                                      "<b>S</b>tolper-<b>S</b>amuelson = <b>S</b>alários (remuneração) a partir dos "
                                      "preços."]),
                    ("😈 Para dificultar", [
                        "<i>“O Teorema de Stolper-Samuelson descreve como mudanças nos preços relativos dos bens "
                        "afetam a remuneração real dos fatores.”</i> → CERTO",
                        "<i>“Pelo teorema de Rybczynski, o aumento da dotação de capital reduz a produção do bem "
                        "capital-intensivo.”</i> → ERRADO (inversão: ela aumenta)",
                    ])],
        "reescrita": ("O Teorema de " + hl("Rybczynski") + " descreve como mudanças nas dotações de fatores afetam "
                      "as quantidades produzidas dos bens."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Dotações → produção é Rybczynski; Stolper-Samuelson trata de preços dos bens → "
                            "remuneração real dos fatores.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01508-1 (teorema de Rybczynski)"],
    },
    # ------------------------------------------------------------------ E2-L00573
    {
        "id": "ECO-E2-L00573-1", "fonte_ref": "E2-L00573", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_TC,
        "rotulo_item": "Item",
        "assertiva": ("A aplicação do Teorema de Stolper-Samuelson mostra que o retorno real do fator relativamente "
                      "escasso de um país tende a aumentar com o livre comércio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A aplicação do Teorema de Stolper-Samuelson mostra que o retorno real do fator "
                       "relativamente escasso de um país tende a ") + vm("aumentar") + az(" com o livre comércio.")),
        "poucas": ("Com o livre comércio, o fator " + azb("abundante") + " ganha e o " + azb("escasso")
                   + " perde em termos reais: o retorno do escasso tende a " + vm("cair") + "."),
        "destrinchando": [
            "Cadeia de " + oc("Stolper") + " e " + oc("Samuelson") + " (1941): ao abrir-se, o país exporta o bem "
            "intensivo no fator abundante, cujo preço relativo " + vd("sobe") + " até o nível mundial; o bem "
            "importado (intensivo no fator escasso) fica relativamente " + vd("mais barato") + ".",
            "A produção se desloca para o setor exportador, que demanda proporcionalmente mais do fator abundante. "
            "Com dotações fixas e pleno emprego, a remuneração do fator abundante sobe e a do escasso cai.",
            "O " + azb("efeito ampliação") + " (" + oc("Jones") + ") torna o resultado <b>real</b>, não só "
            "nominal: a remuneração do fator abundante sobe mais que o preço de qualquer bem; a do escasso cai mais "
            "que qualquer preço. O fator escasso perde poder de compra em termos de ambos os bens.",
            "Consequência política: o comércio gera ganhadores e perdedores <b>dentro</b> de cada país. Em país "
            "rico em capital, o trabalho (escasso) tende a apoiar proteção; em país rico em trabalho, o capital. "
            "Os ganhos agregados permitem, em tese, compensar os perdedores.",
            vm("Regra-âncora: abertura → fator abundante ganha; fator escasso perde."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sinal do efeito sobre o fator escasso. O “tende a” "
                       "é só um modulador neutro; o erro está no verbo. 🔥 A banca alterna “escasso” e “abundante” "
                       "e “aumentar” e “reduzir”: monte a cadeia preço do exportado ↑ → fator abundante ↑ antes "
                       "de responder."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o retorno real do fator relativamente abundante de um país tende a aumentar com o livre "
            "comércio.”</i> → CERTO",
            "<i>“…a proteção tarifária tende a elevar o retorno real do fator relativamente escasso.”</i> → CERTO",
        ])],
        "reescrita": ("A aplicação do Teorema de Stolper-Samuelson mostra que o retorno real do fator relativamente "
                      "escasso de um país tende a " + hl("diminuir") + " com o livre comércio."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "O livre comércio aumenta o retorno real do fator abundante e reduz o do fator escasso.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00698-1, ECO-E2-L01470-1, ECO-E2-L00974-1 (Stolper-Samuelson e "
                    "abertura)"],
    },
    # ------------------------------------------------------------------ E2-L00641
    {
        "id": "ECO-E2-L00641-1", "fonte_ref": "E2-L00641", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_TC,
        "rotulo_item": "Item",
        "assertiva": ("As teorias clássicas do comércio internacional baseiam-se nas diferenças tecnológicas que "
                      "culminam em diferentes produtividades relativas da mão de obra, e a teoria neoclássica do "
                      "comércio internacional, na diferença relativa de dotação dos fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As teorias <u>clássicas</u> do comércio internacional baseiam-se nas diferenças tecnológicas "
                      "que culminam em diferentes produtividades relativas da mão de obra, e a teoria "
                      "<u>neoclássica</u> do comércio internacional, na diferença relativa de dotação dos fatores "
                      "de produção."),
        "poucas": ("É a divisão de manual: " + azb("clássicos") + " (Smith, Ricardo) → tecnologia e produtividade "
                   "do trabalho; " + azb("neoclássicos") + " (Heckscher-Ohlin-Samuelson) → dotação relativa de "
                   "fatores."),
        "destrinchando": [
            azb("Teoria clássica") + ": " + oc("Adam Smith") + " (1776, vantagem absoluta) e " + oc("David Ricardo")
            + " (1817, vantagem comparativa). Valor-trabalho, um único fator; os países diferem nos coeficientes "
            "de trabalho por unidade de produto, isto é, na " + vd("tecnologia") + ". No exemplo de Ricardo, "
            "Portugal produz vinho e tecido com menos trabalho que a Inglaterra, mas sua vantagem é "
            "<b>relativamente</b> maior no vinho.",
            azb("Teoria neoclássica") + ": " + oc("Heckscher") + ", " + oc("Ohlin") + " e " + oc("Samuelson")
            + ". Dois ou mais fatores, tecnologia idêntica entre países, e o comércio explicado pela "
            + vd("abundância relativa") + " de capital, trabalho ou terra, combinada com a "
            + vd("intensidade fatorial") + " de cada bem.",
            "O que os une: ambos explicam o comércio por " + azb("vantagem comparativa") + ", com concorrência "
            "perfeita e retornos constantes de escala. O que vem depois: as " + azb("novas teorias do comércio")
            + " (" + oc("Krugman") + "), com economias de escala e concorrência imperfeita, explicam o comércio "
            "intraindustrial entre países parecidos.",
            "A palavra “relativas” importa: o que gera comércio em Ricardo é a produtividade <b>relativa</b> (o "
            "custo de oportunidade), não a absoluta.",
        ],
        "dissecando": (cz("[literalidade]") + " Frase de manual reproduzida quase literalmente. O risco é a troca "
                       "dos rótulos (clássica ↔ neoclássica), que é a versão ERRADA mais cobrada. 🔥 Mesmo item "
                       "aparece em vários simulados, às vezes com “economias de escala” enxertadas no H-O."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As teorias neoclássicas do comércio baseiam-se nas diferenças tecnológicas que geram diferentes "
            "produtividades do trabalho.”</i> → ERRADO (troca clássica ↔ neoclássica)",
            "<i>“No modelo H-O, as vantagens comparativas decorrem de economias de escala.”</i> → ERRADO (economias "
            "de escala são da nova teoria do comércio)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Clássicos (Ricardo): vantagens comparativas por produtividade do trabalho; neoclássicos "
                            "(H-O): tecnologia idêntica e diferenças de dotação de fatores.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01160-1 (mesma assertiva, Nabuco Pré-TPS/2023), ECO-E2-L01468-1, "
                    "ECO-E2-L00845-1"],
    },
    # ------------------------------------------------------------------ E2-L00642
    {
        "id": "ECO-E2-L00642-1", "fonte_ref": "E2-L00642", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_TC,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Heckscher-Ohlin de comércio internacional, as vantagens comparativas, que levam "
                      "ao comércio entre dois países, decorrem de economias de escala na produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Heckscher-Ohlin de comércio internacional, as vantagens comparativas, que "
                       "levam ao comércio entre dois países, decorrem de ") + vm("economias de escala na produção")
                    + az(".")),
        "poucas": ("O H-O supõe " + azb("retornos constantes de escala") + "; a vantagem comparativa vem das "
                   + azb("diferenças de dotação relativa de fatores") + ". Economias de escala são o motor das "
                   "novas teorias do comércio."),
        "destrinchando": [
            "Hipóteses do " + azb("modelo H-O") + ": dois países, dois bens, dois fatores; tecnologia idêntica; "
            "preferências idênticas; " + vd("retornos constantes de escala") + "; concorrência perfeita; fatores "
            "móveis entre setores e imóveis entre países; sem custos de transporte nem reversão de intensidade "
            "fatorial.",
            "Com tudo isso igualado, a única assimetria é a " + vd("dotação relativa") + ": o país rico em capital "
            "tem capital relativamente barato em autarquia e, por isso, vantagem comparativa no bem "
            "capital-intensivo.",
            azb("Economias de escala") + " (retornos crescentes) são a base da " + azb("nova teoria do comércio")
            + " de " + oc("Paul Krugman") + " (fim dos anos 1970, Nobel de 2008): mesmo países idênticos ganham ao "
            "se especializar em variedades diferentes, porque a produção em larga escala reduz o custo médio e "
            "amplia a variedade disponível. Ela explica o " + azb("comércio intraindustrial") + " entre países "
            "ricos parecidos, que o H-O não explica bem.",
            "Distinção útil: no H-O o ganho vem da <b>diferença</b> entre países; na nova teoria, pode existir "
            "comércio vantajoso entre países <b>iguais</b>.",
            vm("Regra-âncora: H-O = dotações + retornos constantes; escala = nova teoria do comércio."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item mantém a moldura certa (H-O, vantagem comparativa) e "
                       "troca só a fonte da vantagem por uma explicação de outra escola. Pista: “economias de "
                       "escala” é incompatível com a hipótese de retornos constantes, que todo manual lista entre as "
                       "premissas do H-O."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Heckscher-Ohlin, as vantagens comparativas decorrem de diferenças na dotação "
            "relativa de fatores entre os países.”</i> → CERTO",
            "<i>“As novas teorias do comércio explicam o comércio intraindustrial por economias de escala e "
            "diferenciação de produtos.”</i> → CERTO",
        ])],
        "reescrita": ("No modelo de Heckscher-Ohlin de comércio internacional, as vantagens comparativas, que levam "
                      "ao comércio entre dois países, decorrem de " + hl("diferenças na dotação relativa de fatores "
                                                                          "de produção entre eles") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "H-O assume retornos constantes e concorrência perfeita; vantagem comparativa só por "
                            "dotação de fatores; economias de escala são das Novas Teorias do Comércio (Krugman), "
                            "que explicam o comércio intraindustrial.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01161-1 (mesma assertiva, Nabuco Pré-TPS/2023)"],
    },
    # ------------------------------------------------------------------ E2-L00643
    {
        "id": "ECO-E2-L00643-1", "fonte_ref": "E2-L00643", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_TC,
        "rotulo_item": "Item",
        "assertiva": ("Uma política de proteção tarifária sobre bens importados em um país relativamente escasso em "
                      "trabalho, segundo a lógica do teorema de Stolper-Samuelson, levará a um aumento do preço "
                      "relativo desses bens e, consequentemente, a uma redução da remuneração real do trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma política de proteção tarifária sobre bens importados em um país relativamente escasso "
                       "em trabalho, segundo a lógica do teorema de Stolper-Samuelson, levará a um aumento do preço "
                       "relativo desses bens e, consequentemente, a ") + vm("uma redução") + az(" da remuneração "
                                                                                                  "real do "
                                                                                                  "trabalho.")),
        "poucas": ("País escasso em trabalho importa bens " + azb("trabalho-intensivos") + ". A tarifa encarece "
                   "esses bens e, por " + azb("Stolper-Samuelson") + ", " + vd("eleva") + " o salário real; quem "
                   "perde é o capital (fator abundante)."),
        "destrinchando": [
            "Passo 1 — padrão de comércio (H-O): o país escasso em trabalho é abundante em capital; exporta o bem "
            "capital-intensivo e " + vd("importa o trabalho-intensivo") + ".",
            "Passo 2 — a tarifa eleva o preço doméstico do importado. A primeira metade do item está certa: o "
            "preço relativo do bem trabalho-intensivo sobe.",
            "Passo 3 — Stolper-Samuelson: preço relativo de um bem ↑ → remuneração real do fator usado "
            "intensivamente nele ↑ (mais que proporcionalmente, pelo efeito ampliação) e a do outro fator ↓. "
            "Logo, " + vd("salário real ↑") + " e " + vd("renda real do capital ↓") + ".",
            "Foi esse o argumento original do artigo de 1941: a proteção pode beneficiar o fator escasso, em "
            "termos reais, mesmo com a perda de bem-estar agregada. Explica por que, em países ricos em capital, "
            "sindicatos tendem a apoiar barreiras a importações trabalho-intensivas.",
            "A tarifa é o espelho da abertura: abrir o comércio favorece o fator abundante; proteger favorece o "
            "fator escasso.",
            vm("Regra-âncora: protege-se o bem intensivo no fator X → o fator X ganha em termos reais."),
        ],
        "dissecando": (cz("[inversão]") + " O raciocínio é montado corretamente até o último elo, e o sinal é "
                       "invertido no fim. A armadilha é a intuição de que “proteção = perda geral”: no agregado sim, "
                       "mas o fator escasso ganha. Pista: o bem protegido usa intensivamente o trabalho."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a tarifa levará à redução da remuneração real do capital.”</i> → CERTO",
            "<i>“…a tarifa reduzirá o preço relativo dos bens importados.”</i> → ERRADO (inversão: a tarifa o "
            "eleva)",
        ])],
        "reescrita": ("Uma política de proteção tarifária sobre bens importados em um país relativamente escasso em "
                      "trabalho, segundo a lógica do teorema de Stolper-Samuelson, levará a um aumento do preço "
                      "relativo desses bens e, consequentemente, a " + hl("um aumento") + " da remuneração real do "
                      "trabalho."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "País escasso em trabalho importa bens trabalho-intensivos; a tarifa eleva seu preço e, "
                            "por Stolper-Samuelson, eleva a remuneração real do trabalho; a do capital cai.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00573-1 (Stolper-Samuelson e fator escasso)"],
    },
    # ------------------------------------------------------------------ E2-L00661
    {
        "id": "ECO-E2-L00661-1", "fonte_ref": "E2-L00661", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_EI,
        "rotulo_item": "Item",
        "assertiva": ("O livre-comércio internacional pode expandir as possibilidades de produção de um país para "
                      "além de sua própria fronteira de possibilidades de consumo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O livre-comércio internacional pode expandir as possibilidades de ") + vm("produção")
                    + az(" de um país para além de sua própria fronteira de possibilidades de ") + vm("consumo")
                    + az(".")),
        "poucas": ("O comércio expande as possibilidades de " + azb("consumo") + " para além da " + azb("FPP")
                   + "; a fronteira de produção, que depende de fatores e tecnologia, não se move. O item inverte "
                   "os termos."),
        "destrinchando": [
            "A " + azb("fronteira de possibilidades de produção") + " (FPP) mostra o máximo que o país produz com "
            "seus fatores e sua tecnologia. Em autarquia, consumo = produção: o país consome em algum ponto da FPP.",
            "Com comércio, o país se " + azb("especializa") + " no bem de vantagem comparativa (ponto P no "
            "gráfico) e troca parte dele aos " + azb("termos de troca") + " mundiais. A linha de troca que passa "
            "por P fica acima da FPP quando o preço mundial difere do preço de autarquia: o país passa a consumir "
            "cestas " + vd("inalcançáveis") + " só com produção doméstica.",
            "No modelo ricardiano, a FPP é uma reta; o ganho é a distância entre ela e a linha de troca. Quanto "
            "mais os termos de troca se afastam do custo de oportunidade doméstico, maior o ganho.",
            "O que desloca a FPP é crescimento: mais fatores (capital, trabalho) ou progresso técnico. O comércio "
            "pode estimular isso indiretamente (difusão de tecnologia, escala), mas o ganho estático do comércio é "
            "de " + vd("consumo") + ", não de capacidade produtiva.",
            vm("Regra-âncora: comércio → consumo além da FPP; a FPP fica onde está."),
        ],
        "grafico_verso": "ECO-E2-L00661-1-V1",
        "dissecando": (cz("[inversão]") + " Troca de lugar entre “produção” e “consumo”: a frase certa existe e "
                       "é famosa, e o item a devolve com os termos permutados. O “pode” dá ar de moderação, mas "
                       "não salva a inversão. Pista: “fronteira de possibilidades de consumo” não é o conceito "
                       "usual; o nome consagrado é FPP."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O livre comércio pode permitir que um país consuma uma cesta de bens fora de sua fronteira de "
            "possibilidades de produção.”</i> → CERTO",
            "<i>“O livre comércio desloca para fora a fronteira de possibilidades de produção do país.”</i> → "
            "ERRADO (confunde ganho de consumo com crescimento)",
        ])],
        "reescrita": ("O livre-comércio internacional pode expandir as possibilidades de " + hl("consumo")
                      + " de um país para além de sua própria fronteira de possibilidades de " + hl("produção")
                      + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "O comércio expande as possibilidades de consumo para além da FPP, pela especialização; "
                            "não expande a fronteira física de produção.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00696
    {
        "id": "ECO-E2-L00696-1", "fonte_ref": "E2-L00696", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("A fronteira de possibilidades de produção (FPP) no modelo ricardiano é côncava, refletindo "
                      "custos de oportunidade crescentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A fronteira de possibilidades de produção (FPP) no modelo ricardiano é ") + vm("côncava")
                    + az(", refletindo custos de oportunidade ") + vm("crescentes") + az(".")),
        "poucas": ("Com um único fator (trabalho) e produtividade " + azb("constante") + ", a FPP ricardiana é uma "
                   + vd("reta") + ": o custo de oportunidade é constante. A concavidade aparece em modelos com dois "
                   "fatores, como o H-O."),
        "destrinchando": [
            "No modelo de " + oc("Ricardo") + ", produzir 1 unidade de x exige a<sub>Lx</sub> horas, e 1 de y, "
            "a<sub>Ly</sub> horas, sempre os mesmos valores. Com L horas: a<sub>Lx</sub>·x + a<sub>Ly</sub>·y = L, "
            "a equação de uma " + vd("reta") + ".",
            "A inclinação, a<sub>Lx</sub>/a<sub>Ly</sub>, é o " + azb("custo de oportunidade") + " de x em "
            "unidades de y e não muda ao longo da fronteira: deslocar uma hora de y para x sempre rende o mesmo.",
            "Consequência: com comércio, o país tende à " + azb("especialização completa") + " (vai a um dos "
            "extremos da reta), o que é uma marca do modelo ricardiano.",
            "A " + azb("FPP côncava") + " (custos crescentes) surge quando os recursos não são igualmente aptos "
            "para os dois bens: em modelos com dois fatores e intensidades diferentes (H-O) ou com fatores "
            "específicos e rendimentos decrescentes. Aí a especialização tende a ser " + vd("incompleta") + ".",
            vm("Regra-âncora: Ricardo → FPP reta, custo constante; dois fatores → FPP côncava, custo crescente."),
        ],
        "grafico_verso": "ECO-E2-L00696-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item cola no modelo ricardiano a FPP “padrão” dos livros de "
                       "introdução, que é côncava. Pista: um fator só, com produtividade fixa, não tem como gerar "
                       "custos crescentes. 🔥 A forma da FPP é a pergunta-relâmpago clássica sobre Ricardo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, a FPP é linear, o que tende a levar à especialização completa com o "
            "comércio.”</i> → CERTO",
            "<i>“No modelo H-O, a FPP é linear, refletindo custos de oportunidade constantes.”</i> → ERRADO "
            "(no H-O ela é côncava)",
        ])],
        "reescrita": ("A fronteira de possibilidades de produção (FPP) no modelo ricardiano é " + hl("linear")
                      + ", refletindo custos de oportunidade " + hl("constantes") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "No ricardiano, trabalho único com produtividade constante → custo de oportunidade "
                            "constante → FPP linear; a concavidade é típica do H-O.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00697
    {
        "id": "ECO-E2-L00697-1", "fonte_ref": "E2-L00697", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("O Teorema de Heckscher-Ohlin assume tecnologias e preferências idênticas, enquanto o modelo "
                      "Ricardiano explica o comércio internacional com base nas diferenças de tecnologia e "
                      "produtividade do trabalho entre países com preferências idênticas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Teorema de Heckscher-Ohlin assume tecnologias e preferências <u>idênticas</u>, enquanto o "
                      "modelo Ricardiano explica o comércio internacional com base nas <u>diferenças de tecnologia "
                      "e produtividade do trabalho</u> entre países com <u>preferências idênticas</u>."),
        "poucas": ("Nos dois modelos as " + azb("preferências") + " são supostas iguais; o que muda é a fonte da "
                   "vantagem: " + azb("tecnologia") + " em Ricardo, " + azb("dotação de fatores") + " em H-O."),
        "destrinchando": [
            "Por que supor preferências idênticas? Para que o comércio não seja explicado pela demanda (um país "
            "gostar mais de um bem). Fixada a demanda, a explicação tem de vir da " + vd("oferta") + ".",
            "Em " + oc("Ricardo") + ", a oferta difere pela " + vd("tecnologia") + ": requisitos de trabalho por "
            "unidade diferentes entre países (produtividade do trabalho). O preço relativo de autarquia reflete "
            "esses requisitos.",
            "Em " + oc("Heckscher") + "-" + oc("Ohlin") + ", a tecnologia também é igual; a oferta difere pela "
            + vd("abundância relativa de fatores") + ". O país rico em capital tem capital barato em autarquia e "
            "produz relativamente mais barato o bem capital-intensivo.",
            "Os dois são modelos de " + azb("vantagem comparativa") + " com concorrência perfeita e retornos "
            "constantes. Diferenças relevantes: Ricardo tem um fator, FPP linear e especialização completa; H-O "
            "tem dois fatores, FPP côncava, especialização em geral incompleta e efeitos distributivos "
            "(Stolper-Samuelson).",
            vm("Regra-âncora: preferências iguais nos dois; tecnologia diferente só em Ricardo."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item longo, com três afirmações empilhadas, todas corretas. O "
                       "risco é desconfiar das “preferências idênticas” em Ricardo. 🔥 A versão ERRADA mais comum "
                       "diz que em Ricardo “tecnologia <b>e preferências</b> diferem”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Ricardo, a tecnologia e as preferências diferem entre os países.”</i> → ERRADO "
            "(preferências são idênticas)",
            "<i>“O modelo H-O explica o comércio por diferenças tecnológicas entre países com a mesma dotação "
            "de fatores.”</i> → ERRADO (inversão das hipóteses)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "H-O supõe tecnologias e preferências idênticas e explica o comércio pela dotação; "
                            "Ricardo atribui o comércio às diferenças tecnológicas, com preferências idênticas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01022-1 (versão ERRADA: preferências diferentes em Ricardo), "
                    "ECO-E2-L00571-1"],
    },
    # ------------------------------------------------------------------ E2-L00698
    {
        "id": "ECO-E2-L00698-1", "fonte_ref": "E2-L00698", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o Teorema de Stolper-Samuelson, a abertura comercial em um país abundante em "
                      "trabalho e escasso em capital tende a reduzir o salário real e aumentar a remuneração real "
                      "do capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o Teorema de Stolper-Samuelson, a abertura comercial em um país abundante em "
                       "trabalho e escasso em capital tende a ") + vm("reduzir") + az(" o salário real e ")
                    + vm("aumentar") + az(" a remuneração real do capital.")),
        "poucas": ("O país abundante em trabalho exporta bens " + azb("trabalho-intensivos") + "; a abertura "
                   "eleva seu preço relativo e, com ele, o " + vd("salário real") + ". O capital, escasso, perde."),
        "destrinchando": [
            "Pelo " + azb("teorema de H-O") + ", o país abundante em trabalho tem vantagem comparativa no bem "
            "trabalho-intensivo (têxteis, calçados, montagem). Ao abrir-se, exporta esse bem, cujo preço relativo "
            "sobe ao nível mundial.",
            "Pelo " + azb("teorema de Stolper-Samuelson") + ", a alta do preço relativo do bem trabalho-intensivo "
            "eleva a remuneração real do trabalho e reduz a do capital, em termos de ambos os bens (efeito "
            "ampliação).",
            "Intuição pela demanda de fatores: o setor que cresce (exportador) usa muito trabalho; o que encolhe "
            "(concorrente das importações) libera relativamente mais capital do que o setor exportador absorve. "
            "Para manter o pleno emprego, o salário relativo " + vd("sobe") + " e a renda do capital " + vd("cai")
            + ".",
            "Leitura para países em desenvolvimento: o modelo prevê que a liberalização reduz a desigualdade "
            "salarial em países ricos em mão de obra pouco qualificada. A evidência das aberturas latino-americanas "
            "dos anos 1990, porém, mostrou com frequência o contrário (prêmio de qualificação maior), um dos "
            "limites empíricos do modelo.",
            vm("Regra-âncora: abertura → fator abundante ganha; fator escasso perde."),
        ],
        "dissecando": (cz("[inversão]") + " Os dois sinais foram trocados ao mesmo tempo, o que mantém a frase "
                       "internamente coerente e engana quem só confere a lógica. Pista: identifique o fator "
                       "abundante (trabalho) e aplique “abundante ganha”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a abertura comercial em um país abundante em capital tende a reduzir o salário real.”</i> → CERTO",
            "<i>“…a abertura comercial eleva a remuneração de todos os fatores, pois amplia o bem-estar "
            "agregado.”</i> → ERRADO (generalização: o fator escasso perde)",
        ])],
        "reescrita": ("De acordo com o Teorema de Stolper-Samuelson, a abertura comercial em um país abundante em "
                      "trabalho e escasso em capital tende a " + hl("aumentar") + " o salário real e "
                      + hl("reduzir") + " a remuneração real do capital."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "A abertura eleva a remuneração real do fator abundante e reduz a do escasso; país "
                            "abundante em trabalho exporta bens trabalho-intensivos e o salário real sobe.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00573-1, ECO-E2-L01470-1 (Stolper-Samuelson e abertura)"],
    },
    # ------------------------------------------------------------------ E2-L00699
    {
        "id": "ECO-E2-L00699-1", "fonte_ref": "E2-L00699", "destino": "73", "subtema": H2["leo"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("O Paradoxo de Leontief refere-se à constatação empírica de que os Estados Unidos, país "
                      "abundante em capital, apresentava importações capital-intensivas relativamente às suas "
                      "exportações, contrariando as previsões iniciais do modelo Heckscher-Ohlin."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Paradoxo de Leontief refere-se à constatação empírica de que os Estados Unidos, país "
                      "abundante em capital, apresentava <u>importações capital-intensivas relativamente às suas "
                      "exportações</u>, contrariando as previsões iniciais do modelo Heckscher-Ohlin."),
        "poucas": ("Pelo H-O, os EUA, ricos em capital, deveriam exportar bens capital-intensivos. " + oc("Leontief")
                   + " encontrou o oposto: " + vd("importações mais capital-intensivas que as exportações") + "."),
        "destrinchando": [
            oc("Wassily Leontief") + " (estudo publicado em 1953, com a matriz insumo-produto dos EUA de 1947) "
            "calculou o capital e o trabalho necessários para produzir US$ 1 milhão de exportações e de "
            "substitutos domésticos das importações. A razão " + vd("K/L das importações") + " superou a das "
            + vd("exportações") + ".",
            "Como os EUA eram o país mais abundante em capital do mundo, o resultado contrariava o "
            + azb("teorema de H-O") + ". Daí “paradoxo”. Estudos posteriores com dados de 1962 (" + oc("Baldwin")
            + ", 1971) repetiram o padrão.",
            "Explicações propostas: " + azb("capital humano") + " (as exportações americanas usavam trabalho mais "
            "qualificado, com mais engenheiros e cientistas); o próprio Leontief sugeriu que o trabalhador "
            "americano era mais produtivo, o que tornaria os EUA abundantes em trabalho “efetivo”; recursos "
            "naturais complementares ao capital nas importações; estrutura de proteção tarifária; e diferenças "
            "de tecnologia entre países.",
            "Legado: o paradoxo estimulou versões do H-O com mais fatores (capital humano, terra) e abriu espaço "
            "para explicações tecnológicas (ciclo do produto) e para a nova teoria do comércio.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição correta do paradoxo, na ordem certa (importações "
                       "capital-intensivas). 🔥 A banca gera o ERRADO invertendo a direção: “exportações mais "
                       "intensivas em capital que as importações”, que é o que a teoria previa, não o que Leontief "
                       "achou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O paradoxo de Leontief revelou que as exportações dos EUA eram mais intensivas em capital do que "
            "suas importações.”</i> → ERRADO (inversão: isso confirmaria o H-O)",
            "<i>“Uma das explicações do paradoxo é a maior intensidade de capital humano das exportações "
            "americanas.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Leontief (1953): EUA, abundantes em capital, exportavam bens trabalho-intensivos e "
                            "importavam capital-intensivos, contradizendo o H-O.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01507-1 (versão ERRADA com a direção invertida)"],
    },
    # ------------------------------------------------------------------ E2-L00845
    {
        "id": "ECO-E2-L00845-1", "fonte_ref": "E2-L00845", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_DC,
        "rotulo_item": "Item",
        "assertiva": ("Nas teorias neoclássicas de comércio internacional, as vantagens comparativas se originam de "
                      "diferenças tecnológicas, culminando em diferenças de produtividade do trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nas teorias neoclássicas de comércio internacional, as vantagens comparativas se originam "
                       "de ") + vm("diferenças tecnológicas, culminando em diferenças de produtividade do trabalho")
                    + az(".")),
        "poucas": ("Diferença de tecnologia e de produtividade do trabalho é a fonte " + azb("clássica")
                   + " (Ricardo). Na teoria " + azb("neoclássica") + " (H-O-S), a vantagem vem das "
                   + vd("dotações relativas de fatores") + ", com tecnologia igual."),
        "destrinchando": [
            "A " + azb("teoria neoclássica do comércio") + " tem como núcleo o modelo de " + oc("Heckscher")
            + " e " + oc("Ohlin") + ", formalizado por " + oc("Samuelson") + " (por isso “H-O-S”). Hipótese-chave: "
            "tecnologia e preferências " + vd("idênticas") + " entre países.",
            "Se a tecnologia é igual, a vantagem comparativa só pode vir da diferença de " + vd("dotação") + ": o "
            "fator relativamente abundante é relativamente barato em autarquia, e o bem que o usa intensivamente "
            "sai mais barato. O país exporta esse bem.",
            "A descrição do item (“diferenças tecnológicas → produtividade do trabalho”) é a do "
            + azb("modelo ricardiano") + ", núcleo da teoria " + azb("clássica") + ", com um único fator.",
            "Por que “neoclássica”? Porque abandona o valor-trabalho dos clássicos e usa a teoria marginalista "
            "de preços dos fatores, com dois ou mais fatores substituíveis entre si.",
            vm("Regra-âncora: clássica = tecnologia; neoclássica = dotação de fatores."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item pega a definição certa da teoria clássica e a cola no "
                       "rótulo “neoclássicas”. Pista: “produtividade do trabalho” pressupõe um só fator, o que já "
                       "denuncia Ricardo. 🔥 A mesma frase com “clássicas” é CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nas teorias clássicas de comércio internacional, as vantagens comparativas se originam de "
            "diferenças tecnológicas, que geram diferenças de produtividade do trabalho.”</i> → CERTO",
            "<i>“Nas teorias neoclássicas, as vantagens comparativas se originam de diferenças nas dotações "
            "relativas de fatores.”</i> → CERTO",
        ])],
        "reescrita": ("Nas teorias neoclássicas de comércio internacional, as vantagens comparativas se originam "
                      "de " + hl("diferenças na dotação relativa de fatores de produção entre os países") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Teoria neoclássica (H-O-S): vantagens comparativas por diferenças de dotação, com "
                            "tecnologias e preferências semelhantes; diferenças tecnológicas explicam o modelo "
                            "ricardiano, clássico.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00641-1, ECO-E2-L01160-1 (versão CERTO da mesma distinção)"],
    },
    # ------------------------------------------------------------------ E2-L00846
    {
        "id": "ECO-E2-L00846-1", "fonte_ref": "E2-L00846", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_DC,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Heckscher-Ohlin, múltiplos fatores de produção podem deslocar-se entre os "
                      "setores e entre os países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Heckscher-Ohlin, múltiplos fatores de produção podem deslocar-se entre os "
                       "setores ") + vm("e entre os países") + az(".")),
        "poucas": ("No H-O, os fatores são " + azb("móveis entre setores") + " dentro de cada país, mas "
                   + vm("imóveis entre países") + ": o que cruza a fronteira são os bens."),
        "destrinchando": [
            "A " + azb("mobilidade intersetorial") + " (capital e trabalho migram livremente entre a produção de "
            "um bem e de outro) é o que garante que cada fator tenha uma única remuneração dentro do país e que a "
            "economia esteja sobre a FPP.",
            "A " + azb("imobilidade internacional") + " é o que dá sentido ao modelo: se capital e trabalho "
            "pudessem migrar, as diferenças de dotação desapareceriam e não haveria base para o comércio de bens. "
            "No H-O, o comércio de bens " + vd("substitui") + " o movimento dos fatores: exportar bens "
            "trabalho-intensivos equivale a exportar serviços de trabalho.",
            "Disso nasce o " + azb("teorema da equalização dos preços dos fatores") + " (" + oc("Samuelson")
            + "): mesmo sem migração, o comércio tende a igualar salários e rendas do capital entre os países. "
            + oc("Mundell") + " (1957) mostrou a simetria: a mobilidade de fatores, sem comércio de bens, levaria "
            "ao mesmo resultado.",
            "Contraste: no " + azb("modelo de fatores específicos") + " (Ricardo-Viner), pelo menos um fator é "
            "imóvel também entre setores, o que muda os efeitos distributivos no curto prazo.",
        ],
        "dissecando": (cz("[meia-verdade]") + " A primeira metade (entre os setores) é verdadeira; o erro foi "
                       "acrescentado com um simples “e entre os países”. Pista: se os fatores cruzassem fronteiras, "
                       "as dotações se igualariam e o próprio motivo do comércio no H-O sumiria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Heckscher-Ohlin, os fatores de produção são móveis entre setores, mas imóveis entre "
            "países.”</i> → CERTO",
            "<i>“No modelo de fatores específicos, todos os fatores são perfeitamente móveis entre setores.”</i> "
            "→ ERRADO (há fator específico, imóvel)",
        ])],
        "reescrita": ("No modelo de Heckscher-Ohlin, múltiplos fatores de produção podem deslocar-se entre os "
                      "setores" + hl(", mas não entre os países") + "."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": "Um dos pressupostos do H-O é a imobilidade dos fatores entre países; são móveis entre "
                            "setores.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “Hecksher-Ohlin” na fonte corrigido para “Heckscher-Ohlin”"],
    },
    # ------------------------------------------------------------------ E2-L00967
    {
        "id": "ECO-E2-L00967-1", "fonte_ref": "E2-L00967", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AB,
        "aviso_frente": AVISO_AB,
        "excerto_tabela": TAB_AB,
        "rotulo_item": "Item",
        "assertiva": ("Na situação 1, mesmo que o país A seja absolutamente mais eficiente na produção de ambos os "
                      "bens, haverá ganhos mútuos na troca entre os países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Na situação 1, mesmo que o país A seja <u>absolutamente</u> mais eficiente na produção de "
                      "ambos os bens, haverá <u>ganhos mútuos</u> na troca entre os países."),
        "poucas": ("Na situação 1 os custos de oportunidade diferem (" + vd("1x = 2y em A") + "; " + vd("1x = 6y em B")
                   + "): A tem " + azb("vantagem comparativa") + " em x e B em y, o que abre espaço para ganhos "
                   "de troca, apesar da vantagem absoluta de A nos dois bens."),
        "condicionais": [("⚠️ Gabarito contestável",
            "o CERTO segue a lição geral de Ricardo. Mas o próprio comando diz que B não consegue suprir o "
            "mercado mundial: A continua produzindo os dois bens, e o preço mundial fica no seu preço de autarquia "
            "(" + vd("1x = 2y") + "). Nesse caso, B fica com " + vm("todo o ganho") + " e o ganho de A é nulo (A "
            "não perde, mas também não ganha). A leitura mais defensável, à luz da premissa do país grande, seria "
            "ERRADO para “ganhos mútuos”; mantido o gabarito CERTO da fonte.")],
        "destrinchando": [
            azb("Vantagem absoluta") + " (" + oc("Smith") + "): quem produz mais por trabalhador. A produz 4 x "
            "contra 1 de B, e 8 y contra 6: vantagem absoluta de A nos dois bens.",
            azb("Vantagem comparativa") + " (" + oc("Ricardo") + "): menor custo de oportunidade. Em A, 1 x custa "
            "8/4 = " + vd("2 y") + "; em B, 1 x custa 6/1 = " + vd("6 y") + ". A tem vantagem comparativa em "
            + vd("x") + "; B, em " + vd("y") + " (1 y custa a B só 1/6 de x, contra 1/2 em A).",
            "Para os dois ganharem, os " + azb("termos de troca") + " precisam ficar entre os preços de autarquia: "
            + vd("2 y < preço de 1 x < 6 y") + ". A qualquer preço estritamente dentro do intervalo, cada país "
            "obtém pela troca mais do que obteria produzindo internamente.",
            "O detalhe do país grande: se B é pequeno demais para abastecer o mundo, A não se especializa "
            "completamente e o preço internacional coincide com o preço de autarquia de A. Na lição de "
            + oc("Krugman") + " e " + oc("Obstfeld") + ", é a “importância de ser desimportante”: o país pequeno "
            "capta os ganhos.",
            vm("Regra-âncora: vantagem absoluta em tudo não impede o comércio; o que importa é o custo de "
               "oportunidade."),
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " O “mesmo que” convida a pensar que o país mais "
                       "eficiente em tudo não precisaria comerciar: é a intuição que Ricardo derrubou. O ponto "
                       "frágil é “mútuos”, que a premissa do país grande torna discutível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na situação 1, com termos de troca de 1x = 7y, ambos os países ganham com o comércio.”</i> → "
            "ERRADO (fora do intervalo 2y–6y: B perderia)",
            "<i>“Na situação 1, o país B tem vantagem comparativa na produção do bem y.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["mesmo que"], "dificuldade": 2,
        "comentario_fonte": "A tem vantagem absoluta em ambos e vantagem comparativa em x (4/8 contra 1/6 de B); "
                            "há ganhos mútuos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_160,
        "alertas": [ALERTA_160,
                    "contestavel: com o país A grande, o preço mundial fica na autarquia de A e só B ganha; "
                    "“ganhos mútuos” é discutível — gabarito CERTO da fonte mantido"],
    },
    # ------------------------------------------------------------------ E2-L00968
    {
        "id": "ECO-E2-L00968-1", "fonte_ref": "E2-L00968", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AB,
        "aviso_frente": AVISO_AB,
        "excerto_tabela": TAB_AB,
        "rotulo_item": "Item",
        "assertiva": "O país maior, devido a sua dimensão e seu poder econômico, terá todos os benefícios do comércio.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O país maior, devido a sua dimensão e seu poder econômico, ")
                    + vm("terá todos os benefícios do comércio") + az(".")),
        "poucas": ("É o contrário: o país grande " + azb("impõe seu preço de autarquia") + " ao mercado mundial e "
                   "não ganha nada; " + vm("todo o ganho fica com o país pequeno") + ", que troca a um preço muito "
                   "diferente do seu."),
        "destrinchando": [
            "O ganho de comércio de um país depende da distância entre os " + azb("termos de troca")
            + " internacionais e o seu preço relativo de autarquia. Quanto mais o preço mundial se afasta do "
            "preço doméstico, maior o ganho.",
            "Na situação 1, A (grande) tem autarquia de " + vd("1x = 2y") + "; B (pequeno), de " + vd("1x = 6y")
            + ". Como B não consegue abastecer o mundo nem de y, A continua produzindo os dois bens, e o preço "
            "mundial fica em " + vd("1x = 2y") + ", o de A.",
            "Para A, nada muda: troca ao mesmo preço que obtinha produzindo sozinho, ganho " + vd("nulo")
            + ". Para B, que antes “pagava” 6 y por x, passa a pagar 2 y: especializa-se em y e obtém "
            "um ganho grande.",
            "É a lição de " + oc("Krugman") + " e " + oc("Obstfeld") + " sobre a “importância de ser "
            "desimportante”: no modelo ricardiano, o país pequeno tende a captar os ganhos do comércio. Poder "
            "econômico não entra no modelo, que supõe concorrência perfeita e países tomadores de preço.",
            vm("Regra-âncora: país grande fixa o preço e ganha pouco ou nada; país pequeno capta o ganho."),
        ],
        "dissecando": (cz("[inversão · juízo indevido]") + " O item apela ao senso comum (“o mais forte leva "
                       "tudo”) e atribui ao tamanho um poder de barganha que o modelo não tem. Pista: no modelo "
                       "ricardiano, quem mais ganha é quem troca a preços mais distantes dos seus."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o país A for muito maior que B, os termos de troca tenderão a coincidir com o preço relativo "
            "de autarquia de A.”</i> → CERTO",
            "<i>“O país menor nada ganha com o comércio, pois não altera os preços mundiais.”</i> → ERRADO "
            "(inversão: ele capta os ganhos)",
        ])],
        "reescrita": ("O país maior, devido a sua dimensão e seu poder econômico, " + hl("imporá ao mercado mundial "
                      "o seu preço relativo de autarquia e não terá ganhos com o comércio, que ficarão todos com o "
                      "país menor") + "."),
        "tipo_erro": ["INVERSAO", "JUIZO_INDEVIDO"], "moduladores": ["todos"], "dificuldade": 2,
        "comentario_fonte": "Os ganhos do comércio são mútuos com especialização por vantagem comparativa, "
                            "independentemente do tamanho e do poder econômico dos países.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": FIG_160,
        "alertas": [ALERTA_160,
                    "qualidade_fonte: o comentário de origem diz que os ganhos são mútuos “independentemente do "
                    "tamanho”; com a premissa do enunciado, o ganho do país grande é nulo e o pequeno capta tudo"],
    },
    # ------------------------------------------------------------------ E2-L00969
    {
        "id": "ECO-E2-L00969-1", "fonte_ref": "E2-L00969", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AB,
        "aviso_frente": AVISO_AB,
        "excerto_tabela": TAB_AB,
        "rotulo_item": "Item",
        "assertiva": ("Na situação 2, o país A possui vantagem comparativa na produção do bem x, enquanto o país B "
                      "possui vantagem comparativa na produção do bem y."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na situação 2, ") + vm("o país A possui vantagem comparativa na produção do bem x, enquanto "
                                               "o país B possui vantagem comparativa na produção do bem y")
                    + az(".")),
        "poucas": ("Na situação 2, as produtividades de B são exatamente " + vd("1/4") + " das de A nos dois bens: "
                   "o custo de oportunidade é " + vd("1x = 2y") + " em ambos. Sem diferença, " + vm("ninguém")
                   + " tem vantagem comparativa."),
        "destrinchando": [
            "Custos de oportunidade na situação 2: A → 1 x custa 8/4 = " + vd("2 y") + "; B → 1 x custa 2/1 = "
            + vd("2 y") + ". Pelo outro lado, 1 y custa " + vd("0,5 x") + " nos dois países.",
            azb("Vantagem comparativa") + " é conceito relativo: existe só quando os custos de oportunidade "
            "<b>diferem</b>. Com custos iguais, os preços de autarquia coincidem e não há preço internacional que "
            "beneficie a troca.",
            "A segue com " + azb("vantagem absoluta") + " nos dois bens (4 > 1 e 8 > 2), mas isso é irrelevante "
            "para o comércio ricardiano: A é “4 vezes melhor” em tudo, na mesma proporção.",
            "Contraste com a situação 1: lá B produzia 6 y (e não 2), o que tornava y relativamente barato em B "
            "(1x = 6y) e criava vantagem comparativa de B em y e de A em x.",
            vm("Regra-âncora: produtividades proporcionais → custos de oportunidade iguais → sem vantagem "
               "comparativa."),
        ],
        "dissecando": (cz("[extrapolação · troca de conceito]") + " O item transporta para a situação 2 o padrão "
                       "de especialização que valia na situação 1. Pista: dividir as linhas da tabela (4/8 e 1/2) "
                       "e perceber que as razões são iguais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na situação 2, o país A possui vantagem absoluta na produção de ambos os bens.”</i> → CERTO",
            "<i>“Na situação 1, o país A possui vantagem comparativa na produção do bem x, e o país B, na do bem "
            "y.”</i> → CERTO",
        ])],
        "reescrita": ("Na situação 2, " + hl("nenhum dos países possui vantagem comparativa, pois os custos de "
                                             "oportunidade são iguais (1x = 2y em A e em B)") + "."),
        "tipo_erro": ["EXTRAPOLACAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Na situação 2, ambos têm a mesma produtividade relativa (4/8 = 1/2): sem ganhos de "
                            "comércio por vantagem comparativa.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_160,
        "alertas": [ALERTA_160],
    },
    # ------------------------------------------------------------------ E2-L00970
    {
        "id": "ECO-E2-L00970-1", "fonte_ref": "E2-L00970", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AB,
        "aviso_frente": AVISO_AB,
        "excerto_tabela": TAB_AB,
        "rotulo_item": "Item",
        "assertiva": ("Na situação 2, não há bases em termos de vantagem comparativa para o comércio mutuamente "
                      "benéfico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na situação 2, <u>não há</u> bases em termos de vantagem comparativa para o comércio "
                      "mutuamente benéfico."),
        "poucas": ("Na situação 2, os " + azb("custos de oportunidade são iguais") + " (" + vd("1x = 2y")
                   + " em A e em B): os preços de autarquia coincidem e não há termo de troca que melhore a "
                   "situação de algum país."),
        "destrinchando": [
            "A produz 4 x ou 8 y; B produz 1 x ou 2 y por trabalhador. As produtividades de B são " + vd("1/4")
            + " das de A em <b>ambos</b> os bens: a desvantagem de B é uniforme.",
            "Custo de oportunidade de x: 8/4 = 2 y em A; 2/1 = 2 y em B. De y: 0,5 x nos dois. O preço relativo de "
            "autarquia é o mesmo, " + vd("1x = 2y") + ", nos dois países.",
            "O ganho de comércio ricardiano nasce de trocar a um preço diferente do de autarquia. Se os dois países "
            "já têm o mesmo preço, qualquer termo de troca prejudicaria um deles; ao preço comum, ninguém ganha. "
            "Não há incentivo à " + azb("especialização") + ".",
            azb("Vantagem absoluta") + " de A nos dois bens não basta: é a lição central de " + oc("Ricardo")
            + " (1817). O que gera comércio é a diferença de produtividade " + vd("relativa") + ".",
            "O tamanho dos países, citado no comando, só importaria para definir quem fica com os ganhos se "
            "houvesse base para o comércio; aqui ela não existe.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item de conta: basta comparar as razões x/y das duas "
                       "linhas. O risco é marcar ERRADO por reflexo (“Ricardo diz que sempre há ganho”) ou "
                       "confundir com a vantagem absoluta de A."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na situação 2, como A tem vantagem absoluta nos dois bens, deve se especializar em ambos e "
            "exportá-los para B.”</i> → ERRADO (vantagem absoluta não gera comércio)",
            "<i>“Na situação 1, há bases para o comércio mutuamente benéfico, desde que 1 x se troque por mais de "
            "2 e menos de 6 y.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Situação 2: A 4x/8y, B 1x/2y; custos de oportunidade idênticos (2y por x; 0,5x por y); "
                            "sem vantagem comparativa e sem base para comércio benéfico; A tem vantagem absoluta, "
                            "irrelevante; o tamanho importaria só para o preço mundial.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 160", "tipo_fonte": "TEXTO", "lado": "frente",
                           "acao": "transcrita_html (tabela aninhada reconstruída pelos números do comentário)"},
                          {"ref": "IMAGEM 161", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 162", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [ALERTA_160],
    },
    # ------------------------------------------------------------------ E2-L00974
    {
        "id": "ECO-E2-L00974-1", "fonte_ref": "E2-L00974", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria das vantagens comparativas, nas versões de Heckscher-Ohlin e Samuelson, "
                      "quando um país em desenvolvimento adota um programa radical de liberalização comercial, "
                      "caracterizado pela redução linear de todas as tarifas de importação de mercadorias, o efeito "
                      "será o aumento dos salários relativos nos setores produtores dos bens, que utilizam "
                      "intensivamente o fator de produção escasso do país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a teoria das vantagens comparativas, nas versões de Heckscher-Ohlin e "
                       "Samuelson, quando um país em desenvolvimento adota um programa radical de liberalização "
                       "comercial, caracterizado pela redução linear de todas as tarifas de importação de "
                       "mercadorias, o efeito será o aumento ")
                    + vm("dos salários relativos nos setores produtores dos bens, que utilizam intensivamente o "
                         "fator de produção escasso do país") + az(".")),
        "poucas": ("A liberalização encarece relativamente o bem " + azb("exportado") + ", intensivo no fator "
                   + azb("abundante") + ", e eleva a remuneração desse fator. O fator escasso perde; e, com fatores "
                   "móveis, não há salários diferentes por setor."),
        "destrinchando": [
            "Cadeia H-O-S: tarifas caem → o bem importado (intensivo no fator " + vd("escasso") + ") fica mais "
            "barato internamente → seu setor encolhe; o setor exportador (intensivo no fator " + vd("abundante")
            + ") se expande.",
            "Pelo " + azb("teorema de Stolper-Samuelson") + ", a queda do preço relativo do bem importado reduz a "
            "remuneração real do fator escasso e eleva a do abundante. Num país em desenvolvimento típico, "
            "abundante em trabalho pouco qualificado, o salário desse trabalho " + vd("sobe") + " e a renda do "
            "capital (escasso) " + vd("cai") + ".",
            "Segundo erro, mais sutil: no H-O os fatores são " + azb("perfeitamente móveis entre setores") + ". "
            "Não existem “salários dos setores” que usam o fator escasso: há um único salário na economia. O que "
            "muda é a remuneração de cada <b>fator</b>, não de cada setor.",
            "Diferença para o " + azb("modelo de fatores específicos") + " (curto prazo): com fatores presos ao "
            "setor, os donos do fator específico do setor importador perdem e os do exportador ganham. O H-O "
            "descreve o longo prazo.",
            vm("Regra-âncora: liberalização → fator abundante ganha; fator escasso perde."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item embrulha a inversão (fator escasso ganharia) "
                       "num enunciado longo e técnico (“redução linear de todas as tarifas”) e ainda fala em salário "
                       "por setor, conceito estranho ao H-O. Pista: “escasso” ao lado de “aumento”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o efeito será o aumento da remuneração real do fator de produção abundante do país.”</i> → CERTO",
            "<i>“…a liberalização elevará o preço relativo dos bens importáveis.”</i> → ERRADO (inversão: ele cai)",
        ])],
        "reescrita": ("De acordo com a teoria das vantagens comparativas, nas versões de Heckscher-Ohlin e Samuelson, "
                      "quando um país em desenvolvimento adota um programa radical de liberalização comercial, "
                      "caracterizado pela redução linear de todas as tarifas de importação de mercadorias, "
                      "o efeito será o aumento " + hl("da remuneração real do fator de produção abundante do "
                                                         "país, usado intensivamente nos bens exportados") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["todas"], "dificuldade": 2,
        "comentario_fonte": "A liberalização eleva a demanda e o preço relativo do bem exportado, intensivo no fator "
                            "abundante, cuja remuneração relativa e absoluta sobe; com fatores móveis, não há "
                            "remunerações diferentes do mesmo fator em setores distintos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00573-1, ECO-E2-L00698-1 (Stolper-Samuelson e abertura)"],
    },
    # ------------------------------------------------------------------ E2-L01022
    {
        "id": "ECO-E2-L01022-1", "fonte_ref": "E2-L01022", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Heckscher-Ohlin, pressupõe-se a igualdade entre a tecnologia e as preferências "
                      "dos consumidores entre os países. Já no modelo de Ricardo a tecnologia e as preferências "
                      "diferem entre os países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Heckscher-Ohlin, pressupõe-se a igualdade entre a tecnologia e as preferências "
                       "dos consumidores entre os países. Já no modelo de Ricardo a tecnologia ")
                    + vm("e as preferências diferem") + az(" entre os países.")),
        "poucas": ("Em " + azb("Ricardo") + " só a " + vd("tecnologia") + " difere; as " + azb("preferências")
                   + " são supostas idênticas, como no H-O. A primeira frase está certa; o erro está nas "
                   "preferências da segunda."),
        "destrinchando": [
            "Os dois modelos clássicos de vantagem comparativa explicam o comércio pelo " + vd("lado da oferta")
            + ". Para isolar esse canal, ambos supõem preferências iguais entre países: se cada país quisesse "
            "bens diferentes, o comércio poderia ser explicado pela demanda, e o modelo perderia o foco.",
            "Em " + oc("Ricardo") + ", a assimetria é a " + vd("produtividade do trabalho") + " (tecnologia); em "
            + oc("Heckscher") + "-" + oc("Ohlin") + ", a " + vd("dotação relativa de fatores") + ", com tecnologia "
            "igual.",
            "Na prática, as preferências entram no modelo ricardiano só para fechar o equilíbrio mundial (definir "
            "os termos de troca dentro do intervalo dos custos de oportunidade), e isso se faz com uma demanda "
            "mundial comum aos dois países.",
            "Quadro-resumo: tecnologia → diferente em Ricardo, igual em H-O; preferências → iguais nos dois; "
            "dotações → irrelevantes em Ricardo (um fator), decisivas em H-O.",
        ],
        "dissecando": (cz("[meia-verdade]") + " A primeira frase é perfeita e dá confiança; o erro foi enxertado na "
                       "segunda com “e as preferências”. Pista: se as preferências também diferissem em Ricardo, "
                       "haveria duas causas de comércio, e o modelo ricardiano é famoso por ter uma só."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Ricardo, a tecnologia difere entre os países, enquanto as preferências são "
            "idênticas.”</i> → CERTO",
            "<i>“No modelo de Heckscher-Ohlin, a tecnologia difere entre os países, e as dotações são "
            "idênticas.”</i> → ERRADO (inversão das hipóteses)",
        ])],
        "reescrita": ("No modelo de Heckscher-Ohlin, pressupõe-se a igualdade entre a tecnologia e as preferências "
                      "dos consumidores entre os países. Já no modelo de Ricardo a tecnologia " + hl("difere")
                      + " entre os países" + hl(", mas as preferências são idênticas") + "."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "H-O: tecnologia e preferências idênticas; diferenças de dotação explicam o comércio. "
                            "Ricardo: preferências idênticas, tecnologia diferente.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00697-1 (versão CERTO), ECO-E2-L00571-1"],
    },
    # ------------------------------------------------------------------ E2-L01023
    {
        "id": "ECO-E2-L01023-1", "fonte_ref": "E2-L01023", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Ambos os modelos Heckscher-Ohlin e Ricardiano assumem competição perfeita nos mercados de bens "
                      "e de fatores, retornos constantes de escala e permitem explicar o comércio utilizando o "
                      "conceito de vantagens comparativas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ambos os modelos Heckscher-Ohlin e Ricardiano assumem <u>competição perfeita</u> nos mercados "
                      "de bens e de fatores, <u>retornos constantes de escala</u> e permitem explicar o comércio "
                      "utilizando o conceito de <u>vantagens comparativas</u>."),
        "poucas": ("São as hipóteses comuns aos dois modelos “tradicionais”: " + azb("concorrência perfeita")
                   + ", " + azb("retornos constantes") + " e comércio por " + azb("vantagem comparativa")
                   + ". Muda só a fonte da vantagem."),
        "destrinchando": [
            "Pontos em comum: mercados competitivos (preço = custo, sem lucros extraordinários), retornos "
            "constantes de escala (dobrar insumos dobra o produto), pleno emprego, sem custos de transporte, e "
            "comércio explicado por diferenças de custo de oportunidade entre países.",
            "Diferenças: " + oc("Ricardo") + " usa um fator (trabalho) e explica a vantagem pela "
            + vd("tecnologia") + "; H-O usa dois fatores, tecnologia idêntica, e explica pela " + vd("dotação")
            + ". Em Ricardo a FPP é linear; em H-O, côncava.",
            "Essas hipóteses são justamente as que a " + azb("nova teoria do comércio") + " (" + oc("Krugman")
            + ") relaxa: com " + vd("retornos crescentes") + " e " + vd("concorrência monopolística") + ", há "
            "comércio vantajoso mesmo entre países idênticos, e o padrão de comércio passa a ser intraindustrial.",
            "Detalhe de redação: “mercados de fatores” em Ricardo se reduz ao mercado de trabalho, competitivo, "
            "com salário igual ao valor do produto marginal (constante).",
        ],
        "dissecando": (cz("[literalidade]") + " Lista de hipóteses comuns, sem modulador perigoso. O risco é "
                       "achar que H-O teria retornos decrescentes de escala (confusão com rendimentos marginais "
                       "decrescentes de cada fator, que de fato existem no H-O)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ambos os modelos assumem retornos crescentes de escala e concorrência monopolística.”</i> → "
            "ERRADO (essas são hipóteses da nova teoria do comércio)",
            "<i>“No modelo H-O, cada fator tem produto marginal decrescente, embora a função tenha retornos "
            "constantes de escala.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["ambos"], "dificuldade": 1,
        "comentario_fonte": "Ambos se fundam em vantagens comparativas (Ricardo: tecnologia; H-O: dotação) e "
                            "assumem competição perfeita e retornos constantes.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01160
    {
        "id": "ECO-E2-L01160-1", "fonte_ref": "E2-L01160", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_TCI,
        "rotulo_item": "Item",
        "assertiva": ("As teorias clássicas do comércio internacional baseiam-se nas diferenças tecnológicas que "
                      "culminam em diferentes produtividades relativas da mão de obra, e a teoria neoclássica do "
                      "comércio internacional, na diferença relativa de dotação dos fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As teorias <u>clássicas</u> do comércio internacional baseiam-se nas diferenças tecnológicas "
                      "que culminam em diferentes produtividades relativas da mão de obra, e a teoria "
                      "<u>neoclássica</u> do comércio internacional, na diferença relativa de dotação dos fatores "
                      "de produção."),
        "poucas": (azb("Clássicos") + " (Ricardo): vantagem por " + vd("tecnologia") + " (produtividade relativa do "
                   "trabalho). " + azb("Neoclássicos") + " (Heckscher-Ohlin): vantagem por " + vd("dotação relativa "
                   "de fatores") + "."),
        "destrinchando": [
            "No " + azb("modelo ricardiano") + ", o trabalho é o único fator, e os países diferem na produtividade "
            "do trabalho entre produtos. Um país tem vantagem comparativa no bem que exige a "
            + vd("menor quantidade relativa de trabalho") + " por unidade, em comparação com o outro país.",
            "No " + azb("modelo H-O") + ", há ao menos dois fatores, e a tecnologia é igual entre países. O "
            + azb("teorema de H-O") + " diz que cada país se especializa e exporta o bem que usa intensivamente o "
            "fator que lhe é " + vd("relativamente abundante") + ".",
            "“Relativa” é a palavra-chave nos dois casos: em Ricardo, produtividade relativa (custo de "
            "oportunidade); em H-O, abundância relativa (razão K/L de um país comparada à do outro), não a "
            "quantidade absoluta de capital.",
            "Cronologia: " + oc("Smith") + " (1776) e " + oc("Ricardo") + " (1817) → " + oc("Heckscher")
            + " (1919) e " + oc("Ohlin") + " (1933) → " + oc("Samuelson") + " (Stolper-Samuelson, 1941; "
            "equalização, 1948) → " + oc("Leontief") + " (paradoxo, 1953) → " + oc("Krugman") + " (nova teoria, "
            "anos 1970-80).",
        ],
        "dissecando": (cz("[literalidade]") + " Frase-padrão de manual. O perigo é a versão invertida (neoclássica = "
                       "tecnologia), cobrada pela mesma banca em outros simulados. Pista: “mão de obra” como único "
                       "fator → Ricardo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As teorias neoclássicas baseiam-se nas diferenças tecnológicas que culminam em diferentes "
            "produtividades do trabalho.”</i> → ERRADO (troca clássica ↔ neoclássica)",
            "<i>“No H-O, o país exporta o bem que usa intensivamente o fator relativamente escasso.”</i> → ERRADO "
            "(inversão: fator abundante)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Ricardo: vantagens por diferenças de tecnologia (produtividade do trabalho, fator "
                            "único). H-O: diferenças de dotação relativa de ao menos dois fatores; teorema de H-O: "
                            "exporta o bem intensivo no fator abundante.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00641-1 (mesma assertiva, Nabuco 2026), ECO-E2-L01468-1"],
    },
    # ------------------------------------------------------------------ E2-L01161
    {
        "id": "ECO-E2-L01161-1", "fonte_ref": "E2-L01161", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_TCI,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Heckscher-Ohlin de comércio internacional, as vantagens comparativas, que levam "
                      "ao comércio entre dois países, decorrem de economias de escala na produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Heckscher-Ohlin de comércio internacional, as vantagens comparativas, que "
                       "levam ao comércio entre dois países, decorrem de ") + vm("economias de escala na produção")
                    + az(".")),
        "poucas": ("No H-O, a vantagem comparativa decorre da " + azb("dotação relativa de fatores") + ", com "
                   "retornos constantes. " + azb("Economias de escala") + " são outra explicação do comércio, "
                   "independente da vantagem comparativa."),
        "destrinchando": [
            "O H-O pressupõe " + vd("retornos constantes de escala") + " e concorrência perfeita; logo, não há "
            "espaço para que o tamanho da produção reduza custos.",
            "A fonte da vantagem é a abundância relativa: país com muito capital por trabalhador tem capital "
            "barato e exporta o bem " + vd("capital-intensivo") + ".",
            azb("Economias de escala") + " explicam ganhos de comércio por um canal diferente: concentrar a "
            "produção de cada variedade num só lugar reduz o custo médio e amplia a variedade disponível aos "
            "consumidores. É a " + azb("nova teoria do comércio") + " (" + oc("Krugman") + "), que explica o "
            "comércio " + vd("intraindustrial") + " entre países semelhantes (carros alemães × carros franceses).",
            "As duas explicações se complementam: dotações explicam o comércio " + vd("interindustrial")
            + " entre países diferentes (Norte × Sul); escala explica o intraindustrial entre parecidos (Norte × "
            "Norte).",
            vm("Regra-âncora: H-O = dotações; escala = nova teoria do comércio."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca da fonte do comércio por uma de outra escola. Pista: "
                       "“economias de escala” contradiz a hipótese de retornos constantes do H-O. 🔥 A mesma "
                       "frase circula em vários simulados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Economias de escala podem gerar comércio vantajoso mesmo entre países com dotações e tecnologias "
            "idênticas.”</i> → CERTO",
            "<i>“No modelo de Heckscher-Ohlin, as vantagens comparativas decorrem de diferenças tecnológicas.”</i> "
            "→ ERRADO (essa é a fonte ricardiana)",
        ])],
        "reescrita": ("No modelo de Heckscher-Ohlin de comércio internacional, as vantagens comparativas, que levam "
                      "ao comércio entre dois países, decorrem de " + hl("diferenças na dotação relativa de fatores "
                                                                          "de produção entre eles") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Economias de escala são outra explicação dos ganhos de comércio, independente de "
                            "vantagens comparativas, enfatizada pela Nova Teoria do Comércio.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00642-1 (mesma assertiva, Nabuco 2026)"],
    },
    # ------------------------------------------------------------------ E2-L01427
    {
        "id": "ECO-E2-L01427-1", "fonte_ref": "E2-L01427", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT1,
        "rotulo_item": "Item",
        "assertiva": ("Sendo as vacinas um bem cuja produção usa intensivamente a tecnologia, espera-se que, com a "
                      "pandemia e a elevação da demanda por vacinas, a remuneração relativa deste fator de produção "
                      "diminua comparado aos demais fatores, no modelo Heckscher-Ohlin."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Sendo as vacinas um bem cuja produção usa intensivamente a tecnologia, espera-se que, com a "
                       "pandemia e a elevação da demanda por vacinas, a remuneração relativa deste fator de produção ")
                    + vm("diminua") + az(" comparado aos demais fatores, no modelo Heckscher-Ohlin.")),
        "poucas": ("Demanda maior por vacinas → " + vd("preço relativo das vacinas ↑") + " → pela lógica de "
                   + azb("Stolper-Samuelson") + ", a remuneração do fator usado intensivamente nelas "
                   + vd("aumenta") + ", não diminui."),
        "destrinchando": [
            "O item trata a “tecnologia” como um fator de produção (algo como capital humano qualificado ou "
            "capital de P&D) e pede o efeito de um choque de " + vd("demanda") + " sobre um bem intensivo nesse "
            "fator.",
            "Encadeamento: a pandemia eleva a demanda por vacinas → o " + vd("preço relativo") + " das vacinas sobe "
            "→ o setor de vacinas se expande e disputa, proporcionalmente, mais do fator que usa intensivamente → "
            "com a oferta desse fator fixa, sua remuneração relativa " + vd("sobe") + ", e a dos demais fatores "
            "cai.",
            "É exatamente o " + azb("teorema de Stolper-Samuelson") + " (1941), derivado do H-O: alta do preço "
            "relativo de um bem → alta mais que proporcional da remuneração real do fator intensivo nele (efeito "
            "ampliação) e queda da do outro fator.",
            "Não confundir com " + azb("Rybczynski") + ": lá o choque é de oferta de fator (dotação), a preços "
            "constantes, e o efeito é sobre as quantidades produzidas. Aqui o choque é de preço do bem, e o efeito "
            "é sobre as remunerações.",
            vm("Regra-âncora: bem fica mais caro → o fator intensivo nele ganha."),
        ],
        "dissecando": (cz("[inversão]") + " Contexto atual (pandemia) e um fator pouco usual (“tecnologia”) para "
                       "desviar a atenção de um mecanismo simples; o sinal da conclusão foi invertido. Pista: "
                       "demanda ↑ por um bem nunca reduz a remuneração do fator que esse bem mais usa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a remuneração relativa deste fator de produção aumente comparado aos demais fatores…”</i> → "
            "CERTO",
            "<i>“…a elevação da demanda por vacinas aumentaria a dotação do fator tecnologia, pelo teorema de "
            "Rybczynski.”</i> → ERRADO (troca de teorema: Rybczynski parte da dotação, não da demanda)",
        ])],
        "reescrita": ("Sendo as vacinas um bem cuja produção usa intensivamente a tecnologia, espera-se que, com a "
                      "pandemia e a elevação da demanda por vacinas, a remuneração relativa deste fator de produção "
                      + hl("aumente") + " comparado aos demais fatores, no modelo Heckscher-Ohlin."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["espera-se"], "dificuldade": 1,
        "comentario_fonte": "Demanda maior por bem intensivo em tecnologia eleva seu preço e, por "
                            "Stolper-Samuelson, aumenta a remuneração relativa do fator intensivo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01468
    {
        "id": "ECO-E2-L01468-1", "fonte_ref": "E2-L01468", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT2,
        "rotulo_item": "Item",
        "assertiva": ("As teorias clássicas do comércio internacional baseiam-se na produtividade relativa da mão de "
                      "obra, e a teoria neoclássica do comércio internacional, na diferença relativa de dotação dos "
                      "fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As teorias <u>clássicas</u> do comércio internacional baseiam-se na <u>produtividade relativa "
                      "da mão de obra</u>, e a teoria <u>neoclássica</u> do comércio internacional, na diferença "
                      "relativa de dotação dos fatores de produção."),
        "poucas": ("Correto: " + azb("clássicos") + " (Smith, Ricardo) → produtividade relativa do trabalho; "
                   + azb("neoclássicos") + " (Heckscher-Ohlin) → dotação relativa de capital e trabalho."),
        "destrinchando": [
            oc("Adam Smith") + " (vantagem absoluta) e " + oc("David Ricardo") + " (vantagem comparativa) "
            "trabalham com a teoria do valor-trabalho: o custo de um bem é o trabalho nele contido. Diferenças de "
            + vd("produtividade do trabalho") + " entre países geram diferenças de custo e, portanto, comércio.",
            "Ricardo mostrou que basta a produtividade " + vd("relativa") + " diferir: Portugal, mais produtivo "
            "em vinho e em tecido, ainda ganha especializando-se no vinho, onde sua vantagem é maior.",
            "A teoria " + azb("neoclássica") + " (" + oc("Heckscher") + ", " + oc("Ohlin") + ", "
            + oc("Samuelson") + ") supõe tecnologia igual e explica o comércio pela " + vd("abundância relativa")
            + " de fatores e pela intensidade fatorial dos bens. Seu desdobramento são os teoremas de "
            "Stolper-Samuelson, Rybczynski e da equalização dos preços dos fatores.",
            "Ambas compartilham concorrência perfeita, retornos constantes e o princípio da vantagem comparativa; "
            "diferem na <b>fonte</b> da vantagem.",
        ],
        "dissecando": (cz("[literalidade]") + " Versão enxuta da frase de manual. A armadilha seria uma troca de "
                       "rótulos, que não ocorreu. 🔥 A mesma banca cobra a versão errada atribuindo a Smith e "
                       "Ricardo a dotação de capital e trabalho."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A teoria clássica de Smith e Ricardo defendia a especialização com base na dotação relativa de "
            "capital e trabalho.”</i> → ERRADO (troca clássica ↔ neoclássica)",
            "<i>“Para Ricardo, só há ganho de comércio se cada país tiver vantagem absoluta em algum bem.”</i> → "
            "ERRADO (basta a vantagem comparativa)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Clássicos (Ricardo): produtividade relativa do trabalho; neoclássicos (H-O): dotação "
                            "relativa de fatores.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00641-1, ECO-E2-L01160-1 (mesma distinção), ECO-E2-L01505-1 "
                    "(versão ERRADA)"],
    },
    # ------------------------------------------------------------------ E2-L01469
    {
        "id": "ECO-E2-L01469-1", "fonte_ref": "E2-L01469", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT2,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo ricardiano, as vantagens decorrentes do comércio internacional são "
                      "afastadas na hipótese de um país ser relativamente menos produtivo do que outro em todas as "
                      "indústrias."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o modelo ricardiano, as vantagens decorrentes do comércio internacional ")
                    + vm("são afastadas") + az(" na hipótese de um país ser relativamente menos produtivo do que "
                                               "outro em todas as indústrias.")),
        "poucas": ("É a tese central de " + oc("Ricardo") + ": mesmo com " + azb("desvantagem absoluta")
                   + " em tudo, o país ganha ao se especializar onde sua desvantagem é " + vd("menor") + " (sua "
                   + azb("vantagem comparativa") + ")."),
        "destrinchando": [
            "Ser menos produtivo em todas as indústrias é ter " + azb("desvantagem absoluta") + " em tudo. Para "
            + oc("Smith") + ", isso eliminaria o comércio; " + oc("Ricardo") + " (1817) mostrou que não.",
            "O que importa é o " + azb("custo de oportunidade") + ". Exemplo: A produz 6 x ou 6 y por hora; B, "
            "1 x ou 3 y. B é pior nos dois, mas em B 1 y custa só " + vd("1/3 x") + " (contra 1 x em A): B tem "
            "vantagem comparativa em y, e A, em x.",
            "Trocando a um preço entre os dois custos de oportunidade (entre 1/3 e 1 x por y), ambos consomem mais "
            "do que conseguiriam sozinhos. O país menos produtivo compete com " + vd("salários menores")
            + ", que refletem sua menor produtividade.",
            "Mitos que o modelo derruba (" + oc("Krugman") + " e " + oc("Obstfeld") + "): (1) “só ganha quem é "
            "competitivo”; (2) “competir com salários baixos é exploração”; (3) “o país menos produtivo é "
            "prejudicado”. O único caso sem ganho é o de produtividades " + vd("proporcionais") + " (custos de "
            "oportunidade iguais).",
            vm("Regra-âncora: desvantagem absoluta em tudo não impede o comércio; basta custo de oportunidade "
               "diferente."),
        ],
        "dissecando": (cz("[contradição]") + " O item afirma o oposto do teorema que cita. O “relativamente” "
                       "confunde: se o país fosse menos produtivo em termos <b>relativos</b> em tudo, não haveria "
                       "vantagem comparativa, mas isso é impossível com dois bens. A banca usa a palavra no sentido "
                       "de “em comparação com o outro país”, isto é, desvantagem absoluta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, um país com desvantagem absoluta em todos os bens ainda pode ganhar com o "
            "comércio, especializando-se no bem em que sua desvantagem é menor.”</i> → CERTO",
            "<i>“No modelo ricardiano, não há ganhos de comércio quando as produtividades relativas dos dois "
            "países são iguais.”</i> → CERTO",
        ])],
        "reescrita": ("De acordo com o modelo ricardiano, as vantagens decorrentes do comércio internacional "
                      + hl("não são afastadas") + " na hipótese de um país ser relativamente menos produtivo do que "
                      "outro em todas as indústrias."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": ["todas"], "dificuldade": 1,
        "comentario_fonte": "Mesmo com desvantagem absoluta em todas as indústrias, há vantagem comparativa e ganho "
                            "de comércio; o país se especializa onde a desvantagem é menor.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01470
    {
        "id": "ECO-E2-L01470-1", "fonte_ref": "E2-L01470", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT2,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Heckscher-Ohlin, o comércio internacional leva a um aumento do preço do fator de "
                      "produção mais abundante relativamente ao preço do fator de produção menos abundante dentro "
                      "de cada país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Heckscher-Ohlin, o comércio internacional leva a um <u>aumento</u> do preço do "
                      "fator de produção <u>mais abundante</u> relativamente ao preço do fator de produção menos "
                      "abundante dentro de cada país."),
        "poucas": ("É a implicação de " + azb("Stolper-Samuelson") + ": com comércio, cada país exporta o bem "
                   "intensivo no fator abundante, e o preço relativo desse fator " + vd("sobe") + "."),
        "destrinchando": [
            "Em autarquia, o fator abundante é relativamente " + vd("barato") + " (é isso que dá ao país vantagem "
            "comparativa no bem que o usa intensivamente).",
            "Com o comércio, o país se especializa no bem intensivo no fator abundante; a demanda por esse fator "
            "cresce, e a do fator escasso diminui. Resultado: o " + vd("preço relativo do fator abundante sobe")
            + " (e o fator escasso perde, inclusive em termos reais).",
            "O mesmo movimento ocorre no parceiro, em sentido inverso: lá, o outro fator é o abundante. Assim, as "
            "razões w/r dos dois países " + azb("convergem") + ": é o caminho para o " + azb("teorema da "
            "equalização dos preços dos fatores") + " (" + oc("Samuelson") + ", 1948).",
            "Exemplo: num país rico em trabalho, como a China nas décadas de abertura, o modelo prevê alta dos "
            "salários relativos; num país rico em capital, como os EUA, queda do salário relativo do trabalho "
            "pouco qualificado.",
            vm("Regra-âncora: comércio → fator abundante fica relativamente mais caro em cada país."),
        ],
        "dissecando": (cz("[literalidade]") + " Enunciado correto do efeito distributivo do H-O. O risco é a "
                       "intuição de que “o que é abundante fica mais barato”: isso vale em autarquia; o comércio "
                       "faz justamente o contrário, valorizando o fator abundante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o comércio internacional leva a um aumento do preço do fator menos abundante relativamente ao "
            "do mais abundante.”</i> → ERRADO (inversão)",
            "<i>“…o comércio tende a aproximar as remunerações relativas dos fatores entre os países.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Stolper-Samuelson: a abertura aumenta a remuneração do fator abundante e reduz a do "
                            "escasso; o país se especializa nos bens intensivos no fator abundante.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00573-1, ECO-E2-L00698-1 (Stolper-Samuelson e abertura)"],
    },
    # ------------------------------------------------------------------ E2-L01505
    {
        "id": "ECO-E2-L01505-1", "fonte_ref": "E2-L01505", "destino": "73", "subtema": H2["vac"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT3,
        "rotulo_item": "Item",
        "assertiva": ("A teoria clássica de Smith e Ricardo defendia a especialização com base na dotação relativa "
                      "dos fatores de produção capital e trabalho, que apresentariam rendimentos constantes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A teoria clássica de Smith e Ricardo defendia a especialização com base na ")
                    + vm("dotação relativa dos fatores de produção capital e trabalho, que apresentariam")
                    + az(" rendimentos constantes.")),
        "poucas": ("Smith e Ricardo baseavam a especialização na " + azb("produtividade do trabalho")
                   + " (único fator). A " + azb("dotação relativa de capital e trabalho") + " é a base da teoria "
                   "neoclássica de Heckscher-Ohlin."),
        "destrinchando": [
            oc("Adam Smith") + " (1776): " + azb("vantagem absoluta") + ", cada país produz o que faz com menos "
            "trabalho. " + oc("David Ricardo") + " (1817): " + azb("vantagem comparativa") + ", cada país produz o "
            "que faz com menor custo de oportunidade. Nos dois, o insumo é o " + vd("trabalho") + ", sob a teoria "
            "do valor-trabalho.",
            "No modelo ricardiano, a produtividade do trabalho é constante (cada hora rende sempre o mesmo): daí "
            "custos de oportunidade constantes e FPP linear. A ideia de “rendimentos constantes” cabe ao "
            "trabalho, não a uma dotação de capital e trabalho.",
            "A especialização por " + vd("dotação relativa de fatores") + " (capital × trabalho) é a contribuição "
            "de " + oc("Heckscher") + " (1919) e " + oc("Ohlin") + " (1933), o núcleo da teoria "
            + azb("neoclássica") + ", já no século XX.",
            "Por que a banca mistura? Porque os dois modelos compartilham concorrência perfeita, retornos "
            "constantes e vantagem comparativa. O traço distintivo é a fonte da vantagem: tecnologia (clássicos) × "
            "dotações (neoclássicos).",
            vm("Regra-âncora: clássicos = trabalho e produtividade; neoclássicos = capital e trabalho, dotações."),
        ],
        "dissecando": (cz("[troca de conceito · anacronismo]") + " O item atribui aos clássicos a explicação "
                       "neoclássica, formulada mais de um século depois. A cauda “rendimentos constantes” é "
                       "verdadeira para os dois modelos e serve de isca. Pista: “capital e trabalho” como dupla de "
                       "fatores = H-O."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A teoria clássica de Smith e Ricardo defendia a especialização com base nas diferenças de "
            "produtividade do trabalho entre os países.”</i> → CERTO",
            "<i>“Para Smith, a especialização se baseava no menor custo de oportunidade.”</i> → ERRADO (troca de "
            "ator: custo de oportunidade é Ricardo; Smith é vantagem absoluta)",
        ])],
        "reescrita": ("A teoria clássica de Smith e Ricardo defendia a especialização com base na "
                      + hl("produtividade relativa do trabalho, fator único que apresentaria") + " rendimentos "
                      "constantes."),
        "tipo_erro": ["TROCA_CONCEITO", "ANACRONISMO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Clássicos (Smith: vantagem absoluta; Ricardo: comparativa) baseavam a especialização na "
                            "produtividade do trabalho; dotação de capital e trabalho é o modelo H-O, do século XX.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01468-1 (versão CERTO da mesma distinção)"],
    },
    # ------------------------------------------------------------------ E2-L01506
    {
        "id": "ECO-E2-L01506-1", "fonte_ref": "E2-L01506", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT3,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o teorema de equalização dos preços dos fatores, havendo livre comércio dos bens "
                      "finais, não é necessária a mobilidade internacional dos fatores de produção para que seus "
                      "preços relativos se igualem entre os países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o teorema de equalização dos preços dos fatores, havendo livre comércio dos bens "
                      "finais, <u>não é necessária</u> a mobilidade internacional dos fatores de produção para que "
                      "seus preços relativos se igualem entre os países."),
        "poucas": ("O comércio de bens funciona como " + azb("comércio implícito de fatores") + ": exportar bens "
                   "trabalho-intensivos é exportar serviços de trabalho. Por isso os preços dos fatores convergem "
                   + vd("sem migração") + "."),
        "destrinchando": [
            "Partida (autarquia): no país B, abundante em trabalho, o salário relativo é baixo: "
            "w<sub>B</sub>/r<sub>B</sub> &lt; w<sub>W</sub>/r<sub>W</sub>, em que W é o parceiro rico em capital.",
            "Com o comércio, B expande o bem trabalho-intensivo e contrai o capital-intensivo; a demanda por "
            "trabalho cresce mais que a por capital, e w<sub>B</sub>/r<sub>B</sub> " + vd("sobe") + ". Em W ocorre o "
            "inverso. As razões convergem até " + vd("w<sub>B</sub>/r<sub>B</sub> = w<sub>W</sub>/r<sub>W</sub>")
            + ".",
            "Resultado formal de " + oc("Samuelson") + " (1948-49): sob as hipóteses do H-O, a equalização vale "
            "para os preços relativos <b>e absolutos</b> dos fatores. Condições: tecnologias idênticas, "
            "concorrência perfeita, retornos constantes, sem custos de transporte nem barreiras, sem reversão de "
            "intensidade fatorial e especialização incompleta (os dois países produzem os dois bens).",
            oc("Mundell") + " (1957) mostrou a simetria: mobilidade de fatores sem comércio de bens levaria ao "
            "mesmo resultado. Comércio de bens e migração de fatores são " + azb("substitutos") + ".",
            "Na prática, a equalização plena não se observa (salários muito diferentes entre países), porque as "
            "hipóteses falham: tecnologias diferentes, custos de comércio, barreiras e especialização completa.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " Parece que só a migração igualaria salários; o teorema diz que o "
                       "comércio de bens basta. O “não é necessária” é a pegadinha: quem lê rápido entende “não "
                       "ocorre sem mobilidade” e marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo teorema de equalização, o livre comércio de bens só iguala os preços dos fatores se houver "
            "também livre mobilidade internacional de capital e trabalho.”</i> → ERRADO (a mobilidade é "
            "dispensável)",
            "<i>“A equalização dos preços dos fatores depende, entre outras hipóteses, de tecnologias idênticas "
            "entre os países.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["não é necessária"], "dificuldade": 2,
        "comentario_fonte": "O comércio de bens substitui a mobilidade dos fatores; os preços relativos dos fatores "
                            "convergem (wB/rB = wW/rW) sem migração; Mundell (1957) mostrou a simetria.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 385", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 386", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 387", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01507
    {
        "id": "ECO-E2-L01507-1", "fonte_ref": "E2-L01507", "destino": "73", "subtema": H2["leo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT3,
        "rotulo_item": "Item",
        "assertiva": ("O paradoxo de Leontief revelou que, ao contrário do esperado pela teoria, as exportações dos "
                      "EUA eram mais intensivas em capital do que as suas importações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O paradoxo de Leontief revelou que, ao contrário do esperado pela teoria, as exportações "
                       "dos EUA eram ") + vm("mais") + az(" intensivas em capital do que as suas importações.")),
        "poucas": ("Exportações mais capital-intensivas era o que a teoria " + azb("previa") + ". O paradoxo foi o "
                   "contrário: as exportações dos EUA eram " + vd("menos") + " intensivas em capital que as "
                   "importações."),
        "destrinchando": [
            "Previsão do " + azb("H-O") + ": os EUA, país mais abundante em capital do pós-guerra, exportariam bens "
            "capital-intensivos e importariam trabalho-intensivos.",
            oc("Leontief") + " (1953), com a matriz insumo-produto de 1947, achou o oposto: a relação capital/"
            "trabalho dos substitutos das importações superava a das exportações. Estudo de " + oc("Baldwin")
            + " (1971) com dados de 1962, reproduzido por " + oc("Krugman") + " e " + oc("Obstfeld") + ": K/L de "
            + vd("US$ 17.916") + " por trabalhador nas importações contra " + vd("US$ 14.321") + " nas "
            "exportações.",
            "Mesma tabela: as exportações tinham trabalhadores com mais anos de estudo (" + vd("10,1 × 9,9")
            + ") e maior proporção de engenheiros e cientistas (" + vd("0,0255 × 0,0189") + "). Daí a "
            "explicação mais aceita: os EUA exportavam bens intensivos em " + azb("capital humano") + " e "
            "tecnologia.",
            "Outras explicações: recursos naturais complementares ao capital nas importações, proteção tarifária "
            "a setores trabalho-intensivos e diferenças tecnológicas entre países (que violam a hipótese de "
            "tecnologia idêntica).",
        ],
        "dissecando": (cz("[inversão]") + " O item descreve a <b>previsão</b> da teoria como se fosse o resultado "
                       "paradoxal. A expressão “ao contrário do esperado” denuncia: se as exportações eram mais "
                       "capital-intensivas, não haveria nada de inesperado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O paradoxo de Leontief revelou que as importações dos EUA eram mais intensivas em capital do que "
            "suas exportações.”</i> → CERTO",
            "<i>“O paradoxo de Leontief confirmou empiricamente o teorema de Heckscher-Ohlin.”</i> → ERRADO "
            "(contradição: ele o contrariou)",
        ])],
        "reescrita": ("O paradoxo de Leontief revelou que, ao contrário do esperado pela teoria, as exportações dos "
                      "EUA eram " + hl("menos") + " intensivas em capital do que as suas importações."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Leontief (1953): EUA, ricos em capital, exportavam bens trabalho-intensivos e "
                            "importavam capital-intensivos; tabela de Baldwin (1971) com dados de 1962.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 388", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00699-1 (versão CERTO do paradoxo)"],
    },
    # ------------------------------------------------------------------ E2-L01508
    {
        "id": "ECO-E2-L01508-1", "fonte_ref": "E2-L01508", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT3,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o teorema de Rybczynski, o aumento da dotação de um fator de produção levará à queda "
                      "do preço relativo deste fator e consequente redução da produção do bem que usa "
                      "intensivamente este fator."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo o teorema de Rybczynski, o aumento da dotação de um fator de produção levará ")
                    + vm("à queda do preço relativo deste fator e consequente redução") + az(" da produção do bem "
                                                                                               "que usa "
                                                                                               "intensivamente "
                                                                                               "este fator.")),
        "poucas": ("Rybczynski: a preços dos bens constantes, mais de um fator → " + vd("aumento mais que "
                   "proporcional") + " da produção do bem intensivo nele e queda da do outro bem. Os preços dos "
                   "fatores " + vm("não mudam") + "."),
        "destrinchando": [
            "Hipótese do " + azb("teorema de Rybczynski") + " (1955): preços dos bens " + vd("fixos") + " (país "
            "pequeno, tomador de preços). Com preços dos bens fixos e tecnologia dada, as remunerações dos fatores "
            "também ficam fixas (são determinadas pelos preços dos bens, via Stolper-Samuelson).",
            "Se cresce a dotação de capital, o único modo de empregá-lo, mantendo as técnicas, é expandir o setor "
            "capital-intensivo; ele precisa de algum trabalho, que sai do setor trabalho-intensivo. Resultado: "
            "produção do bem capital-intensivo " + vd("sobe mais que proporcionalmente") + "; a do outro bem "
            + vd("cai em termos absolutos") + ".",
            "Aplicações: crescimento enviesado da FPP (a fronteira se expande mais no eixo do bem intensivo no "
            "fator que cresceu) e " + azb("doença holandesa") + " (descoberta de recursos naturais expande o setor "
            "extrativo e encolhe a indústria).",
            "Os dois erros do item: (1) a queda do preço do fator não faz parte do teorema, que o mantém constante; "
            "(2) a produção do bem intensivo no fator " + vd("aumenta") + ", não diminui.",
            vm("Regra-âncora: dotação de um fator ↑ → bem intensivo nele ↑ (mais que proporcional); o outro ↓."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " Dois erros: o efeito sobre a produção foi invertido, "
                       "e um efeito de preço que o teorema exclui foi acrescentado, com ar de “lei da oferta”. "
                       "Pista: Rybczynski fala de quantidades a preços constantes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o teorema de Rybczynski, a preços constantes, o aumento da dotação de capital reduz a "
            "produção do bem trabalho-intensivo.”</i> → CERTO",
            "<i>“O teorema de Rybczynski relaciona o preço dos bens à remuneração dos fatores.”</i> → ERRADO (esse é "
            "Stolper-Samuelson)",
        ])],
        "reescrita": ("Segundo o teorema de Rybczynski, o aumento da dotação de um fator de produção levará "
                      + hl("a um aumento mais que proporcional") + " da produção do bem que usa intensivamente este "
                      "fator" + hl(" e à redução da produção do outro bem, mantidos constantes os preços dos bens")
                      + "."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Rybczynski: a preços constantes, aumento da dotação de um fator eleva mais que "
                            "proporcionalmente a produção do bem intensivo nesse fator e reduz a do outro bem.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 389", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00572-1 (Rybczynski × Stolper-Samuelson)"],
    },
]
