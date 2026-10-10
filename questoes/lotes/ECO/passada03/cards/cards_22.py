"""Cards do lote de redação 22 — ECO, passada 03 (nota 79: políticas comerciais; nota 83: conjuntura do Brasil)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "tar": "🧾 Tarifas",
    "cot": "🚫 Cotas e barreiras não tarifárias",
    "sub": "💰 Subsídios e defesa comercial",
    "omc": "🏛️ Política comercial e OMC",
    "conj": "🌋 Conjuntura brasileira",
}

CMD_RT = "A respeito da teoria do comércio internacional, julgue o item a seguir."

EXC_TJPA = (
    "<p><i>Nos últimos anos, a economia internacional tem sido marcada por intensas transformações nos fluxos "
    "comerciais e financeiros, impulsionadas por mudanças na taxa de câmbio, nas políticas comerciais e na "
    "integração entre mercados. Nesse cenário, o papel das tarifas, subsídios, blocos econômicos, organismos "
    "multilaterais e dos capitais internacionais tornou-se ainda mais relevante na formulação de políticas "
    "públicas, o que exige compreensão crítica dos seus mecanismos e implicações para o equilíbrio "
    "macroeconômico.</i></p>"
)

CMD_TJPA = ("Tendo como referência inicial as informações precedentes, julgue o item seguinte, com base nos "
            "fundamentos do comércio exterior, das finanças internacionais e das instituições multilaterais.")

EXC_FIBRA = (
    "<p><i>Uma determinada fibra vegetal é comercializada no mercado mundial numa estrutura de mercado altamente "
    "competitivo e seu preço mundial é de $9 dólares a saca. Quantidades ilimitadas encontram-se disponíveis para "
    "importação por parte do Brasil a esse preço. A demanda nacional é dada por Q<sub>D</sub> = 40 − 2P e a "
    "oferta nacional é dada por Q<sub>S</sub> = (2/3)P, sendo a quantidade expressa em milhões de sacas do "
    "produto e o preço em dólares.</i></p>"
)

CMD_FIBRA = "Com base nas informações apresentadas, julgue o item a seguir."

CMD_INTERV = "No que se refere à intervenção pública no equilíbrio dos mercados, julgue o item a seguir."

CMD_AGRO = "Sobre a agropecuária brasileira no processo de desenvolvimento, julgue o item a seguir."

CMD_TQ = "A respeito das tarifas e quotas utilizadas no comércio internacional, julgue o item a seguir."

EXC_MSUE = (
    "<p><i>Em dezembro de 2024, durante a 65.ª Reunião de Cúpula do Mercosul em Montevidéu, foram anunciadas as "
    "últimas informações a respeito das negociações do Acordo de Parceria entre o Mercosul e a União Europeia. As "
    "decisões encerram um processo de negociações que se estendeu por mais de 25 anos. Esse acordo busca integrar "
    "dois dos maiores blocos econômicos do mundo, abrangendo aproximadamente 718 milhões de pessoas e um PIB "
    "combinado de cerca de US$ 22 trilhões.</i></p>"
)

CMD_MSUE = "A respeito do tema, julgue o item a seguir."

EXC_NOV = (
    "<p><i>A política comercial envolve o uso de diversos instrumentos, como acordos comerciais, normas técnicas, "
    "subsídios e tarifas, que afetam as relações comerciais entre os países e a competitividade global. "
    "[...]</i></p>"
)

CMD_NOV = ("Considerando os efeitos desses instrumentos no comércio interno e externo, julgue o item a seguir.")

EXC_OUT = (
    "<p><i>A partir da interpretação das teorias clássicas de comércio, a abertura ao comércio internacional leva "
    "a um aumento do bem-estar social [...].</i></p>"
)

CMD_OUT = ("Considerando as diferentes estruturas de mercado e as interpretações das teorias de comércio mais "
           "modernas, julgue o item a seguir.")

CMD_TEORIAS = "No que se refere à economia internacional e às suas teorias de comércio, julgue o item a seguir."

CMD_CONJ = "Acerca da economia brasileira contemporânea, julgue o item a seguir."

CMD_PAUTA = "Acerca do comércio exterior brasileiro, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01764
    {
        "id": "ECO-E2-L01764-1", "fonte_ref": "E2-L01764", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT,
        "rotulo_item": "Item",
        "assertiva": ("Um subsídio aplicado à produção doméstica de um bem exportado, diferentemente de um subsídio "
                      "aplicado diretamente à sua exportação, não vai gerar aumento das exportações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um subsídio aplicado à produção doméstica de um bem exportado, ") + vm("diferentemente de")
                    + az(" um subsídio aplicado diretamente à sua exportação, ") + vm("não vai gerar")
                    + az(" aumento das exportações.")),
        "poucas": ("O " + azb("subsídio à produção") + " barateia o custo do produtor e desloca a oferta para a "
                   "direita: ao mesmo preço mundial, produz-se mais, consome-se o mesmo e "
                   + vd("exporta-se mais") + ". Os dois subsídios elevam as exportações; muda o mecanismo e o "
                   "custo."),
        "destrinchando": [
            "País pequeno exportador: o preço interno é o preço mundial P<sub>m</sub> e as exportações são a "
            "diferença entre o que se produz e o que se consome a esse preço (X = Q<sup>S</sup> − Q<sup>D</sup>).",
            azb("Subsídio à produção") + " (s por unidade produzida, vendida aqui ou lá fora): o produtor passa "
            "a receber P<sub>m</sub> + s; a oferta se desloca para a direita. O consumidor continua pagando "
            "P<sub>m</sub>, logo Q<sup>D</sup> não muda, e todo o aumento de Q<sup>S</sup> vira "
            + vd("exportação adicional") + ". O peso morto é só o da distorção de produção.",
            azb("Subsídio à exportação") + " (s só sobre o que vai para fora): vender no exterior passa a "
            "render P<sub>m</sub> + s, e o produtor só aceita vender no mercado interno a esse mesmo preço. O "
            "preço doméstico sobe, Q<sup>D</sup> <b>cai</b> e Q<sup>S</sup> sobe: as exportações crescem pelos "
            "dois lados. Para o mesmo s, o efeito sobre X é maior, mas o custo também: perdem os consumidores e "
            "há peso morto de produção <b>e</b> de consumo (Krugman e Obstfeld).",
            "Daí a hierarquia de eficiência: se o objetivo é expandir a produção, o subsídio à produção atinge o "
            "alvo com menos distorção que o subsídio à exportação ou que a tarifa.",
            "Na OMC, a diferença é jurídica: pelo " + azb("Acordo sobre Subsídios e Medidas Compensatórias "
            "(ASMC)") + ", o subsídio vinculado ao desempenho exportador é " + vd("proibido") + " (art. 3); o "
            "subsídio à produção, se específico, é " + vd("acionável") + ": só pode ser contestado se causar "
            "efeitos adversos a outro membro. Na agricultura, os subsídios à exportação foram eliminados na "
            "Conferência de " + vd("Nairóbi (2015)") + ".",
            vm("Regra-âncora: qualquer subsídio que eleve a oferta de um bem exportável aumenta as exportações; o "
               "subsídio à exportação ainda reduz o consumo interno."),
        ],
        "grafico_verso": "ECO-E2-L01764-1-V1",
        "dissecando": (cz("[troca de conceito · inversão]") + " O item parte de uma diferença real (o "
                       "subsídio à exportação atua só no mercado externo e é proibido na OMC) e a transforma "
                       "numa diferença de resultado que não existe. Pista: “não vai gerar” é categórico; basta "
                       "lembrar que mais produção ao mesmo preço mundial só pode ir para fora."),
        "modulos": [
            ("🟣 Posição do Brasil", [
                rx("O Brasil") + " venceu os EUA no contencioso do " + rx("algodão") + " (DS267, 2004–2005): "
                "o Órgão de Apelação condenou subsídios à exportação (garantias de crédito) e apoios internos "
                "que deprimiam o preço mundial — exemplo de subsídio à produção atacado pelos efeitos "
                "adversos.",
            ]),
            ("😈 Para dificultar", [
                "<i>“Para um mesmo valor unitário, o subsídio à exportação eleva o preço doméstico e reduz o "
                "consumo interno, o que não ocorre com o subsídio à produção.”</i> → CERTO",
                "<i>“O subsídio à produção gera perda de peso morto maior que o subsídio à exportação de mesmo "
                "valor unitário.”</i> → ERRADO (inversão: o subsídio à exportação distorce também o consumo)",
            ]),
        ],
        "reescrita": ("Um subsídio aplicado à produção doméstica de um bem exportado, " + hl("assim como")
                      + " um subsídio aplicado diretamente à sua exportação, " + hl("também gera")
                      + " aumento das exportações."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": ["não vai"], "dificuldade": 2,
        "comentario_fonte": ("Subsídio à produção reduz custo, torna o produto mais competitivo no mercado interno "
                             "e externo e também aumenta exportações; o subsídio à exportação afeta apenas o "
                             "mercado externo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 527", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (subsídio à exportação; substituída pelo gráfico didático)"},
                          {"ref": "IMAGEM 528", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (gráfico didático ECO-E2-L01764-1-V1)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00034
    {
        "id": "ECO-E3-L00034-1", "fonte_ref": "E3-L00034", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA,
        "excerto": EXC_TJPA,
        "rotulo_item": "Item",
        "assertiva": ("Em uma união aduaneira, os países-membros adotam uma tarifa comum para terceiros e podem "
                      "aplicar sanções comerciais internas caso uma das nações descumpra os compromissos do bloco."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma união aduaneira, os países-membros adotam uma <u>tarifa comum para terceiros</u> e "
                      "<u>podem</u> aplicar sanções comerciais internas caso uma das nações descumpra os "
                      "compromissos do bloco."),
        "poucas": ("União aduaneira = " + azb("livre comércio interno + tarifa externa comum (TEC)") + ". Como "
                   "há compromissos jurídicos, o bloco pode prever mecanismos de solução de controvérsias com "
                   "retaliação contra o membro que descumpre."),
        "destrinchando": [
            "Escala de integração de " + oc("Bela Balassa") + " (1961): " + azb("área de livre comércio")
            + " (tarifas internas zeradas, cada um com sua tarifa externa) → " + azb("união aduaneira")
            + " (+ TEC) → " + azb("mercado comum") + " (+ livre circulação de fatores) → "
            + azb("união econômica") + " (+ coordenação de políticas) → integração total.",
            "A TEC é o que distingue a união aduaneira da área de livre comércio: sem ela, é preciso "
            + azb("regras de origem") + " para evitar a triangulação (importar pelo membro de tarifa mais baixa "
            "e revender aos demais).",
            "Para o comércio intrabloco funcionar, o bloco precisa de disciplina: no " + rx("Mercosul")
            + ", o " + azb("Protocolo de Brasília") + " (" + vd("1991") + ") e depois o " + azb("Protocolo de "
            "Olivos") + " (" + vd("2002") + ", que criou o Tribunal Permanente de Revisão) autorizam o membro "
            "vencedor a aplicar " + azb("medidas compensatórias temporárias") + " — suspensão de concessões — "
            "se o laudo não for cumprido. É a “sanção comercial interna” do item.",
            "Mesma lógica no plano multilateral: no Órgão de Solução de Controvérsias da OMC, a retaliação "
            "autorizada também é suspensão de concessões.",
            "O " + rx("Mercosul") + " é chamado de " + azb("união aduaneira imperfeita") + ": tem TEC desde "
            + vd("1995") + " (Protocolo de Ouro Preto, 1994), mas com listas nacionais de exceção e regimes "
            "especiais.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " A primeira metade é a definição de manual; "
                       "a segunda se salva pelo “podem” — não é que toda união aduaneira tenha sanções, mas que "
                       "os compromissos do bloco admitem mecanismos de cumprimento. A armadilha seria trocar "
                       "“união aduaneira” por “área de livre comércio”."),
        "modulos": [
            ("🧭 Panorama", [
                "ALC (ex.: USMCA) → sem TEC; união aduaneira (Mercosul, SACU, UE na origem) → TEC; mercado comum "
                "(UE desde o Ato Único de 1986/1992) → livre circulação de bens, serviços, capitais e pessoas.",
            ]),
            ("😈 Para dificultar", [
                "<i>“Em uma área de livre comércio, os países-membros adotam uma tarifa comum para terceiros "
                "países.”</i> → ERRADO (troca de conceito: TEC é marca da união aduaneira)",
                "<i>“A união aduaneira pressupõe a livre circulação de trabalho e capital entre os membros.”</i> → "
                "ERRADO (troca de conceito: isso é mercado comum)",
            ]),
        ],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": ("União aduaneira: livre comércio interno + TEC; o bloco pode prever mecanismos de "
                             "enforcement (salvaguardas, suspensão de benefícios), como nos Protocolos de Brasília "
                             "e de Olivos no Mercosul."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00035
    {
        "id": "ECO-E3-L00035-1", "fonte_ref": "E3-L00035", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": CMD_TJPA,
        "excerto": EXC_TJPA,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de tarifas de importação, por si só, assegura a melhora do saldo da balança "
                      "comercial, independentemente do comportamento da taxa de câmbio e da demanda agregada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A imposição de tarifas de importação, por si só, ") + vm("assegura")
                    + az(" a melhora do saldo da balança comercial, ") + vm("independentemente")
                    + az(" do comportamento da taxa de câmbio e da demanda agregada.")),
        "poucas": ("A tarifa corta importações no primeiro momento, mas o saldo externo depende do câmbio e da "
                   "relação " + azb("poupança × investimento") + ": apreciação cambial, retaliação e aumento da "
                   "absorção podem anular o efeito."),
        "destrinchando": [
            "Pela identidade macroeconômica, " + vd("NX ≈ S − I") + " (o saldo externo é o excesso de poupança "
            "sobre investimento). Se a tarifa não muda a poupança nem o investimento agregados, não pode mudar "
            "o saldo de forma duradoura: alguma outra variável se ajusta.",
            "A variável que costuma se ajustar é o " + azb("câmbio") + ": com menos importações, cai a demanda "
            "por divisas e a moeda nacional se aprecia; as exportações perdem competitividade e as importações "
            "não tarifadas ficam mais baratas. É a " + azb("simetria de Lerner") + " (" + oc("Abba Lerner")
            + ", 1936): no equilíbrio geral, um imposto sobre importações equivale a um imposto sobre "
            "exportações.",
            "Outros canais: " + azb("retaliação") + " dos parceiros (cai a exportação); encarecimento de "
            + azb("insumos importados") + " (perde-se competitividade da produção exportadora); e, se a tarifa "
            "estimula a renda interna, a demanda agregada maior puxa importações de volta.",
            "Por isso a teoria trata a balança comercial como fenômeno macroeconômico (abordagem da absorção, "
            "de " + oc("Sidney Alexander") + ") e a tarifa como instrumento de alocação, não de ajuste externo.",
            vm("Regra-âncora: tarifa muda a composição do comércio; o saldo depende de câmbio, renda e S − I."),
        ],
        "dissecando": (cz("[modulador absoluto · nexo indevido]") + " Dois absolutos empilhados — “por si só, "
                       "assegura” e “independentemente” — sobre um efeito que a teoria considera ambíguo. 🔥 "
                       "CEBRASPE cobra com frequência o nexo indevido “protecionismo → melhora da balança”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A imposição de tarifas de importação pode provocar apreciação cambial que reduz as exportações, "
            "neutralizando parte do efeito sobre o saldo comercial.”</i> → CERTO",
            "<i>“Pela simetria de Lerner, uma tarifa de importação equivale a um subsídio às exportações.”</i> → "
            "ERRADO (troca de conceito: equivale a um imposto sobre exportações)",
        ])],
        "reescrita": ("A imposição de tarifas de importação, por si só, " + hl("não assegura")
                      + " a melhora do saldo da balança comercial, " + hl("que depende")
                      + " do comportamento da taxa de câmbio e da demanda agregada."),
        "tipo_erro": ["GENERALIZACAO", "NEXO_INDEVIDO"], "moduladores": ["por si só", "assegura",
                                                                        "independentemente"],
        "dificuldade": 1,
        "comentario_fonte": ("Efeito ambíguo: apreciação cambial, retaliação, simetria de Lerner, identidade "
                             "CA = S − I, condição de Marshall-Lerner; a tarifa não assegura melhora do saldo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00119
    {
        "id": "ECO-E3-L00119-1", "fonte_ref": "E3-L00119", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_FIBRA,
        "excerto": EXC_FIBRA,
        "rotulo_item": "Item",
        "assertiva": ("Na ausência de restrições ao comércio, o Brasil importaria 16 milhões de sacas desta fibra "
                      "vegetal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na ausência de restrições ao comércio, o Brasil importaria <u>16 milhões</u> de sacas desta "
                      "fibra vegetal."),
        "poucas": ("Com livre comércio, o preço interno é o mundial (" + vd("P = 9") + "): Q<sub>D</sub> = "
                   + vd("22") + ", Q<sub>S</sub> = " + vd("6") + "; importações = 22 − 6 = " + vd("16")
                   + " milhões de sacas."),
        "destrinchando": [
            "“Quantidades ilimitadas a $9” significa oferta externa " + azb("perfeitamente elástica") + ": o "
            "Brasil é " + azb("país pequeno") + " (tomador de preço) e, sem barreiras, ninguém paga mais nem "
            "recebe menos que 9 no mercado interno.",
            "A esse preço: Q<sub>D</sub> = 40 − 2·9 = " + vd("22") + "; Q<sub>S</sub> = (2/3)·9 = " + vd("6")
            + ". O hiato entre consumo e produção é coberto por importações: " + vd("M = 22 − 6 = 16") + ".",
            "Para saber se o país importa ou exporta, compare com a " + azb("autarquia") + ": 40 − 2P = (2/3)P → "
            + vd("P = 15, Q = 10") + ". Como 9 &lt; 15, o país é importador; se o preço mundial fosse maior que "
            "15, seria exportador.",
            "Bem-estar do livre comércio frente à autarquia: o consumidor ganha (paga 9 em vez de 15 e consome 22 "
            "em vez de 10), o produtor perde (vende 6 a 9 em vez de 10 a 15) e o ganho do consumidor supera a "
            "perda do produtor — o país como um todo ganha.",
            vm("Regra-âncora: país pequeno com livre comércio → P interno = P mundial; M = Q<sub>D</sub>(P<sub>m</sub>) "
               "− Q<sub>S</sub>(P<sub>m</sub>)."),
        ],
        "dissecando": (cz("[detalhe]") + " Item de cálculo direto. Os erros que a banca espera: usar o preço de "
                       "autarquia (15) em vez do mundial, ou confundir importação com consumo total (22). "
                       "Fixe o roteiro: preço vigente → Q<sub>D</sub> e Q<sub>S</sub> → diferença."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na ausência de restrições ao comércio, o consumo interno seria de 16 milhões de sacas.”</i> → "
            "ERRADO (dado trocado: consumo é 22; 16 é a importação)",
            "<i>“Se o preço mundial fosse $18, o Brasil exportaria a fibra.”</i> → CERTO (18 &gt; 15: "
            "Q<sub>S</sub> = 12 &gt; Q<sub>D</sub> = 4)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("P = 9: QD = 22, QS = 6, importações = 16; autarquia em P = 15 e Q = 10; consumidores "
                             "ganham, produtores perdem, ganho líquido do país."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 97", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 98", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 99", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00120
    {
        "id": "ECO-E3-L00120-1", "fonte_ref": "E3-L00120", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_FIBRA,
        "excerto": EXC_FIBRA,
        "rotulo_item": "Item",
        "assertiva": ("Se o Brasil impusesse um imposto de importação de $9 dólares por saca, não haveria "
                      "importações. Nesse caso, a quantidade de equilíbrio seria igual a 10 milhões de sacas, a um "
                      "preço de $15 dólares por unidade."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o Brasil impusesse um imposto de importação de $9 dólares por saca, <u>não haveria "
                      "importações</u>. Nesse caso, a quantidade de equilíbrio seria igual a <u>10 milhões</u> de "
                      "sacas, a um preço de <u>$15</u> dólares por unidade."),
        "poucas": ("Com a tarifa, o importado custa " + vd("9 + 9 = 18") + ", acima do preço de autarquia ("
                   + vd("15") + "): é uma " + azb("tarifa proibitiva") + ". Ninguém importa e o mercado volta ao "
                   "equilíbrio interno, " + vd("Q = 10 e P = 15") + "."),
        "destrinchando": [
            "Autarquia: 40 − 2P = (2/3)P → 120 − 6P = 2P → " + vd("P = 15") + "; Q = 40 − 30 = " + vd("10")
            + ".",
            "Com tarifa específica de 9, o produto importado chega a " + vd("18") + ". O mercado interno só "
            "importaria se o preço doméstico ficasse acima de 18, mas o equilíbrio sem importações já se dá a 15: "
            "a tarifa “passa do ponto” e as importações zeram.",
            azb("Tarifa proibitiva") + " é qualquer t ≥ P<sub>autarquia</sub> − P<sub>m</sub> = 15 − 9 = "
            + vd("6") + ". A partir daí, aumentar a tarifa não muda nada: o preço interno fica no de autarquia "
            "(15), não em P<sub>m</sub> + t (18). Erro comum é responder 18.",
            "Consequências: a arrecadação é " + vd("zero") + " (não há importação a tributar) e o peso morto é "
            "máximo — todo o ganho de comércio desaparece. Com tarifas menores que 6 (não proibitivas), o preço "
            "interno seria 9 + t e ainda haveria importação.",
            vm("Regra-âncora: tarifa proibitiva → preço interno = preço de autarquia, importação e receita zero."),
        ],
        "grafico_verso": "ECO-E3-L00120-1-V1",
        "dissecando": (cz("[detalhe · contraintuitivo]") + " A armadilha é somar e responder que o preço vai a "
                       "18. Quem lembra que o mercado nunca paga mais que o equilíbrio interno quando não há "
                       "importação acerta. Cobrança típica: perguntar a partir de que tarifa as importações "
                       "zeram (6)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com o imposto de importação de $9, o preço interno passaria a $18 por saca.”</i> → ERRADO (a "
            "tarifa é proibitiva: o preço fica no de autarquia, 15)",
            "<i>“Qualquer imposto de importação igual ou superior a $6 por saca eliminaria as importações.”</i> "
            "→ CERTO",
            "<i>“Com o imposto de $9, a arrecadação seria de $9 × 10 milhões.”</i> → ERRADO (sem importação, a "
            "arrecadação é zero)",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Tarifa de 9 leva o importado a 18 > preço de autarquia 15: tarifa proibitiva, sem "
                             "importações, equilíbrio em P = 15 e Q = 10."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 100", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 101", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 102", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 103", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00121
    {
        "id": "ECO-E3-L00121-1", "fonte_ref": "E3-L00121", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_FIBRA,
        "excerto": EXC_FIBRA,
        "rotulo_item": "Item",
        "assertiva": ("Se ao invés do imposto, for estabelecida uma quota de importação igual a 8 milhões de "
                      "sacas, o preço de equilíbrio nacional passa a ser de $12 dólares por saca."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se ao invés do imposto, for estabelecida uma quota de importação igual a 8 milhões de "
                      "sacas, o preço de equilíbrio nacional passa a ser de <u>$12</u> dólares por saca."),
        "poucas": ("Com a cota, o preço interno sobe até que o hiato entre demanda e oferta nacionais caiba nas "
                   "8 milhões permitidas: (40 − 2P) − (2/3)P = 8 → " + vd("P = 12") + "."),
        "destrinchando": [
            "Cota fixa a <b>quantidade</b> importada; o <b>preço</b> é que se ajusta. Condição de equilíbrio: "
            + azb("importação = Q<sub>D</sub> − Q<sub>S</sub> = cota") + ".",
            "Conta: 40 − 2P − (2/3)P = 8 → 32 = (8/3)P → " + vd("P = 12") + ". Conferência: Q<sub>D</sub> = "
            + vd("16") + ", Q<sub>S</sub> = " + vd("8") + ", diferença " + vd("8") + ".",
            "Como 9 &lt; 12 &lt; 15, a cota “morde”: é menor que as importações de livre comércio (16) e maior "
            "que zero. Cota ≥ 16 seria inócua (P = 9); cota zero levaria à autarquia (P = 15).",
            azb("Tarifa equivalente") + ": uma tarifa de " + vd("t = 3") + " levaria o preço a 9 + 3 = 12 e as "
            "importações aos mesmos 8 milhões. Preço, quantidades, consumo e produção são idênticos; muda o "
            "destino do retângulo 3 × 8 = " + vd("24") + ": receita do governo na tarifa, " + azb("renda da "
            "cota") + " de quem detém as licenças na cota (" + oc("Bhagwati") + ", equivalência tarifa-cota em "
            "concorrência perfeita).",
            "Diferença dinâmica: se a demanda crescer, com tarifa o preço fica em 12 e a importação aumenta; com "
            "cota, a importação fica travada em 8 e o preço sobe.",
            vm("Regra-âncora: com cota, resolva Q<sub>D</sub>(P) − Q<sub>S</sub>(P) = cota; o preço é a incógnita."),
        ],
        "dissecando": (cz("[detalhe]") + " Item de cálculo em que a dificuldade é o raciocínio inverso: na cota "
                       "não se soma nada ao preço mundial, procura-se o preço que encaixa a quantidade. O erro "
                       "típico é imaginar que a cota não muda o preço (fica em 9) ou somar a cota à oferta "
                       "nacional sem igualar à demanda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A quota de 8 milhões de sacas tem efeito sobre preços equivalente ao de uma tarifa de $3 por "
            "saca.”</i> → CERTO",
            "<i>“Com a quota de 8 milhões de sacas, o governo arrecada $24 milhões.”</i> → ERRADO (na cota, os "
            "24 viram renda de quem tem as licenças, salvo se leiloadas)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Importações = QD − QS = 8 → P = 12; QD = 16, QS = 8; renda de quota de 3 por saca "
                             "para os detentores das licenças."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 104", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 105", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 106", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 107", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 108", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 109", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 110", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 111", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00122
    {
        "id": "ECO-E3-L00122-1", "fonte_ref": "E3-L00122", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_FIBRA,
        "excerto": EXC_FIBRA,
        "rotulo_item": "Item",
        "assertiva": ("No caso do estabelecimento da quota de importação de 8 milhões de sacas, os produtores "
                      "nacionais teriam uma melhora de bem-estar equivalente a $21 milhões de dólares em relação à "
                      "situação de livre comércio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No caso do estabelecimento da quota de importação de 8 milhões de sacas, os produtores "
                      "nacionais teriam uma melhora de bem-estar equivalente a <u>$21 milhões</u> de dólares em "
                      "relação à situação de livre comércio."),
        "poucas": ("O " + azb("excedente do produtor") + " passa de (6 × 9)/2 = " + vd("27") + " para (8 × 12)/2 = "
                   + vd("48") + ": ganho de " + vd("21") + " milhões — o trapézio entre os preços 9 e 12, à "
                   "esquerda da oferta."),
        "destrinchando": [
            "Com a cota de 8, o preço interno vai a " + vd("12") + " e a produção nacional, de 6 para "
            + vd("8") + " milhões de sacas.",
            azb("Excedente do produtor") + " = área acima da oferta e abaixo do preço. Como a oferta parte da "
            "origem (Q<sub>S</sub> = 0 com P = 0), é um triângulo: livre comércio " + vd("27") + "; com cota "
            + vd("48") + ".",
            "Atalho pelo trapézio: ΔEP = (Q<sub>S</sub> antes + Q<sub>S</sub> depois)/2 × ΔP = (6 + 8)/2 × 3 = "
            + vd("21") + ".",
            "Quadro completo da cota (em US$ milhões): o consumidor perde (22 + 16)/2 × 3 = " + vd("57")
            + "; desses, " + vd("21") + " vão ao produtor, " + vd("24") + " viram " + azb("renda da cota")
            + " (3 × 8, de quem detém as licenças) e " + vd("12") + " são " + azb("peso morto") + " (dois "
            "triângulos: 3 × 2/2 de produção e 3 × 6/2 de consumo).",
            "Se as licenças forem dadas a importadores nacionais, a renda da cota fica no país; se a cota for "
            "administrada pelo exportador (restrição voluntária de exportação), ela vai para o estrangeiro e a "
            "perda nacional sobe de 12 para 36.",
        ],
        "grafico_verso": "ECO-E3-L00122-1-V1",
        "dissecando": (cz("[detalhe]") + " Cálculo de área. Erros previsíveis: usar só o retângulo 3 × 6 = 18 "
                       "(esquecendo o triângulo da produção adicional), usar o retângulo 3 × 8 = 24 (que é a "
                       "renda da cota) ou calcular só o excedente final (48)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com a quota, a perda de excedente dos consumidores seria de $57 milhões.”</i> → CERTO",
            "<i>“Com a quota, a perda de peso morto da economia seria de $24 milhões.”</i> → ERRADO (24 é a renda "
            "da cota; o peso morto é 12)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("EP livre comércio = 9 × 6/2 = 27; com quota = 12 × 8/2 = 48; ganho de 21. Perda dos "
                             "consumidores 57, renda de quota 24, peso morto 12."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 112", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (gráfico didático ECO-E3-L00122-1-V1)"},
                          {"ref": "IMAGEM 113", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (mesmo gráfico com a cota)"},
                          {"ref": "IMAGEM 114", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 115", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 116", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 117", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 118", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 119", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00145
    {
        "id": "ECO-E3-L00145-1", "fonte_ref": "E3-L00145", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": "Julgue o item subsequente, em relação aos principais acordos e organismos internacionais.",
        "rotulo_item": "Item",
        "assertiva": ("Existe a prática de <i>dumping</i> quando a oferta de um produto no mercado internacional "
                      "ocorre a um preço inferior ao praticado no país exportador."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Existe a prática de <i>dumping</i> quando a oferta de um produto no mercado internacional "
                       "ocorre ") + vm("a um preço inferior ao praticado no país exportador") + az(".")),
        "poucas": ("A definição técnica compara o " + azb("preço de exportação") + " com o " + azb("valor normal")
                   + " — que nem sempre é o preço interno do exportador —, e a medida antidumping exige ainda "
                   + azb("dano") + " à indústria do importador e " + azb("nexo causal") + ". A banca considerou "
                   "a definição do item insuficiente."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o gabarito oficial é ERRADO, mas a frase reproduz o núcleo do " + vd("art. VI do GATT")
                          + ", que define dumping como introdução de um produto no mercado de outro país a preço "
                          "inferior ao valor normal, tomado em regra como o preço comparável no mercado interno "
                          "do exportador. Dano e nexo causal são condições para <b>aplicar</b> o direito "
                          "antidumping, não para que o dumping exista. A resposta CERTO seria defensável; o "
                          "ERRADO se sustenta pela leitura de que o item simplifica o valor normal e omite os "
                          "requisitos de dano.")],
        "destrinchando": [
            "Base normativa: " + vd("art. VI do GATT 1994") + ", o " + azb("Acordo Antidumping da OMC") + " e, "
            "no " + rx("Brasil") + ", o " + vd("Decreto n.º 8.058/2013") + ". Dumping é uma forma de "
            + azb("discriminação internacional de preços") + ": exportar abaixo do " + azb("valor normal") + ".",
            "Valor normal, em ordem: (1) preço do produto similar no mercado interno do exportador, em "
            "<b>operações comerciais normais</b> (vendas abaixo do custo podem ser desconsideradas); (2) na falta "
            "dele, preço de exportação para um " + azb("terceiro país") + "; ou (3) " + azb("valor construído")
            + " (custo de produção + despesas + margem razoável de lucro). Para economias que não são de mercado, "
            "usa-se um terceiro país substituto.",
            "Diferença de preço é condição necessária, não suficiente, para a defesa comercial: o direito "
            "antidumping só se aplica com (i) " + vd("margem de dumping") + ", (ii) " + vd("dano material")
            + " ou ameaça de dano à indústria doméstica e (iii) " + vd("nexo causal") + " entre as importações "
            "a preço de dumping e o dano. O direito não pode exceder a margem.",
            "Não confundir com " + azb("medida compensatória") + " (contra " + azb("subsídio") + " concedido "
            "por governo estrangeiro, ASMC) nem com " + azb("salvaguarda") + " (contra surto de importações "
            "<b>leais</b>, sem prática desleal). Antidumping responde a conduta da <b>empresa</b>; a "
            "compensatória, a conduta do <b>governo</b>.",
            "Tipologia clássica de " + oc("Jacob Viner") + " (1923): dumping esporádico (desova de estoques), "
            "predatório/intermitente (eliminar concorrentes) e persistente (discriminação de preços entre mercados "
            "com elasticidades diferentes).",
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A banca tratou a frase como definição "
                       "incompleta: “preço praticado no país exportador” no lugar de “valor normal” e silêncio "
                       "sobre dano e nexo. 🔥 CEBRASPE costuma cobrar o tripé margem + dano + nexo; diante de "
                       "uma definição de dumping, confira se ela fala em valor normal e se o item fala em "
                       "<b>existência</b> da prática ou em <b>aplicação</b> de medida."),
        "modulos": [
            ("⚖️ Base normativa", [
                vd("Decreto 8.058/2013, art. 7.º") + ": há dumping na introdução de produto no mercado brasileiro "
                "a preço de exportação inferior ao valor normal. A aplicação do direito exige determinação de "
                "dumping, dano e nexo causal em investigação conduzida pela área de defesa comercial da Secex e decidida pelo Gecex/Camex.",
            ]),
            ("😈 Para dificultar", [
                "<i>“A aplicação de direito antidumping exige a demonstração de dano à indústria doméstica do país "
                "importador e de nexo causal entre o dumping e esse dano.”</i> → CERTO",
                "<i>“Direitos antidumping são aplicados contra subsídios concedidos por governos "
                "estrangeiros.”</i> → ERRADO (troca de conceito: isso é medida compensatória)",
            ]),
        ],
        "reescrita": ("Existe a prática de <i>dumping</i> quando a oferta de um produto no mercado internacional "
                      "ocorre " + hl("a um preço de exportação inferior ao seu valor normal — em regra, o preço "
                      "comparável, em operações comerciais normais, no mercado interno do país exportador") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("Definição incompleta: dumping exige comparação com o valor normal (preço interno, "
                             "preço a terceiro país ou valor construído), e a medida antidumping requer dano e nexo "
                             "causal (Acordo Antidumping; Decreto 8.058/2013); tipologia de Viner."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 150", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["contestavel: a frase reproduz o núcleo do art. VI do GATT; dano e nexo são requisitos da "
                    "medida, não da existência do dumping — CERTO seria defensável"],
    },
    # ------------------------------------------------------------------ E3-L00201
    {
        "id": "ECO-E3-L00201-1", "fonte_ref": "E3-L00201", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_INTERV,
        "rotulo_item": "Item",
        "assertiva": ("A eliminação de tarifas de importação conduz à redução do excedente apropriado pelos "
                      "produtores locais, acompanhada por elevação do nível de bem-estar medido pelo excedente "
                      "total."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A eliminação de tarifas de importação conduz à <u>redução</u> do excedente apropriado pelos "
                      "produtores locais, acompanhada por <u>elevação</u> do nível de bem-estar medido pelo "
                      "excedente total."),
        "poucas": ("Sem a tarifa, o preço interno cai ao preço mundial: o produtor perde excedente, o consumidor "
                   "ganha mais do que o produtor e o governo perdem juntos, e o " + azb("peso morto") + " da "
                   "tarifa desaparece — o excedente total sobe."),
        "destrinchando": [
            "Modelo de " + azb("país pequeno") + " importador (equilíbrio parcial): com tarifa t, o preço "
            "interno é P<sub>m</sub> + t; eliminada a tarifa, volta a P<sub>m</sub>.",
            "Contabilidade da eliminação: " + azb("produtor") + " perde a faixa entre os dois preços até a sua "
            "oferta (−C); " + azb("governo") + " perde a receita (−receita); " + azb("consumidor") + " ganha "
            "toda a faixa entre os preços até a demanda: C + receita + os dois triângulos.",
            "Saldo: os dois triângulos — " + azb("distorção de produção") + " (produção doméstica cara que é "
            "substituída por importação barata) e " + azb("distorção de consumo") + " (consumo que a tarifa "
            "reprimia) — são o ganho líquido. Por isso " + vm("excedente total sobe") + ".",
            "Ressalvas que a banca pode cobrar em outros itens: em " + azb("país grande") + ", a tarifa melhora "
            "os termos de troca, e eliminar uma tarifa pequena (abaixo da " + azb("tarifa ótima") + ") pode "
            "reduzir o bem-estar nacional; e o modelo ignora custos de ajustamento (desemprego setorial "
            "temporário).",
        ],
        "grafico_verso": "ECO-E3-L00201-1-V1",
        "dissecando": (cz("[literalidade]") + " Reproduz o resultado-padrão da abertura em país pequeno: perde o "
                       "produtor, ganha o país. A armadilha seria inverter os sinais (excedente do produtor "
                       "sobe) ou dizer que o bem-estar total cai porque o governo perde receita — a receita é "
                       "transferência, recuperada pelo consumidor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A eliminação de tarifas de importação reduz o bem-estar total, porque o governo deixa de "
            "arrecadar.”</i> → ERRADO (a receita volta ao consumidor; o ganho líquido são os triângulos de peso "
            "morto)",
            "<i>“Em um país grande, a eliminação de uma tarifa pode reduzir o bem-estar nacional, por piorar os "
            "termos de troca.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Abertura reduz o preço doméstico ao internacional: produtor perde, consumidor ganha "
                             "mais (recupera os triângulos de peso morto), excedente total aumenta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 263", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (gráfico didático ECO-E3-L00201-1-V1)"},
                          {"ref": "IMAGEM 264", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (quadro de excedentes no 📖)"},
                          {"ref": "IMAGEM 265", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "absorvida (quadro de excedentes no 📖)"},
                          {"ref": "IMAGEM 266", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00324
    {
        "id": "ECO-E3-L00324-1", "fonte_ref": "E3-L00324", "destino": "79", "subtema": H2["omc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_AGRO,
        "rotulo_item": "Item",
        "assertiva": ("A Rodada Uruguai do GATT, na década de 1990, teve como uma de suas consequências no Brasil a "
                      "redução dos subsídios às exportações e o compromisso de manter o teto em suas tarifas "
                      "agrícolas e industriais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Rodada Uruguai do GATT, na década de 1990, teve como uma de suas consequências no Brasil a "
                      "redução dos subsídios às exportações e o compromisso de manter o <u>teto</u> em suas "
                      "tarifas agrícolas e industriais."),
        "poucas": ("A Rodada Uruguai (" + vd("1986–1994") + ") disciplinou subsídios à exportação e exigiu a "
                   + azb("consolidação") + " das tarifas: o " + rx("Brasil") + " assumiu tetos (tarifas "
                   "consolidadas) para bens agrícolas e industriais."),
        "destrinchando": [
            "A rodada foi lançada em Punta del Este (" + vd("1986") + "), concluída em Marraquexe (" + vd("1994")
            + ") e criou a " + azb("OMC") + " (" + vd("1995") + "). Trouxe para as regras multilaterais a "
            "agricultura, os serviços (GATS) e a propriedade intelectual (TRIPS).",
            azb("Consolidação tarifária") + ": o país se compromete a não ultrapassar uma alíquota máxima "
            "(tarifa " + azb("consolidada") + "); a tarifa " + azb("aplicada") + " pode ficar abaixo. A "
            "diferença entre as duas é o “colchão” (<i>water</i>), que dá espaço de política. O "
            + rx("Brasil") + " consolidou praticamente todo o seu universo tarifário, com tetos em torno de "
            + vd("35%") + " para bens industriais e " + vd("55%") + " para agrícolas — bem acima das tarifas "
            "aplicadas após a abertura de 1988–1994.",
            "O " + azb("Acordo sobre Agricultura") + " tem três pilares: acesso a mercados (tarificação de "
            "barreiras não tarifárias e consolidação), apoio interno (caixas amarela, azul e verde) e "
            + azb("subsídios à exportação") + " (redução de valor e volume, com prazos maiores para países em "
            "desenvolvimento). Para bens industriais, o " + azb("ASMC") + " passou a proibir subsídios "
            "vinculados à exportação.",
            "Para o " + rx("Brasil") + ", competidor agrícola sem grandes subsídios, a rodada foi vantajosa: "
            "criou disciplinas que depois sustentaram os contenciosos do algodão (contra os EUA) e do açúcar "
            "(contra a UE).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Combina dois compromissos reais da rodada: disciplina "
                       "de subsídios e consolidação. A palavra-chave é “teto”: consolidar não é reduzir de "
                       "imediato a tarifa aplicada, e sim não ultrapassar um máximo. A troca típica seria dizer "
                       "que o Brasil teve de zerar tarifas ou reduzir as aplicadas ao nível consolidado."),
        "modulos": [
            ("🟣 Posição do Brasil", [
                rx("O Brasil") + " atuou na rodada pelo " + rx("Grupo de Cairns") + " (exportadores agrícolas "
                "sem subsídios) e depois liderou, na Rodada Doha, o " + rx("G-20 comercial") + " (Cancún, "
                + vd("2003") + "), em defesa da eliminação dos subsídios agrícolas dos países ricos.",
            ]),
            ("😈 Para dificultar", [
                "<i>“A Rodada Uruguai obrigou o Brasil a reduzir suas tarifas aplicadas ao nível das tarifas "
                "consolidadas dos países desenvolvidos.”</i> → ERRADO (troca de conceito: consolidou tetos "
                "próprios, acima das aplicadas)",
                "<i>“A Rodada Uruguai incorporou a agricultura às disciplinas multilaterais de comércio.”</i> → "
                "CERTO",
            ]),
        ],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["uma de suas consequências"], "dificuldade": 2,
        "comentario_fonte": ("Rodada Uruguai (1986–1994) criou a OMC; impôs limites a subsídios agrícolas e "
                             "industriais; o Brasil consolidou tarifas máximas, sem redução imediata das "
                             "aplicadas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 453", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["dado_aproximado: tetos consolidados do Brasil (~35% industriais, ~55% agrícolas) citados de "
                    "memória, em ordem de grandeza"],
    },
    # ------------------------------------------------------------------ E3-L00325
    {
        "id": "ECO-E3-L00325-1", "fonte_ref": "E3-L00325", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TQ,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de tarifas de importação e exportação alteram os preços relativos dos produtos "
                      "comercializados internacionalmente, no entanto, elas não alteraram o excedente dos "
                      "consumidores, dado que esses ajustam suas cestas de consumo de acordo a sempre manter o "
                      "mesmo nível de bem-estar."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A imposição de tarifas de importação e exportação alteram os preços relativos dos produtos "
                       "comercializados internacionalmente, ") + vm("no entanto, elas não alteraram")
                    + az(" o excedente dos consumidores, ") + vm("dado que esses ajustam suas cestas de consumo "
                                                                 "de acordo a sempre manter o mesmo nível de "
                                                                 "bem-estar") + az(".")),
        "poucas": ("Se a tarifa muda o preço que o consumidor paga, muda o " + azb("excedente do consumidor")
                   + ": a tarifa de importação o reduz; a de exportação, ao baixar o preço interno, o aumenta. "
                   "Ajustar a cesta atenua a perda, mas não devolve o bem-estar inicial."),
        "destrinchando": [
            azb("Tarifa de importação") + " (país pequeno): o preço interno sobe para P<sub>m</sub> + t; o "
            "consumidor paga mais e consome menos. Perde a faixa entre os dois preços até a demanda: parte vai "
            "ao produtor, parte ao governo (receita) e o resto é " + azb("peso morto") + ".",
            azb("Tarifa de exportação") + ": o exportador passa a receber, lá fora, P<sub>m</sub> − t, e por "
            "isso aceita vender internamente a esse preço menor. O preço doméstico <b>cai</b>: o consumidor "
            "<b>ganha</b> excedente, o produtor perde, o governo arrecada, e há peso morto. Também aqui o "
            "excedente do consumidor muda — no sentido oposto.",
            "Por que “ajustar a cesta” não salva: na teoria do consumidor, um aumento de preço contrai a "
            "restrição orçamentária e leva a uma " + azb("curva de indiferença mais baixa") + ". Manter a "
            "utilidade exigiria compensação de renda (variação compensatória de " + oc("Hicks") + "), que a "
            "tarifa não dá. A substituição só reduz o tamanho da perda.",
            "O item ainda acerta que as tarifas alteram preços relativos — é justamente por isso que alteram "
            "excedentes.",
            vm("Regra-âncora: preço do consumidor muda → excedente do consumidor muda; tarifa de importação reduz, "
               "tarifa de exportação aumenta."),
        ],
        "dissecando": (cz("[contradição · nexo indevido]") + " O item é incoerente por dentro: admite que os "
                       "preços mudam e nega o efeito sobre o excedente, sustentado por uma justificativa falsa "
                       "(ajuste da cesta preservaria o bem-estar). Pista: “sempre manter o mesmo nível de "
                       "bem-estar” é um absoluto que só a compensação de renda garantiria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma tarifa de exportação, em país pequeno, reduz o preço doméstico do bem e eleva o excedente do "
            "consumidor nacional.”</i> → CERTO",
            "<i>“A tarifa de importação reduz o excedente do consumidor, mas essa perda é integralmente "
            "transferida ao governo sob a forma de receita.”</i> → ERRADO (meia-verdade: parte vai ao produtor e "
            "parte é peso morto)",
        ])],
        "reescrita": ("A imposição de tarifas de importação e exportação alteram os preços relativos dos produtos "
                      "comercializados internacionalmente, " + hl("e, por isso, alteram") + " o excedente dos "
                      "consumidores, " + hl("que não conseguem ajustar suas cestas de consumo de modo a manter o "
                      "mesmo nível de bem-estar") + "."),
        "tipo_erro": ["CONTRADICAO", "NEXO_INDEVIDO"], "moduladores": ["sempre"], "dificuldade": 1,
        "comentario_fonte": ("Tarifa eleva o preço doméstico, reduz quantidade demandada e o excedente do "
                             "consumidor; ajuste da cesta não mantém a utilidade (curva de indiferença inferior); "
                             "há peso morto. Quadro: consumidores −B−C−D; produtores +A+C; governo +D+E."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 454", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"},
                          {"ref": "IMAGEM 455", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (dois países, ilegível; mecanismo descrito no 📖)"},
                          {"ref": "IMAGEM 456", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"},
                          {"ref": "IMAGEM 457", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"},
                          {"ref": "IMAGEM 458", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 459", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"},
                          {"ref": "IMAGEM 460", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00326
    {
        "id": "ECO-E3-L00326-1", "fonte_ref": "E3-L00326", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TQ,
        "rotulo_item": "Item",
        "assertiva": ("A tarifa lump sum, ou tarifa específica, é um imposto de valor fixo que independe do valor "
                      "do transacionado, dependendo apenas do número de unidades recebida pelo país importador."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A tarifa lump sum, ou tarifa específica, é um imposto de <u>valor fixo</u> que "
                      "<u>independe do valor</u> do transacionado, dependendo apenas do <u>número de unidades</u> "
                      "recebida pelo país importador."),
        "poucas": ("A " + azb("tarifa específica") + " cobra um valor monetário fixo por unidade física (US$ 2 "
                   "por par, R$ 0,50 por litro), qualquer que seja o preço do bem; a " + azb("ad valorem")
                   + " cobra um percentual do valor."),
        "destrinchando": [
            "Tipos de tarifa pela base de cálculo: " + azb("ad valorem") + " (percentual sobre o valor aduaneiro, "
            "em geral CIF — ex.: 20%); " + azb("específica") + " (valor fixo por unidade, peso ou volume); "
            + azb("mista ou composta") + " (combinação das duas, ex.: 10% + US$ 2 por unidade).",
            "Efeitos da específica: a proteção, em termos percentuais, <b>sobe quando o preço mundial cai</b> e "
            "<b>se corrói com a inflação</b> (o valor nominal fica parado). É " + azb("regressiva") + " dentro "
            "da mesma categoria: pesa mais, proporcionalmente, sobre a versão barata do produto, o que incentiva "
            "importar a variedade de maior valor (efeito <i>upgrading</i>).",
            "A ad valorem acompanha preço e inflação e é mais transparente para comparação internacional; em "
            "compensação, depende da valoração aduaneira e abre espaço ao subfaturamento. A específica é simples "
            "de cobrar (basta contar ou pesar).",
            "Sobre o rótulo do item: na teoria tributária, <i>lump sum</i> designa o imposto de "
            + azb("montante fixo") + " que não depende de nenhuma decisão do contribuinte (e por isso não "
            "distorce). A tarifa específica depende da quantidade importada, logo não é <i>lump sum</i> nesse "
            "sentido estrito; o item usa o termo como sinônimo informal de “valor fixo por unidade”, e a "
            "definição que dá é a correta.",
            "No " + rx("Brasil") + ", o Imposto de Importação segue a TEC do Mercosul e é essencialmente "
            "<b>ad valorem</b>.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " A definição está certa; o ruído é o rótulo “lump sum”, "
                       "impreciso na teoria, que pode levar o candidato a marcar ERRADO por desconfiança. Julgue "
                       "pelo conteúdo: valor fixo por unidade, independente do preço = específica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A tarifa específica mantém constante a proteção efetiva quando o preço internacional do bem "
            "cai.”</i> → ERRADO (inversão: com preço menor, a proteção percentual aumenta)",
            "<i>“A tarifa ad valorem é calculada como percentual do valor da mercadoria importada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("Tarifa específica: valor fixo por unidade física, independente do preço; ad valorem: "
                             "percentual do valor; composta: combinação. Ressalva: “lump sum” não é a nomenclatura "
                             "técnica (em teoria, imposto de montante fixo total)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 461", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 462", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 463", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["nota_redacao: termo “lump sum” impreciso no enunciado; gabarito mantido por a definição dada "
                    "ser a da tarifa específica"],
    },
    # ------------------------------------------------------------------ E3-L00327
    {
        "id": "ECO-E3-L00327-1", "fonte_ref": "E3-L00327", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TQ,
        "rotulo_item": "Item",
        "assertiva": ("A quota de importação tem o mesmo objetivo de um imposto sobre importações, contudo o peso "
                      "morto causado pela sua adoção não é parcialmente compensado com arrecadação tributária, o "
                      "que a difere dos impostos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A quota de importação tem o mesmo objetivo de um imposto sobre importações, contudo o peso "
                      "morto causado pela sua adoção <u>não é parcialmente compensado com arrecadação "
                      "tributária</u>, o que a difere dos impostos."),
        "poucas": ("Cota e tarifa equivalentes geram o mesmo preço, o mesmo peso morto e o mesmo retângulo entre "
                   "os preços; na tarifa ele é " + azb("receita do governo") + "; na cota, " + azb("renda da cota")
                   + " de quem detém as licenças."),
        "destrinchando": [
            "Objetivo comum: elevar o preço interno, reduzir importações e proteger a produção nacional. Em "
            "concorrência perfeita, para cada cota existe uma " + azb("tarifa equivalente") + " que produz o "
            "mesmo preço e as mesmas quantidades (" + oc("Jagdish Bhagwati") + ", 1965).",
            "A diferença está no retângulo (P<sub>interno</sub> − P<sub>m</sub>) × importações: com tarifa, é "
            + azb("arrecadação") + " que fica com o Estado; com cota, é " + azb("renda da cota") + " (<i>quota "
            "rent</i>), apropriada por quem tem o direito de importar.",
            "Destino da renda da cota: (i) licenças gratuitas a importadores nacionais → fica no país, mas com "
            "privado; (ii) " + azb("restrição voluntária de exportação") + " (o exportador controla a cota) → vai "
            "para o estrangeiro e a perda nacional aumenta; (iii) " + azb("leilão de licenças") + " → vira "
            "receita pública, e a cota fica economicamente idêntica à tarifa.",
            "Além disso, a cota estimula " + azb("rent-seeking") + " (gasto de recursos para obter licenças), "
            "que pode dissipar a renda e ampliar a perda social, e trava a importação mesmo se a demanda crescer, "
            "fazendo o preço subir mais que sob a tarifa.",
            "Por isso a OMC prefere tarifas: o " + vd("art. XI do GATT") + " proíbe, em regra, restrições "
            "quantitativas; o Acordo sobre Agricultura converteu cotas em tarifas (" + azb("tarificação") + ").",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Formulação correta do resultado-padrão. O ponto "
                       "decisivo é ler “não é parcialmente compensado com arrecadação tributária”: o peso morto "
                       "é o mesmo; o que muda é o destino do retângulo. A armadilha seria afirmar que a cota gera "
                       "peso morto <b>maior</b> que a tarifa equivalente (só ocorre com rent-seeking ou "
                       "demanda crescente)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se as licenças de importação forem leiloadas pelo governo, a cota produz efeitos de bem-estar "
            "equivalentes aos da tarifa.”</i> → CERTO",
            "<i>“A restrição voluntária de exportação é menos custosa para o país importador do que a tarifa "
            "equivalente.”</i> → ERRADO (inversão: a renda da cota vai para o exportador estrangeiro)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["parcialmente"], "dificuldade": 2,
        "comentario_fonte": ("Tarifa e quota protegem igualmente; na tarifa o retângulo é arrecadação, na quota é "
                             "renda de quota (licenças gratuitas, VERs, leilão); OMC prefere tarifas; rent-seeking."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 464", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00328
    {
        "id": "ECO-E3-L00328-1", "fonte_ref": "E3-L00328", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_TQ,
        "rotulo_item": "Item",
        "assertiva": ("Apesar de as quotas imporem um limite ao número de unidades que podem ser importadas, elas "
                      "não afetam os preços do produto comercializado, já que a taxa de câmbio se ajusta para "
                      "compensar qualquer efeito sobre os preços, elemento que atua como outro diferenciador em "
                      "relação aos impostos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Apesar de as quotas imporem") + az(" um limite ao número de unidades que podem ser "
                                                           "importadas, elas ")
                    + vm("não afetam os preços do produto comercializado, já que a taxa de câmbio se ajusta para "
                         "compensar qualquer efeito sobre os preços, elemento que atua como outro diferenciador em "
                         "relação aos impostos") + az(".")),
        "poucas": ("A cota restringe a oferta disponível e " + azb("eleva o preço interno") + ", exatamente como "
                   "a tarifa equivalente. Câmbio não neutraliza o efeito sobre um produto específico, e preço não "
                   "é o que diferencia cota de tarifa."),
        "destrinchando": [
            "Mecanismo: com a importação limitada, a oferta total (nacional + cota) fica abaixo da demanda ao "
            "preço mundial; o preço interno sobe até que Q<sub>D</sub> − Q<sub>S</sub> = cota. Resultado: "
            + vd("P ↑") + ", consumo ↓, produção nacional ↑.",
            "O câmbio é um preço macroeconômico, determinado por fluxos de comércio e de capitais, juros, "
            "expectativas. Uma cota sobre um bem altera marginalmente a demanda por divisas e não tem como "
            "“devolver” o preço daquele bem ao nível anterior. Mesmo em equilíbrio geral, eventual apreciação "
            "cambial afeta <b>todos</b> os bens comerciáveis, e não anula a cunha criada pela cota no bem "
            "restringido.",
            "Em concorrência perfeita, cota e tarifa são " + azb("equivalentes") + " em preço e quantidade ("
            + oc("Bhagwati") + "). As diferenças reais são outras: o destino do retângulo (receita na tarifa, "
            + azb("renda da cota") + " na cota), a resposta a choques de demanda (a cota trava a quantidade e "
            "deixa o preço subir mais) e, com monopólio doméstico, a cota pode dar poder de mercado que a "
            "tarifa não dá.",
            vm("Regra-âncora: cota afeta preço como a tarifa; o que muda é quem fica com a renda."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O item inventa um mecanismo (o câmbio "
                       "neutraliza o preço) e, sobre ele, cria uma falsa diferença entre cota e tarifa. Pista: a "
                       "concessão “apesar de imporem um limite” já denuncia a incoerência — limitar a quantidade "
                       "sem afetar o preço exigiria demanda perfeitamente inelástica."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em concorrência perfeita, uma quota de importação e a tarifa equivalente produzem o mesmo preço "
            "doméstico.”</i> → CERTO",
            "<i>“Sob quota, um aumento da demanda doméstica eleva as importações, mantendo o preço "
            "constante.”</i> → ERRADO (inversão: isso ocorre com a tarifa; com cota, sobe o preço)",
        ])],
        "reescrita": (hl("Como as quotas impõem") + " um limite ao número de unidades que podem ser importadas, "
                      "elas " + hl("elevam o preço interno do produto comercializado, como faria a tarifa "
                      "equivalente; o que as diferencia dos impostos é o destino da renda gerada, que vai a quem "
                      "detém as licenças, e não ao governo") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": ["qualquer"], "dificuldade": 1,
        "comentario_fonte": ("Quotas afetam preços (restrição de oferta eleva o preço interno); o ajuste cambial "
                             "automático não tem fundamento; cota e tarifa são equivalentes em preço e quantidade "
                             "(Bhagwati), diferindo na apropriação da renda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 465", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_corrigido: “podem sem importadas” → “podem ser importadas” (erro de digitação da fonte)"],
    },
    # ------------------------------------------------------------------ E3-L00361
    {
        "id": "ECO-E3-L00361-1", "fonte_ref": "E3-L00361", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": CMD_MSUE,
        "excerto": EXC_MSUE,
        "rotulo_item": "Item",
        "assertiva": ("Em conformidade com as normas da OMC, o capítulo de Defesa Comercial do Acordo limita a "
                      "possibilidade de aplicação de medidas antidumping e compensatórias entre as partes, em favor "
                      "da liberalização comercial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em conformidade com as normas da OMC, o capítulo de Defesa Comercial do Acordo ")
                    + vm("limita a possibilidade de aplicação de") + az(" medidas antidumping e compensatórias "
                                                                       "entre as partes")
                    + vm(", em favor da liberalização comercial") + az(".")),
        "poucas": ("O capítulo de defesa comercial do acordo Mercosul–UE " + azb("reafirma") + " os direitos e "
                   "obrigações da OMC: as partes continuam podendo aplicar antidumping e medidas compensatórias, "
                   "observados os acordos multilaterais."),
        "destrinchando": [
            "Acordos de livre comércio, em regra, <b>preservam</b> os instrumentos de " + azb("defesa "
            "comercial") + " — antidumping, medidas compensatórias e salvaguardas — nos termos do " + vd("art. VI "
            "do GATT") + ", do " + azb("Acordo Antidumping") + " e do " + azb("ASMC") + ". Isso não contraria a "
            "liberalização: são remédios contra comércio desleal (dumping, subsídio), não barreiras.",
            "O que esses capítulos costumam acrescentar é procedimento: transparência, notificação prévia, "
            "consultas e troca de informações antes da aplicação. O acordo Mercosul–UE também prevê "
            + azb("salvaguardas bilaterais") + " para surtos de importação decorrentes da própria redução "
            "tarifária no período de transição.",
            "Exceção que confirma a regra: só em integrações profundas a defesa comercial intrabloco desaparece "
            "— na UE, o mercado único substituiu o antidumping entre membros pelas regras de concorrência e de "
            "auxílios de Estado.",
            "Contexto ⏳ (out/2026): as negociações foram concluídas politicamente em " + vd("dezembro de 2024")
            + " (Cúpula de Montevidéu), após mais de 25 anos; a entrada em vigor depende das etapas de "
            "assinatura e ratificação nas partes, e o acordo segue cercado de resistências agrícolas europeias.",
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " O item inverte o conteúdo do capítulo (preserva → "
                       "limita) e acrescenta uma justificativa de aparência lógica (“em favor da liberalização”). "
                       "Pista: “em conformidade com as normas da OMC” combina com <b>preservar</b> os direitos "
                       "multilaterais, não com restringi-los."),
        "modulos": [
            ("🟣 Posição do Brasil", [
                rx("O Brasil") + " é usuário frequente de antidumping (investigação pela Secex, decisão pelo "
                "Gecex/Camex) e buscou, na negociação, manter intacto esse instrumental e garantir salvaguardas "
                "para setores sensíveis da indústria.",
            ]),
            ("😈 Para dificultar", [
                "<i>“O acordo Mercosul–UE reafirma os direitos e obrigações das partes no âmbito da OMC em matéria "
                "de antidumping e medidas compensatórias.”</i> → CERTO",
                "<i>“O acordo elimina a possibilidade de salvaguardas entre as partes durante o período de "
                "transição.”</i> → ERRADO (inversão: prevê salvaguardas bilaterais)",
            ]),
        ],
        "reescrita": ("Em conformidade com as normas da OMC, o capítulo de Defesa Comercial do Acordo "
                      + hl("preserva o direito de aplicação de") + " medidas antidumping e compensatórias entre as "
                      "partes" + hl(", observados os acordos multilaterais") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O capítulo de Defesa Comercial reafirma os direitos de aplicação de antidumping e "
                             "medidas compensatórias conforme a OMC; ALCs não restringem esses instrumentos, apenas "
                             "acrescentam transparência e diálogo prévio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 514", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 515", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (repetia a assertiva)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00395
    {
        "id": "ECO-E3-L00395-1", "fonte_ref": "E3-L00395", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NOV,
        "excerto": EXC_NOV,
        "rotulo_item": "Item",
        "assertiva": ("Adoção de acordos comerciais regionais e a implementação de normas técnicas são formas de "
                      "barreiras não-tarifárias que, ao facilitar a integração e a harmonização de mercados entre "
                      "países membros, podem resultar em distúrbios nas relações comerciais com países "
                      "não-participantes, potencialmente criando efeitos de exclusão ou distorcendo a competição "
                      "internacional, ao favorecer a cooperação intrabloco em detrimento das trocas com o resto do "
                      "mundo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Adoção de acordos comerciais regionais e a implementação de normas técnicas são formas de "
                      "<u>barreiras não-tarifárias</u> que, ao facilitar a integração e a harmonização de mercados "
                      "entre países membros, <u>podem</u> resultar em distúrbios nas relações comerciais com países "
                      "não-participantes, potencialmente criando efeitos de exclusão ou distorcendo a competição "
                      "internacional, ao favorecer a cooperação intrabloco em detrimento das trocas com o resto do "
                      "mundo."),
        "poucas": ("Acordos regionais e normas harmonizadas no bloco podem gerar " + azb("desvio de comércio")
                   + " e exclusão de terceiros — o núcleo do item está certo, protegido por “podem” e "
                   "“potencialmente”."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "classificar “acordos comerciais regionais” como barreira não tarifária é impreciso: "
                          "acordo regional é forma de integração (preferência tarifária), e não instrumento de "
                          "barreira; barreiras não tarifárias são cotas, licenças, normas técnicas, medidas "
                          "sanitárias, exigências de conteúdo local. Numa prova CEBRASPE, a enumeração poderia "
                          "levar ao ERRADO; o gabarito CERTO se apoia nos efeitos (desvio de comércio, exclusão) "
                          "e nos moduladores.")],
        "destrinchando": [
            oc("Jacob Viner") + " (<i>The Customs Union Issue</i>, 1950): a integração regional gera "
            + azb("criação de comércio") + " (produção cara de um membro substituída por importação mais barata "
            "de outro membro — ganho) e " + azb("desvio de comércio") + " (importação de terceiro eficiente "
            "substituída por importação de membro menos eficiente, só porque este não paga tarifa — perda). O "
            "efeito líquido é ambíguo.",
            "Harmonização de " + azb("normas técnicas") + " e reconhecimento mútuo dentro do bloco barateiam o "
            "comércio intrabloco, mas o produtor de fora continua tendo de certificar-se separadamente — é um "
            "canal não tarifário de exclusão.",
            "Na OMC, o " + vd("art. XXIV do GATT") + " admite uniões aduaneiras e áreas de livre comércio se "
            "cobrirem “substancialmente todo o comércio” e não elevarem as barreiras a terceiros; a "
            + azb("Cláusula de Habilitação") + " (" + vd("1979") + ") permite acordos entre países em "
            "desenvolvimento (base do Mercosul). Normas técnicas seguem o " + azb("Acordo TBT") + " (e o SPS, "
            "para sanitárias), que exige não discriminação e não serem mais restritivas que o necessário.",
            "Contraponto: o “regionalismo aberto” da Cepal (anos 1990) via os blocos como degrau para a inserção "
            "global, não como fortaleza.",
        ],
        "dissecando": (cz("[modulador relativo · paráfrase fiel]") + " O efeito descrito (desvio de comércio, "
                       "exclusão) é real, e “podem” + “potencialmente” protegem a afirmação. O ponto frágil é a "
                       "classificação inicial; em itens longos, separe a premissa conceitual (o que é BNT) do "
                       "efeito (o que pode acontecer)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Acordos regionais de comércio sempre elevam o bem-estar mundial, por eliminarem tarifas entre os "
            "membros.”</i> → ERRADO (modulador absoluto: o desvio de comércio pode superar a criação)",
            "<i>“O Acordo TBT da OMC exige que regulamentos técnicos não sejam mais restritivos ao comércio do "
            "que o necessário para alcançar um objetivo legítimo.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], "moduladores": ["podem", "potencialmente"],
        "dificuldade": 2,
        "comentario_fonte": ("Acordos regionais podem gerar desvio de comércio, favorecendo membros ineficientes em "
                             "detrimento de não membros mais eficientes."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: “acordos comerciais regionais” não são, a rigor, barreira não tarifária; "
                    "ERRADO seria defensável pela classificação"],
    },
    # ------------------------------------------------------------------ E3-L00396
    {
        "id": "ECO-E3-L00396-1", "fonte_ref": "E3-L00396", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NOV,
        "excerto": EXC_NOV,
        "rotulo_item": "Item",
        "assertiva": ("A adoção de normas técnicas rigorosas, como certificações ambientais ou padrões de "
                      "qualidade, visa principalmente garantir a segurança dos consumidores e não costuma "
                      "representar um desafio significativo para os países em desenvolvimento no acesso aos "
                      "mercados dos países mais avançados."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A adoção de normas técnicas rigorosas, como certificações ambientais ou padrões de "
                       "qualidade, visa principalmente garantir a segurança dos consumidores e ")
                    + vm("não costuma representar") + az(" um desafio significativo para os países em "
                                                        "desenvolvimento no acesso aos mercados dos países mais "
                                                        "avançados.")),
        "poucas": ("Normas técnicas rigorosas são uma das principais " + azb("barreiras não tarifárias") + " "
                   "enfrentadas pelos países em desenvolvimento: certificar, testar e rastrear custa caro e exige "
                   "infraestrutura que muitos não têm."),
        "destrinchando": [
            "Com a queda das tarifas após as rodadas do GATT, ganharam peso as " + azb("barreiras técnicas")
            + " (regulamentos, normas, procedimentos de avaliação da conformidade) e as " + azb("medidas "
            "sanitárias e fitossanitárias") + ". É o chamado " + azb("neoprotecionismo") + ".",
            "Por que pesam mais sobre o país em desenvolvimento: exigem " + azb("infraestrutura da qualidade")
            + " (laboratórios acreditados, metrologia, certificadoras), têm altos custos fixos (prejudicam "
            "pequenos produtores), mudam com frequência e muitas vezes vêm de " + azb("padrões privados")
            + " (redes varejistas) ainda mais exigentes que a regulação pública.",
            "Os objetivos legítimos vão além da segurança do consumidor: saúde humana, animal e vegetal, meio "
            "ambiente, informação ao consumidor, compatibilidade técnica. A dificuldade está em separar o "
            "objetivo legítimo do " + azb("protecionismo disfarçado") + ".",
            "Na OMC, o " + azb("Acordo TBT") + " e o " + azb("Acordo SPS") + " admitem as normas, mas exigem "
            "não discriminação, base científica (SPS), preferência por padrões internacionais e que a medida "
            "não seja mais restritiva que o necessário; preveem ainda assistência técnica e tratamento especial "
            "para países em desenvolvimento.",
            "Exemplo atual ⏳ (out/2026): o " + rx("regulamento europeu antidesmatamento (EUDR)") + ", que exige "
            "comprovação de origem livre de desmatamento para soja, carne, café, cacau e madeira, é contestado "
            "pelo " + rx("Brasil") + " justamente pelo custo de rastreabilidade para exportadores.",
        ],
        "dissecando": (cz("[inversão · juízo indevido]") + " O item nega o ponto central da literatura sobre "
                       "barreiras técnicas (o custo de conformidade é desproporcional para países em "
                       "desenvolvimento). A primeira oração, que reduz o objetivo das normas à segurança do "
                       "consumidor, é simplificadora, mas o erro decisivo é o “não costuma representar um "
                       "desafio”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Normas técnicas legítimas podem funcionar, na prática, como barreiras não tarifárias, ao imporem "
            "custos de conformidade elevados a exportadores de países em desenvolvimento.”</i> → CERTO",
            "<i>“O Acordo TBT da OMC proíbe a adoção de regulamentos técnicos mais rigorosos que os padrões "
            "internacionais.”</i> → ERRADO (extrapolação: admite-os se justificados e não discriminatórios)",
        ])],
        "reescrita": ("A adoção de normas técnicas rigorosas, como certificações ambientais ou padrões de "
                      "qualidade, visa principalmente garantir a segurança dos consumidores e "
                      + hl("costuma representar") + " um desafio significativo para os países em desenvolvimento "
                      "no acesso aos mercados dos países mais avançados."),
        "tipo_erro": ["INVERSAO", "JUIZO_INDEVIDO"], "moduladores": ["principalmente", "não costuma"],
        "dificuldade": 1,
        "comentario_fonte": ("Normas técnicas são grandes BNTs: países em desenvolvimento muitas vezes não têm "
                             "tecnologia ou recursos para cumprir padrões rigorosos (infraestrutura da qualidade, "
                             "custos fixos, padrões privados); TBT e SPS na OMC."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 572", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00397
    {
        "id": "ECO-E3-L00397-1", "fonte_ref": "E3-L00397", "destino": "79", "subtema": H2["sub"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NOV,
        "excerto": EXC_NOV,
        "rotulo_item": "Item",
        "assertiva": ("O uso de subsídios à exportação, embora possa aumentar a competitividade dos produtos de um "
                      "país no mercado internacional, pode levar a disputas comerciais e ações antidumping, uma vez "
                      "que os países concorrentes podem alegar que o subsídio distorce as condições de competição e "
                      "leva à venda de produtos abaixo do custo de produção, prejudicando suas indústrias locais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O uso de subsídios à exportação, embora possa aumentar a competitividade dos produtos de um "
                      "país no mercado internacional, <u>pode</u> levar a disputas comerciais e <u>ações "
                      "antidumping</u>, uma vez que os países concorrentes podem alegar que o subsídio distorce as "
                      "condições de competição e leva à venda de produtos abaixo do custo de produção, prejudicando "
                      "suas indústrias locais."),
        "poucas": ("Subsídio à exportação é " + azb("proibido") + " na OMC e gera disputas e retaliação. O item "
                   "está certo no efeito, mas o remédio técnico contra subsídio é a " + azb("medida "
                   "compensatória") + ", não o antidumping."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "na terminologia da OMC, o instrumento contra subsídio concedido por governo é o "
                          + vd("direito compensatório") + " (ASMC), enquanto o " + vd("antidumping")
                          + " responde a preço de exportação abaixo do valor normal praticado pela empresa. "
                          "Uma prova CEBRASPE poderia considerar o item ERRADO pela troca. O CERTO se sustenta "
                          "pelos moduladores (“pode”, “podem alegar”) e porque, na prática, exportações "
                          "subsidiadas a preço abaixo do custo também podem ser alvo de investigação "
                          "antidumping (valor normal construído).")],
        "destrinchando": [
            azb("Acordo sobre Subsídios e Medidas Compensatórias (ASMC)") + ": subsídio = contribuição financeira "
            "do governo que confere benefício, sendo " + azb("específico") + ". Classes: " + vd("proibidos")
            + " (vinculados à exportação ou ao uso de conteúdo local, art. 3) e " + vd("acionáveis") + " "
            "(contestáveis se causarem efeitos adversos).",
            "Dois caminhos contra um subsídio: (i) o " + azb("multilateral") + " — painel no Órgão de Solução de "
            "Controvérsias, que pode autorizar retaliação; (ii) o " + azb("unilateral") + " — investigação "
            "nacional e imposição de " + azb("direito compensatório") + " sobre as importações subsidiadas, se "
            "houver dano à indústria doméstica e nexo causal.",
            azb("Antidumping") + " é outra coisa: combate a discriminação de preços praticada pela "
            "<b>empresa</b> exportadora (preço de exportação &lt; valor normal), sem precisar provar subsídio "
            "governamental.",
            "Casos emblemáticos: " + rx("Embraer × Bombardier") + " (Brasil e Canadá se condenaram mutuamente "
            "por subsídios a jatos regionais — Proex × apoios canadenses, 1999–2002) e o contencioso do "
            + rx("algodão") + " contra os EUA.",
            vm("Regra-âncora: subsídio de governo → medida compensatória; preço de empresa abaixo do valor normal "
               "→ antidumping; surto de importações leais → salvaguarda."),
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " O item é salvo pelos “pode”/“podem alegar”, mas "
                       "embaralha os remédios de defesa comercial. 🔥 A distinção antidumping × compensatória × "
                       "salvaguarda é cobrança clássica do CEBRASPE; num item de banca oficial, “ações "
                       "antidumping contra subsídios” costuma ser o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Contra exportações subsidiadas que causem dano à indústria doméstica, o país importador pode "
            "aplicar direitos compensatórios.”</i> → CERTO",
            "<i>“Os subsídios à exportação de bens industriais são acionáveis, isto é, permitidos salvo prova de "
            "efeitos adversos.”</i> → ERRADO (troca de conceito: são proibidos)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["pode", "podem alegar"],
        "dificuldade": 2,
        "comentario_fonte": ("A OMC regula subsídios porque distorcem preços, permitindo que países afetados "
                             "apliquem medidas compensatórias."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: o remédio contra subsídio é a medida compensatória, não o antidumping; ERRADO "
                    "seria defensável pela troca de instrumento"],
    },
    # ------------------------------------------------------------------ E3-L00398
    {
        "id": "ECO-E3-L00398-1", "fonte_ref": "E3-L00398", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NOV,
        "excerto": EXC_NOV,
        "rotulo_item": "Item",
        "assertiva": ("A imposição de tarifas à importação tem como principal efeito o aumento da competitividade "
                      "dos produtos domésticos, provocando impactos positivos sobre o bem-estar de produtores e "
                      "consumidores nacionais, uma vez que estimula um maior nível de produção nacional e o consumo "
                      "de bens internamente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A imposição de tarifas à importação tem como principal efeito o aumento da competitividade "
                       "dos produtos domésticos, provocando impactos positivos sobre o bem-estar de produtores ")
                    + vm("e consumidores") + az(" nacionais, uma vez que estimula um maior nível de produção "
                                                "nacional ") + vm("e o consumo de bens internamente") + az(".")),
        "poucas": ("A tarifa eleva o preço interno: o " + azb("produtor") + " ganha, mas o " + azb("consumidor")
                   + " perde — paga mais e consome menos. Há receita para o governo e " + azb("peso morto")
                   + "; o bem-estar total cai (país pequeno)."),
        "destrinchando": [
            "Efeitos da tarifa em país pequeno: preço interno P<sub>m</sub> + t; " + azb("efeito produção")
            + " (Q<sup>S</sup> ↑, produtor ganha excedente); " + azb("efeito consumo") + " (Q<sup>D</sup> ↓, "
            "consumidor perde excedente); " + azb("efeito receita") + " (governo arrecada t × importações); "
            + azb("efeito comércio") + " (importações ↓).",
            "Saldo: a perda do consumidor é maior que a soma do ganho do produtor com a receita; a diferença são "
            "os dois triângulos de " + azb("peso morto") + " (distorção de produção e de consumo).",
            "O consumo interno do bem <b>diminui</b>: o aumento da produção nacional não compensa a queda das "
            "importações, porque o preço é mais alto para todos.",
            "Argumentos pró-tarifa existem, mas são outros: " + azb("indústria nascente") + " (" + oc("Hamilton")
            + ", " + oc("List") + "), " + azb("tarifa ótima") + " em país grande, correção de falhas de mercado e "
            "a tradição cepalina de industrialização por substituição de importações. Nenhum deles afirma que o "
            "consumidor ganha no curto prazo.",
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " Parte verdadeira (produtor ganha, produção nacional "
                       "sobe) com parte falsa enxertada (consumidor ganha, consumo sobe). Pista: medida que "
                       "beneficia “produtores e consumidores” ao mesmo tempo, via aumento de preço, é contradição "
                       "em termos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A tarifa de importação transfere excedente dos consumidores para os produtores domésticos e para "
            "o governo, com perda líquida de bem-estar.”</i> → CERTO",
            "<i>“A tarifa reduz o consumo interno, mas o aumento da produção nacional compensa exatamente a queda "
            "das importações.”</i> → ERRADO (as importações caem mais do que a produção sobe)",
        ])],
        "reescrita": ("A imposição de tarifas à importação tem como principal efeito o aumento da competitividade "
                      "dos produtos domésticos, provocando impactos positivos sobre o bem-estar de produtores "
                      + hl("e negativos sobre o de consumidores") + " nacionais, uma vez que estimula um maior "
                      "nível de produção nacional " + hl("mas reduz o consumo do bem internamente") + "."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Tarifas geram peso morto; ajudam produtores locais, mas prejudicam consumidores "
                             "(preços mais altos) e reduzem o bem-estar agregado."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 573", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00432
    {
        "id": "ECO-E3-L00432-1", "fonte_ref": "E3-L00432", "destino": "79", "subtema": H2["tar"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_OUT,
        "excerto": EXC_OUT,
        "rotulo_item": "Item",
        "assertiva": ("Seguindo a tradição das teorias críticas, segundo modelos de comércio mais modernos, como o "
                      "modelo gravitacional, em um cenário de livre comércio, a imposição de tarifas sobre produtos "
                      "importados pode resultar em um aumento da receita do governo e, ao mesmo tempo, uma melhoria "
                      "no bem-estar econômico total do país que impõe a tarifa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Seguindo a tradição das teorias críticas, segundo modelos de comércio mais modernos, como "
                       "o modelo gravitacional") + az(", em um cenário de livre comércio, a imposição de tarifas "
                                                      "sobre produtos importados pode resultar em um aumento da "
                                                      "receita do governo e, ao mesmo tempo, uma melhoria no "
                                                      "bem-estar econômico total do país que impõe a tarifa.")),
        "poucas": ("Tarifa com ganho de bem-estar nacional é o argumento da " + azb("tarifa ótima") + ", da teoria "
                   + azb("neoclássica") + " e válido só para " + azb("país grande") + ". Não vem das teorias "
                   "críticas nem do " + azb("modelo gravitacional") + ", que é empírico."),
        "destrinchando": [
            azb("Tarifa ótima") + ": um país grande, com poder sobre o preço mundial, ao tarifar reduz sua "
            "demanda por importações e força a queda do preço que paga ao exterior — melhora dos "
            + azb("termos de troca") + ". Se esse ganho supera os triângulos de peso morto, o bem-estar nacional "
            "sobe (o mundo, porém, perde). Fórmula clássica: t* = 1/ε, com ε a elasticidade da oferta externa de "
            "exportações. Em país pequeno (ε → ∞), t* = 0.",
            azb("Modelo gravitacional") + " (" + oc("Jan Tinbergen") + ", 1962): o comércio bilateral cresce com "
            "o tamanho das economias (PIB) e cai com a distância. É uma ferramenta " + azb("empírica")
            + " de previsão de fluxos, não uma teoria normativa de tarifas e bem-estar.",
            azb("Teorias críticas") + " (estruturalismo cepalino, dependência): defendem proteção por razões de "
            "desenvolvimento — deterioração dos termos de troca da periferia (" + oc("Prebisch") + "–"
            + oc("Singer") + "), indústria nascente, mudança estrutural —, não pela maximização do excedente "
            "total no sentido neoclássico.",
            "Já as “novas teorias” (" + oc("Krugman") + ", concorrência imperfeita e economias de escala) "
            "abriram espaço para a " + azb("política comercial estratégica") + " (" + oc("Brander") + "–"
            + oc("Spencer") + "), mas com ressalvas fortes sobre retaliação e informação.",
        ],
        "dissecando": (cz("[troca de ator · troca de conceito]") + " A segunda metade descreve um resultado "
                       "verdadeiro em condições específicas (tarifa ótima); o erro está na atribuição a "
                       "tradições e modelos que não o sustentam. 🔥 Se aparecer “modelo gravitacional” + "
                       "“bem-estar” + “tarifa”, desconfie: a gravidade explica quem comercia com quem, não "
                       "prescreve política."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para um país pequeno, a tarifa ótima é nula.”</i> → CERTO",
            "<i>“O modelo gravitacional prevê que o comércio entre dois países aumenta com a distância entre "
            "eles.”</i> → ERRADO (inversão: diminui com a distância)",
        ])],
        "reescrita": (hl("Segundo a teoria neoclássica do comércio, no caso de um país grande, com poder sobre os "
                         "termos de troca (argumento da tarifa ótima)") + ", em um cenário de livre comércio, a "
                      "imposição de tarifas sobre produtos importados pode resultar em um aumento da receita do "
                      "governo e, ao mesmo tempo, uma melhoria no bem-estar econômico total do país que impõe a "
                      "tarifa."),
        "tipo_erro": ["TROCA_ATOR", "TROCA_CONCEITO"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": ("Mistura incoerente: tarifa ótima é argumento neoclássico para país grande; o modelo "
                             "gravitacional é empírico (PIB e distância), não normativo; teorias críticas defendem "
                             "proteção por razões de desenvolvimento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 598", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 599", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 600", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (não passa no teste do quadro-negro: o erro é de atribuição)"},
                          {"ref": "IMAGEM 601", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00464
    {
        "id": "ECO-E3-L00464-1", "fonte_ref": "E3-L00464", "destino": "79", "subtema": H2["cot"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_TEORIAS,
        "rotulo_item": "Item",
        "assertiva": ("Em economias que privilegiam a produção, quotas são preferíveis às tarifas, porque, as "
                      "tarifas tendem a reduzir o excedente de consumidores e produtores nacionais, já que esses "
                      "dividem a tarifa imposta de maneira proporcional às elasticidades preço da demanda e da "
                      "oferta pelo produto importado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em economias que privilegiam a produção, ") + vm("quotas são preferíveis às tarifas")
                    + az(", porque, as tarifas tendem a reduzir o excedente de consumidores ")
                    + vm("e produtores nacionais, já que esses dividem a tarifa imposta de maneira proporcional às "
                         "elasticidades preço da demanda e da oferta pelo produto importado") + az(".")),
        "poucas": ("A tarifa " + azb("aumenta") + " o excedente do produtor nacional — tal como a cota. E o ônus "
                   "da tarifa se divide entre " + azb("consumidores domésticos e exportadores estrangeiros")
                   + ", não entre consumidores e produtores nacionais."),
        "destrinchando": [
            "Tarifa e cota protegem o produtor do mesmo modo: ambas elevam o preço interno, a produção nacional "
            "e o " + azb("excedente do produtor") + ". Em concorrência perfeita, há uma tarifa equivalente a cada "
            "cota (" + oc("Bhagwati") + ").",
            azb("Incidência da tarifa") + ": quem divide a cunha são os " + azb("compradores domésticos") + " e "
            "os " + azb("vendedores estrangeiros") + ", na proporção inversa das elasticidades da demanda por "
            "importações e da oferta externa. Em " + azb("país pequeno") + " (oferta externa perfeitamente "
            "elástica), o consumidor doméstico arca com tudo; em país grande, parte recai sobre o exportador "
            "estrangeiro (melhora dos termos de troca).",
            "Não há regra geral de que cotas sejam preferíveis para quem privilegia a produção. Argumentos a "
            "favor da cota: certeza sobre a quantidade importada. Contra: perde-se a receita (vira renda da "
            "cota), o preço dispara quando a demanda cresce, há rent-seeking, e a OMC proíbe em regra restrições "
            "quantitativas (" + vd("art. XI do GATT") + ").",
            vm("Regra-âncora: tarifa → consumidor perde, produtor nacional ganha, governo arrecada, há peso morto."),
        ],
        "dissecando": (cz("[troca de ator · inversão]") + " O item pega a lógica da incidência de um imposto "
                       "interno (comprador × vendedor, conforme elasticidades) e troca o vendedor estrangeiro "
                       "pelo produtor nacional — que, na verdade, é o grande beneficiado. Pista: “reduzir o "
                       "excedente de produtores nacionais” com uma medida protecionista é contradição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um país pequeno, o ônus de uma tarifa de importação recai integralmente sobre os consumidores "
            "domésticos.”</i> → CERTO",
            "<i>“A cota de importação, ao contrário da tarifa, não eleva o excedente do produtor doméstico.”</i> "
            "→ ERRADO (ambas elevam o preço interno e o excedente do produtor)",
        ])],
        "reescrita": ("Em economias que privilegiam a produção, " + hl("quotas e tarifas protegem igualmente o "
                      "produtor") + ", porque, as tarifas tendem a reduzir o excedente de consumidores "
                      + hl("mas elevam o dos produtores nacionais; o ônus da tarifa divide-se entre consumidores "
                           "domésticos e exportadores estrangeiros, conforme as elasticidades da demanda por "
                           "importações e da oferta externa") + "."),
        "tipo_erro": ["TROCA_ATOR", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Tarifas aumentam (não reduzem) o excedente do produtor nacional; a incidência por "
                             "elasticidades divide o ônus entre consumidores domésticos e exportadores estrangeiros; "
                             "não há preferência geral por quotas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 668", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0489
    {
        "id": "ECO-E1-0489-1", "fonte_ref": "E1-0489", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_CONJ,
        "rotulo_item": "Item",
        "assertiva": ("A redução da participação do setor industrial na economia brasileira nos últimos anos pode "
                      "estar relacionada com a situação conhecida como doença holandesa, em que a abundância de "
                      "recursos naturais ou o bom desempenho de commodities leva a uma valorização cambial, "
                      "prejudicando a competitividade industrial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A redução da participação do setor industrial na economia brasileira nos últimos anos "
                      "<u>pode estar relacionada</u> com a situação conhecida como doença holandesa, em que a "
                      "abundância de recursos naturais ou o bom desempenho de commodities leva a uma valorização "
                      "cambial, prejudicando a competitividade industrial."),
        "poucas": ("A " + azb("doença holandesa") + " — boom de recursos naturais → apreciação cambial → perda de "
                   "competitividade da manufatura — é uma das explicações em debate para a "
                   + azb("desindustrialização") + " brasileira; o “pode” torna o item correto."),
        "destrinchando": [
            "O termo nasce da Holanda dos anos 1960–70: a descoberta de gás natural valorizou o florim e encolheu "
            "a indústria. Formalização de " + oc("Corden") + " e " + oc("Neary") + " (1982): o setor em boom "
            "atrai fatores (efeito deslocamento de recursos) e, via câmbio e demanda, encarece os não "
            "comerciáveis (efeito gasto), espremendo a manufatura exportadora.",
            "No " + rx("Brasil") + ", a tese foi difundida por " + oc("Bresser-Pereira") + ": no superciclo de "
            "commodities (" + vd("2003–2011") + "), a forte entrada de divisas apreciou o real e a indústria de "
            "transformação perdeu espaço no PIB e na pauta exportadora — a participação dos manufaturados nas "
            "exportações caiu e os produtos básicos voltaram a liderar a partir de " + vd("2010") + ".",
            "Explicações concorrentes ou complementares: desindustrialização “natural” (renda maior → demanda "
            "migra para serviços, como nos países ricos), mas no Brasil ela foi " + azb("precoce") + " (começou "
            "com renda per capita baixa, desde meados dos anos 1980, segundo " + oc("Palma") + "); juros reais "
            "altos; custo Brasil e baixa produtividade; competição chinesa.",
            "Contraponto: parte da literatura atribui o câmbio apreciado sobretudo aos juros e aos fluxos de "
            "capital, e não às commodities, e lembra que a desindustrialização é fenômeno global.",
        ],
        "dissecando": (cz("[modulador relativo]") + " O “pode estar relacionada” transforma uma tese disputada "
                       "num item correto: a banca não pede que a doença holandesa seja <b>a</b> causa, só que "
                       "seja uma explicação plausível. Seria ERRADO com “decorre exclusivamente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A desindustrialização brasileira decorre exclusivamente da doença holandesa provocada pelo "
            "pré-sal.”</i> → ERRADO (modulador absoluto e anacronismo: o processo é anterior ao pré-sal)",
            "<i>“Na doença holandesa, o boom de recursos naturais tende a depreciar a moeda nacional, estimulando "
            "a indústria.”</i> → ERRADO (inversão: aprecia a moeda e prejudica a indústria)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Países com recursos de extração tendem a se “viciar” na venda desses produtos, "
                             "postergando ou depredando a matriz industrial, motor autônomo do crescimento."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0918
    {
        "id": "ECO-E1-0918-1", "fonte_ref": "E1-0918", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simulado julho/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_PAUTA,
        "rotulo_item": "Item",
        "assertiva": ("O setor econômico brasileiro com maior crescimento nas exportações no ano de 2022 foi o "
                      "agropecuário, que apresentou aumento em valor, consequência da guerra na Ucrânia, mas também "
                      "foi registrada elevação nos volumes exportados."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O setor econômico brasileiro com maior crescimento nas exportações no ano de 2022 foi o "
                      "<u>agropecuário</u>, que apresentou aumento em valor, consequência da guerra na Ucrânia, mas "
                      "<u>também</u> foi registrada elevação nos volumes exportados."),
        "poucas": ("Em 2022, as exportações brasileiras bateram recorde ⏳ (out/2026), e a " + azb("agropecuária")
                   + " foi o setor de maior alta: sobretudo por preços — inflados pela guerra na Ucrânia —, mas "
                   "também por volume."),
        "destrinchando": [
            "Classificação da Secex por setor (ISIC): " + azb("agropecuária") + ", " + azb("indústria "
            "extrativa") + " e " + azb("indústria de transformação") + ". Em 2022 ⏳ (out/2026), as exportações "
            "totais chegaram a cerca de " + vd("US$ 335 bilhões") + " (recorde, alta próxima de 20%), com "
            "superávit comercial de cerca de " + vd("US$ 60 bilhões") + ".",
            "A guerra (fevereiro de 2022) tirou do mercado parte das exportações de grãos e fertilizantes da "
            "Ucrânia e da Rússia e elevou os preços de " + azb("milho, trigo, soja e óleos vegetais") + ". O "
            "efeito preço foi o principal motor do valor exportado pelo agro.",
            "Volume: houve quebra de safra de soja no Sul (estiagem), mas o " + azb("milho") + " teve "
            "exportações recordes — com a abertura do mercado chinês ao milho brasileiro no fim de 2022 — e "
            "cresceram carnes e açúcar, de modo que o volume agregado do setor também subiu ⏳ (out/2026).",
            "Na extrativa, o minério de ferro caiu de preço, enquanto o petróleo subiu; a transformação cresceu "
            "menos que o agro em termos relativos.",
            "Lição para conjuntura: separe sempre " + azb("efeito preço") + " e " + azb("efeito quantidade") + " — "
            "a Secex divulga os índices de preço e de volume das exportações.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de dado conjuntural que cobra a decomposição preço × "
                       "quantidade. A armadilha seria afirmar que o aumento foi “exclusivamente” de preços, ou "
                       "que o volume caiu por causa da quebra da soja."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O crescimento das exportações agropecuárias em 2022 decorreu exclusivamente da alta de "
            "preços.”</i> → ERRADO (restrição indevida: o volume também cresceu)",
            "<i>“A China é o principal destino das exportações do agronegócio brasileiro.”</i> → CERTO ⏳ "
            "(out/2026)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["também"], "dificuldade": 2,
        "comentario_fonte": ("Alta de preços das commodities agrícolas em 2022 (guerra na Ucrânia) e aumento do "
                             "volume exportado de milho, soja, carnes e açúcar; maior crescimento entre os setores."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: totais de 2022 (exportações ~US$ 335 bi; saldo ~US$ 60 bi) em ordem de "
                    "grandeza; a fonte afirmava alta de volume da soja, que caiu em 2022 — substituída pelo milho"],
    },
    # ------------------------------------------------------------------ E1-0934
    {
        "id": "ECO-E1-0934-1", "fonte_ref": "E1-0934", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2017, "cacd": False,
        "errei": False,
        "comando": CMD_PAUTA,
        "rotulo_item": "Item",
        "assertiva": ("No Brasil, apesar de décadas de tentativas de aumento da participação industrial nas "
                      "exportações, commodities ainda têm importância para a pauta de exportações, com o aumento, "
                      "em anos recentes, da relevância de países asiáticos como destinatários de produtos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No Brasil, apesar de décadas de tentativas de aumento da participação industrial nas "
                      "exportações, commodities ainda têm importância para a pauta de exportações, com o aumento, em "
                      "anos recentes, da relevância de <u>países asiáticos</u> como destinatários de produtos."),
        "poucas": ("A pauta brasileira segue ancorada em " + azb("commodities") + " (soja, minério, petróleo, "
                   "carnes) e, desde os anos 2000, a " + azb("Ásia") + " — sobretudo a China, principal destino "
                   "desde " + vd("2009") + " — ganhou peso como compradora."),
        "destrinchando": [
            "Trajetória: a industrialização por substituição de importações e a promoção de exportações dos anos "
            "1970 elevaram os manufaturados até cerca de metade da pauta nos anos 1980–90. Com o "
            + azb("superciclo de commodities") + " (2003–2011), os " + azb("produtos básicos") + " voltaram a "
            "superar os manufaturados (a partir de " + vd("2010") + ").",
            "Destinos: a " + rx("China") + " tornou-se o maior comprador do Brasil em " + vd("2009") + ", "
            "superando os EUA, e hoje absorve cerca de " + vd("30%") + " das exportações ⏳ (out/2026), "
            "concentradas em soja, minério de ferro, petróleo e carnes.",
            "Leitura crítica: a combinação “pauta primária + destino asiático” é chamada de "
            + azb("reprimarização") + " ou especialização regressiva — expõe a balança aos ciclos de preços e à "
            "demanda chinesa e reforça o debate sobre doença holandesa e desindustrialização.",
            "Contraponto: o agro brasileiro é intensivo em tecnologia (Embrapa, ganhos de produtividade), e a "
            "pauta para a América do Sul e os EUA continua majoritariamente industrial.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Afirmação qualitativa e prudente "
                       "(“ainda têm importância”, “aumento da relevância”), difícil de derrubar. Seria ERRADO se "
                       "dissesse que os manufaturados voltaram a liderar a pauta ou que a UE superou a Ásia como "
                       "destino."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Desde 2009, a China é o principal destino das exportações brasileiras.”</i> → CERTO ⏳ "
            "(out/2026)",
            "<i>“Na última década, os manufaturados voltaram a responder pela maior parte das exportações "
            "brasileiras.”</i> → ERRADO (inversão: predominam os básicos)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["ainda", "em anos recentes"],
        "dificuldade": 1,
        "comentario_fonte": ("Processo conhecido como “especialização regressiva”, nocivo ao desenvolvimento e que "
                             "deixa a estabilidade comercial à mercê dos ciclos de preços das commodities."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: participação da China (~30%) em ordem de grandeza"],
    },
    # ------------------------------------------------------------------ E1-0966
    {
        "id": "ECO-E1-0966-1", "fonte_ref": "E1-0966", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": True,
        "comando": CMD_PAUTA,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a classificação oficialmente adotada, as exportações brasileiras por fator "
                      "agregado são decrescentes, ou seja, da maior para a menor proporção de valor agregado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a classificação oficialmente adotada, as exportações brasileiras por fator "
                       "agregado são ") + vm("decrescentes, ou seja, da maior para a menor") + az(" proporção de "
                                                                                                 "valor agregado.")),
        "poucas": ("A classificação por " + azb("fator agregado") + " vai do menor ao maior grau de elaboração: "
                   + azb("básicos → semimanufaturados → manufaturados") + " — ordem crescente."),
        "condicionais": [("⏳ Desatualizado (out/2026)",
                          "a Secex passou a divulgar a balança comercial sobretudo pela classificação por setor "
                          "(ISIC: agropecuária, indústria extrativa, indústria de transformação); a divisão por "
                          "fator agregado continua útil para séries históricas e é a que o item cobra.")],
        "destrinchando": [
            azb("Básicos") + ": bens de baixo valor agregado, próximos do estado natural (minério de ferro, soja "
            "em grão, café em grão, carne <i>in natura</i>, petróleo bruto).",
            azb("Semimanufaturados") + ": passaram por alguma transformação, mas ainda são insumos (açúcar "
            "bruto, celulose, ferro-gusa, couro, óleo de soja em bruto).",
            azb("Manufaturados") + ": maior grau de elaboração (aviões, automóveis, máquinas, etanol, suco de "
            "laranja, açúcar refinado). Somados aos semimanufaturados, formam os " + azb("industrializados") + "; "
            "há ainda as " + azb("operações especiais") + " (consumo de bordo, reexportação).",
            "Na época do item (" + vd("2013") + "), os básicos já eram o maior grupo — perto de metade da pauta — "
            "e os manufaturados haviam caído para menos de 40%, inversão iniciada em " + vd("2010") + ".",
            vm("Regra-âncora: fator agregado em ordem crescente: básicos &lt; semimanufaturados &lt; manufaturados."),
        ],
        "dissecando": (cz("[inversão]") + " Troca a ordem da classificação. O “ou seja” dá uma definição "
                       "aparentemente didática que reforça o erro. Lembre que a lista oficial começa pelos "
                       "básicos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na classificação por fator agregado, o açúcar bruto e a celulose são semimanufaturados.”</i> → "
            "CERTO",
            "<i>“Desde 2010, os manufaturados representam a maior parcela das exportações brasileiras por fator "
            "agregado.”</i> → ERRADO (inversão: os básicos passaram à frente)",
        ])],
        "reescrita": ("De acordo com a classificação oficialmente adotada, as exportações brasileiras por fator "
                      "agregado são " + hl("crescentes, ou seja, da menor para a maior") + " proporção de valor "
                      "agregado."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Classificação de maior a menor valor adicionado, com manufaturados primeiro e básicos "
                             "depois (minérios, grãos, carne in natura)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário da fonte dizia que a classificação vai do maior ao menor valor "
                    "agregado, o que contradiz o próprio gabarito; corrigido para a ordem oficial crescente",
                    "dado_aproximado: participações de 2013 (básicos perto de metade; manufaturados abaixo de 40%)"],
    },
    # ------------------------------------------------------------------ E1-0967
    {
        "id": "ECO-E1-0967-1", "fonte_ref": "E1-0967", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_PAUTA,
        "rotulo_item": "Item",
        "assertiva": ("O Brasil apresentou superávit em 2013, tendo havido déficit na maioria dos meses do ano, com "
                      "reversão do saldo negativo a partir do começo do 2.º semestre."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Brasil apresentou superávit em 2013, tendo havido déficit na ") + vm("maioria")
                    + az(" dos meses do ano") + vm(", com reversão do saldo negativo a partir do começo do 2.º "
                                                   "semestre") + az(".")),
        "poucas": ("O superávit comercial de 2013 (cerca de " + vd("US$ 2,6 bilhões") + ", o menor desde 2000 ⏳ "
                   "(out/2026)) existiu, mas os meses de déficit não foram maioria, e o saldo acumulado só se "
                   "firmou positivo no fim do ano."),
        "destrinchando": [
            "O ano começou muito mal: " + vd("janeiro de 2013") + " teve um dos piores déficits mensais da série "
            "(perto de US$ 4 bilhões), puxado por importações de combustíveis contabilizadas com atraso.",
            "Os déficits mensais se concentraram no primeiro semestre, mas não foram maioria; houve ainda meses "
            "negativos no segundo semestre, e o saldo acumulado do ano só voltou ao azul nos últimos meses, com "
            "exportações fortes de fim de ano — incluindo exportações fictas de " + azb("plataformas de "
            "petróleo") + " pelo regime aduaneiro do Repetro.",
            "Contexto: 2013 marcou a erosão do superávit comercial que vinha desde 2001 — queda dos preços de "
            "commodities, déficit em combustíveis (gasolina e diesel importados com preço interno represado) e "
            "importações de manufaturados elevadas. Em " + vd("2014") + ", a balança fecharia em déficit pela "
            "primeira vez desde 2000 ⏳ (out/2026).",
            "Para julgar itens assim, separe três afirmações: o saldo anual (positivo ✓), a contagem de meses "
            "(maioria? ✗) e o momento da reversão (início do 2.º semestre? ✗).",
        ],
        "dissecando": (cz("[dado alterado · meia-verdade]") + " A primeira oração (superávit em 2013) é "
                       "verdadeira e dá credibilidade ao resto; o erro está na contagem (“maioria dos meses”) e "
                       "no marco temporal da virada. 🔥 Itens de conjuntura antiga empilham detalhes de série "
                       "mensal: basta um falhar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em 2013, o Brasil registrou o menor superávit comercial desde 2000.”</i> → CERTO ⏳ (out/2026)",
            "<i>“Em 2014, a balança comercial brasileira voltou a registrar superávit.”</i> → ERRADO (dado "
            "alterado: houve déficit)",
        ])],
        "reescrita": ("O Brasil apresentou superávit em 2013, tendo havido déficit na " + hl("minoria")
                      + " dos meses do ano" + hl(", concentrados no primeiro semestre, e saldo acumulado positivo "
                                                 "só nos últimos meses") + "."),
        "tipo_erro": ["DADO_ALTERADO", "MEIA_VERDADE"], "moduladores": ["maioria"], "dificuldade": 3,
        "comentario_fonte": ("Superávit consistente a partir do segundo semestre; déficits em 3 meses do primeiro "
                             "semestre de 2013, conforme gráfico (imagem não preservada)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "00045.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem não preservada; série mensal descrita em texto)"}],
        "alertas": ["dado_aproximado: superávit de 2013 (~US$ 2,6 bi), déficit de janeiro (~US$ 4 bi) e "
                    "momento em que o acumulado voltou a ser positivo descritos de memória, sem a série mensal",
                    "figura_irrecuperavel: gráfico do saldo mensal de 2013 (00045.jpeg) não veio na exportação"],
    },
    # ------------------------------------------------------------------ E1-0968
    {
        "id": "ECO-E1-0968-1", "fonte_ref": "E1-0968", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_PAUTA,
        "rotulo_item": "Item",
        "assertiva": ("Ao se examinar a atual pauta de exportações brasileiras por blocos econômicos, constata-se "
                      "que os países do MERCOSUL são grandes importadores do Brasil, somente superados pela Ásia e "
                      "pela União Europeia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Ao se examinar a atual pauta de exportações brasileiras por blocos econômicos, constata-se "
                      "que os países do MERCOSUL são grandes importadores do Brasil, <u>somente superados pela Ásia "
                      "e pela União Europeia</u>."),
        "poucas": ("Na época do item (dados de " + vd("2013") + "), a ordem por blocos era " + azb("Ásia")
                   + " (cerca de um terço) → " + azb("União Europeia") + " (cerca de um quinto) → "
                   + rx("Mercosul") + " (cerca de 11%, puxado pela Argentina) → EUA."),
        "condicionais": [("⏳ Desatualizado (out/2026)",
                          "a ordem mudou: com a China sozinha perto de 30% das exportações e a perda de peso da "
                          "Argentina, o Mercosul caiu para a casa de um dígito e ficou atrás também dos EUA. Hoje "
                          "o item tenderia a ser ERRADO.")],
        "destrinchando": [
            "Para o " + rx("Brasil") + ", o Mercosul sempre foi destino de qualidade: compra sobretudo "
            + azb("manufaturados") + " (automóveis e autopeças, máquinas, químicos), ao contrário da Ásia, que "
            "compra commodities. A Argentina chegou a ser o terceiro maior parceiro individual, atrás de China e "
            "EUA.",
            "A participação do bloco nas exportações brasileiras atingiu o auge no fim dos anos 1990 (perto de "
            + vd("17%") + " em 1998) e encolheu depois, com as crises argentinas, o comércio administrado no "
            "setor automotivo e a ascensão chinesa.",
            "Leitura de pauta por blocos exige atenção ao recorte: “América Latina e Caribe” (que inclui o "
            "Mercosul) é maior que “Mercosul”; “Ásia” inclui China, Japão, Coreia e Índia.",
            "A observação da fonte sobre o peso do Brasil nas pautas dos vizinhos é verdadeira no sentido "
            "inverso: o Brasil é o maior ou um dos maiores fornecedores de Argentina, Paraguai e Uruguai, o que "
            "gera assimetrias e atritos no bloco.",
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item de ranking. O “somente superados” exige saber a "
                       "posição exata: terceiro lugar. A pegadinha mais comum é incluir os EUA à frente — o que "
                       "não valia em 2013, mas passou a valer depois ⏳ (out/2026)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As exportações brasileiras para o Mercosul concentram-se em produtos manufaturados.”</i> → CERTO",
            "<i>“O Mercosul é o principal destino das exportações brasileiras de produtos básicos.”</i> → ERRADO "
            "(troca de ator: é a Ásia, sobretudo a China)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": ["somente"], "dificuldade": 2,
        "comentario_fonte": ("O Brasil é o país latino-americano dominante nas pautas de exportação dos vizinhos, "
                             "posição que gera tensão com os parceiros."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: participações por bloco em 2013 e o pico de 1998 em ordem de grandeza"],
    },
    # ------------------------------------------------------------------ E1-0969
    {
        "id": "ECO-E1-0969-1", "fonte_ref": "E1-0969", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2014, "cacd": False,
        "errei": False,
        "comando": CMD_PAUTA,
        "rotulo_item": "Item",
        "assertiva": ("As importações brasileiras são constituídas por numerosos grupos de produtos, destacando-se "
                      "óleos brutos de petróleo, com menos de 10% do total."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As importações brasileiras são constituídas por numerosos grupos de produtos, destacando-se "
                      "óleos brutos de petróleo, com <u>menos de 10%</u> do total."),
        "poucas": ("A pauta de importações brasileira é " + azb("diversificada") + " (insumos, bens de capital, "
                   "combustíveis); o petróleo bruto era o principal item individual, mas com cerca de " + vd("7%")
                   + " do total em 2013 ⏳ (out/2026)."),
        "destrinchando": [
            "Por categoria de uso, as importações brasileiras se dividem em " + azb("bens intermediários") + " "
            "(o maior grupo, mais da metade), " + azb("bens de capital") + ", " + azb("bens de consumo") + " e "
            + azb("combustíveis e lubrificantes") + ". Dependência de insumos importados é traço estrutural da "
            "indústria brasileira.",
            "Em " + vd("2013") + ", o país importou cerca de US$ 16 bilhões em petróleo bruto, perto de "
            + vd("7%") + " de importações totais de cerca de US$ 240 bilhões ⏳ (out/2026) — item individual "
            "relevante, mas abaixo de 10%.",
            "Comparação histórica: após os choques de 1973 e 1979, o petróleo chegou a responder por " + vd("perto "
            "da metade") + " das importações brasileiras no início dos anos 1980 — um dos motores da crise da "
            "dívida. A autossuficiência foi buscada com Proálcool, Bacia de Campos e, depois, o pré-sal.",
            "Hoje ⏳ (out/2026) o quadro se inverteu: com o pré-sal, o " + rx("Brasil") + " é grande "
            + azb("exportador líquido de petróleo bruto") + " — que passou a disputar com a soja o posto de "
            "principal produto da pauta de exportação —, mas segue importando derivados (diesel, gasolina, "
            "nafta) por limitação de refino.",
        ],
        "dissecando": (cz("[detalhe]") + " Item de ordem de grandeza: o candidato sabe que o petróleo pesa na "
                       "pauta e tende a superestimar. O limiar “menos de 10%” é o ponto decisivo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os bens intermediários constituem a maior parte das importações brasileiras por categoria de "
            "uso.”</i> → CERTO",
            "<i>“O Brasil é hoje importador líquido de petróleo bruto.”</i> ⏳ (out/2026) → ERRADO (inversão: com o "
            "pré-sal, é exportador líquido)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["menos de 10%"], "dificuldade": 2,
        "comentario_fonte": ("O petróleo representa, em média, 8% da pauta de importações; no fim dos anos 1970, "
                             "após o choque do petróleo, chegou a 80% do valor importado."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: a fonte dizia que o petróleo chegou a 80% das importações no fim dos anos "
                    "1970; o pico foi perto da metade, no início dos anos 1980",
                    "dado_aproximado: valores de 2013 (petróleo bruto ~US$ 16 bi; total ~US$ 240 bi) em ordem de "
                    "grandeza"],
    },
    # ------------------------------------------------------------------ E1-0983
    {
        "id": "ECO-E1-0983-1", "fonte_ref": "E1-0983", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Prof. Daniel (Telegram Economia CACD)", "prova": "", "ano": 2022,
        "cacd": False, "errei": False,
        "comando": "Acerca da política comercial brasileira recente, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Nesse ano de 2022, a Câmara de Comércio Exterior (Camex) tentou aprovar a redução do Imposto "
                      "de Importação, via inclusão na Lista de Exceções à Tarifa Externa Comum do Mercosul (Letec), "
                      "para insumos industriais como glifosato e resinas plásticas, mas tal tentativa fracassou por "
                      "violar as regras do bloco. Reduções nas tarifas de importação possuem a capacidade de reduzir "
                      "os custos dos insumos importados, abrindo espaço para uma inflação menor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nesse ano de 2022, a Câmara de Comércio Exterior (Camex) ") + vm("tentou aprovar")
                    + az(" a redução do Imposto de Importação, via inclusão na Lista de Exceções à Tarifa Externa "
                         "Comum do Mercosul (Letec), para insumos industriais como glifosato e resinas plásticas")
                    + vm(", mas tal tentativa fracassou por violar as regras do bloco") + az(". Reduções nas tarifas "
                    "de importação possuem a capacidade de reduzir os custos dos insumos importados, abrindo espaço "
                    "para uma inflação menor.")),
        "poucas": ("A Camex (pelo Gecex) " + azb("efetivamente reduziu") + " o Imposto de Importação de insumos "
                   "industriais em 2022, usando a " + azb("Letec") + " — instrumento previsto pelas próprias "
                   "normas do Mercosul. A segunda frase (tarifa menor → custo menor → inflação menor) está certa."),
        "destrinchando": [
            "A " + azb("Letec") + " (Lista Nacional de Exceções à TEC) é uma lista de códigos NCM, em número "
            "limitado e autorizado pelo Mercosul, nos quais cada sócio pode aplicar alíquota diferente da TEC. "
            "Usá-la é cumprir, e não violar, as regras do bloco. Há também a lista de " + azb("desabastecimento")
            + " e o regime de " + azb("ex-tarifários") + " para bens de capital e informática.",
            "Em 2021–2022 ⏳ (out/2026), em meio à alta da inflação, o governo reduziu tarifas em várias rodadas: "
            "corte linear de " + vd("10%") + " em novembro de 2021, novo corte de " + vd("10%") + " em maio de "
            "2022 (temporário, até o fim de 2023) e reduções pontuais para insumos industriais e alimentos, "
            "incluindo inclusões na Letec. Em julho de 2022, o Mercosul aprovou redução de " + vd("10%") + " da "
            "própria TEC para a maior parte do universo tarifário.",
            "Canal inflacionário: tarifa menor reduz o preço interno de importados e de insumos, diminui custos de "
            "produção e aumenta a concorrência — efeito " + azb("desinflacionário") + ", em geral pontual (nível "
            "de preços), não permanente sobre a taxa de inflação.",
            "Pano de fundo: a TEC média do Mercosul é alta para padrões internacionais, e o " + rx("Brasil")
            + " defendia sua redução; Argentina resistia, e o Uruguai pressionava por flexibilizar acordos "
            "extrabloco.",
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " O item narra um fracasso que não houve e, em seguida, "
                       "acerta o mecanismo econômico. Pista: Letec é instrumento <b>do próprio</b> Mercosul — "
                       "usá-la não pode “violar as regras do bloco”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A Letec permite que cada membro do Mercosul aplique, em número limitado de produtos, alíquotas "
            "de importação diferentes da TEC.”</i> → CERTO",
            "<i>“A redução de tarifas de importação tende a pressionar a inflação para cima, por aumentar a "
            "demanda por importados.”</i> → ERRADO (inversão: barateia importados e insumos)",
        ])],
        "reescrita": ("Nesse ano de 2022, a Câmara de Comércio Exterior (Camex) " + hl("aprovou") + " a redução do "
                      "Imposto de Importação, via inclusão na Lista de Exceções à Tarifa Externa Comum do Mercosul "
                      "(Letec), para insumos industriais como glifosato e resinas plásticas"
                      + hl(", instrumento previsto pelas regras do bloco") + ". Reduções nas tarifas de importação "
                      "possuem a capacidade de reduzir os custos dos insumos importados, abrindo espaço para uma "
                      "inflação menor."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("O Brasil efetivamente reduziu esse imposto (Gecex reduz tarifas de importação de "
                             "insumos industriais, ago/2022); cortes de 10% em nov/2021 (permanente) e mai/2022 "
                             "(até o fim de 2023)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “resinas plástiva” → “resinas plásticas”",
                    "dado_aproximado: cronologia dos cortes tarifários de 2021–2022 resumida de memória"],
    },
    # ------------------------------------------------------------------ E2-L00349
    {
        "id": "ECO-E2-L00349-1", "fonte_ref": "E2-L00349", "destino": "83", "subtema": H2["conj"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Acerca da política monetária brasileira recente, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Entre 2021 e 2025, a contração monetária elevou a Selic do piso histórico a patamar de dois "
                      "dígitos, ancorando expectativas e produzindo convergência do IPCA para a meta projetada (3,8% "
                      "em 2025). Tais ganhos ocorreram sem custos relevantes sobre crédito e investimento, dada a "
                      "rápida normalização global."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Entre 2021 e 2025, a contração monetária elevou a Selic do piso histórico a patamar de dois "
                       "dígitos, ancorando expectativas e produzindo convergência do IPCA para a meta projetada (3,8% "
                       "em 2025). Tais ganhos ") + vm("ocorreram sem custos relevantes") + az(" sobre crédito e "
                                                                                             "investimento")
                    + vm(", dada a rápida normalização global") + az(".")),
        "poucas": ("Juros reais entre os mais altos do mundo têm " + azb("custo") + ": crédito mais caro e "
                   "escasso, investimento contido, endividamento e inadimplência. E a normalização monetária "
                   "global foi lenta e desigual ⏳ (out/2026)."),
        "destrinchando": [
            "Trajetória da Selic ⏳ (out/2026): piso histórico de " + vd("2%") + " (agosto de 2020 a março de "
            "2021) → alta até " + vd("13,75%") + " (agosto de 2022) → cortes até " + vd("10,50%") + " (maio de "
            "2024) → novo ciclo de alta até " + vd("15%") + " (junho de 2025), maior nível desde 2006.",
            "Mecanismo de transmissão: juro básico ↑ → custo do crédito ↑ e concessões ↓ → consumo e "
            "investimento ↓ → hiato do produto negativo → inflação ↓. O " + azb("custo") + " em atividade é "
            "parte do canal, não um efeito colateral evitável: a política monetária desinflaciona justamente "
            "esfriando a demanda.",
            "Custos observados ⏳ (out/2026): juro real ex-ante perto de 10% ao ano, desaceleração do crédito "
            "livre, alta da inadimplência e do comprometimento de renda das famílias, encarecimento da dívida "
            "pública (maior despesa com juros) e investimento produtivo contido.",
            "Exterior: o Fed só iniciou cortes em setembro de 2024 e manteve juros altos por longo período; a "
            "normalização foi heterogênea entre países, e o dólar forte pressionou moedas emergentes — nada de "
            "“rápida normalização global” que poupasse a economia brasileira.",
            "A primeira frase é generosa — as expectativas chegaram a se desancorar em 2024–2025, e o IPCA de "
            "2025 voltou ao intervalo de tolerância, mas acima do centro da meta de " + vd("3%") + " (meta "
            "contínua desde 2025, com tolerância de 1,5 ponto) ⏳ (out/2026) —, porém o gabarito se decide na "
            "segunda.",
        ],
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " A primeira frase narra fatos conhecidos (Selic de "
                       "2% a dois dígitos) para ganhar credibilidade; o erro está na segunda: “sem custos "
                       "relevantes” contraria o próprio mecanismo de transmissão, e a justificativa (“rápida "
                       "normalização global”) é falsa. Desconfie de política monetária contracionista “sem "
                       "custos”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O ciclo de aperto monetário iniciado em 2021 elevou a Selic do piso histórico de 2% para "
            "13,75% em 2022.”</i> → CERTO ⏳ (out/2026)",
            "<i>“A política monetária contracionista reduz a inflação sem afetar o nível de atividade no curto "
            "prazo.”</i> → ERRADO (o canal passa justamente pela demanda)",
        ])],
        "reescrita": ("Entre 2021 e 2025, a contração monetária elevou a Selic do piso histórico a patamar de dois "
                      "dígitos, ancorando expectativas e produzindo convergência do IPCA para a meta projetada (3,8% "
                      "em 2025). Tais ganhos " + hl("tiveram custos relevantes") + " sobre crédito e investimento"
                      + hl(", num cenário de normalização global lenta e heterogênea") + "."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": ["sem custos relevantes"],
        "dificuldade": 1,
        "comentario_fonte": ("Houve custos relevantes (crédito/investimento) e riscos institucionais; a "
                             "normalização global foi heterogênea."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: a primeira frase (ancoragem e convergência a 3,8% em 2025) também é discutível; "
                    "mantida em azul por o gabarito se apoiar na segunda frase"],
    },
]
