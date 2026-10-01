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
    # ------------------------------------------------------------------ E1-0045
    {
        "id": "ECO-E1-0045-1", "fonte_ref": "E1-0045", "destino": "06", "subtema": H2["cec"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Acerca da distinção entre as abordagens contábil e econômica dos custos de produção, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("A abordagem contábil visa fornecer e utilizar valores que representem a eficiência da "
                      "utilização dos recursos no processo produtivo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A abordagem ") + vm("contábil") + az(" visa fornecer e utilizar valores que representem a "
                    "eficiência da utilização dos recursos no processo produtivo.")),
        "poucas": ("Medir a eficiência do uso dos recursos — o que exige o " + azb("custo de oportunidade")
                   + " — é o objetivo da abordagem <b>econômica</b>. A contábil registra os valores efetivamente "
                   "pagos, para relatórios e tributação."),
        "destrinchando": [
            azb("Abordagem contábil") + ": olha para trás. Registra custos <b>explícitos</b> (desembolsos), a "
            "valores históricos, com depreciação por regras legais e fiscais. Serve a acionistas, credores e "
            "fisco.",
            azb("Abordagem econômica") + ": olha para a decisão. Mede o " + azb("custo de oportunidade")
            + " de todos os recursos — explícitos e <b>implícitos</b> (o salário que o dono deixa de ganhar "
            "fora, o rendimento que o capital próprio teria em outro uso). Serve para decidir se e quanto "
            "produzir.",
            "Exemplo: receita de R$ 500 mil e custos explícitos de R$ 350 mil → " + vd("lucro contábil = 150 mil")
            + ". Se o dono ganharia R$ 100 mil como empregado e o capital próprio renderia R$ 60 mil, o "
            + vd("lucro econômico = −10 mil") + ": o negócio destrói valor, embora o balanço mostre lucro.",
            "Por isso " + azb("lucro econômico nulo") + " é o “lucro normal”: todos os fatores recebem o que "
            "receberiam no melhor uso alternativo. É o equilíbrio de longo prazo da concorrência perfeita.",
            vm("Regra-âncora: eficiência alocativa e custo de oportunidade → economista; valores pagos e "
               "históricos → contador."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A definição está correta, mas atribuída à abordagem errada. "
                       "Pista: “eficiência da utilização dos recursos” é linguagem de alocação, que só faz sentido "
                       "com custo de oportunidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A abordagem econômica dos custos considera os custos de oportunidade, inclusive os implícitos.”</i> "
            "→ CERTO",
            "<i>“O lucro econômico é sempre maior ou igual ao lucro contábil.”</i> → ERRADO (inversão: é menor ou "
            "igual, pois desconta os custos implícitos)",
        ])],
        "reescrita": ("A abordagem " + hl("econômica") + " visa fornecer e utilizar valores que representem a "
                      "eficiência da utilização dos recursos no processo produtivo."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Essa é a abordagem econômica, não a contábil.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0046
    {
        "id": "ECO-E1-0046-1", "fonte_ref": "E1-0046", "destino": "06", "subtema": H2["cec"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Acerca da distinção entre as abordagens contábil e econômica dos custos de produção, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("Os custos econômicos são aqueles medidos em termos de valores pagos por uma firma na "
                      "aquisição de seus insumos de produção (os chamados custos históricos)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os custos econômicos são aqueles medidos em termos de ")
                    + vm("valores pagos por uma firma na aquisição de seus insumos de produção (os chamados custos "
                         "históricos)") + az(".")),
        "poucas": ("Custo histórico é critério <b>contábil</b>. O " + azb("custo econômico") + " é o custo de "
                   "oportunidade: o valor do melhor uso alternativo de cada recurso hoje, incluindo os custos "
                   "implícitos."),
        "destrinchando": [
            azb("Custo histórico") + " = o preço pago na aquisição. " + azb("Custo econômico")
            + " = o que se renuncia ao usar o recurso agora. Exemplo: um estoque comprado a R$ 10 por unidade "
            "que hoje vale " + vd("R$ 15") + " no mercado custa, economicamente, R$ 15 para ser usado — é o que "
            "a firma deixa de receber vendendo-o.",
            "Inclui " + azb("custos implícitos") + ", que não passam pelo caixa: trabalho do proprietário, "
            "imóvel próprio que poderia ser alugado, capital próprio que renderia juros.",
            azb("Custos irrecuperáveis") + " (afundados): uma máquina sob medida, sem revenda, tem custo "
            "histórico alto e custo de oportunidade de uso ≈ " + vd("zero") + ". Para a decisão, o que foi gasto "
            "e não volta é irrelevante.",
            "Consequência prática: a contabilidade pode mostrar lucro onde o economista vê prejuízo (e vice-"
            "versa, quando ativos se valorizaram).",
            vm("Regra-âncora: custo econômico = custo de oportunidade — olhe para a melhor alternativa, não para "
               "a nota fiscal."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A definição de custo contábil foi atribuída ao custo "
                       "econômico. O parêntese “os chamados custos históricos” é a pista: é termo de "
                       "contabilidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O custo econômico de usar um estoque adquirido no passado é seu valor atual de mercado, e não o "
            "preço pago.”</i> → CERTO",
            "<i>“Custos irrecuperáveis devem pesar na decisão de continuar ou não produzindo.”</i> → ERRADO "
            "(custos afundados são irrelevantes para a decisão)",
        ])],
        "reescrita": ("Os custos econômicos são aqueles medidos em termos de " + hl("custo de oportunidade — o "
                      "valor do melhor uso alternativo dos insumos, inclusive os próprios —, e não dos valores "
                      "históricos pagos na sua aquisição") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Custos históricos referem-se à contabilidade; custos econômicos incluem custo "
                            "de oportunidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0221
    {
        "id": "ECO-E1-0221-1", "fonte_ref": "E1-0221", "destino": "06", "subtema": H2["ccp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_RT_FIRMA,
        "rotulo_item": "Item",
        "assertiva": "Se o produto marginal do trabalho for decrescente, então o custo marginal será crescente.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o produto marginal do trabalho for <u>decrescente</u>, então o custo marginal será "
                      "<u>crescente</u>."),
        "poucas": ("Com salário dado e trabalho como fator variável, " + vd("CMg = w/PMg<sub>L</sub>")
                   + ": se cada trabalhador extra produz menos, cada unidade extra exige mais horas e custa mais."),
        "destrinchando": [
            "Dedução: CMg = ΔCV/ΔQ = w·ΔL/ΔQ = " + vd("w/PMg<sub>L</sub>") + ". Do mesmo modo, CVMe = w·L/Q = "
            + vd("w/PMe<sub>L</sub>") + ". As curvas de custo são o “espelho” das curvas de produto.",
            "Espelhamento completo: PMg crescente ↔ CMg decrescente; " + vd("PMg máximo ↔ CMg mínimo") + "; "
            + vd("PMe máximo ↔ CVMe mínimo") + ". Exemplo: w = R$ 100; se o PMg<sub>L</sub> cai de 20 para 10 "
            "unidades, o CMg sobe de R$ 5 para R$ 10.",
            "A " + azb("lei dos rendimentos marginais decrescentes") + " é, portanto, a origem do CMg crescente "
            "no curto prazo — e daí vem a curva de oferta positivamente inclinada da firma competitiva (P = CMg, "
            "acima do mínimo do CVMe).",
            "Hipóteses implícitas: curto prazo (capital fixo) e salário constante (a firma é tomadora de preço no "
            "mercado de trabalho).",
            vm("Regra-âncora: produto e custo andam em sentidos opostos — CMg = w/PMg."),
        ],
        "dissecando": (cz("[literalidade]") + " Relação-padrão de dualidade, enunciada como condicional (“se… "
                       "então”). O candidato hesita porque “decrescente” e “crescente” parecem contraditórios; "
                       "é justamente essa oposição que está certa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o produto médio do trabalho for máximo, o custo variável médio será mínimo.”</i> → CERTO",
            "<i>“Se o produto marginal do trabalho for decrescente, o custo total médio será necessariamente "
            "crescente.”</i> → ERRADO (o CTMe ainda cai enquanto o CMg estiver abaixo dele)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["se… então"], "dificuldade": 1,
        "comentario_fonte": "CMg = w/PMgL; com salário constante, PMgL decrescente implica CMg crescente "
                            "(dualidade entre produção e custos).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: fonte indica apenas “Aula 7” do professor, sem prova de origem"],
    },
    # ------------------------------------------------------------------ E1-0222
    {
        "id": "ECO-E1-0222-1", "fonte_ref": "E1-0222", "destino": "06", "subtema": H2["ccp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_RT_FIRMA,
        "rotulo_item": "Item",
        "assertiva": "Se o custo marginal estiver acima do custo total médio, então este último está diminuindo.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o custo marginal estiver acima do custo total médio, então este último está ")
                    + vm("diminuindo") + az(".")),
        "poucas": ("Se a unidade extra custa <b>mais</b> que a média, ela puxa a média para cima: com "
                   "CMg > CTMe, o " + azb("CTMe está aumentando") + "."),
        "destrinchando": [
            "Regra da média: com média 7 na disciplina, tirar 9 na próxima prova sobe a média; tirar 5 a "
            "derruba. No custo: " + vd("CMg &lt; CTMe") + " → CTMe cai; " + vd("CMg = CTMe") + " → CTMe no "
            "mínimo; " + vd("CMg > CTMe") + " → CTMe sobe.",
            "Atenção: o que decide é a <b>posição</b> do CMg em relação à média, não a inclinação do CMg. O CMg "
            "já começa a subir antes do mínimo do CTMe — nesse trecho, ainda abaixo da média, ele continua a "
            "puxá-la para baixo.",
            "Formato em U do CTMe = " + azb("CFMe") + " (sempre decrescente, pela diluição do custo fixo) + "
            + azb("CVMe") + " (crescente a partir de certo ponto, pelos rendimentos decrescentes).",
            "O CMg corta o CVMe e o CTMe nos respectivos mínimos; o mínimo do CVMe vem antes (à esquerda), "
            "porque CTMe − CVMe = CFMe > 0 e ainda está caindo.",
            "Importância: o mínimo do CTMe é a " + azb("escala eficiente") + " da planta; na concorrência "
            "perfeita de longo prazo, o preço converge para ele.",
        ],
        "grafico_verso": "ECO-E1-0222-1-V1",
        "dissecando": (cz("[inversão]") + " O item inverte a relação marginal × média. Quem guarda só a "
                       "imagem do CMg “cortando” o CTMe, sem saber de que lado está cada trecho, cai. Pista: "
                       "“acima” ↔ “aumentando”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o custo marginal estiver crescendo, o custo total médio também estará crescendo.”</i> → "
            "ERRADO (o CMg sobe antes do mínimo do CTMe)",
            "<i>“O custo marginal intercepta o custo variável médio no ponto mínimo deste.”</i> → CERTO",
        ])],
        "reescrita": ("Se o custo marginal estiver acima do custo total médio, então este último está "
                      + hl("aumentando") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["se… então"], "dificuldade": 1,
        "comentario_fonte": "É o contrário: com CMg > CTMe, o CTMe está subindo; o CMg passa pelo mínimo do CTMe. "
                            "Analogia da nota da prova e da média.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (74).png, image (75).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagens não preservadas; mecanismo redesenhado em ECO-E1-0222-1-V1)"}],
        "alertas": ["nota_redacao: fonte indica apenas “Aula 7” do professor, sem prova de origem"],
    },
    # ------------------------------------------------------------------ E1-0223
    {
        "id": "ECO-E1-0223-1", "fonte_ref": "E1-0223", "destino": "06", "subtema": H2["clp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False, "errei": True,
        "comando": CMD_RT_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Se a função de produção tem retornos de escala constantes, então o custo total médio de "
                      "longo prazo será crescente"),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se a função de produção tem retornos de escala constantes, então o custo total médio de "
                       "longo prazo será ") + vm("crescente")),
        "poucas": ("Com " + azb("retornos constantes") + " (e preços de fatores dados), dobrar a produção dobra "
                   "os insumos e o custo total: o " + vd("CTMe de longo prazo é constante") + " (horizontal). "
                   "Crescente seria com retornos decrescentes."),
        "destrinchando": [
            "Mapa escala → custo, com preços dos fatores constantes: retornos " + vd("crescentes") + " → CMeLP "
            "decrescente (economias de escala); " + vd("constantes") + " → CMeLP constante, e CMgLP = CMeLP; "
            + vd("decrescentes") + " → CMeLP crescente (deseconomias).",
            "Conta: com retornos constantes, produzir 2Q exige 2K e 2L; o custo vai de wL + rK para 2(wL + rK). "
            "Custo médio = CT/Q fica igual.",
            "A ressalva “preços dos fatores constantes” importa: se a expansão da firma encarece os insumos que "
            "ela compra (deseconomias <b>pecuniárias</b>), o custo médio pode subir mesmo com tecnologia de "
            "retornos constantes.",
            "Por isso se distinguem " + azb("rendimentos de escala") + " (propriedade da função de produção) e "
            + azb("economias de escala") + " (comportamento do custo médio).",
            "A CMeLP típica em U combina os três trechos: economias no início, um fundo plano ou ponto de "
            "mínimo (escala eficiente) e deseconomias depois.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item associa retornos constantes ao comportamento de "
                       "custo dos retornos decrescentes. Pista: “constante” na produção vira “constante” no "
                       "custo médio — a palavra se conserva."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com retornos constantes de escala e preços dos fatores dados, o custo marginal de longo prazo "
            "iguala o custo médio de longo prazo.”</i> → CERTO",
            "<i>“Retornos crescentes de escala implicam custo médio de longo prazo crescente.”</i> → ERRADO "
            "(inversão: implicam custo médio decrescente)",
        ])],
        "reescrita": ("Se a função de produção tem retornos de escala constantes, então o custo total médio de "
                      "longo prazo será " + hl("constante") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["se… então"], "dificuldade": 1,
        "comentario_fonte": "Retornos constantes → CTMe de longo prazo constante; crescente seria com retornos "
                            "decrescentes.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: fonte indica apenas “Aula 7” do professor, sem prova de origem"],
    },
    # ------------------------------------------------------------------ E1-0224
    {
        "id": "ECO-E1-0224-1", "fonte_ref": "E1-0224", "destino": "06", "subtema": H2["isc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_RT_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Uma elevação da taxa de juros (custo do capital) relativamente ao salário levará as empresas "
                      "a usarem técnicas de produção menos intensivas em capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma elevação da taxa de juros (custo do capital) relativamente ao salário levará as empresas "
                      "a usarem técnicas de produção <u>menos intensivas em capital</u>."),
        "poucas": ("Juros mais altos encarecem o capital em relação ao trabalho (w/r cai): a isocusto fica mais "
                   "plana e a nova tangência usa " + vd("menos K por unidade de L") + " — efeito substituição."),
        "destrinchando": [
            "O preço do serviço do capital (r) é o seu " + azb("custo de uso") + ": juros (o custo de "
            "oportunidade dos recursos empatados) mais depreciação. Se os juros sobem, r sobe.",
            "Condição de custo mínimo: " + vd("TMST = PMg<sub>L</sub>/PMg<sub>K</sub> = w/r") + ". Com r maior, "
            "w/r cai; para restabelecer a igualdade, a firma precisa reduzir PMg<sub>L</sub>/PMg<sub>K</sub> — "
            "usar mais trabalho e menos capital.",
            "No gráfico (Q fixo): com w = r, o ótimo é A = (4; 4), K/L = 1; se r quadruplica, o ótimo passa a "
            "B = (8; 2), " + vd("K/L = 1/4") + ".",
            "Ressalva: isso é o efeito-substituição, com produção dada. O custo maior também pode reduzir a "
            "escala (efeito-produção) e, com ele, o uso dos dois fatores. Mas a <b>intensidade</b> em capital "
            "(K/L), que é o que o item afirma, cai.",
            "Exceção: com " + azb("complementares perfeitos") + " (isoquanta em L, proporções fixas), não há "
            "substituição e K/L não muda.",
        ],
        "grafico_verso": "ECO-E1-0224-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " Item de mecanismo direto. O cuidado é ler “intensivas em "
                       "capital” como proporção K/L, e não como quantidade absoluta de capital — é isso que "
                       "garante o CERTO independentemente do efeito-produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma elevação dos salários em relação à taxa de juros levará as empresas a adotar técnicas mais "
            "intensivas em capital.”</i> → CERTO",
            "<i>“Com tecnologia de proporções fixas, a alta dos juros reduz a relação capital/trabalho.”</i> → "
            "ERRADO (proporções fixas: não há substituição)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["relativamente"], "dificuldade": 1,
        "comentario_fonte": "Juros maiores elevam o custo do capital em relação ao salário; a minimização de "
                            "custos leva à substituição de capital por trabalho.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: fonte indica apenas “Aula 7” do professor, sem prova de origem"],
    },
    # ------------------------------------------------------------------ E1-0225
    {
        "id": "ECO-E1-0225-1", "fonte_ref": "E1-0225", "destino": "06", "subtema": H2["isc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_RT_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("A firma minimiza custos quando a inclinação da curva de isocusto (salário/remuneração do "
                      "capital) é igual à razão entre os produtos marginais do trabalho e do capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A firma minimiza custos quando a inclinação da curva de isocusto (<u>salário/remuneração do "
                      "capital</u>) é igual à razão entre os produtos marginais <u>do trabalho e do capital</u>."),
        "poucas": ("No custo mínimo, isocusto e isoquanta são tangentes: " + vd("w/r = PMg<sub>L</sub>/"
                   "PMg<sub>K</sub> = TMST") + " — ou, o que é o mesmo, PMg<sub>L</sub>/w = PMg<sub>K</sub>/r."),
        "destrinchando": [
            azb("Isocusto") + ": C = wL + rK → K = C/r − (w/r)·L; inclinação (em módulo) = " + vd("w/r") + ", o "
            "preço relativo do trabalho. " + azb("Isoquanta") + ": inclinação = TMST = PMg<sub>L</sub>/"
            "PMg<sub>K</sub>.",
            "Três formas da mesma condição: (1) tangência entre a isocusto e a isoquanta; (2) TMST = w/r; "
            "(3) " + vd("PMg<sub>L</sub>/w = PMg<sub>K</sub>/r") + " — o último real gasto rende o mesmo produto "
            "em qualquer fator.",
            "Fora do ótimo: w = 20, r = 10, PMg<sub>L</sub> = 30, PMg<sub>K</sub> = 10 → PMg<sub>L</sub>/w = 1,5 "
            "> PMg<sub>K</sub>/r = 1. Cada real em trabalho rende mais: trocar capital por trabalho reduz o custo "
            "até a igualdade.",
            "Condições para a tangência ser mínimo: isoquantas convexas (TMST decrescente) e solução interior "
            "(a firma usa os dois fatores).",
            "É o espelho exato do consumidor: TMS = P<sub>X</sub>/P<sub>Y</sub>, ou UMg<sub>X</sub>/P<sub>X</sub> "
            "= UMg<sub>Y</sub>/P<sub>Y</sub>.",
        ],
        "dissecando": (cz("[literalidade]") + " Enunciado de manual. O risco está na <b>ordem</b> das razões: "
                       "trabalho em cima dos dois lados (w/r com PMg<sub>L</sub>/PMg<sub>K</sub>). A banca "
                       "costuma inverter uma delas para fabricar o ERRADO."),
        "modulos": [
            ("🧠 Mnemônico", ["“Trabalho em cima nos dois lados”: w/r = PMg<sub>L</sub>/PMg<sub>K</sub>."]),
            ("😈 Para dificultar", [
                "<i>“…é igual à razão entre os produtos marginais do capital e do trabalho.”</i> → ERRADO (razão "
                "invertida)",
                "<i>“No ponto de custo mínimo, o produto marginal por real gasto é o mesmo em todos os "
                "fatores.”</i> → CERTO",
            ]),
        ],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Tangência entre isocusto (inclinação w/r) e isoquanta (PMgL/PMgK); três formas do "
                            "ponto ótimo: tangência, TMST = preço relativo, PMgL/w = PMgK/r.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (72).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": ["nota_redacao: fonte indica apenas “Aula 7” do professor, sem prova de origem"],
    },
    # ------------------------------------------------------------------ E1-0237
    {
        "id": "ECO-E1-0237-1", "fonte_ref": "E1-0237", "destino": "06", "subtema": H2["clp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo a custos de produção e economias de escala.",
        "rotulo_item": "Item",
        "assertiva": ("Alegar que as escolas públicas brasileiras, por serem muito pequenas, apresentam custos "
                      "médios elevados é um raciocínio consistente com a existência de economias de escala na "
                      "produção do ensino público."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Alegar que as escolas públicas brasileiras, por serem muito pequenas, apresentam custos "
                      "médios elevados é um raciocínio <u>consistente com</u> a existência de economias de escala "
                      "na produção do ensino público."),
        "poucas": (azb("Economias de escala") + " = custo médio de longo prazo que cai quando a produção "
                   "aumenta. Unidade pequena opera no trecho descendente da CMeLP — logo, " + vd("custo por "
                   "aluno alto") + ". O raciocínio é coerente."),
        "destrinchando": [
            "Fontes de economias de escala numa escola: custos fixos e indivisíveis (direção, secretaria, "
            "biblioteca, laboratório, quadra) diluídos por mais alunos; professores especializados com turmas "
            "completas; compras em volume.",
            "Exemplo: um professor de física com 3 turmas ou com 10 turmas recebe o mesmo salário por aula, mas "
            "a escola pequena paga-o subocupado; o custo por aluno da disciplina é maior.",
            "Limites: a partir de certo tamanho surgem " + azb("deseconomias") + " (gestão mais difícil, turmas "
            "superlotadas, deslocamentos longos dos alunos), e há a dimensão da qualidade, que o custo médio não "
            "capta.",
            rx("No Brasil") + ", o argumento aparece no debate sobre a " + azb("nucleação") + " de escolas "
            "rurais pequenas (agrupamento em unidades maiores com transporte escolar), em que o ganho de escala "
            "é confrontado com o custo do transporte e com o fechamento de escolas próximas das comunidades.",
            "O item pede <b>consistência lógica</b> do argumento com a teoria, não a sua verdade empírica.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " “Consistente com” rebaixa a exigência: "
                       "basta que a alegação decorra do conceito. Quem procura dado empírico sobre escolas "
                       "brasileiras para julgar perde tempo — é aplicação direta de economias de escala."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Alegar que escolas muito grandes têm custo médio elevado é consistente com a existência de "
            "deseconomias de escala.”</i> → CERTO",
            "<i>“Se o ensino público tivesse retornos constantes de escala, escolas menores teriam custo médio "
            "por aluno mais alto.”</i> → ERRADO (com retornos constantes e preços dados, a CMeLP é constante)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["consistente com"],
        "dificuldade": 1,
        "comentario_fonte": "Correta: economias de escala; escola maior dilui custos (um aluno a mais não eleva "
                            "proporcionalmente o custo do professor), reduzindo o custo médio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE/CACD 2012 (não confirmada: a fonte só traz o ano entre "
                    "parênteses)"],
    },
    # ------------------------------------------------------------------ E2-L00020
    {
        "id": "ECO-E2-L00020-1", "fonte_ref": "E2-L00020", "destino": "06", "subtema": H2["ccp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_IDEG,
        "rotulo_item": "Item",
        "assertiva": ("O custo marginal é sempre inferior ao custo médio em todos os pontos de produção, o que "
                      "implica que o custo médio continuará a cair conforme o volume de produção aumenta. Este "
                      "fenômeno ocorre devido à capacidade das empresas de diluir seus custos fixos "
                      "proporcionalmente à quantidade produzida, garantindo que a média de custos seja "
                      "constantemente reduzida à medida que a produção se expande."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O custo marginal é ") + vm("sempre inferior ao custo médio em todos os pontos de produção")
                    + az(", o que implica que o custo médio ") + vm("continuará a cair conforme o volume de "
                    "produção aumenta") + az(". Este fenômeno ocorre devido à capacidade das empresas de diluir seus "
                    "custos fixos proporcionalmente à quantidade produzida, ") + vm("garantindo que a média de "
                    "custos seja constantemente reduzida à medida que a produção se expande") + az(".")),
        "poucas": ("No curto prazo o custo médio tem formato de " + azb("U") + ": a diluição do custo fixo o "
                   "puxa para baixo, mas os rendimentos decrescentes acabam puxando-o para cima. Depois do "
                   "mínimo, " + vd("CMg > CMe") + "."),
        "destrinchando": [
            "CTMe = " + azb("CFMe") + " + " + azb("CVMe") + ". O CFMe = CF/q cai sempre (a diluição é real); o "
            "CVMe, depois de certo ponto, sobe por causa da " + azb("lei dos rendimentos marginais "
            "decrescentes") + " (CMg = w/PMg crescente).",
            "Enquanto a queda do CFMe domina, o CTMe cai; quando a alta do CVMe passa a dominar, ele sobe. O "
            "ponto de virada é exatamente onde " + vd("CMg = CMe") + " — o mínimo do custo médio.",
            "A implicação lógica do item está certa (se o CMg fosse sempre menor, a média cairia sempre); o que "
            "é falso é a premissa e a garantia de queda contínua.",
            "Onde o item quase vale: no " + azb("monopólio natural") + " (custo fixo enorme e CMg baixo e "
            "constante — redes de água, energia, ferrovias), o CMe é decrescente em toda a faixa relevante de "
            "demanda. É um caso particular, não a regra de “todos os pontos de produção”.",
            vm("Regra-âncora: CMg abaixo da média → média cai; acima → média sobe; igual → mínimo."),
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " O item embrulha um fato verdadeiro (a "
                       "diluição do custo fixo) em generalizações: “sempre”, “em todos os pontos”, “continuará”, "
                       "“constantemente”. Excesso de absolutos num item de custos é sinal forte de ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um monopólio natural, com custo fixo elevado e custo marginal constante, o custo médio é "
            "decrescente em toda a faixa relevante de produção.”</i> → CERTO",
            "<i>“A diluição dos custos fixos faz o custo variável médio cair indefinidamente.”</i> → ERRADO "
            "(a diluição atua no CFMe, não no CVMe)",
        ])],
        "reescrita": ("O custo marginal " + hl("fica abaixo do custo médio apenas até o ponto mínimo deste") + ", o "
                      "que implica que o custo médio " + hl("cai até esse ponto e depois sobe") + ". Este fenômeno "
                      "ocorre devido à capacidade das empresas de diluir seus custos fixos proporcionalmente à "
                      "quantidade produzida, " + hl("efeito que acaba superado pelos rendimentos decrescentes, que "
                      "fazem o custo médio voltar a subir") + "."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"],
        "moduladores": ["sempre", "em todos os pontos", "constantemente"], "dificuldade": 1,
        "comentario_fonte": "O CMg pode ser inferior ou superior ao CMe conforme o ponto; abaixo, puxa a média para "
                            "baixo; acima, para cima. A diluição dos custos fixos reduz o CMe só em certa medida.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00021
    {
        "id": "ECO-E2-L00021-1", "fonte_ref": "E2-L00021", "destino": "06", "subtema": H2["ccp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_IDEG,
        "rotulo_item": "Item",
        "assertiva": ("A curva de custo variável médio tende a se aproximar da curva de custo total médio conforme a "
                      "produção aumenta, devido à diluição do custo marginal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva de custo variável médio tende a se aproximar da curva de custo total médio conforme "
                       "a produção aumenta, devido à diluição do custo ") + vm("marginal") + az(".")),
        "poucas": ("A distância entre CTMe e CVMe é o " + azb("custo fixo médio") + " (CF/q), que encolhe "
                   "quando q cresce. O que se dilui é o custo <b>fixo</b>; o marginal não se dilui."),
        "destrinchando": [
            "Identidade: " + vd("CTMe − CVMe = CFMe = CF/q") + ". Com CF = R$ 1.000, a distância vertical é 100 "
            "com q = 10 e 10 com q = 100.",
            "As curvas se aproximam <b>assintoticamente</b>, mas nunca se tocam no curto prazo, porque CF > 0 "
            "faz CFMe > 0 em qualquer q.",
            "O " + azb("custo marginal") + " é ΔCV/Δq: não contém nenhuma parcela fixa, logo não há o que "
            "“diluir”. Ele é o que determina se as médias sobem ou caem, não a distância entre elas.",
            "Por causa dessa distância decrescente, o mínimo do CVMe ocorre em q menor que o mínimo do CTMe, e o "
            "CMg corta os dois nos respectivos mínimos.",
            "No longo prazo não existe custo fixo: CVMe e CTMe coincidem. A aproximação descrita no item é "
            "fenômeno de <b>curto prazo</b>.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Uma palavra trocada: “marginal” no lugar de “fixo”. O resto "
                       "do item (as curvas se aproximam) está certo, o que induz o CERTO na leitura rápida."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A distância vertical entre o CTMe e o CVMe diminui com a produção porque o custo fixo médio é "
            "decrescente.”</i> → CERTO",
            "<i>“O valor do custo fixo influencia o formato da curva de custo marginal.”</i> → ERRADO (o CMg só "
            "depende do custo variável)",
        ])],
        "reescrita": ("A curva de custo variável médio tende a se aproximar da curva de custo total médio conforme "
                      "a produção aumenta, devido à diluição do custo " + hl("fixo") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Os custos fixos é que se diluem, aproximando CVMe e CTMe; o comentário acrescenta "
                            "“especialmente em uma análise de longo prazo”, o que é incorreto (no longo prazo não "
                            "há custo fixo).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem associa a diluição do custo fixo ao longo prazo; ela "
                    "é fenômeno de curto prazo"],
    },
    # ------------------------------------------------------------------ E2-L00022
    {
        "id": "ECO-E2-L00022-1", "fonte_ref": "E2-L00022", "destino": "06", "subtema": H2["clp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_IDEG,
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, o custo fixo já não é relevante para a análise de custos, pois ele está "
                      "diluído pela produção intensiva. Além disso, a longo prazo, os rendimentos de escala, sejam "
                      "crescentes, decrescentes ou constantes, influenciam significativamente a modelagem dos "
                      "custos da empresa, permitindo maior flexibilidade e adaptação conforme a estrutura de "
                      "produção se estabiliza."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("No longo prazo, o custo fixo já não é relevante para a análise de custos, <u>pois ele está "
                      "diluído pela produção intensiva</u>. Além disso, a longo prazo, os rendimentos de escala, "
                      "sejam crescentes, decrescentes ou constantes, influenciam significativamente a modelagem "
                      "dos custos da empresa, permitindo maior flexibilidade e adaptação conforme a estrutura de "
                      "produção se estabiliza."),
        "poucas": ("As duas conclusões valem: no longo prazo não há custo fixo, e a escala molda a curva de "
                   "custo médio. Mas a <b>justificativa</b> está errada — não há custo fixo porque " + azb("todos "
                   "os fatores são variáveis") + ", não porque ele “se diluiu”."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o gabarito do simulado é CERTO, mas a oração causal “pois ele está diluído pela produção "
                          "intensiva” é falsa: a diluição (CFMe = CF/q cada vez menor) é fenômeno de curto prazo e "
                          "nunca zera o custo fixo. Numa banca rigorosa como o CEBRASPE, a justificativa errada "
                          "tenderia a tornar o item ERRADO, resposta que parece mais defensável.")],
        "destrinchando": [
            azb("Longo prazo") + " não é um prazo de calendário: é o horizonte em que a firma pode ajustar "
            "<b>todos</b> os fatores, inclusive o tamanho da planta. Por definição, não há custo fixo — todo "
            "custo é variável (ou evitável).",
            azb("Curto prazo") + ": ao menos um fator fixo, logo há custo fixo. O CFMe = CF/q cai com a "
            "produção, mas nunca chega a zero — “diluir” não é “eliminar”.",
            "No longo prazo, quem dá o formato da " + azb("CMeLP") + " são os rendimentos de escala (com preços "
            "de fatores dados): crescentes → CMeLP decrescente; constantes → plana; decrescentes → crescente.",
            "A CMeLP é a envoltória das curvas de curto prazo: para cada nível de produção, a firma escolhe a "
            "planta que dá o menor custo médio.",
            "Leitura de prova: um item cujo núcleo está certo e cuja justificativa (“pois…”) está errada é, em "
            "regra, ERRADO no CEBRASPE. Simulados de curso nem sempre seguem esse rigor.",
        ],
        "dissecando": (cz("[detalhe]") + " A segunda frase é genérica e verdadeira; o ponto sensível é o "
                       "conectivo causal “pois”, que amarra a conclusão certa a uma causa errada. Sempre teste a "
                       "oração explicativa separadamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, todos os custos são variáveis, porque a firma pode ajustar todos os fatores, "
            "inclusive o tamanho da planta.”</i> → CERTO",
            "<i>“No curto prazo, o custo fixo médio torna-se nulo quando a produção é suficientemente "
            "grande.”</i> → ERRADO (o CFMe tende a zero, mas nunca se anula)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["pois"], "dificuldade": 2,
        "comentario_fonte": "No longo prazo os custos fixos são irrelevantes por estarem diluídos; os fatores "
                            "tornam-se variáveis e os rendimentos de escala influenciam os custos.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: a justificativa “pois ele está diluído pela produção intensiva” é falsa (no "
                    "longo prazo não há custo fixo porque todos os fatores são variáveis); ERRADO seria mais "
                    "defensável — mantido o gabarito CERTO da fonte"],
    },
    # ------------------------------------------------------------------ E2-L00329
    {
        "id": "ECO-E2-L00329-1", "fonte_ref": "E2-L00329", "destino": "06", "subtema": H2["clp"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo às curvas de custo de longo prazo.",
        "rotulo_item": "Item",
        "assertiva": ("A curva de Custo Médio de Longo Prazo (CMeLP) é formada pelo envelope inferior das curvas de "
                      "Custo Médio de Curto Prazo (CMeCP). Geometricamente, a CMeLP tangencia o ponto mínimo de "
                      "cada curva de CMeCP, independentemente do tipo de rendimentos de escala que a firma "
                      "apresente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva de Custo Médio de Longo Prazo (CMeLP) é formada pelo envelope inferior das curvas "
                       "de Custo Médio de Curto Prazo (CMeCP). Geometricamente, a CMeLP tangencia ")
                    + vm("o ponto mínimo de cada curva") + az(" de CMeCP, ")
                    + vm("independentemente do tipo de rendimentos de escala que a firma apresente") + az(".")),
        "poucas": ("A " + azb("envoltória") + " está certa, mas a tangência só ocorre no mínimo da CMeCP onde há "
                   "rendimentos constantes (fundo da CMeLP). Com economias de escala, ela fica no trecho "
                   + vd("descendente") + " da CMeCP; com deseconomias, no " + vd("ascendente") + "."),
        "destrinchando": [
            "Duas curvas tangentes têm a mesma inclinação no ponto de contato. Onde a CMeLP é decrescente "
            "(economias de escala), a CMeCP tangente também está descendo — seu mínimo fica à direita. Onde a "
            "CMeLP é crescente, a CMeCP tangente está subindo — seu mínimo fica à esquerda.",
            "No gráfico: T₁ (q = 5) está à esquerda do mínimo M₁ (q = 6,25); T₃ (q = 15), à direita de M₃ "
            "(q = 13,75); só em T₂, no mínimo da CMeLP, a tangência coincide com o mínimo da CMeCP.",
            "Intuição econômica: para produzir pouco quando há economias de escala, compensa usar uma planta "
            "um pouco maior e operá-la abaixo do seu ponto de custo mínimo (subutilização); com deseconomias, "
            "compensa uma planta menor operada acima dele (sobreutilização).",
            "Única exceção que tornaria o item verdadeiro: rendimentos <b>constantes</b> em toda a extensão "
            "(CMeLP horizontal), quando todas as tangências se dão nos mínimos.",
            "No ponto de tangência, também os custos marginais de curto e longo prazo se igualam; o CMgLP corta "
            "a CMeLP no mínimo desta.",
        ],
        "grafico_verso": "ECO-E2-L00329-1-V1",
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " A 1ª frase (envoltória) é de manual; o erro "
                       "foi enxertado na 2ª, com o absoluto “independentemente do tipo de rendimentos de "
                       "escala”. 🔥 É o “erro de Viner”, clássico em provas de micro."),
        "modulos": [
            ("📚 Autores e teses", [
                oc("Jacob Viner") + " (“Cost Curves and Supply Curves”, 1931) pediu ao desenhista que traçasse "
                "a curva de longo prazo passando pelos mínimos de todas as curvas de curto prazo e por baixo "
                "delas; o desenhista mostrou que as duas exigências são incompatíveis. O episódio virou o nome "
                "do erro.",
            ]),
            ("😈 Para dificultar", [
                "<i>“No ponto mínimo da CMeLP, a CMeCP tangente também está em seu mínimo.”</i> → CERTO",
                "<i>“Com deseconomias de escala, a tangência entre a CMeLP e a CMeCP ocorre no trecho descendente "
                "da CMeCP.”</i> → ERRADO (inversão: ocorre no trecho ascendente)",
            ]),
        ],
        "reescrita": ("A curva de Custo Médio de Longo Prazo (CMeLP) é formada pelo envelope inferior das curvas de "
                      "Custo Médio de Curto Prazo (CMeCP). Geometricamente, a CMeLP tangencia " + hl("cada curva")
                      + " de CMeCP, " + hl("mas só no ponto mínimo desta onde há rendimentos constantes de escala; "
                      "com economias de escala, a tangência ocorre no trecho descendente da CMeCP e, com "
                      "deseconomias, no trecho ascendente") + "."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["independentemente"], "dificuldade": 2,
        "comentario_fonte": "A CMeLP só tangencia os mínimos das CMeCP com retornos constantes; com economias de "
                            "escala, na parte descendente; com deseconomias, na ascendente.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 045", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00329-1-V1, com as três situações de tangência)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00535
    {
        "id": "ECO-E2-L00535-1", "fonte_ref": "E2-L00535", "destino": "06", "subtema": H2["ccp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação às estruturas de mercado, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A concorrência perfeita e o monopólio são duas estruturas de mercado consideradas opostas em "
                      "vários aspectos, todavia há pontos em comum na análise do comportamento da firma em um "
                      "ambiente de concorrência perfeita e em um ambiente monopolista. Considerando firmas que "
                      "produzem um único produto com custos marginais convexos, tanto no ambiente de concorrência "
                      "perfeita quanto no monopólio, se o custo marginal se iguala ao custo médio, então a produção "
                      "tem o menor custo médio possível."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A concorrência perfeita e o monopólio são duas estruturas de mercado consideradas opostas em "
                      "vários aspectos, todavia há pontos em comum na análise do comportamento da firma em um "
                      "ambiente de concorrência perfeita e em um ambiente monopolista. Considerando firmas que produzem um único "
                      "produto com custos marginais convexos, <u>tanto</u> no ambiente de concorrência perfeita "
                      "<u>quanto</u> no monopólio, se o custo marginal se iguala ao custo médio, então a produção "
                      "tem o menor custo médio possível."),
        "poucas": (vd("CMg = CMe") + " ocorre no mínimo do custo médio por uma propriedade matemática da função "
                   "de custo. A estrutura de mercado não entra na conta: ela só decide se a firma produz ou não "
                   "nesse ponto."),
        "destrinchando": [
            "Prova em uma linha: d(CT/q)/dq = (CMg − CMe)/q. A derivada do custo médio é zero exatamente quando "
            + vd("CMg = CMe") + "; antes, negativa (CMg &lt; CMe); depois, positiva.",
            "A hipótese de custos “bem-comportados” (CMg em U, CMe em U) garante que esse ponto é um "
            + azb("mínimo") + ", e não um máximo, e que há um único cruzamento.",
            "O que muda entre as estruturas é <b>onde a firma produz</b>: em " + azb("concorrência perfeita")
            + ", no longo prazo, P = CMg = CMe mínimo (lucro econômico nulo, escala eficiente). O "
            + azb("monopolista") + " produz onde RMg = CMg, em geral fora do mínimo do CMe.",
            "Por isso o item é condicional: “<b>se</b> o CMg se iguala ao CMe, então…”. Não afirma que o "
            "monopolista opera no custo mínimo — afirma que, se a igualdade ocorrer, ali está o mínimo.",
            "Item quase idêntico, de outro simulado da mesma origem: ECO-E2-L00865-1.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " O preâmbulo sobre estruturas “opostas” sugere que a resposta "
                       "depende do mercado. Não depende: a relação marginal × média é propriedade dos custos. "
                       "Pista: o “tanto… quanto” está protegido pelo “se… então”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Tanto em concorrência perfeita quanto em monopólio, a firma produz, no longo prazo, no ponto de "
            "mínimo custo médio.”</i> → ERRADO (só a firma competitiva; o monopolista produz onde RMg = CMg)",
            "<i>“Se o custo marginal for igual ao custo médio, o custo médio estará em seu ponto mínimo, qualquer "
            "que seja a estrutura de mercado.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["se… então"], "dificuldade": 1,
        "comentario_fonte": "CMg = CTMe no mínimo do custo médio; a regra vale em qualquer estrutura de mercado.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: mesma tese de ECO-E2-L00865-1 (outro simulado Nabuco, com enunciado mais "
                    "curto); mantidos os dois (Folha -Q §8.6)"],
    },
    # ------------------------------------------------------------------ E2-L00651
    {
        "id": "ECO-E2-L00651-1", "fonte_ref": "E2-L00651", "destino": "06", "subtema": H2["clp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à microeconomia, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Uma empresa pode ter economias de escala ao mudar sua tecnologia ou combinação de insumos, "
                      "mesmo que seu processo produtivo demonstre rendimentos marginais decrescentes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma empresa <u>pode</u> ter economias de escala ao mudar sua tecnologia ou combinação de "
                      "insumos, <u>mesmo que</u> seu processo produtivo demonstre rendimentos marginais "
                      "decrescentes."),
        "poucas": ("Rendimentos marginais decrescentes são fenômeno de " + azb("curto prazo") + " (um fator "
                   "varia, os outros fixos); economias de escala, de " + azb("longo prazo") + " (todos os insumos "
                   "e até a tecnologia se ajustam). Um não exclui o outro."),
        "destrinchando": [
            azb("Rendimento marginal decrescente") + ": acrescentar trabalhadores a uma fábrica de tamanho fixo "
            "rende cada vez menos. " + azb("Economias de escala") + ": ao ampliar a produção com liberdade para "
            "ajustar tudo, o custo médio de longo prazo cai.",
            "Exemplo: Q = K<sup>0,6</sup>·L<sup>0,6</sup> tem PMg decrescente em cada fator e, ao mesmo tempo, "
            "retornos crescentes de escala (soma 1,2) — portanto custo médio de longo prazo decrescente com "
            "preços de fatores dados.",
            "Economias de escala são conceito mais amplo que rendimentos crescentes de escala: admitem " + azb(
                "mudar a proporção dos insumos") + " e a técnica ao crescer (distinção feita, por exemplo, em "
            + oc("Pindyck e Rubinfeld") + ", <i>Microeconomia</i>). Fontes típicas: especialização, "
            "indivisibilidades, compras em grande volume, acesso a técnicas que só compensam em grande escala.",
            "Logo, a frase do item reúne exatamente as duas dimensões: curto prazo com rendimentos decrescentes "
            "e longo prazo com custo médio caindo.",
            vm("Regra-âncora: rendimento marginal = um fator, curto prazo; economia de escala = custo médio, "
               "longo prazo."),
        ],
        "dissecando": (cz("[modulador relativo]") + " “Pode” e “mesmo que” deixam o item no terreno da "
                       "possibilidade: basta um caso para ser CERTO. A armadilha é achar que rendimentos "
                       "decrescentes implicam custos médios sempre crescentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Rendimentos marginais decrescentes do trabalho no curto prazo implicam deseconomias de escala no "
            "longo prazo.”</i> → ERRADO (nexo indevido: horizontes e conceitos distintos)",
            "<i>“Uma firma pode ter rendimentos marginais decrescentes em cada fator e rendimentos crescentes de "
            "escala.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode", "mesmo que"], "dificuldade": 1,
        "comentario_fonte": "Horizontes distintos: rendimentos marginais decrescentes no curto prazo (um fator "
                            "varia); economias de escala no longo prazo (todos variam). É possível ter os dois.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00865
    {
        "id": "ECO-E2-L00865-1", "fonte_ref": "E2-L00865", "destino": "06", "subtema": H2["ccp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação às estruturas de mercado, julgue (C ou E) o item que se segue.",
        "rotulo_item": "Item",
        "assertiva": ("Tanto no ambiente de concorrência perfeita quanto no monopólio, se o custo marginal se iguala "
                      "ao custo médio, então a produção tem o menor custo médio possível."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Tanto</u> no ambiente de concorrência perfeita <u>quanto</u> no monopólio, se o custo "
                      "marginal se iguala ao custo médio, então a produção tem o menor custo médio possível."),
        "poucas": ("O CMg cruza o CMe no ponto mínimo deste em <b>qualquer</b> estrutura de mercado: é "
                   "propriedade da " + azb("função de custo") + ", não da demanda nem do preço."),
        "destrinchando": [
            "Exemplo numérico: CT = 100 + q² → CMe = 100/q + q e CMg = 2q. Igualando: 2q = 100/q + q → "
            + vd("q = 10") + ", com " + vd("CMe = CMg = 20") + ". Teste: em q = 9, CMe ≈ 20,1; em q = 11, "
            "CMe ≈ 20,1 — o 20 é mesmo o mínimo.",
            "A conta não usa preço, receita nem número de concorrentes: por isso vale igualmente para a firma "
            "competitiva e para o monopolista.",
            "Onde as estruturas diferem: a firma competitiva produz onde P = CMg e, no longo prazo, no mínimo "
            "do CMe; o " + azb("monopolista") + " produz onde RMg = CMg, em geral com P > CMg e fora do mínimo "
            "do CMe (ineficiência alocativa e, muitas vezes, produtiva).",
            "A mesma lógica liga PMg e PMe na produção: o PMg corta o PMe no máximo deste.",
            "Item quase idêntico, de outro simulado da mesma origem: ECO-E2-L00535-1.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " A menção ao monopólio induz a pensar que, com poder de mercado, "
                       "a regra mudaria. Não muda: o item fala de custos, e a relação marginal × média é "
                       "geométrica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio, como o preço supera o custo marginal, a igualdade entre custo marginal e custo "
            "médio não corresponde ao mínimo do custo médio.”</i> → ERRADO (a propriedade independe do preço)",
            "<i>“Em concorrência perfeita, no equilíbrio de longo prazo, P = CMg = CMe mínimo.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["se… então"], "dificuldade": 1,
        "comentario_fonte": "Independentemente da estrutura de mercado, o CMg cruza o CMe no ponto mínimo deste.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: mesma tese de ECO-E2-L00535-1 (outro simulado Nabuco, com preâmbulo); "
                    "mantidos os dois (Folha -Q §8.6)"],
    },
]
