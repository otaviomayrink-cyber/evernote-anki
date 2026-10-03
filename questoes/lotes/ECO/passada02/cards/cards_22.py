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
    # ------------------------------------------------------------------ E1-0596
    {
        "id": "ECO-E1-0596-1", "fonte_ref": "E1-0596", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_IDEAL,
        "rotulo_item": "Item",
        "assertiva": ("A Teoria da Tributação estabelece que o sistema tributário ideal distribui o ônus tributário "
                      "equitativamente entre os diversos indivíduos da sociedade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Teoria da Tributação estabelece que o sistema tributário ideal distribui o ônus tributário "
                      "<u>equitativamente</u> entre os diversos indivíduos da sociedade."),
        "poucas": ("A " + azb("equidade") + " é o primeiro dos princípios do sistema tributário ideal: o ônus deve "
                   "ser repartido de forma justa entre os indivíduos."),
        "destrinchando": [
            "Na lista clássica dos manuais de finanças públicas (" + oc("Giambiagi e Além") + ", <i>Finanças "
            "Públicas</i>), o sistema tributário ideal atende a quatro princípios: " + azb("equidade") + ", "
            + azb("progressividade") + ", " + azb("neutralidade") + " e " + azb("simplicidade") + ".",
            "Equidade tem duas dimensões: " + azb("horizontal") + " — quem está na mesma situação paga o mesmo; "
            + azb("vertical") + " — quem tem mais capacidade paga mais. A vertical é a ponte para a progressividade.",
            "Dois critérios para medir o que é “justo”: " + azb("princípio do benefício") + " (cada um paga conforme "
            "o que recebe do Estado — funciona para taxas e pedágios, não para bens públicos puros) e "
            + azb("princípio da capacidade de pagamento") + " (cada um paga conforme renda, consumo ou patrimônio — "
            "a base dos impostos gerais). " + rx("Brasil") + ": a CF/1988 consagra a capacidade contributiva no "
            + vd("art. 145, § 1º") + ".",
            "Antecedente histórico: a primeira das quatro máximas de " + oc("Adam Smith") + " (<i>A Riqueza das "
            "Nações</i>, livro V) é justamente a igualdade — os súditos devem contribuir na proporção de suas "
            "capacidades; as outras são certeza, conveniência e economia na cobrança.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz o primeiro princípio do manual. O advérbio "
                       "“equitativamente” não significa “igualmente”: a banca às vezes troca um pelo outro para "
                       "derrubar o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o sistema tributário ideal distribui o ônus tributário igualmente entre os diversos indivíduos da "
            "sociedade.”</i> → ERRADO (troca de conceito: igual ≠ equitativo)",
            "<i>“Pelo princípio do benefício, cada contribuinte paga conforme sua renda.”</i> → ERRADO (troca de "
            "conceito: isso é capacidade de pagamento)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. A equidade é um princípio central da teoria da tributação, garantindo que o ônus "
                            "seja justo conforme a capacidade contributiva.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [FIG_PERDIDA("Untitled (102).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0597
    {
        "id": "ECO-E1-0597-1", "fonte_ref": "E1-0597", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_IDEAL,
        "rotulo_item": "Item",
        "assertiva": ("A Teoria da Tributação estabelece que o sistema tributário ideal adota o conceito de "
                      "progressividade, segundo o qual deve-se tributar menos quem tem uma renda mais elevada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Teoria da Tributação estabelece que o sistema tributário ideal adota o conceito de "
                       "progressividade, segundo o qual deve-se tributar ") + vm("menos") + az(" quem tem uma renda "
                                                                                              "mais elevada.")),
        "poucas": ("Progressividade é o contrário: tributar " + azb("mais") + " — proporcionalmente à renda — quem "
                   "ganha mais. Tributar menos os ricos descreve um sistema " + azb("regressivo") + "."),
        "destrinchando": [
            azb("Progressividade") + ": a alíquota média (imposto ÷ renda) cresce com a renda. Não basta o rico "
            "pagar mais em reais — no imposto proporcional ele já paga; é preciso pagar uma <b>fração maior</b> da "
            "renda.",
            "Fundamento: a " + azb("equidade vertical") + " e a ideia de " + azb("utilidade marginal decrescente")
            + " da renda — R$ 100 tirados de quem ganha R$ 1 mil pesam muito mais do que de quem ganha R$ 100 mil. "
            "Igualar o “sacrifício” exige alíquotas maiores no topo.",
            "Instrumentos típicos: imposto de renda com faixas e alíquotas marginais crescentes, impostos sobre "
            "patrimônio e herança, isenção na base. " + rx("Brasil") + ": a CF/1988 manda que o IR seja informado "
            "pela progressividade (" + vd("art. 153, § 2º, I") + ").",
            "Na lista de princípios do sistema ideal (equidade, progressividade, neutralidade, simplicidade), a "
            "progressividade é o desdobramento operacional da equidade.",
            vm("Regra-âncora: progressivo = quem ganha mais paga proporcionalmente mais; regressivo = o contrário."),
        ],
        "dissecando": (cz("[inversão]") + " A definição está certa até “tributar”; a banca inverteu só o "
                       "advérbio (“mais” → “menos”), que transforma progressividade em regressividade. Item curto de "
                       "definição: leia a última palavra decisiva com calma."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…progressividade, segundo o qual quem tem renda mais elevada deve pagar mais imposto em valor "
            "absoluto.”</i> → ERRADO (insuficiente: o imposto proporcional também cumpre isso)",
            "<i>“…progressividade, segundo o qual a alíquota média do imposto cresce com a renda.”</i> → CERTO",
        ])],
        "reescrita": ("A Teoria da Tributação estabelece que o sistema tributário ideal adota o conceito de "
                      "progressividade, segundo o qual deve-se tributar " + hl("mais") + " quem tem uma renda mais "
                      "elevada."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. A progressividade implica tributar mais quem possui maior renda, respeitando a "
                            "capacidade de pagamento.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0598
    {
        "id": "ECO-E1-0598-1", "fonte_ref": "E1-0598", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_IDEAL,
        "rotulo_item": "Item",
        "assertiva": ("A Teoria da Tributação estabelece que o sistema tributário ideal segue o princípio da justiça "
                      "empresarial, isto é, os impostos devem ser formulados com vistas a melhorar o poder econômico "
                      "das empresas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Teoria da Tributação estabelece que o sistema tributário ideal segue o princípio ")
                    + vm("da justiça empresarial") + az(", isto é, os impostos devem ser formulados com vistas a ")
                    + vm("melhorar o poder econômico das empresas") + az(".")),
        "poucas": ("Não existe “princípio da justiça empresarial”. Os princípios do sistema tributário ideal são "
                   + azb("equidade") + ", " + azb("progressividade") + ", " + azb("neutralidade") + " e "
                   + azb("simplicidade") + " — nenhum deles visa fortalecer empresas."),
        "destrinchando": [
            "A justiça que a teoria da tributação persegue é a " + azb("justiça entre indivíduos") + ": repartir o "
            "ônus conforme a capacidade de pagamento (equidade horizontal e vertical). Empresa não “sofre” o tributo "
            "em última instância: a carga recai sempre sobre pessoas — consumidores, trabalhadores ou acionistas.",
            "O princípio que mais se aproxima do mundo empresarial é a " + azb("neutralidade") + ": o tributo não "
            "deve distorcer decisões de produção, localização, organização da cadeia ou financiamento. Neutralidade "
            "não é <b>favorecer</b> empresas; é não interferir nas escolhas delas.",
            "Benefícios fiscais a setores (isenções, regimes especiais) existem, mas são instrumentos "
            + azb("extrafiscais") + " de política industrial ou regional — exceções justificadas caso a caso, não "
            "princípio do sistema ideal. Pela ótica da neutralidade, aliás, são distorções.",
            "Lista para revisar: " + vd("equidade") + " (justiça entre indivíduos) · " + vd("progressividade")
            + " (mais de quem ganha mais) · " + vd("neutralidade") + " (não distorcer) · " + vd("simplicidade")
            + " (fácil de entender e de arrecadar).",
        ],
        "dissecando": (cz("[outro: princípio inventado · troca de conceito]") + " A banca fabricou um princípio "
                       "com rótulo plausível (“justiça”) e o definiu com o objetivo oposto ao da teoria: proteger "
                       "agentes econômicos em vez de repartir o ônus com justiça. Princípio que você nunca viu na "
                       "lista é sinal de ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…segue o princípio da neutralidade, isto é, os impostos não devem alterar as decisões econômicas "
            "dos agentes.”</i> → CERTO",
            "<i>“…segue o princípio da neutralidade, isto é, os impostos devem favorecer os setores mais "
            "produtivos.”</i> → ERRADO (contradição: favorecer setores é distorcer)",
        ])],
        "reescrita": ("A Teoria da Tributação estabelece que o sistema tributário ideal segue o princípio "
                      + hl("da equidade") + ", isto é, os impostos devem ser formulados com vistas a "
                      + hl("distribuir o ônus tributário de forma justa entre os indivíduos") + "."),
        "tipo_erro": ["OUTRO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Não existe “justiça empresarial” como princípio tributário. A teoria busca "
                            "justiça social e eficiência, e não proteger lucros empresariais.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: ponto final acrescentado ao fim da assertiva"],
    },
    # ------------------------------------------------------------------ E1-0599
    {
        "id": "ECO-E1-0599-1", "fonte_ref": "E1-0599", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_IDEAL,
        "rotulo_item": "Item",
        "assertiva": ("A Teoria da Tributação estabelece que o sistema tributário ideal atende ao critério da "
                      "simplicidade, ou seja, o sistema tributário deve ser de fácil compreensão para os contribuintes "
                      "e de fácil arrecadação por parte do governo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Teoria da Tributação estabelece que o sistema tributário ideal atende ao critério da "
                      "<u>simplicidade</u>, ou seja, o sistema tributário deve ser de fácil compreensão para os "
                      "contribuintes e de fácil arrecadação por parte do governo."),
        "poucas": ("A " + azb("simplicidade") + " é um dos quatro princípios do sistema ideal: regras fáceis de "
                   "entender reduzem o custo de cumprir (contribuinte) e o de cobrar e fiscalizar (governo)."),
        "destrinchando": [
            "Simplicidade tem duas faces, ambas no item: " + azb("custo de conformidade") + " (tempo e dinheiro que "
            "o contribuinte gasta para apurar e pagar — contadores, sistemas, litígios) e " + azb("custo "
            "administrativo") + " (o que o fisco gasta para arrecadar e fiscalizar). Os dois são desperdício do "
            "ponto de vista social.",
            "Sistemas complexos ainda geram " + azb("insegurança jurídica") + ", contencioso e espaço para "
            "planejamento tributário agressivo e sonegação — e tendem a ser menos equitativos, porque quem tem "
            "assessoria paga menos.",
            "O critério conversa com as máximas de " + oc("Adam Smith") + ": <b>certeza</b> (o contribuinte sabe "
            "quanto, quando e como pagar), <b>conveniência</b> e <b>economia</b> na cobrança.",
            rx("Brasil") + ": a complexidade da tributação do consumo (27 legislações de ICMS, milhares de regras de "
            "ISS, PIS/Cofins com regimes distintos) foi o principal motor da reforma da " + vd("EC 132/2023")
            + ", que unifica tudo num IVA dual com regras nacionais ⏳ (out/2026).",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual com as duas pontas (contribuinte e governo). "
                       "Itens irmãos sobre o “sistema tributário ideal” se resolvem lembrando a lista fechada: "
                       "equidade, progressividade, neutralidade, simplicidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…critério da simplicidade, ou seja, o sistema deve ter uma única alíquota para todos os "
            "tributos.”</i> → ERRADO (extrapolação: simples não é alíquota única)",
            "<i>“…critério da simplicidade, que se refere apenas aos custos de arrecadação do governo.”</i> → ERRADO "
            "(restrição indevida: inclui o custo do contribuinte)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. A simplicidade é uma diretriz importante para reduzir custos de conformidade e "
                            "facilitar a fiscalização.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0600
    {
        "id": "ECO-E1-0600-1", "fonte_ref": "E1-0600", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_II,
        "rotulo_item": "Item",
        "assertiva": ("A extrafiscalidade característica do Imposto de Importação é destacada por ser exclusivamente "
                      "arrecadatório."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A extrafiscalidade característica do Imposto de Importação é destacada por ")
                    + vm("ser exclusivamente arrecadatório") + az(".")),
        "poucas": ("Contradição em termos: " + azb("extrafiscal") + " é o tributo usado para <b>regular</b> a "
                   "economia, não só para arrecadar. Função exclusivamente arrecadatória é a " + azb("fiscal") + "."),
        "destrinchando": [
            "Todo tributo arrecada; a distinção é de finalidade predominante. " + azb("Fiscal") + ": o objetivo "
            "principal é levar recursos aos cofres públicos (IR, ICMS). " + azb("Extrafiscal") + ": o objetivo "
            "principal é induzir comportamentos — proteger setores, desestimular consumos, regular mercados. "
            + azb("Parafiscal") + ": arrecadação destinada a entidades que exercem atividade de interesse público "
            "(contribuições do Sistema S, por exemplo).",
            "O " + azb("Imposto de Importação") + " é o exemplo-padrão de extrafiscalidade: ao encarecer o produto "
            "estrangeiro, protege a indústria nacional, corrige desequilíbrios externos e serve de instrumento de "
            "negociação comercial. Sua receita é secundária no orçamento.",
            "Por isso a Constituição lhe dá flexibilidade: o Executivo pode alterar as alíquotas por ato próprio "
            "(" + vd("art. 153, § 1º") + ") e o imposto escapa das anterioridades anual e nonagesimal ("
            + vd("art. 150, § 1º") + "). Mesmo regime vale para IE, IPI e IOF — todos com forte papel regulatório.",
            rx("Brasil") + ": as alíquotas seguem a Tarifa Externa Comum do " + azb("Mercosul") + ", com listas "
            "de exceção decididas pelo Gecex/Camex.",
        ],
        "dissecando": (cz("[contradição · modulador absoluto]") + " O sujeito (“a extrafiscalidade”) e o "
                       "predicado (“exclusivamente arrecadatório”) se anulam. O “exclusivamente” é o gatilho: nem o "
                       "imposto fiscal mais puro é só arrecadação, e o extrafiscal, por definição, não é."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A extrafiscalidade do Imposto de Importação explica por que suas alíquotas podem ser alteradas pelo "
            "Poder Executivo.”</i> → CERTO",
            "<i>“O Imposto de Importação submete-se à anterioridade nonagesimal.”</i> → ERRADO (é exceção às duas "
            "anterioridades)",
        ])],
        "reescrita": ("A extrafiscalidade característica do Imposto de Importação é destacada por "
                      + hl("atuar como instrumento de regulação do comércio exterior, e não por ser apenas "
                           "arrecadatório") + "."),
        "tipo_erro": ["CONTRADICAO", "GENERALIZACAO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Imposto exclusivamente arrecadatório é típico de impostos fiscais; o Imposto de "
                            "Importação possui caráter extrafiscal, pois visa regular o comércio exterior.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0601
    {
        "id": "ECO-E1-0601-1", "fonte_ref": "E1-0601", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_II,
        "rotulo_item": "Item",
        "assertiva": ("A extrafiscalidade característica do Imposto de Importação é destacada por atuar como "
                      "instrumento de intervenção estatal no comércio exterior."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A extrafiscalidade característica do Imposto de Importação é destacada por atuar como "
                      "<u>instrumento de intervenção estatal</u> no comércio exterior."),
        "poucas": ("É a definição de " + azb("extrafiscalidade") + ": o Imposto de Importação é usado mais para "
                   "regular o comércio exterior (proteger, liberalizar, negociar) do que para arrecadar."),
        "destrinchando": [
            "Extrafiscal é o tributo cuja finalidade predominante é " + azb("intervir") + " na economia — induzir "
            "ou desestimular condutas — e não financiar o Estado. O Imposto de Importação é o caso de livro.",
            "Como intervém: a tarifa eleva o preço interno do importado, aumenta a produção doméstica, reduz o "
            "consumo e as importações. No modelo de economia pequena, gera receita para o governo e ganho aos "
            "produtores, mas impõe " + azb("peso morto") + " (perdas de produção e de consumo) — é um instrumento "
            "de política, com custo.",
            "Usos típicos: proteção à indústria nascente, defesa contra surtos de importação, combate à inflação "
            "(redução tarifária temporária de alimentos), retaliação e moeda de troca em negociações comerciais.",
            "A Constituição reconhece o papel regulatório: alíquotas alteráveis pelo Executivo (" + vd("art. 153, "
            "§ 1º") + ") e exceção às anterioridades (" + vd("art. 150, § 1º") + "), para que a política comercial "
            "reaja rápido. " + rx("Brasil") + ": as decisões tarifárias cabem ao Gecex/Camex, dentro da TEC do "
            "Mercosul.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição direta. A banca costuma montar o par: “instrumento de "
                       "intervenção” (CERTO) × “exclusivamente arrecadatório” (ERRADO) — basta saber que extrafiscal "
                       "significa regular, não arrecadar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A extrafiscalidade do Imposto de Importação é destacada por ser exclusivamente arrecadatório.”</i> "
            "→ ERRADO (contradição: isso é função fiscal)",
            "<i>“O Imposto de Importação tem natureza parafiscal, pois sua receita é vinculada ao comércio "
            "exterior.”</i> → ERRADO (troca de conceito)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. A extrafiscalidade do Imposto de Importação refere-se ao seu uso como instrumento "
                            "de política econômica, para proteger a indústria nacional, regular o mercado e influenciar "
                            "o comércio exterior.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0602
    {
        "id": "ECO-E1-0602-1", "fonte_ref": "E1-0602", "destino": "47", "subtema": H2["trib"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à carga tributária brasileira.",
        "rotulo_item": "Item",
        "assertiva": ("A carga tributária é definida como a parcela da renda interna destinada aos cofres do setor "
                      "público. No caso brasileiro: a arrecadação de impostos indiretos constitui uma das principais "
                      "fontes de recursos para todos os entes federativos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A carga tributária é definida como a parcela da renda interna destinada aos cofres do setor "
                      "público. No caso brasileiro: a arrecadação de impostos indiretos constitui <u>uma das "
                      "principais</u> fontes de recursos para <u>todos os entes federativos</u>."),
        "poucas": ("No " + rx("Brasil") + ", a tributação sobre bens e serviços sustenta os três níveis: "
                   + azb("IPI, PIS/Cofins") + " (União), " + azb("ICMS") + " (estados) e " + azb("ISS")
                   + " mais a cota-parte do ICMS (municípios)."),
        "destrinchando": [
            azb("Carga tributária bruta") + " = arrecadação total de tributos ÷ PIB. No Brasil, gira na casa de "
            + vd("32% a 33% do PIB") + " ⏳ (out/2026), alta para um país de renda média.",
            "Composição: os tributos sobre " + azb("bens e serviços") + " respondem por cerca de " + vd("40%")
            + " da arrecadação ⏳ (out/2026), a maior fatia; renda e patrimônio pesam menos que a média da OCDE.",
            "Por ente: " + azb("União") + " — IPI, PIS/Cofins, IOF, Imposto de Importação; " + azb("estados")
            + " — " + vd("ICMS") + ", o maior tributo isolado do país; " + azb("municípios") + " — " + vd("ISS")
            + " e, sobretudo, transferências de " + vd("25% do ICMS") + " (cota-parte) e do FPM, formado por IR e IPI. "
            "Indiretos aparecem em todas as esferas, direta ou indiretamente.",
            "Consequência: matriz " + azb("regressiva") + " (consumo pesa mais para os pobres), pouco transparente e "
            "complexa. A reforma da " + vd("EC 132/2023") + " troca ICMS, ISS, IPI e PIS/Cofins por " + vd("IBS")
            + " e " + vd("CBS") + " (transição " + vd("2026–2033") + ") ⏳ (out/2026), mas mantém o peso do consumo.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O “todos os entes” soa como modulador "
                       "absoluto, mas é verdadeiro — e o “uma das principais” suaviza a afirmação. A definição de "
                       "carga tributária na 1ª frase é a de manual."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No caso brasileiro, os impostos diretos sobre a renda constituem a principal fonte de arrecadação "
            "dos municípios.”</i> → ERRADO (troca de conceito: ISS e transferências)",
            "<i>“A carga tributária brasileira é progressiva porque se concentra em tributos sobre o consumo.”</i> → "
            "ERRADO (nexo indevido: consumo torna a carga regressiva)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["uma das principais", "todos"],
        "dificuldade": 1,
        "comentario_fonte": "CERTO. No Brasil, a tributação indireta (ICMS, IPI, ISS) representa grande parcela da "
                            "arrecadação e afeta todos os níveis de governo; é também razão da regressividade da "
                            "carga.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
