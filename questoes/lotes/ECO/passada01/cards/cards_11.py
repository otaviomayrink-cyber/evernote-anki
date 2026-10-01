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
        "condicionais": [("⚠️ Gabarito contestável", "Em linguagem de manual introdutório (Pindyck, Varian), "
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
]
