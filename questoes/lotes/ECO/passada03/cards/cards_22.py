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
]
