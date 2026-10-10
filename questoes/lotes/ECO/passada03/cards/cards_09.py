"""Cards do lote de redação 09 — ECO, passada 03 (notas 67, 68 e 69: reservas, poupança externa, câmbio-juros)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "res": "📘 Reservas e intervenção",
    "pe": "🧂 Poupança externa",
    "hi": "🔗 Hiatos e restrição externa",
    "par": "🔗 Paridades e repasse cambial",
}

CMD_BOZAN_PPC = "Sobre a paridade do poder de compra internacional (PPC), julgue certo ou errado as assertivas."

CMD_BOZAN_Q3 = ("Julgue as assertivas a seguir sobre a dinâmica dos mercados de bens, monetário e cambial no contexto "
                "de economias internacionais.")

CMD_BOZAN_Q4 = ("Julgue as afirmativas a seguir sobre investimentos internacionais e fluxos de capitais, considerando o "
                "entendimento técnico de paridades de juros e riscos associados.")

CMD_NAB_26 = "Em relação à macroeconomia aberta, julgue (C ou E) os seguintes itens."

CMD_NAB_23 = "Com base nos conceitos de macroeconomia aberta, julgue (C ou E) os itens seguintes."

CMD_RT_ABERTA = "A respeito dos conceitos e teorias da macroeconomia aberta, responda C ou E."

CMD_RT_UIP = "Com base na equação de Paridade Descoberta da Taxa de Juros, avalie as seguintes afirmativas."

CMD_JUROS_CAMBIO = "Julgue o item a seguir, relativo à relação entre taxa de juros e taxa de câmbio."

CARDS = [
    # ------------------------------------------------------------------ E3-L00420
    {
        "id": "ECO-E3-L00420-1", "fonte_ref": "E3-L00420", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": ("A respeito dos efeitos que alterações na política monetária ou a flutuação do mercado cambial "
                    "produzem sobre a base monetária e a liquidez do sistema financeiro nacional, julgue certo ou "
                    "errado (C ou E) os itens a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Mantendo todas as demais condições no mercado constantes, quando o Banco Central compra dólares "
                      "das instituições bancárias e financeiras, há um aumento da base monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Mantendo todas as demais condições no mercado constantes</u>, quando o Banco Central "
                      "<u>compra</u> dólares das instituições bancárias e financeiras, há um <u>aumento</u> da base "
                      "monetária."),
        "poucas": ("Para comprar dólares, o BC paga em " + azb("reais") + " creditados nas reservas bancárias: o "
                   "ativo (reservas internacionais) e o passivo monetário sobem juntos e a " + vd("base monetária "
                   "aumenta") + " — salvo esterilização posterior."),
        "destrinchando": [
            azb("Base monetária") + " = papel-moeda emitido (em poder do público + caixa dos bancos) + "
            + azb("reservas bancárias") + " no Banco Central. É o passivo monetário do BC: tudo o que ele compra "
            "pagando com esse passivo expande a base.",
            "No balanço do BC, a compra de US$ 1 bilhão a R$ 5,00 registra " + vd("+ R$ 5 bilhões") + " no ativo "
            "(reservas internacionais) e " + vd("+ R$ 5 bilhões") + " no passivo (reservas dos bancos). A venda "
            "de dólares faz o inverso: o BC recolhe reais e a base encolhe.",
            "Regra geral que resolve a família inteira de itens: " + vm("BC compra ativo (dólar, título, crédito "
            "a banco) → injeta liquidez; BC vende ativo → enxuga liquidez.") + " Valem pelo mesmo raciocínio a "
            "compra de títulos no open market e o redesconto.",
            azb("Esterilização") + ": para que a compra de divisas não derrube os juros abaixo da meta, o BC "
            "recolhe a liquidez criada vendendo títulos ou fazendo " + azb("operações compromissadas") + ". A "
            "base volta ao nível inicial; o que muda é a composição do ativo (mais reservas, menos títulos "
            "livres) e o custo fiscal (o BC paga juros domésticos e recebe juros externos, em geral menores).",
            "No " + rx("Brasil") + ", o forte acúmulo de reservas dos anos 2000 foi esterilizado sobretudo com "
            "compromissadas — por isso a base não explodiu, mas a dívida bruta do governo geral cresceu.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item reproduz o mecanismo de manual e se protege com o "
                       "“mantendo todas as demais condições constantes”, que afasta a esterilização. A banca "
                       "costuma inverter o sentido (venda de dólares → aumento da base) ou afirmar que a compra "
                       "esterilizada expande a base."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando o Banco Central vende dólares às instituições financeiras, há um aumento da base "
            "monetária.”</i> → ERRADO (inversão: a venda enxuga reais)",
            "<i>“A compra de dólares pelo Banco Central, acompanhada de venda de títulos em igual montante, eleva "
            "a base monetária.”</i> → ERRADO (compra esterilizada: a base fica inalterada)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["mantendo todas as demais condições constantes"],
        "dificuldade": 1,
        "comentario_fonte": ("O BC paga os dólares em reais creditados nas reservas bancárias, expandindo a base "
                             "monetária, salvo esterilização; BC compra ativos → injeta liquidez; vende → enxuga."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0771
    {
        "id": "ECO-E1-0771-1", "fonte_ref": "E1-0771", "destino": "68", "subtema": H2["hi"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": ("Acerca da relação entre regime cambial, contas externas e financiamento do crescimento, julgue "
                    "o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de câmbio fixo, o crescimento sustentado da economia baseado em déficits em "
                      "transações correntes torna o equilíbrio das contas externas diretamente dependente da "
                      "liquidez no mercado financeiro internacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um regime de <u>câmbio fixo</u>, o crescimento sustentado da economia baseado em "
                      "<u>déficits em transações correntes</u> torna o equilíbrio das contas externas diretamente "
                      "dependente da liquidez no mercado financeiro internacional."),
        "poucas": ("Déficit em transações correntes precisa ser " + azb("financiado") + " por entrada de capitais "
                   "ou por perda de reservas. Com câmbio fixo, não há depreciação que corrija o déficit: se o "
                   "crédito externo seca, o país queima reservas até a crise."),
        "destrinchando": [
            "Identidade do balanço de pagamentos: " + vd("TC + conta capital + conta financeira = variação de "
            "reservas") + " (com erros e omissões). Um déficit em TC é coberto por capitais que entram ou por "
            "reservas que saem — não há terceira via.",
            "No câmbio " + azb("flutuante") + ", a escassez de financiamento deprecia a moeda, encarece "
            "importações, estimula exportações e reduz o déficit: o preço faz o ajuste. No câmbio "
            + azb("fixo") + ", o BC se compromete a vender divisas à taxa anunciada; se os capitais param de "
            "entrar, o ajuste recai sobre as reservas (e, no limite, sobre a recessão ou a desvalorização "
            "forçada).",
            "Por isso o crescimento “puxado” por poupança externa sob câmbio fixo fica refém do ciclo de "
            "liquidez global — o que a literatura chama de " + azb("sudden stop") + " (parada súbita dos "
            "fluxos).",
            "Dois episódios do " + rx("Brasil") + ": o II PND, financiado com petrodólares nos anos 1970, "
            "desembocou na crise da dívida após o choque de juros de 1979 e a moratória mexicana de 1982; e o "
            "Plano Real, com câmbio administrado e déficits em TC crescentes, sofreu com as crises asiática "
            "(1997) e russa (1998) até a flutuação de " + vd("janeiro de 1999") + ".",
            vm("Regra-âncora: déficit em TC + câmbio fixo = financiamento externo contínuo ou perda de "
               "reservas."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item é a descrição padrão da vulnerabilidade externa; as "
                       "palavras-chave são “câmbio fixo” (sem ajuste via preço) e “déficits em transações "
                       "correntes” (necessidade de financiamento). A banca costuma errar o item trocando o "
                       "regime: no flutuante, a dependência é menor, porque o câmbio ajusta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio flutuante puro, déficits em transações correntes são financiados "
            "obrigatoriamente pela venda de reservas do Banco Central.”</i> → ERRADO (no flutuante o ajuste é "
            "pelo câmbio, não pelas reservas)",
            "<i>“Sob câmbio fixo, a interrupção dos fluxos de capitais externos tende a provocar perda de "
            "reservas internacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["diretamente"], "dificuldade": 1,
        "comentario_fonte": ("Em câmbio fixo, déficits em TC precisam ser financiados por entrada de capitais; caso "
                             "contrário, há perda de reservas, o que torna o equilíbrio externo dependente da "
                             "liquidez externa."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00102
    {
        "id": "ECO-E2-L00102-1", "fonte_ref": "E2-L00102", "destino": "68", "subtema": H2["hi"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Com base na estrutura das transações correntes no balanço de pagamentos, julgue as assertivas "
                    "a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Um hiato do produto é caracterizado quando a economia importa mais do que exporta, sugerindo "
                      "uma produção doméstica insuficiente que leva à absorção de bens do exterior."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Um <u>hiato do produto</u> é caracterizado quando a economia importa mais do que exporta, "
                      "sugerindo uma produção doméstica insuficiente que leva à absorção de bens do exterior."),
        "poucas": ("O curso considera CERTO lendo o “hiato” como " + azb("hiato de recursos") + ": importar mais do "
                   "que exportar significa que a absorção interna supera o produto. Mas “hiato do produto”, na "
                   "nomenclatura consagrada, é outra coisa."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "na macroeconomia padrão, " + azb("hiato do produto") + " (<i>output gap</i>) é a "
                          "diferença entre o produto efetivo e o " + azb("produto potencial") + " — mede ociosidade "
                          "ou superaquecimento, não o saldo comercial. O que o item descreve (M &gt; X, absorção "
                          "acima do produto) é o " + azb("hiato de recursos") + " ou " + azb("hiato externo")
                          + " do modelo de dois hiatos. Numa prova CEBRASPE, a resposta mais defensável seria "
                          "ERRADO (troca de conceito).")],
        "destrinchando": [
            "Identidade da absorção: " + vd("Y = A + (X − M)") + ", em que A = C + I + G é a absorção interna. Se "
            + vd("M &gt; X") + ", então " + vd("A &gt; Y") + ": o país usa mais bens e serviços do que produz, e "
            "a diferença vem do exterior. É o sentido em que a assertiva fala em “produção doméstica "
            "insuficiente”.",
            azb("Hiato do produto") + " = (Y − Y*) / Y*. Negativo → recursos ociosos, desemprego acima do "
            "natural, pressão desinflacionária; positivo → economia aquecida, pressão inflacionária. É variável "
            "central do regime de metas (regra de " + oc("Taylor") + "), e nada tem a ver com o sinal da balança "
            "comercial: um país em recessão pode ter déficit externo, e um país superaquecido, superávit.",
            "O " + azb("modelo de dois hiatos") + " (" + oc("Chenery e Strout") + ", 1966) diz que o crescimento "
            "de um país em desenvolvimento pode ser limitado pelo " + azb("hiato de poupança") + " (I &gt; S) ou "
            "pelo " + azb("hiato de divisas") + " (importações necessárias &gt; exportações); a ajuda ou o "
            "capital externo fecham o hiato que estiver “mordendo”.",
            "Leitura correta da situação descrita: déficit comercial → " + vd("poupança externa positiva")
            + " → I − S = M − X (desconsideradas rendas e transferências).",
        ],
        "dissecando": (cz("[outro: nomenclatura não padrão]") + " O item cola o rótulo “hiato do produto” numa "
                       "descrição que corresponde ao hiato de recursos externo. O curso tratou como CERTO; na "
                       "prova, o reflexo deve ser conferir a definição: <i>output gap</i> compara produto efetivo "
                       "e potencial, não exportações e importações."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O hiato do produto corresponde à diferença entre o produto efetivo e o produto potencial da "
            "economia.”</i> → CERTO",
            "<i>“Quando a economia importa mais do que exporta, a absorção interna é inferior ao produto.”</i> → "
            "ERRADO (inversão: M &gt; X implica absorção maior que o produto)",
        ])],
        "tipo_erro": ["OUTRO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Hiato do produto surge quando a produção interna não atende à demanda doméstica, "
                             "forçando o aumento das importações e gerando déficits em transações correntes."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: “hiato do produto” é, na nomenclatura padrão, a diferença entre produto efetivo e "
                    "potencial; o item descreve o hiato de recursos externo (M > X, absorção > produto) — "
                    "resposta mais defensável: ERRADO",
                    "qualidade_fonte: o comentário de origem identifica hiato do produto com déficit comercial"],
    },
    # ------------------------------------------------------------------ E2-L00957
    {
        "id": "ECO-E2-L00957-1", "fonte_ref": "E2-L00957", "destino": "68", "subtema": H2["pe"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": ("Acerca da estrutura do balanço de pagamentos e das contas nacionais, julgue os próximos "
                    "itens."),
        "excerto": ("<p><i>Um país realizou, em determinado ano, as transações com o exterior apresentadas a seguir: "
                    "importações de mercadoria: 5; exportações de mercadoria: 15; recebimento de doações na forma "
                    "de mercadorias: 1; empréstimos e financiamentos recebidos no exterior: 10; investimento "
                    "estrangeiro direto recebido do exterior, sem cobertura cambial, na forma de equipamentos: 15; "
                    "juros de empréstimos pagos ao exterior: 5; fretes pagos ao exterior: 10.</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("Com base nessas informações, no período em apreço, o país utilizou poupança externa no "
                      "financiamento dos seus gastos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com base nessas informações, no período em apreço, o país <u>utilizou</u> poupança externa "
                      "no financiamento dos seus gastos."),
        "poucas": ("O saldo em transações correntes é " + vd("TC = −20") + ". Déficit em TC = " + azb("poupança "
                   "externa positiva") + " (S<sub>e</sub> = −TC = " + vd("20") + "): o país financiou parte dos "
                   "gastos com recursos do exterior."),
        "destrinchando": [
            "Ponte com as contas nacionais: " + vd("S − I = TC") + " → " + vd("I = S + S<sub>e</sub>") + ", com "
            "S<sub>e</sub> = −TC. Basta descobrir o sinal de TC.",
            azb("Balança comercial") + ": exportações 15 − importações 5 − mercadorias doadas 1 − equipamentos do "
            "IED 15 = " + vd("−6") + ". As entradas “sem cobertura cambial” (doação e IED em bens) são, "
            "fisicamente, importações e entram como débito na balança.",
            azb("Serviços") + ": fretes pagos " + vd("−10") + ". " + azb("Renda primária") + ": juros pagos "
            + vd("−5") + ". " + azb("Renda secundária") + ": doação recebida " + vd("+1") + " (contrapartida da "
            "importação doada). Soma: −6 − 10 − 5 + 1 = " + vd("TC = −20") + ".",
            "Contrapartidas na " + azb("conta financeira") + ": empréstimos recebidos (+10) e IED em equipamentos "
            "(+15) são passivos externos novos, total " + vd("25") + ". Como 25 &gt; 20, sobram 5 de "
            "acumulação de reservas — o BP fecha.",
            "Pegadinhas do enunciado: empréstimos não entram em TC (só os juros); IED sem cobertura cambial "
            "aparece duas vezes (importação na balança e passivo na conta financeira); a doação em mercadoria "
            "também tem lançamento duplo (importação e renda secundária), com efeito líquido nulo sobre TC.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de cálculo: o examinador espalha lançamentos de natureza diferente "
                       "(financeiros, de bens, de renda) para ver se o candidato separa o que é TC. Quem soma os "
                       "empréstimos e o IED como receita de TC acha superávit e erra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O saldo da balança comercial foi superavitário em 10.”</i> → ERRADO (esqueceu as importações "
            "sem cobertura cambial: o saldo é −6)",
            "<i>“O país acumulou reservas internacionais no período.”</i> → CERTO (conta financeira de 25 "
            "supera o déficit de 20)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("S − I = TC; se TC < 0, há poupança externa. BC = 15 − 5 − 15 − 1 = −6; BS = −10; "
                             "RP = −5; RS = +1; TC = −20."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 158", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 159", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_corrigido: numeração “4.” retirada da assertiva; dados das transações levados ao "
                    "excerto"],
    },
    # ------------------------------------------------------------------ E2-L01590
    {
        "id": "ECO-E2-L01590-1", "fonte_ref": "E2-L01590", "destino": "68", "subtema": H2["pe"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "A respeito das relações entre consumo, poupança e crescimento econômico, julgue os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Quando um país tem déficit em transações correntes, pode-se dizer que a poupança doméstica "
                      "não foi suficiente para financiar o investimento doméstico, de forma que há o recurso à "
                      "poupança externa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando um país tem <u>déficit</u> em transações correntes, pode-se dizer que a poupança "
                      "doméstica <u>não foi suficiente</u> para financiar o investimento doméstico, de forma que há "
                      "o recurso à poupança externa."),
        "poucas": ("Pela identidade " + vd("S − I = TC") + ", TC &lt; 0 implica S &lt; I: a diferença é coberta "
                   "por " + azb("poupança externa") + " (S<sub>e</sub> = −TC), isto é, por entrada líquida de "
                   "capitais."),
        "destrinchando": [
            "Derivação: Y = C + I + G + (X − M). Com a renda nacional disponível (que soma as rendas e "
            "transferências líquidas do exterior), a poupança doméstica é S = Y<sub>d</sub> − C − G e o saldo "
            "externo relevante passa a ser o de transações correntes: " + vd("S − I = TC") + ".",
            "Leitura dos sinais: " + vd("TC &gt; 0") + " → S &gt; I, o país empresta ao resto do mundo e acumula "
            "ativos externos; " + vd("TC &lt; 0") + " → S &lt; I, o país absorve " + azb("poupança externa")
            + " e acumula passivos (IED, carteira, empréstimos), registrados na conta financeira.",
            "A poupança doméstica se divide em privada (S<sub>p</sub> = Y<sub>d</sub> − C) e pública "
            "(S<sub>g</sub> = T − G). Daí a versão dos " + azb("déficits gêmeos") + ": com investimento e "
            "poupança privada dados, um déficit público maior tende a aparecer como déficit externo maior.",
            "É identidade contábil, sem causalidade embutida: o déficit externo pode refletir investimento "
            "alto (bom sinal, se produtivo) ou consumo alto (mais preocupante). A sustentabilidade depende de "
            "como é financiado — IED é mais estável que capital de curto prazo.",
            "O " + rx("Brasil") + " costuma operar com déficit em transações correntes financiado em boa parte "
            "por investimento direto no país.",
        ],
        "dissecando": (cz("[literalidade]") + " O item é a leitura direta da identidade S − I = TC. Para errar, "
                       "a banca trocaria o sinal (“superávit em transações correntes indica recurso à poupança "
                       "externa”) ou transformaria a identidade em relação causal obrigatória."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um superávit em transações correntes indica que o país recorreu à poupança externa para "
            "financiar seu investimento.”</i> → ERRADO (sinal trocado: superávit = S &gt; I, o país exporta "
            "poupança)",
            "<i>“O déficit em transações correntes decorre necessariamente de excesso de consumo do "
            "governo.”</i> → ERRADO (nexo indevido: a identidade não indica a causa)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["pode-se dizer"], "dificuldade": 1,
        "comentario_fonte": ("I = S + S<sub>e</sub>; déficit em TC significa S < I, e a diferença é financiada "
                             "por poupança externa (entrada líquida de capitais)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 445", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0672
    {
        "id": "ECO-E1-0672-1", "fonte_ref": "E1-0672", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": "Acerca das relações entre juros, câmbio e fluxos de capitais, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Um forte diferencial positivo entre a taxa de juros interna e as taxas de juros "
                      "internacionais tem efeitos sobre a economia por meio da atração de capital, da valorização "
                      "cambial e do aumento das importações."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um forte diferencial <u>positivo</u> entre a taxa de juros interna e as taxas de juros "
                      "internacionais tem efeitos sobre a economia por meio da atração de capital, da "
                      "<u>valorização</u> cambial e do <u>aumento</u> das importações."),
        "poucas": ("Juro interno bem acima do externo atrai capital (" + azb("carry trade") + "), a oferta de "
                   "divisas sobe, a moeda nacional se " + vd("valoriza") + " e os importados ficam mais "
                   "baratos: " + vd("importações ↑") + "."),
        "destrinchando": [
            "Cadeia de transmissão: " + vd("i − i* ↑ → entrada de capitais → oferta de dólares ↑ → E ↓ "
            "(apreciação) → M ↑ e X ↓") + ". É o canal cambial da política monetária, que também ajuda a "
            "derrubar a inflação (importados mais baratos).",
            "O que atrai o capital não é o diferencial bruto, mas o diferencial ajustado ao " + azb("risco-país")
            + " e à " + azb("depreciação esperada") + ": i − i* − ρ − ΔE<sup>e</sup>. Um diferencial “forte” "
            "costuma superar essas deduções — daí o fluxo.",
            azb("Carry trade") + ": tomar emprestado em moeda de juro baixo (iene, franco suíço, dólar em 2009–"
            "2015) e aplicar em moeda de juro alto. Ganha-se o diferencial enquanto o câmbio não se move contra; "
            "a saída abrupta em momentos de aversão a risco provoca depreciações bruscas.",
            "No " + rx("Brasil") + ", Selic elevada e alta das commodities levaram a forte apreciação do real "
            "entre meados dos anos 2000 e 2011. O governo reagiu com IOF sobre a entrada de capitais (a partir "
            "de 2009) e o ministro Guido Mantega cunhou a expressão “guerra cambial” (2010).",
            "Custo de longo prazo discutido na literatura: câmbio apreciado por muito tempo reduz a "
            "competitividade da indústria e alimenta o debate sobre " + azb("desindustrialização") + ".",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item encadeia três efeitos na ordem certa. A banca costuma "
                       "errar trocando um elo: “desvalorização cambial” ou “redução das importações”. Teste "
                       "rápido: juro alto → dólar barato → importação sobe."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um forte diferencial positivo de juros tende a desvalorizar a moeda nacional, estimulando as "
            "exportações.”</i> → ERRADO (inversão: a entrada de capitais valoriza a moeda)",
            "<i>“A atração de capitais depende do diferencial de juros descontados o risco-país e a depreciação "
            "esperada.”</i> → CERTO",
        ]), ("🃏 Carta na manga", [
            "Juros altos por tempo prolongado produzem um câmbio apreciado que barateia importações e ajuda a "
            "conter a inflação, mas comprimem a competitividade da indústria — um dilema recorrente da "
            "política macroeconômica brasileira desde o Plano Real.",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["forte"], "dificuldade": 1,
        "comentario_fonte": ("Juros internos altos atraem capitais (carry trade), valorizam a moeda e estimulam as "
                             "importações; o Brasil viveu isso entre 2005 e 2011."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: o comando da prova remete a um texto motivador não preservado na fonte; comando "
                    "neutro adotado (o item é julgável sem o texto)"],
    },
    # ------------------------------------------------------------------ E1-0747
    {
        "id": "ECO-E1-0747-1", "fonte_ref": "E1-0747", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo aos fluxos financeiros internacionais.",
        "rotulo_item": "Item",
        "assertiva": ("Os fluxos financeiros são impactados por expectativas e políticas cambiais e monetárias das "
                      "diferentes economias; assim, se a taxa de juros de um país for superior à de outro país, "
                      "espera-se um fluxo positivo de recursos em direção ao país com taxa de juros mais elevada, "
                      "com mesmo perfil de risco."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os fluxos financeiros são impactados por expectativas e políticas cambiais e monetárias das "
                      "diferentes economias; assim, se a taxa de juros de um país for superior à de outro país, "
                      "<u>espera-se</u> um fluxo positivo de recursos em direção ao país com taxa de juros mais "
                      "elevada, <u>com mesmo perfil de risco</u>."),
        "poucas": ("Com risco igual, o capital procura o " + azb("maior retorno") + ": juro mais alto atrai "
                   "recursos. O fluxo só não ocorre se a " + azb("depreciação esperada") + " da moeda do país "
                   "de juro alto anular o diferencial."),
        "destrinchando": [
            "A referência é a " + azb("paridade descoberta da taxa de juros") + ": em equilíbrio, "
            + vd("i = i* + ΔE<sup>e</sup> + ρ") + " (ρ = prêmio de risco). Se i supera o lado direito, há "
            "ganho esperado em aplicar no país e o capital entra; se fica abaixo, o capital sai.",
            "O item neutraliza ρ (“mesmo perfil de risco”) e fala de expectativa (“espera-se”), não de "
            "certeza. O que resta para frear o fluxo é a variação cambial esperada: um diferencial de 1 p.p. "
            "atrai capital se a depreciação esperada for menor que 1%.",
            "A primeira oração também está certa: expectativas (sobre câmbio, inflação, solvência) e políticas "
            "(juros do banco central, controles de capital, intervenções) mexem diretamente nos retornos "
            "esperados e, portanto, nos fluxos.",
            "O próprio fluxo tende a fechar o diferencial: a entrada de capitais aprecia a moeda hoje e, com o "
            "câmbio esperado dado, aumenta a depreciação esperada dali em diante, até a paridade se restabelecer.",
            vm("Regra-âncora: capital vai para onde i − i* supera depreciação esperada + risco."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item se protege com “espera-se” e “com "
                       "mesmo perfil de risco”. Sem essa última cláusula, uma banca exigente poderia objetar que "
                       "o juro alto apenas compensa risco maior. Versões ERRADAS trocam o sentido do fluxo ou "
                       "afirmam que ele independe das expectativas cambiais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…espera-se um fluxo de recursos em direção ao país com taxa de juros mais elevada, "
            "independentemente da expectativa de variação cambial.”</i> → ERRADO (modulador absoluto: a "
            "depreciação esperada pode anular o diferencial)",
            "<i>“…espera-se fluxo em direção ao país de juros mais altos, ainda que seu risco de crédito seja "
            "muito superior.”</i> → ERRADO (ignora o prêmio de risco)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["espera-se", "com mesmo perfil de risco"],
        "dificuldade": 1,
        "comentario_fonte": ("A paridade de juros sugere que diferenciais de juros explicam os fluxos de capital, "
                             "corrigidos pela expectativa de variação cambial: 1% a mais de juro atrai capital se "
                             "a depreciação esperada for menor que 1%."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ 2014 na fonte sugere CACD 2014; não confirmada"],
    },
    # ------------------------------------------------------------------ E1-0752
    {
        "id": "ECO-E1-0752-1", "fonte_ref": "E1-0752", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo a regimes cambiais e à paridade de juros.",
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de câmbio fixo, a taxa de câmbio definida pelo Banco Central será a taxa de "
                      "equilíbrio quando se verificar a condição da paridade dos juros, ou seja, quando a taxa de "
                      "juros doméstica for igual à taxa de juros estrangeira."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um regime de <u>câmbio fixo</u>, a taxa de câmbio definida pelo Banco Central será a "
                      "taxa de equilíbrio quando se verificar a condição da paridade dos juros, ou seja, quando a "
                      "taxa de juros doméstica for <u>igual</u> à taxa de juros estrangeira."),
        "poucas": ("Com câmbio fixo e crível, a " + azb("depreciação esperada é zero") + "; a paridade descoberta "
                   "(i = i* + ΔE<sup>e</sup>) vira " + vd("i = i*") + ". Só aí não há pressão de entrada ou saída "
                   "de capitais e a paridade se sustenta sem perda ou ganho de reservas."),
        "destrinchando": [
            "Se " + vd("i &gt; i*") + ", entra capital: há excesso de oferta de divisas, e o BC, para manter a "
            "paridade, compra dólares e emite reais. A base monetária cresce e os juros domésticos caem até "
            "i = i*. Se " + vd("i &lt; i*") + ", sai capital: o BC vende reservas, a base encolhe e os juros "
            "sobem.",
            "Diferente do que sugere a fonte, sob câmbio fixo o ajuste não é feito pela apreciação do câmbio "
            "(que está travado), mas pela " + azb("quantidade de moeda") + ": a oferta monetária vira variável "
            "endógena.",
            "É a " + azb("trindade impossível") + " (" + oc("Mundell") + "): câmbio fixo + livre mobilidade de "
            "capitais = perda da autonomia monetária. No Mundell-Fleming com mobilidade perfeita, a política "
            "monetária é ineficaz sob câmbio fixo, e a fiscal, máxima.",
            "Ressalvas: com risco-país, o equilíbrio é " + vd("i = i* + ρ") + "; se o mercado duvida da "
            "paridade, entra um termo de desvalorização esperada e o juro doméstico fica acima de i* + ρ (falta "
            "de credibilidade).",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item usa a versão simplificada (sem risco e com "
                       "paridade crível). A pista é “câmbio fixo”: zera a expectativa de variação cambial e "
                       "reduz a paridade a i = i*. A versão ERRADA típica diria que o equilíbrio exige i acima de "
                       "i* ou que o BC controla os juros livremente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio fixo com livre mobilidade de capitais, o Banco Central pode fixar a taxa de "
            "juros doméstica independentemente da taxa externa.”</i> → ERRADO (trindade impossível)",
            "<i>“Sob câmbio fixo, juros domésticos acima dos externos levam o Banco Central a acumular "
            "reservas.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Pela não arbitragem, o câmbio de equilíbrio ocorre quando não há incentivo de entrada "
                             "ou saída de divisas; a entrada de capitais aprecia o câmbio, equalizando os juros."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: marca ⌚ 2019 na fonte sugere CACD 2019; não confirmada",
                    "qualidade_fonte: o comentário de origem atribui o ajuste à apreciação cambial, que não "
                    "ocorre sob câmbio fixo; o ajuste é pela oferta de moeda"],
    },
    # ------------------------------------------------------------------ E1-0819
    {
        "id": "ECO-E1-0819-1", "fonte_ref": "E1-0819", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": "Acerca de macroeconomia aberta, regime cambial e determinação da taxa de câmbio, julgue o item subsequente.",
        "excerto": ("<p><i>Em economias abertas, choques de confiança e alterações no prêmio de risco podem afetar "
                    "fluxos de capitais e pressionar a taxa de câmbio. A resposta de política econômica — "
                    "incluindo-se o uso de juros, intervenção e reservas — depende, entre outros fatores, do regime "
                    "cambial vigente e das restrições impostas pelo grau de mobilidade de capitais. Ademais, "
                    "distinções conceituais entre taxa de câmbio nominal e taxa de câmbio real são relevantes para "
                    "analisar preços relativos e competitividade, assim como para discutir mecanismos de "
                    "transmissão do câmbio para a inflação.</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("Um aumento persistente do diferencial de juros tende a desvalorizar o câmbio e, por essa via, "
                      "elevar a inflação doméstica; ademais, os efeitos sobre exportações e importações tendem a "
                      "atenuar esse aumento do nível de preços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um aumento persistente do diferencial de juros tende a ") + vm("desvalorizar") + az(" o "
                    "câmbio e, por essa via, ") + vm("elevar") + az(" a inflação doméstica; ademais, os efeitos "
                    "sobre exportações e importações tendem a ") + vm("atenuar esse aumento") + az(" do nível de "
                    "preços.")),
        "poucas": ("Diferencial de juros maior atrai capital e " + azb("valoriza") + " a moeda: importados ficam "
                   "mais baratos e a inflação " + vd("cai") + ". E o efeito sobre o comércio (X ↓, M ↑) reduz a "
                   "demanda agregada, " + vm("reforçando") + " a desinflação, não atenuando."),
        "destrinchando": [
            "Canal cambial da política monetária: " + vd("i − i* ↑ → entrada de capitais → E ↓ (apreciação) → "
            "preços em reais dos bens importados ↓ → inflação ↓") + ". É por isso que o aperto monetário costuma "
            "agir mais rápido sobre os bens comercializáveis.",
            "Canal da demanda: com a moeda apreciada, " + vd("exportações ↓ e importações ↑") + " → exportações "
            "líquidas ↓ → demanda agregada ↓ → menor pressão sobre preços. Os dois canais apontam na mesma "
            "direção.",
            "O item inverte tudo de forma coerente: se o câmbio se desvalorizasse, a inflação subiria e o "
            "comércio (X ↑, M ↓) <b>aqueceria</b> a demanda — também reforçaria a inflação, em vez de atenuá-la. "
            "Há, portanto, dois erros independentes.",
            "Aparente paradoxo com a " + azb("paridade descoberta") + ": i &gt; i* implica depreciação "
            "<b>esperada</b>. No modelo de " + oc("Dornbusch") + " (1976, <i>overshooting</i>), a alta de juros "
            "aprecia o câmbio imediatamente além do nível de longo prazo; a partir daí, espera-se depreciação "
            "gradual. O efeito de impacto, que é o que transmite à inflação, é de apreciação.",
            "Exceção estudada no " + rx("Brasil") + " de 2002–2003 (" + oc("Blanchard") + ", “dominância "
            "fiscal”): com dívida alta e risco-país elevado, juros maiores podem aumentar o risco de default e "
            "depreciar a moeda. É caso-limite, não a regra que a banca cobra.",
        ],
        "dissecando": (cz("[inversão]") + " O item descreve com coerência interna o efeito de uma redução do "
                       "diferencial de juros e ainda erra o sinal do canal comercial. A armadilha é a lembrança "
                       "da paridade descoberta (i alto ↔ depreciação esperada), que não descreve o efeito de "
                       "impacto sobre o câmbio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento persistente do diferencial de juros tende a valorizar o câmbio e, por essa via, "
            "reduzir a inflação doméstica.”</i> → CERTO",
            "<i>“A valorização cambial decorrente de juros altos tende a elevar as exportações líquidas.”</i> → "
            "ERRADO (inversão: X ↓ e M ↑, exportações líquidas caem)",
        ]), ("🃏 Carta na manga", [
            "No regime de metas brasileiro, boa parte da eficácia de curto prazo da Selic passa pelo câmbio: o "
            "diferencial de juros valoriza o real e derruba os preços dos comercializáveis antes de a demanda "
            "doméstica reagir.",
        ])],
        "reescrita": ("Um aumento persistente do diferencial de juros tende a " + hl("valorizar") + " o câmbio e, "
                      "por essa via, " + hl("reduzir") + " a inflação doméstica; ademais, os efeitos sobre "
                      "exportações e importações tendem a " + hl("reforçar essa redução") + " do nível de preços."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende a", "persistente"], "dificuldade": 2,
        "comentario_fonte": "Verso só com o gabarito (ERRADO), sem comentário.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: o texto motivador da prova foi levado ao excerto, e o comando, ajustado ao "
                    "singular (“julgue o item subsequente”)"],
    },
    # ------------------------------------------------------------------ E1-0864
    {
        "id": "ECO-E1-0864-1", "fonte_ref": "E1-0864", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": CMD_JUROS_CAMBIO,
        "rotulo_item": "Item",
        "assertiva": ("Uma elevação da taxa de juros doméstica, sem alteração na taxa de juros internacional, "
                      "provocará um processo de perda de valor da moeda estrangeira no mercado de câmbio "
                      "doméstico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma elevação da taxa de juros doméstica, sem alteração na taxa de juros internacional, "
                      "provocará um processo de <u>perda de valor da moeda estrangeira</u> no mercado de câmbio "
                      "doméstico."),
        "poucas": ("Juro doméstico maior atrai capital e aumenta a oferta de divisas: a moeda " + azb("estrangeira "
                   "perde valor") + ", o que é o mesmo que dizer que a moeda nacional se " + vd("aprecia") + " (E "
                   "em R$/US$ cai)."),
        "destrinchando": [
            "Pela " + azb("paridade descoberta") + " com câmbio esperado e risco constantes, " + vd("i ↑ → "
            "retorno dos ativos domésticos ↑ → entrada de capitais → E ↓") + ". No mercado doméstico, o dólar "
            "fica mais barato em reais.",
            "Tradução de vocabulário que a banca explora: “perda de valor da moeda estrangeira” = “depreciação "
            "do dólar” = “apreciação do real” = “queda da taxa de câmbio” (cotação do incerto, R$ por US$). "
            "Quatro formas de dizer a mesma coisa.",
            "A expressão “sem alteração na taxa de juros internacional” isola o diferencial: o que importa é "
            + vd("i − i*") + ". Se o juro externo subisse na mesma medida, o efeito sumiria.",
            "Contraexemplo raro, mas cobrado: quando a dívida pública é alta e o risco de default é sensível aos "
            "juros (" + oc("Blanchard") + ", sobre o " + rx("Brasil") + " de 2002–2003), a alta da Selic pode "
            "elevar o risco-país e depreciar o real — a chamada " + azb("dominância fiscal") + ".",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O item descreve a apreciação da moeda nacional "
                       "pelo avesso (“perda de valor da moeda estrangeira”), para confundir quem associa “perda "
                       "de valor” a algo ruim para o país. Traduza sempre para “R$ por US$ sobe ou cai?”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma elevação da taxa de juros doméstica, sem alteração da taxa internacional, provocará "
            "depreciação da moeda nacional.”</i> → ERRADO (inversão: a moeda nacional se aprecia)",
            "<i>“Uma elevação simultânea e de mesma magnitude das taxas de juros doméstica e internacional "
            "tende a apreciar a moeda nacional.”</i> → ERRADO (o diferencial não muda)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["sem alteração na taxa de juros "
                                                                            "internacional"],
        "dificuldade": 1,
        "comentario_fonte": ("Juros e câmbio têm relação inversa: quando a taxa de juros sobe, a cotação do dólar "
                             "tende a cair, valorizando a moeda nacional (fonte citada: site Rede Câmbio Seguro)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: a fonte trazia o item na forma “É correto afirmar que “…”?”; mantida só a "
                    "assertiva, com vírgula após “internacional”"],
    },
    # ------------------------------------------------------------------ E1-0866
    {
        "id": "ECO-E1-0866-1", "fonte_ref": "E1-0866", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, relativo à paridade descoberta da taxa de juros.",
        "rotulo_item": "Item",
        "assertiva": ("A adição de um termo de risco país na equação da paridade descoberta da taxa de juros tende a "
                      "reforçar a necessidade de elevação do diferencial da taxa de juros entre a economia doméstica "
                      "e a economia internacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A adição de um termo de risco país na equação da paridade descoberta da taxa de juros tende "
                      "a <u>reforçar</u> a necessidade de elevação do diferencial da taxa de juros entre a economia "
                      "doméstica e a economia internacional."),
        "poucas": ("Com risco-país, a paridade vira " + vd("i = i* + ΔE<sup>e</sup> + ρ") + ": para reter capital, o "
                   "juro doméstico precisa superar o externo também pelo " + azb("prêmio de risco") + ". O "
                   "diferencial exigido aumenta."),
        "destrinchando": [
            azb("Paridade descoberta") + " pura: ativos de dois países são substitutos perfeitos e rendem o mesmo "
            "em moeda comum: " + vd("i = i* + ΔE<sup>e</sup>") + ". O diferencial i − i* só compensa a "
            "depreciação esperada.",
            "Com ativos de risco diferente, o investidor exige um adicional ρ por default, conversibilidade ou "
            "instabilidade política: " + vd("i − i* = ΔE<sup>e</sup> + ρ") + ". Para a mesma expectativa "
            "cambial, o diferencial necessário é maior em ρ.",
            "Medidas usuais do " + azb("risco-país") + ": spread do EMBI+ (títulos soberanos em dólar sobre os "
            "Treasuries) e o prêmio dos CDS soberanos. No " + rx("Brasil") + ", o EMBI+ passou de 2.000 pontos "
            "em 2002, o que exigiu juros muito altos e conviveu com forte depreciação do real.",
            "Consequência de política: países com risco elevado operam com juros estruturalmente mais altos; "
            "reduzir o risco (ajuste fiscal, previsibilidade institucional) abre espaço para juros menores sem "
            "fuga de capitais.",
        ],
        "dissecando": (cz("[literalidade]") + " O item descreve o efeito de somar ρ ao lado direito da paridade. "
                       "A versão ERRADA diria que o risco-país “reduz” o diferencial necessário ou que ele "
                       "substitui a expectativa cambial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A inclusão do risco-país na paridade descoberta reduz o diferencial de juros necessário para "
            "atrair capitais.”</i> → ERRADO (inversão: o risco eleva o diferencial exigido)",
            "<i>“Com risco-país e expectativa de depreciação nulos, a paridade descoberta implica igualdade "
            "entre os juros doméstico e externo.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("A paridade descoberta iguala i a i* mais a depreciação esperada; com o risco-país, os "
                             "investidores exigem compensação adicional, e i deve superar i* mais a depreciação "
                             "esperada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: a fonte trazia o item na forma “É correto afirmar que “…”?”; mantida só a "
                    "assertiva"],
    },
    # ------------------------------------------------------------------ E1-0982
    {
        "id": "ECO-E1-0982-1", "fonte_ref": "E1-0982", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_JUROS_CAMBIO,
        "rotulo_item": "Item",
        "assertiva": ("A elevação do juro por parte do Banco Central Europeu tende a valorizar a moeda única europeia "
                      "em função de uma maior rentabilidade de ativos de renda fixa dentro da zona do euro."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A elevação do juro por parte do Banco Central Europeu <u>tende a</u> valorizar a moeda única "
                      "europeia em função de uma maior rentabilidade de ativos de renda fixa dentro da zona do "
                      "euro."),
        "poucas": ("Juro maior na zona do euro eleva o retorno dos títulos em euro, atrai capital e aumenta a "
                   "demanda pela moeda: o " + vd("euro se valoriza") + ", tudo o mais constante."),
        "destrinchando": [
            "Mesmo mecanismo de qualquer moeda: " + vd("i<sub>BCE</sub> ↑ → retorno dos ativos em euro ↑ → "
            "demanda por euros ↑ → euro se aprecia") + " (EUR/USD sobe, isto é, mais dólares por euro).",
            "O " + azb("“tende a”") + " é essencial. O que move o câmbio é o " + vd("diferencial") + " em relação "
            "aos outros bancos centrais e a surpresa diante do que o mercado já esperava. Em 2022, o BCE subiu "
            "os juros pela primeira vez em 11 anos (julho), mas o Federal Reserve subia mais rápido, e o euro "
            "chegou a cair abaixo da paridade com o dólar.",
            "Alta já precificada também não move o câmbio: os mercados reagem à mudança das expectativas. Por "
            "isso o efeito de uma decisão de juros depende tanto do comunicado (sinalização futura) quanto do "
            "número.",
            "Ressalva estrutural: o BCE define uma política única para economias heterogêneas; juros altos "
            "valorizam o euro, mas pressionam os países mais endividados da periferia (prêmios de risco "
            "soberano), tema recorrente desde a crise da dívida de 2010–2012.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Item de mecanismo básico aplicado a outro "
                       "banco central. O “tende a” protege contra as exceções (diferencial relativo, expectativas). "
                       "A versão ERRADA trocaria “valorizar” por “desvalorizar” ou poria um “necessariamente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A elevação do juro pelo Banco Central Europeu necessariamente valoriza o euro em relação ao "
            "dólar, qualquer que seja a política do Federal Reserve.”</i> → ERRADO (modulador absoluto: conta o "
            "diferencial)",
            "<i>“A elevação do juro pelo Banco Central Europeu tende a desvalorizar o euro, por encarecer o "
            "crédito na zona do euro.”</i> → ERRADO (inversão)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Verso só com o gabarito (CERTO), uma imagem não preservada e um link do Telegram.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "image (317).png", "tipo_fonte": "não identificado", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": ["texto_corrigido: retirado o rótulo “Questão 7” da assertiva"],
    },
    # ------------------------------------------------------------------ E2-L00193
    {
        "id": "ECO-E2-L00193-1", "fonte_ref": "E2-L00193", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_PPC,
        "rotulo_item": "Item",
        "assertiva": ("A relação câmbio-juros é definida quando a taxa de câmbio atual se igualar à razão da taxa de "
                      "câmbio esperada pela diferença entre as taxas de juros doméstica e internacional acrescida "
                      "de uma unidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A relação câmbio-juros é definida quando a taxa de câmbio atual se igualar à razão da taxa "
                      "de câmbio esperada pela <u>diferença entre as taxas de juros doméstica e internacional "
                      "acrescida de uma unidade</u>."),
        "poucas": ("É a " + azb("paridade descoberta") + " escrita para o câmbio corrente: " + vd("E = E<sup>e</sup> "
                   "/ [1 + (i − i*)]") + ", aproximação de E = E<sup>e</sup>·(1 + i*)/(1 + i)."),
        "destrinchando": [
            "Forma exata: aplicar R$ 1 no país rende (1 + i); converter em dólares, aplicar lá e reconverter rende "
            "(1 + i*)·E<sup>e</sup>/E. Sem arbitragem: " + vd("1 + i = (1 + i*)·E<sup>e</sup>/E") + " → "
            + vd("E = E<sup>e</sup>·(1 + i*)/(1 + i)") + ".",
            "Com juros pequenos, (1 + i)/(1 + i*) ≈ " + vd("1 + (i − i*)") + ". Daí a versão do item: o câmbio "
            "atual é o câmbio esperado dividido pela diferença de juros “acrescida de uma unidade”. A mesma "
            "aproximação gera a forma linear " + vd("i ≈ i* + (E<sup>e</sup> − E)/E") + ".",
            "Leitura econômica: com E<sup>e</sup> e i* dados, " + vd("i ↑ → denominador ↑ → E ↓") + " (apreciação "
            "imediata). Uma alta do câmbio esperado (E<sup>e</sup> ↑) deprecia o câmbio hoje: expectativas se "
            "autorrealizam no mercado de ativos.",
            "Atenção ao enquadramento: o comando fala em " + azb("PPC") + " (paridade do poder de compra), que "
            "liga câmbio a <b>preços</b>; a assertiva trata da " + azb("paridade de juros") + ", que liga câmbio "
            "a <b>juros</b>. O item é julgado pelo seu conteúdo.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item descreve a fórmula em palavras, de propósito "
                       "truncadas (“razão … pela diferença … acrescida de uma unidade”). O método é reescrever: "
                       "E = E<sup>e</sup>/(1 + i − i*). Erros típicos: inverter a razão (E = E<sup>e</sup>·(1 + "
                       "i − i*)) ou somar em vez de dividir."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a taxa de câmbio atual se iguala ao produto da taxa de câmbio esperada pela diferença entre "
            "as taxas de juros doméstica e internacional acrescida de uma unidade.”</i> → ERRADO (relação "
            "invertida: juro maior apreciaria, não depreciaria)",
            "<i>“Mantidos o câmbio esperado e os juros externos, a elevação dos juros domésticos aprecia o câmbio "
            "corrente.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Pela paridade descoberta, 1 + i = (E<sup>e</sup>/E)·(1 + i*), logo E = E<sup>e</sup>·"
                             "(1 + i*)/(1 + i): o câmbio corrente iguala o esperado dividido pela razão de juros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “paridade do poder compra” corrigido para “paridade do poder de compra” no "
                    "comando; retirado o rótulo “Questão 03 —”",
                    "nota_redacao: o comando da prova anuncia PPC, mas a assertiva trata de paridade de juros"],
    },
    # ------------------------------------------------------------------ E2-L00194
    {
        "id": "ECO-E2-L00194-1", "fonte_ref": "E2-L00194", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_PPC,
        "rotulo_item": "Item",
        "assertiva": ("A relação entre a taxa de juros e a taxa de câmbio será positiva em uma economia que adote a "
                      "cotação do incerto e regime de câmbio flutuante."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A relação entre a taxa de juros e a taxa de câmbio será ") + vm("positiva") + az(" em uma "
                    "economia que adote a cotação do incerto e regime de câmbio flutuante.")),
        "poucas": ("Na " + azb("cotação do incerto") + " (R$ por US$, a usada no Brasil), juro maior atrai capital e "
                   "faz a taxa de câmbio " + vd("cair") + ": a relação é " + vm("negativa") + "."),
        "destrinchando": [
            "Convenções de cotação: " + azb("cotação do incerto") + " (direta) fixa uma unidade de moeda "
            "estrangeira e varia a nacional — " + vd("US$ 1 = R$ 5,00") + "; é o padrão no " + rx("Brasil")
            + " e nos modelos de livro-texto (E = moeda doméstica por estrangeira). " + azb("Cotação do certo")
            + " (indireta) fixa a moeda nacional — R$ 1 = US$ 0,20; é usada, por exemplo, para a libra e o euro.",
            "Com câmbio flutuante: " + vd("i ↑ → entrada de capitais → moeda nacional se aprecia → E (R$/US$) "
            "↓") + ". Juros e câmbio andam em sentidos opostos: relação " + vd("negativa") + ".",
            "Na cotação do certo, o mesmo fenômeno aparece com sinal trocado: a moeda nacional comprando mais "
            "dólares significa número maior (US$/R$ ↑) — relação positiva. Por isso a convenção decide o sinal, "
            "e a banca a usa como armadilha.",
            "Pela paridade descoberta, " + vd("E = E<sup>e</sup>·(1 + i*)/(1 + i)") + ": com E<sup>e</sup> e i* "
            "dados, E é função decrescente de i — a mesma conclusão, agora formal.",
            "Detalhe de enquadramento: o comando fala em PPC, que relaciona câmbio e <b>preços</b>; juros e câmbio "
            "são assunto da paridade de juros.",
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item usa a convenção certa (incerto, a padrão) "
                       "com o sinal errado; a pegadinha é que, na cotação do certo, “positiva” estaria correto. "
                       "Método: traduza para R$ por US$ e pergunte se o número sobe ou cai quando o juro sobe."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A relação entre a taxa de juros e a taxa de câmbio será positiva em uma economia que adote a "
            "cotação do certo e regime de câmbio flutuante.”</i> → CERTO",
            "<i>“Sob câmbio fixo e crível, a alta dos juros domésticos aprecia a taxa de câmbio nominal.”</i> → "
            "ERRADO (câmbio fixo: o ajuste é via reservas e moeda, não via câmbio)",
        ])],
        "reescrita": ("A relação entre a taxa de juros e a taxa de câmbio será " + hl("negativa") + " em uma "
                      "economia que adote a cotação do incerto e regime de câmbio flutuante."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Com cotação do incerto (E = moeda doméstica por unidade de estrangeira), juro maior "
                             "aprecia a moeda: E cai, relação negativa. Um dos comentários empilhados troca as "
                             "definições de certo e incerto."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 019", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": ["qualidade_fonte: um dos comentários empilhados define cotação do incerto como “1 real = X "
                    "dólares” (é a cotação do certo) e por isso hesita no gabarito",
                    "nota_redacao: o comando da prova anuncia PPC, mas a assertiva trata de juros e câmbio"],
    },
    # ------------------------------------------------------------------ E2-L00221
    {
        "id": "ECO-E2-L00221-1", "fonte_ref": "E2-L00221", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_Q3,
        "rotulo_item": "Item",
        "assertiva": ("A condição de paridade de juros enfatiza que o equilíbrio internacional dos mercados cambial e "
                      "de investimentos se manifesta com base na taxa de juros exclusivamente, desconsiderando os "
                      "efeitos inflacionários."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A condição de paridade de juros enfatiza que o equilíbrio internacional dos mercados "
                       "cambial e de investimentos se manifesta com base na taxa de juros ")
                    + vm("exclusivamente, desconsiderando") + az(" os efeitos inflacionários.")),
        "poucas": ("A paridade de juros iguala retornos em moeda comum: " + vd("i = i* + ΔE<sup>e</sup>") + ". Entra "
                   "a " + azb("expectativa de variação cambial") + ", que por sua vez reflete o diferencial de "
                   "inflação esperado."),
        "destrinchando": [
            "Retorno de aplicar no exterior, medido em moeda doméstica = juro externo + variação esperada do "
            "câmbio. Por isso o equilíbrio nunca depende só dos juros: um juro alto pode ser anulado por uma "
            "depreciação esperada equivalente.",
            "Onde entra a inflação: pela " + azb("PPC relativa") + ", " + vd("ΔE<sup>e</sup> ≈ π<sup>e</sup> − "
            "π*<sup>e</sup>") + ". Substituindo na paridade descoberta: i − π<sup>e</sup> = i* − π*<sup>e</sup>, "
            "isto é, " + vd("r = r*") + " — a " + azb("paridade real de juros") + " (efeito " + oc("Fisher")
            + " internacional).",
            "Leitura: países com inflação esperada maior pagam juros nominais maiores, e suas moedas tendem a se "
            "depreciar — o diferencial nominal compensa a inflação, não é ganho real.",
            "Versões da paridade: " + azb("coberta") + " (com contrato a termo: (1 + i) = (1 + i*)·F/E, sem risco "
            "cambial) e " + azb("descoberta") + " (com o câmbio esperado). Com risco-país, soma-se ρ ao lado "
            "direito.",
            vm("Regra-âncora: paridade de juros = juros + câmbio esperado (+ risco); a inflação entra pelo câmbio "
               "esperado."),
        ],
        "dissecando": (cz("[restrição indevida]") + " O “exclusivamente” amputa da paridade justamente o termo que "
                       "a define (a variação cambial esperada), e o “desconsiderando os efeitos inflacionários” "
                       "ignora que essa expectativa carrega o diferencial de inflação. 🔥 Moduladores absolutos em "
                       "itens de paridade costumam marcar ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Combinada com a paridade do poder de compra relativa, a paridade descoberta de juros implica "
            "igualdade entre as taxas reais de juros dos dois países.”</i> → CERTO",
            "<i>“A paridade coberta de juros depende da expectativa dos agentes quanto ao câmbio futuro.”</i> → "
            "ERRADO (troca de conceito: a coberta usa a taxa a termo contratada)",
        ])],
        "reescrita": ("A condição de paridade de juros enfatiza que o equilíbrio internacional dos mercados cambial "
                      "e de investimentos se manifesta com base na taxa de juros " + hl("e na expectativa de "
                      "variação cambial, que incorpora") + " os efeitos inflacionários."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["exclusivamente"], "dificuldade": 1,
        "comentario_fonte": ("A paridade de juros considera as taxas de juros e a expectativa de desvalorização "
                             "cambial; não se baseia apenas na taxa de juros."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: retirado o rótulo “Questão 03 —” do comando"],
    },
    # ------------------------------------------------------------------ E2-L00223
    {
        "id": "ECO-E2-L00223-1", "fonte_ref": "E2-L00223", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_Q3,
        "rotulo_item": "Item",
        "assertiva": ("A condição de paridade salarial internacional pressupõe que em um sistema econômico global "
                      "equilibrado, não só os preços dos bens e as taxas de câmbio se igualam, mas também os "
                      "salários nacionais se tornam equivalentes aos salários internacionais. Esse equilíbrio "
                      "salarial global é alcançado, em teoria, pela estabilização dos mercados de trabalho, "
                      "fundamentada na harmonização da produtividade e eficiência laboral entre as nações "
                      "participantes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A condição de paridade salarial internacional pressupõe que em um sistema econômico global "
                      "equilibrado, não só os preços dos bens e as taxas de câmbio se igualam, mas também os "
                      "salários nacionais se tornam equivalentes aos salários internacionais. Esse equilíbrio "
                      "salarial global é alcançado, <u>em teoria</u>, pela estabilização dos mercados de trabalho, "
                      "fundamentada na <u>harmonização da produtividade</u> e eficiência laboral entre as nações "
                      "participantes."),
        "poucas": ("O curso dá CERTO tratando a “paridade salarial” como extensão teórica da lei do preço único: "
                   "com produtividades iguais, salários convergiriam. Mas o conceito não é consagrado e o item "
                   "mistura noções imprecisas."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "não existe, na literatura padrão, uma “condição de paridade salarial internacional” "
                          "ao lado da PPC e da paridade de juros. O resultado mais próximo é o "
                          + azb("teorema da equalização dos preços dos fatores") + " (" + oc("Samuelson") + "), "
                          "que decorre do livre-comércio sob hipóteses estritas (tecnologias idênticas, "
                          "especialização incompleta). Além disso, “taxas de câmbio se igualam” não tem sentido "
                          "econômico. A resposta mais defensável seria ERRADO; o gabarito do curso é mantido.")],
        "destrinchando": [
            azb("Lei do preço único") + " → " + azb("PPC") + ": bens comercializáveis idênticos tenderiam a "
            "custar o mesmo em moeda comum. O trabalho, porém, é pouco móvel entre países, e a arbitragem que "
            "sustenta a PPC não se aplica diretamente a ele.",
            azb("Equalização dos preços dos fatores") + " (modelo de Heckscher-Ohlin-Samuelson): o comércio de "
            "bens substitui a mobilidade dos fatores; com tecnologias iguais, o livre-comércio tende a igualar "
            "salários e rendas do capital entre países, mesmo sem migração. É um resultado teórico, "
            "empiricamente distante.",
            "Na prática, salários refletem a " + azb("produtividade do trabalho") + ": o que se equaliza, no "
            "máximo, é o salário por unidade de eficiência. Diferenças de capital, tecnologia e instituições "
            "explicam as enormes distâncias salariais entre países.",
            "Vínculo com o câmbio: pelo efeito " + oc("Balassa-Samuelson") + ", países com maior produtividade "
            "nos comercializáveis pagam salários maiores em toda a economia, o que encarece os não "
            "comercializáveis e eleva o nível de preços — por isso países ricos parecem “caros” e a PPC absoluta "
            "falha. Os salários não se igualam; o que os acompanha é a produtividade.",
        ],
        "dissecando": (cz("[outro: conceito não padrão]") + " O item é redigido com termos de aparência técnica "
                       "(“paridade”, “equilíbrio global”) e se protege com “em teoria”. O gabarito do curso se "
                       "apoia nesse modulador; numa prova CEBRASPE, a ausência de base teórica consagrada e a "
                       "frase sobre igualdade de taxas de câmbio levariam ao ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Heckscher-Ohlin-Samuelson, o livre-comércio tende a igualar as remunerações dos "
            "fatores entre países, sob tecnologias idênticas.”</i> → CERTO",
            "<i>“A paridade do poder de compra exige a livre mobilidade internacional do trabalho.”</i> → ERRADO "
            "(a PPC se apoia na arbitragem de bens, não de fatores)",
        ])],
        "tipo_erro": ["OUTRO"], "moduladores": ["em teoria"], "dificuldade": 3,
        "comentario_fonte": ("A paridade salarial internacional seria uma extensão da lógica de mercados "
                             "equilibrados: com produtividades harmonizadas, os salários se nivelariam entre "
                             "economias."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: “paridade salarial internacional” não é conceito consagrado; o mais próximo é a "
                    "equalização dos preços dos fatores (HOS), sob hipóteses estritas, e “taxas de câmbio se "
                    "igualam” não faz sentido — resposta mais defensável: ERRADO",
                    "texto_corrigido: retirado o rótulo “Questão 03 —” do comando"],
    },
    # ------------------------------------------------------------------ E2-L00224
    {
        "id": "ECO-E2-L00224-1", "fonte_ref": "E2-L00224", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_Q4,
        "rotulo_item": "Item",
        "assertiva": ("A paridade coberta de juros implica que todos os riscos cambiais associados ao investimento "
                      "internacional são neutralizados, já que variações cambiais potenciais são consideradas no "
                      "cálculo do retorno, garantindo assim uma estabilidade total no retorno sobre o "
                      "investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A paridade <u>coberta</u> de juros implica que <u>todos os riscos cambiais</u> associados ao "
                      "investimento internacional são neutralizados, já que variações cambiais potenciais são "
                      "consideradas no cálculo do retorno, garantindo assim uma estabilidade total no retorno "
                      "sobre o investimento."),
        "poucas": ("Na paridade " + azb("coberta") + ", o investidor trava hoje, com um " + azb("contrato a termo")
                   + ", o câmbio de retorno: o resultado em moeda doméstica fica " + vd("predeterminado") + " e o "
                   "risco cambial desaparece por inteiro."),
        "destrinchando": [
            "Fórmula: " + vd("(1 + i) = (1 + i*)·F/S") + ", com S = câmbio à vista e F = câmbio a termo "
            "(moeda doméstica por estrangeira). Em forma aproximada: " + vd("i − i* ≈ (F − S)/S") + " — o "
            + azb("prêmio a termo") + " iguala o diferencial de juros.",
            "Operação: converter à vista, aplicar a i* e, no mesmo instante, vender a termo o montante final a F. "
            "Nenhuma variação posterior do câmbio à vista afeta o resultado: é um ativo doméstico “sintético”.",
            "Por isso é condição de " + azb("não arbitragem") + ": se o retorno coberto superasse i, tomar "
            "emprestado em casa e aplicar fora com cobertura daria lucro sem risco, até o diferencial sumir.",
            "Contraste com a " + azb("descoberta") + ": sem contrato a termo, usa-se o câmbio esperado "
            "(i = i* + ΔE<sup>e</sup>), e o risco cambial permanece. A coberta usa preços observáveis e vale "
            "quase como identidade em mercados líquidos; a descoberta falha com frequência (o "
            "<i>forward premium puzzle</i>).",
            "Limite da “estabilidade total”: o retorno fica imune ao <b>câmbio</b>, mas restam riscos de crédito, "
            "de contraparte do contrato a termo, de conversibilidade e regulatórios. Desde 2008 há desvios "
            "persistentes da paridade coberta entre grandes moedas (" + oc("Du, Tepper e Verdelhan") + ", 2018).",
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Os absolutos (“todos”, “estabilidade total”) "
                       "induzem ao ERRADO, mas estão no recorte certo: risco <b>cambial</b>, eliminado pelo "
                       "hedge. A armadilha clássica é confundir coberta e descoberta — na descoberta o mesmo "
                       "item seria ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A paridade descoberta de juros implica que todos os riscos cambiais do investimento "
            "internacional são neutralizados.”</i> → ERRADO (troca de conceito: na descoberta não há hedge)",
            "<i>“Válida a paridade coberta, o diferencial de juros entre dois países iguala o prêmio (ou "
            "desconto) a termo da moeda.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["todos", "estabilidade total"],
        "dificuldade": 2,
        "comentario_fonte": ("A paridade coberta usa o contrato a termo: o investidor conhece desde o início a taxa de "
                             "reconversão, o retorno em moeda doméstica fica predeterminado e o risco cambial é "
                             "neutralizado; restam outros riscos (crédito, contraparte)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 022", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": ["texto_corrigido: retirado o rótulo “Questão 04 —” do comando"],
    },
    # ------------------------------------------------------------------ E2-L00225
    {
        "id": "ECO-E2-L00225-1", "fonte_ref": "E2-L00225", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_Q4,
        "rotulo_item": "Item",
        "assertiva": ("Um investidor estrangeiro só deve considerar deslocar capital para outro país se o retorno "
                      "esperado for no mínimo igual ao que poderia obter no país de origem, mesmo com todos os "
                      "possíveis riscos sendo abatidos contra suas expectativas de ganho."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um investidor estrangeiro <u>só</u> deve considerar deslocar capital para outro país se o "
                      "retorno esperado for <u>no mínimo igual</u> ao que poderia obter no país de origem, mesmo "
                      "com todos os possíveis riscos sendo abatidos contra suas expectativas de ganho."),
        "poucas": ("Regra de decisão da paridade com risco: só compensa sair se o retorno esperado lá fora, "
                   + azb("líquido dos riscos") + " (cambial, de crédito, país), for " + vd("≥") + " o retorno em "
                   "casa."),
        "destrinchando": [
            "Para o investidor de fora, aplicar no país de destino rende " + vd("i − ΔE<sup>e</sup> − ρ") + " em "
            "sua moeda (juro local, menos a depreciação esperada da moeda local, menos o prêmio pelo risco). Ele "
            "só desloca capital se isso for pelo menos " + vd("i*") + ", o juro de casa.",
            "Em equilíbrio, a igualdade vale: " + vd("i = i* + ΔE<sup>e</sup> + ρ") + " — a paridade descoberta "
            "com risco-país. Desvios desencadeiam fluxos que reequilibram câmbio e juros.",
            "“Mesmo com todos os possíveis riscos sendo abatidos” significa comparar retornos " + azb("ajustados "
            "ao risco") + ": um juro nominal alto que apenas paga o risco não atrai ninguém.",
            "Na prática, entram também custos de transação, impostos (IOF, retenção na fonte), custo do hedge e "
            "a diversificação de carteira — que pode justificar manter ativos com retorno ajustado algo menor, "
            "se reduzirem o risco total.",
        ],
        "dissecando": (cz("[contraintuitivo]") + " “Só” e “no mínimo” costumam sinalizar ERRADO, mas aqui descrevem "
                       "exatamente a condição de equilíbrio (retorno ajustado ≥ retorno doméstico). A versão "
                       "ERRADA compararia retornos nominais brutos, sem abater os riscos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Basta que a taxa de juros nominal do país de destino supere a do país de origem para que o "
            "investidor desloque seu capital.”</i> → ERRADO (ignora depreciação esperada e risco)",
            "<i>“Em equilíbrio, o juro doméstico iguala o externo acrescido da depreciação esperada e do prêmio "
            "de risco.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["só", "no mínimo", "todos"], "dificuldade": 2,
        "comentario_fonte": ("O investidor avalia não só o retorno nominal, mas os riscos cambiais, inflacionários e "
                             "de juros; o investimento só é atraente se o retorno ajustado igualar ou superar o "
                             "benchmark doméstico."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: retirado o rótulo “Questão 04 —” do comando",
                    "nota_redacao: o comentário de origem cita um retorno doméstico de 2% que não consta do "
                    "enunciado preservado; o dado foi desconsiderado"],
    },
    # ------------------------------------------------------------------ E2-L00637
    {
        "id": "ECO-E2-L00637-1", "fonte_ref": "E2-L00637", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_26,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a Paridade Descoberta dos Juros e ignorando o prêmio de risco, se a taxa de "
                      "juros nominal doméstica for maior que a externa, haverá uma expectativa de depreciação "
                      "nominal da moeda doméstica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a Paridade Descoberta dos Juros e <u>ignorando o prêmio de risco</u>, se a taxa "
                      "de juros nominal doméstica for maior que a externa, haverá uma <u>expectativa de "
                      "depreciação</u> nominal da moeda doméstica."),
        "poucas": ("Sem prêmio de risco, a paridade descoberta é " + vd("i − i* = ΔE<sup>e</sup>") + ". Se i &gt; i*, "
                   "então ΔE<sup>e</sup> &gt; 0: o mercado espera que a moeda doméstica se " + azb("deprecie")
                   + " e anule o ganho extra de juros."),
        "destrinchando": [
            "Lógica de não arbitragem: os ativos são substitutos perfeitos, então o retorno esperado em moeda "
            "comum deve ser o mesmo. Quem aplica no país de juro alto “ganha” o diferencial, mas espera perder "
            "na reconversão da moeda — e as duas coisas se compensam.",
            "Exemplo: i = 10%, i* = 4% → o mercado espera depreciação de cerca de " + vd("6%") + " da moeda "
            "doméstica no período.",
            "Aparente paradoxo: subir os juros <b>aprecia</b> a moeda hoje. As duas afirmações convivem: a "
            "alta de i derruba E imediatamente (com E<sup>e</sup> dado), e, a partir desse nível mais baixo, "
            "espera-se depreciação até E<sup>e</sup>. É a lógica do " + azb("overshooting") + " de "
            + oc("Dornbusch") + " (1976).",
            "Empiricamente a paridade descoberta falha com frequência: moedas de juro alto muitas vezes se "
            "apreciam em vez de se depreciar — é o que torna lucrativo o " + azb("carry trade") + " (o "
            "<i>forward premium puzzle</i>).",
            vm("Regra-âncora: na paridade descoberta, juro mais alto = depreciação esperada da moeda que paga "
               "mais."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O item é a leitura direta da equação, mas "
                       "contraria a intuição “juro alto valoriza a moeda”, que vale para o efeito de impacto, "
                       "não para a expectativa. A versão ERRADA troca “depreciação” por “apreciação”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se a taxa de juros nominal doméstica for maior que a externa, haverá uma expectativa de "
            "apreciação nominal da moeda doméstica.”</i> → ERRADO (inversão)",
            "<i>“Sob câmbio fixo plenamente crível e sem prêmio de risco, a paridade descoberta implica juros "
            "domésticos iguais aos externos.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["ignorando o prêmio de risco"],
        "dificuldade": 1,
        "comentario_fonte": ("Pela paridade descoberta, i = i* + E(Δe); se i &gt; i*, os investidores só ficam "
                             "indiferentes esperando depreciação da moeda doméstica que anule o ganho de juros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 099", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01233-1 (mesma assertiva em lista Nabuco de 2023)"],
    },
    # ------------------------------------------------------------------ E2-L00638
    {
        "id": "ECO-E2-L00638-1", "fonte_ref": "E2-L00638", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_26,
        "rotulo_item": "Item",
        "assertiva": ("Supondo que os títulos dos países A e B sejam substitutos perfeitos e paguem, respectivamente, "
                      "5% a.a. e 6% a.a. de taxa de juros, então o mercado de câmbio prevê implicitamente que a "
                      "moeda do país A irá se depreciar em relação à moeda do país B em 1% no próximo ano."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Supondo que os títulos dos países A e B sejam substitutos perfeitos e paguem, "
                       "respectivamente, 5% a.a. e 6% a.a. de taxa de juros, então o mercado de câmbio prevê "
                       "implicitamente que a moeda do país A irá se ") + vm("depreciar") + az(" em relação à moeda "
                       "do país B em 1% no próximo ano.")),
        "poucas": ("A moeda que paga " + azb("menos juros") + " precisa ter " + vm("apreciação") + " esperada para "
                   "compensar: ΔE<sup>e</sup> (A por B) = 5% − 6% = " + vd("−1%") + " → A se aprecia 1%."),
        "destrinchando": [
            "Do ponto de vista de A, com E = unidades de A por unidade de B: " + vd("i<sub>A</sub> = i<sub>B</sub> "
            "+ ΔE<sup>e</sup>") + " → 5% = 6% + ΔE<sup>e</sup> → " + vd("ΔE<sup>e</sup> = −1%") + ". E cai: é "
            "preciso menos moeda A por moeda B — A se " + vd("aprecia") + ".",
            "Intuição: aplicar em A rende 1 p.p. a menos. Para que alguém aceite manter títulos de A, a moeda A "
            "precisa valorizar-se cerca de 1%, de modo que o retorno total em moeda comum seja o mesmo.",
            "Se o mercado esperasse depreciação de A, aplicar em A seria duplamente pior (juro menor e perda "
            "cambial): ninguém compraria títulos de A, e a paridade estaria violada.",
            "“Substitutos perfeitos” é a hipótese que elimina o prêmio de risco e autoriza a paridade descoberta "
            "pura.",
            vm("Regra-âncora: juro maior → depreciação esperada; juro menor → apreciação esperada."),
        ],
        "dissecando": (cz("[inversão]") + " O número (1%) está certo; o sentido está invertido. O examinador conta "
                       "com quem calcula o diferencial e atribui a depreciação ao país errado. Teste: a moeda de "
                       "<b>maior</b> juro é a que se espera que deprecie."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o mercado prevê implicitamente que a moeda do país B irá se depreciar em relação à moeda do "
            "país A em cerca de 1% no próximo ano.”</i> → CERTO",
            "<i>“…prevê que a moeda do país A irá se apreciar em 11%.”</i> → ERRADO (dado alterado: somou as taxas "
            "em vez de subtrair)",
        ])],
        "reescrita": ("Supondo que os títulos dos países A e B sejam substitutos perfeitos e paguem, respectivamente, "
                      "5% a.a. e 6% a.a. de taxa de juros, então o mercado de câmbio prevê implicitamente que a "
                      "moeda do país A irá se " + hl("apreciar") + " em relação à moeda do país B em 1% no próximo "
                      "ano."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A moeda de A, que paga menos juros, deve ter expectativa de apreciação de "
                             "aproximadamente 1%: ΔE<sup>e</sup> = 5% − 6% = −1%."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 214 (E2-L01234)", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida"}],
        "alertas": ["duplicata: comentário fundido com o de E2-L01234",
                    "nota_redacao: E2-L01234 vem de outra lista Nabuco (2023); pela regra de provas diferentes, "
                    "poderia ter card próprio — a classificação o registrou como duplicata"],
    },
    # ------------------------------------------------------------------ E2-L00640
    {
        "id": "ECO-E2-L00640-1", "fonte_ref": "E2-L00640", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_26,
        "rotulo_item": "Item",
        "assertiva": ("Pela Paridade Descoberta da Taxa de Juros com mobilidade perfeita de capitais, quando um país "
                      "emergente fixa o câmbio em relação ao dólar e continua pagando uma taxa de juros doméstica, "
                      "ajustada ao risco-país, maior que a taxa de juros americana é porque o regime de câmbio fixo "
                      "não é crível."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Pela Paridade Descoberta da Taxa de Juros com mobilidade perfeita de capitais, quando um país "
                      "emergente fixa o câmbio em relação ao dólar e continua pagando uma taxa de juros doméstica, "
                      "<u>ajustada ao risco-país</u>, maior que a taxa de juros americana é porque o regime de "
                      "câmbio fixo <u>não é crível</u>."),
        "poucas": ("Com " + vd("i = i* + ρ + ΔE<sup>e</sup>") + ", um câmbio fixo crível teria ΔE<sup>e</sup> = 0. "
                   "Se, descontado o risco, o juro ainda supera o americano, o resíduo é " + azb("desvalorização "
                   "esperada") + ": o mercado não acredita na paridade."),
        "destrinchando": [
            "Decomposição do diferencial: " + vd("i − i* = ρ + ΔE<sup>e</sup>") + ". O item manda tirar ρ "
            "(“ajustada ao risco-país”). O que sobra só pode ser a expectativa de variação cambial.",
            "Se o regime fosse plenamente " + azb("crível") + ", ninguém esperaria mudança da paridade: "
            "ΔE<sup>e</sup> = 0 e i = i* + ρ. Um resíduo positivo é o prêmio que os investidores cobram pela "
            "probabilidade de " + azb("desvalorização") + " — o chamado “problema do peso”.",
            "Implicação de política: manter o câmbio fixo sem credibilidade exige juros altos, que deprimem a "
            "atividade e encarecem a dívida pública. Isso alimenta a dúvida sobre a sustentabilidade da paridade "
            "e pode acabar em ataque especulativo (modelos de crise cambial de segunda geração).",
            "Exemplos: o " + rx("Brasil") + " de 1998, com juros muito elevados para defender o câmbio "
            "administrado após a crise russa, até a flutuação de janeiro de 1999; a Argentina da "
            "conversibilidade, cujos spreads dispararam antes do colapso de 2001–2002.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O detalhe decisivo é “ajustada ao risco-país”: "
                       "eliminado ρ, sobra apenas a expectativa de desvalorização. Sem essa cláusula, o "
                       "diferencial poderia ser só prêmio de risco, e o item ficaria ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…quando um país emergente fixa o câmbio e paga juros maiores que os americanos, isso prova que "
            "o regime não é crível.”</i> → ERRADO (o diferencial pode ser só prêmio de risco)",
            "<i>“Sob câmbio fixo crível e mobilidade perfeita, o juro doméstico iguala o externo acrescido do "
            "risco-país.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["ajustada ao risco-país"], "dificuldade": 2,
        "comentario_fonte": ("Com câmbio fixo e livre mobilidade, i = i* + E(Δe) + risco; se, descontado o risco, "
                             "i continua maior, há expectativa de desvalorização: falta de credibilidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 100", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01236-1 (mesma assertiva em lista Nabuco de 2023)"],
    },
    # ------------------------------------------------------------------ E2-L01044
    {
        "id": "ECO-E2-L01044-1", "fonte_ref": "E2-L01044", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Em relação à macroeconomia aberta, julgue (C ou E) os seguintes itens.",
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a equação de paridade descoberta da taxa de juros e supondo que a taxa de câmbio "
                      "futura esperada e o prêmio de risco sejam constantes, um aumento da taxa de juros nominal "
                      "doméstica leva a uma apreciação da taxa de câmbio nominal doméstica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a equação de paridade descoberta da taxa de juros e supondo que a <u>taxa de "
                      "câmbio futura esperada e o prêmio de risco sejam constantes</u>, um aumento da taxa de juros "
                      "nominal doméstica leva a uma <u>apreciação</u> da taxa de câmbio nominal doméstica."),
        "poucas": ("Com " + vd("i = i* + (E<sup>e</sup> − E)/E + ρ") + " e E<sup>e</sup>, ρ fixos, i maior exige "
                   "depreciação esperada maior; como E<sup>e</sup> não muda, " + azb("E tem de cair hoje")
                   + ": a moeda doméstica se aprecia."),
        "destrinchando": [
            "Mecanismo de mercado: com i maior, ativos domésticos passam a render mais que os externos ajustados; "
            "investidores compram moeda doméstica para comprá-los, e o câmbio à vista cai até que a "
            "depreciação esperada dali em diante restabeleça a igualdade.",
            "Conta: E = E<sup>e</sup> / (1 + i − i* − ρ). Com E<sup>e</sup> = 5,00, i* + ρ = 5% e i subindo de "
            "8% para 10%, E vai de 5,00/1,03 ≈ " + vd("4,85") + " para 5,00/1,05 ≈ " + vd("4,76") + ".",
            "No diagrama do mercado de câmbio (" + oc("Krugman e Obstfeld") + "), o retorno dos depósitos "
            "domésticos é uma reta vertical em i; o retorno esperado dos externos, i* + (E<sup>e</sup> − E)/E, "
            "decresce em E. Juros maiores deslocam a vertical para a direita e o equilíbrio desce.",
            "As duas cláusulas são essenciais: se a alta de juros elevasse o câmbio esperado (por medo "
            "inflacionário) ou o prêmio de risco (dominância fiscal), o efeito poderia ser anulado ou "
            "invertido.",
        ],
        "grafico_verso": "ECO-E2-L01044-1-V1",
        "dissecando": (cz("[literalidade]") + " Item de estática comparativa com o “ceteris paribus” explícito "
                       "(E<sup>e</sup> e ρ constantes). A confusão provável é com a expectativa de "
                       "depreciação que a paridade associa a i alto — ela aparece justamente porque E cai hoje."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…um aumento da taxa de juros nominal doméstica leva a uma depreciação imediata da taxa de "
            "câmbio nominal doméstica.”</i> → ERRADO (inversão)",
            "<i>“Mantidos os juros, um aumento da taxa de câmbio futura esperada deprecia o câmbio à vista.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["supondo … constantes"], "dificuldade": 1,
        "comentario_fonte": ("Pela paridade descoberta, i = i* + ΔE<sup>e</sup> + prêmio de risco; com E<sup>e</sup> "
                             "e prêmio constantes, o aumento de i exige ΔE<sup>e</sup> maior, logo E cai: o câmbio "
                             "se aprecia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 179", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_corrigido: numeração “2.” retirada da assertiva"],
    },
    # ------------------------------------------------------------------ E2-L01233
    {
        "id": "ECO-E2-L01233-1", "fonte_ref": "E2-L01233", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a Paridade Descoberta dos Juros e ignorando o prêmio de risco, se a taxa de "
                      "juros nominal doméstica for maior que a externa, haverá uma expectativa de depreciação "
                      "nominal da moeda doméstica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a Paridade Descoberta dos Juros e <u>ignorando o prêmio de risco</u>, se a taxa "
                      "de juros nominal doméstica for <u>maior</u> que a externa, haverá uma expectativa de "
                      "<u>depreciação</u> nominal da moeda doméstica."),
        "poucas": ("Paridade descoberta sem risco: " + vd("(i − i*) = ΔE<sup>e</sup>") + ". Diferencial positivo ⇒ "
                   "ΔE<sup>e</sup> &gt; 0 ⇒ " + azb("depreciação esperada") + " da moeda doméstica."),
        "destrinchando": [
            "A paridade descoberta é uma condição de " + azb("indiferença") + ": o investidor só aceita o juro "
            "menor de fora se espera ganhar com a valorização da moeda estrangeira (isto é, com a depreciação "
            "da doméstica) na mesma medida.",
            "Com E em moeda doméstica por estrangeira: " + vd("ΔE<sup>e</sup> = (E<sup>e</sup> − E)/E") + ". "
            "Positivo → espera-se que o dólar fique mais caro → depreciação da moeda doméstica.",
            "Exemplo numérico: Selic de 12% e juro americano de 5%, sem prêmio de risco → depreciação esperada "
            "de cerca de " + vd("7%") + " ao ano. Na realidade brasileira, parte do diferencial é prêmio de "
            "risco, e a depreciação implícita é menor.",
            "Não confundir com o efeito de impacto de uma <b>alta</b> de juros, que aprecia a moeda hoje; a "
            "expectativa de depreciação é a trajetória a partir desse novo nível.",
        ],
        "dissecando": (cz("[literalidade]") + " Reprodução direta da equação, com a cláusula “ignorando o prêmio de "
                       "risco” para fechar a conta. Erros típicos da banca: trocar por “apreciação” ou retirar "
                       "a cláusula e afirmar que todo diferencial é depreciação esperada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela paridade descoberta com prêmio de risco positivo, todo o diferencial entre juros doméstico "
            "e externo corresponde à depreciação esperada.”</i> → ERRADO (parte do diferencial é prêmio de "
            "risco)",
            "<i>“Se a taxa de juros doméstica for menor que a externa, a paridade descoberta implica "
            "expectativa de apreciação da moeda doméstica.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["ignorando o prêmio de risco"], "dificuldade": 1,
        "comentario_fonte": "Pela paridade descoberta, (i − i*) = ΔE<sup>e</sup>; logo ΔE<sup>e</sup> &gt; 0 quando i &gt; i*.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 213", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L00637-1 (mesma assertiva em lista Nabuco de 2026)",
                    "texto_corrigido: numeração “1.” retirada da assertiva"],
    },
    # ------------------------------------------------------------------ E2-L01236
    {
        "id": "ECO-E2-L01236-1", "fonte_ref": "E2-L01236", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_23,
        "rotulo_item": "Item",
        "assertiva": ("Pela Paridade Descoberta da Taxa de Juros com mobilidade perfeita de capitais, quando um país "
                      "emergente fixa o câmbio em relação ao dólar e continua pagando uma taxa de juros doméstica, "
                      "ajustada ao risco-país, maior que a taxa de juros americana é porque o regime de câmbio fixo "
                      "não é crível."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Pela Paridade Descoberta da Taxa de Juros com mobilidade perfeita de capitais, quando um país "
                      "emergente <u>fixa o câmbio</u> em relação ao dólar e continua pagando uma taxa de juros "
                      "doméstica, <u>ajustada ao risco-país</u>, maior que a taxa de juros americana é porque o "
                      "regime de câmbio fixo não é crível."),
        "poucas": ("Câmbio fixo crível ⇒ " + vd("ΔE<sup>e</sup> = 0") + " ⇒ i = i* (+ ρ). Juro ajustado ao risco "
                   "acima de i* revela " + azb("expectativa de desvalorização") + ", isto é, falta de "
                   "credibilidade."),
        "destrinchando": [
            "Raciocínio por eliminação: na paridade " + vd("i = i* + ρ + ΔE<sup>e</sup>") + ", o item já "
            "descontou ρ. Se o regime fosse crível, ΔE<sup>e</sup> seria nulo e o juro ajustado igualaria i*. "
            "Como é maior, ΔE<sup>e</sup> &gt; 0.",
            azb("Credibilidade") + " de uma âncora cambial depende de reservas suficientes, disciplina fiscal e "
            "disposição política de aceitar juros altos e recessão para defender a paridade. Quando o mercado "
            "duvida, cobra o prêmio cambial — e o próprio custo desse prêmio pode precipitar o abandono do "
            "regime.",
            "Arranjos que buscam credibilidade máxima: " + azb("currency board") + " (Hong Kong; Argentina "
            "1991–2001) e " + azb("dolarização") + " (Equador, Panamá). Mesmo o currency board argentino "
            "conviveu com spreads crescentes antes de ruir.",
            "Ligação com a " + azb("trindade impossível") + ": câmbio fixo + mobilidade perfeita retiram a "
            "autonomia monetária; o juro doméstico fica preso a i* + ρ + prêmio cambial.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A cláusula “ajustada ao risco-país” é o que transforma "
                       "o diferencial em prova de falta de credibilidade. 🔥 Itens de paridade com câmbio fixo "
                       "testam sempre se o candidato zera a depreciação esperada no regime crível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio fixo crível e mobilidade perfeita, o país pode manter juros ajustados ao risco "
            "permanentemente acima dos americanos.”</i> → ERRADO (a arbitragem eliminaria o diferencial)",
            "<i>“Um diferencial de juros positivo sob câmbio fixo pode refletir apenas o prêmio de "
            "risco-país.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["ajustada ao risco-país"], "dificuldade": 2,
        "comentario_fonte": ("Pela paridade descoberta, i = i* + ΔE<sup>e</sup>; com regime crível, ΔE<sup>e</sup> = "
                             "0 e i = i*; como i &gt; i*, a única razão é o regime não ser crível."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00640-1 (mesma assertiva em lista Nabuco de 2026)",
                    "texto_corrigido: numeração “4.” retirada da assertiva"],
    },
    # ------------------------------------------------------------------ E2-L01239
    {
        "id": "ECO-E2-L01239-1", "fonte_ref": "E2-L01239", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "A respeito dos conceitos de macroeconomia aberta, julgue os itens a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Pela paridade descoberta da taxa de juros e supondo que não exista risco de crédito, o "
                      "investidor terá um retorno mais elevado ao comprar um título que paga uma taxa de juros mais "
                      "elevada do que teria se investisse em um título que paga uma taxa de juros menor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Pela paridade descoberta da taxa de juros e supondo que não exista risco de crédito, o "
                       "investidor ") + vm("terá um retorno mais elevado") + az(" ao comprar um título que paga uma "
                       "taxa de juros mais elevada do que teria se investisse em um título que paga uma taxa de "
                       "juros menor.")),
        "poucas": ("A paridade descoberta é justamente a condição de " + azb("retornos esperados iguais") + ": o "
                   "juro maior é compensado pela " + vd("depreciação esperada") + " da moeda do título que paga "
                   "mais."),
        "destrinchando": [
            "Equação: " + vd("i = i* + ΔE<sup>e</sup> + ρ") + ". Sem risco de crédito (ρ = 0): i − i* = "
            "ΔE<sup>e</sup>. O título doméstico rende i; o externo rende i* + ΔE<sup>e</sup> em moeda doméstica "
            "— que é exatamente i.",
            "Exemplo: título brasileiro a 10%, americano a 4%. A paridade implica depreciação esperada do real "
            "de cerca de 6%: aplicar nos EUA rende 4% + 6% ≈ " + vd("10%") + " em reais. Mesmo retorno.",
            "Se o retorno esperado fosse maior no título de juro alto, haveria arbitragem: todos comprariam esse "
            "título e venderiam o outro, apreciando a moeda dele hoje até a vantagem desaparecer.",
            "Ressalvas: a igualdade vale para o retorno <b>esperado</b>; o realizado depende do câmbio que de fato "
            "ocorrer. E, empiricamente, a paridade descoberta falha com frequência — o que dá lucro ao "
            + azb("carry trade") + ", à custa de risco de perdas bruscas.",
            vm("Regra-âncora: sob paridade descoberta, não há almoço grátis — juro alto paga depreciação "
               "esperada (e risco)."),
        ],
        "dissecando": (cz("[contradição]") + " O item contradiz a própria condição que invoca: a paridade "
                       "descoberta <b>é</b> a igualdade dos retornos esperados. O erro se esconde no senso comum "
                       "“juro maior rende mais”, que esquece a variação cambial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela paridade descoberta e sem risco de crédito, o retorno esperado em moeda comum é o mesmo "
            "para títulos com juros diferentes.”</i> → CERTO",
            "<i>“Pela paridade coberta, o investidor obtém retorno maior no título de juro mais alto mesmo após "
            "contratar o hedge cambial.”</i> → ERRADO (o prêmio a termo absorve o diferencial)",
        ])],
        "reescrita": ("Pela paridade descoberta da taxa de juros e supondo que não exista risco de crédito, o "
                      "investidor " + hl("não terá um retorno esperado mais elevado") + " ao comprar um título que "
                      "paga uma taxa de juros mais elevada do que teria se investisse em um título que paga uma "
                      "taxa de juros menor" + hl(", pois a depreciação esperada compensa o diferencial") + "."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("i = i* + ΔE<sup>e</sup> + prêmio de risco; sem prêmio, a remuneração do título "
                             "nacional equivale à do estrangeiro somada à desvalorização esperada: o retorno é o "
                             "mesmo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 216", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": ["texto_corrigido: numeração “3.” retirada da assertiva"],
    },
    # ------------------------------------------------------------------ E2-L01510
    {
        "id": "ECO-E2-L01510-1", "fonte_ref": "E2-L01510", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Se for válida a paridade coberta de juros, ao sofrer um súbito aumento do seu risco, um país "
                      "precisará elevar sua taxa de juros se quiser manter a taxa de câmbio estável."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se for válida a paridade coberta de juros, ao sofrer um súbito aumento do seu risco, um país "
                      "<u>precisará elevar</u> sua taxa de juros <u>se quiser manter a taxa de câmbio "
                      "estável</u>."),
        "poucas": ("Na paridade com risco, " + vd("i = i* + ΔE<sup>e</sup> + ρ") + ". Se ρ sobe e o país quer E "
                   "parado (sem depreciação), o ajuste tem de vir pelo " + azb("juro doméstico") + ": i ↑ na mesma "
                   "medida."),
        "destrinchando": [
            "Choque de risco: investidores passam a exigir mais para manter ativos do país. Com i inalterado, "
            "o retorno ajustado cai abaixo do externo → saída de capitais → " + vd("depreciação") + ".",
            "Para evitar a depreciação, há dois instrumentos: " + azb("subir os juros") + " (restaurar a "
            "paridade) ou " + azb("vender reservas") + " (atender à demanda por divisas). No modelo do item, a "
            "resposta é a primeira.",
            "Nota de nomenclatura: na literatura padrão, a " + azb("paridade coberta") + " compara retornos com "
            "hedge a termo — (1 + i) = (1 + i*)·F/S — e o risco que sobra é de crédito, conversibilidade ou "
            "controle de capitais (o “risco-país”). O curso usa a forma i = i* + depreciação + risco; com F "
            "acompanhando S, a conclusão é a mesma.",
            "Dilema real: elevar juros para defender o câmbio contrai a atividade e piora a dívida pública, o que "
            "pode aumentar ainda mais o risco percebido. No " + rx("Brasil") + " de 2002, com o risco-país acima "
            "de 2.000 pontos, o real se depreciou fortemente mesmo com alta da Selic.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O item é condicional (“se quiser manter a taxa "
                       "de câmbio estável”): não diz que o país deve subir juros, mas que, para segurar o câmbio, "
                       "precisa fazê-lo. A versão ERRADA inverteria (reduzir juros) ou diria que o câmbio se "
                       "aprecia com o aumento do risco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um súbito aumento do risco-país, mantidos os juros, tende a apreciar a moeda doméstica.”</i> → "
            "ERRADO (inversão: há saída de capitais e depreciação)",
            "<i>“Sem alterar os juros, o país pode conter a depreciação provocada pelo aumento do risco vendendo "
            "reservas internacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["se quiser"], "dificuldade": 2,
        "comentario_fonte": ("Aumento do risco-país pressiona a saída de capitais e a depreciação; para manter o "
                             "câmbio estável, é preciso elevar o juro doméstico e compensar o prêmio de risco."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: o curso chama de “paridade coberta” a forma i = i* + depreciação esperada + "
                    "risco; na literatura padrão essa forma é a descoberta com risco-país"],
    },
    # ------------------------------------------------------------------ E2-L01511
    {
        "id": "ECO-E2-L01511-1", "fonte_ref": "E2-L01511", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("A depreciação cambial torna os bens exportados pelo país mais baratos no exterior, favorecendo "
                      "as exportações e auxiliando no combate à inflação doméstica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A depreciação cambial torna os bens exportados pelo país mais baratos no exterior, "
                       "favorecendo as exportações e ") + vm("auxiliando no combate à") + az(" inflação "
                       "doméstica.")),
        "poucas": ("A primeira parte está certa; a segunda, não. A depreciação " + azb("encarece importados") + " e "
                   "insumos e aquece a demanda externa: é " + vm("inflacionária") + " (" + azb("pass-through")
                   + ")."),
        "destrinchando": [
            azb("Repasse cambial") + " (pass-through): a depreciação eleva em reais o preço dos bens finais "
            "importados, dos insumos importados (custos) e dos comercializáveis cotados em dólar (commodities, "
            "combustíveis, alimentos). O efeito chega aos índices de preços em semanas ou meses.",
            "Canal da demanda: exportações ↑ e importações ↓ → exportações líquidas ↑ → demanda agregada ↑ → "
            "pressão adicional sobre preços. Além disso, a demanda externa por exportáveis pode subir seu preço "
            "no mercado interno.",
            "A intensidade do repasse depende do grau de abertura, do hiato do produto, da credibilidade do "
            "banco central e da persistência esperada da depreciação: em economias com inflação ancorada, o "
            "repasse tende a ser menor.",
            "Exemplo: no " + rx("Brasil") + ", a forte depreciação do real em 2015, somada ao reajuste de preços "
            "administrados, levou o IPCA a " + vd("10,67%") + " naquele ano.",
            "Efeito sobre o saldo comercial: melhora, mas com defasagem — a " + azb("curva J") + " — e desde que "
            "valha a condição de " + oc("Marshall-Lerner") + " (soma das elasticidades-preço de X e M em módulo "
            "maior que 1).",
            vm("Regra-âncora: depreciação → exportações ↑, mas inflação ↑; apreciação → ajuda a desinflacionar."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " A 1ª parte é o efeito-competitividade, verdadeiro; o erro "
                       "foi enxertado no final, invertendo o efeito sobre preços. 🔥 Itens de câmbio costumam "
                       "juntar uma consequência certa com outra de sinal trocado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A apreciação cambial, ao baratear os importados, auxilia no combate à inflação doméstica.”</i> "
            "→ CERTO",
            "<i>“A depreciação cambial melhora imediatamente a balança comercial, independentemente das "
            "elasticidades.”</i> → ERRADO (curva J e condição de Marshall-Lerner)",
        ])],
        "reescrita": ("A depreciação cambial torna os bens exportados pelo país mais baratos no exterior, favorecendo "
                      "as exportações e " + hl("pressionando a") + " inflação doméstica."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Trecho incorreto: “auxiliando no combate à inflação doméstica”. A depreciação encarece "
                             "importações e insumos e tem efeito inflacionário (pass-through)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01554
    {
        "id": "ECO-E2-L01554-1", "fonte_ref": "E2-L01554", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_UIP,
        "rotulo_item": "Item",
        "assertiva": ("Seja a taxa de juros brasileira i = 6,5% a.a.; a taxa de juros internacional i* = 1,5%; e o "
                      "prêmio de risco-Brasil (risco de calote) igual a 3,0%. Se a paridade de juros coberta for "
                      "válida, os investidores esperam que o real esteja mais depreciado daqui 1 ano (há "
                      "expectativa de depreciação da moeda doméstica)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Seja a taxa de juros brasileira i = 6,5% a.a.; a taxa de juros internacional i* = 1,5%; e o "
                      "prêmio de risco-Brasil (risco de calote) igual a 3,0%. Se a paridade de juros coberta for "
                      "válida, os investidores <u>esperam que o real esteja mais depreciado</u> daqui 1 ano (há "
                      "expectativa de depreciação da moeda doméstica)."),
        "poucas": ("Com " + vd("i = i* + ρ + ΔE<sup>e</sup>") + ": 6,5% = 1,5% + 3,0% + ΔE<sup>e</sup> → "
                   + vd("ΔE<sup>e</sup> = 2,0%") + " &gt; 0. Há " + azb("expectativa de depreciação") + " do real."),
        "destrinchando": [
            "Decomposição do diferencial de " + vd("5 p.p.") + " (6,5% − 1,5%): " + vd("3 p.p.") + " pagam o risco "
            "de calote e " + vd("2 p.p.") + " compensam a depreciação esperada do real. Se o diferencial fosse "
            "só de 3 p.p., a depreciação esperada seria zero.",
            "Leitura: os investidores aceitam juros de 6,5% no Brasil, e não exigem mais, porque contam perder "
            "cerca de 2% na reconversão; ao mesmo tempo, não migram para fora porque o juro brasileiro paga o "
            "risco e essa perda esperada.",
            "Nota de nomenclatura: o item fala em paridade “coberta”, mas usa a equação com câmbio "
            + azb("esperado") + " e prêmio de risco — que é a " + azb("descoberta") + " ajustada ao risco (é a "
            "equação indicada no próprio comando). Na coberta estrita, (1 + i) = (1 + i*)·F/S: a diferença de "
            "juros aparece no " + azb("prêmio a termo") + " (F acima de S), que só coincide com a depreciação "
            "esperada se a descoberta também valer.",
            "Erro clássico de conta: esquecer o prêmio de risco e concluir por depreciação esperada de 5%.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de cálculo em que o examinador inclui o prêmio de risco para ver se o "
                       "candidato o desconta. O resultado positivo (2%) basta para o CERTO; uma versão ERRADA "
                       "pediria o valor exato errado (5%) ou falaria em apreciação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os investidores esperam depreciação do real de 5% em um ano.”</i> → ERRADO (dado alterado: "
            "esqueceu o prêmio de risco de 3%)",
            "<i>“Se o prêmio de risco-Brasil fosse de 6,0%, mantidos os juros, a paridade implicaria expectativa "
            "de apreciação do real.”</i> → CERTO (ΔE<sup>e</sup> = 6,5 − 1,5 − 6,0 = −1%)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("i = i* + risco + expectativa de depreciação: 6,5% = 1,5% + 3,0% + ΔE<sup>e</sup> → "
                             "ΔE<sup>e</sup> = 2,0%; há expectativa de depreciação do real."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 422", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 423", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 424", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 425", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 426", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["nota_redacao: o item diz “paridade de juros coberta”, mas aplica a forma com câmbio esperado e "
                    "risco-país (descoberta ajustada ao risco), coerente com o comando; gabarito mantido"],
    },
    # ------------------------------------------------------------------ E2-L01556
    {
        "id": "ECO-E2-L01556-1", "fonte_ref": "E2-L01556", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_UIP,
        "rotulo_item": "Item",
        "assertiva": ("As taxas de juros pagas pelos títulos brasileiros são bem superiores às taxas de juros pagas "
                      "pelos títulos americanos. Portanto, os investidores deveriam ter somente títulos brasileiros "
                      "em sua carteira."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As taxas de juros pagas pelos títulos brasileiros são bem superiores às taxas de juros "
                       "pagas pelos títulos americanos. ") + vm("Portanto,") + az(" os investidores ")
                    + vm("deveriam") + az(" ter somente títulos brasileiros em sua carteira.")),
        "poucas": ("Juro nominal maior não é retorno maior: pela paridade descoberta, o diferencial paga o "
                   + azb("risco-país") + " e a " + azb("depreciação esperada") + " do real. Não há vantagem que "
                   "justifique concentrar a carteira."),
        "destrinchando": [
            "Paridade com risco: " + vd("i<sub>BR</sub> = i<sub>EUA</sub> + ΔE<sup>e</sup> + ρ") + ". O juro "
            "brasileiro mais alto é a soma do juro americano, da desvalorização esperada do real e do prêmio por "
            "risco de crédito e de conversibilidade. Ajustados, os retornos se equivalem.",
            "Mesmo que sobrasse algum excesso de retorno, a teoria de carteiras (" + oc("Markowitz") + ") "
            "recomenda " + azb("diversificação") + ": combinar ativos imperfeitamente correlacionados reduz o "
            "risco total para um mesmo retorno esperado. Concentrar tudo num único país é ineficiente.",
            "Em crises de confiança, ativos de emergentes caem juntos e a moeda se deprecia ao mesmo tempo — a "
            "perda cambial pode superar com folga o ganho de juros de vários anos (a saída abrupta do "
            + azb("carry trade") + ").",
            "O próprio comportamento dos investidores confirma: o capital estrangeiro aplica no " + rx("Brasil")
            + " uma parte da carteira, sensível ao risco-país e às expectativas cambiais, e não migra por "
            "inteiro.",
        ],
        "dissecando": (cz("[nexo indevido · restrição indevida]") + " A premissa (juros brasileiros bem maiores) é "
                       "verdadeira; o “portanto” cria uma conclusão que não decorre dela, e o “somente” leva essa "
                       "conclusão ao extremo. 🔥 Conclusão normativa com “somente” costuma ser ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela paridade descoberta, o diferencial entre os juros brasileiros e americanos reflete a "
            "depreciação esperada do real e o prêmio de risco-Brasil.”</i> → CERTO",
            "<i>“Como os juros brasileiros superam os americanos, a paridade descoberta prevê apreciação "
            "esperada do real.”</i> → ERRADO (inversão: juro maior implica depreciação esperada)",
        ])],
        "reescrita": ("As taxas de juros pagas pelos títulos brasileiros são bem superiores às taxas de juros pagas "
                      "pelos títulos americanos. " + hl("Ainda assim,") + " os investidores " + hl("não deveriam")
                      + " ter somente títulos brasileiros em sua carteira" + hl(": o diferencial compensa o "
                      "risco-país e a depreciação esperada") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "RESTRICAO"], "moduladores": ["somente", "portanto"], "dificuldade": 1,
        "comentario_fonte": ("Trecho errado: “os investidores deveriam ter somente títulos brasileiros”. Juros "
                             "maiores compensam risco maior; investidores diversificam para otimizar risco e "
                             "retorno."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01557
    {
        "id": "ECO-E2-L01557-1", "fonte_ref": "E2-L01557", "destino": "69", "subtema": H2["par"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_UIP,
        "rotulo_item": "Item",
        "assertiva": ("Sob mobilidade perfeita de capitais, quando há expectativa de depreciação cambial, podemos "
                      "afirmar que a taxa de juros doméstica supera a taxa de juros externa acrescida do "
                      "risco-país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sob <u>mobilidade perfeita de capitais</u>, quando há expectativa de depreciação cambial, "
                      "podemos afirmar que a taxa de juros doméstica <u>supera</u> a taxa de juros externa "
                      "acrescida do risco-país."),
        "poucas": ("Da paridade " + vd("i = i* + ρ + ΔE<sup>e</sup>") + ": se ΔE<sup>e</sup> &gt; 0, então "
                   + vd("i &gt; i* + ρ") + ". O excedente sobre i* + ρ é a " + azb("compensação pela depreciação "
                   "esperada") + "."),
        "destrinchando": [
            azb("Mobilidade perfeita") + " garante que a arbitragem funcione e a paridade valha a todo momento: "
            "qualquer retorno ajustado diferente provoca fluxos imediatos até a igualdade se restabelecer.",
            "O diferencial i − i* tem duas parcelas: " + vd("ρ") + " (risco de crédito, conversibilidade, "
            "instabilidade) e " + vd("ΔE<sup>e</sup>") + " (perda cambial esperada). Com ΔE<sup>e</sup> &gt; 0, "
            "o juro doméstico precisa superar i* + ρ; com ΔE<sup>e</sup> &lt; 0 (apreciação esperada), ficaria "
            "abaixo.",
            "Exemplo: i* = 4%, ρ = 3% e depreciação esperada de 2% → i = " + vd("9%") + " &gt; 7%.",
            "Leitura de política: quando surge expectativa de depreciação (crise de confiança, incerteza "
            "política), o banco central tende a subir os juros para conter a saída de capitais — é o mesmo "
            "mecanismo visto de trás para a frente.",
        ],
        "dissecando": (cz("[literalidade]") + " Reprodução direta da equação. As pistas que a banca dá são "
                       "“mobilidade perfeita” (a paridade vale) e “acrescida do risco-país” (ρ já está no lado "
                       "direito). Uma versão ERRADA diria que, com expectativa de depreciação, o juro doméstico "
                       "fica abaixo do externo acrescido do risco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob mobilidade perfeita de capitais, quando há expectativa de apreciação cambial, a taxa de "
            "juros doméstica supera a externa acrescida do risco-país.”</i> → ERRADO (inversão: fica abaixo)",
            "<i>“Com mobilidade nula de capitais, a paridade descoberta determina o diferencial de juros.”</i> → "
            "ERRADO (sem mobilidade, não há arbitragem que imponha a paridade)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["podemos afirmar"], "dificuldade": 1,
        "comentario_fonte": ("Pela paridade descoberta, i = i* + expectativa de depreciação + risco-país; se há "
                             "expectativa de depreciação, i deve ser maior que i* + risco."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 427", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 428", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
]
