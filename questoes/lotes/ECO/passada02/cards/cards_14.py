"""Cards do lote de redação 14 — ECO, passada 02 (notas 29: curva de Phillips; 30: síntese neoclássica e
debate contemporâneo; 35: economia monetária)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "phil": "📉 Phillips original e aceleracionista",
    "exp": "🔮 Expectativas e NAIRU",
    "deb": "🗣️ Debate contemporâneo",
    "fun": "🪙 Funções e agregados monetários",
    "mult": "🏦 Criação de moeda e multiplicador",
}

CMD_NAB_918 = ("Em relação à curva de Phillips e à formação de expectativas dos agentes, julgue (C ou E) os itens a "
               "seguir.")
CMD_NAB_TEORIAS = "Sobre as teorias macroeconômicas, julgue (C ou E) os seguintes itens."
CMD_NAB_MACRO = "Em relação à teoria macroeconômica, julgue (C ou E) os itens a seguir."
CMD_NAB_PH_OA = ("Em relação à Curva de Phillips e ao modelo de oferta e demanda agregada, julgue (C ou E) os itens a "
                 "seguir.")
CMD_RT_INF = "Julgue os itens seguintes, a respeito da relação entre inflação e desemprego na macroeconomia."
CMD_RT_PAND = ("Durante a pandemia, a taxa de desemprego aumentou muito no Brasil e em todo o mundo. A respeito dos "
               "conceitos de desemprego e das suas relações com a inflação e atividade econômica, julgue os itens a "
               "seguir.")
CMD_RT_REL = "Sobre a relação entre inflação e desemprego, julgue os itens a seguir."
CMD_DANIEL = "Julgue o item a seguir, relativo à moeda e aos agregados monetários."

CARDS = [
    # ------------------------------------------------------------------ E2-L00918
    {
        "id": "ECO-E2-L00918-1", "fonte_ref": "E2-L00918", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_918,
        "rotulo_item": "Item",
        "assertiva": ("Na versão forte das expectativas racionais, na média a expectativa de inflação é igual a "
                      "inflação efetiva."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na versão forte das expectativas racionais, <u>na média</u> a expectativa de inflação é "
                      "igual a inflação efetiva."),
        "poucas": ("Na " + azb("versão forte") + " das expectativas racionais, o erro de previsão tem "
                   + vd("média zero") + " e é imprevisível: os agentes erram, mas não erram sistematicamente — "
                   "logo, em média, πᵉ = π."),
        "destrinchando": [
            "Formalmente: π = E[π | informação disponível] + ε, com " + vd("E[ε] = 0") + " e ε não correlacionado "
            "com nada que já se sabia (inclusive os erros passados). É a hipótese de " + oc("John Muth")
            + " (1961), levada à macroeconomia por " + oc("Robert Lucas") + ", " + oc("Thomas Sargent") + " e "
            + oc("Neil Wallace") + " nos anos 1970.",
            "Expectativas racionais <b>não</b> são previsão perfeita. Choques imprevisíveis (uma quebra de safra, "
            "uma guerra) fazem a inflação efetiva divergir da esperada; o que a hipótese exclui é o erro "
            + azb("sistemático") + " — errar sempre para o mesmo lado ou repetir o padrão do período anterior.",
            "Versão <b>fraca</b> × <b>forte</b>: na fraca, os agentes usam da melhor forma a informação de que "
            "dispõem, que pode ser incompleta; na forte, conhecem o modelo verdadeiro da economia (inclusive a regra "
            "de política do banco central), e a expectativa subjetiva coincide com a esperança matemática do "
            "modelo.",
            "Contraste com as " + azb("expectativas adaptativas") + " (πᵉₜ = πₜ₋₁ ou média ponderada do passado): "
            "com inflação acelerando, o agente adaptativo subestima a inflação período após período — exatamente o "
            "erro sistemático que as racionais proíbem.",
            vm("Regra-âncora: expectativas racionais = acerto em média, erro aleatório; não = acerto sempre."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Reproduz a definição de manual. O risco está na leitura "
                       "apressada que troca “na média” por “sempre”: quem acha que expectativas racionais exigem "
                       "previsão perfeita marca ERRADO. O “na média” é exatamente o que salva o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na versão forte das expectativas racionais, a expectativa de inflação é sempre igual à inflação "
            "efetiva.”</i> → ERRADO (modulador absoluto: há erros aleatórios)",
            "<i>“Sob expectativas racionais, os erros de previsão de inflação não são autocorrelacionados.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["na média"], "dificuldade": 1,
        "comentario_fonte": ("Versão forte: expectativas coincidem, em média, com os valores verdadeiros; erros "
                             "aleatórios e não relacionados ao passado; não é previsão perfeita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00919
    {
        "id": "ECO-E2-L00919-1", "fonte_ref": "E2-L00919", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_918,
        "rotulo_item": "Item",
        "assertiva": ("A curva de Phillips baseou-se no que Friedman chamou de doutrina-padrão: elevação da renda leva "
                      "a aumento do produto e do emprego. Essa curva relaciona inflação e emprego: taxas baixas de "
                      "emprego podem ser obtidas com taxas mais altas de inflação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva de Phillips baseou-se no que Friedman chamou de doutrina-padrão: elevação da renda "
                       "leva a aumento do produto e do emprego. Essa curva relaciona inflação e emprego: taxas baixas "
                       "de ") + vm("emprego") + az(" podem ser obtidas com taxas mais altas de inflação.")),
        "poucas": ("O trade-off de Phillips é entre inflação e " + azb("desemprego") + ": inflação mais alta "
                   "compra desemprego <b>mais baixo</b> (ou emprego mais alto) — e, depois de " + oc("Friedman")
                   + ", só no " + vd("curto prazo") + "."),
        "destrinchando": [
            oc("A. W. Phillips") + " (1958) encontrou, nos dados do Reino Unido de " + vd("1861–1957")
            + ", uma relação <b>inversa</b> entre desemprego e variação dos salários nominais. " + oc("Samuelson")
            + " e " + oc("Solow") + " (1960) a reescreveram com a inflação de preços no eixo vertical e a "
            "apresentaram como um “cardápio” de política.",
            "Lógica do mercado de trabalho: com desemprego baixo, os trabalhadores têm mais poder de barganha, os "
            "salários sobem mais depressa e as empresas repassam aos preços. Portanto " + vd("u ↓ ↔ π ↑")
            + " — equivalentemente, emprego ↑ ↔ π ↑.",
            "O item inverte a direção: “taxas baixas de emprego” (desemprego alto) obtidas com inflação mais alta "
            "seria a " + azb("estagflação") + ", o fenômeno dos anos 1970 que a curva original não explicava.",
            "Leitura moderna: a curva negativamente inclinada vale no " + azb("curto prazo") + ", dada a inflação "
            "esperada; no longo prazo (" + oc("Friedman") + " 1968, " + oc("Phelps") + " 1967) ela é vertical na "
            "taxa natural de desemprego.",
            vm("Regra-âncora: Phillips = inflação × DESemprego, relação inversa (no curto prazo)."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item gasta uma linha inteira de contexto "
                       "plausível e esconde o erro numa sílaba: “emprego” no lugar de “desemprego”. Quem lê "
                       "rápido vê “baixo … com inflação alta” e confirma por reflexo. 🔥 Em Phillips, confira sempre "
                       "qual variável está no eixo horizontal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…taxas baixas de desemprego podem ser obtidas com taxas mais altas de inflação no curto "
            "prazo.”</i> → CERTO",
            "<i>“…taxas baixas de desemprego podem ser mantidas permanentemente com inflação estável e mais "
            "alta.”</i> → ERRADO (contradiz a aceleracionista: exigiria inflação crescente)",
        ])],
        "reescrita": ("A curva de Phillips baseou-se no que Friedman chamou de doutrina-padrão: elevação da renda leva "
                      "a aumento do produto e do emprego. Essa curva relaciona inflação e emprego: taxas baixas de "
                      + hl("desemprego") + " podem ser obtidas com taxas mais altas de inflação."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Taxas baixas de desemprego podem ser obtidas com taxas mais altas de inflação no curto prazo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01007
    {
        "id": "ECO-E2-L01007-1", "fonte_ref": "E2-L01007", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a versão aceleracionista da Curva de Phillips, quando a taxa de desemprego excede "
                      "a taxa natural de desemprego, a taxa de inflação aumenta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a versão aceleracionista da Curva de Phillips, quando a taxa de desemprego "
                       "excede a taxa natural de desemprego, a taxa de inflação ") + vm("aumenta") + az(".")),
        "poucas": ("Na aceleracionista, " + vd("πₜ − πₜ₋₁ = −α(uₜ − uₙ)") + ": desemprego <b>acima</b> da taxa "
                   "natural faz a inflação <b>cair</b>; abaixo dela, acelerar."),
        "destrinchando": [
            "Com expectativas adaptativas simples (πᵉₜ = πₜ₋₁), a curva de Phillips aumentada pelas expectativas "
            "πₜ = πᵉₜ − α(uₜ − uₙ) vira " + vd("Δπₜ = −α(uₜ − uₙ)") + ". O que o desemprego determina é a "
            "<b>variação</b> da inflação, não o seu nível — daí o nome “aceleracionista”.",
            "Três casos: u < uₙ → Δπ > 0 (inflação acelera); " + vd("u = uₙ → Δπ = 0") + " (inflação estável); "
            "u > uₙ → Δπ < 0 (inflação desacelera). Por isso a taxa natural também é chamada de "
            + azb("NAIRU") + " — a taxa de desemprego que não acelera a inflação.",
            "Intuição: desemprego acima do natural = folga no mercado de trabalho → reajustes salariais menores que "
            "a inflação passada → inflação corrente abaixo da do período anterior. É o custo de uma "
            + azb("desinflação") + ": para baixar a inflação, mantém-se o desemprego acima de uₙ por algum tempo.",
            "Com choque de oferta (ε), a equação fica Δπ = −α(u − uₙ) + ε: um choque adverso pode elevar a "
            "inflação mesmo com desemprego alto — mas isso é o choque, não o desemprego.",
            vm("Regra-âncora: u > uₙ → inflação cai; u < uₙ → inflação sobe."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sinal da relação. A pista é “excede”: desemprego acima do "
                       "natural é folga, e folga não pressiona preços. 🔥 Nabuco e CEBRASPE gostam de pedir o "
                       "sentido da aceleração a partir da equação Δπ = −α(u − uₙ)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…quando a taxa de desemprego é inferior à taxa natural, a taxa de inflação aumenta.”</i> → CERTO",
            "<i>“…quando a taxa de desemprego excede a taxa natural, o nível de preços cai.”</i> → ERRADO (troca de "
            "conceito: cai a taxa de inflação, não necessariamente o nível de preços)",
        ])],
        "reescrita": ("De acordo com a versão aceleracionista da Curva de Phillips, quando a taxa de desemprego excede "
                      "a taxa natural de desemprego, a taxa de inflação " + hl("diminui") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Verso só com imagem: fórmula da aceleracionista, πₜ − πₜ₋₁ = −α(uₜ − uₙ) + choque, "
                             "com a marca ERRADO."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 168", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "texto (fórmula transcrita no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01351
    {
        "id": "ECO-E2-L01351-1", "fonte_ref": "E2-L01351", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria novo clássica, os agentes econômicos formam expectativas racionais, o "
                      "que significa, entre outros aspectos, que não cometem erros sistemáticos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a teoria novo clássica, os agentes econômicos formam expectativas racionais, o "
                      "que significa, entre outros aspectos, que não cometem erros <u>sistemáticos</u>."),
        "poucas": ("Expectativas racionais permitem erros, mas só " + azb("aleatórios") + ": os erros de períodos "
                   "diferentes não são correlacionados, e em média as expectativas acertam."),
        "destrinchando": [
            "Os " + oc("novos clássicos") + " (" + oc("Lucas") + ", " + oc("Sargent") + ", " + oc("Wallace")
            + ", " + oc("Barro") + ") combinam três hipóteses: " + azb("expectativas racionais") + ", "
            + azb("preços e salários flexíveis") + " (mercados se equilibram continuamente) e agentes "
            "maximizadores.",
            "Expectativas racionais: os agentes usam toda a informação disponível, inclusive o modelo que descreve a "
            "economia, da forma mais eficiente possível. Se cometessem erros sistemáticos, perceberiam o padrão e o "
            "corrigiriam — persistir no erro não seria racional.",
            "Consequência de política: só choques " + azb("não antecipados") + " (surpresas) afetam produto e "
            "emprego; regras sistemáticas e previsíveis são incorporadas às expectativas e afetam apenas preços — é "
            "a " + azb("proposição da ineficácia da política") + " de Sargent e Wallace (1975).",
            "Contraste: com " + azb("expectativas adaptativas") + " (" + oc("Friedman") + "), quem olha só o passado "
            "erra sistematicamente quando a inflação acelera, e é esse erro que abre espaço para o trade-off de curto "
            "prazo.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definição de manual. O qualificador “sistemáticos” "
                       "protege o item; a armadilha seria a versão sem ele (“não cometem erros”), que é ERRADA."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo os novos clássicos, os agentes não cometem erros de previsão.”</i> → ERRADO (modulador "
            "absoluto: erros aleatórios existem)",
            "<i>“Com expectativas racionais, uma expansão monetária não antecipada pode elevar o produto "
            "temporariamente.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["entre outros aspectos"], "dificuldade": 1,
        "comentario_fonte": ("Em média as expectativas estão corretas; erros de tempos em tempos, mas não sistemáticos "
                             "nem autocorrelacionados; uso eficiente da informação e da estrutura do modelo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00918-1 cobra a mesma ideia (acerto em média, erro não sistemático)"],
    },
    # ------------------------------------------------------------------ E2-L01356
    {
        "id": "ECO-E2-L01356-1", "fonte_ref": "E2-L01356", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_PH_OA,
        "rotulo_item": "Item",
        "assertiva": ("A Curva de Oferta Agregada de Lucas estabelece que variações antecipadas na quantidade de moeda "
                      "afetam o produto no curto prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": (az("A Curva de Oferta Agregada de Lucas estabelece que variações ") + vm("antecipadas")
                    + az(" na quantidade de moeda afetam o produto no curto prazo.")),
        "poucas": ("Na oferta de " + oc("Lucas") + ", " + vd("Y = Ȳ + α(P − Pᵉ)") + ": o produto só se afasta do "
                   "natural quando o nível de preços <b>surpreende</b>. Moeda antecipada já está em Pᵉ e não mexe "
                   "no produto nem no curto prazo."),
        "destrinchando": [
            "Modelo das ilhas de " + oc("Lucas") + " (1972–1973): cada produtor vê o preço do próprio bem antes de "
            "conhecer o nível geral de preços. Diante de uma alta, ele não sabe se é preço <b>relativo</b> (vale "
            "produzir mais) ou inflação geral (não vale). Produz um pouco mais porque atribui parte da alta ao preço "
            "relativo — é o " + azb("problema de extração de sinal") + ".",
            "Daí a curva de oferta de surpresa: " + vd("Y − Ȳ = α(P − Pᵉ)") + ". Se a expansão monetária é "
            "anunciada ou segue regra conhecida, os agentes já a embutem em Pᵉ; P sobe, Pᵉ sobe junto e "
            + vd("Y = Ȳ") + ". Só a parcela " + azb("não antecipada") + " da moeda tem efeito real, e ainda assim "
            "transitório.",
            "Implicação: " + azb("ineficácia da política sistemática") + " (Sargent e Wallace) e "
            + azb("crítica de Lucas") + " (1976) — relações estimadas, como a curva de Phillips, mudam quando muda "
            "a regra de política, porque mudam as expectativas.",
            "Contraste com " + oc("Friedman") + ": com expectativas adaptativas, mesmo uma expansão conhecida tem "
            "efeito real de curto prazo, porque as expectativas só se ajustam depois. Para os " + oc("novos "
            "keynesianos") + ", contratos e rigidezes nominais também permitem efeito real de moeda antecipada.",
            vm("Regra-âncora: em Lucas, só moeda NÃO antecipada afeta o produto (e só no curto prazo)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca “não antecipadas” por “antecipadas” — "
                       "exatamente o adjetivo que define o modelo. O “no curto prazo” dá ar de prudência, mas não "
                       "salva: em Lucas, a moeda antecipada é neutra também no curto prazo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…variações não antecipadas na quantidade de moeda afetam o produto no curto prazo.”</i> → CERTO",
            "<i>“…variações não antecipadas na quantidade de moeda afetam o produto de forma permanente.”</i> → "
            "ERRADO (o efeito dura só até o erro ser percebido)",
        ])],
        "reescrita": ("A Curva de Oferta Agregada de Lucas estabelece que variações " + hl("não antecipadas")
                      + " na quantidade de moeda afetam o produto no curto prazo."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["no curto prazo"], "dificuldade": 2,
        "comentario_fonte": ("Verso só com imagem: página de texto sobre o modelo de Lucas e a antecipação monetária; "
                             "sem gabarito explícito."),
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 234", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (conteúdo no 📖)"}],
        "alertas": ["nota_redacao: verso da fonte sem gabarito explícito (só imagem de texto); item resolvido como "
                    "ERRADO pela teoria — na oferta de Lucas só a moeda não antecipada tem efeito real"],
    },
    # ------------------------------------------------------------------ E2-L01357
    {
        "id": "ECO-E2-L01357-1", "fonte_ref": "E2-L01357", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_PH_OA,
        "rotulo_item": "Item",
        "assertiva": ("Com relação à versão aceleracionista, se a curva de Phillips for inclinada (mas não vertical) e "
                      "as expectativas forem adaptativas, então a política monetária pode afetar o nível de emprego no "
                      "curto prazo, mas não no longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com relação à versão aceleracionista, se a curva de Phillips for inclinada (mas não vertical) "
                      "e as expectativas forem adaptativas, então a política monetária pode afetar o nível de emprego "
                      "<u>no curto prazo, mas não no longo prazo</u>."),
        "poucas": ("É a conclusão monetarista de " + oc("Friedman") + ": com curva de curto prazo inclinada e "
                   + azb("expectativas adaptativas") + ", a expansão monetária reduz o desemprego enquanto as "
                   "expectativas não se ajustam; ajustadas, o desemprego volta a " + vd("uₙ") + " e só fica a "
                   "inflação maior."),
        "destrinchando": [
            "Curva de curto prazo: " + vd("π = πᵉ − α(u − uₙ)") + ". Com πᵉ dado, uma expansão monetária leva a "
            "economia ao longo da curva: inflação acima da esperada, salário real menor do que os trabalhadores "
            "supunham, mais contratações — o desemprego cai abaixo de uₙ.",
            "Com " + azb("expectativas adaptativas") + ", πᵉ passa a incorporar a inflação mais alta observada; a "
            "curva de curto prazo sobe, e o desemprego volta a uₙ com inflação permanentemente maior. Manter u < uₙ "
            "exigiria acelerar a inflação continuamente.",
            "No longo prazo (πᵉ = π), a curva de Phillips é " + azb("vertical") + " em uₙ: moeda é neutra para "
            "o emprego. A condição “inclinada, mas não vertical” do item refere-se à curva de " + vd("curto prazo")
            + " — é ela que dá margem ao efeito temporário.",
            "Contraste: com " + azb("expectativas racionais") + " e política antecipada (" + oc("Lucas") + ", "
            + oc("Sargent") + "), nem o efeito de curto prazo existiria; com a curva original (sem expectativas), "
            "o efeito seria permanente.",
            vm("Regra-âncora: Friedman — moeda afeta emprego no curto prazo, não no longo."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz a síntese monetarista. O “pode” e o "
                       "par “curto prazo, mas não longo” encaixam exatamente na versão adaptativa; a armadilha "
                       "seria trocar o tipo de expectativa ou inverter os prazos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…e as expectativas forem racionais, a política monetária antecipada pode afetar o emprego no "
            "curto prazo.”</i> → ERRADO (troca de conceito: com expectativas racionais, política antecipada é "
            "neutra)",
            "<i>“…a política monetária pode afetar o nível de emprego no longo prazo, mas não no curto.”</i> → "
            "ERRADO (inversão de prazos)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Conclusão monetarista (Friedman): efeito de curto prazo; expectativas se ajustam à "
                             "inflação passada, a curva desloca-se e, no longo prazo, fica vertical."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01358
    {
        "id": "ECO-E2-L01358-1", "fonte_ref": "E2-L01358", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_PH_OA,
        "rotulo_item": "Item",
        "assertiva": ("Segundo Friedman, é possível reduzir a taxa de desemprego observada em relação à taxa natural "
                      "com políticas monetárias expansionistas. Daí vem a denominação dessa corrente, o monetarismo. "
                      "Friedman apoia suas ideias no tripé: taxa natural de desemprego, curva de Phillips e "
                      "expectativas adaptativas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Segundo Friedman, é <u>possível</u> reduzir a taxa de desemprego observada em relação à taxa "
                      "natural com políticas monetárias expansionistas. <u>Daí vem a denominação dessa corrente, o "
                      "monetarismo.</u> Friedman apoia suas ideias no tripé: taxa natural de desemprego, curva de "
                      "Phillips e expectativas adaptativas."),
        "poucas": ("Para " + oc("Friedman") + ", a expansão monetária <b>pode</b> levar o desemprego abaixo de "
                   + vd("uₙ") + " — mas só no curto prazo, enquanto as " + azb("expectativas adaptativas")
                   + " não alcançam a inflação. O tripé citado é o da sua crítica à curva de Phillips."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "a frase “daí vem a denominação dessa corrente” é frouxa. O rótulo " + azb("monetarismo")
                          + " (cunhado por " + oc("Karl Brunner") + ", 1968) vem da primazia que a corrente dá à "
                          "<b>oferta de moeda</b> na determinação da renda nominal e da inflação (teoria quantitativa "
                          "reformulada), e não da tese de que a moeda reduz o desemprego. A banca aceitou o item "
                          "pelo conjunto; numa prova mais rigorosa, esse nexo poderia render ERRADO.")],
        "destrinchando": [
            "Em “The Role of Monetary Policy” (" + vd("1968") + "), " + oc("Friedman") + " separa curto e longo "
            "prazo: a política monetária consegue, por algum tempo, manter o desemprego abaixo da " + azb("taxa "
            "natural") + ", porque a inflação surpreende trabalhadores que formam expectativas olhando o passado.",
            "Com o tempo, as expectativas se ajustam, os salários nominais são renegociados e o desemprego volta à "
            "taxa natural, com inflação mais alta. Insistir em u < uₙ exige inflação crescente — a tese "
            + azb("aceleracionista") + ", formulada também por " + oc("Edmund Phelps") + " (1967).",
            "O " + azb("tripé") + " do item resume o argumento: (1) " + vd("taxa natural") + " determinada por "
            "fatores reais (fricções, instituições do mercado de trabalho); (2) curva de Phillips aumentada pelas "
            "expectativas; (3) " + vd("expectativas adaptativas") + ", que explicam por que o efeito existe mas é "
            "temporário.",
            "Implicação de política: em vez de ajuste fino da demanda, Friedman defendia uma " + azb("regra "
            "monetária") + " — crescimento constante da oferta de moeda (regra dos k%).",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " As duas pontas verdadeiras (efeito possível; "
                       "tripé) sustentam o CERTO; o “é possível” não afirma permanência. O elo frágil é o “daí vem "
                       "a denominação”, um nexo histórico duvidoso que a banca deixou passar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Friedman, é possível manter permanentemente a taxa de desemprego abaixo da natural com "
            "políticas monetárias expansionistas.”</i> → ERRADO (só no curto prazo, à custa de inflação "
            "crescente)",
            "<i>“Friedman apoia suas ideias no tripé taxa natural de desemprego, curva de Phillips e expectativas "
            "racionais.”</i> → ERRADO (troca de conceito: as racionais são dos novos clássicos)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["é possível"], "dificuldade": 2,
        "comentario_fonte": ("No curto prazo a curva é negativamente inclinada e é possível reduzir o desemprego com "
                             "políticas monetárias expansionistas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: o nexo “daí vem a denominação monetarismo” é historicamente impreciso (o nome vem "
                    "da primazia da oferta de moeda); gabarito oficial CERTO mantido"],
    },
    # ------------------------------------------------------------------ E2-L01359
    {
        "id": "ECO-E2-L01359-1", "fonte_ref": "E2-L01359", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_PH_OA,
        "rotulo_item": "Item",
        "assertiva": ("A versão aceleracionista da curva de Phillips difere substancialmente da chamada curva de "
                      "oferta de Lucas, particularmente no que se refere ao trade-off entre inflação e desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A versão aceleracionista da curva de Phillips ") + vm("difere substancialmente da")
                    + az(" chamada curva de oferta de Lucas, particularmente no que se refere ao trade-off entre "
                         "inflação e desemprego.")),
        "poucas": ("As duas são a " + azb("mesma relação") + " escrita em variáveis diferentes: desvio do produto "
                   "(ou do desemprego) só quando a inflação <b>surpreende</b>; trade-off temporário no curto prazo e "
                   "nenhum no longo. O que muda é a formação das expectativas."),
        "destrinchando": [
            "Friedman–Phelps: " + vd("u − uₙ = −β(π − πᵉ)") + ". Lucas: " + vd("Y − Ȳ = α(P − Pᵉ)")
            + ". Pela lei de " + oc("Okun") + " (produto acima do potencial ↔ desemprego abaixo do natural), uma "
            "é a imagem espelhada da outra: só o erro de expectativa afasta a economia do natural.",
            "Pontos comuns: " + azb("taxa natural") + " determinada por fatores reais; trade-off apenas de curto "
            "prazo, gerado por surpresas; curva de Phillips de longo prazo " + azb("vertical") + "; neutralidade "
            "da moeda no longo prazo.",
            "Diferença real: " + azb("adaptativas") + " (Friedman) × " + azb("racionais") + " (Lucas). Com "
            "adaptativas, até a política sistemática gera surpresa por algum tempo; com racionais, só choques "
            "não antecipados geram — a política previsível perde o efeito mesmo no curto prazo. Lucas também "
            "deu " + azb("microfundamentos") + " (modelo das ilhas, confusão entre preço relativo e nível geral).",
            "Por isso os manuais tratam a oferta de Lucas como " + vd("radicalização") + " da aceleracionista, não "
            "como ruptura: o desacordo é sobre mecanismo e velocidade do ajuste, não sobre a natureza do "
            "trade-off.",
            vm("Regra-âncora: Friedman e Lucas concordam — trade-off só com surpresa, nunca no longo prazo."),
        ],
        "dissecando": (cz("[contradição · juízo indevido]") + " O item fabrica uma oposição entre dois modelos "
                       "aparentados e a ancora justamente no ponto em que eles convergem (o trade-off). O "
                       "“substancialmente” é a palavra a desconfiar: as diferenças existem, mas estão nas "
                       "expectativas. 🔥 A banca gosta de cobrar Friedman × Lucas como continuidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A versão aceleracionista e a curva de oferta de Lucas diferem quanto à formação das "
            "expectativas dos agentes.”</i> → CERTO",
            "<i>“Ao contrário da aceleracionista, a curva de oferta de Lucas admite trade-off de longo prazo.”</i> "
            "→ ERRADO (nenhuma das duas admite)",
        ])],
        "reescrita": ("A versão aceleracionista da curva de Phillips " + hl("converge, em essência, com a")
                      + " chamada curva de oferta de Lucas, particularmente no que se refere ao trade-off entre "
                      "inflação e desemprego."),
        "tipo_erro": ["CONTRADICAO", "JUIZO_INDEVIDO"], "moduladores": ["substancialmente"], "dificuldade": 2,
        "comentario_fonte": ("Em Lucas também há, no curto prazo, expansão do produto e redução do desemprego com mais "
                             "inflação; ambas rejeitam trade-off permanente; diferem na formação das expectativas. "
                             "Verso com várias respostas de IA empilhadas e seis imagens."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 235-238", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (curvas de Phillips e OA de Lucas; mecanismo absorvido no 📖)"},
                          {"ref": "IMAGEM 239-240", "tipo_fonte": "TABELA/TEXTO", "lado": "verso",
                           "acao": "absorvidas (comparação Friedman–Phelps × Lucas no 📖)"}],
        "alertas": ["nota_redacao: a IMAGEM 237 descrita na fonte (custos por alíquota) não tem relação com o item; "
                    "cortada"],
    },
    # ------------------------------------------------------------------ E2-L01450
    {
        "id": "ECO-E2-L01450-1", "fonte_ref": "E2-L01450", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": "Julgue os itens abaixo acerca do modelo de oferta e demanda agregadas e da Curva de Phillips.",
        "excerto": ("<p><i>Item 3: A existência de elevado desemprego e capacidade ociosa geradas pela pandemia aumenta "
                    "a elasticidade da curva de oferta agregada de curto prazo, reduzindo os impactos das políticas "
                    "econômicas expansionistas sobre a inflação.</i></p>"),
        "rotulo_item": "Item",
        "assertiva": "Na situação do item 3, a curva de Phillips de longo prazo será negativamente inclinada.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na situação do item 3, a curva de Phillips de longo prazo será ")
                    + vm("negativamente inclinada") + az(".")),
        "poucas": ("Ociosidade torna mais elásticas a OA e a curva de Phillips de <b>curto</b> prazo. A de "
                   + azb("longo prazo") + " continua " + vd("vertical em uₙ") + ": conjuntura não cria trade-off "
                   "permanente."),
        "destrinchando": [
            "O item 3 (verdadeiro) descreve o curto prazo: com desemprego alto e máquinas paradas, as empresas "
            "expandem a produção sem pressionar custos; a " + azb("OA de curto prazo") + " fica mais horizontal e "
            "um estímulo de demanda gera mais produto e pouca inflação.",
            "No plano inflação × desemprego, isso equivale a uma " + azb("curva de Phillips de curto prazo")
            + " mais <b>achatada</b>: reduzir o desemprego custa pouca inflação — a “taxa de sacrifício” da "
            "expansão é baixa.",
            "A " + azb("curva de longo prazo") + " é outra coisa: o lugar das combinações em que πᵉ = π. Aí o "
            "desemprego está na taxa natural, determinada por fatores estruturais (fricções, qualificação, "
            "instituições), e não por ociosidade conjuntural. Por isso ela é " + vd("vertical") + " em uₙ, com ou "
            "sem pandemia.",
            "A ociosidade, aliás, é a própria distância entre u e uₙ: quando a economia a absorve, volta-se à "
            "taxa natural e a OA retoma a inclinação usual.",
            vm("Regra-âncora: choques e folgas mudam a curva de CURTO prazo; a de longo prazo é vertical."),
        ],
        "dissecando": (cz("[troca de conceito · extrapolação]") + " O item se apoia num item anterior verdadeiro "
                       "(curto prazo) e estende a conclusão ao longo prazo, onde ela não vale. Pista: “de longo "
                       "prazo” + “negativamente inclinada” é combinação proibida em qualquer versão com "
                       "expectativas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na situação do item 3, a curva de Phillips de curto prazo será mais horizontal.”</i> → CERTO",
            "<i>“Na situação do item 3, a taxa natural de desemprego cai, deslocando a curva de Phillips de longo "
            "prazo para a esquerda.”</i> → ERRADO (nexo indevido: ociosidade conjuntural não altera uₙ)",
        ])],
        "reescrita": ("Na situação do item 3, a curva de Phillips de longo prazo será " + hl("vertical na taxa "
                      "natural de desemprego") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "EXTRAPOLACAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A curva de Phillips de longo prazo é vertical na taxa natural; inclinação negativa é da "
                             "curva de curto prazo; ociosidade torna a OACP mais elástica e a CP de curto prazo mais "
                             "plana, sem alterar a de longo prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: o texto do item 3, citado pela assertiva, veio na própria frente da fonte e foi "
                    "posto como excerto"],
    },
    # ------------------------------------------------------------------ E2-L01476
    {
        "id": "ECO-E2-L01476-1", "fonte_ref": "E2-L01476", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_INF,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a curva de Phillips na versão com expectativas adaptativas, a recente elevação dos juros "
                      "pelo Banco Central do Brasil levará a aumento do desemprego apenas no curto prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a curva de Phillips na versão com expectativas adaptativas, a recente elevação dos "
                      "juros pelo Banco Central do Brasil levará a aumento do desemprego <u>apenas no curto "
                      "prazo</u>."),
        "poucas": ("Política " + azb("contracionista") + " move a economia ao longo da curva de curto prazo: "
                   "inflação cai, desemprego sobe acima de uₙ. Com expectativas adaptativas, πᵉ recua aos poucos, a "
                   "curva desce e o desemprego volta ao natural — o custo é " + vd("temporário") + "."),
        "destrinchando": [
            "Transmissão: Selic ↑ → crédito mais caro → consumo e investimento ↓ → demanda agregada ↓ → menos "
            "produção e emprego. Com πᵉ ainda presa à inflação passada, a inflação efetiva cai abaixo da esperada, "
            "e o desemprego sobe acima da " + azb("taxa natural") + " (de A para B no gráfico).",
            "Ajuste: os agentes observam a inflação menor e revisam πᵉ para baixo; os reajustes salariais "
            "encolhem, a curva de Phillips de curto prazo desce e a economia volta a " + vd("uₙ")
            + " com inflação menor (ponto C).",
            "O desemprego extra durante a transição é o " + azb("custo da desinflação") + " — medido pela "
            + azb("taxa de sacrifício") + " (pontos de produto perdidos por ponto de inflação reduzido). Com "
            "expectativas adaptativas ele é inevitável; com " + azb("expectativas racionais") + " e banco central "
            "crível, poderia ser menor ou até nulo.",
            "Contexto: o " + rx("Banco Central do Brasil") + " elevou a Selic de " + vd("2% (mar/2021)") + " a "
            + vd("13,75% (ago/2022)") + " no ciclo pós-pandemia — é a “recente elevação” a que o item se refere.",
        ],
        "grafico_verso": "ECO-E2-L01476-1-V1",
        "dissecando": (cz("[modulador relativo · literalidade]") + " O “apenas no curto prazo” parece "
                       "restrição perigosa, mas é exatamente a tese da versão adaptativa: o trade-off existe e é "
                       "temporário. O contexto brasileiro é decoração; o julgamento é teórico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a curva de Phillips original, a elevação dos juros levará a aumento do desemprego apenas "
            "no curto prazo.”</i> → ERRADO (na original, sem expectativas, o trade-off é permanente)",
            "<i>“Segundo a versão com expectativas racionais, uma elevação de juros anunciada e crível pode reduzir "
            "a inflação sem aumento do desemprego.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Com expectativas adaptativas, política contracionista eleva o desemprego só no curto "
                             "prazo; as expectativas se ajustam e a economia volta à taxa natural com inflação menor. "
                             "Várias respostas de IA empilhadas e gráfico A → B → C."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 367", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01476-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01477
    {
        "id": "ECO-E2-L01477-1", "fonte_ref": "E2-L01477", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_INF,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a versão das expectativas racionais da Curva de Phillips, a recente aprovação da "
                      "autonomia do Banco Central, com mandatos fixos para presidente e diretoria, tende a fazer a "
                      "inflação convergir para a meta mais rapidamente e com menores custos em termos de desemprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a versão das expectativas racionais da Curva de Phillips, a recente aprovação da "
                      "autonomia do Banco Central, com mandatos fixos para presidente e diretoria, <u>tende a</u> "
                      "fazer a inflação convergir para a meta mais rapidamente e com menores custos em termos de "
                      "desemprego."),
        "poucas": ("Com " + azb("expectativas racionais") + ", o custo da desinflação depende da "
                   + azb("credibilidade") + ": se os agentes acreditam no BC, baixam πᵉ já, a curva de Phillips de "
                   "curto prazo desce logo e a " + vd("taxa de sacrifício") + " cai. Autonomia com mandatos fixos "
                   "reforça a credibilidade."),
        "destrinchando": [
            "Desinflar exige trazer πᵉ para baixo. Com expectativas adaptativas, isso só acontece depois de a "
            "inflação efetiva cair — o que pede um período de desemprego acima do natural. Com expectativas "
            "racionais, πᵉ responde ao <b>anúncio</b> da política, desde que ele seja crível.",
            azb("Inconsistência temporal") + " (" + oc("Kydland") + " e " + oc("Prescott") + ", 1977; "
            + oc("Barro") + " e " + oc("Gordon") + ", 1983): um BC sujeito ao ciclo político tem incentivo a "
            "prometer inflação baixa e depois surpreender com expansão; os agentes antecipam isso e mantêm πᵉ "
            "alta. A saída é delegar a política a uma autoridade independente e conservadora (" + oc("Rogoff")
            + ", 1985).",
            "No " + rx("Brasil") + ", a " + vd("Lei Complementar 179/2021") + " deu autonomia formal ao "
            + rx("BCB") + ": mandatos de " + vd("4 anos") + " para presidente e diretores, não coincidentes com o "
            "do Presidente da República, e demissão só em hipóteses previstas em lei. O objetivo fundamental é a "
            "estabilidade de preços; suavizar flutuações da atividade e fomentar o pleno emprego são objetivos "
            "acessórios.",
            "Por isso a assertiva usa “tende a”: autonomia aumenta a credibilidade, mas não garante desinflação "
            "indolor — rigidezes de contratos e choques de oferta continuam a cobrar seu preço.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Aplica ao caso brasileiro o argumento "
                       "padrão credibilidade → expectativas → custo menor. O “tende a” protege o item; a versão "
                       "absoluta (“eliminará o custo”) seria discutível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a versão com expectativas adaptativas, a autonomia do BC eliminaria o custo da "
            "desinflação em termos de desemprego.”</i> → ERRADO (com adaptativas, πᵉ só cai depois da inflação "
            "efetiva)",
            "<i>“A Lei Complementar 179/2021 fixou mandatos coincidentes com o do Presidente da República.”</i> → "
            "ERRADO (os mandatos são não coincidentes)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Credibilidade do BC (via autonomia) faz as expectativas se ajustarem mais rápido e reduz "
                             "o custo de desinflação; com expectativas racionais a curva de Phillips pode ser vertical "
                             "até no curto prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 368", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (slide sobre custo da desinflação e credibilidade, no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01673-1 cobra a mesma tese (autonomia do BC reduz o custo da "
                    "desinflação sob expectativas racionais)"],
    },
    # ------------------------------------------------------------------ E2-L01479
    {
        "id": "ECO-E2-L01479-1", "fonte_ref": "E2-L01479", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_INF,
        "rotulo_item": "Item",
        "assertiva": "Se a oferta agregada é inelástica a preços, a curva de Phillips será negativamente inclinada.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se a oferta agregada é inelástica a preços, a curva de Phillips será ")
                    + vm("negativamente inclinada") + az(".")),
        "poucas": ("OA inelástica (" + azb("vertical") + ") = produto fixo no potencial: choques de demanda só mexem "
                   "nos preços. Sem variação de produto, o desemprego não sai de uₙ — a curva de Phillips também é "
                   + vd("vertical") + "."),
        "destrinchando": [
            "A curva de Phillips é a OA “traduzida”: OA positivamente inclinada → um aumento da demanda eleva "
            "preços <b>e</b> produto → inflação maior com desemprego menor → Phillips negativamente inclinada. "
            "É o par do curto prazo, com salários e preços rígidos ou expectativas defasadas.",
            "Com OA " + azb("inelástica a preços") + ", a expansão da demanda (DA₁ → DA₂) só eleva P; o produto "
            "fica em Yₚ e, pela lei de " + oc("Okun") + ", o desemprego fica na taxa natural. No plano π × u, os "
            "pontos se empilham numa " + vd("vertical em uₙ") + ": nenhum trade-off.",
            "Esse é o caso " + azb("clássico") + " e o do " + azb("longo prazo") + " (OALP vertical ↔ CPLP "
            "vertical). Também é o curto prazo dos " + oc("novos clássicos") + " para política antecipada.",
            "No outro extremo, OA horizontal (keynesiana, com grande ociosidade) dá curva de Phillips horizontal: "
            "mais demanda reduz o desemprego sem inflação. A inclinação da Phillips acompanha a da OA.",
            vm("Regra-âncora: OA vertical ↔ Phillips vertical; OA inclinada ↔ Phillips negativamente inclinada."),
        ],
        "grafico_verso": "ECO-E2-L01479-1-V1",
        "dissecando": (cz("[troca de conceito · inversão]") + " O item cruza uma premissa de longo prazo (OA "
                       "inelástica) com uma conclusão de curto prazo (trade-off). A pista é “inelástica a "
                       "preços”: se o produto não reage ao preço, não há como o desemprego reagir à inflação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a oferta agregada é positivamente inclinada, a curva de Phillips de curto prazo é "
            "negativamente inclinada.”</i> → CERTO",
            "<i>“Se a oferta agregada é perfeitamente elástica, a curva de Phillips é vertical.”</i> → ERRADO "
            "(OA horizontal ↔ Phillips horizontal)",
        ])],
        "reescrita": ("Se a oferta agregada é inelástica a preços, a curva de Phillips será " + hl("vertical na taxa "
                      "natural de desemprego") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("OA inelástica (vertical): demanda afeta só preços; não há trade-off e a curva de Phillips "
                             "é vertical; inclinação negativa está associada a OA positivamente inclinada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 369", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01479-1-V1, adaptada ao caso de OA vertical)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01553
    {
        "id": "ECO-E2-L01553-1", "fonte_ref": "E2-L01553", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("Sobre a teoria da política econômica numa economia aberta (modelo Mundell-Fleming), o modelo de "
                    "oferta e demanda agregadas e a Curva de Phillips, julgue as afirmativas abaixo."),
        "rotulo_item": "Item",
        "assertiva": ("Se prevalece a versão da curva de Philips com expectativas racionais, um presidente que deseja "
                      "se reeleger e fizesse uso de uma política fiscal expansionista num regime de câmbio fixo e "
                      "perfeita mobilidade de capitais, teria sucesso em reduzir o desemprego no ano eleitoral, ou "
                      "seja, no curto prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se prevalece a versão da curva de Philips com expectativas racionais, um presidente que "
                       "deseja se reeleger e fizesse uso de uma política fiscal expansionista num regime de câmbio "
                       "fixo e perfeita mobilidade de capitais, ") + vm("teria sucesso em reduzir")
                    + az(" o desemprego no ano eleitoral, ou seja, no curto prazo.")),
        "poucas": ("No " + azb("Mundell-Fleming") + " com câmbio fixo a política fiscal é potente para a "
                   "<b>demanda</b>; mas, com " + azb("expectativas racionais") + ", uma expansão previsível (ano "
                   "eleitoral!) é antecipada e vira só preço: o desemprego não cai nem no curto prazo."),
        "destrinchando": [
            "Primeira camada, " + azb("Mundell-Fleming") + " com câmbio fixo e mobilidade perfeita: a expansão "
            "fiscal desloca a IS, pressiona os juros, atrai capital; para segurar o câmbio, o BC compra divisas e "
            "expande a moeda (LM acompanha). Resultado: " + vd("política fiscal muito eficaz") + " sobre a demanda "
            "agregada (e a monetária, inócua). Essa parte do item está certa.",
            "Segunda camada, " + azb("curva de Phillips com expectativas racionais") + ": produto e emprego só "
            "se afastam do natural quando a inflação surpreende (π ≠ πᵉ). Uma política sistemática e previsível "
            "entra nas expectativas, salários e preços se ajustam de imediato, e o aumento da demanda vira "
            "inflação, com u = uₙ.",
            "O caso do item é o mais previsível de todos: o " + azb("ciclo político-econômico") + " de "
            + oc("Nordhaus") + " (1975) — expandir antes da eleição — pressupõe eleitores e agentes que não "
            "antecipam. Com expectativas racionais, o estímulo eleitoral é antecipado e falha.",
            "Contraste: com " + azb("expectativas adaptativas") + " (" + oc("Friedman") + "), a manobra funcionaria "
            "temporariamente (desemprego menor no ano eleitoral, conta de inflação depois). Só uma " + vd("surpresa")
            + " genuína teria efeito real sob expectativas racionais.",
            vm("Regra-âncora: expectativas racionais + política antecipada = efeito real nulo, até no curto prazo."),
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " Duas camadas: a do Mundell-Fleming é verdadeira "
                       "(fiscal eficaz em câmbio fixo) e serve de isca; a das expectativas racionais decide o item. "
                       "O “ou seja, no curto prazo” tenta vender o efeito como temporário e, por isso, aceitável — "
                       "mas sob expectativas racionais nem o temporário existe para política antecipada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se prevalece a versão com expectativas adaptativas, o presidente teria sucesso em reduzir o "
            "desemprego no ano eleitoral.”</i> → CERTO",
            "<i>“No modelo Mundell-Fleming com câmbio fixo e perfeita mobilidade de capitais, a política fiscal "
            "expansionista é ineficaz para elevar a renda.”</i> → ERRADO (é a monetária que é ineficaz nesse "
            "regime)",
        ])],
        "reescrita": ("Se prevalece a versão da curva de Philips com expectativas racionais, um presidente que deseja "
                      "se reeleger e fizesse uso de uma política fiscal expansionista num regime de câmbio fixo e "
                      "perfeita mobilidade de capitais, " + hl("não conseguiria reduzir") + " o desemprego no ano "
                      "eleitoral, ou seja, no curto prazo" + hl(", porque a expansão seria antecipada pelos "
                      "agentes") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Com expectativas racionais a política sistemática (como a de ano eleitoral) é antecipada "
                             "e neutralizada mesmo no curto prazo; fiscal é eficaz no Mundell-Fleming com câmbio fixo, "
                             "mas isso não salva o item. Respostas de IA empilhadas, uma delas errando ao dizer que a "
                             "fiscal tem eficácia limitada em câmbio fixo."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01597
    {
        "id": "ECO-E2-L01597-1", "fonte_ref": "E2-L01597", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_PAND,
        "rotulo_item": "Item",
        "assertiva": ("Se a taxa de desemprego efetiva está abaixo da taxa natural de desemprego, haverá elevação da "
                      "inflação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a taxa de desemprego efetiva está <u>abaixo</u> da taxa natural de desemprego, haverá "
                      "<u>elevação</u> da inflação."),
        "poucas": ("A " + azb("taxa natural") + " é a " + azb("NAIRU") + " — o desemprego compatível com inflação "
                   "estável. Abaixo dela, o mercado de trabalho está aquecido e a inflação " + vd("acelera")
                   + ": Δπ = −α(u − uₙ) > 0."),
        "destrinchando": [
            "Taxa natural = desemprego " + azb("friccional") + " + " + azb("estrutural") + ", sem o "
            + azb("cíclico") + ". Quando o desemprego efetivo cai abaixo dela, há desemprego cíclico negativo: a "
            "economia opera acima do potencial.",
            "Mecanismo: escassez de mão de obra → reajustes salariais acima da inflação esperada → custos maiores "
            "repassados aos preços → inflação sobe e alimenta as expectativas do período seguinte.",
            "Por isso o nome " + azb("NAIRU") + " (<i>non-accelerating inflation rate of unemployment</i>): só em "
            + vd("u = uₙ") + " a inflação fica parada; u < uₙ → inflação crescente; u > uₙ → inflação cadente.",
            "Uso prático: bancos centrais olham o " + azb("hiato do produto") + " e o hiato do desemprego. "
            "Desemprego abaixo da NAIRU é sinal para elevar juros e esfriar a economia. A estimativa da NAIRU é "
            "incerta e muda com a estrutura do mercado de trabalho.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Item direto da definição de NAIRU. O contexto da "
                       "pandemia (desemprego alto) induz a pensar em folga e marcar ERRADO, mas a assertiva trata "
                       "do caso oposto — desemprego <b>abaixo</b> do natural."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a taxa de desemprego efetiva está acima da taxa natural, haverá elevação da inflação.”</i> → "
            "ERRADO (inversão: a inflação desacelera)",
            "<i>“Se a taxa de desemprego efetiva é igual à natural, a inflação será nula.”</i> → ERRADO (será "
            "estável, não necessariamente zero)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Desemprego abaixo da NAIRU = mercado de trabalho aquecido, pressão salarial e repasse "
                             "aos preços; inflação acelera. Várias respostas de IA empilhadas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01598
    {
        "id": "ECO-E2-L01598-1", "fonte_ref": "E2-L01598", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_PAND,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a versão aceleracionista, a Curva de Philips de longo prazo é negativamente inclinada, "
                      "ou seja, há um trade off entre inflação e desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a versão aceleracionista, a Curva de Philips de longo prazo é ")
                    + vm("negativamente inclinada") + az(", ou seja, ") + vm("há") + az(" um trade off entre "
                                                                                        "inflação e desemprego.")),
        "poucas": ("Na aceleracionista (" + oc("Friedman") + "–" + oc("Phelps") + "), a curva de longo prazo é "
                   + vd("vertical") + " na taxa natural: não há trade-off permanente. A inclinação negativa é só da "
                   "curva de " + azb("curto prazo") + ", dada a inflação esperada."),
        "destrinchando": [
            "Curto prazo: π = πᵉ − α(u − uₙ). Com πᵉ fixa, mais inflação compra menos desemprego — uma curva "
            "negativamente inclinada para cada nível de inflação esperada.",
            "Longo prazo: as expectativas se ajustam (" + vd("πᵉ = π") + "), o termo α(u − uₙ) tem de zerar e "
            + vd("u = uₙ") + " qualquer que seja a inflação. O lugar desses pontos é uma vertical em uₙ — a "
            + azb("CPLP") + ".",
            "O nome “aceleracionista”: para manter u < uₙ, o governo teria de surpreender sempre, o que exige "
            "inflação <b>crescente</b>. Trade-off estável só existiria entre desemprego e a <b>variação</b> da "
            "inflação.",
            "Quem defendia curva negativamente inclinada também no longo prazo era a leitura " + azb("original")
            + " (Phillips 1958; Samuelson–Solow 1960), sem expectativas — refutada pela " + azb("estagflação")
            + " dos anos 1970.",
            vm("Regra-âncora: aceleracionista = curto prazo inclinado, longo prazo vertical."),
        ],
        "dissecando": (cz("[troca de conceito · anacronismo]") + " Atribui à aceleracionista a tese da curva "
                       "original. O “de longo prazo” é a palavra que decide: em qualquer versão com expectativas, "
                       "longo prazo = vertical."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a versão aceleracionista, a curva de Phillips de curto prazo é negativamente "
            "inclinada.”</i> → CERTO",
            "<i>“Segundo a versão aceleracionista, a curva de Phillips de longo prazo é vertical na taxa natural, "
            "e manter o desemprego abaixo dela exige inflação crescente.”</i> → CERTO",
        ])],
        "reescrita": ("Segundo a versão aceleracionista, a Curva de Philips de longo prazo é " + hl("vertical")
                      + ", ou seja, " + hl("não há") + " um trade off entre inflação e desemprego."),
        "tipo_erro": ["TROCA_CONCEITO", "ANACRONISMO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Na aceleracionista a curva de longo prazo é vertical na taxa natural; inclinação negativa "
                             "só no curto prazo. Gráfico de Mankiw: A → B → C com a CPCP subindo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 453", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo A → B → C absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01671
    {
        "id": "ECO-E2-L01671-1", "fonte_ref": "E2-L01671", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_REL,
        "rotulo_item": "Item",
        "assertiva": ("Na versão aceleracionista da curva de Phillips, expansões da oferta de moeda que façam o "
                      "desemprego ficar abaixo da taxa natural no curto prazo, levarão a um aumento nas expectativas de "
                      "inflação e ao deslocamento da curva de Phillips de longo prazo para cima e para direita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na versão aceleracionista da curva de Phillips, expansões da oferta de moeda que façam o "
                       "desemprego ficar abaixo da taxa natural no curto prazo, levarão a um aumento nas expectativas "
                       "de inflação e ao deslocamento da curva de Phillips de ") + vm("longo prazo") + az(" para cima")
                    + vm(" e para direita") + az(".")),
        "poucas": ("O aumento de πᵉ desloca para cima a curva de " + azb("curto prazo") + ". A de "
                   + azb("longo prazo") + " é vertical em uₙ e só se moveria se a própria taxa natural mudasse — o "
                   "que expansão monetária não faz."),
        "destrinchando": [
            "Sequência de " + oc("Friedman") + " (A → B → C): a expansão monetária leva a economia ao longo da "
            "CPCP₁ até B (desemprego abaixo de uₙ, inflação maior que a esperada). Os agentes revisam πᵉ para "
            "cima; cada ponto da curva de curto prazo sobe na mesma medida: " + vd("CPCP₁ → CPCP₂") + ".",
            "Com πᵉ = π, a economia volta a " + vd("uₙ") + " em C, com inflação mais alta. A " + azb("CPLP")
            + " liga A e C: é vertical e não se mexeu.",
            "O que desloca a CPLP é mudança na " + azb("taxa natural") + ": seguro-desemprego mais generoso, "
            "descasamento de qualificações ou mais fricções a deslocam para a direita; reformas que facilitam a "
            "busca de emprego, para a esquerda. Nunca “para cima”: sendo vertical, subir não muda nada.",
            "Resumo: " + vd("πᵉ ↑ → CPCP sobe") + "; " + vd("uₙ ↑ → CPLP vai para a direita") + ". Política "
            "monetária mexe só no primeiro.",
            vm("Regra-âncora: expectativas deslocam a curva de CURTO prazo; a de longo só muda com uₙ."),
        ],
        "grafico_verso": "ECO-E2-L01671-1-V1",
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " Todo o mecanismo está certo até “aumento nas "
                       "expectativas”; o erro está no objeto do deslocamento (longo × curto prazo) e na direção "
                       "enxertada (“e para direita”). Pista: curva vertical que se desloca “para cima” não muda de "
                       "lugar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…levarão a um aumento nas expectativas de inflação e ao deslocamento da curva de Phillips de curto "
            "prazo para cima.”</i> → CERTO",
            "<i>“Um aumento do seguro-desemprego que eleve a taxa natural desloca a curva de Phillips de longo prazo "
            "para a direita.”</i> → CERTO",
        ])],
        "reescrita": ("Na versão aceleracionista da curva de Phillips, expansões da oferta de moeda que façam o "
                      "desemprego ficar abaixo da taxa natural no curto prazo, levarão a um aumento nas expectativas de "
                      "inflação e ao deslocamento da curva de Phillips de " + hl("curto prazo") + " para cima"
                      "<s> e para direita</s>."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O aumento das expectativas desloca para cima a curva de curto prazo; a de longo prazo é "
                             "vertical na taxa natural e não se desloca. Uma das respostas empilhadas dizia, "
                             "erradamente, que a de longo prazo sobe; comentário da linha duplicada E2-L01738 fundido."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 487", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01671-1-V1)"},
                          {"ref": "IMAGEM 523 (linha duplicada)", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo gráfico)"}],
        "alertas": ["duplicata: linha E2-L01738 (mesma assertiva) fundida neste card"],
    },
    # ------------------------------------------------------------------ E2-L01672
    {
        "id": "ECO-E2-L01672-1", "fonte_ref": "E2-L01672", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_REL,
        "rotulo_item": "Item",
        "assertiva": ("Na curva de Phillips versão sem expectativas, o trade off entre inflação e desemprego é "
                      "temporário e válido apenas no curto prazo, sendo a curva de Phillips de curto prazo vertical na "
                      "taxa natural de desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na curva de Phillips versão sem expectativas, o trade off entre inflação e desemprego é ")
                    + vm("temporário e válido apenas no curto prazo") + az(", sendo a curva de Phillips ")
                    + vm("de curto prazo vertical na taxa natural de desemprego") + az(".")),
        "poucas": ("Duplo erro: na versão " + azb("sem expectativas") + " (a original), o trade-off é "
                   + vd("permanente") + " e a curva é negativamente inclinada; a distinção curto × longo prazo e a "
                   "verticalidade em uₙ só aparecem com " + oc("Friedman") + " e " + oc("Phelps") + "."),
        "destrinchando": [
            "Versão original (" + oc("Phillips") + " 1958; " + oc("Samuelson") + " e " + oc("Solow") + " 1960): "
            "π = f(u), com f decrescente. Nada de expectativas, nada de taxa natural: uma única curva estável, um "
            "“cardápio” em que o governo escolheria a combinação desejada para sempre.",
            "Versão com " + azb("expectativas adaptativas") + " (" + oc("Friedman") + " 1968, " + oc("Phelps")
            + " 1967): a curva de curto prazo continua negativamente inclinada, mas desloca-se com πᵉ; no longo "
            "prazo, vertical em uₙ. O trade-off vira temporário.",
            "Versão com " + azb("expectativas racionais") + " (" + oc("Lucas") + ", " + oc("Sargent") + "): para "
            "política antecipada, a curva é vertical já no curto prazo; só surpresas geram trade-off.",
            "O item cola na versão sem expectativas duas propriedades que pertencem às outras: o trade-off "
            "temporário (adaptativas) e a vertical em uₙ (longo prazo, ou curto prazo dos novos clássicos). Uma "
            "curva de curto prazo vertical, aliás, anularia o próprio trade-off que a frase acabou de afirmar.",
            vm("Regra-âncora: sem expectativas → trade-off permanente; adaptativas → temporário; racionais → só "
               "com surpresa."),
        ],
        "dissecando": (cz("[troca de conceito · contradição]") + " Atribui à versão original as conclusões das "
                       "versões posteriores, e ainda se contradiz (trade-off de curto prazo com curva de curto prazo "
                       "vertical). Pista: “sem expectativas” e “taxa natural” não convivem — a taxa natural nasce "
                       "junto com as expectativas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na curva de Phillips versão sem expectativas, o trade-off entre inflação e desemprego é "
            "permanente.”</i> → CERTO",
            "<i>“Na versão com expectativas adaptativas, a curva de Phillips de curto prazo é vertical na taxa "
            "natural.”</i> → ERRADO (vertical é a de longo prazo)",
        ])],
        "reescrita": ("Na curva de Phillips versão sem expectativas, o trade off entre inflação e desemprego é "
                      + hl("permanente") + ", sendo a curva de Phillips " + hl("negativamente inclinada, sem "
                      "distinção entre curto e longo prazo") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Na versão sem expectativas o trade-off é estável e permanente; a ideia de trade-off "
                             "temporário e a CP de longo prazo vertical vêm com as expectativas; a CP de curto prazo é "
                             "inclinada. Comentário da linha duplicada E2-L01739 fundido."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 523 (linha duplicada)", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico genérico de deslocamento da CPCP)"}],
        "alertas": ["duplicata: linha E2-L01739 (mesma assertiva) fundida neste card"],
    },
    # ------------------------------------------------------------------ E2-L01673
    {
        "id": "ECO-E2-L01673-1", "fonte_ref": "E2-L01673", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_REL,
        "rotulo_item": "Item",
        "assertiva": ("Com expectativas racionais, o custo da desinflação será menor caso haja maior autonomia da "
                      "autoridade monetária diante das interferências políticas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com expectativas racionais, o custo da desinflação será <u>menor</u> caso haja maior "
                      "autonomia da autoridade monetária diante das interferências políticas."),
        "poucas": ("Autonomia → " + azb("credibilidade") + " → expectativas racionais caem logo após o anúncio → a "
                   "curva de Phillips de curto prazo desce depressa → menos desemprego para baixar a inflação (menor "
                   + vd("taxa de sacrifício") + ")."),
        "destrinchando": [
            azb("Custo da desinflação") + " = produto perdido (ou desemprego extra) para reduzir a inflação. Mede-se "
            "pela " + azb("taxa de sacrifício") + ": pontos percentuais de PIB anual perdidos por ponto de inflação "
            "reduzido.",
            "Com expectativas racionais, o que importa é se os agentes <b>acreditam</b> no anúncio. Um BC sujeito a "
            "pressões políticas tem incentivo a abandonar a desinflação quando o desemprego sobe — o problema da "
            + azb("inconsistência temporal") + " (" + oc("Kydland") + " e " + oc("Prescott") + ", 1977). Sabendo "
            "disso, os agentes não baixam πᵉ, e a desinflação sai cara.",
            "Autonomia (mandatos fixos, blindagem contra demissão política, objetivo claro de estabilidade de "
            "preços) torna o compromisso crível; πᵉ cai junto com a política, e a economia pode ir de inflação alta "
            "para baixa com pouco desemprego. No limite teórico (crença total, sem rigidezes), a " + vd("desinflação "
            "seria indolor") + " (" + oc("Sargent") + ", “The Ends of Four Big Inflations”, 1982).",
            "Ressalva empírica: desinflações reais quase sempre custam algo (Volcker, 1979–1982, gerou recessão "
            "forte), porque há contratos e rigidezes; a credibilidade reduz, não zera, o custo.",
        ],
        "dissecando": (cz("[literalidade]") + " Encadeamento clássico autonomia → credibilidade → custo menor. O "
                       "item é comparativo (“será menor”), não absoluto; a armadilha seria a versão “será nulo”, "
                       "discutível na prática."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com expectativas adaptativas, a autonomia do banco central torna a desinflação indolor.”</i> → "
            "ERRADO (πᵉ só cai depois da inflação efetiva)",
            "<i>“Com expectativas racionais, uma desinflação anunciada por autoridade sem credibilidade pode ter "
            "custo elevado em desemprego.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["maior", "menor"], "dificuldade": 1,
        "comentario_fonte": ("Credibilidade é crucial sob expectativas racionais; autonomia reduz interferência e o "
                             "problema da inconsistência temporal, as expectativas se ajustam mais rápido e a taxa de "
                             "sacrifício cai. Comentário da linha duplicada E2-L01740 fundido."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: linha E2-L01740 (mesma assertiva) fundida neste card",
                    "quase_duplicata: ECO-E2-L01477-1 cobra a mesma tese aplicada à autonomia legal do BCB"],
    },
    # ------------------------------------------------------------------ E2-L01674
    {
        "id": "ECO-E2-L01674-1", "fonte_ref": "E2-L01674", "destino": "29", "subtema": H2["phil"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_REL,
        "rotulo_item": "Item",
        "assertiva": ("Segundo Friedman, é possível o desemprego ficar abaixo da taxa natural no curto prazo. No longo "
                      "prazo, porém, a curva de Phillips é vertical na taxa natural de desemprego, tal como na versão "
                      "com expectativas racionais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo Friedman, é possível o desemprego ficar abaixo da taxa natural <u>no curto prazo</u>. "
                      "No longo prazo, porém, a curva de Phillips é vertical na taxa natural de desemprego, <u>tal "
                      "como na versão com expectativas racionais</u>."),
        "poucas": ("Friedman: trade-off só no curto prazo, CPLP " + vd("vertical em uₙ") + ". Os novos clássicos "
                   "chegam à <b>mesma</b> vertical de longo prazo — a diferença está no curto prazo e na velocidade "
                   "do ajuste."),
        "destrinchando": [
            oc("Friedman") + " (1968): com " + azb("expectativas adaptativas") + ", a inflação acima da esperada "
            "reduz o salário real, as empresas contratam mais e o desemprego cai abaixo da taxa natural. É "
            "temporário: quando πᵉ alcança π, o desemprego volta a uₙ.",
            "Longo prazo: πᵉ = π ⇒ u = uₙ para qualquer inflação ⇒ curva vertical. É a " + azb("neutralidade "
            "da moeda") + " no longo prazo aplicada ao mercado de trabalho.",
            "Expectativas racionais (" + oc("Lucas") + ", " + oc("Sargent") + ", " + oc("Wallace") + "): a mesma "
            "CPLP vertical; a diferença é que a política <b>antecipada</b> já é neutra no curto prazo — só "
            "surpresas tiram a economia de uₙ, e por pouco tempo.",
            "Quadro-resumo: original → inclinada sempre; adaptativas → inclinada no curto, " + vd("vertical no "
            "longo") + "; racionais → vertical no curto (para política antecipada) e " + vd("no longo") + ".",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Duas afirmações certas encadeadas. O “tal como na versão "
                       "com expectativas racionais” é o ponto que derruba quem acha que as escolas divergem em "
                       "tudo: no longo prazo elas concordam."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Friedman, a curva de Phillips é vertical na taxa natural também no curto prazo, tal como na "
            "versão com expectativas racionais.”</i> → ERRADO (em Friedman há trade-off de curto prazo)",
            "<i>“Na versão com expectativas racionais, a curva de Phillips de longo prazo é negativamente "
            "inclinada.”</i> → ERRADO (também é vertical)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["é possível", "porém"], "dificuldade": 1,
        "comentario_fonte": ("Friedman: desemprego abaixo da natural no curto prazo por inflação não antecipada; no longo "
                             "prazo a curva é vertical, conclusão compartilhada pelas expectativas racionais. "
                             "Comentário da linha duplicada E2-L01741 fundido."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: linha E2-L01741 (mesma assertiva) fundida neste card",
                    "quase_duplicata: ECO-E2-L01358-1 cobra a mesma tese de Friedman (efeito só de curto prazo)"],
    },
    # ------------------------------------------------------------------ E3-L00379
    {
        "id": "ECO-E3-L00379-1", "fonte_ref": "E3-L00379", "destino": "29", "subtema": H2["exp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": ("Considerando os determinantes do crescimento econômico e a experiência recente do Brasil, julgue "
                    "certo ou errado (C ou E) os itens a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A hipótese de neutralidade da moeda no curto prazo é compatível com uma curva de Phillips "
                      "vertical, em que tanto expansões fiscais quanto monetárias são capazes de afetar o nível de "
                      "produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A hipótese de neutralidade da moeda no curto prazo é compatível com uma curva de Phillips "
                       "vertical, em que tanto expansões fiscais quanto monetárias ") + vm("são capazes")
                    + az(" de afetar o nível de produto.")),
        "poucas": ("Curva de Phillips " + azb("vertical") + " = produto e desemprego presos ao nível natural: "
                   "expansões de demanda, fiscais ou monetárias, só geram " + vd("inflação") + ". A primeira "
                   "metade do item (neutralidade ↔ vertical) é coerente; o erro é dizer que as políticas afetam o "
                   "produto."),
        "destrinchando": [
            azb("Neutralidade da moeda") + ": variações da quantidade de moeda alteram só variáveis nominais "
            "(preços, salários nominais), não as reais (produto, emprego, juro real). Se vale num horizonte, nele a "
            "curva de Phillips é vertical: mais demanda nominal não compra menos desemprego.",
            "Em que horizonte vale? Para " + oc("Friedman") + " e a síntese, só no " + vd("longo prazo")
            + "; no curto, rigidezes e erros de expectativa tornam a moeda não neutra e a curva, inclinada. Para os "
            + oc("novos clássicos") + " (política antecipada) e para os " + azb("ciclos reais") + ", a "
            "neutralidade vale já no " + vd("curto prazo") + ". Por isso a primeira oração é defensável como "
            "hipótese: “neutralidade no curto prazo” e “Phillips vertical” andam juntas.",
            "Com a curva vertical, a política fiscal também não move o produto agregado: a expansão de demanda "
            "eleva preços e, por " + azb("crowding out") + ", troca gasto privado por público. Pode mudar a "
            "<b>composição</b> do produto, não o seu nível.",
            "Os desenhos da fonte resumem: curva inclinada → Δπ = −α(u − uₙ), trade-off; curva vertical → "
            "“políticas fiscais e monetárias expansionistas não têm impacto sobre o produto, apenas elevam o nível "
            "de preços”.",
            vm("Regra-âncora: curva de Phillips vertical ⇒ política de demanda só mexe em preços."),
        ],
        "dissecando": (cz("[contradição]") + " O item começa coerente (neutralidade ↔ vertical) e se contradiz no "
                       "fim: numa curva vertical, por definição, a demanda não afeta o produto. Cuidado com a "
                       "tentação de marcar o erro em “curto prazo”: é hipótese aceitável dos novos clássicos — a "
                       "contradição está no “são capazes”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A hipótese de neutralidade da moeda no longo prazo é compatível com uma curva de Phillips vertical, "
            "em que expansões monetárias afetam apenas o nível de preços.”</i> → CERTO",
            "<i>“Uma curva de Phillips negativamente inclinada é compatível com a não neutralidade da moeda no "
            "curto prazo.”</i> → CERTO",
        ])],
        "reescrita": ("A hipótese de neutralidade da moeda no curto prazo é compatível com uma curva de Phillips "
                      "vertical, em que tanto expansões fiscais quanto monetárias " + hl("não são capazes")
                      + " de afetar o nível de produto."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": ["tanto … quanto"], "dificuldade": 2,
        "comentario_fonte": ("Gabarito ERRADO com destaque da fonte em “são capazes”. Respostas de IA empilhadas "
                             "(Claude, Gemini, GPT, DeepSeek) acrescentam que “neutralidade no curto prazo” seria "
                             "contradição em termos — leitura excessiva: é hipótese dos novos clássicos e dos ciclos "
                             "reais."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 539-540", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (curva inclinada × vertical; legendas transcritas no 📖)"},
                          {"ref": "IMAGEM 541", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quadro curto × longo prazo no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00453 (+ E2-L01348)
    {
        "id": "ECO-E2-L00453-1", "fonte_ref": "E2-L00453", "destino": "30", "subtema": H2["deb"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": True,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("Para os teóricos da síntese neoclássica, o produto e o emprego variam em função de choques "
                      "tecnológicos, alterações nos preços relativos, mudanças tributárias e mudanças nas preferências "
                      "dos indivíduos entre renda e lazer."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para os teóricos ") + vm("da síntese neoclássica") + az(", o produto e o emprego variam em "
                    "função de choques tecnológicos, alterações nos preços relativos, mudanças tributárias e mudanças "
                    "nas preferências dos indivíduos entre renda e lazer.")),
        "poucas": ("A lista de causas é a da teoria dos " + azb("ciclos reais de negócios") + " (" + oc("Kydland")
                   + " e " + oc("Prescott") + "). Para a " + azb("síntese neoclássica") + ", no curto prazo o "
                   "produto flutua com a " + vd("demanda agregada") + ", porque preços e salários se ajustam "
                   "devagar."),
        "destrinchando": [
            azb("Síntese neoclássica") + " (anos 1950–1960; " + oc("Hicks") + ", " + oc("Samuelson") + ", "
            + oc("Modigliani") + ", " + oc("Tobin") + "): Keynes no curto prazo, clássicos no longo. Núcleo: "
            + vd("IS-LM + curva de Phillips") + ". Preços e salários rígidos fazem a demanda agregada determinar "
            "produto e emprego no curto prazo; política fiscal e monetária servem para estabilizar. Samuelson, na "
            "edição de " + vd("1955") + " de <i>Economics</i>, dizia que 90% dos economistas americanos já "
            "trabalhavam nessa síntese.",
            azb("Ciclos reais de negócios") + " (RBC, " + oc("Kydland") + " e " + oc("Prescott") + ", 1982): "
            "preços flexíveis, agentes otimizadores, mercados sempre em equilíbrio. As flutuações são respostas "
            "eficientes a " + vd("choques reais") + " — de produtividade (tecnologia), de preços relativos (petróleo), "
            "de impostos — e a substituição " + azb("intertemporal") + " entre trabalho e lazer explica as "
            "variações do emprego. Moeda é neutra; política de estabilização é inútil ou nociva.",
            "Mapa das escolas: síntese (demanda + rigidez exógena) → monetaristas (moeda, expectativas "
            "adaptativas) → novos clássicos (expectativas racionais, surpresas monetárias) → RBC (choques reais) → "
            + azb("novos keynesianos") + " (rigidezes com microfundamentos: custos de menu, contratos escalonados, "
            "salário-eficiência) → " + azb("novo consenso") + " (DSGE com rigidezes e regra de juros).",
            "Fronteira útil: tecnologia é relevante para a síntese, mas como determinante do produto "
            "<b>potencial</b> (longo prazo, Solow); para o RBC, ela explica também o <b>ciclo</b>.",
            vm("Regra-âncora: choque tecnológico + escolha renda × lazer como motor do ciclo = RBC, não síntese."),
        ],
        "dissecando": (cz("[troca de ator]") + " A descrição é fiel — de outra escola. O item atribui à síntese "
                       "neoclássica o programa dos ciclos reais. Pista: “preferências entre renda e lazer” como causa "
                       "do emprego pressupõe desemprego voluntário, ideia estranha à tradição keynesiana. 🔥 A Nabuco "
                       "repete este item em mais de um simulado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para os teóricos dos ciclos reais de negócios, a moeda é neutra e as flutuações refletem respostas "
            "ótimas a choques de produtividade.”</i> → CERTO",
            "<i>“Para os teóricos da síntese neoclássica, as flutuações de curto prazo decorrem sobretudo de choques "
            "de demanda agregada, dada a rigidez de preços e salários.”</i> → CERTO",
        ])],
        "reescrita": ("Para os teóricos " + hl("dos ciclos reais de negócios") + ", o produto e o emprego variam em "
                      "função de choques tecnológicos, alterações nos preços relativos, mudanças tributárias e "
                      "mudanças nas preferências dos indivíduos entre renda e lazer."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A descrição é a dos ciclos reais (RBC); para a síntese neoclássica (IS-LM + Phillips), o "
                             "produto varia no curto prazo com a demanda agregada, por rigidez de preços e salários. "
                             "Respostas de IA empilhadas e tabela síntese × novos keynesianos; fundido com o "
                             "comentário da linha E2-L01348 (citação de Samuelson, 1955)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 077", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (comparação síntese × novos keynesianos no 📖)"}],
        "alertas": ["duplicata: linha E2-L01348 (Nabuco Pré-TPS/2022, mesma assertiva e mesmo comando) fundida "
                    "neste card"],
    },
    # ------------------------------------------------------------------ E2-L00584
    {
        "id": "ECO-E2-L00584-1", "fonte_ref": "E2-L00584", "destino": "30", "subtema": H2["deb"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação aos modelos macroeconômicos, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("A Nova Economia Clássica argumenta que a política monetária sistemática pode gerenciar "
                      "efetivamente a produção e o emprego reais apenas no curto prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Nova Economia Clássica argumenta que a política monetária sistemática ") + vm("pode")
                    + az(" gerenciar efetivamente a produção e o emprego reais ") + vm("apenas")
                    + az(" no curto prazo.")),
        "poucas": ("Para os " + oc("novos clássicos") + ", política " + azb("sistemática") + " é previsível, entra "
                   "nas expectativas racionais e é neutra " + vd("já no curto prazo") + ". Efeito real, e "
                   "passageiro, só a surpresa."),
        "destrinchando": [
            azb("Proposição da ineficácia da política") + " (" + oc("Sargent") + " e " + oc("Wallace") + ", "
            "1975–1976): com expectativas racionais e preços flexíveis, uma regra monetária conhecida (por "
            "exemplo, expandir a moeda quando o desemprego sobe) é antecipada; P e Pᵉ sobem juntos e Y = Ȳ.",
            "Só a parte " + azb("não antecipada") + " da política gera surpresa de preços e, pela oferta de "
            + oc("Lucas") + ", desvio transitório do produto. Mas uma política feita de surpresas aleatórias não "
            "serve para gerenciar nada: aumenta a variância do produto sem melhorar sua média.",
            "Quem diz “eficaz só no curto prazo” é " + oc("Friedman") + " (expectativas adaptativas): a política "
            "sistemática funciona por algum tempo, até as expectativas se ajustarem. O item atribui aos novos "
            "clássicos a conclusão monetarista.",
            "Reação: os " + azb("novos keynesianos") + " (" + oc("Fischer") + " 1977, " + oc("Taylor")
            + " 1980) mostraram que, com contratos salariais plurianuais, até a política antecipada tem efeito "
            "real — rigidez, não irracionalidade, devolve espaço à estabilização.",
            vm("Regra-âncora: novos clássicos — sistemática = neutra até no curto prazo; Friedman — eficaz só no "
               "curto prazo."),
        ],
        "dissecando": (cz("[troca de ator · restrição indevida]") + " O “apenas no curto prazo” soa prudente e "
                       "engana: é a tese de Friedman, não dos novos clássicos. A palavra “sistemática” é a pista — "
                       "para os novos clássicos, sistemático é sinônimo de antecipado e, logo, de neutro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para a Nova Economia Clássica, apenas choques monetários não antecipados afetam a produção e o "
            "emprego reais, e de forma transitória.”</i> → CERTO",
            "<i>“Para os monetaristas, a política monetária sistemática afeta o emprego no curto prazo, mas não no "
            "longo.”</i> → CERTO",
        ])],
        "reescrita": ("A Nova Economia Clássica argumenta que a política monetária sistemática " + hl("não pode")
                      + " gerenciar efetivamente a produção e o emprego reais " + hl("nem mesmo") + " no curto "
                      "prazo."),
        "tipo_erro": ["TROCA_ATOR", "RESTRICAO"], "moduladores": ["apenas"], "dificuldade": 2,
        "comentario_fonte": ("Com expectativas racionais, políticas sistemáticas e previsíveis são ineficazes até no "
                             "curto prazo; só surpresas teriam efeito."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00838
    {
        "id": "ECO-E2-L00838-1", "fonte_ref": "E2-L00838", "destino": "30", "subtema": H2["deb"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação às políticas monetárias e fiscais, julgue (C ou E) os itens que se seguem.",
        "rotulo_item": "Item",
        "assertiva": ("De acordo com os novos clássicos, a redução preanunciada na taxa de crescimento do estoque "
                      "monetário é instrumento eficaz de combate à inflação, mas reduz a atividade econômica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com os novos clássicos, a redução preanunciada na taxa de crescimento do estoque "
                       "monetário é instrumento eficaz de combate à inflação, ") + vm("mas reduz a atividade "
                                                                                     "econômica") + az(".")),
        "poucas": ("Anunciada e crível, a redução do crescimento monetário baixa a inflação esperada junto com a "
                   "efetiva: " + azb("desinflação sem dor") + ", com " + vd("taxa de sacrifício zero")
                   + ". A atividade não cai."),
        "destrinchando": [
            "Lógica novo-clássica: expectativas racionais + preços e salários flexíveis. O anúncio entra em πᵉ "
            "imediatamente; salários e preços passam a subir menos já no período seguinte; a curva de Phillips de "
            "curto prazo desce junto e a economia vai de inflação alta a baixa " + vd("sem sair de uₙ") + ".",
            "Primeira metade do item é verdadeira: reduzir o crescimento da moeda combate a inflação (teoria "
            "quantitativa, π ≈ gM − gY no longo prazo). O erro é o custo em atividade, que só existe com "
            "<b>surpresa</b> ou expectativas adaptativas.",
            "Condição decisiva: " + azb("credibilidade") + ". Se o público duvida do anúncio, πᵉ não cai e a "
            "política vira, na prática, surpresa contracionista — com recessão. " + oc("Sargent") + " (“The Ends "
            "of Four Big Inflations”, 1982) usou o fim das hiperinflações europeias dos anos 1920, obtido com "
            "reformas fiscais e monetárias críveis, como evidência.",
            "Contraste: monetaristas e keynesianos preveem desemprego temporário (taxa de sacrifício positiva); "
            "novos keynesianos lembram que contratos já firmados impedem o ajuste instantâneo, de modo que até a "
            "desinflação crível custa algo.",
            vm("Regra-âncora: novos clássicos + anúncio crível = desinflação sem perda de produto."),
        ],
        "dissecando": (cz("[meia-verdade · troca de ator]") + " Primeira oração certa, segunda enxertada de outra "
                       "escola. A pista está no “preanunciada”: para os novos clássicos, anunciar é justamente o "
                       "que elimina o custo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com os novos clássicos, uma redução não antecipada do crescimento monetário pode reduzir "
            "temporariamente a atividade econômica.”</i> → CERTO",
            "<i>“Para os monetaristas, a redução gradual do crescimento monetário combate a inflação com custo "
            "temporário em desemprego.”</i> → CERTO",
        ])],
        "reescrita": ("De acordo com os novos clássicos, a redução preanunciada na taxa de crescimento do estoque "
                      "monetário é instrumento eficaz de combate à inflação, " + hl("sem reduzir a atividade "
                                                                                   "econômica") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Política antecipada afeta só os preços; redução preanunciada do crescimento da moeda "
                             "reduz a inflação sem afetar a atividade — desinflação “sem dor”, sem taxa de sacrifício."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01005
    {
        "id": "ECO-E2-L01005-1", "fonte_ref": "E2-L01005", "destino": "30", "subtema": H2["deb"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("No Modelo Novo Clássico, a existência de rigidezes (nominal ou real) explica a não neutralidade "
                      "da moeda no longo prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No Modelo ") + vm("Novo Clássico") + az(", a existência de rigidezes (nominal ou real) "
                       "explica a não neutralidade da moeda no ") + vm("longo prazo") + az(".")),
        "poucas": ("O modelo " + oc("novo clássico") + " supõe preços e salários " + vd("flexíveis") + " — não há "
                   "rigidez. Rigidezes que explicam a não neutralidade são dos " + oc("novos keynesianos")
                   + ", e valem para o " + vd("curto prazo") + "."),
        "destrinchando": [
            "Novos clássicos: agentes maximizadores, expectativas racionais e " + azb("market clearing")
            + " contínuo. Moeda antecipada é neutra já no curto prazo; a não antecipada tem efeito transitório por "
            "erro de percepção (confundir nível geral com preço relativo), e não por rigidez.",
            "Novos keynesianos (" + oc("Mankiw") + ", " + oc("Akerlof") + " e " + oc("Yellen") + ", "
            + oc("Blanchard") + ", " + oc("Stiglitz") + "): mantêm expectativas racionais, mas mostram por que "
            "preços e salários não se ajustam de imediato. " + azb("Rigidez nominal") + ": custos de menu, "
            "contratos escalonados (" + oc("Taylor") + ", " + oc("Calvo") + "). " + azb("Rigidez real") + ": "
            "salário-eficiência, contratos implícitos, insiders × outsiders.",
            "Mesmo para os novos keynesianos, rigidez é fenômeno de " + vd("curto prazo") + ": com o tempo, preços e "
            "salários se ajustam e a moeda volta a ser neutra. Neutralidade de longo prazo é praticamente consenso "
            "entre as escolas do mainstream.",
            vm("Regra-âncora: rigidez → novos keynesianos → não neutralidade de curto prazo."),
        ],
        "dissecando": (cz("[troca de ator · troca de conceito]") + " Dois enxertos: a escola (novos clássicos no "
                       "lugar de novos keynesianos) e o horizonte (longo no lugar de curto). Pista imediata: "
                       "“novo clássico” e “rigidez” são termos que se excluem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nos modelos novo-keynesianos, rigidezes nominais e reais explicam a não neutralidade da moeda no "
            "curto prazo.”</i> → CERTO",
            "<i>“No modelo novo clássico, a moeda não antecipada é neutra mesmo no curto prazo.”</i> → ERRADO (a "
            "não antecipada tem efeito transitório)",
        ])],
        "reescrita": ("No Modelo " + hl("Novo Keynesiano") + ", a existência de rigidezes (nominal ou real) explica a "
                      "não neutralidade da moeda no " + hl("curto prazo") + "."),
        "tipo_erro": ["TROCA_ATOR", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("No modelo novo clássico preços e salários são flexíveis e as expectativas racionais; "
                             "política sistemática não afeta produção e emprego; só surpresas têm efeito de curto "
                             "prazo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
