"""Cards do lote de redação 06 — ECO, passada 02 (nota 18: Balanço de Pagamentos — estrutura e lançamentos)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "est": "🏗️ Estrutura do BP (BPM6)",
    "lanc": "✍️ Lançamentos",
    "cn": "🔗 BP e contas nacionais",
}

CMD_CN_BP_SM = ("Em relação às contas nacionais, ao balanço de pagamentos e ao sistema monetário, julgue o item "
                "a seguir.")

CMD_EST_BP = "Acerca da estrutura do balanço de pagamentos e das contas nacionais, julgue o item a seguir."

CMD_CN_BP_3 = "Acerca das contas nacionais e do balanço de pagamentos, julgue o item a seguir."

CMD_BPM6_I = ("Com base na sexta edição do Manual do Balanço de Pagamentos do Fundo Monetário Internacional (BPM6), "
              "julgue o item a seguir.")

CMD_AGREG_3 = ("Acerca de agregados macroeconômicos, das contas nacionais e de balanço de pagamentos, julgue o item "
               "a seguir.")

CMD_Q1 = "Julgue o item a seguir, acerca dos fluxos internacionais de bens e de capital em uma economia aberta."

CMD_Q2 = ("No que diz respeito aos conceitos subjacentes a uma economia aberta e ao balanço de pagamentos — registro "
          "das transações de um país com o resto do mundo —, julgue o item a seguir.")

CMD_Q3 = "No que diz respeito às contas do balanço de pagamentos, julgue o item a seguir."

CMD_Q4 = ("Com referência aos dados do balanço de pagamentos apresentados na tabela, julgue o item a seguir.")

TAB_Q4 = {
    "titulo": "Balanço de pagamentos (em US$ bilhões)",
    "cabecalho": ["Operação", "Sentido", "US$ bilhões"],
    "linhas": [["Exportações", "receita", "100"],
               ["Importações", "despesa", "80"],
               ["Empréstimos externos", "ingresso", "20"],
               ["Donativos", "recebidos", "5"],
               ["Fretes", "pagos", "20"],
               ["Amortizações", "pagas", "10"]],
}

CMD_TEIX = ("Com base na sexta edição do Manual do Balanço de Pagamentos do Fundo Monetário Internacional (BPM6), "
            "julgue o item a seguir.")

ESTRUTURA_BPM6 = (
    "Estrutura do BP no " + azb("BPM6") + " (adotado pelo " + rx("Banco Central do Brasil") + " em "
    + vd("2015") + "): " + azb("Transações correntes") + " (bens, serviços, renda primária, renda secundária) + "
    + azb("Conta capital") + " = " + azb("Conta financeira") + " (investimento direto, carteira, derivativos, "
    "outros investimentos, ativos de reserva), com " + azb("Erros e omissões") + " fechando a diferença.")

CARDS = [
    # ------------------------------------------------------------------ E2-L00702
    {
        "id": "ECO-E2-L00702-1", "fonte_ref": "E2-L00702", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": ("A respeito dos instrumentos de política comercial e dos regimes cambiais, julgue o item a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Um déficit em Transações Correntes indica que o país está enviando poupança para o resto do "
                      "mundo, ou seja, a Renda Nacional Bruta Disponível é superior à Absorção Interna."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um déficit em Transações Correntes indica que o país está ") + vm("enviando poupança para o")
                    + az(" resto do mundo, ou seja, a Renda Nacional Bruta Disponível é ") + vm("superior")
                    + az(" à Absorção Interna.")),
        "poucas": ("Déficit em transações correntes = o país " + azb("absorve mais do que a renda") + " que "
                   "dispõe e cobre a diferença com " + azb("poupança externa") + ": ele <b>recebe</b> poupança do "
                   "resto do mundo, não envia."),
        "destrinchando": [
            "Identidade de partida: " + vd("TC = RNBD − A") + ", em que A = C + I + G é a " + azb("absorção "
            "interna") + " e RNBD é a renda nacional bruta disponível (PIB + renda primária líquida + renda "
            "secundária líquida).",
            "Pela ótica da poupança: " + vd("TC = S<sub>dom</sub> − I") + ". Se TC < 0, o investimento supera a "
            "poupança doméstica, e o hiato é financiado por " + azb("poupança externa") + " (S<sub>ext</sub> = −TC "
            "> 0), que entra pela conta financeira (investimento direto, carteira, empréstimos).",
            "Logo, com déficit: A > RNBD, S<sub>ext</sub> > 0 e o país acumula passivos externos líquidos. Com "
            "superávit, o inverso: A < RNBD, o país empresta ao resto do mundo (S<sub>ext</sub> < 0) — é o caso "
            "de exportadores líquidos de capital como China e Alemanha.",
            "O " + rx("Brasil") + " tem histórico de déficits em transações correntes, financiados em boa parte "
            "por investimento direto no país; déficit externo não é, por si, sinal de crise — importa a "
            "qualidade do financiamento e a sustentabilidade.",
            vm("Regra-âncora: déficit em TC ⇔ A > RNBD ⇔ I > S doméstica ⇔ poupança externa positiva."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sentido do fluxo de poupança e, coerentemente, a "
                       "desigualdade entre renda e absorção: tudo “fecha” por dentro, mas descreve um "
                       "<b>superávit</b>. Teste rápido: déficit = gastar mais do que ganha → alguém de fora "
                       "financia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um superávit em transações correntes indica que o país está enviando poupança para o resto do "
            "mundo.”</i> → CERTO",
            "<i>“Um déficit em transações correntes implica que a poupança externa é negativa.”</i> → ERRADO "
            "(sinal trocado: é positiva)",
        ])],
        "reescrita": ("Um déficit em Transações Correntes indica que o país está " + hl("recebendo poupança do")
                      + " resto do mundo, ou seja, a Renda Nacional Bruta Disponível é " + hl("inferior")
                      + " à Absorção Interna."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Déficit em TC significa receber poupança externa para financiar o excesso de "
                            "investimento sobre a poupança doméstica; a absorção supera a RNBD.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00720
    {
        "id": "ECO-E2-L00720-1", "fonte_ref": "E2-L00720", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "No que diz respeito aos principais agregados macroeconômicos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considerando a versão BPM6 da estrutura do Balanço de Pagamentos (BP), a aquisição de marcas e "
                      "patentes está incluída na Conta Financeira."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando a versão BPM6 da estrutura do Balanço de Pagamentos (BP), a aquisição de "
                       "marcas e patentes está incluída ") + vm("na Conta Financeira") + az(".")),
        "poucas": ("Marcas são " + azb("ativos não financeiros não produzidos") + ": sua compra e venda vai para "
                   "a " + azb("Conta Capital") + ". Patentes resultantes de P&D vão para " + azb("Serviços")
                   + ". Nenhuma das duas é ativo financeiro."),
        "destrinchando": [
            "A " + azb("Conta Financeira") + " registra só transações com <b>ativos e passivos financeiros</b>: "
            "investimento direto, investimento em carteira, derivativos, outros investimentos e ativos de "
            "reserva. Marca ou patente não é direito financeiro sobre ninguém.",
            "A " + azb("Conta Capital") + " registra (i) aquisição e alienação de " + azb("ativos não "
            "financeiros não produzidos") + " — recursos naturais, contratos, arrendamentos e licenças, e "
            "ativos de comercialização (marcas, logotipos, nomes de domínio) vendidos separadamente da empresa "
            "— e (ii) " + azb("transferências de capital") + " (perdão de dívida, doações para investimento).",
            "Exceção de detalhe: a venda definitiva de direitos que resultam de " + azb("pesquisa e "
            "desenvolvimento") + " (patentes, por exemplo) é registrada em " + azb("Serviços") + " (outros "
            "serviços empresariais — P&D). Já o pagamento pelo <b>uso</b> de marcas e patentes (royalties, "
            "licenças) é serviço: “uso de propriedade intelectual”.",
            vm("Regra-âncora: ativo financeiro → Conta Financeira; ativo não financeiro não produzido → Conta "
               "Capital; uso de propriedade intelectual → Serviços."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca a Conta Capital pela Conta Financeira, vizinhas desde "
                       "que o BPM5 desmembrou a antiga “conta capital e financeira”. A pista é a natureza do "
                       "ativo: marca não é passivo de ninguém, logo não pode estar na financeira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No BPM6, a compra e venda de marcas registradas separadamente da empresa é lançada na conta "
            "capital.”</i> → CERTO",
            "<i>“O pagamento de royalties pelo uso de patentes é registrado na conta capital.”</i> → ERRADO "
            "(troca de conceito: é serviço — uso de propriedade intelectual)",
        ])],
        "reescrita": ("Considerando a versão BPM6 da estrutura do Balanço de Pagamentos (BP), a aquisição de marcas e "
                      "patentes está incluída " + hl("na Conta Capital (marcas) ou na conta de Serviços (patentes "
                                                     "resultantes de P&D)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "No BPM6, compra e venda de direitos de concessões e marcas registradas vão para a "
                            "conta capital; se resultarem de P&D, para serviços (P&D). A conta financeira registra "
                            "ativos e passivos financeiros.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: comentário de E2-L00775 (mesma assertiva) fundido"],
    },
    # ------------------------------------------------------------------ E2-L00755
    {
        "id": "ECO-E2-L00755-1", "fonte_ref": "E2-L00755", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CN_BP_SM,
        "rotulo_item": "Item",
        "assertiva": ("Os serviços da dívida externa, incluindo despesas financeiras e juros, são registrados na "
                      "conta capital e financeira."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os serviços da dívida externa, incluindo despesas financeiras e juros, são registrados ")
                    + vm("na conta capital e financeira") + az(".")),
        "poucas": ("Juros são " + azb("rendimento de investimento") + ": vão para a " + azb("renda primária")
                   + ", dentro das transações correntes. Só a amortização do principal é operação financeira."),
        "destrinchando": [
            "Distinga as duas partes do " + azb("serviço da dívida") + ": " + vd("juros") + " (remuneração do "
            "capital) e " + vd("amortizações") + " (devolução do principal). O BP separa as duas.",
            "Os juros pagos ao exterior são débito em " + azb("renda primária") + " (rendas de investimento — "
            "juros, lucros e dividendos), subconta das transações correntes. Por isso pioram o saldo em "
            "transações correntes.",
            "A amortização reduz um passivo externo: é lançada na " + azb("conta financeira") + " (outros "
            "investimentos ou carteira, conforme o instrumento). Não afeta transações correntes.",
            "“Conta capital e financeira” é rótulo do BPM5; no " + azb("BPM6") + ", as duas são contas "
            "distintas, e nenhuma delas recebe juros.",
            ESTRUTURA_BPM6,
        ],
        "dissecando": (cz("[troca de conceito]") + " O item aproveita a palavra “dívida” para empurrar tudo "
                       "para a conta financeira. O gatilho é “juros”: rendimento é sempre renda primária, "
                       "seja de dívida, seja de ação (dividendos)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As amortizações da dívida externa são registradas na conta financeira.”</i> → CERTO",
            "<i>“O pagamento de juros da dívida externa reduz o saldo da balança de serviços.”</i> → ERRADO "
            "(troca de conta: é renda primária)",
        ])],
        "reescrita": ("Os serviços da dívida externa, incluindo despesas financeiras e juros, são registrados "
                      + hl("na conta de renda primária, das transações correntes") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Juros da dívida externa vão para a renda primária (transações correntes); "
                            "amortizações, para a conta financeira.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 110", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (esquema do plano de contas BPM6 no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00756
    {
        "id": "ECO-E2-L00756-1", "fonte_ref": "E2-L00756", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_CN_BP_SM,
        "rotulo_item": "Item",
        "assertiva": ("As transferências de capital relacionadas com patrimônio de migrantes impactam a conta de "
                      "capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As transferências de capital relacionadas com patrimônio de migrantes ")
                    + vm("impactam a conta de capital") + az(".")),
        "poucas": ("O " + azb("BPM6") + " retirou o patrimônio de migrantes da conta capital e do próprio BP: "
                   "não há transação entre residente e não residente — muda só a residência do dono."),
        "destrinchando": [
            "O BP registra " + azb("transações entre residentes e não residentes") + ". Quando alguém migra com "
            "seus bens, ninguém compra nem vende nada: o mesmo dono passa a ser residente de outro país, e os "
            "ativos o acompanham.",
            "No " + azb("BPM5") + ", essas “transferências de migrantes” eram lançadas na conta capital como "
            "transferências unilaterais de capital. O " + azb("BPM6") + " (FMI, 2009) as excluiu do BP: a "
            "mudança aparece como " + azb("outra variação de volume") + " na posição de investimento "
            "internacional (estoques), não como fluxo.",
            "O que continua na " + azb("conta capital") + ": transferências de capital (perdão de dívida, "
            "doações para investimento) e compra e venda de ativos não financeiros não produzidos (terras para "
            "embaixadas, licenças, marcas).",
            "Não confundir com as " + azb("remessas de trabalhadores") + " (dinheiro enviado periodicamente à "
            "família): essas são transferências correntes, em " + azb("renda secundária") + ".",
        ],
        "dissecando": (cz("[anacronismo · troca de conceito]") + " O item descreve o tratamento do BPM5, "
                       "superado pelo BPM6. 🔥 Itens sobre “o que mudou do BPM5 para o BPM6” são recorrentes: "
                       "migrantes, operações intercompanhia, reservas na conta financeira, nomes das contas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No BPM5, as transferências de patrimônio de migrantes eram registradas na conta capital.”</i> "
            "→ CERTO",
            "<i>“No BPM6, as remessas de imigrantes às suas famílias deixaram de ser registradas no BP.”</i> → "
            "ERRADO (confunde remessa, que é renda secundária, com patrimônio de migrante)",
        ])],
        "reescrita": ("As transferências de capital relacionadas com patrimônio de migrantes "
                      + hl("deixaram, no BPM6, de ser registradas na conta de capital e no próprio BP") + "."),
        "tipo_erro": ["ANACRONISMO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "O BPM6 excluiu as transferências de patrimônio de migrantes da conta capital e do BP, "
                            "por não serem transações entre residente e não residente; no BPM5 iam para a conta "
                            "capital.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00935
    {
        "id": "ECO-E2-L00935-1", "fonte_ref": "E2-L00935", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": ("A respeito das contas nacionais, do balanço de pagamentos e da teoria monetária, julgue o item "
                    "a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O FMI e outros organismos internacionais revisaram a metodologia para criptoativos nas "
                      "estatísticas de balanço de pagamentos, conforme a 7ª edição do manual de balanço de "
                      "pagamentos, BPM7. Criptoativos sem emissor, antes tratados como bens e registrados na "
                      "balança comercial, agora são considerados ativos não financeiros não produzidos e "
                      "registrados na conta de capital. A adoção desta mudança deve alterar os resultados da "
                      "conta corrente e da conta capital, mas não os resultados da conta financeira."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O FMI e outros organismos internacionais revisaram a metodologia para criptoativos nas "
                      "estatísticas de balanço de pagamentos, conforme a 7ª edição do manual de balanço de "
                      "pagamentos, BPM7. Criptoativos sem emissor, antes tratados como bens e registrados na "
                      "balança comercial, agora são considerados <u>ativos não financeiros não produzidos</u> e "
                      "registrados na <u>conta de capital</u>. A adoção desta mudança deve alterar os resultados "
                      "da conta corrente e da conta capital, <u>mas não os resultados da conta financeira</u>."),
        "poucas": ("A compra de criptoativo sai das " + azb("importações") + " (transações correntes) e vai para "
                   "a " + azb("conta capital") + ": as duas contas mudam em sentidos opostos. A contrapartida "
                   "financeira (o pagamento) continua igual, então a " + vd("conta financeira não muda") + "."),
        "destrinchando": [
            "Criptoativos <b>sem emissor</b> (como o bitcoin) não são passivo de ninguém, logo não são ativos "
            "financeiros. Também não são produzidos como um bem comum. Daí a nova classificação: " + azb("ativos "
            "não financeiros não produzidos") + ", a mesma categoria de terras, licenças e marcas — conta "
            "capital.",
            "Partidas dobradas: na importação de cripto por um residente, débito em bens (antes) ou em conta "
            "capital (agora); o crédito é sempre a saída de recursos na " + azb("conta financeira") + " (redução "
            "de depósitos no exterior, por exemplo). Só o débito mudou de lugar.",
            "Efeito nos saldos: o déficit da balança comercial diminui (menos importações), o saldo da conta "
            "capital piora no mesmo valor e " + vd("TC + K fica igual") + " — logo, pela identidade "
            + vd("CF = TC + K + EO") + ", a conta financeira não se altera.",
            "Criptoativos <b>com emissor</b> (stablecoins lastreadas, por exemplo) têm contraparte que responde "
            "por eles e tendem a ser tratados como instrumentos financeiros.",
            "⏳ (out/2026) O " + rx("Banco Central do Brasil") + " aplicou a mudança numa revisão extraordinária "
            "divulgada em " + vd("25 de julho de 2024") + ", antecipando o tratamento previsto no BPM7.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item longo e tecnicamente correto, construído sobre "
                       "a nota do BCB. O risco está na última frase: quem esquece as partidas dobradas acha que "
                       "toda mudança de classificação mexe em todas as contas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A reclassificação dos criptoativos reduz o déficit em transações correntes e, na mesma "
            "medida, o saldo da conta financeira.”</i> → ERRADO (a conta financeira não se altera)",
            "<i>“Criptoativos sem emissor passaram a ser registrados como investimento em carteira.”</i> → "
            "ERRADO (troca de conceito: não são ativos financeiros)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": ["mas não"], "dificuldade": 3,
        "comentario_fonte": "Transfere-se o registro da balança comercial para a conta capital; a contrapartida "
                            "continua na conta financeira, que não se altera (CF = TC + K + EO). Cita nota do BCB "
                            "sobre a revisão de 25/07/2024.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00954
    {
        "id": "ECO-E2-L00954-1", "fonte_ref": "E2-L00954", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_EST_BP,
        "rotulo_item": "Item",
        "assertiva": ("O balanço de pagamentos é o registro estatístico de todas as transações – fluxo de bens e "
                      "direitos de valor econômico – entre os residentes de uma economia e o restante do mundo, "
                      "ocorridos em determinado período. A componente desse registro que representa o somatório "
                      "dos valores líquidos dos investimentos diretos, investimentos em carteira, derivativos e "
                      "outros investimentos é denominada conta de capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O balanço de pagamentos é o registro estatístico de todas as transações – fluxo de bens e "
                       "direitos de valor econômico – entre os residentes de uma economia e o restante do mundo, "
                       "ocorridos em determinado período. A componente desse registro que representa o "
                       "somatório dos valores líquidos dos investimentos diretos, investimentos em carteira, "
                       "derivativos e outros investimentos é denominada ") + vm("conta de capital") + az(".")),
        "poucas": ("Investimento direto, carteira, derivativos e outros investimentos são as rubricas da "
                   + azb("conta financeira") + ". A " + azb("conta capital") + " é pequena e trata de ativos não "
                   "financeiros não produzidos e transferências de capital."),
        "destrinchando": [
            "A 1ª frase é a definição de manual e está correta: o BP registra " + azb("fluxos") + " (não "
            "estoques) entre " + azb("residentes e não residentes") + " num período. O critério é a residência, "
            "não a nacionalidade.",
            azb("Conta financeira") + " (BPM6): " + vd("investimento direto") + " (IDP e IDE/IBD), "
            + vd("investimento em carteira") + " (ações e títulos), " + vd("derivativos") + ", "
            + vd("outros investimentos") + " (empréstimos, créditos comerciais, depósitos) e " + vd("ativos de "
            "reserva") + ". O saldo é ativos líquidos adquiridos − passivos líquidos incorridos.",
            azb("Conta capital") + ": (a) compra e venda de ativos não financeiros não produzidos — recursos "
            "naturais (terras, direitos de pesca, espectro eletromagnético), contratos, arrendamentos e "
            "licenças, ativos de comercialização (marcas, logotipos, nomes de domínio vendidos separadamente); "
            "(b) transferências de capital, como o " + azb("perdão de dívida") + " e doações para investimento.",
            "A confusão vem do BPM5, em que se falava de “conta capital e financeira” como um bloco, e de "
            "manuais anglo-saxões antigos, que chamavam de <i>capital account</i> o que hoje é a conta "
            "financeira.",
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " Uma frase inteira de definição correta "
                       "serve de isca; o erro está só no nome da conta, na última palavra. Em itens longos de "
                       "BP, leia o rótulo final antes de se convencer pela introdução."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é denominada conta financeira, que no BPM6 inclui também os ativos de reserva.”</i> → CERTO",
            "<i>“O balanço de pagamentos registra os estoques de ativos e passivos externos de uma economia.”</i>"
            " → ERRADO (troca de conceito: estoques estão na posição de investimento internacional)",
        ])],
        "reescrita": ("O balanço de pagamentos é o registro estatístico de todas as transações – fluxo de bens e "
                      "direitos de valor econômico – entre os residentes de uma economia e o restante do mundo, "
                      "ocorridos em determinado período. A componente desse registro que representa o somatório "
                      "dos valores líquidos dos investimentos diretos, investimentos em carteira, derivativos e "
                      "outros investimentos é denominada " + hl("conta financeira") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "É a conta financeira. A conta capital registra ativos não financeiros não produzidos "
                            "(recursos naturais, contratos e licenças, marcas) e transferências de capital, como o "
                            "perdão de dívida.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00955
    {
        "id": "ECO-E2-L00955-1", "fonte_ref": "E2-L00955", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_EST_BP,
        "rotulo_item": "Item",
        "assertiva": ("Considere a 6ª edição do Manual de Balanço de Pagamentos do FMI (BPM6). Suponha que uma "
                      "subsidiária offshore tenha captado recursos e emprestado esses recursos para a matriz no "
                      "Brasil. O ingresso desses recursos no Brasil é registrado no Balanço de Pagamentos como "
                      "redução do Investimento Brasileiro Direto (IBD) no exterior, na conta de operações "
                      "intercompanhia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considere a 6ª edição do Manual de Balanço de Pagamentos do FMI (BPM6). Suponha que uma "
                       "subsidiária offshore tenha captado recursos e emprestado esses recursos para a matriz no "
                       "Brasil. O ingresso desses recursos no Brasil é registrado no Balanço de Pagamentos como ")
                    + vm("redução do Investimento Brasileiro Direto (IBD) no exterior")
                    + az(", na conta de operações intercompanhia.")),
        "poucas": ("No BPM6 vale o " + azb("critério de ativos e passivos") + ": a matriz residente passa a "
                   "<b>dever</b> a um não residente — é passivo, registrado como " + vd("Investimento Direto no "
                   "País (IDP)") + ", operações intercompanhia. Redução de IBD era o tratamento do BPM5."),
        "destrinchando": [
            "No " + azb("BPM5") + " vigorava o " + azb("princípio direcional") + ": o que importava era a "
            "direção do investimento original (matriz brasileira → filial no exterior). Um empréstimo da filial "
            "à matriz era tratado como <b>desinvestimento</b> — redução do IBD (antigo IBD, hoje IDE).",
            "No " + azb("BPM6") + ", as operações intercompanhia seguem o " + azb("critério de ativos e "
            "passivos") + ": olha-se só a residência de credor e devedor. Devedor residente (a matriz no "
            + rx("Brasil") + ") e credor não residente (a subsidiária offshore) → " + vd("passivo") + " → "
            + vd("IDP") + ".",
            "Simétrico: empréstimos de matrizes no Brasil a filiais no exterior, ou de filiais no Brasil a "
            "matrizes no exterior, viram " + vd("ativo") + " → investimento direto no exterior.",
            "Efeito prático: o critério novo eleva <b>ao mesmo tempo</b> os ativos e os passivos de "
            "investimento direto do país. A captação via subsidiárias offshore (comum entre grandes empresas "
            "brasileiras) passou a inflar o IDP, o que exige cuidado ao ler o IDP como “capital produtivo "
            "estrangeiro”.",
        ],
        "dissecando": (cz("[anacronismo · troca de conceito]") + " O item descreve com precisão o lançamento do "
                       "BPM5 e o atribui ao BPM6, que ele próprio invoca no início. A pista é justamente “Considere "
                       "o BPM6” + “matriz” + “subsidiária”: a banca quer saber se você conhece a troca de "
                       "critério."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo BPM5, o empréstimo da subsidiária no exterior à matriz no Brasil reduzia o investimento "
            "brasileiro direto.”</i> → CERTO",
            "<i>“Pelo BPM6, o empréstimo da matriz no Brasil à filial no exterior é registrado como IDP.”</i> → "
            "ERRADO (é ativo do residente: investimento direto no exterior)",
        ])],
        "reescrita": ("Considere a 6ª edição do Manual de Balanço de Pagamentos do FMI (BPM6). Suponha que uma "
                      "subsidiária offshore tenha captado recursos e emprestado esses recursos para a matriz no "
                      "Brasil. O ingresso desses recursos no Brasil é registrado no Balanço de Pagamentos como "
                      + hl("aumento do Investimento Direto no País (IDP), um passivo") + ", na conta de operações "
                      "intercompanhia."),
        "tipo_erro": ["ANACRONISMO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": "No BPM6, crédito da filial no exterior à matriz no Brasil passa a ser IDP (passivo), "
                            "pelas residências de credor e devedor; no BPM5 era redução do IBD.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 156", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (texto do comentário no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01062
    {
        "id": "ECO-E2-L01062-1", "fonte_ref": "E2-L01062", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN_BP_3,
        "rotulo_item": "Item",
        "assertiva": ("Na sexta edição do Manual do Balanço de Pagamentos do Fundo Monetário Internacional (BPM6), "
                      "os erros e Omissões são obtidos a partir do saldo da Conta Financeira deduzido dos saldos "
                      "de Transações Correntes e da Conta Capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na sexta edição do Manual do Balanço de Pagamentos do Fundo Monetário Internacional (BPM6), "
                      "os erros e Omissões são obtidos a partir do saldo da <u>Conta Financeira deduzido dos "
                      "saldos de Transações Correntes e da Conta Capital</u>."),
        "poucas": ("No BPM6, " + vd("TC + K = CF") + " em tese; na prática, as fontes diferem, e a discrepância "
                   "é " + vd("EO = CF − TC − K") + "."),
        "destrinchando": [
            "Identidade do " + azb("BPM6") + ": o que o país empresta (ou toma) ao exterior pelas contas "
            "correntes e de capital tem de aparecer como aquisição líquida de ativos menos incidência líquida "
            "de passivos. Em símbolos: " + vd("TC + K + EO = CF") + ".",
            "Leitura dos sinais: TC + K > 0 é " + azb("capacidade de financiamento") + " (o país empresta ao "
            "resto do mundo) e deve corresponder a CF > 0 (acumula ativos líquidos). TC + K < 0 é "
            + azb("necessidade de financiamento") + ".",
            azb("Erros e omissões") + " não são transações: são o resíduo que fecha a identidade, porque "
            "transações correntes e conta financeira são medidas por fontes diferentes (câmbio, registros "
            "aduaneiros, declarações de capitais), com defasagens e lacunas.",
            "Mudança em relação ao " + azb("BPM5") + ": lá, o “resultado do BP” = TC + conta capital e "
            "financeira + EO, e os ativos de reserva ficavam fora, com sinal invertido. No BPM6, as reservas "
            "estão <b>dentro</b> da conta financeira, e o antigo “resultado do BP” deixou de existir como "
            "linha.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a fórmula do BCB. A dificuldade é a ordem da "
                       "subtração: quem decorou o BPM5 (“EO completa o resultado”) tende a inverter os sinais e "
                       "marcar ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No BPM6, os erros e omissões correspondem à soma dos saldos de transações correntes e da conta "
            "capital, deduzida da conta financeira.”</i> → ERRADO (sinal invertido: EO = CF − TC − K)",
            "<i>“No BPM6, os ativos de reserva integram a conta financeira.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Saldo da conta financeira − saldo de transações correntes − saldo da conta capital = "
                            "erros e omissões.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01063
    {
        "id": "ECO-E2-L01063-1", "fonte_ref": "E2-L01063", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_CN_BP_3,
        "rotulo_item": "Item",
        "assertiva": ("O BPM6 passou a adotar o critério de ativos e passivos, no qual não é mais preciso "
                      "identificar a matriz."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O BPM6 passou a adotar o <u>critério de ativos e passivos</u>, no qual <u>não é mais "
                      "preciso identificar a matriz</u>."),
        "poucas": ("Nas operações intercompanhia, o BPM6 trocou o " + azb("princípio direcional") + " pelo "
                   + azb("critério de ativos e passivos") + ": basta saber a residência do credor e a do devedor."),
        "destrinchando": [
            azb("Princípio direcional") + " (BPM5): para classificar uma dívida intercompanhia, era "
            "indispensável saber quem é a matriz (a investidora). Crédito da filial à matriz era "
            "desinvestimento, não novo investimento.",
            azb("Critério de ativos e passivos") + " (BPM6): se o credor é residente, é " + vd("ativo") + " "
            "(investimento direto no exterior); se o devedor é residente, é " + vd("passivo") + " (investimento "
            "direto no país). Ser matriz, subsidiária ou empresa-irmã deixa de ser determinante.",
            "O BPM6 também explicitou as operações entre " + azb("empresas-irmãs") + " (sob o mesmo controlador, "
            "sem participação uma no capital da outra), incluídas como investimento direto — dívida "
            "intercompanhia.",
            "O critério vale só para a modalidade " + azb("dívida intercompanhia") + "; a participação no "
            "capital continua sendo classificada pela relação de controle. O FMI mantém o princípio direcional "
            "como apresentação complementar.",
            "Foi a mudança de maior impacto da adoção do BPM6 pelo " + rx("BCB") + " (" + vd("2015") + "): "
            "aumentou simultaneamente IDP e investimento direto no exterior.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Frase curta e correta, tirada da nota metodológica do "
                       "BCB. O “não é mais preciso” assusta quem associa investimento direto a controle — mas o "
                       "item fala do critério de classificação, que é por residência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No BPM6, a classificação das operações intercompanhia depende da identificação da empresa "
            "investidora.”</i> → ERRADO (anacronismo: era o princípio direcional do BPM5)",
            "<i>“No BPM6, empréstimos entre empresas-irmãs residentes em países distintos integram o "
            "investimento direto.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["não é mais"], "dificuldade": 2,
        "comentario_fonte": "O BPM6 substituiu o princípio direcional (identificar a matriz) pelo critério de "
                            "ativos e passivos, pela residência de credor e devedor, na dívida intercompanhia.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01286
    {
        "id": "ECO-E2-L01286-1", "fonte_ref": "E2-L01286", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_BPM6_I,
        "rotulo_item": "Item",
        "assertiva": ("As variações nas reservas internacionais são contabilizadas na Conta Financeira como Ativos "
                      "de Reserva."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As variações nas reservas internacionais são contabilizadas na <u>Conta Financeira</u> como "
                      "<u>Ativos de Reserva</u>."),
        "poucas": ("No " + azb("BPM6") + ", as reservas são mais um tipo de ativo financeiro: a rubrica "
                   + azb("ativos de reserva") + " fica <b>dentro</b> da conta financeira. É como se o antigo "
                   "“resultado do BP” tivesse sido incorporado a ela."),
        "destrinchando": [
            azb("Ativos de reserva") + " são ativos externos à disposição e sob controle da autoridade monetária "
            "para financiar desequilíbrios, intervir no câmbio e dar confiança: " + vd("ouro monetário") + ", "
            + vd("DES") + " (direitos especiais de saque), " + vd("posição de reserva no FMI") + " e outros "
            "ativos em moeda estrangeira.",
            "No " + azb("BPM5") + ", a estrutura terminava num “resultado do balanço” (TC + conta capital e "
            "financeira + EO), compensado por “haveres da autoridade monetária”, fora da conta financeira. No "
            "BPM6, a conta financeira passa a ter cinco grupos: investimento direto, carteira, derivativos, "
            "outros investimentos e " + vd("ativos de reserva") + ".",
            "Sinal no BPM6: a conta financeira mostra aquisição líquida de ativos com sinal <b>positivo</b>. "
            "Acúmulo de reservas aumenta o saldo da CF (no BPM5, a convenção de crédito e débito o mostrava "
            "com sinal negativo).",
            "O " + rx("Banco Central do Brasil") + " publica o BP pelo BPM6 desde " + vd("2015") + ". ⏳ "
            "(out/2026) As reservas brasileiras estão na casa de centenas de bilhões de dólares; consulte as "
            "Estatísticas do Setor Externo do BCB para o valor corrente.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a regra do manual. A armadilha é a memória do BPM5, "
                       "em que reserva era o “resultado” do BP, fora da conta financeira: quem estudou pela "
                       "estrutura antiga marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No BPM6, as variações das reservas internacionais são registradas fora da conta financeira, "
            "como resultado do balanço de pagamentos.”</i> → ERRADO (anacronismo: estrutura do BPM5)",
            "<i>“Ouro monetário e direitos especiais de saque integram os ativos de reserva.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Uma das principais mudanças do BPM6, adotado pelo BCB: o antigo saldo do BP foi "
                            "incorporado pela rubrica “ativos de reserva”, componente da conta financeira.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 224", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (estrutura das transações correntes no 📖)"},
                          {"ref": "IMAGEM 225", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (estrutura das contas capital e financeira no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01663-1 (mesma assertiva, outra fonte)"],
    },
    # ------------------------------------------------------------------ E2-L01287
    {
        "id": "ECO-E2-L01287-1", "fonte_ref": "E2-L01287", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_BPM6_I,
        "rotulo_item": "Item",
        "assertiva": ("Os salários recebidos por trabalhadores residentes, quando trabalham para uma empresa não "
                      "residente no país, são contabilizados na Conta de Serviços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os salários recebidos por trabalhadores residentes, quando trabalham para uma empresa não "
                       "residente no país, são contabilizados na ") + vm("Conta de Serviços") + az(".")),
        "poucas": ("Salário pago por não residente a residente é " + azb("remuneração de empregados") + ", "
                   "rubrica da " + azb("renda primária") + " — remuneração de fator de produção, não venda de "
                   "serviço."),
        "destrinchando": [
            "A " + azb("renda primária") + " registra a remuneração dos fatores de produção cedidos entre "
            "residentes e não residentes: " + vd("remuneração de empregados") + " (trabalho) e " + vd("renda de "
            "investimentos") + " (capital: juros, lucros, dividendos, lucros reinvestidos).",
            "Exemplos de remuneração de empregados: brasileiro residente contratado por uma embaixada estrangeira "
            "em Brasília; trabalhador sazonal ou de fronteira que trabalha alguns meses para empregador no "
            "exterior sem mudar de residência.",
            "Diferença para " + azb("serviços") + ": quando o residente é <b>autônomo ou empresa</b> e vende "
            "um serviço (consultoria, frete, engenharia) a um não residente, há exportação de serviço. A "
            "linha divisória é a relação de emprego.",
            "Diferença para " + azb("renda secundária") + ": se o trabalhador migra (vira residente do outro "
            "país) e manda dinheiro para casa, o salário deixa de ser transação externa e a remessa é "
            "transferência pessoal (renda secundária).",
            vm("Regra-âncora: fator de produção (trabalho ou capital) remunerado → renda primária; "
               "transferência sem contrapartida → renda secundária."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca renda primária por serviços, a confusão mais comum "
                       "da balança de transações correntes: o trabalhador “presta um serviço” no sentido comum, "
                       "mas contabilmente é fator remunerado. 🔥 Salários, juros e lucros caem sempre em renda "
                       "primária."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os honorários de um consultor autônomo residente pagos por uma empresa estrangeira são "
            "registrados na conta de serviços.”</i> → CERTO",
            "<i>“Os salários de trabalhadores residentes pagos por empresa não residente são registrados na "
            "renda secundária.”</i> → ERRADO (troca de conceito: é renda primária)",
        ])],
        "reescrita": ("Os salários recebidos por trabalhadores residentes, quando trabalham para uma empresa não "
                      "residente no país, são contabilizados na " + hl("Conta de Renda Primária") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "São incluídos na conta de renda primária.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01288
    {
        "id": "ECO-E2-L01288-1", "fonte_ref": "E2-L01288", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_BPM6_I,
        "rotulo_item": "Item",
        "assertiva": ("As remessas de dinheiro de imigrantes no exterior para seus países de origem são "
                      "contabilizadas na Conta de Renda Secundária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As remessas de dinheiro de imigrantes no exterior para seus países de origem são "
                      "contabilizadas na <u>Conta de Renda Secundária</u>."),
        "poucas": ("Remessa de imigrante é " + azb("transferência corrente sem contrapartida") + ": vai para a "
                   + azb("renda secundária") + ", nome que o BPM6 deu às antigas “transferências unilaterais "
                   "correntes”."),
        "destrinchando": [
            "A " + azb("renda secundária") + " registra transferências <b>correntes</b>: valores que mudam de "
            "mãos sem contrapartida e sem formar patrimônio do recebedor — remessas pessoais de trabalhadores, "
            "doações para consumo, ajuda humanitária, contribuições a organismos internacionais, certos "
            "impostos e benefícios sociais.",
            "O imigrante já é " + azb("residente") + " do país onde vive: a remessa à família no país de origem "
            "é transação entre residente e não residente. No país de origem, entra como crédito em renda "
            "secundária; no país que envia, como débito.",
            "Não confundir com " + azb("renda primária") + " (salário de quem trabalha no exterior <b>sem</b> "
            "mudar de residência) nem com " + azb("conta capital") + " (transferências de capital, como "
            "perdão de dívida e doação para investimento).",
            "Nomes: BPM5 → “transferências unilaterais correntes”; BPM6 → “renda secundária”. O BPM5 também "
            "chamava a renda primária só de “rendas” (ou “serviços de fatores”, em manuais brasileiros).",
            "Em países como México, Filipinas e El Salvador, as remessas são fonte de divisas de primeira "
            "grandeza; no " + rx("Brasil") + ", o saldo de renda secundária é pequeno perto do déficit de renda "
            "primária.",
        ],
        "dissecando": (cz("[literalidade]") + " Correto e direto. O risco é a nomenclatura: “secundária” parece "
                       "algo de menor importância, e o candidato desconfia, ou confunde com a renda primária, "
                       "que remunera fatores."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As remessas de imigrantes para seus países de origem são contabilizadas na conta capital.”</i>"
            " → ERRADO (troca de conceito: são transferências correntes)",
            "<i>“No BPM5, as remessas de imigrantes eram registradas em transferências unilaterais "
            "correntes.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Vão para a renda secundária, que no BPM5 se chamava transferências unilaterais "
                            "correntes.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 226", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (comparação BPM5 × BPM6 de 2014; transcrição incompleta)"},
                          {"ref": "IMAGEM 227", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (tabela de transações correntes de 2021; transcrição incompleta)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01664-1 (mesmo tema; lá a conta trocada é a conta capital)"],
    },
    # ------------------------------------------------------------------ E2-L01289
    {
        "id": "ECO-E2-L01289-1", "fonte_ref": "E2-L01289", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_BPM6_I,
        "rotulo_item": "Item",
        "assertiva": ("O saldo da Conta Financeira é calculado pela diferença entre a aquisição líquida de Ativos "
                      "Financeiros e a incidência líquida de Passivos Financeiros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O saldo da Conta Financeira é calculado pela diferença entre a <u>aquisição líquida de "
                      "Ativos Financeiros</u> e a <u>incidência líquida de Passivos Financeiros</u>."),
        "poucas": ("É a definição do BPM6: " + vd("CF = Δativos − Δpassivos") + ". Saldo positivo = o país "
                   "acumula ativos externos líquidos (empresta ao resto do mundo)."),
        "destrinchando": [
            "O " + azb("BPM6") + " abandonou o par crédito/débito na conta financeira e passou a apresentar "
            "cada rubrica em " + azb("ativos") + " (aquisição líquida: compras − vendas de ativos externos por "
            "residentes) e " + azb("passivos") + " (incidência líquida: novas obrigações − amortizações com não "
            "residentes).",
            "Saldo = ativos − passivos. Exemplo: residentes compram US$ 30 bi em títulos estrangeiros e não "
            "residentes investem US$ 50 bi no país → CF = 30 − 50 = " + vd("−20") + ": o país tomou "
            "recursos líquidos do exterior.",
            "Ligação com as demais contas: " + vd("CF = TC + K + EO") + ". Déficit em transações correntes "
            "costuma vir com CF negativa (passivos crescendo mais que ativos) — o país financia o déficit "
            "com capital externo.",
            "Atenção ao sinal, que inverteu em relação ao BPM5: lá, entrada de capital era crédito "
            "(positiva). No BPM6, entrada de capital estrangeiro = aumento de passivo = <b>reduz</b> o saldo "
            "da CF.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição literal do manual. O estranhamento vem do jargão "
                       "(“incidência líquida de passivos”) e da convenção de sinais nova; quem pensa em “entrada "
                       "de capital = positivo” desconfia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No BPM6, o ingresso de investimento estrangeiro direto eleva o saldo da conta "
            "financeira.”</i> → ERRADO (inversão: aumenta passivos e reduz o saldo)",
            "<i>“No BPM6, um déficit em transações correntes, sem erros e omissões nem conta capital, "
            "corresponde a saldo negativo da conta financeira.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "É a nova definição do saldo da conta financeira.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01295
    {
        "id": "ECO-E2-L01295-1", "fonte_ref": "E2-L01295", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AGREG_3,
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta, se o investimento é superior à poupança doméstica, o saldo total do "
                      "balanço de pagamentos é necessariamente negativo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma economia aberta, se o investimento é superior à poupança doméstica, o saldo ")
                    + vm("total") + az(" do balanço de pagamentos é necessariamente negativo.")),
        "poucas": ("I > S doméstica implica " + azb("déficit em transações correntes") + " (poupança externa "
                   "positiva). O saldo <b>total</b> do BP depende também da conta capital e financeira, que pode "
                   "mais do que cobrir o déficit."),
        "destrinchando": [
            "Identidade: " + vd("I = S<sub>priv</sub> + S<sub>gov</sub> + S<sub>ext</sub>") + ". Com "
            "S<sub>dom</sub> = S<sub>priv</sub> + S<sub>gov</sub>: I − S<sub>dom</sub> = S<sub>ext</sub> = "
            + vd("−TC") + ". Logo I > S<sub>dom</sub> ⇔ " + vd("TC < 0") + " — isso sim é necessário.",
            "O “saldo total do BP” (linguagem do " + azb("BPM5") + ") era TC + conta capital e financeira + EO, "
            "igual à variação de reservas. Se o déficit em TC for financiado por entradas de capital maiores "
            "que ele, o saldo total é <b>positivo</b> e as reservas crescem.",
            "Exemplo: TC = −50 e entradas líquidas de capital = +70 → saldo do BP = " + vd("+20") + " "
            "(acúmulo de reservas), apesar de I > S. Foi a configuração do " + rx("Brasil") + " entre o fim "
            "da década de 2000 e o início da de 2010, com déficit externo e reservas em alta.",
            "No " + azb("BPM6") + ", o “saldo total” deixou de ser linha do BP: a variação de reservas está "
            "dentro da conta financeira, e a identidade é " + vd("TC + K + EO = CF") + ". Mesmo assim, o "
            "déficit em TC nada diz, sozinho, sobre o sinal da variação das reservas.",
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O item troca “transações correntes” "
                       "por “saldo total do BP” e fecha com “necessariamente”. A identidade macro garante só o "
                       "sinal de TC; o resto depende do financiamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se o investimento é superior à poupança doméstica, o saldo em transações correntes é "
            "necessariamente negativo.”</i> → CERTO",
            "<i>“…se o investimento é superior à poupança doméstica, a poupança externa é negativa.”</i> → "
            "ERRADO (sinal trocado: é positiva)",
        ])],
        "reescrita": ("Em uma economia aberta, se o investimento é superior à poupança doméstica, o saldo "
                      + hl("em transações correntes") + " do balanço de pagamentos é necessariamente negativo."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["necessariamente"], "dificuldade": 2,
        "comentario_fonte": "I − S dom = S ext > 0, ou seja, TC < 0; o saldo do BP (BPM5) soma TC e conta capital "
                            "e financeira, de sinal desconhecido.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01296
    {
        "id": "ECO-E2-L01296-1", "fonte_ref": "E2-L01296", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_AGREG_3,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento dos pagamentos de juros ao exterior gera uma diminuição do saldo (ou um aumento do "
                      "déficit) da conta Financeira do Balanço de Pagamentos, ceteris paribus."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Um aumento dos pagamentos de juros ao exterior gera uma diminuição do saldo (ou um aumento "
                       "do déficit) da conta ") + vm("Financeira") + az(" do Balanço de Pagamentos, ceteris "
                                                                        "paribus.")),
        "poucas": ("Juros pagos ao exterior são débito em " + azb("renda primária") + ": o saldo que piora "
                   "diretamente é o de " + azb("transações correntes") + ", não o da conta financeira."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Pelas " + azb("partidas dobradas") + ", todo pagamento tem contrapartida financeira "
                          "(saída de depósitos ou de reservas), e no BPM6 " + vd("CF = TC + K + EO") + ": se TC "
                          "cai e o resto fica constante, o saldo da CF (ativos − passivos) também cai. Lido assim, "
                          "o item seria CERTO. O ERRADO se sustenta pela leitura usual da banca — em que conta o "
                          "<b>juro</b> é lançado —, que é a mais provável numa prova.")],
        "destrinchando": [
            "Onde se lança: o pagamento de juros é " + azb("renda de investimento") + ", subconta da "
            + azb("renda primária") + ", dentro de " + azb("transações correntes") + ". Juros, lucros e "
            "dividendos remeteram-se sempre por aí; é a principal fonte do déficit externo estrutural do "
            + rx("Brasil") + ".",
            "Para comparar: a " + azb("amortização") + " do principal reduz um passivo e é lançada na conta "
            "financeira, sem afetar transações correntes. Daí a regra: juro piora TC; amortização mexe só na "
            "CF.",
            "A contrapartida do pagamento de juros, porém, está na conta financeira (por exemplo, redução de "
            "depósitos no exterior ou de reservas). No " + azb("BPM6") + ", como a CF é ativos − passivos e "
            "inclui as reservas, ela acompanha TC + K — é isso que torna o item discutível.",
            vm("Regra-âncora: juro (rendimento) → renda primária; principal (estoque) → conta financeira."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item desloca o lançamento dos juros para a conta "
                       "financeira, apoiado no senso comum de que “juro é coisa financeira”. A banca quer a "
                       "classificação da rubrica, não a contrapartida."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento dos pagamentos de juros ao exterior reduz o saldo da conta de transações correntes, "
            "ceteris paribus.”</i> → CERTO",
            "<i>“Um aumento das amortizações da dívida externa reduz o saldo em transações correntes.”</i> → "
            "ERRADO (troca de conceito: amortização é conta financeira)",
        ])],
        "reescrita": ("Um aumento dos pagamentos de juros ao exterior gera uma diminuição do saldo (ou um aumento do "
                      "déficit) da conta " + hl("de Transações Correntes (renda primária)") + " do Balanço de "
                      "Pagamentos, ceteris paribus."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["ceteris paribus"], "dificuldade": 2,
        "comentario_fonte": "Pagamento de juros é registrado na renda primária, em transações correntes.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: pelas partidas dobradas e pela identidade do BPM6 (CF = TC + K + EO), a queda "
                    "de TC também reduz o saldo da conta financeira; ERRADO mantido pela leitura de "
                    "classificação da rubrica"],
    },
    # ------------------------------------------------------------------ E2-L01308
    {
        "id": "ECO-E2-L01308-1", "fonte_ref": "E2-L01308", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q1,
        "rotulo_item": "Item",
        "assertiva": ("As exportações líquidas de uma economia devem sempre igualar a diferença entre sua poupança e "
                      "seu investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As exportações líquidas de uma economia devem <u>sempre</u> igualar a diferença entre sua "
                      "poupança e seu investimento."),
        "poucas": ("É uma " + azb("identidade contábil") + ": de Y = C + I + G + NX e S = Y − C − G sai "
                   + vd("S − I = NX") + ". Por ser identidade, vale “sempre”."),
        "destrinchando": [
            "Dedução: Y = C + I + G + NX → Y − C − G = I + NX → " + vd("S = I + NX") + " → "
            + vd("NX = S − I") + ", em que S é a poupança nacional (privada + pública).",
            "Leitura econômica (" + oc("Mankiw") + "): S − I é a " + azb("saída líquida de capital") + ". Se "
            "S > I, o país exporta mais do que importa e empresta a diferença ao exterior; se S < I, importa "
            "mais, e estrangeiros financiam parte do investimento doméstico.",
            "Identidade não é teoria causal: ela não diz se é o déficit comercial que causa a falta de poupança "
            "ou o contrário. É por isso que o “sempre” não é armadilha aqui — identidades valem por "
            "construção.",
            "Precisão de manual: no modelo simples, NX faz o papel de " + azb("transações correntes") + ". Com "
            "rendas e transferências externas, a identidade exata usa a poupança nacional bruta disponível: "
            "S − I = TC.",
            "Aplicação: a tese dos " + azb("déficits gêmeos") + " sai daqui — com S<sub>priv</sub> − I estável, "
            "um déficit público maior (S<sub>gov</sub> menor) se traduz em déficit externo maior.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O “sempre” costuma sinalizar erro, mas aqui "
                       "protege uma identidade. Regra prática: diante de modulador absoluto, pergunte se a "
                       "frase é identidade contábil (vale sempre) ou relação comportamental (tem exceções)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As exportações líquidas tendem a igualar a diferença entre poupança e investimento, salvo em "
            "economias com câmbio fixo.”</i> → ERRADO (restrição indevida: identidade sem exceção)",
            "<i>“Se a poupança nacional supera o investimento, a economia é exportadora líquida de "
            "capital.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": "Identidade Y = C + I + G + NX → S − I = NX; S − I é o fluxo líquido de capital para o "
                            "exterior (Mankiw).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01309
    {
        "id": "ECO-E2-L01309-1", "fonte_ref": "E2-L01309", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q1,
        "rotulo_item": "Item",
        "assertiva": ("O fluxo de saída de capital líquido é igual ao montante que os residentes internos estão "
                      "emprestando ao exterior menos o montante que os estrangeiros estão nos emprestando."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O fluxo de saída de capital líquido é igual ao montante que os residentes internos estão "
                      "<u>emprestando ao exterior menos</u> o montante que os estrangeiros estão nos "
                      "emprestando."),
        "poucas": ("É a definição de " + azb("saída líquida de capital") + " (" + oc("Mankiw") + "): compras de "
                   "ativos externos por residentes " + vd("menos") + " compras de ativos domésticos por "
                   "estrangeiros."),
        "destrinchando": [
            azb("Saída líquida de capital") + " (<i>net capital outflow</i>, NCO) = o que residentes aplicam "
            "lá fora (títulos, ações, empréstimos, empresas) − o que estrangeiros aplicam aqui. “Emprestar” "
            "está em sentido amplo: inclui qualquer aquisição de ativos.",
            "Identidade-chave: " + vd("NCO = NX = S − I") + ". Todo superávit comercial tem de virar ativo "
            "externo líquido (as divisas recebidas são aplicadas fora); todo déficit é financiado por "
            "estrangeiros adquirindo ativos domésticos.",
            "No vocabulário do " + azb("BPM6") + ", NCO corresponde ao saldo da " + azb("conta financeira")
            + " (aquisição líquida de ativos − incidência líquida de passivos), reservas incluídas.",
            "NCO > 0: o país é credor líquido no fluxo (caso de China, Alemanha); NCO < 0: devedor líquido, "
            "como o " + rx("Brasil") + " na maior parte de sua história, com déficit em transações correntes.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, com a ordem certa da subtração (o que "
                       "sai menos o que entra). A banca costuma inverter a ordem ou trocar “saída” por "
                       "“entrada”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A saída líquida de capital é igual ao que os estrangeiros emprestam ao país menos o que os "
            "residentes emprestam ao exterior.”</i> → ERRADO (inversão: essa é a entrada líquida)",
            "<i>“Numa economia aberta, a saída líquida de capital é igual às exportações líquidas.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Definição do termo: diferença entre saída e entrada de capital do país.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01312
    {
        "id": "ECO-E2-L01312-1", "fonte_ref": "E2-L01312", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q2,
        "rotulo_item": "Item",
        "assertiva": ("O Balanço de Pagamentos é o registro contábil de todas as transações de um país com o resto "
                      "do mundo. Envolve tanto transações com bens e serviços como transações com capitais físicos "
                      "e financeiros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Balanço de Pagamentos é o registro contábil de <u>todas as transações</u> de um país com o "
                      "resto do mundo. Envolve tanto transações com bens e serviços como transações com capitais "
                      "físicos e financeiros."),
        "poucas": ("Definição de manual: o BP registra os " + azb("fluxos") + " entre residentes e não "
                   "residentes num período — bens, serviços, rendas, transferências e capitais (físicos e "
                   "financeiros)."),
        "destrinchando": [
            "“País com o resto do mundo” quer dizer, tecnicamente, " + azb("residentes × não residentes") + ". "
            "Residência é o centro de interesse econômico (ficar ou pretender ficar ≥ 1 ano), não "
            "nacionalidade: a filial de multinacional estrangeira no " + rx("Brasil") + " é residente.",
            "Cobertura: bens e serviços (balança comercial e de serviços); remuneração de fatores (renda "
            "primária); transferências (renda secundária e de capital); ativos não financeiros não produzidos "
            "(conta capital); ativos e passivos financeiros (conta financeira).",
            "“Capitais físicos” aparece em dois lugares: a compra de uma fábrica por estrangeiros é "
            + azb("investimento direto") + " (conta financeira, porque se adquire participação no capital); "
            "terrenos e recursos naturais em si, quando transacionados, vão para a conta capital.",
            "O BP é " + azb("fluxo") + " (um período); o " + azb("estoque") + " de ativos e passivos externos "
            "é a " + azb("posição de investimento internacional") + " (PII).",
        ],
        "dissecando": (cz("[literalidade]") + " Definição genérica, sem armadilha de rótulo. O “todas as "
                       "transações” é seguro porque o BP de fato pretende cobrir todas; a imprecisão “país” em "
                       "vez de “residentes” não basta para invalidar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O balanço de pagamentos registra as transações entre cidadãos de um país e estrangeiros.”</i> "
            "→ ERRADO (troca de conceito: o critério é residência, não nacionalidade)",
            "<i>“O balanço de pagamentos registra o estoque de ativos externos do país em determinada "
            "data.”</i> → ERRADO (troca de conceito: estoque é a PII)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["todas"], "dificuldade": 1,
        "comentario_fonte": "O BP registra as relações do país com o resto do mundo (residentes e não residentes) "
                            "e envolve todas as transações mencionadas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01313
    {
        "id": "ECO-E2-L01313-1", "fonte_ref": "E2-L01313", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q2,
        "rotulo_item": "Item",
        "assertiva": ("A contabilização dessas transações segue as normas gerais de contabilidade, não seguindo, "
                      "porém, o método das partidas dobradas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A contabilização dessas transações segue as normas gerais de contabilidade, ")
                    + vm("não seguindo, porém,") + az(" o método das partidas dobradas.")),
        "poucas": ("O BP é montado por " + azb("partidas dobradas") + ": cada transação gera um crédito e um "
                   "débito de mesmo valor. É por isso que, em tese, o saldo total é zero."),
        "destrinchando": [
            "Toda transação tem duas pontas. Exportação de US$ 100: " + vd("crédito") + " em bens (transações "
            "correntes) e " + vd("débito") + " (aumento de ativo) na conta financeira — depósitos no exterior "
            "ou reservas.",
            "Juros pagos ao exterior: débito em renda primária; crédito na conta financeira (redução de "
            "ativos ou aumento de passivos). Doação recebida em mercadoria: crédito em renda secundária, débito "
            "em bens (importação).",
            "Consequência: " + vd("TC + K + EO = CF") + " (BPM6). Se a soma não fecha, a culpa é das fontes "
            "estatísticas, e a diferença vai para " + azb("erros e omissões") + ".",
            "Convenção de sinais (BPM6): crédito = exportações e rendimentos recebidos; débito = importações e "
            "rendimentos pagos. Na conta financeira, apresentam-se variações líquidas de ativos e de passivos.",
            vm("Regra-âncora: partidas dobradas → todo lançamento tem contrapartida → o BP sempre fecha."),
        ],
        "dissecando": (cz("[contradição]") + " A frase nega justamente o princípio que estrutura o BP. A pista "
                       "interna: se segue “as normas gerais de contabilidade”, não poderia abrir mão da partida "
                       "dobrada, que é o núcleo delas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo método das partidas dobradas, o saldo global do balanço de pagamentos, incluídos erros e "
            "omissões, é nulo.”</i> → CERTO",
            "<i>“No balanço de pagamentos, as doações recebidas em mercadorias não geram lançamento, por não "
            "envolverem pagamento.”</i> → ERRADO (há crédito em renda secundária e débito em bens)",
        ])],
        "reescrita": ("A contabilização dessas transações segue as normas gerais de contabilidade, "
                      + hl("inclusive") + " o método das partidas dobradas."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": ["porém"], "dificuldade": 1,
        "comentario_fonte": "O BP utiliza o método das partidas dobradas: cada transação é registrada em pelo menos "
                            "duas contas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01314
    {
        "id": "ECO-E2-L01314-1", "fonte_ref": "E2-L01314", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q2,
        "rotulo_item": "Item",
        "assertiva": ("Se o saldo do Balanço de Transações Correntes for positivo, temos uma Poupança Externa "
                      "Positiva."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o saldo do Balanço de Transações Correntes for positivo, temos uma Poupança Externa ")
                    + vm("Positiva") + az(".")),
        "poucas": ("Poupança externa é o " + azb("simétrico do saldo em transações correntes") + ": "
                   + vd("S<sub>ext</sub> = −TC") + ". TC positivo → poupança externa <b>negativa</b>: o país "
                   "financia o resto do mundo."),
        "destrinchando": [
            azb("Poupança externa") + " é a poupança que o resto do mundo põe à disposição do país para "
            "financiar seu investimento. Ela só existe se o país gasta mais do que sua renda disponível, isto "
            "é, se há " + vd("déficit em TC") + ".",
            "Identidade: I = S<sub>priv</sub> + S<sub>gov</sub> + S<sub>ext</sub>, com " + vd("S<sub>ext</sub> "
            "= −TC") + ". TC > 0 (superávit) → S<sub>ext</sub> < 0: o país investe menos do que poupa e "
            "empresta a diferença ao exterior.",
            "Exemplos: superavitários crônicos (China, Alemanha, Japão) têm poupança externa negativa — "
            "exportam poupança. O " + rx("Brasil") + ", com déficits recorrentes em TC, usa poupança externa "
            "positiva.",
            "Ligação com a conta financeira (BPM6): TC > 0 corresponde a " + vd("CF > 0") + " (acúmulo líquido "
            "de ativos externos) — mais um modo de ver que o país está “emprestando”, não “recebendo”.",
        ],
        "dissecando": (cz("[inversão]") + " Troca o sinal de uma identidade. Armadilha de vocabulário: "
                       "“positivo” no TC e “positiva” na poupança soam coerentes, mas as duas variáveis têm sinais "
                       "opostos por definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o saldo em transações correntes for negativo, a poupança externa será positiva.”</i> → "
            "CERTO",
            "<i>“Superávit em transações correntes indica que o país absorve poupança do resto do mundo.”</i> "
            "→ ERRADO (inversão: ele exporta poupança)",
        ])],
        "reescrita": ("Se o saldo do Balanço de Transações Correntes for positivo, temos uma Poupança Externa "
                      + hl("Negativa") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A poupança externa é o contrário do saldo em TC; com STC positivo, o país é investidor "
                            "líquido no exterior e sua poupança externa é negativa.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01315
    {
        "id": "ECO-E2-L01315-1", "fonte_ref": "E2-L01315", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q3,
        "rotulo_item": "Item",
        "assertiva": "Caso a renda nacional se amplie, há tendência de redução do saldo de Transações Correntes.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Caso a renda nacional se amplie, <u>há tendência</u> de redução do saldo de Transações "
                      "Correntes."),
        "poucas": ("As " + azb("importações dependem da renda doméstica") + " (propensão marginal a importar): "
                   "renda maior → mais importações → saldo comercial e de TC menor, mantidos o câmbio e a renda "
                   "externa."),
        "destrinchando": [
            "Função de importações típica: " + vd("M = M₀ + m·Y") + ", com 0 < m < 1 (propensão marginal a "
            "importar). Exportações dependem da renda do <b>resto do mundo</b> e do câmbio, não da renda "
            "doméstica.",
            "Logo, com Y crescendo e o resto constante: M ↑, X estável → " + vd("NX ↓") + " → TC ↓. Na "
            "economia aberta keynesiana, é esse " + azb("vazamento") + " que reduz o multiplicador: "
            "1/(1 − c + m).",
            "Pela identidade " + vd("TC = RNBD − A") + ": crescimento puxado pela demanda interna eleva a "
            "absorção, e parte dela se dirige a bens importados.",
            "Contrapartida: crescimento do " + azb("resto do mundo") + " aumenta nossas exportações e melhora "
            "o TC. Também pesa a renda primária: lucros de filiais estrangeiras crescem com a economia e são "
            "remetidos.",
            "No " + rx("Brasil") + ", o padrão é visível: fases de forte crescimento costumam vir com "
            "deterioração do TC, e recessões, com melhora rápida do saldo externo.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “há tendência” salva o item: não afirma que o saldo cai "
                       "sempre (o câmbio ou a renda externa podem compensar), só a direção do efeito-renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Caso a renda nacional se amplie, o saldo de transações correntes necessariamente se torna "
            "deficitário.”</i> → ERRADO (modulador absoluto: pode só diminuir um superávit)",
            "<i>“Um aumento da renda do resto do mundo tende a elevar o saldo de transações correntes do "
            "país.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["há tendência"], "dificuldade": 1,
        "comentario_fonte": "Com maior renda nacional, há maior pressão por importação de bens e serviços.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01316
    {
        "id": "ECO-E2-L01316-1", "fonte_ref": "E2-L01316", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q3,
        "rotulo_item": "Item",
        "assertiva": ("Na conta capital são contabilizadas as contrapartidas financeiras das exportações e "
                      "importações de mercadorias e serviços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Na <u>conta capital</u> são contabilizadas as contrapartidas financeiras das exportações e "
                      "importações de mercadorias e serviços."),
        "poucas": ("O CERTO só se sustenta se “conta capital” for lida no sentido amplo e antigo (a “conta "
                   "capital e financeira”). Pelo " + azb("BPM6") + " — e já pelo BPM5 —, as contrapartidas "
                   "financeiras do comércio vão para a " + azb("conta financeira") + "."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A estrutura atual separa " + azb("conta capital") + " (ativos não financeiros não "
                          "produzidos e transferências de capital) e " + azb("conta financeira") + " (ativos e "
                          "passivos financeiros). O pagamento de uma exportação — divisas recebidas, crédito "
                          "comercial concedido — é variação de ativo ou passivo <b>financeiro</b>: conta "
                          "financeira. O gabarito CERTO pressupõe a terminologia antiga, em que “conta de "
                          "capital” designava todo o movimento de capitais. A leitura mais defensável hoje é "
                          "ERRADO.")],
        "destrinchando": [
            "Partidas dobradas: exportação de US$ 100 → crédito em bens; a contrapartida é débito (aumento de "
            "ativo) em depósitos no exterior, reservas ou créditos comerciais — rubricas de " + vd("outros "
            "investimentos") + " ou de " + vd("ativos de reserva") + ", ambas na conta financeira.",
            "Conta capital (BPM6): " + vd("(a)") + " compra e venda de ativos não financeiros não produzidos — "
            "terras para embaixadas, direitos de exploração, licenças, marcas e nomes de domínio vendidos "
            "separadamente; " + vd("(b)") + " transferências de capital — perdão de dívida, doações para "
            "investimento. Passes de atletas costumam ser citados como exemplo por manuais brasileiros.",
            "Histórico da nomenclatura: até o BPM4 e em manuais anglo-saxões antigos (<i>capital account</i>), "
            "“conta de capital” abrangia todos os fluxos financeiros. O " + azb("BPM5") + " (1993) criou a "
            "dupla “conta capital e financeira”, e o " + azb("BPM6") + " (2009) consolidou as duas como contas "
            "distintas.",
            ESTRUTURA_BPM6,
        ],
        "dissecando": (cz("[troca de conceito]") + " O item usa “conta capital” onde a nomenclatura atual pede "
                       "“conta financeira”. Em prova CEBRASPE recente, a versão mais segura é tratar a frase como "
                       "ERRADA; o CERTO deste simulado só vale no vocabulário antigo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na conta financeira são contabilizadas as contrapartidas financeiras das exportações e "
            "importações de mercadorias e serviços.”</i> → CERTO",
            "<i>“Na conta capital é registrado o perdão de dívida externa concedido por credores "
            "oficiais.”</i> → CERTO",
        ])],
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "CORRETO — e define a conta capital como aquisição e alienação de bens não financeiros "
                            "não produzidos e transferências de capital (passes de atletas, perdão de dívida).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: pelo BPM5 e pelo BPM6 as contrapartidas financeiras do comércio vão para a conta "
                    "financeira; o CERTO só vale na terminologia antiga de “conta de capital” ampla",
                    "qualidade_fonte: o comentário de origem marca CORRETO, mas define a conta capital de modo que "
                    "contradiz o próprio gabarito"],
    },
    # ------------------------------------------------------------------ E2-L01317
    {
        "id": "ECO-E2-L01317-1", "fonte_ref": "E2-L01317", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q3,
        "rotulo_item": "Item",
        "assertiva": ("Na ausência de Erros e Omissões, a soma da Conta Corrente, da Conta Capital e da Conta "
                      "Financeira é igual à variação das reservas internacionais da autoridade monetária do país, "
                      "decorrente de transações com o resto do mundo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na ausência de Erros e Omissões, a soma da Conta Corrente, da Conta Capital e da Conta "
                      "Financeira é igual à <u>variação das reservas internacionais</u> da autoridade monetária "
                      "do país, decorrente de transações com o resto do mundo."),
        "poucas": ("É a lógica do “resultado do BP”: tudo o que entra e sai em transações correntes, de capital "
                   "e financeiras (fora as reservas) desemboca na " + azb("variação das reservas") + ", que "
                   "fecha as partidas dobradas."),
        "destrinchando": [
            "Na estrutura do " + azb("BPM5") + ", com sinais de crédito positivo: " + vd("TC + K + CF + EO = "
            "resultado do BP = Δreservas") + ", com a conta financeira <b>sem</b> as reservas. Resultado "
            "positivo = acúmulo de reservas.",
            "Exemplo: TC = −30 (déficit) e entradas líquidas de capital = +45 → resultado = " + vd("+15") + ": o "
            "BC comprou os dólares que sobraram, e as reservas subiram 15.",
            "No " + azb("BPM6") + ", com as reservas dentro da conta financeira e o saldo medido como ativos − "
            "passivos, a mesma ideia se escreve " + vd("TC + K + EO = CF") + ": a variação de reservas é parte da "
            "CF. O item só fecha lendo “Conta Financeira” como a CF sem os ativos de reserva, à moda do BPM5.",
            "A ressalva “decorrente de transações” importa: as reservas também variam por " + azb("reavaliação") + " "
            "(câmbio entre moedas, preço do ouro) e por rendimentos, efeitos que não passam pelo BP como "
            "transação e aparecem só na posição de investimento internacional.",
            "Com câmbio flutuante puro, o BC não intervém, Δreservas ≈ 0 e o resultado do BP tende a zero: o "
            "câmbio se ajusta para que entradas e saídas se igualem.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Correto na estrutura de manual em que a conta financeira "
                       "exclui as reservas. Os detalhes que blindam o item são “na ausência de erros e omissões” "
                       "e “decorrente de transações com o resto do mundo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Toda variação do estoque de reservas internacionais decorre de transações registradas no "
            "balanço de pagamentos.”</i> → ERRADO (modulador absoluto: há variação por reavaliação)",
            "<i>“Em regime de câmbio flutuante sem intervenção, a variação de reservas por transações tende a "
            "zero.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["na ausência de"], "dificuldade": 2,
        "comentario_fonte": "O resultado do BP define se o país acumulou ou perdeu reservas internacionais.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01318
    {
        "id": "ECO-E2-L01318-1", "fonte_ref": "E2-L01318", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q3,
        "rotulo_item": "Item",
        "assertiva": ("Para “zerar” o sistema, introduz-se a conta de Haveres da Autoridade Monetária, onde um saldo "
                      "negativo representa diminuição nas reservas internacionais do país, e um saldo positivo, um "
                      "aumento nas reservas internacionais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para “zerar” o sistema, introduz-se a conta de Haveres da Autoridade Monetária, onde um "
                       "saldo negativo representa ") + vm("diminuição") + az(" nas reservas internacionais do "
                                                                            "país, e um saldo positivo, ")
                    + vm("um aumento") + az(" nas reservas internacionais.")),
        "poucas": ("A conta de " + azb("haveres da autoridade monetária") + " é lançada com sinal "
                   + vd("oposto") + " ao resultado do BP: saldo negativo = <b>aumento</b> de reservas (débito, "
                   "aquisição de ativo); positivo = <b>diminuição</b>."),
        "destrinchando": [
            "No " + azb("BPM5") + ", o BCB apresentava: TC + conta capital e financeira + EO = " + azb("resultado "
            "do balanço") + "; logo abaixo, " + vd("haveres da autoridade monetária (− = aumento)") + ", igual "
            "ao resultado com sinal trocado. Somadas, as duas linhas dão zero — é o “zerar” do item.",
            "Por que o sinal negativo? Nas partidas dobradas, aumento de ativo é " + vd("débito") + ". Quando o "
            "BC acumula reservas, adquire ativo externo: lançamento negativo. Superávit de 15 no resultado → "
            "haveres = −15.",
            azb("Erros e omissões") + " têm outro papel: são o resíduo estatístico entre as contas medidas por "
            "fontes diferentes. Também “fecham” o BP, mas não representam reservas. Por isso há quem aponte o "
            "erro no papel de “zerar” — e, de fato, não é o EO que ele descreve.",
            "No " + azb("BPM6") + ", a figura dos haveres desapareceu: as reservas viraram " + azb("ativos de "
            "reserva") + " dentro da conta financeira, apresentados como aquisição líquida (aumento = sinal "
            "positivo).",
            vm("Regra-âncora: BPM5 — haveres com sinal trocado (− = aumento); BPM6 — ativos de reserva na CF, "
               "+ = aumento."),
        ],
        "dissecando": (cz("[inversão]") + " O item descreve corretamente a função da conta (compensar o "
                       "resultado) e inverte a convenção de sinal, intuitiva para quem pensa em “saldo positivo = "
                       "mais reservas”. Pista: conta que zera o sistema tem de ter sinal oposto ao resultado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na apresentação do BPM5, um resultado superavitário do balanço de pagamentos corresponde a "
            "haveres da autoridade monetária com sinal negativo.”</i> → CERTO",
            "<i>“No BPM6, a conta de haveres da autoridade monetária segue fora da conta financeira.”</i> → "
            "ERRADO (anacronismo: virou ativos de reserva, dentro da CF)",
        ])],
        "reescrita": ("Para “zerar” o sistema, introduz-se a conta de Haveres da Autoridade Monetária, onde um saldo "
                      "negativo representa " + hl("aumento") + " nas reservas internacionais do país, e um saldo "
                      "positivo, " + hl("uma diminuição") + " nas reservas internacionais."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": "ERRADO: para zerar o sistema introduz-se a conta erros e omissões; haveres da "
                            "autoridade monetária indica a variação de reservas.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem atribui o erro ao papel de “zerar” (que seria de erros "
                    "e omissões); na apresentação do BPM5, a linha de haveres (− = aumento) zera o resultado, e o "
                    "erro objetivo do item é o sinal invertido"],
    },
    # ------------------------------------------------------------------ E2-L01319 (1)
    {
        "id": "ECO-E2-L01319-1", "fonte_ref": "E2-L01319", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q4,
        "excerto_tabela": TAB_Q4,
        "rotulo_item": "Item",
        "assertiva": "O saldo da Balança Comercial foi positivo em US$ 20 bilhões.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O saldo da <u>Balança Comercial</u> foi positivo em US$ 20 bilhões."),
        "poucas": ("Balança comercial = só " + azb("bens") + ": exportações − importações = 100 − 80 = "
                   + vd("+20") + ". Fretes, donativos e empréstimos ficam de fora."),
        "destrinchando": [
            "A " + azb("balança comercial") + " registra mercadorias, com valores " + vd("FOB") + " (sem frete "
            "e seguro). O frete pago a estrangeiros vai para a " + azb("balança de serviços") + " (transportes).",
            "Classificando a tabela inteira: exportações e importações → bens; fretes pagos → serviços (−20); "
            "donativos recebidos → " + azb("renda secundária") + " (+5); empréstimos externos (+20) e "
            "amortizações (−10) → movimento de capitais (conta financeira).",
            "Saldos resultantes: balança comercial " + vd("+20") + "; serviços " + vd("−20") + "; renda "
            "secundária " + vd("+5") + "; transações correntes " + vd("+5") + "; capitais " + vd("+10") + "; "
            "variação de reservas " + vd("+15") + " (5 + 10).",
            "Roteiro para qualquer tabela de BP: (1) classificar cada linha na sua conta; (2) atribuir sinal "
            "(recebimento +, pagamento −); (3) somar por conta, de baixo para cima.",
        ],
        "dissecando": (cz("[literalidade]") + " Cálculo direto. A única armadilha seria somar o frete à "
                       "balança comercial (dando zero) — mas frete é serviço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo da balança comercial e de serviços foi nulo.”</i> → CERTO",
            "<i>“O saldo da balança comercial, incluídos os fretes pagos, foi de US$ 20 bilhões.”</i> → ERRADO "
            "(frete é serviço; a soma daria zero)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "100 de exportações menos 80 de importações.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 232", "tipo_fonte": "TABELA", "lado": "frente",
                           "acao": "transcrita_html (tabela aninhada, 3 colunas)"}],
        "alertas": ["texto_parcial: tabela da IMAGEM 232 reconstruída pela descrição; a coluna “Sentido” "
                    "(donativos recebidos, fretes e amortizações pagos, empréstimos ingressados) foi deduzida dos "
                    "sinais do gabarito comentado"],
    },
    # ------------------------------------------------------------------ E2-L01319 (2)
    {
        "id": "ECO-E2-L01319-2", "fonte_ref": "E2-L01319", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q4,
        "excerto_tabela": TAB_Q4,
        "rotulo_item": "Item",
        "assertiva": "O saldo de Transações Correntes foi de US$ 45 bilhões.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O saldo de Transações Correntes foi de US$ ") + vm("45") + az(" bilhões."),
        "poucas": ("TC = bens + serviços + renda primária + renda secundária = 20 − 20 + 0 + 5 = " + vd("+5")
                   + ". Empréstimos e amortizações não entram."),
        "destrinchando": [
            azb("Transações correntes") + " (BPM6) = balança comercial + serviços + " + azb("renda primária")
            + " + " + azb("renda secundária") + ".",
            "Na tabela: bens " + vd("+20") + " (100 − 80); serviços " + vd("−20") + " (fretes pagos); renda "
            "primária " + vd("0") + " (não há juros, lucros nem salários); renda secundária " + vd("+5") + " "
            "(donativos). Total: " + vd("+5") + ".",
            "O 45 sai de erros típicos: tratar o frete pago como receita (20 + 20 + 5 = 45) ou misturar "
            "empréstimos (+20) com as correntes. Empréstimos e amortizações são " + azb("conta financeira") + ", "
            "porque mexem em passivos.",
            "Fechamento: TC (+5) + capitais (+10) = " + vd("+15") + " de variação de reservas — o país teve "
            "superávit corrente pequeno e ainda recebeu capital líquido.",
        ],
        "dissecando": (cz("[dado alterado]") + " Número fabricado a partir de um erro de sinal no frete. Em "
                       "tabelas de BP, confira o sinal de cada serviço: frete <b>pago</b> é débito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo de transações correntes foi positivo, embora inferior ao da balança comercial.”</i> → "
            "CERTO",
            "<i>“O saldo de transações correntes foi de US$ 25 bilhões.”</i> → ERRADO (incluiu o empréstimo "
            "líquido e esqueceu o frete)",
        ])],
        "reescrita": "O saldo de Transações Correntes foi de US$ " + hl("5") + " bilhões.",
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "+100 de exportações, −80 de importações, +5 de donativos recebidos, −20 de fretes "
                            "pagos = +5.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 232", "tipo_fonte": "TABELA", "lado": "frente",
                           "acao": "transcrita_html (tabela aninhada, 3 colunas)"}],
        "alertas": ["texto_parcial: tabela da IMAGEM 232 reconstruída pela descrição e pelos sinais do gabarito "
                    "comentado"],
    },
    # ------------------------------------------------------------------ E2-L01319 (3)
    {
        "id": "ECO-E2-L01319-3", "fonte_ref": "E2-L01319", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q4,
        "excerto_tabela": TAB_Q4,
        "rotulo_item": "Item",
        "assertiva": "O Balanço de Rendas Secundárias teve saldo positivo em US$ 15 bilhões.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Balanço de Rendas Secundárias teve saldo positivo em US$ ") + vm("15") + az(" bilhões."),
        "poucas": ("A única transferência corrente da tabela são os " + azb("donativos") + " recebidos: renda "
                   "secundária = " + vd("+5") + ". O 15 é a variação de reservas, outra coisa."),
        "destrinchando": [
            azb("Renda secundária") + " (antigas “transferências unilaterais correntes”) registra transferências "
            "sem contrapartida: donativos, remessas de trabalhadores, ajuda humanitária. Aqui, " + vd("+5") + ".",
            "Não entram: fretes (serviços), empréstimos e amortizações (conta financeira). Juros, lucros e "
            "salários iriam para a renda <b>primária</b> — e não há nenhum na tabela.",
            "De onde pode vir o 15: é a soma TC (+5) + capitais (+10), isto é, a " + azb("variação de "
            "reservas") + "; ou 20 − 5, confundindo fretes com transferências.",
            "Se os donativos fossem para <b>investimento</b> (doação de capital para construir uma escola, por "
            "exemplo), iriam para a " + azb("conta capital") + ", não para a renda secundária. Na falta de "
            "especificação, donativo é transferência corrente.",
        ],
        "dissecando": (cz("[dado alterado]") + " Item de conta: o sinal está certo (positivo), o valor não. O "
                       "número escolhido coincide com outro saldo da tabela para confundir quem calcula tudo "
                       "de uma vez."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo de renda primária foi nulo.”</i> → CERTO",
            "<i>“A conta de renda secundária registrou saldo negativo de US$ 5 bilhões.”</i> → ERRADO (sinal "
            "trocado: donativos recebidos são crédito)",
        ])],
        "reescrita": "O Balanço de Rendas Secundárias teve saldo positivo em US$ " + hl("5") + " bilhões.",
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "+5.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 232", "tipo_fonte": "TABELA", "lado": "frente",
                           "acao": "transcrita_html (tabela aninhada, 3 colunas)"}],
        "alertas": ["texto_parcial: tabela da IMAGEM 232 reconstruída pela descrição e pelos sinais do gabarito "
                    "comentado"],
    },
    # ------------------------------------------------------------------ E2-L01319 (4)
    {
        "id": "ECO-E2-L01319-4", "fonte_ref": "E2-L01319", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_Q4,
        "excerto_tabela": TAB_Q4,
        "rotulo_item": "Item",
        "assertiva": "O saldo da Conta Capital e da Conta Financeira foi igual a US$ 10 bilhões.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O saldo da Conta Capital e da Conta Financeira foi igual a <u>US$ 10 bilhões</u>."),
        "poucas": ("Movimento de capitais: empréstimos ingressados " + vd("+20") + " − amortizações pagas "
                   + vd("10") + " = " + vd("+10") + ", na convenção de crédito (entrada) positivo."),
        "destrinchando": [
            "Empréstimo externo recebido aumenta um passivo do país com não residentes; amortização o reduz. "
            "Ambos são " + azb("outros investimentos") + " (ou carteira, se forem títulos) na conta "
            "financeira. A conta capital, aqui, é zero.",
            "Na convenção do " + azb("BPM5") + " (ingresso = crédito), o saldo é " + vd("+10") + ". Somado a "
            "TC (+5), dá resultado de " + vd("+15") + ", que é o aumento de reservas.",
            "No " + azb("BPM6") + ", a conta financeira é ativos − passivos e inclui as reservas: passivos "
            "líquidos +10, ativos de reserva +15 → CF = 15 − 10 = " + vd("+5") + " = TC + K. O mesmo dado "
            "muda de número conforme a convenção — por isso convém ler o item com a estrutura que ele usa.",
            "Observe que o ingresso líquido de capital (10) e o superávit corrente (5) foram ambos convertidos "
            "em reservas: o BC comprou as divisas excedentes.",
        ],
        "dissecando": (cz("[literalidade]") + " Cálculo direto (20 − 10). O risco é incluir algo indevido — "
                       "os donativos (+5), que são correntes — e chegar a 15."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As reservas internacionais aumentaram US$ 15 bilhões.”</i> → CERTO",
            "<i>“O saldo da conta capital e financeira foi de US$ 30 bilhões.”</i> → ERRADO (somou as "
            "amortizações em vez de subtraí-las)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "+20 − 10 = 10.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 232", "tipo_fonte": "TABELA", "lado": "frente",
                           "acao": "transcrita_html (tabela aninhada, 3 colunas)"}],
        "alertas": ["texto_parcial: tabela da IMAGEM 232 reconstruída pela descrição e pelos sinais do gabarito "
                    "comentado"],
    },
    # ------------------------------------------------------------------ E2-L01663
    {
        "id": "ECO-E2-L01663-1", "fonte_ref": "E2-L01663", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_TEIX,
        "rotulo_item": "Item",
        "assertiva": ("As variações nas reservas internacionais são contabilizadas na Conta Financeira como Ativos "
                      "de Reserva."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As variações nas reservas internacionais são contabilizadas na <u>Conta Financeira</u> como "
                      "<u>Ativos de Reserva</u>."),
        "poucas": ("No " + azb("BPM6") + ", reservas são ativos financeiros externos como os demais: a variação "
                   "entra na " + azb("conta financeira") + ", rubrica " + azb("ativos de reserva") + "."),
        "destrinchando": [
            "Composição dos " + azb("ativos de reserva") + ": " + vd("ouro monetário") + ", " + vd("direitos "
            "especiais de saque (DES)") + ", " + vd("posição de reserva no FMI") + " e outros ativos em moeda "
            "estrangeira (depósitos, títulos de governos estrangeiros) sob controle da autoridade monetária.",
            "Para que servem: financiar desequilíbrios do BP, intervir no mercado de câmbio, dar segurança a "
            "credores e reduzir a vulnerabilidade externa.",
            "Sinal: no " + azb("BPM6") + ", a conta financeira mostra a aquisição líquida de ativos com sinal "
            "positivo — aumento de reservas eleva o saldo da CF. Na convenção de crédito/débito do " + azb("BPM5")
            + ", o mesmo aumento era débito (sinal negativo), lançado fora da conta financeira, em “haveres da "
            "autoridade monetária”.",
            "Consequência estrutural: o antigo “resultado do BP” sumiu como linha; na identidade do BPM6, "
            + vd("TC + K + EO = CF") + ", as reservas estão do lado direito, junto com os demais fluxos "
            "financeiros.",
            "⏳ (out/2026) O " + rx("Brasil") + " mantém reservas na casa de centenas de bilhões de dólares, "
            "acumuladas sobretudo a partir de meados dos anos 2000; valor corrente nas Estatísticas do Setor "
            "Externo do BCB.",
        ],
        "dissecando": (cz("[literalidade]") + " Regra de manual sem pegadinha de redação. Quem erra costuma "
                       "trazer a estrutura do BPM5, em que reserva era o fechamento do BP e ficava fora da conta "
                       "financeira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No BPM6, um aumento das reservas internacionais é registrado com sinal negativo na conta "
            "financeira.”</i> → ERRADO (convenção do BPM5: no BPM6, aquisição de ativo é positiva)",
            "<i>“A posição de reserva no FMI integra os ativos de reserva.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Reservas na conta financeira, subconta ativos de reserva (ouro, DES, posição no FMI, "
                            "moeda estrangeira); aumento descrito como débito/saída com sinal negativo.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 522", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (estrutura das transações correntes no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01286-1 (mesma assertiva, outra fonte)",
                    "duplicata: comentário de E2-L01734 fundido",
                    "qualidade_fonte: os comentários de origem dizem que o aumento de reservas entra com sinal "
                    "negativo na conta financeira, convenção de crédito/débito do BPM5; no BPM6, aquisição "
                    "líquida de ativos é positiva"],
    },
    # ------------------------------------------------------------------ E2-L01664
    {
        "id": "ECO-E2-L01664-1", "fonte_ref": "E2-L01664", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_TEIX,
        "rotulo_item": "Item",
        "assertiva": ("As remessas de dinheiro de imigrantes no exterior para seus países de origem são "
                      "contabilizadas na Conta Capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As remessas de dinheiro de imigrantes no exterior para seus países de origem são "
                       "contabilizadas na ") + vm("Conta Capital") + az(".")),
        "poucas": ("Remessa de imigrante é " + azb("transferência corrente") + ": vai para a " + azb("renda "
                   "secundária") + ", dentro das transações correntes — não para a conta capital."),
        "destrinchando": [
            "Critério que separa as transferências: a " + azb("corrente") + " financia consumo e não forma "
            "patrimônio do recebedor (remessas à família, ajuda humanitária em alimentos); a " + azb("de "
            "capital") + " transfere a propriedade de um ativo ou financia sua formação (perdão de dívida, "
            "doação para construir uma ponte).",
            azb("Conta capital") + " (BPM6): transferências de capital + compra e venda de ativos não "
            "financeiros não produzidos (terras para embaixadas, licenças, marcas). É uma conta pequena; "
            "remessas pessoais regulares não cabem nela.",
            azb("Renda secundária") + " = antigas “transferências unilaterais correntes” do BPM5: remessas de "
            "trabalhadores, doações correntes, contribuições a organismos internacionais.",
            "Cuidado com o vizinho: o <b>patrimônio</b> que o migrante leva ao mudar de país não é remessa — e, "
            "desde o BPM6, nem sequer entra no BP (não há transação entre residente e não residente).",
            vm("Regra-âncora: remessa pessoal → renda secundária; transferência de patrimônio/ativo → conta "
               "capital."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A palavra “transferência” serve aos dois lados; o item "
                       "escolhe o lado de capital. Pergunte: o dinheiro paga consumo (corrente) ou forma ativo "
                       "(capital)? A banca também cobra a versão com “Renda Secundária”, que é CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O perdão de uma dívida externa por um governo estrangeiro é registrado na conta capital.”</i> "
            "→ CERTO",
            "<i>“As remessas de imigrantes são registradas na conta de renda primária, como remuneração do "
            "trabalho.”</i> → ERRADO (troca de conceito: renda primária é salário de não migrante)",
        ])],
        "reescrita": ("As remessas de dinheiro de imigrantes no exterior para seus países de origem são "
                      "contabilizadas na " + hl("Conta de Renda Secundária") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Remessas são transferências correntes, em renda secundária (antigas transferências "
                            "unilaterais correntes); a conta capital registra transferências de capital e ativos "
                            "não financeiros não produzidos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 522", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (estrutura das transações correntes no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01288-1 (mesmo tema; lá a conta é a renda secundária)",
                    "duplicata: comentário de E2-L01735 fundido"],
    },
]
