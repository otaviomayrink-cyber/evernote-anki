"""Cards do lote de redação 22 — ECO, passada 02 (nota 47: setor público, funções do Estado e política fiscal)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "est": "🏛️ Funções do Estado",
    "trib": "💸 Tributação: princípios e incidência",
    "fisc": "📊 Política fiscal e multiplicadores",
}

BNI = "Banca não identificada"

CMD_TRIB = "Julgue o item a seguir, relativo aos princípios e às espécies de tributação."

CMD_IDEAL = ("Acerca dos princípios que a teoria da tributação estabelece para um sistema tributário ideal, julgue o "
             "item a seguir.")

CMD_II = "Acerca das funções fiscal e extrafiscal dos tributos, julgue o item a seguir."

CMD_CONTR = "Acerca dos instrumentos e dos efeitos da política fiscal contracionista, julgue o item a seguir."

CMD_EXP = "Considerando os instrumentos de política econômica de que dispõe o governo, julgue o item a seguir."

CMD_ESTAB = "Julgue o item a seguir, relativo à política fiscal e à estabilização macroeconômica."

CMD_FUN = ("Acerca das funções econômicas do governo — alocativa, distributiva e estabilizadora —, julgue o item a "
           "seguir.")

CMD_ESTADO = "Julgue o item a seguir, relativo à atuação do Estado na economia."

FIG_PERDIDA = lambda ref: {"ref": ref, "tipo_fonte": "GRÁFICO/TEXTO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}

CARDS = [
    # ------------------------------------------------------------------ E1-0591
    {
        "id": "ECO-E1-0591-1", "fonte_ref": "E1-0591", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Um imposto é neutro quando a participação dos impostos na renda dos agentes aumenta conforme a "
                      "renda aumenta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um imposto é ") + vm("neutro") + az(" quando a participação dos impostos na renda dos "
                                                           "agentes aumenta conforme a renda aumenta.")),
        "poucas": ("O item descreve o imposto " + azb("progressivo") + " (alíquota média cresce com a renda). "
                   + azb("Neutro") + " é o imposto que não altera as decisões econômicas dos agentes."),
        "destrinchando": [
            "Classificação pela relação entre imposto pago e renda (alíquota média T/Y): " + azb("progressivo")
            + " — T/Y sobe quando Y sobe; " + azb("proporcional") + " — T/Y constante; " + azb("regressivo")
            + " — T/Y cai quando Y sobe. É o critério da <b>equidade vertical</b>.",
            azb("Neutralidade") + " é outro eixo, o da <b>eficiência</b>: o tributo é neutro quando não muda os "
            "preços relativos que guiam as escolhas (consumir × poupar, trabalhar × lazer, um bem × outro). O imposto "
            "que mais se aproxima disso é o " + azb("lump-sum") + " (montante fixo por pessoa), que não depende de "
            "nenhuma decisão do contribuinte e, por isso, não gera peso morto.",
            "Os dois eixos costumam brigar: o tributo neutro por excelência (lump-sum) é regressivo, porque cobra o "
            "mesmo valor do pobre e do rico; a progressividade, por sua vez, mexe no incentivo marginal a trabalhar "
            "e poupar.",
            "Exemplo de distorção: um imposto em cascata incentiva a verticalização artificial das empresas só para "
            "fugir das etapas tributadas — o contrário da neutralidade.",
            vm("Regra-âncora: progressivo/regressivo/proporcional = distribuição; neutro = não distorce escolhas."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item cola a definição de progressividade no rótulo "
                       "“neutro”. A pista está no próprio texto: “participação dos impostos na renda” que “aumenta "
                       "conforme a renda aumenta” é a fórmula literal da alíquota média crescente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um imposto é progressivo quando a participação dos impostos na renda dos agentes aumenta conforme a "
            "renda aumenta.”</i> → CERTO",
            "<i>“Um imposto é neutro quando sua alíquota é igual para todos os níveis de renda.”</i> → ERRADO (troca "
            "de conceito: isso é imposto proporcional)",
        ])],
        "reescrita": ("Um imposto é " + hl("progressivo") + " quando a participação dos impostos na renda dos agentes "
                      "aumenta conforme a renda aumenta."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Nesse caso, o imposto seria progressivo. Um imposto neutro não altera as "
                            "decisões econômicas dos agentes.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [FIG_PERDIDA("Untitled (100).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0592
    {
        "id": "ECO-E1-0592-1", "fonte_ref": "E1-0592", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Um imposto pode ser do tipo valor adicionado, quando é devido apenas sobre o valor agregado ou "
                      "acrescido."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um imposto pode ser do tipo valor adicionado, quando é devido <u>apenas sobre o valor agregado "
                      "ou acrescido</u>."),
        "poucas": ("É a definição do " + azb("imposto sobre valor adicionado") + " (IVA): cada etapa paga só sobre o "
                   "que acrescentou ao produto, porque abate o imposto já pago nas etapas anteriores."),
        "destrinchando": [
            "Mecânica: a empresa calcula o imposto sobre o valor da venda e desconta, como " + azb("crédito")
            + ", o imposto embutido nas compras. Exemplo: o fabricante compra insumo de 100 e vende por 160; com "
            "alíquota de 10%, deve 16 − 10 = " + vd("6") + ", exatamente 10% do valor que adicionou (60).",
            "Por isso o IVA é " + azb("não cumulativo") + ": a carga final não depende do número de etapas da cadeia. "
            "O oposto é o imposto " + azb("cumulativo") + " ou “em cascata” (imposto sobre faturamento bruto), que "
            "incide de novo a cada etapa, tributa imposto sobre imposto e incentiva a verticalização artificial.",
            "Variantes de cálculo: método de " + azb("crédito sobre crédito") + " (imposto sobre a venda menos "
            "imposto das compras — o usado no Brasil) e método de base sobre base (alíquota sobre a diferença "
            "vendas − compras).",
            rx("Brasil") + ": ICMS e IPI sempre foram não cumulativos por mandamento constitucional, e PIS/Cofins "
            "conviviam com regimes cumulativo e não cumulativo. A reforma da " + vd("EC 132/2023") + " cria um "
            + azb("IVA dual") + " — " + vd("CBS") + " (União) e " + vd("IBS") + " (estados e municípios) — que "
            "substitui PIS, Cofins, IPI, ICMS e ISS na transição de " + vd("2026 a 2033") + " ⏳ (out/2026).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definição de manual. O “apenas” parece "
                       "restrição indevida, mas é justamente o que define o IVA: a base é só o valor acrescido, não o "
                       "valor total da operação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O imposto sobre valor adicionado é cumulativo, pois incide em todas as etapas da cadeia "
            "produtiva.”</i> → ERRADO (troca de conceito: incide em todas as etapas, mas sem cumulatividade)",
            "<i>“No imposto em cascata, a carga final independe do número de etapas de produção.”</i> → ERRADO "
            "(inversão: essa é a vantagem do IVA)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["pode", "apenas"], "dificuldade": 1,
        "comentario_fonte": "CERTO. O imposto não cumulativo incide apenas sobre o valor agregado entre uma operação "
                            "e outra, gerando crédito para a empresa; ICMS e IPI são exemplos de impostos sobre valor "
                            "adicionado.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_PERDIDA("Untitled (111).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0593
    {
        "id": "ECO-E1-0593-1", "fonte_ref": "E1-0593", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": "Ao escolher o tipo de impostos, existe um trade-off (conflito) entre eficiência e justiça.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ao escolher o tipo de impostos, existe um <u>trade-off</u> (conflito) entre eficiência e "
                      "justiça."),
        "poucas": ("O dilema clássico da tributação: o imposto que menos distorce (" + azb("eficiência") + ") "
                   "costuma ser o menos justo, e o mais justo (" + azb("equidade") + ") costuma distorcer mais."),
        "destrinchando": [
            azb("Eficiência") + " = arrecadar com o menor " + azb("peso morto") + " possível, isto é, alterando o "
            "mínimo as decisões de consumir, trabalhar, poupar e investir. " + azb("Justiça") + " (equidade) = "
            "repartir o ônus conforme algum critério aceito — capacidade de pagamento ou benefício recebido.",
            "Os extremos mostram o conflito: o " + azb("imposto lump-sum") + " (valor fixo por cabeça) é o mais "
            "eficiente, pois não depende de nenhuma escolha, mas é brutalmente regressivo. Um imposto de renda muito "
            "progressivo é mais justo, mas eleva a alíquota <b>marginal</b> sobre quem ganha mais e reduz o incentivo "
            "a trabalhar e poupar na margem.",
            "Regra de " + oc("Ramsey") + " (eficiência pura): tributar mais os bens de demanda " + azb("inelástica")
            + ", que distorcem menos — mas esses costumam ser bens de primeira necessidade, pesados no orçamento dos "
            "pobres. Eficiência e justiça apontam para lados opostos.",
            "O desenho tributário real é uma escolha política sobre <b>quanto</b> de eficiência se troca por quanto "
            "de equidade; não existe imposto que maximize as duas ao mesmo tempo.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de conceito que reproduz o manual. Pode assustar quem acha que "
                       "um bom imposto deve ser, ao mesmo tempo, eficiente e justo — o ideal existe, mas os dois "
                       "critérios entram em conflito na escolha concreta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O imposto lump-sum é, simultaneamente, o mais eficiente e o mais equitativo.”</i> → ERRADO "
            "(meia-verdade: é eficiente, mas regressivo)",
            "<i>“Pela regra de Ramsey, a eficiência recomenda alíquotas maiores sobre bens de demanda mais "
            "inelástica.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. O dilema clássico está entre eficiência alocativa (não distorcer decisões) e "
                            "justiça distributiva (reduzir desigualdade); impostos mais justos tendem a gerar "
                            "distorções.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0594
    {
        "id": "ECO-E1-0594-1", "fonte_ref": "E1-0594", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("A estrutura tributária de um país tenderá a ter a desigualdade ampliada se significante parcela "
                      "da arrecadação depender de impostos indiretos e houver ausência de políticas de redistribuição "
                      "de renda e de riqueza."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A estrutura tributária de um país <u>tenderá</u> a ter a desigualdade ampliada se significante "
                      "parcela da arrecadação depender de <u>impostos indiretos</u> e houver ausência de políticas de "
                      "redistribuição de renda e de riqueza."),
        "poucas": ("Impostos " + azb("indiretos") + " (sobre consumo) são " + azb("regressivos") + ": pesam mais, em "
                   "proporção da renda, sobre os pobres. Sem gasto redistributivo que compense, a desigualdade cresce."),
        "destrinchando": [
            "Por que o indireto é regressivo: famílias pobres consomem quase toda a renda; famílias ricas poupam "
            "parte dela. Uma alíquota igual sobre o consumo vira, portanto, uma fatia <b>maior da renda</b> de quem "
            "ganha menos. Exemplo: quem gasta 100% de R$ 2 mil com 20% de imposto embutido paga 20% da renda; quem "
            "gasta 50% de R$ 20 mil paga 10%.",
            "O indireto ainda é " + azb("pouco visível") + " (vem embutido no preço) e não distingue a capacidade "
            "contributiva de quem compra — o pão custa o mesmo imposto ao rico e ao pobre.",
            "O efeito final sobre a desigualdade depende do " + azb("lado do gasto") + ": transferências focalizadas, "
            "saúde e educação públicas podem compensar uma tributação regressiva. Daí a dupla condição do item: "
            "muito indireto <b>e</b> ausência de redistribuição.",
            rx("Brasil") + ": caso clássico de carga concentrada em consumo (cerca de 40% da arrecadação ⏳ "
            "(out/2026)) e pouco peso de renda e patrimônio; atenuantes recentes são o " + azb("cashback")
            + " do IBS/CBS (EC 132/2023) e a ampliação da isenção do IRPF com tributação mínima das altas rendas "
            "(reforma do IR aprovada em 2025) ⏳ (out/2026).",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O item é protegido por “tenderá” e pela "
                       "condição dupla (muito imposto indireto + falta de redistribuição). Para errar, a banca teria "
                       "de dizer que o indireto, por si só, sempre amplia a desigualdade, qualquer que seja o gasto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Impostos indiretos são progressivos, pois quem consome mais paga mais imposto em valor "
            "absoluto.”</i> → ERRADO (troca de conceito: progressividade se mede pela fração da renda, não pelo "
            "valor absoluto)",
        ]), ("🃏 Carta na manga", [
            "A regressividade da matriz tributária brasileira — muito consumo, pouca renda e patrimônio — é argumento "
            "recorrente para explicar por que o Estado arrecada muito e redistribui pouco via tributo; a "
            "redistribuição vem sobretudo do gasto social.",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["tenderá", "se"], "dificuldade": 1,
        "comentario_fonte": "CERTO. Impostos indiretos são regressivos e podem aumentar a desigualdade, especialmente "
                            "quando faltam mecanismos redistributivos, como gastos sociais ou transferências.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0595
    {
        "id": "ECO-E1-0595-1", "fonte_ref": "E1-0595", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_TRIB,
        "rotulo_item": "Item",
        "assertiva": ("Os impostos diretos sobre a renda podem melhorar a distribuição de renda de uma sociedade, caso "
                      "haja um número de faixas de renda suficientemente diferenciadas com elevações progressivas de "
                      "alíquotas de impostos e que seja adequado à estrutura social do país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os impostos diretos sobre a renda <u>podem</u> melhorar a distribuição de renda de uma "
                      "sociedade, caso haja um número de faixas de renda suficientemente diferenciadas com "
                      "<u>elevações progressivas de alíquotas</u> de impostos e que seja adequado à estrutura social "
                      "do país."),
        "poucas": ("Imposto de renda com " + azb("alíquotas crescentes por faixa") + " faz a alíquota média subir com "
                   "a renda — é " + azb("progressivo") + " e, por isso, comprime a desigualdade da renda disponível."),
        "destrinchando": [
            "O imposto " + azb("direto") + " incide sobre quem tem a capacidade contributiva (renda, patrimônio) e "
            "permite personalizar a cobrança: faixas, deduções, isenção na base. É o instrumento por excelência da "
            + azb("equidade vertical") + " (quem ganha mais paga proporcionalmente mais).",
            "Faixas com alíquotas " + azb("marginais") + " crescentes fazem a alíquota " + azb("média")
            + " subir com a renda: quem passa para a faixa de 27,5% paga essa alíquota só sobre o que excede o "
            "limite, nunca sobre toda a renda. É essa curva de alíquota média crescente que reduz o índice de Gini "
            "da renda após impostos.",
            "As condições do item importam: poucas faixas, teto baixo de alíquota ou muitas isenções para rendas do "
            "capital esvaziam a progressividade. Daí a ressalva de que a tabela seja “adequada à estrutura social”.",
            rx("Brasil") + ": IRPF com alíquotas de 0 a " + vd("27,5%") + "; desde " + vd("2026") + ", isenção até "
            + vd("R$ 5 mil") + " mensais e tributação mínima das rendas muito altas (reforma do IR aprovada em 2025) ⏳ (out/2026). "
            "A crítica clássica é a isenção de lucros e dividendos, que torna o topo da pirâmide menos tributado.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “podem” e o “caso haja” salvam o item: não se afirma que o "
                       "imposto de renda sempre redistribui, só que redistribui se for desenhado com progressividade "
                       "real. Item condicional e modalizado da banca costuma ser CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os impostos diretos sobre a renda sempre melhoram a distribuição de renda, independentemente da "
            "estrutura de alíquotas.”</i> → ERRADO (modulador absoluto)",
            "<i>“Com alíquotas marginais crescentes, a alíquota média do contribuinte é igual à alíquota da sua "
            "faixa mais alta.”</i> → ERRADO (troca de conceito: a média fica abaixo da marginal)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["podem", "caso haja"], "dificuldade": 1,
        "comentario_fonte": "CERTO. Progressividade no imposto de renda com múltiplas faixas pode promover justiça "
                            "distributiva, tornando o sistema mais equitativo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “estrutural social” → “estrutura social” (erro evidente de digitação)"],
    },
]
