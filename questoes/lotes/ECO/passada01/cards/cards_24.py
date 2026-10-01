"""Cards da redação ECO — passada 01 — lote 24 (nota 12 — Falhas de mercado, externalidades, tipos de bens e
informações assimétricas)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "ext": "🌫️ Externalidades e Coase",
    "bens": "🏞️ Bens públicos e comuns",
    "info": "🕵️ Informação assimétrica",
    "reg": "🏛️ Falhas de governo e regulação",
}

COM_BENS = "Acerca dos bens públicos e da classificação dos bens na teoria econômica, julgue o item a seguir."
COM_EXT = "A respeito das externalidades e de suas formas de correção, julgue o item a seguir."
COM_FALHAS = "Acerca das falhas de mercado e da atuação do governo na economia, julgue o item a seguir."
COM_INFO = "A respeito da informação assimétrica e de seus efeitos sobre os mercados, julgue o item a seguir."
COM_REG = "Acerca da regulação econômica e das falhas de governo, julgue o item a seguir."


def _base(rid, sub, comando):
    return {"id": f"ECO-{rid}-1", "fonte_ref": rid, "destino": "12", "subtema": H2[sub], "tipo": "C/E",
            "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
            "comando": comando, "rotulo_item": "Item", "gabarito_origem": "fonte", "status": "normal"}


def _img(ref, acao="irrecuperavel"):
    return {"ref": ref, "tipo_fonte": "não preservada", "lado": "verso", "acao": acao}


TABELA_BENS = ("Quadro clássico (" + oc("Mankiw") + "): " + azb("bens privados") + " (excludentes e rivais: "
               "sorvete, roupa); " + azb("monopólios naturais / bens de clube") + " (excludentes, não rivais: TV "
               "a cabo, estrada com pedágio vazia); " + azb("recursos comuns") + " (não excludentes, rivais: "
               "peixes no oceano, pastagem aberta); " + azb("bens públicos") + " (não excludentes e não rivais: "
               "defesa nacional, farol, iluminação pública).")

CARDS = [
    # ------------------------------------------------------------------ E1-0324
    dict(_base("E1-0324", "bens", COM_BENS), **{
        "assertiva": ("No que se refere à promoção da mudança tecnológica, a pesquisa básica é um bem público. Isso "
                      "significa que as externalidades provenientes da pesquisa básica são tão grandes que podem "
                      "ser consideradas um bem não-excludente e não rival."),
        "gabarito": "CERTO",
        "anotada": az("No que se refere à promoção da mudança tecnológica, a pesquisa básica é um "
                      "<u>bem público</u>. Isso significa que as externalidades provenientes da pesquisa básica "
                      "são tão grandes que podem ser consideradas um bem <u>não-excludente e não rival</u>."),
        "poucas": ("O conhecimento gerado pela " + azb("pesquisa básica") + " é " + azb("não rival") + " (uma "
                   "ideia usada por um não se esgota para os demais) e, uma vez publicado, " + azb("não excludente")
                   + ": é o exemplo de manual de bem público."),
        "destrinchando": [
            "Um teorema matemático ou uma descoberta sobre a estrutura da célula pode ser usado por qualquer "
            "pesquisador ou empresa, ao mesmo tempo, sem que o conhecimento se “gaste”: " + azb("não rivalidade")
            + ". E, divulgado o resultado, não há como cobrar de cada usuário: " + azb("não exclusão") + ".",
            "Consequência: quem financia a pesquisa básica gera um enorme " + azb("transbordamento") + " "
            "(externalidade positiva) que não consegue apropriar. Sozinho, o mercado investe menos do que o "
            "socialmente ótimo — o problema do " + azb("carona") + ".",
            "Respostas de política: financiamento público direto (agências como " + rx("CNPq, CAPES e FINEP")
            + " no Brasil; NIH e NSF nos EUA), universidades públicas e subsídios fiscais à P&D.",
            "Contraste com a " + azb("pesquisa aplicada") + ": o resultado pode virar produto patenteável. A "
            "patente cria " + azb("exclusão artificial") + " temporária, transformando o conhecimento em algo "
            "parecido com um bem de clube — incentivo ao inventor ao custo de um monopólio temporário.",
            vm("Regra-âncora: conhecimento geral = bem público; conhecimento patenteado = exclusão artificial."),
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " O item reproduz a lição de manual (" + oc("Mankiw")
                       + ", capítulo de bens públicos e recursos comuns) sobre pesquisa básica. A redação "
                       "“externalidades tão grandes que podem ser consideradas um bem” soa estranha e convida ao "
                       "ERRADO, mas o núcleo — não excludente e não rival — está certo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A pesquisa aplicada protegida por patente é um bem público puro.”</i> → ERRADO (a patente "
            "torna o conhecimento excludente)",
            "<i>“Por ser bem público, a pesquisa básica tende a ser suprida em quantidade excessiva pelo "
            "mercado.”</i> → ERRADO (inversão: tende à suboferta)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": ("A pesquisa básica é tipicamente não-excludente e não-rival, apresentando fortes "
                             "externalidades positivas."),
        "qualidade_fonte": "raso", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0325
    dict(_base("E1-0325", "bens", COM_BENS), **{
        "assertiva": ("De acordo com a teoria econômica, bens públicos são bens cujo consumo é não excludente e não "
                      "rival."),
        "gabarito": "CERTO",
        "anotada": az("De acordo com a teoria econômica, bens públicos são bens cujo consumo é "
                      "<u>não excludente e não rival</u>."),
        "poucas": ("É a definição de " + oc("Samuelson") + " (1954): bem público puro reúne " + azb("não exclusão")
                   + " (não dá para impedir quem não paga) e " + azb("não rivalidade") + " (o consumo de um não "
                   "reduz o dos outros)."),
        "destrinchando": [
            azb("Exclusão") + " é uma questão de tecnologia e de custo: é possível (barato) impedir alguém de "
            "consumir? " + azb("Rivalidade") + " é uma questão física: o que eu consumo deixa de estar "
            "disponível para você?",
            TABELA_BENS,
            "O critério é o <b>consumo</b>, não quem produz: a escola pública é rival e excludente (vaga "
            "limitada) e, portanto, não é bem público no sentido econômico; um software livre produzido por uma "
            "empresa privada pode ser quase público.",
            "Na prática há " + azb("bens públicos impuros") + ": uma estrada é não rival até congestionar; um "
            "parque é não excludente, mas pode lotar.",
            vm("Regra-âncora: bem público = não exclusão + não rivalidade, independentemente de quem o produz."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição pura, sem armadilha. A banca costuma montar o par "
                       "certo/errado trocando as duas características (“excludente e rival”) ou trocando o "
                       "critério do consumo pelo da propriedade (“bens produzidos pelo Estado”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens públicos são aqueles produzidos ou fornecidos pelo Estado.”</i> → ERRADO (critério "
            "trocado: propriedade em vez de consumo)",
            "<i>“Recursos comuns são não excludentes, mas rivais no consumo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Definição clássica: não exclusão e não rivalidade. Exemplos: defesa nacional, "
                             "iluminação pública."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0326
    dict(_base("E1-0326", "bens", COM_BENS), **{
        "assertiva": ("De acordo com a teoria econômica, bens públicos são bens cujo consumo é excludente e rival, "
                      "independentemente de quem os produz ou comercializa."),
        "gabarito": "ERRADO",
        "anotada": (az("De acordo com a teoria econômica, bens públicos são bens cujo consumo é ")
                    + vm("excludente e rival") + az(", independentemente de quem os produz ou comercializa.")),
        "poucas": ("Excludente e rival é o " + azb("bem privado") + ". O bem público é o oposto nas duas "
                   "dimensões: " + vd("não excludente e não rival") + "."),
        "destrinchando": [
            TABELA_BENS,
            "A segunda parte do item está certa e é importante: a classificação depende das características "
            "do <b>consumo</b>, não de quem produz ou vende. Um bem produzido pelo Estado pode ser privado no "
            "sentido econômico (energia elétrica de estatal) e um bem fornecido por particular pode ser público "
            "(farol mantido por associação de armadores).",
            "Por que importa: só no bem privado o mercado aloca bem sozinho, porque quem não paga fica de fora "
            "(exclusão) e cada unidade consumida tem custo de oportunidade (rivalidade). Sem essas "
            "propriedades, o preço deixa de funcionar como racionador e sinalizador.",
            vm("Regra-âncora: bem privado = excludente + rival; bem público = nenhum dos dois."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item copia a estrutura da definição verdadeira e troca as "
                       "duas propriedades pelas do bem privado; a cauda verdadeira (“independentemente de quem os "
                       "produz”) dá credibilidade ao todo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens privados são bens cujo consumo é excludente e rival, independentemente de quem os produz "
            "ou comercializa.”</i> → CERTO",
            "<i>“Bens públicos são excludentes, mas não rivais.”</i> → ERRADO (essa é a definição de bem de "
            "clube)",
        ])],
        "reescrita": ("De acordo com a teoria econômica, bens públicos são bens cujo consumo é "
                      + hl("não excludente e não rival") + ", independentemente de quem os produz ou "
                      "comercializa."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["independentemente"], "dificuldade": 1,
        "comentario_fonte": "A excludência e a rivalidade caracterizam bens privados, não bens públicos.",
        "qualidade_fonte": "raso", "figuras_fonte": [_img("Untitled (75).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0328
    dict(_base("E1-0328", "bens", COM_BENS), **{
        "assertiva": ("Uma característica básica dos bens públicos é que apresentam custo marginal de produção "
                      "igual a zero para um consumidor adicional."),
        "gabarito": "CERTO",
        "anotada": az("Uma característica básica dos bens públicos é que apresentam custo marginal de produção "
                      "igual a zero <u>para um consumidor adicional</u>."),
        "poucas": ("É a " + azb("não rivalidade") + " em linguagem de custos: atender <b>mais um consumidor</b> "
                   "não exige produzir mais, logo o custo marginal desse consumidor é " + vd("zero") + "."),
        "destrinchando": [
            "Distinga dois custos marginais. O de <b>produzir mais uma unidade</b> do bem (mais um poste, mais "
            "um navio de guerra) é positivo. O de <b>servir mais um consumidor</b> com a quantidade já "
            "produzida é nulo: o morador que se muda para a rua iluminada não aumenta a conta de luz. É este "
            "segundo que o item descreve.",
            "Consequência normativa: se o custo marginal do consumidor adicional é zero, a eficiência pede "
            + azb("preço zero") + " para o uso (P = CMg). Cobrar pelo acesso — mesmo quando é possível excluir — "
            "afasta quem tem benefício positivo e gera peso morto.",
            "Por isso o financiamento eficiente vem de " + azb("tributos gerais") + ", não de tarifa de uso; e "
            "a quantidade ótima é dada pela " + azb("condição de Samuelson") + ": a <b>soma vertical</b> dos "
            "benefícios marginais de todos os consumidores igual ao custo marginal de produção.",
            "Com congestionamento (estrada lotada), o custo marginal do usuário adicional deixa de ser zero — o "
            "bem vira impuro e o pedágio de congestionamento pode ser eficiente.",
        ],
        "dissecando": (cz("[detalhe]") + " A expressão “custo marginal de produção” assusta quem pensa no custo "
                       "de fabricar mais uma unidade; o qualificador “para um consumidor adicional” salva o item. "
                       "Leia sempre até o fim o complemento do custo marginal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como o custo marginal de servir um consumidor adicional é nulo, o preço eficiente pelo uso de "
            "um bem público não congestionado é zero.”</i> → CERTO",
            "<i>“Bens públicos têm custo de produção nulo.”</i> → ERRADO (generalização: só o custo do "
            "consumidor adicional é nulo)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O custo marginal de permitir que mais uma pessoa consuma o bem público é zero (ex.: "
                             "iluminação pública)."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0329
    dict(_base("E1-0329", "bens", COM_BENS), **{
        "assertiva": "Uma característica básica dos bens públicos é que as pessoas podem ser impedidas de consumi-los.",
        "gabarito": "ERRADO",
        "anotada": (az("Uma característica básica dos bens públicos é que as pessoas ")
                    + vm("podem ser impedidas") + az(" de consumi-los.")),
        "poucas": ("Poder impedir o consumo é a " + azb("excludabilidade") + ", traço do bem privado e do bem de "
                   "clube. O bem público é " + vd("não excludente") + "."),
        "destrinchando": [
            "Não exclusão significa que é impossível — ou proibitivamente caro — impedir que alguém usufrua do "
            "bem depois de ofertado: não se pode deixar uma casa fora da proteção da defesa nacional nem "
            "apagar o farol para o navio que não pagou.",
            "É a não exclusão que gera o " + azb("problema do carona") + ": se não posso ser impedido de usar, "
            "não tenho incentivo para pagar. Daí a " + azb("suboferta") + " pelo mercado e a justificativa "
            "para o provimento público financiado por impostos.",
            "A exclusão pode mudar com a tecnologia: a TV aberta era não excludente; o sinal codificado da TV "
            "por assinatura a tornou excludente (bem de clube). Por isso a classificação não é eterna.",
            vm("Regra-âncora: poder excluir → privado ou clube; não poder excluir → público ou recurso comum."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Inverte a não exclusão. A banca costuma alternar, no mesmo "
                       "bloco, um item verdadeiro (custo marginal zero para o consumidor adicional) e um falso "
                       "como este, que atribui ao bem público a propriedade do bem privado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma característica básica dos bens de clube é que as pessoas podem ser impedidas de "
            "consumi-los.”</i> → CERTO",
        ])],
        "reescrita": ("Uma característica básica dos bens públicos é que as pessoas " + hl("não podem")
                      + " ser impedidas de consumi-los."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": ("Bens públicos são não excludentes: não é possível impedir o acesso, mesmo de quem não "
                             "paga."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (83).jpeg")], "alertas": [],
    }),
]
