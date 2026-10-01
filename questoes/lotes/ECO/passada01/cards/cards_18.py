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
    # FIM
]
