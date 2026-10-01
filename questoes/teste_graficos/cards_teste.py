"""Fonte dos cards do teste de gráficos (00-TESTE-GRAF-1 - Obj.).

Cada card é um dict; montar_nota_q.py compõe frente e verso na ordem da Folha -Q
e grava o JSONL, o HTML e o ENEX. Os gráficos estão em specs/ (uma spec por figura).
"""

# ---- atalhos de marcação (Folha v9 §5.1 / Folha -Q §3.2)
def az(t):  # trecho correto da assertiva anotada (azul, sem negrito)
    return f'<span style="color: rgb(0, 60, 200);">{t}</span>'


def vm(t):  # trecho errado da assertiva anotada / regra decisiva
    return f'<span style="color: rgb(200, 0, 0);"><b>{t}</b></span>'


def azb(t):  # conceito
    return f'<span style="color: rgb(0, 60, 200);"><b>{t}</b></span>'


def vd(t):  # dado, número, CERTO
    return f'<span style="color: rgb(0, 130, 0);"><b>{t}</b></span>'


def oc(t):  # autor
    return f'<span style="color: rgb(170, 85, 0);"><b>{t}</b></span>'


def rx(t):  # Brasil
    return f'<span style="color: rgb(130, 0, 160);"><b>{t}</b></span>'


def cz(t):  # meta / taxonomia
    return f'<span style="color: rgb(160, 160, 160);">{t}</span>'


def hl(t):  # correção da reescrita / termo-chave
    return f'<span style="background-color:#FFEF9E;"><b>{t}</b></span>'


H2 = {
    "dem": "📈 Demanda: deslocamento × movimento",
    "eq": "⚖️ Equilíbrio, excedentes e tabelamento",
    "elas": "🧮 Elasticidade, gasto e tributos",
    "com": "🌍 Comércio internacional",
    "prod": "🏭 Produção e isoquantas",
    "islm": "🏦 IS-LM",
    "solow": "🌱 Crescimento: Solow",
    "fisc": "💰 Contas públicas: NFSP",
}

COMANDO_NABUCO_3 = ("Em relação à oferta e demanda e à classificação dos bens, julgue o item, considerando o "
                    "Gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo de D1 para D2.")

