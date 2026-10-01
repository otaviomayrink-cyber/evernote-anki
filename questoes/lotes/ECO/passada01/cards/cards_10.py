"""Cards da passada 01 de ECO — lote de redação 10 (nota 04: teoria do consumidor)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "pref": "🧠 Preferências e axiomas",
    "util": "🎯 Utilidade e curvas de indiferença",
    "ro": "💵 Restrição orçamentária",
    "otimo": "⚖️ Escolha ótima do consumidor",
    "dem": "📊 Demanda individual e de mercado",
}

COMANDO_UTIL = "Julgue o item a seguir, relativo à teoria da utilidade e às preferências do consumidor."
COMANDO_CLIP25 = ("As escolhas do consumidor são fundamentais para entender a formação de preços e quantidades em "
                  "mercados competitivos. Com base na teoria da demanda e nas preferências dos agentes, julgue os "
                  "itens a seguir.")
COMANDO_TPS26 = ("Considere um consumidor com função utilidade U = x₁x₂, em que x₁ e x₂ representam, "
                 "respectivamente, as quantidades consumidas dos bens 1 e 2. Considere, ainda, que o preço do bem 1 "
                 "seja p₁ = 10, o preço do bem 2 seja p₂ = 4, o rendimento do consumidor seja r = 80 e que o "
                 "consumidor seja racional, prefira mais a menos (monotonicidade) e gaste toda a sua renda em x₁ e "
                 "x₂. Com base nessas informações, e considerando que TMS seja a taxa marginal de substituição, "
                 "julgue os itens a seguir.")
COMANDO_TELEGRAM = "Julgue o item a seguir, relativo à teoria do consumidor."

CARDS = [
    # ------------------------------------------------------------------ E1-0184
    {
        "id": "ECO-E1-0184-1", "fonte_ref": "E1-0184", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2019", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": COMANDO_UTIL,
        "rotulo_item": "Item",
        "assertiva": ("A satisfação adicional a cada unidade adicional adquirida do bem é reflexo da lei da "
                      "utilidade marginal decrescente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A <u>satisfação adicional</u> a cada unidade adicional adquirida do bem é reflexo da lei da "
                      "utilidade marginal decrescente."),
        "poucas": ("A " + azb("utilidade marginal") + " é justamente a satisfação adicional de cada nova unidade; "
                   "a lei diz que ela " + vd("diminui") + " à medida que o consumo aumenta. O gabarito foi CERTO, "
                   "mas a redação é frouxa."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O item fala em “satisfação adicional”, sem dizer que ela <b>cai</b>. Que cada unidade "
                          "extra traga satisfação positiva é consequência da " + azb("monotonicidade") + " (mais "
                          "é melhor), não da lei da utilidade marginal decrescente, que trata do <b>ritmo</b> "
                          "dessa satisfação. Professores apontaram o item como passível de recurso (anulação ou "
                          "ERRADO); a leitura da banca — “a satisfação adicional por unidade é o objeto da lei” — "
                          "prevaleceu. Na prova, aceite CERTO, mas saiba a distinção.")],
        "destrinchando": [
            azb("Utilidade total") + " (UT) é a satisfação com todo o consumo; " + azb("utilidade marginal")
            + " (UMg = ΔUT/Δq) é o acréscimo de satisfação trazido pela última unidade.",
            "A " + azb("lei da utilidade marginal decrescente") + " afirma que, mantido o resto constante, cada "
            "unidade adicional acrescenta <b>menos</b> satisfação que a anterior: o primeiro copo d’água no "
            "deserto vale muito; o quinto, pouco. A UT continua subindo enquanto UMg > 0, só que cada vez mais "
            "devagar; atinge o máximo (saciedade) quando UMg = 0.",
            "Origem histórica: a lei é associada a " + oc("Hermann Gossen") + " (1854, “primeira lei de "
            "Gossen”) e foi o pilar da " + azb("revolução marginalista") + " de " + oc("Jevons") + ", "
            + oc("Menger") + " e " + oc("Walras") + " (1871–1874). Não confundir com a lei dos "
            + azb("rendimentos decrescentes") + " de " + oc("David Ricardo") + ", que trata da <b>produção</b> "
            "(terras de fertilidade decrescente e renda da terra), não da satisfação do consumidor.",
            "Vínculo com a demanda: se cada unidade extra vale menos para o consumidor, ele só compra mais se o "
            "preço cair — eis a intuição marshalliana da curva de demanda negativamente inclinada.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item recorta a definição de utilidade marginal e "
                       "omite o adjetivo-chave (decrescente). Em CEBRASPE, “incompleto não é errado”: a banca "
                       "costuma manter CERTO quando nada do que foi dito é falso. 🔥 Itens sobre UMg costumam "
                       "trocar decrescente por constante ou crescente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A lei da utilidade marginal decrescente implica que a utilidade total diminui a cada unidade "
            "adicional consumida.”</i> → ERRADO (troca UMg por UT: a total cresce enquanto UMg > 0)",
            "<i>“Segundo a lei da utilidade marginal decrescente, a satisfação adicional proporcionada por cada "
            "unidade consumida tende a diminuir à medida que o consumo aumenta.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Atribui a “lei dos rendimentos marginais decrescentes” a David Ricardo (Princípios, "
                             "renda da terra), formalizada por Jevons. Na duplicata em imagem (E1-0213), o "
                             "professor considera o item mal redigido: satisfação adicional seria monotonicidade; "
                             "estaria certo com “satisfação adicional (decrescente)”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: professor sugere anulação/ERRADO (a satisfação adicional positiva decorre da "
                    "monotonicidade); mantido o gabarito CERTO da fonte",
                    "qualidade_fonte: o comentário de origem atribui a lei a Ricardo, que formulou os rendimentos "
                    "decrescentes da terra (produção), não a utilidade marginal decrescente (Gossen, marginalistas)",
                    "duplicata: fundido o comentário de E1-0213 (mesmo item, frente em imagem)"],
    },
    # ------------------------------------------------------------------ E1-0185
    {
        "id": "ECO-E1-0185-1", "fonte_ref": "E1-0185", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2019", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": COMANDO_UTIL,
        "rotulo_item": "Item",
        "assertiva": ("A quantidade máxima que pode ser adquirida de um bem sem reduzir a utilidade total do "
                      "consumidor, quando existe, marca um ponto de saciedade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A quantidade máxima que pode ser adquirida de um bem sem reduzir a utilidade total do "
                      "consumidor, <u>quando existe</u>, marca um ponto de saciedade."),
        "poucas": ("O " + azb("ponto de saciedade") + " é onde a utilidade total atinge o máximo (" + vd("UMg = 0")
                   + "): até ali, mais unidades não reduzem a satisfação; além dele, reduzem."),
        "destrinchando": [
            "Com UMg decrescente, a utilidade total (UT) sobe cada vez mais devagar. Se a UMg chega a zero, a UT "
            "para de crescer: esse é o " + azb("ponto de saciedade") + " (ou de “bliss”). Depois dele, UMg < 0 e "
            "cada unidade extra <b>reduz</b> a UT — o bem passa a ser um incômodo.",
            "Gráfico mental: UT em forma de morro (sobe, achata, cai); UMg é a inclinação desse morro — positiva "
            "na subida, zero no topo, negativa na descida.",
            "O “quando existe” é decisivo: em muitos bens a saciedade nunca chega no intervalo relevante (UMg "
            "decresce, mas segue positiva). É o caso que a teoria usa por padrão, com a hipótese de "
            + azb("monotonicidade") + " (mais é sempre melhor).",
            "Consequência prática: ninguém paga por unidades além da saciedade, porque elas reduziriam a "
            "satisfação. Um consumidor racional nunca escolhe ficar no trecho de UMg negativa se puder descartar "
            "o excesso.",
            vm("Regra-âncora: UMg > 0 → UT sobe; UMg = 0 → UT máxima (saciedade); UMg < 0 → UT cai."),
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " O item define saciedade por paráfrase "
                       "(“quantidade máxima sem reduzir a utilidade total”) e se protege com o “quando existe”. "
                       "A pegadinha seria trocar “utilidade total” por “utilidade marginal”: o máximo é da total; "
                       "a marginal, ali, vale zero."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No ponto de saciedade, a utilidade marginal do bem atinge seu valor máximo.”</i> → ERRADO "
            "(troca de conceito: a UMg é nula; máxima é a UT)",
            "<i>“Todo bem apresenta, necessariamente, um ponto de saciedade.”</i> → ERRADO (modulador absoluto: "
            "sob monotonicidade, não há saciedade)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["quando existe"], "dificuldade": 1,
        "comentario_fonte": ("Incrementos decrescentes de utilidade levam a um máximo além do qual unidades "
                             "adicionais têm utilidade negativa; no ponto de máxima satisfação está a saciedade."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0186
    {
        "id": "ECO-E1-0186-1", "fonte_ref": "E1-0186", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2019", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": COMANDO_UTIL,
        "rotulo_item": "Item",
        "assertiva": ("Bens que apresentam nível de quantidade a partir do qual a satisfação adicional é negativa "
                      "têm curva de demanda crescente a partir dessa quantidade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Bens que apresentam nível de quantidade a partir do qual a satisfação adicional é negativa ")
                   + vm("têm curva de demanda crescente a partir dessa quantidade") + az("."),
        "poucas": ("Além da " + azb("saciedade") + " (UMg < 0) ninguém paga por unidades extras: a demanda "
                   "<b>não</b> se estende para lá, muito menos com inclinação positiva."),
        "destrinchando": [
            "Pela lógica marshalliana, o consumidor compra até que o valor da última unidade (UMg em termos "
            "monetários) iguale o preço. Se a UMg é negativa, a disposição a pagar é negativa: a quantidade "
            "demandada a qualquer preço positivo fica <b>abaixo</b> do ponto de saciedade.",
            "Logo, o trecho de UMg negativa simplesmente não gera demanda — o consumidor para de comprar. Uma "
            "curva crescente exigiria que ele pagasse <b>mais</b> por unidades que lhe tiram satisfação: "
            "contrassenso.",
            "Demanda positivamente inclinada só aparece em casos específicos: o " + azb("bem de Giffen") + " "
            "(bem inferior com efeito renda forte o bastante para superar o efeito substituição; "
            + oc("Marshall") + " registrou o caso e o atribuiu a " + oc("Robert Giffen") + ") e os " + azb("bens de Veblen")
            + " (consumo conspícuo, " + oc("Veblen") + ", 1899). Nenhum deles tem relação com saciedade.",
            vm("Regra-âncora: UMg negativa = fim da demanda, não demanda crescente."),
        ],
        "dissecando": (cz("[nexo indevido]") + " Duas ideias verdadeiras isoladas (existe saciedade; existem "
                       "demandas crescentes) são ligadas por uma causalidade falsa. Pista: “satisfação negativa” "
                       "e “demanda crescente” apontam em sentidos opostos — quem perde satisfação não quer mais "
                       "do bem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A partir do ponto de saciedade, o consumidor não demanda unidades adicionais do bem, ainda que "
            "seu preço seja nulo.”</i> → CERTO",
            "<i>“A curva de demanda crescente caracteriza os bens inferiores.”</i> → ERRADO (generalização: só o "
            "Giffen, caso extremo de inferior)",
        ])],
        "reescrita": ("Bens que apresentam nível de quantidade a partir do qual a satisfação adicional é negativa "
                      + hl("não têm demanda além dessa quantidade, pois o consumidor deixa de adquirir unidades "
                           "adicionais") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Não há relação entre utilidade marginal decrescente e demanda positivamente "
                             "inclinada; seria contrassenso pagar mais após a saciedade. Na duplicata em imagem "
                             "(E1-0213): demanda crescente só no bem de Giffen; após a saciedade o consumidor para "
                             "de consumir."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: fundido o trecho do comentário de E1-0213 sobre o mesmo item"],
    },
    # ------------------------------------------------------------------ E1-0187
    {
        "id": "ECO-E1-0187-1", "fonte_ref": "E1-0187", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2018", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à escolha ótima do consumidor.",
        "rotulo_item": "Item",
        "assertiva": ("Caso as preferências do indivíduo sejam representadas por uma função de utilidade linear, "
                      "é possível que ele escolha não consumir um dos bens."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Caso as preferências do indivíduo sejam representadas por uma função de utilidade linear, "
                      "<u>é possível</u> que ele escolha não consumir um dos bens."),
        "poucas": ("Utilidade linear = " + azb("substitutos perfeitos") + ": a TMS é constante e, salvo "
                   "coincidência com a razão de preços, o ótimo é uma " + azb("solução de canto") + " — gasta-se "
                   "tudo num só bem."),
        "destrinchando": [
            "Com U = a·x₁ + b·x₂, as curvas de indiferença são retas de inclinação −a/b: a "
            + azb("TMS") + " = a/b não muda ao longo da curva. Não há a convexidade que leva o consumidor a "
            "diversificar.",
            "Compare a TMS com a razão de preços p₁/p₂: se " + vd("a/b > p₁/p₂") + ", cada real gasto em x₁ rende "
            "mais utilidade → só x₁; se " + vd("a/b < p₁/p₂") + " → só x₂; se forem iguais, qualquer ponto da reta "
            "orçamentária é ótimo (infinitas soluções).",
            "Por isso a regra TMS = p₁/p₂ (tangência) não vale aqui: ela pressupõe solução interior e "
            "preferências estritamente convexas. Nos cantos, a condição é de desigualdade.",
            "Exemplo: U = x₁ + x₂, p₁ = 2, p₂ = 1, renda 10. Cada unidade de x₂ custa metade e dá a mesma "
            "utilidade: compra-se " + vd("x₂ = 10, x₁ = 0") + ".",
            "Outras funções que geram canto: " + azb("quase lineares") + " (U = v(x₁) + x₂, com renda baixa) e "
            "preferências côncavas.",
        ],
        "grafico_verso": "ECO-E1-0187-1-V1",
        "dissecando": (cz("[modulador relativo]") + " O “é possível” salva o item: o canto não é obrigatório "
                       "(se a/b = p₁/p₂ há infinitas soluções, inclusive interiores), mas pode ocorrer. A banca "
                       "inverteria com “necessariamente consumirá ambos os bens”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com utilidade linear, o consumidor sempre deixará de consumir um dos bens.”</i> → ERRADO "
            "(modulador absoluto: se a TMS iguala p₁/p₂, há soluções interiores)",
            "<i>“Com utilidade Cobb-Douglas U = x₁x₂ e preços positivos, o consumidor pode optar por não "
            "consumir um dos bens.”</i> → ERRADO (na Cobb-Douglas o ótimo é sempre interior)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["é possível"], "dificuldade": 1,
        "comentario_fonte": ("Utilidade linear: curvas de indiferença retas, TMS constante; permite soluções de "
                             "canto (especialização do consumo). Remetia a figura não preservada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "00033.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0187-1-V1, gráfico didático da solução de canto)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0190
    {
        "id": "ECO-E1-0190-1", "fonte_ref": "E1-0190", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2018", "ano": 2018, "cacd": False,
        "errei": True,
        "comando": COMANDO_UTIL,
        "rotulo_item": "Item",
        "assertiva": "Um aumento no consumo de um bem pode não aumentar o nível de utilidade de um indivíduo.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um aumento no consumo de um bem <u>pode não</u> aumentar o nível de utilidade de um "
                      "indivíduo."),
        "poucas": ("A " + azb("monotonicidade") + " é uma <b>hipótese</b>, não uma lei: com saciedade, bem neutro "
                   "ou “mal”, consumir mais pode deixar a utilidade igual ou até reduzi-la."),
        "destrinchando": [
            "A hipótese de " + azb("monotonicidade") + " (“mais é melhor”) diz que mais de um bem, mantido o "
            "resto, não piora o consumidor — e, na versão estrita, sempre melhora. Ela é conveniente (curvas de "
            "indiferença negativamente inclinadas), mas não é verdade lógica.",
            "Casos em que mais consumo <b>não</b> aumenta a utilidade: (i) " + azb("saciedade") + " — passado o "
            "ponto em que UMg = 0, unidades extras não acrescentam ou até reduzem a satisfação; (ii) "
            + azb("bem neutro") + " — o consumidor é indiferente a ele (UMg = 0 sempre); (iii) "
            + azb("mal") + " (“bad”) — poluição, fumaça de cigarro: mais quantidade reduz a utilidade.",
            "Atenção: utilidade marginal <b>decrescente</b> não basta para o item ser certo. Enquanto UMg > 0, "
            "a utilidade total sobe, ainda que pouco. O que torna o item verdadeiro é a possibilidade de UMg "
            "chegar a zero ou ficar negativa.",
            vm("Regra-âncora: “pode não aumentar” é verdadeiro porque a monotonicidade é uma hipótese, que "
               "falha na saciedade, no bem neutro e no mal."),
        ],
        "dissecando": (cz("[modulador relativo · contraintuitivo]") + " Quem decorou “mais é melhor” marca "
                       "ERRADO. O “pode não” só exige um contraexemplo, e há vários. 🔥 Itens com “pode” sobre "
                       "hipóteses da teoria tendem a ser CERTOS; com “sempre”, ERRADOS."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob a hipótese de monotonicidade estrita, um aumento no consumo de um bem pode não aumentar a "
            "utilidade do indivíduo.”</i> → ERRADO (a monotonicidade estrita garante que a utilidade aumenta)",
            "<i>“Um aumento no consumo de um bem sempre aumenta a utilidade, ainda que a taxas decrescentes.”</i> "
            "→ ERRADO (modulador absoluto: falha na saciedade e no bem neutro)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "CONTRAINTUITIVO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("Item testa a monotonicidade; pela lei dos rendimentos marginais decrescentes, pode-se "
                             "atingir a saciedade, a partir da qual a UMg fica negativa e a utilidade total cai."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem chama de “lei dos rendimentos marginais decrescentes” "
                    "(conceito da produção) o que é a utilidade marginal decrescente"],
    },
    # ------------------------------------------------------------------ E1-0191
    {
        "id": "ECO-E1-0191-1", "fonte_ref": "E1-0191", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à escolha ótima do consumidor.",
        "rotulo_item": "Item",
        "assertiva": ("Um ponto de escolha ótima é aquele onde a taxa marginal de substituição entre dois bens é "
                      "estritamente superior aos seus preços relativos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um ponto de escolha ótima é aquele onde a taxa marginal de substituição entre dois bens é ")
                   + vm("estritamente superior aos") + az(" seus preços relativos."),
        "poucas": ("No ótimo interior com preferências convexas, a " + azb("TMS é igual") + " à razão de preços "
                   "(" + vd("TMS = p₁/p₂") + "): a curva de indiferença tangencia a reta orçamentária."),
        "destrinchando": [
            "A " + azb("TMS") + " (TMS₁₂ = UMg₁/UMg₂, em valor absoluto) é quanto de x₂ o consumidor "
            "<b>aceita</b> ceder por mais uma unidade de x₁; a razão de preços p₁/p₂ é quanto de x₂ o "
            "<b>mercado exige</b> por essa unidade. No ótimo, a valoração subjetiva iguala a objetiva.",
            "Se " + vd("TMS > p₁/p₂") + ", o consumidor valoriza x₁ (o bem do eixo horizontal) mais do que o "
            "mercado cobra: trocar x₂ por x₁ eleva a utilidade — ele ainda não está no ótimo e deve consumir "
            "<b>mais x₁</b>. Se TMS < p₁/p₂, o raciocínio se inverte (mais x₂).",
            "Formulação equivalente — " + azb("equimarginalidade") + ": UMg₁/p₁ = UMg₂/p₂. O último real gasto "
            "em cada bem rende a mesma utilidade.",
            "Exceção: em " + azb("soluções de canto") + " (substitutos perfeitos, quase lineares), o ótimo pode "
            "ter TMS ≠ p₁/p₂ — por exemplo, TMS > p₁/p₂ com x₂ = 0. Mas aí a desigualdade decorre da "
            "impossibilidade de consumir menos que zero, e não define o ótimo em geral.",
            vm("Regra-âncora: ótimo interior → TMS = p₁/p₂ (tangência); qualquer desigualdade indica que "
               "ainda dá para melhorar."),
        ],
        "dissecando": (cz("[dado alterado · troca de conceito]") + " O item troca o sinal da condição "
                       "(igual → “estritamente superior”). O advérbio “estritamente” é o gatilho: exclui a "
                       "igualdade, que é justamente a resposta. A banca também cobra a versão com “inferior” "
                       "no lugar de “igual”, igualmente ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em uma solução interior, o ótimo do consumidor iguala a razão das utilidades marginais à razão "
            "dos preços.”</i> → CERTO",
            "<i>“Se a TMS for superior à razão de preços, o consumidor eleva sua utilidade consumindo menos do "
            "bem representado no eixo horizontal.”</i> → ERRADO (inversão: deve consumir mais dele)",
        ])],
        "reescrita": ("Um ponto de escolha ótima é aquele onde a taxa marginal de substituição entre dois bens é "
                      + hl("igual aos") + " seus preços relativos."),
        "tipo_erro": ["DADO_ALTERADO", "TROCA_CONCEITO"], "moduladores": ["estritamente"], "dificuldade": 1,
        "comentario_fonte": ("Ótimo: TMS igual aos preços relativos. Afirma que, se TMS > preços relativos, o "
                             "consumidor valoriza mais o bem do eixo vertical e deveria consumir mais dele."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: com TMS₁₂ = UMg₁/UMg₂ > p₁/p₂, o consumidor valoriza relativamente mais o "
                    "bem do eixo horizontal (x₁) e deve consumir mais dele; o comentário de origem diz o "
                    "contrário (eixo vertical) — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0195
    {
        "id": "ECO-E1-0195-1", "fonte_ref": "E1-0195", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Simulado Clipping", "prova": "07/2023", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": COMANDO_UTIL,
        "rotulo_item": "Item",
        "assertiva": ("A utilidade marginal constante é um conceito fundamental na teoria do consumidor, que "
                      "indica que a satisfação adicional obtida com o consumo de uma unidade adicional de um bem "
                      "ou serviço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A utilidade marginal ") + vm("constante") + az(" é um conceito fundamental na teoria do "
                      "consumidor, que indica que a satisfação adicional obtida com o consumo de uma unidade "
                      "adicional de um bem ou serviço") + vm(" [...]") + az("."),
        "poucas": ("O pilar da teoria do consumidor é a utilidade marginal " + azb("decrescente") + ": cada "
                   "unidade adicional acrescenta <b>menos</b> satisfação que a anterior."),
        "destrinchando": [
            azb("Utilidade marginal") + " (UMg) = acréscimo de utilidade total gerado por uma unidade a mais do "
            "bem. A hipótese padrão é que ela " + vd("decresce") + " com o consumo — a "
            + azb("lei da utilidade marginal decrescente") + " (" + oc("Gossen") + ", 1854; revolução "
            "marginalista de " + oc("Jevons") + ", " + oc("Menger") + " e " + oc("Walras") + ", 1871–1874).",
            "Por que importa: (i) explica a demanda negativamente inclinada (unidades extras valem menos, então "
            "só se compram mais a preço menor); (ii) fundamenta o " + azb("princípio equimarginal")
            + " (UMg₁/p₁ = UMg₂/p₂) e a diversificação do consumo; (iii) resolve o "
            + azb("paradoxo da água e do diamante") + ": a água tem enorme utilidade total, mas UMg baixa "
            "porque é abundante.",
            "UMg constante não é impossível — aparece, por exemplo, na utilidade linear (substitutos perfeitos) "
            "—, mas é caso particular, não o “conceito fundamental”.",
            "Na abordagem ordinal moderna, fala-se mais em " + azb("TMS decrescente") + " (convexidade das "
            "preferências), que não depende de medir a utilidade; a UMg decrescente é a versão cardinal da "
            "mesma intuição.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca “decrescente” por “constante” numa frase de "
                       "definição; o restante é paráfrase de manual. A frase vem truncada na fonte (falta o "
                       "verbo depois de “satisfação adicional obtida…”), mas o julgamento decorre da troca do "
                       "adjetivo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A utilidade marginal decrescente indica que a utilidade total do consumidor diminui a cada "
            "unidade adicional consumida.”</i> → ERRADO (troca UMg por UT)",
            "<i>“Se a utilidade marginal de um bem for constante, cada unidade adicional proporcionará o mesmo "
            "acréscimo de satisfação, independentemente da quantidade já consumida.”</i> → CERTO",
        ])],
        "reescrita": ("A utilidade marginal " + hl("decrescente") + " é um conceito fundamental na teoria do "
                      "consumidor, que indica que a satisfação adicional obtida com o consumo de uma unidade "
                      "adicional de um bem ou serviço " + hl("diminui à medida que o consumo aumenta") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A utilidade marginal não é constante, é decrescente: o acréscimo de satisfação de "
                             "cada unidade adicional diminui, podendo chegar a nulo ou negativo; pilar da teoria "
                             "da demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: a assertiva da fonte está truncada (falta o predicado após “satisfação "
                    "adicional obtida…”); mantida fiel"],
    },
    # ------------------------------------------------------------------ E1-0196
    {
        "id": "ECO-E1-0196-1", "fonte_ref": "E1-0196", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Simulado Clipping", "prova": "07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos fundamentos da teoria do consumidor.",
        "rotulo_item": "Item",
        "assertiva": ("A teoria do consumidor se baseia na suposição de que os indivíduos são racionais e "
                      "maximizam sua utilidade, mas essa abordagem tem sido criticada por negligenciar fatores "
                      "psicológicos e sociais que influenciam as escolhas de consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria do consumidor se baseia na suposição de que os indivíduos são racionais e "
                      "maximizam sua utilidade, mas essa abordagem <u>tem sido criticada</u> por negligenciar "
                      "fatores psicológicos e sociais que influenciam as escolhas de consumo."),
        "poucas": ("O núcleo neoclássico é o " + azb("consumidor racional maximizador") + "; a "
                   + azb("economia comportamental") + " e abordagens sociológicas o criticam por ignorar vieses, "
                   "hábitos e influências sociais."),
        "destrinchando": [
            "Hipóteses do modelo padrão: preferências completas, transitivas e monotônicas; o consumidor conhece "
            "preços e renda e escolhe a cesta que maximiza a utilidade sujeita ao orçamento. É um modelo "
            "deliberadamente simplificado, avaliado pela capacidade de previsão.",
            "Críticas psicológicas — " + azb("economia comportamental") + ": " + oc("Herbert Simon")
            + " (" + azb("racionalidade limitada") + ", Nobel de 1978); " + oc("Kahneman") + " e "
            + oc("Tversky") + " (teoria do prospecto, 1979: aversão à perda, efeito enquadramento; Nobel de "
            "Kahneman em 2002); " + oc("Richard Thaler") + " (contabilidade mental, <i>nudges</i>; Nobel de 2017).",
            "Críticas sociais: " + oc("Veblen") + " (<i>A teoria da classe ociosa</i>, 1899: consumo conspícuo, "
            "em que o preço alto aumenta o desejo) e " + oc("Duesenberry") + " (hipótese da renda relativa: o "
            "consumo depende do padrão do grupo de referência, com efeito-demonstração).",
            "Resposta neoclássica: o modelo não pretende descrever a psicologia de cada pessoa, mas prever "
            "comportamentos agregados; parte das anomalias foi incorporada (preferências dependentes de "
            "referência, desconto hiperbólico).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de panorama, sem armadilha técnica: descreve a hipótese "
                       "central e a crítica, sem afirmar que a crítica derrubou o modelo. Ficaria ERRADO com um "
                       "absoluto (“a teoria ignora completamente…”, “foi abandonada”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As críticas da economia comportamental levaram ao abandono da hipótese de maximização da "
            "utilidade na microeconomia contemporânea.”</i> → ERRADO (extrapolação: o modelo segue como "
            "referência)",
            "<i>“O conceito de racionalidade limitada, de Herbert Simon, questiona a capacidade dos agentes de "
            "processar toda a informação relevante para suas decisões.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["tem sido"], "dificuldade": 1,
        "comentario_fonte": "Verdadeiro; abordagem criticada pelos behavioristas, que incluem aspectos psicológicos, "
                            "sociais e comportamentais.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0198
    {
        "id": "ECO-E1-0198-1", "fonte_ref": "E1-0198", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Simulado Clipping", "prova": "07/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos fundamentos da teoria do consumidor.",
        "rotulo_item": "Item",
        "assertiva": ("A teoria do consumidor pode ser aplicada não apenas para entender as escolhas individuais "
                      "de consumo, mas também para analisar o comportamento de mercado e o impacto de políticas "
                      "públicas sobre o bem-estar dos consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria do consumidor <u>pode</u> ser aplicada não apenas para entender as escolhas "
                      "individuais de consumo, mas também para analisar o comportamento de mercado e o impacto "
                      "de políticas públicas sobre o bem-estar dos consumidores."),
        "poucas": ("Da escolha individual derivam-se a " + azb("demanda de mercado") + " (soma horizontal) e as "
                   "medidas de " + azb("bem-estar") + " (excedente do consumidor, variações compensatória e "
                   "equivalente) usadas para avaliar políticas."),
        "destrinchando": [
            "Do indivíduo ao mercado: a maximização da utilidade gera a demanda individual; somando "
            "horizontalmente as demandas de todos os consumidores, obtém-se a " + azb("demanda de mercado")
            + ", que, cruzada com a oferta, determina preços e quantidades.",
            "Bem-estar: o " + azb("excedente do consumidor") + " (área sob a demanda e acima do preço) e as "
            "medidas de " + oc("Hicks") + " — " + azb("variação compensatória") + " e "
            + azb("variação equivalente") + " — quantificam quanto um consumidor ganha ou perde com mudanças de "
            "preço.",
            "Aplicações a políticas públicas: incidência de impostos e subsídios; comparação entre transferência "
            "em dinheiro e em espécie (o dinheiro nunca deixa o beneficiário pior, pela teoria da escolha); "
            "viés de substituição dos índices de preços (o IPC de Laspeyres superestima o custo de vida).",
            "Exemplos " + rx("brasileiros") + ": avaliação do Bolsa Família como transferência monetária e "
            "efeitos de desonerações da cesta básica sobre o bem-estar das famílias.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Afirmação abrangente, salva pelo "
                       "“pode”. Itens de “alcance da teoria” são quase sempre CERTOS; viram ERRADOS quando "
                       "restringem (“aplica-se apenas às escolhas individuais”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A teoria do consumidor aplica-se apenas à explicação de escolhas individuais, não servindo à "
            "análise de bem-estar.”</i> → ERRADO (restrição indevida)",
            "<i>“A curva de demanda de mercado é obtida pela soma vertical das demandas individuais.”</i> → "
            "ERRADO (a soma é horizontal; a vertical é a dos bens públicos)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode", "não apenas"],
        "dificuldade": 1,
        "comentario_fonte": "Apenas “É verdade”.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0200
    {
        "id": "ECO-E1-0200-1", "fonte_ref": "E1-0200", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_TELEGRAM,
        "rotulo_item": "Item",
        "assertiva": ("O axioma fraco da preferência revelada é um dos critérios que precisa ser satisfeito para "
                      "garantir que o consumidor seja consistente com suas preferências. Se uma cesta de bens A "
                      "for escolhida em detrimento de outra cesta B quando ambos forem acessíveis, o consumidor "
                      "revela que prefere A em relação a B."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O axioma fraco da preferência revelada é um dos critérios que precisa ser satisfeito para "
                      "garantir que o consumidor seja consistente com suas preferências. Se uma cesta de bens A "
                      "for escolhida em detrimento de outra cesta B <u>quando ambos forem acessíveis</u>, o "
                      "consumidor revela que prefere A em relação a B."),
        "poucas": ("Escolher A quando B também cabia no orçamento = A é " + azb("revelada preferida") + " a B. O "
                   + azb("axioma fraco") + " exige coerência: se A é revelada preferida a B, B nunca pode ser "
                   "revelada preferida a A."),
        "destrinchando": [
            "A " + azb("teoria da preferência revelada") + " (" + oc("Paul Samuelson") + ", 1938) parte do "
            "que se observa — escolhas e orçamentos — em vez de supor uma função utilidade.",
            "Definição: se o consumidor escolhe A quando B também era acessível (p·B ≤ p·A, ao preço vigente), "
            "então A é " + azb("diretamente revelada preferida") + " a B. É exatamente a segunda frase do item.",
            azb("Axioma fraco (AFrPR)") + ": se A é revelada preferida a B (A ≠ B), então, em nenhuma outra "
            "situação, B pode ser escolhida quando A for acessível. Violação: escolher A com B disponível hoje "
            "e B com A disponível amanhã — inconsistência.",
            azb("Axioma forte (AFoPR)") + " (" + oc("Houthakker") + ", 1950): estende a regra às cadeias "
            "indiretas (A ≻ B ≻ C ⇒ não C ≻ A) — é a versão “transitiva” e garante que as escolhas podem ser "
            "racionalizadas por preferências bem-comportadas.",
            "Uso prático: testar se dados de consumo são compatíveis com maximização e comparar bem-estar "
            "(se a cesta nova era acessível antes e não foi escolhida, o consumidor não está melhor).",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A condição “quando ambos forem acessíveis” é o "
                       "detalhe que sustenta o item: escolher A quando B era inacessível nada revela. A banca "
                       "inverteria trocando fraco por forte ou removendo a acessibilidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o consumidor escolhe A quando B não lhe era acessível, ele revela que prefere A a B.”</i> → "
            "ERRADO (sem acessibilidade de B, nada se revela)",
            "<i>“O axioma forte da preferência revelada acrescenta ao fraco a exigência de consistência nas "
            "relações indiretas, análoga à transitividade.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Apenas o gabarito (CERTO), uma imagem não preservada e link para o canal do Telegram.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (50).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; comentário escrito do zero)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0201
    {
        "id": "ECO-E1-0201-1", "fonte_ref": "E1-0201", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_TELEGRAM,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria da utilidade ordinal não se podem colocar ponderações nas diferenças "
                      "absolutas quanto à utilidade de um conjunto de bens associado com outro conjunto, mas "
                      "apenas é possível fazer comparações relativas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a teoria da utilidade ordinal não se podem colocar ponderações nas diferenças "
                      "absolutas quanto à utilidade de um conjunto de bens associado com outro conjunto, mas "
                      "<u>apenas</u> é possível fazer comparações relativas."),
        "poucas": ("Na " + azb("utilidade ordinal") + " os números só <b>ordenam</b> cestas (A melhor que B); a "
                   "distância entre eles não tem significado — isso seria utilidade " + azb("cardinal") + "."),
        "destrinchando": [
            azb("Utilidade cardinal") + " (marginalistas do século XIX): supõe que a satisfação é mensurável em "
            "“útiles”, de modo que faz sentido dizer que A dá o dobro da satisfação de B ou comparar diferenças "
            "de utilidade.",
            azb("Utilidade ordinal") + " (" + oc("Pareto") + "; " + oc("Hicks") + " e " + oc("Allen")
            + ", 1934): basta saber se A ≻ B, A ∼ B ou B ≻ A. A função utilidade é só um índice: qualquer "
            + azb("transformação monotônica crescente") + " (multiplicar por 2, elevar ao quadrado, tirar log) "
            "representa as mesmas preferências.",
            "Exemplo: U = x₁x₂ e V = ln x₁ + ln x₂ ordenam as cestas da mesma forma e geram a mesma demanda; "
            "por isso “quanto” uma cesta é melhor não tem resposta na teoria ordinal.",
            "O que sobrevive à ordinalidade: curvas de indiferença, TMS e escolha ótima. O que não sobrevive: "
            "UMg decrescente como propriedade (depende da escala escolhida) e comparações interpessoais de "
            "utilidade.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Redação truncada (“ponderações nas diferenças absolutas”), "
                       "mas fiel à definição. O “apenas” não torna o item absoluto indevido — ordenar é, de fato, "
                       "tudo o que a ordinal permite. A banca também cobra a utilidade como “medida objetiva”, que "
                       "é ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na abordagem ordinal, se U(A) = 20 e U(B) = 10, pode-se afirmar que a cesta A proporciona o "
            "dobro da satisfação de B.”</i> → ERRADO (isso é leitura cardinal)",
            "<i>“Uma transformação monotônica crescente de uma função utilidade representa as mesmas "
            "preferências.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Ordinal só ordena cestas; cardinal quantifica diferenças de utilidade, imprecisas "
                             "para o consumidor; “cardinal é usada para firmas/produtores”. Link para material da UAL."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0202
    {
        "id": "ECO-E1-0202-1", "fonte_ref": "E1-0202", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_TELEGRAM,
        "rotulo_item": "Item",
        "assertiva": ("A preferência do consumidor é representada pela utilidade: De acordo com a teoria do "
                      "consumidor, as preferências dos consumidores são expressas em termos de utilidade. A "
                      "utilidade é uma medida objetiva de satisfação ou benefício que os consumidores atribuem "
                      "aos diferentes bens e serviços que consomem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A preferência do consumidor é representada pela utilidade: De acordo com a teoria do "
                      "consumidor, as preferências dos consumidores são expressas em termos de utilidade. A "
                      "utilidade é uma medida ") + vm("objetiva") + az(" de satisfação ou benefício que os "
                      "consumidores atribuem aos diferentes bens e serviços que consomem."),
        "poucas": ("A utilidade é " + azb("subjetiva") + " (cada um atribui a sua) e, na teoria moderna, "
                   + azb("ordinal") + ": só ordena cestas, não mede satisfação de forma objetiva."),
        "destrinchando": [
            "A primeira parte está certa: a função utilidade é a forma de <b>representar</b> preferências — "
            "atribui números maiores às cestas preferidas. Exige preferências completas, transitivas e "
            "contínuas (teorema de " + oc("Debreu") + ").",
            "O erro é “objetiva”: o valor que um bem tem para alguém depende dos gostos dessa pessoa. É a "
            "herança da " + azb("teoria subjetiva do valor") + " dos marginalistas, em oposição à teoria do "
            "valor-trabalho dos clássicos.",
            "Além de subjetiva, a utilidade relevante é " + azb("ordinal") + ": qualquer transformação monotônica "
            "crescente de U representa as mesmas preferências. Não existe uma unidade de medida da satisfação.",
            "Consequência: não se fazem " + azb("comparações interpessoais") + " de utilidade — não dá para "
            "dizer que R$ 100 trazem mais satisfação a um pobre que a um rico só com a teoria ordinal; isso "
            "exige juízos normativos adicionais (ex.: funções de bem-estar social).",
            vm("Regra-âncora: utilidade = índice subjetivo e ordinal das preferências, não medida objetiva."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Duas frases corretas de abertura e o erro "
                       "enxertado no adjetivo final (“objetiva”). Pista: “que os consumidores <b>atribuem</b>” "
                       "já denuncia a subjetividade. A versão que diz que a utilidade ordinal só permite comparações "
                       "relativas, sem ponderar diferenças absolutas, é CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A utilidade é uma medida subjetiva e, na abordagem ordinal, serve apenas para ordenar as cestas "
            "de bens.”</i> → CERTO",
            "<i>“A teoria ordinal permite comparar a satisfação de consumidores diferentes.”</i> → ERRADO (não "
            "há comparação interpessoal)",
        ])],
        "reescrita": ("[...] A utilidade é uma medida " + hl("subjetiva") + " de satisfação ou benefício que os "
                      "consumidores atribuem aos diferentes bens e serviços que consomem."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas o gabarito (ERRADO) e uma imagem não preservada.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (51).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; comentário escrito do zero)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0206
    {
        "id": "ECO-E1-0206-1", "fonte_ref": "E1-0206", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "MP/ENAP/Economista/2015", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": "Com relação à teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "As curvas de indiferença são côncavas em relação à origem no espaço de bens.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As curvas de indiferença são ") + vm("côncavas") + az(" em relação à origem no espaço de "
                                                                            "bens."),
        "poucas": ("Com preferências bem-comportadas, as curvas de indiferença são " + azb("convexas")
                   + " em relação à origem: a " + azb("TMS é decrescente") + " — o consumidor prefere cestas "
                   "diversificadas a cestas extremas."),
        "destrinchando": [
            azb("Espaço de bens") + " é o quadrante (x₁, x₂ ≥ 0) em que cada ponto é uma cesta; nele se desenha "
            "o " + azb("mapa de indiferença") + ".",
            "Formato padrão, de duas hipóteses: " + azb("monotonicidade") + " → inclinação negativa (para "
            "manter a utilidade, mais de um bem exige menos do outro); " + azb("convexidade") + " → curva "
            "“arqueada para dentro”, voltada para a origem, com TMS decrescente: quem tem muito x₂ e pouco x₁ "
            "aceita ceder muito x₂ por uma unidade de x₁; à medida que x₁ aumenta, aceita ceder cada vez menos.",
            "Convexidade significa que " + vd("médias são preferidas a extremos") + ": a cesta (5, 5) é ao "
            "menos tão boa quanto (10, 0) ou (0, 10), se estas forem indiferentes entre si.",
            "Convexidade é <b>hipótese</b>, não definição: preferências côncavas existem (quem prefere só "
            "cerveja ou só vinho, nunca misturar) e levam a soluções de canto. Casos-limite: substitutos "
            "perfeitos (retas, convexidade fraca) e complementares perfeitos (L).",
            vm("Regra-âncora: bem-comportada = monotônica + convexa → curva decrescente e convexa em relação à "
               "origem."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca “convexas” por “côncavas” — par de antônimos "
                       "que a banca adora, porque a curva convexa “parece côncava” para quem olha de cima. "
                       "Lembre-se: o referencial é a origem; a barriga aponta para ela."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Curvas de indiferença convexas em relação à origem implicam taxa marginal de substituição "
            "decrescente.”</i> → CERTO",
            "<i>“A fronteira de possibilidades de produção é tipicamente convexa em relação à origem.”</i> → "
            "ERRADO (a FPP é côncava: custo de oportunidade crescente)",
        ])],
        "reescrita": "As curvas de indiferença são " + hl("convexas") + " em relação à origem no espaço de bens.",
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Curvas de indiferença são convexas (decrescentes) “por definição”; espaço de bens é "
                             "a área dos eixos onde se representa o mapa de indiferença. Imagem não preservada."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (55).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (formato descrito no 📖)"}],
        "alertas": ["qualidade_fonte: a convexidade é hipótese das preferências bem-comportadas, não definição "
                    "de curva de indiferença — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0207
    {
        "id": "ECO-E1-0207-1", "fonte_ref": "E1-0207", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TC/RO/ACE – Economia/2013", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": "Com relação à teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": "Curva de indiferença de dois bens substitutos perfeitos é uma reta.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Curva de indiferença de dois bens <u>substitutos perfeitos</u> é uma reta."),
        "poucas": ("Substitutos perfeitos trocam-se a uma " + azb("taxa constante") + " (U = a·x₁ + b·x₂): a "
                   "TMS = a/b não varia e a curva de indiferença é uma reta de inclinação −a/b."),
        "destrinchando": [
            azb("Substitutos perfeitos") + ": o consumidor só se importa com o total “equivalente” dos dois bens. "
            "Exemplo clássico: lápis azul e lápis vermelho (1:1), ou garrafa de 2 litros × duas de 1 litro (1:2).",
            "Função utilidade: " + vd("U = a·x₁ + b·x₂") + ". Curva de indiferença: x₂ = U/b − (a/b)·x₁ — "
            "reta. TMS = UMg₁/UMg₂ = a/b, " + azb("constante") + " ao longo da curva.",
            "Consequência na escolha: compara-se a/b com p₁/p₂ e, em regra, o ótimo é de " + azb("canto")
            + " (só o bem relativamente mais barato); se a/b = p₁/p₂, qualquer cesta da reta orçamentária serve.",
            "Galeria dos formatos: retas → substitutos perfeitos; " + azb("L") + " → complementares perfeitos "
            "(U = min{a·x₁, b·x₂}); convexas suaves → caso usual (Cobb-Douglas); horizontais ou verticais → um "
            "dos bens é neutro.",
            "Para não confundir com a demanda: substitutos “comuns” (café e chá) têm elasticidade-preço cruzada "
            "positiva, mas curvas de indiferença convexas — só os <b>perfeitos</b> geram retas.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, sem armadilha. A banca costuma trocar o "
                       "par: “complementares perfeitos → reta” (ERRADO) ou “substitutos perfeitos → L” (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de indiferença de dois bens complementares perfeitos é uma reta negativamente "
            "inclinada.”</i> → ERRADO (troca de conceito: é um L)",
            "<i>“Para substitutos perfeitos, a taxa marginal de substituição é decrescente.”</i> → ERRADO (é "
            "constante)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas “CORRETO” e uma imagem não preservada.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (56).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (formato descrito no 📖; gráfico análogo em ECO-E1-0187-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0208
    {
        "id": "ECO-E1-0208-1", "fonte_ref": "E1-0208", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/AL/Analista Judiciário – Economia/2012", "ano": 2012,
        "cacd": False, "errei": True,
        "comando": "Com relação à teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Se um indivíduo gosta de um bem e é neutro em relação a outro, então a curva de indiferença "
                      "será uma linha paralela ao eixo do bem neutro."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um indivíduo gosta de um bem e é neutro em relação a outro, então a curva de indiferença "
                      "será uma linha <u>paralela ao eixo do bem neutro</u>."),
        "poucas": ("Com um bem " + azb("neutro") + ", a utilidade depende só do bem desejado: mudar a quantidade "
                   "do neutro não altera a utilidade, então a curva corre " + vd("paralela ao eixo do neutro")
                   + " (perpendicular ao eixo do bem desejado)."),
        "destrinchando": [
            azb("Bem neutro") + ": o consumidor não se importa com ele — UMg = 0. Exemplo: creme de barbear para "
            "quem não tem barba. Diferente do " + azb("mal") + " (“bad”), que <b>reduz</b> a utilidade (fumaça de "
            "cigarro para um não fumante).",
            "Se x₁ é neutro e x₂ desejado, U = f(x₂). Uma curva de indiferença fixa x₂ e deixa x₁ livre: no plano "
            "(x₁ na horizontal, x₂ na vertical), é uma reta " + vd("horizontal") + " — paralela ao eixo de x₁, "
            "o neutro.",
            "As curvas mais altas (mais x₂) representam mais utilidade; andar para a direita (mais x₁) não muda "
            "nada.",
            "Comparação: com um " + azb("mal") + " no eixo horizontal, as curvas ficam " + vd("positivamente "
            "inclinadas") + " — para aceitar mais do mal, o consumidor exige mais do bem.",
            vm("Regra-âncora: bem neutro → curva paralela ao eixo do neutro; mal → curva crescente."),
        ],
        "grafico_verso": "ECO-E1-0208-1-V1",
        "dissecando": (cz("[detalhe · contraintuitivo]") + " A armadilha é de geometria: “paralela ao eixo do "
                       "neutro” soa como se o neutro “mandasse” na curva. Faça o teste: mudar o neutro deve "
                       "manter a utilidade — logo a curva se estende <b>na direção</b> do eixo do neutro. "
                       "Trocar por “paralela ao eixo do bem desejado” tornaria o item ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se um indivíduo gosta de um bem e é neutro em relação a outro, a curva de indiferença será "
            "paralela ao eixo do bem de que ele gosta.”</i> → ERRADO (eixo trocado)",
            "<i>“Se um dos bens for um mal, as curvas de indiferença serão positivamente inclinadas.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Distingue mal (bem cuja presença reduz a utilidade, ex.: fumaça de cigarro) e bem "
                             "neutro (indiferença absoluta, ex.: creme de barbear para quem não tem barba); as "
                             "curvas são perpendiculares ao eixo do “bem normal”. Três imagens não preservadas."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (57).png, image (58).png, image (63).png", "tipo_fonte": "GRÁFICO",
                           "lado": "verso", "acao": "redesenhadas em ECO-E1-0208-1-V1 (gráfico didático)"}],
        "alertas": ["qualidade_fonte: o comentário de origem chama de “bem normal” o bem desejado; “normal” é "
                    "classificação pela elasticidade-renda — corrigido para “bem desejado”"],
    },
    # ------------------------------------------------------------------ E1-0209
    {
        "id": "ECO-E1-0209-1", "fonte_ref": "E1-0209", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "MP/ENAP/Economista/2015", "ano": 2015, "cacd": False,
        "errei": True,
        "comando": "Com relação à teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Se o consumidor sempre tomar uma xícara de café adoçado com uma colher de açúcar, então as "
                      "curvas de indiferença do consumidor apresentarão o formato de linhas retas no espaço de "
                      "bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o consumidor sempre tomar uma xícara de café adoçado com uma colher de açúcar, então as "
                      "curvas de indiferença do consumidor apresentarão o formato de ") + vm("linhas retas")
                   + az(" no espaço de bens."),
        "poucas": ("Café e açúcar em proporção fixa (1:1) são " + azb("complementares perfeitos")
                   + ": U = min(x₁, x₂), e as curvas de indiferença têm formato de " + vd("L") + ", não de reta."),
        "destrinchando": [
            azb("Complementares perfeitos") + " são consumidos em proporção fixa: uma xícara de café só vale com "
            "uma colher de açúcar; café ou açúcar a mais, sozinhos, não acrescentam nada. Função "
            + vd("U = min{x₁, x₂}") + " (em geral, min{a·x₁, b·x₂}, a " + azb("Leontief") + ").",
            "Geometria: a partir do vértice (x₁ = x₂), aumentar só um bem mantém a utilidade → trecho horizontal "
            "e trecho vertical: um " + azb("L") + ". Os vértices ficam sobre o raio x₂ = x₁. A TMS é infinita "
            "no ramo vertical, zero no horizontal e indefinida no vértice.",
            "Escolha ótima: sempre no vértice. Com p₁, p₂ e renda m, x₁ = x₂ = " + vd("m/(p₁ + p₂)") + ". Não há "
            "efeito substituição — mudança de preço só produz efeito renda.",
            "Linhas retas corresponderiam a " + azb("substitutos perfeitos") + " (U = a·x₁ + b·x₂), o caso oposto: "
            "taxa de troca constante, e não proporção fixa.",
            vm("Regra-âncora: substituto perfeito → reta; complementar perfeito → L."),
        ],
        "grafico_verso": "ECO-E1-0209-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O enunciado descreve corretamente o caso de complementares "
                       "perfeitos (“sempre … com uma colher”) e cola o formato de substitutos perfeitos. Pista: "
                       "“sempre” + proporção fixa = L. 🔥 CEBRASPE repete o par reta × L com frequência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o consumidor sempre tomar uma xícara de café com uma colher de açúcar, suas curvas de "
            "indiferença terão formato de L, com vértices sobre a reta x₂ = x₁.”</i> → CERTO",
            "<i>“Para complementares perfeitos, uma variação de preço gera apenas efeito substituição.”</i> → "
            "ERRADO (inversão: só efeito renda; o de substituição é nulo)",
        ])],
        "reescrita": ("Se o consumidor sempre tomar uma xícara de café adoçado com uma colher de açúcar, então as "
                      "curvas de indiferença do consumidor apresentarão o formato de " + hl("L (ângulo reto)")
                      + " no espaço de bens."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Bens complementares, consumidos juntos: a curva de indiferença é um “L”, não reta.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (65).png", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada em ECO-E1-0209-1-V1 (gráfico didático)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0215
    {
        "id": "ECO-E1-0215-1", "fonte_ref": "E1-0215", "destino": "04", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às funções de demanda do consumidor.",
        "rotulo_item": "Item",
        "assertiva": ("Na função Walrasiana ou Marshaliana a quantidade demandada é função do preço de um bem e "
                      "da renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na função Walrasiana ou Marshaliana a quantidade demandada é função do <u>preço</u> de um "
                      "bem e da <u>renda</u>."),
        "poucas": ("A " + azb("demanda marshalliana") + " (ou walrasiana), x(p, m), resulta de maximizar a "
                   "utilidade dada a renda: depende dos " + vd("preços") + " e da " + vd("renda")
                   + " — e não do nível de utilidade, como a hicksiana."),
        "destrinchando": [
            "Problema de " + oc("Marshall") + "/" + oc("Walras") + ": max U(x₁, x₂) sujeito a p₁x₁ + p₂x₂ = m. "
            "A solução é a " + azb("demanda marshalliana") + " xᵢ = xᵢ(p₁, p₂, m): preço próprio, preço dos "
            "outros bens e renda nominal.",
            "Contraponto: a " + azb("demanda hicksiana") + " (compensada) vem de minimizar o gasto para atingir "
            "uma utilidade dada: hᵢ = hᵢ(p₁, p₂, U). Depende de preços e <b>utilidade</b>, não da renda — por "
            "isso isola o efeito substituição.",
            "A marshalliana é " + azb("homogênea de grau zero") + " em preços e renda: multiplicar todos os "
            "preços e a renda pelo mesmo fator não muda a escolha (ausência de ilusão monetária). Daí a ideia "
            "de que importam os " + vd("preços relativos") + " e a renda real.",
            "Exemplo Cobb-Douglas U = x₁x₂: x₁ = m/(2p₁), x₂ = m/(2p₂) — preço próprio e renda.",
            "Ponte entre as duas: a " + azb("equação de Slutsky") + " decompõe a variação da demanda "
            "marshalliana em efeito substituição (hicksiana) e efeito renda.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Formulação simplificada (“do preço de um bem e da "
                       "renda”): a forma completa inclui os demais preços, mas incompleto não é errado. A "
                       "pegadinha clássica é trocar renda por utilidade, o que descreveria a hicksiana."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na função de demanda marshalliana, a quantidade demandada depende dos preços e do nível de "
            "utilidade do consumidor.”</i> → ERRADO (troca de conceito: isso é a hicksiana)",
            "<i>“A demanda marshalliana é homogênea de grau zero nos preços e na renda.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A demanda walrasiana/marshalliana expressa a quantidade como função dos preços e da "
                             "renda; ênfase nos preços relativos, não absolutos. Imagem não preservada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (50).jpeg", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; conteúdo coberto no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0229
    {
        "id": "ECO-E1-0229-1", "fonte_ref": "E1-0229", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": COMANDO_TELEGRAM,
        "rotulo_item": "Item",
        "assertiva": ("A Taxa Marginal de Substituição indica a taxa a que um consumidor está disposto a trocar um "
                      "determinado bem por outro de forma a manter o mesmo nível de utilidade. Num mapa de curvas "
                      "de indiferença, e para cada combinação de bens x e y, a Taxa Marginal de Substituição é "
                      "dada pela inclinação da curva de indiferença."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Taxa Marginal de Substituição indica a taxa a que um consumidor está disposto a trocar um "
                      "determinado bem por outro de forma a <u>manter o mesmo nível de utilidade</u>. Num mapa de "
                      "curvas de indiferença, e para cada combinação de bens x e y, a Taxa Marginal de "
                      "Substituição é dada pela <u>inclinação da curva de indiferença</u>."),
        "poucas": ("A " + azb("TMS") + " é a taxa de troca que mantém a utilidade — geometricamente, a "
                   "inclinação (em módulo) da curva de indiferença naquele ponto: " + vd("TMS = −dy/dx = "
                   "UMgₓ/UMgᵧ") + "."),
        "destrinchando": [
            "Definição: quanto de y o consumidor aceita ceder por uma unidade adicional de x, permanecendo na "
            "mesma curva de indiferença. Como a curva é o lugar das cestas de mesma utilidade, essa taxa é a "
            + azb("inclinação da curva") + " em cada ponto.",
            "Por que UMgₓ/UMgᵧ: ao longo da curva, dU = UMgₓ·dx + UMgᵧ·dy = 0 → −dy/dx = UMgₓ/UMgᵧ.",
            "Sinal: com bens desejáveis a inclinação é negativa; por convenção, a TMS é tratada em "
            + azb("valor absoluto") + " (ou definida com o sinal de menos). Itens CEBRASPE aceitam “dada pela "
            "inclinação” sem a ressalva.",
            azb("TMS decrescente") + " = curvas convexas: quanto mais x se tem, menos y se aceita ceder por uma "
            "unidade extra de x. Na reta (substitutos perfeitos) é constante; no L (complementares perfeitos), "
            "infinita ou zero.",
            "No ótimo interior, a inclinação da curva iguala a da reta orçamentária: " + vd("TMS = pₓ/pᵧ") + ".",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual em duas frases. A banca costuma errar a TMS "
                       "trocando a referência (“mantendo a renda constante” em vez da utilidade) ou a curva "
                       "(“inclinação da reta orçamentária” como definição)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A taxa marginal de substituição mede a taxa à qual o consumidor troca um bem por outro mantendo "
            "constante a sua renda.”</i> → ERRADO (troca de conceito: mantém-se a utilidade)",
            "<i>“A taxa marginal de substituição corresponde à razão entre as utilidades marginais dos dois "
            "bens.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas o gabarito (CERTO) e link para o canal do Telegram.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0432
    {
        "id": "ECO-E1-0432-1", "fonte_ref": "E1-0432", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COMANDO_CLIP25,
        "rotulo_item": "Item",
        "assertiva": ("A condição de equilíbrio do consumidor em uma situação de convexidade das preferências "
                      "ocorre quando a taxa marginal de substituição entre dois bens é inferior ao preço relativo "
                      "entre esses bens."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A condição de equilíbrio do consumidor em uma situação de convexidade das preferências "
                      "ocorre quando a taxa marginal de substituição entre dois bens é ") + vm("inferior ao")
                   + az(" preço relativo entre esses bens."),
        "poucas": ("Com preferências convexas, o ótimo (interior) é a " + azb("tangência") + " entre a curva de "
                   "indiferença mais alta e a reta orçamentária: " + vd("TMS = p₁/p₂") + ", e não TMS menor."),
        "destrinchando": [
            "A " + azb("convexidade") + " garante que a tangência é um máximo (e não um mínimo) e que ele é "
            "único quando a convexidade é estrita. Por isso a condição de primeira ordem — "
            + vd("TMS₁₂ = UMg₁/UMg₂ = p₁/p₂") + " — caracteriza o equilíbrio.",
            "Leitura econômica: a TMS é a taxa à qual o consumidor <b>quer</b> trocar; p₁/p₂ é a taxa à qual o "
            "mercado <b>permite</b> trocar. Se TMS < p₁/p₂, x₁ vale menos para ele do que custa: vender x₁ "
            "(comprar menos) e comprar x₂ eleva a utilidade. O ponto ainda não é ótimo.",
            "Se TMS > p₁/p₂, o ajuste é o inverso: comprar mais x₁. Só na igualdade não há troca vantajosa.",
            "Formulação equivalente: " + vd("UMg₁/p₁ = UMg₂/p₂") + " — o último real gasto rende a mesma "
            "utilidade em qualquer bem.",
            "Exceção sem convexidade estrita: substitutos perfeitos e preferências côncavas levam a soluções de "
            "canto, em que a desigualdade pode subsistir.",
        ],
        "dissecando": (cz("[dado alterado]") + " Troca “igual” por “inferior”. A menção à convexidade é isca "
                       "de sofisticação: ela reforça que a solução é de tangência, ou seja, de igualdade. A banca "
                       "recicla a construção em outros simulados, inclusive com “estritamente superior” no lugar "
                       "de “igual” — sempre ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com preferências convexas e solução interior, no ótimo a TMS iguala a razão entre os preços dos "
            "bens.”</i> → CERTO",
            "<i>“Se a TMS for inferior ao preço relativo, o consumidor aumenta sua utilidade comprando mais do "
            "bem 1.”</i> → ERRADO (inversão: deve comprar menos do bem 1)",
        ])],
        "reescrita": ("A condição de equilíbrio do consumidor em uma situação de convexidade das preferências "
                      "ocorre quando a taxa marginal de substituição entre dois bens é " + hl("igual ao")
                      + " preço relativo entre esses bens."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Ótimo do consumidor: TMS igual à razão de preços; curva de indiferença mais alta "
                             "tangencia a reta orçamentária (comentário idêntico na duplicata E1-0534)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: fundido o comentário da duplicata E1-0534",
                    "quase_duplicata: ECO-E1-0687-1 (mesma construção, Simuladão Clipping Março/2026)"],
    },
    # ------------------------------------------------------------------ E1-0433
    {
        "id": "ECO-E1-0433-1", "fonte_ref": "E1-0433", "destino": "04", "subtema": H2["ro"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COMANDO_CLIP25,
        "rotulo_item": "Item",
        "assertiva": ("A restrição orçamentária representa todas as combinações de bens que um consumidor pode "
                      "adquirir, sendo modificada apenas quando há variação da renda nominal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A restrição orçamentária representa todas as combinações de bens que um consumidor pode "
                      "adquirir, sendo modificada ") + vm("apenas quando há variação da renda nominal") + az("."),
        "poucas": ("A reta orçamentária " + vd("p₁x₁ + p₂x₂ = m") + " muda com a " + azb("renda")
                   + " (deslocamento paralelo) <b>e</b> com os " + azb("preços") + " (giro, mudança de "
                   "inclinação)."),
        "destrinchando": [
            "Elementos da reta: interceptos " + vd("m/p₁") + " (tudo em x₁) e " + vd("m/p₂") + " (tudo em x₂); "
            "inclinação " + vd("−p₁/p₂") + " (custo de oportunidade de x₁ em unidades de x₂). O "
            + azb("conjunto orçamentário") + " inclui a reta e a área abaixo dela.",
            "Variação da renda m (preços fixos): " + azb("deslocamento paralelo") + " — para fora se m sobe, "
            "para dentro se cai. A inclinação não muda.",
            "Variação de um preço: a reta " + azb("gira") + " em torno do intercepto do outro bem. Se p₁ cai, o "
            "intercepto m/p₁ se afasta e a reta fica menos inclinada.",
            "Variação proporcional de todos os preços: equivale a uma variação da renda real — p e m "
            "multiplicados pelo mesmo fator deixam a reta intacta (homogeneidade de grau zero).",
            "Outras mudanças: impostos e subsídios específicos alteram o preço efetivo (giro); "
            "racionamento ou impostos sobre quantidades acima de um limite criam “quebras” na reta.",
        ],
        "dissecando": (cz("[restrição indevida]") + " O “apenas” elimina os preços como causa de mudança. "
                       "Pista: a própria definição (combinações que se <b>pode adquirir</b>) depende dos preços. "
                       "🔥 “Apenas”/“somente” em itens de teoria quase sempre sinaliza ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução do preço de um dos bens provoca um giro da reta orçamentária, que se torna menos "
            "inclinada se o bem barateado estiver no eixo horizontal.”</i> → CERTO",
            "<i>“Um aumento da renda nominal altera a inclinação da reta orçamentária.”</i> → ERRADO (troca de "
            "conceito: desloca paralelamente)",
        ])],
        "reescrita": ("A restrição orçamentária representa todas as combinações de bens que um consumidor pode "
                      "adquirir, sendo modificada " + hl("tanto por variações da renda nominal quanto por "
                                                         "variações dos preços dos bens") + "."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Muda com a renda (deslocamento paralelo) e com os preços (mudança de inclinação) "
                             "(comentário idêntico na duplicata E1-0535)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: fundido o comentário da duplicata E1-0535"],
    },
    # ------------------------------------------------------------------ E1-0434
    {
        "id": "ECO-E1-0434-1", "fonte_ref": "E1-0434", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COMANDO_CLIP25,
        "rotulo_item": "Item",
        "assertiva": ("O axioma da transitividade das preferências garante que, se um consumidor prefere A a B e "
                      "B a C, ele também preferirá A a C, conferindo consistência às escolhas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O axioma da transitividade das preferências garante que, se um consumidor prefere A a B e "
                      "B a C, ele também preferirá A a C, conferindo consistência às escolhas."),
        "poucas": ("É a definição de " + azb("transitividade") + ": A ≻ B e B ≻ C ⇒ " + vd("A ≻ C")
                   + ". Sem ela, as preferências seriam circulares e não haveria escolha “melhor”."),
        "destrinchando": [
            "Axiomas das preferências racionais: " + azb("completude") + " (toda cesta é comparável: A ≿ B, "
            "B ≿ A ou ambos), " + azb("reflexividade") + " (A ≿ A) e " + azb("transitividade") + " (A ≿ B e "
            "B ≿ C ⇒ A ≿ C). Completude + transitividade = racionalidade.",
            "Hipóteses adicionais, de “bom comportamento”: " + azb("monotonicidade") + " (mais é melhor), "
            + azb("convexidade") + " (médias preferidas a extremos) e " + azb("continuidade") + " (necessária "
            "para haver função utilidade).",
            "Por que a transitividade importa: com A ≻ B ≻ C ≻ A não existe cesta “melhor” e o consumidor "
            "poderia ser explorado indefinidamente — o argumento da " + azb("bomba de dinheiro") + " (ele paga "
            "para trocar C por B, B por A, A por C…).",
            "Consequência gráfica: curvas de indiferença " + vd("não se cruzam") + ". Se se cruzassem, a "
            "transitividade (junto com a monotonicidade) seria violada.",
            "Crítica empírica: há violações observadas em laboratório (efeitos de enquadramento), estudadas pela "
            "economia comportamental — mas, na teoria, a transitividade é axioma.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição pura. A banca costuma trocar o nome do axioma "
                       "(atribuir “mais é melhor” à transitividade, que é ERRADO) ou inverter a "
                       "conclusão (“C preferida a A”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O axioma da completude garante que, se A é preferida a B e B a C, então A é preferida a C.”</i> "
            "→ ERRADO (troca de conceito: isso é transitividade)",
            "<i>“Se as preferências forem transitivas e monotônicas, as curvas de indiferença não se "
            "cruzam.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Transitividade é axioma da escolha racional: preferências lógicas, não circulares, "
                             "permitem ordenar cestas (comentário idêntico na duplicata E1-0536)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: fundido o comentário da duplicata E1-0536",
                    "quase_duplicata: ECO-E1-0688-1 (mesmo conteúdo, Simuladão Clipping Março/2026)"],
    },
    # ------------------------------------------------------------------ E1-0632
    {
        "id": "ECO-E1-0632-1", "fonte_ref": "E1-0632", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Set/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Acerca das preferências do consumidor, julgue o item a seguir.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("A propriedade da transitividade das preferências estabelece que o consumidor sempre prefere "
                      "mais a menos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A propriedade da ") + vm("transitividade") + az(" das preferências estabelece que o "
                                                                     "consumidor sempre prefere mais a menos."),
        "poucas": ("“Preferir mais a menos” é a " + azb("monotonicidade") + ". A " + azb("transitividade")
                   + " trata da coerência entre comparações: A ≻ B e B ≻ C ⇒ A ≻ C."),
        "destrinchando": [
            azb("Transitividade") + " — axioma de racionalidade: impede preferências circulares e permite "
            "ordenar todas as cestas. Não diz nada sobre quantidades.",
            azb("Monotonicidade") + " — hipótese de “bom comportamento”: se a cesta A tem ao menos tanto de cada "
            "bem que B e mais de algum, A é preferida (versão estrita) ou ao menos tão boa (versão fraca). É "
            "ela que gera curvas de indiferença " + vd("negativamente inclinadas") + " e curvas mais afastadas "
            "da origem com " + vd("mais utilidade") + ".",
            "Ela falha com saciedade, bem neutro e mal — por isso é hipótese, não axioma de racionalidade.",
            "Mapa rápido: completude e transitividade → racionalidade; monotonicidade → inclinação negativa; "
            "convexidade → curvatura (TMS decrescente); continuidade → existência de função utilidade.",
            vm("Regra-âncora: “mais é melhor” = monotonicidade; “coerência A-B-C” = transitividade."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui à transitividade o conteúdo da monotonicidade. "
                       "Itens sobre axiomas costumam trocar nome e definição entre os vizinhos da lista; "
                       "memorize o par nome → frase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A hipótese de monotonicidade estabelece que o consumidor prefere mais a menos.”</i> → CERTO",
            "<i>“A transitividade garante que as curvas de indiferença sejam convexas.”</i> → ERRADO (troca de "
            "conceito: convexidade é outra hipótese)",
        ])],
        "reescrita": ("A propriedade da " + hl("monotonicidade") + " das preferências estabelece que o consumidor "
                      "sempre prefere mais a menos."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("Preferir mais a menos é monotonicidade; não tem relação com a transitividade."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (178).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto reconstruído pelo comentário"}],
        "alertas": ["texto_reconstruido: frente original era imagem (image (178).png); assertiva reconstruída a "
                    "partir do comentário, que refuta a atribuição de “preferir mais a menos” à transitividade; "
                    "redação exata não preservada"],
    },
    # ------------------------------------------------------------------ E1-0633
    {
        "id": "ECO-E1-0633-1", "fonte_ref": "E1-0633", "destino": "04", "subtema": H2["dem"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Set/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Acerca da demanda do consumidor, julgue o item a seguir.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("Ao longo da curva de demanda individual há diferentes níveis de utilidade associados, "
                      "mantidos constantes a renda e os preços dos demais bens."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ao longo da curva de demanda individual há <u>diferentes níveis de utilidade</u> "
                      "associados, mantidos constantes a renda e os preços dos demais bens."),
        "poucas": ("Na demanda " + azb("marshalliana") + " (renda fixa), cada preço gera uma cesta ótima numa "
                   "curva de indiferença diferente: preço mais alto → " + vd("utilidade menor") + ". A utilidade "
                   "só é constante ao longo da " + azb("hicksiana") + "."),
        "destrinchando": [
            "Derivação: fixe renda e preço de y; varie p<sub>x</sub>. A reta orçamentária gira e o ótimo percorre "
            "a " + azb("curva preço-consumo") + ", tocando curvas de indiferença diferentes. Cada par (p<sub>x</sub>, "
            "x*) vira um ponto da demanda.",
            "Se p<sub>x</sub> sobe, o conjunto orçamentário encolhe e o consumidor vai para uma curva de "
            "indiferença mais baixa: " + vd("utilidade decresce com o preço") + " ao longo da demanda ordinária.",
            "A " + azb("demanda hicksiana") + " (compensada) faz o oposto: ajusta a renda para manter a "
            "utilidade fixa. Ela capta só o " + azb("efeito substituição") + "; a marshalliana capta "
            "substituição + renda (equação de " + oc("Slutsky") + ").",
            "Para bens normais, a hicksiana é mais inclinada (menos sensível ao preço) que a marshalliana, pois "
            "esta soma o efeito renda no mesmo sentido.",
            vm("Regra-âncora: marshalliana → renda constante, utilidade varia; hicksiana → utilidade constante, "
               "renda compensada."),
        ],
        "dissecando": (cz("[detalhe]") + " O item testa se o candidato confunde as "
                       "duas demandas. A versão ERRADA diria “mesmo nível de utilidade ao longo da curva de "
                       "demanda ordinária”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao longo da curva de demanda marshalliana, o nível de utilidade do consumidor permanece "
            "constante.”</i> → ERRADO (troca de conceito: isso é a hicksiana)",
            "<i>“A curva de demanda compensada de Hicks reflete apenas o efeito substituição.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Ao longo da curva de demanda há diferentes utilidades; o nível de utilidade decresce "
                             "à medida que o preço aumenta, com renda e preço dos outros bens constantes."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (182).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto reconstruído pelo comentário"}],
        "alertas": ["texto_reconstruido: frente original era imagem (image (182).png); assertiva reconstruída a "
                    "partir do comentário, que a reafirma (utilidades diferentes ao longo da demanda, com renda e "
                    "outros preços constantes); redação exata não preservada"],
    },
    # ------------------------------------------------------------------ E1-0687
    {
        "id": "ECO-E1-0687-1", "fonte_ref": "E1-0687", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Com base na teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A condição de equilíbrio do consumidor exige que a taxa marginal de substituição entre dois "
                      "bens seja inferior ao preço relativo, pois apenas nesse ponto o consumidor terá esgotado "
                      "todas as possibilidades de ganho de utilidade dentro da restrição orçamentária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A condição de equilíbrio do consumidor exige que a taxa marginal de substituição entre dois "
                      "bens seja ") + vm("inferior ao") + az(" preço relativo, pois apenas nesse ponto o "
                      "consumidor terá esgotado todas as possibilidades de ganho de utilidade dentro da restrição "
                      "orçamentária."),
        "poucas": ("O equilíbrio exige " + vd("TMS = p₁/p₂") + ". Com TMS inferior ao preço relativo ainda há "
                   "ganho a explorar (comprar menos x₁ e mais x₂) — o oposto de “esgotado”."),
        "destrinchando": [
            "A justificativa do item (“esgotar as possibilidades de ganho de utilidade”) está correta — é "
            "exatamente a ideia de ótimo. O problema é que ela só vale na " + azb("igualdade") + ".",
            "Teste numérico: TMS = 1 e p₁/p₂ = 2. O consumidor aceita trocar 1 unidade de x₁ por 1 de x₂; o "
            "mercado paga 2 unidades de x₂ por 1 de x₁. Vendendo uma unidade de x₁ ele obtém 2 de x₂ e precisa "
            "só de 1 para ficar igual: ganha 1 unidade de x₂ “de graça”. O ponto não é ótimo.",
            "A trajetória de ajuste continua até que a TMS (que cresce à medida que x₁ fica escasso, pela "
            "convexidade) alcance 2 = p₁/p₂ — a " + azb("tangência") + ".",
            "Geometria: TMS ≠ p₁/p₂ significa que a curva de indiferença <b>corta</b> a reta orçamentária; "
            "há cestas acessíveis em curvas mais altas. Só na tangência não há.",
            vm("Regra-âncora: ótimo interior ⇔ TMS = p₁/p₂ ⇔ UMg₁/p₁ = UMg₂/p₂."),
        ],
        "dissecando": (cz("[dado alterado · meia-verdade]") + " Construção recorrente nos simulados Clipping: "
                       "troca “igual” por “inferior” e cola uma justificativa verdadeira para dar "
                       "credibilidade. Pista: “esgotado todas as possibilidades” só combina com igualdade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A condição de equilíbrio do consumidor exige que a TMS seja igual ao preço relativo, pois apenas "
            "nesse ponto o consumidor terá esgotado as possibilidades de ganho de utilidade dentro da "
            "restrição orçamentária.”</i> → CERTO",
            "<i>“Se a TMS for inferior ao preço relativo, o consumidor pode aumentar sua utilidade reduzindo o "
            "consumo do bem 1.”</i> → CERTO",
        ])],
        "reescrita": ("A condição de equilíbrio do consumidor exige que a taxa marginal de substituição entre dois "
                      "bens seja " + hl("igual ao") + " preço relativo, pois apenas nesse ponto o consumidor terá "
                      "esgotado todas as possibilidades de ganho de utilidade dentro da restrição orçamentária."),
        "tipo_erro": ["DADO_ALTERADO", "MEIA_VERDADE"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Equilíbrio: TMS = Px/Py, inclinação da curva de indiferença igual à da reta "
                             "orçamentária; com TMS inferior ou superior, o consumidor ainda poderia realocar."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0432-1 (mesma construção, Simuladão Clipping Julho/2025)"],
    },
    # ------------------------------------------------------------------ E1-0688
    {
        "id": "ECO-E1-0688-1", "fonte_ref": "E1-0688", "destino": "04", "subtema": H2["pref"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Com base na teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O axioma da transitividade das preferências assegura coerência interna às escolhas do "
                      "consumidor, pois, se ele prefere a cesta A à cesta B e prefere B à C, deverá "
                      "necessariamente preferir A à C, sob pena de violar a racionalidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O axioma da transitividade das preferências assegura coerência interna às escolhas do "
                      "consumidor, pois, se ele prefere a cesta A à cesta B e prefere B à C, deverá "
                      "<u>necessariamente</u> preferir A à C, sob pena de violar a racionalidade."),
        "poucas": ("Na teoria, " + azb("racionalidade") + " = preferências completas e " + azb("transitivas")
                   + ". Violar a transitividade é, por definição, ser irracional — daí o “necessariamente”."),
        "destrinchando": [
            "O “necessariamente” não é absoluto indevido: a transitividade é um <b>axioma</b>, logo a conclusão "
            "A ≻ C decorre por definição. Fora do modelo pode haver violações; dentro dele, não.",
            "Argumento da " + azb("bomba de dinheiro") + " (“money pump”): quem tem A ≻ B ≻ C ≻ A aceita pagar "
            "um centavo para trocar C por B, outro para B por A e outro para A por C — e volta ao início mais "
            "pobre, indefinidamente.",
            "Manuais de referência — " + oc("Varian") + " (<i>Microeconomia intermediária</i>) e " + oc("Pindyck")
            + " & " + oc("Rubinfeld") + " (<i>Microeconomia</i>) — listam completude e transitividade entre as "
            "hipóteses básicas sobre preferências; Pindyck acrescenta “mais é melhor”.",
            "Implicação gráfica: curvas de indiferença não se cruzam; e só preferências completas, transitivas "
            "(e contínuas) podem ser representadas por uma função utilidade.",
            "Contraponto empírico: violações de transitividade em escolhas sob incerteza e com enquadramentos "
            "diferentes (" + oc("Tversky") + ", 1969) alimentam a economia comportamental.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Quem decorou que “necessariamente” é sinal de "
                       "ERRADO cai. Aqui o advérbio só explicita que a conclusão é lógica, dada a premissa do "
                       "axioma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O axioma da transitividade assegura que o consumidor sempre prefere mais a menos.”</i> → ERRADO "
            "(troca de conceito: monotonicidade)",
            "<i>“Se as preferências não forem transitivas, não é possível representá-las por uma função "
            "utilidade.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": ("Segundo Varian e Pindyck & Rubinfeld, a transitividade é pilar da teoria da "
                             "preferência; impede ciclos (“bomba de dinheiro”) e é essencial à racionalidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0434-1 (mesmo conteúdo, Simuladão Clipping Julho/2025)"],
    },
    # ------------------------------------------------------------------ E1-0689
    {
        "id": "ECO-E1-0689-1", "fonte_ref": "E1-0689", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Com base na teoria do consumidor, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Curvas de indiferença mais elevadas no espaço de consumo representam níveis menores de "
                      "utilidade quando se assume utilidade marginal decrescente, dado que o consumidor valoriza "
                      "menos unidades adicionais de cada bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Curvas de indiferença mais elevadas no espaço de consumo representam níveis ")
                   + vm("menores") + az(" de utilidade quando se assume utilidade marginal decrescente, ")
                   + vm("dado que o consumidor valoriza") + az(" menos unidades adicionais de cada bem."),
        "poucas": ("Pela " + azb("monotonicidade") + ", curvas mais afastadas da origem = " + vd("mais utilidade")
                   + ". UMg decrescente só faz a utilidade crescer mais devagar; enquanto UMg > 0, ela cresce."),
        "destrinchando": [
            "Curvas mais altas contêm cestas com mais de ambos os bens (ou mais de um sem menos do outro). Com "
            + azb("monotonicidade") + ", essas cestas são preferidas: o " + azb("mapa de indiferença") + " cresce "
            "para nordeste.",
            "O item confunde " + azb("utilidade marginal") + " com " + azb("utilidade total") + ". UMg "
            "decrescente significa que cada unidade extra acrescenta menos, mas ainda acrescenta: a UT sobe, "
            "a taxas decrescentes. UT só cairia com UMg negativa (além da saciedade).",
            "Exemplo: U = √x — UMg = 1/(2√x) cai sempre, mas U(4) = 2 < U(9) = 3: mais consumo, mais utilidade.",
            "Na abordagem ordinal, o que dá a curvatura das curvas é a " + azb("TMS decrescente") + " "
            "(convexidade), não a UMg; e a ordem das curvas vem da monotonicidade.",
            vm("Regra-âncora: UMg decrescente ≠ utilidade decrescente."),
        ],
        "dissecando": (cz("[nexo indevido · inversão]") + " A premissa (UMg decrescente) é verdadeira; a "
                       "conclusão (curvas mais altas = menos utilidade) não decorre dela e inverte a ordem do "
                       "mapa. O “dado que” costura o nexo falso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob monotonicidade, curvas de indiferença mais afastadas da origem representam níveis maiores "
            "de utilidade, ainda que a utilidade marginal seja decrescente.”</i> → CERTO",
            "<i>“Utilidade marginal decrescente implica utilidade total decrescente.”</i> → ERRADO (troca UMg por "
            "UT)",
        ])],
        "reescrita": ("Curvas de indiferença mais elevadas no espaço de consumo representam níveis "
                      + hl("maiores") + " de utilidade quando se assume utilidade marginal decrescente, "
                      + hl("embora o consumidor valorize") + " menos unidades adicionais de cada bem."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Monotonicidade: curvas mais afastadas = maior utilidade; UMg decrescente só faz a "
                             "utilidade total crescer a taxas menores, enquanto UMg > 0."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0807
    {
        "id": "ECO-E1-0807-1", "fonte_ref": "E1-0807", "destino": "04", "subtema": H2["util"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": COMANDO_TPS26,
        "rotulo_item": "Item",
        "assertiva": "A função em questão é do tipo Cobb-Douglas.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função em questão é do tipo <u>Cobb-Douglas</u>."),
        "poucas": ("U = x₁x₂ é o caso " + vd("A = 1, α = β = 1") + " da " + azb("Cobb-Douglas")
                   + " U = A·x₁<sup>α</sup>x₂<sup>β</sup>."),
        "destrinchando": [
            "Forma geral: " + vd("U = A·x₁<sup>α</sup>·x₂<sup>β</sup>") + ", com A, α, β > 0. Nome herdado da "
            "função de produção de " + oc("Charles Cobb") + " e " + oc("Paul Douglas") + " (1928).",
            "Propriedades no consumo: curvas de indiferença " + azb("convexas") + " e assintóticas aos eixos "
            "(nunca há solução de canto com preços positivos); " + vd("TMS₁₂ = (α/β)·(x₂/x₁)") + ", decrescente.",
            "Demandas: o consumidor gasta frações fixas da renda — " + vd("x₁ = [α/(α+β)]·r/p₁") + " e "
            + vd("x₂ = [β/(α+β)]·r/p₂") + ". Aqui, metade da renda em cada bem: x₁ = 40/10 = 4 e x₂ = 40/4 = 10.",
            "Consequências: elasticidade-preço própria = −1 (gasto constante com o bem), elasticidade-renda = 1 "
            "(bens normais) e elasticidade cruzada = 0 (bens independentes).",
            "A soma α + β = 2 não importa no consumo: como a utilidade é ordinal, U = x₁x₂ e √(x₁x₂) "
            "representam as mesmas preferências. Rendimentos de escala só têm sentido na produção.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de reconhecimento de forma funcional, porta de entrada do "
                       "bloco 191–193 do TPS 2026. A pegadinha possível seria confundir com substitutos "
                       "perfeitos (soma) ou complementares perfeitos (mínimo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como os expoentes somam 2, a utilidade apresenta rendimentos crescentes de escala, o que altera "
            "a escolha ótima do consumidor.”</i> → ERRADO (utilidade ordinal: transformação monotônica não muda "
            "a escolha)",
            "<i>“Com essa função, o consumidor gasta metade de sua renda em cada bem, quaisquer que sejam os "
            "preços.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas o gabarito (CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0808
    {
        "id": "ECO-E1-0808-1", "fonte_ref": "E1-0808", "destino": "04", "subtema": H2["ro"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": True,
        "comando": COMANDO_TPS26,
        "rotulo_item": "Item",
        "assertiva": ("Se ambos os preços forem multiplicados por 2, passando-se a p'₁ = 20 e p'₂ = 8, com a renda "
                      "mantida em r = 80, o vetor de demanda ótima (x₁*, x₂*) permanecerá o mesmo, pois a "
                      "restrição orçamentária se deslocará paralelamente, sem alterar-se a solução de "
                      "maximização de utilidade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se ambos os preços forem multiplicados por 2, passando-se a p'₁ = 20 e p'₂ = 8, com a renda "
                      "mantida em r = 80, o vetor de demanda ótima (x₁*, x₂*) ") + vm("permanecerá o mesmo")
                   + az(", pois a restrição orçamentária se deslocará paralelamente, ")
                   + vm("sem alterar-se a solução de maximização de utilidade") + az("."),
        "poucas": ("Dobrar os preços com renda fixa = " + azb("cortar a renda real pela metade") + ": a reta se "
                   "desloca paralelamente <b>para dentro</b> e o ótimo cai de " + vd("(4; 10)") + " para "
                   + vd("(2; 5)") + "."),
        "destrinchando": [
            "Reta original: 10x₁ + 4x₂ = 80 (interceptos 8 e 20). Nova: 20x₁ + 8x₂ = 80, ou seja, "
            "10x₁ + 4x₂ = 40 (interceptos 4 e 10). A inclinação p₁/p₂ = " + vd("2,5") + " não muda — o "
            "deslocamento é de fato <b>paralelo</b>, mas para dentro.",
            "Com Cobb-Douglas U = x₁x₂, gasta-se metade da renda em cada bem: x₁* = 40/20 = " + vd("2") + " e "
            "x₂* = 40/8 = " + vd("5") + ". A utilidade cai de 40 para 10.",
            "O que manteria o ótimo: multiplicar " + azb("preços e renda") + " pelo mesmo fator (p' = 2p e "
            "r' = 160). É a " + azb("homogeneidade de grau zero") + " da demanda marshalliana — ausência de "
            "ilusão monetária.",
            "Generalização: mudar todos os preços na mesma proporção, com renda fixa, equivale a uma variação "
            "da " + azb("renda real") + " (deslocamento paralelo); mudar preços relativos gira a reta.",
            vm("Regra-âncora: deslocamento paralelo da reta = mudança de renda real → muda o ótimo; só p e r "
               "juntos na mesma proporção o preservam."),
        ],
        "grafico_verso": "ECO-E1-0808-1-V1",
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A premissa geométrica é verdadeira (deslocamento "
                       "paralelo, preços relativos intactos); o erro é concluir que o ótimo não muda — confunde "
                       "“mesma inclinação” com “mesma reta”. Quem lembra da homogeneidade de grau zero sem "
                       "conferir se a renda também dobrou cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se os preços e a renda forem multiplicados por 2, o vetor de demanda ótima permanecerá "
            "(4, 10).”</i> → CERTO",
            "<i>“Com p'₁ = 20, p'₂ = 8 e r = 80, a restrição orçamentária gira em torno do intercepto do bem "
            "2.”</i> → ERRADO (desloca-se paralelamente: os preços relativos não mudaram)",
        ])],
        "reescrita": ("Se ambos os preços forem multiplicados por 2, passando-se a p'₁ = 20 e p'₂ = 8, com a renda "
                      "mantida em r = 80, o vetor de demanda ótima (x₁*, x₂*) " + hl("passará de (4, 10) para "
                                                                                    "(2, 5)") + ", pois a "
                      "restrição orçamentária se deslocará paralelamente" + hl(" para dentro, reduzindo-se a "
                                                                             "renda real à metade") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Apenas o gabarito (ERRADO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0809
    {
        "id": "ECO-E1-0809-1", "fonte_ref": "E1-0809", "destino": "04", "subtema": H2["otimo"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": COMANDO_TPS26,
        "rotulo_item": "Item",
        "assertiva": ("O consumo ótimo é dado por (x₁*, x₂*) = (4, 10), obtido no ponto em que a TMS₁₂ é igual à "
                      "razão entre os preços p₁/p₂, sujeito à restrição orçamentária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O consumo ótimo é dado por (x₁*, x₂*) = <u>(4, 10)</u>, obtido no ponto em que a TMS₁₂ é "
                      "igual à razão entre os preços p₁/p₂, sujeito à restrição orçamentária."),
        "poucas": ("TMS₁₂ = x₂/x₁ = p₁/p₂ = 2,5 → " + vd("x₂ = 2,5x₁") + "; na restrição 10x₁ + 4(2,5x₁) = 80 "
                   "→ " + vd("x₁ = 4, x₂ = 10") + "."),
        "destrinchando": [
            "Passo 1 — " + azb("TMS") + ": UMg₁ = x₂ e UMg₂ = x₁, logo TMS₁₂ = UMg₁/UMg₂ = " + vd("x₂/x₁") + ".",
            "Passo 2 — " + azb("tangência") + ": x₂/x₁ = p₁/p₂ = 10/4 = 2,5 → x₂ = 2,5x₁.",
            "Passo 3 — " + azb("restrição orçamentária") + ": 10x₁ + 4·(2,5x₁) = 80 → 20x₁ = 80 → "
            + vd("x₁* = 4") + "; " + vd("x₂* = 10") + ". Confere: 10·4 + 4·10 = 80 ✓. Utilidade: U = 40.",
            "Atalho Cobb-Douglas: com expoentes iguais, metade da renda em cada bem — x₁ = 40/p₁ = 4 e "
            "x₂ = 40/p₂ = 10. Gasto: 40 em cada bem.",
            "Por que a tangência basta: a Cobb-Douglas tem curvas convexas e assintóticas aos eixos, então o "
            "ótimo é interior e único; a condição de primeira ordem é também suficiente.",
            "Armadilha de ordem: (x₁, x₂) = (10, 4) inverteria os bens — custaria 10·10 + 4·4 = 116 > 80, fora "
            "do orçamento.",
        ],
        "grafico_verso": "ECO-E1-0809-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " Item de cálculo com o método descrito corretamente. "
                       "A banca poderia errar o par ordenado ((10, 4)), a razão (p₂/p₁) ou o método (TMS maior "
                       "que a razão de preços). Conferir sempre a restrição: o ponto precisa esgotar a renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O consumo ótimo é (x₁*, x₂*) = (10, 4).”</i> → ERRADO (bens invertidos: gasto de 116 > 80)",
            "<i>“No ótimo, o consumidor gasta a mesma quantia com cada um dos bens.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Apenas o gabarito (CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
]
