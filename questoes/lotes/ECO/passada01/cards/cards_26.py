"""Cards da redação ECO — passada 01 — lote 26 (nota 12 — Falhas de mercado; notas 15 e 16)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "ext": "🌫️ Externalidades e Coase",
    "bp": "🏞️ Bens públicos e comuns",
    "info": "🕵️ Informação assimétrica",
    "reg": "🏛️ Falhas de governo e regulação",
    "esc": "📜 Escolas do pensamento macroeconômico",
    "agr": "🧭 Agregados e conceitos básicos",
}

COM_NAB_COASE = "Com referência ao teorema de Coase, julgue (C ou E) os itens a seguir."
COM_RT_MICRO = "A respeito dos conceitos e teorias da microeconomia, julgue os itens a seguir."
COM_RT_FIRMA = ("A teoria da firma permite analisar a relação entre os custos de produção e as estruturas de "
                "mercado. A respeito deste tema, julgue as afirmações a seguir.")
COM_TJPA = ("Julgue os itens que se seguem, a respeito das políticas fiscal e monetária, do papel da dívida pública "
            "como fonte de financiamento e da função reguladora do Estado na economia.")
COM_NIDI_JUL = ("A respeito das Teorias das Externalidades e dos Bens Públicos, julgue como certo ou errado os itens "
                "a seguir.")
COM_ANTT_BATERIA = ("Em um prédio residencial, residem, em um apartamento, um casal e um bebê recém-nascido que "
                    "precisa dormir várias horas durante o dia; em outro apartamento, mora um baterista que tem de "
                    "ensaiar suas músicas durante o dia. Esses dois apartamentos são vizinhos. A respeito da "
                    "situação hipotética precedente, julgue o próximo item.")
COM_ANTT_VIA = ("Uma via genérica em uma cidade é um exemplo de bem público, pois apresenta as características de "
                "não exclusividade e não rivalidade no consumo. Considerando esse contexto, julgue os itens "
                "subsecutivos.")
COM_ANTT_REG = "Acerca da teoria da regulação e das estruturas de mercado, julgue os itens subsequentes."
COM_NIDI_59 = ("Os bens públicos e as externalidades são conceitos fundamentais na teoria econômica [...]. Julgue os "
               "itens a seguir.")
COM_NIDI_BENS = ("Sobre os diferentes tipos de bens, as falhas de mercado e o papel do Estado no ajuste da oferta e "
                 "correções de problemas decorrentes da livre flutuação dos mercados, julgue (C ou E) os itens a "
                 "seguir.")
COM_JB_ESTADO = ("A teoria dos mercados estuda como os agentes econômicos interagem em diferentes estruturas de "
                 "mercado [...]. Considerando a relação entre o Estado e diferentes estruturas de mercado existente "
                 "numa economia mista, julgue certo ou errado (C ou E) as assertivas a seguir.")
COM_BOZAN = ("Julgue as seguintes assertivas sobre a teoria econômica clássica e suas críticas no contexto "
             "keynesiano e da ortodoxia econômica.")

CARDS = [
    # ------------------------------------------------------------------ E2-L01180
    {
        "id": "ECO-E2-L01180-1", "fonte_ref": "E2-L01180", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_COASE,
        "rotulo_item": "Item",
        "assertiva": ("A solução de Coase é afetada pela presença de custos transacionais, que obstaculariza a geração "
                      "de acordos eficientes entre as partes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A solução de Coase é <u>afetada pela presença de custos transacionais</u>, que obstaculariza "
                      "a geração de acordos eficientes entre as partes."),
        "poucas": ("O teorema de Coase só garante a solução eficiente por barganha se os " + azb("custos de "
                   "transação") + " forem nulos (ou baixos). Com custos de negociar, fiscalizar e fazer cumprir o "
                   "acordo, a barganha pode não acontecer."),
        "destrinchando": [
            oc("Ronald Coase") + " (<i>The Problem of Social Cost</i>, 1960; Nobel de " + vd("1991") + ") mostrou "
            "que, com " + azb("direitos de propriedade bem definidos") + " e " + azb("custos de transação nulos")
            + ", as partes negociam até a alocação eficiente, seja quem for o titular do direito.",
            "Custos de transação são todos os custos de fechar e manter o acordo: identificar as partes, reunir "
            "informação sobre danos e custos de evitá-los, negociar, redigir o contrato e fiscalizar o "
            "cumprimento. Quando superam o ganho da barganha, ela simplesmente não ocorre e a externalidade "
            "persiste.",
            "Os custos crescem com o " + azb("número de partes") + " (poluição urbana atinge milhões), com a "
            "informação imperfeita (cada lado exagera seu dano ou seu custo) e com o " + azb("carona")
            + " (cada vítima espera que as outras paguem pela negociação).",
            "Por isso o teorema é lido ao contrário na literatura: ele mostra <b>por que</b> as externalidades "
            "persistem no mundo real e quando se justifica a ação do Estado (impostos de " + oc("Pigou")
            + ", regulação, mercado de licenças).",
            vm("Regra-âncora: Coase = direitos definidos + custo de transação zero → eficiência, qualquer que "
               "seja a distribuição inicial dos direitos."),
        ],
        "dissecando": (cz("[literalidade]") + " O item reproduz a principal ressalva do teorema. A concordância "
                       "“custos transacionais, que obstaculariza” é falha de redação, não de conteúdo. 🔥 Itens "
                       "de Coase quase sempre giram em torno de três palavras: custos de transação, direitos de "
                       "propriedade e “independentemente” da atribuição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A solução de Coase dispensa a definição de direitos de propriedade, bastando que os custos de "
            "transação sejam nulos.”</i> → ERRADO (os direitos precisam estar definidos)",
            "<i>“Com custos de transação nulos, o resultado eficiente independe de a quem se atribui o "
            "direito.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Sem custo de transação, os agentes privados podem negociar e resolver por conta própria "
                            "o problema das externalidades.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01181
    {
        "id": "ECO-E2-L01181-1", "fonte_ref": "E2-L01181", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_COASE,
        "rotulo_item": "Item",
        "assertiva": ("Segundo o teorema de Coase, é possível ter soluções privadas para as externalidades geradas "
                      "em uma economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo o teorema de Coase, <u>é possível</u> ter soluções privadas para as externalidades "
                      "geradas em uma economia."),
        "poucas": ("É a tese central de " + oc("Coase") + ": a externalidade pode ser resolvida por " + azb("barganha "
                   "privada") + ", sem imposto nem regulação, desde que haja direitos definidos e custos de "
                   "transação baixos."),
        "destrinchando": [
            "Até 1960, a resposta-padrão às externalidades era a de " + oc("Pigou") + " (<i>The Economics of "
            "Welfare</i>, 1920): o Estado tributa quem gera custo externo e subsidia quem gera benefício externo.",
            oc("Coase") + " mostrou que a externalidade é um problema <b>recíproco</b> (o fazendeiro sofre com o "
            "gado do vizinho, mas impedir o gado também custa ao criador) e que, com direitos definidos, a parte "
            "que mais valoriza o resultado paga à outra. Exemplo do próprio texto: se cercar a lavoura custa menos "
            "que o dano, a cerca sai — pagam o fazendeiro ou o criador, conforme o direito.",
            "Soluções privadas na prática: " + azb("negociação direta") + " entre vizinhos; " + azb("fusão")
            + " das partes (o apicultor e o pomar sob um mesmo dono internalizam a polinização); contratos; "
            "normas sociais e códigos morais; ações de responsabilidade civil.",
            "O teorema não afirma que essas soluções sempre funcionam: com muitas partes, informação imperfeita "
            "ou carona, a barganha falha e volta o espaço para impostos, regulação e licenças negociáveis.",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O “é possível” salva o item: a banca não "
                       "diz que a solução privada sempre ocorre, só que o teorema a admite. Itens com “sempre”, "
                       "“qualquer que sejam os custos” ou “dispensa direitos de propriedade” costumam ser os "
                       "ERRADOS do bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo o teorema de Coase, as externalidades sempre são resolvidas por negociação privada, "
            "dispensando a intervenção estatal.”</i> → ERRADO (modulador absoluto: depende de custos de "
            "transação baixos)",
            "<i>“A fusão entre a empresa que polui e a que sofre a poluição é uma forma de internalizar a "
            "externalidade.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["é possível"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito (CERTO), sem comentário.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01182
    {
        "id": "ECO-E2-L01182-1", "fonte_ref": "E2-L01182", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_NAB_COASE,
        "rotulo_item": "Item",
        "assertiva": ("O nível ótimo (minimização) de danos ambientais, tais como ameaças à fauna e à flora do país, "
                      "bem como os decorrentes de poluição sonora e atmosférica, pode ser determinado no âmbito do "
                      "teorema de Coase."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O nível ótimo (minimização) de danos ambientais, tais como ameaças à fauna e à flora do "
                       "país, bem como os decorrentes de poluição sonora e atmosférica, ")
                    + vm("pode ser determinado no âmbito do teorema de Coase") + az(".")),
        "poucas": ("Danos ambientais difusos envolvem " + azb("milhões de partes") + ", custos de transação "
                   "altíssimos, carona e direitos mal definidos: é justamente o caso em que a barganha de Coase "
                   "não funciona."),
        "destrinchando": [
            "A solução de " + oc("Coase") + " pressupõe poucas partes identificáveis, direitos de propriedade "
            "claros e custos de negociar baixos. Fauna, flora e ar são " + azb("bens públicos ou recursos "
            "comuns") + ": não há dono, não se exclui ninguém e os afetados são numerosos e dispersos.",
            "Com muitas vítimas, organizar a negociação custa caro e cada uma prefere pegar " + azb("carona")
            + " no esforço das demais. Com muitos poluidores, nem sempre se consegue atribuir a cada um a sua "
            "parcela do dano. Em ambos os casos não há contrato estável possível.",
            "Há ainda o problema intergeracional: as gerações futuras, que sofrerão a extinção de espécies, não "
            "podem sentar à mesa de negociação.",
            "Por isso a política ambiental recorre a instrumentos públicos: " + azb("impostos de Pigou") + ", "
            "padrões de emissão (comando e controle), " + azb("licenças negociáveis") + " (o mercado de carbono "
            "é uma solução “coasiana” criada pelo Estado, que define e distribui os direitos) e áreas protegidas.",
            vm("Regra-âncora: muitas partes + bem sem dono → custo de transação alto → Coase não se aplica."),
        ],
        "dissecando": (cz("[extrapolação]") + " O item estende o teorema a um caso que ele não cobre. A lista "
                       "longa de danos “difusos” (fauna, flora, ar, ruído) é a pista: em todos eles a outra "
                       "parte da negociação é a coletividade inteira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O dano causado pelo gado de um fazendeiro à lavoura do vizinho pode ser resolvido por "
            "negociação, nos termos do teorema de Coase.”</i> → CERTO",
            "<i>“A existência de muitas vítimas da poluição reduz os custos de transação, favorecendo a solução "
            "de Coase.”</i> → ERRADO (inversão: aumenta os custos)",
        ])],
        "reescrita": ("O nível ótimo (minimização) de danos ambientais, tais como ameaças à fauna e à flora do país, "
                      "bem como os decorrentes de poluição sonora e atmosférica, " + hl("dificilmente pode ser "
                      "alcançado por negociação privada") + " no âmbito do teorema de Coase" + hl(", por envolver "
                      "muitas partes e custos de transação elevados") + "."),
        "tipo_erro": ["EXTRAPOLACAO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": "A solução de Coase não funciona com muitas partes: dificuldade de organização, carona, "
                            "custos de transação altos; não se aplica a recursos comuns e bens públicos puros, e "
                            "exige direitos de propriedade definidos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ---- fim
]
