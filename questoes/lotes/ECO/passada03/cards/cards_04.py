"""Cards do lote de redação 04 — ECO, passada 03 (notas 57, 58 e 59: crescimento, desenvolvimento e trabalho)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "cresc": "💡 Teorias do crescimento",
    "desenv": "🌾 Teorias do desenvolvimento",
    "desemp": "👷 Desemprego e mercado de trabalho",
    "okun": "📏 Lei de Okun",
}

CMD_NAB_CRESC = "Com base nas teorias do crescimento econômico, julgue o item seguinte."

CMD_RT_CRESC = ("Com relação aos modelos e teorias de crescimento e desenvolvimento econômico, julgue o item a "
                "seguir.")

CMD_NIDI = "A respeito dos modelos de crescimento clássicos e modernos, julgue o item a seguir."

CMD_DESENV = "Acerca das teorias de crescimento e desenvolvimento econômico, julgue o item a seguir."

CMD_TRAB = "Acerca do mercado de trabalho e das estatísticas de emprego e desemprego, julgue o item a seguir."

CMD_DESEMP = "Acerca do desemprego e do funcionamento do mercado de trabalho, julgue o item a seguir."

CMD_OKUN = "Acerca da relação entre produto e desemprego, julgue o item a seguir."

CMD_CLIO = "Acerca do mercado de trabalho e do desemprego, julgue o item a seguir."

CMD_BOZAN = "Sobre os conceitos de desemprego, julgue a assertiva a seguir."

CMD_NAB_DESEMP = ("Acerca dos indicadores do mercado de trabalho, conceitos e tipos de desemprego, julgue o item "
                  "a seguir.")

AL_2016 = "banca_provavel: marca ⌚ 2016 na fonte sugere CACD 2016; não confirmada"
AL_2020 = "banca_provavel: marca ⌚ 2020 na fonte sugere CACD 2020; não confirmada"
AL_2022 = ("banca_provavel: a fonte só traz o ano (2022) e menciona recursos indeferidos pela banca; possivelmente "
           "CEBRASPE (CACD 2022), não confirmado")

CARDS = [
    # ------------------------------------------------------------------ E2-L01258
    {
        "id": "ECO-E2-L01258-1", "fonte_ref": "E2-L01258", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a visão de Schumpeter sobre o processo de desenvolvimento econômico, a inovação "
                      "desempenha um papel central nesse processo. A teoria schumpeteriana, em especial, enfatiza "
                      "o lado da demanda e o papel inovador do consumidor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a visão de Schumpeter sobre o processo de desenvolvimento econômico, a inovação "
                       "desempenha um papel central nesse processo. A teoria schumpeteriana, em especial, enfatiza "
                       "o lado da ") + vm("demanda") + az(" e o papel inovador do ") + vm("consumidor") + az(".")),
        "poucas": ("Em " + oc("Schumpeter") + ", a inovação nasce do lado da " + azb("oferta") + ": quem inova é o "
                   + azb("empresário (empreendedor)") + ", e o consumidor é “educado” a desejar o novo."),
        "destrinchando": [
            "Na " + oc("Teoria do Desenvolvimento Econômico") + " (" + vd("1911") + "), " + oc("Schumpeter")
            + " parte do " + azb("fluxo circular") + ": uma economia que se repete, sem lucro extraordinário. O "
            "desenvolvimento é a ruptura desse fluxo por " + azb("novas combinações") + " de fatores.",
            "As novas combinações são cinco: novo bem, novo método de produção, novo mercado, nova fonte de "
            "matérias-primas e nova organização de um setor (criar ou romper um monopólio). Quem as executa é o "
            + azb("empresário inovador") + " — não necessariamente o dono do capital —, financiado pelo "
            + azb("crédito bancário") + ", que lhe dá poder de compra antes de existir a produção.",
            "O prêmio da inovação é o " + azb("lucro extraordinário") + ", temporário: os imitadores chegam em "
            "“enxame”, o lucro se dissipa e a onda de investimentos explica os ciclos. Em "
            + oc("Capitalismo, Socialismo e Democracia") + " (" + vd("1942") + "), o processo ganha o nome de "
            + azb("destruição criadora") + ".",
            "O consumidor, para Schumpeter, é em regra passivo: as mudanças partem do produtor, e os consumidores "
            "aprendem a querer coisas novas. Ênfase na demanda é marca de " + oc("Keynes") + ", não de Schumpeter.",
            vm("Regra-âncora: Schumpeter = oferta, empresário, crédito e destruição criadora."),
        ],
        "dissecando": (cz("[meia-verdade · troca de ator]") + " A 1ª frase é a tese correta (inovação central); "
                       "o erro foi enxertado na 2ª, que troca o agente (consumidor no lugar do empresário) e o "
                       "lado do mercado (demanda no lugar da oferta). O “em especial” dá ar de detalhe técnico ao "
                       "que é inversão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Schumpeter, o crédito bancário é essencial porque transfere poder de compra ao empresário "
            "inovador.”</i> → CERTO",
            "<i>“Para Schumpeter, o lucro do inovador é permanente, garantido pela patente.”</i> → ERRADO (o "
            "lucro extraordinário é temporário: some com a imitação)",
        ])],
        "reescrita": ("Segundo a visão de Schumpeter sobre o processo de desenvolvimento econômico, a inovação "
                      "desempenha um papel central nesse processo. A teoria schumpeteriana, em especial, enfatiza "
                      "o lado da " + hl("oferta") + " e o papel inovador do " + hl("empresário") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_ATOR"], "moduladores": ["em especial"], "dificuldade": 1,
        "comentario_fonte": "Schumpeter enfatiza o papel inovador dos empresários/empreendedores (e não do "
                            "consumidor), que investem e criam novos produtos, serviços ou métodos de produção.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “shumpeteriana” → “schumpeteriana”"],
    },
    # ------------------------------------------------------------------ E2-L01260
    {
        "id": "ECO-E2-L01260-1", "fonte_ref": "E2-L01260", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("As modernas teorias do crescimento endógeno tentam explicar a taxa de progresso "
                      "tecnológico, que o Modelo de Solow considera exógeno."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As modernas teorias do crescimento endógeno tentam <u>explicar a taxa de progresso "
                      "tecnológico</u>, que o Modelo de Solow considera <u>exógeno</u>."),
        "poucas": ("É a definição do " + azb("crescimento endógeno") + ": trazer para dentro do modelo o progresso "
                   "técnico que, em " + oc("Solow") + ", é um dado externo que “cai do céu”."),
        "destrinchando": [
            "Em " + oc("Solow") + " (" + vd("1956") + "), a acumulação de capital esbarra nos rendimentos "
            "marginais decrescentes: a economia converge ao " + azb("estado estacionário") + ". Com progresso "
            "técnico à taxa g, o produto per capita cresce exatamente a " + vd("g") + " no longo prazo — mas g "
            "é exógeno: o modelo explica tudo, menos o motor do crescimento.",
            "As teorias de " + azb("crescimento endógeno") + " (anos 1980–1990) atacam essa lacuna: "
            + oc("Romer") + " (" + vd("1986") + ") com externalidades do conhecimento; " + oc("Lucas") + " ("
            + vd("1988") + ") com capital humano; " + oc("Romer") + " (" + vd("1990") + ") com P&D e ideias "
            + azb("não rivais") + "; " + oc("Aghion e Howitt") + " (" + vd("1992") + ") com destruição criadora "
            "schumpeteriana; e os modelos " + azb("AK") + ", em que o capital não tem rendimento decrescente.",
            "Consequência de política: no endógeno, poupança, educação, P&D e instituições podem alterar a "
            + azb("taxa") + " de crescimento de longo prazo, não só o nível da renda, como em Solow.",
            "Precursor: " + oc("Arrow") + " (" + vd("1962") + "), com o " + azb("learning by doing") + " — a "
            "produtividade sobe com a experiência acumulada de produzir.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Reproduz a definição de manual; o "
                       "“tentam explicar” é prudente e verdadeiro. A pegadinha possível estaria em inverter os "
                       "papéis (Solow endógeno × modelos novos exógenos), o que não ocorre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, a taxa de crescimento de longo prazo do produto per capita depende da taxa "
            "de poupança.”</i> → ERRADO (a poupança afeta o nível; a taxa de longo prazo é g, exógena)",
            "<i>“Nos modelos de crescimento endógeno, políticas de incentivo à P&D podem elevar "
            "permanentemente a taxa de crescimento.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tentam"], "dificuldade": 1,
        "comentario_fonte": "Em Solow, o crescimento per capita no estado estacionário iguala a taxa de progresso "
                            "tecnológico, exógena; os modelos endógenos explicam essa variável por externalidades, "
                            "P&D etc.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01261
    {
        "id": "ECO-E2-L01261-1", "fonte_ref": "E2-L01261", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("Contrariamente ao Modelo de Solow, <u><b>EM ALGUNS MODELOS DE CRESCIMENTO "
                      "ENDÓGENO</b></u>, o capital, seja físico ou humano, apresenta retornos marginais constantes "
                      "e não decrescentes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Contrariamente ao Modelo de Solow, <u>EM ALGUNS MODELOS DE CRESCIMENTO ENDÓGENO</u>, o "
                      "capital, seja físico ou humano, apresenta retornos marginais constantes e não "
                      "decrescentes."),
        "poucas": ("No " + azb("modelo AK") + " (Y = AK) o produto marginal do capital é a constante " + vd("A")
                   + ": sem rendimento decrescente, não há estado estacionário e o crescimento é perpétuo. O "
                   "“em alguns” salva o item."),
        "destrinchando": [
            "Em " + oc("Solow") + ", f(k) é côncava: " + vd("f″(k) < 0") + ". Cada unidade extra de capital "
            "rende menos, até que o investimento só repõe a depreciação e a diluição — fim do crescimento per "
            "capita sem progresso técnico.",
            "No " + azb("modelo AK") + " (" + oc("Rebelo") + ", " + vd("1991") + "), Y = AK, com K entendido em "
            "sentido amplo (físico + humano + conhecimento). PMgK = " + vd("A") + ", constante. Então Δk/k = "
            "sA − (n + δ): quem poupa mais cresce mais, para sempre.",
            "Em " + oc("Lucas") + " (" + vd("1988") + "), o capital humano é acumulado com rendimento linear "
            "no tempo dedicado ao estudo; em " + oc("Romer") + " (" + vd("1986") + "), o capital de cada firma "
            "tem rendimento decrescente para ela, mas o " + azb("transbordamento") + " de conhecimento torna "
            "constante (ou crescente) o retorno agregado.",
            "Por isso a generalização seria falsa: há modelos endógenos baseados em P&D e variedade de produtos "
            "(" + oc("Romer") + ", " + vd("1990") + ") que mantêm rendimentos decrescentes do capital físico e "
            "põem o motor do crescimento nas ideias.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O item é salvo pelo “em alguns”, que a própria fonte "
                       "destacou em maiúsculas. 🔥 A versão sem o modulador (“nos modelos de crescimento "
                       "endógeno, o capital apresenta retornos constantes”) é a armadilha clássica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em todos os modelos de crescimento endógeno, o capital apresenta retornos marginais "
            "constantes.”</i> → ERRADO (modulador absoluto)",
            "<i>“No modelo AK, um aumento da taxa de poupança eleva permanentemente a taxa de crescimento.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["em alguns"], "dificuldade": 2,
        "comentario_fonte": "Os modelos endógenos costumam abandonar o retorno marginal decrescente do capital; o "
                            "AK tem retornos constantes, mas isso não vale para todos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01442
    {
        "id": "ECO-E2-L01442-1", "fonte_ref": "E2-L01442", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": ("Acerca da relação entre poupança e investimento e dos modelos de crescimento econômico, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Nos modelos de crescimento endógeno, os investimentos em capital humano e pesquisa e "
                      "desenvolvimento são fatores essenciais para explicar o crescimento de longo prazo da "
                      "economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Nos modelos de crescimento endógeno, os investimentos em capital humano e pesquisa e "
                      "desenvolvimento são fatores <u>essenciais</u> para explicar o crescimento de longo prazo da "
                      "economia."),
        "poucas": ("Capital humano (" + oc("Lucas") + ") e P&D (" + oc("Romer") + ", " + oc("Aghion-Howitt")
                   + ") são justamente os mecanismos que os modelos endógenos usam para escapar dos rendimentos "
                   "decrescentes e explicar o crescimento contínuo."),
        "destrinchando": [
            "Sem progresso técnico, " + oc("Solow") + " prevê crescimento per capita nulo no longo prazo. Os "
            "modelos endógenos precisam de um fator que se acumule " + azb("sem rendimentos decrescentes")
            + " no agregado — e as candidatas naturais são o conhecimento e as qualificações.",
            azb("Capital humano") + ": em " + oc("Lucas") + " (" + vd("1988") + "), os trabalhadores dividem o "
            "tempo entre produzir e estudar; a acumulação de qualificações sustenta o crescimento e gera "
            "externalidades (quem convive com gente qualificada fica mais produtivo).",
            azb("P&D") + ": em " + oc("Romer") + " (" + vd("1990") + "), firmas investem em pesquisa para criar "
            "novos bens e obter poder de mercado temporário; as ideias são " + azb("não rivais") + " (usá-las não "
            "as esgota), por isso o estoque de conhecimento alimenta novas ideias. Em " + oc("Aghion e Howitt")
            + " (" + vd("1992") + "), a inovação de qualidade substitui a anterior (destruição criadora).",
            "Implicação de política: subsídio a P&D, proteção (calibrada) à propriedade intelectual e "
            "investimento em educação afetam a " + azb("taxa") + " de crescimento, não apenas o nível da renda.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Reproduz o núcleo da teoria. O “essenciais” pode assustar "
                       "como exagero, mas é exato: sem esses mecanismos (ou o AK), o modelo volta a ser Solow. "
                       "Desconfie do adjetivo forte só quando ele contraria a teoria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nos modelos de crescimento endógeno, o progresso tecnológico é tratado como variável exógena, "
            "determinada fora do sistema econômico.”</i> → ERRADO (inversão: isso é Solow)",
            "<i>“Como o conhecimento é não rival, sua acumulação pode gerar rendimentos crescentes no "
            "agregado.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["essenciais"], "dificuldade": 1,
        "comentario_fonte": "Romer, Lucas e Aghion-Howitt internalizam o progresso técnico: capital humano e P&D "
                            "geram externalidades e retornos não decrescentes, sustentando o crescimento de longo "
                            "prazo (vários comentários de IA empilhados, convergentes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01654
    {
        "id": "ECO-E2-L01654-1", "fonte_ref": "E2-L01654", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Harrod-Domar, a taxa de crescimento da economia cresce com a taxa de poupança "
                      "e o produto médio do capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Harrod-Domar, a taxa de crescimento da economia cresce com a taxa de poupança "
                      "e o <u>produto médio do capital</u>."),
        "poucas": ("Em " + azb("Harrod-Domar") + ", " + vd("g = s/v") + ", com v = K/Y. Como o produto médio do "
                   "capital é Y/K = 1/v, " + vd("g = s × (Y/K)") + ": sobe com a poupança e com o produto médio "
                   "do capital."),
        "destrinchando": [
            "Hipóteses: tecnologia de proporções fixas, relação " + azb("capital-produto") + " v = K/Y constante, "
            "poupança proporcional à renda (S = sY) e S = I. Como ΔK = I = sY e ΔY = ΔK/v, vem "
            + vd("ΔY/Y = s/v") + ".",
            "Exemplo: s = " + vd("20%") + " e v = " + vd("4") + " → g = " + vd("5% ao ano") + ". Com "
            "depreciação, a fórmula vira " + vd("g = σ·s − δ") + ", em que σ = Y/K é a produtividade do capital.",
            "Origem: " + oc("Roy Harrod") + " (" + vd("1939") + ") e " + oc("Evsey Domar") + " (" + vd("1946")
            + "), de forma independente, ampliando a lógica keynesiana para o longo prazo: o investimento gera "
            "demanda (multiplicador) e também capacidade (efeito-capacidade).",
            "Harrod distingue a " + azb("taxa garantida") + " (s/v, que mantém os empresários satisfeitos), a "
            + azb("taxa efetiva") + " e a " + azb("taxa natural") + " (crescimento da força de trabalho mais o "
            "progresso técnico). Coincidirem é acaso: daí o " + azb("“fio da navalha”") + " — instabilidade que "
            + oc("Solow") + " eliminou ao permitir substituição entre capital e trabalho.",
            "Na economia do desenvolvimento, a fórmula fundamentou os cálculos de poupança necessária e o "
            + azb("modelo de dois hiatos") + " (poupança e divisas).",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A banca escreveu “produto médio do capital” em vez "
                       "da forma usual “relação capital-produto”, que entra no <b>denominador</b>. Quem decorou "
                       "g = s/v e não inverteu a razão marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Harrod-Domar, a taxa de crescimento aumenta com a relação capital-produto.”</i> → "
            "ERRADO (inversão: v está no denominador)",
            "<i>“Uma economia que poupa 24% da renda, com relação capital-produto igual a 3, cresce 8% ao "
            "ano.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "g = s/v, com v = relação capital-produto (inverso do produto médio do capital); "
                            "logo g = s × (Y/K) cresce com s e com Y/K. Imagem da fonte: ΔY/Y = σ·s − δ.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 479", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (fórmula transcrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01656
    {
        "id": "ECO-E2-L01656-1", "fonte_ref": "E2-L01656", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_CRESC,
        "rotulo_item": "Item",
        "assertiva": ("Na teoria de Schumpeter, as inovações são fundamentais para se compreender o "
                      "desenvolvimento econômico, ao contrário dos modelos de crescimento endógeno, que não levam "
                      "em conta tais inovações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na teoria de Schumpeter, as inovações são fundamentais para se compreender o "
                       "desenvolvimento econômico, ") + vm("ao contrário dos") + az(" modelos de crescimento "
                                                                                  "endógeno, que ")
                    + vm("não levam") + az(" em conta tais inovações.")),
        "poucas": ("A 1ª parte está certa; a 2ª inverte tudo: os modelos de " + azb("crescimento endógeno")
                   + " existem justamente para explicar a inovação por dentro do modelo — alguns até formalizam "
                   "a destruição criadora de Schumpeter."),
        "destrinchando": [
            oc("Schumpeter") + " (" + oc("Teoria do Desenvolvimento Econômico") + ", " + vd("1911") + ") põe o "
            "empresário inovador e suas “novas combinações” no centro do desenvolvimento; em " + vd("1942")
            + " cunha a " + azb("destruição criadora") + ".",
            "Os modelos endógenos endogeneizam o progresso técnico: inovação resulta de decisões econômicas "
            "(investir em P&D, estudar, aprender fazendo). Em " + oc("Romer") + " (" + vd("1990") + "), a "
            "inovação amplia a variedade de bens; em " + oc("Aghion e Howitt") + " (" + vd("1992") + "), cada "
            "inovação melhora a qualidade e torna obsoleta a anterior — é o chamado " + azb("crescimento "
            "schumpeteriano") + ".",
            "O modelo que <b>não</b> explica a inovação é o de " + oc("Solow") + " (" + vd("1956") + "): nele o "
            "progresso técnico é exógeno, um resíduo — o " + azb("resíduo de Solow") + ", que mede a parte do "
            "crescimento não explicada pela acumulação de fatores.",
            vm("Regra-âncora: exógeno = Solow; endógeno = inovação explicada pelo modelo."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 1ª oração (Schumpeter e inovação) é isca verdadeira; "
                       "o “ao contrário” cria uma oposição falsa e atribui aos modelos endógenos a característica "
                       "do modelo de Solow. Pista: “endógeno” quer dizer explicado dentro do modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…ao contrário do modelo de Solow, que trata o progresso técnico como exógeno.”</i> → CERTO",
            "<i>“O modelo de Aghion e Howitt rejeita a ideia schumpeteriana de destruição criadora.”</i> → "
            "ERRADO (inversão: ele a formaliza)",
        ])],
        "reescrita": ("Na teoria de Schumpeter, as inovações são fundamentais para se compreender o "
                      "desenvolvimento econômico, " + hl("assim como os") + " modelos de crescimento endógeno, "
                      "que " + hl("também levam") + " em conta tais inovações."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["ao contrário"], "dificuldade": 1,
        "comentario_fonte": "1ª parte correta (Schumpeter, destruição criadora); 2ª errada: os modelos endógenos "
                            "(Romer, Lucas, Aghion-Howitt) endogeneizam inovação e progresso técnico.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00448
    {
        "id": "ECO-E3-L00448-1", "fonte_ref": "E3-L00448", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Os modelos de crescimento endógeno consideram o volume de poupança externa entrando no "
                      "país como o promotor fundamental de seu crescimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os modelos de crescimento endógeno consideram ") + vm("o volume de poupança externa "
                                                                             "entrando no país")
                    + az(" como o promotor fundamental de seu crescimento.")),
        "poucas": ("O motor dos modelos endógenos é " + azb("interno") + ": capital humano, conhecimento, P&D, "
                   "aprendizado e transbordamentos. Esses modelos nem sequer distinguem poupança externa de "
                   "interna."),
        "destrinchando": [
            "“Endógeno” significa que o crescimento de longo prazo é explicado por variáveis decididas dentro do "
            "sistema econômico: investimento em " + azb("capital humano") + " (" + oc("Lucas") + ", "
            + vd("1988") + "), em " + azb("P&D") + " (" + oc("Romer") + ", " + vd("1990") + "; "
            + oc("Aghion e Howitt") + ", " + vd("1992") + "), " + azb("learning by doing") + " e externalidades "
            "de conhecimento (" + oc("Arrow") + ", " + vd("1962") + "; " + oc("Romer") + ", " + vd("1986") + ").",
            "A poupança importa em alguns deles — no " + azb("modelo AK") + ", g = sA − (n + δ), e mais poupança "
            "eleva a taxa de crescimento para sempre —, mas não há hipótese alguma sobre a <b>origem</b> dessa "
            "poupança.",
            "A ideia de poupança externa como motor do crescimento vem de outra tradição: os modelos de "
            + azb("hiato") + " (" + oc("Chenery e Strout") + ", " + vd("1966") + "), que somam ao hiato de "
            "poupança o de divisas. No " + rx("Brasil") + ", a estratégia de “crescimento com poupança externa” "
            "é criticada por " + oc("Bresser-Pereira") + ", para quem déficits em conta corrente apreciam o "
            "câmbio e substituem a poupança interna em vez de somar-se a ela.",
            vm("Regra-âncora: crescimento endógeno = ideias e qualificações produzidas dentro da economia."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca o motor do crescimento endógeno por um conceito de "
                       "outra literatura (poupança externa, dos modelos de hiato). Pista: nada em “endógeno” "
                       "remete a fluxo vindo de fora do país."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo AK, a taxa de poupança afeta a taxa de crescimento de longo prazo.”</i> → CERTO",
            "<i>“Os modelos de crescimento endógeno atribuem o crescimento de longo prazo a um progresso "
            "técnico exógeno.”</i> → ERRADO (troca de conceito: isso é Solow)",
        ])],
        "reescrita": ("Os modelos de crescimento endógeno consideram " + hl("a acumulação de capital humano e de "
                                                                            "conhecimento")
                      + " como o promotor fundamental de seu crescimento."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["fundamental"], "dificuldade": 1,
        "comentario_fonte": "O pilar do crescimento endógeno não é a poupança externa, e sim spillovers, P&D, "
                            "capital humano e learning by doing; esses modelos não definem a origem da poupança "
                            "(quatro comentários convergentes; IMAGEM 649 com o comentário da professora).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 649", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00449
    {
        "id": "ECO-E3-L00449-1", "fonte_ref": "E3-L00449", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Os modelos de crescimento endógeno consideram a explicação do processo de acumulação de "
                      "capital humano e de conhecimento como parte do modelo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os modelos de crescimento endógeno consideram a explicação do processo de acumulação de "
                      "capital humano e de conhecimento <u>como parte do modelo</u>."),
        "poucas": ("É o que os torna " + azb("endógenos") + ": a acumulação de qualificações e de ideias resulta "
                   "de decisões dos agentes, modeladas explicitamente, e não de uma taxa dada de fora."),
        "destrinchando": [
            "Em " + oc("Solow") + ", a tecnologia A cresce a uma taxa g que “cai do céu”. Os modelos endógenos "
            "escrevem equações para o próprio processo de acumulação, a partir de escolhas otimizadoras.",
            oc("Lucas") + " (" + vd("1988") + "): a taxa de acumulação de " + azb("capital humano") + " depende "
            "do tempo que as pessoas dedicam a adquirir qualificações em vez de produzir.",
            oc("Romer") + " (" + vd("1990") + "): um " + azb("setor de P&D") + " usa capital humano e o estoque "
            "de ideias para gerar novas ideias; como o conhecimento é não rival, a produção de ideias não "
            "esbarra em rendimentos decrescentes. " + oc("Arrow") + " (" + vd("1962") + ") antecipou o canal "
            "do " + azb("learning by doing") + ".",
            "Daí a agenda de política: educação, ciência e inovação alteram a taxa de crescimento de longo "
            "prazo e ajudam a explicar por que as rendas dos países <b>não</b> convergem automaticamente.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Reescreve a definição de crescimento endógeno com vocabulário "
                       "formal (“explicação… como parte do modelo” = endogeneização). Não há modulador nem "
                       "troca de agente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os modelos de crescimento endógeno tomam a acumulação de conhecimento como dada, fora do "
            "modelo.”</i> → ERRADO (inversão: isso é exógeno)",
            "<i>“No modelo de Lucas, a acumulação de capital humano depende do tempo dedicado à "
            "qualificação.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Exemplos: Romer (P&D) e Lucas (capital humano pelo tempo dedicado às qualificações); "
                            "os modelos endógenos incorporam a acumulação de capital humano e conhecimento como "
                            "resultado de decisões otimizadoras (IMAGEM 650 + quatro comentários convergentes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 650", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0722
    {
        "id": "ECO-E1-0722-1", "fonte_ref": "E1-0722", "destino": "58", "subtema": H2["desenv"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": True,
        "comando": CMD_DESENV,
        "rotulo_item": "Item",
        "assertiva": ("Segundo neoinstitucionalistas como Douglass North, as instituições, entendidas como as "
                      "regras do jogo de uma sociedade, são o principal elemento responsável pelo aumento do nível "
                      "de renda nos últimos séculos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo neoinstitucionalistas como Douglass North, as instituições, entendidas como as "
                      "<u>regras do jogo</u> de uma sociedade, são o <u>principal elemento</u> responsável pelo "
                      "aumento do nível de renda nos últimos séculos."),
        "poucas": ("É a tese da " + azb("Nova Economia Institucional") + ": para " + oc("North") + ", "
                   "instituições que protegem direitos de propriedade e reduzem custos de transação são a causa "
                   "fundamental do crescimento moderno."),
        "destrinchando": [
            oc("Douglass North") + " (" + oc("Institutions, Institutional Change and Economic Performance")
            + ", " + vd("1990") + "; Nobel de " + vd("1993") + ", com " + oc("Robert Fogel") + ") define "
            + azb("instituições") + " como as " + azb("regras do jogo") + ": restrições criadas pelos homens "
            "para estruturar a interação humana. Podem ser " + azb("formais") + " (constituições, leis, "
            "direitos de propriedade) ou " + azb("informais") + " (costumes, normas, códigos de conduta), "
            "mais os mecanismos de fazê-las cumprir.",
            "Distinção clássica: instituições são as regras; " + azb("organizações") + " (empresas, partidos, "
            "sindicatos) são os jogadores.",
            "Mecanismo: regras estáveis reduzem incerteza e " + azb("custos de transação") + " (" + oc("Coase")
            + ", " + oc("Williamson") + "), tornando rentável investir, especializar-se e trocar com "
            "desconhecidos. Com " + oc("Weingast") + " (" + vd("1989") + "), North liga a Revolução Gloriosa "
            "inglesa (" + vd("1688") + ") a compromissos críveis do Estado de respeitar a propriedade e as "
            "dívidas.",
            "A tese foi retomada por " + oc("Acemoglu e Robinson") + " (" + oc("Por que as nações fracassam")
            + ", " + vd("2012") + "), com a oposição entre instituições " + azb("inclusivas") + " e "
            + azb("extrativas") + ". Rivais: geografia (" + oc("Sachs") + "), preços relativos dos fatores ("
            + oc("Robert Allen") + "), cultura e conhecimento (" + oc("Mokyr") + ").",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item atribui a tese ao autor certo e com a definição "
                       "canônica (“regras do jogo”). O “principal elemento” parece exagero, mas é exatamente a "
                       "posição de North; o item seria falso se atribuísse a tese a todos os economistas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para North, as instituições restringem-se às regras formais, como leis e constituições.”</i> → "
            "ERRADO (restrição indevida: há também as informais)",
            "<i>“Para North, instituições e organizações são sinônimos.”</i> → ERRADO (troca de conceito: "
            "organizações são os jogadores)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["principal"], "dificuldade": 2,
        "comentario_fonte": "North, principal neoinstitucionalista: instituições sólidas (regras formais e "
                            "informais e seu enforcement) geram os incentivos ao progresso; cita Parlamento e "
                            "Judiciário protegendo a propriedade (vários comentários empilhados).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (232).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "cortada (imagem não preservada; o texto do verso basta)"},
                          {"ref": "image (235).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "cortada (imagem não preservada; o texto do verso basta)"}],
        "alertas": [AL_2022],
    },
    # ------------------------------------------------------------------ E1-0723
    {
        "id": "ECO-E1-0723-1", "fonte_ref": "E1-0723", "destino": "58", "subtema": H2["desenv"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": True,
        "comando": CMD_DESENV,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o economista Robert Allen, a Revolução Industrial e o consequente aumento do "
                      "nível de renda são principalmente causados pelos altos salários e pelo baixo preço da "
                      "energia, observados na Grã-Bretanha no final do século 18."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o economista Robert Allen, a Revolução Industrial e o consequente aumento do "
                      "nível de renda são principalmente causados pelos <u>altos salários</u> e pelo <u>baixo "
                      "preço da energia</u>, observados na Grã-Bretanha no final do século 18."),
        "poucas": ("É a tese da " + azb("economia de salários altos") + " de " + oc("Robert Allen") + ": "
                   "trabalho caro e carvão barato tornaram lucrativo inventar máquinas que poupavam trabalho e "
                   "consumiam energia — só na Grã-Bretanha."),
        "destrinchando": [
            "Em " + oc("The British Industrial Revolution in Global Perspective") + " (" + vd("2009") + "), "
            + oc("Allen") + " compara salários, preços do capital e da energia em várias cidades da Europa e da "
            "Ásia. A Grã-Bretanha tinha " + azb("salário alto em relação ao custo do capital") + " e "
            + azb("energia barata") + " (carvão abundante e acessível).",
            "Mecanismo de " + azb("preços relativos dos fatores") + " (inovação induzida): a máquina de fiar ou a "
            "máquina a vapor de " + oc("Newcomen") + " só compensavam onde o trabalho economizado era caro e o "
            "carvão consumido, barato. Na China ou na Índia, com mão de obra barata, as mesmas invenções não "
            "pagariam o custo — por isso não surgiram lá primeiro.",
            "Depois, o aperfeiçoamento das máquinas reduziu custos e as tornou rentáveis também em outros países, "
            "difundindo a industrialização.",
            "Críticas: há quem conteste a medida dos salários britânicos (sobretudo de mulheres e crianças) e "
            "quem prefira explicações por cultura e conhecimento (" + oc("Mokyr") + ", “Iluminismo Industrial”) "
            "ou por instituições (" + oc("North") + "). Mas a pergunta é <b>o que Allen diz</b>, e a assertiva "
            "o descreve corretamente.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Contraria a intuição de que salários "
                       "<b>baixos</b> atraem indústria: em Allen, salário alto é incentivo à mecanização. O "
                       "“principalmente” é fiel à tese. Item de atribuição autor → tese: o recurso contra ele "
                       "não prosperou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Robert Allen, os baixos salários britânicos explicam o pioneirismo industrial da "
            "Grã-Bretanha.”</i> → ERRADO (inversão: eram altos)",
            "<i>“Para Allen, a energia cara estimulou a invenção de máquinas poupadoras de carvão.”</i> → ERRADO "
            "(dado alterado: a energia era barata)",
        ]), ("🃏 Carta na manga", [
            "Allen ilustra a ideia de que tecnologia responde a incentivos de preços: argumento útil para "
            "discutir por que políticas de inovação precisam considerar a dotação de fatores de cada país.",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["principalmente"], "dificuldade": 2,
        "comentario_fonte": "Allen (The High Wage Economy and the Industrial Revolution; The British Industrial "
                            "Revolution in Global Perspective, 2009): salários altos e capital e energia baratos "
                            "induziram tecnologias poupadoras de trabalho; recursos indeferidos pela banca.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (234).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "cortada (imagem não preservada; o texto do verso basta)"}],
        "alertas": [AL_2022],
    },
    # ------------------------------------------------------------------ E1-0724
    {
        "id": "ECO-E1-0724-1", "fonte_ref": "E1-0724", "destino": "58", "subtema": H2["desenv"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_DESENV,
        "rotulo_item": "Item",
        "assertiva": ("Economistas como Jeffrey Sachs atribuem a fatores geográficos, como a propensão à "
                      "incidência de malária, uma contribuição substantiva para as diferentes trajetórias de "
                      "crescimento e a presença de armadilhas de pobreza."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Economistas como Jeffrey Sachs atribuem a <u>fatores geográficos</u>, como a propensão à "
                      "incidência de malária, uma contribuição <u>substantiva</u> para as diferentes trajetórias de "
                      "crescimento e a presença de armadilhas de pobreza."),
        "poucas": (oc("Jeffrey Sachs") + " é o principal nome da " + azb("hipótese geográfica") + ": clima "
                   "tropical, doenças como a malária, isolamento e custos de transporte ajudam a prender países "
                   "em " + azb("armadilhas de pobreza") + "."),
        "destrinchando": [
            "Em trabalhos com " + oc("John Gallup") + " e " + oc("Andrew Mellinger") + " (fim dos anos 1990), "
            "Sachs mostra que países tropicais, sem litoral ou longe dos grandes mercados tendem a crescer menos: "
            "transporte caro, solos frágeis e " + azb("doenças endêmicas") + " — a malária reduz a produtividade, "
            "a escolaridade e o investimento estrangeiro.",
            "Em " + oc("O Fim da Pobreza") + " (" + vd("2005") + "), a " + azb("armadilha da pobreza") + " é a "
            "situação em que a renda mal cobre a subsistência: sem poupança, não há investimento em saúde, "
            "infraestrutura e capital humano, e a pobreza se reproduz. A saída proposta é um "
            + azb("grande impulso") + " de ajuda externa (meta de " + vd("0,7% do PIB") + " dos países ricos), "
            "lembrando o círculo vicioso de " + oc("Myrdal") + " e o big push de " + oc("Rosenstein-Rodan") + ".",
            "Contraponto institucionalista: " + oc("Acemoglu, Johnson e Robinson") + " (" + vd("2001") + ") "
            "argumentam que a geografia age sobretudo <b>pelas instituições</b>: onde a mortalidade dos colonos "
            "era alta, os europeus montaram instituições extrativas. " + oc("Easterly") + " critica a "
            "eficácia da ajuda massiva.",
            "Para o item, basta a atribuição: Sachs dá à geografia uma contribuição “substantiva”, não exclusiva.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Atribuição autor → tese correta, com "
                       "moduladores prudentes (“contribuição substantiva”, não “causa única”). A versão ERRADA "
                       "trocaria o autor (Acemoglu) ou absolutizaria (“determinam inteiramente”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Acemoglu, Johnson e Robinson sustentam que a geografia é a causa direta e principal das "
            "diferenças de renda entre países.”</i> → ERRADO (troca de ator: para eles, a geografia age pelas "
            "instituições)",
            "<i>“Para Sachs, as armadilhas de pobreza podem ser superadas sem qualquer ajuda externa, apenas "
            "pela poupança doméstica.”</i> → ERRADO (contradição: ele defende o grande impulso de ajuda)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["substantiva"], "dificuldade": 1,
        "comentario_fonte": "Sachs lista oito problemas estruturais (fiscal, geopolítica, falhas de governo, falta "
                            "de inovação, demografia, cultura, geografia — malária —, armadilha da pobreza); O Fim "
                            "da Pobreza; armadilha lembra o círculo vicioso de Myrdal.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (233).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "cortada (imagem não preservada; o texto do verso basta)"},
                          {"ref": "image (239).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "cortada (imagem não preservada; o texto do verso basta)"},
                          {"ref": "image (236).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "cortada (imagem não preservada; o texto do verso basta)"}],
        "alertas": [AL_2022],
    },
    # ------------------------------------------------------------------ E1-0490
    {
        "id": "ECO-E1-0490-1", "fonte_ref": "E1-0490", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False,
        "errei": False,
        "comando": CMD_TRAB,
        "rotulo_item": "Item",
        "assertiva": ("Em decorrência da metodologia utilizada pelo IBGE, é possível que haja diminuição do número "
                      "de desocupados durante conjuntura econômica recessiva."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em decorrência da metodologia utilizada pelo IBGE, <u>é possível</u> que haja diminuição do "
                      "número de desocupados durante conjuntura econômica recessiva."),
        "poucas": ("Para o IBGE, só é " + azb("desocupado") + " quem procurou trabalho. Na recessão, parte dos "
                   "sem-emprego desiste de procurar (" + azb("desalento") + ") e sai da força de trabalho: o "
                   "número de desocupados pode cair sem que ninguém tenha sido contratado."),
        "destrinchando": [
            "Na " + rx("PNAD Contínua") + ", a pessoa em idade de trabalhar (" + vd("14 anos ou mais") + ") é: "
            + azb("ocupada") + " (trabalhou ao menos 1 hora na semana de referência); " + azb("desocupada")
            + " (não trabalhou, tomou providência efetiva para conseguir trabalho nos " + vd("30 dias") + " "
            "anteriores e estava disponível); ou " + azb("fora da força de trabalho") + " (nenhuma das duas).",
            vd("Taxa de desocupação = desocupados ÷ (ocupados + desocupados)") + ". Quem para de procurar sai "
            "do numerador <b>e</b> do denominador.",
            azb("Desalentado") + ": queria trabalhar e estava disponível, mas não procurou por achar que não "
            "encontraria (falta de vaga na localidade, idade, falta de experiência). Fica fora da força de "
            "trabalho e não conta como desocupado.",
            "Por isso, em recessões longas, o desemprego aberto pode subestimar a deterioração. O IBGE publica a "
            + azb("taxa composta de subutilização") + ", que soma aos desocupados os subocupados por "
            "insuficiência de horas e a " + azb("força de trabalho potencial") + " (inclui os desalentados).",
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Parece absurdo (recessão reduzindo "
                       "desocupados), mas o “é possível” e a referência à metodologia apontam para o efeito "
                       "estatístico do desalento. 🔥 Tema recorrente: desocupado exige procura."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela metodologia do IBGE, os desalentados são contabilizados entre os desocupados.”</i> → "
            "ERRADO (troca de conceito: estão fora da força de trabalho)",
            "<i>“O aumento do desalento tende a reduzir a taxa de participação na força de trabalho.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["é possível"], "dificuldade": 2,
        "comentario_fonte": "As pessoas desistem de procurar emprego e saem da força de trabalho; com a base "
                            "menor, há efeito estatístico de queda do desemprego.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [AL_2016],
    },
    # ------------------------------------------------------------------ E1-0492
    {
        "id": "ECO-E1-0492-1", "fonte_ref": "E1-0492", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False,
        "errei": True,
        "comando": CMD_DESEMP,
        "rotulo_item": "Item",
        "assertiva": ("As causas do desemprego natural, decorrente do tempo necessário para que o mercado de "
                      "trabalho se ajuste, incluem a desinformação e a falta de mobilidade dos agentes que ofertam "
                      "e buscam trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("As causas do desemprego natural, decorrente do tempo necessário para que o mercado de "
                       "trabalho se ajuste, incluem ") + vm("a desinformação e a falta de mobilidade dos agentes "
                                                            "que ofertam e buscam trabalho") + az(".")),
        "poucas": ("Gabarito ERRADO pela leitura de que o desemprego natural (friccional) decorre da "
                   + azb("mobilidade") + " — da troca de empregos —, e não da falta dela. Leitura frágil: ver ⚠️."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "mantido o ERRADO da fonte. Pelos manuais (" + oc("Mankiw") + ", " + oc("Blanchard")
                          + "), o " + azb("desemprego friccional") + " — componente da taxa natural — existe "
                          "porque a informação sobre vagas e candidatos é imperfeita e a realocação entre setores "
                          "e regiões leva tempo; a baixa mobilidade geográfica e de qualificações alimenta o "
                          + azb("estrutural") + ", também parte da taxa natural. Nessa leitura, o item seria "
                          "defensável como CERTO. A justificativa usual do ERRADO confunde a mobilidade, que gera "
                          "rotatividade, com a fricção, que é a demora e o custo dessa mobilidade.")],
        "destrinchando": [
            "A " + azb("taxa natural de desemprego") + " (" + oc("Friedman") + ", " + vd("1968") + ") é a que "
            "prevalece com o mercado em equilíbrio de longo prazo, sem pressão sobre a inflação. Compõe-se do "
            + azb("friccional") + " e do " + azb("estrutural") + " (na leitura clássica, também do voluntário); "
            "o " + azb("cíclico") + " é o desvio em relação a ela.",
            "Friccional: tempo de busca e de casamento entre trabalhador e vaga (recém-formados, quem troca de "
            "emprego). Estrutural: descompasso persistente de qualificações, setores ou regiões, ou salário "
            "acima do equilíbrio (salário mínimo, sindicatos, salário-eficiência).",
            "A taxa natural cai com políticas que encurtam a busca (agências de emprego, intermediação, "
            "requalificação) e sobe com benefícios generosos que alongam a procura (seguro-desemprego).",
            "Os comentários de origem dão duas justificativas para o ERRADO: (1) o friccional decorre da "
            "<b>presença</b> de mobilidade; (2) desinformação e baixa mobilidade explicariam desvios em relação "
            "à taxa natural (desemprego de curto prazo). Nenhuma delas é a leitura padrão dos manuais.",
        ],
        "dissecando": (cz("[outro: gabarito por leitura restritiva]") + " A banca construiu o item com as causas "
                       "de manual do friccional e o considerou falso, ao que tudo indica, pela ideia de que o "
                       "friccional nasce da mobilidade dos trabalhadores. Em prova, guarde as duas coisas: "
                       "a rotatividade gera o friccional; desinformação e baixa mobilidade o prolongam."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O desemprego friccional decorre da rotatividade dos trabalhadores entre empregos e integra a "
            "taxa natural de desemprego.”</i> → CERTO",
            "<i>“A taxa natural de desemprego inclui o desemprego cíclico.”</i> → ERRADO (troca de conceito: "
            "o cíclico é o desvio em relação à taxa natural)",
        ])],
        "reescrita": ("As causas do desemprego natural, decorrente do tempo necessário para que o mercado de "
                      "trabalho se ajuste, incluem " + hl("a rotatividade normal entre empregos e o descompasso "
                                                         "entre as qualificações dos trabalhadores e as "
                                                         "exigências das vagas") + "."),
        "tipo_erro": ["OUTRO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": "Comentários divergentes: natural ligado a fatores institucionais e tecnológicos, e "
                            "desinformação/baixa mobilidade aos desvios; ou friccional decorrente da presença de "
                            "mobilidade, não da falta dela.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [AL_2016,
                    "contestavel: gabarito ERRADO mantido; pelos manuais, informação imperfeita e baixa mobilidade "
                    "são causas clássicas dos desempregos friccional e estrutural, componentes da taxa natural — "
                    "o item seria defensável como CERTO"],
    },
    # ------------------------------------------------------------------ E1-0493
    {
        "id": "ECO-E1-0493-1", "fonte_ref": "E1-0493", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False,
        "errei": True,
        "comando": CMD_TRAB,
        "rotulo_item": "Item",
        "assertiva": ("Uma das principais diferenças entre a Pesquisa Mensal de Emprego (PME) e a Pesquisa "
                      "Nacional por Amostra de Domicílios Contínua (PNAD-Contínua) – pesquisas periódicas sobre "
                      "mercado de trabalho no Brasil realizadas pelo IBGE – reside no fato de a PNAD-Contínua ser "
                      "mais abrangente do ponto de vista geográfico que a PME."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma das principais diferenças entre a Pesquisa Mensal de Emprego (PME) e a Pesquisa "
                      "Nacional por Amostra de Domicílios Contínua (PNAD-Contínua) – pesquisas periódicas sobre "
                      "mercado de trabalho no Brasil realizadas pelo IBGE – reside no fato de a PNAD-Contínua ser "
                      "<u>mais abrangente do ponto de vista geográfico</u> que a PME."),
        "poucas": ("A " + rx("PME") + " cobria só " + vd("6 regiões metropolitanas") + "; a " + rx("PNAD Contínua")
                   + " tem amostra " + azb("nacional") + ", com cerca de " + vd("3.500 municípios") + " de todas "
                   "as unidades da federação."),
        "destrinchando": [
            rx("PME") + ": pesquisa mensal das regiões metropolitanas de Recife, Salvador, Belo Horizonte, Rio "
            "de Janeiro, São Paulo e Porto Alegre. Retratava o mercado de trabalho urbano e metropolitano e foi "
            "encerrada em " + vd("2016") + ".",
            rx("PNAD Contínua") + ": iniciada em " + vd("2012") + ", visita cerca de " + vd("211 mil domicílios")
            + " por trimestre, em todo o território; divulga resultados mensais em " + azb("trimestres móveis")
            + " e trimestrais, com recortes por UF, capitais e regiões metropolitanas. Substituiu a PME e a PNAD "
            "anual.",
            "Outras diferenças: idade de trabalhar de " + vd("14 anos") + " na PNAD Contínua (" + vd("10 anos")
            + " na PME); temas mais amplos (rendimentos de todas as fontes, trabalho infantil, afazeres "
            "domésticos, subutilização). Por isso as taxas das duas pesquisas não são diretamente comparáveis.",
            "Consequência analítica: a PME, restrita às metrópoles, captava mal o mercado de trabalho das "
            "regiões Norte, Nordeste e Centro-Oeste e o interior, onde a informalidade e a ocupação agrícola "
            "pesam mais.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de conhecimento institucional sobre as pesquisas do IBGE: o "
                       "nome “Nacional” já indica a cobertura. A versão ERRADA inverteria a abrangência ou "
                       "trocaria a diferença (periodicidade, idade de trabalhar)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A PME, por abranger todas as unidades da federação, era mais representativa que a PNAD "
            "Contínua.”</i> → ERRADO (inversão: a PME cobria só seis regiões metropolitanas)",
            "<i>“A PNAD Contínua divulga mensalmente taxas de desocupação referentes a trimestres móveis.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas “Correto.”, sem justificativa.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [AL_2016],
    },
    # ------------------------------------------------------------------ E1-0494
    {
        "id": "ECO-E1-0494-1", "fonte_ref": "E1-0494", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": CMD_DESEMP,
        "rotulo_item": "Item",
        "assertiva": ("Um indivíduo que trabalhava em determinado banco pediu demissão do emprego, a fim de estudar "
                      "para um concurso de seu estado; nesse caso, ele seria incluído na categoria do desemprego "
                      "natural."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um indivíduo que trabalhava em determinado banco <u>pediu demissão</u> do emprego, a fim de "
                      "estudar para um concurso de seu estado; nesse caso, ele seria incluído na categoria do "
                      "<u>desemprego natural</u>."),
        "poucas": ("Quem sai do emprego por escolha está em " + azb("desemprego voluntário") + " — que, junto com "
                   "o friccional, compõe o " + azb("desemprego natural") + ", e não o cíclico ou involuntário."),
        "destrinchando": [
            "Na teoria, o desemprego se divide em " + azb("voluntário") + " (não aceita trabalhar ao salário "
            "vigente ou prefere outra atividade), " + azb("friccional") + " (transição entre empregos), "
            + azb("estrutural") + " (descompasso de qualificações ou setores) e " + azb("cíclico") + " "
            "(involuntário, por falta de demanda agregada).",
            "A " + azb("taxa natural") + " reúne os componentes que existem mesmo com a economia no pleno "
            "emprego. Na formulação de " + oc("Friedman") + " e na tradição clássica, o voluntário e o "
            "friccional; nos manuais modernos, o friccional e o estrutural. Em qualquer versão, o caso do item "
            "não é cíclico: ninguém o demitiu por queda de demanda.",
            "Cuidado com a estatística: pelo critério do " + rx("IBGE") + ", se ele só estuda e não procura "
            "trabalho, fica " + azb("fora da força de trabalho") + " (não é desocupado). O item fala da "
            "categoria teórica, não da classificação da PNAD.",
            vm("Regra-âncora: saiu por escolha ou está trocando de emprego → natural; foi demitido pela "
               "recessão → cíclico."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O “pediu demissão” é a pista do caráter voluntário. "
                       "A dúvida está em saber se o voluntário integra a taxa natural — integra, na tradição "
                       "clássica e friedmaniana."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um bancário demitido porque a recessão reduziu a demanda por crédito integra o desemprego "
            "natural.”</i> → ERRADO (troca de conceito: é desemprego cíclico)",
            "<i>“Pelo critério do IBGE, quem deixa o emprego para só estudar, sem procurar trabalho, é "
            "classificado como desocupado.”</i> → ERRADO (troca de conceito: fica fora da força de trabalho)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Ele seria incluído entre os desocupados; teoricamente, compatível com o desemprego "
                            "voluntário.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [AL_2020,
                    "qualidade_fonte: o comentário de origem o inclui “entre os desocupados”; pelo critério do "
                    "IBGE, sem procura de trabalho ele fica fora da força de trabalho"],
    },
    # ------------------------------------------------------------------ E1-0495
    {
        "id": "ECO-E1-0495-1", "fonte_ref": "E1-0495", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": CMD_TRAB,
        "rotulo_item": "Item",
        "assertiva": ("Um diplomata do Ministério de Relações Exteriores é considerado como ocupado, entre as "
                      "pessoas na força de trabalho, ainda que não tenha carteira assinada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um diplomata do Ministério de Relações Exteriores é considerado como <u>ocupado</u>, entre "
                      "as pessoas na força de trabalho, <u>ainda que não tenha carteira assinada</u>."),
        "poucas": ("Ocupação não depende de carteira: o diplomata é " + azb("servidor estatutário") + " e entra "
                   "entre os ocupados na posição de " + azb("empregado no setor público") + "."),
        "destrinchando": [
            "Para o " + rx("IBGE") + " (PNAD Contínua), " + azb("ocupado") + " é quem trabalhou ao menos "
            + vd("1 hora") + " na semana de referência em atividade remunerada (em dinheiro, produtos ou "
            "benefícios) ou sem remuneração em ajuda a familiar — ou estava temporariamente afastado.",
            "Posições na ocupação: " + azb("empregado") + " no setor privado (com ou sem carteira), "
            "trabalhador doméstico, " + azb("empregado no setor público") + " (com carteira, sem carteira ou "
            + azb("militar e servidor estatutário") + "), empregador, conta própria e trabalhador familiar "
            "auxiliar.",
            "Diplomatas são servidores de carreira, regidos pelo regime jurídico único (" + vd("Lei 8.112/1990")
            + ") e pela lei do Serviço Exterior (" + vd("Lei 11.440/2006") + "): não têm carteira porque não são "
            "regidos pela CLT, e não por informalidade.",
            "Carteira assinada importa para medir " + azb("informalidade") + " (empregado sem carteira, conta "
            "própria sem CNPJ etc.), não para separar ocupados de desocupados.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " A banca aposta na confusão entre “ter carteira” e "
                       "“estar ocupado”. O “ainda que” convida a pensar em exceção; não há: o critério de "
                       "ocupação é ter trabalhado, não o vínculo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Trabalhadores por conta própria, por não terem vínculo empregatício, são classificados como "
            "desocupados.”</i> → ERRADO (troca de conceito: são ocupados)",
            "<i>“O servidor estatutário é classificado entre os empregados sem carteira no setor público, "
            "compondo a informalidade.”</i> → ERRADO (troca de conceito: categoria própria, formal)",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["ainda que"], "dificuldade": 1,
        "comentario_fonte": "A ocupação admite diversos vínculos; o diplomata, concursado em carreira de Estado, "
                            "figura entre os ocupados no setor público.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [AL_2020],
    },
    # ------------------------------------------------------------------ E1-0496
    {
        "id": "ECO-E1-0496-1", "fonte_ref": "E1-0496", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": CMD_DESEMP,
        "rotulo_item": "Item",
        "assertiva": ("Políticas de salário mínimo acima do nível de equilíbrio contribuem para o aumento do "
                      "desemprego voluntário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Políticas de salário mínimo acima do nível de equilíbrio contribuem para o aumento do "
                       "desemprego ") + vm("voluntário") + az(".")),
        "poucas": ("Com o salário mínimo acima do equilíbrio, há gente disposta a trabalhar pelo salário vigente "
                   "sem encontrar vaga: o desemprego criado é " + azb("involuntário") + "."),
        "destrinchando": [
            "No modelo competitivo, o salário mínimo é um " + azb("preço mínimo") + " do trabalho. Só tem "
            "efeito se " + vd("w mín > w*") + ": a esse salário, as firmas contratam menos (demanda) e mais "
            "pessoas querem trabalhar (oferta). O excesso de oferta de trabalho é desemprego.",
            azb("Desemprego voluntário") + ": a pessoa não aceita trabalhar ao salário vigente (prefere lazer, "
            "estudo, esperar oferta melhor). " + azb("Involuntário") + ": aceitaria o salário vigente — ou até "
            "menos —, mas não há vaga. Os desempregados do salário mínimo querem trabalhar a w mín e não "
            "conseguem.",
            "O salário mínimo é um dos fatores de " + azb("rigidez salarial") + " que explicam o desemprego "
            "estrutural (ao lado de sindicatos e do salário-eficiência), segundo " + oc("Mankiw") + ".",
            "Ressalva empírica: " + oc("Card e Krueger") + " (" + vd("1994") + ", Nova Jersey × Pensilvânia) não "
            "encontraram queda de emprego após aumento do mínimo; em mercados com " + azb("monopsônio") + ", um "
            "mínimo moderado pode até elevar o emprego. O efeito depende de quão acima do equilíbrio o mínimo "
            "é fixado.",
        ],
        "grafico_verso": "ECO-E1-0496-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O mecanismo (salário mínimo vinculante gera desemprego) "
                       "está certo; o erro está só no adjetivo. Pergunta-teste: o desempregado aceitaria "
                       "trabalhar pelo salário vigente? Se sim, é involuntário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um salário mínimo fixado acima do equilíbrio gera excesso de oferta de trabalho.”</i> → CERTO",
            "<i>“Um salário mínimo fixado abaixo do equilíbrio eleva o desemprego involuntário.”</i> → ERRADO "
            "(abaixo do equilíbrio o mínimo não tem efeito)",
        ])],
        "reescrita": ("Políticas de salário mínimo acima do nível de equilíbrio contribuem para o aumento do "
                      "desemprego " + hl("involuntário") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Salário mínimo acima do equilíbrio: oferta de trabalho > demanda; excedente de mão "
                            "de obra com desemprego involuntário (Mankiw, Princípios de Microeconomia).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (163).png; b6c02ce0-…; image (160), (158), (161), (162).png",
                           "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0496-1-V1: gráfico de Mankiw do salário mínimo)"}],
        "alertas": [AL_2020],
    },
    # ------------------------------------------------------------------ E1-0497
    {
        "id": "ECO-E1-0497-1", "fonte_ref": "E1-0497", "destino": "59", "subtema": H2["okun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": CMD_OKUN,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a lei de Okun, se o produto interno bruto se mantiver sempre igual ao produto "
                      "potencial, a taxa de desemprego será igual a 0."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a lei de Okun, se o produto interno bruto se mantiver sempre igual ao "
                       "produto potencial, a taxa de desemprego será igual ") + vm("a 0") + az(".")),
        "poucas": ("Com o PIB no potencial, o desemprego fica na " + azb("taxa natural") + " — positiva, por "
                   "causa do friccional e do estrutural —, não em zero."),
        "destrinchando": [
            azb("Lei de Okun") + " (" + oc("Arthur Okun") + ", " + vd("1962") + "): relação empírica negativa "
            "entre hiato do produto e desemprego. Na forma de hiato: " + vd("(Y − Y*)/Y* = −β (u − uₙ)") + ", "
            "com β em torno de " + vd("2") + " nos EUA (Okun estimou cerca de 3).",
            "Se Y = Y* (hiato zero), o lado direito também zera: " + vd("u = uₙ") + ". O produto potencial é "
            "justamente o produzido quando o desemprego está na taxa natural.",
            "A " + azb("taxa natural") + " é positiva: sempre há gente trocando de emprego (friccional) e "
            "descompasso de qualificações (estrutural). Desemprego zero exigiria produto acima do potencial — e, "
            "pela curva de Phillips, inflação acelerando.",
            "Forma em variações (" + oc("Blanchard") + "): " + vd("Δu ≈ −0,4 (g − 3%)") + " para os EUA: o "
            "desemprego só cai se o PIB crescer acima da sua tendência.",
            vm("Regra-âncora: PIB = potencial ⇔ desemprego = taxa natural (> 0)."),
        ],
        "dissecando": (cz("[troca de conceito · dado alterado]") + " Confunde pleno emprego (desemprego na taxa "
                       "natural) com desemprego nulo. Pista: “sempre igual ao potencial” descreve hiato zero, "
                       "que corresponde a u = uₙ, nunca a u = 0."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela lei de Okun, se o produto se mantiver igual ao potencial, a taxa de desemprego tenderá à "
            "taxa natural.”</i> → CERTO",
            "<i>“Pela lei de Okun, qualquer crescimento positivo do PIB reduz a taxa de desemprego.”</i> → "
            "ERRADO (é preciso crescer acima da tendência)",
        ])],
        "reescrita": ("De acordo com a lei de Okun, se o produto interno bruto se mantiver sempre igual ao produto "
                      "potencial, a taxa de desemprego será igual " + hl("à taxa natural de desemprego") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "DADO_ALTERADO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Okun relaciona emprego e produto, mas não fixa um nível de desemprego nulo, que é "
                            "impossível dado o desemprego voluntário a cada nível de produto.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [AL_2020],
    },
    # ------------------------------------------------------------------ E1-0502
    {
        "id": "ECO-E1-0502-1", "fonte_ref": "E1-0502", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Clio", "prova": "Clio 04/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_CLIO,
        "rotulo_item": "Item",
        "assertiva": ("A redução da população desocupada em uma economia garante uma retração na taxa de "
                      "desocupação dessa economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A redução da população desocupada em uma economia ") + vm("garante")
                    + az(" uma retração na taxa de desocupação dessa economia.")),
        "poucas": ("A taxa é uma " + azb("razão") + ": " + vd("D ÷ (O + D)") + ". Se os ocupados caírem "
                   "proporcionalmente mais que os desocupados, a taxa sobe mesmo com menos desocupados."),
        "destrinchando": [
            vd("Taxa de desocupação = desocupados ÷ força de trabalho") + ", e força de trabalho = ocupados + "
            "desocupados (não a população em idade de trabalhar inteira).",
            "Exemplo: 90 ocupados e 10 desocupados → " + vd("10%") + ". Numa recessão, 30 ocupados perdem o "
            "emprego e, junto com 1 desocupado, desistem de procurar e saem da força de trabalho: ficam 60 "
            "ocupados e 9 desocupados → 9 ÷ 69 ≈ " + vd("13%") + ". Menos desocupados, taxa maior.",
            "O caso inverso também acontece: a população desocupada pode crescer e a taxa cair, se muita gente "
            "entrar na força de trabalho e for contratada (o denominador cresce mais).",
            "Por isso a análise do mercado de trabalho olha várias séries juntas: nível de ocupação "
            "(ocupados ÷ população em idade de trabalhar), " + azb("taxa de participação") + ", desalento e "
            + azb("subutilização") + ".",
            vm("Regra-âncora: número absoluto ≠ taxa; sempre confira o denominador."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " A direção “normal” (menos desocupados → taxa menor) é a "
                       "mais comum; o erro está no “garante”, que transforma tendência em certeza. 🔥 Itens de "
                       "taxa × nível absoluto são frequentes em estatísticas de trabalho."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Mantida constante a força de trabalho, a redução da população desocupada implica queda da "
            "taxa de desocupação.”</i> → CERTO",
            "<i>“A taxa de desocupação é a razão entre os desocupados e a população em idade de "
            "trabalhar.”</i> → ERRADO (denominador trocado: é a força de trabalho)",
        ])],
        "reescrita": ("A redução da população desocupada em uma economia " + hl("não garante")
                      + " uma retração na taxa de desocupação dessa economia."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["garante"], "dificuldade": 2,
        "comentario_fonte": "A taxa também depende da força de trabalho e da população ocupada; não há garantia "
                            "de queda.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem define a taxa como percentual da população em idade "
                    "de trabalhar (é da força de trabalho) e diz que a taxa sobe se a força crescer mais que os "
                    "ocupados — com desocupados em queda isso é impossível; o caso correto é a queda dos "
                    "ocupados proporcionalmente maior que a dos desocupados"],
    },
    # ------------------------------------------------------------------ E1-0504
    {
        "id": "ECO-E1-0504-1", "fonte_ref": "E1-0504", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Clio", "prova": "Clio 04/2022", "ano": 2022, "cacd": False, "errei": True,
        "comando": CMD_CLIO,
        "rotulo_item": "Item",
        "assertiva": ("A elevação da produtividade marginal do trabalho tende a reduzir a demanda por trabalho, uma "
                      "vez que agora cada trabalhador contribui com uma parcela maior do nível total de "
                      "produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A elevação da produtividade marginal do trabalho tende a ") + vm("reduzir")
                    + az(" a demanda por trabalho, uma vez que agora cada trabalhador contribui com uma parcela "
                         "maior do nível total de produção.")),
        "poucas": ("A demanda por trabalho " + azb("é") + " a curva do valor do produto marginal (P × PMgL). Se "
                   "cada trabalhador produz mais, contratá-lo rende mais: a demanda " + vd("aumenta") + "."),
        "destrinchando": [
            "A firma competitiva contrata até que o trabalhador adicional custe o que acrescenta à receita: "
            + vd("W = P × PMgL") + ", ou " + vd("W/P = PMgL") + ". A curva de demanda por trabalho é, portanto, "
            "a curva do " + azb("valor do produto marginal do trabalho") + ", decrescente pelos rendimentos "
            "marginais decrescentes.",
            "Com PMgL maior (melhor tecnologia, mais capital por trabalhador, trabalhadores mais qualificados), a "
            "cada salário a firma deseja mais trabalhadores: a curva se desloca para a " + vd("direita")
            + ", e o equilíbrio tem " + vd("mais emprego e salário real maior") + ".",
            "É o elo micro da ideia macro de que o " + azb("salário real acompanha a produtividade") + " no "
            "longo prazo.",
            "O raciocínio do item confunde produto marginal com necessidade de pessoal: “se cada um produz mais, "
            "preciso de menos gente” só vale com a produção total fixa. A firma maximiza lucro e expande a "
            "produção quando o trabalho fica mais rentável. Caso diferente é a inovação que " + azb("poupa "
            "trabalho") + " em certas tarefas — aí o PMgL desses trabalhadores cai, e não sobe.",
        ],
        "grafico_verso": "ECO-E1-0504-1-V1",
        "dissecando": (cz("[inversão · nexo indevido]") + " A justificativa do item é verdadeira (cada "
                       "trabalhador contribui mais), mas a conclusão é invertida. Pista: “contribui com uma "
                       "parcela maior” é razão para contratar mais, não menos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma queda do preço do produto, tudo o mais constante, reduz a demanda da firma por "
            "trabalho.”</i> → CERTO",
            "<i>“A demanda por trabalho da firma competitiva independe do preço do produto que ela vende.”</i> "
            "→ ERRADO (W = P × PMgL)",
        ])],
        "reescrita": ("A elevação da produtividade marginal do trabalho tende a " + hl("elevar") + " a demanda por "
                      "trabalho, uma vez que agora cada trabalhador contribui com uma parcela maior do nível total "
                      "de produção."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Comentário único e confuso: afirma que, na teoria clássica, maior PMgL eleva a "
                            "demanda por trabalho, mas que na neoclássica poderia reduzi-la, concluindo que a "
                            "afirmação “pode ser correta ou incorreta”.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem sugere que maior PMgL pode reduzir a demanda por "
                    "trabalho e não toma posição; a teoria neoclássica dá deslocamento para a direita"],
    },
    # ------------------------------------------------------------------ E1-0505
    {
        "id": "ECO-E1-0505-1", "fonte_ref": "E1-0505", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Clio", "prova": "Clio 04/2022", "ano": 2022, "cacd": False, "errei": True,
        "comando": CMD_CLIO,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de um salário mínimo em nível inferior ao salário de equilíbrio não terá efeito "
                      "sobre a alteração da taxa de desemprego dessa economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de um salário mínimo em nível <u>inferior</u> ao salário de equilíbrio "
                      "<u>não terá efeito</u> sobre a alteração da taxa de desemprego dessa economia."),
        "poucas": ("Um piso abaixo do equilíbrio " + azb("não é vinculante") + ": o mercado já paga mais que o "
                   "mínimo, e emprego e salário continuam em (L*, w*)."),
        "destrinchando": [
            "Salário mínimo é um " + azb("preço mínimo") + ": só “morde” se ficar " + vd("acima") + " do "
            "salário de equilíbrio. Abaixo dele, nenhuma firma é obrigada a mudar nada — ela já paga w* > w mín.",
            "Espelho: o " + azb("preço máximo") + " (teto) só tem efeito abaixo do equilíbrio. Piso alto gera "
            "excesso de oferta (desemprego); teto baixo gera excesso de demanda (escassez).",
            "Acima do equilíbrio, o mínimo gera desemprego " + azb("involuntário") + " (oferta de trabalho > "
            "demanda), o argumento clássico contra mínimos elevados.",
            "Na prática, o mercado de trabalho não tem um único salário: um mínimo pode ser não vinculante para "
            "uns segmentos e vinculante para outros (jovens, regiões mais pobres). No " + rx("Brasil") + ", "
            "estudos apontam ainda o " + azb("“efeito farol”") + ": o mínimo serve de referência até no "
            "mercado informal, onde não é obrigatório. O item, porém, é de modelo: um mercado, um equilíbrio.",
        ],
        "grafico_verso": "ECO-E1-0505-1-V1",
        "dissecando": (cz("[detalhe · contraintuitivo]") + " Quem associa automaticamente salário mínimo a "
                       "desemprego marca ERRADO. A palavra decisiva é “inferior”: piso abaixo do equilíbrio é "
                       "inócuo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um salário mínimo fixado abaixo do equilíbrio gera excesso de demanda por trabalho.”</i> → "
            "ERRADO (piso abaixo do equilíbrio é inócuo; excesso de demanda viria de um teto)",
            "<i>“Um salário mínimo fixado acima do equilíbrio gera desemprego involuntário.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Salário mínimo abaixo do equilíbrio não altera o desemprego; o mínimo afeta também "
                            "distribuição de renda, informalidade, inflação e consumo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: suprimido o “É correto afirmar que” repetido no início da citação do item"],
    },
    # ------------------------------------------------------------------ E1-0522
    {
        "id": "ECO-E1-0522-1", "fonte_ref": "E1-0522", "destino": "59", "subtema": H2["okun"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Ago/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_OKUN,
        "rotulo_item": "Item",
        "assertiva": ("A Lei de Okun estabelece uma relação empírica entre o crescimento econômico e a variação na "
                      "taxa de desemprego, sugerindo que um aumento no PIB é acompanhado por um aumento na taxa "
                      "de desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Lei de Okun estabelece uma relação empírica entre o crescimento econômico e a variação "
                       "na taxa de desemprego, sugerindo que um aumento no PIB é acompanhado por ")
                    + vm("um aumento") + az(" na taxa de desemprego.")),
        "poucas": ("A relação de " + oc("Okun") + " é " + azb("inversa") + ": crescimento do PIB (acima da "
                   "tendência) vem acompanhado de " + vd("queda") + " do desemprego."),
        "destrinchando": [
            oc("Arthur Okun") + " (" + vd("1962") + "), economista do Conselho de Assessores Econômicos de "
            "Kennedy, observou nos dados dos EUA que cada ponto percentual de desemprego acima do “pleno "
            "emprego” correspondia a cerca de " + vd("3%") + " de produto abaixo do potencial. Estimativas "
            "posteriores dão algo perto de " + vd("2 para 1") + ".",
            "Mecanismo: para produzir mais, as firmas contratam; para produzir menos, demitem. A relação é "
            "menor que 1 para 1 porque, no ajuste, também variam horas trabalhadas, produtividade e taxa de "
            "participação (firmas retêm mão de obra nas recessões; desalentados voltam na recuperação).",
            "Forma em variações: " + vd("Δu = −β (g − ḡ)") + ", em que ḡ é o crescimento do potencial. O "
            "primeiro item da assertiva — relação empírica entre crescimento e variação do desemprego — está "
            "certo; o sinal é que foi trocado.",
            "Usos: estimar o custo em produto da desinflação (taxa de sacrifício, junto com a curva de "
            "Phillips) e o efeito de recessões sobre o emprego.",
        ],
        "dissecando": (cz("[inversão]") + " Começa com uma definição correta (“relação empírica”) e troca o "
                       "sinal no final. Pista lógica: crescer exige mais trabalhadores, não menos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Lei de Okun é uma relação teórica exata, derivada da função de produção.”</i> → ERRADO "
            "(troca de conceito: é regularidade empírica, com coeficiente variável)",
            "<i>“Pela Lei de Okun, a redução do desemprego exige crescimento do produto superior ao do produto "
            "potencial.”</i> → CERTO",
        ])],
        "reescrita": ("A Lei de Okun estabelece uma relação empírica entre o crescimento econômico e a variação "
                      "na taxa de desemprego, sugerindo que um aumento no PIB é acompanhado por "
                      + hl("uma redução") + " na taxa de desemprego."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Okun: relação inversa entre crescimento do PIB e taxa de desemprego; ex.: 2% de "
                            "crescimento associado a 1 p.p. de queda do desemprego (dois comentários convergentes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0708-1 (mesma inversão do sinal da Lei de Okun, em outro simulado "
                    "da Clipping)"],
    },
    # ------------------------------------------------------------------ E1-0708
    {
        "id": "ECO-E1-0708-1", "fonte_ref": "E1-0708", "destino": "59", "subtema": H2["okun"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_OKUN,
        "rotulo_item": "Item",
        "assertiva": ("A Lei de Okun estabelece uma relação positiva entre crescimento econômico e desemprego: "
                      "quanto maior o crescimento do PIB, maior será o aumento da taxa de desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Lei de Okun estabelece uma relação ") + vm("positiva") + az(" entre crescimento "
                                                                                     "econômico e desemprego: "
                                                                                     "quanto maior o "
                                                                                     "crescimento do PIB, maior "
                                                                                     "será ")
                    + vm("o aumento") + az(" da taxa de desemprego.")),
        "poucas": ("A relação é " + azb("negativa") + ": quanto mais o PIB cresce acima do potencial, mais cai o "
                   "desemprego; crescimento fraco ou negativo o faz subir."),
        "destrinchando": [
            "Forma em variações: " + vd("Δu ≈ −β (g − ḡ)") + ". Com ḡ (crescimento do potencial) de 3% e "
            "β = 0,4 — ordem de grandeza de " + oc("Blanchard") + " para os EUA —, crescer " + vd("5%")
            + " reduz o desemprego em cerca de " + vd("0,8 p.p.") + ".",
            "Consequência pouco intuitiva: crescimento <b>positivo, mas abaixo do potencial</b> faz o desemprego "
            "<b>subir</b>, porque a produtividade e a força de trabalho continuam crescendo. É o caso das "
            "“recuperações sem emprego” (jobless recoveries).",
            "Forma em hiato: (Y − Y*)/Y* = −β′(u − uₙ): produto acima do potencial ⇔ desemprego abaixo da taxa "
            "natural.",
            "O coeficiente varia entre países e épocas: é maior onde a legislação facilita contratar e demitir "
            "(EUA) e menor onde as firmas ajustam horas e retêm mão de obra (Alemanha, Japão).",
            vm("Regra-âncora: Okun = sinal negativo entre crescimento (acima da tendência) e variação do "
               "desemprego."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sinal duas vezes, de forma coerente (“positiva” e “maior "
                       "aumento”), o que dá falsa consistência interna. Basta lembrar que crescer exige "
                       "contratar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um crescimento positivo do PIB, porém inferior ao do produto potencial, pode vir acompanhado "
            "de aumento do desemprego.”</i> → CERTO",
            "<i>“Pela Lei de Okun, a cada ponto de crescimento do PIB, o desemprego cai exatamente um ponto "
            "percentual.”</i> → ERRADO (dado alterado: a relação é menor que 1 para 1 e varia)",
        ])],
        "reescrita": ("A Lei de Okun estabelece uma relação " + hl("negativa") + " entre crescimento econômico e "
                      "desemprego: quanto maior o crescimento do PIB, maior será " + hl("a redução")
                      + " da taxa de desemprego."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["quanto maior"], "dificuldade": 1,
        "comentario_fonte": "Okun: relação inversa entre crescimento do produto e variação do desemprego; "
                            "crescimento acima do potencial reduz o desemprego, crescimento pífio ou negativo o "
                            "aumenta.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0522-1 (mesma inversão do sinal da Lei de Okun, em outro simulado "
                    "da Clipping)"],
    },
    # ------------------------------------------------------------------ E2-L00168
    {
        "id": "ECO-E2-L00168-1", "fonte_ref": "E2-L00168", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O desemprego sazonal ocorre quando existem variações na demanda de trabalho devido, por "
                      "exemplo, às estações do ano, e é mais comum em segmentos como a agricultura e a indústria, "
                      "onde a produção é altamente dependente das condições sazonais ou eventos programados "
                      "periodicamente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O desemprego sazonal ocorre quando existem variações na demanda de trabalho devido, por "
                      "exemplo, às <u>estações do ano</u>, e é mais comum em segmentos como a agricultura e a "
                      "indústria, onde a produção é altamente dependente das condições sazonais ou eventos "
                      "programados periodicamente."),
        "poucas": (azb("Desemprego sazonal") + " = oscilação previsível e recorrente da demanda por trabalho ao "
                   "longo do ano (safra e entressafra, alta temporada, datas comemorativas)."),
        "destrinchando": [
            "Exemplos clássicos: colheita de café, laranja e cana (agricultura); turismo de verão; comércio e "
            "indústria que contratam para o Natal e dispensam em janeiro; construção civil em regiões de "
            "inverno rigoroso.",
            "Diferenças: o " + azb("cíclico") + " acompanha recessões (irregular, ligado à demanda agregada); o "
            + azb("estrutural") + ", mudanças duradouras na economia; o " + azb("friccional") + ", a busca "
            "entre empregos. O sazonal se repete todo ano no mesmo período — alguns manuais o tratam como "
            "variante do friccional.",
            "Consequência estatística: por causa da sazonalidade, a taxa de desocupação do " + rx("IBGE")
            + " costuma subir no 1º trimestre e cair no fim do ano. A comparação correta é com o mesmo período "
            "do ano anterior, ou com a " + azb("série dessazonalizada") + ".",
            "Política: sazonal não se combate com estímulo à demanda agregada; mitigam-no a diversificação "
            "produtiva regional e instrumentos como o " + rx("seguro-defeso") + " (pescadores artesanais no "
            "período de reprodução dos peixes).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição de manual com exemplos plausíveis. A menção à "
                       "“indústria” pode gerar dúvida, mas há indústrias de forte sazonalidade (alimentos, "
                       "brinquedos, vestuário); o item não diz “exclusivamente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O desemprego sazonal decorre de recessões e é combatido por políticas de estímulo à demanda "
            "agregada.”</i> → ERRADO (troca de conceito: isso é o cíclico)",
            "<i>“A comparação da taxa de desocupação com o mesmo trimestre do ano anterior neutraliza efeitos "
            "sazonais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["por exemplo", "mais comum"], "dificuldade": 1,
        "comentario_fonte": "Variações previsíveis da demanda de trabalho por fatores sazonais (colheitas, alta "
                            "temporada); temporário e não reflete desequilíbrio econômico.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00169
    {
        "id": "ECO-E2-L00169-1", "fonte_ref": "E2-L00169", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O desemprego cíclico é gerado exclusivamente por mudanças permanentes nos padrões "
                      "tecnológicos de produção, resultando em substituição de mão de obra por máquinas "
                      "avançadas, afetando especialmente os trabalhadores que não conseguem adaptar-se rapidamente "
                      "a novas tecnologias no mercado de trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O desemprego ") + vm("cíclico") + az(" é gerado ") + vm("exclusivamente")
                    + az(" por mudanças permanentes nos padrões tecnológicos de produção, resultando em "
                         "substituição de mão de obra por máquinas avançadas, afetando especialmente os "
                         "trabalhadores que não conseguem adaptar-se rapidamente a novas tecnologias no mercado de "
                         "trabalho.")),
        "poucas": ("O item descreve o " + azb("desemprego estrutural (tecnológico)") + " e o rotula de cíclico. "
                   "O " + azb("cíclico") + " vem das recessões — queda da demanda agregada — e é temporário."),
        "destrinchando": [
            azb("Cíclico") + " (conjuntural, keynesiano): na recessão, as vendas caem, as firmas cortam produção "
            "e demitem; na retomada, recontratam. É o desvio do desemprego em relação à taxa natural e responde "
            "a políticas fiscal e monetária anticíclicas.",
            azb("Estrutural") + ": descompasso duradouro entre as qualificações ou a localização dos "
            "trabalhadores e as vagas (automação, declínio de setores, abertura comercial), ou salário acima do "
            "equilíbrio (salário mínimo, sindicatos, salário-eficiência). Persiste mesmo na expansão e pede "
            "requalificação e políticas ativas de emprego.",
            "As pistas do item são todas estruturais: “mudanças permanentes”, “substituição de mão de obra por "
            "máquinas”, “trabalhadores que não conseguem adaptar-se”.",
            "O “exclusivamente” é um segundo erro: mesmo o estrutural tem outras causas além da tecnologia "
            "(mudança na composição da demanda, rigidez salarial, descompasso regional).",
            vm("Regra-âncora: temporário + recessão = cíclico; permanente + tecnologia/qualificação = "
               "estrutural."),
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " Definição correta do estrutural com o "
                       "rótulo trocado, reforçada por um “exclusivamente”. Leia o adjetivo do sujeito antes do "
                       "resto: o predicado é que denuncia o tipo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O desemprego estrutural pode persistir mesmo em fases de crescimento econômico.”</i> → CERTO",
            "<i>“O desemprego cíclico integra a taxa natural de desemprego.”</i> → ERRADO (troca de conceito: é "
            "o desvio em relação a ela)",
        ])],
        "reescrita": ("O desemprego " + hl("estrutural") + " é gerado" + hl(", entre outras causas,") + " por "
                      "mudanças permanentes nos padrões tecnológicos de produção, resultando em substituição de mão "
                      "de obra por máquinas avançadas, afetando especialmente os trabalhadores que não conseguem "
                      "adaptar-se rapidamente a novas tecnologias no mercado de trabalho."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": "Cíclico decorre das flutuações econômicas (recessões); a descrição é do estrutural "
                            "tecnológico; erros extras: “exclusivamente” e “mudanças permanentes” (vários "
                            "comentários de IA empilhados, convergentes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00170
    {
        "id": "ECO-E2-L00170-1", "fonte_ref": "E2-L00170", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O desemprego friccional ocorre naturalmente no pleno emprego dos fatores e reflete um "
                      "período de transição para os trabalhadores que estão trocando de empregos ou buscando novas "
                      "oportunidades."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O desemprego friccional ocorre naturalmente <u>no pleno emprego</u> dos fatores e reflete "
                      "um período de transição para os trabalhadores que estão trocando de empregos ou buscando "
                      "novas oportunidades."),
        "poucas": ("Pleno emprego não é desemprego zero: mesmo nele há o " + azb("friccional") + ", fruto do "
                   "tempo de busca e de casamento entre trabalhadores e vagas."),
        "destrinchando": [
            "O " + azb("friccional") + " existe porque trabalhadores e vagas são heterogêneos e a informação é "
            "imperfeita: leva tempo para o recém-formado achar o primeiro emprego, para quem pediu demissão "
            "encontrar coisa melhor, para a firma achar o candidato certo.",
            "Por isso é visto como “saudável”: realoca trabalhadores para usos mais produtivos. Junto com o "
            "estrutural, compõe a " + azb("taxa natural de desemprego") + " — a que prevalece com o produto no "
            "potencial, ou seja, no " + azb("pleno emprego") + ".",
            "Determinantes: rotatividade da economia, eficiência da intermediação (agências públicas e privadas, "
            "plataformas digitais), benefícios que alongam a busca (seguro-desemprego) e mobilidade "
            "geográfica.",
            "Contraste: o " + azb("cíclico") + " é zero no pleno emprego por definição — ele mede justamente o "
            "desemprego acima da taxa natural.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Definição de manual. A armadilha é a "
                       "intuição de que “pleno emprego” significa todos empregados; o “naturalmente” remete à "
                       "taxa natural."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No pleno emprego, a taxa de desemprego é nula.”</i> → ERRADO (há desemprego friccional e "
            "estrutural)",
            "<i>“Programas de intermediação de mão de obra tendem a reduzir o desemprego friccional.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["naturalmente"], "dificuldade": 1,
        "comentario_fonte": "Friccional ocorre naturalmente na transição entre empregos; inerente ao funcionamento "
                            "eficiente do mercado de trabalho.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00171
    {
        "id": "ECO-E2-L00171-1", "fonte_ref": "E2-L00171", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de desemprego estrutural aplica-se adequadamente aos momentos em que a economia "
                      "enfrenta uma recessão, forçando as empresas a reduzir seu quadro de funcionários devido a "
                      "uma queda na demanda por bens e serviços, caracterizando um desequilíbrio temporário e "
                      "reversível no mercado de trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O conceito de desemprego ") + vm("estrutural") + az(" aplica-se adequadamente aos "
                                                                           "momentos em que a economia "
                                                                           "enfrenta uma recessão, forçando as "
                                                                           "empresas a reduzir seu quadro de "
                                                                           "funcionários devido a uma queda na "
                                                                           "demanda por bens e serviços, "
                                                                           "caracterizando um desequilíbrio "
                                                                           "temporário e reversível no mercado "
                                                                           "de trabalho.")),
        "poucas": ("Recessão + queda da demanda + temporário e reversível = " + azb("desemprego cíclico")
                   + ". O " + azb("estrutural") + " é persistente e nasce de mudanças na estrutura produtiva."),
        "destrinchando": [
            azb("Cíclico") + ": a demanda agregada cai, as firmas vendem menos e demitem. É " + vd("temporário")
            + " — desaparece com a retomada — e combatido com política fiscal e monetária expansionista. Na "
            "visão keynesiana, é desemprego " + azb("involuntário") + " por insuficiência de demanda efetiva.",
            azb("Estrutural") + ": descompasso entre o perfil dos trabalhadores e o das vagas (tecnologia, "
            "declínio de setores, mudança regional) ou rigidez salarial. É " + vd("persistente") + ", não some "
            "com a retomada, e exige requalificação e realocação.",
            "Na " + rx("recessão brasileira de 2014–2016") + ", a desocupação subiu de cerca de " + vd("7%")
            + " (fim de 2014) para mais de " + vd("13%") + " (início de 2017), pela PNAD Contínua: predominou o componente cíclico, revertido "
            "lentamente na recuperação.",
            "Ressalva: recessões longas podem converter desemprego cíclico em estrutural (perda de qualificação "
            "e de vínculo com o mercado) — é a " + azb("histerese") + " (" + oc("Blanchard e Summers") + ", "
            + vd("1986") + ").",
        ],
        "dissecando": (cz("[troca de conceito]") + " Descrição perfeita do cíclico com o rótulo trocado. O item "
                       "ainda oferece as pistas contra si mesmo: “recessão”, “queda na demanda”, “temporário e "
                       "reversível”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Recessões prolongadas podem transformar parte do desemprego cíclico em estrutural.”</i> → "
            "CERTO",
            "<i>“O desemprego estrutural é eliminado por políticas de estímulo à demanda agregada.”</i> → ERRADO "
            "(troca de conceito: pede requalificação e realocação)",
        ])],
        "reescrita": ("O conceito de desemprego " + hl("cíclico") + " aplica-se adequadamente aos momentos em que a "
                      "economia enfrenta uma recessão, forçando as empresas a reduzir seu quadro de funcionários "
                      "devido a uma queda na demanda por bens e serviços, caracterizando um desequilíbrio "
                      "temporário e reversível no mercado de trabalho."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["adequadamente"], "dificuldade": 1,
        "comentario_fonte": "A definição é do desemprego cíclico (recessões temporárias); o estrutural decorre "
                            "de mudanças tecnológicas ou na estrutura econômica.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00920
    {
        "id": "ECO-E2-L00920-1", "fonte_ref": "E2-L00920", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_DESEMP,
        "rotulo_item": "Item",
        "assertiva": ("Quando há inovação tecnológica em um segmento da economia, gerando aumento da "
                      "produtividade, sem que ocorra aumento de emprego em outros segmentos, tem-se o desemprego "
                      "denominado estrutural."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando há inovação tecnológica em um segmento da economia, gerando aumento da "
                      "produtividade, <u>sem que ocorra aumento de emprego em outros segmentos</u>, tem-se o "
                      "desemprego denominado <u>estrutural</u>."),
        "poucas": ("Inovação que poupa trabalho num setor, sem absorção dos trabalhadores em outros, gera "
                   + azb("desemprego estrutural") + " na variante " + azb("tecnológica") + "."),
        "destrinchando": [
            "O " + azb("desemprego estrutural") + " resulta de incompatibilidade persistente entre a oferta e a "
            "demanda de mão de obra. Causas típicas: mudança tecnológica e setorial (qualificações que deixam de "
            "ser demandadas) e rigidez que mantém o salário real acima do equilíbrio (salário mínimo, poder "
            "sindical, legislação).",
            "Junto com o friccional, compõe a " + azb("taxa natural de desemprego") + ".",
            "A condição “sem que ocorra aumento de emprego em outros segmentos” é o ponto técnico: em geral, o "
            "ganho de produtividade barateia produtos, eleva a renda real e cria vagas em outras atividades "
            "(efeito compensação). Quando essa absorção não ocorre — ou exige qualificações que os demitidos não "
            "têm —, o desemprego persiste.",
            "A expressão " + azb("desemprego tecnológico") + " foi popularizada por " + oc("Keynes") + " ("
            + vd("1930") + "), que o via como fase de transição. O debate volta a cada onda de automação — hoje, "
            "a inteligência artificial.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Item CERTO cuidadoso: a ressalva “sem aumento de "
                       "emprego em outros segmentos” afasta a objeção de que a inovação cria empregos alhures. "
                       "Sem ela, a afirmação seria discutível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Toda inovação tecnológica que eleva a produtividade gera desemprego no conjunto da "
            "economia.”</i> → ERRADO (modulador absoluto: há efeito compensação)",
            "<i>“O desemprego estrutural integra a taxa natural de desemprego.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["sem que"], "dificuldade": 1,
        "comentario_fonte": "Estrutural: incompatibilidade persistente entre demanda e oferta de mão de obra; "
                            "causas: mudanças tecnológicas e setoriais e salários reais acima do equilíbrio; compõe "
                            "a taxa natural com o friccional.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00921
    {
        "id": "ECO-E2-L00921-1", "fonte_ref": "E2-L00921", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_DESEMP,
        "rotulo_item": "Item",
        "assertiva": ("Quando um trabalhador demora para encontrar uma vaga de trabalho devido apenas a custos de "
                      "locomoção e procura, tem-se o desemprego denominado cíclico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quando um trabalhador demora para encontrar uma vaga de trabalho devido apenas a custos de "
                       "locomoção e procura, tem-se o desemprego denominado ") + vm("cíclico") + az(".")),
        "poucas": ("Demora causada só por custos de busca e locomoção é " + azb("desemprego friccional")
                   + ". O " + azb("cíclico") + " vem da queda da demanda agregada nas recessões."),
        "destrinchando": [
            azb("Friccional") + ": o tempo necessário para trabalhadores e vagas se encontrarem. Procurar custa "
            "(deslocamento, entrevistas, informação), e o trabalhador pondera aceitar a primeira oferta ou "
            "esperar uma melhor. Existe mesmo no pleno emprego.",
            azb("Cíclico") + ": associado às flutuações do produto. Na recessão há menos vagas para todos, e o "
            "desemprego sobe acima da taxa natural; na expansão, cai.",
            "O “apenas” do item é a pista: se a única barreira é o custo de procurar e de se locomover, há vaga "
            "disponível — falta só o encontro. No cíclico, falta a vaga.",
            "Políticas contra o friccional: intermediação de mão de obra (no " + rx("Brasil") + ", o "
            + rx("Sine") + "), informação sobre vagas, auxílio-transporte para busca. Contra o cíclico: política "
            "fiscal e monetária.",
        ],
        "dissecando": (cz("[troca de conceito]") + " A situação descrita é friccional de manual; o rótulo foi "
                       "trocado pelo tipo mais famoso. Pergunte sempre: falta vaga (cíclico/estrutural) ou falta "
                       "o encontro (friccional)?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando um trabalhador demora a se recolocar por causa de uma recessão que reduziu as vagas em "
            "toda a economia, tem-se desemprego cíclico.”</i> → CERTO",
            "<i>“O desemprego friccional desaparece quando a economia atinge o pleno emprego.”</i> → ERRADO "
            "(o friccional existe no pleno emprego)",
        ])],
        "reescrita": ("Quando um trabalhador demora para encontrar uma vaga de trabalho devido apenas a custos de "
                      "locomoção e procura, tem-se o desemprego denominado " + hl("friccional") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": "É desemprego friccional (tempo para procurar e encontrar recolocação); o cíclico se "
                            "associa às flutuações do produto e da demanda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00922
    {
        "id": "ECO-E2-L00922-1", "fonte_ref": "E2-L00922", "destino": "59", "subtema": H2["desemp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_DESEMP,
        "rotulo_item": "Item",
        "assertiva": ("O programa de seguro-desemprego reduz o desemprego friccional, visto que os trabalhadores "
                      "desempregados recebem, durante certo período de tempo, parte do salário que recebiam no seu "
                      "último emprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O programa de seguro-desemprego ") + vm("reduz") + az(" o desemprego friccional, visto que "
                                                                             "os trabalhadores desempregados "
                                                                             "recebem, durante certo período de "
                                                                             "tempo, parte do salário que "
                                                                             "recebiam no seu último emprego.")),
        "poucas": ("Com renda durante a busca, o trabalhador pode procurar por mais tempo e recusar ofertas: o "
                   "seguro-desemprego " + azb("tende a aumentar") + " o desemprego friccional."),
        "destrinchando": [
            "O benefício reduz o custo de ficar desempregado e eleva o " + azb("salário de reserva") + " (o "
            "mínimo que o trabalhador aceita). A busca se alonga e a taxa de desemprego friccional — e, com ela, "
            "a " + azb("taxa natural") + " — tende a subir. É o argumento de " + oc("Mankiw") + " nos manuais.",
            "A própria justificativa do item (recebem parte do salário anterior) explica o aumento, não a "
            "redução: o nexo foi invertido.",
            "Contrapeso: a busca mais longa pode gerar " + azb("melhores casamentos") + " entre trabalhador e "
            "vaga (mais produtividade e menos rotatividade futura), e o seguro protege a renda e o consumo na "
            "recessão (estabilizador automático). Por isso o desenho importa: duração limitada, valor "
            "decrescente, exigência de busca ativa.",
            "O que reduz o friccional são políticas de " + azb("intermediação e treinamento") + ", que encurtam o "
            "tempo de encontro entre trabalhadores e vagas. No " + rx("Brasil") + ", o seguro-desemprego é "
            "pago em " + vd("3 a 5 parcelas") + ", com recursos do " + rx("FAT") + ".",
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " Fato verdadeiro (o trabalhador recebe parte do "
                       "salário) usado para sustentar a conclusão oposta à da teoria. Pista: renda durante o "
                       "desemprego diminui a urgência de aceitar a primeira oferta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Programas de intermediação de mão de obra tendem a reduzir a taxa natural de "
            "desemprego.”</i> → CERTO",
            "<i>“O seguro-desemprego, por elevar o salário de reserva, tende a reduzir a duração do "
            "desemprego.”</i> → ERRADO (inversão: tende a alongá-la)",
        ])],
        "reescrita": ("O programa de seguro-desemprego " + hl("tende a aumentar") + " o desemprego friccional, visto "
                      "que os trabalhadores desempregados recebem, durante certo período de tempo, parte do salário "
                      "que recebiam no seu último emprego."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O seguro-desemprego tende a aumentar o friccional (mais tempo de busca, recusa de "
                            "propostas); treinamento e intermediação reduzem o friccional e a taxa natural.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
