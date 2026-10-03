"""Cards do lote de redação 12 — ECO, passada 02 (notas 27: IS-LM e 28: OA-DA)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H27 = {
    "is": "📉 Curva IS",
    "lm": "📈 Curva LM",
    "pol": "🏦 Política fiscal e monetária",
    "ext": "🕳️ Casos extremos",
}
H28 = {
    "da": "📈 Demanda agregada",
    "oa": "🏭 Oferta agregada e choques",
}

CMD_ANTT_1 = "Considerando o modelo IS-LM, em que o Banco Central fixa a quantidade de moeda, julgue o item a seguir."
CMD_ANTT_2 = "Julgue o próximo item, tendo em vista os modelos macroeconômicos para economias abertas."
CMD_ANTT_3 = "A partir da teoria macroeconômica, julgue o item a seguir."
CMD_NIDI = ("A respeito das interações entre política fiscal, política monetária e suas implicações para as curvas "
            "IS-LM em um modelo macroeconômico, julgue (C ou E) o item a seguir.")

ALERTA_ANO_ANTT = ("nota_redacao: a frente data a prova de 2023; o print do banco de questões reproduzido no verso "
                   "da fonte a identifica como CEBRASPE 2024, Especialista em Regulação da ANTT — mantido o ano da "
                   "frente")

CMD_TPS = "Considere uma economia descrita pelo seguinte sistema de equações, em tempo contínuo."
EXC_TPS = ("<p><i>Função de produção agregada: Y = F(K, N); F<sub>K</sub> > 0, F<sub>N</sub> > 0, "
           "F<sub>KN</sub> > 0, F<sub>NN</sub> < 0, F<sub>KK</sub> < 0, em que F<sub>i</sub> é a primeira derivada "
           "da função de produção com relação ao insumo i, e F<sub>ii</sub> é a segunda derivada da função de "
           "produção com relação ao insumo i.</i></p>"
           "<p><i>Demanda de trabalho em termos reais: W / P = F<sub>N</sub>(K, N).</i></p>"
           "<p><i>Função investimento: I = I(q(K, N, r − π) − 1); I′ < 0, em que I′ é a derivada do investimento em "
           "relação à taxa de juros.</i></p>"
           "<p><i>Função consumo: C = C(Y − T); 0 < C′ < 1, em que C′ é a derivada do consumo em relação à renda "
           "disponível.</i></p>"
           "<p><i>Equilíbrio no mercado de bens: Y = C + I + G + δK (5)</i></p>"
           "<p><i>Equilíbrio monetário: M / P = m(Y, r) (6), em que Y é o produto, N o emprego, K o estoque de "
           "capital, w o salário nominal, P o nível geral de preços, I o investimento, q o Q de Tobin, r a taxa "
           "nominal de juros, π a taxa de inflação, C o consumo, T os tributos autônomos, G os gastos autônomos "
           "do governo, m(Y, r) a demanda real por moeda e M o estoque nominal de moeda, δK a taxa de "
           "depreciação do estoque de capital.</i></p>"
           "<p><i>Considere, ainda, um regime em que: o governo (via Banco Central) controla exogenamente a "
           "quantidade de moeda M; o estoque de capital é constante no tempo.</i></p>"
           "<p><i>A respeito dessa economia, julgue o item que se segue.</i></p>")
CMD_BOZAN = ("Considere o modelo de demanda e oferta agregada, especialmente no contexto de choques de demanda e "
             "políticas econômicas. Julgue o item a seguir como certo ou errado.")
CMD_NAB4 = ("Considerando a importância da oferta agregada e da demanda agregada para a formação do produto na "
            "economia, julgue o item a seguir.")
CMD_RT1 = "Julgue o item a seguir, acerca do modelo de oferta e demanda agregadas e da curva de Phillips."
CMD_RT2 = "Com relação à oferta agregada, salários, preços e emprego, julgue o item a seguir."
CMD_RT3 = ("Em 2021, o mundo todo tem passado por uma aceleração inflacionária, que combina elementos de oferta e "
           "de demanda. A este respeito, julgue o item a seguir.")
ALERTA_TPS = ("texto_parcial: a equação da demanda de trabalho não veio na frente da fonte (só o rótulo); "
              "restituída como W / P = F_N(K, N), forma citada no item 196 da mesma prova")

CARDS = [
    # ------------------------------------------------------------------ E3-L00131
    {
        "id": "ECO-E3-L00131-1", "fonte_ref": "E3-L00131", "destino": "27", "subtema": H27["pol"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_ANTT_1,
        "rotulo_item": "Item",
        "assertiva": ("Uma política expansionista, por parte do governo, de aumento dos salários dos empregados "
                      "gera, como resultado, o aumento da taxa de juros de equilíbrio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Uma política expansionista, por parte do governo, de aumento dos salários dos empregados ")
                    + vm("gera, como resultado,") + az(" o aumento da taxa de juros de equilíbrio.")),
        "poucas": ("Salário não é instrumento do IS-LM (G, T e M são). O efeito de um aumento salarial sobre a "
                   + azb("IS") + " é ambíguo — mais consumo, mas custos maiores e menos investimento —, então a "
                   "alta dos juros não é resultado necessário."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "se “aumento dos salários dos empregados” for lido como reajuste do funcionalismo sem "
                          "compensação, trata-se de " + azb("G ↑") + ": a IS vai para a direita e, com M fixo, os "
                          "juros sobem — o item seria CERTO. O ERRADO oficial se sustenta pela leitura de que "
                          "salário não é variável do modelo e de que o sinal do efeito líquido é indeterminado.")],
        "destrinchando": [
            "No IS-LM de curto prazo (preços dados), a política fiscal entra por " + azb("G") + " e " + azb("T")
            + " na IS: Y = C(Y − T) + I(i) + G; a monetária entra por " + azb("M") + " na LM: M/P = L(Y, i). "
            "Salário nominal não aparece em nenhuma das duas equações.",
            "Um aumento de salários pode significar coisas diferentes: (a) reajuste de servidores, que eleva G se "
            "não for compensado; (b) aumento do salário mínimo ou dos salários privados, que é choque de "
            + azb("custo") + " (desloca a oferta agregada para a esquerda) e pode reduzir lucros e investimento; "
            "(c) reajuste compensado por corte de outros gastos ou alta de tributos, com ΔG ≈ 0.",
            "Por isso o deslocamento líquido da IS pode ser para a direita, nulo ou para a esquerda, e o efeito "
            "sobre i é " + vd("indeterminado") + ". O mecanismo que garante juros maiores com M fixo é o de "
            "G ↑ ou T ↓ não compensados: IS → direita, Y ↑, demanda por moeda ↑, " + vd("i ↑") + ".",
            vm("Regra-âncora: no IS-LM, juros sobem com certeza só quando a IS vai para a direita ou a LM vai "
               "para a esquerda; o item precisa dizer qual curva se move."),
        ],
        "dissecando": (cz("[nexo indevido · modulador absoluto]") + " O item rotula como “expansionista” uma "
                       "medida que o modelo não contém e afirma um resultado certo (“gera, como resultado”). "
                       "Pista: o comando fixa M, mas a medida descrita não é nem G, nem T, nem M. 🔥 O mesmo bloco "
                       "da prova cobrava, como CERTO, a queda de G (IS para a esquerda) e o aumento da incerteza "
                       "(LM para a esquerda)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento autônomo dos gastos do governo, não compensado por tributos, gera aumento da taxa de "
            "juros de equilíbrio.”</i> → CERTO",
            "<i>“Uma política fiscal expansionista gera, com M fixo, redução da taxa de juros de equilíbrio.”</i> → "
            "ERRADO (inversão: os juros sobem)",
        ])],
        "reescrita": ("Uma política expansionista, por parte do governo, de aumento dos salários dos empregados "
                      + hl("não gera, necessariamente,") + " o aumento da taxa de juros de equilíbrio"
                      + hl(", pois seu efeito líquido sobre a IS é ambíguo") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["gera, como resultado"], "dificuldade": 3,
        "comentario_fonte": ("Várias respostas empilhadas: salário não é G nem T; efeito ambíguo (consumo × "
                             "custos); uma delas confunde com política monetária expansionista; outra diz que o "
                             "efeito contracionista (custos) supera o expansionista."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 120", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (IS-LM e OA-DA com deslocamentos; conteúdo absorvido no 📖)"},
                          {"ref": "IMAGEM 121", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 122-123", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (conteúdo absorvido no 📖)"}],
        "alertas": ["contestavel: lido como reajuste do funcionalismo não compensado (G ↑), o item seria CERTO; "
                    "mantido o ERRADO oficial", ALERTA_ANO_ANTT,
                    "qualidade_fonte: um dos comentários do verso explica o item como se fosse política monetária "
                    "expansionista (que reduz juros), o que não corresponde à assertiva"],
    },
    # ------------------------------------------------------------------ E3-L00133
    {
        "id": "ECO-E3-L00133-1", "fonte_ref": "E3-L00133", "destino": "27", "subtema": H27["pol"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_1,
        "rotulo_item": "Item",
        "assertiva": "A redução dos gastos do governo gera queda da renda e da taxa de juros de equilíbrio.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A redução dos gastos do governo gera queda <u>da renda e da taxa de juros</u> de equilíbrio."),
        "poucas": ("G ↓ é " + azb("política fiscal contracionista") + ": a IS vai para a esquerda ao longo de uma LM "
                   "fixa (M dado), e o novo equilíbrio tem " + vd("Y menor e i menor") + "."),
        "destrinchando": [
            "A IS reúne os pares (Y, i) que equilibram o mercado de bens: Y = C(Y − T) + I(i) + G. Com menos G, "
            "a demanda agregada é menor a cada taxa de juros → a IS se desloca para a <b>esquerda</b>, de ΔG "
            "vezes o multiplicador.",
            "Com o Banco Central fixando M, a LM não se move. Ao cair a renda, cai a " + azb("demanda por moeda "
            "para transações") + "; com a oferta de moeda parada, sobra moeda e os juros caem até reequilibrar o "
            "mercado monetário.",
            "Os juros mais baixos estimulam parte do investimento privado (" + azb("crowding in") + "), de modo "
            "que a renda cai <b>menos</b> do que no multiplicador simples. É o espelho do crowding out da "
            "expansão fiscal.",
            "Tabela de sinais que a banca cobra: fiscal expansionista → Y ↑, i ↑; fiscal contracionista → Y ↓, "
            "i ↓; monetária expansionista → Y ↑, i ↓; monetária contracionista → Y ↓, i ↑.",
            vm("Regra-âncora: política fiscal move Y e i no mesmo sentido; política monetária, em sentidos "
               "opostos."),
        ],
        "grafico_verso": "ECO-E3-L00133-1-V1",
        "dissecando": (cz("[literalidade]") + " Item de manual, sem modulador: basta saber qual curva a "
                       "medida desloca e para onde. O risco é o candidato achar que “menos gasto” reduz juros só "
                       "via menor necessidade de financiamento (argumento de fundos emprestáveis): o resultado é "
                       "o mesmo, mas o mecanismo do IS-LM é a queda da demanda por moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução dos gastos do governo gera queda da renda e elevação da taxa de juros de "
            "equilíbrio.”</i> → ERRADO (sinal trocado: i cai)",
            "<i>“A redução da oferta de moeda gera queda da renda e da taxa de juros de equilíbrio.”</i> → ERRADO "
            "(curva trocada: LM para a esquerda eleva i)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("G ↓ reduz a demanda agregada, IS para a esquerda, LM fixa: renda e juros caem; "
                             "gráfico com IS original e IS após redução de gastos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 125", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00133-1-V1)"}],
        "alertas": [ALERTA_ANO_ANTT],
    },
    # ------------------------------------------------------------------ E3-L00135
    {
        "id": "ECO-E3-L00135-1", "fonte_ref": "E3-L00135", "destino": "27", "subtema": H27["lm"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_1,
        "rotulo_item": "Item",
        "assertiva": "O aumento da incerteza gera elevação da taxa de juros de equilíbrio.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento da incerteza gera <u>elevação</u> da taxa de juros de equilíbrio."),
        "poucas": ("Incerteza ↑ → " + azb("preferência pela liquidez") + " ↑ → demanda por moeda ↑. Com M fixo, "
                   "a LM vai para a esquerda e o novo equilíbrio tem " + vd("i maior") + " (e Y menor)."),
        "destrinchando": [
            oc("Keynes") + " (<i>Teoria Geral</i>, 1936) distingue três motivos para reter moeda: "
            + azb("transação") + ", " + azb("precaução") + " e " + azb("especulação") + ". A incerteza reforça "
            "os dois últimos: guarda-se moeda como colchão contra imprevistos e evita-se o risco de perda de "
            "capital em títulos.",
            "Formalmente, L = L(Y, i, σ), com ∂L/∂σ > 0. Para cada renda, a demanda por moeda é maior; como a "
            "oferta real M/P está fixa, só uma taxa de juros mais alta reequilibra o mercado monetário → a LM se "
            "desloca para cima/esquerda.",
            "Mecanismo de mercado: para obter liquidez, os agentes vendem títulos; o preço dos títulos cai e, "
            "como preço e rendimento variam em sentido inverso, " + vd("i sobe") + ".",
            "No equilíbrio IS-LM, juros maiores derrubam o investimento: " + vd("i ↑ e Y ↓") + ". Se a incerteza "
            "também deprimir o investimento (IS para a esquerda), Y cai ainda mais e o efeito sobre i fica menor, "
            "mas o canal que o item cobra é o monetário.",
            "Por isso, em crises de confiança, bancos centrais costumam " + azb("acomodar") + " a “fuga para a "
            "liquidez” expandindo a base monetária — o que o enunciado exclui ao fixar M.",
        ],
        "grafico_verso": "ECO-E3-L00135-1-V1",
        "dissecando": (cz("[contraintuitivo]") + " A intuição leiga associa incerteza a “economia fraca, juros "
                       "baixos”. A banca ancora tudo no comando (“o Banco Central fixa a quantidade de moeda”): "
                       "sem acomodação, mais demanda por moeda só pode sair em juros mais altos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento da incerteza desloca a LM para a direita, reduzindo a taxa de juros.”</i> → ERRADO "
            "(sentido trocado: a LM vai para a esquerda)",
            "<i>“O aumento da incerteza, por elevar a demanda por moeda, tende a reduzir o produto de "
            "equilíbrio.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Incerteza eleva a preferência pela liquidez (precaução e especulação); com M fixo, "
                             "excesso de demanda por moeda, venda de títulos, juros sobem; LM para a esquerda, "
                             "Y cai."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 126", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00135-1-V1)"},
                          {"ref": "IMAGEM 127", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [ALERTA_ANO_ANTT],
    },
    # ------------------------------------------------------------------ E3-L00141
    {
        "id": "ECO-E3-L00141-1", "fonte_ref": "E3-L00141", "destino": "27", "subtema": H27["is"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_ANTT_2,
        "rotulo_item": "Item",
        "assertiva": ("A curva IS para a economia aberta possui menor inclinação que a curva IS para a economia "
                      "fechada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A curva IS para a economia aberta possui ") + vm("menor") + az(" inclinação que a curva IS "
                    "para a economia fechada.")),
        "poucas": ("As importações são um " + azb("vazamento") + " que reduz o multiplicador: a renda reage menos "
                   "aos juros, e a IS da economia aberta é " + vd("mais inclinada") + " (mais íngreme)."),
        "destrinchando": [
            "A inclinação da IS mede quanto Y responde a uma variação de i. Uma queda de juros eleva o "
            "investimento em b·Δi; a renda sobe ΔY = " + azb("multiplicador") + " × b·Δi. Quanto maior o "
            "multiplicador, mais Y reage → IS mais plana.",
            "Economia fechada (sem tributos): k = " + vd("1/(1 − c)") + ". Economia aberta, com importações "
            "M = m·Y: k = " + vd("1/(1 − c + m)") + ". Como m > 0, o multiplicador é menor: parte de cada real "
            "de renda adicional “vaza” para produtores estrangeiros.",
            "Com multiplicador menor, a mesma queda de juros gera aumento menor de Y → a IS fica "
            + vd("mais íngreme") + ". Pelo mesmo motivo, tributos proporcionais à renda (alíquota t) também "
            "deixam a IS mais inclinada: k = 1/[1 − c(1 − t) + m].",
            "Nuance: em modelos com câmbio flutuante, juros mais baixos depreciam a moeda e elevam as "
            "exportações líquidas — um canal adicional que torna a renda <b>mais</b> sensível aos juros. A "
            "leitura padrão da banca, porém, é a do multiplicador com propensão a importar.",
            vm("Regra-âncora: multiplicador maior → IS mais plana; todo vazamento (s, t, m) deixa a IS mais "
               "inclinada."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte o sentido do efeito da abertura. Armadilha de "
                       "vocabulário: “mais inclinada” = mais íngreme = renda <b>menos</b> sensível aos juros. "
                       "Quem associa economia aberta a “mais canais de transmissão” marca CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a propensão marginal a importar, mais inclinada é a curva IS.”</i> → CERTO",
            "<i>“Uma maior propensão marginal a consumir torna a curva IS mais inclinada.”</i> → ERRADO "
            "(inversão: c maior → multiplicador maior → IS mais plana)",
        ])],
        "reescrita": ("A curva IS para a economia aberta possui " + hl("maior") + " inclinação que a curva IS para "
                      "a economia fechada."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Propensão a importar no denominador reduz o multiplicador; IS aberta mais inclinada. "
                             "Outros comentários: um atribui o efeito à fuga de capitais com apreciação ao reduzir "
                             "juros; o último afirma maior sensibilidade de Y aos juros na economia aberta."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 135", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "cortada (print do banco de questões)"},
                          {"ref": "IMAGEM 136", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [ALERTA_ANO_ANTT,
                    "qualidade_fonte: um comentário diz que juros menores provocam apreciação do real (seria "
                    "depreciação); outro conclui que a renda é mais sensível aos juros na economia aberta, o que "
                    "contradiz o gabarito — corrigidos"],
    },
    # ------------------------------------------------------------------ E3-L00173
    {
        "id": "ECO-E3-L00173-1", "fonte_ref": "E3-L00173", "destino": "27", "subtema": H27["pol"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": True,
        "comando": CMD_ANTT_3,
        "rotulo_item": "Item",
        "assertiva": ("Tomando um modelo IS-LM em uma economia fechada, a política fiscal será tão mais eficaz em "
                      "alterar o produto agregado quanto mais elástico for o investimento em relação à taxa de "
                      "juros."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Tomando um modelo IS-LM em uma economia fechada, a política fiscal será tão mais eficaz em "
                       "alterar o produto agregado quanto mais ") + vm("elástico") + az(" for o investimento em "
                       "relação à taxa de juros.")),
        "poucas": ("Investimento muito sensível aos juros = " + azb("crowding out") + " forte: a alta de i causada "
                   "pela expansão fiscal derruba muito o investimento. A fiscal é mais eficaz quanto "
                   + vd("menos") + " elástico o investimento."),
        "destrinchando": [
            "Expansão fiscal (G ↑): a IS vai para a direita, Y sobe, a demanda por moeda sobe e, com M fixo, "
            + vd("i sobe") + ". Os juros maiores reduzem o investimento privado — é o " + azb("efeito "
            "deslocamento (crowding out)") + ".",
            "Se o investimento é muito elástico aos juros (parâmetro b alto), a IS é <b>plana</b> e o crowding "
            "out é grande: boa parte do estímulo é anulada. Se é pouco elástico, a IS é <b>íngreme</b> e quase "
            "todo o multiplicador se realiza.",
            "Na álgebra do modelo (I = Ī − b·i; M/P = kY − h·i): ΔY/ΔG = " + vd("1 / [1 − c + b·k/h]") + ". "
            "Com b no denominador, b ↑ → multiplicador fiscal ↓.",
            "Caso-limite: IS vertical (b = 0, investimento autônomo) → fiscal com eficácia máxima e monetária "
            "nula. O espelho vale para a monetária: quanto <b>mais</b> elástico o investimento, mais eficaz ela é.",
            vm("Regra-âncora: IS plana favorece a monetária; IS íngreme favorece a fiscal."),
        ],
        "grafico_verso": "ECO-E3-L00173-1-V1",
        "dissecando": (cz("[inversão]") + " O item troca o sinal da relação (“tão mais… quanto mais”). Ele "
                       "aposta na associação “investimento sensível = economia responsiva = política forte”, que "
                       "vale para a monetária, não para a fiscal. Pista: na fiscal, os juros sobem — e juros que "
                       "sobem prejudicam justamente o investimento sensível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a política monetária será tão mais eficaz em alterar o produto quanto mais elástico for o "
            "investimento em relação à taxa de juros.”</i> → CERTO",
            "<i>“…a política fiscal será tão mais eficaz quanto mais elástica for a demanda por moeda em relação à "
            "taxa de juros.”</i> → CERTO",
        ])],
        "reescrita": ("Tomando um modelo IS-LM em uma economia fechada, a política fiscal será tão mais eficaz em "
                      "alterar o produto agregado quanto mais " + hl("inelástico") + " for o investimento em "
                      "relação à taxa de juros."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tão mais… quanto mais"], "dificuldade": 2,
        "comentario_fonte": ("Investimento elástico → IS plana → fiscal menos eficaz (crowding out); dedução pelo "
                             "multiplicador 1/(1 − c + bk/h). Um comentário fala em IS horizontal com fiscal "
                             "ineficaz e monetária totalmente eficaz."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 214", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E3-L00173-1-V1)"},
                          {"ref": "IMAGEM 215-216", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvidas"},
                          {"ref": "IMAGEM 217", "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": "cortada"}],
        "alertas": [ALERTA_ANO_ANTT],
    },
    # ------------------------------------------------------------------ E3-L00174
    {
        "id": "ECO-E3-L00174-1", "fonte_ref": "E3-L00174", "destino": "27", "subtema": H27["ext"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT_3,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo IS-LM com economia fechada caracterizado pelo cenário da armadilha de liquidez, "
                      "uma política fiscal expansionista será mais eficaz que a política monetária expansionista "
                      "para ampliar o nível de renda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um modelo IS-LM com economia fechada caracterizado pelo cenário da armadilha de liquidez, "
                      "uma política <u>fiscal</u> expansionista será mais eficaz que a política "
                      "<u>monetária</u> expansionista para ampliar o nível de renda."),
        "poucas": ("Na " + azb("armadilha da liquidez") + " a LM é horizontal: a monetária não reduz juros (é "
                   "ineficaz) e a fiscal desloca a IS sem elevar juros, com " + vd("eficácia máxima") + "."),
        "destrinchando": [
            "Com juros muito baixos, todos esperam que eles subam e que os títulos percam valor: ninguém quer "
            "comprar títulos, e a demanda por moeda para especulação torna-se " + azb("infinitamente elástica") 
            + " aos juros. Toda moeda adicional é entesourada.",
            "Graficamente, a LM tem um " + azb("trecho horizontal") + " (o “trecho keynesiano”). Uma expansão "
            "monetária desloca a LM sem mudar o ponto de equilíbrio nesse trecho: i não cai, I não sobe, "
            + vd("Y fica parado") + ".",
            "Já a expansão fiscal desloca a IS para a direita ao longo da LM plana: os juros não sobem, não há "
            + azb("crowding out") + ", e Y cresce o multiplicador keynesiano inteiro.",
            "Origem: " + oc("Keynes") + " (1936) aventou a possibilidade; " + oc("Hicks") + " (1937) a formalizou "
            "no IS-LM. Ganhou atualidade com o Japão dos anos 1990 e o pós-2008, quando juros perto de zero "
            "levaram bancos centrais a recorrer a instrumentos não convencionais.",
            vm("Regra-âncora: LM horizontal → fiscal manda; LM vertical (caso clássico) → monetária manda."),
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz o resultado-padrão dos casos extremos. O comparativo "
                       "(“mais eficaz que”) torna o item ainda mais seguro: não exige eficácia total, só a "
                       "ordenação. 🔥 Itens de IS-LM extremo testam sempre a tabela de quatro casas "
                       "(LM horizontal/vertical × fiscal/monetária)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a política monetária expansionista será mais eficaz que a fiscal para ampliar a renda.”</i> → "
            "ERRADO (inversão: na armadilha, a monetária é a ineficaz)",
            "<i>“No caso clássico, com LM vertical, a política fiscal expansionista é totalmente ineficaz para "
            "ampliar a renda.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["mais eficaz que"], "dificuldade": 1,
        "comentario_fonte": ("Na armadilha a preferência pela liquidez prevalece; política monetária impotente; "
                             "fiscal com eficácia plena porque os juros não mudam. Quadro-resumo: LM plana → "
                             "fiscal eficaz; LM vertical → monetária eficaz."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 218", "tipo_fonte": "DIAGRAMA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 219", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"},
                          {"ref": "IMAGEM 220", "tipo_fonte": "TABELA", "lado": "verso", "acao": "absorvida"}],
        "alertas": [ALERTA_ANO_ANTT],
    },
    # ------------------------------------------------------------------ E3-L00348
    {
        "id": "ECO-E3-L00348-1", "fonte_ref": "E3-L00348", "destino": "27", "subtema": H27["pol"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("A combinação de um aumento dos gastos do governo com uma redução da oferta de moeda pelo "
                      "Banco Central levará a um aumento da taxa de juros e uma redução do nível de produto no novo "
                      "equilíbrio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A combinação de um aumento dos gastos do governo com uma redução da oferta de moeda pelo "
                       "Banco Central levará a um aumento da taxa de juros e ") + vm("uma redução do nível de "
                       "produto") + az(" no novo equilíbrio.")),
        "poucas": ("IS para a direita e LM para a esquerda: os dois movimentos " + vd("elevam i") + ", mas puxam Y "
                   "em sentidos opostos. O efeito sobre o produto é " + azb("ambíguo") + "."),
        "destrinchando": [
            "G ↑ (fiscal expansionista): IS → direita; sozinha, eleva " + vd("Y e i") + ".",
            "M ↓ (monetária contracionista): LM → esquerda; sozinha, " + vd("eleva i e reduz Y") + ".",
            "Combinadas: juros sobem com certeza (as duas forças empurram i para cima). Já o produto pode subir, "
            "cair ou ficar igual, conforme o tamanho relativo dos deslocamentos e as inclinações das curvas.",
            "Método para qualquer item de “mix de políticas”: anote o sinal de cada política sobre Y e sobre i; "
            "a variável em que os sinais coincidem tem resultado <b>determinado</b>; aquela em que se opõem é "
            + azb("indeterminada") + ".",
            "Exemplo histórico do mix: nos EUA do início dos anos 1980, a expansão fiscal de " + oc("Reagan")
            + " combinada ao aperto monetário de " + oc("Volcker") + " produziu juros reais muito altos.",
            vm("Regra-âncora: sinais iguais → resultado certo; sinais opostos → depende da magnitude."),
        ],
        "grafico_verso": "ECO-E3-L00348-1-V1",
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " A primeira consequência (juros ↑) é "
                       "verdadeira e dá credibilidade; o erro está em cravar o sentido do produto, que depende "
                       "das magnitudes. Pista: duas políticas de sinais opostos sobre Y nunca permitem "
                       "“levará a uma redução” sem dados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…levará inequivocamente a um aumento da taxa de juros, sendo indeterminado o efeito sobre o "
            "produto.”</i> → CERTO",
            "<i>“A combinação de aumento de gastos com aumento da oferta de moeda elevará o produto, com efeito "
            "indeterminado sobre os juros.”</i> → CERTO",
        ])],
        "reescrita": ("A combinação de um aumento dos gastos do governo com uma redução da oferta de moeda pelo "
                      "Banco Central levará a um aumento da taxa de juros e " + hl("a um efeito indeterminado "
                      "sobre o nível de produto") + " no novo equilíbrio."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["levará"], "dificuldade": 1,
        "comentario_fonte": ("G ↑: IS à direita (i ↑, Y ↑); M ↓: LM à esquerda (i ↑, Y ↓); juros sobem com "
                             "certeza, produto ambíguo; três cenários gráficos conforme a intensidade."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 491-492", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvidas"},
                          {"ref": "IMAGEM 493-496", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "fundidas em ECO-E3-L00348-1-V1 (cenário de produto inalterado)"},
                          {"ref": "IMAGEM 497", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00349
    {
        "id": "ECO-E3-L00349-1", "fonte_ref": "E3-L00349", "destino": "27", "subtema": H27["pol"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("A combinação de um aumento dos impostos e um aumento da oferta de moeda pelo Banco Central "
                      "levará a uma queda da taxa de juros de equilíbrio. Já o novo produto de equilíbrio poderá "
                      "ser maior, igual ou menor que o anterior, dependendo da magnitude dos aumentos dos impostos "
                      "e da oferta de moeda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A combinação de um aumento dos impostos e um aumento da oferta de moeda pelo Banco Central "
                      "levará a uma <u>queda da taxa de juros</u> de equilíbrio. Já o novo produto de equilíbrio "
                      "<u>poderá ser maior, igual ou menor</u> que o anterior, dependendo da magnitude dos "
                      "aumentos dos impostos e da oferta de moeda."),
        "poucas": ("T ↑ leva a IS para a esquerda (i ↓, Y ↓); M ↑ leva a LM para a direita (i ↓, Y ↑). Juros "
                   + vd("caem com certeza") + "; o produto é " + azb("indeterminado") + "."),
        "destrinchando": [
            "Aumento de impostos = " + azb("política fiscal contracionista") + ": reduz a renda disponível e o "
            "consumo; a IS vai para a esquerda, com queda de Y e de i.",
            "Aumento da oferta de moeda = " + azb("política monetária expansionista") + ": a LM vai para a "
            "direita/baixo, com queda de i e alta de Y.",
            "Sinais sobre i: (−) e (−) → queda certa. Sinais sobre Y: (−) e (+) → depende de qual deslocamento é "
            "maior e das inclinações. Se os efeitos se compensarem, Y fica igual.",
            "Esse mix muda a <b>composição</b> do produto: com juros menores e impostos maiores, o investimento "
            "sobe e o consumo cai. É a receita clássica de quem quer consolidar as contas públicas sem recessão: "
            "aperto fiscal acompanhado de afrouxamento monetário.",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O “poderá ser maior, igual ou menor” "
                       "protege a segunda frase, e a primeira está certa porque as duas políticas reduzem i. "
                       "Repare que o item é a contraparte correta de outra cobrança comum: “G ↑ com M ↓ reduz o "
                       "produto”, que é ERRADO pelo mesmo raciocínio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…levará a uma queda da taxa de juros e a uma redução do produto de equilíbrio.”</i> → ERRADO "
            "(produto indeterminado)",
            "<i>“…o novo produto será necessariamente maior, pois a política monetária domina a fiscal.”</i> → "
            "ERRADO (modulador absoluto: depende das magnitudes)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["poderá", "dependendo"],
        "dificuldade": 1,
        "comentario_fonte": ("T ↑: IS à esquerda (r ↓, Y ↓); M ↑: LM à direita (r ↓, Y ↑); juros caem com "
                             "certeza; produto indeterminado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 498-500", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvidas"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00350
    {
        "id": "ECO-E3-L00350-1", "fonte_ref": "E3-L00350", "destino": "27", "subtema": H27["lm"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Quanto mais sensível for a demanda por moeda à taxa de juros, mais horizontal (ou menos "
                      "inclinada) será a LM."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quanto mais sensível for a demanda por moeda à taxa de juros, <u>mais horizontal</u> (ou "
                      "menos inclinada) será a LM."),
        "poucas": ("Na LM, M/P = kY − hi; a inclinação é " + vd("k/h") + ". Quanto maior h (sensibilidade aos "
                   "juros), " + azb("mais plana") + " a LM; no limite h → ∞, ela é horizontal (armadilha da "
                   "liquidez)."),
        "destrinchando": [
            "A LM reúne os pares (Y, i) que equilibram o mercado monetário com a oferta real M/P dada. Se Y "
            "sobe, a demanda por moeda para transações sobe (k·ΔY); para manter L = M/P, os juros precisam subir "
            "o bastante para reduzir a demanda especulativa em h·Δi. Logo Δi/ΔY = " + vd("k/h") + ".",
            "h grande: uma pequena alta de juros já libera muita moeda → basta pouca variação de i para "
            "acomodar a renda maior → LM " + azb("plana") + ". h pequeno: são precisos grandes saltos de i → "
            "LM " + azb("íngreme") + ".",
            "Extremos: h → ∞ → " + azb("armadilha da liquidez") + " (LM horizontal; monetária ineficaz, fiscal "
            "máxima). h = 0 → " + azb("caso clássico") + " / teoria quantitativa (LM vertical; fiscal ineficaz, "
            "monetária máxima).",
            "Exemplo numérico: com M/P = 0,97 e L = Y − 0,3i, elevar i de 0,10 para 0,50 exige Y de 1 para 1,12; "
            "com L = Y − 0,9i (e M/P = 0,91), a mesma alta de juros acompanha Y de 1 para 1,36 — LM mais plana.",
            vm("Regra-âncora: inclinação da LM = k/h; h ↑ → LM mais plana; k ↑ → LM mais íngreme."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, com o sinônimo entre parênteses para evitar "
                       "a confusão “horizontal × inclinada”. A troca típica da banca é a da sensibilidade à "
                       "<b>renda</b> (k), que tem o efeito oposto."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto mais sensível for a demanda por moeda à renda, mais horizontal será a LM.”</i> → ERRADO "
            "(troca de parâmetro: k maior deixa a LM mais íngreme)",
            "<i>“Se a demanda por moeda for insensível à taxa de juros, a LM será vertical.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["quanto mais"], "dificuldade": 1,
        "comentario_fonte": ("Inclinação da LM = k/h; h grande → LM achatada; h → ∞ armadilha da liquidez; "
                             "exemplo numérico com sensibilidades 0,3 e 0,9."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 501", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 502", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 503-505", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortadas (exemplo numérico absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00351
    {
        "id": "ECO-E3-L00351-1", "fonte_ref": "E3-L00351", "destino": "27", "subtema": H27["pol"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Dezembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Uma maior sensibilidade do investimento em relação à taxa real de juros diminui o efeito da "
                      "política monetária sobre o produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma maior sensibilidade do investimento em relação à taxa real de juros ") + vm("diminui")
                    + az(" o efeito da política monetária sobre o produto.")),
        "poucas": ("A política monetária age <b>pelos juros sobre o investimento</b>. Investimento mais sensível "
                   "= " + azb("IS mais plana") + " = mesma queda de juros gera mais produto: o efeito "
                   + vd("aumenta") + "."),
        "destrinchando": [
            "Canal de transmissão no IS-LM: M ↑ → LM para a direita → i ↓ → I ↑ → Y ↑ (via multiplicador). O "
            "elo decisivo é a resposta de I a i, medida pelo parâmetro b em I = Ī − b·i.",
            "b grande → IS " + azb("plana") + ": o deslocamento da LM “desliza” ao longo de uma IS quase "
            "horizontal e Y varia muito. b pequeno → IS " + azb("íngreme") + ": Y quase não muda.",
            "Caso-limite: IS vertical (investimento insensível aos juros, “modelo keynesiano simplificado”) → "
            "política monetária totalmente ineficaz.",
            "A eficácia monetária cai quando a demanda por moeda é muito sensível aos juros (LM plana) ou "
            "quando o investimento é pouco sensível (IS íngreme). Para a fiscal, vale o espelho: investimento "
            "sensível <b>reduz</b> sua eficácia (crowding out maior).",
            vm("Regra-âncora: b ↑ → IS plana → monetária mais forte e fiscal mais fraca."),
        ],
        "grafico_verso": "ECO-E3-L00351-1-V1",
        "dissecando": (cz("[inversão]") + " O item aplica à monetária a relação que vale para a fiscal "
                       "(investimento sensível ↓ eficácia). Pista: pergunte por onde a política atua — se é pelos "
                       "juros, sensibilidade maior aos juros só pode ampliar o efeito."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma maior sensibilidade do investimento à taxa real de juros diminui o efeito da política "
            "fiscal sobre o produto.”</i> → CERTO",
            "<i>“Uma maior sensibilidade da demanda por moeda aos juros aumenta o efeito da política monetária "
            "sobre o produto.”</i> → ERRADO (inversão: LM plana enfraquece a monetária)",
        ])],
        "reescrita": ("Uma maior sensibilidade do investimento em relação à taxa real de juros " + hl("aumenta")
                      + " o efeito da política monetária sobre o produto."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Investimento sensível → IS mais plana → deslocamento da LM gera variação maior de "
                             "Y; a monetária é menos eficaz com LM plana ou IS íngreme."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 506-507", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvidas"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0812
    {
        "id": "ECO-E1-0812-1", "fonte_ref": "E1-0812", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": CMD_TPS, "excerto": EXC_TPS,
        "rotulo_item": "Item",
        "assertiva": ("Como o modelo especifica apenas a demanda de trabalho das firmas, dada por W / P = F<sub>N</sub>"
                      "(K, N) e não uma oferta de trabalho, choques que alterem o salário nominal ou o nível de "
                      "preços podem modificar o emprego e o produto mesmo sem qualquer mudança nas preferências dos "
                      "trabalhadores, de modo que variáveis estritamente nominais influenciam variáveis reais, no "
                      "curto prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Como o modelo especifica apenas a demanda de trabalho das firmas, dada por W / P = "
                      "F<sub>N</sub>(K, N) e não uma oferta de trabalho, choques que alterem o salário nominal ou o "
                      "nível de preços <u>podem modificar o emprego e o produto</u> mesmo sem qualquer mudança nas "
                      "preferências dos trabalhadores, de modo que <u>variáveis estritamente nominais influenciam "
                      "variáveis reais</u>, no curto prazo."),
        "poucas": ("Sem oferta de trabalho, o emprego sai da " + azb("demanda de trabalho") + " ao salário real "
                   "W/P. Com W dado, qualquer mudança em P (ou em W) muda W/P e, portanto, N e Y: a moeda "
                   + vd("não é neutra") + " no curto prazo."),
        "destrinchando": [
            "As firmas contratam até que o " + azb("produto marginal do trabalho") + " iguale o salário real: "
            "W/P = F<sub>N</sub>(K, N). Como F<sub>NN</sub> < 0, salário real menor → mais emprego.",
            "Num modelo clássico, haveria também uma oferta de trabalho N<sup>s</sup>(W/P); o mercado de "
            "trabalho fixaria W/P e N independentemente de P (dicotomia clássica, OA vertical). Aqui ela não "
            "existe: o salário nominal é um dado (" + azb("rigidez nominal") + ", à " + oc("Keynes") + ").",
            "Então P sobe → W/P cai → N sobe → Y = F(K, N) sobe. Resultado: a " + azb("oferta agregada de curto "
            "prazo") + " é positivamente inclinada, P = W / F<sub>N</sub>(K, N).",
            "Consequência: choques nominais (M, W, P) deslocam emprego e produto, e não por mudança de "
            "preferências dos trabalhadores, mas porque o salário real se ajusta via preços. É a não "
            "neutralidade de curto prazo da síntese neoclássica.",
            vm("Regra-âncora: salário nominal rígido + só demanda de trabalho → OA positivamente inclinada → "
               "moeda não neutra no curto prazo."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " O item descreve corretamente a estrutura do "
                       "sistema e se protege com “podem” e “no curto prazo”. A armadilha é a frase longa e técnica "
                       "fazer o candidato desconfiar de “variáveis nominais influenciam reais”, associada à "
                       "neutralidade clássica de longo prazo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…de modo que variáveis estritamente nominais influenciam variáveis reais também no longo prazo, "
            "quando os salários se ajustam.”</i> → ERRADO (com W flexível, volta a neutralidade)",
            "<i>“Se o modelo incluísse uma oferta de trabalho com salário nominal flexível, a curva de oferta "
            "agregada seria vertical.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["podem", "no curto prazo"],
        "dificuldade": 3,
        "comentario_fonte": "Verso só com o gabarito (CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [ALERTA_TPS],
    },
    # ------------------------------------------------------------------ E1-0813
    {
        "id": "ECO-E1-0813-1", "fonte_ref": "E1-0813", "destino": "28", "subtema": H28["da"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": CMD_TPS, "excerto": EXC_TPS,
        "rotulo_item": "Item",
        "assertiva": ("Como o produto de equilíbrio é dado pela função de produção Y = F(K, N) e pelo estoque de "
                      "capital K constante no curto prazo, um aumento permanente da quantidade de moeda M, com "
                      "salário nominal dado, é necessariamente neutro: eleva apenas o nível de preços P, sem alterar "
                      "o produto real Y nem o emprego N."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Como o produto de equilíbrio é dado pela função de produção Y = F(K, N) e pelo estoque de "
                       "capital K constante no curto prazo, um aumento permanente da quantidade de moeda M, com "
                       "salário nominal dado, é ") + vm("necessariamente neutro: eleva apenas o nível de preços P, "
                       "sem alterar o produto real Y nem o emprego N") + az(".")),
        "poucas": ("K fixo não fixa Y: o emprego N varia. Com W dado, M ↑ eleva a " + azb("demanda agregada")
                   + " e P; o salário real W/P cai, as firmas contratam mais, e " + vd("N e Y sobem") + "."),
        "destrinchando": [
            "Lado da demanda: M ↑ → M/P ↑ → LM para a direita → r ↓ → investimento ↑ → " + azb("DA") + " para a "
            "direita.",
            "Lado da oferta: com W dado, a condição W/P = F<sub>N</sub>(K, N) gera uma " + azb("OA positivamente "
            "inclinada") + ": P maior → W/P menor → N maior → Y = F(K, N) maior.",
            "Novo equilíbrio: " + vd("P ↑, Y ↑, N ↑") + " e r menor. O aumento de P é menor que o de M (os "
            "saldos reais M/P sobem), justamente porque parte do estímulo vira produto.",
            "A neutralidade exigiria OA vertical: salário nominal flexível, que acompanhasse P e mantivesse W/P "
            "no nível de pleno emprego. É o resultado clássico (e o de longo prazo da síntese), não o deste "
            "sistema de curto prazo.",
            "Erro de premissa: “K constante” significa que a função de produção fica fixa, não que o produto "
            "fique fixo — Y é função também de N.",
        ],
        "dissecando": (cz("[nexo indevido · modulador absoluto]") + " O item parte de um fato verdadeiro (K "
                       "constante) e tira uma conclusão que não decorre dele (Y fixo), coroada pelo "
                       "“necessariamente”. A pista está no próprio enunciado: “com salário nominal dado” é a "
                       "hipótese que quebra a neutralidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com salário nominal perfeitamente flexível, um aumento permanente de M eleva apenas P, sem "
            "alterar Y nem N.”</i> → CERTO",
            "<i>“…um aumento de M, com salário nominal dado, reduz o salário real e eleva o emprego.”</i> → CERTO",
        ])],
        "reescrita": ("Como o produto de equilíbrio é dado pela função de produção Y = F(K, N) e pelo estoque de "
                      "capital K constante no curto prazo, um aumento permanente da quantidade de moeda M, com "
                      "salário nominal dado, " + hl("não é neutro: eleva o nível de preços P, reduz o salário real "
                      "W/P e aumenta o emprego N e o produto real Y") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "GENERALIZACAO"], "moduladores": ["necessariamente", "apenas"],
        "dificuldade": 2,
        "comentario_fonte": "Verso só com o gabarito (ERRADO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [ALERTA_TPS],
    },
    # ------------------------------------------------------------------ E1-0815
    {
        "id": "ECO-E1-0815-1", "fonte_ref": "E1-0815", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": True,
        "comando": CMD_TPS, "excerto": EXC_TPS,
        "rotulo_item": "Item",
        "assertiva": ("O aumento do salário nominal gera aumento do nível geral de preços via equação da oferta "
                      "agregada e, consequentemente, redução do nível de renda de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O aumento do salário nominal gera <u>aumento do nível geral de preços</u> via equação da "
                      "oferta agregada e, consequentemente, <u>redução do nível de renda</u> de equilíbrio."),
        "poucas": ("W ↑ desloca a " + azb("OA") + " para cima/esquerda (P = W/F<sub>N</sub>): "
                   "é um choque adverso de oferta, com " + vd("P ↑ e Y ↓") + " ao longo da DA."),
        "destrinchando": [
            "Da demanda de trabalho, P = W / F<sub>N</sub>(K, N): para cada nível de emprego (e de produto), um "
            "W maior exige um P maior para manter o salário real compatível com a produtividade marginal. A "
            "curva de oferta agregada " + azb("sobe") + ".",
            "Pelo lado da demanda: P ↑ → saldos reais M/P ↓ (M é fixado pelo Banco Central) → LM para a "
            "esquerda → r ↑ → investimento ↓. É o " + azb("efeito Keynes") + " que dá à DA inclinação negativa.",
            "Equilíbrio: " + vd("P sobe e Y cai") + "; como Y = F(K, N), o emprego também cai — o salário real "
            "final é maior que o inicial.",
            "É o mecanismo da " + azb("inflação de custos") + " e, se repetido (espiral preços-salários), da "
            "estagflação dos anos 1970. Se o Banco Central acomodasse (M ↑ na proporção de W), Y voltaria, "
            "com P ainda mais alto.",
            vm("Regra-âncora: choque de custo (W, petróleo) → OA para cima → P ↑ e Y ↓ ao mesmo tempo."),
        ],
        "dissecando": (cz("[literalidade]") + " Encadeamento correto em dois passos (oferta → preço → renda). "
                       "A armadilha é achar que salário maior, por elevar a renda dos trabalhadores, expande a "
                       "demanda: no sistema dado, o salário não entra no consumo, só no custo das firmas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento do salário nominal, por elevar a renda disponível, desloca a demanda agregada para a "
            "direita e eleva a renda de equilíbrio.”</i> → ERRADO (nexo indevido: no sistema, W só entra na "
            "oferta)",
            "<i>“O aumento do salário nominal reduz o emprego de equilíbrio.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["consequentemente"], "dificuldade": 2,
        "comentario_fonte": "Verso só com o gabarito (CERTO).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": [ALERTA_TPS],
    },
    # ------------------------------------------------------------------ E2-L00147
    {
        "id": "ECO-E2-L00147-1", "fonte_ref": "E2-L00147", "destino": "28", "subtema": H28["da"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Em um cenário de choque positivo de demanda agregada, resultante de políticas econômicas "
                      "expansivas, a renda e o crescimento econômico inicialmente aumentam, enquanto o desemprego "
                      "diminui abaixo do nível natural. Essa expansão da demanda provoca um aumento dos preços, "
                      "levando, no curto prazo, a uma inflação. No entanto, a tendência de longo prazo é o reajuste "
                      "para o nível de pleno emprego dos fatores, restabelecendo o equilíbrio econômico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um cenário de choque positivo de demanda agregada, resultante de políticas econômicas "
                      "expansivas, a renda e o crescimento econômico <u>inicialmente</u> aumentam, enquanto o "
                      "desemprego diminui abaixo do nível natural. Essa expansão da demanda provoca um aumento dos "
                      "preços, levando, no curto prazo, a uma inflação. No entanto, a tendência de <u>longo "
                      "prazo</u> é o reajuste para o nível de pleno emprego dos fatores, restabelecendo o "
                      "equilíbrio econômico."),
        "poucas": ("Choque positivo de " + azb("DA") + ": no curto prazo, Y acima do potencial, desemprego abaixo "
                   "do natural e preços em alta; no longo prazo, salários e expectativas se ajustam, a "
                   + azb("OA de curto prazo") + " sobe e a economia volta ao " + vd("produto potencial") + "."),
        "destrinchando": [
            "Curto prazo: a DA vai para a direita ao longo de uma " + azb("OA positivamente inclinada") + " "
            "(salários e preços rígidos, percepções equivocadas). Resultado: " + vd("Y ↑, P ↑, u ↓") + " — o "
            "desemprego fica abaixo da taxa natural.",
            "Ajuste: com a economia aquecida, trabalhadores e firmas revisam salários e expectativas de preços "
            "para cima; a OA de curto prazo desloca-se para a esquerda até reencontrar a " + azb("OA de longo "
            "prazo") + ", vertical no produto potencial.",
            "Longo prazo: " + vd("Y volta a Y*") + ", u volta à taxa natural, e o único legado do choque é um "
            "nível de preços mais alto — a " + azb("neutralidade de longo prazo") + " da política de demanda.",
            "Na linguagem da curva de Phillips: o choque move a economia ao longo da curva de curto prazo "
            "(mais inflação, menos desemprego); a revisão de expectativas a desloca para cima, e o desemprego "
            "retorna à NAIRU (" + oc("Friedman") + " e " + oc("Phelps") + ", fim dos anos 1960).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Narra a sequência-padrão curto prazo → longo prazo. "
                       "Os marcadores temporais (“inicialmente”, “no curto prazo”, “tendência de longo prazo”) "
                       "são o que torna o item verdadeiro; a banca costuma fabricar o ERRADO apagando-os "
                       "(“permanentemente”, “também no longo prazo”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a renda e o crescimento econômico aumentam permanentemente, enquanto o desemprego se mantém "
            "abaixo do nível natural.”</i> → ERRADO (anula o ajuste de longo prazo)",
            "<i>“…no longo prazo, o choque de demanda eleva apenas o nível de preços.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["inicialmente", "no curto prazo", "tendência"],
        "dificuldade": 1,
        "comentario_fonte": ("Choque positivo de DA eleva renda e reduz desemprego no curto prazo, com inflação; "
                             "no longo prazo, retorno ao pleno emprego (visão neoclássica)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00148
    {
        "id": "ECO-E2-L00148-1", "fonte_ref": "E2-L00148", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Choques, como o aumento repentino nos preços do petróleo, afetam imediatamente a demanda "
                      "agregada, causando uma diminuição nos níveis de emprego e crescimento econômico. A inflação "
                      "resultante do referido choque é uma inflação de demanda, visto que a elevação dos custos "
                      "reduz a capacidade de consumo da população."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Choques, como o aumento repentino nos preços do petróleo, afetam imediatamente a ")
                    + vm("demanda") + az(" agregada, causando uma diminuição nos níveis de emprego e crescimento "
                    "econômico. A inflação resultante do referido choque é uma inflação de ") + vm("demanda")
                    + az(", visto que ") + vm("a elevação dos custos reduz a capacidade de consumo da população")
                    + az(".")),
        "poucas": ("Alta do petróleo é " + azb("choque de oferta") + ": encarece a produção, desloca a OA para "
                   "cima/esquerda e gera " + vd("inflação de custos") + " com queda do produto — a estagflação."),
        "destrinchando": [
            "O petróleo é insumo de quase tudo (energia, transporte, petroquímica). Seu encarecimento eleva o "
            "custo de produzir cada unidade: a " + azb("oferta agregada de curto prazo") + " sobe. Novo "
            "equilíbrio: " + vd("P ↑ e Y ↓") + ", com mais desemprego.",
            "Inflação de demanda é a que nasce de " + azb("excesso de gasto") + " (DA para a direita) e vem "
            "com produto em alta. Inflação de custos nasce de choques de oferta e vem com produto em queda. O "
            "sinal de Y distingue as duas.",
            "A perda de poder de compra provocada pela alta de preços é <b>consequência</b> do choque, não sua "
            "origem: o consumidor compra menos porque os preços subiram (movimento ao longo da DA), não porque "
            "a DA tenha sido o canal do choque.",
            "Referência histórica: os choques da OPEP de " + vd("1973") + " e " + vd("1979") + " produziram a "
            + azb("estagflação") + " dos anos 1970 e minaram a curva de Phillips estável dos anos 1960.",
            vm("Regra-âncora: preço e produto em sentidos opostos → choque de oferta; no mesmo sentido → choque "
               "de demanda."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item acerta os efeitos (menos emprego e "
                       "crescimento) e erra a curva e o rótulo da inflação, costurando-os com uma justificativa "
                       "que inverte causa e efeito (custo → menor consumo → “inflação de demanda”). Pista: "
                       "a própria frase fala em “elevação dos custos”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O aumento repentino do preço do petróleo desloca a oferta agregada para a esquerda, gerando "
            "inflação de custos e queda do produto.”</i> → CERTO",
            "<i>“Choques de oferta adversos elevam preços e produto simultaneamente.”</i> → ERRADO (produto cai)",
        ])],
        "reescrita": ("Choques, como o aumento repentino nos preços do petróleo, afetam imediatamente a "
                      + hl("oferta") + " agregada, causando uma diminuição nos níveis de emprego e crescimento "
                      "econômico. A inflação resultante do referido choque é uma inflação de " + hl("custos")
                      + ", visto que " + hl("decorre da elevação dos custos de produção") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["imediatamente"], "dificuldade": 1,
        "comentario_fonte": ("Choques de petróleo reduzem a oferta agregada (custos de produção); inflação de "
                             "custo, não de demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00150
    {
        "id": "ECO-E2-L00150-1", "fonte_ref": "E2-L00150", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("A teoria de Phillips sugere que existindo um choque de demanda, ocorre um deslocamento "
                      "direto da curva de oferta agregada de longo prazo. Esse deslocamento implica uma estrutura de "
                      "crescimento econômico contínuo e sustentável com níveis de desemprego constantes, respaldando "
                      "diretamente um novo equilíbrio no ponto de pleno emprego dos fatores."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A teoria de Phillips sugere que existindo um choque de demanda, ")
                    + vm("ocorre um deslocamento direto da") + az(" curva de oferta agregada de longo prazo. ")
                    + vm("Esse deslocamento implica uma estrutura de crescimento econômico contínuo e sustentável "
                         "com níveis de desemprego constantes, respaldando diretamente um novo equilíbrio no ponto "
                         "de pleno emprego dos fatores") + az(".")),
        "poucas": ("Choque de demanda move a " + azb("DA") + ", não a " + azb("OA de longo prazo") + ". Na curva de "
                   "Phillips, ele gera só um " + vd("trade-off temporário") + " entre inflação e desemprego; no "
                   "longo prazo, a economia volta ao produto potencial com mais inflação."),
        "destrinchando": [
            "A " + azb("OA de longo prazo") + " é vertical no produto potencial, determinado por fatores reais: "
            "trabalho, capital, tecnologia, instituições. Ela se desloca com choques de produtividade ou de "
            "dotação de fatores, nunca diretamente por choques de demanda.",
            oc("A. W. Phillips") + " (1958) documentou, para o Reino Unido, a relação inversa entre variação dos "
            "salários nominais e desemprego. " + oc("Samuelson") + " e " + oc("Solow") + " (1960) a leram como "
            "cardápio de política; " + oc("Friedman") + " e " + oc("Phelps") + " mostraram que o trade-off só "
            "existe enquanto as expectativas não se ajustam.",
            "Com expectativas adaptativas, um choque de demanda reduz o desemprego temporariamente; quando a "
            "inflação esperada sobe, a curva de Phillips de curto prazo se desloca para cima e o desemprego "
            "volta à " + azb("taxa natural") + ". A curva de longo prazo é " + vd("vertical") + ".",
            "Logo, nada de “crescimento contínuo e sustentável”: o choque de demanda produz uma flutuação, não "
            "uma mudança de tendência. Crescimento sustentado é assunto dos modelos de crescimento (Solow), "
            "não do OA-DA.",
            vm("Regra-âncora: demanda move a DA e a Phillips de curto prazo; a OA de longo prazo só se move "
               "com fatores reais."),
        ],
        "dissecando": (cz("[troca de conceito · extrapolação]") + " Item de “erro em cascata”: atribui à "
                       "Phillips um mecanismo que não é dela (deslocar a OA de longo prazo), troca demanda por "
                       "oferta e extrai disso crescimento sustentado. Pista: “deslocamento direto” e “contínuo e "
                       "sustentável” são termos estranhos a qualquer versão da curva."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a curva de Phillips aceleracionista, um choque de demanda reduz o desemprego apenas "
            "temporariamente.”</i> → CERTO",
            "<i>“Um aumento da produtividade total dos fatores desloca a curva de oferta agregada de longo prazo "
            "para a direita.”</i> → CERTO",
        ])],
        "reescrita": ("A teoria de Phillips sugere que existindo um choque de demanda, " + hl("não ocorre "
                      "deslocamento da") + " curva de oferta agregada de longo prazo. " + hl("O choque gera apenas "
                      "um trade-off temporário entre inflação e desemprego, e, no longo prazo, a economia retorna "
                      "ao produto potencial, com inflação maior") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "EXTRAPOLACAO"], "moduladores": ["diretamente"], "dificuldade": 1,
        "comentario_fonte": ("Choque de demanda desloca a DA, não a OA de longo prazo; deslocamento da OA-LP "
                             "reflete mudanças estruturais (tecnologia); não há crescimento contínuo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “co nstantes” → “constantes” (erro de OCR)"],
    },
    # ------------------------------------------------------------------ E2-L01006
    {
        "id": "ECO-E2-L01006-1", "fonte_ref": "E2-L01006", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Sobre as teorias macroeconômicas, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A explicação presente na versão de Lucas para o formato da curva de oferta agregada "
                      "pressupõe que mesmo os preços sendo flexíveis, existe assimetria de informação onde os "
                      "fornecedores só acompanham atentamente os preços dos bens que produzem, mas desatentamente "
                      "os preços dos bens que consomem."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A explicação presente na versão de Lucas para o formato da curva de oferta agregada "
                      "pressupõe que <u>mesmo os preços sendo flexíveis</u>, existe <u>assimetria de "
                      "informação</u> onde os fornecedores só acompanham atentamente os preços dos bens que "
                      "produzem, mas desatentamente os preços dos bens que consomem."),
        "poucas": ("No modelo de " + oc("Lucas") + " (" + azb("informação imperfeita") + "), preços são "
                   "flexíveis e mercados competitivos, mas o produtor vê o próprio preço e não o nível geral: "
                   "confunde alta geral com alta relativa e produz mais."),
        "destrinchando": [
            "Equação: " + vd("Y = Y<sub>N</sub> + a(P − P<sup>e</sup>)") + ", a > 0. O produto só se afasta do "
            "natural quando o nível de preços surpreende as expectativas.",
            "A “parábola das ilhas”: cada produtor observa de perto o preço do que vende, mas só estima (P"
            "<sup>e</sup>) os preços do que compra. Se P sobe de forma geral e inesperada, ele vê o próprio "
            "preço subir, atribui parte disso a uma alta <b>relativa</b> do seu produto e eleva a oferta → "
            "OA de curto prazo positivamente inclinada.",
            "É uma das quatro explicações clássicas da OA de curto prazo (Mankiw): salários rígidos, preços "
            "rígidos, informação imperfeita (Lucas) e percepções equivocadas dos trabalhadores. A de Lucas é a "
            "única com " + azb("preços plenamente flexíveis") + ".",
            "Com " + azb("expectativas racionais") + ", choques monetários antecipados são incorporados a "
            "P<sup>e</sup> e não afetam Y (" + azb("ineficácia da política antecipada") + ", Sargent e Wallace); "
            "só surpresas monetárias têm efeito real, e temporário.",
            vm("Regra-âncora: Lucas = preços flexíveis + informação imperfeita; só a surpresa (P ≠ Pᵉ) move o "
               "produto."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Parafraseia o mecanismo das ilhas. O "
                       "“mesmo os preços sendo flexíveis” é o detalhe que separa Lucas dos novos-keynesianos "
                       "(preços rígidos, custos de menu); a banca costuma inverter justamente isso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na versão de Lucas, a inclinação positiva da oferta agregada decorre da rigidez dos preços "
            "causada por custos de menu.”</i> → ERRADO (troca de teoria: é a explicação novo-keynesiana)",
            "<i>“No modelo de Lucas, uma expansão monetária plenamente antecipada não altera o produto.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["mesmo", "só"], "dificuldade": 2,
        "comentario_fonte": ("Lucas: empresas conhecem o próprio preço mas não os demais; confundem variação do "
                             "nível geral com variação relativa; Y = Y_N + a(P − Pe); choques antecipados sem efeito "
                             "real."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 166", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "texto (equação de Lucas no 📖)"},
                          {"ref": "IMAGEM 167", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": ["texto_corrigido: “OS fornecedores” → “os fornecedores”",
                    "qualidade_fonte: a descrição da IMAGEM 167 diz que, com choque antecipado, “p − pe é igual a "
                    "Y*”; o correto é p − pe = 0 e Y = Y*"],
    },
    # ------------------------------------------------------------------ E2-L01337
    {
        "id": "ECO-E2-L01337-1", "fonte_ref": "E2-L01337", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB4,
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, a curva de oferta agregada independe do nível de preços, ao contrário do "
                      "curto prazo, no qual a oferta agregada varia positivamente em relação ao preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No longo prazo, a curva de oferta agregada <u>independe do nível de preços</u>, ao "
                      "contrário do curto prazo, no qual a oferta agregada <u>varia positivamente</u> em relação "
                      "ao preço."),
        "poucas": ("A " + azb("OA de longo prazo") + " é vertical no produto potencial (só fatores reais o "
                   "determinam); a " + azb("OA de curto prazo") + " é positivamente inclinada por rigidezes e "
                   "informação imperfeita."),
        "destrinchando": [
            "Longo prazo: Y* = F(K̄, L*, tecnologia). Preços e salários já se ajustaram por inteiro, de modo que "
            "dobrar P dobra também W e não muda o salário real nem o emprego → OA " + vd("vertical") + ". É a "
            + azb("dicotomia clássica") + ": variáveis nominais não afetam as reais.",
            "Curto prazo: algo impede o ajuste completo, e P maior faz as firmas produzirem mais → OA "
            + vd("positivamente inclinada") + ". Explicações: " + azb("salários rígidos") + " (contratos), "
            + azb("preços rígidos") + " (custos de menu), " + azb("informação imperfeita") + " (Lucas).",
            "A ponte entre os dois é a equação Y = Y* + a(P − P<sup>e</sup>): no curto prazo, P pode diferir do "
            "esperado; no longo, P = P<sup>e</sup> e Y = Y*.",
            "Implicação de política: choques de demanda mexem no produto apenas no curto prazo; no longo, só no "
            "nível de preços. Para elevar Y*, só políticas que mudem fatores e produtividade.",
            "Variante keynesiana extrema: com muito desemprego, a OA de curto prazo é quase horizontal (trecho "
            "keynesiano); perto do pleno emprego, quase vertical.",
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a distinção básica do modelo. O verbo “independe” pode "
                       "assustar, mas é exatamente o que significa curva vertical: Y não muda quando P muda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a oferta agregada varia positivamente com o nível de preços, ao contrário do "
            "curto prazo, em que é vertical.”</i> → ERRADO (inversão dos prazos)",
            "<i>“No longo prazo, a oferta agregada é determinada pelo trabalho, pelo capital e pela "
            "tecnologia.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Curto prazo: relação positiva entre preço e oferta; longo prazo: OA vertical, "
                             "pleno emprego, máxima capacidade dos fatores."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01338
    {
        "id": "ECO-E2-L01338-1", "fonte_ref": "E2-L01338", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB4,
        "rotulo_item": "Item",
        "assertiva": ("A relação entre oferta agregada e preços, no curto prazo, é mais complexa que no âmbito "
                      "microeconômico. Uma das teorias que explicam essa correlação é a da rigidez salarial, que "
                      "expressa a lenta adaptação às mudanças das condições econômicas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A relação entre oferta agregada e preços, no curto prazo, é mais complexa que no âmbito "
                      "microeconômico. <u>Uma das</u> teorias que explicam essa correlação é a da "
                      "<u>rigidez salarial</u>, que expressa a lenta adaptação às mudanças das condições "
                      "econômicas."),
        "poucas": ("Com " + azb("salários nominais rígidos") + " (contratos, convenções), P maior reduz o "
                   "salário real W/P; as firmas contratam e produzem mais → OA de curto prazo " 
                   + vd("positivamente inclinada") + "."),
        "destrinchando": [
            "No micro, a oferta de um bem sobe com o seu preço <b>relativo</b>. No macro, quando todos os preços "
            "sobem juntos, não há mudança relativa — por que a produção total reagiria? A resposta exige alguma "
            "fricção nominal; daí a “complexidade”.",
            "Teoria dos " + azb("salários rígidos") + " (" + oc("Keynes") + "; Mankiw a apresenta como a "
            "primeira das explicações): salários são fixados por contratos de um a três anos, com base no nível "
            "de preços esperado. Se P supera o esperado, W/P cai, o trabalho fica barato e as firmas expandem "
            "emprego e produto.",
            "Em fórmula: Y = Y* + a(P − P<sup>e</sup>). Quando os contratos são renegociados, W acompanha P, o "
            "salário real volta e o produto retorna a Y*.",
            "Outras teorias da mesma família: " + azb("preços rígidos") + " (custos de menu, preços "
            "escalonados) e " + azb("informação imperfeita") + " (Lucas). Todas geram OA inclinada no curto "
            "prazo e vertical no longo.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O “uma das teorias” impede que o item "
                       "seja lido como explicação única. A definição de rigidez salarial é genérica, mas "
                       "correta: lentidão de ajuste dos salários nominais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A única teoria que explica a inclinação positiva da oferta agregada de curto prazo é a da "
            "rigidez salarial.”</i> → ERRADO (restrição indevida: há também preços rígidos e informação "
            "imperfeita)",
            "<i>“Pela teoria da rigidez salarial, um nível de preços acima do esperado reduz o salário real e "
            "eleva o emprego.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["uma das"], "dificuldade": 1,
        "comentario_fonte": ("Pela rigidez salarial, a adaptação a mudanças de preços demora, o que altera a "
                             "produção até novo equilíbrio."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01339
    {
        "id": "ECO-E2-L01339-1", "fonte_ref": "E2-L01339", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB4,
        "rotulo_item": "Item",
        "assertiva": ("O fenômeno da estagflação ocorre quando a demanda agregada sofre um significativo impacto, "
                      "que acarreta aumento de preços e redução da produção."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O fenômeno da estagflação ocorre quando a ") + vm("demanda") + az(" agregada sofre um "
                    "significativo impacto, que acarreta aumento de preços e redução da produção.")),
        "poucas": ("Preços ↑ com produção ↓ é a assinatura de um " + azb("choque adverso de oferta") + " (OA para "
                   "cima/esquerda). Choque de demanda move preço e produto no " + vd("mesmo sentido") + "."),
        "destrinchando": [
            azb("Estagflação") + " = estagnação (ou recessão) + inflação. No OA-DA, só aparece quando a OA de "
            "curto prazo se desloca para a esquerda: o novo equilíbrio tem " + vd("P ↑ e Y ↓") + ".",
            "Um choque de demanda negativo (DA para a esquerda) dá P ↓ e Y ↓ — recessão com desinflação. Um "
            "positivo dá P ↑ e Y ↑ — aquecimento. Nenhum dos dois produz a combinação do item.",
            "Causas típicas: choques do petróleo de " + vd("1973") + " e " + vd("1979") + ", quebras de safra, "
            "desarticulação de cadeias produtivas (pandemia, 2020–2022), espiral salários-preços.",
            "Dilema de política: estimular a demanda recupera o produto, mas sobe ainda mais a inflação; "
            "contraí-la derruba a inflação, mas aprofunda a recessão. É por isso que choques de oferta são os "
            "mais difíceis para os bancos centrais.",
            vm("Regra-âncora: P e Y em sentidos opostos → choque de oferta."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Os efeitos estão certos; trocou-se só a curva que sofre o "
                       "choque. A imprecisão de “significativo impacto” (sem dizer se positivo ou negativo) "
                       "reforça a pista: nenhum choque de demanda gera, sozinho, preço para cima e produto para "
                       "baixo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A estagflação decorre tipicamente de um choque adverso de oferta, como a alta abrupta do preço "
            "do petróleo.”</i> → CERTO",
            "<i>“A estagflação ocorre quando a oferta agregada se expande, reduzindo preços e elevando a "
            "produção.”</i> → ERRADO (sentido trocado)",
        ])],
        "reescrita": ("O fenômeno da estagflação ocorre quando a " + hl("oferta") + " agregada sofre um "
                      "significativo impacto " + hl("adverso") + ", que acarreta aumento de preços e redução da "
                      "produção."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Estagflação: choque adverso na oferta agregada (choque do petróleo), custos maiores, "
                             "menos oferta e preços mais altos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01340
    {
        "id": "ECO-E2-L01340-1", "fonte_ref": "E2-L01340", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_NAB4,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria dos preços rígidos, a inclinação da curva de oferta agregada varia no curto "
                      "prazo por causa dos chamados custos de menu, que consistem no tempo necessário para as "
                      "empresas adaptarem a produção às novas circunstâncias."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Segundo a teoria dos preços rígidos, a inclinação da curva de oferta agregada varia no "
                      "curto prazo por causa dos chamados <u>custos de menu</u>, que consistem no <u>tempo "
                      "necessário para as empresas adaptarem a produção</u> às novas circunstâncias."),
        "poucas": ("A teoria dos " + azb("preços rígidos") + " explica a OA de curto prazo positivamente inclinada "
                   "pelos " + azb("custos de menu") + ". O gabarito oficial é CERTO, mas a definição dada aos "
                   "custos de menu é imprecisa."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "custos de menu são os custos de <b>alterar preços</b> (reimprimir cardápios e "
                          "catálogos, remarcar, informar clientes), não o “tempo necessário para adaptar a "
                          "produção”. Pela definição de manual (" + oc("Mankiw") + "), a segunda oração é falsa, "
                          "e ERRADO seria a resposta mais defensável. Mantido o CERTO da fonte, que parece ter "
                          "julgado só a ideia geral (preços rígidos → OA inclinada no curto prazo).")],
        "destrinchando": [
            "Teoria dos " + azb("preços rígidos") + " (novos-keynesianos — " + oc("Mankiw") + ", " + oc("Akerlof")
            + " e " + oc("Yellen") + ", anos 1980): como mudar preços custa, algumas firmas mantêm o preço fixado "
            "com base no nível de preços esperado. Se a demanda e o nível geral sobem, essas firmas ficam com "
            "preço relativamente baixo, vendem mais e expandem a produção.",
            azb("Custos de menu") + ": todo custo de reajustar preços — físico (etiquetas, cardápios) ou de "
            "decisão e de relação com o cliente. Pequenos para cada firma, podem gerar grandes rigidezes "
            "agregadas (externalidade de demanda agregada).",
            "Outras fontes de rigidez de preço: contratos e " + azb("preços escalonados") + " (Taylor, Calvo), em "
            "que só uma fração das firmas reajusta a cada período.",
            "Quanto maior a fração de firmas com preço rígido, mais " + vd("plana") + " a OA de curto prazo. No "
            "longo prazo, todas reajustam e a OA fica vertical.",
            vm("Regra-âncora: custo de menu = custo de mudar o PREÇO, não a produção."),
        ],
        "dissecando": (cz("[outro: definição imprecisa aceita pela banca · detalhe]") + " A primeira parte "
                       "(preços rígidos → custos de menu → OA inclinada) é a tese correta; o aposto que define "
                       "custos de menu confunde ajuste de preço com ajuste de produção. Em prova CEBRASPE, uma "
                       "definição assim tende a ser o erro do item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Custos de menu são os custos em que a firma incorre ao alterar seus preços, o que pode tornar "
            "os preços rígidos no curto prazo.”</i> → CERTO",
            "<i>“Segundo a teoria dos preços rígidos, a oferta agregada é vertical no curto prazo.”</i> → ERRADO "
            "(é positivamente inclinada; vertical só no longo prazo)",
        ])],
        "tipo_erro": ["OUTRO", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Com mudança das condições, os preços ofertados diferem do esperado; até as empresas "
                             "ajustarem os preços, a produção é afetada."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: custos de menu são custos de alterar preços, não o tempo para adaptar a "
                    "produção; ERRADO seria mais defensável — mantido o CERTO da fonte"],
    },
    # ------------------------------------------------------------------ E2-L01447
    {
        "id": "ECO-E2-L01447-1", "fonte_ref": "E2-L01447", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT1,
        "rotulo_item": "Item",
        "assertiva": ("O choque de oferta provocado pela desarticulação das cadeias globais de valor na pandemia, "
                      "por reduzir a renda e o produto, tende a reduzir a inflação."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O choque de oferta provocado pela desarticulação das cadeias globais de valor na pandemia, ")
                    + vm("por reduzir") + az(" a renda e o produto, tende a ") + vm("reduzir") + az(" a inflação.")),
        "poucas": ("Choque " + azb("adverso de oferta") + " desloca a OA para cima/esquerda: o produto cai, mas "
                   "os preços " + vd("sobem") + ". É estagflação, não desinflação."),
        "destrinchando": [
            "A desarticulação das cadeias (fábricas paradas, falta de semicondutores, contêineres e fretes "
            "caros) eleva o custo de produzir cada unidade: a " + azb("OA de curto prazo") + " se desloca para "
            "a esquerda.",
            "Ao longo da DA inalterada, o novo equilíbrio tem " + vd("Y ↓ e P ↑") + ". Produto e preços "
            "andam em sentidos opostos — marca registrada do choque de oferta.",
            "A queda de renda <b>pela demanda</b> (DA para a esquerda) é que reduz a inflação. O item aplica ao "
            "choque de oferta a lógica do choque de demanda: a redução do produto é consequência do mesmo "
            "deslocamento que eleva os preços, não um freio sobre eles.",
            "Na prática (2020–2022): no início da pandemia predominou o choque de demanda (deflação em vários "
            "setores); depois, os gargalos de oferta, somados aos estímulos, levaram a inflação mundial a "
            "máximas de décadas.",
            vm("Regra-âncora: choque de oferta adverso → Y ↓ e P ↑ (estagflação)."),
        ],
        "grafico_verso": "ECO-E2-L01447-1-V1",
        "dissecando": (cz("[nexo indevido · inversão]") + " A premissa (choque de oferta reduz o produto) é "
                       "verdadeira; o “por reduzir” fabrica uma causalidade que só vale para choques de demanda. "
                       "🔥 A banca adora o encadeamento “menos renda → menos inflação” aplicado ao choque errado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O choque de oferta provocado pela desarticulação das cadeias globais tende a reduzir o produto "
            "e elevar a inflação.”</i> → CERTO",
            "<i>“A queda da demanda no início da pandemia tendeu a reduzir a inflação.”</i> → CERTO",
        ])],
        "reescrita": ("O choque de oferta provocado pela desarticulação das cadeias globais de valor na pandemia, "
                      + hl("embora reduza") + " a renda e o produto, tende a " + hl("elevar") + " a inflação."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Choque adverso de oferta: OA para a esquerda, produto cai e preços sobem "
                             "(estagflação); o item confunde com choque de demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 345", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01447-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01599-1 (mesmo choque das cadeias, versão CERTA)"],
    },
    # ------------------------------------------------------------------ E2-L01448
    {
        "id": "ECO-E2-L01448-1", "fonte_ref": "E2-L01448", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT1,
        "rotulo_item": "Item",
        "assertiva": ("A expansão da demanda pelas políticas monetária e fiscal expansionistas durante a pandemia "
                      "terá eficácia em expandir o produto no curto e no longo prazos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A expansão da demanda pelas políticas monetária e fiscal expansionistas durante a pandemia "
                       "terá eficácia em expandir o produto no curto ") + vm("e no longo prazos") + az(".")),
        "poucas": ("Política de demanda move o produto só no " + vd("curto prazo") + ". No longo, a "
                   + azb("OA é vertical") + " no produto potencial e a expansão vira apenas preços mais altos."),
        "destrinchando": [
            "Curto prazo: a DA vai para a direita ao longo de uma OA positivamente inclinada (rigidezes) → "
            "Y ↑ e P ↑. Com a capacidade ociosa da pandemia, o ganho de produto podia ser grande.",
            "Longo prazo: salários e expectativas se ajustam, a OA de curto prazo sobe e a economia volta a "
            "Y*. O produto potencial depende de " + azb("fatores reais") + " — trabalho, capital, capital "
            "humano, tecnologia — e não da DA.",
            "É a " + azb("neutralidade de longo prazo") + " da moeda (e, no modelo-padrão, da política de "
            "demanda em geral). Para elevar o produto de longo prazo, só políticas estruturais: investimento, "
            "educação, produtividade.",
            "Nuance: correntes que admitem " + azb("histerese") + " (Blanchard e Summers) argumentam que "
            "recessões longas destroem capital e capital humano, de modo que sustentar a demanda pode preservar "
            "o potencial. É exceção discutida, não a resposta-padrão de prova.",
            vm("Regra-âncora: demanda mexe em Y no curto prazo; no longo prazo, só em P."),
        ],
        "dissecando": (cz("[meia-verdade]") + " Acerta o curto prazo e estende o efeito ao longo "
                       "prazo, onde a OA é vertical. Pista: “no curto e no longo prazos” é a fórmula clássica da "
                       "banca para enxertar o erro na segunda metade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A expansão da demanda durante a pandemia teve eficácia em expandir o produto no curto prazo, "
            "mas, no longo prazo, tende a afetar apenas o nível de preços.”</i> → CERTO",
            "<i>“Políticas de demanda são ineficazes para alterar o produto mesmo no curto prazo.”</i> → ERRADO "
            "(no curto prazo, com OA inclinada, elas alteram Y)",
        ])],
        "reescrita": ("A expansão da demanda pelas políticas monetária e fiscal expansionistas durante a pandemia "
                      "terá eficácia em expandir o produto no curto " + hl("prazo, mas não no longo") + "."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Política de demanda pode expandir o produto no curto prazo; no longo prazo, OA "
                             "vertical, só preços mudam."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 346", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01449
    {
        "id": "ECO-E2-L01449-1", "fonte_ref": "E2-L01449", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT1,
        "rotulo_item": "Item",
        "assertiva": ("A existência de elevado desemprego e capacidade ociosa geradas pela pandemia aumenta a "
                      "elasticidade da curva de oferta agregada de curto prazo, reduzindo os impactos das políticas "
                      "econômicas expansionistas sobre a inflação."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A existência de elevado desemprego e capacidade ociosa geradas pela pandemia <u>aumenta a "
                      "elasticidade</u> da curva de oferta agregada de curto prazo, <u>reduzindo</u> os impactos "
                      "das políticas econômicas expansionistas sobre a inflação."),
        "poucas": ("Com trabalhadores e máquinas parados, as firmas expandem a produção sem pressionar custos: a "
                   + azb("OA de curto prazo") + " fica mais " + vd("plana (elástica)") + ", e a expansão da DA "
                   "vira mais produto e menos preço."),
        "destrinchando": [
            "A inclinação da OA de curto prazo depende do grau de utilização da capacidade. Longe do pleno "
            "emprego, contratar mais e usar máquinas ociosas quase não eleva o custo marginal → OA quase "
            "horizontal (o “trecho keynesiano”). Perto do pleno emprego, gargalos e salários em alta → OA quase "
            "vertical.",
            "Elasticidade alta = Y reage muito a P. Quando a DA se desloca para a direita, a divisão do efeito "
            "entre " + vd("ΔY") + " e " + vd("ΔP") + " depende dessa inclinação: OA plana → muito ΔY, pouco ΔP.",
            "Na curva de Phillips, o mesmo raciocínio: com " + azb("hiato do produto") + " negativo grande "
            "(desemprego acima da NAIRU), o estímulo reduz o desemprego com pouca pressão inflacionária.",
            "Nuance da pandemia: a ociosidade conviveu com gargalos setoriais de oferta (chips, logística), o "
            "que explica a inflação de 2021–2022 mesmo com desemprego ainda alto em alguns países.",
            vm("Regra-âncora: ociosidade → OA plana → política de demanda rende produto, não inflação."),
        ],
        "grafico_verso": "ECO-E2-L01449-1-V1",
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " Item correto, mas o vocabulário confunde: "
                       "“aumenta a elasticidade” = curva mais <b>horizontal</b>. Quem associa elasticidade a "
                       "“mais reação de preços” marca ERRADO. Teste rápido: elasticidade da OA = quanto a "
                       "quantidade ofertada reage ao preço."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com elevada capacidade ociosa, a oferta agregada de curto prazo é mais inclinada, e as políticas "
            "expansionistas geram sobretudo inflação.”</i> → ERRADO (inversão: OA mais plana, mais produto)",
            "<i>“Próximo ao pleno emprego, uma expansão da demanda agregada tende a gerar mais inflação e menos "
            "produto.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Desemprego e capacidade ociosa tornam a OA de curto prazo mais elástica (horizontal); "
                             "políticas expansionistas resultam mais em produto e menos em inflação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01558
    {
        "id": "ECO-E2-L01558-1", "fonte_ref": "E2-L01558", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT2,
        "rotulo_item": "Item",
        "assertiva": ("Se os salários nominais fossem mais flexíveis, uma política monetária expansionista seria "
                      "mais eficaz em reduzir a taxa de desemprego."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se os salários nominais fossem mais flexíveis, uma política monetária expansionista seria ")
                    + vm("mais") + az(" eficaz em reduzir a taxa de desemprego.")),
        "poucas": ("A política monetária afeta o emprego <b>porque</b> os salários nominais são rígidos. Com "
                   "salários " + azb("flexíveis") + ", W acompanha P, o salário real não cai e a moeda se "
                   "aproxima da " + vd("neutralidade") + ": eficácia " + vd("menor") + "."),
        "destrinchando": [
            "Mecanismo com rigidez: M ↑ → DA ↑ → P ↑; com W fixo por contrato, " + vd("W/P cai") + ", o trabalho "
            "fica mais barato, as firmas contratam e o desemprego cai (abaixo do natural, temporariamente).",
            "Mecanismo com flexibilidade: W sobe junto com P, o salário real fica igual, emprego e produto não "
            "mudam. A OA de curto prazo fica mais " + azb("íngreme") + " — no limite, vertical — e o estímulo "
            "vira só inflação.",
            "Na curva de Phillips: salários mais flexíveis (ou indexados) tornam a curva de curto prazo mais "
            "inclinada — o trade-off inflação × desemprego piora.",
            "Mesma lógica nas teorias rivais: no modelo de " + oc("Lucas") + ", só surpresas monetárias têm "
            "efeito real; nos novos-keynesianos, a não neutralidade vem das rigidezes nominais.",
            "Ironia útil para discursiva: flexibilidade salarial ajuda a economia a se reequilibrar sozinha "
            "após choques, mas tira potência da política monetária.",
        ],
        "dissecando": (cz("[inversão]") + " Inverte a relação entre rigidez e eficácia. Armadilha de senso "
                       "comum: “mercado mais flexível funciona melhor” — verdade para o ajuste espontâneo, falso "
                       "para a eficácia da política monetária, que vive da rigidez."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se os salários nominais fossem perfeitamente flexíveis, a política monetária expansionista não "
            "alteraria o desemprego, apenas o nível de preços.”</i> → CERTO",
            "<i>“A indexação plena dos salários à inflação passada amplia o efeito da política monetária sobre o "
            "emprego.”</i> → ERRADO (inversão: reduz)",
        ])],
        "reescrita": ("Se os salários nominais fossem mais flexíveis, uma política monetária expansionista seria "
                      + hl("menos") + " eficaz em reduzir a taxa de desemprego."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Rigidez salarial é o que dá efeito real à política monetária; com salários "
                             "flexíveis, ajuste rápido e menor eficácia sobre o desemprego."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 429", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01559
    {
        "id": "ECO-E2-L01559-1", "fonte_ref": "E2-L01559", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT2,
        "rotulo_item": "Item",
        "assertiva": ("Se a autoridade monetária decidir acomodar um choque de oferta adverso, minimizará os efeitos "
                      "recessivos sobre o produto e o emprego, mas intensificará os efeitos inflacionários da "
                      "política monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se a autoridade monetária decidir <u>acomodar</u> um choque de oferta adverso, minimizará "
                      "os efeitos recessivos sobre o produto e o emprego, mas <u>intensificará os efeitos "
                      "inflacionários</u> da política monetária."),
        "poucas": ("" + azb("Acomodar") + " = expandir a moeda para deslocar a DA para a direita e compensar a "
                   "queda de produto do choque. O produto se preserva, mas o nível de preços sobe " 
                   + vd("ainda mais") + "."),
        "destrinchando": [
            "O choque adverso desloca a OA de curto prazo para a esquerda: " + vd("P ↑ e Y ↓") + " "
            "(estagflação). O banco central escolhe entre duas respostas.",
            "Não acomodar (ou apertar): mantém a DA, aceita a recessão; com o tempo, salários e custos cedem, a "
            "OA volta e os preços recuam — custo em produto e emprego.",
            azb("Acomodar") + ": política monetária expansionista leva a DA para a direita e o produto de volta "
            "ao potencial — mas o nível de preços fica permanentemente mais alto. É o “dilema da "
            "estabilização”: diante de choque de oferta, não se estabilizam preço e produto ao mesmo tempo.",
            "Risco da acomodação: validar a alta de preços pode desancorar expectativas e gerar " + azb("efeitos "
            "de segunda ordem") + " (salários reajustados, espiral). Por isso bancos centrais com metas de "
            "inflação costumam “olhar através” só do impacto direto de choques temporários.",
            vm("Regra-âncora: choque de oferta + acomodação → produto preservado, inflação maior."),
        ],
        "grafico_verso": "ECO-E2-L01559-1-V1",
        "dissecando": (cz("[literalidade]") + " Descreve o trade-off-padrão da acomodação. A expressão final "
                       "(“efeitos inflacionários da política monetária”) é estranha — o choque já é inflacionário "
                       "e a política acrescenta inflação —, mas não altera o sentido."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao acomodar um choque de oferta adverso, a autoridade monetária neutraliza tanto a recessão "
            "quanto a inflação.”</i> → ERRADO (impossível estabilizar os dois)",
            "<i>“Se a autoridade monetária não acomodar o choque de oferta adverso, o produto tende a cair mais, "
            "com inflação menor.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Acomodar = expansão monetária que desloca a DA para a direita; menos recessão, mais "
                             "inflação; trade-off entre estabilização do produto e dos preços."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 430", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada e ampliada com a acomodação (ECO-E2-L01559-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01601-1 (mesma ideia, outra questão do mesmo curso)"],
    },
    # ------------------------------------------------------------------ E2-L01599
    {
        "id": "ECO-E2-L01599-1", "fonte_ref": "E2-L01599", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT3,
        "rotulo_item": "Item",
        "assertiva": ("A desarticulação das cadeias produtivas globais levou a aumentos de custos, o que tende a "
                      "deslocar a curva de oferta agregada para cima e para esquerda, gerando inflação de oferta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A desarticulação das cadeias produtivas globais levou a aumentos de custos, o que tende a "
                      "deslocar a curva de oferta agregada <u>para cima e para esquerda</u>, gerando <u>inflação "
                      "de oferta</u>."),
        "poucas": ("Custos maiores a cada nível de produto = " + azb("OA para cima/esquerda") + " → P ↑ e Y ↓: "
                   + vd("inflação de oferta (de custos)") + "."),
        "destrinchando": [
            "Na pandemia, lockdowns, escassez de semicondutores, falta de contêineres e fretes até várias vezes "
            "mais caros elevaram o custo de produzir e entregar bens. Os índices de preços ao produtor subiram "
            "antes dos preços ao consumidor.",
            "“Para cima” e “para a esquerda” descrevem o mesmo deslocamento: cada quantidade passa a exigir "
            "preço maior (cima); a cada preço, oferta-se menos (esquerda).",
            "Resultado no OA-DA: " + vd("P ↑ e Y ↓") + " — a " + azb("inflação de custos") + ", distinta da de "
            "demanda (P ↑ com Y ↑).",
            "O surto inflacionário de 2021–2022 combinou os dois: gargalos de oferta + demanda sustentada por "
            "estímulos fiscais e monetários e pela migração do consumo de serviços para bens. Daí o comando "
            "falar em “elementos de oferta e de demanda”.",
            vm("Regra-âncora: choque de custo → OA para cima/esquerda → inflação de oferta com queda do produto."),
        ],
        "dissecando": (cz("[literalidade]") + " Encadeamento correto (custo → OA → inflação de oferta). A "
                       "dupla direção “para cima e para esquerda” é proposital: quem pensa que são movimentos "
                       "diferentes desconfia do item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o que tende a deslocar a curva de demanda agregada para a esquerda, gerando inflação de "
            "demanda.”</i> → ERRADO (troca de curva e de tipo de inflação)",
            "<i>“…gerando inflação de oferta, acompanhada de redução do produto.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Desarticulação das cadeias eleva custos; choque de oferta negativo; OA para cima e "
                             "para a esquerda; inflação de custos com estagnação."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 454", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (conteúdo absorvido no 📖)"},
                          {"ref": "IMAGEM 455", "tipo_fonte": "DIAGRAMA", "lado": "verso", "acao": "cortada"}],
        "alertas": ["quase_duplicata: ECO-E2-L01447-1 (mesmo choque, versão ERRADA)"],
    },
    # ------------------------------------------------------------------ E2-L01600
    {
        "id": "ECO-E2-L01600-1", "fonte_ref": "E2-L01600", "destino": "28", "subtema": H28["da"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT3,
        "rotulo_item": "Item",
        "assertiva": ("As políticas monetárias e fiscais expansionistas adotadas durante a pandemia têm como efeito "
                      "elevar a inflação, o que acaba por reduzir a demanda agregada da economia, visto que esta é "
                      "negativamente inclinada com os preços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As políticas monetárias e fiscais expansionistas adotadas durante a pandemia têm como "
                       "efeito elevar a inflação, o que ") + vm("acaba por reduzir a demanda agregada da economia")
                    + az(", visto que esta é negativamente inclinada com os preços.")),
        "poucas": ("Políticas expansionistas " + azb("deslocam") + " a DA para a direita. A alta de preços que "
                   "resulta é " + azb("movimento ao longo") + " da DA (menor quantidade demandada), não redução "
                   "da demanda agregada."),
        "destrinchando": [
            "A DA é negativamente inclinada por três efeitos: " + azb("riqueza") + " (Pigou: P ↑ reduz o valor "
            "real dos saldos), " + azb("juros") + " (Keynes: P ↑ reduz M/P e eleva i) e " + azb("câmbio real") 
            + " (P ↑ encarece as exportações).",
            "Isso descreve o que acontece com a quantidade demandada quando P muda <b>tudo o mais constante</b>. "
            "Políticas fiscais e monetárias mudam o “tudo o mais”: deslocam a curva inteira.",
            "Sequência correta: estímulo → DA para a direita → P ↑ e Y ↑ ao longo da OA. A parte do estímulo "
            "“absorvida” pela alta de preços aparece como movimento ao longo da nova DA, mas o resultado "
            "líquido continua sendo demanda maior que a inicial.",
            "Mesma distinção da microeconomia: “variação da demanda” (deslocamento) × “variação da quantidade "
            "demandada” (movimento ao longo).",
            vm("Regra-âncora: P muda → anda-se na DA; política muda → a DA anda."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Usa um fato verdadeiro (DA negativamente "
                       "inclinada) para justificar uma conclusão falsa (a inflação “reduz a demanda agregada”), "
                       "confundindo deslocamento com movimento ao longo da curva. Pista: “visto que” costuma "
                       "colar uma justificativa verdadeira a uma conclusão errada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As políticas expansionistas deslocam a demanda agregada para a direita; a alta de preços "
            "resultante reduz a quantidade demandada ao longo da curva.”</i> → CERTO",
            "<i>“A curva de demanda agregada é negativamente inclinada, entre outros motivos, pelo efeito dos "
            "preços sobre os saldos monetários reais.”</i> → CERTO",
        ])],
        "reescrita": ("As políticas monetárias e fiscais expansionistas adotadas durante a pandemia têm como efeito "
                      "elevar a inflação, o que " + hl("reduz apenas a quantidade demandada, ao longo da curva, sem "
                      "anular o deslocamento da demanda agregada para a direita") + ", visto que esta é "
                      "negativamente inclinada com os preços."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["acaba por"], "dificuldade": 2,
        "comentario_fonte": ("Expansionistas deslocam a DA para a direita; a inflação é movimento ao longo da "
                             "curva, não redução da demanda; confusão entre deslocamento e movimento."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 456", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (acomodação de choque; não trata do item)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01601
    {
        "id": "ECO-E2-L01601-1", "fonte_ref": "E2-L01601", "destino": "28", "subtema": H28["oa"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT3,
        "rotulo_item": "Item",
        "assertiva": ("Diante de uma retração na oferta, o BC pode focar em estimular a atividade econômica, "
                      "acomodando o produto e emprego, porém ao custo de uma inflação ainda mais alta."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Diante de uma retração na oferta, o BC <u>pode</u> focar em estimular a atividade "
                      "econômica, acomodando o produto e emprego, porém <u>ao custo de uma inflação ainda mais "
                      "alta</u>."),
        "poucas": ("Diante de choque de oferta, o BC escolhe: " + azb("acomodar") + " (estimular a DA, preservar "
                   "produto e emprego, " + vd("mais inflação") + ") ou combater a inflação (apertar, " 
                   + vd("mais recessão") + "). O item descreve a primeira opção."),
        "destrinchando": [
            "Retração da oferta: OA de curto prazo para a esquerda → P ↑ e Y ↓. Não existe resposta de demanda "
            "que desfaça os dois efeitos ao mesmo tempo.",
            "Opção 1 — acomodar: juros mais baixos/moeda maior → DA para a direita → Y volta para perto do "
            "potencial, " + vd("P sobe mais") + " do que subiria com o choque sozinho.",
            "Opção 2 — combater: juros mais altos → DA para a esquerda → inflação menor, " + vd("recessão "
            "maior") + ". Foi a escolha de " + oc("Volcker") + " no Fed (1979–1982) diante do segundo choque do "
            "petróleo.",
            "Em 2021–2022, a maioria dos bancos centrais começou acomodando (tratando os gargalos como "
            "transitórios) e depois apertou fortemente. O " + rx("Banco Central do Brasil") + " foi dos "
            "primeiros a subir juros, a partir de " + vd("março de 2021") + ".",
            vm("Regra-âncora: choque de oferta impõe o dilema — produto ou preços, não os dois."),
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O “pode” transforma o item em descrição de "
                       "uma opção possível, não de uma recomendação. O “porém ao custo” explicita o trade-off. "
                       "Seria ERRADO se dissesse que o BC estabiliza produto e inflação ao mesmo tempo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Diante de uma retração na oferta, o BC pode estimular a atividade e, ao mesmo tempo, reduzir a "
            "inflação.”</i> → ERRADO (o dilema impede os dois)",
            "<i>“Diante de uma retração na oferta, o BC pode priorizar a inflação, ao custo de queda maior do "
            "produto.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Dilema do BC diante de choque de oferta: acomodar (emprego, mais inflação) ou "
                             "combater (inflação, mais recessão); o item descreve a primeira opção."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01559-1 (mesma ideia, outra questão do mesmo curso)"],
    },
]
