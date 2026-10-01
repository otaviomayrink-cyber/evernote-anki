"""Cards da passada 01 de ECO — lote de redação 04 (E1-0007 a E1-0117, nota 02 — Elasticidades)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "epd": "📐 Elasticidade-preço da demanda",
    "rec": "💰 Elasticidade, receita e gasto",
    "cruz": "🔗 Elasticidade-renda e cruzada",
    "ofe": "🏭 Elasticidade da oferta",
    "det": "⏳ Determinantes e prazos",
}

BANCA_PROVAVEL = "banca_provavel: CEBRASPE (formato C/E e ano na fonte; órgão não informado, banca não confirmada)"
NAO_PRESERVADA = "não preservada (caderno 1 exportado sem imagens)"

CARDS = [
    # ------------------------------------------------------------------ E1-0007
    {
        "id": "ECO-E1-0007-1", "fonte_ref": "E1-0007", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2010", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da demanda e da elasticidade-preço.",
        "rotulo_item": "Item",
        "assertiva": ("Campanhas publicitárias bem-sucedidas, além de deslocarem, para cima e para a direita, a curva "
                      "de demanda de mercado do produto anunciado, contribuem, quando promovem a fidelização do "
                      "cliente, para tornar essa curva mais preço-inelástica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Campanhas publicitárias bem-sucedidas, além de <u>deslocarem, para cima e para a direita</u>, "
                      "a curva de demanda de mercado do produto anunciado, contribuem, quando promovem a "
                      "<u>fidelização do cliente</u>, para tornar essa curva <u>mais preço-inelástica</u>."),
        "poucas": ("Publicidade muda as " + azb("preferências") + " — um determinante da demanda que não é o "
                   "preço —, então <b>desloca</b> a curva; e a fidelização reduz os " + azb("substitutos "
                   "percebidos") + ", o que torna a demanda " + vd("menos elástica") + "."),
        "destrinchando": [
            "A curva de demanda é traçada com gostos, renda e preços dos outros bens constantes. Publicidade age "
            "sobre os <b>gostos</b>: se é bem-sucedida, aumenta a quantidade desejada a cada preço (curva para a "
            "<b>direita</b>) ou, o que é o mesmo lido no outro eixo, a disposição a pagar por cada unidade (para "
            "<b>cima</b>). É " + azb("variação da demanda") + ", não da quantidade demandada.",
            "O principal determinante da elasticidade-preço é a existência de " + azb("substitutos próximos")
            + " — e o que conta é o substituto <i>percebido</i>. A fidelização (marca, hábito, identidade) faz o "
            "cliente deixar de ver as marcas rivais como equivalentes: diante de um aumento de preço, ele troca "
            "menos de produto. Resultado: |ε| menor, curva mais inclinada a partir do mesmo ponto.",
            "Por isso as empresas investem em marca: com demanda menos elástica, ganham " + azb("poder de mercado")
            + ". O índice de " + oc("Lerner") + " resume a ligação: " + vd("(P − CMg)/P = 1/|ε|") + " — quanto "
            "menor a elasticidade, maior a margem sustentável. É a lógica da diferenciação de produto na "
            + azb("concorrência monopolística") + ".",
            "Contraexemplo: publicidade negativa ou campanhas antitabagismo deslocam a demanda para a "
            "<b>esquerda</b>.",
            vm("Regra-âncora: a publicidade mexe na posição da curva (desloca); se fideliza, mexe também na "
               "inclinação (menos elástica)."),
        ],
        "grafico_verso": "ECO-E1-0007-1-V1",
        "dissecando": (cz("[detalhe · modulador relativo]") + " O item empilha duas afirmações verdadeiras e "
                       "aposta que o candidato estranhe o “para cima e para a direita” (é o mesmo deslocamento "
                       "visto pelos dois eixos) ou ache que elasticidade só depende do preço. O “contribuem” e o "
                       "“mais” (comparativo) tornam a segunda parte segura."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…quando promovem a fidelização do cliente, tornam essa curva perfeitamente inelástica.”</i> → "
            "ERRADO (exagero: a sensibilidade cai, não zera)",
            "<i>“Campanhas publicitárias bem-sucedidas provocam movimento ao longo da curva de demanda do produto "
            "anunciado.”</i> → ERRADO (troca deslocamento por movimento)",
        ])],
        "tipo_erro": ["DETALHE", "MODULADOR_RELATIVO"], "moduladores": ["contribuem", "mais", "quando"],
        "dificuldade": 1,
        "comentario_fonte": ("Publicidade bem-sucedida desloca a demanda para cima e para a direita; a fidelização "
                             "torna o consumidor menos sensível ao preço (demanda mais inelástica, mais inclinada) e "
                             "dá poder de mercado à empresa; publicidade negativa desloca para a esquerda."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [BANCA_PROVAVEL,
                    "qualidade_fonte: um dos comentários de origem fala em “aumento da quantidade demandada” "
                    "(é aumento da demanda) e em elasticidade “reforçada em outros produtos” (sem sentido) — "
                    "corrigido"],
    },
    # ------------------------------------------------------------------ E1-0011
    {
        "id": "ECO-E1-0011-1", "fonte_ref": "E1-0011", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço cruzada da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("É correto afirmar que “Caso dois bens, A e B, apresentem elasticidade positiva em termos de "
                      "preço cruzado da demanda, podemos afirmar que os bens A e B seriam bens substitutos.”?"),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("É correto afirmar que “Caso dois bens, A e B, apresentem elasticidade <u>positiva</u> em "
                      "termos de preço cruzado da demanda, podemos afirmar que os bens A e B seriam bens "
                      "<u>substitutos</u>.”?"),
        "poucas": ("Elasticidade cruzada " + vd("positiva") + ": o preço de B sobe e a quantidade demandada de A "
                   "também sobe — o consumidor migra de B para A. É a marca dos " + azb("substitutos") + "."),
        "destrinchando": [
            azb("Elasticidade-preço cruzada") + ": ε<sub>AB</sub> = %ΔQ<sub>A</sub> / %ΔP<sub>B</sub>. Mede "
            "como a demanda de um bem reage ao preço de <b>outro</b>.",
            "O sinal classifica a relação: " + vd("ε > 0") + " → substitutos (manteiga × margarina, Uber × táxi); "
            + vd("ε < 0") + " → complementares (impressora × cartucho, carro × gasolina); " + vd("ε = 0")
            + " → independentes (sal × sapatos).",
            "Intuição dos substitutos: atendem à mesma necessidade; se um encarece, parte do consumo vai para o "
            "outro. Nos complementares, consumidos juntos, encarecer um encarece o “pacote” e reduz a compra dos "
            "dois.",
            "O <b>módulo</b> mede a proximidade: ε cruzada alta = substitutos muito próximos (gasolina comum de "
            "dois postos vizinhos); ε pequena = substituição fraca. Em defesa da concorrência, a cruzada ajuda a "
            "definir o " + azb("mercado relevante") + ".",
            "Cuidado técnico: ε<sub>AB</sub> e ε<sub>BA</sub> não precisam ter o mesmo valor (o efeito renda "
            "pesa diferente para cada bem). Em prova, basta o sinal.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, com a redação truncada típica de questionário "
                       "(“em termos de preço cruzado”). O risco é inverter os sinais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade-preço cruzada entre A e B for negativa, A e B serão substitutos.”</i> → ERRADO "
            "(sinal trocado: negativa indica complementares)",
            "<i>“Elasticidade-preço cruzada nula indica que os bens são independentes.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Cruzada positiva → substitutos (aumento do preço de um eleva a demanda do outro); "
                             "negativa → complementares; nula → independentes. Exemplos: gasolina × carro "
                             "elétrico; café × açúcar; livro × sapato."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: frente marcada “(04/22)”, sem banca nem órgão; provável questionário próprio",
                    "quase_duplicata: ECO-E1-0114-1 (mesma regra do sinal, outra redação e outra origem)"],
    },
    # ------------------------------------------------------------------ E1-0017
    {
        "id": "ECO-E1-0017-1", "fonte_ref": "E1-0017", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando que haja relação positiva entre criminalidade e gastos com o consumo de drogas "
                      "e que a demanda por drogas seja preço-inelástica, políticas antidrogas fundamentadas no "
                      "combate ao tráfico elevarão o preço das drogas e os gastos com esses produtos, agravando "
                      "os níveis de criminalidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando que haja relação positiva entre criminalidade e gastos com o consumo de drogas "
                      "e que a demanda por drogas seja <u>preço-inelástica</u>, políticas antidrogas fundamentadas "
                      "no <u>combate ao tráfico</u> elevarão o preço das drogas e <u>os gastos</u> com esses "
                      "produtos, agravando os níveis de criminalidade."),
        "poucas": ("Combater o tráfico " + azb("reduz a oferta") + " e eleva o preço; com demanda "
                   + azb("inelástica") + ", a quantidade cai proporcionalmente menos que o preço sobe, o "
                   + vd("gasto (p × q) aumenta") + " e, pela premissa dada, a criminalidade também."),
        "destrinchando": [
            "Gasto do consumidor = receita do vendedor = p × q. Em termos percentuais, %Δgasto ≈ %Δp + %Δq. Se "
            + vd("|ε| < 1") + ", a queda de q é menor que a alta de p → o gasto <b>sobe</b>; se |ε| > 1, cai; se "
            "|ε| = 1, fica constante.",
            "Drogas são o exemplo clássico de demanda inelástica: dependência química, poucos substitutos, hábito. "
            "A repressão (apreensões, prisões, risco maior) eleva o custo do traficante: a " + azb("oferta")
            + " se desloca para a esquerda. Preço sobe muito; consumo cai pouco.",
            "Junte a premissa do item — crime cresce com o gasto (usuários financiam o vício com furtos; o tráfico "
            "fatura mais) — e a conclusão é dedutiva: mais gasto, mais crime.",
            "É o exemplo de " + oc("Mankiw") + " (<i>Introdução à Economia</i>, aplicações da elasticidade): "
            "políticas que reduzem a <b>demanda</b> (educação, tratamento) baixam preço e quantidade ao mesmo "
            "tempo e, por isso, reduzem o gasto e o crime associado.",
            vm("Regra-âncora: choque de oferta + demanda inelástica → preço e gasto total sobem."),
        ],
        "grafico_verso": "ECO-E1-0017-1-V1",
        "dissecando": (cz("[contraintuitivo]") + " Verdadeiro, mas contra o senso comum de que reprimir o tráfico "
                       "sempre reduz o crime. A banca entrega as duas premissas (“relação positiva” e "
                       "“preço-inelástica”): o julgamento é dedução, não opinião sobre política de drogas. 🔥 "
                       "“Inelástica + choque de oferta → gasto sobe” é cobrança recorrente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se a demanda por drogas fosse preço-elástica, a repressão ao tráfico elevaria o gasto com "
            "drogas…”</i> → ERRADO (com |ε| > 1 o gasto cai)",
            "<i>“Campanhas de prevenção que reduzam a demanda por drogas diminuem o preço e o gasto com esses "
            "produtos.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Premissas dadas como fato; repressão reduz a oferta e eleva o preço; com demanda "
                             "inelástica o consumo quase não cai, o gasto aumenta e, pela premissa, a "
                             "criminalidade. Imagens comparavam o retângulo de gasto antes e depois."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "image (4).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
             "acao": "texto (assertiva reconstruída pelo comentário e por versões do item em bancos de questões)"},
            {"ref": "image (3).png, image (1).png, image (2).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
             "acao": "redesenhada (ECO-E1-0017-1-V1, antes × depois)"}],
        "alertas": ["texto_reconstruido: frente original era só imagem (image (4).png); assertiva reconstruída a "
                    "partir do comentário, que a refuta ponto a ponto, e da versão do item que circula em bancos "
                    "de questões — conferir com a imagem",
                    "banca_provavel: CEBRASPE (não confirmada: a fonte não traz órgão nem ano)"],
    },
    # ------------------------------------------------------------------ E1-0085
    {
        "id": "ECO-E1-0085-1", "fonte_ref": "E1-0085", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2017", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda e à receita total.",
        "rotulo_item": "Item",
        "assertiva": ("Para os ofertantes de um bem essencial não vale a pena reduzir a oferta desse bem para forçar "
                      "o aumento do preço, uma vez que a sua receita total diminuirá ao fim do processo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para os ofertantes de um bem essencial ") + vm("não vale a pena") + az(" reduzir a oferta "
                      "desse bem para forçar o aumento do preço, uma vez que a sua receita total ")
                   + vm("diminuirá") + az(" ao fim do processo."),
        "poucas": ("Bem essencial tem " + azb("demanda inelástica") + ": o preço sobe proporcionalmente mais do "
                   "que a quantidade cai, e a " + vd("receita total aumenta") + ". Reduzir a oferta compensa — "
                   "é a lógica dos cartéis."),
        "destrinchando": [
            "Receita total RT = P × Q, e " + vd("%ΔRT ≈ %ΔP + %ΔQ") + ". Com |ε| < 1, a queda de Q é menor que a "
            "alta de P: a RT sobe. Ex.: preço +10% e quantidade −2% → RT ≈ " + vd("+8%") + ".",
            "Exemplo numérico: P = 8 e Q = 10 → RT = " + vd("80") + ". A oferta é contraída, o preço dobra para 16 "
            "e a quantidade cai só 30%, para 7 → RT = " + vd("112") + ". Além de faturar mais, o ofertante produz "
            "menos — o custo cai e o lucro sobe ainda mais.",
            "Por que essencial = inelástica: o consumidor não pode abrir mão do bem (remédio de uso contínuo, "
            "energia, combustível no curto prazo) e há poucos substitutos.",
            "Caso histórico: a " + azb("OPEP") + " em 1973–74 — corte coordenado de produção, preço do barril "
            "multiplicado, receitas dos exportadores em alta, porque a demanda de petróleo era muito inelástica "
            "no curto prazo.",
            "Limites da estratégia: exige " + azb("poder de mercado") + " (um produtor em concorrência perfeita não "
            "move o preço), coordenação estável (cada membro do cartel tem incentivo a furar a cota) e tempo — "
            "no longo prazo a demanda fica mais elástica (substitutos, economia de energia), como a própria OPEP "
            "viveu nos anos 1980.",
        ],
        "grafico_verso": "ECO-E1-0085-1-V1",
        "dissecando": (cz("[inversão · nexo indevido]") + " O item inverte o efeito sobre a receita e, sobre a "
                       "inversão, constrói a conclusão (“não vale a pena”). A palavra “essencial” é a pista: ela "
                       "sinaliza demanda inelástica, e inelástica + preço ↑ = receita ↑. 🔥 A banca junta "
                       "essencialidade, elasticidade e receita no mesmo item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para os ofertantes de um bem supérfluo, de demanda elástica, reduzir a oferta para forçar o "
            "aumento do preço diminui a receita total.”</i> → CERTO",
            "<i>“Se a demanda for de elasticidade unitária, a contração da oferta eleva a receita total dos "
            "ofertantes.”</i> → ERRADO (com |ε| = 1 a receita fica constante)",
        ])],
        "reescrita": ("Para os ofertantes de um bem essencial " + hl("pode valer a pena") + " reduzir a oferta "
                      "desse bem para forçar o aumento do preço, uma vez que a sua receita total "
                      + hl("aumentará") + " ao fim do processo" + hl(", dada a demanda inelástica") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Bem essencial tem demanda inelástica; reduzir a oferta eleva o preço mais que "
                             "proporcionalmente à queda da quantidade e aumenta a receita (RT = P × Q). Exemplos "
                             "numéricos 8 × 10 = 80 → 16 × 7 = 112 e +10% − 2% = +8%; lembrar da OPEP. Duplicata "
                             "E3-L00451 com gráfico de demanda íngreme e reescrita sugerida."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "E3-L00451 IMAGEM 653", "tipo_fonte": "GRÁFICO", "lado": "verso",
             "acao": "redesenhada (ECO-E1-0085-1-V1, com os números do exemplo)"},
            {"ref": "E3-L00451 IMAGEM 654", "tipo_fonte": "TEXTO", "lado": "verso",
             "acao": "absorvida (reproduzia o enunciado)"}],
        "alertas": [BANCA_PROVAVEL,
                    "duplicata_fundida: comentário de E3-L00451 (mesmo item) incorporado"],
    },
    # ------------------------------------------------------------------ E1-0086
    {
        "id": "ECO-E1-0086-1", "fonte_ref": "E1-0086", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2017", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("No inverno, uma cidade onde as pessoas disponham de sistemas a gás para aquecimento de água "
                      "deve apresentar elasticidade-preço da demanda por eletricidade maior que a de outra cidade "
                      "em que haja somente sistemas elétricos de aquecimento de água."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No inverno, uma cidade onde as pessoas <u>disponham de sistemas a gás</u> para aquecimento "
                      "de água deve apresentar elasticidade-preço da demanda por eletricidade <u>maior</u> que a de "
                      "outra cidade em que haja somente sistemas elétricos de aquecimento de água."),
        "poucas": ("O gás é um " + azb("substituto") + " da eletricidade no aquecimento: onde ele existe, um "
                   "aumento da tarifa elétrica leva parte do consumo para o gás. Mais substitutos → "
                   + vd("demanda mais elástica") + "."),
        "destrinchando": [
            "Na cidade com os dois sistemas, se a tarifa de energia sobe, as famílias passam a aquecer a água com "
            "gás: a quantidade demandada de eletricidade cai bastante. Na cidade só com chuveiro elétrico, não "
            "há para onde fugir — paga-se mais e consome-se quase o mesmo.",
            "Determinantes da " + azb("elasticidade-preço da demanda") + ": (1) " + vd("substitutos próximos")
            + " — o mais importante; (2) essencialidade; (3) peso do bem no orçamento; (4) horizonte de tempo; "
            "(5) amplitude da definição do mercado (“energia” é menos elástica que “eletricidade”).",
            "O inverno reforça o argumento: o aquecimento de água pesa mais na conta, e o incentivo a "
            "substituir cresce justamente quando a alternativa existe.",
            "Ligação com a " + azb("elasticidade cruzada") + ": gás e eletricidade, nesse uso, têm ε cruzada "
            "positiva (substitutos). Onde a cruzada é alta, a elasticidade-preço própria tende a ser alta.",
            vm("Regra-âncora: quanto mais e melhores os substitutos, mais elástica a demanda."),
        ],
        "grafico_verso": "ECO-E1-0086-1-V1",
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item disfarça a regra “substitutos ↑ → "
                       "elasticidade ↑” num cenário concreto e longo. O “deve apresentar” (tendência) deixa a "
                       "comparação segura. Quem lê rápido pode achar que o inverno torna a eletricidade "
                       "“essencial” nas duas cidades por igual — o que muda é a existência da alternativa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…deve apresentar elasticidade-preço da demanda por eletricidade menor que a de outra cidade em que "
            "haja somente sistemas elétricos…”</i> → ERRADO (inversão: o substituto aumenta a elasticidade)",
            "<i>“Na cidade que só dispõe de aquecimento elétrico, um aumento da tarifa tende a elevar o gasto das "
            "famílias com eletricidade.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": ("Substitutos elevam a sensibilidade ao preço; com gás disponível, a alta da energia "
                             "leva à troca e a demanda por eletricidade é mais elástica; sem alternativa, menos "
                             "elástica. Fatores: substitutos, essencialidade, peso no orçamento, horizonte de "
                             "tempo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [BANCA_PROVAVEL],
    },
    # ------------------------------------------------------------------ E1-0087
    {
        "id": "ECO-E1-0087-1", "fonte_ref": "E1-0087", "destino": "02", "subtema": H2["ofe"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2017", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da oferta e ao equilíbrio de mercado.",
        "rotulo_item": "Item",
        "assertiva": ("Se a oferta de um bem tiver elasticidade zero em relação ao preço, a demanda determinará "
                      "unicamente o preço de equilíbrio da transação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a oferta de um bem tiver <u>elasticidade zero</u> em relação ao preço, a demanda "
                      "determinará <u>unicamente</u> o preço de equilíbrio da transação."),
        "poucas": ("Oferta com elasticidade zero é " + azb("vertical") + ": a quantidade está fixada. A demanda "
                   "não consegue mudar a quantidade — só o " + vd("preço") + "."),
        "destrinchando": [
            azb("Elasticidade-preço da oferta") + " = %ΔQ<sup>s</sup> / %ΔP. Se é " + vd("zero") + ", a "
            "quantidade ofertada não reage ao preço: a curva de oferta é uma reta vertical em Q* "
            "(" + azb("perfeitamente inelástica") + ").",
            "Equilíbrio: qualquer curva de demanda cruza a oferta em Q*. Demanda maior (D → D′) só eleva o preço "
            "(P → P′); demanda menor só o reduz. O “unicamente” está certo: a demanda determina o preço, e só "
            "ele.",
            "Exemplos: terra urbana numa localização dada, ingressos de um estádio, obras de um pintor já falecido "
            "e, no curtíssimo prazo, o peixe que chegou ao mercado e precisa ser vendido no dia — o "
            + azb("período de mercado") + " de " + oc("Alfred Marshall") + ".",
            "Consequência tributária: com oferta vertical, um imposto recai inteiramente sobre o vendedor e não "
            "gera peso morto (a quantidade não muda). É o argumento de " + oc("Henry George") + " para o "
            "imposto sobre a renda da terra.",
            "Espelho: oferta " + azb("perfeitamente elástica") + " (horizontal) → o preço fica fixado pela oferta "
            "e a demanda determina apenas a quantidade.",
        ],
        "grafico_verso": "ECO-E1-0087-1-V1",
        "dissecando": (cz("[contraintuitivo · literalidade]") + " O “unicamente” costuma denunciar erro, mas aqui "
                       "descreve o caso-limite com precisão. Atenção ao objeto: o item fala de <b>oferta</b> "
                       "inelástica, não de demanda — quem troca as curvas conclui o contrário."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a oferta de um bem tiver elasticidade zero em relação ao preço, um aumento da demanda elevará "
            "o preço e a quantidade de equilíbrio.”</i> → ERRADO (a quantidade é fixa: só o preço sobe)",
            "<i>“Se a oferta de um bem for infinitamente elástica, deslocamentos da demanda alterarão apenas a "
            "quantidade de equilíbrio.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["unicamente"], "dificuldade": 1,
        "comentario_fonte": ("Elasticidade zero da oferta = curva vertical; a quantidade é sempre Q*; qualquer "
                             "demanda determina apenas o preço (D → P; D′ → P′). Exemplo: recurso com estoque dado "
                             "pela natureza."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [
            {"ref": "image (47).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
             "acao": "redesenhada (ECO-E1-0087-1-V1; original " + NAO_PRESERVADA + ", conteúdo descrito no "
                     "comentário: oferta vertical em Q*, D e D′, P e P′)"},
            {"ref": "image (48).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
             "acao": "absorvida (mesmo gráfico, em ECO-E1-0087-1-V1)"}],
        "alertas": [BANCA_PROVAVEL,
                    "qualidade_fonte: um comentário de origem repete “se o preço estiver alto” nas duas linhas "
                    "(a segunda deveria ser “baixo”) — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0088
    {
        "id": "ECO-E1-0088-1", "fonte_ref": "E1-0088", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Bens de consumo essencial tendem a ter elasticidade-preço da demanda menor do que bens de "
                      "consumo supérfluo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Bens de consumo essencial <u>tendem a</u> ter elasticidade-preço da demanda <u>menor</u> do "
                      "que bens de consumo supérfluo."),
        "poucas": ("Do essencial não se abre mão: quando o preço sobe, a quantidade cai pouco — |ε| "
                   + vd("menor") + ". O supérfluo é o primeiro a ser cortado — |ε| maior."),
        "destrinchando": [
            "Elasticidade-preço = sensibilidade da quantidade demandada ao preço, comparada sempre em "
            + azb("módulo") + ". “Menor” aqui significa menos sensível.",
            "Essencial (sal, arroz, remédio de uso contínuo, energia): o consumidor mantém o consumo mesmo com "
            "preço maior → " + azb("inelástica") + " (|ε| < 1). Supérfluo (viagem de lazer, restaurante, "
            "joias): fácil de adiar ou cortar → " + azb("elástica") + " (|ε| > 1).",
            "Os determinantes costumam andar juntos: o sal é essencial, não tem substituto próximo e pesa quase "
            "nada no orçamento — três razões para a demanda inelástica. Os outros determinantes são o horizonte "
            "de tempo e a amplitude da definição do mercado.",
            "Não confundir com a " + azb("elasticidade-renda") + ": “bem necessário” (0 < η < 1) × “bem de luxo” "
            "(η > 1) classifica pela reação à <b>renda</b>. Os conceitos se correlacionam, mas são medidas "
            "diferentes.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Regra direta de manual, protegida pelo "
                       "“tendem a”. Em itens desse tipo, o erro costuma vir da inversão (essencial → mais "
                       "elástica) ou de um absoluto (“essenciais têm elasticidade nula”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens de consumo essencial têm elasticidade-preço da demanda nula.”</i> → ERRADO (modulador "
            "absoluto: são inelásticos, não perfeitamente inelásticos)",
            "<i>“A demanda de um produto será mais elástica se ele for extremamente essencial ao "
            "consumidor.”</i> → ERRADO (inversão)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tendem a"], "dificuldade": 1,
        "comentario_fonte": ("Quanto mais essencial, menor a elasticidade-preço (em módulo); supérfluos são mais "
                             "elásticos porque podem ser dispensados; exemplos: sal, arroz, feijão."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [BANCA_PROVAVEL],
    },
    # ------------------------------------------------------------------ E1-0089
    {
        "id": "ECO-E1-0089-1", "fonte_ref": "E1-0089", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às elasticidades-preço da demanda e da oferta.",
        "rotulo_item": "Item",
        "assertiva": ("Por ser um serviço vital aos seus usuários, a hemodiálise pode ser considerada um serviço de "
                      "oferta preço-inelástica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Por ser um serviço vital aos seus usuários, a hemodiálise pode ser considerada um serviço "
                      "de ") + vm("oferta") + az(" preço-inelástica."),
        "poucas": ("Ser vital para o <b>usuário</b> diz respeito ao comprador: torna a " + azb("demanda")
                   + " inelástica. A elasticidade da " + azb("oferta") + " depende de fatores do lado do "
                   "produtor."),
        "destrinchando": [
            "Essencialidade é determinante da " + azb("elasticidade-preço da demanda") + ": o paciente renal não "
            "pode deixar de fazer as sessões se o preço sobe → quantidade demandada quase insensível ao preço.",
            "A " + azb("elasticidade-preço da oferta") + " (%ΔQ<sup>s</sup>/%ΔP) depende de quão fácil é expandir "
            "a produção quando o preço sobe: capacidade ociosa, disponibilidade de insumos (máquinas, "
            "nefrologistas, técnicos treinados), tempo para investir, custo de estocar.",
            "A oferta de hemodiálise até pode ser inelástica no curto prazo — equipamentos caros e mão de obra "
            "especializada não surgem de um dia para o outro —, mas por motivos de <b>produção</b>, não porque o "
            "serviço é vital para quem o consome.",
            vm("Regra-âncora: característica do consumidor (necessidade, hábito, substitutos) → demanda; "
               "característica da produção (capacidade, insumos, tempo) → oferta."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " A banca trocou “demanda” por “oferta” e "
                       "manteve uma justificativa que só serve para a demanda. Pista: “vital aos seus "
                       "<b>usuários</b>” — usuário é quem demanda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por ser um serviço vital aos seus usuários, a hemodiálise pode ser considerada um serviço de "
            "demanda preço-inelástica.”</i> → CERTO",
            "<i>“Por ser um serviço vital, a hemodiálise tem demanda perfeitamente inelástica.”</i> → ERRADO "
            "(modulador absoluto: inelástica não é elasticidade zero)",
        ])],
        "reescrita": ("Por ser um serviço vital aos seus usuários, a hemodiálise pode ser considerada um serviço "
                      "de " + hl("demanda") + " preço-inelástica."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("A banca trocou demanda por oferta; ser vital para os usuários torna a demanda "
                             "preço-inelástica; a oferta pode até ser inelástica por falta de insumos e "
                             "profissionais treinados, mas não pelo motivo dado."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [BANCA_PROVAVEL,
                    "qualidade_fonte: um dos comentários de origem trata a hemodiálise como serviço para “doença "
                    "rara” e conclui por elasticidade nula — descartado"],
    },
    # ------------------------------------------------------------------ E1-0091
    {
        "id": "ECO-E1-0091-1", "fonte_ref": "E1-0091", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-renda da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Um produto ter elasticidade-renda unitária significa que um aumento de percentual na renda "
                      "do consumidor não produzirá efeito na receita total auferida pelo vendedor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um produto ter elasticidade-renda unitária significa que um aumento de percentual na renda "
                      "do consumidor ") + vm("não produzirá efeito na receita total")
                   + az(" auferida pelo vendedor."),
        "poucas": ("Elasticidade-renda " + vd("unitária") + ": renda +10% → quantidade demandada +10%. A preço "
                   "constante, a receita do vendedor também sobe " + vd("10%") + ". Quem deixa a receita intacta "
                   "é a elasticidade-<b>preço</b> unitária."),
        "destrinchando": [
            azb("Elasticidade-renda") + ": η = %ΔQ / %ΔR. Classificação: " + vd("η < 0") + " → bem inferior; "
            + vd("0 < η < 1") + " → normal necessário; " + vd("η > 1") + " → normal de luxo (superior); η = 1 → "
            "fronteira entre os dois.",
            "Com η = 1, a quantidade cresce na mesma proporção da renda: o gasto com o bem é uma " + azb("fração "
            "constante") + " do orçamento. O vendedor, que recebe esse gasto, vê sua receita crescer no mesmo "
            "ritmo da renda.",
            "A confusão do item vem da " + azb("elasticidade-preço unitária") + ": aí, se o preço sobe 10%, a "
            "quantidade cai 10% e a receita (p × q) fica constante. São perguntas diferentes: a elasticidade-"
            "preço desloca o consumidor <b>ao longo</b> da curva; a elasticidade-renda <b>desloca</b> a curva.",
            "Aplicação clássica: a " + azb("Lei de Engel") + " (" + oc("Ernst Engel") + ", séc. XIX) — a parcela "
            "da renda gasta com alimentação cai quando a renda sobe, porque alimentos têm η < 1.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item pega a propriedade da elasticidade-<b>preço</b> "
                       "unitária (receita constante) e a cola na elasticidade-<b>renda</b> unitária. Pista: renda "
                       "maior com preço inalterado só pode aumentar ou reduzir compras — e, sendo η = 1 > 0, "
                       "aumenta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade-preço da demanda for unitária, uma variação percentual no preço não altera a "
            "receita total do vendedor.”</i> → CERTO",
            "<i>“Com elasticidade-renda unitária, a participação do bem no orçamento do consumidor cresce quando "
            "a renda aumenta.”</i> → ERRADO (permanece constante)",
        ])],
        "reescrita": ("Um produto ter elasticidade-renda unitária significa que um aumento de percentual na renda "
                      "do consumidor " + hl("produzirá, mantido o preço, aumento de igual percentual na quantidade "
                      "demandada e na receita total") + " auferida pelo vendedor."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Elasticidade-renda unitária: renda +x% → demanda +x%; participação no orçamento "
                             "constante; a receita do vendedor sobe na mesma proporção. Seria correto para a "
                             "elasticidade-preço unitária."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [BANCA_PROVAVEL],
    },
    # ------------------------------------------------------------------ E1-0092
    {
        "id": "ECO-E1-0092-1", "fonte_ref": "E1-0092", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda e à receita total.",
        "rotulo_item": "Item",
        "assertiva": ("Quando a demanda por um bem é inelástica, um aumento de preço leva a uma diminuição "
                      "proporcionalmente menor da quantidade demandada. Diante disso, a Receita Total do "
                      "ofertante aumenta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando a demanda por um bem é inelástica, um aumento de preço leva a uma diminuição "
                      "<u>proporcionalmente menor</u> da quantidade demandada. Diante disso, a Receita Total do "
                      "ofertante <u>aumenta</u>."),
        "poucas": ("Inelástica = |ε| < 1: a quantidade cai " + vd("menos, em %") + ", do que o preço sobe. Como "
                   "RT = P × Q, o efeito do preço vence e a " + azb("receita total sobe") + "."),
        "destrinchando": [
            "Regra prática: " + vd("%ΔRT ≈ %ΔP + %ΔQ") + ". Preço +10% e quantidade −4% → RT ≈ +6%.",
            "Os três casos, para uma alta de preço: " + azb("inelástica") + " (|ε| < 1) → RT sobe; "
            + azb("elástica") + " (|ε| > 1) → RT cai; " + azb("unitária") + " (|ε| = 1) → RT constante. Para "
            "uma queda de preço, tudo se inverte.",
            "Receita do ofertante e " + azb("gasto do consumidor") + " são o mesmo número visto de lados "
            "diferentes: o item vale igualmente para “o gasto com o bem aumenta”.",
            "Ligação com a receita marginal: " + vd("RMg = P (1 − 1/|ε|)") + ". No trecho inelástico, RMg < 0 — "
            "vender uma unidade a mais (baixando o preço) reduz a receita. Por isso quem tem poder de mercado "
            "não opera ali.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição seguida da consequência correta. O risco é a leitura "
                       "intuitiva “quantidade caiu → receita caiu”; a palavra decisiva é "
                       "“proporcionalmente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando a demanda por um bem é inelástica, um aumento de preço reduz a Receita Total do "
            "ofertante.”</i> → ERRADO (isso vale para a demanda elástica)",
            "<i>“Quando a demanda é elástica, uma redução de preço eleva a receita total do ofertante.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Gabarito “CORRETO”, com imagem e link de canal do Telegram; sem texto explicativo.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (38).png", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (" + NAO_PRESERVADA + "; conteúdo coberto pelo 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0098
    {
        "id": "ECO-E1-0098-1", "fonte_ref": "E1-0098", "destino": "02", "subtema": H2["ofe"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da oferta.",
        "rotulo_item": "Item",
        "assertiva": ("Mudanças lentas e previsíveis na curva de demanda de um mercado são compatíveis com uma curva "
                      "de oferta com alta elasticidade-preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Mudanças <u>lentas e previsíveis</u> na curva de demanda de um mercado são "
                      "<u>compatíveis</u> com uma curva de oferta com alta elasticidade-preço."),
        "poucas": ("Se a demanda muda devagar e de forma antecipável, os produtores têm " + azb("tempo para "
                   "ajustar") + " capacidade, mão de obra e insumos: a quantidade ofertada acompanha o preço — "
                   + vd("oferta elástica") + "."),
        "destrinchando": [
            "A " + azb("elasticidade-preço da oferta") + " depende sobretudo de quanto a produção pode ser "
            "expandida ou contraída quando o preço muda: capacidade ociosa, mobilidade de fatores, estoques e, "
            "acima de tudo, " + vd("tempo") + ".",
            "Demanda que cresce lenta e previsivelmente é planejável: a firma investe antes, contrata, amplia a "
            "planta. A oferta relevante é a de " + azb("longo prazo") + ", mais elástica: o ajuste vem pela "
            "quantidade, e o preço varia pouco.",
            "Contraste: choques súbitos de demanda (hotéis numa final de Copa, máscaras no início da pandemia) "
            "encontram oferta rígida de curto prazo — o ajuste vem pelo preço, que dispara.",
            "Na tipologia de " + oc("Alfred Marshall") + ": período de mercado (oferta vertical) → curto prazo "
            "(capacidade dada, oferta inclinada) → longo prazo (capacidade variável, oferta mais elástica, até "
            "horizontal em indústrias de custo constante).",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item não diz que a demanda “causa” a "
                       "elasticidade: diz que os dois são <b>compatíveis</b> — formulação modesta e verdadeira. O "
                       "candidato que procura um nexo causal rígido tende a marcar ERRADO sem motivo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Choques súbitos e imprevistos de demanda tendem a encontrar oferta muito elástica, o que mantém "
            "os preços estáveis.”</i> → ERRADO (inversão: no curto prazo a oferta é rígida e o preço salta)",
            "<i>“A elasticidade-preço da oferta tende a ser maior no longo prazo do que no curto prazo.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["compatíveis"], "dificuldade": 2,
        "comentario_fonte": "Mudanças lentas e previsíveis permitem ajustes na oferta, elevando sua elasticidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0099
    {
        "id": "ECO-E1-0099-1", "fonte_ref": "E1-0099", "destino": "02", "subtema": H2["rec"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda e à receita total.",
        "rotulo_item": "Item",
        "assertiva": ("Após estudos, uma consultoria determinou que o equilíbrio do mercado do bem Y encontra-se em "
                      "um ponto de baixa elasticidade-preço da demanda. É previsível que os fornecedores com poder "
                      "de mercado aumentem os preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Após estudos, uma consultoria determinou que o equilíbrio do mercado do bem Y encontra-se em "
                      "um ponto de <u>baixa elasticidade-preço</u> da demanda. É previsível que os fornecedores "
                      "<u>com poder de mercado</u> aumentem os preços."),
        "poucas": ("No trecho " + azb("inelástico") + ", subir o preço " + vd("aumenta a receita") + " e, como "
                   "se vende menos, reduz o custo: o lucro sobe. Quem pode fixar preço (poder de mercado) "
                   "tem todo incentivo a elevá-lo."),
        "destrinchando": [
            "Com |ε| < 1, preço ↑ → quantidade ↓ proporcionalmente menos → " + vd("RT = P × Q ↑") + ". E produzir "
            "menos custa menos. Receita maior + custo menor = lucro maior, sem ambiguidade.",
            "Em linguagem de margem: " + vd("RMg = P (1 − 1/|ε|)") + " é <b>negativa</b> quando |ε| < 1. Uma "
            "firma com poder de mercado maximiza lucro onde RMg = CMg > 0, logo " + azb("nunca opera no trecho "
            "inelástico") + ": vai subindo o preço até alcançar a parte elástica da demanda.",
            "Daí o índice de " + oc("Lerner") + ", " + vd("(P − CMg)/P = 1/|ε|") + ": só faz sentido com |ε| > 1, "
            "e a margem é maior quanto menos elástica a demanda.",
            "O qualificador “com poder de mercado” é essencial. Em concorrência perfeita, cada firma é "
            + azb("tomadora de preço") + " — a demanda que ela enfrenta é horizontal (perfeitamente elástica), "
            "mesmo que a demanda do mercado seja inelástica. Sozinha, ela não sobe o preço; só um cartel "
            "conseguiria.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item é seguro porque restringe a conclusão aos "
                       "fornecedores <b>com poder de mercado</b> e usa “previsível”, não “necessário”. Tire esse "
                       "qualificador e o item fica discutível (tomadores de preço não escolhem preço)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em concorrência perfeita, diante de demanda de mercado inelástica, cada produtor individual "
            "elevará seu preço para aumentar a receita.”</i> → ERRADO (tomador de preço: a demanda da firma é "
            "perfeitamente elástica)",
            "<i>“Um monopolista maximizador de lucro não opera no trecho inelástico da curva de demanda.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["previsível", "com poder de mercado"],
        "dificuldade": 2,
        "comentario_fonte": "Com baixa elasticidade-preço, o aumento do preço eleva a receita total, porque a "
                            "quantidade demandada cai pouco.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0100
    {
        "id": "ECO-E1-0100-1", "fonte_ref": "E1-0100", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": "A elasticidade será perfeita quando for igual a zero.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elasticidade será perfeita quando for ") + vm("igual a zero") + az("."),
        "poucas": ("Demanda “perfeitamente elástica” é a de elasticidade " + vd("infinita") + " (curva "
                   "horizontal). Elasticidade " + vd("zero") + " é o extremo oposto: demanda "
                   + azb("perfeitamente inelástica") + " (curva vertical)."),
        "destrinchando": [
            "A escala da elasticidade-preço, em módulo: " + vd("|ε| = 0") + " → perfeitamente inelástica "
            "(vertical: a quantidade não reage ao preço); " + vd("0 < |ε| < 1") + " → inelástica; " + vd("|ε| = 1")
            + " → unitária (gasto constante); " + vd("|ε| > 1") + " → elástica; " + vd("|ε| → ∞") + " → "
            "perfeitamente elástica (horizontal: ao menor aumento de preço, a quantidade vai a zero).",
            "Exemplo de horizontal: a demanda que a firma de " + azb("concorrência perfeita") + " enfrenta — se "
            "cobrar um centavo acima do mercado, não vende nada. Exemplo aproximado de vertical: a dose de um "
            "medicamento sem substituto, que o paciente compra a qualquer preço (dentro da renda).",
            "“Perfeita” qualifica o grau máximo de <b>elasticidade</b>; “perfeitamente inelástica”, o grau "
            "máximo de inelasticidade. O zero é o fim da escala da inelasticidade, não da elasticidade.",
        ],
        "dissecando": (cz("[inversão]") + " O item troca os extremos da escala. Redação curta e vaga "
                       "(“a elasticidade será perfeita”), típica de questionário; a resposta sai da tabela dos "
                       "cinco casos. A banca também cobra a versão mais precisa (“…perfeitamente elástica se sua "
                       "elasticidade-preço for igual a zero”), igualmente ERRADO."),
        "modulos": [("🧠 Mnemônico", [
            "Perfeitamente <b>I</b>nelástica tem a forma de um <b>I</b> (vertical, ε = 0); perfeitamente "
            "<b>E</b>lástica é um horizonte que se <b>E</b>stende ao infinito (horizontal, ε = ∞)."]),
            ("😈 Para dificultar", [
                "<i>“A demanda será perfeitamente inelástica quando sua elasticidade-preço for igual a zero.”</i> "
                "→ CERTO",
                "<i>“A demanda perfeitamente elástica é representada por uma reta vertical.”</i> → ERRADO (é "
                "horizontal)",
            ])],
        "reescrita": "A elasticidade será perfeita quando for " + hl("infinita") + ".",
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Elasticidade perfeita = elasticidade-preço infinita; igual a zero = demanda "
                             "perfeitamente inelástica."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (17).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (" + NAO_PRESERVADA + "; conteúdo coberto pelo 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0107-1 (mesmo erro — zero × infinito —, redação mais precisa)"],
    },
    # ------------------------------------------------------------------ E1-0101
    {
        "id": "ECO-E1-0101-1", "fonte_ref": "E1-0101", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": "A demanda de um bem será mais inelástica se não houver substitutos no mercado.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A demanda de um bem será <u>mais inelástica</u> se <u>não houver substitutos</u> no "
                      "mercado."),
        "poucas": ("Sem " + azb("substitutos") + ", o consumidor não tem para onde migrar quando o preço sobe: "
                   "a quantidade demandada cai pouco — demanda " + vd("mais inelástica") + "."),
        "destrinchando": [
            "A existência de substitutos próximos é o determinante mais forte da elasticidade-preço. Com "
            "alternativas, um aumento de preço faz o consumidor trocar de bem; sem elas, ele reduz pouco o "
            "consumo.",
            "A " + azb("amplitude da definição do mercado") + " muda a resposta: “alimentos” quase não têm "
            "substituto (muito inelástica); “feijão” tem alguns; “feijão da marca X” tem muitos (muito "
            "elástica). Quanto mais estreita a definição, mais substitutos — e mais elástica a demanda.",
            "Exemplos de pouca substituição: insulina, energia elétrica residencial no curto prazo, tarifa de "
            "pedágio na única estrada da região.",
            "Efeito prático: é sobre esses bens que o vendedor com poder de mercado consegue elevar preço sem "
            "perder receita, e onde tributos arrecadam muito com pouca distorção (regra de " + oc("Ramsey")
            + ").",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Regra direta, em forma comparativa (“mais inelástica”), o que "
                       "a torna segura. A banca também cobra a versão com “mais elástica”, que é ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda de um produto será mais elástica se não houver produtos substitutos no "
            "mercado.”</i> → ERRADO (inversão)",
            "<i>“Na ausência de substitutos, a demanda de um bem será perfeitamente inelástica.”</i> → ERRADO "
            "(modulador absoluto: será menos elástica, não de elasticidade zero)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["mais"], "dificuldade": 1,
        "comentario_fonte": "A ausência de substitutos torna a demanda mais inelástica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0110-1 (versão ERRADA do par, com “mais elástica”)"],
    },
    # ------------------------------------------------------------------ E1-0102
    {
        "id": "ECO-E1-0102-1", "fonte_ref": "E1-0102", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço.",
        "rotulo_item": "Item",
        "assertiva": "A elasticidade no longo prazo pode diferir daquela vigente no curto prazo.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elasticidade no longo prazo <u>pode diferir</u> daquela vigente no curto prazo."),
        "poucas": ("O " + azb("horizonte de tempo") + " é determinante da elasticidade: com mais tempo, "
                   "consumidores e produtores encontram substitutos e ajustam hábitos e equipamentos — em geral, "
                   "a elasticidade " + vd("cresce") + " no longo prazo."),
        "destrinchando": [
            "Caso típico: a gasolina. No curto prazo, quem depende do carro paga mais e roda quase o mesmo "
            "(inelástica). No longo prazo, troca por um carro econômico, muda de casa, usa transporte coletivo — "
            "a quantidade cai muito mais. Por isso a demanda de longo prazo é " + vd("mais elástica") + ".",
            "Exceção que a banca adora: " + azb("bens duráveis") + " (carros, geladeiras). Diante de uma alta de "
            "preço, o consumidor <b>adia</b> a troca e a compra despenca no curto prazo; no longo prazo, o "
            "estoque envelhece e a reposição volta. Aí a demanda é mais elástica no <b>curto</b> prazo "
            "(exemplo de " + oc("Pindyck e Rubinfeld") + ").",
            "Na oferta vale o mesmo raciocínio: em geral mais elástica no longo prazo (tempo para ampliar a "
            "capacidade); exceção na oferta de material reciclado, que reage forte no curto prazo.",
            "O “pode diferir” cobre os dois sentidos — por isso o item é inatacável.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “pode” salva o item: não afirma em que sentido a "
                       "elasticidade muda, só que muda. A banca transforma esse tema em ERRADO com absolutos "
                       "(“é sempre maior no longo prazo”) ou trocando o sentido para bens duráveis."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-preço da demanda é sempre maior no longo prazo do que no curto prazo.”</i> → "
            "ERRADO (modulador absoluto: duráveis são exceção)",
            "<i>“A demanda por gasolina tende a ser mais elástica no longo prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("A elasticidade-preço pode ser maior no longo prazo, porque os consumidores têm mais "
                             "tempo para ajustar seu comportamento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0103
    {
        "id": "ECO-E1-0103-1", "fonte_ref": "E1-0103", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": "As alterações no ponto da curva de demanda não alteram a elasticidade-preço.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As alterações no ponto da curva de demanda ") + vm("não alteram") + az(" a "
                      "elasticidade-preço."),
        "poucas": ("Em regra, a elasticidade-preço " + azb("muda ao longo da curva") + ": na demanda linear, "
                   "vai de muito elástica (preço alto) a muito inelástica (preço baixo). Constância é exceção "
                   "(curvas isoelásticas, vertical, horizontal)."),
        "destrinchando": [
            "Fórmula: " + vd("ε = (ΔQ/ΔP) · (P/Q)") + ". O primeiro fator é o inverso da inclinação; o segundo, "
            "a posição na curva. Numa reta, a inclinação é constante, mas P/Q muda de ponto a ponto — logo ε "
            "muda.",
            "Na reta Q = a − bP: |ε| é infinito no intercepto do preço (Q = 0), " + vd("1 no ponto médio")
            + " e zero no intercepto da quantidade (P = 0). Acima do meio, elástica; abaixo, inelástica.",
            "Exceções em que mudar de ponto não muda ε: " + azb("curva isoelástica") + " Q = A·P<sup>−b</sup> "
            "(ε = −b em todos os pontos; com b = 1, a hipérbole equilátera, gasto constante), a demanda vertical "
            "(ε = 0) e a horizontal (ε = ∞).",
            vm("Regra-âncora: inclinação não é elasticidade — reta tem inclinação constante e elasticidade "
               "variável."),
        ],
        "grafico_verso": "ECO-E1-0103-1-V1",
        "dissecando": (cz("[modulador absoluto]") + " O item transforma uma exceção (curvas isoelásticas) em "
                       "regra geral. A armadilha está em confundir inclinação com elasticidade: quem pensa “a "
                       "reta tem a mesma inclinação em tudo” marca CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao longo de uma curva de demanda do tipo Q = A/P, a elasticidade-preço é constante e "
            "unitária.”</i> → CERTO",
            "<i>“Numa demanda linear, a elasticidade-preço é constante porque a inclinação é constante.”</i> → "
            "ERRADO (confunde inclinação com elasticidade)",
        ])],
        "reescrita": ("As alterações no ponto da curva de demanda " + hl("em regra alteram") + " a "
                      "elasticidade-preço" + hl(" (exceto em curvas isoelásticas)") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A elasticidade-preço varia ao longo da curva de demanda, conforme o ponto.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (20).jpeg", "tipo_fonte": "GRÁFICO?", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0103-1-V1, conteúdo presumido; original "
                                   + NAO_PRESERVADA + ")"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0104
    {
        "id": "ECO-E1-0104-1", "fonte_ref": "E1-0104", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Com a existência de bens substitutos pode-se esperar maior elasticidade-preço da demanda de "
                      "um bem."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com a existência de bens substitutos <u>pode-se esperar</u> maior elasticidade-preço da "
                      "demanda de um bem."),
        "poucas": ("Havendo " + azb("substitutos") + ", um aumento de preço leva o consumidor a trocar de bem: "
                   "a quantidade demandada reage mais — " + vd("elasticidade maior") + "."),
        "destrinchando": [
            "Exemplo: se a tarifa do Uber sobe muito, parte dos passageiros vai para o táxi, o 99 ou o ônibus. "
            "Com alternativas à mão, a demanda por cada serviço é sensível ao seu próprio preço.",
            "O que importa é a <b>proximidade</b> do substituto: quanto mais parecido (mesma qualidade, mesmo "
            "uso, custo de troca baixo), maior a elasticidade. Marcas de um mesmo produto são substitutos "
            "próximos; categorias inteiras (transporte, alimento), não.",
            "Ligação com a " + azb("elasticidade cruzada") + ": dois bens são substitutos quando ε cruzada > 0. "
            "Quanto maior a cruzada, mais o preço de um bem “vaza” para a demanda do outro — e mais elástica a "
            "demanda própria de cada um.",
            "Custos de troca (fidelidade, contrato, aprendizado) funcionam como redutores da substituição: por "
            "isso empresas os criam deliberadamente — planos de fidelidade, ecossistemas fechados.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Regra de manual, protegida pelo "
                       "“pode-se esperar”. A versão ERRADA desse item costuma inverter o sentido (“reduz a "
                       "elasticidade”) ou trocar o modulador por um absoluto (“perfeitamente elástica”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A existência de bens substitutos reduz a elasticidade-preço da demanda de um bem.”</i> → ERRADO "
            "(inversão)",
            "<i>“A existência de bens substitutos torna a demanda de um bem perfeitamente elástica.”</i> → ERRADO "
            "(modulador absoluto: só se fossem substitutos perfeitos)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode-se esperar"],
        "dificuldade": 1,
        "comentario_fonte": ("Substitutos tornam a demanda mais elástica, pois o consumidor troca de produto; "
                             "exemplo: Uber × táxi."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0105
    {
        "id": "ECO-E1-0105-1", "fonte_ref": "E1-0105", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando uma curva de demanda na forma Q = a – bP, é correto afirmar que a elasticidade "
                      "preço não é a mesma para todos os pontos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando uma curva de demanda na forma <u>Q = a – bP</u>, é correto afirmar que a "
                      "elasticidade preço <u>não é a mesma</u> para todos os pontos."),
        "poucas": ("Na demanda linear, " + vd("ε = −bP/Q") + ": a inclinação é constante, mas a razão P/Q muda "
                   "a cada ponto. A elasticidade vai de " + vd("∞") + " (Q = 0) a " + vd("0") + " (P = 0)."),
        "destrinchando": [
            "Derivando Q = a − bP: dQ/dP = −b. Logo " + vd("ε = −b · P/Q = −bP/(a − bP)") + ". O numerador "
            "cresce e o denominador cai quando P sobe: |ε| aumenta à medida que se sobe pela curva.",
            "Três marcos: no intercepto do preço (Q = 0), |ε| → ∞; no " + azb("ponto médio") + " (P = a/2b, "
            "Q = a/2), " + vd("|ε| = 1") + "; no intercepto da quantidade (P = 0), ε = 0. Metade de cima: "
            "elástica; metade de baixo: inelástica.",
            "Consequência para a receita: no trecho elástico, baixar o preço eleva a receita; no inelástico, "
            "reduz. A receita total é " + azb("máxima no ponto médio") + " da reta (onde RMg = 0).",
            "Exemplo: Q = 10 − P. Em P = 8, Q = 2 → |ε| = 8/2 = " + vd("4") + ". Em P = 5, Q = 5 → "
            + vd("1") + ". Em P = 2, Q = 8 → " + vd("0,25") + ".",
            vm("Regra-âncora: reta tem inclinação constante e elasticidade variável."),
        ],
        "grafico_verso": "ECO-E1-0105-1-V1",
        "dissecando": (cz("[contraintuitivo]") + " O item aposta na confusão entre inclinação e elasticidade: a "
                       "reta “parece igual em todos os pontos”. Itens desse bloco cobram também o ponto de "
                       "elasticidade unitária no meio da reta e a receita máxima ali."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na demanda Q = a − bP, a elasticidade-preço é unitária no ponto médio da curva, onde a receita "
            "total é máxima.”</i> → CERTO",
            "<i>“Na demanda Q = a − bP, a demanda é inelástica nos preços mais altos.”</i> → ERRADO (inversão: é "
            "elástica nos preços altos)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Em uma demanda linear, a elasticidade-preço varia ao longo da curva.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (16).jpeg", "tipo_fonte": "GRÁFICO?", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0105-1-V1, conteúdo presumido; original "
                                   + NAO_PRESERVADA + ")"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0106
    {
        "id": "ECO-E1-0106-1", "fonte_ref": "E1-0106", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("A respeito da demanda, podemos afirmar que a existência de bens substitutos pode exercer "
                      "influência sobre a elasticidade de um bem."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A respeito da demanda, podemos afirmar que a existência de bens substitutos <u>pode exercer "
                      "influência</u> sobre a elasticidade de um bem."),
        "poucas": ("Substitutos são o principal " + azb("determinante da elasticidade-preço") + ": quanto mais "
                   "e melhores, mais elástica a demanda. O item afirma só que “pode influenciar” — "
                   + vd("verdadeiro") + " com folga."),
        "destrinchando": [
            "Os cinco determinantes clássicos da elasticidade-preço da demanda: (1) " + azb("substitutos")
            + " próximos (↑ elasticidade); (2) " + azb("essencialidade") + " (↓); (3) " + azb("peso no "
            "orçamento") + " — bem que pesa muito na renda gera reação maior (↑); (4) " + azb("tempo")
            + " — no longo prazo há mais ajuste (↑, com exceção dos duráveis); (5) " + azb("amplitude do "
            "mercado") + " — definição estreita (marca) tem mais substitutos que a ampla (categoria) (↑).",
            "Os determinantes se combinam: o sal é essencial, sem substituto e barato — demanda muito "
            "inelástica; uma marca de refrigerante tem dezenas de substitutos — muito elástica.",
            "A substituição também explica a forma da curva de demanda: quando o preço de um bem sobe, o "
            + azb("efeito substituição") + " leva o consumidor a trocar parte do consumo por outros bens.",
        ],
        "dissecando": (cz("[modulador relativo]") + " Afirmação de alcance mínimo (“pode exercer influência”): "
                       "não diz em que sentido nem quanto. Itens assim quase sempre são CERTO; o risco é o "
                       "candidato desconfiar da obviedade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A existência de bens substitutos não influencia a elasticidade-preço da demanda, que depende "
            "apenas da essencialidade do bem.”</i> → ERRADO (restrição indevida)",
            "<i>“Quanto maior a participação do gasto com o bem no orçamento do consumidor, maior tende a ser a "
            "elasticidade-preço da sua demanda.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Substitutos tornam a demanda mais elástica, pois os consumidores podem optar por "
                            "outros bens.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0101-1, ECO-E1-0104-1 (mesmo tema: substitutos × elasticidade-preço)"],
    },
    # ------------------------------------------------------------------ E1-0107
    {
        "id": "ECO-E1-0107-1", "fonte_ref": "E1-0107", "destino": "02", "subtema": H2["epd"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": "A demanda de um produto será perfeitamente elástica se sua elasticidade-preço for igual a zero.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A demanda de um produto será perfeitamente elástica se sua elasticidade-preço for ")
                   + vm("igual a zero") + az("."),
        "poucas": ("Elasticidade " + vd("zero") + " = demanda " + azb("perfeitamente inelástica") + " (vertical). "
                   "Perfeitamente elástica é a de elasticidade " + vd("infinita") + " (horizontal)."),
        "destrinchando": [
            azb("Perfeitamente inelástica") + " (ε = 0): a quantidade não muda, qualquer que seja o preço. "
            "Gráfico: reta <b>vertical</b>. Exemplo aproximado: a dose de insulina de que o paciente precisa.",
            azb("Perfeitamente elástica") + " (|ε| → ∞): a um preço dado, compra-se qualquer quantidade; um "
            "centavo acima, nada. Gráfico: reta <b>horizontal</b>. Exemplo: a demanda que a firma em "
            "concorrência perfeita enfrenta ao preço de mercado.",
            "Entre os extremos: 0 < |ε| < 1 inelástica; |ε| = 1 unitária; |ε| > 1 elástica.",
            "Consequências que a banca cobra: com demanda vertical, um imposto recai inteiro sobre o "
            "consumidor e não gera peso morto (a quantidade não muda); com demanda horizontal, recai inteiro "
            "sobre o produtor.",
        ],
        "grafico_verso": "ECO-E1-0107-1-V1",
        "dissecando": (cz("[inversão]") + " Troca os extremos: atribui ao zero o rótulo do infinito. A banca também "
                       "cobra a versão vaga (“A elasticidade será perfeita quando for igual a zero”), igualmente "
                       "ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda de um produto será perfeitamente inelástica se sua elasticidade-preço for igual a "
            "zero.”</i> → CERTO",
            "<i>“Com demanda perfeitamente elástica, um imposto sobre o produto é integralmente repassado ao "
            "consumidor.”</i> → ERRADO (recai inteiro sobre o produtor)",
        ])],
        "reescrita": ("A demanda de um produto será perfeitamente elástica se sua elasticidade-preço for "
                      + hl("infinita") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A demanda perfeitamente elástica tem elasticidade infinita; elasticidade zero = "
                             "demanda perfeitamente inelástica."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (17).jpeg", "tipo_fonte": "GRÁFICO?", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0107-1-V1, conteúdo presumido; original "
                                   + NAO_PRESERVADA + ")"}],
        "alertas": ["quase_duplicata: ECO-E1-0100-1 (mesmo erro — zero × infinito —, redação mais vaga)"],
    },
    # ------------------------------------------------------------------ E1-0108
    {
        "id": "ECO-E1-0108-1", "fonte_ref": "E1-0108", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando a relação de elasticidade-preço da demanda de um produto, a demanda desse "
                      "produto será mais elástica a longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Considerando a relação de elasticidade-preço da demanda de um produto, a demanda desse "
                      "produto <u>será</u> mais elástica a <u>longo prazo</u>."),
        "poucas": ("Com mais tempo, o consumidor encontra " + azb("substitutos") + " e muda hábitos e "
                   "equipamentos: em regra, a demanda é " + vd("mais elástica no longo prazo") + "."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O “será” não admite exceção, e os " + azb("bens duráveis") + " são a exceção de "
                          "manual: a demanda por carros e eletrodomésticos é mais elástica no <b>curto</b> prazo, "
                          "porque o consumidor adia a reposição. O CERTO se sustenta como regra geral (bens não "
                          "duráveis); numa prova que trouxesse duráveis, o item seria ERRADO.")],
        "destrinchando": [
            "Regra: o " + azb("horizonte de tempo") + " amplia a elasticidade. Gasolina: no curto prazo, roda-se "
            "quase o mesmo; no longo prazo, compram-se carros mais econômicos, muda-se de casa, usa-se "
            "transporte coletivo — a quantidade cai bem mais.",
            "Graficamente, pelo mesmo ponto inicial passam uma demanda de curto prazo " + azb("íngreme")
            + " e uma de longo prazo " + azb("mais plana") + ": a mesma alta de preço reduz pouco a quantidade "
            "no curto prazo e muito no longo.",
            "Exceção dos " + azb("duráveis") + " (" + oc("Pindyck e Rubinfeld") + "): a alta de preço faz o "
            "consumidor adiar a troca do carro — as compras caem muito de imediato e se recuperam depois, "
            "quando o estoque envelhece. Demanda mais elástica no curto prazo.",
            "Implicação de política: choques de preço do petróleo derrubam pouco o consumo no ano do choque e "
            "muito ao longo da década seguinte (eficiência, substituição de fontes).",
        ],
        "grafico_verso": "ECO-E1-0108-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Regra geral apresentada sem modulador (“será”). O "
                       "gabarito oficial a aceita; o detalhe que a tornaria ERRADA é a exceção dos duráveis. "
                       "Compare com a versão modalizada (“a elasticidade no longo prazo pode diferir daquela vigente no "
                       "curto prazo”), que não tem esse risco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda por automóveis tende a ser mais elástica no longo prazo do que no curto prazo.”</i> → "
            "ERRADO (duráveis: mais elástica no curto prazo)",
            "<i>“A demanda por gasolina tende a ser mais elástica no longo prazo do que no curto prazo.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["será"], "dificuldade": 2,
        "comentario_fonte": ("A demanda tende a ser mais elástica no longo prazo, pois os consumidores têm mais "
                             "tempo para ajustar seu comportamento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: assertiva sem modulador; a demanda de bens duráveis é mais elástica no curto "
                    "prazo (Pindyck e Rubinfeld) — gabarito CERTO mantido como regra geral",
                    "quase_duplicata: ECO-E1-0102-1 (mesmo tema, com o modalizador “pode diferir”)"],
    },
    # ------------------------------------------------------------------ E1-0109
    {
        "id": "ECO-E1-0109-1", "fonte_ref": "E1-0109", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": "A demanda de um produto será mais elástica se ele for extremamente essencial ao consumidor.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A demanda de um produto será ") + vm("mais elástica") + az(" se ele for extremamente "
                      "essencial ao consumidor."),
        "poucas": ("Essencialidade reduz a sensibilidade ao preço: do que é imprescindível não se abre mão. A "
                   "demanda é " + vd("mais inelástica") + ", não mais elástica."),
        "destrinchando": [
            "Quando o preço de um bem essencial sobe (remédio de uso contínuo, gás de cozinha, arroz), o "
            "consumidor corta outras despesas para mantê-lo: a quantidade demandada cai pouco → " + azb("demanda "
            "inelástica") + " (|ε| < 1).",
            "O supérfluo é o oposto: ao primeiro aumento de preço, é adiado ou cortado → " + azb("demanda "
            "elástica") + ".",
            "Cuidado com o exemplo intuitivo errado: “quem ganha mais não come mais arroz” fala da reação à "
            "<b>renda</b> (" + azb("elasticidade-renda") + " baixa), não ao preço. Os dois traços costumam vir "
            "juntos nos bens essenciais, mas são medidas diferentes.",
            vm("Regra-âncora: essencial → inelástica; supérfluo → elástica."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido da relação essencialidade × elasticidade. O "
                       "“extremamente” reforça a pista: quanto mais essencial, mais perto de elasticidade "
                       "zero. Versão CERTO do mesmo tema: “bens de consumo essencial tendem a ter elasticidade-preço "
                       "da demanda menor do que bens de consumo supérfluo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda de um produto tende a ser mais inelástica se ele for extremamente essencial ao "
            "consumidor.”</i> → CERTO",
            "<i>“Bens essenciais têm, necessariamente, elasticidade-preço da demanda igual a zero.”</i> → ERRADO "
            "(modulador absoluto)",
        ])],
        "reescrita": ("A demanda de um produto será " + hl("menos elástica (mais inelástica)") + " se ele for "
                      "extremamente essencial ao consumidor."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["extremamente"], "dificuldade": 1,
        "comentario_fonte": ("Bens essenciais costumam ter demanda inelástica; exemplo dado: ter mais dinheiro não "
                             "faz a pessoa consumir mais arroz ou feijão."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o exemplo de origem (renda maior não aumenta o consumo de arroz) ilustra "
                    "elasticidade-renda, não elasticidade-preço — corrigido no 📖",
                    "quase_duplicata: ECO-E1-0088-1 (versão CERTO do mesmo tema)"],
    },
    # ------------------------------------------------------------------ E1-0110
    {
        "id": "ECO-E1-0110-1", "fonte_ref": "E1-0110", "destino": "02", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos determinantes da elasticidade-preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": "A demanda de um produto será mais elástica se não houver produtos substitutos no mercado.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A demanda de um produto será ") + vm("mais elástica") + az(" se não houver produtos "
                      "substitutos no mercado."),
        "poucas": ("Sem " + azb("substitutos") + ", o consumidor não tem alternativa quando o preço sobe e "
                   "reduz pouco o consumo: a demanda fica " + vd("mais inelástica") + "."),
        "destrinchando": [
            "A elasticidade-preço mede quanto a quantidade demandada reage ao preço. A principal válvula dessa "
            "reação é a " + azb("substituição") + ": quem encontra outro bem que cumpre a mesma função foge do "
            "aumento.",
            "Sem substitutos — insulina, água encanada, o único pedágio no caminho — a fuga é impossível; o "
            "consumidor paga mais e mantém o consumo → " + azb("inelástica") + ". Com muitos substitutos (marcas "
            "de sabão em pó) → " + azb("elástica") + ".",
            "Efeito sobre a receita: é justamente nos bens sem substitutos que o vendedor com poder de mercado "
            "consegue subir preços e faturar mais (|ε| < 1 → preço ↑, receita ↑). Por isso a ausência de "
            "substitutos é critério central na análise de poder de mercado.",
            vm("Regra-âncora: mais substitutos → mais elástica; menos substitutos → mais inelástica."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sentido da regra. É a versão ERRADA de um par: a "
                       "banca também cobra a mesma frase com “mais inelástica” (CERTO). Em pares assim, decore a "
                       "regra, não a frase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda de um bem será mais inelástica se não houver substitutos no mercado.”</i> → CERTO",
            "<i>“A demanda de um produto será perfeitamente elástica se houver substitutos no mercado.”</i> → "
            "ERRADO (exagero: perfeitamente elástica exige substitutos perfeitos)",
        ])],
        "reescrita": ("A demanda de um produto será " + hl("mais inelástica") + " se não houver produtos "
                      "substitutos no mercado."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A ausência de substitutos torna a demanda mais inelástica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0101-1 (versão CERTO do par, com “mais inelástica”)"],
    },
    # ------------------------------------------------------------------ E1-0111
    {
        "id": "ECO-E1-0111-1", "fonte_ref": "E1-0111", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à elasticidade-preço cruzada da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Elasticidade-preço cruzada da demanda é a variação proporcional na quantidade demandada de um "
                      "dado bem dividida pela variação proporcional no preço de outro bem."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Elasticidade-preço cruzada da demanda é a variação proporcional na quantidade demandada de "
                      "<u>um dado bem</u> dividida pela variação proporcional no preço de <u>outro bem</u>."),
        "poucas": ("Definição exata: " + vd("ε<sub>xy</sub> = %ΔQ<sub>x</sub> / %ΔP<sub>y</sub>") + ". "
                   "“Proporcional” = percentual; o preço é de <b>outro</b> bem — se fosse do próprio, seria a "
                   "elasticidade-preço direta."),
        "destrinchando": [
            "Família das elasticidades da demanda: " + azb("preço direta") + " (%ΔQ<sub>x</sub>/%ΔP<sub>x</sub>), "
            + azb("cruzada") + " (%ΔQ<sub>x</sub>/%ΔP<sub>y</sub>) e " + azb("renda")
            + " (%ΔQ<sub>x</sub>/%ΔR). Todas usam variações percentuais, o que as torna independentes de "
            "unidades.",
            "Uso: classificar a relação entre os bens — " + vd("ε > 0") + " substitutos; " + vd("ε < 0")
            + " complementares; " + vd("ε = 0") + " independentes.",
            "Exemplo numérico: o preço do café sobe 10% e a compra de chá sobe 4% → ε<sub>chá,café</sub> = "
            + vd("+0,4") + " (substitutos). O preço da impressora sobe 10% e a venda de cartuchos cai 6% → "
            + vd("−0,6") + " (complementares).",
            "Em variações grandes, usa-se a " + azb("fórmula do ponto médio (arco)") + ", que divide cada "
            "variação pela média dos valores inicial e final, para o resultado não depender do sentido da "
            "mudança.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. Itens ERRADOS sobre ela costumam trocar o "
                       "“outro bem” pelo próprio bem (vira elasticidade direta) ou o preço pela renda (vira "
                       "elasticidade-renda)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Elasticidade-preço cruzada é a variação proporcional na quantidade demandada de um bem dividida "
            "pela variação proporcional no seu próprio preço.”</i> → ERRADO (troca de conceito: é a "
            "elasticidade-preço direta)",
            "<i>“Elasticidade-preço cruzada é a variação absoluta na quantidade demandada de um bem dividida pela "
            "variação absoluta no preço de outro bem.”</i> → ERRADO (absoluta × percentual)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Mede a sensibilidade da quantidade demandada de um bem à variação do preço de "
                             "outro; positiva → substitutos; negativa → complementares."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (19).jpeg, Untitled (22).jpeg", "tipo_fonte": "desconhecido",
                           "lado": "verso",
                           "acao": "irrecuperavel (" + NAO_PRESERVADA + "; conteúdo coberto pelo 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0112
    {
        "id": "ECO-E1-0112-1", "fonte_ref": "E1-0112", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às elasticidades-renda e preço da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("A elasticidade-renda da demanda pode ser positiva, nula ou negativa, ao passo em que a "
                      "elasticidade-preço da demanda é sempre negativa (fora do módulo) devido à lei geral da "
                      "demanda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A elasticidade-renda da demanda <u>pode ser positiva, nula ou negativa</u>, ao passo em que "
                      "a elasticidade-preço da demanda é <u>sempre negativa</u> (fora do módulo) <u>devido à lei "
                      "geral da demanda</u>."),
        "poucas": ("O sinal da " + azb("elasticidade-renda") + " depende do tipo de bem (normal, inferior, "
                   "neutro). O da " + azb("elasticidade-preço") + " é negativo porque preço e quantidade "
                   "demandada andam em sentidos opostos — a " + vd("lei da demanda") + "."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O “sempre” ignora o " + azb("bem de Giffen") + ", cuja demanda sobe com o preço "
                          "(elasticidade-preço positiva). O item se salva por ancorar o sinal na lei da demanda: "
                          "onde a lei vale, ε < 0. Numa prova que cobrasse Giffen, a versão “sempre negativa” "
                          "seria ERRADA.")],
        "destrinchando": [
            "Elasticidade-renda η = %ΔQ/%ΔR: " + vd("η > 0") + " → bem normal (necessário se 0 < η < 1; de luxo "
            "se η > 1); " + vd("η < 0") + " → bem " + azb("inferior") + " (a renda sobe, o consumo cai: "
            "transporte coletivo, carne de segunda); " + vd("η = 0") + " → bem de consumo saciado, "
            "insensível à renda (sal).",
            "Elasticidade-preço ε = %ΔQ/%ΔP: pela " + azb("lei da demanda") + ", preço ↑ → quantidade "
            "demandada ↓, então ε < 0. Por isso os manuais costumam trabalhar em " + azb("módulo") + " — daí o "
            "“fora do módulo” do item.",
            "A exceção teórica é o " + azb("bem de Giffen") + ": um bem inferior com peso tão grande no "
            "orçamento que o efeito renda (negativo) supera o efeito substituição — a alta do preço empobrece o "
            "consumidor, que passa a comprar <b>mais</b> do bem. É a única violação da lei da demanda dentro da "
            "teoria do consumidor; bens de Veblen (ostentação) às vezes são citados como outra.",
            "Todo Giffen é inferior, mas nem todo inferior é Giffen: na maioria dos inferiores, o efeito "
            "substituição domina e a lei da demanda vale.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item reúne duas regras de manual. O ponto sensível é o "
                       "“sempre”, normalmente sinal de ERRADO; aqui ele é atenuado por “devido à lei geral da "
                       "demanda”, que delimita o universo em que a afirmação vale."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elasticidade-renda da demanda é sempre positiva, pois o consumo cresce com a renda.”</i> → "
            "ERRADO (bens inferiores têm elasticidade-renda negativa)",
            "<i>“No caso de um bem de Giffen, a elasticidade-preço da demanda é positiva.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["pode", "sempre"], "dificuldade": 2,
        "comentario_fonte": ("A elasticidade-renda muda de sinal conforme o tipo de bem; a elasticidade-preço é "
                             "negativa pela lei da demanda."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (21).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (" + NAO_PRESERVADA + "; conteúdo coberto pelo 📖)"}],
        "alertas": ["contestavel: “sempre negativa” ignora o bem de Giffen; gabarito CERTO mantido porque o item "
                    "ancora o sinal na lei da demanda"],
    },
    # ------------------------------------------------------------------ E1-0113
    {
        "id": "ECO-E1-0113-1", "fonte_ref": "E1-0113", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à classificação dos bens pela elasticidade cruzada.",
        "rotulo_item": "Item",
        "assertiva": ("Se o aumento de preço do bem X provocar o aumento da demanda do bem Y, pode-se dizer que esses "
                      "bens X e Y são complementares."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o aumento de preço do bem X provocar o aumento da demanda do bem Y, pode-se dizer que "
                      "esses bens X e Y são ") + vm("complementares") + az("."),
        "poucas": ("P<sub>X</sub> ↑ → demanda de Y ↑ é elasticidade cruzada " + vd("positiva") + ": X e Y são "
                   + azb("substitutos") + ". Complementares reagiriam ao contrário (P<sub>X</sub> ↑ → demanda de "
                   "Y ↓)."),
        "destrinchando": [
            "Substitutos competem pela mesma necessidade: se X encarece, o consumidor migra para Y — a curva de "
            "demanda de Y se desloca para a <b>direita</b>. Ex.: o preço do etanol sobe e a demanda por "
            "gasolina aumenta (carros flex).",
            "Complementares são consumidos juntos: se X encarece, o conjunto encarece e a demanda de Y cai "
            "(curva para a <b>esquerda</b>). Ex.: o preço da gasolina sobe e a demanda por carros de alto "
            "consumo cai.",
            "Teste do sinal: ε<sub>YX</sub> = %ΔQ<sub>Y</sub>/%ΔP<sub>X</sub>. Os dois aumentam → sinal "
            + vd("+") + " → substitutos. Um sobe e o outro cai → sinal " + vd("−") + " → complementares.",
            "Note o vocabulário correto do item: o preço de X <b>desloca</b> a demanda de Y (“aumento da "
            "demanda”), não provoca movimento ao longo dela.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O mecanismo está descrito corretamente; só o rótulo final foi "
                       "trocado. Pista: “aumento… provocar o aumento” — mesmo sentido → sinal positivo → "
                       "substitutos."),
        "modulos": [("🧠 Mnemônico", ["<b>S</b>ubstituto: preços e demandas <b>S</b>obem juntos (sinal +); "
                                      "<b>C</b>omplementar: <b>C</b>ontrário (sinal −)."]),
                    ("😈 Para dificultar", [
                        "<i>“Se o aumento de preço do bem X provocar a redução da demanda do bem Y, X e Y são "
                        "complementares.”</i> → CERTO",
                        "<i>“Se o aumento de preço do bem X provocar o aumento da quantidade demandada do próprio "
                        "bem X, X é um bem substituto.”</i> → ERRADO (seria bem de Giffen, conceito trocado)",
                    ])],
        "reescrita": ("Se o aumento de preço do bem X provocar o aumento da demanda do bem Y, pode-se dizer que "
                      "esses bens X e Y são " + hl("substitutos") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode-se dizer"], "dificuldade": 1,
        "comentario_fonte": ("Complementares se movem juntos no consumo: aumento no preço de X reduziria a demanda "
                             "de Y."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (15).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (" + NAO_PRESERVADA + "; conteúdo coberto pelo 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0114
    {
        "id": "ECO-E1-0114-1", "fonte_ref": "E1-0114", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à classificação dos bens pela elasticidade cruzada.",
        "rotulo_item": "Item",
        "assertiva": "Se a elasticidade preço cruzada entre os bens A e B é positiva, então A e B são substitutos.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a elasticidade preço cruzada entre os bens A e B é <u>positiva</u>, então A e B são "
                      "<u>substitutos</u>."),
        "poucas": ("Cruzada " + vd("positiva") + " = o preço de um sobe e a demanda pelo outro também sobe: o "
                   "consumidor troca um pelo outro — " + azb("substitutos") + "."),
        "destrinchando": [
            "ε<sub>AB</sub> = %ΔQ<sub>A</sub>/%ΔP<sub>B</sub>. Sinal positivo: P<sub>B</sub> e Q<sub>A</sub> "
            "andam juntos. Ex.: a carne bovina sobe 10% e a compra de frango sobe 3% → ε = " + vd("+0,3") + ".",
            "Escala da substituição: ε cruzada alta → " + azb("substitutos próximos") + " (duas marcas de leite); "
            "baixa → substitutos fracos (cinema × streaming). No limite, substitutos perfeitos — o consumidor só "
            "compra o mais barato.",
            "Uso fora da sala de aula: autoridades de defesa da concorrência (no " + rx("Brasil")
            + ", o " + rx("CADE") + ") usam a substituibilidade pelo lado da demanda para delimitar o "
            + azb("mercado relevante") + " numa fusão.",
            "Rigor de manual: o critério de sinal identifica substitutos “brutos” (efeito total, com efeito "
            "renda). Em prova objetiva, a regra do sinal basta.",
        ],
        "dissecando": (cz("[literalidade]") + " Regra do sinal, sem armadilha. A banca também cobra o espelho com "
                       "sinal negativo (“…é negativa, então tais bens são complementares”), igualmente CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade-preço cruzada entre A e B é positiva, A e B são complementares.”</i> → ERRADO "
            "(sinal trocado)",
            "<i>“Se a elasticidade-renda da demanda de A é positiva, A e B são substitutos.”</i> → ERRADO (troca "
            "de conceito: elasticidade-renda classifica normal × inferior)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Cruzada positiva: aumento no preço de A eleva a demanda de B — substitutos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (23).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (" + NAO_PRESERVADA + "; conteúdo coberto pelo 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0011-1 (mesma regra do sinal, outra redação e outra origem)",
                    "quase_duplicata: ECO-E1-0115-1 (espelho com sinal negativo)"],
    },
    # ------------------------------------------------------------------ E1-0115
    {
        "id": "ECO-E1-0115-1", "fonte_ref": "E1-0115", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à classificação dos bens pela elasticidade cruzada.",
        "rotulo_item": "Item",
        "assertiva": "Se a elasticidade preço cruzada entre os bens A e B é negativa, então tais bens são complementares.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a elasticidade preço cruzada entre os bens A e B é <u>negativa</u>, então tais bens são "
                      "<u>complementares</u>."),
        "poucas": ("Cruzada " + vd("negativa") + " = o preço de um sobe e a demanda pelo outro cai: os bens são "
                   "consumidos juntos — " + azb("complementares") + "."),
        "destrinchando": [
            "Complementares formam um “pacote”: café e açúcar, impressora e cartucho, smartphone e plano de "
            "dados. Se um encarece, o pacote encarece e a demanda do outro cai — curva para a <b>esquerda</b>.",
            "Exemplo numérico: o preço do cartucho sobe 20% e a venda de impressoras cai 5% → ε = "
            + vd("−0,25") + ".",
            "No limite estão os " + azb("complementares perfeitos") + " (sapato esquerdo e direito), consumidos "
            "em proporção fixa — curvas de indiferença em L (preferências de " + oc("Leontief") + ").",
            "Estratégia empresarial ligada ao tema: vender o bem principal barato e lucrar no complementar "
            "(lâminas de barbear, cartuchos, consoles e jogos).",
        ],
        "dissecando": (cz("[literalidade]") + " Espelho do item com sinal positivo (positiva → substitutos, também "
                       "CERTO). A banca "
                       "costuma testar o par na mesma prova, trocando o sinal ou o rótulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a elasticidade-preço cruzada entre A e B é negativa, A e B são substitutos.”</i> → ERRADO "
            "(sinal trocado)",
            "<i>“Se a elasticidade-preço cruzada entre A e B é nula, os bens são independentes.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Cruzada negativa: aumento no preço de A reduz a demanda de B — complementares.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (18).jpeg", "tipo_fonte": "desconhecido", "lado": "verso",
                           "acao": "irrecuperavel (" + NAO_PRESERVADA + "; conteúdo coberto pelo 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0114-1 (espelho com sinal positivo)"],
    },
    # ------------------------------------------------------------------ E1-0116
    {
        "id": "ECO-E1-0116-1", "fonte_ref": "E1-0116", "destino": "02", "subtema": H2["ofe"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às elasticidades-preço da oferta e da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("Se a variação percentual da quantidade ofertada de um bem em relação à variação percentual do "
                      "preço deste mesmo bem é maior do que 1, é correto afirmar que esse bem apresenta demanda "
                      "elástica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a variação percentual da quantidade ofertada de um bem em relação à variação percentual "
                      "do preço deste mesmo bem é maior do que 1, é correto afirmar que esse bem apresenta ")
                   + vm("demanda") + az(" elástica."),
        "poucas": ("%ΔQ<b><sup>s</sup></b>/%ΔP > 1 é " + azb("oferta elástica") + ": a razão usa a quantidade "
                   "<b>ofertada</b>. Nada se pode concluir sobre a demanda."),
        "destrinchando": [
            azb("Elasticidade-preço da oferta") + ": ε<sub>s</sub> = %ΔQ<sup>s</sup>/%ΔP, positiva (lei da "
            "oferta). " + vd("ε<sub>s</sub> > 1") + " elástica; " + vd("= 1") + " unitária; " + vd("< 1")
            + " inelástica; 0 vertical; ∞ horizontal.",
            azb("Elasticidade-preço da demanda") + ": ε<sub>d</sub> = %ΔQ<sup>d</sup>/%ΔP, negativa. As duas "
            "medem coisas distintas (produtores × consumidores) e podem ter qualquer combinação: oferta elástica "
            "com demanda inelástica é perfeitamente possível.",
            "Determinantes também diferem: oferta depende de capacidade ociosa, insumos, tempo de ajuste; "
            "demanda, de substitutos, essencialidade, peso no orçamento.",
            "Curiosidade de prova: toda oferta linear que parte da origem (Q = cP) tem elasticidade " + vd("1")
            + " em todos os pontos; se corta o eixo do preço, é elástica; se corta o da quantidade, inelástica.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item descreve com precisão a elasticidade da oferta e "
                       "troca só a última palavra. Pista: “quantidade <b>ofertada</b>” no início e "
                       "“<b>demanda</b>” no fim."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é correto afirmar que esse bem apresenta oferta elástica.”</i> → CERTO",
            "<i>“Se a elasticidade-preço da oferta for maior que 1, a demanda pelo bem será necessariamente "
            "inelástica.”</i> → ERRADO (nexo indevido: são independentes)",
        ])],
        "reescrita": ("Se a variação percentual da quantidade ofertada de um bem em relação à variação percentual "
                      "do preço deste mesmo bem é maior do que 1, é correto afirmar que esse bem apresenta "
                      + hl("oferta") + " elástica."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O dado refere-se à oferta elástica, e não à demanda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0117
    {
        "id": "ECO-E1-0117-1", "fonte_ref": "E1-0117", "destino": "02", "subtema": H2["cruz"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às aplicações das elasticidades da demanda.",
        "rotulo_item": "Item",
        "assertiva": "Utiliza-se as elasticidades também para medir a “prioridade” de um certo bem no consumo.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Utiliza-se as elasticidades <u>também</u> para medir a “prioridade” de um certo bem no "
                      "consumo."),
        "poucas": ("A " + azb("elasticidade-renda") + " revela o lugar do bem na hierarquia do consumo: "
                   "necessidades (" + vd("0 < η < 1") + ") vêm primeiro; luxos (" + vd("η > 1") + ") ganham "
                   "espaço quando a renda sobe; inferiores (" + vd("η < 0") + ") são abandonados."),
        "destrinchando": [
            "Com renda baixa, o orçamento vai para o prioritário (alimento básico, moradia). À medida que a renda "
            "cresce, a fatia desses bens cai e a dos luxos sobe. Medir η de cada bem é medir essa ordem de "
            "prioridade.",
            "É a " + azb("Lei de Engel") + " (" + oc("Ernst Engel") + ", séc. XIX): a participação da "
            "alimentação no orçamento familiar cai com a renda — alimentos têm η < 1. As " + azb("curvas de "
            "Engel") + " (quantidade × renda) mostram o formato de cada bem.",
            "A elasticidade-preço complementa: bens prioritários (essenciais) têm demanda " + azb("inelástica")
            + " ao preço; supérfluos, elástica — o consumidor corta primeiro o que é menos prioritário.",
            "Aplicação: pesquisas de orçamento familiar (no " + rx("Brasil") + ", a " + rx("POF do IBGE")
            + ") fornecem os dados para estimar essas elasticidades e definem os pesos dos índices de preços "
            "ao consumidor.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Redação informal e vaga, com "
                       "“prioridade” entre aspas para sinalizar sentido figurado. O “também” reduz o alcance: as "
                       "elasticidades servem a isso, entre outros usos. Itens vagos assim tendem a CERTO quando "
                       "não há termo falso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens de luxo apresentam elasticidade-renda entre zero e um.”</i> → ERRADO (troca de conceito: "
            "luxo tem η > 1; entre 0 e 1 são os necessários)",
            "<i>“Pela Lei de Engel, a participação dos gastos com alimentação na renda das famílias diminui à "
            "medida que a renda aumenta.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["também"], "dificuldade": 2,
        "comentario_fonte": ("A elasticidade-renda identifica a prioridade de um bem no orçamento: alta (bens "
                             "superiores) indica demanda sensível à renda; baixa ou negativa (inferiores), menor "
                             "prioridade quando a renda aumenta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
