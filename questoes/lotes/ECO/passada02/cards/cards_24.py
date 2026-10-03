"""Cards do lote de redação 24 — ECO, passada 02 (notas 47 e 48: política fiscal, equivalência ricardiana,
déficit e dívida públicos, Laffer)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "ric": "🔮 Equivalência ricardiana",
    "pf": "📊 Política fiscal e multiplicadores",
    "conc": "📏 Conceitos de déficit e dívida",
    "fin": "🧮 Financiamento e sustentabilidade",
    "laf": "📈 Wagner e Laffer",
}

CMD_NIDI_JUL = ("Sobre os conceitos pertencentes ao ramo da Economia que se dedica ao estudo do Setor Público e seu "
                "orçamento e sobre o princípio da Equivalência Ricardiana, julgue o item a seguir.")

CMD_NIDI_ABR = "Acerca dos indicadores orçamentários e da equivalência ricardiana, julgue o item a seguir."

CMD_NIDI_NOV = ("A análise das contas públicas é um elemento importante da macroeconomia. A esse respeito, julgue o "
                "item a seguir.")

CMD_CLIP = ("A política fiscal é instrumento central para o equilíbrio macroeconômico e a sustentabilidade da dívida "
            "pública. Com base nisso, julgue o item a seguir.")

CMD_LAFFER = "Acerca da curva de Laffer e da relação entre alíquotas e arrecadação, julgue o item a seguir."

CMD_BOZAN_MED = ("Julgue o item a respeito da medição do desempenho fiscal do governo no contexto da economia do "
                 "setor público.")

CMD_BOZAN_APR = ("Sobre a apresentação das contas do governo e os diferentes conceitos relacionados ao déficit e à "
                 "dívida pública, julgue o item a seguir.")

CMD_RT = "A respeito da política fiscal e da dívida pública, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E3-L00074
    {
        "id": "ECO-E3-L00074-1", "fonte_ref": "E3-L00074", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a Equivalência Ricardiana, o financiamento do déficit fiscal por meio do aumento da "
                      "arrecadação ou por meio do aumento da dívida pública são equivalentes para os consumidores. "
                      "Portanto, o consumo privado no presente e o nível de atividade econômica não se alteram."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a Equivalência Ricardiana, o financiamento do déficit fiscal por meio do aumento da "
                      "arrecadação ou por meio do aumento da dívida pública são <u>equivalentes para os "
                      "consumidores</u>. Portanto, o consumo privado <u>no presente</u> e o nível de atividade "
                      "econômica não se alteram."),
        "poucas": ("Na " + azb("equivalência ricardiana") + ", dívida hoje = impostos amanhã: o consumidor racional "
                   "poupa todo o alívio tributário presente, e consumo e produto não mudam — <b>já no presente</b>, "
                   "não só no longo prazo."),
        "destrinchando": [
            "Ideia levantada por " + oc("David Ricardo") + " (que, aliás, duvidava de sua validade prática) e "
            "formalizada por " + oc("Robert Barro") + " em " + vd("1974") + " (<i>Are Government Bonds Net "
            "Wealth?</i>): para um dado caminho de gastos públicos, trocar imposto presente por dívida não altera "
            "a riqueza das famílias, porque o valor presente dos impostos futuros necessários para pagar a dívida "
            "é exatamente igual ao corte de hoje.",
            "Mecanismo: o governo corta T hoje e emite títulos → a " + azb("poupança pública") + " cai → as "
            "famílias, antevendo T maior amanhã, elevam a " + azb("poupança privada") + " no mesmo montante → a "
            "poupança nacional, os juros, o consumo e a demanda agregada ficam onde estavam.",
            "Em dois períodos: C₁ + C₂/(1 + r) = Y₁ − T₁ + (Y₂ − T₂)/(1 + r). Se T₁ cai em Δ e T₂ sobe em "
            "Δ(1 + r), o lado direito não muda — logo o consumo ótimo de hoje também não.",
            "Por que “no presente”? O ajuste é <b>imediato</b>: o agente ricardiano reage no momento do anúncio, "
            "porque calcula o valor presente da conta futura. A ideia de “efeito no curto prazo e neutralidade "
            "no longo” é a leitura keynesiana, não a ricardiana.",
            "Hipóteses (e as críticas de cada uma): racionalidade e previsão perfeita (miopia), horizonte "
            "infinito via altruísmo entre gerações (vida finita), mercado de crédito perfeito (restrição de "
            "liquidez), impostos " + azb("lump-sum") + " (impostos distorcivos).",
            vm("Regra-âncora: a equivalência fala da FORMA de financiar um gasto dado; o ajuste se dá todo na "
               "poupança privada."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O item reproduz a definição do teorema. A "
                       "armadilha está em “no presente”: quem raciocina com o modelo keynesiano (efeito de curto "
                       "prazo, neutralidade só no longo) marca ERRADO. Em item sobre a teoria, julgue pela teoria, "
                       "não pela evidência empírica contra ela."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a equivalência ricardiana, o corte de impostos financiado por dívida eleva o consumo no "
            "curto prazo, mas não no longo prazo.”</i> → ERRADO (leitura keynesiana: na teoria o efeito é nulo "
            "desde já)",
            "<i>“Pela equivalência ricardiana, um déficit financiado por dívida eleva a poupança privada no mesmo "
            "montante da queda da poupança pública.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Dívida é vista como impostos futuros; consumidores poupam o ganho presente, e consumo "
                             "e PIB não se alteram. Discussão sobre o “no presente”: na teoria pura, a neutralidade "
                             "é imediata; o efeito de curto prazo é a leitura keynesiana."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 21-25", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (ilegíveis ou repetiam o comentário; conteúdo absorvido no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00210-1 e ECO-E3-L00384-1 (mesma tese, outras provas)",
                    "nota_redacao: dados empíricos atribuídos pelas respostas de IA do verso (estudos, "
                    "percentuais) foram descartados por não serem verificáveis"],
    },
    # ------------------------------------------------------------------ E3-L00075
    {
        "id": "ECO-E3-L00075-1", "fonte_ref": "E3-L00075", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_JUL,
        "rotulo_item": "Item",
        "assertiva": ("A existência de indivíduos sem acesso ao mercado de crédito é um dos motivos apontados para a "
                      "violação da hipótese da Equivalência Ricardiana."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A existência de indivíduos <u>sem acesso ao mercado de crédito</u> é <u>um dos</u> motivos "
                      "apontados para a violação da hipótese da Equivalência Ricardiana."),
        "poucas": ("A equivalência supõe que todos podem poupar e tomar emprestado à mesma taxa. Quem sofre "
                   + azb("restrição de liquidez") + " gasta o alívio tributário de hoje — e a neutralidade "
                   "ricardiana cai."),
        "destrinchando": [
            "A neutralidade depende de as famílias " + azb("suavizarem o consumo") + " ao longo do tempo: "
            "poupam quando a renda de hoje sobe sem mudar a riqueza e se endividam quando ela cai.",
            "Política <b>expansionista</b> (corte de impostos com dívida): o indivíduo sem crédito, que já queria "
            "consumir mais e não conseguia, usa o dinheiro extra para consumir agora → C ↑, demanda agregada ↑. "
            "O corte funciona para ele como um empréstimo que o mercado lhe negava.",
            "Política <b>contracionista</b> (alta de impostos para reduzir dívida): o ricardiano manteria o "
            "consumo sacando poupança ou tomando crédito; quem não tem nem uma coisa nem outra é obrigado a "
            "cortar o consumo.",
            "Outros motivos clássicos de violação: " + azb("miopia") + " (agentes que não calculam a conta "
            "futura), " + azb("horizonte finito") + " (impostos que cairão sobre quem não tem herdeiros com quem "
            "se importe), " + azb("impostos distorcivos") + " (o imposto futuro muda incentivos) e incerteza "
            "sobre quem pagará e quando.",
            "Consequência de política: quanto maior a fração de famílias com restrição de crédito — típica de "
            "economias emergentes —, maior o " + azb("multiplicador") + " de transferências e cortes de "
            "impostos voltados à baixa renda.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz a crítica-padrão dos manuais. O "
                       "“um dos motivos” protege o item: não diz que é o único. Itens sobre hipóteses da "
                       "equivalência costumam trocar a restrição de crédito por algo que <b>reforça</b> a teoria "
                       "(altruísmo intergeracional, por exemplo)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O altruísmo intergeracional, que leva os pais a deixarem heranças, é um dos motivos apontados "
            "para a violação da equivalência ricardiana.”</i> → ERRADO (inversão: é hipótese que a sustenta)",
            "<i>“A restrição de crédito é o único motivo apontado para a violação da equivalência.”</i> → ERRADO "
            "(restrição indevida: há miopia, vida finita, impostos distorcivos)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["um dos"], "dificuldade": 1,
        "comentario_fonte": ("Restrição de liquidez impede a suavização do consumo: o corte de impostos é gasto "
                             "e a equivalência é violada."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00209
    {
        "id": "ECO-E3-L00209-1", "fonte_ref": "E3-L00209", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o princípio da Equivalência Ricardiana, um aumento do déficit orçamentário "
                      "corrente do governo promove uma elevação do nível de atividade econômica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o princípio da Equivalência Ricardiana, um aumento do déficit orçamentário "
                       "corrente do governo ") + vm("promove uma elevação do") + az(" nível de atividade "
                                                                                    "econômica.")),
        "poucas": ("Na " + azb("equivalência ricardiana") + " o déficit é neutro: o corte de impostos que o gera "
                   "é integralmente poupado para pagar os impostos futuros, e consumo e produto <b>não se "
                   "alteram</b>."),
        "destrinchando": [
            "Roteiro do teorema: impostos ↓ hoje → déficit ↑ (poupança pública ↓) → renda disponível ↑ → "
            "famílias racionais sabem que o governo terá de elevar impostos no futuro para honrar a dívida → "
            "poupam todo o acréscimo de renda → " + vd("C, DA e Y inalterados") + ".",
            "A poupança nacional (pública + privada) não muda, porque a privada sobe exatamente o que a pública "
            "cai. Por isso, além do produto, também os juros e o investimento ficam onde estavam: não há nem "
            "estímulo nem " + azb("crowding out") + ".",
            "Contraste com o modelo keynesiano: lá o consumo depende da renda disponível <b>corrente</b>, e o "
            "mesmo déficit ativa o " + azb("multiplicador") + " — Y sobe. A equivalência ricardiana é justamente "
            "a negação desse canal.",
            "O item seria verdadeiro se trocasse o referencial teórico (“De acordo com o modelo keynesiano "
            "simples…”) ou se as hipóteses ricardianas falhassem (restrição de crédito, miopia, vida finita).",
            vm("Regra-âncora: ricardiano → déficit neutro; keynesiano → déficit expansionista."),
        ],
        "dissecando": (cz("[troca de conceito · contradição]") + " O item atribui à equivalência ricardiana a "
                       "conclusão da escola rival. A pista é o próprio nome do princípio: “equivalência” entre "
                       "imposto e dívida significa que a escolha do déficit não muda nada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com a equivalência ricardiana, um aumento do déficit orçamentário corrente eleva a "
            "poupança privada.”</i> → CERTO",
            "<i>“De acordo com a equivalência ricardiana, um aumento do déficit eleva a taxa de juros e reduz o "
            "investimento privado.”</i> → ERRADO (troca de conceito: isso é crowding out)",
        ])],
        "reescrita": ("De acordo com o princípio da Equivalência Ricardiana, um aumento do déficit orçamentário "
                      "corrente do governo " + hl("não altera o") + " nível de atividade econômica."),
        "tipo_erro": ["TROCA_CONCEITO", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("O déficit não afeta o nível de atividade: os agentes poupam o rendimento extra para "
                             "pagar o imposto futuro; consumo e demanda agregada ficam inalterados."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 301", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (reproduzia o enunciado, com OCR ruim)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00210
    {
        "id": "ECO-E3-L00210-1", "fonte_ref": "E3-L00210", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_ABR,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o princípio da Equivalência Ricardiana, a forma pela qual o governo financia "
                      "seus gastos, impostos ou empréstimos, não tem efeito sobre o produto da economia."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o princípio da Equivalência Ricardiana, <u>a forma pela qual</u> o governo "
                      "financia seus gastos, impostos ou empréstimos, não tem efeito sobre o produto da economia."),
        "poucas": ("É o enunciado do teorema: dado o gasto, financiá-lo com " + azb("imposto hoje") + " ou com "
                   + azb("dívida") + " (imposto amanhã) dá no mesmo — consumo, demanda agregada e produto não "
                   "mudam."),
        "destrinchando": [
            "Objeto preciso da equivalência: a " + azb("composição do financiamento") + " de um caminho de "
            "gastos públicos <b>dado</b>. Ela não diz que o gasto público é irrelevante; diz que, para um mesmo "
            "G, tanto faz T agora ou T depois.",
            "Por quê: a restrição orçamentária intertemporal do governo obriga o valor presente dos impostos a "
            "cobrir o valor presente dos gastos. Mudar o calendário dos impostos não muda esse valor presente — "
            "logo não muda a riqueza das famílias que, com " + azb("expectativas racionais") + ", o "
            "internalizam.",
            "Encadeamento: consumo inalterado → demanda agregada inalterada → " + vd("produto inalterado") + ". "
            "A única variável que se mexe é a composição da poupança (pública ↓, privada ↑).",
            "Formulação moderna de " + oc("Robert Barro") + " (" + vd("1974") + "), sobre ideia de "
            + oc("David Ricardo") + ". As hipóteses — crédito perfeito, horizonte infinito, impostos lump-sum, "
            "previsão perfeita — raramente valem por inteiro; por isso a evidência costuma encontrar "
            "equivalência apenas parcial.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Definição do manual com outras palavras. O que "
                       "decide é “a forma pela qual… financia”: o item fala do financiamento, não do tamanho do "
                       "gasto. A banca costuma errar a versão que diz que o <b>gasto</b> é neutro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com a equivalência ricardiana, um aumento dos gastos do governo não tem efeito sobre o "
            "produto, qualquer que seja a forma de financiamento.”</i> → ERRADO (extrapolação: o teorema trata "
            "da forma de financiar um gasto dado)",
            "<i>“Segundo a equivalência ricardiana, a substituição de impostos correntes por dívida eleva a "
            "poupança privada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Enunciado do teorema: sob mercados perfeitos e impostos lump-sum, é indiferente "
                             "financiar com imposto agora ou dívida; consumo e PIB não mudam."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 302", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖"}],
        "alertas": ["quase_duplicata: ECO-E3-L00074-1 e ECO-E3-L00384-1 (mesma tese)"],
    },
    # ------------------------------------------------------------------ E3-L00277
    {
        "id": "ECO-E3-L00277-1", "fonte_ref": "E3-L00277", "destino": "47", "subtema": H2["pf"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": "Julgue o item a seguir, relativo às proposições de política econômica keynesiana.",
        "excerto": ("<p>Na década de 30, durante a Grande Depressão, a teoria econômica debatia, entre outros "
                    "temas [...]</p>"),
        "rotulo_item": "Item",
        "assertiva": ("Para um quadro de crise, uma proposição de política econômica keynesiana seria o governo "
                      "ampliar os gastos públicos como forma de elevar a demanda agregada e recuperar o nível de "
                      "emprego, para que, ao passo para um momento de superaquecimento, a recomendação keynesiana "
                      "seria reduzir gastos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Para um quadro de crise, uma proposição de política econômica keynesiana seria o governo "
                      "<u>ampliar os gastos públicos</u> como forma de elevar a demanda agregada e recuperar o nível "
                      "de emprego, para que, ao passo para um momento de superaquecimento, a recomendação "
                      "keynesiana seria <u>reduzir gastos</u>."),
        "poucas": ("É a " + azb("política fiscal anticíclica") + ": gastar mais (ou tributar menos) na recessão "
                   "para sustentar a demanda e o emprego, e retirar o estímulo no superaquecimento para conter a "
                   "inflação."),
        "destrinchando": [
            "Diagnóstico de " + oc("Keynes") + " (<i>Teoria Geral</i>, " + vd("1936") + "): o nível de emprego é "
            "determinado pela " + azb("demanda efetiva") + "; na depressão, a demanda privada (sobretudo o "
            "investimento, movido por expectativas) desaba, e não há força automática que traga o pleno "
            "emprego de volta.",
            "Na crise (" + azb("hiato recessivo") + "): G ↑ ou T ↓ eleva a demanda agregada DA = C + I + G + "
            "X − M; pelo " + azb("multiplicador") + " 1/(1 − c), cada real de gasto gera mais de um real de "
            "renda. Déficit, aqui, é instrumento, não problema.",
            "No superaquecimento (" + azb("hiato inflacionário") + "): G ↓ ou T ↑ retira demanda, contém preços "
            "e gera superávits que compensam os déficits da fase ruim. É a simetria que distingue o "
            "keynesianismo da defesa de déficit permanente.",
            "Dois modos de agir: " + azb("estabilizadores automáticos") + " (seguro-desemprego, imposto de "
            "renda progressivo, que se movem sozinhos com o ciclo) e política " + azb("discricionária")
            + " (decisões novas de gasto ou de alíquota).",
            "A sistematização da regra “déficit na recessão, superávit no boom” deve muito a "
            + oc("Abba Lerner") + " (finanças funcionais) e aos keynesianos do pós-guerra; Keynes enfatizou "
            "sobretudo o estímulo na depressão e a crítica à austeridade prematura.",
        ],
        "dissecando": (cz("[literalidade]") + " Descrição correta da política contracíclica, apesar da redação "
                       "truncada (“para que, ao passo para…”). O risco é o candidato achar que keynesiano "
                       "“sempre gasta” e estranhar a recomendação de cortar no boom — o keynesianismo é "
                       "anticíclico, não pró-déficit em qualquer fase."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para a abordagem keynesiana, a ampliação dos gastos públicos é recomendável em qualquer fase do "
            "ciclo econômico.”</i> → ERRADO (modulador absoluto: no superaquecimento recomenda-se contração)",
            "<i>“Na recessão, a recomendação keynesiana seria cortar gastos para restaurar a confiança dos "
            "investidores.”</i> → ERRADO (inversão: é a tese da austeridade expansionista, não a keynesiana)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Política fiscal anticíclica: gasto na recessão para elevar a demanda e o emprego; "
                             "redução de gastos/aumento de impostos no superaquecimento. PIB = C + I + G + X − M."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 383", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (identidade DA = C + I + G + X − M no 📖)"}],
        "alertas": ["texto_parcial: o texto-base da questão 61 veio truncado na fonte (“…entre outros tema…”); "
                    "comando neutro e excerto parcial"],
    },
    # ------------------------------------------------------------------ E3-L00384
    {
        "id": "ECO-E3-L00384-1", "fonte_ref": "E3-L00384", "destino": "47", "subtema": H2["ric"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI_NOV,
        "rotulo_item": "Item",
        "assertiva": ("A equivalência ricardiana estabelece que manejos do fisco não se traduzem em efeitos sobre o "
                      "produto e a renda de um país, dado que os agentes econômicos adotam ações com efeitos "
                      "contrários e equivalentes àqueles adotados pelo Estado na política fiscal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A equivalência ricardiana estabelece que manejos do fisco não se traduzem em efeitos sobre o "
                      "produto e a renda de um país, dado que os agentes econômicos adotam ações com efeitos "
                      "<u>contrários e equivalentes</u> àqueles adotados pelo Estado na política fiscal."),
        "poucas": ("É a tese da " + azb("neutralidade") + " ricardiana: o setor privado “desfaz” o déficit "
                   "poupando exatamente o que o governo despoupa, e produto e renda ficam inalterados."),
        "destrinchando": [
            "O “efeito contrário e equivalente” é a " + azb("poupança privada") + ": o governo corta impostos e "
            "reduz a poupança pública em Δ; as famílias, que antecipam os impostos futuros, elevam a poupança "
            "privada em Δ. A poupança nacional fica igual, e com ela juros, investimento, consumo e produto.",
            "Raiz do argumento: a " + azb("restrição orçamentária intertemporal") + " do governo. Ele não pode "
            "rolar a dívida para sempre; o que não se cobra hoje se cobra amanhã, com juros. Para quem enxerga "
            "isso, dívida pública não é riqueza líquida (" + oc("Barro") + ", " + vd("1974") + ").",
            "Leitura precisa: o teorema trata da <b>forma de financiar</b> um gasto dado (imposto × dívida). Um "
            "aumento de G com o mesmo valor presente de impostos ainda absorve recursos reais. O item, porém, "
            "usa “manejos do fisco” no sentido corrente de déficit e corte de impostos — e é assim que a "
            "banca o julgou.",
            "Por que a neutralidade costuma falhar: restrição de crédito, miopia, vida finita sem herança, "
            "impostos distorcivos e incerteza. A evidência empírica, em geral, acha equivalência parcial.",
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Paráfrase do núcleo do teorema. A palavra "
                       "que assusta é “equivalentes” (parece absoluta), mas é exatamente o que a teoria diz: "
                       "compensação integral. Cuidado com a versão que estende a neutralidade a <b>qualquer</b> "
                       "teoria ou ao mundo real."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A equivalência ricardiana demonstra empiricamente que a política fiscal é ineficaz nas economias "
            "emergentes.”</i> → ERRADO (extrapolação: é proposição teórica, e a restrição de crédito a enfraquece "
            "justamente nos emergentes)",
            "<i>“Na equivalência ricardiana, a queda da poupança pública é compensada por aumento igual da "
            "poupança privada.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Agentes racionais poupam o excedente de renda para pagar impostos futuros; não há "
                             "impacto sobre consumo ou renda, apenas sobre a poupança. Ressalva das respostas de "
                             "IA: a proposição é caso-limite e trata da forma de financiamento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 559", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida no 📖"}],
        "alertas": ["quase_duplicata: ECO-E3-L00074-1 e ECO-E3-L00210-1 (mesma tese)"],
    },
    # ------------------------------------------------------------------ E3-L00385
    {
        "id": "ECO-E3-L00385-1", "fonte_ref": "E3-L00385", "destino": "47", "subtema": H2["pf"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_NOV,
        "rotulo_item": "Item",
        "assertiva": "A hipótese do <i>crowding out</i> relaciona a formação de poupança privada e a despoupança pública.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A hipótese do <i>crowding out</i> relaciona ")
                    + vm("a formação de poupança privada e a despoupança pública") + az(".")),
        "poucas": ("Compensar despoupança pública com poupança privada é a " + azb("equivalência ricardiana")
                   + ". O " + azb("crowding out") + " é outra coisa: o gasto público eleva os juros e "
                   "<b>expulsa o investimento privado</b>."),
        "destrinchando": [
            azb("Crowding out") + " (efeito deslocamento): a política fiscal expansionista eleva a demanda por "
            "moeda e por fundos emprestáveis; com a oferta de moeda dada, " + vd("i ↑") + "; o investimento "
            "privado (e o consumo a crédito) " + vd("cai") + ", e parte do impulso fiscal se perde.",
            "No IS-LM: G ↑ desloca a IS para a direita; se os juros não mudassem, a renda subiria pelo "
            "multiplicador pleno; como a LM não se move, os juros sobem e a renda sobe menos. A diferença é o "
            "crowding out.",
            "Grau do efeito: <b>total</b> no caso clássico (LM vertical — demanda por moeda insensível aos "
            "juros); <b>nulo</b> na armadilha da liquidez (LM horizontal) ou se o Banco Central acomodar, "
            "expandindo a moeda para segurar os juros. Investimento muito sensível aos juros amplia o efeito.",
            "Na versão de fundos emprestáveis: déficit ↑ → poupança nacional ↓ → r ↑ → I ↓. Ali aparece a "
            "despoupança pública, mas o que define o conceito é o <b>deslocamento do investimento</b>, não uma "
            "compensação por poupança privada. Em economia aberta, a alta de juros atrai capital, aprecia o "
            "câmbio e desloca também as exportações líquidas.",
            "A tese de que a poupança privada sobe para compensar a despoupança pública é a "
            + azb("equivalência ricardiana") + " (" + oc("Barro") + "), na qual, aliás, <b>não</b> há "
            "crowding out: a poupança nacional não muda e os juros ficam parados.",
        ],
        "grafico_verso": "ECO-E3-L00385-1-V1",
        "dissecando": (cz("[troca de conceito]") + " O item cola no crowding out a definição de outro conceito "
                       "do mesmo capítulo. A pista: crowding out tem sempre três peças — gasto público, "
                       "<b>juros</b>, <b>investimento privado</b>; se a frase não fala em juros nem em "
                       "investimento, desconfie."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O crowding out é total quando a curva LM é vertical.”</i> → CERTO",
            "<i>“O crowding out é máximo na armadilha da liquidez.”</i> → ERRADO (inversão: com LM horizontal "
            "os juros não sobem e o efeito é nulo)",
        ])],
        "reescrita": ("A hipótese do <i>crowding out</i> relaciona " + hl("a expansão do gasto público à redução "
                      "do investimento privado, por meio da alta dos juros") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Crowding out é a redução do investimento privado causada pela alta dos juros quando "
                             "o governo expande o gasto; a relação poupança privada × despoupança pública é a "
                             "equivalência ricardiana."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 560-561", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvidas no 📖; mecanismo redesenhado em ECO-E3-L00385-1-V1"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0128
    {
        "id": "ECO-E1-0128-1", "fonte_ref": "E1-0128", "destino": "48", "subtema": H2["laf"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "A respeito dos mercados competitivos e da tributação, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("A Curva de Laffer mostra que há limites para o governo elevar a arrecadação tributária "
                      "através da elevação de impostos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A Curva de Laffer mostra que <u>há limites</u> para o governo elevar a arrecadação "
                      "tributária através da elevação de impostos."),
        "poucas": ("A " + azb("curva de Laffer") + " liga alíquota e arrecadação: a receita sobe até uma alíquota "
                   "t* e depois cai, chegando a zero com alíquota de 100%. Elevar impostos não eleva a "
                   "arrecadação indefinidamente."),
        "destrinchando": [
            "Arrecadação = alíquota × base. Com " + vd("t = 0") + ", não se arrecada nada; com "
            + vd("t = 100%") + ", ninguém tem incentivo a produzir, trabalhar ou declarar — a base some e a "
            "arrecadação também é zero. Entre os extremos há um ponto de " + azb("receita máxima") + ".",
            "À esquerda de t*, alíquota maior ainda rende mais (o efeito alíquota supera a erosão da base); à "
            "direita, na " + azb("zona proibitiva") + ", a base encolhe mais que proporcionalmente — por menos "
            "trabalho, menos investimento, mais evasão, elisão e informalidade — e a receita cai.",
            "Associada a " + oc("Arthur Laffer") + " e à " + azb("economia do lado da oferta") + " dos anos "
            "1970–80 (cortes de impostos de Reagan). A ideia de que impostos altos demais reduzem a receita é "
            "bem mais antiga; o que se discute empiricamente é <b>onde</b> fica t*.",
            "A curva não diz que a economia está na zona proibitiva, nem que cortar impostos sempre aumenta a "
            "arrecadação: isso só vale se a alíquota de partida estiver acima de t*.",
        ],
        "dissecando": (cz("[literalidade]") + " Enunciado básico da curva. Os itens da banca sobre Laffer giram "
                       "quase sempre em torno de absolutos: “qualquer”, “sempre”, “ilimitada”, “relação "
                       "inversa”. Este, sem modulador absoluto, é CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva de Laffer mostra que a redução de alíquotas sempre eleva a arrecadação.”</i> → ERRADO "
            "(modulador absoluto: só na zona proibitiva)",
            "<i>“Pela curva de Laffer, uma alíquota de 100% maximiza a arrecadação.”</i> → ERRADO (dado "
            "alterado: com 100% a arrecadação tende a zero)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A um determinado nível de tributação, não haverá arrecadação.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0658-1 (mesma tese, versão ERRADO com “ilimitada”)"],
    },
    # ------------------------------------------------------------------ E1-0356
    {
        "id": "ECO-E1-0356-1", "fonte_ref": "E1-0356", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Acerca dos conceitos de déficit e dívida públicos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O déficit público nominal é igual à variação da dívida líquida do setor público apurada no "
                      "ano."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O déficit público nominal é igual à variação da dívida ") + vm("líquida do setor público")
                    + az(" apurada no ano.")),
        "poucas": ("As " + azb("NFSP nominais") + " correspondem à variação da dívida líquida <b>descontados os "
                   "ajustes</b> patrimoniais e metodológicos (privatizações, reconhecimento de dívidas, efeito do "
                   "câmbio). Ou seja, igualam a variação da " + azb("dívida fiscal líquida") + ", não a da DLSP."),
        "destrinchando": [
            "O " + rx("Banco Central do Brasil") + " mede o resultado fiscal “abaixo da linha”: pela variação do "
            "endividamento. Mas nem toda variação da DLSP vem do déficit. Parte vem de " + azb("ajustes "
            "patrimoniais") + " (privatizações reduzem a dívida; reconhecimento de passivos antigos, os "
            "“esqueletos”, a aumenta) e de " + azb("ajustes metodológicos") + " (sobretudo o efeito da "
            "variação cambial sobre ativos e passivos em moeda estrangeira).",
            "Daí a identidade: " + vd("dívida fiscal líquida = DLSP − ajustes") + " e "
            + vd("NFSP nominal = Δ dívida fiscal líquida") + ". O déficit é a parte da variação da dívida "
            "explicada pelos fluxos de receitas, despesas e juros do período.",
            "Exemplo: o " + rx("Brasil") + " é credor líquido em moeda estrangeira (reservas internacionais "
            "superam a dívida externa). Uma " + azb("depreciação do real") + " aumenta o valor das reservas em "
            "reais e <b>reduz</b> a DLSP sem que tenha havido superávit algum — e uma apreciação faz o "
            "contrário.",
            "Nem a dívida bruta resolve: a DBGG também se move por operações sem relação com o resultado do ano "
            "(emissões para formar caixa, compromissadas do BC, empréstimos a bancos públicos). Por isso a "
            "medida oficial usa a dívida <b>líquida ajustada</b>.",
            vm("Regra-âncora: NFSP nominal = variação da dívida fiscal líquida (DLSP sem os ajustes)."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " Em manuais introdutórios, “déficit = "
                       "variação da dívida” é aproximação aceita; o item a apresenta como igualdade exata com a "
                       "DLSP e esquece os ajustes. Pista: “igual” + um agregado específico de dívida pede o "
                       "conceito ajustado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As necessidades de financiamento do setor público no conceito nominal correspondem à variação "
            "da dívida fiscal líquida.”</i> → CERTO",
            "<i>“Uma depreciação cambial eleva a dívida líquida do setor público brasileiro.”</i> → ERRADO "
            "(inversão: o país é credor líquido em dólar e a DLSP cai)",
        ])],
        "reescrita": ("O déficit público nominal é igual à variação da dívida " + hl("fiscal líquida (a dívida "
                      "líquida do setor público descontados os ajustes patrimoniais e metodológicos)")
                      + " apurada no ano."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["igual"], "dificuldade": 3,
        "comentario_fonte": ("Diz que o déficit nominal equivale à variação da dívida bruta, porque a líquida "
                             "desconta ativos como as reservas, cuja valorização cambial reduz a dívida líquida."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem iguala o déficit nominal à variação da dívida bruta; "
                    "o conceito oficial (BCB) é a variação da dívida fiscal líquida, isto é, da DLSP sem os "
                    "ajustes patrimoniais e cambiais — corrigido",
                    "banca_provavel: a fonte marca o item como de 2019 (possivelmente CACD), sem confirmação"],
    },
    # ------------------------------------------------------------------ E1-0438
    {
        "id": "ECO-E1-0438-1", "fonte_ref": "E1-0438", "destino": "48", "subtema": H2["conc"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Clipping", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": CMD_CLIP,
        "rotulo_item": "Item",
        "assertiva": ("O conceito de déficit nominal considera apenas o saldo primário do governo, excluindo os "
                      "encargos com os juros da dívida pública."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O conceito de déficit ") + vm("nominal") + az(" considera apenas o saldo primário do "
                                                                     "governo, excluindo os encargos com os "
                                                                     "juros da dívida pública.")),
        "poucas": ("A definição é a do " + azb("resultado primário") + ". O " + azb("resultado nominal")
                   + " é o primário <b>mais</b> os juros nominais da dívida — é a medida completa das "
                   "necessidades de financiamento."),
        "destrinchando": [
            azb("Primário") + " = receitas não financeiras − despesas não financeiras (pessoal, custeio, "
            "investimento, previdência, transferências). Mede o " + azb("esforço fiscal") + " corrente, sem o "
            "peso das decisões passadas que estão nos juros.",
            azb("Nominal") + " = " + vd("primário + juros nominais") + ". Corresponde às " + azb("NFSP")
            + " no conceito nominal: quanto o setor público precisou financiar no período e, portanto, quanto "
            "a dívida fiscal aumentou.",
            azb("Operacional") + " = primário + juros <b>reais</b> (o nominal sem a correção monetária). Útil em "
            "inflação alta, quando a maior parte dos juros nominais é mera reposição da inflação.",
            "Leitura conjunta: é possível ter " + vd("superávit primário e déficit nominal") + " ao mesmo tempo "
            "— basta que os juros superem o superávit. É a situação típica do " + rx("Brasil") + " nas décadas "
            "de metas de primário com juros altos: o esforço fiscal existe, mas a dívida continua a crescer.",
            "Convenção das NFSP do BCB: valor positivo = déficit (necessidade de financiamento); negativo = "
            "superávit.",
            vm("Regra-âncora: primário exclui juros; operacional inclui só os reais; nominal inclui todos."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Definição correta do primário com o rótulo trocado para "
                       "“nominal”. O “apenas” e o “excluindo” são as pistas: o nominal é o conceito "
                       "<b>mais amplo</b>, o único que não exclui nada."),
        "modulos": [
            ("😈 Para dificultar", [
                "<i>“O conceito de déficit primário considera o saldo das contas do governo excluindo os encargos "
                "com os juros da dívida pública.”</i> → CERTO",
                "<i>“O déficit operacional inclui os juros nominais e exclui as despesas primárias.”</i> → ERRADO "
                "(troca de conceito: inclui as primárias e só os juros reais)",
            ]),
            ("🧠 Mnemônico", ["<b>N</b>ominal = tudo; <b>O</b>peracional = tira a inflação dos juros; "
                             "<b>P</b>rimário = tira todos os juros."]),
        ],
        "reescrita": ("O conceito de déficit " + hl("primário") + " considera apenas o saldo primário do governo, "
                      "excluindo os encargos com os juros da dívida pública."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("O conceito descrito é o de resultado primário; o nominal é o primário somado aos "
                             "juros nominais e mede a necessidade total de financiamento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: comentário fundido com o da linha E1-0540 (mesmo item e mesmo verso)",
                    "quase_duplicata: ECO-E2-L01775-1 (nominal × primário, outra prova)"],
    },
]
