"""Cards do lote de redação 03 — ECO, passada 03 (notas 56: Solow; 57: crescimento endógeno, Schumpeter,
Harrod-Domar)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ss": "⚙️ Estado estacionário",
    "ouro": "🥇 Regra de ouro",
    "pop": "👥 População, tecnologia e convergência",
    "cresc": "💡 Teorias do crescimento",
}

CMD_NIDI_24 = ("Considerando os determinantes do crescimento econômico e a experiência recente do Brasil, julgue o "
               "item a seguir.")

CMD_NIDI_26 = "A respeito dos modelos de crescimento clássicos e modernos, julgue o item a seguir."

CMD_CLIP_25 = ("O crescimento de longo prazo depende da acumulação de fatores e da produtividade total. Com base nas "
               "teorias de crescimento, julgue o item a seguir.")

CMD_RT_A8 = "Com relação aos modelos de crescimento e desenvolvimento, julgue o item a seguir."

CMD_BOZAN = "No contexto das teorias de crescimento endógeno e do impacto da tecnologia, julgue o item a seguir."

CMD_DANIEL = "Julgue o item a seguir, relativo às teorias do crescimento econômico."

CMD_NAB_4 = "Em relação aos modelos de crescimento, julgue o item a seguir."

CMD_NAB_INTERT = "A respeito dos modelos de crescimento e da economia intertemporal, julgue o item a seguir."

CMD_NAB_TEOR = "Sobre teorias do crescimento econômico, julgue o item a seguir."

CMD_GEN = "Julgue o item a seguir, relativo às teorias do crescimento econômico."

ALERTA_BANCA_2019 = ("banca_provavel: CEBRASPE (formato C/E e comentários de professores no padrão de bancos de "
                     "questões; a fonte não traz órgão — não confirmada)")

CARDS = [
    # ------------------------------------------------------------------ E2-L01733
    {
        "id": "ECO-E2-L01733-1", "fonte_ref": "E2-L01733", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": "Com base no modelo de Solow, julgue a afirmativa a seguir como verdadeira ou falsa.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando dois países que apresentam mesma função de produção, mesmos valores de taxa de "
                      "crescimento populacional, depreciação e de poupança, pode-se dizer que o país mais pobre hoje "
                      "tenderá a crescer mais rapidamente do que o país mais rico, levando à convergência da renda "
                      "per capita no estado estacionário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando dois países que apresentam <u>mesma função de produção, mesmos valores de taxa "
                      "de crescimento populacional, depreciação e de poupança</u>, pode-se dizer que o país mais "
                      "pobre hoje <u>tenderá</u> a crescer mais rapidamente do que o país mais rico, levando à "
                      "convergência da renda per capita no estado estacionário."),
        "poucas": ("Com parâmetros iguais, os dois países têm o " + azb("mesmo estado estacionário") + "; o mais "
                   "pobre está mais longe dele e, pelos " + azb("rendimentos marginais decrescentes") + " do "
                   "capital, cresce mais rápido até alcançá-lo: é a " + azb("convergência condicional") + "."),
        "destrinchando": [
            "No modelo de " + oc("Solow") + " (1956), o capital por trabalhador evolui por Δk = s·f(k) − (n+δ)k. "
            "Dividindo por k: " + vd("γ<sub>k</sub> = s·f(k)/k − (n+δ)") + ". Como f é côncava, s·f(k)/k cai "
            "à medida que k sobe: quanto menos capital, maior a taxa de crescimento.",
            "Mesmos s, n, δ e mesma f(k) → mesmo k* e mesmo y*. O país pobre (k baixo) tem produto marginal do "
            "capital alto: cada unidade poupada rende muito, e ele cresce mais rápido durante a "
            + azb("transição") + ". O rico, perto de k*, cresce pouco. As rendas per capita se aproximam.",
            "Vocabulário: " + azb("convergência absoluta") + " = todos os pobres crescem mais que os ricos, "
            "independentemente dos parâmetros (empiricamente rejeitada no mundo como um todo); "
            + azb("convergência condicional") + " = cada país converge para o <b>seu</b> estado estacionário — "
            "só converge para o mesmo nível de renda quem tem os mesmos parâmetros. O item descreve exatamente "
            "esse caso: entre países com parâmetros idênticos, a condição está satisfeita.",
            "Evidência: a convergência aparece entre economias parecidas (estados dos EUA, países da OCDE, "
            "regiões europeias), nos estudos de " + oc("Barro e Sala-i-Martin") + " e no Solow ampliado de "
            + oc("Mankiw, Romer e Weil") + " (1992).",
            vm("Regra-âncora: mesmos parâmetros → mesmo k*; quem está mais longe dele cresce mais rápido."),
        ],
        "grafico_verso": "ECO-E2-L01733-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " É a definição de manual da convergência "
                       "condicional, protegida por “tenderá”. O risco é o candidato achar que a convergência de "
                       "Solow “não existe” (a absoluta é rejeitada) e marcar ERRADO sem ler a cláusula dos "
                       "parâmetros idênticos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Solow prevê que todos os países pobres crescerão mais rapidamente que os ricos, "
            "independentemente de suas taxas de poupança e de crescimento populacional.”</i> → ERRADO (isso é "
            "convergência absoluta)",
            "<i>“…o país mais pobre tenderá a crescer mais rapidamente, porque o produto marginal do capital é "
            "maior onde o capital por trabalhador é menor.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tenderá"], "dificuldade": 1,
        "comentario_fonte": "Convergência condicional: com parâmetros idênticos, o país mais pobre, de menor k, "
                            "tem PMgK maior e cresce mais rápido na transição para o mesmo estado estacionário.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00381-1 (convergência condicional no Solow)"],
    },
    # ------------------------------------------------------------------ E3-L00380
    {
        "id": "ECO-E3-L00380-1", "fonte_ref": "E3-L00380", "destino": "56", "subtema": H2["ss"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_24,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o modelo de Solow, um aumento na taxa de poupança é capaz de aumentar de forma "
                      "permanente a taxa de crescimento de um país. Logo, as baixas taxas de poupança registradas no "
                      "Brasil estão relacionadas com o seu baixo crescimento econômico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o modelo de Solow, um aumento na taxa de poupança é capaz de aumentar de "
                       "forma permanente ") + vm("a taxa de crescimento") + az(" de um país. Logo, as baixas taxas "
                       "de poupança registradas no Brasil estão relacionadas com o seu baixo ")
                    + vm("crescimento econômico") + az(".")),
        "poucas": ("No Solow, poupar mais tem " + azb("efeito nível") + ", não " + azb("efeito crescimento")
                   + ": eleva para sempre k* e y*, mas a taxa de crescimento só sobe na transição; no longo prazo, "
                   "volta a ser a do " + vd("progresso técnico (g)") + "."),
        "destrinchando": [
            "Com s maior, a curva s·f(k) sobe: o investimento passa a superar o investimento de reposição "
            "(n+δ)k, e k cresce até um novo k* mais alto. Nesse novo estado estacionário, Δk = 0 de novo.",
            "Resultado: o produto por trabalhador fica " + vd("permanentemente mais alto") + " (nível), e a taxa "
            "de crescimento fica " + vd("temporariamente mais alta") + " (transição). Sem progresso técnico, o "
            "crescimento per capita de longo prazo é zero; com progresso técnico à taxa g, é " + vd("g")
            + " — e g é exógeno, independente de s.",
            "Por quê? Os " + azb("rendimentos marginais decrescentes") + " do capital: cada aumento de k rende "
            "menos produto, até que a poupança adicional só baste para repor a depreciação e equipar os novos "
            "trabalhadores.",
            "Aplicação ao " + rx("Brasil") + ": a poupança doméstica baixa (na casa de 15% a 17% do PIB nos "
            "anos recentes) ⏳ (out/2026) ajuda a explicar, no Solow, um <b>nível</b> de renda per capita menor. "
            "O baixo crescimento persistente, porém, o modelo atribuiria à " + azb("produtividade total dos "
            "fatores") + " estagnada, não à poupança.",
            "Contraste: nos modelos de " + azb("crescimento endógeno") + " do tipo AK, sem rendimentos "
            "decrescentes do capital, poupar mais eleva a taxa de crescimento de forma permanente.",
            vm("Regra-âncora: no Solow, s mexe no nível; só g mexe na taxa de longo prazo."),
        ],
        "grafico_verso": "ECO-E3-L00380-1-V1",
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item troca efeito nível por efeito "
                       "crescimento e, sobre a premissa falsa, ergue uma conclusão sobre o Brasil com “Logo”. "
                       "Pista: “de forma permanente” junto de “taxa de crescimento” no Solow é quase sempre "
                       "ERRADO. 🔥 Tema recorrente em CEBRASPE e ANPEC."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com o modelo de Solow, um aumento na taxa de poupança eleva de forma permanente o "
            "nível do produto per capita e apenas temporariamente sua taxa de crescimento.”</i> → CERTO",
            "<i>“No modelo AK, um aumento na taxa de poupança eleva apenas temporariamente a taxa de "
            "crescimento.”</i> → ERRADO (no AK o efeito sobre a taxa é permanente)",
        ])],
        "reescrita": ("De acordo com o modelo de Solow, um aumento na taxa de poupança é capaz de aumentar de forma "
                      "permanente " + hl("o nível de renda per capita") + " de um país. Logo, as baixas taxas de "
                      "poupança registradas no Brasil estão relacionadas com o seu baixo "
                      + hl("nível de renda per capita") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["de forma permanente", "logo"],
        "dificuldade": 1,
        "comentario_fonte": "Várias respostas de IA concordantes: a poupança afeta o nível de renda de estado "
                            "estacionário, não a taxa de crescimento permanente, que depende do progresso técnico "
                            "exógeno; efeito sobre o crescimento só na transição.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 542, 543, 544, 546, 547", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (conteúdo no 📖)"},
                          {"ref": "IMAGEM 545", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (equação de acumulação no 📖)"}],
        "alertas": ["dado_aproximado: poupança doméstica brasileira “na casa de 15% a 17% do PIB” — ordem de "
                    "grandeza, conferir na série do IBGE (Contas Nacionais)"],
    },
    # ------------------------------------------------------------------ E3-L00381
    {
        "id": "ECO-E3-L00381-1", "fonte_ref": "E3-L00381", "destino": "56", "subtema": H2["pop"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_24,
        "rotulo_item": "Item",
        "assertiva": ("Uma das consequências do modelo de Solow é a sua rejeição de convergência de níveis de renda "
                      "para todos os países na presença de mudanças tecnológicas. Tal conclusão, contudo, não é "
                      "explicada pelo modelo que trata a tecnologia como uma variável exógena."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma das consequências do modelo de Solow é a sua rejeição de convergência de níveis de renda "
                      "<u>para todos os países</u> na presença de mudanças tecnológicas. Tal conclusão, contudo, "
                      "<u>não é explicada pelo modelo</u> que trata a tecnologia como uma variável exógena."),
        "poucas": ("O Solow prevê só " + azb("convergência condicional") + ": níveis de renda iguais apenas "
                   "entre países com os mesmos parâmetros e a mesma tecnologia. Por que a tecnologia difere entre "
                   "países, o modelo não diz — ela é " + azb("exógena") + "."),
        "destrinchando": [
            "No Solow com progresso técnico, y = A·f(k̃), com A crescendo à taxa g. O nível de renda per "
            "capita de longo prazo depende de s, n, δ e do <b>nível</b> de A; a taxa de crescimento de longo "
            "prazo é g. Países com A, s ou n diferentes convergem para trajetórias diferentes.",
            "Por isso o modelo " + vd("rejeita a convergência absoluta") + " (todos para o mesmo nível de renda) "
            "e aceita a " + vd("condicional") + " (cada um para o seu estado estacionário, mais rápido quanto "
            "mais longe dele).",
            "A tecnologia “cai do céu”: o modelo toma A e g como dados, sem explicar por que alguns países "
            "inovam ou absorvem tecnologia mais que outros. É o “" + azb("resíduo de Solow") + "” — a parte do "
            "crescimento que a acumulação de fatores não explica, chamada de " + azb("produtividade total dos "
            "fatores") + " (PTF).",
            "Essa lacuna motivou os modelos de " + azb("crescimento endógeno") + " (" + oc("Romer") + ", 1986 "
            "e 1990; " + oc("Lucas") + ", 1988), em que P&D, capital humano e transbordamentos de conhecimento "
            "resultam de decisões dos agentes e podem gerar divergência permanente de renda.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Redação truncada, mas as duas ideias estão "
                       "certas: não há convergência para todos (só a condicional) e a causa — diferença "
                       "tecnológica — é exógena ao modelo. Quem associa “Solow = convergência” tende a marcar "
                       "ERRADO na primeira oração."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Solow prevê convergência absoluta das rendas per capita de todos os países, desde "
            "que a tecnologia seja exógena.”</i> → ERRADO (a previsão é condicional)",
            "<i>“No modelo de Solow, as diferenças de progresso técnico entre países são explicadas pelas "
            "diferenças de taxa de poupança.”</i> → ERRADO (nexo indevido: tecnologia é exógena)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["todos"], "dificuldade": 2,
        "comentario_fonte": "Solow prevê convergência condicional; se a tecnologia (exógena) difere, não há "
                            "convergência absoluta; o modelo não explica a origem do progresso técnico, o que "
                            "motivou os modelos endógenos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 548-552", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (conteúdo no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01733-1 (convergência condicional)"],
    },
    # ------------------------------------------------------------------ E3-L00446
    {
        "id": "ECO-E3-L00446-1", "fonte_ref": "E3-L00446", "destino": "56", "subtema": H2["ss"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI_26,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow sem progresso técnico, o aumento da taxa de depreciação do capital leva a "
                      "economia a uma nova trajetória de crescimento equilibrado, na qual a taxa de retorno do "
                      "capital é menor do que no equilíbrio original."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow sem progresso técnico, o aumento da taxa de depreciação do capital leva "
                       "a economia a uma nova trajetória de crescimento equilibrado, na qual a taxa de retorno do "
                       "capital é ") + vm("menor") + az(" do que no equilíbrio original.")),
        "poucas": ("Mais depreciação → " + vd("k* menor") + ". Com " + azb("rendimentos marginais "
                   "decrescentes") + ", capital mais escasso tem produto marginal <b>maior</b>: a taxa de retorno "
                   "do capital sobe, não cai."),
        "destrinchando": [
            "Estado estacionário: " + vd("s·f(k*) = (n+δ)k*") + ". Com δ maior, a reta (n+δ)k fica mais "
            "inclinada: a mesma poupança precisa repor um capital que se desgasta mais rápido, e a economia "
            "recua para um k* menor (e um y* menor).",
            "Na economia competitiva, o capital é remunerado pelo seu " + azb("produto marginal") + ": "
            "r = PMgK = f′(k). Como f é côncava (f″ &lt; 0), f′ é maior onde k é menor. Logo, no novo estado "
            "estacionário, " + vd("PMgK sobe") + ".",
            "Exemplo: f(k) = 3√k e s = 0,4. Com n+δ = 0,2, k* = 36 e PMgK = " + vd("0,25") + "; com n+δ = 0,3, "
            "k* = 16 e PMgK = " + vd("0,375") + ".",
            "Detalhe técnico: se “taxa de retorno” for lida <b>líquida</b> da depreciação (f′ − δ), o sinal "
            "depende dos parâmetros — na Cobb-Douglas, f′(k*) − δ = α(n+δ)/s − δ, que sobe com δ quando s &lt; α "
            "(economia abaixo da regra de ouro). A leitura padrão de prova é a do produto marginal (bruta).",
            "“Trajetória de crescimento equilibrado” sem progresso técnico = estado estacionário: k e y por "
            "trabalhador constantes; Y e K crescem à taxa n.",
            vm("Regra-âncora: k* ↓ ⇒ PMgK ↑ (e vice-versa) — sempre pela concavidade de f(k)."),
        ],
        "grafico_verso": "ECO-E3-L00446-1-V1",
        "dissecando": (cz("[inversão]") + " A primeira parte (nova trajetória equilibrada) está certa; o erro é "
                       "o sentido do efeito sobre o retorno. A intuição apressada “mais desgaste = capital rende "
                       "menos” confunde depreciação com produtividade. Pista: pergunte sempre o que acontece com "
                       "k* e aplique a concavidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, um aumento da taxa de poupança reduz o produto marginal do capital no novo "
            "estado estacionário.”</i> → CERTO (k* sobe)",
            "<i>“Um aumento da taxa de depreciação eleva o capital por trabalhador de estado "
            "estacionário.”</i> → ERRADO (inversão: k* cai)",
        ])],
        "reescrita": ("No modelo de Solow sem progresso técnico, o aumento da taxa de depreciação do capital leva a "
                      "economia a uma nova trajetória de crescimento equilibrado, na qual a taxa de retorno do "
                      "capital é " + hl("maior") + " do que no equilíbrio original."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "δ maior → reta de reposição mais inclinada → k* menor; por rendimentos marginais "
                            "decrescentes, o produto marginal (taxa de retorno) do capital fica maior. Várias IAs "
                            "concordantes; uma ressalva sobre retorno líquido de depreciação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 630-632", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (fundidas em ECO-E3-L00446-1-V1)"},
                          {"ref": "IMAGEM 633", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (no 📖)"},
                          {"ref": "IMAGEM 634-636", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00447-1 (mesma prova; choque em n com s fixo)"],
    },
    # ------------------------------------------------------------------ E3-L00447
    {
        "id": "ECO-E3-L00447-1", "fonte_ref": "E3-L00447", "destino": "56", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI_26,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Solow, se o estoque de capital por trabalhador se encontra acima do nível "
                      "associado à regra de ouro, então o aumento da taxa de crescimento populacional pode aumentar "
                      "(tudo o mais constante) o nível de consumo per capita, dado que permite diminuir o estoque de "
                      "capital por trabalhador."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Solow, se o estoque de capital por trabalhador se encontra acima do nível "
                       "associado à regra de ouro, então o aumento da taxa de crescimento populacional ")
                    + vm("pode aumentar") + az(" (tudo o mais constante) o nível de consumo per capita, ")
                    + vm("dado que") + az(" permite diminuir o estoque de capital por trabalhador.")),
        "poucas": ("Com s fixo (“tudo o mais constante”), o consumo de estado estacionário é " + vd("c* = (1−s)·f(k*)")
                   + ". Se n sobe, k* cai, f(k*) cai e c* " + vm("cai") + " — esteja a economia acima ou abaixo "
                   "da regra de ouro."),
        "destrinchando": [
            azb("Regra de ouro") + " (" + oc("Phelps") + ", 1961): o k* que maximiza c* = f(k*) − (n+δ)k* "
            "satisfaz " + vd("f′(k<sub>ouro</sub>) = n+δ") + ". Acima dele há " + azb("ineficiência dinâmica")
            + ": capital demais, consumo de menos.",
            "Até aqui o item acerta a intuição: acima da regra de ouro, <b>reduzir k*</b> pode elevar c*. O "
            "erro está no instrumento. Decompondo: dc*/dn = [f′(k*) − (n+δ)]·dk*/dn − k*. O 1º termo é "
            "positivo (menos capital excessivo), mas o 2º, " + vd("− k*") + ", é o custo direto de equipar mais "
            "trabalhadores novos. Somados, dão (1−s)·f′(k*)·dk*/dn &lt; 0: o efeito líquido é "
            + vm("sempre negativo") + " com s constante.",
            "Exemplo: f(k) = 3√k, s = 0,7 (acima de α = 0,5, logo acima da regra de ouro). Com n+δ = 0,2, "
            "k* ≈ 110 e c* ≈ " + vd("9,45") + "; com n+δ = 0,3, k* = 49 e c* = " + vd("6,3") + ".",
            "O caminho certo para sair da sobreacumulação é " + vd("reduzir s") + ": o consumo sobe já na "
            "transição e também no novo estado estacionário (é o que define a ineficiência dinâmica).",
            vm("Regra-âncora: com s fixo, n ↑ ⇒ k* ↓ ⇒ y* ↓ ⇒ c* ↓; para corrigir excesso de capital, mexa em s."),
        ],
        "grafico_verso": "ECO-E3-L00447-1-V1",
        "dissecando": (cz("[nexo indevido · meia-verdade]") + " Parte verdadeira (n ↑ reduz k*; acima da regra "
                       "de ouro, menos capital pode ser bom) + nexo falso (“dado que”) que transforma a queda de "
                       "k* em ganho de consumo, ignorando o custo de diluir o capital entre mais trabalhadores. "
                       "Pista: “tudo o mais constante” congela s."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o capital por trabalhador está acima do nível da regra de ouro, uma redução da taxa de "
            "poupança eleva o consumo per capita tanto na transição quanto no novo estado "
            "estacionário.”</i> → CERTO",
            "<i>“Na regra de ouro, o produto marginal do capital é igual à taxa de poupança.”</i> → ERRADO "
            "(é igual a n+δ)",
        ])],
        "reescrita": ("No modelo de Solow, se o estoque de capital por trabalhador se encontra acima do nível "
                      "associado à regra de ouro, então o aumento da taxa de crescimento populacional "
                      + hl("reduz") + " (tudo o mais constante) o nível de consumo per capita, "
                      + hl("embora") + " permita diminuir o estoque de capital por trabalhador."),
        "tipo_erro": ["NEXO_INDEVIDO", "MEIA_VERDADE"], "moduladores": ["pode", "tudo o mais constante"],
        "dificuldade": 3,
        "comentario_fonte": "Com s fixo, c = (1−s)·f(k); n maior reduz k e f(k), logo reduz o consumo per capita; "
                            "para corrigir a sobreacumulação, reduz-se s. Uma das IAs diz que o sinal seria "
                            "“ambíguo em geral” e só negativo na Cobb-Douglas.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 637-640, 643-648", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"},
                          {"ref": "IMAGEM 641", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto (no 📖)"},
                          {"ref": "IMAGEM 642", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00447-1-V1, com os consumos c₁* e c₂*)"}],
        "alertas": ["qualidade_fonte: uma das respostas de IA afirma que dc*/dn é “ambíguo em geral”; com s "
                    "constante, c* = (1−s)·f(k*) cai sempre que k* cai, para qualquer f crescente — corrigido",
                    "quase_duplicata: ECO-E3-L00446-1 (mesma prova; choque em δ)"],
    },
    # ------------------------------------------------------------------ E1-0452
    {
        "id": "ECO-E1-0452-1", "fonte_ref": "E1-0452", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": CMD_CLIP_25,
        "rotulo_item": "Item",
        "assertiva": ("A abordagem schumpeteriana do crescimento destaca o papel da destruição criadora, na qual "
                      "novas tecnologias substituem processos ineficientes e impulsionam a inovação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A abordagem schumpeteriana do crescimento destaca o papel da <u>destruição criadora</u>, na "
                      "qual novas tecnologias substituem processos ineficientes e impulsionam a inovação."),
        "poucas": ("É o núcleo de " + oc("Schumpeter") + ": o capitalismo se transforma por " + azb("destruição "
                   "criadora") + " — inovações introduzidas pelo empresário inovador tornam obsoletos produtos, "
                   "métodos e empresas antigos, e é essa ruptura que move o desenvolvimento."),
        "destrinchando": [
            "Em <i>Teoria do Desenvolvimento Econômico</i> (" + vd("1911") + "), " + oc("Schumpeter") + " parte "
            "do " + azb("fluxo circular") + " — uma economia estacionária que se repete — e define o "
            "desenvolvimento como a ruptura desse fluxo por " + azb("novas combinações") + ": novo produto, novo "
            "método de produção, novo mercado, nova fonte de matéria-prima, nova organização de um setor.",
            "Quem realiza as novas combinações é o " + azb("empresário inovador") + " (empreendedor), "
            "financiado pelo " + azb("crédito bancário") + ", que cria poder de compra novo. Os imitadores "
            "vêm em enxame, os lucros extraordinários se dissipam e os produtores antigos são expulsos.",
            "Em <i>Capitalismo, Socialismo e Democracia</i> (" + vd("1942") + "), ele chama esse processo de "
            "“destruição criadora” e o descreve como o fato essencial do capitalismo. A concorrência que "
            "importa não é a de preços, mas a da nova mercadoria e da nova tecnologia.",
            "Herança moderna: os modelos " + azb("neoschumpeterianos") + " de crescimento endógeno (" + oc("Aghion "
            "e Howitt") + ", 1992) formalizam o crescimento como uma sequência de inovações que tornam obsoletas "
            "as anteriores. Aghion e Howitt receberam o Nobel de 2025, junto com " + oc("Joel Mokyr") + ".",
            vm("Regra-âncora: Schumpeter = inovação + empresário + crédito → destruição criadora."),
        ],
        "dissecando": (cz("[literalidade]") + " Item de definição, sem modulador perigoso. Variações ERRADAS "
                       "costumam trocar o agente (“o Estado”, “os trabalhadores”), dizer que a inovação vem de "
                       "fora do sistema econômico ou atribuir o conceito a outro autor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Schumpeter, a destruição criadora é um choque exógeno ao sistema capitalista, que o afasta "
            "de seu equilíbrio natural.”</i> → ERRADO (o processo é endógeno: surge “de dentro”)",
            "<i>“Para Schumpeter, a concorrência relevante no capitalismo é a da nova mercadoria e da nova "
            "tecnologia, mais do que a de preços.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Conceito central de Schumpeter: “vendaval perene de destruição criadora”, em que "
                            "inovações radicais destroem estruturas antigas e criam novas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0554 (mesmo item e mesma prova) fundida neste card",
                    "quase_duplicata: ECO-E1-0717-1, ECO-E2-L00620-1, ECO-E1-0742-1 (destruição criadora em "
                    "outras provas)"],
    },
    # ------------------------------------------------------------------ E1-0453
    {
        "id": "ECO-E1-0453-1", "fonte_ref": "E1-0453", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": CMD_CLIP_25,
        "rotulo_item": "Item",
        "assertiva": ("O capital humano é irrelevante nos modelos de crescimento de inspiração clássica, pois "
                      "considera-se que sua contribuição se limita à reprodução da força de trabalho."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O capital humano ") + vm("é irrelevante") + az(" nos modelos de crescimento de inspiração "
                       "clássica, pois ") + vm("considera-se que sua contribuição se limita à reprodução da força "
                                              "de trabalho") + az(".")),
        "poucas": ("Desde " + oc("Adam Smith") + " as habilidades adquiridas pelos trabalhadores contam como "
                   "fonte de produtividade, e a teoria moderna fez do " + azb("capital humano") + " um motor "
                   "central do crescimento. Nada de “irrelevante”."),
        "destrinchando": [
            "Na <i>Riqueza das Nações</i> (" + vd("1776") + "), " + oc("Smith") + " inclui no capital fixo da "
            "sociedade “as habilidades adquiridas e úteis” dos habitantes: a educação e o aprendizado custam, "
            "e se pagam com trabalho mais produtivo. A " + azb("divisão do trabalho") + " — motor do "
            "crescimento em Smith — atua justamente pelo aumento da destreza do trabalhador.",
            "A ideia de que o trabalhador só “reproduz” a força de trabalho (salário de subsistência) é uma "
            "leitura da teoria clássica da distribuição — " + oc("Ricardo") + ", " + oc("Malthus") + " —, não uma "
            "negação de que qualificação aumente a produtividade.",
            "Na teoria moderna: " + oc("Schultz") + " e " + oc("Becker") + " (anos 1960) formalizam o "
            + azb("capital humano") + "; o Solow ampliado de " + oc("Mankiw, Romer e Weil") + " (1992) o "
            "inclui na função de produção (Y = K<sup>α</sup>H<sup>β</sup>(AL)<sup>1−α−β</sup>); e " + oc("Lucas")
            + " (1988) faz da acumulação de capital humano o motor do " + azb("crescimento endógeno") + ".",
            "Leitura do enunciado: se “inspiração clássica” for entendida como neoclássica (Solow), o item "
            "continua ERRADO — o capital humano entra no Solow ampliado e explica boa parte das diferenças de "
            "renda entre países.",
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " “Irrelevante” é absoluto, e a "
                       "justificativa (“se limita à reprodução da força de trabalho”) mistura teoria do salário "
                       "com teoria do crescimento. Em itens sobre fatores de crescimento, negar papel a um fator "
                       "quase sempre é ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Lucas (1988), a acumulação de capital humano pode sustentar o crescimento da renda "
            "per capita no longo prazo.”</i> → CERTO",
            "<i>“O modelo de Solow ampliado por Mankiw, Romer e Weil exclui o capital humano da função de "
            "produção.”</i> → ERRADO (é justamente o que ele inclui)",
        ])],
        "reescrita": ("O capital humano " + hl("não") + " é irrelevante nos modelos de crescimento de inspiração "
                      "clássica, pois " + hl("já Adam Smith contava as habilidades adquiridas dos trabalhadores "
                      "como capital, fonte de maior produtividade") + "."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["irrelevante", "se limita"],
        "dificuldade": 2,
        "comentario_fonte": "O capital humano é central nos modelos de crescimento endógeno, que buscam explicar o "
                            "progresso técnico exógeno no Solow.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0555 (mesmo item e mesma prova) fundida neste card"],
    },
    # ------------------------------------------------------------------ E1-0706
    {
        "id": "ECO-E1-0706-1", "fonte_ref": "E1-0706", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca dos modelos de crescimento econômico, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Harrod-Domar, o crescimento econômico é determinado exclusivamente pela taxa de "
                      "poupança e pelo coeficiente de capital necessário por unidade de produto, sendo que a "
                      "produtividade marginal do capital é considerada constante e independente de tecnologia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de Harrod-Domar, o crescimento econômico é determinado <u>exclusivamente</u> pela "
                      "taxa de poupança e pelo coeficiente de capital necessário por unidade de produto, sendo que "
                      "a produtividade marginal do capital é considerada <u>constante</u> e independente de "
                      "tecnologia."),
        "poucas": ("No Harrod-Domar, " + vd("g = s/v") + ": só a poupança (s) e a relação capital-produto (v) "
                   "determinam o crescimento. Com proporções fixas, o produto marginal do capital (1/v) é "
                   "constante e não há progresso técnico no modelo."),
        "destrinchando": [
            "Origem: " + oc("Roy Harrod") + " (1939) e " + oc("Evsey Domar") + " (1946) estendem " + oc("Keynes")
            + " para o longo prazo. A tecnologia é de " + azb("proporções fixas") + " (tipo Leontief): cada "
            "unidade de produto exige v unidades de capital, e v é um parâmetro dado.",
            "Dedução: poupança S = sY financia o investimento I = ΔK; com K = vY, ΔK = vΔY. Logo sY = vΔY → "
            + vd("ΔY/Y = s/v") + ". Ex.: s = 20% e v = 4 → g = " + vd("5%") + " ao ano.",
            "Implicações: (1) " + azb("produtividade marginal = média = 1/v") + ", constante — não há "
            "rendimentos decrescentes; (2) não há substituição entre capital e trabalho; (3) não há progresso "
            "técnico que altere v ao longo do tempo. “Independente de tecnologia” deve ser lido nesse sentido: "
            "v é um coeficiente técnico dado, que nenhum progresso tecnológico modifica dentro do modelo.",
            "Por isso o modelo serviu à " + azb("teoria do desenvolvimento") + " e ao planejamento dos anos "
            "1950–60: para crescer a g desejado, bastaria elevar s (inclusive com poupança externa) — o "
            "“hiato de poupança”.",
            vm("Regra-âncora: Harrod-Domar → g = s/v, v fixo, sem substituição de fatores nem progresso técnico."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O “exclusivamente” assusta, mas é exato: na equação "
                       "fundamental só entram s e v. O ponto delicado é “independente de tecnologia”, que só se "
                       "sustenta lido como “sem progresso técnico”: v é, ele mesmo, um dado técnico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Harrod-Domar, a taxa de crescimento é diretamente proporcional à relação "
            "capital-produto.”</i> → ERRADO (inversamente: g = s/v)",
            "<i>“No modelo de Harrod-Domar, a produtividade marginal do capital é decrescente, como no modelo de "
            "Solow.”</i> → ERRADO (é constante)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": "Função de produção de proporções fixas, v = K/Y constante, g = s/v; PMgK = 1/v "
                            "constante, sem substituição de fatores nem progresso técnico endógeno.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “margin aldo capital” → “marginal do capital” (OCR)",
                    "quase_duplicata: ECO-E2-L00523-1, ECO-E1-0713-1 (g = s/v)"],
    },
    # ------------------------------------------------------------------ E1-0713
    {
        "id": "ECO-E1-0713-1", "fonte_ref": "E1-0713", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_GEN,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Harrod-Domar, o produto de uma economia é função do estoque de capital, e a taxa "
                      "de crescimento de longo prazo é determinada pela produtividade total dos fatores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Harrod-Domar, o produto de uma economia é função do estoque de capital, e a "
                       "taxa de crescimento de longo prazo é determinada ") + vm("pela produtividade total dos "
                                                                                 "fatores") + az(".")),
        "poucas": ("A 1ª parte está certa (Y = K/v). O erro é a 2ª: no Harrod-Domar, " + vd("g = s/v") + " — "
                   "poupança e relação capital-produto. " + azb("Produtividade total dos fatores") + " é conceito "
                   "neoclássico (resíduo de Solow)."),
        "destrinchando": [
            "Harrod-Domar: Y = K/v, com v (relação capital-produto) fixo. O produto depende só do capital — o "
            "trabalho é suposto abundante. Taxa de crescimento: " + vd("g = s/v = s·σ") + ", em que σ = 1/v é "
            "a produtividade do capital (a “produtividade social média potencial do investimento”, na "
            "linguagem de " + oc("Domar") + ").",
            "A " + azb("PTF") + " (ou " + azb("resíduo de Solow") + ") nasce da contabilidade do crescimento de "
            + oc("Solow") + " (1957): ΔY/Y = αΔK/K + (1−α)ΔL/L + ΔA/A. É o pedaço do crescimento não explicado "
            "pela acumulação de capital e trabalho. Não existe no Harrod-Domar, que não tem progresso técnico.",
            "A produtividade que conta no Harrod-Domar é a de um fator só — a do " + azb("capital") + " (1/v) "
            "—, não a de todos os fatores em conjunto. E falta a outra variável: a taxa de poupança.",
            "Natureza do modelo: keynesiano, destaca o " + azb("duplo papel do investimento") + " — gera "
            "demanda (multiplicador) e capacidade produtiva (acelerador). O crescimento equilibrado exige que "
            "os dois andem juntos, o que leva à instabilidade do “fio da navalha”.",
        ],
        "dissecando": (cz("[troca de conceito · anacronismo]") + " Primeira oração verdadeira para ganhar "
                       "confiança; na segunda, o determinante do crescimento neoclássico (PTF) é transplantado "
                       "para o modelo keynesiano. Pista: Harrod-Domar não tem progresso técnico — qualquer menção "
                       "a tecnologia ou PTF como motor do modelo é suspeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Harrod-Domar, a taxa de crescimento é o produto da taxa de poupança pela relação "
            "produto-capital.”</i> → CERTO",
            "<i>“No modelo de Solow com progresso técnico, a taxa de crescimento de longo prazo do produto per "
            "capita é determinada pela taxa de poupança.”</i> → ERRADO (troca de conceito: é pela taxa de "
            "progresso técnico)",
        ])],
        "reescrita": ("No modelo de Harrod-Domar, o produto de uma economia é função do estoque de capital, e a taxa "
                      "de crescimento de longo prazo é determinada " + hl("pela taxa de poupança e pela relação "
                      "capital-produto (g = s/v)") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "ANACRONISMO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Vários comentários de professores: g = s × (relação produto-capital); PTF é o resíduo "
                            "de Solow. Um deles afirma que no Harrod-Domar o crescimento depende do progresso "
                            "técnico e do crescimento ponderado de capital e trabalho (equação neoclássica).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "976907-b4f5…png, 976907-233a…png", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "irrecuperavel (fórmulas refeitas no 📖)"},
                          {"ref": "image (255), (256), (257), (260), (261).png", "tipo_fonte": "QUESTÃO EM IMAGEM",
                           "lado": "verso", "acao": "irrecuperavel (imagens do verso não preservadas)"}],
        "alertas": [ALERTA_BANCA_2019,
                    "qualidade_fonte: um dos comentários descreve a taxa de crescimento do Harrod-Domar pela "
                    "decomposição neoclássica (tecnologia + trabalho + capital ponderados); corrigido para "
                    "g = s/v",
                    "quase_duplicata: ECO-E1-0706-1, ECO-E2-L00523-1 (g = s/v)"],
    },
    # ------------------------------------------------------------------ E1-0716
    {
        "id": "ECO-E1-0716-1", "fonte_ref": "E1-0716", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": CMD_GEN,
        "rotulo_item": "Item",
        "assertiva": ("Uma característica definidora dos modelos de crescimento endógeno mais recentes é a "
                      "incorporação da inovação tecnológica como variável interna, decorrente das decisões dos "
                      "agentes econômicos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma característica definidora dos modelos de crescimento endógeno mais recentes é a "
                      "incorporação da inovação tecnológica como <u>variável interna</u>, decorrente das "
                      "<u>decisões dos agentes econômicos</u>."),
        "poucas": ("É a definição de " + azb("crescimento endógeno") + ": o progresso técnico, exógeno no Solow, "
                   "passa a ser explicado dentro do modelo, como resultado de escolhas de firmas e pessoas (P&D, "
                   "educação, aprendizado)."),
        "destrinchando": [
            "No " + oc("Solow") + ", a tecnologia A cresce a uma taxa g dada — “cai do céu”. Como só g gera "
            "crescimento per capita no longo prazo, o modelo deixa sem explicação justamente o motor do "
            "crescimento.",
            "Primeira geração endógena: " + oc("Romer") + " (1986) — " + azb("learning-by-doing") + " e "
            "transbordamentos de conhecimento (ideia de " + oc("Arrow") + ", 1962) eliminam os rendimentos "
            "decrescentes do capital agregado; " + oc("Lucas") + " (1988) — acumulação de " + azb("capital "
            "humano") + "; modelos " + azb("AK") + " (" + oc("Rebelo") + ", 1991).",
            "Segunda geração, a dos “mais recentes”: " + oc("Romer") + " (1990) cria um setor de P&D movido "
            "pelo lucro de monopólio das patentes; as " + azb("ideias") + " são " + azb("não rivais") + " (um uso "
            "não impede outro) e parcialmente excludentes. " + oc("Aghion e Howitt") + " (1992) e " + oc("Grossman "
            "e Helpman") + " (1991) seguem a linha schumpeteriana. Romer ganhou o Nobel em 2018.",
            "Consequência de política: subsídio a P&D, proteção de patentes, educação e abertura a ideias podem "
            "alterar a taxa de crescimento de longo prazo — algo que, no Solow, nenhuma política consegue.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. As versões ERRADAS que a banca usa: "
                       "“tecnologia exógena” nos modelos endógenos, “rendimentos decrescentes do capital” como "
                       "marca do modelo AK ou a atribuição da endogeneização a Solow."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nos modelos de crescimento endógeno, o progresso técnico é tratado como variável exógena, tal "
            "como no modelo de Solow.”</i> → ERRADO (inversão)",
            "<i>“No modelo de Romer (1990), o conhecimento é um bem não rival, o que permite rendimentos "
            "crescentes na produção de ideias.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Comentários de professores: Solow tratava a tecnologia como exógena; Romer e Lucas a "
                            "endogeneizam como resultado de decisões de P&D e de capital humano.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (253), (254), (259).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "verso",
                           "acao": "irrecuperavel (imagens do verso não preservadas; conteúdo no 📖)"}],
        "alertas": [ALERTA_BANCA_2019,
                    "quase_duplicata: ECO-E2-L00621-1 (mesma definição, prova Nabuco)"],
    },
    # ------------------------------------------------------------------ E1-0717
    {
        "id": "ECO-E1-0717-1", "fonte_ref": "E1-0717", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_GEN,
        "rotulo_item": "Item",
        "assertiva": ("Schumpeter cunhou a expressão “destruição criadora” para descrever o processo pelo qual as "
                      "inovações revolucionam a estrutura econômica a partir de dentro, destruindo incessantemente "
                      "o antigo e criando elementos novos. Esse processo de destruição criadora é básico para se "
                      "entender o capitalismo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Schumpeter cunhou a expressão “destruição criadora” para descrever o processo pelo qual as "
                      "inovações revolucionam a estrutura econômica <u>a partir de dentro</u>, destruindo "
                      "incessantemente o antigo e criando elementos novos. Esse processo de destruição criadora é "
                      "básico para se entender o capitalismo."),
        "poucas": ("O item parafraseia " + oc("Schumpeter") + " em <i>Capitalismo, Socialismo e Democracia</i> "
                   "(" + vd("1942") + "): a mutação industrial que revoluciona a estrutura econômica “de dentro”, "
                   "destruindo o velho e criando o novo, é o " + azb("fato essencial do capitalismo") + "."),
        "destrinchando": [
            "Três ideias do trecho: (1) a mudança é " + azb("endógena") + " — nasce da própria concorrência "
            "capitalista, não de choques externos; (2) é " + azb("descontínua") + " — revoluções na estrutura "
            "produtiva, não ajustes marginais; (3) é " + azb("constitutiva") + " — o capitalismo é, por "
            "natureza, um método de transformação econômica e nunca pode ser estacionário.",
            "O agente é o " + azb("empresário inovador") + ", que introduz novas combinações; o " + azb("crédito")
            + " bancário lhe dá o poder de compra; os imitadores difundem a inovação; os que não se adaptam são "
            "eliminados. Daí os " + azb("ciclos") + " (Schumpeter os associou às ondas longas de "
            + oc("Kondratiev") + ").",
            "Exemplos clássicos: a ferrovia contra a diligência, a lâmpada elétrica contra a vela, o smartphone "
            "contra a câmera e o GPS dedicados, o streaming contra as locadoras.",
            "Detalhe de história do pensamento: a expressão já aparecia antes, em " + oc("Werner Sombart")
            + " (1913); foi Schumpeter quem a consagrou na economia. Em prova, “Schumpeter cunhou” é tratado como "
            "correto.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Reprodução quase literal do capítulo 7 de "
                       "<i>Capitalismo, Socialismo e Democracia</i>. A armadilha possível seria trocar “de dentro” "
                       "por “de fora” ou dizer que o processo leva ao equilíbrio estacionário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Schumpeter, a destruição criadora resulta de choques externos ao sistema econômico, como "
            "guerras e mudanças demográficas.”</i> → ERRADO (o processo é endógeno)",
            "<i>“Schumpeter via no capitalismo um sistema que, por natureza, nunca pode ser "
            "estacionário.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Vários comentários concordantes: destruição criadora como motor do capitalismo; "
                            "exemplos (streaming, lâmpada, celular); papel do empreendedor e da imitação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (231).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada)"}],
        "alertas": [ALERTA_BANCA_2019.replace("formato C/E", "formato C/E, ano 2022"),
                    "quase_duplicata: ECO-E1-0452-1, ECO-E2-L00620-1 (destruição criadora)"],
    },
    # ------------------------------------------------------------------ E1-0729
    {
        "id": "ECO-E1-0729-1", "fonte_ref": "E1-0729", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_GEN,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de crescimento econômico de Harrod-Domar, a taxa garantida de crescimento – ou "
                      "seja, aquela que mantém o equilíbrio entre a taxa de poupança e investimento de longo prazo e "
                      "garante que o estoque de capital disponível, em cada ponto do tempo, seja suficiente para "
                      "produzir a quantidade de bens que as firmas desejam – é instável e, portanto, improvável que "
                      "coincida com a taxa de crescimento natural."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de crescimento econômico de Harrod-Domar, a <u>taxa garantida</u> de crescimento – "
                      "ou seja, aquela que mantém o equilíbrio entre a taxa de poupança e investimento de longo prazo "
                      "e garante que o estoque de capital disponível, em cada ponto do tempo, seja suficiente para "
                      "produzir a quantidade de bens que as firmas desejam – é <u>instável</u> e, portanto, "
                      "<u>improvável</u> que coincida com a taxa de crescimento natural."),
        "poucas": ("Harrod distingue a " + azb("taxa garantida") + " (g<sub>w</sub> = s/v, que satisfaz os "
                   "empresários) da " + azb("taxa natural") + " (g<sub>n</sub> = n + progresso técnico, que mantém "
                   "o pleno emprego). Nada as iguala, e a garantida é um equilíbrio instável: o pleno emprego com "
                   "crescimento equilibrado é obra do acaso."),
        "destrinchando": [
            "Três taxas em " + oc("Harrod") + " (1939): a " + vd("efetiva") + " (g, a que de fato ocorre); a "
            + vd("garantida") + " (g<sub>w</sub> = s/v: com ela, o capital existente é exatamente o desejado e "
            "os empresários repetem suas decisões); a " + vd("natural") + " (g<sub>n</sub>: crescimento da força "
            "de trabalho mais o da produtividade do trabalho, teto do crescimento com pleno emprego).",
            "Primeiro problema — " + azb("instabilidade") + " (o “fio da navalha”): se g > g<sub>w</sub>, falta "
            "capacidade, as firmas investem mais, a demanda cresce ainda mais (multiplicador) e o desvio se "
            "amplia; se g &lt; g<sub>w</sub>, sobra capacidade, o investimento cai e a economia afunda. Os "
            "desvios são cumulativos.",
            "Segundo problema — " + azb("coincidência") + ": s, v e g<sub>n</sub> são determinados por fatores "
            "independentes (hábitos de poupança, tecnologia, demografia). Só por acaso s/v = g<sub>n</sub>. Se "
            "g<sub>w</sub> > g<sub>n</sub>, a economia tende à estagnação e à capacidade ociosa; se "
            "g<sub>w</sub> &lt; g<sub>n</sub>, ao desemprego estrutural crescente.",
            "Respostas teóricas: " + oc("Solow") + " (1956) torna v variável (substituição entre K e L) e faz "
            "g<sub>w</sub> se ajustar a g<sub>n</sub>; " + oc("Kaldor") + " e " + oc("Pasinetti") + " tornam s "
            "variável pela distribuição da renda entre salários e lucros.",
            vm("Regra-âncora: Harrod-Domar → g_w instável (fio da navalha) e g_w = g_n só por acaso."),
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " O enunciado é longo, mas a definição de taxa "
                       "garantida está correta, e os dois problemas de Harrod (instabilidade e coincidência "
                       "improvável) aparecem juntos. O “portanto” liga as duas ideias de forma frouxa, mas não "
                       "chega a criar um nexo falso: um equilíbrio instável também torna improvável o encontro com "
                       "g<sub>n</sub>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Harrod-Domar, a taxa garantida converge automaticamente para a taxa natural por "
            "meio de ajustes na relação capital-produto.”</i> → ERRADO (esse é o mecanismo de Solow)",
            "<i>“Se a taxa garantida supera a natural, o modelo de Harrod prevê tendência à estagnação, com "
            "capacidade ociosa crescente.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["improvável"], "dificuldade": 2,
        "comentario_fonte": "Taxa garantida g = s/c e taxa natural n = p + a, independentes; só coincidem por "
                            "acaso; g > n gera escassez de mão de obra e inflação, g &lt; n gera desemprego.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0740-1, ECO-E2-L01058-1, ECO-E2-L00765-1 (fio da navalha)"],
    },
    # ------------------------------------------------------------------ E1-0731
    {
        "id": "ECO-E1-0731-1", "fonte_ref": "E1-0731", "destino": "57", "subtema": H2["cresc"],
        "tipo": "ME", "banca": "FGV", "prova": "Senado Federal/Consultor (Área XX)/2022", "ano": 2022,
        "cacd": False, "errei": True,
        "comando": "Em relação ao modelo de crescimento de Harrod-Domar, analise as afirmativas a seguir.",
        "rotulo_item": "Questão",
        "assertiva": ("1. O aumento do investimento agregado resulta em: (i) aumento da demanda pelo produto e (ii) "
                      "aumento da capacidade da economia em elaborar o produto.</p><p>2. Existe o equilíbrio fio da "
                      "navalha, em que se um país sai da trajetória de equilíbrio de longo prazo, ele não retorna "
                      "mais a essa trajetória.</p><p>3. Se um país está em crescimento equilibrado, considerando uma "
                      "taxa de poupança de 10% e produtividade média social potencial do capital igual a 20%, então "
                      "as taxas de crescimento do investimento líquido e do produto devem ser iguais a 1%.</p><p>Está "
                      "correto o que se afirma em</p><p>(A) 1, 2 e 3.</p><p>(B) 1 e 2, apenas.</p><p>(C) 1 e 3, "
                      "apenas.</p><p>(D) 2 e 3, apenas.</p><p>(E) 2, apenas."),
        "gabarito": "B", "gabarito_origem": "fonte", "status": "normal",
        "anotada": ("❌ " + az("(A) 1, 2 ") + vm("e 3") + az(".") + "</p><p>✅ " + az("(B) 1 e 2, apenas.")
                    + "</p><p>❌ " + az("(C) 1 e ") + vm("3") + az(", apenas.") + "</p><p>❌ " + az("(D) 2 e ")
                    + vm("3") + az(", apenas.") + "</p><p>❌ " + az("(E) 2, ") + vm("apenas") + az(".")),
        "poucas": ("1 e 2 descrevem o " + azb("duplo papel do investimento") + " e o " + azb("fio da navalha")
                   + ". A 3 erra a conta: " + vd("g = s·σ = 10% × 20% = 2%") + ", não 1%."),
        "destrinchando": [
            "Afirmativa 1 — CERTA. É a contribuição central de " + oc("Domar") + " (1946): o investimento tem "
            + azb("duplo caráter") + " — pelo lado da demanda, gera renda via multiplicador (ΔY = ΔI/s); pelo "
            "lado da oferta, amplia a capacidade produtiva (ΔY<sub>potencial</sub> = σ·I). O crescimento "
            "equilibrado exige que a demanda cresça no ritmo da capacidade.",
            "Afirmativa 2 — CERTA. " + azb("Fio da navalha") + ": a trajetória de crescimento equilibrado é "
            "instável; um desvio da taxa efetiva em relação à garantida se amplia em vez de se corrigir, porque "
            "as decisões de investimento reforçam o desequilíbrio.",
            "Afirmativa 3 — ERRADA. σ é a “produtividade social média potencial do investimento” (termo de "
            "Domar; σ = 1/v, a relação produto-capital). Igualando o crescimento da demanda ao da capacidade: "
            + vd("ΔI/I = ΔY/Y = s·σ = 0,10 × 0,20 = 0,02 = 2%") + ". No crescimento equilibrado, investimento, "
            "produto e capital crescem todos a essa taxa.",
            "(A) ❌ inclui a 3. (B) ✅ só 1 e 2. (C) ❌ inclui a 3 e exclui a 2. (D) ❌ inclui a 3 e exclui a "
            "1. (E) ❌ exclui a 1, que é o próprio núcleo do modelo.",
            vm("Regra-âncora: Harrod-Domar → g = s·σ = s/v; investimento = demanda + capacidade."),
        ],
        "dissecando": (cz("[dado alterado]") + " A afirmativa falsa erra só o número (1% no lugar de 2%) e se "
                       "esconde atrás do nome pomposo “produtividade média social potencial do capital”, que é "
                       "apenas σ = 1/v. Quem não reconhece o termo de Domar tende a dividir (10%/20%… ou 20%/10%) "
                       "em vez de multiplicar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com taxa de poupança de 10% e relação capital-produto igual a 5, a taxa de crescimento "
            "equilibrado é de 2%.”</i> → CERTO (g = s/v = 0,10/5)",
            "<i>“No modelo de Harrod-Domar, o investimento afeta apenas a demanda agregada, como no modelo "
            "keynesiano de curto prazo.”</i> → ERRADO (restrição indevida: também cria capacidade)",
        ])],
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": ["apenas"], "dificuldade": 2,
        "comentario_fonte": "Comentário de professor: 1 certo (duplo papel), 2 certo (instabilidade), 3 errado "
                            "(g = 0,10 × 0,20 = 2%); gabarito B; resumo do modelo (Lopes e Vasconcellos) com o "
                            "fio da navalha.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (237), (242)-(248), (250), (251).png", "tipo_fonte": "QUESTÃO EM IMAGEM",
                           "lado": "verso", "acao": "irrecuperavel (imagens do verso não preservadas)"}],
        "alertas": ["banca_confirmada: concurso do Senado Federal de 2022 organizado pela FGV",
                    "texto_corrigido: “Harro-Domar” → “Harrod-Domar” (erro de digitação da fonte)"],
    },
    # ------------------------------------------------------------------ E1-0733
    {
        "id": "ECO-E1-0733-1", "fonte_ref": "E1-0733", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": CMD_DANIEL,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de Harrod-Domar conclui que uma economia não alcança o pleno emprego e taxas estáveis "
                      "de crescimento naturalmente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo de Harrod-Domar conclui que uma economia não alcança o pleno emprego e taxas "
                      "estáveis de crescimento <u>naturalmente</u>."),
        "poucas": ("Conclusão keynesiana de " + oc("Harrod") + ": não há mecanismo de mercado que leve a "
                   "economia ao " + azb("crescimento equilibrado com pleno emprego") + " — a taxa garantida é "
                   "instável e só por acaso coincide com a natural."),
        "destrinchando": [
            "O pleno emprego com crescimento estável exigiria duas condições ao mesmo tempo: g (efetiva) = "
            "g<sub>w</sub> = s/v (capital desejado = capital existente) e g<sub>w</sub> = g<sub>n</sub> (força de "
            "trabalho plenamente empregada). Como s, v e g<sub>n</sub> são dados independentes, o encontro é "
            "fortuito — a “" + azb("idade de ouro") + "”, na expressão de " + oc("Joan Robinson") + ".",
            "Mesmo que a economia esteja em g<sub>w</sub>, qualquer choque a afasta cumulativamente: é o "
            + azb("fio da navalha") + ". Não há preço que se ajuste para corrigir (salário e juros não substituem "
            "capital por trabalho, porque v é fixo).",
            "Daí a mensagem de política: o crescimento estável com pleno emprego depende de " + azb("ação do "
            "Estado") + " (política fiscal anticíclica, planejamento do investimento) — a extensão dinâmica da "
            "conclusão de " + oc("Keynes") + " de que o mercado não garante o pleno emprego.",
            "Contraste neoclássico: no " + oc("Solow") + " (1956), com substituição entre fatores e preços "
            "flexíveis, a economia converge sozinha para o estado estacionário com pleno emprego — o "
            "“naturalmente” que o Harrod-Domar nega.",
        ],
        "dissecando": (cz("[literalidade]") + " Item curto, que cobra a conclusão política do modelo. O "
                       "“naturalmente” (= por mecanismos de mercado) é a palavra-chave: o pleno emprego "
                       "<b>pode</b> ocorrer, mas não é garantido. Trocar Harrod-Domar por Solow inverteria o "
                       "gabarito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Solow conclui que uma economia não alcança naturalmente taxas estáveis de "
            "crescimento.”</i> → ERRADO (troca de ator: Solow converge ao estado estacionário)",
            "<i>“No modelo de Harrod-Domar, o crescimento equilibrado com pleno emprego é impossível.”</i> → "
            "ERRADO (modulador absoluto: é possível, mas improvável e instável)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["naturalmente"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito CERTO, uma imagem não preservada e o link do canal do "
                            "Telegram.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (240).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; comentário refeito no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0736-1 (mesmo professor; ausência de equilíbrio automático)"],
    },
    # ------------------------------------------------------------------ E1-0736
    {
        "id": "ECO-E1-0736-1", "fonte_ref": "E1-0736", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DANIEL,
        "rotulo_item": "Item",
        "assertiva": ("O Modelo Harrod-Domar de crescimento econômico apresenta uma grande simplicidade e, na medida "
                      "em que dá primazia à acumulação de capital e não garante qualquer equilíbrio automático da "
                      "economia através dos mecanismos de mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Modelo Harrod-Domar de crescimento econômico apresenta uma grande simplicidade e, na medida "
                      "em que dá <u>primazia à acumulação de capital</u> e <u>não garante qualquer equilíbrio "
                      "automático</u> da economia através dos mecanismos de mercado."),
        "poucas": ("As três características estão certas: modelo " + azb("simples") + " (g = s/v), centrado na "
                   + azb("acumulação de capital") + " e sem " + azb("mecanismo automático de equilíbrio") + " (fio "
                   "da navalha)."),
        "destrinchando": [
            azb("Simplicidade") + ": duas relações bastam. Pelo lado da oferta, a relação marginal "
            "produto-capital (quanto a produção aumenta quando o investimento eleva o estoque de capital em uma "
            "unidade); pelo lado da demanda, a propensão marginal a poupar. Delas sai " + vd("g = s/v")
            + ". Foi justamente essa simplicidade que o tornou ferramenta de planejamento.",
            azb("Primazia da acumulação de capital") + ": o produto depende só do capital (Y = K/v); o trabalho "
            "é suposto abundante e não há progresso técnico. Crescer = investir. Daí a leitura desenvolvimentista "
            "dos anos 1950: países pobres crescem pouco porque poupam pouco.",
            azb("Sem equilíbrio automático") + ": proporções fixas impedem a substituição entre capital e "
            "trabalho; a taxa garantida é instável (" + azb("fio da navalha") + ") e só por acaso coincide com a "
            "natural. Os mercados não corrigem os desvios — eles os amplificam.",
            "Por isso o modelo é classificado como " + azb("keynesiano") + " (ou pós-keynesiano) de crescimento, "
            "em oposição ao neoclássico de " + oc("Solow") + ", em que a relação capital-produto se ajusta e a "
            "economia converge.",
        ],
        "dissecando": (cz("[literalidade]") + " Item descritivo, com redação truncada (“e, na medida em que dá… "
                       "e não garante…” fica sem a oração principal), mas sem afirmação falsa. Atenção ao "
                       "“qualquer”: aqui ele é exato, porque o modelo não tem mecanismo de mercado algum de volta "
                       "ao equilíbrio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Harrod-Domar dá primazia ao progresso tecnológico como motor do crescimento.”</i> → "
            "ERRADO (troca de conceito: a primazia é da acumulação de capital)",
            "<i>“No modelo de Harrod-Domar, os mecanismos de mercado garantem a convergência para a taxa "
            "natural.”</i> → ERRADO (inversão)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["qualquer"], "dificuldade": 1,
        "comentario_fonte": "Link para texto da FGV-EAESP sobre o modelo Harrod-Domar; modelo baseado na relação "
                            "marginal produto-capital (oferta) e na propensão marginal a poupar (demanda).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: assertiva mantida fiel, com a construção truncada da fonte (“e, na medida em "
                    "que dá… e não garante…”)",
                    "quase_duplicata: ECO-E1-0733-1"],
    },
    # ------------------------------------------------------------------ E1-0740
    {
        "id": "ECO-E1-0740-1", "fonte_ref": "E1-0740", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Aula 8 - Macro", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_A8,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de Harrod-Domar, a taxa de crescimento do produto é um equilíbrio estável, isto é, "
                      "uma vez fora do equilíbrio, a economia tem mecanismos que a conduzem naturalmente de volta à "
                      "trajetória de crescimento equilibrado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo de Harrod-Domar, a taxa de crescimento do produto é um equilíbrio ")
                    + vm("estável") + az(", isto é, uma vez fora do equilíbrio, a economia ") + vm("tem")
                    + az(" mecanismos que a ") + vm("conduzem") + az(" naturalmente de volta à trajetória de "
                                                                     "crescimento equilibrado.")),
        "poucas": ("É o contrário: no Harrod-Domar o crescimento equilibrado é " + vm("instável") + " — o "
                   + azb("fio da navalha") + ". Quem tem equilíbrio estável, com retorno automático, é o modelo de "
                   + oc("Solow") + "."),
        "destrinchando": [
            "Mecanismo da instabilidade (" + oc("Harrod") + ", 1939): se a taxa efetiva supera a garantida "
            "(s/v), o capital fica aquém do desejado; as firmas aceleram o investimento, a demanda cresce ainda "
            "mais pelo multiplicador e o desvio aumenta. Se fica abaixo, sobra capacidade, o investimento cai e "
            "a economia se afasta para baixo. Os desvios são " + vd("cumulativos") + ".",
            "Raiz técnica: proporções fixas (v constante) e poupança s fixa. Não há variável de preço que mude "
            "a intensidade de capital ou a poupança para trazer a economia de volta.",
            "No " + oc("Solow") + " (1956), com rendimentos marginais decrescentes e substituição entre K e L, "
            "fora do estado estacionário a economia volta sozinha: se k &lt; k*, s·f(k) > (n+δ)k e k sobe; se "
            "k > k*, k cai. É o equilíbrio " + vd("globalmente estável") + ".",
            "Atenção à palavra “instável”: não significa que a economia oscile em torno do equilíbrio, e sim "
            "que ela se afasta dele depois de qualquer perturbação.",
            vm("Regra-âncora: Harrod-Domar = instável (fio da navalha); Solow = estável (convergência a k*)."),
        ],
        "dissecando": (cz("[troca de ator · inversão]") + " O item cola a propriedade do Solow (estabilidade) no "
                       "Harrod-Domar. A explicação depois do “isto é” é coerente com o “estável”, o que dá "
                       "falsa segurança: o erro está na premissa, não na definição. 🔥 Cobrança recorrente: "
                       "fio da navalha × convergência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Solow, uma vez fora do estado estacionário, a economia tem mecanismos que a "
            "conduzem de volta a ele.”</i> → CERTO",
            "<i>“O modelo de Solow apresenta o equilíbrio em fio de navalha.”</i> → ERRADO (troca de ator: é o "
            "Harrod-Domar)",
        ])],
        "reescrita": ("No modelo de Harrod-Domar, a taxa de crescimento do produto é um equilíbrio "
                      + hl("instável") + ", isto é, uma vez fora do equilíbrio, a economia " + hl("não tem")
                      + " mecanismos que a " + hl("conduzam") + " naturalmente de volta à trajetória de "
                      "crescimento equilibrado."),
        "tipo_erro": ["TROCA_ATOR", "INVERSAO"], "moduladores": ["naturalmente"], "dificuldade": 1,
        "comentario_fonte": "Equilíbrio estável é o de Solow; Harrod-Domar tem equilíbrio instável, o fio da "
                            "navalha.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00765-1, ECO-E2-L01058-1, ECO-E1-0729-1 (fio da navalha)"],
    },
    # ------------------------------------------------------------------ E1-0741
    {
        "id": "ECO-E1-0741-1", "fonte_ref": "E1-0741", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Aula 8 - Macro", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_A8,
        "rotulo_item": "Item",
        "assertiva": ("A teoria do desenvolvimento de Schumpeter rejeita a noção do fluxo circular da renda, "
                      "introduzindo o papel das inovações tecnológicas, e também rejeita a noção da neutralidade "
                      "monetária, tendo o crédito e a capacidade de criação de poder de compra pelo sistema "
                      "bancário um papel fundamental no desenvolvimento econômico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria do desenvolvimento de Schumpeter rejeita a noção do fluxo circular da renda, "
                      "introduzindo o papel das inovações tecnológicas, e também rejeita a noção da <u>neutralidade "
                      "monetária</u>, tendo o <u>crédito</u> e a capacidade de criação de poder de compra pelo "
                      "sistema bancário um papel fundamental no desenvolvimento econômico."),
        "poucas": ("Em " + oc("Schumpeter") + ", o desenvolvimento é a " + azb("ruptura do fluxo circular")
                   + " pelas inovações, e a moeda não é neutra: o " + azb("crédito bancário") + " cria o poder de "
                   "compra com que o empresário inovador retira recursos dos usos antigos."),
        "destrinchando": [
            "<i>Teoria do Desenvolvimento Econômico</i> (" + vd("1911") + "): o " + azb("fluxo circular") + " é a "
            "economia estacionária, que se repete ano a ano, sem lucro (além dos salários de gestão) e sem juro. "
            "Schumpeter o usa como ponto de partida e mostra que ele <b>não explica</b> o desenvolvimento, que "
            "só surge quando o empresário rompe a rotina com novas combinações.",
            "Moeda e crédito: o inovador não tem os meios de produção; precisa desviá-los de quem já os usa. O "
            "banqueiro — o “" + azb("éforo da economia de troca") + "”, nas palavras de Schumpeter — cria poder "
            "de compra novo (crédito sem poupança prévia) e o entrega ao inovador. A moeda é, assim, causa ativa "
            "do desenvolvimento, e não um véu neutro sobre a economia real.",
            "Juro e lucro: o " + azb("lucro") + " é o prêmio temporário da inovação (some com a imitação); o "
            + azb("juro") + " é uma parcela desse lucro paga ao banqueiro. No fluxo circular, sem inovação, não "
            "haveria juro.",
            "Contraste com a visão clássica e neoclássica da " + azb("neutralidade da moeda") + " (teoria "
            "quantitativa: moeda só afeta preços) e com a ideia de que o investimento depende de poupança "
            "prévia.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item longo, com duas “rejeições” verdadeiras. O "
                       "“rejeita o fluxo circular” é uma simplificação aceita pela banca: Schumpeter não nega o "
                       "fluxo circular como descrição da economia estacionária, mas o rejeita como explicação do "
                       "desenvolvimento. A pegadinha provável seria afirmar a neutralidade da moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Schumpeter, o financiamento das inovações depende exclusivamente da poupança prévia das "
            "famílias.”</i> → ERRADO (o crédito bancário cria poder de compra novo)",
            "<i>“Para Schumpeter, no fluxo circular, sem inovações, a taxa de juros tende a zero.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Verso repete a assertiva com “Certíssimo”.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0742
    {
        "id": "ECO-E1-0742-1", "fonte_ref": "E1-0742", "destino": "57", "subtema": H2["cresc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Aula 8 - Macro", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_A8,
        "rotulo_item": "Item",
        "assertiva": ("O processo de destruição criadora de Schumpeter é caracterizado pelo impacto das inovações no "
                      "sistema econômico, que embora sejam responsáveis pela dinâmica do desenvolvimento, podem "
                      "destruir empresas velhas e modelos de negócios ultrapassados, criando falências e "
                      "desemprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O processo de destruição criadora de Schumpeter é caracterizado pelo impacto das inovações no "
                      "sistema econômico, que embora sejam responsáveis pela dinâmica do desenvolvimento, <u>podem "
                      "destruir</u> empresas velhas e modelos de negócios ultrapassados, criando falências e "
                      "desemprego."),
        "poucas": ("A " + azb("destruição criadora") + " tem dois lados inseparáveis: a inovação gera "
                   "desenvolvimento e, ao mesmo tempo, " + vd("destrói") + " empresas, setores e empregos "
                   "ligados às técnicas antigas."),
        "destrinchando": [
            "A inovação traz lucro extraordinário ao pioneiro; os imitadores entram em enxame; a concorrência "
            "derruba preços e margens; quem ficou com a técnica antiga perde mercado e quebra. O desemprego "
            "aparece nos setores em declínio, enquanto os novos setores absorvem — com atraso e em outro lugar "
            "— parte da mão de obra.",
            "Para " + oc("Schumpeter") + ", esse lado destrutivo explica os " + azb("ciclos econômicos") + ": "
            "ondas de inovação geram expansão (crédito, investimento, euforia) e depois depressão (ajuste, "
            "falências, “limpeza” do sistema). As crises não são acidentes, mas parte do mecanismo.",
            "Exemplos: a máquina a vapor e os artesãos têxteis; o automóvel e os fabricantes de carroças; a "
            "fotografia digital e a Kodak; o streaming e as locadoras de vídeo.",
            "Debate atual: automação e inteligência artificial reacendem a discussão sobre o “desemprego "
            "tecnológico”. A teoria schumpeteriana sugere que o emprego total se recompõe no longo prazo, mas "
            "com custos concentrados em trabalhadores e regiões específicos — daí políticas de requalificação.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição correta, protegida por "
                       "“podem destruir”. O candidato pode estranhar a menção a falências e desemprego num "
                       "conceito “positivo”, mas a destruição é metade do processo. Variante ERRADA comum: "
                       "dizer que a destruição criadora não afeta o emprego ou que só ocorre em crises "
                       "externas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Schumpeter, as inovações sempre preservam as empresas existentes, que se adaptam "
            "gradualmente.”</i> → ERRADO (modulador absoluto e inversão)",
            "<i>“Na visão schumpeteriana, os ciclos econômicos estão ligados à difusão das inovações.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": "Verso repete a assertiva com “Certíssimo”.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0452-1, ECO-E1-0717-1 (destruição criadora)"],
    },
    # FIM
]
