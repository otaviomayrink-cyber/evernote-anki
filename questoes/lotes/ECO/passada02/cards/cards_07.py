"""Cards do lote de redação 07 — ECO, passada 02 (notas 18: balanço de pagamentos; 19: indicadores fiscais e
de liquidez/solvência externa)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "est": "🏗️ Estrutura do BP (BPM6)",
    "lanc": "✍️ Lançamentos",
    "nfsp": "💰 Resultados fiscais (NFSP)",
    "ext": "🌐 Indicadores externos",
}

CMD_RT_BPM6 = ("Com base na sexta edição do Manual do Balanço de Pagamentos do Fundo Monetário Internacional "
               "(BPM6), avalie as seguintes afirmativas como verdadeiras ou falsas.")

CMD_ANTT = ("Um país realizou, em determinado ano, as transações com o exterior apresentadas na tabela a seguir. "
            "Com fulcro nessa situação hipotética, julgue o item.")

EXC_ANTT = ("<p><b>Transações com o exterior (valores em bilhões de dólares)</b></p><ul>"
            "<li>importações de mercadoria: 5</li>"
            "<li>exportações de mercadoria: 15</li>"
            "<li>recebimento de doações na forma de mercadorias: 1</li>"
            "<li>empréstimos e financiamentos recebidos no exterior: 10</li>"
            "<li>investimento estrangeiro direto recebido do exterior, sem cobertura cambial, na forma de "
            "equipamentos: 15</li>"
            "<li>juros de empréstimos pagos ao exterior: 5</li>"
            "<li>fretes pagos ao exterior: 10</li></ul>")

CMD_NIDI = ("Considere as transações de um país com o exterior apresentadas a seguir, extraídas do seu balanço de "
            "pagamentos, e julgue o item.")

EXC_NIDI = ("<p><b>BALANÇO DE PAGAMENTOS (EM US$ BILHÕES)</b></p><ul>"
            "<li>Exportações: 120</li>"
            "<li>Importações: 110</li>"
            "<li>Donativos recebidos de ONGs sediadas no exterior: 2</li>"
            "<li>Investimentos para ampliação de empreendimento industrial: 18</li>"
            "<li>Reinvestimento de lucros de uma multinacional no Brasil: 10</li>"
            "<li>Aplicação de estrangeiros na aquisição de ações no mercado secundário: 11</li>"
            "<li>Remessa de lucros por filiais de empresas estrangeiras: 15</li>"
            "<li>Amortização de empréstimos externos: 7</li>"
            "<li>Empréstimos externos obtidos: 22</li>"
            "<li>Juros sobre empréstimos a instituições internacionais: 14</li>"
            "<li>Viagens internacionais de residentes no Brasil: 13</li>"
            "<li>Pagamento de royalties e assistência técnica: 9</li>"
            "<li>Fretes pagos a transportadores estrangeiros: 6</li></ul>")

FIG_NIDI_FRENTE = {"ref": "IMAGEM 269", "tipo_fonte": "TEXTO", "lado": "frente",
                   "acao": "texto (lista de transações no excerto; valores faltantes completados pelo comentário)"}
FIG_NIDI_270 = {"ref": "IMAGEM 270", "tipo_fonte": "TABELA", "lado": "verso",
                "acao": "absorvida (lançamentos e saldos no 📖)"}

ALERTA_NIDI = ("texto_corrigido: a transcrição da tabela da frente (IMAGEM 269) perdeu os valores de donativos (2), "
               "amortização (7), royalties (9) e fretes (6) e desalinhou o 18 (é da ampliação industrial); "
               "completados pelos lançamentos do comentário, que fecham TC = −55, conta financeira sem reservas = "
               "+54 e reservas = −1")

CMD_NFSP_TAB = ("Considerando as informações apresentadas na tabela, referentes à evolução do déficit público "
                "brasileiro nos anos de 2022 e 2023, bem como aspectos relativos à estrutura orçamentária do "
                "governo, julgue o item.")

TAB_NFSP = {
    "titulo": "Necessidades de financiamento do setor público — setor público consolidado",
    "cabecalho": ["Conceito", "2022 (R$ bi)", "2022 (% PIB)", "2023 (R$ bi)", "2023 (% PIB)"],
    "linhas": [["Nominal", "460,4", "4,6", "967,4", "8,9"],
               ["Juros nominais", "586,4", "5,8", "718,3", "6,6"],
               ["Primário", "−126,0", "−1,2", "249,1", "2,3"]],
    "fonte": "Banco Central do Brasil, 2024 (com adaptações). PIB: R$ 10.079,7 bi (2022) e R$ 10.856,1 bi (2023).",
}

FIG_NFSP_TAB = [{"ref": "IMAGEM 105", "tipo_fonte": "TABELA", "lado": "frente",
                 "acao": "transcrita_html (tabela aninhada, 5 colunas)"}]

ALERTAS_NFSP_TAB = ["transcricao_incoerente: a transcrição da IMAGEM 105 dá o nominal de 2022 como −460,4 (−4,6%); "
                    "pela identidade nominal = primário + juros (−126,0 + 586,4) o valor é +460,4 (4,6%) — "
                    "corrigido",
                    "texto_parcial: a tabela original discrimina governo central, estados, municípios e estatais; "
                    "a transcrição só preservou o consolidado"]

CMD_BOZAN_NFSP = ("Sobre a apresentação das contas do governo e os diferentes conceitos relacionados ao déficit e à "
                  "dívida pública, julgue o item a seguir.")

CMD_NAB_FISC = ("Julgue o item a seguir, relativo a conceitos básicos de contabilidade fiscal e sustentabilidade "
                "do endividamento público.")

CMD_CACD25 = "Em relação aos indicadores de liquidez e de solvência externa, julgue o item que se segue."

CARDS = [
    # ------------------------------------------------------------------ E2-L01665
    {
        "id": "ECO-E2-L01665-1", "fonte_ref": "E2-L01665", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_BPM6,
        "rotulo_item": "Item",
        "assertiva": "A amortização de um passivo externo é contabilizada na Conta de Rendas Primárias.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A amortização de um passivo externo é contabilizada na ") + vm("Conta de Rendas Primárias")
                   + az("."),
        "poucas": ("Amortização é a devolução do " + azb("principal") + ": reduz um passivo e vai para a "
                   + azb("conta financeira") + ". Na renda primária entram só os " + azb("juros") + " sobre esse "
                   "passivo."),
        "destrinchando": [
            "O serviço da dívida tem duas partes que o BP separa: " + vd("juros") + " (remuneração do capital, "
            "um fluxo de renda) e " + vd("amortização") + " (devolução do principal, uma transação com o "
            "próprio passivo).",
            azb("Renda primária") + " (parte das transações correntes) registra a remuneração dos fatores de "
            "produção: salários de não residentes, juros, lucros e dividendos, lucros reinvestidos. "
            + azb("Conta financeira") + " registra as variações de ativos e passivos financeiros: investimento "
            "direto, carteira, derivativos, outros investimentos e reservas.",
            "Exemplo: o país paga 12 a um banco estrangeiro, sendo 2 de juros e 10 de principal. Lança-se "
            + vd("−2") + " em renda primária (piora as transações correntes) e uma " + vd("redução de 10") + " na "
            "incidência de passivos em outros investimentos (empréstimos); a contrapartida é a queda de 12 em "
            "ativos (depósitos no exterior ou reservas).",
            "Consequência para a leitura das contas: amortizar dívida <b>não</b> mexe no saldo em transações "
            "correntes; pesa sobre a necessidade de financiamento externo (rolagem), não sobre a absorção "
            "interna.",
            vm("Regra-âncora: juros → transações correntes (renda primária); principal → conta financeira."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item pega um lançamento que nasce da dívida e o joga na "
                       "conta da remuneração da dívida. A pista é o substantivo: “amortização” é sempre "
                       "principal; quem vai para a renda primária é o “juro”. 🔥 A banca alterna os dois verbos "
                       "(amortizar × pagar juros) no mesmo bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os juros pagos sobre um passivo externo são contabilizados na conta de renda primária.”</i> → "
            "CERTO",
            "<i>“A amortização de dívida externa piora o saldo em transações correntes.”</i> → ERRADO (troca de "
            "conceito: afeta só a conta financeira)",
        ])],
        "reescrita": ("A amortização de um passivo externo é contabilizada na " + hl("Conta Financeira") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Amortização = pagamento do principal, transação financeira registrada na conta "
                            "financeira (outros investimentos/carteira); a renda primária registra os juros, não "
                            "o principal.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L01736 (mesmo item; comentários fundidos)"],
    },
    # ------------------------------------------------------------------ E2-L01666
    {
        "id": "ECO-E2-L01666-1", "fonte_ref": "E2-L01666", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_BPM6,
        "rotulo_item": "Item",
        "assertiva": ("O saldo da Conta Financeira é calculado pela diferença entre a aquisição líquida de Ativos "
                      "Financeiros e a incidência líquida de Passivos Financeiros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O saldo da Conta Financeira é calculado pela diferença entre a <u>aquisição líquida de "
                      "Ativos</u> Financeiros e a <u>incidência líquida de Passivos</u> Financeiros."),
        "poucas": ("No " + azb("BPM6") + ", conta financeira = " + vd("ΔAtivos − ΔPassivos") + ". Saldo "
                   "positivo = o país empresta ao exterior; negativo = capta recursos externos."),
        "destrinchando": [
            "O BPM6 abandonou a lógica de créditos e débitos na conta financeira. Cada linha é uma "
            "<b>variação líquida</b>: " + azb("aquisição líquida de ativos") + " (compras menos vendas de ativos "
            "externos por residentes) e " + azb("incidência líquida de passivos") + " (novas obrigações com não "
            "residentes menos as liquidadas).",
            "Saldo = ativos − passivos. É o " + azb("empréstimo líquido") + " do país ao resto do mundo (net "
            "lending): " + vd("> 0") + " = exportação líquida de capital; " + vd("< 0") + " = captação líquida "
            "(o país se financia lá fora).",
            "Identidade do BPM6: " + vd("TC + CK − CF + EO = 0") + ", ou seja, " + vd("CF = TC + CK + EO") + ". "
            "Déficit em transações correntes ⇒ conta financeira <b>negativa</b>: aumentam os passivos (ou caem "
            "os ativos) para financiá-lo.",
            "Mudança de sinal em relação ao BPM5: no manual antigo, entrada de capital aparecia com sinal "
            "positivo e aumento de reservas com sinal negativo; no BPM6, aumento de ativos (inclusive reservas) é "
            "positivo. O " + rx("Banco Central do Brasil") + " passou a divulgar o BP no BPM6 em " + vd("2015")
            + ".",
            vm("Regra-âncora: conta financeira (BPM6) = ativos − passivos = TC + CK."),
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição do manual. O risco é a ordem dos termos: "
                       "quem ainda pensa no BPM5 (“entrada de capital é positiva”) tende a achar que o certo é "
                       "passivos − ativos — inclusive parte dos comentários-padrão comete esse erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo da conta financeira é calculado pela diferença entre a incidência líquida de passivos e "
            "a aquisição líquida de ativos.”</i> → ERRADO (inversão da ordem)",
            "<i>“Um saldo negativo na conta financeira indica que o país captou recursos líquidos no "
            "exterior.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Saldo da conta financeira = aquisição líquida de ativos − incidência líquida de "
                            "passivos; positivo = exportação líquida de capital. Um dos comentários afirma o "
                            "contrário (passivos − ativos).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L01737 (mesmo item; comentários fundidos)",
                    "qualidade_fonte: um dos comentários fundidos diz que no BPM6 o saldo é passivos − ativos; "
                    "a convenção do BPM6 é ativos − passivos"],
    },
    # ------------------------------------------------------------------ E2-L01699
    {
        "id": "ECO-E2-L01699-1", "fonte_ref": "E2-L01699", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Sobre os conceitos e teorias da economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Se um país registrou saldo negativo em transações correntes num dado ano, e saldo zero para "
                      "a conta capital, seu saldo da conta financeira foi positivo, para cobrir as necessidades de "
                      "financiamento externo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se um país registrou saldo negativo em transações correntes num dado ano, e saldo zero para "
                      "a conta capital, seu saldo da conta financeira foi ") + vm("positivo") + az(", para cobrir "
                      "as necessidades de financiamento externo."),
        "poucas": ("No " + azb("BPM6") + ", a conta financeira tem o mesmo sinal das transações correntes: "
                   + vd("CF = TC + CK") + ". Com TC < 0 e CK = 0, a conta financeira é " + vd("negativa")
                   + " — o país aumentou passivos líquidos."),
        "destrinchando": [
            "Identidade do BPM6: " + vd("TC + CK − CF + EO = 0") + ". A conta financeira é medida como "
            "aquisição líquida de ativos <b>menos</b> incidência líquida de passivos — é o empréstimo líquido "
            "do país ao exterior.",
            "Quem tem déficit em transações correntes gasta mais do que recebe do exterior e precisa se "
            "financiar: emite passivos (IDE recebido, títulos, empréstimos) ou vende ativos (inclusive "
            "reservas). Nos dois casos, ativos − passivos fica <b>negativo</b>. Com TC = −50 e CK = 0, CF = −50 "
            "(desprezados erros e omissões).",
            "A intuição do item (“entra capital para cobrir o déficit”) é correta; o que está errado é o "
            "<b>sinal</b>. No BPM5, entrada de capital era registrada como positiva e a conta financeira "
            "“espelhava” as transações correntes com sinal trocado; no BPM6, as duas andam com o mesmo sinal.",
            "Leitura macro: " + vd("TC = S − I") + " (poupança menos investimento). Déficit em TC = poupança "
            "externa positiva, que aparece na conta financeira como captação líquida (saldo negativo).",
            vm("Regra-âncora: no BPM6, déficit em transações correntes ⇒ conta financeira negativa."),
        ],
        "dissecando": (cz("[inversão]") + " O item descreve o mecanismo certo (financiamento externo do déficit) "
                       "com a convenção de sinais do BPM5. A pista é a palavra “saldo”: pergunta-se pelo número "
                       "da conta, e no BPM6 ele é ativos − passivos. 🔥 Itens de BP pós-2015 testam quase sempre "
                       "o sinal da conta financeira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…seu saldo da conta financeira foi negativo, indicando incidência líquida de passivos superior "
            "à aquisição líquida de ativos.”</i> → CERTO",
            "<i>“…seu saldo da conta financeira foi necessariamente igual a zero, porque o BP sempre se "
            "equilibra.”</i> → ERRADO (confunde o fechamento do BP com o saldo de uma conta)",
        ])],
        "reescrita": ("Se um país registrou saldo negativo em transações correntes num dado ano, e saldo zero para "
                      "a conta capital, seu saldo da conta financeira foi " + hl("negativo") + ", para cobrir as "
                      "necessidades de financiamento externo."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Comentário afirma que a conta financeira deve ser positiva para manter a identidade e "
                            "atribui o erro ao nexo causal (“financia”); fórmula transcrita CF = TC + CK.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 502", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (identidade CF = TC + CK no 📖)"}],
        "alertas": ["qualidade_fonte: o comentário diz que a conta financeira seria positiva e situa o erro no "
                    "nexo causal; pela própria fórmula transcrita (CF = TC + CK, BPM6) ela é negativa — o erro do "
                    "item é o sinal"],
    },
    # ------------------------------------------------------------------ E3-L00164
    {
        "id": "ECO-E3-L00164-1", "fonte_ref": "E3-L00164", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT,
        "excerto": EXC_ANTT,
        "rotulo_item": "Item",
        "assertiva": ("As reservas internacionais do país apresentaram redução de 5 bilhões de dólares no ano em "
                      "questão."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As reservas internacionais do país apresentaram ") + vm("redução") + az(" de 5 bilhões de "
                      "dólares no ano em questão."),
        "poucas": ("Só mexem nas reservas as transações " + azb("com cobertura cambial") + ": 15 − 5 + 10 − 5 − 10 = "
                   + vd("+5") + ". As reservas <b>aumentaram</b> 5 bilhões."),
        "destrinchando": [
            "Atalho: separe o que movimenta divisas do que não movimenta. Entram moeda: exportações (+15) e "
            "empréstimos recebidos (+10). Saem moeda: importações (−5), juros (−5) e fretes (−10). Saldo: "
            + vd("+5") + ". Doação em mercadorias e IED em equipamentos chegam “em espécie”: não trazem dólar.",
            "Pelas partidas dobradas (BPM6), as transações sem cobertura cambial têm contrapartida <b>dentro</b> "
            "do próprio BP: a doação lança +1 em " + azb("renda secundária") + " e −1 em importação de bens; o IED "
            "em equipamentos lança +15 em " + azb("investimento direto") + " (passivo) e −15 em importação.",
            "Saldos: balança comercial 15 − 5 − 1 − 15 = " + vd("−6") + "; serviços (fretes) " + vd("−10")
            + "; renda primária (juros) " + vd("−5") + "; renda secundária " + vd("+1") + " → transações correntes "
            + vd("−20") + ". Passivos da conta financeira: 10 + 15 = " + vd("+25") + ". Resultado do BP: −20 + 25 = "
            + vd("+5") + " = acúmulo de " + azb("ativos de reserva") + ".",
            "Conferência no BPM6: conta financeira = ativos − passivos = 5 − 25 = −20 = TC. Fecha.",
            vm("Regra-âncora: variação de reservas = saldo das transações que movimentam divisas = resultado do BP."),
        ],
        "dissecando": (cz("[inversão]") + " O número está certo (5); o sentido foi trocado. A banca conta com quem "
                       "soma tudo com sinal de “gasto” ou trata a importação dos equipamentos como saída de "
                       "dólares. 🔥 CEBRASPE adora transação “sem cobertura cambial” para separar lançamento de "
                       "fluxo de divisas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo em transações correntes do país foi deficitário em 20 bilhões de dólares.”</i> → CERTO",
            "<i>“A doação em mercadorias elevou as reservas internacionais em 1 bilhão de dólares.”</i> → ERRADO "
            "(sem cobertura cambial: a contrapartida é importação de bens)",
        ])],
        "reescrita": ("As reservas internacionais do país apresentaram " + hl("aumento") + " de 5 bilhões de dólares "
                      "no ano em questão."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Transações com cobertura cambial: 15 − 5 − 10 − 5 + 10 = +5; doações em mercadorias "
                            "e IED em equipamentos não afetam as reservas; BP = −6 −10 −5 +1 +25 = +5 → aumento "
                            "de reservas de 5.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 180", "tipo_fonte": "TEXTO", "lado": "frente",
                           "acao": "texto (lista de transações no excerto)"},
                          {"ref": "IMAGEM 187-188", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖"},
                          {"ref": "IMAGEM 189-190", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "absorvidas no 📖 (lançamentos por conta)"},
                          {"ref": "IMAGEM 191", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "irrecuperavel (ilegível; cortada)"}],
        "alertas": ["texto_corrigido: a transcrição da frente (IMAGEM 180) perdeu os valores das doações (1) e dos "
                    "juros (5) e desalinhou os demais; valores completados pelos lançamentos do comentário"],
    },
    # ------------------------------------------------------------------ E3-L00203
    {
        "id": "ECO-E3-L00203-1", "fonte_ref": "E3-L00203", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "excerto": EXC_NIDI,
        "rotulo_item": "Item",
        "assertiva": "O balanço de serviços apresentou saldo negativo de US$ 43 bilhões.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O balanço de serviços apresentou saldo negativo de US$ ") + vm("43") + az(" bilhões."),
        "poucas": ("Serviços são só viagens, royalties e fretes: −(13 + 9 + 6) = " + vd("−28") + ". O 43 soma "
                   "indevidamente a " + azb("remessa de lucros") + " (15), que é renda primária."),
        "destrinchando": [
            azb("Serviços") + " remuneram atividades prestadas: transporte (fretes), viagens, seguros, "
            "royalties e assistência técnica, aluguel de equipamentos, serviços financeiros. Na tabela: viagens "
            "13, royalties e assistência técnica 9, fretes 6 — todos débitos → " + vd("−28") + ".",
            azb("Renda primária") + " remunera fatores (capital e trabalho): remessa de lucros 15, juros 14 e "
            "lucros reinvestidos 10 → " + vd("−39") + ". A soma 28 + 15 = 43 é exatamente o erro do item.",
            "Fechando a conta corrente: balança comercial 120 − 110 = " + vd("+10") + "; serviços −28; renda "
            "primária −39; renda secundária (donativos) " + vd("+2") + " → transações correntes " + vd("−55")
            + ".",
            "Royalties merecem atenção: no BPM6 são serviço (“encargos pelo uso de propriedade intelectual”), "
            "não renda — apesar de parecerem “remuneração” de um ativo.",
            vm("Regra-âncora: serviço remunera atividade; renda remunera fator (lucro, juro, salário)."),
        ],
        "dissecando": (cz("[dado alterado · troca de conceito]") + " O número foi fabricado somando uma rubrica de "
                       "renda primária (lucros remetidos, 15) aos serviços. Pista: 43 − 28 = 15, que é um valor "
                       "da própria tabela. Em itens de cálculo de BP, refaça a soma só com o que pertence à "
                       "conta pedida."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A conta de renda primária apresentou saldo negativo de US$ 39 bilhões.”</i> → CERTO",
            "<i>“O pagamento de royalties integra a conta de renda primária.”</i> → ERRADO (troca de conceito: "
            "é serviço)",
        ])],
        "reescrita": ("O balanço de serviços apresentou saldo negativo de US$ " + hl("28") + " bilhões."),
        "tipo_erro": ["DADO_ALTERADO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Serviços: −13 −9 −6 = −28; o 43 vem de somar a remessa de lucros (15), que é renda "
                            "primária; rendas = −39.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_NIDI_FRENTE, FIG_NIDI_270,
                          {"ref": "IMAGEM 271-274", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [ALERTA_NIDI],
    },
    # ------------------------------------------------------------------ E3-L00204
    {
        "id": "ECO-E3-L00204-1", "fonte_ref": "E3-L00204", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "excerto": EXC_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Ocorrendo saldo negativo no balanço de pagamentos, ele poderá ser financiado mediante redução "
                      "das reservas internacionais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ocorrendo saldo negativo no balanço de pagamentos, ele <u>poderá</u> ser financiado "
                      "mediante redução das reservas internacionais."),
        "poucas": ("O “saldo do BP” é o resultado <b>antes</b> das contas de ajuste; déficit significa que "
                   "faltaram divisas, e a forma clássica de cobri-lo é o " + azb("Banco Central vender "
                   "reservas") + "."),
        "destrinchando": [
            "Contabilmente o BP sempre fecha em zero (partidas dobradas). Quando se fala em " + azb("saldo do "
            "balanço de pagamentos") + ", fala-se do resultado das transações correntes, da conta capital e da "
            "conta financeira <b>exceto</b> os ativos de reserva (e, na linguagem antiga, exceto as operações "
            "de regularização).",
            "Na tabela: transações correntes " + vd("−55") + " (comércio +10, serviços −28, renda primária −39, "
            "renda secundária +2) e conta financeira sem reservas " + vd("+54") + " (passivos: IED 18 + 10, "
            "carteira 11, empréstimos 22 − 7). Resultado: " + vd("−1") + " → reservas caem US$ 1 bilhão.",
            "Formas de financiar o déficit: (1) " + azb("uso de reservas") + "; (2) " + azb("empréstimos de "
            "regularização") + " (FMI, outros bancos centrais); (3) acúmulo de atrasados. Sob câmbio "
            "flutuante puro, o ajuste se dá pelo preço: a moeda deprecia até que o déficit desapareça, sem "
            "perda de reservas.",
            "Por isso o item usa “poderá”: a redução de reservas é <b>um</b> dos instrumentos, não o único.",
            vm("Regra-âncora: déficit do BP = perda de reservas (ou financiamento compensatório)."),
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O “poderá” salva o item: há outros meios de "
                       "financiar o déficit, mas a redução das reservas é o mecanismo de manual. Troque por "
                       "“deverá necessariamente” e o item vira ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ocorrendo saldo negativo no balanço de pagamentos, ele deverá necessariamente ser financiado "
            "mediante redução das reservas internacionais.”</i> → ERRADO (modulador absoluto: há empréstimos de "
            "regularização e atrasados)",
            "<i>“Com os dados da tabela, as reservas internacionais aumentaram US$ 1 bilhão.”</i> → ERRADO "
            "(inversão: caíram US$ 1 bilhão)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["poderá"], "dificuldade": 1,
        "comentario_fonte": "BP é contabilmente nulo; déficit global antes das transações compensatórias é coberto "
                            "pela venda de reservas pelo Banco Central; BP − BK − BF = variação de reservas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_NIDI_FRENTE, FIG_NIDI_270,
                          {"ref": "IMAGEM 275-277", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [ALERTA_NIDI],
    },
    # ------------------------------------------------------------------ E3-L00205
    {
        "id": "ECO-E3-L00205-1", "fonte_ref": "E3-L00205", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "excerto": EXC_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("A aquisição de ações no mercado secundário e o reinvestimento de lucros não contribuem para o "
                      "aumento do estoque de capital da economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A aquisição de ações no <u>mercado secundário</u> e o <u>reinvestimento de lucros</u> não "
                      "contribuem para o aumento do estoque de capital da economia."),
        "poucas": ("Ação comprada no secundário só muda de dono; lucro reinvestido é lançamento de "
                   + azb("financiamento") + ", não de " + azb("formação bruta de capital fixo") + ". Nenhum dos "
                   "dois, por si, cria máquina ou fábrica."),
        "destrinchando": [
            "O estoque de capital cresce com " + azb("FBCF") + " (máquinas, equipamentos, construções). "
            "Lançamentos da conta financeira registram <b>quem financia</b> e <b>quem é dono</b>; só viram "
            "capital novo se o dinheiro for gasto em investimento real.",
            azb("Mercado secundário") + ": o estrangeiro paga a outro investidor, não à empresa. É troca de "
            "titularidade de um ativo existente (investimento em carteira, +11 na tabela). No "
            + azb("mercado primário") + " (IPO, follow-on) o dinheiro vai para o caixa da companhia e pode "
            "financiar expansão.",
            azb("Reinvestimento de lucros") + " (+10): o BP registra como se a filial remetesse o lucro (débito "
            "em renda primária) e a matriz o reaplicasse (crédito em IED). Não entra divisa nova; é a retenção "
            "de um lucro gerado aqui. Pode financiar FBCF depois, mas o lançamento em si não é investimento "
            "real.",
            "Contraste na mesma tabela: os " + vd("18") + " de “investimentos para ampliação de empreendimento "
            "industrial” são o caso típico de IED que se converte em capacidade produtiva nova.",
            "Ressalva útil para discursivas: o secundário influencia o investimento <b>indiretamente</b> "
            "(liquidez e preço das ações reduzem o custo de capital), e o lucro retido é fonte importante de "
            "financiamento do investimento das multinacionais.",
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " Soa errado porque as duas operações aparecem como "
                       "“investimento” no BP. O item cobra a diferença entre investimento financeiro e "
                       "investimento no sentido das contas nacionais (FBCF). A leitura pretendida é “por si "
                       "sós”: o lançamento não cria capital."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A subscrição de ações em oferta primária por estrangeiros, destinada à ampliação da planta, não "
            "contribui para o aumento do estoque de capital.”</i> → ERRADO (aí há recurso novo para FBCF)",
            "<i>“O reinvestimento de lucros é registrado simultaneamente em renda primária e em investimento "
            "direto.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Mercado secundário é revenda de ativo existente (o aumento de capital foi no IPO); "
                            "reinvestimento de lucros é retenção contábil (renda primária + IED) que só aumenta o "
                            "capital se virar FBCF.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_NIDI_FRENTE, FIG_NIDI_270,
                          {"ref": "IMAGEM 278-279", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [ALERTA_NIDI],
    },
    # ------------------------------------------------------------------ E3-L00206
    {
        "id": "ECO-E3-L00206-1", "fonte_ref": "E3-L00206", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "excerto": EXC_NIDI,
        "rotulo_item": "Item",
        "assertiva": "O movimento de capitais autônomos foi positivo e igual a US$ 39 bilhões.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O movimento de capitais autônomos foi positivo e igual a US$ ") + vm("39") + az(" bilhões."),
        "poucas": ("Capitais autônomos = todos os fluxos financeiros voluntários: 18 + 10 + 11 + (22 − 7) = "
                   + vd("+54") + ". O 39 esquece os " + azb("empréstimos líquidos") + " (+15)."),
        "destrinchando": [
            azb("Capitais autônomos") + " × " + azb("compensatórios") + " é uma classificação analítica da era "
            "BPM5: autônomos são os movidos por decisão própria dos agentes (IED, carteira, empréstimos e "
            "financiamentos voluntários); compensatórios são os que fecham o resultado (uso de reservas, "
            "empréstimos do FMI, atrasados). No BPM6, tudo isso está dentro da conta financeira.",
            "Na tabela: IED " + vd("18 + 10") + " (ampliação industrial e lucros reinvestidos), carteira "
            + vd("11") + " (ações), outros investimentos " + vd("22 − 7 = 15") + " (empréstimos obtidos menos "
            "amortização). Total " + vd("+54") + ".",
            "Conferência: transações correntes −55 + autônomos +54 = " + vd("−1") + " = déficit do BP, coberto "
            "pelos compensatórios (reservas −1). Fecha com os outros itens da tabela.",
            "Leituras mais estreitas de alguns manuais antigos excluem os lucros reinvestidos (sem fluxo de "
            "divisas) e os empréstimos, chegando a 18 + 11 = 29. Em nenhuma convenção dá 39: esse número soma "
            "só os investimentos (direto e carteira) e larga a dívida pelo caminho.",
            vm("Regra-âncora: capitais autônomos = conta financeira sem reservas e sem operações de "
               "regularização."),
        ],
        "dissecando": (cz("[dado alterado]") + " O 39 é uma soma parcial plausível (18 + 10 + 11), pensada para "
                       "quem lembra do IED e da carteira mas esquece que empréstimos e amortizações também são "
                       "capitais autônomos. O sinal positivo está certo; o valor, não."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O movimento de capitais autônomos foi positivo e igual a US$ 54 bilhões.”</i> → CERTO",
            "<i>“A amortização de empréstimos externos integra os capitais compensatórios.”</i> → ERRADO (troca "
            "de conceito: amortização voluntária é capital autônomo)",
        ])],
        "reescrita": ("O movimento de capitais autônomos foi positivo e igual a US$ " + hl("54") + " bilhões."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Capitais autônomos = fluxos de iniciativa dos agentes (carteira, IDE, empréstimos); "
                            "compensatórios = reservas, FMI. Respostas de IA divergem: 54 (conceito amplo) ou 29 "
                            "(conceito estreito, sem reinvestimento e sem empréstimos).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [FIG_NIDI_FRENTE, FIG_NIDI_270,
                          {"ref": "IMAGEM 280-288", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖"}],
        "alertas": [ALERTA_NIDI,
                    "qualidade_fonte: as respostas de IA do verso divergem (54 × 29) e uma atribui o 29 à banca "
                    "sem base; adotado o conceito amplo (54), coerente com a definição do próprio comentário e "
                    "com o fechamento TC −55 + 54 = −1 = reservas"],
    },
    # ------------------------------------------------------------------ E1-0355
    {
        "id": "ECO-E1-0355-1", "fonte_ref": "E1-0355", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às necessidades de financiamento do setor público.",
        "rotulo_item": "Item",
        "assertiva": ("As necessidades de financiamento do setor público (NFSP) correspondem ao deficit público "
                      "nominal apurado ano a ano."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As necessidades de financiamento do setor público (NFSP) correspondem ao <u>deficit público "
                      "nominal</u> apurado <u>ano a ano</u>."),
        "poucas": ("Sem qualificação, " + azb("NFSP") + " = resultado " + azb("nominal") + ": tudo o que o setor "
                   "público precisa tomar emprestado no período para cobrir o déficit primário e os juros."),
        "destrinchando": [
            "Lógica: o resultado primário (receitas − despesas não financeiras) é a “poupança” disponível para "
            "pagar juros. Se não basta, a diferença — o " + azb("déficit nominal") + " — tem de ser financiada "
            "com nova dívida. Daí a equivalência NFSP = déficit nominal.",
            "Três medidas, uma escada: " + vd("primário") + " (sem juros) → " + vd("operacional") + " = primário "
            "+ juros reais → " + vd("nominal") + " = operacional + correção monetária (e cambial) = primário + "
            "juros nominais.",
            "NFSP é " + azb("fluxo") + " (do ano, do mês, acumulado em 12 meses); a " + azb("dívida líquida do "
            "setor público") + " (DLSP) é " + azb("estoque") + ". O fluxo alimenta o estoque: grosso modo, "
            "ΔDLSP ≈ NFSP + ajustes (câmbio, privatizações, reconhecimento de passivos).",
            "No Brasil, o " + rx("Banco Central") + " apura as NFSP “abaixo da linha”, pela variação da dívida "
            "líquida, com o sinal positivo indicando déficit.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. O que pode assustar é a falta de qualificador: "
                       "quando a banca diz só “NFSP”, entende-se o conceito nominal, o mais amplo. “Ano a ano” "
                       "sublinha que é medida de fluxo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As NFSP correspondem ao estoque da dívida líquida do setor público.”</i> → ERRADO (troca de "
            "conceito: fluxo × estoque)",
            "<i>“As NFSP no conceito primário incluem os juros nominais da dívida.”</i> → ERRADO (o primário "
            "exclui juros)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "NFSP = montante para honrar os compromissos com credores; se o primário não cobre os "
                            "juros, há déficit nominal financiado com títulos — daí a equivalência.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE/CACD 2019 (marca de ano da fonte; órgão e banca não informados)"],
    },
    # ------------------------------------------------------------------ E1-0357
    {
        "id": "ECO-E1-0357-1", "fonte_ref": "E1-0357", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à apuração do resultado fiscal do setor público.",
        "rotulo_item": "Item",
        "assertiva": ("As estatísticas fiscais calculadas pelo critério “acima da linha” correspondem às medidas de "
                      "receitas e despesas relacionadas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As estatísticas fiscais calculadas pelo critério “<u>acima da linha</u>” correspondem às "
                      "medidas de <u>receitas e despesas</u> relacionadas."),
        "poucas": ("“" + azb("Acima da linha") + "” = resultado apurado pelos " + azb("fluxos") + " de receitas "
                   "e despesas; “abaixo da linha” = pelo " + azb("financiamento") + ", isto é, pela variação da "
                   "dívida."),
        "destrinchando": [
            "A “linha” é a do demonstrativo: acima dela ficam as contas de resultado (receitas e despesas); "
            "abaixo, as contas patrimoniais que mostram como o saldo foi financiado (emissão ou resgate de "
            "dívida, variação de ativos).",
            azb("Acima da linha") + ": receita − despesa. No Brasil, é a apuração do " + rx("Tesouro Nacional")
            + " para o governo central (Resultado do Tesouro Nacional), em regime de caixa. Permite ver "
            "<b>onde</b> está o desequilíbrio (Previdência, pessoal, custeio).",
            azb("Abaixo da linha") + ": variação da dívida líquida, descontados ajustes patrimoniais. É a "
            "apuração oficial do " + rx("Banco Central") + " (NFSP), que cobre todo o setor público "
            "consolidado, mas não diz que receita ou despesa causou o resultado.",
            "As duas medidas deveriam coincidir; a diferença é a " + azb("discrepância estatística") + " (datas "
            "de registro, cobertura, ajustes).",
            vm("Regra-âncora: acima da linha = receitas − despesas; abaixo da linha = variação da dívida."),
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição. A redação vaga (“receitas e despesas "
                       "relacionadas”) faz o candidato desconfiar; o ponto é só saber qual critério usa fluxos e "
                       "qual usa a dívida. 🔥 A banca inverte os dois com frequência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As estatísticas fiscais calculadas pelo critério acima da linha correspondem à variação da "
            "dívida líquida do setor público.”</i> → ERRADO (inversão: isso é o abaixo da linha)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Acima da linha = contas de resultado (receitas − despesas); abaixo da linha = contas "
                            "patrimoniais, variação da dívida (NFSP).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE/CACD 2019 (marca de ano da fonte; órgão e banca não informados)",
                    "quase_duplicata: ECO-E2-L00446-1 e ECO-E2-L00946-1 (acima × abaixo da linha)"],
    },
    # ------------------------------------------------------------------ E1-0358
    {
        "id": "ECO-E1-0358-1", "fonte_ref": "E1-0358", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, relativo às necessidades de financiamento do setor público.",
        "rotulo_item": "Item",
        "assertiva": "Uma política fiscal expansionista tende a reduzir as NFSP.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma política fiscal expansionista tende a ") + vm("reduzir") + az(" as NFSP."),
        "poucas": ("Expansão fiscal = mais gasto e/ou menos tributo → piora o " + azb("resultado primário")
                   + " → " + vd("eleva") + " as NFSP (e, se mantida, a dívida)."),
        "destrinchando": [
            azb("Política fiscal expansionista") + ": aumento de gastos do governo, redução da carga tributária "
            "ou combinação das duas. Efeito direto: o primário piora (menor superávit ou maior déficit).",
            "Como NFSP nominal = déficit primário + juros nominais, a piora do primário aumenta a necessidade de "
            "financiamento <b>diretamente</b>. Há ainda um canal indireto: mais dívida e expectativas fiscais "
            "piores tendem a elevar a taxa de juros dos títulos, o que aumenta a conta de juros.",
            "Contra-argumento que a banca pode explorar: em recessão profunda, o estímulo eleva a renda e a "
            "arrecadação (efeito dos " + azb("estabilizadores automáticos") + " e do multiplicador). Esse efeito "
            "atenua, mas, salvo casos extremos, não anula o impacto direto — por isso o item fala em "
            "“tende a”, e a tendência é de <b>alta</b>.",
            "Sinal das NFSP no " + rx("Brasil") + ": positivo = déficit. Elevar as NFSP = gastar mais do que se "
            "arrecada.",
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sentido do efeito. O “tende a” dá aparência de "
                       "prudência, mas a tendência descrita está ao contrário. Quem pensa no multiplicador "
                       "(“a economia cresce e arrecada mais”) cai na armadilha."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma política fiscal contracionista tende a reduzir as NFSP.”</i> → CERTO",
            "<i>“Uma política fiscal expansionista, por elevar a renda, necessariamente reduz a relação "
            "dívida/PIB.”</i> → ERRADO (modulador absoluto e nexo indevido)",
        ])],
        "reescrita": ("Uma política fiscal expansionista tende a " + hl("elevar") + " as NFSP."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Expansão fiscal piora o resultado orçamentário e eleva as NFSP, pressionando o "
                            "endividamento e os juros.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: CEBRASPE/CACD 2019 (marca de ano da fonte; órgão e banca não informados)"],
    },
    # ------------------------------------------------------------------ E1-0361
    {
        "id": "ECO-E1-0361-1", "fonte_ref": "E1-0361", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2012, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos conceitos de necessidades de financiamento do setor público.",
        "rotulo_item": "Item",
        "assertiva": ("As necessidades de financiamento no setor público, no conceito operacional, incluem a "
                      "correção monetária, aplicando-se, portanto, a taxa de juros nominal sobre o estoque da "
                      "dívida pública."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As necessidades de financiamento no setor público, no conceito operacional, ")
                   + vm("incluem") + az(" a correção monetária, aplicando-se, portanto, a taxa de juros ")
                   + vm("nominal") + az(" sobre o estoque da dívida pública."),
        "poucas": ("O conceito " + azb("operacional") + " existe justamente para <b>tirar</b> a correção "
                   "monetária: aplica-se a taxa de juros " + vd("real") + ". Quem usa a nominal é o conceito "
                   "nominal."),
        "destrinchando": [
            "Em fórmula (B = estoque da dívida): " + vd("NFSP nominal = G − T + i·B") + "; "
            + vd("NFSP operacional = G − T + r·B") + "; " + vd("NFSP primária = G − T") + ", com i ≈ r + π.",
            "Origem histórica: a " + azb("correção monetária") + " foi institucionalizada no PAEG (governo "
            "Castelo Branco, 1964–1967). Nos anos 1980, com inflação muito alta, os juros nominais passaram a "
            "conter sobretudo a reposição do valor real da dívida — não era “gasto novo”, mas o déficit nominal "
            "explodia. Criou-se então o conceito operacional para medir o desequilíbrio <b>real</b>.",
            "Por isso, com inflação alta, o nominal superestima o desequilíbrio, e o operacional é a medida "
            "mais informativa; com inflação baixa, nominal e operacional se aproximam.",
            "Hoje o " + rx("Banco Central") + " divulga NFSP nominal e primária; o operacional caiu em desuso "
            "com a estabilização, mas segue cobrado em prova pela lógica da escada primário → operacional → "
            "nominal.",
            vm("Regra-âncora: operacional = primário + juros reais; nominal = operacional + correção monetária."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item descreve com precisão o conceito <b>nominal</b> e o "
                       "rotula de operacional. Coerente por dentro (“incluem correção → juros nominais”), só "
                       "erra a etiqueta. Pista: “operacional” sempre aparece associado a “real”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As NFSP, no conceito nominal, incluem a correção monetária, aplicando-se a taxa de juros nominal "
            "sobre o estoque da dívida.”</i> → CERTO",
            "<i>“O resultado operacional difere do primário pela correção monetária da dívida.”</i> → ERRADO "
            "(difere pelos juros reais)",
        ])],
        "reescrita": ("As necessidades de financiamento no setor público, no conceito operacional, "
                      + hl("excluem") + " a correção monetária, aplicando-se, portanto, a taxa de juros "
                      + hl("real") + " sobre o estoque da dívida pública."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Correção monetária (PAEG) inflava a dívida nos anos 1980; o conceito operacional "
                            "desconta a correção monetária e aplica o juro real: NFSP operacional = G − T + r·B.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "00041.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}],
        "alertas": ["banca_provavel: CEBRASPE/CACD 2012 (marca de ano da fonte; órgão e banca não informados)"],
    },
    # ------------------------------------------------------------------ E1-0440
    {
        "id": "ECO-E1-0440-1", "fonte_ref": "E1-0440", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Clipping", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("A política fiscal é instrumento central para o equilíbrio macroeconômico e a sustentabilidade "
                    "da dívida pública. Com base nisso, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O equilíbrio orçamentário estrutural é aquele que considera as receitas e despesas do governo "
                      "ajustadas pelo ciclo econômico, refletindo uma visão de longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O equilíbrio orçamentário estrutural é aquele que considera as receitas e despesas do governo "
                      "<u>ajustadas pelo ciclo econômico</u>, refletindo uma visão de longo prazo."),
        "poucas": ("O " + azb("resultado estrutural") + " (ciclicamente ajustado) estima o saldo que o governo "
                   "teria com a economia no " + azb("produto potencial") + ", livre das oscilações do ciclo."),
        "destrinchando": [
            "Na recessão a arrecadação cai e gastos como o seguro-desemprego sobem sozinhos; no boom, o "
            "contrário. São os " + azb("estabilizadores automáticos") + ": melhoram ou pioram o resultado "
            "observado sem nenhuma decisão de política.",
            "O resultado estrutural retira esse componente cíclico (usando o hiato do produto e as "
            "elasticidades da receita e da despesa ao ciclo) e, em geral, também os " + azb("eventos não "
            "recorrentes") + " (receitas extraordinárias, concessões, operações contábeis pontuais).",
            "Uso: medir a <b>orientação</b> da política fiscal. A variação do resultado estrutural é o "
            + azb("impulso fiscal") + ": se o estrutural piora, a política foi expansionista, ainda que o "
            "resultado observado tenha melhorado por causa do crescimento.",
            "Limite: depende do produto potencial, variável não observável e sujeita a revisões — por isso o "
            "estrutural é uma estimativa, não um dado contábil como o primário ou o nominal.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. A expressão “visão de longo prazo” poderia "
                       "parecer exagero, mas é o próprio sentido de neutralizar o ciclo: o estrutural mostra a "
                       "situação fiscal “permanente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado estrutural incorpora os efeitos dos estabilizadores automáticos sobre as contas "
            "públicas.”</i> → ERRADO (inversão: ele os remove)",
            "<i>“Uma melhora do resultado primário observado prova que a política fiscal foi "
            "contracionista.”</i> → ERRADO (pode ser só efeito do ciclo)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Resultado estrutural filtra os efeitos temporários do ciclo; indica o saldo com a "
                            "economia no potencial; mede melhor a orientação da política fiscal.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0542 (mesmo item; comentários fundidos)"],
    },
    # ------------------------------------------------------------------ E1-0661
    {
        "id": "ECO-E1-0661-1", "fonte_ref": "E1-0661", "destino": "19", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_CACD25,
        "rotulo_item": "Item",
        "assertiva": ("Quanto maior for a relação entre a dívida externa e o produto interno bruto de um país, maior "
                      "será seu risco de inadimplência."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto maior for a relação entre a <u>dívida externa e o produto interno bruto</u> de um país, "
                      "maior será seu risco de inadimplência."),
        "poucas": ("Dívida externa/PIB é indicador de " + azb("solvência") + ": quanto maior, maior a parcela da "
                   "produção comprometida com credores externos e maior o " + vd("risco de default") + "."),
        "destrinchando": [
            "Os indicadores de endividamento externo se dividem em dois grupos. " + azb("Liquidez") + " (curto "
            "prazo): capacidade de honrar o que vence logo — reservas/dívida de curto prazo, reservas/serviço "
            "da dívida, reservas em meses de importação. " + azb("Solvência") + " (médio e longo prazo): "
            "capacidade de sustentar o estoque — dívida/PIB, dívida/exportações, serviço da dívida/exportações, "
            "juros/exportações.",
            "Dívida/PIB compara o estoque devido com o tamanho da economia que vai gerar renda para pagá-lo. "
            "Razão alta: o país precisa transferir mais recursos ao exterior (superávits comerciais maiores, "
            "absorção interna menor), o refinanciamento fica mais caro e o prêmio de risco sobe.",
            "Limitação: o PIB é medido em moeda local e a dívida em moeda estrangeira. Uma depreciação forte "
            "eleva a razão de uma vez — o canal do " + azb("descasamento cambial") + " das crises dos anos 1980 "
            "e 1990. Por isso a banca combina o indicador com dívida/exportações.",
            "Referência " + rx("brasileira") + ": a acumulação de reservas nos anos 2000 tornou o país "
            "credor externo líquido (reservas acima da dívida externa total) a partir de 2008, o que reduziu "
            "sua vulnerabilidade a choques externos.",
        ],
        "dissecando": (cz("[literalidade]") + " Relação direta e intuitiva, cobrada como definição do indicador. "
                       "A estrutura “quanto maior… maior” lembra modulador absoluto, mas aqui descreve a "
                       "própria lógica do índice (mantido o resto constante)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A relação dívida externa/PIB é um indicador de liquidez externa de curto prazo.”</i> → ERRADO "
            "(troca de conceito: é de solvência)",
            "<i>“Uma depreciação cambial forte tende a elevar a relação dívida externa/PIB.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["quanto maior"], "dificuldade": 1,
        "comentario_fonte": "Dívida externa/PIB é indicador de solvência; quanto maior, maior a parcela da produção "
                            "necessária para quitar compromissos externos e o risco percebido; FMI usa também "
                            "dívida/exportações e serviço/exportações.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0662
    {
        "id": "ECO-E1-0662-1", "fonte_ref": "E1-0662", "destino": "19", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_CACD25,
        "rotulo_item": "Item",
        "assertiva": ("A razão entre o serviço da dívida externa e as exportações mede a parcela das receitas de "
                      "exportação utilizada para cobrir os pagamentos do principal, exceto juros, de maneira que um "
                      "elevado índice não significa maior risco de superendividamento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A razão entre o serviço da dívida externa e as exportações mede a parcela das receitas de "
                      "exportação utilizada para cobrir os pagamentos do principal") + vm(", exceto juros")
                   + az(", de maneira que um elevado índice ") + vm("não significa") + az(" maior risco de "
                   "superendividamento."),
        "poucas": (azb("Serviço da dívida") + " = " + vd("amortizações + juros") + ". E índice alto significa "
                   "<b>mais</b> risco: grande parte das divisas de exportação já está comprometida com credores."),
        "destrinchando": [
            "Serviço da dívida externa é o total pago no período para honrar a dívida: principal que vence "
            "(amortização) <b>e</b> juros. Indicador vizinho que isola os juros: " + vd("juros/exportações") + ".",
            "Por que exportações no denominador: são a fonte autônoma de " + azb("divisas") + " de um país em "
            "desenvolvimento. A razão compara a necessidade de pagamento com a capacidade de gerar moeda forte "
            "para fazê-lo.",
            "Leitura: índice elevado → pouca folga cambial, maior dependência de rolagem e de capital externo, "
            "maior risco de crise de balanço de pagamentos. Na crise da dívida dos anos 1980, os latino-"
            "americanos chegaram a comprometer parcela muito alta das exportações com o serviço da dívida.",
            "Classificação: serviço/exportações é usado como indicador de solvência (médio prazo) por muitos "
            "manuais e também como sinal de pressão de liquidez; o que a banca cobra é a composição "
            "(principal + juros) e o sentido da relação (maior = pior).",
            vm("Regra-âncora: serviço = principal + juros; mais alto o índice, mais vulnerável o país."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Dois erros empilhados: tira os juros do serviço da "
                       "dívida e nega a consequência lógica do índice. A pista é o “exceto juros”: qualquer "
                       "definição de serviço da dívida inclui juros."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A razão entre o serviço da dívida externa e as exportações mede a parcela das receitas de "
            "exportação comprometida com o pagamento de juros e amortizações.”</i> → CERTO",
            "<i>“A razão entre juros da dívida externa e exportações inclui as amortizações do período.”</i> → "
            "ERRADO (troca de conceito: só juros)",
        ])],
        "reescrita": ("A razão entre o serviço da dívida externa e as exportações mede a parcela das receitas de "
                      "exportação utilizada para cobrir os pagamentos do principal" + hl(" e dos juros")
                      + ", de maneira que um elevado índice " + hl("significa") + " maior risco de "
                      "superendividamento."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": ["exceto"], "dificuldade": 1,
        "comentario_fonte": "Serviço da dívida inclui principal e juros; índice elevado significa maior parcela "
                            "das receitas externas comprometida e maior risco de superendividamento.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0663
    {
        "id": "ECO-E1-0663-1", "fonte_ref": "E1-0663", "destino": "19", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_CACD25,
        "rotulo_item": "Item",
        "assertiva": ("Quanto mais baixa a proporção na relação entre dívida externa e exportações, maior a "
                      "vulnerabilidade do país, pois a flutuação na receita de exportação indica dificuldades em "
                      "cumprir as obrigações da dívida pública."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto mais baixa a proporção na relação entre dívida externa e exportações, ")
                   + vm("maior") + az(" a vulnerabilidade do país, pois ")
                   + vm("a flutuação na receita de exportação indica dificuldades em cumprir as obrigações da "
                        "dívida pública") + az("."),
        "poucas": ("Dívida externa/exportações " + vd("baixa") + " = dívida pequena diante da capacidade de gerar "
                   "divisas = " + azb("menor") + " vulnerabilidade. O item inverte a lógica do indicador."),
        "destrinchando": [
            "A razão dívida externa/exportações diz quantos anos de exportação seriam necessários para quitar o "
            "estoque da dívida. Indicador de " + azb("solvência") + " (médio e longo prazo).",
            "Razão alta → o país precisaria comprometer muitos anos de receitas externas → maior risco de "
            "insolvência. Razão baixa → folga para honrar os compromissos → menor vulnerabilidade.",
            "A justificativa do item também falha: a <b>volatilidade</b> das exportações é outro fator de risco "
            "(países dependentes de commodities), mas não decorre de a razão ser baixa; e o indicador trata de "
            "dívida <b>externa</b>, não de dívida pública em geral.",
            "Variante usada pelos analistas: " + azb("dívida externa líquida") + " (dívida − reservas) / "
            "exportações, que desconta os ativos de reserva já disponíveis.",
            vm("Regra-âncora: em todo indicador dívida/capacidade de pagamento, maior razão = maior risco."),
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " Troca o sentido da relação e cola uma justificativa "
                       "que não decorre do indicador (volatilidade das exportações). A pista é testar o caso "
                       "extremo: dívida quase zero (razão baixa) seria “mais vulnerável”? Absurdo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto mais baixa a relação entre dívida externa e exportações, menor a vulnerabilidade "
            "externa do país.”</i> → CERTO",
            "<i>“A relação dívida externa/exportações é indicador de liquidez externa de curtíssimo prazo.”</i> → "
            "ERRADO (troca de conceito: é de solvência)",
        ])],
        "reescrita": ("Quanto mais baixa a proporção na relação entre dívida externa e exportações, " + hl("menor")
                      + " a vulnerabilidade do país, pois " + hl("menor é a parcela das receitas de exportação "
                      "necessária para cumprir as obrigações da dívida externa") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": ["quanto mais baixa"], "dificuldade": 1,
        "comentario_fonte": "Dívida/exportações é indicador de solvência; quanto mais baixa, menor a "
                            "vulnerabilidade, pois menor a necessidade de receita para honrar compromissos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0664
    {
        "id": "ECO-E1-0664-1", "fonte_ref": "E1-0664", "destino": "19", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_CACD25,
        "rotulo_item": "Item",
        "assertiva": ("A relação entre dívida externa de curto prazo e reservas internacionais mede a capacidade de "
                      "um país de liquidar sua dívida externa rapidamente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A relação entre dívida externa de <u>curto prazo</u> e <u>reservas internacionais</u> mede "
                      "a capacidade de um país de liquidar sua dívida externa rapidamente."),
        "poucas": ("É indicador de " + azb("liquidez externa") + ": compara o que vence em até um ano com o "
                   "“colchão” imediato de divisas. Razão " + vd("≤ 1") + " = reservas cobrem o curto prazo."),
        "destrinchando": [
            "Liquidez trata do que é exigível já. Uma dívida enorme que vence em 20 anos não pressiona as "
            "reservas hoje; a de curto prazo (vencimento em até 12 meses, inclusive a parcela de longo prazo "
            "que vence no período, em versões mais rigorosas) sim.",
            azb("Regra de Guidotti–Greenspan") + ": as reservas devem cobrir ao menos " + vd("100%") + " da "
            "dívida externa de curto prazo, para que o país atravesse um ano sem acesso a crédito externo. É "
            "a referência usada pelo FMI e por agências de risco.",
            "Outros indicadores de liquidez: reservas/serviço da dívida, reservas em meses de importação "
            "(referência tradicional: ao menos " + vd("3 meses") + "), reservas/M2 (risco de fuga de capitais "
            "domésticos). Os de solvência (dívida/PIB, dívida/exportações) olham o estoque e o médio prazo.",
            "A crise asiática de 1997 é o caso clássico: países com fundamentos fiscais razoáveis, mas dívida "
            "de curto prazo maior que as reservas, sofreram parada súbita de capitais.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição do indicador. A palavra decisiva é “rapidamente”, "
                       "que casa com “curto prazo” e “reservas” (ativo líquido). 🔥 A banca alterna liquidez e "
                       "solvência no mesmo bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A relação entre dívida externa de curto prazo e reservas internacionais é um indicador de "
            "solvência de longo prazo.”</i> → ERRADO (troca de conceito: é de liquidez)",
            "<i>“Razão superior a 1 entre dívida de curto prazo e reservas sinaliza vulnerabilidade externa.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Indicador de liquidez externa: compara a dívida que vence em até um ano com as "
                            "reservas; razão ≤ 1 = liquidez confortável; > 1 = vulnerabilidade.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00070
    {
        "id": "ECO-E2-L00070-1", "fonte_ref": "E2-L00070", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Julgue o item a respeito da medição do desempenho fiscal do governo no contexto da economia do "
                    "setor público."),
        "rotulo_item": "Item",
        "assertiva": ("A necessidade de financiamento do setor público (NFSP) nominal reflete diretamente o déficit "
                      "nominal, incluindo a totalidade das despesas financeiras e operacionais. Essa necessidade "
                      "considera a soma das despesas do governo para manter sua estrutura e pagar juros, ajustados "
                      "pelas receitas financeiras, formando um dos indicadores mais abrangentes da saúde fiscal do "
                      "governo ao englobar todos os compromissos financeiros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A necessidade de financiamento do setor público (NFSP) nominal reflete diretamente o déficit "
                      "nominal, incluindo a totalidade das despesas financeiras e operacionais. Essa necessidade "
                      "considera a soma das despesas do governo para manter sua estrutura e pagar juros, "
                      "<u>ajustados pelas receitas financeiras</u>, formando um dos indicadores <u>mais "
                      "abrangentes</u> da saúde fiscal do governo ao englobar todos os compromissos financeiros."),
        "poucas": ("NFSP " + azb("nominal") + " = déficit nominal = déficit primário + " + vd("juros nominais "
                   "líquidos") + " (pagos menos recebidos). É a medida mais ampla do desequilíbrio fiscal."),
        "destrinchando": [
            "Decomposição: despesas para “manter a estrutura” (pessoal, custeio, investimento, transferências) "
            "são as " + azb("despesas primárias") + "; somando os juros e descontando as receitas financeiras "
            "(juros recebidos sobre ativos do setor público), chega-se ao resultado nominal.",
            "Por que “mais abrangente”: o nominal inclui tudo o que o setor público precisa financiar — a "
            "parte que depende das decisões correntes de gasto e receita (primário) e a herança do estoque de "
            "dívida (juros reais e correção monetária).",
            "Por que não é a única medida útil: o nominal mistura esforço fiscal com política monetária (a Selic "
            "move os juros). Para avaliar o esforço do governo, olha-se o " + azb("primário") + "; com inflação "
            "alta, o " + azb("operacional") + " evita superestimar o desequilíbrio.",
            "No " + rx("Brasil") + ", o Banco Central apura as NFSP abaixo da linha, com juros apropriados por "
            "competência, para governo central, governos regionais e estatais (exceto Petrobras e Eletrobras).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item longo e prolixo, que repete a definição com outras palavras. "
                       "O risco está em “despesas operacionais”, que pode ser confundido com o conceito "
                       "operacional — aqui é só “despesas de funcionamento”. Nada no item restringe ou inverte "
                       "a definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A NFSP nominal exclui a correção monetária da dívida, aplicando-se a taxa de juros real.”</i> → "
            "ERRADO (troca de conceito: isso é o operacional)",
            "<i>“A NFSP nominal é a soma do déficit primário com os juros nominais líquidos.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "NFSP nominal reflete o déficit nominal ampliado, com juros e despesas operacionais; "
                            "indica integralmente as exigências fiscais.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00084
    {
        "id": "ECO-E2-L00084-1", "fonte_ref": "E2-L00084", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_NFSP,
        "rotulo_item": "Item",
        "assertiva": ("A necessidade de financiamento do setor público (NFSP) primária é calculada considerando "
                      "apenas as despesas e receitas financeiras de um governo, sem incluir despesas de juros, "
                      "sendo crucial para entender o tamanho real da dívida fiscal líquida do governo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A necessidade de financiamento do setor público (NFSP) primária é calculada considerando "
                      "apenas as despesas e receitas ") + vm("financeiras") + az(" de um governo, sem incluir "
                      "despesas de juros, sendo crucial para entender ") + vm("o tamanho real da dívida fiscal "
                      "líquida") + az(" do governo."),
        "poucas": ("O " + azb("primário") + " usa só receitas e despesas " + vd("não financeiras") + ". E ele "
                   "mede o " + azb("esforço fiscal") + " corrente, não o tamanho da dívida (que é estoque)."),
        "destrinchando": [
            "Primário = receitas primárias − despesas primárias. Ficam fora as receitas financeiras (juros sobre "
            "ativos, retorno de empréstimos) e as despesas financeiras (juros e amortizações). O item é "
            "contraditório por dentro: “apenas financeiras” e “sem juros” ao mesmo tempo.",
            "Para que serve o primário: medir quanto o governo economiza (ou gasta além) com suas decisões "
            "correntes, sem o peso da herança da dívida. É a base das metas fiscais brasileiras desde 1999 e "
            "do arcabouço de 2023 (" + vd("Lei Complementar 200/2023") + ").",
            "O tamanho da dívida é medido por " + azb("estoques") + " (DLSP, DBGG). A ligação entre os dois é "
            "dinâmica: o " + azb("primário necessário para estabilizar a dívida/PIB") + " ≈ (r − g)·d, em que r "
            "é o juro real, g o crescimento e d a dívida/PIB.",
            "Escada dos conceitos: primário → + juros reais = operacional → + correção monetária = nominal.",
            vm("Regra-âncora: primário = não financeiro; a dívida é estoque, o primário é fluxo."),
        ],
        "dissecando": (cz("[troca de conceito · extrapolação]") + " Troca “não financeiras” por “financeiras” — "
                       "e a contradição com “sem incluir despesas de juros” é a pista. Depois atribui ao primário "
                       "uma função que é dos indicadores de estoque."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A NFSP primária considera apenas receitas e despesas não financeiras e mede o esforço fiscal "
            "corrente do governo.”</i> → CERTO",
            "<i>“Superávit primário positivo garante a queda da dívida líquida.”</i> → ERRADO (modulador "
            "absoluto: depende de cobrir os juros reais)",
        ])],
        "reescrita": ("A necessidade de financiamento do setor público (NFSP) primária é calculada considerando "
                      "apenas as despesas e receitas " + hl("não financeiras") + " de um governo, sem incluir "
                      "despesas de juros, sendo crucial para entender " + hl("o esforço fiscal corrente") + " do "
                      "governo."),
        "tipo_erro": ["TROCA_CONCEITO", "EXTRAPOLACAO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": "NFSP primária considera apenas receitas e despesas não financeiras, sem juros; não está "
                            "diretamente ligada ao tamanho da dívida fiscal líquida.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00087
    {
        "id": "ECO-E2-L00087-1", "fonte_ref": "E2-L00087", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_NFSP,
        "rotulo_item": "Item",
        "assertiva": ("A análise acima da linha considera o regime de competência e trata de como o governo apura "
                      "suas contas pelo desempenho diário de suas receitas e despesas, incluindo todas as suas "
                      "obrigações financeiras."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A análise acima da linha considera o ") + vm("regime de competência") + az(" e trata de "
                      "como o governo apura suas contas pelo desempenho diário de suas receitas e despesas, "
                      "incluindo todas as suas obrigações financeiras."),
        "poucas": ("A apuração " + azb("acima da linha") + " (Tesouro) segue o " + vd("regime de caixa")
                   + ": receitas e despesas entram quando o dinheiro efetivamente entra ou sai."),
        "destrinchando": [
            azb("Acima da linha") + ": receitas − despesas, registradas quando arrecadadas e pagas (caixa). É "
            "o Resultado do " + rx("Tesouro Nacional") + " para o governo central, que detalha a origem do "
            "resultado (Previdência, pessoal, custeio, investimento).",
            azb("Abaixo da linha") + ": variação da dívida líquida, apurada pelo " + rx("Banco Central") + " "
            "para todo o setor público. Nela os juros são apropriados por " + vd("competência") + " (no período "
            "em que incorrem, não quando são pagos).",
            "Por isso as duas medidas não coincidem exatamente: além das diferenças de cobertura, há diferença "
            "de critério temporal. O saldo entre elas é a " + azb("discrepância estatística") + ".",
            "Lembrete de vocabulário contábil: " + azb("competência") + " registra o fato gerador; "
            + azb("caixa") + " registra o fluxo financeiro. Restos a pagar, por exemplo, são despesa por "
            "competência ainda não paga em caixa.",
            vm("Regra-âncora: acima da linha = Tesouro, caixa; abaixo da linha = BCB, variação da dívida."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca o regime contábil. O resto da frase é vago "
                       "(“desempenho diário”, “todas as obrigações”) e serve de cortina de fumaça; o ponto "
                       "decisivo é “competência” no lugar de “caixa”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A análise acima da linha considera o regime de caixa e apura o resultado pela diferença entre "
            "receitas e despesas.”</i> → CERTO",
            "<i>“A análise abaixo da linha permite identificar quais despesas causaram o déficit.”</i> → ERRADO "
            "(inversão: isso é próprio do acima da linha)",
        ])],
        "reescrita": ("A análise acima da linha considera o " + hl("regime de caixa") + " e trata de como o governo "
                      "apura suas contas pelo desempenho diário de suas receitas e despesas, incluindo todas as "
                      "suas obrigações financeiras."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Acima da linha considera o regime de caixa (receitas e despesas que entram e saem); "
                            "o regime de competência é aplicado no abaixo da linha, que mede a variação da dívida.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00446
    {
        "id": "ECO-E2-L00446-1", "fonte_ref": "E2-L00446", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": ("A respeito das contas nacionais, do balanço de pagamentos, das contas públicas e do sistema "
                    "monetário, julgue o item seguinte."),
        "rotulo_item": "Item",
        "assertiva": ("O resultado fiscal denominado “acima da linha” refere-se à apuração do resultado primário ou "
                      "nominal com base nas receitas e despesas efetivamente realizadas, enquanto o resultado "
                      "“abaixo da linha” é medido pela variação do endividamento líquido."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O resultado fiscal denominado “acima da linha” refere-se à apuração do resultado primário ou "
                      "nominal com base nas <u>receitas e despesas efetivamente realizadas</u>, enquanto o "
                      "resultado “abaixo da linha” é medido pela <u>variação do endividamento líquido</u>."),
        "poucas": ("Dois caminhos para o mesmo resultado: pelos " + azb("fluxos") + " (receitas − despesas, acima "
                   "da linha) ou pelo " + azb("financiamento") + " (variação da dívida líquida, abaixo da linha)."),
        "destrinchando": [
            "Se o governo gastou mais do que arrecadou, a diferença foi coberta por dívida nova ou por venda de "
            "ativos. Medir a receita e a despesa (acima) ou medir a dívida (abaixo) deveria dar o mesmo número.",
            "As duas permitem apurar o " + vd("primário") + " e o " + vd("nominal") + ": acima da linha, "
            "incluindo ou não os juros; abaixo da linha, pela variação da dívida líquida com ou sem os juros "
            "apropriados.",
            "No " + rx("Brasil") + ": o Tesouro publica o resultado acima da linha do governo central; o Banco "
            "Central publica as NFSP abaixo da linha para todo o setor público consolidado — é a estatística "
            "oficial para as metas fiscais.",
            "Vantagens de cada um: acima da linha mostra a <b>composição</b> (que despesa cresceu); abaixo da "
            "linha tem maior <b>cobertura</b> e confiabilidade, porque se apoia nos registros do sistema "
            "financeiro.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição correta dos dois critérios na mesma frase. O item "
                       "testa se o candidato sabe que primário e nominal podem ser apurados pelos dois métodos e "
                       "não confunde qual usa a dívida. 🔥 Cobrança recorrente em provas de ECO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado acima da linha é medido pela variação do endividamento líquido.”</i> → ERRADO "
            "(inversão)",
            "<i>“O resultado primário só pode ser apurado pelo critério acima da linha.”</i> → ERRADO (restrição "
            "indevida)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Acima da linha = receitas − despesas orçamentárias; abaixo da linha = como o déficit "
                            "foi financiado, pela variação da dívida líquida.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0357-1 e ECO-E2-L00946-1 (acima × abaixo da linha)"],
    },
    # ------------------------------------------------------------------ E2-L00596
    {
        "id": "ECO-E2-L00596-1", "fonte_ref": "E2-L00596", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação aos conceitos macroeconômicos, julgue o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("O superávit fiscal no conceito operacional é calculado pela diferença entre receitas e despesas "
                      "governamentais, excluindo os pagamentos de juros nominais que incidem sobre as dívidas do "
                      "governo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O superávit fiscal no conceito ") + vm("operacional") + az(" é calculado pela diferença "
                      "entre receitas e despesas governamentais, excluindo os pagamentos de juros nominais que "
                      "incidem sobre as dívidas do governo."),
        "poucas": ("Excluir <b>todos</b> os juros nominais define o " + azb("primário") + ". O "
                   + azb("operacional") + " exclui só a " + vd("correção monetária") + " e mantém os juros "
                   "reais."),
        "destrinchando": [
            "Juros nominais = juros reais + correção monetária (e cambial) da dívida. Cada conceito tira uma "
            "fatia: o " + vd("primário") + " tira tudo; o " + vd("operacional") + " tira só a correção; o "
            + vd("nominal") + " não tira nada.",
            "Em fórmula: primário = T − G; operacional = T − G − r·B; nominal = T − G − i·B (escrito como "
            "superávit; com sinal trocado, como NFSP).",
            "Exemplo: receitas 100, despesas primárias 95, dívida 200, juros reais 3%, inflação 4%. Primário = "
            + vd("+5") + "; operacional = 5 − 6 = " + vd("−1") + "; nominal = 5 − 14 = " + vd("−9") + ".",
            "O operacional nasceu no " + rx("Brasil") + " dos anos 1980 para separar o efeito da inflação sobre "
            "a dívida; hoje o Banco Central divulga oficialmente o primário e o nominal.",
            vm("Regra-âncora: sem juros = primário; sem correção monetária = operacional."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A definição é exatamente a do primário, rotulada como "
                       "operacional. Pista: “juros nominais” excluídos por inteiro — se fosse operacional, o item "
                       "falaria em excluir só a correção monetária."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O superávit operacional é o superávit primário menos os juros reais da dívida.”</i> → CERTO",
            "<i>“Com inflação zero, o resultado operacional coincide com o primário.”</i> → ERRADO (coincide com "
            "o nominal)",
        ])],
        "reescrita": ("O superávit fiscal no conceito " + hl("primário") + " é calculado pela diferença entre receitas "
                      "e despesas governamentais, excluindo os pagamentos de juros nominais que incidem sobre as "
                      "dívidas do governo."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A definição é a do primário (exclui todos os juros nominais); o operacional exclui só "
                            "a correção monetária e cambial, = primário + juros reais.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00947-1 (primário × operacional)"],
    },
    # ------------------------------------------------------------------ E2-L00719
    {
        "id": "ECO-E2-L00719-1", "fonte_ref": "E2-L00719", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "No que diz respeito aos principais agregados macroeconômicos, julgue o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia com inflação elevada, a necessidade de financiamento do setor público no seu "
                      "conceito nominal tende a subestimar o desequilíbrio orçamentário do setor público."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia com inflação elevada, a necessidade de financiamento do setor público no seu "
                      "conceito nominal tende a ") + vm("subestimar") + az(" o desequilíbrio orçamentário do setor "
                      "público."),
        "poucas": ("Com inflação alta, os juros nominais embutem a " + azb("correção monetária") + " da dívida: "
                   "a NFSP nominal fica inflada e " + vd("superestima") + " o desequilíbrio real."),
        "destrinchando": [
            "Juros nominais ≈ juros reais + inflação × dívida. A parcela da inflação apenas repõe o valor real "
            "do estoque: o credor não fica mais rico, o devedor não fica mais pobre em termos reais.",
            "Exemplo (com a aproximação i ≈ r + π): dívida 100, juro real 5%, inflação 100% ao ano. Juros "
            "nominais ≈ 105; juros reais = 5. "
            "Com primário zerado, o déficit nominal é " + vd("105") + " e o operacional, " + vd("5") + ": a "
            "medida nominal multiplica por 21 o desequilíbrio efetivo.",
            "Foi esse o problema do " + rx("Brasil") + " dos anos 1980 e início dos 1990: déficits nominais "
            "enormes que, em boa parte, eram correção monetária. Para negociar metas, criou-se o conceito "
            + azb("operacional") + " (primário + juros reais).",
            "Com inflação baixa (como hoje), a distância entre nominal e operacional diminui, e a NFSP nominal "
            "volta a ser boa medida do quanto o setor público precisa se financiar.",
            vm("Regra-âncora: inflação alta → nominal superestima; operacional corrige."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido do viés. A pista está na própria lógica: a inflação "
                       "<b>adiciona</b> correção monetária aos juros, então só pode inflar a medida nominal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em uma economia com inflação elevada, a NFSP no conceito operacional é medida mais adequada do "
            "desequilíbrio do que a nominal.”</i> → CERTO",
            "<i>“Em uma economia com inflação elevada, o resultado primário superestima o desequilíbrio.”</i> → "
            "ERRADO (troca de conceito: o primário não tem juros)",
        ])],
        "reescrita": ("Em uma economia com inflação elevada, a necessidade de financiamento do setor público no seu "
                      "conceito nominal tende a " + hl("superestimar") + " o desequilíbrio orçamentário do setor "
                      "público."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "NFSP nominal inclui a totalidade dos juros nominais, que com inflação alta incorporam "
                            "a correção monetária; ela superestima, e não subestima, o desequilíbrio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L00774 (mesmo item; comentários fundidos)"],
    },
    # ------------------------------------------------------------------ E2-L00738
    {
        "id": "ECO-E2-L00738-1", "fonte_ref": "E2-L00738", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NFSP_TAB,
        "excerto_tabela": TAB_NFSP,
        "rotulo_item": "Item",
        "assertiva": ("Em 2022, observou-se um déficit primário de R$ 126 bilhões, o que foi compensado pelo bom "
                      "desempenho das contas no ano seguinte, evidenciado pelo superávit primário de R$ 249,1 "
                      "bilhões."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em 2022, observou-se um ") + vm("déficit") + az(" primário de R$ 126 bilhões, ")
                   + vm("o que foi compensado pelo bom desempenho das contas no ano seguinte, evidenciado pelo "
                        "superávit") + az(" primário de R$ 249,1 bilhões."),
        "poucas": ("Nas " + azb("NFSP") + ", sinal positivo = <b>déficit</b>; negativo = <b>superávit</b>. Houve "
                   + vd("superávit primário em 2022") + " (−126,0) e " + vd("déficit primário em 2023")
                   + " (249,1): o item inverte os dois anos."),
        "destrinchando": [
            azb("Necessidades de financiamento") + " medem quanto o setor público precisa tomar emprestado. Por "
            "isso o déficit entra com sinal <b>positivo</b> (há necessidade de financiamento) e o superávit com "
            "sinal negativo. É a convenção do " + rx("Banco Central do Brasil") + " (critério abaixo da linha).",
            "Conferência pela identidade " + vd("nominal = primário + juros nominais") + ": −126,0 + 586,4 = "
            + vd("460,4") + " (4,6% do PIB) em 2022; 249,1 + 718,3 = " + vd("967,4") + " (8,9%) em 2023.",
            "Leitura econômica: em 2022, o superávit primário (receitas infladas por commodities e inflação "
            "alta) conviveu com déficit nominal de 4,6% do PIB, puxado pelos juros. Em 2023, a virada para "
            "déficit primário, somada a juros maiores, levou o nominal a 8,9% do PIB.",
            "Mesmo com superávit primário a dívida pode crescer: basta que o primário não cubra os juros. Por "
            "isso a discussão de sustentabilidade gira em torno do primário <b>necessário</b> para estabilizar a "
            "relação dívida/PIB.",
            "⏳ (out/2026) Valores de 2022–2023 conforme a tabela; as séries atualizadas estão na Nota de "
            "Estatísticas Fiscais do BCB.",
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " O item inverte a convenção de sinais das NFSP e, sobre "
                       "a inversão, constrói uma relação (“compensado pelo bom desempenho”). Quem lê “−126” como "
                       "déficit cai. 🔥 Tabela de NFSP em prova quase sempre testa o sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em 2022, o setor público apresentou superávit primário e déficit nominal.”</i> → CERTO",
            "<i>“Em 2023, o déficit nominal decorreu exclusivamente da conta de juros.”</i> → ERRADO (modulador "
            "absoluto: o primário também foi deficitário)",
        ])],
        "reescrita": ("Em 2022, observou-se um " + hl("superávit") + " primário de R$ 126 bilhões, "
                      + hl("seguido, no ano seguinte, de déficit") + " primário de R$ 249,1 bilhões."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Valores positivos = déficit; negativos = superávit. 2022: superávit primário de 126; "
                            "2023: déficit primário de 249 (2,3% do PIB).",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_NFSP_TAB,
        "alertas": list(ALERTAS_NFSP_TAB),
    },
    # ------------------------------------------------------------------ E2-L00739
    {
        "id": "ECO-E2-L00739-1", "fonte_ref": "E2-L00739", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NFSP_TAB,
        "excerto_tabela": TAB_NFSP,
        "rotulo_item": "Item",
        "assertiva": ("O resultado primário é composto pelo saldo entre as receitas e despesas, excluído o pagamento "
                      "de juros da dívida."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O resultado primário é composto pelo saldo entre as receitas e despesas, <u>excluído o "
                      "pagamento de juros</u> da dívida."),
        "poucas": (azb("Resultado primário") + " = receitas primárias − despesas primárias: fica de fora a conta "
                   "de " + vd("juros") + " (pagos e recebidos)."),
        "destrinchando": [
            "Mais precisamente, o primário exclui as receitas e despesas <b>financeiras</b>: juros pagos sobre "
            "a dívida, juros recebidos sobre ativos do setor público, amortizações e concessões/retornos de "
            "empréstimos. O item descreve a parte mais importante (juros pagos) e continua correto.",
            "Na tabela: primário de " + vd("−126,0") + " (superávit, pelo sinal das NFSP) em 2022 e "
            + vd("249,1") + " (déficit) em 2023. A diferença para o nominal é exatamente a linha dos juros "
            "nominais: 586,4 e 718,3.",
            "Por que separar: o primário mostra o resultado das decisões <b>correntes</b> de gasto e "
            "arrecadação; os juros dependem do estoque herdado e da política monetária (Selic), sobre os quais "
            "o governo do momento tem pouco controle.",
            "É a variável-alvo das regras fiscais brasileiras: metas de primário desde " + vd("1999") + " e, "
            "no arcabouço de 2023, metas com bandas de tolerância.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, em versão simplificada. O candidato que sabe "
                       "que o primário também exclui juros <b>recebidos</b> pode desconfiar por incompletude — "
                       "mas incompleto não é errado para o CEBRASPE, e o mesmo vale nos simulados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado primário é o saldo entre receitas e despesas, excluídos apenas os juros reais da "
            "dívida.”</i> → ERRADO (troca de conceito: isso se aproxima do operacional)",
            "<i>“Na tabela, o resultado primário de 2022 foi superavitário.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Primário = receitas primárias − despesas primárias, sem receitas e despesas com juros; "
                            "exclui também o recebimento de juros.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_NFSP_TAB,
        "alertas": list(ALERTAS_NFSP_TAB),
    },
    # ------------------------------------------------------------------ E2-L00740
    {
        "id": "ECO-E2-L00740-1", "fonte_ref": "E2-L00740", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NFSP_TAB,
        "excerto_tabela": TAB_NFSP,
        "rotulo_item": "Item",
        "assertiva": ("Em 2022, o resultado primário negativo sinaliza que o governo não conseguiu arcar com o "
                      "pagamento de juros da dívida naquele ano em específico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em 2022, o resultado primário ") + vm("negativo sinaliza que o governo não conseguiu arcar "
                      "com o pagamento de juros da dívida") + az(" naquele ano em específico."),
        "poucas": ("O −126,0 das NFSP é " + vd("superávit") + " primário. E nem um déficit primário impediria o "
                   "pagamento de juros: a diferença é coberta com " + azb("nova dívida") + "."),
        "destrinchando": [
            "Primeiro erro, de leitura: nas NFSP o sinal negativo indica " + azb("superávit") + ". Em 2022 o "
            "setor público economizou R$ 126 bilhões antes dos juros.",
            "Segundo erro, de conceito: o primário mede quanto o governo consegue pagar de juros <b>com recursos "
            "próprios</b>. Se ele não cobre a conta (ou é deficitário), o governo paga os juros do mesmo jeito, "
            "emitindo títulos — o resultado é o " + azb("déficit nominal") + " e o aumento da dívida, não o "
            "calote.",
            "Em 2022: superávit primário de 126 diante de juros de 586,4 → déficit nominal de " + vd("460,4")
            + ". O governo pagou com recursos próprios só parte dos juros e financiou o resto com dívida.",
            "Inadimplência de fato depende de perda de acesso ao financiamento (o mercado se recusa a rolar a "
            "dívida), não do sinal do primário num único ano.",
            vm("Regra-âncora: primário insuficiente → mais dívida (déficit nominal), não calote."),
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " Erra o sinal (superávit lido como déficit) e tira "
                       "uma consequência que não decorre nem do déficit verdadeiro. O “naquele ano em específico” "
                       "reforça a ideia falsa de que juros só se pagam com o saldo do próprio ano."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em 2022, o superávit primário foi insuficiente para cobrir os juros nominais, o que resultou em "
            "déficit nominal.”</i> → CERTO",
            "<i>“Em 2023, o déficit primário obrigou o governo a suspender o pagamento de juros.”</i> → ERRADO "
            "(nexo indevido: os juros foram financiados com dívida)",
        ])],
        "reescrita": ("Em 2022, o resultado primário " + hl("superavitário (−126,0, pois nas NFSP o sinal negativo "
                      "indica superávit) sinaliza que o governo pagou com recursos próprios parte dos juros da "
                      "dívida") + " naquele ano em específico."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Em 2022 o primário foi positivo (superávit); mesmo um déficit primário não implicaria "
                            "falta de pagamento de juros, financiados com aumento do endividamento.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_NFSP_TAB,
        "alertas": list(ALERTAS_NFSP_TAB),
    },
    # ------------------------------------------------------------------ E2-L00741
    {
        "id": "ECO-E2-L00741-1", "fonte_ref": "E2-L00741", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NFSP_TAB,
        "excerto_tabela": TAB_NFSP,
        "rotulo_item": "Item",
        "assertiva": ("Déficit Nominal é a diferença entre todas as receitas e despesas do governo, incluindo as "
                      "despesas com juros nominais da dívida e as receitas financeiras, e pode ser mensurado pelo "
                      "método abaixo da linha, a partir do resultado da variação da dívida fiscal líquida."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Déficit Nominal é a diferença entre <u>todas</u> as receitas e despesas do governo, incluindo "
                      "as despesas com juros nominais da dívida e as receitas financeiras, e <u>pode</u> ser "
                      "mensurado pelo método abaixo da linha, a partir do resultado da variação da dívida fiscal "
                      "líquida."),
        "poucas": ("O " + azb("nominal") + " é o conceito mais amplo (inclui juros pagos e recebidos) e é "
                   "justamente o que se apura " + azb("abaixo da linha") + ", pela variação da " + vd("dívida "
                   "fiscal líquida") + "."),
        "destrinchando": [
            "Nominal = primário + juros nominais líquidos. Na tabela: 460,4 em 2022 e 967,4 em 2023 — os "
            "números que as NFSP divulgam como déficit nominal.",
            azb("Dívida fiscal líquida") + " é a dívida líquida do setor público descontados os ajustes que "
            "não decorrem do resultado fiscal: variação cambial sobre dívida e ativos em moeda estrangeira, "
            "reconhecimento de passivos antigos (“esqueletos”), privatizações. Sua variação isola o efeito do "
            "déficit.",
            "Por isso o BCB apura o nominal como " + vd("ΔDFL") + " (variação da dívida fiscal líquida) e o "
            "primário como ΔDFL menos os juros nominais apropriados.",
            "O “pode” é correto: o nominal também pode ser apurado acima da linha, somando receitas e "
            "despesas (inclusive financeiras). No Brasil, o número oficial é o do BCB, abaixo da linha.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Junta duas definições corretas: a do "
                       "nominal (tudo incluído) e a do método abaixo da linha (variação da dívida). O “todas” "
                       "aqui não é generalização indevida — é o que distingue o nominal dos demais conceitos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O déficit nominal só pode ser mensurado pelo método acima da linha.”</i> → ERRADO (restrição "
            "indevida e inversão)",
            "<i>“A variação da dívida fiscal líquida inclui o efeito da desvalorização cambial sobre a dívida "
            "externa.”</i> → ERRADO (a dívida fiscal líquida exclui esses ajustes)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["todas", "pode"], "dificuldade": 2,
        "comentario_fonte": "Nominal inclui juros nominais e receitas financeiras; o método abaixo da linha observa a "
                            "variação do endividamento líquido.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_NFSP_TAB,
        "alertas": list(ALERTAS_NFSP_TAB),
    },
    # ------------------------------------------------------------------ E2-L00795
    {
        "id": "ECO-E2-L00795-1", "fonte_ref": "E2-L00795", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação ao sistema monetário e ao conceito de déficit público, julgue o item seguinte.",
        "rotulo_item": "Item",
        "assertiva": ("Déficit Primário é a diferença entre as receitas totais do governo, incluindo receitas "
                      "financeiras, e suas despesas totais, excluídas as despesas com juros da dívida."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Déficit Primário é a diferença entre as receitas ") + vm("totais do governo, incluindo "
                      "receitas financeiras") + az(", e suas despesas totais, excluídas as despesas com juros da "
                      "dívida."),
        "poucas": ("O " + azb("primário") + " exclui o lado financeiro <b>dos dois lados</b>: sai a despesa com "
                   "juros e saem também as " + vd("receitas financeiras") + "."),
        "destrinchando": [
            azb("Receitas primárias") + ": tributos, contribuições, receitas patrimoniais não financeiras "
            "(royalties, dividendos de estatais, concessões). " + azb("Receitas financeiras") + ": juros sobre "
            "aplicações e empréstimos concedidos, retorno de empréstimos, operações de crédito.",
            "A simetria importa: se se excluem os juros pagos, é preciso excluir também os juros recebidos — "
            "senão o resultado mistura gestão da dívida com esforço fiscal. O primário mede só o que o governo "
            "arrecada e gasta com sua atividade não financeira.",
            "Consequência para a análise: um governo com muitos ativos remunerados (reservas, créditos a bancos "
            "públicos) teria um primário artificialmente melhor se as receitas financeiras entrassem na conta.",
            "Nos conceitos acima: primário (sem financeiras) → operacional (+ juros reais líquidos) → nominal "
            "(+ correção monetária).",
            vm("Regra-âncora: primário = receitas não financeiras − despesas não financeiras."),
        ],
        "dissecando": (cz("[meia-verdade]") + " O lado da despesa está certo (exclui juros); o erro foi enxertado "
                       "no lado da receita, com “totais” e “incluindo receitas financeiras”. Itens desse tipo "
                       "testam a simetria do conceito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Déficit primário é a diferença entre as despesas e as receitas não financeiras do governo.”</i> → "
            "CERTO",
            "<i>“O resultado primário inclui os juros recebidos pelo setor público sobre seus ativos.”</i> → "
            "ERRADO (exclui as receitas financeiras)",
        ])],
        "reescrita": ("Déficit Primário é a diferença entre as receitas " + hl("não financeiras do governo, excluídas "
                      "as receitas financeiras") + ", e suas despesas totais, excluídas as despesas com juros da "
                      "dívida."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["totais"], "dificuldade": 1,
        "comentario_fonte": "Primário = receitas primárias − despesas primárias; receitas e despesas financeiras "
                            "(juros, privatizações) não entram.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 117", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00946
    {
        "id": "ECO-E2-L00946-1", "fonte_ref": "E2-L00946", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_FISC,
        "rotulo_item": "Item",
        "assertiva": "O resultado fiscal denominado acima da linha mensura a variação da dívida líquida total, interna ou externa.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O resultado fiscal denominado ") + vm("acima") + az(" da linha mensura a variação da dívida "
                      "líquida total, interna ou externa."),
        "poucas": ("Medir pela " + azb("variação da dívida") + " é o critério " + vd("abaixo da linha") + ". "
                   "Acima da linha, o resultado sai de receitas − despesas."),
        "destrinchando": [
            azb("Acima da linha") + ": fluxos de receita e despesa do período (no Brasil, apuração do Tesouro "
            "para o governo central, em regime de caixa). Mostra a composição do resultado.",
            azb("Abaixo da linha") + ": variação da dívida líquida (interna e externa) do setor público, "
            "descontados ajustes patrimoniais e cambiais. É o critério do " + rx("Banco Central") + " para as "
            "NFSP oficiais.",
            "Os dois deveriam convergir, porque todo déficit precisa ser financiado; a diferença residual é a "
            "discrepância estatística.",
            "Truque para lembrar: a “linha” separa o resultado (em cima) do financiamento (embaixo); embaixo "
            "está a dívida.",
            vm("Regra-âncora: abaixo da linha = dívida; acima da linha = receitas e despesas."),
        ],
        "dissecando": (cz("[inversão]") + " Troca simples de rótulo entre os dois critérios. A descrição (“variação "
                       "da dívida líquida total”) é perfeita — para o abaixo da linha. 🔥 Inversão recorrente em "
                       "itens de contabilidade fiscal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado fiscal denominado abaixo da linha mensura a variação da dívida líquida total, interna "
            "ou externa.”</i> → CERTO",
        ])],
        "reescrita": ("O resultado fiscal denominado " + hl("abaixo") + " da linha mensura a variação da dívida "
                      "líquida total, interna ou externa."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Acima da linha = receitas − despesas; abaixo da linha = variação da dívida líquida "
                            "total, interna ou externa.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0357-1 e ECO-E2-L00446-1 (acima × abaixo da linha)"],
    },
    # ------------------------------------------------------------------ E2-L00947
    {
        "id": "ECO-E2-L00947-1", "fonte_ref": "E2-L00947", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_FISC,
        "rotulo_item": "Item",
        "assertiva": ("Na hipótese de a inflação no Brasil ser nula em 2020, os conceitos ligados às necessidades de "
                      "financiamento do setor público sofrerão alterações. Nesse caso, o valor do resultado "
                      "primário será igual ao valor do resultado operacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na hipótese de a inflação no Brasil ser nula em 2020, os conceitos ligados às necessidades "
                      "de financiamento do setor público sofrerão alterações. Nesse caso, o valor do resultado ")
                   + vm("primário") + az(" será igual ao valor do resultado operacional."),
        "poucas": ("Inflação zero elimina a " + azb("correção monetária") + ", que separa " + vd("nominal")
                   + " de operacional. Primário e operacional seguem diferentes pelos " + azb("juros reais") + "."),
        "destrinchando": [
            "Escada: " + vd("nominal = primário + juros reais + correção monetária") + "; " + vd("operacional = "
            "primário + juros reais") + ". O degrau entre nominal e operacional é a inflação; o degrau entre "
            "operacional e primário são os juros reais.",
            "Com π = 0, a correção some e " + azb("nominal = operacional") + ". O primário só igualaria o "
            "operacional se os juros reais fossem zero — o que não depende da inflação.",
            "Exemplo: dívida 1.000, juro real 4%, inflação 0, déficit primário 10. Operacional = 10 + 40 = "
            + vd("50") + " = nominal; primário = " + vd("10") + ".",
            "Observação técnica: no " + rx("Brasil") + ", parte da dívida é corrigida também pelo câmbio "
            "(dívida externa e títulos cambiais); a rigor, nominal = operacional exige ausência de inflação "
            "<b>e</b> de correção cambial. A banca ignora esse detalhe no item.",
            vm("Regra-âncora: sem inflação, nominal = operacional; primário ≠ operacional enquanto houver juro real."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira frase é verdadeira e prepara o terreno; o erro está "
                       "no par escolhido: o conceito que coincide com o operacional sem inflação é o nominal. "
                       "Pista: inflação só mexe na correção monetária."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com inflação nula, o resultado nominal será igual ao resultado operacional.”</i> → CERTO",
            "<i>“Com juros reais nulos, o resultado primário será igual ao nominal, qualquer que seja a "
            "inflação.”</i> → ERRADO (a correção monetária ainda separa os dois)",
        ])],
        "reescrita": ("Na hipótese de a inflação no Brasil ser nula em 2020, os conceitos ligados às necessidades de "
                      "financiamento do setor público sofrerão alterações. Nesse caso, o valor do resultado "
                      + hl("nominal") + " será igual ao valor do resultado operacional."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Primário = nominal − juros nominais; operacional = primário + juros reais = nominal − "
                            "correção monetária; o que diferencia operacional de primário são os juros reais, "
                            "não a inflação.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00596-1 (primário × operacional)"],
    },
]
