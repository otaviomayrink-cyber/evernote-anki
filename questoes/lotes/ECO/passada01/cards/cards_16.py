"""Cards da passada 01 de ECO — lote de redação 16 (notas 06, 07 e 07-A)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "cp": "💰 Custos de curto prazo",
    "lp": "📈 Custos de longo prazo e escala",
    "iso": "⚖️ Isocusto e combinação ótima",
    "comp": "🗺️ Comparação entre estruturas",
    "hip": "📐 Hipóteses e maximização de lucro",
    "ofcp": "⏱️ Curto prazo: oferta da firma",
    "lpcp": "⏳ Longo prazo e entrada/saída",
}

COMANDO_TJPA = ("Julgue o item a seguir, a respeito de determinação das curvas de procura, elasticidade, "
                "produtividade e custos de produção.")
COMANDO_NIDI_DEZ24 = ("Considerando a teoria da produção e suas implicações para o equilíbrio de curto e longo "
                      "prazo para empresas competitivas, julgue (C ou E) o item a seguir.")
COMANDO_CP = "Acerca do modelo de concorrência perfeita, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01724
    {
        "id": "ECO-E2-L01724-1", "fonte_ref": "E2-L01724", "destino": "06", "subtema": H2["lp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "A respeito da teoria da produção e dos custos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, uma firma que tem dois insumos, capital (fixo) e trabalho (variável), pode "
                      "atingir curvas de isoquanta mais altas, com a mesma linha isocusto, do que no curto prazo, "
                      "uma vez que no curto prazo ela não pode variar a quantidade de capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No longo prazo, uma firma que tem dois insumos, capital (fixo) e trabalho (variável), "
                      "<u>pode</u> atingir curvas de isoquanta mais altas, com a mesma linha isocusto, do que no "
                      "curto prazo, uma vez que no curto prazo ela não pode variar a quantidade de capital."),
        "poucas": ("Com o capital travado, a firma só anda sobre a reta K = K̄ e em geral não chega à tangência; "
                   "no " + azb("longo prazo") + " escolhe K e L livremente e, com o mesmo gasto, alcança a "
                   "isoquanta mais alta — a tangente à isocusto."),
        "destrinchando": [
            azb("Isocusto") + ": C = wL + rK — todas as cestas de insumos que custam o mesmo. "
            + azb("Isoquanta") + ": todas as cestas que produzem o mesmo q. O ótimo de longo prazo é a "
            "tangência, onde " + vd("TMST = PMg<sub>L</sub>/PMg<sub>K</sub> = w/r") + " (cada real gasto em "
            "qualquer insumo rende o mesmo produto).",
            "No " + azb("curto prazo") + " o capital está fixo em K̄: a firma só escolhe L. Sobre a mesma "
            "isocusto, ela fica no ponto em que a reta K = K̄ corta a isocusto — que só coincide com a "
            "tangência se, por acaso, K̄ for exatamente o capital ótimo.",
            "Por isso o curto prazo é uma escolha <b>com uma restrição a mais</b>: no máximo empata com o longo "
            "prazo, nunca o supera. Dado o gasto, produz-se menos (isoquanta mais baixa); dado o produto, "
            "gasta-se mais (isocusto mais alta).",
            "É a mesma ideia que faz o " + azb("custo médio de longo prazo") + " ser a <b>envoltória</b> dos "
            "custos médios de curto prazo: cada CMe de curto prazo toca o de longo prazo só no nível de "
            "produção para o qual aquele K̄ é o ótimo.",
            vm("Regra-âncora: menos restrições → resultado igual ou melhor; o longo prazo nunca é pior que o "
               "curto."),
        ],
        "grafico_verso": "ECO-E2-L01724-1-V1",
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " O “pode” salva o item: se K̄ já fosse o "
                       "ótimo, não haveria ganho algum. Quem pensa no caso particular e marca ERRADO cai na "
                       "armadilha; o que a banca testa é a lógica de que a firma com mais liberdade de escolha "
                       "alcança pelo menos o mesmo resultado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…no longo prazo, a firma sempre atinge isoquantas mais altas, com a mesma isocusto, do que no "
            "curto prazo…”</i> → ERRADO (modulador absoluto: se K̄ já é ótimo, empata)",
            "<i>“Para um mesmo nível de produção, o custo total de curto prazo nunca é inferior ao de longo "
            "prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("No curto prazo o capital fixo impede a combinação ótima; no longo prazo todos os "
                             "fatores variam e, com a mesma isocusto, a firma alcança isoquanta mais alta (a "
                             "tangente), se o K fixo era subótimo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 513", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01724-1-V1, versão didática simplificada)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00013
    {
        "id": "ECO-E3-L00013-1", "fonte_ref": "E3-L00013", "destino": "06", "subtema": H2["lp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": COMANDO_TJPA,
        "rotulo_item": "Item",
        "assertiva": ("Uma empresa pode ter economias de escala ao mudar sua tecnologia ou combinação de insumos, "
                      "mesmo que seu processo produtivo demonstre rendimentos constantes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma empresa <u>pode</u> ter economias de escala ao mudar sua tecnologia ou combinação de "
                      "insumos, mesmo que seu processo produtivo demonstre <u>rendimentos constantes</u>."),
        "poucas": (azb("Rendimentos de escala") + " são conceito <b>técnico</b> (insumos × produto, na mesma "
                   "proporção); " + azb("economias de escala") + " são conceito de <b>custo</b> (CMe de longo "
                   "prazo caindo). Mudar a proporção dos insumos ou a tecnologia pode baixar o CMe mesmo com "
                   "rendimentos constantes."),
        "destrinchando": [
            "Rendimentos de escala respondem à pergunta: se <b>todos</b> os insumos forem multiplicados por λ, "
            "o produto se multiplica por mais, menos ou exatamente λ? É propriedade da função de produção, "
            "medida <b>com a proporção dos insumos fixa</b>.",
            "Economias de escala respondem a outra: quando a produção aumenta, o " + azb("custo médio de longo "
            "prazo") + " cai? Aqui a firma pode crescer <b>mudando</b> a combinação de insumos, trocando de "
            "tecnologia, especializando tarefas ou comprando insumos com desconto por volume (economias "
            "pecuniárias).",
            "Ligação entre os dois: com preços de insumos dados e proporções mantidas, rendimentos crescentes ⇒ "
            "economias de escala; constantes ⇒ CMe constante; decrescentes ⇒ deseconomias. Mas a recíproca não "
            "vale: há fontes de economia de escala que não passam pela função de produção original.",
            "Exemplo: uma gráfica cujo processo tem rendimentos constantes (dobrar máquinas e operadores dobra "
            "a tiragem) passa, ao crescer, a usar uma rotativa industrial — tecnologia que só compensa em "
            "grande escala — e o custo por exemplar cai.",
            vm("Regra-âncora: rendimento de escala é físico; economia de escala é de custo — e a segunda pode "
               "existir sem a primeira."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " O item aposta em quem trata os dois "
                       "conceitos como sinônimos (“rendimentos constantes ⇒ não há economia de escala”) e marca "
                       "ERRADO. A pista está em “ao mudar sua tecnologia ou combinação de insumos”: a mudança "
                       "tira a análise do terreno dos rendimentos de escala, que pressupõem proporções fixas. 🔥 "
                       "CEBRASPE gosta de cobrar a distinção físico × custo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Economias de escala e rendimentos crescentes de escala são expressões sinônimas.”</i> → ERRADO "
            "(troca de conceito: custo × técnica)",
            "<i>“Com preços de insumos constantes, rendimentos crescentes de escala implicam custo médio de "
            "longo prazo decrescente.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode", "mesmo que"],
        "dificuldade": 2,
        "comentario_fonte": ("Rendimentos de escala são relação técnica insumo-produto; economias de escala, "
                             "queda do custo médio de longo prazo, que pode vir de nova tecnologia, nova "
                             "combinação de insumos, especialização e economias pecuniárias."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00014
    {
        "id": "ECO-E3-L00014-1", "fonte_ref": "E3-L00014", "destino": "06", "subtema": H2["lp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": COMANDO_TJPA,
        "rotulo_item": "Item",
        "assertiva": ("A curva de custo médio no longo prazo apresenta formato em U, em função da rigidez na "
                      "alocação dos fatores de produção e de rendimentos decrescentes de escala."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de custo médio no longo prazo apresenta formato em U, em função ")
                   + vm("da rigidez na alocação dos fatores de produção e de rendimentos decrescentes de escala")
                   + az("."),
        "poucas": ("No longo prazo " + azb("não há fator fixo") + ": o U do CMe de longo prazo vem de "
                   + azb("economias de escala") + " (trecho que desce) seguidas de " + azb("deseconomias de "
                   "escala") + " (trecho que sobe). Rigidez de fatores explica o U do <b>curto</b> prazo."),
        "destrinchando": [
            "<b>Curto prazo</b>: há ao menos um fator fixo. O CMe cai no início pela diluição do custo fixo e "
            "pelo produto marginal crescente; depois sobe pela " + azb("lei dos rendimentos marginais "
            "decrescentes") + " — mais trabalho sobre a mesma planta. A “rigidez” é exatamente essa.",
            "<b>Longo prazo</b>: todos os fatores variam; a firma escolhe a planta ótima para cada nível de "
            "produção. O CMe de longo prazo é a " + azb("envoltória") + " dos CMe de curto prazo.",
            "Por que ele também tende ao U: no início, " + azb("economias de escala") + " — especialização, "
            "indivisibilidades (equipamento que só compensa em grande escala), descontos na compra de insumos; "
            "a partir de certo tamanho, " + azb("deseconomias de escala") + " — custos de coordenação, "
            "burocracia, perda de controle gerencial. O fundo do U é a " + vd("escala mínima eficiente") + ".",
            "Rendimentos decrescentes de escala podem, sim, contribuir para o trecho ascendente; o que torna o "
            "item falso é atribuir o formato à <b>rigidez</b> dos fatores, que por definição não existe no "
            "longo prazo — e omitir a fase de economias, sem a qual não há U, só uma curva crescente.",
            vm("Regra-âncora: U de curto prazo → rendimentos marginais (fator fixo); U de longo prazo → "
               "economias e deseconomias de escala."),
        ],
        "dissecando": (cz("[troca de conceito · anacronismo]") + " O item empresta a explicação do curto prazo "
                       "(rigidez de fatores) e a cola no longo prazo — um “anacronismo” de horizonte temporal. "
                       "A expressão “rendimentos decrescentes de escala” soa técnica e distrai; a palavra que "
                       "entrega o erro é <b>rigidez</b>. 🔥 Banca adora trocar as causas do U de curto e de "
                       "longo prazo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de custo médio no curto prazo apresenta formato em U em função da lei dos rendimentos "
            "marginais decrescentes.”</i> → CERTO",
            "<i>“O trecho descendente do custo médio de longo prazo decorre da diluição dos custos "
            "fixos.”</i> → ERRADO (no longo prazo não há custo fixo; são economias de escala)",
        ])],
        "reescrita": ("A curva de custo médio no longo prazo apresenta formato em U, em função " + hl("de "
                      "economias de escala em níveis baixos de produção e de deseconomias de escala em níveis "
                      "elevados") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "ANACRONISMO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("No longo prazo todos os fatores são variáveis; o U do CMeLP decorre de economias e "
                             "deseconomias de escala, e a rigidez de fatores é típica do curto prazo. Um dos "
                             "comentários empilhados marcava CERTO, alegando gabarito oficial nesse sentido."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: gabarito a conferir — a indicação principal da fonte e quatro dos seis comentários dão "
                    "ERRADO; dois comentários dão CERTO, um deles alegando que o gabarito oficial considerou o "
                    "item correto — não confirmado por busca; mantido ERRADO, que é o defensável pelo conteúdo"],
    },
    # ------------------------------------------------------------------ E3-L00341
    {
        "id": "ECO-E3-L00341-1", "fonte_ref": "E3-L00341", "destino": "06", "subtema": H2["iso"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": COMANDO_NIDI_DEZ24,
        "rotulo_item": "Item",
        "assertiva": ("A linha de isocusto é geralmente reta porque sua inclinação representa a razão entre os "
                      "preços dos insumos de produção que tendem a ser fixos no curto prazo. Assim, a linha de "
                      "isocusto só poderia apresentar um formato não linear no caso em que os preços dos insumos "
                      "variassem com as quantidades adquiridas, o que pode ocorrer em situações de ampliação da "
                      "escala produtiva e aquisição de insumos em maiores quantidades."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A linha de isocusto é <u>geralmente</u> reta porque sua inclinação representa a razão "
                      "entre os preços dos insumos de produção que tendem a ser fixos no curto prazo. Assim, a "
                      "linha de isocusto só poderia apresentar um formato não linear no caso em que os preços "
                      "dos insumos <u>variassem com as quantidades adquiridas</u>, o que pode ocorrer em "
                      "situações de ampliação da escala produtiva e aquisição de insumos em maiores "
                      "quantidades."),
        "poucas": ("C = wL + rK é uma " + azb("reta") + " de inclinação " + vd("−w/r") + " porque w e r são "
                   "dados para a firma. Se o preço do insumo mudar com a quantidade comprada (desconto por "
                   "volume, poder de monopsônio), a inclinação muda ao longo da linha e ela se curva."),
        "destrinchando": [
            "Isolando K na equação do custo: " + vd("K = C/r − (w/r)·L") + ". Intercepto C/r, inclinação −w/r. "
            "A linha é reta porque a firma é " + azb("tomadora de preços") + " nos mercados de insumos: cada "
            "hora de trabalho custa w, compre ela 10 ou 10 mil horas.",
            "Quando a reta deixa de ser reta: (i) " + azb("descontos por volume") + " — o preço unitário cai "
            "com a quantidade comprada (isocusto convexa em relação à origem no trecho com desconto); "
            "(ii) " + azb("monopsônio") + " — a firma é grande no mercado do insumo e, para contratar mais, "
            "precisa pagar mais (o salário sobe com L); (iii) tarifas em blocos e custos de ajuste.",
            "Mudanças que <b>não</b> curvam a isocusto: aumento do orçamento C (desloca paralelamente) e "
            "variação de w ou r constante em toda a faixa (gira a reta, mas ela continua reta).",
            "Ressalva técnica: isocusto e isoquanta são ferramentas típicas do <b>longo prazo</b>, quando os "
            "dois insumos variam; a menção ao curto prazo é heterodoxa, mas não falseia o núcleo do item, "
            "que é a relação entre preços constantes e linearidade.",
            vm("Regra-âncora: preço de insumo constante → isocusto reta; preço que varia com a quantidade → "
               "isocusto curva."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Item longo, com dois moduladores "
                       "protetores (“geralmente”, “pode ocorrer”) e um “só” que parece restrição indevida mas "
                       "é verdadeiro: a única forma de curvar a isocusto é preço de insumo dependente da "
                       "quantidade. A menção a “curto prazo” é o ruído plantado para induzir ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento do salário, mantidos o custo total e o preço do capital, desloca a isocusto "
            "paralelamente para dentro.”</i> → ERRADO (a reta gira em torno do intercepto do eixo K)",
            "<i>“Uma firma monopsonista no mercado de trabalho pode enfrentar isocusto não linear.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["geralmente", "só", "pode"],
        "dificuldade": 2,
        "comentario_fonte": ("Isocusto C = wL + rK, inclinação −w/r; reta com w e r constantes (firma tomadora "
                             "de preços); curva com descontos por volume, monopsônio ou preço efetivo que "
                             "depende da quantidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 477", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 478", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (isoquanta e TMST; não passa no teste do quadro-negro para este item)"},
                          {"ref": "IMAGEM 479", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (idem)"},
                          {"ref": "IMAGEM 480", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00342
    {
        "id": "ECO-E3-L00342-1", "fonte_ref": "E3-L00342", "destino": "06", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": COMANDO_NIDI_DEZ24,
        "rotulo_item": "Item",
        "assertiva": ("Um custo marginal decrescente provoca uma redução no custo médio total de produção. Isso "
                      "ocorre porque as novas unidades produzidas geram acréscimos no custo total menores do que "
                      "as unidades anteriormente produzidas, reduzindo o custo médio total."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um custo marginal <u>decrescente</u> provoca uma redução no custo médio total de produção. "
                      "Isso ocorre porque as novas unidades produzidas geram acréscimos no custo total menores do "
                      "que as unidades anteriormente produzidas, reduzindo o custo médio total."),
        "poucas": ("Na curva de custos típica, o trecho em que o " + azb("CMg cai") + " fica todo abaixo do "
                   + azb("CMe") + ": cada unidade nova custa menos que a média e a puxa para baixo."),
        "destrinchando": [
            "Relação marginal × média (vale para qualquer média, inclusive notas de prova): " + vd("CMg < CMe "
            "→ CMe cai") + "; " + vd("CMg > CMe → CMe sobe") + "; CMg = CMe no <b>mínimo</b> do CMe. Por isso "
            "o CMg corta o CMe (e o CVMe) exatamente no ponto mais baixo deles.",
            "Na curva típica em U, o CMg atinge o mínimo <b>antes</b> do CMe. Logo, enquanto o CMg desce, ele "
            "está necessariamente abaixo do CMe — e o CMe está caindo. É o que o item descreve.",
            "O inverso não vale: depois do mínimo, o CMg já <b>sobe</b>, mas continua abaixo do CMe por um "
            "trecho; ali o CMe ainda cai. O que decide a direção do CMe é a <b>posição</b> do CMg (acima ou "
            "abaixo), não a sua inclinação.",
            "Origem econômica do CMg decrescente: produto marginal do trabalho crescente nas primeiras "
            "contratações (especialização, melhor uso da planta). Como " + vd("CMg = w/PMg<sub>L</sub>")
            + ", PMg subindo ⇒ CMg caindo.",
            vm("Regra-âncora: quem manda na média é a posição do marginal, não a direção em que ele anda."),
        ],
        "grafico_verso": "ECO-E3-L00342-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item é correto dentro da curva-padrão, e a "
                       "justificativa reproduz o mecanismo da média. A armadilha está no candidato que lembra "
                       "a ressalva “o que importa é CMg &lt; CMe” e julga o item incompleto. 🔥 A versão "
                       "ERRADA clássica é a inversa: “CMg crescente implica CMe crescente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um custo marginal crescente provoca necessariamente um aumento do custo médio total.”</i> → "
            "ERRADO (CMe só sobe quando CMg > CMe)",
            "<i>“A curva de custo marginal intercepta a de custo médio total no ponto mínimo desta.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Se o marginal está abaixo da média, puxa a média para baixo; CMg decrescente "
                             "ocorre abaixo do CMe na curva típica; CMg crescente ainda reduz o CMe enquanto "
                             "estiver abaixo dele."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 481", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 482", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00342-1-V1)"},
                          {"ref": "IMAGEM 483", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "fundida em ECO-E3-L00342-1-V1"},
                          {"ref": "IMAGEM 484", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0009
    {
        "id": "ECO-E1-0009-1", "fonte_ref": "E1-0009", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca das estruturas de mercado, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O conceito de mercados não competitivos sugere que o único atributo para a determinação da "
                      "quantidade demandada e quantidade ofertada de um bem é o preço de mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O conceito de mercados não competitivos sugere que ") + vm("o único atributo")
                   + az(" para a determinação da quantidade demandada e quantidade ofertada de um bem ")
                   + vm("é o preço de mercado") + az("."),
        "poucas": ("Em mercados " + azb("não competitivos") + " há " + azb("poder de mercado") + ": o preço "
                   "deixa de ser dado e passa a ser escolhido, e pesam também diferenciação, barreiras à "
                   "entrada, número de rivais e estratégia."),
        "destrinchando": [
            "Em " + azb("concorrência perfeita") + ", cada agente é " + azb("tomador de preços") + ": o preço "
            "de mercado é um dado, e a firma decide só quanto produzir (P = CMg). É o mundo em que “o preço "
            "resolve tudo”.",
            "Em mercados " + azb("não competitivos") + " (monopólio, oligopólio, concorrência monopolística, "
            "monopsônio), compradores ou vendedores reconhecem que suas decisões mexem no preço — são "
            + azb("fixadores de preço") + ". O preço vira variável de escolha, não sinal externo.",
            "Por isso entram outros atributos: " + vd("diferenciação do produto") + " (marca, qualidade), "
            + vd("barreiras à entrada") + ", " + vd("número e porte dos rivais") + ", publicidade, reação "
            "esperada dos concorrentes (oligopólio estratégico), contratos de exclusividade.",
            "Consequência de bem-estar: com poder de mercado, P > CMg, a quantidade fica abaixo da eficiente e "
            "surge peso morto — razão de existir da defesa da concorrência (no Brasil, o " + rx("CADE") + ").",
            vm("Regra-âncora: preço como único sinal e dado externo é marca da concorrência perfeita, não dos "
               "mercados não competitivos."),
        ],
        "dissecando": (cz("[troca de conceito · restrição indevida]") + " O item atribui aos mercados não "
                       "competitivos a hipótese típica do modelo competitivo e a blinda com “o único atributo”. "
                       "Restrição forte (“único”, “apenas”) em tema de estruturas de mercado costuma ser o "
                       "ponto do erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em concorrência perfeita, a firma toma o preço de mercado como dado e escolhe apenas a "
            "quantidade a produzir.”</i> → CERTO",
            "<i>“Em mercados não competitivos, as firmas são tomadoras de preço.”</i> → ERRADO (inversão: "
            "são fixadoras)",
        ])],
        "reescrita": ("O conceito de mercados não competitivos sugere que " + hl("o preço de mercado não é o "
                      "único atributo") + " para a determinação da quantidade demandada e quantidade ofertada "
                      "de um bem" + hl(", que depende também de poder de mercado, diferenciação e barreiras à "
                      "entrada") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "RESTRICAO"], "moduladores": ["único"], "dificuldade": 1,
        "comentario_fonte": ("Em mercados não competitivos há poder de mercado; os agentes são fixadores de preço "
                             "e outros atributos (diferenciação, barreiras, número de ofertantes) influenciam o "
                             "resultado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: a fonte formulava o item como pergunta (“É correto afirmar que …?”); "
                    "convertida em afirmação, com “quantidade oferta” corrigido para “quantidade ofertada”"],
    },
    # ------------------------------------------------------------------ E1-0231
    {
        "id": "ECO-E1-0231-1", "fonte_ref": "E1-0231", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": True,
        "comando": "Acerca das estruturas de mercado e das barreiras à entrada, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Entre as condições que contribuem para impedir a entrada de produtores concorrentes em um "
                      "mercado monopolista, inclui-se a capacidade do produtor de diferenciar seu produto, "
                      "criando e mantendo, por exemplo, uma imagem de tradição e estabilidade, ou mesmo, "
                      "inversamente, de renovação e inovação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Entre as condições que contribuem para impedir a entrada de produtores concorrentes em um "
                      "mercado monopolista, inclui-se a capacidade do produtor de <u>diferenciar seu "
                      "produto</u>, criando e mantendo, por exemplo, uma imagem de tradição e estabilidade, ou "
                      "mesmo, inversamente, de renovação e inovação."),
        "poucas": ("A " + azb("diferenciação de produto") + " é uma " + azb("barreira à entrada") + " "
                   "clássica: o entrante teria de gastar muito para conquistar uma reputação (de tradição ou de "
                   "inovação) que o incumbente já tem."),
        "destrinchando": [
            "Classificação de " + oc("Joe Bain") + " (<i>Barriers to New Competition</i>, 1956), base da "
            "organização industrial: as barreiras à entrada vêm de (1) " + vd("economias de escala") + "; (2) "
            + vd("vantagens absolutas de custo") + " (acesso exclusivo a insumos, tecnologia, patentes); (3) "
            + vd("diferenciação de produto") + "; (4) " + vd("exigências elevadas de capital inicial") + ".",
            "Como a diferenciação barra a entrada: lealdade à marca, gastos acumulados com publicidade, redes "
            "de distribuição e contratos de exclusividade fazem o consumidor não ver o produto do entrante como "
            "substituto perfeito. O novato precisa vender abaixo do preço do incumbente ou gastar mais em "
            "marketing por unidade — custo que o incumbente já amortizou.",
            "“Tradição e estabilidade” e “renovação e inovação” são duas estratégias opostas de construir a "
            "mesma coisa: uma imagem de marca que o rival não replica de imediato. O “inversamente” do item não "
            "é contradição.",
            "Contraste: em " + azb("concorrência perfeita") + " o produto é homogêneo — não há diferenciação "
            "possível, e a entrada é livre. Em " + azb("concorrência monopolística") + " há diferenciação, mas "
            "a entrada continua livre: a diferenciação dá algum poder de mercado, sem bloquear rivais.",
            "A banca também cobra a versão com “na presença de poder de mercado” no lugar de “mercado "
            "monopolista”, também CERTO.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Redação de manual; o “inversamente” e a menção a "
                       "inovação parecem contraditórios com “impedir a entrada” e induzem o ERRADO. Quem "
                       "conhece a lista de Bain resolve em segundos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência monopolística, a diferenciação de produto impede a entrada de novas "
            "firmas.”</i> → ERRADO (troca de estrutura: lá a entrada é livre)",
            "<i>“Economias de escala e exigências elevadas de capital são barreiras à entrada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["por exemplo", "ou mesmo"], "dificuldade": 1,
        "comentario_fonte": ("Diferenciação de produto como barreira à entrada (controle de tecnologia, "
                             "propaganda, durabilidade e complexidade, contratos de exclusividade); outras "
                             "barreiras: vantagens absolutas de custo, economias de escala, investimentos "
                             "iniciais elevados. Inclui digressões sobre concorrência monopolística e "
                             "vantagens e desvantagens do monopólio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (80).png", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada no caderno E1)"}],
        "alertas": ["banca_provavel: possivelmente CACD/2014 (CEBRASPE), não confirmado pela fonte",
                    "quase_duplicata: ECO-E1-0305-1 (mesma assertiva, prova diferente) — mantidos os dois"],
    },
    # ------------------------------------------------------------------ E1-0305
    {
        "id": "ECO-E1-0305-1", "fonte_ref": "E1-0305", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Acerca das estruturas de mercado e das barreiras à entrada, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na presença de poder de mercado, entre as condições que contribuem para impedir a entrada "
                      "de produtores concorrentes, inclui-se a capacidade do produtor de diferenciar seu "
                      "produto, criando e mantendo, por exemplo, uma imagem de tradição e estabilidade, ou "
                      "mesmo, inversamente, de renovação e inovação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Na presença de poder de mercado</u>, entre as condições que contribuem para impedir a "
                      "entrada de produtores concorrentes, inclui-se a capacidade do produtor de diferenciar seu "
                      "produto, criando e mantendo, por exemplo, uma imagem de tradição e estabilidade, ou "
                      "mesmo, inversamente, de renovação e inovação."),
        "poucas": ("Diferenciar o produto — por tradição <b>ou</b> por inovação — cria lealdade à marca que o "
                   "entrante não replica sem custo: é " + azb("barreira à entrada") + " e sustenta o "
                   + azb("poder de mercado") + "."),
        "destrinchando": [
            azb("Poder de mercado") + " = capacidade de fixar preço acima do custo marginal sem perder toda a "
            "clientela. Para durar, precisa de algo que impeça rivais de entrar e disputar o lucro: as "
            + azb("barreiras à entrada") + ".",
            "Fontes clássicas (" + oc("Joe Bain") + "): economias de escala, vantagens absolutas de custo, "
            "exigência elevada de capital e " + vd("diferenciação de produto") + ". A esta lista somam-se as "
            "barreiras legais (patentes, concessões, licenças).",
            "A diferenciação funciona porque torna o produto do incumbente um substituto <b>imperfeito</b> do "
            "do entrante: a demanda do incumbente fica menos elástica (mais poder de preço), e o entrante "
            "precisa investir em publicidade e reputação antes de vender.",
            "As duas estratégias citadas são opostas apenas na aparência: tradição e estabilidade (marcas "
            "centenárias de cerveja, bancos) e renovação e inovação (eletrônicos, moda) servem ao mesmo fim — "
            "criar uma identidade de marca difícil de copiar.",
            "A banca também cobra a versão com “mercado monopolista” no lugar de “na presença de poder de "
            "mercado” (prova de 2014), também CERTO. A versão do simulado é mais ampla e cobre oligopólio e "
            "concorrência monopolística.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Releitura de item de prova antiga, com o "
                       "escopo ampliado para “poder de mercado”. A troca não muda o gabarito: diferenciação é "
                       "barreira onde quer que haja poder de mercado a proteger. O “inversamente” é o ruído que "
                       "tenta parecer contradição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência perfeita, a diferenciação de produto é uma das barreiras que protegem as "
            "firmas estabelecidas.”</i> → ERRADO (produto homogêneo e entrada livre)",
            "<i>“Patentes e concessões públicas constituem barreiras legais à entrada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["por exemplo", "ou mesmo"],
        "dificuldade": 1,
        "comentario_fonte": "Verso apenas repete a assertiva com o gabarito CERTO.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0231-1 (mesma assertiva, prova diferente) — mantidos os dois"],
    },
    # ------------------------------------------------------------------ E1-0268
    {
        "id": "ECO-E1-0268-1", "fonte_ref": "E1-0268", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca da maximização de lucro nas diferentes estruturas de mercado, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em qualquer estrutura de mercado a firma maximiza seu lucro quando a receita marginal é "
                      "igual ao custo marginal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em <u>qualquer</u> estrutura de mercado a firma maximiza seu lucro quando a receita "
                      "marginal é igual ao custo marginal."),
        "poucas": (vd("RMg = CMg") + " é a condição de primeira ordem de <b>qualquer</b> firma maximizadora de "
                   "lucro; o que muda entre as estruturas é a relação entre RMg e preço."),
        "destrinchando": [
            "Lucro π(q) = RT(q) − CT(q). No máximo, a derivada se anula: dRT/dq − dCT/dq = 0 ⇒ "
            + vd("RMg = CMg") + ". A intuição: enquanto a última unidade traz mais receita do que custo (RMg > "
            "CMg), vale produzir mais; quando custa mais do que rende, vale produzir menos.",
            "O que varia é a RMg. Em " + azb("concorrência perfeita") + ", a firma é tomadora de preço: "
            + vd("RMg = P") + " e a regra vira P = CMg. Em " + azb("monopólio") + " e demais estruturas com "
            "demanda negativamente inclinada, vender mais exige baixar o preço de todas as unidades: "
            + vd("RMg < P") + ", e no ótimo P > CMg (" + azb("markup") + ").",
            "Ressalvas que não derrubam a regra: (i) é condição necessária — exige também o CMg cortando a RMg "
            "de baixo para cima (segunda ordem); (ii) no curto prazo, a firma só produz se P ≥ CVMe, senão "
            "fecha; (iii) em oligopólio, a RMg depende da reação esperada dos rivais (Cournot, Stackelberg), "
            "mas cada firma ainda iguala a <b>sua</b> RMg ao seu CMg.",
            vm("Regra-âncora: RMg = CMg vale em toda estrutura; P = CMg só em concorrência perfeita."),
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " O “qualquer” tem cara de modulador absoluto "
                       "e induz ERRADO, mas aqui a generalização é verdadeira. A versão errada típica troca RMg "
                       "por preço: “em qualquer estrutura, a firma maximiza o lucro quando P = CMg”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em qualquer estrutura de mercado a firma maximiza seu lucro quando o preço é igual ao custo "
            "marginal.”</i> → ERRADO (P = CMg só em concorrência perfeita)",
            "<i>“No monopólio, o preço que maximiza o lucro supera o custo marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["qualquer"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito (CERTO) e uma imagem não preservada.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "Untitled (57).jpeg", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada no caderno E1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00044
    {
        "id": "ECO-E2-L00044-1", "fonte_ref": "E2-L00044", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Sobre as falhas de mercado e as intervenções governamentais para corrigir essas falhas, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Monopólios e oligopólios são considerados falhas de mercado do lado da oferta, enquanto "
                      "monopsônio e oligopsônio são falhas do lado da demanda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Monopólios e oligopólios são considerados falhas de mercado do lado da <u>oferta</u>, "
                      "enquanto monopsônio e oligopsônio são falhas do lado da <u>demanda</u>."),
        "poucas": ("Todas são " + azb("poder de mercado") + ": nos “-pólios”, poucos <b>vendedores</b>; nos "
                   "“-psônios”, poucos <b>compradores</b>. Em ambos, a quantidade transacionada fica abaixo da "
                   "eficiente."),
        "destrinchando": [
            "Mercado competitivo pressupõe que ninguém influencia o preço. Quando um lado é concentrado, essa "
            "hipótese cai e o preço deixa de igualar custo marginal e benefício marginal — " + azb("falha de "
            "mercado") + " por " + azb("concorrência imperfeita") + ", ao lado de externalidades, bens "
            "públicos e assimetria de informação.",
            azb("Monopólio") + " (um vendedor) e " + azb("oligopólio") + " (poucos vendedores): restringem a "
            "oferta para elevar o preço; P > CMg e peso morto.",
            azb("Monopsônio") + " (um comprador) e " + azb("oligopsônio") + " (poucos compradores): restringem "
            "as compras para baixar o preço pago; o preço fica abaixo do valor marginal do que se compra. "
            "Exemplo de livro: empregador único numa cidade pequena paga salário abaixo do produto marginal do "
            "trabalho e contrata menos que o eficiente.",
            "Exemplo brasileiro recorrente: cadeias agroindustriais em que poucos compradores (laticínios, "
            "frigoríficos, tradings) adquirem a produção de muitos produtores pequenos — tema de atenção do "
            + rx("CADE") + ".",
            "Os dois lados podem coexistir: " + azb("monopólio bilateral") + " (um vendedor diante de um "
            "comprador), em que o preço se define por barganha.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item de classificação: a banca testa se o candidato "
                       "sabe que “-psônio” é o lado comprador. A versão errada mais provável inverteria os lados "
                       "ou negaria ao monopsônio o status de falha de mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O monopsônio é uma falha de mercado do lado da oferta, caracterizada por um único "
            "vendedor.”</i> → ERRADO (inversão: único comprador, lado da demanda)",
            "<i>“No monopsônio, o preço pago pelo insumo é inferior ao seu valor marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Monopólio e oligopólio reduzem a concorrência do lado da oferta; monopsônio e "
                             "oligopsônio, do lado da demanda (exemplo: grandes compradores no setor leiteiro "
                             "retardando compras para pressionar preços)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00442
    {
        "id": "ECO-E2-L00442-1", "fonte_ref": "E2-L00442", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "A respeito das estruturas de mercado, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Barreiras à entrada, sejam elas legais, naturais ou estratégicas, são características "
                      "essenciais para a sustentação de poder de mercado em monopólios e oligopólios no longo "
                      "prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Barreiras à entrada, sejam elas legais, naturais ou estratégicas, são características "
                      "<u>essenciais</u> para a sustentação de poder de mercado em monopólios e oligopólios "
                      "<u>no longo prazo</u>."),
        "poucas": ("Sem " + azb("barreiras à entrada") + ", o lucro extraordinário atrai entrantes até "
                   "desaparecer. São elas que permitem a monopólios e oligopólios manter P > CMe <b>no longo "
                   "prazo</b>."),
        "destrinchando": [
            "Mecanismo: lucro econômico positivo é sinal de entrada. Se nada impede a entrada, novas firmas "
            "expandem a oferta, o preço cai e o lucro tende a zero — é o que acontece em concorrência perfeita "
            "e em " + azb("concorrência monopolística") + " no longo prazo.",
            "Tipologia do item: " + vd("legais") + " (patentes, concessões, licenças, regulação); "
            + vd("naturais") + " ou estruturais (economias de escala que tornam o " + azb("monopólio "
            "natural") + " a solução de menor custo, controle de insumo essencial, efeitos de rede); "
            + vd("estratégicas") + " (excesso de capacidade como ameaça crível, preço-limite, proliferação de "
            "marcas, contratos de exclusividade).",
            "No curto prazo, mesmo sem barreiras, uma firma pode ter lucro extraordinário — a entrada leva "
            "tempo. Por isso o item fala, com precisão, em sustentação <b>no longo prazo</b>.",
            "Contraponto teórico: a " + azb("teoria dos mercados contestáveis") + " (" + oc("Baumol") + ", "
            + oc("Panzar") + " e " + oc("Willig") + ", 1982) mostra que, sem custos irrecuperáveis (entrada e "
            "saída livres), até um monopólio é disciplinado pela mera ameaça de entrada — o que reforça que é "
            "a barreira, não o número de firmas, que sustenta o poder de mercado.",
            vm("Regra-âncora: poder de mercado duradouro = barreira à entrada; sem barreira, o lucro atrai "
               "rivais."),
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " O “essenciais” parece exagero, mas é a tese "
                       "padrão dos manuais. O item foi construído para quem confunde monopólio com "
                       "concorrência monopolística, onde há poder de mercado sem barreira — e, por isso, sem "
                       "lucro de longo prazo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência monopolística, as barreiras à entrada permitem lucro econômico positivo no "
            "longo prazo.”</i> → ERRADO (entrada livre: lucro zero no longo prazo)",
            "<i>“Em um mercado perfeitamente contestável, um monopolista não consegue sustentar lucro "
            "extraordinário.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["essenciais", "no longo prazo"],
        "dificuldade": 1,
        "comentario_fonte": ("Barreiras legais (patentes), naturais (economias de escala) e estratégicas "
                             "(diferenciação) impedem a entrada e preservam os lucros extraordinários no longo "
                             "prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00851
    {
        "id": "ECO-E2-L00851-1", "fonte_ref": "E2-L00851", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação às estruturas de mercado, julgue (C ou E) o item que se segue.",
        "rotulo_item": "Item",
        "assertiva": ("Assim como no mercado monopolista, as firmas que atuam no mercado de concorrência perfeita "
                      "maximizam o lucro no ponto de igualdade entre a receita marginal e o custo marginal; "
                      "porém, no equilíbrio de longo prazo, as firmas em concorrência perfeita sempre vão auferir "
                      "um lucro econômico igual a zero, enquanto o lucro econômico da firma monopolista poderá "
                      "ser positivo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Assim como no mercado monopolista, as firmas que atuam no mercado de concorrência perfeita "
                      "maximizam o lucro no ponto de igualdade entre a receita marginal e o custo marginal; "
                      "porém, no equilíbrio de longo prazo, as firmas em concorrência perfeita <u>sempre</u> vão "
                      "auferir um lucro econômico igual a zero, enquanto o lucro econômico da firma monopolista "
                      "<u>poderá</u> ser positivo."),
        "poucas": ("A regra " + vd("RMg = CMg") + " é comum às duas estruturas; a diferença de longo prazo vem "
                   "das " + azb("barreiras à entrada") + ": livre entrada zera o lucro competitivo; barreiras "
                   "permitem ao monopolista mantê-lo."),
        "destrinchando": [
            "Quadro comparativo — " + azb("concorrência perfeita") + ": demanda da firma horizontal (RMg = P), "
            "P = CMg, sem barreiras, lucro de longo prazo " + vd("zero") + ". " + azb("Concorrência "
            "monopolística") + ": demanda negativamente inclinada (RMg < P), P > CMg, sem barreiras, lucro de "
            "longo prazo " + vd("zero") + ". " + azb("Monopólio") + ": demanda negativamente inclinada, P > CMg, "
            "com barreiras, lucro de longo prazo " + vd("pode ser positivo") + ". Nas três, RMg = CMg.",
            "Concorrência perfeita: lucro positivo atrai entrantes; a oferta da indústria cresce e o preço cai "
            "até " + vd("P = CMe mínimo") + ". Prejuízo provoca saída até o mesmo ponto. Por isso o "
            "“sempre” do item é correto <b>no equilíbrio de longo prazo</b> do modelo.",
            "Monopólio: as barreiras impedem a entrada, e o lucro extraordinário pode persistir. “Poderá” é a "
            "palavra certa: se a demanda for fraca, o monopolista pode ter lucro nulo ou até sair do mercado.",
            "Lucro econômico zero ≠ lucro contábil zero: a firma competitiva de longo prazo cobre todos os "
            "custos, inclusive o de oportunidade do capital, e obtém o " + azb("lucro normal") + ".",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item de duas metades, ambas verdadeiras. "
                       "O “sempre” parece modulador absoluto, mas está ancorado no equilíbrio de longo prazo do "
                       "modelo; o “poderá” do monopólio é o modulador relativo que salva a segunda parte. A "
                       "versão ERRADA típica diria que o monopolista “sempre” tem lucro positivo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…enquanto o lucro econômico da firma monopolista será necessariamente positivo no longo "
            "prazo.”</i> → ERRADO (modulador absoluto: pode ser nulo)",
            "<i>“Na concorrência monopolística, as firmas obtêm lucro econômico positivo no longo prazo.”</i> → "
            "ERRADO (entrada livre zera o lucro)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["sempre", "poderá"], "dificuldade": 1,
        "comentario_fonte": ("Verso só com o gabarito e uma tabela comparativa de concorrência perfeita, "
                             "concorrência monopolística e monopólio (regra de maximização, demanda, RMg, "
                             "preço, bem-estar, barreiras, lucro de longo prazo)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 130", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (quadro comparativo no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01200
    {
        "id": "ECO-E2-L01200-1", "fonte_ref": "E2-L01200", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Quanto às estruturas de mercado, julgue (C ou E) o item subsequente.",
        "rotulo_item": "Item",
        "assertiva": ("Na presença de economias externas de escala, não é possível que a estrutura de mercado "
                      "seja composta por várias empresas pequenas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na presença de economias externas de escala, ") + vm("não é possível")
                   + az(" que a estrutura de mercado seja composta por várias empresas pequenas."),
        "poucas": ("Nas " + azb("economias externas") + ", o custo cai com o tamanho da <b>indústria</b>, não "
                   "da firma: são justamente compatíveis com muitas firmas pequenas e concorrência perfeita."),
        "destrinchando": [
            "Distinção de " + oc("Krugman e Obstfeld") + " (<i>Economia Internacional</i>), herdeira de "
            + oc("Alfred Marshall") + ": " + azb("economias internas") + " — o custo médio depende do tamanho "
            "da <b>firma</b>; favorecem firmas grandes e levam a " + azb("concorrência imperfeita") + ". "
            + azb("Economias externas") + " — o custo médio depende do tamanho da <b>indústria</b> no local; "
            "cada firma pode continuar pequena.",
            "Fontes das economias externas (os “distritos industriais” de Marshall): fornecedores "
            "especializados, mercado de trabalho comum (pooling de mão de obra qualificada) e transbordamentos "
            "de conhecimento. Exemplos: Vale do Silício, polo calçadista do " + rx("Vale dos Sinos (RS)")
            + ", polo moveleiro de Bento Gonçalves.",
            "Como a vantagem é da indústria, nenhuma firma a captura sozinha nem ganha poder de mercado por "
            "isso: o modelo usado é o de " + vd("concorrência perfeita") + ", com uma " + azb("curva de oferta "
            "decrescente") + " da indústria (quanto mais ela produz, menor o custo e o preço).",
            "Implicação para o comércio: economias externas explicam a concentração geográfica da produção e "
            "a força da vantagem histórica — quem começou primeiro tende a manter a liderança.",
            vm("Regra-âncora: interna → firma grande, concorrência imperfeita; externa → indústria grande, "
               "muitas firmas pequenas."),
        ],
        "dissecando": (cz("[troca de conceito · restrição indevida]") + " O item atribui às economias "
                       "<b>externas</b> a consequência das <b>internas</b> e a blinda com “não é possível”. "
                       "🔥 A dupla interna × externa é recorrente nas provas de comércio internacional do CACD."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na presença de economias internas de escala, tende a prevalecer a concorrência "
            "imperfeita.”</i> → CERTO",
            "<i>“Com economias externas, a curva de oferta de longo prazo da indústria é positivamente "
            "inclinada.”</i> → ERRADO (é decrescente)",
        ])],
        "reescrita": ("Na presença de economias externas de escala, " + hl("é possível — e típico —") + " que a "
                      "estrutura de mercado seja composta por várias empresas pequenas."),
        "tipo_erro": ["TROCA_CONCEITO", "RESTRICAO"], "moduladores": ["não é possível"], "dificuldade": 2,
        "comentario_fonte": ("Economias externas: custo por unidade depende do tamanho da indústria; indústria "
                             "de muitas firmas pequenas, concorrência perfeita. Internas: depende do tamanho da "
                             "firma; concorrência imperfeita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00102
    {
        "id": "ECO-E3-L00102-1", "fonte_ref": "E3-L00102", "destino": "07", "subtema": H2["comp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": ("A partir dos conceitos e das teorias usuais de concorrência perfeita, monopólio e oligopólio, "
                    "julgue (C ou E) o item que se segue."),
        "rotulo_item": "Item",
        "assertiva": ("Em mercados de concorrência imperfeita, a elasticidade da curva de demanda das empresas é "
                      "menor do que a elasticidade da demanda do mercado. Isso ocorre porque é mais fácil para os "
                      "consumidores optarem por consumir um produto altamente substituível de outra empresa do "
                      "que optarem por consumir um outro produto totalmente diferente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em mercados de concorrência imperfeita, a elasticidade da curva de demanda das empresas é ")
                   + vm("menor") + az(" do que a elasticidade da demanda do mercado. Isso ocorre porque é mais "
                   "fácil para os consumidores optarem por consumir um produto altamente substituível de outra "
                   "empresa do que optarem por consumir um outro produto totalmente diferente."),
        "poucas": ("A justificativa está certa e prova o contrário da conclusão: como é fácil trocar de "
                   "<b>marca</b>, a demanda da " + azb("empresa") + " é " + vd("mais elástica") + " que a do "
                   + azb("mercado") + "."),
        "destrinchando": [
            "Elasticidade-preço cresce com a disponibilidade de " + azb("substitutos") + ". Para a demanda de "
            "uma <b>marca</b>, os substitutos são as outras marcas do mesmo produto — muito próximos. Para a "
            "demanda do <b>mercado</b>, os substitutos são outros produtos — mais distantes.",
            "Exemplo: se só a Coca-Cola sobe o preço, muitos migram para outra cola (queda grande da quantidade "
            "da firma). Se <b>todos</b> os refrigerantes sobem, o consumidor só reduz o consumo ou troca por "
            "suco e água (queda menor). Logo " + vd("|ε<sub>firma</sub>| > |ε<sub>mercado</sub>|") + ".",
            "Espectro das estruturas: " + azb("monopólio") + " — firma = mercado, elasticidades iguais; "
            + azb("concorrência monopolística") + " e oligopólio com diferenciação — demanda da firma "
            "negativamente inclinada, porém mais plana que a do mercado; " + azb("concorrência perfeita")
            + " — demanda da firma horizontal (elasticidade infinita), enquanto a do mercado é negativamente "
            "inclinada.",
            "Ligação com o poder de mercado: pelo " + azb("índice de Lerner") + ", " + vd("(P − CMg)/P = "
            "1/|ε<sub>firma</sub>|") + ". Quanto mais elástica a demanda da firma, menor o markup — por isso a "
            "firma de um setor com muitos rivais próximos tem pouco poder de preço, mesmo que a demanda do "
            "setor seja inelástica.",
            vm("Regra-âncora: substituto fácil → demanda mais elástica; e a marca sempre tem substitutos mais "
               "fáceis que o setor."),
        ],
        "dissecando": (cz("[inversão · contradição]") + " O item é internamente contraditório: a segunda frase "
                       "(troca fácil entre marcas) é a razão de a elasticidade da firma ser <b>maior</b>. A "
                       "banca inverte só o comparativo e conta com a leitura apressada de uma justificativa "
                       "correta. Teste rápido: “mais fácil trocar” = mais elástico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio, a elasticidade da demanda da empresa coincide com a da demanda de "
            "mercado.”</i> → CERTO",
            "<i>“Em concorrência perfeita, a demanda da firma individual é perfeitamente inelástica.”</i> → "
            "ERRADO (é perfeitamente elástica, horizontal)",
        ])],
        "reescrita": ("Em mercados de concorrência imperfeita, a elasticidade da curva de demanda das empresas é "
                      + hl("maior") + " do que a elasticidade da demanda do mercado. Isso ocorre porque é mais "
                      "fácil para os consumidores optarem por consumir um produto altamente substituível de outra "
                      "empresa do que optarem por consumir um outro produto totalmente diferente."),
        "tipo_erro": ["INVERSAO", "CONTRADICAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A demanda da empresa individual é mais elástica que a do mercado, porque há "
                             "substitutos próximos (outras marcas); no monopólio coincidem; na concorrência "
                             "perfeita a da firma é horizontal. Reescrita: trocar “menor” por “maior”. Verso com "
                             "várias respostas de IA empilhadas, convergentes."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 60", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (exemplo do refrigerante)"},
                          {"ref": "IMAGEM 61", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (espectro das estruturas descrito no 📖)"},
                          {"ref": "IMAGEM 62", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 63", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 64", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 65", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0194
    {
        "id": "ECO-E1-0194-1", "fonte_ref": "E1-0194", "destino": "07-A", "subtema": H2["ofcp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": True,
        "comando": "Acerca da curva de oferta da firma em mercado competitivo, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A curva de oferta de um bem representa a parcela da curva de custo marginal acima do custo "
                      "médio total."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de oferta de um bem representa a parcela da curva de custo marginal acima do ")
                   + vm("custo médio total") + az("."),
        "poucas": ("No curto prazo, a oferta da firma competitiva é o " + azb("CMg acima do mínimo do CVMe")
                   + " (ponto de fechamento), não do CMe total: com P entre CVMe e CMe, ela produz com "
                   "prejuízo, porque perderia mais parando."),
        "destrinchando": [
            "A firma competitiva produz onde " + vd("P = CMg") + ". A pergunta é a partir de que preço ela "
            "produz. No curto prazo o custo fixo é afundado: paga-se de qualquer forma, produzindo ou não.",
            "Três faixas de preço: (1) " + vd("P > CMe") + " — lucro; produz em P = CMg. (2) "
            + vd("CVMe < P < CMe") + " — prejuízo, mas a receita cobre o custo variável e ainda amortiza parte "
            "do fixo; parar daria prejuízo maior (todo o custo fixo). Produz. (3) " + vd("P < CVMe mínimo")
            + " — nem o variável se paga; a firma fecha e perde só o fixo.",
            "Daí: oferta de curto prazo = trecho do CMg acima do " + azb("ponto de fechamento") + " (mínimo do "
            "CVMe). O mínimo do CMe total é o " + azb("ponto de nivelamento") + " (lucro zero), que importa "
            "para a decisão de <b>longo prazo</b>.",
            "No longo prazo não há custo fixo: a firma só permanece se P ≥ CMe mínimo. Aí, sim, a oferta "
            "individual é o CMg acima do mínimo do CMe — e com livre entrada o preço é empurrado justamente "
            "para esse mínimo.",
            vm("Regra-âncora: curto prazo → piso no CVMe (fechamento); longo prazo → piso no CMe (saída)."),
        ],
        "grafico_verso": "ECO-E1-0194-1-V1",
        "dissecando": (cz("[troca de conceito · anacronismo]") + " O item usa a condição de <b>longo prazo</b> "
                       "(CMe total) sem dizer o horizonte; a leitura padrão da banca é a curva de oferta de "
                       "curto prazo, cuja referência é o CVMe. 🔥 A dupla fechamento (CVMe) × nivelamento (CMe) "
                       "é cobrada com frequência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, a curva de oferta da firma competitiva é o trecho da curva de custo marginal "
            "acima do mínimo do custo variável médio.”</i> → CERTO",
            "<i>“Com preço abaixo do custo médio total, a firma competitiva interrompe imediatamente a "
            "produção.”</i> → ERRADO (só se P < CVMe; senão produz com prejuízo)",
        ])],
        "reescrita": ("A curva de oferta de um bem representa a parcela "
                      "da curva de custo marginal acima do " + hl("mínimo do custo variável médio") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "ANACRONISMO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Correto seria acima do custo variável médio (curto prazo): a firma opera com "
                             "prejuízo enquanto cobre o custo variável; o CMe total é a referência de longo "
                             "prazo. Verso longo, com várias respostas de IA e reescritas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (68).png, image (64).png, image (66).png", "tipo_fonte": "não preservada",
                           "lado": "verso", "acao": "cortadas; gráfico didático novo em ECO-E1-0194-1-V1"}],
        "alertas": ["texto_corrigido: a fonte formulava o item como pergunta (“É correto afirmar que …?”); "
                    "convertida em afirmação"],
    },
    # ------------------------------------------------------------------ E1-0230
    {
        "id": "ECO-E1-0230-1", "fonte_ref": "E1-0230", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": "Acerca da maximização de lucro pela firma, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado em que há muitos produtores e muitos consumidores de tal modo que um "
                      "produtor isoladamente não pode fixar o preço de seu produto, é a igualdade entre receita e "
                      "custo marginais que determinará a quantidade que o produtor deverá produzir para maximizar "
                      "o lucro."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um mercado em que há muitos produtores e muitos consumidores de tal modo que um "
                      "produtor isoladamente não pode fixar o preço de seu produto, é a igualdade entre "
                      "<u>receita e custo marginais</u> que determinará a quantidade que o produtor deverá "
                      "produzir para maximizar o lucro."),
        "poucas": ("Lucro máximo em " + vd("RMg = CMg") + " — regra de qualquer estrutura. Para o tomador de "
                   "preço, RMg = P, e a regra vira " + vd("P = CMg") + "."),
        "destrinchando": [
            "O mercado descrito é o de " + azb("concorrência perfeita") + ": atomicidade (muitos vendedores e "
            "compradores) torna cada produtor " + azb("tomador de preço") + ". Vender uma unidade a mais "
            "acrescenta exatamente P à receita: " + vd("RMg = RMe = P") + ".",
            "Lucro π = RT − CT. Derivando e igualando a zero: RMg − CMg = 0. Graficamente, é a quantidade em "
            "que a distância vertical entre a receita total (reta, na concorrência perfeita) e o custo total "
            "é máxima — onde as inclinações das duas curvas são iguais.",
            "Condição de segunda ordem: o CMg deve estar <b>subindo</b> no ponto (cortando a RMg de baixo para "
            "cima). Há, em geral, dois pontos com P = CMg; o primeiro, no trecho descendente do CMg, é um "
            "mínimo de lucro.",
            "Condição de operação: no curto prazo, só vale produzir se P ≥ CVMe mínimo; abaixo disso, a "
            "quantidade ótima é zero.",
            vm("Regra-âncora: RMg = CMg em qualquer estrutura; na concorrência perfeita, RMg = P."),
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Definição de manual, descrita por perífrase "
                       "(“muitos produtores … não pode fixar o preço”). Quem espera ver “preço = custo "
                       "marginal” pode estranhar “receita marginal” e marcar ERRADO — mas, para o tomador de "
                       "preço, as duas formulações são equivalentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é a igualdade entre receita média e custo médio que determinará a quantidade que maximiza o "
            "lucro.”</i> → ERRADO (troca de conceito: RMe = CMe é lucro zero)",
            "<i>“Nesse mercado, a receita marginal do produtor é igual ao preço de mercado.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Lucro = RT − CT; derivando, lucro máximo em RMg = CMg, válido para qualquer "
                             "estrutura (inclusive monopólio); graficamente, maior distância entre receita e "
                             "custo totais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled.png, image (78).png", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "cortadas (imagens do verso não preservadas no caderno E1)"}],
        "alertas": ["banca_provavel: possivelmente CACD/2014 (CEBRASPE), não confirmado pela fonte"],
    },
    # ------------------------------------------------------------------ E1-0233
    {
        "id": "ECO-E1-0233-1", "fonte_ref": "E1-0233", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": True,
        "comando": "Acerca das características dos mercados competitivos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Uma das características de um mercado competitivo ou de concorrência perfeita é a "
                      "homogeneidade do produto, ainda que as marcas acentuem diferenças nas qualidades do "
                      "produto; nesse caso, os consumidores irão preferir marcas de menor preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma das características de um mercado competitivo ou de concorrência perfeita é a "
                      "homogeneidade do produto, ") + vm("ainda que as marcas acentuem diferenças nas "
                      "qualidades do produto; nesse caso, os consumidores irão preferir marcas de menor preço")
                   + az("."),
        "poucas": (azb("Homogeneidade") + " significa que não há diferença de qualidade percebida entre "
                   "vendedores. Se as marcas acentuam diferenças, o produto deixou de ser homogêneo — já é "
                   + azb("concorrência monopolística") + "."),
        "destrinchando": [
            "Hipóteses da " + azb("concorrência perfeita") + ": atomicidade, " + vd("produto homogêneo") + ", "
            "informação perfeita, livre entrada e saída, mobilidade de fatores. Da homogeneidade decorre o "
            + vd("preço único") + ": quem cobrar um centavo a mais perde toda a clientela, porque os produtos "
            "são substitutos perfeitos.",
            "Por isso, em concorrência perfeita, “o consumidor prefere o mais barato” nem chega a ser escolha "
            "entre marcas: há um só preço. Exemplos de " + oc("Pindyck e Rubinfeld") + ": milho, petróleo, "
            "cobre, algodão — as " + azb("commodities") + ", em que o comprador nem pergunta de que fazenda "
            "veio o grão.",
            "Quando a marca diferencia qualidade (real ou percebida), cada firma tem um pequeno poder de preço: "
            "pode cobrar mais sem perder todos os clientes. É a " + azb("concorrência monopolística") + " de "
            + oc("Chamberlin") + ": muitas firmas, entrada livre, mas produto diferenciado.",
            "E o consumidor, diante de diferenças de qualidade, não escolhe necessariamente o menor preço: "
            "pesa qualidade e preço. A segunda metade do item também falha por isso.",
            vm("Regra-âncora: diferenciação por marca e homogeneidade do produto são incompatíveis."),
        ],
        "dissecando": (cz("[meia-verdade · contradição]") + " A 1ª oração é a hipótese correta; o erro foi "
                       "enxertado no “ainda que”, que acrescenta uma condição que destrói a própria "
                       "homogeneidade. O “nesse caso…” fecha com um desfecho plausível, para dar ar de "
                       "consequência lógica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na concorrência monopolística, as firmas vendem produtos diferenciados, o que lhes confere "
            "algum poder sobre o preço.”</i> → CERTO",
            "<i>“A homogeneidade do produto na concorrência perfeita permite a cada firma cobrar preço "
            "diferente conforme sua marca.”</i> → ERRADO (homogeneidade implica preço único)",
        ])],
        "reescrita": ("Uma das características de um mercado competitivo ou de concorrência perfeita é a "
                      "homogeneidade do produto" + hl(", sem diferenças de qualidade entre as marcas; por isso, "
                      "vigora um preço único, e nenhuma firma pode cobrar acima dele sem perder seus "
                      "clientes") + "."),
        "tipo_erro": ["MEIA_VERDADE", "CONTRADICAO"], "moduladores": ["ainda que"], "dificuldade": 1,
        "comentario_fonte": ("Produto homogêneo não admite diferenciação de qualidade por marcas, que é traço da "
                             "concorrência monopolística; citação de Pindyck e Rubinfeld sobre homogeneidade e "
                             "commodities; lista de hipóteses da concorrência perfeita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (83).png", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada no caderno E1)"}],
        "alertas": ["banca_provavel: possivelmente CACD/2014 (CEBRASPE), não confirmado pela fonte"],
    },
    # ------------------------------------------------------------------ E1-0238
    {
        "id": "ECO-E1-0238-1", "fonte_ref": "E1-0238", "destino": "07-A", "subtema": H2["ofcp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False,
        "errei": False,
        "comando": "Acerca do comportamento da firma em mercados competitivos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Nos mercados competitivos, a maximização dos lucros no curto prazo, que exige que o preço "
                      "seja superior ao custo médio de produção, impede uma firma de operar com perdas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Nos mercados competitivos, a maximização dos lucros no curto prazo, ")
                   + vm("que exige que o preço seja superior ao custo médio de produção, impede") + az(" uma "
                   "firma de operar com perdas."),
        "poucas": ("Maximizar lucro exige " + vd("P = CMg") + ", não P > CMe. No curto prazo a firma pode "
                   "operar " + azb("com prejuízo") + ", desde que P cubra o " + azb("custo variável médio") + "."),
        "destrinchando": [
            "“Maximizar lucro” é escolher a melhor quantidade dado o preço — e a melhor pode ser a que "
            + azb("minimiza o prejuízo") + ". A condição é P = CMg (com o CMg crescente), e ela não diz nada "
            "sobre o sinal do lucro.",
            "No curto prazo o custo fixo já está comprometido. Se " + vd("CVMe < P < CMe") + ", a firma perde "
            "dinheiro produzindo, mas perderia mais parando (todo o custo fixo). Produzir é a melhor opção, e "
            "ela opera com perdas. Só fecha se " + vd("P < CVMe mínimo") + ".",
            "A comparação entre P e CMe decide outra coisa: a " + azb("permanência no longo prazo") + ". "
            "P > CMe → lucro econômico, atrai entrantes; P = CMe → lucro normal; P < CMe → a firma sai do "
            "mercado quando puder desfazer-se dos custos fixos.",
            "Exemplo: um hotel de praia na baixa temporada cobra diárias que não pagam o aluguel do imóvel, "
            "mas pagam faxina, energia e pessoal temporário. Fechar seria pior: o aluguel corre de qualquer "
            "jeito.",
            vm("Regra-âncora: P = CMg diz quanto produzir; P × CVMe diz se produz; P × CMe diz se fica no "
               "longo prazo."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item cria uma condição falsa para a "
                       "maximização (P > CMe, que é condição de lucro positivo) e daí deduz uma consequência "
                       "falsa (impossibilidade de prejuízo). A pista é o “no curto prazo”: é justamente o "
                       "horizonte em que operar com perdas é racional."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, uma firma competitiva continua produzindo, ainda que com prejuízo, se o preço "
            "cobrir o custo variável médio.”</i> → CERTO",
            "<i>“No longo prazo, uma firma competitiva permanece no mercado mesmo com preço inferior ao custo "
            "médio total.”</i> → ERRADO (no longo prazo ela sai)",
        ])],
        "reescrita": ("Nos mercados competitivos, a maximização dos lucros no curto prazo, " + hl("que exige que "
                      "o preço seja igual ao custo marginal, não impede") + " uma firma de operar com perdas"
                      + hl(", desde que o preço cubra o custo variável médio") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Maximização exige RMg = CMg (= P), não P > CMe; a comparação P × CMe diz respeito "
                             "à permanência no longo prazo; com P < CMe a firma sai no longo prazo, mas opera "
                             "com perdas no curto."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: possivelmente CACD/2012 (CEBRASPE), não confirmado pela fonte"],
    },
    # ------------------------------------------------------------------ E1-0243
    {
        "id": "ECO-E1-0243-1", "fonte_ref": "E1-0243", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Acerca do modelo de concorrência perfeita, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A consequência direta dos pressupostos de produto homogêneo, informação completa e livre "
                      "entrada e saída de agentes pequenos e numerosos em um mercado de concorrência perfeita é um "
                      "único preço de equilíbrio por todo o mercado do produto em questão, a menos que haja "
                      "choques que possam produzir abalos temporários."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A consequência direta dos pressupostos de produto homogêneo, informação completa e livre "
                      "entrada e saída de agentes pequenos e numerosos em um mercado de concorrência perfeita é "
                      "um <u>único preço de equilíbrio</u> por todo o mercado do produto em questão, a menos que "
                      "haja choques que possam produzir abalos <u>temporários</u>."),
        "poucas": ("Produto homogêneo + informação completa = ninguém paga mais caro por algo igual; muitos "
                   "agentes pequenos = ninguém fixa preço. Resultado: " + azb("lei do preço único") + " no "
                   "mercado, salvo desvios passageiros."),
        "destrinchando": [
            "Cada hipótese tem um papel: " + vd("homogeneidade") + " torna os produtos substitutos perfeitos; "
            + vd("informação completa") + " faz todos saberem onde está o preço mais baixo; "
            + vd("atomicidade") + " (agentes pequenos e numerosos) impede qualquer um de influenciar o preço; "
            + vd("livre entrada e saída") + " elimina lucros extraordinários no longo prazo.",
            "Juntas, elas produzem a " + azb("lei do preço único") + ": se um vendedor cobrar acima, perde "
            "todos os clientes; se cobrar abaixo, abre mão de receita sem necessidade (ao preço de mercado ele "
            "vende quanto quiser). O preço converge para um só valor.",
            "Isso não quer dizer preço <b>imutável</b>: deslocamentos de oferta ou de demanda mudam o "
            "equilíbrio. O que se mantém é a unicidade — em cada momento, um só preço para todo o mercado; "
            "choques produzem dispersões temporárias, que a arbitragem desfaz.",
            "Mesmo raciocínio, em escala internacional: a lei do preço único sustenta a " + azb("paridade do "
            "poder de compra") + " (PPC) — e as violações reais (custos de transporte, barreiras, bens não "
            "comercializáveis) mostram quão exigentes são essas hipóteses.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " A ressalva “a menos que haja choques … "
                       "temporários” protege o item contra a objeção de que preços mudam. Redação longa e "
                       "imprecisa (“consequência direta”), que convida a procurar um erro inexistente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em concorrência perfeita, o preço de equilíbrio é invariável, pois nenhum agente tem poder "
            "sobre ele.”</i> → ERRADO (choques de oferta e demanda alteram o equilíbrio)",
            "<i>“A homogeneidade do produto é condição para a existência de preço único em concorrência "
            "perfeita.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["a menos que", "temporários"],
        "dificuldade": 1,
        "comentario_fonte": ("Os pressupostos levam a um preço de equilíbrio único e estável, do qual o mercado "
                             "se afasta só com choques não antecipados e temporários; o equilíbrio pode mudar "
                             "com oferta e demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0246
    {
        "id": "ECO-E1-0246-1", "fonte_ref": "E1-0246", "destino": "07-A", "subtema": H2["lpcp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": True,
        "comando": "Acerca das economias de escala e da oferta de longo prazo da indústria, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A presença de substanciais economias externas de escala em determinada indústria é "
                      "compatível com a existência de uma curva de oferta de longo prazo positivamente "
                      "inclinada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A presença de substanciais economias externas de escala em determinada indústria é "
                      "compatível com a existência de uma curva de oferta de longo prazo ")
                   + vm("positivamente inclinada") + az("."),
        "poucas": ("Com " + azb("economias externas") + " substanciais, o custo de cada firma cai quando a "
                   "<b>indústria</b> cresce: a oferta de longo prazo da indústria é " + vd("negativamente "
                   "inclinada") + " (decrescente)."),
        "destrinchando": [
            "Oferta de longo prazo da indústria competitiva: com livre entrada, o preço tende ao CMe mínimo das "
            "firmas. A inclinação depende do que acontece com esse mínimo quando a indústria se expande. "
            "Três casos: " + azb("custos constantes") + " (horizontal), " + azb("custos crescentes") + " — "
            "insumos encarecem (positiva), " + azb("custos decrescentes") + " — " + vd("economias externas")
            + " (negativa).",
            "Economias externas (" + oc("Marshall") + "): fornecedores especializados, mão de obra qualificada "
            "concentrada, difusão de conhecimento. Quanto maior a indústria, menor o custo de cada firma — "
            "ainda que todas continuem pequenas e competitivas.",
            "Em " + oc("Krugman e Obstfeld") + ", isso aparece como a " + azb("curva de oferta "
            "decrescente") + " (<i>forward-falling supply curve</i>): mais produção, preço menor. É a base para "
            "explicar polos industriais e o peso da vantagem histórica no comércio internacional.",
            "Correção do comentário de origem: economias de escala não são fenômeno de curto prazo nem "
            "dependem de custo fixo; e rendimentos de escala da firma descrevem economias <b>internas</b>, não "
            "externas.",
            vm("Regra-âncora: economias externas substanciais → oferta de longo prazo da indústria "
               "decrescente."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item inverte a inclinação típica e se "
                       "apoia no reflexo “oferta sobe com o preço”. O “substanciais” é a pista: com economias "
                       "externas fortes, o efeito de redução de custo domina. 🔥 Tema recorrente nas provas de "
                       "comércio internacional do CACD (Krugman)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em indústria de custos crescentes, a curva de oferta de longo prazo é positivamente "
            "inclinada.”</i> → CERTO",
            "<i>“Economias externas de escala exigem que a indústria seja dominada por poucas firmas "
            "grandes.”</i> → ERRADO (troca com economias internas)",
        ])],
        "reescrita": ("A presença de substanciais economias externas de escala em determinada indústria é "
                      "compatível com a existência de uma curva de oferta de longo prazo " + hl("negativamente "
                      "inclinada (decrescente)") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["substanciais"], "dificuldade": 3,
        "comentario_fonte": ("Comentário de origem confunde economias de escala com diluição de custo fixo de "
                             "curto prazo e discute retornos de escala da firma (CMg crescente, constante ou "
                             "decrescente); conclusão ERRADO."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: possivelmente CACD/2010 (CEBRASPE), não confirmado pela fonte",
                    "qualidade_fonte: o comentário de origem associa economias de escala ao curto prazo e ao "
                    "custo fixo e não trata de economias externas — reescrito"],
    },
    # ------------------------------------------------------------------ E1-0249
    {
        "id": "ECO-E1-0249-1", "fonte_ref": "E1-0249", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de concorrência perfeita, as empresas maximizam seus lucros ao produzir no ponto "
                      "em que o preço é superior ao custo marginal de produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de concorrência perfeita, as empresas maximizam seus lucros ao produzir no "
                      "ponto em que o preço é ") + vm("superior") + az(" ao custo marginal de produção."),
        "poucas": ("Tomadora de preço, a firma tem " + vd("RMg = P") + "; o lucro é máximo em "
                   + vd("P = CMg") + ". Se P > CMg, ainda vale produzir mais."),
        "destrinchando": [
            "Raciocínio na margem: se " + vd("P > CMg") + ", a próxima unidade traz mais receita do que custo "
            "— produzir mais aumenta o lucro. Se " + vd("P < CMg") + ", a última unidade custou mais do que "
            "rendeu — produzir menos aumenta o lucro. O máximo está na igualdade.",
            "Por que P e não RMg genérica: na " + azb("concorrência perfeita") + " a firma vende quanto quiser "
            "ao preço de mercado, então cada unidade adicional rende exatamente P (" + vd("RMg = RMe = P")
            + "). A regra geral RMg = CMg vira P = CMg.",
            "Onde P > CMg aparece: no " + azb("monopólio") + " e nas demais estruturas com poder de mercado, "
            "porque lá RMg < P. A diferença P − CMg é o " + azb("markup") + " e gera peso morto; P = CMg é "
            "a condição de " + azb("eficiência alocativa") + ".",
            "No longo prazo competitivo, além de P = CMg, a livre entrada leva a P = CMe mínimo: lucro "
            "econômico zero.",
            vm("Regra-âncora: concorrência perfeita → P = CMg; poder de mercado → P > CMg."),
        ],
        "dissecando": (cz("[troca de conceito · troca de ator]") + " O item transplanta para a concorrência "
                       "perfeita o resultado do monopólio (P > CMg). Uma só palavra — “superior” — decide o "
                       "gabarito; o resto é definição correta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio, as empresas maximizam seus lucros produzindo onde o preço é superior ao custo "
            "marginal.”</i> → CERTO",
            "<i>“Em concorrência perfeita, a firma maximiza lucro onde o preço iguala o custo médio.”</i> → "
            "ERRADO (P = CMe é lucro zero, não regra de máximo)",
        ])],
        "reescrita": ("No modelo de concorrência perfeita, as empresas maximizam seus lucros ao produzir no "
                      "ponto em que o preço é " + hl("igual") + " ao custo marginal de produção."),
        "tipo_erro": ["TROCA_CONCEITO", "TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Em concorrência perfeita o lucro é máximo onde P = RMg = CMg; firma tomadora de "
                             "preço não vende acima do preço de mercado; no longo prazo, lucro econômico zero."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0250
    {
        "id": "ECO-E1-0250-1", "fonte_ref": "E1-0250", "destino": "07-A", "subtema": H2["lpcp"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado 07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de concorrência perfeita, a entrada e saída de empresas é livre, o que significa "
                      "que novas empresas podem entrar no mercado facilmente e as empresas existentes podem sair "
                      "quando não estão obtendo lucro suficiente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de concorrência perfeita, a entrada e saída de empresas é <u>livre</u>, o que "
                      "significa que novas empresas podem entrar no mercado facilmente e as empresas existentes "
                      "podem sair quando não estão obtendo lucro suficiente."),
        "poucas": (azb("Livre entrada e saída") + " é hipótese da concorrência perfeita: sem barreiras nem "
                   "custos irrecuperáveis, firmas entram quando há lucro econômico e saem quando há prejuízo."),
        "destrinchando": [
            "Livre entrada e saída = ausência de " + azb("barreiras à entrada") + " (patentes, escala mínima "
            "enorme, controle de insumos) e de " + azb("custos irrecuperáveis") + " (<i>sunk costs</i>) que "
            "prendam a firma ao mercado.",
            "É o motor do ajuste de longo prazo: " + vd("P > CMe") + " → lucro econômico → entrada → oferta "
            "da indústria ↑ → preço ↓; " + vd("P < CMe") + " → prejuízo → saída → oferta ↓ → preço ↑. O "
            "processo para em " + vd("P = CMe mínimo") + ", com lucro econômico zero.",
            "“Lucro suficiente” deve ser lido em termos econômicos: a firma sai quando não cobre o "
            + azb("custo de oportunidade") + " dos recursos (lucro econômico negativo), ainda que tenha lucro "
            "contábil.",
            "Contraste: no " + azb("monopólio") + " e em muitos oligopólios, barreiras bloqueiam a entrada e "
            "permitem lucro persistente; na " + azb("concorrência monopolística") + ", a entrada também é "
            "livre e o lucro de longo prazo também tende a zero.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Definição de manual, com linguagem coloquial "
                       "(“facilmente”, “lucro suficiente”) que pode soar imprecisa e induzir ERRADO. A banca "
                       "costuma errar o item trocando a estrutura (“no monopólio, a entrada é livre”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, a entrada de novas firmas é livre e o lucro de longo prazo tende a "
            "zero.”</i> → ERRADO (economias de escala são barreira)",
            "<i>“Com livre entrada, o lucro econômico das firmas competitivas tende a zero no longo "
            "prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": "Verso apenas repete a assertiva com o gabarito CERTO.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0255
    {
        "id": "ECO-E1-0255-1", "fonte_ref": "E1-0255", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos conceitos de receita da firma, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "A receita marginal é a mudança na receita total dividida pela mudança no produto total.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A receita marginal é a mudança na receita total <u>dividida pela mudança no produto "
                      "total</u>."),
        "poucas": (azb("Receita marginal") + " = " + vd("ΔRT/ΔQ") + " (no limite, dRT/dQ): quanto a receita "
                   "total varia por unidade adicional vendida."),
        "destrinchando": [
            "Família de conceitos: " + azb("receita total") + " RT = P × Q; " + azb("receita média") + " RMe "
            "= RT/Q = P (a curva de RMe é a própria demanda); " + azb("receita marginal") + " RMg = ΔRT/ΔQ.",
            "Concorrência perfeita: P constante para a firma → RT é uma reta saindo da origem e "
            + vd("RMg = RMe = P") + ".",
            "Monopólio com demanda linear P = a − bQ: RT = aQ − bQ² e " + vd("RMg = a − 2bQ") + " — mesma "
            "ordenada na origem da demanda, inclinação duas vezes maior. RMg < P porque, para vender mais uma "
            "unidade, o monopolista baixa o preço de todas.",
            "Ligação com elasticidade: " + vd("RMg = P(1 − 1/|ε|)") + ". No trecho elástico (|ε| > 1), RMg > "
            "0; com |ε| = 1, RMg = 0 e a RT é máxima; no trecho inelástico, RMg < 0 — por isso o monopolista "
            "nunca opera na parte inelástica da demanda.",
            "Não confundir com o produto marginal (ΔQ/ΔL), em que o denominador é o insumo, não o produto.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição pura. A versão ERRADA costuma inverter a razão "
                       "(“mudança no produto dividida pela mudança na receita”) ou trocar o numerador pela "
                       "receita média."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A receita marginal é a receita total dividida pela quantidade vendida.”</i> → ERRADO (essa é "
            "a receita média)",
            "<i>“No monopólio com demanda linear, a curva de receita marginal tem o dobro da inclinação da "
            "curva de demanda.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "RMg = acréscimo de receita por unidade adicional; RMg = dRT/dQ.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (52).jpeg", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "cortada (fórmula dRT/dQ absorvida no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0257
    {
        "id": "ECO-E1-0257-1", "fonte_ref": "E1-0257", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": ("Se a natureza do produto requer que produtores usem grandes quantidades de maquinário e "
                      "equipamento especializado, então a indústria não se adequa às hipóteses de competição "
                      "perfeita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a natureza do produto requer que produtores usem grandes quantidades de maquinário e "
                      "<u>equipamento especializado</u>, então a indústria não se adequa às hipóteses de "
                      "competição perfeita."),
        "poucas": ("Capital fixo grande e específico cria " + azb("custos irrecuperáveis") + " e "
                   + azb("economias de escala") + ": a entrada e a saída deixam de ser livres e o número de "
                   "firmas tende a ser pequeno."),
        "destrinchando": [
            "Duas hipóteses da " + azb("concorrência perfeita") + " ficam ameaçadas: " + vd("livre entrada e "
            "saída") + " e " + vd("atomicidade") + " (muitas firmas pequenas).",
            "Entrada: exigir grande investimento inicial é uma das barreiras clássicas de " + oc("Joe Bain")
            + " (exigência de capital). Poucos conseguem financiar a planta.",
            "Saída: equipamento <b>especializado</b> não tem uso alternativo nem bom mercado de revenda — é "
            + azb("custo afundado") + ". A firma não sai com facilidade, e o entrante sabe que, se der errado, "
            "perde o investimento; isso também desestimula a entrada.",
            "Escala: com custo fixo alto, o CMe cai por uma faixa longa de produção; a " + azb("escala mínima "
            "eficiente") + " fica grande em relação ao mercado, e cabem poucas firmas — oligopólio ou até "
            "monopólio natural (siderurgia, refino, aviação).",
            "Contraste com mercados próximos da concorrência perfeita: agricultura de commodities, feiras "
            "livres — capital pouco específico, muitas unidades pequenas.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " O item não cita nenhuma das hipóteses pelo nome: "
                       "exige que o candidato derive, do tipo de capital, a violação da livre entrada e da "
                       "atomicidade. A palavra decisiva é “especializado” (custo afundado)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A necessidade de capital fixo elevado e específico favorece a livre entrada de novas "
            "firmas.”</i> → ERRADO (inversão: é barreira à entrada)",
            "<i>“Custos irrecuperáveis elevados dificultam tanto a entrada quanto a saída de firmas.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Altos investimentos em capital fixo dificultam a livre entrada e saída, violando "
                             "condição básica da concorrência perfeita."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0258
    {
        "id": "ECO-E1-0258-1", "fonte_ref": "E1-0258", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": ("No modelo de concorrência perfeita, o equilíbrio geral se dá, dentre outras condições, na "
                      "capacidade das firmas estabelecerem seus preços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de concorrência perfeita, o equilíbrio geral se dá, dentre outras condições, ")
                   + vm("na capacidade das firmas estabelecerem seus preços") + az("."),
        "poucas": ("Em concorrência perfeita as firmas são " + azb("tomadoras de preço") + " (<i>price "
                   "takers</i>): o preço sai da interação de oferta e demanda, e nenhuma firma isolada o "
                   "fixa."),
        "destrinchando": [
            "Por que ninguém fixa preço: cada firma é pequena demais em relação ao mercado (" + vd("atomicidade")
            + ") e vende um produto idêntico ao dos rivais (" + vd("homogeneidade") + "). Se cobrar acima do "
            "preço de mercado, vende zero; abaixo, perde receita sem ganhar nada.",
            "Para a firma, a demanda é " + azb("horizontal") + " ao preço de mercado (perfeitamente elástica). "
            "A única variável de escolha é a quantidade, fixada em P = CMg.",
            "No " + azb("equilíbrio geral") + " competitivo (" + oc("Walras") + "; formalizado por "
            + oc("Arrow e Debreu") + "), os preços são os que zeram o excesso de demanda em todos os mercados "
            "ao mesmo tempo, com todos os agentes tomando-os como dados. A figura do “leiloeiro walrasiano” "
            "expressa isso: os preços vêm de fora das decisões individuais.",
            "Fixar preço é atributo de quem tem " + azb("poder de mercado") + " — monopólio, oligopólio, "
            "concorrência monopolística.",
            vm("Regra-âncora: concorrência perfeita = tomador de preço; formador de preço = poder de mercado."),
        ],
        "dissecando": (cz("[inversão]") + " Troca “tomar” por “estabelecer” preços — exatamente o oposto da "
                       "hipótese. O “dentre outras condições” dá ar de lista técnica e disfarça a inversão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de concorrência perfeita, as firmas tomam os preços como dados e escolhem apenas a "
            "quantidade.”</i> → CERTO",
            "<i>“Na concorrência monopolística, as firmas são tomadoras de preço.”</i> → ERRADO (têm algum "
            "poder de preço pela diferenciação)",
        ])],
        "reescrita": ("No modelo de concorrência perfeita, o equilíbrio geral se dá, dentre outras condições, "
                      + hl("com firmas tomadoras de preço, incapazes de estabelecer seus preços") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["dentre outras condições"], "dificuldade": 1,
        "comentario_fonte": "Na concorrência perfeita, as firmas são tomadoras de preço, sem poder de mercado.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0259
    {
        "id": "ECO-E1-0259-1", "fonte_ref": "E1-0259", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": ("Na concorrência perfeita, o equilíbrio geral se dá, dentre outras condições, na necessidade "
                      "da observância de equilíbrio no mercado de trabalho, quando demanda e oferta de trabalho "
                      "se igualam."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na concorrência perfeita, o <u>equilíbrio geral</u> se dá, dentre outras condições, na "
                      "necessidade da observância de equilíbrio no mercado de trabalho, quando demanda e oferta "
                      "de trabalho se igualam."),
        "poucas": (azb("Equilíbrio geral") + " = todos os mercados equilibrados ao mesmo tempo, inclusive os "
                   "de fatores. O de trabalho é um deles: oferta = demanda de trabalho ao salário real de "
                   "equilíbrio."),
        "destrinchando": [
            azb("Equilíbrio parcial") + " (" + oc("Marshall") + ") olha um mercado de cada vez, com o resto "
            "constante. " + azb("Equilíbrio geral") + " (" + oc("Walras") + ", <i>Elementos de Economia Política "
            "Pura</i>, 1874) exige que bens, serviços e fatores — trabalho, capital, terra — estejam "
            "simultaneamente em equilíbrio, porque os mercados são interdependentes.",
            "No mercado de trabalho competitivo, a firma contrata até " + vd("w = P × PMg<sub>L</sub>") + " "
            "(valor do produto marginal); as famílias ofertam trabalho comparando salário e lazer. O "
            "equilíbrio iguala as duas.",
            azb("Lei de Walras") + ": se n − 1 mercados estão em equilíbrio, o n-ésimo também está — a soma "
            "dos excessos de demanda, valorados a preços, é zero.",
            "Por que importa: o " + azb("primeiro teorema do bem-estar") + " garante que o equilíbrio geral "
            "competitivo é " + vd("eficiente no sentido de Pareto") + " — o que exige todos os mercados, "
            "inclusive o de trabalho, funcionando em concorrência e equilibrados.",
            "Contraponto: para " + oc("Keynes") + ", a economia pode ficar em equilíbrio no mercado de bens com "
            "desemprego involuntário — o mercado de trabalho não se equilibra sozinho. A afirmação vale "
            "<b>dentro</b> do modelo competitivo.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item amplia o foco para além do mercado do bem; quem "
                       "pensa só em equilíbrio parcial estranha a menção ao trabalho e marca ERRADO. A redação "
                       "truncada (“na necessidade da observância”) é ruído, não erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O equilíbrio geral competitivo dispensa o equilíbrio nos mercados de fatores de "
            "produção.”</i> → ERRADO (todos os mercados se equilibram simultaneamente)",
            "<i>“Segundo a lei de Walras, se todos os mercados menos um estão em equilíbrio, o restante também "
            "está.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["dentre outras condições"], "dificuldade": 1,
        "comentario_fonte": ("O equilíbrio geral pressupõe que todos os mercados, inclusive o de trabalho, estejam "
                             "em equilíbrio."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0261
    {
        "id": "ECO-E1-0261-1", "fonte_ref": "E1-0261", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": ("Em um mercado de concorrência perfeita, a maximização do lucro de uma dada empresa ocorre "
                      "sob a mesma condição de igualdade entre o custo marginal e o custo médio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um mercado de concorrência perfeita, a maximização do lucro de uma dada empresa ocorre "
                      "sob a mesma condição de igualdade entre o custo marginal e ") + vm("o custo médio")
                   + az("."),
        "poucas": ("Lucro máximo: " + vd("RMg = CMg") + " (na concorrência perfeita, P = CMg). CMg = CMe marca "
                   "o " + azb("mínimo do custo médio") + " — condição de eficiência produtiva, não de lucro "
                   "máximo."),
        "destrinchando": [
            "Dois cruzamentos diferentes no mesmo gráfico: P = CMg dá a quantidade que maximiza o lucro; "
            "CMg = CMe dá a quantidade que minimiza o custo por unidade. Coincidem só se o preço for exatamente "
            "o CMe mínimo.",
            "Curto prazo: com " + vd("P > CMe mínimo") + ", a firma produz <b>além</b> do mínimo do CMe (onde "
            "CMg já supera o CMe) e tem lucro econômico; com P menor, produz aquém dele.",
            "Longo prazo competitivo: a livre entrada empurra o preço até " + vd("P = CMg = CMe mínimo") + ". "
            "Aí as duas condições coincidem — por isso o item seduz. Mas a coincidência é <b>resultado</b> do "
            "ajuste de mercado, não a regra de decisão da firma.",
            "Por que a firma não mira o CMe mínimo: produzir menos custos médios não é o objetivo; o objetivo é "
            "o lucro total. Se o preço está alto, vale aceitar um custo médio maior para vender mais unidades "
            "lucrativas.",
            vm("Regra-âncora: CMg = CMe → custo médio mínimo; RMg = CMg → lucro máximo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca a condição de lucro máximo (RMg = CMg) pela de "
                       "custo médio mínimo (CMg = CMe), aproveitando que as duas se cruzam no equilíbrio de longo "
                       "prazo. O “sob a mesma condição” é o gancho: “mesma” que qual? — nenhuma regra de lucro "
                       "envolve o CMe."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio de longo prazo da concorrência perfeita, o preço iguala o custo marginal e o "
            "custo médio mínimo.”</i> → CERTO",
            "<i>“A firma competitiva sempre produz no ponto de custo médio mínimo.”</i> → ERRADO (só no longo "
            "prazo; no curto, produz onde P = CMg)",
        ])],
        "reescrita": ("Em um mercado de concorrência perfeita, a maximização do lucro de uma dada empresa ocorre "
                      "sob a mesma condição de igualdade entre o custo marginal e " + hl("a receita marginal (o "
                      "preço)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Lucro máximo em RMg = CMg; CMg = CMe indica o mínimo do custo médio.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0262
    {
        "id": "ECO-E1-0262-1", "fonte_ref": "E1-0262", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": ("Em concorrência perfeita, a definição do quanto produzir de cada bem será determinada pela "
                      "atuação dos consumidores e dos produtores no mercado com os ajustamentos dados pelo "
                      "sistema de preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em concorrência perfeita, a definição do quanto produzir de cada bem será determinada pela "
                      "atuação dos consumidores e dos produtores no mercado com os ajustamentos dados pelo "
                      "<u>sistema de preços</u>."),
        "poucas": ("Na economia de mercado competitiva, o " + azb("sistema de preços") + " coordena "
                   "descentralizadamente o que e quanto produzir: preços sobem onde há escassez e caem onde há "
                   "excesso, e produtores e consumidores reagem."),
        "destrinchando": [
            "Problemas econômicos fundamentais: " + vd("o que e quanto produzir, como produzir e para quem") + ". "
            "Em economia de mercado, quem os resolve é o mecanismo de preços; em economia planificada, o órgão "
            "central de planejamento.",
            "Como os preços ajustam: excesso de demanda → preço sobe → consumidores compram menos e produtores "
            "ofertam mais; excesso de oferta → o contrário. Os preços carregam " + azb("informação") + " "
            "(escassez relativa) e " + azb("incentivo") + " (lucro).",
            oc("Adam Smith") + " (<i>A Riqueza das Nações</i>, 1776) chamou a coordenação descentralizada de "
            + azb("mão invisível") + "; " + oc("Hayek") + " (“O uso do conhecimento na sociedade”, 1945) "
            "enfatizou o preço como sinal que resume informação dispersa, que nenhum planejador teria.",
            "Limites: a alocação é eficiente só sem " + azb("falhas de mercado") + " (externalidades, bens "
            "públicos, informação assimétrica, poder de mercado) — terreno da intervenção do Estado.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Item de fundamentos, sem armadilha técnica. "
                       "A versão ERRADA atribuiria a decisão a um agente único (“será determinada pelo governo” "
                       "ou “pelas firmas, que fixam os preços”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em concorrência perfeita, a quantidade produzida de cada bem é fixada pelas firmas, que "
            "estabelecem os preços.”</i> → ERRADO (firmas são tomadoras de preço)",
            "<i>“Os preços sinalizam a escassez relativa dos bens e orientam a alocação de recursos.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O quanto produzir é definido pela interação entre oferta e demanda, ajustada pelos preços.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0264
    {
        "id": "ECO-E1-0264-1", "fonte_ref": "E1-0264", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": "Firmas em competição perfeita não têm economias de escala como um fator dominante.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Firmas em competição perfeita não têm economias de escala como um fator "
                      "<u>dominante</u>."),
        "poucas": ("Se as " + azb("economias de escala") + " dominassem, a firma maior teria custo menor e "
                   "expulsaria as demais — a " + azb("atomicidade") + " desapareceria. Concorrência perfeita "
                   "pressupõe escala mínima eficiente pequena em relação ao mercado."),
        "destrinchando": [
            "Economias de escala = custo médio de longo prazo decrescente com o volume. Quando persistem até "
            "volumes grandes em relação à demanda, a estrutura tende ao " + azb("oligopólio") + " ou ao "
            + azb("monopólio natural") + " (uma só firma produz mais barato que várias).",
            "Para caber muitas firmas pequenas, a " + vd("escala mínima eficiente") + " (fundo do CMe de "
            "longo prazo) deve ser pequena diante do mercado. As firmas até podem ter economias de escala em "
            "níveis baixos de produção, mas elas se esgotam cedo — não são “dominantes”.",
            "Daí o CMe de longo prazo em U (ou com fundo plano longo) da firma competitiva: economias de escala "
            "no início, depois rendimentos constantes ou deseconomias.",
            "Economias <b>externas</b> são outra história: dependem do tamanho da indústria, não da firma, e "
            "são compatíveis com concorrência perfeita (" + oc("Marshall") + ").",
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " O “como um fator dominante” é o que torna o "
                       "item verdadeiro: não se nega que existam economias de escala, só que prevaleçam. A "
                       "versão ERRADA tiraria o modulador (“não têm economias de escala”) ou diria que elas "
                       "são compatíveis com atomicidade em qualquer nível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Economias internas de escala substanciais, relativamente ao tamanho do mercado, levam a "
            "estruturas concentradas.”</i> → CERTO",
            "<i>“O monopólio natural surge quando há deseconomias de escala em toda a faixa relevante de "
            "produção.”</i> → ERRADO (inversão: surge com economias de escala)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["dominante"], "dificuldade": 1,
        "comentario_fonte": ("Em concorrência perfeita as firmas operam geralmente em escala eficiente mínima; "
                             "economias de escala não são o principal fator competitivo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0265
    {
        "id": "ECO-E1-0265-1", "fonte_ref": "E1-0265", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_CP,
        "rotulo_item": "Item",
        "assertiva": "Firmas em um mercado competitivo não podem influenciar a quantidade do bem que é produzida.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Firmas em um mercado competitivo não podem influenciar ") + vm("a quantidade do bem que é "
                      "produzida") + az("."),
        "poucas": ("A firma competitiva não influencia o " + azb("preço") + ", mas escolhe livremente a "
                   + azb("quantidade") + " que produz — aquela em que " + vd("P = CMg") + "."),
        "destrinchando": [
            "Divisão de papéis na " + azb("concorrência perfeita") + ": o mercado (oferta × demanda) fixa o "
            "preço; cada firma, tomando-o como dado, decide quanto produzir. Quantidade é a variável de "
            "decisão; preço é o parâmetro.",
            "A decisão segue a curva de custo marginal: preço maior → a firma desliza para cima no CMg e "
            "produz mais. Por isso a oferta de curto prazo da firma é o próprio CMg acima do mínimo do CVMe, e "
            "a oferta da indústria é a soma horizontal dessas curvas.",
            "O que a firma não consegue: mexer no preço pelo volume que vende. Como é pequena, dobrar ou zerar "
            "sua produção não altera a oferta total de modo perceptível — e é <b>nesse</b> sentido estrito "
            "que ela não “influencia” o mercado.",
            "No monopólio é diferente: a firma escolhe a quantidade <b>sabendo</b> que ela determina o preço "
            "(ao longo da demanda). Daí RMg < P.",
            vm("Regra-âncora: tomador de preço, não de quantidade."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca preço por quantidade. A frase lembra a definição de "
                       "tomador de preço e por isso soa familiar; quem lê rápido marca CERTO. Leitura "
                       "rigorosa: a firma controla a quantidade que <b>ela</b> produz, e é isso que o item "
                       "nega."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Firmas em um mercado competitivo não podem influenciar o preço de mercado do bem.”</i> → "
            "CERTO",
            "<i>“A firma competitiva produz a quantidade em que o preço iguala o custo médio.”</i> → ERRADO "
            "(regra é P = CMg)",
        ])],
        "reescrita": ("Firmas em um mercado competitivo não podem influenciar " + hl("o preço do bem, mas "
                      "escolhem a quantidade que produzem") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Cada firma decide quanto produzir, onde preço = custo marginal; o que ela não pode "
                             "influenciar é o preço."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
