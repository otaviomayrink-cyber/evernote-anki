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
    # ------------------------------------------------------------------ E1-0338
    dict(_base("E1-0338", "ext", COM_FALHAS), **{
        "assertiva": ("Uma das principais falhas de mercado para justificar a função alocativa da ação do Governo é a "
                      "existência de deseconomias de escala."),
        "gabarito": "ERRADO",
        "anotada": (az("Uma das principais falhas de mercado para justificar a função alocativa da ação do Governo "
                       "é a existência de ") + vm("deseconomias de escala") + az(".")),
        "poucas": ("A falha de mercado ligada à escala é a " + azb("economia de escala") + " (custo médio "
                   "decrescente), que gera " + vd("monopólio natural") + ". Deseconomias de escala só limitam o "
                   "tamanho eficiente da firma."),
        "destrinchando": [
            azb("Economias de escala") + ": o custo médio cai à medida que a produção cresce (custos fixos "
            "altíssimos, como redes de água, gás, energia e ferrovias). Se o custo médio cai em toda a faixa "
            "relevante da demanda, uma única firma abastece o mercado mais barato do que várias: "
            + azb("monopólio natural") + ". Sem regulação, ele cobra preço de monopólio — daí a regulação "
            "tarifária ou a provisão estatal.",
            azb("Deseconomias de escala") + ": o custo médio sobe a partir de certo tamanho (problemas de "
            "coordenação, burocracia interna). Isso <b>favorece</b> a concorrência, pois impede que uma firma "
            "cresça indefinidamente; não é falha de mercado nem motivo para o governo intervir.",
            "Lista usual de falhas que justificam a " + azb("função alocativa") + " (" + oc("Musgrave") + "; "
            + oc("Giambiagi e Além") + "): bens públicos, externalidades, monopólios naturais, mercados "
            "incompletos e falhas de informação.",
            vm("Regra-âncora: economia de escala → monopólio natural → falha; deseconomia → não é falha."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca de prefixo: “economias” → “deseconomias”. O item "
                       "aposta que o candidato associe “escala” à lista de falhas sem conferir o sentido. Mesmo "
                       "comando do item-irmão sobre externalidades (CERTO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A existência de rendimentos crescentes de escala, que dão origem a monopólios naturais, é uma "
            "das falhas de mercado que justificam a função alocativa do governo.”</i> → CERTO",
        ])],
        "reescrita": ("Uma das principais falhas de mercado para justificar a função alocativa da ação do Governo é "
                      "a existência de " + hl("economias de escala (que dão origem a monopólios naturais)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Deseconomias de escala dizem respeito a aumento do custo médio com a produção, mas não "
                             "são falhas de mercado."),
        "qualidade_fonte": "raso", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0339
    dict(_base("E1-0339", "ext", COM_EXT), **{
        "assertiva": "A competição perfeita é socialmente desejável, pois elimina a externalidade negativa.",
        "gabarito": "ERRADO",
        "anotada": (az("A competição perfeita é socialmente desejável, ") + vm("pois elimina a externalidade "
                                                                               "negativa") + az(".")),
        "poucas": ("A concorrência perfeita iguala preço ao custo marginal " + azb("privado") + "; com "
                   "externalidade negativa, esse custo fica abaixo do social e o mercado " + vd("produz demais")
                   + " — a externalidade persiste."),
        "destrinchando": [
            "O " + azb("1º teorema do bem-estar") + " diz que o equilíbrio competitivo é eficiente (Pareto) "
            "<b>desde que não haja falhas de mercado</b>. A externalidade é justamente uma falha: o teorema "
            "deixa de valer.",
            "Mecanismo: a firma competitiva produz até P = CMgP. Como " + vd("CMgS = CMgP + dano externo")
            + ", o mercado vai até Qₘ, além do ótimo Q* (onde BMg = CMgS). Cada unidade entre Q* e Qₘ custa à "
            "sociedade mais do que vale: " + azb("peso morto") + ".",
            "Ironia que a banca gosta de cobrar: com externalidade negativa, um " + azb("monopólio") + " poluidor "
            "pode até chegar mais perto do ótimo, porque restringe a produção. A concorrência, que é virtude "
            "sem falhas, amplia o dano quando há externalidade.",
            "Correções: imposto pigouviano, licenças negociáveis, regulação ou barganha de Coase — todas "
            "introduzem o custo externo na decisão privada.",
            vm("Regra-âncora: concorrência perfeita não corrige falha de mercado; ela só é ótima na ausência "
               "delas."),
        ],
        "grafico_verso": "ECO-E1-0339-1-V1",
        "dissecando": (cz("[nexo indevido]") + " A 1ª oração tem fundo verdadeiro (o teorema do bem-estar); o "
                       "erro está na justificativa enxertada com “pois”, que atribui à concorrência um efeito "
                       "que ela não tem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em concorrência perfeita, a presença de externalidade negativa faz a quantidade de equilíbrio "
            "superar a socialmente ótima.”</i> → CERTO",
            "<i>“Com externalidade negativa, a concorrência perfeita produz menos do que o ótimo social.”</i> → "
            "ERRADO (inversão: produz mais)",
        ])],
        "reescrita": ("A competição perfeita é socialmente desejável, " + hl("mas não elimina a externalidade "
                      "negativa, que exige correção específica (imposto pigouviano, regulação ou negociação à "
                      "Coase)") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["pois"], "dificuldade": 1,
        "comentario_fonte": ("A concorrência perfeita não elimina externalidades; pode ampliar a produção "
                             "ineficiente, pois as empresas não internalizam os custos sociais."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0341
    dict(_base("E1-0341", "ext", COM_EXT), **{
        "assertiva": ("Falhas de mercado na forma de externalidade ocorrem quando nem todos os custos e benefícios "
                      "estão incluídos nos preços dos bens."),
        "gabarito": "CERTO",
        "anotada": az("Falhas de mercado na forma de externalidade ocorrem quando <u>nem todos os custos e "
                      "benefícios estão incluídos nos preços</u> dos bens."),
        "poucas": ("Externalidade é o efeito de uma atividade sobre " + azb("terceiros") + " que não passa pelo "
                   "preço: custo que ninguém paga (negativa) ou benefício que ninguém cobra (positiva)."),
        "destrinchando": [
            "Definição operacional: a ação de um agente afeta o bem-estar de outro <b>sem compensação</b> pelo "
            "mercado. O preço reflete só o custo e o benefício privados; a parte social fica de fora.",
            "Quatro casos: produção negativa (fábrica que polui o rio), produção positiva (apicultor cujas "
            "abelhas polinizam o pomar vizinho), consumo negativo (fumo em local fechado), consumo positivo "
            "(vacinação, que protege os não vacinados).",
            "Efeito na quantidade: negativa → " + vd("produção excessiva") + " (CMgS > CMgP); positiva → "
            + vd("produção insuficiente") + " (BMgS > BMgP). Corrigir é " + azb("internalizar") + ": fazer o "
            "preço carregar o efeito externo.",
            "Não confundir com efeitos que passam <b>pelo</b> preço (" + azb("externalidade pecuniária") + "): "
            "se a demanda por um bem sobe e encarece o insumo de outra firma, o mercado está funcionando — não "
            "há falha.",
            vm("Regra-âncora: externalidade = efeito sobre terceiros fora do sistema de preços."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição em linguagem de preços, correta. As versões erradas "
                       "costumam restringir a externalidade a custos (“só efeitos negativos”) ou ao Estado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Externalidades são sempre efeitos negativos de uma atividade sobre terceiros.”</i> → ERRADO "
            "(modulador absoluto: há externalidades positivas)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["nem todos"], "dificuldade": 1,
        "comentario_fonte": ("Divergência entre custos/benefícios privados e sociais: nem todos refletidos no preço, "
                             "o que compromete a eficiência alocativa."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0342
    dict(_base("E1-0342", "ext", COM_FALHAS), **{
        "assertiva": ("Não se trata de uma falha de mercado: a variação dos preços agrícolas ao longo do ano, devido à "
                      "presença de períodos de safra e de entressafra."),
        "gabarito": "CERTO",
        "anotada": az("<u>Não</u> se trata de uma falha de mercado: a variação dos preços agrícolas ao longo do "
                      "ano, devido à presença de períodos de safra e de entressafra."),
        "poucas": ("Preço que cai na safra e sobe na entressafra é o " + azb("sistema de preços funcionando") + ": "
                   "sinaliza escassez e abundância, estimula estocagem e racionaliza o consumo."),
        "destrinchando": [
            "Falha de mercado é a situação em que o equilíbrio de mercado " + azb("não é eficiente") + ": bens "
            "públicos, externalidades, poder de mercado, informação assimétrica, mercados incompletos.",
            "Na sazonalidade agrícola, o preço reflete a escassez real: na entressafra há menos produto, o "
            "preço sobe e premia quem estocou; na safra, o preço cai e o consumo aumenta. É a " + azb("função "
            "sinalizadora") + " dos preços em ação, não sua falha.",
            "Volatilidade não é sinônimo de ineficiência. O governo pode intervir por outras razões — renda do "
            "produtor, segurança alimentar — com " + rx("política de garantia de preços mínimos (PGPM) e "
            "estoques reguladores da Conab") + ", mas isso é objetivo de política, não correção de falha "
            "alocativa.",
            "O que <b>seria</b> falha no mesmo setor: uso de agrotóxico que contamina o vizinho (externalidade), "
            "seguro rural com seleção adversa (informação), ausência de mercado futuro para pequenos produtores "
            "(mercado incompleto).",
        ],
        "dissecando": (cz("[contraintuitivo]") + " A formulação negativa (“não se trata”) e a ideia de que "
                       "preço oscilante é “problema” induzem ao ERRADO. Itens desse tipo vêm de questões de "
                       "múltipla escolha do tipo “assinale o que NÃO é falha de mercado”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Não se trata de uma falha de mercado: a poluição de um rio por indústria situada a montante de "
            "uma comunidade de pescadores.”</i> → ERRADO (é externalidade negativa)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": ("A variação sazonal reflete oscilações de oferta e demanda, dinâmica normal de "
                             "mercado, não falha."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0333
    dict(_base("E1-0333", "info", COM_FALHAS), **{
        "assertiva": ("Ao analisar os conceitos microeconômicos de “falha de mercado” e de “informação assimétrica”: "
                      "falhas de mercado estão associadas à sinalização inadequada a partir do sistema de preços."),
        "gabarito": "CERTO",
        "anotada": az("Ao analisar os conceitos microeconômicos de “falha de mercado” e de “informação "
                      "assimétrica”: falhas de mercado estão associadas à <u>sinalização inadequada</u> a partir "
                      "do sistema de preços."),
        "poucas": ("No mercado eficiente, o preço resume custo e benefício " + azb("sociais") + ". Na falha de "
                   "mercado, ele " + vd("sinaliza errado") + " — omite custo externo, não capta benefício "
                   "coletivo ou não incorpora informação — e a alocação se desvia do ótimo."),
        "destrinchando": [
            "O preço tem três papéis: " + azb("sinalizar") + " (escassez relativa), " + azb("incentivar") + " "
            "(produzir mais o que está caro) e " + azb("racionar") + " (alocar a quem valoriza mais). "
            + oc("Hayek") + " (“The Use of Knowledge in Society”, 1945) destacou o preço como transmissor de "
            "informação dispersa.",
            "Em cada falha, a sinalização se rompe de um jeito: externalidade → o preço não inclui o dano a "
            "terceiros; bem público → não há preço que revele a disposição a pagar; poder de mercado → preço "
            "acima do custo marginal; " + azb("informação assimétrica") + " → o preço não distingue qualidade "
            "ou risco (no mercado de “limões” de " + oc("Akerlof") + ", o preço médio expulsa os bons carros).",
            "Por isso a correção típica atua sobre o preço (imposto, subsídio, regulação tarifária) ou sobre a "
            "informação que o forma (transparência, certificação, garantias).",
            vm("Regra-âncora: falha de mercado = preço que não reflete o custo ou o benefício social."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Formulação genérica e verdadeira. Itens assim costumam vir em "
                       "bloco com outro que confunde os dois conceitos (por exemplo, “a informação assimétrica "
                       "não é falha de mercado”, ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A informação assimétrica, por decorrer de escolhas individuais, não constitui falha de "
            "mercado.”</i> → ERRADO (é uma das falhas clássicas)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Na falha de mercado o sinal de preços não reflete custos ou benefícios sociais, "
                             "levando à má alocação (externalidades, assimetria de informação)."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0327
    dict(_base("E1-0327", "reg", COM_REG), **{
        "assertiva": ("De acordo com a teoria microeconômica convencional, na presença de falhas de mercado, a "
                      "regulação dos mercados por parte do governo pode ser benéfica na presença de poder de "
                      "mercado, como monopólios naturais ou legais que podem impor perdas substanciais de "
                      "bem-estar aos consumidores."),
        "gabarito": "CERTO",
        "anotada": az("De acordo com a teoria microeconômica convencional, na presença de falhas de mercado, a "
                      "regulação dos mercados por parte do governo <u>pode</u> ser benéfica na presença de poder "
                      "de mercado, como monopólios naturais ou legais que podem impor perdas substanciais de "
                      "bem-estar aos consumidores."),
        "poucas": ("O monopolista cobra " + vd("P > CMg") + " e produz menos que o ótimo, gerando "
                   + azb("peso morto") + "; a regulação de preço ou de entrada pode aproximar o resultado do "
                   "competitivo."),
        "destrinchando": [
            "Poder de mercado é falha porque rompe P = CMg: a firma restringe a quantidade para elevar o preço, "
            "transfere excedente do consumidor para si e destrói parte dele (peso morto).",
            azb("Monopólio natural") + " (custo médio decrescente, como redes de saneamento e transmissão de "
            "energia): uma firma só é o arranjo mais barato, então a solução não é fragmentar, e sim "
            + azb("regular") + " — tarifa pelo custo médio, preço-teto (" + azb("price cap") + ") ou "
            "regulação por taxa de retorno. No " + rx("Brasil") + ", esse é o papel de agências como "
            + rx("ANEEL e ANA") + ".",
            azb("Monopólio legal") + " (patentes, concessões exclusivas): o próprio Estado cria o poder de "
            "mercado e, por isso, costuma acompanhá-lo de regras de preço, prazo e qualidade.",
            "A ressalva do item — “pode ser benéfica” — importa: a regulação também falha (" + azb("captura")
            + ", assimetria de informação entre regulador e regulado, custos administrativos). A teoria "
            "convencional justifica a intervenção, mas não garante que ela melhore o resultado.",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " Dois “pode” blindam o item. Versões erradas "
                       "trocam por “sempre aumenta o bem-estar” ou dizem que monopólios naturais devem ser "
                       "desmembrados para gerar concorrência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No monopólio natural, a solução eficiente é dividir a empresa em várias concorrentes.”</i> → "
            "ERRADO (o custo médio subiria: uma firma é o arranjo mais barato)",
            "<i>“A regulação de monopólios sempre eleva o bem-estar social.”</i> → ERRADO (modulador absoluto: "
            "há falhas de governo)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["pode", "podem"], "dificuldade": 1,
        "comentario_fonte": ("Monopólios geram ineficiências alocativas e reduzem o excedente do consumidor; a "
                             "regulação pode conter abusos e melhorar o bem-estar."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0343
    dict(_base("E1-0343", "reg", COM_REG), **{
        "assertiva": ("Quando uma agência reguladora atua em favor de interesses do setor regulado, diz-se que, nesta "
                      "situação, encontramos a Teoria da captura."),
        "gabarito": "CERTO",
        "anotada": az("Quando uma agência reguladora atua em favor de interesses do <u>setor regulado</u>, diz-se "
                      "que, nesta situação, encontramos a <u>Teoria da captura</u>."),
        "poucas": ("A " + azb("captura regulatória") + " ocorre quando o regulador passa a servir aos interesses "
                   "das empresas reguladas, e não ao interesse público — exemplo clássico de " + vd("falha de "
                   "governo") + "."),
        "destrinchando": [
            "Origem: " + oc("George Stigler") + " (“The Theory of Economic Regulation”, 1971; Nobel de 1982), "
            "na Escola de Chicago. Tese: a regulação é “adquirida” pela indústria e desenhada e operada "
            "principalmente em seu benefício.",
            "Por que acontece: " + azb("concentração de benefícios e dispersão de custos") + " — as poucas "
            "firmas reguladas ganham muito com uma decisão favorável e se organizam para obtê-la; os milhões "
            "de consumidores perdem pouco cada um e não se mobilizam (lógica de " + oc("Mancur Olson") + "). "
            "Somam-se a assimetria de informação (o regulador depende de dados da empresa) e a "
            + azb("porta giratória") + " entre agência e setor.",
            "Contraste com a " + azb("teoria do interesse público") + " (regulação como correção desinteressada "
            "de falhas de mercado). A captura mostra que corrigir uma falha de mercado pode criar uma " + azb(
                "falha de governo") + ".",
            "Antídotos: mandatos fixos e não coincidentes para dirigentes, quarentena, autonomia orçamentária, "
            "consultas públicas e análise de impacto regulatório — no " + rx("Brasil") + ", em boa parte disciplinados pela "
            + rx("Lei 13.848/2019") + " (Lei Geral das Agências Reguladoras).",
            vm("Regra-âncora: regulador a serviço do regulado = captura (Stigler) = falha de governo."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. A banca pode trocar o nome (“teoria do interesse "
                       "público”, “risco moral”) ou o beneficiário (“atua em favor dos consumidores”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela teoria do interesse público, as agências tendem a ser capturadas pelos setores "
            "regulados.”</i> → ERRADO (teoria trocada: é a da captura)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("As agências passam a defender os interesses das empresas que deveriam fiscalizar, "
                             "perdendo a imparcialidade."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0344
    dict(_base("E1-0344", "info", COM_INFO), **{
        "assertiva": "A relação agente-principal é aplicável ao setor público.",
        "gabarito": "CERTO",
        "anotada": az("A relação agente-principal é <u>aplicável ao setor público</u>."),
        "poucas": ("Sempre que alguém (" + azb("principal") + ") delega uma tarefa a outro (" + azb("agente")
                   + ") que tem informação e interesses próprios há problema de agência — e o setor público está "
                   "cheio dessas cadeias: " + vd("cidadão → político → burocrata") + "."),
        "destrinchando": [
            "O " + azb("problema agente-principal") + " nasce da combinação de três elementos: delegação, "
            "interesses divergentes e " + azb("informação assimétrica") + " (o principal não observa "
            "perfeitamente o esforço ou as informações do agente). Formalização clássica: " + oc("Jensen e "
            "Meckling") + " (1976), para a relação acionista × administrador.",
            "No setor público: eleitores (principal) × parlamentares e governantes (agente); Congresso × "
            "Executivo; ministério × agência reguladora ou estatal; governo × gestor de uma empresa pública. O "
            "agente pode perseguir reeleição, prestígio, orçamento maior ou interesses de grupos.",
            "Agravante: no setor público os mecanismos de mercado que disciplinam o agente privado (preço da "
            "ação, ameaça de aquisição hostil, falência) são fracos ou inexistentes.",
            "Instrumentos de alinhamento: eleições, mandatos e prestação de contas (" + azb("accountability")
            + "), controle externo (" + rx("TCU") + "), contratos de gestão com metas, remuneração por "
            "desempenho, transparência e regras de governança das estatais (" + rx("Lei 13.303/2016") + ").",
            vm("Regra-âncora: delegação + interesses divergentes + informação oculta = problema de agência, "
               "público ou privado."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Quem associa o modelo só a empresas "
                       "(acionista × gerente) tende a restringi-lo ao setor privado. Desconfie das versões "
                       "com “aplica-se exclusivamente às relações privadas”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O problema agente-principal limita-se à relação entre acionistas e administradores de "
            "empresas privadas.”</i> → ERRADO (restrição indevida)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O cidadão (principal) delega ao político ou gestor (agente) decisões em seu nome, com "
                             "risco de interesses desalinhados."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0345
    dict(_base("E1-0345", "info", COM_INFO), **{
        "assertiva": "O risco moral altera o comportamento dos indivíduos.",
        "gabarito": "CERTO",
        "anotada": az("O risco moral <u>altera o comportamento</u> dos indivíduos."),
        "poucas": ("O " + azb("risco moral") + " (<i>moral hazard</i>) é exatamente a mudança de comportamento "
                   + vd("depois") + " do contrato, quando o agente está protegido do risco e a outra parte não "
                   "consegue observar suas ações."),
        "destrinchando": [
            "Dois problemas de informação assimétrica, distinguidos pelo <b>momento</b>: " + azb("seleção "
            "adversa") + " — informação <b>oculta</b> antes do contrato (quem compra seguro saúde sabe mais "
            "sobre a própria saúde); " + azb("risco moral") + " — <b>ação oculta</b> depois do contrato (o "
            "segurado relaxa os cuidados).",
            "Exemplos: motorista com seguro total que estaciona em qualquer lugar; paciente com plano que pede "
            "exames desnecessários; banco “grande demais para quebrar” que assume riscos excessivos contando "
            "com socorro (" + azb("too big to fail") + "); devedor que, com o dinheiro na mão, aplica em projeto "
            "mais arriscado.",
            "Remédios: " + azb("franquia") + " e " + azb("coparticipação") + " (o segurado volta a arcar com "
            "parte do risco), bônus por ausência de sinistro, monitoramento, colateral no crédito, regulação "
            "prudencial dos bancos.",
            vm("Regra-âncora: seleção adversa = antes (quem contrata); risco moral = depois (como se "
               "comporta)."),
        ],
        "dissecando": (cz("[literalidade]") + " Item curto e verdadeiro por definição. A pegadinha usual troca o "
                       "momento (“o risco moral ocorre antes da celebração do contrato”) ou o nome do problema "
                       "(seleção adversa × risco moral)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O risco moral decorre de informação oculta antes da assinatura do contrato.”</i> → ERRADO "
            "(troca de conceito: isso é seleção adversa)",
            "<i>“A franquia nos contratos de seguro é um mecanismo de atenuação do risco moral.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O risco moral surge após a contratação, quando o indivíduo muda o comportamento por "
                             "estar protegido dos riscos (seguros, crédito)."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (84).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0346
    dict(_base("E1-0346", "info", COM_INFO), **{
        "assertiva": ("Uma assimetria de informações caracterizada pela insuficiência destas pode levar as autoridades "
                      "a atuarem por meio de regulação."),
        "gabarito": "CERTO",
        "anotada": az("Uma assimetria de informações caracterizada pela insuficiência destas <u>pode</u> levar as "
                      "autoridades a atuarem por meio de <u>regulação</u>."),
        "poucas": ("Informação assimétrica é " + azb("falha de mercado") + "; quando uma das partes não tem "
                   "informação suficiente para decidir bem, a regulação (divulgação obrigatória, padrões, "
                   "certificação) " + vd("pode") + " corrigir o desvio."),
        "destrinchando": [
            "Com informação insuficiente de um lado, o mercado pode encolher ou desaparecer (seleção adversa, "
            "os “limões” de " + oc("Akerlof") + ", 1970) ou funcionar com comportamentos indesejados (risco "
            "moral).",
            "Formas de atuação estatal: " + azb("divulgação obrigatória") + " (prospecto de oferta de ações, "
            "fiscalizado no " + rx("Brasil") + " pela " + rx("CVM") + "; rotulagem nutricional); "
            + azb("padrões mínimos") + " e licenças profissionais (registro de medicamentos pela "
            + rx("Anvisa") + "); " + azb("seguro obrigatório") + " (evita que só os de alto risco contratem); "
            "proteção ao consumidor (direito de arrependimento, garantia legal).",
            "O mercado também cria soluções privadas: " + azb("sinalização") + " (" + oc("Spence") + ": "
            "diploma, garantia estendida), " + azb("filtragem") + " (" + oc("Stiglitz") + ": menu de contratos "
            "com franquias diferentes), reputação e marcas. Akerlof, Spence e Stiglitz dividiram o Nobel de "
            + vd("2001") + " por essa agenda.",
            "O “pode” é essencial: a regulação também enfrenta assimetria (o regulador sabe menos que o "
            "regulado) e pode ser capturada.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Redação truncada (“insuficiência destas”), "
                       "mas conteúdo correto e protegido pelo “pode”. O inverso típico seria “a assimetria de "
                       "informação dispensa a regulação, pois o mercado a corrige integralmente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A assimetria de informação só pode ser corrigida por regulação estatal.”</i> → ERRADO "
            "(restrição indevida: há sinalização, filtragem e reputação)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Falha de mercado que pode justificar intervenção por regulação, transparência ou "
                             "regras de mercado."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (82).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0347
    dict(_base("E1-0347", "info", COM_INFO), **{
        "assertiva": "O mercado de crédito é exemplo de setor sem informações assimétricas.",
        "gabarito": "ERRADO",
        "anotada": (az("O mercado de crédito é exemplo de setor ") + vm("sem") + az(" informações "
                                                                                     "assimétricas.")),
        "poucas": ("O crédito é o exemplo-padrão de " + azb("informação assimétrica") + ": o tomador conhece o "
                   "próprio risco e as próprias intenções melhor que o banco — há " + vd("seleção adversa e "
                   "risco moral") + "."),
        "destrinchando": [
            azb("Seleção adversa") + " (antes do empréstimo): se o banco sobe os juros, os bons pagadores "
            "desistem e ficam os tomadores com projetos mais arriscados, dispostos a pagar qualquer taxa. Por "
            "isso o banco prefere " + azb("racionar o crédito") + " a elevar a taxa — tese de " + oc("Stiglitz e "
            "Weiss") + " (1981).",
            azb("Risco moral") + " (depois): com o dinheiro na mão, o devedor pode aplicar em projeto mais "
            "arriscado que o combinado ou se esforçar menos para pagar.",
            "Respostas do mercado e do Estado: garantias e colateral, análise de cadastro e " + azb("cadastro "
            "positivo") + ", covenants, relacionamento de longo prazo; no " + rx("Brasil") + ", o "
            + rx("Sistema de Informações de Crédito (SCR) do Banco Central") + " e o cadastro positivo "
            "reduzem a assimetria.",
            "A assimetria também explica o " + azb("spread") + " bancário elevado e a dificuldade de crédito "
            "para pequenas empresas sem histórico.",
            vm("Regra-âncora: crédito e seguros = mercados-símbolo de seleção adversa e risco moral."),
        ],
        "dissecando": (cz("[contradição · troca de conceito]") + " Uma palavra (“sem”) inverte o exemplo mais "
                       "clássico da literatura. Pista: qualquer mercado em que uma parte promete pagar no "
                       "futuro envolve informação privada sobre a capacidade e a vontade de pagar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mercado de crédito, a elevação da taxa de juros pode piorar a qualidade média dos tomadores, "
            "levando os bancos a racionar o crédito.”</i> → CERTO",
        ])],
        "reescrita": ("O mercado de crédito é exemplo de setor " + hl("com") + " informações assimétricas"
                      + hl(", sujeito a seleção adversa e risco moral") + "."),
        "tipo_erro": ["CONTRADICAO", "TROCA_CONCEITO"], "moduladores": ["sem"], "dificuldade": 1,
        "comentario_fonte": ("Um dos exemplos mais clássicos de informação assimétrica, com seleção adversa e risco "
                             "moral antes e depois da concessão."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0348
    dict(_base("E1-0348", "info", COM_FALHAS), **{
        "assertiva": ("As falhas de mercado impedem a máxima eficiência na alocação de recursos. A presença de "
                      "informação assimétrica pode ocasionar o problema do risco moral nos mercados de seguros de "
                      "automóveis."),
        "gabarito": "CERTO",
        "anotada": az("As falhas de mercado impedem a máxima eficiência na alocação de recursos. A presença de "
                      "informação assimétrica pode ocasionar o problema do <u>risco moral</u> nos mercados de "
                      "seguros de automóveis."),
        "poucas": ("Com o carro segurado, o motorista arca com menos risco e tende a ser " + vd("menos "
                   "cuidadoso") + "; como a seguradora não observa o cuidado, há " + azb("risco moral") + "."),
        "destrinchando": [
            "O risco moral exige duas condições: a ação do segurado afeta a probabilidade ou o tamanho do "
            "sinistro, e a seguradora " + azb("não consegue observá-la") + " (ação oculta). O seguro de "
            "automóvel reúne as duas: velocidade, local de estacionamento e uso de alarme mudam o risco e não "
            "são monitoráveis a custo baixo.",
            "O mesmo mercado sofre também de " + azb("seleção adversa") + " (os motoristas mais arriscados têm "
            "mais interesse em contratar). As seguradoras respondem a cada problema com instrumentos "
            "diferentes: perfil e questionário (seleção adversa); " + azb("franquia") + ", bônus por anos sem "
            "sinistro e rastreadores (risco moral).",
            "A 1ª frase do item também é correta: falha de mercado é, por definição, situação em que o "
            "equilíbrio não é eficiente no sentido de " + oc("Pareto") + ".",
            vm("Regra-âncora: seguro + comportamento não observável depois do contrato = risco moral."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Exemplo de manual, com “pode ocasionar”. O "
                       "par errado típico troca o nome do problema (“seleção adversa” para o descuido após a "
                       "contratação) ou nega que haja assimetria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nos seguros de automóveis, o fato de motoristas mais imprudentes terem mais interesse em "
            "contratar o seguro caracteriza o risco moral.”</i> → ERRADO (troca de conceito: é seleção "
            "adversa)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("O comportamento do segurado muda após contratar o seguro, agindo de forma menos "
                             "cautelosa."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0350
    dict(_base("E1-0350", "info", COM_INFO), **{
        "assertiva": ("Sobre assimetrias da informação: resultam sempre em externalidades positivas, pois envolvem "
                      "benefícios não reconhecidos pelos agentes diretamente interessados em determinado tipo de "
                      "transação."),
        "gabarito": "ERRADO",
        "anotada": (az("Sobre assimetrias da informação: ") + vm("resultam sempre em externalidades positivas, "
                       "pois envolvem benefícios não reconhecidos pelos agentes diretamente interessados") + az(
                       " em determinado tipo de transação.")),
        "poucas": ("Assimetria de informação é uma falha de mercado " + azb("própria") + " — gera " + vd("seleção "
                   "adversa e risco moral") + ", em geral com perdas — e não se confunde com externalidade, muito "
                   "menos “sempre positiva”."),
        "destrinchando": [
            "São falhas distintas: na " + azb("externalidade") + ", o efeito recai sobre <b>terceiros</b> fora "
            "da transação; na " + azb("assimetria de informação") + ", o problema está <b>dentro</b> da "
            "transação — uma das partes sabe mais que a outra sobre qualidade, risco ou comportamento.",
            "Consequências típicas são negativas: mercados que encolhem ou desaparecem (" + oc("Akerlof")
            + ", os “limões”), racionamento de crédito, prêmios de seguro altos, comportamento menos cuidadoso "
            "após o contrato.",
            "A justificativa do item descreve, na verdade, um fenômeno vizinho: benefícios não apropriados por "
            "quem os gera é a definição de " + azb("externalidade positiva") + " (ex.: pesquisa básica, "
            "vacinação), não de assimetria de informação.",
            vm("Regra-âncora: assimetria = informação desigual entre as partes; externalidade = efeito sobre "
               "terceiros."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " Dois erros: o “sempre” e a fusão de "
                       "duas falhas diferentes. A justificativa com “pois” descreve corretamente uma "
                       "externalidade positiva, para dar ar de verdade ao conjunto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Assimetrias de informação podem levar à seleção adversa, reduzindo a qualidade média dos bens "
            "transacionados.”</i> → CERTO",
        ])],
        "reescrita": ("Sobre assimetrias da informação: " + hl("podem resultar em seleção adversa e risco moral, "
                      "pois uma das partes detém informações relevantes que a outra não possui") + " em "
                      "determinado tipo de transação."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("Assimetrias geram falhas de mercado, não externalidades; podem levar a seleção adversa "
                             "e risco moral."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (86).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0351
    dict(_base("E1-0351", "info", COM_INFO), **{
        "assertiva": ("Sobre assimetrias da informação: podem ocorrer quando do estabelecimento de contratos "
                      "financeiros, pois os elementos relevantes para a realização de uma transação financeira não "
                      "são totalmente transparentes."),
        "gabarito": "CERTO",
        "anotada": az("Sobre assimetrias da informação: <u>podem ocorrer</u> quando do estabelecimento de contratos "
                      "financeiros, pois os elementos relevantes para a realização de uma transação financeira "
                      "não são totalmente transparentes."),
        "poucas": ("Contratos financeiros trocam dinheiro hoje por promessa futura; quem promete sabe mais sobre "
                   "a própria capacidade de cumprir: " + azb("assimetria de informação") + " com " + vd("seleção "
                   "adversa") + " antes e " + vd("risco moral") + " depois."),
        "destrinchando": [
            "Empréstimo: o tomador conhece o risco do projeto melhor que o banco. Emissão de ações: os "
            "administradores conhecem a empresa melhor que os investidores (por isso emitir ações pode ser lido "
            "como sinal de que a ação está cara). Seguro: o segurado conhece o próprio risco.",
            "Essa é a base da teoria moderna da intermediação: bancos existem em parte porque se especializam "
            "em coletar e produzir informação sobre tomadores (análise de crédito, relacionamento), reduzindo a "
            "assimetria que inviabilizaria o financiamento direto.",
            "Regulação financeira como resposta: divulgação obrigatória (prospectos, demonstrações auditadas), "
            "agências de rating, regras contra uso de informação privilegiada (" + azb("insider trading")
            + "), fiscalizados no " + rx("Brasil") + " pela " + rx("CVM") + " e pelo " + rx("Banco Central") + ".",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O “podem ocorrer” e o “não são totalmente "
                       "transparentes” calibram bem a afirmação. É o item-irmão correto de um bloco cujo erro "
                       "está no “sempre externalidades positivas”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em contratos financeiros, a assimetria de informação é eliminada pela livre negociação das "
            "taxas de juros.”</i> → ERRADO (a taxa mais alta agrava a seleção adversa)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["podem", "totalmente"],
        "dificuldade": 1,
        "comentario_fonte": ("Comum em contratos financeiros, em que uma das partes detém mais informações "
                             "relevantes."),
        "qualidade_fonte": "raso", "figuras_fonte": [], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0352
    dict(_base("E1-0352", "info", COM_INFO), **{
        "assertiva": ("No funcionamento dos mercados, algumas pessoas sabem de coisas que outras não sabem, o que pode "
                      "impedir transações mutuamente benéficas. Essa falha de mercado é denominada: confiança do "
                      "consumidor."),
        "gabarito": "ERRADO",
        "anotada": (az("No funcionamento dos mercados, algumas pessoas sabem de coisas que outras não sabem, o que "
                       "pode impedir transações mutuamente benéficas. Essa falha de mercado é denominada: ")
                    + vm("confiança do consumidor") + az(".")),
        "poucas": ("A situação descrita é a " + azb("informação assimétrica") + ". “Confiança do consumidor” é um "
                   + vd("indicador de expectativas") + " (sentimento sobre a economia), não uma falha de mercado."),
        "destrinchando": [
            "A descrição do item é a definição de manual (" + oc("Mankiw") + "): diferença de acesso a "
            "informação relevante entre as partes, capaz de impedir trocas que seriam vantajosas para ambas.",
            "Como a troca vantajosa deixa de ocorrer: no mercado de carros usados de " + oc("Akerlof")
            + " (1970), o comprador não distingue o carro bom do “limão” e só aceita pagar o preço médio; os "
            "donos de carros bons, que valem mais, retiram-se — e o mercado de bons carros desaparece, embora "
            "houvesse compradores dispostos a pagar o valor justo.",
            azb("Índice de confiança do consumidor") + ": pesquisa de expectativas sobre renda, emprego e "
            "situação econômica (no " + rx("Brasil") + ", calculado pela " + rx("FGV") + "). Serve para "
            "antecipar consumo; nada tem a ver com falhas de mercado.",
            vm("Regra-âncora: “uns sabem o que outros não sabem” = informação assimétrica."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Item derivado de múltipla escolha: a descrição é correta e "
                       "a etiqueta foi trocada por um termo econômico real, mas de outro campo "
                       "(macroeconomia/conjuntura). Pista: falhas de mercado têm lista fechada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Essa falha de mercado é denominada informação assimétrica e pode gerar seleção adversa.”</i> → "
            "CERTO",
            "<i>“Essa falha de mercado é denominada externalidade.”</i> → ERRADO (troca de conceito: o efeito "
            "não recai sobre terceiros)",
        ])],
        "reescrita": ("No funcionamento dos mercados, algumas pessoas sabem de coisas que outras não sabem, o que "
                      "pode impedir transações mutuamente benéficas. Essa falha de mercado é denominada: "
                      + hl("informação assimétrica") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Confiança do consumidor é indicador de sentimento econômico, não falha de mercado; o "
                             "caso é de assimetria de informação."),
        "qualidade_fonte": "bom", "figuras_fonte": [_img("Untitled (86).jpeg")], "alertas": [],
    }),
    # ------------------------------------------------------------------ E1-0353
    dict(_base("E1-0353", "info", COM_INFO), **{
        "assertiva": ("A presença de informação assimétrica entre agentes do mercado justifica a presença de "
                      "regulação estatal, exigindo-se maior transparência nas transações entre agentes privados."),
        "gabarito": "CERTO",
        "anotada": az("A presença de informação assimétrica entre agentes do mercado <u>justifica</u> a presença "
                      "de regulação estatal, exigindo-se <u>maior transparência</u> nas transações entre agentes "
                      "privados."),
        "poucas": ("Sendo " + azb("falha de mercado") + ", a assimetria fundamenta a intervenção; a resposta "
                   "típica é " + vd("regulação de transparência") + " — obrigar quem sabe mais a revelar o que "
                   "sabe."),
        "destrinchando": [
            "Lógica: se o problema é informação desigual, o remédio mais direto é reduzir a desigualdade — "
            "divulgação obrigatória, padronização das informações, auditoria independente e punição da fraude.",
            "Exemplos: demonstrações financeiras auditadas e fatos relevantes no mercado de capitais (" + rx(
                "CVM") + "); Custo Efetivo Total (CET) obrigatório nos empréstimos (" + rx("Banco Central")
            + "); dever de informação do " + rx("Código de Defesa do Consumidor") + " (art. 6º, III, e art. "
            "31); rotulagem de alimentos.",
            "Note o verbo: “justifica” não significa que toda regulação seja bem-sucedida. A teoria aponta "
            "também falhas de governo (captura, custo de cumprimento) e soluções privadas (sinalização de "
            + oc("Spence") + ", filtragem de " + oc("Stiglitz") + ", reputação).",
            vm("Regra-âncora: falha de informação → remédio de informação (transparência)."),
        ],
        "dissecando": (cz("[literalidade]") + " Conteúdo de manual sobre a fundamentação da regulação. Versões "
                       "erradas costumam dizer que a regulação “elimina completamente” a assimetria ou que ela "
                       "“dispensa” intervenção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A exigência de transparência elimina por completo os problemas de seleção adversa e risco "
            "moral.”</i> → ERRADO (modulador absoluto: atenua, não elimina)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["justifica"], "dificuldade": 1,
        "comentario_fonte": ("Falha de mercado clássica que justifica intervenção estatal para promover "
                             "transparência e proteção ao consumidor."),
        "qualidade_fonte": "bom", "figuras_fonte": [], "alertas": [],
    }),
]
