"""Cards do lote de redação 02 — ECO, passada 02 (nota 17: Contas Nacionais)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "id": "🔄 Identidades e óticas do produto",
    "pib": "📏 PIB, PNB, RNB e conceitos derivados",
    "pm": "💲 Preços de mercado × custo de fatores",
    "real": "📊 Nominal × real e deflator",
    "scn": "🧾 SCN e tabelas",
}

CMD_SCN = "Julgue o item a seguir, relativo à estrutura do Sistema de Contas Nacionais."

CMD_NIDI_26 = ("As Contas Nacionais são fundamentais para a análise da atividade econômica e a formulação de "
               "políticas públicas. Compreender sua estrutura e seus agregados permite uma avaliação precisa do "
               "desempenho econômico. Sobre os conceitos básicos da Contabilidade Social, julgue (C ou E) os itens "
               "a seguir.")

CMD_BOZAN = "Em relação à estrutura e ao cálculo das Contas Nacionais, julgue (C ou E) os próximos itens."

CMD_ARM = "Julgue o item a seguir, relativo às Contas Nacionais."

CMD_NAB_CN = ("A respeito das contas nacionais, balanço de pagamentos, contas públicas e sistema monetário, julgue "
              "(C ou E) os itens seguintes.")

FIG_E1 = lambda ref: [{"ref": ref, "tipo_fonte": "GRÁFICO", "lado": "verso",
                       "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}]

CARDS = [
    # ------------------------------------------------------------------ E1-0420
    {
        "id": "ECO-E1-0420-1", "fonte_ref": "E1-0420", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_SCN,
        "rotulo_item": "Item",
        "assertiva": ("O saldo final da Conta de Acumulação, também denominada Conta de Capital, expressa a "
                      "Necessidade ou Capacidade de Financiamento Externo da economia. Esta conta evidencia como o "
                      "“não consumo” da produção nacional se distribui entre a Formação Bruta de Capital Fixo e a "
                      "Formação de Estoques, além de considerar as Transferências de Capital com o resto do mundo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O saldo final da Conta de Acumulação, também denominada Conta de Capital, expressa a "
                      "<u>Necessidade ou Capacidade de Financiamento</u> Externo da economia. Esta conta evidencia "
                      "como o “não consumo” da produção nacional se distribui entre a Formação Bruta de Capital Fixo "
                      "e a Formação de Estoques, além de considerar as <u>Transferências de Capital</u> com o resto "
                      "do mundo."),
        "poucas": ("Na conta de capital, a " + azb("poupança bruta") + " (o “não consumo”) e as transferências de "
                   "capital líquidas financiam a FBCF e a variação de estoques; o que sobra ou falta é a "
                   + azb("capacidade (+) ou necessidade (−) de financiamento") + " perante o resto do mundo."),
        "destrinchando": [
            "A sequência de contas funciona como uma cascata: produção gera " + azb("valor adicionado") + "; a "
            "distribuição da renda leva à " + azb("renda disponível") + "; o uso da renda a reparte entre consumo "
            "final e " + azb("poupança") + "; e a poupança desemboca na conta de capital, a última etapa interna "
            "antes das operações com o exterior.",
            "Conta de capital — recursos: poupança bruta + transferências de capital líquidas recebidas; usos: "
            "formação bruta de capital fixo + variação de estoques (+ aquisição líquida de ativos não produzidos). "
            "Saldo: " + vd("S + TK − FBCF − ΔE") + ".",
            "Saldo positivo = " + azb("capacidade de financiamento") + ": o país gerou mais poupança do que "
            "investiu e empresta a diferença ao resto do mundo. Saldo negativo = " + azb("necessidade de "
            "financiamento") + ": a economia absorve poupança externa.",
            "O mesmo número aparece no balanço de pagamentos: capacidade/necessidade de financiamento = "
            + vd("saldo em transações correntes + saldo da conta capital") + ". Um déficit em transações "
            "correntes, como o que o " + rx("Brasil") + " registra tradicionalmente, corresponde a necessidade de "
            "financiamento.",
            "Cuidado com o homônimo: a <b>conta capital do BP</b> (transferências de capital e ativos não "
            "financeiros não produzidos) é outra coisa que a <b>conta de capital do SCN</b>, que registra a "
            "acumulação de toda a economia.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item reproduz a descrição de manual da conta de "
                       "capital. O risco está no vocabulário: “não consumo” é a poupança, e “Necessidade ou "
                       "Capacidade” cobre os dois sinais do saldo. Quem confunde com a conta capital do BP tende a "
                       "marcar ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Saldo positivo da conta de capital indica necessidade de financiamento externo.”</i> → ERRADO "
            "(inversão: positivo = capacidade)",
            "<i>“A capacidade de financiamento da economia equivale à soma dos saldos em transações correntes e "
            "da conta capital do balanço de pagamentos.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("CERTO: é o saldo da conta de acumulação; negativo = quanto se precisa absorver do "
                             "exterior; positivo = quanto sobrou. Cascata de contas; conta capital do BP ≠ conta "
                             "de capital da CEI."),
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("image (143).png, image (153).png, image (150).png"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0421
    {
        "id": "ECO-E1-0421-1", "fonte_ref": "E1-0421", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_SCN,
        "rotulo_item": "Item",
        "assertiva": ("No Sistema de Contas Nacionais, o saldo final de cada conta representa o ponto de partida "
                      "da próxima conta do sistema. Desta maneira, o saldo final da Conta 0 (Conta de Bens e "
                      "Serviços) é a primeira rubrica apresentada na Conta 1 (Conta de Produção) e assim "
                      "sucessivamente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No Sistema de Contas Nacionais, o saldo final de cada conta representa o ponto de partida "
                       "da próxima conta do sistema. Desta maneira, o saldo final da ")
                    + vm("Conta 0 (Conta de Bens e Serviços)") + az(" é a primeira rubrica apresentada na ")
                    + vm("Conta 1 (Conta de Produção)") + az(" e assim sucessivamente.")),
        "poucas": ("A " + azb("Conta 0 (bens e serviços)") + " é uma conta de <b>equilíbrio</b> — oferta total = "
                   "demanda total — e não tem saldo. O encadeamento de saldos começa na " + azb("Conta 1 "
                   "(produção)") + ", cujo saldo, o valor adicionado, abre a conta de renda."),
        "destrinchando": [
            "As Contas Econômicas Integradas do IBGE se organizam em: " + vd("Conta 0") + " bens e serviços; "
            + vd("Conta 1") + " produção; " + vd("Conta 2") + " distribuição e uso da renda; " + vd("Conta 3")
            + " acumulação; " + vd("Conta 4") + " resto do mundo.",
            "A Conta 0 confronta recursos e usos de bens e serviços: " + vd("produção + importações + impostos "
            "sobre produtos − subsídios = consumo intermediário + consumo final + FBC + exportações") + ". Os dois "
            "lados se igualam por construção; não há saldo a transportar.",
            "A partir da Conta 1, cada saldo vira a primeira linha da conta seguinte: " + azb("valor adicionado")
            + " → geração da renda → " + azb("excedente operacional") + " → alocação da renda primária → "
            + azb("saldo da renda primária") + " → distribuição secundária → " + azb("renda disponível")
            + " → uso da renda → " + azb("poupança") + " → conta de capital → capacidade/necessidade de "
            "financiamento.",
            "A primeira metade do item (cada saldo abre a conta seguinte) descreve bem essa cascata; o erro é "
            "pôr nela a Conta 0, que funciona como quadro de conferência entre a oferta e a demanda de bens e "
            "serviços, ligando a Tabela de Recursos e Usos às contas dos setores.",
            vm("Regra-âncora: Conta 0 = equilíbrio sem saldo; o primeiro saldo do sistema é o valor adicionado."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A regra geral do encadeamento é verdadeira; o "
                       "erro foi enxertado no exemplo, que estende a regra à única conta que não tem saldo. Pista: "
                       "“Desta maneira” transforma uma regra correta em exemplo falso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo da conta de produção, o valor adicionado bruto, é o ponto de partida da conta de geração "
            "da renda.”</i> → CERTO",
            "<i>“O saldo da conta de uso da renda é a renda disponível bruta.”</i> → ERRADO (troca de conceito: "
            "o saldo é a poupança bruta)",
        ])],
        "reescrita": ("No Sistema de Contas Nacionais, o saldo final de cada conta representa o ponto de partida da "
                      "próxima conta do sistema. Desta maneira, o saldo final da " + hl("Conta 1 (Conta de "
                      "Produção)") + " é a primeira rubrica apresentada na " + hl("Conta 2 (Conta de Distribuição e "
                      "Uso da Renda)") + " e assim sucessivamente."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("ERRADO: a Conta 0 é conta-espelho, integra a TRU e a CEI e mostra o panorama geral; "
                             "seu saldo seria tudo o que foi produzido e consumido (oferta final, incluindo bens "
                             "intermediários)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": FIG_E1("image (143).png"),
        "alertas": ["qualidade_fonte: a fonte fala em “saldo final da Conta 0”; a Conta 0 é conta de equilíbrio "
                    "sem saldo — corrigido no comentário"],
    },
    # ------------------------------------------------------------------ E1-0843
    {
        "id": "ECO-E1-0843-1", "fonte_ref": "E1-0843", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Maio/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_26,
        "rotulo_item": "Item",
        "assertiva": ("O PIB real refere-se à contabilização do valor de mercado, ao preço de um período base, de "
                      "tudo o que foi produzido de bens e serviços finais dentro de um território. Assim, a melhoria "
                      "na qualidade dos produtos e serviços prestados enviesa o PIB real para baixo, em função da "
                      "dificuldade estatística de incorporar essas variações à mensuração do valor."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O PIB real refere-se à contabilização do valor de mercado, ao preço de um período base, de "
                      "tudo o que foi produzido de bens e serviços finais dentro de um território. Assim, a melhoria "
                      "na qualidade dos produtos e serviços prestados <u>enviesa o PIB real para baixo</u>, em função "
                      "da dificuldade estatística de incorporar essas variações à mensuração do valor."),
        "poucas": ("Se o índice de preços trata como <b>inflação</b> o que é, em parte, <b>produto melhor</b>, o "
                   "deflator fica alto demais e o " + azb("PIB real") + " (nominal ÷ deflator) sai "
                   + azb("subestimado") + "."),
        "destrinchando": [
            azb("PIB real") + " = produção do ano valorada a preços de um ano-base: isola a variação de "
            "<b>quantidade</b>. Na prática, obtém-se dividindo o nominal por um índice de preços (deflator).",
            "O problema: um celular deste ano custa mais que o do ano passado, mas também faz mais coisas. Se o "
            "estatístico registra a diferença de preço inteira como inflação, ignora o ganho de qualidade; a "
            "inflação medida fica <b>acima</b> da verdadeira e o crescimento real, <b>abaixo</b>.",
            "Para atenuar o viés, os institutos usam " + azb("preços hedônicos") + " (decompõem o preço em "
            "atributos: memória, velocidade, potência) e ajustes de qualidade na troca de itens da cesta. Mesmo "
            "assim, parte do ganho escapa — sobretudo em serviços (saúde, educação) e em bens novos.",
            "Referência clássica: a " + oc("Comissão Boskin") + " (EUA, " + vd("1996") + ") estimou que o "
            "índice de preços ao consumidor norte-americano superestimava a inflação em cerca de "
            + vd("1,1 ponto percentual por ano") + ", em boa parte por qualidade e bens novos.",
            "Vizinhos do tema: o PIB também ignora produção doméstica não remunerada, lazer e degradação "
            "ambiental — limitações do PIB como medida de bem-estar.",
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " Parece estranho que “melhorar” os produtos baixe o "
                       "PIB real; o item se salva porque fala em viés de <b>mensuração</b>, não em queda efetiva da "
                       "produção. A cadeia é: qualidade não captada → inflação superestimada → real subestimado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a melhoria na qualidade dos produtos enviesa para baixo a inflação medida.”</i> → ERRADO "
            "(inversão: enviesa a inflação para cima)",
            "<i>“O uso de preços hedônicos busca separar, na variação de preço, a parcela devida à melhoria de "
            "qualidade.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("PIB real mede a produção a preços constantes; melhorias de qualidade são difíceis de "
                             "separar de aumentos de preço e, não captadas, subestimam o crescimento real."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0844
    {
        "id": "ECO-E1-0844-1", "fonte_ref": "E1-0844", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Maio/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_26,
        "rotulo_item": "Item",
        "assertiva": ("A diferença entre o produto nacional (PN) e o produto interno (PI) é dada pela renda líquida "
                      "do exterior. Se a renda enviada ao exterior for maior que a renda recebida do exterior, "
                      "então: PI > PN."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A diferença entre o produto nacional (PN) e o produto interno (PI) é dada pela renda líquida "
                      "do exterior. Se a renda enviada ao exterior for <u>maior</u> que a renda recebida do "
                      "exterior, então: <u>PI > PN</u>."),
        "poucas": (vd("PN = PI − RLEE") + ". Se a renda enviada supera a recebida, a " + azb("renda líquida "
                   "enviada ao exterior") + " é positiva e o produto nacional fica <b>abaixo</b> do interno."),
        "destrinchando": [
            azb("Produto interno") + " = critério <b>territorial</b>: tudo o que se produz dentro das fronteiras, "
            "seja quem for o dono dos fatores. " + azb("Produto nacional") + " = critério de <b>propriedade</b>: "
            "a renda dos fatores pertencentes a residentes, onde quer que trabalhem.",
            "A ponte entre eles são as rendas de fatores (renda primária: lucros, dividendos, juros, salários) que "
            "cruzam a fronteira: " + vd("PN = PI + renda recebida − renda enviada") + " = PI − RLEE.",
            "Dois sinais, dois casos: RLEE > 0 (envia mais do que recebe) → " + vd("PI > PN") + ", típico de "
            "economias com muito capital estrangeiro e dívida externa; RLEE < 0 → PN > PI, típico de países "
            "credores ou com muitos investimentos no exterior.",
            "O " + rx("Brasil") + " é historicamente devedor de renda primária (remessas de lucros e dividendos "
            "de multinacionais e juros da dívida externa): por isso a " + azb("renda nacional bruta") + " "
            "brasileira fica abaixo do PIB.",
            "No vocabulário atual (SCN 2008/BPM6), PNB virou " + azb("renda nacional bruta (RNB)") + ", e a "
            "conta é a de “renda primária” do balanço de pagamentos.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de sinal: basta escrever a identidade e testar o caso. A "
                       "armadilha é a terminologia — “renda líquida do exterior” pode ser lida como recebida ou "
                       "enviada; o item resolve isso ao dizer quem é maior."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a renda recebida do exterior superar a enviada, o produto interno será maior que o "
            "nacional.”</i> → ERRADO (inversão: PN > PI)",
            "<i>“Em uma economia fechada, PIB e PNB coincidem.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PN = PI + (renda recebida − renda enviada); se envia mais do que recebe, a parcela é "
                             "negativa e PN < PI."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0845
    {
        "id": "ECO-E1-0845-1", "fonte_ref": "E1-0845", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Maio/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_26,
        "rotulo_item": "Item",
        "assertiva": "A taxa de crescimento do PIB real é sempre igual ou menor do que a taxa de crescimento do PIB nominal.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A taxa de crescimento do PIB real é ") + vm("sempre")
                    + az(" igual ou menor do que a taxa de crescimento do PIB nominal.")),
        "poucas": ("Real e nominal se separam pela variação do " + azb("deflator") + ": com inflação, o nominal "
                   "cresce mais; com " + azb("deflação") + ", o real cresce <b>mais</b> que o nominal. O "
                   "“sempre” derruba o item."),
        "destrinchando": [
            "Identidade: " + vd("(1 + g<sub>nominal</sub>) = (1 + g<sub>real</sub>) × (1 + π<sub>deflator</sub>)")
            + ", ou, aproximadamente, " + vd("g<sub>nominal</sub> ≈ g<sub>real</sub> + π") + ".",
            "Com π > 0 (caso usual), g<sub>real</sub> < g<sub>nominal</sub>; com π = 0, são iguais; com "
            + vd("π < 0") + " (deflação do PIB), g<sub>real</sub> > g<sub>nominal</sub>.",
            "Exemplo: produção física +2% e deflator −1% → PIB nominal ≈ +1%, real +2%. Pode até ocorrer PIB "
            "nominal em queda com PIB real em alta — o caso do " + azb("Japão") + " em vários anos de deflação "
            "desde os anos 1990.",
            "Note que o deflator relevante é o " + azb("deflator implícito do PIB") + " (preços de tudo o que se "
            "produz, incluindo exportações e bens de capital), não o índice ao consumidor: os dois podem divergir, "
            "por exemplo quando caem os preços das commodities exportadas.",
            vm("Regra-âncora: real > nominal ⇔ deflator caiu."),
        ],
        "dissecando": (cz("[modulador absoluto]") + " O item descreve o caso típico (inflação positiva) e o "
                       "transforma em lei com “sempre”. Em contas nacionais, absolutos sobre a relação "
                       "real × nominal quase sempre caem na exceção da deflação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o deflator do PIB cair, a taxa de crescimento real superará a nominal.”</i> → CERTO",
            "<i>“PIB nominal em queda implica, necessariamente, recessão.”</i> → ERRADO (modulador absoluto: "
            "pode ser só deflação)",
        ])],
        "reescrita": ("A taxa de crescimento do PIB real é <s>sempre</s> igual ou menor do que a taxa de "
                      "crescimento do PIB nominal" + hl(" quando o deflator do PIB não cai") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("A relação entre crescimento nominal e real depende do deflator; com deflação, o real "
                             "pode crescer mais que o nominal; “sempre” torna o item falso."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0846
    {
        "id": "ECO-E1-0846-1", "fonte_ref": "E1-0846", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Maio/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_26,
        "rotulo_item": "Item",
        "assertiva": ("Para fins de registro nas Contas Nacionais, o investimento é qualquer gasto em bem ou serviço "
                      "final que aumenta a capacidade da economia de produzir mais no futuro."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para fins de registro nas Contas Nacionais, o investimento é ")
                    + vm("qualquer gasto em bem ou serviço final que aumenta a capacidade da economia de produzir "
                         "mais no futuro") + az(".")),
        "poucas": ("Nas Contas Nacionais, investimento é a " + azb("formação bruta de capital") + " — FBCF + "
                   "variação de estoques —, categoria contábil fechada. Gastos que elevam a capacidade futura, "
                   "como educação, ficam fora dela."),
        "destrinchando": [
            vd("I = FBC = FBCF + ΔE") + " (no SCN 2008, também a aquisição líquida de objetos de valor). "
            + azb("FBCF") + ": máquinas, equipamentos, construções (inclusive imóveis residenciais novos comprados "
            "por famílias), cultivos permanentes e, desde o SCN 2008, " + azb("produtos de propriedade "
            "intelectual") + " (P&D, software, bancos de dados, exploração mineral).",
            "Ficam <b>fora</b>, apesar de aumentarem a capacidade produtiva futura: gasto com " + azb("educação")
            + " e saúde (capital humano → consumo final das famílias ou do governo); compra de bens de consumo "
            "duráveis pelas famílias (carro, geladeira → consumo); treinamento de pessoal (consumo intermediário).",
            "Também não é investimento, no sentido macroeconômico, a compra de ativos <b>financeiros</b> (ações, "
            "títulos) nem de bens usados: são trocas de propriedade, não criação de capital novo.",
            "A definição contábil existe para que a identidade " + vd("PIB = C + I + G + (X − M)") + " some "
            "cada bem final uma vez só e para que " + vd("S = I") + " (em economia fechada) feche.",
            vm("Regra-âncora: investimento no SCN = FBCF + variação de estoques, não “todo gasto que aumenta a "
               "capacidade futura”."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O item troca a definição contábil pela "
                       "noção econômica intuitiva de investimento e a amplia com “qualquer”. Pista: em Contas "
                       "Nacionais, definições começam pela lista de componentes, não pela finalidade do gasto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A compra de um imóvel residencial novo por uma família é registrada como investimento.”</i> → "
            "CERTO",
            "<i>“Os gastos públicos com educação são registrados como formação bruta de capital fixo.”</i> → "
            "ERRADO (troca de conceito: são consumo final do governo)",
        ])],
        "reescrita": ("Para fins de registro nas Contas Nacionais, o investimento é " + hl("a formação bruta de "
                      "capital — formação bruta de capital fixo mais variação de estoques —, e não qualquer gasto "
                      "final que possa aumentar a capacidade de produção futura") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["qualquer"], "dificuldade": 1,
        "comentario_fonte": ("Investimento tem definição contábil (FBCF, variação de estoques); nem todo gasto que "
                             "eleva a capacidade futura, como educação, é contabilizado como investimento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0847
    {
        "id": "ECO-E1-0847-1", "fonte_ref": "E1-0847", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Maio/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_26,
        "rotulo_item": "Item",
        "assertiva": ("O Produto Interno Líquido a Custo de Fatores de um país é calculado subtraindo-se a "
                      "depreciação e os impostos indiretos líquidos de subsídios do Produto Interno Bruto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Produto Interno Líquido a Custo de Fatores de um país é calculado subtraindo-se a "
                      "<u>depreciação</u> e os <u>impostos indiretos líquidos de subsídios</u> do Produto Interno "
                      "Bruto."),
        "poucas": ("Duas passagens: bruto → líquido tira a " + azb("depreciação") + "; preço de mercado → custo "
                   "de fatores tira os " + azb("impostos indiretos líquidos de subsídios") + ". "
                   + vd("PILcf = PIBpm − D − (II − Sub)") + "."),
        "destrinchando": [
            "Os quatro qualificadores do produto se combinam em dois eixos: " + azb("bruto × líquido")
            + " (com ou sem depreciação) e " + azb("preços de mercado × custo de fatores") + " (com ou sem "
            "impostos indiretos líquidos de subsídios). Um terceiro eixo, " + azb("interno × nacional")
            + ", é a renda líquida enviada ao exterior.",
            "Por que tirar os impostos indiretos? O preço de mercado inclui ICMS, IPI, ISS etc., que não "
            "remuneram nenhum fator. O " + azb("custo de fatores") + " é só a remuneração de trabalho, capital, "
            "terra e empresário — salários, juros, aluguéis e lucros.",
            "Os subsídios fazem o contrário: barateiam o preço sem reduzir a remuneração dos fatores; por isso "
            "são <b>somados</b> na passagem de mercado para fatores: " + vd("PIBcf = PIBpm − II + Sub") + ".",
            "Bônus clássico: " + vd("PNLcf = renda nacional (RN)") + " — o produto nacional líquido a custo de "
            "fatores é a soma das remunerações dos fatores dos residentes.",
            "No SCN atual, aparece ainda o " + azb("valor adicionado a preços básicos") + ", que exclui só os "
            "impostos líquidos sobre <b>produtos</b>; os demais impostos sobre a produção (IPTU de empresas, "
            "taxas) continuam dentro dele.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a fórmula de manual. O risco está no sinal dos subsídios: "
                       "“impostos indiretos líquidos de subsídios” já embute o +Sub; quem lê “subtraindo-se… "
                       "subsídios” como se fosse para subtrair os subsídios desconfia sem razão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB a custo de fatores é obtido somando-se ao PIB a preços de mercado os impostos "
            "indiretos.”</i> → ERRADO (inversão: subtraem-se)",
            "<i>“O produto nacional líquido a custo de fatores corresponde à renda nacional.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PIBpm − depreciação = PIL; retirar impostos indiretos líquidos de subsídios passa a "
                             "custo de fatores: PILcf = PIBpm − depreciação − impostos indiretos + subsídios."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0860
    {
        "id": "ECO-E1-0860-1", "fonte_ref": "E1-0860", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2016", "ano": 2016, "cacd": True,
        "errei": True,
        "comando": ("O diplomata responsável pelo setor econômico da embaixada brasileira em determinado país "
                    "elaborou e enviou à Secretaria de Estado um relatório sobre a situação econômica desse país. "
                    "Considerando o fato de que uma das funções do diplomata é manter o governo brasileiro "
                    "informado a respeito do contexto político, econômico e cultural do país onde ele esteja "
                    "temporariamente vivendo, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Para não cometer o erro denominado “ilusão monetária”, o diplomata deve informar, em seu "
                      "relatório, o PIB real do país, em vez do nominal, dos últimos cinco anos. Para deflacionar "
                      "esses números, o diplomata deve utilizar o deflator (implícito) do PIB, que é calculado pelo "
                      "quociente entre o PIB real, medido a preços constantes, e o PIB nominal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para não cometer o erro denominado “ilusão monetária”, o diplomata deve informar, em seu "
                       "relatório, o PIB real do país, em vez do nominal, dos últimos cinco anos. Para deflacionar "
                       "esses números, o diplomata deve utilizar o deflator (implícito) do PIB, que é calculado pelo "
                       "quociente entre o ") + vm("PIB real, medido a preços constantes, e o PIB nominal")
                    + az(".")),
        "poucas": ("O " + azb("deflator implícito do PIB") + " é " + vd("PIB nominal ÷ PIB real") + " (× 100), "
                   "não o inverso. O resto do item — usar o PIB real para não cair em ilusão monetária — está "
                   "certo."),
        "destrinchando": [
            "PIB nominal = Σ p<sub>t</sub>·q<sub>t</sub> (preços correntes); PIB real = Σ p<sub>0</sub>·q<sub>t</sub> "
            "(preços do ano-base). A razão entre eles isola o efeito <b>preço</b>: " + vd("deflator = Σ "
            "p<sub>t</sub>q<sub>t</sub> / Σ p<sub>0</sub>q<sub>t</sub>") + " — um índice de Paasche.",
            "Daí o uso: " + vd("PIB real = PIB nominal ÷ deflator") + ". Com inflação, o nominal supera o real "
            "e o deflator fica acima de 100; com a fórmula invertida do item, ele ficaria abaixo de 100 e "
            "“deflacionar” inflaria a série.",
            azb("Ilusão monetária") + " é confundir variações nominais com reais — achar que o país cresceu 10% "
            "quando 8 pontos foram só inflação. Relatar o PIB real elimina o problema; por isso a primeira "
            "frase do item é correta.",
            "Por que o deflator implícito e não o IPCA? Porque cobre <b>todos</b> os bens finais produzidos "
            "(inclusive bens de capital e exportações), exatamente a cesta do PIB; o índice ao consumidor cobre "
            "só o consumo das famílias e inclui importados.",
            vm("Regra-âncora: deflator = nominal no numerador."),
        ],
        "dissecando": (cz("[inversão]") + " O item constrói um contexto inteiro verdadeiro e inverte só o "
                       "quociente na última oração. 🔥 O CEBRASPE gosta de esconder a inversão no fim de "
                       "assertivas longas, depois de o candidato já ter “comprado” a premissa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o PIB nominal cresceu 12% e o deflator 8%, o PIB real cresceu cerca de 3,7%.”</i> → CERTO "
            "(1,12 ÷ 1,08 ≈ 1,037)",
            "<i>“Em período de inflação, o deflator implícito do PIB é inferior a 100.”</i> → ERRADO (inversão: "
            "é superior a 100)",
        ])],
        "reescrita": ("Para não cometer o erro denominado “ilusão monetária”, o diplomata deve informar, em seu "
                      "relatório, o PIB real do país, em vez do nominal, dos últimos cinco anos. Para deflacionar "
                      "esses números, o diplomata deve utilizar o deflator (implícito) do PIB, que é calculado pelo "
                      "quociente entre o " + hl("PIB nominal e o PIB real, medido a preços constantes") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentários de professores (Jetro Coutinho, Celso Natale) e de alunos: o erro está na "
                             "definição do deflator, que é PIB nominal ÷ PIB real; um comentário especulava erro em "
                             "outro ponto (uso do termo ilusão monetária)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (283).png", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (fórmula do deflator absorvida no 📖)"}],
        "alertas": ["banca_confirmada: contexto do diplomata e ano 2016 batem com a prova objetiva do CACD 2016 "
                    "(CEBRASPE), conforme registros do item em bancos de questões; a fonte trazia só “(2016)”"],
    },
    # ------------------------------------------------------------------ E2-L00059
    {
        "id": "ECO-E2-L00059-1", "fonte_ref": "E2-L00059", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O produto interno bruto a preço de mercado incorpora o valor dos tributos indiretos e deduz "
                      "os subsídios pagos, refletindo assim o valor de mercado dos bens e serviços finais produzidos "
                      "dentro das fronteiras de um país em um período determinado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O produto interno bruto a preço de mercado <u>incorpora</u> o valor dos tributos indiretos e "
                      "<u>deduz</u> os subsídios pagos, refletindo assim o valor de mercado dos bens e serviços "
                      "finais produzidos dentro das fronteiras de um país em um período determinado."),
        "poucas": (vd("PIBpm = PIBcf + impostos indiretos − subsídios") + ". O preço que o comprador paga embute "
                   "os tributos e é rebaixado pelos subsídios; medir a " + azb("preços de mercado") + " é medir "
                   "por esse preço."),
        "destrinchando": [
            "O " + azb("custo de fatores") + " soma apenas o que remunera trabalho e capital. Entre ele e o preço "
            "final, o governo interfere duas vezes: " + azb("impostos indiretos") + " (ICMS, IPI, ISS, PIS/Cofins) "
            "encarecem; " + azb("subsídios") + " barateiam.",
            "Logo, para chegar ao preço de mercado: " + vd("+ impostos indiretos − subsídios") + ". Na volta "
            "(mercado → fatores), os sinais se invertem: − impostos + subsídios.",
            "Os demais qualificadores do item estão corretos: “bruto” (sem descontar depreciação), “interno” "
            "(critério territorial), “bens e serviços finais” (sem consumo intermediário, para evitar dupla "
            "contagem) e “período determinado” (é fluxo, não estoque).",
            "No SCN brasileiro, o PIB é publicado a preços de mercado: " + vd("PIB = VAB a preços básicos + "
            "impostos sobre produtos − subsídios sobre produtos") + ".",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definição de manual com dois verbos de sinal "
                       "(“incorpora” e “deduz”). A banca inverte justamente esses verbos na versão ERRADA; aqui "
                       "estão na ordem certa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB a preços de mercado deduz os tributos indiretos e incorpora os subsídios.”</i> → ERRADO "
            "(inversão: essa é a passagem para custo de fatores)",
            "<i>“Um aumento de subsídios, mantido o resto constante, reduz o PIB a preços de mercado sem alterar "
            "o PIB a custo de fatores.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O PIBpm reflete o valor dos bens e serviços finais produzidos no território, ajustado "
                             "por tributos indiretos e subsídios."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00060
    {
        "id": "ECO-E2-L00060-1", "fonte_ref": "E2-L00060", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Para converter o produto nacional em produto interno, é necessário subtrair a renda líquida "
                      "enviada ao exterior, ajustando assim a produção nacional àquela gerada exclusivamente dentro "
                      "das fronteiras do país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para converter o produto nacional em produto interno, é necessário ") + vm("subtrair")
                    + az(" a renda líquida enviada ao exterior, ajustando assim a produção nacional àquela gerada "
                         "exclusivamente dentro das fronteiras do país.")),
        "poucas": (vd("PI = PN + RLEE") + ". A renda enviada ao exterior foi gerada <b>aqui dentro</b> por fatores "
                   "estrangeiros: está no produto interno e não no nacional. Para ir de PN a PI, " + azb("soma-se")
                   + "."),
        "destrinchando": [
            "Partindo do " + azb("produto interno") + " (territorial): PN = PI + renda recebida do exterior − "
            "renda enviada ao exterior = " + vd("PI − RLEE") + ". Isolando: " + vd("PI = PN + RLEE") + ".",
            "Intuição: os lucros de uma montadora estrangeira no Brasil nascem no território (entram no PI), mas "
            "pertencem a não residentes (saem do PN). Para reconstruir o PI a partir do PN, é preciso devolver "
            "essa renda — somar.",
            "Teste rápido com números: PI = 100, renda enviada 8, recebida 3 → RLEE = 5 → PN = 95. Para voltar: "
            "95 + 5 = 100. Subtraindo, chegaria a 90, sem sentido.",
            "O " + rx("Brasil") + ", com RLEE historicamente positiva (remessas de lucros e juros), tem "
            + azb("RNB") + " menor que o PIB.",
            vm("Regra-âncora: PN → PI soma a RLEE; PI → PN subtrai."),
        ],
        "dissecando": (cz("[inversão]") + " Item de sinal: troca “somar” por “subtrair”. A segunda metade "
                       "(“exclusivamente dentro das fronteiras”) é a definição correta de produto interno e serve "
                       "de isca para quem lê só o final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para converter o produto interno em produto nacional, subtrai-se a renda líquida enviada ao "
            "exterior.”</i> → CERTO",
            "<i>“Se a renda líquida enviada ao exterior for negativa, o produto nacional supera o interno.”</i> → "
            "CERTO",
        ])],
        "reescrita": ("Para converter o produto nacional em produto interno, é necessário " + hl("somar")
                      + " a renda líquida enviada ao exterior, ajustando assim a produção nacional àquela gerada "
                      "exclusivamente dentro das fronteiras do país."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": ("Para converter PN em PI, adiciona-se (e não se subtrai) a renda líquida enviada ao "
                             "exterior, que é o rendimento de capitais estrangeiros no país."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00061
    {
        "id": "ECO-E2-L00061-1", "fonte_ref": "E2-L00061", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A renda disponível bruta de uma economia é composta exclusivamente pela sua renda nacional "
                      "bruta, desconsiderando as transferências unilaterais recebidas do exterior, que são "
                      "contabilizadas separadamente como entradas líquidas de capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A renda disponível bruta de uma economia é composta ")
                    + vm("exclusivamente pela sua renda nacional bruta, desconsiderando as transferências "
                         "unilaterais recebidas do exterior, que são contabilizadas separadamente como entradas "
                         "líquidas de capital") + az(".")),
        "poucas": (vd("RDB = RNB + transferências correntes líquidas do exterior") + ". As transferências "
                   "unilaterais correntes (remessas de emigrantes, doações) <b>entram</b> na " + azb("renda "
                   "disponível") + "; não são fluxo de capital."),
        "destrinchando": [
            "Escada dos agregados de renda: " + azb("PIB") + " + renda primária líquida do exterior = "
            + azb("RNB") + "; RNB + " + azb("transferências correntes líquidas") + " recebidas do exterior = "
            + azb("renda nacional disponível bruta") + "; RDB − consumo final = " + azb("poupança bruta") + ".",
            "Transferências unilaterais (sem contrapartida) se dividem em duas: as " + azb("correntes")
            + " (remessas de trabalhadores, ajuda humanitária, contribuições a organismos internacionais) afetam "
            "a renda disponível e vão para a conta de " + azb("renda secundária") + " do BP; as " + azb("de "
            "capital") + " (perdão de dívida, doação para construir um hospital) vão para a " + azb("conta "
            "capital") + " e não entram na renda disponível.",
            "Por isso o item erra duas vezes: o “exclusivamente” exclui as transferências correntes, e a "
            "classificação delas como “entradas líquidas de capital” confunde renda secundária com conta "
            "capital (ou com a conta financeira).",
            "Exemplo de peso: em países como " + azb("Honduras") + " ou " + azb("Nepal") + ", as remessas de "
            "emigrantes somam parcela grande do PIB, e a RDB fica visivelmente acima da RNB.",
        ],
        "dissecando": (cz("[restrição indevida · troca de conceito]") + " O “exclusivamente” corta da renda "
                       "disponível justamente o componente que a distingue da RNB; o resto da frase dá uma "
                       "justificativa plausível, mas falsa, tirada da confusão entre transferência corrente e "
                       "fluxo de capital."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O perdão de uma dívida externa pelo governo credor é registrado na conta capital do balanço de "
            "pagamentos.”</i> → CERTO",
            "<i>“As remessas de emigrantes a suas famílias no país de origem reduzem a renda disponível desse "
            "país.”</i> → ERRADO (inversão: aumentam)",
        ])],
        "reescrita": ("A renda disponível bruta de uma economia é composta " + hl("pela sua renda nacional bruta "
                      "acrescida das transferências unilaterais correntes líquidas recebidas do exterior, que não "
                      "são contabilizadas como entradas de capital") + "."),
        "tipo_erro": ["RESTRICAO", "TROCA_CONCEITO"], "moduladores": ["exclusivamente"], "dificuldade": 2,
        "comentario_fonte": ("A RDB inclui as transferências unilaterais, contabilizadas junto à RNB como parte da "
                             "renda disponível, e não separadamente como fluxos de capital."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00062
    {
        "id": "ECO-E2-L00062-1", "fonte_ref": "E2-L00062", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A renda disponível bruta do governo é composta apenas pelas receitas arrecadadas através de "
                      "impostos, sem considerar as transferências que o governo faz para famílias e empresas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A renda disponível bruta do governo é composta ")
                    + vm("apenas") + az(" pelas receitas arrecadadas através de impostos, ") + vm("sem considerar")
                    + az(" as transferências que o governo faz para famílias e empresas.")),
        "poucas": ("A " + azb("renda disponível bruta do governo") + " é o que lhe resta <b>depois</b> da "
                   "redistribuição: impostos, contribuições sociais e rendas de propriedade, " + vd("menos") + " "
                   "benefícios sociais, subsídios e demais transferências pagas."),
        "destrinchando": [
            "Fórmula de qualquer setor institucional: " + vd("RDB = saldo da renda primária bruta + "
            "transferências correntes recebidas − transferências correntes pagas") + ".",
            "Para o governo: a renda primária inclui os impostos sobre a produção e a importação (líquidos de "
            "subsídios) e as rendas de propriedade (juros, dividendos de estatais, royalties); na distribuição "
            "secundária entram impostos sobre renda e patrimônio e " + azb("contribuições sociais") + ", e saem "
            + azb("benefícios sociais") + " (aposentadorias, seguro-desemprego, Bolsa Família) e outras "
            "transferências correntes.",
            "Erros do item: (1) “apenas impostos” — esquece contribuições e rendas de propriedade; (2) “sem "
            "considerar as transferências” — elas são exatamente o que transforma a renda primária em renda "
            "<b>disponível</b>. Sem deduzi-las, o mesmo dinheiro contaria duas vezes: com o governo e com a "
            "família que recebeu o benefício.",
            "Uso da renda: " + vd("poupança bruta do governo = RDB − consumo final do governo") + ". No "
            + rx("Brasil") + ", o peso das transferências previdenciárias e assistenciais faz essa poupança ser "
            "frequentemente negativa.",
            "Não confundir com " + azb("receita pública") + " (contabilidade orçamentária, que inclui até "
            "operações de crédito): renda disponível é conceito das Contas Nacionais.",
        ],
        "dissecando": (cz("[restrição indevida · meia-verdade]") + " Impostos de fato compõem a renda do governo "
                       "(parte verdadeira); o “apenas” e o “sem considerar” apagam o que define o conceito de "
                       "renda disponível. Pista: o adjetivo “disponível” sempre pressupõe a etapa de "
                       "transferências."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O pagamento de aposentadorias pelo governo reduz sua renda disponível bruta, mas não o PIB.”</i> "
            "→ CERTO",
            "<i>“Os benefícios sociais pagos pelo governo integram a despesa de consumo final do governo.”</i> → "
            "ERRADO (troca de conceito: são transferências, não consumo)",
        ])],
        "reescrita": ("A renda disponível bruta do governo é composta <s>apenas</s> pelas receitas arrecadadas "
                      "através de impostos, " + hl("contribuições e demais rendas que recebe, deduzidas")
                      + " as transferências que o governo faz para famílias e empresas."),
        "tipo_erro": ["RESTRICAO", "MEIA_VERDADE"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Várias respostas de IA fundidas: RDB do governo = receitas − transferências e "
                             "subsídios; RDB = saldo da renda primária + transferências correntes líquidas; códigos "
                             "SCN (B.5, B.6, D.61, D.62, D.7); poupança do governo = RDB − consumo final."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 004", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00294
    {
        "id": "ECO-E2-L00294-1", "fonte_ref": "E2-L00294", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A partir das identidades das Contas Nacionais em uma economia aberta, sabe-se que "
                      "(S − I) + (T − G) = (X − M). Portanto, ceteris paribus, um aumento do déficit público "
                      "(redução de T − G) deve ser compensado por um aumento da poupança privada líquida ou por um "
                      "aumento do déficit em transações correntes (entrada de poupança externa)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A partir das identidades das Contas Nacionais em uma economia aberta, sabe-se que "
                      "(S − I) + (T − G) = (X − M). Portanto, ceteris paribus, um aumento do déficit público "
                      "(redução de T − G) <u>deve ser compensado</u> por um aumento da poupança privada líquida "
                      "<u>ou</u> por um aumento do déficit em transações correntes (entrada de poupança externa)."),
        "poucas": ("É aritmética da " + azb("identidade dos três hiatos") + ": se (T − G) cai, a igualdade só se "
                   "mantém se (S − I) subir, (X − M) cair, ou uma combinação dos dois."),
        "destrinchando": [
            "De onde vem a identidade: Y = C + I + G + (X − M) e Y = C + S + T (renda usada em consumo, poupança "
            "privada e impostos líquidos). Igualando: " + vd("(S − I) + (T − G) = (X − M)") + " — saldo privado "
            "+ saldo público = saldo externo.",
            "Leitura de financiamento: o investimento é financiado por poupança privada, poupança pública "
            "(T − G) e " + azb("poupança externa") + " (M − X, isto é, déficit em transações correntes): "
            + vd("I = S + (T − G) + (M − X)") + ".",
            "Se o governo amplia o déficit e I não muda, alguém precisa cobrir o buraco: o setor privado poupa "
            "mais (no limite, a " + azb("equivalência ricardiana") + " de " + oc("Barro") + " prevê compensação "
            "integral) ou o país absorve poupança do exterior — base da tese dos " + azb("déficits gêmeos")
            + ". O “ceteris paribus” fixa o investimento; sem ele, uma terceira via seria a queda de I "
            "(" + azb("crowding out") + ").",
            "Nota técnica: em rigor, o lado externo é o saldo em transações correntes (X − M inclui aqui "
            "serviços e rendas); a forma simplificada do item é a usual em prova.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O item usa a identidade corretamente: o "
                       "“ou” admite qualquer combinação e o “ceteris paribus” trava o investimento. Não afirma "
                       "<b>causalidade</b> nem diz qual via ocorrerá — só que a soma tem de fechar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…um aumento do déficit público necessariamente provoca aumento equivalente do déficit em "
            "transações correntes.”</i> → ERRADO (modulador absoluto: a identidade não fixa a via de ajuste)",
            "<i>“Mantidos o investimento e a poupança privada, maior déficit público implica maior déficit "
            "externo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["ceteris paribus", "ou"],
        "dificuldade": 1,
        "comentario_fonte": ("Equilíbrio de fundos: o investimento é financiado por poupança nacional (privada + "
                             "pública) ou externa; se a poupança pública cai, é preciso mais poupança privada ou "
                             "externa (déficit em transações correntes); base da tese dos déficits gêmeos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00424-1 (mesma identidade, cobrando a ausência de causalidade)"],
    },
    # ------------------------------------------------------------------ E2-L00398
    {
        "id": "ECO-E2-L00398-1", "fonte_ref": "E2-L00398", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("No Sistema de Contas Nacionais, os gastos com pesquisa e desenvolvimento (P&D) e a aquisição "
                      "de sistemas de armamentos deixaram de ser registrados como consumo intermediário e passaram a "
                      "compor a Formação Bruta de Capital Fixo (FBCF), o que gerou um impacto positivo no nível do "
                      "Produto Interno Bruto (PIB) quando da mudança metodológica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No Sistema de Contas Nacionais, os gastos com pesquisa e desenvolvimento (P&D) e a aquisição "
                      "de sistemas de armamentos deixaram de ser registrados como consumo intermediário e passaram a "
                      "compor a Formação Bruta de Capital Fixo (FBCF), o que gerou um <u>impacto positivo no nível "
                      "do Produto Interno Bruto</u> (PIB) quando da mudança metodológica."),
        "poucas": ("O " + azb("SCN 2008") + " ampliou a fronteira dos ativos: P&D e armamentos duráveis viraram "
                   + azb("FBCF") + ". O que era insumo (subtraído do valor adicionado) passou a ser demanda final, "
                   "e o nível do PIB subiu."),
        "destrinchando": [
            "Critério do SCN: é ativo fixo o que presta serviços à produção por <b>mais de um ano</b>. O "
            "conhecimento gerado por P&D e um navio de guerra ou caça (que presta serviço de defesa por décadas) "
            "passam no teste; por isso entraram na FBCF. P&D compõe os " + azb("produtos de propriedade "
            "intelectual") + ", ao lado de software e exploração mineral.",
            "Armamentos de uso único (munição, bombas, mísseis descartáveis) <b>não</b> viram capital fixo: "
            "ficam como estoques militares.",
            "Por que o PIB sobe: na ótica da produção, " + vd("VAB = produção − consumo intermediário") + "; "
            "tirar um gasto do consumo intermediário eleva o VAB. Na ótica da despesa, ele passa a somar como "
            "investimento. No governo, o efeito líquido é o surgimento do consumo de capital fixo desses ativos "
            "no valor da produção não mercantil.",
            "É efeito de <b>mensuração</b>, não de atividade: os gastos já existiam. No " + rx("Brasil") + ", o "
            "IBGE incorporou o SCN 2008 na " + vd("série referência 2010") + ", divulgada em " + vd("2015")
            + ", que elevou o nível do PIB e da FBCF — a capitalização de P&D foi uma das mudanças.",
            "Outra novidade correlata do SCN 2008: os " + azb("SIFIM") + " passam a ser alocados aos setores "
            "usuários.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item de atualização metodológica: quem estudou só a "
                       "versão antiga (P&D como despesa) marca ERRADO. O efeito sobre o PIB é a consequência "
                       "lógica da reclassificação: saiu do consumo intermediário, entrou na demanda final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A reclassificação de P&D como investimento elevou a taxa de crescimento real da economia no "
            "ano da mudança.”</i> → ERRADO (troca de conceito: muda o nível medido, não a atividade; as séries "
            "são retropoladas)",
            "<i>“No SCN 2008, a compra de munições pelas Forças Armadas é registrada como FBCF.”</i> → ERRADO "
            "(modulador absoluto: só armamentos duráveis)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Várias respostas de IA: SCN 2008 (IBGE, referência 2010) capitalizou P&D e "
                             "armamentos duráveis como FBCF; sai do consumo intermediário, eleva VAB e PIB; munição "
                             "de uso único fica em estoques; revisão do IBGE elevou o PIB de 2010 em cerca de 3%."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 053", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 054", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00399
    {
        "id": "ECO-E2-L00399-1", "fonte_ref": "E2-L00399", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Na Matriz de Insumo-Produto, os coeficientes técnicos diretos são obtidos pela divisão do "
                      "valor de cada insumo adquirido por um setor pelo valor total da produção desse mesmo setor. "
                      "Sendo assim, a matriz de Leontief, calculada a partir desses coeficientes, permite captar "
                      "exclusivamente os efeitos diretos que uma variação na demanda final de determinado setor causa "
                      "na produção dos demais setores da economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na Matriz de Insumo-Produto, os coeficientes técnicos diretos são obtidos pela divisão do "
                       "valor de cada insumo adquirido por um setor pelo valor total da produção desse mesmo setor. "
                       "Sendo assim, a matriz de Leontief, calculada a partir desses coeficientes, permite captar ")
                    + vm("exclusivamente os efeitos diretos")
                    + az(" que uma variação na demanda final de determinado setor causa na produção dos demais "
                         "setores da economia.")),
        "poucas": ("A matriz A de coeficientes técnicos mede efeitos <b>diretos</b>; a " + azb("inversa de "
                   "Leontief") + " " + vd("(I − A)⁻¹") + " capta efeitos " + azb("diretos e indiretos") + " ao "
                   "longo de toda a cadeia."),
        "destrinchando": [
            "Coeficiente técnico " + vd("a<sub>ij</sub> = z<sub>ij</sub> / x<sub>j</sub>") + ": quanto do setor i "
            "o setor j compra para produzir R$ 1. A primeira frase do item está correta.",
            "Modelo de " + oc("Wassily Leontief") + " (Nobel de " + vd("1973") + "): produção = consumo "
            "intermediário + demanda final → " + vd("x = Ax + y") + " → " + vd("x = (I − A)⁻¹ y") + ".",
            "Por que “indiretos”: para atender mais carros (efeito direto), a montadora compra aço; a siderúrgica "
            "compra minério e energia; a mineradora compra máquinas… A inversa soma a série infinita "
            + vd("I + A + A² + A³ + …") + ": I é o próprio choque, A o 1º round de insumos, A² o 2º, e assim por "
            "diante.",
            "Daí os " + azb("multiplicadores de produção") + " (soma das colunas da inversa) e os "
            + azb("índices de ligação") + " de Rasmussen-Hirschman, usados para identificar setores-chave. "
            "Incluindo as famílias na matriz (modelo fechado), captam-se também efeitos <b>induzidos</b> pela "
            "renda.",
            "No " + rx("Brasil") + ", o IBGE publica as Matrizes de Insumo-Produto a partir das Tabelas de "
            "Recursos e Usos do SCN.",
        ],
        "dissecando": (cz("[restrição indevida · troca de conceito]") + " Primeira frase correta; o erro está no "
                       "“exclusivamente”, que atribui à inversa de Leontief a limitação da matriz A. Pista: se a "
                       "matriz de Leontief só repetisse os efeitos diretos, não haveria motivo para invertê-la."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A matriz de coeficientes técnicos diretos, isoladamente, capta apenas os efeitos de primeira "
            "ordem de uma variação na demanda final.”</i> → CERTO",
            "<i>“Os multiplicadores de produção derivados da inversa de Leontief são sempre menores que 1.”</i> "
            "→ ERRADO (inversão: são maiores ou iguais a 1)",
        ])],
        "reescrita": ("Na Matriz de Insumo-Produto, os coeficientes técnicos diretos são obtidos pela divisão do "
                      "valor de cada insumo adquirido por um setor pelo valor total da produção desse mesmo setor. "
                      "Sendo assim, a matriz de Leontief, calculada a partir desses coeficientes, permite captar "
                      + hl("os efeitos diretos e indiretos") + " que uma variação na demanda final de determinado "
                      "setor causa na produção dos demais setores da economia."),
        "tipo_erro": ["RESTRICAO", "TROCA_CONCEITO"], "moduladores": ["exclusivamente"], "dificuldade": 2,
        "comentario_fonte": ("A primeira parte está correta (matriz A); a inversa de Leontief capta efeitos diretos "
                             "e indiretos sobre toda a cadeia produtiva."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00400
    {
        "id": "ECO-E2-L00400-1", "fonte_ref": "E2-L00400", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Sob a ótica da renda, o PIB é obtido pela soma da Remuneração dos Empregados, do Rendimento "
                      "Misto Bruto, do Excedente Operacional Bruto e dos impostos líquidos de subsídios sobre a "
                      "produção e a importação. O Rendimento Misto Bruto diferencia-se do Excedente Operacional "
                      "Bruto por contabilizar as rendas das empresas não constituídas em sociedade (como "
                      "autônomos), não sendo possível separar contabilisticamente a remuneração do trabalho da "
                      "remuneração do capital nesse componente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sob a ótica da renda, o PIB é obtido pela soma da Remuneração dos Empregados, do Rendimento "
                      "Misto Bruto, do Excedente Operacional Bruto e dos impostos líquidos de subsídios sobre a "
                      "produção e a importação. O Rendimento Misto Bruto diferencia-se do Excedente Operacional "
                      "Bruto por contabilizar as rendas das <u>empresas não constituídas em sociedade</u> (como "
                      "autônomos), <u>não sendo possível separar</u> contabilisticamente a remuneração do trabalho "
                      "da remuneração do capital nesse componente."),
        "poucas": (vd("PIB = RE + RMB + EOB + (impostos − subsídios sobre a produção e a importação)") + ". O "
                   + azb("rendimento misto") + " é a renda do autônomo, que remunera ao mesmo tempo seu trabalho e "
                   "seu capital, sem como separar."),
        "destrinchando": [
            "A ótica da renda pergunta <b>quem se apropriou</b> do valor adicionado: o trabalho assalariado, os "
            "donos do capital, os autônomos e o governo.",
            azb("Remuneração dos empregados (RE)") + ": salários brutos + contribuições sociais dos "
            "empregadores (INSS patronal, FGTS). " + azb("Excedente operacional bruto (EOB)") + ": o que sobra às "
            "empresas constituídas em sociedade (S.A., Ltda.) depois de pagar empregados e impostos — lucros, "
            "juros, aluguéis, antes da depreciação; inclui o aluguel imputado de imóveis próprios.",
            azb("Rendimento misto bruto (RMB)") + ": renda das famílias produtoras — encanador, médico ou "
            "motorista por conta própria, pequeno comércio sem constituição societária. O dono não paga salário "
            "a si mesmo nem apura lucro separado: o rendimento é “misto” de trabalho e capital.",
            "Impostos: aqui entram <b>todos</b> os impostos sobre a produção e a importação (sobre produtos — "
            "ICMS, IPI, II — e outros sobre a produção — IPTU de empresas, taxas), líquidos dos subsídios. "
            "Impostos sobre a renda (IR) não entram: já estão dentro de RE, EOB e RMB.",
            "Uso analítico: a participação da RE no PIB mede a " + azb("distribuição funcional da renda")
            + "; quando o emprego formal cai e cresce o trabalho por conta própria, renda migra de RE para RMB.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Fórmula de manual mais o critério que separa RMB de "
                       "EOB: a forma jurídica (sociedade ou não) e a impossibilidade de separar trabalho e "
                       "capital. O advérbio “contabilisticamente” é um aportuguesamento europeu, não um erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O lucro de uma sociedade anônima de capital aberto integra o rendimento misto bruto.”</i> → "
            "ERRADO (troca de conceito: é EOB)",
            "<i>“As contribuições previdenciárias patronais integram a remuneração dos empregados.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Várias respostas de IA: PIB = RE + RMB + EOB + impostos líquidos de subsídios; RMB "
                             "agrupa a renda de autônomos e pequenos proprietários, mistura de trabalho e capital; "
                             "EOB é retorno ao capital de empresas constituídas; dados aproximados de participação no "
                             "PIB brasileiro sem fonte precisa (não aproveitados)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 055", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 056", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 057", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (era só texto: ILSI = impostos − subsídios, absorvido)"},
                          {"ref": "IMAGEM 058", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 059", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00444-1 (mesma fórmula da ótica da renda, outra fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00401
    {
        "id": "ECO-E2-L00401-1", "fonte_ref": "E2-L00401", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Se a Renda Líquida de Fatores Enviada ao Exterior (RLFEE) for positiva, o Produto Interno "
                      "Bruto a preços de mercado será necessariamente menor que o Produto Nacional Bruto a preços de "
                      "mercado, indicando que o país paga mais rendimentos de fatores ao resto do mundo do que "
                      "recebe."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se a Renda Líquida de Fatores Enviada ao Exterior (RLFEE) for positiva, o Produto Interno "
                       "Bruto a preços de mercado será necessariamente ") + vm("menor")
                    + az(" que o Produto Nacional Bruto a preços de mercado, indicando que o país paga mais "
                         "rendimentos de fatores ao resto do mundo do que recebe.")),
        "poucas": (vd("PNB = PIB − RLFEE") + ". Com RLFEE > 0, o PNB é que fica menor: o " + azb("PIB") + " é "
                   "<b>maior</b> que o PNB. A interpretação do final do item está certa; a desigualdade está "
                   "invertida."),
        "destrinchando": [
            azb("RLFEE") + " = renda de fatores enviada − renda de fatores recebida do exterior (lucros, "
            "dividendos, juros, salários). Positiva = o país paga mais do que recebe.",
            "O PIB conta tudo o que se produz no território; o PNB tira a renda que pertence a não residentes e "
            "acrescenta a que residentes ganham fora: " + vd("PNB = PIB + recebida − enviada = PIB − RLFEE")
            + ".",
            "Logo: " + vd("RLFEE > 0 ⇒ PIB > PNB") + "; " + vd("RLFEE < 0 ⇒ PNB > PIB") + ". Países com grande "
            "estoque de investimento estrangeiro e dívida externa — como o " + rx("Brasil") + " — tendem ao "
            "primeiro caso; países credores ou sede de multinacionais, ao segundo.",
            "Exemplo clássico de distância extrema: a " + azb("Irlanda") + ", sede de lucros de multinacionais, "
            "tem PIB muito acima da renda nacional — por isso o país criou um indicador próprio de renda "
            "nacional modificada.",
            vm("Regra-âncora: enviou mais renda do que recebeu → o nacional é o menor."),
        ],
        "dissecando": (cz("[inversão]") + " A troca de “maior” por “menor” é escondida entre um “necessariamente” "
                       "(que, no sentido correto, seria verdadeiro) e uma explicação final correta, que dá ao item "
                       "aparência de coerência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a RLFEE for negativa, o PNB superará o PIB.”</i> → CERTO",
            "<i>“Se a RLFEE for positiva, a renda nacional bruta superará o PIB.”</i> → ERRADO (inversão: será "
            "menor)",
        ])],
        "reescrita": ("Se a Renda Líquida de Fatores Enviada ao Exterior (RLFEE) for positiva, o Produto Interno "
                      "Bruto a preços de mercado será necessariamente " + hl("maior") + " que o Produto Nacional "
                      "Bruto a preços de mercado, indicando que o país paga mais rendimentos de fatores ao resto do "
                      "mundo do que recebe."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": ("PNB = PIB − RLFEE; com RLFEE positiva, o PNB é menor que o PIB, e não o contrário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0844-1 (mesma relação PI × PN, versão CERTO de outra fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00403
    {
        "id": "ECO-E2-L00403-1", "fonte_ref": "E2-L00403", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Na transição do Valor Adicionado Bruto (VAB) a preços básicos para o Produto Interno Bruto "
                      "(PIB) a preços de mercado, é necessária a adição de todos os impostos incidentes sobre a "
                      "produção, líquidos de subsídios."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na transição do Valor Adicionado Bruto (VAB) a preços básicos para o Produto Interno Bruto "
                       "(PIB) a preços de mercado, é necessária a adição ")
                    + vm("de todos os impostos incidentes sobre a produção") + az(", líquidos de subsídios.")),
        "poucas": (vd("PIBpm = VABpb + impostos sobre produtos − subsídios sobre produtos") + ". Os "
                   + azb("outros impostos sobre a produção") + " (IPTU da fábrica, taxas) já estão dentro do VAB "
                   "a preços básicos."),
        "destrinchando": [
            "O SCN separa dois grupos de impostos ligados à produção: " + azb("impostos sobre produtos")
            + " — incidem por unidade vendida ou transacionada (ICMS, IPI, ISS, PIS/Cofins, imposto de "
            "importação) — e " + azb("outros impostos sobre a produção") + " — incidem pelo simples fato de "
            "produzir, independentemente do volume (IPTU de imóvel produtivo, IPVA de frota comercial, taxas e "
            "licenças).",
            azb("Preço básico") + " = o que o produtor recebe por unidade, <b>sem</b> impostos sobre produtos e "
            "<b>com</b> subsídios sobre produtos. Os outros impostos sobre a produção são custo do produtor e já "
            "estão embutidos no preço básico, logo no VAB a preços básicos.",
            azb("Preço de mercado") + " = preço básico + impostos sobre produtos − subsídios sobre produtos. Por "
            "isso, na passagem VABpb → PIBpm, só entram os impostos líquidos sobre <b>produtos</b>; somar também "
            "os outros impostos seria dupla contagem.",
            "Contraste útil: na ótica da <b>renda</b>, o PIB soma os impostos sobre a produção e a importação "
            "<b>todos</b> (produtos + outros), porque ali o VAB foi desmontado em RE, EOB e RMB e os outros "
            "impostos precisam reaparecer.",
            vm("Regra-âncora: VABpb → PIBpm = + impostos sobre produtos − subsídios sobre produtos."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O “todos” amplia o ajuste de impostos "
                       "sobre <b>produtos</b> para impostos sobre a <b>produção</b>. A diferença é de uma palavra e "
                       "é exatamente o que a banca testa nesse par de conceitos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O IPTU pago por uma indústria sobre seu galpão integra o valor adicionado bruto a preços "
            "básicos.”</i> → CERTO",
            "<i>“Pela ótica da renda, o PIB soma apenas os impostos sobre produtos, líquidos de subsídios.”</i> → "
            "ERRADO (restrição indevida: entram todos os impostos sobre a produção e a importação)",
        ])],
        "reescrita": ("Na transição do Valor Adicionado Bruto (VAB) a preços básicos para o Produto Interno Bruto "
                      "(PIB) a preços de mercado, é necessária a adição " + hl("dos impostos sobre produtos") + ", líquidos de subsídios"
                      + hl(" sobre produtos") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["todos"], "dificuldade": 2,
        "comentario_fonte": ("Várias respostas de IA: só os impostos sobre produtos (líquidos de subsídios sobre "
                             "produtos) entram na passagem; outros impostos sobre a produção já estão no VAB a "
                             "preços básicos; uma delas incluía o INSS patronal entre os outros impostos sobre a "
                             "produção (é remuneração dos empregados)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 060", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (era tabela de tipos de imposto; absorvida no 📖)"},
                          {"ref": "IMAGEM 061", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 062", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (texto absorvido no 📖)"},
                          {"ref": "IMAGEM 063", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conceitos de preço absorvidos no 📖)"},
                          {"ref": "IMAGEM 064", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (exemplo numérico com erro de classificação)"}],
        "alertas": ["qualidade_fonte: um dos comentários tratava o INSS patronal como outro imposto sobre a "
                    "produção; contribuição patronal integra a remuneração dos empregados — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L00404
    {
        "id": "ECO-E2-L00404-1", "fonte_ref": "E2-L00404", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("O deflator implícito do PIB é um índice de preços que reflete a variação de preços de todos "
                      "os bens e serviços produzidos internamente. Na contabilidade nacional, ele equivale "
                      "formalmente a um índice de Paasche, uma vez que utiliza as quantidades do período corrente "
                      "como fatores de ponderação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O deflator implícito do PIB é um índice de preços que reflete a variação de preços de todos "
                      "os bens e serviços produzidos internamente. Na contabilidade nacional, ele equivale "
                      "formalmente a um índice de <u>Paasche</u>, uma vez que utiliza as quantidades do <u>período "
                      "corrente</u> como fatores de ponderação."),
        "poucas": ("Deflator = " + vd("Σp<sub>t</sub>q<sub>t</sub> / Σp<sub>0</sub>q<sub>t</sub>") + ": preços "
                   "variam, quantidades ficam as do " + azb("ano corrente") + " — a definição do " + azb("índice "
                   "de Paasche") + "."),
        "destrinchando": [
            azb("Laspeyres") + ": pondera pelas quantidades do <b>ano-base</b> — " + vd("Σp<sub>t</sub>q<sub>0"
            "</sub> / Σp<sub>0</sub>q<sub>0</sub>") + ". É a forma dos índices ao consumidor (IPCA, INPC), "
            "que fixam uma cesta da pesquisa de orçamentos familiares.",
            azb("Paasche") + ": pondera pelas quantidades do <b>período corrente</b> — " + vd("Σp<sub>t</sub>"
            "q<sub>t</sub> / Σp<sub>0</sub>q<sub>t</sub>") + ". É exatamente PIB nominal (numerador) sobre PIB "
            "real a preços do ano-base (denominador).",
            "Viés de substituição: os consumidores trocam bens que encareceram por outros. Laspeyres, com a cesta "
            "antiga, tende a <b>superestimar</b> a inflação; Paasche, com a cesta nova, tende a "
            "<b>subestimar</b>. O índice de " + oc("Fisher") + " (média geométrica dos dois) é o “ideal”.",
            "Diferenças com o IPCA: o deflator inclui bens de capital, gastos do governo e exportações, e exclui "
            "importados; o IPCA só mede a cesta do consumidor, inclusive importados.",
            "Na prática, o IBGE calcula o PIB real com encadeamento anual (preços do ano anterior), mas a lógica "
            "do deflator implícito continua a de Paasche.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item conceitual de números-índice: a armadilha seria "
                       "trocar Paasche por Laspeyres. A justificativa dada (quantidades correntes como peso) é a "
                       "própria definição de Paasche, o que confirma o gabarito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O deflator implícito do PIB é um índice de Laspeyres, pois fixa as quantidades do ano-base.”</i> "
            "→ ERRADO (troca de conceito)",
            "<i>“Por ignorar a substituição entre bens, o índice de Laspeyres tende a superestimar a variação do "
            "custo de vida.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Deflator = PIB nominal / PIB real, índice de Paasche (quantidades correntes como "
                             "pesos); Paasche tende a subestimar a inflação pela substituição."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00405
    {
        "id": "ECO-E2-L00405-1", "fonte_ref": "E2-L00405", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A Renda Nacional Bruta Disponível (RNBD) representa o montante de recursos de que a nação "
                      "dispõe para consumo final ou poupança, sendo obtida pela soma do Produto Nacional Bruto com as "
                      "transferências unilaterais correntes (renda secundária) líquidas recebidas do resto do mundo. "
                      "Diante das identidades contábeis, caso a economia apresente déficit em transações correntes, a "
                      "Poupança Nacional Bruta será inferior à Formação Bruta de Capital da economia (Investimento "
                      "total)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Renda Nacional Bruta Disponível (RNBD) representa o montante de recursos de que a nação "
                      "dispõe para consumo final ou poupança, sendo obtida pela soma do Produto Nacional Bruto com "
                      "as transferências unilaterais correntes (renda secundária) líquidas recebidas do resto do "
                      "mundo. Diante das identidades contábeis, caso a economia apresente <u>déficit em transações "
                      "correntes</u>, a Poupança Nacional Bruta será <u>inferior</u> à Formação Bruta de Capital da "
                      "economia (Investimento total)."),
        "poucas": (vd("STC = S<sub>nacional</sub> − I") + ". Déficit em transações correntes ⇔ poupança nacional "
                   "< investimento: a diferença é a " + azb("poupança externa") + "."),
        "destrinchando": [
            "Escada: PIB + renda primária líquida do exterior = " + azb("RNB (PNB)") + "; RNB + transferências "
            "correntes líquidas (renda secundária) = " + azb("RNBD") + "; RNBD − consumo final = " + azb("poupança "
            "nacional bruta") + ".",
            "Como a RNBD soma PIB, renda primária e renda secundária, e o PIB = C + I + (X − M), segue: "
            + vd("S − I = (X − M) + renda primária + renda secundária = saldo em transações correntes") + ".",
            "Logo: STC < 0 (déficit) ⇒ " + vd("S < I") + ". O investimento é financiado em parte por "
            + azb("poupança externa") + " = −STC, que entra pela conta financeira do BP.",
            "O " + rx("Brasil") + " convive com déficits em transações correntes há décadas: a taxa de "
            "investimento fica acima da taxa de poupança doméstica, e a diferença é coberta por investimento "
            "estrangeiro direto e outros fluxos.",
            "Detalhe de rigor: “investimento” aqui é a formação bruta de capital (FBCF + variação de estoques); "
            "a identidade completa também desconta as transferências de capital (conta capital), em geral "
            "pequenas.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Duas afirmações certas encadeadas: a definição de RNBD "
                       "e a identidade S − I = STC. O item é longo para cansar; a única verificação necessária é o "
                       "sinal: déficit externo = poupança nacional insuficiente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Superávit em transações correntes indica que o país absorve poupança externa.”</i> → ERRADO "
            "(inversão: o país exporta poupança)",
            "<i>“A RNBD é obtida somando ao PNB as transferências unilaterais de capital recebidas do exterior.”</i> "
            "→ ERRADO (troca de conceito: correntes, não de capital)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Definição de RNBD correta; investimento = poupança nacional + poupança externa; "
                             "déficit em transações correntes = poupança externa positiva ⇒ poupança nacional < "
                             "investimento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00406
    {
        "id": "ECO-E2-L00406-1", "fonte_ref": "E2-L00406", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Nas contas nacionais, o pagamento de juros da dívida pública pelo governo é classificado como "
                      "despesa de consumo final da administração pública, o que eleva a demanda agregada e impacta "
                      "diretamente e de forma positiva o cálculo do PIB pela ótica da despesa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nas contas nacionais, o pagamento de juros da dívida pública pelo governo é classificado "
                       "como ")
                    + vm("despesa de consumo final da administração pública, o que eleva a demanda agregada e "
                         "impacta diretamente e de forma positiva o cálculo do PIB pela ótica da despesa")
                    + az(".")),
        "poucas": ("Juros são " + azb("renda de propriedade") + " — remuneração do capital emprestado, registrada "
                   "na distribuição da renda. Não compram bem nem serviço: não são consumo do governo e não entram "
                   "no PIB pela ótica da despesa."),
        "destrinchando": [
            "O " + azb("consumo final do governo") + " (G) mede o valor dos serviços não mercantis que a "
            "administração pública presta à coletividade — saúde, educação, segurança —, avaliados pelo custo: "
            "salários dos servidores, compras de bens e serviços, depreciação.",
            "Ficam fora de G todos os pagamentos sem contrapartida em produção corrente: " + azb("juros")
            + " (renda de propriedade, conta de alocação da renda primária), " + azb("benefícios sociais")
            + " e demais " + azb("transferências") + " (distribuição secundária), subsídios.",
            "Por isso a despesa do orçamento público não coincide com G: a maior parte do gasto da União é "
            "previdência, transferências e juros. Os juros aparecem no " + azb("resultado nominal") + " (NFSP), "
            "não no PIB.",
            "Efeito indireto existe — quem recebe os juros pode consumir mais —, mas aí o registro é no consumo "
            "das famílias, e não “diretamente” como G.",
            vm("Regra-âncora: só entra no PIB pela despesa o gasto que compra produção corrente; juros e "
               "transferências redistribuem renda."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item reclassifica juros (renda de "
                       "propriedade) como consumo e, sobre o erro, constrói um efeito “direto e positivo” no PIB. "
                       "🔥 A banca costuma testar a fronteira de G com juros, aposentadorias e Bolsa Família."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O pagamento de salários aos professores da rede pública integra o consumo final do "
            "governo.”</i> → CERTO",
            "<i>“O aumento das aposentadorias pagas pelo INSS eleva diretamente o consumo final do governo.”</i> "
            "→ ERRADO (troca de conceito: é transferência)",
        ])],
        "reescrita": ("Nas contas nacionais, o pagamento de juros da dívida pública pelo governo é classificado como "
                      + hl("renda de propriedade, na distribuição da renda, e por isso não integra o consumo final "
                           "da administração pública nem o cálculo do PIB pela ótica da despesa") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["diretamente"], "dificuldade": 1,
        "comentario_fonte": ("Juros não são consumo final; são renda de propriedade (distribuição primária); o "
                             "consumo do governo mede serviços à coletividade, sem despesas financeiras."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00407
    {
        "id": "ECO-E2-L00407-1", "fonte_ref": "E2-L00407", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("No atual Sistema de Contas Nacionais, os Serviços de Intermediação Financeira Indiretamente "
                      "Medidos (SIFIM) são alocados integralmente como consumo intermediário de um “setor "
                      "institucional fictício” (dummy), de modo que o lucro advindo do spread bancário não altere o "
                      "nível global do Produto Interno Bruto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No atual Sistema de Contas Nacionais, os Serviços de Intermediação Financeira Indiretamente "
                       "Medidos (SIFIM) são alocados ")
                    + vm("integralmente como consumo intermediário de um “setor institucional fictício” (dummy), de "
                         "modo que o lucro advindo do spread bancário não altere o nível global do Produto Interno "
                         "Bruto") + az(".")),
        "poucas": ("O setor " + azb("dummy") + " é coisa das séries antigas. No SCN 2008 (no Brasil, série "
                   "referência 2010), os " + azb("SIFIM") + " são alocados aos usuários: consumo intermediário das "
                   "empresas, mas demanda final das famílias, do governo e do exterior — e essa parte eleva o PIB."),
        "destrinchando": [
            "Bancos cobram parte de seus serviços sem tarifa explícita, via " + azb("spread") + " (juros "
            "cobrados − juros pagos, em relação a uma taxa de referência). Esse serviço implícito é o SIFIM.",
            "Problema contábil: quem consome o serviço? Nas séries antigas, sem resposta, lançava-se todo o SIFIM "
            "como consumo intermediário de um setor fictício com produção nula — o " + azb("dummy financeiro")
            + " —, cujo valor adicionado negativo anulava o do setor financeiro na parcela imputada.",
            "No SCN 2008, o SIFIM é " + azb("repartido entre os usuários") + ": a parte usada por empresas "
            "entra como consumo intermediário (não altera o PIB, só redistribui valor adicionado entre setores); "
            "a parte usada por famílias (como consumidoras) e por não residentes vira " + vd("consumo final e "
            "exportação") + ", elevando o PIB. No governo, o SIFIM entra no custo da produção não mercantil e, "
            "por isso, também no consumo final do governo.",
            "O mesmo movimento de modernização trouxe a capitalização de P&D e de armamentos duráveis na FBCF.",
        ],
        "dissecando": (cz("[anacronismo · modulador absoluto]") + " O item apresenta como “atual” o tratamento "
                       "antigo (dummy) e reforça com “integralmente”. Pista: “No atual” + prática que só existia "
                       "porque não se sabia alocar o serviço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A alocação do SIFIM às famílias, como consumo final, eleva o nível do PIB em relação ao "
            "tratamento com setor fictício.”</i> → CERTO",
            "<i>“No SCN 2008, o SIFIM consumido pelas empresas é registrado como formação bruta de capital "
            "fixo.”</i> → ERRADO (troca de conceito: é consumo intermediário)",
        ])],
        "reescrita": ("No atual Sistema de Contas Nacionais, os Serviços de Intermediação Financeira Indiretamente "
                      "Medidos (SIFIM) são alocados " + hl("aos setores usuários — como consumo intermediário das "
                      "empresas e como demanda final dos demais usuários —, de modo que a parcela destinada "
                      "à demanda final eleva o nível global do Produto Interno Bruto") + "."),
        "tipo_erro": ["ANACRONISMO", "GENERALIZACAO"], "moduladores": ["integralmente"], "dificuldade": 3,
        "comentario_fonte": ("Setor dummy era prática de sistemas antigos; no SNA 93/2008 o SIFIM é distribuído "
                             "aos setores; parcelas de famílias, governo e exportações são demanda final e elevam o "
                             "PIB."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00408
    {
        "id": "ECO-E2-L00408-1", "fonte_ref": "E2-L00408", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Nas Contas Econômicas Integradas, os setores institucionais agrupam unidades com autonomia de "
                      "decisão e contabilidade completa. As empresas estatais que vendem seus bens e serviços no "
                      "mercado a preços economicamente significativos devem ser classificadas no setor "
                      "“Administração Pública”, dada a origem governamental e estatal de seu controle acionário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nas Contas Econômicas Integradas, os setores institucionais agrupam unidades com autonomia "
                       "de decisão e contabilidade completa. As empresas estatais que vendem seus bens e serviços no "
                       "mercado a preços economicamente significativos devem ser classificadas no setor ")
                    + vm("“Administração Pública”, dada a origem governamental e estatal de seu controle "
                         "acionário") + az(".")),
        "poucas": ("O SCN classifica pela " + azb("função econômica") + ", não pelo dono: estatal que vende a "
                   + azb("preços economicamente significativos") + " é produtora mercantil e vai para "
                   "<b>empresas não financeiras</b> (ou financeiras)."),
        "destrinchando": [
            azb("Setores institucionais") + " das CEI: empresas não financeiras, empresas financeiras, "
            "administração pública, famílias, instituições sem fins de lucro a serviço das famílias e, à parte, "
            "o resto do mundo. A primeira frase do item (autonomia de decisão e contabilidade completa) define "
            "corretamente a " + azb("unidade institucional") + ".",
            "Critério decisivo: " + azb("mercantil × não mercantil") + ". Vende a preço que cobre a maior parte "
            "dos custos (preço economicamente significativo)? É mercantil → setor de empresas. Fornece de graça "
            "ou a preço simbólico, financiada por impostos? É administração pública.",
            "Exemplos: " + rx("Petrobras") + " e Correios → empresas não financeiras; " + rx("Banco do Brasil")
            + ", Caixa e BNDES → empresas financeiras; universidade federal, SUS, autarquias → administração "
            "pública.",
            "O controle estatal muda a classificação em outra dimensão: as estatísticas fiscais. As estatais "
            "entram no setor público consolidado das NFSP, mas, nas Contas Nacionais, são empresas.",
            vm("Regra-âncora: no SCN, quem decide o setor é o comportamento econômico, não a propriedade do "
               "capital."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A primeira frase é correta; na segunda, o "
                       "item reconhece que a estatal vende a preços significativos — o critério que a põe no setor "
                       "de empresas — e mesmo assim a classifica pela propriedade. A pista está no próprio "
                       "enunciado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma universidade pública federal, financiada por impostos, integra o setor administração "
            "pública.”</i> → CERTO",
            "<i>“O Banco do Brasil, por ser controlado pela União, integra o setor administração pública nas "
            "Contas Nacionais.”</i> → ERRADO (troca de conceito: empresas financeiras)",
        ])],
        "reescrita": ("Nas Contas Econômicas Integradas, os setores institucionais agrupam unidades com autonomia de "
                      "decisão e contabilidade completa. As empresas estatais que vendem seus bens e serviços no "
                      "mercado a preços economicamente significativos devem ser classificadas no setor "
                      + hl("“Empresas não financeiras” (ou “Empresas financeiras”), dado o caráter mercantil de sua "
                           "produção, e não a origem estatal de seu controle acionário") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Critério é o comportamento econômico, não a propriedade; estatais mercantis vão para "
                             "empresas não financeiras ou financeiras; administração pública só engloba unidades de "
                             "não mercado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00409
    {
        "id": "ECO-E2-L00409-1", "fonte_ref": "E2-L00409", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A variação de estoques compõe a parcela de formação bruta de capital da economia, refletindo "
                      "as flutuações de bens não comercializados no período. Se uma indústria automobilística produz "
                      "veículos e não os vende no mesmo ano civil, essas unidades são contabilizadas positivamente na "
                      "variação de estoques. No ano seguinte, quando forem efetivamente vendidas a consumidores "
                      "finais residentes, haverá um impacto positivo no consumo e um impacto negativo de igual valor "
                      "na variação de estoques, não se alterando o PIB deste ano subsequente por essa transação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A variação de estoques compõe a parcela de formação bruta de capital da economia, refletindo "
                      "as flutuações de bens não comercializados no período. Se uma indústria automobilística produz "
                      "veículos e não os vende no mesmo ano civil, essas unidades são contabilizadas positivamente na "
                      "variação de estoques. No ano seguinte, quando forem efetivamente vendidas a consumidores "
                      "finais residentes, haverá um impacto positivo no consumo e um impacto negativo de igual valor "
                      "na variação de estoques, <u>não se alterando o PIB</u> deste ano subsequente por essa "
                      "transação."),
        "poucas": ("O PIB mede a " + azb("produção") + " do período. O carro entra no PIB do ano 1, como "
                   + azb("variação de estoques") + "; no ano 2, a venda soma em C e subtrai em ΔE: efeito líquido "
                   + vd("zero") + "."),
        "destrinchando": [
            "Ótica da despesa: " + vd("PIB = C + FBCF + ΔE + G + (X − M)") + ". A " + azb("variação de "
            "estoques") + " é a “despesa” que fecha a conta quando a produção não é vendida no período: "
            "contabilmente, a empresa “compra de si mesma” o que não vendeu.",
            "Ano 1: carro de R$ 100 mil produzido e não vendido → ΔE = +100 → PIB +100. Ano 2: vendido a uma "
            "família → C = +100 e ΔE = −100 → contribuição líquida ao PIB do ano 2 = " + vd("0") + ".",
            "Se o carro fosse vendido no ano 2 a um não residente, o lançamento seria X = +100 e ΔE = −100: "
            "mesmo efeito nulo. Se fosse vendido usado, anos depois, também não entraria (bem usado não é "
            "produção nova), salvo a margem do revendedor.",
            "A mesma lógica explica por que estoques indesejados sinalizam desaceleração: a produção "
            "superou as vendas, e a empresa tende a cortar a produção futura (ajuste da " + azb("cruz "
            "keynesiana") + ").",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Item longo, todo verdadeiro. A armadilha é "
                       "achar que a venda “gera” PIB no ano 2: quem pensa em vendas, e não em produção, marca "
                       "ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A venda, no ano seguinte, de veículos produzidos e estocados no ano anterior eleva o PIB do ano "
            "da venda.”</i> → ERRADO (troca de conceito: o PIB mede produção, não vendas)",
            "<i>“Variação de estoques negativa reduz o PIB pela ótica da despesa, mantidos os demais "
            "componentes.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O PIB mede a produção do período; o carro não vendido entra via investimento em "
                             "estoques; vendido no ano seguinte, entra no consumo e sai dos estoques: o PIB do ano 2 "
                             "não sobe."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00422
    {
        "id": "ECO-E2-L00422-1", "fonte_ref": "E2-L00422", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Se quantidades e tecnologia não mudam, PIB a preços de mercado não se afasta do produto a "
                      "custo de fatores, já que impostos e subsídios seriam ‘meras transferências’."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se quantidades e tecnologia não mudam, PIB a preços de mercado ") + vm("não se afasta")
                    + az(" do produto a custo de fatores")
                    + vm(", já que impostos e subsídios seriam ‘meras transferências’") + az(".")),
        "poucas": ("A distância entre os dois é, por definição, " + vd("impostos indiretos − subsídios")
                   + ". Quantidades fixas não a anulam: basta haver tributação indireta líquida — ou mudar a "
                   "alíquota — para o " + azb("PIBpm") + " diferir do " + azb("PIBcf") + "."),
        "destrinchando": [
            vd("PIBpm = PIBcf + impostos indiretos − subsídios") + ". A diferença depende só da tributação "
            "indireta líquida, não das quantidades nem da tecnologia.",
            "Exemplo: produção física idêntica em dois anos; o governo eleva o ICMS. O preço de mercado sobe, o "
            "PIBpm nominal sobe; a remuneração dos fatores (PIBcf) não muda. A distância entre eles aumentou "
            "sem nenhuma mudança real.",
            "O argumento de “meras transferências” mistura dois planos: é verdade que impostos não remuneram "
            "fatores — é <b>justamente por isso</b> que ficam fora do custo de fatores e dentro do preço de "
            "mercado. Ser transferência não os faz sumir da medida a preços de mercado.",
            "Implicação analítica: comparações internacionais de PIBpm podem refletir estruturas tributárias "
            "diferentes (países com muito imposto indireto, como o " + rx("Brasil") + ", têm cunha maior entre "
            "as duas medidas).",
            vm("Regra-âncora: PIBpm − PIBcf = impostos indiretos líquidos de subsídios, com ou sem mudança de "
               "quantidades."),
        ],
        "dissecando": (cz("[nexo indevido · contradição]") + " O item usa uma premissa irrelevante (quantidades e "
                       "tecnologia constantes) e uma meia-ideia verdadeira (“transferências”) para concluir que a "
                       "cunha tributária desaparece — o que contraria a própria definição dos dois agregados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento de impostos indiretos, com produção física constante, eleva o PIB nominal a preços de "
            "mercado, mas não o PIB a custo de fatores.”</i> → CERTO",
            "<i>“Em uma economia sem impostos indiretos nem subsídios, PIB a preços de mercado e a custo de "
            "fatores coincidem.”</i> → CERTO",
        ])],
        "reescrita": ("Se quantidades e tecnologia não mudam, PIB a preços de mercado " + hl("ainda se afasta")
                      + " do produto a custo de fatores" + hl(" pelo valor dos impostos indiretos líquidos de "
                      "subsídios, que entram no preço de mercado") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "CONTRADICAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Produto a preços de mercado = produto a custo de fatores + impostos sobre produtos − "
                             "subsídios; mudanças tributárias alteram a mensuração a preços de mercado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: aspas finais soltas e apóstrofo da fonte normalizados (‘meras "
                    "transferências’)"],
    },
    # ------------------------------------------------------------------ E2-L00423
    {
        "id": "ECO-E2-L00423-1", "fonte_ref": "E2-L00423", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Apesar de produto, renda e despesa serem equivalentes, mudanças em qualquer uma das óticas não "
                      "causam automaticamente igual variação nas demais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Apesar de produto, renda e despesa serem equivalentes, mudanças em qualquer uma das óticas "
                      "<u>não causam automaticamente</u> igual variação nas demais."),
        "poucas": ("A igualdade " + vd("P ≡ R ≡ D") + " é " + azb("identidade contábil ex post") + ": vale "
                   "sempre, depois de feitos os registros, mas não diz <b>como</b> um choque se propaga. Causalidade "
                   "exige comportamento (propensões, expectativas, ajuste de estoques e preços)."),
        "destrinchando": [
            "As três óticas medem o mesmo fluxo: o valor adicionado na produção é a renda de alguém e é "
            "comprado por alguém. A igualdade é garantida por construção — sobretudo pela " + azb("variação de "
            "estoques") + ", que absorve na despesa tudo o que foi produzido e não vendido.",
            "Exemplo: as famílias decidem consumir menos. No curto prazo, a produção e a renda não mudam; o que "
            "não foi vendido vira " + azb("investimento não planejado em estoques") + " e a identidade fecha. "
            "Só depois, se as empresas reduzirem a produção, a queda chega à renda — e em proporção que depende "
            "da " + azb("propensão marginal a consumir") + " (multiplicador).",
            "É a distinção de " + oc("Keynes") + " entre grandezas " + azb("ex ante") + " (planejadas: o que se "
            "pretende gastar e produzir) e " + azb("ex post") + " (realizadas). Ex ante, despesa planejada e "
            "produto podem divergir; o equilíbrio é uma condição a alcançar, não uma identidade.",
            "Outros canais que impedem o espelhamento 1:1: vazamentos (poupança, impostos, importações), "
            "mudanças de preços relativos, defasagens temporais.",
            vm("Regra-âncora: identidade contábil descreve, não explica; causalidade exige teoria."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Quem decorou “as três óticas são iguais” "
                       "tende a deduzir que mexer em uma mexe nas outras na mesma medida. O “automaticamente” é o "
                       "ponto: a identidade fecha sempre, mas o caminho do ajuste não é automático."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como produto, renda e despesa são idênticos, uma queda do consumo reduz a renda na mesma "
            "proporção e no mesmo período.”</i> → ERRADO (nexo indevido: o ajuste passa por estoques e "
            "comportamento)",
            "<i>“Ex post, o investimento realizado inclui a variação não planejada de estoques.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["automaticamente"],
        "dificuldade": 2,
        "comentario_fonte": ("Equivalência contábil/ex post; causalidade exige mecanismo. Respostas de IA: estoques "
                             "como válvula de ajuste, vazamentos e injeções, ex ante × ex post, cunha de impostos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 065", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (P ≡ R ≡ D)"},
                          {"ref": "IMAGEM 066", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "cortada (fluxo circular de banco de imagens; não passa no teste do "
                                   "quadro-negro)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00424
    {
        "id": "ECO-E2-L00424-1", "fonte_ref": "E2-L00424", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A identidade (X − M) = (T − G) + (S − I) não demonstra que déficit público necessariamente "
                      "causa déficit externo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A identidade (X − M) = (T − G) + (S − I) <u>não demonstra</u> que déficit público "
                      "<u>necessariamente causa</u> déficit externo."),
        "poucas": ("Uma " + azb("identidade") + " só garante que os três saldos fecham. Um déficit público maior "
                   "pode ser compensado por mais " + azb("poupança privada") + " ou menos " + azb("investimento")
                   + ", sem tocar no saldo externo; a tese dos " + azb("déficits gêmeos") + " exige hipótese "
                   "comportamental."),
        "destrinchando": [
            "A igualdade " + vd("(X − M) = (T − G) + (S − I)") + " vale em qualquer economia, em qualquer ano, "
            "por construção contábil. Ela não tem variável dependente: qualquer termo pode ser o que se ajusta.",
            "Três vias de ajuste a um aumento do déficit (T − G cai): (1) " + azb("déficit externo") + " maior "
            "— déficits gêmeos, como nos " + rx("EUA") + " dos anos 1980; (2) " + azb("poupança privada")
            + " maior — no limite, " + azb("equivalência ricardiana") + " (" + oc("Barro") + "); (3) "
            + azb("investimento") + " menor — " + azb("crowding out") + " via juros.",
            "Qual via prevalece depende de modelo: grau de mobilidade de capitais, regime cambial, expectativas "
            "das famílias. No " + azb("Mundell-Fleming") + " com capital móvel e câmbio flutuante, a expansão "
            "fiscal aprecia o câmbio e piora as exportações líquidas — aí a ligação aparece, mas como resultado "
            "do modelo, não da identidade.",
            "Há também episódios de sinais opostos (déficit público com superávit externo), o que mostra que a "
            "relação não é necessária.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O item nega uma relação causal "
                       "“necessária” — e a negação de um absoluto costuma ser CERTA. A banca testa se o candidato "
                       "distingue identidade de teoria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A identidade dos três hiatos comprova que todo déficit público gera déficit em transações "
            "correntes de igual valor.”</i> → ERRADO (modulador absoluto e nexo indevido)",
            "<i>“Sob equivalência ricardiana plena, um aumento do déficit público não altera o saldo em "
            "transações correntes.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": "Não é mecanismo causal unívoco.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00294-1 (mesma identidade, cobrando as vias de compensação)"],
    },
    # ------------------------------------------------------------------ E2-L00444
    {
        "id": "ECO-E2-L00444-1", "fonte_ref": "E2-L00444", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": True,
        "comando": CMD_NAB_CN,
        "rotulo_item": "Item",
        "assertiva": ("O Produto Interno Bruto (PIB) pela ótica da renda é composto pela soma da remuneração dos "
                      "empregados, rendimento misto bruto, excedente operacional bruto e impostos sobre a produção e "
                      "importação, líquidos de subsídios."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Produto Interno Bruto (PIB) pela ótica da renda é composto pela soma da remuneração dos "
                      "empregados, <u>rendimento misto bruto</u>, excedente operacional bruto e <u>impostos sobre a "
                      "produção e importação, líquidos de subsídios</u>."),
        "poucas": ("É a decomposição oficial do IBGE: " + vd("PIB = RE + RMB + EOB + (impostos − subsídios sobre "
                   "a produção e a importação)") + ". Cada parcela diz <b>quem se apropriou</b> do valor "
                   "gerado."),
        "destrinchando": [
            azb("Remuneração dos empregados") + ": salários, 13º, férias e contribuições sociais dos "
            "empregadores — trabalho assalariado.",
            azb("Excedente operacional bruto") + ": remuneração do capital das empresas constituídas em sociedade "
            "(lucros, juros, aluguéis), antes da depreciação; inclui o aluguel imputado dos imóveis ocupados "
            "pelos donos.",
            azb("Rendimento misto bruto") + ": renda de autônomos e negócios familiares não constituídos em "
            "sociedade, em que trabalho e capital não se separam.",
            azb("Impostos sobre a produção e a importação, líquidos de subsídios") + ": a fatia do governo. "
            "Somam-se aqui <b>todos</b> — os sobre produtos (ICMS, IPI, II) e os outros sobre a produção "
            "(IPTU de empresas, taxas) — porque o objetivo é chegar ao valor a preços de mercado. Impostos sobre "
            "a renda não entram (já estão dentro dos rendimentos).",
            "As outras óticas: produção, " + vd("Σ VAB + impostos líquidos sobre produtos") + "; despesa, "
            + vd("C + I + G + (X − M)") + ". As três coincidem ex post, com ajuste estatístico na prática.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a fórmula oficial. Variantes que a banca usa para "
                       "derrubar: trocar EOB por “lucro líquido”, omitir o rendimento misto, ou dizer que os "
                       "impostos entram “acrescidos” de subsídios."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…e impostos sobre a produção e importação, acrescidos dos subsídios.”</i> → ERRADO (inversão: "
            "subsídios são subtraídos)",
            "<i>“O imposto de renda das pessoas físicas é somado à parte, como componente do PIB pela ótica da "
            "renda.”</i> → ERRADO (troca de conceito: já está dentro dos rendimentos)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PIB pela renda = salários + EOB (lucros e aluguéis) + RMB (autônomos) + impostos "
                             "indiretos líquidos de subsídios; resposta de IA com as três óticas e o que entra e "
                             "fica fora do PIB."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 073, 074, 075", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto"},
                          {"ref": "IMAGEM 076", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00400-1 (mesma fórmula da ótica da renda, outra fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00502
    {
        "id": "ECO-E2-L00502-1", "fonte_ref": "E2-L00502", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": ("Acerca de macroeconomia aberta e sistema monetário internacional, julgue (C ou E) os itens a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Em certo país, entre dois anos, a poupança do setor privado se manteve constante e a "
                      "poupança do governo diminuiu, mas o investimento bruto aumentou. Logo, podemos concluir que o "
                      "saldo em transações correntes necessariamente aumentou."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em certo país, entre dois anos, a poupança do setor privado se manteve constante e a "
                       "poupança do governo diminuiu, mas o investimento bruto aumentou. Logo, podemos concluir que "
                       "o saldo em transações correntes necessariamente ") + vm("aumentou") + az(".")),
        "poucas": (vd("STC = S<sub>privada</sub> + S<sub>governo</sub> − I") + ". Poupança nacional caiu e "
                   "investimento subiu: o " + azb("saldo em transações correntes") + " necessariamente "
                   + vd("diminuiu") + "."),
        "destrinchando": [
            "Identidade da economia aberta: " + vd("S − I = STC") + ", com S = poupança nacional = privada + "
            "pública. Toda a informação do item cabe nela.",
            "Conta: ΔS<sub>priv</sub> = 0; ΔS<sub>gov</sub> < 0 → ΔS < 0. ΔI > 0. Logo " + vd("ΔSTC = ΔS − ΔI "
            "< 0") + ": o saldo piorou — superávit menor ou déficit maior.",
            "Leitura econômica: o país passou a poupar menos e investir mais; a diferença só pode vir da "
            + azb("poupança externa") + " (déficit em transações correntes financiado pela conta financeira).",
            "Note que aqui o “necessariamente” seria verdadeiro com o verbo certo, porque <b>as duas</b> "
            "variações empurram o STC para baixo. Se uma subisse e outra caísse, o sinal ficaria indeterminado.",
            vm("Regra-âncora: menos poupança ou mais investimento → pior saldo externo."),
        ],
        "dissecando": (cz("[inversão]") + " O item faz a conta certa até o fim e troca só o sentido "
                       "(“aumentou” por “diminuiu”). O “necessariamente” está lá para parecer o erro, mas não é: "
                       "a conclusão correta também é necessária."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a poupança privada aumentou e o investimento também aumentou, o saldo em transações correntes "
            "necessariamente diminuiu.”</i> → ERRADO (indeterminado: depende das magnitudes)",
            "<i>“Mantidos o investimento e a poupança privada, um aumento do déficit público piora o saldo em "
            "transações correntes.”</i> → CERTO",
        ])],
        "reescrita": ("Em certo país, entre dois anos, a poupança do setor privado se manteve constante e a "
                      "poupança do governo diminuiu, mas o investimento bruto aumentou. Logo, podemos concluir que o "
                      "saldo em transações correntes necessariamente " + hl("diminuiu") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": ("STC = S − I; poupança nacional caiu e investimento subiu: o STC diminuiu (ou o déficit "
                             "aumentou)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00654
    {
        "id": "ECO-E2-L00654-1", "fonte_ref": "E2-L00654", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à macroeconomia, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("Na macroeconomia, a Contabilidade Nacional é uma ferramenta essencial para medir a atividade "
                      "econômica de um país. O Produto Interno Bruto (PIB) pode ser mensurado por diferentes óticas. "
                      "As três óticas principais de mensuração do PIB são: Ótica do Consumo, Ótica da Produção e "
                      "Ótica da Renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na macroeconomia, a Contabilidade Nacional é uma ferramenta essencial para medir a atividade "
                       "econômica de um país. O Produto Interno Bruto (PIB) pode ser mensurado por diferentes "
                       "óticas. As três óticas principais de mensuração do PIB são: ") + vm("Ótica do Consumo")
                    + az(", Ótica da Produção e Ótica da Renda.")),
        "poucas": ("As três óticas são " + azb("produção") + ", " + azb("renda") + " e " + azb("despesa")
                   + " (ou dispêndio). O consumo é só um componente da despesa, não uma ótica."),
        "destrinchando": [
            azb("Produção") + " (valor adicionado): " + vd("PIB = Σ (valor bruto da produção − consumo "
            "intermediário) + impostos líquidos sobre produtos") + ". Evita a dupla contagem somando só o que "
            "cada etapa acrescenta.",
            azb("Renda") + ": " + vd("PIB = remuneração dos empregados + rendimento misto + excedente "
            "operacional + impostos líquidos sobre a produção e a importação") + " — quem se apropriou do valor "
            "gerado.",
            azb("Despesa") + " (dispêndio, demanda): " + vd("PIB = C + I + G + (X − M)") + ". O consumo das "
            "famílias é o maior componente — no " + rx("Brasil") + ", mais de 60% do PIB ⏳ (out/2026) —, mas é "
            "uma parcela, ao lado de investimento, governo e setor externo.",
            "As três chegam ao mesmo valor ex post (identidade). No " + rx("Brasil") + ", o IBGE divulga o PIB "
            "trimestral pelas óticas da produção e da despesa; a da renda aparece nas contas anuais.",
            vm("Regra-âncora: produção, renda e despesa — nunca “consumo”."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca uma ótica (despesa) por um de seus componentes "
                       "(consumo). O texto introdutório é todo verdadeiro e serve para baixar a guarda; o erro "
                       "está numa palavra da lista final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela ótica da despesa, o PIB é a soma do consumo das famílias, da formação bruta de capital, do "
            "consumo do governo e das exportações líquidas.”</i> → CERTO",
            "<i>“A ótica da produção soma o valor bruto da produção de todos os setores.”</i> → ERRADO (dupla "
            "contagem: soma o valor adicionado)",
        ])],
        "reescrita": ("Na macroeconomia, a Contabilidade Nacional é uma ferramenta essencial para medir a atividade "
                      "econômica de um país. O Produto Interno Bruto (PIB) pode ser mensurado por diferentes óticas. "
                      "As três óticas principais de mensuração do PIB são: " + hl("Ótica da Despesa")
                      + ", Ótica da Produção e Ótica da Renda."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("As três óticas são produção (valor adicionado), renda e despesa (dispêndio); o consumo "
                             "é componente da despesa, não ótica isolada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
