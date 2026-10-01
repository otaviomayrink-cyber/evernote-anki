"""Cards do lote de redação 09 — ECO, passada 01 (notas 03 e 04)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "exc": "😊 Excedentes e eficiência",
    "trib": "💸 Tributos: incidência e peso morto",
    "teto": "🚧 Preços máximos e mínimos",
    "pref": "🧠 Preferências e axiomas",
    "util": "🎯 Utilidade e curvas de indiferença",
    "esc": "⚖️ Escolha ótima do consumidor",
    "dem": "📊 Demanda individual e de mercado",
}

CMD_NABUCO_TRIB = ("Em relação aos impostos indiretos sobre vendas nos mercados em concorrência perfeita, julgue o "
                   "item a seguir.")
CMD_NABUCO_OD = "Acerca da análise microeconômica relacionada à oferta e à demanda, julgue o item subsequente."
CMD_NIDI_ABR_TRIB = ("Elasticidades e incidência tributária em concorrência perfeita. Considerando que a questão se "
                     "limita a mercados de concorrência perfeita, julgue o item a seguir.")
CMD_NIDI_ABR_INTERV = ("No que se refere à intervenção pública no equilíbrio dos mercados, julgue o item a "
                       "seguir.")
CMD_NIDI_DEZ = ("Considerando o ponto de equilíbrio do mercado entre os desejos dos consumidores e dos produtores "
                "e as relações de bem-estar ou peso-morto a partir dessa situação, julgue o item a seguir.")

CARDS = [
    # ------------------------------------------------------------------ E2-L01208
    {
        "id": "ECO-E2-L01208-1", "fonte_ref": "E2-L01208", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Se, em módulo, a elasticidade-preço da oferta ao preço vigente no mercado for menor que a da "
                      "demanda, o ônus decorrente de um aumento na alíquota do imposto recairá mais sobre os "
                      "produtores do que sobre os consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se, em módulo, a elasticidade-preço da <u>oferta</u> ao preço vigente no mercado for "
                      "<u>menor</u> que a da demanda, o ônus decorrente de um aumento na alíquota do imposto "
                      "recairá mais sobre os <u>produtores</u> do que sobre os consumidores."),
        "poucas": ("O ônus do imposto recai mais sobre o " + azb("lado menos elástico") + " do mercado. Oferta "
                   "menos elástica que a demanda → os " + vd("produtores") + " arcam com a maior parte."),
        "destrinchando": [
            "O imposto abre uma " + azb("cunha") + " entre o preço pago pelo comprador (pc) e o recebido pelo "
            "vendedor (pv): pc − pv = t. A questão é quanto da cunha vem de alta de pc e quanto de queda de pv.",
            "Fórmula de repartição (variações pequenas): parcela do consumidor = "
            + vd("ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|)") + "; parcela do produtor = "
            + vd("|ε<sub>D</sub>| / (ε<sub>O</sub> + |ε<sub>D</sub>|)") + ". Se ε<sub>O</sub> < |ε<sub>D</sub>|, "
            "a parcela do produtor passa de 50%.",
            "Intuição: quem tem <b>alternativa</b> foge do imposto. O consumidor com demanda elástica troca de "
            "produto se o preço subir; o produtor com oferta inelástica (terra, safra já plantada, capacidade "
            "instalada) não consegue reduzir a produção e aceita receber menos.",
            "Vale para qualquer variação da alíquota (criação ou aumento) e independe de quem recolhe legalmente o "
            "tributo: " + azb("incidência legal ≠ incidência econômica") + ".",
            vm("Regra-âncora: o lado mais inelástico paga mais (e, numa redução do imposto, ganha mais)."),
        ],
        "grafico_verso": "ECO-E2-L01208-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item reescreve a regra da incidência em linguagem "
                       "de elasticidades “em módulo”. A armadilha é a ordem da comparação: “oferta menor que a "
                       "demanda” = oferta mais inelástica. Quem lê rápido associa imposto sobre vendas a repasse "
                       "ao consumidor e marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade da oferta for, em módulo, maior que a da demanda, o ônus recairá mais sobre os "
            "produtores.”</i> → ERRADO (inversão: recairá mais sobre os consumidores)",
            "<i>“A repartição do ônus depende de o imposto ser recolhido pelo vendedor ou pelo comprador.”</i> → "
            "ERRADO (depende só das elasticidades)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["em módulo", "mais"], "dificuldade": 1,
        "comentario_fonte": "O ônus recai sobre o lado mais inelástico; como a oferta tem menor elasticidade, "
                            "recai mais sobre os produtores.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01209
    {
        "id": "ECO-E2-L01209-1", "fonte_ref": "E2-L01209", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Se a curva de demanda for infinitamente elástica, o ônus da instituição de um imposto sobre "
                      "vendas recairá integralmente sobre os consumidores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a curva de demanda for infinitamente elástica, o ônus da instituição de um imposto sobre "
                      "vendas recairá integralmente sobre os ") + vm("consumidores") + az("."),
        "poucas": ("Demanda infinitamente elástica (horizontal) = consumidor que não aceita pagar um centavo a "
                   "mais. O preço ao consumidor não muda e o imposto inteiro recai sobre os "
                   + vd("vendedores") + "."),
        "destrinchando": [
            "Demanda " + azb("infinitamente elástica") + " (|ε<sub>D</sub>| → ∞) é horizontal: a qualquer preço "
            "acima de p₀ a quantidade demandada vai a zero. Exemplos: a firma em concorrência perfeita diante "
            "da demanda pelo seu produto; o exportador pequeno diante do preço mundial.",
            "Com o imposto, a oferta relevante sobe t (O → O + t). O novo equilíbrio fica na mesma horizontal: "
            + vd("pc = p₀") + " e " + vd("pv = p₀ − t") + ". Toda a cunha sai do preço líquido do vendedor; a "
            "quantidade cai.",
            "Pela fórmula de repartição, a parcela do consumidor é ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|) "
            "→ " + vd("0") + " quando |ε<sub>D</sub>| → ∞.",
            "Os quatro casos-limite que a banca cobra: demanda horizontal ou oferta vertical → vendedor paga "
            "tudo; demanda vertical ou oferta horizontal → comprador paga tudo.",
        ],
        "grafico_verso": "ECO-E2-L01209-1-V1",
        "dissecando": (cz("[troca de ator]") + " O item mantém o “integralmente” (correto para o caso-limite) e "
                       "troca o lado que paga. Quem confunde “infinitamente elástica” com “insensível ao preço” "
                       "cai: é o oposto — sensibilidade máxima."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a curva de demanda for perfeitamente inelástica, o ônus de um imposto sobre vendas recairá "
            "integralmente sobre os consumidores.”</i> → CERTO",
            "<i>“Com demanda infinitamente elástica, o imposto não altera a quantidade transacionada.”</i> → "
            "ERRADO (a quantidade cai; o que não muda é o preço ao consumidor)",
        ])],
        "reescrita": ("Se a curva de demanda for infinitamente elástica, o ônus da instituição de um imposto sobre "
                      "vendas recairá integralmente sobre os " + hl("vendedores") + "."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": ["integralmente"], "dificuldade": 1,
        "comentario_fonte": "Com demanda infinitamente elástica, o ônus recai integralmente sobre os vendedores.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01210
    {
        "id": "ECO-E2-L01210-1", "fonte_ref": "E2-L01210", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("A instituição do imposto não afetará o preço e a quantidade produzida nesse mercado se a "
                      "curva de oferta for infinitamente elástica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A instituição do imposto ") + vm("não afetará o preço e a quantidade produzida")
                   + az(" nesse mercado se a curva de oferta for infinitamente elástica."),
        "poucas": ("Com oferta horizontal, o preço ao consumidor sobe " + vd("o valor inteiro do imposto")
                   + " e a quantidade " + vd("cai") + ". O único preço que não muda é o líquido recebido pelo "
                   "vendedor."),
        "destrinchando": [
            "Oferta " + azb("infinitamente elástica") + " (horizontal) significa que os produtores ofertam "
            "qualquer quantidade a p₀ e nenhuma abaixo dele — típico de custos constantes no longo prazo em "
            "concorrência perfeita.",
            "O imposto desloca a oferta para cima em t. Novo equilíbrio: " + vd("pc = p₀ + t") + " (o consumidor "
            "paga tudo) e " + vd("pv = p₀") + ". Como a demanda é negativamente inclinada, a quantidade cai de "
            "q₀ para q₁.",
            "Repartição: parcela do consumidor = ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|) → "
            + vd("1") + " quando ε<sub>O</sub> → ∞. O ônus é todo do comprador, mas isso não significa ausência "
            "de efeito: há receita (t × q₁) e " + azb("peso morto") + " (o triângulo entre q₁ e q₀).",
            "Para o imposto não alterar a quantidade, seria preciso uma curva <b>vertical</b> (demanda ou oferta "
            "perfeitamente inelástica) — e, mesmo assim, algum preço muda.",
            vm("Regra-âncora: curva horizontal → o seu lado não paga nada; curva vertical → o seu lado paga tudo "
               "e a quantidade não muda."),
        ],
        "grafico_verso": "ECO-E2-L01210-1-V1",
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item confunde “o vendedor não arca com o "
                       "imposto” com “o mercado não se altera”. A pista é pedir preço <b>e</b> quantidade: com "
                       "oferta horizontal, ambos mudam."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a curva de oferta for infinitamente elástica, o preço recebido pelos produtores não se "
            "altera.”</i> → CERTO",
            "<i>“Se a oferta for perfeitamente inelástica, o imposto não altera a quantidade "
            "transacionada.”</i> → CERTO",
            "<i>“Se a oferta for infinitamente elástica, o preço pago pelo consumidor sobe menos que o "
            "imposto.”</i> → ERRADO (sobe exatamente t)",
        ])],
        "reescrita": ("A instituição do imposto " + hl("elevará o preço ao consumidor no valor do imposto e "
                      "reduzirá a quantidade produzida") + " nesse mercado se a curva de oferta for infinitamente "
                      "elástica."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Oferta infinitamente elástica: ônus integral nos compradores; a quantidade se reduz e "
                            "o preço ao consumidor sobe no montante do imposto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01211
    {
        "id": "ECO-E2-L01211-1", "fonte_ref": "E2-L01211", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("A quantidade transacionada no mercado após a instituição do imposto será tanto menor quanto "
                      "mais elástica for a curva de demanda dos consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A quantidade transacionada no mercado após a instituição do imposto será <u>tanto menor "
                      "quanto mais elástica</u> for a curva de demanda dos consumidores."),
        "poucas": ("Com demanda elástica, a mesma alta de preço provocada pelo imposto derruba muito a quantidade: "
                   "o mercado " + azb("encolhe mais") + ", ceteris paribus."),
        "destrinchando": [
            "Fixe a oferta, a alíquota e o equilíbrio inicial. O imposto obriga a abrir uma cunha t entre pc e "
            "pv; a quantidade tem de cair até um ponto em que essa cunha caiba entre as duas curvas.",
            "Se a demanda é " + azb("elástica") + " (mais plana), pequenas altas de pc já cortam muito a "
            "quantidade demandada: o novo equilíbrio fica bem à esquerda. Se é " + azb("inelástica")
            + " (mais íngreme), os consumidores aceitam pagar mais e a quantidade quase não cai.",
            "Vale o mesmo para a oferta: quanto mais elásticas forem <b>as duas</b> curvas, maior a queda de q e "
            "maior o " + azb("peso morto") + " (≈ ½ · t · Δq). Daí a " + oc("regra de Ramsey")
            + ": tributar mais pesadamente as bases inelásticas minimiza a distorção.",
            "Não confundir os dois resultados: a elasticidade decide <b>quem paga</b> (o lado inelástico) e "
            "<b>quanto o mercado encolhe</b> (mais, quanto mais elásticas as curvas). Demanda elástica → o "
            "consumidor paga pouco do imposto, mas a quantidade cai muito.",
        ],
        "grafico_verso": "ECO-E2-L01211-1-V1",
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " A estrutura “tanto menor quanto mais "
                       "elástica” parece contradizer a regra de que o lado elástico “escapa” do imposto. Não "
                       "contradiz: escapar do imposto é justamente comprar menos. 🔥 A banca alterna os dois "
                       "efeitos (incidência × quantidade) no mesmo bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O peso morto de um imposto será tanto maior quanto mais inelástica for a demanda.”</i> → ERRADO "
            "(inversão: maior quanto mais elástica)",
            "<i>“Quanto mais elástica a demanda, maior a parcela do imposto paga pelos consumidores.”</i> → "
            "ERRADO (inversão: menor)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["tanto menor quanto mais"],
        "dificuldade": 2,
        "comentario_fonte": "Demanda elástica: a quantidade reage muito ao preço; a queda da quantidade após o "
                            "imposto é maior. Várias respostas de IA empilhadas distinguem incidência (lado "
                            "inelástico paga) de redução da quantidade (maior com curvas elásticas).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 204", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (cinco formatos de demanda; substituída por ECO-E2-L01211-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01212
    {
        "id": "ECO-E2-L01212-1", "fonte_ref": "E2-L01212", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_OD,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de preço máximo (“teto”) necessariamente conduz à perda de bem-estar e ao "
                      "desabastecimento, independente da estrutura de mercado prevalecente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de preço máximo (“teto”) ") + vm("necessariamente") + az(" conduz à perda "
                      "de bem-estar e ao desabastecimento, ") + vm("independente da estrutura de mercado "
                      "prevalecente") + az("."),
        "poucas": ("Em concorrência perfeita, o teto abaixo do equilíbrio gera escassez e peso morto; em "
                   + azb("monopólio") + ", um teto entre o preço de monopólio e o custo marginal " + vd("aumenta")
                   + " a quantidade e reduz o peso morto."),
        "destrinchando": [
            azb("Mercado competitivo") + ": o equilíbrio já é eficiente. Um teto abaixo de p₀ reduz a quantidade "
            "ofertada, cria excesso de demanda (filas, racionamento, mercado paralelo, queda de qualidade) e "
            "gera peso morto. Um teto acima de p₀ é inócuo (não vinculante).",
            azb("Monopólio") + ": a firma iguala RMg = CMg e vende Qm < Qc ao preço Pm > CMg — já existe peso "
            "morto antes de qualquer intervenção. Com um teto Pmáx, a receita marginal passa a ser o próprio "
            "Pmáx até a demanda: vender mais uma unidade não derruba mais o preço das outras.",
            "Se " + vd("CMg < Pmáx < Pm") + ", a firma expande a produção até a demanda (Qmáx > Qm): o preço cai, "
            "a quantidade sobe, não há desabastecimento e o peso morto encolhe. No limite, Pmáx = P no cruzamento "
            "da demanda com o CMg reproduz o resultado competitivo — é a lógica da " + azb("regulação por "
            "preço-teto") + " de monopólios naturais.",
            "Só abaixo do ponto em que a demanda cruza o CMg o teto volta a gerar escassez.",
            vm("Regra-âncora: teto em concorrência perfeita → perda; teto bem calibrado em monopólio → ganho de "
               "eficiência."),
        ],
        "grafico_verso": "ECO-E2-L01212-1-V1",
        "dissecando": (cz("[modulador absoluto]") + " Dois absolutos empilhados — “necessariamente” e "
                       "“independente da estrutura de mercado” — transformam o resultado do caso competitivo em "
                       "lei geral. 🔥 O mesmo item caiu no Simulado Abril/2025 (Nidi/Jacqueline Bueno), também "
                       "com gabarito ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em mercados competitivos, a imposição de preço máximo abaixo do preço de equilíbrio conduz à "
            "escassez e à perda de bem-estar.”</i> → CERTO",
            "<i>“Em monopólio, qualquer preço máximo abaixo do preço de monopólio eleva a quantidade "
            "transacionada.”</i> → ERRADO (modulador absoluto: abaixo do cruzamento da demanda com o CMg a "
            "quantidade volta a cair)",
        ])],
        "reescrita": ("A imposição de preço máximo (“teto”) " + hl("abaixo do equilíbrio, em mercados "
                      "competitivos,") + " conduz à perda de bem-estar e ao desabastecimento" + hl("; em "
                      "monopólio, um teto entre o preço de monopólio e o custo marginal pode elevar a quantidade "
                      "e reduzir o peso morto") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["necessariamente", "independente"], "dificuldade": 2,
        "comentario_fonte": "Em mercado competitivo, o teto gera desabastecimento; em monopólio, pode aumentar a "
                            "quantidade e reduzir o peso morto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 205", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (teto em concorrência perfeita; substituída por ECO-E2-L01212-1-V1, "
                                   "caso do monopólio)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01213
    {
        "id": "ECO-E2-L01213-1", "fonte_ref": "E2-L01213", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_OD,
        "rotulo_item": "Item",
        "assertiva": ("Quando o governo adota uma política de preços mínimos para determinado produto, com vistas "
                      "à garantia de renda e ao estímulo da produção, ao optar pela política de compra, pagará ao "
                      "produtor a diferença entre o preço pago pelo consumidor no mercado e o preço mínimo "
                      "definido."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando o governo adota uma política de preços mínimos para determinado produto, com vistas "
                      "à garantia de renda e ao estímulo da produção, ao optar pela política de compra, pagará ao "
                      "produtor ") + vm("a diferença entre o preço pago pelo consumidor no mercado e") + az(" o "
                      "preço mínimo definido."),
        "poucas": ("Na " + azb("política de compra") + " o governo adquire o excedente pagando o "
                   + vd("preço mínimo cheio") + " por unidade. Pagar só a diferença é a outra modalidade — o "
                   + azb("subsídio") + " (pagamento da diferença)."),
        "destrinchando": [
            "O preço mínimo só tem efeito se fixado <b>acima</b> do equilíbrio: a Pmín, os produtores ofertam Qs e "
            "os consumidores compram Qd < Qs. Sobra o excedente Qs − Qd, e o governo precisa escolher como "
            "sustentar o preço.",
            azb("Compra (aquisição)") + ": o governo entra como demandante e compra o excedente a Pmín. O preço de "
            "mercado fica em Pmín; o gasto público é " + vd("Pmín × (Qs − Qd)") + "; surgem estoques públicos a "
            "administrar.",
            azb("Pagamento da diferença (subsídio)") + ": toda a produção Qs vai ao mercado, cujo preço cai até a "
            "demanda absorvê-la (p < Pmín); o governo paga ao produtor " + vd("Pmín − p") + " por unidade. O "
            "consumidor se beneficia de preço baixo; o gasto público é (Pmín − p) × Qs.",
            "Qual sai mais barato depende das elasticidades: com demanda inelástica, o preço despenca para "
            "absorver Qs, e o pagamento da diferença tende a custar mais que a compra.",
            rx("No Brasil") + ", a " + azb("PGPM") + " (Política de Garantia de Preços Mínimos, operada pela "
            "Conab) combina as duas lógicas: aquisição direta (AGF) e instrumentos de equalização, como prêmios "
            "pagos sobre a diferença.",
        ],
        "grafico_verso": "ECO-E2-L01213-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item descreve corretamente o objetivo da política e "
                       "nomeia a modalidade “compra”, mas cola nela o mecanismo da modalidade “subsídio”. Pista: "
                       "“diferença entre o preço pago pelo consumidor e o preço mínimo” só existe se o consumidor "
                       "paga menos que Pmín — o que não ocorre na compra. 🔥 Item copiado da prova da "
                       "PF/Agente/2009 (CEBRASPE), com o mesmo gabarito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…ao optar pela política de subsídio, pagará ao produtor a diferença entre o preço pago pelo "
            "consumidor no mercado e o preço mínimo definido.”</i> → CERTO",
            "<i>“Na política de compra, o preço pago pelo consumidor fica abaixo do preço mínimo.”</i> → ERRADO "
            "(fica igual a Pmín)",
        ])],
        "reescrita": ("Quando o governo adota uma política de preços mínimos para determinado produto, com vistas à "
                      "garantia de renda e ao estímulo da produção, ao optar pela política de compra, pagará ao "
                      "produtor o preço mínimo definido " + hl("pelas unidades excedentes que adquirir") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Na política de compra, o governo paga ao produtor o preço mínimo, e não a diferença.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 206", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01213-1-V1: compra × pagamento da diferença)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01214
    {
        "id": "ECO-E2-L01214-1", "fonte_ref": "E2-L01214", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_OD,
        "rotulo_item": "Item",
        "assertiva": ("Políticas de controle de preços, aplicadas a um determinado mercado, procuram determinar o "
                      "preço de transação desse mercado, porém não alteram a quantidade transacionada no "
                      "equilíbrio competitivo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Políticas de controle de preços, aplicadas a um determinado mercado, procuram determinar o "
                      "preço de transação desse mercado, porém ") + vm("não alteram") + az(" a quantidade "
                      "transacionada no equilíbrio competitivo."),
        "poucas": ("Um controle de preço que “morde” tira o mercado do equilíbrio: transaciona-se o "
                   + azb("lado curto") + " (a menor entre oferta e demanda), e a quantidade " + vd("cai") + "."),
        "destrinchando": [
            "Fora do equilíbrio, nenhuma das partes pode ser obrigada a transacionar: vale a " + azb("regra do "
            "lado curto") + " — q = mín(Qᴰ, Qˢ).",
            azb("Teto") + " abaixo de p₀: Qˢ cai, Qᴰ sobe; transaciona-se Qˢ < q₀ e sobra escassez (Qᴰ − Qˢ). "
            + azb("Piso") + " acima de p₀: Qᴰ cai, Qˢ sobe; transaciona-se Qᴰ < q₀ (salvo compra pública do "
            "excedente) e sobra produto.",
            "Nos dois casos, a quantidade cai abaixo da competitiva e aparece " + azb("peso morto") + ": deixam "
            "de ocorrer trocas em que o valor para o comprador superava o custo do vendedor.",
            "Exceção: controle <b>não vinculante</b> (teto acima ou piso abaixo do equilíbrio) não muda nada — "
            "mas também não determina o preço, que é o objetivo que o item atribui à política.",
        ],
        "grafico_verso": "ECO-E2-L01214-1-V1",
        "dissecando": (cz("[meia-verdade]") + " A primeira oração (o controle fixa o preço) é correta; o erro "
                       "está no “porém não alteram”, que separa preço e quantidade como se fossem independentes. "
                       "Num mercado, mexer em um sem mexer no outro só é possível com curvas verticais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um preço máximo fixado acima do preço de equilíbrio não altera a quantidade "
            "transacionada.”</i> → CERTO",
            "<i>“Um preço máximo vinculante eleva a quantidade transacionada, pois a quantidade demandada "
            "aumenta.”</i> → ERRADO (vale o lado curto: a oferta cai)",
        ])],
        "reescrita": ("Políticas de controle de preços, aplicadas a um determinado mercado, procuram determinar o "
                      "preço de transação desse mercado, porém " + hl("reduzem") + " a quantidade transacionada "
                      + hl("em relação ao") + " equilíbrio competitivo."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["porém"], "dificuldade": 1,
        "comentario_fonte": "A quantidade ofertada diminui e resulta em escassez do produto.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 207", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01214-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01215
    {
        "id": "ECO-E2-L01215-1", "fonte_ref": "E2-L01215", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NABUCO_OD,
        "rotulo_item": "Item",
        "assertiva": ("Políticas efetivas de fixação do salário nominal mínimo exigem que ele seja fixado acima do "
                      "salário de equilíbrio do mercado de trabalho, porém essa política salarial poderá causar "
                      "desemprego, especialmente no segmento não qualificado do mercado de trabalho."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Políticas <u>efetivas</u> de fixação do salário nominal mínimo exigem que ele seja fixado "
                      "<u>acima</u> do salário de equilíbrio do mercado de trabalho, porém essa política salarial "
                      "<u>poderá</u> causar desemprego, especialmente no segmento não qualificado do mercado de "
                      "trabalho."),
        "poucas": ("O salário mínimo é um " + azb("preço mínimo") + " no mercado de trabalho: só tem efeito "
                   "acima de w₀ e, no modelo competitivo, gera excesso de oferta de trabalho — "
                   + vd("desemprego = L₂ − L₁") + "."),
        "destrinchando": [
            "Piso abaixo do salário de equilíbrio é " + azb("não vinculante") + ": o mercado já paga mais que "
            "ele. Por isso “efetiva” exige wmín > w₀.",
            "Acima de w₀, as empresas contratam só L₁ (demanda por trabalho) e os trabalhadores ofertam L₂: o "
            "excedente L₂ − L₁ é desemprego involuntário. É o mesmo mecanismo do preço mínimo de um bem.",
            "O efeito se concentra nos " + azb("não qualificados") + ": é para eles que o mínimo fica mais acima "
            "do salário de mercado (produtividade marginal baixa). Para trabalhadores qualificados, o piso não "
            "vincula.",
            "O “poderá” é decisivo: a evidência empírica é controversa. " + oc("Card e Krueger") + " (1994) não "
            "encontraram perda de emprego após alta do mínimo em Nova Jersey, e em mercados com "
            + azb("monopsônio") + " um piso moderado pode até <b>aumentar</b> o emprego.",
            rx("No Brasil") + ", a política de valorização do salário mínimo (INPC + crescimento do PIB de dois "
            "anos antes, com o ganho real limitado desde 2025 pelos parâmetros do arcabouço fiscal; ⏳ (out/2026)) "
            "é discutida justamente nesses termos: renda da base × informalidade e emprego formal.",
        ],
        "grafico_verso": "ECO-E2-L01215-1-V1",
        "dissecando": (cz("[modulador relativo]") + " Item salvo pelo “poderá”: afirma uma possibilidade "
                       "compatível com o modelo competitivo sem negar a controvérsia empírica. Se a banca "
                       "trocasse por “necessariamente causará”, o item ficaria ERRADO pelo caso do "
                       "monopsônio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O salário mínimo fixado abaixo do salário de equilíbrio gera desemprego no segmento não "
            "qualificado.”</i> → ERRADO (piso abaixo do equilíbrio não vincula)",
            "<i>“Em qualquer estrutura de mercado de trabalho, a elevação do salário mínimo reduz o "
            "emprego.”</i> → ERRADO (modulador absoluto: no monopsônio pode aumentá-lo)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["poderá", "especialmente"], "dificuldade": 1,
        "comentario_fonte": "Com salário mínimo acima de w0, as empresas pagam ao menos wmín; desemprego de "
                            "L2 − L1.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 208", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01215-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01389
    {
        "id": "ECO-E2-L01389-1", "fonte_ref": "E2-L01389", "destino": "03", "subtema": H2["trib"],
        "tipo": "EXERC", "banca": "Intensivo MM", "prova": "Intensivo Pré-TPS/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": "Responda à questão a seguir, sobre os efeitos de um imposto sobre o bem-estar.",
        "rotulo_item": "Questão",
        "assertiva": ("Indique graficamente onde identificar o que é excedente e o que é peso morto após a "
                      "imposição de um imposto."),
        "gabarito": "RESPOSTA", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("Com o imposto t, o preço pago pelo comprador sobe para pc e o recebido pelo vendedor cai "
                      "para pv; a quantidade cai de q₀ para qₜ. Excedente do consumidor: área entre a demanda e "
                      "pc. Excedente do produtor: área entre pv e a oferta. Receita do governo: retângulo t × qₜ. "
                      "Peso morto: triângulo entre as curvas, de qₜ a q₀."),
        "poucas": ("O imposto abre uma " + azb("cunha") + " entre pc e pv; parte dos antigos excedentes vira "
                   "receita do governo (retângulo) e parte se perde sem ir para ninguém (" + azb("peso morto")
                   + ", triângulo)."),
        "destrinchando": [
            "Antes do imposto: equilíbrio (q₀, p₀); EC = área entre a demanda e p₀; EP = área entre p₀ e a "
            "oferta. A soma é o excedente total, máximo no equilíbrio competitivo.",
            "Imposto específico t (cobrado do vendedor ou do comprador — o resultado econômico é o mesmo): a "
            "oferta relevante vira O + t. Novo equilíbrio em qₜ, com " + vd("pc − pv = t") + ".",
            "Repartição do bolo: o EC encolhe para o triângulo acima de pc; o EP, para o triângulo abaixo de pv; "
            "o retângulo " + vd("t × qₜ") + " é a " + azb("receita tributária") + " (transferência ao governo, "
            "não perda); o triângulo entre qₜ e q₀ é o " + azb("peso morto") + ": trocas mutuamente vantajosas "
            "que deixaram de existir.",
            "Tamanho do peso morto ≈ ½ · t · (q₀ − qₜ): cresce com as elasticidades e com o <b>quadrado</b> da "
            "alíquota — dobrar t quase quadruplica a perda.",
            "Quem paga mais: o lado <b>menos elástico</b>. Demanda inelástica → pc sobe quase t inteiro.",
        ],
        "grafico_verso": "ECO-E2-L01389-1-V1",
        "dissecando": (cz("[exercício aberto]") + " Em C/E, a banca transforma esse gráfico em itens como “a "
                       "receita arrecadada corresponde à perda dos consumidores” (ERRADO: só a parte do "
                       "retângulo acima de p₀) ou “a incidência depende de quem recolhe o imposto” (ERRADO: "
                       "depende das elasticidades)."),
        "modulos": [("🃏 Carta na manga", ["Tributo eficiente é o que incide sobre bases inelásticas (regra de "
                                           + oc("Ramsey") + "), mas isso conflita com equidade: bens "
                                           "inelásticos costumam pesar mais no orçamento dos mais pobres."])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso composto só de quatro imagens (receita tributária e peso morto), sem texto.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 281", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "cortada (a frente pede o gráfico: ele vai para o verso)"},
                          {"ref": "IMAGEM 282-285", "tipo_fonte": "GRÁFICO/DIAGRAMA", "lado": "verso",
                           "acao": "redesenhadas e fundidas em ECO-E2-L01389-1-V1"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01392
    {
        "id": "ECO-E2-L01392-1", "fonte_ref": "E2-L01392", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "FCC", "prova": "CLDF/Consultor Legislativo/2018", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Acerca das políticas de preços mínimos, julgue o item a seguir (item adaptado).",
        "rotulo_item": "Item",
        "assertiva": ("A política de preços mínimos compulsórios tem por objetivo ajustar a relação de oferta e "
                      "demanda, eliminando o excesso de oferta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A política de preços mínimos compulsórios tem por objetivo ") + vm("ajustar a relação de "
                      "oferta e demanda, eliminando o excesso de oferta") + az("."),
        "poucas": ("O preço mínimo visa " + azb("garantir renda ao produtor") + ", com preço acima do "
                   "equilíbrio — e, por isso mesmo, " + vd("cria") + " excesso de oferta, em vez de eliminá-lo."),
        "destrinchando": [
            "Quem ajusta oferta e demanda e elimina excessos é o próprio " + azb("mecanismo de preços") + ": "
            "excesso de oferta derruba o preço até o equilíbrio. Uma intervenção só é necessária quando o "
            "governo quer um resultado <b>diferente</b> do de mercado.",
            "O " + azb("preço mínimo") + " (piso) só é efetivo se fixado acima de p₀. Nesse caso, Qˢ > Qᴰ: o piso "
            + vd("gera") + " excedente de produto. Para sustentá-lo, o governo compra o excedente, paga a "
            "diferença ao produtor ou restringe a produção.",
            "Objetivos típicos: estabilizar e garantir a renda do produtor (sobretudo agrícola, sujeito a "
            "choques de safra), estimular a produção e formar estoques reguladores. Exemplos no mercado de "
            "trabalho: o salário mínimo.",
            "Custos: gasto público, estoques a administrar, preço mais alto para o consumidor e peso morto. "
            + rx("No Brasil") + ", o instrumento é a " + azb("PGPM") + " (Política de Garantia de Preços "
            "Mínimos), operada pela Conab.",
            vm("Regra-âncora: piso acima do equilíbrio → excesso de oferta; teto abaixo → excesso de demanda."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item atribui ao preço mínimo o efeito oposto "
                       "ao que ele produz: em vez de eliminar o excesso de oferta, ele o cria. A linguagem "
                       "neutra (“ajustar a relação de oferta e demanda”) descreve o mercado livre, não a "
                       "intervenção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política de preços mínimos, quando o preço é fixado acima do equilíbrio, gera excesso de "
            "oferta que precisa ser absorvido pelo governo ou pelo mercado.”</i> → CERTO",
            "<i>“O preço mínimo fixado abaixo do preço de equilíbrio gera excesso de oferta.”</i> → ERRADO "
            "(abaixo do equilíbrio o piso não vincula)",
        ])],
        "reescrita": ("A política de preços mínimos compulsórios tem por objetivo " + hl("garantir renda ao "
                      "produtor, fixando preço acima do equilíbrio, o que gera") + " excesso de oferta."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O objetivo é beneficiar o produtor, com preço geralmente acima do equilíbrio.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01393
    {
        "id": "ECO-E2-L01393-1", "fonte_ref": "E2-L01393", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "PF/Agente/2009", "ano": 2009, "cacd": False,
        "errei": False,
        "comando": "Acerca das políticas de intervenção do governo nos mercados, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Quando o governo adota uma política de preços mínimos para determinado produto, com vistas "
                      "à garantia de renda e ao estímulo da produção, ao optar pela política de compra, pagará ao "
                      "produtor a diferença entre o preço pago pelo consumidor no mercado e o preço mínimo "
                      "definido."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando o governo adota uma política de preços mínimos para determinado produto, com vistas "
                      "à garantia de renda e ao estímulo da produção, ao optar pela política de compra, pagará ao "
                      "produtor ") + vm("a diferença entre o preço pago pelo consumidor no mercado e") + az(" o "
                      "preço mínimo definido."),
        "poucas": ("No " + azb("programa de compras") + ", o governo vira comprador e adquire o excedente "
                   "pagando o " + vd("preço mínimo") + ". Pagar a diferença entre o preço de mercado e o mínimo "
                   "é a política de " + azb("subsídio") + "."),
        "destrinchando": [
            "Preço mínimo acima do equilíbrio gera Qˢ > Qᴰ. Duas formas clássicas de sustentá-lo:",
            azb("Compra") + ": o governo adquire o excedente (Qˢ − Qᴰ) a Pmín. O preço de mercado fica em Pmín "
            "para todos; o consumidor compra menos e paga mais; o governo gasta " + vd("Pmín × (Qˢ − Qᴰ)")
            + " e acumula estoques.",
            azb("Subsídio (pagamento da diferença)") + ": o governo deixa o mercado absorver toda a produção, o "
            "preço cai para p < Pmín, e paga ao produtor " + vd("Pmín − p") + " por unidade vendida. O "
            "consumidor sai ganhando; o gasto é (Pmín − p) × Qˢ.",
            "Nos dois casos o produtor recebe Pmín por unidade e produz Qˢ — a diferença está em quem consome o "
            "produto (governo × consumidor) e em quanto custa ao Tesouro, o que depende da elasticidade da "
            "demanda.",
            rx("No Brasil") + ", a PGPM, operada pela Conab, usa a aquisição direta (AGF) e prêmios que cobrem a "
            "diferença de preço — as duas lógicas.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Fabricação por empréstimo: o mecanismo correto do subsídio "
                       "foi colado no rótulo “compra”. Pista lógica: na compra, o consumidor paga Pmín, então a "
                       "“diferença entre o preço pago pelo consumidor e o preço mínimo” seria zero. 🔥 O item foi "
                       "reaproveitado, com o mesmo texto e gabarito, no Pré-TPS/2023 da Nabuco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na política de compra, o governo adquire o excedente de produção ao preço mínimo, tornando-se "
            "demandante do bem.”</i> → CERTO",
            "<i>“A política de subsídio eleva o preço pago pelo consumidor ao nível do preço mínimo.”</i> → "
            "ERRADO (no subsídio o consumidor paga menos que Pmín)",
        ])],
        "reescrita": ("Quando o governo adota uma política de preços mínimos para determinado produto, com vistas à "
                      "garantia de renda e ao estímulo da produção, ao optar pela política de " + hl("subsídio")
                      + ", pagará ao produtor a diferença entre o preço pago pelo consumidor no mercado e o preço "
                      "mínimo definido."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "No programa de compras, o governo adquire o excedente ao preço mínimo, tornando-se "
                            "demandante; a política descrita no item é a de subsídios.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01394
    {
        "id": "ECO-E2-L01394-1", "fonte_ref": "E2-L01394", "destino": "03", "subtema": H2["exc"],
        "tipo": "DISC", "banca": "Intensivo MM", "prova": "Intensivo Pré-TPS/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": "Explique a diferença entre os dois conceitos indicados a seguir.",
        "rotulo_item": "Questão",
        "assertiva": "Excedente do produtor vs excedente do consumidor.",
        "gabarito": "RESPOSTA", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("Excedente do consumidor: diferença entre o que o consumidor estaria disposto a pagar e o "
                      "que efetivamente paga, somada sobre as unidades compradas — área entre a curva de demanda "
                      "e o preço. Excedente do produtor: diferença entre o preço recebido e o custo marginal (o "
                      "mínimo que o vendedor aceitaria), somada sobre as unidades vendidas — área entre o preço e "
                      "a curva de oferta. A soma é o excedente total, máximo no equilíbrio competitivo."),
        "poucas": ("EC mede o ganho de quem " + azb("compra") + " (disposição a pagar − preço); EP, o ganho de "
                   "quem " + azb("vende") + " (preço − custo marginal). Um fica acima do preço, o outro abaixo."),
        "destrinchando": [
            azb("Excedente do consumidor") + ": cada ponto da demanda é a disposição a pagar marginal (o "
            "“preço de reserva” daquela unidade). Exemplo: três consumidores valorizam o bem em 10, 7 e 5; com "
            "preço 5, os dois primeiros ganham 10 − 5 = 5 e 7 − 5 = 2; o terceiro é indiferente. "
            + vd("EC = 7") + ".",
            azb("Excedente do produtor") + ": cada ponto da oferta competitiva é o custo marginal daquela unidade "
            "— o preço mínimo que o vendedor aceitaria. EP = Σ (p − CMg). No curto prazo, equivale a "
            + vd("receita total − custo variável") + " (= lucro + custo fixo), não ao lucro.",
            "Preço sobe → EP cresce e EC encolhe (parte é transferência de um para o outro). Preço cai → o "
            "contrário. Intervenções (impostos, tetos, pisos, tarifas) criam ainda o " + azb("peso morto")
            + ": excedente que some sem ir para ninguém.",
            vm("Regra-âncora: EC = área entre a demanda e o preço; EP = área entre o preço e a oferta; o "
               "equilíbrio competitivo maximiza EC + EP."),
        ],
        "grafico_verso": "ECO-E2-L01394-1-V1",
        "dissecando": (cz("[exercício aberto]") + " Em C/E, a banca costuma testar: EC definido como “diferença "
                       "entre o que o consumidor está disposto a pagar e o que paga” (CERTO), EP medido pelo "
                       "lucro (ERRADO no curto prazo) e queda de preço aumentando o EP (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O excedente do produtor corresponde à área abaixo da curva de oferta e acima do eixo das "
            "quantidades.”</i> → ERRADO (essa área é o custo variável; o EP fica entre o preço e a oferta)",
            "<i>“No equilíbrio competitivo, a soma dos excedentes do consumidor e do produtor é máxima.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso só com imagem: exemplo numérico com consumidores que valorizam o bem em 10, "
                            "7 e 5, preço 5 e excedente total do consumidor de 7.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 289", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (exemplo numérico no 📖; gráfico substituído por "
                                   "ECO-E2-L01394-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01401
    {
        "id": "ECO-E2-L01401-1", "fonte_ref": "E2-L01401", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "FCC", "prova": "TCE/PR/Analista de Controle/2011", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": "Acerca da incidência de impostos sobre vendas, julgue o item a seguir (item adaptado).",
        "rotulo_item": "Item",
        "assertiva": ("A instituição de um imposto sobre vendas implicará aumento do preço de mercado exatamente "
                      "igual ao valor do imposto, qualquer que seja a elasticidade-preço da demanda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A instituição de um imposto sobre vendas implicará aumento do preço de mercado ")
                   + vm("exatamente igual ao valor do imposto, qualquer que seja") + az(" a elasticidade-preço "
                   "da demanda."),
        "poucas": ("O repasse ao preço depende das " + azb("elasticidades") + ": em regra o preço ao consumidor "
                   "sobe " + vd("menos") + " que o imposto. Repasse integral só com demanda perfeitamente "
                   "inelástica ou oferta perfeitamente elástica."),
        "destrinchando": [
            "Com o imposto, abre-se a cunha pc − pv = t. A alta de pc é a parcela do consumidor: "
            + vd("Δpc = t · ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|)") + ". Só é igual a t se "
            "|ε<sub>D</sub>| = 0 ou ε<sub>O</sub> → ∞.",
            "Casos: demanda " + azb("perfeitamente inelástica") + " (vertical) → pc sobe t inteiro, quantidade "
            "não muda; demanda " + azb("infinitamente elástica") + " (horizontal) → pc não sobe nada, o "
            "vendedor absorve tudo; casos intermediários → o imposto se reparte.",
            "Por isso a frase “o imposto indireto é repassado ao consumidor” é uma " + azb("presunção "
            "jurídica") + " (contribuinte de fato × de direito), não um resultado econômico: a "
            "<b>incidência econômica</b> é decidida pelas elasticidades.",
            vm("Regra-âncora: repasse integral é exceção (curva vertical de demanda ou horizontal de oferta), "
               "não regra."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " Dois absolutos — “exatamente igual” e “qualquer que seja "
                       "a elasticidade” — transformam um caso-limite em regra. O caso-limite existe (demanda "
                       "vertical), e é justamente a exceção que o “qualquer que seja” ignora."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a demanda for perfeitamente inelástica, o preço de mercado aumentará exatamente no valor do "
            "imposto.”</i> → CERTO",
            "<i>“Quanto mais inelástica a demanda, menor a parcela do imposto repassada ao preço.”</i> → ERRADO "
            "(inversão: maior)",
        ])],
        "reescrita": ("A instituição de um imposto sobre vendas implicará aumento do preço de mercado "
                      + hl("que depende das elasticidades-preço da demanda e da oferta, sendo igual ao valor do "
                        "imposto apenas se a demanda for perfeitamente inelástica ou a oferta perfeitamente "
                        "elástica") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["exatamente", "qualquer que seja"], "dificuldade": 1,
        "comentario_fonte": "Verso com gráfico de peso morto e observação de que, com demanda totalmente "
                            "inelástica, o consumidor arca com todo o imposto (exceção à regra geral).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 308", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"},
                          {"ref": "IMAGEM 309", "tipo_fonte": "DECORATIVA", "lado": "verso",
                           "acao": "cortada"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00008
    {
        "id": "ECO-E3-L00008-1", "fonte_ref": "E3-L00008", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": "Acerca dos conceitos fundamentais de microeconomia, julgue o item que se segue.",
        "rotulo_item": "Item",
        "assertiva": ("A intervenção governamental por meio de controle de preços corrige falhas de mercado e tem "
                      "impacto positivo no bem-estar de consumidores e produtores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A intervenção governamental por meio de controle de preços ") + vm("corrige falhas de "
                      "mercado") + az(" e ") + vm("tem impacto positivo no bem-estar de consumidores e produtores")
                   + az("."),
        "poucas": ("Controle de preços, em regra, " + azb("cria distorções") + " em vez de corrigir falhas: teto "
                   "gera escassez, piso gera excedente, e o bem-estar total cai — no máximo, um lado ganha à "
                   "custa do outro."),
        "destrinchando": [
            azb("Falhas de mercado") + " são externalidades, bens públicos, assimetria de informação e poder de "
            "mercado. Os remédios típicos são outros: tributo pigouviano ou mercado de licenças "
            "(externalidade), provisão pública (bem público), regulação de informação, defesa da concorrência.",
            azb("Teto") + " abaixo do equilíbrio: escassez, filas, mercado paralelo, queda de qualidade. "
            + azb("Piso") + " acima: excedente, estoques, desemprego (salário mínimo). Em mercado competitivo, "
            "ambos geram " + vd("peso morto") + ".",
            "Efeito distributivo: o teto pode beneficiar os consumidores que conseguem comprar (transferência de "
            "EP para EC), mas prejudica produtores e quem fica sem o bem; o piso faz o inverso. Melhorar "
            "<b>os dois lados ao mesmo tempo</b> é impossível partindo de um equilíbrio eficiente.",
            "Exceção relevante: em " + azb("monopólio") + " (inclusive o natural), um teto calibrado entre o "
            "preço de monopólio e o custo marginal aumenta a quantidade e reduz o peso morto — aí o controle de "
            "preço corrige a falha de poder de mercado. Mesmo nesse caso, o monopolista perde excedente.",
            vm("Regra-âncora: controle de preço em mercado competitivo = transferência + peso morto, nunca "
               "ganho para todos."),
        ],
        "dissecando": (cz("[juízo indevido · modulador absoluto]") + " O item atribui ao instrumento uma "
                       "virtude genérica (“corrige falhas”) e um efeito impossível (melhora para consumidores "
                       "<b>e</b> produtores). A pista é o “e”: qualquer controle de preço transfere excedente de "
                       "um lado para o outro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O tabelamento de preços abaixo do equilíbrio, em mercado competitivo, tende a gerar escassez e "
            "mercados paralelos.”</i> → CERTO",
            "<i>“A regulação do preço de um monopólio natural nunca pode elevar o bem-estar social.”</i> → ERRADO "
            "(modulador absoluto: o teto bem calibrado reduz o peso morto)",
        ])],
        "reescrita": ("A intervenção governamental por meio de controle de preços " + hl("em regra não corrige")
                      + " falhas de mercado e " + hl("tende a reduzir o bem-estar total, beneficiando um dos "
                      "lados à custa do outro") + "."),
        "tipo_erro": ["JUIZO_INDEVIDO", "GENERALIZACAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Seis respostas de IA concordantes: controle de preços cria distorções (escassez ou "
                            "excedente), perda de eficiência e efeitos distributivos; exceção teórica no monopólio "
                            "natural.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00017
    {
        "id": "ECO-E3-L00017-1", "fonte_ref": "E3-L00017", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("Em relação à teoria da produção, ao equilíbrio da firma e à economia do bem-estar, julgue o "
                    "item subsecutivo."),
        "rotulo_item": "Item",
        "assertiva": ("O resultado do equilíbrio competitivo resulta em uma alocação pareto-eficiente, que "
                      "pressupõe a equidade na distribuição dos bens produzidos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O resultado do equilíbrio competitivo resulta em uma alocação pareto-eficiente, que ")
                   + vm("pressupõe a equidade") + az(" na distribuição dos bens produzidos."),
        "poucas": ("O equilíbrio competitivo é " + azb("Pareto-eficiente") + " (1º teorema do bem-estar), mas "
                   "eficiência " + vd("não implica equidade") + ": uma alocação pode ser eficiente e muito "
                   "desigual."),
        "destrinchando": [
            azb("Eficiência de Pareto") + ": não é possível melhorar alguém sem piorar outro. É um critério "
            "sobre o “tamanho do bolo”, não sobre a sua divisão — dar tudo a uma só pessoa também é "
            "Pareto-eficiente.",
            azb("1º Teorema Fundamental do Bem-Estar") + ": sob concorrência perfeita, mercados completos e "
            "ausência de externalidades, todo equilíbrio competitivo é Pareto-eficiente. O resultado depende da "
            "dotação inicial: dotações desiguais geram equilíbrios eficientes e desiguais.",
            azb("2º Teorema") + ": qualquer alocação eficiente pode ser alcançada como equilíbrio competitivo, "
            "desde que se redistribuam as dotações iniciais (por transferências lump-sum). É a separação "
            "clássica: o mercado cuida da eficiência; a " + azb("função distributiva") + " do Estado, da "
            "equidade.",
            "Na prática, a redistribuição usa impostos distorcivos, e surge o dilema eficiência × equidade "
            "(" + oc("Arthur Okun") + ", <i>Equality and Efficiency: The Big Tradeoff</i>, 1975).",
            vm("Regra-âncora: Pareto mede eficiência, não justiça distributiva."),
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A primeira parte reproduz o 1º teorema "
                       "(correta); o erro está na oração adjetiva, que amarra à eficiência um pressuposto que ela "
                       "não tem. 🔥 CEBRASPE gosta de colar “justo”, “equitativo” ou “igualitário” em definições "
                       "de eficiência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma alocação pareto-eficiente pode ser altamente desigual.”</i> → CERTO",
            "<i>“Pelo segundo teorema do bem-estar, toda alocação eficiente é equitativa.”</i> → ERRADO (troca "
            "de conceito: o teorema trata de alcançar qualquer alocação eficiente via redistribuição de "
            "dotações)",
        ])],
        "reescrita": ("O resultado do equilíbrio competitivo resulta em uma alocação pareto-eficiente, que "
                      + hl("não pressupõe") + " a equidade na distribuição dos bens produzidos."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Seis respostas de IA concordantes: eficiência de Pareto e equidade são conceitos "
                            "distintos; uma alocação eficiente pode ser profundamente desigual.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00195
    {
        "id": "ECO-E3-L00195-1", "fonte_ref": "E3-L00195", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento no imposto sobre o consumo de um bem com demanda perfeitamente preço-elástica e "
                      "oferta preço-inelástica terá incidência apenas sobre o bem-estar dos produtores, pois os "
                      "consumidores somente adquirem o bem a um preço único de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento no imposto sobre o consumo de um bem com demanda <u>perfeitamente "
                      "preço-elástica</u> e oferta preço-inelástica terá incidência <u>apenas</u> sobre o "
                      "bem-estar dos produtores, pois os consumidores somente adquirem o bem a um preço único de "
                      "equilíbrio."),
        "poucas": ("Demanda perfeitamente elástica (horizontal): o consumidor não aceita preço acima do vigente, "
                   "então o imposto não chega ao preço final — o " + vd("produtor absorve tudo") + "."),
        "destrinchando": [
            "Demanda " + azb("perfeitamente elástica") + " = horizontal no preço p*. Qualquer centavo acima e a "
            "quantidade demandada vai a zero; o preço pago pelo consumidor fica fixo (o “preço único” do item).",
            "Com o imposto, a cunha pc − pv = t sai inteira do lado do vendedor: " + vd("pc = p*") + " e "
            + vd("pv = p* − t") + ". Pela fórmula, a parcela do consumidor é ε<sub>O</sub> / (ε<sub>O</sub> + "
            "|ε<sub>D</sub>|) → 0.",
            "A oferta inelástica reforça o resultado: os produtores não conseguem reduzir muito a produção, a "
            "quantidade cai pouco e quase toda a perda vira receita do governo, com peso morto pequeno. Com a "
            "demanda horizontal, porém, a incidência sobre o produtor seria total mesmo com oferta elástica — "
            "nesse caso a quantidade cairia mais.",
            "Bem-estar: o excedente do consumidor não muda (com demanda horizontal ele já é nulo); o do produtor "
            "encolhe pela receita arrecadada mais o peso morto.",
            vm("Regra-âncora: curva horizontal de um lado → esse lado não paga nada do imposto."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item construído sobre um caso-limite. O “apenas” "
                       "assusta quem associa absolutos a ERRADO, mas aqui é exato: demanda perfeitamente elástica "
                       "torna a incidência sobre o consumidor nula. 🔥 A banca combina extremos (horizontal, "
                       "vertical) com o modulador absoluto para testar se o candidato sabe quando ele é "
                       "legítimo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com demanda perfeitamente preço-inelástica e oferta preço-elástica terá incidência apenas sobre "
            "o bem-estar dos produtores…”</i> → ERRADO (inversão: recairia só sobre os consumidores)",
            "<i>“Com demanda perfeitamente elástica, o imposto não altera a quantidade transacionada.”</i> → "
            "ERRADO (a quantidade cai, salvo oferta perfeitamente inelástica)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas", "somente"], "dificuldade": 1,
        "comentario_fonte": "Demanda horizontal: o consumidor não aceita pagar acima do preço; o imposto não é "
                            "repassado e o preço recebido pelo produtor cai no valor integral do imposto. "
                            "Anotações com as condições da cunha e gráficos de incidência.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 245", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (condições da cunha no 📖)"},
                          {"ref": "IMAGEM 246-249", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (gráficos de incidência; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00196
    {
        "id": "ECO-E3-L00196-1", "fonte_ref": "E3-L00196", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento no imposto sobre o consumo de um bem cuja demanda e oferta tenham elasticidades "
                      "unitárias incidirá apenas sobre o bem-estar do consumidor, pois as firmas conseguem "
                      "repassar o tributo totalmente no novo preço de equilíbrio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento no imposto sobre o consumo de um bem cuja demanda e oferta tenham elasticidades "
                      "unitárias incidirá ") + vm("apenas sobre o bem-estar do consumidor") + az(", pois as "
                      "firmas ") + vm("conseguem repassar o tributo totalmente") + az(" no novo preço de "
                      "equilíbrio."),
        "poucas": ("Elasticidades iguais (|ε<sub>D</sub>| = ε<sub>O</sub> = 1) → o ônus se " + vd("reparte ao "
                   "meio") + " entre consumidores e produtores. Repasse total exigiria demanda vertical ou "
                   "oferta horizontal."),
        "destrinchando": [
            "Parcela do consumidor = ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|) = 1 / (1 + 1) = "
            + vd("½") + ". O preço ao consumidor sobe metade do imposto; o preço líquido do produtor cai a outra "
            "metade (para variações pequenas, em torno do equilíbrio).",
            "A regra geral: " + azb("o lado mais inelástico paga mais") + ". Elasticidades iguais = nenhum lado "
            "“foge” mais que o outro = divisão equilibrada.",
            "Repasse integral ao consumidor só em dois extremos: " + azb("demanda perfeitamente inelástica")
            + " (vertical) ou " + azb("oferta perfeitamente elástica") + " (horizontal).",
            "Atenção: elasticidade <b>unitária</b> (|ε| = 1) não tem nada a ver com repasse integral; o que ela "
            "tem de especial é a receita (p × q) ficar constante quando o preço varia ao longo da demanda.",
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " O item usa elasticidades simétricas e "
                       "conclui por uma incidência assimétrica e total. Pista: se nada distingue os dois lados, "
                       "nada justifica que um pague tudo. O “apenas” e o “totalmente” só seriam válidos nos "
                       "casos-limite."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se demanda e oferta tiverem a mesma elasticidade-preço, em módulo, o ônus do imposto se "
            "dividirá igualmente entre consumidores e produtores.”</i> → CERTO",
            "<i>“Com oferta perfeitamente elástica, as firmas repassam o tributo totalmente ao preço.”</i> → "
            "CERTO",
        ])],
        "reescrita": ("Um aumento no imposto sobre o consumo de um bem cuja demanda e oferta tenham elasticidades "
                      "unitárias incidirá " + hl("igualmente sobre o bem-estar do consumidor e o das firmas")
                      + ", pois " + hl("cada lado arca com metade do tributo") + " no novo preço de "
                      "equilíbrio."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["apenas", "totalmente"],
        "dificuldade": 1,
        "comentario_fonte": "Com elasticidades iguais, o ônus é repartido; repasse total só com demanda "
                            "perfeitamente inelástica ou oferta perfeitamente elástica. Gráfico com divisão "
                            "50%-50%.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 250", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"},
                          {"ref": "IMAGEM 251-252", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvidas (divisão 50%-50% no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00197
    {
        "id": "ECO-E3-L00197-1", "fonte_ref": "E3-L00197", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Um imposto sobre o consumo de produtos viciantes tem redução pequena no bem-estar dos "
                      "consumidores, uma vez que a demanda desses produtos é altamente elástica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um imposto sobre o consumo de produtos viciantes tem redução ") + vm("pequena")
                   + az(" no bem-estar dos consumidores, uma vez que a demanda desses produtos é altamente ")
                   + vm("elástica") + az("."),
        "poucas": ("Produtos viciantes têm demanda " + azb("inelástica") + ": o consumidor continua comprando "
                   "quase o mesmo e paga quase todo o imposto — a perda de bem-estar dele é " + vd("grande")
                   + "."),
        "destrinchando": [
            "Determinantes da elasticidade-preço da demanda: disponibilidade de substitutos, essencialidade ou "
            + azb("dependência") + ", peso no orçamento e horizonte de tempo. Cigarro, álcool e drogas têm "
            "dependência e poucos substitutos → demanda inelástica.",
            "Incidência: o lado mais inelástico arca com a maior parte do imposto. Aqui, o preço ao consumidor "
            "sobe quase o valor de t, e a quantidade cai pouco: a perda de excedente do consumidor ≈ (Δpc) × q é "
            + vd("grande") + ".",
            "Por que esses bens são tributados pesadamente (" + azb("impostos seletivos") + ", “sin taxes”): "
            "arrecadam muito com peso morto pequeno (a quantidade cai pouco) e ainda desestimulam um consumo com "
            "externalidades negativas. O efeito sobre o consumo é maior no longo prazo, quando a demanda fica "
            "mais elástica.",
            rx("No Brasil") + ", a reforma tributária do consumo (EC 132/2023) criou o " + azb("Imposto "
            "Seletivo") + ", que incide sobre bens prejudiciais à saúde ou ao meio ambiente, como fumo e "
            "bebidas alcoólicas.",
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Dois erros encadeados: classifica a "
                       "demanda como elástica (é inelástica) e, a partir disso, conclui pela perda pequena. A "
                       "pista é “viciantes”: vício é o exemplo de manual de inelasticidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto sobre produtos viciantes recai majoritariamente sobre os consumidores, cuja demanda "
            "é inelástica.”</i> → CERTO",
            "<i>“Por ser inelástica a demanda de cigarros, o imposto sobre eles gera grande peso morto.”</i> → "
            "ERRADO (demanda inelástica → peso morto pequeno)",
        ])],
        "reescrita": ("Um imposto sobre o consumo de produtos viciantes tem redução " + hl("grande") + " no "
                      "bem-estar dos consumidores, uma vez que a demanda desses produtos é altamente "
                      + hl("inelástica") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["altamente"], "dificuldade": 1,
        "comentario_fonte": "A demanda por produtos viciantes é inelástica e a redução de bem-estar do "
                            "consumidor é grande: ele continua comprando quase o mesmo, a preço maior.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 253", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"},
                          {"ref": "IMAGEM 254", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00198
    {
        "id": "ECO-E3-L00198-1", "fonte_ref": "E3-L00198", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Uma redução no imposto sobre o consumo de um bem com demanda preço-inelástica e oferta "
                      "preço-elástica terá incidência maior sobre o bem-estar dos consumidores do que sobre o "
                      "bem-estar das firmas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma <u>redução</u> no imposto sobre o consumo de um bem com demanda <u>preço-inelástica</u> "
                      "e oferta preço-elástica terá incidência maior sobre o bem-estar dos <u>consumidores</u> do "
                      "que sobre o bem-estar das firmas."),
        "poucas": ("A regra da incidência vale nos dois sentidos: o lado " + azb("mais inelástico") + " paga a "
                   "maior parte de um aumento e " + vd("captura a maior parte de uma redução") + ". Aqui, os "
                   "consumidores."),
        "destrinchando": [
            "A cunha pc − pv encolhe com a redução do imposto. Como a demanda é inelástica e a oferta elástica, "
            "o ajuste se dá quase todo em pc: o " + vd("preço ao consumidor cai quase o valor da redução")
            + ", e o preço líquido do produtor quase não muda.",
            "Parcela do consumidor = ε<sub>O</sub> / (ε<sub>O</sub> + |ε<sub>D</sub>|): com ε<sub>O</sub> "
            "grande e |ε<sub>D</sub>| pequeno, fica próxima de 1.",
            "Implicação de política: desonerações de bens com oferta elástica (produção facilmente expansível) "
            "tendem a chegar ao consumidor; com oferta inelástica, a desoneração fica com os produtores (vira "
            "margem).",
            rx("No Brasil") + ", o debate sobre repasse de desonerações (cesta básica, combustíveis) gira "
            "exatamente em torno disso: o repasse ao preço depende das elasticidades, não da intenção da lei.",
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " A palavra “incidência” costuma vir associada a "
                       "ônus; aqui ela se aplica a um <b>benefício</b> (redução de imposto). Quem não percebe "
                       "a simetria da regra hesita. Pista: demanda inelástica + oferta elástica = consumidor "
                       "no centro do ajuste, para cima ou para baixo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução de imposto sobre um bem com oferta inelástica e demanda elástica beneficiará "
            "sobretudo os produtores.”</i> → CERTO",
            "<i>“Uma redução de imposto sempre se transmite integralmente ao preço pago pelo consumidor.”</i> → "
            "ERRADO (modulador absoluto: depende das elasticidades)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["maior"], "dificuldade": 2,
        "comentario_fonte": "A parte mais inelástica arca com a maior parte do ônus num aumento e se apropria da "
                            "maior parte do benefício numa redução; os consumidores capturam a redução via queda "
                            "de preços.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 255-256", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00199
    {
        "id": "ECO-E3-L00199-1", "fonte_ref": "E3-L00199", "destino": "03", "subtema": H2["teto"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_INTERV,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de preço máximo necessariamente conduz à perda de bem-estar e ao "
                      "desabastecimento, independente da estrutura de mercado prevalecente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de preço máximo ") + vm("necessariamente") + az(" conduz à perda de "
                      "bem-estar e ao desabastecimento, ") + vm("independente da estrutura de mercado "
                      "prevalecente") + az("."),
        "poucas": ("O resultado depende do nível do teto e da estrutura de mercado: em " + azb("monopólio")
                   + ", um teto entre o preço de monopólio e o custo marginal " + vd("eleva a quantidade e "
                   "reduz o peso morto") + ", sem desabastecimento."),
        "destrinchando": [
            "Três situações a separar: (1) teto " + azb("acima") + " do preço de equilíbrio → não vinculante, "
            "nada muda; (2) teto abaixo do equilíbrio em " + azb("concorrência perfeita") + " → escassez e peso "
            "morto; (3) teto em " + azb("monopólio") + " → pode melhorar a alocação.",
            "No monopólio, a firma produz onde RMg = CMg e cobra P > CMg: já há peso morto (o “triângulo de "
            + oc("Harberger") + "”). Com o teto, a receita marginal vira o próprio Pmáx até a demanda; a firma "
            "passa a vender mais.",
            "Resumo comparativo: concorrência perfeita com teto abaixo do equilíbrio → quantidade " + vd("cai")
            + ", peso morto " + vd("aumenta") + "; monopólio com teto entre Pm e o CMg → quantidade "
            + vd("sobe") + ", peso morto " + vd("diminui") + ".",
            "O teto ótimo para o monopólio é o preço em que a demanda cruza o CMg: replica o resultado "
            "competitivo. Abaixo dele, o teto volta a criar escassez. É a base da " + azb("regulação por "
            "preço-teto") + " (price cap) de monopólios naturais.",
            vm("Regra-âncora: o efeito do teto depende de onde ele é fixado e da estrutura de mercado."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " “Necessariamente” + “independente da estrutura de mercado” "
                       "convertem o caso competitivo em lei universal. 🔥 Mesmo item do Pré-TPS/2023 da Nabuco "
                       "(gabarito ERRADO): estrutura de mercado como contraexemplo é padrão recorrente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em concorrência perfeita, um preço máximo fixado acima do preço de equilíbrio não produz "
            "desabastecimento.”</i> → CERTO",
            "<i>“Em monopólio, um preço máximo igual ao preço de monopólio eleva a quantidade "
            "transacionada.”</i> → ERRADO (teto igual a Pm não vincula)",
        ])],
        "reescrita": ("A imposição de preço máximo " + hl("pode conduzir") + " à perda de bem-estar e ao "
                      "desabastecimento " + hl("em mercados competitivos, mas, em monopólio, um teto bem "
                      "calibrado pode elevar a quantidade e reduzir o peso morto") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["necessariamente", "independente"], "dificuldade": 2,
        "comentario_fonte": "Várias respostas de IA concordantes: em monopólio, um preço máximo entre o preço de "
                            "monopólio e o CMg aumenta a quantidade e reduz o peso morto; em concorrência "
                            "perfeita, gera escassez; teto acima do equilíbrio é não vinculante.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 257", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"},
                          {"ref": "IMAGEM 258", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"},
                          {"ref": "IMAGEM 259", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (resumo comparativo no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00202
    {
        "id": "ECO-E3-L00202-1", "fonte_ref": "E3-L00202", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR_INTERV,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de um imposto sobre a margem de lucro das empresas não afeta a condição de "
                      "equilíbrio de primeira ordem em nenhuma estrutura de mercado, ou seja, o ponto no qual a "
                      "receita marginal é igual ao custo marginal (Rmg = Cmg)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A imposição de um imposto sobre a <u>margem de lucro</u> das empresas não afeta a condição "
                      "de equilíbrio de primeira ordem em <u>nenhuma</u> estrutura de mercado, ou seja, o ponto no "
                      "qual a receita marginal é igual ao custo marginal (Rmg = Cmg)."),
        "poucas": ("Imposto proporcional ao lucro multiplica a função lucro por " + vd("(1 − t)") + ", uma "
                   "constante positiva: o máximo continua no mesmo q, onde " + azb("RMg = CMg") + "."),
        "destrinchando": [
            "Sem imposto: máx π(q) = RT(q) − CT(q) → CPO: RMg = CMg. Com alíquota t sobre o lucro: máx "
            "(1 − t)·π(q) → CPO: (1 − t)·(RMg − CMg) = 0. Como " + vd("1 − t > 0") + ", a condição continua "
            "RMg = CMg.",
            "Intuição: o governo vira um “sócio” que leva uma fração fixa do lucro. Para maximizar a sua parte, "
            "a firma precisa maximizar o lucro total — o ranking das opções não muda (100 > 80 vira 70 > 56).",
            "Vale para concorrência perfeita (P = CMg), monopólio (RMg = CMg), concorrência monopolística e "
            "oligopólio (as funções de reação não mudam). Por isso o imposto sobre lucro econômico puro é "
            + azb("neutro") + " no curto prazo: não gera peso morto na decisão de quanto produzir.",
            "Contraste: imposto " + azb("específico") + " (por unidade) desloca o CMg para cima (CMg + t); "
            "imposto " + azb("ad valorem") + " sobre a receita reduz a RMg para (1 − t)·RMg — ambos alteram q e P.",
            "Ressalvas (fora do modelo estático): se a base for o lucro contábil, que inclui o retorno normal "
            "do capital, o imposto afeta entrada, saída e investimento no longo prazo; há também elisão e "
            "planejamento tributário.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O “em nenhuma estrutura de mercado” soa como "
                       "modulador absoluto, mas é exato: a neutralidade decorre da matemática da maximização, "
                       "não da estrutura. A armadilha é tratar “imposto” como sinônimo de custo marginal maior."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto específico por unidade vendida não altera a quantidade ofertada pelo "
            "monopolista.”</i> → ERRADO (desloca o CMg para cima e reduz q)",
            "<i>“Um imposto sobre o lucro econômico reduz o lucro do monopolista sem alterar o preço "
            "cobrado.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["nenhuma"], "dificuldade": 2,
        "comentario_fonte": "Imposto sobre o lucro não altera RMg nem CMg; a CPO continua RMg = CMg, só o lucro "
                            "líquido diminui. Demonstração com (1 − t)·π, tabela por estrutura de mercado e "
                            "contraste com impostos específico e ad valorem.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 267", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (demonstração formal no 📖)"},
                          {"ref": "IMAGEM 268", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (validade por estrutura de mercado no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00271
    {
        "id": "ECO-E3-L00271-1", "fonte_ref": "E3-L00271", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Segundo a teoria microeconômica e os seus axiomas da racionalidade, julgue o item a seguir, "
                    "relativo ao bem-estar do consumidor."),
        "rotulo_item": "Item",
        "assertiva": ("A perda de bem-estar do consumidor no caso de um aumento de preço de um bem será dada pelo "
                      "aumento na despesa com a quantidade que ele continua consumindo do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A perda de bem-estar do consumidor no caso de um aumento de preço de um bem será dada ")
                   + vm("pelo aumento na despesa com a quantidade que ele continua consumindo do bem") + az("."),
        "poucas": ("A perda é a " + azb("redução do excedente do consumidor") + ": o gasto a mais com as "
                   "unidades que continua comprando (A) " + vd("mais") + " o excedente das unidades que deixou de "
                   "comprar (B). O item conta só A."),
        "destrinchando": [
            "Preço sobe de p₁ para p₂; a quantidade cai de q₁ para q₂. O excedente do consumidor (área entre a "
            "demanda e o preço) encolhe em duas parcelas:",
            "<b>A — retângulo</b> (p₂ − p₁) × q₂: o que o consumidor paga a mais pelas unidades que mantém. Não "
            "some da economia: vira excedente do produtor (ou receita do governo, se a alta vier de um imposto).",
            "<b>B — triângulo</b> entre q₂ e q₁: as unidades que deixaram de ser compradas, que valiam para ele "
            "mais que p₁. Com demanda linear, ≈ ½ · Δp · Δq. Exemplo: p de 4 para 6, q de 6 para 4 → A = "
            + vd("8") + ", B = " + vd("2") + ", perda total = " + vd("10") + ".",
            "Quanto mais elástica a demanda, maior B em relação a A. Com demanda perfeitamente inelástica, B "
            "desaparece e o item seria correto — é o único caso.",
            "Medidas exatas de bem-estar (" + oc("Hicks") + "): a " + azb("variação compensatória") + " e a "
            + azb("variação equivalente") + "; a variação do excedente marshalliano é uma aproximação entre "
            "elas, que coincidem quando não há efeito-renda.",
        ],
        "grafico_verso": "ECO-E3-L00271-1-V1",
        "dissecando": (cz("[meia-verdade]") + " O item descreve uma parte verdadeira da perda (o retângulo A) "
                       "como se fosse o todo. O “será dada pelo” exige a medida completa; falta o triângulo das "
                       "unidades abandonadas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento na despesa com a quantidade que o consumidor continua consumindo é parte da perda de "
            "excedente do consumidor.”</i> → CERTO",
            "<i>“Com demanda perfeitamente inelástica, a perda de excedente do consumidor equivale ao aumento "
            "da despesa com a quantidade consumida.”</i> → CERTO",
        ])],
        "reescrita": ("A perda de bem-estar do consumidor no caso de um aumento de preço de um bem será dada "
                      + hl("pela redução do excedente do consumidor: o aumento na despesa com a quantidade que ele "
                        "continua consumindo mais a perda de excedente nas unidades que deixou de consumir") + "."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Perda de EC = gasto adicional com as unidades ainda consumidas + perda nas unidades "
                            "que deixaram de ser consumidas. Algumas respostas de IA associam as duas parcelas "
                            "aos efeitos renda e substituição.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 376", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00271-1-V1: áreas A e B)"}],
        "alertas": ["qualidade_fonte: respostas de origem identificam o retângulo com o efeito-renda e o "
                    "triângulo com o efeito-substituição — associação imprecisa, não reproduzida"],
    },
    # ------------------------------------------------------------------ E3-L00336
    {
        "id": "ECO-E3-L00336-1", "fonte_ref": "E3-L00336", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_DEZ,
        "rotulo_item": "Item",
        "assertiva": ("Preço Marginal de Reserva é o preço máximo que o consumidor está disposto a pagar por uma "
                      "unidade adicional da mercadoria."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Preço Marginal de Reserva é o preço <u>máximo</u> que o consumidor está disposto a pagar "
                      "por uma <u>unidade adicional</u> da mercadoria."),
        "poucas": ("É a " + azb("disposição marginal a pagar") + ": quanto vale, em dinheiro, a próxima unidade. "
                   "Graficamente, a " + vd("altura da curva de demanda") + " em cada quantidade."),
        "destrinchando": [
            azb("Preço de reserva") + ": o máximo que um consumidor pagaria por um bem (para um bem indivisível "
            "comprado uma vez, como um carro). " + azb("Preço marginal de reserva") + ": o mesmo conceito "
            "aplicado a cada unidade adicional — a 1ª, a 2ª, a 3ª…",
            "Como a utilidade marginal é decrescente, o preço marginal de reserva cai à medida que o consumidor "
            "já tem mais unidades. É por isso que a demanda individual é negativamente inclinada: lida "
            "verticalmente, ela é a curva de benefício marginal.",
            "O consumidor compra enquanto o preço marginal de reserva for ≥ preço de mercado. Cada unidade "
            "rende um excedente de (preço de reserva − preço); somando-se tudo, chega-se ao "
            + azb("excedente do consumidor") + " = área entre a demanda e o preço.",
            "Leitura dupla da demanda: horizontal (dado p, quanto se compra) e vertical (dada a quantidade, "
            "quanto se pagaria pela última unidade). O conceito do item é a leitura vertical.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, com os dois termos-chave no lugar: "
                       "“máximo” e “unidade adicional”. A dúvida que derruba o candidato é confundir o preço "
                       "marginal de reserva com o preço de mercado ou com o preço de reserva da unidade inteira "
                       "comprada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Preço marginal de reserva é o preço mínimo que o consumidor aceita pagar por uma unidade "
            "adicional.”</i> → ERRADO (é o máximo)",
            "<i>“O preço marginal de reserva corresponde ao preço de mercado pago pelo consumidor.”</i> → ERRADO "
            "(coincide com ele só na última unidade comprada)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["máximo"], "dificuldade": 1,
        "comentario_fonte": "Cinco respostas de IA concordantes: disposição marginal a pagar, lida na altura da "
                            "curva de demanda; base do cálculo do excedente do consumidor.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 466", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00337
    {
        "id": "ECO-E3-L00337-1", "fonte_ref": "E3-L00337", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_DEZ,
        "rotulo_item": "Item",
        "assertiva": ("Excedente do Consumidor é a diferença que o consumidor está disposto a pagar e o que ele "
                      "efetivamente paga por uma mercadoria."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Excedente do Consumidor é a diferença <u>que o consumidor está disposto a pagar e o que ele "
                      "efetivamente paga</u> por uma mercadoria."),
        "poucas": ("Definição clássica: " + azb("disposição a pagar − preço pago") + ". Somada sobre todas as "
                   "unidades, é a " + vd("área entre a demanda e o preço") + "."),
        "destrinchando": [
            "Para uma unidade: excedente = preço de reserva − preço. Para o mercado: soma dessas diferenças "
            "sobre todas as unidades compradas — o triângulo abaixo da demanda e acima do preço (com demanda "
            "linear, ½ × base × altura).",
            "Mede o ganho líquido de bem-estar dos compradores por participarem do mercado. Sobe quando o preço "
            "cai (os antigos compradores pagam menos e novos compradores entram) e cai quando o preço sobe.",
            "Par simétrico: " + azb("excedente do produtor") + " = preço recebido − custo marginal (área entre o "
            "preço e a oferta). A soma é o excedente total, máximo no equilíbrio competitivo.",
            "A redação omite o “entre” (“a diferença [entre o] que…”) e não diz “somada sobre as unidades”, mas "
            "o núcleo da definição está correto — e é assim que a banca a aceita.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item-definição. O risco é o candidato procurar defeito na "
                       "redação imperfeita e marcar ERRADO; o critério é o conteúdo, que está certo. Erraria se "
                       "trocasse “disposto a pagar” por “custo de produção” (seria o EP)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Excedente do consumidor é a diferença entre o preço pago pelo consumidor e o custo marginal de "
            "produção.”</i> → ERRADO (troca de conceito: mistura com o excedente do produtor)",
            "<i>“Uma queda no preço de mercado aumenta o excedente do consumidor.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Cinco respostas de IA concordantes: definição clássica; área abaixo da demanda e "
                            "acima do preço; formalmente, soma das diferenças por unidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 467-469", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00338
    {
        "id": "ECO-E3-L00338-1", "fonte_ref": "E3-L00338", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_DEZ,
        "rotulo_item": "Item",
        "assertiva": ("Se o preço de um bem cair, o excedente do produtor aumenta por duas razões. Primeiro, há "
                      "aumento do excedente para os produtores que já vendiam o bem por causa do aumento da "
                      "demanda e, além disso, há crescimento por causa do incentivo à entrada de novos "
                      "produtores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o preço de um bem ") + vm("cair") + az(", o excedente do produtor aumenta por duas "
                      "razões. Primeiro, há aumento do excedente para os produtores que já vendiam o bem por "
                      "causa do aumento da demanda e, além disso, há crescimento por causa do incentivo à "
                      "entrada de novos produtores."),
        "poucas": ("As “duas razões” descrevem uma " + azb("alta") + " de preço: produtores antigos ganham mais "
                   "por unidade e novos produtores entram. Com o preço em queda, o excedente do produtor "
                   + vd("diminui") + "."),
        "destrinchando": [
            "Excedente do produtor = área entre o preço e a oferta. Se o preço " + azb("sobe") + " (por exemplo, "
            "por aumento da demanda), a área cresce por duas vias: (1) os produtores que já vendiam recebem mais "
            "por unidade (retângulo); (2) novos produtores, com custo marginal mais alto, passam a vender "
            "(triângulo). É a decomposição de " + oc("Mankiw") + " no capítulo sobre consumidores, produtores e "
            "eficiência dos mercados.",
            "Se o preço " + azb("cai") + ", ocorre o inverso: os antigos produtores recebem menos e os de custo "
            "mais alto saem do mercado. O EP " + vd("encolhe") + ".",
            "O item também é incoerente por dentro: aumento da demanda <b>eleva</b> o preço — não pode ser a "
            "causa de um preço em queda.",
            "Espelho do lado do consumidor: com preço em queda, o " + azb("excedente do consumidor") + " aumenta "
            "por duas razões — os compradores antigos pagam menos e novos compradores entram. O item parece "
            "ter misturado as duas decomposições.",
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " O item copia a decomposição correta do aumento do EP "
                       "e troca só o sentido da variação de preço. Pista interna: “aumento da demanda” e “preço "
                       "cair” não convivem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o preço de um bem cair, o excedente do consumidor aumenta, porque os compradores antigos "
            "pagam menos e novos compradores entram no mercado.”</i> → CERTO",
            "<i>“Uma alta do preço eleva o excedente do produtor apenas por meio da entrada de novos "
            "produtores.”</i> → ERRADO (restrição indevida: os antigos também ganham)",
        ])],
        "reescrita": ("Se o preço de um bem " + hl("subir") + ", o excedente do produtor aumenta por duas razões. "
                      "Primeiro, há aumento do excedente para os produtores que já vendiam o bem por causa do "
                      "aumento da demanda e, além disso, há crescimento por causa do incentivo à entrada de novos "
                      "produtores."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Várias respostas de IA concordantes: queda de preço reduz o EP; aumento da demanda "
                            "eleva o preço; a descrição corresponde a uma alta de preço (ou ao EC numa queda).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 470-471", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00339
    {
        "id": "ECO-E3-L00339-1", "fonte_ref": "E3-L00339", "destino": "03", "subtema": H2["exc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_DEZ,
        "rotulo_item": "Item",
        "assertiva": "O excedente do produtor no curto prazo pode ser medido pelo lucro total da empresa.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O excedente do produtor no curto prazo pode ser medido pelo ") + vm("lucro total")
                   + az(" da empresa."),
        "poucas": ("No curto prazo, " + vd("EP = RT − CV") + "; lucro = RT − CV − CF. Logo "
                   + vd("EP = lucro + custo fixo") + ": os dois só coincidem se o custo fixo for zero."),
        "destrinchando": [
            "O excedente do produtor é a soma, sobre as unidades vendidas, de (preço − custo marginal). Como a "
            "soma dos custos marginais é o " + azb("custo variável") + " (o custo fixo não varia com q), "
            "EP = RT − CV — no gráfico da firma, o retângulo (P − CVMe) × q.",
            azb("Lucro econômico") + " = RT − CT = RT − CV − CF. A diferença é o " + azb("custo fixo")
            + ", que no curto prazo é afundado e não afeta a decisão de produzir.",
            "Por isso a firma pode ter EP positivo com lucro negativo: se P > CVMe, ela cobre os custos variáveis "
            "e parte do fixo — melhor produzir que fechar (fechar daria prejuízo = CF inteiro).",
            "No longo prazo, sem custos fixos, EP e lucro econômico tendem a coincidir. Referência: "
            + oc("Pindyck e Rubinfeld") + ", <i>Microeconomia</i>, capítulo sobre maximização de lucros e "
            "oferta competitiva.",
            vm("Regra-âncora: EP de curto prazo = lucro + custo fixo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca o excedente do produtor por um conceito vizinho "
                       "(lucro). A pista é “no curto prazo”: é justamente o horizonte em que existe custo fixo "
                       "e os dois conceitos se separam."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, o excedente do produtor é igual à receita total menos o custo variável "
            "total.”</i> → CERTO",
            "<i>“O excedente do produtor de curto prazo é sempre menor que o lucro econômico.”</i> → ERRADO "
            "(inversão: é maior, pelo custo fixo)",
        ])],
        "reescrita": ("O excedente do produtor no curto prazo pode ser medido " + hl("pela receita total menos o "
                      "custo variável, isto é, pelo lucro mais o custo fixo") + " da empresa."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["no curto prazo"], "dificuldade": 2,
        "comentario_fonte": "EP = RT − CV; lucro = RT − CT; EP = lucro + custo fixo. Referência a Pindyck nas "
                            "anotações.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 472", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (identidades no 📖)"},
                          {"ref": "IMAGEM 473-474", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0008
    {
        "id": "ECO-E1-0008-1", "fonte_ref": "E1-0008", "destino": "04", "subtema": H2["esc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": "Acerca da escolha do consumidor em mercados competitivos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Nos mercados competitivos, a escolha ótima a ser feita por determinado consumidor "
                      "corresponde à escolha em que a taxa marginal de substituição entre dois bens quaisquer é "
                      "igual para todos os consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Nos <u>mercados competitivos</u>, a escolha ótima a ser feita por determinado consumidor "
                      "corresponde à escolha em que a taxa marginal de substituição entre dois bens quaisquer é "
                      "<u>igual para todos os consumidores</u>."),
        "poucas": ("Cada consumidor escolhe onde " + vd("TMS = p<sub>x</sub>/p<sub>y</sub>") + ". Em mercado "
                   "competitivo, todos enfrentam os " + azb("mesmos preços") + ", logo, no ótimo, todas as TMS "
                   "são iguais."),
        "destrinchando": [
            "Ótimo do consumidor (solução interior): tangência entre a curva de indiferença e a reta "
            "orçamentária, " + vd("TMS<sub>xy</sub> = UMg<sub>x</sub>/UMg<sub>y</sub> = "
            "p<sub>x</sub>/p<sub>y</sub>") + ". A TMS mede quanto de y o consumidor aceita ceder por mais uma "
            "unidade de x; o preço relativo, quanto o mercado cobra.",
            "Em concorrência perfeita há preço único (todos são tomadores de preço). Se cada um iguala a sua "
            "TMS ao mesmo p<sub>x</sub>/p<sub>y</sub>, então TMS<sup>A</sup> = TMS<sup>B</sup> = … para todos "
            "— ainda que as cestas, as rendas e as preferências sejam diferentes.",
            "Esse é o resultado de " + azb("eficiência nas trocas") + ": com TMS iguais, não há troca adicional "
            "que melhore alguém sem piorar outro (curva de contrato na caixa de " + oc("Edgeworth")
            + "). É peça do 1º teorema do bem-estar.",
            "Se as TMS diferissem (A valoriza x em 3 y e B em 1 y), A compraria x de B a qualquer preço entre 1 "
            "e 3 e ambos ganhariam — sinal de que o ótimo ainda não foi atingido.",
            "Limites: soluções de canto (consumidor que não compra um dos bens) e preços diferenciados "
            "(discriminação, subsídios por grupo) quebram a igualdade.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " A redação junta duas coisas — o ótimo individual "
                       "(TMS = preço relativo) e a consequência agregada (TMS igual para todos) — numa só frase, "
                       "o que soa estranho. O elo é o preço único do mercado competitivo; quem pensa que "
                       "preferências diferentes geram TMS diferentes no ótimo marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em mercados competitivos, no ótimo, todos os consumidores consomem as mesmas quantidades dos "
            "bens.”</i> → ERRADO (as TMS se igualam, não as cestas)",
            "<i>“Se o vendedor praticar discriminação de preços entre consumidores, as TMS no ótimo continuam "
            "necessariamente iguais.”</i> → ERRADO (preços relativos diferentes → TMS diferentes)",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["quaisquer", "todos"], "dificuldade": 2,
        "comentario_fonte": "Comentários empilhados concordam: TMS = preço relativo no ótimo; preços dados e "
                            "iguais para todos tornam as TMS iguais; igualdade de TMS não implica igualdade de "
                            "quantidades. Um deles traz exemplo numérico inconsistente (troca de 2 kg de arroz "
                            "por um cinto convertida em TMS de 5 kg por cinto).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["gabarito: a classificação marcava “?”; o verso da fonte indica CERTO em todas as respostas "
                    "(“Correta”, “Item correto!”, “Verdadeiro”)",
                    "banca_provavel: item com ano (2010) e estilo C/E de CEBRASPE; prova não identificada por "
                    "busca"],
    },
    # ------------------------------------------------------------------ E1-0012
    {
        "id": "ECO-E1-0012-1", "fonte_ref": "E1-0012", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca da teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("É correto afirmar que “Uma curva de indiferença representa uma combinação de quantidades "
                      "de bens expressa em cestas de consumo que mantém o consumidor indiferente entre tais "
                      "cestas.”?"),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma curva de indiferença representa uma combinação de quantidades de bens expressa em "
                      "cestas de consumo que mantém o consumidor <u>indiferente</u> entre tais cestas."),
        "poucas": ("Curva de indiferença = lugar geométrico das " + azb("cestas que dão o mesmo nível de "
                   "utilidade") + ": o consumidor não prefere nenhuma delas às demais."),
        "destrinchando": [
            "Cada ponto da curva é uma cesta (x, y); todas as cestas da mesma curva geram a mesma satisfação. "
            "Cestas acima/à direita (em curvas mais altas) são preferidas, sob monotonicidade.",
            "A curva retrata só as " + azb("preferências") + ": não envolve preços nem renda — estes entram pela "
            "reta orçamentária. O ótimo é a tangência entre as duas.",
            "Propriedades das preferências bem-comportadas: inclinação negativa (monotonicidade: para ter menos "
            "de um bem, é preciso mais do outro), convexidade (TMS decrescente) e curvas que " + vd("não se "
            "cruzam") + " (transitividade).",
            "A inclinação é a " + azb("taxa marginal de substituição") + " (TMS = UMg<sub>x</sub>/UMg<sub>y</sub>), "
            "a taxa à qual o consumidor troca um bem pelo outro sem mudar de utilidade.",
            "Formatos especiais: retas (substitutos perfeitos), em L (complementares perfeitos), "
            "positivamente inclinadas quando um dos bens é um “mal”.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual em forma de pergunta. O risco é procurar "
                       "pelo em ovo: “combinação de quantidades … em cestas” é redundante, mas correto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma curva de indiferença mostra as cestas que o consumidor pode adquirir com a sua "
            "renda.”</i> → ERRADO (troca de conceito: essa é a restrição orçamentária)",
            "<i>“Curvas de indiferença de um mesmo consumidor com preferências transitivas podem se "
            "cruzar.”</i> → ERRADO (o cruzamento violaria a transitividade)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Definição: combinações de dois bens entre as quais o consumidor é indiferente, mesma "
                            "utilidade; não considera preços nem renda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0053
    {
        "id": "ECO-E1-0053-1", "fonte_ref": "E1-0053", "destino": "04", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca da demanda de mercado, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "A curva de demanda de mercado de um determinado bem representa a soma das demandas individuais.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de demanda de mercado de um determinado bem representa a <u>soma</u> das demandas "
                      "individuais."),
        "poucas": ("A demanda de mercado é a " + azb("soma horizontal") + " das demandas individuais: para cada "
                   "preço, somam-se as " + vd("quantidades") + " demandadas por todos os consumidores."),
        "destrinchando": [
            "Soma horizontal: fixa-se o preço e somam-se as quantidades — Q(p) = q<sub>1</sub>(p) + "
            "q<sub>2</sub>(p) + … Não se somam preços (isso seria soma vertical).",
            "Exemplo: q<sub>A</sub> = 10 − p e q<sub>B</sub> = 20 − 2p → Q = " + vd("30 − 3p") + " para p ≤ 10. "
            "Acima de p = 10, A sai do mercado e só B demanda: a curva de mercado tem uma " + azb("quebra")
            + " (dobra) no preço em que um consumidor entra ou sai.",
            "Consequências: a demanda de mercado é mais plana (mais elástica em cada preço) que as individuais, e "
            "se desloca também com o " + azb("número de consumidores") + " — um determinante que não existe "
            "na demanda individual.",
            "Contraste: para " + azb("bens públicos") + " (não rivais), a disposição a pagar agregada é a soma "
            + vd("vertical") + " das demandas — todos consomem a mesma quantidade, e somam-se os valores "
            "marginais.",
            "Ressalva teórica: a soma simples supõe demandas independentes; efeitos de rede, “efeito manada” ou "
            "“esnobe” tornam a demanda de cada um dependente da dos outros.",
        ],
        "dissecando": (cz("[literalidade]") + " Item curto e verdadeiro. A versão que a banca usa para "
                       "derrubar é trocar “soma horizontal” por “vertical” ou aplicar a soma horizontal a bens "
                       "públicos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de demanda de mercado é obtida pela soma vertical das curvas de demanda "
            "individuais.”</i> → ERRADO (soma-se horizontalmente, as quantidades)",
            "<i>“Para bens públicos, a curva de disposição marginal a pagar agregada é a soma vertical das "
            "individuais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A demanda de mercado é a soma horizontal das demandas individuais para cada preço.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0183
    {
        "id": "ECO-E1-0183-1", "fonte_ref": "E1-0183", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": True,
        "comando": "Acerca das preferências do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O pressuposto de que “quanto mais de um bem, melhor” é tratado no axioma da "
                      "monotonicidade das preferências."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O pressuposto de que “quanto mais de um bem, melhor” é tratado no axioma da "
                      "<u>monotonicidade</u> das preferências."),
        "poucas": ("" + azb("Monotonicidade") + " (não saciedade): uma cesta com mais de pelo menos um bem, e não "
                   "menos de nenhum, é preferida. É o “quanto mais, melhor”."),
        "destrinchando": [
            "Axiomas das preferências racionais: " + azb("completude") + " (o consumidor compara quaisquer duas "
            "cestas), " + azb("transitividade") + " (A ≻ B e B ≻ C ⇒ A ≻ C) e, para preferências "
            "<b>bem-comportadas</b>, " + azb("monotonicidade") + " e " + azb("convexidade") + ".",
            "Monotonicidade = não saciedade: utilidade marginal positiva, mesmo que pequena. Consequências "
            "gráficas: curvas de indiferença " + vd("negativamente inclinadas") + " (perder um bem exige "
            "compensação no outro) e curvas mais afastadas da origem representando mais utilidade.",
            "Convexidade é outra coisa: “médias são preferidas aos extremos” — gera TMS decrescente e curvas "
            "convexas em relação à origem.",
            "Exceções que violam a monotonicidade: males (poluição, lixo), bens com ponto de saciedade "
            "(“bliss point”) e bens neutros.",
        ],
        "dissecando": (cz("[literalidade]") + " Associação direta entre o rótulo e a ideia. As versões erradas "
                       "costumam trocar o axioma: atribuir o “quanto mais, melhor” à convexidade ou à "
                       "transitividade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O pressuposto de que médias são preferidas aos extremos decorre do axioma da "
            "monotonicidade.”</i> → ERRADO (troca de conceito: é a convexidade)",
            "<i>“Sob monotonicidade, as curvas de indiferença têm inclinação negativa.”</i> → CERTO",
        ]), ("🧠 Mnemônico", ["<b>MONEY</b>tonicidade: com dinheiro, quanto mais, melhor."])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Vários comentários de professores concordantes: monotonicidade = não saciedade, "
                            "“quanto mais, melhor”; lista de axiomas (completude, transitividade, monotonicidade, "
                            "convexidade); mnemônico “MONEYtonicidade”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
