"""Cards do lote de redação 21 — ECO, passada 02 (nota 47: setor público, funções do Estado, tributação,
política fiscal, equivalência ricardiana)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "func": "🏛️ Funções do Estado",
    "trib": "💸 Tributação: princípios e incidência",
    "pf": "📊 Política fiscal e multiplicadores",
    "ric": "🔮 Equivalência ricardiana",
}

CMD_TRIB = "Julgue o item a seguir, relativo aos princípios da tributação e à incidência tributária."

CMD_FUNC = "Acerca das funções econômicas do governo e dos objetivos da política fiscal, julgue o item a seguir."

CMD_INC = "Julgue o item a seguir, relativo à incidência de tributos em mercados competitivos."

CARDS = [
    # ------------------------------------------------------------------ E1-0176
    {
        "id": "ECO-E1-0176-1", "fonte_ref": "E1-0176", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INC,
        "rotulo_item": "Item",
        "assertiva": ("Com relação à incidência de um imposto sobre vendas de um bem X num mercado em concorrência "
                      "perfeita, é correto afirmar que o imposto é regressivo, porque tende a onerar mais "
                      "fortemente os consumidores mais ricos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Com relação à incidência de um imposto sobre vendas de um bem X num mercado em concorrência "
                       "perfeita, é correto afirmar que o imposto é regressivo, porque tende a onerar mais "
                       "fortemente os consumidores ") + vm("mais ricos") + az(".")),
        "poucas": ("O imposto sobre vendas é, de fato, " + azb("regressivo") + ", mas pelo motivo oposto: pesa "
                   "mais, <b>em proporção da renda</b>, sobre os " + vd("mais pobres") + ", que consomem quase "
                   "tudo o que ganham."),
        "destrinchando": [
            "Progressividade e regressividade medem-se pela " + azb("alíquota efetiva") + " (imposto pago ÷ "
            "renda) ao longo da escala de renda: se ela cai quando a renda sobe, o tributo é regressivo; se sobe, "
            "progressivo; se fica constante, proporcional.",
            "Um imposto sobre vendas com alíquota uniforme cobra o mesmo percentual de cada real <b>gasto</b>. "
            "Como a " + azb("propensão a consumir") + " cai com a renda, a família pobre, que gasta "
            "praticamente toda a renda, entrega ao fisco uma fração maior dela do que a família rica, que poupa "
            "parte do que ganha.",
            "Exemplo: alíquota de 20% sobre o consumo. Renda de R$ 2.000 toda gasta → R$ 400 = " + vd("20% da "
            "renda") + ". Renda de R$ 20.000 com R$ 10.000 gastos → R$ 2.000 = " + vd("10% da renda") + ". Em "
            "valor absoluto o rico paga mais; em proporção, paga menos — é isso que define a regressividade.",
            "Quem paga o imposto entre compradores e vendedores (incidência econômica) depende das "
            "elasticidades; a regressividade é outra pergunta: como o ônus que chega às famílias se distribui "
            "pelas faixas de renda.",
            vm("Regra-âncora: tributo sobre consumo com alíquota uniforme é regressivo porque onera "
               "proporcionalmente mais quem tem menor renda."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A conclusão (“é regressivo”) está certa; o erro foi "
                       "enxertado na justificativa, que inverte o grupo onerado. O conector “porque” é o ponto a "
                       "conferir: a banca costuma acertar a classificação e trocar o motivo. Pista: onerar mais os "
                       "ricos é a definição de <b>progressivo</b>, o que contradiz a própria oração principal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o imposto é regressivo, porque a parcela da renda comprometida com o tributo é maior entre os "
            "consumidores de menor renda.”</i> → CERTO",
            "<i>“…o imposto é progressivo, porque os ricos, que consomem mais em valor absoluto, pagam mais "
            "imposto.”</i> → ERRADO (confunde valor absoluto com proporção da renda)",
        ])],
        "reescrita": ("Com relação à incidência de um imposto sobre vendas de um bem X num mercado em concorrência "
                      "perfeita, é correto afirmar que o imposto é regressivo, porque tende a onerar mais "
                      "fortemente os consumidores " + hl("mais pobres, que gastam em consumo uma fração maior da "
                                                          "renda") + "."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. O imposto sobre vendas com alíquota uniforme é regressivo porque os "
                             "consumidores de menor renda gastam maior proporção da renda no consumo; onera "
                             "proporcionalmente mais os pobres, não os ricos."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0319
    {
        "id": "ECO-E1-0319-1", "fonte_ref": "E1-0319", "destino": "47", "subtema": H2["func"],
        "tipo": "ME", "banca": "Banca não identificada", "prova": "Senado/Consultor/2022", "ano": 2022,
        "cacd": False, "errei": False,
        "comando": "Leia o enunciado a seguir e assinale a opção correta.",
        "rotulo_item": "Questão",
        "assertiva": ("Relacione cada função do governo com suas respectivas características:</p>"
                      "<p>1. Função Estabilizadora.</p><p>2. Função Alocativa.</p><p>3. Função Distributiva.</p>"
                      "<p>( ) Lança mão da política econômica, a fim de realocar incentivos entre agentes "
                      "econômicos, visando o crescimento econômico e o máximo de empregos.</p>"
                      "<p>( ) Utiliza subsídios tributários para estimular o investimento privado em escolas, "
                      "ampliando a oferta de vagas.</p>"
                      "<p>( ) Um instrumento importante dessa função são as alíquotas progressivas do Imposto sobre "
                      "a Renda (IR).</p>"
                      "<p>Assinale a opção que indica a relação correta, na ordem apresentada.</p>"
                      "<p>(A) 1 – 2 – 3.</p><p>(B) 1 – 3 – 2.</p><p>(C) 2 – 1 – 3.</p><p>(D) 2 – 3 – 1.</p>"
                      "<p>(E) 3 – 2 – 1."),
        "gabarito": "A", "gabarito_origem": "fonte", "status": "normal",
        "anotada": ("✅ " + az("(A) 1 – 2 – 3.")
                    + "</p><p>❌ " + az("(B) 1 – ") + vm("3 – 2") + az(".")
                    + "</p><p>❌ " + az("(C) ") + vm("2 – 1") + az(" – 3.")
                    + "</p><p>❌ " + az("(D) ") + vm("2 – 3 – 1") + az(".")
                    + "</p><p>❌ " + az("(E) ") + vm("3") + az(" – 2 – ") + vm("1") + az(".")),
        "poucas": ("Crescimento e emprego → " + azb("estabilizadora") + "; incentivo à oferta de educação → "
                   + azb("alocativa") + "; IR progressivo → " + azb("distributiva") + ". Ordem 1 – 2 – 3."),
        "destrinchando": [
            "A tríade clássica é de " + oc("Richard Musgrave") + " (<i>The Theory of Public Finance</i>, 1959), "
            "difundida no Brasil por " + oc("Giambiagi e Além") + " (<i>Finanças Públicas</i>): "
            + azb("alocativa") + " (prover bens que o mercado não oferta ou oferta mal), " + azb("distributiva")
            + " (corrigir a distribuição de renda que o mercado gera) e " + azb("estabilizadora")
            + " (alto emprego, preços estáveis, crescimento adequado).",
            "1º parêntese — “política econômica”, “crescimento” e “máximo de empregos” são as palavras-chave da "
            "função " + vd("estabilizadora (1)") + ": uso das políticas fiscal, monetária e cambial para "
            "suavizar o ciclo. O “realocar incentivos” é ruído para atrair a resposta “alocativa”.",
            "2º parêntese — subsídio tributário a escolas privadas amplia a oferta de um " + azb("bem meritório")
            + " com externalidade positiva (educação): função " + vd("alocativa (2)") + " na modalidade "
            "<b>indireta</b> (o governo induz o setor privado em vez de produzir ele mesmo).",
            "3º parêntese — alíquotas progressivas do IR cobram proporcionalmente mais de quem ganha mais: "
            "função " + vd("distributiva (3)") + ", que combina tributação progressiva e transferências aos mais "
            "pobres.",
            "(A) ✅ 1 – 2 – 3.",
            "(B) ❌ Inverte alocativa e distributiva: subsídio a escolas não visa redistribuir renda, e IR "
            "progressivo não corrige falha de mercado.",
            "(C) ❌ Troca estabilizadora e alocativa nos dois primeiros parênteses.",
            "(D) ❌ Erra os três.",
            "(E) ❌ Acerta só o do meio; troca estabilizadora e distributiva.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Questão de associação: resolve-se pelas palavras-gatilho "
                       "(emprego/crescimento → estabilizadora; bem público ou meritório → alocativa; "
                       "progressividade/renda → distributiva). A armadilha está no verbo “realocar” do 1º "
                       "parêntese, posto para puxar o candidato para a alocativa. 🔥 A tríade de Musgrave é "
                       "tema recorrente de setor público."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A provisão de bens públicos puros, como defesa nacional, é típica da função distributiva.”</i> "
            "→ ERRADO (troca de conceito: é alocativa)",
            "<i>“Os estabilizadores automáticos, como o seguro-desemprego e o imposto de renda progressivo, "
            "servem também à função estabilizadora.”</i> → CERTO",
        ])],
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Estabilizadora: política econômica para crescimento, pleno emprego e estabilidade de "
                             "preços; alocativa: subsídio a escolas amplia a oferta de bem meritório (modalidade "
                             "indireta); distributiva: IR progressivo. Ordem 1 – 2 – 3, letra A (vários comentários "
                             "concordantes, inclusive Prof. Celso Natale, Estratégia Concursos)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: FGV (concurso do Senado Federal de 2022; a fonte não nomeia a banca)",
                    "texto_corrigido: “afim de” → “a fim de” no 1º parêntese"],
    },
    # ------------------------------------------------------------------ E1-0320
    {
        "id": "ECO-E1-0320-1", "fonte_ref": "E1-0320", "destino": "47", "subtema": H2["pf"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à política fiscal.",
        "rotulo_item": "Item",
        "assertiva": ("Política Fiscal Expansiva refere-se ao aumento de gastos governamentais e/ou redução da "
                      "tributação (carga tributária). A adoção desse tipo de política pode resultar, por exemplo, "
                      "no aumento do consumo das famílias e dos investimentos. O impacto esperado da política "
                      "fiscal expansionista é a ampliação da produção e dos níveis de emprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Política Fiscal Expansiva refere-se ao aumento de gastos governamentais e/ou redução da "
                      "tributação (carga tributária). A adoção desse tipo de política <u>pode</u> resultar, por "
                      "exemplo, no aumento do consumo das famílias e dos investimentos. O impacto "
                      "<u>esperado</u> da política fiscal expansionista é a ampliação da produção e dos níveis de "
                      "emprego."),
        "poucas": ("Mais gasto ou menos imposto eleva a " + azb("demanda agregada") + "; com capacidade ociosa, "
                   "o " + azb("multiplicador") + " amplia produção e emprego. É a definição de manual."),
        "destrinchando": [
            azb("Política fiscal") + " é o manejo de gastos e tributos do governo. " + azb("Expansionista")
            + ": ↑G e/ou ↓T (ou ↑transferências); " + azb("contracionista") + ": o inverso.",
            "Canais: o gasto público entra direto na demanda (Y = C + I + G + NX); o corte de tributos eleva a "
            "renda disponível e, com ela, o consumo; incentivos fiscais e vendas maiores podem estimular o "
            "investimento (efeito " + azb("acelerador") + ").",
            "No modelo keynesiano simples, o efeito sobre a renda é multiplicado: ΔY = ΔG ÷ (1 − c). Com "
            "propensão marginal a consumir " + vd("c = 0,8") + ", o " + azb("multiplicador dos gastos")
            + " é " + vd("5") + "; o dos tributos é menor, " + vd("−c/(1 − c) = −4") + ", porque parte do "
            "corte de imposto é poupada.",
            "Os freios que a banca gosta de cobrar: " + azb("crowding out") + " (o gasto eleva os juros e "
            "desloca investimento privado), " + azb("equivalência ricardiana") + " (as famílias poupam o corte "
            "de imposto financiado por dívida) e economia no pleno emprego (o estímulo vira inflação, não "
            "produto). Por isso o item fala em impacto “esperado” e em “pode resultar” — o efeito é a regra, não "
            "uma garantia.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Três frases de manual, protegidas por "
                       "“pode” e “esperado”. A dúvida plantada é o “aumento dos investimentos”, que o leitor "
                       "atento ao crowding out poderia contestar — mas o “pode resultar, por exemplo” afasta a "
                       "generalização."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política fiscal expansionista necessariamente aumenta o investimento privado.”</i> → ERRADO "
            "(modulador absoluto: o crowding out pode reduzi-lo)",
            "<i>“Na armadilha da liquidez, a política fiscal expansionista eleva a renda sem efeito deslocamento "
            "sobre o investimento.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "esperado"], "dificuldade": 1,
        "comentario_fonte": "CERTO (com remissão ao módulo de política econômica da Enap).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0380
    {
        "id": "ECO-E1-0380-1", "fonte_ref": "E1-0380", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2013", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à carga tributária.",
        "rotulo_item": "Item",
        "assertiva": ("O índice da carga tributária corresponde ao total da arrecadação fiscal do Ministério da "
                      "Fazenda em relação à renda nacional bruta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O índice da carga tributária corresponde ao total da arrecadação fiscal ")
                    + vm("do Ministério da Fazenda") + az(" em relação ") + vm("à renda nacional bruta")
                    + az(".")),
        "poucas": ("Carga tributária = arrecadação de " + azb("todas as esferas de governo") + " (União, "
                   "estados e municípios) ÷ " + vd("PIB") + ". O item erra o numerador (só o federal) e o "
                   "denominador (RNB)."),
        "destrinchando": [
            azb("Carga tributária bruta (CTB)") + " = total de tributos (impostos, taxas e contribuições, "
            "inclusive as previdenciárias) arrecadados pela União, pelos estados, pelo Distrito Federal e pelos "
            "municípios, dividido pelo " + vd("PIB") + " do período. É a medida usada pela Receita Federal, "
            "pelo Tesouro Nacional e pela OCDE nas comparações internacionais.",
            "Numerador errado: a Receita Federal (órgão do Ministério da Fazenda) arrecada só os tributos "
            "federais. ICMS, ISS, IPVA e IPTU ficam de fora — e o ICMS sozinho é o maior tributo do país em "
            "arrecadação.",
            "Denominador errado: a " + azb("renda nacional bruta") + " = PIB + renda líquida recebida do "
            "exterior. No " + rx("Brasil") + ", que remete mais renda (juros, lucros) do que recebe, a RNB é "
            "<b>menor</b> que o PIB, e usá-la inflaria o indicador.",
            "Conceito vizinho: " + azb("carga tributária líquida") + " = CTB − transferências do governo ao "
            "setor privado (previdência, assistência, subsídios, juros). Mede o que fica com o Estado para "
            "financiar o próprio gasto.",
            "Ordem de grandeza: a CTB brasileira gira em torno de " + vd("32% a 33% do PIB") + " nos anos "
            "2020 ⏳ (out/2026), acima da média latino-americana e próxima da média da OCDE.",
        ],
        "dissecando": (cz("[restrição indevida · troca de conceito]") + " Dois erros independentes: restringe "
                       "a arrecadação ao Ministério da Fazenda (âmbito federal) e troca o PIB pela RNB, agregado "
                       "vizinho e de valor próximo. Bastaria um deles para o ERRADO; a banca empilha para testar "
                       "quem só confere o primeiro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A carga tributária bruta corresponde à razão entre a arrecadação de tributos das três esferas "
            "de governo e o PIB.”</i> → CERTO",
            "<i>“A carga tributária líquida soma à bruta as transferências e os subsídios pagos pelo "
            "governo.”</i> → ERRADO (inversão: subtrai)",
        ])],
        "reescrita": ("O índice da carga tributária corresponde ao total da arrecadação fiscal "
                      + hl("das três esferas de governo (União, estados e municípios)") + " em relação "
                      + hl("ao produto interno bruto (PIB)") + "."),
        "tipo_erro": ["RESTRICAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Errado: carga tributária = tributos arrecadados em todos os níveis de governo ÷ PIB; "
                             "não se limita à arrecadação federal nem usa a RNB (quatro comentários "
                             "concordantes)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0579-1 (outro item sobre a definição de carga tributária)"],
    },
    # ------------------------------------------------------------------ E1-0439
    {
        "id": "ECO-E1-0439-1", "fonte_ref": "E1-0439", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("A política fiscal é instrumento central para o equilíbrio macroeconômico e a "
                    "sustentabilidade da dívida pública. Com base nisso, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A abordagem ricardiana da dívida pública defende que, diante de um aumento no déficit "
                      "financiado por dívida, os agentes antecipam elevação futura de impostos e aumentam "
                      "imediatamente seus gastos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A abordagem ricardiana da dívida pública defende que, diante de um aumento no déficit "
                       "financiado por dívida, os agentes antecipam elevação futura de impostos e ")
                    + vm("aumentam imediatamente seus gastos") + az(".")),
        "poucas": ("Quem antecipa imposto futuro " + azb("poupa") + " hoje, não gasta: na "
                   + azb("equivalência ricardiana") + " o corte de impostos financiado por dívida deixa o consumo "
                   "e a demanda agregada inalterados."),
        "destrinchando": [
            "A ideia remonta a " + oc("David Ricardo") + " (que a esboçou e duvidou de sua validade prática) e "
            "foi formalizada por " + oc("Robert Barro") + " em “Are Government Bonds Net Wealth?” (" + vd("1974")
            + "): para uma dada trajetória de gastos públicos, financiar o governo com impostos hoje ou com "
            "dívida hoje (imposto amanhã) é <b>equivalente</b>.",
            "Passo a passo: o governo corta R$ 1 bi de impostos e emite R$ 1 bi em títulos, sem cortar gastos. "
            "A renda disponível sobe, mas o agente racional sabe que pagará R$ 1 bi mais juros no futuro; o "
            "valor presente de sua obrigação fiscal sobe exatamente o que ganhou. Sua " + azb("riqueza "
            "permanente") + " não muda — logo, ele poupa o alívio inteiro (pode até comprar os títulos emitidos).",
            "Resultado: " + vd("poupança privada ↑ = poupança pública ↓") + "; poupança nacional, juros, "
            "consumo e demanda agregada ficam iguais. O estímulo fiscal via endividamento é neutro.",
            "Hipóteses fortes (e as críticas): agentes racionais e bem informados; horizonte infinito ou "
            "altruísmo intergeracional (visão dinástica); ausência de " + azb("restrição de liquidez")
            + "; impostos " + azb("lump-sum") + " (não distorcivos); certeza sobre quando e como a dívida será "
            "paga. A evidência empírica é mista: a maioria vê equivalência <b>parcial</b>.",
            vm("Regra-âncora: ricardiano poupa o corte de imposto; keynesiano gasta parte dele."),
        ],
        "dissecando": (cz("[inversão]") + " A premissa (antecipar impostos futuros) é a do modelo; a conclusão "
                       "foi trocada pela keynesiana. Teste de coerência: quem espera pagar mais imposto amanhã "
                       "não tem motivo para gastar mais hoje. 🔥 Ricardiana em prova quase sempre testa "
                       "poupar × gastar ou neutralidade × multiplicador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela equivalência ricardiana, a substituição de impostos por dívida não altera a poupança "
            "nacional.”</i> → CERTO",
            "<i>“A equivalência ricardiana sustenta que um aumento dos gastos públicos não tem nenhum efeito "
            "sobre a economia.”</i> → ERRADO (troca de conceito: neutra é a forma de financiamento, dado o "
            "gasto)",
        ])],
        "reescrita": ("A abordagem ricardiana da dívida pública defende que, diante de um aumento no déficit "
                      "financiado por dívida, os agentes antecipam elevação futura de impostos e "
                      + hl("aumentam a poupança na mesma medida, mantendo inalterado o consumo") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["imediatamente"], "dificuldade": 1,
        "comentario_fonte": ("ERRADO: agentes racionais antecipam impostos futuros e aumentam a poupança, "
                             "neutralizando o efeito expansionista; Ricardo esboçou, Barro formalizou na década de "
                             "1970; críticas: miopia, restrição de liquidez, horizonte finito, incerteza, "
                             "impostos distorcivos (comentários longos, fundidos com os da linha duplicada)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0541 (mesmo item; comentário fundido neste card)"],
    },
    # ------------------------------------------------------------------ E1-0468
    {
        "id": "ECO-E1-0468-1", "fonte_ref": "E1-0468", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à equivalência ricardiana.",
        "rotulo_item": "Item",
        "assertiva": ("A equivalência ricardiana é uma teoria que indica que um aumento dos gastos do governo, ou "
                      "um corte de impostos no presente, não afeta a renda real em um horizonte de longo prazo. O "
                      "conceito da equivalência ricardiana se alinha, sobretudo, à teoria Keynesiana, que prega "
                      "que um aumento dos gastos do governo não afeta a demanda agregada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A equivalência ricardiana é uma teoria que indica que ")
                    + vm("um aumento dos gastos do governo, ou") + az(" um corte de impostos no presente")
                    + az(", não afeta a renda real em um horizonte de longo prazo. O conceito da equivalência "
                         "ricardiana se alinha, sobretudo, ")
                    + vm("à teoria Keynesiana, que prega que") + az(" um aumento dos gastos do governo ")
                    + vm("não afeta") + az(" a demanda agregada.")),
        "poucas": ("A equivalência ricardiana é tese " + azb("novo-clássica") + " (" + oc("Barro") + ") sobre a "
                   "<b>forma de financiar</b> um dado gasto; para os " + azb("keynesianos") + ", o gasto "
                   "público <b>eleva</b> a demanda agregada."),
        "destrinchando": [
            "O que a equivalência diz: dado o caminho dos gastos públicos, trocar imposto de hoje por dívida "
            "(imposto de amanhã) não altera consumo, poupança nacional nem demanda. O que ela <b>não</b> diz: que "
            "um aumento do próprio gasto seja neutro — mais G absorve recursos, seja qual for o financiamento. Por "
            "isso o “aumento dos gastos do governo” não cabe na 1ª frase.",
            "Filiação: a tese foi formalizada por " + oc("Robert Barro") + " (" + vd("1974") + "), no ambiente "
            "das " + azb("expectativas racionais") + " da escola " + azb("novo-clássica") + ", justamente como "
            "crítica à eficácia da política fiscal keynesiana.",
            "Para " + oc("Keynes") + " e a síntese neoclássica, o gasto público é componente da demanda agregada "
            "(Y = C + I + G + NX) e tem efeito " + azb("multiplicador") + ": ΔY = ΔG ÷ (1 − c). Um corte de "
            "impostos eleva a renda disponível e o consumo corrente, porque o consumo depende da renda "
            "<b>corrente</b>.",
            "O contraste em uma linha: keynesiano → déficit estimula; ricardiano → déficit financiado por dívida "
            "é poupado e não estimula; " + azb("crowding out") + " (visão clássica de fundos emprestáveis) → "
            "déficit eleva juros e desloca investimento.",
            vm("Regra-âncora: equivalência ricardiana = novo-clássica (Barro), oposta à visão keynesiana da "
               "política fiscal."),
        ],
        "dissecando": (cz("[troca de ator · inversão]") + " O item atribui a tese à escola adversária e ainda "
                       "inverte a tese keynesiana (“não afeta a demanda”). Na 1ª frase, enxerta o aumento de "
                       "gastos no que deveria ser só a troca imposto × dívida. Pista: “Keynesiana” e “gasto "
                       "público não afeta a demanda” não cabem na mesma frase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para a equivalência ricardiana, um corte de impostos financiado por emissão de dívida não "
            "altera o consumo corrente das famílias.”</i> → CERTO",
            "<i>“A equivalência ricardiana reforça a eficácia do multiplicador keynesiano dos tributos.”</i> → "
            "ERRADO (inversão: ela anula esse multiplicador)",
        ])],
        "reescrita": ("A equivalência ricardiana é uma teoria que indica que <s>um aumento dos gastos do governo, "
                      "ou</s> um corte de impostos no presente" + hl(", financiado por dívida") + ", não afeta a "
                      "renda real em um horizonte de longo prazo. O conceito da equivalência ricardiana se alinha, "
                      "sobretudo, " + hl("à escola novo-clássica (Barro), e não à teoria keynesiana, segundo a "
                                         "qual") + " um aumento dos gastos do governo " + hl("eleva")
                      + " a demanda agregada."),
        "tipo_erro": ["TROCA_ATOR", "INVERSAO"], "moduladores": ["sobretudo"], "dificuldade": 1,
        "comentario_fonte": "ERRADO (justificativa só em imagem, não preservada; remissão a t.me/cacdeconomia/97).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (155).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; comentário redigido a partir "
                                   "do gabarito)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0567
    {
        "id": "ECO-E1-0567-1", "fonte_ref": "E1-0567", "destino": "47", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_FUNC,
        "rotulo_item": "Item",
        "assertiva": ("A ação do governo por meio da política fiscal tem como função buscar um alto nível de "
                      "emprego, estabilidade de preços e taxas apropriadas de crescimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A ação do governo por meio da política fiscal tem como função buscar um <u>alto nível de "
                      "emprego, estabilidade de preços e taxas apropriadas de crescimento</u>."),
        "poucas": ("É a definição da " + azb("função estabilizadora") + " da política fiscal, quase literal em "
                   + oc("Giambiagi e Além") + "."),
        "destrinchando": [
            oc("Giambiagi e Além") + " (<i>Finanças Públicas: teoria e prática no Brasil</i>): “a função "
            "estabilizadora tem como objetivo o uso da política econômica visando a um alto nível de emprego, à "
            "estabilidade de preços e à obtenção de uma taxa apropriada de crescimento econômico”. O item é "
            "paráfrase direta.",
            "Instrumentos: no lado fiscal, gastos e tributos (expansão na recessão, contração no "
            "superaquecimento) e os " + azb("estabilizadores automáticos") + " (seguro-desemprego, IR "
            "progressivo), que amortecem o ciclo sem decisão nova; no lado monetário, juros e liquidez.",
            "Por que os três objetivos andam juntos: crescer e empregar com inflação descontrolada não se "
            "sustenta; a " + azb("estabilidade de preços") + " é condição para que o crescimento da renda e do "
            "emprego dure.",
            "As outras duas funções de " + oc("Musgrave") + ": " + azb("alocativa") + " (bens públicos e "
            "meritórios, correção de falhas de mercado) e " + azb("distributiva") + " (tributação progressiva e "
            "transferências). Um mesmo instrumento pode servir a mais de uma — o IR progressivo redistribui e "
            "estabiliza.",
        ],
        "dissecando": (cz("[literalidade]") + " Reprodução quase textual do manual. O risco era desconfiar da "
                       "lista tripla (emprego, preços, crescimento) achando que algum dos objetivos é só da "
                       "política monetária; na doutrina, os três compõem a função estabilizadora."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função estabilizadora da política fiscal busca reduzir as desigualdades de renda entre as "
            "regiões do país.”</i> → ERRADO (troca de conceito: é a distributiva)",
            "<i>“A estabilidade de preços é objetivo exclusivo da política monetária, alheio à política "
            "fiscal.”</i> → ERRADO (restrição indevida)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Certo: função estabilizadora (citação de Giambiagi e Além, 2011, p. 10); há ainda "
                             "as funções alocativa e distributiva; um comentário vê viés desenvolvimentista."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0568
    {
        "id": "ECO-E1-0568-1", "fonte_ref": "E1-0568", "destino": "47", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": True,
        "comando": CMD_FUNC,
        "rotulo_item": "Item",
        "assertiva": ("Por intermédio da política fiscal, pode-se dizer que o processo político surge como "
                      "mecanismo substituto ao sistema de mercado, ao dispor em relação a alocações de bens "
                      "públicos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Por intermédio da política fiscal, pode-se dizer que o <u>processo político</u> surge "
                      "como <u>mecanismo substituto ao sistema de mercado</u>, ao dispor em relação a alocações "
                      "de <u>bens públicos</u>."),
        "poucas": ("Para " + azb("bens públicos") + ", o sistema de preços falha; quem decide o que e quanto "
                   "ofertar é o " + azb("processo político") + " (orçamento votado), que faz as vezes do mercado "
                   "na " + azb("função alocativa") + "."),
        "destrinchando": [
            "Em regra, o mercado aloca recursos pelos preços, que sinalizam escassez e preferências. Os "
            + azb("bens públicos puros") + " têm duas propriedades que quebram esse mecanismo: "
            + azb("não rivalidade") + " (o consumo de um não reduz o do outro) e " + azb("não exclusão")
            + " (não se impede quem não paga de usufruir).",
            "Consequência: cada um tende a esconder quanto valoriza o bem e a pegar " + azb("carona")
            + " (<i>free rider</i>) no pagamento alheio. Sem preferências reveladas não há preço, e a provisão "
            "privada fica abaixo do ótimo — defesa, iluminação pública, segurança.",
            "Saída: a quantidade e o financiamento passam a ser definidos coletivamente — eleição de "
            "representantes, proposta do Executivo, votação do orçamento pelo Legislativo. É nesse sentido que "
            + oc("Musgrave") + " e, no Brasil, " + oc("Giambiagi e Além") + " tratam o processo político como "
            "<b>substituto</b> do mercado na função alocativa.",
            "Limite que a banca pode cobrar: a votação também falha (preferências agregadas imperfeitamente, "
            "grupos de interesse, horizonte eleitoral). A escola da " + azb("escolha pública") + " ("
            + oc("James Buchanan") + ") chama isso de <b>falhas de governo</b> — o substituto não é perfeito.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " A linguagem rebuscada (“ao dispor em "
                       "relação a alocações”) e a palavra “substituto” assustam, mas a tese é a de manual. "
                       "Pista: o item restringe o papel do processo político aos <b>bens públicos</b>, "
                       "exatamente onde o mercado falha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o processo político surge como mecanismo substituto ao sistema de mercado na alocação de "
            "todos os bens e serviços da economia.”</i> → ERRADO (modulador absoluto: só onde o mercado falha)",
            "<i>“A não exclusão dos bens públicos estimula o comportamento de carona, o que dificulta sua "
            "provisão pelo mercado.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["pode-se dizer"], "dificuldade": 2,
        "comentario_fonte": ("Certo: com bens públicos (falha de mercado), a alocação não se dá pelo mecanismo de "
                             "preços, mas pelo processo político, inclusive pela aprovação do orçamento no "
                             "Legislativo; o governo substitui o mercado na função alocativa."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0569
    {
        "id": "ECO-E1-0569-1", "fonte_ref": "E1-0569", "destino": "47", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_FUNC,
        "rotulo_item": "Item",
        "assertiva": "A política fiscal é incapaz de alterar a distribuição funcional da renda de uma sociedade.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A política fiscal ") + vm("é incapaz") + az(" de alterar a distribuição funcional da "
                                                                     "renda de uma sociedade.")),
        "poucas": ("A " + azb("função distributiva") + " existe justamente porque tributos e gastos alteram a "
                   "repartição da renda — entre pessoas e entre fatores (salários × lucros, juros e aluguéis)."),
        "destrinchando": [
            "Dois recortes da distribuição: " + azb("funcional") + " = como a renda nacional se divide entre os "
            "fatores de produção (salários, lucros, juros, aluguéis) — por exemplo, a participação dos salários "
            "no PIB; " + azb("pessoal") + " = como se divide entre indivíduos ou famílias, medida pelo "
            + azb("índice de Gini") + " ou pela fatia dos 10% mais ricos.",
            "A política fiscal mexe na funcional quando tributa de forma diferente o trabalho e o capital "
            "(encargos sobre a folha × tributação de lucros e dividendos), quando desonera a folha, quando paga "
            "juros da dívida pública (renda que vai para detentores de capital) ou quando o gasto público eleva "
            "a demanda por trabalho.",
            "Na pessoal, os instrumentos clássicos são a " + azb("tributação progressiva") + " (IR com "
            "alíquotas crescentes), as " + azb("transferências") + " (Bolsa Família, BPC) e os subsídios a bens "
            "consumidos pelos mais pobres.",
            "Tríade de " + oc("Musgrave") + ", adotada pelo " + rx("Tesouro Nacional") + ": a política fiscal "
            "arrecada e gasta para cumprir as funções " + vd("alocativa, distributiva e estabilizadora")
            + ". Negar a capacidade distributiva é negar uma das três.",
        ],
        "dissecando": (cz("[modulador absoluto · contradição]") + " “Incapaz” é absoluto e contraria a "
                       "doutrina. O adjetivo “funcional” tenta fazer o candidato hesitar (a distribuição entre "
                       "fatores parece “do mercado”), mas tributar capital e trabalho de forma diferente já a "
                       "altera. 🔥 Absolutos negativos (“incapaz”, “nunca”) em funções do governo são quase "
                       "sempre ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A distribuição funcional da renda refere-se à repartição da renda entre os fatores de "
            "produção.”</i> → CERTO",
            "<i>“O índice de Gini mede a distribuição funcional da renda.”</i> → ERRADO (troca de conceito: "
            "mede a pessoal)",
        ])],
        "reescrita": ("A política fiscal " + hl("é capaz") + " de alterar a distribuição funcional da renda de "
                      "uma sociedade."),
        "tipo_erro": ["GENERALIZACAO", "CONTRADICAO"], "moduladores": ["incapaz"], "dificuldade": 1,
        "comentario_fonte": ("Errado: a distributiva é uma das três funções da política fiscal; tributos "
                             "progressivos e transferências alteram a distribuição (citações do Tesouro Nacional e "
                             "do Blog do IBRE). Nenhum comentário distingue distribuição funcional de pessoal."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0570
    {
        "id": "ECO-E1-0570-1", "fonte_ref": "E1-0570", "destino": "47", "subtema": H2["func"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "2022", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_FUNC,
        "rotulo_item": "Item",
        "assertiva": "Um dos principais instrumentos da função distributiva da política fiscal são os tributos.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Um dos</u> principais instrumentos da função distributiva da política fiscal são os "
                      "<u>tributos</u>."),
        "poucas": ("A " + azb("função distributiva") + " usa os dois lados do orçamento: " + azb("tributação "
                   "progressiva") + " (arrecadar mais de quem ganha mais) e transferências e gastos focalizados. "
                   "Os tributos são um dos instrumentos centrais."),
        "destrinchando": [
            "Na lista de " + oc("Giambiagi e Além") + ", os instrumentos da função distributiva são "
            + vd("três") + ": transferências, impostos e subsídios. Por exemplo, imposto progressivo que "
            "financia programas para a população de baixa renda; subsídio a bens consumidos sobretudo pelos "
            "mais pobres.",
            "Pelo lado da receita: alíquotas do IR crescentes com a renda, faixa de isenção mais alta, tributação "
            "de grandes heranças e patrimônio, menor peso dos tributos sobre consumo (regressivos).",
            "Pelo lado do gasto: transferências focalizadas (Bolsa Família, BPC), saúde e educação gratuitas. "
            "No " + rx("Brasil") + ", estudos de incidência mostram que as transferências reduzem mais a "
            "desigualdade do que os tributos, porque a carga recai muito sobre o consumo.",
            "Exemplo recente: a reforma do IR aprovada em 2025 amplia a isenção para rendas de até "
            + vd("R$ 5 mil mensais") + " a partir de 2026 e cria tributação mínima sobre altas rendas — medida "
            "típica da função distributiva ⏳ (out/2026).",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " “Um dos” protege o item: não afirma que os "
                       "tributos sejam o único nem o principal instrumento. A troca perigosa seria por "
                       "“o único” ou “exclusivamente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O único instrumento da função distributiva da política fiscal são os tributos "
            "progressivos.”</i> → ERRADO (restrição indevida: há transferências e subsídios)",
            "<i>“A elevação da participação dos tributos indiretos na arrecadação tende a reforçar a função "
            "distributiva.”</i> → ERRADO (inversão: tributos indiretos tendem a ser regressivos)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["um dos"], "dificuldade": 1,
        "comentario_fonte": ("Certo: para distribuir renda o governo tributa e gasta de forma progressiva; o IR "
                             "pode ter alíquotas maiores para rendas altas e faixa de isenção mais alta; citação "
                             "do Tesouro Nacional sobre as três funções."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0571
    {
        "id": "ECO-E1-0571-1", "fonte_ref": "E1-0571", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o princípio do benefício, uma tributação justa é aquela que faz com que o indivíduo "
                      "pague o tributo de modo a igualar o preço do serviço recebido ao benefício marginal que ele "
                      "aufere com sua utilização."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o princípio do benefício, uma tributação justa é aquela que faz com que o indivíduo "
                      "pague o tributo de modo a igualar o preço do serviço recebido ao <u>benefício "
                      "marginal</u> que ele aufere com sua utilização."),
        "poucas": ("No " + azb("princípio do benefício") + " o tributo funciona como um <b>preço</b>: cada um "
                   "paga pelo serviço público o equivalente ao " + azb("benefício marginal") + " que obtém, como "
                   "num mercado."),
        "destrinchando": [
            "Dois critérios clássicos de justiça tributária: o " + azb("princípio do benefício") + " (paga quem "
            "usa, na medida do benefício) e o da " + azb("capacidade de pagamento") + " (paga quem pode, na "
            "medida da renda ou da riqueza).",
            "No do benefício, a referência é o mercado: lá, o consumidor compra até o ponto em que o preço iguala "
            "o benefício marginal. Aplicado ao setor público, gera os " + azb("preços de Lindahl") + " (" + oc("Erik "
            "Lindahl") + ", na tradição de " + oc("Wicksell") + "): cada um paga uma parcela do custo do bem "
            "público igual à sua valoração marginal, e a soma das parcelas cobre o custo.",
            "Onde ele funciona: serviços com usuário identificável e exclusão possível — " + azb("taxas")
            + " (emissão de passaporte, coleta de lixo), pedágio, " + azb("contribuição de melhoria") + " "
            "(valorização do imóvel por obra pública).",
            "Onde ele falha: bens públicos puros, porque ninguém revela o benefício que tira (carona) — e ele "
            "não tem vocação redistributiva: quem recebe mais do Estado pagaria mais, o que inviabilizaria "
            "transferências aos pobres.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definição de manual com um termo técnico decisivo: "
                       "“benefício <b>marginal</b>”. A banca poderia trocar por “benefício total” ou “custo "
                       "marginal de produção”, ou atribuir a definição à capacidade de pagamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o princípio da capacidade de pagamento, cada indivíduo deve pagar tributo igual ao "
            "benefício marginal que aufere dos serviços públicos.”</i> → ERRADO (troca de conceito: é o "
            "princípio do benefício)",
            "<i>“O princípio do benefício é o fundamento usual das taxas cobradas por serviços públicos "
            "divisíveis.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. O princípio do benefício defende que os indivíduos paguem tributos "
                             "proporcionalmente ao benefício que recebem dos serviços públicos, como se fosse o "
                             "preço desses serviços."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0572
    {
        "id": "ECO-E1-0572-1", "fonte_ref": "E1-0572", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Observa-se o princípio da neutralidade tributária quando as decisões alocativas dos "
                      "diferentes agentes são afetadas por alterações dos preços relativos desencadeadas pela "
                      "tributação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Observa-se o princípio da neutralidade tributária quando as decisões alocativas dos "
                       "diferentes agentes ") + vm("são afetadas") + az(" por alterações dos preços relativos "
                                                                         "desencadeadas pela tributação.")),
        "poucas": ("Tributo " + azb("neutro") + " é o que <b>não</b> altera preços relativos nem, portanto, as "
                   "decisões de consumir, produzir e investir. O item descreve a quebra da neutralidade."),
        "destrinchando": [
            "Pelo " + azb("princípio da neutralidade") + ", o sistema tributário deve arrecadar sem distorcer a "
            "alocação que o mercado faria: os agentes escolhem o que consumir, como produzir e onde investir "
            "como se o tributo não existisse.",
            "Quando o tributo muda preços relativos, os agentes trocam o bem tributado por outros, produzem "
            "menos e deixam de fazer trocas vantajosas: surge o " + azb("excesso de carga")
            + " (peso morto), custo de eficiência além do valor arrecadado.",
            "Neutralidade perfeita só o " + azb("tributo lump-sum") + " (valor fixo, que não depende de nenhuma "
            "decisão). Na prática, busca-se reduzir distorções: base ampla, alíquota uniforme, não "
            "cumulatividade. O IVA dual (CBS e IBS) da reforma tributária do " + rx("Brasil") + " (" + vd("EC "
            "132/2023") + ") foi justificado pela neutralidade, contra a cumulatividade e a guerra fiscal do "
            "modelo antigo.",
            "Exceção deliberada: tributos " + azb("extrafiscais") + " e " + azb("pigouvianos") + " (cigarro, "
            "poluição) querem <b>mudar</b> comportamentos — abrem mão da neutralidade para corrigir "
            "externalidades.",
            vm("Regra-âncora: neutro = não altera preços relativos nem decisões; se altera, há distorção."),
        ],
        "dissecando": (cz("[inversão]") + " O item pega a descrição da distorção e a chama de neutralidade: "
                       "trocou-se “não são afetadas” por “são afetadas”. O resto (decisões alocativas, preços "
                       "relativos, tributação) é vocabulário correto, o que dá ar de verdade à frase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto de valor fixo por pessoa, independente de renda ou consumo, aproxima-se da "
            "neutralidade plena.”</i> → CERTO",
            "<i>“Tributos cumulativos, em cascata, favorecem a neutralidade por incidirem em todas as etapas "
            "da produção.”</i> → ERRADO (inversão: a cascata distorce e induz verticalização)",
        ])],
        "reescrita": ("Observa-se o princípio da neutralidade tributária quando as decisões alocativas dos "
                      "diferentes agentes " + hl("não são afetadas") + " por alterações dos preços relativos "
                      "desencadeadas pela tributação."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A neutralidade exige que a tributação não afete as decisões alocativas; se "
                             "os preços relativos mudam e as escolhas também, a neutralidade não é respeitada."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0573
    {
        "id": "ECO-E1-0573-1", "fonte_ref": "E1-0573", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("A adoção de um Imposto de Renda regressivo, embora contrarie orientações redistributivas, "
                      "atende o princípio da capacidade de pagamento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A adoção de um Imposto de Renda regressivo, ") + vm("embora contrarie")
                    + az(" orientações redistributivas, ") + vm("atende") + az(" o princípio da capacidade de "
                                                                              "pagamento.")),
        "poucas": ("A " + azb("capacidade de pagamento") + " pede que quem tem mais renda contribua com "
                   "<b>parcela maior</b>; um IR " + azb("regressivo") + " faz o contrário e viola o princípio, "
                   "não o atende."),
        "destrinchando": [
            "O " + azb("princípio da capacidade de pagamento") + " (ou capacidade contributiva) gradua o tributo "
            "pela renda ou riqueza de cada um. Tem duas faces: " + azb("equidade horizontal") + " (quem tem a "
            "mesma capacidade paga o mesmo) e " + azb("equidade vertical") + " (quem tem mais capacidade paga "
            "mais).",
            "A equidade vertical é a base da " + azb("progressividade") + ": alíquota efetiva crescente com a "
            "renda. No " + rx("Brasil") + ", a " + vd("CF/1988, art. 145, § 1º") + " manda graduar os impostos "
            "“segundo a capacidade econômica do contribuinte”, e o art. 153, § 2º, I, exige que o IR seja "
            "informado pela progressividade.",
            "Imposto " + azb("regressivo") + " = alíquota efetiva que cai quando a renda sobe: o pobre "
            "compromete fração maior da renda que o rico. Fere a equidade vertical e, logo, a capacidade de "
            "pagamento.",
            "Por isso não há o contraste sugerido pelo “embora”: capacidade de pagamento e orientação "
            "redistributiva apontam no mesmo sentido. Quem se opõe à lógica redistributiva é o "
            + azb("princípio do benefício") + ", que cobra pelo uso, não pela renda.",
        ],
        "dissecando": (cz("[contradição · nexo indevido]") + " O conector concessivo “embora” fabrica uma "
                       "oposição falsa entre redistribuição e capacidade de pagamento, que andam juntas. Ao "
                       "admitir que o tributo contraria a redistribuição, o próprio item entrega o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto de renda progressivo é a expressão típica do princípio da capacidade de "
            "pagamento.”</i> → CERTO",
            "<i>“O princípio da capacidade de pagamento concretiza-se apenas com alíquotas progressivas, sendo "
            "incompatível com alíquotas proporcionais.”</i> → ERRADO (restrição indevida: a proporcional já "
            "cobra mais, em valor, de quem ganha mais)",
        ])],
        "reescrita": ("A adoção de um Imposto de Renda regressivo, " + hl("além de contrariar") + " orientações "
                      "redistributivas, " + hl("viola") + " o princípio da capacidade de pagamento."),
        "tipo_erro": ["CONTRADICAO", "NEXO_INDEVIDO"], "moduladores": ["embora"], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A capacidade de pagamento exige que quem tem mais pague mais "
                             "proporcionalmente; o imposto regressivo onera proporcionalmente mais os de menor "
                             "renda."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0574
    {
        "id": "ECO-E1-0574-1", "fonte_ref": "E1-0574", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("O princípio da equidade é observado quando o ônus da tributação é distribuído de maneira "
                      "justa entre os indivíduos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O princípio da equidade é observado quando o ônus da tributação é distribuído de maneira "
                      "<u>justa</u> entre os indivíduos."),
        "poucas": ("É a definição de " + azb("equidade tributária") + ": repartir o ônus de forma justa. O "
                   "debate está em <b>como</b> medir o justo — pelo benefício ou pela capacidade de pagamento."),
        "destrinchando": [
            "Os princípios clássicos de um bom sistema tributário: " + azb("equidade") + ", "
            + azb("neutralidade") + " (eficiência), " + azb("simplicidade") + " e " + azb("progressividade")
            + " — já presentes nos cânones de " + oc("Adam Smith") + " (<i>A Riqueza das Nações</i>, 1776), "
            "cujo primeiro cânone pede que cada um contribua na proporção de sua capacidade.",
            "Equidade = distribuição <b>justa</b> do ônus. Dois critérios para dizer o que é justo: o "
            + azb("princípio do benefício") + " (paga mais quem mais usa os serviços públicos) e o da "
            + azb("capacidade de pagamento") + " (paga mais quem tem mais renda ou riqueza).",
            "Dentro da capacidade de pagamento: " + azb("equidade horizontal") + " — iguais pagam igual (duas "
            "famílias com a mesma renda não podem pagar valores diferentes por causa da fonte da renda) — e "
            + azb("equidade vertical") + " — desiguais pagam desigualmente, base da progressividade.",
            "Conflito clássico: equidade × eficiência. Tributar mais as bases inelásticas reduz o peso morto "
            "(regra de " + oc("Ramsey") + "), mas bens de demanda inelástica, como alimentos, pesam mais no "
            "orçamento dos pobres — a tributação mais eficiente tende a ser menos equitativa.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição genérica, sem armadilha de modulador. A banca "
                       "costuma fabricar o ERRADO trocando a equidade pela neutralidade (“não alterar decisões”) "
                       "ou dizendo que a progressividade a contraria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A equidade horizontal exige que contribuintes com maior capacidade econômica paguem mais "
            "tributo.”</i> → ERRADO (troca de conceito: isso é equidade vertical)",
            "<i>“O princípio da equidade é observado quando a tributação não altera os preços relativos da "
            "economia.”</i> → ERRADO (troca de conceito: é a neutralidade)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A equidade está ligada à justiça distributiva e busca que a carga recaia de "
                             "forma justa, respeitando as diferenças de capacidade de pagamento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0575
    {
        "id": "ECO-E1-0575-1", "fonte_ref": "E1-0575", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Nas relações entre tributação e atividade econômica: os impostos regressivos geram uma "
                      "contribuição proporcionalmente maior que o incremento ocorrido na renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nas relações entre tributação e atividade econômica: os impostos ") + vm("regressivos")
                    + az(" geram uma contribuição proporcionalmente maior que o incremento ocorrido na renda.")),
        "poucas": ("Imposto cuja arrecadação cresce " + azb("mais que proporcionalmente") + " à renda é "
                   + azb("progressivo") + " (elasticidade-renda > 1). No regressivo, o imposto cresce menos que "
                   "a renda."),
        "destrinchando": [
            "Classificação pela relação entre o imposto (T) e a renda (Y), ou seja, pela " + azb("alíquota "
            "média") + " T/Y: " + vd("progressivo") + " → T/Y sobe com Y (o imposto cresce mais que a renda); "
            + vd("proporcional") + " → T/Y constante; " + vd("regressivo") + " → T/Y cai com Y (o imposto "
            "cresce menos que a renda, ou nem cresce).",
            "Em elasticidade: ε = %ΔT ÷ %ΔY. ε > 1 → progressivo; ε = 1 → proporcional; ε < 1 → regressivo. "
            "O item descreve ε > 1 e dá o nome errado.",
            "Exemplos: IR com alíquotas marginais crescentes (renda 10% maior → imposto mais de 10% maior) é "
            "progressivo; um tributo de valor fixo por pessoa é o caso extremo de regressivo (a renda dobra e o "
            "imposto fica igual, então T/Y cai pela metade); o ICMS sobre alimentos tende a ser regressivo, porque "
            "o consumo cresce menos que a renda.",
            "Consequência macro: tributos progressivos são " + azb("estabilizadores automáticos") + " mais "
            "potentes — na expansão a arrecadação sobe mais que a renda e freia a demanda; na recessão, cai mais "
            "que a renda e amortece a queda.",
            vm("Regra-âncora: imposto cresce mais que a renda → progressivo; menos → regressivo."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A definição está correta, só o rótulo foi trocado. A "
                       "redação indireta (“contribuição proporcionalmente maior que o incremento”) obriga a "
                       "traduzir para T/Y antes de julgar — quem associa “maior” a “pior para o pobre” cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os impostos progressivos geram uma contribuição proporcionalmente maior que o incremento "
            "ocorrido na renda.”</i> → CERTO",
            "<i>“Um imposto de valor fixo por contribuinte é proporcional, pois todos pagam o mesmo "
            "montante.”</i> → ERRADO (troca de conceito: T/Y cai com a renda — é regressivo)",
        ])],
        "reescrita": ("Nas relações entre tributação e atividade econômica: os impostos " + hl("progressivos")
                      + " geram uma contribuição proporcionalmente maior que o incremento ocorrido na renda."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("ERRADO. Impostos regressivos oneram proporcionalmente mais os mais pobres, "
                             "independentemente do crescimento da renda; a frase está mal formulada."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0576
    {
        "id": "ECO-E1-0576-1", "fonte_ref": "E1-0576", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Sobre a estrutura tributária de um país: a produtividade dos tributos em contribuir com a "
                      "receita fiscal é medida pelos coeficientes de elasticidade de receita em relação à renda "
                      "nacional para diferentes alternativas de tributação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sobre a estrutura tributária de um país: a produtividade dos tributos em contribuir com a "
                      "receita fiscal é medida pelos coeficientes de <u>elasticidade de receita em relação à "
                      "renda nacional</u> para diferentes alternativas de tributação."),
        "poucas": ("A " + azb("produtividade") + " de um tributo é sua capacidade de gerar receita à medida que "
                   "a economia cresce, medida pela " + azb("elasticidade-renda da arrecadação") + " (%ΔT ÷ "
                   "%ΔY)."),
        "destrinchando": [
            "Coeficiente: ε = %Δarrecadação ÷ %Δrenda. Com " + vd("ε > 1") + ", a receita cresce mais que a "
            "renda e a carga sobe sozinha com o crescimento; com " + vd("ε < 1") + ", a receita perde terreno e "
            "o governo precisa de novos tributos ou de alíquotas maiores para manter a carga.",
            "Comparar os coeficientes de várias alternativas (IR, tributos sobre consumo, sobre patrimônio, "
            "sobre comércio exterior) diz quais bases acompanham melhor a expansão da economia — critério de "
            "planejamento da estrutura tributária.",
            "O que eleva a elasticidade: alíquotas progressivas (a renda sobe e o contribuinte salta de faixa), "
            "bases que crescem mais que o PIB (renda urbana formal, consumo de bens duráveis). O que a reduz: "
            "tributos específicos em valor fixo (não acompanham preços), bases estreitas, muitas isenções.",
            "Ligação com a política fiscal: tributos de alta elasticidade são também " + azb("estabilizadores "
            "automáticos") + " mais fortes, porque a arrecadação oscila mais que a renda ao longo do ciclo.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Formulação técnica e pouco intuitiva, típica de "
                       "manual de finanças públicas. O risco é estranhar “produtividade” (palavra que lembra "
                       "eficiência produtiva) e marcar ERRADO; aqui ela significa capacidade de arrecadar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um tributo com elasticidade-renda da receita inferior à unidade amplia sua participação na "
            "arrecadação quando a economia cresce.”</i> → ERRADO (inversão: perde participação)",
            "<i>“Alíquotas progressivas tendem a elevar a elasticidade-renda da arrecadação.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("CERTO. A produtividade tributária é analisada pela elasticidade-receita, que mede "
                             "quanto a arrecadação varia proporcionalmente em resposta a variações na renda "
                             "nacional."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0577
    {
        "id": "ECO-E1-0577-1", "fonte_ref": "E1-0577", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("O sistema tributário brasileiro revela que a incidência de impostos indiretos é "
                      "necessariamente regressiva em termos da equidade da distribuição pessoal da renda "
                      "disponível."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O sistema tributário brasileiro revela que a incidência de impostos indiretos é "
                      "<u>necessariamente</u> regressiva em termos da equidade da distribuição pessoal da renda "
                      "disponível."),
        "poucas": ("Tributos indiretos incidem sobre o " + azb("consumo") + ", que pesa mais na renda dos pobres; "
                   "no " + rx("Brasil") + ", onde eles dominam a arrecadação, o efeito agregado é "
                   + azb("regressivo") + "."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O “necessariamente” é forte demais para a teoria: com " + azb("seletividade")
                          + " (alíquotas maiores sobre bens de luxo e menores ou nulas sobre a cesta básica), um "
                          "imposto indireto pode ser neutro ou até progressivo em relação à renda. O CERTO se "
                          "sustenta como leitura do caso brasileiro — em que a regressividade dos indiretos é "
                          "achado empírico constante —, não como regra lógica. Numa prova CEBRASPE, o mesmo "
                          "item formulado em abstrato tenderia a ser ERRADO.")],
        "destrinchando": [
            azb("Impostos indiretos") + " (ICMS, IPI, ISS, PIS/Cofins e, após a reforma, IBS e CBS) incidem "
            "sobre bens e serviços e são repassados ao preço: o contribuinte de fato é o consumidor. "
            + azb("Diretos") + " (IR, IPTU, IPVA) incidem sobre renda e patrimônio de quem os paga.",
            "Por que tendem à regressividade: a família pobre consome quase toda a renda; a rica poupa uma "
            "parte. Com a mesma alíquota sobre o consumo, o imposto representa fatia maior da renda disponível "
            "de quem ganha menos.",
            "No " + rx("Brasil") + ", a tributação sobre bens e serviços responde por perto de " + vd("40% da "
            "arrecadação") + " ⏳ (out/2026), bem acima da média da OCDE, e os estudos de incidência com dados "
            "da POF (IBGE) mostram que o peso dos indiretos na renda das famílias mais pobres é várias vezes o "
            "peso nas mais ricas.",
            "Instrumentos que atenuam: " + azb("seletividade") + " (IPI e ICMS por essencialidade), alíquota "
            "zero da cesta básica e o " + azb("cashback") + " para famílias de baixa renda previsto na reforma "
            "tributária (" + vd("EC 132/2023") + ").",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " O item mistura uma constatação empírica (o caso "
                       "brasileiro) com um modulador absoluto (“necessariamente”), que normalmente sinaliza "
                       "ERRADO. O gabarito da fonte privilegiou a constatação; em itens assim, o 🔥 padrão "
                       "CEBRASPE é punir o absoluto quando há exceção teórica (seletividade)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No Brasil, os tributos indiretos tendem a ser regressivos, pois as famílias de menor renda "
            "destinam ao consumo maior parcela de seus rendimentos.”</i> → CERTO",
            "<i>“A seletividade das alíquotas impede, por definição, que tributos indiretos sejam "
            "regressivos.”</i> → ERRADO (modulador absoluto: atenua, não impede)",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["necessariamente"], "dificuldade": 2,
        "comentario_fonte": ("CERTO. Impostos indiretos (ICMS, IPI, PIS/Cofins) incidem sobre o consumo e afetam "
                             "proporcionalmente mais os pobres, que gastam maior parcela da renda em bens "
                             "tributados."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: “necessariamente” é absoluto; com seletividade, tributos indiretos podem não "
                    "ser regressivos — o CERTO da fonte vale como constatação do caso brasileiro"],
    },
    # ------------------------------------------------------------------ E1-0578
    {
        "id": "ECO-E1-0578-1", "fonte_ref": "E1-0578", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Uma estrutura tributária com maior parcela de impostos diretos será obrigatoriamente mais "
                      "progressiva."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma estrutura tributária com maior parcela de impostos diretos ")
                    + vm("será obrigatoriamente") + az(" mais progressiva.")),
        "poucas": ("Impostos diretos " + azb("tendem") + " a ser mais progressivos, mas não "
                   "<b>obrigatoriamente</b>: isenções, alíquotas planas e brechas podem anular a "
                   "progressividade."),
        "destrinchando": [
            "Direto × indireto diz respeito à <b>base</b> (renda e patrimônio × consumo); progressivo × "
            "regressivo diz respeito ao <b>perfil da alíquota efetiva</b> ao longo da renda. São classificações "
            "independentes: o vínculo entre elas é tendência, não regra.",
            "Por que tendem: a renda e o patrimônio permitem alíquotas graduadas e personalizadas (faixas, "
            "deduções, isenção dos mais pobres), o que o imposto sobre consumo não permite.",
            "Por que não é obrigatório: um IR de " + azb("alíquota única") + " (<i>flat tax</i>, adotado em "
            "países do Leste Europeu) é proporcional; contribuições sobre a folha com teto são regressivas no "
            "topo; e isenções concentradas nas rendas altas quebram a progressividade.",
            "Caso " + rx("brasileiro") + ": a isenção de lucros e dividendos distribuídos (desde 1995) e a "
            "tributação de rendas de capital em alíquotas exclusivas faziam a alíquota efetiva do IRPF "
            + vd("cair") + " no topo da distribuição — o IR, imposto direto por excelência, tornava-se "
            "regressivo para os mais ricos. A reforma de 2025 criou tributação mínima das altas rendas para "
            "atacar esse ponto ⏳ (out/2026).",
        ],
        "dissecando": (cz("[modulador absoluto]") + " O núcleo é verdadeiro como tendência; o "
                       "“obrigatoriamente” o transforma em lei. 🔥 Em tributação, “necessariamente”, "
                       "“obrigatoriamente” e “sempre” ligando direto/indireto a progressivo/regressivo são o "
                       "erro mais comum."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma estrutura tributária com maior parcela de impostos diretos tende a ser mais "
            "progressiva.”</i> → CERTO",
            "<i>“Todo imposto sobre a renda é progressivo, por incidir sobre a capacidade contributiva.”</i> → "
            "ERRADO (modulador absoluto: há IR de alíquota única)",
        ])],
        "reescrita": ("Uma estrutura tributária com maior parcela de impostos diretos " + hl("tende a ser")
                      + " mais progressiva."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["obrigatoriamente"], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. Impostos diretos tendem a ser mais progressivos (IRPF), mas a "
                             "progressividade pode ser anulada por brechas, isenções ou alíquotas mal calibradas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0579
    {
        "id": "ECO-E1-0579-1", "fonte_ref": "E1-0579", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("A carga tributária é definida como a parcela da renda das famílias destinada aos cofres do "
                      "setor público."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A carga tributária é definida como a parcela ") + vm("da renda das famílias")
                    + az(" destinada aos cofres do setor público.")),
        "poucas": ("A " + azb("carga tributária") + " mede o total arrecadado em tributos (de famílias "
                   "<b>e</b> empresas, nas três esferas) em proporção do " + vd("PIB") + ", não da renda das "
                   "famílias."),
        "destrinchando": [
            "Definição: " + vd("CTB = arrecadação tributária total ÷ PIB") + ". O numerador soma impostos, "
            "taxas e contribuições (inclusive previdenciárias) da União, dos estados e dos municípios.",
            "Por que não “renda das famílias”: parte relevante dos tributos é recolhida pelas empresas (IRPJ, "
            "CSLL, contribuições sobre a folha e o faturamento) e incide sobre lucros e transações, não só sobre "
            "a renda pessoal. O denominador também é outro: o PIB mede toda a renda gerada no país, não só a "
            "das famílias.",
            "Mesmo que, ao fim, todo tributo seja pago por pessoas (consumidores, trabalhadores ou acionistas), "
            "a <b>medida</b> de carga não acompanha esse caminho: ela relaciona arrecadação e produto agregado.",
            "Medidas vizinhas: " + azb("carga tributária líquida") + " (bruta menos transferências, subsídios e "
            "juros pagos pelo governo) e, para a família, a " + azb("alíquota efetiva") + " (tributos pagos ÷ "
            "renda), usada nos estudos de progressividade. No " + rx("Brasil") + ", a CTB fica perto de "
            + vd("um terço do PIB") + " ⏳ (out/2026).",
        ],
        "dissecando": (cz("[troca de conceito · restrição indevida]") + " Troca a base da medida (PIB) por um "
                       "agregado menor (renda das famílias), restringindo quem paga. A frase soa intuitiva — "
                       "“quanto do que ganho vai para o governo” —, e é por isso que engana."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A carga tributária bruta corresponde à razão entre a arrecadação total de tributos das três "
            "esferas de governo e o produto interno bruto.”</i> → CERTO",
            "<i>“A carga tributária líquida é sempre superior à bruta.”</i> → ERRADO (inversão: a líquida "
            "desconta as transferências)",
        ])],
        "reescrita": ("A carga tributária é definida como a parcela " + hl("do produto interno bruto (PIB)")
                      + " destinada aos cofres do setor público."),
        "tipo_erro": ["TROCA_CONCEITO", "RESTRICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A carga tributária é a relação entre o total arrecadado pelo Estado "
                             "(impostos, contribuições e taxas) e o PIB, não apenas a renda das famílias."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0380-1 (outro item sobre a definição de carga tributária)"],
    },
]