CARDS = [
    # ------------------------------------------------------------------ T01
    {
        "id": "ECO-T01-1", "fonte_ref": "ECO2 linha 746", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COMANDO_NABUCO_3,
        "frente_figuras": ["ECO-T01-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por uma redução do preço do bem x."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base no gráfico 1, […] é correto afirmar que o deslocamento da curva de demanda em "
                      "questão pode ser explicado por ") + vm("uma redução do preço do bem x") + az("."),
        "poucas": ("Variação no preço do <b>próprio</b> bem não desloca a curva de demanda: provoca "
                   + azb("movimento ao longo") + " dela. A curva só se desloca quando muda outro determinante."),
        "destrinchando": [
            "A curva de demanda é o gráfico de q<sub>d</sub> = f(p) <i>mantido o resto constante</i> (renda, "
            "preços de outros bens, gostos, expectativas, número de consumidores). Por isso o próprio preço já "
            "está <b>nos eixos</b>: quando ele muda, o consumidor apenas escolhe outro ponto da mesma curva.",
            "Distinção de vocabulário que a banca cobra: " + azb("variação da quantidade demandada")
            + " (movimento ao longo, causado por p do próprio bem) × " + azb("variação da demanda")
            + " (deslocamento da curva, causado por qualquer outro determinante).",
            "Para ir de D1 a D2 (para a direita, mais quantidade a cada preço) servem, por exemplo: aumento de "
            "renda se x for normal; queda de renda se x for inferior; alta do preço de um substituto; queda do "
            "preço de um complementar; mudança de gostos a favor de x.",
            vm("Regra-âncora: preço do próprio bem → anda na curva; qualquer outra causa → a curva anda."),
        ],
        "grafico_verso": "ECO-T01-V1",
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item troca “variação da demanda” por "
                       "“variação da quantidade demandada”: atribui o deslocamento da curva à única variável "
                       "que, por construção, não pode deslocá-la. Pista: o enunciado fala em curva que <b>se "
                       "desloca</b> e oferece como causa o preço do próprio bem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…pode ser explicado por uma redução do preço de um bem substituto de x…”</i> → ERRADO (sentido "
            "trocado: deslocaria para a esquerda)",
            "<i>“…pode ser explicado por uma redução do preço de um bem complementar de x…”</i> → CERTO",
        ])],
        "reescrita": ("Com base no gráfico 1, […] o deslocamento da curva de demanda em questão " + hl("não")
                      + " pode ser explicado por uma redução do preço do bem x, " + hl("que provocaria apenas "
                      "movimento ao longo de D1") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Deslocamento para a direita decorre de outros determinantes (renda, preço de "
                            "bens relacionados); preço do próprio bem gera movimento ao longo da curva.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 109", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada"}],
        "alertas": ["figura_conjectural: ECO-T01-F1 redesenhada a partir da descrição (D1 e D2 paralelas, "
                    "seta para a direita); posição exata das retas não preservada"],
    },
    # ------------------------------------------------------------------ T02
    {
        "id": "ECO-T02-1", "fonte_ref": "ECO2 linha 747", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": COMANDO_NABUCO_3,
        "frente_figuras": ["ECO-T01-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Com base no gráfico 1, que representa a curva de demanda do bem x, que se desloca no tempo "
                      "de D1 para D2, é correto afirmar que o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento no preço do bem y, se este for complementar do bem x."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base no gráfico 1, […] o deslocamento da curva de demanda em questão pode ser "
                      "explicado por um aumento no preço do bem y, se este for ") + vm("complementar")
                   + az(" do bem x."),
        "poucas": ("Se y é " + azb("complementar") + " de x, encarecer y <b>reduz</b> a demanda por x (curva "
                   "para a esquerda). O deslocamento para a direita exigiria y " + azb("substituto") + "."),
        "destrinchando": [
            "Bens relacionados se classificam pela " + azb("elasticidade-preço cruzada") + " ε<sub>xy</sub> = "
            "%Δq<sub>x</sub> / %Δp<sub>y</sub>: " + vd("ε > 0") + " → substitutos (café × chá); "
            + vd("ε < 0") + " → complementares (carro × gasolina); ε = 0 → independentes.",
            "Complementares são consumidos juntos: se y encarece, o “pacote” x + y fica mais caro e o consumidor "
            "compra menos dos dois. A demanda de x cai a cada preço de x — deslocamento para a <b>esquerda</b>.",
            "Substitutos competem pela mesma necessidade: se y encarece, parte do consumo migra para x, e a "
            "demanda de x sobe — deslocamento para a <b>direita</b>, como no Gráfico 1.",
            "Atenção ao objeto: o preço de y aparece no gráfico de x como <b>deslocador</b>; no gráfico de y, "
            "o mesmo aumento seria movimento ao longo da curva de y.",
        ],
        "grafico_verso": "ECO-T02-V1",
        "dissecando": (cz("[troca de conceito]") + " O mecanismo (preço de outro bem desloca a curva) está "
                       "certo; o erro está só no rótulo da relação: “complementar” no lugar de “substituto”. "
                       "Itens desse tipo se resolvem pelo sinal: ↑p<sub>y</sub> + complementar = ↓D<sub>x</sub>."),
        "modulos": [("🧠 Mnemônico", ["<b>C</b>omplementar <b>C</b>ai junto; <b>S</b>ubstituto <b>S</b>obe o outro."])],
        "reescrita": ("Com base no gráfico 1, […] o deslocamento da curva de demanda em questão pode ser explicado "
                      "por um aumento no preço do bem y, se este for " + hl("substituto") + " do bem x."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode", "se"], "dificuldade": 1,
        "comentario_fonte": "Complementares: ↑p de um reduz a demanda do outro; substitutos: aumenta. "
                            "O deslocamento seria explicado se y fosse substituto.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 109", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada"}],
        "alertas": ["figura_conjectural: ECO-T01-F1 (mesma figura do item 1)"],
    },
    # ------------------------------------------------------------------ T03
    {
        "id": "ECO-T03-1", "fonte_ref": "ECO2 linha 495", "subtema": H2["com"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": ("Considere os coeficientes técnicos de produção de dois países, em horas de trabalho por "
                    "unidade produzida, e suponha custos de transporte nulos. Com base na teoria das vantagens "
                    "absolutas (Adam Smith) e comparativas (David Ricardo), julgue o item."),
        "frente_figuras": ["ECO-T03-F1"],
        "rotulo_item": "Item",
        "assertiva": "Brasil detém vantagem comparativa em vestuário.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": vm("Brasil") + az(" detém vantagem comparativa em vestuário."),
        "poucas": ("Vantagem comparativa = menor " + azb("custo de oportunidade") + ". Em vestuário, ele é "
                   + vd("7/3 de calçado") + " no Brasil e " + vd("1/2 calçado") + " no México: a vantagem é "
                   "mexicana."),
        "destrinchando": [
            "Custo de oportunidade de 1 unidade de vestuário = horas para fazer vestuário ÷ horas para fazer "
            "calçado. " + rx("Brasil") + ": (1/3) ÷ (1/7) = " + vd("7/3 ≈ 2,33 calçados") + ". "
            "<b>México</b>: (1/2) ÷ 1 = " + vd("0,5 calçado") + ".",
            "Logo o México tem vantagem comparativa em <b>vestuário</b>, e o " + rx("Brasil")
            + ", em <b>calçados</b> (custo de 3/7 de vestuário por calçado, contra 2 no México).",
            "Não confundir com " + azb("vantagem absoluta") + " (" + oc("Adam Smith") + "), que compara horas "
            "diretamente: o Brasil gasta menos horas nos dois bens (1/7 < 1 e 1/3 < 1/2) e tem vantagem "
            "absoluta em ambos — e, mesmo assim, há ganho de comércio, que é a tese de " + oc("David Ricardo")
            + ".",
            "Ganho mútuo exige termos de troca entre os custos de oportunidade dos dois: 3/7 < p<sub>calçado</sub>"
            " (em vestuário) < 2.",
            vm("Regra-âncora: na comparativa, compara-se a razão entre os bens dentro de cada país, nunca as "
               "horas entre países."),
        ],
        "dissecando": (cz("[troca de ator · troca de conceito]") + " O item troca o país detentor e se apoia na "
                       "confusão absoluta × comparativa: quem olha só as horas vê o Brasil “melhor em tudo” e "
                       "marca CERTO. 🔥 A banca adora tabela de coeficientes com um país absolutamente superior "
                       "nos dois bens."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Brasil detém vantagem absoluta na produção de ambos os bens.”</i> → CERTO",
            "<i>“Com termos de troca de 1 calçado por 3 unidades de vestuário, ambos ganham com o comércio.”</i> "
            "→ ERRADO (fora do intervalo 3/7–2)",
        ])],
        "reescrita": hl("O México") + " detém vantagem comparativa em vestuário " + hl("e o Brasil, em calçados")
                     + ".",
        "tipo_erro": ["TROCA_ATOR", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Custo de oportunidade do vestuário: México 1/2 calçado; Brasil 7/3. México tem "
                            "vantagem comparativa em vestuário; Brasil em calçados.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 086", "tipo_fonte": "TABELA", "lado": "frente",
                           "acao": "tabela_png (teste da alternativa à tabela HTML)"}],
        "alertas": ["teste_importacao: tabela da frente como PNG (comparar com ECO-T13-1, tabela HTML aninhada)"],
    },
    # ------------------------------------------------------------------ T04
    {
        "id": "ECO-T04-1", "fonte_ref": "ECO2 linha 1036", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Em um mercado competitivo, as curvas de demanda e de oferta de um produto são "
                    "Qᴰ = 300 − 30p e Qˢ = 10p + 20, em que p é o preço do produto, em reais. Julgue o item."),
        "rotulo_item": "Item",
        "assertiva": "O consumidor tem um excedente no valor de R$ 135,00.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O consumidor tem um excedente no valor de <u>R$ 135,00</u>."),
        "poucas": ("Equilíbrio em " + vd("p = 7, Q = 90") + "; o preço de reserva (Qᴰ = 0) é "
                   + vd("10") + ". Excedente do consumidor = (10 − 7) × 90 ÷ 2 = " + vd("135") + "."),
        "destrinchando": [
            "Roteiro de três passos para qualquer mercado linear: (1) igualar Qᴰ = Qˢ → 300 − 30p = 10p + 20 → "
            + vd("p* = 7") + "; (2) substituir → " + vd("Q* = 90") + "; (3) achar os interceptos no eixo do "
            "preço: demanda zera em " + vd("p = 10") + "; oferta zera em p = −2 (só começa a ofertar com "
            "p > 0, a partir de Q = 20).",
            azb("Excedente do consumidor") + " = soma, sobre as unidades compradas, de (disposição a pagar − "
            "preço pago): é o triângulo entre a demanda e a linha do preço. Base 90, altura 10 − 7 = 3 → "
            + vd("135") + ".",
            azb("Excedente do produtor") + " = área entre o preço e a oferta. Aqui a oferta corta o eixo das "
            "<b>quantidades</b> (Q = 20 com p = 0), então a área é um retângulo 20 × 7 mais um triângulo "
            "70 × 7 ÷ 2 = " + vd("385") + ".",
            "Erro clássico: usar a demanda escrita como Q(p) direto na fórmula da área. Sempre reescreva em "
            "função inversa (p = 10 − Q/30) ou leia os interceptos antes.",
        ],
        "grafico_verso": "ECO-T04-V1",
        "dissecando": (cz("[detalhe]") + " Item de cálculo puro: a banca dá o número exato e aposta que o "
                       "candidato erre o intercepto (usar 300 em vez de 10) ou esqueça a divisão por 2 "
                       "(resultado 270)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O consumidor tem um excedente no valor de R$ 270,00.”</i> → ERRADO (esqueceu o ÷ 2)",
            "<i>“O excedente do produtor é inferior ao do consumidor.”</i> → ERRADO (385 > 135)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "p = 7, Q = 90; intercepto da demanda p = 10; EC = 90 × 3 / 2 = 135.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 174", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "texto (equações transcritas no comando)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ T05
    {
        "id": "ECO-T05-1", "fonte_ref": "ECO2 linha 1037", "subtema": H2["eq"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Em um mercado competitivo, as curvas de demanda e de oferta de um produto são "
                    "Qᴰ = 300 − 30p e Qˢ = 10p + 20, em que p é o preço do produto, em reais. Julgue o item."),
        "rotulo_item": "Item",
        "assertiva": "Se o governo tabelar o preço do produto em R$ 6,00, haverá um excesso de oferta de 50 unidades.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o governo tabelar o preço do produto em R$ 6,00, haverá um excesso de ")
                   + vm("oferta de 50") + az(" unidades."),
        "poucas": ("Teto abaixo do equilíbrio (6 < 7) gera " + azb("excesso de demanda") + ": Qᴰ = "
                   + vd("120") + " e Qˢ = " + vd("80") + " — faltam " + vd("40") + " unidades."),
        "destrinchando": [
            "Com p = 6: Qᴰ = 300 − 180 = " + vd("120") + "; Qˢ = 60 + 20 = " + vd("80") + ". Diferença: "
            + vd("40") + " unidades de <b>escassez</b>.",
            "Um " + azb("preço máximo") + " (teto) só “morde” se ficar <b>abaixo</b> do equilíbrio: aí gera "
            "filas, racionamento, mercado paralelo e queda de qualidade. Um " + azb("preço mínimo")
            + " (piso) só morde <b>acima</b> do equilíbrio e gera excedente de oferta (ex.: salário mínimo × "
            "desemprego no modelo competitivo; preços mínimos agrícolas com compra do excedente pelo governo).",
            "Teto acima do equilíbrio ou piso abaixo dele são inócuos: o mercado continua em (90; 7).",
            "Bem-estar: com o teto, transaciona-se só o que os produtores aceitam vender (80); surge peso morto "
            "entre 80 e 90.",
        ],
        "grafico_verso": "ECO-T05-V1",
        "dissecando": (cz("[troca de conceito · dado alterado]") + " Duas falhas empilhadas: o sentido do "
                       "desequilíbrio (oferta × demanda) e o tamanho (50 × 40). O 50 sai de quem calcula "
                       "Qᴰ − Q* ou erra a conta da oferta; basta a primeira falha para marcar ERRADO."),
        "modulos": [("🧠 Mnemônico", ["<b>Teto</b> baixo → <b>t</b>odo mundo quer comprar (escassez); "
                                      "<b>piso</b> alto → <b>p</b>roduto sobrando."])],
        "reescrita": ("Se o governo tabelar o preço do produto em R$ 6,00, haverá um excesso de "
                      + hl("demanda") + " de " + hl("40") + " unidades."),
        "tipo_erro": ["TROCA_CONCEITO", "DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "P = 6 < 7 gera excesso de demanda, não de oferta.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 174", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "texto (equações transcritas no comando)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ T06
    {
        "id": "ECO-T06-1", "fonte_ref": "ECO2 linha 1353", "subtema": H2["islm"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Considere o gráfico seguinte, em que Y* é o produto de equilíbrio e i* consiste na taxa de "
                    "juros de equilíbrio. Com base no gráfico apresentado e no modelo IS-LM, julgue o item."),
        "frente_figuras": ["ECO-T06-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Uma compra de títulos, por parte da autoridade monetária, deslocaria a curva LM para cima "
                      "(esquerda), o que provocaria um aumento da taxa de juros de equilíbrio e uma redução da "
                      "renda da economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma compra de títulos, por parte da autoridade monetária, deslocaria a curva LM para ")
                   + vm("cima (esquerda)") + az(", o que provocaria ") + vm("um aumento") + az(" da taxa de "
                   "juros de equilíbrio e ") + vm("uma redução") + az(" da renda da economia."),
        "poucas": ("Comprar títulos = " + azb("injetar moeda") + " (open market expansionista): a LM vai para "
                   "baixo/direita, os juros caem e a renda sobe."),
        "destrinchando": [
            "No " + azb("open market") + ", o Banco Central paga os títulos que compra com moeda nova: a base "
            "monetária e a oferta de moeda (M/P) aumentam. Venda de títulos faz o contrário (enxuga liquidez).",
            "Mais moeda com a mesma demanda por moeda exige juros menores para o mercado monetário se equilibrar "
            "a cada nível de renda → a LM se desloca para a <b>direita</b> (para baixo).",
            "Novo equilíbrio: " + vd("i ↓") + " estimula o investimento → " + vd("Y ↑")
            + ". A intensidade depende das inclinações: LM muito inclinada (clássico) → política monetária "
            "muito eficaz; LM horizontal (armadilha da liquidez) → ineficaz.",
            vm("Regra-âncora: política monetária mexe na LM; política fiscal mexe na IS."),
        ],
        "grafico_verso": "ECO-T06-V1",
        "dissecando": (cz("[inversão]") + " O item descreve com coerência interna o efeito de uma <b>venda</b> "
                       "de títulos (contracionista) e o atribui à compra. Como tudo “fecha” (LM esquerda → i↑, "
                       "Y↓), a armadilha é não checar o ponto de partida: quem compra título <b>paga em "
                       "moeda</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma venda de títulos pela autoridade monetária deslocaria a LM para a esquerda, elevando os "
            "juros e reduzindo a renda.”</i> → CERTO",
            "<i>“Uma compra de títulos deslocaria a curva IS para a direita.”</i> → ERRADO (curva trocada: é a LM)",
        ])],
        "reescrita": ("Uma compra de títulos, por parte da autoridade monetária, deslocaria a curva LM para "
                      + hl("baixo (direita)") + ", o que provocaria " + hl("uma redução") + " da taxa de "
                      "juros de equilíbrio e " + hl("um aumento") + " da renda da economia."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Compra de títulos é expansionista: LM para baixo/direita, juros caem, renda sobe.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 233", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada"}],
        "alertas": ["figura_conjectural: ECO-T06-F1 redesenhada a partir da descrição (IS × LM em (Y*, i*))"],
    },
    # ------------------------------------------------------------------ T07
    {
        "id": "ECO-T07-1", "fonte_ref": "ECO2 linha 1355", "subtema": H2["islm"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Considere o gráfico seguinte, em que Y* é o produto de equilíbrio e i* consiste na taxa de "
                    "juros de equilíbrio. Com base no gráfico apresentado e no modelo IS-LM, julgue o item."),
        "frente_figuras": ["ECO-T06-F1"],
        "rotulo_item": "Item",
        "assertiva": ("No curto prazo, em uma situação de armadilha da liquidez, a política fiscal é ineficaz "
                      "para alterar o nível de renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No curto prazo, em uma situação de armadilha da liquidez, a política ")
                   + vm("fiscal") + az(" é ineficaz para alterar o nível de renda."),
        "poucas": ("Na " + azb("armadilha da liquidez") + " a LM é horizontal: a política <b>monetária</b> é "
                   "ineficaz e a <b>fiscal</b> tem eficácia máxima (sem crowding out)."),
        "destrinchando": [
            "Com juros muito baixos, todos esperam que eles subam (e que os títulos percam valor): a demanda "
            "por moeda torna-se " + azb("infinitamente elástica aos juros") + ". Qualquer moeda adicional é "
            "entesourada — a LM fica horizontal.",
            "Política monetária: mais moeda não reduz juros que já não caem → Y não muda. Política fiscal: a "
            "IS se desloca ao longo do trecho plano, os juros não sobem, não há " + azb("crowding out")
            + " e o " + azb("multiplicador keynesiano") + " opera por inteiro.",
            "Origem: " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) descreveu a possibilidade; o nome e a "
            "formalização vieram depois, com " + oc("Hicks") + " (1937), criador do IS-LM. O caso voltou ao "
            "debate com o Japão dos anos 1990 e o pós-2008 (juro zero).",
            "Espelho: no " + azb("caso clássico") + " (LM vertical, demanda por moeda insensível aos juros), a "
            "fiscal é totalmente ineficaz (crowding out completo) e a monetária, máxima.",
            vm("Regra-âncora: LM horizontal → fiscal manda; LM vertical → monetária manda."),
        ],
        "grafico_verso": "ECO-T07-V1",
        "dissecando": (cz("[troca de conceito · inversão]") + " Troca a política: a ineficácia na armadilha "
                       "é da <b>monetária</b>. Itens de IS-LM extremos quase sempre testam essa tabela de "
                       "quatro casas (LM horizontal/vertical × fiscal/monetária)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na armadilha da liquidez, a política monetária é ineficaz para alterar a renda.”</i> → CERTO",
            "<i>“No caso clássico, a política fiscal expansionista eleva a renda sem efeito "
            "deslocamento.”</i> → ERRADO (inversão: no clássico o crowding out é total)",
        ])],
        "reescrita": ("No curto prazo, em uma situação de armadilha da liquidez, a política "
                      + hl("monetária") + " é ineficaz para alterar o nível de renda" + hl(", e a fiscal tem "
                      "eficácia máxima") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "LM horizontal: monetária ineficaz, fiscal com eficácia máxima, sem crowding out.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 233", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada"}],
        "alertas": ["figura_conjectural: ECO-T06-F1 (mesma figura)"],
    },
    # ------------------------------------------------------------------ T08
    {
        "id": "ECO-T08-1", "fonte_ref": "ECO2 linha 1218", "subtema": H2["prod"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Considere uma função de produção que utilize capital (K) e trabalho (L), estando as "
                    "isoquantas dessa produção (Q) descritas na figura apresentada. A partir desses dados, "
                    "julgue o item."),
        "frente_figuras": ["ECO-T08-F1"],
        "rotulo_item": "Item",
        "assertiva": "A função de produção em questão respeita a lei dos rendimentos marginais decrescentes.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função de produção em questão ") + vm("respeita") + az(" a lei dos rendimentos "
                                                                                "marginais decrescentes."),
        "poucas": ("Isoquantas retas e igualmente espaçadas = " + azb("substitutos perfeitos") + " (Q = aK + "
                   "bL): o produto marginal de cada fator é <b>constante</b>, não decrescente."),
        "destrinchando": [
            "Isoquanta reta → " + azb("TMST constante") + ": troca-se K por L sempre à mesma taxa. Forma "
            "funcional típica: Q = aK + bL. Daí PMg<sub>K</sub> = a e PMg<sub>L</sub> = b, constantes.",
            "Fixe K e aumente L: cada unidade extra de L acrescenta sempre b unidades de produto — "
            + azb("rendimentos marginais constantes") + ". A lei dos rendimentos decrescentes exigiria PMg "
            "caindo com o uso do fator.",
            "Espaçamento uniforme (Q₁, Q₂ = 2Q₁, Q₃ = 3Q₁ a distâncias iguais da origem) indica "
            + azb("rendimentos constantes de escala") + ": dobrar K e L dobra Q.",
            "Não confundir os dois conceitos: <b>rendimento marginal</b> = um fator varia, o outro fixo (curto "
            "prazo); <b>rendimento de escala</b> = todos os fatores na mesma proporção (longo prazo). Uma "
            "Cobb-Douglas com α + β = 1 tem rendimentos constantes de escala <i>e</i> marginais decrescentes.",
            "Comparação de formatos: retas → substitutos perfeitos; em L → complementares perfeitos "
            "(Leontief, PMg zero além do vértice); convexas → caso usual.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item empresta uma “lei” geral da microeconomia e a "
                       "aplica a uma tecnologia que é justamente a exceção. Pista visual: retas. 🔥 A banca "
                       "costuma pedir no mesmo bloco escala (CERTO aqui) e rendimento marginal (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função apresenta rendimentos constantes de escala.”</i> → CERTO",
            "<i>“A taxa marginal de substituição técnica é decrescente ao longo de cada isoquanta.”</i> → "
            "ERRADO (é constante: isoquanta reta)",
        ])],
        "reescrita": ("A função de produção em questão " + hl("não") + " respeita a lei dos rendimentos "
                      "marginais decrescentes" + hl(": os produtos marginais de K e de L são constantes") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Insumos com rendimentos constantes; fixando um fator, cada unidade adicional do "
                            "outro gera acréscimo constante de produção.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 209", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada"},
                          {"ref": "IMAGEM 210", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (repetia a figura da frente)"}],
        "alertas": ["figura_conjectural: ECO-T08-F1 sem os valores numéricos das isoquantas (não constam da "
                    "transcrição); espaçamento uniforme deduzido do gabarito do item 1 (rendimentos constantes "
                    "de escala = CERTO)"],
    },
    # ------------------------------------------------------------------ T09
    {
        "id": "ECO-T09-1", "fonte_ref": "ECO2 linha 1389", "subtema": H2["elas"],
        "tipo": "EXERC", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Responda à questão a seguir, sobre os efeitos de um imposto sobre o bem-estar.",
        "rotulo_item": "Questão",
        "assertiva": ("Indique graficamente onde identificar o que é excedente e o que é peso morto após a "
                      "imposição de um imposto."),
        "gabarito": "RESPOSTA", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("Com o imposto t, o preço pago pelo comprador sobe para pc e o recebido pelo vendedor cai "
                      "para pv; a quantidade cai de q0 para qt. Excedente do consumidor: área entre a demanda e "
                      "pc. Excedente do produtor: área entre pv e a oferta. Receita: retângulo t × qt. Peso "
                      "morto: triângulo entre as curvas, de qt a q0."),
        "poucas": ("O imposto abre uma " + azb("cunha") + " entre pc e pv; parte dos antigos excedentes vira "
                   "receita do governo (retângulo) e parte se perde (" + azb("peso morto") + ", triângulo)."),
        "destrinchando": [
            "Antes do imposto: equilíbrio (q0, p0); EC = área entre D e p0; EP = área entre p0 e O.",
            "Imposto específico t (no vendedor ou no comprador — o resultado econômico é o mesmo): a oferta "
            "relevante passa a ser O + t. Novo equilíbrio em qt, com " + vd("pc − pv = t") + ".",
            "Repartição do bolo: EC encolhe para o triângulo acima de pc; EP, para o triângulo abaixo de pv; o "
            "retângulo " + vd("t × qt") + " é a " + azb("receita tributária") + " (transferência, não perda); o "
            "triângulo entre qt e q0 é o " + azb("peso morto") + ": trocas mutuamente vantajosas que deixaram "
            "de existir.",
            "Quem paga mais: o lado <b>menos elástico</b>. Demanda inelástica → pc sobe quase t inteiro "
            "(consumidor arca). O peso morto cresce com as elasticidades e com o <b>quadrado</b> da alíquota "
            "(dobrar t ≈ quadruplicar o peso morto).",
        ],
        "grafico_verso": "ECO-T09-V1",
        "dissecando": (cz("[exercício aberto]") + " Em C/E, a banca transforma esse gráfico em itens do tipo "
                       "“a receita do governo corresponde à perda do consumidor” (ERRADO: só parte dela) ou "
                       "“a incidência depende de quem recolhe o imposto” (ERRADO: depende das elasticidades)."),
        "modulos": [("🃏 Carta na manga", ["Tributo eficiente é o que incide sobre bases inelásticas "
                                           "(regra de " + oc("Ramsey") + "), mas isso conflita com equidade: "
                                           "bens inelásticos costumam pesar mais no orçamento dos pobres."])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Verso original composto só de cinco imagens (gráficos de receita tributária e "
                            "peso morto), sem texto.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 281", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "cortada (a frente pede o gráfico: ele vai para o verso)"},
                          {"ref": "IMAGEM 282-285", "tipo_fonte": "GRÁFICO/DIAGRAMA", "lado": "verso",
                           "acao": "fundidas em ECO-T09-V1"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ T10
    {
        "id": "ECO-T10-1", "fonte_ref": "ECO2 linha 1657", "subtema": H2["com"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "O gráfico ilustra a imposição de uma tarifa de importação de aço num dado país. Julgue o item.",
        "frente_figuras": ["ECO-T10-F1"],
        "rotulo_item": "Item",
        "assertiva": ("Após a tarifa, o excedente dos ofertantes domésticos vai crescer no montante equivalente à "
                      "soma das áreas C e G."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Após a tarifa, o excedente dos ofertantes domésticos vai crescer no montante equivalente "
                      "à ") + vm("soma das áreas C e G") + az("."),
        "poucas": ("O excedente do produtor <b>passa a ser</b> C + G, mas <b>cresce</b> só " + vd("C")
                   + ": G já pertencia aos produtores antes da tarifa."),
        "destrinchando": [
            "Com livre-comércio ao preço mundial: EC = A + B + C + D + E + F; EP = G. O país importa "
            "Qᴰ₁ − Qˢ₁.",
            "Com a tarifa, o preço doméstico sobe ao preço mundial + tarifa: EC = A + B; EP = " + vd("C + G")
            + "; receita do governo = " + vd("E") + " (tarifa × importações remanescentes Qᴰ₂ − Qˢ₂).",
            "Variações: consumidor perde C + D + E + F; produtor ganha " + vd("C") + "; governo ganha "
            + vd("E") + "; " + azb("peso morto") + " = " + vd("D + F") + " — D é a ineficiência de produzir "
            "domesticamente o que se importava mais barato; F, o consumo que deixou de ocorrer.",
            "Cota de importação equivalente produz o mesmo preço e as mesmas perdas, com uma diferença: a "
            "área E vira " + azb("renda de cota") + " de quem detém as licenças, não receita pública.",
            vm("Regra-âncora: “cresce” pede a variação (C), não o estoque final (C + G)."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A soma C + G é real — é o excedente "
                       "<b>final</b> do produtor. O erro está no verbo: “crescer no montante” pede a "
                       "<b>variação</b>. 🔥 Gráficos com áreas em letra sempre testam estoque × variação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Após a tarifa, o excedente dos ofertantes domésticos passa a ser a soma das áreas C e G.”</i> → "
            "CERTO",
            "<i>“O peso morto da tarifa corresponde às áreas D, E e F.”</i> → ERRADO (E é receita do governo, "
            "não perda)",
        ])],
        "reescrita": ("Após a tarifa, o excedente dos ofertantes domésticos vai crescer no montante equivalente à "
                      + hl("área C") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Aumento do EP é só a área C; G não faz parte do ganho. Peso morto = D + F; receita "
                            "= E; cota também eleva o preço.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 480", "tipo_fonte": "GRÁFICO", "lado": "frente",
                           "acao": "redesenhada (convenção de áreas de Mankiw)"},
                          {"ref": "IMAGEM 481-482", "tipo_fonte": "GRÁFICO/TABELA", "lado": "verso",
                           "acao": "cortadas (conteúdo absorvido no 📖)"}],
        "alertas": ["figura_conjectural: ECO-T10-F1 com áreas A–G posicionadas pela convenção de Mankiw; a "
                    "transcrição não traz a posição das letras. O item 3 da mesma questão cita uma área R que "
                    "não existe nessa convenção — reenviar a imagem original antes de converter os itens 2 a 4",
                    "qualidade_fonte: o comentário de origem descreve G como “perda do consumidor”; G é o "
                    "excedente do produtor anterior à tarifa"],
    },
    # ------------------------------------------------------------------ T11
    {
        "id": "ECO-T11-1", "fonte_ref": "ECO2 linha 151", "subtema": H2["solow"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": "Com base nos modelos de crescimento econômico, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("No contexto do modelo de Solow, o ponto de ouro no estado estacionário é onde a economia "
                      "maximiza seu nível de consumo, sendo este ponto alcançado no ponto estacionário máximo, em "
                      "que a taxa de investimento per capita se iguala à taxa de depreciação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No contexto do modelo de Solow, o ponto de ouro no estado estacionário é onde a economia "
                      "maximiza seu nível de consumo, sendo este ponto alcançado ") + vm("no ponto estacionário "
                      "máximo, em que a taxa de investimento per capita se iguala à taxa de depreciação")
                   + az("."),
        "poucas": ("Investimento = depreciação (efetiva) vale em <b>todo</b> estado estacionário. A regra de ouro "
                   "é o estado estacionário em que " + vd("f′(k) = n + δ") + " — e não o de capital "
                   "“máximo”."),
        "destrinchando": [
            "Dinâmica de " + oc("Solow") + " (1956): Δk = s·f(k) − (n + δ)k. No " + azb("estado estacionário")
            + " k* o investimento por trabalhador cobre exatamente a depreciação e a diluição pelo crescimento "
            "populacional: " + vd("s·f(k*) = (n + δ)k*") + ". Há um k* para cada taxa de poupança s.",
            "Consumo de estado estacionário: c* = f(k*) − (n + δ)k*. Maximizando em k*: "
            + vd("f′(k_ouro) = n + δ") + " (com progresso técnico, n + g + δ). É a " + azb("regra de ouro")
            + " de " + oc("Phelps") + " (1961): a inclinação da função de produção iguala a da reta de "
            "investimento necessário.",
            "O “ponto estacionário máximo” (s = 100%) é o pior possível: todo o produto vai para investimento e "
            "o consumo é zero. Poupar acima de s_ouro leva a " + azb("ineficiência dinâmica") + ": capital "
            "demais, consumo de menos, e reduzir s elevaria o consumo em todas as datas.",
            "Na Cobb-Douglas f(k) = k^α, a regra de ouro dá " + vd("s_ouro = α") + " (a participação do capital "
            "na renda).",
        ],
        "grafico_verso": "ECO-T11-V1",
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A primeira oração é a definição correta "
                       "(maximiza o consumo); o erro foi enxertado na condição, que é a de <b>qualquer</b> "
                       "estado estacionário, e no “máximo”, que sugere mais capital = melhor. Pista: a "
                       "condição oferecida não envolve a inclinação de f(k)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No estado estacionário de regra de ouro, o produto marginal do capital iguala a soma das taxas "
            "de crescimento populacional e de depreciação.”</i> → CERTO",
            "<i>“Se a poupança supera a de regra de ouro, reduzi-la diminui o consumo no curto prazo.”</i> → "
            "ERRADO (inversão: aumenta o consumo já e no longo prazo)",
        ])],
        "reescrita": ("No contexto do modelo de Solow, o ponto de ouro no estado estacionário é onde a economia "
                      "maximiza seu nível de consumo, sendo este ponto alcançado " + hl("no estado estacionário "
                      "em que o produto marginal do capital se iguala à soma das taxas de depreciação e de "
                      "crescimento populacional") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["máximo"], "dificuldade": 2,
        "comentario_fonte": "Investimento = depreciação efetiva vale em todo estado estacionário; a regra de "
                            "ouro exige f'(k) = n + g + δ (Phelps).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 011", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-T11-V1)"},
                          {"ref": "IMAGEM 012", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (texto absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ T12
    {
        "id": "ECO-T12-1", "fonte_ref": "ECO1 nota 01.1 - Obj., linha 1", "subtema": H2["elas"],
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
        "anotada": az("Considerando que haja relação positiva entre criminalidade e gastos com o consumo de "
                      "drogas e que a demanda por drogas seja <u>preço-inelástica</u>, políticas antidrogas "
                      "fundamentadas no combate ao tráfico elevarão o preço das drogas e <u>os gastos</u> com "
                      "esses produtos, agravando os níveis de criminalidade."),
        "poucas": ("Reprimir o tráfico reduz a " + azb("oferta") + " e eleva o preço; com demanda "
                   + azb("inelástica") + ", a quantidade cai menos que o preço sobe e o " + vd("gasto (p × q) "
                   "aumenta") + " — e, pela premissa, a criminalidade também."),
        "destrinchando": [
            "Gasto do consumidor = receita do vendedor = p × q. Quando p sobe, o efeito sobre o gasto depende "
            "de |ε|: " + vd("|ε| < 1") + " (inelástica) → gasto sobe; |ε| > 1 (elástica) → gasto cai; |ε| = 1 "
            "→ gasto constante.",
            "Drogas são o exemplo clássico de demanda inelástica: dependência química, poucos substitutos, "
            "peso do hábito. A repressão desloca a oferta para a esquerda (custo e risco maiores para o "
            "traficante), o preço sobe muito e a quantidade cai pouco.",
            "Com a premissa do item (crime ↑ quando o gasto ↑), o efeito líquido é mais crime: usuários "
            "cometem crimes para financiar o consumo, e o tráfico fatura mais. É o exemplo de "
            + oc("Mankiw") + " (<i>Introdução à Economia</i>, capítulo sobre elasticidade e suas aplicações) "
            "para defender políticas de redução da <b>demanda</b> (educação, tratamento), que reduzem p e q "
            "ao mesmo tempo.",
            vm("Regra-âncora: choque de oferta + demanda inelástica → gasto total sobe."),
        ],
        "grafico_verso": "ECO-T12-V1",
        "dissecando": (cz("[contraintuitivo]") + " O item é verdadeiro, mas contraria o senso comum de que "
                       "reprimir o tráfico sempre reduz o crime. A banca entrega as duas premissas "
                       "(“relação positiva” e “preço-inelástica”): o julgamento é dedução, não opinião."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se a demanda por drogas fosse preço-elástica, a repressão elevaria o gasto com drogas…”</i> → "
            "ERRADO (com |ε| > 1 o gasto cai)",
            "<i>“Políticas de educação sobre os riscos das drogas, ao reduzirem a demanda, diminuem o preço e "
            "o gasto com drogas.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Demanda inelástica: repressão reduz a oferta, preço sobe, consumo quase não cai, "
                            "gasto aumenta e, pela premissa, a criminalidade. Retângulo de gasto maior depois.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "ECO1 image (4).png", "tipo_fonte": "QUESTÃO EM IMAGEM",
                           "lado": "frente", "acao": "texto reconstruído pelo comentário"},
                          {"ref": "ECO1 image (3), (1), (2).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhadas em ECO-T12-V1 (antes × depois)"}],
        "alertas": ["texto_reconstruido: frente original era imagem; assertiva reconstruída a partir do "
                    "comentário e de versões do item em bancos de questões — conferir com a imagem "
                    "image (4).png do caderno 1 (nota 01.1 - Obj.)",
                    "banca_provavel: CEBRASPE (não confirmada: a fonte não traz órgão nem ano)"],
    },
    # ------------------------------------------------------------------ T13
    {
        "id": "ECO-T13-1", "fonte_ref": "ECO2 linha 738", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": ("Considerando as informações apresentadas na tabela, referentes à evolução do déficit público "
                    "brasileiro nos anos de 2022 e 2023, bem como aspectos relativos à estrutura orçamentária do "
                    "governo, julgue o item."),
        "excerto_tabela": {
            "titulo": "Necessidades de financiamento do setor público — setor público consolidado",
            "cabecalho": ["Conceito", "2022 (R$ bi)", "2022 (% PIB)", "2023 (R$ bi)", "2023 (% PIB)"],
            "linhas": [["Nominal", "460,4", "4,6", "967,4", "8,9"],
                       ["Juros nominais", "586,4", "5,8", "718,3", "6,6"],
                       ["Primário", "−126,0", "−1,2", "249,1", "2,3"]],
            "fonte": "Banco Central do Brasil, 2024 (com adaptações). PIB: R$ 10.079,7 bi (2022) e "
                     "R$ 10.856,1 bi (2023).",
        },
        "rotulo_item": "Item",
        "assertiva": ("Em 2022, observou-se um déficit primário de R$ 126 bilhões, o que foi compensado pelo bom "
                      "desempenho das contas no ano seguinte, evidenciado pelo superávit primário de R$ 249,1 "
                      "bilhões."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em 2022, observou-se um ") + vm("déficit") + az(" primário de R$ 126 bilhões, ")
                   + vm("o que foi compensado pelo bom desempenho das contas no ano seguinte, evidenciado pelo "
                        "superávit") + az(" primário de R$ 249,1 bilhões."),
        "poucas": ("Nas " + azb("NFSP") + ", sinal positivo = <b>déficit</b> e negativo = <b>superávit</b>. "
                   "Houve " + vd("superávit primário em 2022") + " (−126,0) e " + vd("déficit primário em "
                   "2023") + " (249,1): o item inverte os dois."),
        "destrinchando": [
            azb("Necessidades de financiamento do setor público") + " medem quanto o setor público precisa "
            "tomar emprestado: por isso o déficit aparece com sinal <b>positivo</b>. É a convenção do "
            + rx("Banco Central do Brasil") + " (critério “abaixo da linha”, pela variação da dívida).",
            azb("Resultado primário") + " = receitas − despesas, excluídos os juros. "
            + azb("Resultado nominal") + " = primário + juros nominais. Confira na tabela: "
            "−1,2 + 5,8 = " + vd("4,6% do PIB") + " (2022) e 2,3 + 6,6 = " + vd("8,9%") + " (2023).",
            "Leitura econômica: em 2022, o superávit primário (com receitas de commodities e inflação alta) "
            "conviveu com déficit nominal de 4,6% do PIB, puxado por juros de 5,8%. Em 2023, a virada para "
            "déficit primário e juros maiores levaram o nominal a 8,9%.",
            "Mesmo com superávit primário, a dívida pode crescer: basta que o primário não cubra os juros. "
            "Por isso a sustentabilidade se discute pelo primário <b>necessário</b> para estabilizar a "
            "relação dívida/PIB.",
            "⏳ (out/2026) Valores de 2022–2023 conforme a tabela; séries atualizadas na Nota de Política "
            "Fiscal do BCB.",
        ],
        "grafico_verso": "ECO-T13-V1",
        "dissecando": (cz("[inversão]") + " O item inverte a convenção de sinais das NFSP e, sobre a "
                       "inversão, constrói um nexo (“compensado pelo bom desempenho”). Quem lê “−126” como "
                       "déficit cai. 🔥 Tabela de NFSP em prova quase sempre testa o sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em 2022, o setor público apresentou superávit primário e déficit nominal.”</i> → CERTO",
            "<i>“Em 2023, o déficit nominal decorreu exclusivamente da conta de juros.”</i> → ERRADO (modulador "
            "absoluto: o primário também foi deficitário)",
        ])],
        "reescrita": ("Em 2022, observou-se um " + hl("superávit") + " primário de R$ 126 bilhões, "
                      + hl("seguido, no ano seguinte, de déficit") + " primário de R$ 249,1 bilhões."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Valores positivos = déficit; negativos = superávit. 2022 superávit primário de 126; "
                            "2023 déficit primário de 249.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 105", "tipo_fonte": "TABELA", "lado": "frente",
                           "acao": "transcrita_html (tabela aninhada, 5 colunas)"}],
        "alertas": ["transcricao_incoerente: a transcrição da IMAGEM 105 dá o nominal de 2022 como −460,4 "
                    "(−4,6%); pela identidade nominal = primário + juros (−126,0 + 586,4) o valor é +460,4 "
                    "(4,6%) — corrigido",
                    "texto_parcial: a tabela original discrimina governo central, estados, municípios e "
                    "estatais; a transcrição só preservou o consolidado",
                    "teste_importacao: tabela HTML aninhada na frente (comparar com ECO-T03-1, tabela PNG)"],
    },
]
