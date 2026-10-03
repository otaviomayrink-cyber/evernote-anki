"""Cards do lote de redação 09 — ECO, passada 02 (notas 25: modelo clássico/TQM e 26: keynesiano simples)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "cla": "⚙️ Modelo clássico",
    "tqm": "💵 Teoria quantitativa da moeda",
    "de": "📈 Demanda efetiva e cruz keynesiana",
    "mult": "✖️ Multiplicadores",
}

CMD_NAB_MACRO = "Em relação à teoria macroeconômica, julgue o item a seguir."

CMD_NAB_SI = ("A publicação da obra A Teoria Geral do Emprego, do Juro e da Moeda, em 1936, por John Maynard Keynes, "
              "foi fundamental para que os economistas se deparassem com duas das principais abordagens acerca da "
              "relação entre investimento e poupança. As correntes do pensamento econômico apresentam visões "
              "distintas sobre as relações entre o investimento (I) e a poupança (S). Considerando o exposto, julgue "
              "o item seguinte.")

CMD_RT_CLA = "Avalie a afirmação abaixo, relativa ao modelo clássico e ao modelo IS-LM."

CMD_BOZAN_MULT = ("Sobre a estrutura de multiplicação keynesiana, analise a assertiva abaixo e julgue-a como certa ou "
                  "errada.")

CARDS = [
    # ------------------------------------------------------------------ E2-L00938
    {
        "id": "ECO-E2-L00938-1", "fonte_ref": "E2-L00938", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a macroeconomia clássica, a taxa real de juros resulta do equilíbrio entre a oferta e "
                      "a demanda de moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a macroeconomia clássica, a taxa real de juros resulta do equilíbrio entre a oferta "
                       "e a demanda de ") + vm("moeda") + az(".")),
        "poucas": ("No modelo clássico, o juro real nasce no mercado de " + azb("fundos emprestáveis")
                   + " (poupança = investimento). Oferta e demanda de moeda decidem o nível de preços — e, em "
                   "Keynes, os juros."),
        "destrinchando": [
            "Oferta de fundos = " + azb("poupança") + ", que cresce com o juro (recompensa por adiar consumo — "
            "preferência intertemporal). Demanda de fundos = " + azb("investimento") + ", que cai com o juro "
            "(as firmas investem enquanto a produtividade marginal do capital supera o custo do capital). O juro "
            "real é o preço que iguala as duas.",
            "Por isso o juro clássico é uma " + azb("variável real") + ": depende de “parcimônia e produtividade”, "
            "não da quantidade de moeda. É a " + azb("dicotomia clássica") + ": o lado real (produto, emprego, "
            "juro real) se resolve sem a moeda; a moeda só fixa o nível de preços (MV = PY).",
            "A política monetária, portanto, pode mexer na taxa <b>nominal</b> (via inflação esperada, efeito "
            + oc("Fisher") + ": i = r + πᵉ), mas não na real.",
            "A explicação monetária do juro é de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936): o juro é o "
            "prêmio por abrir mão da liquidez e se fixa no mercado monetário (" + azb("preferência pela liquidez")
            + " × oferta de moeda). No IS-LM, esse mercado é a curva LM.",
            vm("Regra-âncora: clássico → juro real em S = I (fundos emprestáveis); Keynes → juro em Mᵈ = Mˢ "
               "(preferência pela liquidez)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca o mercado onde o juro se forma: atribui aos "
                       "clássicos a teoria monetária do juro, que é a keynesiana. Pista: “taxa <b>real</b>” + "
                       "“clássica” → pense em poupança e investimento, nunca em moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Keynes, a taxa de juros resulta do equilíbrio entre a oferta e a demanda de moeda.”</i> "
            "→ CERTO",
            "<i>“Na macroeconomia clássica, um aumento da oferta de moeda reduz permanentemente a taxa real de "
            "juros.”</i> → ERRADO (neutralidade: a moeda só altera preços)",
        ])],
        "reescrita": ("Segundo a macroeconomia clássica, a taxa real de juros resulta do equilíbrio entre a oferta e "
                      "a demanda de " + hl("fundos emprestáveis (poupança e investimento)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No modelo clássico, o juro real é determinado no mercado de fundos emprestáveis "
                             "(poupança × investimento), por preferências intertemporais e produtividade marginal do "
                             "capital; a política monetária afeta só o juro nominal."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01344
    {
        "id": "ECO-E2-L01344-1", "fonte_ref": "E2-L01344", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_SI,
        "rotulo_item": "Item",
        "assertiva": ("O comportamento dos poupadores não condiciona a realização de investimentos, de acordo com a "
                      "abordagem clássica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O comportamento dos poupadores ") + vm("não condiciona") + az(" a realização de "
                    "investimentos, de acordo com a abordagem clássica.")),
        "poucas": ("Para os clássicos, a " + azb("poupança prévia") + " financia o investimento: o que os "
                   "poupadores decidem ofertar no mercado de fundos condiciona quanto se investe. Quem inverte a "
                   "causalidade é Keynes."),
        "destrinchando": [
            "No mercado de " + azb("fundos emprestáveis") + ", poupança (oferta) e investimento (demanda) se "
            "determinam juntos, e a taxa de juros garante S = I. Se as famílias decidem poupar mais, a oferta de "
            "fundos cresce, o juro cai e o investimento aumenta: a decisão dos poupadores <b>puxa</b> o "
            "investimento.",
            "Daí a ideia de que poupança é condição prévia do investimento — “é preciso poupar para investir”. "
            "Na visão clássica, poupar mais é virtude também no agregado: mais capital, mais crescimento.",
            oc("Keynes") + " inverte a seta: o " + azb("investimento") + " (decidido pelas expectativas de lucro, a "
            "eficiência marginal do capital) gera renda, e a renda gera a poupança que o financia. A identidade "
            "S = I continua valendo ex post, mas a causalidade é " + vd("I → Y → S") + ".",
            "Consequência keynesiana: se todos tentam poupar mais, a renda cai e a poupança agregada não sobe — o "
            + azb("paradoxo da parcimônia") + ".",
            vm("Regra-âncora: clássicos — S determina I (via juros); Keynes — I determina S (via renda)."),
        ],
        "dissecando": (cz("[inversão · troca de ator]") + " Uma negação (“não condiciona”) transforma a tese "
                       "clássica na keynesiana. Em itens que opõem as duas escolas, pergunte sempre: quem causa "
                       "quem, e por qual variável (juros ou renda)?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Keynes, a poupança é resultado do investimento, que gera a renda da qual ela sai.”</i> → "
            "CERTO",
            "<i>“Para a abordagem clássica, a igualdade entre poupança e investimento é garantida por variações "
            "da renda.”</i> → ERRADO (troca de variável: é a taxa de juros)",
        ])],
        "reescrita": ("O comportamento dos poupadores " + hl("condiciona") + " a realização de investimentos, de "
                      "acordo com a abordagem clássica."),
        "tipo_erro": ["INVERSAO", "TROCA_ATOR"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": ("S e I são determinados simultaneamente no mercado de fundos, e o juro garante S = I; "
                             "logo os poupadores condicionam o investimento. Na visão convencional, poupança prévia "
                             "é condição do investimento; para Keynes, a poupança resulta do investimento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01345
    {
        "id": "ECO-E2-L01345-1", "fonte_ref": "E2-L01345", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_SI,
        "rotulo_item": "Item",
        "assertiva": ("A taxa de juros, para o modelo clássico, é determinada pela produtividade marginal do capital "
                      "e pela preferência intertemporal dos indivíduos; tal análise difere da perspectiva de Keynes, "
                      "que analisa a taxa de juros como resultante da preferência por liquidez, dada a oferta de "
                      "moeda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A taxa de juros, para o modelo clássico, é determinada pela <u>produtividade marginal do "
                      "capital</u> e pela <u>preferência intertemporal</u> dos indivíduos; tal análise difere da "
                      "perspectiva de Keynes, que analisa a taxa de juros como resultante da <u>preferência por "
                      "liquidez</u>, dada a oferta de moeda."),
        "poucas": ("Juro clássico = fenômeno " + azb("real") + " (produtividade × paciência, em S = I); juro "
                   "keynesiano = fenômeno " + azb("monetário") + " (preferência pela liquidez × oferta de moeda)."),
        "destrinchando": [
            "Por trás da <b>demanda</b> de fundos (investimento) está a " + azb("produtividade marginal do capital")
            + ": a firma investe até o retorno do capital adicional igualar o juro. Por trás da <b>oferta</b> "
            "(poupança) está a " + azb("preferência intertemporal") + ": quanto consumo presente o indivíduo troca "
            "por consumo futuro, dado o prêmio do juro. É a fórmula de " + oc("Irving Fisher") + ": juro = "
            "“impaciência” e “oportunidade de investimento”.",
            "Para " + oc("Keynes") + ", o juro não remunera a espera (poupar), e sim a renúncia à "
            + azb("liquidez") + ": quem poupa ainda escolhe <b>como</b> guardar — moeda ou títulos. A demanda por "
            "moeda tem motivos transacional, precaucional e " + azb("especulativo") + "; com a oferta de moeda "
            "dada pelo banco central, o juro é o preço que equilibra esse mercado.",
            "Consequências: no clássico, a política monetária não afeta o juro real (dicotomia); em Keynes, mais "
            "moeda reduz o juro e pode estimular investimento e renda — salvo na " + azb("armadilha da liquidez")
            + ".",
            "No IS-LM (" + oc("Hicks") + ", 1937), as duas visões convivem: o juro de equilíbrio sai do encontro "
            "da IS (lado real, poupança e investimento) com a LM (lado monetário).",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " O item enfileira os determinantes corretos de "
                       "cada escola e só testa se o candidato não os embaralha. A armadilha seria trocar os "
                       "pares (“para Keynes, produtividade marginal do capital…”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para o modelo clássico, a taxa de juros é determinada pela preferência pela liquidez.”</i> → "
            "ERRADO (troca de ator: é a tese de Keynes)",
            "<i>“Para Keynes, o juro é a recompensa pela abstinência do consumo presente.”</i> → ERRADO (é a "
            "visão clássica; para Keynes, recompensa por abrir mão da liquidez)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Produtividade marginal do capital fundamenta a demanda por investimento; a poupança "
                             "resulta da escolha intertemporal; em Keynes, o juro vem da preferência pela liquidez e "
                             "da oferta de moeda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01347
    {
        "id": "ECO-E2-L01347-1", "fonte_ref": "E2-L01347", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_SI,
        "rotulo_item": "Item",
        "assertiva": ("O investimento, no mercado de fundos emprestáveis, é determinado pela poupança, e a taxa de "
                      "juros é responsável pela igualdade entre poupança e investimento (S = I), no modelo clássico, "
                      "de acordo com a Lei de Say."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("O investimento, no mercado de fundos emprestáveis, é determinado pela poupança, e a taxa de "
                       "juros é responsável pela igualdade entre poupança e investimento (S = I), no modelo "
                       "clássico, ") + vm("de acordo com a Lei de Say") + az(".")),
        "poucas": ("Até “modelo clássico” o item é correto; o problema é atribuir o mecanismo dos fundos "
                   "emprestáveis à " + azb("Lei de Say") + ", que não diz isso literalmente — daí a anulação."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Item anulado. A parte sobre fundos emprestáveis e S = I é incontroversa. O acréscimo "
                          "“de acordo com a Lei de Say” é ambíguo: lido como “a Lei de Say enuncia isso”, o item "
                          "seria ERRADO (Say trata de oferta que cria demanda, não de juros); lido como “de modo "
                          "coerente com a Lei de Say”, seria " + vd("CERTO") + ", porque o ajuste pelo juro é "
                          "justamente o que garante que a poupança volte ao circuito como investimento.")],
        "destrinchando": [
            azb("Lei de Say") + " (" + oc("Jean-Baptiste Say") + ", <i>Tratado de Economia Política</i>, 1803), na "
            "forma popularizada: “a oferta cria sua própria demanda” — quem produz o faz para comprar outros bens, "
            "de modo que não pode haver superprodução <b>geral</b> e duradoura.",
            "Objeção óbvia: e a renda que é poupada, e não gasta? A resposta clássica (desenvolvida por "
            + oc("Ricardo") + " e pelos neoclássicos) é o mercado de " + azb("fundos emprestáveis") + ": a "
            "poupança é ofertada como crédito, e o " + azb("juro") + " se ajusta até que toda ela seja tomada "
            "pelos investidores (S = I). O vazamento da poupança volta como gasto de investimento.",
            "Por isso o mecanismo do juro é a <b>demonstração</b> (ou a garantia) da Lei de Say, não o seu "
            "enunciado. É essa distância entre “a lei diz” e “a lei é validada por” que gerou a ambiguidade.",
            oc("Keynes") + " ataca as duas peças: o juro é monetário (preferência pela liquidez), e não garante "
            "S = I ao nível de pleno emprego; quem ajusta S a I é a <b>renda</b>. Sem esse elo, cai a Lei de Say "
            "e nasce o " + azb("princípio da demanda efetiva") + ".",
        ],
        "dissecando": (cz("[outro: atribuição ambígua]") + " Um item correto ganhou uma cauda de autoridade "
                       "(“de acordo com…”) que pode ser lida como fonte literal ou como compatibilidade. Quando a "
                       "banca cola um nome próprio no fim de uma tese, confira se aquele autor ou lei "
                       "<b>enunciou</b> exatamente aquilo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, a taxa de juros garante S = I, o que assegura que a poupança retorne ao "
            "fluxo de gastos, em consonância com a Lei de Say.”</i> → CERTO",
            "<i>“A Lei de Say estabelece que a taxa de juros é determinada pela oferta e pela demanda de "
            "moeda.”</i> → ERRADO (troca de conceito: juro monetário é Keynes)",
        ])],
        "reescrita": ("O investimento, no mercado de fundos emprestáveis, é determinado pela poupança, e a taxa de "
                      "juros é responsável pela igualdade entre poupança e investimento (S = I), no modelo "
                      "clássico, " + hl("em consonância com") + " a Lei de Say."),
        "tipo_erro": ["OUTRO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("ANULADA: até “modelo clássico” correta; “de acordo com a Lei de Say” é ambíguo — "
                             "não é a proposição original de Say, mas o mecanismo dos fundos emprestáveis é a via "
                             "pela qual a lei é demonstrada (Ricardo, neoclássicos)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: item anulado pela ambiguidade de “de acordo com a Lei de Say” (enunciado da lei × "
                    "compatibilidade com ela)"],
    },
    # ------------------------------------------------------------------ E2-L01350
    {
        "id": "ECO-E2-L01350-1", "fonte_ref": "E2-L01350", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria clássica, a economia funciona no nível de pleno emprego; e o desemprego "
                      "é o resultado da recusa dos trabalhadores de trabalharem pelo salário vigente. Segundo essa "
                      "corrente teórica, o desemprego pode ser classificado como voluntário ou friccional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a teoria clássica, a economia funciona no nível de pleno emprego; e o "
                      "desemprego é o resultado da recusa dos trabalhadores de trabalharem pelo salário vigente. "
                      "Segundo essa corrente teórica, o desemprego pode ser classificado como <u>voluntário ou "
                      "friccional</u>."),
        "poucas": ("Com salários flexíveis, o mercado de trabalho se equilibra no " + azb("pleno emprego")
                   + "; o desemprego que sobra é " + azb("voluntário") + " (não aceita o salário vigente) ou "
                   + azb("friccional") + " (transição entre empregos). O involuntário é a novidade de Keynes."),
        "destrinchando": [
            "No modelo clássico, a demanda por trabalho vem da produtividade marginal do trabalho (a firma "
            "contrata até PMgL = w/P) e a oferta, da escolha trabalho × lazer. O " + azb("salário real")
            + " flexível iguala as duas: todo mundo que quer trabalhar àquele salário está empregado.",
            azb("Desemprego voluntário") + ": quem está na força de trabalho mas não aceita o salário corrente — "
            "na linguagem do item, “recusa” de trabalhar pelo salário vigente.",
            azb("Desemprego friccional") + ": quem está mudando de emprego ou entrando no mercado; nasce da "
            "informação imperfeita e do tempo de busca, e existe mesmo no pleno emprego.",
            "O que a teoria clássica <b>não</b> admite como situação persistente é o " + azb("desemprego "
            "involuntário") + " — gente disposta a trabalhar pelo salário vigente (ou menos) sem encontrar vaga. "
            "Se ele surgisse, o salário cairia até eliminá-lo. " + oc("Keynes") + " (1936) construiu a "
            "<i>Teoria Geral</i> justamente para explicar o desemprego involuntário duradouro.",
            vm("Regra-âncora: pleno emprego clássico ≠ desemprego zero; ele convive com o voluntário e o "
               "friccional."),
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a classificação clássica dos manuais. A tentação é "
                       "estranhar “pleno emprego” ao lado de “desemprego” e marcar ERRADO; o risco real está em "
                       "trocar a dupla por “involuntário”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a teoria clássica, o desemprego pode ser classificado como involuntário ou "
            "friccional.”</i> → ERRADO (troca de conceito: involuntário é categoria keynesiana)",
            "<i>“No pleno emprego clássico, a taxa de desemprego é nula.”</i> → ERRADO (há friccional e "
            "voluntário)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Voluntário: quem não deseja trabalhar ao salário corrente; friccional: mudança de "
                             "emprego ou entrada na força de trabalho; no clássico, o mercado de trabalho se ajusta "
                             "ao pleno emprego, com só esses dois tipos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01439
    {
        "id": "ECO-E2-L01439-1", "fonte_ref": "E2-L01439", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("Acerca da relação entre poupança e investimento e dos modelos de crescimento econômico, julgue "
                    "a afirmação."),
        "rotulo_item": "Item",
        "assertiva": ("No mercado de fundos emprestáveis, a elevação de superávits fiscais pelo governo tende a "
                      "reduzir a taxa de juros, elevando o investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No mercado de fundos emprestáveis, a elevação de superávits fiscais pelo governo "
                      "<u>tende a reduzir</u> a taxa de juros, <u>elevando</u> o investimento."),
        "poucas": ("Superávit maior = " + azb("poupança pública") + " maior: a oferta de fundos se desloca para a "
                   "direita, o juro cai e o investimento privado sobe (" + azb("crowding in") + ")."),
        "destrinchando": [
            "Identidade de partida (economia fechada): " + vd("S nacional = S privada + (T − G) = I")
            + ". A poupança pública é o resultado do governo: superávit soma fundos ao mercado; déficit "
            "retira.",
            "Elevar o superávit (corte de gastos ou alta de impostos) aumenta a poupança nacional a cada nível de "
            "juros: a curva de <b>oferta</b> de fundos vai para a direita. Leitura equivalente: o governo "
            "<b>demanda</b> menos crédito. Pelos dois caminhos, o juro de equilíbrio cai.",
            "Com juro menor, projetos antes inviáveis passam a render mais que o custo do capital: o "
            "investimento privado cresce. É o espelho do " + azb("crowding out") + " provocado pelo déficit.",
            "No longo prazo, mais investimento significa mais capital por trabalhador — por isso a "
            + azb("consolidação fiscal") + " aparece, nos modelos de crescimento, como forma de elevar a taxa "
            "de poupança (no " + oc("Solow") + ", mais s → k* maior).",
            "Ressalva keynesiana: num cenário de desemprego, o corte de gastos também derruba a renda, e o efeito "
            "líquido sobre o investimento pode ser negativo. O “tende a” do item protege a conclusão, que vale "
            "no modelo de fundos emprestáveis (produto dado).",
        ],
        "grafico_verso": "ECO-E2-L01439-1-V1",
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Reproduz o resultado-padrão do modelo e "
                       "se protege com “tende a”. A armadilha é confundir superávit com déficit e aplicar o "
                       "crowding out na direção errada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mercado de fundos emprestáveis, a elevação de déficits fiscais tende a reduzir a taxa de "
            "juros, elevando o investimento.”</i> → ERRADO (inversão: déficit eleva os juros e reduz o "
            "investimento)",
            "<i>“A elevação do superávit fiscal reduz a poupança nacional.”</i> → ERRADO (aumenta a poupança "
            "pública e, com ela, a nacional)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Superávit maior = mais poupança pública/menor demanda do governo por fundos; oferta à "
                             "direita (ou demanda à esquerda), juro cai, investimento privado sobe (crowding in)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 341", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (gráfico didático do verso, no sentido do superávit)"}],
        "alertas": ["nota_redacao: a imagem do verso ilustrava o caso do déficit (oferta à esquerda); o gráfico "
                    "novo mostra o superávit, que é o caso do item"],
    },
    # ------------------------------------------------------------------ E2-L01561
    {
        "id": "ECO-E2-L01561-1", "fonte_ref": "E2-L01561", "destino": "25", "subtema": H2["tqm"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": "Com relação à oferta agregada, salários, preços e emprego, julgue a afirmativa.",
        "rotulo_item": "Item",
        "assertiva": ("A neutralidade da moeda significa que, no longo prazo, se o Banco Central reduzir a oferta "
                      "monetária em 3 por cento, preços e salários reduzir-se-ão em 3 por cento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A neutralidade da moeda significa que, <u>no longo prazo</u>, se o Banco Central reduzir a "
                      "oferta monetária em 3 por cento, preços e salários <u>reduzir-se-ão em 3 por cento</u>."),
        "poucas": ("Moeda " + azb("neutra") + " = só mexe em variáveis nominais. Com produto e velocidade dados, "
                   "MV = PY exige que P caia na mesma proporção de M; o salário nominal acompanha, e o "
                   + azb("salário real") + " fica igual."),
        "destrinchando": [
            "Equação de trocas (" + oc("Irving Fisher") + "): " + vd("MV = PY") + ". Em taxas: %ΔM + %ΔV = %ΔP + "
            "%ΔY. No longo prazo, Y é dado pelos fatores reais (trabalho, capital, tecnologia) e V pelos hábitos "
            "de pagamento; logo " + vd("%ΔP = %ΔM = −3%") + ".",
            "Os salários nominais caem os mesmos 3%: o salário real (W/P), a produtividade, o emprego e o "
            "produto não mudam. Isso é a " + azb("neutralidade") + " — moeda como “véu” sobre a economia real "
            "(a ideia remonta a " + oc("David Hume") + ", no século XVIII, e foi retomada por " + oc("Milton "
            "Friedman") + ").",
            "Não confundir com " + azb("superneutralidade") + ": esta exige que nem a <b>taxa de crescimento</b> "
            "da moeda afete variáveis reais — hipótese mais forte e mais discutível (efeito Tobin, custos da "
            "inflação).",
            "No <b>curto prazo</b>, a maioria das escolas admite não neutralidade: contratos, rigidez de preços e "
            "salários e custos de menu fazem a contração monetária reduzir produto e emprego antes de os preços "
            "se ajustarem. Por isso o “no longo prazo” é a palavra que salva o item.",
            vm("Regra-âncora: longo prazo → moeda neutra (só preços); curto prazo → moeda pode afetar produto."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Exemplo numérico direto da definição. A dúvida de "
                       "quem errou costuma ser “salários também?” — sim: <b>nominais</b> caem 3%; os reais ficam "
                       "constantes. Sem o “no longo prazo”, o item ficaria vulnerável."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A neutralidade da moeda significa que, no curto prazo, uma redução de 3% da oferta monetária "
            "reduz preços e salários em 3%, sem efeito sobre o produto.”</i> → ERRADO (horizonte trocado: no "
            "curto prazo há rigidez)",
            "<i>“…preços e salários reais reduzir-se-ão em 3 por cento.”</i> → ERRADO (o salário real não "
            "muda)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["no longo prazo"], "dificuldade": 1,
        "comentario_fonte": ("Neutralidade: no longo prazo, variações da oferta monetária afetam só variáveis "
                             "nominais; redução de 3% em M → preços e salários nominais −3%, sem efeito real. Raiz "
                             "na TQM (MV = PY), Hume e Friedman; críticas sobre rigidezes de curto prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01588
    {
        "id": "ECO-E2-L01588-1", "fonte_ref": "E2-L01588", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("A respeito das relações entre consumo, poupança e crescimento econômico, julgue o item a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("No mercado de fundos emprestáveis, uma elevação do consumo do governo levará a um aumento da "
                      "renda e da poupança."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No mercado de fundos emprestáveis, uma elevação do consumo do governo levará a ")
                    + vm("um aumento da renda e da poupança") + az(".")),
        "poucas": ("Nesse modelo a renda é a de " + azb("pleno emprego") + " (dada); mais G sem mais impostos "
                   "reduz a " + azb("poupança pública") + " e, com ela, a nacional — os juros sobem e o "
                   "investimento privado cai (" + azb("crowding out") + ")."),
        "destrinchando": [
            "O mercado de fundos emprestáveis é a peça clássica (de longo prazo) da macro: Y está fixado pela "
            "função de produção e pelo mercado de trabalho. Logo, o gasto do governo <b>não</b> eleva a renda; "
            "ele só muda a composição da demanda.",
            "Contas: " + vd("S nacional = Y − C − G") + ". Com Y e C dados, cada real a mais de G é um real a "
            "menos de poupança nacional (ou, separando, a poupança pública T − G cai).",
            "No gráfico (juros × fundos), a oferta de fundos se desloca para a <b>esquerda</b>: o juro sobe e a "
            "quantidade de fundos — o investimento — cai. Alguma poupança privada pode reagir ao juro maior, mas "
            "não compensa a queda da pública: a poupança nacional diminui.",
            "A ideia de que G eleva a renda (e, com ela, a poupança induzida) pertence ao " + azb("modelo "
            "keynesiano") + " de curto prazo, com desemprego e multiplicador. O item mistura os dois modelos.",
            vm("Regra-âncora: fundos emprestáveis → G↑ = S nacional↓, r↑, I↓ (Y dado)."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item aplica o raciocínio do multiplicador "
                       "(G↑ → Y↑ → S↑) dentro de um modelo em que a renda é fixa. A expressão “no mercado de "
                       "fundos emprestáveis” é a pista: ali G compete por poupança, não cria renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mercado de fundos emprestáveis, uma elevação do consumo do governo financiada por dívida "
            "eleva a taxa de juros e reduz o investimento.”</i> → CERTO",
            "<i>“…uma elevação do consumo do governo desloca a oferta de fundos para a direita.”</i> → ERRADO "
            "(sentido trocado: para a esquerda)",
        ])],
        "reescrita": ("No mercado de fundos emprestáveis, uma elevação do consumo do governo levará a "
                      + hl("uma redução da poupança nacional, sem aumento da renda") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("G↑ sem aumento de T reduz a poupança pública e a nacional; o juro sobe e o "
                             "investimento privado cai (crowding out); o modelo não determina a renda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 443", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida no 📖 (oferta de fundos para a esquerda, juro sobe)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01704
    {
        "id": "ECO-E2-L01704-1", "fonte_ref": "E2-L01704", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CLA,
        "rotulo_item": "Item",
        "assertiva": ("Havendo flexibilidade de preços e salários, o modelo clássico do mercado de trabalho implica "
                      "pleno-emprego, excluindo portanto a possibilidade de desemprego friccional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Havendo flexibilidade de preços e salários, o modelo clássico do mercado de trabalho "
                       "implica pleno-emprego, ") + vm("excluindo portanto") + az(" a possibilidade de desemprego "
                       "friccional.")),
        "poucas": ("O pleno emprego clássico elimina o desemprego " + azb("involuntário") + ", não o "
                   + azb("friccional") + ", que decorre do tempo de busca entre trabalhadores e vagas."),
        "destrinchando": [
            "Com preços e salários flexíveis, o " + azb("salário real") + " se ajusta até igualar oferta e "
            "demanda de trabalho: quem quer trabalhar ao salário de equilíbrio encontra vaga. Esse é o "
            "“pleno emprego” clássico.",
            "Mas o mercado de trabalho não é um leilão instantâneo: pessoas trocam de emprego, recém-formados "
            "procuram a primeira vaga, empresas demoram a preencher postos. Esse " + azb("desemprego "
            "friccional") + " existe com qualquer salário e não é eliminado pela flexibilidade de preços.",
            "Também convive com o pleno emprego o " + azb("desemprego voluntário") + " (quem não aceita o "
            "salário vigente). O que o modelo exclui é o " + azb("involuntário") + " persistente — o objeto da "
            "<i>Teoria Geral</i> de " + oc("Keynes") + ".",
            "Em linguagem moderna: pleno emprego = desemprego na " + azb("taxa natural") + " (" + oc("Friedman")
            + ", 1968), que inclui o friccional e o estrutural; nunca desemprego zero.",
            vm("Regra-âncora: pleno emprego ≠ desemprego zero; o friccional sempre existe."),
        ],
        "dissecando": (cz("[troca de conceito · extrapolação]") + " A primeira oração é a tese clássica correta; "
                       "o erro está na conclusão enxertada com “portanto”, que estende a exclusão do desemprego "
                       "involuntário ao friccional. Conectivo conclusivo no fim de item é lugar clássico de "
                       "extrapolação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o modelo clássico do mercado de trabalho implica pleno-emprego, excluindo a possibilidade de "
            "desemprego involuntário persistente.”</i> → CERTO",
            "<i>“…implica taxa de desemprego igual a zero.”</i> → ERRADO (há friccional e voluntário)",
        ])],
        "reescrita": ("Havendo flexibilidade de preços e salários, o modelo clássico do mercado de trabalho implica "
                      "pleno-emprego, " + hl("sem excluir, contudo,") + " a possibilidade de desemprego "
                      "friccional."),
        "tipo_erro": ["TROCA_CONCEITO", "EXTRAPOLACAO"], "moduladores": ["portanto"], "dificuldade": 1,
        "comentario_fonte": ("O que não existe no clássico é o desemprego involuntário; o friccional existe mesmo "
                             "no pleno emprego (taxa natural)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01705
    {
        "id": "ECO-E2-L01705-1", "fonte_ref": "E2-L01705", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CLA,
        "rotulo_item": "Item",
        "assertiva": ("No modelo clássico, o conhecimento da função de produção e da oferta de moeda é condição "
                      "suficiente para a determinação do produto de pleno-emprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No modelo clássico, o conhecimento da função de produção e ") + vm("da oferta de moeda")
                    + az(" é condição suficiente para a determinação do produto de pleno-emprego.")),
        "poucas": ("O produto clássico sai do lado " + azb("real") + ": mercado de trabalho (oferta e demanda) "
                   "fixa o emprego N*, e a função de produção converte N* em Y*. A moeda só determina o "
                   + azb("nível de preços") + "."),
        "destrinchando": [
            "Sequência do modelo clássico: (1) a " + azb("demanda por trabalho") + " vem da função de produção "
            "(PMgL = w/P); (2) a " + azb("oferta de trabalho") + " vem das preferências entre consumo e lazer; "
            "(3) o equilíbrio fixa N* e w/P*; (4) " + vd("Y* = F(K, N*)") + ".",
            "Conhecer só a função de produção não basta: falta a oferta de trabalho. E a moeda não ajuda: pela "
            + azb("dicotomia clássica") + ", ela entra depois, na " + azb("teoria quantitativa") + " (MV = PY), "
            "para determinar P dado Y*.",
            "Graficamente: no quadrante do mercado de trabalho, Nᵈ × Nˢ dão N*; na função de produção, N* dá Y*; "
            "no plano (Y, P), a " + azb("oferta agregada clássica") + " é vertical em Y* — qualquer variação de "
            "M desloca a demanda agregada e só muda P.",
            "Por isso a moeda é " + azb("neutra") + " no modelo clássico: dobrar M dobra preços e salários "
            "nominais e deixa N*, Y* e w/P intactos.",
            vm("Regra-âncora: clássico — produção e trabalho fixam Y; moeda fixa P."),
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " Metade certa (função de produção é "
                       "necessária) e metade trocada: no lugar do mercado de trabalho, a banca pôs a variável que, "
                       "no clássico, justamente não afeta o produto. “Condição suficiente” obriga a checar se "
                       "falta algo e se sobra algo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, a função de produção e as curvas de oferta e demanda de trabalho determinam "
            "o produto de pleno emprego; a oferta de moeda determina o nível de preços.”</i> → CERTO",
            "<i>“No modelo clássico, a oferta agregada é horizontal.”</i> → ERRADO (é vertical; horizontal é o "
            "caso keynesiano extremo)",
        ])],
        "reescrita": ("No modelo clássico, o conhecimento da função de produção e " + hl("das curvas de oferta e "
                      "demanda de trabalho") + " é condição suficiente para a determinação do produto de "
                      "pleno-emprego."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": ["suficiente"], "dificuldade": 2,
        "comentario_fonte": ("Produto de pleno emprego exige função de produção e mercado de trabalho (oferta e "
                             "demanda); a oferta de moeda só determina o nível de preços (dicotomia clássica)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "IMAGEM 506", "tipo_fonte": "GRÁFICO", "lado": "verso",
             "acao": "absorvida no 📖 (mercado de trabalho Nᵈ × Nˢ)"},
            {"ref": "IMAGEM 507", "tipo_fonte": "GRÁFICO", "lado": "verso",
             "acao": "absorvida no 📖 (oferta agregada clássica vertical)"},
        ],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01706
    {
        "id": "ECO-E2-L01706-1", "fonte_ref": "E2-L01706", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_CLA,
        "rotulo_item": "Item",
        "assertiva": ("Um imposto sobre os rendimentos de aplicações financeiras, no mercado de poupança e "
                      "investimento, levará a um deslocamento para a direita da poupança agregada e redução da taxa "
                      "de juros e dos investimentos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um imposto sobre os rendimentos de aplicações financeiras, no mercado de poupança e "
                       "investimento, levará a um deslocamento para a ") + vm("direita") + az(" da poupança "
                       "agregada e ") + vm("redução") + az(" da taxa de juros e dos investimentos.")),
        "poucas": ("Tributar o rendimento das aplicações reduz o retorno líquido de poupar: a poupança se desloca "
                   "para a " + azb("esquerda") + ", o juro " + vd("sobe") + " e o investimento " + vd("cai")
                   + ". O item acerta só a queda do investimento."),
        "destrinchando": [
            "No mercado de fundos emprestáveis, a oferta é a poupança e responde ao juro <b>líquido</b> que o "
            "poupador recebe. Um imposto sobre esse rendimento faz o poupador receber menos a cada taxa bruta: "
            "poupa-se menos em cada nível de juros — curva " + azb("S para a esquerda") + ".",
            "Novo equilíbrio: escassez relativa de fundos → juro de mercado " + vd("sobe") + " → projetos "
            "marginais deixam de ser rentáveis → investimento " + vd("cai") + ". É um resultado parecido com o "
            "do déficit público (crowding out).",
            "Incoerência interna do item: se a poupança fosse para a direita, o juro cairia e o investimento "
            "<b>subiria</b>; “redução dos investimentos” não decorre do mecanismo que o próprio item descreve.",
            "Espelho: isenções ou redução de imposto sobre rendimentos de aplicações deslocam S para a direita, "
            "baixam o juro e estimulam o investimento — argumento clássico para desonerar a poupança.",
            "Ressalva teórica: o efeito do juro líquido sobre a poupança mistura " + azb("efeito substituição")
            + " (poupar rende menos → poupa-se menos) e " + azb("efeito renda") + " (para atingir uma meta, "
            "poupa-se mais). O modelo-padrão do item supõe o primeiro dominante.",
        ],
        "grafico_verso": "ECO-E2-L01706-1-V1",
        "dissecando": (cz("[inversão · meia-verdade]") + " Duas direções invertidas (direita, redução dos "
                       "juros) e uma conclusão correta no fim (queda do investimento). O teste rápido é a "
                       "coerência: S para a direita nunca reduz investimento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução do imposto sobre os rendimentos de aplicações financeiras desloca a poupança para a "
            "direita, reduzindo a taxa de juros e elevando o investimento.”</i> → CERTO",
            "<i>“O imposto sobre rendimentos de aplicações desloca a curva de investimento para a esquerda.”</i> "
            "→ ERRADO (curva trocada: a afetada é a poupança)",
        ])],
        "reescrita": ("Um imposto sobre os rendimentos de aplicações financeiras, no mercado de poupança e "
                      "investimento, levará a um deslocamento para a " + hl("esquerda") + " da poupança agregada "
                      "e " + hl("elevação") + " da taxa de juros e " + hl("redução") + " dos investimentos."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O imposto reduz o retorno líquido da poupança: S à esquerda, juros sobem, "
                             "investimento cai; o item erra a direção da poupança e dos juros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 508", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (gráfico didático no sentido do imposto: S para a esquerda)"}],
        "alertas": ["nota_redacao: a imagem do verso mostrava a redução do imposto (S para a direita); o gráfico "
                    "novo mostra o caso do item"],
    },
    # ------------------------------------------------------------------ E1-0638
    {
        "id": "ECO-E1-0638-1", "fonte_ref": "E1-0638", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Set/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo aos efeitos da política fiscal em uma economia fechada.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("Quando uma economia fechada se encontra em pleno emprego, o aumento dos gastos "
                      "governamentais provocará redução equivalente no consumo privado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quando uma economia fechada se encontra em pleno emprego, o aumento dos gastos "
                       "governamentais provocará redução equivalente ") + vm("no consumo privado") + az(".")),
        "poucas": ("Em pleno emprego o produto não cresce: para Y = C + I + G fechar, " + azb("algum")
                   + " componente privado tem de cair na mesma medida — mas não necessariamente o consumo; "
                   "tipicamente é o " + azb("investimento") + ", via juros (" + azb("crowding out") + ")."),
        "destrinchando": [
            "Economia fechada: " + vd("Y = C + I + G") + ". Em pleno emprego, Y está no teto (Y*). Se G sobe "
            "ΔG, então " + vd("ΔC + ΔI = −ΔG") + ": o deslocamento é <b>total</b>, mas a divisão entre C e I "
            "não está dada.",
            "Mecanismo clássico: G maior reduz a poupança nacional (S = Y* − C − G), a oferta de fundos se "
            "desloca para a esquerda e o " + azb("juro real sobe") + ". O ajuste recai sobre os gastos "
            "sensíveis ao juro — sobretudo o investimento; o consumo só cai se também reagir ao juro (ou a "
            "impostos futuros).",
            "Se G for financiado por impostos, a renda disponível cai e o consumo recua em c·ΔT (menos que ΔG); "
            "o restante vem do investimento. Em nenhum caso a teoria garante que o ajuste seja só via consumo.",
            "Em economia <b>aberta</b>, entram também as exportações líquidas: o juro mais alto atrai capital, "
            "aprecia o câmbio e reduz NX.",
            "Contraste com o curto prazo keynesiano: com desemprego, G↑ eleva Y pelo multiplicador e pode até "
            "aumentar o consumo — mas o item se passa em pleno emprego.",
            vm("Regra-âncora: pleno emprego → crowding out total (ΔC + ΔI = −ΔG), não necessariamente via consumo."),
        ],
        "dissecando": (cz("[restrição indevida · meia-verdade]") + " A identidade garante que algo cai na mesma "
                       "medida; o item escolhe arbitrariamente quem cai. “Equivalente” está certo; o erro está "
                       "no destinatário único (“no consumo privado”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando uma economia fechada se encontra em pleno emprego, o aumento dos gastos governamentais "
            "provocará redução equivalente na soma de consumo e investimento privados.”</i> → CERTO",
            "<i>“…o aumento dos gastos governamentais elevará o produto real pelo efeito multiplicador.”</i> → "
            "ERRADO (em pleno emprego Y não cresce)",
        ])],
        "reescrita": ("Quando uma economia fechada se encontra em pleno emprego, o aumento dos gastos "
                      "governamentais provocará redução equivalente " + hl("na demanda privada (consumo e/ou "
                      "investimento), não necessariamente no consumo privado") + "."),
        "tipo_erro": ["RESTRICAO", "MEIA_VERDADE"], "moduladores": ["equivalente"], "dificuldade": 2,
        "comentario_fonte": ("Para a economia se manter em equilíbrio, algum componente da demanda agregada terá "
                             "que cair, mas não necessariamente o consumo privado (crowding out incide sobretudo no "
                             "investimento). Respostas de IA empilhadas, algumas confusas (multiplicador em pleno "
                             "emprego)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (189).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto (enunciado reconstruído pelo verso e por busca do item)"}],
        "alertas": ["texto_reconstruido: assertiva reconstruída pela justificativa do verso, que coincide com a "
                    "resolução publicada do item “Quando uma economia fechada se encontra em pleno emprego, o "
                    "aumento dos gastos governamentais provocará redução equivalente no consumo privado”",
                    "redirecionado: de 26 para 25 (o item trata de crowding out total em pleno emprego, não de "
                    "multiplicador)"],
    },
    # ------------------------------------------------------------------ E1-0360
    {
        "id": "ECO-E1-0360-1", "fonte_ref": "E1-0360", "destino": "26", "subtema": H2["de"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo ao modelo keynesiano de determinação da renda.",
        "rotulo_item": "Item",
        "assertiva": ("Segundo o paradoxo da parcimônia, um aumento da poupança, no curto prazo, contribui para "
                      "elevar o investimento e o nível de equilíbrio do produto interno bruto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo o paradoxo da parcimônia, um aumento da poupança, no curto prazo, ")
                    + vm("contribui para elevar o investimento e o nível de equilíbrio do produto interno bruto")
                    + az(".")),
        "poucas": ("O " + azb("paradoxo da parcimônia") + " diz o contrário: se todos tentam poupar mais, o "
                   "consumo cai, a renda de equilíbrio " + vd("cai") + " pelo multiplicador e a poupança "
                   "agregada realizada não aumenta."),
        "destrinchando": [
            "Modelo keynesiano simples: Y = C + I, com C = Ca + cY e I autônomo. No equilíbrio, poupança "
            "planejada = investimento planejado (" + vd("S = I") + "). Como I não depende da poupança, é a "
            + azb("renda") + " que se ajusta até que a poupança desejada caiba no investimento dado.",
            "Se a propensão a poupar sobe (c cai), o multiplicador 1/(1 − c) encolhe e a renda de equilíbrio "
            "cai. Na nova posição, S volta a ser igual ao mesmo I: a sociedade quis poupar mais, mas só ficou "
            "mais pobre. Se o investimento depender da renda (investimento induzido), a poupança agregada pode "
            "até <b>cair</b>.",
            "É a " + azb("falácia da composição") + ": o que é prudente para um indivíduo (poupar mais) é "
            "contraproducente para todos ao mesmo tempo. A ideia remonta a " + oc("Mandeville") + " (<i>A "
            "Fábula das Abelhas</i>, 1714) e foi sistematizada por " + oc("Keynes") + " na <i>Teoria Geral</i> "
            "(1936).",
            "Inversão de causalidade frente aos clássicos: para estes, mais poupança baixa os juros e financia "
            "mais investimento (S → I); para Keynes, o investimento gera a renda que gera a poupança (I → Y → S).",
            "Escopo: vale no <b>curto prazo</b> com capacidade ociosa. No longo prazo (Solow), taxa de poupança "
            "maior eleva o capital e a renda per capita — o “no curto prazo” do item é justamente o que o "
            "derruba.",
        ],
        "dissecando": (cz("[inversão]") + " O item descreve a visão clássica (poupança → investimento → "
                       "crescimento) e a batiza com o nome do paradoxo keynesiano, que afirma o oposto. 🔥 A banca "
                       "cobra o paradoxo invertendo o sinal da renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o paradoxo da parcimônia, um aumento da propensão a poupar reduz a renda de equilíbrio, "
            "sem elevar a poupança agregada.”</i> → CERTO",
            "<i>“No modelo de Solow, uma taxa de poupança maior reduz a renda per capita de estado "
            "estacionário.”</i> → ERRADO (inversão: eleva k* e y*)",
        ])],
        "reescrita": ("Segundo o paradoxo da parcimônia, um aumento da poupança, no curto prazo, " + hl("não eleva "
                      "o investimento e reduz o nível de equilíbrio do produto interno bruto") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["no curto prazo"], "dificuldade": 1,
        "comentario_fonte": ("Com gastos autônomos dados, maior propensão a poupar reduz a renda; Keynes inverteu a "
                             "causalidade S → I; o investimento gera a renda e a poupança."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ 2012 na fonte sugere CACD 2012; não confirmada",
                    "quase_duplicata: ECO-E2-L00293-1 (mesmo tema, outra fonte)"],
    },
    # ------------------------------------------------------------------ E1-0363
    {
        "id": "ECO-E1-0363-1", "fonte_ref": "E1-0363", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo ao multiplicador keynesiano.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta, caso a propensão marginal para poupar seja igual a 0,25 e a "
                      "propensão marginal para consumir bens importados, igual a 0,15, então o multiplicador "
                      "keynesiano será igual a 10."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma economia aberta, caso a propensão marginal para poupar seja igual a 0,25 e a "
                       "propensão marginal para consumir bens importados, igual a 0,15, então o multiplicador "
                       "keynesiano será igual a ") + vm("10") + az(".")),
        "poucas": ("Na economia aberta sem governo, o multiplicador é " + vd("1/(s + m) = 1/(0,25 + 0,15) = 1/0,4 "
                   "= 2,5") + ". O 10 sai de quem subtrai m em vez de somar (1/0,10)."),
        "destrinchando": [
            "Equilíbrio: Y = C + I + X − M, com C = Ca + cY e M = M₀ + mY. Isolando Y: " + vd("Y = (Ca + I + X "
            "− M₀) / (1 − c + m)") + ". Como 1 − c = s, o multiplicador é " + vd("α = 1/(s + m)") + ".",
            "Com s = 0,25 e m = 0,15: α = 1/0,40 = " + vd("2,5") + ". Na economia fechada, seria 1/0,25 = 4.",
            "Intuição: a cada rodada de gasto, parte da renda nova " + azb("vaza") + " do circuito doméstico — "
            "pela poupança (s) e pelas importações (m), que geram renda no exterior. Mais vazamentos, "
            "multiplicador menor.",
            "Forma geral com governo e imposto proporcional t: " + vd("α = 1/[1 − c(1 − t) + m]") + ". Os três "
            "vazamentos (poupança, tributos, importações) reduzem o multiplicador; por isso economias muito "
            "abertas têm multiplicadores fiscais menores.",
            vm("Regra-âncora: vazamentos somam no denominador — 1/(s + m), nunca 1/(s − m)."),
        ],
        "dissecando": (cz("[dado alterado]") + " Item de cálculo com o número errado escolhido de propósito: 10 "
                       "= 1/(0,25 − 0,15), resultado de quem trata a importação como injeção. Confira sempre o "
                       "sinal de m."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…então o multiplicador keynesiano será igual a 2,5, inferior ao de uma economia fechada com a "
            "mesma propensão a poupar.”</i> → CERTO",
            "<i>“A abertura comercial eleva o multiplicador keynesiano.”</i> → ERRADO (inversão: m é vazamento)",
        ])],
        "reescrita": ("Em uma economia aberta, caso a propensão marginal para poupar seja igual a 0,25 e a "
                      "propensão marginal para consumir bens importados, igual a 0,15, então o multiplicador "
                      "keynesiano será igual a " + hl("2,5") + "."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("α = 1/(1 − c(1 − t) + m); com t = 0, c = 0,75 e m = 0,15, α = 2,5, não 10; a "
                             "propensão a importar reduz o multiplicador."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "00042.jpeg", "tipo_fonte": "FÓRMULA", "lado": "verso",
             "acao": "texto (fórmula do multiplicador transcrita no 📖)"},
            {"ref": "image (130).png", "tipo_fonte": "FÓRMULA", "lado": "verso",
             "acao": "texto (comparação aberta × fechada absorvida no 📖)"},
            {"ref": "image (127).png", "tipo_fonte": "FÓRMULA", "lado": "verso",
             "acao": "texto (comparação aberta × fechada absorvida no 📖)"},
        ],
        "alertas": ["banca_provavel: marca ⌚ 2012 na fonte sugere CACD 2012; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0429
    {
        "id": "ECO-E1-0429-1", "fonte_ref": "E1-0429", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à transmissão internacional das flutuações econômicas.",
        "rotulo_item": "Item",
        "assertiva": ("Diz-se que uma expansão em uma economia como a dos Estados Unidos tende a gerar expansões "
                      "econômicas em outros países pois as importações americanas irão aumentar."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Diz-se que uma expansão em uma economia como a dos Estados Unidos <u>tende a</u> gerar "
                      "expansões econômicas em outros países pois as <u>importações americanas</u> irão aumentar."),
        "poucas": ("Importação de um país é " + azb("exportação") + " de outro. Se a renda americana sobe, as "
                   "importações (M = M₀ + mY) sobem, e o gasto autônomo dos parceiros cresce — com multiplicador."),
        "destrinchando": [
            "No modelo keynesiano aberto, as importações dependem da renda interna pela " + azb("propensão "
            "marginal a importar") + " (m). Uma expansão de ΔY nos EUA gera ΔM ≈ m·ΔY de compras externas.",
            "Para os parceiros, essas compras são " + azb("exportações") + " — gasto autônomo que, via "
            "multiplicador 1/(s + m), eleva a renda deles. É a " + azb("locomotiva") + ": economias grandes "
            "puxam (ou arrastam) as demais.",
            "O efeito volta parcialmente: a renda maior lá fora eleva as importações dos parceiros, que são "
            "exportações americanas (" + azb("efeito de repercussão externa") + ", ou <i>foreign repercussion</i>).",
            "A força do canal depende do tamanho da economia que se expande, do peso dela na pauta do parceiro e "
            "de m. Para o " + rx("Brasil") + ", o canal comercial mais forte hoje é a China, principal destino das "
            "exportações ⏳ (out/2026); os EUA vêm em segundo.",
            "Há outros canais (financeiro, juros, câmbio, preços de commodities) que podem até jogar contra: uma "
            "expansão americana acompanhada de alta de juros nos EUA pode drenar capitais dos emergentes — daí o "
            "“tende a”.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Mecanismo-padrão do canal comercial, "
                       "protegido por “tende a”. A dúvida que derruba o candidato é pensar que importar “tira” "
                       "renda do país — e esquecer que é renda para o exportador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma expansão nos EUA tende a reduzir a renda dos parceiros, pois as importações americanas "
            "diminuem.”</i> → ERRADO (inversão: importações sobem com a renda)",
            "<i>“Quanto maior a propensão marginal a importar dos EUA, menor o efeito de sua expansão sobre os "
            "parceiros.”</i> → ERRADO (inversão: m maior transmite mais)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Expansão nos EUA eleva a renda e a demanda por importações, beneficiando os "
                             "exportadores para os EUA."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0459
    {
        "id": "ECO-E1-0459-1", "fonte_ref": "E1-0459", "destino": "26", "subtema": H2["de"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à teoria keynesiana.",
        "rotulo_item": "Item",
        "assertiva": ("Rejeitando a ortodoxia e sua visão em relação ao desemprego, Keynes se contrapõe à Lei de Say "
                      "através do princípio da demanda efetiva, uma vez que para ele a ideia que toda oferta gera "
                      "sua própria demanda não se aplica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Rejeitando a ortodoxia e sua visão em relação ao desemprego, Keynes se contrapõe à Lei de "
                      "Say através do <u>princípio da demanda efetiva</u>, uma vez que para ele a ideia que toda "
                      "oferta gera sua própria demanda não se aplica."),
        "poucas": ("O " + azb("princípio da demanda efetiva") + " é a negação keynesiana da " + azb("Lei de Say")
                   + ": é o gasto esperado que determina produção e emprego, e nada garante que ele absorva a "
                   "produção de pleno emprego."),
        "destrinchando": [
            azb("Lei de Say") + ": a produção gera renda igual ao seu valor, e essa renda é gasta — em consumo ou, "
            "via poupança e juros, em investimento. Logo não há insuficiência geral de demanda, e o desemprego "
            "só pode ser voluntário ou friccional.",
            oc("Keynes") + " (<i>Teoria Geral</i>, 1936, cap. 3): as firmas contratam conforme a receita que "
            "<b>esperam</b> obter. A " + azb("demanda efetiva") + " é o ponto em que a demanda agregada esperada "
            "encontra a oferta agregada — e esse ponto pode ficar abaixo do pleno emprego.",
            "Dois vazamentos quebram o circuito de Say: a poupança não se converte automaticamente em "
            "investimento (que depende das expectativas, a " + azb("eficiência marginal do capital") + "), e a "
            + azb("preferência pela liquidez") + " permite entesourar renda em moeda em vez de gastá-la.",
            "Resultado: " + azb("equilíbrio com desemprego involuntário") + ". Daí a defesa de política fiscal "
            "ativa para elevar a demanda.",
            vm("Regra-âncora: Say — oferta cria demanda; Keynes — demanda (efetiva) determina oferta e emprego."),
        ],
        "dissecando": (cz("[literalidade]") + " Tese de manual sobre a ruptura keynesiana. Sem armadilha "
                       "lexical; a única chance de erro é confundir “ortodoxia” com o próprio Keynes ou atribuir "
                       "a Lei de Say a ele."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Keynes reformula a Lei de Say ao afirmar que a demanda efetiva garante o pleno emprego.”</i> → "
            "ERRADO (a demanda efetiva pode ficar aquém do pleno emprego)",
            "<i>“Para a ortodoxia clássica, o desemprego involuntário duradouro é incompatível com a Lei de "
            "Say.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas gabarito CERTO e link para material externo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0465
    {
        "id": "ECO-E1-0465-1", "fonte_ref": "E1-0465", "destino": "26", "subtema": H2["de"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo ao pensamento de Keynes.",
        "rotulo_item": "Item",
        "assertiva": ("Conforme Keynes, o nível de emprego agregado não se define meramente como um ponto de "
                      "equilíbrio parcial, dado no encontro de curvas agregadas de oferta e de demanda por trabalho. "
                      "Para ele, em uma dada estrutura produtiva, o nível de emprego resulta da decisão dos "
                      "empresários de empregar a força de trabalho em função das expectativas de consumo e de "
                      "investimento na economia. Assim, poderá persistir o desemprego involuntário enquanto o nível "
                      "de demanda efetiva for demasiadamente baixo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Conforme Keynes, o nível de emprego agregado não se define meramente como um ponto de "
                      "equilíbrio parcial, dado no encontro de curvas agregadas de oferta e de demanda por trabalho. "
                      "Para ele, em uma dada estrutura produtiva, o nível de emprego resulta da decisão dos "
                      "empresários de empregar a força de trabalho em função das <u>expectativas de consumo e de "
                      "investimento</u> na economia. Assim, <u>poderá persistir</u> o desemprego involuntário "
                      "enquanto o nível de demanda efetiva for demasiadamente baixo."),
        "poucas": ("Em Keynes, o emprego não sai do mercado de trabalho isolado: sai da " + azb("demanda efetiva")
                   + " — o que os empresários esperam vender em consumo e investimento. Demanda baixa sustenta "
                   + azb("desemprego involuntário") + "."),
        "destrinchando": [
            "Clássicos: o emprego se define no mercado de trabalho (Nᵈ = Nˢ ao salário real de equilíbrio) — um "
            "equilíbrio <b>parcial</b>, do qual o produto deriva pela função de produção.",
            oc("Keynes") + " inverte a ordem: o empresário decide quanto produzir (e, portanto, quantos contratar) "
            "olhando a demanda esperada — consumo, que depende da renda, e investimento, que depende das "
            "expectativas de longo prazo (" + azb("eficiência marginal do capital") + ", “" + azb("animal "
            "spirits") + "”). O mercado de trabalho só “recebe” o nível de emprego definido no mercado de bens.",
            "Por isso o desemprego pode ser " + azb("involuntário") + ": trabalhadores dispostos a aceitar o "
            "salário vigente (ou até menos) não são contratados porque não há demanda para o que produziriam. "
            "Baixar salários não resolve, pois reduz renda e consumo.",
            "A solução está do lado da demanda: política fiscal (gasto público), juros baixos e, sobretudo, "
            "reanimação das expectativas de investimento.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Paráfrase longa da tese central da "
                       "<i>Teoria Geral</i>. O “meramente” e o “poderá persistir” calibram o item; a tentação de "
                       "marcar ERRADO vem de achar que Keynes “nega” o mercado de trabalho — ele o subordina à "
                       "demanda efetiva."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Conforme Keynes, o nível de emprego é determinado exclusivamente pelo encontro das curvas de "
            "oferta e demanda por trabalho.”</i> → ERRADO (modulador absoluto; é a visão clássica)",
            "<i>“Para Keynes, a redução dos salários nominais é condição suficiente para eliminar o desemprego "
            "involuntário.”</i> → ERRADO (cortes salariais deprimem a demanda)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["meramente", "poderá"],
        "dificuldade": 2,
        "comentario_fonte": "Correto; a alternativa é exaustiva no que há de relevante ao tema.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ 2017 na fonte sugere CACD 2017; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0466
    {
        "id": "ECO-E1-0466-1", "fonte_ref": "E1-0466", "destino": "26", "subtema": H2["de"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo ao pensamento de Keynes.",
        "rotulo_item": "Item",
        "assertiva": ("A suposição feita por Keynes de que os salários nominais e outros elementos de custo "
                      "permanecem constantes altera a natureza do raciocínio que ele desenvolveu para explicar os "
                      "determinantes do volume de emprego agregado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A suposição feita por Keynes de que os salários nominais e outros elementos de custo "
                       "permanecem constantes ") + vm("altera") + az(" a natureza do raciocínio que ele "
                       "desenvolveu para explicar os determinantes do volume de emprego agregado.")),
        "poucas": ("Keynes adota salários nominais constantes só como " + azb("simplificação expositiva")
                   + " e avisa que o caráter essencial do argumento é o mesmo com ou sem ela: o emprego é "
                   "determinado pela " + azb("demanda efetiva") + ", não pela rigidez salarial."),
        "destrinchando": [
            "No cap. 3 da <i>Teoria Geral</i> (1936), " + oc("Keynes") + " supõe constantes o salário nominal e "
            "os demais custos por unidade de trabalho, mas declara que a simplificação serve apenas para "
            "facilitar a exposição e será abandonada depois — o caráter essencial do argumento não muda se os "
            "salários variarem.",
            "E ele a abandona: no cap. 19 (“Variações dos salários nominais”), mostra que cortar salários não "
            "garante mais emprego. Salário menor reduz renda e consumo; a deflação aumenta o peso real das "
            "dívidas e piora expectativas. O único canal favorável seria a queda dos juros pela menor demanda "
            "de moeda — e esse efeito a política monetária obteria de forma mais simples.",
            "Por isso, para Keynes, o desemprego involuntário <b>não é causado</b> pela rigidez salarial: nasce "
            "da insuficiência de " + azb("demanda efetiva") + " (consumo + investimento esperados). A rigidez é "
            "um traço do mundo real, não o motor da teoria.",
            "Atenção à leitura posterior: a " + azb("síntese neoclássica") + " (" + oc("Modigliani") + ", 1944) "
            "e os " + azb("novo-keynesianos") + " atribuem o desemprego à rigidez de preços e salários. É essa "
            "leitura que o item tenta projetar sobre o próprio Keynes.",
            vm("Regra-âncora: em Keynes, salário nominal constante é hipótese de exposição; a causa do "
               "desemprego é a demanda efetiva."),
        ],
        "dissecando": (cz("[troca de conceito · juízo indevido]") + " O item converte uma hipótese simplificadora "
                       "em pilar da teoria — confusão entre o Keynes original e a síntese neoclássica. Pergunta-"
                       "teste: com salários flexíveis o desemprego involuntário some? Para Keynes, não."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A suposição de salários nominais constantes, adotada por Keynes para facilitar a exposição, não "
            "altera a natureza do seu raciocínio sobre os determinantes do emprego.”</i> → CERTO",
            "<i>“Para Keynes, a flexibilidade dos salários nominais restabeleceria automaticamente o pleno "
            "emprego.”</i> → ERRADO (cortes salariais deprimem a demanda)",
        ])],
        "reescrita": ("A suposição feita por Keynes de que os salários nominais e outros elementos de custo "
                      "permanecem constantes " + hl("não altera") + " a natureza do raciocínio que ele desenvolveu "
                      "para explicar os determinantes do volume de emprego agregado."),
        "tipo_erro": ["TROCA_CONCEITO", "JUIZO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Comentários empilhados (inclusive Prof. Jetro Coutinho e Prof. Bolzan/IDEG) — vários "
                             "afirmam que a rigidez salarial é a premissa que sustenta o desemprego keynesiano; a "
                             "duplicata corrige: a hipótese é simplificação expositiva e o emprego é determinado "
                             "pela demanda efetiva."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 382", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖 (anotação da duplicata)"}],
        "alertas": ["duplicata: comentário de E3-L00276 fundido",
                    "banca_provavel: a duplicata numera o item como “Questão 61 – Item 3”, ano 2017; possível "
                    "CACD 2017, não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0467
    {
        "id": "ECO-E1-0467-1", "fonte_ref": "E1-0467", "destino": "26", "subtema": H2["de"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo ao pensamento de Keynes.",
        "rotulo_item": "Item",
        "assertiva": ("Para um quadro de crise, uma proposição de política econômica keynesiana seria o governo "
                      "ampliar os gastos públicos como forma de elevar a demanda agregada e recuperar o nível de "
                      "emprego, ao passo que, para um momento de superaquecimento, a recomendação keynesiana seria "
                      "reduzir gastos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para um quadro de crise, uma proposição de política econômica keynesiana seria o governo "
                      "<u>ampliar</u> os gastos públicos como forma de elevar a demanda agregada e recuperar o nível "
                      "de emprego, ao passo que, para um momento de superaquecimento, a recomendação keynesiana "
                      "seria <u>reduzir</u> gastos."),
        "poucas": ("Política fiscal " + azb("anticíclica") + ": gastar mais na recessão (demanda efetiva "
                   "insuficiente) e menos no superaquecimento (pressão inflacionária). Keynesianismo não é "
                   "“gastar sempre”."),
        "destrinchando": [
            "Na crise, a demanda efetiva fica abaixo do pleno emprego; o gasto público entra como gasto "
            "autônomo e, pelo " + azb("multiplicador") + ", eleva a renda em mais que o valor gasto, puxando "
            "emprego e investimento.",
            "No superaquecimento (demanda acima da capacidade), o mesmo raciocínio pede o inverso: cortar gastos "
            "ou elevar impostos para conter a " + azb("inflação de demanda") + " — " + oc("Keynes") + " tratou "
            "disso em <i>How to Pay for the War</i> (1940), propondo poupança compulsória para conter a demanda "
            "de guerra.",
            "Além da política discricionária, há os " + azb("estabilizadores automáticos") + " (seguro-desemprego, "
            "imposto de renda progressivo), que expandem o déficit na recessão e o reduzem na expansão sem nova "
            "decisão de governo.",
            "Na prática, o difícil é a simetria: cortar gastos na alta é politicamente custoso, o que explica o "
            "“viés deficitário” criticado pela escola da " + azb("escolha pública") + " (" + oc("Buchanan")
            + " e " + oc("Wagner") + ", <i>Democracy in Deficit</i>, 1977).",
            vm("Regra-âncora: keynesianismo = política fiscal anticíclica (expande na crise, contrai no boom)."),
        ],
        "dissecando": (cz("[literalidade]") + " Descrição correta e simétrica da política anticíclica. A "
                       "armadilha seria julgar a segunda metade como “não keynesiana” por associar Keynes só a "
                       "gasto e déficit."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A recomendação keynesiana é ampliar os gastos públicos tanto em crises quanto em momentos de "
            "superaquecimento.”</i> → ERRADO (a política é anticíclica)",
            "<i>“Os estabilizadores automáticos tornam o resultado fiscal pró-cíclico.”</i> → ERRADO (inversão: "
            "são anticíclicos)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas “Correto.”",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ 2017 na fonte sugere CACD 2017; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0869
    {
        "id": "ECO-E1-0869-1", "fonte_ref": "E1-0869", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos efeitos da política fiscal no modelo keynesiano.",
        "rotulo_item": "Item",
        "assertiva": ("A adoção de uma política fiscal expansionista de aumento dos gastos públicos provoca um efeito "
                      "de estímulo à demanda agregada maior do que uma política fiscal expansionista baseada na "
                      "redução de impostos sobre a renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A adoção de uma política fiscal expansionista de aumento dos gastos públicos provoca um "
                      "efeito de estímulo à demanda agregada <u>maior</u> do que uma política fiscal expansionista "
                      "baseada na redução de impostos sobre a renda."),
        "poucas": ("O gasto entra <b>inteiro</b> na demanda já na 1ª rodada; o corte de impostos só vira gasto na "
                   "fração c (o resto é poupado). Multiplicador do gasto " + vd("1/(1 − c)") + " > do imposto "
                   + vd("c/(1 − c)") + "."),
        "destrinchando": [
            "No modelo keynesiano simples: ΔY/ΔG = " + vd("1/(1 − c)") + "; ΔY/ΔT = " + vd("−c/(1 − c)") + ". "
            "Com c = 0,8: gasto → 5; corte de impostos → 4.",
            "A diferença está na primeira rodada: R$ 100 de compras do governo são R$ 100 de demanda; R$ 100 de "
            "imposto a menos viram R$ 100 de renda disponível, dos quais só R$ 80 são gastos.",
            "Corolário: o " + azb("multiplicador do orçamento equilibrado") + " (" + oc("Haavelmo") + ", 1945) é "
            + vd("1") + " — elevar G e T no mesmo valor aumenta a renda exatamente nesse valor.",
            "Com imposto proporcional à renda (t), o multiplicador do gasto vira 1/[1 − c(1 − t)], e a "
            "comparação continua: o gasto supera o corte de alíquota em impacto por real.",
            "Ressalvas fora do modelo simples: cortes focados nos mais pobres (c alto) se aproximam do gasto; "
            "e, sob " + azb("equivalência ricardiana") + " (" + oc("Barro") + ", 1974), um corte de impostos "
            "financiado por dívida nem altera o consumo, pois as famílias poupam para pagar os impostos futuros. "
            "Não é essa equivalência que explica o item: aqui basta a poupança da 1ª rodada.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Resultado clássico de comparação de multiplicadores. "
                       "Quem erra costuma achar que “R$ 1 é R$ 1” nos dois instrumentos e esquece o vazamento "
                       "da 1ª rodada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento de gastos públicos financiado por aumento equivalente de impostos não altera a renda "
            "de equilíbrio.”</i> → ERRADO (multiplicador do orçamento equilibrado = 1)",
            "<i>“O multiplicador dos impostos é, em módulo, maior que o dos gastos.”</i> → ERRADO (inversão: "
            "o do gasto é maior)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Explica pela possibilidade de as famílias entesourarem a renda liberada (chamando isso "
                             "de “efeito ricardiano”) e pelo gasto direto do Estado; menciona a alta propensão a "
                             "consumir das classes C e D."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: a fonte chama de “efeito ricardiano” a poupança parcial do corte de impostos; "
                    "corrigido (equivalência ricardiana é outro mecanismo)"],
    },
    # ------------------------------------------------------------------ E2-L00055
    {
        "id": "ECO-E2-L00055-1", "fonte_ref": "E2-L00055", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_MULT,
        "rotulo_item": "Item",
        "assertiva": ("O multiplicador keynesiano demonstra que variações nos gastos autônomos, como o gasto "
                      "governamental, são amplificadas na economia, resultando em um aumento da renda maior do que "
                      "o gasto inicial. Esta propriedade refuta a Lei de Say, que afirma que a oferta é infinita, "
                      "enquanto, para Keynes, a demanda pode ser insuficiente e precisa ser estimulada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O multiplicador keynesiano demonstra que variações nos gastos autônomos, como o gasto "
                       "governamental, são amplificadas na economia, resultando em um aumento da renda maior do que "
                       "o gasto inicial. Esta propriedade refuta a Lei de Say, que afirma que ")
                    + vm("a oferta é infinita") + az(", enquanto, para Keynes, a demanda pode ser insuficiente e "
                    "precisa ser estimulada.")),
        "poucas": ("A " + azb("Lei de Say") + " não diz que a oferta é infinita: diz que “a oferta cria sua própria "
                   "demanda” — toda produção gera renda que será gasta, sem insuficiência geral de demanda."),
        "destrinchando": [
            "O multiplicador está bem descrito: ΔY = ΔA/(1 − c), com 0 < c < 1 → o aumento da renda supera o "
            "gasto autônomo inicial, porque cada gasto vira renda de alguém, que gasta a fração c, e assim por "
            "diante (" + oc("Kahn") + ", 1931; " + oc("Keynes") + ", 1936).",
            "A " + azb("Lei de Say") + " (" + oc("J.-B. Say") + ", 1803): quem produz o faz para trocar; a renda "
            "gerada pela produção basta para comprá-la. Logo, não há superprodução geral; o gasto se ajusta à "
            "oferta, e o produto é limitado pelo <b>lado da oferta</b> (fatores e tecnologia) — nada de "
            "“infinito”.",
            "A ruptura keynesiana: o produto é limitado pela " + azb("demanda efetiva") + ", que pode ficar "
            "abaixo do pleno emprego. O multiplicador é a ferramenta que mostra como um estímulo de demanda move "
            "o produto quando há capacidade ociosa — algo sem sentido num mundo regido por Say.",
            "Nuance: o multiplicador por si só não “refuta” Say; ele pressupõe recursos ociosos, que é a tese "
            "keynesiana. O item, porém, cai pela definição inventada da lei.",
            vm("Regra-âncora: Lei de Say = “a oferta cria sua própria demanda”."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Item longo e quase todo correto; o erro está numa definição "
                       "enxertada no meio (“a oferta é infinita”). Em itens de Say, confira a fórmula canônica "
                       "palavra por palavra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Lei de Say afirma que a demanda cria sua própria oferta.”</i> → ERRADO (inversão)",
            "<i>“Para Keynes, o produto é limitado pela demanda efetiva, que pode ser insuficiente para o pleno "
            "emprego.”</i> → CERTO",
        ])],
        "reescrita": ("O multiplicador keynesiano demonstra que variações nos gastos autônomos, como o gasto "
                      "governamental, são amplificadas na economia, resultando em um aumento da renda maior do que o "
                      "gasto inicial. Esta propriedade refuta a Lei de Say, que afirma que " + hl("a oferta cria "
                      "sua própria demanda") + ", enquanto, para Keynes, a demanda pode ser insuficiente e precisa "
                      "ser estimulada."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Multiplicador amplifica o gasto; Lei de Say propõe que a oferta encontra demanda "
                             "suficiente (a fonte acrescenta, erradamente, “ou seja, a demanda é infinita”)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00056
    {
        "id": "ECO-E2-L00056-1", "fonte_ref": "E2-L00056", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_MULT,
        "rotulo_item": "Item",
        "assertiva": ("A propensão marginal a consumir (PMC) reflete a parte da renda disponível que é destinada ao "
                      "consumo pelas famílias. Keynes postula que uma maior PMC resultaria em um multiplicador mais "
                      "elevado, o que sugere uma economia mais dinâmica e com ciclos de amplificação da renda mais "
                      "frequentes e intensos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A propensão marginal a consumir (PMC) reflete a parte da renda disponível que é destinada "
                      "ao consumo pelas famílias. Keynes postula que uma <u>maior PMC</u> resultaria em um "
                      "<u>multiplicador mais elevado</u>, o que sugere uma economia mais dinâmica e com ciclos de "
                      "amplificação da renda mais <u>frequentes</u> e intensos."),
        "poucas": ("Multiplicador = " + vd("1/(1 − PMC)") + ": PMC maior → multiplicador maior → cada choque de "
                   "gasto autônomo é mais amplificado na renda."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o núcleo (PMC maior → multiplicador maior → amplificação mais <b>intensa</b>) é "
                          "correto. Já “mais <b>frequentes</b>” não decorre do multiplicador, que mede a amplitude "
                          "da resposta, não quantos choques ocorrem. Rigorosamente, esse trecho seria motivo para "
                          "ERRADO; a banca manteve CERTO lendo a frase como conclusão genérica.")],
        "destrinchando": [
            azb("PMC") + " (c) = ΔC/ΔY<sub>d</sub>: a fração de cada real adicional de renda disponível que vai "
            "para o consumo; 1 − c é a " + azb("propensão marginal a poupar") + ". " + oc("Keynes") + " a "
            "supôs entre 0 e 1 (“lei psicológica fundamental”).",
            "Multiplicador: " + vd("k = 1/(1 − c)") + ". Com c = 0,5 → k = 2; c = 0,8 → k = 5; c = 0,9 → k = 10. "
            "Quanto menos “vaza” para a poupança a cada rodada, maior o efeito acumulado.",
            "Consequência para a estabilidade: k alto amplifica tanto estímulos (política fiscal mais potente) "
            "quanto choques negativos (queda do investimento vira recessão maior). Daí a importância dos "
            + azb("estabilizadores automáticos") + ", que reduzem o multiplicador efetivo (imposto proporcional: "
            "k = 1/[1 − c(1 − t)]).",
            "A PMC tende a ser maior entre os mais pobres — por isso transferências focadas têm alto efeito "
            "multiplicador.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Definição + relação PMC–multiplicador corretas; a "
                       "conclusão final é retórica (“mais dinâmica”, “mais frequentes”). Em provas CEBRASPE, um "
                       "acréscimo desses pode derrubar o item; aqui o gabarito ficou CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma maior propensão marginal a poupar resulta em um multiplicador mais elevado.”</i> → ERRADO "
            "(inversão: k = 1/s cai com s maior)",
            "<i>“Com PMC = 0,75, o multiplicador keynesiano é 4.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("PMC alta intensifica o efeito multiplicador; k = 1/(1 − PMC); amplifica variações e "
                             "acelera os ciclos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: “ciclos mais frequentes” não decorre do multiplicador (que afeta a amplitude, não "
                    "a frequência); gabarito CERTO mantido"],
    },
    # ------------------------------------------------------------------ E2-L00057
    {
        "id": "ECO-E2-L00057-1", "fonte_ref": "E2-L00057", "destino": "26", "subtema": H2["mult"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_MULT,
        "rotulo_item": "Item",
        "assertiva": ("A abordagem keynesiana considera que, em uma economia fechada, para cada aumento nos gastos do "
                      "governo, há um aumento exato correspondente na renda da economia, invalidando a noção de "
                      "multiplicador trazida pelos clássicos, especificamente, pela abordagem de David Ricardo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A abordagem keynesiana considera que, em uma economia fechada, para cada aumento nos gastos "
                       "do governo, há um aumento ") + vm("exato correspondente") + az(" na renda da economia, ")
                    + vm("invalidando a noção de multiplicador trazida pelos clássicos, especificamente, pela "
                         "abordagem de David Ricardo") + az(".")),
        "poucas": ("Para Keynes, o aumento da renda é " + azb("maior") + " que o do gasto (multiplicador "
                   "1/(1 − c) > 1). E o multiplicador não é clássico nem ricardiano: é de " + oc("Kahn")
                   + " (1931), incorporado por " + oc("Keynes") + "."),
        "destrinchando": [
            "Mecanismo: ΔG vira renda de quem vende ao governo; essa renda gera consumo c·ΔG, que vira renda de "
            "outros, e assim por diante. Soma: ΔG(1 + c + c² + …) = " + vd("ΔG/(1 − c)") + ". Com c = 0,8, cada "
            "R$ 1 de gasto gera R$ 5 de renda.",
            "Origem: " + oc("Richard Kahn") + " formulou o multiplicador do emprego em 1931 (“The Relation of "
            "Home Investment to Unemployment”); " + oc("Keynes") + " o transformou no multiplicador do "
            "investimento/gasto na <i>Teoria Geral</i> (1936).",
            "Os clássicos não tinham multiplicador: com pleno emprego e Lei de Say, mais gasto público apenas "
            "desloca gasto privado (" + azb("crowding out") + " total). E " + oc("David Ricardo") + " entra no "
            "debate por outra porta — a " + azb("equivalência ricardiana") + " (dívida × impostos), formalizada "
            "por " + oc("Barro") + " em 1974.",
            "“Aumento exato correspondente” (ΔY = ΔG) é o resultado do " + azb("orçamento equilibrado")
            + " (" + oc("Haavelmo") + "), quando G sobe financiado por T igual — não o do gasto em geral.",
            vm("Regra-âncora: multiplicador keynesiano > 1; origem Kahn/Keynes, não os clássicos."),
        ],
        "dissecando": (cz("[dado alterado · troca de ator]") + " Dois erros empilhados: o tamanho do efeito "
                       "(exato × amplificado) e a autoria (clássicos/Ricardo × Kahn/Keynes). Nome de autor "
                       "fora do lugar, como Ricardo aqui, é sinal clássico de item fabricado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na abordagem keynesiana, um aumento dos gastos do governo financiado por igual aumento de "
            "impostos eleva a renda exatamente no valor do gasto.”</i> → CERTO",
            "<i>“O multiplicador keynesiano é tanto maior quanto maior a propensão marginal a poupar.”</i> → "
            "ERRADO (inversão)",
        ])],
        "reescrita": ("A abordagem keynesiana considera que, em uma economia fechada, para cada aumento nos gastos "
                      "do governo, há um aumento " + hl("mais que proporcional") + " na renda da economia, "
                      + hl("conforme a noção de multiplicador formulada por Kahn e incorporada por Keynes") + "."),
        "tipo_erro": ["DADO_ALTERADO", "TROCA_ATOR"], "moduladores": ["exato"], "dificuldade": 1,
        "comentario_fonte": ("Quando o governo aumenta seus gastos, a renda aumenta de forma mais acentuada que o "
                             "gasto inicial, pelo efeito multiplicador."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
