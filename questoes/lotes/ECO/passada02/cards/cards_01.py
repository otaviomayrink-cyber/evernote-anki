"""Cards do lote de redação 01 — ECO, passada 02 (nota 17: Contas Nacionais)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ident": "🔄 Identidades e óticas do produto",
    "pib": "📏 PIB, PNB, RNB e conceitos derivados",
    "defl": "📊 Nominal × real e deflator",
    "scn": "🧾 SCN e tabelas",
}

CMD_CN = "Julgue o item a seguir, relativo às contas nacionais."
CMD_CN_LISTA = "Com relação às contas nacionais, julgue o item a seguir."
CMD_PIB_CONCEITO = "Julgue o item a seguir, relativo aos conceitos de agregados das contas nacionais."
CMD_OTICAS = "Julgue o item a seguir, relativo às óticas de mensuração do produto nas contas nacionais."
CMD_IDENT_ABERTA = "Julgue o item a seguir, relativo às identidades macroeconômicas de uma economia aberta."
CMD_CLIPPING = "Julgue o item a seguir, relativo à mensuração do produto e da renda nacional."
CMD_IBGE = ("O Instituto Brasileiro de Geografia e Estatística (IBGE) detalha a metodologia para registro das "
            "transações internacionais no sistema de contas nacionais. Quanto a esse registro, julgue o item a "
            "seguir.")
CMD_SCN = "Julgue o item a seguir, relativo ao Sistema de Contas Nacionais do Brasil."


def provavel(ano):
    return (f"banca_provavel: CEBRASPE (item de {ano} com marca de prova antiga na fonte, que só traz o ano; "
            "provável IRBr/CACD) — não confirmada")


ALERTA_2022 = ("banca_provavel: prova de 2022 para diplomata, segundo comentário de professor reproduzido na fonte "
               "(provável IRBr/CACD/2022) — banca não confirmada")

ALERTA_2010 = ("banca_confirmada: CEBRASPE — a fonte reproduz a justificativa de anulação do CESPE; órgão e cargo "
               "não informados (provável IRBr/CACD/2010, não confirmado)")


def fig_verso(*refs):
    return [{"ref": r, "tipo_fonte": "GRÁFICO/TEXTO", "lado": "verso",
             "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"} for r in refs]


CARDS = [
    # ------------------------------------------------------------------ E1-0314
    {
        "id": "ECO-E1-0314-1", "fonte_ref": "E1-0314", "destino": "17", "subtema": H2["defl"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_PIB_CONCEITO,
        "rotulo_item": "Item",
        "assertiva": ("O Produto Nacional Bruto (PNB) representa o valor dos bens e serviços finais, em preços "
                      "correntes, e o seu deflator é obtido pela razão entre o PNB nominal e o PNB real."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Produto Nacional Bruto (PNB) representa o valor dos bens e serviços <u>finais</u>, em "
                      "preços correntes, e o seu deflator é obtido pela razão entre o <u>PNB nominal e o PNB "
                      "real</u>."),
        "poucas": ("O PNB nominal é a produção final (de residentes) a " + azb("preços correntes") + "; o real, a "
                   "preços de um ano-base. O " + azb("deflator") + " é " + vd("nominal ÷ real") + " — mede quanto "
                   "do valor nominal é só preço."),
        "destrinchando": [
            azb("PNB") + " = PIB + renda líquida recebida do exterior (ou PIB − " + vd("RLEE") + ", a renda "
            "líquida enviada ao exterior). O PIB olha a produção no território; o PNB, a renda dos "
            "residentes. No SCN 2008 o agregado passou a se chamar " + azb("Renda Nacional Bruta (RNB)") + ".",
            azb("Nominal × real") + ": o valor nominal multiplica as quantidades do ano pelos preços do próprio "
            "ano; o real multiplica as mesmas quantidades pelos preços de um ano-base. Só o real mede variação "
            "de volume.",
            "Deflator implícito = " + vd("nominal ÷ real (× 100)") + ". Exemplo: PNB nominal de 1.100 e real "
            "de 1.000 → deflator " + vd("110") + ": os preços subiram 10% desde o ano-base. Daí "
            "real = nominal ÷ deflator — por isso “deflacionar” uma série.",
            "Como as quantidades são as do ano corrente, o deflator é um índice do tipo " + azb("Paasche")
            + " e cobre toda a produção final (consumo, investimento, exportações), ao contrário do IPCA, que "
            "segue uma cesta fixa de consumo (tipo Laspeyres) e inclui importados.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definição de manual em duas partes. O risco está na "
                       "ordem da razão (nominal sobre real, não o inverso) e em aceitar “bens e serviços "
                       "finais” para o PNB — o que a banca já tratou como essencial na definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o seu deflator é obtido pela razão entre o PNB real e o PNB nominal.”</i> → ERRADO "
            "(inversão: é nominal ÷ real)",
            "<i>“…o PNB representa o valor de todos os bens e serviços, inclusive intermediários…”</i> → ERRADO "
            "(dupla contagem: só bens finais)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PNB = produção dos residentes (PIB menos remessas líquidas de renda ao exterior); o "
                             "deflator corrige o efeito da inflação pela razão nominal/real."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [provavel(2014), "texto_corrigido: “bens e serviço finais” → “bens e serviços finais”"],
    },
    # ------------------------------------------------------------------ E1-0366
    {
        "id": "ECO-E1-0366-1", "fonte_ref": "E1-0366", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "", "ano": 2010, "cacd": False, "errei": True,
        "comando": CMD_PIB_CONCEITO,
        "rotulo_item": "Item",
        "assertiva": ("O produto nacional bruto (PNB) nominal mede o valor da produção aos preços vigentes no "
                      "período em que o produto é produzido; a renda nacional, por sua vez, mede as receitas "
                      "provenientes da venda da produção; logo, desconsiderando-se a depreciação e os impostos, o "
                      "PNB e a renda nacional são, por definição, iguais."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("O produto nacional bruto (PNB) nominal mede ") + vm("o valor da produção")
                    + az(" aos preços vigentes no período em que o produto é produzido; a renda nacional, por sua "
                         "vez, mede as receitas provenientes da venda da produção; logo, desconsiderando-se a "
                         "depreciação e os impostos, o PNB e a renda nacional são, por definição, iguais.")),
        "poucas": ("Era a alternativa dada como correta numa questão de múltipla escolha, mas definia o PNB como "
                   "“valor da produção” sem dizer " + azb("bens e serviços finais") + " — imprecisão que levou o "
                   "CESPE a anular a questão."),
        "condicionais": [("🏛️ Justificativa da banca",
                          cz("O fato de não ter sido especificado, na opção apontada como gabarito, que se tratava "
                             "de valor da produção de bens e serviços finais, comprometeu a precisão da definição "
                             "de produto nacional bruto (PNB), fato suficiente para determinar a anulação da "
                             "questão."))],
        "destrinchando": [
            "“Valor da produção”, sem qualificação, lembra o " + azb("valor bruto da produção (VBP)") + ", que "
            "soma também os bens intermediários e conta o mesmo insumo várias vezes. Os agregados (PIB, PNB) "
            "medem só os " + vd("bens e serviços finais") + " — ou, o que dá no mesmo, a soma dos valores "
            "adicionados.",
            "A conclusão da alternativa é a identidade de manual: " + azb("renda nacional") + " = PNB − "
            "depreciação − impostos indiretos líquidos de subsídios (= produto nacional líquido a custo de "
            "fatores). Descontados depreciação e impostos, produto e renda nacionais coincidem por construção.",
            "Há uma segunda frouxidão: a renda nacional não é “receita de vendas”, e sim a soma das "
            + azb("remunerações dos fatores") + " (salários, juros, aluguéis e lucros) dos residentes. No fluxo "
            "circular simplificado, a receita da venda da produção final é integralmente repartida entre os "
            "fatores — daí a banca ter aceitado a formulação.",
            vm("Regra-âncora: produto = renda = despesa vale para a produção FINAL; definição sem “finais” é "
               "imprecisa."),
        ],
        "dissecando": (cz("[outro: definição incompleta]") + " A alternativa encadeia três afirmações e "
                       "conclui com “logo… por definição”. A falha não está na conclusão, mas na premissa "
                       "inicial, que omite o qualificador “finais” — exatamente o tipo de detalhe que a banca "
                       "costuma cobrar como erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PNB nominal mede o valor dos bens e serviços finais produzidos pelos residentes, aos preços "
            "vigentes no período.”</i> → CERTO",
            "<i>“O PNB e a renda nacional são iguais por definição, mesmo considerando a depreciação e os impostos "
            "indiretos.”</i> → ERRADO (a renda nacional exclui ambos)",
        ])],
        "reescrita": ("O produto nacional bruto (PNB) nominal mede o valor da produção " + hl("de bens e serviços "
                      "finais") + " aos preços vigentes no período em que o produto é produzido; a renda "
                      "nacional, por sua vez, mede as receitas provenientes da venda da produção; logo, "
                      "desconsiderando-se a depreciação e os impostos, o PNB e a renda nacional são, por "
                      "definição, iguais."),
        "tipo_erro": ["OUTRO"], "moduladores": ["por definição"], "dificuldade": 3,
        "comentario_fonte": ("Comentários que tratam a afirmação como falsa (“é o PIB que mede o valor nominal da "
                             "produção”), seguidos da anotação “Item anulado!” e da justificativa do CESPE sobre a "
                             "omissão de “bens e serviços finais” na opção apontada como gabarito."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [ALERTA_2010,
                    "nota_redacao: classificação sugeria ERRADO; a justificativa do CESPE refere-se à opção "
                    "apontada como gabarito que define o PNB sem “bens e serviços finais” — exatamente esta "
                    "afirmação. Card registrado como ANULADO, com o trecho da anulação em vermelho",
                    "qualidade_fonte: comentário de origem diz que só o PIB mede a produção a preços correntes e "
                    "chama a afirmação de falsa, contra o gabarito preliminar"],
    },
    # ------------------------------------------------------------------ E1-0367
    {
        "id": "ECO-E1-0367-1", "fonte_ref": "E1-0367", "destino": "17", "subtema": H2["defl"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "", "ano": 2010, "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo aos índices de preços e ao deflator do produto.",
        "rotulo_item": "Item",
        "assertiva": ("Um aumento no preço dos produtos importados necessariamente causa aumento no deflator do "
                      "produto interno bruto (PIB)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um aumento no preço dos produtos importados ") + vm("necessariamente causa aumento no")
                    + az(" deflator do produto interno bruto (PIB).")),
        "poucas": ("O " + azb("deflator do PIB") + " só mede preços de bens e serviços " + vd("produzidos no "
                   "país") + ". Importado mais caro entra no IPCA, não no deflator — que só sobe se houver "
                   "repasse aos preços domésticos."),
        "condicionais": [("🏛️ Justificativa da banca",
                          cz("A afirmação era uma alternativa de questão de múltipla escolha, considerada errada "
                             "no gabarito preliminar. A questão foi anulada por imprecisão de outra alternativa "
                             "(a apontada como gabarito, que definia o PNB sem mencionar bens e serviços finais), "
                             "o que não altera o julgamento desta."))],
        "destrinchando": [
            "Deflator implícito = PIB nominal ÷ PIB real. Como o PIB é a produção <b>doméstica</b>, os preços que "
            "importam são os dos bens feitos aqui — consumo, investimento, gasto do governo e exportações. Os "
            "importados não fazem parte do PIB (entram com sinal negativo em X − M justamente para serem "
            "excluídos).",
            "Contraste de " + oc("Mankiw") + " (<i>Macroeconomia</i>, cap. 2): se sobe o preço de um carro "
            "importado, o " + azb("IPC") + " sobe (o carro está na cesta do consumidor), mas o deflator não se "
            "mexe. Choque do petróleo num país importador: o IPC sobe mais que o deflator.",
            "Duas outras diferenças: o deflator usa as quantidades correntes (" + azb("Paasche") + "), o IPC "
            "usa cesta fixa (" + azb("Laspeyres") + "); o deflator inclui bens de capital e exportações, que "
            "não estão na cesta do consumidor.",
            "Efeito indireto possível: o " + azb("pass-through") + " — insumos importados mais caros elevam os "
            "custos e, depois, os preços domésticos. Mas é contingente, não “necessário”.",
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O item aplica ao deflator o "
                       "comportamento do índice de preços ao consumidor e o reforça com “necessariamente”. "
                       "Pista: deflator do PIB → só o que é produzido no país."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento no preço dos produtos importados eleva o índice de preços ao consumidor, ainda que "
            "não afete diretamente o deflator do PIB.”</i> → CERTO",
            "<i>“Uma alta no preço das exportações não afeta o deflator do PIB.”</i> → ERRADO (exportações são "
            "produção doméstica e entram no deflator)",
        ])],
        "reescrita": ("Um aumento no preço dos produtos importados " + hl("não afeta diretamente o")
                      + " deflator do produto interno bruto (PIB)."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["necessariamente"], "dificuldade": 2,
        "comentario_fonte": ("Primeira resposta diz “Correta” (pass-through); as seguintes corrigem: o deflator só "
                             "considera bens produzidos internamente; a banca deu ERRADO e a questão (múltipla "
                             "escolha) foi anulada por erro em outra alternativa."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [ALERTA_2010,
                    "qualidade_fonte: a primeira resposta do verso dá a afirmação como correta; corrigido pela "
                    "indicação da própria fonte de que a banca a considerou errada"],
    },
    # ------------------------------------------------------------------ E1-0378
    {
        "id": "ECO-E1-0378-1", "fonte_ref": "E1-0378", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de formação bruta de capital fixo inclui não apenas os investimentos em máquinas "
                      "e equipamentos, mas também os investimentos em imóveis e a variação dos estoques tanto de "
                      "produtos acabados quanto intermediários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O conceito de formação bruta de capital fixo inclui não apenas os investimentos em "
                       "máquinas e equipamentos, mas também os investimentos em imóveis")
                    + vm(" e a variação dos estoques tanto de produtos acabados quanto intermediários") + az(".")),
        "poucas": ("A " + azb("FBCF") + " é só capital <b>fixo</b> (máquinas, construções, software…). A "
                   + azb("variação de estoques") + " é componente à parte: FBC = " + vd("FBCF + ΔE") + "."),
        "destrinchando": [
            "Pela ótica da despesa, o investimento agregado é a " + azb("formação bruta de capital (FBC)")
            + ": " + vd("I = FBCF + variação de estoques") + ". São contas distintas e publicadas "
            "separadamente pelo IBGE; a taxa de investimento que se cita na imprensa (FBCF/PIB) não inclui "
            "estoques.",
            azb("FBCF") + ": aquisição de ativos fixos produzidos, usados repetidamente por mais de um ano — "
            "máquinas e equipamentos, construções (inclusive imóveis residenciais <b>novos</b>), "
            "infraestrutura, ativos cultivados (pomares, rebanhos reprodutores) e produtos de propriedade "
            "intelectual (software, P&amp;D).",
            azb("Variação de estoques") + ": matérias-primas, produtos em elaboração e acabados ainda não "
            "vendidos. Pode ser involuntária (vendas abaixo do esperado) e pode ser <b>negativa</b> "
            "(desestocagem) — a FBCF, não.",
            "Compra de imóvel usado ou de ações não é investimento nas contas nacionais: é troca de ativos já "
            "existentes, sem produção nova.",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Começa certo (máquinas, imóveis) e enxerta "
                       "no fim um componente vizinho, a variação de estoques, que pertence à FBC, não à FBCF. "
                       "🔥 A banca joga com a palavra “fixo”: se não é fixo, não é FBCF."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A formação bruta de capital compreende a formação bruta de capital fixo e a variação de "
            "estoques.”</i> → CERTO",
            "<i>“A aquisição de imóveis usados pelas famílias integra a formação bruta de capital fixo.”</i> → "
            "ERRADO (troca de ativo existente, não produção nova)",
        ])],
        "reescrita": ("O conceito de formação bruta de capital fixo inclui não apenas os investimentos em máquinas "
                      "e equipamentos, mas também os investimentos em imóveis" + hl(", mas não a variação dos "
                      "estoques, que, somada à FBCF, compõe a formação bruta de capital") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["não apenas", "mas também"],
        "dificuldade": 1,
        "comentario_fonte": ("Comentários empilhados: o primeiro afirma (erradamente) que a FBCF considera a "
                             "variação de estoques; os demais corrigem — investimento = FBCF + variação de "
                             "estoques, contas distintas."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [provavel(2013), "duplicata: comentário de E3-L00242 fundido",
                    "qualidade_fonte: a primeira resposta do verso inclui a variação de estoques na FBCF, "
                    "contra o próprio gabarito"],
    },
    # ------------------------------------------------------------------ E1-0379
    {
        "id": "ECO-E1-0379-1", "fonte_ref": "E1-0379", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": True,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("A acumulação de capital é sempre positiva, pois a depreciação de um ativo fixo não pode ser "
                      "maior que o valor do próprio ativo fixo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A acumulação de capital ") + vm("é sempre positiva, pois a depreciação de um ativo fixo "
                                                        "não pode ser maior que o valor do próprio ativo fixo")
                    + az(".")),
        "poucas": ("Acumulação de capital = " + azb("investimento líquido") + " = investimento bruto − "
                   "depreciação. Se a depreciação do <b>estoque</b> supera o investimento do ano, ela é "
                   + vd("negativa") + "."),
        "destrinchando": [
            "Distinção estoque × fluxo: o " + azb("estoque de capital") + " (K) é sempre positivo; a "
            + azb("acumulação") + " é a variação desse estoque no período: " + vd("ΔK = I bruto − D") + ".",
            "A depreciação (" + azb("consumo de capital fixo") + ") incide sobre <b>todo</b> o estoque herdado do "
            "passado — estradas, fábricas, máquinas —, enquanto o investimento bruto é só o fluxo novo do ano. "
            "Exemplo: estoque de 10 trilhões, depreciação de 5% (500 bilhões), investimento bruto de 300 "
            "bilhões → acumulação de " + vd("−200 bilhões") + ".",
            "O argumento do item (uma máquina não perde mais do que vale) é verdadeiro para um ativo isolado, "
            "mas não diz nada sobre o agregado: é uma " + azb("falácia de composição") + ".",
            "Casos reais de investimento líquido negativo: guerras, recessões profundas, economias que deixam de "
            "repor infraestrutura — a economia “come” o próprio capital (descapitalização).",
            vm("Regra-âncora: investimento líquido < 0 sempre que FBC < depreciação."),
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " O “sempre” anuncia a generalização, e a "
                       "justificativa troca o agregado (fluxo da economia) por um ativo individual. A premissa "
                       "é verdadeira; a ligação com a conclusão é que é falsa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A formação bruta de capital fixo não pode ser negativa.”</i> → CERTO",
            "<i>“O investimento líquido é negativo sempre que a variação de estoques for negativa.”</i> → ERRADO "
            "(depende de FBC total frente à depreciação)",
        ])],
        "reescrita": ("A acumulação de capital " + hl("pode ser negativa, pois a depreciação do estoque de capital "
                      "pode superar o investimento bruto do período") + "."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["sempre"], "dificuldade": 2,
        "comentario_fonte": ("Várias respostas: acumulação é variação (não nível) do estoque; pode ser negativa "
                             "quando a depreciação supera o investimento bruto; exemplo numérico e falácia de "
                             "composição. Uma das respostas a trata, imprecisamente, como sinônimo de investimento "
                             "bruto."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [provavel(2013), "duplicata: comentário de E3-L00243 fundido"],
    },
    # ------------------------------------------------------------------ E1-0381
    {
        "id": "ECO-E1-0381-1", "fonte_ref": "E1-0381", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False,
        "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("O produto nacional bruto é obtido pelo somatório do produto interno bruto com a renda "
                      "recebida do exterior, descontadas as importações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O produto nacional bruto é obtido pelo somatório do produto interno bruto com a ")
                    + vm("renda recebida do exterior, descontadas as importações") + az(".")),
        "poucas": (vd("PNB = PIB + renda recebida − renda enviada ao exterior") + ". Importações não entram: "
                   "já foram descontadas no próprio PIB (C + I + G + X − M)."),
        "destrinchando": [
            "PIB = produção no território; " + azb("PNB") + " (hoje " + azb("RNB") + ") = renda dos residentes, "
            "onde quer que gerada. A passagem é só um ajuste de " + azb("titularidade da renda") + ": soma-se o "
            "que residentes recebem do exterior por seus fatores e subtrai-se o que não residentes levam daqui.",
            "Esses fluxos são a " + azb("renda primária") + " do balanço de pagamentos: lucros e dividendos, "
            "juros, salários. Exemplo: dividendos remetidos pela filial de uma multinacional no "
            + rx("Brasil") + " entram no PIB brasileiro, mas saem do PNB.",
            "Fórmula compacta: " + vd("PNB = PIB − RLEE") + " (renda líquida enviada ao exterior). O "
            + rx("Brasil") + ", devedor líquido e receptor de investimento estrangeiro, tem RLEE positiva: "
            "PNB < PIB.",
            "Descontar as importações seria contar o vazamento duas vezes: pela ótica da despesa, M já é "
            "subtraído para tirar do PIB o que foi produzido fora.",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Mistura duas contas com o exterior: renda "
                       "de fatores (ajusta PIB → PNB) e comércio de bens (já dentro do PIB). Além do enxerto das "
                       "importações, falta subtrair a renda <b>enviada</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PNB é obtido somando-se ao PIB a renda líquida recebida do exterior.”</i> → CERTO",
            "<i>“Num país com grande estoque de investimento estrangeiro direto, o PNB tende a superar o "
            "PIB.”</i> → ERRADO (inversão: as remessas de lucros fazem PNB < PIB)",
        ])],
        "reescrita": ("O produto nacional bruto é obtido pelo somatório do produto interno bruto com a "
                      + hl("renda líquida recebida do exterior (renda recebida menos renda enviada)") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PNB = PIB + renda líquida recebida do exterior (ou PIB − RLEE); importações já "
                             "descontadas no PIB pela ótica da despesa; várias respostas repetidas e quadro-resumo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [provavel(2013), "duplicata: comentário de E3-L00244 fundido"],
    },
    # ------------------------------------------------------------------ E1-0383
    {
        "id": "ECO-E1-0383-1", "fonte_ref": "E1-0383", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Clipping", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_CLIPPING,
        "rotulo_item": "Item",
        "assertiva": ("Embora o PIB seja um indicador importante, ele não reflete necessariamente o bem-estar ou a "
                      "qualidade de vida de uma população. O PIB não considera fatores como desigualdade de renda, "
                      "acesso a serviços públicos, poluição ambiental e outros aspectos que podem influenciar o "
                      "bem-estar dos cidadãos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Embora o PIB seja um indicador importante, ele <u>não reflete necessariamente</u> o "
                      "bem-estar ou a qualidade de vida de uma população. O PIB não considera fatores como "
                      "desigualdade de renda, acesso a serviços públicos, poluição ambiental e outros aspectos que "
                      "podem influenciar o bem-estar dos cidadãos."),
        "poucas": ("O PIB mede o " + azb("valor de mercado da produção final") + ", não o bem-estar: ignora "
                   "distribuição, qualidade dos serviços, danos ambientais, lazer e tudo o que não passa pelo "
                   "mercado."),
        "destrinchando": [
            "O PIB soma valores monetários de bens e serviços finais. Daí suas limitações clássicas como medida "
            "de bem-estar: (1) " + azb("distribuição") + " — o PIB per capita é uma média e não muda se a renda "
            "se concentrar; (2) " + azb("gasto × resultado") + " — conta o que se gasta em saúde e educação, não "
            "a saúde e o aprendizado obtidos; (3) " + azb("meio ambiente") + " — desmatamento e poluição podem "
            "<i>aumentar</i> o PIB, e a depleção de recursos naturais não é descontada; (4) "
            + azb("atividades fora do mercado") + " — trabalho doméstico não remunerado, voluntariado e lazer "
            "não entram.",
            "Gastos “defensivos” elevam o PIB sem elevar o bem-estar: reconstruir após um desastre, segurança "
            "privada contra a violência, tratamento de doenças causadas pela poluição.",
            "Alternativas e complementos: " + azb("IDH") + " (PNUD, 1990, idealizado por " + oc("Mahbub ul Haq")
            + " com a abordagem das capacitações de " + oc("Amartya Sen") + ": renda, saúde e educação), Índice "
            "de Progresso Social, PIB verde e o relatório " + oc("Stiglitz-Sen-Fitoussi") + " (2009), que "
            "recomendou olhar renda e consumo das famílias, distribuição e sustentabilidade.",
            "Nada disso torna o PIB inútil: ele segue a melhor medida da " + azb("atividade econômica")
            + " e do ciclo; o erro é tomá-lo como medida de bem-estar.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O “não reflete <b>necessariamente</b>” "
                       "salva o item: ninguém afirma que PIB e bem-estar não se relacionam, só que não se "
                       "confundem. 🔥 Em ECO, versões com “o PIB é o melhor indicador de bem-estar” são ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como o PIB não considera a desigualdade, um aumento da concentração de renda reduz o PIB per "
            "capita.”</i> → ERRADO (o PIB per capita é média: não muda com a distribuição)",
            "<i>“Os gastos com despoluição de um rio são contabilizados no PIB.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["necessariamente", "podem"],
        "dificuldade": 1,
        "comentario_fonte": ("Lista de limitações do PIB (desigualdade, serviços públicos, poluição, lazer e "
                             "aspectos não mercantis) e indicadores alternativos (IDH, IPS, FIB)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0385
    {
        "id": "ECO-E1-0385-1", "fonte_ref": "E1-0385", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Clipping", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_CLIPPING,
        "rotulo_item": "Item",
        "assertiva": "Um produto produzido em 2022 e vendido em 2023 impacta o PIB de 2023.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um produto produzido em 2022 e vendido em 2023 ") + vm("impacta o PIB de 2023") + az("."),
        "poucas": ("O PIB mede a " + azb("produção") + " do período, não as vendas: o bem entra no PIB de "
                   + vd("2022") + " como " + azb("variação de estoques") + "; em 2023, a venda só troca estoque "
                   "por consumo."),
        "destrinchando": [
            "Em 2022, o bem produzido e não vendido é contabilizado como investimento em estoques: "
            + vd("ΔE > 0") + " na ótica da despesa, e o valor adicionado já aparece na ótica da produção.",
            "Em 2023, quando é vendido, o consumo (C) sobe, mas os estoques caem no mesmo valor ("
            + vd("ΔE < 0") + "): efeito líquido " + vd("nulo") + " sobre o PIB de 2023. Sem esse lançamento, o "
            "mesmo bem seria contado duas vezes.",
            "Ressalva fina: se, em 2023, um comerciante presta serviço sobre o bem (transporte, revenda), a "
            + azb("margem de comércio") + " é produção nova de 2023 e entra no PIB desse ano — o bem em si, não.",
            "Mesma lógica para " + azb("bens usados") + " (carro de segunda mão, imóvel antigo): a revenda não "
            "entra no PIB; só a comissão do corretor ou a margem da revendedora.",
            vm("Regra-âncora: o PIB é um fluxo de produção do período; vender estoque antigo não é produzir."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca o critério de produção pelo de venda. O item aposta "
                       "na intuição comercial (“a receita entrou em 2023”). Pista: o PIB é produto, não "
                       "faturamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A venda, em 2023, de um carro produzido em 2022 eleva o consumo das famílias de 2023, mas não o "
            "PIB desse ano.”</i> → CERTO",
            "<i>“A venda de um imóvel usado entra integralmente na formação bruta de capital fixo do ano.”</i> → "
            "ERRADO (bem existente: só a corretagem é produção nova)",
        ])],
        "reescrita": ("Um produto produzido em 2022 e vendido em 2023 " + hl("entra no PIB de 2022 (como variação "
                      "de estoques), e não no de 2023") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O PIB contabiliza o que foi produzido no período, vendido ou não; o bem de 2022 "
                             "entra no PIB de 2022; produtos usados não entram."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0386
    {
        "id": "ECO-E1-0386-1", "fonte_ref": "E1-0386", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado Clipping", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_CLIPPING,
        "rotulo_item": "Item",
        "assertiva": ("As exportações líquidas do país não podem ser usadas como alavanca de crescimento do PIB, "
                      "pois geram vazamento de renda via importações de bens e serviços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As exportações líquidas do país ") + vm("não podem ser usadas como alavanca de crescimento "
                    "do PIB, pois geram vazamento de renda via importações de bens e serviços") + az(".")),
        "poucas": ("Exportações líquidas são componente da " + azb("demanda agregada") + " (Y = C + I + G + "
                   + vd("X − M") + "): seu aumento eleva o PIB. O vazamento por importações reduz o "
                   "multiplicador, mas não anula o efeito."),
        "destrinchando": [
            "Na identidade da despesa, um aumento de X (ou queda de M), com o resto constante, eleva Y "
            "diretamente. Pelo " + azb("multiplicador da economia aberta") + " — " + vd("1 / (1 − c + m)")
            + ", com c = propensão a consumir e m = propensão a importar —, o efeito final é ainda maior que o "
            "impulso inicial.",
            "O " + azb("vazamento") + " é real: parte da renda gerada se gasta com importados e “vaza” para o "
            "exterior. Mas isso só torna o multiplicador menor que o da economia fechada (1/(1 − c)); ele "
            "continua maior que 1.",
            azb("Crescimento liderado por exportações") + " (<i>export-led growth</i>) é estratégia histórica: "
            "Japão no pós-guerra, Tigres Asiáticos, China. Além da demanda, a exportação dá escala, "
            "aprendizado e divisas para importar bens de capital.",
            "Na tradição keynesiano-kaldoriana, a " + azb("lei de Thirlwall") + " (" + oc("Thirlwall") + ", 1979) "
            "vai além: no longo prazo, o crescimento é limitado pelo balanço de pagamentos — a razão entre a "
            "elasticidade-renda das exportações e a das importações.",
        ],
        "dissecando": (cz("[nexo indevido · modulador absoluto]") + " Parte de um fato verdadeiro (há vazamento "
                       "via importações) para uma conclusão absoluta (“não podem”). O vazamento reduz o "
                       "efeito; não o elimina."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a propensão marginal a importar, menor o multiplicador dos gastos autônomos.”</i> "
            "→ CERTO",
            "<i>“Um superávit comercial reduz o PIB, pois parte da produção é enviada ao exterior.”</i> → ERRADO "
            "(X − M > 0 soma ao PIB)",
        ])],
        "reescrita": ("As exportações líquidas do país " + hl("podem ser usadas como alavanca de crescimento do "
                      "PIB, embora parte do estímulo vaze via importações de bens e serviços") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["não podem"], "dificuldade": 1,
        "comentario_fonte": ("Exportações líquidas são componente do PIB pela ótica da demanda; aumentá-las "
                             "eleva o PIB; exemplos como a China; economias de escala e inovação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0394
    {
        "id": "ECO-E1-0394-1", "fonte_ref": "E1-0394", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("No Brasil, o Instituto Brasileiro de Geografia e Estatística é incumbido de apurar o PIB de "
                      "acordo com o System of National Accounts 2008. Uma definição aproximada para tal agregado é "
                      "a soma do valor dos produtos e serviços finais consumidos na economia de um país, medidos a "
                      "preços de atacado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No Brasil, o Instituto Brasileiro de Geografia e Estatística é incumbido de apurar o PIB "
                       "de acordo com o System of National Accounts 2008. Uma definição aproximada para tal "
                       "agregado é a soma do valor dos produtos e serviços finais ") + vm("consumidos")
                    + az(" na economia de um país, medidos a preços de ") + vm("atacado") + az(".")),
        "poucas": ("O PIB soma os bens e serviços finais " + azb("produzidos") + " (não só consumidos), "
                   "avaliados a " + azb("preços de mercado") + " — não a preços de atacado."),
        "destrinchando": [
            "A primeira frase está certa: o " + rx("IBGE") + " calcula o PIB e o Sistema de Contas Nacionais "
            "seguindo o manual da ONU " + azb("SNA 2008") + " (adotado na série com referência 2010).",
            "<b>Produzidos × consumidos</b>: o PIB pela ótica da despesa é C + I + G + X − M. Investimento e "
            "exportações são produção final que não é consumida internamente; restringir o PIB ao consumo "
            "deixaria de fora a formação de capital e as vendas ao exterior.",
            "<b>Preço de mercado × atacado</b>: o PIB a " + azb("preços de mercado") + " inclui os impostos "
            "sobre produtos líquidos de subsídios; o valor adicionado é medido a " + azb("preços básicos")
            + " (o que o produtor recebe). “Preço de atacado” não é critério de valoração das contas nacionais.",
            "Ponte útil: PIB a preços de mercado = valor adicionado a preços básicos + " + vd("impostos "
            "líquidos de subsídios sobre produtos") + ".",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A primeira frase, institucional e correta, "
                       "dá credibilidade; o erro vem em duas palavras da definição. Em definições de PIB, "
                       "confira sempre o verbo (produzidos) e a base de preços (de mercado)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB corresponde à soma dos bens e serviços finais produzidos na economia, avaliados a preços "
            "de mercado.”</i> → CERTO",
            "<i>“O valor adicionado bruto é medido a preços de mercado, e o PIB, a preços básicos.”</i> → ERRADO "
            "(inversão)",
        ])],
        "reescrita": ("No Brasil, o Instituto Brasileiro de Geografia e Estatística é incumbido de apurar o PIB de "
                      "acordo com o System of National Accounts 2008. Uma definição aproximada para tal agregado é "
                      "a soma do valor dos produtos e serviços finais " + hl("produzidos") + " na economia de um "
                      "país, medidos a preços de " + hl("mercado") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O PIB considera os bens finais produzidos, não só consumidos, a preços de mercado.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0395
    {
        "id": "ECO-E1-0395-1", "fonte_ref": "E1-0395", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_SCN,
        "rotulo_item": "Item",
        "assertiva": ("No Sistema de Contas Nacionais do Brasil, a mensuração da Formação Bruta de Capital Fixo se "
                      "baseia, para o setor Governo Geral, no levantamento das despesas de investimentos "
                      "informadas nos planos de contas dos Balanços Orçamentários dos diferentes níveis de governo, "
                      "sendo que para os Governos Estaduais uma fonte utilizada é a Execução Orçamentária dos "
                      "Estados."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No Sistema de Contas Nacionais do Brasil, a mensuração da Formação Bruta de Capital Fixo se "
                      "baseia, para o setor Governo Geral, no levantamento das <u>despesas de investimentos</u> "
                      "informadas nos planos de contas dos <u>Balanços Orçamentários</u> dos diferentes níveis de "
                      "governo, sendo que para os Governos Estaduais uma fonte utilizada é a Execução "
                      "Orçamentária dos Estados."),
        "poucas": ("Para o governo, o " + rx("IBGE") + " estima a " + azb("FBCF") + " pelas despesas de "
                   + azb("investimento") + " registradas na execução orçamentária de cada esfera — União, "
                   "estados e municípios."),
        "destrinchando": [
            "O setor institucional " + azb("governo geral") + " reúne União, estados e municípios (e fundos e "
            "autarquias). Como não há pesquisa empresarial para ele, a fonte natural é a "
            + azb("contabilidade pública") + ": balanços orçamentários e execução orçamentária.",
            "A FBCF do governo vem das despesas classificadas como " + vd("investimentos") + " (obras, "
            "equipamentos), com ajustes para levar a classificação orçamentária ao conceito do SCN — por "
            "exemplo, excluir aquisições de imóveis já existentes e de ativos financeiros, que não são "
            "formação de capital.",
            "Distinções úteis: no orçamento, “inversões financeiras” (compra de participações, concessão de "
            "empréstimos) não são FBCF; e despesa de " + azb("custeio") + " (salários, material de consumo) "
            "vai para o consumo final do governo.",
            "A FBCF pública no " + rx("Brasil") + " é baixa — tipicamente em torno de 2% do PIB nas últimas "
            "décadas ⏳ (out/2026) — e costuma ser a primeira despesa cortada em ajustes fiscais, porque é "
            "discricionária.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item copiado de nota metodológica do IBGE. Não há "
                       "como deduzi-lo; reconhece-se pela coerência: investimento público se mede pela despesa "
                       "de investimento do orçamento. O detalhe nominal (Execução Orçamentária dos Estados) "
                       "intimida, mas é a fonte esperada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A FBCF do governo geral é estimada pelas despesas de custeio registradas nos balanços "
            "orçamentários.”</i> → ERRADO (troca de conceito: custeio vai para o consumo do governo)",
            "<i>“As inversões financeiras do orçamento integram a FBCF do governo.”</i> → ERRADO (ativo "
            "financeiro não é capital fixo)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("A FBCF do governo geral é estimada a partir das despesas com investimentos dos "
                             "balanços orçamentários, como a Execução Orçamentária dos Estados."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0398
    {
        "id": "ECO-E1-0398-1", "fonte_ref": "E1-0398", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_PIB_CONCEITO,
        "rotulo_item": "Item",
        "assertiva": ("O total dos bens e serviços produzidos pelas unidades produtoras residentes do país, "
                      "destinados ao consumo final, corresponde ao conceito de produto interno bruto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O total dos bens e serviços produzidos pelas <u>unidades produtoras residentes</u> do país, "
                      "<u>destinados ao consumo final</u>, corresponde ao conceito de produto interno bruto."),
        "poucas": ("É a definição do " + azb("PIB") + ": produção de " + azb("bens e serviços finais") + " das "
                   "unidades " + azb("residentes") + " — “destinados ao consumo final” quer dizer finais, não "
                   "intermediários."),
        "destrinchando": [
            "Pelo " + azb("SNA 2008") + ", o PIB é a soma do valor adicionado bruto de todas as unidades "
            "produtoras <b>residentes</b> (mais os impostos líquidos sobre produtos) — o que equivale ao valor "
            "dos bens e serviços finais que elas produzem.",
            "“Residente” não é “nacional”: a filial de uma montadora estrangeira instalada aqui é unidade "
            "residente (tem centro de interesse econômico no território) e sua produção entra no PIB. Por isso "
            "se diz que o PIB mede a produção no " + azb("território econômico") + ".",
            "“Destinados ao consumo final” é a forma antiga de dizer " + azb("uso final") + " — por oposição ao "
            + azb("consumo intermediário") + ", que é insumo de outra produção. Uso final inclui consumo das "
            "famílias e do governo, investimento e exportações.",
            "Excluir os intermediários evita a " + azb("dupla contagem") + ": o trigo vendido ao moinho já está "
            "dentro do preço do pão.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Definição clássica, com dois termos que assustam: "
                       "“residentes” (parece PNB) e “consumo final” (parece excluir investimento). Lidos no "
                       "sentido técnico — unidade residente e bem final —, o item fecha. A banca usa o mesmo "
                       "enunciado trocando o agregado no fim (ex.: “poupança bruta”, que é ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O total dos bens e serviços produzidos pelas unidades produtoras residentes, destinados ao "
            "consumo final, corresponde ao conceito de poupança bruta.”</i> → ERRADO (troca de conceito)",
            "<i>“O PIB inclui o valor dos bens intermediários utilizados na produção.”</i> → ERRADO (dupla "
            "contagem)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O PIB representa o valor total dos bens e serviços finais produzidos por unidades "
                             "residentes no território econômico de um país."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0399
    {
        "id": "ECO-E1-0399-1", "fonte_ref": "E1-0399", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_PIB_CONCEITO,
        "rotulo_item": "Item",
        "assertiva": ("O total dos bens e serviços produzidos pelas unidades produtoras residentes do país, "
                      "destinados ao consumo final, corresponde ao conceito de poupança bruta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O total dos bens e serviços produzidos pelas unidades produtoras residentes do país, "
                       "destinados ao consumo final, corresponde ao conceito de ") + vm("poupança bruta") + az(".")),
        "poucas": ("Essa é a definição do " + azb("PIB") + ". A " + azb("poupança bruta") + " é a parte da "
                   "renda disponível " + vd("não consumida") + " — um resíduo, não o total produzido."),
        "destrinchando": [
            "A produção final das unidades residentes (bens e serviços de uso final) é o " + azb("produto "
            "interno bruto") + ".",
            azb("Poupança bruta") + " = renda disponível bruta − consumo final. É o saldo da conta de uso da "
            "renda: o que sobra depois de consumir e que financia a acumulação.",
            "Na conta de capital, a poupança aparece como recurso que financia a " + azb("formação bruta de "
            "capital") + "; numa economia fechada e sem governo, " + vd("S = I = FBCF + ΔE") + ". Na economia "
            "aberta, a diferença entre poupança doméstica e investimento é coberta pela poupança externa.",
            "Ordem de grandeza no " + rx("Brasil") + ": poupança bruta e FBCF giram em torno de 15% a 18% do "
            "PIB ⏳ (out/2026) — o PIB é a base, a poupança é uma fração dele.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O enunciado é a definição do PIB, idêntica palavra por "
                       "palavra; só o agregado do fim foi trocado. Itens assim se resolvem lendo a definição "
                       "até o último termo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A poupança bruta corresponde à parcela da renda disponível bruta não destinada ao consumo "
            "final.”</i> → CERTO",
            "<i>“A poupança bruta corresponde à renda disponível bruta somada ao consumo final.”</i> → ERRADO "
            "(sinal trocado: é renda disponível menos consumo)",
        ])],
        "reescrita": ("O total dos bens e serviços produzidos pelas unidades produtoras residentes do país, "
                      "destinados ao consumo final, corresponde ao conceito de " + hl("produto interno bruto")
                      + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A poupança bruta é o que resta da renda disponível após o consumo final; é fluxo de "
                             "acumulação, não a produção total."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0400
    {
        "id": "ECO-E1-0400-1", "fonte_ref": "E1-0400", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CN_LISTA,
        "rotulo_item": "Item",
        "assertiva": "O Produto Interno Bruto caracteriza o volume de valor adicionado pelos residentes no país.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("O Produto Interno Bruto caracteriza o volume de valor adicionado ") + vm("pelos residentes "
                    "no") + az(" país.")),
        "poucas": ("Na leitura de manual, o " + azb("PIB") + " é o valor adicionado " + azb("no território") + ", "
                   "por quem quer que produza; “dos residentes” remete ao " + azb("PNB/RNB") + ". Daí o "
                   "ERRADO — discutível à luz do SNA."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "pelo " + azb("SNA 2008") + ", o PIB é a soma do valor adicionado bruto das unidades "
                          "produtoras <b>residentes</b> — e “residente” é quem tem centro de interesse econômico "
                          "no território, inclusive a filial de empresa estrangeira. Nesse sentido técnico, a "
                          "frase seria defensável como CERTO. O gabarito ERRADO pressupõe a leitura de "
                          "“residentes” como os titulares da renda (nacionais), critério que define o PNB.")],
        "destrinchando": [
            azb("PIB") + " (critério geográfico): tudo o que é produzido no " + azb("território econômico")
            + ", independentemente da origem do capital ou da nacionalidade dos trabalhadores. A fábrica de "
            "uma multinacional no " + rx("Brasil") + " entra no PIB brasileiro.",
            azb("PNB/RNB") + " (critério da titularidade da renda): PIB + renda recebida do exterior − renda "
            "enviada ao exterior. O lucro dessa fábrica remetido à matriz sai do PNB brasileiro.",
            "A ambiguidade: no SCN, “unidade residente” é justamente a que produz no território econômico de "
            "forma não temporária; por isso “produção dos residentes” e “produção no território” coincidem "
            "para o PIB. A distinção PIB × PNB está na <b>renda</b>, não na produção.",
            "Para a prova, siga o padrão das bancas: PIB → “no território”, “interno”; PNB → “dos "
            "residentes/nacionais”, “renda”.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca o critério territorial do PIB pelo critério "
                       "de titularidade que define o PNB. É uma troca sutil, que depende da acepção de "
                       "“residentes”; por isso o gabarito é contestável."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Produto Interno Bruto corresponde ao valor adicionado no território econômico do país, "
            "independentemente da nacionalidade dos produtores.”</i> → CERTO",
            "<i>“O PNB inclui a produção das filiais estrangeiras instaladas no país, inclusive os lucros "
            "remetidos às matrizes.”</i> → ERRADO (os lucros remetidos saem do PNB)",
        ])],
        "reescrita": ("O Produto Interno Bruto caracteriza o volume de valor adicionado " + hl("no território "
                      "econômico do") + " país."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O PIB mede o valor adicionado no território, independentemente da nacionalidade "
                             "dos produtores."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: pelo SNA 2008 o PIB é o valor adicionado das unidades produtoras residentes; "
                    "o ERRADO da fonte só se sustenta lendo “residentes” como titulares da renda (critério do PNB)",
                    "texto_corrigido: o prefixo “Com relação às Contas Nacionais:” da assertiva foi levado ao "
                    "comando"],
    },
    # ------------------------------------------------------------------ E1-0401
    {
        "id": "ECO-E1-0401-1", "fonte_ref": "E1-0401", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CN_LISTA,
        "rotulo_item": "Item",
        "assertiva": "O Investimento Bruto se decompõe em Formação Bruta de Capital Fixo e Variação de Estoques.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Investimento Bruto se decompõe em <u>Formação Bruta de Capital Fixo</u> e <u>Variação de "
                      "Estoques</u>."),
        "poucas": ("Investimento bruto = " + azb("formação bruta de capital") + " = " + vd("FBCF + variação de "
                   "estoques") + ". Descontada a depreciação, tem-se o investimento líquido."),
        "destrinchando": [
            azb("FBCF") + ": aquisição de ativos fixos produzidos e usados por mais de um ano — máquinas e "
            "equipamentos, construções, infraestrutura, software e P&amp;D, ativos cultivados.",
            azb("Variação de estoques") + ": diferença entre os estoques do fim e do início do período "
            "(matérias-primas, produtos em elaboração e acabados). Pode ser negativa e muitas vezes é "
            "involuntária — é a variável de ajuste quando as vendas surpreendem.",
            "Do bruto ao líquido: " + vd("investimento líquido = investimento bruto − depreciação") + " "
            "(consumo de capital fixo). Só o líquido aumenta o estoque de capital.",
            "Detalhe do manual: no " + azb("SNA 2008") + " a formação bruta de capital tem ainda um terceiro "
            "componente, de peso pequeno, a aquisição líquida de " + azb("objetos de valor") + " (joias, obras "
            "de arte). Nas provas, vale a decomposição em dois.",
            "No PIB pela ótica da despesa, o “I” de C + I + G + X − M é esse investimento bruto: inclui o "
            "investimento do governo, que, nas contas nacionais, não fica em G.",
        ],
        "dissecando": (cz("[literalidade]") + " Identidade de manual. A banca costuma inverter as peças (estoques "
                       "dentro da FBCF) ou trocar bruto por líquido; aqui está tudo no lugar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O investimento líquido se decompõe em formação bruta de capital fixo e variação de "
            "estoques.”</i> → ERRADO (troca de conceito: isso é o bruto; o líquido desconta a depreciação)",
            "<i>“A formação bruta de capital fixo inclui a variação de estoques de produtos acabados.”</i> → "
            "ERRADO (componentes separados)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O investimento bruto (formação bruta de capital) compõe-se de FBCF e variação de "
                             "estoques."),
        "qualidade_fonte": "raso",
        "figuras_fonte": fig_verso("Untitled (89).jpeg"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0403
    {
        "id": "ECO-E1-0403-1", "fonte_ref": "E1-0403", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("Nas contas nacionais, ao considerarmos a conta de capital em uma economia fechada e sem "
                      "governo, a poupança bruta se apresenta como contrapartida das variações ativas dadas pela "
                      "formação bruta de capital fixo mais a variação de estoques."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Nas contas nacionais, ao considerarmos a conta de capital em uma <u>economia fechada e sem "
                      "governo</u>, a poupança bruta se apresenta como contrapartida das variações ativas dadas "
                      "pela formação bruta de capital fixo mais a variação de estoques."),
        "poucas": ("Na " + azb("conta de capital") + ", a poupança bruta é o recurso que financia a acumulação. "
                   "Fechada e sem governo, não há outra fonte: " + vd("S = FBCF + ΔE = I") + "."),
        "destrinchando": [
            "A " + azb("conta de capital") + " registra, de um lado, as <b>variações do patrimônio líquido</b> "
            "(poupança bruta e transferências de capital) e, do outro, as <b>variações dos ativos</b> não "
            "financeiros (FBCF, variação de estoques). O saldo é a capacidade ou necessidade de financiamento.",
            "Economia fechada e sem governo: Y = C + I e Y = C + S, logo " + vd("S = I") + ". Toda a poupança "
            "das famílias e empresas é a contrapartida contábil do investimento bruto.",
            "Com governo: " + vd("I = S privada + (T − G)") + ". Com setor externo: soma-se a "
            + azb("poupança externa") + " (déficit em transações correntes). A identidade vale sempre <i>ex "
            "post</i>; o ajuste, nos modelos, se dá por renda (" + oc("Keynes") + ") ou por juros (clássicos).",
            "É uma identidade contábil, não uma teoria de causalidade: diz que os dois lados são iguais, não "
            "quem determina quem.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Linguagem de manual de SCN (“contrapartida das "
                       "variações ativas”). As condições “fechada e sem governo” são o que torna a igualdade "
                       "exata; o risco é desconfiar do jargão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Numa economia aberta e com governo, a poupança privada bruta é sempre igual à formação bruta de "
            "capital.”</i> → ERRADO (faltam poupança do governo e poupança externa)",
            "<i>“Numa economia fechada e sem governo, a poupança bruta é igual ao investimento bruto.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Em economia fechada e sem governo, a poupança bruta é igual ao investimento bruto "
                             "(FBCF + variação de estoques)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": fig_verso("Untitled (87).jpeg", "Untitled (88).jpeg"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0404
    {
        "id": "ECO-E1-0404-1", "fonte_ref": "E1-0404", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_OTICAS,
        "rotulo_item": "Item",
        "assertiva": ("Nas contas nacionais, o valor do Produto Interno Bruto − PIB pode ser visto sob as óticas da "
                      "produção, da demanda e da renda. Quando expressa a produção, o valor é igual à despesa de "
                      "consumo das famílias, mais o consumo do governo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nas contas nacionais, o valor do Produto Interno Bruto − PIB pode ser visto sob as óticas "
                       "da produção, da demanda e da renda. Quando expressa a produção, o valor é igual ")
                    + vm("à despesa de consumo das famílias, mais o consumo do governo") + az(".")),
        "poucas": ("Consumo das famílias e do governo são parcelas da " + azb("ótica da despesa") + " (e "
                   "incompleta). Pela " + azb("ótica da produção") + ", o PIB é o " + vd("VBP − consumo "
                   "intermediário + impostos líquidos sobre produtos") + "."),
        "destrinchando": [
            "As três óticas medem o mesmo fluxo por caminhos diferentes:",
            "<b>Produção</b>: soma dos " + azb("valores adicionados") + ": VBP a preços básicos − consumo "
            "intermediário + impostos líquidos de subsídios sobre produtos = PIB a preços de mercado.",
            "<b>Despesa (demanda)</b>: " + vd("C + G + FBCF + ΔE + X − M") + ". Consumo das famílias e do "
            "governo são só duas das parcelas; faltam investimento e exportações líquidas.",
            "<b>Renda</b>: remuneração dos empregados + excedente operacional bruto e rendimento misto + "
            "impostos líquidos sobre produção e importação.",
            "A resposta dada pelo item não serve nem para a ótica da demanda: C + G mede apenas o "
            + azb("consumo final") + " da economia.",
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " A primeira frase é correta e anuncia as três "
                       "óticas; a segunda atribui à ótica da produção um pedaço da ótica da despesa. Pista: "
                       "“produção” pede valor adicionado, nunca “despesa”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando expressa a produção, o valor é igual ao valor bruto da produção, a preços básicos, menos "
            "o consumo intermediário, a preços de consumidor, mais os impostos, líquidos de subsídios, sobre "
            "produtos.”</i> → CERTO",
            "<i>“Quando expressa a renda, o PIB é igual à soma do consumo final com a formação bruta de "
            "capital.”</i> → ERRADO (troca de ótica: isso é despesa, e ainda sem X − M)",
        ])],
        "reescrita": ("Nas contas nacionais, o valor do Produto Interno Bruto − PIB pode ser visto sob as óticas "
                      "da produção, da demanda e da renda. Quando expressa a produção, o valor é igual "
                      + hl("ao valor bruto da produção menos o consumo intermediário, mais os impostos, líquidos "
                           "de subsídios, sobre produtos") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Descrição parcial da ótica da demanda, não da produção; pela produção, o PIB é "
                             "apurado a partir do valor adicionado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": fig_verso("Untitled (90).jpeg"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0405
    {
        "id": "ECO-E1-0405-1", "fonte_ref": "E1-0405", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_OTICAS,
        "rotulo_item": "Item",
        "assertiva": ("Nas contas nacionais, o valor do Produto Interno Bruto − PIB pode ser visto sob as óticas da "
                      "produção, da demanda e da renda. Quando expressa a produção, o valor é igual ao valor bruto "
                      "da produção, a preços básicos, menos o consumo intermediário, a preços de consumidor, mais "
                      "os impostos, líquidos de subsídios, sobre produtos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Nas contas nacionais, o valor do Produto Interno Bruto − PIB pode ser visto sob as óticas "
                      "da produção, da demanda e da renda. Quando expressa a produção, o valor é igual ao valor "
                      "bruto da produção, <u>a preços básicos</u>, menos o consumo intermediário, <u>a preços de "
                      "consumidor</u>, mais os impostos, líquidos de subsídios, sobre produtos."),
        "poucas": ("É a fórmula do " + rx("IBGE") + ": " + vd("PIB = VBP (preços básicos) − CI (preços de "
                   "consumidor) + impostos líquidos sobre produtos") + ". As duas bases de preço diferentes são "
                   "corretas."),
        "destrinchando": [
            azb("VBP a preços básicos") + ": o que o produtor recebe por unidade, sem impostos sobre produtos "
            "e com os subsídios. É a ótica do vendedor.",
            azb("Consumo intermediário a preços de consumidor") + " (de comprador): o que a empresa paga pelos "
            "insumos, com impostos e margens de comércio e transporte. É a ótica de quem compra.",
            "VBP − CI = " + azb("valor adicionado bruto") + " a preços básicos. Para chegar ao PIB a "
            + azb("preços de mercado") + ", somam-se os " + vd("impostos sobre produtos líquidos de subsídios")
            + " (ICMS, IPI, PIS/Cofins, imposto de importação), que estão nos preços pagos pelos usuários finais "
            "mas não no VBP a preços básicos.",
            "A mistura de bases (básicos na produção, consumidor nos insumos) é o que garante que o PIB pela "
            "produção bata com o PIB pela despesa, que é avaliado a preços de comprador.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Reproduz a nota metodológica do IBGE. A "
                       "assimetria de preços (básicos × consumidor) parece erro proposital e induz a marcar "
                       "ERRADO; é justamente o detalhe que está certo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o valor bruto da produção, a preços básicos, menos o consumo intermediário, a preços básicos, "
            "sem a soma de impostos…”</i> → ERRADO (isso dá o valor adicionado a preços básicos, não o PIB a "
            "preços de mercado)",
            "<i>“Quando expressa a produção, o valor é igual à despesa de consumo das famílias mais o consumo do "
            "governo.”</i> → ERRADO (troca de ótica)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("VBP − CI = valor adicionado bruto; somam-se os impostos líquidos de subsídios sobre "
                             "produtos para chegar ao PIB a preços de mercado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0406
    {
        "id": "ECO-E1-0406-1", "fonte_ref": "E1-0406", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_PIB_CONCEITO,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de produto interno bruto considera, como unidade residente, aquela que mantém o "
                      "centro de interesse econômico predominante no território econômico, realizando, sem "
                      "caráter temporário, atividades econômicas nesse território."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O conceito de produto interno bruto considera, como unidade residente, aquela que mantém o "
                      "<u>centro de interesse econômico predominante</u> no território econômico, realizando, "
                      "<u>sem caráter temporário</u>, atividades econômicas nesse território."),
        "poucas": ("" + azb("Residência") + " no SCN não depende de nacionalidade nem de cidadania: é ter o "
                   "centro de interesse econômico predominante no território, de forma " + vd("não temporária")
                   + "."),
        "destrinchando": [
            "Critério do " + azb("SNA 2008") + " e do BPM6: uma unidade é residente onde tem seu " + azb("centro "
            "de interesse econômico predominante") + " — onde produz, consome ou mantém ativos de forma "
            "duradoura. Como regra prática, a referência é " + vd("um ano ou mais") + ".",
            "Exemplos: a filial de uma empresa estrangeira instalada no " + rx("Brasil") + " é residente no "
            "Brasil; o turista estrangeiro e o trabalhador sazonal não são; o estudante no exterior continua "
            "residente do país de origem; embaixadas são extraterritoriais e pertencem à economia do país "
            "que representam.",
            azb("Território econômico") + " é mais amplo que o geográfico: inclui espaço aéreo, águas "
            "territoriais, zonas francas e enclaves no exterior (embaixadas, bases), e exclui os enclaves "
            "estrangeiros dentro do país.",
            "O conceito separa os agregados: o " + azb("PIB") + " soma o valor adicionado das unidades "
            "residentes; o " + azb("balanço de pagamentos") + " registra as transações entre residentes e não "
            "residentes.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição do manual quase literal. Os qualificadores "
                       "“predominante” e “sem caráter temporário” estão corretos; a banca costuma errar "
                       "trocando residência por nacionalidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Considera-se unidade residente aquela cujo capital pertence a nacionais do país.”</i> → ERRADO "
            "(troca de conceito: residência ≠ nacionalidade)",
            "<i>“A filial de uma montadora estrangeira instalada no país é unidade residente, e sua produção "
            "integra o PIB.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Pelo SNA, unidade residente é a que mantém o centro de interesse econômico no país, "
                             "com atividade não temporária."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0407
    {
        "id": "ECO-E1-0407-1", "fonte_ref": "E1-0407", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_IDENT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Ao considerar a igualdade “I = S + (T – G) + (M – X)”, a expressão “(M − X)” representa uma "
                      "contribuição positiva ao volume de investimentos quando as exportações são maiores que as "
                      "importações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Ao considerar a igualdade “I = S + (T – G) + (M – X)”, a expressão “(M − X)” representa "
                       "uma contribuição positiva ao volume de investimentos quando ")
                    + vm("as exportações são maiores que as importações") + az(".")),
        "poucas": ("(M − X) é a " + azb("poupança externa") + ". Ela só é positiva — e só soma ao investimento — "
                   "quando " + vd("M > X") + " (déficit externo). Com X > M, é negativa: o país empresta ao "
                   "resto do mundo."),
        "destrinchando": [
            "Dedução: Y = C + I + G + X − M e Y = C + S + T (renda vai para consumo, poupança privada e "
            "impostos). Igualando: " + vd("I = S + (T − G) + (M − X)") + " — investimento = poupança privada + "
            "poupança do governo + " + azb("poupança externa") + ".",
            "Se " + vd("M > X") + ", o país absorve mais bens do que produz para fora; o excesso é financiado "
            "pelo exterior, e a poupança externa positiva permite investir além da poupança doméstica.",
            "Se " + vd("X > M") + ", (M − X) < 0: parte da poupança doméstica financia o resto do mundo, e o "
            "investimento interno fica <b>menor</b> que a poupança doméstica — caso de exportadores líquidos "
            "como China e Alemanha.",
            "Com rendas e transferências, a medida exata da poupança externa é o " + azb("déficit em transações "
            "correntes") + "; com M − X, o modelo usa só a balança de bens e serviços.",
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sinal da condição. Teste rápido: substitua números (X = "
                       "10, M = 5 → M − X = −5, o termo <b>reduz</b> o investimento). 🔥 Identidades com sinal "
                       "trocado são clássico de banca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a expressão (M − X) representa uma contribuição positiva ao investimento quando as importações "
            "superam as exportações.”</i> → CERTO",
            "<i>“Um superávit fiscal (T > G) reduz o volume de investimento possível, dada a identidade.”</i> → "
            "ERRADO (T − G > 0 é poupança pública e soma ao investimento)",
        ])],
        "reescrita": ("Ao considerar a igualdade “I = S + (T – G) + (M – X)”, a expressão “(M − X)” representa uma "
                      "contribuição positiva ao volume de investimentos quando " + hl("as importações são maiores "
                      "que as exportações") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Com X > M, (M − X) é negativo: há contribuição da economia local ao resto do mundo; "
                             "a contribuição positiva ao investimento ocorre com M > X (déficit comercial)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0408
    {
        "id": "ECO-E1-0408-1", "fonte_ref": "E1-0408", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_IDENT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Ao considerar a igualdade “I = S + (T – G) + (M – X)”, a expressão “(M − X)” representa uma "
                      "transferência de poupança da economia local para o resto do mundo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Ao considerar a igualdade “I = S + (T – G) + (M – X)”, a expressão “(M − X)” representa "
                       "uma <u>transferência de poupança da economia local para o resto do mundo</u>.")),
        "poucas": ("Gabarito da fonte: CERTO, lendo (M − X) como a " + azb("transferência líquida de poupança") +
                   " entre a economia local e o resto do mundo. Pelo rigor da identidade, porém, (M − X) > 0 é "
                   "poupança que vem " + vd("do resto do mundo para a economia local") + " — ver ⚠️."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "mantido o CERTO da fonte, que lê (M − X) genericamente como “transferência líquida de "
                          "poupança entre países”. Mas o termo entra na identidade <b>somando</b> ao "
                          "investimento: positivo, é poupança que o resto do mundo transfere à economia local; "
                          "a transferência da economia local para o exterior corresponde a (X − M) > 0. A "
                          "resposta mais defensável é ERRADO, e a formulação rigorosa seria: <i>“(M − X) "
                          "representa uma transferência de poupança do resto do mundo para a economia "
                          "local”</i>.")],
        "destrinchando": [
            "Da identidade: " + vd("I = S privada + (T − G) + (M − X)") + ". Cada parcela é uma fonte de "
            "financiamento do investimento: poupança privada, do governo e " + azb("externa") + ".",
            "Com " + vd("M > X") + ", o país gasta mais do que produz e cobre a diferença com recursos de fora "
            "(dívida, investimento estrangeiro): o resto do mundo transfere poupança para cá. É o caso típico "
            "do " + rx("Brasil") + ", com déficit em transações correntes financiado por investimento direto.",
            "Com " + vd("X > M") + ", (M − X) é negativo: a economia local poupa mais do que investe e empresta "
            "a diferença ao exterior — aí, sim, há transferência da economia local para o resto do mundo, mas "
            "medida por (X − M).",
            "Rigor: a poupança externa exata é o " + azb("déficit em transações correntes") + " (inclui rendas "
            "e transferências); M − X é a versão simplificada, só com bens e serviços.",
            vm("Regra-âncora: (M − X) > 0 = poupança externa entrando; (X − M) > 0 = poupança doméstica saindo."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " O item fala em “transferência de poupança” sem sinal, e a "
                       "fonte aceitou a leitura genérica. Na prova, desconfie: na identidade, (M − X) soma ao "
                       "investimento, e uma parcela que soma não representa saída de recursos quando é positiva. "
                       "Itens mais rigorosos invertem o sentido para cobrar justamente esse ponto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a expressão (M − X) representa a poupança externa, que financia o investimento quando as "
            "importações superam as exportações.”</i> → CERTO",
            "<i>“Um país com superávit comercial recebe poupança externa líquida.”</i> → ERRADO (inversão: "
            "exporta poupança)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Gabarito dado como CERTO: com M > X a economia usa poupança externa; com X > M "
                             "transfere poupança ao exterior; (M − X) representa essa transferência líquida."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: gabarito CERTO da fonte mantido; pela identidade, (M − X) > 0 é poupança "
                    "transferida do resto do mundo para a economia local, e ERRADO seria mais defensável"],
    },
    # ------------------------------------------------------------------ E1-0409
    {
        "id": "ECO-E1-0409-1", "fonte_ref": "E1-0409", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": ("Considere uma economia aberta em que o governo recolha impostos e efetue gastos. A "
                    "Contabilidade Nacional pode ser sucintamente representada pela seguinte relação: "
                    "Y = C + I + G + X − M. Julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Essa equação revela a necessidade de poupança externa como o diferencial entre os valores "
                      "das importações e exportações, indicado pela relação, após algum rearranjo algébrico, "
                      "S − I = X − M, em que S contempla tanto a poupança pública quanto a privada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Essa equação revela a necessidade de poupança externa como o diferencial entre os valores "
                      "das importações e exportações, indicado pela relação, após algum rearranjo algébrico, "
                      "<u>S − I = X − M</u>, em que S contempla <u>tanto a poupança pública quanto a "
                      "privada</u>."),
        "poucas": ("Rearranjando, " + vd("(S privada + S pública) − I = X − M") + ". Se M > X, a poupança "
                   "doméstica não basta para o investimento, e a diferença é a " + azb("poupança externa") + "."),
        "destrinchando": [
            "Passo a passo: Y − C − G = I + X − M. Somando e subtraindo T: (Y − T − C) + (T − G) = I + X − M. "
            "Como Y − T − C = poupança privada e T − G = poupança pública, " + vd("S − I = X − M") + ", com S = "
            "poupança doméstica total.",
            "Leitura: o saldo externo é o espelho do " + azb("hiato poupança-investimento") + ". Se o país "
            "investe mais do que poupa (S < I), precisa de M > X — importa a diferença e a financia com "
            "poupança externa (I − S = M − X).",
            "É a base da " + azb("abordagem de absorção") + " do balanço de pagamentos: déficit externo = "
            "absorção interna (C + I + G) maior que a renda. Corrigir o déficit exige poupar mais ou investir "
            "menos.",
            "Também é a base do argumento dos " + azb("déficits gêmeos") + ": mantida a poupança privada e o "
            "investimento, um déficit fiscal (T < G) tende a se refletir em déficit externo.",
            "Com rendas e transferências do exterior, troca-se X − M pelo saldo em " + azb("transações "
            "correntes") + ".",
        ],
        "dissecando": (cz("[literalidade]") + " Paráfrase correta da identidade. O que pode confundir é o sinal "
                       "(S − I = X − M, e não M − X) e a cláusula final sobre S, que precisa incluir o governo "
                       "para a conta fechar — e inclui."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…indicado pela relação S − I = M − X…”</i> → ERRADO (sinal trocado)",
            "<i>“…em que S representa apenas a poupança privada.”</i> → ERRADO (restrição indevida: falta o "
            "termo T − G)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A identidade pode ser reescrita como S − I = X − M; com M > X há necessidade de "
                             "poupança externa; S inclui os setores público e privado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: a primeira frase da frente (economia aberta com governo e Y = C + I + G + "
                    "X − M) foi levada ao comando"],
    },
    # ------------------------------------------------------------------ E1-0410
    {
        "id": "ECO-E1-0410-1", "fonte_ref": "E1-0410", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("Em macroeconomia, sabendo que: Y é o Produto Interno Bruto (PIB), C é o consumo das "
                      "famílias, I é investimento privado, G são os gastos do governo, X são as exportações e M "
                      "são as importações, a identidade macroeconômica básica, também conhecida como equação do "
                      "PIB pelo lado da demanda, é dada por: Y = C + G + I + (X − M)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em macroeconomia, sabendo que: Y é o Produto Interno Bruto (PIB), C é o consumo das "
                      "famílias, I é investimento privado, G são os gastos do governo, X são as exportações e M "
                      "são as importações, a identidade macroeconômica básica, também conhecida como equação do "
                      "PIB pelo lado da demanda, é dada por: <u>Y = C + G + I + (X − M)</u>."),
        "poucas": ("É a " + azb("ótica da despesa") + ": o PIB é a soma do que se gasta em bens finais "
                   "domésticos — consumo, investimento, governo — mais as " + vd("exportações líquidas") + "."),
        "destrinchando": [
            "Cada componente compra produção final: " + azb("C") + " (famílias), " + azb("I") + " (formação "
            "bruta de capital), " + azb("G") + " (consumo do governo) e " + azb("X") + " (estrangeiros). Como "
            "C, I e G incluem bens importados, subtrai-se " + azb("M") + " para ficar só com a produção "
            "interna.",
            "A ordem das parcelas é irrelevante (Y = C + G + I + (X − M) é a mesma coisa). O que a banca "
            "costuma mexer é o sinal de M ou a inclusão de transferências.",
            "Em G entram compras de bens e serviços do governo, <b>não</b> transferências (aposentadorias, "
            "Bolsa Família), que são redistribuição de renda e reaparecem como consumo das famílias.",
            "Nuance de nomenclatura: nas contas nacionais, o investimento público fica em I (FBCF do governo) e "
            "G é só o consumo final do governo; nos manuais, G costuma reunir todo o gasto do governo e I fica "
            "como investimento privado — como no item.",
            "Ordem de grandeza no " + rx("Brasil") + ": consumo das famílias ≈ " + vd("60–65%") + " do PIB; "
            "consumo do governo ≈ " + vd("19–20%") + "; FBCF ≈ " + vd("16–17%") + " ⏳ (out/2026).",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual com as parcelas fora da ordem habitual. A "
                       "troca de ordem é cosmética; confira sinais e o que está em G."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é dada por Y = C + I + G + (M − X).”</i> → ERRADO (sinal trocado)",
            "<i>“Os pagamentos de aposentadorias pelo governo integram G na identidade do PIB.”</i> → ERRADO "
            "(transferência não é compra de bem ou serviço)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("É a identidade do PIB pela ótica da demanda em economia aberta com governo: "
                             "consumo, investimento, gastos do governo e saldo comercial."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0411
    {
        "id": "ECO-E1-0411-1", "fonte_ref": "E1-0411", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("A relação entre Produto Bruto e Produto Líquido nas Contas Nacionais é expressa pela "
                      "fórmula: PB = PL + Depreciação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A relação entre Produto Bruto e Produto Líquido nas Contas Nacionais é expressa pela "
                      "fórmula: <u>PB = PL + Depreciação</u>."),
        "poucas": ("“Bruto” inclui a reposição do capital gasto; “líquido” a desconta. Logo " + vd("bruto = "
                   "líquido + depreciação") + " — para o interno (PIB/PIL) e para o nacional (PNB/PNL)."),
        "destrinchando": [
            "Os qualificadores dos agregados combinam três pares independentes: " + azb("bruto × líquido")
            + " (com ou sem depreciação), " + azb("interno × nacional") + " (território × residentes: renda "
            "líquida do exterior) e " + azb("preços de mercado × custo de fatores") + " (com ou sem impostos "
            "indiretos líquidos de subsídios).",
            "Bruto → líquido: " + vd("PIL = PIB − depreciação") + "; " + vd("PNL = PNB − depreciação") + ". Nas "
            "contas nacionais, a depreciação chama-se " + azb("consumo de capital fixo") + ".",
            "Combinando: renda nacional = PNL a custo de fatores = PIB − RLEE − depreciação − (impostos "
            "indiretos − subsídios).",
            "Por que o bruto é o mais usado? A depreciação é difícil de medir (depende de vida útil e "
            "obsolescência estimadas); o PIB evita essa estimativa e é comparável entre países.",
        ],
        "dissecando": (cz("[literalidade]") + " Fórmula direta. A banca a erra trocando o sinal (PB = PL − "
                       "depreciação) ou o termo (impostos indiretos no lugar da depreciação, que é a passagem "
                       "preços de mercado × custo de fatores)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“PB = PL − Depreciação.”</i> → ERRADO (sinal trocado)",
            "<i>“A diferença entre o produto a preços de mercado e o produto a custo de fatores é a "
            "depreciação.”</i> → ERRADO (troca de conceito: são os impostos indiretos líquidos de subsídios)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Produto bruto = produto líquido + depreciação; vale para PIB/PIL e PNB/PNL.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0412
    {
        "id": "ECO-E1-0412-1", "fonte_ref": "E1-0412", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_CN,
        "rotulo_item": "Item",
        "assertiva": ("A poupança (S) é a parcela da renda gerada (salários, juros, aluguéis, lucros) mas que não "
                      "foi consumida, ou seja, é a renda nacional (Y) menos o consumo (C)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A poupança (S) é a parcela da renda gerada (salários, juros, aluguéis, lucros) mas que "
                      "<u>não foi consumida</u>, ou seja, é a renda nacional (Y) <u>menos o consumo</u> (C)."),
        "poucas": ("Poupar é " + azb("não consumir") + " a renda: " + vd("S = Y − C") + ". Os parênteses listam "
                   "as remunerações dos fatores, que somadas formam a renda nacional."),
        "destrinchando": [
            "A renda nacional é a soma das remunerações dos fatores: " + azb("salários") + " (trabalho), "
            + azb("juros") + " (capital financeiro), " + azb("aluguéis") + " (terra e imóveis) e "
            + azb("lucros") + " (capacidade empresarial). Parte é consumida, o resto é poupado.",
            "Em economia fechada e sem governo, " + vd("S = Y − C") + " e, como Y = C + I, " + vd("S = I")
            + " — a poupança é a contrapartida do investimento.",
            "Com governo, distingue-se a " + azb("poupança privada") + " (renda disponível − consumo = Y − T − C) "
            "da " + azb("poupança pública") + " (T − G). A poupança total, Y − C − G, segue sendo a renda não "
            "consumida pelo conjunto da economia.",
            "Poupança é <b>fluxo</b> (quanto se deixou de consumir no período), não estoque: o acumulado ao "
            "longo do tempo é riqueza ou patrimônio.",
            "No SCN, " + azb("poupança bruta") + " = renda disponível bruta − consumo final.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, válida no modelo simples. Itens desse tipo "
                       "ficam ERRADO quando trocam fluxo por estoque (“poupança é o total acumulado”) ou somam "
                       "o consumo em vez de subtraí-lo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A poupança corresponde ao estoque de riqueza acumulado pelas famílias.”</i> → ERRADO (troca "
            "fluxo por estoque)",
            "<i>“Com governo, a poupança privada é a renda disponível (Y − T) menos o consumo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A poupança é a parte da renda nacional não consumida: S = Y − C.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0414
    {
        "id": "ECO-E1-0414-1", "fonte_ref": "E1-0414", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_IBGE,
        "rotulo_item": "Item",
        "assertiva": ("As transferências sociais em espécie correspondem aos bens e serviços individuais fornecidos "
                      "gratuitamente, ou a preços simbólicos, pelo governo ou por instituições sem fins de lucro a "
                      "serviço das famílias, às famílias."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As transferências sociais em espécie correspondem aos <u>bens e serviços individuais</u> "
                      "fornecidos gratuitamente, ou a preços simbólicos, pelo governo ou por instituições sem fins "
                      "de lucro a serviço das famílias, às famílias."),
        "poucas": ("É a definição do " + rx("IBGE") + " (SNA 2008): " + azb("transferências sociais em espécie")
                   + " são " + vd("bens e serviços") + " (não dinheiro) entregues às famílias de graça ou a "
                   "preço simbólico pelo governo ou pelas ISFLSF."),
        "destrinchando": [
            "Exemplos: atendimento no " + rx("SUS") + ", escola pública, merenda escolar, medicamentos "
            "gratuitos, vacinas. São serviços <b>individuais</b> — usufruídos por uma família identificável —, "
            "ao contrário dos serviços coletivos (defesa, segurança pública, diplomacia).",
            "Não confundir com " + azb("benefícios sociais em dinheiro") + ": aposentadorias, Bolsa Família, "
            "seguro-desemprego e auxílio emergencial são transferências <b>monetárias</b>; a família decide "
            "como gastar.",
            "Função no SCN (conta de redistribuição da renda em espécie): " + vd("renda disponível ajustada = "
            "renda disponível + transferências sociais em espécie recebidas") + ". Do lado do consumo, o "
            + azb("consumo final efetivo") + " das famílias soma ao que elas compram o que recebem do governo "
            "e das ISFLSF.",
            "Empresas financeiras e não financeiras não participam dessa conta: não recebem transferências "
            "sociais em espécie.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Trecho copiado do relatório metodológico do IBGE. A "
                       "redação longa (“a serviço das famílias, às famílias”) parece truncada, mas está "
                       "correta. A banca erraria trocando “bens e serviços” por pagamentos em dinheiro ou "
                       "incluindo empresas como fornecedoras."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os pagamentos do Bolsa Família são registrados como transferências sociais em espécie.”</i> → "
            "ERRADO (troca de conceito: é benefício em dinheiro)",
            "<i>“A renda disponível ajustada das famílias inclui as transferências sociais em espécie "
            "recebidas.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Definição idêntica à do IBGE (Sistema de Contas Nacionais, relatório metodológico "
                             "vol. 24); conta de redistribuição da renda em espécie; cita Bolsa Família, auxílio "
                             "emergencial e seguro-desemprego como exemplos. O verso principal trata do registro "
                             "CIF/FOB das importações, de outro item."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [ALERTA_2022, "duplicata: comentário de E1-0417 fundido",
                    "qualidade_fonte: o comentário de origem dá Bolsa Família, auxílio emergencial e "
                    "seguro-desemprego como transferências sociais em espécie; são benefícios em dinheiro"],
    },
    # ------------------------------------------------------------------ E1-0415
    {
        "id": "ECO-E1-0415-1", "fonte_ref": "E1-0415", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_IBGE,
        "rotulo_item": "Item",
        "assertiva": ("Todos os serviços de transporte e de seguro relativos à importação, prestados por produtores "
                      "residentes e não residentes e incluídos no valor CIF da importação por produtos, são "
                      "globalmente deduzidos. Então, no Sistema de Contas Nacionais, o total da importação de bens "
                      "é sempre registrado a preços FOB."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Todos os serviços de transporte e de seguro relativos à importação, prestados por "
                      "produtores residentes e não residentes e incluídos no valor CIF da importação por "
                      "produtos, são <u>globalmente deduzidos</u>. Então, no Sistema de Contas Nacionais, o "
                      "<u>total</u> da importação de bens é <u>sempre</u> registrado a preços <u>FOB</u>."),
        "poucas": ("O detalhe por produto vem a preços " + azb("CIF") + " (com frete e seguro), mas um "
                   + azb("ajuste CIF/FOB") + " global retira esses serviços: o " + vd("total") + " das "
                   "importações de bens fica a preços " + vd("FOB") + "."),
        "destrinchando": [
            azb("FOB") + " (<i>free on board</i>): valor da mercadoria posta a bordo no país exportador, sem "
            "frete e seguro internacionais. " + azb("CIF") + " (<i>cost, insurance and freight</i>): valor "
            "com frete e seguro até o porto de destino.",
            "As estatísticas de comércio exterior registram as importações por produto a preços CIF. Mas, "
            "pelo SNA, frete e seguro são <b>serviços</b>, com produtor próprio: se prestados por não "
            "residentes, são importação de serviços; se por residentes, são produção doméstica. Deixá-los "
            "dentro do valor do bem contaria o serviço no lugar errado.",
            "Solução do " + rx("IBGE") + " (nota metodológica da estrutura do SCN): mantém o detalhe por "
            "produto a preços CIF e faz uma " + vd("dedução global") + " de transporte e seguro na linha "
            "do ajuste CIF/FOB. Resultado: total das importações de bens a FOB, coerente com o "
            + azb("balanço de pagamentos") + " (BPM6), que também registra bens a FOB.",
            "Por isso é CERTO tanto dizer que “as importações de bens, detalhadas por produtos, são avaliadas "
            "a preços CIF” quanto que “o total é registrado a FOB” — a banca dividiu o mesmo parágrafo em dois "
            "itens.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O “sempre” costuma denunciar erro, mas aqui "
                       "é a regra do manual: o total é FOB. O item parece contradizer a ideia de importações a "
                       "CIF, que vale só para o detalhamento por produto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No SCN, as importações de bens, detalhadas por produtos, são avaliadas a preços CIF.”</i> → "
            "CERTO",
            "<i>“No SCN, o total das importações de bens é registrado a preços CIF, incluindo frete e "
            "seguro.”</i> → ERRADO (troca de conceito: o total é FOB, após o ajuste global)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["todos", "sempre"], "dificuldade": 3,
        "comentario_fonte": ("Comentários de professores (Jetro Coutinho e outros) citando a nota metodológica "
                             "do IBGE: detalhe por produto a CIF, dedução global de frete e seguro, total a FOB."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_2022],
    },
    # ------------------------------------------------------------------ E1-0416
    {
        "id": "ECO-E1-0416-1", "fonte_ref": "E1-0416", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_IBGE,
        "rotulo_item": "Item",
        "assertiva": ("Os usos são transações que reduzem o saldo de um setor institucional, enquanto os recursos "
                      "são transações que aumentam seu saldo. Algumas transações podem ser apenas recurso dos "
                      "setores institucionais, como a produção, por exemplo, ou apenas uso, como o consumo "
                      "intermediário. Outras são registradas tanto nos usos quanto nos recursos, como os juros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os <u>usos</u> são transações que <u>reduzem</u> o saldo de um setor institucional, "
                      "enquanto os <u>recursos</u> são transações que <u>aumentam</u> seu saldo. Algumas "
                      "transações podem ser apenas recurso dos setores institucionais, como a produção, por "
                      "exemplo, ou apenas uso, como o consumo intermediário. Outras são registradas tanto nos "
                      "usos quanto nos recursos, como os juros."),
        "poucas": ("Nas " + azb("Contas Econômicas Integradas") + ", " + azb("recursos") + " (à direita) "
                   "aumentam o saldo e " + azb("usos") + " (à esquerda) o reduzem. Produção é só recurso; "
                   "consumo intermediário, só uso; juros, ambos."),
        "destrinchando": [
            "Usos e recursos substituem o par débito/crédito da contabilidade empresarial. Em cada conta, "
            + vd("saldo = recursos − usos") + ", e o saldo de uma conta abre a seguinte (valor adicionado → "
            "excedente operacional → renda disponível → poupança).",
            "<b>Só recurso</b>: a " + azb("produção") + " (conta de produção) — nenhum setor “usa” produção "
            "nessa conta. <b>Só uso</b>: o " + azb("consumo intermediário") + " e o consumo final.",
            "<b>Nos dois lados</b>: transações distributivas, como " + azb("juros") + ", dividendos e salários: "
            "para quem paga é uso; para quem recebe, recurso. Uma família recebe juros da poupança e paga "
            "juros do financiamento imobiliário.",
            "As CEI, base do SCN do " + rx("IBGE") + ", trazem em colunas os setores institucionais (empresas "
            "não financeiras, financeiras, governo, famílias, ISFLSF), o resto do mundo — visto do ponto de "
            "vista do resto do mundo — e bens e serviços; nas linhas, as transações e saldos.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Trecho copiado do relatório metodológico do IBGE. A "
                       "banca poderia inverter usos e recursos ou trocar os exemplos (produção como uso); os "
                       "três exemplos estão no lugar certo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os usos são transações que aumentam o saldo de um setor institucional, enquanto os recursos o "
            "reduzem.”</i> → ERRADO (inversão)",
            "<i>“Os juros são registrados apenas como uso dos setores institucionais.”</i> → ERRADO (restrição "
            "indevida: são uso de quem paga e recurso de quem recebe)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas"], "dificuldade": 2,
        "comentario_fonte": ("Trecho do IBGE (Sistema de Contas Nacionais, vol. 24): CEI com usos à esquerda e "
                             "recursos à direita; produção como recurso, consumo intermediário como uso, juros nos "
                             "dois lados."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_2022, "duplicata: comentário de E3-L00240 fundido"],
    },
    # ------------------------------------------------------------------ E1-0418
    {
        "id": "ECO-E1-0418-1", "fonte_ref": "E1-0418", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Nidi", "ano": 2023, "cacd": False,
        "errei": True,
        "comando": CMD_SCN,
        "rotulo_item": "Item",
        "assertiva": ("No formato vigente do Sistema de Contas Nacionais, as estimativas efetuadas sobre o "
                      "desempenho da economia são apresentadas por meio de dois tipos de classificação. A "
                      "classificação por tipo de atividade econômica é expressa nas Contas Econômicas Integradas e "
                      "a classificação por setor institucional aparece nas Tabelas de Recursos e Usos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No formato vigente do Sistema de Contas Nacionais, as estimativas efetuadas sobre o "
                       "desempenho da economia são apresentadas por meio de dois tipos de classificação. A "
                       "classificação por tipo de atividade econômica é expressa nas ")
                    + vm("Contas Econômicas Integradas") + az(" e a classificação por setor institucional aparece "
                                                               "nas ")
                    + vm("Tabelas de Recursos e Usos") + az(".")),
        "poucas": ("Está trocado: as " + azb("TRU") + " detalham a economia por " + vd("atividade e produto")
                   + "; as " + azb("CEI") + ", por " + vd("setor institucional") + "."),
        "destrinchando": [
            "O SCN do " + rx("IBGE") + " tem dois blocos principais: as " + azb("Tabelas de Recursos e Usos "
            "(TRU)") + " e as " + azb("Contas Econômicas Integradas (CEI)") + ".",
            "<b>TRU</b>: ótica da produção e dos produtos. Mostram a oferta (produção + importação) e a "
            "demanda (consumo intermediário + usos finais) de cada produto e a produção de cada "
            + azb("atividade econômica") + " (agropecuária, indústrias, serviços). Servem de base à matriz "
            "insumo-produto (" + oc("Leontief") + ").",
            "<b>CEI</b>: ótica dos agentes. Encadeiam as contas (produção, renda, uso da renda, capital, "
            "financeira) por " + azb("setor institucional") + ": empresas não financeiras, empresas "
            "financeiras, administração pública, famílias, ISFLSF e resto do mundo.",
            "Atalho: atividade é <b>o que</b> se produz (TRU); setor institucional é <b>quem</b> decide e "
            "detém a renda (CEI). Uma mesma atividade (ex.: saúde) aparece em vários setores (hospital "
            "público, privado, filantrópico).",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca cruzada dos dois quadros: as duas classificações "
                       "existem, mas cada uma foi posta na tabela da outra. Lembre que a CEI é “integrada” "
                       "justamente por reunir os setores institucionais."),
        "modulos": [("🧠 Mnemônico", ["<b>TRU</b> = <b>T</b>ipo de atividade; <b>CEI</b> = <b>C</b>ada setor "
                                      "<b>I</b>nstitucional."])],
        "reescrita": ("No formato vigente do Sistema de Contas Nacionais, as estimativas efetuadas sobre o "
                      "desempenho da economia são apresentadas por meio de dois tipos de classificação. A "
                      "classificação por tipo de atividade econômica é expressa nas " + hl("Tabelas de Recursos e "
                      "Usos") + " e a classificação por setor institucional aparece nas " + hl("Contas Econômicas "
                      "Integradas") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Está trocado: TRU distribuem a produção por atividade econômica; CEI, por setor "
                             "institucional; panorama do SCN do IBGE."),
        "qualidade_fonte": "bom",
        "figuras_fonte": fig_verso("image (142).png", "image (143).png", "image (144).png", "image (145).png",
                                   "image (146).png", "image (147).png", "image (148).png", "image (149).png"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0419
    {
        "id": "ECO-E1-0419-1", "fonte_ref": "E1-0419", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Nidi", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_SCN,
        "rotulo_item": "Item",
        "assertiva": ("A Renda Nacional Bruta se diferencia do Produto Interno Bruto por acrescentar as "
                      "remunerações dos fatores produtivos brasileiros fora do território e descontar a "
                      "remuneração dos fatores produtivos estrangeiros. Apesar disso, não se refere ao total da "
                      "renda disponível para consumo do país, devendo ainda considerar outras remessas de renda "
                      "secundária, ou seja, sem contrapartida econômica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Renda Nacional Bruta se diferencia do Produto Interno Bruto por acrescentar as "
                      "remunerações dos fatores produtivos brasileiros fora do território e descontar a "
                      "remuneração dos fatores produtivos estrangeiros. Apesar disso, <u>não se refere ao total da "
                      "renda disponível</u> para consumo do país, devendo ainda considerar outras remessas de "
                      "<u>renda secundária</u>, ou seja, sem contrapartida econômica."),
        "poucas": (vd("RNB = PIB + renda primária líquida do exterior") + "; " + vd("RDB = RNB + renda "
                   "secundária líquida") + " (transferências correntes sem contrapartida). A renda disponível "
                   "é um passo além da RNB."),
        "destrinchando": [
            azb("PIB") + " → " + azb("RNB") + ": soma-se a " + azb("renda primária") + " recebida do exterior "
            "(salários, juros, lucros e dividendos de fatores de residentes lá fora) e subtrai-se a enviada "
            "(fatores de não residentes aqui). O " + rx("Brasil") + ", com grande passivo externo, tem renda "
            "primária líquida negativa: RNB < PIB.",
            azb("RNB") + " → " + azb("renda disponível bruta (RDB)") + ": soma-se a " + azb("renda "
            "secundária") + " líquida — transferências correntes <b>sem contrapartida</b>: remessas de "
            "emigrantes às famílias, doações, ajuda internacional, contribuições a organismos.",
            "A RDB se reparte entre " + vd("consumo final + poupança bruta") + ": é a medida da renda que o "
            "país pode efetivamente gastar.",
            "No balanço de pagamentos (" + azb("BPM6") + "), as duas contas aparecem nas transações correntes: "
            "renda primária e renda secundária, ao lado de bens e serviços.",
            "Nuance de redação: o critério do SCN é residência, não nacionalidade; “fatores brasileiros” deve "
            "ser lido como fatores de residentes.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Duas frases corretas encadeadas: a primeira define a "
                       "RNB; a segunda (“apesar disso”) lembra que falta a renda secundária para chegar à renda "
                       "disponível. A banca erraria dizendo que a RNB já é a renda disponível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A renda nacional bruta já incorpora as transferências unilaterais correntes recebidas do "
            "exterior.”</i> → ERRADO (troca de conceito: isso é a renda disponível bruta)",
            "<i>“Remessas de emigrantes às famílias no país de origem são registradas como renda "
            "secundária.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Item correto: definição de renda nacional e de produto interno; relação do BP com "
                             "a conta de operações com o resto do mundo das CEI; estrutura do BP."),
        "qualidade_fonte": "raso",
        "figuras_fonte": fig_verso("image (143).png", "image (150).png", "image (151).png", "image (152).png"),
        "alertas": [],
    },
]
