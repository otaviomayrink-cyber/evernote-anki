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
]
