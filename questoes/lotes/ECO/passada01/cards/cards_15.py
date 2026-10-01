"""Cards da redação ECO — passada 01 — lote 15 (notas 05 e 06: produção e custos)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "fp": "🏭 Função de produção e curto prazo",
    "pmg": "📉 Produto marginal e rendimentos",
    "iso": "🗺️ Isoquantas e TMST",
    "esc": "📏 Rendimentos de escala",
    "ccp": "💰 Custos de curto prazo",
    "clp": "📈 Custos de longo prazo e escala",
    "isc": "⚖️ Isocusto e combinação ótima",
    "cec": "🧾 Custo econômico × contábil",
}

PROVA_FGV = "Câmara Municipal de São Paulo/Consultor Técnico Legislativo/2024"
CMD_RT_PROD = "A respeito da teoria da produção e dos custos, julgue o item a seguir."
CMD_RT_FIRMA = "A respeito da teoria da firma, julgue o item a seguir."
CMD_NIDI_OUT = ("As teorias do consumidor e do produtor são fundamentais para compreender como agentes econômicos "
                "tomam decisões racionais em condições de escassez [...]. Considerando essas teorias básicas da "
                "microeconomia e os conceitos que elas envolvem, julgue certo ou errado (C ou E) o item a seguir.")
CMD_IDEG = "Julgue o item a seguir, sobre a aplicação da análise de custos e receitas em mercados."
CMD_FEPESE = "Julgue o item a seguir, relativo aos custos de produção da firma."

CARDS = [
    # ------------------------------------------------------------------ E2-L01386
    {
        "id": "ECO-E2-L01386-1", "fonte_ref": "E2-L01386", "destino": "05", "subtema": H2["pmg"],
        "tipo": "C/E", "banca": "FGV", "prova": PROVA_FGV, "ano": 2024, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à teoria da produção (questão adaptada).",
        "rotulo_item": "Item",
        "assertiva": "O produto médio atinge seu nível máximo no ponto em que iguala com a produtividade marginal.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O produto médio atinge seu <u>nível máximo</u> no ponto em que <u>iguala</u> com a "
                      "produtividade marginal."),
        "poucas": ("Enquanto o " + azb("produto marginal") + " está acima do " + azb("produto médio")
                   + ", cada trabalhador extra puxa a média para cima; quando fica abaixo, puxa para baixo. "
                   "Logo, o PMg corta o PMe exatamente no " + vd("máximo do PMe") + "."),
        "destrinchando": [
            "No curto prazo (capital fixo), " + azb("PMe") + " = Q/L é a produção por trabalhador, e "
            + azb("PMg") + " = ΔQ/ΔL é o que o último trabalhador acrescenta. Com a lei dos rendimentos "
            "marginais decrescentes, ambos sobem no início e depois caem.",
            "A regra é a da média de notas: se a nota da nova prova (marginal) supera a média, a média sobe; "
            "se fica abaixo, a média cai; se é igual, a média está parada — no seu ponto de máximo (ou de "
            "mínimo, no caso dos custos).",
            "Sequência típica no exemplo do gráfico (Q = 6L² − 0,5L³): o PMg chega ao máximo primeiro "
            "(" + vd("L = 4") + "), corta o PMe no máximo deste (" + vd("L = 6, PMe = PMg = 18") + ") e zera "
            "quando o produto total é máximo (" + vd("L = 8") + ").",
            "Daí os " + azb("três estágios da produção") + ": I — até o máximo do PMe (vale ampliar L); "
            "II — do máximo do PMe até PMg = 0 (região econômica); III — PMg negativo (nenhuma firma racional "
            "opera aí).",
            "Espelho nos custos: com salário w dado, CVMe = w/PMe e CMg = w/PMg. O máximo do PMe corresponde "
            "ao mínimo do CVMe — e é por isso que o CMg corta o CVMe no seu ponto mínimo.",
            vm("Regra-âncora: a curva marginal corta a média sempre no extremo da média (máximo do PMe, mínimo "
               "do CMe)."),
        ],
        "grafico_verso": "ECO-E2-L01386-1-V1",
        "dissecando": (cz("[literalidade]") + " O item reproduz a regra de manual, com redação truncada "
                       "(“iguala com”). O risco é confundir com o <b>máximo do PMg</b>, que vem antes, ou com "
                       "PMg = 0, que marca o máximo do produto <b>total</b>. 🔥 Bancas costumam trocar qual "
                       "curva está no máximo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O produto marginal atinge seu máximo no ponto em que se iguala ao produto médio.”</i> → ERRADO "
            "(curva trocada: o máximo é do PMe; ali o PMg já está caindo)",
            "<i>“O produto total é máximo quando o produto marginal do trabalho é nulo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito (CERTO) e um gráfico de produto marginal e produto médio "
                            "(PMg com pico de 30 unidades com 3 trabalhadores).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 274", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01386-1-V1, com função ilustrativa própria)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01387
    {
        "id": "ECO-E2-L01387-1", "fonte_ref": "E2-L01387", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "FGV", "prova": PROVA_FGV, "ano": 2024, "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo à teoria da produção (questão adaptada).",
        "rotulo_item": "Item",
        "assertiva": ("A taxa marginal de substituição técnica entre dois bens é igual a razão de suas "
                      "produtividades marginais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A taxa marginal de substituição técnica entre dois ") + vm("bens")
                    + az(" é igual a razão de suas produtividades marginais.")),
        "poucas": ("A " + azb("TMST") + " é definida entre dois <b>fatores de produção</b> (insumos), ao longo "
                   "da isoquanta. Entre dois bens, as taxas são outras: a TMS do consumidor ou a TMT da "
                   "fronteira de possibilidades de produção."),
        "destrinchando": [
            azb("TMST") + " de trabalho por capital = quanto de K se pode retirar ao acrescentar 1 unidade de L "
            "<b>sem alterar a produção</b>: TMST = −ΔK/ΔL, ou seja, a inclinação da isoquanta em módulo.",
            "Por que vale a razão das produtividades: ao longo da isoquanta, ΔQ = PMg<sub>L</sub>·ΔL + "
            "PMg<sub>K</sub>·ΔK = 0 → " + vd("−ΔK/ΔL = PMg<sub>L</sub>/PMg<sub>K</sub>") + ". Exemplo: "
            "PMg<sub>L</sub> = 10 e PMg<sub>K</sub> = 5 → TMST = 2 (um trabalhador substitui 2 unidades de "
            "capital).",
            "As “taxas vizinhas” que a banca usa para confundir: " + azb("TMS") + " (consumidor, entre dois "
            "<b>bens</b>) = UMg<sub>X</sub>/UMg<sub>Y</sub>, inclinação da curva de indiferença; " + azb("TMT")
            + " (taxa marginal de transformação, entre dois <b>bens produzidos</b>) = CMg<sub>X</sub>/"
            "CMg<sub>Y</sub>, inclinação da FPP. Bem não tem “produtividade marginal”.",
            "No ótimo da firma, a TMST se iguala ao preço relativo dos fatores (w/r): é a tangência entre "
            "isoquanta e isocusto.",
            vm("Regra-âncora: TMS → bens e utilidade; TMST → fatores e produção; TMT → bens e custos (FPP)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Todo o resto é literal; o erro está numa única palavra: "
                       "“bens” no lugar de “fatores de produção”. Pista: “produtividades marginais” só existem "
                       "para insumos. 🔥 Trocar bens × fatores e utilidade × produção é clássico de FGV e "
                       "CEBRASPE."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A TMST de trabalho por capital é igual a PMg<sub>L</sub>/PMg<sub>K</sub>.”</i> → CERTO",
            "<i>“A TMST entre dois fatores é igual à razão de seus preços em qualquer ponto da isoquanta.”</i> → "
            "ERRADO (só no ponto de custo mínimo)",
        ])],
        "reescrita": ("A taxa marginal de substituição técnica entre dois " + hl("fatores de produção")
                      + " é igual " + hl("à") + " razão de suas produtividades marginais."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O item trocou “fatores de produção” por “bens”; TMST = ΔK/ΔL = PMgL/PMgK, taxa de "
                            "substituição de um insumo por outro mantida a produção.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 275", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (isoquanta ilustrativa; definição absorvida no 📖)"},
                          {"ref": "IMAGEM 276-277", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01722
    {
        "id": "ECO-E2-L01722-1", "fonte_ref": "E2-L01722", "destino": "05", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_PROD,
        "rotulo_item": "Item",
        "assertiva": ("Se há retornos crescentes de escala na função de produção, pode-se afirmar que as curvas de "
                      "isoquanta, ao aumentar a quantidade produzida sucessivamente no mesmo montante, ficarão "
                      "cada vez mais distantes entre si."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se há retornos crescentes de escala na função de produção, pode-se afirmar que as curvas "
                       "de isoquanta, ao aumentar a quantidade produzida sucessivamente no mesmo montante, ficarão "
                       "cada vez ") + vm("mais distantes") + az(" entre si.")),
        "poucas": ("Com " + azb("retornos crescentes") + ", cada acréscimo igual de produto exige acréscimos "
                   "<b>cada vez menores</b> de insumos: as isoquantas ficam " + vd("mais próximas") + "."),
        "destrinchando": [
            azb("Retornos crescentes de escala") + ": multiplicar todos os insumos por t > 1 multiplica o "
            "produto por mais que t — F(tK, tL) > t·F(K, L). Dobrar a fábrica e a equipe mais que dobra a "
            "produção.",
            "Leitura no mapa de isoquantas: siga um raio a partir da origem (K/L fixo) e meça quanto de insumo "
            "é preciso para ir de 100 a 200 e de 200 a 300 unidades. Com retornos " + vd("constantes")
            + ", os saltos são iguais; com " + vd("crescentes") + ", cada vez menores (isoquantas se "
            "aproximam); com " + vd("decrescentes") + ", cada vez maiores (isoquantas se afastam).",
            "No gráfico, com rendimentos crescentes (Q proporcional a K·L, homogênea de grau 2), os pontos sobre "
            "o raio são A = (2; 2), B ≈ (2,83; 2,83) e C ≈ (3,46; 3,46): saltos de 0,83 e depois 0,63.",
            "Não confundir as duas leituras do mapa: o <b>formato</b> de cada isoquanta (curvatura) diz como os "
            "fatores se substituem (TMST); o <b>espaçamento</b> entre isoquantas diz os rendimentos de escala.",
            "Ponte com custos: com preços de fatores dados, retornos crescentes significam custo médio de longo "
            "prazo decrescente — " + azb("economias de escala") + ".",
        ],
        "grafico_verso": "ECO-E2-L01722-1-V1",
        "dissecando": (cz("[inversão]") + " O experimento está descrito corretamente (acréscimos iguais de "
                       "produto); a conclusão foi invertida — “mais distantes” é o retrato dos rendimentos "
                       "<b>decrescentes</b>. Pista: “crescente” = a tecnologia rende mais, logo precisa de "
                       "<b>menos</b> insumo a cada passo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com rendimentos decrescentes de escala, as isoquantas que representam acréscimos iguais de "
            "produto ficam cada vez mais distantes entre si.”</i> → CERTO",
            "<i>“Com rendimentos constantes de escala, a distância entre isoquantas consecutivas, ao longo de um "
            "raio, diminui.”</i> → ERRADO (com rendimentos constantes ela é igual)",
        ])],
        "reescrita": ("Se há retornos crescentes de escala na função de produção, pode-se afirmar que as curvas de "
                      "isoquanta, ao aumentar a quantidade produzida sucessivamente no mesmo montante, ficarão "
                      "cada vez " + hl("mais próximas") + " entre si."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["pode-se afirmar"], "dificuldade": 2,
        "comentario_fonte": "Retornos crescentes: para aumentos iguais de produção, os acréscimos de insumos são "
                            "cada vez menores; as isoquantas ficam mais próximas, não mais distantes.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 511", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01722-1-V1, constantes × crescentes)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01725
    {
        "id": "ECO-E2-L01725-1", "fonte_ref": "E2-L01725", "destino": "05", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_PROD,
        "rotulo_item": "Item",
        "assertiva": ("Uma firma que tenha função de produção com rendimentos decrescentes para cada um dos fatores "
                      "de produção, não poderá ter retornos crescentes de escala."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma firma que tenha função de produção com rendimentos decrescentes para cada um dos "
                       "fatores de produção, ") + vm("não poderá ter") + az(" retornos crescentes de escala.")),
        "poucas": ("Rendimento " + azb("marginal") + " (um fator varia) e rendimento " + azb("de escala")
                   + " (todos variam juntos) são independentes: Q = K<sup>0,6</sup>·L<sup>0,6</sup> tem PMg "
                   "decrescente em cada fator e retornos crescentes (" + vd("0,6 + 0,6 = 1,2 > 1") + ")."),
        "destrinchando": [
            "Na " + azb("Cobb-Douglas") + " Q = A·K<sup>α</sup>·L<sup>β</sup>: o PMg<sub>L</sub> = β·Q/L é "
            "decrescente em L se " + vd("β &lt; 1") + " (idem para K com α &lt; 1); os rendimentos de escala dependem "
            "da " + vd("soma α + β") + ".",
            "Conta do exemplo: fixando K e dobrando só L, o produto cresce 2<sup>0,6</sup> ≈ " + vd("1,52")
            + " vez (menos que dobra: rendimento marginal decrescente). Dobrando K e L juntos, cresce "
            "2<sup>1,2</sup> ≈ " + vd("2,30") + " vezes (mais que dobra: retornos crescentes).",
            "Intuição: quando só um fator aumenta, ele se congestiona sobre o fator fixo (mais operários na "
            "mesma máquina). Quando todos aumentam, a proporção se mantém e podem surgir especialização e "
            "indivisibilidades bem aproveitadas.",
            "O que a soma permite e o que não permite (expoentes positivos): α + β &lt; 1 obriga α e β &lt; 1 "
            "(escala decrescente vem com marginais decrescentes); mas α, β &lt; 1 é compatível com qualquer "
            "rendimento de escala. E um único expoente > 1 já garante escala crescente.",
            vm("Regra-âncora: marginal = um fator, curto prazo; escala = todos os fatores, longo prazo — um não "
               "determina o outro."),
        ],
        "dissecando": (cz("[nexo indevido · modulador absoluto]") + " O item amarra dois conceitos "
                       "independentes e fecha com um “não poderá”. Basta um contraexemplo (Cobb-Douglas com "
                       "α, β &lt; 1 e α + β > 1) para derrubar. 🔥 A distinção marginal × escala é das mais "
                       "cobradas em teoria da produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma Cobb-Douglas com α + β = 1 apresenta rendimentos constantes de escala e rendimentos "
            "marginais decrescentes em cada fator.”</i> → CERTO",
            "<i>“Se uma Cobb-Douglas apresenta rendimento marginal crescente em algum fator, seus rendimentos de "
            "escala serão necessariamente decrescentes.”</i> → ERRADO (inversão: um expoente > 1 já faz a soma "
            "passar de 1)",
        ])],
        "reescrita": ("Uma firma que tenha função de produção com rendimentos decrescentes para cada um dos fatores "
                      "de produção " + hl("pode") + " ter retornos crescentes de escala."),
        "tipo_erro": ["NEXO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["não poderá"], "dificuldade": 2,
        "comentario_fonte": "Rendimentos decrescentes dos fatores e retornos crescentes de escala podem coexistir: "
                            "Q = L^0,6·K^0,6 (soma 1,2).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 514-516", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00015
    {
        "id": "ECO-E3-L00015-1", "fonte_ref": "E3-L00015", "destino": "05", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": ("Em relação à teoria da produção, ao equilíbrio da firma e à economia do bem-estar, julgue o "
                    "item subsecutivo."),
        "rotulo_item": "Item",
        "assertiva": ("Uma função de produção Cobb-Douglas Q(K,L) = A · K<sup>α</sup> · L<sup>β</sup> tem "
                      "rendimentos decrescentes de escala se α + β &lt; 1."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma função de produção Cobb-Douglas Q(K,L) = A · K<sup>α</sup> · L<sup>β</sup> tem "
                      "rendimentos decrescentes de escala se <u>α + β &lt; 1</u>."),
        "poucas": ("Multiplicar K e L por λ multiplica Q por " + vd("λ<sup>α+β</sup>") + ". Com α + β &lt; 1, o "
                   "produto cresce menos que proporcionalmente: " + azb("rendimentos decrescentes de escala")
                   + "."),
        "destrinchando": [
            "Conta que resolve qualquer item do tipo: Q(λK, λL) = A·(λK)<sup>α</sup>·(λL)<sup>β</sup> = "
            "λ<sup>α+β</sup>·Q. A Cobb-Douglas é " + azb("homogênea de grau α + β") + ".",
            "Tabela: " + vd("α + β &lt; 1") + " → decrescentes; " + vd("= 1") + " → constantes; " + vd("> 1")
            + " → crescentes. Exemplo: α = 0,3 e β = 0,5 → dobrar os insumos multiplica o produto por "
            "2<sup>0,8</sup> ≈ 1,74.",
            "A constante A (produtividade total dos fatores) desloca o nível da produção, mas não altera os "
            "rendimentos de escala.",
            "α e β são as " + azb("elasticidades-produto") + " de K e L. Com α + β = 1 e mercados competitivos, "
            "elas coincidem com as participações do capital e do trabalho na renda — por isso o modelo de "
            + oc("Solow") + " usa a Cobb-Douglas com α ≈ 1/3.",
            "Ponte com custos: rendimentos decrescentes de escala, com preços de fatores dados, geram custo médio "
            "de longo prazo crescente (deseconomias de escala).",
        ],
        "dissecando": (cz("[literalidade]") + " Regra de manual reproduzida sem desvio. O risco é confundir com "
                       "os rendimentos <b>marginais</b>, que dependem de cada expoente isolado (β &lt; 1 → PMg<sub>L</sub> "
                       "decrescente), e não da soma. 🔥 O CEBRASPE cobra a soma dos expoentes com frequência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tem rendimentos decrescentes de escala se α &lt; 1 e β &lt; 1.”</i> → ERRADO (α = β = 0,6 dá "
            "soma 1,2: crescentes)",
            "<i>“Se α + β = 1, o produto marginal do trabalho é constante.”</i> → ERRADO (escala constante, mas "
            "PMg<sub>L</sub> decrescente se β &lt; 1)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["se"], "dificuldade": 1,
        "comentario_fonte": "Q(λK, λL) = λ^(α+β)·Q; soma < 1 → decrescentes, = 1 → constantes, > 1 → crescentes "
                            "(cinco respostas repetidas).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: o sinal “<” de “α + β < 1” e os expoentes da função se perderam na "
                    "transcrição; restaurados pelo gabarito (CERTO) e pelos comentários"],
    },
    # ------------------------------------------------------------------ E3-L00340
    {
        "id": "ECO-E3-L00340-1", "fonte_ref": "E3-L00340", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": ("Considerando a teoria da produção e suas implicações para o equilíbrio de curto e longo prazo "
                    "para empresas competitivas, julgue (C ou E) o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A curvatura da isoquanta é medida por sua inclinação em cada ponto, que representa a taxa à "
                      "qual os dois insumos podem ser substituídos mantendo-se a produção constante. Esta taxa é "
                      "chamada de taxa marginal de substituição técnica e, ao longo de uma isoquanta típica, ela "
                      "diminui para o fator que está se tornando relativamente mais abundante à medida que nos "
                      "movemos para os extremos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curvatura da isoquanta é medida por sua inclinação em cada ponto, que representa a taxa "
                      "à qual os dois insumos podem ser substituídos mantendo-se a produção constante. Esta taxa "
                      "é chamada de taxa marginal de substituição técnica e, ao longo de uma isoquanta típica, "
                      "ela <u>diminui</u> para o fator que está se tornando relativamente <u>mais abundante</u> à "
                      "medida que nos movemos para os extremos."),
        "poucas": ("A inclinação da isoquanta é a " + azb("TMST") + "; na isoquanta convexa típica, ela "
                   + vd("decresce") + ": o fator que vai ficando abundante consegue substituir cada vez menos do "
                   "fator que vai ficando escasso."),
        "destrinchando": [
            azb("TMST") + " de trabalho por capital = −ΔK/ΔL ao longo da isoquanta = PMg<sub>L</sub>/"
            "PMg<sub>K</sub>. Mede quantas unidades de capital um trabalhador a mais consegue substituir sem "
            "mudar a produção.",
            "Por que decresce: ao trocar K por L, o trabalho fica abundante (PMg<sub>L</sub> cai) e o capital "
            "fica escasso (PMg<sub>K</sub> sobe) — a razão PMg<sub>L</sub>/PMg<sub>K</sub> despenca. No "
            "gráfico: de A para B, 1 trabalhador substitui " + vd("3") + " unidades de capital; de C para D, "
            "só " + vd("0,5") + ".",
            "TMST decrescente é o mesmo que " + azb("isoquanta convexa") + " em relação à origem. Casos-limite: "
            "substitutos perfeitos (isoquanta reta, TMST constante) e complementares perfeitos (isoquanta em L, "
            "sem substituição possível).",
            "Precisão de vocabulário: a inclinação mede a TMST; a <b>curvatura</b>, a rigor, é a variação dessa "
            "inclinação ao longo da curva (quanto mais curva, mais difícil a substituição). O item usa as duas "
            "ideias de forma frouxa, mas o núcleo — TMST decrescente na isoquanta típica — está correto.",
            "Por que importa: com TMST decrescente, a tangência entre isoquanta e isocusto (TMST = w/r) é de fato "
            "um mínimo de custo, e a firma substitui gradualmente o fator que encarece.",
        ],
        "grafico_verso": "ECO-E3-L00340-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item parafraseia a definição de manual em frase "
                       "longa e com uma imprecisão (“curvatura medida pela inclinação”) que pode levar o "
                       "candidato a marcar ERRADO por excesso de rigor. O que decide é o comportamento da TMST "
                       "ao longo da curva: “diminui” está certo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao longo de uma isoquanta convexa, a TMST de trabalho por capital é crescente à medida que se "
            "substitui capital por trabalho.”</i> → ERRADO (inversão: é decrescente)",
            "<i>“Se os insumos forem substitutos perfeitos, a TMST é constante ao longo da isoquanta.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["isoquanta típica"], "dificuldade": 2,
        "comentario_fonte": "Isoquanta convexa reflete TMST decrescente: quanto mais se usa um insumo, menor a "
                            "facilidade de substituí-lo pelo outro; TMST = −dK/dL = PMgL/PMgK (quatro respostas "
                            "concordantes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 475", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (anotações manuscritas sobre TMST, com OCR ilegível)"},
                          {"ref": "IMAGEM 476", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00340-1-V1, com valores próprios)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00406
    {
        "id": "ECO-E3-L00406-1", "fonte_ref": "E3-L00406", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_OUT,
        "rotulo_item": "Item",
        "assertiva": ("A Taxa Marginal de Substituição (TMS) para o consumidor indica a relação entre as quantidades "
                      "de dois bens que um indivíduo está disposto a trocar para manter o mesmo nível de utilidade "
                      "e é análoga à Taxa Marginal de Substituição Técnica (TMST) do produtor, que reflete a "
                      "relação entre os insumos que o produtor pode substituir, mantendo o mesmo nível de "
                      "produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Taxa Marginal de Substituição (TMS) para o consumidor indica a relação entre as "
                      "quantidades de dois bens que um indivíduo está disposto a trocar para manter o mesmo nível "
                      "de utilidade e é <u>análoga</u> à Taxa Marginal de Substituição Técnica (TMST) do "
                      "produtor, que reflete a relação entre os insumos que o produtor pode substituir, mantendo "
                      "o mesmo nível de produção."),
        "poucas": ("As duas são " + azb("taxas de troca na margem") + " que mantêm algo constante — utilidade "
                   "(TMS, curva de indiferença) ou produção (TMST, isoquanta). A analogia é a estrutura comum das "
                   "teorias do consumidor e da firma."),
        "destrinchando": [
            azb("TMS") + " = |ΔY/ΔX| com utilidade constante = " + vd("UMg<sub>X</sub>/UMg<sub>Y</sub>")
            + ": inclinação da curva de indiferença. TMS = 2 → o consumidor cede 2 unidades de Y por 1 de X "
            "e fica igualmente satisfeito.",
            azb("TMST") + " = |ΔK/ΔL| com produção constante = " + vd("PMg<sub>L</sub>/PMg<sub>K</sub>")
            + ": inclinação da isoquanta. TMST = 3 → um trabalhador a mais permite dispensar 3 unidades de "
            "capital.",
            "Paralelos completos: ambas são <b>decrescentes</b> no caso típico (preferências convexas × "
            "rendimentos marginais decrescentes); no ótimo, ambas se igualam a um preço relativo (TMS = "
            "P<sub>X</sub>/P<sub>Y</sub>, na tangência com a reta orçamentária; TMST = w/r, na tangência com a "
            "isocusto).",
            "Diferenças que a banca pode explorar: a utilidade é <b>ordinal</b> (o número da curva de indiferença "
            "só ordena) e subjetiva; a isoquanta é <b>cardinal</b> (Q = 100 é mensurável) e técnica. "
            "“Análoga” ≠ “idêntica”.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item longo e sem armadilha de conteúdo: descreve corretamente as "
                       "duas taxas e afirma só a analogia. Ele viraria ERRADO se trocasse os objetos (TMST entre "
                       "bens; TMS entre insumos) ou se dissesse que os conceitos são idênticos ou que a utilidade "
                       "é mensurável como a produção."),
        "modulos": [
            ("🧭 Panorama", [
                "Consumidor → curva de indiferença → TMS → restrição orçamentária → ótimo TMS = P<sub>X</sub>/"
                "P<sub>Y</sub>.",
                "Produtor → isoquanta → TMST → isocusto → ótimo TMST = w/r.",
            ]),
            ("😈 Para dificultar", [
                "<i>“A TMS é cardinal, assim como a TMST, pois ambas medem níveis observáveis de satisfação e de "
                "produção.”</i> → ERRADO (a utilidade é ordinal)",
                "<i>“No ótimo, a TMS iguala a razão de preços dos bens, e a TMST, a razão de preços dos "
                "fatores.”</i> → CERTO",
            ]),
        ],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "TMS = UMgX/UMgY, inclinação da curva de indiferença; TMST = PMgL/PMgK, inclinação da "
                            "isoquanta; ambas são taxas de troca na margem com algo constante (quatro respostas "
                            "concordantes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 574", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (curva de indiferença ilustrativa; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00407
    {
        "id": "ECO-E3-L00407-1", "fonte_ref": "E3-L00407", "destino": "05", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_OUT,
        "rotulo_item": "Item",
        "assertiva": ("Um produtor racional sempre escolhe uma combinação de fatores de produção localizada em uma "
                      "curva de indiferença mais alta, pois curvas de indiferença mais baixas representam menores "
                      "níveis de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um produtor racional ") + vm("sempre") + az(" escolhe uma combinação de fatores de "
                    "produção localizada em uma ") + vm("curva de indiferença mais alta") + az(", pois ")
                    + vm("curvas de indiferença") + az(" mais baixas representam menores níveis de produção.")),
        "poucas": ("Dois erros: o produtor trabalha com " + azb("isoquantas") + ", não com curvas de "
                   "indiferença; e não escolhe “sempre a mais alta”, mas a isoquanta mais alta que sua "
                   + azb("isocusto") + " alcança (ou a isocusto mais baixa para um dado produto)."),
        "destrinchando": [
            "Vocabulário: " + azb("curva de indiferença") + " = cestas de <b>bens</b> com a mesma "
            "<b>utilidade</b> (consumidor); " + azb("isoquanta") + " = combinações de <b>insumos</b> com a mesma "
            "<b>produção</b> (firma).",
            "Critério de escolha: produzir mais custa mais. Escolher “sempre a isoquanta mais alta” sem olhar o "
            "custo levaria a gastar sem limite. O problema da firma tem duas formas equivalentes: "
            "<b>maximizar Q dado o custo</b> (isoquanta mais alta tocada pela isocusto) ou <b>minimizar o custo "
            "dado Q</b> (isocusto mais baixa que toca a isoquanta). Ambas levam à tangência " + vd("TMST = w/r")
            + ".",
            "E a escala? O lucro máximo exige, além do custo mínimo para cada Q, escolher o Q em que a receita "
            "marginal iguala o custo marginal. Mais produção só compensa até aí.",
            "O paralelo com o consumidor é legítimo (curva mais alta = melhor, sob restrição), mas cada teoria "
            "tem seu objeto e sua restrição: orçamento × custo.",
            vm("Regra-âncora: firma → isoquanta + isocusto; consumidor → curva de indiferença + reta "
               "orçamentária."),
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " O item transplanta o vocabulário do "
                       "consumidor para a firma e retira a restrição de custo com o “sempre”. Pista imediata: "
                       "“curva de indiferença” e “níveis de produção” na mesma frase não combinam. 🔥 Simulados "
                       "do CACD gostam dessa troca de rótulos entre as duas teorias."),
        "modulos": [
            ("🧠 Mnemônico", ["Iso<b>quanta</b> = igual <b>quanti</b>dade; curva de indiferença = igual "
                              "felicidade."]),
            ("😈 Para dificultar", [
                "<i>“Um consumidor racional escolhe a cesta na curva de indiferença mais alta compatível com sua "
                "restrição orçamentária.”</i> → CERTO",
                "<i>“Dada a isocusto, o produtor escolhe a isoquanta mais alta, ponto em que a TMST é maior que a "
                "razão w/r.”</i> → ERRADO (no ótimo, TMST = w/r)",
            ]),
        ],
        "reescrita": ("Um produtor racional " + hl("escolhe, dada a sua isocusto,") + " uma combinação de fatores "
                      "de produção localizada " + hl("na isoquanta mais alta alcançável") + ", pois "
                      + hl("isoquantas") + " mais baixas representam menores níveis de produção."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Produtores usam isoquantas, não curvas de indiferença; a escolha é a tangência entre "
                            "isoquanta e isocusto, não “sempre a mais alta” (cinco respostas concordantes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 575", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (anotação manuscrita: “o nome da curva é isoquanta”; absorvida no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00409
    {
        "id": "ECO-E3-L00409-1", "fonte_ref": "E3-L00409", "destino": "05", "subtema": H2["fp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_OUT,
        "rotulo_item": "Item",
        "assertiva": ("O axioma da transitividade na teoria do consumidor, que afirma que se um consumidor prefere o "
                      "bem A ao bem B e prefere o bem B ao bem C, ele também prefere o bem A ao bem C, possui uma "
                      "contraparte na teoria do produtor, segundo a qual a produção com uma combinação de insumos "
                      "mais eficiente sempre é preferida pelo produtor, respeitando a lógica de eficiência "
                      "técnica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O axioma da transitividade na teoria do consumidor, que afirma que se um consumidor prefere "
                      "o bem A ao bem B e prefere o bem B ao bem C, ele também prefere o bem A ao bem C, possui uma "
                      "<u>contraparte</u> na teoria do produtor, segundo a qual a produção com uma combinação de "
                      "insumos <u>mais eficiente</u> sempre é preferida pelo produtor, respeitando a lógica de "
                      "eficiência técnica."),
        "poucas": ("A " + azb("transitividade") + " garante uma ordenação coerente das cestas. No produtor, o "
                   "papel equivalente cabe à ordenação por " + azb("eficiência técnica") + ": entre combinações "
                   "que produzem o mesmo, a que usa menos insumo domina — e essa dominância também é transitiva."),
        "destrinchando": [
            "Axiomas do consumidor racional: " + azb("completude") + " (sabe comparar quaisquer duas cestas) e "
            + azb("transitividade") + " (A ≻ B e B ≻ C ⇒ A ≻ C), além de monotonicidade e convexidade. "
            "Completude + transitividade (com continuidade) permitem representar as preferências por uma função "
            "utilidade; e é a transitividade que impede curvas de indiferença de se cruzarem.",
            "Sem transitividade haveria ciclos (café ≻ chá ≻ suco ≻ café) e nenhuma cesta “melhor” — não haveria "
            "o que maximizar.",
            "No produtor: uma combinação é " + azb("tecnicamente eficiente") + " se nenhuma outra produz o mesmo "
            "com menos de algum insumo e não mais de nenhum. Se A domina B e B domina C, A domina C. O produtor "
            "racional nunca escolhe uma combinação dominada (desperdício): as eficientes formam a própria "
            "isoquanta.",
            "Segundo degrau: entre combinações tecnicamente eficientes, a firma prefere a de " + azb("menor custo")
            + " (eficiência econômica, dados w e r) — de novo uma ordenação transitiva, agora pelo custo.",
            "Limite da analogia: no consumidor a transitividade é um <b>axioma</b> sobre gostos subjetivos; no "
            "produtor, a ordenação decorre da tecnologia e do objetivo de lucro — é objetiva. Por isso o item "
            "fala em “contraparte”, não em identidade.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Item abstrato e longo, que parece forçar uma "
                       "analogia. O “sempre” assusta, mas aqui é legítimo: uma combinação mais eficiente "
                       "(dominante) nunca pode ser pior para a firma. Moral: modulador absoluto não é erro "
                       "automático — teste se a afirmação admite exceção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A transitividade das preferências garante que curvas de indiferença de um mesmo consumidor não "
            "se cruzem.”</i> → CERTO",
            "<i>“Um produtor racional pode preferir uma combinação tecnicamente ineficiente, desde que seja mais "
            "barata.”</i> → ERRADO (combinação dominada usa mais de algum insumo e não menos de nenhum: nunca é "
            "mais barata)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["sempre"], "dificuldade": 3,
        "comentario_fonte": "Transitividade garante preferências ordenáveis; no produtor, a contraparte é a "
                            "preferência por combinações tecnicamente eficientes (dominância transitiva). Uma das "
                            "respostas ressalva que a analogia não é perfeita (axioma subjetivo × consequência "
                            "técnica), sem mudar o gabarito.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
