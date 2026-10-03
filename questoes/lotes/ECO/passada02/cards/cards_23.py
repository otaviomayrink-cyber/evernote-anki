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
                      "dos recursos " + hl("tanto") + " em momentos de recessão, quando o desemprego aumenta <s>e a taxa "
                      "de câmbio se valoriza</s>" + hl(", quanto em fases de superaquecimento e inflação") + "."),
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
    # ------------------------------------------------------------------ E2-L00063
    {
        "id": "ECO-E2-L00063-1", "fonte_ref": "E2-L00063", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZ_A,
        "rotulo_item": "Item",
        "assertiva": ("Após a crise de 1929, a intervenção do governo na economia por meio de políticas fiscais se "
                      "intensificou, baseando-se nas ideias de Keynes, que propôs que o governo poderia desempenhar "
                      "um papel central na regulação dos ciclos econômicos e na mitigação das chamadas falhas de "
                      "mercado. Neste momento, governo assumiu não apenas um papel regulador, mas também de produção "
                      "direta em alguns setores, promovendo um crescimento econômico sustentado e a conformação de "
                      "um estado de bem-estar social pela Europa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Após a crise de 1929</u>, a intervenção do governo na economia por meio de políticas "
                      "fiscais se intensificou, <u>baseando-se nas ideias de Keynes</u>, que propôs que o governo "
                      "poderia desempenhar um papel central na regulação dos ciclos econômicos e na mitigação das "
                      "chamadas falhas de mercado. Neste momento, governo assumiu não apenas um papel regulador, mas "
                      "também de <u>produção direta</u> em alguns setores, promovendo um crescimento econômico "
                      "sustentado e a conformação de um <u>estado de bem-estar social</u> pela Europa."),
        "poucas": ("O item descreve um " + azb("arco histórico") + " (1930–1970): a crise de 1929 derruba a "
                   "confiança na autorregulação, " + oc("Keynes") + " dá base teórica à intervenção e o pós-guerra "
                   "europeu combina Estado regulador, produtor e de bem-estar."),
        "destrinchando": [
            "Antes de 1929 predominava a visão clássica (lei de Say, orçamento equilibrado): o mercado se "
            "autorregula e o desemprego é transitório. A Grande Depressão — desemprego de cerca de "
            + vd("25%") + " nos EUA em 1933 — tornou essa posição insustentável.",
            oc("Keynes") + " formaliza a ruptura na <i>Teoria Geral do Emprego, do Juro e da Moeda</i> ("
            + vd("1936") + "): a economia pode ficar presa num equilíbrio com " + azb("desemprego involuntário")
            + " por insuficiência de " + azb("demanda efetiva") + ", e o gasto público pode compensá-la.",
            "Objeção cronológica comum: o New Deal começa em " + vd("1933") + ", antes da <i>Teoria Geral</i>. "
            "Mas Keynes já defendia obras públicas e gasto deficitário (<i>The Means to Prosperity</i>, 1933; "
            "carta aberta a Roosevelt em dezembro de 1933), e o item fala da intensificação da intervenção "
            "<b>após</b> 1929, num processo que culmina no pós-guerra — não diz que o New Deal nasceu do livro.",
            "No pós-1945, o " + azb("Estado de bem-estar") + " europeu (Relatório " + oc("Beveridge") + ", 1942; "
            "NHS britânico, 1948) somou-se a nacionalizações (carvão, aço e ferrovias no Reino Unido do governo "
            "Attlee; Renault e bancos na França): o Estado passou a <b>produzir</b>, não só a regular. Foram os "
            "“Trinta Gloriosos” de crescimento alto e estável.",
            "Esse consenso keynesiano será atacado nos anos 1970 (estagflação) por monetaristas e novos-clássicos.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Narrativa de manual sem modulador absoluto. A armadilha "
                       "é cronológica: quem lembra que a <i>Teoria Geral</i> é de 1936 tende a ver anacronismo. "
                       "Pergunta-teste: o item afirma uma causalidade pontual (“o New Deal se baseou no livro de "
                       "1936”) ou uma tendência de época? Aqui é tendência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O New Deal, lançado em 1933, aplicou as prescrições formuladas por Keynes na Teoria "
            "Geral.”</i> → ERRADO (anacronismo: a obra é de 1936)",
            "<i>“O Estado de bem-estar europeu do pós-guerra limitou-se a funções regulatórias, sem produção "
            "direta.”</i> → ERRADO (restrição indevida: houve nacionalizações)",
        ]), ("🃏 Carta na manga", [
            "A crise de 1929 marca a passagem do Estado liberal ao intervencionista; o keynesianismo deu a essa "
            "passagem uma teoria, e o pós-guerra, uma arquitetura institucional (bem-estar, empresas públicas, "
            "Bretton Woods)."])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Sob as ideias keynesianas, o governo tornou-se agente ativo, produtor em alguns setores, "
                            "regulador e estabilizador; a objeção cronológica (Teoria Geral de 1936 × New Deal de "
                            "1933) não invalida o item, que descreve um processo amplo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00064
    {
        "id": "ECO-E2-L00064-1", "fonte_ref": "E2-L00064", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_A,
        "rotulo_item": "Item",
        "assertiva": ("Os novos keynesianos defendem que o governo deve atuar especificamente como um parceiro da "
                      "iniciativa privada, sem suplantá-la, mas sim direcionando e regulando as atividades econômicas "
                      "para garantir um desenvolvimento sustentado e justo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os novos keynesianos defendem que o governo deve atuar especificamente como um "
                      "<u>parceiro da iniciativa privada, sem suplantá-la</u>, mas sim direcionando e regulando as "
                      "atividades econômicas para garantir um desenvolvimento sustentado e justo."),
        "poucas": ("Os " + azb("novos keynesianos") + " aceitam o mercado como alocador principal, mas veem "
                   "falhas (rigidezes, informação imperfeita) que justificam um governo regulador e estabilizador — "
                   "complemento, não substituto, do setor privado."),
        "destrinchando": [
            "A escola surge nos anos 1980 (" + oc("Mankiw") + ", " + oc("Romer") + ", " + oc("Stiglitz") + ", "
            + oc("Akerlof") + ", " + oc("Blanchard") + ") como resposta à crítica novo-clássica: adota "
            "expectativas racionais e microfundamentos, mas mostra que " + azb("rigidezes nominais e reais")
            + " (custos de menu, contratos escalonados, salário-eficiência) fazem choques de demanda afetarem "
            "produto e emprego.",
            "Consequência para o Estado: política de estabilização faz sentido (sobretudo monetária, guiada por "
            "regras e metas de inflação), e a regulação corrige falhas de informação — " + oc("Stiglitz")
            + " e " + oc("Akerlof") + " sobre assimetria de informação em crédito e seguros.",
            "Contraste com o keynesianismo do pós-guerra: lá o Estado chegava a produzir diretamente e a "
            "planejar; aqui ele regula, estabiliza e corrige falhas, deixando a produção ao mercado.",
            "Contraste com neoclássicos e novos-clássicos: para estes, o mercado se ajusta rapidamente e a "
            "estabilização ativa é inócua ou prejudicial.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de curso com redação vaga (“parceiro”, “desenvolvimento "
                       "justo”), mas sem erro: a ideia central — governo complementa e regula, não substitui o "
                       "setor privado — é a dos novos keynesianos. O “especificamente” incomoda, mas não cria "
                       "exclusão falsa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os novos keynesianos defendem que o governo substitua a iniciativa privada nos setores "
            "estratégicos, por meio de empresas estatais.”</i> → ERRADO (troca de conceito: visão do "
            "pós-guerra, não dos novos keynesianos)",
            "<i>“Os novos keynesianos sustentam que a política monetária é neutra mesmo no curto prazo.”</i> → "
            "ERRADO (troca de ator: é tese novo-clássica)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["especificamente"], "dificuldade": 2,
        "comentario_fonte": "Os novos keynesianos valorizam o governo como regulador e parceiro da iniciativa "
                            "privada, sem substituí-la, usando políticas fiscal e monetária para corrigir distorções.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00065
    {
        "id": "ECO-E2-L00065-1", "fonte_ref": "E2-L00065", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_A,
        "rotulo_item": "Item",
        "assertiva": ("Uma das críticas dos neoliberais nas décadas de 60 e 70 ao “reinado keynesiano” foi a "
                      "identificação das patologias associadas ao excesso de intervenção governamental. A partir "
                      "dessa crítica, a escola neoliberal emergiu defendendo que o governo deveria reduzir sua "
                      "atuação ao mínimo, abrindo mão de ações de natureza alocativa, distributiva e reguladora, "
                      "privilegiando o livre mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma das críticas dos neoliberais nas décadas de 60 e 70 ao “reinado keynesiano” foi a "
                       "identificação das patologias associadas ao excesso de intervenção governamental. A partir "
                       "dessa crítica, a escola neoliberal emergiu defendendo que o governo deveria reduzir sua "
                       "atuação ao mínimo, ") + vm("abrindo mão de ações de natureza alocativa, distributiva e "
                                                  "reguladora") + az(", privilegiando o livre mercado.")),
        "poucas": ("Estado " + azb("mínimo") + " não é Estado " + azb("ausente") + ": os neoliberais querem "
                   "menos intervenção, mas mantêm funções essenciais — bens públicos, garantia de contratos e de "
                   "concorrência, rede básica de proteção."),
        "destrinchando": [
            "A crítica dos anos 1960–70 vem de várias frentes: " + azb("monetarismo") + " (" + oc("Friedman")
            + "), " + azb("escola austríaca") + " (" + oc("Hayek") + "), " + azb("escolha pública") + " ("
            + oc("Buchanan") + ") e, depois, os novos-clássicos (" + oc("Lucas") + "). As “patologias”: "
            "inflação crescente, déficits crônicos, captura, ineficiência das estatais e a estagflação dos "
            "anos 1970.",
            "O que propõem: desregulação, privatização, abertura comercial, disciplina fiscal e banco central "
            "focado na inflação. Na prática, os governos " + oc("Thatcher") + " (1979) e " + oc("Reagan")
            + " (1981) e, na América Latina, a agenda do Consenso de Washington (" + oc("Williamson") + ", "
            "1989).",
            "O que <b>não</b> propõem: abandonar as três funções. " + oc("Friedman") + " defendia o imposto de "
            "renda negativo (distributiva); " + oc("Hayek") + " aceitava renda mínima e provisão de bens "
            "públicos (alocativa); a defesa da concorrência e dos contratos exige regulação.",
            vm("Regra-âncora: neoliberalismo = Estado mínimo e regras, não Estado zero."),
        ],
        "dissecando": (cz("[modulador absoluto · extrapolação]") + " A primeira frase é correta e a segunda começa "
                       "bem (“reduzir ao mínimo”); o erro é a lista de funções abandonadas, que transforma "
                       "“mínimo” em “nenhum”. Pista: abrir mão até da regulação é incompatível com a defesa de "
                       "mercados que funcionem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…defendendo que o governo deveria reduzir sua atuação, concentrando-se em funções essenciais e "
            "privilegiando o livre mercado.”</i> → CERTO",
            "<i>“A crítica neoliberal ao keynesianismo ganhou força com a estagflação dos anos 1970.”</i> → "
            "CERTO",
        ])],
        "reescrita": ("Uma das críticas dos neoliberais nas décadas de 60 e 70 ao “reinado keynesiano” foi a "
                      "identificação das patologias associadas ao excesso de intervenção governamental. A partir "
                      "dessa crítica, a escola neoliberal emergiu defendendo que o governo deveria reduzir sua "
                      "atuação ao mínimo, " + hl("preservando, porém, funções essenciais — como bens públicos, "
                      "garantia de contratos e regulação da concorrência —") + ", privilegiando o livre mercado."),
        "tipo_erro": ["GENERALIZACAO", "EXTRAPOLACAO"], "moduladores": ["ao mínimo"], "dificuldade": 2,
        "comentario_fonte": "Os neoliberais não defendem ausência do governo, mas redução da intervenção ao mínimo "
                            "necessário, sem abandono absoluto das funções.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00066
    {
        "id": "ECO-E2-L00066-1", "fonte_ref": "E2-L00066", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_A,
        "rotulo_item": "Item",
        "assertiva": ("Tanto neokeynesianos quanto neoclássicos concordam que o governo deve intervir para corrigir "
                      "falhas de mercado. No entanto, enquanto os neokeynesianos acreditam que o governo deve atuar "
                      "também para amenizar ciclos econômicos de expansão e retração, os neoclássicos veem na "
                      "intervenção governamental o papel apenas de corrigir essas falhas para que o mercado possa "
                      "chegar naturalmente a um equilíbrio ótimo de Pareto sem a necessidade de intervenções "
                      "econômicas agressivas no sistema."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Tanto neokeynesianos quanto neoclássicos concordam que o governo deve intervir para corrigir "
                      "<u>falhas de mercado</u>. No entanto, enquanto os neokeynesianos acreditam que o governo deve "
                      "atuar <u>também</u> para amenizar ciclos econômicos de expansão e retração, os neoclássicos "
                      "veem na intervenção governamental o papel <u>apenas</u> de corrigir essas falhas para que o "
                      "mercado possa chegar naturalmente a um equilíbrio ótimo de Pareto sem a necessidade de "
                      "intervenções econômicas agressivas no sistema."),
        "poucas": ("Ponto comum: corrigir " + azb("falhas de mercado") + " (função alocativa). Diferença: os "
                   + azb("neokeynesianos") + " acrescentam a " + azb("estabilização do ciclo") + "; os "
                   + azb("neoclássicos") + " confiam no ajuste do próprio mercado."),
        "destrinchando": [
            "Base comum: o " + azb("primeiro teorema do bem-estar") + " — mercados competitivos completos levam "
            "a um " + azb("ótimo de Pareto") + ". Quando faltam suas hipóteses (bens públicos, externalidades, "
            "poder de mercado, informação assimétrica), há falha de mercado, e as duas escolas admitem "
            "intervenção corretiva.",
            "Divergência macro: para os " + azb("neoclássicos") + " (e novos-clássicos), preços e salários se "
            "ajustam rápido e as expectativas são racionais; flutuações são, em boa parte, respostas eficientes a "
            "choques reais (ciclos reais de negócios, " + oc("Kydland e Prescott") + "). Política "
            "anticíclica seria inútil ou nociva.",
            "Para os " + azb("neokeynesianos") + ", rigidezes nominais e reais fazem choques de demanda gerarem "
            "desemprego involuntário; o governo (sobretudo via política monetária, e fiscal em casos extremos) "
            "deve suavizar o ciclo.",
            "Essa síntese virou o “novo consenso macroeconômico” dos anos 1990–2000: modelos DSGE com rigidezes "
            "e banco central com meta de inflação.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O “apenas” aqui está certo, porque descreve "
                       "a posição neoclássica, que de fato restringe a intervenção às falhas de mercado. A "
                       "armadilha é tratar todo “apenas” como sinal de erro: olhe a quem o modulador é atribuído."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os neoclássicos defendem que o governo atue para amenizar os ciclos econômicos, ao passo que os "
            "neokeynesianos restringem a intervenção à correção de falhas de mercado.”</i> → ERRADO (inversão das "
            "escolas)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["também", "apenas"],
        "dificuldade": 2,
        "comentario_fonte": "Ambas reconhecem intervenção em falhas de mercado; os neokeynesianos favorecem atuação "
                            "anticíclica, os neoclássicos restringem-se às falhas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00080
    {
        "id": "ECO-E2-L00080-1", "fonte_ref": "E2-L00080", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZ_B,
        "rotulo_item": "Item",
        "assertiva": ("A visão keynesiana sugere que o governo deve sempre manter um déficit público para que a "
                      "iniciativa privada prospere, visto que o superávit público poderia levar à restrição do "
                      "crescimento econômico e ao aumento do desemprego involuntário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A visão keynesiana sugere que o governo deve ") + vm("sempre manter um déficit público "
                                                                             "para que a iniciativa privada prospere")
                    + az(", visto que o superávit público poderia levar à restrição do crescimento econômico e ao "
                         "aumento do desemprego involuntário.")),
        "poucas": ("A política fiscal keynesiana é " + azb("contracíclica") + ": déficit na recessão, contenção "
                   "(até superávit) na expansão. Keynes defendia déficit " + vm("pertinente") + ", não "
                   "permanente."),
        "destrinchando": [
            "Diagnóstico de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936): quando a " + azb("demanda "
                                                                                             "efetiva")
            + " é insuficiente, a economia pode ficar presa com desemprego involuntário; o gasto público (ou o "
            "corte de tributos), mesmo deficitário, compensa a retração privada e opera com efeito "
            + azb("multiplicador") + ".",
            "Simetria: o multiplicador age nos dois sentidos. Perto do pleno emprego, mais déficit gera "
            "<b>inflação</b>, não produto. O próprio Keynes, em <i>How to Pay for the War</i> (1940), propôs "
            "poupança compulsória e contenção de demanda para evitar inflação no esforço de guerra.",
            "Ideia operacional: orçamento equilibrado <b>ao longo do ciclo</b>, não a cada ano — superávits nas "
            "“vacas gordas” recompõem o espaço fiscal para as “vacas magras”. Os " + azb("estabilizadores "
                                                                                         "automáticos")
            + " já fazem isso sozinhos: a arrecadação sobe e as transferências caem na expansão.",
            "A segunda oração (superávit podendo restringir o crescimento) só vale em recessão; em economia "
            "aquecida, superávit evita superaquecimento. A caricatura do “déficit sempre” é o que "
            + oc("Joan Robinson") + " chamou de “keynesianismo bastardo”.",
            vm("Regra-âncora: déficit em recessão, ajuste na expansão."),
        ],
        "dissecando": (cz("[modulador absoluto · meia-verdade]") + " O “sempre” converte uma prescrição "
                       "condicionada ao ciclo em regra permanente. A justificativa que segue (“visto que o "
                       "superávit…”) parece keynesiana e dá credibilidade ao erro. 🔥 Itens sobre Keynes e "
                       "déficit quase sempre testam a contraciclicidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na visão keynesiana, em recessões com desemprego involuntário, o governo pode incorrer em "
            "déficit para sustentar a demanda agregada.”</i> → CERTO",
            "<i>“Keynes defendia o orçamento equilibrado em todos os exercícios fiscais.”</i> → ERRADO (troca de "
            "ator: essa é a visão clássica)",
        ])],
        "reescrita": ("A visão keynesiana sugere que o governo deve " + hl("incorrer em déficit público em "
                      "recessões, quando a demanda privada é insuficiente") + ", visto que o superávit público "
                      "poderia levar à restrição do crescimento econômico e ao aumento do desemprego involuntário."),
        "tipo_erro": ["GENERALIZACAO", "MEIA_VERDADE"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Keynes propõe política fiscal contracíclica: déficit em crises, superávit em expansões "
                            "e pressões inflacionárias; o erro está no “sempre”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 006", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (ciclo econômico de banco de imagens; conteúdo absorvido no 📖)"},
                          {"ref": "IMAGEM 007", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (quadro-resumo de terceiros; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00083
    {
        "id": "ECO-E2-L00083-1", "fonte_ref": "E2-L00083", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZ_B,
        "rotulo_item": "Item",
        "assertiva": ("A política fiscal contracionista, caracterizada por aumento dos impostos e diminuição do gasto "
                      "público, é implementada por governos keynesianos em tempos de recessão para estimular o "
                      "crescimento econômico, ajustando a demanda agregada conforme necessário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A política fiscal contracionista, caracterizada por aumento dos impostos e diminuição do "
                       "gasto público, é implementada por governos keynesianos em tempos de ") + vm("recessão")
                    + az(" para ") + vm("estimular o crescimento econômico") + az(", ajustando a demanda agregada "
                                                                                  "conforme necessário.")),
        "poucas": ("Política " + azb("contracionista") + " retira demanda: é para " + azb("superaquecimento e "
                   "inflação") + ". Na recessão, o receituário keynesiano é a " + azb("expansionista") + "."),
        "destrinchando": [
            "Pela identidade " + vd("DA = C + I + G + (X − M)") + ", cortar G reduz a demanda diretamente; "
            "elevar tributos reduz a renda disponível e, portanto, C. Os dois movimentos derrubam a renda com "
            "efeito " + azb("multiplicador") + " — o oposto de estimular o crescimento.",
            "No modelo IS-LM, a contração fiscal desloca a IS para a esquerda: renda e juros caem. Serve para "
            "fechar um " + azb("hiato do produto positivo") + " (produto acima do potencial, inflação subindo).",
            "Na recessão (hiato negativo), o keynesiano prescreve mais gasto e/ou menos impostos, aceitando "
            "déficit temporário. Contração na recessão aprofunda a queda: é o argumento contra a austeridade em "
            "crises (debate europeu pós-2010).",
            "Ressalva acadêmica: a tese da “contração fiscal expansionista” (" + oc("Giavazzi e Pagano") + ", "
            "1990; " + oc("Alesina") + ") sustenta que ajustes críveis podem elevar a confiança e o "
            "crescimento — mas é tese anti-keynesiana, não prescrição de governos keynesianos.",
            vm("Regra-âncora: recessão → expansionista; inflação/superaquecimento → contracionista."),
        ],
        "dissecando": (cz("[inversão]") + " A definição de política contracionista está certa; o item a encaixa "
                       "na fase errada do ciclo e lhe atribui o objetivo da política oposta. O fecho genérico "
                       "(“ajustando a demanda conforme necessário”) soa keynesiano e disfarça a inversão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política fiscal contracionista é recomendada pela abordagem keynesiana em períodos de "
            "superaquecimento, para conter a inflação.”</i> → CERTO",
            "<i>“A redução de impostos em recessão é exemplo de política fiscal contracionista.”</i> → ERRADO "
            "(troca de conceito: é expansionista)",
        ])],
        "reescrita": ("A política fiscal contracionista, caracterizada por aumento dos impostos e diminuição do gasto "
                      "público, é implementada por governos keynesianos em tempos de " + hl("superaquecimento")
                      + " para " + hl("conter a inflação") + ", ajustando a demanda agregada conforme necessário."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Contracionista é aplicada no superaquecimento para conter a inflação; na recessão, "
                            "o keynesianismo recomenda política expansionista.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00426
    {
        "id": "ECO-E2-L00426-1", "fonte_ref": "E2-L00426", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A equivalência ricardiana implica que qualquer expansão fiscal é ineficaz, independentemente "
                      "de horizonte de vida, tributação e crédito."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A equivalência ricardiana implica que ") + vm("qualquer") + az(" expansão fiscal ")
                    + vm("é ineficaz, independentemente de") + az(" horizonte de vida, tributação e crédito.")),
        "poucas": ("A " + azb("equivalência ricardiana") + " é um resultado " + azb("condicional") + ": vale com "
                   "horizonte infinito (ou altruísmo intergeracional), impostos lump-sum e crédito perfeito — "
                   "justamente as três condições que o item declara irrelevantes."),
        "destrinchando": [
            "Tese de " + oc("Robert Barro") + " (“Are Government Bonds Net Wealth?”, 1974), retomando intuição "
            "de " + oc("David Ricardo") + ": dado o caminho dos gastos, financiar por " + azb("dívida")
            + " hoje ou por " + azb("impostos") + " hoje é equivalente, porque a dívida é imposto futuro. O "
            "corte de impostos é poupado, e o consumo não muda.",
            vd("Horizonte de vida") + ": com vidas finitas e sem herança altruísta (gerações sobrepostas, "
            + oc("Diamond") + ", 1965), parte do imposto futuro recai sobre quem ainda não nasceu; a dívida "
            "vira riqueza líquida e o consumo sobe.",
            vd("Tributação") + ": o teorema supõe impostos " + azb("lump-sum") + ". Com impostos distorcivos "
            "(sobre renda, trabalho), mudar o momento da tributação altera incentivos e decisões reais.",
            vd("Crédito") + ": famílias com " + azb("restrição de liquidez") + " consomem o alívio tributário "
            "imediato, pois não conseguiam tomar emprestado contra a renda futura.",
            "Há ainda um segundo erro: o teorema trata da <b>forma de financiamento</b> dado o gasto. Um aumento "
            "do gasto público continua afetando a demanda mesmo sob equivalência; não é “qualquer” expansão que "
            "fica ineficaz.",
            vm("Regra-âncora: equivalência ricardiana = neutralidade dívida × imposto sob hipóteses fortes."),
        ],
        "dissecando": (cz("[modulador absoluto · contradição]") + " Dois absolutos: “qualquer” expansão e "
                       "“independentemente de”. O segundo contradiz o próprio teorema, pois lista exatamente as "
                       "hipóteses de que ele depende. 🔥 “Independentemente de” é marca de ERRADO em itens sobre "
                       "resultados teóricos condicionais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na presença de restrições de crédito, um corte de impostos financiado por dívida tende a elevar o "
            "consumo corrente.”</i> → CERTO",
            "<i>“A equivalência ricardiana exige que os impostos sejam distorcivos.”</i> → ERRADO (inversão: exige "
            "impostos lump-sum)",
        ])],
        "reescrita": ("A equivalência ricardiana implica que " + hl("a") + " expansão fiscal " + hl("financiada por "
                      "dívida tem o mesmo efeito do financiamento por impostos apenas sob hipóteses restritas de")
                      + " horizonte de vida, tributação e crédito."),
        "tipo_erro": ["GENERALIZACAO", "CONTRADICAO"], "moduladores": ["qualquer", "independentemente"],
        "dificuldade": 2,
        "comentario_fonte": "A equivalência ricardiana é condicional: depende de horizonte infinito/altruísmo, "
                            "impostos lump-sum e mercados de crédito perfeitos; violadas as hipóteses, a política "
                            "fiscal tem efeitos reais.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00725
    {
        "id": "ECO-E2-L00725-1", "fonte_ref": "E2-L00725", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NAB_MACRO,
        "rotulo_item": "Item",
        "assertiva": ("O seguro-desemprego é uma espécie de estabilizador automático, instrumento de política fiscal "
                      "que visa reduzir as flutuações da atividade econômica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O seguro-desemprego é uma espécie de <u>estabilizador automático</u>, instrumento de "
                      "política fiscal que visa reduzir as flutuações da atividade econômica."),
        "poucas": ("O " + azb("seguro-desemprego") + " sobe na recessão e cai na expansão sem decisão nova do "
                   "governo: amortece a queda da renda disponível e, por isso, é " + azb("estabilizador "
                                                                                          "automático") + "."),
        "destrinchando": [
            azb("Estabilizadores automáticos") + " são componentes do orçamento que variam com o ciclo por "
            "força das regras já vigentes: na recessão, a arrecadação cai e as transferências sobem (o déficit "
            "aumenta); na expansão, o inverso. Sustentam a demanda quando ela cai e a contêm quando acelera.",
            "Exemplos clássicos: " + vd("imposto de renda progressivo") + " (a alíquota média cai quando a renda "
            "cai), seguro-desemprego e outras transferências condicionadas à renda, tributos sobre lucros.",
            "Vantagem sobre a política " + azb("discricionária") + ": não sofrem as defasagens de reconhecimento, "
            "decisão e implementação (aprovar lei, executar obra). Atuam no mesmo trimestre do choque.",
            "No modelo keynesiano, reduzem o " + azb("multiplicador") + ": com tributos proporcionais à renda, "
            "k = 1/[1 − c(1 − t)], menor que 1/(1 − c). Uma parte de cada variação de renda é absorvida pelo "
            "orçamento — é exatamente isso que amortece as flutuações.",
            "Por isso se separa o resultado fiscal em parte " + azb("cíclica") + " e " + azb("estrutural") + ": "
            "só a estrutural revela a postura discricionária do governo.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. O risco é achar que, por ser política "
                       "social, o seguro-desemprego não seria instrumento de política fiscal — mas toda "
                       "transferência do orçamento é política fiscal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os estabilizadores automáticos aumentam o multiplicador keynesiano dos gastos públicos.”</i> → "
            "ERRADO (inversão: reduzem-no)",
            "<i>“Os estabilizadores automáticos dependem de decisão discricionária do governo a cada fase do "
            "ciclo.”</i> → ERRADO (contradição: operam pelas regras vigentes)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["uma espécie de"], "dificuldade": 1,
        "comentario_fonte": "Estabilizadores automáticos suavizam o ciclo sem decisão discricionária; o "
                            "seguro-desemprego é exemplo clássico. (Comentário idêntico na duplicata E2-L00780.)",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L00780 (mesma assertiva e comentário) fundida neste card"],
    },
    # ------------------------------------------------------------------ E2-L00902
    {
        "id": "ECO-E2-L00902-1", "fonte_ref": "E2-L00902", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_24,
        "rotulo_item": "Item",
        "assertiva": ("Em relação à equivalência ricardiana, se o governo financiar o corte de impostos hoje através "
                      "de endividamento a longo prazo, as famílias irão consumir mais, caso não sejam altruístas em "
                      "relação as suas gerações futuras."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em relação à equivalência ricardiana, se o governo financiar o corte de impostos hoje através "
                      "de endividamento <u>a longo prazo</u>, as famílias irão consumir mais, <u>caso não sejam "
                      "altruístas</u> em relação as suas gerações futuras."),
        "poucas": ("Sem " + azb("altruísmo intergeracional") + ", a dívida de longo prazo será paga em parte "
                   "pelos descendentes: a geração atual fica mais rica e " + vd("consome mais") + " — a "
                   "equivalência falha."),
        "destrinchando": [
            "Mecânica da " + azb("equivalência ricardiana") + ": corte de impostos hoje + dívida = impostos "
            "maiores amanhã, de mesmo valor presente. Família racional poupa todo o corte e o consumo não muda. "
            "Nas palavras de " + oc("Mankiw") + ", a política é “uma redução de impostos no presente e um "
            "aumento no futuro”.",
            "Se a dívida vence <b>a longo prazo</b>, os impostos futuros podem cair sobre filhos e netos. "
            + oc("Barro") + " (1974) salva a equivalência com o " + azb("altruísmo") + ": pais que se importam "
            "com os filhos aumentam a herança na exata medida dos impostos futuros deles — a família age como "
            "uma dinastia de horizonte infinito.",
            "Sem altruísmo, a geração atual trata os títulos como " + azb("riqueza líquida") + ": o valor "
            "presente dos impostos que ela própria pagará é menor que o corte recebido. Resultado: consumo maior "
            "agora — o item é CERTO.",
            "Outras quebras da equivalência: " + azb("restrição de crédito") + ", impostos distorcivos, "
            "miopia, incerteza sobre quem pagará e migração (quem sai do país escapa do imposto futuro).",
        ],
        "dissecando": (cz("[exceção · contraintuitivo]") + " O item cobra justamente a hipótese que, violada, "
                       "derruba o teorema. Quem decorou “equivalência ricardiana = consumo não muda” marca ERRADO "
                       "sem ler o “caso não sejam altruístas”. Leia sempre a condição final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as famílias manterão o consumo inalterado, ainda que não sejam altruístas em relação às "
            "gerações futuras.”</i> → ERRADO (contradição: sem altruísmo, a dívida longa vira riqueza líquida)",
            "<i>“Se as famílias forem altruístas e não houver restrição de crédito, o corte de impostos "
            "financiado por dívida não altera o consumo.”</i> → CERTO",
        ])],
        "tipo_erro": ["EXCECAO", "CONTRAINTUITIVO"], "moduladores": ["caso"], "dificuldade": 2,
        "comentario_fonte": "Pela visão ricardiana, endividamento hoje é imposto amanhã; Barro acrescenta o "
                            "altruísmo intergeracional. Sem altruísmo, o consumo aumenta, uma das hipóteses que "
                            "invalidam a equivalência, ao lado de restrições de crédito e migração.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01041
    {
        "id": "ECO-E2-L01041-1", "fonte_ref": "E2-L01041", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o Princípio da Equivalência Ricardiana, uma redução dos impostos leva a um "
                      "aumento proporcional do consumo privado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o Princípio da Equivalência Ricardiana, uma redução dos impostos ")
                    + vm("leva a um aumento proporcional do consumo privado") + az(".")),
        "poucas": ("Sob " + azb("equivalência ricardiana") + ", o corte de impostos (com gasto constante) é "
                   "integralmente " + azb("poupado") + " para pagar os impostos futuros: o consumo " + vd("não "
                                                                                                       "muda") + "."),
        "destrinchando": [
            "Com o gasto público dado, cortar impostos hoje cria déficit, financiado por títulos. A "
            + azb("restrição orçamentária intertemporal do governo") + " exige que o valor presente dos impostos "
            "futuros suba exatamente o valor do corte.",
            "A família racional faz a mesma conta: sua riqueza (valor presente da renda líquida de impostos) não "
            "mudou. Ela compra os títulos com o dinheiro do corte: " + vd("poupança privada ↑ = déficit ↑")
            + ", " + vd("poupança nacional constante") + ", consumo, juros e investimento inalterados.",
            "A visão tradicional (keynesiana) prevê o contrário: renda disponível ↑ → consumo ↑ pela "
            + azb("propensão marginal a consumir") + " — e, mesmo nela, o aumento seria uma fração (c × ΔT), "
            "não “proporcional” no sentido de acompanhar o corte por inteiro.",
            "Hipóteses do teorema (" + oc("Barro") + ", 1974): agentes racionais e prospectivos, horizonte "
            "infinito ou altruísmo intergeracional, crédito perfeito e impostos lump-sum.",
            vm("Regra-âncora: equivalência ricardiana → corte de impostos vira poupança, não consumo."),
        ],
        "dissecando": (cz("[troca de conceito · contradição]") + " O item atribui à equivalência ricardiana a "
                       "previsão da visão keynesiana tradicional. Pista: se o corte elevasse o consumo, não haveria "
                       "“equivalência” entre financiar por dívida ou por imposto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a equivalência ricardiana, uma redução de impostos financiada por dívida eleva a "
            "poupança privada no mesmo montante.”</i> → CERTO",
            "<i>“Segundo a equivalência ricardiana, uma redução de impostos financiada por dívida eleva a "
            "poupança nacional.”</i> → ERRADO (troca de conceito: a poupança nacional fica constante)",
        ])],
        "reescrita": ("De acordo com o Princípio da Equivalência Ricardiana, uma redução dos impostos "
                      + hl("não altera o consumo privado, pois a poupança privada aumenta no mesmo montante") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": ["proporcional"], "dificuldade": 1,
        "comentario_fonte": "O consumo não se altera: a poupança privada aumenta na mesma medida, pois os "
                            "indivíduos antecipam impostos futuros para pagar a dívida.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01255-1 (corte de impostos e consumo corrente sob equivalência "
                    "ricardiana)"],
    },
    # ------------------------------------------------------------------ E2-L01254
    {
        "id": "ECO-E2-L01254-1", "fonte_ref": "E2-L01254", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_ER,
        "rotulo_item": "Item",
        "assertiva": ("Pelo princípio da Equivalência Ricardiana, uma redução de impostos financiada pela emissão de "
                      "títulos públicos não implica aumento de poupança."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Pelo princípio da Equivalência Ricardiana, uma redução de impostos financiada pela emissão "
                       "de títulos públicos ") + vm("não") + az(" implica aumento de poupança.")),
        "poucas": ("É o contrário: a família " + azb("poupa todo o corte") + " para pagar os impostos futuros — a "
                   + vd("poupança privada sobe") + " no mesmo montante do déficit."),
        "destrinchando": [
            "Raciocínio ricardiano em três passos: (1) o governo corta T e emite títulos de mesmo valor; (2) os "
            "títulos serão pagos, com juros, por impostos futuros de " + vd("mesmo valor presente") + "; (3) a "
            "família, que antecipa isso, não se sente mais rica e guarda o corte — em geral comprando os próprios "
            "títulos emitidos.",
            "Contabilidade: " + vd("S_nacional = S_privada + S_pública") + ". O corte reduz a poupança pública "
            "(déficit maior) e eleva a privada na mesma medida: a " + azb("poupança nacional") + " fica "
            "constante, e por isso juros, investimento e conta-corrente também não se movem.",
            "Atenção ao termo: o item diz só “poupança”. Para a " + azb("privada") + ", há aumento (item "
            "ERRADO). Se dissesse “poupança nacional”, não haveria aumento — e o item seria CERTO. A banca "
            "explora essa ambiguidade.",
            "Sem equivalência (visão tradicional), parte do corte é consumida: a poupança privada sobe menos que "
            "o déficit, a nacional cai, os juros sobem e há " + azb("crowding out") + ".",
        ],
        "dissecando": (cz("[inversão]") + " Negação simples do mecanismo central do teorema. Pista: a "
                       "equivalência ricardiana se explica justamente pela poupança — se ela não subisse, o "
                       "consumo subiria e não haveria equivalência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela equivalência ricardiana, uma redução de impostos financiada por títulos não altera a "
            "poupança nacional.”</i> → CERTO",
            "<i>“Pela equivalência ricardiana, a redução de impostos financiada por títulos eleva a taxa de "
            "juros.”</i> → ERRADO (contradição: juros inalterados)",
        ])],
        "reescrita": ("Pelo princípio da Equivalência Ricardiana, uma redução de impostos financiada pela emissão de "
                      "títulos públicos <s>não</s> implica aumento de poupança" + hl(" privada, no mesmo montante "
                                                                                     "do corte") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": "Os agentes pouparão exatamente o necessário para pagar impostos mais elevados no "
                            "futuro.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01255
    {
        "id": "ECO-E2-L01255-1", "fonte_ref": "E2-L01255", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_ER,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a equivalência ricardiana, um corte de impostos correntes, mantidos constantes "
                      "todos os outros elementos, produz aumento do consumo corrente, em face da elevação da renda "
                      "disponível."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a equivalência ricardiana, um corte de impostos correntes, mantidos constantes "
                       "todos os outros elementos, ") + vm("produz aumento do consumo corrente, em face da elevação "
                                                           "da renda disponível") + az(".")),
        "poucas": ("A renda disponível sobe hoje, mas a " + azb("renda permanente") + " não: com o gasto "
                   "constante, o corte vira dívida e impostos futuros. O ricardiano " + azb("poupa") + " o "
                   "acréscimo, e o " + vd("consumo corrente não muda") + "."),
        "destrinchando": [
            "“Mantidos constantes todos os outros elementos” inclui o gasto público: o corte de impostos gera "
            "déficit, financiado por títulos, que exigirão impostos maiores no futuro.",
            "O consumidor ricardiano decide pelo " + azb("valor presente") + " de toda a sua renda líquida de "
            "impostos — a lógica da " + azb("renda permanente") + " de " + oc("Friedman") + " e do ciclo de "
            "vida de " + oc("Modigliani") + ". Imposto menor hoje e maior amanhã, de mesmo valor presente, deixa "
            "essa riqueza intacta; logo, o consumo também.",
            "O acréscimo de renda disponível corrente é poupado (geralmente em títulos públicos). Conclusão "
            "ricardiana: o corte de impostos financiado por dívida é " + azb("ineficaz") + " para estimular a "
            "demanda — por isso a tese é tratada como crítica ao multiplicador keynesiano.",
            "O raciocínio do item (renda disponível ↑ → consumo ↑) é o da " + azb("função consumo "
                                                                                   "keynesiana") + ", "
            "em que o consumo depende da renda corrente.",
            vm("Regra-âncora: ricardiano olha a riqueza, não a renda do ano."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Aplica a função consumo keynesiana dentro de uma pergunta "
                       "sobre equivalência ricardiana. O “em face da elevação da renda disponível” é a isca: "
                       "parece uma justificativa óbvia, mas é exatamente o canal que o teorema nega."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a visão keynesiana tradicional, um corte de impostos correntes eleva o consumo corrente "
            "pela elevação da renda disponível.”</i> → CERTO",
            "<i>“De acordo com a equivalência ricardiana, um corte de impostos acompanhado de corte permanente "
            "dos gastos não altera o consumo.”</i> → ERRADO (troca de conceito: com gasto menor, a riqueza "
            "sobe e o consumo aumenta)",
        ])],
        "reescrita": ("De acordo com a equivalência ricardiana, um corte de impostos correntes, mantidos constantes "
                      "todos os outros elementos, " + hl("não altera o consumo corrente, pois a elevação da renda "
                                                         "disponível é poupada para pagar os impostos futuros") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Com equivalência ricardiana, o corte eleva o déficit e os impostos futuros; os agentes "
                            "poupam o aumento de renda disponível, e o consumo não se altera.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01041-1 (corte de impostos e consumo sob equivalência ricardiana)"],
    },
    # ------------------------------------------------------------------ E2-L01482
    {
        "id": "ECO-E2-L01482-1", "fonte_ref": "E2-L01482", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_PAND,
        "rotulo_item": "Item",
        "assertiva": ("O aumento recente do endividamento do governo e das taxas de juros pagas pelos títulos da "
                      "dívida pública é compatível com o chamado efeito deslocamento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento recente do endividamento do governo e das taxas de juros pagas pelos títulos da "
                      "dívida pública é <u>compatível</u> com o chamado <u>efeito deslocamento</u>."),
        "poucas": ("No " + azb("efeito deslocamento") + " (" + azb("crowding out") + "), o governo financia o "
                   "gasto com dívida, disputa a poupança, eleva os juros e afasta o investimento privado. Dívida "
                   "e juros subindo juntos é o retrato desse mecanismo."),
        "destrinchando": [
            "Mecanismo no IS-LM: a expansão fiscal desloca a IS para a direita; com a oferta de moeda dada, a "
            "renda maior eleva a demanda por moeda e os " + vd("juros sobem") + "; juros maiores reduzem o "
            "investimento privado. A renda cresce, mas menos que o multiplicador simples prometia.",
            "No mercado de " + azb("fundos emprestáveis") + ": o déficit reduz a poupança nacional; a oferta de "
            "fundos cai e o juro de equilíbrio sobe. Mesma conclusão: o gasto público toma o lugar de parte do "
            "investimento privado.",
            "Intensidade: " + azb("crowding out total") + " com LM vertical (caso clássico) ou pleno emprego; "
            + azb("nulo") + " na armadilha da liquidez (LM horizontal). Há ainda o canal de " + azb("risco "
                                                                                                    "fiscal")
            + ": dívida alta exige prêmio maior nos títulos.",
            "No " + rx("Brasil") + ", a resposta à pandemia (auxílio emergencial, gasto em saúde, adiamento de "
            "tributos) elevou fortemente a dívida bruta em " + vd("2020") + ", e a " + vd("Selic subiu de 2% "
                                                                                       "(2020–21) a 13,75% "
                                                                                       "(2022)") + ". A alta "
            "dos juros teve como causa principal a inflação, mas o quadro dívida ↑ + juros ↑ é "
            "<b>compatível</b> com o deslocamento — e é só isso que o item afirma.",
        ],
        "grafico_verso": "ECO-E2-L01482-1-V1",
        "dissecando": (cz("[modulador relativo]") + " O verbo “é compatível” protege o item: não se afirma que a "
                       "alta dos juros foi causada pelo crowding out, só que o quadro é coerente com ele. Seria "
                       "ERRADO se dissesse que o deslocamento <b>explica integralmente</b> a alta dos juros."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O efeito deslocamento é máximo quando a economia está na armadilha da liquidez.”</i> → ERRADO "
            "(inversão: aí ele é nulo)",
            "<i>“A elevação dos juros dos títulos públicos no pós-pandemia decorreu exclusivamente do efeito "
            "deslocamento.”</i> → ERRADO (modulador absoluto: a inflação foi o motor principal)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["compatível"], "dificuldade": 1,
        "comentario_fonte": "O crowding out ocorre quando o aumento do gasto financiado por dívida eleva os juros e "
                            "desloca o investimento privado; dívida e juros maiores na pandemia são compatíveis "
                            "com esse efeito.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 375", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01482-1-V1, IS-LM com crowding out)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01483
    {
        "id": "ECO-E2-L01483-1", "fonte_ref": "E2-L01483", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_PAND,
        "rotulo_item": "Item",
        "assertiva": ("Da perspectiva ricardiana da dívida pública, o aumento temporário da renda gerado pelo impacto "
                      "da política fiscal expansionista tende a elevar o consumo no curto prazo, mas no longo prazo "
                      "ocorrerá apenas um aumento da poupança privada, que servirá para pagar os impostos que subirão "
                      "para pagar o serviço do endividamento adicional do governo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Da perspectiva ricardiana da dívida pública, o aumento temporário da renda gerado pelo "
                       "impacto da política fiscal expansionista ") + vm("tende a elevar o consumo no curto prazo, "
                                                                        "mas no longo prazo ocorrerá apenas")
                    + az(" um aumento da poupança privada, que servirá para pagar os impostos que subirão para pagar "
                         "o serviço do endividamento adicional do governo.")),
        "poucas": ("Na visão " + azb("ricardiana") + ", o consumidor antecipa os impostos futuros " + vd("desde o "
                   "início") + ": não há alta do consumo no curto prazo; a poupança privada sobe " + azb("já") + ", "
                   "no mesmo montante do déficit."),
        "destrinchando": [
            "O agente ricardiano é " + azb("prospectivo") + " (<i>forward-looking</i>): ao ver o déficit, "
            "reconhece imediatamente que a dívida é imposto futuro de mesmo valor presente. Sua riqueza não "
            "muda, e ele não tem motivo para consumir mais em nenhum momento.",
            "Por isso o ajuste é " + vd("imediato e integral") + ": a poupança privada sobe no próprio período "
            "do corte de impostos ou da transferência, compensando a queda da poupança pública. Não existe uma "
            "fase inicial de consumo seguida de poupança.",
            "A sequência descrita no item (consumo sobe agora, poupança depois) é a de um consumidor "
            + azb("míope") + " ou com " + azb("restrição de liquidez") + " — justamente os casos que "
            "<b>violam</b> a equivalência.",
            "Empiricamente, o auxílio emergencial de " + vd("2020") + " no " + rx("Brasil") + " foi em grande "
            "parte consumido: beneficiários de baixa renda, sem acesso a crédito, comportam-se de modo "
            "não ricardiano. Isso não muda o gabarito — o item pede a <b>perspectiva ricardiana</b>.",
            vm("Regra-âncora: ricardiano não tem “curto prazo keynesiano” — poupa desde o primeiro real."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A segunda metade (poupança para pagar impostos "
                       "futuros) é o mecanismo ricardiano correto; o erro foi enxertado na cronologia, com um "
                       "consumo inicial que a teoria nega — comportamento keynesiano enxertado no curto prazo. "
                       "Desconfie de “no curto prazo… mas no longo prazo” em itens "
                       "sobre expectativas racionais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Da perspectiva ricardiana, a política fiscal expansionista financiada por dívida eleva desde logo "
            "a poupança privada, sem efeito sobre o consumo.”</i> → CERTO",
            "<i>“Famílias com restrição de liquidez tendem a consumir transferências temporárias, contrariando a "
            "equivalência ricardiana.”</i> → CERTO",
        ])],
        "reescrita": ("Da perspectiva ricardiana da dívida pública, o aumento temporário da renda gerado pelo impacto "
                      "da política fiscal expansionista " + hl("não eleva o consumo nem no curto prazo: desde logo "
                                                               "ocorre apenas") + " um aumento da poupança privada, "
                      "que servirá para pagar os impostos que subirão para pagar o serviço do endividamento adicional "
                      "do governo."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["tende a", "apenas"], "dificuldade": 2,
        "comentario_fonte": "Na equivalência ricardiana, os consumidores antecipam impostos futuros e poupam o "
                            "acréscimo de renda imediatamente; o erro é afirmar alta do consumo no curto prazo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 376-377", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (slides de aula em texto; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01520
    {
        "id": "ECO-E2-L01520-1", "fonte_ref": "E2-L01520", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_DIV,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de equivalência ricardiana implica que os agentes levem em conta os impactos futuros "
                      "de políticas fiscais expansionistas, levando ao aumento da poupança no presente e reduzindo o "
                      "impacto esperado pela teoria keynesiana."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O conceito de equivalência ricardiana implica que os agentes levem em conta os <u>impactos "
                      "futuros</u> de políticas fiscais expansionistas, levando ao <u>aumento da poupança no "
                      "presente</u> e <u>reduzindo</u> o impacto esperado pela teoria keynesiana."),
        "poucas": ("Agentes " + azb("prospectivos") + " veem no déficit de hoje os impostos de amanhã, "
                   + vd("poupam já") + " e neutralizam o estímulo: a equivalência ricardiana é uma " + azb("crítica "
                   "ao multiplicador keynesiano") + "."),
        "destrinchando": [
            "Argumento em quatro passos (como nos manuais): (1) o governo pode financiar o gasto com impostos "
            "atuais ou com dívida; (2) a dívida terá de ser paga, com impostos futuros maiores; (3) a escolha é, "
            "portanto, entre imposto hoje e imposto amanhã; (4) o contribuinte, antecipando isso, aumenta a "
            "poupança e compra os títulos emitidos.",
            "Consequência: para um dado gasto, trocar imposto por dívida " + vd("não afeta a demanda agregada "
                                                                                "nem os juros") + ". Como a "
            "poupança privada sobe no mesmo montante do déficit, não há queda da poupança nacional, nem "
            "crowding out, nem piora das contas externas. A dívida não é riqueza líquida do setor privado.",
            "Por que “reduzindo” e não “anulando”: na versão estrita, o efeito de um corte de impostos financiado "
            "por dívida é nulo; nas versões com violações parciais (parte das famílias com restrição de crédito), "
            "é apenas menor. “Reduzir” cobre as duas leituras — o item não usa absoluto.",
            "Autores: intuição de " + oc("David Ricardo") + " (que, aliás, duvidava de que as pessoas agissem "
            "assim) e formalização de " + oc("Robert Barro") + " (1974); daí o nome “equivalência "
            "Barro-Ricardo”.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Reproduz a tese do manual. O que derruba "
                       "o candidato é o verbo: quem acha que a equivalência “anula” e não só “reduz” marca ERRADO. "
                       "Reduzir é compatível com anular; seria ERRADO trocar por “intensificar”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…intensificando o efeito multiplicador previsto por Keynes.”</i> → ERRADO (inversão: reduz ou "
            "anula)",
            "<i>“…levando à redução da poupança no presente.”</i> → ERRADO (inversão: a poupança aumenta)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["reduzindo"], "dificuldade": 1,
        "comentario_fonte": "Agentes racionais antecipam impostos futuros e elevam a poupança, atenuando ou anulando "
                            "o multiplicador keynesiano; slides de aula reproduzem a argumentação da equivalência "
                            "Barro-Ricardo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 403-404", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (slides de aula absorvidos no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01635-1 (mesmo item com o acréscimo “como o aumento da dívida "
                    "pública e de impostos”)"],
    },
    # ------------------------------------------------------------------ E2-L01635
    {
        "id": "ECO-E2-L01635-1", "fonte_ref": "E2-L01635", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_DIV,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de equivalência ricardiana implica que os agentes levem em conta os impactos futuros "
                      "de políticas fiscais expansionistas como o aumento da dívida pública e de impostos, levando ao "
                      "aumento da poupança no presente e reduzindo o impacto da política fiscal que seria esperado "
                      "pela teoria keynesiana."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O conceito de equivalência ricardiana implica que os agentes levem em conta os impactos futuros "
                      "de políticas fiscais expansionistas como o <u>aumento da dívida pública e de impostos</u>, "
                      "levando ao <u>aumento da poupança no presente</u> e reduzindo o impacto da política fiscal que "
                      "seria esperado pela teoria keynesiana."),
        "poucas": ("Dívida maior hoje = " + azb("impostos maiores amanhã") + ". O agente ricardiano antecipa a "
                   "conta, " + vd("poupa no presente") + " e esvazia o estímulo que o multiplicador keynesiano "
                   "prometia."),
        "destrinchando": [
            "O item explicita os “impactos futuros”: a expansão financiada por dívida eleva o " + azb("estoque "
            "de dívida") + " e, por consequência, os " + azb("impostos futuros") + " necessários para pagar "
            "principal e juros (restrição orçamentária intertemporal do governo).",
            "O consumidor, que é também contribuinte, internaliza essa restrição: sua riqueza líquida não muda "
            "com o corte de impostos financiado por dívida, então ele " + vd("poupa o corte") + " — "
            "tipicamente comprando os próprios títulos públicos.",
            "Resultado agregado: poupança privada ↑ = poupança pública ↓; poupança nacional, juros e demanda "
            "agregada constantes. É a " + azb("crítica ricardiana ao multiplicador") + ": no modelo keynesiano, "
            "o corte de impostos teria efeito −c/(1 − c) × ΔT sobre a renda; sob equivalência, efeito zero.",
            "Hipóteses: horizonte infinito ou " + azb("altruísmo intergeracional") + " (" + oc("Barro") + ", "
            "1974), crédito perfeito e impostos lump-sum. Violadas, o efeito keynesiano reaparece em parte.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Mesma tese do manual, com o mecanismo explicitado (dívida → "
                       "impostos). O “reduzindo” é moderado e verdadeiro; não há modulador absoluto. A banca "
                       "costuma trocar por “intensificando” para fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…intensificando o efeito multiplicador previsto por Keynes.”</i> → ERRADO (inversão)",
            "<i>“…desde que os agentes tenham restrição de liquidez.”</i> → ERRADO (inversão: a restrição de "
            "liquidez quebra a equivalência)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["reduzindo"], "dificuldade": 1,
        "comentario_fonte": "Agentes antecipam impostos futuros, poupam para compensar déficits e reduzem o "
                            "multiplicador keynesiano; resumo da argumentação Barro-Ricardo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01520-1 (mesmo item sem o trecho “como o aumento da dívida pública "
                    "e de impostos”)"],
    },
    # ------------------------------------------------------------------ E2-L01778
    {
        "id": "ECO-E2-L01778-1", "fonte_ref": "E2-L01778", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_DIV,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de equivalência ricardiana implica que os agentes levem em conta os impactos futuros "
                      "de políticas fiscais expansionistas, intensificando o efeito multiplicador previsto por "
                      "Keynes e elevando o impacto de políticas fiscais expansionistas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O conceito de equivalência ricardiana implica que os agentes levem em conta os impactos "
                       "futuros de políticas fiscais expansionistas, ") + vm("intensificando") + az(" o efeito "
                       "multiplicador previsto por Keynes e ") + vm("elevando") + az(" o impacto de políticas "
                                                                                    "fiscais expansionistas.")),
        "poucas": ("Antecipar os impostos futuros leva a " + azb("poupar") + ", não a gastar: a equivalência "
                   "ricardiana " + vm("reduz ou anula") + " o multiplicador keynesiano."),
        "destrinchando": [
            "Lógica ricardiana: déficit hoje → dívida → " + azb("impostos futuros") + " de mesmo valor presente. "
            "O agente racional poupa o corte de impostos (ou a transferência) para pagar essa conta.",
            "No " + azb("multiplicador keynesiano") + ", a cadeia é a oposta: renda disponível ↑ → consumo ↑ → "
            "renda de outros ↑ → novas rodadas de consumo. Se a primeira rodada é poupada, a cadeia não começa: "
            "o multiplicador do corte de impostos financiado por dívida vai a " + vd("zero") + ".",
            "Antecipar o futuro pode até <b>reduzir</b> o consumo presente em outro cenário: se o agente teme "
            "que a dívida alta leve a ajuste mais duro adiante, poupa ainda mais (efeitos não keynesianos, tese "
            "da “contração fiscal expansionista”). Em nenhuma versão a antecipação intensifica o multiplicador.",
            "A tese de " + oc("Barro") + " (1974) é, por isso, classificada nos manuais como "
            + azb("crítica ao multiplicador keynesiano") + ".",
            vm("Regra-âncora: equivalência ricardiana enfraquece a política fiscal; nunca a fortalece."),
        ],
        "dissecando": (cz("[inversão]") + " A primeira metade copia a definição correta; a segunda inverte o "
                       "efeito. O item é a versão “trocada” de um CERTO clássico, que diz “aumento da poupança e "
                       "redução do impacto keynesiano”. Pista: “levar em conta os impactos futuros” é "
                       "comportamento de poupador."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…levando ao aumento da poupança no presente e reduzindo o impacto esperado pela teoria "
            "keynesiana.”</i> → CERTO",
        ])],
        "reescrita": ("O conceito de equivalência ricardiana implica que os agentes levem em conta os impactos futuros "
                      "de políticas fiscais expansionistas, " + hl("reduzindo") + " o efeito multiplicador previsto "
                      "por Keynes e " + hl("diminuindo") + " o impacto de políticas fiscais expansionistas."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A equivalência ricardiana reduz ou anula o multiplicador: os agentes poupam para pagar "
                            "impostos futuros.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00037
    {
        "id": "ECO-E3-L00037-1", "fonte_ref": "E3-L00037", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": True,
        "comando": CMD_TJPA_FUN,
        "rotulo_item": "Item",
        "assertiva": ("A provisão de bens públicos é um exemplo de atuação do Estado no exercício de sua função "
                      "alocativa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A provisão de <u>bens públicos</u> é um exemplo de atuação do Estado no exercício de sua "
                      "<u>função alocativa</u>."),
        "poucas": ("Bens " + azb("não rivais e não excludentes") + " são subofertados pelo mercado por causa do "
                   + azb("carona") + "; o Estado os provê para corrigir a alocação — é o exemplo-padrão da "
                   + azb("função alocativa") + "."),
        "destrinchando": [
            MUSGRAVE,
            azb("Bem público") + " puro: " + vd("não rival") + " (meu consumo não reduz o seu) e "
            + vd("não excludente") + " (não dá para barrar quem não paga). Exemplos: defesa nacional, "
            "iluminação pública, segurança, farol, sinal aberto de rádio.",
            "Falha de mercado: cada um espera que o outro pague — o problema do " + azb("carona")
            + " (<i>free rider</i>). A receita privada não cobre o custo e o bem é ofertado abaixo do "
            "eficiente. Solução: financiamento compulsório por tributos.",
            "Provisão ≠ produção: o Estado pode contratar a empresa privada que constrói e mantém a iluminação; "
            "o que importa é quem decide e financia a quantidade ofertada.",
            "Compare: oferecer educação gratuita (bem meritório) também é alocativa; transferir renda pelo "
            + rx("Bolsa Família") + " é distributiva; reduzir juros e ampliar gasto na recessão é estabilizadora.",
        ],
        "dissecando": (cz("[literalidade]") + " Exemplo canônico, sem modulador. O CEBRASPE costuma alternar, no "
                       "mesmo bloco, itens com a função certa e itens em que troca alocativa por distributiva ou "
                       "estabilizadora; o par “bens públicos ↔ alocativa” é o mais seguro de todos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A provisão de bens públicos é exemplo da função distributiva do Estado.”</i> → ERRADO (troca de "
            "conceito)",
            "<i>“Bens públicos caracterizam-se pela rivalidade no consumo e pela possibilidade de "
            "exclusão.”</i> → ERRADO (inversão: são não rivais e não excludentes)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Na tripartição de Musgrave, a provisão de bens públicos (não rivais e não excludentes), "
                            "subofertados pelo mercado por causa do carona, é o exemplo clássico da função alocativa.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0625-1 (função alocativa decorre da existência de bens públicos)"],
    },
    # ------------------------------------------------------------------ E3-L00038
    {
        "id": "ECO-E3-L00038-1", "fonte_ref": "E3-L00038", "destino": "47", "subtema": H2["fun"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_FUN,
        "rotulo_item": "Item",
        "assertiva": ("A função econômica estabilizadora do Estado busca suavizar as flutuações do ciclo econômico, "
                      "controlando a inflação e visando ao pleno emprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A função econômica estabilizadora do Estado busca <u>suavizar as flutuações do ciclo "
                      "econômico</u>, controlando a <u>inflação</u> e visando ao <u>pleno emprego</u>."),
        "poucas": ("A " + azb("função estabilizadora") + " usa as políticas fiscal e monetária para amortecer o "
                   "ciclo: " + vd("inflação controlada") + " e " + vd("emprego perto do pleno") + "."),
        "destrinchando": [
            MUSGRAVE,
            "Objetivos clássicos: " + vd("pleno emprego") + ", " + vd("estabilidade de preços") + ", "
            "equilíbrio do balanço de pagamentos e crescimento sustentado. Os dois primeiros podem entrar em "
            "conflito no curto prazo (curva de Phillips), o que exige dosar a política.",
            "Instrumentos: " + azb("política fiscal") + " (gasto, tributos, estabilizadores automáticos como IR "
            "progressivo e seguro-desemprego) e " + azb("política monetária") + " (juros, compulsório, mercado "
            "aberto). No " + rx("Brasil") + ", a monetária cabe ao " + rx("Banco Central") + ", autônomo desde "
            "a " + vd("LC 179/2021") + ", com mandato principal de estabilidade de preços e, como objetivos "
            "acessórios, suavizar o nível de atividade e fomentar o pleno emprego.",
            "Atuação simétrica: expansão na recessão, contenção no superaquecimento. Itens que restringem a "
            "estabilizadora “apenas” às recessões são ERRADO.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. O “visando ao” (objetivo, não garantia) e a "
                       "ausência de “apenas” mantêm o item verdadeiro. 🔥 No mesmo bloco, o CEBRASPE cobrou "
                       "“provisão de bens públicos = alocativa” (CERTO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A função estabilizadora do Estado busca corrigir a distribuição de renda resultante do "
            "mercado.”</i> → ERRADO (troca de conceito: é a distributiva)",
            "<i>“A função estabilizadora atua apenas em períodos recessivos.”</i> → ERRADO (restrição indevida)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["visando ao"], "dificuldade": 1,
        "comentario_fonte": "A estabilizadora (Musgrave) usa políticas fiscal e monetária para suavizar ciclos, "
                            "controlar a inflação e aproximar o emprego do pleno emprego.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00042
    {
        "id": "ECO-E3-L00042-1", "fonte_ref": "E3-L00042", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_POL,
        "rotulo_item": "Item",
        "assertiva": ("A política fiscal, um dos principais instrumentos de atuação governamental, controla a oferta "
                      "de moeda e os tributos na atividade econômica do país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A política fiscal, um dos principais instrumentos de atuação governamental, controla ")
                    + vm("a oferta de moeda") + az(" e os tributos na atividade econômica do país.")),
        "poucas": ("Política " + azb("fiscal") + " = " + vd("gastos e tributos") + ". O controle da "
                   + azb("oferta de moeda") + " é instrumento da política " + azb("monetária") + ", conduzida "
                   "pelo Banco Central."),
        "destrinchando": [
            azb("Política fiscal") + ": decisões sobre receitas (tributos) e despesas do governo, e o resultado "
            "que delas decorre (primário, nominal, dívida). No " + rx("Brasil") + ", é formulada pelo Executivo "
            "(Fazenda e Planejamento) e aprovada pelo Congresso no ciclo orçamentário (PPA, LDO, LOA).",
            azb("Política monetária") + ": controle da liquidez e dos juros — taxa básica (Selic), operações de "
            "mercado aberto, depósito compulsório, redesconto. No " + rx("Brasil") + ", cabe ao "
            + rx("Banco Central") + " sob o regime de metas de inflação definido pelo CMN.",
            "Pontos de contato que confundem: o déficit pode ser financiado por emissão de moeda (hoje vedado: "
            "o art. " + vd("164, § 1º, da Constituição") + " proíbe o BC de financiar o Tesouro), e a gestão da "
            "dívida pública afeta a liquidez. Mas emitir títulos para financiar o déficit é operação fiscal; "
            "comprá-los e vendê-los para regular a moeda é operação monetária.",
            vm("Regra-âncora: fiscal mexe em G e T; monetária mexe em M e i."),
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " O item junta um instrumento correto "
                       "(tributos) a um da política vizinha (oferta de moeda). A meia-verdade é a pista: quando "
                       "uma enumeração mistura instrumentos, confira cada um contra a política anunciada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política fiscal atua sobre a economia por meio dos gastos públicos e da tributação.”</i> → "
            "CERTO",
            "<i>“As operações de mercado aberto são instrumento da política fiscal.”</i> → ERRADO (troca de "
            "conceito: são monetárias)",
        ])],
        "reescrita": ("A política fiscal, um dos principais instrumentos de atuação governamental, controla "
                      + hl("os gastos públicos") + " e os tributos na atividade econômica do país."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A assertiva mistura política fiscal (gastos e tributos) e monetária (oferta de moeda e "
                            "juros, a cargo do Banco Central). Um dos comentários empilhados afirma, sem fonte, que o "
                            "gabarito oficial seria CERTO.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: um dos seis comentários da fonte afirma que o gabarito oficial foi CERTO; os "
                    "demais e a indicação principal dão ERRADO, coerente com o conteúdo — conferir no gabarito "
                    "definitivo do CEBRASPE (TJ/PA 2025, item 86)"],
    },
    # ------------------------------------------------------------------ E3-L00050
    {
        "id": "ECO-E3-L00050-1", "fonte_ref": "E3-L00050", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("A estrutura tributária brasileira é eminentemente progressiva, ou seja, a proporção da renda "
                      "destinada aos impostos aumenta conforme a renda do contribuinte diminui."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A estrutura tributária brasileira é eminentemente ") + vm("progressiva") + az(", ou seja, a "
                       "proporção da renda destinada aos impostos aumenta conforme a renda do contribuinte "
                       "diminui.")),
        "poucas": ("O sistema brasileiro é " + azb("regressivo") + " — e a própria explicação do item (a carga "
                   "pesa mais conforme a renda diminui) é a definição de " + azb("regressividade") + ", não de "
                   "progressividade."),
        "destrinchando": [
            "Definições, sempre pela " + azb("alíquota média") + " (imposto ÷ renda): " + azb("progressivo")
            + " → a proporção cresce com a renda; " + azb("proporcional") + " → constante; "
            + azb("regressivo") + " → cai com a renda (pesa mais nos pobres).",
            "Por que o " + rx("Brasil") + " é regressivo: a carga se apoia em " + vd("tributos sobre bens e "
                                                                                     "serviços") + " (ICMS, "
            "PIS/Cofins, IPI, ISS), que respondem pela maior fatia da arrecadação. Como os mais pobres consomem "
            "quase toda a renda, pagam proporcionalmente mais.",
            "A parte progressiva (IRPF com faixas) pesa pouco: base estreita, isenção histórica de lucros e "
            "dividendos distribuídos (desde " + vd("1995") + ") e tributação baixa sobre patrimônio e "
            "herança. Estudos do " + rx("Ipea") + " e da Receita confirmam carga proporcionalmente maior nos "
            "decis de menor renda.",
            "⏳ (out/2026) Mudanças em curso: a " + vd("EC 132/2023") + " cria o IVA dual (CBS e IBS), com "
            "transição a partir de 2026 e cashback para famílias de baixa renda; a reforma do IR aprovada em 2025 "
            "isentou rendas mensais até R$ 5 mil e instituiu imposto mínimo sobre altas rendas. O efeito sobre a "
            "regressividade ainda depende da implantação.",
            vm("Regra-âncora: tributação indireta pesada → sistema regressivo."),
        ],
        "dissecando": (cz("[troca de conceito · contradição]") + " O item rotula o sistema como progressivo e, no "
                       "“ou seja”, descreve a regressividade: a definição contradiz o rótulo. O conteúdo descrito "
                       "é verdadeiro para o Brasil; o erro está só na palavra “progressiva”. 🔥 O CEBRASPE gosta "
                       "de testar se o candidato confere a definição que o próprio item oferece."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A estrutura tributária brasileira é eminentemente regressiva, em razão do peso dos tributos "
            "indiretos sobre o consumo.”</i> → CERTO",
            "<i>“Um tributo é progressivo quando sua alíquota média cai à medida que a renda aumenta.”</i> → "
            "ERRADO (inversão: isso é regressividade)",
        ])],
        "reescrita": ("A estrutura tributária brasileira é eminentemente " + hl("regressiva") + ", ou seja, a "
                      "proporção da renda destinada aos impostos aumenta conforme a renda do contribuinte diminui."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": ["eminentemente"], "dificuldade": 1,
        "comentario_fonte": "O sistema brasileiro é regressivo: predomínio de tributos indiretos sobre o consumo, "
                            "que pesam mais nos mais pobres; o IRPF progressivo não reverte o quadro.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
