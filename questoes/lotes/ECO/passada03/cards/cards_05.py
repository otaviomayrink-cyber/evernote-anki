"""Cards do lote de redação 05 — ECO, passada 03 (notas 59: mercado de trabalho e Lei de Okun; 65: sistema
financeiro internacional)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "des": "👷 Desemprego e mercado de trabalho",
    "okun": "📏 Lei de Okun",
    "ouro": "🥇 Padrão-ouro",
    "bw": "🏦 Bretton Woods",
    "pos": "💥 Crises e pós-Bretton Woods",
}


def provavel(ano):
    return (f"banca_provavel: a fonte só traz o ano ({ano}), com marca de prova antiga; possivelmente "
            "CEBRASPE (IRBr/CACD), não confirmado")


CMD_NAB_DES = "Acerca do nível de desemprego e seus tipos, julgue o item a seguir."

CMD_RT_INF = "Julgue o item seguinte, a respeito da relação entre inflação e desemprego na macroeconomia."

CMD_RT_OA = "Com relação à oferta agregada, aos salários, aos preços e ao emprego, julgue o item a seguir."

CMD_RT_PAND = ("Durante a pandemia, a taxa de desemprego aumentou muito no Brasil e em todo o mundo. A respeito dos "
               "conceitos de desemprego e das suas relações com a inflação e a atividade econômica, julgue o item a "
               "seguir.")

CMD_TJPA_74 = ("Considerando essa situação hipotética, julgue o item que se segue, em relação aos efeitos "
               "macroeconômicos de choques salariais e fiscais, e de movimentos nos preços internos.")

EXC_TJPA_74 = ("<p><i>Uma economia nacional opera com capital fixo no curto prazo e está sujeita a variações nominais "
               "de salários, preços internos e políticas fiscais expansionistas. O país adota um regime de taxa de "
               "câmbio fixa e mantém constante o nível de preços internacionais.</i></p>")

CMD_SMI = "Acerca do sistema monetário internacional, julgue o item a seguir."

CMD_ARM = "Acerca da evolução do sistema monetário internacional, do padrão-ouro aos dias atuais, julgue o item a seguir."

CMD_NAB_26 = "Acerca de macroeconomia aberta e sistema monetário internacional, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01277
    {
        "id": "ECO-E2-L01277-1", "fonte_ref": "E2-L01277", "destino": "59", "subtema": H2["okun"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_DES,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a Lei de Okun, um aumento de 1% no PIB está associado a uma redução de 1% na "
                      "taxa de desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a Lei de Okun, um aumento de 1% no PIB está associado a uma redução de ")
                    + vm("1%") + az(" na taxa de desemprego.")),
        "poucas": ("A Lei de Okun dá uma relação " + azb("inversa") + " entre produto e desemprego, mas "
                   + vm("não unitária") + ": o coeficiente é estimado (nos EUA, algo como " + vd("0,4–0,5") + ") e "
                   "varia por país e período."),
        "destrinchando": [
            oc("Arthur Okun") + " (1962), assessor econômico do governo Kennedy, observou nos dados dos EUA uma "
            "regularidade " + azb("empírica") + " — não uma lei teórica — entre o ciclo do produto e o desemprego.",
            "Versão em diferenças (a de " + oc("Blanchard") + "): " + vd("u<sub>t</sub> − u<sub>t−1</sub> = "
            "−β(g<sub>t</sub> − ḡ)") + ". O desemprego só cai quando o PIB cresce <b>acima</b> da taxa normal ḡ "
            "(nos EUA, em torno de 3% ao ano, segundo a estimativa do manual); com β ≈ " + vd("0,4") + ", crescer "
            "1 ponto acima do normal reduz o desemprego em cerca de 0,4 ponto.",
            "Versão em hiato: cada ponto de desemprego acima da taxa natural corresponde a uma perda de produto "
            "de algo como " + vd("2% a 3%") + " do potencial (Okun estimou cerca de 3%; estudos posteriores, "
            "valores menores).",
            "Por que a relação é menor que 1 para 1: (1) a " + azb("produtividade") + " cresce, e parte do "
            "aumento do PIB vem de produzir mais com as mesmas pessoas; (2) a força de trabalho cresce, e é "
            "preciso absorver os novos entrantes; (3) as firmas ajustam primeiro as horas trabalhadas (horas "
            "extras, retenção de mão de obra treinada) e só depois o número de empregados.",
            "O coeficiente depende das instituições: com legislação mais rígida ou informalidade elevada, como "
            "no " + rx("Brasil") + ", o desemprego reage menos às variações do PIB.",
            vm("Regra-âncora: Okun = relação inversa produto × desemprego, com coeficiente estimado — nunca 1 "
               "para 1 por definição."),
        ],
        "dissecando": (cz("[dado alterado]") + " O item acerta o sentido (PIB ↑, desemprego ↓) e inventa a "
                       "magnitude: “1% → 1%” transforma uma regularidade estatística em identidade. Pista: "
                       "números redondos e simétricos em relação empírica costumam ser fabricados. A banca também "
                       "explora a mistura de unidades (% do PIB × pontos percentuais de desemprego)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela Lei de Okun, se o PIB cresce à sua taxa normal, a taxa de desemprego tende a permanecer "
            "estável.”</i> → CERTO",
            "<i>“Pela Lei de Okun, qualquer crescimento positivo do PIB reduz a taxa de desemprego.”</i> → ERRADO "
            "(só o crescimento acima do normal)",
        ])],
        "reescrita": ("De acordo com a Lei de Okun, um aumento de 1% no PIB está associado a uma redução de "
                      + hl("menos de 1 ponto percentual (nos EUA, cerca de 0,4 a 0,5 ponto por ponto de "
                           "crescimento acima do normal)") + " na taxa de desemprego."),
        "tipo_erro": ["DADO_ALTERADO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A Lei de Okun relaciona produto e desemprego, mas a relação não é necessariamente "
                            "unitária: o aumento de 1% no PIB pode reduzir o desemprego em mais ou menos de 1%.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00139-1, ECO-E2-L01596-1 (Lei de Okun)"],
    },
    # ------------------------------------------------------------------ E2-L01278
    {
        "id": "ECO-E2-L01278-1", "fonte_ref": "E2-L01278", "destino": "59", "subtema": H2["des"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_DES,
        "rotulo_item": "Item",
        "assertiva": ("Desemprego estrutural compõe a taxa natural de desemprego; desemprego friccional não compõe "
                      "a taxa natural de desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Desemprego estrutural compõe a taxa natural de desemprego; desemprego friccional ")
                    + vm("não") + az(" compõe a taxa natural de desemprego.")),
        "poucas": ("A " + azb("taxa natural") + " é a soma do desemprego " + vd("friccional") + " e do "
                   + vd("estrutural") + ": só o " + azb("cíclico") + " fica de fora."),
        "destrinchando": [
            "Classificação clássica do desemprego: " + azb("friccional") + " (tempo de busca e de "
            "pareamento entre trabalhador e vaga: quem acabou de se formar, quem trocou de cidade, quem largou "
            "um emprego para procurar outro melhor); " + azb("estrutural") + " (descasamento persistente entre "
            "as qualificações ou a localização dos trabalhadores e as vagas, ou salário real mantido acima do "
            "equilíbrio por salário mínimo, sindicatos ou salários de eficiência); " + azb("cíclico")
            + " (falta de demanda agregada na recessão).",
            "A " + azb("taxa natural de desemprego") + " é a que prevalece quando o produto está no potencial: "
            + vd("u<sub>n</sub> = friccional + estrutural") + ". O desemprego efetivo é u = u<sub>n</sub> + "
            "cíclico; na recessão, o cíclico é positivo; no superaquecimento, negativo.",
            "O friccional existe mesmo num mercado de trabalho saudável e flexível: informação imperfeita e "
            "heterogeneidade de vagas e de pessoas fazem a busca levar tempo. Ele pode até ser produtivo, porque "
            "melhora a qualidade do pareamento.",
            "Por isso a taxa natural nunca é zero, e políticas de demanda (fiscal, monetária) só atacam o "
            "componente cíclico; o friccional e o estrutural pedem políticas de oferta: intermediação de mão de "
            "obra, qualificação, reformas institucionais.",
            vm("Regra-âncora: taxa natural = friccional + estrutural; cíclico = desvio em relação a ela."),
        ],
        "dissecando": (cz("[meia-verdade]") + " A primeira oração está certa; a segunda exclui justamente o "
                       "componente mais “natural” de todos. Pista: o item separa os dois tipos que os manuais "
                       "sempre apresentam juntos como formadores da taxa natural. 🔥 A banca costuma trocar o "
                       "cíclico por um dos outros dois."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O desemprego cíclico não compõe a taxa natural de desemprego.”</i> → CERTO",
            "<i>“Políticas monetárias expansionistas são o instrumento adequado para reduzir o desemprego "
            "estrutural de forma duradoura.”</i> → ERRADO (troca de conceito: política de demanda só atinge o "
            "cíclico)",
        ])],
        "reescrita": ("Desemprego estrutural compõe a taxa natural de desemprego; desemprego friccional "
                      + hl("também") + " compõe a taxa natural de desemprego."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": "Friccional decorre do tempo de procura; estrutural, do descasamento entre oferta e "
                            "demanda de mão de obra (tecnologia, legislação, salário mínimo, sindicatos, bolsões "
                            "regionais). Ambos compõem a taxa natural.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01279
    {
        "id": "ECO-E2-L01279-1", "fonte_ref": "E2-L01279", "destino": "59", "subtema": H2["des"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_DES,
        "rotulo_item": "Item",
        "assertiva": ("A taxa natural de desemprego pode ser conceituada como a taxa de desemprego do pleno emprego "
                      "ou de longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A taxa natural de desemprego <u>pode ser conceituada</u> como a taxa de desemprego do "
                      "<u>pleno emprego</u> ou de <u>longo prazo</u>."),
        "poucas": ("A " + azb("taxa natural") + " é o desemprego que persiste com a economia no "
                   + azb("produto potencial") + " — o “pleno emprego” possível — e para o qual ela converge no "
                   "longo prazo."),
        "destrinchando": [
            "O conceito vem de " + oc("Milton Friedman") + " (discurso presidencial na American Economic "
            "Association, 1968) e de " + oc("Edmund Phelps") + ": no longo prazo, com expectativas ajustadas, o "
            "desemprego volta a um nível determinado por fatores <b>reais</b>, não monetários.",
            "“Pleno emprego” não é desemprego zero: é a situação em que só há desemprego " + vd("friccional")
            + " e " + vd("estrutural") + " — o cíclico é nulo. Por isso a taxa natural é chamada de taxa do pleno "
            "emprego.",
            "Na " + azb("curva de Phillips aumentada por expectativas") + ", é a taxa em que a inflação efetiva "
            "iguala a esperada; abaixo dela, a inflação acelera. Daí o nome " + azb("NAIRU") + " (taxa de "
            "desemprego que não acelera a inflação). No longo prazo, a curva de Phillips é vertical nesse ponto: "
            "não há <i>trade-off</i> permanente entre inflação e desemprego.",
            "Determinantes: seguro-desemprego e outros benefícios, salário mínimo acima do equilíbrio, poder "
            "sindical, encargos sobre a folha, demografia, descasamentos setoriais e regionais e "
            + azb("histerese") + " (recessões longas que deixam desemprego permanente, por perda de "
            "qualificação ou desalento).",
            "A taxa natural não é constante nem “desejável”: “natural” quer dizer apenas compatível com a "
            "estrutura da economia, e muda com instituições e políticas de oferta.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Item conceitual, salvo pelo “pode ser "
                       "conceituada”. O risco é o candidato achar que “pleno emprego” significa desemprego zero e "
                       "marcar ERRADO. Lembre: pleno emprego = desemprego só friccional e estrutural."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na taxa natural de desemprego, o desemprego friccional e o estrutural são nulos.”</i> → ERRADO "
            "(troca de conceito: nulo é o cíclico)",
            "<i>“Mantido o desemprego abaixo da taxa natural, a inflação tende a acelerar.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Taxa de pleno emprego ou de longo prazo, sem trade-off entre inflação e desemprego; "
                            "Friedman: apoia-se em fatores reais (eficácia do mercado de trabalho, competição, "
                            "incentivos); determinantes: benefícios, salário mínimo, sindicatos, impostos sobre a "
                            "folha, demografia, histerese.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01280
    {
        "id": "ECO-E2-L01280-1", "fonte_ref": "E2-L01280", "destino": "59", "subtema": H2["des"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_DES,
        "rotulo_item": "Item",
        "assertiva": ("Benefícios aos trabalhadores desempregados, tais como o programa de seguro-desemprego, "
                      "reduzem o desemprego friccional, visto que os trabalhadores desempregados recebem, durante "
                      "certo período de tempo, parte do salário que recebiam no seu último emprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Benefícios aos trabalhadores desempregados, tais como o programa de seguro-desemprego, ")
                    + vm("reduzem") + az(" o desemprego friccional, visto que os trabalhadores desempregados "
                                         "recebem, durante certo período de tempo, parte do salário que recebiam "
                                         "no seu último emprego.")),
        "poucas": ("O seguro-desemprego " + vm("aumenta") + " o desemprego friccional: ao reduzir o custo de ficar "
                   "sem trabalho, alonga a " + azb("busca") + " por um novo emprego."),
        "destrinchando": [
            "Desemprego " + azb("friccional") + " = tempo gasto procurando uma vaga adequada. Cada dia de busca "
            "tem um custo (a renda que se deixa de ganhar) e um benefício (a chance de achar um emprego melhor). "
            "O trabalhador aceita uma oferta quando ela supera seu " + azb("salário de reserva") + ".",
            "O benefício paga parte do salário perdido: o custo de continuar procurando cai, o salário de reserva "
            "sobe, e o desempregado passa a recusar ofertas que antes aceitaria. A duração média do desemprego "
            "— e, com ela, a taxa friccional — " + vd("aumenta") + ". É o exemplo clássico de " + oc("Mankiw")
            + " para os determinantes da taxa natural.",
            "Repare que a justificativa do item (“recebem parte do salário”) é verdadeira: é justamente ela que "
            "explica o efeito contrário ao afirmado.",
            "Isso não torna o programa ruim: ele reduz a incerteza de renda, sustenta o consumo na recessão "
            "(estabilizador automático) e pode melhorar o pareamento, porque o trabalhador não precisa aceitar "
            "a primeira vaga que aparece. O trade-off é entre proteção e duração do desemprego.",
            "No " + rx("Brasil") + ", o seguro-desemprego (previsto na Constituição e financiado pelo FAT) paga "
            "de " + vd("3 a 5 parcelas") + ", conforme o tempo de trabalho anterior.",
        ],
        "dissecando": (cz("[inversão]") + " Premissa verdadeira, conclusão invertida: o item usa o fato certo "
                       "(o benefício substitui parte do salário) para defender o efeito errado. Pista: pergunte-se "
                       "o que acontece com o <b>incentivo a procurar</b> quando ficar desempregado custa menos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O seguro-desemprego tende a elevar a taxa natural de desemprego, por aumentar a duração da "
            "busca por emprego.”</i> → CERTO",
            "<i>“O seguro-desemprego, por aumentar o salário de reserva, reduz o tempo médio de procura por "
            "emprego.”</i> → ERRADO (inversão: aumenta o tempo de procura)",
        ])],
        "reescrita": ("Benefícios aos trabalhadores desempregados, tais como o programa de seguro-desemprego, "
                      + hl("aumentam") + " o desemprego friccional, visto que os trabalhadores desempregados "
                      "recebem, durante certo período de tempo, parte do salário que recebiam no seu último "
                      "emprego."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Programas como o seguro-desemprego aumentam o desemprego friccional porque "
                            "desincentivam a procura mais rápida de um novo emprego.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01478
    {
        "id": "ECO-E2-L01478-1", "fonte_ref": "E2-L01478", "destino": "59", "subtema": H2["des"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_INF,
        "rotulo_item": "Item",
        "assertiva": ("As pessoas que desistiram de procurar emprego na pandemia, os chamados desalentados, não "
                      "fazem parte da população economicamente ativa, não sendo contabilizados como desempregados "
                      "na estatística oficial do IBGE."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As pessoas que desistiram de procurar emprego na pandemia, os chamados desalentados, "
                      "<u>não fazem parte da população economicamente ativa</u>, não sendo contabilizados como "
                      "desempregados na estatística oficial do IBGE."),
        "poucas": ("Desocupado é quem " + azb("procurou trabalho") + " e está disponível. O " + azb("desalentado")
                   + " quer trabalhar, mas desistiu de procurar: fica " + vd("fora da força de trabalho") + " e não "
                   "entra na taxa de desocupação."),
        "destrinchando": [
            "Pela metodologia do " + rx("IBGE") + " (PNAD Contínua, alinhada à OIT), a população em idade de "
            "trabalhar (14 anos ou mais) divide-se em " + azb("força de trabalho") + " — o antigo nome era "
            "população economicamente ativa (PEA) — e " + azb("fora da força de trabalho") + ". A força de "
            "trabalho = " + vd("ocupados + desocupados") + ".",
            "Para ser " + azb("desocupado") + " é preciso, na semana de referência: não ter trabalho, ter tomado "
            "providência efetiva para consegui-lo nos últimos 30 dias e estar disponível. Taxa de desocupação = "
            "desocupados ÷ força de trabalho.",
            "O " + azb("desalentado") + " gostaria de trabalhar e estaria disponível, mas não procurou por achar "
            "que não encontraria vaga (falta de oportunidade na localidade, de experiência, idade). Sem procura, "
            "não é desocupado: integra a " + azb("força de trabalho potencial") + ", fora da força de trabalho.",
            "Consequência estatística: quando muitos desistem de procurar, a taxa de desocupação pode cair ou "
            "subir menos sem que o mercado tenha melhorado. Foi o que se viu na pandemia, quando o desalento "
            "bateu recorde (cerca de " + vd("6 milhões") + " de pessoas no início de 2021).",
            "Por isso o IBGE divulga também a " + azb("taxa composta de subutilização da força de trabalho")
            + ", que soma desocupados, subocupados por insuficiência de horas e a força de trabalho potencial "
            "(onde estão os desalentados).",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a definição oficial. O risco é a intuição: “quem quer "
                       "trabalhar e não trabalha é desempregado”. Para o IBGE, o critério decisivo é a "
                       "<b>procura efetiva</b>. A banca também cobra o efeito do desalento sobre a taxa "
                       "(“mascara” o desemprego)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento do número de desalentados, mantido o resto constante, tende a reduzir a taxa de "
            "desocupação medida pelo IBGE.”</i> → CERTO",
            "<i>“Os desalentados integram a força de trabalho, por estarem disponíveis para trabalhar.”</i> → "
            "ERRADO (troca de conceito: sem procura, ficam fora da força de trabalho)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Desalentados desistiram de procurar emprego; sem procura ativa, estão fora da PEA e "
                            "não entram na taxa de desocupação; o IBGE os inclui nas medidas de subutilização.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01595-1 (critério de procura efetiva para ser desocupado)"],
    },
    # ------------------------------------------------------------------ E2-L01560
    {
        "id": "ECO-E2-L01560-1", "fonte_ref": "E2-L01560", "destino": "59", "subtema": H2["des"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_OA,
        "rotulo_item": "Item",
        "assertiva": "No longo-prazo, os salários são flexíveis e portanto a taxa natural de desemprego é nula.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No longo-prazo, os salários são flexíveis e ") + vm("portanto") + az(" a taxa natural de "
                                                                                              "desemprego ")
                    + vm("é nula") + az(".")),
        "poucas": ("Salários flexíveis eliminam o desemprego " + azb("cíclico") + ", não o " + azb("friccional")
                   + " nem o " + azb("estrutural") + ": a taxa natural é " + vm("positiva") + "."),
        "destrinchando": [
            "A primeira oração está certa: nos modelos de longo prazo (clássico, OA vertical, curva de Phillips "
            "vertical), preços e salários se ajustam por completo, e a economia volta ao " + azb("produto "
            "potencial") + ".",
            "Mas o produto potencial convive com desemprego: a " + azb("taxa natural") + " = " + vd("friccional "
            "+ estrutural") + ". O que a flexibilidade zera é só o " + azb("cíclico") + " (o desvio em relação à "
            "taxa natural causado por falta de demanda).",
            "Por que a flexibilidade não elimina os outros dois: o friccional nasce da informação imperfeita e do "
            "tempo de busca (trabalhadores e vagas são heterogêneos); o estrutural, de descasamentos de "
            "qualificação e de localização e de rigidezes institucionais (salário mínimo, sindicatos, salários "
            "de eficiência) que mantêm o salário real de alguns segmentos acima do equilíbrio.",
            "Na formulação de " + oc("Friedman") + " (1968), a taxa natural incorpora justamente essas "
            "“características estruturais” do mercado de trabalho. Em economias desenvolvidas, as estimativas "
            "ficam em geral entre " + vd("4% e 6%") + ", variando com as instituições.",
            vm("Regra-âncora: longo prazo com salários flexíveis → desemprego = taxa natural (> 0), cíclico = 0."),
        ],
        "dissecando": (cz("[nexo indevido · meia-verdade]") + " Premissa correta + “portanto” + conclusão falsa. "
                       "O examinador confunde “desemprego cíclico nulo” com “taxa natural nula”. Pista: o conector "
                       "conclusivo ligando flexibilidade de preço a desemprego zero — flexibilidade não cria "
                       "informação perfeita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, com salários flexíveis, o desemprego cíclico tende a desaparecer.”</i> → CERTO",
            "<i>“A taxa natural de desemprego corresponde ao desemprego involuntário causado por insuficiência "
            "de demanda agregada.”</i> → ERRADO (troca de conceito: isso é o cíclico)",
        ])],
        "reescrita": ("No longo-prazo, os salários são flexíveis e " + hl("ainda assim") + " a taxa natural de "
                      "desemprego " + hl("é positiva") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "MEIA_VERDADE"], "moduladores": ["portanto"], "dificuldade": 1,
        "comentario_fonte": "A flexibilidade salarial de longo prazo elimina o desemprego cíclico, mas a taxa "
                            "natural (NAIRU) inclui fricções e desequilíbrios estruturais e não é nula; estimativas "
                            "de 4% a 6% em economias desenvolvidas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01595
    {
        "id": "ECO-E2-L01595-1", "fonte_ref": "E2-L01595", "destino": "59", "subtema": H2["des"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_PAND,
        "rotulo_item": "Item",
        "assertiva": ("Uma pessoa que deixa seu emprego para se dedicar aos estudos para um concurso público faz "
                      "parte dos desempregados pela metodologia das estatísticas oficiais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma pessoa que deixa seu emprego para se dedicar aos estudos para um concurso público ")
                    + vm("faz parte dos desempregados") + az(" pela metodologia das estatísticas oficiais.")),
        "poucas": ("Quem não " + azb("procura trabalho") + " não é desocupado: o concurseiro em dedicação "
                   "exclusiva está " + vd("fora da força de trabalho") + "."),
        "destrinchando": [
            "Critério da OIT, adotado pelo " + rx("IBGE") + " na PNAD Contínua: é " + azb("desocupada") + " a "
            "pessoa que, na semana de referência, (1) não trabalhou, (2) tomou providência efetiva para conseguir "
            "trabalho nos 30 dias anteriores e (3) estava disponível para assumi-lo. Faltando qualquer um dos "
            "três, não há desemprego no sentido estatístico.",
            "Quem largou o emprego para estudar não procura trabalho (nem está disponível para assumi-lo de "
            "imediato): é classificado " + azb("fora da força de trabalho") + ", ao lado de estudantes, "
            "aposentados, pessoas dedicadas aos afazeres domésticos e desalentados.",
            "Ter saído voluntariamente do emprego não é o que decide: quem pede demissão e passa a procurar outra "
            "vaga é desocupado (e é um caso típico de desemprego " + azb("friccional") + "). O que decide é a "
            "procura efetiva.",
            "Efeito sobre a taxa: a taxa de desocupação (desocupados ÷ força de trabalho) não registra essa "
            "pessoa. Se, depois da prova, ela passar a procurar emprego sem achar, entra na força de trabalho "
            "como desocupada e a taxa sobe.",
            vm("Regra-âncora: desocupado = sem trabalho + procurou + disponível."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Confunde “estar sem emprego” com “estar desempregado” no "
                       "sentido estatístico. Pista: o item não diz que a pessoa procura trabalho — e o motivo da "
                       "saída (estudar) indica que não procura. 🔥 A banca alterna os casos-limite: desalentado, "
                       "estudante, quem trabalha poucas horas (ocupado), quem aguarda resposta de seleção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quem trabalhou ao menos uma hora na semana de referência, ainda que sem remuneração em dinheiro, "
            "é considerado ocupado pela PNAD Contínua.”</i> → CERTO",
            "<i>“Quem pede demissão para procurar emprego melhor fica fora da força de trabalho enquanto "
            "procura.”</i> → ERRADO (com procura efetiva, é desocupado)",
        ])],
        "reescrita": ("Uma pessoa que deixa seu emprego para se dedicar aos estudos para um concurso público "
                      + hl("não faz parte dos desempregados, e sim da população fora da força de trabalho,")
                      + " pela metodologia das estatísticas oficiais."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Pela metodologia oficial (IBGE/OIT), desempregado é quem não trabalha, está "
                            "disponível e procurou trabalho no período de referência; quem estuda para concurso sem "
                            "procurar emprego está fora da força de trabalho.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01478-1 (desalentados fora da força de trabalho)"],
    },
    # ------------------------------------------------------------------ E2-L01596
    {
        "id": "ECO-E2-L01596-1", "fonte_ref": "E2-L01596", "destino": "59", "subtema": H2["okun"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_PAND,
        "rotulo_item": "Item",
        "assertiva": ("A lei de Okun mostra que um aumento do hiato do produto levará a uma redução da taxa de "
                      "inflação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A lei de Okun mostra que um aumento do hiato do produto levará a uma redução da taxa de ")
                    + vm("inflação") + az(".")),
        "poucas": ("A " + azb("Lei de Okun") + " liga produto e " + vm("desemprego") + "; quem liga atividade e "
                   "inflação é a " + azb("curva de Phillips") + "."),
        "destrinchando": [
            azb("Hiato do produto") + " = (Y − Y*) ÷ Y*, a distância entre o PIB efetivo e o potencial. Na "
            "convenção do " + rx("Banco Central do Brasil") + ", hiato positivo = economia aquecida; negativo = "
            "ociosidade. Um <b>aumento</b> do hiato, nessa convenção, é aquecimento.",
            "Lei de Okun, versão em hiato: " + vd("u − u<sub>n</sub> = −β·(Y − Y*)/Y*") + ". Hiato maior → "
            "desemprego <b>abaixo</b> da taxa natural. Versão em crescimento: " + vd("Δu = −β(g − ḡ)") + ". Em "
            "nenhuma das duas aparece a inflação.",
            "A ligação com a inflação vem da " + azb("curva de Phillips") + " (aumentada por expectativas): "
            + vd("π = π<sup>e</sup> − α(u − u<sub>n</sub>)") + ", ou, em termos de hiato, π = π<sup>e</sup> + "
            "γ·hiato. Economia aquecida → desemprego baixo → salários e preços sobem mais depressa.",
            "Encadeando as duas relações: Okun leva do produto ao desemprego; Phillips, do desemprego à inflação. "
            "Por isso o item tem um segundo problema: com hiato crescente (aquecimento), a pressão é de "
            + vd("alta") + " da inflação, não de queda — a “redução” só valeria se “hiato” fosse lido como "
            "ociosidade.",
            "É exatamente o raciocínio dos bancos centrais: o hiato do produto é variável-chave dos modelos de "
            "metas de inflação do BCB e entra na regra de Taylor.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui à Lei de Okun o objeto da curva de Phillips. "
                       "Pista: “Okun” na frase + “inflação” na conclusão = troca de relação. 🔥 Itens desse bloco "
                       "costumam embaralhar as três peças: Okun (produto–desemprego), Phillips "
                       "(desemprego–inflação) e oferta agregada (produto–preços)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela curva de Phillips aumentada por expectativas, um hiato do produto positivo tende a elevar "
            "a inflação acima da esperada.”</i> → CERTO",
            "<i>“A lei de Okun estabelece que o desemprego abaixo da taxa natural acelera a inflação.”</i> → "
            "ERRADO (troca de conceito: isso é a curva de Phillips)",
        ])],
        "reescrita": ("A lei de Okun mostra que um aumento do hiato do produto levará a uma redução da taxa de "
                      + hl("desemprego") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A Lei de Okun relaciona hiato do produto e desemprego, não inflação; a relação com a "
                            "inflação é a da curva de Phillips. Fórmula de Okun (imagem): u_t − u_{t−1} = "
                            "−β(g_yt − ḡ_y).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 452", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["qualidade_fonte: os comentários da fonte usam convenções opostas de hiato (um diz que o "
                    "aumento do hiato eleva o desemprego, outro que o reduz); o card adota a convenção do BCB "
                    "(hiato positivo = economia aquecida)",
                    "quase_duplicata: ECO-E2-L01277-1, ECO-E3-L00139-1 (Lei de Okun)"],
    },
    # ------------------------------------------------------------------ E3-L00030
    {
        "id": "ECO-E3-L00030-1", "fonte_ref": "E3-L00030", "destino": "59", "subtema": H2["des"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA_74,
        "excerto": EXC_TJPA_74,
        "rotulo_item": "Item",
        "assertiva": ("Se o salário nominal aumenta, mas o nível de preços permanece constante, o salário real "
                      "também se mantém constante, e o equilíbrio do mercado de trabalho não é afetado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se o salário nominal aumenta, mas o nível de preços permanece constante, o salário real ")
                    + vm("também se mantém constante") + az(", e o equilíbrio do mercado de trabalho ")
                    + vm("não é afetado") + az(".")),
        "poucas": ("Salário real = " + vd("W/P") + ". Com W ↑ e P constante, W/P " + vm("sobe") + ": o trabalho "
                   "fica mais caro, as firmas contratam menos e o mercado de trabalho sai do equilíbrio."),
        "destrinchando": [
            azb("Salário real") + " = salário nominal ÷ nível de preços = poder de compra do salário. Em taxas: "
            "variação do salário real ≈ variação de W − inflação. Com inflação zero, todo aumento nominal é "
            "aumento real.",
            "A " + azb("demanda por trabalho") + " das firmas depende do salário real: contrata-se até que o "
            "produto marginal do trabalho iguale W/P. Com W/P maior, a quantidade demandada de trabalho cai "
            "(movimento ao longo de Lᴰ).",
            "A " + azb("oferta de trabalho") + " também responde a W/P: mais gente quer trabalhar. Com W/P acima "
            "do equilíbrio, Lˢ > Lᴰ: " + vd("excesso de oferta de trabalho") + " — desemprego, se o salário não "
            "voltar a cair.",
            "No cenário do comando (capital fixo no curto prazo), o choque salarial reduz o emprego e, pela "
            "função de produção, o produto: a oferta agregada de curto prazo se desloca para a esquerda.",
            "Contraste útil: se W e P subirem na mesma proporção, W/P fica constante e o equilíbrio real não se "
            "altera — é a ideia de " + azb("neutralidade") + " que o item tentou aplicar no caso errado.",
        ],
        "grafico_verso": "ECO-E3-L00030-1-V1",
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Confunde salário nominal com salário real e "
                       "tira daí a conclusão de que nada muda. Pista: “nominal aumenta” + “preços constantes” só "
                       "admite uma resposta para W/P. O CEBRASPE costuma testar a versão neutra (W e P subindo "
                       "juntos), que seria CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o salário nominal e o nível de preços aumentam na mesma proporção, o salário real permanece "
            "constante.”</i> → CERTO",
            "<i>“Se o salário nominal sobe 5% e a inflação é de 8%, o salário real aumenta cerca de 3%.”</i> → "
            "ERRADO (sinal trocado: cai cerca de 3%)",
        ])],
        "reescrita": ("Se o salário nominal aumenta, mas o nível de preços permanece constante, o salário real "
                      + hl("aumenta") + ", e o equilíbrio do mercado de trabalho " + hl("é afetado") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "W/P sobe se W aumenta com P constante; o trabalho fica mais caro, a demanda por "
                            "trabalho cai e o equilíbrio do mercado de trabalho é afetado (excesso de oferta de "
                            "trabalho).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00139
    {
        "id": "ECO-E3-L00139-1", "fonte_ref": "E3-L00139", "destino": "59", "subtema": H2["okun"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Julgue o próximo item, tendo em vista os modelos macroeconômicos para economias abertas.",
        "rotulo_item": "Item",
        "assertiva": "A lei de Okun estabelece que o aumento do produto de equilíbrio gera redução do desemprego.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A lei de Okun estabelece que o aumento do produto de equilíbrio gera <u>redução do "
                      "desemprego</u>."),
        "poucas": ("Okun = relação " + azb("inversa") + " entre produto e desemprego: produzir mais exige mais "
                   "trabalho, e o desemprego cai."),
        "destrinchando": [
            "Regularidade empírica observada por " + oc("Arthur Okun") + " (1962) nos dados dos EUA. Mecanismo: "
            "o trabalho é " + azb("demanda derivada") + " — as firmas contratam porque precisam produzir; no "
            "curto prazo, com capital fixo, mais produto exige mais horas e mais trabalhadores.",
            "Duas formulações: em crescimento, " + vd("Δu = −β(g − ḡ)") + " (o desemprego cai quando o PIB "
            "cresce acima da taxa normal ḡ); em hiato, " + vd("u − u<sub>n</sub> = −β·(Y − Y*)/Y*") + " "
            "(produto acima do potencial → desemprego abaixo da taxa natural).",
            "“Produto de equilíbrio”, no contexto de modelos de curto prazo (IS-LM, OA-DA, Mundell-Fleming), é o "
            "produto efetivo determinado pela demanda. Uma política que o eleva reduz o desemprego, e a Lei de "
            "Okun dá a ordem de grandeza.",
            "Qualificações: o coeficiente não é unitário nem fixo (a produtividade e a força de trabalho também "
            "crescem; as firmas ajustam primeiro as horas); há defasagens; e existem as “recuperações sem "
            "emprego” (<i>jobless recovery</i>). No " + rx("Brasil") + ", a informalidade amortece a resposta "
            "do desemprego às variações do PIB.",
            "Exemplo brasileiro: na recessão de 2015–2016 (queda acumulada do PIB de cerca de " + vd("7%")
            + "), a desocupação mais que dobrou, de cerca de 6,5% para mais de 12%.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Enunciado simples, sem modulador, que descreve o sentido da "
                       "relação. O risco é o excesso de zelo: “produto de equilíbrio” pode parecer produto "
                       "potencial, e “estabelece” parece forte para uma regularidade empírica. Para o CEBRASPE, "
                       "basta o sentido correto da relação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A lei de Okun estabelece que cada ponto percentual de crescimento do PIB reduz em um ponto "
            "percentual a taxa de desemprego.”</i> → ERRADO (dado alterado: a relação não é unitária)",
            "<i>“Segundo a lei de Okun, o desemprego tende a subir quando o PIB cresce abaixo de sua taxa "
            "normal.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Relação empírica de Okun (1962): produto acima do potencial reduz o desemprego; "
                            "coeficiente varia por país; fórmula Δu = −β(g − ḡ); qualificações (produtividade, "
                            "horas, jobless recovery); exemplo brasileiro 2015–2016.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 134", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01277-1, ECO-E2-L01596-1 (Lei de Okun)"],
    },
    # ------------------------------------------------------------------ E1-0307
    {
        "id": "ECO-E1-0307-1", "fonte_ref": "E1-0307", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_SMI,
        "rotulo_item": "Item",
        "assertiva": ("Um argumento favorável à existência de um emprestador internacional de última instância é a "
                      "função que este exerceria de proporcionar liquidez para amenizar as alterações necessárias "
                      "nos valores das moedas e para impedir mudanças inconsistentes com os fundamentos "
                      "econômicos, uma vez que existem bancos centrais nacionais que perseguem políticas monetárias "
                      "distintas, de modo que alterações no valor das moedas são inevitáveis."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um argumento favorável à existência de um emprestador internacional de última instância é a "
                      "função que este exerceria de <u>proporcionar liquidez</u> para <u>amenizar</u> as "
                      "alterações necessárias nos valores das moedas e para <u>impedir mudanças inconsistentes "
                      "com os fundamentos</u> econômicos, uma vez que existem bancos centrais nacionais que "
                      "perseguem políticas monetárias distintas, de modo que alterações no valor das moedas são "
                      "inevitáveis."),
        "poucas": ("Com políticas monetárias nacionais divergentes, o câmbio vai mudar; o "
                   + azb("emprestador internacional de última instância") + " fornece liquidez para que o ajuste "
                   "necessário seja gradual e para conter ataques especulativos que " + vd("descolam") + " as "
                   "moedas dos fundamentos."),
        "destrinchando": [
            "No plano doméstico, o " + azb("emprestador de última instância") + " é o banco central que empresta "
            "a bancos solventes, mas sem liquidez, numa corrida (a doutrina clássica de " + oc("Walter Bagehot")
            + ", <i>Lombard Street</i>, 1873). A pergunta internacional é: quem faz isso para <b>países</b> que "
            "ficam sem divisas?",
            "O argumento do item tem duas partes: (1) mudanças de câmbio são inevitáveis, porque cada banco "
            "central persegue sua própria política; (2) sem um provedor de liquidez, essas mudanças tendem a ser "
            "bruscas e a ultrapassar o necessário — <i>overshooting</i>, pânico, fuga de capitais, crises "
            "autorrealizáveis. A liquidez internacional suaviza o ajuste legítimo e impede o ilegítimo.",
            oc("Charles Kindleberger") + " (<i>The World in Depression, 1929–1939</i>) incluiu essa função entre "
            "as tarefas do " + azb("estabilizador hegemônico") + ": a ausência de um emprestador internacional "
            "de última instância em 1929–1931 (o Reino Unido já não podia, os EUA ainda não queriam) ajudou a "
            "transformar a crise em depressão.",
            "Na prática, a função é exercida de forma incompleta: pelo " + azb("FMI") + " (com recursos limitados "
            "e condicionalidades) e pelas " + azb("linhas de swap") + " do Federal Reserve com outros bancos "
            "centrais (2008 e 2020). No " + rx("Brasil") + ", o Fed abriu linhas de swap com o BCB em 2008 (US$ 30 "
            "bilhões) e em 2020 (US$ 60 bilhões).",
            "Objeção clássica: o " + azb("risco moral") + " — a certeza de socorro estimula políticas "
            "irresponsáveis e credores imprudentes. Daí a regra de Bagehot: emprestar livremente, a juros "
            "punitivos, contra boa garantia.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item longo e abstrato, de vocabulário técnico, que reproduz um "
                       "argumento de manual. O risco é o candidato achar contraditório “alterações necessárias” e "
                       "“impedir mudanças”: o item distingue as mudanças <b>coerentes</b> com os fundamentos (que "
                       "se suavizam) das <b>incoerentes</b> (que se impedem)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A existência de um emprestador internacional de última instância elimina a necessidade de "
            "ajustes cambiais entre países com políticas monetárias distintas.”</i> → ERRADO (modulador absoluto: "
            "ele só suaviza ajustes inevitáveis)",
            "<i>“Um argumento contrário ao emprestador internacional de última instância é o risco moral que ele "
            "geraria sobre governos e credores.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Correto. A alternativa é exaustiva no que há de relevante ao tema.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [provavel(2017)],
    },
    # ------------------------------------------------------------------ E1-0317
    {
        "id": "ECO-E1-0317-1", "fonte_ref": "E1-0317", "destino": "65", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False,
        "errei": False,
        "comando": CMD_SMI,
        "rotulo_item": "Item",
        "assertiva": ("Em um regime conhecido como Caixa de Conversão, como o que vigorou no Brasil no começo do "
                      "século 20, a autoridade monetária autorizada emite moeda nacional somente no caso de deficit "
                      "comercial, a uma taxa de conversão pré-fixada, que é mantida constante durante a vigência "
                      "desse mecanismo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um regime conhecido como Caixa de Conversão, como o que vigorou no Brasil no começo do "
                       "século 20, a autoridade monetária autorizada emite moeda nacional somente ")
                    + vm("no caso de deficit comercial") + az(", a uma taxa de conversão pré-fixada, que é mantida "
                                                               "constante durante a vigência desse mecanismo.")),
        "poucas": ("A " + azb("Caixa de Conversão") + " só emite moeda " + vd("contra a entrada de ouro") + " (ou "
                   "divisas conversíveis): a base monetária cresce com " + vm("superávit") + " no balanço de "
                   "pagamentos, nunca com déficit."),
        "destrinchando": [
            "Lógica de " + azb("currency board") + ": cada unidade de moeda nacional emitida tem lastro integral "
            "em reservas, à taxa fixa. A oferta de moeda vira variável <b>endógena</b> do balanço de pagamentos: "
            "entra ouro (superávit comercial ou entrada de capitais) → emite-se; sai ouro (déficit) → a moeda é "
            "resgatada e a base encolhe.",
            "Com déficit comercial, os importadores precisam de ouro e divisas para pagar o exterior: entregam "
            "notas e retiram lastro — a base monetária " + vd("diminui") + ". É o ajuste automático do "
            "padrão-ouro (mecanismo preço-espécie de " + oc("Hume") + ").",
            "No " + rx("Brasil") + ": a " + rx("Caixa de Conversão") + " foi criada em " + vd("1906") + " (governo "
            "Afonso Pena), no contexto do Convênio de Taubaté e da valorização do café. Emitia notas conversíveis "
            "à taxa de " + vd("15 pence por mil-réis") + " (revista para 16 pence em 1910), para impedir que a "
            "entrada de capitais apreciasse o mil-réis e prejudicasse os cafeicultores.",
            "Funcionou enquanto houve superávit e entrada de capitais externos; com a fuga de ouro na crise de "
            "1913–1914 e o início da Primeira Guerra Mundial, a conversibilidade foi suspensa e a Caixa, "
            "encerrada (1914). Experiência parecida: a Caixa de Estabilização (1926–1930), no governo "
            "Washington Luís, que ruiu com a crise de 1929.",
            "Paralelo moderno: o currency board da Argentina (Plano de Conversibilidade, 1991–2001, 1 peso = "
            "1 dólar) e o de Hong Kong (desde 1983).",
            vm("Regra-âncora: caixa de conversão → moeda só nasce de reservas que entram (superávit)."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sinal do balanço: superávit → déficit. Pista: num regime de "
                       "lastro, déficit significa <b>saída</b> de reservas, e não há como emitir sem reservas "
                       "entrando. O resto (taxa pré-fixada e constante) descreve corretamente o mecanismo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na Caixa de Conversão, a expansão da base monetária dependia da entrada de ouro e divisas no "
            "país.”</i> → CERTO",
            "<i>“A Caixa de Conversão de 1906 buscava impedir a desvalorização do mil-réis, para baratear as "
            "importações.”</i> → ERRADO (inversão: buscava impedir a apreciação, em favor do café)",
        ])],
        "reescrita": ("Em um regime conhecido como Caixa de Conversão, como o que vigorou no Brasil no começo do "
                      "século 20, a autoridade monetária autorizada emite moeda nacional somente "
                      + hl("contra a entrada de ouro ou divisas conversíveis, o que pressupõe superávit no balanço "
                           "de pagamentos") + ", a uma taxa de conversão pré-fixada, que é mantida constante durante "
                      "a vigência desse mecanismo."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["somente"], "dificuldade": 2,
        "comentario_fonte": "A Caixa de Conversão emitia bilhetes conversíveis apenas com lastro em ouro (libra "
                            "e/ou dólar): só o superávit comercial, e não o déficit, permitia expandir a base "
                            "monetária.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [provavel(2020)],
    },
    # ------------------------------------------------------------------ E1-0454
    {
        "id": "ECO-E1-0454-1", "fonte_ref": "E1-0454", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("A década de 1980 ficou marcada por instabilidade econômica, aceleração inflacionária e "
                    "sucessivos planos de ajuste. Considerando esse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A crise da dívida externa nos anos 1980 foi desencadeada, em parte, pela elevação abrupta "
                      "das taxas de juros internacionais e pela deterioração dos termos de troca, comprometendo a "
                      "solvência externa dos países latino-americanos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A crise da dívida externa nos anos 1980 foi desencadeada, <u>em parte</u>, pela elevação "
                      "abrupta das taxas de juros internacionais e pela deterioração dos termos de troca, "
                      "comprometendo a solvência externa dos países latino-americanos."),
        "poucas": ("O " + azb("choque Volcker") + " (juros dos EUA perto de " + vd("20%") + " em 1979–1981) "
                   "encareceu a dívida contratada a juros flutuantes, e a recessão mundial derrubou os preços das "
                   "exportações: a moratória do México (" + vd("1982") + ") abriu a crise."),
        "destrinchando": [
            "Origem: nos anos 1970, os bancos privados reciclaram os " + azb("petrodólares") + " emprestando à "
            "América Latina a " + azb("juros flutuantes") + " (indexados à Libor ou à <i>prime rate</i>). O "
            + rx("Brasil") + " financiou assim o II PND e os déficits causados pelo choque do petróleo.",
            "Os choques de 1979–1982: (1) " + oc("Paul Volcker") + ", no Fed, elevou os juros para conter a "
            "inflação americana — o serviço da dívida explodiu; (2) o " + azb("segundo choque do petróleo")
            + " (1979) encareceu as importações; (3) a recessão nos países ricos reduziu a demanda e os preços "
            "das commodities exportadas — " + azb("termos de troca") + " em queda; (4) o dólar se apreciou, "
            "pesando sobre dívidas em dólar.",
            "Em agosto de " + vd("1982") + ", o México declarou não poder pagar; os bancos cortaram o crédito "
            "voluntário para toda a região. Seguiu-se a " + azb("década perdida") + ": ajustes recessivos com o "
            "FMI, transferência líquida de recursos ao exterior, aceleração inflacionária. O Brasil decretou "
            "moratória em " + vd("1987") + " (governo Sarney).",
            "Saídas: Plano Baker (1985, novos empréstimos condicionados a reformas) e " + azb("Plano Brady")
            + " (1989): troca da dívida bancária por títulos com desconto ou juros reduzidos, garantidos por "
            "títulos do Tesouro americano. O Brasil concluiu seu acordo Brady em 1994.",
            "Por que “em parte”: havia também causas internas — endividamento excessivo, déficits fiscais, "
            "estratégias de crescimento financiadas com poupança externa.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Item de manual, protegido pelo “em parte”, "
                       "que admite as causas internas. O risco é o candidato achar que só a irresponsabilidade "
                       "doméstica explicaria a crise. 🔥 A banca adora trocar o choque de juros por “queda dos "
                       "juros internacionais” ou atribuir a crise ao primeiro choque do petróleo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A crise da dívida dos anos 1980 decorreu exclusivamente da indisciplina fiscal dos países "
            "latino-americanos.”</i> → ERRADO (modulador absoluto: houve choques externos decisivos)",
            "<i>“A queda das taxas de juros internacionais no início dos anos 1980 aliviou o serviço da dívida "
            "latino-americana.”</i> → ERRADO (inversão: os juros subiram)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["em parte"], "dificuldade": 1,
        "comentario_fonte": "A década perdida começou com a moratória do México em 1982, resultado do choque "
                            "Volcker e da recessão global, que encareceram o serviço da dívida e reduziram as "
                            "receitas de exportação.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0464
    {
        "id": "ECO-E1-0464-1", "fonte_ref": "E1-0464", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_SMI,
        "rotulo_item": "Item",
        "assertiva": ("Na Conferência de Bretton Woods, Keynes, como representante do Reino Unido, teve papel "
                      "ativo e central na construção de uma governança financeira global. Nessa conferência, Keynes "
                      "sugeriu um regime de taxas de câmbio flutuantes como forma de apoiar o crescimento do "
                      "comércio internacional, que foi fundamental para a recuperação econômica do pós-guerra."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na Conferência de Bretton Woods, Keynes, como representante do Reino Unido, teve papel "
                       "ativo e central na construção de uma governança financeira global. Nessa conferência, "
                       "Keynes sugeriu um regime de taxas de câmbio ") + vm("flutuantes")
                    + az(" como forma de apoiar o crescimento do comércio internacional, que foi fundamental para "
                         "a recuperação econômica do pós-guerra.")),
        "poucas": ("Keynes e White defendiam " + azb("câmbio fixo, porém ajustável") + " (<i>adjustable peg</i>). "
                   "A diferença entre eles estava no meio de liquidação: " + vd("bancor") + " (Keynes) × "
                   + vd("dólar conversível em ouro") + " (White)."),
        "destrinchando": [
            "Contexto: a experiência dos anos 1930 — desvalorizações competitivas (“empobrecer o vizinho”), "
            "controles, blocos comerciais, colapso do comércio — convenceu britânicos e americanos de que o "
            "pós-guerra exigia " + azb("estabilidade cambial") + " com alguma flexibilidade. Ninguém, em 1944, "
            "propunha flutuação generalizada.",
            azb("Plano Keynes") + " (Reino Unido): " + vd("União Internacional de Compensação") + " (<i>International "
            "Clearing Union</i>), com uma moeda contábil supranacional, o " + vd("bancor") + "; saldos de "
            "deficitários e superavitários penalizados de forma <b>simétrica</b>; grandes facilidades de "
            "saque. Interesse de um país devedor e com reservas escassas.",
            azb("Plano White") + " (EUA, " + oc("Harry Dexter White") + "): um fundo de estabilização com "
            "cotas, recursos limitados, ajuste a cargo do deficitário e o dólar conversível em ouro no centro. "
            "Interesse do grande credor. Prevaleceu: daí o " + azb("FMI") + " e o padrão " + vd("ouro-dólar")
            + " (US$ 35 por onça).",
            "O regime acordado: paridades fixas em relação ao dólar (margem de 1%), alteráveis em caso de "
            + azb("desequilíbrio fundamental") + " do balanço de pagamentos, com consulta ao FMI; controles de "
            "capital permitidos. A flutuação generalizada só veio com o colapso do sistema (1971–1973) e foi "
            "legalizada pelos Acordos da Jamaica (1976).",
            "A primeira oração do item está certa: " + oc("Keynes") + " chefiou a delegação britânica e foi o "
            "principal formulador intelectual da conferência, ainda que derrotado no desenho final.",
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " Primeira frase verdadeira (o papel de "
                       "Keynes), segunda com o regime trocado. Pista: o objetivo declarado em Bretton Woods era "
                       "<b>evitar</b> a instabilidade cambial do entreguerras; “flutuante” contradiz o próprio "
                       "espírito da conferência. 🔥 Itens sobre os planos costumam trocar bancor × dólar ou "
                       "inverter Keynes × White."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Tanto o plano de Keynes quanto o de White previam taxas de câmbio fixas, mas ajustáveis.”</i> → "
            "CERTO",
            "<i>“O plano de Keynes atribuía exclusivamente aos países deficitários o ônus do ajuste externo.”</i> "
            "→ ERRADO (inversão: o ajuste seria simétrico; o ônus no deficitário era a lógica do plano White)",
        ])],
        "reescrita": ("Na Conferência de Bretton Woods, Keynes, como representante do Reino Unido, teve papel ativo "
                      "e central na construção de uma governança financeira global. Nessa conferência, Keynes "
                      "sugeriu um regime de taxas de câmbio " + hl("fixas, porém ajustáveis,") + " como forma de "
                      "apoiar o crescimento do comércio internacional, que foi fundamental para a recuperação "
                      "econômica do pós-guerra."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Keynes chefiou a delegação britânica; White fez valer o poder americano e instituiu "
                            "câmbio fixo centrado no dólar lastreado em ouro. Ambos defendiam câmbio fixo ajustável; "
                            "Keynes propôs o bancor e a união de compensação, White o dólar conversível em ouro "
                            "(versos fundidos de duas linhas da fonte).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 380", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 381", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia o enunciado)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00274-1 (mesmo item em outra prova)", provavel(2017),
                    "duplicata: verso da linha E3-L00274 (mesmo item) fundido neste card",
                    "quase_duplicata: ECO-E2-L00361-1, ECO-E2-L00486-1 (planos Keynes × White)"],
    },
    # ------------------------------------------------------------------ E1-0779
    {
        "id": "ECO-E1-0779-1", "fonte_ref": "E1-0779", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": True,
        "comando": "Acerca do sistema monetário internacional e do papel das moedas de reserva, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Uma transição para um sistema monetário internacional multipolar, no qual os ativos "
                      "denominados em várias moedas são globalmente reconhecidos como seguros e líquidos, "
                      "pressupõe a existência de sólida coordenação e de políticas estáveis entre os governos "
                      "emissores das moedas de reserva."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma transição para um sistema monetário internacional multipolar, no qual os ativos "
                      "denominados em várias moedas são globalmente reconhecidos como seguros e líquidos, "
                      "<u>pressupõe</u> a existência de sólida coordenação e de políticas estáveis entre os "
                      "governos emissores das moedas de reserva."),
        "poucas": ("Várias moedas só funcionam juntas como reserva se cada uma for " + azb("confiável") + " "
                   "(política estável) e se seus emissores se " + azb("coordenarem") + " — senão, a troca "
                   "rápida entre elas gera instabilidade cambial."),
        "destrinchando": [
            "Hoje o sistema é " + azb("unipolar") + ": o dólar responde por cerca de " + vd("57–58%") + " das "
            "reservas cambiais identificadas e pela maior parte do faturamento comercial e das dívidas em moeda "
            "estrangeira ⏳ (out/2026). Um sistema " + azb("multipolar") + " teria euro, renminbi e outras moedas "
            "dividindo essas funções.",
            "Para uma moeda ser reserva, seus ativos precisam ser " + vd("seguros") + " (baixo risco de "
            "calote, de inflação e de confisco) e " + vd("líquidos") + " (mercados profundos de títulos, livre "
            "conversibilidade). Isso exige políticas estáveis do emissor: disciplina fiscal, banco central "
            "crível, Estado de direito.",
            "Por que a " + azb("coordenação") + ": com várias moedas substitutas próximas, os investidores trocam "
            "de uma para outra ao menor sinal de divergência de políticas. Sem coordenação, um sistema "
            "multipolar pode ser <b>mais</b> volátil que o unipolar (o entreguerras, com libra e dólar "
            "disputando, é o exemplo histórico).",
            "Entraves atuais: o euro carece de um título soberano comum profundo; o renminbi tem conta de "
            "capital controlada. Por isso a transição, se ocorrer, tende a ser lenta.",
            "Para o " + rx("Brasil") + " e os BRICS, a discussão aparece nas propostas de comércio em moedas "
            "locais e de redução da dependência do dólar.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Item de CACD tirado de texto analítico: afirma uma condição "
                       "(“pressupõe”) razoável e bem fundamentada. O risco é achar o verbo forte demais. Pista: "
                       "o próprio item define multipolaridade pela confiança nos ativos — e confiança depende de "
                       "política estável."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um sistema monetário multipolar dispensaria a coordenação entre os emissores, pois a "
            "concorrência entre moedas disciplinaria automaticamente suas políticas.”</i> → ERRADO (contradição: "
            "a concorrência sem coordenação gera volatilidade)",
            "<i>“A liquidez dos ativos denominados em uma moeda é condição para que ela exerça a função de reserva "
            "internacional.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["pressupõe"], "dificuldade": 2,
        "comentario_fonte": "Num sistema multipolar, coordenação e estabilidade das economias emissoras tornam-se "
                            "centrais: a má condução da política de um emissor afeta a estabilidade de todo o "
                            "sistema; confiança e liquidez dependem de políticas estáveis.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: o item pertence a bloco de prova com texto motivador que a fonte não "
                    "preservou; comando neutro"],
    },
    # ------------------------------------------------------------------ E1-0781
    {
        "id": "ECO-E1-0781-1", "fonte_ref": "E1-0781", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": "Acerca do sistema monetário internacional e do papel das moedas de reserva, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O domínio do dólar durante grande parte dos últimos 75 anos é considerado, por alguns "
                      "economistas, uma “anomalia histórica”, já que, antes do padrão-ouro, a prata, o ouro e os "
                      "blocos bimetálicos coexistiam e interagiam; no período entre as duas grandes guerras "
                      "mundiais, a libra esterlina e o dólar contribuíram para o estoque de liquidez global."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O domínio do dólar durante grande parte dos últimos 75 anos é considerado, <u>por alguns "
                      "economistas</u>, uma “anomalia histórica”, já que, antes do padrão-ouro, a prata, o ouro e "
                      "os blocos bimetálicos coexistiam e interagiam; no período entre as duas grandes guerras "
                      "mundiais, a libra esterlina e o dólar contribuíram para o estoque de liquidez global."),
        "poucas": ("A história monetária foi quase sempre " + azb("multipolar") + " (metais e blocos no "
                   "século XIX; libra e dólar no entreguerras); a hegemonia quase solitária do dólar depois de "
                   + vd("1945") + " é a exceção."),
        "destrinchando": [
            "Antes do padrão-ouro clássico (consolidado a partir de " + vd("1870") + "), conviviam três blocos: "
            "o do ouro, em torno do Império Britânico; o " + azb("bimetálico") + " (ouro e prata), em torno da "
            "França e da União Monetária Latina; e o da prata, da Europa oriental à Ásia.",
            "No padrão-ouro clássico (1870–1914), a libra era a principal moeda internacional, mas franco e "
            "marco também serviam como reserva. No " + azb("entreguerras") + ", sob o " + azb("padrão "
            "câmbio-ouro") + " (Conferência de Gênova, " + vd("1922") + "), os bancos centrais guardavam libras "
            "e dólares ao lado do ouro: as duas moedas dividiram a provisão de liquidez.",
            "Só depois de Bretton Woods (" + vd("1944") + ") o dólar se tornou a âncora única do sistema — e "
            "manteve a primazia mesmo após o fim da conversibilidade em ouro (1971), graças à profundidade do "
            "mercado de títulos do Tesouro americano e aos efeitos de rede.",
            oc("Barry Eichengreen") + " (<i>Exorbitant Privilege</i>, 2011) é a referência mais citada da tese: "
            "o mundo de uma moeda só é a anomalia, e o futuro tende a ser multipolar. O argumento serve de base "
            "aos debates sobre desdolarização.",
            "Leitura do conector: o “já que” liga a tese a duas evidências históricas verdadeiras — o item não "
            "afirma que a tese é consensual, apenas que “alguns economistas” a sustentam.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Atribuição prudente (“por alguns "
                       "economistas”) seguida de fatos históricos corretos. O risco é estranhar a palavra "
                       "“anomalia” ou duvidar da coexistência libra–dólar no entreguerras. Pista: quando o item "
                       "atribui a tese a “alguns”, a banca só cobra se os fatos de apoio estão certos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No período entre as guerras, a libra esterlina foi a única moeda de reserva internacional, papel "
            "que o dólar só assumiu em 1944.”</i> → ERRADO (restrição indevida: libra e dólar dividiam o papel)",
            "<i>“Antes da generalização do padrão-ouro, sistemas monetários baseados na prata e bimetálicos "
            "coexistiam com o padrão-ouro britânico.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["por alguns economistas"],
        "dificuldade": 2,
        "comentario_fonte": "A hegemonia do dólar no pós-1945 é vista como sem precedentes; antes de 1870 "
                            "coexistiam blocos do ouro, bimetálico e da prata; no entreguerras, libra e dólar "
                            "forneceram liquidez (câmbio-ouro, Gênova 1922). Referências a Eichengreen.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: o item pertence a bloco de prova com texto motivador que a fonte não "
                    "preservou; comando neutro"],
    },
    # ------------------------------------------------------------------ E1-0976
    {
        "id": "ECO-E1-0976-1", "fonte_ref": "E1-0976", "destino": "65", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_SMI,
        "rotulo_item": "Item",
        "assertiva": ("No século XIX, o padrão-ouro internacional manteve as taxas de câmbio em faixa determinada "
                      "pelos custos de transporte, o que impediu movimentos persistentes das taxas de câmbio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No século XIX, o padrão-ouro internacional manteve as taxas de câmbio em <u>faixa "
                      "determinada pelos custos de transporte</u>, o que impediu movimentos persistentes das taxas "
                      "de câmbio."),
        "poucas": ("No padrão-ouro, o câmbio só oscilava entre os " + azb("pontos de ouro") + ": a paridade "
                   "metálica " + vd("± o custo de transportar e segurar o ouro") + ". Fora dessa faixa, era "
                   "mais barato embarcar o metal."),
        "destrinchando": [
            "Cada moeda valia um peso fixo de ouro; a razão entre esses pesos dava a " + azb("paridade da casa da "
            "moeda") + " (<i>mint parity</i>) — por exemplo, cerca de US$ 4,87 por libra antes de 1914.",
            "Se o câmbio de mercado subisse acima da paridade + custo de frete, seguro e juros do ouro em "
            "trânsito (o " + azb("ponto de exportação de ouro") + "), o devedor preferia comprar ouro em casa e "
            "embarcá-lo. Abaixo da paridade − esses custos (" + azb("ponto de importação") + "), ocorria o "
            "contrário. A arbitragem mantinha o câmbio dentro da banda.",
            "Por isso as taxas oscilavam pouco e de forma temporária: os desvios persistentes eram cortados pelos "
            "fluxos de metal, e estes, pelo mecanismo preço-espécie de " + oc("Hume") + ", corrigiam o próprio "
            "desequilíbrio do balanço de pagamentos.",
            "Atenção: o custo de transporte relevante é o do <b>ouro</b>, não o das mercadorias. Os pontos de ouro "
            "funcionam como as margens de flutuação de um regime de bandas cambiais, só que definidas pela "
            "tecnologia de transporte e pelos juros, não por decisão do governo.",
            "Ressalva histórica: a estabilidade valia para o núcleo (Reino Unido, França, Alemanha, EUA). Na "
            "periferia — " + rx("Brasil") + " incluído —, a adesão era intermitente, com suspensões da "
            "conversibilidade e desvalorizações.",
        ],
        "dissecando": (cz("[detalhe]") + " Item verdadeiro por um conceito pouco lembrado: os pontos de ouro. O "
                       "risco é ler “custos de transporte” como custo de frete das mercadorias e achar a frase sem "
                       "sentido. Pista: no padrão-ouro, a única “flexibilidade” do câmbio era a banda dada pelo "
                       "custo de mover o metal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No padrão-ouro clássico, as taxas de câmbio eram rigorosamente fixas, sem qualquer margem de "
            "oscilação em torno da paridade.”</i> → ERRADO (modulador absoluto: oscilavam entre os pontos de "
            "ouro)",
            "<i>“Uma redução dos custos de transporte do ouro estreitaria a faixa de oscilação das taxas de "
            "câmbio no padrão-ouro.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Correto; o padrão-ouro permitia correções nominais decorrentes da alteração dos "
                            "custos de transporte (de mercadorias), preservando a competitividade do exportador.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [provavel(2014),
                    "qualidade_fonte: o comentário de origem associa a faixa ao custo de transporte das "
                    "mercadorias e à competitividade do exportador; a faixa é dada pelos pontos de ouro (custo de "
                    "embarcar o metal) — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L00360
    {
        "id": "ECO-E2-L00360-1", "fonte_ref": "E2-L00360", "destino": "65", "subtema": H2["ouro"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("O Padrão-Ouro Clássico (1870-1914) operava sob a lógica do “mecanismo de fluxo de preços em "
                      "espécie” de David Hume, que previa que desequilíbrios no Balanço de Pagamentos seriam "
                      "corrigidos automaticamente pela movimentação física do metal, sem a necessidade de "
                      "intervenções discricionárias dos Bancos Centrais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Padrão-Ouro Clássico (1870-1914) operava sob a lógica do “mecanismo de fluxo de preços em "
                      "espécie” de David Hume, que previa que desequilíbrios no Balanço de Pagamentos seriam "
                      "corrigidos <u>automaticamente</u> pela movimentação física do metal, sem a necessidade de "
                      "intervenções discricionárias dos Bancos Centrais."),
        "poucas": ("No modelo de " + oc("Hume") + ", o ouro que sai do país deficitário reduz sua oferta de moeda "
                   "e seus preços, o que estimula exportações e corta importações: o " + azb("ajuste é "
                   "automático") + "."),
        "destrinchando": [
            oc("David Hume") + " (<i>Of the Balance of Trade</i>, 1752) formulou o " + azb("mecanismo "
            "preço-espécie-fluxo") + " contra os mercantilistas, que queriam acumular metal indefinidamente com "
            "superávits.",
            "Cadeia do ajuste: " + vd("déficit → saída de ouro → M ↓ → P ↓ (teoria quantitativa) → "
            "exportações ↑, importações ↓ → déficit some") + ". No superavitário, o inverso: entra ouro, preços "
            "sobem, a competitividade cai. O metal se redistribui até equilibrar as balanças.",
            "Corolário: a acumulação permanente de ouro é impossível — superávits se autocorrigem. E a moeda é "
            "endógena ao balanço de pagamentos: não há política monetária autônoma.",
            "Na prática do padrão-ouro clássico, os bancos centrais ajudavam o ajuste pelas " + azb("“regras do "
            "jogo”") + " (subir a taxa de redesconto quando perdiam ouro), e o Banco da Inglaterra atraía "
            "capitais de curto prazo pelos juros — canal financeiro mais rápido que o de preços. Estudos "
            "históricos mostram que as regras eram frequentemente descumpridas.",
            "Daí a leitura do item: ele descreve a <b>lógica</b> teórica do sistema (“operava sob a lógica”), e "
            "não a ausência total de bancos centrais.",
            vm("Regra-âncora: Hume = déficit → sai ouro → preços caem → ajuste automático."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Descreve o modelo de manual. O risco é o "
                       "candidato que conhece as “regras do jogo” e o papel do Banco da Inglaterra marcar ERRADO "
                       "por causa do “sem intervenções discricionárias”. Pista: o item fala da lógica do "
                       "mecanismo que Hume previa, não da prática histórica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mecanismo de Hume, o país superavitário acumularia ouro indefinidamente, sem efeitos sobre "
            "seus preços internos.”</i> → ERRADO (contradição: a entrada de ouro eleva os preços e corrige o "
            "superávit)",
            "<i>“O mecanismo preço-espécie-fluxo pressupõe a teoria quantitativa da moeda.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["automaticamente"], "dificuldade": 1,
        "comentario_fonte": "Déficit no BP → saída de ouro → queda da oferta de moeda → queda de preços → "
                            "aumento das exportações → reequilíbrio.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00361
    {
        "id": "ECO-E2-L00361-1", "fonte_ref": "E2-L00361", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A Conferência de Bretton Woods (1944) resultou na vitória do Plano Keynes sobre o Plano "
                      "White, estabelecendo a criação da International Clearing Union e de uma moeda contábil "
                      "supranacional, o Bancor, para evitar a hegemonia de uma moeda nacional no sistema."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A Conferência de Bretton Woods (1944) resultou na vitória do Plano ") + vm("Keynes")
                    + az(" sobre o Plano ") + vm("White") + az(", estabelecendo ")
                    + vm("a criação da International Clearing Union e de uma moeda contábil "
                         "supranacional, o Bancor, para evitar a hegemonia de uma moeda nacional no sistema")
                    + az(".")),
        "poucas": ("Venceu o " + azb("Plano White") + " (EUA): criou-se o " + vd("FMI") + " e o padrão "
                   + vd("ouro-dólar") + ", que consolidou a hegemonia do dólar. Clearing Union e bancor eram o "
                   "plano derrotado de Keynes."),
        "destrinchando": [
            azb("Plano Keynes") + ": União Internacional de Compensação, com o " + vd("bancor") + " como moeda "
            "contábil dos bancos centrais; facilidades de saque generosas (da ordem de US$ 26 bilhões, na "
            "proposta) e ajuste <b>simétrico</b>, com encargos também sobre os superavitários.",
            azb("Plano White") + ": fundo de estabilização com cotas subscritas em ouro e moedas (cerca de "
            + vd("US$ 8,8 bilhões") + " no acordo final), saques limitados às cotas, ônus do ajuste no "
            "deficitário e o dólar, conversível em ouro a " + vd("US$ 35 por onça") + ", como âncora.",
            "Por que White venceu: os EUA detinham perto de dois terços das reservas de ouro do mundo, eram o "
            "grande credor e não aceitariam financiar sem limites os déficits alheios. O Reino Unido, "
            "endividado, dependia da ajuda americana.",
            "Resultado institucional: " + azb("FMI") + " (estabilidade cambial e crédito de curto prazo ao balanço "
            "de pagamentos) e " + azb("BIRD") + " (reconstrução e desenvolvimento); paridades fixas, mas "
            "ajustáveis em desequilíbrio fundamental. O bancor ressurge como ideia nos DES (1969) e nas "
            "propostas de moeda supranacional depois de 2008.",
            vm("Regra-âncora: Keynes = bancor + Clearing Union (perdeu); White = FMI + dólar-ouro (venceu)."),
        ],
        "dissecando": (cz("[inversão · troca de ator]") + " O item inverte vencedor e vencido e, coerentemente, "
                       "descreve o plano derrotado como resultado. Pista: o sistema que saiu de Bretton Woods é "
                       "chamado de padrão <b>ouro-dólar</b> — nome que já entrega a hegemonia de uma moeda "
                       "nacional."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O sistema acordado em Bretton Woods tinha o dólar, conversível em ouro, como moeda-âncora.”</i> → "
            "CERTO",
            "<i>“O FMI foi concebido a partir da International Clearing Union proposta por Keynes.”</i> → ERRADO "
            "(troca de ator: deriva do fundo de estabilização de White)",
        ])],
        "reescrita": ("A Conferência de Bretton Woods (1944) resultou na vitória do Plano " + hl("White")
                      + " sobre o Plano " + hl("Keynes") + ", estabelecendo " + hl("o FMI e o padrão ouro-dólar, "
                      "com o dólar conversível em ouro como âncora, o que consolidou a hegemonia de uma moeda "
                      "nacional no sistema") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Foi o contrário: o Plano White venceu o Plano Keynes; adotou-se a paridade "
                            "dólar-ouro, e não o bancor supranacional, consolidando a hegemonia do dólar.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0464-1, ECO-E2-L00486-1 (planos Keynes × White)"],
    },
    # ------------------------------------------------------------------ E2-L00362
    {
        "id": "ECO-E2-L00362-1", "fonte_ref": "E2-L00362", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("O chamado “Dilema de Triffin” aponta para uma contradição inerente ao sistema de Bretton "
                      "Woods: para prover liquidez ao comércio global, os EUA precisariam incorrer em déficits "
                      "persistentes, mas esses mesmos déficits minariam, a longo prazo, a confiança na "
                      "conversibilidade do dólar em ouro."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O chamado “Dilema de Triffin” aponta para uma contradição inerente ao sistema de Bretton "
                      "Woods: para prover liquidez ao comércio global, os EUA precisariam incorrer em <u>déficits "
                      "persistentes</u>, mas esses mesmos déficits minariam, a longo prazo, a <u>confiança na "
                      "conversibilidade</u> do dólar em ouro."),
        "poucas": ("O mundo só recebia dólares se os EUA tivessem " + azb("déficits") + " no balanço de "
                   "pagamentos; mas, quanto mais dólares fora, menor o lastro em ouro por dólar e menor a "
                   + azb("confiança") + " na conversibilidade a US$ 35."),
        "destrinchando": [
            oc("Robert Triffin") + " (<i>Gold and the Dollar Crisis</i>, " + vd("1960") + ") mostrou a "
            "contradição: a oferta mundial de ouro crescia devagar; a liquidez adicional vinha de dólares, que "
            "só saíam dos EUA por déficits no balanço de pagamentos.",
            "Dois caminhos ruins: (1) se os EUA eliminassem os déficits, faltaria liquidez e o comércio "
            "mundial seria freado (tendência deflacionária); (2) se os mantivessem, os passivos externos em "
            "dólar ultrapassariam as reservas de ouro americanas, e a promessa de conversão perderia "
            "credibilidade — risco de corrida contra o dólar.",
            "Isso aconteceu: por volta de " + vd("1960") + ", os passivos externos em dólar já superavam o ouro "
            "dos EUA. Respostas paliativas: o " + azb("pool do ouro") + " (1961–1968), o duplo mercado do ouro "
            "(1968) e a criação dos " + azb("Direitos Especiais de Saque") + " (1969), um ativo de reserva que "
            "não dependia de déficits americanos.",
            "Desfecho: a França de De Gaulle converteu dólares em ouro; em agosto de " + vd("1971") + ", "
            + oc("Nixon") + " suspendeu a conversibilidade. O dilema tem versão contemporânea: a demanda mundial "
            "por ativos seguros em dólar exige que os EUA emitam dívida externa crescente.",
            vm("Regra-âncora: Triffin = liquidez exige déficit americano; déficit destrói confiança."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, reproduzida com precisão. O risco é inverter "
                       "a lógica (achar que superávits americanos dariam liquidez). Pista: liquidez em dólar para o "
                       "resto do mundo = dólares saindo dos EUA = déficit."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo Triffin, a liquidez internacional em Bretton Woods dependia de superávits persistentes no "
            "balanço de pagamentos dos EUA.”</i> → ERRADO (inversão: dependia de déficits)",
            "<i>“A criação dos Direitos Especiais de Saque, em 1969, foi uma tentativa de atenuar o dilema de "
            "Triffin.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Triffin identificou a falha em 1960: sem déficits americanos, falta liquidez; com "
                            "eles, o lastro em ouro se torna insuficiente.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00363
    {
        "id": "ECO-E2-L00363-1", "fonte_ref": "E2-L00363", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("Os Direitos Especiais de Saque (SDRs) do FMI são ativos de reserva internacional cujo valor é "
                      "determinado por uma cesta de moedas que, desde 2016, inclui o Renminbi (Yuan) chinês, "
                      "refletindo a ascensão da China no sistema financeiro global."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os Direitos Especiais de Saque (SDRs) do FMI são ativos de reserva internacional cujo valor "
                      "é determinado por uma cesta de moedas que, <u>desde 2016</u>, inclui o Renminbi (Yuan) "
                      "chinês, refletindo a ascensão da China no sistema financeiro global."),
        "poucas": ("O " + azb("DES/SDR") + " vale uma cesta de cinco moedas; o " + vd("renminbi") + " entrou em "
                   + vd("1º de outubro de 2016") + ", ao lado de dólar, euro, iene e libra."),
        "destrinchando": [
            "Os " + azb("Direitos Especiais de Saque") + " foram criados em " + vd("1969") + " (primeira emenda "
            "ao Convênio Constitutivo do FMI) para complementar as reservas de ouro e dólar — uma resposta ao "
            "dilema de Triffin. São alocados aos países-membros na proporção de suas cotas.",
            "Valor: de início, igual a 0,888671 g de ouro (= US$ 1); desde 1974, definido por uma " + azb("cesta "
            "de moedas") + ", revista a cada cinco anos. Critérios de entrada: ser moeda de grande exportador e "
            "ser " + azb("“livremente utilizável”") + " (amplamente usada em pagamentos e negociada nos "
            "principais mercados de câmbio).",
            "O FMI decidiu incluir o renminbi em novembro de " + vd("2015") + ", com vigência a partir de "
            + vd("outubro de 2016") + " — primeira moeda de país emergente na cesta. Pesos da revisão de 2022: "
            "dólar " + vd("43,38%") + ", euro " + vd("29,31%") + ", renminbi " + vd("12,28%") + ", iene "
            + vd("7,59%") + ", libra " + vd("7,44%") + " ⏳ (out/2026).",
            "A inclusão teve peso simbólico (reconhecimento da internacionalização do renminbi) maior que o "
            "efeito prático: o DES é pouco usado e o renminbi ainda responde por fatia pequena das reservas "
            "mundiais, por causa dos controles de capital chineses.",
            "Maiores alocações: " + vd("2009") + " (resposta à crise global) e " + vd("agosto de 2021") + " "
            "(cerca de US$ 650 bilhões, resposta à pandemia).",
        ],
        "dissecando": (cz("[detalhe]") + " Item factual: o dado decisivo é o ano de entrada do renminbi. "
                       "Pista: a decisão é de 2015 e a vigência, de 2016 — a banca pode trocar uma pela outra, ou "
                       "dizer que a cesta inclui o franco suíço ou o rublo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A cesta do DES é composta pelo dólar, pelo euro, pelo iene, pela libra e pelo franco "
            "suíço.”</i> → ERRADO (troca de ator: a quinta moeda é o renminbi)",
            "<i>“O DES foi criado em 1969 para complementar as reservas internacionais no sistema de Bretton "
            "Woods.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O yuan entrou na cesta do SDR em 1º de outubro de 2016, juntando-se ao dólar, "
                            "euro, iene e libra esterlina.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00371-1 (natureza dos DES)"],
    },
    # ------------------------------------------------------------------ E2-L00364
    {
        "id": "ECO-E2-L00364-1", "fonte_ref": "E2-L00364", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("O sistema de “Petrodólares”, consolidado na década de 1970, ajudou a sustentar a demanda "
                      "global pelo dólar após o fim da paridade ouro, ao estabelecer que as exportações de petróleo "
                      "da OPEP seriam liquidadas exclusivamente na moeda norte-americana."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O sistema de “Petrodólares”, consolidado na década de 1970, ajudou a sustentar a demanda "
                      "global pelo dólar após o fim da paridade ouro, ao estabelecer que as exportações de petróleo "
                      "da OPEP seriam liquidadas <u>exclusivamente</u> na moeda norte-americana."),
        "poucas": ("Com o petróleo cotado e pago em " + azb("dólar") + ", todo importador precisa de dólares, e os "
                   "exportadores reciclam seus superávits em " + vd("títulos do Tesouro americano") + ": o dólar "
                   "ganhou uma âncora de demanda no lugar do ouro."),
        "destrinchando": [
            "Depois do fim da conversibilidade (1971) e do primeiro choque do petróleo (1973), os EUA fecharam "
            "com a " + azb("Arábia Saudita") + " (1974) um arranjo de cooperação econômica e militar; os "
            "sauditas passaram a aplicar seus excedentes em títulos do Tesouro, e a OPEP adotou o dólar como "
            "moeda de cotação e de faturamento do petróleo (1975).",
            "Mecanismo de sustentação: a commodity mais negociada do mundo exige dólares → demanda "
            "transacional constante pela moeda; os superávits dos exportadores voltam aos EUA como "
            + azb("petrodólares") + " aplicados em ativos americanos → financiamento dos déficits dos EUA e "
            "liquidez para o sistema bancário internacional.",
            "Parte desses recursos foi " + azb("reciclada") + " pelos bancos do euromercado em empréstimos a "
            "países importadores de petróleo — inclusive o " + rx("Brasil") + " —, o que preparou a crise da "
            "dívida dos anos 1980.",
            "Sobre o “exclusivamente”: tratava-se de convenção de faturamento adotada pelos exportadores, não de "
            "regra jurídica; houve exceções pontuais (o Iraque passou a vender em euros em 2000; o Irã, sob "
            "sanções, aceita outras moedas) e hoje parte do comércio com a China usa renminbi. Para a década de "
            "1970, porém, a descrição é a de manual.",
            "É um dos pilares do " + azb("“privilégio exorbitante”") + " do dólar e um dos alvos dos debates "
            "atuais sobre desdolarização.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Descrição de manual do sistema dos petrodólares. O "
                       "risco está no modulador absoluto “exclusivamente”, que costuma ser sinal de ERRADO: aqui "
                       "ele descreve a convenção adotada pela OPEP nos anos 1970. Pista: o item situa o arranjo "
                       "no tempo (“consolidado na década de 1970”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A reciclagem dos petrodólares pelos bancos internacionais contribuiu para o endividamento "
            "externo de países latino-americanos nos anos 1970.”</i> → CERTO",
            "<i>“O sistema dos petrodólares foi criado na Conferência de Bretton Woods, em 1944.”</i> → ERRADO "
            "(anacronismo: consolidou-se depois de 1971–1973)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["exclusivamente"], "dificuldade": 2,
        "comentario_fonte": "Após o colapso de Bretton Woods, o acordo dos EUA com a Arábia Saudita garantiu "
                            "que o petróleo fosse cotado em dólar, reciclando os superávits árabes em títulos do "
                            "Tesouro americano.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01096-1 (reciclagem dos petrodólares)",
                    "nota_redacao: o “exclusivamente” descreve uma convenção de faturamento, não uma regra; o "
                    "gabarito CERTO da fonte foi mantido e a ressalva vai no 📖"],
    },
    # ------------------------------------------------------------------ E2-L00366
    {
        "id": "ECO-E2-L00366-1", "fonte_ref": "E2-L00366", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("No regime de Bretton Woods, os países membros estavam proibidos de realizar desvalorizações "
                      "cambiais, mesmo em casos de “desequilíbrio fundamental”, devendo manter a paridade fixa a "
                      "qualquer custo para evitar as desvalorizações competitivas dos anos 1930."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime de Bretton Woods, os países membros ") + vm("estavam proibidos de")
                    + az(" realizar desvalorizações cambiais") + vm(", mesmo em")
                    + az(" casos de “desequilíbrio fundamental”, devendo manter a paridade fixa ")
                    + vm("a qualquer custo")
                    + az(" para evitar as desvalorizações competitivas dos anos 1930.")),
        "poucas": ("Bretton Woods era de " + azb("paridades fixas, mas ajustáveis") + ": em " + vd("desequilíbrio "
                   "fundamental") + ", o país podia alterar a paridade, com consulta ao FMI."),
        "destrinchando": [
            "Pelo Convênio Constitutivo do FMI (art. IV), cada moeda tinha uma paridade em ouro ou em dólar, com "
            "margem de " + vd("±1%") + ". A alteração só podia ser proposta para corrigir um "
            + azb("desequilíbrio fundamental") + " do balanço de pagamentos, e após consulta ao Fundo; mudanças "
            "de até " + vd("10%") + " da paridade inicial não sofriam objeção.",
            "A ideia era combinar o melhor dos dois mundos: estabilidade (contra as " + azb("desvalorizações "
            "competitivas") + " dos anos 1930, que o item cita corretamente como motivação) e flexibilidade (para "
            "não repetir o ajuste deflacionário do padrão-ouro, que forçava recessão para defender a paridade).",
            "Exemplos de ajustes: a libra desvalorizou-se em " + vd("1949") + " (de US$ 4,03 para 2,80) e em "
            + vd("1967") + " (para 2,40); o marco alemão foi revalorizado em 1961 e 1969; o franco francês, "
            "desvalorizado em 1958 e 1969.",
            "O conceito de “desequilíbrio fundamental” nunca foi definido no convênio — deixou margem ao "
            "julgamento político. Na prática, os países relutavam em ajustar (desvalorizar parecia derrota; "
            "revalorizar prejudicava exportadores), e a rigidez acabou sendo um dos fatores do colapso do sistema.",
            vm("Regra-âncora: Bretton Woods = fixo + ajustável em desequilíbrio fundamental, com o FMI."),
        ],
        "dissecando": (cz("[modulador absoluto · contradição]") + " “Proibidos”, “mesmo em” e “a qualquer custo” "
                       "transformam um regime ajustável em câmbio rígido. Pista: o próprio item menciona o "
                       "“desequilíbrio fundamental”, que é justamente a cláusula de escape do sistema. A motivação "
                       "(evitar as desvalorizações competitivas) está certa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No sistema de Bretton Woods, alterações de paridade eram admitidas para corrigir desequilíbrios "
            "fundamentais do balanço de pagamentos.”</i> → CERTO",
            "<i>“Bretton Woods previa a livre flutuação das moedas em relação ao dólar, com intervenções apenas em "
            "situações de crise.”</i> → ERRADO (troca de conceito: paridades fixas com margem de 1%)",
        ])],
        "reescrita": ("No regime de Bretton Woods, os países membros " + hl("podiam") + " realizar desvalorizações cambiais"
                      + hl(", com consulta ao FMI, em") + " casos de “desequilíbrio fundamental”, devendo "
                      "manter a paridade fixa " + hl("nos demais casos") + " para evitar as desvalorizações "
                      "competitivas dos anos 1930."),
        "tipo_erro": ["GENERALIZACAO", "CONTRADICAO"], "moduladores": ["proibidos", "mesmo", "a qualquer custo"],
        "dificuldade": 1,
        "comentario_fonte": "Bretton Woods permitia ajustes cambiais em desequilíbrio fundamental, com consulta "
                            "ou aprovação do FMI: paridades fixas, mas ajustáveis.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00504-1 (ajuste de paridade em desequilíbrio fundamental)"],
    },
    # ------------------------------------------------------------------ E2-L00367
    {
        "id": "ECO-E2-L00367-1", "fonte_ref": "E2-L00367", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("O fim do padrão dólar-ouro em 1971, por decisão unilateral de Richard Nixon (o “Nixon "
                      "Shock”), marcou a transição definitiva para um sistema global de taxas de câmbio flutuantes "
                      "e moedas fiduciárias (fiat money)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O fim do padrão dólar-ouro em 1971, por decisão unilateral de Richard Nixon (o “Nixon "
                      "Shock”), <u>marcou</u> a transição definitiva para um sistema global de taxas de câmbio "
                      "flutuantes e moedas fiduciárias (fiat money)."),
        "poucas": ("Ao fechar a " + azb("janela do ouro") + " em " + vd("15/8/1971") + ", Nixon cortou o último "
                   "vínculo metálico do sistema: desde então as moedas são " + azb("fiduciárias") + ", e a "
                   "flutuação se generalizou em seguida."),
        "destrinchando": [
            "Antecedentes: déficits americanos crescentes (Vietnã, Grande Sociedade), dólares no exterior muito "
            "acima do ouro dos EUA (o " + azb("dilema de Triffin") + " realizado), conversões pela França e "
            "especulação contra o dólar. Em agosto de 1971, " + oc("Nixon") + " suspendeu a conversibilidade, "
            "impôs sobretaxa de 10% às importações e congelou preços e salários — sem consultar o FMI.",
            "A transição não foi instantânea: o " + azb("Acordo Smithsonian") + " (dezembro de " + vd("1971")
            + ") tentou restaurar paridades fixas (ouro a US$ 38 por onça, bandas de 2,25%), sem "
            "conversibilidade. Ruiu em " + vd("março de 1973") + ", quando as principais moedas passaram a "
            "flutuar. A flutuação foi legalizada pelos " + azb("Acordos da Jamaica") + " (" + vd("1976") + "), "
            "que alteraram o convênio do FMI.",
            "Por isso o item fala que 1971 <b>marcou</b> a transição: é o marco de ruptura, ainda que a "
            "flutuação generalizada só se consolide em 1973. Desde então nenhuma moeda relevante tem lastro "
            "metálico: o valor depende da confiança no emissor (" + azb("moeda fiduciária") + ").",
            "“Sistema global de câmbio flutuante” é uma simplificação: muitos países mantêm câmbio fixo ou "
            "administrado (o " + rx("Brasil") + " teve crawling peg, bandas e âncora cambial até adotar a "
            "flutuação em " + vd("1999") + "). O que acabou foi a obrigação de paridade fixa dentro de um "
            "sistema comum.",
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " Item verdadeiro na leitura usual dos manuais. O "
                       "risco é o candidato bem informado lembrar do Acordo Smithsonian e da flutuação de 1973 e "
                       "marcar ERRADO por causa do “definitiva”. Pista: o verbo é “marcou”, de marco histórico. "
                       "A banca costuma errar a data (1973 no lugar de 1971) ou o autor da decisão."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os Acordos da Jamaica, de 1976, legalizaram a flutuação cambial no âmbito do FMI.”</i> → CERTO",
            "<i>“O Acordo Smithsonian, de 1971, restabeleceu a conversibilidade do dólar em ouro a US$ 38 por "
            "onça.”</i> → ERRADO (detalhe: houve nova paridade, mas sem conversibilidade)",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["definitiva"], "dificuldade": 2,
        "comentario_fonte": "Nixon fechou a janela do ouro, encerrando a última âncora metálica do sistema e "
                            "inaugurando a era das moedas fiduciárias.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00370
    {
        "id": "ECO-E2-L00370-1", "fonte_ref": "E2-L00370", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("A “Exorbitante Prerrogativa” (Exorbitant Privilege), termo cunhado na França dos anos 1960, "
                      "refere-se à vantagem dos EUA de financiar seus déficits em conta corrente emitindo sua "
                      "própria moeda, que é aceita globalmente sem os custos de ajuste impostos a outros países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A “Exorbitante Prerrogativa” (Exorbitant Privilege), termo cunhado na <u>França dos anos "
                      "1960</u>, refere-se à vantagem dos EUA de financiar seus déficits em conta corrente "
                      "emitindo sua própria moeda, que é aceita globalmente sem os custos de ajuste impostos a "
                      "outros países."),
        "poucas": ("O " + azb("privilégio exorbitante") + " (expressão de " + oc("Valéry Giscard d'Estaing")
                   + ", ministro das Finanças de De Gaulle) é poder pagar o resto do mundo com passivos na "
                   "própria moeda, que todos aceitam e guardam como reserva."),
        "destrinchando": [
            "Origem: na década de 1960, sob o padrão ouro-dólar, a França criticava a assimetria do sistema — os "
            "EUA financiavam déficits (e investimentos e guerras no exterior) emitindo dólares que os outros "
            "bancos centrais eram obrigados a acumular. " + oc("Jacques Rueff") + " e De Gaulle defendiam a "
            "volta ao padrão-ouro; a França converteu dólares em ouro.",
            "Vantagens concretas para os EUA: (1) " + azb("senhoriagem") + " internacional (papel-moeda e "
            "títulos detidos por estrangeiros); (2) juros mais baixos, pela demanda mundial por títulos do "
            "Tesouro como ativo seguro; (3) dívida externa na própria moeda, sem " + azb("descasamento "
            "cambial") + " — uma depreciação do dólar até reduz o valor real do passivo externo; (4) menor "
            "pressão para ajustar o balanço de pagamentos.",
            "Contraste com os demais países, sobretudo emergentes: déficits persistentes exigem divisas que eles "
            "não emitem; quando o financiamento seca, o ajuste vem por recessão e desvalorização (o "
            + azb("“pecado original”") + " de não conseguir se endividar externamente na própria moeda).",
            oc("Barry Eichengreen") + " retomou o termo em <i>Exorbitant Privilege</i> (2011). A outra face é o "
            + azb("dilema de Triffin") + ": o privilégio depende de oferecer ao mundo ativos em dólar, o que "
            "exige déficits e endividamento crescentes.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição correta e atribuição correta de origem. O risco é o "
                       "detalhe histórico: a expressão é francesa, dos anos 1960 (não de economistas americanos "
                       "nem do pós-2008). Pista: “sem os custos de ajuste” é exatamente a assimetria que os "
                       "franceses denunciavam."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O privilégio exorbitante permite aos EUA endividar-se externamente em sua própria moeda, sem "
            "risco de descasamento cambial.”</i> → CERTO",
            "<i>“A expressão “privilégio exorbitante” foi cunhada por autoridades norte-americanas para justificar "
            "o papel do dólar.”</i> → ERRADO (troca de ator: foi cunhada por críticos franceses)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Como o mundo quer dólares para reserva, os EUA podem importar mais do que exportam e "
                            "pagar com moeda que eles mesmos emitem, com juros mais baixos do que teriam em outra "
                            "situação.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00371
    {
        "id": "ECO-E2-L00371-1", "fonte_ref": "E2-L00371", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("O estatuto do FMI permite que os SDRs sejam utilizados diretamente em transações comerciais "
                      "privadas e no varejo internacional, funcionando como uma alternativa líquida ao dólar para "
                      "cidadãos e empresas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O estatuto do FMI ") + vm("permite") + az(" que os SDRs sejam utilizados ")
                    + vm("diretamente em transações comerciais privadas e no varejo internacional, funcionando "
                         "como uma alternativa líquida ao dólar para cidadãos e empresas") + az(".")),
        "poucas": ("O " + azb("DES") + " não é moeda circulante: é um " + azb("ativo de reserva escritural")
                   + " que só bancos centrais, governos e alguns " + vd("detentores oficiais autorizados")
                   + " podem deter e trocar."),
        "destrinchando": [
            "O DES é um direito potencial sobre as moedas livremente utilizáveis dos membros do FMI: quem o "
            "detém pode trocá-lo, entre detentores oficiais, por dólares, euros etc. Não existe cédula, conta "
            "bancária de varejo nem pagamento comercial em DES.",
            "Quem pode deter: os " + vd("países-membros") + " (via Departamento de DES do FMI), o próprio Fundo "
            "e cerca de vinte " + azb("detentores prescritos") + " (organismos como o BIS e bancos centrais "
            "regionais). Particulares, não.",
            "Funções reais: reforçar reservas (as alocações de 2009 e de 2021 deram liquidez a países sem acesso "
            "a mercado), servir de " + azb("unidade de conta") + " do FMI e de outros organismos e de referência "
            "para algumas cestas cambiais.",
            "Por que nunca rivalizou com o dólar: volume pequeno, ausência de mercado privado de ativos em DES e "
            "de um emissor com poder fiscal. Daí as propostas recorrentes (por exemplo, do presidente do banco "
            "central chinês em 2009) de ampliar seu papel — sem resultado prático.",
            vm("Regra-âncora: DES = ativo de reserva oficial, não moeda de pagamento privado."),
        ],
        "dissecando": (cz("[troca de conceito · extrapolação]") + " Transforma um ativo de reserva oficial em "
                       "moeda de uso privado. Pista: “varejo”, “cidadãos e empresas” — nenhum particular tem conta "
                       "em DES. 🔥 Itens sobre DES alternam composição da cesta, ano de criação e quem pode "
                       "detê-los."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os DES podem ser trocados por moedas livremente utilizáveis entre os países-membros do "
            "FMI.”</i> → CERTO",
            "<i>“Os DES são emitidos pelo FMI sob a forma de cédulas, para uso nas transações oficiais entre bancos "
            "centrais.”</i> → ERRADO (são escriturais)",
        ])],
        "reescrita": ("O estatuto do FMI " + hl("não permite") + " que os SDRs sejam utilizados "
                      + hl("por particulares: eles servem como ativo de reserva escritural, detido e negociado "
                           "apenas por bancos centrais, governos e detentores oficiais autorizados") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "EXTRAPOLACAO"], "moduladores": ["diretamente"], "dificuldade": 1,
        "comentario_fonte": "O SDR não é moeda circulante: é ativo de reserva escritural usado exclusivamente por "
                            "bancos centrais, governos e algumas organizações internacionais autorizadas.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00363-1 (DES)"],
    },
    # ------------------------------------------------------------------ E2-L00486
    {
        "id": "ECO-E2-L00486-1", "fonte_ref": "E2-L00486", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_26,
        "rotulo_item": "Item",
        "assertiva": ("Uma das principais diferenças entre os planos White e Keynes na conferência de Bretton Woods "
                      "refere-se à ideia, defendida pelo primeiro, da criação de uma moeda supranacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma das principais diferenças entre os planos White e Keynes na conferência de Bretton "
                       "Woods refere-se à ideia, defendida pelo ") + vm("primeiro")
                    + az(", da criação de uma moeda supranacional.")),
        "poucas": ("A moeda supranacional — o " + vd("bancor") + " — era a peça central do plano " + azb("Keynes")
                   + " (o segundo da enumeração). White queria o " + vd("dólar conversível em ouro") + " no centro."),
        "destrinchando": [
            azb("Plano Keynes") + " (Reino Unido): " + vd("International Clearing Union") + " — uma câmara de "
            "compensação entre bancos centrais, com contas em " + vd("bancor") + ", moeda contábil "
            "supranacional criada pela própria União. Grandes linhas de crédito automático e encargos sobre "
            "<b>credores e devedores</b> (ajuste simétrico).",
            azb("Plano White") + " (EUA, " + oc("Harry Dexter White") + "): um " + vd("Fundo de "
            "Estabilização") + " formado por cotas em ouro e moedas nacionais, que emprestaria aos deficitários "
            "dentro de limites. O plano chegou a prever uma unidade de conta para o fundo (a <i>unitas</i>), "
            "mas sem poder de criar liquidez — nada comparável ao bancor.",
            "O desenho final seguiu White: o " + azb("FMI") + " nasceu do Fundo de Estabilização, e o dólar, "
            "conversível a US$ 35 por onça, virou a moeda-âncora (padrão ouro-dólar).",
            "Outras diferenças cobradas: tamanho dos recursos (Keynes queria muito mais), simetria do ajuste "
            "(Keynes penalizava superavitários; White deixava o ônus no deficitário) e o interesse nacional por "
            "trás de cada plano (devedor × credor).",
            vm("Regra-âncora: bancor = Keynes; dólar-ouro e Fundo de Estabilização = White."),
        ],
        "dissecando": (cz("[troca de ator · inversão]") + " Troca de autoria disfarçada pela ordem da enumeração: "
                       "“o primeiro” remete a White. Pista: leia com atenção “primeiro/segundo” e "
                       "“respectivamente” — a banca adora inverter a correspondência sem mexer no conteúdo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A criação de uma moeda supranacional de compensação foi proposta no plano britânico, elaborado "
            "por Keynes.”</i> → CERTO",
            "<i>“O plano White previa que os países superavitários arcassem com encargos pelos saldos acumulados, "
            "em simetria com os deficitários.”</i> → ERRADO (troca de ator: essa simetria era do plano Keynes)",
        ])],
        "reescrita": ("Uma das principais diferenças entre os planos White e Keynes na conferência de Bretton Woods "
                      "refere-se à ideia, defendida pelo " + hl("segundo") + ", da criação de uma moeda "
                      "supranacional."),
        "tipo_erro": ["TROCA_ATOR", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A afirmação inverte os proponentes: o bancor era a peça central do plano de Keynes; o "
                            "plano de White previa um fundo de estabilização (futuro FMI) com o dólar conversível "
                            "em ouro no centro.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0464-1, ECO-E2-L00361-1 (planos Keynes × White)"],
    },
    # ------------------------------------------------------------------ E2-L00504
    {
        "id": "ECO-E2-L00504-1", "fonte_ref": "E2-L00504", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_26,
        "rotulo_item": "Item",
        "assertiva": ("Pelo sistema Bretton Woods de taxas de câmbio fixas, instituído após a Segunda Guerra "
                      "Mundial, mudanças nas taxas cambiais eram permitidas somente com autorização do Fundo "
                      "Monetário Internacional (FMI), desde que houvesse desequilíbrios estruturais no balanço de "
                      "pagamentos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Pelo sistema Bretton Woods de taxas de câmbio fixas, instituído após a Segunda Guerra "
                      "Mundial, mudanças nas taxas cambiais eram permitidas <u>somente com autorização do Fundo "
                      "Monetário Internacional (FMI)</u>, desde que houvesse <u>desequilíbrios estruturais</u> no "
                      "balanço de pagamentos."),
        "poucas": ("Regime de " + azb("paridades fixas, mas ajustáveis") + ": a paridade só mudava para "
                   "corrigir " + vd("desequilíbrio fundamental") + " (estrutural) do balanço de pagamentos, com "
                   "o aval do FMI."),
        "destrinchando": [
            "Cada membro declarava ao FMI a paridade de sua moeda em ouro ou em dólar e a defendia dentro de "
            "uma margem de " + vd("±1%") + ", comprando e vendendo dólares. O dólar, por sua vez, era "
            "conversível em ouro a " + vd("US$ 35 por onça") + " para bancos centrais.",
            "Mudança de paridade: só por proposta do país e para corrigir " + azb("desequilíbrio fundamental")
            + " (expressão do art. IV do convênio, que os manuais traduzem por desequilíbrio estrutural ou "
            "persistente — e que nunca foi definida com precisão). O FMI devia concordar; para variações "
            "acumuladas de até " + vd("10%") + " da paridade inicial, não podia se opor.",
            "Lógica: impedir as " + azb("desvalorizações competitivas") + " dos anos 1930 (mudança por "
            "conveniência comercial) sem obrigar os países a recessões para defender paridades insustentáveis, "
            "como no padrão-ouro.",
            "Complementos do regime: controles de capital eram permitidos (art. VI), e as transações correntes "
            "deveriam tornar-se conversíveis (art. VIII) — o que na Europa só ocorreu em " + vd("1958") + ".",
            "Na prática, os ajustes foram raros e tardios (libra em 1949 e 1967; marco em 1961 e 1969), e a "
            "rigidez contribuiu para o colapso do sistema em 1971–1973.",
        ],
        "dissecando": (cz("[paráfrase fiel · restrição indevida aparente]") + " O “somente” costuma sinalizar "
                       "ERRADO, mas aqui descreve a regra do convênio. O risco é marcar ERRADO por lembrar que "
                       "Bretton Woods é “câmbio fixo” (sem ajuste) ou pela margem de 10% sem objeção. Pista: "
                       "“desequilíbrios estruturais” é a paráfrase de “desequilíbrio fundamental”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em Bretton Woods, os países podiam alterar livremente suas paridades para estimular "
            "exportações.”</i> → ERRADO (contradição: era isso que o sistema queria impedir)",
            "<i>“O sistema de Bretton Woods combinava paridades fixas com a possibilidade de ajuste em caso de "
            "desequilíbrio fundamental.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["somente", "desde que"], "dificuldade": 1,
        "comentario_fonte": "Bretton Woods era um regime de taxas fixas, porém ajustáveis; a paridade só podia "
                            "mudar para corrigir desequilíbrio fundamental (estrutural) do BP, com aprovação prévia "
                            "do FMI.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00366-1 (ajuste de paridade em desequilíbrio fundamental)"],
    },
    # ------------------------------------------------------------------ E2-L01096
    {
        "id": "ECO-E2-L01096-1", "fonte_ref": "E2-L01096", "destino": "65", "subtema": H2["pos"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Sobre a economia brasileira na década de 1970, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No início da década de 70 do séc. passado o Brasil e o mundo passam a assistir ao embargo "
                      "efetivado pelos países membros da OPEP (Organização dos Países Exportadores de Petróleo) na "
                      "distribuição de petróleo para os Estados Unidos e países da Europa. A ação provoca um "
                      "descomunal aumento dos preços do petróleo no mundo. Nesse período houve mudanças "
                      "importantes, tais como a subida do déficit em conta corrente das nações importadoras de "
                      "petróleo, movimento financiado pelos chamados “petrodólares”, via sistema financeiro "
                      "internacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No início da década de 70 do séc. passado o Brasil e o mundo passam a assistir ao embargo "
                      "efetivado pelos países membros da OPEP (Organização dos Países Exportadores de Petróleo) na "
                      "distribuição de petróleo para os Estados Unidos e países da Europa. A ação provoca um "
                      "descomunal aumento dos preços do petróleo no mundo. Nesse período houve mudanças "
                      "importantes, tais como a <u>subida do déficit em conta corrente</u> das nações importadoras "
                      "de petróleo, movimento <u>financiado pelos chamados “petrodólares”</u>, via sistema "
                      "financeiro internacional."),
        "poucas": ("O choque de " + vd("1973") + " transferiu renda dos importadores para os exportadores de "
                   "petróleo; os superávits árabes, depositados nos bancos internacionais (" + azb("reciclagem "
                   "dos petrodólares") + "), financiaram os déficits dos importadores — o Brasil entre eles."),
        "destrinchando": [
            "Em outubro de " + vd("1973") + ", na Guerra do Yom Kippur, os países árabes da OPEP embargaram o "
            "petróleo para os EUA e alguns aliados europeus e cortaram a produção. O preço do barril "
            + vd("quadruplicou") + " em poucos meses (de cerca de US$ 3 para perto de US$ 12).",
            "Efeito contábil: a conta de importação dos países consumidores disparou → " + azb("déficits em "
            "conta corrente") + "; do outro lado, os exportadores acumularam superávits que não conseguiam gastar "
            "de imediato.",
            azb("Reciclagem") + ": esses superávits foram depositados nos grandes bancos internacionais, sobretudo "
            "no " + azb("euromercado") + ", que os emprestaram aos deficitários a juros flutuantes. A reciclagem "
            "foi essencialmente privada (“competitiva”); o FMI teve papel secundário, com facilidades especiais "
            "do petróleo em 1974–1975.",
            "No " + rx("Brasil") + ": em vez de ajustar pela recessão, o governo Geisel lançou o " + azb("II PND")
            + " (1974–1979), que aprofundou a substituição de importações (bens de capital, insumos básicos, "
            "energia) financiada com dívida externa — o “crescimento com endividamento”. A dívida externa "
            "multiplicou-se ao longo da década.",
            "A conta veio depois: o segundo choque do petróleo (1979) e o " + azb("choque de juros") + " de "
            "Volcker tornaram impagável a dívida contratada a juros flutuantes — a crise dos anos 1980.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Narrativa longa e verdadeira, típica de item de contexto. O "
                       "risco são as imprecisões aparentes (“início da década” para 1973; “descomunal”), que não "
                       "alteram o núcleo: choque → déficits → financiamento por petrodólares. Pista: o item não "
                       "tem modulador absoluto nem nexo forçado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A reciclagem dos petrodólares foi conduzida majoritariamente pelo FMI, por meio de empréstimos "
            "condicionados.”</i> → ERRADO (troca de ator: foi feita sobretudo pelos bancos privados)",
            "<i>“O II PND respondeu ao primeiro choque do petróleo com a manutenção do crescimento, financiado por "
            "endividamento externo.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Os excedentes dos exportadores de petróleo geraram liquidez internacional que "
                            "financiou os déficits em conta corrente dos importadores; a proposta de reciclagem sob "
                            "supervisão do FMI não teve apoio, e a reciclagem foi feita pelos bancos privados "
                            "(“reciclagem competitiva”).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00364-1 (petrodólares)"],
    },
    # ------------------------------------------------------------------ E3-L00036
    {
        "id": "ECO-E3-L00036-1", "fonte_ref": "E3-L00036", "destino": "65", "subtema": H2["bw"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("Tendo como referência inicial as informações precedentes, julgue o item seguinte, com base nos "
                    "fundamentos do comércio exterior, das finanças internacionais e das instituições "
                    "multilaterais."),
        "excerto": ("<p><i>Nos últimos anos, a economia internacional tem sido marcada por intensas transformações "
                    "nos fluxos comerciais e financeiros, impulsionadas por mudanças na taxa de câmbio, nas "
                    "políticas comerciais e na integração entre mercados. Nesse cenário, o papel das tarifas, "
                    "subsídios, blocos econômicos, organismos multilaterais e dos capitais internacionais tornou-se "
                    "ainda mais relevante na formulação de políticas públicas, o que exige compreensão crítica dos "
                    "seus mecanismos e implicações para o equilíbrio macroeconômico.</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("O principal objetivo do FMI é financiar projetos de longo prazo em infraestrutura e "
                      "desenvolvimento sustentável nos países em desenvolvimento."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O principal objetivo do FMI é ") + vm("financiar projetos de longo prazo em infraestrutura "
                                                              "e desenvolvimento sustentável nos países em "
                                                              "desenvolvimento") + az(".")),
        "poucas": ("Financiar projetos de desenvolvimento é papel do " + azb("Banco Mundial") + ". O " + azb("FMI")
                   + " cuida da " + vd("estabilidade monetária e financeira internacional") + ": supervisão e "
                   "crédito a países com problemas de balanço de pagamentos."),
        "destrinchando": [
            "As duas “instituições de Bretton Woods” (1944) nasceram com mandatos complementares: o "
            + azb("FMI") + " para a cooperação monetária e a estabilidade cambial; o " + azb("BIRD") + " (Banco "
            "Internacional para Reconstrução e Desenvolvimento, núcleo do Grupo Banco Mundial) para a "
            "reconstrução europeia e, depois, o desenvolvimento.",
            "Funções do FMI: (1) " + azb("supervisão") + " das políticas econômicas (consultas do art. IV); (2) "
            + azb("assistência financeira") + " a países com dificuldades de balanço de pagamentos, em geral "
            "de curto e médio prazo e com condicionalidades (Stand-By, Extended Fund Facility); (3) assistência "
            "técnica. Os recursos vêm das cotas dos membros.",
            "Funções do Banco Mundial: empréstimos de longo prazo para projetos (infraestrutura, saúde, "
            "educação, clima) e programas de reforma; a AID (Associação Internacional de Desenvolvimento) "
            "empresta em condições concessionais aos países mais pobres.",
            "Zona cinzenta: o FMI criou, em 2022, o " + azb("Resilience and Sustainability Trust") + ", com "
            "financiamento de prazo mais longo para choques climáticos e pandêmicos — mas isso não altera seu "
            "mandato principal. ⏳ (out/2026)",
            "O " + rx("Brasil") + " recorreu ao FMI nas crises da dívida (anos 1980) e em 1998–2002; quitou "
            "antecipadamente a dívida com o Fundo em " + vd("2005") + " e hoje é credor da instituição ⏳ (out/2026).",
            vm("Regra-âncora: FMI = balanço de pagamentos e estabilidade; Banco Mundial = projetos e "
               "desenvolvimento."),
        ],
        "dissecando": (cz("[troca de ator]") + " Atribui ao FMI o mandato do Banco Mundial. Pista: “projetos de "
                       "longo prazo” e “infraestrutura” são palavras do vocabulário do banco de desenvolvimento; "
                       "o FMI trabalha com “balanço de pagamentos”, “supervisão” e “estabilidade”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O principal objetivo do Banco Mundial é financiar projetos de longo prazo voltados ao "
            "desenvolvimento dos países-membros.”</i> → CERTO",
            "<i>“O FMI concede empréstimos de longo prazo a projetos de infraestrutura, sem condicionalidades, "
            "aos países mais pobres.”</i> → ERRADO (troca de ator: descreve a AID, do Grupo Banco Mundial)",
        ])],
        "reescrita": ("O principal objetivo do FMI é " + hl("promover a estabilidade monetária e financeira "
                      "internacional, com apoio de curto e médio prazo a países com problemas de balanço de "
                      "pagamentos") + "."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O objetivo descrito é o do Banco Mundial; o FMI promove a estabilidade monetária e "
                            "financeira internacional e assiste países com desequilíbrios de balanço de "
                            "pagamentos com crédito de curto e médio prazo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: uma das respostas empilhadas na fonte menciona gabarito oficial C para o item "
                    "80, atribuindo a divergência a erro de leitura; as demais e a indicação principal da fonte "
                    "dão ERRADO, que é também a resposta correta pelo conteúdo — mantido"],
    },
]
