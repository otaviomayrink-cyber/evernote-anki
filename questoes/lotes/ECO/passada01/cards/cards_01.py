"""Cards da passada 01 de ECO — lote de redação 01 (caderno E1, nota 01)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "fund": "🧭 Fundamentos e escassez",
    "cpp": "📐 Curva de possibilidades de produção",
    "dem": "📈 Demanda: determinantes e deslocamentos",
    "ofe": "🏭 Oferta: determinantes e deslocamentos",
    "bens": "🏷️ Classificação dos bens",
    "eq": "⚖️ Equilíbrio e estática comparativa",
}

CMD_FUND = "Julgue o item a seguir, relativo aos conceitos fundamentais da ciência econômica."
CMD_BENS = "Julgue o item a seguir, relativo aos bens econômicos e à sua classificação."
CMD_DEM = "Julgue o item a seguir, relativo à demanda e aos seus determinantes."
CMD_OFE = "Julgue o item a seguir, relativo à oferta, à demanda e aos deslocamentos de suas curvas."

ALERTA_2012 = ("banca_provavel: CEBRASPE (item de 2012 no estilo da banca; a fonte só traz o ano, sem órgão) — "
               "não confirmada")

CARDS = [
    # ------------------------------------------------------------------ E1-0003
    {
        "id": "ECO-E1-0003-1", "fonte_ref": "E1-0003", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False,
        "errei": False,
        "comando": CMD_DEM,
        "rotulo_item": "Item",
        "assertiva": ("Suponha que o aumento substancial dos preços cobrados para o estacionamento de veículos nas "
                      "grandes cidades eleve a quantidade demandada de corridas de táxi nesses locais. Dessa forma, "
                      "conclui-se que esse aumento de preços provoca um deslocamento ao longo da curva de demanda "
                      "por serviços de táxi."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Suponha que o aumento substancial dos preços cobrados para o estacionamento de veículos "
                       "nas grandes cidades eleve a quantidade demandada de corridas de táxi nesses locais. Dessa "
                       "forma, conclui-se que esse aumento de preços provoca um ")
                    + vm("deslocamento ao longo da curva") + az(" de demanda por serviços de táxi.")),
        "poucas": ("O preço do estacionamento não está nos eixos do gráfico do táxi: é um " + azb("determinante "
                   "externo") + " da demanda. Quando ele muda, a <b>curva inteira</b> de demanda por táxi se "
                   "desloca para a direita; não há movimento ao longo dela."),
        "destrinchando": [
            "A curva de demanda por táxi relaciona a quantidade de corridas ao <b>preço da corrida</b>, mantidos "
            "constantes os demais fatores (renda, gostos, preços de bens relacionados, expectativas, número de "
            "consumidores). Só a variação do preço da própria corrida produz " + azb("movimento ao longo da "
            "curva") + " (variação da quantidade demandada).",
            "Estacionar o carro próprio e andar de táxi são formas alternativas de se deslocar na cidade: o "
            "carro com estacionamento é " + azb("substituto") + " do táxi. Encarecido o estacionamento, parte "
            "dos motoristas migra para o táxi, e a demanda por corridas aumenta <b>a cada preço</b> da corrida — "
            "a curva vai para a direita (ou, o que é o mesmo, para cima).",
            "Vocabulário que a banca cobra: " + azb("variação da demanda") + " = deslocamento da curva; "
            + azb("variação da quantidade demandada") + " = movimento sobre a curva. O item usa a expressão "
            "“quantidade demandada” no cenário, mas o que decide é a <b>causa</b>: um fator fora dos eixos.",
            "Para haver movimento ao longo da demanda por táxi, seria preciso mudar o preço da corrida — por "
            "exemplo, por um aumento da oferta de táxis (novas licenças, aplicativos) que barateasse as corridas.",
            vm("Regra-âncora: preço do próprio bem → anda na curva; preço de outro bem → a curva anda."),
        ],
        "grafico_verso": "ECO-E1-0003-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O cenário é verdadeiro (estacionamento caro → mais "
                       "corridas); o erro está só na conclusão, que troca “deslocamento da curva” por "
                       "“deslocamento ao longo da curva”. A palavra “quantidade demandada” no enunciado funciona "
                       "como isca. Pista: a variável que mudou não é o preço da corrida."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…esse aumento de preços desloca para a direita a curva de demanda por serviços de táxi.”</i> → "
            "CERTO",
            "<i>“…esse aumento de preços desloca para a esquerda a curva de demanda por serviços de táxi, por "
            "serem bens complementares.”</i> → ERRADO (relação trocada: são substitutos)",
        ])],
        "reescrita": ("Suponha que o aumento substancial dos preços cobrados para o estacionamento de veículos nas "
                      "grandes cidades eleve a quantidade demandada de corridas de táxi nesses locais. Dessa forma, "
                      "conclui-se que esse aumento de preços provoca um deslocamento " + hl("da curva de demanda "
                      "por serviços de táxi para a direita") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Estacionamento e táxi são substitutos; o aumento do preço do estacionamento é "
                             "variável externa ao mercado de táxi e desloca a curva de demanda para a direita, e "
                             "não ao longo dela. Vários comentários repetidos; um deles chama o deslocamento da "
                             "demanda de “alteração da oferta”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [
            {"ref": "image (30).png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel (mecanismo redesenhado em ECO-E1-0003-1-V1)"},
            {"ref": "image (31).png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel"}],
        "alertas": [ALERTA_2012],
    },
    # ------------------------------------------------------------------ E1-0004
    {
        "id": "ECO-E1-0004-1", "fonte_ref": "E1-0004", "destino": "01", "subtema": H2["ofe"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False,
        "errei": True,
        "comando": CMD_OFE,
        "rotulo_item": "Item",
        "assertiva": ("Mudanças legislativas que facilitem a entrada de mão de obra estrangeira especializada na "
                      "área de eletrônica contribuem para deslocar — para baixo e para a direita — a curva de "
                      "oferta de longo prazo da indústria eletrônica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Mudanças legislativas que facilitem a entrada de mão de obra estrangeira especializada na "
                      "área de eletrônica <u>contribuem para</u> deslocar — <u>para baixo e para a direita</u> — "
                      "a curva de oferta de longo prazo da indústria eletrônica."),
        "poucas": ("Mais trabalhadores especializados disponíveis barateiam um " + azb("insumo") + " da "
                   "indústria; custo menor = mais oferta a cada preço. Numa curva ascendente, deslocar para a "
                   "direita é o mesmo que deslocar para baixo."),
        "destrinchando": [
            "Determinantes da oferta (fora o preço do próprio bem): " + azb("preço dos insumos") + ", "
            "tecnologia, número de vendedores, expectativas, tributos e subsídios. A imigração facilitada amplia "
            "a oferta de trabalho especializado: o salário do setor tende a cair e/ou a produtividade a subir — "
            "nos dois casos, o custo por unidade produzida diminui.",
            "Por que “para baixo e para a direita” descrevem o mesmo movimento: a curva de oferta é ascendente. "
            "Ir para a direita = a <b>cada preço</b>, oferta-se mais; ir para baixo = <b>cada quantidade</b> "
            "passa a ser oferecida por um preço menor (o preço mínimo aceito pelo produtor reflete o custo "
            "marginal, que caiu).",
            "No longo prazo, a curva de oferta da indústria reflete os custos de entrada das firmas. Com custos "
            "menores, novas firmas entram e as existentes se expandem até o lucro econômico se anular a um preço "
            "mais baixo. Na indústria de " + azb("custos constantes") + " a oferta de longo prazo é horizontal "
            "e simplesmente desce; nas de custos crescentes, é ascendente e se desloca para baixo/direita.",
            "Contraponto: um choque que <b>encarece</b> insumos (restrição à imigração, alta de salários) "
            "desloca a oferta para cima e para a esquerda.",
            vm("Regra-âncora: oferta aumenta → direita = baixo; oferta diminui → esquerda = cima."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " A dupla “para baixo e para a direita” "
                       "parece contraditória para quem pensa que “aumentar” é sempre “subir”; com curva "
                       "ascendente, é a descrição exata de um aumento da oferta. O “contribuem para” e o "
                       "“longo prazo” deixam o item ainda mais seguro (não exigem efeito imediato)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…contribuem para deslocar — para cima e para a direita — a curva de oferta…”</i> → ERRADO "
            "(direção incoerente: oferta ascendente vai para a direita descendo)",
            "<i>“…contribuem para deslocar para a direita a curva de demanda por produtos eletrônicos.”</i> → "
            "ERRADO (curva trocada: o choque é de custo, logo de oferta)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["contribuem para"],
        "dificuldade": 2,
        "comentario_fonte": ("Mão de obra especializada mais disponível reduz o custo do insumo trabalho ou eleva "
                             "a produtividade, deslocando a oferta para a direita e para baixo. Comentários "
                             "empilhados; alguns afirmam que a oferta de longo prazo seria vertical ou que a "
                             "quantidade não mudaria."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [
            {"ref": "image.png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel"},
            {"ref": "image (29).png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel"}],
        "alertas": [ALERTA_2012],
    },
    # ------------------------------------------------------------------ E1-0010
    {
        "id": "ECO-E1-0010-1", "fonte_ref": "E1-0010", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DEM,
        "rotulo_item": "Item",
        "assertiva": ("Uma elevação do nível de renda da economia desloca a curva de demanda por um determinado "
                      "bem para a direita, indicando elevação da quantidade demandada mesmo sem uma alteração no "
                      "preço do produto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Uma elevação do nível de renda da economia desloca a curva de demanda por um "
                      "<u>determinado bem</u> para a direita, indicando elevação da quantidade demandada "
                      "<u>mesmo sem uma alteração no preço</u> do produto."),
        "poucas": ("Para um " + azb("bem normal") + ", mais renda desloca a demanda para a direita: compra-se "
                   "mais ao mesmo preço. O item vale tomando o caso típico; para um bem inferior, a curva iria "
                   "para a esquerda."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o item não diz que o bem é normal. Para um " + azb("bem inferior") + " (pão "
                          "dormido, transporte coletivo de baixa qualidade), o aumento de renda desloca a "
                          "demanda para a <b>esquerda</b>. O gabarito CERTO pressupõe o caso padrão; a leitura "
                          "mais rigorosa seria ERRADO pela generalização a “um determinado bem” qualquer.")],
        "destrinchando": [
            "A renda é um " + azb("determinante da demanda") + " que não está nos eixos (p × q): quando muda, a "
            "curva inteira se desloca. O sentido depende do tipo de bem, medido pela " + azb("elasticidade-renda")
            + " (η = %Δq / %ΔR).",
            vd("η > 0") + " → bem normal (renda ↑, demanda ↑, curva para a direita); dentro dele, " + vd("η > 1")
            + " → bem superior ou de luxo. " + vd("η < 0") + " → bem inferior (renda ↑, demanda ↓, curva para a "
            "esquerda). " + vd("η = 0") + " → bem de consumo saciado (sal).",
            "“Elevação da quantidade demandada mesmo sem alteração no preço” é a leitura do deslocamento: no "
            "mesmo preço p₀, o consumidor passa a comprar mais. Em rigor terminológico, o nome é “aumento da "
            "<b>demanda</b>”; “variação da quantidade demandada” se reserva ao movimento ao longo da curva, "
            "causado pelo preço do próprio bem.",
            "Na maioria dos itens, a banca trata o bem como normal quando não diz nada; quando quer cobrar o "
            "inferior, ela o menciona expressamente.",
        ],
        "dissecando": (cz("[detalhe · modulador relativo]") + " O item é verdadeiro no caso padrão (bem "
                       "normal) e usa “quantidade demandada” de modo frouxo; quem conhece a exceção do bem "
                       "inferior hesita. Em itens assim, a banca costuma considerar o caso típico, salvo se o "
                       "texto puxar a exceção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma elevação da renda desloca para a esquerda a curva de demanda por um bem inferior.”</i> → "
            "CERTO",
            "<i>“Uma elevação da renda desloca para a direita a curva de demanda por qualquer bem.”</i> → "
            "ERRADO (modulador absoluto: bens inferiores)",
        ])],
        "tipo_erro": ["DETALHE", "MODULADOR_RELATIVO"], "moduladores": ["determinado"], "dificuldade": 2,
        "comentario_fonte": ("Resposta de IA: certo para bem normal; para bem inferior, a curva se desloca para a "
                             "esquerda."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: o item não especifica bem normal; para bem inferior, o aumento de renda desloca "
                    "a demanda para a esquerda — mantido o CERTO da fonte",
                    "assertiva: retirada a duplicação “É correto afirmar que ‘É correto afirmar que…’” da frente "
                    "(formato de questionário próprio, data 04/22)"],
    },
    # ------------------------------------------------------------------ E1-0014
    {
        "id": "ECO-E1-0014-1", "fonte_ref": "E1-0014", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à teoria do consumidor e à lei da demanda.",
        "rotulo_item": "Item",
        "assertiva": ("A curva de demanda é descendente: de acordo com a teoria do consumidor, a curva de demanda "
                      "tem uma inclinação negativa, o que significa que, à medida que o preço de um bem aumenta, a "
                      "quantidade demandada por esse bem diminui. Essa relação inversa entre preço e quantidade "
                      "demandada é conhecida como Lei da Demanda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de demanda é descendente: de acordo com a teoria do consumidor, a curva de "
                      "demanda tem uma <u>inclinação negativa</u>, o que significa que, à medida que o preço de um "
                      "bem aumenta, a <u>quantidade demandada</u> por esse bem diminui. Essa relação inversa entre "
                      "preço e quantidade demandada é conhecida como Lei da Demanda."),
        "poucas": ("Definição de manual: " + azb("lei da demanda") + " = relação inversa entre o preço de um bem "
                   "e a quantidade demandada dele, <i>ceteris paribus</i>; por isso a curva é negativamente "
                   "inclinada."),
        "destrinchando": [
            "Por que a curva desce: quando o preço de um bem sobe, atuam dois efeitos. O " + azb("efeito "
            "substituição") + " (o bem fica relativamente mais caro, e o consumidor migra para substitutos) é "
            "<b>sempre</b> contrário ao preço. O " + azb("efeito renda") + " (o poder de compra cai) reduz o "
            "consumo se o bem for normal.",
            "Para um bem normal, os dois efeitos vão na mesma direção, e a lei vale com folga. Para um bem "
            "inferior, o efeito renda vai no sentido oposto, mas em regra é menor que o de substituição — a "
            "curva continua descendente.",
            "A exceção teórica é o " + azb("bem de Giffen") + ": inferior e com efeito renda tão forte que supera "
            "o de substituição; a curva fica positivamente inclinada. Outra exceção citada é o " + azb("bem de "
            "Veblen") + " (ostentação), cuja demanda pode subir com o preço por razões de status.",
            "Atenção ao vocabulário, que o item usa corretamente: a lei fala em <b>quantidade demandada</b> "
            "(movimento ao longo da curva), não em “demanda” (a curva inteira).",
        ],
        "dissecando": (cz("[literalidade]") + " Paráfrase direta do manual; não há armadilha no texto. O "
                       "risco é o candidato desconfiar por lembrar do bem de Giffen — mas o item descreve a regra "
                       "geral, sem dizer “sempre” ou “todos os bens”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A lei da demanda vale para todos os bens, sem exceção.”</i> → ERRADO (modulador absoluto: bem de "
            "Giffen)",
            "<i>“À medida que o preço de um bem aumenta, a demanda por esse bem se desloca para a esquerda.”</i> → "
            "ERRADO (troca de conceito: preço do próprio bem gera movimento ao longo da curva)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Só o gabarito (“CORRETO”), sem comentário.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0015
    {
        "id": "ECO-E1-0015-1", "fonte_ref": "E1-0015", "destino": "01", "subtema": H2["cpp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2003", "ano": 2003, "cacd": True,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo à curva de possibilidades de produção.",
        "rotulo_item": "Item",
        "assertiva": ("A recente retomada econômica nos Estados Unidos da América (EUA) contribuiu para reduzir os "
                      "níveis de desemprego naquele país. Como consequência, a curva de possibilidades de produção "
                      "da economia americana foi deslocada para cima e para a direita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A recente retomada econômica nos Estados Unidos da América (EUA) contribuiu para reduzir "
                       "os níveis de desemprego naquele país. Como consequência, a curva de possibilidades de "
                       "produção da economia americana ") + vm("foi deslocada para cima e para a direita")
                    + az(".")),
        "poucas": ("Reduzir o desemprego é usar recursos que <b>já existiam</b>: a economia sai de um "
                   + azb("ponto interior") + " e se aproxima da fronteira. A CPP só se desloca com mais fatores "
                   "ou melhor tecnologia."),
        "destrinchando": [
            "A " + azb("curva (fronteira) de possibilidades de produção") + " mostra as combinações "
            "<b>máximas</b> de dois bens que a economia consegue produzir com pleno emprego dos recursos e a "
            "tecnologia dada. Pontos sobre a curva são eficientes; pontos internos indicam " + azb("desemprego ou "
            "capacidade ociosa") + "; pontos externos são inatingíveis.",
            "Uma economia em recessão opera <b>dentro</b> da CPP. A retomada reocupa trabalhadores e máquinas "
            "parados: a produção cresce, mas o movimento é de dentro para a fronteira, sem mudar a fronteira.",
            "O que desloca a CPP para fora (" + azb("crescimento econômico") + " de longo prazo): aumento da "
            "quantidade de fatores (mais capital por investimento, mais força de trabalho, recursos naturais "
            "descobertos) ou " + azb("progresso técnico") + ". Catástrofes, guerras e emigração em massa a "
            "deslocam para dentro.",
            "Ligação com a macro: a retomada fecha o " + azb("hiato do produto") + " (produto efetivo → "
            "potencial); o deslocamento da CPP equivale a aumentar o próprio produto potencial.",
            vm("Regra-âncora: menos desemprego → o ponto vai até a curva; mais recursos ou tecnologia → a curva "
               "vai para fora."),
        ],
        "grafico_verso": "ECO-E1-0015-1-V1",
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " A primeira frase é um fato plausível "
                       "(retomada → menos desemprego); o erro está no “Como consequência”, que liga esse fato a "
                       "um deslocamento da fronteira. Confunde aproveitamento da capacidade com expansão da "
                       "capacidade. 🔥 Clássico do CACD: desemprego = ponto interior."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…Como consequência, a economia americana aproximou-se de sua curva de possibilidades de "
            "produção.”</i> → CERTO",
            "<i>“O aumento do estoque de capital, decorrente de novos investimentos, desloca a curva de "
            "possibilidades de produção para fora.”</i> → CERTO",
            "<i>“A redução do desemprego desloca a curva de possibilidades de produção para a direita.”</i> → "
            "ERRADO (nexo indevido: só muda o ponto)",
        ])],
        "reescrita": ("A recente retomada econômica nos Estados Unidos da América (EUA) contribuiu para reduzir os "
                      "níveis de desemprego naquele país. Como consequência, a " + hl("economia americana "
                      "aproximou-se de sua curva de possibilidades de produção, sem que esta se deslocasse")
                      + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A economia passou a usar fatores que estavam desempregados: saiu de um ponto interior "
                             "rumo à curva; a CPP só se desloca com aumento de fatores ou de tecnologia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "image (5).png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel (mecanismo redesenhado em ECO-E1-0015-1-V1)"},
            {"ref": "image (20).png", "tipo_fonte": "não preservada (GRÁFICO de CPP com pontos B, Y, Z)",
             "lado": "verso", "acao": "irrecuperavel (mecanismo redesenhado em ECO-E1-0015-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0016
    {
        "id": "ECO-E1-0016-1", "fonte_ref": "E1-0016", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2003", "ano": 2003, "cacd": True,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo ao conceito de custo de oportunidade.",
        "rotulo_item": "Item",
        "assertiva": ("Quando as datas do concurso de admissão à carreira de diplomata coincidem com aquelas do "
                      "concurso para assessor legislativo, o custo de oportunidade de fazer a segunda seleção "
                      "aumenta substancialmente para os candidatos que tencionam submeter-se aos dois certames."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando as datas do concurso de admissão à carreira de diplomata <u>coincidem</u> com "
                      "aquelas do concurso para assessor legislativo, o custo de oportunidade de fazer a segunda "
                      "seleção <u>aumenta substancialmente</u> para os candidatos que tencionam submeter-se aos "
                      "dois certames."),
        "poucas": ("Com datas coincidentes, fazer uma prova passa a significar <b>renunciar à outra</b>. O "
                   + azb("custo de oportunidade") + " de uma seleção inclui agora a perda da chance na outra — "
                   "por isso sobe muito."),
        "destrinchando": [
            azb("Custo de oportunidade") + " = valor da <b>melhor alternativa sacrificada</b> quando se faz uma "
            "escolha. Não é só o gasto em dinheiro: inclui tempo, esforço e as chances de que se abre mão.",
            "Com datas diferentes, fazer o concurso de assessor custa a inscrição, o deslocamento e algumas "
            "horas de estudo desviadas — um custo de oportunidade baixo. Com datas iguais, fazer o de assessor "
            "custa também a <b>chance de ingressar na carreira diplomática</b> naquele ano: o custo dá um salto.",
            "O exemplo mostra que o custo de oportunidade depende das <b>alternativas disponíveis</b>, não do "
            "bem em si: o mesmo concurso fica “mais caro” quando a melhor alternativa muda.",
            "É o segundo dos dez princípios de " + oc("Mankiw") + ": “o custo de alguma coisa é aquilo de que "
            "você desiste para obtê-la”. A escassez (de tempo, aqui) é que obriga à escolha.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de aplicação do conceito a um caso concreto, com tom "
                       "anedótico (a própria carreira de diplomata). A palavra “substancialmente” pode assustar, "
                       "mas é justificada: a alternativa perdida passa a ser uma prova inteira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o custo de oportunidade de fazer a segunda seleção não se altera, pois as taxas de inscrição "
            "são as mesmas.”</i> → ERRADO (custo de oportunidade não é só o desembolso monetário)",
            "<i>“Para quem só pretende prestar o concurso de diplomata, a coincidência de datas não eleva o custo "
            "de oportunidade dessa escolha.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["substancialmente"], "dificuldade": 1,
        "comentario_fonte": ("Quem quer prestar os dois concursos terá de escolher um e abrir mão do outro: o custo "
                             "de oportunidade é alto. Custo de oportunidade = valor da melhor alternativa "
                             "sacrificada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0018
    {
        "id": "ECO-E1-0018-1", "fonte_ref": "E1-0018", "destino": "01", "subtema": H2["ofe"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2003", "ano": 2003, "cacd": True,
        "errei": False,
        "comando": CMD_OFE,
        "rotulo_item": "Item",
        "assertiva": ("O pacote recente do governo brasileiro que injetou crédito de R$ 400 milhões para a compra "
                      "de eletrodomésticos deslocará a curva de demanda de eletroeletrônicos para cima e para a "
                      "direita, e a curva de oferta desses bens, para baixo e para a esquerda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O pacote recente do governo brasileiro que injetou crédito de R$ 400 milhões para a "
                       "compra de eletrodomésticos deslocará a curva de demanda de eletroeletrônicos para cima e "
                       "para a direita") + vm(", e a curva de oferta desses bens, para baixo e para a esquerda")
                    + az(".")),
        "poucas": ("O crédito ao consumidor desloca a " + azb("demanda") + " (direita/cima), mas não mexe nos "
                   "custos de produção: a " + azb("oferta") + " não se desloca. E “baixo e esquerda” nem "
                   "descreve um deslocamento possível de uma curva ascendente."),
        "destrinchando": [
            "Crédito para a compra de eletrodomésticos amplia o poder de compra dos consumidores a cada preço: "
            "funciona como aumento de renda disponível. A demanda se desloca para a direita — e, numa curva "
            "descendente, “direita” e “cima” são o mesmo movimento (o consumidor aceita pagar mais por cada "
            "quantidade). Essa parte do item está certa.",
            "A " + azb("curva de oferta") + " depende de custos (insumos, salários), tecnologia, número de "
            "produtores e tributos. Nada disso muda com crédito ao comprador. O que ocorre com a oferta é "
            + azb("movimento ao longo dela") + ": com a demanda maior, o preço sobe e os produtores ofertam "
            "mais (E₁ → E₂).",
            "Erro geométrico adicional: uma curva <b>ascendente</b> deslocada para baixo vai para a direita "
            "(aumento da oferta), e deslocada para a esquerda vai para cima (redução). “Para baixo e para a "
            "esquerda” combina metades de movimentos opostos.",
            "Leitura de longo prazo (fora do item): a expectativa de demanda maior pode atrair novas firmas e, "
            "aí sim, deslocar a oferta para a direita/baixo — nunca para a esquerda.",
        ],
        "grafico_verso": "ECO-E1-0018-1-V1",
        "dissecando": (cz("[meia-verdade · inversão]") + " A primeira metade (demanda) está correta e dá "
                       "confiança; o erro foi enxertado na segunda, que inventa um efeito na oferta e ainda "
                       "lhe dá uma direção geometricamente impossível. Pista: o pacote atua sobre o "
                       "comprador, não sobre o custo do vendedor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O pacote deslocará a curva de demanda de eletroeletrônicos para a direita, elevando o preço e a "
            "quantidade de equilíbrio, sem deslocar a curva de oferta.”</i> → CERTO",
            "<i>“Um subsídio aos fabricantes de eletrodomésticos deslocaria a curva de oferta para cima e para a "
            "esquerda.”</i> → ERRADO (inversão: subsídio ao produtor desloca a oferta para baixo e para a "
            "direita)",
        ])],
        "reescrita": ("O pacote recente do governo brasileiro que injetou crédito de R$ 400 milhões para a compra "
                      "de eletrodomésticos deslocará a curva de demanda de eletroeletrônicos para cima e para a "
                      "direita" + hl(", sem deslocar a curva de oferta desses bens, ao longo da qual o mercado se "
                      "moverá") + "."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Demanda correta (direita/cima); a oferta, dada pela estrutura de custos, não se "
                             "altera, e “baixo e esquerda” é incoerente com a inclinação positiva. Um dos "
                             "comentários defende que a oferta se ajustaria ao crediário, confundindo movimento "
                             "ao longo da curva com deslocamento."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [
            {"ref": "image (8).png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel"},
            {"ref": "image (26).png", "tipo_fonte": "não preservada (GRÁFICO: deslocamento só da demanda)",
             "lado": "verso", "acao": "irrecuperavel (mecanismo redesenhado em ECO-E1-0018-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0019
    {
        "id": "ECO-E1-0019-1", "fonte_ref": "E1-0019", "destino": "01", "subtema": H2["ofe"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2004", "ano": 2004, "cacd": True,
        "errei": False,
        "comando": CMD_OFE,
        "rotulo_item": "Item",
        "assertiva": ("A comercialização dos bilhetes das companhias aéreas, realizadas por via eletrônica, ao "
                      "reduzir os custos dessas empresas, desloca, para baixo e para direita, a curva de oferta de "
                      "passagens aéreas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A comercialização dos bilhetes das companhias aéreas, realizadas por via eletrônica, ao "
                      "<u>reduzir os custos</u> dessas empresas, desloca, <u>para baixo e para direita</u>, a curva "
                      "de oferta de passagens aéreas."),
        "poucas": ("Venda eletrônica corta custos (agências, comissões, emissão em papel). " + azb("Custo menor")
                   + " = oferta maior a cada preço = curva de oferta para a direita, que, sendo ascendente, "
                   "também desce."),
        "destrinchando": [
            "Entre os " + azb("determinantes da oferta") + " estão o preço dos insumos e a " + azb("tecnologia")
            + ". A venda on-line é inovação de processo: elimina intermediários e reduz o custo de colocar cada "
            "assento à venda.",
            "Duas leituras do mesmo deslocamento: <b>horizontal</b> — a cada preço, as companhias aceitam ofertar "
            "mais assentos (direita); <b>vertical</b> — cada quantidade passa a ser ofertada a um preço mínimo "
            "menor, porque o custo marginal caiu (baixo).",
            "Efeito no mercado, com demanda inalterada: " + vd("preço de equilíbrio ↓") + " e " + vd("quantidade "
            "↑") + " (E₁ → E₂). Note-se: o preço menor é <b>consequência</b> do deslocamento, e não sua causa — "
            "a curva desce porque o custo caiu.",
            "Choques opostos (alta do querosene de aviação, novos tributos) deslocam a oferta para cima e para a "
            "esquerda: preço ↑, quantidade ↓.",
            vm("Regra-âncora: custo ↓ ou tecnologia ↑ → oferta para a direita/baixo."),
        ],
        "grafico_verso": "ECO-E1-0019-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " Aplicação direta do determinante “custos”. O par “para baixo "
                       "e para a direita” é o mesmo que derruba candidatos em outros itens: para a oferta, que "
                       "sobe da esquerda para a direita, é a descrição correta de um aumento. 🔥 O CACD dos anos "
                       "2000 cobrava esse par em quase toda prova."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…desloca, para cima e para a esquerda, a curva de oferta de passagens aéreas.”</i> → ERRADO "
            "(sentido invertido: seria redução da oferta)",
            "<i>“…desloca, para a direita, a curva de demanda por passagens aéreas.”</i> → ERRADO (curva trocada: "
            "redução de custo atua na oferta)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Redução de custos aumenta a oferta: curva para a direita e para baixo. Um comentário "
                             "atribui o “para baixo” à redução do preço de equilíbrio (inverte causa e efeito); "
                             "outro trata apenas de deslocamentos da demanda."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [
            {"ref": "image (10).png", "tipo_fonte": "não preservada (provável GRÁFICO de slide)", "lado": "verso",
             "acao": "irrecuperavel"},
            {"ref": "image (28).png", "tipo_fonte": "não preservada (GRÁFICO: oferta de O para O')",
             "lado": "verso", "acao": "irrecuperavel (mecanismo redesenhado em ECO-E1-0019-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0029
    {
        "id": "ECO-E1-0029-1", "fonte_ref": "E1-0029", "destino": "01", "subtema": H2["cpp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2004", "ano": 2004, "cacd": True,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo à fronteira de possibilidades de produção.",
        "rotulo_item": "Item",
        "assertiva": ("A redução do imposto sobre operações financeiras (IOF), ao incentivar a poupança, contribui "
                      "para deslocar, para cima e para a direita, a fronteira de possibilidades de produção da "
                      "economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A redução do imposto sobre operações financeiras (IOF), ao incentivar a poupança, "
                      "<u>contribui para</u> deslocar, para cima e para a direita, a fronteira de possibilidades "
                      "de produção da economia."),
        "poucas": ("Cadeia: IOF ↓ → poupança ↑ → " + azb("investimento") + " ↑ → " + azb("estoque de capital")
                   + " ↑ → mais capacidade produtiva → a FPP se expande. O “contribui para” torna o item "
                   "seguro."),
        "destrinchando": [
            "A FPP se desloca para fora quando aumenta a <b>quantidade de fatores</b> ou melhora a tecnologia. "
            "O capital é fator de produção; ele cresce com o " + azb("investimento") + ", que é financiado pela "
            + azb("poupança") + " (na economia fechada, identidade " + vd("S = I") + ").",
            "O IOF incide sobre crédito, câmbio, seguros e operações com títulos e valores mobiliários. Reduzi-lo "
            "eleva o retorno líquido das aplicações e barateia a intermediação: na visão " + azb("neoclássica")
            + " dos fundos emprestáveis, mais poupança derruba os juros e estimula o investimento.",
            "Diferença em relação ao item do desemprego (CACD 2003): lá, a economia apenas se aproximava da "
            "fronteira usando recursos ociosos; aqui, cria-se capital novo, que <b>aumenta o potencial</b> — a "
            "fronteira se move.",
            "Ressalva teórica que não derruba o item: na leitura " + oc("keynesiana") + " (paradoxo da "
            "parcimônia), poupar mais pode reduzir a demanda e o investimento no curto prazo. Por isso a banca "
            "usa “contribui para”, e não “desloca necessariamente”.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Item de cadeia causal longa (imposto → "
                       "poupança → investimento → capital → FPP), em que cada elo é padrão de manual. O "
                       "“contribui para” protege o item de objeções de curto prazo; quem pensa só no curto prazo "
                       "(ou confunde com o caso do desemprego) marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução do IOF, ao incentivar o consumo das famílias, desloca a FPP para fora.”</i> → ERRADO "
            "(nexo indevido: consumo não acumula capital)",
            "<i>“A redução do IOF, ao incentivar a poupança, desloca necessariamente a FPP no curto prazo.”</i> → "
            "ERRADO (modulador absoluto: o efeito depende da conversão em investimento)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["contribui para"],
        "dificuldade": 2,
        "comentario_fonte": ("Redução do IOF amplia a poupança e, por S = I, o investimento e o capital; a "
                             "fronteira se desloca para fora. Comentários repetidos, com digressão sobre a "
                             "identidade poupança–investimento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "image (25).png", "tipo_fonte": "não preservada (provável GRÁFICO de FPP)", "lado": "verso",
             "acao": "irrecuperavel"},
            {"ref": "image (24).png", "tipo_fonte": "não preservada (GRÁFICO de FPP com pontos 1 a 7)",
             "lado": "verso", "acao": "irrecuperavel (descrição absorvida no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0030
    {
        "id": "ECO-E1-0030-1", "fonte_ref": "E1-0030", "destino": "01", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2004", "ano": 2004, "cacd": True,
        "errei": False,
        "comando": CMD_DEM,
        "rotulo_item": "Item",
        "assertiva": ("O recrudescimento, na Ásia, da gripe do frango, conhecida cientificamente como influenza "
                      "aviária, abre novos mercados para o produto brasileiro e desloca, para cima e para a "
                      "direita, a curva de demanda por carne de frango no Brasil."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O recrudescimento, na Ásia, da gripe do frango, conhecida cientificamente como influenza "
                      "aviária, abre novos mercados para o produto brasileiro e desloca, <u>para cima e para a "
                      "direita</u>, a curva de demanda por carne de frango no Brasil."),
        "poucas": ("A gripe derruba a oferta asiática; importadores buscam o " + azb("substituto") + " "
                   "brasileiro. Mais compradores (externos) a cada preço = " + azb("demanda") + " pelo frango "
                   "produzido no Brasil para a direita/cima."),
        "destrinchando": [
            "Determinantes da demanda que entram aqui: " + azb("número de compradores") + " (novos mercados "
            "externos) e " + azb("preço dos substitutos") + " (o frango asiático, escasso, encarece). Ambos "
            "deslocam a curva de demanda pelo frango brasileiro para a direita.",
            "Numa curva descendente, “para a direita” e “para cima” são o mesmo deslocamento: a cada preço, "
            "compra-se mais; para cada quantidade, aceita-se pagar mais.",
            "Efeito no mercado brasileiro: preço e quantidade de equilíbrio sobem, e os produtores respondem "
            "<b>ao longo</b> da curva de oferta. Contraponto que já caiu em prova: um surto de gripe aviária "
            "<b>no Brasil</b> faria o inverso — fechamento de mercados (demanda ↓) e abate de plantéis "
            "(oferta ↓).",
            "⏳ (out/2026) Leitura de " + rx("Brasil") + ": o país é desde a década de 2000 o maior exportador mundial de carne "
            "de frango; choques sanitários em concorrentes costumam abrir espaço às exportações brasileiras.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item testa se o candidato identifica que um "
                       "choque de <b>oferta</b> lá fora vira choque de <b>demanda</b> aqui. A expressão “no "
                       "Brasil” gera dúvida (consumo doméstico × demanda pelo produto brasileiro); a banca a usa "
                       "no sentido da demanda total enfrentada pelos produtores brasileiros, inclusive a externa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…desloca, para cima e para a esquerda, a curva de oferta de carne de frango no Brasil.”</i> → "
            "ERRADO (curva trocada: o choque, para o Brasil, é de demanda)",
            "<i>“…eleva o preço do frango no mercado brasileiro, com aumento da quantidade ofertada pelos "
            "produtores nacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A gripe na Ásia reduz a oferta asiática e direciona a demanda ao produto brasileiro: "
                             "a curva de demanda desloca-se para cima e para a direita. Inclui troca de mensagens "
                             "sobre “no Brasil” × “do Brasil”."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [
            {"ref": "image (32).png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel"},
            {"ref": "image (27).png", "tipo_fonte": "não preservada (provável GRÁFICO)", "lado": "verso",
             "acao": "irrecuperavel"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0031
    {
        "id": "ECO-E1-0031-1", "fonte_ref": "E1-0031", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": ("O mercado, apesar de ter falhas, é um mecanismo muito eficaz para resolver o problema de "
                      "alocação de recursos na sociedade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O mercado, <u>apesar de ter falhas</u>, é um mecanismo muito eficaz para resolver o "
                      "problema de alocação de recursos na sociedade."),
        "poucas": ("É a visão do manual: o " + azb("sistema de preços") + " coordena, de forma descentralizada, "
                   "o que, como e para quem produzir — com eficiência na maioria dos casos, mas com "
                   + azb("falhas de mercado") + " que justificam intervenção pontual."),
        "destrinchando": [
            "Os preços transmitem informação (escassez relativa) e incentivos (lucro, economia de custo): cada "
            "agente decide com base no próprio interesse, e o resultado agregado tende à alocação eficiente — a "
            "“" + azb("mão invisível") + "” de " + oc("Adam Smith") + ", formalizada pelo " + azb("primeiro "
            "teorema do bem-estar") + " (equilíbrio competitivo é eficiente no sentido de Pareto).",
            "As hipóteses do teorema nem sempre valem: " + azb("externalidades") + " (poluição), " + azb("bens "
            "públicos") + " (defesa), " + azb("poder de mercado") + " (monopólio) e " + azb("informação "
            "assimétrica") + " (seguros, crédito). São as falhas que o item admite.",
            "Daí o consenso de manual: mercado como regra, Estado para corrigir falhas e cuidar da distribuição. "
            "São os princípios 6 e 7 de " + oc("Mankiw") + ": “os mercados são geralmente uma boa "
            "maneira de organizar a atividade econômica”, e “os governos às vezes podem melhorar os resultados "
            "do mercado”.",
            "Eficiência não é equidade: o mercado pode alocar bem e, ainda assim, distribuir a renda de modo "
            "socialmente inaceitável.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " A concessão “apesar de ter falhas” "
                       "equilibra o elogio e torna o item defensável. Desconfie da versão que retira a "
                       "ressalva ou troca “muito eficaz” por “perfeito” ou “sempre eficiente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O mercado aloca os recursos de forma sempre eficiente, dispensando a intervenção do "
            "governo.”</i> → ERRADO (modulador absoluto: há falhas de mercado)",
            "<i>“A alocação eficiente pelo mercado garante distribuição equitativa da renda.”</i> → ERRADO (nexo "
            "indevido: eficiência ≠ equidade)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["apesar de", "muito"],
        "dificuldade": 1,
        "comentario_fonte": "Visão da microeconomia neoclássica: o mercado é eficaz na alocação, apesar das falhas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0032
    {
        "id": "ECO-E1-0032-1", "fonte_ref": "E1-0032", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": "A escassez de recursos não afetará uma sociedade se ela imprimir a sua própria moeda.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A escassez de recursos ") + vm("não afetará") + az(" uma sociedade ")
                    + vm("se ela imprimir a sua própria moeda") + az(".")),
        "poucas": ("Escassez é limite <b>físico</b> (terra, trabalho, capital, tecnologia). Moeda é só meio de "
                   "troca: imprimi-la não cria um grão de " + azb("recurso real") + "; com a produção dada, "
                   "gera " + azb("inflação") + "."),
        "destrinchando": [
            azb("Escassez") + " = recursos limitados diante de necessidades ilimitadas. É o problema que "
            "funda a economia (" + oc("Lionel Robbins") + ": ciência que estuda a relação entre fins e meios "
            "escassos de usos alternativos). Afeta qualquer sociedade, rica ou pobre, com qualquer regime "
            "monetário.",
            "A moeda é " + azb("meio de troca") + ", unidade de conta e reserva de valor — não é fator de "
            "produção. Mais papel-moeda sem mais bens significa mais moeda perseguindo a mesma produção: na "
            + azb("teoria quantitativa") + " (MV = PY), com V e Y dados, M ↑ → P ↑.",
            "No curto prazo, com recursos ociosos, a expansão monetária pode estimular a produção (visão "
            "keynesiana) — mas só porque põe para trabalhar recursos já existentes; não remove o limite da "
            "fronteira de possibilidades de produção.",
            "Exemplos históricos de emissão descontrolada (Alemanha de 1923, Zimbábue nos anos 2000) mostram o "
            "resultado: hiperinflação, não abundância.",
            vm("Regra-âncora: dinheiro não é riqueza real; a escassez é de bens e fatores."),
        ],
        "dissecando": (cz("[nexo indevido]") + " Liga duas coisas sem relação causal (emissão de moeda e fim da "
                       "escassez). A pista é a confusão entre riqueza nominal e real — erro que a banca "
                       "explora também em itens sobre senhoriagem e “financiar o déficit com emissão”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A escassez de recursos afeta todas as sociedades, independentemente de seu nível de renda ou de "
            "seu regime monetário.”</i> → CERTO",
            "<i>“A emissão de moeda, com o produto no pleno emprego, tende a elevar o nível de preços.”</i> → "
            "CERTO",
        ])],
        "reescrita": ("A escassez de recursos " + hl("afetará") + " uma sociedade " + hl("ainda que") + " ela "
                      "imprima a sua própria moeda."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["se"], "dificuldade": 1,
        "comentario_fonte": "Escassez está ligada à limitação física dos recursos, não à quantidade de moeda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0033
    {
        "id": "ECO-E1-0033-1", "fonte_ref": "E1-0033", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": ("As intervenções do governo na sociedade devem, segundo a microeconomia neoclássica, pautar-se "
                      "pela preocupação de escolher o melhor para os cidadãos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As intervenções do governo na sociedade devem, segundo a microeconomia neoclássica, "
                       "pautar-se pela preocupação de ") + vm("escolher o melhor para os cidadãos") + az(".")),
        "poucas": ("Na microeconomia neoclássica, quem escolhe é o " + azb("indivíduo") + " (soberania do "
                   "consumidor). O governo intervém para " + azb("corrigir falhas de mercado") + ", não para "
                   "decidir no lugar do cidadão o que é melhor para ele."),
        "destrinchando": [
            "O ponto de partida neoclássico é o " + azb("individualismo metodológico") + ": cada agente conhece "
            "suas preferências e é o melhor juiz do próprio bem-estar. O bem-estar social é avaliado a partir "
            "das utilidades individuais (critério de " + oc("Pareto") + ").",
            "Por isso a intervenção legítima é <b>corretiva</b>: internalizar " + azb("externalidades")
            + " (tributo de " + oc("Pigou") + "), prover " + azb("bens públicos") + ", regular "
            + azb("monopólios") + ", reduzir " + azb("assimetrias de informação") + " — sempre para que as "
            "escolhas individuais levem a resultados eficientes, não para substituí-las.",
            "A ideia de um governo que “escolhe o melhor para os cidadãos” é " + azb("paternalismo") + ": "
            "aparece, por exemplo, nos " + azb("bens de mérito") + " de " + oc("Musgrave") + " (educação "
            "obrigatória, proibição de drogas), tratados como exceção justamente por contrariarem a soberania "
            "do consumidor.",
            "A justificativa da fonte (“a escola defende menor intervenção”) é incompleta: o problema do item "
            "não é a <b>quantidade</b> de intervenção, mas o <b>critério</b> — eficiência a partir das "
            "preferências individuais, não um “melhor” definido pelo Estado.",
        ],
        "dissecando": (cz("[troca de conceito · juízo indevido]") + " A frase soa virtuosa (“escolher o melhor "
                       "para os cidadãos”), e é aí que mora a armadilha: atribui à escola neoclássica um critério "
                       "paternalista. Itens que invocam uma escola costumam testar a <b>premissa</b> dela."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a microeconomia neoclássica, a intervenção do governo justifica-se para corrigir falhas "
            "de mercado, como externalidades e bens públicos.”</i> → CERTO",
            "<i>“Segundo a microeconomia neoclássica, o governo nunca deve intervir na economia.”</i> → ERRADO "
            "(modulador absoluto: admite intervenção corretiva)",
        ])],
        "reescrita": ("As intervenções do governo na sociedade devem, segundo a microeconomia neoclássica, pautar-se "
                      "pela preocupação de " + hl("corrigir falhas de mercado, respeitando as escolhas dos próprios "
                      "cidadãos") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "JUIZO_INDEVIDO"], "moduladores": ["devem"], "dificuldade": 2,
        "comentario_fonte": "A microeconomia neoclássica defende menor intervenção estatal.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a justificativa da fonte (menor intervenção) foi trocada pelo critério da "
                    "soberania do consumidor e da intervenção corretiva"],
    },
    # ------------------------------------------------------------------ E1-0034
    {
        "id": "ECO-E1-0034-1", "fonte_ref": "E1-0034", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": "A distribuição do produto nacional é parte central do problema econômico.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A <u>distribuição</u> do produto nacional é parte central do problema econômico."),
        "poucas": ("O " + azb("problema econômico") + " fundamental desdobra-se em três perguntas: o que "
                   "produzir, como produzir e " + azb("para quem produzir") + " — esta última é exatamente a "
                   "distribuição do produto."),
        "destrinchando": [
            "Toda sociedade, diante da " + azb("escassez") + ", precisa responder: <b>o que</b> e quanto "
            "produzir (composição do produto); <b>como</b> produzir (técnicas e combinação de fatores); e "
            "<b>para quem</b> produzir (como o produto se reparte entre as pessoas).",
            "A distribuição se faz, na economia de mercado, pela remuneração dos fatores — salários, juros, "
            "aluguéis e lucros — e é corrigida por tributos e transferências do Estado. Em economias "
            "centralmente planificadas, o plano define as três respostas.",
            "Na tradição clássica, a distribuição era o centro da disciplina: " + oc("David Ricardo") + " "
            "afirmava, no prefácio dos <i>Princípios</i> (1817), que determinar as leis que regulam a "
            "distribuição entre proprietários, capitalistas e trabalhadores é o “principal problema da Economia "
            "Política”.",
            "Para o " + rx("Brasil") + ", o tema é central no debate de desenvolvimento: alta concentração de "
            "renda, medida pelo " + azb("índice de Gini") + ", e o papel das transferências e da tributação na "
            "redução da desigualdade.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz um dos três problemas fundamentais (“para quem "
                       "produzir”) com outro nome — “distribuição do produto nacional”. Quem não liga os dois "
                       "rótulos pode achar que distribuição é tema de política social, e não de economia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O problema econômico restringe-se a decidir o que produzir e como produzir, sendo a distribuição "
            "questão estranha à ciência econômica.”</i> → ERRADO (restrição indevida: falta o “para quem”)",
            "<i>“Em economias de mercado, a distribuição do produto resulta da remuneração dos fatores de "
            "produção.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Distribuição é um dos aspectos fundamentais do problema econômico.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0035
    {
        "id": "ECO-E1-0035-1", "fonte_ref": "E1-0035", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": "A economia estuda a forma pela qual uma sociedade organiza a sua produção.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A economia estuda a forma pela qual uma sociedade <u>organiza a sua produção</u>."),
        "poucas": ("A " + azb("ciência econômica") + " estuda como a sociedade administra recursos escassos para "
                   "produzir bens e serviços e distribuí-los; a organização da produção é parte central desse "
                   "objeto."),
        "destrinchando": [
            "Definições de manual: economia é o estudo de como a sociedade administra seus " + azb("recursos "
            "escassos") + " (" + oc("Mankiw") + "); ou de como as sociedades utilizam recursos escassos para "
            "produzir bens valiosos e distribuí-los entre pessoas (" + oc("Samuelson") + " e Nordhaus).",
            "“Organizar a produção” responde às perguntas <b>o que</b> e <b>como</b> produzir: que bens, com que "
            "técnica, com que combinação de trabalho, capital e recursos naturais. A terceira pergunta (<b>para "
            "quem</b>) trata da distribuição.",
            "As formas de organização variam: " + azb("economia de mercado") + " (decisões descentralizadas, "
            "coordenadas por preços), " + azb("economia planificada") + " (decisões centralizadas no Estado) e, "
            "na prática, " + azb("economias mistas") + ".",
            "O item não diz que a economia estuda <b>só</b> a produção — por isso é verdadeiro. A ciência também "
            "estuda consumo, distribuição, moeda, comércio e crescimento.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição básica, sem modulador. Uma versão ERRADA típica "
                       "acrescentaria “exclusivamente” ou trocaria “organiza a produção” por algo alheio, como "
                       "“estuda a formação dos preços políticos”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A economia estuda exclusivamente a forma pela qual uma sociedade organiza a sua produção.”</i> → "
            "ERRADO (modulador absoluto: também distribuição e consumo)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "É um dos objetivos centrais da ciência econômica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0036
    {
        "id": "ECO-E1-0036-1", "fonte_ref": "E1-0036", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": "Os governos são dispensáveis como mecanismo de maximização do bem-estar social.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os governos ") + vm("são dispensáveis") + az(" como mecanismo de maximização do "
                                                                     "bem-estar social.")),
        "poucas": ("Quando há " + azb("falhas de mercado") + " (externalidades, bens públicos, monopólio, "
                   "informação assimétrica) ou problemas de " + azb("distribuição") + ", o mercado sozinho não "
                   "maximiza o bem-estar: o governo pode melhorar o resultado."),
        "destrinchando": [
            "O " + azb("primeiro teorema do bem-estar") + " diz que o equilíbrio competitivo é eficiente — mas "
            "só sob hipóteses fortes: concorrência perfeita, informação completa, ausência de externalidades e "
            "mercados para todos os bens. Fora delas, o mercado falha.",
            "Exemplos em que o governo é necessário: " + azb("bens públicos") + " (não rivais e não excludentes "
            "— defesa, iluminação pública) não seriam ofertados pelo mercado; " + azb("externalidades") + " "
            "(poluição) pedem tributo, regulação ou mercado de licenças; " + azb("monopólios naturais") + " "
            "pedem regulação; " + azb("assimetrias de informação") + " pedem normas e supervisão.",
            "Além da eficiência, a " + azb("equidade") + ": o mercado pode chegar a um ótimo de Pareto com "
            "distribuição muito desigual. O " + azb("segundo teorema do bem-estar") + " mostra que, com "
            "redistribuição prévia de dotações, outro equilíbrio eficiente e mais justo é alcançável.",
            "Ressalva: existem também " + azb("falhas de governo") + " (captura, busca de renda, informação "
            "limitada). Por isso o consenso é que o governo <b>pode</b> melhorar os resultados, não que sempre "
            "melhore.",
        ],
        "dissecando": (cz("[juízo indevido · modulador absoluto]") + " Afirmação categórica de cunho "
                       "ideológico, sem ressalva. “Dispensáveis” equivale a “nunca necessários”: basta um "
                       "contraexemplo (bem público, externalidade) para derrubar o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os governos podem melhorar os resultados do mercado quando há externalidades ou bens "
            "públicos.”</i> → CERTO",
            "<i>“A intervenção do governo sempre eleva o bem-estar social.”</i> → ERRADO (modulador absoluto: há "
            "falhas de governo)",
        ])],
        "reescrita": ("Os governos " + hl("não são dispensáveis") + " como mecanismo de maximização do bem-estar "
                      "social" + hl(", sobretudo diante de falhas de mercado") + "."),
        "tipo_erro": ["JUIZO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["dispensáveis"], "dificuldade": 1,
        "comentario_fonte": "O governo pode ser necessário para corrigir falhas de mercado.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0037
    {
        "id": "ECO-E1-0037-1", "fonte_ref": "E1-0037", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": "Todas as decisões individuais, em geral, enfrentam custos de oportunidade.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Todas</u> as decisões individuais, em geral, enfrentam custos de oportunidade."),
        "poucas": ("Toda escolha, sob " + azb("escassez") + " (de dinheiro, tempo ou atenção), implica renunciar "
                   "a alguma alternativa; o valor da melhor delas é o " + azb("custo de oportunidade") + "."),
        "destrinchando": [
            azb("Custo de oportunidade") + " = valor da melhor alternativa sacrificada. Como os recursos são "
            "limitados, escolher A é deixar de escolher B: não há decisão sem renúncia.",
            "Vale para recursos não monetários: ler um livro custa as horas que poderiam ser de trabalho ou "
            "descanso; cursar uma faculdade custa a mensalidade <b>e</b> o salário que se deixa de ganhar "
            "(muitas vezes o maior componente).",
            "Liga-se aos princípios de " + oc("Mankiw") + ": “as pessoas enfrentam " + azb("trade-offs") + "” "
            "(1º) e “o custo de alguma coisa é aquilo de que se desiste para obtê-la” (2º). O mesmo raciocínio "
            "explica a FPP (custo de oportunidade crescente) e a vantagem comparativa de " + oc("Ricardo") + ".",
            "Caso-limite: um bem livre (ar respirável, em geral) não tem custo de oportunidade para quem o usa. "
            "Por isso o item diz “em geral”.",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " Aqui “todas” vem amortecido por “em "
                       "geral” — combinação estranha, mas que torna o item seguro. Não marque ERRADO "
                       "automaticamente diante de “todas”: no custo de oportunidade, a generalização é a "
                       "própria regra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Decisões que não envolvem gasto monetário não têm custo de oportunidade.”</i> → ERRADO (troca de "
            "conceito: o tempo também é recurso escasso)",
            "<i>“O custo de oportunidade de cursar uma faculdade inclui a renda que o estudante deixa de "
            "auferir.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["todas", "em geral"], "dificuldade": 1,
        "comentario_fonte": "Toda escolha implica abrir mão de outra alternativa.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0038
    {
        "id": "ECO-E1-0038-1", "fonte_ref": "E1-0038", "destino": "01", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_BENS,
        "rotulo_item": "Item",
        "assertiva": "Os bens econômicos são de livre acesso a todos os agentes econômicos.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os bens econômicos ") + vm("são de livre acesso a todos os agentes econômicos") + az(".")),
        "poucas": ("Livre acesso é característica dos " + azb("bens livres") + " (abundantes, sem preço). "
                   + azb("Bens econômicos") + " são escassos, têm preço e exigem esforço ou pagamento para "
                   "serem obtidos."),
        "destrinchando": [
            "Classificação básica quanto à escassez: " + azb("bens livres") + " existem em quantidade "
            "ilimitada em relação à necessidade (ar, luz solar) — não têm preço nem custo de oportunidade; "
            + azb("bens econômicos") + " são relativamente escassos, demandam trabalho para serem produzidos e, "
            "por isso, têm preço.",
            "A condição de livre ou econômico depende do contexto: a água de um rio na Amazônia é praticamente "
            "livre; a água tratada numa metrópole é bem econômico. O ar limpo, com a poluição, tornou-se escasso "
            "em muitas cidades.",
            "Não confundir com a classificação de " + azb("bens públicos") + " (não rivais e não excludentes): "
            "um bem público, como a defesa nacional, é bem econômico (custa recursos) mesmo que ninguém possa ser "
            "excluído de usá-lo.",
            vm("Regra-âncora: bem econômico = escasso + útil + com preço; bem livre = abundante e gratuito."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui aos bens econômicos a característica que define "
                       "o grupo oposto (bens livres). O “todos os agentes” acentua a generalização."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os bens livres são abundantes e, por isso, não possuem preço.”</i> → CERTO",
            "<i>“Bens públicos não são bens econômicos, pois ninguém pode ser excluído de seu consumo.”</i> → "
            "ERRADO (troca de conceito: não exclusão ≠ abundância)",
        ])],
        "reescrita": ("Os bens " + hl("livres") + " são de livre acesso a todos os agentes econômicos" + hl("; "
                      "os econômicos são escassos e têm preço") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["todos"], "dificuldade": 1,
        "comentario_fonte": "Bens econômicos são escassos, não de livre acesso.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0039
    {
        "id": "ECO-E1-0039-1", "fonte_ref": "E1-0039", "destino": "01", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_BENS,
        "rotulo_item": "Item",
        "assertiva": ("Os bens econômicos são destituídos de atribuição de valor por parte dos agentes "
                      "econômicos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os bens econômicos ") + vm("são destituídos de atribuição de valor") + az(" por parte "
                                                                                                 "dos agentes "
                                                                                                 "econômicos.")),
        "poucas": ("É o contrário: bens econômicos são " + azb("úteis e escassos") + ", e é justamente essa "
                   "combinação que faz os agentes lhes atribuírem " + azb("valor") + " — expresso no preço."),
        "destrinchando": [
            "Um bem econômico reúne duas condições: " + azb("utilidade") + " (satisfaz alguma necessidade) e "
            + azb("escassez relativa") + ". Sem utilidade, ninguém o deseja; sem escassez, ninguém paga por ele "
            "(bem livre).",
            "O " + azb("paradoxo da água e do diamante") + " (" + oc("Adam Smith") + ") ilustra a distinção: a "
            "água tem enorme valor de uso e baixo valor de troca; o diamante, o contrário. A solução veio com a "
            + azb("revolução marginalista") + " (" + oc("Jevons") + ", " + oc("Menger") + " e " + oc("Walras")
            + ", anos 1870): o preço reflete a " + azb("utilidade marginal") + ", que é baixa para o que é "
            "abundante e alta para o que é escasso.",
            "Nas teorias clássicas do " + azb("valor-trabalho") + " (" + oc("Ricardo") + ", " + oc("Marx")
            + "), o valor vem do trabalho incorporado; nas neoclássicas, da utilidade e da escassez. Em ambas, "
            "bens econômicos <b>têm</b> valor.",
        ],
        "dissecando": (cz("[inversão]") + " Nega a propriedade definidora do conceito. O jargão “destituídos "
                       "de atribuição de valor” é rebuscado para disfarçar uma afirmação simplesmente oposta à "
                       "definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O valor atribuído aos bens econômicos decorre de sua utilidade e de sua escassez "
            "relativa.”</i> → CERTO",
            "<i>“Na teoria marginalista, o preço de um bem é determinado por sua utilidade total.”</i> → ERRADO "
            "(troca de conceito: é a utilidade marginal)",
        ])],
        "reescrita": ("Os bens econômicos " + hl("recebem") + " atribuição de valor por parte dos agentes "
                      "econômicos" + hl(", por serem úteis e escassos") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Bens econômicos possuem valor atribuído justamente por serem escassos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0040
    {
        "id": "ECO-E1-0040-1", "fonte_ref": "E1-0040", "destino": "01", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_BENS,
        "rotulo_item": "Item",
        "assertiva": "Quanto à sua função, os bens econômicos são caracterizados como finais ou intermediários.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Quanto à sua função</u>, os bens econômicos são caracterizados como finais ou "
                      "intermediários."),
        "poucas": ("Pela função (ou destino) no processo econômico, o bem é " + azb("final") + " (vendido ao "
                   "usuário final: consumo ou investimento) ou " + azb("intermediário") + " (insumo, "
                   "transformado ou consumido em outra etapa da produção)."),
        "destrinchando": [
            azb("Bens intermediários") + " são incorporados ou gastos na produção de outros bens dentro do "
            "período: trigo para o moinho, aço para a montadora, energia para a fábrica.",
            azb("Bens finais") + " chegam ao destino final: " + azb("bens de consumo") + " (duráveis e não "
            "duráveis, usados pelas famílias) e " + azb("bens de capital") + " (máquinas, equipamentos, "
            "edificações — usados na produção, mas <b>não</b> se esgotam nela; por isso entram como "
            "investimento, e não como insumo).",
            "A distinção importa nas " + azb("contas nacionais") + ": o PIB soma só os bens e serviços finais "
            "(ou o valor adicionado de cada etapa), para evitar a " + azb("dupla contagem") + " dos "
            "intermediários.",
            "O mesmo bem muda de classe conforme o uso: o açúcar comprado pela família é final; o comprado pela "
            "padaria é intermediário. O critério é a função, não a natureza física.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz uma classificação de manual. Atenção ao critério "
                       "citado: “quanto à função” leva a final × intermediário; “quanto à escassez”, a livre × "
                       "econômico; “quanto à relação com a renda”, a normal × inferior. A banca troca os "
                       "critérios para fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto à sua função, os bens econômicos são classificados como livres ou econômicos.”</i> → "
            "ERRADO (critério trocado: essa classificação é quanto à escassez)",
            "<i>“Uma máquina adquirida por uma fábrica é bem intermediário.”</i> → ERRADO (troca de conceito: é "
            "bem de capital, um bem final)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Essa é uma classificação aceita na economia.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0041
    {
        "id": "ECO-E1-0041-1", "fonte_ref": "E1-0041", "destino": "01", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_BENS,
        "rotulo_item": "Item",
        "assertiva": ("Os bens econômicos são chamados de bens de consumo quando participam do processo de "
                      "produção de novos bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os bens econômicos são chamados de ") + vm("bens de consumo") + az(" quando participam "
                                                                                          "do processo de "
                                                                                          "produção de novos "
                                                                                          "bens.")),
        "poucas": ("Bens que participam da produção de outros bens são " + azb("bens de produção") + " (de "
                   "capital ou intermediários). " + azb("Bens de consumo") + " satisfazem diretamente as "
                   "necessidades das famílias."),
        "destrinchando": [
            azb("Bens de consumo") + " destinam-se ao usuário final: " + azb("não duráveis") + " (alimentos, "
            "combustível do carro particular) e " + azb("duráveis") + " (geladeira, automóvel da família).",
            azb("Bens de produção") + " servem para produzir outros bens: " + azb("bens de capital") + " "
            "(máquinas, equipamentos, instalações — duram vários ciclos produtivos) e " + azb("bens "
            "intermediários") + " (matérias-primas e insumos, consumidos ou transformados no processo).",
            "Mais uma vez, o critério é o uso: um computador comprado por uma família é bem de consumo durável; o "
            "mesmo computador comprado por um escritório é bem de capital.",
            "Nas contas nacionais, a compra de bens de capital pelas empresas entra como " + azb("formação bruta "
            "de capital fixo") + " (investimento); a compra de bens de consumo pelas famílias, como consumo.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Mantém a definição correta de bens de produção e lhe cola "
                       "o rótulo errado (“bens de consumo”). Pista: “participam do processo de produção” é "
                       "definição de insumo ou capital."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os bens econômicos são chamados de bens de capital quando participam do processo de produção "
            "de novos bens sem se esgotarem nele.”</i> → CERTO",
            "<i>“Um automóvel é sempre bem de consumo durável.”</i> → ERRADO (modulador absoluto: se usado por "
            "uma empresa de táxi, é bem de capital)",
        ])],
        "reescrita": ("Os bens econômicos são chamados de " + hl("bens de produção") + " quando participam do "
                      "processo de produção de novos bens."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Bens de consumo não participam da produção de novos bens; isso é função dos bens de "
                             "produção."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0042
    {
        "id": "ECO-E1-0042-1", "fonte_ref": "E1-0042", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": ("O trade off é entendido como termo que define uma situação de escolha conflitante, ou seja, "
                      "quando uma ação econômica, visando à resolução de determinado problema acarreta, "
                      "inevitavelmente, outros problemas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O trade off é entendido como termo que define uma situação de <u>escolha conflitante</u>, "
                      "ou seja, quando uma ação econômica, visando à resolução de determinado problema acarreta, "
                      "<u>inevitavelmente</u>, outros problemas."),
        "poucas": (azb("Trade-off") + " = escolha conflitante: obter mais de uma coisa exige abrir mão de outra. "
                   "Resolver um problema gera, inevitavelmente, um custo em outra frente."),
        "destrinchando": [
            "O termo vem do inglês (<i>to trade off</i>, “trocar uma coisa por outra”) e é o primeiro princípio "
            "de " + oc("Mankiw") + ": “as pessoas enfrentam trade-offs”. A raiz é a " + azb("escassez") + ": "
            "com recursos limitados, mais de A implica menos de B.",
            "Exemplos clássicos: " + azb("“canhões ou manteiga”") + " (defesa × consumo); " + azb("eficiência × "
            "equidade") + " (redistribuir pode reduzir incentivos); " + azb("inflação × desemprego") + " no curto "
            "prazo (curva de Phillips); meio ambiente × renda.",
            "O trade-off é a situação; o " + azb("custo de oportunidade") + " é a medida do que se renuncia nela. "
            "Graficamente, a FPP é o desenho do trade-off, e sua inclinação mede o custo de oportunidade.",
            "O “inevitavelmente” é coerente com o conceito: se a ação não gerasse custo em outra frente, não "
            "haveria trade-off — haveria um ganho sem perda (algo possível só fora da fronteira, com recursos "
            "ociosos).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição correta em linguagem mais solta (“acarreta outros "
                       "problemas”). O “inevitavelmente” pode parecer modulador absoluto, mas é da essência do "
                       "conceito: toda escolha sob escassez tem custo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O trade-off implica um custo de oportunidade.”</i> → CERTO",
            "<i>“Em uma economia com recursos ociosos, o aumento da produção de um bem exige, necessariamente, a "
            "redução da produção de outro.”</i> → ERRADO (modulador absoluto: dentro da FPP é possível produzir "
            "mais dos dois)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["inevitavelmente"], "dificuldade": 1,
        "comentario_fonte": "O trade-off envolve escolha conflitante, implicando custo de oportunidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0043
    {
        "id": "ECO-E1-0043-1", "fonte_ref": "E1-0043", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": ("O custo de oportunidade é aquilo que o agente econômico deve ter de recompensa para abrir mão "
                      "de algum consumo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O custo de oportunidade é ") + vm("aquilo que o agente econômico deve ter de recompensa "
                                                          "para abrir mão de algum consumo") + az(".")),
        "poucas": ("Custo de oportunidade é o " + azb("valor da melhor alternativa sacrificada") + ", não uma "
                   "recompensa a receber. A ideia de “prêmio para abrir mão do consumo” descreve os " + azb("juros")
                   + " (remuneração da poupança)."),
        "destrinchando": [
            azb("Custo de oportunidade") + ": ao escolher A, o que se perde é o benefício da melhor opção não "
            "escolhida, B. Ex.: o custo de oportunidade de manter R$ 1.000 parados em casa é o rendimento que "
            "eles teriam numa aplicação.",
            "O item descreve outra coisa: a compensação exigida para adiar o consumo. É a lógica da "
            + azb("taxa de juros") + " como prêmio pela espera (" + oc("Böhm-Bawerk") + ", " + oc("Fisher")
            + ") ou da " + azb("taxa de preferência intertemporal") + ". Na visão de " + oc("Keynes") + ", o juro "
            "é o prêmio pela renúncia à " + azb("liquidez") + ", e não ao consumo.",
            "Há parentesco entre as ideias (a recompensa exigida costuma igualar o custo de oportunidade na "
            "margem), mas os conceitos não se confundem: um é o que se <b>perde</b>; o outro, o que se "
            "<b>exige receber</b>.",
            vm("Regra-âncora: custo de oportunidade = melhor alternativa renunciada."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca a definição de custo de oportunidade pela de "
                       "remuneração da espera (juros). A frase soa econômica e “plausível”; a pista é a palavra "
                       "“recompensa”, que não faz parte da definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O custo de oportunidade corresponde ao valor da melhor alternativa sacrificada em uma "
            "escolha.”</i> → CERTO",
            "<i>“O custo de oportunidade de uma escolha corresponde à soma de todas as alternativas "
            "renunciadas.”</i> → ERRADO (dado alterado: só a melhor delas)",
        ])],
        "reescrita": ("O custo de oportunidade é " + hl("o valor da melhor alternativa de que o agente econômico "
                      "abre mão ao fazer uma escolha") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "O custo de oportunidade é o valor do melhor uso alternativo dos recursos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0044
    {
        "id": "ECO-E1-0044-1", "fonte_ref": "E1-0044", "destino": "01", "subtema": H2["fund"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUND,
        "rotulo_item": "Item",
        "assertiva": ("A mudança marginal, pequeno ajuste incremental em um plano de ação, não é revestida de "
                      "racionalidade econômica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A mudança marginal, pequeno ajuste incremental em um plano de ação, ") + vm("não é")
                    + az(" revestida de racionalidade econômica.")),
        "poucas": ("“" + azb("Pessoas racionais pensam na margem") + "”: decidir por mudanças marginais — "
                   "comparando " + azb("benefício marginal") + " e " + azb("custo marginal") + " — é a própria "
                   "essência da racionalidade econômica."),
        "destrinchando": [
            "A definição do item está certa: " + azb("mudança marginal") + " é um pequeno ajuste incremental num "
            "plano (estudar uma hora a mais, produzir uma unidade a mais). O erro está em negar que ela tenha "
            "racionalidade.",
            "Regra de decisão: o agente racional amplia uma atividade enquanto o " + vd("benefício marginal > "
            "custo marginal") + " e para quando " + vd("BMg = CMg") + ". É o 3º princípio de " + oc("Mankiw")
            + ". Daí derivam as condições de ótimo da micro: a firma produz até " + vd("RMg = CMg") + "; o "
            "consumidor iguala a utilidade marginal por real gasto em todos os bens.",
            "A ideia vem da " + azb("revolução marginalista") + " (" + oc("Jevons") + ", " + oc("Menger") + ", "
            + oc("Walras") + ", anos 1870) e foi sistematizada por " + oc("Alfred Marshall") + " (<i>Princípios "
            "de Economia</i>, 1890).",
            "Exemplo clássico: uma companhia aérea com assentos vazios aceita vender um bilhete abaixo do custo "
            "<b>médio</b> se o preço superar o custo <b>marginal</b> de levar mais um passageiro.",
        ],
        "dissecando": (cz("[inversão]") + " A primeira metade (definição de mudança marginal) é correta e dá "
                       "credibilidade; o erro está no “não”, que inverte o princípio. Itens de fundamentos "
                       "costumam reproduzir os princípios de Mankiw e negar um deles."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um agente racional só realiza uma ação se o benefício marginal for maior ou igual ao custo "
            "marginal.”</i> → CERTO",
            "<i>“A decisão racional exige comparar o benefício total com o custo total de cada nova unidade.”</i> "
            "→ ERRADO (troca de conceito: compara-se o marginal)",
        ])],
        "reescrita": ("A mudança marginal, pequeno ajuste incremental em um plano de ação, " + hl("é")
                      + " revestida de racionalidade econômica."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": "Mudança marginal é um pequeno ajuste incremental que considera racionalidade econômica.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
