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
    # ------------------------------------------------------------------ E2-L01408
    {
        "id": "ECO-E2-L01408-1", "fonte_ref": "E2-L01408", "destino": "12", "subtema": H2["ext"],
        "tipo": "DISC", "banca": "Intensivo MM", "prova": "Intensivo Pré-TPS/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Responda à questão a seguir, sobre externalidades e eficiência na produção.",
        "rotulo_item": "Questão",
        "assertiva": "Defina o nível eficiente de produção no setor.",
        "gabarito": "RESPOSTA", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O nível eficiente de produção no setor é aquele em que o benefício marginal de uma unidade "
                      "adicional do produto é igual ao custo marginal social (custo marginal privado + custo "
                      "marginal externo)."),
        "poucas": ("Eficiência = " + vd("BMgS = CMgS") + ". Com externalidade negativa, o mercado iguala o "
                   "benefício ao custo <b>privado</b> e produz demais; o ótimo social exige incluir o custo "
                   "externo."),
        "destrinchando": [
            "Regra geral do bem-estar: vale produzir mais uma unidade enquanto o que ela acrescenta de benefício "
            "à sociedade superar o que ela custa à sociedade. O ponto de parada é " + azb("benefício marginal "
            "social = custo marginal social") + ".",
            azb("Custo marginal social") + " = custo marginal privado (insumos, salários, energia) + "
            + azb("custo marginal externo") + " (dano a terceiros não pago pela firma: poluição, ruído, "
            "congestionamento).",
            "No mercado competitivo, a oferta reflete só o CMg privado. Com externalidade negativa, CMgS > CMgP: "
            "o equilíbrio de mercado produz <b>acima</b> do eficiente e cobra preço <b>abaixo</b> do custo "
            "social. Com externalidade positiva no consumo, ocorre o contrário: BMgS > BMgP e o mercado produz "
            "<b>abaixo</b> do eficiente.",
            "Correções: o " + azb("imposto de Pigou") + " igual ao custo marginal externo no ponto ótimo faz a "
            "firma enxergar o CMgS; o " + azb("subsídio de Pigou") + " faz o consumidor enxergar o BMgS.",
            vm("Regra-âncora: eficiência sempre se mede com valores sociais — BMgS = CMgS."),
        ],
        "dissecando": (cz("[discursiva curta]") + " Em C/E, o conceito volta como “o equilíbrio de mercado com "
                       "externalidade negativa é eficiente” (ERRADO) ou “o nível eficiente iguala o benefício "
                       "marginal ao custo marginal privado” (ERRADO: falta o custo externo). A palavra-chave é "
                       "<b>social</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na presença de externalidade negativa, o nível eficiente de produção é aquele em que o "
            "benefício marginal iguala o custo marginal privado.”</i> → ERRADO (troca de conceito: é o custo "
            "marginal social)",
            "<i>“Com externalidade negativa, o mercado competitivo produz acima do nível socialmente "
            "eficiente.”</i> → CERTO",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Nível eficiente: benefício marginal de uma unidade adicional = custo marginal social.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: a frente da fonte trazia só o tópico (“nível eficiente de produção no setor”); "
                    "a pergunta foi formulada a partir dele"],
    },
    # ------------------------------------------------------------------ E2-L01409
    {
        "id": "ECO-E2-L01409-1", "fonte_ref": "E2-L01409", "destino": "12", "subtema": H2["info"],
        "tipo": "DISC", "banca": "Intensivo MM", "prova": "Intensivo Pré-TPS/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": "Responda à questão a seguir, sobre as falhas de mercado.",
        "rotulo_item": "Questão",
        "assertiva": "O que são mercados incompletos?",
        "gabarito": "RESPOSTA", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um mercado é incompleto quando um bem ou serviço não é ofertado, ainda que o custo de "
                      "produzi-lo esteja abaixo do preço que os consumidores estariam dispostos a pagar. É uma "
                      "falha de mercado: o setor privado deixa de ofertar, sobretudo por risco elevado ou "
                      "informação insuficiente (ex.: crédito de longo prazo, seguros)."),
        "poucas": ("Mercado incompleto = há quem pague mais do que o custo, mas o bem " + azb("não é ofertado")
                   + ". Típico de crédito de longo prazo e seguros, em que risco e informação travam a oferta "
                   "privada."),
        "destrinchando": [
            "Conceito-espelho: um " + azb("mercado completo") + " oferta todo bem ou serviço cujo custo de "
            "provisão é menor que o preço de reserva dos consumidores. Quando isso não acontece, há ganho de "
            "troca não realizado — ineficiência de Pareto.",
            "Por que falta oferta? Risco que o setor privado não quer ou não consegue diversificar; "
            + azb("informação assimétrica") + " (seleção adversa e risco moral afastam seguradoras e "
            "credores); horizontes longos e incerteza; custos de transação; falta de mercados futuros para "
            "riscos que ainda não existem.",
            "Exemplos clássicos: seguro contra desemprego ou contra quebra de safra, crédito para pequenos "
            "agricultores e estudantes, financiamento de longo prazo para infraestrutura. Nos países em "
            "desenvolvimento, o mercado de capitais raramente oferece prazos compatíveis com projetos de "
            "maturação longa.",
            "Resposta do Estado: provisão direta ou garantia — no " + rx("Brasil") + ", o " + rx("BNDES")
            + " no crédito de longo prazo, o crédito rural oficial, o seguro-desemprego, fundos garantidores.",
            "Mercados incompletos aparecem na lista de falhas de mercado de " + oc("Joseph Stiglitz")
            + " (<i>Economics of the Public Sector</i>), ao lado de falhas de concorrência, bens públicos, "
            "externalidades, falhas de informação e desemprego.",
        ],
        "dissecando": (cz("[discursiva curta]") + " Em C/E, a banca costuma inverter a lógica: “mercado "
                       "incompleto é aquele em que o preço supera o custo de produção” (ERRADO: o problema é a "
                       "<b>ausência</b> de oferta) ou confundi-lo com concorrência imperfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A ausência de seguro privado contra o desemprego pode ser explicada pela existência de "
            "mercados incompletos.”</i> → CERTO",
            "<i>“Mercados incompletos só surgem em estruturas de monopólio.”</i> → ERRADO (restrição indevida: "
            "decorrem de risco e informação)",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Mercado incompleto: bem não ofertado embora o custo esteja abaixo do preço de reserva; "
                            "setor privado não assume riscos; ex.: financiamento de longo prazo, BNDES.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: frente “OQ SÃO MERCADOS INCOMPLETOS?” normalizada"],
    },
    # ------------------------------------------------------------------ E2-L01413
    {
        "id": "ECO-E2-L01413-1", "fonte_ref": "E2-L01413", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "FCC", "prova": "ManausPrev/Analista Previdenciário/2021", "ano": 2021,
        "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo às externalidades e aos instrumentos para corrigi-las (item adaptado).",
        "rotulo_item": "Item",
        "assertiva": ("O atual risco de crise de abastecimento de energia elétrica no Brasil levou à adoção de "
                      "sobretaxas nas tarifas de consumo, o que equivale a um imposto de Pigou, dado o seu efeito "
                      "positivo sobre o meio ambiente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O atual risco de crise de abastecimento de energia elétrica no Brasil levou à adoção de "
                       "sobretaxas nas tarifas de consumo, o que ")
                    + vm("equivale a um imposto de Pigou, dado o seu efeito positivo sobre o meio ambiente")
                    + az(".")),
        "poucas": ("Imposto de " + oc("Pigou") + " corrige uma " + azb("externalidade") + " (custo social não "
                   "refletido no preço). A sobretaxa da crise hídrica é " + azb("gestão de demanda") + " e "
                   "repasse do custo da geração mais cara: não mira dano ambiental."),
        "destrinchando": [
            "O " + azb("imposto pigouviano") + " (" + oc("A. C. Pigou") + ", <i>The Economics of Welfare</i>, "
            "1920) é igual ao custo marginal externo no ponto ótimo: faz o agente pagar pelo dano que impõe a "
            "terceiros (ex.: tributo sobre carbono) e leva a produção ao nível socialmente eficiente.",
            "Na crise hídrica de " + rx("2021") + ", com reservatórios baixos, o sistema acionou mais "
            "termelétricas, de custo maior, e a tarifa ganhou um adicional (a bandeira de escassez hídrica). "
            "O objetivo era duplo: <b>cobrir</b> o custo privado mais alto da geração e <b>desestimular</b> o "
            "consumo para evitar racionamento e apagão.",
            "Isso é sinal de " + azb("escassez") + ", não correção de externalidade: o preço sobe porque o "
            "insumo ficou mais caro, como em qualquer mercado. Não há um dano a terceiros sendo precificado.",
            "O “efeito positivo sobre o meio ambiente” também não se sustenta: o despacho térmico eleva as "
            "emissões. Menos consumo ajuda, mas é efeito colateral, não o fundamento da medida.",
            vm("Regra-âncora: só é Pigou se o tributo internaliza um custo EXTERNO; preço que sobe por escassez "
               "não é Pigou."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item cola o rótulo “Pigou” em qualquer "
                       "tributo com efeito sobre o consumo e justifica com um benefício ambiental acidental. "
                       "Pergunte sempre: qual é a externalidade que o tributo corrige? Se a resposta for "
                       "“nenhuma”, não é Pigou."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um tributo sobre a emissão de carbono das termelétricas, fixado no valor do dano marginal "
            "causado, equivale a um imposto de Pigou.”</i> → CERTO",
            "<i>“O imposto de Pigou tem como objetivo principal a arrecadação de receitas para o governo.”</i> "
            "→ ERRADO (o objetivo é corrigir a externalidade; a receita é subproduto)",
        ])],
        "reescrita": ("O atual risco de crise de abastecimento de energia elétrica no Brasil levou à adoção de "
                      "sobretaxas nas tarifas de consumo, o que " + hl("não equivale a um imposto de Pigou: é "
                      "medida de gestão da demanda e de repasse do custo mais alto da geração, sem correção de "
                      "externalidade ambiental") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Pigou corrige externalidade negativa; as sobretaxas visam desestimular o consumo em "
                            "período crítico (seca, reservatórios baixos) e evitar apagão, não corrigir "
                            "externalidade ambiental.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: item adaptado pela fonte a partir de questão da FCC; o “atual risco” refere-se à "
                    "crise hídrica de 2021"],
    },
    # ------------------------------------------------------------------ E2-L01426
    {
        "id": "ECO-E2-L01426-1", "fonte_ref": "E2-L01426", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_RT_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("Dentre as soluções para a externalidade positiva da vacinação contra Covid 19, estão a "
                      "regulamentação do governo, por exemplo instituindo o passaporte da vacina, com a exigência "
                      "da vacinação para frequentar certos locais, e os impostos de Pigou, que são o aumento da "
                      "carga tributária para gerar receita e pagar pelas vacinas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Dentre as soluções para a externalidade positiva da vacinação contra Covid 19, estão a "
                       "regulamentação do governo, por exemplo instituindo o passaporte da vacina, com a exigência "
                       "da vacinação para frequentar certos locais, e os ")
                    + vm("impostos de Pigou, que são o aumento da carga tributária para gerar receita e pagar pelas "
                         "vacinas") + az(".")),
        "poucas": ("Externalidade <b>positiva</b> se corrige com " + azb("subsídio de Pigou") + " (barateia a "
                   "atividade); o " + azb("imposto de Pigou") + " é para externalidade negativa e não tem "
                   "finalidade arrecadatória."),
        "destrinchando": [
            "A vacina gera " + azb("externalidade positiva no consumo") + ": quem se vacina protege também os "
            "outros (imunidade coletiva). O benefício social supera o privado, e o mercado entrega vacinação "
            "<b>abaixo</b> do ótimo.",
            "Correções possíveis: " + azb("subsídio de Pigou") + " (vacina gratuita ou paga ao vacinado, igual "
            "ao benefício externo marginal); provisão pública direta (o " + rx("Programa Nacional de "
            "Imunizações") + " do SUS); " + azb("regulação") + " (obrigatoriedade, passaporte vacinal). Essa "
            "última parte do item está correta.",
            "O " + azb("imposto de Pigou") + " tributa a atividade que gera custo externo (poluição, cigarro, "
            "álcool) para reduzi-la ao nível ótimo. Aplicá-lo à vacinação a <b>reduziria</b> — o oposto do "
            "desejado.",
            "Além disso, a definição dada está errada: “aumentar a carga tributária para gerar receita” "
            "descreve tributação comum. O que caracteriza o tributo pigouviano é a função " + azb("corretiva")
            + " (alterar o incentivo na margem), não a arrecadação.",
            vm("Regra-âncora: externalidade negativa → imposto de Pigou; positiva → subsídio de Pigou."),
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " A primeira solução (regulação, passaporte) "
                       "está certa; o erro foi enxertado na segunda, com dois problemas: instrumento trocado "
                       "(imposto no lugar de subsídio) e definição deturpada (arrecadação no lugar de correção). "
                       "🔥 A banca adora pedir o sinal do instrumento pigouviano."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Subsídios de Pigou à vacinação aproximam o consumo do nível socialmente ótimo.”</i> → CERTO",
            "<i>“O imposto de Pigou ideal é aquele que maximiza a arrecadação do governo.”</i> → ERRADO (troca "
            "de conceito: iguala o custo marginal externo)",
        ])],
        "reescrita": ("Dentre as soluções para a externalidade positiva da vacinação contra Covid 19, estão a "
                      "regulamentação do governo, por exemplo instituindo o passaporte da vacina, com a exigência "
                      "da vacinação para frequentar certos locais, e os " + hl("subsídios de Pigou, que reduzem "
                      "o custo privado da vacinação e aproximam o consumo do nível socialmente ótimo") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Para externalidade positiva, subsídio de Pigou, não imposto; o passaporte vacinal é "
                            "regulação válida; aumentar a carga para financiar vacinas não é imposto de Pigou.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01761
    {
        "id": "ECO-E2-L01761-1", "fonte_ref": "E2-L01761", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": COM_RT_FIRMA,
        "rotulo_item": "Item",
        "assertiva": ("Por gerarem externalidades positivas no consumo, pode-se afirmar que no mercado de vacinas o "
                      "custo social de produção supera o custo privado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Por gerarem externalidades positivas no consumo, pode-se afirmar que no mercado de vacinas o ")
                    + vm("custo social de produção supera o custo privado") + az(".")),
        "poucas": ("Externalidade positiva <b>no consumo</b> mexe no lado do " + azb("benefício") + ": BMg social "
                   "> BMg privado. O custo de produzir a vacina não muda (CMg social = CMg privado)."),
        "destrinchando": [
            "Toda externalidade tem dois atributos: o <b>sinal</b> (positiva ou negativa) e o <b>lado</b> do "
            "mercado onde surge (produção ou consumo). O sinal diz se há custo ou benefício externo; o lado diz "
            "qual curva se descola da curva privada.",
            "Quatro casos: negativa na produção (poluição da fábrica) → " + vd("CMgS > CMgP") + "; positiva "
            "na produção (apicultor que poliniza o pomar) → CMgS < CMgP; negativa no consumo (fumo passivo) → "
            "BMgS < BMgP; positiva no consumo (vacina, educação) → " + vd("BMgS > BMgP") + ".",
            "Na vacina, quem se imuniza reduz o contágio dos outros: a curva de benefício social fica "
            "<b>acima</b> da demanda privada. A oferta continua a mesma. O mercado para em qm, <b>abaixo</b> "
            "do ótimo q*, com peso morto.",
            "O “custo social maior que o privado” é a assinatura da externalidade <b>negativa na produção</b> "
            "— o item misturou os dois atributos.",
            "Correção: " + azb("subsídio de Pigou") + " ao consumo igual ao benefício externo marginal, ou "
            "provisão pública gratuita.",
        ],
        "grafico_verso": "ECO-E2-L01761-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item usa a premissa certa (externalidade positiva no "
                       "consumo) e tira a conclusão de outro caso (custo social > privado = negativa na "
                       "produção). Pista: “no consumo” aponta para benefício, nunca para custo de produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mercado de vacinas, o benefício marginal social supera o benefício marginal privado, e o "
            "mercado tende a produzir abaixo do ótimo.”</i> → CERTO",
            "<i>“Na poluição industrial, o custo marginal privado supera o custo marginal social.”</i> → ERRADO "
            "(inversão: CMgS > CMgP)",
        ])],
        "reescrita": ("Por gerarem externalidades positivas no consumo, pode-se afirmar que no mercado de vacinas o "
                      + hl("benefício social do consumo supera o benefício privado") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode-se afirmar"], "dificuldade": 2,
        "comentario_fonte": "Externalidade positiva no consumo: benefício social > privado; custo social > privado "
                            "seria externalidade negativa na produção. Gráfico de subsídio pigouviano à educação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 525", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01761-1-V1, adaptada da educação para a vacina)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00045
    {
        "id": "ECO-E3-L00045-1", "fonte_ref": "E3-L00045", "destino": "12", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": COM_TJPA,
        "rotulo_item": "Item",
        "assertiva": ("As agências reguladoras no Brasil atuam exclusivamente na privatização de empresas "
                      "estatais, garantindo a eficiência do processo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As agências reguladoras no Brasil atuam ")
                    + vm("exclusivamente na privatização de empresas estatais, garantindo a eficiência do "
                         "processo") + az(".")),
        "poucas": ("As agências fazem " + azb("regulação setorial permanente") + " (normas, tarifas, contratos de "
                   "concessão, qualidade, fiscalização). Quem conduz privatizações é o programa de desestatização, "
                   "não a agência."),
        "destrinchando": [
            "As agências nasceram na reforma do Estado dos anos 1990, junto com as privatizações e concessões: "
            + rx("ANEEL") + " (" + vd("Lei 9.427/1996") + "), " + rx("Anatel") + " (" + vd("Lei 9.472/1997")
            + "), " + rx("ANP") + " (" + vd("Lei 9.478/1997") + "), depois Anvisa, ANS, ANA, ANTT, Antaq e "
            "outras. A ideia: se o Estado deixa de produzir, precisa passar a <b>regular</b> quem produz.",
            "Funções: editar normas técnicas; fixar ou revisar tarifas; celebrar e fiscalizar contratos de "
            "concessão e autorizações; zelar pela qualidade e continuidade do serviço; arbitrar conflitos entre "
            "empresas e usuários; aplicar sanções. Atuam em " + azb("monopólios naturais") + ", serviços "
            "públicos e mercados com falhas de informação (saúde suplementar, medicamentos).",
            "A " + vd("Lei 13.848/2019") + " (Lei Geral das Agências) reforçou a autonomia: mandatos fixos e "
            "não coincidentes dos dirigentes, autonomia administrativa e financeira, " + azb("Análise de "
            "Impacto Regulatório") + " obrigatória e consultas públicas.",
            "A desestatização em si é conduzida pelo Programa Nacional de Desestatização, com o " + rx("BNDES")
            + " como gestor; a agência entra antes (modelagem regulatória) e, sobretudo, depois, por todo o "
            "prazo da concessão.",
            vm("Regra-âncora: agência reguladora = regulação contínua do setor, com ou sem empresa estatal nele."),
        ],
        "dissecando": (cz("[modulador absoluto · restrição indevida]") + " O “exclusivamente” reduz uma função "
                       "permanente a um evento pontual. 🔥 CEBRASPE usa muito esse molde: atribuição real "
                       "(as agências se relacionam com as privatizações) + modulador absoluto que a torna falsa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As agências reguladoras brasileiras foram criadas, em grande parte, no contexto das "
            "privatizações e concessões da década de 1990.”</i> → CERTO",
            "<i>“A Lei 13.848/2019 vedou a realização de consultas públicas pelas agências reguladoras.”</i> → "
            "ERRADO (inversão: a lei as prevê)",
        ])],
        "reescrita": ("As agências reguladoras no Brasil atuam " + hl("na regulação e na fiscalização permanentes de "
                      "setores específicos — normas técnicas, tarifas, contratos de concessão e qualidade —, não "
                      "se limitando à") + " privatização de empresas estatais."),
        "tipo_erro": ["GENERALIZACAO", "RESTRICAO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": "Agências fazem regulação setorial (normas, tarifas, concessões, qualidade, "
                            "fiscalização), função permanente; não atuam exclusivamente na privatização.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ---- fim
]
