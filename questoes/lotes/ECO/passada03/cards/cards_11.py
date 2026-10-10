"""Cards do lote de redação 11 — ECO, passada 03 (nota 70: modelo IS-LM-BP / Mundell-Fleming)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "bp": "📍 Curva BP e mobilidade de capital",
    "fixo": "🔒 Câmbio fixo",
    "flut": "🌊 Câmbio flutuante",
}

CMD_MF = "Julgue o item a seguir, relativo ao modelo IS-LM-BP (Mundell-Fleming)."

CMD_BOZAN_1 = ("Considerando o modelo IS-LM-BP e as inter-relações entre os mercados de bens, monetário e cambial, "
               "julgue a assertiva a seguir.")

CMD_BOZAN_2 = ("Considere o modelo IS-LM-BP em diferentes contextos de mobilidade de capitais e regimes cambiais. "
               "Julgue se a assertiva a seguir é verdadeira (Certo) ou falsa (Errado).")

CMD_BOZAN_3 = ("Com base no modelo IS-LM, julgue a assertiva a seguir sobre o impacto das políticas econômicas em "
               "regimes de câmbio fixo e flutuante, sob perfeita mobilidade de capitais.")

CMD_BOZAN_4 = ("Analisando os cenários de mobilidade de capitais e suas implicações sobre políticas monetárias e "
               "fiscais em regimes de câmbio fixo e flutuante, julgue a assertiva a seguir.")

CMD_NAB_ABERTA = "Acerca de macroeconomia aberta e sistema monetário internacional, julgue o item a seguir."

FIG_VERSO_DIDATICA = "redesenhada como gráfico didático do verso"

CARDS = [
    # ------------------------------------------------------------------ E1-0881
    {
        "id": "ECO-E1-0881-1", "fonte_ref": "E1-0881", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                      "fiscal reduz o nível da taxa de juros."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                       "fiscal ") + vm("reduz") + az(" o nível da taxa de juros.")),
        "poucas": ("A expansão fiscal desloca a IS para a direita e " + azb("eleva") + " os juros; com baixa "
                   "mobilidade e câmbio fixo, a defesa da paridade ainda contrai a moeda e empurra os juros "
                   + vm("mais para cima") + "."),
        "destrinchando": [
            "Com " + azb("baixa mobilidade de capital") + ", a curva BP é " + vd("mais inclinada que a LM")
            + ": para atrair capital suficiente e cobrir o déficit comercial gerado por uma renda maior, os juros "
            "precisam subir muito.",
            "Sequência: G ↑ → IS para a direita → Y ↑ e i ↑ (ponto provisório E′). A renda maior eleva as "
            "importações, e a pouca entrada de capital não compensa: surge " + azb("déficit no balanço de "
            "pagamentos") + " (E′ fica à direita da BP).",
            "Para manter o câmbio fixo, o Banco Central " + vd("vende reservas") + " e recolhe moeda doméstica: "
            "a base monetária cai e a LM se desloca para a " + vd("esquerda") + " até encontrar IS₂ sobre a BP.",
            "Resultado final: " + vd("i ↑ (mais que no ponto provisório)") + " e " + vd("Y ↑ pouco") + ". A "
            "política fiscal funciona, mas com eficácia limitada — tanto menor quanto mais vertical a BP (no "
            "limite, capitais imóveis, a renda não muda).",
            "Contraste: com " + azb("alta mobilidade") + " (BP menos inclinada que a LM), o mesmo choque gera "
            "superávit, o BC compra divisas, a LM vai para a direita e a fiscal fica mais forte. Em nenhum dos "
            "casos os juros caem.",
            vm("Regra-âncora: em câmbio fixo, a mobilidade decide para que lado a LM “acompanha” a IS — baixa "
               "mobilidade → LM à esquerda; alta → LM à direita."),
        ],
        "grafico_verso": "ECO-E1-0881-1-V1",
        "dissecando": (cz("[inversão]") + " Troca o sinal do efeito sobre os juros. A expansão fiscal só eleva "
                       "juros no IS-LM-BP (ou os mantém em i*, no caso-limite de mobilidade perfeita); nenhum "
                       "arranjo de mobilidade e regime faz a IS para a direita derrubar os juros."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma expansão fiscal provoca perda de reservas internacionais.”</i> → CERTO",
            "<i>“…uma expansão fiscal provoca deslocamento da LM para a direita.”</i> → ERRADO (sentido trocado: "
            "com baixa mobilidade, a LM vai para a esquerda)",
        ])],
        "reescrita": ("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                      "fiscal " + hl("eleva") + " o nível da taxa de juros."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A expansão fiscal eleva a demanda agregada e desloca a IS para a direita, o "
                             "que tende a elevar a taxa de juros. Segue texto sobre entrada de capital especulativo "
                             "e valorização da moeda."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "Untitled (121).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; " + FIG_VERSO_DIDATICA + ")"}],
        "alertas": ["qualidade_fonte: o comentário de origem descreve entrada de capital e valorização da moeda, "
                    "mecanismo de alta mobilidade; com baixa mobilidade, a expansão fiscal gera déficit externo e "
                    "pressão de desvalorização — corrigido"],
    },
    # ------------------------------------------------------------------ E1-0882
    {
        "id": "ECO-E1-0882-1", "fonte_ref": "E1-0882", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                      "fiscal provoca deslocamento de LM para a direita."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                       "fiscal provoca deslocamento de LM para a ") + vm("direita") + az(".")),
        "poucas": ("Com baixa mobilidade, a expansão fiscal gera " + azb("déficit externo") + "; o BC vende "
                   "reservas para defender o câmbio, a moeda encolhe e a LM vai para a " + vm("esquerda") + "."),
        "destrinchando": [
            "Choque inicial: a política fiscal mexe na " + azb("IS") + " (para a direita). A LM só se move depois, "
            "como reflexo da intervenção cambial — em câmbio fixo, a oferta de moeda é " + azb("endógena") + ".",
            "Para que lado ela se move depende do saldo do " + azb("balanço de pagamentos") + " no ponto "
            "provisório. Com " + vd("baixa mobilidade") + " (BP mais inclinada que a LM), a renda maior puxa as "
            "importações mais do que os juros maiores atraem capital: " + vd("déficit") + ".",
            "Déficit → excesso de demanda por divisas → pressão de desvalorização → BC " + vd("vende dólares e "
            "recolhe reais") + " → base monetária ↓ → LM para a " + vd("esquerda") + ".",
            "Com " + vd("alta mobilidade") + " (BP menos inclinada que a LM), ocorre o contrário: superávit, BC "
            "compra dólares, emite reais e a LM vai para a direita, reforçando a fiscal.",
            "Por isso o mesmo item tem gabaritos opostos conforme a mobilidade: decorar “em câmbio fixo a LM "
            "acompanha a IS para a direita” só vale para mobilidade alta ou perfeita.",
            vm("Regra-âncora: em câmbio fixo, compare as inclinações — BP mais inclinada que a LM → déficit → "
               "LM à esquerda."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item aplica à baixa mobilidade o ajuste típico "
                       "da mobilidade alta (BC comprando divisas e expandindo a moeda). A pista é a premissa "
                       "“baixa mobilidade de capital”, que muda o sinal do saldo externo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com perfeita mobilidade de capital e câmbio fixo, uma expansão fiscal provoca deslocamento de LM "
            "para a direita.”</i> → CERTO",
            "<i>“…com baixa mobilidade de capital e câmbio fixo, a expansão fiscal eleva as reservas "
            "internacionais.”</i> → ERRADO (inversão: as reservas caem)",
        ])],
        "reescrita": ("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                      "fiscal provoca deslocamento de LM para a " + hl("esquerda") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("ERRADO. Inicialmente, a expansão fiscal desloca a IS; a LM só se desloca para a "
                             "direita depois, como consequência da intervenção do BC (comprando moeda estrangeira)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem afirma que a LM se desloca depois para a direita "
                    "(BC comprando divisas); com baixa mobilidade, o BC vende divisas e a LM vai para a esquerda — "
                    "corrigido"],
    },
    # ------------------------------------------------------------------ E1-0883
    {
        "id": "ECO-E1-0883-1", "fonte_ref": "E1-0883", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                      "fiscal movimenta IS para a esquerda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                       "fiscal movimenta IS para a ") + vm("esquerda") + az(".")),
        "poucas": ("Expansão fiscal (G ↑ ou T ↓) aumenta a demanda agregada a cada taxa de juros: a IS vai para a "
                   + azb("direita") + ", qualquer que seja o regime cambial ou a mobilidade."),
        "destrinchando": [
            "A " + azb("curva IS") + " reúne os pares (Y, i) que equilibram o mercado de bens: Y = C(Y − T) + "
            "I(i) + G + NX(e, Y). Mais G, ou menos T, eleva a demanda a cada i → a curva se desloca para a "
            + vd("direita") + ".",
            "Regime cambial e mobilidade de capital não mudam esse <b>impacto</b>; mudam o <b>ajuste</b> que vem "
            "depois. Com baixa mobilidade e câmbio fixo: déficit externo → BC vende reservas → LM para a "
            "esquerda → juros sobem bastante e a renda sobe pouco.",
            "No câmbio flutuante, a IS pode voltar parcialmente (alta mobilidade: valorização reduz NX) ou "
            "avançar ainda mais (baixa mobilidade: desvalorização eleva NX) — mas o primeiro movimento é sempre "
            "para a direita.",
            "O que desloca a IS para a esquerda: contração fiscal, queda da confiança e do investimento autônomo, "
            "valorização cambial (NX ↓), recessão no exterior.",
            vm("Regra-âncora: fiscal expansionista → IS à direita; o regime cambial só decide o que a LM (ou o "
               "câmbio) faz depois."),
        ],
        "dissecando": (cz("[inversão]") + " Item de sentido puro: a banca enche o enunciado de premissas (baixa "
                       "mobilidade, câmbio fixo) que não interferem no deslocamento inicial, apostando que o "
                       "candidato se perca no ajuste e esqueça o básico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma expansão fiscal desloca a IS para a direita e, no ajuste, a LM para a esquerda.”</i> → CERTO",
            "<i>“…uma expansão fiscal desloca a BP para a direita.”</i> → ERRADO (troca de curva: a fiscal mexe na "
            "IS; a BP se desloca com o câmbio real ou com os juros externos)",
        ])],
        "reescrita": ("Considerando um modelo IS-LM-BP com baixa mobilidade de capital e câmbio fixo: uma expansão "
                      "fiscal movimenta IS para a " + hl("direita") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ERRADO. A expansão fiscal sempre desloca a IS para a direita, pois aumenta a demanda "
                            "agregada.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (120).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; conteúdo refeito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0884
    {
        "id": "ECO-E1-0884-1", "fonte_ref": "E1-0884", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta com perfeita mobilidade de capitais, segundo o modelo Mundell-Fleming: "
                      "a curva IS, em uma política monetária expansionista, sofre impacto inicial da queda da taxa "
                      "de juros e, na sequência, impacto da desvalorização cambial, com câmbio flexível."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia aberta com perfeita mobilidade de capitais, segundo o modelo Mundell-Fleming: "
                      "a curva IS, em uma política monetária expansionista, sofre <u>impacto inicial da queda da taxa "
                      "de juros</u> e, <u>na sequência, impacto da desvalorização cambial</u>, com câmbio flexível."),
        "poucas": ("É a sequência do Mundell-Fleming: a expansão monetária derruba os juros (movimento " + azb("ao "
                   "longo") + " da IS) e, em seguida, a saída de capitais deprecia o câmbio, eleva NX e " + azb("desloca")
                   + " a IS para a direita."),
        "destrinchando": [
            "1º elo — " + azb("canal dos juros") + ": M ↑ → LM para a direita → i cai abaixo de i* → o investimento "
            "reage e a economia desce ao longo da IS. É o efeito da economia fechada.",
            "2º elo — " + azb("canal do câmbio") + ": com i < i* e mobilidade perfeita, há fuga de capitais; no "
            "câmbio flexível, a moeda doméstica se " + vd("deprecia") + ", as exportações sobem, as importações "
            "caem e NX ↑ → a IS se desloca para a " + vd("direita") + ".",
            "Equilíbrio final: a IS anda até cruzar a nova LM sobre a BP horizontal → " + vd("i = i*") + ", "
            + vd("Y ↑ muito") + ", câmbio depreciado. É o caso de " + azb("máxima eficácia da política "
            "monetária") + ".",
            "Rigor de vocabulário: a queda de juros, sozinha, é movimento ao longo da IS (i é variável do eixo); "
            "quem desloca a curva é a desvalorização, via NX. O item fala em “impacto” sobre a IS, o que cobre os "
            "dois efeitos.",
            "A eficácia supõe a " + azb("condição de Marshall-Lerner") + " (|ε<sub>X</sub>| + |ε<sub>M</sub>| > 1): "
            "só assim a depreciação melhora o saldo comercial.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item descreve a ordem dos canais (juros primeiro, câmbio "
                       "depois). O risco está em achar que a IS “não se mexe” com política monetária — vale na "
                       "economia fechada, não no Mundell-Fleming com câmbio flexível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com câmbio fixo, a curva IS sofre, na sequência, impacto da desvalorização cambial.”</i> → "
            "ERRADO (no câmbio fixo não há desvalorização: o BC vende reservas e a LM volta)",
            "<i>“…a desvalorização cambial desloca a IS para a esquerda.”</i> → ERRADO (sentido trocado: NX ↑ "
            "desloca a IS para a direita)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. Em câmbio flutuante, a política monetária expansionista reduz os juros, "
                             "provocando saída de capitais e desvalorização cambial, o que estimula as exportações "
                             "líquidas e desloca a IS para a direita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "Untitled (122).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (imagem do verso não preservada; conteúdo refeito no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00143-1, ECO-E2-L00160-1 (mesmo mecanismo: expansão monetária sob "
                    "câmbio flutuante e mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E1-0885
    {
        "id": "ECO-E1-0885-1", "fonte_ref": "E1-0885", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta com perfeita mobilidade de capitais, segundo o modelo Mundell-Fleming: "
                      "uma ação monetária contracionista, com câmbio flexível, não altera a curva LM, que é "
                      "vertical, portanto, deixando inalterados a curva IS e o nível do produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em uma economia aberta com perfeita mobilidade de capitais, segundo o modelo Mundell-Fleming: "
                       "uma ação monetária contracionista, com câmbio flexível, ") + vm("não altera")
                    + az(" a curva LM, que é vertical, portanto, ")
                    + vm("deixando inalterados a curva IS e o nível do produto") + az(".")),
        "poucas": ("Com câmbio flexível e mobilidade perfeita, a política monetária é " + azb("muito eficaz")
                   + ": a contração desloca a LM para a esquerda, aprecia o câmbio, derruba NX e " + vm("reduz o "
                   "produto") + "."),
        "destrinchando": [
            "Mecanismo: M ↓ → LM para a esquerda → i sobe acima de i* → entrada de capitais → " + vd("apreciação")
            + " → exportações ↓, importações ↑ → NX ↓ → IS para a esquerda. Final: " + vd("i = i*") + ", "
            + vd("Y ↓") + ", câmbio apreciado.",
            "Sobre a “LM vertical”: no Mundell-Fleming de " + oc("Mankiw") + ", desenhado no plano renda × câmbio "
            "(Y, e), a LM* é de fato vertical, porque com i = i* a demanda por moeda só fixa um nível de renda. "
            "Mas ser vertical não a torna imóvel: menos moeda a desloca para a " + vd("esquerda") + " e a renda "
            "cai, com apreciação ao longo da IS*.",
            "No plano (Y, i) do IS-LM-BP, a LM é crescente e a BP é horizontal em i*; o mesmo resultado aparece "
            "como LM e IS deslocadas para a esquerda.",
            "Política monetária só fica “sem efeito” sobre a renda no Mundell-Fleming com " + azb("câmbio fixo")
            + " (o BC desfaz a contração comprando divisas) — é o regime que o item trocou.",
            vm("Regra-âncora: câmbio flexível + mobilidade perfeita → política monetária forte, fiscal nula."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item usa uma meia-lembrança verdadeira (LM* "
                       "vertical no gráfico de Mankiw) para concluir algo falso (curva imóvel, produto inalterado) "
                       "e, de quebra, atribui ao câmbio flexível a ineficácia monetária que é do câmbio fixo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma ação monetária contracionista, com câmbio fixo, deixa inalterado o nível do produto.”</i> → "
            "CERTO",
            "<i>“…uma ação monetária contracionista, com câmbio flexível, reduz o produto e deprecia o "
            "câmbio.”</i> → ERRADO (sentido do câmbio trocado: ele se aprecia)",
        ])],
        "reescrita": ("Em uma economia aberta com perfeita mobilidade de capitais, segundo o modelo Mundell-Fleming: "
                      "uma ação monetária contracionista, com câmbio flexível, " + hl("desloca para a esquerda")
                      + " a curva LM, que é vertical, portanto, " + hl("reduzindo o nível do produto, com apreciação "
                      "cambial") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("ERRADO. A LM no Mundell-Fleming não é vertical. A contração monetária eleva os juros, "
                             "valoriza o câmbio, reduz as exportações líquidas, desloca a IS para a esquerda e reduz "
                             "o produto."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem afirma que a LM no Mundell-Fleming não é vertical; na "
                    "versão de Mankiw, no plano (Y, e), a LM* é vertical — o erro do item é dizer que ela não se "
                    "desloca. Nuance incorporada"],
    },
    # ------------------------------------------------------------------ E1-0888
    {
        "id": "ECO-E1-0888-1", "fonte_ref": "E1-0888", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em um país pequeno, com mobilidade perfeita de capitais, segundo o modelo Mundell-Fleming, uma "
                      "política fiscal expansionista com regime de câmbio fixo será eficaz para elevar o produto, "
                      "sendo que, no processo de ajuste, a ação do Banco Central ampliará a efetividade da política "
                      "fiscal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um país pequeno, com mobilidade perfeita de capitais, segundo o modelo Mundell-Fleming, uma "
                      "política fiscal expansionista com regime de câmbio fixo será <u>eficaz</u> para elevar o "
                      "produto, sendo que, no processo de ajuste, a ação do Banco Central <u>ampliará</u> a "
                      "efetividade da política fiscal."),
        "poucas": ("Câmbio fixo + mobilidade perfeita = " + azb("fiscal com eficácia máxima") + ": para impedir a "
                   "valorização, o BC compra divisas, emite moeda e a LM acompanha a IS, sem crowding out."),
        "destrinchando": [
            "G ↑ → IS para a direita → pressão de alta nos juros (i > i*) → entrada maciça de capitais → pressão "
            "de " + vd("valorização") + " da moeda doméstica.",
            "Para sustentar a paridade, o BC " + vd("compra dólares") + " e paga com moeda nova: reservas ↑, base "
            "monetária ↑, " + vd("LM para a direita") + ". É uma expansão monetária " + azb("endógena") + ", "
            "ditada pela defesa do câmbio.",
            "O ajuste para quando i volta a i*. Como os juros não sobem no final, não há " + azb("crowding out")
            + " do investimento: o multiplicador fiscal opera inteiro, maior que na economia fechada.",
            "“País pequeno” importa: ele toma i* como dado; um país grande, ao expandir, poderia elevar o próprio "
            "juro mundial.",
            "Espelho: no mesmo regime, a política " + azb("monetária") + " é ineficaz — o BC teria de vender as "
            "reservas que a expansão faz sair. Resumo da " + azb("trindade impossível") + ": câmbio fixo e "
            "capital livre custam a autonomia monetária.",
            vm("Regra-âncora: câmbio fixo → fiscal forte, monetária nula; câmbio flutuante → monetária forte, "
               "fiscal nula."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Parece estranho que o BC “ajude” a fiscal, mas é "
                       "o que a defesa do câmbio impõe: comprar divisas é emitir moeda. O verbo “ampliará” é o ponto "
                       "de risco — quem pensa em intervenção como “enxugar” marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a ação do Banco Central, vendendo reservas, reduzirá a efetividade da política fiscal.”</i> → "
            "ERRADO (inversão: o BC compra reservas e amplia o efeito)",
            "<i>“…com regime de câmbio flutuante, a política fiscal expansionista será eficaz para elevar o "
            "produto.”</i> → ERRADO (troca de regime: no flutuante, a valorização anula o efeito)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. Em câmbio fixo, a fiscal é eficaz: renda e juros maiores atraem capital; o BC "
                             "compra reservas para manter a paridade, expandindo a base monetária e deslocando a LM "
                             "para a direita."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00144-1, ECO-E2-L00658-1 (fiscal sob câmbio fixo e mobilidade "
                    "perfeita)"],
    },
    # ------------------------------------------------------------------ E1-0889
    {
        "id": "ECO-E1-0889-1", "fonte_ref": "E1-0889", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                      "fixo: uma desvalorização cambial provoca uma redução da renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                       "fixo: uma desvalorização cambial provoca ") + vm("uma redução") + az(" da renda.")),
        "poucas": ("A desvalorização barateia os bens nacionais, eleva " + azb("NX") + " e desloca a IS para a "
                   "direita; o superávit externo ainda leva o BC a emitir moeda: a renda " + vm("aumenta") + "."),
        "destrinchando": [
            "No câmbio fixo, a " + azb("desvalorização") + " é decisão da autoridade (muda-se a paridade). Com "
            "preços rígidos, o câmbio real também sobe: exportações ↑, importações ↓, " + vd("NX ↑") + ".",
            "Efeitos nas curvas: a " + vd("IS vai para a direita") + " (mais demanda externa) e a " + vd("BP vai "
            "para a direita") + " (a cada renda, o saldo comercial é melhor, e o equilíbrio externo admite juros "
            "menores).",
            "No novo cruzamento, há superávit: o BC compra divisas para manter a nova paridade, a base monetária "
            "cresce e a LM também se desloca para a direita. Resultado: " + vd("Y ↑") + ", reservas ↑.",
            "Ressalvas fora do modelo-padrão: exige a " + azb("condição de Marshall-Lerner") + "; no curtíssimo "
            "prazo pode haver " + azb("curva J") + " (o saldo piora antes de melhorar); e a literatura das "
            "“desvalorizações contracionistas” (dívida em dólar, perda de salário real) mostra casos de queda da "
            "renda — mas não é o que o IS-LM-BP prevê.",
            vm("Regra-âncora: desvalorização no IS-LM-BP → IS e BP à direita → renda ↑."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sinal do efeito sobre a renda. A premissa “alta, mas não "
                       "perfeita, mobilidade” serve só para garantir uma BP inclinada que possa se deslocar; não "
                       "altera a direção do resultado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma desvalorização cambial provoca aumento da base monetária, como consequência do aumento de "
            "reservas.”</i> → CERTO",
            "<i>“…uma desvalorização cambial desloca a BP para a esquerda.”</i> → ERRADO (sentido trocado: a BP vai "
            "para a direita)",
        ])],
        "reescrita": ("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                      "fixo: uma desvalorização cambial provoca " + hl("um aumento") + " da renda."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A desvalorização torna os produtos nacionais mais competitivos, estimula as "
                             "exportações líquidas e aumenta a demanda agregada e a renda."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0890
    {
        "id": "ECO-E1-0890-1", "fonte_ref": "E1-0890", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                      "fixo, uma desvalorização cambial provoca aumento da base monetária, como consequência do "
                      "aumento de reservas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                      "fixo, uma desvalorização cambial provoca <u>aumento da base monetária</u>, como consequência "
                      "do <u>aumento de reservas</u>."),
        "poucas": ("A desvalorização gera " + azb("superávit no balanço de pagamentos") + "; para manter a nova "
                   "paridade, o BC compra as divisas excedentes com moeda nova: reservas ↑ e " + vd("base "
                   "monetária ↑") + "."),
        "destrinchando": [
            "Balanço do Banco Central: do lado do ativo, " + azb("reservas internacionais") + "; do passivo, "
            + azb("base monetária") + ". Comprar US$ 1 bi de divisas = emitir o equivalente em moeda doméstica. "
            "Por isso, em câmbio fixo, " + vd("ΔReservas ≈ ΔBase") + " (sem esterilização).",
            "Desvalorização → NX ↑ → IS e BP para a direita → o ponto IS-LM fica acima/à esquerda da nova BP → "
            "superávit → excesso de oferta de dólares → BC compra para não deixar a moeda se valorizar.",
            "A base monetária maior desloca a " + vd("LM para a direita") + ", reforçando a alta da renda iniciada "
            "pela desvalorização.",
            azb("Esterilização") + ": o BC pode vender títulos para enxugar a moeda emitida. Isso mantém a base "
            "estável, mas eleva a dívida pública e o custo de carregar reservas — e, com mobilidade alta, atrai "
            "ainda mais capital. Sem menção à esterilização, vale a regra do modelo.",
            rx("Brasil") + ": nos anos 2000, o BCB acumulou reservas comprando dólares e esterilizou boa parte "
            "via operações compromissadas, que cresceram muito no período.",
        ],
        "dissecando": (cz("[literalidade]") + " O item encadeia corretamente desvalorização → superávit → compra "
                       "de reservas → base maior. O risco seria inverter o elo do meio (achar que o BC vende "
                       "reservas para “sustentar” a desvalorização)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma desvalorização cambial provoca redução da base monetária, pois o BC vende reservas para "
            "sustentar a nova paridade.”</i> → ERRADO (inversão: há superávit, e o BC compra)",
            "<i>“…uma valorização cambial provoca perda de reservas e contração da base monetária.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A desvalorização melhora o setor externo e gera superávit no balanço de "
                             "pagamentos; o BC compra moeda estrangeira para manter a paridade, expandindo a base "
                             "monetária."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0891
    {
        "id": "ECO-E1-0891-1", "fonte_ref": "E1-0891", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                      "fixo: uma desvalorização cambial provoca movimento da curva BP para a esquerda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                       "fixo: uma desvalorização cambial provoca movimento da curva BP para a ") + vm("esquerda")
                    + az(".")),
        "poucas": ("Com a desvalorização, cada nível de renda passa a ter saldo comercial melhor: o equilíbrio "
                   "externo admite renda maior (ou juros menores), e a BP se desloca para a " + vm("direita") + "."),
        "destrinchando": [
            "A " + azb("curva BP") + " reúne os pares (Y, i) com balanço de pagamentos equilibrado: NX(e, Y) + "
            "CF(i − i*) = 0. NX cai com a renda (importações) e sobe com o câmbio real; a conta financeira CF sobe "
            "com o diferencial de juros.",
            "Inclinação: positiva, porque renda maior piora NX e exige juros maiores para atrair capital. Quanto "
            "maior a mobilidade, mais plana: " + vd("perfeita → horizontal") + " em i*; " + vd("nula → "
            "vertical") + ".",
            "Deslocadores: " + vd("desvalorização real") + " (e ↑) → NX ↑ → BP para a " + vd("direita/baixo")
            + "; valorização → esquerda/cima; alta de i* → BP para cima; aumento do prêmio de risco-país → BP "
            "para cima.",
            "Abaixo/à direita da BP há déficit; acima/à esquerda, superávit. Após a desvalorização, o ponto de "
            "partida fica à esquerda da nova BP → superávit → em câmbio fixo, o BC compra divisas e a LM vai para "
            "a direita.",
            vm("Regra-âncora: câmbio que desvaloriza empurra IS e BP para a direita; que valoriza, para a "
               "esquerda."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido do deslocamento. Para não errar, raciocine pelo saldo: "
                       "se a desvalorização melhora as contas externas, a mesma renda agora gera superávit, e a "
                       "curva de equilíbrio precisa andar para onde a renda é maior — a direita."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma elevação da taxa de juros internacional desloca a curva BP para cima.”</i> → CERTO",
            "<i>“…com perfeita mobilidade de capital, uma desvalorização desloca a BP para baixo.”</i> → ERRADO "
            "(com mobilidade perfeita, a BP fica presa em i* e não se move com o câmbio)",
        ])],
        "reescrita": ("Em um modelo IS-LM-BP com alta, mas não perfeita, mobilidade de capital e com regime de câmbio "
                      "fixo: uma desvalorização cambial provoca movimento da curva BP para a " + hl("direita") + "."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A desvalorização melhora o balanço de pagamentos via exportações líquidas, o "
                             "que desloca a BP para a direita."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0892
    {
        "id": "ECO-E1-0892-1", "fonte_ref": "E1-0892", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo IS-LM-BP com perfeita mobilidade de capital, câmbio fixo e juros internacionais "
                      "dados, uma política monetária expansionista provoca uma potencial fuga de capitais, em face "
                      "da mudança nas taxas de juros internas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um modelo IS-LM-BP com perfeita mobilidade de capital, câmbio fixo e juros internacionais "
                      "dados, uma política monetária expansionista provoca uma <u>potencial</u> fuga de capitais, em "
                      "face da mudança nas taxas de juros internas."),
        "poucas": ("A expansão monetária pressiona os juros internos para " + azb("baixo de i*") + "; com mobilidade "
                   "perfeita, isso dispara saída de capitais, que o BC precisa cobrir vendendo reservas."),
        "destrinchando": [
            "M ↑ → LM para a direita → i tenderia a cair abaixo de i*. Com " + azb("mobilidade perfeita") + ", "
            "qualquer diferencial negativo, por menor que seja, leva os investidores a buscar o retorno externo: "
            + vd("fuga de capitais") + ".",
            "Saída de capitais = demanda por divisas → pressão de desvalorização. No câmbio fixo, o BC " + vd("vende "
            "reservas") + " e recolhe a moeda doméstica, desfazendo a expansão: a LM volta à posição inicial.",
            "Por isso a fuga é “potencial”: a queda dos juros nem chega a se materializar, pois a arbitragem e a "
            "intervenção acontecem quase instantaneamente. No equilíbrio, i = i*, Y e M inalterados, reservas "
            "menores.",
            "É a base da " + azb("trindade impossível") + " (" + oc("Mundell") + "): câmbio fixo + capital livre "
            "→ a política monetária deixa de ser autônoma; a oferta de moeda passa a ser determinada pelo balanço "
            "de pagamentos.",
            "Limite prático: se as reservas acabam antes, o regime cai — dinâmica dos " + azb("ataques "
            "especulativos") + " (" + rx("Brasil") + ", jan./1999).",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O “potencial” salva o item: a fuga é a força "
                       "que impede os juros de caírem, não um fluxo que se observa no equilíbrio final. Versões "
                       "com “redução permanente dos juros” seriam ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política monetária expansionista reduz de forma duradoura a taxa de juros interna.”</i> → "
            "ERRADO (com câmbio fixo e mobilidade perfeita, i permanece em i*)",
            "<i>“…uma política monetária expansionista provoca perda de reservas internacionais.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["potencial"], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A redução dos juros internos gera saída de capitais em busca de retornos no "
                             "exterior, o que pressiona o câmbio e força o BC a intervir."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00161-1 (política monetária sob câmbio fixo e mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E1-0940
    {
        "id": "ECO-E1-0940-1", "fonte_ref": "E1-0940", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2015, "cacd": False,
        "errei": True,
        "comando": "Julgue o item a seguir, acerca dos efeitos da política fiscal em uma economia aberta.",
        "rotulo_item": "Item",
        "assertiva": ("Políticas fiscais expansionistas contribuem para a depreciação da moeda e para o aumento do "
                      "investimento e das exportações líquidas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Políticas fiscais expansionistas contribuem para a ") + vm("depreciação") + az(" da moeda e "
                    "para ") + vm("o aumento do investimento e das exportações líquidas") + az(".")),
        "poucas": ("No Mundell-Fleming com mobilidade de capitais, a expansão fiscal eleva os juros, atrai capital e "
                   + azb("aprecia") + " a moeda: as exportações líquidas " + vm("caem") + " e o investimento não sobe "
                   "(cai, se os juros ficam mais altos)."),
        "destrinchando": [
            "Mecanismo-padrão (câmbio flutuante, mobilidade alta): G ↑ → IS para a direita → i ↑ → entrada de "
            "capitais → " + vd("apreciação") + " → X ↓, M ↑ → " + vd("NX ↓") + ". A demanda externa é "
            "“expulsa” para abrir espaço ao gasto público: " + azb("crowding out cambial") + ".",
            "Investimento: com mobilidade imperfeita, os juros terminam mais altos e o " + vd("investimento cai")
            + " (crowding out clássico). Com mobilidade perfeita, i volta a i* e o investimento fica igual — em "
            "nenhum caso aumenta.",
            "Identidade útil: S − I = NX. Um déficit público maior reduz a poupança nacional; para dado I, NX "
            "precisa cair (" + azb("déficits gêmeos") + "). Exemplo clássico: EUA nos anos 1980 (" + oc("Reagan")
            + "), com expansão fiscal, dólar forte e déficit externo crescente.",
            "Quando a expansão fiscal deprecia a moeda? Só com " + azb("baixa mobilidade") + " (a alta das "
            "importações pesa mais que a entrada de capital) ou se o mercado passa a temer a solvência do país "
            "(dominância fiscal, prêmio de risco ↑). Nesse caso, o investimento ainda assim tende a cair.",
            vm("Regra-âncora: fiscal expansionista + mobilidade de capitais → câmbio aprecia, NX ↓."),
        ],
        "dissecando": (cz("[inversão · meia-verdade]") + " O item inverte o sentido do câmbio e, sobre a inversão, "
                       "deduz um ganho de NX; acrescenta “aumento do investimento”, ignorando o crowding out. "
                       "Tudo parece coerente porque depreciação → NX ↑ é verdade isolada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Políticas monetárias expansionistas contribuem para a depreciação da moeda e para o aumento das "
            "exportações líquidas.”</i> → CERTO",
            "<i>“Políticas fiscais expansionistas, sob câmbio flutuante e perfeita mobilidade de capitais, elevam "
            "a renda de forma duradoura.”</i> → ERRADO (a apreciação anula o efeito sobre a renda)",
        ])],
        "reescrita": ("Políticas fiscais expansionistas contribuem para a " + hl("apreciação") + " da moeda e para "
                      + hl("a queda das exportações líquidas, sem elevar o investimento") + "."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Incorreta. Comentário mistura dois mecanismos (alta das importações pressionando o "
                             "câmbio para desvalorização e alta dos juros atraindo moeda estrangeira e apreciando "
                             "o câmbio) e conclui pela queda das exportações líquidas."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem afirma que a expansão fiscal leva à desvalorização e "
                    "que o governo “aumenta os juros para financiar o déficit”; no modelo, a alta dos juros é de "
                    "mercado e o câmbio se aprecia — corrigido",
                    "nota_redacao: frente com marcador ⌚ além do ❌; prova de 2015 sem órgão identificado"],
    },
    # ------------------------------------------------------------------ E1-0948
    {
        "id": "ECO-E1-0948-1", "fonte_ref": "E1-0948", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": "Julgue o item a seguir, acerca da eficácia das políticas macroeconômicas em regimes cambiais.",
        "rotulo_item": "Item",
        "assertiva": ("Nos sistemas de câmbio fixo, as políticas monetárias expansionistas são particularmente "
                      "eficazes para elevar a demanda agregada porque, nesses sistemas, o efeito deslocamento é "
                      "minimizado."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Nos sistemas de câmbio fixo, as políticas monetárias expansionistas são ")
                    + vm("particularmente eficazes") + az(" para elevar a demanda agregada porque, nesses sistemas, ")
                    + vm("o efeito deslocamento é minimizado") + az(".")),
        "poucas": ("Em câmbio fixo (com mobilidade de capital), a política " + azb("monetária") + " é "
                   + vm("ineficaz") + ": o BC perde reservas e desfaz a expansão. Quem se beneficia da ausência de "
                   "crowding out é a política " + azb("fiscal") + "."),
        "destrinchando": [
            "Expansão monetária em câmbio fixo: M ↑ → i tende a cair → saída de capitais → pressão de "
            "desvalorização → BC " + vd("vende reservas") + " e recolhe moeda → M volta ao nível inicial. A "
            "moeda torna-se " + azb("endógena") + " (passiva), atrelada ao balanço de pagamentos.",
            "Com mobilidade perfeita, a ineficácia é total; com mobilidade imperfeita, sobra efeito transitório, "
            "que se esgota à medida que as reservas caem. Em qualquer caso, o BC não controla a oferta de moeda "
            "de forma duradoura.",
            azb("Efeito deslocamento") + " (crowding out) é conceito de política " + vd("fiscal") + ": o gasto "
            "público eleva os juros e expulsa investimento privado. Em câmbio fixo com mobilidade, ele é "
            "minimizado porque o BC, ao comprar divisas, expande a moeda e segura os juros em i* — o que torna a "
            + vd("fiscal") + " particularmente eficaz.",
            "Leitura cruzada: o item cola na política monetária a justificativa que pertence à fiscal.",
            vm("Regra-âncora: câmbio fixo → fiscal forte (sem crowding out), monetária nula."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca “fiscal” por “monetária” mantendo a justificativa "
                       "verdadeira da fiscal (crowding out minimizado). Pista: “efeito deslocamento” é vocabulário de "
                       "gasto público, não de oferta de moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Nos sistemas de câmbio fixo, as políticas fiscais expansionistas são particularmente eficazes "
            "para elevar a demanda agregada porque, nesses sistemas, o efeito deslocamento é minimizado.”</i> → "
            "CERTO",
            "<i>“Nos sistemas de câmbio flutuante, as políticas monetárias expansionistas são particularmente "
            "eficazes, pois a depreciação estimula as exportações líquidas.”</i> → CERTO",
        ])],
        "reescrita": ("Nos sistemas de câmbio fixo, as políticas monetárias expansionistas são " + hl("ineficazes")
                      + " para elevar a demanda agregada porque, nesses sistemas, " + hl("a perda de reservas "
                      "desfaz a expansão da moeda") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["particularmente"], "dificuldade": 1,
        "comentario_fonte": ("Incorreta: em câmbio fixo, a política monetária é passiva, dependente das reservas; o "
                             "efeito deslocamento resulta da expansão de gastos públicos, que eleva os juros e expulsa "
                             "o setor privado."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00161-1, ECO-E1-0892-1 (monetária ineficaz em câmbio fixo)"],
    },
    # ------------------------------------------------------------------ E2-L00141
    {
        "id": "ECO-E2-L00141-1", "fonte_ref": "E2-L00141", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_1,
        "rotulo_item": "Item",
        "assertiva": ("A introdução de uma política fiscal expansiva, como um aumento no gasto público, desloca a "
                      "curva IS para a direita, resultando no aumento da renda, da demanda e da taxa de juros. Esse "
                      "último aumento, por sua vez, provoca a valorização da moeda nacional, reduzindo a taxa de "
                      "câmbio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A introdução de uma política fiscal expansiva, como um aumento no gasto público, desloca a "
                      "curva IS para a direita, resultando no aumento da renda, da demanda e da taxa de juros. Esse "
                      "último aumento, por sua vez, provoca a <u>valorização da moeda nacional</u>, <u>reduzindo a "
                      "taxa de câmbio</u>."),
        "poucas": ("G ↑ → IS à direita → Y e i sobem → os juros maiores atraem capital → a moeda nacional se "
                   + azb("valoriza") + ", e a taxa de câmbio (R$ por US$) " + vd("cai") + "."),
        "destrinchando": [
            "Primeira etapa é IS-LM puro: mais gasto público eleva a demanda; a renda maior aumenta a demanda por "
            "moeda e, com oferta monetária dada, os " + vd("juros sobem") + ".",
            "Segunda etapa, o elo externo: juros domésticos acima dos internacionais tornam os ativos locais mais "
            "atraentes → entrada de capitais → mais oferta de divisas → " + azb("valorização") + " da moeda "
            "nacional.",
            "Convenção: a " + azb("taxa de câmbio") + " é cotada como preço da moeda estrangeira (e = R$/US$). "
            "Valorizar o real = " + vd("e cair") + "; desvalorizar = e subir. Itens que dizem “valorização, "
            "elevando a taxa de câmbio” estão errados nessa convenção.",
            "Premissa implícita: mobilidade de capitais " + azb("alta") + " (BP menos inclinada que a LM). Com "
            "baixa mobilidade, a alta das importações pesaria mais que a entrada de capital, e o real se "
            "desvalorizaria.",
            "Consequência: a valorização reduz NX e devolve parte do deslocamento da IS — em câmbio flutuante "
            "com mobilidade perfeita, devolve tudo (fiscal ineficaz).",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Cadeia correta do manual. O detalhe que derruba candidatos "
                       "é a convenção de câmbio: valorização da moeda nacional = queda da taxa de câmbio. A premissa "
                       "de mobilidade alta está implícita no “inter-relações” do comando."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…provoca a valorização da moeda nacional, elevando a taxa de câmbio.”</i> → ERRADO (convenção "
            "invertida: valorização reduz R$/US$)",
            "<i>“…com baixa mobilidade de capitais, a expansão fiscal tende a desvalorizar a moeda nacional.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A expansão fiscal desloca a IS para a direita, eleva renda e juros; os juros "
                             "atraem capital estrangeiro, valorizam a moeda nacional e reduzem a taxa de câmbio."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00143
    {
        "id": "ECO-E2-L00143-1", "fonte_ref": "E2-L00143", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_2,
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de câmbio flutuante com perfeita mobilidade de capitais, uma política monetária "
                      "expansiva resulta na elevação da renda e na manutenção da taxa de juros, já que a BP "
                      "horizontal impede alterações na taxa de juros."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um regime de câmbio flutuante com perfeita mobilidade de capitais, uma política monetária "
                      "expansiva resulta na <u>elevação da renda</u> e na <u>manutenção da taxa de juros</u>, já que "
                      "a BP horizontal impede alterações na taxa de juros."),
        "poucas": ("Caso de " + azb("máxima eficácia monetária") + ": a LM vai à direita, os juros ameaçam cair, a "
                   "saída de capitais deprecia o câmbio, NX desloca a IS e o equilíbrio volta a " + vd("i = i*")
                   + " com renda bem maior."),
        "destrinchando": [
            "Mobilidade perfeita → " + azb("BP horizontal") + " em i*: qualquer diferencial de juros provoca fluxo "
            "ilimitado de capitais, então nenhum equilíbrio admite i ≠ i*.",
            "Passo a passo: M ↑ → LM₁ → LM₂ → no ponto provisório E′, i < i* → saída de capitais → " + vd("depreciação")
            + " → NX ↑ → IS₁ → IS₂ → novo equilíbrio E₂ sobre a BP: " + vd("Y ↑") + ", " + vd("i = i*") + ".",
            "A renda sobe mais que na economia fechada, porque o estímulo vem por dois canais (juros e câmbio). "
            "Pressupõe a condição de " + azb("Marshall-Lerner") + ".",
            "“A BP horizontal impede alterações” é forma condensada: a BP não é uma força, é o lugar dos "
            "equilíbrios externos; quem impede a mudança dos juros é a arbitragem de capitais, que move o câmbio.",
            "Espelho: no mesmo regime, a política " + azb("fiscal") + " é ineficaz (a apreciação devolve a IS); no "
            "câmbio fixo, os papéis se invertem.",
        ],
        "grafico_verso": "ECO-E2-L00143-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " Resultado de manual com uma justificativa simplificada "
                       "(“a BP impede”). A banca aceita a simplificação; o que derrubaria o item seria dizer que os "
                       "juros caem de forma duradoura ou que a renda não muda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política monetária expansiva resulta na elevação da renda e na queda permanente da taxa de "
            "juros.”</i> → ERRADO (com mobilidade perfeita, i volta a i*)",
            "<i>“…uma política fiscal expansiva resulta na elevação da renda e na manutenção da taxa de "
            "juros.”</i> → ERRADO (troca de política: no flutuante, a fiscal não eleva a renda)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. Expansão monetária desloca a LM para a direita; a queda provisória dos juros "
                             "provoca saída de capitais, depreciação e deslocamento da IS; juros voltam a i* e a renda "
                             "sobe (máxima eficácia). Várias respostas empilhadas com o mesmo passo a passo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00160-1, ECO-E1-0884-1 (expansão monetária sob câmbio flutuante e "
                    "mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L00144
    {
        "id": "ECO-E2-L00144-1", "fonte_ref": "E2-L00144", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_2,
        "rotulo_item": "Item",
        "assertiva": ("Sob câmbio fixo com perfeita mobilidade de capitais, uma política fiscal expansiva resulta na "
                      "elevação permanente da taxa de juros, dada a necessidade do Banco Central de vender dólares "
                      "para manter o câmbio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Sob câmbio fixo com perfeita mobilidade de capitais, uma política fiscal expansiva resulta na elevação permanente da ")
                    + vm("taxa de juros") + az(", dada a necessidade do Banco Central de ")
                    + vm("vender") + az(" dólares para manter o câmbio.")),
        "poucas": ("A pressão de alta dos juros atrai capital e ameaça " + azb("valorizar") + " a moeda; o BC "
                   + vm("compra") + " dólares, emite moeda, a LM acompanha a IS e os juros ficam em i* — o que sobe, "
                   "de forma permanente, é a " + vd("renda") + "."),
        "destrinchando": [
            "G ↑ → IS para a direita → no ponto provisório E′, i > i* → entrada maciça de capitais → excesso de "
            "oferta de dólares → pressão de " + vd("valorização") + ".",
            "Para manter a paridade, o BC " + vd("compra") + " o excesso de dólares, pagando com moeda nova: "
            "reservas ↑, base ↑, LM₁ → LM₂. O processo só para quando i volta a " + vd("i*") + ".",
            "Equilíbrio final E₂: " + vd("Y ↑ forte") + ", juros inalterados, reservas maiores. Sem alta de juros, "
            "não há crowding out: é o caso de " + azb("máxima eficácia da política fiscal") + ".",
            "Quando o BC vende dólares? Quando há pressão de desvalorização: expansão " + azb("monetária") + " "
            "(i < i*, fuga de capitais) ou, com baixa mobilidade, expansão fiscal que gera déficit comercial. O "
            "item misturou os casos.",
            "Única forma de juros ficarem mais altos: " + azb("esterilização") + " (o BC vende títulos para "
            "anular a emissão) — mas isso atrai ainda mais capital e é insustentável com mobilidade perfeita.",
        ],
        "grafico_verso": "ECO-E2-L00144-1-V1",
        "dissecando": (cz("[inversão · troca de conceito]") + " Dois erros: o resultado (juros “permanentemente” "
                       "maiores, quando ficam em i*) e o sentido da intervenção (vender, quando é comprar). O "
                       "“permanente” é a pista: com BP horizontal, nenhum choque altera i no equilíbrio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política fiscal expansiva resulta em aumento das reservas internacionais e da renda, sem "
            "alteração da taxa de juros.”</i> → CERTO",
            "<i>“Sob câmbio fixo com perfeita mobilidade, uma política monetária expansiva obriga o Banco Central a "
            "vender dólares.”</i> → CERTO",
        ])],
        "reescrita": ("Sob câmbio fixo com perfeita mobilidade de capitais, uma política fiscal expansiva resulta na elevação permanente da "
                      + hl("renda, sem alteração duradoura da taxa de juros") + ", dada a "
                      "necessidade do Banco Central de " + hl("comprar") + " dólares para manter o câmbio."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["permanente"], "dificuldade": 2,
        "comentario_fonte": ("ERRADO. A fiscal eleva os juros só inicialmente; o BC compra dólares e vende reais, "
                             "expandindo a base monetária e devolvendo os juros a i*. Várias respostas empilhadas "
                             "(trindade impossível, esterilização, reescrita)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0888-1, ECO-E2-L00658-1 (fiscal sob câmbio fixo e mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L00145
    {
        "id": "ECO-E2-L00145-1", "fonte_ref": "E2-L00145", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_2,
        "rotulo_item": "Item",
        "assertiva": ("Em um cenário de câmbio flutuante com baixa mobilidade de capitais, a política fiscal expansiva "
                      "tem pouco impacto sobre a renda, devido à limitação na entrada de capitais estrangeiros, "
                      "resultando em um aumento modesto das exportações."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um cenário de câmbio flutuante com baixa mobilidade de capitais, a política fiscal expansiva "
                       "tem ") + vm("pouco") + az(" impacto sobre a renda, ")
                    + vm("devido à limitação na entrada de capitais estrangeiros, resultando em um aumento modesto "
                         "das exportações") + az(".")),
        "poucas": ("Com baixa mobilidade, a expansão fiscal gera " + azb("déficit externo") + " e "
                   + azb("desvalorização") + "; as exportações sobem, a IS avança de novo e o impacto sobre a renda é "
                   + vm("grande") + "."),
        "destrinchando": [
            "G ↑ → IS para a direita → Y ↑ e i ↑. A renda maior eleva as importações; com " + vd("baixa "
            "mobilidade") + " (BP mais inclinada que a LM), a pouca entrada de capital não cobre o rombo: "
            + vd("déficit no balanço de pagamentos") + ".",
            "Câmbio flutuante: o déficit se resolve pelo preço — a moeda doméstica se " + vd("desvaloriza") + ", "
            "as exportações sobem, as importações caem, NX ↑ → a IS se desloca " + vd("de novo para a direita") +
            " (e a BP também). O efeito sobre a renda é amplificado.",
            "A limitação na entrada de capitais é justamente o que " + azb("fortalece") + " a fiscal aqui: impede "
            "a valorização que, com mobilidade alta, devolveria parte do estímulo.",
            "Quadro: câmbio flutuante + mobilidade " + vd("alta") + " → fiscal fraca (valorização); + mobilidade "
            + vd("baixa") + " → fiscal forte (desvalorização); câmbio fixo + mobilidade baixa → fiscal fraca (BC "
            "vende reservas e contrai a moeda).",
            vm("Regra-âncora: no flutuante, quanto menor a mobilidade, mais forte a fiscal."),
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " O item parte de um fato verdadeiro (pouca entrada de "
                       "capital) e tira a conclusão oposta, como se o capital estrangeiro fosse o motor da renda. "
                       "Raciocine pelo câmbio: sem entrada de capital, ele desvaloriza — e isso ajuda a renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com alta mobilidade de capitais, a política fiscal expansiva tem pouco impacto sobre a renda, "
            "devido à valorização cambial.”</i> → CERTO",
            "<i>“…com baixa mobilidade de capitais, a política fiscal expansiva valoriza a moeda nacional.”</i> → "
            "ERRADO (sentido trocado: desvaloriza)",
        ])],
        "reescrita": ("Em um cenário de câmbio flutuante com baixa mobilidade de capitais, a política fiscal expansiva "
                      "tem " + hl("grande") + " impacto sobre a renda, " + hl("pois o déficit externo deprecia o "
                      "câmbio e eleva as exportações, reforçando a expansão") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("ERRADO. A fiscal desloca a IS e aumenta a renda; a desvalorização causada pela saída de "
                             "dólares por importações aumenta as exportações, desloca a IS novamente à direita e "
                             "amplia significativamente a renda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00146
    {
        "id": "ECO-E2-L00146-1", "fonte_ref": "E2-L00146", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_2,
        "rotulo_item": "Item",
        "assertiva": ("No caso de câmbio fixo e alta mobilidade de capitais, um aumento na taxa de juros devido a "
                      "política fiscal expansionista resultaria em maior entrada de capitais do que saída por "
                      "comércio, levando à valorização do real e necessitando intervenção do Banco Central."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No caso de câmbio fixo e alta mobilidade de capitais, um aumento na taxa de juros devido a "
                      "política fiscal expansionista resultaria em <u>maior entrada de capitais do que saída por "
                      "comércio</u>, levando à <u>valorização do real</u> e necessitando intervenção do Banco "
                      "Central."),
        "poucas": ("Com " + azb("alta mobilidade") + ", a conta financeira reage mais aos juros que a balança "
                   "comercial à renda: superávit, pressão de " + vd("valorização") + " e BC comprando divisas "
                   "para segurar a paridade."),
        "destrinchando": [
            "G ↑ → Y ↑ e i ↑. Dois efeitos externos opostos: a renda maior eleva as importações (saída de divisas "
            "por comércio); os juros maiores atraem capital (entrada pela conta financeira).",
            "Qual prevalece depende da " + azb("inclinação relativa") + ": BP " + vd("menos inclinada") + " que a "
            "LM (alta mobilidade) → entrada > saída → " + vd("superávit") + "; BP mais inclinada (baixa "
            "mobilidade) → déficit.",
            "Superávit = excesso de oferta de dólares = pressão de " + azb("valorização") + " do real. Em câmbio "
            "fixo, o BC intervém " + vd("comprando dólares") + ": reservas ↑, base monetária ↑, LM para a "
            "direita, reforçando o efeito fiscal.",
            "Rigor de linguagem: em câmbio fixo a valorização é só “pressão” — a intervenção impede que ela se "
            "concretize. O item diz “levando à valorização… e necessitando intervenção”, leitura aceitável da "
            "sequência.",
            vm("Regra-âncora: câmbio fixo + mobilidade alta → fiscal gera superávit → BC compra divisas → LM à "
               "direita."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item compara os dois fluxos do balanço de pagamentos — "
                       "exatamente o que decide o resultado no IS-LM-BP. O risco é marcar ERRADO por achar que, em "
                       "câmbio fixo, “não há valorização”: há pressão, e é ela que obriga a intervenção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com baixa mobilidade de capitais, a política fiscal expansionista resultaria em maior entrada de "
            "capitais do que saída por comércio.”</i> → ERRADO (com baixa mobilidade prevalece a saída: déficit)",
            "<i>“…necessitando que o Banco Central venda dólares para conter a valorização.”</i> → ERRADO "
            "(inversão: conter a valorização exige comprar dólares)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("CERTO. A fiscal eleva os juros e atrai capital; a entrada supera a saída por comércio, "
                             "pressionando o real à valorização; o BC compra dólares, injetando reais."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00160
    {
        "id": "ECO-E2-L00160-1", "fonte_ref": "E2-L00160", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_3,
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de câmbio flutuante, uma política monetária expansiva resulta em uma desvalorização "
                      "cambial, o que, por sua vez, aumenta as exportações e reduz as importações, levando a um novo "
                      "deslocamento positivo da curva IS."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um regime de câmbio flutuante, uma política monetária expansiva resulta em uma "
                      "<u>desvalorização cambial</u>, o que, por sua vez, aumenta as exportações e reduz as "
                      "importações, levando a um <u>novo deslocamento positivo da curva IS</u>."),
        "poucas": ("No câmbio flutuante, a expansão monetária derruba os juros, provoca saída de capitais e "
                   + azb("deprecia") + " o câmbio; NX ↑ desloca a IS para a direita — a renda sobe pelos canais dos "
                   "juros " + vd("e") + " do câmbio."),
        "destrinchando": [
            "Cadeia em cinco elos: (1) BC expande a moeda → LM para a direita; (2) i cai abaixo de i*; (3) fuga "
            "de capitais → demanda por divisas ↑; (4) " + vd("depreciação") + " (e = R$/US$ sobe); (5) X ↑, M ↓ "
            "→ " + vd("NX ↑") + " → IS para a direita.",
            "Equilíbrio final (mobilidade perfeita): i = i*, renda bem maior, câmbio depreciado, BP equilibrado "
            "— a melhora da conta corrente compensa a saída pela conta financeira.",
            "O “novo” deslocamento positivo é preciso: o primeiro impulso veio da LM (movimento ao longo da IS); "
            "o segundo, do câmbio, desloca a própria IS. É por isso que a política monetária é " + azb("mais "
            "eficaz") + " na economia aberta com câmbio flutuante do que na fechada.",
            "Condições: " + azb("Marshall-Lerner") + " satisfeita; no curtíssimo prazo, a " + azb("curva J")
            + " pode atrasar a melhora do saldo. O Mundell-Fleming trabalha com o ajuste já completo.",
            "Contraste: no câmbio fixo, o elo (4) é bloqueado — o BC vende reservas para impedir a depreciação, "
            "a moeda volta e a renda não se move.",
        ],
        "dissecando": (cz("[literalidade]") + " Descrição canônica do canal cambial. O item é longo e encadeado; "
                       "o risco é desconfiar da “desvalorização” (achar que expansão monetária valoriza) ou do "
                       "deslocamento da IS (achar que política monetária só mexe na LM)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um regime de câmbio fixo, uma política monetária expansiva resulta em desvalorização cambial e "
            "novo deslocamento positivo da IS.”</i> → ERRADO (troca de regime: o BC impede a desvalorização)",
            "<i>“Em um regime de câmbio flutuante, uma política fiscal expansiva resulta em desvalorização "
            "cambial.”</i> → ERRADO (troca de política: com mobilidade perfeita, a fiscal valoriza o câmbio)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A expansão monetária desloca a LM, reduz os juros e desvaloriza a moeda; a "
                             "desvalorização aumenta exportações e reduz importações, deslocando a IS para a direita. "
                             "Várias respostas empilhadas com o passo a passo, Marshall-Lerner, curva J e trindade "
                             "impossível."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 013", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (cadeia de cinco passos refeita no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L00143-1, ECO-E1-0884-1 (expansão monetária sob câmbio flutuante e "
                    "mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L00161
    {
        "id": "ECO-E2-L00161-1", "fonte_ref": "E2-L00161", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_3,
        "rotulo_item": "Item",
        "assertiva": ("Quando a economia opera sob um regime de câmbio fixo, uma política monetária expansiva não "
                      "consegue alterar o nível de renda de forma significativa, pois o Banco Central precisa agir "
                      "para manter a taxa de câmbio fixa, anulando o impacto inicial de expansão monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Quando a economia opera sob um regime de câmbio fixo, uma política monetária expansiva <u>não "
                      "consegue alterar o nível de renda</u> de forma significativa, pois o Banco Central precisa agir "
                      "para manter a taxa de câmbio fixa, <u>anulando o impacto inicial</u> de expansão monetária."),
        "poucas": ("Câmbio fixo + mobilidade perfeita: a expansão monetária gera fuga de capitais; para defender a "
                   "paridade, o BC " + azb("vende reservas") + " e recolhe a moeda emitida, e a LM volta ao ponto de "
                   "partida — " + vd("renda inalterada") + "."),
        "destrinchando": [
            "M ↑ → LM₁ → LM₂ → juros abaixo de i* no ponto provisório E′ → saída de capitais → pressão de "
            "desvalorização.",
            "Defesa da paridade: o BC " + vd("vende dólares") + " e retira reais de circulação → base monetária ↓ → "
            "a LM retorna a LM₁. Fim: " + vd("Y, i e M iguais") + " aos iniciais; o único rastro é a " + vd("perda "
            "de reservas") + " (o BC trocou reservas por títulos domésticos).",
            "A política monetária deixa de ser instrumento: a oferta de moeda é " + azb("endógena") + ", "
            "determinada pelo balanço de pagamentos. É o vértice “abre mão da autonomia monetária” da "
            + azb("trindade impossível") + " (" + oc("Mundell") + ").",
            "Com mobilidade imperfeita, sobra um efeito transitório; e o BC pode tentar " + azb("esterilizar")
            + " a perda de reservas, mas só enquanto elas durarem.",
            "Exemplos: " + azb("currency board") + " argentino (1991–2001) e as bandas do Plano Real até jan./1999 — "
            + rx("Brasil") + ": a defesa da paridade exigiu juros altíssimos e queima de reservas até a flutuação.",
            vm("Regra-âncora: câmbio fixo → monetária nula, fiscal forte."),
        ],
        "grafico_verso": "ECO-E2-L00161-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " O “de forma significativa” protege o item de "
                       "discussões sobre efeitos transitórios. A justificativa (BC precisa defender o câmbio e anula "
                       "a expansão) é exatamente a do modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o Banco Central precisa comprar dólares para manter a taxa de câmbio fixa.”</i> → ERRADO "
            "(inversão: a fuga de capitais exige vender dólares)",
            "<i>“Sob câmbio flutuante, uma política monetária expansiva não consegue alterar o nível de "
            "renda.”</i> → ERRADO (troca de regime: no flutuante ela é muito eficaz)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["de forma significativa"], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A necessidade de manter o câmbio leva o BC a vender dólares e retirar moeda "
                             "doméstica, restaurando a LM à posição inicial e anulando a elevação da renda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0948-1, ECO-E1-0892-1 (monetária ineficaz em câmbio fixo)"],
    },
    # ------------------------------------------------------------------ E2-L00162
    {
        "id": "ECO-E2-L00162-1", "fonte_ref": "E2-L00162", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_3,
        "rotulo_item": "Item",
        "assertiva": ("Sob um câmbio fixo, a política fiscal expansiva é ineficiente, pois, ao elevar a taxa de juros "
                      "como resposta ao aumento da renda, ocorre uma valorização da moeda nacional que impede o "
                      "aumento desejado nas exportações líquidas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Sob um câmbio fixo, a política fiscal expansiva é ") + vm("ineficiente") + az(", pois, ao "
                    "elevar a taxa de juros como resposta ao aumento da renda, ")
                    + vm("ocorre uma valorização da moeda nacional que impede o aumento desejado nas exportações "
                         "líquidas") + az(".")),
        "poucas": ("Em câmbio fixo com mobilidade perfeita, a fiscal tem " + azb("eficácia máxima") + ": o BC "
                   + vm("impede") + " a valorização comprando divisas, a moeda se expande e não há crowding out. A "
                   "história do item é a do câmbio flutuante."),
        "destrinchando": [
            "G ↑ → IS para a direita → i tende a subir → entrada de capitais → pressão de valorização. No câmbio "
            "fixo, o BC " + vd("compra dólares") + " para manter a paridade: base ↑, " + vd("LM para a direita")
            + ", juros de volta a i*.",
            "Resultado: " + vd("Y ↑ forte") + ", câmbio inalterado, reservas ↑. Nem os juros nem o câmbio expulsam "
            "demanda privada — o multiplicador opera inteiro.",
            "O mecanismo descrito no item (juros ↑ → " + azb("valorização efetiva") + " → NX ↓ → IS volta) é o do "
            + vd("câmbio flutuante") + ", onde a fiscal é ineficaz com mobilidade perfeita (" + azb("crowding out "
            "cambial") + ").",
            "Detalhe de enunciado: a fiscal não busca “aumentar exportações líquidas”; o que a valorização faria "
            "seria reduzi-las e devolver o estímulo. O item embaralha objetivo e efeito colateral.",
            vm("Regra-âncora: fixo → fiscal forte; flutuante → monetária forte."),
        ],
        "dissecando": (cz("[troca de conceito · inversão]") + " Transplanta para o câmbio fixo o roteiro do câmbio "
                       "flutuante. Pista: “ocorre uma valorização” é incompatível com câmbio fixo, em que a "
                       "intervenção existe justamente para que ela não ocorra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio flutuante, a política fiscal expansiva é ineficaz, pois a valorização da moeda nacional "
            "reduz as exportações líquidas.”</i> → CERTO",
            "<i>“Sob câmbio fixo, a política fiscal expansiva leva o Banco Central a vender reservas.”</i> → "
            "ERRADO (inversão: com mobilidade alta, ele compra)",
        ])],
        "reescrita": ("Sob um câmbio fixo, a política fiscal expansiva é " + hl("eficaz") + ", pois, ao elevar a taxa "
                      "de juros como resposta ao aumento da renda, " + hl("atrai capitais, e o Banco Central, para "
                      "impedir a valorização da moeda nacional, compra divisas e expande a oferta de moeda") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A fiscal é eficiente em câmbio fixo: o aumento da renda eleva a demanda "
                             "monetária e o BC, ao comprar moeda estrangeira, introduz moeda nacional, intensificando "
                             "o efeito fiscal."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00163
    {
        "id": "ECO-E2-L00163-1", "fonte_ref": "E2-L00163", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_3,
        "rotulo_item": "Item",
        "assertiva": ("O efeito crowding out é observado em uma política fiscal expansiva em câmbio flutuante, onde o "
                      "aumento na taxa de juros leva a uma valorização cambial, anulando o ganho inicial da renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (vm("O efeito crowding out") + az(" é observado em uma política fiscal expansiva em câmbio "
                    "flutuante, onde o aumento na taxa de juros leva a uma valorização cambial, anulando o ganho "
                    "inicial da renda.")),
        "poucas": ("Pela leitura da fonte, o que anula a renda no câmbio flutuante é a " + azb("queda das "
                   "exportações líquidas") + " (crowding out cambial), com juros de volta a i* — não o crowding out "
                   "clássico, em que juros altos expulsam o investimento."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá ERRADO, mas o mecanismo descrito é o resultado-padrão do Mundell-Fleming sob "
                          "câmbio flutuante e mobilidade perfeita (premissa do comando): a alta provisória dos juros "
                          "atrai capital, o câmbio se valoriza, NX cai e o ganho de renda " + vd("é anulado")
                          + ". Manuais como o de " + oc("Mankiw") + " chamam isso de crowding out das exportações "
                          "líquidas. A resposta mais defensável seria " + vm("CERTO") + "; o ERRADO só se sustenta "
                          "numa leitura estrita de “efeito crowding out” como expulsão do investimento via juros.")],
        "destrinchando": [
            "Sequência: G ↑ → IS para a direita → i provisoriamente acima de i* → entrada de capitais → "
            + vd("valorização") + " → X ↓, M ↑ → NX ↓ → IS volta à posição inicial. Final: " + vd("Y e i "
            "inalterados") + ", câmbio apreciado, " + vd("ΔNX = −ΔG") + ".",
            azb("Crowding out clássico") + " (economia fechada): o gasto público eleva juros e reduz o investimento "
            "privado. " + azb("Crowding out cambial") + " (economia aberta, câmbio flutuante): o gasto público "
            "valoriza a moeda e reduz as exportações líquidas. No caso de mobilidade perfeita, o segundo é total e "
            "o primeiro não ocorre (i volta a i*).",
            "Por isso a crítica da fonte: o item atribui o resultado ao “aumento na taxa de juros” como se ele "
            "persistisse e chama de “crowding out” um efeito que não passa pelo investimento.",
            "Com mobilidade apenas alta (não perfeita), os dois canais coexistem e a renda sobe um pouco: "
            "anulação parcial, não total.",
            vm("Regra-âncora: câmbio flutuante + mobilidade perfeita → fiscal sem efeito sobre Y; quem é expulso é "
               "NX, não I."),
        ],
        "dissecando": (cz("[troca de conceito · outro: rótulo disputado]") + " A banca joga com o nome do "
                       "mecanismo: o resultado (renda anulada) é o do modelo, mas o rótulo “efeito crowding out” "
                       "e o protagonismo dos juros são discutíveis. Em prova, vale verificar se a banca distingue "
                       "crowding out de juros e de câmbio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em câmbio flutuante com perfeita mobilidade de capitais, a política fiscal expansiva reduz as "
            "exportações líquidas na mesma magnitude do aumento do gasto, sem alterar a renda.”</i> → CERTO",
            "<i>“…em câmbio fixo, onde o aumento na taxa de juros leva a uma valorização cambial, anulando o ganho "
            "da renda.”</i> → ERRADO (troca de regime: no fixo, o BC impede a valorização e a fiscal é eficaz)",
        ])],
        "reescrita": (hl("O deslocamento das exportações líquidas (crowding out cambial, e não o crowding out "
                         "clássico do investimento)") + " é observado em uma política fiscal expansiva em câmbio "
                      "flutuante, onde o aumento na taxa de juros leva a uma valorização cambial, anulando o ganho "
                      "inicial da renda."),
        "tipo_erro": ["TROCA_CONCEITO", "OUTRO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": ("ERRADO. Respostas empilhadas e divergentes: uma diz que crowding out não implica "
                             "anulação total; outra, que em mobilidade perfeita a anulação é total, mas via NX, sem "
                             "alta persistente de juros nem crowding out clássico do investimento."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["contestavel: sob câmbio flutuante e mobilidade perfeita (premissa do comando), a expansão "
                    "fiscal é integralmente anulada pela valorização e queda de NX — resultado que muitos manuais "
                    "chamam de crowding out; a resposta mais defensável seria CERTO. Mantido o ERRADO da fonte",
                    "qualidade_fonte: uma das respostas de origem afirma que o ganho de renda não é necessariamente "
                    "anulado, ignorando a premissa de mobilidade perfeita do comando",
                    "quase_duplicata: ECO-E2-L00164-1, ECO-E2-L00505-1"],
    },
    # ------------------------------------------------------------------ E2-L00164
    {
        "id": "ECO-E2-L00164-1", "fonte_ref": "E2-L00164", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_4,
        "rotulo_item": "Item",
        "assertiva": ("Em um cenário de câmbio flutuante com perfeita mobilidade de capitais, a política fiscal "
                      "expansiva não afeta a renda ou a taxa de juros, já que a curva IS retorna ao ponto de "
                      "equilíbrio inicial devido à movimentação do câmbio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um cenário de câmbio flutuante com perfeita mobilidade de capitais, a política fiscal "
                      "expansiva <u>não afeta a renda ou a taxa de juros</u>, já que a curva IS <u>retorna ao ponto de "
                      "equilíbrio inicial</u> devido à movimentação do câmbio."),
        "poucas": ("É a " + azb("ineficácia total da fiscal") + " no Mundell-Fleming: a IS avança, a valorização "
                   "cambial derruba NX e a IS volta a IS₁ — " + vd("Y e i") + " terminam onde começaram."),
        "destrinchando": [
            "G ↑ → IS₁ → IS₂ → no ponto provisório E′, Y e i sobem (i > i*) → entrada maciça de capitais → "
            + vd("valorização") + " → NX ↓ → a IS volta a IS₁.",
            "Por que volta exatamente? Com mobilidade perfeita, o equilíbrio exige i = i*. Com a LM parada (o BC "
            "não intervém no câmbio flutuante), há um único Y compatível com M/P e i*: o inicial. A IS precisa "
            "voltar ao mesmo lugar.",
            "Composição muda: mais " + vd("G") + ", menos " + vd("NX") + " na mesma medida (" + azb("crowding out "
            "cambial") + " total). Investimento e consumo ficam iguais, porque juros e renda não mudaram.",
            "Contraste: no câmbio fixo, o BC compraria divisas e a LM acompanharia a IS — fiscal forte. Com "
            "mobilidade imperfeita no flutuante, sobra algum efeito sobre Y e i.",
            "Aplicação: em país grande (EUA), a expansão fiscal eleva também o juro mundial e o resultado é menos "
            "extremo — o modelo é de " + azb("pequena economia aberta") + ".",
            vm("Regra-âncora: flutuante + mobilidade perfeita → ΔG = −ΔNX; Y e i inalterados."),
        ],
        "grafico_verso": "ECO-E2-L00164-1-V1",
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Contraria a intuição keynesiana de que gasto "
                       "público sempre eleva a renda. As premissas (flutuante + perfeita) são as do caso extremo, e "
                       "o item tira a conclusão correta — inclusive sobre os juros, que voltam a i*."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a política fiscal expansiva eleva a taxa de juros de forma permanente, mas não afeta a "
            "renda.”</i> → ERRADO (com mobilidade perfeita, i volta a i*)",
            "<i>“…em câmbio fixo com perfeita mobilidade de capitais, a política fiscal expansiva não afeta a "
            "renda.”</i> → ERRADO (troca de regime: no fixo, a fiscal tem eficácia máxima)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A fiscal desloca a IS e eleva os juros; o capital estrangeiro valoriza o câmbio e "
                             "aumenta importações, e a IS retorna ao ponto inicial, anulando os efeitos sobre renda e "
                             "juros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00505-1, ECO-E2-L00658-1 (fiscal ineficaz sob câmbio flutuante e "
                    "mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L00165
    {
        "id": "ECO-E2-L00165-1", "fonte_ref": "E2-L00165", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_4,
        "rotulo_item": "Item",
        "assertiva": ("Em câmbio fixo e alta mobilidade de capitais, uma política fiscal expansiva leva a um aumento "
                      "na renda, enquanto a política monetária produz efeitos sobre o nível de renda, pois o Banco "
                      "Central não pode atuar para neutralizar impactos cambiais causados por flutuações na "
                      "quantidade de moeda nacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em câmbio fixo e alta mobilidade de capitais, uma política fiscal expansiva leva a um aumento "
                       "na renda, enquanto a política monetária ") + vm("produz") + az(" efeitos sobre o nível de "
                       "renda, pois o Banco Central ") + vm("não pode") + az(" atuar para neutralizar impactos "
                       "cambiais causados por flutuações na quantidade de moeda nacional.")),
        "poucas": ("A primeira oração está certa (fiscal eficaz). Na segunda, o modelo diz o oposto: o BC "
                   + vm("precisa") + " neutralizar os impactos cambiais da moeda, e por isso a política monetária "
                   + azb("não") + " afeta a renda."),
        "destrinchando": [
            azb("Fiscal") + " (correto): G ↑ → juros pressionados para cima → entrada de capitais → pressão de "
            "valorização → BC " + vd("compra dólares") + ", emite moeda → LM para a direita → " + vd("Y ↑") + " "
            "sem crowding out.",
            azb("Monetária") + " (errado no item): M ↑ → juros pressionados para baixo → saída de capitais → "
            "pressão de desvalorização → BC " + vd("vende dólares") + ", recolhe moeda → LM volta → " + vd("Y "
            "inalterado") + ".",
            "Ou seja, o BC não só pode como " + vd("é obrigado") + " a neutralizar os efeitos cambiais das "
            "variações de moeda: é o que define o câmbio fixo. Com isso perde o controle da oferta monetária "
            "(" + azb("trindade impossível") + ").",
            "A frase seria verdadeira sob " + azb("câmbio flutuante") + ": aí o BC não intervém, o câmbio absorve "
            "o choque e a política monetária afeta fortemente a renda.",
            vm("Regra-âncora: câmbio fixo → fiscal eficaz, monetária ineficaz; o BC é refém da paridade."),
        ],
        "dissecando": (cz("[meia-verdade · inversão]") + " Começa com uma verdade (fiscal eficaz em câmbio fixo) "
                       "para dar credibilidade e inverte a segunda metade. Pista: “não pode atuar” contradiz a "
                       "própria definição de câmbio fixo, em que o BC atua sempre."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…enquanto a política monetária não produz efeitos sobre o nível de renda, pois o Banco Central "
            "precisa atuar para manter a paridade.”</i> → CERTO",
            "<i>“Em câmbio fixo e alta mobilidade de capitais, uma política fiscal expansiva leva o Banco Central a "
            "vender moeda estrangeira.”</i> → ERRADO (inversão: ele compra)",
        ])],
        "reescrita": ("Em câmbio fixo e alta mobilidade de capitais, uma política fiscal expansiva leva a um aumento na "
                      "renda, enquanto a política monetária " + hl("não produz") + " efeitos sobre o nível de renda, "
                      "pois o Banco Central " + hl("precisa") + " atuar para neutralizar impactos cambiais causados "
                      "por flutuações na quantidade de moeda nacional."),
        "tipo_erro": ["MEIA_VERDADE", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. A fiscal tem impacto positivo na renda (o comentário diz que o BC vende moeda "
                             "estrangeira e compra moeda nacional, ampliando a base); a monetária não produz efeitos, "
                             "pois o BC neutraliza as flutuações monetárias para manter o câmbio."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem diz que, na expansão fiscal, o BC vende moeda "
                    "estrangeira e compra moeda nacional, “ampliando a base monetária”; o correto é comprar moeda "
                    "estrangeira e emitir moeda nacional — corrigido"],
    },
    # ------------------------------------------------------------------ E2-L00166
    {
        "id": "ECO-E2-L00166-1", "fonte_ref": "E2-L00166", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN_4,
        "rotulo_item": "Item",
        "assertiva": ("No regime de câmbio flutuante com forte mobilidade de capitais, uma política monetária "
                      "expansiva não afeta a taxa de juros, mas gera uma significativa elevação na renda, devido à "
                      "interação entre o aumento das exportações e a desvalorização cambial que o movimento de "
                      "capital ocasiona."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime de câmbio flutuante com forte mobilidade de capitais, uma política monetária "
                       "expansiva ") + vm("não afeta") + az(" a taxa de juros, mas gera uma significativa elevação na "
                       "renda, devido à interação entre o aumento das exportações e a desvalorização cambial que o "
                       "movimento de capital ocasiona.")),
        "poucas": ("“Forte” não é “perfeita”: com a BP " + azb("inclinada") + ", o equilíbrio final admite juros "
                   "um pouco " + vm("menores") + " que os iniciais. A renda sobe muito, mas a taxa de juros também "
                   "muda."),
        "destrinchando": [
            "Mobilidade " + vd("perfeita") + " → BP horizontal em i* → no equilíbrio, i = i* sempre: a expansão "
            "monetária eleva Y sem mudar i.",
            "Mobilidade " + vd("forte, mas imperfeita") + " → BP positivamente inclinada, mais plana que a LM. Os "
            "capitais reagem bastante ao diferencial de juros, mas não infinitamente: para cada nível de renda "
            "existe um juro de equilíbrio externo diferente.",
            "Ajuste: M ↑ → LM à direita → i ↓ → saída de capitais → depreciação → NX ↑ → IS e BP à direita. O "
            "novo cruzamento tem " + vd("Y bem maior") + " e " + vd("i um pouco menor") + " que o inicial.",
            "O mecanismo descrito na segunda parte (desvalorização → exportações → renda) está certo; o erro é "
            "só o “não afeta”, que pertence ao caso-limite.",
            vm("Regra-âncora: “juros inalterados” é marca exclusiva da mobilidade perfeita (BP horizontal)."),
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " A banca troca “perfeita” por “forte” e "
                       "mantém a conclusão do caso-limite. Leia o grau de mobilidade antes de tudo: é ele que decide "
                       "se os juros voltam a i*."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de câmbio flutuante com perfeita mobilidade de capitais, uma política monetária "
            "expansiva não afeta a taxa de juros, mas eleva significativamente a renda.”</i> → CERTO",
            "<i>“…com forte mobilidade de capitais, uma política monetária expansiva valoriza o câmbio.”</i> → "
            "ERRADO (sentido trocado: a saída de capitais deprecia)",
        ])],
        "reescrita": ("No regime de câmbio flutuante com forte mobilidade de capitais, uma política monetária "
                      "expansiva " + hl("reduz levemente") + " a taxa de juros, mas gera uma significativa elevação "
                      "na renda, devido à interação entre o aumento das exportações e a desvalorização cambial que o "
                      "movimento de capital ocasiona."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["forte"], "dificuldade": 3,
        "comentario_fonte": ("ERRADO. A monetária expansiva reduz os juros momentaneamente; a saída de capital deprecia "
                             "o câmbio e desloca a IS, mas a taxa de juros pode não retornar ao nível original: há "
                             "efeitos sobre renda e juros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00167
    {
        "id": "ECO-E2-L00167-1", "fonte_ref": "E2-L00167", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BOZAN_4,
        "rotulo_item": "Item",
        "assertiva": ("Sob câmbio fixo e imobilidade de capitais, políticas fiscais expansivas resultam em aumento da "
                      "taxa de juros e, devido à intervenção do Banco Central para estabilizar a moeda, a renda "
                      "permanece inalterada, tornando a política ineficaz em termos de estímulo ao crescimento "
                      "econômico."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sob câmbio fixo e imobilidade de capitais, políticas fiscais expansivas resultam em <u>aumento "
                      "da taxa de juros</u> e, devido à intervenção do Banco Central para estabilizar a moeda, a "
                      "<u>renda permanece inalterada</u>, tornando a política ineficaz em termos de estímulo ao "
                      "crescimento econômico."),
        "poucas": ("Capitais imóveis → " + azb("BP vertical") + " no único nível de renda que equilibra a balança "
                   "comercial. A fiscal eleva Y, gera déficit, o BC vende reservas, a LM recua: " + vd("Y volta ao "
                   "nível inicial") + " com juros mais altos."),
        "destrinchando": [
            "Sem fluxo de capitais, o balanço de pagamentos é só a balança comercial, que depende da renda (via "
            "importações) e não dos juros: " + vd("BP vertical") + " em Y₁.",
            "G ↑ → IS₁ → IS₂ → no ponto provisório E′, Y > Y₁: importações ↑ → " + vd("déficit") + " (E′ à direita "
            "da BP) → pressão de desvalorização.",
            "Para manter a paridade, o BC " + vd("vende reservas") + " e recolhe moeda doméstica → base ↓ → LM₁ → "
            "LM₂, até a economia voltar à BP. Equilíbrio E₂: " + vd("Y = Y₁") + ", " + vd("i₂ > i₁") + ".",
            "A composição da demanda muda: mais gasto público, menos investimento privado (juros maiores) — "
            + azb("crowding out completo") + ", agora imposto pela " + azb("restrição externa") + ".",
            "Contexto: retrata economias com controle de capitais e reservas escassas — " + rx("Brasil") + " e "
            "América Latina antes dos anos 1990, quando o crescimento esbarrava no “estrangulamento externo” "
            "(tema caro à " + oc("CEPAL") + ").",
            "Para escapar da restrição sem mudar a mobilidade, só a política que desloca a própria BP: "
            "desvalorização (NX ↑ a cada renda) ou proteção comercial.",
        ],
        "grafico_verso": "ECO-E2-L00167-1-V1",
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Caso-limite pouco lembrado: muitos associam "
                       "“câmbio fixo” a “fiscal forte”, o que só vale com mobilidade alta. Aqui a imobilidade "
                       "inverte o resultado. Pista: “imobilidade” = BP vertical = renda presa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio fixo e imobilidade de capitais, a política fiscal expansiva eleva a renda sem alterar "
            "os juros.”</i> → ERRADO (troca de caso: isso vale com mobilidade perfeita)",
            "<i>“Sob câmbio fixo e imobilidade de capitais, uma desvalorização cambial eleva a renda de "
            "equilíbrio.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("CERTO. A fiscal eleva juros e renda; sem entrada de capitais, o déficit comercial leva "
                             "o BC a vender reservas e retirar moeda, a LM recua e a renda volta ao nível inicial, com "
                             "juros maiores. Várias respostas empilhadas com o passo a passo e a BP vertical."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00485
    {
        "id": "ECO-E2-L00485-1", "fonte_ref": "E2-L00485", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("A trindade impossível identificada por Mundell refere-se à impossibilidade de combinar livre "
                      "mobilidade de capital, taxa de câmbio flutuante e política monetária autônoma."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A trindade impossível identificada por Mundell refere-se à impossibilidade de combinar livre "
                       "mobilidade de capital, taxa de câmbio ") + vm("flutuante") + az(" e política monetária "
                       "autônoma.")),
        "poucas": ("O trilema é entre " + azb("câmbio fixo") + ", livre mobilidade de capital e política monetária "
                   "autônoma. Câmbio " + vm("flutuante") + " + capital livre + autonomia é justamente a combinação "
                   "possível."),
        "destrinchando": [
            "Enunciado: um país pode ter, no máximo, " + vd("dois de três") + " objetivos — (1) câmbio fixo, (2) "
            "livre mobilidade de capital, (3) política monetária autônoma. Formulação associada a " + oc("Mundell")
            + " e " + oc("Fleming") + " (anos 1960); o nome “trilema” popularizou-se depois, com " + oc("Obstfeld")
            + " e outros.",
            "Lógica: com capital livre, i = i* + expectativa de desvalorização. Se o câmbio é fixo e crível, i = "
            "i*: o BC não escolhe os juros. Para ter juros próprios, é preciso deixar o câmbio flutuar ou "
            "restringir o capital.",
            "As três combinações possíveis: " + vd("fixo + capital livre") + " (zona do euro, currency boards; sem "
            "autonomia); " + vd("flutuante + capital livre") + " (Brasil desde 1999, EUA; com autonomia); "
            + vd("fixo + autonomia") + " (Bretton Woods, China por muito tempo; com controles de capital).",
            rx("Brasil") + ": o tripé de 1999 (metas de inflação, câmbio flutuante, metas fiscais) escolheu o "
            "vértice flutuante + capital livre + autonomia monetária.",
            "Debate recente: " + oc("Hélène Rey") + " (2013) argumenta que o ciclo financeiro global reduz a "
            "autonomia mesmo com câmbio flutuante — o trilema viraria “dilema”.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca um dos vértices pelo seu oposto. Teste rápido: a "
                       "combinação descrita existe no mundo real? Câmbio flutuante + capital livre + juros próprios "
                       "é o arranjo de quase todos os grandes emergentes — logo, não é “impossível”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela trindade impossível, um país com câmbio fixo e livre mobilidade de capital abre mão da "
            "autonomia monetária.”</i> → CERTO",
            "<i>“A trindade impossível impede que um país adote simultaneamente câmbio fixo e controle de "
            "capitais.”</i> → ERRADO (essa dupla é compatível e preserva a autonomia monetária)",
        ])],
        "reescrita": ("A trindade impossível identificada por Mundell refere-se à impossibilidade de combinar livre "
                      "mobilidade de capital, taxa de câmbio " + hl("fixa") + " e política monetária autônoma."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. O trilema envolve livre mobilidade de capitais, câmbio fixo e política monetária "
                             "autônoma; o câmbio flutuante é o que permite combinar capital livre e autonomia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00505
    {
        "id": "ECO-E2-L00505-1", "fonte_ref": "E2-L00505", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Numa economia aberta, se o governo realiza uma política fiscal ativa, evidencia-se redução das "
                      "exportações líquidas na mesma magnitude dos gastos do governo quando a autoridade monetária "
                      "garante liberdade de capitais e câmbio flexível."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Numa economia aberta, se o governo realiza uma política fiscal ativa, evidencia-se redução das "
                      "exportações líquidas <u>na mesma magnitude</u> dos gastos do governo quando a autoridade "
                      "monetária garante liberdade de capitais e câmbio flexível."),
        "poucas": ("Câmbio flexível + capital livre: a expansão fiscal valoriza a moeda até que " + vd("ΔNX = −ΔG")
                   + ". É o " + azb("crowding out cambial") + " total do Mundell-Fleming — a renda não muda."),
        "destrinchando": [
            "Por que “na mesma magnitude”? No equilíbrio, i = i* e a LM não se move (o BC não intervém no câmbio). "
            "Então Y fica igual; com Y e i iguais, consumo e investimento também. Da identidade Y = C + I + G + "
            "NX, se G sobe e Y, C, I não mudam, " + vd("NX cai exatamente o mesmo valor") + ".",
            "Mecanismo: G ↑ → pressão de alta dos juros → entrada de capitais → " + azb("valorização") + " → "
            "X ↓, M ↑ → a IS volta ao ponto de partida.",
            "Pela ótica da poupança: S − I = NX. O gasto público reduz a poupança nacional (S ↓); I fica igual; "
            "logo NX cai — e a contrapartida é a entrada de capital externo que financia o déficit (" + azb("déficits "
            "gêmeos") + ").",
            "“Liberdade de capitais” deve ser lida como " + vd("mobilidade perfeita") + " em pequena economia "
            "aberta. Com mobilidade apenas alta, NX cai menos que G e a renda sobe um pouco.",
            vm("Regra-âncora: flutuante + mobilidade perfeita → ΔNX = −ΔG, ΔY = 0."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O “na mesma magnitude” é o detalhe que assusta, mas decorre "
                       "da ineficácia total da fiscal. Variações com “câmbio fixo” no lugar de “câmbio flexível” "
                       "seriam ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…evidencia-se redução das exportações líquidas na mesma magnitude dos gastos do governo quando a "
            "autoridade monetária garante câmbio fixo.”</i> → ERRADO (troca de regime: no fixo, a renda sobe e NX "
            "não compensa G)",
            "<i>“…evidencia-se redução do investimento privado na mesma magnitude dos gastos do governo.”</i> → "
            "ERRADO (troca de conceito: com i = i*, o investimento não muda; quem cai é NX)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["na mesma magnitude"], "dificuldade": 2,
        "comentario_fonte": ("CERTO. Resultado clássico do Mundell-Fleming: a expansão fiscal eleva os juros, atrai "
                             "capital e valoriza o câmbio, reduzindo as exportações líquidas na mesma magnitude do "
                             "gasto e tornando a fiscal ineficaz."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00164-1, ECO-E2-L00658-1 (fiscal ineficaz sob câmbio flutuante e "
                    "mobilidade perfeita)",
                    "texto_corrigido: removido do comentário de origem um resíduo de outra questão (“4. Acerca dos "
                    "instrumentos de política comercial…”)"],
    },
    # ------------------------------------------------------------------ E2-L00564
    {
        "id": "ECO-E2-L00564-1", "fonte_ref": "E2-L00564", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação ao modelo IS-LM, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Supondo uma economia sob o regime de câmbio flutuante e com elevada mobilidade (embora "
                      "imperfeita) de capitais, de acordo com o modelo de Mundell-Fleming, os efeitos finais, "
                      "decorrentes de uma política fiscal expansionista, sobre a taxa de juros, a taxa de câmbio "
                      "Real/Dólar (R$/US$) e a renda agregada no país, comparativamente à situação prevalecente no "
                      "equilíbrio inicial, serão, respectivamente, aumento, redução e aumento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Supondo uma economia sob o regime de câmbio flutuante e com elevada mobilidade (embora "
                      "imperfeita) de capitais, de acordo com o modelo de Mundell-Fleming, os efeitos finais, "
                      "decorrentes de uma política fiscal expansionista, sobre a taxa de juros, a taxa de câmbio "
                      "Real/Dólar (R$/US$) e a renda agregada no país, comparativamente à situação prevalecente no "
                      "equilíbrio inicial, serão, respectivamente, <u>aumento, redução e aumento</u>."),
        "poucas": ("Mobilidade alta, mas imperfeita: a fiscal atrai capital e " + azb("valoriza") + " o real (R$/US$ "
                   + vd("cai") + "), o que devolve só " + azb("parte") + " do estímulo — juros e renda terminam "
                   + vd("acima") + " do ponto inicial."),
        "destrinchando": [
            "Com mobilidade " + vd("elevada, mas imperfeita") + ", a BP é positivamente inclinada e " + vd("menos "
            "inclinada que a LM") + ": juros um pouco acima de i* já atraem muito capital, mas não infinitamente.",
            "G ↑ → IS à direita → i e Y sobem → como a BP é mais plana que a LM, o ponto provisório fica acima "
            "dela → " + vd("superávit") + " → no câmbio flutuante, " + vd("valorização") + " (R$/US$ ↓).",
            "A valorização reduz NX: a IS recua parcialmente e a BP sobe (cada renda agora exige juros maiores "
            "para equilibrar as contas externas), até as três curvas se cruzarem em E₂.",
            "Saldo: " + vd("i ↑, R$/US$ ↓, Y ↑") + " — a fiscal funciona, mas pouco. Nos extremos: mobilidade "
            "perfeita → Y e i inalterados; mobilidade baixa → desvalorização e fiscal forte.",
            "Convenção: “taxa de câmbio R$/US$” é o preço do dólar em reais; " + vd("redução") + " = real mais "
            "forte.",
        ],
        "grafico_verso": "ECO-E2-L00564-1-V1",
        "dissecando": (cz("[detalhe · literalidade]") + " Item de três sinais em sequência; o detalhe decisivo é o "
                       "“embora imperfeita”, que permite aos juros e à renda ficarem acima do inicial. Quem aplica o "
                       "caso de mobilidade perfeita marca ERRADO pensando em “inalterado, redução, inalterado”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com perfeita mobilidade de capitais, os efeitos finais sobre juros, câmbio R$/US$ e renda serão, "
            "respectivamente, aumento, redução e aumento.”</i> → ERRADO (com mobilidade perfeita, juros e renda "
            "ficam inalterados)",
            "<i>“…com baixa mobilidade de capitais, os efeitos finais serão aumento, aumento e aumento.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": ["embora imperfeita"], "dificuldade": 2,
        "comentario_fonte": ("CERTO. Verso só com o gráfico IS-LM-BP (IS₁ → IS₂, BP quase horizontal) e o texto: a "
                             "elevação de i atrai capitais, aprecia o câmbio, reduz exportações líquidas e desloca a IS "
                             "parcialmente de volta; produto e juros maiores, fiscal pouco eficaz."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 093", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L00564-1-V1, gráfico didático)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00658
    {
        "id": "ECO-E2-L00658-1", "fonte_ref": "E2-L00658", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à economia internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Considere uma política fiscal expansionista representada pelo aumento dos gastos do governo em "
                      "um modelo Mundell-Fleming em uma pequena economia aberta e com perfeita mobilidade de "
                      "capitais. No regime de câmbio fixo, o produto aumenta; no de câmbio flutuante, o produto não "
                      "se altera."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere uma política fiscal expansionista representada pelo aumento dos gastos do governo em "
                      "um modelo Mundell-Fleming em uma pequena economia aberta e com perfeita mobilidade de "
                      "capitais. No regime de câmbio fixo, o produto <u>aumenta</u>; no de câmbio flutuante, o produto "
                      "<u>não se altera</u>."),
        "poucas": ("É o quadro central do Mundell-Fleming: " + azb("fixo") + " → o BC compra divisas, a LM acompanha "
                   "a IS e " + vd("Y ↑") + "; " + azb("flutuante") + " → a valorização derruba NX, a IS volta e "
                   + vd("Y não muda") + "."),
        "destrinchando": [
            "Ponto comum: G ↑ → IS para a direita → juros pressionados acima de i* → entrada de capitais. O que "
            "difere é quem absorve a pressão.",
            vd("Câmbio fixo") + ": o BC impede a valorização comprando dólares → base ↑ → LM para a direita → i "
            "volta a i* com renda maior. A moeda se ajusta à fiscal: " + azb("eficácia máxima") + ".",
            vd("Câmbio flutuante") + ": o câmbio absorve a pressão → valorização → NX ↓ → a IS volta → Y e i "
            "inalterados, " + vd("ΔNX = −ΔG") + ": " + azb("ineficácia total") + ".",
            "Quadro de quatro casas (mobilidade perfeita): fiscal — fixo eficaz, flutuante ineficaz; monetária — "
            "fixo ineficaz, flutuante eficaz. Origem: " + oc("Robert Mundell") + " e " + oc("J. Marcus Fleming")
            + " (início dos anos 1960); Mundell recebeu o Nobel de 1999.",
            "Hipóteses que sustentam o resultado: pequena economia (i* dado), preços rígidos, expectativas "
            "estáticas sobre o câmbio e Marshall-Lerner.",
        ],
        "dissecando": (cz("[literalidade]") + " Item-síntese que testa as duas casas da fiscal ao mesmo tempo. A "
                       "armadilha habitual é inverter os regimes; aqui eles estão na ordem certa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…No regime de câmbio flutuante, o produto aumenta; no de câmbio fixo, o produto não se "
            "altera.”</i> → ERRADO (regimes invertidos: esse é o resultado da política monetária)",
            "<i>“…No regime de câmbio fixo, as reservas internacionais aumentam.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. Câmbio fixo: o BC compra moeda estrangeira, a LM se desloca para a direita e o "
                             "produto aumenta. Câmbio flutuante: a valorização reduz as exportações líquidas, a IS "
                             "volta e o produto não muda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00144-1, ECO-E2-L00164-1, ECO-E2-L00505-1 (fiscal nos dois regimes "
                    "com mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L00728
    {
        "id": "ECO-E2-L00728-1", "fonte_ref": "E2-L00728", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Em relação aos conceitos macroeconômicos, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia aberta, com câmbio flexível e mobilidade de capitais imperfeita, uma política "
                      "monetária expansionista provoca desvalorização da moeda local no curto prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia aberta, com câmbio flexível e mobilidade de capitais <u>imperfeita</u>, uma "
                      "política monetária expansionista provoca <u>desvalorização da moeda local</u> no curto prazo."),
        "poucas": ("A expansão monetária reduz os juros domésticos; mesmo com mobilidade imperfeita, sai capital (ou "
                   "entra menos), e a renda maior eleva as importações: os dois efeitos " + azb("depreciam") + " a "
                   "moeda."),
        "destrinchando": [
            "M ↑ → LM para a direita → i ↓ e Y ↑. No balanço de pagamentos, os " + vd("dois canais apontam para o "
            "mesmo lado") + ": juros menores pioram a conta financeira; renda maior piora a balança comercial.",
            "Resultado: déficit → excesso de demanda por divisas → no câmbio flexível, " + vd("depreciação") + " "
            "(e = R$/US$ ↑). A depreciação eleva NX e desloca IS e BP para a direita, reforçando a alta da renda.",
            "Diferença em relação à fiscal: na expansão fiscal, os canais se opõem (juros ↑ atraem capital; renda "
            "↑ eleva importações), e o sinal do câmbio depende da mobilidade. Na monetária, o sinal é "
            + azb("inequívoco") + ", qualquer que seja a mobilidade — por isso o “imperfeita” não muda nada.",
            "Com mobilidade imperfeita, os juros finais ficam abaixo dos iniciais; com mobilidade perfeita, voltam "
            "a i*. Nos dois casos, câmbio depreciado e renda maior.",
            "Na " + azb("paridade descoberta de juros") + ": i = i* + expectativa de depreciação; cortar i exige "
            "que a moeda se deprecie hoje (" + oc("Dornbusch") + ", 1976, mostra que ela pode até “ultrapassar” "
            "o novo nível de longo prazo — " + azb("overshooting") + ").",
            vm("Regra-âncora: expansão monetária em câmbio flutuante → moeda deprecia, sempre."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " A ressalva “imperfeita” tenta fazer o candidato duvidar, "
                       "mas não altera o sinal: juros menores e renda maior pressionam o câmbio no mesmo sentido. "
                       "Seria ERRADO trocar “desvalorização” por “valorização” ou “monetária” por “fiscal”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política monetária expansionista provoca valorização da moeda local no curto prazo.”</i> → "
            "ERRADO (sentido trocado)",
            "<i>“…com mobilidade de capitais imperfeita, uma política fiscal expansionista provoca necessariamente "
            "desvalorização da moeda local.”</i> → ERRADO (modulador absoluto: depende de a BP ser mais ou menos "
            "inclinada que a LM)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["no curto prazo"], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A expansão monetária reduz os juros domésticos; mesmo com mobilidade imperfeita, "
                             "os ativos domésticos ficam menos atraentes, há saída de capitais e, no câmbio flexível, "
                             "depreciação da moeda local."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: comentário fundido com o da linha E2-L00783 (mesmo item, mesmo caderno)"],
    },
]
