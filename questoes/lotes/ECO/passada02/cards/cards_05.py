"""Cards do lote de redação 05 — ECO, passada 02 (nota 18: balanço de pagamentos — estrutura e lançamentos)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "est": "🏗️ Estrutura do BP (BPM6)",
    "lanc": "✍️ Lançamentos",
    "cn": "🔗 BP e contas nacionais",
}

CMD_LANC = "Julgue o item a seguir, relativo ao registro de transações no balanço de pagamentos."
CMD_EST = "Julgue o item a seguir, relativo à estrutura do balanço de pagamentos."
CMD_CACD24 = "Em relação ao balanço de pagamentos e à macroeconomia aberta, julgue (C ou E) o item a seguir."
CMD_CACD26 = ("Considerando as principais identidades macroeconômicas, julgue os itens seguintes, em relação ao sistema "
              "de contas nacionais.")
CMD_TAB15 = ("Com referência aos dados do balanço de pagamentos apresentados na tabela, julgue (C ou E) o item "
             "seguinte.")
CMD_BOZAN_TC = "Com base na estrutura das transações correntes no balanço de pagamentos, julgue as assertivas a seguir."
CMD_NAB_BP = "Em relação ao balanço de pagamentos, julgue (C ou E) os seguintes itens."
CMD_NAB_MACRO = "Em relação aos conceitos macroeconômicos, julgue (C ou E) os seguintes itens."

TAB15 = {
    "titulo": "Balanço de pagamentos (em US$ bilhões)",
    "cabecalho": ["Nº", "Transação", "US$ bilhões"],
    "linhas": [["1", "Investimentos para ampliação de empreendimento industrial", "18"],
               ["2", "Reinvestimento de lucros de uma multinacional no Brasil", "10"],
               ["3", "Aplicação de estrangeiros na aquisição de ações no mercado secundário", "11"],
               ["4", "Amortização de empréstimos externos", "7"],
               ["5", "Empréstimos externos obtidos", "22"],
               ["6", "Remessa de lucros por filiais de empresas estrangeiras", "15"],
               ["7", "Viagens internacionais de residentes no Brasil", "13"],
               ["8", "Pagamento de royalties e assistência técnica", "9"],
               ["9", "Fretes pagos a transportadores estrangeiros", "6"]],
    "fonte": "Tabela redesenhada com as rubricas recuperadas da questão original.",
}
AVISO_TAB15 = ("Tabela reconstruída: na fonte, a tabela era uma imagem, não preservada; uma linha de US$ 14 bilhões, "
               "de rótulo desconhecido, ficou de fora.")
ALERTA_TAB15 = ["texto_reconstruido: tabela da frente (image (306).png, comum a E1-0929, E1-0930 e E1-0932) "
                "reconstruída a partir dos valores e rótulos citados nos comentários do verso",
                "texto_parcial: falta uma linha de US$ 14 bilhões cujo rótulo não aparece nos comentários (somada "
                "por um dos comentários ao saldo de serviços); não altera o gabarito"]
FIG_TAB15 = {"ref": "image (306).png", "tipo_fonte": "TABELA", "lado": "frente",
             "acao": "transcrita_html (tabela aninhada reconstruída a partir dos comentários; imagem não preservada)"}

CARDS = [
    # ------------------------------------------------------------------ E1-0422
    {
        "id": "ECO-E1-0422-1", "fonte_ref": "E1-0422", "destino": "18", "subtema": H2["est"],
        "tipo": "ME", "banca": "Banca não identificada", "prova": "Senado/Consultor/2022", "ano": 2022,
        "cacd": False, "errei": False,
        "comando": "Leia o enunciado a seguir e assinale a opção correta.",
        "rotulo_item": "Questão",
        "assertiva": ("Considerando a 6ª edição do Manual de Balanço de Pagamentos e Posição de Investimento "
                      "Internacional do FMI (BPM6), em relação ao conceito de balança comercial, não é correto "
                      "afirmar que"
                      "</p><p>(A) os valores das exportações e importações são computados sem os custos de frete e "
                      "seguros de seu transporte até o destino.</p>"
                      "<p>(B) é possível detalhar a balança comercial por categorias econômicas.</p>"
                      "<p>(C) o seu saldo registra as transações de compra e venda de bens entre residentes e não "
                      "residentes.</p>"
                      "<p>(D) em relação à fonte primária do MDIC, o BACEN ajusta o saldo da balança comercial, "
                      "incorporando importações de energia elétrica sem cobertura cambial.</p>"
                      "<p>(E) o BACEN desconsidera do cômputo do saldo as exportações e importações fictas, mas "
                      "incorpora bens em triangulação (merchanting) e para processamento."),
        "gabarito": "E", "gabarito_origem": "fonte", "status": "normal",
        "anotada": ("❌ " + az("(A) os valores das exportações e importações são computados sem os custos de frete "
                               "e seguros de seu transporte até o destino.")
                    + "</p><p>❌ " + az("(B) é possível detalhar a balança comercial por categorias econômicas.")
                    + "</p><p>❌ " + az("(C) o seu saldo registra as transações de compra e venda de bens entre "
                                       "residentes e não residentes.")
                    + "</p><p>❌ " + az("(D) em relação à fonte primária do MDIC, o BACEN ajusta o saldo da balança "
                                       "comercial, incorporando importações de energia elétrica sem cobertura "
                                       "cambial.")
                    + "</p><p>✅ " + az("(E) o BACEN ") + vm("desconsidera") + az(" do cômputo do saldo as "
                                                                          "exportações e importações fictas, mas "
                                                                          "incorpora bens em triangulação "
                                                                          "(merchanting) ")
                    + vm("e para processamento") + az(".")),
        "poucas": ("Pede-se a <b>incorreta</b>: a (E) erra duas vezes — as operações " + azb("fictas")
                   + " <b>entram</b> no saldo, e os " + azb("bens para processamento") + " <b>saem</b> da balança "
                   "comercial (viram serviço de manufatura). Só o merchanting está certo."),
        "destrinchando": [
            "Critério-mestre do " + azb("BPM6") + ": bem é exportado ou importado quando há " + vd("mudança de "
            "propriedade econômica") + " entre residente e não residente — não quando cruza a fronteira. Todas "
            "as alternativas se resolvem por esse critério.",
            "(A) ❌ Não é o gabarito: afirmação verdadeira. Exportações e importações são valoradas " + vd("FOB")
            + " (na fronteira aduaneira do exportador, BPM6 §10.30); frete e seguro até o destino vão para a "
            "conta de " + azb("serviços") + " (transportes e seguros), não para o valor do bem (CIF).",
            "(B) ❌ Verdadeira: o BCB e a Secex detalham a balança por " + azb("grandes categorias econômicas")
            + " — bens de capital, intermediários, de consumo e combustíveis.",
            "(C) ❌ Verdadeira: é a definição de bens no BP — transações entre residentes e não residentes.",
            "(D) ❌ Verdadeira: o BCB parte dos registros alfandegários (Siscomex/MDIC) e amplia a cobertura; um "
            "dos ajustes é incluir a energia elétrica importada sem cobertura cambial, caso de " + rx("Itaipu")
            + " (a energia do Paraguai cedida ao Brasil abate custos da binacional e não passa pelo Siscomex).",
            "(E) ✅ É a incorreta. <b>Fictas</b>: há troca de propriedade sem o bem cruzar a fronteira (ex.: "
            "combustível comprado no exterior por companhias aéreas e de navegação brasileiras; bens do Repetro) "
            "— o BCB as <b>inclui</b>. <b>Merchanting</b>: o residente compra o bem num país e o revende a "
            "outro sem que ele entre no território; no BPM6 a compra é registrada como " + vd("exportação "
            "negativa") + " e a venda como exportação positiva (no BPM5, a margem ia para serviços) — essa parte "
            "está certa. <b>Bens para processamento</b>: atravessam a fronteira sem mudar de dono; o BPM6 os "
            "<b>exclui</b> da balança e registra só a tarifa em " + azb("serviços de manufatura sobre insumos "
            "físicos pertencentes a terceiros") + ".",
            vm("Regra-âncora: no BPM6, conta a troca de propriedade, não a travessia da fronteira."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A (E) empilha três ajustes e acerta só o do meio: "
                       "inverte o tratamento das fictas (entram, não saem) e enxerta os bens para processamento, "
                       "que o BPM6 tirou da balança. As alternativas A a D são literais do manual e da nota "
                       "metodológica do BCB; em “assinale a incorreta”, procure a que mistura várias rubricas."),
        "modulos": [("🧭 Panorama", [
            "Mudanças do BPM5 para o BPM6 em bens: merchanting sai de serviços e vai para bens; bens para "
            "processamento e reparos saem de bens e vão para serviços; o critério passa a ser a propriedade "
            "econômica.",
        ]), ("😈 Para dificultar", [
            "<i>“No BPM6, as operações de merchanting continuam registradas como serviços comerciais.”</i> → "
            "ERRADO (anacronismo: era a regra do BPM5)",
            "<i>“O valor dos serviços de montagem prestados por empresa residente sobre bem de não residente é "
            "registrado como exportação de serviços.”</i> → CERTO",
        ])],
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Gabarito do professor: letra E. Comentários (três) sobre FOB × CIF, categorias "
                             "econômicas, ajustes do BCB (energia de Itaipu, fictas, merchanting, encomendas "
                             "postais) e exclusão dos bens para processamento, com trechos do BPM6 e da nota "
                             "metodológica do BCB. Um deles diz que o BCB “considera do cômputo” as fictas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: FGV (concurso do Senado Federal de 2022 para Consultor Legislativo; a fonte "
                    "não nomeia a banca)"],
    },
    # ------------------------------------------------------------------ E1-0423
    {
        "id": "ECO-E1-0423-1", "fonte_ref": "E1-0423", "destino": "18", "subtema": H2["lanc"],
        "tipo": "EXERC", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 20", "ano": None,
        "cacd": False, "errei": False,
        "comando": ("As seguintes transações com o resto do mundo foram registradas por um país num determinado "
                    "ano. Com base nelas, resolva a questão."),
        "excerto": ("<ul><li>Exportações de mercadorias: 200</li><li>Importações de mercadorias: 250</li>"
                    "<li>Receitas, líquidas de despesas, de fretes e seguros: −10</li>"
                    "<li>Salários, lucros e juros recebidos: 50</li>"
                    "<li>Salários, lucros e juros pagos a não residentes: 90</li>"
                    "<li>Transferências de migrantes recebidas (líquidas): 5</li>"
                    "<li>Transferências de capital recebidas menos enviadas: 15</li>"
                    "<li>Investimento Direto no Exterior: 100</li><li>Investimento Direto no País: 200</li>"
                    "<li>Empréstimos concedidos: 10</li><li>Empréstimos recebidos: 40</li></ul>"),
        "rotulo_item": "Questão",
        "assertiva": ("Calcule: 1. o saldo da balança comercial e da balança de serviços; 2. o saldo da balança de "
                      "renda primária e da balança de renda secundária; 3. o saldo em transações correntes; 4. o "
                      "saldo da conta capital; 5. o saldo da conta ativos de reservas; 6. o saldo da conta "
                      "financeira."),
        "gabarito": "RESPOSTA", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("1. Balança comercial = 200 − 250 = −50; serviços = −10. 2. Renda primária = 50 − 90 = −40; "
                      "renda secundária = +5. 3. TC = −50 − 10 − 40 + 5 = −95. 4. Conta capital = +15. 5. Ativos "
                      "de reserva = +50 (as reservas aumentaram 50). 6. Conta financeira = −80 (o país tomou 80 "
                      "do exterior em termos líquidos)."),
        "poucas": ("TC (" + vd("−95") + ") + conta capital (" + vd("+15") + ") = " + vd("−80") + " = saldo da "
                   + azb("conta financeira") + ". Com ID líquido de −100 e empréstimos líquidos de −30, o que "
                   "falta para fechar −80 são " + vd("+50") + " de reservas."),
        "destrinchando": [
            "Transações correntes = bens + serviços + renda primária + renda secundária. Salários, lucros e "
            "juros são " + azb("renda primária") + " (remuneração de fatores); transferências de migrantes, "
            + azb("renda secundária") + ". TC = −50 − 10 − 40 + 5 = " + vd("−95") + ".",
            "Conta capital: transferências de capital e ativos não financeiros não produzidos → " + vd("+15")
            + ".",
            "Identidade do BPM6 (sem erros e omissões): " + vd("TC + KA = CF") + ". Logo CF = −95 + 15 = "
            + vd("−80") + ": o país é " + azb("tomador líquido") + " de recursos externos (necessidade de "
            "financiamento).",
            "No BPM6, CF = aquisição líquida de ativos − passivos incorridos líquidos. Ativos: IDE 100 + "
            "empréstimos concedidos 10 + ΔReservas. Passivos: IDP 200 + empréstimos recebidos 40. Então "
            "110 + ΔR − 240 = −80 → " + vd("ΔR = +50") + ".",
            "Leitura “à antiga” (fluxo de divisas): entram 200 (IDP) + 40 (empréstimos) e saem 100 (IDE) + 10 "
            "(concessões): conta financeira sem reservas = +130 de entrada; somada ao −80 das contas TC + KA, "
            "sobra " + vd("+50") + " de divisas, que o BC acumula em reservas. As duas leituras chegam ao mesmo "
            "número, com sinais de convenções diferentes.",
            vm("Regra-âncora: TC + conta capital = conta financeira (BPM6); reserva é o resíduo que fecha a "
               "conta."),
        ],
        "dissecando": (cz("[exercício aberto]") + " Em C/E, a banca transforma essa conta em itens como “o saldo "
                       "da conta financeira foi positivo” (ERRADO: −80 no BPM6) ou “as reservas caíram” (ERRADO: "
                       "subiram 50). A armadilha é misturar a convenção de sinais do BPM6 (ativo +, passivo +, "
                       "saldo = ativos − passivos) com a lógica antiga de entrada e saída de divisas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O país apresentou necessidade de financiamento externo de 80.”</i> → CERTO",
            "<i>“O saldo em transações correntes foi de −55, pois a renda primária não integra a conta "
            "corrente.”</i> → ERRADO (troca de conceito: renda primária integra TC)",
        ])],
        "tipo_erro": [], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("BC −50; BS −10; RP −40; RS 5; TC −95; CK 15; ativos de reserva 50 (pelo saldo do BP "
                             "em entradas e saídas de divisas); CF = 100 − 200 + 10 − 40 + 50 = −80 = CK + TC. A "
                             "explicação dos sinais de IDE e IDP é confusa (troca ativo e passivo)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem diz que o IDE “é um passivo nosso” e o IDP “um ativo "
                    "de um brasileiro no estrangeiro” — é o contrário; os números finais estão certos"],
    },
    # ------------------------------------------------------------------ E1-0424
    {
        "id": "ECO-E1-0424-1", "fonte_ref": "E1-0424", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_LANC,
        "rotulo_item": "Item",
        "assertiva": ("Uma venda à vista de mercadoria pelo país A ao país B implica um fluxo monetário na direção "
                      "oposta. No país A, registra-se o valor como crédito para o país na conta de Exportações e, "
                      "simultaneamente, um débito para sua conta Rendas de Capitais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma venda à vista de mercadoria pelo país A ao país B implica um fluxo monetário na "
                       "direção oposta. No país A, registra-se o valor como crédito para o país na conta de "
                       "Exportações e, simultaneamente, um débito para sua conta ") + vm("Rendas de Capitais")
                    + az(".")),
        "poucas": ("A contrapartida da exportação à vista é o " + azb("pagamento recebido") + " — aumento de "
                   "haveres no exterior (moeda e depósitos ou reservas), na " + azb("conta financeira")
                   + ". Rendas de capitais registram juros, lucros e dividendos."),
        "destrinchando": [
            "O BP usa " + azb("partidas dobradas") + ": cada transação gera um crédito e um débito de mesmo "
            "valor. Crédito = exportação de bens e serviços, renda recebida, redução de ativo ou aumento de "
            "passivo externo; débito = o inverso.",
            "Exportação à vista: crédito em <b>bens</b> (exportações) e débito na conta financeira — o "
            "exportador recebe divisas (aumento de depósitos no exterior, em “outros investimentos – ativos”) "
            "ou, se as vende ao Banco Central, as " + azb("reservas") + " aumentam.",
            "Exportação a prazo: o débito vai para “créditos comerciais” (ativo do exportador). Exportação sem "
            "pagamento, como doação: o débito vai para " + azb("renda secundária") + " (transferência).",
            "A conta de " + azb("rendas de capitais") + " (hoje " + azb("renda primária") + " — renda de "
            "investimento) só registra a <b>remuneração</b> dos ativos: juros, lucros, dividendos. O "
            "pagamento de uma mercadoria não remunera ativo nenhum.",
            vm("Regra-âncora: o pagamento de uma transação corrente fica na conta financeira, não em outra conta "
               "corrente."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira frase e o crédito em exportações estão certos; a "
                       "banca trocou só a conta da contrapartida, usando uma rubrica de nome “financeiro” (rendas "
                       "de capitais) que, na verdade, pertence às transações correntes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…e, simultaneamente, um débito em sua conta financeira, pelo aumento de haveres no "
            "exterior.”</i> → CERTO",
            "<i>“Se a mercadoria fosse doada, a contrapartida seria registrada na conta capital.”</i> → ERRADO "
            "(troca de conceito: doação de bem de consumo é renda secundária)",
        ])],
        "reescrita": ("Uma venda à vista de mercadoria pelo país A ao país B implica um fluxo monetário na direção "
                      "oposta. No país A, registra-se o valor como crédito para o país na conta de Exportações e, "
                      "simultaneamente, um débito para sua conta " + hl("financeira (aumento de haveres no "
                                                                         "exterior ou de reservas)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["simultaneamente"], "dificuldade": 1,
        "comentario_fonte": ("Crédito em bens (exportações) e débito em reservas internacionais ou meios de "
                             "pagamento; rendas de capitais são juros, lucros e dividendos."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0425
    {
        "id": "ECO-E1-0425-1", "fonte_ref": "E1-0425", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_LANC,
        "rotulo_item": "Item",
        "assertiva": ("Uma compra financiada de uma máquina fornecida por uma empresa estrangeira corresponde à "
                      "troca de um produto importado por um título de dívida."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma compra financiada de uma máquina fornecida por uma empresa estrangeira corresponde à "
                      "troca de um produto importado por um <u>título de dívida</u>."),
        "poucas": ("Na importação financiada, o país recebe o bem (" + vd("débito em bens") + ") e entrega uma "
                   "promessa de pagamento futuro — um " + azb("passivo externo") + " (" + vd("crédito na conta "
                   "financeira") + ")."),
        "destrinchando": [
            "Lançamento: débito em <b>importações de bens</b> (a máquina entra no país); crédito na "
            + azb("conta financeira") + " pelo aumento de passivos — " + azb("créditos comerciais") + " ou "
            "empréstimos, em “outros investimentos”. Se o fornecedor for a matriz do importador, a dívida é "
            + azb("intercompanhia") + " e vai para investimento direto.",
            "Nenhuma divisa sai na data da compra: por isso o resultado imediato não mexe nas reservas. A saída "
            "vem depois, quando se paga — o principal (amortização) na conta financeira, os juros na "
            + azb("renda primária") + ".",
            "Contraste com a importação à vista: débito em bens e crédito na conta financeira por <b>redução de "
            "ativo</b> (depósitos no exterior ou reservas), não por aumento de passivo.",
            "Leitura macroeconômica: a importação financiada é exatamente o que significa absorver "
            + azb("poupança externa") + " — o déficit corrente (a máquina) é coberto por endividamento.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Linguagem de livro-texto: “troca de um produto por um título” é "
                       "a forma clássica de descrever as duas pernas do lançamento. O risco é achar que, sem "
                       "pagamento à vista, não haveria registro no BP."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A importação financiada não é registrada no balanço de pagamentos até que o pagamento seja "
            "efetuado.”</i> → ERRADO (o registro é por competência, na troca de propriedade)",
            "<i>“Os juros pagos sobre esse financiamento serão registrados na conta financeira.”</i> → ERRADO "
            "(troca de conceito: juros são renda primária)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Importação financiada: débito em bens (importações) e crédito na conta financeira, "
                             "pela emissão de um passivo em troca do bem."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0430
    {
        "id": "ECO-E1-0430-1", "fonte_ref": "E1-0430", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_EST,
        "rotulo_item": "Item",
        "assertiva": "As transações no balanço de pagamentos podem ser autônomas ou compensatórias.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As transações no balanço de pagamentos podem ser <u>autônomas ou compensatórias</u>."),
        "poucas": ("É a classificação analítica clássica: " + azb("autônomas") + " ocorrem por decisão própria "
                   "dos agentes; " + azb("compensatórias") + " acontecem para fechar o saldo que as autônomas "
                   "deixam."),
        "destrinchando": [
            azb("Transações autônomas") + " (ex ante): exportações, importações, serviços, rendas, investimento "
            "direto, em carteira, empréstimos voluntários e créditos comerciais — motivadas por preço, lucro, "
            "juros ou câmbio, sem relação com o saldo do BP.",
            azb("Transações compensatórias") + " (ex post, de “regularização”): uso ou acúmulo de "
            + azb("reservas internacionais") + ", empréstimos de regularização (FMI) e atrasados comerciais. "
            "Existem porque o resultado das autônomas precisa ser financiado.",
            "O " + azb("resultado do balanço de pagamentos") + " na apresentação tradicional é justamente a "
            "soma das autônomas (TC + conta capital e financeira + erros e omissões); as compensatórias têm o "
            "mesmo valor com sinal trocado. Superávit → reservas sobem; déficit → reservas caem ou o país "
            "recorre ao FMI.",
            "No " + azb("BPM6") + ", a distinção não organiza mais as contas: os ativos de reserva estão dentro "
            "da conta financeira e o saldo da conta financeira é ativos − passivos. A ideia sobrevive na "
            "<b>apresentação analítica</b> (linha acima × abaixo da linha) e nas provas.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de definição, sem modulador perigoso (“podem ser”). Em itens "
                       "irmãos, a banca troca as funções: compensatório “movido por especulação” ou empréstimo "
                       "voluntário como “compensatório” → ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os empréstimos de regularização junto ao FMI são classificados como transações "
            "autônomas.”</i> → ERRADO (troca de conceito: são compensatórios)",
            "<i>“O resultado do balanço de pagamentos corresponde ao saldo das transações autônomas.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": ("Autônomas: decisão própria dos agentes (exportações, importações, investimentos, "
                             "empréstimos voluntários). Compensatórias: ajustam o balanço (reservas, empréstimos "
                             "de curto prazo para financiar déficits)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0431
    {
        "id": "ECO-E1-0431-1", "fonte_ref": "E1-0431", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_EST,
        "rotulo_item": "Item",
        "assertiva": ("Os erros e omissões no balanço de pagamentos referem-se a discrepâncias que surgem durante o "
                      "processo de contabilização das transações internacionais de um país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os erros e omissões no balanço de pagamentos referem-se a <u>discrepâncias</u> que surgem "
                      "durante o processo de contabilização das transações internacionais de um país."),
        "poucas": ("Em teoria, as partidas dobradas zeram o BP; na prática, cada perna vem de uma fonte "
                   "diferente. " + azb("Erros e omissões") + " é a rubrica residual que absorve essa "
                   "discrepância estatística."),
        "destrinchando": [
            "Identidade do BPM6: " + vd("TC + conta capital − conta financeira + erros e omissões = 0")
            + ". Erros e omissões = CF − (TC + KA): é calculado por <b>diferença</b>, não medido.",
            "Por que surge: crédito e débito de uma mesma transação são captados por fontes distintas (Siscomex "
            "para bens, contratos de câmbio, declarações de capitais, pesquisas), com diferenças de "
            "<b>momento</b> de registro, de <b>valoração</b> e de <b>cobertura</b> (subnotificação, "
            "contrabando, operações não declaradas).",
            "Erros e omissões grandes e persistentes, num mesmo sentido, costumam ser lidos como sinal de fluxos "
            "não captados — por exemplo, fuga de capitais não registrada.",
            "Não confundir com " + azb("ativos de reserva") + " (contrapartida financeira real das transações "
            "do BC) nem com o resultado do BP: erros e omissões são só o ajuste estatístico.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, sem modulador. A versão errada costuma dizer "
                       "que a rubrica registra transações “ilegais” ou “compensatórias”, ou que mede variação de "
                       "reservas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como o balanço de pagamentos segue o método das partidas dobradas, a rubrica erros e omissões "
            "é sempre nula.”</i> → ERRADO (modulador absoluto: as fontes estatísticas divergem)",
            "<i>“Erros e omissões são obtidos como resíduo, para que o balanço de pagamentos feche.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Rubrica que ajusta discrepâncias estatísticas por diferenças de registro, "
                             "subnotificação, atrasos ou falhas; garante que o balanço feche."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0782
    {
        "id": "ECO-E1-0782-1", "fonte_ref": "E1-0782", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("Quando as importações de um país superam suas exportações, diz-se que o país tem déficit em "
                      "conta-corrente; portanto, é correto concluir que, se um país compra mais dos estrangeiros "
                      "do que vende a estes, ele precisará financiar a diferença por meio da aquisição de "
                      "empréstimos externos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "alterado",
        "anotada": (az("Quando as importações de um país superam suas exportações, diz-se que o país tem déficit ")
                    + vm("em conta-corrente") + az("; ") + vm("portanto, é correto concluir")
                    + az(" que, se um país compra mais dos estrangeiros do que vende a estes, ele precisará "
                         "financiar a diferença por meio da aquisição de empréstimos externos.")),
        "poucas": ("Importar mais do que exportar é " + azb("déficit comercial") + ", não necessariamente "
                   "déficit em conta-corrente (há rendas e transferências); e um déficit corrente pode ser "
                   "coberto por " + azb("investimento direto, em carteira ou reservas") + ", não só por "
                   "empréstimos."),
        "condicionais": [("🏛️ Justificativa da banca", cz(
            "Gabarito preliminar CERTO, alterado para ERRADO: “A redação do item não pode ser considerada "
            "correta, uma vez que o resultado da conta-corrente do balanço de pagamentos engloba não apenas a "
            "balança comercial (diferença entre exportações e importações de bens e serviços), mas a balança "
            "de serviços e rendas.”"))],
        "destrinchando": [
            azb("Transações correntes") + " = bens + serviços + " + azb("renda primária") + " (juros, lucros, "
            "salários) + " + azb("renda secundária") + " (transferências). Um déficit em bens e serviços pode "
            "ser compensado por superávit de rendas — basta pensar num país que recebe muitas remessas de "
            "emigrantes ou muitos juros de ativos no exterior.",
            "Financiamento do déficit corrente: pela identidade " + vd("TC + KA = CF") + ", o que falta em TC "
            "é coberto pela conta capital e pela financeira — " + azb("IDP") + " (não residentes compram "
            "empresas e participações), " + azb("investimento em carteira") + " (ações e títulos), "
            "empréstimos e créditos comerciais, ou queda de " + azb("ativos de reserva") + ". Empréstimo é só "
            "uma das vias.",
            oc("Paulani e Braga") + " (<i>A Nova Contabilidade Social</i>) ilustram: o país pode ter déficit corrente e, "
            "ainda assim, aumentar reservas, se a entrada de investimento estrangeiro superar o déficit; se não, "
            "gasta reservas e, sem elas, pode chegar à moratória.",
            "Origem provável do gabarito preliminar: a frase é paráfrase de um trecho de manual de economia "
            "internacional (" + oc("Krugman e Obstfeld") + ") que usa “importar/exportar” em sentido amplo "
            "(todas as transações correntes) e “tomar emprestado” em sentido amplo (vender ativos ao exterior). "
            "Em linguagem técnica de BP, as duas palavras ficam estreitas demais.",
            vm("Regra-âncora: déficit comercial ≠ déficit em TC; e déficit em TC se financia pela conta "
               "financeira inteira, não só por empréstimos."),
        ],
        "dissecando": (cz("[troca de conceito · restrição indevida]") + " Duas falhas: chama de “conta-corrente” "
                       "o saldo comercial e reduz o financiamento a “empréstimos externos”. O “portanto, é "
                       "correto concluir” amarra uma conclusão necessária a uma premissa já imprecisa. 🔥 O CACD "
                       "2024 cobrou várias vezes a distinção balança comercial × transações correntes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um déficit em transações correntes pode ser financiado por ingressos de investimento "
            "estrangeiro direto.”</i> → CERTO",
            "<i>“Déficit na balança comercial implica, necessariamente, déficit em transações correntes.”</i> "
            "→ ERRADO (modulador absoluto: rendas e transferências podem compensar)",
        ])],
        "reescrita": ("Quando as importações de um país superam suas exportações, diz-se que o país tem déficit "
                      + hl("na balança comercial") + "; " + hl("não é correto concluir, porém,") + " que, se um "
                      "país compra mais dos estrangeiros do que vende a estes, ele precisará financiar a diferença "
                      + hl("exclusivamente") + " por meio da aquisição de empréstimos externos."),
        "tipo_erro": ["TROCA_CONCEITO", "RESTRICAO"], "moduladores": ["portanto", "precisará"],
        "dificuldade": 2,
        "comentario_fonte": ("“CERTO > ERRADO” com o motivo da alteração; vários comentários (Clipping, "
                             "professores, IA) sobre balança comercial × conta corrente e sobre formas de "
                             "financiar o déficit corrente; citação de Paulani e Braga; quadro da estrutura do BP "
                             "em imagem."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (269).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (estrutura do BP, imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0817-1 (CACD 2026, déficit em TC × déficit comercial)"],
    },
    # ------------------------------------------------------------------ E1-0783
    {
        "id": "ECO-E1-0783-1", "fonte_ref": "E1-0783", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": True,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("As transferências unilaterais líquidas não são consideradas parte da conta-corrente, visto "
                      "que, por sua natureza, elas não são resultado da compra e venda de nenhuma mercadoria, "
                      "serviço ou ativo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As transferências unilaterais líquidas ") + vm("não são consideradas")
                    + az(" parte da conta-corrente, ") + vm("visto que") + az(", por sua natureza, elas não são "
                                                                              "resultado da compra e venda de "
                                                                              "nenhuma mercadoria, serviço ou "
                                                                              "ativo.")),
        "poucas": ("As transferências unilaterais correntes formam a " + azb("renda secundária") + ", uma das "
                   "quatro subcontas das " + azb("transações correntes") + ". Não ter contrapartida é a "
                   "definição delas, não motivo de exclusão."),
        "destrinchando": [
            "Transações correntes (BPM6) = " + vd("bens + serviços + renda primária + renda secundária")
            + ". A renda secundária registra as " + azb("transferências correntes") + ": remessas pessoais de "
            "trabalhadores, doações e ajuda humanitária para consumo, contribuições a organismos internacionais, "
            "pensões, impostos pagos a outro país.",
            "Por que ficam na conta corrente: alteram a <b>renda disponível</b> do país — a renda nacional "
            "disponível bruta = RNB + transferências correntes líquidas do exterior. São fluxos que financiam "
            "consumo corrente, como a renda do trabalho.",
            "“Líquidas” = recebidas − enviadas. Num país de emigração (México, Filipinas, países da América "
            "Central), as remessas são enormes e podem compensar déficits comerciais.",
            "Contraste necessário: " + azb("transferências de capital") + " (perdão de dívida, doações para "
            "investimento) também não têm contrapartida, mas vão para a <b>conta capital</b>, porque afetam a "
            "riqueza, não a renda corrente.",
            vm("Regra-âncora: transferência corrente → renda secundária (TC); transferência de capital → conta "
               "capital."),
        ],
        "dissecando": (cz("[nexo indevido · contradição]") + " A justificativa (“não resultam de compra e "
                       "venda”) é verdadeira, mas foi usada como causa de uma exclusão que não existe. Pista: a "
                       "conta corrente não é só de compra e venda — renda primária e secundária também não "
                       "são trocas de mercadorias."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As remessas de trabalhadores emigrados para suas famílias são registradas na renda "
            "secundária.”</i> → CERTO",
            "<i>“O perdão de dívida externa concedido por um credor oficial é registrado na renda "
            "secundária.”</i> → ERRADO (troca de conceito: é transferência de capital, na conta capital)",
        ])],
        "reescrita": ("As transferências unilaterais líquidas " + hl("são consideradas") + " parte da "
                      "conta-corrente, " + hl("mas") + ", por sua natureza, elas não são resultado da compra e "
                      "venda de nenhuma mercadoria, serviço ou ativo."),
        "tipo_erro": ["NEXO_INDEVIDO", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Vários comentários concordes: transferências unilaterais são renda secundária e "
                             "integram a conta corrente; exemplos (remessas, doações, pensões); quadros da "
                             "estrutura do BP em imagem."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "41c9ffda-ec50-4fe0-b718-b85c018e22e6", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"},
                          {"ref": "image (268).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"},
                          {"ref": "image (280).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0784
    {
        "id": "ECO-E1-0784-1", "fonte_ref": "E1-0784", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("A equação Y = C + I + G + EX – IM mostra a identidade da renda nacional para uma economia "
                      "aberta, e uma análise desses agregados indica a importância da conta-corrente no "
                      "dimensionamento do empréstimo internacional."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("A equação Y = C + I + G + EX – IM mostra a ") + vm("identidade da renda nacional")
                    + az(" para uma economia aberta, e uma análise desses agregados indica a importância da ")
                    + vm("conta-corrente") + az(" no dimensionamento do empréstimo internacional.")),
        "poucas": ("A ideia é de manual (a conta-corrente mede o empréstimo internacional), mas a equação dada é a "
                   "do " + azb("produto") + " e contém só " + azb("exportações líquidas") + ", não a "
                   "conta-corrente inteira: duas leituras possíveis, item anulado (preliminar: CERTO)."),
        "condicionais": [("🏛️ Justificativa da banca", cz(
            "Gabarito preliminar CERTO, alterado para ANULADO: “O item possibilita mais de uma interpretação, "
            "o que prejudicou seu julgamento objetivo.”"))],
        "destrinchando": [
            "Y = C + I + G + (EX − IM) é a identidade do " + azb("PIB pela ótica da despesa") + ". A renda "
            "nacional (RNB) acrescenta a " + azb("renda líquida recebida do exterior") + ": RNB = PIB − RLEE.",
            "Da identidade sai " + vd("S − I = EX − IM") + " (com S = Y − C − G) — a forma de manual, em que "
            "exportações líquidas e conta-corrente se confundem porque o modelo ignora rendas e "
            "transferências.",
            "Com rendas, a versão correta é " + vd("TC = (EX − IM) − RLEE + transferências = (S − I) + (T − G)")
            + ": o saldo em transações correntes é o excesso de poupança doméstica sobre o investimento. "
            "Déficit em TC = " + azb("poupança externa") + " positiva = o país toma emprestado do resto do "
            "mundo em termos líquidos.",
            "Leitura que sustentava o CERTO: em " + oc("Krugman e Obstfeld") + ", a conta-corrente “mede o "
            "tamanho e a direção do empréstimo internacional”. Leitura que levava ao ERRADO: a equação dada não "
            "contém a conta-corrente (faltam rendas e transferências) e não é a identidade da renda nacional.",
            vm("Regra-âncora: Y = C + I + G + NX é o PIB; a conta-corrente exige somar rendas e "
               "transferências."),
        ],
        "dissecando": (cz("[outro: imprecisão conceitual que gerou duas leituras]") + " O item mistura vocabulário "
                       "de livro-texto (renda = produto; NX = conta-corrente) com o rigor de contas nacionais. Em "
                       "provas de contas nacionais, “renda nacional” e “conta-corrente” têm sentido técnico: "
                       "quando a banca os usa frouxamente, o item fica sujeito a recurso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A partir de Y = C + I + G + NX, obtém-se que as exportações líquidas igualam a diferença entre "
            "poupança nacional e investimento.”</i> → CERTO",
            "<i>“Um déficit em transações correntes indica que o país está concedendo empréstimos ao resto do "
            "mundo.”</i> → ERRADO (inversão: está tomando)",
        ])],
        "tipo_erro": ["OUTRO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("“CERTO > ANULADA” com o motivo oficial; comentários de professores (Bozan: correto "
                             "“mecanicamente”; Eliézer: impreciso) e de IA dando CERTO; dedução de "
                             "(EX − IM) − Rf = (S − I) + (T − G). Um comentário atribui a este item, por engano, "
                             "a justificativa de alteração de outro item da mesma prova."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: um dos comentários reproduz como motivo da anulação a justificativa de "
                    "alteração do item sobre balança comercial × conta-corrente; usada a justificativa própria "
                    "deste item (“mais de uma interpretação”)"],
    },
    # ------------------------------------------------------------------ E1-0785
    {
        "id": "ECO-E1-0785-1", "fonte_ref": "E1-0785", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": CMD_CACD24,
        "rotulo_item": "Item",
        "assertiva": ("A conta financeira do balanço de pagamentos, que registra todas as compras e vendas "
                      "internacionais de ativos financeiros, direitos sobre recursos naturais, marcas, logotipos e "
                      "domínios, contribui para a análise do movimento de capitais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A conta financeira do balanço de pagamentos, que registra todas as compras e vendas "
                       "internacionais de ativos financeiros, ") + vm("direitos sobre recursos naturais, marcas, "
                                                                      "logotipos e domínios")
                    + az(", contribui para a análise do movimento de capitais.")),
        "poucas": ("Direitos sobre recursos naturais, marcas, logotipos e domínios são " + azb("ativos não "
                   "financeiros não produzidos") + ": suas compras e vendas vão para a " + azb("conta capital")
                   + ", não para a financeira."),
        "destrinchando": [
            "A " + azb("conta capital") + " (BPM6) tem duas partes: (1) " + azb("transferências de capital")
            + " — perdão de dívidas, doações para investimento; (2) aquisição e alienação de " + azb("ativos "
            "não financeiros não produzidos") + " — terras e direitos sobre recursos naturais (concessões de "
            "exploração, licenças de pesca), contratos e licenças negociáveis e " + azb("ativos de marketing")
            + " (marcas, logotipos, nomes de domínio).",
            "A " + azb("conta financeira") + " registra ativos e passivos <b>financeiros</b>: investimento "
            "direto, investimento em carteira, derivativos, outros investimentos (empréstimos, depósitos, "
            "créditos comerciais) e ativos de reserva. É ela que mostra o “movimento de capitais” — essa parte "
            "do item está certa.",
            "Cuidado com " + azb("patentes e direitos autorais") + ": no BPM6 são resultado de P&amp;D, portanto "
            "ativos <b>produzidos</b>; licenças de uso entram em serviços (encargos pelo uso de propriedade "
            "intelectual) e a venda definitiva, em serviços de pesquisa e desenvolvimento. No BPM5, iam para a "
            "conta capital — muitos materiais ainda repetem isso.",
            "Por que separar: comprar uma marca ou uma concessão muda a riqueza real do país, mas não cria "
            "direito financeiro contra não residente. A contrapartida financeira (o pagamento) é que vai para a "
            "conta financeira.",
            vm("Regra-âncora: não financeiro e não produzido (terra, recurso natural, marca, domínio) → conta "
               "capital."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A moldura é verdadeira (a conta financeira "
                       "registra ativos financeiros e serve à análise de fluxos de capital); o erro foi enxertado "
                       "na lista, com itens da conta capital. Pista: “marcas, logotipos e domínios” não são "
                       "ativos financeiros."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A conta capital registra a aquisição e a alienação de ativos não financeiros não produzidos, "
            "como direitos sobre recursos naturais e marcas.”</i> → CERTO",
            "<i>“No BPM6, a venda definitiva de uma patente resultante de pesquisa é registrada na conta "
            "capital.”</i> → ERRADO (anacronismo: regra do BPM5; hoje é serviço)",
        ])],
        "reescrita": ("A conta financeira do balanço de pagamentos, que registra todas as compras e vendas "
                      "internacionais de ativos financeiros<s>, direitos sobre recursos naturais, marcas, logotipos "
                      "e domínios</s>, contribui para a análise do movimento de capitais" + hl("; as de direitos "
                      "sobre recursos naturais, marcas, logotipos e domínios vão para a conta capital") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["todas"], "dificuldade": 2,
        "comentario_fonte": ("Comentários concordes: esses itens são ativos não financeiros não produzidos, da "
                             "conta capital; quadros da estrutura do BP em imagem. Alguns incluem patentes e "
                             "direitos autorais na conta capital."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "image (281).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"},
                          {"ref": "41c9ffda-ec50-4fe0-b718-b85c018e22e6", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"},
                          {"ref": "image (267).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": ["qualidade_fonte: comentários de origem põem patentes e direitos autorais na conta capital "
                    "(regra do BPM5); no BPM6 são ativos produzidos, registrados em serviços"],
    },
    # ------------------------------------------------------------------ E1-0796
    {
        "id": "ECO-E1-0796-1", "fonte_ref": "E1-0796", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": ("Em relação à macroeconomia internacional dos fluxos de bens e de capital, julgue (C ou E) o "
                    "item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Os recursos estrangeiros que entram em um país para aplicações no mercado financeiro não são "
                      "contabilizados no fluxo de capitais, por não constituírem formação bruta de capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Os recursos estrangeiros que entram em um país para aplicações no mercado financeiro ")
                    + vm("não são contabilizados no fluxo de capitais, por não constituírem")
                    + az(" formação bruta de capital.")),
        "poucas": ("Aplicação estrangeira em ações e títulos é " + azb("investimento em carteira") + " (passivo, "
                   "na conta financeira) — é fluxo de capital. " + azb("Formação bruta de capital") + " é "
                   "conceito das contas nacionais e não é critério de registro no BP."),
        "destrinchando": [
            "O BP registra toda transação entre residentes e não residentes. Quando um estrangeiro compra ações "
            "na bolsa ou títulos públicos brasileiros, há " + vd("aumento de passivo externo") + " em "
            + azb("investimento em carteira") + " (passivos), dentro da " + azb("conta financeira") + ".",
            azb("Formação bruta de capital fixo") + " (máquinas, construções, equipamentos) é um componente da "
            "demanda no PIB. Comprar ação no mercado secundário só troca a titularidade de um ativo existente: "
            "não há FBCF, mas há fluxo financeiro com o exterior.",
            "Nem o " + azb("investimento direto") + " é sinônimo de FBCF: a compra de uma empresa já existente "
            "(fusão ou aquisição) é ID na conta financeira sem nenhuma máquina nova.",
            "Diferença ID × carteira: no ID, o investidor tem " + vd("10% ou mais") + " do poder de voto "
            "(influência duradoura na gestão); abaixo disso, ações são carteira. Carteira tende a ser mais "
            "volátil (" + azb("hot money") + "), daí o peso nas análises de vulnerabilidade externa.",
            vm("Regra-âncora: o BP registra fluxos financeiros pelo que são (ativos e passivos), não pelo que "
               "financiam."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O item importa um critério das contas "
                       "nacionais (FBCF) para decidir o registro no BP. O “por não constituírem” cria uma causa "
                       "falsa a partir de um fato verdadeiro (aplicação financeira não é FBCF)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A aquisição, por não residentes, de títulos públicos brasileiros é registrada como passivo em "
            "investimento em carteira.”</i> → CERTO",
            "<i>“Só os ingressos de capital destinados à formação bruta de capital fixo são registrados como "
            "investimento direto.”</i> → ERRADO (restrição indevida: aquisição de empresa existente também é "
            "ID)",
        ])],
        "reescrita": ("Os recursos estrangeiros que entram em um país para aplicações no mercado financeiro "
                      + hl("são contabilizados no fluxo de capitais (investimento em carteira, na conta "
                           "financeira), embora não constituam") + " formação bruta de capital."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentários concordes: aplicações financeiras de estrangeiros são investimento em "
                             "carteira (passivos) na conta financeira, mesmo sem FBCF; um professor nota que "
                             "“fluxo de capitais” não é rubrica formal. Quadros em imagem."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "41c9ffda-ec50-4fe0-b718-b85c018e22e6", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"},
                          {"ref": "image (278).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0817
    {
        "id": "ECO-E1-0817-1", "fonte_ref": "E1-0817", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": CMD_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("Se um país apresenta déficit em transações correntes, isso implica necessariamente que sua "
                      "balança comercial também está em déficit."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se um país apresenta déficit em transações correntes, ") + vm("isso implica "
                                                                                     "necessariamente")
                    + az(" que sua balança comercial também está em déficit.")),
        "poucas": ("TC = " + vd("bens + serviços + renda primária + renda secundária") + ". O déficit pode vir "
                   "de serviços e rendas com a balança comercial " + azb("superavitária") + " — é o caso típico "
                   "do " + rx("Brasil") + "."),
        "destrinchando": [
            "Como TC é soma de quatro saldos, o sinal de uma parcela não decide o sinal do total. Exemplo: bens "
            "+50, serviços −30, renda primária −60, renda secundária +5 → TC = " + vd("−35") + " com superávit "
            "comercial.",
            rx("Brasil") + ": há anos combina " + azb("superávit comercial") + " expressivo (commodities) com "
            + azb("déficit em transações correntes") + ", porque os déficits de serviços (viagens, fretes, "
            "aluguel de equipamentos, propriedade intelectual) e de renda primária (lucros, dividendos e juros "
            "pagos a não residentes) superam o saldo de bens ⏳ (out/2026).",
            "O inverso também ocorre: déficit comercial com superávit corrente, em países que recebem muita "
            "renda do exterior (grandes detentores de ativos externos) ou muitas remessas de emigrantes.",
            "Ligação com contas nacionais: TC = (S − I) + (T − G). O déficit corrente diz que o país "
            + azb("absorve poupança externa") + "; não diz em qual subconta o “buraco” aparece.",
            vm("Regra-âncora: déficit em TC não implica déficit comercial, nem o contrário."),
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " O “necessariamente” transforma uma "
                       "possibilidade em implicação lógica. 🔥 O CACD cobrou a mesma distinção em 2024 (gabarito "
                       "alterado de CERTO para ERRADO num item que chamava déficit comercial de déficit em "
                       "conta-corrente)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um país pode apresentar superávit na balança comercial e, simultaneamente, déficit em "
            "transações correntes.”</i> → CERTO",
            "<i>“Déficit na renda primária implica necessariamente déficit em transações correntes.”</i> → "
            "ERRADO (modulador absoluto: bens e serviços podem compensar)",
        ])],
        "reescrita": ("Se um país apresenta déficit em transações correntes, " + hl("isso não implica "
                                                                                     "necessariamente")
                      + " que sua balança comercial também está em déficit."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["necessariamente"], "dificuldade": 1,
        "comentario_fonte": "Só o gabarito (ERRADO), sem comentário.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0782-1 (CACD 2024, déficit comercial × déficit em conta-corrente)"],
    },
    # ------------------------------------------------------------------ E1-0818
    {
        "id": "ECO-E1-0818-1", "fonte_ref": "E1-0818", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True,
        "errei": False,
        "comando": CMD_CACD26,
        "rotulo_item": "Item",
        "assertiva": ("Se o país possui poupança externa positiva, isso significa que há superávit no saldo da "
                      "conta de transações correntes do balanço de pagamentos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o país possui poupança externa positiva, isso significa que há ") + vm("superávit")
                    + az(" no saldo da conta de transações correntes do balanço de pagamentos.")),
        "poucas": (vd("Poupança externa = −TC") + ". Poupança externa positiva = o resto do mundo financia o "
                   "país = " + azb("déficit") + " em transações correntes."),
        "destrinchando": [
            "Identidade macroeconômica em economia aberta: " + vd("I = S<sub>privada</sub> + "
            "S<sub>governo</sub> + S<sub>externa</sub>") + ". A " + azb("poupança externa") + " é a parte do "
            "investimento doméstico financiada por não residentes.",
            "Como S<sub>externa</sub> = −TC: déficit em TC de 50 → poupança externa de +50 (o país absorve "
            "recursos reais do exterior e se endivida ou vende ativos); superávit em TC → poupança externa "
            "<b>negativa</b> (o país exporta poupança e acumula ativos externos).",
            "Outra forma de ver: TC = Y − A (renda menos absorção). Quem gasta mais do que produz tem TC < 0 e "
            "precisa de recursos de fora.",
            "Exemplos: a " + azb("China") + " e a " + azb("Alemanha") + ", com superávits correntes "
            "persistentes, fornecem poupança ao resto do mundo; os " + azb("EUA") + ", com déficits "
            "persistentes, absorvem poupança externa. O " + rx("Brasil") + " costuma ser absorvedor "
            "(déficit em TC).",
            vm("Regra-âncora: S externa > 0 ⇔ TC < 0."),
        ],
        "dissecando": (cz("[inversão]") + " O item troca o sinal da identidade. A pegadinha está na palavra "
                       "“positiva”, que parece combinar com “superávit”. 🔥 A banca repete esse item com a "
                       "redação invertida (“superávit em TC indica poupança externa”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um superávit em transações correntes corresponde a poupança externa negativa.”</i> → CERTO",
            "<i>“Com orçamento público equilibrado, poupança externa positiva implica investimento superior à "
            "poupança privada.”</i> → CERTO",
        ])],
        "reescrita": ("Se o país possui poupança externa positiva, isso significa que há " + hl("déficit")
                      + " no saldo da conta de transações correntes do balanço de pagamentos."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Só o gabarito (ERRADO), sem comentário.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00100-1 (Bozan, superávit em TC × poupança externa)"],
    },
    # ------------------------------------------------------------------ E1-0929
    {
        "id": "ECO-E1-0929-1", "fonte_ref": "E1-0929", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_TAB15,
        "aviso_frente": AVISO_TAB15,
        "excerto_tabela": TAB15,
        "rotulo_item": "Item",
        "assertiva": "O balanço de serviços apresentou saldo negativo de US$ 43 bilhões.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O balanço de serviços apresentou saldo negativo de US$ ") + vm("43") + az(" bilhões."),
        "poucas": ("Serviços são só viagens (13), royalties e assistência técnica (9) e fretes (6): saldo de "
                   + vd("−28") + ". O 43 sai de quem soma a " + azb("remessa de lucros") + " (15), que é renda "
                   "primária."),
        "destrinchando": [
            azb("Balança de serviços") + " (BPM5 e BPM6): transportes (fretes, passagens), viagens, seguros, "
            "serviços financeiros, telecomunicações e informática, " + azb("propriedade intelectual")
            + " (royalties e licenças), aluguel de equipamentos, serviços técnicos e profissionais, serviços "
            "governamentais.",
            "Na tabela, são serviços: viagens de residentes ao exterior (" + vd("−13") + "), royalties e "
            "assistência técnica (" + vd("−9") + "), fretes pagos a estrangeiros (" + vd("−6") + "). Total: "
            + vd("−28") + ".",
            "A " + azb("remessa de lucros") + " de filiais estrangeiras remunera o capital: é " + azb("renda "
            "primária") + " (renda de investimento direto). 28 + 15 = 43 é exatamente o valor do item.",
            "Fonte da confusão: na metodologia brasileira antiga, rendas eram “serviços fatores” e ficavam no "
            "mesmo bloco que os “serviços não fatores”. Desde a adoção do BPM5 (2001) e, depois, do BPM6 (2015), "
            "renda primária é subconta própria.",
            "As linhas de capital (investimentos, reinvestimento, ações, amortizações, empréstimos) vão para a "
            "conta financeira e não entram nessa conta.",
            vm("Regra-âncora: serviço = não fator; lucros, juros e salários = renda primária."),
        ],
        "dissecando": (cz("[dado alterado · troca de conceito]") + " O número foi fabricado para quem inclui uma "
                       "renda nos serviços. Em tabelas de BP, a banca sempre põe ao menos uma linha de renda "
                       "“disfarçada” entre os serviços."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A conta de serviços apresentou déficit de US$ 28 bilhões.”</i> → CERTO",
            "<i>“O reinvestimento de lucros não afeta o saldo em transações correntes.”</i> → ERRADO (é débito "
            "na renda primária, com crédito na conta financeira)",
        ])],
        "reescrita": "O balanço de serviços apresentou saldo negativo de US$ " + hl("28") + " bilhões.",
        "tipo_erro": ["DADO_ALTERADO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Dois cálculos divergentes: um soma as “quatro últimas linhas” mais a remessa de lucros "
                             "(−57, metodologia antiga de serviços fatores e não fatores); outros somam só viagens, "
                             "royalties e fretes (−28). Definição de serviços do BCB."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [FIG_TAB15,
                          {"ref": "image (308).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada)"},
                          {"ref": "image (305).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada)"}],
        "alertas": ALERTA_TAB15 + [
            "qualidade_fonte: um comentário de origem soma rendas aos serviços (−57); prevaleceu o critério "
            "BPM5/BPM6 (−28), que é o dos demais comentários"],
    },
    # ------------------------------------------------------------------ E1-0930
    {
        "id": "ECO-E1-0930-1", "fonte_ref": "E1-0930", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_TAB15,
        "aviso_frente": AVISO_TAB15,
        "excerto_tabela": TAB15,
        "rotulo_item": "Item",
        "assertiva": ("Ocorrendo saldo negativo no balanço de pagamentos, ele poderá ser financiado mediante "
                      "redução das reservas internacionais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ocorrendo saldo negativo no balanço de pagamentos, ele <u>poderá</u> ser financiado "
                      "mediante redução das reservas internacionais."),
        "poucas": ("Déficit no " + azb("resultado do BP") + " (transações autônomas) é coberto por transações "
                   "compensatórias: " + vd("queda de reservas") + " ou empréstimos de regularização (FMI)."),
        "destrinchando": [
            "Na apresentação tradicional: resultado do BP = TC + conta capital e financeira (sem reservas) + "
            "erros e omissões. Se negativo, faltaram divisas: alguém precisa supri-las.",
            "Quem supre é a autoridade monetária: vende " + azb("reservas internacionais") + " ao mercado de "
            "câmbio (a variação de reservas tem o mesmo valor do resultado, com sinal trocado) ou contrai "
            + azb("empréstimos de regularização") + " (FMI, acordos bilaterais).",
            "No " + azb("BPM6") + ", reservas são uma subconta da " + azb("conta financeira") + " (“ativos de "
            "reserva”): uma redução de reservas aparece como aquisição líquida <b>negativa</b> de ativos, que "
            "fecha a identidade TC + KA = CF. O raciocínio é o mesmo.",
            "Limites: reservas são finitas e servem de seguro; queimá-las para sustentar déficits persistentes, "
            "sobretudo com câmbio fixo, prepara crises cambiais (" + rx("Brasil") + " em 1998–1999, Argentina "
            "em vários episódios). Com câmbio flutuante, a desvalorização faz parte do ajuste.",
            "A tabela da questão não importa para este item: ele cobra só o mecanismo.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “poderá” salva o item: reservas são <b>uma</b> das formas "
                       "de financiar o déficit. A versão errada usa “necessariamente” ou “exclusivamente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ocorrendo saldo negativo no balanço de pagamentos, ele será necessariamente financiado pela "
            "redução das reservas internacionais.”</i> → ERRADO (modulador absoluto: há também empréstimos de "
            "regularização)",
            "<i>“Superávit no balanço de pagamentos corresponde a aumento das reservas internacionais.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["poderá"], "dificuldade": 1,
        "comentario_fonte": ("Vários comentários concordes (CERTO): déficit do BP coberto por reservas ou "
                             "empréstimos de regularização; estrutura do BP; adaptação ao BPM6; longas explicações "
                             "de IA sobre venda de reservas pelo BCB."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_TAB15,
                          {"ref": "image (307).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada)"}],
        "alertas": ALERTA_TAB15,
    },
    # ------------------------------------------------------------------ E1-0932
    {
        "id": "ECO-E1-0932-1", "fonte_ref": "E1-0932", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": True,
        "comando": CMD_TAB15,
        "aviso_frente": AVISO_TAB15,
        "excerto_tabela": TAB15,
        "rotulo_item": "Item",
        "assertiva": "O movimento de capitais autônomos foi positivo e igual a US$ 39 bilhões.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O movimento de capitais autônomos foi positivo e igual a US$ ") + vm("39") + az(" bilhões."),
        "poucas": ("Capitais autônomos = 18 + 10 + 11 − 7 + 22 = " + vd("+54") + ". O 39 aparece para quem "
                   "desconta a " + azb("remessa de lucros") + " (15), que é transação corrente (renda primária)."),
        "destrinchando": [
            "Na classificação tradicional, o " + azb("movimento de capitais autônomos") + " é a conta de capitais "
            "(hoje, conta financeira sem reservas): investimentos, reinvestimentos, carteira, empréstimos e "
            "amortizações.",
            "Entradas (crédito): investimento para ampliar empreendimento industrial (" + vd("+18") + "), "
            "reinvestimento de lucros (" + vd("+10") + "), compra de ações por estrangeiros (" + vd("+11")
            + "), empréstimos obtidos (" + vd("+22") + "). Saída: amortização (" + vd("−7") + "). Soma: "
            + vd("+54") + ".",
            azb("Reinvestimento de lucros") + ": não há divisa circulando, mas há dois lançamentos — débito em "
            "renda primária (lucro que “sai”) e crédito em investimento direto (lucro que “volta” como "
            "capital). Por isso entra na conta de capitais.",
            azb("Remessa de lucros") + " e juros remuneram o capital: vão para a " + azb("renda primária")
            + ", nas transações correntes. Amortização é devolução de principal: conta financeira.",
            "No BPM6, o mesmo conjunto aparece como " + vd("passivos incorridos líquidos de 54") + " — e, como "
            "o saldo da conta financeira é ativos − passivos, o saldo seria −54 (captação líquida).",
            vm("Regra-âncora: principal → conta financeira; juros e lucros → renda primária."),
        ],
        "dissecando": (cz("[dado alterado · troca de conceito]") + " O 39 = 54 − 15 é a resposta de quem joga a "
                       "remessa de lucros na conta de capitais. O sentido (“positivo”) está certo; só o valor "
                       "foi alterado, o que obriga a fazer a conta inteira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O movimento de capitais autônomos foi positivo e igual a US$ 54 bilhões.”</i> → CERTO",
            "<i>“O reinvestimento de lucros, por não envolver entrada de divisas, não é registrado no balanço "
            "de pagamentos.”</i> → ERRADO (é registrado em renda primária e investimento direto)",
        ])],
        "reescrita": "O movimento de capitais autônomos foi positivo e igual a US$ " + hl("54") + " bilhões.",
        "tipo_erro": ["DADO_ALTERADO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Comentários divergentes: um diz que autônomos são só aplicações de curto prazo (11); "
                             "outro, que são 18 + 11 = 29; dois professores calculam 18 + 10 + 11 − 7 + 22 = 54 e "
                             "explicam a armadilha da remessa de lucros; lançamentos do reinvestimento."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [FIG_TAB15,
                          {"ref": "21e8a23d-51dd-4e26-9fb8-b3622319a221", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada; conteúdo absorvido no 📖)"},
                          {"ref": "image (311).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada)"},
                          {"ref": "image (312).png", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (imagem não preservada)"}],
        "alertas": ALERTA_TAB15 + [
            "qualidade_fonte: dois comentários de origem chegam a 11 e a 29; prevaleceu o cálculo de 54, "
            "coerente com a classificação das contas"],
    },
    # ------------------------------------------------------------------ E1-0939
    {
        "id": "ECO-E1-0939-1", "fonte_ref": "E1-0939", "destino": "18", "subtema": H2["lanc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": False,
        "comando": CMD_LANC,
        "rotulo_item": "Item",
        "assertiva": ("Considere que uma empresa mineradora brasileira compre empresa da área de mineração na "
                      "Tailândia. Nessa situação, a transação deve ser registrada na conta capital da CCF (conta "
                      "capital e financeira) do balanço de pagamentos brasileiro."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considere que uma empresa mineradora brasileira compre empresa da área de mineração na "
                       "Tailândia. Nessa situação, a transação deve ser registrada na ") + vm("conta capital")
                    + az(" da CCF (conta capital e financeira) do balanço de pagamentos brasileiro.")),
        "poucas": ("Comprar uma empresa no exterior é adquirir " + azb("participação no capital") + " — "
                   + azb("investimento direto no exterior") + ", na " + azb("conta financeira") + ". A conta "
                   "capital é para transferências de capital e ativos não financeiros não produzidos."),
        "destrinchando": [
            "Na estrutura do BPM5 (usada no Brasil até 2015), a CCF tinha dois blocos: " + azb("conta capital")
            + " (transferências de capital e ativos não financeiros não produzidos) e " + azb("conta "
            "financeira") + " (investimento direto, carteira, derivativos, outros investimentos). No BPM6, são "
            "duas contas separadas, com a mesma divisão de conteúdo.",
            "A aquisição de uma empresa estrangeira por residente, com controle ou influência relevante "
            "(" + vd("≥ 10% do capital votante") + "), é " + azb("investimento direto no exterior") + ", "
            "participação no capital. Contrapartida: saída de divisas (redução de depósitos no exterior ou "
            "aumento de passivos, se financiada).",
            "Convenção de sinais: na lógica antiga, débito (saída de capital); no BPM6, " + vd("+") + " em "
            "“aquisição líquida de ativos” — o estoque de ativos externos do Brasil aumenta.",
            "Os lucros que essa filial tailandesa gerar e remeter à matriz entrarão como crédito em "
            + azb("renda primária") + " (transações correntes).",
            "Iria para a conta capital, por exemplo, a compra de um <b>direito de exploração mineral</b> "
            "isolado (concessão, ativo não produzido) — não a compra da empresa que o detém.",
        ],
        "dissecando": (cz("[troca de conceito]") + " A banca usa o nome “conta capital” para atrair quem associa "
                       "“capital” a investimento. Pista: comprar uma empresa é comprar ações (ativo financeiro)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a transação deve ser registrada como investimento direto no exterior, na conta financeira do "
            "balanço de pagamentos brasileiro.”</i> → CERTO",
            "<i>“Se a mineradora comprasse apenas 5% das ações da empresa tailandesa, sem influência na gestão, "
            "a operação seria investimento direto.”</i> → ERRADO (abaixo de 10%: investimento em carteira)",
        ])],
        "reescrita": ("Considere que uma empresa mineradora brasileira compre empresa da área de mineração na "
                      "Tailândia. Nessa situação, a transação deve ser registrada na " + hl("conta financeira, "
                      "como investimento direto no exterior,") + " da CCF (conta capital e financeira) do balanço "
                      "de pagamentos brasileiro."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": ("Registro como investimento direto de empresas brasileiras no exterior, na conta "
                             "financeira, com débito por saída de divisas; não na conta capital."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0977
    {
        "id": "ECO-E1-0977-1", "fonte_ref": "E1-0977", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo às relações entre balanço de pagamentos e contas nacionais.",
        "rotulo_item": "Item",
        "assertiva": ("Sendo a conta de capital igual a investimento menos poupança, é possível avaliar o impacto "
                      "das políticas econômicas nos fluxos internacionais pelo seu impacto nos investimentos e na "
                      "poupança."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("Sendo a ") + vm("conta de capital igual a investimento menos poupança") + az(", é possível "
                    "avaliar o impacto das políticas econômicas nos fluxos internacionais pelo seu impacto nos "
                    "investimentos e na poupança.")),
        "poucas": ("A identidade exata é " + vd("I − S = −TC") + " (poupança externa). Ela só vale para a “conta "
                   "de capital” se esta for entendida como toda a conta capital e financeira, sem reservas — "
                   "ambiguidade que derruba o item."),
        "condicionais": [("⚠️ Gabarito contestável", (
            "Anulação (gabarito preliminar não preservado na fonte). Motivo provável: “conta de capital” tem "
            "dois sentidos. No sentido técnico do BPM5/BPM6 (transferências de capital e ativos não financeiros "
            "não produzidos), ela não é igual a I − S — o item seria " + vd("ERRADO") + ". No sentido de livro-"
            "texto (conta de capitais = entradas líquidas de capital que financiam a conta corrente), "
            "I − S = −TC = saldo da conta de capitais, e o item seria " + vd("CERTO") + "."))],
        "destrinchando": [
            "Da identidade da renda: (S − I) + (T − G) = TC. Agregando o governo na poupança doméstica "
            "(S<sub>dom</sub> = S<sub>privada</sub> + T − G): " + vd("I − S<sub>dom</sub> = −TC = "
            "S<sub>externa</sub>") + ".",
            "Pelo BP, TC + KA = CF (BPM6): o déficit corrente é coberto por entrada líquida de capitais (conta "
            "capital + passivos financeiros − ativos financeiros, incluídas as reservas). Em modelo sem reservas "
            "nem conta capital estrita, “entrada líquida de capitais” = I − S.",
            "A segunda parte do item é a " + azb("abordagem poupança-investimento") + " da conta corrente: "
            "políticas que reduzem a poupança (déficit fiscal, por exemplo) ou elevam o investimento tendem a "
            "piorar a conta corrente e a aumentar a entrada de capitais — a lógica dos " + azb("déficits "
            "gêmeos") + ".",
            "Cautela que o comentário da fonte acrescenta: a identidade é contábil, não causal; entrada de "
            "capital não vira necessariamente investimento — pode financiar consumo ou compra de ativos já "
            "existentes.",
            vm("Regra-âncora: I − S = −TC; chame de “conta de capital” só o que o enunciado define assim."),
        ],
        "dissecando": (cz("[outro: termo técnico com dois sentidos]") + " O item usa “conta de capital” no sentido "
                       "amplo dos livros-texto, enquanto a classificação do BP dá ao termo sentido estrito. Quando "
                       "o enunciado não define a conta, desconfie: é ali que mora a anulação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O excesso de investimento sobre a poupança doméstica corresponde ao déficit em transações "
            "correntes.”</i> → CERTO",
            "<i>“No BPM6, o saldo da conta capital corresponde à diferença entre investimento e poupança "
            "domésticos.”</i> → ERRADO (troca de conceito: I − S = −TC)",
        ])],
        "tipo_erro": ["OUTRO"], "moduladores": ["é possível"], "dificuldade": 2,
        "comentario_fonte": ("“Anulada”; explica que o correto seria igualar I − S ao déficit em transações "
                             "correntes (I − S = M − X) e que entrada de capitais não implica aumento de "
                             "investimento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00099
    {
        "id": "ECO-E2-L00099-1", "fonte_ref": "E2-L00099", "destino": "18", "subtema": H2["est"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_TC,
        "rotulo_item": "Item",
        "assertiva": ("Transações correntes são interações entre residentes e não-residentes que incluem fluxos "
                      "como exportação e importação de bens e serviços, fatores e não fatores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Transações correntes são interações entre residentes e não-residentes que incluem fluxos "
                       "como exportação e importação de bens e serviços") + vm(", fatores e não fatores")
                    + az(".")),
        "poucas": ("Pelo gabarito da fonte, transações correntes teriam só serviços " + azb("não fatores")
                   + ". Mas a renda primária — os antigos " + azb("serviços fatores") + " — integra as "
                   "transações correntes: o item é defensável como CERTO."),
        "condicionais": [("⚠️ Gabarito contestável", (
            "A fonte dá ERRADO alegando que transações correntes incluem “apenas importações e exportações não "
            "fatores”. Isso não se sustenta: TC = bens + serviços + " + vd("renda primária") + " + renda "
            "secundária, e a renda primária (juros, lucros, dividendos, salários) é justamente a remuneração dos "
            "fatores, que a nomenclatura antiga chamava de “serviços fatores”. O gabarito mais defensável seria "
            + vd("CERTO") + ". A única leitura que salva o ERRADO é a de que renda de fatores não é “exportação "
            "e importação de serviços” no BPM6 — leitura terminológica, não conceitual."))],
        "destrinchando": [
            "Nomenclatura antiga (Brasil antes de 2001): balança de serviços = " + azb("serviços não fatores")
            + " (fretes, viagens, seguros, royalties) + " + azb("serviços fatores") + " (juros, lucros, "
            "dividendos, salários — a remuneração do capital e do trabalho). Tudo dentro das transações "
            "correntes.",
            "BPM5 e BPM6: os serviços fatores viraram " + azb("renda") + " (no BPM6, " + azb("renda primária")
            + "), subconta separada, mas <b>continuam</b> nas transações correntes. A conta “serviços” passou a "
            "abrigar só os não fatores.",
            "Estrutura do BPM6: TC = bens + serviços + renda primária + renda secundária; depois conta capital; "
            "depois conta financeira; erros e omissões.",
            "Por isso, quem lê “serviços fatores e não fatores” pensando na estrutura antiga encontra uma "
            "descrição completa das transações correntes (faltariam só as transferências, e o item diz “fluxos "
            "como”, exemplificativo).",
            vm("Regra-âncora: serviços fatores = renda primária = parte das transações correntes."),
        ],
        "dissecando": (cz("[troca de conceito · outro: nomenclatura antiga × BPM6]") + " O item mistura a "
                       "terminologia antiga (fatores e não fatores) com a atual. Para a fonte, o erro estaria em "
                       "chamar renda de “serviço”; na prova oficial, prefira a leitura conceitual — renda de "
                       "fatores está nas transações correntes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os juros pagos a credores estrangeiros integram as transações correntes, na renda "
            "primária.”</i> → CERTO",
            "<i>“No BPM6, a conta de serviços inclui os lucros e dividendos remetidos ao exterior.”</i> → ERRADO "
            "(troca de conceito: são renda primária)",
        ])],
        "reescrita": ("Transações correntes são interações entre residentes e não-residentes que incluem fluxos "
                      "como exportação e importação de bens e serviços" + hl(" não fatores, além das rendas "
                                                                            "primária e secundária") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["como"], "dificuldade": 2,
        "comentario_fonte": ("ERRADO: transações correntes englobam comércio de bens e serviços, “porém incluem "
                             "apenas importações e exportações não fatores”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: gabarito da fonte (ERRADO) se apoia na tese de que TC só inclui serviços não "
                    "fatores; a renda primária (serviços fatores) integra TC, e o item é defensável como CERTO"],
    },
    # ------------------------------------------------------------------ E2-L00100
    {
        "id": "ECO-E2-L00100-1", "fonte_ref": "E2-L00100", "destino": "18", "subtema": H2["cn"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_TC,
        "rotulo_item": "Item",
        "assertiva": ("O saldo das transações correntes é obtido pela soma dos saldos do balanço comercial, do "
                      "balanço de serviços, da renda primária e da renda secundária, e seu superávit indica "
                      "poupança externa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O saldo das transações correntes é obtido pela soma dos saldos do balanço comercial, do "
                       "balanço de serviços, da renda primária e da renda secundária, e seu ") + vm("superávit")
                    + az(" indica poupança externa.")),
        "poucas": ("A composição está certa; o sinal, não: " + vd("S<sub>externa</sub> = −TC") + ". É o "
                   + azb("déficit") + " em transações correntes que indica poupança externa (positiva)."),
        "destrinchando": [
            "Composição (BPM6): TC = balança comercial (bens) + serviços + renda primária (salários, juros, "
            "lucros, dividendos) + renda secundária (transferências correntes). Essa primeira metade do item é "
            "literal.",
            "Identidade: " + vd("I = S<sub>privada</sub> + S<sub>governo</sub> + S<sub>externa</sub>") + ", com "
            "S<sub>externa</sub> = −TC. Déficit em TC → o país absorve mais do que produz e o resto do mundo "
            "financia a diferença (poupança externa positiva).",
            "Superávit em TC → o país produz mais do que absorve, acumula ativos externos (ou reduz passivos) e "
            "“exporta” poupança: poupança externa <b>negativa</b>.",
            "Contrapartida no BP: o déficit em TC aparece como entrada líquida na conta financeira (IDP, "
            "carteira, empréstimos) ou queda de reservas.",
            vm("Regra-âncora: déficit em TC = poupança externa positiva."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " Primeira oração literal, segunda com o sinal invertido. "
                       "🔥 Itens de identidade macro quase sempre testam o sinal da poupança externa; a banca "
                       "oficial cobra o mesmo ponto com “poupança externa positiva → superávit”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…e seu déficit corresponde à poupança externa.”</i> → CERTO",
            "<i>“Um superávit em transações correntes indica que o país é tomador líquido de recursos do resto "
            "do mundo.”</i> → ERRADO (inversão: é fornecedor líquido)",
        ])],
        "reescrita": ("O saldo das transações correntes é obtido pela soma dos saldos do balanço comercial, do "
                      "balanço de serviços, da renda primária e da renda secundária, e seu " + hl("déficit")
                      + " indica poupança externa."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Superávit em TC indica envio de recursos ao exterior, não poupança externa; duas "
                             "respostas de IA com S<sub>ext</sub> = −TC e I = Sp + Sg + Sext (fórmulas em imagem). "
                             "O comentário inicial diz que, no déficit, o país “transfere suas reservas para o "
                             "exterior”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 008", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (S externa = −TC, no 📖)"},
                          {"ref": "IMAGEM 009", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (I = Sp + Sg + Sext, no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0818-1 (CACD 2026, poupança externa positiva × superávit em TC)",
                    "qualidade_fonte: o comentário inicial confunde déficit em TC com transferência de reservas "
                    "ao exterior; corrigido pelas respostas seguintes da própria fonte"],
    },
]
