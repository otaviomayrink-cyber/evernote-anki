"""Cards do lote de redação 04 — ECO, passada 02 (notas 17: Contas Nacionais; 18: Balanço de Pagamentos)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ident": "🔄 Identidades e óticas do produto",
    "pib": "📏 PIB, PNB, RNB e conceitos derivados",
    "pm": "💲 Preços de mercado × custo de fatores",
    "real": "📊 Nominal × real e deflator",
    "scn": "🧾 SCN e tabelas",
    "bp_estr": "🏗️ Estrutura do BP (BPM6)",
    "bp_lanc": "✍️ Lançamentos",
    "bp_cn": "🔗 BP e contas nacionais",
}

CMD_NAB_2 = ("No que diz respeito à formação da renda e do produto e suas relações com a riqueza nacional, "
             "avalie o item a seguir.")
CMD_NAB_3 = "Acerca de temas de contabilidade nacional e agregados macroeconômicos, julgue o item a seguir."

CMD_ANTT_PIB = ("A tabela a seguir apresenta a quantidade dos bens finais (x, y e z) produzidos em determinado país "
                "entre os anos de 2020 e 2022. Os preços dos bens, em cada ano, são expressos em unidades monetárias "
                "($) e as quantidades são expressas em unidades. Com base nessa situação hipotética e considerando "
                "que esses são os únicos bens finais produzidos no país em questão, julgue o item a seguir.")
TAB_ANTT_PIB = {
    "titulo": "Bens finais produzidos no país, 2020–2022",
    "cabecalho": ["Ano", "Bem final", "Preço ($)", "Quantidade (unidades)"],
    "linhas": [["2020", "x", "2", "10"], ["2020", "y", "4", "15"], ["2020", "z", "1", "20"],
               ["2021", "x", "2", "15"], ["2021", "y", "3", "10"], ["2021", "z", "1", "25"],
               ["2022", "x", "3", "15"], ["2022", "y", "5", "15"], ["2022", "z", "2", "35"]],
    "fonte": "CEBRASPE, ANTT, 2023 (situação hipotética).",
}
FIG_ANTT_PIB = {"ref": "IMAGEM 170", "tipo_fonte": "TEXTO", "lado": "frente",
                "acao": "transcrita_html (tabela aninhada, 4 colunas; preços reconstituídos pelos cálculos do verso)"}
ALERTA_ANTT_PIB = ("transcricao_incoerente: a transcrição da IMAGEM 170 perdeu a coluna de preços e embaralhou as "
                   "linhas; preços (2020: 2, 4, 1; 2021: 2, 3, 1; 2022: 3, 5, 2) reconstituídos pelos cálculos "
                   "concordantes de quatro comentários do verso (PIB nominal 100, 85 e 190; PIB real 100, 95 e 125)")

CMD_ANTT_BP = ("Um país realizou, em determinado ano, as transações com o exterior apresentadas a seguir. Com fulcro "
               "nessa situação hipotética, julgue o próximo item.")
EXC_ANTT_BP = ("<p>Transações com o exterior (em bilhões de dólares):</p><ul>"
               "<li>importações de mercadorias: 5</li>"
               "<li>exportações de mercadorias: 15</li>"
               "<li>recebimento de doações na forma de mercadorias: 1</li>"
               "<li>empréstimos e financiamentos recebidos do exterior: 10</li>"
               "<li>investimento estrangeiro direto recebido do exterior, sem cobertura cambial, na forma de "
               "equipamentos: 15</li>"
               "<li>juros de empréstimos pagos ao exterior: 5</li>"
               "<li>fretes pagos ao exterior: 10</li></ul>")

CMD_NIDI_IBGE = ("O Instituto Brasileiro de Geografia e Estatística (IBGE) detalha a metodologia para registro das "
                 "transações internacionais no sistema de contas nacionais. Quanto a esse registro, julgue (C ou E) "
                 "o item a seguir.")
CMD_NIDI_CN = ("O objetivo da contabilidade nacional é analisar a evolução dos indicadores da economia de um país "
               "como um todo. A esse respeito, avalie como certo ou errado (C ou E) o item a seguir.")
CMD_NIDI_62 = ("As Contas Nacionais são fundamentais para a análise da atividade econômica e a formulação de "
               "políticas. A respeito delas, julgue o item a seguir.")
CMD_NIDI_BPM6 = ("O estudo da economia no seu nível agregado é comumente conhecido por Macroeconomia. Uma parte "
                 "importante desse campo de estudos é designada por Contabilidade Nacional, onde se estuda os "
                 "agregados macroeconômicos. A respeito da Contabilidade Nacional, tal como codificada pelo BPM6, "
                 "julgue o item a seguir (C ou E).")
CMD_NIDI_OUT = ("No contexto da contabilidade nacional, diversos conceitos sobre produto e renda são fundamentais "
                "para a compreensão da estrutura do Sistema de Contas Nacionais (SCN) de um país. A respeito desses "
                "conceitos, avalie como certo ou errado (C ou E) o item a seguir.")

CMD_BP = "Julgue o item a seguir, relativo ao balanço de pagamentos."

ALERTA_62 = ("texto_parcial: a fonte trunca o comando da Questão 62 (“…e a formulação…”); comando completado de "
             "forma neutra")

CARDS = []

# ====================================================================== bloco 1 — Nabuco (Pré-TPS/2022)
CARDS += [
    # ------------------------------------------------------------------ E2-L01332
    {
        "id": "ECO-E2-L01332-1", "fonte_ref": "E2-L01332", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_2,
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia com formação de capital, as famílias também poupam, e as empresas também "
                      "produzem e investem em bens de capital, de modo que S (poupança) equivale a I (investimento), "
                      "desde que os vazamentos se equiparem às injeções."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia com formação de capital, as famílias também poupam, e as empresas também "
                      "produzem e investem em bens de capital, de modo que <u>S (poupança) equivale a I "
                      "(investimento)</u>, desde que os vazamentos se equiparem às injeções."),
        "poucas": ("Com formação de capital, parte da renda não consumida (" + azb("vazamento") + ": S) volta ao "
                   "fluxo como gasto em bens de capital (" + azb("injeção") + ": I). Fechado o período, "
                   + vd("S ≡ I") + " é identidade contábil."),
        "destrinchando": [
            "Economia fechada e sem governo: pela ótica da renda, Y = C + S; pela ótica da despesa, Y = C + I. "
            "Igualando, " + vd("S = I") + ". A parcela da renda que as famílias não consomem é exatamente o valor "
            "da produção que não foi para consumo — e essa produção é, por definição, investimento.",
            "A igualdade é " + azb("ex post") + " (realizada): vale sempre nas contas fechadas, porque a "
            + azb("variação de estoques") + " entra no investimento. Se as famílias poupam mais do que as empresas "
            "planejavam investir, sobra mercadoria na prateleira, o estoque sobe e o investimento realizado "
            "acompanha a poupança.",
            "Ex ante (planejado), S e I são decididos por agentes diferentes e podem divergir. Para " + oc("Keynes")
            + ", a diferença se resolve pelo ajuste da renda (multiplicador); para os clássicos, pela taxa de juros.",
            "Generalização: com governo e setor externo, vazamentos = S + T + M e injeções = I + G + X; a "
            "identidade vira " + vd("I = S<sub>privada</sub> + (T − G) + S<sub>externa</sub>") + ".",
            "Ressalva de leitura: a igualdade contábil não diz que a poupança de um período financie o investimento "
            "daquele mesmo período, nem quem causa quem.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O “desde que” sugere uma condição que poderia "
                       "falhar, mas, ex post, vazamentos e injeções sempre se igualam — o item continua verdadeiro. "
                       "🔥 A banca alterna “identidade ex post” (CERTO) e “ex ante” (ERRADO)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A igualdade entre poupança e investimento é uma identidade ex ante, válida para os valores "
            "planejados pelos agentes.”</i> → ERRADO (troca ex post por ex ante)",
            "<i>“Numa economia aberta, o investimento pode superar a poupança doméstica, financiado por poupança "
            "externa.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["desde que"], "dificuldade": 1,
        "comentario_fonte": ("S = I é identidade contábil a posteriori; vazamentos retornam como injeções, sem que "
                             "toda a poupança se destine ao investimento no mesmo período."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01333
    {
        "id": "ECO-E2-L01333-1", "fonte_ref": "E2-L01333", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("Os gastos das empresas públicas e sociedades de economia mista, por atuarem no mercado como "
                      "empresas privadas, são considerados no setor de produção, junto com estas últimas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os gastos das empresas públicas e sociedades de economia mista, <u>por atuarem no mercado "
                      "como empresas privadas</u>, são considerados no setor de produção, junto com estas últimas."),
        "poucas": ("As contas nacionais classificam as unidades pela " + azb("natureza da atividade") + ", não pela "
                   "propriedade: estatal que vende a preços de mercado é " + azb("empresa") + ", não governo."),
        "destrinchando": [
            "O critério é ser " + azb("produtor mercantil") + ": vender bens e serviços a preços economicamente "
            "significativos, cobrindo custos com receita de vendas. Petrobras, Banco do Brasil ou Correios fazem "
            "isso — logo ficam com as empresas privadas.",
            "No SCN atual (padrão " + oc("SNA 2008") + "), isso aparece nos " + azb("setores institucionais")
            + ": as estatais entram em " + vd("sociedades não financeiras") + " ou " + vd("sociedades financeiras")
            + "; o " + azb("governo geral") + " reúne só as unidades que produzem serviços não mercantis (saúde, "
            "educação, defesa) financiados por tributos.",
            "Consequência prática: o gasto de uma estatal com insumos é consumo intermediário de empresa, e a "
            "compra de máquinas é FBCF de empresa; não entra em G (consumo do governo).",
            "Nas estatísticas fiscais do " + rx("Brasil") + ", a fronteira reaparece: o resultado primário do "
            "“setor público consolidado” inclui estatais, mas exclui as instituições financeiras públicas e o grupo "
            "Petrobras (e, até a privatização de 2022, a Eletrobras), de comportamento tipicamente empresarial.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a regra do manual. A armadilha é o candidato associar "
                       "“pública” a governo e marcar ERRADO; a justificativa no próprio item (“por atuarem no "
                       "mercado como empresas privadas”) é a pista."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por pertencerem ao Estado, as empresas públicas têm seus gastos computados no consumo final do "
            "governo.”</i> → ERRADO (critério é a atividade, não a propriedade)",
            "<i>“Hospitais públicos que atendem gratuitamente integram o setor governo nas contas nacionais.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "As contas nacionais consideram o tipo de atividade econômica, e não a propriedade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01334
    {
        "id": "ECO-E2-L01334-1", "fonte_ref": "E2-L01334", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("O produto nacional pode ser avaliado a preços de mercado (PNpm) e a custo de fatores (PNcf). "
                      "Aquele avalia o preço pago pelo consumidor final, ao passo que este reflete os custos de "
                      "produção e não considera impostos indiretos nem subsídios."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O produto nacional pode ser avaliado a preços de mercado (PNpm) e a custo de fatores (PNcf). "
                      "Aquele avalia o preço pago pelo consumidor final, ao passo que este reflete os custos de "
                      "produção e <u>não considera impostos indiretos nem subsídios</u>."),
        "poucas": ("A custo de fatores, o produto mede só a " + azb("remuneração dos fatores") + "; a preços de "
                   "mercado, inclui a cunha fiscal: " + vd("PNpm = PNcf + impostos indiretos − subsídios") + "."),
        "destrinchando": [
            "O preço que o consumidor paga embute impostos indiretos (ICMS, IPI): eles encarecem o bem sem "
            "remunerar nenhum fator. Já o " + azb("subsídio") + " barateia o bem, mas o produtor recebe o preço "
            "cheio — a diferença é paga pelo governo e remunera os fatores.",
            "Por isso: " + vd("PNcf = PNpm − impostos indiretos + subsídios") + ", ou, no sentido inverso, "
            + vd("PNpm = PNcf + impostos indiretos − subsídios") + ". Os subsídios entram com sinal "
            "<b>contrário</b> ao dos impostos.",
            "A mesma passagem vale para qualquer agregado: PIB, PIL, PNB, PNL. A renda nacional, em sentido "
            "estrito, é o " + azb("PNL a custo de fatores") + " (salários + juros + aluguéis + lucros).",
            "No SCN brasileiro, a distinção moderna é entre " + azb("preços básicos") + " (o que o produtor "
            "recebe, sem impostos e com subsídios sobre produtos) e preços de mercado; a ótica da renda separa "
            "ainda os “impostos sobre a produção e importação”.",
            vm("Regra-âncora: de custo de fatores para preços de mercado, soma impostos e subtrai subsídios."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição de manual com os pronomes “aquele/este” para "
                       "testar atenção à ordem. 🔥 A variante errada típica troca os sinais (somar subsídios para "
                       "chegar a preços de mercado)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PNpm equivale ao PNcf acrescido dos impostos indiretos e dos subsídios.”</i> → ERRADO (os "
            "subsídios se subtraem)",
            "<i>“Num país sem impostos indiretos e sem subsídios, PNpm e PNcf coincidem.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PNpm medido pelos valores de mercado; PNcf reflete custos de produção e remuneração "
                             "dos fatores; “PNpm = PNcf + impostos indiretos + subsídios”."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem diz que o PNpm é o PNcf “acrescido dos impostos "
                    "indiretos e dos subsídios”; os subsídios se subtraem — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L01335
    {
        "id": "ECO-E2-L01335-1", "fonte_ref": "E2-L01335", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("O produto nacional divide-se em nominal e real. O primeiro é medido a preços correntes (PNN), "
                      "ao passo que o segundo, a preços constantes (PNR). Consequentemente, o deflator consiste na "
                      "equação: PNR = PNN/índice de preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O produto nacional divide-se em nominal e real. O primeiro é medido a preços correntes (PNN), "
                      "ao passo que o segundo, a preços constantes (PNR). Consequentemente, o deflator consiste na "
                      "equação: <u>PNR = PNN/índice de preços</u>."),
        "poucas": ("" + azb("Deflacionar") + " é dividir o valor nominal por um índice de preços: "
                   + vd("real = nominal ÷ deflator") + ", o que equivale a " + vd("deflator = nominal ÷ real") + "."),
        "destrinchando": [
            azb("Produto nominal") + ": quantidades do ano × preços do próprio ano (preços correntes). "
            + azb("Produto real") + ": quantidades do ano × preços de um ano-base (preços constantes). O real "
            "isola a variação de volume; o nominal mistura volume e preço.",
            azb("Deflator implícito") + " = nominal ÷ real (× 100, se expresso em base 100). Ele é “implícito” "
            "porque não é coletado diretamente: resulta das duas medidas do produto. No ano-base, vale "
            + vd("1 (ou 100)") + ".",
            "Rearranjando: " + vd("real = nominal ÷ deflator") + " — exatamente a equação do item. Se o índice "
            "estiver em base 100, divide-se por índice/100.",
            "Diferença para o " + azb("IPCA") + ": o deflator cobre todos os bens e serviços finais produzidos no "
            "país (inclusive investimento e exportações) e tem ponderação variável; o IPCA mede uma cesta fixa de "
            "consumo, inclusive importados.",
            "Em taxas: (1 + g<sub>nominal</sub>) = (1 + g<sub>real</sub>) × (1 + π<sub>deflator</sub>), ou, "
            "aproximadamente, " + vd("g<sub>nominal</sub> ≈ g<sub>real</sub> + π") + ".",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. O ponto sensível é a direção da divisão: "
                       "o nominal vai no numerador. Quem inverte (real = índice ÷ nominal) erra a variante "
                       "fabricada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O deflator do PIB é a razão entre o PIB real e o PIB nominal.”</i> → ERRADO (razão invertida)",
            "<i>“No ano-base, o PIB nominal e o PIB real são iguais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PNN a preços correntes; PNR com ano-base; deflator = PIB nominal/PIB real, medida "
                             "de inflação."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01336
    {
        "id": "ECO-E2-L01336-1", "fonte_ref": "E2-L01336", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB_3,
        "rotulo_item": "Item",
        "assertiva": ("O investimento bruto é sempre positivo, mas o investimento líquido pode ser negativo, caso a "
                      "taxa de juros seja superior ao equilíbrio de mercado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O investimento bruto é sempre positivo, mas o investimento líquido pode ser negativo, caso ")
                    + vm("a taxa de juros seja superior ao equilíbrio de mercado") + az(".")),
        "poucas": ("" + azb("Investimento líquido") + " = investimento bruto − " + azb("depreciação")
                   + ". Ele fica negativo quando a depreciação supera o investimento bruto — juros não entram na "
                   "conta."),
        "destrinchando": [
            "Investimento bruto (FBC) = FBCF + variação de estoques: tudo o que se acrescentou ao estoque de "
            "capital no período. Parte disso só repõe o que se desgastou — o " + azb("consumo de capital fixo")
            + " (depreciação).",
            vd("I<sub>líquido</sub> = I<sub>bruto</sub> − depreciação") + ". Se a economia investe menos do que o "
            "necessário para repor o desgaste, o estoque de capital <b>encolhe</b> e o investimento líquido é "
            "negativo — típico de guerras, depressões longas ou países em colapso.",
            "A taxa de juros afeta a <b>decisão</b> de investir (juro alto → menos projetos viáveis → I bruto "
            "menor), mas não define o sinal do investimento líquido. Ela pode contribuir indiretamente, se derrubar "
            "o investimento bruto abaixo da depreciação — e é essa comparação que decide.",
            "Ressalva sobre o “sempre positivo”: a FBCF não é negativa, mas a variação de estoques pode ser; em "
            "rigor, a FBC poderia ficar negativa com grande desacumulação de estoques. Como regra de prova, aceita-se "
            "o investimento bruto como não negativo.",
            "A mesma lógica liga os agregados brutos e líquidos: " + vd("PIL = PIB − depreciação") + ".",
        ],
        "dissecando": (cz("[nexo indevido]") + " A primeira parte é a regra do manual; o erro foi enxertado na "
                       "condição, que troca a variável contábil decisiva (depreciação) por uma variável "
                       "comportamental (juros). Pista: “equilíbrio de mercado” não aparece em identidades "
                       "contábeis."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O investimento líquido será negativo sempre que a depreciação superar o investimento bruto.”</i> "
            "→ CERTO",
            "<i>“O investimento líquido é negativo quando o investimento bruto é inferior à poupança.”</i> → "
            "ERRADO (a comparação é com a depreciação)",
        ])],
        "reescrita": ("O investimento bruto é sempre positivo, mas o investimento líquido pode ser negativo, caso "
                      + hl("a depreciação seja superior ao investimento bruto") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["sempre", "pode"], "dificuldade": 1,
        "comentario_fonte": ("Investimento líquido = bruto − depreciação; negativo se a depreciação supera o "
                             "investimento bruto."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]

# ====================================================================== bloco 2 — CEBRASPE ANTT/2023
CARDS += [
    # ------------------------------------------------------------------ E3-L00161
    {
        "id": "ECO-E3-L00161-1", "fonte_ref": "E3-L00161", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_ANTT_PIB,
        "excerto_tabela": TAB_ANTT_PIB,
        "rotulo_item": "Item",
        "assertiva": "A preços de 2020, o deflator implícito do PIB, em 2021, foi maior que 0,9.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A preços de 2020, o deflator implícito do PIB, em 2021, foi ") + vm("maior") + az(" que 0,9."),
        "poucas": ("PIB nominal de 2021 = " + vd("85") + "; PIB real de 2021 a preços de 2020 = " + vd("95")
                   + ". " + azb("Deflator") + " = 85 ÷ 95 ≈ " + vd("0,895") + " — abaixo de 0,9."),
        "destrinchando": [
            azb("PIB nominal") + " de 2021 = quantidades de 2021 × preços de 2021: 15 × 2 + 10 × 3 + 25 × 1 = "
            "30 + 30 + 25 = " + vd("85") + ".",
            azb("PIB real") + " de 2021 (base 2020) = quantidades de 2021 × preços de 2020: 15 × 2 + 10 × 4 + "
            "25 × 1 = 30 + 40 + 25 = " + vd("95") + ".",
            azb("Deflator implícito") + " = nominal ÷ real = 85 ÷ 95 = " + vd("0,8947") + " (ou 89,47 em base "
            "100). Como é menor que 1, houve " + azb("deflação") + " de cerca de 10,5% entre 2020 e 2021: o bem y "
            "caiu de 4 para 3, e x e z ficaram estáveis.",
            "Conferência dos outros anos: no ano-base (2020), nominal = real = " + vd("100") + " e o deflator é "
            "1; em 2022, nominal = 3 × 15 + 5 × 15 + 2 × 35 = 190 e real = 2 × 15 + 4 × 15 + 1 × 35 = 125, "
            "deflator ≈ " + vd("1,52") + ".",
            "Roteiro para tabelas de PIB: (1) monte duas colunas, nominal (p<sub>t</sub> × q<sub>t</sub>) e real "
            "(p<sub>base</sub> × q<sub>t</sub>); (2) some por ano; (3) divida. As quantidades são sempre as do ano "
            "em análise; só os preços mudam.",
            vm("Regra-âncora: deflator = PIB nominal ÷ PIB real; abaixo de 1, os preços caíram em relação ao ano-base."),
        ],
        "dissecando": (cz("[dado alterado]") + " Item de cálculo com limiar apertado: 0,8947 fica a um passo de "
                       "0,9, e quem arredonda cedo (85/95 ≈ 0,9) marca CERTO. Outra pegadinha: usar as quantidades "
                       "de 2020 no PIB real de 2021."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Entre 2020 e 2021, o nível geral de preços da economia, medido pelo deflator implícito do PIB, "
            "caiu.”</i> → CERTO",
            "<i>“Em 2021, o PIB real, a preços de 2020, foi inferior ao PIB nominal.”</i> → ERRADO (inversão: real "
            "95 > nominal 85)",
        ])],
        "reescrita": ("A preços de 2020, o deflator implícito do PIB, em 2021, foi " + hl("menor") + " que 0,9."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Quatro resoluções concordantes: PIB nominal 2021 = 85; PIB real 2021 (preços de "
                             "2020) = 95; deflator = 0,8947 < 0,9; houve deflação. Tabela-resumo com os três anos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_ANTT_PIB,
                          {"ref": "IMAGEM 171-175", "tipo_fonte": "FÓRMULA/TABELA/TEXTO", "lado": "verso",
                           "acao": "absorvidas (contas e tabela-resumo levadas ao 📖)"}],
        "alertas": [ALERTA_ANTT_PIB],
    },
    # ------------------------------------------------------------------ E3-L00162
    {
        "id": "ECO-E3-L00162-1", "fonte_ref": "E3-L00162", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_PIB,
        "excerto_tabela": TAB_ANTT_PIB,
        "rotulo_item": "Item",
        "assertiva": ("O PIB real, a preços de 2020, aumentou mais de 30% entre os anos de 2021 e 2022, ao passo que "
                      "o PIB nominal, no mesmo período, aumentou mais de 100%."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O PIB real, a preços de 2020, aumentou <u>mais de 30%</u> entre os anos de 2021 e 2022, ao "
                      "passo que o PIB nominal, no mesmo período, aumentou <u>mais de 100%</u>."),
        "poucas": ("PIB real: 95 → 125 (" + vd("+31,6%") + "). PIB nominal: 85 → 190 (" + vd("+123,5%")
                   + "). As duas partes passam dos limiares."),
        "destrinchando": [
            azb("PIB real") + " (preços de 2020): 2021 = 2 × 15 + 4 × 10 + 1 × 25 = " + vd("95") + "; 2022 = "
            "2 × 15 + 4 × 15 + 1 × 35 = " + vd("125") + ". Variação: 125 ÷ 95 − 1 = " + vd("31,6%") + ".",
            azb("PIB nominal") + " (preços de cada ano): 2021 = 2 × 15 + 3 × 10 + 1 × 25 = " + vd("85")
            + "; 2022 = 3 × 15 + 5 × 15 + 2 × 35 = " + vd("190") + ". Variação: 190 ÷ 85 − 1 = "
            + vd("123,5%") + ".",
            "A diferença entre as duas taxas é o " + azb("deflator") + ": de 0,895 (2021) para 1,52 (2022), alta "
            "de cerca de 70%. Confere: 1,316 × 1,70 ≈ 2,235 = 190/85.",
            "Atalho para limiares: em vez de calcular a taxa, multiplique a base. 95 × 1,3 = 123,5 < 125 → "
            "passou de 30%; 85 × 2 = 170 < 190 → passou de 100%.",
            "Atenção ao padrão de item composto: “ao passo que” liga duas afirmações, e as duas precisam ser "
            "verdadeiras para o CERTO.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de cálculo duplo; a banca escolhe limiares próximos do resultado "
                       "(31,6% × 30%) para punir arredondamento e cobra a disciplina de usar preços fixos de 2020 "
                       "no real e preços correntes no nominal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB real, a preços de 2020, aumentou mais de 35% entre 2021 e 2022.”</i> → ERRADO (dado "
            "alterado: 31,6%)",
            "<i>“Entre 2021 e 2022, a variação do deflator implícito superou a variação do PIB real.”</i> → CERTO "
            "(≈ 70% × 31,6%)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["mais de"], "dificuldade": 2,
        "comentario_fonte": ("PIB real 95 → 125 (+31,58%); PIB nominal 85 → 190 (+123,53%); ambas as partes "
                             "corretas. Tabela-resumo e simulação dos limiares."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [FIG_ANTT_PIB,
                          {"ref": "IMAGEM 173, 176-179", "tipo_fonte": "TABELA/TEXTO", "lado": "verso",
                           "acao": "absorvidas (contas levadas ao 📖)"}],
        "alertas": [ALERTA_ANTT_PIB],
    },
    # ------------------------------------------------------------------ E3-L00163
    {
        "id": "ECO-E3-L00163-1", "fonte_ref": "E3-L00163", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_ANTT_BP,
        "excerto": EXC_ANTT_BP,
        "rotulo_item": "Item",
        "assertiva": "No período em apreço, o produto nacional bruto do país foi inferior ao produto interno bruto.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No período em apreço, o produto nacional bruto do país foi <u>inferior</u> ao produto "
                      "interno bruto."),
        "poucas": ("PNB = PIB − " + azb("renda líquida enviada ao exterior") + ". Na lista, a única renda de "
                   "fator é o pagamento de " + vd("juros (5)") + ": RLEE = 5 > 0, logo " + vd("PNB < PIB") + "."),
        "destrinchando": [
            vd("PNB = PIB + rendas recebidas do exterior − rendas enviadas ao exterior") + ". Só entram as "
            "rendas de fatores — no BP, a conta de " + azb("renda primária") + ": salários, juros, lucros e "
            "dividendos.",
            "Classificando a lista: importações (5) e exportações (15) → balança comercial; fretes (10) → "
            "serviços; doações (1) → " + azb("renda secundária") + "; empréstimos (10) e IED (15) → conta "
            "financeira. Nenhum desses altera a diferença entre PIB e PNB.",
            "Sobra " + vd("juros pagos = 5") + ": renda enviada 5, recebida 0 → " + vd("PNB = PIB − 5") + ".",
            "Erro comum: somar a doação recebida à renda (RLEE = 5 − 1 = 4). Transferências unilaterais não "
            "remuneram fatores; afetam a " + azb("renda nacional disponível bruta") + " (RNDB = RNB + "
            "transferências correntes líquidas), não o PNB. Aqui o erro não muda o gabarito, mas muda a conta.",
            "Caso do " + rx("Brasil") + ": a renda primária é estruturalmente deficitária (juros, lucros e "
            "dividendos remetidos superam os recebidos), por isso a RNB brasileira costuma ficar abaixo do PIB.",
        ],
        "dissecando": (cz("[detalhe]") + " A tabela é recheada de distratores de valor alto (IED 15, "
                       "exportações 15, fretes 10) para quem confunde fluxo comercial ou financeiro com renda. O "
                       "julgamento depende de achar o único item de renda primária."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A renda líquida enviada ao exterior no período foi de US$ 4 bilhões.”</i> → ERRADO (doação é "
            "renda secundária: RLEE = 5)",
            "<i>“A renda nacional disponível bruta foi inferior ao PIB em US$ 4 bilhões.”</i> → CERTO (−5 de "
            "renda primária + 1 de renda secundária)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("PNB = PIB − RLEE; só juros (5) são renda de fator; exportações, doações, empréstimos, "
                             "IED e fretes não entram. Uma resolução calcula RLEE = 4, somando a doação."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 180", "tipo_fonte": "TEXTO", "lado": "frente",
                           "acao": "texto (tabela de 2 colunas transcrita como lista no excerto)"},
                          {"ref": "IMAGEM 181-186", "tipo_fonte": "FÓRMULA/TEXTO/TABELA", "lado": "verso",
                           "acao": "absorvidas (classificação das transações levada ao 📖)"}],
        "alertas": ["qualidade_fonte: duas resoluções de origem calculam RLEE = 4, tratando a doação (renda "
                    "secundária) como renda de fator; o correto é RLEE = 5 — corrigido (gabarito inalterado)"],
    },
]

# ====================================================================== bloco 3 — Nidi/Jacqueline Bueno, Simulado Março/2025
CARDS += [
    # ------------------------------------------------------------------ E3-L00238
    {
        "id": "ECO-E3-L00238-1", "fonte_ref": "E3-L00238", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_IBGE,
        "rotulo_item": "Item",
        "assertiva": "As importações de bens, detalhadas por produtos, são avaliadas a preços CIF.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As importações de bens, <u>detalhadas por produtos</u>, são avaliadas a preços <u>CIF</u>."),
        "poucas": ("No SCN do IBGE, o quadro de importações " + azb("por produto") + " usa o valor " + vd("CIF")
                   + " (mercadoria + frete + seguro até a fronteira do importador); só o " + azb("total")
                   + " de bens é depois ajustado para FOB."),
        "destrinchando": [
            azb("FOB") + " (<i>free on board</i>): valor da mercadoria posta a bordo na fronteira do país "
            "exportador. " + azb("CIF") + " (<i>cost, insurance and freight</i>): FOB + frete + seguro "
            "internacionais, isto é, o valor na fronteira do país importador. CIF − FOB = frete + seguro.",
            "Por que CIF no detalhamento por produto: é a base das estatísticas aduaneiras (a Receita Federal "
            "registra a declaração de importação em CIF, que é também a base do imposto de importação) e é o "
            "custo do bem para quem o usa internamente — o que interessa para a oferta de cada produto na tabela "
            "de recursos e usos.",
            "No fechamento, o IBGE faz o " + azb("ajuste CIF/FOB") + ": deduz globalmente fretes e seguros do "
            "total de bens, que passa a ser registrado " + vd("FOB") + "; a parte prestada por não residentes "
            "vira importação de <b>serviços</b>, e a prestada por residentes já está na produção doméstica.",
            "A frase do item reproduz a " + oc("Nota Metodológica nº 2 do SCN (IBGE, referência 2010)") + ", "
            "anexo sobre o ajuste CIF/FOB.",
            "No " + azb("balanço de pagamentos") + " (BPM6), bens são registrados FOB nas exportações e nas "
            "importações; frete e seguro vão para a conta de serviços.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Cópia do manual do IBGE. A armadilha é o candidato "
                       "lembrar que “importação no BP é FOB” e marcar ERRADO sem perceber o qualificador "
                       "“detalhadas por produtos”. 🔥 O mesmo bloco costuma cobrar a outra metade: o total "
                       "registrado FOB."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No Sistema de Contas Nacionais, o total da importação de bens é registrado a preços CIF.”</i> → "
            "ERRADO (o total é ajustado para FOB)",
            "<i>“A diferença entre os valores CIF e FOB de uma importação corresponde aos fretes e seguros "
            "internacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Item copiado do anexo 2 da Nota Metodológica nº 2 do SCN (IBGE); várias respostas de "
                             "IA sobre CIF × FOB, base aduaneira e ajuste para FOB no total."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 326", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (definições CIF/FOB e referência ao IBGE levadas ao 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00239
    {
        "id": "ECO-E3-L00239-1", "fonte_ref": "E3-L00239", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_IBGE,
        "rotulo_item": "Item",
        "assertiva": ("Todos os serviços de transporte e de seguro relativos à importação, prestados por produtores "
                      "residentes e não residentes e incluídos no valor CIF da importação por produtos, são "
                      "globalmente deduzidos. Então, no Sistema de Contas Nacionais, o total da importação de bens é "
                      "sempre registrado a preços FOB."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("<u>Todos</u> os serviços de transporte e de seguro relativos à importação, prestados por "
                      "produtores residentes e não residentes e incluídos no valor CIF da importação por produtos, "
                      "são globalmente deduzidos. Então, no Sistema de Contas Nacionais, o total da importação de "
                      "bens é <u>sempre</u> registrado a preços <u>FOB</u>."),
        "poucas": ("O detalhe por produto vem em CIF; uma " + azb("dedução global") + " retira todo frete e seguro "
                   "embutidos, e o " + azb("total") + " de bens fica " + vd("FOB") + ". Os absolutos (“todos”, "
                   "“sempre”) estão no próprio manual."),
        "destrinchando": [
            "Mecânica do " + azb("ajuste CIF/FOB") + " na tabela de recursos e usos do IBGE: (1) cada produto "
            "importado entra em CIF; (2) uma linha de ajuste subtrai, de uma vez, todos os fretes e seguros "
            "internacionais incluídos nesses valores; (3) o total de bens resulta FOB.",
            "Destino do que foi deduzido: se o transporte ou o seguro foi prestado por " + azb("não residente")
            + ", o valor é registrado como importação de <b>serviços</b>; se por " + azb("residente") + " (navio "
            "de bandeira nacional, seguradora brasileira), já está na produção doméstica de transporte e seguro — "
            "mantê-lo dentro da importação de bens seria " + vd("dupla contagem") + ".",
            "Por que “residentes e não residentes”: o valor CIF embute o frete independentemente de quem o "
            "prestou; a dedução precisa ser total para que o bem fique valorado na fronteira do exportador, como "
            "nas exportações.",
            "Coerência com o " + azb("BPM6") + ": no balanço de pagamentos, bens também são FOB nos dois sentidos, "
            "e frete e seguro estão em serviços. Assim, a importação de bens do SCN e a do BP são comparáveis.",
            "A frase é a cópia do item (B) do anexo sobre o ajuste CIF/FOB da " + oc("Nota Metodológica nº 2 do "
            "SCN (IBGE, referência 2010)") + ".",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " “Todos” e “sempre” fazem o candidato farejar "
                       "modulador absoluto e marcar ERRADO, mas aqui eles são a regra do manual. Lição de C/E: "
                       "absoluto não é erro automático — confira se a regra admite exceção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Apenas os fretes e seguros prestados por não residentes são deduzidos do valor CIF das "
            "importações.”</i> → ERRADO (restrição indevida: deduzem-se todos)",
            "<i>“Os fretes deduzidos que foram prestados por não residentes são registrados como importação de "
            "serviços.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["todos", "sempre"], "dificuldade": 2,
        "comentario_fonte": ("Item copiado do item (B) do anexo 2 da Nota Metodológica nº 2 do SCN (IBGE); respostas "
                             "de IA sobre dedução global, dupla contagem e realocação de fretes."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 326-327", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (referência ao IBGE e mecânica do ajuste levadas ao 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00241
    {
        "id": "ECO-E3-L00241-1", "fonte_ref": "E3-L00241", "destino": "17", "subtema": H2["scn"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_IBGE,
        "rotulo_item": "Item",
        "assertiva": ("As transferências sociais em espécie correspondem aos bens e serviços individuais fornecidos "
                      "gratuitamente, ou a preços simbólicos, pelo governo ou por instituições sem fins de lucro a "
                      "serviço das famílias, às famílias."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As transferências sociais em espécie correspondem aos bens e serviços <u>individuais</u> "
                      "fornecidos gratuitamente, ou a preços simbólicos, pelo governo ou por instituições sem fins "
                      "de lucro a serviço das famílias, às famílias."),
        "poucas": ("" + azb("Transferências sociais em espécie") + " = bens e serviços " + vd("individuais")
                   + " e não mercantis (SUS, escola pública, merenda) que o governo e as ISFLSF entregam às "
                   "famílias de graça ou a preço simbólico."),
        "destrinchando": [
            "Transferência em espécie ≠ transferência monetária: no Bolsa Família, a família recebe dinheiro e "
            "decide o que comprar (é renda); na consulta do SUS, recebe diretamente o serviço.",
            "“Individual” é a chave: o serviço tem um beneficiário identificável (aluno, paciente). Serviços "
            + azb("coletivos") + " — defesa, segurança pública, administração geral — beneficiam a todos ao "
            "mesmo tempo e ficam como consumo coletivo do governo.",
            "Para que serve: o SCN distingue " + azb("despesa de consumo final") + " (quem paga) de "
            + azb("consumo final efetivo") + " (quem usufrui). O consumo efetivo das famílias = despesa das "
            "famílias + transferências sociais em espécie; correspondentemente, a " + azb("renda disponível "
            "ajustada") + " das famílias soma essas transferências à renda disponível.",
            "Isso permite comparar países com sistemas diferentes: onde saúde e educação são públicas, o consumo "
            "das famílias “em dinheiro” parece menor, mas o efetivo não.",
            "ISFLSF = " + azb("instituições sem fins de lucro a serviço das famílias") + " (igrejas, ONGs, "
            "associações filantrópicas) — um dos setores institucionais do SCN.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição do manual do SCN. Variantes erradas costumam trocar "
                       "“individuais” por “coletivos”, incluir transferências em dinheiro ou excluir as ISFLSF."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os serviços de defesa nacional prestados pelo governo integram as transferências sociais em "
            "espécie às famílias.”</i> → ERRADO (troca de conceito: consumo coletivo)",
            "<i>“O consumo final efetivo das famílias inclui as transferências sociais em espécie recebidas.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Bens e serviços não mercantis individuais providos pelo governo e pelas ISFLSF, que "
                             "elevam o consumo efetivo das famílias; exemplos (SUS, educação, merenda); renda "
                             "disponível ajustada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00245
    {
        "id": "ECO-E3-L00245-1", "fonte_ref": "E3-L00245", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Março/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_CN,
        "rotulo_item": "Item",
        "assertiva": "No cálculo da poupança externa, não se incluem aumentos ou diminuições das reservas cambiais do país.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No cálculo da poupança externa, <u>não se incluem</u> aumentos ou diminuições das reservas "
                      "cambiais do país."),
        "poucas": ("" + azb("Poupança externa") + " = déficit em " + azb("transações correntes") + " (acima da "
                   "linha). A variação de reservas é " + vd("financiamento") + " desse saldo (conta financeira), "
                   "não parte dele."),
        "destrinchando": [
            "Da ótica da despesa: Y = C + I + G + X − M. Separando a renda nacional, chega-se a "
            + vd("I = S<sub>privada</sub> + S<sub>governo</sub> + S<sub>externa</sub>") + ", com "
            + vd("S<sub>externa</sub> = −(saldo em transações correntes)") + " = M − X + renda líquida enviada − "
            "transferências líquidas recebidas.",
            "Transações correntes = balança comercial + serviços + renda primária + renda secundária. Nenhum "
            "desses itens é reserva.",
            "As " + azb("reservas internacionais") + " ficam na " + azb("conta financeira") + " (ativos de "
            "reserva). Pela identidade do BP, TC + conta capital + conta financeira (sem reservas) + erros e "
            "omissões = Δreservas: a variação de reservas é a forma como o saldo foi coberto.",
            "Exemplo: déficit corrente de US$ 10 bi. Se entraram US$ 10 bi de IED, as reservas não mudam; se "
            "entraram só 4, o Banco Central vende 6 de reservas. Nos dois casos, a poupança externa é a mesma: "
            + vd("10") + ". Incluir as reservas zeraria o segundo caso e esconderia que o país absorveu mais do "
            "que produziu.",
            "No " + rx("Brasil") + ", a poupança externa aparece no SCN como " + azb("necessidade de "
            "financiamento") + " da economia na conta do resto do mundo.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Item que separa “acima da linha” (TC = poupança externa) "
                       "de “abaixo da linha” (reservas = financiamento). Quem associa reservas a “recursos "
                       "externos” marca ERRADO. 🔥 O mesmo item circula em provas desde 2013."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A poupança externa corresponde ao resultado global do balanço de pagamentos, que inclui a variação "
            "das reservas.”</i> → ERRADO (troca de conceito: é o saldo em transações correntes)",
            "<i>“Um déficit em transações correntes pode ser financiado pela redução das reservas "
            "internacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Várias respostas de IA: poupança externa = −saldo em TC; reservas são ativo da conta "
                             "financeira e forma de financiar o saldo; exemplos numéricos. Uma resposta isolada "
                             "conclui “incorreta”, contra a indicação principal e o gabarito."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 341-345", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (identidades, exemplo e esquema das contas levados ao 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0382-1 (mesma assertiva, item de 2013 sem banca identificada; o "
                    "simulado reaproveita o item)",
                    "qualidade_fonte: uma das respostas do verso (IMAGEM 345) dá o item como incorreto; descartada"],
    },
]

# ====================================================================== bloco 4 — Nidi/Jacqueline Bueno, Fevereiro/2025 (Questão 62)
CARDS += [
    # ------------------------------------------------------------------ E3-L00278
    {
        "id": "ECO-E3-L00278-1", "fonte_ref": "E3-L00278", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_62,
        "rotulo_item": "Item",
        "assertiva": ("A diferença entre o produto nacional (PN) e o produto interno (PI) é dada pela renda líquida do "
                      "exterior. Se a renda enviada ao exterior for maior que a renda recebida do exterior, então: "
                      "PI > PN."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A diferença entre o produto nacional (PN) e o produto interno (PI) é dada pela renda líquida "
                      "do exterior. Se a renda enviada ao exterior for maior que a renda recebida do exterior, "
                      "então: <u>PI > PN</u>."),
        "poucas": ("" + vd("PN = PI + renda recebida − renda enviada") + ". Se se envia mais do que se recebe, a "
                   "renda líquida do exterior é negativa e o produto nacional fica " + vd("abaixo") + " do interno."),
        "destrinchando": [
            azb("Produto interno") + " (critério territorial): tudo o que se produz dentro das fronteiras, por "
            "fatores nacionais ou estrangeiros. " + azb("Produto nacional") + " (critério de residência): o que "
            "remunera os fatores pertencentes a residentes, onde quer que atuem.",
            "A ponte é a " + azb("renda líquida de fatores externos") + " — no BP, o saldo da " + azb("renda "
            "primária") + " (salários, juros, lucros e dividendos). Duas convenções equivalentes: PN = PI + RLRE "
            "(renda líquida <b>recebida</b>) ou " + vd("PN = PI − RLEE") + " (renda líquida <b>enviada</b>).",
            "Com renda enviada > recebida: RLEE > 0 (ou RLRE < 0) → " + vd("PN < PI") + ". O valor gerado "
            "internamente é maior do que o apropriado pelos residentes, porque parte sai como juros e lucros a "
            "estrangeiros.",
            "É o caso típico de economias com muito capital estrangeiro e dívida externa, como o " + rx("Brasil")
            + ", onde a RNB fica abaixo do PIB; Irlanda e Luxemburgo são casos extremos do mesmo fenômeno "
            "(sedes de multinacionais), e países com muitos ativos no exterior podem ter RNB > PIB.",
            vm("Regra-âncora: interno = território; nacional = residência; a diferença é só a renda primária."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Regra de manual com conclusão algébrica. A armadilha é a "
                       "convenção de sinais: quem mistura RLEE e RLRE inverte a desigualdade. Sempre traduza para "
                       "“envio mais do que recebo → nacional menor”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a renda enviada ao exterior superar a recebida, o produto nacional será maior que o "
            "interno.”</i> → ERRADO (inversão)",
            "<i>“Doações recebidas do exterior elevam o produto nacional bruto.”</i> → ERRADO (renda secundária: "
            "afeta a renda disponível, não o PNB)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PNB = PIB − RLEE; renda enviada > recebida → RLEE > 0 → PIB > PNB; caso típico do "
                             "Brasil. Algumas respostas usam RLEE com sinal trocado na definição."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 384", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (fórmulas levadas ao 📖)"}],
        "alertas": [ALERTA_62],
    },
    # ------------------------------------------------------------------ E3-L00279
    {
        "id": "ECO-E3-L00279-1", "fonte_ref": "E3-L00279", "destino": "17", "subtema": H2["real"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_62,
        "rotulo_item": "Item",
        "assertiva": "A taxa de crescimento do PIB real é sempre igual ou menor do que a taxa de crescimento do PIB nominal.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A taxa de crescimento do PIB real é ") + vm("sempre") + az(" igual ou menor do que a taxa "
                    "de crescimento do PIB nominal.")),
        "poucas": ("" + vd("g<sub>nominal</sub> ≈ g<sub>real</sub> + variação do deflator") + ". Com "
                   + azb("deflação") + " (deflator em queda), o PIB real cresce " + vd("mais") + " que o nominal."),
        "destrinchando": [
            "PIB nominal = quantidades × preços correntes; PIB real = quantidades × preços do ano-base. O nominal "
            "varia por volume e por preço; o real, só por volume.",
            "Relação exata: (1 + g<sub>N</sub>) = (1 + g<sub>R</sub>) × (1 + π), em que π é a variação do "
            + azb("deflator implícito") + ". Se π > 0, g<sub>N</sub> > g<sub>R</sub>; se " + vd("π < 0")
            + ", g<sub>R</sub> > g<sub>N</sub>; se π = 0, são iguais.",
            "Exemplo: volume +3% e deflação de 2% → nominal ≈ +1%. Ou ainda: o PIB nominal pode até cair enquanto "
            "o real sobe.",
            "Casos reais de deflator negativo: " + azb("Japão") + " em boa parte dos anos 1990–2000; economias "
            "exportadoras de commodities em anos de queda de preços (o deflator inclui exportações). Na prática "
            "brasileira, com inflação positiva, o nominal costuma crescer mais — daí a tentação do “sempre”.",
            "Detalhe técnico: o deflator pode cair mesmo sem queda do IPCA, porque mede todos os bens finais "
            "produzidos no país (inclusive exportações e investimento), não a cesta do consumidor.",
        ],
        "dissecando": (cz("[modulador absoluto]") + " Descreve o caso usual (inflação positiva) e o transforma "
                       "em regra com “sempre”. Em C/E, absoluto sobre variável que pode trocar de sinal (inflação, "
                       "juro real, saldo externo) quase sempre é o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Havendo deflação no período, a taxa de crescimento do PIB real supera a do PIB nominal.”</i> → "
            "CERTO",
            "<i>“O PIB nominal nunca pode cair se o PIB real estiver crescendo.”</i> → ERRADO (modulador absoluto: "
            "deflação forte o derruba)",
        ])],
        "reescrita": ("A taxa de crescimento do PIB real é <s>sempre</s> " + hl("geralmente") + " igual ou menor do "
                      "que a taxa de crescimento do PIB nominal" + hl(", mas a supera quando há deflação") + "."),
        "tipo_erro": ["GENERALIZACAO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("ΔPIB nominal ≈ ΔPIB real + inflação; com deflação, o real cresce mais que o nominal; "
                             "o “sempre” torna o item falso (ex.: Japão nos anos 1990)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 385", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (relação entre as taxas levada ao 📖)"}],
        "alertas": [ALERTA_62],
    },
    # ------------------------------------------------------------------ E3-L00280
    {
        "id": "ECO-E3-L00280-1", "fonte_ref": "E3-L00280", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI_62,
        "rotulo_item": "Item",
        "assertiva": ("Para fins de registro nas Contas Nacionais, o investimento é qualquer gasto em bem ou serviço "
                      "final que aumente a capacidade da economia de produzir mais no futuro."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para fins de registro nas Contas Nacionais, o investimento é ")
                    + vm("qualquer gasto em bem ou serviço final que aumente a capacidade da economia de produzir "
                         "mais no futuro") + az(".")),
        "poucas": ("Nas contas nacionais, investimento é a " + azb("formação bruta de capital") + ": "
                   + vd("FBCF + variação de estoques") + ". Gastos que ampliam a capacidade futura sem gerar ativo "
                   "fixo — educação, saúde, treinamento — são " + azb("consumo") + "."),
        "destrinchando": [
            azb("FBCF") + ": aquisição de ativos fixos produzidos, usados repetidamente na produção por mais de um "
            "ano — máquinas e equipamentos, construções (inclusive residenciais e obras públicas) e "
            + azb("produtos de propriedade intelectual") + " (software, exploração mineral e, pelo " + oc("SNA 2008")
            + ", P&amp;D). Somada à " + azb("variação de estoques") + ", forma a FBC (o “I” de C + I + G + X − M).",
            "O que <b>não</b> é investimento, embora pareça: curso de pós-graduação (consumo das famílias); "
            "salário de professor da rede pública (consumo do governo); treinamento de pessoal (consumo "
            "intermediário da empresa); compra de ações ou de imóvel usado (transação financeira ou troca de "
            "ativo existente); terreno (ativo não produzido).",
            "A ideia de " + azb("capital humano") + " (" + oc("Becker") + ", " + oc("Schultz") + ") trata a "
            "educação como investimento em sentido econômico; a contabilidade nacional não a capitaliza, por falta "
            "de um ativo separável e mensurável.",
            "Também é consumo, não investimento, o bem durável das famílias (carro, geladeira) — exceção: imóvel "
            "residencial novo, que é FBCF.",
            vm("Regra-âncora: no SCN, investimento = FBCF + Δestoques; “aumentar a capacidade futura” não basta."),
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " O “qualquer” e o “bem ou serviço” trocam "
                       "a definição contábil (ativo fixo produzido) pela ideia econômica ampla de investimento. "
                       "Pista: “para fins de registro nas Contas Nacionais” pede o conceito operacional."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A construção de um hospital público é registrada como formação bruta de capital fixo.”</i> → CERTO",
            "<i>“Os gastos das famílias com educação superior são contabilizados como investimento.”</i> → ERRADO "
            "(consumo final)",
        ])],
        "reescrita": ("Para fins de registro nas Contas Nacionais, o investimento é " + hl("a formação bruta de "
                      "capital: o gasto em ativos fixos produzidos (FBCF) mais a variação de estoques") + "."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["qualquer"], "dificuldade": 2,
        "comentario_fonte": ("Investimento = FBCF + variação de estoques; educação, saúde e treinamento são consumo; "
                             "quadro comparativo do que é e do que não é investimento; várias respostas de IA "
                             "concordantes."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 386-393", "tipo_fonte": "FÓRMULA/TEXTO", "lado": "verso",
                           "acao": "absorvidas (definição e quadro comparativo levados ao 📖)"}],
        "alertas": [ALERTA_62],
    },
    # ------------------------------------------------------------------ E3-L00281
    {
        "id": "ECO-E3-L00281-1", "fonte_ref": "E3-L00281", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI_62,
        "rotulo_item": "Item",
        "assertiva": ("O Produto Interno Líquido a Custo de Fatores de um país é calculado subtraindo-se a "
                      "depreciação e os impostos indiretos líquidos de subsídios do Produto Interno Bruto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Produto Interno Líquido a Custo de Fatores de um país é calculado subtraindo-se a "
                      "<u>depreciação</u> e os <u>impostos indiretos líquidos de subsídios</u> do Produto Interno "
                      "Bruto."),
        "poucas": ("Dois ajustes independentes: " + azb("bruto → líquido") + " tira a depreciação; "
                   + azb("mercado → custo de fatores") + " tira os impostos indiretos líquidos de subsídios. "
                   + vd("PILcf = PIBpm − depreciação − (II − Sub)") + "."),
        "destrinchando": [
            "Três eixos de qualificação dos agregados: " + azb("interno × nacional") + " (renda líquida do "
            "exterior), " + azb("bruto × líquido") + " (depreciação) e " + azb("preços de mercado × custo de "
            "fatores") + " (impostos indiretos − subsídios). Cada passo mexe em um só eixo.",
            "Passo 1: PIBpm − depreciação = " + vd("PILpm") + ". Passo 2: PILpm − (impostos indiretos − "
            "subsídios) = " + vd("PILcf") + ". A ordem não importa: as subtrações comutam.",
            "“Impostos indiretos líquidos de subsídios” = impostos indiretos − subsídios. Subtrair esse líquido "
            "equivale a <b>tirar</b> os impostos e <b>somar</b> os subsídios — coerente com o fato de que o "
            "subsídio remunera fatores sem passar pelo preço.",
            "Mais um passo, agora no eixo interno × nacional: PILcf − RLEE = " + vd("PNLcf") + ", a "
            + azb("renda nacional") + " em sentido estrito (salários + juros + aluguéis + lucros).",
            "Por que o PIB a preços de mercado é a medida usual: " + oc("Leda Paulani") + " observa que a produção "
            "que repõe o capital desgastado também consumiu fatores e gerou renda (daí o bruto) e que o que se "
            "arrecada em impostos indiretos líquidos também é valor adicionado (daí os preços de mercado).",
        ],
        "dissecando": (cz("[literalidade]") + " Item de “passagem” entre agregados: a banca empilha dois ajustes "
                       "na mesma frase e aposta que o candidato se confunda com o sinal dos subsídios. "
                       "“Líquidos de subsídios” já resolve o sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIL a custo de fatores é obtido subtraindo-se do PIB a depreciação e os impostos indiretos e "
            "somando-se a renda líquida enviada ao exterior.”</i> → ERRADO (a renda do exterior muda o eixo interno "
            "× nacional, não entra no PIL)",
            "<i>“A diferença entre o PIB e o PIL corresponde à depreciação do estoque de capital.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("PIBpm − depreciação = PILpm; PILpm − (impostos indiretos − subsídios) = PILcf; trecho "
                             "de Paulani sobre a preferência pelo PIB bruto a preços de mercado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 394", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (argumento de Paulani levado ao 📖)"}],
        "alertas": [ALERTA_62],
    },
]

# ====================================================================== bloco 5 — Nidi/Jacqueline Bueno (sem data)
ALERTA_BPM6 = ("nota_redacao: o comando da fonte atribui a contabilidade nacional ao BPM6, que é o manual do balanço "
               "de pagamentos; o SCN segue o SNA 2008. Mantido por fidelidade; não afeta o julgamento")

CARDS += [
    # ------------------------------------------------------------------ E3-L00309
    {
        "id": "ECO-E3-L00309-1", "fonte_ref": "E3-L00309", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": True,
        "comando": CMD_NIDI_BPM6,
        "rotulo_item": "Item",
        "assertiva": ("O conceito do Excedente Operacional Bruto pode ser compreendido como a remuneração do capital, "
                      "gerada no processo de formação do produto de uma economia. É esse excedente que, em conjunto "
                      "com a remuneração dos empregados, compõem o Produto Interno Bruto a custo de fatores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O conceito do Excedente Operacional Bruto pode ser compreendido como a <u>remuneração do "
                      "capital</u>, gerada no processo de formação do produto de uma economia. É esse excedente que, "
                      "em conjunto com a remuneração dos empregados, compõem o <u>Produto Interno Bruto a custo de "
                      "fatores</u>."),
        "poucas": ("Pela " + azb("ótica da renda") + ", o PIB a custo de fatores reparte-se entre trabalho "
                   "(" + vd("remuneração dos empregados") + ") e capital (" + vd("excedente operacional bruto")
                   + "); somando os impostos líquidos sobre produção e importação, chega-se ao PIB a preços de "
                   "mercado."),
        "destrinchando": [
            "Na " + azb("conta de geração da renda") + " do SCN, o PIB é distribuído em: remuneração dos "
            "empregados (salários + contribuições sociais) + " + azb("excedente operacional bruto") + " + "
            + azb("rendimento misto bruto") + " + impostos líquidos de subsídios sobre a produção e a importação. "
            "Tirando os impostos, sobra a remuneração dos fatores: o PIB a custo de fatores.",
            "O EOB é um " + azb("saldo") + ": o que sobra do valor adicionado depois de pagar o trabalho e os "
            "impostos. Ele remunera o capital em sentido amplo — lucros, juros, aluguéis — e é “bruto” porque "
            "ainda contém a depreciação.",
            "Nuance: o " + azb("rendimento misto") + " é a renda dos autônomos e das empresas familiares sem "
            "contabilidade separada, em que não se distingue o que é salário e o que é lucro. Muitos manuais o "
            "tratam junto do EOB (“EOB e rendimento misto”), e é assim que o item se sustenta: capital + trabalho "
            "esgotam a remuneração dos fatores.",
            "Exemplo das contas de um exercício: PIB 4.440 = remuneração dos empregados 2.216 + impostos líquidos "
            "694 + rendimento misto 284 + EOB " + vd("1.246") + ". PIB a custo de fatores = 4.440 − 694 = "
            + vd("3.746") + ".",
            "No " + rx("Brasil") + ", o peso do rendimento misto é relevante por causa da informalidade e do "
            "trabalho por conta própria.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Definição de manual, com o rendimento misto "
                       "subentendido no excedente. A leitura “falta o RMB, então está errado” é excessiva para "
                       "o padrão do item; o que a banca testa é a ótica da renda e o custo de fatores."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O excedente operacional bruto, somado à remuneração dos empregados, compõe o PIB a preços de "
            "mercado.”</i> → ERRADO (faltam os impostos líquidos de subsídios)",
            "<i>“O excedente operacional bruto inclui o consumo de capital fixo.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Ótica da renda: PIBcf = remuneração dos empregados + EOB + rendimento misto; esquema "
                             "das contas econômicas integradas e conta de geração da renda com números; uma resposta "
                             "chama o item de “parcialmente correto” pela omissão do rendimento misto."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 432", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (esquema das contas do SCN; conteúdo resumido no 📖)"},
                          {"ref": "IMAGEM 433-436", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas (conta de geração da renda e números levados ao 📖)"}],
        "alertas": [ALERTA_BPM6],
    },
    # ------------------------------------------------------------------ E3-L00310
    {
        "id": "ECO-E3-L00310-1", "fonte_ref": "E3-L00310", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NIDI_BPM6,
        "rotulo_item": "Item",
        "assertiva": ("A identidade que se estabelece entre a poupança nacional e o investimento nacional é ex-ante, "
                      "não demonstrando uma relação de causalidade entre as variáveis."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A identidade que se estabelece entre a poupança nacional e o investimento nacional é ")
                    + vm("ex-ante") + az(", não demonstrando uma relação de causalidade entre as variáveis.")),
        "poucas": ("S ≡ I é identidade " + azb("ex post") + " (valores realizados). Ex ante (planejados), S = I é "
                   "só uma " + azb("condição de equilíbrio") + ", que pode não se verificar."),
        "destrinchando": [
            "Economia fechada sem governo: " + vd("Y = C + S") + " (destino da renda) e " + vd("Y = C + I")
            + " (destino do produto) → S = I. Vale por definição contábil, depois de fechado o período.",
            "O que garante a identidade é a " + azb("variação de estoques") + ": se as famílias poupam mais do que "
            "as empresas planejavam investir, a produção encalha, o estoque sobe, e esse “investimento "
            "involuntário” iguala, ex post, o investimento à poupança.",
            "Ex ante, poupança (famílias) e investimento (empresas) são decididos por agentes distintos. A "
            "diferença é o motor do ajuste: em " + oc("Keynes") + ", a renda se ajusta (o investimento gera, "
            "via " + azb("multiplicador") + ", a poupança que o financia); nos " + oc("clássicos") + ", a taxa de "
            "juros equilibra oferta e demanda de fundos.",
            "A segunda parte do item está certa: identidade contábil não revela causalidade — se é a poupança que "
            "permite o investimento ou o contrário é questão de teoria, não de contabilidade.",
            vm("Regra-âncora: identidade = ex post; equilíbrio = ex ante."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca-se um único termo técnico (ex post → ex ante) e "
                       "mantém-se o resto correto, inclusive a observação sobre causalidade, que dá ar de "
                       "sofisticação. Pista: “identidade” não combina com “ex ante”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No plano ex ante, a igualdade entre poupança e investimento é condição de equilíbrio, e não "
            "identidade.”</i> → CERTO",
            "<i>“A identidade S = I prova que a poupança determina o investimento.”</i> → ERRADO (nexo indevido: "
            "identidade não mostra causalidade)",
        ])],
        "reescrita": ("A identidade que se estabelece entre a poupança nacional e o investimento nacional é "
                      + hl("ex-post") + ", não demonstrando uma relação de causalidade entre as variáveis."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Identidade S = I é ex post, garantida pela variação de estoques; ex ante é condição de "
                             "equilíbrio; clássicos × keynesianos; esquema Y = C + S = C + I (Dornbusch)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 437", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (identidades levadas ao 📖)"}],
        "alertas": [ALERTA_BPM6],
    },
    # ------------------------------------------------------------------ E3-L00311
    {
        "id": "ECO-E3-L00311-1", "fonte_ref": "E3-L00311", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NIDI_BPM6,
        "rotulo_item": "Item",
        "assertiva": ("A Renda Nacional Bruta representa um conceito semelhante ao do Produto Interno Bruto e "
                      "discriminam duas das três possíveis óticas, ou formas, existentes de medir a riqueza "
                      "econômica de um país: produto, dispêndio e renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Renda Nacional Bruta representa um conceito semelhante ao do Produto Interno Bruto e ")
                    + vm("discriminam duas das") + az(" três possíveis óticas, ou formas, existentes de medir a "
                    "riqueza econômica de um país: produto, dispêndio e renda.")),
        "poucas": ("PIB e RNB são " + azb("agregados") + ", não " + azb("óticas") + ". As três óticas (produto, "
                   "despesa, renda) são métodos que chegam ao mesmo PIB; a RNB difere do PIB pela " + vd("renda "
                   "primária líquida") + " do exterior, não pelo método."),
        "destrinchando": [
            "As três óticas medem o <b>mesmo</b> agregado por caminhos diferentes: " + azb("produto") + " (soma "
            "dos valores adicionados), " + azb("despesa") + " (C + I + G + X − M) e " + azb("renda") + " "
            "(remuneração dos empregados + EOB + rendimento misto + impostos líquidos). Por construção, as três "
            "dão o mesmo PIB.",
            "O que distingue PIB e RNB é o critério: " + vd("território") + " (PIB) × " + vd("residência")
            + " (RNB). " + vd("RNB = PIB + rendas primárias recebidas − enviadas ao exterior") + ". A RNB é o "
            "novo nome, no SNA 1993/2008, do antigo PNB.",
            "Armadilha de vocabulário: “renda nacional” não é a “ótica da renda”. Pela ótica da renda mede-se o "
            "PIB (renda interna); para chegar à renda nacional ainda é preciso somar a renda líquida do exterior.",
            "Os conceitos são “semelhantes” no sentido de que " + azb("produto ≡ renda") + ": todo valor produzido "
            "vira renda de alguém. Produto interno = renda interna; produto nacional = renda nacional.",
            "Para o " + rx("Brasil") + ", a RNB fica abaixo do PIB porque a renda primária é deficitária "
            "(remessas de juros, lucros e dividendos).",
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira oração é defensável; o erro é transformar dois "
                       "agregados em “óticas” — sugerindo PIB = ótica do produto e RNB = ótica da renda. A "
                       "concordância falha (“discriminam”) não decide o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB pode ser mensurado pelas óticas do produto, da despesa e da renda, que conduzem ao mesmo "
            "valor.”</i> → CERTO",
            "<i>“A RNB é o PIB medido pela ótica da renda.”</i> → ERRADO (troca de conceito: a RNB acrescenta a "
            "renda líquida do exterior)",
        ])],
        "reescrita": ("A Renda Nacional Bruta representa um conceito semelhante ao do Produto Interno Bruto e "
                      + hl("nenhum dos dois corresponde a uma das") + " três possíveis óticas, ou formas, existentes "
                      "de medir a riqueza econômica de um país: produto, dispêndio e renda."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("PIB e RNB são agregados (território × residência), não óticas; as três óticas são "
                             "métodos equivalentes de medir o PIB; produto = renda; erro de concordância "
                             "apontado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 438", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (produto = renda; interno × nacional levados ao 📖)"}],
        "alertas": [ALERTA_BPM6],
    },
    # ------------------------------------------------------------------ E3-L00312
    {
        "id": "ECO-E3-L00312-1", "fonte_ref": "E3-L00312", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": CMD_NIDI_BPM6,
        "rotulo_item": "Item",
        "assertiva": ("Considerando uma economia com governo em um contexto no qual existe comércio internacional, o "
                      "investimento agregado dessa economia deve ser igual ao somatório das seguintes variáveis nos "
                      "seus respectivos níveis agregados: poupança privada, poupança pública e poupança externa."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando uma economia com governo em um contexto no qual existe comércio internacional, "
                      "o investimento agregado dessa economia deve ser igual ao somatório das seguintes variáveis "
                      "nos seus respectivos níveis agregados: <u>poupança privada, poupança pública e poupança "
                      "externa</u>."),
        "poucas": ("Identidade da economia aberta com governo: " + vd("I = S<sub>p</sub> + S<sub>g</sub> + "
                   "S<sub>e</sub>") + ". O investimento é financiado pela poupança das famílias e empresas, pelo "
                   "saldo do governo e pela poupança do resto do mundo."),
        "destrinchando": [
            "Derivação: Y = C + I + G + (X − M) e, pelo lado da renda, Y = C + S<sub>p</sub> + T. Igualando: "
            "I = S<sub>p</sub> + " + vd("(T − G)") + " + " + vd("(M − X)") + ".",
            azb("Poupança privada") + " = Y − T − C. " + azb("Poupança pública") + " = T − G (receitas correntes "
            "menos despesas correntes; negativa quando há déficit corrente). " + azb("Poupança externa") + " = "
            "déficit em transações correntes (M − X, mais a renda líquida enviada ao exterior e menos as "
            "transferências recebidas, se a renda for nacional).",
            "Leitura de política: com investimento dado, um déficit público maior precisa ser coberto por mais "
            "poupança privada ou por mais déficit externo — a lógica dos " + azb("déficits gêmeos") + " "
            "(EUA nos anos 1980).",
            "Como identidade, vale ex post e não diz quem causa quem: uma alta do investimento pode “gerar” a "
            "poupança via renda (" + oc("Keynes") + ") ou atrair poupança externa.",
            "⏳ (out/2026) No " + rx("Brasil") + ", a taxa de investimento gira em torno de 16%–17% do PIB, e a "
            "poupança doméstica fica alguns pontos abaixo; a diferença é a poupança externa (déficit em "
            "transações correntes). Séries no IBGE (SCN trimestral) e no BCB.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a identidade de manual. O “deve ser igual” não é "
                       "condição de equilíbrio, mas identidade contábil — e por isso o item é CERTO sem ressalvas. "
                       "Variantes erradas tiram uma das três parcelas ou trocam poupança externa por saldo "
                       "comercial positivo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Numa economia aberta com governo, um superávit em transações correntes significa poupança "
            "externa positiva.”</i> → ERRADO (inversão: poupança externa positiva = déficit)",
            "<i>“Mantidos o investimento e a poupança privada, um aumento do déficit público corresponde a um "
            "aumento da poupança externa.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["deve"], "dificuldade": 1,
        "comentario_fonte": ("Derivação I = Sp + Sg + Se a partir de Y = C + I + G + X − M; contas da renda e da "
                             "acumulação com números; dados aproximados do Brasil."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 439", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (identidade levada ao 📖)"},
                          {"ref": "IMAGEM 440-441", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortadas (exercício numérico de contas; não acrescenta ao julgamento)"}],
        "alertas": [ALERTA_BPM6,
                    "dado_aproximado: taxa de investimento brasileira em ordem de grandeza (16%–17% do PIB), sem "
                    "ano exato"],
    },
]

# ====================================================================== bloco 6 — Nidi/Jacqueline Bueno, Outubro/2024
CARDS += [
    # ------------------------------------------------------------------ E3-L00414
    {
        "id": "ECO-E3-L00414-1", "fonte_ref": "E3-L00414", "destino": "17", "subtema": H2["pib"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI_OUT,
        "rotulo_item": "Item",
        "assertiva": ("A renda nacional é a soma dos salários, aluguéis, juros e lucros recebidos pelos fatores de "
                      "produção, inclusive dos fatores que estão fora das fronteiras, e inclui ainda as "
                      "transferências governamentais, como pensões e subsídios."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A renda nacional é a soma dos salários, aluguéis, juros e lucros recebidos pelos fatores de "
                       "produção, inclusive dos fatores que estão fora das fronteiras, ") + vm("e inclui ainda")
                    + az(" as transferências governamentais, como pensões e subsídios.")),
        "poucas": ("A " + azb("renda nacional") + " soma só a " + azb("remuneração dos fatores") + " de "
                   "residentes (dentro ou fora do país). Pensões e bolsas são " + vd("transferências") + ": "
                   "redistribuem renda já gerada e não entram."),
        "destrinchando": [
            "A primeira parte está certa: renda nacional = salários + aluguéis + juros + lucros dos fatores "
            "pertencentes a residentes, inclusive os que atuam no exterior (por isso “nacional”, e não "
            "“interna”). Em sentido estrito, é o " + vd("PNL a custo de fatores") + ".",
            "Transferências (aposentadorias, pensões, Bolsa Família, seguro-desemprego) não remuneram produção "
            "corrente: o governo tira de quem produziu (tributos) e repassa. Somá-las contaria duas vezes a mesma "
            "renda — na mão do contribuinte e na do beneficiário.",
            "Onde as transferências entram: na " + azb("renda pessoal") + " (renda nacional − lucros retidos − "
            "contribuições sociais + transferências) e na " + azb("renda disponível") + " (após impostos "
            "diretos); no SCN, na distribuição secundária da renda, que gera a " + azb("renda disponível bruta")
            + ".",
            "Cuidado com os " + azb("subsídios") + ": na passagem de preços de mercado para custo de fatores eles "
            "são <b>somados</b>, mas porque já estão embutidos na remuneração dos fatores das empresas "
            "subsidiadas — não como renda adicional. Tratá-los como “transferência às famílias”, ao lado de "
            "pensões, é parte do erro.",
            vm("Regra-âncora: renda nacional = remuneração de fatores; transferência só entra na renda pessoal "
               "ou disponível."),
        ],
        "dissecando": (cz("[meia-verdade]") + " Primeira oração correta e completa; o erro foi acrescentado no "
                       "fim com “e inclui ainda”. Itens que terminam alongando uma definição correta merecem "
                       "atenção redobrada ao enxerto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A renda pessoal disponível inclui as transferências do governo às famílias.”</i> → CERTO",
            "<i>“A renda nacional exclui a renda dos fatores de residentes que atuam no exterior.”</i> → ERRADO "
            "(confunde nacional com interna)",
        ])],
        "reescrita": ("A renda nacional é a soma dos salários, aluguéis, juros e lucros recebidos pelos fatores de "
                      "produção, inclusive dos fatores que estão fora das fronteiras, " + hl("mas não inclui")
                      + " as transferências governamentais, como pensões e subsídios."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["inclusive"], "dificuldade": 1,
        "comentario_fonte": ("Renda nacional = remuneração dos fatores; transferências são redistribuição, gerariam "
                             "dupla contagem; distinção renda nacional × pessoal × disponível. Uma reescrita da "
                             "fonte restringe a renda nacional aos fatores “dentro das fronteiras” (incorreto)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 581-584", "tipo_fonte": "TEXTO/TABELA", "lado": "verso",
                           "acao": "absorvidas (conceitos de renda levados ao 📖)"}],
        "alertas": ["qualidade_fonte: uma das reescritas de origem limita a renda nacional aos fatores “localizados "
                    "dentro das fronteiras”, o que é o conceito de renda interna — descartada"],
    },
    # ------------------------------------------------------------------ E3-L00415
    {
        "id": "ECO-E3-L00415-1", "fonte_ref": "E3-L00415", "destino": "17", "subtema": H2["pm"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI_OUT,
        "rotulo_item": "Item",
        "assertiva": ("O Produto Interno Bruto (PIB) a preços de mercado é obtido a partir do PIB a preços básicos, "
                      "fazendo a subtração dos impostos indiretos que incidem sobre a produção e a venda e a soma dos "
                      "subsídios concedidos à produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Produto Interno Bruto (PIB) a preços de mercado é obtido a partir do PIB a preços "
                       "básicos, fazendo a ") + vm("subtração") + az(" dos impostos indiretos que incidem sobre a "
                       "produção e a venda e a ") + vm("soma") + az(" dos subsídios concedidos à produção.")),
        "poucas": ("Sinais invertidos: " + vd("PIBpm = PIBpb + impostos sobre produtos − subsídios sobre "
                   "produtos") + ". O preço de mercado (o que o comprador paga) fica acima do básico (o que o "
                   "produtor recebe) por causa dos impostos."),
        "destrinchando": [
            azb("Preço básico") + ": o que o produtor recebe por unidade, sem os impostos sobre produtos e "
            "incluindo os subsídios sobre produtos. " + azb("Preço de comprador") + " (de mercado): o que o "
            "comprador paga, com impostos e sem o subsídio, que já baixou o preço.",
            "Do produtor ao consumidor, o preço " + vd("sobe") + " com o imposto e " + vd("cai") + " com o "
            "subsídio. Logo: preço de mercado = básico + impostos − subsídios. Exemplo: PIB básico 100, impostos "
            "10, subsídios 2 → PIB de mercado " + vd("108") + ".",
            "No SCN do IBGE, o valor adicionado é medido a preços básicos; o PIB resulta de " + vd("VA (preços "
            "básicos) + impostos líquidos de subsídios sobre produtos") + ". Os “outros impostos sobre a "
            "produção” (que não incidem sobre o produto, como IPTU de fábrica) já estão no preço básico.",
            "Não confundir com " + azb("custo de fatores") + ", conceito mais antigo que exclui todos os impostos "
            "indiretos, inclusive os que não incidem sobre produtos: custo de fatores ≤ preços básicos ≤ preços de "
            "mercado (com impostos líquidos positivos).",
            vm("Regra-âncora: para chegar a preços de mercado, soma impostos e subtrai subsídios."),
        ],
        "dissecando": (cz("[inversão]") + " As duas operações foram trocadas ao mesmo tempo, e a frase continua "
                       "fluente. Teste rápido: o PIB a preços de mercado precisa ser <b>maior</b> que o básico "
                       "quando os impostos superam os subsídios — a versão do item o faria menor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB a preços básicos é obtido subtraindo-se do PIB a preços de mercado os impostos sobre "
            "produtos líquidos de subsídios.”</i> → CERTO",
            "<i>“Num país em que os subsídios superam os impostos sobre produtos, o PIB a preços de mercado é "
            "maior que o PIB a preços básicos.”</i> → ERRADO (seria menor)",
        ])],
        "reescrita": ("O Produto Interno Bruto (PIB) a preços de mercado é obtido a partir do PIB a preços básicos, "
                      "fazendo a " + hl("soma") + " dos impostos indiretos que incidem sobre a produção e a venda e a "
                      + hl("subtração") + " dos subsídios concedidos à produção."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Preço de mercado = preço básico + impostos − subsídios; a assertiva inverte os "
                             "sinais; exemplo 100 + 10 − 2 = 108."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 585", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "texto (regra de sinais levada ao 📖)"}],
        "alertas": ["texto_corrigido: “subsidios” → “subsídios” (acento, erro de digitação)"],
    },
    # ------------------------------------------------------------------ E3-L00416
    {
        "id": "ECO-E3-L00416-1", "fonte_ref": "E3-L00416", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_OUT,
        "rotulo_item": "Item",
        "assertiva": ("O PIB é uma medida que contabiliza o valor total dos bens e serviços finais produzidos em um "
                      "país durante um determinado período, excluindo as transações de bens intermediários para "
                      "evitar a contagem dupla."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O PIB é uma medida que contabiliza o valor total dos bens e serviços <u>finais</u> produzidos "
                      "em um país durante um determinado período, <u>excluindo as transações de bens "
                      "intermediários</u> para evitar a contagem dupla."),
        "poucas": ("Definição de manual: PIB = valor dos " + azb("bens e serviços finais") + " = soma dos "
                   + azb("valores adicionados") + ". Incluir os intermediários contaria o mesmo insumo várias "
                   "vezes."),
        "destrinchando": [
            "Cadeia trigo → farinha → pão: se o trigo vale 10, a farinha 25 e o pão 40, somar tudo (75) contaria o "
            "trigo três vezes e a farinha duas. O PIB é " + vd("40") + ": o valor do bem final, ou a soma dos "
            "valores adicionados (10 + 15 + 15).",
            azb("Bem intermediário") + " é definido pelo <b>uso</b>, não pela natureza: farinha comprada pela "
            "padaria é intermediária; a mesma farinha comprada pela família é bem final (consumo).",
            "Equivalência das óticas: " + azb("produto") + " (Σ valor adicionado = VBP − consumo intermediário) = "
            + azb("despesa") + " (C + I + G + X − M, só usos finais) = " + azb("renda") + " (remuneração dos "
            "fatores + impostos líquidos).",
            "Bens finais incluem os de capital (máquinas compradas pelas empresas, que são FBCF) e a variação de "
            "estoques: insumo produzido e não usado no período entra como estoque, não some.",
            "Também ficam fora do PIB transações que não são produção corrente: revenda de usados (só a margem do "
            "revendedor entra), compra de ações e transferências.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição canônica. Variantes erradas incluem os intermediários "
                       "(“valor total de todas as transações”) ou trocam “finais” por “de consumo”, esquecendo "
                       "investimento e exportações."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O PIB corresponde à soma do valor bruto da produção de todos os setores da economia.”</i> → "
            "ERRADO (inclui o consumo intermediário: dupla contagem)",
            "<i>“Uma máquina adquirida por uma empresa para uso na produção é bem final e entra no PIB como "
            "investimento.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Definição do PIB pela ótica do produto; exemplos farinha/pão e aço/carro; soma de "
                             "valores adicionados; tabela de insumo-produto ilustrativa."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 586", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (tabela de insumo-produto ilustrativa com transcrição incompleta)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00417
    {
        "id": "ECO-E3-L00417-1", "fonte_ref": "E3-L00417", "destino": "17", "subtema": H2["ident"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI_OUT,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de valor agregado, que é fundamental na contabilidade nacional, considera não apenas "
                      "o valor dos bens e serviços finais, mas também as contribuições dos fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O conceito de valor agregado, que é fundamental na contabilidade nacional, considera não "
                      "apenas o valor dos bens e serviços finais, mas também as <u>contribuições dos fatores de "
                      "produção</u>."),
        "poucas": ("" + azb("Valor agregado") + " = VBP − consumo intermediário: o valor novo criado em cada etapa, "
                   "que remunera os " + azb("fatores de produção") + ". Somado na economia, iguala o valor dos bens "
                   "finais."),
        "destrinchando": [
            "Em cada empresa: " + vd("VA = valor bruto da produção − consumo intermediário") + ". Madeireira vende "
            "100 com 20 de insumos → VA 80; marcenaria transforma a madeira (100) em móveis de 300 → VA 200. "
            "PIB = 80 + 200 = " + vd("280") + " (e não 400).",
            "O VA de cada etapa é exatamente o que fica para pagar trabalho (salários), capital (lucros, juros), "
            "terra (aluguéis) e governo (impostos líquidos sobre a produção). Por isso a ótica do produto (Σ VA) "
            "coincide com a ótica da renda.",
            "E Σ VA coincide com o valor dos bens finais (ótica da despesa): é a mesma “pizza” cortada de três "
            "jeitos. Essa dupla face é o que o item descreve, de forma pouco técnica, como considerar o valor dos "
            "bens finais “e também” as contribuições dos fatores.",
            "Utilidade prática: o VA permite medir a contribuição de cada setor ao PIB (agropecuária, indústria, "
            "serviços) sem dupla contagem; é também a base do " + azb("IVA") + ", imposto que incide só sobre o "
            "valor adicionado em cada etapa.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Redação imprecisa (“não apenas… mas "
                       "também”), mas sem afirmação falsa: o VA liga as óticas do produto e da renda. Em item "
                       "conceitual frouxo, a banca de simulado tende ao CERTO se nada estiver objetivamente errado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O valor agregado de uma empresa corresponde ao valor bruto de sua produção.”</i> → ERRADO (falta "
            "subtrair o consumo intermediário)",
            "<i>“A soma dos valores agregados de todas as unidades produtivas residentes, mais os impostos "
            "líquidos sobre produtos, corresponde ao PIB.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["não apenas", "mas também"],
        "dificuldade": 1,
        "comentario_fonte": ("VA = VBP − CI = remuneração dos fatores; soma dos VA = PIB; exemplos padaria e "
                             "madeireira/marcenaria."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 586", "tipo_fonte": "TABELA", "lado": "verso",
                           "acao": "cortada (tabela de insumo-produto ilustrativa com transcrição incompleta)"}],
        "alertas": [],
    },
]
