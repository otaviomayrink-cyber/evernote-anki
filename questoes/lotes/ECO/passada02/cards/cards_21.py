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
]
