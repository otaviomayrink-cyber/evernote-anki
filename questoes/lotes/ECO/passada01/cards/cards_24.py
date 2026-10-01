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
    # ------------------------------------------------------------------ E1-0330
    dict(_base("E1-0330", "bens", COM_BENS), **{
        "assertiva": ("Uma situação passível de consideração na análise dos tipos de bens é a figura do “carona”. Ele "
                      "dificulta a oferta eficiente de bens pelos mercados."),
        "gabarito": "CERTO",
        "anotada": az("Uma situação passível de consideração na análise dos tipos de bens é a figura do “carona”. "
                      "Ele <u>dificulta</u> a oferta eficiente de bens pelos mercados."),
        "poucas": ("O " + azb("carona") + " (<i>free rider</i>) usufrui do bem não excludente sem pagar; como "
                   "todos têm esse incentivo, a receita privada não cobre o custo e o mercado " + vd("oferta "
                   "menos que o ótimo") + " — ou nada."),
        "destrinchando": [
            "Exemplo clássico: o farol. Todo navio que passa se beneficia da luz, mas nenhum armador quer "
            "pagar sozinho, porque o farol aceso servirá também a quem não pagou. Resultado provável: farol "
            "nenhum, embora o benefício somado de todos supere o custo.",
            "A raiz do carona é a " + azb("não exclusão") + ": se fosse possível excluir quem não paga, cada "
            "um revelaria sua disposição a pagar. Sem exclusão, as pessoas " + azb("escondem a preferência")
            + " — esperam que os outros financiem.",
            "Soluções: provimento público financiado por " + azb("tributos compulsórios") + " (o imposto "
            "elimina a opção de não pagar); tecnologias de exclusão (sinal codificado, pedágio); normas sociais "
            "e reputação em grupos pequenos.",
            "Contraponto empírico: " + oc("Coase") + " (“The Lighthouse in Economics”, 1974) mostrou que faróis "
            "ingleses foram financiados por taxas portuárias cobradas dos navios — a exclusão se fazia no "
            "porto. O carona dificulta, mas nem sempre impede, a oferta privada.",
            vm("Regra-âncora: não exclusão → carona → suboferta privada → provisão via tributos."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O verbo “dificulta” é a medida certa: o "
                       "carona torna a oferta privada ineficiente, não necessariamente impossível. Desconfie de "
                       "versões com “impede” ou “inviabiliza totalmente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O problema do carona decorre da rivalidade no consumo dos bens públicos.”</i> → ERRADO (troca: "
            "decorre da não exclusão)",
            "<i>“O carona impede, em qualquer circunstância, a provisão privada de bens públicos.”</i> → ERRADO "
            "(modulador absoluto)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["dificulta"], "dificuldade": 1,
        "comentario_fonte": ("A não exclusão leva ao problema do carona; isso inviabiliza o financiamento privado "
                             "eficiente, levando à suboferta do bem público."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (78).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0331
    dict(_base("E1-0331", "bens", COM_BENS), **{
        "assertiva": ("No tocante aos bens públicos: observada a característica de não exclusividade, falhas "
                      "alocativas podem ocorrer em função dos chamados “consumidores caronas”, isto é, aqueles que "
                      "não pagam pelo bem, na expectativa de que outros o façam."),
        "gabarito": "CERTO",
        "anotada": az("No tocante aos bens públicos: observada a característica de <u>não exclusividade</u>, "
                      "falhas alocativas podem ocorrer em função dos chamados “consumidores caronas”, isto é, "
                      "aqueles que não pagam pelo bem, na expectativa de que outros o façam."),
        "poucas": ("O item liga corretamente a causa (" + azb("não exclusão") + ") ao efeito (" + azb("carona")
                   + ") e à consequência (" + azb("falha alocativa") + ": suboferta do bem)."),
        "destrinchando": [
            "“Não exclusividade” é sinônimo de não exclusão (ou não excludabilidade) na literatura de finanças "
            "públicas: não se consegue impedir o uso por quem não contribuiu.",
            "Lógica do carona como dilema dos prisioneiros: para cada indivíduo, não contribuir é a estratégia "
            "dominante (se os outros pagam, usufruo de graça; se não pagam, minha contribuição sozinha não "
            "basta). Se todos raciocinam assim, o bem não é provido, embora todos preferissem que fosse.",
            azb("Falha alocativa") + ": a quantidade fornecida pelo mercado fica abaixo da ótima de "
            + oc("Samuelson") + " (soma dos benefícios marginais = custo marginal). É uma das razões clássicas da "
            + azb("função alocativa") + " do governo na tipologia de " + oc("Musgrave") + " (alocativa, "
            "distributiva e estabilizadora).",
            "O problema cresce com o tamanho do grupo: em grupos pequenos, a pressão social e a percepção de "
            "que a própria contribuição faz diferença atenuam o carona (" + oc("Mancur Olson") + ", <i>A lógica "
            "da ação coletiva</i>, 1965).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Encadeamento correto característica → comportamento → falha, "
                       "suavizado por “podem ocorrer”. A versão errada típica troca a característica de origem "
                       "(“observada a rivalidade…”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Observada a característica de não rivalidade, os caronas tornam impossível excluir quem não "
            "paga.”</i> → ERRADO (troca de conceito: a impossibilidade de excluir é a não exclusão)",
        ]), ("🃏 Carta na manga", [
            "Na escala internacional, o mesmo raciocínio explica a dificuldade de financiar " + azb("bens públicos "
            "globais") + " (estabilidade climática, combate a pandemias): cada país tende a pegar carona no "
            "esforço dos demais.",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": ("A não exclusividade permite o comportamento do free rider, gerando falhas de mercado e "
                             "suboferta do bem público."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (77).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0349
    dict(_base("E1-0349", "bens", COM_FALHAS), **{
        "assertiva": ("As falhas de mercado impedem a máxima eficiência na alocação de recursos. Um bem não rival pode "
                      "ser subofertado em virtude de o custo marginal de produção do bem exceder o seu benefício "
                      "marginal social."),
        "gabarito": "ERRADO",
        "anotada": (az("As falhas de mercado impedem a máxima eficiência na alocação de recursos. Um bem não rival "
                       "pode ser subofertado em virtude de ") + vm("o custo marginal de produção do bem exceder o "
                       "seu benefício marginal social") + az(".")),
        "poucas": ("Se o custo marginal supera o " + azb("benefício marginal social") + ", produzir menos é o "
                   "<b>eficiente</b>, não suboferta. A suboferta do bem não rival ocorre quando o benefício social "
                   + vd("supera") + " o custo, mas o mercado não o capta."),
        "destrinchando": [
            "Regra geral de eficiência: produzir enquanto " + vd("BMg social ≥ CMg") + ". Onde CMg > BMgS, cada "
            "unidade a mais destrói valor — deixar de produzi-la é exatamente o que um planejador benevolente "
            "faria. Não há falha alguma nisso.",
            azb("Suboferta") + " significa quantidade abaixo do ótimo, ou seja, unidades que <b>valem mais do "
            "que custam</b> e mesmo assim não são produzidas. No bem não rival, isso acontece porque o "
            "benefício social é a <b>soma vertical</b> dos benefícios de todos os que usufruem (condição de "
            + oc("Samuelson") + "), mas cada comprador só paga pelo próprio benefício — e, sem exclusão, nem "
            "isso (carona).",
            "Em termos de custo, a não rivalidade joga a favor da produção: o custo de servir um usuário "
            "adicional é zero, de modo que o benefício social de cada unidade tende a ser alto relativamente "
            "ao custo.",
            vm("Regra-âncora: suboferta = BMg social > CMg sem que o mercado produza; nunca o contrário."),
        ],
        "dissecando": (cz("[inversão]") + " A frase inicial (verdadeira) dá o tom técnico; o erro está na "
                       "condição invertida: CMg > BMgS descreve o ponto em que parar de produzir é ótimo. Pista: "
                       "“subofertado” só faz sentido se o benefício superar o custo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um bem não rival pode ser subofertado em virtude de o seu benefício marginal social exceder o "
            "benefício marginal privado de cada comprador.”</i> → CERTO",
        ])],
        "reescrita": ("As falhas de mercado impedem a máxima eficiência na alocação de recursos. Um bem não rival "
                      "pode ser subofertado em virtude de " + hl("o seu benefício marginal social exceder o "
                      "benefício marginal privado de cada comprador, que é o que o mercado capta") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("Em bens não rivais o custo marginal é próximo de zero; o problema é o contrário: o "
                             "benefício social excede o custo, mas há suboferta por causa da não exclusividade."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0354
    dict(_base("E1-0354", "bens", COM_FALHAS), **{
        "assertiva": ("A existência de bens públicos conforma uma falha de mercado, pois a natureza rival (ou "
                      "indivisível) deste tipo de bem acarreta suboferta pelo mercado."),
        "gabarito": "ERRADO",
        "anotada": (az("A existência de bens públicos conforma uma falha de mercado, pois a natureza ")
                    + vm("rival") + az(" (ou indivisível) deste tipo de bem acarreta suboferta pelo mercado.")),
        "poucas": ("Bem público é " + vd("não rival") + " — e é essa natureza, somada à não exclusão, que leva o "
                   "mercado à suboferta. O item troca “não rival” por “rival”."),
        "destrinchando": [
            "A primeira parte é correta: bens públicos são uma das falhas de mercado clássicas, ao lado de "
            "externalidades, poder de mercado e informação assimétrica.",
            "“Indivisível” é a palavra certa no lugar errado: na tradição de " + oc("Musgrave") + ", bem público "
            "tem " + azb("consumo indivisível") + " (conjunto) — todos consomem a mesma unidade ao mesmo tempo. "
            "Isso é justamente a <b>não rivalidade</b>; o parêntese contradiz o adjetivo “rival”.",
            "Divisão de papéis das duas propriedades: a " + azb("não exclusão") + " gera o carona e esconde a "
            "disposição a pagar (causa direta da suboferta); a " + azb("não rivalidade") + " faz com que "
            "excluir alguém, mesmo quando possível, seja ineficiente (custo marginal do usuário extra = 0).",
            "Bens rivais e não excludentes são os " + azb("recursos comuns") + ", cujo problema é o oposto: "
            "<b>sobreuso</b> (tragédia dos comuns, " + oc("Hardin") + ", 1968), não suboferta.",
            vm("Regra-âncora: bem público → não rival e não excludente → suboferta; recurso comum → rival → "
               "sobreuso."),
        ],
        "dissecando": (cz("[troca de conceito · contradição]") + " Basta trocar um prefixo (“não rival” → "
                       "“rival”) para falsear a definição; o parêntese “ou indivisível” — sinônimo de consumo "
                       "conjunto — é a pista de que a palavra anterior foi adulterada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Recursos comuns, por serem rivais e não excludentes, tendem a ser sobreutilizados.”</i> → CERTO",
            "<i>“A rivalidade dos bens públicos gera o problema do carona.”</i> → ERRADO (troca: o carona vem da "
            "não exclusão)",
        ])],
        "reescrita": ("A existência de bens públicos conforma uma falha de mercado, pois a natureza "
                      + hl("não rival") + " (ou indivisível) " + hl("e não excludente") + " deste tipo de bem "
                      "acarreta suboferta pelo mercado."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A suboferta se deve à não rivalidade e não exclusividade, não à rivalidade; "
                             "justificativa nas externalidades positivas e no carona."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0332
    dict(_base("E1-0332", "ext", COM_EXT), **{
        "assertiva": ("Na presença de externalidades negativas, um imposto pode alinhar o benefício marginal privado "
                      "ao custo marginal social."),
        "gabarito": "CERTO",
        "anotada": az("Na presença de externalidades negativas, um <u>imposto</u> pode alinhar o benefício marginal "
                      "privado ao <u>custo marginal social</u>."),
        "poucas": ("É o " + azb("imposto de Pigou") + ": cobrando do poluidor o dano marginal, o custo privado "
                   "passa a refletir o social, e o mercado para onde " + vd("BMg = CMgS") + " — o ótimo."),
        "destrinchando": [
            "Na externalidade negativa de produção, " + vd("CMgS = CMgP + dano marginal externo") + ". A firma "
            "decide olhando só o CMgP; o mercado iguala o benefício marginal (a demanda) ao CMgP e produz "
            "<b>demais</b> (Qₘ > Q*).",
            "O " + azb("imposto pigouviano") + " (" + oc("Pigou") + ", <i>The Economics of Welfare</i>, 1920) "
            "fixa t igual ao dano marginal no ótimo. A oferta sobe de CMgP para CMgP + t = CMgS, e o novo "
            "equilíbrio iguala o benefício marginal ao custo marginal <b>social</b>: a externalidade foi "
            + azb("internalizada") + ".",
            "Exemplo: o " + azb("imposto sobre carbono") + " cobra por tonelada de CO₂ emitida; a empresa passa "
            "a comparar o custo de abater emissões com o imposto e escolhe a forma mais barata de reduzir. "
            "Alternativa de mesmo efeito: mercado de licenças negociáveis (" + azb("cap and trade") + "), que "
            "fixa a quantidade e deixa o preço flutuar.",
            "Na externalidade positiva, o espelho é o " + azb("subsídio pigouviano") + " (vacinação, P&D).",
            vm("Regra-âncora: externalidade negativa → produção excessiva → imposto = dano marginal."),
        ],
        "grafico_verso": "ECO-E1-0332-1-V1",
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " A formulação é pouco usual — o imposto "
                       "atua sobre o <b>custo</b> privado, não sobre o benefício —, mas o resultado descrito é "
                       "exato: no novo equilíbrio, BMg privado = CMg social. O “pode” cobre a condição de o "
                       "imposto ser calibrado no dano marginal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na presença de externalidades negativas, um subsídio à produção alinha o custo privado ao "
            "social.”</i> → ERRADO (instrumento invertido: subsídio é para externalidade positiva)",
            "<i>“O imposto pigouviano ótimo é igual ao dano marginal externo na quantidade eficiente.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("Imposto de Pigou internaliza o custo social; exemplo do imposto sobre emissões de "
                             "CO₂."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [_img("Untitled (85).jpeg", "irrecuperavel (mecanismo redesenhado em ECO-E1-0332-1-V1)")],
        "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0334
    dict(_base("E1-0334", "ext", COM_EXT), **{
        "assertiva": "O Teorema de Coase aplica-se a negociações entre particulares, sem custos para as partes envolvidas.",
        "gabarito": "CERTO",
        "anotada": az("O Teorema de Coase aplica-se a <u>negociações entre particulares</u>, <u>sem custos</u> "
                      "para as partes envolvidas."),
        "poucas": ("O " + azb("Teorema de Coase") + " vale para barganha privada com " + vd("custos de transação "
                   "nulos") + " e direitos de propriedade bem definidos: aí as partes chegam sozinhas ao resultado "
                   "eficiente."),
        "destrinchando": [
            "Enunciado (" + oc("Ronald Coase") + ", “The Problem of Social Cost”, 1960; Nobel de 1991): se os "
            "direitos de propriedade estão definidos e negociar não custa nada, as partes negociam até o nível "
            "eficiente da atividade geradora da externalidade, " + azb("qualquer que seja") + " a parte a quem "
            "o direito foi atribuído. A atribuição muda só a distribuição da renda (quem paga a quem).",
            "Exemplo: fábrica que polui um rio usado por pescadores. Se o direito é da fábrica, os pescadores "
            "lhe pagam para reduzir a poluição enquanto o dano evitado superar o lucro perdido; se é dos "
            "pescadores, a fábrica lhes paga para poluir enquanto o lucro superar o dano. Mesmo nível final.",
            azb("Custos de transação") + " incluem identificar as partes, medir o dano, negociar, redigir e "
            "fazer cumprir o contrato. Com muitas partes (poluição do ar de uma cidade), eles explodem — e o "
            "carona aparece. Por isso o teorema serve sobretudo como " + azb("referência") + ": mostra que o "
            "problema real são os custos de transação.",
            vm("Regra-âncora: Coase = direitos definidos + custo de transação zero → eficiência pela barganha, "
               "independentemente de quem detém o direito."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " “Sem custos para as partes” é a paráfrase leiga de “custos de "
                       "transação nulos”. 🔥 As versões erradas costumam afirmar que o teorema exige intervenção "
                       "estatal, que a eficiência depende de a quem cabe o direito ou que funciona com muitos "
                       "agentes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo Teorema de Coase, o nível eficiente de poluição depende de a qual parte o direito de "
            "propriedade é atribuído.”</i> → ERRADO (a atribuição afeta só a distribuição)",
            "<i>“O Teorema de Coase pressupõe a cobrança de um imposto pigouviano.”</i> → ERRADO (troca de "
            "conceito: a solução é a barganha privada)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Pressupõe negociação privada sem custos de transação, com direitos de propriedade "
                             "bem definidos; o resultado é eficiente."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (80).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0335
    dict(_base("E1-0335", "ext", COM_EXT), **{
        "assertiva": ("Duas empresas enfrentam uma situação de conflito sobre poluição. Segundo o Teorema de Coase: a "
                      "definição de quem tem direito sobre a poluição pode possibilitar negociação que objetive "
                      "alcançar o nível ótimo de emissão de poluição."),
        "gabarito": "CERTO",
        "anotada": az("Duas empresas enfrentam uma situação de conflito sobre poluição. Segundo o Teorema de Coase: "
                      "a <u>definição de quem tem direito</u> sobre a poluição pode possibilitar negociação que "
                      "objetive alcançar o nível ótimo de emissão de poluição."),
        "poucas": ("É o núcleo do teorema: definidos os " + azb("direitos de propriedade") + " (e com custos de "
                   "transação baixos), as duas empresas barganham até o " + vd("nível eficiente") + " de "
                   "emissão."),
        "destrinchando": [
            "Sem direito definido, ninguém sabe quem deve pagar a quem, e a negociação não começa. Definido o "
            "direito, ele vira um ativo negociável: quem valoriza mais o uso do recurso (poluir ou ter ar/água "
            "limpos) compra o direito do outro.",
            "Exemplo numérico: poluir rende 100 à empresa A e causa dano de 150 à empresa B. Se A tem o "
            "direito, B paga entre 100 e 150 para A parar; se B tem o direito, A não consegue pagar 150 e não "
            "polui. Em ambos os casos, " + vd("não há poluição") + " — o resultado eficiente —; muda apenas quem "
            "fica com o excedente.",
            "Com " + vd("duas") + " empresas o cenário é o mais favorável ao teorema: partes identificáveis, "
            "poucas e com incentivo a negociar. Por isso o exemplo de manual é sempre bilateral (fazendeiro × "
            "rancheiro, fábrica × lavanderia).",
            "Limites: custos de transação altos, informação assimétrica sobre custos e danos (cada lado "
            "exagera) e comportamento estratégico podem travar a barganha.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " “Pode possibilitar” e “objetive alcançar” "
                       "são moduladores prudentes que tornam o item inatacável. O item-irmão do mesmo bloco troca "
                       "a negociação por um teto imposto — que é comando e controle, não Coase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o Teorema de Coase, apenas a atribuição do direito à empresa poluída garante o nível "
            "ótimo de emissão.”</i> → ERRADO (restrição indevida: qualquer atribuição leva ao ótimo)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "objetive"],
        "dificuldade": 1,
        "comentario_fonte": ("Com direitos de propriedade claros e custos de transação nulos, as partes negociam até "
                             "o nível eficiente de poluição."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (79).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0336
    dict(_base("E1-0336", "ext", COM_EXT), **{
        "assertiva": ("Duas empresas enfrentam uma situação de conflito sobre poluição. Segundo o Teorema de Coase: "
                      "deve ser imposta a quantidade máxima de quanto pode ser emitido de poluição por cada uma das "
                      "duas empresas."),
        "gabarito": "ERRADO",
        "anotada": (az("Duas empresas enfrentam uma situação de conflito sobre poluição. Segundo o Teorema de "
                       "Coase: ") + vm("deve ser imposta a quantidade máxima de quanto pode ser emitido de "
                       "poluição por cada uma das duas empresas") + az(".")),
        "poucas": ("Teto imposto a cada empresa é " + azb("regulação de comando e controle") + ". Coase propõe o "
                   "contrário: definir direitos e deixar as partes " + vd("negociarem") + " o nível de emissão."),
        "destrinchando": [
            "Três famílias de solução para externalidades: (1) " + azb("comando e controle") + " — o Estado fixa "
            "limites, padrões tecnológicos ou proibições; (2) " + azb("instrumentos de mercado") + " — imposto "
            "pigouviano, subsídio, licenças negociáveis; (3) " + azb("solução privada") + " de " + oc("Coase")
            + " — direitos de propriedade bem definidos e barganha entre as partes.",
            "A mensagem central de Coase é que, com custos de transação baixos, a intervenção estatal pode ser "
            "<b>desnecessária</b>: basta o direito estar claro. Impor cotas a cada empresa é justamente o tipo "
            "de intervenção que o teorema dispensa.",
            "Detalhe que a banca explora: um teto de emissões combinado com licenças <b>negociáveis</b> (cap and "
            "trade) tem parentesco com Coase — cria um direito de poluir transferível. Mas o item fala só em "
            "teto imposto a cada uma, sem troca.",
            "Desvantagem do teto rígido por empresa: ignora diferenças de custo de abatimento — a redução não "
            "é feita por quem consegue reduzir mais barato.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui ao teorema a solução de comando e controle. O verbo "
                       "“deve ser imposta” é a pista: Coase trabalha com negociação voluntária, não com "
                       "imposição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o Teorema de Coase, a definição do direito de poluir e a negociação entre as empresas "
            "podem levar ao nível eficiente de emissão, sem intervenção adicional do Estado.”</i> → CERTO",
        ])],
        "reescrita": ("Duas empresas enfrentam uma situação de conflito sobre poluição. Segundo o Teorema de Coase: "
                      + hl("basta definir quem tem direito sobre a poluição para que as duas empresas negociem o "
                           "nível eficiente de emissão, sem que o Estado imponha limites a cada uma") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": "Limites máximos são regulação direta (command and control), não solução negociada.",
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0337
    dict(_base("E1-0337", "ext", COM_FALHAS), **{
        "assertiva": ("Uma das principais falhas de mercado para justificar a função alocativa da ação do Governo é a "
                      "existência de externalidades."),
        "gabarito": "CERTO",
        "anotada": az("Uma das principais falhas de mercado para justificar a função alocativa da ação do Governo "
                      "é a existência de <u>externalidades</u>."),
        "poucas": ("Externalidades separam custo/benefício " + azb("privado") + " do " + azb("social") + "; o "
                   "mercado produz demais (negativas) ou de menos (positivas), o que justifica a "
                   + vd("função alocativa") + " do governo."),
        "destrinchando": [
            "Na tipologia de " + oc("Musgrave") + ", o governo tem três funções: " + azb("alocativa") + " "
            "(corrigir a composição do que se produz quando o mercado falha), " + azb("distributiva") + " "
            "(ajustar a repartição da renda) e " + azb("estabilizadora") + " (emprego, preços, crescimento).",
            "Falhas de mercado que fundamentam a função alocativa, na lista usual dos manuais de finanças "
            "públicas (" + oc("Giambiagi e Além") + "): bens públicos, " + vd("externalidades") + ", monopólios "
            "naturais (economias de escala), mercados incompletos e falhas de informação.",
            "Instrumentos para externalidades: impostos e subsídios pigouvianos, regulação de comando e "
            "controle, licenças negociáveis, definição de direitos de propriedade (Coase) e provisão direta.",
            vm("Regra-âncora: externalidade = custo ou benefício fora do preço → função alocativa."),
        ],
        "dissecando": (cz("[literalidade]") + " Item de lista: “externalidades” é falha de mercado clássica. O "
                       "item-irmão troca a última palavra por “deseconomias de escala”, que não constam da "
                       "lista — leia sempre o termo final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A existência de externalidades justifica a função distributiva do governo.”</i> → ERRADO "
            "(função trocada: é a alocativa)",
            "<i>“A existência de monopólios naturais é uma das falhas de mercado que justificam a função "
            "alocativa.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Externalidades causam divergência entre custos/benefícios privados e sociais e "
                             "justificam a função alocativa (subsídios, impostos, regulação)."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
]
