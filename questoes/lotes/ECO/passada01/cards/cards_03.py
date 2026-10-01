"""Cards da passada 01 de ECO — lote de redação 03."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "fund": "🧭 Fundamentos e escassez",
    "fpp": "📐 Curva de possibilidades de produção",
    "dem": "📈 Demanda: determinantes e deslocamentos",
    "of": "🏭 Oferta: determinantes e deslocamentos",
    "bens": "🏷️ Classificação dos bens",
    "eq": "⚖️ Equilíbrio e estática comparativa",
    "cp": "📐 Hipóteses e maximização de lucro",
    "pmin": "🚧 Preços máximos e mínimos",
}

COMANDO_NABUCO_3 = ("Em relação à oferta e demanda e à classificação dos bens, julgue o item, considerando o "
                    "Gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo de D1 para D2.")

COMANDO_MACAS = "Considere a situação hipotética a seguir e julgue o item."
EXCERTO_MACAS = ("<p><i>Em um pequeno país, o mercado de maçãs funciona em equilíbrio sob concorrência perfeita. "
                 "Em determinada data, o quilo da maçã é vendido, em todo o país, por $ 5. Considere nulos os custos "
                 "de transação e os custos de menu.</i></p>")

COMANDO_NIDI = ("A teoria da demanda aborda como os consumidores tomam decisões sobre a quantidade de bens que "
                "adquirem com base em fatores como preços, preferências, restrições orçamentárias e a relação entre "
                "os tipos de bens. Considerando a Teoria do Consumidor e os fatores que contribuem para formação da "
                "Curva de Demanda, avalie como certo ou errado (C ou E) o item a seguir.")

COMANDO_EQ = ("Em um mercado competitivo, as curvas de demanda e de oferta de um produto são Qᴰ = 300 − 30p e "
              "Qˢ = 10p + 20, em que p é o preço do produto, em reais. Julgue o item.")

CARDS = [
    # ------------------------------------------------------------------ E1-0083
    {
        "id": "ECO-E1-0083-1", "fonte_ref": "E1-0083", "destino": "01", "subtema": H2["of"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da oferta.",
        "rotulo_item": "Item",
        "assertiva": ("O deslocamento para a esquerda da curva de oferta de um bem pode ser ocasionado por um "
                      "aumento da tributação indireta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O deslocamento para a esquerda da curva de oferta de um bem <u>pode</u> ser ocasionado por "
                      "um aumento da <u>tributação indireta</u>."),
        "poucas": ("Tributo indireto funciona como " + azb("custo adicional por unidade") + " para o vendedor: a "
                   "cada preço ele oferta menos, e a curva de oferta sobe (= vai para a esquerda)."),
        "destrinchando": [
            azb("Tributos indiretos") + " (ICMS, IPI, ISS, imposto específico) incidem sobre a venda do bem. "
            "Para continuar ofertando a mesma quantidade, o produtor precisa receber o preço anterior "
            "<b>mais</b> o tributo: a oferta, vista pelo comprador, desloca-se verticalmente para cima no valor "
            "do imposto — o que, numa curva crescente, é o mesmo que deslocar-se para a esquerda.",
            "Determinantes que deslocam a oferta: preço dos insumos, tecnologia, tributos e subsídios, número "
            "de vendedores, expectativas e preços de outros bens que a firma poderia produzir. O "
            "<b>preço do próprio bem</b> não desloca: faz andar ao longo da curva.",
            "Efeito no equilíbrio: preço pago pelo consumidor sobe, quantidade cai. Quanto do imposto cada "
            "lado arca depende das " + azb("elasticidades") + " (o lado menos elástico paga mais), e não de "
            "quem recolhe o tributo ao fisco.",
            "Espelho: um " + azb("subsídio") + " por unidade reduz o custo efetivo e desloca a oferta para a "
            "direita.",
            vm("Regra-âncora: tudo o que encarece produzir (insumo, tributo) tira oferta; tudo o que barateia "
               "(tecnologia, subsídio) põe oferta."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item de manual, protegido pelo “pode”: "
                       "basta que a tributação indireta seja <b>uma</b> causa possível de contração da oferta. "
                       "O risco é confundir com o imposto cobrado do comprador, que se costuma desenhar como "
                       "deslocamento da demanda — e que tem o mesmo efeito econômico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento da tributação indireta provoca movimento ao longo da curva de oferta do bem.”</i> → "
            "ERRADO (troca de conceito: é deslocamento)",
            "<i>“A concessão de subsídio por unidade produzida desloca a curva de oferta para a direita.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "CERTO. O aumento de tributos indiretos eleva o custo de produção, reduzindo a oferta "
                            "— deslocamento da curva para a esquerda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (13).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; o texto basta)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0204
    {
        "id": "ECO-E1-0204-1", "fonte_ref": "E1-0204", "destino": "01", "subtema": H2["of"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "MPE/TO/Analista Ministerial/2006", "ano": 2006,
        "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à curva de oferta.",
        "rotulo_item": "Item",
        "assertiva": ("Na curva de oferta, a relação positiva entre a quantidade ofertada e o preço é consistente "
                      "com a lei do custo de oportunidade crescente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na curva de oferta, a relação positiva entre a quantidade ofertada e o preço é "
                      "<u>consistente</u> com a lei do custo de oportunidade crescente."),
        "poucas": ("Se cada unidade adicional custa mais (em recursos desviados de outros usos), o produtor só a "
                   "oferta com " + azb("preço maior") + ": a oferta crescente espelha o " + azb("custo de "
                   "oportunidade crescente") + "."),
        "destrinchando": [
            "A " + azb("lei do custo de oportunidade crescente") + " diz que, para produzir mais de um bem, a "
            "economia (ou a firma) precisa sacrificar quantidades cada vez maiores de outros bens, porque os "
            "recursos deslocados são progressivamente menos adequados à nova atividade. É ela que dá à "
            + azb("FPP") + " o formato côncavo.",
            "Na firma, a mesma ideia aparece como " + azb("custo marginal crescente") + " (rendimentos "
            "marginais decrescentes de algum fator). Em concorrência perfeita, a oferta da firma é o trecho "
            "do CMg acima do CVMe mínimo: se o CMg sobe, a quantidade ofertada só aumenta se o preço aumentar "
            "— daí a " + vd("inclinação positiva") + ".",
            "Ou seja: o preço tem de cobrir o custo da última unidade, e esse custo é, no fundo, o valor do que "
            "se deixou de produzir com os mesmos recursos.",
            "Contraponto útil: com custo de oportunidade <b>constante</b> (FPP reta, CMg constante), a oferta "
            "de longo prazo seria horizontal (perfeitamente elástica), e não crescente.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item liga dois capítulos (FPP e oferta) com a palavra "
                       "“consistente”, que é fraca: não afirma causalidade única, só compatibilidade. Quem não "
                       "reconhece o CMg como custo de oportunidade tende a achar que se misturaram temas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A inclinação positiva da curva de oferta é consistente com custos de oportunidade "
            "decrescentes.”</i> → ERRADO (inversão: crescentes)",
            "<i>“Com custo marginal constante, a curva de oferta de longo prazo de uma indústria competitiva é "
            "horizontal.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "CORRETO. O custo de oportunidade também é crescente.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (52).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0205
    {
        "id": "ECO-E1-0205-1", "fonte_ref": "E1-0205", "destino": "01", "subtema": H2["of"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "Prefeitura de Rio Branco/2007", "ano": 2007,
        "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da oferta e ao equilíbrio de mercado.",
        "rotulo_item": "Item",
        "assertiva": ("A recente crise de energia na Argentina, por aumentar o preço de insumos básicos para a "
                      "indústria, gera um deslocamento ao longo da curva de oferta do setor manufatureiro, "
                      "elevando, assim, o preço da produção industrial naquele país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A recente crise de energia na Argentina, por aumentar o preço de insumos básicos para a "
                      "indústria, gera um ") + vm("deslocamento ao longo da curva de oferta")
                   + az(" do setor manufatureiro, elevando, assim, o preço da produção industrial naquele país."),
        "poucas": ("Insumo mais caro é determinante da oferta: a " + azb("curva de oferta inteira se desloca") +
                   " para a esquerda. Movimento ao longo da oferta só ocorre quando muda o preço do próprio bem."),
        "destrinchando": [
            "Energia é insumo: se encarece, o " + azb("custo marginal") + " de cada unidade produzida sobe, e a "
            "indústria passa a ofertar menos a cada preço — " + azb("contração da oferta") + " (O₁ → O₂, para "
            "a esquerda/para cima).",
            "A consequência descrita no fim do item está certa: o novo equilíbrio tem " + vd("preço maior") +
            " e " + vd("quantidade menor") + ". O erro está só no mecanismo.",
            "Detalhe que derruba muita gente: depois do choque, há sim um movimento ao longo de uma curva — "
            "mas é ao longo da curva de <b>demanda</b> (de E₁ para E₂), porque os consumidores reagem ao novo "
            "preço. A curva de oferta, essa, mudou de lugar.",
            "Vocabulário: " + azb("variação da oferta") + " (deslocamento) × " + azb("variação da quantidade "
            "ofertada") + " (movimento ao longo, causado pelo preço do próprio bem).",
            vm("Regra-âncora: choque de custo → a oferta se desloca; o mercado então anda ao longo da "
               "demanda."),
        ],
        "grafico_verso": "ECO-E1-0205-1-V1",
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " A causa (insumos mais caros) e o efeito "
                       "(preço maior) estão corretos; a banca trocou só o rótulo do mecanismo, “deslocamento "
                       "ao longo” no lugar de “deslocamento da curva”. 🔥 Expressão híbrida típica da "
                       "CEBRASPE: “deslocamento ao longo” é o sinal para checar qual curva se moveu."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…gera um deslocamento da curva de oferta do setor manufatureiro para a direita…”</i> → ERRADO "
            "(sentido trocado: custo maior desloca para a esquerda)",
            "<i>“…gera movimento ao longo da curva de demanda por bens industriais, com queda da quantidade "
            "demandada.”</i> → CERTO",
        ])],
        "reescrita": ("A recente crise de energia na Argentina, por aumentar o preço de insumos básicos para a "
                      "indústria, gera um " + hl("deslocamento para a esquerda da curva de oferta") + " do setor "
                      "manufatureiro, elevando, assim, o preço da produção industrial naquele país."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Deslocamento ao longo da curva só quando há alteração no preço.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (54).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; mecanismo redesenhado em "
                                   "ECO-E1-0205-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0210
    {
        "id": "ECO-E1-0210-1", "fonte_ref": "E1-0210", "destino": "01", "subtema": H2["fpp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "MEC/Analista Administrativo – Economia/2018",
        "ano": 2018, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo aos conceitos fundamentais de economia.",
        "rotulo_item": "Item",
        "assertiva": ("Fronteira de possibilidades de produção consiste de uma construção gráfica que mostra a "
                      "limitação do potencial produtivo de um país na produção de um par de bens ou serviços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Fronteira de possibilidades de produção consiste de uma construção gráfica que mostra a "
                      "<u>limitação do potencial produtivo</u> de um país na produção de um par de bens ou "
                      "serviços."),
        "poucas": ("A " + azb("FPP") + " é o gráfico das combinações <b>máximas</b> de dois bens que a economia "
                   "consegue produzir com os recursos e a tecnologia dados: é a escassez desenhada."),
        "destrinchando": [
            "Hipóteses: dois bens, recursos (terra, trabalho, capital) e tecnologia <b>fixos</b>, uso pleno e "
            "eficiente dos fatores. Cada ponto da curva é uma alocação eficiente.",
            "Leitura das regiões: ponto <b>sobre</b> a curva → eficiente; <b>dentro</b> → ineficiente "
            "(desemprego, ociosidade); <b>fora</b> → inatingível com os recursos atuais.",
            "A FPP ilustra três ideias de uma vez: " + azb("escassez") + " (há limite), " + azb("escolha") +
            " (é preciso decidir o ponto) e " + azb("custo de oportunidade") + " (inclinação: quanto de um "
            "bem se sacrifica por unidade adicional do outro). Côncava → custo de oportunidade crescente; "
            "reta → constante.",
            "Desloca-se para fora com crescimento: mais fatores, progresso técnico, capital humano. Uma "
            "recessão <b>não</b> desloca a FPP; leva a economia para dentro dela.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, com sinônimos (“limitação do potencial "
                       "produtivo” = escassez de recursos). A banca às vezes troca o par de bens por “todos os "
                       "bens” ou diz que pontos internos são inatingíveis — aí sim o item cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os pontos situados abaixo da fronteira de possibilidades de produção são inatingíveis com os "
            "recursos disponíveis.”</i> → ERRADO (troca de conceito: são atingíveis, mas ineficientes)",
            "<i>“Uma recessão desloca a fronteira de possibilidades de produção para dentro.”</i> → ERRADO "
            "(troca de conceito: a economia passa a operar dentro da FPP)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CORRETO (verso sem texto além do gabarito).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (60).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0211
    {
        "id": "ECO-E1-0211-1", "fonte_ref": "E1-0211", "destino": "01", "subtema": H2["fpp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "EBC/2011", "ano": 2011, "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo à fronteira de possibilidades de produção.",
        "rotulo_item": "Item",
        "assertiva": ("Se um avanço tecnológico no setor de informática implicar deslocamento da fronteira de "
                      "possibilidades de produção de automóveis e computadores de um país, mais computadores e "
                      "automóveis serão produzidos nessa economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um avanço tecnológico no setor de informática implicar deslocamento da fronteira de "
                      "possibilidades de produção de automóveis e computadores de um país, mais computadores "
                      "<u>e automóveis</u> serão produzidos nessa economia."),
        "poucas": ("Mesmo um progresso técnico só na informática expande a FPP: produzir os mesmos computadores "
                   "exige menos recursos, e o que sobra pode ir para automóveis. " + azb("Mais dos dois") +
                   " passa a ser possível."),
        "destrinchando": [
            "Progresso técnico " + azb("viesado") + " (só em um setor) não desloca a FPP em paralelo: ela "
            "<b>gira</b> para fora, ancorada no intercepto do bem que não mudou. O máximo de automóveis (todos "
            "os recursos em carros) continua igual; o máximo de computadores aumenta.",
            "Mas, em qualquer ponto interior da fronteira, a nova FPP fica <b>acima</b> da antiga: com a "
            "tecnologia melhor, a quantidade anterior de computadores é feita com menos trabalho e capital, "
            "e os fatores liberados podem produzir automóveis. Por isso é possível ter " + vd("mais "
            "computadores e mais automóveis") + " ao mesmo tempo (ponto A → ponto B no gráfico).",
            "É a lógica do crescimento: mais fatores ou melhor tecnologia ampliam o conjunto de escolhas "
            "da sociedade, mesmo quando o ganho nasce num só setor.",
            "Nuance de redação: a FPP mostra o que <b>pode</b> ser produzido; se a economia de fato produzirá "
            "mais dos dois depende da escolha do novo ponto (e do pleno emprego). A banca leu o “serão "
            "produzidos” como “podem ser produzidos” e manteve CERTO.",
        ],
        "grafico_verso": "ECO-E1-0211-1-V1",
        "dissecando": (cz("[contraintuitivo]") + " A armadilha é achar que um avanço “no setor de informática” "
                       "só beneficia computadores. O item é verdadeiro porque a nova fronteira domina a antiga "
                       "em todo o interior. O “serão produzidos” (em vez de “poderão”) é o que tornava o item "
                       "arriscado — e o motivo provável do ❌."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um avanço tecnológico restrito ao setor de informática desloca paralelamente a FPP, elevando "
            "na mesma proporção a produção máxima de automóveis e de computadores.”</i> → ERRADO (a FPP gira; "
            "o máximo de automóveis não muda)",
            "<i>“Um avanço tecnológico restrito ao setor de informática não altera a produção máxima possível "
            "de automóveis, se todos os recursos forem alocados nesse setor.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["serão"], "dificuldade": 2,
        "comentario_fonte": "CERTO. Exatamente. A fronteira foi deslocada, agora eu posso produzir mais.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (59).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; mecanismo redesenhado em "
                                   "ECO-E1-0211-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0234 (1)
    {
        "id": "ECO-E1-0234-1", "fonte_ref": "E1-0234", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2020", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": COMANDO_MACAS, "excerto": EXCERTO_MACAS,
        "rotulo_item": "Item",
        "assertiva": ("Se um novo morador migrar para o país e não houver choques exógenos de oferta e de "
                      "demanda, pagará o preço de $ 5 por quilo de maçã que adquirir."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um novo morador migrar para o país e <u>não houver choques exógenos</u> de oferta e de "
                      "demanda, pagará o preço de $ 5 por quilo de maçã que adquirir."),
        "poucas": ("Em concorrência perfeita, cada agente é " + azb("tomador de preço") + ": um consumidor a mais "
                   "é desprezível diante do mercado e não move a demanda. Sem choques, o preço segue " +
                   vd("$ 5") + "."),
        "destrinchando": [
            "Hipóteses da " + azb("concorrência perfeita") + ": " + azb("atomicidade") + " (muitos compradores "
            "e vendedores, cada um pequeno demais para influir no preço), produto homogêneo, informação "
            "perfeita, livre entrada e saída. Daí a " + azb("lei do preço único") + ": todos pagam o mesmo "
            "preço.",
            "Um morador novo acrescenta uma parcela infinitesimal à demanda de mercado; o deslocamento é "
            "desprezível e o equilíbrio (p = 5) não se altera. Para o indivíduo, a oferta que ele enfrenta é, "
            "na prática, horizontal ao preço de mercado.",
            "Custos de transação e de menu nulos eliminam diferenças de preço entre lojas e atrasos de "
            "reajuste: não há por que alguém pagar mais (ou menos) que $ 5.",
            "Contraste: num mercado com poucos vendedores ou num bem diferenciado, preços distintos podem "
            "coexistir e um comprador grande (monopsônio) pode influir no preço.",
        ],
        "dissecando": (cz("[detalhe]") + " A ressalva “não houver choques exógenos” blinda o item; o que se "
                       "testa é a atomicidade. Quem imagina que “mais demanda → mais preço” sem pesar o tamanho "
                       "do choque marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A chegada de milhares de novos moradores com renda elevada, sem alteração da oferta, manteria "
            "o preço em $ 5.”</i> → ERRADO (choque de demanda relevante eleva o preço)",
            "<i>“Em concorrência perfeita, nenhum consumidor isolado consegue alterar o preço de "
            "mercado.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Correto. Pela condição de concorrência perfeita, a adição de um único consumidor a "
                            "uma base muito numerosa não gera efeito sobre a demanda de mercado, deixando o preço "
                            "inalterado.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: a fonte só traz o ano (2020); possivelmente CEBRASPE, não confirmado"],
    },
    # ------------------------------------------------------------------ E1-0234 (2)
    {
        "id": "ECO-E1-0234-2", "fonte_ref": "E1-0234", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2020", "ano": 2020, "cacd": False,
        "errei": True,
        "comando": COMANDO_MACAS, "excerto": EXCERTO_MACAS,
        "rotulo_item": "Item",
        "assertiva": ("Uma nova mercearia que venda maçãs no pequeno país não terá incentivos para vender as "
                      "frutas por menos que $ 5 por quilo, pois obterá lucros menores do que conseguiria caso "
                      "mantivesse o preço no nível de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma nova mercearia que venda maçãs no pequeno país não terá incentivos para vender as "
                      "frutas por menos que $ 5 por quilo, pois obterá <u>lucros menores</u> do que conseguiria "
                      "caso mantivesse o preço no nível de equilíbrio."),
        "poucas": ("A firma competitiva enfrenta " + azb("demanda horizontal") + " ao preço de mercado: vende "
                   "tudo o que quiser a $ 5. Baixar o preço não lhe traz um cliente a mais que já não teria — "
                   "só reduz a receita e o lucro."),
        "destrinchando": [
            "Para a firma em concorrência perfeita, a demanda é perfeitamente elástica ao preço de mercado: "
            + vd("p = RMe = RMg = 5") + ". Ela maximiza o lucro produzindo onde " + azb("p = CMg") + ".",
            "Vender abaixo de $ 5 é dinheiro deixado na mesa: a mesma quantidade poderia ser vendida a $ 5. "
            "Vender acima é perder todos os clientes, que compram dos concorrentes ao preço de mercado "
            "(produto homogêneo, informação perfeita).",
            "Por isso a firma competitiva é " + azb("tomadora de preço") + ": não há guerra de preços nem "
            "estratégia de preço em concorrência perfeita; a única decisão é <b>quanto</b> produzir.",
            "Cuidado com a justificativa que às vezes acompanha o item (“venderia abaixo do custo "
            "marginal”): o ponto central é a receita perdida. Abaixo de $ 5, na quantidade ótima anterior, o "
            "preço passaria a ficar abaixo do CMg, e o lucro cai por qualquer ângulo.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O senso comum diz que “preço menor atrai "
                       "clientes”; em concorrência perfeita, isso não vale, porque a firma já vende quanto "
                       "quiser ao preço vigente. A palavra “nova” tenta sugerir estratégia de entrada com "
                       "preço baixo — irrelevante aqui."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma nova mercearia poderá ampliar seu lucro vendendo a $ 4,90, pois atrairá todos os "
            "consumidores do país.”</i> → ERRADO (a firma competitiva já vende tudo a $ 5)",
            "<i>“Se a nova mercearia cobrar $ 5,10, perderá toda a sua clientela.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Correto. Se a mercearia assim o fizer, estará vendendo a maçã por um preço abaixo do "
                            "seu custo marginal de produção (P = CMg), tornando inviável tal estratégia.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: errei — na fonte, a marca ❌ está só no item 2 da questão",
                    "banca_provavel: a fonte só traz o ano (2020); possivelmente CEBRASPE, não confirmado"],
    },
    # ------------------------------------------------------------------ E1-0234 (3)
    {
        "id": "ECO-E1-0234-3", "fonte_ref": "E1-0234", "destino": "01", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2020", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": COMANDO_MACAS, "excerto": EXCERTO_MACAS,
        "rotulo_item": "Item",
        "assertiva": ("Suponha que, no final do ano, haverá a festa nacional das tortas de maçã não prevista no "
                      "pequeno país; isso causará uma elevação no preço e um aumento nas quantidades vendidas de "
                      "maçãs."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Suponha que, no final do ano, haverá a festa nacional das tortas de maçã <u>não "
                      "prevista</u> no pequeno país; isso causará uma elevação no preço e um aumento nas "
                      "quantidades vendidas de maçãs."),
        "poucas": ("A festa é um " + azb("choque positivo de demanda") + ": a curva de demanda vai para a "
                   "direita e, com oferta crescente, o novo equilíbrio tem " + vd("preço e quantidade "
                   "maiores") + "."),
        "destrinchando": [
            "A festa muda um determinante da demanda que não é o preço (gostos/ocasião de consumo): D₁ → D₂. "
            "Ao preço antigo surge excesso de demanda, o preço sobe e os produtores respondem andando "
            "<b>ao longo</b> da curva de oferta — mais quantidade.",
            "Tabela dos quatro choques simples: ↑D → p↑ q↑; ↓D → p↓ q↓; ↑O → p↓ q↑; ↓O → p↑ q↓. "
            "Com dois choques simultâneos, uma das variáveis fica indeterminada.",
            "Por que “não prevista” importa: se a festa fosse antecipada, ofertantes poderiam ter planejado "
            "estoques ou plantio, deslocando também a oferta e amortecendo a alta do preço. Como surpresa, só "
            "a demanda se move no curto prazo.",
            "Exceção a lembrar: oferta perfeitamente inelástica (vertical) → só o preço sobe; perfeitamente "
            "elástica (horizontal) → só a quantidade sobe.",
        ],
        "dissecando": (cz("[literalidade]") + " Estática comparativa de manual: um choque, uma curva, efeitos "
                       "na mesma direção. O “não prevista” serve para isolar o choque de demanda; a banca "
                       "testaria o erro trocando o sentido de uma das variáveis."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…isso causará uma elevação no preço e uma redução nas quantidades vendidas de maçãs.”</i> → "
            "ERRADO (esse par é de choque negativo de oferta)",
            "<i>“Se, além da festa, uma praga reduzisse a colheita, o preço subiria, mas o efeito sobre a "
            "quantidade seria indeterminado.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Correto. Em concorrência perfeita, a informação é livremente disponível; só uma "
                            "surpresa desloca o equilíbrio. Trata-se de elevação inesperada da demanda: preço "
                            "sobe e produtores respondem com maior produção.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: classificação sem gabarito; adotado o da fonte (Correto)",
                    "banca_provavel: a fonte só traz o ano (2020); possivelmente CEBRASPE, não confirmado"],
    },
    # ------------------------------------------------------------------ E1-0234 (4)
    {
        "id": "ECO-E1-0234-4", "fonte_ref": "E1-0234", "destino": "03", "subtema": H2["pmin"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2020", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": COMANDO_MACAS, "excerto": EXCERTO_MACAS,
        "rotulo_item": "Item",
        "assertiva": ("Um mês depois da data do texto, uma epidemia assolou o país e reduziu a população em 40%. "
                      "Para evitar uma crise no setor de maçãs, o governo fixou o preço das maçãs em $ 5 por "
                      "quilo. Com isso, conclui-se que a quantidade semanal vendida de maçãs será a mesma de antes "
                      "da epidemia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um mês depois da data do texto, uma epidemia assolou o país e reduziu a população em 40%. "
                      "Para evitar uma crise no setor de maçãs, o governo fixou o preço das maçãs em $ 5 por "
                      "quilo. Com isso, conclui-se que a quantidade semanal vendida de maçãs será ")
                   + vm("a mesma") + az(" de antes da epidemia."),
        "poucas": ("Com 40% menos consumidores, a demanda cai e o equilíbrio iria abaixo de $ 5. Fixado em $ 5, "
                   "o preço vira " + azb("preço mínimo") + " efetivo: vende-se só o que os consumidores "
                   "restantes compram — " + vd("menos") + " que antes — e sobra maçã."),
        "destrinchando": [
            "Queda da população = menos compradores → " + azb("demanda desloca-se para a esquerda") + " (D₁ → "
            "D₂). Livre, o mercado iria a um novo equilíbrio com preço e quantidade menores.",
            "Fixar o preço no nível antigo ($ 5) transforma-o num " + azb("piso acima do equilíbrio") + ". "
            "Nesse preço, os produtores continuam querendo vender o mesmo (a oferta não mudou), mas os "
            "consumidores compram menos: " + vd("excesso de oferta") + ".",
            "Quem limita a quantidade transacionada num piso é a <b>demanda</b> (ninguém é obrigado a "
            "comprar). No exemplo do gráfico: antes, 10 unidades a $ 5; depois da epidemia, ao mesmo $ 5, "
            "demandam-se só " + vd("6") + " — e os produtores ofertam 10.",
            "Para sustentar o piso sem estoques apodrecendo, o governo teria de comprar o excedente (como na "
            "política de preços mínimos agrícolas) ou restringir a produção. Peso morto e transferências "
            "aparecem em qualquer caso.",
            vm("Regra-âncora: num preço mínimo efetivo, vende-se a quantidade demandada; num preço máximo "
               "efetivo, a quantidade ofertada — sempre o lado curto do mercado."),
        ],
        "grafico_verso": "ECO-E1-0234-4-V1",
        "dissecando": (cz("[nexo indevido]") + " O item supõe que manter o preço mantém a quantidade, como se "
                       "o preço fosse a única variável do mercado. Esquece que a curva de demanda mudou de "
                       "lugar. 🔥 Preço fixado “para evitar crise” após choque é a deixa clássica para "
                       "excesso de oferta (piso) ou escassez (teto)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…conclui-se que haverá excesso de oferta de maçãs ao preço fixado.”</i> → CERTO",
            "<i>“…conclui-se que a quantidade vendida será limitada pela oferta, gerando escassez.”</i> → "
            "ERRADO (troca de conceito: é piso, logo excesso de oferta)",
        ])],
        "reescrita": ("Um mês depois da data do texto, uma epidemia assolou o país e reduziu a população em 40%. "
                      "Para evitar uma crise no setor de maçãs, o governo fixou o preço das maçãs em $ 5 por "
                      "quilo. Com isso, conclui-se que a quantidade semanal vendida de maçãs será "
                      + hl("menor que a") + " de antes da epidemia" + hl(", com excesso de oferta") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Errado. A queda da população reduz a demanda; espera-se queda do preço de "
                            "equilíbrio. Mantido o preço mínimo no nível anterior, o efeito é excesso de oferta e "
                            "menor quantidade demandada.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: classificação sem gabarito; adotado o da fonte (errado)",
                    "banca_provavel: a fonte só traz o ano (2020); possivelmente CEBRASPE, não confirmado"],
    },
    # ------------------------------------------------------------------ E2-L00336
    {
        "id": "ECO-E2-L00336-1", "fonte_ref": "E2-L00336", "destino": "01", "subtema": H2["fpp"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo à fronteira de possibilidades de produção.",
        "rotulo_item": "Item",
        "assertiva": ("Considere uma economia com dois setores que produzem bens utilizando capital e trabalho. "
                      "Mesmo que ambos os setores apresentem retornos constantes de escala individualmente, a "
                      "Fronteira de Possibilidades de Produção (FPP) dessa economia será côncava em relação à "
                      "origem se as intensidades de uso dos fatores (razão capital/trabalho) forem diferentes "
                      "entre os setores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere uma economia com dois setores que produzem bens utilizando capital e trabalho. "
                      "<u>Mesmo que</u> ambos os setores apresentem retornos constantes de escala "
                      "individualmente, a Fronteira de Possibilidades de Produção (FPP) dessa economia será "
                      "côncava em relação à origem <u>se as intensidades de uso dos fatores</u> (razão "
                      "capital/trabalho) <u>forem diferentes</u> entre os setores."),
        "poucas": ("Com intensidades fatoriais distintas, os fatores liberados por um setor não vêm na proporção "
                   "que o outro deseja: a realocação enfrenta " + azb("produtividade marginal decrescente") +
                   " e o " + azb("custo de oportunidade cresce") + " — FPP côncava, mesmo com retornos "
                   "constantes de escala."),
        "destrinchando": [
            "Suponha que alimentos sejam intensivos em trabalho e aço, em capital. Para produzir mais aço, a "
            "economia tira recursos dos alimentos — que liberam muito trabalho e pouco capital. O setor de aço "
            "precisa absorver esse trabalho com capital relativamente escasso: a razão K/L cai nos dois "
            "setores, e o " + azb("produto marginal") + " dos fatores no aço diminui a cada transferência.",
            "Resultado: cada tonelada adicional de aço custa mais alimentos que a anterior — "
            + azb("custo de oportunidade crescente") + ", isto é, " + vd("FPP côncava") + ". Em equilíbrio "
            "competitivo, isso aparece como mudança dos preços relativos dos fatores (" + oc("Stolper-"
            "Samuelson") + ").",
            "Caso-limite: se os dois setores usassem capital e trabalho <b>na mesma proporção</b> (e retornos "
            "constantes), os recursos poderiam ser transferidos “em bloco”, sem perda: a FPP seria uma "
            "<b>reta</b> (custo de oportunidade constante, como no modelo ricardiano de um fator).",
            "É a base do modelo de " + oc("Heckscher-Ohlin") + ": dois fatores, intensidades distintas, FPP "
            "côncava e especialização incompleta com o comércio.",
            vm("Regra-âncora: retornos constantes de escala não garantem FPP reta; o que encurva a FPP é a "
               "diferença de intensidade fatorial (ou a imperfeita adaptabilidade dos recursos)."),
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " O “mesmo que” provoca: quem associa concavidade só a "
                       "rendimentos <b>de escala</b> decrescentes marca ERRADO. Os rendimentos que importam "
                       "aqui são os <b>marginais</b> de cada fator, que caem quando a razão K/L muda. Ver também "
                       "o item CEBRASPE (TJ/PA 2025) que liga concavidade a rendimentos marginais "
                       "decrescentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se ambos os setores tiverem retornos constantes de escala e a mesma razão capital/trabalho, a "
            "FPP será linear.”</i> → CERTO",
            "<i>“Retornos constantes de escala nos dois setores implicam, necessariamente, FPP linear.”</i> → "
            "ERRADO (modulador absoluto: depende das intensidades fatoriais)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["mesmo que", "se"], "dificuldade": 3,
        "comentario_fonte": "CERTO. Resultado da teoria de comércio (Heckscher-Ohlin) e equilíbrio geral: com "
                            "intensidades fatoriais diferentes, a realocação enfrenta rendimentos decrescentes, "
                            "custo de oportunidade crescente e FPP côncava; seria linear com intensidades "
                            "idênticas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00481
    {
        "id": "ECO-E2-L00481-1", "fonte_ref": "E2-L00481", "destino": "01", "subtema": H2["of"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à teoria microeconômica, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considerada a expectativa de que o preço da soja aumente daqui a 6 meses, é correto "
                      "afirmar que, na visão do produtor, no mercado da soja, hoje, haverá um deslocamento da "
                      "curva de oferta para esquerda, definindo-se um novo ponto de equilíbrio com preços mais "
                      "elevados."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerada a expectativa de que o preço da soja aumente daqui a 6 meses, é correto "
                      "afirmar que, <u>na visão do produtor</u>, no mercado da soja, hoje, haverá um deslocamento "
                      "da curva de oferta para esquerda, definindo-se um novo ponto de equilíbrio com preços mais "
                      "elevados."),
        "poucas": ("Soja é estocável: se o preço vai subir, o produtor " + azb("retém parte da safra") + " para "
                   "vender depois. A oferta de hoje cai (curva para a esquerda) e o preço presente sobe."),
        "destrinchando": [
            azb("Expectativas") + " são determinante da oferta (e da demanda). Com bem estocável, vender hoje "
            "ou daqui a seis meses é uma escolha intertemporal: a expectativa de preço futuro maior eleva o "
            "custo de oportunidade de vender agora.",
            "Efeito no mercado presente: O₁ → O₂ (esquerda), " + vd("preço ↑") + " e " + vd("quantidade ↓") +
            " hoje. Esse mecanismo aproxima os preços presente e futuro: as expectativas tendem a se "
            "realizar em parte já no presente.",
            "O recorte “na visão do produtor” é deliberado. Do lado dos compradores (tradings, esmagadoras), a "
            "mesma expectativa leva a antecipar compras: a <b>demanda</b> de hoje também sobe, reforçando a "
            "alta do preço (e deixando a quantidade indeterminada).",
            "A lógica vale para bens armazenáveis (grãos, petróleo, minérios). Para perecíveis, reter "
            "produção não é opção, e o efeito sobre a oferta presente é fraco.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " Intuição apressada: “preço vai subir → produtor "
                       "quer produzir mais → oferta para a direita”. O item cobra o horizonte: hoje, a oferta "
                       "cai; o aumento de plantio é decisão para a safra futura. A expressão “na visão do "
                       "produtor” isola um só lado do mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A expectativa de alta futura do preço da soja desloca hoje a curva de oferta para a direita, "
            "pois estimula a produção.”</i> → ERRADO (inversão: no presente o produtor retém estoques)",
            "<i>“Na visão dos compradores, a expectativa de alta futura do preço tende a elevar a demanda "
            "presente por soja.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "CERTO. Expectativa de preços futuros é determinante da oferta; com bem estocável, "
                            "produtores retêm parte da produção atual; contração da oferta presente, deslocamento "
                            "para a esquerda e preços mais altos hoje.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00746
    {
        "id": "ECO-E2-L00746-1", "fonte_ref": "E2-L00746", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COMANDO_NABUCO_3,
        "frente_figuras": ["ECO-E2-L00746-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por uma redução do preço do bem x."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão ")
                   + vm("pode ser explicado") + az(" por uma redução do preço do bem x."),
        "poucas": ("Variação no preço do <b>próprio</b> bem não desloca a curva de demanda: provoca "
                   + azb("movimento ao longo") + " dela. A curva só se desloca quando muda outro determinante."),
        "destrinchando": [
            "A curva de demanda é o gráfico de q<sub>d</sub> = f(p) <i>mantido o resto constante</i> (renda, "
            "preços de outros bens, gostos, expectativas, número de consumidores). O próprio preço já está "
            "<b>nos eixos</b>: quando ele muda, o consumidor apenas escolhe outro ponto da mesma curva.",
            "Vocabulário que a banca cobra: " + azb("variação da quantidade demandada") + " (movimento ao "
            "longo, causado pelo preço do próprio bem) × " + azb("variação da demanda") + " (deslocamento da "
            "curva, causado por qualquer outro determinante).",
            "Para ir de D1 a D2 (mais quantidade a cada preço) servem: aumento de renda se x for normal; "
            "queda de renda se x for inferior; alta do preço de um substituto; queda do preço de um "
            "complementar; mudança de gostos a favor de x; mais consumidores; expectativa de alta futura do "
            "preço de x.",
            vm("Regra-âncora: preço do próprio bem → anda na curva; qualquer outra causa → a curva anda."),
        ],
        "grafico_verso": "ECO-E2-L00746-1-V1",
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item troca “variação da demanda” por "
                       "“variação da quantidade demandada”: atribui o deslocamento à única variável que, por "
                       "construção, não pode deslocá-la. Pista: o enunciado fala em curva que <b>se desloca</b> "
                       "e oferece como causa o preço do próprio bem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…pode ser explicado por uma redução do preço de um bem substituto de x…”</i> → ERRADO "
            "(sentido trocado: deslocaria para a esquerda)",
            "<i>“…pode ser explicado por uma redução do preço de um bem complementar de x…”</i> → CERTO",
        ])],
        "reescrita": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão "
                      + hl("não pode ser explicado") + " por uma redução do preço do bem x" + hl(", que "
                      "provocaria apenas movimento ao longo de D1") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "O deslocamento para a direita significa aumento da quantidade demandada a cada "
                            "preço, causado por fatores que não o próprio preço (renda, preços de bens "
                            "relacionados). Mudanças no preço do próprio bem provocam movimento ao longo da curva.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 109", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada"}],
        "alertas": ["figura_conjectural: ECO-E2-L00746-1-F1 redesenhada a partir da descrição (D1 e D2 "
                    "paralelas e decrescentes, seta para a direita); posição exata das retas não preservada"],
    },
    # ------------------------------------------------------------------ E2-L00747
    {
        "id": "ECO-E2-L00747-1", "fonte_ref": "E2-L00747", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COMANDO_NABUCO_3,
        "frente_figuras": ["ECO-E2-L00746-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento no preço do bem y, se este for complementar do bem x."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento no preço do bem y, se este for ") + vm("complementar")
                   + az(" do bem x."),
        "poucas": ("Se y é " + azb("complementar") + " de x, encarecer y <b>reduz</b> a demanda por x (curva "
                   "para a esquerda). O deslocamento para a direita exigiria y " + azb("substituto") + "."),
        "destrinchando": [
            "Bens relacionados se classificam pela " + azb("elasticidade-preço cruzada") + " ε<sub>xy</sub> = "
            "%Δq<sub>x</sub> / %Δp<sub>y</sub>: " + vd("ε > 0") + " → substitutos (café × chá); "
            + vd("ε < 0") + " → complementares (carro × gasolina); ε = 0 → independentes.",
            "Complementares são consumidos juntos: se y encarece, o “pacote” x + y fica mais caro e o "
            "consumidor compra menos dos dois. A demanda de x cai a cada preço de x — deslocamento para a "
            "<b>esquerda</b>.",
            "Substitutos competem pela mesma necessidade: se y encarece, parte do consumo migra para x, e a "
            "demanda de x sobe — deslocamento para a <b>direita</b>, como no Gráfico 1.",
            "Atenção ao objeto: o preço de y aparece no gráfico de x como <b>deslocador</b>; no gráfico de y, "
            "o mesmo aumento seria movimento ao longo da curva de y.",
        ],
        "grafico_verso": "ECO-E2-L00747-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O mecanismo (preço de outro bem desloca a curva) está "
                       "certo; o erro está só no rótulo da relação: “complementar” no lugar de “substituto”. "
                       "Itens desse tipo se resolvem pelo sinal: ↑p<sub>y</sub> + complementar = "
                       "↓D<sub>x</sub>."),
        "modulos": [("🧠 Mnemônico", ["<b>C</b>omplementar <b>C</b>ai junto; <b>S</b>ubstituto <b>S</b>obe o "
                                      "outro."])],
        "reescrita": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento no preço do bem y, se este for " + hl("substituto") + " do bem x."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode", "se"], "dificuldade": 1,
        "comentario_fonte": "Complementares: ao aumentar o preço de um, a demanda pelo outro diminui; "
                            "substitutos: aumenta. O deslocamento seria explicado se y fosse substituto, não "
                            "complementar.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 109", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (figura compartilhada ECO-E2-L00746-1-F1)"}],
        "alertas": ["figura_conjectural: ECO-E2-L00746-1-F1 (mesma figura do item 1)"],
    },
    # ------------------------------------------------------------------ E2-L00748
    {
        "id": "ECO-E2-L00748-1", "fonte_ref": "E2-L00748", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COMANDO_NABUCO_3,
        "frente_figuras": ["ECO-E2-L00746-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento na renda, se x for um bem inferior."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento na renda, se x for um bem ") + vm("inferior") + az("."),
        "poucas": ("Para bem " + azb("inferior") + ", renda maior <b>reduz</b> a demanda (curva para a "
                   "esquerda). D1 → D2 com aumento de renda exige bem " + azb("normal") + "."),
        "destrinchando": [
            "A classificação pela renda usa a " + azb("elasticidade-renda") + " η = %Δq / %Δm: " + vd("η > 0") +
            " → bem normal (η > 1: superior ou de luxo; 0 < η < 1: necessário); " + vd("η < 0") + " → bem "
            "inferior.",
            "Bem inferior é aquele trocado por versões melhores quando a renda permite: transporte coletivo "
            "lotado, carne de segunda, produtos de marca genérica. Com mais renda, compra-se menos dele a cada "
            "preço.",
            "Combinações que levam a D1 → D2 (direita): ↑renda e bem normal; <b>↓renda e bem inferior</b>. "
            "Combinações que levariam para a esquerda: ↑renda e bem inferior (o caso do item); ↓renda e bem "
            "normal.",
            "Não confundir inferior com " + azb("bem de Giffen") + ": todo Giffen é inferior, mas quase nenhum "
            "inferior é Giffen. A inferioridade diz respeito à renda (deslocamento da curva); o Giffen, à "
            "inclinação positiva da própria curva.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mesma estrutura dos itens irmãos: o deslocador (renda) é "
                       "legítimo, a classificação do bem é a errada. Resolva pelo sinal: ↑m × (η < 0) = ↓D."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…pode ser explicado por uma redução na renda, se x for um bem inferior.”</i> → CERTO",
            "<i>“…pode ser explicado por um aumento na renda, se x for um bem de Giffen.”</i> → ERRADO (Giffen "
            "é inferior: a demanda cairia)",
        ])],
        "reescrita": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento na renda, se x for um bem " + hl("normal") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode", "se"], "dificuldade": 1,
        "comentario_fonte": "Bem inferior: aumento de renda reduz a demanda; bem normal: aumenta. O deslocamento "
                            "para a direita seria explicado por aumento de renda se x fosse normal, não inferior.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 109", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (figura compartilhada ECO-E2-L00746-1-F1)"}],
        "alertas": ["figura_conjectural: ECO-E2-L00746-1-F1 (mesma figura do item 1)"],
    },
    # ------------------------------------------------------------------ E2-L00749
    {
        "id": "ECO-E2-L00749-1", "fonte_ref": "E2-L00749", "destino": "01", "subtema": H2["of"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COMANDO_NABUCO_3,
        "frente_figuras": ["ECO-E2-L00746-1-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por uma redução dos preços dos insumos utilizados na produção do bem x."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por ") + vm("uma redução dos preços dos insumos utilizados na produção do bem x")
                   + az("."),
        "poucas": ("Preço de insumo é determinante da " + azb("oferta") + ", não da demanda: insumo mais barato "
                   "desloca a curva de oferta de x para a direita e deixa a curva de demanda onde está."),
        "destrinchando": [
            "Cada curva tem seus deslocadores. " + azb("Demanda") + ": renda, preços de bens relacionados, "
            "gostos, expectativas dos compradores, número de consumidores. " + azb("Oferta") + ": preço dos "
            "insumos, tecnologia, tributos e subsídios, expectativas dos vendedores, número de produtores.",
            "Insumo mais barato reduz o custo marginal: a oferta vai para a direita, o preço de x cai e a "
            "quantidade sobe. Do ponto de vista da demanda, o que houve foi <b>movimento ao longo</b> de D1 "
            "(mais quantidade demandada porque o preço caiu) — nunca o salto de D1 para D2.",
            "É o mesmo erro do item 1 desta questão por outro caminho: o efeito final (preço menor de x) "
            "provoca movimento, não deslocamento da demanda.",
            vm("Regra-âncora: custo de produção mexe na oferta; o bolso e o gosto do consumidor mexem na "
               "demanda."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca a curva: oferece um deslocador de oferta para "
                       "explicar um deslocamento de demanda. A frase soa plausível porque “insumo barato → bem "
                       "barato → mais consumo” é verdadeiro, só que como movimento ao longo de D1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução dos preços dos insumos utilizados na produção de x desloca a curva de oferta de x "
            "para a direita.”</i> → CERTO",
            "<i>“…pode ser explicado por uma redução da renda dos consumidores, se x for um bem normal.”</i> → "
            "ERRADO (sentido trocado: deslocaria para a esquerda)",
        ])],
        "reescrita": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por " + hl("um aumento do número de consumidores do bem x; a redução dos preços "
                      "dos insumos deslocaria a curva de oferta") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Preço dos insumos é determinante da oferta e não da demanda; sua redução desloca a "
                            "curva de oferta do bem x, e não a de demanda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 109", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (figura compartilhada ECO-E2-L00746-1-F1)"}],
        "alertas": ["figura_conjectural: ECO-E2-L00746-1-F1 (mesma figura do item 1)"],
    },
    # ------------------------------------------------------------------ E2-L00885
    {
        "id": "ECO-E2-L00885-1", "fonte_ref": "E2-L00885", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Em relação aos princípios da teoria do consumidor e da teoria da demanda, julgue o item que "
                    "se segue."),
        "rotulo_item": "Item",
        "assertiva": "A demanda de um bem normal é função crescente do preço do bem substituto.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A demanda de um bem normal é função <u>crescente</u> do preço do bem <u>substituto</u>."),
        "poucas": ("Substitutos têm " + azb("elasticidade-preço cruzada positiva") + ": se o substituto "
                   "encarece, a demanda pelo bem aumenta. Logo, ela cresce com o preço do substituto."),
        "destrinchando": [
            "Função demanda: q<sub>x</sub> = f(p<sub>x</sub>, p<sub>y</sub>, m, gostos…). Para substitutos, "
            + vd("∂q<sub>x</sub>/∂p<sub>y</sub> > 0") + "; para complementares, < 0; para independentes, = 0.",
            "Exemplo brasileiro: " + rx("etanol × gasolina") + " no carro flex. Se a gasolina sobe, parte dos "
            "motoristas migra para o etanol — a demanda de etanol se desloca para a direita (a regra prática "
            "dos 70% do preço da gasolina).",
            "O “bem normal” do item é um detalhe que não muda o resultado: a relação com o preço do "
            "substituto vale para bem normal ou inferior. O que define normal/inferior é a reação à "
            "<b>renda</b>, não ao preço de outros bens.",
            "Em termos gráficos: o preço do substituto é um <b>deslocador</b> da curva de demanda de x; o "
            "preço de x é que provoca movimento ao longo dela.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " A banca põe “bem normal” para criar dúvida (quem acha "
                       "que é condição necessária pode desconfiar). “Função crescente de p<sub>y</sub>” é só a "
                       "tradução de ε<sub>xy</sub> > 0."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda de um bem normal é função crescente do preço do bem complementar.”</i> → ERRADO "
            "(troca de conceito: é decrescente)",
            "<i>“A demanda de um bem inferior é função decrescente do preço do bem substituto.”</i> → ERRADO "
            "(a inferioridade não inverte a relação cruzada)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. Elasticidade-preço cruzada positiva para substitutos: se o preço de um "
                            "aumenta, a demanda pelo outro aumenta (gasolina e etanol).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00973
    {
        "id": "ECO-E2-L00973-1", "fonte_ref": "E2-L00973", "destino": "01", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": ("Em relação à microeconomia e à teoria do comércio internacional, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("No mercado de um bem inferior, ocorre um choque que diminui a renda dos consumidores desse "
                      "bem. Assumindo tudo o mais constante, após o choque ocorre redução da quantidade "
                      "transacionada e do preço de equilíbrio do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No mercado de um bem inferior, ocorre um choque que diminui a renda dos consumidores desse "
                      "bem. Assumindo tudo o mais constante, após o choque ocorre ")
                   + vm("redução") + az(" da quantidade transacionada e do preço de equilíbrio do bem."),
        "poucas": ("Bem " + azb("inferior") + " + renda menor = demanda <b>maior</b> (curva para a direita). Com "
                   "oferta inalterada, sobem " + vd("preço e quantidade") + "."),
        "destrinchando": [
            "Passo 1 — qual curva? A renda é deslocador da demanda. Passo 2 — para que lado? Bem inferior tem "
            "elasticidade-renda negativa: ↓renda → ↑demanda. Passo 3 — efeito no equilíbrio: choque positivo "
            "de demanda → " + vd("p ↑ e q ↑") + ".",
            "Intuição: com menos renda, consumidores abandonam versões mais caras e voltam ao bem inferior "
            "(ônibus no lugar do carro, marca própria no lugar da marca líder).",
            "O resultado do item (p ↓ e q ↓) seria correto para um bem <b>normal</b>: menos renda, menos "
            "demanda.",
            "Aplicação: em recessões, bens inferiores costumam ter demanda resiliente ou crescente, e alguns "
            "setores são chamados de anticíclicos por isso.",
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item aplica a um bem inferior o resultado do "
                       "bem normal. Duas negativas (renda ↓ e η < 0) produzem um efeito positivo — quem lê "
                       "rápido erra o sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mercado de um bem normal, a queda da renda reduz o preço e a quantidade de "
            "equilíbrio.”</i> → CERTO",
            "<i>“No mercado de um bem inferior, a queda da renda eleva o preço, mas reduz a quantidade "
            "transacionada.”</i> → ERRADO (meia-verdade: a quantidade também sobe)",
        ])],
        "reescrita": ("No mercado de um bem inferior, ocorre um choque que diminui a renda dos consumidores desse "
                      "bem. Assumindo tudo o mais constante, após o choque ocorre " + hl("aumento") + " da "
                      "quantidade transacionada e do preço de equilíbrio do bem."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Se o bem é inferior, a diminuição de renda aumenta a demanda, aumentando a "
                            "quantidade transacionada e o preço de equilíbrio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01035
    {
        "id": "ECO-E2-L01035-1", "fonte_ref": "E2-L01035", "destino": "01", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COMANDO_EQ,
        "rotulo_item": "Item",
        "assertiva": ("Em equilíbrio, sem intervenção governamental, a quantidade de produto transacionado no "
                      "mercado será de 90 unidades, e o preço praticado será de R$ 7,00 por unidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em equilíbrio, sem intervenção governamental, a quantidade de produto transacionado no "
                      "mercado será de <u>90 unidades</u>, e o preço praticado será de <u>R$ 7,00</u> por "
                      "unidade."),
        "poucas": ("Igualando Qᴰ = Qˢ: 300 − 30p = 10p + 20 → " + vd("p* = 7") + " e, substituindo, "
                   + vd("Q* = 90") + "."),
        "destrinchando": [
            "Equilíbrio = preço em que os planos de compradores e vendedores são compatíveis (Qᴰ = Qˢ). "
            "Conta: 300 − 20 = 30p + 10p → 280 = 40p → " + vd("p = 7") + ".",
            "Quantidade: Qᴰ = 300 − 210 = " + vd("90") + "; confira na oferta: Qˢ = 70 + 20 = 90. Sempre "
            "substitua nas <b>duas</b> curvas — a conferência pega erro de sinal.",
            "Atalhos de prova: interceptos. A demanda zera em " + vd("p = 10") + " (preço de reserva); a "
            "oferta começa em Q = 20 com p = 0. Daí saem os excedentes: consumidor = (10 − 7) × 90 ÷ 2 = "
            + vd("135") + ".",
            "Fora do equilíbrio: p > 7 → excesso de oferta (pressão para baixo); p < 7 → excesso de demanda. "
            "Ex.: com preço tabelado em 6, Qᴰ = 120 e Qˢ = 80 — faltam 40 unidades.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de cálculo direto, que abre a bateria da questão (excedentes e "
                       "tabelamento vêm em seguida). Os erros típicos que a banca exploraria: inverter p e Q "
                       "(“7 unidades a R$ 90”) ou errar o sinal na passagem de termos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em equilíbrio, o excedente do consumidor é de R$ 270,00.”</i> → ERRADO (esqueceu o ÷ 2: são "
            "R$ 135,00)",
            "<i>“Se o preço for fixado em R$ 8,00, haverá excesso de oferta de 40 unidades.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. Igualando 300 − 30p = 10p + 20 → p = 7; QD = 300 − 210 = 90.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 174", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "texto (equações transcritas no comando)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01373
    {
        "id": "ECO-E2-L01373-1", "fonte_ref": "E2-L01373", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "FGV", "prova": "SEFAZ/ES/Consultor Legislativo/2022", "ano": 2022,
        "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir (questão adaptada), relativo aos fatores de produção e às suas remunerações.",
        "rotulo_item": "Item",
        "assertiva": ("São remunerações do trabalho, da terra e do capital, respectivamente, salário, aluguel, e "
                      "juros e lucros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("São remunerações do trabalho, da terra e do capital, <u>respectivamente</u>, salário, "
                      "aluguel, e juros e lucros."),
        "poucas": ("Na repartição funcional da renda: " + vd("trabalho → salário") + "; " + vd("terra → "
                   "aluguel (renda da terra)") + "; " + vd("capital → juros e lucros") + ". A ordem do item "
                   "está correta."),
        "destrinchando": [
            "Os fatores de produção clássicos e suas remunerações: " + azb("trabalho") + " → salários; "
            + azb("terra") + " (recursos naturais) → aluguel ou renda da terra; " + azb("capital") + " "
            "(máquinas, instalações) → juros (e lucros); " + azb("capacidade empresarial") + " → lucro.",
            "Por que “juros e lucros” para o capital: muitos manuais tratam o lucro como retorno do capital "
            "próprio investido; outros o reservam ao fator empresarial (que assume o risco e organiza a "
            "produção). O item adaptado adota a primeira leitura, e o gabarito a aceita.",
            "Na contabilidade nacional, essa divisão aparece na ótica da renda: remuneração dos empregados + "
            "excedente operacional bruto (aluguéis, juros, lucros) + rendimento misto.",
            "Origem da classificação: economia política clássica — " + oc("Adam Smith") + " e " + oc("David "
            "Ricardo") + " dividem a renda entre trabalhadores (salários), proprietários de terras (renda) e "
            "capitalistas (lucros).",
        ],
        "dissecando": (cz("[literalidade]") + " O item testa a ordem (“respectivamente”), que é onde a banca "
                       "costuma plantar o erro trocando aluguel e juros. A marca ❌ provavelmente veio da "
                       "dúvida sobre o lucro, que alguns autores atribuem só ao empresário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“São remunerações do trabalho, da terra e do capital, respectivamente, salário, juros e "
            "aluguel.”</i> → ERRADO (ordem trocada: terra → aluguel; capital → juros)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["respectivamente"], "dificuldade": 1,
        "comentario_fonte": "CERTO. Diagrama: trabalho → salário; terra → aluguel; capital → juros e lucros; "
                            "capacidade empresarial → lucros.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 248", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01374
    {
        "id": "ECO-E2-L01374-1", "fonte_ref": "E2-L01374", "destino": "01", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "FGV", "prova": "SEFAZ/ES/Consultor Legislativo/2022", "ano": 2022,
        "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir (questão adaptada), relativo à classificação dos bens.",
        "rotulo_item": "Item",
        "assertiva": ("Assuma uma economia de dois bens (x1 e x2). Se x1 é um bem inferior, então necessariamente "
                      "x2 é um bem normal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Assuma uma economia de dois bens (x1 e x2). Se x1 é um bem inferior, então "
                      "<u>necessariamente</u> x2 é um bem normal."),
        "poucas": ("Toda renda extra tem de ser gasta em algum bem. Se o gasto com x1 <b>cai</b> quando a renda "
                   "sobe, o gasto com x2 tem de subir mais que a renda: x2 é " + azb("normal") + " (na verdade, "
                   "de luxo)."),
        "destrinchando": [
            "Com preferências monótonas, o consumidor gasta toda a renda: p₁x₁ + p₂x₂ = m. Derivando em m: "
            + vd("p₁·∂x₁/∂m + p₂·∂x₂/∂m = 1") + " — cada real adicional é repartido entre os bens.",
            "Se x₁ é inferior, ∂x₁/∂m < 0: o primeiro termo é negativo, e o segundo precisa ser maior que 1. "
            "Logo ∂x₂/∂m > 0 — x₂ é normal. Os dois não podem ser inferiores (sobraria renda sem destino).",
            "Em elasticidades, é a " + azb("agregação de Engel") + ": s₁η₁ + s₂η₂ = 1 (s = parcela do gasto). "
            "Com η₁ < 0, " + vd("η₂ > 1/s₂ > 1") + ": x₂ é não só normal, mas " + azb("bem de luxo") + ".",
            "Generalizando: com n bens, nem todos podem ser inferiores; a média ponderada das "
            "elasticidades-renda é sempre 1.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " O “necessariamente” assusta, porque a banca costuma usá-lo "
                       "para itens falsos. Aqui ele é verdadeiro por uma restrição contábil (a renda tem de ir "
                       "para algum lugar). Pista: “economia de dois bens”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Numa economia de dois bens, ambos podem ser inferiores.”</i> → ERRADO (a renda adicional "
            "precisa ser gasta)",
            "<i>“Numa economia de dois bens, se x1 é inferior, x2 tem elasticidade-renda maior que 1.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["necessariamente"], "dificuldade": 2,
        "comentario_fonte": "CERTO. Se os dois fossem inferiores, ao aumentar a renda sobraria dinheiro, o que a "
                            "teoria não permite.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01379
    {
        "id": "ECO-E2-L01379-1", "fonte_ref": "E2-L01379", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "SESPA/PA/Economista/2004", "ano": 2004,
        "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo aos fundamentos da economia.",
        "rotulo_item": "Item",
        "assertiva": ("Os consumidores devem fazer escolhas em razão da existência de mapas de preferências "
                      "distintos entre os indivíduos de uma sociedade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os consumidores devem fazer escolhas em razão da ") + vm("existência de mapas de "
                      "preferências distintos entre os indivíduos de uma sociedade") + az("."),
        "poucas": ("Escolher é imposto pela " + azb("escassez") + " (renda limitada diante de desejos "
                   "ilimitados), não pela diversidade de preferências. Um consumidor sozinho no mundo também "
                   "teria de escolher."),
        "destrinchando": [
            "O " + azb("problema econômico fundamental") + ": necessidades ilimitadas × recursos escassos. "
            "Daí as perguntas clássicas — o que, quanto, como e para quem produzir — e a necessidade de "
            "escolha, com " + azb("custo de oportunidade") + ".",
            "No consumidor, a escassez é a " + azb("restrição orçamentária") + ": com preços dados e renda "
            "finita, comprar mais de um bem exige comprar menos de outro.",
            "O " + azb("mapa de indiferença") + " descreve as preferências <b>de cada</b> consumidor e diz "
            "<b>como</b> ele escolhe (qual cesta prefere), não <b>por que</b> precisa escolher. Preferências "
            "diferentes explicam por que as pessoas fazem escolhas diferentes — e por que a troca gera ganho "
            "—, mas não são a origem da escolha.",
            vm("Regra-âncora: a escolha nasce da escassez; as preferências só determinam qual será a escolha."),
        ],
        "dissecando": (cz("[nexo indevido]") + " Dois fatos verdadeiros (consumidores escolhem; preferências "
                       "diferem) ligados por uma causalidade falsa (“em razão da”). O conector é o ponto a "
                       "atacar. 🔥 A CEBRASPE gosta de itens de fundamentos que trocam a causa da escolha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os consumidores devem fazer escolhas em razão da escassez de recursos diante de necessidades "
            "ilimitadas.”</i> → CERTO",
            "<i>“Se todos os indivíduos tivessem as mesmas preferências, não haveria necessidade de "
            "escolha.”</i> → ERRADO (a escassez continuaria a impor escolhas)",
        ])],
        "reescrita": ("Os consumidores devem fazer escolhas em razão da " + hl("escassez de recursos (renda "
                      "limitada) diante de necessidades ilimitadas") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["em razão da"], "dificuldade": 1,
        "comentario_fonte": "ERRADO. O erro está no “em razão da…”: não é porque os consumidores possuem "
                            "preferências diferentes que devem fazer escolhas, mas porque seus recursos são "
                            "limitados e suas necessidades, infinitas. Mesmo um único consumidor teria de "
                            "escolher.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00009
    {
        "id": "ECO-E3-L00009-1", "fonte_ref": "E3-L00009", "destino": "01", "subtema": H2["fpp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": "Acerca dos conceitos fundamentais de microeconomia, julgue o item que se segue.",
        "rotulo_item": "Item",
        "assertiva": ("A concavidade da fronteira de possibilidades de produção decorre da lei dos rendimentos "
                      "marginais decrescentes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A concavidade da fronteira de possibilidades de produção decorre da lei dos "
                      "<u>rendimentos marginais decrescentes</u>."),
        "poucas": ("FPP côncava = " + azb("custo de oportunidade crescente") + "; e o custo cresce porque os "
                   "recursos transferidos rendem cada vez menos no novo uso — " + azb("rendimentos marginais "
                   "decrescentes") + "."),
        "destrinchando": [
            "A inclinação da FPP é a " + azb("taxa marginal de transformação") + ": quanto de Y se sacrifica "
            "por uma unidade a mais de X. Na FPP côncava, ela cresce à medida que se produz mais X.",
            "Por quê: os recursos não são igualmente aptos a todos os usos. Os primeiros fatores deslocados "
            "para X são os mais adequados a X (e menos produtivos em Y); depois, só restam fatores bons em Y "
            "e ruins em X. Cada unidade adicional de X custa mais Y — o " + azb("produto marginal") + " dos "
            "fatores realocados cai.",
            "Leitura numérica (gráfico): cada 2 unidades extras de X custam " + vd("0,3") + ", depois "
            + vd("0,8") + ", " + vd("1,6") + " e, por fim, " + vd("5,3") + " unidades de Y.",
            "Formas da FPP: côncava → custo de oportunidade crescente (caso usual); reta → constante "
            "(recursos perfeitamente substituíveis, modelo ricardiano); convexa → decrescente (economias de "
            "escala fortes).",
            "Nuance técnica: mesmo com retornos constantes de escala nos dois setores, a FPP é côncava se as "
            "intensidades fatoriais diferirem (" + oc("Heckscher-Ohlin") + "); o mecanismo continua sendo a "
            "queda do produto marginal quando muda a proporção capital/trabalho.",
        ],
        "grafico_verso": "ECO-E3-L00009-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " O item pula um elo: rendimentos decrescentes → custo de "
                       "oportunidade crescente → concavidade. A banca aceita o atalho. A versão ERRADA "
                       "clássica é atribuir a concavidade a rendimentos <b>crescentes</b> ou a custo de "
                       "oportunidade constante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A concavidade da fronteira de possibilidades de produção reflete custos de oportunidade "
            "constantes.”</i> → ERRADO (troca de conceito: constantes dão FPP reta)",
            "<i>“Se os recursos fossem igualmente produtivos em todos os usos, a FPP seria uma reta.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. FPP côncava porque os recursos não são perfeitamente adaptáveis; ao "
                            "realocá-los incidem rendimentos marginais decrescentes, elevando o custo de "
                            "oportunidade (seis respostas convergentes fundidas).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00305
    {
        "id": "ECO-E3-L00305-1", "fonte_ref": "E3-L00305", "destino": "01", "subtema": H2["of"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": ("Considerando as diversas estruturas de mercado, suas semelhanças e diferenças, julgue o item "
                    "a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A curva de oferta de um determinado setor ou indústria, como por exemplo a indústria de "
                      "calçados ou de vestuário, é a soma simples da oferta individual de cada empresa "
                      "participante desse mercado para cada nível de preços praticado por pelo menos uma delas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de oferta de um determinado setor ou indústria, como por exemplo a indústria de "
                      "calçados ou de vestuário, é a <u>soma simples</u> da oferta individual de cada empresa "
                      "participante desse mercado <u>para cada nível de preços</u> praticado por pelo menos uma "
                      "delas."),
        "poucas": ("A oferta de mercado é a " + azb("soma horizontal") + " das ofertas individuais: fixa-se o "
                   "preço e somam-se as quantidades que cada firma oferta a esse preço."),
        "destrinchando": [
            "Soma <b>horizontal</b> porque a quantidade está no eixo horizontal: Q(p) = q<sub>A</sub>(p) + "
            "q<sub>B</sub>(p) + … No gráfico, a p = 8 a firma A oferta 6 e a B, 8; o mercado, "
            + vd("14") + ".",
            "“Pelo menos uma delas”: abaixo do preço de fechamento (CVMe mínimo) a firma oferta zero e não "
            "entra na soma. Por isso a curva de mercado tem uma <b>quebra</b>: entre p = 2 e p = 4 só a "
            "firma A produz; acima de 4, as duas — e a oferta de mercado fica mais plana (mais elástica).",
            "A curva individual vem do custo marginal: em concorrência perfeita, a firma oferta onde "
            + vd("p = CMg") + ", no trecho acima do CVMe mínimo.",
            "Limites: (1) se a expansão do setor encarece insumos (couro, tecido), a oferta da indústria fica "
            "mais inclinada que a soma simples — indústria de custos crescentes; (2) em monopólio e oligopólio "
            "não existe curva de oferta no sentido estrito, pois a firma escolhe o preço.",
            "Contraste: " + azb("soma vertical") + " é a dos bens públicos (somam-se as disposições a pagar, "
            "para a mesma quantidade).",
        ],
        "grafico_verso": "ECO-E3-L00305-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " “Soma simples” é a paráfrase de soma horizontal; o "
                       "trecho final, de redação estranha (firma competitiva não “pratica” preço), só quer dizer "
                       "“a cada preço em que alguma firma oferte”. A banca aposta que o candidato confunda com "
                       "soma vertical ou desconfie da redação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de oferta da indústria é obtida pela soma vertical das curvas de oferta individuais, "
            "somando-se os preços para cada quantidade.”</i> → ERRADO (troca de conceito: soma vertical é a "
            "dos bens públicos)",
            "<i>“Em uma indústria de custos crescentes, a oferta de longo prazo é mais inclinada que a simples "
            "soma das ofertas individuais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "CERTO. Respostas de várias IAs fundidas: oferta de mercado como soma horizontal das "
                            "ofertas individuais para cada preço; nuances sobre preço de fechamento, curto × longo "
                            "prazo, indústria de custos crescentes e estruturas não competitivas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 409", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (exemplo numérico substituído pelo do gráfico)"},
                          {"ref": "IMAGEM 410", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00305-1-V1)"},
                          {"ref": "IMAGEM 411", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00375
    {
        "id": "ECO-E3-L00375-1", "fonte_ref": "E3-L00375", "destino": "01", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": COMANDO_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("A inclinação da curva de demanda individual é negativa para bens normais e bens "
                      "superiores, como os bens de Veblen, pois reflete a lei da demanda, segundo a qual, quando "
                      "o preço de um bem aumenta, a quantidade demandada diminui."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A inclinação da curva de demanda individual é negativa para bens normais e bens "
                      "superiores, ") + vm("como os bens de Veblen") + az(", pois reflete a lei da demanda, "
                      "segundo a qual, quando o preço de um bem aumenta, a quantidade demandada diminui."),
        "poucas": ("Bens de " + azb("Veblen") + " são a exceção, não o exemplo: o preço alto é parte do atrativo "
                   "(status), e a demanda pode ter " + vd("inclinação positiva") + "."),
        "destrinchando": [
            "Para bens normais e superiores (de luxo comuns), a lei da demanda vale: efeito substituição e "
            "efeito renda puxam na mesma direção quando o preço sobe — a quantidade cai.",
            azb("Bem superior") + " é classificação pela <b>renda</b> (elasticidade-renda > 1); " + azb("bem "
            "de Veblen") + " é definido pela relação com o <b>preço</b>: o consumo é " + azb("conspícuo") +
            ", e o preço elevado sinaliza exclusividade. Se a joia ou a bolsa de grife barateia, perde parte "
            "do valor simbólico e pode ser menos demandada.",
            "Origem: " + oc("Thorstein Veblen") + ", <i>A Teoria da Classe Ociosa</i> (1899), sobre o consumo "
            "ostentatório.",
            "As duas exceções à lei da demanda, com causas diferentes: " + azb("Giffen") + " (bem inferior com "
            "efeito renda maior que o substituição; batatas na Irlanda do séc. XIX) e " + azb("Veblen") +
            " (preferências que dependem do próprio preço). Todo Giffen é inferior; o Veblen costuma ser bem "
            "de luxo.",
            vm("Regra-âncora: superior ≠ Veblen — o primeiro fala de renda e obedece à lei da demanda; o "
               "segundo fala de status e a desafia."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item cola um exemplo errado (“como os bens de Veblen”) "
                       "numa frase correta, explorando a associação luxo = superior = Veblen. O “como” "
                       "transforma a exceção em ilustração da regra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os bens de Veblen e os bens de Giffen são exceções à lei da demanda.”</i> → CERTO",
            "<i>“Todo bem superior é um bem de Veblen.”</i> → ERRADO (modulador absoluto: o superior comum "
            "segue a lei da demanda)",
        ])],
        "reescrita": ("A inclinação da curva de demanda individual é negativa para bens normais e bens "
                      "superiores, " + hl("mas não para os bens de Veblen, que constituem exceção") + ", pois "
                      "reflete a lei da demanda, segundo a qual, quando o preço de um bem aumenta, a quantidade "
                      "demandada diminui."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Bens de Veblen são exceções à lei da demanda (inclinação positiva, consumo "
                            "por status); bem superior (elasticidade-renda > 1) não se confunde com Veblen. "
                            "Exceções: Giffen e Veblen (três respostas convergentes fundidas).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 533", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (texto absorvido no 📖)"},
                          {"ref": "IMAGEM 534", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem de terceiros, Shutterstock)"},
                          {"ref": "IMAGEM 535", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00376
    {
        "id": "ECO-E3-L00376-1", "fonte_ref": "E3-L00376", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": COMANDO_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("A curva de demanda individual pode se deslocar para a direita se houver um aumento na renda "
                      "do consumidor, considerando que o bem seja normal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de demanda individual pode se deslocar para a direita se houver um aumento na renda "
                      "do consumidor, considerando que o bem seja <u>normal</u>."),
        "poucas": ("Bem " + azb("normal") + " tem elasticidade-renda positiva: renda maior → mais quantidade "
                   "demandada <b>a cada preço</b> → curva inteira para a direita."),
        "destrinchando": [
            "Com o preço do bem constante (p₁), o consumidor mais rico compra q₂ > q₁. Como isso vale para "
            "todos os preços, a curva toda se desloca — não é movimento ao longo dela.",
            "Formalmente: q = D(p, m, …), com " + vd("∂q/∂m > 0") + " para bem normal. Necessários "
            "(0 < η < 1) e de luxo (η > 1) são ambos normais.",
            "Se o bem fosse " + azb("inferior") + " (η < 0), o mesmo aumento de renda deslocaria a demanda "
            "para a <b>esquerda</b>.",
            "Na teoria do consumidor, o aumento de renda desloca a restrição orçamentária para fora em "
            "paralelo; a curva " + azb("renda-consumo") + " e a " + azb("curva de Engel") + " mostram a "
            "trajetória da quantidade com a renda — crescente para bens normais.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item de manual, com dupla proteção: o "
                       "“pode” e a condição “considerando que o bem seja normal”. A versão ERRADA trocaria "
                       "normal por inferior ou deslocamento por movimento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se houver um aumento na renda do consumidor, considerando que o bem seja inferior.”</i> → "
            "ERRADO (troca de conceito: deslocaria para a esquerda)",
            "<i>“O aumento da renda provoca movimento ao longo da curva de demanda de um bem normal.”</i> → "
            "ERRADO (troca de conceito: é deslocamento)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "CERTO. Para bens normais, o aumento da renda eleva a quantidade demandada a qualquer "
                            "preço, deslocando a curva para a direita (três respostas convergentes fundidas).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 536", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (descrição absorvida no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00377
    {
        "id": "ECO-E3-L00377-1", "fonte_ref": "E3-L00377", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": COMANDO_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Se a taxa para carregamento de carros elétricos em estações públicas é substancialmente "
                      "reduzida, a demanda por este tipo de automóvel tende a aumentar, deslocando sua curva de "
                      "demanda para a direita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a taxa para carregamento de carros elétricos em estações públicas é substancialmente "
                      "reduzida, a demanda por este tipo de automóvel <u>tende a</u> aumentar, deslocando sua "
                      "curva de demanda para a direita."),
        "poucas": ("Recarga e carro elétrico são " + azb("complementares") + ": recarga mais barata reduz o "
                   "custo de usar o carro e aumenta a demanda por ele a cada preço — curva para a direita."),
        "destrinchando": [
            "O preço de um complementar é deslocador da demanda: " + vd("↓p do complementar → ↑D do bem") +
            " (elasticidade-preço cruzada negativa). O preço do próprio carro não mudou, logo não se trata de "
            "movimento ao longo da curva.",
            "Intuição: o consumidor avalia o " + azb("custo total de uso") + " (preço do carro + energia + "
            "manutenção). Barateando a energia, o pacote fica mais atraente — o mesmo vale para impressora e "
            "cartucho, carro a combustão e gasolina.",
            "No mercado de recarga, a redução da taxa é movimento ao longo da demanda por recarga; no "
            "mercado de carros elétricos, é deslocamento. Cada gráfico tem seu bem nos eixos.",
            "Aplicação de política: subsidiar infraestrutura e tarifa de recarga é uma forma indireta de "
            "estimular a compra de elétricos, ao lado de incentivos tributários à própria compra.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Aplicação direta de complementaridade, "
                       "amortecida pelo “tende a”. A banca poderia derrubar o item chamando os bens de "
                       "substitutos ou dizendo que a curva se desloca para a esquerda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a demanda por carros elétricos tende a aumentar, pois recarga e carro elétrico são bens "
            "substitutos.”</i> → ERRADO (troca de conceito: são complementares)",
            "<i>“Um aumento no preço da gasolina tende a deslocar para a direita a demanda por carros "
            "elétricos.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "CERTO. Eletricidade e carros elétricos são complementares; a queda no preço do "
                            "complementar aumenta a demanda do bem principal (três respostas convergentes "
                            "fundidas; dados empíricos não verificados descartados).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 537", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00378
    {
        "id": "ECO-E3-L00378-1", "fonte_ref": "E3-L00378", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": COMANDO_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Considerando que os agentes microeconômicos são racionais e tomam suas decisões "
                      "considerando o princípio conhecido como <i>coeteris paribus</i>, mudanças no preço de um "
                      "bem não afetam a posição da curva de demanda dos bens que são substitutos, uma vez que o "
                      "consumidor avalia cada um deles de forma isolada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando que os agentes microeconômicos são racionais e ") + vm("tomam suas decisões "
                      "considerando o princípio conhecido como") + az(" <i>coeteris paribus</i>, mudanças no "
                      "preço de um bem ") + vm("não afetam") + az(" a posição da curva de demanda dos bens que "
                      "são substitutos, uma vez que o consumidor ") + vm("avalia cada um deles de forma isolada")
                   + az("."),
        "poucas": ("O preço de um " + azb("substituto") + " é justamente um deslocador da demanda: se a manteiga "
                   "encarece, a curva de demanda da margarina vai para a direita. " + azb("Coeteris paribus") +
                   " é hipótese do analista, não regra de decisão do consumidor."),
        "destrinchando": [
            "A curva de demanda de x é traçada mantendo constantes os outros preços. Quando um deles muda, "
            "a hipótese deixa de valer e a curva <b>muda de posição</b>: " + vd("↑p substituto → ↑D") + "; "
            + vd("↑p complementar → ↓D") + ".",
            azb("Coeteris paribus") + " (“tudo o mais constante”) é um recurso de método do economista para "
            "isolar o efeito de uma variável; não descreve como o consumidor decide. O consumidor racional "
            "faz exatamente o contrário do que diz o item: compara os bens entre si, pelos preços relativos.",
            "Exemplo: se a Pepsi sobe de preço, parte dos consumidores passa à Coca-Cola, cuja demanda se "
            "desloca para a direita mesmo com o preço da Coca inalterado.",
            "O que não desloca a curva de x é só o preço do <b>próprio</b> x (movimento ao longo).",
            vm("Regra-âncora: ceteris paribus define o que fica fora dos eixos; quando algo fora dos eixos "
               "muda, a curva se move."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O item usa uma premissa pomposa "
                       "(racionalidade + ceteris paribus) para justificar uma conclusão falsa, e transforma uma "
                       "hipótese de análise em comportamento do consumidor. O “avalia cada um de forma isolada” "
                       "contraria a própria definição de substituto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Mudanças no preço de um bem afetam a posição da curva de demanda de seus substitutos e de seus "
            "complementares.”</i> → CERTO",
            "<i>“O aumento do preço da manteiga desloca para a esquerda a curva de demanda por margarina.”</i> "
            "→ ERRADO (sentido trocado: substituto → direita)",
        ])],
        "reescrita": ("Considerando que os agentes microeconômicos são racionais e " + hl("que a curva de demanda "
                      "é traçada sob a hipótese") + " <i>coeteris paribus</i>, mudanças no preço de um bem "
                      + hl("afetam") + " a posição da curva de demanda dos bens que são substitutos, uma vez que "
                      "o consumidor " + hl("compara os bens entre si, pelos preços relativos") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Mudanças no preço de substitutos deslocam a curva (Pepsi × Coca-Cola; "
                            "manteiga × margarina). O ceteris paribus serve para desenhar a curva mantendo os "
                            "outros preços constantes; quando eles mudam, a curva se move.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 538", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (no 📖)"}],
        "alertas": [],
    },
]
