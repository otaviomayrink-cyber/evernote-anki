"""Cards do lote de redação 13 — ECO, passada 02 (notas 28: OA-DA e 29: curva de Phillips e expectativas)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "da": "📈 Demanda agregada",
    "oa": "🏭 Oferta agregada e choques",
    "ph": "📉 Phillips original e aceleracionista",
    "ex": "🔮 Expectativas e NAIRU",
}

CMD_RT_INF = ("Em 2021, o mundo todo tem passado por uma aceleração inflacionária, que combina elementos de oferta e "
              "de demanda. A este respeito, julgue o item a seguir.")

CMD_RT_OADA = "Sobre o modelo de oferta e demanda agregadas com expectativas, julgue o item a seguir."

CMD_TJPA = ("Considerando essa situação hipotética, julgue o item que se segue, em relação aos efeitos "
            "macroeconômicos de choques salariais e fiscais, e de movimentos nos preços internos.")

EXC_TJPA = ("<p><i>Uma economia nacional opera com capital fixo no curto prazo e está sujeita a variações nominais "
            "de salários, preços internos e políticas fiscais expansionistas. O país adota um regime de taxa de "
            "câmbio fixa e mantém constante o nível de preços internacionais.</i></p>")

CMD_ANTT_ISLM = "Considerando o modelo IS-LM, em que o Banco Central fixa a quantidade de moeda, julgue o item a seguir."

CMD_ANTT_ABERTA = "Julgue o próximo item, tendo em vista os modelos macroeconômicos para economias abertas."

CMD_NAB_TEORIA = "Em relação à teoria macroeconômica, julgue o item a seguir."

CMD_NAB_MODELOS = "Em relação aos modelos macroeconômicos, julgue o item a seguir."

CMD_NAB_MACRO = "Em relação à macroeconomia, julgue o item a seguir."

CMD_NAB_PHILLIPS = ("Em relação à curva de Phillips e à formação de expectativas dos agentes, julgue o item a "
                    "seguir.")

ANTT_ANO = ("nota_redacao: a frente data a prova de 2023; o print do Qconcursos reproduzido no verso de outro item "
            "da mesma prova traz 2024 — mantido o ano da frente")

FIG_E1 = lambda ref: [{"ref": ref, "tipo_fonte": "IMAGEM", "lado": "verso",
                       "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}]

CARDS = [
    # ------------------------------------------------------------------ E2-L01602
    {
        "id": "ECO-E2-L01602-1", "fonte_ref": "E2-L01602", "destino": "28", "subtema": H2["da"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_INF,
        "rotulo_item": "Item",
        "assertiva": ("Uma medida como o Auxílio emergencial, adotada para garantir renda aos mais pobres durante a "
                      "pandemia, atua expandindo a demanda agregada da economia, o que pode pressionar a inflação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma medida como o Auxílio emergencial, adotada para garantir renda aos mais pobres durante a "
                      "pandemia, atua <u>expandindo a demanda agregada</u> da economia, o que <u>pode</u> pressionar "
                      "a inflação."),
        "poucas": ("Transferência de renda é " + azb("política fiscal expansionista") + ": eleva a renda disponível "
                   "de quem tem alta propensão a consumir, desloca a " + azb("DA para a direita") + " e, com oferta "
                   "travada, pressiona os preços."),
        "destrinchando": [
            "Transferências (T<sub>r</sub>) não entram diretamente no PIB pela ótica da despesa — não são compra de "
            "bens pelo governo —, mas elevam a " + azb("renda disponível") + " Y<sub>d</sub> = Y − T + T<sub>r</sub>"
            " e, por ela, o consumo. Na cruz keynesiana, o multiplicador da transferência é "
            + vd("c/(1 − c)") + ", menor que o do gasto direto, " + vd("1/(1 − c)") + ".",
            "O efeito é maior quando o dinheiro vai para famílias pobres: sua " + azb("propensão marginal a "
            "consumir") + " é próxima de 1 (quase tudo vira consumo), enquanto famílias ricas poupam boa parte da "
            "renda extra.",
            "No modelo OA-DA, a DA vai para a direita. O resultado depende da oferta: com capacidade ociosa, sobe "
            "sobretudo o produto; com a " + azb("OA inclinada ou travada") + " — como na pandemia, com gargalos "
            "de produção e de cadeias globais —, sobe sobretudo o nível de preços: " + azb("inflação de demanda")
            + ".",
            "Em 2021 os dois lados se somaram: estímulos fiscais e monetários do lado da demanda e choques de "
            "oferta (fretes, semicondutores, energia, alimentos) do lado da oferta. Daí o comando falar em "
            "inflação que “combina elementos de oferta e de demanda”.",
            vm("Regra-âncora: transferência ↑ → renda disponível ↑ → C ↑ → DA → direita; com oferta rígida, o "
               "ajuste vem mais pelos preços que pela quantidade."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item descreve o canal correto "
                       "(transferência → consumo → DA) e se protege com “pode pressionar”: não diz que a inflação "
                       "foi causada só pelo auxílio. A tentação de marcar ERRADO vem de achar que transferência "
                       "“não é gasto” e por isso não mexe na DA."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Auxílio emergencial, por ser transferência e não compra de bens, não altera a demanda "
            "agregada.”</i> → ERRADO (atua pela renda disponível e pelo consumo)",
            "<i>“A transferência de renda tem multiplicador maior que o de um aumento equivalente dos gastos do "
            "governo.”</i> → ERRADO (inversão: o multiplicador da transferência é o menor)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Auxílio é política fiscal expansionista de transferência: eleva a renda disponível de "
                             "famílias com alta propensão a consumir, expande a DA e, com oferta restrita, gera "
                             "inflação de demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01675
    {
        "id": "ECO-E2-L01675-1", "fonte_ref": "E2-L01675", "destino": "28", "subtema": H2["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_OADA,
        "rotulo_item": "Item",
        "assertiva": ("A oferta agregada no longo prazo é dada por fatores de oferta como a tecnologia e a taxa "
                      "natural de desemprego, porém no curto prazo ela pode ser elástica ao nível de preços devido a "
                      "salários nominais rígidos, custos de cardápio ou percepções equivocadas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A oferta agregada no <u>longo prazo</u> é dada por fatores de oferta como a tecnologia e a "
                      "taxa natural de desemprego, porém no <u>curto prazo</u> ela pode ser elástica ao nível de "
                      "preços devido a <u>salários nominais rígidos, custos de cardápio ou percepções "
                      "equivocadas</u>."),
        "poucas": ("No longo prazo a " + azb("OALP é vertical") + " no produto potencial, fixado por fatores "
                   "reais; no curto prazo a " + azb("OACP é positivamente inclinada") + ", e os manuais dão "
                   "exatamente três explicações para isso: salários rígidos, preços rígidos (custos de menu) e "
                   "percepções equivocadas."),
        "destrinchando": [
            azb("Longo prazo") + ": o produto potencial Yₙ depende de trabalho, capital, recursos naturais e "
            "tecnologia; o emprego está na " + azb("taxa natural de desemprego") + ". Preços e salários já se "
            "ajustaram, então P não afeta Y: a OALP é " + vd("vertical") + " — é a dicotomia clássica.",
            azb("Curto prazo") + ": a OACP sobe para a direita, resumida em " + vd("Y = Yₙ + α(P − Pᵉ)") + ". "
            "Os três modelos de " + oc("Mankiw") + " (<i>Macroeconomia</i>) para essa inclinação:",
            "(1) " + azb("salários nominais rígidos") + " (contratos): se P sobe e W não, o salário real cai, as "
            "firmas contratam e produzem mais; (2) " + azb("preços rígidos") + " por " + azb("custos de "
            "cardápio") + " (menu costs): parte das firmas não remarca, vende mais quando a demanda sobe; "
            "(3) " + azb("percepções equivocadas") + " (" + oc("Friedman") + ", " + oc("Lucas") + "): o produtor "
            "confunde alta geral de preços com alta do seu preço relativo e aumenta a produção.",
            "O ponto comum: todos dependem de " + azb("P ≠ Pᵉ") + ". Quando as expectativas se ajustam, a OACP se "
            "desloca até que o produto volte a Yₙ — por isso a não neutralidade da moeda é só de curto prazo.",
            "“Elástica ao nível de preços” aqui quer dizer que a quantidade ofertada reage a P (curva não "
            "vertical) — não que seja horizontal.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz a síntese do manual (OALP real, "
                       "OACP por rigidez ou erro de percepção). O “pode ser elástica” protege o item; o risco é "
                       "achar que custos de cardápio ou percepções equivocadas “não são de oferta”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A oferta agregada de longo prazo depende do nível de preços, pois salários nominais rígidos "
            "impedem o ajuste.”</i> → ERRADO (troca de prazo: rigidez explica a OACP)",
            "<i>“No curto prazo, a oferta agregada pode ser positivamente inclinada porque os produtores confundem "
            "variações do nível geral de preços com variações de preços relativos.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("OALP vertical, determinada por fatores reais; OACP positivamente inclinada por "
                             "salários rígidos, custos de menu ou percepções equivocadas (Lucas); trade-off só de "
                             "curto prazo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 488", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "cortada (diagrama de contração da DA, sem relação direta com o item)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01676
    {
        "id": "ECO-E2-L01676-1", "fonte_ref": "E2-L01676", "destino": "28", "subtema": H2["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_OADA,
        "rotulo_item": "Item",
        "assertiva": "Com uma oferta agregada positivamente inclinada, a moeda será neutra e será válida a lei de Say.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Com uma oferta agregada positivamente inclinada, a moeda ") + vm("será neutra")
                    + az(" e ") + vm("será válida") + az(" a lei de Say.")),
        "poucas": ("OA " + azb("positivamente inclinada") + " é o caso de curto prazo: choques de demanda — "
                   "inclusive monetários — mudam o produto. Neutralidade da moeda e lei de Say são marcas da "
                   + azb("OA vertical") + " (clássica ou de longo prazo)."),
        "destrinchando": [
            azb("Neutralidade da moeda") + ": variações de M alteram só variáveis nominais (P, W, câmbio "
            "nominal), nunca produto, emprego ou juros reais. Graficamente, exige " + vd("OA vertical") + ": a DA "
            "desloca e só P muda.",
            "Com OA inclinada, uma expansão monetária desloca a DA para a direita e eleva " + vd("Y e P")
            + " ao mesmo tempo: a moeda tem efeito real — " + azb("não neutra") + " no curto prazo.",
            azb("Lei de Say") + " (" + oc("Jean-Baptiste Say") + "): “a oferta cria sua própria demanda” — a "
            "produção gera a renda que a compra, e não há insuficiência geral de demanda. No modelo clássico o "
            "produto é determinado só pela oferta (OA vertical), e a demanda apenas fixa P.",
            "Com OA inclinada, a DA importa para o produto: insuficiência de demanda gera recessão e desemprego — "
            "exatamente o que " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) opôs à lei de Say com o "
            + azb("princípio da demanda efetiva") + ".",
            vm("Regra-âncora: OA vertical → moeda neutra e Say; OA inclinada (ou horizontal) → demanda e moeda "
               "afetam o produto."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item cola nas hipóteses de curto prazo as "
                       "conclusões do modelo clássico. Pista: “positivamente inclinada” é justamente o caso em "
                       "que a DA mexe em Y; neutralidade e Say pedem a curva vertical."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com uma oferta agregada vertical, a moeda será neutra.”</i> → CERTO",
            "<i>“Com oferta agregada positivamente inclinada, uma expansão monetária eleva o produto e o nível de "
            "preços no curto prazo.”</i> → CERTO",
        ])],
        "reescrita": ("Com uma oferta agregada positivamente inclinada, a moeda " + hl("não será neutra") + " e "
                      + hl("não valerá") + " a lei de Say."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("OA inclinada implica moeda não neutra no curto prazo; neutralidade e lei de Say "
                             "pertencem ao longo prazo/modelo clássico, com OA vertical."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01677
    {
        "id": "ECO-E2-L01677-1", "fonte_ref": "E2-L01677", "destino": "28", "subtema": H2["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_OADA,
        "rotulo_item": "Item",
        "assertiva": ("Uma contração da demanda no curto prazo, dada por uma elevação da incerteza, terá como efeito "
                      "o aumento do desemprego acima da taxa natural, porém com o tempo a curva de oferta de curto "
                      "prazo vai se expandir até que a economia volte ao equilíbrio de longo prazo, no nível da taxa "
                      "natural de desemprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma contração da demanda no curto prazo, dada por uma elevação da incerteza, terá como "
                      "efeito o aumento do desemprego <u>acima da taxa natural</u>, porém com o tempo a curva de "
                      "oferta de curto prazo vai <u>se expandir</u> até que a economia volte ao equilíbrio de longo "
                      "prazo, no nível da taxa natural de desemprego."),
        "poucas": ("É o " + azb("ajuste automático") + " do modelo OA-DA: a DA cai, o produto fica abaixo de Yₙ "
                   "(desemprego acima do natural); salários e preços esperados cedem, a " + azb("OACP desloca-se "
                   "para a direita") + " e a economia volta a Yₙ com preços menores."),
        "destrinchando": [
            "Mais incerteza reduz consumo (poupança precaucional) e investimento (adiamento de projetos): a "
            + azb("DA desloca-se para a esquerda") + ". Com a OACP inclinada, o produto cai abaixo de Yₙ e o "
            "desemprego sobe acima da " + azb("taxa natural") + " — desemprego cíclico.",
            "Com desemprego alto, os salários nominais e os preços esperados passam a cair nas renegociações. "
            "Custos menores deslocam a " + azb("OACP para baixo e para a direita") + " — é a “expansão” do item.",
            "O processo para quando a OACP cruza a DA nova sobre a OALP: produto de volta a " + vd("Yₙ")
            + ", desemprego de volta à taxa natural, nível de preços " + vd("mais baixo") + " que o inicial.",
            "O debate é sobre a <b>velocidade</b>: para clássicos e novos-clássicos o ajuste é rápido; para "
            "keynesianos ele é lento e custoso (salários rígidos para baixo), o que justifica política "
            "anticíclica para encurtar a recessão. " + oc("Keynes") + ": “no longo prazo, estaremos todos "
            "mortos”.",
        ],
        "grafico_verso": "ECO-E2-L01677-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item narra corretamente as duas etapas (choque de "
                       "demanda e ajuste da oferta). O risco está em “expandir”: quem pensa que uma recessão "
                       "“encolhe” a oferta marca ERRADO. Preste atenção ao sentido: salários em queda → OACP para "
                       "a direita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com o tempo a curva de oferta de curto prazo vai se contrair até que a economia volte ao "
            "equilíbrio de longo prazo.”</i> → ERRADO (sentido trocado: ela se expande)",
            "<i>“…a economia volta ao equilíbrio de longo prazo com nível de preços igual ao inicial.”</i> → ERRADO "
            "(dado alterado: o nível de preços termina mais baixo)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["com o tempo"], "dificuldade": 2,
        "comentario_fonte": ("Incerteza reduz C e I, DA para a esquerda; produto abaixo do potencial e desemprego "
                             "acima do natural; salários caem, OACP desloca-se para a direita até o retorno ao "
                             "potencial com preços menores."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 488", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "redesenhada e completada com o ajuste da OACP (ECO-E2-L01677-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01678
    {
        "id": "ECO-E2-L01678-1", "fonte_ref": "E2-L01678", "destino": "28", "subtema": H2["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_OADA,
        "rotulo_item": "Item",
        "assertiva": ("Partindo do equilíbrio de longo prazo, um choque adverso na oferta poderia ser acomodado com "
                      "uma política de expansão da demanda pelo governo, mantendo a economia na taxa natural de "
                      "desemprego, porém com um nível de preços mais elevado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Partindo do equilíbrio de longo prazo, um choque adverso na oferta <u>poderia</u> ser "
                      "acomodado com uma política de expansão da demanda pelo governo, mantendo a economia na taxa "
                      "natural de desemprego, porém com um <u>nível de preços mais elevado</u>."),
        "poucas": ("Choque adverso desloca a " + azb("OACP para a esquerda") + " (estagflação). "
                   + azb("Acomodar") + " é expandir a DA para devolver o produto a Yₙ: o desemprego volta ao "
                   "natural, mas o nível de preços sobe ainda mais."),
        "destrinchando": [
            "Choque adverso de oferta (petróleo, quebra de safra, alta de salários acima da produtividade) eleva "
            "custos: a OACP sobe/esquerda. Resultado: " + vd("P ↑ e Y ↓") + " — " + azb("estagflação") + ".",
            "Duas saídas: (1) <b>não acomodar</b> — esperar que o desemprego derrube salários e custos até a OACP "
            "voltar; os preços retornam ao nível inicial, mas a recessão dura; (2) <b>acomodar</b> — expandir a DA "
            "(política fiscal ou monetária): o produto volta logo a Yₙ, e o preço fica permanentemente " + vd("mais "
            "alto") + ".",
            "É o dilema dos " + vd("choques do petróleo dos anos 1970") + ": muitos países acomodaram e "
            "colheram inflação persistente. Um ponto conceitual: o item supõe choque <b>temporário de custos</b> "
            "(só a OACP se move). Se o choque reduzisse o próprio produto potencial (OALP para a esquerda), "
            "nenhuma expansão de demanda manteria o produto antigo sem acelerar a inflação.",
            "Nos regimes de " + azb("metas de inflação") + ", a resposta usual é acomodar só os " + azb("efeitos "
            "primários") + " do choque e combater os " + azb("efeitos secundários") + " (contaminação de "
            "expectativas e de preços não afetados diretamente).",
        ],
        "grafico_verso": "ECO-E2-L01678-1-V1",
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item descreve a política de acomodação "
                       "com o custo certo (preços mais altos) e se protege com “poderia”. A dúvida plantada é se a "
                       "política de demanda “consegue” manter a taxa natural diante de um choque de oferta — "
                       "consegue, se o choque atinge só a OACP."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…um choque adverso na oferta poderia ser acomodado com expansão da demanda, mantendo a economia "
            "na taxa natural de desemprego e com o nível de preços inalterado.”</i> → ERRADO (custo omitido: o "
            "preço sobe)",
            "<i>“Diante de um choque adverso de oferta, a política de demanda só pode escolher entre mais "
            "inflação e mais desemprego.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["poderia"], "dificuldade": 2,
        "comentario_fonte": ("Choque adverso desloca a OACP para a esquerda (estagflação); a acomodação expande a "
                             "DA, devolve o produto ao potencial e eleva permanentemente o nível de preços."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 489", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01678-1-V1)"}],
        "alertas": ["qualidade_fonte: um dos comentários de origem diz que o choque desloca a oferta de LONGO prazo "
                    "e fala em “nova taxa natural”; o item supõe choque na OACP, com a OALP fixa — corrigido"],
    },
    # ------------------------------------------------------------------ E3-L00028
    {
        "id": "ECO-E3-L00028-1", "fonte_ref": "E3-L00028", "destino": "28", "subtema": H2["oa"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA, "excerto": EXC_TJPA,
        "rotulo_item": "Item",
        "assertiva": ("O aumento do salário nominal, mantido constante o estoque de capital no curto prazo, tende a "
                      "elevar o nível geral de preços e a reduzir o produto real da economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento do salário nominal, mantido constante o estoque de capital no curto prazo, "
                      "<u>tende a</u> elevar o nível geral de preços e a <u>reduzir o produto real</u> da economia."),
        "poucas": ("Salário nominal maior com capital fixo = custo marginal maior: a " + azb("OACP desloca-se para "
                   "cima e para a esquerda") + " — " + azb("choque adverso de oferta") + ", com " + vd("P ↑")
                   + " e " + vd("Y ↓") + " (estagflação)."),
        "destrinchando": [
            "Com K fixo, a firma produz mais só contratando mais trabalho, e o " + azb("produto marginal do "
            "trabalho") + " é decrescente. Ela contrata até PMgL = W/P. Se W sobe e P não acompanha, o "
            + azb("salário real") + " sobe, a firma contrata menos e produz menos a cada nível de preços.",
            "No gráfico: a OACP desloca-se para cima/esquerda. Com a DA dada, o novo equilíbrio tem "
            + vd("preços maiores e produto menor") + " — " + azb("inflação de custos") + ", o oposto do "
            "choque de demanda, em que P e Y andam juntos.",
            "O enunciado acrescenta câmbio fixo e preços externos constantes: não há desvalorização para "
            "devolver competitividade, e a alta de P interno ainda " + azb("aprecia o câmbio real") + " "
            "(q = eP*/P cai), o que reforça a perda de produto via exportações líquidas.",
            "Sem acomodação, o desemprego tende a forçar os salários de volta para baixo, e a OACP retorna; com "
            "acomodação (expansão da DA), o produto se recupera, mas os preços ficam ainda mais altos.",
            vm("Regra-âncora: salário nominal mexe na OA (custo), não na DA; choque de custo → P ↑ e Y ↓."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item descreve o choque de custos em "
                       "linguagem de manual e se protege com “tende a”. Quem pensa no salário como renda (mais "
                       "consumo, mais DA) espera produto maior e marca ERRADO; a pista é o “capital fixo no curto "
                       "prazo”, que aponta para o lado da oferta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento do salário nominal, mantido constante o estoque de capital, desloca a demanda agregada "
            "para a direita e eleva o produto real.”</i> → ERRADO (troca de conceito: é choque de oferta)",
            "<i>“A redução do salário nominal, com preços dados, desloca a oferta agregada para baixo e para a "
            "direita.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Aumento do salário nominal com capital fixo eleva custos, desloca a OA para a "
                             "esquerda e gera estagflação: preços sobem e produto real cai; câmbio fixo não "
                             "amortece."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00031
    {
        "id": "ECO-E3-L00031-1", "fonte_ref": "E3-L00031", "destino": "28", "subtema": H2["da"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA, "excerto": EXC_TJPA,
        "rotulo_item": "Item",
        "assertiva": ("A elevação dos gastos públicos, mantida constante a taxa de juros nominal, pode provocar "
                      "aumento da atividade econômica, pressão sobre os preços e apreciação da taxa real de câmbio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elevação dos gastos públicos, mantida constante a taxa de juros nominal, <u>pode</u> "
                      "provocar aumento da atividade econômica, pressão sobre os preços e <u>apreciação da taxa "
                      "real de câmbio</u>."),
        "poucas": ("G ↑ com juros constantes desloca a " + azb("DA para a direita") + ": Y ↑ e P ↑. Com câmbio "
                   "nominal fixo e P* constante, a alta de P reduz q = eP*/P — " + azb("apreciação real") + "."),
        "destrinchando": [
            "Juros nominais mantidos constantes significam que a autoridade monetária " + azb("acomoda") + " a "
            "expansão fiscal (a LM acompanha a IS): não há " + azb("crowding out") + " pelos juros, e o efeito "
            "multiplicador sobre a demanda é pleno.",
            "Com a OA de curto prazo positivamente inclinada, a DA maior eleva " + vd("produto e preços")
            + " ao mesmo tempo: mais atividade e pressão inflacionária.",
            azb("Câmbio real") + " q = e · P*/P (preço dos bens externos em termos dos domésticos). Com "
            + vd("e fixo") + " (regime do enunciado) e " + vd("P* constante") + ", o aumento de P derruba q: os "
            "bens nacionais ficam relativamente mais caros — " + azb("apreciação real") + ", com perda de "
            "competitividade e piora das exportações líquidas.",
            "Ligação útil: em câmbio fixo, o ajuste do câmbio real só pode vir pelos <b>preços</b>. É o mecanismo "
            "das experiências de âncora cambial, como a do " + rx("Plano Real (1994–1999)") + ", em que a "
            "inflação residual apreciou o câmbio real e ampliou o déficit em transações correntes.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Três efeitos encadeados, todos corretos, "
                       "protegidos pelo “pode”. A armadilha está no terceiro: quem pensa que câmbio fixo impede "
                       "qualquer variação cambial esquece que o câmbio <b>real</b> muda com os preços."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a elevação dos gastos públicos provoca depreciação da taxa real de câmbio.”</i> → ERRADO "
            "(inversão: P ↑ com e fixo aprecia)",
            "<i>“Em regime de câmbio fixo, a taxa real de câmbio permanece constante.”</i> → ERRADO (troca de "
            "conceito: fixo é o câmbio nominal)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("Com juros constantes, G ↑ desloca a DA: atividade e preços sobem; com câmbio fixo e "
                             "P* constante, P ↑ aprecia o câmbio real e reduz a competitividade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00132
    {
        "id": "ECO-E3-L00132-1", "fonte_ref": "E3-L00132", "destino": "28", "subtema": H2["da"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_ISLM,
        "rotulo_item": "Item",
        "assertiva": "A política monetária expansionista proporciona redução da taxa de juros e do salário real.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A política monetária expansionista proporciona redução da taxa de juros e <u>do salário "
                      "real</u>."),
        "poucas": ("M ↑ desloca a " + azb("LM para a direita") + " (i ↓) e a " + azb("DA para a direita")
                   + "; com OA inclinada, P sobe. Com salário nominal rígido no curto prazo, " + vd("W/P cai")
                   + " — e é isso que permite às firmas contratar mais."),
        "destrinchando": [
            "Juros: mais moeda com a mesma demanda por moeda exige " + vd("i menor") + " para equilibrar o "
            "mercado monetário a cada renda — a LM desloca-se para a direita, i cai e o investimento sobe.",
            "Preços: na passagem para o OA-DA, a LM à direita significa DA à direita. Se nada for dito sobre o "
            "prazo, a banca assume o " + azb("curto prazo com OA positivamente inclinada") + ": Y e " + vd("P")
            + " sobem.",
            "Salário real: no modelo keynesiano de curto prazo o " + azb("salário nominal W é rígido") + ". "
            "Com P maior, " + vd("W/P cai") + ". Isso não é acidente: pela " + azb("demanda por trabalho")
            + " (PMgL = W/P, com PMgL decrescente e capital fixo), as firmas só contratam mais — e só produzem "
            "mais — se o salário real cair. Produto ↑ e salário real ↓ andam juntos nesse modelo.",
            "Fora do curto prazo, os salários nominais se reajustam à inflação, a OA volta ao potencial e W/P "
            "retorna ao nível inicial: a moeda é neutra no longo prazo.",
            "Nota histórica: a correlação prevista (salário real anticíclico) foi contestada empiricamente por "
            + oc("Dunlop") + " e " + oc("Tarshis") + " (1938-1939), o que alimentou as versões de rigidez de "
            "preços (e não de salários) da teoria novo-keynesiana.",
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " A primeira metade é óbvia; o item se decide no "
                       "“salário real”, que exige ligar três peças: LM → DA → OA inclinada com W rígido. 🔥 A "
                       "CEBRASPE usa essa cadeia em várias provas; sem menção a prazo, adote curto prazo com OA "
                       "positivamente inclinada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política monetária expansionista proporciona redução da taxa de juros e aumento do salário "
            "real.”</i> → ERRADO (inversão: P ↑ com W rígido reduz W/P)",
            "<i>“No longo prazo, a política monetária expansionista reduz permanentemente o salário real.”</i> → "
            "ERRADO (troca de prazo: no longo prazo a moeda é neutra)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Expansão monetária reduz juros e eleva a DA; preços sobem e, com salário nominal "
                             "rígido, o salário real cai. Uma das respostas considera o item “impreciso”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 124", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (anotação manuscrita com print do Qconcursos; mecanismo absorvido no "
                                   "📖)"}],
        "alertas": [ANTT_ANO,
                    "qualidade_fonte: um dos comentários de origem diz que o aumento de preços “reduz o salário "
                    "nominal” (é o real) e outro sugere que o item seria impreciso; o gabarito oficial CERTO "
                    "segue o modelo keynesiano de curto prazo"],
    },
    # ------------------------------------------------------------------ E3-L00134
    {
        "id": "ECO-E3-L00134-1", "fonte_ref": "E3-L00134", "destino": "28", "subtema": H2["da"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_ISLM,
        "rotulo_item": "Item",
        "assertiva": "A redução do salário nominal desloca a curva de demanda agregada para baixo e para a direita.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A redução do salário nominal desloca a curva de ") + vm("demanda agregada")
                    + az(" para baixo e para a direita.")),
        "poucas": ("Salário nominal é " + azb("custo de produção") + ": sua redução desloca a " + azb("oferta "
                   "agregada") + " para baixo e para a direita. A DA (IS-LM) não depende de W."),
        "destrinchando": [
            "A " + azb("DA") + " nasce do IS-LM: para cada P, o equilíbrio simultâneo de bens e moeda dá um Y. "
            "Seus deslocadores são G, T, M, expectativas, confiança, exportações — " + vm("não o salário "
            "nominal") + ".",
            "A " + azb("OA") + " de curto prazo vem do mercado de trabalho e dos custos: com W menor, a firma "
            "pode cobrar menos pelo mesmo produto (ou produzir mais ao mesmo preço) — a OA desce/vai para a "
            "direita, P cai e Y sobe.",
            "Pista geométrica: uma curva <b>negativamente inclinada</b> (DA) que se expande vai “para cima e para "
            "a direita”; “para baixo e para a direita” descreve a expansão de uma curva <b>positivamente "
            "inclinada</b> — a OA. A própria redação do item aponta para a curva errada.",
            "Nuance: a rigor, o que move a OA é o " + azb("salário real") + " em relação aos preços; a "
            "formulação de manual (W ↓ com P dado → OA ↓/→) é a cobrada pela banca. Efeitos indiretos de W sobre a "
            "DA (renda dos trabalhadores, efeito Pigou com preços cadentes) não deslocam a DA no modelo básico: "
            "a queda de P resultante gera <b>movimento ao longo</b> da DA.",
            vm("Regra-âncora: salário nominal → OA; política fiscal, monetária e expectativas → DA."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O sentido do deslocamento (baixo/direita) está certo para a "
                       "curva certa; o item troca só a curva. 🔥 A CEBRASPE repete a armadilha “salário nominal "
                       "desloca a DA” em vários concursos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução do salário nominal desloca a curva de oferta agregada para baixo e para a "
            "direita.”</i> → CERTO",
            "<i>“A redução do salário nominal provoca movimento ao longo da curva de demanda agregada, com queda "
            "do nível de preços.”</i> → CERTO",
        ])],
        "reescrita": ("A redução do salário nominal desloca a curva de " + hl("oferta agregada")
                      + " para baixo e para a direita."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Salário nominal afeta a OA, não a DA; a DA se desloca por política fiscal, monetária "
                             "ou expectativas; a expansão da DA seria para cima e para a direita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ANTT_ANO],
    },
    # ------------------------------------------------------------------ E3-L00136
    {
        "id": "ECO-E3-L00136-1", "fonte_ref": "E3-L00136", "destino": "28", "subtema": H2["da"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("O efeito Pigou implica que a elevação dos salários nominais proporcionará inflação de preços, "
                      "de modo que o desemprego se tornará compatível com a situação de equilíbrio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O efeito Pigou implica que a ") + vm("elevação dos salários nominais proporcionará "
                    "inflação de preços") + az(", de modo que o desemprego ") + vm("se tornará compatível com a "
                    "situação de equilíbrio") + az(".")),
        "poucas": ("O " + azb("efeito Pigou") + " (efeito saldos reais) vai no sentido oposto: a " + vd("queda")
                   + " de salários e preços eleva M/P e a riqueza real, estimula o consumo e tende a "
                   + azb("eliminar") + " o desemprego, levando ao pleno emprego."),
        "destrinchando": [
            "Contexto: " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936) sustentou que a economia pode ficar em "
            + azb("equilíbrio com desemprego") + ", mesmo com salários flexíveis — a deflação poderia não "
            "baixar os juros (armadilha da liquidez) nem reanimar o investimento.",
            oc("Arthur Cecil Pigou") + " respondeu (anos 1940) com o " + azb("efeito saldos monetários reais")
            + ": se P cai com M dado, " + vd("M/P ↑") + "; os detentores de moeda (e de ativos nominais) ficam "
            "mais ricos e " + vd("consomem mais") + ", mesmo sem queda de juros. A IS/DA se expande e o "
            "desemprego involuntário tende a desaparecer.",
            "Logo, para Pigou o desemprego <b>não</b> é compatível com o equilíbrio de longo prazo com preços "
            "flexíveis. Junto com o " + azb("efeito Keynes") + " (P ↓ → M/P ↑ → i ↓ → I ↑) e o "
            + azb("efeito Mundell-Fleming") + " (P ↓ → câmbio real deprecia → NX ↑), ele explica a "
            "<b>inclinação negativa da DA</b>.",
            "O item descreve outra coisa: salários nominais subindo e empurrando preços é " + azb("inflação de "
            "custos") + " (choque de oferta). E a inflação, com M fixo, faz o oposto do Pigou: reduz M/P e a "
            "riqueza real.",
            "Ressalva empírica: o efeito é teoricamente válido, mas fraco; a deflação eleva o peso real das "
            "dívidas (" + oc("Irving Fisher") + ", deflação de dívidas) e pode deprimir a demanda.",
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " O item pega o nome de um mecanismo deflacionário "
                       "e o descreve como inflacionário (salários ↑ → preços ↑), e ainda inverte a conclusão: "
                       "Pigou serviu para negar o equilíbrio com desemprego. Pista: efeito Pigou = efeito "
                       "<b>riqueza real</b>; sem M/P, não é Pigou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O efeito Pigou implica que a queda do nível de preços, ao elevar o valor real dos saldos "
            "monetários, estimula o consumo e a demanda agregada.”</i> → CERTO",
            "<i>“O efeito Pigou atua pela redução da taxa de juros decorrente do aumento dos saldos reais.”</i> → "
            "ERRADO (troca de conceito: esse é o efeito Keynes)",
        ])],
        "reescrita": ("O efeito Pigou implica que a " + hl("queda dos salários nominais e dos preços elevará o valor "
                      "real dos saldos monetários e o consumo") + ", de modo que o desemprego " + hl("tenderá a "
                      "ser eliminado, com retorno ao pleno emprego") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Efeito Pigou = efeito riqueza real: queda de preços eleva M/P, o consumo e a DA, "
                             "restaurando o pleno emprego; alta de salários nominais é choque de custos e, com M "
                             "fixo, reduz os saldos reais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 128", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quadro comparativo incorporado ao 📖)"}],
        "alertas": [ANTT_ANO],
    },
    # ------------------------------------------------------------------ E3-L00138
    {
        "id": "ECO-E3-L00138-1", "fonte_ref": "E3-L00138", "destino": "28", "subtema": H2["oa"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("A função oferta agregada da economia é negativamente inclinada no plano (Y, P), em que Y "
                      "representa a renda e P, o nível geral de preços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A função oferta agregada da economia é ") + vm("negativamente") + az(" inclinada no plano "
                    "(Y, P), em que Y representa a renda e P, o nível geral de preços.")),
        "poucas": ("No plano (Y, P), a " + azb("OA") + " é horizontal (preços rígidos), " + azb("positivamente "
                   "inclinada") + " (curto prazo) ou vertical (longo prazo). Negativamente inclinada é a "
                   + azb("DA") + "."),
        "destrinchando": [
            "A inclinação da OA depende do horizonte e da rigidez de preços: " + vd("horizontal") + " no caso "
            "keynesiano extremo de preços fixos; " + vd("positivamente inclinada") + " no curto prazo com "
            "salários ou preços rígidos ou percepções equivocadas (Y = Yₙ + α(P − Pᵉ)); " + vd("vertical")
            + " no longo prazo, em Yₙ, quando todos os preços se ajustaram.",
            "Por que positiva no curto prazo: com salários nominais fixados em contrato, P maior reduz W/P e "
            "torna lucrativo contratar e produzir mais; com custos de cardápio, firmas que não remarcam vendem "
            "mais quando a demanda sobe.",
            "Quem é negativamente inclinada no mesmo plano é a " + azb("demanda agregada") + ": P menor eleva "
            "M/P (efeito Keynes, via juros; efeito Pigou, via riqueza) e deprecia o câmbio real (efeito "
            "Mundell-Fleming).",
            vm("Regra-âncora: no plano (Y, P), DA desce; OA sobe (ou é horizontal/vertical) — nunca desce."),
        ],
        "grafico_verso": "ECO-E3-L00138-1-V1",
        "dissecando": (cz("[troca de conceito]") + " Troca a inclinação da DA pela da OA. Item de definição, mas "
                       "com um detalhe que confunde: o eixo Y vem primeiro no par (Y, P), e quem inverte os eixos "
                       "mentalmente pode se perder."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No curto prazo, com preços totalmente rígidos, a oferta agregada é horizontal.”</i> → CERTO",
            "<i>“No longo prazo, a oferta agregada é positivamente inclinada no plano (Y, P).”</i> → ERRADO (troca "
            "de prazo: é vertical)",
        ])],
        "reescrita": ("A função oferta agregada da economia é " + hl("positivamente") + " inclinada no plano (Y, P), "
                      "em que Y representa a renda e P, o nível geral de preços."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("OA é positivamente inclinada no curto prazo e vertical no longo prazo; nunca "
                             "negativamente inclinada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 132", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (curva de oferta de um bem, microeconomia)"},
                          {"ref": "IMAGEM 133", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00138-1-V1)"}],
        "alertas": [ANTT_ANO],
    },
    # ------------------------------------------------------------------ E1-0458
    {
        "id": "ECO-E1-0458-1", "fonte_ref": "E1-0458", "destino": "29", "subtema": H2["ex"],
        "tipo": "C/E", "banca": "Daniel – Economia CACD (Telegram)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à hipótese de expectativas racionais.",
        "rotulo_item": "Item",
        "assertiva": ("As expectativas racionais se baseiam na hipótese de que os agentes econômicos antecipam de "
                      "forma racional as atitudes e políticas futuras do governo, reagindo no presente em "
                      "consonância com as expectativas formadas e anulando em algum grau a efetividade dessas "
                      "políticas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As expectativas racionais se baseiam na hipótese de que os agentes econômicos antecipam de "
                      "forma racional as atitudes e políticas futuras do governo, reagindo no presente em "
                      "consonância com as expectativas formadas e anulando <u>em algum grau</u> a efetividade "
                      "dessas políticas."),
        "poucas": ("Com " + azb("expectativas racionais") + ", os agentes usam toda a informação disponível — "
                   "inclusive a regra de política do governo —, antecipam seus efeitos e reagem já; a parte "
                   "prevista da política perde efeito real."),
        "destrinchando": [
            "A hipótese foi formulada por " + oc("John Muth") + " (1961) e levada à macroeconomia nos anos 1970 "
            "por " + oc("Robert Lucas") + ", " + oc("Thomas Sargent") + " e " + oc("Neil Wallace") + ": a "
            "expectativa subjetiva dos agentes coincide, em média, com a previsão do modelo econômico relevante; "
            "erros existem, mas não são sistemáticos.",
            "Diferença para as " + azb("expectativas adaptativas") + " (" + oc("Friedman") + "): estas olham "
            "para trás (inflação passada) e corrigem o erro aos poucos; as racionais olham para a frente e "
            "incorporam anúncios, regras e credibilidade.",
            "Consequência: uma política <b>sistemática e antecipada</b> é incorporada nos contratos (salários, "
            "preços) antes de produzir efeito real — é a " + azb("proposição de ineficácia da política") + " de "
            "Sargent e Wallace (1975). Só a surpresa move o produto, e apenas temporariamente.",
            "Também daí a " + azb("crítica de Lucas") + " (1976): como os agentes reagem às regras, os parâmetros "
            "de modelos estimados sob uma política mudam quando a política muda, e não servem para prever seus "
            "efeitos.",
            "O lado positivo: com governo crível, a desinflação pode custar pouco desemprego, porque as "
            "expectativas caem junto com o anúncio.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O “em algum grau” é a salvaguarda: o "
                       "item não diz que a política fica sempre totalmente ineficaz (o que exigiria preços "
                       "flexíveis e política antecipada). Item de definição com conclusão suavizada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…anulando completamente, em qualquer circunstância, a efetividade dessas políticas.”</i> → ERRADO "
            "(modulador absoluto: surpresas ainda têm efeito)",
            "<i>“As expectativas racionais se baseiam na observação dos erros de previsão passados, corrigidos "
            "gradualmente.”</i> → ERRADO (troca de conceito: isso é expectativa adaptativa)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["em algum grau"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito e um anexo em PDF sobre expectativas racionais.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "anexo do verso (sem nome)", "tipo_fonte": "IMAGEM", "lado": "verso",
                           "acao": "cortada (anexo não preservado)"}],
        "alertas": ["texto_corrigido: “os agente econômicos” → “os agentes econômicos” (erro de digitação)"],
    },
    # ------------------------------------------------------------------ E1-0486
    {
        "id": "ECO-E1-0486-1", "fonte_ref": "E1-0486", "destino": "29", "subtema": H2["ex"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo à neutralidade da moeda e à curva de Phillips.",
        "rotulo_item": "Item",
        "assertiva": ("A hipótese de neutralidade da moeda é compatível com uma curva de Phillips vertical, em que "
                      "tanto expansões fiscais quanto monetárias são incapazes de afetar o nível de produto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A hipótese de neutralidade da moeda é compatível com uma curva de Phillips <u>vertical</u>, "
                      "em que tanto expansões <u>fiscais</u> quanto monetárias são incapazes de afetar o nível de "
                      "produto."),
        "poucas": ("Curva de Phillips " + azb("vertical") + " = desemprego (e produto) fixado na taxa natural, "
                   "qualquer que seja a inflação. Aí nenhuma política de <b>demanda</b> — fiscal ou monetária — "
                   "muda o nível de produto; só muda a inflação. É exatamente o mundo da " + azb("moeda neutra")
                   + "."),
        "destrinchando": [
            azb("Neutralidade da moeda") + ": M só afeta variáveis nominais. Na curva de Phillips, isso significa "
            "que mais inflação não compra menos desemprego — a curva é " + vd("vertical em uₙ") + " (longo prazo "
            "de " + oc("Friedman") + " e " + oc("Phelps") + "; até o curto prazo, com expectativas racionais e "
            "política antecipada).",
            "A curva de Phillips vertical é o espelho da " + azb("OA vertical") + " (lei de Okun liga desemprego "
            "e produto): política fiscal e monetária deslocam a DA; com OA vertical, só P responde.",
            "Por que a fiscal também é incapaz? Com produto fixo em Yₙ, mais gasto público só muda a "
            + azb("composição") + " do produto — " + azb("crowding out") + " total de consumo, investimento ou "
            "exportações líquidas —, não o nível.",
            "Implicação prática: financiar gastos com emissão gera " + vd("inflação") + ", não emprego; o "
            "produto de longo prazo depende de fatores reais (capital, trabalho, tecnologia, instituições).",
            vm("Regra-âncora: Phillips vertical ⇔ OA vertical ⇔ moeda neutra: política de demanda só mexe em "
               "preços."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A palavra que derruba candidatos é “fiscais”: "
                       "neutralidade é conceito monetário, e parece extrapolação estendê-lo à política fiscal. Mas "
                       "a premissa é a curva vertical, que vale para qualquer choque de demanda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com uma curva de Phillips vertical, a política fiscal expansionista eleva o produto, embora a "
            "monetária seja neutra.”</i> → ERRADO (curva vertical vale para toda política de demanda)",
            "<i>“A hipótese de neutralidade da moeda é compatível com uma curva de Phillips negativamente "
            "inclinada e estável.”</i> → ERRADO (contradição: haveria trade-off explorável)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["tanto … quanto"], "dificuldade": 2,
        "comentario_fonte": ("Neutralidade monetária: incentivos monetários não afetam a produtividade dos fatores; "
                             "financiar gastos por emissão gera aceleração inflacionária, não queda do "
                             "desemprego."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CACD/2017 (CEBRASPE) — a fonte marca só o ano; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0491
    {
        "id": "ECO-E1-0491-1", "fonte_ref": "E1-0491", "destino": "29", "subtema": H2["ph"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo à curva de Phillips.",
        "rotulo_item": "Item",
        "assertiva": ("A curva de Phillips descreve a relação direta entre maior taxa de desemprego e maior taxa de "
                      "variação dos salários nominais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva de Phillips descreve a relação ") + vm("direta") + az(" entre maior taxa de "
                    "desemprego e ") + vm("maior") + az(" taxa de variação dos salários nominais.")),
        "poucas": ("A curva original de " + oc("Phillips") + " (1958) é " + azb("inversa") + ": desemprego alto "
                   "↔ salários nominais crescendo devagar; desemprego baixo ↔ salários acelerando."),
        "destrinchando": [
            oc("A. W. Phillips") + " (1958) estudou dados do " + vd("Reino Unido, 1861–1957") + " e encontrou "
            "uma relação empírica negativa e convexa entre a " + azb("taxa de desemprego") + " e a "
            + azb("taxa de variação dos salários nominais") + ".",
            "Intuição: com o mercado de trabalho apertado (pouco desemprego), os trabalhadores têm mais "
            + azb("poder de barganha") + " e as firmas disputam mão de obra, então os salários sobem rápido; com "
            "muito desemprego, os reajustes desaceleram.",
            oc("Samuelson") + " e " + oc("Solow") + " (1960) trocaram salários por " + azb("inflação de preços")
            + " (preço = salário + markup) e apresentaram a curva como um “menu” de política: menos desemprego ao "
            "custo de mais inflação.",
            "Depois, " + oc("Friedman") + " e " + oc("Phelps") + " mostraram que o trade-off só vale no curto "
            "prazo: a curva se desloca com as expectativas e é vertical no longo prazo.",
            vm("Regra-âncora: Phillips original = relação INVERSA entre desemprego e inflação (salarial)."),
        ],
        "dissecando": (cz("[inversão]") + " Troca “inversa” por “direta” e ajusta o par (“maior … maior”) para "
                       "parecer coerente. A frase lida rápido soa técnica; o teste é perguntar se desemprego alto "
                       "dá aos trabalhadores força para pedir aumento — não dá."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de Phillips original relacionava a taxa de desemprego à taxa de inflação de preços ao "
            "consumidor.”</i> → ERRADO (detalhe: a original usava salários nominais)",
            "<i>“A curva de Phillips descreve a relação inversa entre a taxa de desemprego e a taxa de variação "
            "dos salários nominais.”</i> → CERTO",
        ])],
        "reescrita": ("A curva de Phillips descreve a relação " + hl("inversa") + " entre maior taxa de desemprego e "
                      + hl("menor") + " taxa de variação dos salários nominais."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Relação inversa: quanto menor o desemprego, maior o poder de barganha e mais rápido o "
                             "crescimento dos salários nominais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CACD/2016 (CEBRASPE) — a fonte marca só o ano; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0498
    {
        "id": "ECO-E1-0498-1", "fonte_ref": "E1-0498", "destino": "29", "subtema": H2["ex"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo às escolas monetarista e novo-clássica.",
        "rotulo_item": "Item",
        "assertiva": ("Lucas, Sargent e Wallace, ao proporem um modelo fundamentado em expectativas racionais que "
                      "concluía pela ineficácia da política monetária, baseavam-se nas mesmas premissas da visão "
                      "monetarista de Milton Friedman."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Lucas, Sargent e Wallace, ao proporem um modelo fundamentado em expectativas racionais que "
                       "concluía pela ineficácia da política monetária, baseavam-se ") + vm("nas mesmas premissas")
                    + az(" da visão monetarista de Milton Friedman.")),
        "poucas": (oc("Friedman") + " supõe " + azb("expectativas adaptativas") + " (política monetária eficaz no "
                   "curto prazo); os " + azb("novos-clássicos") + " supõem " + azb("expectativas racionais") + " e "
                   "mercados sempre em equilíbrio (ineficaz até no curto prazo, se antecipada). Conclusões "
                   "parecidas, premissas diferentes."),
        "destrinchando": [
            azb("Monetarismo") + " (" + oc("Milton Friedman") + ", “The Role of Monetary Policy”, 1968): "
            "expectativas adaptativas — os agentes projetam a inflação pela inflação passada e corrigem o erro "
            "aos poucos. Uma expansão monetária engana os trabalhadores temporariamente: o desemprego cai "
            "abaixo da taxa natural no curto prazo e volta a ela no longo. Recomendação: " + azb("regra de "
            "crescimento constante da moeda") + ", porque a política discricionária age com defasagens longas e "
            "variáveis.",
            azb("Novos-clássicos") + " (" + oc("Lucas") + ", " + oc("Sargent") + ", " + oc("Wallace") + ", anos "
            "1970): expectativas racionais (" + oc("Muth") + ", 1961) + " + azb("equilíbrio contínuo dos "
            "mercados") + " + informação imperfeita sobre preços. A política sistemática é antecipada e neutra "
            "<b>já no curto prazo</b> — " + azb("proposição de ineficácia") + " (Sargent e Wallace, 1975).",
            "O ponto comum é o ceticismo quanto ao ativismo e a taxa natural de desemprego; a diferença está em "
            "<b>como</b> as expectativas se formam — e, com ela, no custo da desinflação: gradual e custoso para "
            "Friedman; potencialmente rápido e barato, se crível, para os novos-clássicos.",
            "Tabela mental: Phillips/keynesianos (expectativas estáticas) → Friedman-Phelps (adaptativas, "
            "trade-off só no curto prazo) → Lucas (racionais, trade-off só com surpresa) → novos-keynesianos "
            "(racionais + rigidezes, política antecipada volta a ter efeito no curto prazo).",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " As escolas concordam na conclusão "
                       "(ceticismo com a política monetária), e o item usa essa semelhança para afirmar premissas "
                       "iguais. Pista: o próprio item diz que Lucas se baseia em expectativas racionais — que "
                       "não são as de Friedman."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Monetaristas e novos-clássicos compartilham a hipótese de taxa natural de desemprego, mas "
            "divergem quanto à formação das expectativas.”</i> → CERTO",
            "<i>“Para Friedman, a política monetária é ineficaz inclusive no curto prazo.”</i> → ERRADO (troca de "
            "ator: essa é a conclusão novo-clássica)",
        ])],
        "reescrita": ("Lucas, Sargent e Wallace, ao proporem um modelo fundamentado em expectativas racionais que "
                      "concluía pela ineficácia da política monetária, baseavam-se " + hl("em premissas diferentes "
                      "daquelas") + " da visão monetarista de Milton Friedman."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["mesmas"], "dificuldade": 2,
        "comentario_fonte": ("Friedman usa expectativas adaptativas e admite eficácia de curto prazo; Lucas usa "
                             "expectativas racionais e nega eficácia mesmo no curto prazo; conclusões parecidas, "
                             "premissas distintas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: prova de 2022, possivelmente CACD — a fonte marca só o ano; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0499
    {
        "id": "ECO-E1-0499-1", "fonte_ref": "E1-0499", "destino": "29", "subtema": H2["ex"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à visão novo-clássica da política monetária.",
        "rotulo_item": "Item",
        "assertiva": ("Na visão de política monetária proposta por Lucas, a taxa corrente de desemprego é igual à "
                      "taxa natural quando a taxa corrente de inflação equivale às expectativas de inflação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na visão de política monetária proposta por Lucas, a taxa corrente de desemprego é "
                      "<u>igual</u> à taxa natural <u>quando</u> a taxa corrente de inflação equivale às "
                      "expectativas de inflação."),
        "poucas": ("Na " + azb("curva de oferta de Lucas") + ", o desemprego só se afasta do natural quando há "
                   + azb("surpresa") + " (π ≠ πᵉ). Sem surpresa, " + vd("u = uₙ") + "."),
        "destrinchando": [
            "Forma da curva: " + vd("Y = Yₙ + α(P − Pᵉ)") + " ou, em termos de Phillips, " + vd("u = uₙ − β(π − "
            "πᵉ)") + ". Se π = πᵉ, o termo de surpresa zera e u = uₙ — é exatamente o item.",
            "Mecanismo (" + azb("modelo das ilhas") + ", " + oc("Lucas") + ", 1972-1973): cada produtor vê o preço "
            "do seu bem, mas não o nível geral. Diante de uma alta, precisa decidir se é aumento do seu "
            + azb("preço relativo") + " (vale produzir mais) ou inflação geral (não vale) — é o "
            + azb("problema de extração de sinal") + ". Só quando a alta geral não foi prevista ele se engana e "
            "expande a produção.",
            "Com " + azb("expectativas racionais") + ", π e πᵉ coincidem em média; os desvios são aleatórios. "
            "Logo, o desemprego oscila em torno da taxa natural, e a política monetária sistemática só gera "
            "inflação.",
            "A mesma equação vale em Friedman-Phelps; a diferença está em como πᵉ se forma (adaptativa × "
            "racional) — e, portanto, em quanto tempo o erro dura.",
            "Lucas recebeu o " + vd("Nobel de 1995") + " por desenvolver e aplicar a hipótese de expectativas "
            "racionais.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a condição de equilíbrio da curva de Lucas. O candidato "
                       "pode hesitar por achar que Lucas “nega” a taxa natural ou que a igualdade só valeria no "
                       "longo prazo; vale sempre que não há surpresa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a taxa corrente de desemprego fica abaixo da taxa natural quando a inflação corrente supera a "
            "esperada.”</i> → CERTO",
            "<i>“…a taxa corrente de desemprego é igual à taxa natural apenas no longo prazo, "
            "independentemente das expectativas.”</i> → ERRADO (restrição indevida: basta π = πᵉ)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["quando"], "dificuldade": 1,
        "comentario_fonte": ("Em Lucas, o desemprego só se desvia da taxa natural se os agentes forem "
                             "surpreendidos; com inflação igual à esperada, u = uₙ e a política monetária só gera "
                             "inflação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_E1("image (159).png") + FIG_E1("image (157).png"),
        "alertas": ["banca_provavel: prova de 2022, possivelmente CACD — a fonte marca só o ano; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0500
    {
        "id": "ECO-E1-0500-1", "fonte_ref": "E1-0500", "destino": "29", "subtema": H2["ex"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo à hipótese de expectativas racionais.",
        "rotulo_item": "Item",
        "assertiva": "Pela definição de expectativas racionais, agentes racionais não são capazes de cometer erros.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Pela definição de expectativas racionais, agentes racionais ") + vm("não são capazes de "
                    "cometer erros") + az(".")),
        "poucas": ("Expectativas racionais admitem erros; o que excluem são " + azb("erros sistemáticos")
                   + ". Em média a previsão acerta, e o erro é aleatório e imprevisível."),
        "destrinchando": [
            "Definição (" + oc("Muth") + ", 1961; " + oc("Lucas") + "): a expectativa subjetiva é igual à "
            "esperança matemática condicionada a toda a informação disponível: " + vd("πᵉ = E[π | Ω]") + ". "
            "Daí " + vd("π = πᵉ + ε") + ", com ε de média zero.",
            "O erro ε existe — choques imprevisíveis acontecem —, mas é " + azb("não viesado") + " (não erra "
            "sempre para o mesmo lado) e " + azb("não autocorrelacionado") + " (o erro de hoje não ajuda a prever "
            "o de amanhã). Se houvesse padrão no erro, um agente racional o usaria para corrigir a previsão.",
            "Contraste: nas " + azb("expectativas adaptativas") + ", com inflação acelerando, o agente erra "
            "<b>sempre para baixo</b> — erro sistemático, justamente o que a hipótese racional descarta.",
            "Versões: a <b>fraca</b> exige uso eficiente da informação disponível; a <b>forte</b> supõe que os "
            "agentes conhecem o modelo verdadeiro da economia. Nenhuma das duas supõe previsão perfeita "
            "(perfeita seria “previsão perfeita”, conceito diferente).",
            vm("Regra-âncora: racional ≠ infalível; racional = sem erro sistemático."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " Confunde expectativas racionais com "
                       "previsão perfeita. 🔥 Confusão clássica cobrada em provas: “racional” é sobre o uso da "
                       "informação, não sobre acertar sempre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela definição de expectativas racionais, os agentes não cometem erros sistemáticos de "
            "previsão.”</i> → CERTO",
            "<i>“Sob expectativas racionais, os erros de previsão são autocorrelacionados ao longo do "
            "tempo.”</i> → ERRADO (inversão: não são autocorrelacionados)",
        ])],
        "reescrita": ("Pela definição de expectativas racionais, agentes racionais " + hl("podem cometer erros, mas "
                      "não erros sistemáticos") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["não são capazes"], "dificuldade": 1,
        "comentario_fonte": ("Expectativas racionais não implicam ausência de erros, mas ausência de erros "
                             "sistemáticos; em média coincidem com os valores verdadeiros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: prova de 2022, possivelmente CACD — a fonte marca só o ano; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0506
    {
        "id": "ECO-E1-0506-1", "fonte_ref": "E1-0506", "destino": "29", "subtema": H2["ph"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à curva de Phillips.",
        "rotulo_item": "Item",
        "assertiva": ("A curva de Phillips apresenta o grau de sacrifício necessário, em termos de desemprego, para "
                      "que se controle a inflação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva de Phillips apresenta o <u>grau de sacrifício</u> necessário, em termos de "
                      "desemprego, para que se controle a inflação."),
        "poucas": ("Ao relacionar inversamente inflação e desemprego no curto prazo, a curva de Phillips mostra o "
                   "custo, em desemprego, de reduzir a inflação — a ideia da " + azb("taxa de sacrifício") + "."),
        "destrinchando": [
            "Na curva de curto prazo π = πᵉ − β(u − uₙ), reduzir π abaixo de πᵉ exige " + vd("u > uₙ") + ": "
            "desemprego acima do natural por algum tempo, até as expectativas caírem.",
            azb("Taxa de sacrifício") + " = perda acumulada de produto (em % do PIB) por ponto percentual de "
            "desinflação. " + oc("Mankiw") + " cita estimativas de cerca de " + vd("5% do PIB por ponto") + " "
            "para os EUA; a desinflação de " + oc("Volcker") + " (1979-1982) derrubou a inflação americana com "
            "desemprego próximo de 10%.",
            "Pela " + azb("lei de Okun") + ", o custo em produto se traduz em desemprego: cada ponto de "
            "desemprego acima do natural custa cerca de 2% do produto (ordem de grandeza clássica).",
            "O tamanho do sacrifício depende das expectativas: com " + azb("expectativas adaptativas") + ", é "
            "alto (desinflação lenta); com " + azb("expectativas racionais") + " e " + azb("credibilidade") + " "
            "(a “desinflação sem dor” de " + oc("Sargent") + "), pode ser pequeno. Daí o valor de bancos "
            "centrais críveis e de regimes de metas.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Descreve a leitura de política da curva (custo da "
                       "desinflação). Pode parecer imprecisa porque “grau de sacrifício” é medida derivada, mas a "
                       "ideia de que a curva mostra esse custo é a dos manuais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela curva de Phillips, a inflação pode ser reduzida sem nenhum custo em desemprego, "
            "independentemente das expectativas.”</i> → ERRADO (contradição: há sacrifício no curto prazo)",
            "<i>“Com expectativas racionais e política crível, a taxa de sacrifício tende a ser menor.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Relação inversa inflação × desemprego no curto prazo; o grau de sacrifício é a queda "
                             "do produto ou o aumento do desemprego necessário para reduzir a inflação."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0507
    {
        "id": "ECO-E1-0507-1", "fonte_ref": "E1-0507", "destino": "29", "subtema": H2["ex"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à curva de Phillips e às expectativas.",
        "rotulo_item": "Item",
        "assertiva": ("Na versão de Lucas, a curva de Phillips reflete que o efeito surpresa pode acarretar "
                      "consequências no produto apenas temporariamente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na versão de Lucas, a curva de Phillips reflete que o <u>efeito surpresa</u> pode acarretar "
                      "consequências no produto <u>apenas temporariamente</u>."),
        "poucas": ("Em " + oc("Lucas") + ", só a " + azb("surpresa") + " (π ≠ πᵉ) desvia o produto do natural, e "
                   "o desvio dura só até os agentes perceberem o erro e refazerem as expectativas."),
        "destrinchando": [
            "Curva de oferta de Lucas: " + vd("Y − Yₙ = α(P − Pᵉ)") + ". Política antecipada eleva P e Pᵉ "
            "juntos — sem efeito real. Política não antecipada eleva P acima de Pᵉ: produtores confundem a alta "
            "geral com alta do preço relativo e produzem mais.",
            "O efeito é " + azb("temporário") + ": assim que a informação sobre o nível geral de preços chega, "
            "Pᵉ se corrige, e o produto volta a Yₙ. Com expectativas racionais, ninguém é enganado de forma "
            "<b>sistemática</b>.",
            "Por isso a surpresa não serve como instrumento: o governo não consegue surpreender sempre, e "
            "tentar fazê-lo apenas eleva a inflação média e a variabilidade, reduzindo a inclinação da curva "
            "(produtores passam a atribuir altas de preço à inflação geral).",
            "Contraste: em " + oc("Friedman") + " (adaptativas), também há efeito temporário, mas a política "
            "sistemática funciona no curto prazo porque o erro de expectativa é previsível e dura mais.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O “apenas temporariamente” é verdadeiro "
                       "aqui — o efeito da surpresa não é permanente. O risco é ler “apenas” como restrição "
                       "indevida ou achar que Lucas nega qualquer efeito real."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na versão de Lucas, a política monetária antecipada afeta o produto apenas "
            "temporariamente.”</i> → ERRADO (troca de conceito: antecipada não afeta nem temporariamente)",
            "<i>“Na versão de Lucas, a surpresa monetária reduz permanentemente o desemprego.”</i> → ERRADO "
            "(dado alterado: o efeito é temporário)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "apenas"],
        "dificuldade": 1,
        "comentario_fonte": ("Na curva de Lucas, só choques inesperados de inflação têm impacto sobre o produto, e "
                             "apenas no curto prazo; no longo prazo, o produto volta ao natural."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0508
    {
        "id": "ECO-E1-0508-1", "fonte_ref": "E1-0508", "destino": "29", "subtema": H2["ph"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à curva de Phillips.",
        "rotulo_item": "Item",
        "assertiva": ("A “Curva de Phillips” oferece aos formuladores de políticas uma gama de possíveis resultados "
                      "econômicos: ao alterarem as políticas monetária e fiscal para influenciar a demanda "
                      "agregada, eles podem escolher qualquer ponto desta curva, que ilustra o trade-off de inflação "
                      "e desemprego no curto prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A “Curva de Phillips” oferece aos formuladores de políticas uma gama de possíveis resultados "
                      "econômicos: ao alterarem as políticas monetária e fiscal para influenciar a demanda "
                      "agregada, eles podem escolher <u>qualquer ponto</u> desta curva, que ilustra o trade-off de "
                      "inflação e desemprego <u>no curto prazo</u>."),
        "poucas": ("É a leitura de " + azb("menu de política") + " da curva de Phillips de curto prazo: mexendo na "
                   "DA, o governo escolhe a combinação de inflação e desemprego — " + vd("enquanto as "
                   "expectativas estiverem dadas") + "."),
        "destrinchando": [
            "A formulação é praticamente a de " + oc("Mankiw") + " (<i>Introdução à Economia</i>): a curva oferece "
            "um “menu” de resultados; políticas de demanda movem a economia ao longo da curva — mais DA, menos "
            "desemprego e mais inflação; menos DA, o inverso.",
            "A ideia vem de " + oc("Samuelson") + " e " + oc("Solow") + " (1960), que adaptaram a relação "
            "salarial de " + oc("Phillips") + " (1958) para inflação de preços e a apresentaram como opção de "
            "política.",
            "O limite está no “curto prazo”: a curva é desenhada para uma " + azb("inflação esperada dada") + ". "
            "Se o governo escolhe um ponto de desemprego abaixo do natural, a inflação efetiva supera a esperada, "
            "as expectativas sobem e a curva se desloca para cima (" + oc("Friedman") + "-" + oc("Phelps")
            + "). No longo prazo, não há menu: a curva é vertical.",
            "A estagflação dos anos 1970 (inflação e desemprego altos ao mesmo tempo) mostrou que o menu não era "
            "estável.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O “qualquer ponto” parece generalização "
                       "indevida, mas está amarrado a “desta curva” e a “no curto prazo”: dado o πᵉ, a política "
                       "de demanda escolhe pontos ao longo dela. Errado seria estender o menu ao longo prazo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…eles podem escolher qualquer ponto desta curva, que ilustra o trade-off permanente de inflação "
            "e desemprego.”</i> → ERRADO (generalização: o trade-off é só de curto prazo)",
            "<i>“Choques de oferta deslocam a curva de Phillips de curto prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["qualquer", "no curto prazo"],
        "dificuldade": 2,
        "comentario_fonte": ("No curto prazo há trade-off entre inflação e desemprego: políticas que reduzem o "
                             "desemprego podem aumentar a inflação, e vice-versa."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0509
    {
        "id": "ECO-E1-0509-1", "fonte_ref": "E1-0509", "destino": "29", "subtema": H2["ph"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à curva de Phillips.",
        "rotulo_item": "Item",
        "assertiva": "A Curva de Phillips ilustra a relação inversa entre desemprego e inflação.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Curva de Phillips ilustra a relação <u>inversa</u> entre desemprego e inflação."),
        "poucas": ("Na forma tradicional, a curva de Phillips é " + azb("negativamente inclinada") + ": menos "
                   "desemprego vem acompanhado de mais inflação, e vice-versa."),
        "destrinchando": [
            "Origem: " + oc("Phillips") + " (1958) mostrou a relação inversa entre desemprego e "
            + azb("inflação salarial") + " no Reino Unido; " + oc("Samuelson") + " e " + oc("Solow") + " (1960) "
            "a reformularam com " + azb("inflação de preços") + ".",
            "Mecanismo: DA mais alta → produção e emprego maiores → mercado de trabalho apertado → salários e "
            "custos sobem → preços sobem. No OA-DA, isso é o movimento ao longo da OACP: P e Y sobem juntos; "
            "pela lei de Okun, Y maior significa u menor.",
            "Versão aceleracionista (" + oc("Friedman") + "-" + oc("Phelps") + "): " + vd("π = πᵉ − β(u − uₙ)")
            + ". A relação inversa vale para cada πᵉ dado (curto prazo); no longo prazo, π = πᵉ e u = uₙ — a "
            "curva é vertical.",
            "A curva também se desloca com " + azb("choques de oferta") + " (petróleo nos anos 1970): inflação "
            "e desemprego podem subir juntos sem contradizer a relação de curto prazo.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição pura. A dúvida plantada é se o candidato vai exigir "
                       "“no curto prazo” para marcar CERTO. Sem modulador em contrário, a banca aceita a "
                       "descrição da curva tradicional."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Curva de Phillips ilustra a relação inversa entre desemprego e inflação tanto no curto quanto "
            "no longo prazo.”</i> → ERRADO (generalização: no longo prazo é vertical)",
            "<i>“A Curva de Phillips ilustra a relação direta entre desemprego e inflação.”</i> → ERRADO "
            "(inversão)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Curva tradicional: relação inversa entre inflação e desemprego no curto prazo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("Untitled (97).jpeg"),
        "alertas": [],
    },
]
