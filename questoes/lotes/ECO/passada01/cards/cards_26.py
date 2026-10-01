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
    # ------------------------------------------------------------------ E3-L00068
    {
        "id": "ECO-E3-L00068-1", "fonte_ref": "E3-L00068", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("Quando o Brasil emprega uma política de restrição à exportação de carne bovina para a Europa "
                      "e, consequentemente, isso provoca um aumento no preço dos bens substitutos, como da carne de "
                      "porco ou frango, nos países europeus, isso pode ser caracterizado como uma externalidade "
                      "negativa da política de restrição brasileira."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Quando o Brasil emprega uma política de restrição à exportação de carne bovina para a Europa "
                       "e, consequentemente, isso provoca um aumento no preço dos bens substitutos, como da carne "
                       "de porco ou frango, nos países europeus, isso ")
                    + vm("pode ser caracterizado como uma externalidade negativa") + az(" da política de "
                                                                                       "restrição brasileira.")),
        "poucas": ("Efeito transmitido <b>pelos preços</b> não é externalidade (falha de mercado): é o mercado "
                   "funcionando. Externalidade é efeito sobre terceiros " + azb("por fora do sistema de preços")
                   + "."),
        "destrinchando": [
            azb("Externalidade") + " (no sentido de falha de mercado, também chamada " + azb("tecnológica")
            + "): a ação de um agente altera diretamente o bem-estar ou a produção de outro, sem passar pelo "
            "mercado e sem compensação. Exemplos: fábrica que polui o rio dos pescadores, ruído do aeroporto, "
            "abelhas que polinizam o pomar vizinho.",
            "O caso do item: a restrição reduz a oferta de carne bovina na Europa → o preço sobe → os "
            "consumidores migram para os " + azb("substitutos") + " (elasticidade-preço cruzada positiva) → a "
            "demanda por porco e frango sobe → o preço deles sobe. Tudo isso ocorre <b>dentro</b> do sistema de "
            "preços, que está sinalizando a nova escassez.",
            "Esse tipo de efeito tem nome técnico: " + azb("externalidade pecuniária") + ". Apesar do nome, "
            "não gera ineficiência nem justifica imposto ou subsídio: o que um perde com o preço maior, o "
            "vendedor ganha. Se todo efeito via preços fosse falha de mercado, qualquer compra seria "
            "externalidade (toda demanda adicional encarece o bem para o próximo comprador).",
            "Contraste útil em política comercial: haveria externalidade tecnológica se, por exemplo, a "
            "produção exportadora poluísse um rio que atravessa a fronteira.",
            vm("Regra-âncora: passou pelo preço → não é externalidade; não passou pelo preço e não foi "
               "compensado → é externalidade."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item descreve corretamente a cadeia de preços e cola "
                       "nela o rótulo errado. A palavra “consequentemente” e a menção a bens substitutos "
                       "entregam o mecanismo: é estática comparativa de oferta e demanda, não falha de mercado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento do preço do frango na Europa, decorrente da restrição brasileira, reflete o "
            "funcionamento do sistema de preços em mercados de bens substitutos.”</i> → CERTO",
            "<i>“O ruído de um aeroporto que reduz o bem-estar dos moradores vizinhos é exemplo de externalidade "
            "pecuniária.”</i> → ERRADO (troca de conceito: é externalidade tecnológica)",
        ])],
        "reescrita": ("Quando o Brasil emprega uma política de restrição à exportação de carne bovina para a Europa e, "
                      "consequentemente, isso provoca um aumento no preço dos bens substitutos, como da carne de "
                      "porco ou frango, nos países europeus, isso " + hl("não") + " pode ser caracterizado como "
                      "uma externalidade negativa da política de restrição brasileira" + hl(", mas como ajuste "
                      "normal de mercado, transmitido pelos preços") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": "Efeito de mercado normal (oferta menor, migração para substitutos, preço sobe), não "
                            "externalidade; externalidade exige efeito não mediado por preços; é externalidade "
                            "pecuniária, que não causa ineficiência.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 5", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (ilegível na transcrição)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00069
    {
        "id": "ECO-E3-L00069-1", "fonte_ref": "E3-L00069", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("As características inerentes aos Recursos de Uso Comum fazem com que o livre acesso a esses "
                      "bens possa resultar em uma alocação socialmente eficiente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As características inerentes aos Recursos de Uso Comum fazem com que o livre acesso a esses "
                       "bens possa resultar em uma alocação socialmente ") + vm("eficiente") + az(".")),
        "poucas": ("Recurso comum = " + azb("rival e não excludente") + ". Com livre acesso, cada usuário ignora "
                   "o custo que impõe aos demais e o recurso é " + azb("sobreutilizado") + ": a "
                   + azb("tragédia dos comuns") + "."),
        "destrinchando": [
            "Matriz de bens (rivalidade × exclusão): " + azb("privados") + " (rivais e excludentes: sorvete, "
            "roupa); " + azb("de clube") + " (excludentes e não rivais: TV a cabo, estrada com pedágio sem "
            "congestionamento); " + azb("recursos comuns") + " (rivais e não excludentes: peixes no oceano, "
            "pastagem aberta, aquífero); " + azb("públicos") + " (nem rivais nem excludentes: defesa nacional, "
            "sirene de alerta).",
            "No recurso comum, o benefício de pescar mais um peixe é todo do pescador; o custo — menos peixe e "
            "estoque menor para os outros e para o futuro — é repartido entre todos. Cada um explora até o "
            "ponto em que o benefício <b>privado</b> iguala o custo <b>privado</b>, além do ótimo social: "
            "sobrepesca, dissipação da renda, colapso do estoque. É uma " + azb("externalidade negativa")
            + " entre usuários.",
            oc("Garrett Hardin") + " popularizou a expressão em <i>The Tragedy of the Commons</i> (" + vd("1968")
            + "). Caso clássico: o colapso do bacalhau na Terra Nova, com moratória em " + vd("1992") + ".",
            "Soluções: cotas, licenças e defeso (regulação); direitos de propriedade (privados ou cotas "
            "individuais transferíveis); tributos sobre o uso; e a " + azb("gestão comunitária") + " estudada "
            "por " + oc("Elinor Ostrom") + " (<i>Governing the Commons</i>, 1990; Nobel de " + vd("2009")
            + "). Todas restringem o livre acesso.",
            vm("Regra-âncora: recurso comum + livre acesso → uso excessivo → ineficiência."),
        ],
        "dissecando": (cz("[inversão]") + " Todo o item é fiel até a última palavra: o erro está em "
                       "“eficiente”. O “possa” ainda tenta proteger a frase, mas não salva: a ineficiência é "
                       "consequência das próprias características do recurso, não um acaso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A gestão comunitária com regras de acesso, monitoramento e sanções pode evitar a tragédia dos "
            "comuns.”</i> → CERTO",
            "<i>“Os recursos comuns são não rivais e não excludentes.”</i> → ERRADO (troca de conceito: são "
            "rivais)",
        ])],
        "reescrita": ("As características inerentes aos Recursos de Uso Comum fazem com que o livre acesso a esses "
                      "bens possa resultar em uma alocação socialmente " + hl("ineficiente, com uso excessivo do "
                      "recurso (a tragédia dos comuns)") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["possa"], "dificuldade": 1,
        "comentario_fonte": "Livre acesso a recursos comuns (rivais e não excludentes) gera a tragédia dos comuns "
                            "(Hardin, 1968): sobreuso e ineficiência; soluções de Ostrom, regulação, propriedade, "
                            "tributação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 6", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida no 📖 (matriz rivalidade × exclusão)"},
                          {"ref": "IMAGEM 7-12", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (ilegível na transcrição)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00070
    {
        "id": "ECO-E3-L00070-1", "fonte_ref": "E3-L00070", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": COM_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("Se duas empresas poluidoras possuem processos produtivos diferentes e diferentes custos de "
                      "redução de emissões, taxas sobre a quantidade de poluente emitida podem ser preferíveis à "
                      "imposição de um limite permitido."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se duas empresas poluidoras possuem processos produtivos diferentes e <u>diferentes custos de "
                      "redução de emissões</u>, taxas sobre a quantidade de poluente emitida <u>podem ser "
                      "preferíveis</u> à imposição de um limite permitido."),
        "poucas": ("Com custos de abatimento diferentes, a taxa faz cada firma reduzir até " + vd("CMgA = t")
                   + ": quem abate barato abate mais, e a meta é atingida ao " + azb("menor custo total")
                   + ". O limite uniforme ignora essa diferença."),
        "destrinchando": [
            azb("Custo marginal de abatimento") + " (CMgA) é quanto custa reduzir mais uma tonelada de poluente. "
            "Ele varia entre firmas (tecnologia, idade da planta) e cresce à medida que se abate mais.",
            "Com uma " + azb("taxa") + " t por tonelada emitida, a firma abate enquanto abater for mais barato "
            "que pagar a taxa: para em CMgA = t. Como t é igual para todas, os custos marginais se "
            + azb("igualam") + " — condição de custo mínimo (princípio equimarginal).",
            "Exemplo do gráfico: CMgA₁ = 0,5a e CMgA₂ = 1,5a; meta de 16 t. Taxa de 6 → firma 1 abate "
            + vd("12") + ", firma 2 abate " + vd("4") + "; custo total " + vd("36 + 12 = 48") + ". Limite "
            "uniforme de 8 para cada → custos " + vd("16 + 48 = 64") + ", com CMgA de 4 numa e 12 na outra: "
            "transferir abatimento da firma 2 para a 1 baratearia a mesma meta.",
            "Outras vantagens da taxa: o regulador não precisa conhecer o custo de cada firma (informação "
            "descentralizada) e há incentivo contínuo a inovar, pois cada tonelada a menos poupa t. As "
            + azb("licenças negociáveis") + " (<i>cap-and-trade</i>, como o mercado europeu de carbono) obtêm "
            "a mesma equalização, fixando a quantidade e deixando o preço surgir no mercado.",
            "Por que “podem ser”: com a taxa, a quantidade final emitida é incerta. Se o dano cresce muito "
            "acima de certo nível (risco catastrófico), o limite pode ser preferível — é o debate preços × "
            "quantidades de " + oc("Weitzman") + " (1974).",
        ],
        "grafico_verso": "ECO-E3-L00070-1-V1",
        "dissecando": (cz("[modulador relativo · literalidade]") + " A condição (“custos de redução "
                       "diferentes”) é exatamente a que dá vantagem à taxa, e o “podem ser preferíveis” evita a "
                       "generalização. 🔥 O mesmo item aparece em outros simulados com redação quase idêntica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se todas as empresas tiverem custos de abatimento idênticos, o limite uniforme e a taxa podem "
            "atingir a mesma meta com o mesmo custo total.”</i> → CERTO",
            "<i>“Com a taxa sobre emissões, a empresa de maior custo de abatimento reduz mais a poluição.”</i> "
            "→ ERRADO (inversão: reduz menos e paga mais taxa)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["podem"], "dificuldade": 2,
        "comentario_fonte": "Taxa permite que cada firma abata até CMgA = taxa, minimizando o custo total; limite "
                            "uniforme é rígido. Exemplos numéricos, Weitzman (preços × quantidades), cap-and-trade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 13", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (ilegível na transcrição)"},
                          {"ref": "IMAGEM 14", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00070-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00268-1 (Nidi, Fevereiro/2025) traz a mesma assertiva com redação "
                    "ampliada; os dois cards foram mantidos e usam o mesmo gráfico"],
    },
    # ------------------------------------------------------------------ E3-L00071
    {
        "id": "ECO-E3-L00071-1", "fonte_ref": "E3-L00071", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": COM_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("Como o bem público é de uso não-disputável, para determinar o seu valor temos de somar os "
                      "benefícios marginais de todas as pessoas que o consomem."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Como o bem público é de uso <u>não-disputável</u>, para determinar o seu valor temos de "
                      "<u>somar os benefícios marginais</u> de todas as pessoas que o consomem."),
        "poucas": ("Não rivalidade = todos consomem a <b>mesma</b> quantidade. O valor social de mais uma unidade é "
                   "a " + azb("soma vertical") + " das disposições a pagar: " + vd("ΣBMg") + "."),
        "destrinchando": [
            "“Uso não disputável” é sinônimo de " + azb("não rivalidade") + ": o consumo de um não reduz o do "
            "outro (o farol ilumina todos os navios, a defesa protege todos os moradores).",
            "Bem privado: cada um consome uma quantidade diferente, e a demanda de mercado é a soma "
            + azb("horizontal") + " (somam-se as quantidades a cada preço). Bem público: a quantidade é a mesma "
            "para todos, e o que se soma são os valores — soma " + azb("vertical") + " das curvas de benefício "
            "marginal, a cada quantidade.",
            "Exemplo: o próximo poste vale R$ 50 para Maria, R$ 30 para João e R$ 20 para Ana: o benefício "
            "marginal social é " + vd("R$ 100") + ". Se o poste custar R$ 90, vale instalar, embora nenhum "
            "deles, sozinho, pagasse por ele.",
            "Daí a " + azb("condição de Samuelson") + " (" + oc("Paul Samuelson") + ", <i>The Pure Theory of "
            "Public Expenditure</i>, " + vd("1954") + "): o nível eficiente é aquele em que " + vd("ΣBMg = CMg")
            + ". No gráfico: 3,50 + 2,00 = 5,50 = CMg em q* = 2.",
            "O problema prático: como ninguém pode ser excluído, cada um tende a " + azb("subdeclarar") + " sua "
            "disposição a pagar (carona). A soma verdadeira não aparece no mercado — por isso o financiamento "
            "costuma ser por tributos.",
        ],
        "grafico_verso": "ECO-E3-L00266-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " O item reproduz Pindyck quase literalmente, mas usa "
                       "“não-disputável” em vez de “não rival” e “valor” em vez de “benefício marginal social” "
                       "— quem não reconhece os sinônimos desconfia. A armadilha clássica é trocar “somar os "
                       "benefícios” por “somar as quantidades”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de demanda de mercado de um bem público obtém-se pela soma horizontal das curvas "
            "individuais.”</i> → ERRADO (troca de conceito: soma vertical)",
            "<i>“Para bens privados, a eficiência exige que o benefício marginal de cada consumidor iguale o "
            "custo marginal.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Não rivalidade: soma vertical dos benefícios marginais (regra de Samuelson); ΣBMg = "
                            "CMg define o nível eficiente; bem privado soma horizontal; carona subdeclara.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 15", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida no 📖 (matriz rivalidade × exclusão)"}],
        "alertas": ["nota_redacao: gráfico do verso compartilhado com ECO-E3-L00266-1 (mesmo mecanismo: soma "
                    "vertical e condição de Samuelson)"],
    },
    # ------------------------------------------------------------------ E3-L00158
    {
        "id": "ECO-E3-L00158-1", "fonte_ref": "E3-L00158", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ANTT_BATERIA,
        "rotulo_item": "Item",
        "assertiva": ("Não há externalidade causada pelo baterista, uma vez que a perda de utilidade pelo casal por "
                      "causa do ruído dos ensaios é compensada pelo aumento da utilidade do baterista ao cumprir "
                      "sua atividade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Não há") + az(" externalidade causada pelo baterista, uma vez que a perda de utilidade pelo "
                                      "casal por causa do ruído dos ensaios ")
                    + vm("é compensada pelo aumento da utilidade do baterista") + az(" ao cumprir sua atividade.")),
        "poucas": ("Há " + azb("externalidade negativa") + ": o ruído reduz o bem-estar do casal sem passar pelo "
                   "mercado e sem pagamento. O ganho do próprio baterista não “compensa” nada — ele não paga ao "
                   "vizinho."),
        "destrinchando": [
            "Definição: externalidade é o efeito da ação de um agente sobre o bem-estar de terceiros que não "
            "participam da decisão, " + azb("sem mediação de preços e sem compensação") + ". O ruído do ensaio "
            "que acorda o bebê se encaixa por inteiro.",
            "A existência da externalidade não depende do saldo de utilidades. Mesmo que o ganho do baterista "
            "superasse a perda do casal, o casal continua arcando com um custo que não escolheu e pelo qual não "
            "recebe nada. Comparar ganhos e perdas serve para outra pergunta: qual é o nível <b>eficiente</b> de "
            "ensaio — não se há externalidade.",
            "Compensação, em economia, é transferência efetiva (o baterista paga ao casal, ou o casal paga ao "
            "baterista para ensaiar em outro horário). Utilidade de uma pessoa não se transfere para outra.",
            "Soluções: " + azb("barganha de Coase") + " (vizinhos combinam horários ou isolamento acústico — "
            "poucas partes, custo de transação baixo); regra do condomínio ou lei do silêncio (regulação); "
            "multa por barulho (lógica pigouviana).",
            vm("Regra-âncora: efeito sobre terceiro + fora do preço + sem compensação = externalidade, qualquer "
               "que seja o saldo de bem-estar."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O item troca o critério de existência da "
                       "externalidade (efeito não compensado sobre terceiro) por um balanço de utilidades entre "
                       "pessoas diferentes. “Compensada” é a palavra-gatilho: ninguém pagou ninguém."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se os custos de transação forem baixos, o casal e o baterista podem chegar, por negociação, a "
            "uma solução eficiente para o ruído.”</i> → CERTO",
            "<i>“O ruído dos ensaios constitui externalidade positiva, pois eleva a utilidade do "
            "baterista.”</i> → ERRADO (troca de conceito: o efeito sobre terceiros é negativo)",
        ])],
        "reescrita": (hl("Há") + " externalidade " + hl("negativa") + " causada pelo baterista, uma vez que a perda "
                      "de utilidade do casal por causa do ruído dos ensaios " + hl("não é compensada, ainda que") +
                      " o baterista ganhe utilidade ao cumprir sua atividade."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Ruído é externalidade negativa: afeta o casal sem mediação de preço nem compensação; "
                            "o saldo de utilidades não é critério; soluções: regulação, Coase, multas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00159
    {
        "id": "ECO-E3-L00159-1", "fonte_ref": "E3-L00159", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ANTT_VIA,
        "rotulo_item": "Item",
        "assertiva": ("Uma avenida, quando congestionada, deixa de ser um bem público, pois, nesse caso, passa a "
                      "apresentar rivalidade no consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma avenida, quando <u>congestionada</u>, deixa de ser um bem público, pois, nesse caso, "
                      "passa a apresentar <u>rivalidade no consumo</u>."),
        "poucas": ("No congestionamento, cada carro a mais atrasa os outros: surge " + azb("rivalidade")
                   + ". Sem pedágio, a via continua não excludente — vira " + azb("recurso comum") + ", não bem "
                   "público."),
        "destrinchando": [
            "A classificação de uma via muda com duas variáveis, pedágio (exclusão) e congestionamento "
            "(rivalidade):",
            "Sem pedágio e sem congestionamento → não excludente e não rival → " + azb("bem público") + ".",
            "Sem pedágio e congestionada → não excludente e rival → " + azb("recurso comum") + " (sofre a "
            "tragédia dos comuns: todos entram, ninguém paga o atraso que impõe aos demais).",
            "Com pedágio e sem congestionamento → excludente e não rival → " + azb("bem de clube") + ".",
            "Com pedágio e congestionada → excludente e rival → " + azb("bem privado") + ". É a classificação "
            "de " + oc("Mankiw") + ", que põe as estradas nos quatro quadrantes.",
            "O congestionamento é uma " + azb("externalidade negativa") + " entre motoristas. Daí as propostas "
            "de " + azb("pedágio urbano") + " (Londres, Singapura): cobrar no horário de pico internaliza o "
            "custo do atraso e transforma o recurso comum em bem excludente.",
            vm("Regra-âncora: rivalidade muda com a lotação; exclusão muda com a cobrança."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " A intuição jurídica diz que “a avenida é pública”; o item "
                       "usa o conceito econômico, em que “público” depende das propriedades do bem, não do "
                       "dono. O comando define bem público pelas duas características: perder uma basta para "
                       "deixar de sê-lo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma avenida congestionada e sem pedágio é um recurso comum.”</i> → CERTO",
            "<i>“Uma avenida congestionada passa a ser excludente, pois motoristas são impedidos de "
            "utilizá-la.”</i> → ERRADO (troca de conceito: muda a rivalidade, não a exclusão)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Sem pedágio e sem congestionamento: bem público; sem pedágio e congestionada: bem "
                            "comum; com pedágio e congestionada: bem privado. Diagrama decisório da via pública.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 169", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "texto (absorvido no 📖 como lista de casos)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00160
    {
        "id": "ECO-E3-L00160-1", "fonte_ref": "E3-L00160", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ANTT_VIA,
        "rotulo_item": "Item",
        "assertiva": "Uma rua em um condomínio fechado não é um bem público, por ser exclusiva.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma rua em um condomínio fechado não é um bem público, por ser <u>exclusiva</u>."),
        "poucas": ("A portaria do condomínio impede o acesso de quem não é morador: o bem é " + azb("excludente")
                   + ". Faltando a não exclusão, não é bem público — sem congestionamento, é " + azb("bem de "
                   "clube") + "."),
        "destrinchando": [
            "Bem público exige as duas propriedades ao mesmo tempo: " + azb("não exclusão") + " (não se consegue "
            "impedir o uso por quem não paga) e " + azb("não rivalidade") + " (o uso de um não reduz o do "
            "outro). Basta faltar uma para o bem sair do quadrante.",
            "A rua do condomínio fechado tem controle de acesso: só moradores e autorizados entram, e o acesso "
            "é custeado pela taxa condominial. Isso é exclusão.",
            "Como a rua normalmente não está congestionada, segue não rival: o bem fica no quadrante "
            + azb("excludente e não rival") + " — os " + azb("bens de clube") + " (ou bens artificialmente "
            "escassos), como TV a cabo, academia, clube recreativo.",
            "Atenção ao vocabulário: “público” em economia não significa “de propriedade do Estado”. Há bens "
            "providos pelo Estado que são privados no sentido econômico (vaga em escola pública é rival e "
            "excludente) e bens públicos providos por particulares.",
            "Os clubes resolvem o carona pela exclusão: quem não paga a taxa não entra. Por isso podem ser "
            "providos pelo mercado ou por arranjos coletivos privados, sem tributo.",
        ],
        "dissecando": (cz("[literalidade]") + " Aplicação direta da definição dada no próprio comando. O risco "
                       "é o candidato confundir “público” com “aberto ao público” ou com propriedade estatal, "
                       "ou achar que a rua precisaria ser também rival para deixar de ser bem público."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma rua em condomínio fechado, sem congestionamento, é exemplo de bem de clube.”</i> → CERTO",
            "<i>“Uma rua em condomínio fechado não é bem público porque é rival no consumo.”</i> → ERRADO "
            "(troca de conceito: o que falta é a não exclusão)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Rua de condomínio fechado é exclusiva (acesso restrito), logo não é bem público; "
                            "diagrama decisório da via pública.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 169", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "texto (absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00175
    {
        "id": "ECO-E3-L00175-1", "fonte_ref": "E3-L00175", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ANTT_REG,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o teorema de Coase, desde que atribuído o direito de propriedade em favor do "
                      "agente que sofre os efeitos de uma externalidade negativa, a negociação privada entre quem "
                      "produz e quem sofre os efeitos da externalidade resultará em uma alocação socialmente "
                      "eficiente na ausência de custos de transação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o teorema de Coase, ")
                    + vm("desde que atribuído o direito de propriedade em favor do agente que sofre os efeitos de "
                         "uma externalidade negativa")
                    + az(", a negociação privada entre quem produz e quem sofre os efeitos da externalidade "
                         "resultará em uma alocação socialmente eficiente na ausência de custos de transação.")),
        "poucas": ("Para " + oc("Coase") + ", basta que o direito esteja " + azb("bem definido") + " — a favor "
                   "de " + vm("qualquer") + " das partes. A atribuição muda quem paga a quem (distribuição), não a "
                   "eficiência."),
        "destrinchando": [
            "Enunciado do teorema: com direitos de propriedade bem definidos e custos de transação nulos, a "
            "barganha leva à alocação eficiente " + azb("independentemente de a quem o direito é atribuído")
            + ".",
            "O exemplo do próprio " + oc("Coase") + " (<i>The Problem of Social Cost</i>, 1960): o gado do "
            "criador invade a lavoura vizinha. Se o direito é do criador, o agricultor paga a cerca quando o "
            "dano supera o custo dela. Se o direito é do agricultor, o criador constrói a cerca (ou indeniza, "
            "se a cerca custar mais que o dano). Em ambos os casos a cerca sai <b>se e somente se</b> é "
            "eficiente que saia.",
            "O que muda com a atribuição é a " + azb("distribuição") + " da renda: quem tem o direito recebe; "
            "quem não tem paga. A " + azb("eficiência") + " (quanto de externalidade sobra) é a mesma.",
            "Ressalvas da literatura: efeitos renda grandes podem alterar o resultado; informação assimétrica "
            "e custos de transação positivos fazem a atribuição voltar a importar (aí o direito deve ir para "
            "quem tem menor custo de evitar o dano).",
            vm("Regra-âncora: Coase exige direito DEFINIDO, não direito da VÍTIMA."),
        ],
        "dissecando": (cz("[restrição indevida]") + " A expressão “desde que” transforma uma das atribuições "
                       "possíveis em condição necessária. O resto (negociação privada, custos de transação "
                       "nulos, eficiência) está certo, o que induz a marcar CERTO. 🔥 Variante frequente: “o "
                       "resultado depende de quem detém o direito” (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo teorema de Coase, a atribuição inicial dos direitos de propriedade afeta a distribuição "
            "da renda entre as partes, mas não a eficiência da alocação.”</i> → CERTO",
            "<i>“O teorema de Coase dispensa a definição de direitos de propriedade.”</i> → ERRADO (os "
            "direitos precisam estar definidos)",
        ])],
        "reescrita": ("De acordo com o teorema de Coase, " + hl("qualquer que seja o agente em favor do qual se "
                      "atribua o direito de propriedade — quem produz ou quem sofre a externalidade —") + ", a "
                      "negociação privada entre quem produz e quem sofre os efeitos da externalidade resultará em "
                      "uma alocação socialmente eficiente na ausência de custos de transação."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["desde que"], "dificuldade": 2,
        "comentario_fonte": "Coase: sem custos de transação e com direitos bem definidos, a alocação é eficiente "
                            "independentemente de quem detém o direito; não é preciso atribuí-lo à vítima. Exemplo "
                            "das fazendas (gado × lavoura).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 221", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖 (exemplo das fazendas)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00177
    {
        "id": "ECO-E3-L00177-1", "fonte_ref": "E3-L00177", "destino": "12", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": COM_ANTT_REG,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria da competição entre grupos de interesse, a regulação se prestaria a "
                      "atender às necessidades dos grupos de interesse que são capazes de exercer maior pressão "
                      "sobre os reguladores, uma vez que esses grupos são mais capazes de contribuir com os "
                      "objetivos individuais desses agentes e de manter ou ampliar seu <i>status</i> político."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a teoria da competição entre grupos de interesse, a regulação se prestaria a "
                      "atender às necessidades dos grupos de interesse que são capazes de exercer <u>maior "
                      "pressão</u> sobre os reguladores, uma vez que esses grupos são mais capazes de contribuir "
                      "com os <u>objetivos individuais</u> desses agentes e de manter ou ampliar seu <i>status</i> "
                      "político."),
        "poucas": ("Na " + azb("teoria econômica da regulação") + ", o regulador maximiza o próprio apoio "
                   "político; a regra resultante favorece quem pressiona mais, não necessariamente o interesse "
                   "público nem só a indústria."),
        "destrinchando": [
            "Três estágios das teorias da regulação (taxonomia de " + oc("Viscusi, Vernon e Harrington")
            + "):",
            azb("Interesse público") + ": a regulação corrige falhas de mercado (monopólio natural, "
            "externalidades); o regulador é um agente técnico e benevolente. Visão normativa — não explica por "
            "que tantas regras beneficiam os regulados.",
            azb("Captura") + ": a agência acaba servindo ao setor regulado, que é concentrado, organizado e "
            "detém a informação técnica. " + oc("George Stigler") + " (<i>The Theory of Economic Regulation</i>, "
            + vd("1971") + ") deu-lhe forma econômica: a regulação é “comprada” pela indústria (barreiras à "
            "entrada, preços mínimos, subsídios).",
            azb("Competição entre grupos de interesse") + ": " + oc("Sam Peltzman") + " (" + vd("1976")
            + ") modela o regulador como maximizador de apoio político, que pondera produtores e consumidores e "
            "escolhe um meio-termo; " + oc("Gary Becker") + " (" + vd("1983") + ") modela a disputa entre "
            "grupos de pressão: vence quem converte recursos em influência com mais eficiência, e o peso morto "
            "da regra limita as transferências.",
            "Por que grupos pequenos ganham: " + oc("Mancur Olson") + " (<i>A Lógica da Ação Coletiva</i>, "
            + vd("1965") + ") — benefícios concentrados e custos difusos; em grupos grandes, cada membro "
            "ganha pouco e prefere pegar carona.",
            "Antídotos institucionais (no " + rx("Brasil") + ", a Lei 13.848/2019): mandatos fixos, "
            "transparência, consultas públicas e Análise de Impacto Regulatório.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item reescreve a definição da teoria (regulador "
                       "preocupado com o próprio poder; regra desenhada para o grupo de maior pressão "
                       "relativa). A armadilha seria confundi-la com a teoria do interesse público, que "
                       "pressupõe regulador benevolente."),
        "modulos": [("📚 Autores e teses", [
            oc("Stigler") + " (1971) → a regulação é adquirida pela indústria e desenhada em seu benefício.",
            oc("Peltzman") + " (1976) → o regulador equilibra ganhos de produtores e consumidores para "
            "maximizar votos/apoio.",
            oc("Becker") + " (1983) → competição entre grupos de pressão; ineficiência das transferências "
            "como freio.",
        ]), ("😈 Para dificultar", [
            "<i>“Segundo a teoria do interesse público, a regulação atende aos grupos capazes de exercer maior "
            "pressão sobre os reguladores.”</i> → ERRADO (troca de conceito: essa é a teoria dos grupos de "
            "interesse)",
            "<i>“A teoria da captura sustenta que a agência tende a agir em favor do setor regulado.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["se prestaria"], "dificuldade": 2,
        "comentario_fonte": "Três teorias: interesse público, captura e competição entre grupos de interesse "
                            "(regulador quer se perpetuar; regra atende ao grupo de maior pressão). Stigler, "
                            "Peltzman, Becker, Olson; tabelas comparativas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 237-239", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖 (síntese comparativa das teorias)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00266
    {
        "id": "ECO-E3-L00266-1", "fonte_ref": "E3-L00266", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": True,
        "comando": COM_NIDI_59,
        "rotulo_item": "Item",
        "assertiva": ("Para determinar o nível eficiente de oferta de um bem público é necessário igualar a soma dos "
                      "benefícios marginais dos usuários do bem público ao custo marginal de sua produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para determinar o nível eficiente de oferta de um bem público é necessário igualar a "
                      "<u>soma dos benefícios marginais</u> dos usuários do bem público ao custo marginal de sua "
                      "produção."),
        "poucas": ("É a " + azb("condição de Samuelson") + ": " + vd("ΣBMg = CMg") + ". Como todos consomem a "
                   "mesma unidade, o benefício social de produzi-la é a soma do que ela vale para cada um."),
        "destrinchando": [
            "Bem privado: eficiência quando o benefício marginal de <b>cada</b> consumidor iguala o custo "
            "marginal (BMg<sub>i</sub> = CMg). Cada um consome a sua unidade.",
            "Bem público: a unidade adicional serve a todos ao mesmo tempo (não rivalidade). Logo o benefício "
            "social dela é " + vd("BMg₁ + BMg₂ + … + BMgₙ") + ", e o nível eficiente está onde essa soma iguala "
            "o CMg. " + oc("Paul Samuelson") + " formalizou a regra em <i>The Pure Theory of Public "
            "Expenditure</i> (" + vd("1954") + ").",
            "Graficamente: soma " + azb("vertical") + " das curvas individuais de benefício marginal (no bem "
            "privado, a demanda de mercado é soma " + azb("horizontal") + "). No gráfico abaixo, em q* = 2: "
            "3,50 + 2,00 = 5,50 = CMg. Note que, isoladamente, nenhuma pessoa pagaria 5,50 pela unidade.",
            "O mercado não chega lá: como ninguém é excluído, cada um subdeclara a disposição a pagar "
            "(" + azb("carona") + ") e a provisão voluntária fica abaixo de q*, quando existe.",
            "Síntese de " + oc("Pindyck") + ": o princípio é o mesmo dos bens privados (benefício marginal = "
            "custo marginal); o que muda no bem público é <b>como</b> se mede o benefício marginal.",
        ],
        "grafico_verso": "ECO-E3-L00266-1-V1",
        "dissecando": (cz("[literalidade]") + " Item extraído quase palavra por palavra do " + oc("Pindyck")
                       + " (capítulo de externalidades e bens públicos). A armadilha seria trocar “soma dos "
                       "benefícios marginais” por “média” ou por “benefício marginal do usuário que mais "
                       "valoriza o bem”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O nível eficiente de um bem público é aquele em que o benefício marginal de cada usuário "
            "iguala o custo marginal.”</i> → ERRADO (troca de conceito: essa é a regra do bem privado)",
            "<i>“A curva de benefício marginal social de um bem público resulta da soma vertical das curvas "
            "individuais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["é necessário"], "dificuldade": 1,
        "comentario_fonte": "Condição de Samuelson: ΣBMg = CMg; soma vertical por não rivalidade; gráfico de "
                            "Pindyck (p. 683) com duas pessoas e CMg; exemplos numéricos; carona.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 369", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00266-1-V1, valores próprios)"},
                          {"ref": "IMAGEM 370", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖"}],
        "alertas": ["texto_parcial: o enunciado da Questão 59 vem truncado na fonte (“…especi...”)"],
    },
    # ------------------------------------------------------------------ E3-L00267
    {
        "id": "ECO-E3-L00267-1", "fonte_ref": "E3-L00267", "destino": "12", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COM_NIDI_59,
        "rotulo_item": "Item",
        "assertiva": ("Uma forma de reduzir o problema do caronista, ou free-rider, no caso da oferta de bens "
                      "públicos é o estabelecimento de tributos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Uma forma de reduzir</u> o problema do caronista, ou free-rider, no caso da oferta de "
                      "bens públicos é o estabelecimento de tributos."),
        "poucas": ("O carona nasce da " + azb("não exclusão") + ": quem não paga usufrui igual. O " + azb("tributo "
                   "compulsório") + " elimina a opção de não pagar e permite financiar a provisão pública."),
        "destrinchando": [
            azb("Caronista") + " (<i>free-rider</i>): quem se beneficia do bem sem contribuir. Se a contribuição "
            "é voluntária, cada um tem incentivo a esconder quanto valoriza o bem, esperando que os outros "
            "paguem. Resultado: subprovisão ou provisão nula — um dilema do prisioneiro com muitos jogadores.",
            "O Estado contorna o problema pelo poder de " + azb("tributar") + ": a contribuição deixa de ser "
            "escolha. É a justificativa clássica da provisão pública de defesa, iluminação, segurança, pesquisa "
            "básica — a " + azb("função alocativa") + " de " + oc("Musgrave") + ".",
            "Limites (por isso “reduzir”, e não “eliminar”): sonegação (o carona fiscal); o governo continua "
            "sem conhecer a verdadeira soma das disposições a pagar, e pode errar a quantidade; a repartição do "
            "ônus raramente corresponde ao benefício de cada um.",
            "Outras saídas: tornar o bem excludente (pedágio, assinatura, clube); vendê-lo junto com um bem "
            "privado (TV aberta financiada por publicidade); grupos pequenos com pressão social; mecanismos de "
            "revelação de preferências; contribuições condicionadas (<i>matching funds</i>).",
        ],
        "dissecando": (cz("[modulador relativo]") + " “Uma forma de reduzir” é modesto o bastante para ser "
                       "verdadeiro. A versão ERRADA típica troca por “a única forma” ou “elimina "
                       "completamente” o problema."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O estabelecimento de tributos elimina completamente o problema do caronista na oferta de bens "
            "públicos.”</i> → ERRADO (modulador absoluto: há sonegação e falta de revelação de preferências)",
            "<i>“O problema do caronista decorre da não exclusão no consumo dos bens públicos.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["uma forma", "reduzir"], "dificuldade": 1,
        "comentario_fonte": "Tributos tornam o pagamento compulsório e financiam o bem público; problemas: evasão, "
                            "valor e repartição do tributo; outras alternativas (clubes, pedágios, doações).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 371", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖 (limites dos tributos)"}],
        "alertas": ["texto_parcial: o enunciado da Questão 59 vem truncado na fonte (“…especi...”)"],
    },
    # ------------------------------------------------------------------ E3-L00268
    {
        "id": "ECO-E3-L00268-1", "fonte_ref": "E3-L00268", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COM_NIDI_59,
        "rotulo_item": "Item",
        "assertiva": ("Se empresas que produzem externalidade negativa, ao executarem uma atividade produtiva "
                      "poluidora, possuem processos produtivos distintos e diferentes níveis de custo para reduzir "
                      "as emissões poluentes, a imposição de uma taxa sobre a quantidade de poluente emitido pode "
                      "ser preferível ao estabelecimento de um limite permitido de emissão."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se empresas que produzem externalidade negativa, ao executarem uma atividade produtiva "
                      "poluidora, possuem processos produtivos distintos e <u>diferentes níveis de custo para "
                      "reduzir as emissões</u> poluentes, a imposição de uma taxa sobre a quantidade de poluente "
                      "emitido <u>pode ser preferível</u> ao estabelecimento de um limite permitido de emissão."),
        "poucas": ("Taxa = preço único da poluição; cada firma abate até " + vd("CMgA = taxa") + ". Quem abate "
                   "barato abate mais e a meta sai ao " + azb("menor custo total") + " — o limite uniforme não "
                   "faz essa triagem."),
        "destrinchando": [
            "Instrumentos de " + azb("comando e controle") + " (padrão, limite por firma) fixam a quantidade "
            "de cada um; " + azb("instrumentos econômicos") + " (taxa pigouviana, licenças negociáveis) fixam "
            "um preço e deixam cada firma escolher quanto abater.",
            "Com custos de abatimento heterogêneos, a taxa produz a " + azb("equalização dos custos "
            "marginais") + " entre firmas, condição de custo mínimo. No gráfico: meta de 16; com taxa 6, a "
            "firma barata abate 12 e a cara abate 4 (custo " + vd("48") + "); limite de 8 para cada custa "
            + vd("64") + ".",
            "Quem abate menos não “escapa”: paga a taxa sobre tudo o que continua emitindo. A firma de "
            "abatimento barato, ao contrário, abate muito e paga <b>menos</b> taxa.",
            "Vantagem dinâmica: cada tonelada evitada poupa a taxa, então há incentivo permanente a inovar; "
            "sob o limite, depois de cumpri-lo, o incentivo some.",
            "O “pode ser” protege o item: com incerteza sobre os custos e dano que dispara acima de um limiar, "
            "o controle por quantidade pode ser preferível (" + oc("Weitzman") + ", 1974).",
        ],
        "grafico_verso": "ECO-E3-L00070-1-V1",
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " Versão ampliada de um item clássico "
                       "(“taxas podem ser preferíveis a limites com custos diferentes”). As expressões "
                       "“diferentes níveis de custo” e “pode ser” são as chaves do CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com uma taxa sobre emissões, as firmas de menor custo de abatimento reduzem menos a poluição e "
            "pagam mais taxa.”</i> → ERRADO (inversão: reduzem mais e pagam menos)",
            "<i>“Um sistema de licenças de emissão negociáveis também tende a igualar os custos marginais de "
            "abatimento entre as firmas.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["pode ser"], "dificuldade": 2,
        "comentario_fonte": "Taxa pigouviana permite que quem abate barato reduza mais e quem abate caro pague a "
                            "taxa; meta ao menor custo; incentivo contínuo à inovação.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 372", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖"}],
        "alertas": ["quase_duplicata: ECO-E3-L00070-1 (Nidi, Simulado Julho/2025) traz a mesma assertiva em "
                    "redação mais curta; os dois cards foram mantidos e usam o mesmo gráfico",
                    "qualidade_fonte: um dos comentários de origem diz que as firmas de baixo custo de "
                    "abatimento “pagam mais imposto” e que o caso “ilustra o teorema de Coase”; ambos corrigidos",
                    "texto_parcial: o enunciado da Questão 59 vem truncado na fonte (“…especi...”)"],
    },
    # ------------------------------------------------------------------ E3-L00269
    {
        "id": "ECO-E3-L00269-1", "fonte_ref": "E3-L00269", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": COM_NIDI_59,
        "rotulo_item": "Item",
        "assertiva": ("Mesmo que não haja intervenção governamental para a reciclagem do lixo, alguma reciclagem "
                      "poderá ocorrer se os preços dos materiais novos forem muito elevados em relação ao material "
                      "reciclado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Mesmo que não haja intervenção governamental para a reciclagem do lixo, <u>alguma</u> "
                      "reciclagem <u>poderá</u> ocorrer se os preços dos materiais novos forem muito elevados em "
                      "relação ao material reciclado."),
        "poucas": ("Material reciclado e virgem são " + azb("insumos substitutos") + ": se o virgem encarece, "
                   "reciclar passa a dar lucro e o mercado recicla sozinho — embora, em geral, menos que o "
                   "socialmente ótimo."),
        "destrinchando": [
            "A firma escolhe o insumo mais barato por unidade de produto. Quando o preço da matéria-prima "
            "virgem sobe em relação ao custo de coletar, separar e processar a sucata, a demanda pelo reciclado "
            "cresce — " + azb("substituição de insumos") + " movida por preços relativos.",
            "Exemplos: latas de alumínio e sucata de cobre (o alumínio reciclado poupa grande parte da energia "
            "da produção primária); papelão e embalagens. No " + rx("Brasil") + ", o índice de reciclagem de "
            "latas de alumínio está entre os mais altos do mundo, sustentado sobretudo pelo valor da sucata e "
            "pelo trabalho de catadores e cooperativas.",
            "Por que ainda há espaço para política: a reciclagem gera " + azb("externalidade positiva") + " "
            "(menos aterro, menos extração, menos emissões) que o preço não remunera, e o descarte em lixão "
            "tem custo social que o consumidor não paga. O mercado recicla, mas " + azb("menos que o ótimo")
            + ".",
            "Instrumentos para aproximar do ótimo: depósito-retorno, taxa sobre o lixo não separado, "
            "logística reversa (no Brasil, a Política Nacional de Resíduos Sólidos, " + vd("Lei 12.305/2010")
            + "), subsídio à coleta seletiva.",
        ],
        "dissecando": (cz("[modulador relativo]") + " “Alguma” e “poderá” fazem do item uma afirmação de "
                       "possibilidade, e o mecanismo (preço relativo) é sólido. A versão ERRADA diria que, sem "
                       "intervenção, a reciclagem atinge o nível socialmente ótimo ou que nunca ocorre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sem intervenção governamental, o mercado leva a reciclagem ao nível socialmente ótimo.”</i> → "
            "ERRADO (ignora a externalidade positiva da reciclagem)",
            "<i>“Uma queda acentuada do preço da matéria-prima virgem tende a reduzir a reciclagem "
            "espontânea.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["alguma", "poderá"], "dificuldade": 1,
        "comentario_fonte": "Substituição de insumos por preços relativos: material virgem caro torna o reciclado "
                            "competitivo; exemplos de alumínio, cobre, embalagens; intervenção pode ampliar.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 373", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖 (exemplos)"}],
        "alertas": ["texto_parcial: o enunciado da Questão 59 vem truncado na fonte (“…especi...”)"],
    },
    # ---- fim
]
