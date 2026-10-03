"""Cards do lote de redação 03 — ECO, passada 02 (nota 17: Contas Nacionais)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "id": "🔄 Identidades e óticas do produto",
    "pib": "📏 PIB, PNB, RNB e conceitos derivados",
    "pm": "💲 Preços de mercado × custo de fatores",
    "scn": "🧾 SCN e tabelas",
}

CMD_AGREG = "No que diz respeito aos principais agregados macroeconômicos, julgue o item a seguir."
CMD_CN_BP_SM = ("Em relação às contas nacionais, ao balanço de pagamentos e ao sistema monetário, julgue o item a "
                "seguir.")
CMD_TEORIA = "Em relação à teoria macroeconômica, julgue o item a seguir."
CMD_CONTAB = "Em relação à contabilidade nacional, julgue o item a seguir."
CMD_CN_BP_TM = ("A respeito das contas nacionais, do balanço de pagamentos e da teoria monetária, julgue o item a "
                "seguir.")
CMD_BP_CN = "Acerca da estrutura do balanço de pagamentos e das contas nacionais, julgue o item a seguir."
CMD_TEORIA_AGREG = ("Considerando a teoria macroeconômica e os principais agregados macroeconômicos, julgue o item a "
                    "seguir.")
CMD_CN_BP = "Acerca das contas nacionais e do balanço de pagamentos, julgue o item a seguir."
CMD_CN = "Em relação às contas nacionais, julgue o item a seguir."
CMD_AGREG_CN_BP = ("Acerca de agregados macroeconômicos, das contas nacionais e de balanço de pagamentos, julgue o "
                   "item a seguir.")
CMD_ABERTA = ("Julgue o item a seguir acerca dos fluxos internacionais de bens e capital em uma economia aberta.")
CMD_ABERTA_BP = ("No que diz respeito aos conceitos subjacentes a uma economia aberta e ao balanço de pagamentos, "
                 "julgue o item a seguir.")
CMD_IMPORT = ("Considerando a importância da contabilidade nacional para o estudo da determinação e do "
              "comportamento dos grandes agregados nacionais, julgue o item a seguir.")
CMD_RIQUEZA = ("No que diz respeito à formação da renda e do produto e suas relações com a riqueza nacional, julgue "
               "o item a seguir.")

CARDS = [
    # ------------------------------------------------------------------ E2-L00717
    {
        "id": "ECO-E2-L00717-1", "fonte_ref": "E2-L00717", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_AGREG,
        "rotulo_item": "Item",
        "assertiva": ("O valor adicionado equivale aos custos de processamento, os quais definem o produto da "
                      "empresa, e difere do valor de produção, por ser inferior a este."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O valor adicionado equivale aos <u>custos de processamento</u>, os quais definem o produto "
                      "da empresa, e difere do valor de produção, por ser <u>inferior</u> a este."),
        "poucas": (azb("Valor adicionado") + " = " + vd("VBP − consumo intermediário") + ": é o que a empresa "
                   "acrescenta ao transformar os insumos comprados — a remuneração dos fatores que ela emprega. "
                   "Como desconta os insumos, é menor que o valor da produção."),
        "destrinchando": [
            azb("Valor bruto da produção (VBP)") + " = valor de tudo o que a unidade produziu no período (vendas "
            "mais variação dos estoques de produtos), inclusive o valor dos insumos comprados de outras empresas. "
            "Subtraindo o " + azb("consumo intermediário (CI)") + " — matérias-primas, energia, serviços usados "
            "e esgotados na produção —, sobra o " + vd("VA = VBP − CI") + ".",
            "Os “custos de processamento” são os custos de transformar os insumos em produto: salários, juros, "
            "aluguéis, lucros e, no conceito bruto, a depreciação. Somados, formam exatamente o VA — por isso o "
            "VA é o <b>produto da empresa</b>, sua contribuição líquida de insumos ao produto do país.",
            "Exemplo: trigo vendido por 100 ao moinho; farinha vendida por 150 à padaria; pão vendido por 250 ao "
            "consumidor. VAs: 100 + 50 + 100 = " + vd("250") + " = valor do bem final. A soma dos VBPs (500) "
            "contaria o trigo três vezes — é a " + azb("dupla contagem") + " que o conceito de VA evita.",
            "Somando os VAs de todas as unidades residentes (e os impostos líquidos sobre produtos) chega-se ao "
            + azb("PIB pela ótica da produção") + ".",
            vm("Regra-âncora: produto da empresa = valor adicionado, nunca o valor bruto da produção."),
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " A expressão “custos de processamento” "
                       "parece excluir o lucro e induz a marcar ERRADO; no jargão das contas nacionais, ela "
                       "abrange a remuneração de todos os fatores. A segunda parte é a identidade VA = VBP − CI "
                       "lida em palavras: com CI positivo, o VA é necessariamente menor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O valor bruto da produção é a medida do produto da empresa, pois inclui todos os seus "
            "custos.”</i> → ERRADO (troca de conceito: o produto da empresa é o VA)",
            "<i>“A soma dos valores adicionados de todas as etapas de produção iguala o valor dos bens "
            "finais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("VA = VBP − CI; “custos de processamento” entendidos como a remuneração de todos os "
                             "fatores (salários, lucros, juros, aluguéis, depreciação); VA inferior ao VBP quando "
                             "há consumo intermediário."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L00772 (mesmo item; verso fundido)"],
    },
    # ------------------------------------------------------------------ E2-L00718
    {
        "id": "ECO-E2-L00718-1", "fonte_ref": "E2-L00718", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_AGREG,
        "rotulo_item": "Item",
        "assertiva": ("Em um país onde haja recebimento líquido de rendas do exterior, o produto nacional bruto "
                      "será maior que o produto interno bruto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um país onde haja <u>recebimento líquido</u> de rendas do exterior, o produto nacional "
                      "bruto será <u>maior</u> que o produto interno bruto."),
        "poucas": (vd("PNB = PIB + RLRE") + ". Se a " + azb("renda líquida recebida do exterior") + " é "
                   "positiva (recebe-se mais do que se envia), o PNB supera o PIB."),
        "destrinchando": [
            azb("Interno") + " × " + azb("nacional") + ": o PIB mede o que é produzido <b>dentro do território</b>, "
            "seja por fatores de residentes ou de não residentes; o PNB mede a renda dos fatores de "
            "<b>residentes</b>, onde quer que estejam empregados.",
            "A ponte entre os dois é a " + azb("renda primária") + " do balanço de pagamentos (BPM6): "
            "remuneração de empregados e renda de investimentos (juros, lucros e dividendos, lucros "
            "reinvestidos). RLRE = renda recebida − renda enviada; RLEE = −RLRE.",
            "Logo: " + vd("RLRE > 0 → PNB > PIB") + " (caso típico de países credores ou com muitos "
            "investimentos no exterior); " + vd("RLRE < 0 → PNB < PIB") + " (caso de países receptores de "
            "capital estrangeiro).",
            "O " + rx("Brasil") + " é estruturalmente remetente líquido de renda primária (lucros e dividendos "
            "de multinacionais, juros da dívida externa): o PNB fica abaixo do PIB, em torno de 3% do PIB nos "
            "anos recentes ⏳ (out/2026).",
            "No SCN 2008, o nome oficial do PNB é " + azb("renda nacional bruta (RNB)") + ": como mede renda de "
            "residentes, o rótulo “produto” caiu em desuso, mas a conta é a mesma.",
        ],
        "dissecando": (cz("[literalidade]") + " Aplicação direta de PNB = PIB + RLRE. O risco está na "
                       "linguagem: “recebimento líquido” = RLRE positiva. A banca costuma inverter usando "
                       "“envio líquido” ou a sigla RLEE para confundir o sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um país onde haja envio líquido de rendas ao exterior, o PNB será maior que o PIB.”</i> → "
            "ERRADO (sinal trocado: PNB < PIB)",
            "<i>“Se a renda líquida enviada ao exterior for negativa, o PNB superará o PIB.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "RLRE = renda recebida − renda enviada; PNB = PIB + RLRE; RLRE > 0 → PNB > PIB.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L00773 (mesmo item; verso fundido)"],
    },
    # ------------------------------------------------------------------ E2-L00757
    {
        "id": "ECO-E2-L00757-1", "fonte_ref": "E2-L00757", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CN_BP_SM,
        "rotulo_item": "Item",
        "assertiva": ("O PIB mede o valor de mercado de todos os bens e serviços (intermediários e finais) "
                      "produzidos em um país em um determinado período."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O PIB mede o valor de mercado de todos os bens e serviços ")
                    + vm("(intermediários e finais)") + az(" produzidos em um país em um determinado período.")),
        "poucas": ("O PIB soma só os bens e serviços " + azb("finais") + ". Incluir os intermediários seria "
                   + azb("dupla contagem") + ": seu valor já está embutido no preço dos bens finais."),
        "destrinchando": [
            "Definição-padrão: PIB = valor de mercado de todos os bens e serviços <b>finais</b> produzidos "
            "<b>dentro do território</b> de um país em um período. Cada palavra conta: “de mercado” (preços de "
            "mercado), “finais”, “produzidos” (não revendidos), “dentro do território” (interno), “no período” "
            "(fluxo).",
            "Bem " + azb("final") + " × " + azb("intermediário") + " é questão de <b>uso</b>, não de natureza: o "
            "pneu comprado pela montadora é intermediário; o pneu comprado pelo motorista é final. A farinha da "
            "padaria é intermediária; a farinha da dona de casa, final.",
            "Há três caminhos equivalentes para chegar ao mesmo número: " + azb("produção") + " (VBP − consumo "
            "intermediário + impostos líquidos sobre produtos), " + azb("despesa") + " (consumo das famílias, "
            "das instituições sem fins de lucro e da administração pública + formação bruta de capital fixo + "
            "variação de estoques + exportações − importações) e " + azb("renda") + " (remuneração dos "
            "empregados + rendimento misto bruto + excedente operacional bruto + impostos líquidos de subsídios "
            "sobre a produção e a importação).",
            "Em todas as óticas, o intermediário some: na produção, pelo desconto do CI; na despesa, porque só "
            "entram usos finais; na renda, porque só se somam remunerações de fatores.",
            vm("Regra-âncora: PIB = só bens e serviços finais; intermediário entra uma única vez, dentro do "
               "preço do final."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A definição está quase literal; o erro foi enxertado no "
                       "parêntese “(intermediários e finais)”, que soa como precisão a mais. Em definições de PIB, "
                       "confira sempre três palavras: <b>finais</b>, <b>produzidos</b> e <b>interno</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB mede o valor de mercado de todos os bens e serviços finais produzidos por residentes de "
            "um país, onde quer que estejam.”</i> → ERRADO (troca de conceito: isso é o produto nacional)",
            "<i>“Uma matéria-prima produzida no ano e não utilizada, que permanece em estoque, entra no PIB "
            "desse ano.”</i> → CERTO",
        ])],
        "reescrita": ("O PIB mede o valor de mercado de todos os bens e serviços " + hl("finais")
                      + " produzidos em um país em um determinado período."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["todos"], "dificuldade": 1,
        "comentario_fonte": ("PIB mede só bens e serviços finais; intermediários gerariam dupla contagem. Quadro "
                             "com as três óticas (produção, despesa, renda)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 111", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (quadro das três óticas no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00814
    {
        "id": "ECO-E2-L00814-1", "fonte_ref": "E2-L00814", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_TEORIA,
        "rotulo_item": "Item",
        "assertiva": ("Ao calcular o Produto Interno Bruto (PIB) pelas despesas, leva-se em consideração a balança "
                      "comercial, que equivale ao valor bruto das exportações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Ao calcular o Produto Interno Bruto (PIB) pelas despesas, leva-se em consideração a "
                       "balança comercial, que equivale ") + vm("ao valor bruto das exportações") + az(".")),
        "poucas": ("Na ótica da despesa entram as " + azb("exportações líquidas") + ": " + vd("X − M")
                   + " de bens e serviços. As importações são subtraídas porque não foram produzidas no país."),
        "destrinchando": [
            "Identidade da despesa: " + vd("PIB = C + I + G + (X − M)") + ". C, I e G já incluem bens "
            "importados (o celular importado está no consumo; a máquina importada, no investimento). Subtrair M "
            "retira o que foi produzido fora; somar X acrescenta o que foi produzido aqui e consumido fora.",
            "Por isso o saldo, e não as exportações brutas, é que pertence ao PIB. Um país pode exportar muito e "
            "ter contribuição externa negativa se importar ainda mais.",
            "Vocabulário: em sentido estrito (BPM6), " + azb("balança comercial") + " é o saldo de <b>bens</b>; o "
            "PIB usa o saldo de <b>bens e serviços</b> (balança comercial + serviços). Os manuais costumam "
            "chamar NX simplesmente de “balança comercial” — o que importa no item é que se trata de "
            "<b>saldo</b>.",
            "Consequência para a leitura de conjuntura: alta das importações reduz o PIB pela despesa só no "
            "sentido contábil — ela tira do PIB o que já estava em C, I ou G, sem destruir produção doméstica.",
            vm("Regra-âncora: no PIB pela despesa entra X − M, nunca X sozinho."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira oração é correta; o erro está na definição de "
                       "balança comercial como valor <b>bruto</b> das exportações. A palavra “bruto” é a pista: "
                       "saldo de comércio é sempre líquido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao calcular o PIB pelas despesas, somam-se as importações, pois representam gasto dos "
            "residentes.”</i> → ERRADO (sinal trocado: M é subtraído)",
            "<i>“Um aumento das importações financiado por queda do consumo de bens domésticos reduz o "
            "PIB.”</i> → CERTO",
        ])],
        "reescrita": ("Ao calcular o Produto Interno Bruto (PIB) pelas despesas, leva-se em consideração a balança "
                      "comercial, que equivale " + hl("às exportações líquidas (exportações menos importações) de "
                                                      "bens e serviços") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Na ótica da despesa entram as exportações líquidas de bens e serviços.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00929
    {
        "id": "ECO-E2-L00929-1", "fonte_ref": "E2-L00929", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_CONTAB,
        "rotulo_item": "Item",
        "assertiva": "Os estoques não entram no cálculo do PIB, pois não foram vendidos.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os estoques ") + vm("não entram") + az(" no cálculo do PIB, ") + vm("pois") + az(" não ")
                    + vm("foram") + az(" vendidos.")),
        "poucas": ("O PIB mede " + azb("produção") + ", não vendas. O que foi produzido e não vendido entra como "
                   + azb("variação de estoques") + ", componente do investimento."),
        "destrinchando": [
            "Investimento nas contas nacionais = " + vd("formação bruta de capital fixo + variação de "
                                                        "estoques") + " (FBC = FBCF + ΔE).",
            "A lógica: a produção do ano precisa aparecer em algum uso final. Se o carro fabricado em dezembro "
            "fica no pátio, ele é tratado como se a própria montadora o tivesse “comprado” para estoque — "
            "investimento em estoques. Assim, a identidade produto = despesa fecha.",
            "Quando o carro for vendido no ano seguinte, o consumo daquele ano sobe, mas a variação de estoques "
            "fica negativa no mesmo valor: o carro <b>não</b> entra de novo no PIB do ano seguinte.",
            "Atenção: o que entra é a " + azb("variação") + " (fluxo), não o nível do estoque. Estoque parado de "
            "um ano para outro não acrescenta nada; redução de estoques entra com sinal negativo.",
            "Matérias-primas compradas e não usadas também entram: no ano, elas não viraram consumo "
            "intermediário, então são uso final (estoque) da empresa.",
            vm("Regra-âncora: produzido e não vendido = investimento em estoques; entra no PIB do ano em que "
               "foi produzido."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item troca “produção” por “venda” e "
                       "cria um nexo falso (não vendido → fora do PIB). A justificativa “pois não foram "
                       "vendidos” parece razoável, mas o PIB nunca foi medida de vendas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A variação de estoques integra a formação bruta de capital.”</i> → CERTO",
            "<i>“Os bens produzidos em um ano e vendidos no seguinte são contabilizados no PIB do ano da "
            "venda.”</i> → ERRADO (anacronismo contábil: entram no ano da produção)",
        ])],
        "reescrita": ("Os estoques " + hl("entram") + " no cálculo do PIB, " + hl("como variação de estoques no "
                                                                                 "investimento, ainda que")
                      + " não " + hl("tenham sido") + " vendidos."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Estoques entram no PIB no ano em que são produzidos, dentro do investimento "
                             "(FBCF + variação de estoques)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00930
    {
        "id": "ECO-E2-L00930-1", "fonte_ref": "E2-L00930", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_CONTAB,
        "rotulo_item": "Item",
        "assertiva": ("O valor da venda de um apartamento usado não entra no cálculo do PIB, mas o valor referente "
                      "à corretagem, sim."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O valor da venda de um apartamento <u>usado</u> não entra no cálculo do PIB, mas o valor "
                      "referente à <u>corretagem</u>, sim."),
        "poucas": ("O apartamento já entrou no PIB do ano em que foi construído; revendê-lo é só "
                   + azb("transferência de ativo") + ". A " + azb("corretagem") + " é um serviço novo, prestado "
                   "no ano da venda, e entra."),
        "destrinchando": [
            "O PIB é um " + azb("fluxo de produção corrente") + ". A venda de bem usado (imóvel, carro, obra de "
            "arte antiga) apenas troca riqueza de mãos: o comprador ganha o imóvel, o vendedor ganha dinheiro, e "
            "nada foi produzido.",
            "Mas a transação de bem usado costuma <b>gerar serviços novos</b>: corretagem, registro em cartório, "
            "avaliação, mudança, reforma. Esses serviços são produção do período e entram no PIB.",
            "Mesma lógica para outras transações que não são produção: compra e venda de ações e títulos "
            "(transação financeira — entra só a comissão da corretora), " + azb("transferências") + " do governo "
            "(aposentadorias, Bolsa Família: redistribuem renda, não remuneram produção) e revenda de "
            "mercadorias (entra só a margem do comércio).",
            "Contraponto que a banca cobra: a construção de um imóvel <b>novo</b> entra no PIB, como formação "
            "bruta de capital fixo (residencial). E o aluguel — inclusive o imputado a quem mora em imóvel "
            "próprio — é serviço corrente e também entra.",
            vm("Regra-âncora: bem usado fora do PIB; serviço que acompanha a venda, dentro."),
        ],
        "dissecando": (cz("[detalhe]") + " Item verdadeiro pela distinção entre o ativo (já contado) e o "
                       "serviço (novo). Quem pensa “houve dinheiro trocando de mão, então entra” ou “nada entra, "
                       "pois o bem é velho” erra em direções opostas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A venda de um apartamento novo, construído no ano, não entra no PIB, pois é transferência de "
            "propriedade.”</i> → ERRADO (o imóvel novo é produção do ano: FBCF)",
            "<i>“A comissão paga à corretora pela compra de ações entra no PIB, mas o valor das ações não.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O apartamento usado foi contado no ano de produção; a venda é transferência de "
                             "propriedade. A corretagem é serviço final produzido no ano da venda e entra no PIB."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00931
    {
        "id": "ECO-E2-L00931-1", "fonte_ref": "E2-L00931", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_CONTAB,
        "rotulo_item": "Item",
        "assertiva": ("Se o país é exportador de capital, ou seja, apresenta superávit em transações correntes, "
                      "então a soma da poupança privada (deduzida dos investimentos) e da poupança do governo deve "
                      "ser positiva."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o país é exportador de capital, ou seja, apresenta superávit em transações correntes, "
                      "então a soma da poupança privada (deduzida dos investimentos) e da poupança do governo "
                      "<u>deve ser positiva</u>."),
        "poucas": ("Pela identidade " + vd("S − I = TC") + ", com S = Sp + Sg: " + vd("(Sp − I) + Sg = TC")
                   + ". Se TC > 0, essa soma é positiva."),
        "destrinchando": [
            "Partindo de Y = C + I + G + NX e definindo a renda disponível, chega-se a " + vd("S − I = TC")
            + " (desprezadas as transferências de capital): o excesso de poupança doméstica sobre o "
            "investimento é emprestado ao resto do mundo.",
            "Desdobrando a poupança doméstica em " + azb("poupança privada") + " (Sp = Y − T − C) e "
            + azb("poupança do governo") + " (Sg = T − G): " + vd("(Sp − I) + (T − G) = TC") + ". É a "
            "identidade dos três hiatos — privado, fiscal e externo.",
            "Superávit em transações correntes = o país gasta menos do que ganha e acumula ativos no exterior "
            "(ou reduz passivos): por isso é chamado " + azb("exportador de capital") + ". Nesse caso, a "
            + azb("poupança externa") + " (Se = −TC) é <b>negativa</b>.",
            "A identidade não diz que cada parcela seja positiva: o governo pode ter déficit (Sg < 0) desde que "
            "o setor privado poupe bem mais do que investe. Exemplo: Japão, com déficit fiscal crônico e "
            "superávit externo sustentado pela alta poupança privada.",
            "Leitura inversa, típica do " + rx("Brasil") + ": déficit em conta corrente (TC < 0) significa "
            "investimento financiado em parte por poupança externa (Se > 0).",
            vm("Regra-âncora: (Sp − I) + (T − G) = TC — o saldo externo é a soma dos saldos internos."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item é a identidade contábil lida em palavras. O "
                       "risco está em confundir “poupança externa” (negativa no superávit) com saldo em "
                       "transações correntes (positivo), ou em achar que o governo precisaria, sozinho, ter "
                       "superávit."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o país apresenta superávit em transações correntes, sua poupança externa é positiva.”</i> → "
            "ERRADO (sinal trocado: Se = −TC < 0)",
            "<i>“Se o país apresenta superávit em transações correntes, o governo necessariamente tem superávit "
            "fiscal.”</i> → ERRADO (modulador absoluto: basta a soma dos hiatos ser positiva)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["deve"], "dificuldade": 2,
        "comentario_fonte": ("S − I = TC; TC > 0 → S > I; S = Sp + Sg → (Sp − I) + Sg > 0; poupança externa "
                             "Se = −TC < 0."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00932
    {
        "id": "ECO-E2-L00932-1", "fonte_ref": "E2-L00932", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_CONTAB,
        "rotulo_item": "Item",
        "assertiva": ("A conta de bens e serviços das Contas Econômicas Integradas (CEI) retrata a atividade de "
                      "produção e o destino dessa produção pelas categorias de demanda final. A oferta agregada "
                      "global em equilíbrio deve igualar a demanda agregada global, que será igual à soma de "
                      "consumo, investimento, gastos do governo e importações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A conta de bens e serviços das Contas Econômicas Integradas (CEI) retrata a atividade de "
                       "produção e o destino dessa produção pelas categorias de demanda final. A oferta agregada "
                       "global em equilíbrio deve igualar a demanda agregada global, que será igual à soma de "
                       "consumo, investimento, gastos do governo e ") + vm("importações") + az(".")),
        "poucas": ("As importações estão do lado da " + azb("oferta global") + " (PIB + M); a "
                   + azb("demanda global") + " é " + vd("C + I + G + X") + "."),
        "destrinchando": [
            "Identidade de bens e serviços: " + vd("PIB + M = C + I + G + X") + ". De um lado, de onde vêm os "
            "bens finais disponíveis (produção doméstica e produção estrangeira importada); de outro, para onde "
            "vão (consumo, investimento, governo e exportação).",
            "Passando M para o outro lado, obtém-se a identidade familiar PIB = C + I + G + (X − M). As duas "
            "formas são a mesma conta; a diferença é só onde se registra M.",
            "Na " + azb("conta de bens e serviços") + " das CEI a identidade aparece de forma mais completa: "
            "recursos = produção + importação + impostos líquidos sobre produtos; usos = consumo intermediário + "
            "consumo final + formação bruta de capital + exportação.",
            "Teste de bom senso: importação é bem que <b>chegou</b> ao país, logo aumenta o que está disponível "
            "(oferta); exportação é bem que <b>saiu</b>, logo é destino (demanda).",
            vm("Regra-âncora: M é oferta, X é demanda — PIB + M = C + I + G + X."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Todo o item é correto até a última palavra: trocou-se "
                       "“exportações” por “importações”. Em enumerações longas, a banca costuma esconder o erro "
                       "no último termo da lista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A oferta global corresponde à soma do PIB com as importações.”</i> → CERTO",
            "<i>“A demanda global corresponde a C + I + G + X − M.”</i> → ERRADO (mistura as formas: C + I + G + "
            "X − M é o PIB, não a demanda global)",
        ])],
        "reescrita": ("A conta de bens e serviços das Contas Econômicas Integradas (CEI) retrata a atividade de "
                      "produção e o destino dessa produção pelas categorias de demanda final. A oferta agregada "
                      "global em equilíbrio deve igualar a demanda agregada global, que será igual à soma de "
                      "consumo, investimento, gastos do governo e " + hl("exportações") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Oferta global = PIB + M = C + I + G + X; a demanda global é C + I + G + X.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00933
    {
        "id": "ECO-E2-L00933-1", "fonte_ref": "E2-L00933", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_CN_BP_TM,
        "rotulo_item": "Item",
        "assertiva": ("A partir das informações das Tabelas de Recursos e Usos, são preparadas as Contas "
                      "Econômicas Integradas (CEI). Uma das contas componentes das CEI é Conta de Bens e Serviços, "
                      "que permite a visualização da identidade Oferta Total = Demanda Total. Essa conta utiliza "
                      "uma convenção contrária ao tradicional débito (usos) e crédito (recursos), sendo mostradas "
                      "as rubricas no centro das contas, os recursos à esquerda e os usos à direita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A partir das informações das Tabelas de Recursos e Usos, são preparadas as Contas "
                      "Econômicas Integradas (CEI). Uma das contas componentes das CEI é Conta de Bens e Serviços, "
                      "que permite a visualização da identidade Oferta Total = Demanda Total. Essa conta utiliza "
                      "uma <u>convenção contrária</u> ao tradicional débito (usos) e crédito (recursos), sendo "
                      "mostradas as rubricas no centro das contas, os <u>recursos à esquerda e os usos à "
                      "direita</u>."),
        "poucas": ("Na " + azb("conta de bens e serviços") + " (a conta 0 das CEI), os " + vd("recursos") + " (a "
                   "oferta total) vêm à esquerda e os " + vd("usos") + " (a demanda total), à direita — o inverso "
                   "das demais contas."),
        "destrinchando": [
            "As " + azb("Tabelas de Recursos e Usos (TRU)") + " detalham, produto a produto e atividade a "
            "atividade, a oferta e a demanda de bens e serviços. Delas saem os agregados que alimentam as "
            + azb("CEI") + ", o núcleo do SCN, que mostra a economia inteira em uma tabela, por setor "
            "institucional.",
            "Nas contas das CEI, a convenção usual é: " + vd("usos à esquerda, recursos à direita") + " (como "
            "débito e crédito). A conta de bens e serviços é a exceção: " + vd("recursos à esquerda, usos à "
                                                                               "direita") + ", com as operações "
            "listadas no centro.",
            "Exemplo do IBGE (2004, R$ milhões): recursos = produção 3.432.735 + importação 243.622 + impostos "
            "sobre produtos 276.077 − subsídios 837 = " + vd("3.951.597") + "; usos = consumo intermediário "
            "1.766.477 + consumo final 1.533.895 + FBCF 312.516 + variação de estoques 19.817 + exportação "
            "318.892 = " + vd("3.951.597") + ".",
            "Dessa conta sai o PIB: 3.951.597 − 1.766.477 − 243.622 = " + vd("1.941.498") + " (R$ 1,94 trilhão, o "
            "PIB brasileiro de 2004).",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item longo e técnico, verdadeiro por um pormenor de "
                       "apresentação. A banca aposta que o candidato, lembrando da convenção débito à esquerda, "
                       "ache que “contrária” é erro. 🔥 Inverter os lados (recursos à direita) é a versão ERRADA "
                       "mais provável."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…sendo mostrados os recursos à direita e os usos à esquerda, como nas demais contas das "
            "CEI.”</i> → ERRADO (inversão: na conta de bens e serviços, recursos à esquerda)",
            "<i>“A conta de bens e serviços registra como recursos a produção, as importações e os impostos "
            "líquidos de subsídios sobre produtos.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("A conta de bens e serviços mostra oferta total = demanda total, com recursos à "
                             "esquerda e usos à direita, contrária às demais contas das CEI. Tabela do IBGE de "
                             "2004."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 153", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (valores da conta de bens e serviços de 2004 no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01061-1 (mesma ideia, Pré-TPS/2023)"],
    },
    # ------------------------------------------------------------------ E2-L00934
    {
        "id": "ECO-E2-L00934-1", "fonte_ref": "E2-L00934", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_CN_BP_TM,
        "rotulo_item": "Item",
        "assertiva": ("Nas Contas Econômicas Integradas (CEI) são apresentadas, de maneira articulada, as rendas "
                      "geradas no processo produtivo; sua distribuição entre os agentes econômicos e sua utilização "
                      "em consumo final; e o montante de poupança destinado à acumulação de ativos não "
                      "financeiros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Nas Contas Econômicas Integradas (CEI) são apresentadas, <u>de maneira articulada</u>, as "
                      "rendas geradas no processo produtivo; sua distribuição entre os agentes econômicos e sua "
                      "utilização em consumo final; e o montante de poupança destinado à acumulação de ativos não "
                      "financeiros."),
        "poucas": ("É a definição do IBGE: as " + azb("CEI") + " encadeiam produção → geração da renda → "
                   "distribuição (primária e secundária) → uso em consumo → poupança → acumulação."),
        "destrinchando": [
            "As CEI são o " + azb("núcleo central do SCN") + ": numa única tabela, para cada setor institucional "
            "(empresas não financeiras, instituições financeiras, governo, famílias, ISFLSF e resto do mundo), "
            "mostram toda a sequência de contas.",
            "Sequência e saldos: " + azb("produção") + " (saldo: valor adicionado) → " + azb("geração da renda")
            + " (saldo: excedente operacional e rendimento misto) → " + azb("alocação da renda primária")
            + " (saldo: renda primária; no total, a RNB) → " + azb("distribuição secundária") + " (saldo: renda "
            "disponível bruta) → " + azb("uso da renda") + " (saldo: " + vd("poupança bruta") + ") → "
            + azb("conta de capital") + " (saldo: capacidade ou necessidade de financiamento).",
            "Cada conta começa com o saldo da anterior: é isso que faz a apresentação “articulada”. O saldo de "
            "uma conta é recurso da seguinte.",
            "A poupança bruta financia a " + azb("acumulação de ativos não financeiros") + " (formação bruta de "
            "capital fixo, estoques). O que sobra ou falta aparece como capacidade ou necessidade de "
            "financiamento, que a conta financeira detalha.",
        ],
        "dissecando": (cz("[literalidade]") + " Reprodução quase textual da nota metodológica do IBGE. Itens "
                       "assim costumam ser CERTO; o ERRADO viria de trocar “não financeiros” por “financeiros” "
                       "ou de dizer que as CEI tratam só da produção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…e o montante de poupança destinado à acumulação de ativos financeiros.”</i> → ERRADO (troca de "
            "conceito: a poupança da conta de capital financia ativos não financeiros)",
            "<i>“As CEI apresentam apenas a geração da renda, sem tratar de sua distribuição entre os "
            "setores.”</i> → ERRADO (restrição indevida)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("CEI: núcleo do SCN; mostram renda gerada, distribuição primária e secundária, "
                             "consumo final e poupança destinada à acumulação de ativos não financeiros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00956
    {
        "id": "ECO-E2-L00956-1", "fonte_ref": "E2-L00956", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_BP_CN,
        "excerto": ("<p>Um país realizou, em determinado ano, as transações com o exterior apresentadas a seguir: "
                    "importações de mercadoria: 5; exportações de mercadoria: 15; recebimento de doações na forma "
                    "de mercadorias: 1; empréstimos e financiamentos recebidos no exterior: 10; investimento "
                    "estrangeiro direto recebido do exterior, sem cobertura cambial, na forma de equipamentos: 15; "
                    "juros de empréstimos pagos ao exterior: 5; fretes pagos ao exterior 10.</p>"),
        "rotulo_item": "Item",
        "assertiva": ("Com base nessas informações, no período em apreço, o produto nacional bruto do país foi "
                      "inferior ao produto interno bruto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base nessas informações, no período em apreço, o produto nacional bruto do país foi "
                      "<u>inferior</u> ao produto interno bruto."),
        "poucas": ("Das transações listadas, só os " + vd("juros pagos (5)") + " são " + azb("renda primária")
                   + ". Logo, " + vd("PNB = PIB − 5") + ": o PNB é menor."),
        "destrinchando": [
            "PNB = PIB + renda recebida − renda enviada. O trabalho é separar o que é renda de fatores do resto "
            "do balanço de pagamentos.",
            "Classificação de cada transação: exportações 15 e importações 5 → " + azb("balança comercial")
            + "; fretes pagos 10 → " + azb("serviços") + " (frete é serviço de transporte, não remuneração de "
            "fator); juros pagos 5 → " + azb("renda primária") + " (renda de investimento enviada); doação em "
            "mercadorias 1 → " + azb("renda secundária") + " (transferência), com o bem doado registrado como "
            "importação; empréstimos recebidos 10 → " + azb("conta financeira") + "; IED em equipamentos 15 → "
            "conta financeira (passivo de investimento direto), com os equipamentos registrados como "
            "importação de bens.",
            "Só a renda primária separa PIB de PNB: RLEE = " + vd("5") + " → PNB = PIB − 5 < PIB.",
            "Pegadinhas da lista: frete parece “pagamento ao exterior” mas é serviço (afeta o PIB pela despesa, "
            "via importações, e não a diferença PIB × PNB); doação é transferência e só afeta a "
            + azb("renda nacional disponível") + "; empréstimos e IED são fluxos financeiros, não rendas.",
            vm("Regra-âncora: só a renda primária (salários, juros, lucros e dividendos) separa PIB de PNB."),
        ],
        "dissecando": (cz("[detalhe]") + " Item de classificação de lançamentos: a lista mistura bens, serviços, "
                       "renda, transferência e fluxos financeiros para atrair quem soma tudo que é "
                       "“pago ao exterior” (juros + fretes = 15) ou desconta empréstimos. O julgamento depende de "
                       "isolar uma única linha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a renda líquida enviada ao exterior foi de 15, considerados os juros e os fretes.”</i> → ERRADO "
            "(troca de conceito: frete é serviço, não renda)",
            "<i>“…a renda nacional disponível bruta foi inferior ao PNB.”</i> → ERRADO (inversão: a doação "
            "recebida de 1 a eleva acima do PNB)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("PNB = PIB + renda recebida − renda enviada = PIB − 5. Imagem com versão da lista "
                             "de transações e as fórmulas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 157", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (fórmulas PNB = PIB − renda líquida enviada no 📖)"}],
        "alertas": ["nota_redacao: a IMAGEM 157 do verso traz versão da lista com números diferentes (IED 5, "
                    "remessa de juros 3); o card segue a frente, coerente com a conclusão PNB = PIB − 5"],
    },
    # ------------------------------------------------------------------ E2-L00975
    {
        "id": "ECO-E2-L00975-1", "fonte_ref": "E2-L00975", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_TEORIA_AGREG,
        "rotulo_item": "Item",
        "assertiva": ("O produto interno líquido nunca será maior do que o produto interno bruto, assim como o "
                      "produto nacional bruto nunca será maior que o produto interno bruto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O produto interno líquido nunca será maior do que o produto interno bruto, ")
                    + vm("assim como") + az(" o produto nacional bruto ") + vm("nunca será")
                    + az(" maior que o produto interno bruto.")),
        "poucas": ("A primeira parte é verdadeira (" + vd("PIL = PIB − depreciação") + "); a segunda, não: "
                   + vd("PNB = PIB + RLRE") + ", e a renda líquida recebida do exterior pode ser positiva."),
        "destrinchando": [
            azb("Bruto") + " × " + azb("líquido") + ": a diferença é a " + azb("depreciação") + " (consumo de "
            "capital fixo), que nunca é negativa. Logo PIL ≤ PIB sempre — o “nunca” da primeira oração "
            "é seguro.",
            azb("Interno") + " × " + azb("nacional") + ": a diferença é a renda primária líquida com o exterior, "
            "que pode ter qualquer sinal. Se o país recebe mais renda do que envia, " + vd("PNB > PIB") + "; se "
            "envia mais, " + vd("PNB < PIB") + ".",
            "Exemplos: países com grandes estoques de investimento no exterior ou muitos trabalhadores "
            "emigrados que remetem salários tendem a ter PNB > PIB; países receptores de capital estrangeiro, "
            "como o " + rx("Brasil") + ", tendem a ter PNB < PIB.",
            "Quadro mental: são dois “ajustes” independentes. Bruto → líquido tira depreciação (sinal sempre "
            "conhecido); interno → nacional soma RLRE (sinal depende do país).",
            vm("Regra-âncora: PIL ≤ PIB sempre; PNB × PIB depende do sinal da renda líquida do exterior."),
        ],
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " A primeira oração é verdadeira e ancora a "
                       "confiança; a segunda pega carona (“assim como”) e estende o mesmo “nunca” a uma relação "
                       "cujo sinal varia. Em itens com dois “nunca”, teste cada um separadamente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O produto nacional líquido nunca será maior do que o produto nacional bruto.”</i> → CERTO",
            "<i>“O produto interno bruto será sempre maior que o produto nacional bruto em países "
            "desenvolvidos.”</i> → ERRADO (modulador absoluto: depende da renda líquida do exterior)",
        ])],
        "reescrita": ("O produto interno líquido nunca será maior do que o produto interno bruto, " + hl("mas")
                      + " o produto nacional bruto " + hl("pode ser") + " maior que o produto interno bruto"
                      + hl(", se a renda recebida do exterior superar a enviada") + "."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["nunca"], "dificuldade": 1,
        "comentario_fonte": ("O PNB pode ser maior ou menor que o PIB, conforme o saldo da renda primária: renda "
                             "enviada > recebida → PNB < PIB; o contrário → PNB > PIB."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00976
    {
        "id": "ECO-E2-L00976-1", "fonte_ref": "E2-L00976", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_TEORIA_AGREG,
        "rotulo_item": "Item",
        "assertiva": ("No cálculo do produto interno bruto (PIB), deduzem-se os bens e serviços intermediários, "
                      "para evitar dupla contagem. Os bens e os serviços finais são medidos pelo preço em que "
                      "chegam ao consumidor, incluídos os impostos sobre os produtos comercializados; trata-se, "
                      "portanto, de um indicador do fluxo de novos bens e serviços finais produzidos no período, e "
                      "não da riqueza do país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No cálculo do produto interno bruto (PIB), deduzem-se os bens e serviços intermediários, "
                      "para evitar dupla contagem. Os bens e os serviços finais são medidos pelo preço em que "
                      "chegam ao consumidor, <u>incluídos os impostos sobre os produtos</u> comercializados; "
                      "trata-se, portanto, de um indicador do <u>fluxo</u> de novos bens e serviços finais "
                      "produzidos no período, e não da riqueza do país."),
        "poucas": ("Três atributos corretos do PIB: só bens " + azb("finais") + " (sem dupla contagem), avaliados "
                   "a " + azb("preços de mercado") + " (com impostos sobre produtos) e medidos como "
                   + azb("fluxo") + " do período, não como estoque de riqueza."),
        "destrinchando": [
            azb("Dupla contagem") + ": o valor dos insumos já está no preço do bem final. Por isso, pela ótica "
            "da produção, deduz-se o consumo intermediário do valor bruto da produção.",
            azb("Preços de mercado") + ": o PIB oficial do IBGE é a preços de mercado — o preço pago pelo "
            "comprador final, com os impostos sobre produtos (ICMS, IPI, PIS/Cofins, ISS) e líquido de "
            "subsídios. Retirando os impostos indiretos líquidos, chega-se ao PIB a " + azb("custo de fatores")
            + ", que mede só a remuneração dos fatores.",
            azb("Fluxo × estoque") + ": o PIB é medido <b>por período</b> (trimestre, ano), como a vazão de uma "
            "torneira. A riqueza (capital, imóveis, ativos financeiros) é estoque, medido <b>em uma data</b>, "
            "como a água acumulada na caixa. O investimento (fluxo) aumenta o estoque de capital; a "
            "depreciação o reduz.",
            "Consequência: um país pode ser rico (grande estoque de riqueza) e ter PIB baixo em um ano de crise, "
            "e um desastre que destrói riqueza pode até elevar o PIB seguinte, via reconstrução — uma das "
            "críticas clássicas ao PIB como medida de bem-estar.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item longo com três afirmações verdadeiras "
                       "encadeadas. O risco está no meio: quem confunde preço de mercado com custo de fatores "
                       "estranha “incluídos os impostos”. Versões ERRADAS trocariam “fluxo” por “estoque” ou "
                       "diriam “excluídos os impostos”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os bens e serviços finais são medidos pelo preço recebido pelo produtor, excluídos os impostos "
            "sobre produtos…”</i> → ERRADO (troca de conceito: isso seria preço básico, não o PIB a preços de "
            "mercado)",
            "<i>“…trata-se de um indicador da riqueza acumulada do país.”</i> → ERRADO (troca de conceito: o PIB "
            "é fluxo, riqueza é estoque)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01060
    {
        "id": "ECO-E2-L01060-1", "fonte_ref": "E2-L01060", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN_BP,
        "rotulo_item": "Item",
        "assertiva": ("As contas econômicas integradas compõem o Sistema de Contas Nacionais do Brasil, conforme "
                      "metodologia orientada pela Organização das Nações Unidas (ONU). A conta de distribuição "
                      "primária da renda é constituída pelas contas geração de renda e renda nacional bruta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As contas econômicas integradas compõem o Sistema de Contas Nacionais do Brasil, conforme "
                       "metodologia orientada pela Organização das Nações Unidas (ONU). A conta de distribuição "
                       "primária da renda é constituída pelas contas geração de renda e ")
                    + vm("renda nacional bruta") + az(".")),
        "poucas": ("A " + azb("renda nacional bruta") + " não é conta: é " + azb("saldo") + ". A distribuição "
                   "primária da renda se divide em " + vd("geração da renda") + " e " + vd("alocação da renda "
                                                                                         "primária") + "."),
        "destrinchando": [
            "O SCN brasileiro segue o manual internacional (SCN 2008, elaborado por ONU, FMI, OCDE, Banco "
            "Mundial e Comissão Europeia). Nas " + azb("CEI") + ", cada conta tem usos, recursos e um "
            + azb("saldo") + " que passa para a conta seguinte.",
            "Contas e saldos: produção → " + vd("valor adicionado / PIB") + "; " + azb("geração da renda")
            + " (como o VA remunera empregados e governo) → " + vd("excedente operacional bruto e rendimento "
                                                                   "misto") + "; " + azb("alocação da renda "
                                                                                         "primária")
            + " (no SCN do IBGE, “alocação da renda”: juros, lucros e dividendos recebidos e pagos) → "
            + vd("saldo da renda primária; no total da economia, a RNB") + ".",
            "Juntas, geração da renda e alocação da renda primária formam a " + azb("conta de distribuição "
                                                                                     "primária da renda")
            + ". Seguem: distribuição secundária (saldo: renda disponível bruta), uso da renda (saldo: "
            "poupança bruta) e conta de capital (saldo: capacidade ou necessidade de financiamento).",
            "Outros agregados que aparecem como saldos: produto interno, saldo externo de bens e serviços, renda "
            "nacional disponível, poupança e patrimônio.",
            vm("Regra-âncora: agregados (PIB, RNB, RDB, poupança) são saldos das contas, não contas."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira frase é verdadeira; na segunda, a banca colocou "
                       "um <b>saldo</b> no lugar de uma <b>conta</b>. Como a RNB é mesmo o resultado da "
                       "distribuição primária, o nome soa familiar e passa despercebido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo da conta de distribuição primária da renda, para o total da economia, corresponde à "
            "renda nacional bruta.”</i> → CERTO",
            "<i>“A conta de distribuição secundária da renda tem como saldo a poupança bruta.”</i> → ERRADO "
            "(saldo trocado: é a renda disponível bruta)",
        ])],
        "reescrita": ("As contas econômicas integradas compõem o Sistema de Contas Nacionais do Brasil, conforme "
                      "metodologia orientada pela Organização das Nações Unidas (ONU). A conta de distribuição "
                      "primária da renda é constituída pelas contas geração de renda e "
                      + hl("alocação da renda primária") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("RNB é saldo, não conta das CEI. CEI: núcleo do SCN; saldos: produto interno, saldo "
                             "externo, RNB, renda disponível, poupança, patrimônio. Tabela da estrutura das "
                             "contas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 188", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (estrutura de contas e saldos no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01061
    {
        "id": "ECO-E2-L01061-1", "fonte_ref": "E2-L01061", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN_BP,
        "rotulo_item": "Item",
        "assertiva": ("A partir das informações das Tabelas de Recursos e Usos, são preparadas as Contas "
                      "Econômicas Integradas (CEI). Para permitir a visualização da identidade Oferta Total = "
                      "Demanda Total, a Conta de Bens e Serviços utiliza uma convenção contrária ao tradicional "
                      "débito (usos) e crédito (recursos), sendo mostradas as rubricas no centro das contas, os "
                      "recursos à esquerda e os usos à direita."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A partir das informações das Tabelas de Recursos e Usos, são preparadas as Contas "
                      "Econômicas Integradas (CEI). Para permitir a visualização da identidade Oferta Total = "
                      "Demanda Total, a Conta de Bens e Serviços utiliza uma <u>convenção contrária</u> ao "
                      "tradicional débito (usos) e crédito (recursos), sendo mostradas as rubricas no centro das "
                      "contas, os <u>recursos à esquerda e os usos à direita</u>."),
        "poucas": ("A " + azb("conta de bens e serviços") + " apresenta a oferta total por origem (recursos, à "
                   "esquerda) e seu destino pelas categorias de demanda (usos, à direita), com as operações no "
                   "centro — o inverso das demais contas das CEI."),
        "destrinchando": [
            "Objetivo da conta: mostrar " + vd("oferta total = demanda total") + ". Recursos: produção, "
            "importação de bens e serviços, impostos sobre produtos (menos subsídios). Usos: consumo "
            "intermediário, consumo final, formação bruta de capital fixo, variação de estoques e exportação.",
            "Convenção geral das CEI: " + vd("usos à esquerda, recursos à direita") + " (débito × crédito). Na "
            "conta de bens e serviços, a ordem se inverte — " + vd("recursos à esquerda, usos à direita") + " —, "
            "com as rubricas listadas no centro.",
            "As " + azb("Tabelas de Recursos e Usos (TRU)") + " são a base: detalham por produto e por atividade o "
            "que a conta de bens e serviços resume para o total da economia. A TRU é a matriz de onde se "
            "derivam também as matrizes de insumo-produto.",
            "Da identidade da conta sai o PIB pela ótica da despesa: consumo final + FBCF + variação de estoques "
            "+ exportação − importação.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item técnico de apresentação contábil: a banca aposta "
                       "na memória da convenção débito-crédito para fazer o candidato achar que “contrária” é o "
                       "erro. 🔥 O mesmo enunciado é recorrente nos simulados; a versão ERRADA mais provável "
                       "inverte os lados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…sendo mostrados os recursos à direita e os usos à esquerda.”</i> → ERRADO (inversão dos lados)",
            "<i>“Na conta de bens e serviços, o consumo intermediário figura entre os recursos.”</i> → ERRADO "
            "(troca de lado: o consumo intermediário é uso)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Conta de bens e serviços: apresenta a oferta total por origem e o destino pelas "
                             "categorias de demanda. Tabela com o total de recursos."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 189", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (estrutura da conta de bens e serviços no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00933-1 (mesma ideia, Pré-TPS/2024)"],
    },
    # ------------------------------------------------------------------ E2-L01290
    {
        "id": "ECO-E2-L01290-1", "fonte_ref": "E2-L01290", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("A diferença entre o produto nacional (PN) e o produto interno (PI) é dada pela renda líquida "
                      "do exterior. Se a renda enviada ao exterior for maior que a renda recebida do exterior "
                      "então: PI > PN."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A diferença entre o produto nacional (PN) e o produto interno (PI) é dada pela renda "
                      "líquida do exterior. Se a renda enviada ao exterior for <u>maior</u> que a renda recebida do "
                      "exterior então: <u>PI > PN</u>."),
        "poucas": (vd("PN = PI + (RR − RE)") + ". Com RE > RR, o termo entre parênteses é negativo e o produto "
                   "nacional fica abaixo do interno."),
        "destrinchando": [
            azb("Renda líquida do exterior") + " = renda recebida (RR) − renda enviada (RE), registrada na "
            "conta de " + azb("renda primária") + " do balanço de pagamentos: salários de residentes que "
            "trabalham fora, juros, lucros e dividendos.",
            "Fórmulas equivalentes: PNB = PIB + RLRE = PIB − RLEE. Se RE > RR → RLEE > 0 → " + vd("PNB < PIB")
            + ".",
            "A mesma relação vale em termos líquidos (PNL × PIL) e a custo de fatores: o ajuste interno → "
            "nacional é sempre a renda líquida do exterior, independente dos demais ajustes.",
            "Caso do " + rx("Brasil") + ": remessas de lucros e dividendos de multinacionais e juros da dívida "
            "externa superam as rendas recebidas; o país é remetente líquido e tem PNB (RNB) menor que o PIB "
            "⏳ (out/2026).",
            "O quadro da identidade produto = despesa = renda (ótica da produção, da despesa e da renda) mede o "
            "<b>interno</b>; para chegar ao nacional, soma-se a renda líquida do exterior.",
        ],
        "dissecando": (cz("[literalidade]") + " Aplicação direta da fórmula. A dificuldade está só no sinal e "
                       "na notação abreviada (PI, PN). A banca inverte o item trocando “enviada” por “recebida” ou "
                       "o sentido da desigualdade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a renda enviada ao exterior for maior que a renda recebida, o produto nacional supera o "
            "interno.”</i> → ERRADO (sinal trocado)",
            "<i>“A diferença entre produto nacional e interno decorre da depreciação do capital.”</i> → ERRADO "
            "(troca de conceito: depreciação separa bruto de líquido)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PNB = PIB + (RR − RE); se RE > RR, PNB < PIB. Quadro da identidade produto = despesa "
                             "= renda."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 228", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvida (identidade produto = despesa = renda no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01291
    {
        "id": "ECO-E2-L01291-1", "fonte_ref": "E2-L01291", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("Para fins de registro nas Contas Nacionais, o investimento é qualquer gasto em bem ou serviço "
                      "final que aumenta a capacidade da economia de produzir mais no futuro."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para fins de registro nas Contas Nacionais, o investimento é ")
                    + vm("qualquer gasto em bem ou serviço final que aumenta a capacidade da economia de produzir "
                         "mais no futuro") + az(".")),
        "poucas": ("Nas contas nacionais, investimento é uma lista fechada: " + vd("FBCF + variação de estoques")
                   + ". A definição do item é econômica e larga demais — e ainda deixa de fora os estoques."),
        "destrinchando": [
            azb("Formação bruta de capital (FBC)") + " = " + azb("formação bruta de capital fixo") + " (máquinas, "
            "equipamentos, construções, produtos de propriedade intelectual) + " + azb("variação de estoques")
            + ".",
            "A variação de estoques entra no investimento mesmo sem aumentar a capacidade produtiva: é produção "
            "do período que não teve outro uso final. A definição do item não a capta.",
            "O “qualquer” também é largo demais: gastos que elevam a capacidade futura, como educação, saúde e "
            "treinamento (capital humano), são registrados como " + azb("consumo") + " (das famílias ou do "
            "governo), não como investimento.",
            "Também não são investimento no sentido das contas: compra de ações, títulos ou imóveis usados — são "
            "transações com ativos já existentes. O “investimento” do mercado financeiro é aplicação, não FBC.",
            vm("Regra-âncora: investimento nas contas nacionais = FBCF + ΔE, e nada além disso."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O item troca a definição contábil "
                       "(lista fechada: FBCF + estoques) pela intuição econômica (“aumenta a capacidade de "
                       "produzir”), e o “qualquer” a amplia. A expressão “para fins de registro nas Contas "
                       "Nacionais” é a pista: pede o conceito contábil."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nas contas nacionais, o investimento compreende a formação bruta de capital fixo e a variação "
            "de estoques.”</i> → CERTO",
            "<i>“Os gastos das famílias com educação são registrados como investimento, por elevarem o capital "
            "humano.”</i> → ERRADO (troca de conceito: são consumo final)",
        ])],
        "reescrita": ("Para fins de registro nas Contas Nacionais, o investimento é " + hl("a formação bruta de "
                                                                                           "capital fixo mais a "
                                                                                           "variação de "
                                                                                           "estoques") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["qualquer"], "dificuldade": 2,
        "comentario_fonte": "Investimento inclui também a variação de estoques: I = FBCF + variação de estoques.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01292
    {
        "id": "ECO-E2-L01292-1", "fonte_ref": "E2-L01292", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("Produto interno bruto é igual ao valor bruto da produção, a preços básicos, menos o consumo "
                      "intermediário, a preços de consumidor, mais os impostos, líquidos de subsídios, sobre "
                      "produtos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Produto interno bruto é igual ao valor bruto da produção, a <u>preços básicos</u>, menos o "
                      "consumo intermediário, a <u>preços de consumidor</u>, mais os impostos, líquidos de "
                      "subsídios, sobre produtos."),
        "poucas": ("É a definição do IBGE pela " + azb("ótica da produção") + ": " + vd("PIB = VBP (preços "
                                                                                        "básicos) − CI (preços "
                                                                                        "de consumidor) + "
                                                                                        "impostos líquidos sobre "
                                                                                        "produtos") + "."),
        "destrinchando": [
            azb("Preço básico") + " = o que o produtor efetivamente recebe por unidade: sem os impostos sobre "
            "produtos (ICMS, IPI, ISS, PIS/Cofins, imposto de importação), com os subsídios sobre produtos. "
            + azb("Preço de consumidor") + " (ou de comprador) = o que o comprador paga: com impostos e margens "
            "de comércio e transporte.",
            "Por que valorações diferentes: o produtor recebe preço básico pelo que vende, mas paga preço de "
            "consumidor pelos insumos que compra. Assim, o VA a preços básicos (VBP − CI) já sai líquido dos "
            "impostos embutidos nos insumos.",
            "Para chegar ao PIB a " + azb("preços de mercado") + ", soma-se o que falta: os " + vd("impostos, "
                                                                                                   "líquidos de "
                                                                                                   "subsídios, "
                                                                                                   "sobre produtos")
            + ". Os demais impostos sobre a produção (IPTU de fábrica, taxas) já estão no VBP a preços básicos.",
            "Escada de valorações: preço básico + impostos líquidos sobre produtos = preço de mercado. A "
            + azb("custo de fatores") + ", tiram-se também os outros impostos líquidos sobre a produção — fica "
            "só a remuneração dos fatores.",
            vm("Regra-âncora: VBP a preços básicos; CI a preços de consumidor; impostos sobre produtos somados "
               "no fim."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Cópia do glossário do IBGE. A armadilha é a "
                       "aparente incoerência de valorar VBP e CI a preços diferentes; quem não conhece o "
                       "conceito de preço básico tende a marcar ERRADO. Versões ERRADAS trocam as valorações "
                       "ou omitem os impostos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Produto interno bruto é igual ao valor bruto da produção, a preços básicos, menos o consumo "
            "intermediário, a preços de consumidor.”</i> → ERRADO (omissão: sem os impostos líquidos sobre "
            "produtos, isso é o valor adicionado a preços básicos)",
            "<i>“O PIB a custo de fatores é o PIB a preços de mercado menos os impostos indiretos, mais os "
            "subsídios.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Definição do PIB pela ótica da produção; consumo intermediário valorado a preços de "
                             "consumidor (glossário do IBGE)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01293
    {
        "id": "ECO-E2-L01293-1", "fonte_ref": "E2-L01293", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("O produto interno bruto é igual à remuneração dos empregados, mais o total dos impostos, "
                      "líquidos de subsídios, sobre a produção e a importação, mais o rendimento misto bruto, mais "
                      "o excedente operacional bruto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O produto interno bruto é igual à remuneração dos empregados, mais o <u>total</u> dos "
                      "impostos, líquidos de subsídios, sobre a produção e a importação, mais o rendimento misto "
                      "bruto, mais o excedente operacional bruto."),
        "poucas": ("É o PIB pela " + azb("ótica da renda") + ": tudo o que se produz vira remuneração de "
                   "alguém — empregados, autônomos (rendimento misto), capital (excedente operacional) e "
                   "governo (impostos líquidos)."),
        "destrinchando": [
            "Componentes: " + azb("remuneração dos empregados") + " (salários e contribuições sociais); "
            + azb("rendimento misto bruto") + " (renda dos autônomos e empresas familiares, em que não se separa "
            "salário de lucro); " + azb("excedente operacional bruto") + " (lucros, juros, aluguéis, inclusive "
            "o aluguel imputado, e a depreciação, por ser bruto); " + vd("impostos líquidos de subsídios sobre "
                                                                         "a produção e a importação") + ".",
            "Por que o <b>total</b> dos impostos: na ótica da renda, parte do valor do PIB a preços de mercado "
            "fica com o governo. Entram tanto os impostos sobre produtos (ICMS, IPI) quanto os demais impostos "
            "sobre a produção (IPTU de estabelecimentos, taxas) — diferentemente da ótica da produção, que soma "
            "só os impostos sobre produtos porque os outros já estão no VBP a preços básicos.",
            "É a conta de " + azb("geração da renda") + " das CEI: o valor adicionado é repartido entre "
            "trabalho, governo e capital; o saldo é o excedente operacional e o rendimento misto.",
            "Identidade fundamental: " + vd("produto = despesa = renda") + ". As três óticas chegam ao mesmo PIB; "
            "no Brasil, o IBGE concilia as três nas TRU.",
        ],
        "dissecando": (cz("[literalidade]") + " Reprodução do glossário do IBGE. Itens desse tipo erram "
                       "trocando “bruto” por “líquido” (o excedente bruto inclui a depreciação) ou restringindo "
                       "os impostos a “sobre produtos”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB é igual à remuneração dos empregados, mais o excedente operacional líquido, mais o "
            "rendimento misto líquido.”</i> → ERRADO (troca de conceito: faltam a depreciação e os impostos "
            "líquidos)",
            "<i>“Pela ótica da renda, o PIB inclui o excedente operacional bruto, no qual se registra o aluguel "
            "imputado dos imóveis ocupados pelos proprietários.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Definição do PIB sob a ótica da renda.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01294
    {
        "id": "ECO-E2-L01294-1", "fonte_ref": "E2-L01294", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AGREG_CN_BP,
        "rotulo_item": "Item",
        "assertiva": "Países com a renda líquida enviada ao exterior negativa possuem um PNB maior do que o PIB.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Países com a renda líquida enviada ao exterior <u>negativa</u> possuem um PNB "
                      "<u>maior</u> do que o PIB."),
        "poucas": (vd("PNB = PIB − RLEE") + ". Se a " + azb("renda líquida enviada") + " é negativa, o país "
                   "recebe mais do que envia — o PNB supera o PIB."),
        "destrinchando": [
            "RLEE = renda enviada − renda recebida (RE − RR); RLRE = RR − RE = −RLEE. São a mesma grandeza com "
            "sinais opostos.",
            "PNB = PIB − RLEE = PIB + RLRE. Com " + vd("RLEE < 0") + ", subtrair um número negativo equivale "
            "a somar: " + vd("PNB > PIB") + ".",
            "Dupla negação é o truque: “enviada negativa” = “recebida positiva”. Traduza sempre para a forma "
            "positiva antes de julgar.",
            "Na prática, PNB > PIB aparece em economias com grandes ativos no exterior (renda de investimentos) "
            "ou com muitos trabalhadores no exterior que remetem salários; o " + rx("Brasil") + " está no caso "
            "oposto (RLEE positiva).",
            vm("Regra-âncora: RLEE > 0 → PNB < PIB; RLEE < 0 → PNB > PIB."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " O item usa a dupla negação (“enviada” + “negativa”) para "
                       "induzir ao erro de sinal; quem lê “enviada” e conclui “PNB menor” sem processar o "
                       "“negativa” marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Países com renda líquida recebida do exterior negativa possuem PNB maior do que o PIB.”</i> → "
            "ERRADO (sinal trocado: RLRE < 0 → PNB < PIB)",
            "<i>“Em países com renda líquida enviada ao exterior positiva, o PIB supera o PNB.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "PNB = PIB − RLEE; RLEE < 0 → PNB > PIB; RLEE = RE − RR.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01297
    {
        "id": "ECO-E2-L01297-1", "fonte_ref": "E2-L01297", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AGREG_CN_BP,
        "rotulo_item": "Item",
        "assertiva": ("A diferença entre Produto Interno Bruto e Produto Nacional Bruto de um país deve-se "
                      "exclusivamente ao pagamento de fatores de produção empregados nesse país que são propriedade "
                      "de não residentes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A diferença entre Produto Interno Bruto e Produto Nacional Bruto de um país deve-se ")
                    + vm("exclusivamente") + az(" ao pagamento de fatores de produção empregados nesse país que "
                                                "são propriedade de não residentes.")),
        "poucas": ("A diferença é a renda " + azb("líquida") + " do exterior: conta o que se " + vd("envia")
                   + " a não residentes e também o que se " + vd("recebe") + " pelos fatores de residentes "
                   "empregados lá fora."),
        "destrinchando": [
            "PIB − PNB = RE − RR = " + azb("renda líquida enviada ao exterior") + ". São duas pernas: rendas "
            "<b>enviadas</b> (salários de estrangeiros que trabalham aqui, lucros e dividendos de multinacionais, "
            "juros pagos a credores externos) e rendas <b>recebidas</b> (o mesmo, no sentido inverso).",
            "Exemplo: uma construtora brasileira que opera em Angola remete lucros ao " + rx("Brasil") + ". Esse "
            "lucro está no PIB angolano, não no brasileiro, mas entra no PNB brasileiro. Sem a perna das rendas "
            "recebidas, não se explicaria por que alguns países têm PNB > PIB.",
            "No balanço de pagamentos (BPM6), ambas as pernas estão na conta de " + azb("renda primária")
            + ": remuneração de empregados e renda de investimentos (direto, em carteira, outros).",
            "Não entram na diferença PIB × PNB: transferências unilaterais (renda secundária — remessas de "
            "emigrantes como doação, ajuda externa), que separam PNB de renda nacional disponível.",
            vm("Regra-âncora: PIB − PNB = rendas enviadas − rendas recebidas; nunca só uma das pernas."),
        ],
        "dissecando": (cz("[restrição indevida]") + " A parte descrita é verdadeira, mas o “exclusivamente” "
                       "corta a outra metade da renda líquida. Em itens de PIB × PNB, procure sempre as duas "
                       "pernas (enviada e recebida)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A diferença entre PIB e PNB deve-se ao saldo entre rendas de fatores enviadas ao exterior e "
            "recebidas do exterior.”</i> → CERTO",
            "<i>“A diferença entre PIB e PNB inclui as doações recebidas do exterior.”</i> → ERRADO (troca de "
            "conceito: doação é renda secundária)",
        ])],
        "reescrita": ("A diferença entre Produto Interno Bruto e Produto Nacional Bruto de um país deve-se "
                      + hl("tanto") + " ao pagamento de fatores de produção empregados nesse país que são "
                      "propriedade de não residentes" + hl(" quanto ao recebimento de rendas de fatores "
                                                            "empregados no exterior que são propriedade de "
                                                            "residentes") + "."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": ("Deve-se também ao pagamento de fatores empregados no exterior que são propriedade "
                             "de residentes; a conta de renda primária registra rendas recebidas e enviadas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01307
    {
        "id": "ECO-E2-L01307-1", "fonte_ref": "E2-L01307", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("O gasto interno não precisa ser igual à produção de bens e serviços. Se o produto fica aquém "
                      "do gasto interno, exportamos a diferença. Assim, as exportações líquidas são positivas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O gasto interno não precisa ser igual à produção de bens e serviços. Se o produto fica "
                       "aquém do gasto interno, ") + vm("exportamos") + az(" a diferença. Assim, as exportações "
                                                                             "líquidas são ")
                    + vm("positivas") + az(".")),
        "poucas": ("Com " + vd("Y < A") + " (produção menor que o gasto interno), a diferença vem de fora: o país "
                   + azb("importa") + " o excesso e as exportações líquidas são " + vd("negativas") + "."),
        "destrinchando": [
            "Na economia aberta: " + vd("Y = C + I + G + NX") + ". Chamando de " + azb("absorção") + " (gasto "
            "interno) A = C + I + G, tem-se " + vd("NX = Y − A") + ".",
            "Se Y > A, o país produz mais do que gasta e vende o excedente ao exterior: NX > 0 (superávit "
            "comercial). Se Y < A, gasta mais do que produz e compra a diferença lá fora: " + vd("NX < 0") + ".",
            "Correspondência financeira: quem gasta mais do que produz precisa de financiamento externo — NX "
            "negativo vem acompanhado de entrada líquida de capital (poupança externa positiva). Daí a "
            "identidade S − I = NX (em economia sem renda líquida do exterior).",
            "A primeira frase do item é correta: em economia aberta, gasto interno e produção podem divergir — "
            "só em economia fechada A = Y obrigatoriamente.",
            "Leitura de política: ajustar um déficit externo exige reduzir a absorção ou elevar a produção "
            "(" + azb("enfoque da absorção") + ", de " + oc("Sidney Alexander") + ", 1952).",
            vm("Regra-âncora: NX = Y − A; produto abaixo do gasto → importação líquida."),
        ],
        "dissecando": (cz("[inversão]") + " A premissa é verdadeira; a conclusão inverte o sentido do fluxo "
                       "(exporta × importa) e, coerentemente, o sinal de NX. Como as duas trocas “combinam”, o "
                       "item parece consistente. Teste: quem gasta mais do que produz precisa comprar de fora."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o produto supera o gasto interno, o país exporta a diferença e as exportações líquidas são "
            "positivas.”</i> → CERTO",
            "<i>“Se o produto fica aquém do gasto interno, o país recorre à poupança externa.”</i> → CERTO",
        ])],
        "reescrita": ("O gasto interno não precisa ser igual à produção de bens e serviços. Se o produto fica aquém "
                      "do gasto interno, " + hl("importamos") + " a diferença. Assim, as exportações líquidas são "
                      + hl("negativas") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Se a produção interna fica aquém dos gastos internos, há importação da diferença; "
                             "afirma, porém, que as exportações líquidas seriam positivas."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem conclui “as exportações líquidas serão positivas”; "
                    "com produto aquém do gasto, NX é negativo — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L01311
    {
        "id": "ECO-E2-L01311-1", "fonte_ref": "E2-L01311", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_ABERTA_BP,
        "rotulo_item": "Item",
        "assertiva": ("A Renda Líquida de Fatores Externos (RLFE) é a remuneração dos ativos pertencentes a "
                      "estrangeiro e se divide em Renda Enviada ao Exterior (RE) e Renda Recebida do Exterior (RR). "
                      "Em países como o Brasil, em que, em geral, o Produto Interno Bruto (PIB) é maior do que o "
                      "Produto Nacional Bruto (PNB), a RR costuma ser maior do que a RE."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Renda Líquida de Fatores Externos (RLFE) é a remuneração dos ativos pertencentes a "
                       "estrangeiro e se divide em Renda Enviada ao Exterior (RE) e Renda Recebida do Exterior "
                       "(RR). Em países como o Brasil, em que, em geral, o Produto Interno Bruto (PIB) é maior do "
                       "que o Produto Nacional Bruto (PNB), a RR costuma ser ") + vm("maior") + az(" do que a RE.")),
        "poucas": ("Se " + vd("PIB > PNB") + ", a renda líquida enviada é positiva: " + vd("RE > RR") + ". O "
                   "item inverte a conclusão."),
        "destrinchando": [
            "PNB = PIB + RR − RE. Se PIB > PNB, então RR − RE < 0, ou seja, " + vd("RE > RR") + ": o país "
            "envia mais renda de fatores do que recebe.",
            "É o caso do " + rx("Brasil") + ": grande estoque de investimento estrangeiro direto (lucros e "
            "dividendos remetidos pelas multinacionais) e de passivos externos (juros), contra um estoque menor "
            "de ativos de residentes no exterior. O déficit em renda primária é componente estrutural do "
            "déficit em transações correntes ⏳ (out/2026).",
            "Sobre a definição: a renda líquida de fatores externos é, a rigor, o <b>saldo</b> entre a "
            "remuneração dos fatores de residentes no exterior (RR) e a dos fatores de não residentes no país "
            "(RE). A formulação do item (“remuneração dos ativos pertencentes a estrangeiro”) é frouxa, mas o "
            "erro que decide o gabarito está no fim.",
            "Atalho de sinal: PIB > PNB ⇔ RE > RR ⇔ RLEE > 0 ⇔ RLRE < 0.",
        ],
        "dissecando": (cz("[inversão]") + " Premissa correta (no Brasil, PIB > PNB) seguida de conclusão "
                       "invertida. A primeira frase, longa e técnica, distrai; o erro está numa única palavra no "
                       "fim (“maior”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No Brasil, em que o PIB costuma superar o PNB, a renda enviada ao exterior costuma ser maior que "
            "a recebida.”</i> → CERTO",
            "<i>“No Brasil, a renda líquida enviada ao exterior costuma ser negativa.”</i> → ERRADO (sinal "
            "trocado: é positiva)",
        ])],
        "reescrita": ("A Renda Líquida de Fatores Externos (RLFE) é a remuneração dos ativos pertencentes a "
                      "estrangeiro e se divide em Renda Enviada ao Exterior (RE) e Renda Recebida do Exterior (RR). "
                      "Em países como o Brasil, em que, em geral, o Produto Interno Bruto (PIB) é maior do que o "
                      "Produto Nacional Bruto (PNB), a RR costuma ser " + hl("menor") + " do que a RE."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["costuma"], "dificuldade": 1,
        "comentario_fonte": ("O erro está no fim: a renda enviada supera a recebida, pois o país remete renda "
                             "ao exterior, sobretudo lucros de multinacionais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01325
    {
        "id": "ECO-E2-L01325-1", "fonte_ref": "E2-L01325", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_IMPORT,
        "rotulo_item": "Item",
        "assertiva": ("O Sistema de Contas Nacionais e o Balanço de Pagamentos calculam parte das transações "
                      "econômicas realizadas no país e do país com o resto do mundo, uma vez que se considera "
                      "inviável calcular certos componentes agregados."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Sistema de Contas Nacionais e o Balanço de Pagamentos calculam ") + vm("parte")
                    + az(" das transações econômicas realizadas no país e do país com o resto do mundo")
                    + vm(", uma vez que se considera inviável calcular certos componentes agregados") + az(".")),
        "poucas": ("O SCN e o BP têm vocação de " + azb("abrangência total") + ": registram todas as transações "
                   "econômicas internas e com o exterior; o que não é observado diretamente é " + azb("estimado")
                   + ", não excluído."),
        "destrinchando": [
            "O " + azb("Sistema de Contas Nacionais") + " (IBGE) registra a totalidade das transações entre "
            "residentes; o " + azb("Balanço de Pagamentos") + " (Banco Central, BPM6) registra a totalidade das "
            "transações entre residentes e não residentes. Juntos, descrevem toda a economia e sua relação com "
            "o resto do mundo.",
            "Princípio da exaustividade: componentes difíceis de medir não são omitidos, são " + azb("imputados")
            + " ou estimados — aluguel imputado de quem mora em imóvel próprio, produção para autoconsumo, "
            "economia informal (estimada a partir de pesquisas domiciliares).",
            "Fronteiras existem, mas são de definição, não de inviabilidade: serviços domésticos não remunerados "
            "das famílias ficam fora da fronteira de produção por convenção; transações ilegais são tratadas "
            "conforme as recomendações do manual.",
            "As identidades (produto = renda = despesa; BP fechando em zero, com erros e omissões) só funcionam "
            "porque o sistema pretende cobrir tudo.",
        ],
        "dissecando": (cz("[restrição indevida · nexo indevido]") + " O item reduz o alcance dos sistemas "
                       "(“parte”) e oferece uma justificativa falsa (“inviável calcular”). Confunde dificuldade "
                       "de medição, resolvida por estimativa, com exclusão do registro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As contas nacionais estimam componentes de difícil observação, como o aluguel imputado.”</i> → "
            "CERTO",
            "<i>“O Balanço de Pagamentos registra apenas as transações do país com o resto do mundo que envolvem "
            "moeda estrangeira.”</i> → ERRADO (restrição indevida: registra também transações sem cobertura "
            "cambial)",
        ])],
        "reescrita": ("O Sistema de Contas Nacionais e o Balanço de Pagamentos calculam " + hl("a totalidade")
                      + " das transações econômicas realizadas no país e do país com o resto do mundo"
                      + "<s>, uma vez que se considera inviável calcular certos componentes agregados</s>" + "."),
        "tipo_erro": ["RESTRICAO", "NEXO_INDEVIDO"], "moduladores": ["parte"], "dificuldade": 1,
        "comentario_fonte": "Esses instrumentos calculam a totalidade das transações econômicas mencionadas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01326
    {
        "id": "ECO-E2-L01326-1", "fonte_ref": "E2-L01326", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_IMPORT,
        "rotulo_item": "Item",
        "assertiva": ("Considerando que o PIB compreende todos os bens e serviços finais produzidos dentro de um "
                      "país em um período de tempo, avaliam-se, para sua mensuração, a produção corrente e a "
                      "transferência de ativos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando que o PIB compreende todos os bens e serviços finais produzidos dentro de um "
                       "país em um período de tempo, ") + vm("avaliam-se") + az(", para sua mensuração, a produção "
                                                                                 "corrente")
                    + vm(" e a transferência de ativos") + az(".")),
        "poucas": ("O PIB mede só a " + azb("produção corrente") + ". A " + azb("transferência de ativos")
                   + " (venda de bens usados, imóveis, ações) apenas muda a propriedade de algo já contado ou não "
                   "produzido."),
        "destrinchando": [
            "Transferência de ativos = troca de propriedade de bens de segunda mão (produzidos e contabilizados "
            "em período anterior) ou de ativos financeiros. Não há produção nova: contá-la seria contar duas "
            "vezes o mesmo bem.",
            "Exemplos fora do PIB: venda de carro usado, de imóvel antigo, de terreno, de ações e títulos. "
            "Dentro do PIB: os <b>serviços</b> associados a essas transações — corretagem, comissão de "
            "concessionária, taxas da corretora de valores —, que são produção do período.",
            "Mesmo critério para as " + azb("transferências de renda") + " (aposentadorias, programas sociais, "
            "doações): redistribuem, não remuneram produção, e por isso não entram no PIB.",
            "A premissa do item (bens e serviços finais produzidos no território, no período) já contém a "
            "resposta: “produzidos” e “no período” excluem o que é só revendido.",
            vm("Regra-âncora: PIB = produção do período; revenda de ativo fica fora, o serviço da revenda fica "
               "dentro."),
        ],
        "dissecando": (cz("[meia-verdade · contradição]") + " A premissa é a definição correta, e o próprio item "
                       "a contradiz ao somar a transferência de ativos. Em item que começa com definição "
                       "correta, confira se o fim é coerente com ela."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A comissão do corretor na venda de um imóvel usado entra no PIB do ano da venda.”</i> → CERTO",
            "<i>“A compra de ações de uma empresa recém-aberta entra no PIB como investimento.”</i> → ERRADO "
            "(troca de conceito: é aplicação financeira, não formação de capital)",
        ])],
        "reescrita": ("Considerando que o PIB compreende todos os bens e serviços finais produzidos dentro de um "
                      "país em um período de tempo, " + hl("avalia-se") + ", para sua mensuração, a produção "
                      "corrente" + hl(", e não a transferência de ativos") + "."),
        "tipo_erro": ["MEIA_VERDADE", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A transferência de ativos é a venda de bens de segunda mão, produzidos e "
                             "contabilizados em período anterior."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01327
    {
        "id": "ECO-E2-L01327-1", "fonte_ref": "E2-L01327", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_IMPORT,
        "rotulo_item": "Item",
        "assertiva": ("A contabilidade nacional, ao corresponder apenas a variáveis de fluxo, não contabiliza as "
                      "chamadas variáveis de estoque, como nível de emprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A contabilidade nacional, ao corresponder <u>apenas</u> a variáveis de fluxo, não "
                      "contabiliza as chamadas variáveis de estoque, como nível de emprego."),
        "poucas": ("No modelo básico de contabilidade social, os agregados (produto, renda, consumo, "
                   "exportações) são " + azb("fluxos") + " medidos por período; " + azb("estoques") + ", como o "
                   "nível de emprego ou de capital, medidos em uma data, ficam fora."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o CERTO vale para o modelo simplificado dos manuais introdutórios. O SCN 2008 "
                          "completo inclui " + azb("contas de patrimônio") + " (estoques de ativos e passivos), e "
                          "o IBGE divulga, com as contas, o número de ocupações por atividade. Em prova de alto "
                          "nível, o “apenas a variáveis de fluxo” poderia ser julgado ERRADO; aqui prevalece o "
                          "gabarito da fonte.")],
        "destrinchando": [
            azb("Fluxo") + " = grandeza medida <b>por unidade de tempo</b> (PIB do ano, consumo do trimestre, "
            "investimento, exportações). " + azb("Estoque") + " = grandeza medida <b>em um instante</b> "
            "(estoque de capital em 31/12, dívida pública, reservas internacionais, população, número de "
            "empregados).",
            "Fluxos alteram estoques: o investimento (fluxo) aumenta o estoque de capital; o déficit nominal "
            "(fluxo) aumenta a dívida; as contratações líquidas (fluxo) alteram o nível de emprego.",
            "As identidades básicas — produto = renda = despesa, S = I, S − I = TC — são todas relações entre "
            "fluxos do mesmo período. Por isso a contabilidade social dos manuais é descrita como um sistema de "
            "fluxos.",
            "Pegadinha clássica: “variação de estoques” entra no PIB, mas é <b>fluxo</b> (a mudança no período), "
            "não o estoque em si.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item de premissa de manual. O “apenas” e o “não "
                       "contabiliza” soam como modulador absoluto e induzem a marcar ERRADO; a fonte o considera "
                       "verdadeiro no recorte do modelo básico de fluxos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A contabilidade nacional registra o estoque de capital da economia no lugar do "
            "investimento.”</i> → ERRADO (troca de conceito: investimento é o fluxo registrado)",
            "<i>“A variação de estoques, registrada no PIB, é uma variável de fluxo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas"], "dificuldade": 2,
        "comentario_fonte": ("Consideram-se apenas agregados referentes a um período; emprego é variável "
                             "estoque, tomada em um ponto do tempo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: o SCN 2008 completo prevê contas de patrimônio (estoques) e o IBGE divulga "
                    "ocupações; o CERTO só vale no modelo simplificado de fluxos"],
    },
    # ------------------------------------------------------------------ E2-L01328
    {
        "id": "ECO-E2-L01328-1", "fonte_ref": "E2-L01328", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_IMPORT,
        "rotulo_item": "Item",
        "assertiva": ("Na contabilidade nacional, a moeda é considerada apenas como unidade de medida e instrumento "
                      "de trocas; não há, portanto, registro dos agregados monetários, como meios de pagamento, "
                      "empréstimos e aplicações financeiras."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Na contabilidade nacional, a moeda é considerada <u>apenas como unidade de medida e "
                      "instrumento de trocas</u>; não há, portanto, registro dos agregados monetários, como meios "
                      "de pagamento, empréstimos e aplicações financeiras."),
        "poucas": ("As contas nacionais medem " + azb("fluxos reais") + " (produção, renda, despesa); a moeda "
                   "serve para exprimi-los em uma unidade comum. Os " + azb("agregados monetários")
                   + " são estatística do Banco Central, não do sistema de contas básico."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o CERTO vale para o modelo básico de contabilidade social. O manual SCN 2008 completo "
                          "inclui a " + azb("conta financeira") + " (aquisição líquida de ativos e passivos "
                          "financeiros por setor: depósitos, empréstimos, títulos) e as contas de patrimônio. "
                          "Em prova que cobre o SCN completo, o item poderia ser julgado ERRADO; aqui prevalece o "
                          "gabarito da fonte.")],
        "destrinchando": [
            "A contabilidade social nasce para medir a atividade produtiva: quanto se produziu, quanto se "
            "pagou aos fatores, como se gastou. Todos esses fluxos são expressos em moeda, que funciona como "
            + azb("unidade de conta") + " (padrão de medida) e meio de troca.",
            "Transações puramente financeiras — tomar empréstimo, comprar título, depositar no banco — não são "
            "produção nem renda: não entram no PIB. Entram apenas os <b>serviços</b> financeiros (tarifas, "
            "margem de intermediação), que são produção do setor financeiro.",
            "Os " + azb("meios de pagamento") + " (M1, M2, M3, M4) são compilados pelo " + rx("Banco Central do "
                                                                                              "Brasil") + " nas "
            "estatísticas monetárias e de crédito; o PIB e as contas de renda são do IBGE.",
            "Correção conceitual importante: isso não significa que a contabilidade nacional suponha que a "
            "moeda seja “neutra”. Neutralidade é tese teórica sobre os efeitos da moeda no produto; nas contas, "
            "trata-se só de uma escolha de registro.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Premissa de manual introdutório. O “apenas” e o “não "
                       "há registro” convidam a pensar no SCN completo, que tem conta financeira; no recorte "
                       "básico, porém, a afirmação é a tradicional."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na contabilidade nacional, os juros recebidos pelas famílias de aplicações financeiras são "
            "computados no PIB pela ótica da despesa.”</i> → ERRADO (troca de conceito: juros são renda, não "
            "despesa final)",
            "<i>“A compra de títulos públicos por uma família não altera o PIB.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas"], "dificuldade": 2,
        "comentario_fonte": ("Para a contabilidade nacional, a moeda é neutra (apenas mede variáveis reais), pois "
                             "o objetivo é mensurar os agregados reais."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: o SCN 2008 completo tem conta financeira e contas de patrimônio; o CERTO só "
                    "vale no modelo básico",
                    "qualidade_fonte: o comentário de origem fala em moeda “neutra”, confundindo convenção de "
                    "registro com tese teórica — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L01329
    {
        "id": "ECO-E2-L01329-1", "fonte_ref": "E2-L01329", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_RIQUEZA,
        "rotulo_item": "Item",
        "assertiva": ("Sob a ótica do produto nacional, consideram-se bens e serviços finais e excluem-se bens e "
                      "serviços intermediários, como matérias-primas e componentes. Todavia, matérias-primas que "
                      "permanecem em estoque são consideradas bens finais e constam na contabilização do produto "
                      "nacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sob a ótica do produto nacional, consideram-se bens e serviços finais e excluem-se bens e "
                      "serviços intermediários, como matérias-primas e componentes. Todavia, matérias-primas que "
                      "<u>permanecem em estoque</u> são consideradas <u>bens finais</u> e constam na "
                      "contabilização do produto nacional."),
        "poucas": ("O que define bem final é o " + azb("uso no período") + ". Matéria-prima produzida e não "
                   "consumida na produção fica em estoque: é " + azb("investimento em estoques") + ", uso final."),
        "destrinchando": [
            "Bem intermediário = o que é " + azb("consumido") + " no processo produtivo do período, "
            "incorporando-se a outro bem. Se a matéria-prima não foi usada, ela não se incorporou a nada — não "
            "há dupla contagem a evitar.",
            "Por isso, a matéria-prima estocada entra no produto como " + vd("variação de estoques") + ", "
            "componente da formação bruta de capital. No ano seguinte, quando for usada, vira consumo "
            "intermediário, e a variação de estoques daquele ano fica negativa — ela não é contada duas vezes.",
            "Exemplo: siderúrgica produz 100 de aço; a montadora usa 80 e guarda 20. Os 80 estão embutidos no "
            "preço dos carros; os 20 entram no produto como estoque.",
            "A mesma lógica vale para bens finais não vendidos e produtos em elaboração: tudo o que foi "
            "produzido no período aparece em algum uso final.",
            vm("Regra-âncora: final × intermediário depende do uso no período, não da natureza física do bem."),
        ],
        "dissecando": (cz("[contraintuitivo · exceção]") + " O “Todavia” anuncia uma aparente exceção que "
                       "parece contradizer a primeira frase (“matéria-prima é intermediária”), induzindo ao "
                       "ERRADO. Não há contradição: o critério sempre foi o uso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Matérias-primas estocadas são excluídas do produto, por serem bens intermediários por "
            "natureza.”</i> → ERRADO (troca de conceito: o critério é o uso, não a natureza)",
            "<i>“A variação de estoques de matérias-primas integra a formação bruta de capital.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "EXCECAO"], "moduladores": ["Todavia"], "dificuldade": 2,
        "comentario_fonte": ("A utilização do bem importa mais que suas características físicas; matéria-prima "
                             "estocada é bem final, pois não foi usada na produção do período."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01330
    {
        "id": "ECO-E2-L01330-1", "fonte_ref": "E2-L01330", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_RIQUEZA,
        "rotulo_item": "Item",
        "assertiva": ("Sob a ótica da renda nacional, avaliam-se as despesas dos agentes econômicos – "
                      "consumidores, empresas, governo e estrangeiros."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Sob a ótica da ") + vm("renda") + az(" nacional, avaliam-se as despesas dos agentes "
                                                              "econômicos – consumidores, empresas, governo e "
                                                              "estrangeiros.")),
        "poucas": ("Somar as despesas de consumidores, empresas, governo e estrangeiros é a " + azb("ótica da "
                                                                                                     "despesa")
                   + ". A ótica da renda soma as " + azb("remunerações dos fatores") + ": salários, aluguéis, "
                   "juros e lucros."),
        "destrinchando": [
            "Três óticas, um mesmo valor: " + azb("produto") + " (soma dos valores adicionados), "
            + azb("despesa") + " (C + I + G + X − M) e " + azb("renda") + " (salários + aluguéis + juros + "
            "lucros; no SCN, remuneração dos empregados + excedente operacional + rendimento misto + impostos "
            "líquidos sobre produção e importação).",
            "Na ótica da despesa, cada agente corresponde a um componente: consumidores → " + vd("C")
            + "; empresas → " + vd("I") + "; governo → " + vd("G") + "; estrangeiros → " + vd("X − M") + ".",
            "Na ótica da renda, olha-se para quem <b>recebe</b>: trabalhadores, proprietários de terra e "
            "imóveis, credores e empresários. O que é despesa de um é renda de outro — é o " + azb("fluxo "
                                                                                                    "circular")
            + " da renda.",
            "Por isso as três medidas coincidem: todo valor produzido é vendido a alguém (despesa) e se reparte "
            "como remuneração de alguém (renda).",
            vm("Regra-âncora: despesa = quem compra (C, I, G, NX); renda = quem recebe (salários, aluguéis, "
               "juros, lucros)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A descrição é exata — mas da ótica da despesa. O item "
                       "troca só o rótulo da ótica. A lista de agentes (consumidores, empresas, governo, "
                       "estrangeiros) é a pista: são os componentes C, I, G e NX."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob a ótica da renda nacional, somam-se salários, aluguéis, juros e lucros.”</i> → CERTO",
            "<i>“Sob a ótica do produto, somam-se os valores brutos da produção de todas as empresas.”</i> → "
            "ERRADO (dupla contagem: somam-se os valores adicionados)",
        ])],
        "reescrita": ("Sob a ótica da " + hl("despesa") + " nacional, avaliam-se as despesas dos agentes "
                      "econômicos – consumidores, empresas, governo e estrangeiros."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Essa é a ótica da despesa; a renda nacional é a soma dos rendimentos (salários, "
                             "aluguéis, juros e lucros)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01331
    {
        "id": "ECO-E2-L01331-1", "fonte_ref": "E2-L01331", "destino": "17", "subtema": H2["id"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_RIQUEZA,
        "rotulo_item": "Item",
        "assertiva": ("Pela ótica da despesa, os bens finais dividem-se em bens de consumo e bens de investimento, "
                      "os quais serão utilizados como fator de produção para produção de bens de consumo finais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Pela ótica da despesa, os bens finais dividem-se em bens de consumo e <u>bens de "
                      "investimento</u>, os quais serão utilizados como fator de produção para produção de bens de "
                      "consumo finais."),
        "poucas": ("Pelo uso, o bem final é de " + azb("consumo") + " (satisfaz necessidades diretamente) ou de "
                   + azb("investimento") + " (bem de capital que servirá à produção futura). Bem de capital é "
                   "final porque não se incorpora ao produto no período."),
        "destrinchando": [
            "Classificação básica do produto pela despesa: " + vd("Y = C + I") + " na economia fechada e sem "
            "governo; com governo e exterior, acrescentam-se G e X − M, mas os bens continuam sendo, por "
            "natureza do uso, de consumo ou de capital.",
            azb("Bem de capital") + " (máquina, prédio, equipamento) é <b>final</b>: é comprado para ficar e "
            "durar vários períodos, não para ser incorporado a outro bem no ano. Ele se desgasta aos poucos — "
            "a " + azb("depreciação") + " — e ajuda a produzir os bens de consumo futuros.",
            "Contraste com o intermediário: o aço comprado pela montadora some dentro do carro no período "
            "(intermediário); a prensa que estampa as chapas fica na fábrica (capital, final).",
            "Os investimentos totais constituem a " + azb("formação bruta de capital") + ": FBCF (capital "
            "físico) + variação de estoques.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Definição de manual. A armadilha está em "
                       "achar contraditório que um bem “utilizado como fator de produção” seja final; o que "
                       "o torna intermediário seria ser consumido e incorporado no período, não apenas usado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por serem usados na produção de outros bens, os bens de capital são classificados como "
            "intermediários.”</i> → ERRADO (troca de conceito: são finais, pois não se incorporam ao produto)",
            "<i>“Pela ótica da despesa, a aquisição de máquinas pelas empresas integra a formação bruta de capital "
            "fixo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Bens de investimento referem-se aos bens de capital físico; os investimentos totais "
                             "constituem a formação bruta de capital."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
