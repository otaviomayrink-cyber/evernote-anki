"""Cards do lote de redação 26 — ECO, passada 02 (nota 55: teorias do consumo e do investimento)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "cons": "🛒 Teorias do consumo",
    "inv": "🏗️ Teorias do investimento",
}

CMD_NAB_1 = "No que se refere às teorias do consumo e do investimento, julgue (C ou E) os itens subsequentes."

CMD_NAB_2 = "A respeito do conceito de equivalência ricardiana e das teorias do consumo, julgue os itens a seguir."

CMD_RT_1 = ("Acerca da relação entre poupança e investimento e dos modelos de crescimento econômico, julgue as "
            "afirmações.")

CMD_RT_2 = "A respeito das relações entre consumo, poupança e crescimento econômico, julgue os itens a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01002
    {
        "id": "ECO-E2-L01002-1", "fonte_ref": "E2-L01002", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_1,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o Modelo do Ciclo da Vida, uma política que transfira renda de consumidores "
                      "mais jovens para consumidores mais velhos aumentaria a poupança agregada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o Modelo do Ciclo da Vida, uma política que transfira renda de consumidores "
                       "mais jovens para consumidores mais velhos ") + vm("aumentaria") + az(" a poupança agregada.")),
        "poucas": ("No " + azb("ciclo da vida") + ", quem está em idade ativa poupa e o idoso " + azb("despoupa")
                   + ": tirar renda de quem poupa para dar a quem consome o patrimônio <b>reduz</b> a poupança "
                   "agregada."),
        "destrinchando": [
            azb("Hipótese do ciclo da vida") + " (" + oc("Franco Modigliani") + ", com " + oc("Richard Brumberg")
            + ", anos 1950; depois com " + oc("Albert Ando") + "): o consumidor planeja o consumo para a vida "
            "inteira e quer mantê-lo <b>estável</b>, embora a renda do trabalho siga uma corcova — baixa no "
            "início da carreira, máxima na meia-idade, nula na aposentadoria.",
            "Daí o perfil de poupança: o jovem toma crédito (despoupa) contra a renda futura; o adulto em idade "
            "ativa paga as dívidas e acumula patrimônio; o aposentado vive desse patrimônio (despoupa). A "
            + azb("taxa de poupança") + " do idoso é baixa ou negativa; a do adulto ativo, alta.",
            "A poupança agregada é a soma das poupanças das coortes. Transferir R$ 1 de quem poupa uma fração alta "
            "da renda para quem tem propensão a consumir próxima de 1 (ou acima dela) faz cair a soma: "
            + vd("S agregada ↓") + ".",
            "Corolários de manual: (i) a poupança agregada depende da <b>estrutura etária</b> — população que "
            "envelhece tende a poupar menos; (ii) um sistema previdenciário de " + azb("repartição") + " (o ativo "
            "paga o benefício do inativo) é exatamente esse tipo de transferência e tende a reduzir a poupança "
            "privada; (iii) crescimento da renda eleva a poupança, porque as coortes ativas ficam mais ricas que "
            "as aposentadas.",
            vm("Regra-âncora: no ciclo da vida, renda para o idoso vira consumo; renda para o ativo vira "
               "poupança."),
        ],
        "grafico_verso": "ECO-E2-L01002-1-V1",
        "dissecando": (cz("[inversão]") + " O mecanismo invocado (transferência entre gerações) é o correto, mas "
                       "o sinal do efeito foi trocado. A pista é perguntar quem tem a maior taxa de poupança: "
                       "o “mais velho” do item é o aposentado, que consome o patrimônio acumulado. 🔥 A banca "
                       "costuma cobrar o ciclo da vida por estrutura etária e previdência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política que transfira renda de consumidores mais velhos para consumidores em idade ativa "
            "aumentaria a poupança agregada.”</i> → CERTO",
            "<i>“…o envelhecimento da população tende a elevar a taxa de poupança agregada.”</i> → ERRADO "
            "(inversão: idosos despoupam)",
        ])],
        "reescrita": ("De acordo com o Modelo do Ciclo da Vida, uma política que transfira renda de consumidores "
                      "mais jovens para consumidores mais velhos " + hl("reduziria") + " a poupança agregada."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Renda baixa e endividamento na juventude, pico na meia-idade (paga dívidas e poupa), "
                             "renda zero na aposentadoria (consome recursos acumulados). Idosos poupam menos: a "
                             "transferência reduziria a poupança agregada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01003
    {
        "id": "ECO-E2-L01003-1", "fonte_ref": "E2-L01003", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_1,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o Modelo do Ciclo da Vida, os indivíduos poupam a mesma fração de sua renda ao longo "
                      "da vida."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo o Modelo do Ciclo da Vida, os indivíduos poupam ") + vm("a mesma fração")
                    + az(" de sua renda ao longo da vida.")),
        "poucas": ("O ciclo da vida existe justamente para explicar uma " + azb("taxa de poupança variável")
                   + ": negativa na juventude, alta na idade ativa, negativa na aposentadoria."),
        "destrinchando": [
            "Em " + oc("Modigliani") + ", o que se mantém estável ao longo da vida é o <b>consumo</b>, não a "
            "fração poupada. Como a renda do trabalho varia (sobe até a meia-idade e cai a zero na "
            "aposentadoria), a poupança é o resíduo que absorve essa variação: S = Y − C.",
            "Perfil típico: " + vd("S/Y < 0") + " no início (crédito estudantil, financiamento), " + vd("S/Y > 0")
            + " e alta na idade ativa (acúmulo de patrimônio e previdência), " + vd("S/Y < 0")
            + " na velhice (consumo do patrimônio acumulado).",
            "Versão simples do modelo (renda constante Y por R anos de trabalho, vida de T anos, juros zero): "
            "C = (R/T)·Y. Na idade ativa, poupa-se a fração 1 − R/T; na aposentadoria, despoupa-se tudo o que se "
            "consome. Mesmo nesse caso extremo a fração poupada muda de positiva para negativa.",
            "Uma taxa de poupança <b>constante</b> é hipótese de outra família de modelos: a função poupança "
            "proporcional usada no " + azb("modelo de Solow") + " (S = sY), que é agregada e de longo prazo, não "
            "uma teoria do comportamento individual.",
        ],
        "dissecando": (cz("[contradição · troca de conceito]") + " O item troca o que é constante no modelo: "
                       "consumo suavizado ↔ fração poupada constante. Pista: se a renda varia e o consumo não, "
                       "a fração poupada não pode ser a mesma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o Modelo do Ciclo da Vida, os indivíduos procuram manter estável o consumo ao longo da "
            "vida.”</i> → CERTO",
            "<i>“Segundo o Modelo do Ciclo da Vida, a taxa de poupança é máxima na aposentadoria.”</i> → ERRADO "
            "(inversão: na aposentadoria se despoupa)",
        ])],
        "reescrita": ("Segundo o Modelo do Ciclo da Vida, os indivíduos poupam " + hl("frações diferentes")
                      + " de sua renda ao longo da vida" + hl(", despoupando na juventude e na velhice e poupando "
                                                               "na idade ativa") + "."),
        "tipo_erro": ["CONTRADICAO", "TROCA_CONCEITO"], "moduladores": ["a mesma"], "dificuldade": 1,
        "comentario_fonte": "A taxa de poupança muda ao longo da vida de uma pessoa.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01004
    {
        "id": "ECO-E2-L01004-1", "fonte_ref": "E2-L01004", "destino": "55", "subtema": H2["inv"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_1,
        "rotulo_item": "Item",
        "assertiva": ("O q de Tobin mostra que as empresas ao tomarem suas decisões de investimento, consideram a "
                      "relação entre o valor de mercado do capital e o seu custo de reposição."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O q de Tobin mostra que as empresas ao tomarem suas decisões de investimento, consideram a "
                      "relação entre o <u>valor de mercado do capital</u> e o seu <u>custo de reposição</u>."),
        "poucas": ("É a definição: " + azb("q = valor de mercado do capital instalado ÷ custo de reposição")
                   + ". Com " + vd("q > 1") + ", vale a pena investir; com " + vd("q < 1") + ", não."),
        "destrinchando": [
            oc("James Tobin") + " (fim dos anos 1960; Nobel de 1981) liga o investimento ao mercado de "
            "ações: o numerador de q é quanto o mercado avalia o capital já instalado (valor das ações e dívidas "
            "da empresa); o denominador, quanto custaria comprar esse mesmo capital hoje.",
            "Lógica de arbitragem: se " + vd("q > 1") + ", cada R$ 1 gasto em máquinas novas vale mais de R$ 1 na "
            "bolsa — a empresa cria valor ao investir (emitir ações e comprar capital). Se " + vd("q < 1")
            + ", é mais barato comprar empresas prontas do que construir capital: o investimento líquido cai, e o "
            "capital não é reposto quando se deprecia.",
            "Por que o q funciona: o preço da ação incorpora as <b>expectativas</b> de lucros futuros. Assim, o q "
            "resume num só número a rentabilidade esperada do capital e o custo de financiamento, e ajuda a "
            "explicar por que o investimento acompanha a bolsa.",
            "Na prática mede-se o " + azb("q médio") + " (valor total ÷ custo de reposição total), mas a decisão "
            "depende do " + azb("q marginal") + " (o valor da <b>próxima</b> unidade de capital); sob concorrência "
            "e retornos constantes, os dois coincidem (" + oc("Hayashi") + ", 1982).",
            "Vizinhos que a banca mistura: modelo neoclássico (investe-se enquanto PMgK > custo de uso do "
            "capital), " + azb("acelerador") + " (investimento proporcional à variação do produto) e eficiência "
            "marginal do capital de " + oc("Keynes") + " (comparada com a taxa de juros).",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição de manual. O risco está em trocar o "
                       "denominador (custo de reposição por valor contábil ou lucro) ou o numerador (valor de "
                       "mercado por custo histórico); aqui os dois estão corretos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o q de Tobin for inferior a 1, as empresas tendem a ampliar o estoque de capital.”</i> → "
            "ERRADO (inversão: investe-se com q > 1)",
            "<i>“O q de Tobin relaciona o valor contábil do capital ao seu custo de reposição.”</i> → ERRADO "
            "(troca de conceito: é o valor de mercado)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Tobin: investimento depende da razão entre o valor de mercado do capital instalado "
                             "(mercado de ações) e o custo de reposição; q > 1 → vale investir."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01256
    {
        "id": "ECO-E2-L01256-1", "fonte_ref": "E2-L01256", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_2,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a Teoria da Renda Permanente e a Teoria do Ciclo da Vida, as decisões de "
                      "consumo dependem não apenas da renda corrente do indivíduo, mas também de sua renda futura "
                      "esperada e de sua riqueza financeira."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a Teoria da Renda Permanente e a Teoria do Ciclo da Vida, as decisões de "
                      "consumo dependem <u>não apenas</u> da renda corrente do indivíduo, mas também de sua "
                      "<u>renda futura esperada</u> e de sua <u>riqueza financeira</u>."),
        "poucas": ("As duas são teorias " + azb("intertemporais") + ": o consumo depende dos recursos de toda a "
                   "vida — renda corrente, renda futura esperada e riqueza —, não só da renda do período."),
        "destrinchando": [
            "Ponto de partida comum: o consumidor " + azb("suaviza o consumo") + ", usando poupança e crédito "
            "para não acompanhar as oscilações da renda. A restrição relevante é a <b>orçamentária "
            "intertemporal</b>: valor presente do consumo = riqueza inicial + valor presente das rendas.",
            azb("Ciclo da vida") + " (" + oc("Modigliani") + "): C = α·W + β·Y, em que W é a riqueza e Y a renda "
            "do trabalho; a propensão a consumir da riqueza depende dos anos de vida que restam. A ênfase está no "
            "horizonte finito e na aposentadoria.",
            azb("Renda permanente") + " (" + oc("Milton Friedman") + ", <i>A Theory of the Consumption "
            "Function</i>, 1957): Y = Yᴾ + Yᵀ e C = k·Yᴾ. A renda permanente é o fluxo sustentável que a riqueza "
            "humana e financeira pode gerar — logo, também incorpora renda futura e patrimônio.",
            "Contraste com " + oc("Keynes") + " (1936): na função consumo keynesiana, C = C₀ + c·Y, o consumo "
            "depende da renda <b>corrente</b>. As duas teorias nasceram para explicar por que a propensão média "
            "a consumir é estável no longo prazo e decrescente no corte transversal (o “enigma” de "
            + oc("Kuznets") + ").",
            "Implicação de política: cortes temporários de impostos estimulam pouco o consumo; mudanças "
            "percebidas como permanentes estimulam muito.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Síntese de manual das duas teorias "
                       "prospectivas. O “não apenas … mas também” protege o item: não nega o papel da renda "
                       "corrente, só acrescenta renda futura e riqueza. Cuidado com versões que digam "
                       "“exclusivamente da renda corrente” — isso é Keynes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as decisões de consumo dependem exclusivamente da renda corrente do indivíduo.”</i> → ERRADO "
            "(troca de autor: é a função consumo keynesiana)",
            "<i>“…a riqueza financeira é irrelevante para o consumo, que depende apenas da renda do trabalho "
            "esperada.”</i> → ERRADO (restrição indevida: a riqueza entra em C = αW + βY)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["não apenas", "mas também"],
        "dificuldade": 1,
        "comentario_fonte": ("As duas teorias consideram longos horizontes; o consumidor decide com base na renda "
                             "corrente e na esperada, podendo antecipar renda ou acumular riqueza; suavização do "
                             "consumo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01257
    {
        "id": "ECO-E2-L01257-1", "fonte_ref": "E2-L01257", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_2,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a Teoria da Renda Permanente, o consumo não responde às variações da renda se elas "
                      "forem transitórias."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a Teoria da Renda Permanente, o consumo ") + vm("não responde")
                    + az(" às variações da renda se elas forem transitórias.")),
        "poucas": ("Renda transitória afeta o consumo, mas <b>pouco</b>: a maior parte vai para a poupança. O "
                   "item transforma “responde pouco” em " + azb("“não responde”") + "."),
        "destrinchando": [
            oc("Friedman") + " decompõe a renda corrente em " + azb("permanente") + " (Yᴾ, o fluxo que o "
            "consumidor espera sustentar) e " + azb("transitória") + " (Yᵀ, desvios temporários: bônus, prêmio, "
            "desemprego passageiro). O consumo segue sobretudo Yᴾ.",
            "Um ganho transitório aumenta a riqueza e, portanto, eleva <b>um pouco</b> a renda permanente: "
            "dividido por todos os anos que restam, ele financia um pequeno aumento do consumo em cada período. "
            "Ex.: um prêmio de R$ 10 mil para quem tem 40 anos de vida pela frente eleva o consumo em cerca de "
            + vd("R$ 250 por ano") + " (juros zero) — a propensão marginal a consumir da renda transitória é "
            "baixa, mas positiva.",
            "Na prática, a resposta é maior que a da teoria pura: " + azb("restrição de liquidez") + " (quem não "
            "tem crédito nem reserva gasta o que recebe), miopia e dificuldade de distinguir choque transitório "
            "de permanente.",
            "Implicação clássica: estímulos temporários (devolução de impostos, abonos) têm efeito limitado "
            "sobre a demanda agregada, e o consumo agregado oscila menos que a renda ao longo do ciclo.",
            vm("Regra-âncora: renda permanente → consumo responde muito; renda transitória → consumo responde "
               "pouco (não zero) e a poupança absorve o resto."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " O item endurece a tese: “responde menos” virou “não "
                       "responde”. 🔥 As bancas divergem nesse ponto: há professores que, apoiados na formulação "
                       "original C = k·Yᴾ, aceitam como CERTO que a renda transitória “vai toda para a "
                       "poupança”. Aqui, o gabarito segue a leitura intertemporal: efeito pequeno, não nulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a Teoria da Renda Permanente, o consumo responde mais às variações permanentes da renda "
            "do que às transitórias.”</i> → CERTO",
            "<i>“Segundo a Teoria da Renda Permanente, a propensão marginal a consumir da renda transitória é "
            "igual à da renda permanente.”</i> → ERRADO (contradição: é bem menor)",
        ])],
        "reescrita": ("Segundo a Teoria da Renda Permanente, o consumo " + hl("responde pouco") + " às variações "
                      "da renda se elas forem transitórias."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["não"], "dificuldade": 2,
        "comentario_fonte": ("Variações transitórias afetam o consumo, mas com impacto menor que o das permanentes; "
                             "choques amortecidos pela poupança e diluídos pelo restante da vida."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01440-1 e ECO-E2-L01587-1 (outra banca, mesma tese, gabarito CERTO "
                    "para a versão estrita)"],
    },
    # ------------------------------------------------------------------ E2-L01440
    {
        "id": "ECO-E2-L01440-1", "fonte_ref": "E2-L01440", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_1,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria da renda permanente de Friedman, a elevação temporária da renda dos "
                      "consumidores que recebem o auxílio emergencial durante a pandemia levará a um aumento da "
                      "poupança sem efeito sobre o consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Segundo a teoria da renda permanente de Friedman, a elevação <u>temporária</u> da renda dos "
                      "consumidores que recebem o auxílio emergencial durante a pandemia levará a um aumento da "
                      "poupança <u>sem efeito sobre o consumo</u>."),
        "poucas": ("Na formulação estrita de " + oc("Friedman") + " (C = k·Yᴾ), renda " + azb("transitória")
                   + " não altera a renda permanente: vai para a poupança e o consumo fica onde estava."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "“Sem efeito” é a leitura extrema da teoria. Na versão intertemporal, um ganho "
                          "temporário eleva um pouco a riqueza e, com ela, o consumo de todos os períodos — efeito "
                          "<b>pequeno, não nulo</b>. Há banca que marca ERRADO a afirmação de que o consumo “não "
                          "responde” à renda transitória. O CERTO se sustenta pelo “segundo a teoria … de "
                          "Friedman” e pela função C = k·Yᴾ; numa prova CEBRASPE, o “sem efeito” seria arriscado.")],
        "destrinchando": [
            "Friedman (<i>A Theory of the Consumption Function</i>, 1957) separa a renda corrente em Y = Yᴾ + Yᵀ e "
            "postula C = k·Yᴾ, com a renda transitória sem correlação com o consumo. Um auxílio de duração "
            "limitada é o exemplo de livro de " + azb("renda transitória") + ".",
            "Mecanismo: o consumidor quer " + azb("suavizar o consumo") + "; um ganho que não se repetirá é "
            "guardado (ou usado para pagar dívidas, que também é poupança) e diluído pelos anos seguintes. "
            "Resultado na teoria: " + vd("S ↑") + ", " + vd("C ≈ constante") + ".",
            "O caso do " + rx("auxílio emergencial") + " (2020) mostra os limites da teoria: boa parte dos "
            "beneficiários eram informais e de baixa renda, com " + azb("restrição de liquidez") + " — sem "
            "reserva nem crédito, gastam o que recebem. Para eles, a propensão a consumir da renda transitória é "
            "alta, e o benefício sustentou o consumo durante a pandemia.",
            "Por isso o item só se salva como enunciado <b>da teoria</b>, não como descrição do que ocorreu: "
            "a poupança das famílias até subiu em 2020, mas por outro motivo — com comércio e serviços fechados, "
            "quem manteve a renda deixou de gastar (poupança forçada, não suavização do consumo).",
            "Contraste: " + oc("Keynes") + " prevê que o consumo acompanhe a renda corrente (C = C₀ + c·Y) — "
            "o auxílio elevaria o consumo em c vezes o valor recebido.",
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Item de aplicação: o candidato pensa no que "
                       "de fato aconteceu com o auxílio (foi gasto) e marca ERRADO, mas a pergunta é o que a "
                       "teoria <b>prevê</b>. O “sem efeito” é o ponto frágil: absoluto, depende da versão estrita "
                       "da teoria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a função consumo keynesiana, o auxílio emergencial elevaria a poupança sem efeito sobre "
            "o consumo.”</i> → ERRADO (troca de autor: em Keynes o consumo acompanha a renda corrente)",
            "<i>“Segundo a teoria da renda permanente, um aumento permanente da renda seria majoritariamente "
            "poupado.”</i> → ERRADO (troca de conceito: renda permanente vira consumo)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["sem efeito"], "dificuldade": 2,
        "comentario_fonte": ("Correta, embora seja aplicação extrema da teoria: renda transitória seria "
                             "majoritariamente poupada, com pouco ou, na versão estrita, nenhum efeito sobre o "
                             "consumo; na prática, famílias com restrição de liquidez consumiram parte do auxílio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["contestavel: “sem efeito sobre o consumo” vale só na versão estrita (C = k·Yᴾ); na leitura "
                    "intertemporal o efeito é pequeno, não nulo, e outra banca marca ERRADO o “não responde”",
                    "quase_duplicata: ECO-E2-L01587-1 (mesmo professor, mesma tese) e ECO-E2-L01257-1 (gabarito "
                    "oposto para a versão “não responde”)"],
    },
    # ------------------------------------------------------------------ E2-L01587
    {
        "id": "ECO-E2-L01587-1", "fonte_ref": "E2-L01587", "destino": "55", "subtema": H2["cons"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_2,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria da renda permanente de Friedman, uma elevação temporária da renda levará a "
                      "um aumento da taxa de poupança, ficando o consumo estável."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a teoria da renda permanente de Friedman, uma elevação <u>temporária</u> da renda "
                      "levará a um aumento da <u>taxa de poupança</u>, ficando o consumo <u>estável</u>."),
        "poucas": ("Renda " + azb("transitória") + " quase não mexe na renda permanente; como C = k·Yᴾ, o "
                   "consumo se mantém e o acréscimo de renda vira poupança — S/Y sobe."),
        "destrinchando": [
            oc("Milton Friedman") + " (1957): Y = Yᴾ + Yᵀ e " + vd("C = k·Yᴾ") + ". A renda permanente é a renda "
            "média que o consumidor espera para o longo prazo; a transitória são desvios temporários (bônus, "
            "ganho inesperado, desemprego passageiro).",
            "Conta do item: com Yᵀ > 0, Y sobe e C quase não muda; logo S = Y − C sobe praticamente no valor "
            "de Yᵀ. A " + azb("taxa de poupança") + " S/Y também sobe, porque quase 100% do acréscimo é "
            "poupado, bem acima da fração média poupada antes.",
            "A teoria nasceu contra " + oc("Keynes") + " (C = C₀ + c·Y, consumo atrelado à renda corrente) e "
            "explica fatos que a função keynesiana não explicava: no corte transversal, famílias com renda "
            "temporariamente alta poupam mais (parte da renda é transitória); nas séries longas, a propensão "
            "média a consumir é estável; o consumo agregado oscila menos que a renda no ciclo.",
            "Limites: " + azb("restrição de liquidez") + " (quem não tem crédito gasta o que recebe), miopia e "
            "dificuldade de saber se o choque é transitório. Na versão intertemporal, o consumo até sobe um "
            "pouco, porque o ganho eleva a riqueza; por isso “estável” deve ser lido como “quase inalterado”.",
            vm("Regra-âncora: transitório → poupança; permanente → consumo."),
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Reproduz a tese central de Friedman. O "
                       "“ficando o consumo estável” é o ponto sensível: aceito aqui como suavização, mas há banca "
                       "que marca ERRADO quando o item diz que o consumo “não responde” à renda transitória. "
                       "Pista: “temporária” + “Friedman” = poupança."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma elevação permanente da renda levará a um aumento da taxa de poupança, ficando o consumo "
            "estável.”</i> → ERRADO (troca de conceito: renda permanente eleva o consumo)",
            "<i>“Segundo a função consumo keynesiana, uma elevação temporária da renda eleva o consumo.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["estável"], "dificuldade": 1,
        "comentario_fonte": ("Friedman: consumo baseado na renda permanente; elevação temporária é poupada, consumo "
                             "estável; C = k·Yp; S = Y − C sobe e a taxa de poupança aumenta; implicações para "
                             "cortes temporários de impostos e restrição de liquidez."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 442", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (resumo da teoria incorporado ao 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01440-1 (mesmo professor, mesma tese, aplicada ao auxílio "
                    "emergencial)"],
    },
]
