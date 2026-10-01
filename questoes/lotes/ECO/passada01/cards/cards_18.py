"""Cards da passada 01 de ECO — lote de redação 18 (notas 07-A e 08)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "hip": "📐 Hipóteses e maximização de lucro",
    "cp": "⏱️ Curto prazo: oferta da firma",
    "lp": "⏳ Longo prazo e entrada/saída",
    "mono": "👑 Equilíbrio do monopólio",
    "markup": "📊 Markup, elasticidade e poder de mercado",
    "disc": "🎟️ Discriminação de preços",
    "nat": "🏛️ Monopólio natural e regulação",
}

RT = {"banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023, "cacd": False}

CMD_FIRMA = "A respeito da teoria da firma, julgue o item a seguir."
CMD_FIRMA2 = ("A teoria da firma permite analisar a relação entre os custos de produção e as estruturas de "
              "mercado. A respeito desse tema, julgue o item a seguir.")
CMD_PANDEMIA = ("Durante a pandemia, diversos negócios, como restaurantes e lojas, optaram por fechar as portas "
                "temporariamente. Tendo em vista os determinantes microeconômicos das decisões das firmas de parar "
                "a produção ou sair do mercado, em mercados perfeitamente competitivos, julgue o item a seguir.")
CMD_2017 = ("Com relação a um produto de um mercado que está sob a situação de monopólio natural, o gráfico a "
            "seguir mostra: a curva de demanda, D, que corresponde ao preço de venda, p, para cada quantidade, Q, "
            "demandada pelo mercado, e a curva de custo marginal, C, que corresponde ao custo marginal, CMg, "
            "quando a produção atinge Q unidades. Nesse gráfico, CMg e p estão medidos na mesma escala do eixo "
            "vertical. Tendo como referência as informações e o gráfico apresentados, bem como conceitos a eles "
            "pertinentes, julgue o item.")
ALERTA_F1 = ("figura_conjectural: ECO-E1-0273-1-F1 redesenhada sem a imagem original (image (98).png): D reta "
             "decrescente e C decrescente que corta D, conforme o enunciado e o item 3 (“embora seja decrescente "
             "no trecho mostrado”); posição e escala exatas não preservadas")
ALERTA_2017 = "banca_provavel: CEBRASPE (CACD 2017), não confirmada: a fonte traz só o ano"

CARDS = [
    # ------------------------------------------------------------------ E2-L01465
    {
        "id": "ECO-E2-L01465-1", "fonte_ref": "E2-L01465", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Quando o preço de mercado de um bem é inferior ao seu custo variável médio, o nível de "
                      "produção que minimiza as perdas é positivo e, portanto, a empresa deve continuar a fabricar "
                      "esse bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quando o preço de mercado de um bem é inferior ao seu custo variável médio, o nível de "
                       "produção que minimiza as perdas é ") + vm("positivo") + az(" e, portanto, a empresa ")
                    + vm("deve continuar a fabricar") + az(" esse bem.")),
        "poucas": ("Com " + vd("P < CVMe") + ", cada unidade produzida não paga nem o próprio custo variável: a "
                   "perda mínima está em " + azb("produção zero") + " (paralisação), que limita o prejuízo ao "
                   "custo fixo."),
        "destrinchando": [
            "No curto prazo há custos fixos (aluguel, máquinas) que se pagam produzindo ou não. A comparação "
            "relevante, portanto, não é com o custo total, mas com o " + azb("custo variável") + ": produzindo "
            "q unidades, a firma perde CF − (RT − CV); parada, perde só CF.",
            "Produzir vale a pena se RT ≥ CV, isto é, " + vd("P ≥ CVMe") + ". Se P < CVMe, RT − CV é negativo e "
            "o prejuízo de produzir passa a ser CF <b>mais</b> a parte do custo variável não coberta.",
            "O mínimo do CVMe é o " + azb("ponto de fechamento") + " (<i>shutdown point</i>). Abaixo dele, a "
            "quantidade ofertada é zero; acima, a firma produz onde P = CMg. Por isso a oferta de curto prazo "
            "da firma competitiva é o trecho do CMg acima do CVMe mínimo.",
            "Paralisar não é sair do mercado: a firma fechada continua pagando o custo fixo e volta a produzir "
            "se o preço subir. Sair é decisão de longo prazo, tomada quando P < CTMe.",
            vm("Regra-âncora: curto prazo → P < CVMe, para; longo prazo → P < CTMe, sai."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte a regra de fechamento: com P abaixo do CVMe, a "
                       "conclusão correta é a oposta (produção zero). A frase soa plausível porque “minimizar "
                       "perdas” costuma vir associado a continuar operando — o que só vale quando P está entre o "
                       "CVMe e o CTMe."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando o preço é inferior ao custo total médio, mas superior ao custo variável médio, a "
            "empresa minimiza perdas mantendo a produção.”</i> → CERTO",
            "<i>“Quando o preço é inferior ao custo variável médio, a empresa deve sair definitivamente do "
            "mercado já no curto prazo.”</i> → ERRADO (troca paralisação por saída)",
        ])],
        "reescrita": ("Quando o preço de mercado de um bem é inferior ao seu custo variável médio, o nível de "
                      "produção que minimiza as perdas é " + hl("zero") + " e, portanto, a empresa deve "
                      + hl("suspender a fabricação") + " desse bem."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["portanto"], "dificuldade": 1,
        "comentario_fonte": ("P < CVMe: a firma deve parar de produzir no curto prazo (produção zero), perdendo "
                             "apenas os custos fixos; se P ≥ CVMe, produz onde RMg = CMg."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 360", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 361", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo mecanismo do gráfico de ECO-E2-L01594-1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01466
    {
        "id": "ECO-E2-L01466-1", "fonte_ref": "E2-L01466", "destino": "07-A", "subtema": H2["lp"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Num mercado competitivo, no longo prazo, se o setor tiver custos decrescentes, a curva de "
                      "oferta será negativamente inclinada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Num mercado competitivo, no longo prazo, se o setor tiver <u>custos decrescentes</u>, a "
                      "curva de oferta será <u>negativamente inclinada</u>."),
        "poucas": ("Numa " + azb("indústria de custos decrescentes") + ", a expansão do setor barateia os "
                   "custos de todas as firmas; o novo equilíbrio de longo prazo tem " + vd("preço menor com "
                   "quantidade maior") + " — a oferta de longo prazo da indústria desce."),
        "destrinchando": [
            "A oferta de longo prazo da " + azb("indústria") + " liga os equilíbrios de longo prazo (P = CMe "
            "mínimo, lucro zero) obtidos depois que a entrada e a saída de firmas se completam. Sua inclinação "
            "depende do que acontece com os custos quando o setor cresce.",
            vd("Custos constantes") + ": os preços dos insumos não mudam; a entrada traz o preço de volta ao "
            "nível inicial → oferta de longo prazo <b>horizontal</b>. " + vd("Custos crescentes") + ": a "
            "expansão encarece insumos escassos (terra, mão de obra qualificada) → oferta <b>positivamente</b> "
            "inclinada (o caso mais comum). " + vd("Custos decrescentes") + ": a expansão barateia os custos → "
            "oferta <b>negativamente</b> inclinada.",
            "O mecanismo dos custos decrescentes são as " + azb("economias externas") + " (" + oc("Marshall")
            + "): fornecedores especializados, mão de obra treinada, infraestrutura e difusão de conhecimento "
            "num polo produtivo. São externas à firma — cada uma continua pequena, com CMe em U —, por isso "
            "convivem com a concorrência perfeita.",
            "Sequência: demanda sobe → preço sobe no curto prazo (lucro) → entram firmas → o setor cresce e os "
            "custos de todas caem → o preço de longo prazo termina <b>abaixo</b> do inicial.",
        ],
        "grafico_verso": "ECO-E2-L01466-1-V1",
        "dissecando": (cz("[contraintuitivo · exceção]") + " O item cobra a exceção à regra de que a oferta é "
                       "crescente. Quem pensa na lei da oferta (ou na firma, cujo CMg é crescente) marca ERRADO. "
                       "Pista: “setor” e “longo prazo” — a inclinação negativa é da oferta da indústria, nunca "
                       "do CMg de curto prazo da firma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se o setor tiver custos constantes, a curva de oferta de longo prazo será horizontal.”</i> → "
            "CERTO",
            "<i>“…se o setor tiver custos decrescentes, a curva de oferta de curto prazo de cada firma será "
            "negativamente inclinada.”</i> → ERRADO (a da firma é o CMg crescente acima do CVMe)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "EXCECAO"], "moduladores": ["se"], "dificuldade": 2,
        "comentario_fonte": ("Custos decrescentes: a expansão do setor gera economias externas que reduzem os "
                             "custos de todas as firmas; o preço de equilíbrio de longo prazo cai e a oferta de "
                             "longo prazo é negativamente inclinada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 362", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01466-1-V1, só o painel do mercado)"},
                          {"ref": "IMAGEM 363", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01501
    {
        "id": "ECO-E2-L01501-1", "fonte_ref": "E2-L01501", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_FIRMA2,
        "rotulo_item": "Item",
        "assertiva": ("Nos mercados perfeitamente competitivos, o equilíbrio da firma é obtido quando o preço se "
                      "iguala ao custo marginal, condição que garante lucro zero mesmo no curto prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nos mercados perfeitamente competitivos, o equilíbrio da firma é obtido quando o preço se "
                       "iguala ao custo marginal, ") + vm("condição que garante lucro zero mesmo no curto prazo")
                    + az(".")),
        "poucas": (vd("P = CMg") + " escolhe a quantidade que maximiza o lucro, mas não diz quanto ele é. O "
                   "lucro depende de P × " + azb("CTMe") + ": no curto prazo pode ser positivo, nulo ou "
                   "negativo; o lucro zero é resultado do " + azb("longo prazo") + "."),
        "destrinchando": [
            "Na concorrência perfeita, a firma é tomadora de preço: RMg = P. A condição de primeira ordem "
            "RMg = CMg vira " + vd("P = CMg") + " e define q*. É regra de <b>quantidade</b>, não de resultado.",
            "O lucro econômico é (P − CTMe) × q*. Com P > CTMe em q*, há lucro extraordinário; com P = CTMe, "
            "lucro normal (zero); com CVMe ≤ P < CTMe, prejuízo — e a firma continua produzindo, porque perderia "
            "mais parada.",
            "O lucro zero aparece no " + azb("equilíbrio de longo prazo") + ": lucros atraem firmas, prejuízos "
            "expulsam, e o preço converge para o mínimo do CTMe, onde " + vd("P = CMg = CTMe mínimo") + ".",
            "Lucro econômico zero não é lucro contábil zero: o capital e o trabalho do empresário recebem a "
            "remuneração normal (custo de oportunidade), que já está dentro do custo.",
        ],
        "grafico_verso": "ECO-E2-L01501-1-V1",
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A primeira oração (P = CMg) é a condição correta; "
                       "o erro foi enxertado na consequência (P = CMg não “garante” lucro algum) e no horizonte: “mesmo no curto prazo” leva para o "
                       "curto prazo um resultado que só vale depois da entrada e saída de firmas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio de longo prazo da concorrência perfeita, P = CMg = CTMe mínimo e o lucro "
            "econômico é nulo.”</i> → CERTO",
            "<i>“No curto prazo, a firma competitiva que iguala preço e custo marginal nunca opera com "
            "prejuízo.”</i> → ERRADO (pode operar com prejuízo se CVMe ≤ P < CTMe)",
        ])],
        "reescrita": ("Nos mercados perfeitamente competitivos, o equilíbrio da firma é obtido quando o preço se "
                      "iguala ao custo marginal, condição que " + hl("maximiza o lucro, mas só leva a lucro zero "
                      "no longo prazo") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": ["garante", "mesmo"], "dificuldade": 1,
        "comentario_fonte": ("P = CMg é a condição de equilíbrio, mas não garante lucro zero no curto prazo: "
                             "lucro positivo se P > CMe, zero se P = CMe, prejuízo se P < CMe; lucro zero é "
                             "característica do longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 381", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 382", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada de forma simplificada (ECO-E2-L01501-1-V1, só a firma)"},
                          {"ref": "IMAGEM 383", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (competição monopolística, fora do tema do item)"},
                          {"ref": "IMAGEM 384", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (competição monopolística, fora do tema do item)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01502
    {
        "id": "ECO-E2-L01502-1", "fonte_ref": "E2-L01502", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_FIRMA2,
        "rotulo_item": "Item",
        "assertiva": ("Retornos crescentes de escala são compatíveis com estruturas de mercado competitivas e "
                      "muitas firmas operando no mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Retornos crescentes de escala ") + vm("são compatíveis") + az(" com estruturas de "
                    "mercado competitivas e muitas firmas operando no mercado.")),
        "poucas": ("Retornos crescentes (internos à firma) significam " + azb("custo médio decrescente") + ": "
                   "a firma maior produz mais barato e tende a dominar o mercado. O resultado natural é "
                   "concentração — no limite, " + azb("monopólio natural") + " —, não concorrência."),
        "destrinchando": [
            azb("Retornos crescentes de escala") + ": multiplicar todos os insumos por λ multiplica o produto "
            "por mais que λ. Com preços de insumos dados, o " + vd("CMe de longo prazo cai") + " à medida que a "
            "produção cresce.",
            "Por que trava a concorrência: (1) quem cresce ganha vantagem de custo e expulsa os menores; (2) com "
            "CMe decrescente, o CMg fica abaixo do CMe, e uma firma tomadora de preço que fixasse P = CMg teria "
            "prejuízo — o equilíbrio competitivo nem existe.",
            "A concorrência perfeita supõe CMe de longo prazo em U (ou retornos constantes) com escala mínima "
            "eficiente <b>pequena</b> diante do mercado, de modo que caibam muitas firmas.",
            "Ressalva útil: se as economias de escala forem " + azb("externas") + " à firma (ganhos do setor "
            "como um todo, à " + oc("Marshall") + "), cada firma segue pequena e a concorrência sobrevive — é "
            "a base da indústria de custos decrescentes e dos modelos de " + oc("Krugman") + " sobre "
            "aglomeração.",
            vm("Regra-âncora: economias de escala internas → concentração; externas → compatíveis com "
               "concorrência."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item atribui à concorrência uma característica de "
                       "tecnologia que é a causa clássica do monopólio natural. Repare que ele não fala em "
                       "economias externas: sem essa qualificação, “retornos crescentes de escala” se lê como "
                       "propriedade da função de produção da firma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Economias de escala externas à firma são compatíveis com mercados competitivos.”</i> → CERTO",
            "<i>“Retornos crescentes de escala em toda a extensão da demanda tendem a gerar monopólio "
            "natural.”</i> → CERTO",
        ])],
        "reescrita": ("Retornos crescentes de escala " + hl("tendem a ser incompatíveis") + " com estruturas de "
                      "mercado competitivas e muitas firmas operando no mercado" + hl(", pois favorecem a "
                      "concentração") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Retornos crescentes de escala implicam custo médio decrescente e levam ao "
                             "monopólio natural; mercados competitivos supõem retornos constantes ou "
                             "decrescentes, ou CMe de longo prazo em U."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01538
    {
        "id": "ECO-E2-L01538-1", "fonte_ref": "E2-L01538", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Uma firma operando num mercado competitivo com prejuízo (lucro econômico negativo) pode "
                      "estar maximizando lucros, no curto prazo, desde que o preço seja superior ao custo "
                      "variável médio, já que o prejuízo seria maior se ela parasse a produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma firma operando num mercado competitivo com prejuízo (lucro econômico negativo) <u>pode "
                      "estar maximizando lucros</u>, no curto prazo, desde que o preço seja superior ao <u>custo "
                      "variável médio</u>, já que o prejuízo seria maior se ela parasse a produção."),
        "poucas": ("Com " + vd("CVMe < P < CTMe") + ", produzir onde P = CMg cobre todo o custo variável e parte "
                   "do fixo; parada, a firma perderia o " + azb("custo fixo inteiro") + ". Maximizar lucro, "
                   "aqui, é minimizar prejuízo."),
        "destrinchando": [
            "No curto prazo, o custo fixo é " + azb("irrecuperável") + " no período: paga-se de qualquer jeito. "
            "Prejuízo parado = CF. Prejuízo produzindo = CF − (RT − CV).",
            "Se P > CVMe, então RT > CV: a diferença (" + azb("margem de contribuição") + ") abate parte do "
            "custo fixo, e o prejuízo produzindo fica menor que CF. Exemplo: CF = 100, RT = 80, CV = 60 → "
            "prejuízo de " + vd("80") + " produzindo contra " + vd("100") + " parada.",
            "“Maximizar lucro” inclui o caso em que o máximo é negativo: a regra P = CMg (com P ≥ CVMe) escolhe "
            "o <b>menor</b> prejuízo possível.",
            "A situação não dura: se o preço não se recupera, no longo prazo o custo fixo vira variável (o "
            "contrato vence, a máquina pode ser vendida) e a firma sai, porque P < CTMe.",
        ],
        "grafico_verso": "ECO-E2-L01538-1-V1",
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Parece contraditório “maximizar lucro” "
                       "com prejuízo — é isso que leva ao ERRADO. O item se salva pelo “pode” e pela condição "
                       "correta (P > CVMe, não P > CTMe), e ainda entrega a justificativa certa no final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…pode estar maximizando lucros, no curto prazo, desde que o preço seja superior ao custo total "
            "médio…”</i> → ERRADO (com P > CTMe não haveria prejuízo; a condição é P > CVMe)",
            "<i>“…pode estar maximizando lucros, no longo prazo, desde que o preço seja superior ao custo "
            "variável médio…”</i> → ERRADO (no longo prazo não há custo fixo: com prejuízo, sai)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode", "desde que"],
        "dificuldade": 1,
        "comentario_fonte": ("Fusão de ECO-E2-L01538 e da duplicata E2-L01713: P > CVMe cobre os custos "
                             "variáveis e parte dos fixos; parar significaria perder todo o custo fixo; só se "
                             "para se P < CVMe."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 412", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01538-1-V1, com as áreas de prejuízo e de custo fixo "
                                   "coberto)"},
                          {"ref": "IMAGEM 510 (duplicata E2-L01713)", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo mecanismo)"}],
        "alertas": ["duplicata_fundida: E2-L01713 (mesma assertiva, mesma prova)"],
    },
    # ------------------------------------------------------------------ E2-L01539
    {
        "id": "ECO-E2-L01539-1", "fonte_ref": "E2-L01539", "destino": "07-A", "subtema": H2["lp"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Uma firma competitiva vai deixar o mercado, no longo prazo, se o seu preço for inferior ao "
                      "custo médio total."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma firma competitiva vai deixar o mercado, <u>no longo prazo</u>, se o seu preço for "
                      "inferior ao <u>custo médio total</u>."),
        "poucas": ("No " + azb("longo prazo") + " todos os custos são variáveis: se " + vd("P < CTMe") + ", a "
                   "firma tem prejuízo econômico que nenhuma paralisação evita, e a saída é a única forma de "
                   "zerá-lo."),
        "destrinchando": [
            "No longo prazo não existe custo fixo: contratos vencem, instalações podem ser vendidas ou "
            "reconvertidas. Sair do mercado reduz o custo a zero — logo, a firma só fica se a receita cobrir "
            "<b>todos</b> os custos: " + vd("P ≥ CTMe") + ".",
            "O CTMe inclui o " + azb("custo de oportunidade") + " do capital e do trabalho do dono. P < CTMe "
            "significa que esses recursos renderiam mais em outra atividade: a firma pode até ter lucro "
            "contábil, mas tem prejuízo econômico.",
            "Contraste com o curto prazo: ali o critério é o CVMe (paralisar × produzir), porque o custo fixo é "
            "pago de qualquer forma. Duas linhas, dois horizontes: " + vd("CVMe") + " decide paralisar; "
            + vd("CTMe") + " decide sair.",
            "A saída de firmas reduz a oferta do mercado e eleva o preço até o mínimo do CTMe, onde as que "
            "ficam obtêm lucro econômico zero — o equilíbrio de longo prazo.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a regra de saída do livro-texto. A armadilha seria "
                       "trocar o horizonte: a mesma frase no <b>curto prazo</b> ficaria ERRADA (ali o "
                       "critério é o CVMe e a decisão é paralisar, não sair)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma firma competitiva vai deixar o mercado, no curto prazo, se o seu preço for inferior ao "
            "custo médio total.”</i> → ERRADO (curto prazo: critério é o CVMe, e a decisão é paralisar)",
            "<i>“Uma firma competitiva vai deixar o mercado, no longo prazo, se o seu preço for inferior ao "
            "custo variável médio.”</i> → ERRADO (no longo prazo todo custo é variável: o critério é o CTMe)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["se"], "dificuldade": 1,
        "comentario_fonte": ("Fusão de ECO-E2-L01539 e da duplicata E2-L01715: no longo prazo todos os custos "
                             "são variáveis; se P < CMeT, a firma sai; condição de permanência P ≥ CMeT."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 412", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (texto absorvido no 📖)"}],
        "alertas": ["duplicata_fundida: E2-L01715 (mesma assertiva, mesma prova)"],
    },
    # ------------------------------------------------------------------ E2-L01591
    {
        "id": "ECO-E2-L01591-1", "fonte_ref": "E2-L01591", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_PANDEMIA,
        "rotulo_item": "Item",
        "assertiva": ("No curto prazo, se a firma se depara com uma receita total menor que seus custos totais, "
                      "ela sairá do mercado, já que existe livre entrada e saída."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No curto prazo, se a firma se depara com uma receita total menor que seus custos totais, "
                       "ela ") + vm("sairá do mercado") + az(", já que existe livre entrada e saída.")),
        "poucas": ("RT < CT é só prejuízo. No curto prazo a firma não sai: compara " + vd("RT com CV") + " e "
                   "continua produzindo se RT ≥ CV, ou " + azb("paralisa") + " se RT < CV — mas segue no "
                   "mercado pagando o custo fixo."),
        "destrinchando": [
            "Duas decisões, dois horizontes. " + azb("Paralisação") + " (<i>shutdown</i>) é de curto prazo: a "
            "firma deixa de produzir por um tempo, mas mantém a estrutura e continua pagando o custo fixo. "
            + azb("Saída") + " (<i>exit</i>) é de longo prazo: a firma encerra a atividade e se livra de todos "
            "os custos.",
            "Regra de curto prazo: produz se " + vd("RT ≥ CV") + " (P ≥ CVMe); paralisa se RT < CV (P < CVMe). "
            "Com CV ≤ RT < CT, opera com prejuízo, porque perderia mais parada.",
            "Regra de longo prazo: sai se " + vd("RT < CT") + " (P < CTMe). É aí que a livre entrada e saída "
            "opera — por definição, o curto prazo é o período em que o número de firmas e a planta estão "
            "dados.",
            "O caso da pandemia ilustra a diferença: restaurantes que “fecharam as portas temporariamente” "
            "paralisaram (receita abaixo do custo variável, com aluguel ainda correndo); os que encerraram o "
            "CNPJ saíram — decisão que exige o horizonte longo.",
        ],
        "dissecando": (cz("[troca de conceito · anacronismo]") + " O item usa o critério e o mecanismo do longo "
                       "prazo (RT < CT, livre entrada e saída) para uma decisão de curto prazo. A justificativa "
                       "“já que existe livre entrada e saída” é a pista: essa hipótese só atua quando o tempo "
                       "permite ajustar todos os fatores."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, se a receita total for menor que o custo variável total, a firma paralisará a "
            "produção.”</i> → CERTO",
            "<i>“No longo prazo, se a receita total for menor que o custo total, a firma sairá do "
            "mercado.”</i> → CERTO",
        ])],
        "reescrita": ("No " + hl("longo") + " prazo, se a firma se depara com uma receita total menor que seus "
                      "custos totais, ela sairá do mercado, já que existe livre entrada e saída."),
        "tipo_erro": ["TROCA_CONCEITO", "ANACRONISMO"], "moduladores": ["se"], "dificuldade": 1,
        "comentario_fonte": ("Sair do mercado é decisão de longo prazo; no curto prazo, a firma continua "
                             "produzindo com RT < CT desde que RT ≥ CVT (P ≥ CVMe) e paralisa se RT < CVT."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 446", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 447", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo mecanismo do gráfico de ECO-E2-L01594-1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01592
    {
        "id": "ECO-E2-L01592-1", "fonte_ref": "E2-L01592", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", **RT, "errei": False,
        "comando": CMD_PANDEMIA,
        "rotulo_item": "Item",
        "assertiva": ("No curto prazo, se a firma se depara com preço menor que o custo médio, porém maior que o "
                      "custo variável médio, ela manterá a operação mesmo com prejuízos, pois o prejuízo será "
                      "menor que o custo fixo que ela pagaria se parasse a operação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No curto prazo, se a firma se depara com preço <u>menor que o custo médio, porém maior que "
                      "o custo variável médio</u>, ela manterá a operação mesmo com prejuízos, pois o prejuízo "
                      "será menor que o custo fixo que ela pagaria se parasse a operação."),
        "poucas": ("Entre o " + vd("CVMe") + " e o " + vd("CTMe") + ", cada unidade vendida paga seu custo "
                   "variável e deixa uma sobra que abate o custo fixo: operar dá prejuízo " + azb("menor que "
                   "CF") + ", que seria a perda com a firma parada."),
        "destrinchando": [
            "Contas da firma no curto prazo: parada, " + vd("prejuízo = CF") + ". Operando, prejuízo = CT − RT "
            "= CF − (RT − CV). Como P > CVMe implica RT > CV, o prejuízo operando é menor que CF.",
            "Exemplo: CF = 1.000; ao preço vigente, RT = 1.100 e CV = 800. Operando, perde " + vd("700")
            + "; parada, perderia " + vd("1.000") + ". A diferença (300) é a contribuição da operação para o "
            "custo fixo.",
            "Essa faixa de preço (" + azb("entre o ponto de fechamento e o ponto de nivelamento") + ") é "
            "a que explica empresas que seguem abertas no vermelho numa crise: o delivery dos restaurantes "
            "na pandemia, mantido com margem baixa porque o aluguel corria de qualquer jeito.",
            "Limites: a lógica vale enquanto houver custo fixo. Persistindo P < CTMe, no longo prazo a firma "
            "sai; e se P cair abaixo do CVMe, paralisa já no curto prazo.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " É a regra de decisão do livro-texto, com a "
                       "faixa certa (CVMe < P < CTMe) e a justificativa certa (comparação com o custo fixo). O "
                       "risco está na intuição de que prejuízo manda fechar — e em ler “custo médio” como se "
                       "fosse o variável."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se a firma se depara com preço menor que o custo variável médio, ela manterá a operação, pois "
            "o prejuízo será menor que o custo fixo…”</i> → ERRADO (abaixo do CVMe o prejuízo operando supera o "
            "custo fixo)",
            "<i>“…ela manterá a operação mesmo com prejuízos, pois a receita cobre integralmente os custos "
            "fixos.”</i> → ERRADO (cobre o variável e só parte do fixo)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["se", "porém"], "dificuldade": 1,
        "comentario_fonte": ("Quando CVMe < P < CMe, a firma opera com prejuízo, mas menor que o custo fixo que "
                             "pagaria parada; a margem sobre o custo variável cobre parte do fixo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01593
    {
        "id": "ECO-E2-L01593-1", "fonte_ref": "E2-L01593", "destino": "07-A", "subtema": H2["lp"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_PANDEMIA,
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, mesmo se o preço ficar abaixo do custo médio, pode ser vantajoso para a "
                      "firma manter a operação se a receita for suficiente para pagar os custos fixos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No longo prazo, mesmo se o preço ficar abaixo do custo médio, ") + vm("pode ser vantajoso "
                    "para a firma manter a operação se a receita for suficiente para pagar os custos fixos")
                    + az(".")),
        "poucas": ("No " + azb("longo prazo") + " não existem custos fixos: todos os fatores são ajustáveis. Com "
                   + vd("P < CTMe") + ", a firma tem prejuízo econômico e a decisão ótima é sair."),
        "destrinchando": [
            "A lógica de “continuar operando no vermelho” depende de um custo que se paga de qualquer jeito. "
            "Ela existe no " + azb("curto prazo") + ", quando há fator fixo; some no longo prazo, por definição "
            "o horizonte em que todos os insumos — inclusive planta e contratos — podem ser alterados ou "
            "eliminados.",
            "Sem custo fixo, sair zera o custo total. Permanecer com P < CTMe significa aceitar prejuízo "
            "econômico sem nada que ele evite: os recursos renderiam mais em outro uso. Condição de "
            "permanência: " + vd("P ≥ CTMe") + ".",
            "O item mistura dois critérios: o do curto prazo (cobrir uma parte dos custos para reduzir a perda) "
            "e o horizonte do longo prazo. Mesmo no curto prazo, a régua não é “pagar os custos fixos”, e sim "
            "cobrir o " + vd("custo variável") + " (P ≥ CVMe).",
            "No mercado, a saída das firmas deficitárias reduz a oferta e eleva o preço até o mínimo do CTMe: é "
            "assim que o prejuízo some no equilíbrio de longo prazo.",
        ],
        "dissecando": (cz("[anacronismo · troca de conceito]") + " Transporta para o longo prazo um raciocínio "
                       "que só faz sentido com custos fixos — e ainda troca a régua (custo fixo no lugar do "
                       "variável). O “pode ser vantajoso” dá ar de prudência, mas não salva: no longo prazo, "
                       "custo fixo não existe."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, mesmo se o preço ficar abaixo do custo médio, pode ser vantajoso para a firma "
            "manter a operação se a receita cobrir os custos variáveis.”</i> → CERTO",
            "<i>“No longo prazo, a firma competitiva permanece no mercado enquanto o preço cobrir o custo "
            "variável médio.”</i> → ERRADO (no longo prazo o critério é o CTMe)",
        ])],
        "reescrita": ("No " + hl("curto") + " prazo, mesmo se o preço ficar abaixo do custo médio, pode ser "
                      "vantajoso para a firma manter a operação se a receita for suficiente para pagar os custos "
                      + hl("variáveis") + "."),
        "tipo_erro": ["ANACRONISMO", "TROCA_CONCEITO"], "moduladores": ["mesmo", "pode"], "dificuldade": 2,
        "comentario_fonte": ("No longo prazo todos os custos são variáveis; com P < CMe de longo prazo a firma "
                             "tem prejuízo e sai; não faz sentido falar em custos fixos no longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 448", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01594
    {
        "id": "ECO-E2-L01594-1", "fonte_ref": "E2-L01594", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": CMD_PANDEMIA,
        "rotulo_item": "Item",
        "assertiva": ("A curva de oferta da firma competitiva no curto prazo é a região da curva de custo "
                      "marginal acima da curva de custo médio total."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva de oferta da firma competitiva no curto prazo é a região da curva de custo "
                       "marginal acima da curva de custo ") + vm("médio total") + az(".")),
        "poucas": ("No curto prazo a firma produz enquanto " + vd("P ≥ CVMe") + ": a oferta é o trecho do CMg "
                   "acima do mínimo do " + azb("custo variável médio") + ". O CTMe mínimo delimita a oferta de "
                   "<b>longo</b> prazo."),
        "destrinchando": [
            "Para cada preço, a firma tomadora de preço escolhe q tal que " + vd("P = CMg") + " (no trecho "
            "ascendente do CMg). Por isso o CMg “é” a curva de oferta — mas só onde vale a pena produzir.",
            "Abaixo do mínimo do CVMe (" + azb("ponto de fechamento") + "), a receita não cobre nem o custo "
            "variável e a quantidade ofertada é zero. Acima dele, a firma produz, mesmo que o preço fique "
            "abaixo do CTMe (prejuízo menor que o custo fixo).",
            "O mínimo do CTMe é o " + azb("ponto de nivelamento") + " (<i>break-even</i>): lucro econômico zero. "
            "Entre o fechamento e o nivelamento, a firma está na oferta de curto prazo e no prejuízo.",
            "No " + azb("longo prazo") + ", sem custos fixos, o critério passa a ser o CTMe: a oferta de longo "
            "prazo da firma é o CMg de longo prazo acima do mínimo do CMe de longo prazo.",
            vm("Regra-âncora: oferta de curto prazo = CMg acima do CVMe mínimo."),
        ],
        "grafico_verso": "ECO-E2-L01594-1-V1",
        "dissecando": (cz("[troca de conceito]") + " Troca uma curva de custo médio pela vizinha: o CTMe é a "
                       "régua do longo prazo (saída), o CVMe a do curto prazo (fechamento). 🔥 A banca alterna "
                       "CVMe × CTMe e curto × longo prazo em itens irmãos — conferir sempre os dois."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de oferta da firma competitiva no curto prazo é a parte da curva de custo marginal "
            "acima do mínimo do custo variável médio.”</i> → CERTO",
            "<i>“Ao preço igual ao mínimo do custo médio total, a firma competitiva obtém lucro econômico "
            "nulo.”</i> → CERTO",
        ])],
        "reescrita": ("A curva de oferta da firma competitiva no curto prazo é a região da curva de custo "
                      "marginal acima da curva de custo " + hl("variável médio") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A oferta de curto prazo é a porção do CMg acima do mínimo do CVMe, não do custo "
                             "médio total; abaixo do CVMe mínimo a firma paralisa."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 449", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 450", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01594-1-V1)"},
                          {"ref": "IMAGEM 451", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (repetia o mecanismo)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01661
    {
        "id": "ECO-E2-L01661-1", "fonte_ref": "E2-L01661", "destino": "07-A", "subtema": H2["hip"],
        "tipo": "C/E", **RT, "errei": True,
        "comando": "A respeito dos conceitos e teorias da microeconomia, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Nos mercados competitivos, a demanda de mercado é totalmente elástica a preço, indicando "
                      "que as firmas são tomadoras de preço."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nos mercados competitivos, a demanda ") + vm("de mercado") + az(" é totalmente elástica "
                    "a preço, indicando que as firmas são tomadoras de preço.")),
        "poucas": ("Perfeitamente elástica (horizontal) é a demanda " + azb("de cada firma") + ". A demanda "
                   + azb("de mercado") + " é a de sempre: negativamente inclinada."),
        "destrinchando": [
            "A demanda de mercado soma as demandas dos consumidores e obedece à lei da demanda: preço menor, "
            "quantidade maior. A concorrência perfeita não muda isso — o equilíbrio (P*, Q*) sai do cruzamento "
            "dessa demanda com a oferta da indústria.",
            "Cada firma é minúscula diante do mercado e vende um produto homogêneo. Se cobrar acima de P*, "
            "perde todos os clientes; abaixo, não precisa, porque vende o quanto quiser a P*. Logo, a demanda "
            "que <b>ela</b> enfrenta é " + vd("horizontal em P*") + " (elasticidade infinita), e "
            + vd("P = RMe = RMg") + ".",
            "Os dois gráficos lado a lado: à direita, mercado com D decrescente e O crescente; à esquerda, a "
            "firma com uma reta horizontal no preço que o mercado determinou.",
            "Elasticidade da firma e do mercado se ligam pela participação: |ε<sub>firma</sub>| ≈ "
            "|ε<sub>mercado</sub>| ÷ participação. Com participação perto de zero, a demanda da firma tende a "
            "ser infinitamente elástica mesmo com a de mercado pouco elástica.",
        ],
        "dissecando": (cz("[troca de ator]") + " A propriedade é verdadeira, mas pertence a outro sujeito: a "
                       "firma, não o mercado. A segunda oração (tomadoras de preço) está certa e dá credibilidade "
                       "à primeira. Pergunta-teste: “demanda de quem?”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nos mercados competitivos, a demanda enfrentada por cada firma é perfeitamente elástica ao "
            "preço de mercado.”</i> → CERTO",
            "<i>“Na concorrência perfeita, a receita marginal da firma é menor que o preço.”</i> → ERRADO "
            "(RMg = P, porque a demanda da firma é horizontal)",
        ])],
        "reescrita": ("Nos mercados competitivos, a demanda " + hl("enfrentada por cada firma") + " é totalmente "
                      "elástica a preço, indicando que as firmas são tomadoras de preço."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": ["totalmente"], "dificuldade": 1,
        "comentario_fonte": ("Confunde a demanda de mercado (negativamente inclinada) com a demanda enfrentada "
                             "pela firma individual (perfeitamente elástica, horizontal no preço de mercado)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00016
    {
        "id": "ECO-E3-L00016-1", "fonte_ref": "E3-L00016", "destino": "07-A", "subtema": H2["lp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("Em relação à teoria da produção, ao equilíbrio da firma e à economia do bem-estar, julgue o "
                    "item subsecutivo."),
        "rotulo_item": "Item",
        "assertiva": ("Para que se alcance o equilíbrio competitivo de longo prazo, todas as empresas de um "
                      "determinado setor devem registrar lucro econômico igual a zero, eliminando-se estímulos "
                      "para entrada ou saída do mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para que se alcance o equilíbrio competitivo de longo prazo, todas as empresas de um "
                      "determinado setor devem registrar <u>lucro econômico igual a zero</u>, eliminando-se "
                      "estímulos para entrada ou saída do mercado."),
        "poucas": ("Equilíbrio de longo prazo = ninguém quer entrar nem sair. Isso exige " + vd("lucro econômico "
                   "zero") + ": lucro positivo atrairia entrantes; prejuízo provocaria saídas."),
        "destrinchando": [
            "Mecanismo: lucro econômico positivo → entram firmas → a oferta do setor cresce → o preço cai. "
            "Prejuízo → saem firmas → a oferta encolhe → o preço sobe. O processo para quando "
            + vd("P = CMg = CMe mínimo") + " de longo prazo.",
            azb("Lucro econômico") + " ≠ " + azb("lucro contábil") + ": o econômico desconta o custo de "
            "oportunidade de todos os fatores (inclusive o capital próprio e o trabalho do empresário). Lucro "
            "econômico zero = " + azb("lucro normal") + ": os donos ganham exatamente o que ganhariam no melhor "
            "uso alternativo.",
            "Propriedades do equilíbrio de longo prazo: eficiência alocativa (P = CMg) e produtiva (produção no "
            "mínimo do CMe). É o ponto de referência para medir as perdas do monopólio.",
            "Nuance: firmas com um fator especialmente produtivo (terra melhor, gestor excepcional) podem ter "
            "lucro contábil maior, mas, medido a preço de mercado desse fator, ele vira " + azb("renda")
            + " do fator e o lucro econômico continua zero.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definição de manual. O “todas as empresas” soa como "
                       "modulador absoluto, mas é exatamente o que o modelo exige: se uma só tivesse lucro "
                       "econômico, haveria estímulo à entrada. A armadilha seria confundir com lucro "
                       "<b>contábil</b> zero."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio competitivo de longo prazo, as empresas registram lucro contábil nulo.”</i> → "
            "ERRADO (troca econômico por contábil)",
            "<i>“No curto prazo, a firma competitiva opera necessariamente com lucro econômico nulo.”</i> → "
            "ERRADO (horizonte trocado)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["todas", "devem"], "dificuldade": 1,
        "comentario_fonte": ("No equilíbrio competitivo de longo prazo, P = CMe mínimo = CMg e o lucro "
                             "econômico é zero; lucro positivo atrai entrada, prejuízo provoca saída; lucro "
                             "contábil pode ser positivo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00343
    {
        "id": "ECO-E3-L00343-1", "fonte_ref": "E3-L00343", "destino": "07-A", "subtema": H2["cp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": ("Considerando a teoria da produção e suas implicações para o equilíbrio de curto e longo prazo "
                    "para empresas competitivas, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Para uma empresa competitiva, a curva de oferta no curto prazo coincide com a curva de "
                      "custo marginal que estará necessariamente acima do ponto de custo variável médio mínimo, "
                      "mas não necessariamente acima do custo médio mínimo total."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para uma empresa competitiva, a curva de oferta no curto prazo coincide com a curva de "
                      "custo marginal que estará <u>necessariamente acima do ponto de custo variável médio "
                      "mínimo</u>, mas <u>não necessariamente acima do custo médio mínimo total</u>."),
        "poucas": ("A oferta de curto prazo é o trecho do CMg acima do " + vd("CVMe mínimo") + " (ponto de "
                   "fechamento). Entre esse ponto e o " + vd("CTMe mínimo") + ", a firma produz com prejuízo — "
                   "por isso a oferta não precisa estar acima do CTMe."),
        "destrinchando": [
            "A firma escolhe q com " + vd("P = CMg") + "; produz desde que " + vd("P ≥ CVMe") + ". O primeiro "
            "ponto da oferta é, então, o cruzamento do CMg com o CVMe, que ocorre no " + azb("mínimo do "
            "CVMe") + " (o CMg corta as curvas de custo médio em seus mínimos).",
            "Entre o mínimo do CVMe e o mínimo do CTMe, a firma está na oferta e tem prejuízo, mas menor que o "
            "custo fixo que perderia parada. Acima do mínimo do CTMe, lucro econômico positivo.",
            "Por que o CMg corta os médios no mínimo: enquanto o custo marginal está abaixo da média, puxa a "
            "média para baixo; quando passa acima, puxa para cima. A média é mínima quando " + vd("CMg = CMe")
            + ".",
            "Oferta da " + azb("indústria") + " no curto prazo = soma horizontal das ofertas das firmas (com "
            "número de firmas fixo).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " A redação sobrepõe dois moduladores "
                       "(“necessariamente” e “não necessariamente”) para gerar dúvida, mas cada um está no "
                       "lugar certo: o CVMe é piso obrigatório; o CTMe, não. É o par CERTO do item que troca o "
                       "CVMe pelo CTMe."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a curva de oferta no curto prazo coincide com a curva de custo marginal acima do custo médio "
            "total mínimo.”</i> → ERRADO (troca o CVMe pelo CTMe)",
            "<i>“A firma competitiva pode produzir, no curto prazo, a um preço inferior ao custo total "
            "médio.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["necessariamente", "não necessariamente"],
        "dificuldade": 1,
        "comentario_fonte": ("Oferta de curto prazo = CMg acima do CVMe mínimo (ponto de fechamento); a firma "
                             "pode operar com prejuízo entre o CVMe e o CTMe; o CTMe mínimo é relevante para a "
                             "saída no longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 485", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo mecanismo do gráfico de ECO-E2-L01594-1)"},
                          {"ref": "IMAGEM 486", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0181
    {
        "id": "ECO-E1-0181-1", "fonte_ref": "E1-0181", "destino": "08", "subtema": H2["mono"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos de um imposto específico em um mercado monopolista, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("Suponha que o governo impõe um imposto específico (por unidade) sobre o produto do "
                      "monopolista. Esse imposto aumenta o custo marginal de cada unidade produzida."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Suponha que o governo impõe um imposto específico (por unidade) sobre o produto do "
                      "monopolista. Esse imposto <u>aumenta o custo marginal</u> de cada unidade produzida."),
        "poucas": ("Imposto específico = valor fixo " + vd("t por unidade") + ": cada unidade a mais passa a "
                   "custar CMg + t. A curva de custo marginal do monopolista sobe paralelamente em t."),
        "destrinchando": [
            azb("Imposto específico") + " (R$ por unidade) × " + azb("imposto ad valorem") + " (% do preço). O "
            "específico soma t ao custo de cada unidade: CT passa a CT + t·q, logo " + vd("CMg' = CMg + t") + ". "
            "O custo fixo não muda.",
            "Novo ótimo: RMg = CMg + t. Como a RMg é decrescente, a quantidade " + vd("cai") + " e o preço, "
            "lido na demanda, " + vd("sobe") + ".",
            "Repasse: com demanda linear e CMg constante, o monopolista repassa só " + vd("metade do imposto")
            + " ao preço (P = (a + c)/2 vira (a + c + t)/2). Na concorrência perfeita com custo constante, o "
            "repasse seria integral. Com demanda de elasticidade constante, o repasse do monopolista pode até "
            "superar t, porque o preço é um markup sobre o custo.",
            "Contraste: um imposto sobre o " + azb("lucro") + " (ou um valor fixo, independente de q) não altera "
            "o CMg nem a RMg e, por isso, não muda a quantidade nem o preço do monopolista — só reduz seu lucro.",
        ],
        "dissecando": (cz("[literalidade]") + " Item conceitual direto: específico → custo marginal. A banca "
                       "costuma testar o vizinho — imposto sobre o lucro ou de valor fixo —, que não mexe no CMg "
                       "e não altera a decisão de produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto sobre o lucro do monopolista eleva seu custo marginal e reduz a quantidade "
            "produzida.”</i> → ERRADO (imposto sobre o lucro não altera CMg nem RMg)",
            "<i>“Com demanda linear e custo marginal constante, o monopolista repassa integralmente o imposto "
            "específico ao preço.”</i> → ERRADO (repassa metade)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O imposto específico eleva o custo marginal em valor constante; no monopólio, "
                             "reduz a quantidade ótima e aumenta o preço."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (49).jpeg", "tipo_fonte": "não preservada", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0182
    {
        "id": "ECO-E1-0182-1", "fonte_ref": "E1-0182", "destino": "08", "subtema": H2["mono"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca dos efeitos de um imposto específico em um mercado monopolista, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("Em monopólio, a perda de bem-estar adicional do imposto pode ser menor do que na "
                      "concorrência perfeita, porque o mercado já operava com preço acima do ótimo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Em monopólio, a perda de bem-estar adicional do imposto <u>pode</u> ser menor do que na "
                      "concorrência perfeita, <u>porque o mercado já operava com preço acima do ótimo</u>."),
        "poucas": ("A fonte dá CERTO, mas a justificativa está invertida: como o monopólio já opera com "
                   + vd("P > CMg") + ", cada unidade que o imposto elimina custa à sociedade P − CMg > 0, o que "
                   "tende a tornar a perda adicional " + azb("maior") + ", não menor."),
        "condicionais": [("⚠️ Gabarito contestável", "O gabarito da fonte é CERTO e foi mantido. O “pode” só se "
                          "sustenta para impostos muito altos: com demanda linear e CMg constante, a perda "
                          "adicional no monopólio é menor que a da concorrência apenas se t > 2/3 da distância "
                          "entre o intercepto da demanda e o custo. Para impostos usuais ela é maior, e a razão "
                          "dada no item (preço já acima do ótimo) é justamente o motivo de a perda ser maior. A "
                          "resposta mais defensável seria ERRADO; formulação correta: “em monopólio, a perda "
                          "adicional do imposto <b>tende a ser maior</b> do que na concorrência perfeita, porque "
                          "o mercado já operava com preço acima do custo marginal”.")],
        "destrinchando": [
            "Na concorrência perfeita, o mercado parte do ótimo (P = CMg): as primeiras unidades eliminadas pelo "
            "imposto valem quase o mesmo que custam, e a perda é um triângulo — de " + azb("segunda ordem") + ", "
            "proporcional a t² (" + oc("Harberger") + ").",
            "No monopólio, o mercado já parte de P > CMg. Cada unidade eliminada tinha valor (P) acima do custo "
            "(CMg): a perda adicional é um trapézio, de " + azb("primeira ordem") + " em t. É a lógica do "
            + azb("segundo melhor") + " (" + oc("Lipsey e Lancaster") + "): uma nova distorção sobre um mercado "
            "já distorcido custa mais, não menos.",
            "Conta com D: P = 10 − Q, CMg = 2, t = 2. Concorrência: Q cai de 8 para 6, perda = "
            + vd("2") + ". Monopólio: Q cai de 4 para 3, mas a perda adicional é a área entre a demanda e o "
            "CMg nessa faixa, (6 + 5)/2 × 1 = " + vd("5,5") + ". Só com t muito alto (acima de 16/3 ≈ "
            + vd("5,3") + ") a desigualdade se inverte.",
            "O que é verdade, e talvez inspirou o item: o monopolista repassa só parte do imposto e reduz menos "
            "a quantidade (metade, no caso linear). Menor ΔQ não significa menor perda, porque cada unidade "
            "perdida vale mais.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “pode” protege a afirmação principal — e só ele sustenta o "
                       "CERTO —, mas o nexo causal (“porque já operava com preço acima do ótimo”) é o oposto do resultado da "
                       "teoria do segundo melhor. Em prova, desconfie de item que usa uma distorção prévia para "
                       "concluir que a nova distorção custa menos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em monopólio, um imposto específico reduz a quantidade produzida em proporção menor que em "
            "concorrência perfeita, no caso de demanda linear e custo marginal constante.”</i> → CERTO",
            "<i>“Como o monopólio já gera peso morto, a introdução de um imposto específico não acarreta perda "
            "adicional de bem-estar.”</i> → ERRADO (há perda adicional, em regra maior)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode", "porque"], "dificuldade": 3,
        "comentario_fonte": ("No monopólio já há ineficiência alocativa; a perda adicional do imposto pode ser "
                             "menor do que na concorrência perfeita, pois parte da ineficiência já existia."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: gabarito da fonte CERTO mantido; pela teoria do segundo melhor a perda "
                    "adicional no monopólio é maior para impostos usuais (menor só se t > 2/3 de (a − c) no caso "
                    "linear) e o nexo causal do item é invertido; resposta mais defensável: ERRADO"],
    },
    # ------------------------------------------------------------------ E1-0239
    {
        "id": "ECO-E1-0239-1", "fonte_ref": "E1-0239", "destino": "08", "subtema": H2["disc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2012", "ano": 2012, "cacd": False,
        "errei": True,
        "comando": "Acerca das estruturas de mercado e da discriminação de preços, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("O fato de as passagens aéreas compradas com antecedência serem, em geral, mais baratas que "
                      "as compradas de última hora é compatível com a suposição de que as companhias aéreas atuam "
                      "como monopólios que praticam discriminação de preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O fato de as passagens aéreas compradas com antecedência serem, em geral, mais baratas que "
                      "as compradas de última hora é <u>compatível</u> com a suposição de que as companhias aéreas "
                      "atuam como monopólios que praticam discriminação de preços."),
        "poucas": ("Preço por antecedência separa grupos de " + azb("elasticidades diferentes") + ": o turista, "
                   "que planeja e é sensível a preço, paga menos; o executivo, que decide em cima da hora e é "
                   "pouco sensível, paga mais. Só quem tem " + azb("poder de mercado") + " consegue fazer isso."),
        "destrinchando": [
            azb("Discriminação de preços") + " = cobrar preços diferentes pelo mesmo bem, por razões que não são "
            "diferenças de custo. Condições: (1) " + vd("poder de mercado") + "; (2) capacidade de separar os "
            "grupos; (3) impossibilidade de revenda (arbitragem) — a passagem é nominal.",
            "Regra do 3º grau: o monopolista iguala RMg em cada mercado ao CMg comum e cobra " + vd("mais") + " "
            "do grupo de demanda " + vd("menos elástica") + " (P = CMg / (1 − 1/|ε|) em cada segmento).",
            "Antecedência funciona como critério de separação: quem viaja a lazer compra cedo e tem "
            "alternativas (outro destino, outra data); quem viaja a trabalho decide tarde e não pode esperar. "
            "Restrições como “estadia no sábado” e tarifas não reembolsáveis reforçam a triagem. "
            + oc("Pindyck e Rubinfeld") + " usam as tarifas aéreas como exemplo de discriminação de 3º grau.",
            "Num mercado perfeitamente competitivo isso não se sustentaria: o preço tenderia ao custo marginal "
            "e o cliente de última hora iria ao concorrente. Por isso o item fala em “compatível”: o padrão de "
            "preços é indício de poder de mercado, não prova de monopólio puro (oligopólios também "
            "discriminam).",
        ],
        "dissecando": (cz("[modulador relativo · contraintuitivo]") + " O item é salvo pelo “compatível com a "
                       "suposição”: não afirma que as aéreas são monopólios, só que o fato não contradiz o "
                       "modelo. Quem pensa “aéreas competem entre si” marca ERRADO; a banca quer que se reconheça "
                       "a discriminação por elasticidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A diferença de preço entre passagens compradas com antecedência e de última hora decorre "
            "exclusivamente de diferenças de custo do serviço.”</i> → ERRADO (modulador absoluto; o motivo é a "
            "elasticidade)",
            "<i>“Na discriminação de terceiro grau, o monopolista cobra preço maior do grupo de demanda mais "
            "elástica.”</i> → ERRADO (inversão: cobra mais do menos elástico)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "CONTRAINTUITIVO"], "moduladores": ["em geral", "compatível"],
        "dificuldade": 2,
        "comentario_fonte": ("Discriminação por antecedência: turistas, mais sensíveis ao preço, compram cedo e "
                             "pagam menos; executivos, menos sensíveis, compram de última hora e pagam mais; "
                             "mercado competitivo impediria essa prática."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE (CACD 2012), não confirmada: a fonte traz só o ano"],
    },
    # ------------------------------------------------------------------ E1-0240
    {
        "id": "ECO-E1-0240-1", "fonte_ref": "E1-0240", "destino": "08", "subtema": H2["disc"],
        "tipo": "DISC", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Responda à questão a seguir, sobre estratégias de preço de firmas com poder de mercado.",
        "rotulo_item": "Questão",
        "assertiva": "O que é “discriminação de preços”?",
        "gabarito": "RESPOSTA", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("É a prática de cobrar preços diferentes pelo mesmo bem ou serviço, de consumidores "
                      "diferentes ou por unidades diferentes, sem que a diferença reflita custos. Exige poder de "
                      "mercado, capacidade de separar os consumidores e impossibilidade de revenda. Graus: 1º — "
                      "cada unidade ao preço de reserva do comprador; 2º — preço varia com a quantidade ou a "
                      "versão, e o consumidor se autosseleciona; 3º — preços diferentes por grupo, conforme a "
                      "elasticidade da demanda."),
        "poucas": ("Discriminar preço é cobrar de cada um conforme sua " + azb("disposição a pagar") + ", e não "
                   "conforme o custo, para transformar " + azb("excedente do consumidor") + " em lucro."),
        "destrinchando": [
            "Condições: " + vd("poder de mercado") + " (o tomador de preço não discrimina), " + vd("informação "
            "ou mecanismo para separar") + " os consumidores e " + vd("ausência de arbitragem") + " (quem "
            "comprou barato não pode revender caro).",
            azb("1º grau (perfeita)") + ": cada unidade ao preço de reserva. O monopolista se apropria de todo o "
            "excedente e produz a quantidade eficiente (P = CMg na última unidade) — não há peso morto. Raro na "
            "prática; aproximações: leilões, negociação caso a caso, preços personalizados por algoritmo.",
            azb("2º grau") + ": o preço depende da quantidade ou do pacote, e cada consumidor escolhe a opção "
            "que lhe convém (autosseleção): descontos por volume, “leve 3, pague 2”, tarifas em blocos de "
            "energia, versões básica e premium.",
            azb("3º grau") + ": o vendedor identifica grupos e cobra mais do menos elástico: meia-entrada para "
            "estudantes, tarifas de lazer × executivas, remédios mais baratos em países pobres. Regra: RMg "
            "igual em todos os mercados.",
            "Efeito sobre o bem-estar: o 1º grau elimina o peso morto, mas zera o excedente do consumidor; no "
            "3º grau o efeito é ambíguo — melhora se permitir atender grupos que, com preço único, ficariam de "
            "fora.",
        ],
        "dissecando": (cz("[discursiva curta]") + " Em C/E, o tema vira itens como “na discriminação perfeita há "
                       "peso morto” (ERRADO) ou “descontos por quantidade são discriminação de 2º grau” (CERTO). "
                       "Atenção a exemplos de fronteira: preço maior na sexta à noite (como no cinema) também "
                       "reflete pico de demanda e capacidade — é discriminação intertemporal, não o exemplo "
                       "típico de 3º grau."),
        "modulos": [("🃏 Carta na manga", [
            "Discriminação de preços pode ampliar o acesso: o preço diferenciado de medicamentos e vacinas "
            "entre países ricos e pobres (preços escalonados) é defendido justamente por permitir vender aos "
            "mais pobres sem destruir o retorno da inovação.",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Prática de cobrar preços diferentes pelo mesmo produto conforme tipo, quantidade "
                             "ou disposição a pagar; três graus: preço de reserva por unidade; preço por lotes ou "
                             "quantidades; preço por grupos de consumidores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0241
    {
        "id": "ECO-E1-0241-1", "fonte_ref": "E1-0241", "destino": "08", "subtema": H2["nat"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2018", "ano": 2018, "cacd": False,
        "errei": False,
        "comando": "Acerca do monopólio natural e de sua regulação, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("O serviço de fornecimento de água e saneamento em uma cidade não constitui monopólio "
                      "natural, uma vez que a atuação exclusiva da empresa em sua área é definida por lei ou "
                      "contrato de concessão."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O serviço de fornecimento de água e saneamento em uma cidade ") + vm("não constitui")
                    + az(" monopólio natural, ") + vm("uma vez que") + az(" a atuação exclusiva da empresa em "
                    "sua área é definida por lei ou contrato de concessão.")),
        "poucas": ("O que define o " + azb("monopólio natural") + " é a " + azb("estrutura de custos") + " (uma "
                   "rede só atende a cidade mais barato que duas), não a origem jurídica da exclusividade. "
                   "Saneamento é o exemplo clássico."),
        "destrinchando": [
            azb("Monopólio natural") + ": a função custo é " + azb("subaditiva") + " — uma única firma produz a "
            "quantidade do mercado a custo menor que qualquer divisão entre várias. Típico de setores com "
            "custo fixo enorme (redes de dutos, adutoras, estações de tratamento) e custo marginal baixo.",
            azb("Monopólio legal") + ": a exclusividade decorre de lei, patente ou concessão. As duas coisas "
            "costumam andar juntas — o Estado concede e regula <b>porque</b> o setor é monopólio natural —, mas "
            "a lei não cria nem desfaz a natureza do custo.",
            "Duplicar a rede de água de uma cidade dobraria o custo fixo para dividir a mesma demanda: cada "
            "operadora teria custo médio mais alto. Daí a solução usual: um operador por área e "
            + azb("regulação") + " de tarifa e qualidade.",
            rx("No Brasil") + ", o " + vd("novo Marco Legal do Saneamento (Lei 14.026/2020)") + " manteve a "
            "lógica de operador único por área, mas exige licitação dos contratos de concessão e dá à "
            + rx("ANA") + " a edição de normas de referência para a regulação. ⏳ (out/2026)",
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O fato citado é verdadeiro (a exclusividade "
                       "vem de lei ou contrato), mas a conclusão não decorre dele: confunde monopólio legal com "
                       "natural. Pista: o critério do monopólio natural é econômico (custos), nunca jurídico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O fornecimento de água e saneamento em uma cidade constitui monopólio natural, em razão das "
            "economias de escala associadas à rede de distribuição.”</i> → CERTO",
            "<i>“Todo monopólio legal é também monopólio natural.”</i> → ERRADO (modulador absoluto: patentes "
            "criam monopólios legais sem custos subaditivos)",
        ])],
        "reescrita": ("O serviço de fornecimento de água e saneamento em uma cidade " + hl("constitui") + " "
                      "monopólio natural, " + hl("em razão de sua estrutura de custos, ainda que") + " a atuação "
                      "exclusiva da empresa em sua área seja definida por lei ou contrato de concessão."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": ["uma vez que"], "dificuldade": 1,
        "comentario_fonte": ("Saneamento é monopólio natural pela estrutura física não compartilhável da rede; a "
                             "definição legal apenas reconhece e permite regular a concessionária."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE (CACD 2018), não confirmada: a fonte traz só o ano"],
    },
    # FIM
]
