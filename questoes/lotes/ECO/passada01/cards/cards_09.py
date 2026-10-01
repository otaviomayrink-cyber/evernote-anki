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
]
