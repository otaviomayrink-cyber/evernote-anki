"""Cards da passada 01 de ECO — lote de redação 11 (nota 04: teoria do consumidor)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "pref": "🧠 Preferências e axiomas",
    "util": "🎯 Utilidade e curvas de indiferença",
    "ro": "💵 Restrição orçamentária",
    "esc": "⚖️ Escolha ótima do consumidor",
    "dem": "📊 Demanda individual e de mercado",
}

COM_CACD26 = ("Considere um consumidor com função utilidade U = x₁x₂, em que x₁ e x₂ representam, respectivamente, as "
              "quantidades consumidas dos bens 1 e 2. Considere, ainda, que o preço do bem 1 seja p₁ = 10, o preço do "
              "bem 2 seja p₂ = 4, o rendimento do consumidor seja r = 80 e que o consumidor seja racional, prefira mais "
              "a menos (monotonicidade) e gaste toda a sua renda em x₁ e x₂. Com base nessas informações, e "
              "considerando que TMS seja a taxa marginal de substituição, julgue o item a seguir.")

COM_NIDI_A = ("Os agentes microeconômicos fazem suas escolhas de forma racional em um cenário de informações completas "
              "e simetricamente distribuídas. A respeito da Teoria do Consumidor, julgue certo ou errado (C ou E) os "
              "itens a seguir.")

COM_NIDI_B = "Com relação à teoria do comportamento do consumidor, julgue certo ou errado (C ou E) os itens a seguir."

COM_BOZAN = ("A análise das restrições orçamentárias e das escolhas do consumidor considera vários elementos centrais "
             "na microeconomia, incluindo preferências, renda, preços, e as curvas de indiferença. Com base nessa "
             "análise, julgue os itens a seguir.")

COM_ARMSTRONG = "Acerca da teoria do consumidor e da escolha ótima, julgue o item a seguir."

COM_NAB_MICRO = "Em relação à microeconomia, julgue (C ou E) os seguintes itens."

COM_NAB_TEORIA = ("Em relação aos princípios da teoria do consumidor e da teoria da demanda, julgue (C ou E) os itens que "
                  "se seguem.")

COM_NAB_FALHAS = ("No que se refere à teoria do consumidor e às falhas de mercado, julgue (C ou E) os seguintes itens.")

COM_NAB_CONS = "Com relação à teoria do consumidor, julgue (C ou E) os itens a seguir."

CARDS = [
    # ------------------------------------------------------------------ E1-0811
    {
        "id": "ECO-E1-0811-1", "fonte_ref": "E1-0811", "destino": "04", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": COM_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("No ponto ótimo, o gasto com o bem 1 é maior do que o gasto com o bem 2, pois o bem 1 é mais caro "
                      "e o consumidor maximiza a utilidade concentrando a renda no bem de maior preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No ponto ótimo, o gasto com o bem 1 ") + vm("é maior do que o") + az(" gasto com o bem 2, ")
                    + vm("pois o bem 1 é mais caro e o consumidor maximiza a utilidade concentrando a renda no bem de "
                         "maior preço") + az(".")),
        "poucas": ("Na " + azb("Cobb-Douglas") + " U = x₁x₂ (expoentes iguais), o consumidor gasta " + vd("metade da renda")
                   + " em cada bem, qualquer que seja o preço: " + vd("R$ 40 em cada") + " (x₁ = 4, x₂ = 10)."),
        "destrinchando": [
            "Condição de ótimo interior: " + azb("TMS = p₁/p₂") + ". Aqui TMS = UMg₁/UMg₂ = x₂/x₁; logo x₂/x₁ = 10/4 "
            "→ x₂ = 2,5x₁. Na restrição 10x₁ + 4x₂ = 80 → 10x₁ + 10x₁ = 80 → " + vd("x₁ = 4") + " e " + vd("x₂ = 10")
            + ".",
            "Gastos: p₁x₁ = 10 × 4 = " + vd("40") + "; p₂x₂ = 4 × 10 = " + vd("40") + ". Iguais. O bem mais caro é "
            "comprado em <b>menor quantidade</b>, exatamente na proporção que deixa o gasto constante.",
            "Regra geral da Cobb-Douglas U = x₁<sup>a</sup>x₂<sup>b</sup>: o gasto com cada bem é uma fração fixa da "
            "renda — " + vd("p₁x₁ = [a/(a+b)]·r") + " e " + vd("p₂x₂ = [b/(a+b)]·r") + ". Com a = b, metade para cada. "
            "Daí as demandas x₁ = a·r/[(a+b)p₁], com elasticidade-preço unitária (gasto constante quando o preço muda).",
            "Nada na teoria manda “concentrar a renda no bem mais caro”: o consumidor iguala a utilidade marginal "
            "<b>por real</b> (UMg₁/p₁ = UMg₂/p₂). Em x = (4; 10): UMg₁/p₁ = 10/10 = 1 e UMg₂/p₂ = 4/4 = 1.",
            vm("Regra-âncora: Cobb-Douglas → participações no gasto iguais aos pesos dos expoentes, independentes "
               "dos preços."),
        ],
        "dissecando": (cz("[nexo indevido · dado alterado]") + " O item inventa uma relação causal (bem caro → mais "
                       "gasto) que soa intuitiva e a apresenta como resultado da maximização. Quem resolve a conta "
                       "acha 40 = 40 em segundos; quem confia na intuição cai. 🔥 Cobb-Douglas com expoentes iguais é "
                       "presença constante no CACD: decore as participações fixas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No ponto ótimo, o consumidor adquire 4 unidades do bem 1 e 10 unidades do bem 2.”</i> → CERTO",
            "<i>“No ponto ótimo, a TMS é igual a 0,4.”</i> → ERRADO (razão invertida: TMS = p₁/p₂ = 2,5)",
            "<i>“Se p₁ dobrar, o gasto com o bem 1 dobrará.”</i> → ERRADO (permanece em 40: elasticidade unitária)",
        ])],
        "reescrita": ("No ponto ótimo, o gasto com o bem 1 é " + hl("igual ao") + " gasto com o bem 2 "
                      + hl("(R$ 40 em cada), pois, na Cobb-Douglas com expoentes iguais, o consumidor destina metade "
                           "da renda a cada bem, qualquer que seja o preço") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito (ERRADO), sem comentário.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0834
    {
        "id": "ECO-E1-0834-1", "fonte_ref": "E1-0834", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_A,
        "rotulo_item": "Item",
        "assertiva": ("Com exceção da relação entre bens substitutos, a taxa marginal de substituição entre dois bens é "
                      "geralmente expressa por uma taxa constante ao longo da curva de indiferença."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Com exceção da relação entre bens ") + vm("substitutos") + az(", a taxa marginal de "
                    "substituição entre dois bens é geralmente expressa por uma taxa ") + vm("constante")
                    + az(" ao longo da curva de indiferença.")),
        "poucas": ("O item inverte regra e exceção: a TMS em geral " + azb("varia") + " (é decrescente em módulo) ao "
                   "longo da curva; ela só é " + azb("constante") + " justamente no caso dos " + vd("substitutos "
                   "perfeitos") + "."),
        "destrinchando": [
            azb("TMS") + " = quanto de x₂ o consumidor aceita ceder por uma unidade a mais de x₁, mantendo a mesma "
            "utilidade; geometricamente, é a inclinação (em módulo) da curva de indiferença: TMS = UMg₁/UMg₂.",
            "Caso usual (preferências bem comportadas): curva convexa e " + azb("TMS decrescente") + ". Quem tem "
            "muito x₂ e pouco x₁ cede bastante x₂ por mais x₁; à medida que x₁ se acumula, cede cada vez menos.",
            "Exceções: " + azb("substitutos perfeitos") + " (U = ax₁ + bx₂) → curvas retas e TMS constante = a/b; "
            + azb("complementares perfeitos") + " (U = mín{ax₁, bx₂}) → curvas em L, TMS infinita no trecho vertical, "
            "nula no horizontal e indefinida no vértice.",
            "Atenção ao adjetivo: substitutos <b>imperfeitos</b> (café e chá) têm curvas convexas comuns, com TMS "
            "variável. Só o caso-limite “perfeito” produz a reta.",
            vm("Regra-âncora: TMS constante = curva reta = substitutos perfeitos; em geral, TMS decrescente."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item pega a exceção (TMS constante dos substitutos "
                       "perfeitos) e a transforma em regra, deixando os substitutos como a exceção. O “geralmente” "
                       "dá ar de prudência a uma afirmação invertida, e o “substitutos” sem “perfeitos” completa a "
                       "armadilha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para substitutos perfeitos, a taxa marginal de substituição é constante ao longo da curva de "
            "indiferença.”</i> → CERTO",
            "<i>“Para complementares perfeitos, a TMS é constante e igual a zero ao longo de toda a curva.”</i> → "
            "ERRADO (é infinita no trecho vertical, nula no horizontal e indefinida no vértice)",
        ])],
        "reescrita": ("Com exceção da relação entre bens substitutos " + hl("perfeitos") + ", a taxa marginal de "
                      "substituição entre dois bens é geralmente expressa por uma taxa " + hl("decrescente (em módulo)")
                      + " ao longo da curva de indiferença."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["geralmente"], "dificuldade": 1,
        "comentario_fonte": "Em curvas convexas usuais a TMS varia e é decrescente; TMS constante é o caso dos "
                            "substitutos perfeitos (curvas retas).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0835
    {
        "id": "ECO-E1-0835-1", "fonte_ref": "E1-0835", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_A,
        "rotulo_item": "Item",
        "assertiva": ("Considerando curvas de indiferença que satisfaçam os axiomas de completude, reflexividade e "
                      "transitividade, bem como a existência de apenas dois bens, é possível que as curvas de "
                      "indiferença de um consumidor que representem níveis distintos de preferência se cruzem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando curvas de indiferença que satisfaçam os axiomas de completude, reflexividade e "
                       "transitividade, bem como a existência de apenas dois bens, ") + vm("é possível")
                    + az(" que as curvas de indiferença de um consumidor que representem níveis distintos de "
                         "preferência se cruzem.")),
        "poucas": ("Curvas de indiferença de níveis distintos " + azb("não se cruzam") + ": o ponto de cruzamento "
                   "seria indiferente a cestas dos dois níveis e, pela " + azb("transitividade") + ", os dois níveis "
                   "seriam um só."),
        "destrinchando": [
            "Prova por absurdo: suponha I₁ e I₂ cruzando em A. A está nas duas, então A ~ C (C em I₁) e A ~ B (B em "
            "I₂). Pela transitividade da indiferença, " + vd("B ~ C") + ". Mas I₁ e I₂ representam níveis "
            "diferentes, e B e C deveriam ser estritamente ordenadas — contradição.",
            "Com " + azb("monotonicidade") + " a contradição fica visível: escolha B com o mesmo x₁ de C e mais x₂. "
            "“Mais é melhor” dá B ≻ C, e a transitividade dá B ~ C. As duas não podem valer juntas.",
            "Os axiomas de racionalidade: " + azb("completude") + " (compara quaisquer duas cestas), "
            + azb("reflexividade") + " (cada cesta é tão boa quanto ela mesma) e " + azb("transitividade") + " "
            "(consistência das comparações). É a transitividade que impede o cruzamento.",
            "Consequência prática: o mapa de indiferença “empilha” curvas sem interseção, e cada cesta pertence a "
            "uma única curva. Curvas mais afastadas da origem = utilidade maior (sob monotonicidade).",
        ],
        "grafico_verso": "ECO-E1-0835-1-V1",
        "dissecando": (cz("[contradição]") + " O item enumera corretamente os axiomas e conclui o oposto do que eles "
                       "implicam. O “é possível” soa como modulador relativo prudente, mas aqui é o erro: o "
                       "cruzamento é <b>logicamente impossível</b> sob transitividade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se as preferências não forem transitivas, as curvas de indiferença podem se cruzar.”</i> → CERTO",
            "<i>“Curvas de indiferença não se cruzam por causa do axioma da completude.”</i> → ERRADO (troca de "
            "axioma: é a transitividade)",
        ])],
        "reescrita": ("Considerando curvas de indiferença que satisfaçam os axiomas de completude, reflexividade e "
                      "transitividade, bem como a existência de apenas dois bens, " + hl("não é possível") + " que as "
                      "curvas de indiferença de um consumidor que representem níveis distintos de preferência se "
                      "cruzem."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": ["é possível"], "dificuldade": 1,
        "comentario_fonte": "Curvas de níveis distintos não se cruzam: o ponto de interseção seria indiferente às "
                            "cestas dos dois níveis e a transitividade igualaria os níveis.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0837
    {
        "id": "ECO-E1-0837-1", "fonte_ref": "E1-0837", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_A,
        "rotulo_item": "Item",
        "assertiva": ("Por causa do axioma da não-saciedade, que estabelece que os consumidores sempre desejam cestas "
                      "com uma maior quantidade de bens, sabemos que o aumento no consumo de um bem sempre provocará "
                      "um aumento do nível de utilidade de um indivíduo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Por causa do axioma da não-saciedade, que estabelece que os consumidores sempre desejam cestas "
                       "com uma maior quantidade de bens, ") + vm("sabemos que o aumento no consumo de um bem sempre "
                       "provocará") + az(" um aumento do nível de utilidade de um indivíduo.")),
        "poucas": ("Não saciedade (ou monotonicidade fraca) não garante que " + azb("mais de um único bem") + " eleve "
                   "a utilidade: com " + vd("complementares perfeitos") + ", mais sapatos esquerdos sem direitos não "
                   "acrescentam nada."),
        "destrinchando": [
            "Três hipóteses vizinhas, do mais fraco ao mais forte: " + azb("não saciedade local") + " (perto de "
            "qualquer cesta há outra estritamente preferida); " + azb("monotonicidade fraca") + " (mais de "
            "<b>todos</b> os bens é melhor); " + azb("monotonicidade forte") + " (mais de <b>pelo menos um</b> bem, "
            "sem menos dos outros, é estritamente melhor).",
            "Só a monotonicidade forte autoriza a conclusão do item. A não saciedade, mesmo na versão de livro "
            "“consumidores sempre desejam mais”, fala de cestas com mais bens, não de aumentar um bem isoladamente.",
            "Contraexemplo clássico: " + azb("complementares perfeitos") + ", U = mín{x₁, x₂}. Em (2; 2), passar a "
            "(3; 2) deixa U = 2. As preferências são não saciadas (basta aumentar os dois), mas o aumento de um bem "
            "só não muda a utilidade. Outros casos: " + azb("bens neutros") + " (utilidade marginal zero) e "
            + azb("males") + " (poluição, lixo), cuja quantidade adicional reduz a utilidade.",
            "Vocabulário: alguns manuais brasileiros chamam “mais é melhor” de não saciedade; outros reservam o nome "
            "para a versão local. Em qualquer leitura, o “sempre” sobre <b>um</b> bem exige a hipótese mais forte.",
        ],
        "dissecando": (cz("[extrapolação · modulador absoluto]") + " O item tira de uma hipótese sobre cestas uma "
                       "conclusão sobre cada bem isolado e a reforça com dois “sempre”. Pista: “cestas com maior "
                       "quantidade de bens” (no plural) virou “um bem” na conclusão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob monotonicidade forte, aumentar a quantidade de um bem, mantidas as dos demais, eleva a "
            "utilidade.”</i> → CERTO",
            "<i>“Com complementares perfeitos, aumentar apenas um dos bens sempre eleva a utilidade.”</i> → ERRADO "
            "(a utilidade não muda fora da proporção fixa)",
        ])],
        "reescrita": ("Por causa do axioma da não-saciedade, que estabelece que os consumidores sempre desejam cestas "
                      "com uma maior quantidade de bens, " + hl("não se pode concluir") + " que o aumento no consumo "
                      "de " + hl("um único bem, mantidos os demais,") + " sempre " + hl("provoque") + " um aumento do "
                      "nível de utilidade de um indivíduo" + hl(" — isso exigiria monotonicidade forte") + "."),
        "tipo_erro": ["EXTRAPOLACAO", "GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 2,
        "comentario_fonte": "Não saciedade local diz que sempre há cesta próxima preferível; não implica que cada "
                            "bem isolado aumente a utilidade (males, saciedade, compensações).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0838
    {
        "id": "ECO-E1-0838-1", "fonte_ref": "E1-0838", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_A,
        "rotulo_item": "Item",
        "assertiva": ("O bem-estar provocado pelo consumo adicional de cada unidade de um bem reflete a lei da "
                      "utilidade marginal decrescente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O bem-estar provocado pelo <u>consumo adicional de cada unidade</u> de um bem reflete a lei da "
                      "utilidade marginal decrescente."),
        "poucas": ("O acréscimo de satisfação de cada unidade extra é a " + azb("utilidade marginal") + "; a lei diz "
                   "que esse acréscimo tende a " + vd("cair") + " à medida que o consumo do bem aumenta."),
        "destrinchando": [
            azb("Utilidade total") + " (UT) = satisfação de todo o consumo; " + azb("utilidade marginal") + " (UMg) "
            "= ΔUT/Δq, o bem-estar trazido pela <b>última</b> unidade. O item descreve exatamente a UMg.",
            azb("Lei da utilidade marginal decrescente") + " (" + oc("Gossen") + ", 1854; retomada pelos "
            "marginalistas " + oc("Jevons") + ", " + oc("Menger") + " e " + oc("Walras") + " na década de 1870): "
            "mantido o resto constante, cada unidade adicional acrescenta menos que a anterior. O 1º copo d’água "
            "com sede vale muito; o 5º, pouco.",
            "UT cresce enquanto UMg > 0 e atinge o máximo quando " + vd("UMg = 0") + " (ponto de saciedade); além "
            "dele, UMg < 0 e a UT cai.",
            "Utilidade marginal decrescente resolve o " + azb("paradoxo da água e do diamante") + ": a água tem "
            "enorme utilidade total, mas, abundante, tem baixa utilidade marginal — e é a margem que forma o "
            "preço.",
            "Na teoria ordinal, a UMg decrescente não é necessária; o que importa é a " + azb("TMS decrescente")
            + ", que não depende da escala de utilidade.",
        ],
        "dissecando": (cz("[literalidade]") + " Paráfrase direta da definição: “bem-estar do consumo adicional de "
                       "cada unidade” = utilidade marginal. A tentação de marcar ERRADO vem da redação vaga "
                       "(“reflete”), que não diz se o bem-estar sobe ou cai — mas a lei é justamente a descrição "
                       "desse acréscimo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela lei da utilidade marginal decrescente, a utilidade total diminui a cada unidade adicional "
            "consumida.”</i> → ERRADO (troca total × marginal: a UT cresce enquanto UMg > 0)",
            "<i>“A utilidade total é máxima quando a utilidade marginal é nula.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Utilidade marginal = satisfação da unidade adicional; a lei diz que cada unidade "
                            "adicional tende a acrescentar menos que a anterior.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0839
    {
        "id": "ECO-E1-0839-1", "fonte_ref": "E1-0839", "destino": "04", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_A,
        "rotulo_item": "Item",
        "assertiva": ("Bens que apresentam nível de quantidade a partir do qual a satisfação adicional é negativa "
                      "apresentam uma curva de demanda crescente a partir dessa quantidade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Bens que apresentam nível de quantidade a partir do qual a satisfação adicional é negativa ")
                    + vm("apresentam uma curva de demanda crescente") + az(" a partir dessa quantidade.")),
        "poucas": ("Além do " + azb("ponto de saciedade") + " (UMg < 0), o consumidor simplesmente " + vd("não "
                   "compra") + " mais — nem de graça. Isso limita a quantidade demandada, mas não torna a demanda "
                   "crescente."),
        "destrinchando": [
            "Se a UMg fica negativa a partir de q<sub>s</sub>, unidades além de q<sub>s</sub> reduzem a satisfação. "
            "Com preço positivo, ninguém paga para piorar; mesmo com p = 0, o consumo para em q<sub>s</sub>. A "
            "demanda fica " + azb("limitada por q<sub>s</sub>") + ", não inclinada para cima.",
            "Na versão cardinal, a demanda individual nasce de UMg = λ·p: preço menor → consumo maior até que a UMg "
            "caia ao novo nível. Como a UMg é decrescente, a relação preço × quantidade é " + vd("negativa") + ".",
            "Demanda positivamente inclinada é outra coisa: o " + azb("bem de Giffen") + ", em que o efeito renda "
            "de um bem muito inferior supera o efeito substituição (o exemplo de livro é a batata na fome irlandesa). "
            "Nada a ver com saciedade.",
            "Também não confundir com " + azb("bens de Veblen") + " (ostentação), cuja demanda pode subir com o "
            "preço porque o próprio preço é fonte de utilidade.",
            vm("Regra-âncora: saciedade → teto de consumo; demanda crescente → Giffen ou Veblen."),
        ],
        "dissecando": (cz("[nexo indevido]") + " A premissa (UMg negativa após certo ponto) é verdadeira e "
                       "possível; o erro está na consequência inventada, que mistura saciedade com o caso Giffen. "
                       "Pista: “a partir dessa quantidade” — além dela o consumidor não compra, então não há curva "
                       "de demanda ali para ser crescente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um bem de Giffen apresenta curva de demanda positivamente inclinada.”</i> → CERTO",
            "<i>“Quando a utilidade marginal se torna negativa, a utilidade total atinge seu máximo e passa a "
            "crescer mais devagar.”</i> → ERRADO (a UT passa a cair)",
        ])],
        "reescrita": ("Bens que apresentam nível de quantidade a partir do qual a satisfação adicional é negativa "
                      + hl("não são consumidos além dessa quantidade, o que limita a demanda sem torná-la crescente")
                      + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "UMg negativa indica saciedade; isso não implica demanda positivamente inclinada, que "
                            "depende de preferências, renda e preços.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0840
    {
        "id": "ECO-E1-0840-1", "fonte_ref": "E1-0840", "destino": "04", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_B,
        "rotulo_item": "Item",
        "assertiva": ("Um consumidor com função de utilidade U(X, Y) = X⁴Y¹ gastará $20 de cada renda de $100 na "
                      "aquisição do bem Y."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um consumidor com função de utilidade U(X, Y) = X⁴Y¹ gastará <u>$20 de cada renda de $100</u> "
                      "na aquisição do bem Y."),
        "poucas": ("Na " + azb("Cobb-Douglas") + " U = X<sup>a</sup>Y<sup>b</sup>, a fração da renda gasta em Y é "
                   + vd("b/(a+b) = 1/5 = 20%") + ", independentemente dos preços: $20 de cada $100."),
        "destrinchando": [
            "Ótimo interior: TMS = UMg<sub>X</sub>/UMg<sub>Y</sub> = 4Y/X = p<sub>X</sub>/p<sub>Y</sub> → "
            + vd("p<sub>X</sub>X = 4·p<sub>Y</sub>Y") + ". O gasto com X é quatro vezes o gasto com Y.",
            "Na restrição p<sub>X</sub>X + p<sub>Y</sub>Y = R: 4p<sub>Y</sub>Y + p<sub>Y</sub>Y = R → "
            + vd("p<sub>Y</sub>Y = R/5") + " e " + vd("p<sub>X</sub>X = 4R/5") + ". Com R = 100: $20 em Y e $80 em X.",
            "Regra de bolso: os expoentes (normalizados pela soma) são as " + azb("participações no gasto") + ". "
            "Funções de demanda: Y = R/(5p<sub>Y</sub>) e X = 4R/(5p<sub>X</sub>) — cada demanda só depende do "
            "próprio preço e da renda.",
            "Corolários cobrados: elasticidade-preço da demanda " + vd("unitária") + " (gasto constante); "
            "elasticidade-renda " + vd("unitária") + " (curva de Engel reta pela origem); elasticidade-preço "
            "cruzada " + vd("nula") + ".",
            "Transformações monotônicas não alteram o resultado: U = X⁴Y, ln U = 4 ln X + ln Y ou U = X<sup>0,8</sup>"
            "Y<sup>0,2</sup> representam as mesmas preferências.",
        ],
        "dissecando": (cz("[detalhe]") + " Cálculo direto; a armadilha é inverter os pesos (80% em Y) ou achar que "
                       "falta informação por não haver preços. Na Cobb-Douglas, o gasto proporcional dispensa preços."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…gastará $80 de cada renda de $100 na aquisição do bem Y.”</i> → ERRADO (pesos invertidos: $80 "
            "vão para X)",
            "<i>“Se o preço de Y dobrar, o gasto com Y continuará sendo de $20.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Cobb-Douglas X⁴Y¹: fração da renda em Y = 1/(4+1) = 20%; com renda 100, gasto 20.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0841
    {
        "id": "ECO-E1-0841-1", "fonte_ref": "E1-0841", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_B,
        "rotulo_item": "Item",
        "assertiva": ("A hipótese da convexidade das preferências equivale à hipótese de taxa marginal de "
                      "substituição decrescente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("A hipótese da convexidade das preferências ") + vm("equivale à") + az(" hipótese de taxa "
                    "marginal de substituição decrescente.")),
        "poucas": ("Convexidade " + azb("implica") + " TMS não crescente, mas não “equivale” a TMS decrescente: "
                   "preferências convexas admitem retas (" + vd("substitutos perfeitos") + ", TMS constante) e "
                   "quinas (" + vd("complementares perfeitos") + ", TMS indefinida)."),
        "condicionais": [("⚠️ Gabarito contestável", "Em linguagem de manual introdutório, "
                          "convexidade e TMS decrescente são tratadas como as duas faces da mesma hipótese, e uma "
                          "banca poderia aceitar o item como CERTO. O ERRADO se sustenta no rigor do “equivale”: a "
                          "convexidade é definida sem derivadas e inclui casos de TMS constante ou indefinida.")],
        "destrinchando": [
            azb("Preferências convexas") + ": se x e y são indiferentes, qualquer média tx + (1−t)y é pelo menos "
            "tão boa quanto elas; o conjunto das cestas “pelo menos tão boas” é convexo. "
            + azb("Estritamente convexas") + ": a média é estritamente preferida.",
            "A definição não exige curvas suaves nem TMS: vale para os complementares perfeitos (L, sem derivada no "
            "vértice) e para os substitutos perfeitos (retas, TMS constante — convexos, mas não estritamente).",
            "Com curvas suaves e monotonicidade: convexidade ⇔ " + vd("|TMS| não crescente") + "; convexidade "
            "estrita ⇒ |TMS| decrescente. A ida “TMS decrescente ⇒ convexidade” vale; a volta, no sentido estrito, "
            "não.",
            "Por isso a frase segura é “a convexidade <b>reflete</b>/<b>se associa a</b> TMS decrescente”, e não "
            "“equivale”. Um item da Nabuco com a redação “reflete a hipótese de TMS decrescente” foi dado como "
            "CERTO — o verbo faz a diferença.",
        ],
        "dissecando": (cz("[generalização · troca de conceito]") + " O verbo “equivale” transforma uma associação "
                       "verdadeira no caso usual em uma equivalência lógica geral. 🔥 Itens de professor costumam "
                       "testar esses verbos de força (implica × equivale × reflete)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Preferências por substitutos perfeitos são convexas, embora não estritamente convexas.”</i> → "
            "CERTO",
            "<i>“Se a TMS é decrescente ao longo de curvas suaves, as preferências são convexas.”</i> → CERTO",
            "<i>“Preferências de complementares perfeitos não são convexas, pois a TMS não está definida no "
            "vértice.”</i> → ERRADO (são convexas; a convexidade não exige TMS)",
        ])],
        "reescrita": ("A hipótese da convexidade " + hl("estrita") + " das preferências" + hl(", com curvas de "
                      "indiferença suaves,") + " " + hl("implica a") + " hipótese de taxa marginal de substituição "
                      "decrescente."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["equivale"], "dificuldade": 3,
        "comentario_fonte": "Convexidade = preferência por combinações; TMS decrescente pode decorrer de "
                            "preferências suaves e estritamente convexas, mas as hipóteses não são equivalentes em "
                            "toda generalidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: em manuais introdutórios convexidade e TMS decrescente são apresentadas como "
                    "equivalentes; ERRADO mantido pelo rigor do “equivale” (cf. ECO-E2-L00671-1, CERTO com "
                    "“reflete”)"],
    },
    # ------------------------------------------------------------------ E1-0842
    {
        "id": "ECO-E1-0842-1", "fonte_ref": "E1-0842", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NIDI_B,
        "rotulo_item": "Item",
        "assertiva": ("Suponha que o consumidor só pode consumir quantidades não negativas dos bens e possui "
                      "preferências representadas pela seguinte função utilidade: U(x1, x2) = –x1x2. Pode-se afirmar "
                      "que as preferências desse consumidor satisfazem às propriedades de monotonicidade e "
                      "convexidade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Suponha que o consumidor só pode consumir quantidades não negativas dos bens e possui "
                       "preferências representadas pela seguinte função utilidade: U(x1, x2) = –x1x2. Pode-se "
                       "afirmar que as preferências desse consumidor ") + vm("satisfazem às propriedades de "
                       "monotonicidade e convexidade") + az(".")),
        "poucas": ("Com U = −x₁x₂, aumentar um bem (com o outro positivo) " + vd("reduz") + " a utilidade: não há "
                   + azb("monotonicidade") + ". E as cestas “melhores” ficam entre os eixos e a hipérbole — "
                   "conjunto " + vd("não convexo") + "."),
        "destrinchando": [
            "Monotonicidade: ∂U/∂x₁ = −x₂ ≤ 0 e ∂U/∂x₂ = −x₁ ≤ 0. Mais de um bem nunca melhora e, com o outro "
            "positivo, piora. Os dois bens são, na prática, " + azb("males") + "; a melhor cesta possível é a "
            "origem (U = 0).",
            "Convexidade: as curvas de indiferença são as mesmas hipérboles x₁x₂ = c da Cobb-Douglas, mas a direção "
            "de preferência se inverte. O conjunto “pelo menos tão bom” {−x₁x₂ ≥ −c} = {x₁x₂ ≤ c} é a região "
            "<b>abaixo</b> da hipérbole, que não é convexa.",
            "Teste numérico (c = 1): (10; 0,1) e (0,1; 10) têm x₁x₂ = 1. A média (5,05; 5,05) tem x₁x₂ ≈ "
            + vd("25,5") + " → U ≈ −25,5, muito pior. A média é <b>pior</b> que os extremos: a preferência favorece a "
            "especialização.",
            "Lição: a forma da curva de indiferença sozinha não diz se as preferências são convexas; é preciso saber "
            "<b>de que lado</b> estão as cestas preferidas. Uma transformação monotônica <b>decrescente</b> (o sinal "
            "de menos) inverte a ordenação.",
            vm("Regra-âncora: U = −f, com f bem comportada, inverte tudo — males no lugar de bens, especialização no "
               "lugar de diversificação."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item conta com o reflexo “x₁x₂ é Cobb-Douglas, logo bem "
                       "comportada” e esconde a inversão no sinal de menos. Pista: sempre teste a direção — "
                       "aumentar um bem eleva ou reduz U?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“As curvas de indiferença de U = −x₁x₂ têm o mesmo formato das de U = x₁x₂.”</i> → CERTO",
            "<i>“U = −x₁x₂ e U = x₁x₂ representam as mesmas preferências, pois diferem por uma transformação "
            "monotônica.”</i> → ERRADO (a transformação é decrescente: inverte a ordenação)",
        ])],
        "reescrita": ("Suponha que o consumidor só pode consumir quantidades não negativas dos bens e possui "
                      "preferências representadas pela seguinte função utilidade: U(x1, x2) = –x1x2. Pode-se afirmar "
                      "que as preferências desse consumidor " + hl("não satisfazem nem à monotonicidade nem à "
                      "convexidade") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Com U = −x₁x₂, aumentar um bem piora a utilidade: não há monotonicidade; os conjuntos "
                            "de preferência superior não satisfazem a convexidade usual.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00015
    {
        "id": "ECO-E2-L00015-1", "fonte_ref": "E2-L00015", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A curva de indiferença é convexa à origem, pois reflete o desejo do consumidor de diversificar "
                      "seu consumo. No entanto, não é possível que uma curva de indiferença seja côncava, pois isso "
                      "contrariaria o princípio de monotonicidade de preferências mais a mais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva de indiferença é convexa à origem, pois reflete o desejo do consumidor de diversificar "
                       "seu consumo. No entanto, ") + vm("não é possível que uma curva de indiferença seja côncava, "
                       "pois isso contrariaria o princípio de monotonicidade") + az(" de preferências mais a mais.")),
        "poucas": ("Curvas " + azb("côncavas") + " são possíveis: violam a " + azb("convexidade") + " (o consumidor "
                   "prefere especializar-se), não a " + azb("monotonicidade") + ", que só exige inclinação negativa."),
        "destrinchando": [
            "Cada hipótese molda um traço da curva: " + azb("monotonicidade") + " → inclinação " + vd("negativa")
            + " (para ganhar x₁ é preciso ceder x₂) e curvas mais altas melhores; " + azb("convexidade") + " → "
            "curvatura voltada para a origem (médias preferidas a extremos).",
            "Uma curva côncava (curvada para fora) continua negativamente inclinada — monotonicidade intacta. O que "
            "muda é a TMS, que passa a ser " + vd("crescente") + ": quanto mais x₁ o consumidor tem, mais x₂ aceita "
            "ceder por x₁ adicional. Resultado: ele prefere os extremos.",
            "Exemplo de manual: alguém que gosta de vinho e de refrigerante, mas não dos dois juntos na mesma "
            "refeição. O ótimo de preferências côncavas é uma " + azb("solução de canto") + ": todo o orçamento em "
            "um só bem, e a tangência seria um ponto de <b>mínimo</b>, não de máximo.",
            "A primeira frase do item está correta para o caso usual (bem comportado). O erro é proibir a "
            "concavidade e atribuir a proibição ao axioma errado.",
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " A 1ª frase, verdadeira, dá credibilidade; "
                       "a 2ª traz um “não é possível” e uma justificativa com o axioma trocado (monotonicidade no "
                       "lugar de convexidade). Pista: monotonicidade fala de <b>inclinação</b>; convexidade, de "
                       "<b>curvatura</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Curvas de indiferença positivamente inclinadas contrariariam a monotonicidade das preferências "
            "quando ambos são bens.”</i> → CERTO",
            "<i>“Com curvas de indiferença côncavas, o ponto de tangência com a restrição orçamentária maximiza a "
            "utilidade.”</i> → ERRADO (a tangência é um mínimo; o ótimo é de canto)",
        ])],
        "reescrita": ("A curva de indiferença é convexa à origem, pois reflete o desejo do consumidor de diversificar "
                      "seu consumo. No entanto, " + hl("é possível") + " que uma curva de indiferença seja côncava"
                      + hl(" — preferências não convexas, que favorecem a especialização —, sem contrariar") + " o "
                      "princípio de monotonicidade de preferências mais a mais."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["não é possível"], "dificuldade": 2,
        "comentario_fonte": "Curvas côncavas refletem especialização e são possíveis sem violar a monotonicidade; "
                            "a fonte as associa, por engano, a bens complementares.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem associa curvas côncavas a “preferências por bens "
                    "complementares”; complementares perfeitos geram curvas em L (convexas), não côncavas"],
    },
    # ------------------------------------------------------------------ E2-L00016
    {
        "id": "ECO-E2-L00016-1", "fonte_ref": "E2-L00016", "destino": "04", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A inclinação das curvas de indiferença corresponde à taxa marginal de substituição entre dois "
                      "bens e deve ser igual à razão entre os preços dos bens na escolha ótima do consumidor. No "
                      "entanto, essa igualdade de inclinações não é válida para substitutos perfeitos, onde a "
                      "maximização pode ocorrer sem que as inclinações sejam equivalentes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A inclinação das curvas de indiferença corresponde à taxa marginal de substituição entre dois "
                      "bens e deve ser igual à razão entre os preços dos bens na escolha ótima do consumidor. No "
                      "entanto, essa igualdade de inclinações não é válida para substitutos perfeitos, onde a "
                      "maximização <u>pode</u> ocorrer sem que as inclinações sejam equivalentes."),
        "poucas": ("A " + azb("tangência") + " (TMS = p₁/p₂) é a regra do ótimo interior; com " + azb("substitutos "
                   "perfeitos") + ", a TMS é constante e, se diferir de p₁/p₂, o ótimo é um " + vd("canto") + ", sem "
                   "igualdade."),
        "destrinchando": [
            "Inclinação da curva de indiferença = " + azb("TMS") + " = UMg₁/UMg₂ (em módulo). Inclinação da "
            "restrição orçamentária = " + azb("preço relativo") + " p₁/p₂. No ótimo interior de preferências "
            "convexas e suaves, as duas se igualam: a taxa a que o consumidor <b>quer</b> trocar coincide com a que "
            "o mercado <b>permite</b>.",
            "Substitutos perfeitos (U = ax₁ + bx₂, TMS = a/b constante): se " + vd("a/b > p₁/p₂") + ", só x₁ é "
            "comprado; se " + vd("a/b < p₁/p₂") + ", só x₂; se " + vd("a/b = p₁/p₂") + ", qualquer ponto da "
            "restrição é ótimo — e aí as inclinações coincidem. Daí o “pode” do item.",
            "Outros casos sem igualdade: " + azb("complementares perfeitos") + " (ótimo no vértice do L, onde a TMS "
            "não está definida) e preferências " + azb("côncavas") + " (ótimo de canto).",
            "No canto, vale uma desigualdade: o bem comprado oferece utilidade marginal por real maior ou igual à do "
            "bem não comprado (UMg₁/p₁ ≥ UMg₂/p₂ se só x₁ é consumido).",
        ],
        "dissecando": (cz("[exceção · modulador relativo]") + " O item ensina a regra e cobra a exceção, protegida "
                       "pelo “pode”. Se dissesse “nunca são equivalentes”, estaria ERRADO (caso a/b = p₁/p₂)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para substitutos perfeitos, a escolha ótima nunca apresenta igualdade entre a TMS e a razão de "
            "preços.”</i> → ERRADO (modulador absoluto: se forem iguais, toda a restrição é ótima)",
            "<i>“Na escolha ótima de complementares perfeitos, a TMS iguala a razão de preços no vértice.”</i> → "
            "ERRADO (no vértice a TMS não está definida)",
        ])],
        "tipo_erro": ["EXCECAO", "MODULADOR_RELATIVO"], "moduladores": ["deve", "pode"], "dificuldade": 1,
        "comentario_fonte": "Tangência TMS = preço relativo no ótimo usual; nos substitutos perfeitos a "
                            "maximização pode ocorrer num extremo, sem igualdade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00017
    {
        "id": "ECO-E2-L00017-1", "fonte_ref": "E2-L00017", "destino": "04", "subtema": H2["ro"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Quando ocorre uma variação na renda de um consumidor, a restrição orçamentária se desloca "
                      "paralelamente sem alterar sua inclinação. Já uma alteração nos preços modifica necessariamente "
                      "a inclinação da restrição orçamentária, impactando as possibilidades de consumo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quando ocorre uma variação na renda de um consumidor, a restrição orçamentária se desloca "
                       "paralelamente sem alterar sua inclinação. Já uma alteração nos preços modifica ")
                    + vm("necessariamente") + az(" a inclinação da restrição orçamentária, impactando as "
                                                 "possibilidades de consumo.")),
        "poucas": ("A inclinação é o " + azb("preço relativo") + " p₁/p₂. Se os " + vd("dois preços") + " variarem "
                   "na mesma proporção, ela não muda: a restrição só se desloca paralelamente, como numa variação "
                   "de renda."),
        "destrinchando": [
            "Restrição: p₁x₁ + p₂x₂ = R. Interceptos: R/p₁ (eixo x₁) e R/p₂ (eixo x₂). Inclinação: " + vd("−p₁/p₂")
            + ".",
            "Renda ↑ → interceptos sobem na mesma proporção → " + azb("deslocamento paralelo") + " para fora. "
            "Um preço só ↑ (p₁) → o intercepto de x₁ cai e a reta " + azb("gira") + " em torno do intercepto de x₂, "
            "ficando mais inclinada.",
            "Todos os preços ↑ k% com R constante → equivale a uma queda da renda real: a reta se desloca "
            "paralelamente para dentro. Preços e renda ↑ k% juntos → " + vd("nada muda") + " (homogeneidade de grau "
            "zero: sem ilusão monetária).",
            "Também não giram: impostos ou subsídios <b>ad valorem</b> uniformes sobre todos os bens. Já um "
            "imposto sobre um único bem gira a reta; um imposto <b>lump-sum</b> (fixo) a desloca paralelamente.",
            vm("Regra-âncora: inclinação = preço relativo; só muda se p₁/p₂ mudar."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " A 1ª frase é exata e o erro mora num advérbio: "
                       "“necessariamente”. Pista: “alteração nos preços” (plural, genérico) inclui a mudança "
                       "proporcional de todos eles."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a renda e todos os preços dobrarem, a restrição orçamentária permanece inalterada.”</i> → CERTO",
            "<i>“A elevação do preço de um dos bens desloca a restrição orçamentária paralelamente para "
            "dentro.”</i> → ERRADO (um preço só faz a reta girar)",
        ])],
        "reescrita": ("Quando ocorre uma variação na renda de um consumidor, a restrição orçamentária se desloca "
                      "paralelamente sem alterar sua inclinação. Já uma alteração nos preços modifica "
                      "<s>necessariamente</s> a inclinação da restrição orçamentária" + hl(", salvo se os dois preços "
                      "variarem na mesma proporção") + ", impactando as possibilidades de consumo."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": "Renda desloca paralelamente; preço altera a inclinação (rotação), salvo se os dois "
                            "preços mudarem na mesma direção e proporção.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00018
    {
        "id": "ECO-E2-L00018-1", "fonte_ref": "E2-L00018", "destino": "04", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": COM_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Uma solução de canto indica que o consumidor emprega toda sua renda na aquisição de apenas um "
                      "dos bens. Isso ocorre frequentemente para complementos perfeitos, onde o consumo de um bem "
                      "depende intrinsecamente do consumo do outro, forçando a escolha para um ponto extremo da "
                      "curva de restrição orçamentária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma solução de canto indica que o consumidor emprega toda sua renda na aquisição de apenas um "
                       "dos bens. Isso ocorre frequentemente para ") + vm("complementos perfeitos, onde o consumo de "
                       "um bem depende intrinsecamente do consumo do outro, forçando") + az(" a escolha para um "
                       "ponto extremo da curva de restrição orçamentária.")),
        "poucas": ("Canto é típico de " + azb("substitutos perfeitos") + " (e de preferências côncavas). Com "
                   + azb("complementos perfeitos") + ", o consumidor compra os " + vd("dois bens") + " na proporção "
                   "fixa: o ótimo fica no vértice do L, no interior da restrição."),
        "destrinchando": [
            azb("Solução de canto") + ": a cesta ótima tem quantidade zero de algum bem. Com dois bens, toda a renda "
            "vai para um só.",
            "Substitutos perfeitos (U = ax₁ + bx₂): o consumidor compara a/b com p₁/p₂ e compra só o bem que dá "
            "mais utilidade por real. Ex.: U = x₁ + x₂, p₁ = 2, p₂ = 4, R = 40 → " + vd("x₁ = 20, x₂ = 0") + ".",
            "Complementos perfeitos (U = mín{x₁, x₂}): comprar um sem o outro não gera utilidade. Com R = 40, p₁ = 2, "
            "p₂ = 4 → x₁ = x₂ = R/(p₁ + p₂) ≈ " + vd("6,67 de cada") + ". Justamente porque um bem “depende do "
            "outro”, o canto é a pior escolha possível.",
            "O canto também aparece com preferências " + azb("côncavas") + " (preferência por especialização) e, em "
            "preferências usuais, quando a TMS em um dos eixos já é menor que o preço relativo (bem muito caro ou "
            "pouco desejado).",
            vm("Regra-âncora: substitutos perfeitos → canto; complementos perfeitos → vértice com os dois bens."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca substitutos por complementos e ainda descreve "
                       "corretamente a complementaridade (“um bem depende do outro”) — o que, lido com atenção, "
                       "desmente a própria conclusão. 🔥 A dupla substitutos × complementos perfeitos é das trocas "
                       "mais frequentes em teoria do consumidor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com substitutos perfeitos, se a TMS for diferente da razão de preços, a escolha ótima será uma "
            "solução de canto.”</i> → CERTO",
            "<i>“Com complementos perfeitos, o consumidor gasta toda a renda no bem mais barato.”</i> → ERRADO "
            "(compra os dois na proporção fixa)",
        ])],
        "reescrita": ("Uma solução de canto indica que o consumidor emprega toda sua renda na aquisição de apenas um "
                      "dos bens. Isso ocorre frequentemente para " + hl("substitutos perfeitos, quando a taxa de troca "
                      "entre os bens difere da razão de preços, o que leva") + " a escolha para um ponto extremo da "
                      "curva de restrição orçamentária" + hl(" (com complementos perfeitos, o ótimo fica no vértice "
                      "do L, com os dois bens)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["frequentemente"], "dificuldade": 1,
        "comentario_fonte": "Canto é típico de substitutos perfeitos; com complementos perfeitos o ótimo é na "
                            "junção (proporção fixa).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00345
    {
        "id": "ECO-E2-L00345-1", "fonte_ref": "E2-L00345", "destino": "04", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_ARMSTRONG,
        "rotulo_item": "Item",
        "assertiva": ("No problema padrão de utilidade bem-comportada, o ponto ótimo exige (TMgS = Px/Py) e, "
                      "equivalentemente, (UMg_X/UMg_Y = Px/Py), o que implica (UMg_X/Px = UMg_Y/Py). Essa igualdade "
                      "vale inclusive em soluções de canto com bens perfeitamente complementares ou substitutos "
                      "perfeitos, pois a utilidade marginal por real sempre se iguala entre bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No problema padrão de utilidade bem-comportada, o ponto ótimo exige (TMgS = Px/Py) e, "
                       "equivalentemente, (UMg_X/UMg_Y = Px/Py), o que implica (UMg_X/Px = UMg_Y/Py). Essa igualdade ")
                    + vm("vale inclusive em soluções de canto com bens perfeitamente complementares ou substitutos "
                         "perfeitos, pois a utilidade marginal por real sempre se iguala entre bens") + az(".")),
        "poucas": ("A " + azb("equimarginalidade") + " (UMg/p igual entre bens) é condição de " + vd("ótimo "
                   "interior") + ". No canto, o bem comprado rende " + vd("mais") + " utilidade por real que o "
                   "outro; no vértice dos complementos, as UMg nem estão definidas."),
        "destrinchando": [
            "A cadeia da 1ª frase está correta: TMgS = UMg<sub>X</sub>/UMg<sub>Y</sub>; igualando a P<sub>X</sub>/"
            "P<sub>Y</sub> e rearranjando, " + vd("UMg<sub>X</sub>/P<sub>X</sub> = UMg<sub>Y</sub>/P<sub>Y</sub>")
            + ": o último real gasto em cada bem rende a mesma utilidade (" + oc("Gossen") + ", “segunda lei”).",
            "Por que vale no interior: se UMg<sub>X</sub>/P<sub>X</sub> > UMg<sub>Y</sub>/P<sub>Y</sub>, tirar um "
            "real de Y e pô-lo em X eleva a utilidade — o consumidor realoca até igualar. No " + azb("canto") + " "
            "(Y = 0) não há mais Y para tirar: a desigualdade " + vd("UMg<sub>X</sub>/P<sub>X</sub> ≥ UMg<sub>Y</sub>"
            "/P<sub>Y</sub>") + " persiste. São as condições de " + azb("Kuhn-Tucker") + ".",
            "Substitutos perfeitos (U = X + Y, P<sub>X</sub> = 1, P<sub>Y</sub> = 2): UMg/P = 1 para X e 0,5 para Y. "
            "Compra-se só X, com utilidades por real diferentes.",
            "Complementos perfeitos não costumam gerar canto: o ótimo é o vértice do L, com os dois bens. Ali a "
            "função não é diferenciável e a condição em UMg simplesmente não se aplica; o ótimo sai de X/Y = "
            "proporção fixa + restrição.",
        ],
        "dissecando": (cz("[generalização · meia-verdade]") + " A 1ª frase, técnica e correta, empresta "
                       "autoridade à 2ª, que estende a regra aos casos que são justamente suas exceções. Os "
                       "gatilhos: “inclusive” e “sempre”. Bônus de erro: complementos perfeitos citados como "
                       "fonte de canto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Numa solução de canto em que só X é consumido, UMg<sub>X</sub>/P<sub>X</sub> ≥ UMg<sub>Y</sub>"
            "/P<sub>Y</sub>.”</i> → CERTO",
            "<i>“Se UMg<sub>X</sub>/P<sub>X</sub> > UMg<sub>Y</sub>/P<sub>Y</sub> num ótimo interior, o consumidor "
            "deve reduzir o consumo de X.”</i> → ERRADO (inversão: deve aumentar X)",
        ])],
        "reescrita": ("No problema padrão de utilidade bem-comportada, o ponto ótimo exige (TMgS = Px/Py) e, "
                      "equivalentemente, (UMg_X/UMg_Y = Px/Py), o que implica (UMg_X/Px = UMg_Y/Py). Essa igualdade "
                      + hl("vale apenas em ótimos interiores com curvas suaves: não vale em soluções de canto "
                           "(típicas de substitutos perfeitos), em que o bem comprado tem utilidade marginal por "
                           "real maior ou igual à do outro, nem no vértice dos complementos perfeitos, onde as "
                           "utilidades marginais não estão definidas") + "."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["inclusive", "sempre"], "dificuldade": 2,
        "comentario_fonte": "UMg_X/Px = UMg_Y/Py vale em ótimos interiores; em cantos (substitutos perfeitos) não "
                            "se aplica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00346
    {
        "id": "ECO-E2-L00346-1", "fonte_ref": "E2-L00346", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": "Acerca do formato das curvas de indiferença, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Quanto maior a facilidade de substituição entre dois bens, mais forte (isto é, maior) a "
                      "convexidade das curvas de indiferença; já quando a substituição é difícil, as curvas tendem a "
                      "ser menos convexas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quanto maior a facilidade de substituição entre dois bens, ") + vm("mais forte (isto é, maior)")
                    + az(" a convexidade das curvas de indiferença; já quando a substituição é difícil, as curvas "
                         "tendem a ser ") + vm("menos") + az(" convexas.")),
        "poucas": ("Relação invertida: substituição " + azb("fácil") + " → curva quase " + vd("reta") + " (pouca "
                   "convexidade); substituição " + azb("difícil") + " → curva muito arqueada, no limite um "
                   + vd("L") + " (convexidade máxima)."),
        "destrinchando": [
            "A curvatura mede quão depressa a " + azb("TMS") + " muda ao longo da curva. Se o consumidor troca um "
            "bem pelo outro sem sofrimento, a taxa de troca quase não muda → curva achatada. Se a troca é difícil, "
            "a taxa despenca à medida que ele fica com pouco de um bem → curva bem “barriguda”.",
            "Extremos: " + azb("substitutos perfeitos") + " (duas marcas idênticas de água, notas de R$ 5 e de "
            "R$ 10) → retas, TMS constante, convexidade nula. " + azb("Complementares perfeitos") + " (sapato "
            "esquerdo e direito) → L, curvatura concentrada no vértice, máxima.",
            "Medida formal: a " + azb("elasticidade de substituição") + " σ (variação % de x₂/x₁ diante de "
            "variação % da TMS). σ → ∞ nos substitutos perfeitos; " + vd("σ = 1") + " na Cobb-Douglas; σ = 0 nos "
            "complementares perfeitos. " + vm("Quanto maior σ, menos convexa a curva.") ,
            "A família " + azb("CES") + " U = (ax₁<sup>ρ</sup> + bx₂<sup>ρ</sup>)<sup>1/ρ</sup> cobre todos os casos: "
            "σ = 1/(1 − ρ); ρ = 1 dá a reta, ρ → 0 a Cobb-Douglas, ρ → −∞ o L.",
        ],
        "grafico_verso": "ECO-E2-L00346-1-V1",
        "dissecando": (cz("[inversão]") + " Troca simétrica dos dois polos: tudo o que é dito de um extremo vale "
                       "para o outro. O “isto é, maior” reforça a inversão para parecer definição. Teste rápido: "
                       "imagine os substitutos perfeitos — reta — e veja se “mais convexa” faz sentido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a elasticidade de substituição entre dois bens, menos convexas são as curvas de "
            "indiferença.”</i> → CERTO",
            "<i>“Complementares perfeitos apresentam elasticidade de substituição infinita.”</i> → ERRADO "
            "(inversão: σ = 0; infinita é a dos substitutos perfeitos)",
        ]), ("🧠 Mnemônico", ["<b>Reta</b> = troca <b>r</b>ápida; <b>L</b> = <b>l</b>igados para sempre."])],
        "reescrita": ("Quanto maior a facilidade de substituição entre dois bens, " + hl("mais fraca (isto é, menor)")
                      + " a convexidade das curvas de indiferença; já quando a substituição é difícil, as curvas "
                      "tendem a ser " + hl("mais") + " convexas."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tendem"], "dificuldade": 2,
        "comentario_fonte": "Substituição fácil → menos convexidade (reta); difícil → mais convexidade (L). Vários "
                            "comentários didáticos repetidos, com exemplos (sapatos, notas de dinheiro) e mnemônico "
                            "gráfico.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 048", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00346-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00601
    {
        "id": "ECO-E2-L00601-1", "fonte_ref": "E2-L00601", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NAB_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("As curvas de indiferença ilustram as diferentes combinações de bens que um consumidor pode "
                      "adquirir, dada sua renda e os preços dos bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As curvas de indiferença ilustram as diferentes combinações de bens ") + vm("que um "
                    "consumidor pode adquirir, dada sua renda e os preços dos bens") + az(".")),
        "poucas": ("O item define a " + azb("restrição orçamentária") + " (o que o consumidor <b>pode</b> comprar). "
                   "A " + azb("curva de indiferença") + " reúne as cestas de " + vd("mesma utilidade") + " (o que ele "
                   "<b>quer</b>)."),
        "destrinchando": [
            "Os dois pilares da escolha do consumidor são independentes: " + azb("preferências") + " (curvas de "
            "indiferença — dependem só dos gostos) e " + azb("possibilidades") + " (restrição orçamentária — "
            "dependem só da renda e dos preços).",
            "Curva de indiferença: lugar das cestas que deixam o consumidor igualmente satisfeito. Não muda quando "
            "a renda ou os preços mudam; muda se mudarem os gostos.",
            "Restrição orçamentária: p₁x₁ + p₂x₂ = R; o conjunto orçamentário inclui também as cestas abaixo da "
            "reta. Muda com renda (deslocamento paralelo) e preços (rotação).",
            "O ótimo junta os dois: a curva de indiferença mais alta que ainda toca o conjunto orçamentário "
            "(tangência, no caso usual: TMS = p₁/p₂).",
            vm("Regra-âncora: indiferença = querer (gostos); orçamento = poder (renda e preços)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Clássica troca de definições entre os dois instrumentos do "
                       "modelo. Pista: qualquer menção a <b>renda</b> ou <b>preços</b> na definição denuncia a "
                       "restrição orçamentária, nunca a curva de indiferença."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento da renda do consumidor desloca suas curvas de indiferença para a direita.”</i> → ERRADO "
            "(renda desloca a restrição orçamentária; as curvas de indiferença só dependem dos gostos)",
            "<i>“A restrição orçamentária representa as combinações de bens que esgotam a renda do consumidor, "
            "dados os preços.”</i> → CERTO",
        ])],
        "reescrita": ("As curvas de indiferença ilustram as diferentes combinações de bens " + hl("que proporcionam "
                      "ao consumidor o mesmo nível de satisfação") + hl("; as que ele pode adquirir, dada sua renda e "
                      "os preços dos bens, formam a restrição orçamentária") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O item descreve a restrição orçamentária; curvas de indiferença reúnem cestas de mesma "
                            "utilidade, independentemente de preços e renda (comentários de E2-L00601 e da "
                            "duplicata E2-L00653 fundidos).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata fundida: E2-L00653 (mesmo item, comentário incorporado)"],
    },
    # ------------------------------------------------------------------ E2-L00616
    {
        "id": "ECO-E2-L00616-1", "fonte_ref": "E2-L00616", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": COM_NAB_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("O pressuposto de que “quanto mais de um bem, melhor” é formalizado pelo axioma da "
                      "monotonicidade das preferências, que implica que as curvas de indiferença são positivamente "
                      "inclinadas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O pressuposto de que “quanto mais de um bem, melhor” é formalizado pelo axioma da "
                       "monotonicidade das preferências, que implica que as curvas de indiferença são ")
                    + vm("positivamente") + az(" inclinadas.")),
        "poucas": ("Monotonicidade → curvas " + vd("negativamente") + " inclinadas: para manter a utilidade ao ganhar "
                   "mais de um bem, é preciso " + azb("abrir mão") + " do outro."),
        "destrinchando": [
            "Raciocínio em duas linhas: parta de uma cesta e aumente x₁. Pela monotonicidade, a utilidade sobe. "
            "Para voltar à mesma curva, x₂ tem de " + vd("cair") + ". Logo, ao longo da curva, x₁ ↑ ⇔ x₂ ↓: "
            "inclinação negativa.",
            "Se a curva fosse positivamente inclinada, haveria duas cestas indiferentes, uma com mais dos dois bens "
            "— absurdo sob “mais é melhor”.",
            "Outras consequências da monotonicidade: curvas mais afastadas da origem representam utilidade "
            "maior, e as curvas são “finas” (não há faixas de indiferença).",
            "Curvas positivamente inclinadas existem, mas com um " + azb("mal") + ": se x₂ é poluição, mais x₁ só "
            "compensa com mais x₂. Já curvas verticais ou horizontais indicam um " + azb("bem neutro") + ".",
            vm("Regra-âncora: dois bens → inclinação negativa; um bem e um mal → inclinação positiva."),
        ],
        "dissecando": (cz("[inversão]") + " A 1ª parte (monotonicidade = “mais é melhor”) é exata; o erro é só o "
                       "sinal da inclinação. Itens desse tipo testam se o candidato deduz a forma da curva a "
                       "partir do axioma, em vez de decorá-la."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se um dos bens for um mal, as curvas de indiferença serão positivamente inclinadas.”</i> → CERTO",
            "<i>“A monotonicidade implica que as curvas de indiferença sejam convexas em relação à origem.”</i> → "
            "ERRADO (troca de axioma: convexidade é outra hipótese)",
        ])],
        "reescrita": ("O pressuposto de que “quanto mais de um bem, melhor” é formalizado pelo axioma da "
                      "monotonicidade das preferências, que implica que as curvas de indiferença são "
                      + hl("negativamente") + " inclinadas."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Monotonicidade implica inclinação negativa: para manter a utilidade ao ganhar mais de "
                            "um bem é preciso abrir mão do outro.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00671
    {
        "id": "ECO-E2-L00671-1", "fonte_ref": "E2-L00671", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito da teoria do consumidor e dos conceitos de elasticidade, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("A convexidade das curvas de indiferença reflete a hipótese de taxa marginal de substituição "
                      "decrescente, indicando que os consumidores preferem cestas de consumo balanceadas a cestas "
                      "extremas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A convexidade das curvas de indiferença <u>reflete</u> a hipótese de taxa marginal de "
                      "substituição decrescente, indicando que os consumidores preferem cestas de consumo "
                      "balanceadas a cestas extremas."),
        "poucas": ("Curva convexa = " + azb("TMS decrescente") + " = " + azb("“médias são preferidas a extremos”")
                   + ": três leituras (geométrica, marginal e de preferência) da mesma hipótese."),
        "destrinchando": [
            "Leitura geométrica: a curva é “curvada para a origem”; a inclinação, em módulo, cai da esquerda para a "
            "direita.",
            "Leitura marginal: com muito x₂ e pouco x₁, o consumidor cede muito x₂ por uma unidade de x₁; com "
            "muito x₁, cede pouco. A " + azb("TMS") + " = UMg₁/UMg₂ " + vd("decresce") + " ao longo da curva.",
            "Leitura de preferências: se A e B estão na mesma curva, a cesta média fica <b>acima</b> dela "
            "(convexidade estrita) — a cesta balanceada é estritamente preferida aos extremos.",
            "Limites: nos " + azb("substitutos perfeitos") + " (retas) a média está na mesma curva — convexidade "
            "fraca, TMS constante; em preferências " + azb("côncavas") + ", o consumidor prefere extremos e "
            "especializa-se.",
            "Rigor: convexidade com curvas suaves equivale a TMS <b>não crescente</b>; por isso um item que diga "
            "“equivale” a TMS decrescente pode ser dado como ERRADO (ver ECO-E1-0841-1). O verbo “reflete” é seguro.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Junta as duas leituras clássicas da convexidade (TMS decrescente "
                       "e preferência por diversificação). A armadilha seria estranhar o verbo “reflete” ou achar "
                       "que “balanceadas” contradiz algo; não contradiz."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A convexidade das curvas de indiferença indica que os consumidores preferem cestas extremas a "
            "cestas balanceadas.”</i> → ERRADO (inversão: isso é concavidade)",
            "<i>“Preferências por substitutos perfeitos são estritamente convexas.”</i> → ERRADO (são convexas, mas "
            "não estritamente: a média fica na mesma reta)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Convexidade = representação geométrica da TMS decrescente; médias preferidas a "
                            "extremos (estritamente, salvo substitutos perfeitos).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00810
    {
        "id": "ECO-E2-L00810-1", "fonte_ref": "E2-L00810", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação à teoria microeconômica, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("A utilidade marginal diminui à medida que mais unidades são produzidas, segundo a lei da "
                      "utilidade marginal decrescente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A utilidade marginal diminui à medida que mais unidades são ") + vm("produzidas")
                    + az(", segundo a lei da utilidade marginal decrescente.")),
        "poucas": ("Utilidade é conceito do " + azb("consumo") + ": a UMg cai à medida que mais unidades são "
                   + vd("consumidas") + ". O equivalente na produção é o " + azb("produto marginal decrescente") + "."),
        "destrinchando": [
            azb("Utilidade marginal") + " = satisfação extra da última unidade <b>consumida</b>. A lei diz que, "
            "mantido o resto constante, cada unidade adicional consumida acrescenta menos satisfação.",
            "Do lado da firma, o paralelo é a " + azb("lei dos rendimentos marginais decrescentes") + ": com um "
            "fator fixo, cada unidade adicional do fator variável acrescenta cada vez menos produto (PMg "
            "decrescente). Dela decorre o custo marginal crescente no curto prazo.",
            "Paralelos úteis para não confundir: consumidor — utilidade, UMg, curva de indiferença, TMS; produtor — "
            "produto, PMg, isoquanta, " + azb("TMST") + ".",
            "A UMg decrescente sustenta a demanda negativamente inclinada na abordagem cardinal (UMg/p igualada "
            "entre bens); o PMg decrescente sustenta a oferta positivamente inclinada.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Uma palavra trocada leva o conceito do consumo para a "
                       "produção. Itens de uma palavra só exigem leitura lenta: “produzidas” ao lado de "
                       "“utilidade” é o sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O produto marginal do trabalho diminui à medida que mais trabalhadores são empregados, mantido o "
            "capital fixo.”</i> → CERTO",
            "<i>“A utilidade total diminui à medida que mais unidades são consumidas.”</i> → ERRADO (troca total × "
            "marginal: a UT cresce enquanto UMg > 0)",
        ])],
        "reescrita": ("A utilidade marginal diminui à medida que mais unidades são " + hl("consumidas") + ", segundo "
                      "a lei da utilidade marginal decrescente."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A UMg diminui à medida que mais unidades são consumidas, não produzidas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00882
    {
        "id": "ECO-E2-L00882-1", "fonte_ref": "E2-L00882", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_NAB_TEORIA,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria ordinal do consumidor, as preferências do consumidor serão transitivas "
                      "quando ele puder decidir se prefere a cesta A à B, se prefere a cesta B à A ou se é "
                      "indiferente às cestas A e B."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a teoria ordinal do consumidor, as preferências do consumidor serão ")
                    + vm("transitivas") + az(" quando ele puder decidir se prefere a cesta A à B, se prefere a "
                                             "cesta B à A ou se é indiferente às cestas A e B.")),
        "poucas": ("Poder comparar " + vd("quaisquer duas cestas") + " é a " + azb("completude") + ". A "
                   + azb("transitividade") + " envolve " + vd("três cestas") + ": A ≿ B e B ≿ C ⇒ A ≿ C."),
        "destrinchando": [
            azb("Completude") + ": para quaisquer A e B, vale A ≿ B, B ≿ A ou ambos (indiferença). O consumidor "
            "nunca diz “não sei comparar”.",
            azb("Transitividade") + ": se A ≿ B e B ≿ C, então A ≿ C. Garante consistência entre comparações e "
            "impede ciclos (A ≻ B ≻ C ≻ A), que tornariam impossível escolher a “melhor” cesta.",
            azb("Reflexividade") + ": A ≿ A. Trivial, mas completa o trio que define a " + azb("preferência "
            "racional") + ".",
            "Na " + azb("teoria ordinal") + " (" + oc("Hicks") + " e " + oc("Allen") + ", 1934; " + oc("Pareto")
            + " antes deles) importa só a ordenação, não a intensidade: a utilidade é um índice, e qualquer "
            "transformação monotônica crescente representa as mesmas preferências.",
            vm("Regra-âncora: dois elementos → completude; três elementos → transitividade."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A definição está correta; o rótulo é o do axioma vizinho. "
                       "Pista: a definição só menciona <b>duas</b> cestas (A e B) — transitividade sempre precisa "
                       "de uma terceira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o consumidor prefere A a B e B a C, mas prefere C a A, suas preferências violam a "
            "transitividade.”</i> → CERTO",
            "<i>“A completude garante que as curvas de indiferença não se cruzem.”</i> → ERRADO (troca de axioma: "
            "é a transitividade)",
        ])],
        "reescrita": ("De acordo com a teoria ordinal do consumidor, as preferências do consumidor serão "
                      + hl("completas") + " quando ele puder decidir se prefere a cesta A à B, se prefere a cesta B "
                      "à A ou se é indiferente às cestas A e B."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Poder ordenar quaisquer duas cestas é completude (integralidade); transitividade é "
                            "A ≻ B e B ≻ C ⇒ A ≻ C.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00883
    {
        "id": "ECO-E2-L00883-1", "fonte_ref": "E2-L00883", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_NAB_TEORIA,
        "rotulo_item": "Item",
        "assertiva": "A inclinação das curvas de indiferença é representada pela razão entre os preços dos bens considerados.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A inclinação das curvas de indiferença é representada pela ") + vm("razão entre os preços dos "
                    "bens considerados") + az(".")),
        "poucas": ("Inclinação da curva de indiferença = " + azb("TMS") + " = UMg₁/UMg₂ (preferências). Razão de "
                   "preços = inclinação da " + azb("restrição orçamentária") + " (mercado). Elas só " + vd("coincidem "
                   "no ótimo") + "."),
        "destrinchando": [
            azb("TMS") + " = quanto de x₂ o consumidor aceita ceder por uma unidade de x₁ mantendo a utilidade; "
            "algebricamente, " + vd("TMS = UMg₁/UMg₂") + ". Depende só dos gostos e da cesta em que ele está.",
            "Inclinação da restrição p₁x₁ + p₂x₂ = R: " + vd("−p₁/p₂") + ". É a taxa a que o <b>mercado</b> permite "
            "trocar um bem pelo outro.",
            "Escolha ótima (caso usual): TMS = p₁/p₂ — a taxa subjetiva iguala a taxa de mercado. Fora do ótimo, "
            "a diferença mostra para onde realocar: se TMS > p₁/p₂, o consumidor valoriza x₁ mais do que o mercado "
            "cobra e deve comprar mais x₁.",
            "Ao longo de uma mesma curva de indiferença a TMS varia (decrescente, no caso usual), enquanto a razão "
            "de preços é uma só — mais uma razão para não confundir as duas.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mistura a condição de equilíbrio (TMS = p₁/p₂) com a definição "
                       "da inclinação. Quem decorou “TMS = razão de preços” sem o contexto do ótimo cai. Pista: "
                       "o item não fala em ótimo nem em equilíbrio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio do consumidor, a inclinação da curva de indiferença é igual à razão entre os preços "
            "dos bens.”</i> → CERTO",
            "<i>“A inclinação da restrição orçamentária é dada pela razão entre as utilidades marginais dos "
            "bens.”</i> → ERRADO (é a razão de preços)",
        ])],
        "reescrita": ("A inclinação das curvas de indiferença é representada pela " + hl("taxa marginal de "
                      "substituição (razão entre as utilidades marginais dos bens), que só se iguala à razão entre os "
                      "preços no ponto ótimo") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Inclinação da curva de indiferença = TMS (razão das UMg); razão de preços = inclinação "
                            "da reta orçamentária; iguais no equilíbrio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00884
    {
        "id": "ECO-E2-L00884-1", "fonte_ref": "E2-L00884", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COM_NAB_TEORIA,
        "rotulo_item": "Item",
        "assertiva": ("Dois bens são considerados complementos perfeitos quando a curva de indiferença apresenta taxa "
                      "marginal de substituição crescente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Dois bens são considerados complementos perfeitos quando a curva de indiferença apresenta ")
                    + vm("taxa marginal de substituição crescente") + az(".")),
        "poucas": ("Complementos perfeitos são consumidos em " + azb("proporção fixa") + ": curva em " + vd("L")
                   + ", com TMS " + vd("infinita") + " no trecho vertical, " + vd("nula") + " no horizontal e "
                   "indefinida no vértice. TMS crescente é sinal de preferências côncavas."),
        "destrinchando": [
            "Função típica: " + vd("U = mín{ax₁, bx₂}") + " (ex.: sapato esquerdo e direito, U = mín{x₁, x₂}). Os "
            "vértices ficam sobre o raio x₂/x₁ = a/b; unidades fora da proporção não acrescentam utilidade.",
            "Trecho vertical: mais x₂ sem x₁ não vale nada, então o consumidor cederia “qualquer quantidade” de x₂ "
            "por um pouco de x₁ → TMS infinita. Trecho horizontal: o inverso → TMS nula. Vértice: a inclinação "
            "salta de ∞ para 0, e a TMS não está definida.",
            "Da esquerda para a direita a TMS cai (de ∞ a 0): se algo, é “decrescente” em sentido extremo — "
            "nunca crescente.",
            azb("TMS crescente") + " ao longo da curva significa curva " + azb("côncava") + ": preferência por "
            "extremos e escolha de canto.",
            "Escolha ótima dos complementos: no vértice, x₁ = x₂ (para a = b = 1) e x₁ = R/(p₁ + p₂). Variação de "
            "preço não gera " + azb("efeito substituição") + " — só efeito renda.",
        ],
        "grafico_verso": "ECO-E2-L00884-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item associa complementos perfeitos a um comportamento da "
                       "TMS que pertence às preferências côncavas. Pista visual: desenhe o L e percorra-o — a TMS "
                       "só cai (∞ → 0)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para complementos perfeitos, a variação do preço de um dos bens não gera efeito "
            "substituição.”</i> → CERTO",
            "<i>“Substitutos perfeitos apresentam taxa marginal de substituição decrescente.”</i> → ERRADO (é "
            "constante: curvas retas)",
        ])],
        "reescrita": ("Dois bens são considerados complementos perfeitos quando a curva de indiferença apresenta "
                      + hl("formato de L (proporção fixa), com TMS infinita no trecho vertical, nula no horizontal e "
                           "indefinida no vértice") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Complementos perfeitos: proporção fixa, curva em L; TMS infinita acima da quina, zero à "
                            "direita, indefinida no vértice.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 141", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00884-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00992
    {
        "id": "ECO-E2-L00992-1", "fonte_ref": "E2-L00992", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("Considerando preferências racionais e bem comportadas, uma das propriedades das curvas de "
                      "indiferença é que a taxa marginal de substituição é decrescente ao longo da curva de "
                      "indiferença."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando preferências racionais e <u>bem comportadas</u>, uma das propriedades das curvas "
                      "de indiferença é que a taxa marginal de substituição é <u>decrescente</u> ao longo da curva de "
                      "indiferença."),
        "poucas": ("Preferências " + azb("bem comportadas") + " = monotônicas + convexas → curvas negativamente "
                   "inclinadas e convexas, com " + vd("|TMS| decrescente") + " da esquerda para a direita."),
        "destrinchando": [
            azb("Racionais") + ": completas, reflexivas e transitivas (permitem ordenar as cestas). " + azb("Bem "
            "comportadas") + " (" + oc("Varian") + "): monotônicas (mais é melhor) e convexas (médias preferidas "
            "a extremos).",
            "Cada hipótese, um traço: monotonicidade → inclinação negativa e curvas mais altas melhores; "
            "convexidade → " + azb("TMS decrescente") + " em módulo.",
            "Intuição: com muito x₂ e pouco x₁ (ponto A), uma unidade de x₁ vale muito em termos de x₂; com muito "
            "x₁ e pouco x₂ (ponto B), vale pouco. A inclinação, em módulo, diminui ao andar para a direita.",
            "Rigor: com convexidade apenas fraca, a TMS é “não crescente” (pode ser constante, como nos "
            "substitutos perfeitos); a convexidade estrita é que garante a queda estrita. Em itens C/E sobre "
            "preferências bem comportadas, “TMS decrescente” é a resposta padrão.",
        ],
        "grafico_verso": "ECO-E2-L00992-1-V1",
        "dissecando": (cz("[literalidade]") + " Reproduz a propriedade de manual. A dúvida possível — “decrescente” "
                       "ou “crescente”? — se resolve lembrando que o sinal é negativo e o que cai é o módulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Preferências bem comportadas apresentam taxa marginal de substituição crescente ao longo da curva "
            "de indiferença.”</i> → ERRADO (inversão: crescente indica preferências côncavas)",
            "<i>“Preferências racionais são, necessariamente, bem comportadas.”</i> → ERRADO (racionalidade não "
            "implica monotonicidade nem convexidade)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Racionais: completas, transitivas, reflexivas; bem comportadas: monotônicas e "
                            "convexas (Varian), com |TMS| não crescente da esquerda para a direita.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 164", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00992-1-V1, com foco na TMS)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01010
    {
        "id": "ECO-E2-L01010-1", "fonte_ref": "E2-L01010", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("Uma das propriedades das curvas de indiferença é que as curvas em formato de “L” representam "
                      "bens substitutos perfeitos."),
        "gabarito": "ERRADO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": (az("Uma das propriedades das curvas de indiferença é que as curvas em formato de “L” representam "
                       "bens ") + vm("substitutos perfeitos") + az(".")),
        "poucas": ("Curva em " + vd("L") + " = " + azb("complementares perfeitos") + " (proporção fixa). "
                   + azb("Substitutos perfeitos") + " têm curvas " + vd("retas") + ", com TMS constante."),
        "destrinchando": [
            azb("Substitutos perfeitos") + ": U = ax₁ + bx₂. O consumidor troca um bem pelo outro sempre à mesma "
            "taxa (ex.: suco de maçã × suco de laranja para quem é indiferente, TMS = −1). Curvas: retas paralelas.",
            azb("Complementares perfeitos") + ": U = mín{ax₁, bx₂}. Só a combinação na proporção certa gera "
            "utilidade (sapato esquerdo × direito). Curvas: L, com vértice sobre o raio da proporção fixa.",
            "Entre os dois extremos está o caso usual (Cobb-Douglas): curva convexa suave. A " + azb("elasticidade "
            "de substituição") + " ordena os três: ∞ (reta), 1 (Cobb-Douglas), 0 (L).",
            "Consequências para a escolha: substitutos → canto (só o bem relativamente mais barato); "
            "complementares → vértice, sem efeito substituição quando um preço muda.",
            vm("Regra-âncora: reta = substitutos; L = complementares."),
        ],
        "grafico_verso": "ECO-E2-L01010-1-V1",
        "dissecando": (cz("[troca de conceito]") + " Troca direta dos dois casos-limite. 🔥 Muito frequente: a "
                       "banca alterna “reta”, “L”, “substitutos” e “complementares” em itens irmãos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Curvas de indiferença lineares indicam bens substitutos perfeitos.”</i> → CERTO",
            "<i>“Para complementares perfeitos, a TMS é constante e igual à proporção de consumo.”</i> → ERRADO "
            "(TMS infinita, nula ou indefinida; constante é a dos substitutos)",
        ])],
        "reescrita": ("Uma das propriedades das curvas de indiferença é que as curvas em formato de “L” representam "
                      "bens " + hl("complementares perfeitos") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só com duas imagens: retas paralelas de substitutos perfeitos (suco de maçã × "
                            "laranja, TMS = −1) e curvas em L de complementos perfeitos (sapatos).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 169", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (painel 1 de ECO-E2-L01010-1-V1)"},
                          {"ref": "IMAGEM 170", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (painel 2 de ECO-E2-L01010-1-V1)"}],
        "alertas": ["gabarito_resolvido: o verso da fonte traz só imagens, sem a palavra ERRADO; gabarito deduzido "
                    "das figuras e do conteúdo"],
    },
    # ------------------------------------------------------------------ E2-L01012
    {
        "id": "ECO-E2-L01012-1", "fonte_ref": "E2-L01012", "destino": "04", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_FALHAS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo a teoria do consumidor, a escolha ótima do consumidor é sempre caracterizada pela "
                      "igualdade entre a taxa marginal de substituição dos bens e a razão entre os seus respectivos "
                      "preços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo a teoria do consumidor, a escolha ótima do consumidor é ") + vm("sempre")
                    + az(" caracterizada pela igualdade entre a taxa marginal de substituição dos bens e a razão "
                         "entre os seus respectivos preços.")),
        "poucas": ("A " + azb("tangência") + " (TMS = p₁/p₂) vale para ótimos interiores de preferências bem "
                   "comportadas. Falha nas " + vd("soluções de canto") + " (substitutos perfeitos, preferências "
                   "côncavas) e no " + vd("vértice") + " dos complementares perfeitos."),
        "destrinchando": [
            "Caso usual: o consumidor sobe de curva de indiferença até a última que toca a restrição — e a toca "
            "tangenciando, com " + vd("TMS = p₁/p₂") + ". É a condição de primeira ordem do problema com curvas "
            "suaves e convexas.",
            "Substitutos perfeitos (TMS constante): se |TMS| > p₁/p₂, vale mais comprar só x₁; se menor, só x₂. "
            "O ótimo é um " + azb("canto") + " em que a curva de indiferença corta a restrição sem tangenciá-la. "
            "Ex.: U = x₁ + x₂ e p₁ < p₂ → toda a renda em x₁.",
            "Complementares perfeitos: o ótimo é o vértice do L, onde a TMS não está definida — não há como "
            "igualá-la a nada.",
            "Preferências côncavas: a tangência seria ponto de <b>mínimo</b>; o ótimo é um canto.",
            "Formulação geral (Kuhn-Tucker): no ótimo com os dois bens, TMS = p₁/p₂; com só x₁, |TMS| ≥ p₁/p₂.",
        ],
        "grafico_verso": "ECO-E2-L01012-1-V1",
        "dissecando": (cz("[modulador absoluto]") + " A condição é a de manual; o erro é o “sempre”, que apaga as "
                       "exceções. 🔥 Itens sobre a escolha ótima com “sempre” ou “necessariamente” quase sempre "
                       "esperam a lembrança da solução de canto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em ótimos interiores de preferências bem comportadas, a TMS é igual à razão entre os preços.”</i> → "
            "CERTO",
            "<i>“Com substitutos perfeitos, a escolha ótima nunca é uma solução de canto.”</i> → ERRADO (o canto "
            "é a regra quando a TMS difere de p₁/p₂)",
        ])],
        "reescrita": ("De acordo a teoria do consumidor, a escolha ótima do consumidor é <s>sempre</s> caracterizada "
                      "pela igualdade entre a taxa marginal de substituição dos bens e a razão entre os seus "
                      "respectivos preços " + hl("apenas nos ótimos interiores de preferências bem comportadas; em "
                      "soluções de canto e no vértice dos complementares perfeitos, essa igualdade não vale") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "TMS = p₁/p₂ só em preferências bem comportadas; com substitutos perfeitos o consumidor "
                            "se especializa (solução de canto), sem tangência.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 171", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (painel 1 de ECO-E2-L01012-1-V1)"},
                          {"ref": "IMAGEM 172", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "redesenhada (painel 2 de ECO-E2-L01012-1-V1)"}],
        "alertas": [],
    },
]
