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
    # ------------------------------------------------------------------ E1-0603
    {
        "id": "ECO-E1-0603-1", "fonte_ref": "E1-0603", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_ESTAB,
        "rotulo_item": "Item",
        "assertiva": ("O aumento dos gastos do governo quando a economia está em depressão e a diminuição desses mesmos "
                      "gastos quando a economia está em crescimento acelerado, pressionando a taxa de inflação, são "
                      "medidas de política de estabilização da economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O <u>aumento</u> dos gastos do governo quando a economia está em <u>depressão</u> e a "
                      "<u>diminuição</u> desses mesmos gastos quando a economia está em <u>crescimento acelerado</u>, "
                      "pressionando a taxa de inflação, são medidas de política de estabilização da economia."),
        "poucas": ("É a " + azb("política fiscal anticíclica") + ": gastar mais na recessão e menos no "
                   "superaquecimento suaviza o ciclo — o núcleo da " + azb("função estabilizadora") + " do Estado."),
        "destrinchando": [
            "Lógica keynesiana: na depressão, a " + azb("demanda agregada") + " é insuficiente e há capacidade "
            "ociosa e desemprego; o gasto público adicional ocupa esse espaço e, via " + azb("multiplicador")
            + ", eleva a renda mais do que o próprio gasto. No boom, a demanda supera a capacidade e pressiona os "
            "preços; cortar gasto esfria a economia e contém a inflação.",
            "No modelo IS-LM, o aumento de G desloca a IS para a direita (Y↑, i↑); o corte a desloca para a esquerda "
            "(Y↓, i↓). No OA-DA, a DA se desloca no mesmo sentido.",
            "Há ainda os " + azb("estabilizadores automáticos") + ": seguro-desemprego e impostos progressivos "
            "variam sozinhos com o ciclo (gasto sobe e receita cai na recessão), sem nova decisão do governo.",
            "Limites: " + azb("defasagens") + " (reconhecer, aprovar e executar leva tempo), " + azb("efeito "
            "deslocamento") + " (crowding out) via juros e o viés político de gastar na recessão e não cortar na "
            "expansão — o que transforma a política anticíclica em déficit permanente.",
            vm("Regra-âncora: anticíclica = remar contra o ciclo; pró-cíclica = acompanhar o ciclo e ampliar a "
               "oscilação."),
        ],
        "dissecando": (cz("[literalidade]") + " O item descreve corretamente os dois lados da política anticíclica. "
                       "A pegadinha possível seria inverter um dos lados (cortar gasto na depressão), o que tornaria a "
                       "política pró-cíclica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução dos gastos do governo durante uma depressão é medida típica de política anticíclica.”</i> "
            "→ ERRADO (inversão: isso é pró-cíclico)",
            "<i>“O seguro-desemprego atua como estabilizador automático.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. Política fiscal anticíclica, instrumento de estabilização: estimula a economia em "
                            "recessões e contém pressões inflacionárias no superaquecimento.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0604
    {
        "id": "ECO-E1-0604-1", "fonte_ref": "E1-0604", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CONTR,
        "rotulo_item": "Item",
        "assertiva": "Na política fiscal contracionista ocorre aumento de taxa de juros.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na política ") + vm("fiscal") + az(" contracionista ocorre aumento de taxa de juros."),
        "poucas": ("Elevar juros é instrumento de política " + azb("monetária") + " contracionista. A política "
                   + azb("fiscal") + " mexe em gastos e tributos — e, no IS-LM, sua versão contracionista até "
                   + "<b>reduz</b> os juros."),
        "destrinchando": [
            "Divisão de instrumentos: " + azb("política fiscal") + " = gasto público, tributos e transferências "
            "(Tesouro, Congresso); " + azb("política monetária") + " = taxa básica de juros, oferta de moeda, "
            "compulsório, redesconto, open market (Banco Central).",
            "Política fiscal contracionista: corte de gastos ou alta de impostos. No " + azb("IS-LM") + ", a IS se "
            "desloca para a esquerda: a renda cai, a demanda por moeda cai e a taxa de juros de equilíbrio "
            + vd("cai") + " — o oposto do que o item afirma.",
            "Política monetária contracionista: o BC eleva a taxa básica (no " + rx("Brasil") + ", a Selic) ou "
            "reduz a oferta de moeda; a LM se desloca para a esquerda, com " + vd("i↑") + " e " + vd("Y↓") + ".",
            "Combinação clássica de ajuste: fiscal contracionista + monetária expansionista permite derrubar o "
            "déficit e os juros sem derrubar tanto a renda — o chamado " + azb("policy mix") + ".",
            vm("Regra-âncora: juros e moeda → monetária (LM); gastos e tributos → fiscal (IS)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item atribui à política fiscal um efeito/instrumento da "
                       "monetária. Itens da série “Na política fiscal contracionista ocorre…” se resolvem "
                       "perguntando: isto é gasto ou tributo? Se for juros ou moeda, é outra política."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na política monetária contracionista ocorre aumento da taxa de juros.”</i> → CERTO",
            "<i>“No modelo IS-LM, a política fiscal contracionista reduz a renda e a taxa de juros.”</i> → CERTO",
        ])],
        "reescrita": "Na política " + hl("monetária") + " contracionista ocorre aumento de taxa de juros.",
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. O aumento da taxa de juros é instrumento de política monetária contracionista, "
                            "não fiscal; a política fiscal atua sobre gastos e tributos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0605
    {
        "id": "ECO-E1-0605-1", "fonte_ref": "E1-0605", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CONTR,
        "rotulo_item": "Item",
        "assertiva": "Na política fiscal contracionista ocorre emissão de moeda.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na política ") + vm("fiscal contracionista") + az(" ocorre emissão de moeda."),
        "poucas": ("Emitir moeda é política " + azb("monetária expansionista") + ". O item erra duas vezes: o tipo "
                   "de política (fiscal × monetária) e o sentido (contracionista × expansionista)."),
        "destrinchando": [
            "Emissão de moeda amplia a base monetária e a liquidez: é medida " + azb("expansionista") + ", conduzida "
            "pelo " + azb("Banco Central") + " (no open market, comprando títulos; no redesconto, emprestando aos "
            "bancos). No IS-LM, desloca a LM para a direita: i↓, Y↑.",
            "Política fiscal contracionista é corte de gastos ou alta de tributos: <b>tira</b> dinheiro de "
            "circulação na economia real, em vez de pôr.",
            "A única ponte entre fiscal e emissão é o " + azb("financiamento monetário do déficit") + " "
            "(senhoriagem): o governo gasta mais do que arrecada e o BC cobre a diferença imprimindo moeda — "
            "situação de política fiscal <b>expansionista</b>, associada a inflação alta. No " + rx("Brasil")
            + ", a CF/1988 proíbe o BC de financiar diretamente o Tesouro (" + vd("art. 164, § 1º") + ").",
            vm("Regra-âncora: emissão de moeda = monetária expansionista; política fiscal não emite moeda."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Duplo erro empilhado: troca o tipo de política e o "
                       "sentido da medida. Na série de itens sobre política fiscal contracionista, só “aumento de "
                       "impostos” e “redução de gastos públicos” são CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na política monetária expansionista ocorre emissão de moeda.”</i> → CERTO",
            "<i>“O financiamento do déficit público por emissão de moeda caracteriza política fiscal "
            "contracionista.”</i> → ERRADO (inversão: o déficit é expansionista)",
        ])],
        "reescrita": "Na política " + hl("monetária expansionista") + " ocorre emissão de moeda.",
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. A emissão de moeda está ligada à política monetária expansionista, realizada "
                            "pelo Banco Central; política fiscal não envolve emissão de moeda diretamente.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [FIG_PERDIDA("Untitled (113).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0606
    {
        "id": "ECO-E1-0606-1", "fonte_ref": "E1-0606", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CONTR,
        "rotulo_item": "Item",
        "assertiva": "Na política fiscal contracionista ocorre aumento de impostos.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na política fiscal contracionista ocorre <u>aumento de impostos</u>."),
        "poucas": ("Política fiscal contracionista = " + azb("alta de tributos") + " e/ou " + azb("corte de gastos")
                   + " públicos: reduz a demanda agregada e a renda."),
        "destrinchando": [
            "Aumento de impostos reduz a " + azb("renda disponível") + " (Y − T); as famílias consomem menos e a "
            "demanda agregada cai. Pela cruz keynesiana, o efeito sobre a renda é dado pelo multiplicador dos "
            "tributos: " + vd("ΔY = −c/(1 − c) · ΔT") + ", menor em módulo que o do gasto (" + vd("1/(1 − c)")
            + "), porque parte do imposto teria sido poupada.",
            "No " + azb("IS-LM") + ", alta de impostos ou corte de gastos desloca a " + azb("IS para a esquerda")
            + ": a renda cai e, com menos demanda por moeda, os juros de equilíbrio também caem.",
            "No " + azb("OA-DA") + ", a DA se desloca para a esquerda: menos produto e menos pressão inflacionária "
            "no curto prazo — por isso a contração fiscal é receita de combate a superaquecimento e de ajuste das "
            "contas públicas.",
            "Os instrumentos fiscais são três: gasto, tributo e transferência. Contracionista é qualquer combinação "
            "que reduza a demanda: ↑T, ↓G, ↓transferências.",
        ],
        "dissecando": (cz("[literalidade]") + " Único item CERTO da série sobre o que “ocorre” na política fiscal "
                       "contracionista ao lado do corte de gastos públicos. Os distratores costumam ser juros, "
                       "emissão de moeda, aumento de gastos públicos ou privados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na política fiscal contracionista, o aumento de impostos desloca a IS para a esquerda e eleva a "
            "taxa de juros.”</i> → ERRADO (inversão: os juros caem)",
            "<i>“O multiplicador dos tributos é, em módulo, maior que o multiplicador dos gastos.”</i> → ERRADO "
            "(inversão: é menor)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. A política fiscal contracionista reduz a demanda agregada por aumento de impostos "
                            "ou redução de gastos; no IS-LM, desloca a IS para a esquerda, reduzindo renda e juros.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_PERDIDA("Untitled (101).jpeg")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0607
    {
        "id": "ECO-E1-0607-1", "fonte_ref": "E1-0607", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CONTR,
        "rotulo_item": "Item",
        "assertiva": "Na política fiscal contracionista ocorre aumento de gastos privados.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na política fiscal contracionista ocorre ") + vm("aumento") + az(" de gastos privados."),
        "poucas": ("A contração fiscal reduz a " + azb("renda disponível") + " e a renda agregada; com isso, o "
                   "consumo das famílias cai. O efeito típico sobre os gastos privados é de " + azb("redução") + "."),
        "destrinchando": [
            "Canal direto: alta de impostos corta a renda disponível (Y − T) → o " + azb("consumo") + " cai pela "
            "propensão marginal a consumir. Canal indireto: corte de gasto público reduz a renda de fornecedores e "
            "trabalhadores → menos consumo, pelo " + azb("multiplicador") + ".",
            "Na cruz keynesiana (investimento autônomo), o único efeito sobre o gasto privado é a queda do consumo. "
            "O gasto privado não “ocupa” o espaço deixado pelo governo.",
            "Nuance de IS-LM: como os juros caem com a contração fiscal, o " + azb("investimento") + " pode subir "
            "(o inverso do " + azb("crowding out") + ", às vezes chamado de crowding in). Mas isso só atenua a "
            "queda da renda; o efeito dominante sobre consumo e demanda é contracionista.",
            "Tese oposta — a " + azb("contração fiscal expansionista") + " — sustenta que um ajuste crível pode "
            "elevar a confiança e o gasto privado. É hipótese controversa, não o efeito padrão cobrado em prova.",
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sentido do efeito: contração gera redução da demanda "
                       "privada, não aumento. Na série “ocorre…”, só aumento de impostos e corte de gastos públicos "
                       "descrevem a política contracionista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na política fiscal contracionista ocorre redução da renda disponível das famílias.”</i> → CERTO",
            "<i>“No IS-LM, a política fiscal contracionista, ao reduzir os juros, pode estimular o investimento "
            "privado.”</i> → CERTO",
        ])],
        "reescrita": "Na política fiscal contracionista ocorre " + hl("redução") + " de gastos privados.",
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. A política fiscal contracionista reduz a renda disponível e a demanda agregada, "
                            "o que tende a reduzir os gastos privados.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0608
    {
        "id": "ECO-E1-0608-1", "fonte_ref": "E1-0608", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CONTR,
        "rotulo_item": "Item",
        "assertiva": "Na política fiscal contracionista ocorre aumento de gastos públicos.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na política fiscal contracionista ocorre ") + vm("aumento") + az(" de gastos públicos."),
        "poucas": ("Aumentar gasto público é política fiscal " + azb("expansionista") + ". A contracionista "
                   + azb("reduz") + " gastos e/ou eleva tributos."),
        "destrinchando": [
            "O gasto do governo (G) é componente direto da demanda agregada (Y = C + I + G + NX). Elevá-lo aumenta a "
            "demanda e, pelo " + azb("multiplicador keynesiano") + " " + vd("1/(1 − c)") + ", a renda cresce mais "
            "que o próprio gasto.",
            "No " + azb("IS-LM") + ", ↑G desloca a IS para a direita (Y↑, i↑); ↓G desloca para a esquerda "
            "(Y↓, i↓).",
            "Classificação de bolso: " + azb("expansionista") + " = ↑G, ↓T, ↑transferências; "
            + azb("contracionista") + " = ↓G, ↑T, ↓transferências.",
            "Caso especial: aumentar G e T no mesmo valor ainda é expansionista — pelo " + azb("teorema do "
            "orçamento equilibrado") + " de " + oc("Haavelmo") + ", a renda sobe exatamente o valor do gasto "
            "(multiplicador igual a 1).",
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido do instrumento: aumento de gasto é a ferramenta "
                       "expansionista por excelência. Item fácil, mas aparece em série com distratores parecidos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na política fiscal contracionista ocorre redução de gastos públicos.”</i> → CERTO",
            "<i>“Um aumento simultâneo e de igual valor de gastos e impostos não altera a renda.”</i> → ERRADO "
            "(contradição com Haavelmo: a renda sobe ΔG)",
        ])],
        "reescrita": "Na política fiscal contracionista ocorre " + hl("redução") + " de gastos públicos.",
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. O aumento de gastos públicos caracteriza política fiscal expansionista; a "
                            "contracionista reduz os gastos públicos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0609
    {
        "id": "ECO-E1-0609-1", "fonte_ref": "E1-0609", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EXP,
        "rotulo_item": "Item",
        "assertiva": ("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política fiscal que "
                      "aumente o gasto do governo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política fiscal que "
                      "<u>aumente o gasto do governo</u>."),
        "poucas": ("↑G eleva diretamente a " + azb("demanda agregada") + " e, pelo " + azb("multiplicador")
                   + ", a renda e o emprego: é a política fiscal expansionista típica."),
        "destrinchando": [
            "Na " + azb("cruz keynesiana") + ", ΔY = ΔG / (1 − c). Com propensão marginal a consumir de "
            + vd("0,8") + ", o multiplicador é " + vd("5") + ": cada R$ 1 de gasto gera até R$ 5 de renda, porque "
            "a renda de quem recebe o gasto vira consumo de outros, em rodadas sucessivas.",
            "No " + azb("IS-LM") + ", ↑G desloca a IS para a direita; a renda sobe menos que na cruz porque os juros "
            "também sobem e deslocam parte do investimento privado (" + azb("crowding out") + ").",
            "Casos-limite: LM vertical (clássico) → crowding out total, a política fiscal não altera a renda; LM "
            "horizontal (" + azb("armadilha da liquidez") + ") → crowding out nulo, efeito máximo.",
            "O “tudo mais constante” isola o efeito: sem reação do Banco Central, sem mudança de expectativas, sem "
            "aumento simultâneo de impostos.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O “pode” e o “tudo mais constante” protegem o "
                       "item contra as exceções (crowding out total, equivalência ricardiana). Itens da série sobre "
                       "objetivo expansionista pedem só o sentido correto de cada instrumento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento do gasto do governo eleva a renda sempre no valor do multiplicador simples, qualquer que "
            "seja a inclinação da LM.”</i> → ERRADO (modulador absoluto: há crowding out)",
            "<i>“Na armadilha da liquidez, a política fiscal expansionista tem efeito máximo sobre a renda.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "tudo mais constante"],
        "dificuldade": 1,
        "comentario_fonte": "CERTO. Aumentar os gastos públicos é política fiscal expansionista, que eleva a demanda "
                            "agregada, o nível de atividade e pode reduzir o desemprego.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0610
    {
        "id": "ECO-E1-0610-1", "fonte_ref": "E1-0610", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EXP,
        "rotulo_item": "Item",
        "assertiva": ("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política fiscal que "
                      "altere alíquotas de tributos, mantendo a arrecadação constante."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política fiscal "
                       "que ") + vm("altere") + az(" alíquotas de tributos, ")
                    + vm("mantendo a arrecadação constante") + az(".")),
        "poucas": ("No modelo agregado, se a " + azb("arrecadação não muda") + ", a renda disponível total não muda "
                   "e não há impulso à demanda. O estímulo exige " + azb("reduzir") + " a carga."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Mantido o ERRADO da fonte, que segue o modelo de propensão a consumir única. Com "
                          "propensões diferentes entre grupos, porém, trocar alíquotas com arrecadação constante "
                          "<b>pode</b> expandir a demanda: tirar carga de quem consome quase toda a renda e pô-la em "
                          "quem poupa mais eleva o consumo agregado. O “pode” do item torna o CERTO defensável; em "
                          "prova, siga a leitura do modelo simples.")],
        "destrinchando": [
            "Na " + azb("cruz keynesiana") + ", o que move a demanda é a renda disponível agregada (Y − T). Se o "
            "total arrecadado T é o mesmo, mudar só a distribuição das alíquotas deixa Y − T igual e o consumo "
            "agregado, com uma única propensão c, não se altera: " + vd("ΔT = 0 → ΔY = 0") + ".",
            "Instrumentos fiscais expansionistas: " + azb("↑G") + " (multiplicador 1/(1 − c)), " + azb("↓T")
            + " (multiplicador −c/(1 − c)) e " + azb("↑transferências") + ". Todos alteram o saldo orçamentário "
            "na direção do déficit — exceto o caso de " + oc("Haavelmo") + " (↑G = ↑T), que expande com orçamento "
            "equilibrado porque o gasto entra inteiro na demanda.",
            "Por que a ressalva do ⚠️ importa: o consumo das famílias de baixa renda reage mais à renda disponível "
            "(propensão marginal a consumir maior). Uma reforma neutra em arrecadação, mas mais progressiva, pode "
            "elevar o consumo agregado — argumento usado a favor de isenções na base com compensação no topo.",
            "Também podem gerar efeito real mudanças que alterem incentivos (alíquotas sobre investimento, "
            "trabalho), mas isso é lado da oferta, não estímulo de demanda.",
        ],
        "dissecando": (cz("[restrição indevida · contradição]") + " A ressalva “mantendo a arrecadação constante” "
                       "anula o canal pelo qual o tributo expande a demanda no modelo de manual. A série de itens "
                       "pede a direção de cada instrumento: ↑G e ↓T expandem; ↓agregados monetários contraem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um objetivo expansionista pode ser alcançado por um aumento do gasto financiado por aumento "
            "equivalente de impostos.”</i> → CERTO (teorema do orçamento equilibrado)",
            "<i>“Um objetivo expansionista pode ser alcançado por uma política fiscal que eleve alíquotas e "
            "arrecadação.”</i> → ERRADO (inversão: é contracionista)",
        ])],
        "reescrita": ("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política fiscal que "
                      + hl("reduza") + " alíquotas de tributos, " + hl("reduzindo a arrecadação") + "."),
        "tipo_erro": ["RESTRICAO", "CONTRADICAO"], "moduladores": ["pode", "tudo mais constante"],
        "dificuldade": 2,
        "comentario_fonte": "ERRADO. Se a arrecadação permanece constante, não há efeito líquido expansionista "
                            "relevante; alterar alíquotas sem mudar a carga não garante estímulo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: com propensões a consumir distintas entre grupos, recompor alíquotas com "
                    "arrecadação constante pode expandir o consumo agregado; mantido o ERRADO da fonte (modelo "
                    "agregado)"],
    },
    # ------------------------------------------------------------------ E1-0611
    {
        "id": "ECO-E1-0611-1", "fonte_ref": "E1-0611", "destino": "47", "subtema": H2["fisc"],
        "tipo": "C/E", "banca": BNI, "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_EXP,
        "rotulo_item": "Item",
        "assertiva": ("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política monetária "
                      "que reduza os agregados monetários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política monetária "
                       "que ") + vm("reduza") + az(" os agregados monetários.")),
        "poucas": ("Reduzir os " + azb("agregados monetários") + " (M1, M2…) enxuga liquidez, eleva juros e contrai "
                   "a demanda. Para expandir, a política monetária precisa " + azb("ampliar") + " a oferta de moeda."),
        "destrinchando": [
            azb("Agregados monetários") + " medem os meios de pagamento em ordem decrescente de liquidez: "
            + vd("M1") + " (papel-moeda em poder do público + depósitos à vista), M2, M3, M4 (incluem depósitos de "
            "poupança, títulos e fundos).",
            "Política monetária " + azb("contracionista") + " — venda de títulos no open market, alta do "
            "compulsório, alta da taxa básica — reduz os agregados; no IS-LM, a LM vai para a esquerda: " + vd("i↑")
            + ", " + vd("Y↓") + ".",
            "Política monetária " + azb("expansionista") + " — compra de títulos, corte do compulsório, queda dos "
            "juros — amplia os agregados; a LM vai para a direita: " + vd("i↓") + ", " + vd("Y↑") + ", via mais "
            "investimento e consumo a crédito.",
            "Limite: na " + azb("armadilha da liquidez") + " (LM horizontal), ampliar a moeda não reduz os juros e "
            "a política monetária perde eficácia.",
            vm("Regra-âncora: mais moeda = expansionista; menos moeda = contracionista."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido do instrumento monetário. Note que a banca mudou de "
                       "política (fiscal → monetária) dentro da mesma série: o que decide é a direção, não o tipo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um objetivo expansionista pode ser alcançado por uma política monetária que eleve os agregados "
            "monetários.”</i> → CERTO",
            "<i>“A venda de títulos públicos pelo Banco Central amplia os agregados monetários.”</i> → ERRADO "
            "(inversão: a venda enxuga moeda)",
        ])],
        "reescrita": ("Um objetivo expansionista, tudo mais constante, pode ser alcançado por uma política monetária "
                      "que " + hl("amplie") + " os agregados monetários."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["pode", "tudo mais constante"], "dificuldade": 1,
        "comentario_fonte": "ERRADO. Reduzir os agregados monetários é medida contracionista: restringe liquidez e "
                            "crédito, desestimulando consumo e investimento.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
