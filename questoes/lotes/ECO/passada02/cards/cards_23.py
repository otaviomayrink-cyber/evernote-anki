"""Cards do lote de redação 23 — ECO, passada 02 (nota 47: funções do Estado, política fiscal,
equivalência ricardiana e estrutura tributária)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "fun": "🏛️ Funções do Estado",
    "trib": "💸 Tributação: princípios e incidência",
    "fisc": "📊 Política fiscal e multiplicadores",
    "ric": "🔮 Equivalência ricardiana",
}

CMD_FUN = "Acerca das funções econômicas do governo, julgue o item a seguir."

CMD_DES = "Acerca do papel do Estado no desenvolvimento econômico, julgue o item a seguir."

CMD_BOZ_A = ("Considerando as abordagens econômicas relativas à intervenção do governo na economia, especialmente no "
             "contexto da política fiscal e das teorias keynesiana e neokeynesiana, julgue o item.")

CMD_BOZ_B = ("Julgue o item a seguir como certo ou errado, com base nos conceitos de política econômica e de "
             "intervenção governamental no contexto keynesiano e clássico.")

CMD_ARM = "Julgue o item a seguir, relativo à equivalência ricardiana."

CMD_NAB_MACRO = "Em relação aos conceitos macroeconômicos, julgue (C ou E) o item seguinte."

CMD_NAB_24 = "Em relação às teorias de consumo, investimento e dívida pública, julgue (C ou E) o item a seguir."

CMD_NAB_23 = "Em relação às políticas monetária e fiscal, julgue (C ou E) o item seguinte."

CMD_NAB_ER = "A respeito do conceito de equivalência ricardiana e das teorias do consumo, julgue o item a seguir."

CMD_RT_PAND = ("O Brasil fez uso da política fiscal durante a pandemia, com o governo elevando gastos com saúde e "
               "educação, reduzindo ou adiando o pagamento de impostos, bem como pagando auxílio às famílias mais "
               "pobres. A esse respeito, julgue o item a seguir.")

CMD_RT_DIV = "A respeito da política fiscal e da dívida pública, julgue o item a seguir."

CMD_TJPA_FUN = "No que diz respeito às funções do Estado em um sistema econômico, julgue o item seguinte."

CMD_TJPA_POL = ("Julgue o item que se segue, a respeito das políticas fiscal e monetária, do papel da dívida pública "
                "como fonte de financiamento e da função reguladora do Estado na economia.")

CMD_TJPA_TRIB = "Julgue o item seguinte, relativo à estrutura tributária brasileira."

FIG_E1 = lambda *refs: [{"ref": r, "tipo_fonte": "GRÁFICO", "lado": "verso",
                         "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"} for r in refs]

MUSGRAVE = ("Na tripartição clássica de " + oc("Richard Musgrave") + " (<i>The Theory of Public Finance</i>, 1959), "
            "o governo tem três funções econômicas: " + azb("alocativa") + " (prover bens e serviços que o mercado "
            "não oferece ou oferece mal e corrigir falhas de mercado), " + azb("distributiva") + " (ajustar a "
            "repartição de renda e riqueza resultante do mercado) e " + azb("estabilizadora") + " (usar as "
            "políticas macroeconômicas para buscar pleno emprego, estabilidade de preços e crescimento "
            "equilibrado).")

CARDS = [
    # ------------------------------------------------------------------ E1-0621
    {
        "id": "ECO-E1-0621-1", "fonte_ref": "E1-0621", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUN,
        "rotulo_item": "Item",
        "assertiva": ("Dentre as funções econômicas do governo, a função estabilizadora faz uso das políticas fiscal "
                      "e monetária para garantir o bom uso qualitativo dos recursos nacionais e a mitigação de "
                      "externalidades."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Dentre as funções econômicas do governo, a função estabilizadora faz uso das políticas "
                       "fiscal e monetária para garantir ") + vm("o bom uso qualitativo dos recursos nacionais e a "
                                                                 "mitigação de externalidades") + az(".")),
        "poucas": ("Uso qualitativo dos recursos e correção de " + azb("externalidades") + " são tarefas da função "
                   + azb("alocativa") + "; a " + azb("estabilizadora") + " cuida do nível agregado: emprego, "
                   "preços e crescimento."),
        "destrinchando": [
            MUSGRAVE,
            "A diferença está na pergunta que cada função responde. A alocativa pergunta <b>o quê</b> e "
            "<b>como</b> se produz (composição do produto: quanto de defesa, de iluminação pública, de poluição "
            "tolerada). A estabilizadora pergunta <b>quanto</b> se produz no agregado (hiato do produto, "
            "desemprego, inflação).",
            azb("Externalidades") + " são falhas de mercado típicas da alocativa: o governo as corrige com "
            "tributo pigouviano, subsídio, regulação ou criação de mercado de licenças. Não é preciso mexer em "
            "juros nem no resultado fiscal agregado para isso.",
            "A estabilizadora, sim, usa os instrumentos macro — " + azb("política fiscal") + " (gastos, "
            "tributos, estabilizadores automáticos) e " + azb("política monetária") + " (juros, liquidez) — "
            "para suavizar o ciclo.",
            vm("Regra-âncora: composição (o quê) → alocativa; nível (quanto) → estabilizadora; repartição "
               "(para quem) → distributiva."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item acerta os instrumentos da estabilizadora (fiscal e "
                       "monetária) e cola neles o objetivo da alocativa. Pista: “uso qualitativo” e "
                       "“externalidades” são vocabulário de eficiência alocativa, não de ciclo econômico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função alocativa busca corrigir externalidades e garantir a provisão de bens públicos.”</i> → "
            "CERTO",
            "<i>“A função estabilizadora visa à redução das desigualdades de renda entre regiões.”</i> → ERRADO "
            "(troca de conceito: é a distributiva)",
        ])],
        "reescrita": ("Dentre as funções econômicas do governo, a função estabilizadora faz uso das políticas fiscal "
                      "e monetária para garantir " + hl("o pleno emprego, a estabilidade de preços e o crescimento "
                                                        "equilibrado") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A estabilizadora corrige flutuações macroeconômicas; externalidades são da função "
                            "alocativa.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0622
    {
        "id": "ECO-E1-0622-1", "fonte_ref": "E1-0622", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUN,
        "rotulo_item": "Item",
        "assertiva": ("A função alocativa prevê ajustamentos na alocação de recursos com vistas à maior eficiência na "
                      "utilização dos recursos disponíveis na economia e refere-se à possibilidade de economias "
                      "externas ou necessidades coletivas, como infraestrutura econômica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função alocativa prevê ajustamentos na alocação de recursos com vistas à <u>maior "
                      "eficiência</u> na utilização dos recursos disponíveis na economia e refere-se à possibilidade "
                      "de <u>economias externas</u> ou <u>necessidades coletivas</u>, como infraestrutura econômica."),
        "poucas": ("É a definição de manual: a " + azb("função alocativa") + " busca eficiência onde o mercado falha "
                   "— " + azb("externalidades") + ", bens públicos e necessidades coletivas como a "
                   "infraestrutura."),
        "destrinchando": [
            MUSGRAVE,
            "A alocativa entra quando o sistema de preços não leva à alocação eficiente: " + azb("bens públicos")
            + " (não rivais e não excludentes, sujeitos ao carona), " + azb("externalidades") + " (custos ou "
            "benefícios que não passam pelo preço), " + azb("monopólios naturais") + " e mercados incompletos.",
            "“Economias externas” é o nome antigo das externalidades positivas: um investimento cujo benefício "
            "transborda para terceiros. Infraestrutura econômica (estradas, saneamento, energia) é o exemplo "
            "clássico — alto custo fixo, longo prazo de maturação e benefícios difusos, que o investidor privado "
            "não captura por inteiro.",
            "Instrumentos: provisão pública direta, concessões e PPPs, tributos e subsídios corretivos, "
            "regulação. Provisão pública não exige produção estatal: o governo pode financiar e contratar.",
        ],
        "dissecando": (cz("[literalidade]") + " Paráfrase próxima dos manuais brasileiros de finanças públicas. "
                       "O risco está em achar que “infraestrutura” seria função de desenvolvimento ou "
                       "estabilizadora; não é — é composição do produto, logo alocativa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função alocativa refere-se à correção das flutuações de curto prazo do nível de "
            "emprego.”</i> → ERRADO (troca de conceito: é a estabilizadora)",
            "<i>“A função alocativa restringe-se à provisão de bens públicos puros.”</i> → ERRADO (restrição "
            "indevida: inclui externalidades, monopólios naturais e bens meritórios)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A alocativa corrige falhas de mercado (bens públicos, externalidades, monopólios "
                            "naturais), especialmente em infraestrutura e bens coletivos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("Untitled (107).jpeg"),
        "alertas": ["quase_duplicata: ECO-E1-0629-1 (mesma definição de função alocativa, outra redação)"],
    },
    # ------------------------------------------------------------------ E1-0623
    {
        "id": "ECO-E1-0623-1", "fonte_ref": "E1-0623", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUN,
        "rotulo_item": "Item",
        "assertiva": ("A função distributiva busca tornar compatíveis entre si a distribuição das remunerações dos "
                      "fatores resultantes da atividade econômica via mercado e aquela que atende aos princípios de "
                      "justiça social."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função distributiva busca tornar compatíveis entre si a <u>distribuição das remunerações "
                      "dos fatores</u> resultantes da atividade econômica via mercado e aquela que atende aos "
                      "<u>princípios de justiça social</u>."),
        "poucas": ("O mercado remunera os fatores pela produtividade e pela dotação inicial; a " + azb("função "
                   "distributiva") + " aproxima essa repartição daquela que a sociedade considera justa."),
        "destrinchando": [
            MUSGRAVE,
            "Ponto de partida: a " + azb("distribuição funcional") + " da renda (salários, lucros, juros, "
            "aluguéis) resulta da dotação de fatores e dos preços de mercado. Mesmo um mercado eficiente pode "
            "gerar uma repartição socialmente inaceitável — eficiência de Pareto não diz nada sobre equidade.",
            "Instrumentos: " + azb("tributação progressiva") + " (renda, herança, patrimônio), "
            + azb("transferências") + " (aposentadorias, programas como o " + rx("Bolsa Família") + "), "
            "gasto público dirigido aos mais pobres (saúde e educação gratuitas) e subsídios a bens de consumo "
            "popular.",
            "A distributiva é a mais normativa das três: o que é “justo” depende de juízo de valor (utilitarismo, "
            + oc("Rawls") + ", igualdade de oportunidades). Por isso os manuais falam em “princípios de justiça "
            "social”, sem fixar um critério único.",
            "Tensão clássica: redistribuir tem custo de eficiência (impostos distorcem incentivos) — o "
            "“balde furado” de " + oc("Arthur Okun") + " (<i>Equality and Efficiency: The Big Tradeoff</i>, 1975).",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição de " + oc("Musgrave") + " na versão dos "
                       "manuais brasileiros. A redação rebuscada (“tornar compatíveis entre si”) assusta, mas não "
                       "há modulador nem troca de função."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função distributiva busca eliminar as diferenças de remuneração entre os fatores de "
            "produção.”</i> → ERRADO (modulador absoluto: busca ajustar, não igualar)",
            "<i>“A tributação progressiva da renda é instrumento típico da função distributiva.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A distributiva corrige desigualdades de renda e riqueza geradas pelo mercado, "
                            "promovendo equidade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("Untitled (112).jpeg", "Untitled (106).jpeg"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0624
    {
        "id": "ECO-E1-0624-1", "fonte_ref": "E1-0624", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUN,
        "rotulo_item": "Item",
        "assertiva": ("A função competitiva do governo decorre diretamente da presença de bens comuns, os quais são "
                      "oferecidos simultaneamente pelo Estado e pelo setor privado, como é o caso da educação básica "
                      "e do sistema de saúde."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A ") + vm("função competitiva") + az(" do governo ") + vm("decorre diretamente da presença "
                                                                               "de bens comuns")
                    + az(", os quais são oferecidos simultaneamente pelo Estado e pelo setor privado, como é o caso "
                         "da educação básica e do sistema de saúde.")),
        "poucas": ("Não existe “função competitiva” na tripartição de " + oc("Musgrave") + ". Educação e saúde, "
                   "ofertadas pelo Estado e pelo mercado, são " + azb("bens meritórios") + ", tratados na função "
                   + azb("alocativa") + " — e não “bens comuns”."),
        "destrinchando": [
            MUSGRAVE,
            azb("Bens meritórios") + " (ou semipúblicos): são rivais e excludentes — o mercado consegue "
            "ofertá-los e cobra por eles —, mas a sociedade julga que seu consumo deve ser maior do que o que "
            "resultaria da escolha individual, por causa de externalidades positivas e de informação imperfeita. "
            "Daí a oferta pública gratuita ao lado da privada (escolas e hospitais particulares).",
            azb("Bens comuns") + " (recursos de uso comum) são outra coisa: " + vd("rivais e não excludentes")
            + " — peixes no oceano, pastos abertos, aquíferos. O problema típico é a superexploração, a "
            "“tragédia dos comuns” de " + oc("Garrett Hardin") + " (1968).",
            "Matriz de classificação: rival + excludente = privado; não rival + não excludente = público; rival + "
            "não excludente = comum; não rival + excludente = de clube (TV a cabo, pedágio sem congestionamento).",
            vm("Regra-âncora: educação e saúde públicas = bens meritórios, função alocativa."),
        ],
        "dissecando": (cz("[troca de conceito · outro: função inexistente]") + " O item inventa uma quarta "
                       "função e a amarra a uma classificação de bens trocada (comum × meritório). A parte "
                       "descritiva — oferta simultânea por Estado e mercado — é verdadeira e dá a falsa sensação "
                       "de acerto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A oferta pública de educação básica, ao lado da privada, justifica-se pelo caráter meritório "
            "desse bem.”</i> → CERTO",
            "<i>“Educação básica é bem público puro, pois é não rival e não excludente.”</i> → ERRADO (troca de "
            "conceito: é excludente e, em larga medida, rival)",
        ])],
        "reescrita": ("A " + hl("função alocativa") + " do governo " + hl("abrange a oferta de bens meritórios")
                      + ", os quais são oferecidos simultaneamente pelo Estado e pelo setor privado, como é o caso da "
                      "educação básica e do sistema de saúde."),
        "tipo_erro": ["TROCA_CONCEITO", "OUTRO"], "moduladores": ["diretamente"], "dificuldade": 2,
        "comentario_fonte": "Não existe função competitiva entre as clássicas; educação e saúde são bens "
                            "meritórios, não bens comuns.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0625
    {
        "id": "ECO-E1-0625-1", "fonte_ref": "E1-0625", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUN,
        "rotulo_item": "Item",
        "assertiva": "A função alocativa decorre da existência de bens públicos.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função alocativa <u>decorre</u> da existência de <u>bens públicos</u>."),
        "poucas": ("Os " + azb("bens públicos") + " são a razão de ser mais clássica da " + azb("função "
                   "alocativa") + ": o mercado não os oferece em quantidade eficiente, e o governo precisa "
                   "provê-los."),
        "destrinchando": [
            MUSGRAVE,
            azb("Bem público") + " puro: " + vd("não rival") + " (o consumo de um não reduz o do outro) e "
            + vd("não excludente") + " (não se consegue impedir quem não paga de consumir). Exemplos: defesa "
            "nacional, iluminação pública, farol, pesquisa básica.",
            "Por que o mercado falha: como ninguém pode ser excluído, cada um tenta ser " + azb("carona")
            + " (<i>free rider</i>) e esconder sua disposição a pagar. A receita privada não cobre o custo e o "
            "bem é subofertado. O governo resolve financiando por tributos.",
            "A regra de provisão eficiente é de " + oc("Samuelson") + " (1954): a soma das " + azb("taxas "
                                                                                          "marginais de "
                                                                                          "substituição")
            + " de todos os consumidores igual ao custo marginal (soma vertical das demandas, e não horizontal, "
            "como nos bens privados).",
            "O item não diz “apenas”: a alocativa também responde a externalidades, monopólios naturais e bens "
            "meritórios. Afirmar que ela <b>decorre</b> dos bens públicos é correto; afirmar que decorre "
            "<b>só</b> deles seria restrição indevida.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item curto e de manual. Quem conhece a lista "
                       "completa de falhas de mercado pode estranhar a ausência das externalidades e marcar "
                       "ERRADO; mas a falta de “apenas” mantém o item verdadeiro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função alocativa decorre exclusivamente da existência de bens públicos.”</i> → ERRADO "
            "(restrição indevida: há também externalidades e monopólios naturais)",
            "<i>“Bens públicos são aqueles produzidos por empresas estatais.”</i> → ERRADO (troca de conceito: o "
            "critério é rivalidade e exclusão, não quem produz)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["decorre"], "dificuldade": 1,
        "comentario_fonte": "A alocativa corrige falhas de mercado como a suboferta de bens públicos (não rivais e "
                            "não excludentes).",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("Untitled (114).jpeg", "Untitled (110).jpeg"),
        "alertas": ["quase_duplicata: ECO-E3-L00037-1 (CEBRASPE TJ/PA 2025: provisão de bens públicos como "
                    "exemplo da função alocativa)"],
    },
    # ------------------------------------------------------------------ E1-0626
    {
        "id": "ECO-E1-0626-1", "fonte_ref": "E1-0626", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUN,
        "rotulo_item": "Item",
        "assertiva": ("A função estabilizadora implica o uso das políticas fiscal e monetária para garantir o bom uso "
                      "dos recursos apenas em momentos de recessão, quando o desemprego aumenta e a taxa de câmbio "
                      "se valoriza."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A função estabilizadora implica o uso das políticas fiscal e monetária para garantir o bom "
                       "uso dos recursos ") + vm("apenas") + az(" em momentos de recessão, quando o desemprego "
                                                               "aumenta") + vm(" e a taxa de câmbio se valoriza")
                    + az(".")),
        "poucas": ("A " + azb("função estabilizadora") + " é " + azb("contracíclica") + " nos dois sentidos: "
                   "estimula na recessão e contém a demanda no superaquecimento inflacionário. O “apenas” mata o "
                   "item."),
        "destrinchando": [
            MUSGRAVE,
            "Os objetivos da estabilizadora são simétricos: " + vd("pleno emprego") + ", "
            + vd("estabilidade de preços") + ", equilíbrio externo e crescimento sustentado. Na recessão, "
            "política expansionista (mais gasto, menos tributo, juros menores); na expansão com inflação, "
            "política contracionista (o inverso).",
            "Parte do trabalho é automático: os " + azb("estabilizadores automáticos") + " (imposto de renda "
            "progressivo, seguro-desemprego) aumentam o déficit na recessão e o reduzem na expansão sem decisão "
            "nova do governo.",
            "O câmbio não é marca da recessão: numa economia emergente, a recessão costuma vir com fuga de "
            "capitais e <b>depreciação</b>; numa economia que importa menos, pode haver apreciação. Não há regra "
            "que associe recessão a câmbio valorizado.",
            vm("Regra-âncora: estabilizar = suavizar o ciclo nas duas direções."),
        ],
        "dissecando": (cz("[restrição indevida · nexo indevido]") + " O núcleo (fiscal e monetária para "
                       "estabilizar) é correto; o erro está no “apenas”, que corta metade do ciclo, e no câmbio "
                       "enxertado como traço típico da recessão. 🔥 “Apenas”, “somente” e “exclusivamente” em "
                       "itens de funções do Estado quase sempre indicam ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função estabilizadora atua tanto em recessões quanto em períodos de pressão "
            "inflacionária.”</i> → CERTO",
            "<i>“Os estabilizadores automáticos dependem de aprovação legislativa a cada fase do ciclo.”</i> → "
            "ERRADO (operam sem decisão discricionária)",
        ])],
        "reescrita": ("A função estabilizadora implica o uso das políticas fiscal e monetária para garantir o bom uso "
                      "dos recursos " + hl("tanto") + " em momentos de recessão, quando o desemprego aumenta, "
                      + hl("quanto em fases de superaquecimento e inflação") + " <s>e a taxa de câmbio se "
                      "valoriza</s>."),
        "tipo_erro": ["RESTRICAO", "NEXO_INDEVIDO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": "A estabilizadora atua em recessões e em períodos de inflação; não se limita a crises.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0627
    {
        "id": "ECO-E1-0627-1", "fonte_ref": "E1-0627", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DES,
        "rotulo_item": "Item",
        "assertiva": ("No que se refere ao desenvolvimento econômico, cabe ao Estado ajustar-se aos objetivos "
                      "econômicos dos grupos economicamente mais relevantes, buscando sempre reduzir a tributação "
                      "incidente sobre os empresários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No que se refere ao desenvolvimento econômico, cabe ao Estado ")
                    + vm("ajustar-se aos objetivos econômicos dos grupos economicamente mais relevantes, buscando "
                         "sempre reduzir a tributação incidente sobre os empresários") + az(".")),
        "poucas": ("O Estado orienta-se pelo " + azb("interesse coletivo") + " — crescimento com redução de "
                   "desigualdades —, não pelos objetivos de grupos dominantes; e nenhuma teoria prescreve reduzir "
                   "<b>sempre</b> a tributação de um grupo."),
        "destrinchando": [
            "No desenvolvimento, as tarefas do Estado são as da tripartição de " + oc("Musgrave") + " aplicadas "
            "ao longo prazo: prover infraestrutura e bens públicos (alocativa), reduzir desigualdades e ampliar "
            "capacidades (distributiva) e dar estabilidade macroeconômica ao investimento (estabilizadora).",
            "Ajustar a política aos interesses de grupos economicamente mais fortes é a descrição de "
            + azb("captura") + " do Estado — tema da " + azb("teoria da escolha pública") + " ("
            + oc("Buchanan e Tullock") + ") e da teoria da regulação de " + oc("Stigler") + " (1971). É uma "
            "falha de governo a ser evitada, não uma função.",
            "Sobre tributos: a carga ótima depende de eficiência e equidade. Cortar sempre a tributação de um "
            "grupo pode reduzir a capacidade de financiar bens públicos e agravar a regressividade — no "
            + rx("Brasil") + ", a tributação da renda e do patrimônio já é baixa frente à do consumo.",
            vm("Regra-âncora: Estado atende ao interesse geral; servir a grupos = captura (falha de governo)."),
        ],
        "dissecando": (cz("[juízo indevido · modulador absoluto]") + " O item atribui ao Estado uma finalidade "
                       "normativamente inaceitável (servir aos mais fortes) e a reforça com “sempre”. Itens de "
                       "papel do Estado com sujeito restrito (“grupos mais relevantes”, “empresários”) costumam ser "
                       "ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Cabe ao Estado investir em infraestrutura e garantir o acesso da população à educação e à "
            "saúde.”</i> → CERTO",
            "<i>“A captura regulatória ocorre quando o regulador passa a atender aos interesses do setor "
            "regulado.”</i> → CERTO",
        ])],
        "reescrita": ("No que se refere ao desenvolvimento econômico, cabe ao Estado " + hl("orientar-se pelo "
                      "interesse coletivo, promovendo crescimento com redução das desigualdades, e não pelos "
                      "objetivos de grupos específicos") + "."),
        "tipo_erro": ["JUIZO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "O Estado deve atuar com foco no bem-estar coletivo e na justiça social, não com base em "
                            "interesses de grupos específicos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0628
    {
        "id": "ECO-E1-0628-1", "fonte_ref": "E1-0628", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_DES,
        "rotulo_item": "Item",
        "assertiva": ("No que se refere ao desenvolvimento econômico, cabe ao Estado investir em infraestrutura, "
                      "promover o investimento privado em setores estratégicos e garantir o acesso da população à "
                      "educação e saúde."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No que se refere ao desenvolvimento econômico, cabe ao Estado investir em "
                      "<u>infraestrutura</u>, <u>promover o investimento privado</u> em setores estratégicos e "
                      "garantir o acesso da população à <u>educação e saúde</u>."),
        "poucas": ("As três tarefas são papéis consensuais do Estado no desenvolvimento: " + azb("infraestrutura")
                   + " (bem público e externalidade), " + azb("indução do investimento") + " e "
                   + azb("capital humano") + "."),
        "destrinchando": [
            azb("Infraestrutura") + ": custo fixo alto, longo prazo, retorno social maior que o privado — "
            "justifica investimento público direto ou concessões e PPPs. Economias externas para toda a cadeia "
            "produtiva.",
            azb("Promoção do investimento privado") + " em setores estratégicos: crédito de longo prazo (no "
            + rx("Brasil") + ", o " + rx("BNDES") + "), incentivos e coordenação de investimentos "
            "complementares. É o núcleo das teorias do " + azb("Estado desenvolvimentista") + " (" + oc("Peter "
                                                                                                    "Evans")
            + ", “autonomia inserida”; " + oc("Alice Amsden") + " e " + oc("Ha-Joon Chang") + " sobre o Leste "
            "Asiático).",
            azb("Educação e saúde") + ": formação de " + azb("capital humano") + ", central nos modelos de "
            "crescimento (Solow aumentado de " + oc("Mankiw, Romer e Weil") + ", 1992; crescimento endógeno de "
            + oc("Lucas") + ", 1988) e bens meritórios na tipologia das finanças públicas.",
            "Ressalva útil em discursiva: a política industrial tem riscos — captura, escolha errada de "
            "“campeões”, custo fiscal. O debate é sobre <b>como</b> o Estado induz, não sobre <b>se</b> induz.",
        ],
        "dissecando": (cz("[literalidade]") + " Enumera papéis de consenso, sem modulador absoluto (“sempre”, "
                       "“exclusivamente”) e sem atribuir ao Estado tarefa que caiba só ao mercado. Contraste "
                       "típico da banca: a versão em que o Estado se ajusta aos interesses dos grupos mais "
                       "fortes, que é ERRADO."),
        "modulos": [("🃏 Carta na manga", [
            "Desenvolvimento exige Estado capaz, não necessariamente grande: infraestrutura, capital humano e "
            "coordenação do investimento são complementos do mercado, não substitutos."])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Ações típicas do Estado desenvolvimentista: corrigir falhas de mercado, reduzir "
                            "desigualdades e promover crescimento sustentável.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0629
    {
        "id": "ECO-E1-0629-1", "fonte_ref": "E1-0629", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FUN,
        "rotulo_item": "Item",
        "assertiva": ("A função desenvolvida pelo Estado com o objetivo de assegurar o ajustamento necessário na "
                      "apropriação de recursos na economia, visando a correção das imperfeições inerentes à própria "
                      "lógica de mercado, denomina-se função alocativa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função desenvolvida pelo Estado com o objetivo de assegurar o ajustamento necessário na "
                      "<u>apropriação de recursos</u> na economia, visando a <u>correção das imperfeições</u> "
                      "inerentes à própria lógica de mercado, denomina-se <u>função alocativa</u>."),
        "poucas": ("Ajustar a alocação de recursos para corrigir " + azb("falhas de mercado") + " é exatamente a "
                   + azb("função alocativa") + "."),
        "destrinchando": [
            MUSGRAVE,
            "As “imperfeições inerentes à lógica de mercado” são as " + azb("falhas de mercado") + ": bens "
            "públicos, externalidades, " + azb("monopólio natural") + " (custo médio decrescente em toda a "
            "faixa relevante: água, energia, gás canalizado), assimetria de informação e mercados incompletos "
            "(crédito de longo prazo, seguros).",
            "Em cada caso o resultado de mercado é ineficiente no sentido de Pareto, e a intervenção pode, em "
            "tese, melhorar a alocação: provisão pública, regulação de preços, tributo ou subsídio corretivo.",
            "“Apropriação de recursos” é o mesmo que alocação: decidir para quais usos vão trabalho, capital e "
            "terra. Não confundir com a " + azb("distributiva") + ", que mexe em <b>quem</b> recebe a renda, "
            "não em <b>o que</b> se produz.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição de manual com vocabulário pouco usual "
                       "(“apropriação de recursos”). A tentação é ler “ajustamento” como estabilização; o que "
                       "decide é “imperfeições da lógica de mercado” = falhas de mercado = alocativa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…visando a correção das desigualdades geradas pela remuneração de mercado dos fatores, "
            "denomina-se função alocativa.”</i> → ERRADO (troca de conceito: é a distributiva)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A alocativa corrige falhas de mercado — bens públicos, externalidades, monopólios "
                            "naturais — promovendo uso eficiente dos recursos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("Untitled (99).jpeg"),
        "alertas": ["quase_duplicata: ECO-E1-0622-1 (mesma definição de função alocativa, outra redação)"],
    },
]
