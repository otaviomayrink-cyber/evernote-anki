"""Cards do lote de redação 13 — ECO, passada 03 (notas 70: IS-LM-BP; 73: teorias clássicas e neoclássicas do
comércio)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "bp": "📍 Curva BP e mobilidade de capital",
    "fixo": "🔒 Câmbio fixo",
    "flut": "🌊 Câmbio flutuante",
    "vant": "⛵ Vantagens absolutas e comparativas",
    "ho": "🧪 Heckscher-Ohlin e teoremas",
    "leon": "❓ Paradoxo de Leontief e termos de troca",
}

CMD_RT_ISLMBP = ("O modelo IS-LM-BP permite analisar os efeitos de políticas econômicas numa economia aberta. Sobre "
                 "este tema, julgue C ou E o item a seguir.")

CMD_ANTT = "Julgue o próximo item, tendo em vista os modelos macroeconômicos para economias abertas."

EXC_TPS25 = ("<p><i>O país A tem abundância de mão de obra, e o país B tem abundância de capital. A produção do bem "
             "X é mais intensiva em mão de obra, enquanto a produção do bem Y é mais intensiva em capital.</i></p>")

CMD_TPS25 = ("Considerando a situação hipotética a seguir e as teorias neoclássicas do comércio internacional, que "
             "aperfeiçoaram a análise proposta pela teoria clássica, incluindo a possibilidade de incorporar múltiplos "
             "fatores de produção, julgue o item seguinte.")

EXC_BANDA = ("<p><i>Um comentarista de rádio proferiu a seguinte frase a respeito do baterista de uma banda de rock: "
             "“O João não é o melhor baterista do mundo… sejamos sinceros, ele não é nem o melhor baterista da sua "
             "banda!”.</i></p>")

CMD_BANDA = ("A partir da situação hipotética a seguir, considerando que a habilidade musical de um membro daquela "
             "banda possa ser medida pela sua contribuição ao ganho monetário em um show e que Carlos, guitarrista da "
             "mesma banda, poderia ser o baterista da banda, julgue (C ou E) o item seguinte, tendo como referência a "
             "teoria das vantagens comparativas.")

CMD_COM = "Acerca das teorias do comércio internacional, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01631
    {
        "id": "ECO-E2-L01631-1", "fonte_ref": "E2-L01631", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("Com perfeita mobilidade de capital, países com regimes cambiais flexíveis tendem a ter menores "
                      "perdas, em termos de produto, do que países com regimes de câmbio fixo, ao serem acometidos "
                      "por fugas de capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com perfeita mobilidade de capital, países com regimes cambiais <u>flexíveis</u> tendem a ter "
                      "<u>menores</u> perdas, em termos de produto, do que países com regimes de câmbio fixo, ao "
                      "serem acometidos por fugas de capital."),
        "poucas": ("No câmbio flexível, a fuga de capitais " + azb("deprecia a moeda") + " e as exportações líquidas "
                   "amortecem o choque; no fixo, o Banco Central vende reservas, a " + azb("oferta de moeda "
                   "encolhe") + " e os juros sobem — o ajuste é recessivo."),
        "destrinchando": [
            "Fuga de capitais no Mundell-Fleming = alta do juro exigido pelos investidores (prêmio de risco ou "
            "juro externo maior): a " + azb("BP horizontal") + " sobe de i* para i* + prêmio. Para o país reter "
            "capital, o juro doméstico precisa subir até o novo patamar.",
            "<b>Câmbio fixo</b>: os capitais saem, há pressão de depreciação e o Banco Central vende divisas para "
            "segurar a paridade. Vender divisas é retirar moeda nacional de circulação: a " + vd("LM se desloca "
            "para a esquerda") + " até o juro doméstico alcançar a nova BP. Resultado: " + vd("i ↑ e Y ↓") + ", "
            "com perda de reservas.",
            "<b>Câmbio flexível</b>: o Banco Central não intervém, a oferta de moeda fica constante e a moeda se "
            + azb("deprecia") + ". A depreciação barateia exportações e encarece importações: a " + vd("IS vai "
            "para a direita") + ". No modelo-padrão, o produto até sobe; na prática, a depreciação funciona como "
            "<b>amortecedor</b> e a perda de produto é menor.",
            "Ressalva empírica: em economias com " + azb("dívida dolarizada") + " (descasamento cambial), a "
            "depreciação encarece passivos e pode ser contracionista — mas o item fala em “tendem a”, e o "
            "resultado canônico é o do câmbio flexível como absorvedor de choques.",
            rx("Brasil") + ": a crise de 1999 encerrou a âncora cambial do Plano Real depois de forte perda de "
            "reservas e juros muito altos para defender a paridade; o regime flutuante adotado desde então "
            "passou a absorver choques externos pelo câmbio.",
            vm("Regra-âncora: choque externo + câmbio fixo → ajuste por quantidades (moeda, juros, produto); "
               "câmbio flexível → ajuste pelo preço (câmbio)."),
        ],
        "grafico_verso": "ECO-E2-L01631-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " É o resultado de manual, protegido por "
                       "“tendem a”. 🔥 O mesmo professor cobra a versão invertida (“flexíveis tendem a ter "
                       "<b>maiores</b> perdas”), que é ERRADO: a pista é lembrar quem perde reservas e moeda na "
                       "defesa da paridade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…países com regimes cambiais flexíveis tendem a ter maiores perdas, em termos de produto…”</i> → "
            "ERRADO (inversão)",
            "<i>“Sob câmbio fixo, a fuga de capitais reduz as reservas internacionais e a base monetária.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tendem a"], "dificuldade": 1,
        "comentario_fonte": ("Três respostas de IA concordantes: no flexível a depreciação amortece (exportações "
                             "líquidas); no fixo o BC vende reservas, sobe juros e contrai a moeda; descrições de "
                             "dois gráficos IS-LM-BP (BP sobe; LM à esquerda no fixo; novo equilíbrio com Y maior "
                             "no flexível)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 470", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (painel do câmbio fixo em ECO-E2-L01631-1-V1)"},
                          {"ref": "IMAGEM 471", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (painel do câmbio flexível em ECO-E2-L01631-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01770-1 (mesmo curso; versão invertida, gabarito ERRADO)"],
    },
    # ------------------------------------------------------------------ E2-L01698
    {
        "id": "ECO-E2-L01698-1", "fonte_ref": "E2-L01698", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Sobre os conceitos e teorias da economia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Se uma pequena economia aberta com regime de câmbio flexível mantém os juros domésticos "
                      "inalterados quando o resto do mundo, diante de uma recessão, reduz suas taxas de juros, "
                      "deve-se esperar uma redução do saldo comercial desta economia diante do resto do mundo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se uma pequena economia aberta com regime de câmbio flexível mantém os juros domésticos "
                      "inalterados quando o resto do mundo, diante de uma recessão, reduz suas taxas de juros, "
                      "deve-se esperar uma <u>redução</u> do saldo comercial desta economia diante do resto do "
                      "mundo."),
        "poucas": ("Com i* em queda e i parado, abre-se o diferencial " + vd("i > i*") + ": entra capital, a moeda "
                   "doméstica se " + azb("aprecia") + ", exportar fica mais difícil e importar mais barato — o "
                   "saldo comercial cai."),
        "destrinchando": [
            "Pela " + azb("paridade descoberta de juros") + ", o retorno de aplicar no país é i; no exterior, "
            "i* + depreciação esperada + prêmio de risco. Se i passa a superar essa soma, o capital entra até o "
            "câmbio se ajustar.",
            "Sob câmbio flexível, o ajuste é feito pelo preço: a entrada de divisas " + vd("reduz E") + " (R$ por "
            "US$), isto é, aprecia a moeda nacional. No IS-LM-BP, a BP horizontal desce para o novo i*, a "
            "economia fica acima dela (superávit no balanço de pagamentos) e a apreciação desloca a IS para a "
            "esquerda.",
            "Canal comercial: moeda apreciada encarece os bens domésticos em moeda estrangeira e barateia as "
            "importações → " + vd("X ↓ e M ↑") + " → saldo comercial menor. É também por isso que a recessão "
            "externa se transmite: ela já reduz a demanda por exportações, e a apreciação reforça o efeito.",
            "Leitura de política: o país preservou a " + azb("autonomia monetária") + " (o trilema permite, com "
            "câmbio flexível), mas paga com perda de competitividade. Se acompanhasse o corte de juros externo, "
            "evitaria a apreciação.",
            vm("Regra-âncora: câmbio flexível + i > i* → entrada de capitais → apreciação → saldo comercial ↓."),
        ],
        "dissecando": (cz("[paráfrase fiel · contraintuitivo]") + " O item descreve o choque pelo lado de fora "
                       "(o mundo corta juros) e não diz “juros domésticos mais altos”: é preciso perceber que "
                       "manter i parado equivale a abrir um diferencial positivo. Quem lê “juros inalterados” "
                       "como “nada acontece” erra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…deve-se esperar uma depreciação da moeda doméstica e uma melhora do saldo comercial…”</i> → "
            "ERRADO (inversão: i > i* atrai capital e aprecia a moeda)",
            "<i>“…sob câmbio fixo, o Banco Central teria de comprar divisas, expandindo a base monetária.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "CONTRAINTUITIVO"], "moduladores": ["deve-se esperar"], "dificuldade": 2,
        "comentario_fonte": ("Três respostas concordantes: juros domésticos relativamente maiores atraem capital, "
                             "apreciam a moeda e reduzem o saldo comercial; menção ao trade-off entre autonomia "
                             "monetária e equilíbrio externo; imagem com a condição de paridade i > i* + Êe + PR."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 501", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (condição de paridade no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01702
    {
        "id": "ECO-E2-L01702-1", "fonte_ref": "E2-L01702", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("Avalie a proposição abaixo sobre criação de base monetária, meios de pagamento e taxa de "
                    "juros."),
        "rotulo_item": "Item",
        "assertiva": ("Em situação de perfeita mobilidade de capitais e regime de câmbio fixo, será nulo o efeito "
                      "líquido sobre a base monetária de uma compra de títulos domésticos no mercado aberto pelo "
                      "Banco Central."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em situação de perfeita mobilidade de capitais e regime de câmbio fixo, será "
                      "<u>nulo</u> o efeito <u>líquido</u> sobre a base monetária de uma compra de títulos "
                      "domésticos no mercado aberto pelo Banco Central."),
        "poucas": ("A compra de títulos injeta moeda, mas os juros caem, o capital sai e o BC precisa " 
                   + azb("vender reservas") + " para defender a paridade, recolhendo a mesma moeda: a base volta "
                   "ao ponto de partida."),
        "destrinchando": [
            "Balanço do Banco Central: a " + azb("base monetária") + " (passivo) tem como contrapartida, no "
            "ativo, os títulos domésticos (crédito interno) e as " + azb("reservas internacionais") + ". "
            "Por isso: " + vd("ΔB = Δ crédito interno + Δ reservas") + ".",
            "Sequência: compra de títulos → crédito interno ↑ e base ↑ → juros domésticos tendem a cair abaixo "
            "de i* → saída maciça de capitais → pressão de depreciação → o BC vende divisas e recolhe moeda "
            "nacional → reservas ↓ e base ↓. Com mobilidade perfeita, a saída só para quando " + vd("i = i*") + ", "
            "isto é, quando a base voltou ao nível inicial.",
            "Resultado: muda a <b>composição</b> do ativo do BC (mais títulos, menos reservas), não o tamanho da "
            "base. A LM vai à direita e volta; renda e juros ficam onde estavam.",
            "É o " + azb("trilema") + " (" + oc("Mundell") + "): com câmbio fixo e capitais livres, a "
            "política monetária perde a autonomia. A " + azb("esterilização") + " só adia o ajuste e esbarra no "
            "estoque de reservas.",
            vm("Regra-âncora: câmbio fixo + mobilidade perfeita → open market só troca títulos por reservas; "
               "a base monetária não muda."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item usa a contabilidade do BC (“efeito líquido sobre "
                       "a base”) em vez do vocabulário usual (“política monetária ineficaz”). O “líquido” é a "
                       "chave: há efeito bruto (a injeção inicial), anulado pela perda de reservas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a compra de títulos reduzirá as reservas internacionais e elevará a base monetária de forma "
            "permanente.”</i> → ERRADO (a base volta ao nível inicial)",
            "<i>“Sob câmbio flutuante e perfeita mobilidade, a mesma operação eleva a renda e deprecia a "
            "moeda.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["líquido"], "dificuldade": 2,
        "comentario_fonte": ("Três respostas concordantes (Mundell-Fleming, trilema): a expansão pressiona os juros "
                             "para baixo, sai capital, o BC vende reservas e recolhe a moeda injetada; efeito "
                             "líquido nulo. Imagem do gráfico IS-LM-BP com a LM indo e voltando."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 504", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo descrito no 📖)"}],
        "alertas": ["texto_corrigido: “será o nulo o efeito” → “será nulo o efeito” (erro de digitação da fonte); "
                    "retirado o número do item (“3”)"],
    },
    # ------------------------------------------------------------------ E2-L01770
    {
        "id": "ECO-E2-L01770-1", "fonte_ref": "E2-L01770", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("A respeito dos conceitos de taxa de câmbio e das relações entre câmbio, juros e inflação, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Países com regimes cambiais mais flexíveis tendem a ter maiores perdas, em termos de produto e "
                      "emprego, do que países com regimes de câmbio fixo, diante de fugas de capital."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Países com regimes cambiais mais flexíveis tendem a ter ") + vm("maiores")
                    + az(" perdas, em termos de produto e emprego, do que países com regimes de câmbio fixo, diante "
                         "de fugas de capital.")),
        "poucas": ("É o contrário: o câmbio flexível funciona como " + azb("absorvedor de choques") + " — a moeda se "
                   "deprecia e as exportações líquidas sustentam o produto —, enquanto o fixo exige "
                   + vm("juros altos e contração monetária") + " para defender a paridade."),
        "destrinchando": [
            "Fuga de capitais = investidores passam a exigir retorno maior para manter recursos no país (alta do "
            "prêmio de risco ou do juro externo). No IS-LM-BP, a " + azb("BP") + " sobe.",
            "<b>Câmbio fixo</b>: a saída de divisas pressiona o câmbio; o Banco Central vende reservas e, com "
            "isso, recolhe moeda nacional. A " + vd("LM recua") + ", os juros sobem até o novo patamar exigido e "
            "o produto cai. Se as reservas se esgotam, vem a desvalorização abrupta — às vezes com crise "
            "bancária e recessão ainda mais funda.",
            "<b>Câmbio flexível</b>: sem intervenção, a oferta de moeda não muda; a moeda se " + azb("deprecia")
            + ", as exportações ficam mais baratas, as importações mais caras, e a " + vd("IS avança")
            + ". O choque é absorvido pelo preço (câmbio), não pela quantidade (produto e emprego).",
            "A literatura empírica costuma confirmar a vantagem do câmbio flexível em choques externos, com a "
            "ressalva do " + azb("descasamento cambial") + ": se empresas e governo devem em dólar, a "
            "depreciação encarece as dívidas e pode ser contracionista.",
            vm("Regra-âncora: diante de choque externo, câmbio flexível amortece; câmbio fixo transmite o choque "
               "para juros, produto e emprego."),
        ],
        "dissecando": (cz("[inversão]") + " Troca de um único adjetivo (“maiores” no lugar de “menores”) inverte "
                       "o resultado canônico. 🔥 O curso cobra as duas versões; a pista é lembrar que, no fixo, "
                       "o BC <b>perde reservas e moeda</b> para segurar o câmbio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Países com regimes cambiais flexíveis tendem a ter menores perdas de produto diante de fugas de "
            "capital, porque a depreciação estimula as exportações líquidas.”</i> → CERTO",
            "<i>“Sob câmbio flexível, a fuga de capitais obriga o Banco Central a vender reservas, contraindo a "
            "base monetária.”</i> → ERRADO (troca de regime: isso ocorre no câmbio fixo)",
        ])],
        "reescrita": ("Países com regimes cambiais mais flexíveis tendem a ter " + hl("menores") + " perdas, em "
                      "termos de produto e emprego, do que países com regimes de câmbio fixo, diante de fugas de "
                      "capital."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tendem a"], "dificuldade": 1,
        "comentario_fonte": ("Comentário único: o trecho errado é “maiores perdas”; o câmbio flexível absorve "
                             "choques via depreciação; o fixo exige juros altos ou recessão. Duas imagens de "
                             "gráficos IS-LM-BP (BP sobe; LM à esquerda no fixo; IS à direita no flexível)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 534", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo descrito no 📖)"},
                          {"ref": "IMAGEM 535", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mecanismo descrito no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01631-1 (mesmo curso; versão correta do mesmo resultado, gabarito "
                    "CERTO, com gráfico fixo × flexível)"],
    },
    # ------------------------------------------------------------------ E2-L01771
    {
        "id": "ECO-E2-L01771-1", "fonte_ref": "E2-L01771", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("A eficácia da política fiscal, num país com taxa de câmbio fixa, será nula se houver perfeita "
                      "mobilidade de capitais, devido ao efeito deslocamento que supera o efeito multiplicador."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A eficácia da política fiscal, num país com taxa de câmbio fixa, será ") + vm("nula")
                    + az(" se houver perfeita mobilidade de capitais, ")
                    + vm("devido ao efeito deslocamento que supera o efeito multiplicador") + az(".")),
        "poucas": ("Com câmbio fixo e mobilidade perfeita, a política fiscal tem " + azb("eficácia máxima")
                   + ": os juros não sobem (não há crowding out) e a defesa da paridade obriga o BC a expandir a "
                   "moeda, reforçando o multiplicador."),
        "destrinchando": [
            "Sequência no " + oc("Mundell-Fleming") + ": G ↑ → IS à direita → renda e demanda por moeda sobem → "
            "os juros tendem a superar i* → entra capital → pressão de " + azb("apreciação") + " → para manter a "
            "paridade, o BC compra divisas e emite moeda → " + vd("LM à direita") + " até i voltar a i*.",
            "Resultado final: juros iguais a i*, renda muito maior. Como os juros não sobem, o investimento "
            "privado não é expulso: o " + azb("efeito deslocamento") + " (crowding out) é " + vd("nulo") + " e "
            "o multiplicador keynesiano opera por inteiro — até reforçado pela expansão monetária endógena.",
            "Onde a política fiscal é nula: no " + azb("câmbio flutuante") + " com mobilidade perfeita. Ali a "
            "entrada de capitais aprecia a moeda, as exportações líquidas caem e a IS volta ao lugar — é um "
            "crowding out <b>externo</b> (via câmbio), não via juros.",
            "Quadro de memória do Mundell-Fleming com mobilidade perfeita: " + vd("fixo") + " → fiscal máxima, "
            "monetária nula; " + vd("flutuante") + " → monetária máxima, fiscal nula.",
            vm("Regra-âncora: câmbio fixo + mobilidade perfeita → a política fiscal arrasta a monetária junto; "
               "eficácia máxima."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " O item cola o resultado do câmbio "
                       "<b>flutuante</b> (fiscal nula) no câmbio fixo e ainda inventa a causa (“deslocamento que "
                       "supera o multiplicador”), que não existe com juros presos a i*. Pista: no fixo, o BC "
                       "acomoda a expansão fiscal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A eficácia da política fiscal, num país com câmbio flutuante, será nula se houver perfeita "
            "mobilidade de capitais.”</i> → CERTO",
            "<i>“Sob câmbio fixo e perfeita mobilidade, a expansão fiscal eleva as reservas internacionais e a "
            "base monetária.”</i> → CERTO",
        ])],
        "reescrita": ("A eficácia da política fiscal, num país com taxa de câmbio fixa, será " + hl("máxima")
                      + " se houver perfeita mobilidade de capitais, " + hl("pois não há efeito deslocamento: a "
                      "expansão monetária exigida pela defesa do câmbio reforça o efeito multiplicador") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["nula"], "dificuldade": 1,
        "comentario_fonte": ("Duas respostas concordantes: a fiscal é altamente eficaz sob câmbio fixo e mobilidade "
                             "perfeita; o BC compra divisas e expande a moeda; não há crowding out porque os juros "
                             "não sobem. Imagem com três diagramas do mecanismo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 536", "tipo_fonte": "DIAGRAMA", "lado": "verso",
                           "acao": "cortada (mecanismo descrito no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01773-1 (mesmo curso; fiscal sob câmbio fixo, alta × baixa "
                    "mobilidade)"],
    },
    # ------------------------------------------------------------------ E2-L01772
    {
        "id": "ECO-E2-L01772-1", "fonte_ref": "E2-L01772", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("Num regime de câmbio flexível, a eficácia da política monetária será maior que numa economia "
                      "fechada, não importando qual o grau de mobilidade de capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Num regime de câmbio flexível, a eficácia da política monetária será <u>maior</u> que numa "
                      "economia fechada, <u>não importando qual o grau de mobilidade de capital</u>."),
        "poucas": ("Com câmbio flexível, a expansão monetária ganha um " + azb("segundo canal") + ": além dos juros, "
                   "a " + azb("depreciação") + " eleva as exportações líquidas. Isso vale com mobilidade nula, "
                   "baixa, alta ou perfeita — muda só a intensidade."),
        "destrinchando": [
            "Economia fechada: M ↑ → i ↓ → I ↑ → Y ↑ (só o canal dos juros). Economia aberta com câmbio "
            "flexível: o mesmo canal mais o " + azb("canal cambial") + ", que desloca a IS para a direita.",
            "<b>Mobilidade nula</b> (BP vertical): a renda maior eleva as importações, o saldo externo fica "
            "negativo, a moeda se deprecia, e a depreciação desloca IS e BP para a direita. Mesmo sem fluxos "
            "financeiros, o câmbio soma demanda.",
            "<b>Mobilidade alta ou perfeita</b>: a queda de i provoca saída de capitais e depreciação mais forte; "
            "no limite (BP horizontal), a renda sobe até os juros voltarem a i* — " + vd("eficácia máxima") + ".",
            "Logo, o “não importando o grau de mobilidade” está protegido: o grau muda <b>quanto</b> a política "
            "monetária é mais eficaz, não <b>se</b> ela é mais eficaz que na economia fechada.",
            vm("Regra-âncora: câmbio flexível sempre soma o canal cambial à política monetária; câmbio fixo "
               "sempre a anula."),
        ],
        "dissecando": (cz("[contraintuitivo · detalhe]") + " A expressão “não importando” soa como modulador "
                       "absoluto e induz ao ERRADO, mas aqui a generalização é verdadeira: em todos os graus de "
                       "mobilidade a depreciação reforça a expansão. Desconfie de absolutos, mas teste-os."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Num regime de câmbio fixo, a eficácia da política monetária será maior que numa economia "
            "fechada.”</i> → ERRADO (troca de regime: no fixo ela é anulada)",
            "<i>“Sob câmbio flexível, a política monetária só é mais eficaz que na economia fechada se houver "
            "mobilidade perfeita de capitais.”</i> → ERRADO (restrição indevida)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["não importando"], "dificuldade": 2,
        "comentario_fonte": ("Duas respostas curtas e concordantes: com câmbio flexível a política monetária opera "
                             "por dois canais (juros e câmbio); a depreciação estimula as exportações líquidas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01774-1 (mesmo curso; política monetária sob câmbio fixo, “não "
                    "importando o grau de mobilidade”)"],
    },
    # ------------------------------------------------------------------ E2-L01773
    {
        "id": "ECO-E2-L01773-1", "fonte_ref": "E2-L01773", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("Num regime de câmbio fixo, a política fiscal expansionista é menos eficaz com alta mobilidade "
                      "de capital do que com baixa mobilidade, pois a tendência de apreciação da moeda doméstica "
                      "será revertida pelo aumento de oferta de moeda pelo BC, atuando contra a política fiscal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Num regime de câmbio fixo, a política fiscal expansionista é ") + vm("menos")
                    + az(" eficaz com alta mobilidade de capital do que com baixa mobilidade, pois a tendência de "
                         "apreciação da moeda doméstica será revertida pelo aumento de oferta de moeda pelo BC, ")
                    + vm("atuando contra") + az(" a política fiscal.")),
        "poucas": ("O mecanismo descrito está certo, mas a conclusão está invertida: a emissão do BC para segurar o "
                   "câmbio " + azb("reforça") + " a expansão fiscal, que por isso é " + vm("mais") + " eficaz com "
                   "alta mobilidade."),
        "destrinchando": [
            "<b>Alta mobilidade</b> (BP menos inclinada que a LM, no limite horizontal): a expansão fiscal eleva "
            "os juros, entra muito capital, surge superávit no balanço de pagamentos e pressão de apreciação. O "
            "BC compra divisas e emite moeda: a " + vd("LM vai para a direita") + " e a renda sobe além do "
            "efeito fiscal isolado.",
            "<b>Baixa mobilidade</b> (BP mais inclinada que a LM): o capital que entra não compensa as importações "
            "trazidas pela renda maior; o balanço de pagamentos fica " + vd("deficitário") + ", a pressão é de "
            "depreciação, o BC vende reservas e recolhe moeda — a " + vd("LM recua") + " e corta parte do ganho "
            "de renda.",
            "Por isso, sob câmbio fixo, a eficácia fiscal " + azb("cresce com a mobilidade de capital") + ": é "
            "máxima com mobilidade perfeita e mínima com mobilidade nula. No câmbio flutuante ocorre o inverso "
            "(a apreciação expulsa exportações líquidas, e a fiscal se anula com mobilidade perfeita).",
            "O critério gráfico: compare as inclinações de " + azb("BP e LM") + ". BP mais plana que a LM → "
            "expansão fiscal gera superávit externo; BP mais íngreme → gera déficit.",
            vm("Regra-âncora: câmbio fixo → quanto mais mobilidade, mais a moeda acompanha a política fiscal e "
               "maior sua eficácia."),
        ],
        "grafico_verso": "ECO-E2-L01773-1-V1",
        "dissecando": (cz("[inversão · meia-verdade]") + " A oração do meio (BC expande a moeda para reverter a "
                       "apreciação) é verdadeira; o examinador inverteu o comparativo e o efeito dessa emissão. "
                       "Pista: moeda a mais com IS deslocada para a direita só pode <b>somar</b> renda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Num regime de câmbio flutuante, a política fiscal expansionista é menos eficaz com alta "
            "mobilidade de capital do que com baixa mobilidade.”</i> → CERTO",
            "<i>“Sob câmbio fixo e baixa mobilidade de capital, a expansão fiscal gera superávit no balanço de "
            "pagamentos.”</i> → ERRADO (com BP mais inclinada que a LM, gera déficit)",
        ])],
        "reescrita": ("Num regime de câmbio fixo, a política fiscal expansionista é " + hl("mais") + " eficaz com "
                      "alta mobilidade de capital do que com baixa mobilidade, pois a tendência de apreciação da "
                      "moeda doméstica será revertida pelo aumento de oferta de moeda pelo BC, " + hl("reforçando")
                      + " a política fiscal."),
        "tipo_erro": ["INVERSAO", "MEIA_VERDADE"], "moduladores": ["menos"], "dificuldade": 2,
        "comentario_fonte": ("Duas respostas concordantes: com alta mobilidade e câmbio fixo a fiscal é mais eficaz; "
                             "a intervenção do BC reforça a fiscal; com baixa mobilidade a expansão monetária "
                             "induzida é menor. Duas imagens de gráficos de política fiscal sob câmbio fixo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 537", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01773-1-V1, painel de alta mobilidade)"},
                          {"ref": "IMAGEM 538", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01773-1-V1, painel de baixa mobilidade)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01771-1 (mesmo curso; fiscal sob câmbio fixo e mobilidade perfeita)",
                    "nota_redacao: o comentário da fonte remetia à “questão 13” do mesmo simulado; remissão "
                    "eliminada"],
    },
    # ------------------------------------------------------------------ E2-L01774
    {
        "id": "ECO-E2-L01774-1", "fonte_ref": "E2-L01774", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("A política monetária num regime de câmbio fixo será sempre ineficaz, não importando o grau de "
                      "mobilidade de capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A política monetária num regime de câmbio fixo será <u>sempre</u> ineficaz, <u>não importando "
                      "o grau de mobilidade de capital</u>."),
        "poucas": ("Com câmbio fixo, a oferta de moeda fica " + azb("endógena") + ": toda expansão gera déficit no "
                   "balanço de pagamentos, perda de reservas e recolhimento da moeda. O grau de mobilidade muda só a "
                   "<b>velocidade</b> do ajuste."),
        "destrinchando": [
            "Expansão monetária → i ↓ e Y ↑. Os dois efeitos pioram o balanço de pagamentos: juros menores fazem "
            "sair capital (conta financeira) e renda maior eleva importações (conta corrente). Com qualquer grau "
            "de mobilidade, surge " + vd("déficit no BP") + ".",
            "Para defender a paridade, o BC vende reservas e recolhe moeda; a " + vd("LM volta") + " até o ponto "
            "inicial, onde IS, LM e BP se cruzam. Com mobilidade perfeita, o retorno é instantâneo; com "
            "mobilidade nula, ele ocorre pela conta corrente, mais devagar — mas o destino é o mesmo.",
            "A " + azb("esterilização") + " (o BC compra títulos para repor a moeda perdida) só prolonga o "
            "déficit e consome reservas: não é solução duradoura.",
            "É uma das pontas do " + azb("trilema") + ": quem fixa o câmbio subordina a moeda à paridade. Em "
            "contrapartida, a política fiscal é eficaz sob câmbio fixo — tanto mais quanto maior a mobilidade.",
            vm("Regra-âncora: câmbio fixo → política monetária ineficaz (no equilíbrio final), qualquer que seja "
               "a mobilidade de capital."),
        ],
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Dois absolutos (“sempre”, “não importando”) "
                       "que, desta vez, estão certos: o resultado do Mundell-Fleming para a moeda no câmbio fixo "
                       "independe da mobilidade. O que depende da mobilidade é a eficácia <b>fiscal</b> — é "
                       "essa a troca que a banca costuma fazer."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política fiscal num regime de câmbio fixo será sempre ineficaz, não importando o grau de "
            "mobilidade de capital.”</i> → ERRADO (troca de conceito: a fiscal é eficaz no fixo)",
            "<i>“Sob câmbio fixo, a política monetária só é ineficaz quando há perfeita mobilidade de "
            "capital.”</i> → ERRADO (restrição indevida)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["sempre", "não importando"], "dificuldade": 1,
        "comentario_fonte": ("Duas respostas concordantes: resultado clássico do Mundell-Fleming; com câmbio fixo o "
                             "BC perde autonomia e subordina a moeda à paridade (trindade impossível)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01702-1 (mesmo curso; open market sob câmbio fixo)"],
    },
    # ------------------------------------------------------------------ E3-L00137
    {
        "id": "ECO-E3-L00137-1", "fonte_ref": "E3-L00137", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT,
        "rotulo_item": "Item",
        "assertiva": ("Se o Banco Central fixar a taxa nominal de câmbio, o aumento dos gastos do governo gerará "
                      "apreciação da taxa real de câmbio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o Banco Central fixar a taxa <u>nominal</u> de câmbio, o aumento dos gastos do governo "
                      "gerará apreciação da taxa <u>real</u> de câmbio."),
        "poucas": ("Com E fixo, a expansão fiscal aquece a demanda e eleva os " + azb("preços domésticos")
                   + "; como " + vd("e = E·P*/P") + ", P maior com E parado significa câmbio real menor — "
                   + azb("apreciação real") + "."),
        "destrinchando": [
            azb("Taxa real de câmbio") + ": " + vd("e = E × P* / P") + " (E em R$ por US$; P* preços externos; "
            "P preços domésticos). Mede quantos bens nacionais custa um bem estrangeiro. e ↓ = "
            + azb("apreciação real") + ": os bens do país ficam relativamente mais caros, e ele perde "
            "competitividade.",
            "Mecanismo: G ↑ → IS à direita → renda e juros tendem a subir → entra capital → pressão de "
            "apreciação <b>nominal</b>. Como o BC fixou E, ele compra divisas e emite moeda (LM à direita). A "
            "demanda agregada sobe duplamente (gasto + moeda) e pressiona P, sobretudo nos " + azb("bens não "
            "comercializáveis") + " (serviços, construção, aluguéis).",
            "Síntese: a apreciação que o câmbio nominal não pode fazer “migra” para o câmbio real pela via dos "
            "preços. No câmbio flutuante, a mesma expansão apreciaria E diretamente.",
            rx("Brasil") + ": no período de âncora cambial do Plano Real (1994–1999), câmbio quase fixo, "
            "déficits fiscais e entrada de capitais conviveram com apreciação real, déficits em conta corrente "
            "crescentes e, por fim, o abandono da âncora em janeiro de 1999.",
            vm("Regra-âncora: câmbio nominal fixo + expansão fiscal → P ↑ → câmbio real ↓ (apreciação real)."),
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " O item joga com a distinção nominal × real: quem lê "
                       "“câmbio fixo” e conclui “o câmbio não muda” marca ERRADO. A pista é o adjetivo "
                       "<b>real</b>, que inclui preços — e preços se movem."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o Banco Central fixar a taxa nominal de câmbio, o aumento dos gastos do governo deixará "
            "inalterada a taxa real de câmbio.”</i> → ERRADO (ignora a alta de P)",
            "<i>“…o aumento dos gastos do governo gerará depreciação da taxa real de câmbio.”</i> → ERRADO "
            "(inversão)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Sete comentários empilhados, todos pelo CERTO: e = E·P*/P; expansão fiscal com E fixo "
                             "eleva P (sobretudo não comercializáveis) e aprecia o câmbio real; canal Mundell-Fleming "
                             "(entrada de capitais, compra de divisas, expansão monetária); trilema; Plano Real. Um "
                             "deles atribui a apreciação real à alta de juros e à entrada de capitais, sem passar "
                             "pelos preços (impreciso com E fixo)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 129", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (mecanismo no 📖)"},
                          {"ref": "IMAGEM 130", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (mecanismo no 📖)"},
                          {"ref": "IMAGEM 131", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (e = E·P*/P no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E3-L00140-1 (mesma prova; expansão fiscal, reservas e base monetária)"],
    },
    # ------------------------------------------------------------------ E3-L00140
    {
        "id": "ECO-E3-L00140-1", "fonte_ref": "E3-L00140", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_ANTT,
        "rotulo_item": "Item",
        "assertiva": ("Se houver perfeita mobilidade de capitais, a expansão fiscal acarretará queda das reservas "
                      "internacionais e da base monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se houver perfeita mobilidade de capitais, a expansão fiscal acarretará ") + vm("queda")
                    + az(" das reservas internacionais e da base monetária.")),
        "poucas": ("A expansão fiscal puxa os juros para cima e " + azb("atrai") + " capital. Sob câmbio fixo, o BC "
                   "compra divisas: reservas e base " + vd("sobem") + ". Sob câmbio flutuante, não há intervenção: "
                   "ficam inalteradas. Em nenhum caso caem."),
        "destrinchando": [
            "Com " + azb("mobilidade perfeita") + " a BP é horizontal em i*. A expansão fiscal desloca a IS para a "
            "direita e cria a tendência i > i*: o país recebe capital, não perde.",
            "<b>Câmbio fixo</b>: a entrada de divisas pressiona a apreciação; para segurar a paridade, o BC "
            "compra moeda estrangeira (" + vd("reservas ↑") + ") pagando com moeda nacional (" + vd("base "
            "monetária ↑") + "). A LM acompanha a IS e a renda sobe muito — fiscal com eficácia máxima.",
            "<b>Câmbio flutuante</b>: o BC não compra nem vende divisas; a moeda se aprecia, as exportações "
            "líquidas caem e a IS volta ao lugar. " + vd("Reservas e base inalteradas") + "; a fiscal é "
            "ineficaz para a renda.",
            "Quando reservas e base <b>caem</b>? Em choques que geram saída de capitais sob câmbio fixo: expansão "
            "<b>monetária</b> (juros menores), fuga de capitais, alta do juro externo.",
            vm("Regra-âncora: sob câmbio fixo, o que atrai capital (fiscal expansionista) aumenta reservas e base; "
               "o que expulsa capital (monetária expansionista) as reduz."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item atribui à política fiscal o efeito típico da "
                       "expansão <b>monetária</b> sob câmbio fixo. O regime cambial omitido não salva a assertiva: "
                       "no fixo as variáveis sobem e no flutuante ficam paradas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio fixo e perfeita mobilidade de capitais, a expansão monetária acarretará queda das "
            "reservas internacionais, sem alterar a base monetária no equilíbrio final.”</i> → CERTO",
            "<i>“Sob câmbio flutuante e perfeita mobilidade, a expansão fiscal eleva as reservas "
            "internacionais.”</i> → ERRADO (no flutuante o BC não intervém)",
        ])],
        "reescrita": ("Se houver perfeita mobilidade de capitais, a expansão fiscal acarretará " + hl("aumento")
                      + " das reservas internacionais e da base monetária" + hl(", caso o câmbio seja fixo (no "
                      "flutuante, ambas ficam inalteradas)") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Sete comentários concordantes no ERRADO: no fixo, o BC compra divisas e reservas e base "
                             "sobem; no flutuante, nada muda nas reservas e na base. Um deles justifica a alta dos "
                             "juros pelo BC “contendo a inflação” (mecanismo alheio ao modelo)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E3-L00137-1 (mesma prova; expansão fiscal sob câmbio fixo e câmbio real)"],
    },
    # ------------------------------------------------------------------ E3-L00170
    {
        "id": "ECO-E3-L00170-1", "fonte_ref": "E3-L00170", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "ANTT/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "A partir da teoria macroeconômica, julgue o seguinte item.",
        "rotulo_item": "Item",
        "assertiva": ("Em um modelo Mundell-Fleming com perfeita mobilidade de capitais, a taxa de juros doméstica "
                      "não pode ser livremente determinada pela autoridade monetária."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("Em um modelo Mundell-Fleming com perfeita mobilidade de capitais, a taxa de juros doméstica "
                       "não pode ser ") + vm("livremente determinada") + az(" pela autoridade monetária.")),
        "poucas": ("No modelo-padrão a assertiva é verdadeira (" + vd("i = i*") + " em qualquer regime), mas o item "
                   "não diz o regime cambial, e no " + azb("câmbio flutuante") + " o BC recupera a autonomia "
                   "monetária — daí a ambiguidade que levou à anulação."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "Item anulado. O motivo provável é a omissão do regime cambial somada à vagueza de "
                          "“livremente determinada”: no câmbio fixo, o BC perde o controle da moeda e dos juros "
                          "(CERTO sem discussão); no flutuante, ele controla a oferta de moeda e faz política "
                          "eficaz, embora o juro de equilíbrio continue preso a i*. Pela leitura canônica do "
                          "modelo, a resposta mais defensável seria " + vd("CERTO") + ".")],
        "destrinchando": [
            "Com " + azb("mobilidade perfeita") + ", qualquer diferença entre i e i* provoca fluxos ilimitados de "
            "capital: a BP é horizontal e o equilíbrio exige " + vd("i = i*") + " (pequena economia aberta, "
            "sem prêmio de risco nem expectativa de variação cambial).",
            "<b>Câmbio fixo</b>: se o BC tenta baixar os juros, sai capital, ele vende reservas e a moeda volta; "
            "se tenta subir, entra capital, ele compra divisas e emite. A oferta de moeda é endógena — política "
            "monetária ineficaz.",
            "<b>Câmbio flutuante</b>: o BC controla M; uma expansão reduz i momentaneamente, a moeda se deprecia, "
            "as exportações líquidas sobem e a renda aumenta até que i volte a i*. A política monetária é "
            "<b>eficaz sobre a renda</b>, mas o juro de equilíbrio continua determinado lá fora.",
            "Daí a disputa de interpretação: “determinar livremente os juros” (falso nos dois regimes, no "
            "equilíbrio) × “ter autonomia monetária” (verdadeiro no flutuante, pelo " + azb("trilema") + ").",
            vm("Regra-âncora: mobilidade perfeita → i = i* em qualquer regime; o que muda com o câmbio é a "
               "eficácia da política monetária sobre a renda."),
        ],
        "dissecando": (cz("[outro: omissão do regime cambial]") + " O examinador quis testar a paridade de juros "
                       "(BP horizontal), mas deixou o regime em aberto e usou um verbo vago. Em prova, quando o "
                       "item de Mundell-Fleming não diz o regime, verifique se a conclusão vale para os dois — "
                       "aqui valia no equilíbrio, mas abria flanco no flutuante."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em um modelo Mundell-Fleming com perfeita mobilidade de capitais e câmbio fixo, a autoridade "
            "monetária não controla a oferta de moeda.”</i> → CERTO",
            "<i>“Com perfeita mobilidade de capitais e câmbio flutuante, a política monetária é ineficaz para "
            "alterar a renda.”</i> → ERRADO (troca de regime: é eficaz)",
        ])],
        "tipo_erro": ["OUTRO"], "moduladores": ["livremente"], "dificuldade": 2,
        "comentario_fonte": ("Anotação “ANULADA — pq não especificou o câmbio” e seis respostas de IA: a maioria "
                             "indica CERTO como resposta provável (i = i* em qualquer regime); uma sustenta que no "
                             "flutuante a assertiva seria falsa ou discutível. Imagem com quatro gráficos IS-LM-BP "
                             "fixo × flexível, ilegível."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 208", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (transcrição ilegível; conteúdo no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0444
    {
        "id": "ECO-E1-0444-1", "fonte_ref": "E1-0444", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Julho/2025", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("Conflitos comerciais entre países, conhecidos como guerras comerciais, têm se tornado eventos "
                    "recorrentes na economia global contemporânea. Geralmente caracterizadas pela imposição "
                    "recíproca de tarifas, essas disputas afetam tanto o fluxo de bens quanto as expectativas dos "
                    "agentes econômicos. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Do ponto de vista da teoria das vantagens comparativas, a guerra comercial representa uma "
                      "realocação eficiente de recursos, pois força os países a se especializarem ainda mais naquilo "
                      "que produzem com menor custo absoluto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Do ponto de vista da teoria das vantagens comparativas, a guerra comercial representa uma "
                       "realocação ") + vm("eficiente") + az(" de recursos, pois ")
                    + vm("força os países a se especializarem ainda mais") + az(" naquilo que produzem com menor "
                                                                                 "custo ") + vm("absoluto")
                    + az(".")),
        "poucas": ("Tarifas recíprocas " + azb("reduzem") + " a especialização: cada país volta a produzir "
                   "internamente o que importava mais barato. E a teoria ricardiana fala em custo "
                   + vm("de oportunidade") + " (relativo), não absoluto."),
        "destrinchando": [
            "Pela teoria das " + azb("vantagens comparativas") + " (" + oc("David Ricardo") + ", <i>Princípios "
            "de Economia Política e Tributação</i>, 1817), cada país ganha ao se especializar no bem de menor "
            + azb("custo de oportunidade") + " e importar o resto. O ganho vem justamente da especialização e "
            "da troca.",
            "Uma tarifa encarece o importado e protege a produção doméstica menos eficiente: recursos migram para "
            "setores em que o país <b>não</b> tem vantagem comparativa. Há " + azb("peso morto") + " de produção "
            "(produzir caro o que se comprava barato) e de consumo (consumidores compram menos).",
            "Em guerra comercial, as tarifas são recíprocas: os dois lados perdem acesso a mercados, as "
            "exportações de quem tem vantagem comparativa encolhem, e o comércio mundial se contrai — o oposto de "
            "aprofundar a especialização.",
            "O “custo absoluto” é o critério de " + oc("Adam Smith") + " (vantagem absoluta). Ricardo mostrou que, "
            "mesmo sem vantagem absoluta em nada, um país ganha com o comércio se especializar-se pela vantagem "
            "<b>relativa</b>.",
            vm("Regra-âncora: barreiras comerciais desfazem especialização e geram perda de bem-estar; o critério "
               "de Ricardo é o custo de oportunidade."),
        ],
        "dissecando": (cz("[inversão · troca de conceito]") + " O item inverte o efeito da guerra comercial e, de "
                       "quebra, troca o critério ricardiano (relativo) pelo smithiano (absoluto). Bastaria o "
                       "“absoluto” para marcar ERRADO num item que abre com “vantagens comparativas”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Do ponto de vista da teoria das vantagens comparativas, a guerra comercial gera perda de "
            "bem-estar, pois reduz a especialização baseada no custo de oportunidade.”</i> → CERTO",
            "<i>“Uma tarifa de importação elimina o peso morto, porque a receita do governo compensa a perda do "
            "consumidor.”</i> → ERRADO (a receita compensa só parte da perda)",
        ])],
        "reescrita": ("Do ponto de vista da teoria das vantagens comparativas, a guerra comercial representa uma "
                      "realocação " + hl("ineficiente") + " de recursos, pois " + hl("reduz a especialização dos "
                      "países") + " naquilo que produzem com menor custo " + hl("de oportunidade") + "."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["ainda mais"], "dificuldade": 1,
        "comentario_fonte": ("Comentário curto (repetido na linha duplicada E1-0546): o livre comércio aloca "
                             "recursos de modo eficiente; guerras comerciais distorcem preços, impedem a "
                             "especialização e causam perdas de bem-estar."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0546 (mesmo item e mesmo comentário) fundida neste card",
                    "texto_corrigido: “paises” → “países”; retirado o número do item (“227.”)"],
    },
    # ------------------------------------------------------------------ E1-0641
    {
        "id": "ECO-E1-0641-1", "fonte_ref": "E1-0641", "destino": "73", "subtema": H2["leon"],
        "tipo": "C/E", "banca": "Simulado Sapientia", "prova": "Set/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": "Acerca do crescimento econômico e dos termos de troca no comércio internacional, julgue o item.",
        "aviso_frente": "Enunciado reconstruído: na fonte, a frente era só uma imagem, não preservada.",
        "rotulo_item": "Item",
        "assertiva": ("O crescimento enviesado pela exportação — aquele que expande desproporcionalmente as "
                      "possibilidades de produção de um país na direção do bem que ele exporta — tende a reduzir o "
                      "preço relativo desse bem e, assim, a piorar os termos de troca do país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O crescimento enviesado pela exportação — aquele que expande desproporcionalmente as "
                      "possibilidades de produção de um país na direção do bem que ele exporta — tende a "
                      "<u>reduzir</u> o preço relativo desse bem e, assim, a <u>piorar</u> os termos de troca do "
                      "país."),
        "poucas": ("Se o país passa a ofertar muito mais do que exporta, a " + azb("oferta relativa mundial")
                   + " desse bem aumenta e seu preço relativo cai: os " + azb("termos de troca") + " (Pₓ/Pₘ) "
                   "pioram."),
        "destrinchando": [
            azb("Termos de troca") + " = preço das exportações ÷ preço das importações. No " + azb("modelo-padrão "
            "de comércio") + " de " + oc("Krugman e Obstfeld") + " (<i>Economia Internacional</i>), eles são "
            "dados pelo cruzamento da oferta relativa (OR) e da demanda relativa (DR) mundiais.",
            "Crescimento " + azb("enviesado pela exportação") + ": a FPP se expande mais na direção do bem "
            "exportado. A oferta relativa mundial desse bem sobe, a OR se desloca e o preço relativo do "
            "exportado " + vd("cai") + " → termos de troca do país que cresceu " + vd("pioram") + " (e os dos "
            "parceiros melhoram).",
            "Espelho: crescimento " + azb("enviesado pela importação") + " (expande o bem que o país importa) "
            "reduz a oferta relativa mundial do bem que ele exporta e " + vd("melhora") + " seus termos de troca.",
            "Caso extremo: o " + azb("crescimento empobrecedor") + " (" + oc("Jagdish Bhagwati") + ", 1958) — a "
            "piora dos termos de troca é tão grande que supera o ganho de produção e o país fica pior. Exige "
            "crescimento fortemente enviesado e OR/DR muito inclinadas; é tido mais como possibilidade teórica.",
            "Ponte com a " + azb("CEPAL") + ": a tese de " + oc("Prebisch") + " e " + oc("Singer") + " sobre a "
            "deterioração dos termos de troca da periferia exportadora de produtos primários dialoga com essa "
            "lógica.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de manual protegida por “tende "
                       "a”. A armadilha usual é trocar o sentido (crescimento enviesado pela exportação "
                       "<b>melhora</b> os termos de troca) ou transformar o caso extremo em regra (“sempre reduz "
                       "o bem-estar”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O crescimento enviesado pela importação tende a piorar os termos de troca do país que "
            "cresce.”</i> → ERRADO (inversão: tende a melhorá-los)",
            "<i>“O crescimento enviesado pela exportação sempre reduz o bem-estar do país que cresce.”</i> → "
            "ERRADO (modulador absoluto: o crescimento empobrecedor é caso extremo)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": ("Comentário curto: crescimento que expande desproporcionalmente a produção na direção "
                             "do bem exportado é enviesado pela exportação; aumenta a produção do exportado em "
                             "relação ao importado, reduz seu preço relativo e piora os termos de troca."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "image (186).png", "tipo_fonte": "QUESTÃO EM IMAGEM", "lado": "frente",
                           "acao": "texto reconstruído pelo comentário"}],
        "alertas": ["texto_reconstruido: frente original era só a imagem image (186).png; assertiva reconstruída a "
                    "partir do comentário (que a reproduz como definição + conclusão, gabarito CERTO); redação "
                    "exata do simulado não localizada em busca na web — conferir com a imagem"],
    },
    # ------------------------------------------------------------------ E1-0673
    {
        "id": "ECO-E1-0673-1", "fonte_ref": "E1-0673", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_TPS25,
        "excerto": EXC_TPS25,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o teorema de Samuelson-Stolper, uma política protecionista voltada à importação "
                      "do bem Y no país B tende a aumentar a remuneração da mão de obra no país B."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o teorema de Samuelson-Stolper, uma política protecionista voltada à "
                       "importação do bem Y no país B tende a aumentar a remuneração ") + vm("da mão de obra")
                    + az(" no país B.")),
        "poucas": ("Proteger Y eleva o preço doméstico de Y, que é " + azb("intensivo em capital") + ". Pelo "
                   "Stolper-Samuelson, sobe a remuneração real do " + vm("capital") + " e cai a do trabalho."),
        "destrinchando": [
            "Teorema de " + azb("Stolper-Samuelson") + " (" + oc("Stolper e Samuelson") + ", 1941): no modelo "
            "2 × 2 × 2 de Heckscher-Ohlin, a alta do preço relativo de um bem eleva a remuneração real do fator "
            "usado intensivamente nele e " + vd("reduz") + " a do outro fator — com efeito “ampliação” (o fator "
            "beneficiado ganha mais que proporcionalmente ao preço).",
            "Aplicação: no país B, uma tarifa sobre Y eleva o preço doméstico de Y → a produção de Y se expande e "
            "demanda relativamente mais capital → " + vd("r ↑, w ↓") + " em termos reais.",
            "Detalhe do enunciado: pelo " + azb("teorema de Heckscher-Ohlin") + ", B (abundante em capital) "
            "<b>exporta</b> Y e importa X. A proteção “à importação de Y” é, portanto, uma hipótese pouco "
            "natural, mas o raciocínio do teorema se aplica do mesmo jeito: o que conta é o bem cujo preço "
            "sobe.",
            "Corolário político: o fator <b>escasso</b> de um país (em B, o trabalho) ganha com protecionismo "
            "sobre o bem que o usa intensivamente (X); o fator abundante ganha com livre comércio. Por isso, "
            "em B, quem defenderia tarifas para elevar salários pediria proteção para X, não para Y.",
            vm("Regra-âncora: preço do bem sobe → ganha o fator intensivo nesse bem; o outro fator perde em "
               "termos reais."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item aplica corretamente o nome do teorema e o "
                       "instrumento (proteção eleva o preço de Y), mas troca o fator beneficiado. 🔥 O CACD gosta "
                       "de cenários com A/B e X/Y: monte a tabela fator abundante → bem exportado → fator "
                       "intensivo antes de julgar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política protecionista voltada à importação do bem X no país B tende a aumentar a "
            "remuneração da mão de obra no país B.”</i> → CERTO",
            "<i>“…uma política protecionista voltada à importação do bem Y no país B tende a aumentar a "
            "remuneração do capital e da mão de obra no país B.”</i> → ERRADO (o fator não intensivo perde)",
        ])],
        "reescrita": ("De acordo com o teorema de Samuelson-Stolper, uma política protecionista voltada à importação "
                      "do bem Y no país B tende a aumentar a remuneração " + hl("do capital") + " no país B"
                      + hl(" e a reduzir a da mão de obra") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": ("Dois comentários concordantes (um com citação de Paulo Gala sobre o teorema): proteger "
                             "Y eleva seu preço relativo e beneficia o capital, fator intensivo em Y; o trabalho "
                             "perde. Três imagens não preservadas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (198).png, image (203).png, image (201).png", "tipo_fonte": "não informado",
                           "lado": "verso", "acao": "irrecuperavel (imagens do verso não preservadas; conteúdo "
                                                   "refeito no 📖)"}],
        "alertas": ["quase_duplicata: ECO-E1-0674-1 (mesma prova e mesmo enunciado; H-O e salário no país A)"],
    },
    # ------------------------------------------------------------------ E1-0674
    {
        "id": "ECO-E1-0674-1", "fonte_ref": "E1-0674", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_TPS25,
        "excerto": EXC_TPS25,
        "rotulo_item": "Item",
        "assertiva": ("Um resultado da aplicação do modelo de Hecksher-Ohlin, atendidos todos os seus pressupostos, "
                      "é que o comércio exterior tende a aumentar a remuneração da mão de obra no país A."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um resultado da aplicação do modelo de Hecksher-Ohlin, atendidos todos os seus pressupostos, "
                      "é que o comércio exterior tende a <u>aumentar</u> a remuneração da mão de obra no país A."),
        "poucas": ("A é abundante em trabalho → exporta X, " + azb("intensivo em trabalho") + " → com o comércio, "
                   "o preço relativo de X sobe em A → pelo " + azb("Stolper-Samuelson") + ", o salário real sobe."),
        "destrinchando": [
            azb("Teorema de Heckscher-Ohlin") + " (" + oc("Eli Heckscher") + ", 1919; " + oc("Bertil Ohlin")
            + ", 1933): cada país exporta o bem intensivo no fator em que é " + azb("relativamente abundante")
            + ". Aqui: A exporta X (trabalho) e B exporta Y (capital).",
            "Abertura: em A, o preço relativo de X sobe (passa a ser vendido também para B); a produção se desloca "
            "para X, que demanda muito trabalho. Pelo " + azb("Stolper-Samuelson") + ": " + vd("w ↑, r ↓") + " "
            "em A; em B, o inverso (" + vd("r ↑, w ↓") + ").",
            "Pelo " + azb("teorema da equalização dos preços dos fatores") + " (" + oc("Samuelson") + "), com "
            "todos os pressupostos atendidos (mesma tecnologia, sem especialização completa, sem custos de "
            "transporte), o comércio de bens tende a igualar w e r entre os países: o salário sobe em A, onde era "
            "baixo, e cai em B.",
            "O “atendidos todos os seus pressupostos” protege o item: na vida real, diferenças tecnológicas, "
            "custos de comércio e fatores específicos (modelo de " + oc("Viner") + "-" + oc("Ricardo") + ") "
            "atenuam esses resultados.",
            vm("Regra-âncora: o comércio favorece o fator abundante de cada país e prejudica o escasso."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item direto, com duas proteções: “atendidos "
                       "todos os seus pressupostos” e “tende a”. O risco é inverter o fator beneficiado ou o país. "
                       "Note a grafia “Hecksher”, erro do próprio enunciado, que não muda o julgamento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o comércio exterior tende a aumentar a remuneração do capital no país A.”</i> → ERRADO (o capital "
            "é o fator escasso de A)",
            "<i>“…o comércio exterior tende a aumentar a remuneração da mão de obra no país B.”</i> → ERRADO (troca "
            "de país: em B o trabalho é escasso)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a", "atendidos todos os seus "
                                                                        "pressupostos"], "dificuldade": 1,
        "comentario_fonte": ("Dois comentários concordantes: A exporta X (intensivo em trabalho); pelo "
                             "Stolper-Samuelson o salário real sobe em A e o retorno do capital cai."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0673-1 (mesma prova e mesmo enunciado; Stolper-Samuelson com proteção "
                    "a Y no país B)"],
    },
    # ------------------------------------------------------------------ E1-0790
    {
        "id": "ECO-E1-0790-1", "fonte_ref": "E1-0790", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": True,
        "comando": CMD_BANDA,
        "excerto": EXC_BANDA,
        "rotulo_item": "Item",
        "assertiva": "Carlos tem vantagem comparativa em ser guitarrista.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Carlos tem vantagem <u>comparativa</u> em ser guitarrista."),
        "poucas": ("Carlos é melhor que João na bateria (vantagem absoluta), mas tirá-lo da guitarra custaria "
                   "muito à banda. Seu menor " + azb("custo de oportunidade") + " está na guitarra; o de João, na "
                   "bateria."),
        "destrinchando": [
            "O enunciado traz duas pistas: João “não é nem o melhor baterista da sua banda” e Carlos “poderia "
            "ser o baterista”. Logo, Carlos toca bateria melhor que João — " + azb("vantagem absoluta") + " de "
            "Carlos na bateria. E, sendo o guitarrista titular, presume-se que também o seja na guitarra.",
            azb("Vantagem comparativa") + " (" + oc("David Ricardo") + ") compara " + azb("custos de "
            "oportunidade") + ": quanto a banda perde, em ganho monetário, ao pôr cada um em cada função. Se "
            "Carlos vai para a bateria, a banda ganha um pouco na bateria e perde muito na guitarra; se João fica "
            "na bateria, a perda é só a pequena diferença de qualidade entre os dois bateristas.",
            "Exemplo numérico: Carlos gera 100 na guitarra e 60 na bateria; João, 20 na guitarra e 50 na bateria. "
            "Custo de oportunidade da bateria: Carlos " + vd("100/60 ≈ 1,7") + " de guitarra; João "
            + vd("20/50 = 0,4") + ". Carlos tem vantagem comparativa na guitarra; João, na bateria — mesmo sendo "
            "pior nas duas.",
            "É a lógica de Ricardo transposta de países para pessoas: o mais produtivo em tudo ainda ganha ao se "
            "especializar onde sua vantagem relativa é maior (o exemplo clássico de " + oc("Mankiw") + " é o do "
            "advogado que digita melhor que a secretária).",
            vm("Regra-âncora: vantagem absoluta = quem faz melhor; vantagem comparativa = quem sacrifica menos "
               "ao fazer."),
        ],
        "dissecando": (cz("[contraintuitivo]") + " O texto motivador sugere que Carlos é “melhor baterista”, e o "
                       "candidato apressado conclui que ele deveria tocar bateria. A banca cobra exatamente a "
                       "separação entre ser melhor (absoluta) e ter menor custo de oportunidade (comparativa)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Carlos tem vantagem comparativa em ser baterista, pois toca bateria melhor que João.”</i> → ERRADO "
            "(confunde absoluta com comparativa)",
            "<i>“Carlos tem vantagem absoluta em ser baterista.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Muitos comentários concordantes (professores e alunos): Carlos tem vantagem absoluta nos "
                             "dois instrumentos, mas comparativa na guitarra; exemplos numéricos de ganho do show; "
                             "lembrança do Foo Fighters (Dave Grohl, baterista que toca guitarra). Duas imagens "
                             "com fórmulas de custo de oportunidade não preservadas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (266).png, image (279).png", "tipo_fonte": "não informado", "lado": "verso",
                           "acao": "irrecuperavel (imagens do verso não preservadas; exemplo numérico refeito no "
                                   "📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0791
    {
        "id": "ECO-E1-0791-1", "fonte_ref": "E1-0791", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": CMD_BANDA,
        "excerto": EXC_BANDA,
        "rotulo_item": "Item",
        "assertiva": "João teria vantagem absoluta em ser guitarrista.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("João ") + vm("teria") + az(" vantagem absoluta em ser guitarrista."),
        "poucas": ("Nada indica que João toque guitarra melhor que Carlos — que é o guitarrista e ainda toca bateria "
                   "melhor que ele. " + azb("Vantagem absoluta") + " na guitarra, se alguém a tem, é de Carlos."),
        "destrinchando": [
            azb("Vantagem absoluta") + " (" + oc("Adam Smith") + ", <i>A Riqueza das Nações</i>, 1776): produzir "
            "mais com os mesmos recursos — aqui, gerar mais ganho no show na mesma função. Compara-se "
            "diretamente o desempenho de cada um.",
            "O que o texto permite inferir: Carlos é melhor baterista que João (João não é o melhor da banda, "
            "e Carlos poderia substituí-lo); Carlos é o guitarrista titular. Sobre João na guitarra, nada — e o "
            "mais razoável é supor que seja pior que o titular.",
            "Leitura do caso: Carlos tem vantagem absoluta nos dois instrumentos; João não tem vantagem absoluta "
            "em nenhum. Ainda assim, João tem " + azb("vantagem comparativa") + " na bateria, porque seu custo de "
            "oportunidade ali é o menor.",
            "Esse é o ponto de " + oc("Ricardo") + ": não ter vantagem absoluta em nada não impede alguém de "
            "contribuir — basta especializar-se onde sua desvantagem é menor.",
            vm("Regra-âncora: absoluta compara desempenho bruto; comparativa compara o que se sacrifica."),
        ],
        "dissecando": (cz("[troca de ator · extrapolação]") + " O item atribui a João uma vantagem que o "
                       "enunciado não sustenta e que, pela lógica do caso, pertence a Carlos. Truque típico: "
                       "trocar o personagem e o tipo de vantagem para ver se o candidato confunde os dois "
                       "conceitos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“João tem vantagem comparativa em ser baterista.”</i> → CERTO",
            "<i>“João teria vantagem absoluta em ser baterista.”</i> → ERRADO (Carlos toca bateria melhor)",
        ])],
        "reescrita": ("João " + hl("não teria") + " vantagem absoluta em ser guitarrista" + hl(": nada no "
                      "enunciado o indica, e Carlos, o guitarrista, é melhor que ele até na bateria") + "."),
        "tipo_erro": ["TROCA_ATOR", "EXTRAPOLACAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Muitos comentários concordantes: não há base para afirmar vantagem absoluta de João na "
                             "guitarra; Carlos teria vantagem absoluta nos dois instrumentos; exemplos numéricos de "
                             "ganho do show. Duas imagens com fórmulas não preservadas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (275).png, image (277).png", "tipo_fonte": "não informado", "lado": "verso",
                           "acao": "irrecuperavel (imagens do verso não preservadas; raciocínio refeito no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0792
    {
        "id": "ECO-E1-0792-1", "fonte_ref": "E1-0792", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": CMD_BANDA,
        "excerto": EXC_BANDA,
        "rotulo_item": "Item",
        "assertiva": ("O custo de oportunidade relativo de João ser baterista é menor que o custo de oportunidade "
                      "relativo de Carlos ser baterista."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O custo de oportunidade relativo de <u>João</u> ser baterista é <u>menor</u> que o custo de "
                      "oportunidade relativo de Carlos ser baterista."),
        "poucas": ("Pôr Carlos na bateria faz a banda " + azb("perder o guitarrista") + "; manter João na bateria "
                   "custa só a diferença de qualidade entre os dois bateristas. O custo de oportunidade de João "
                   "é menor — daí sua " + azb("vantagem comparativa") + " na bateria."),
        "destrinchando": [
            azb("Custo de oportunidade") + " = valor da melhor alternativa sacrificada. O de uma pessoa numa "
            "função é o que ela deixaria de gerar na outra função, medido em relação ao que gera nesta.",
            "Carlos: ao tocar bateria, sacrifica sua contribuição na guitarra, que é alta — custo de "
            "oportunidade " + vd("alto") + ". João: ao tocar bateria, sacrifica sua contribuição na guitarra, "
            "que é baixa ou nula — custo de oportunidade " + vd("baixo") + ".",
            "Ter o menor custo de oportunidade numa atividade é a <b>definição</b> de vantagem comparativa. Por "
            "isso o item é o espelho exato de “Carlos tem vantagem comparativa na guitarra”: com dois agentes e "
            "duas tarefas, se um tem vantagem comparativa numa, o outro necessariamente a tem na outra.",
            "Objeção comum (algumas respostas de cursinho): “não sabemos quanto João rende na guitarra”. A banca "
            "deu CERTO porque a lógica do caso (João é o baterista, sem destaque em nada) implica contribuição "
            "alternativa pequena.",
            vm("Regra-âncora: dois agentes, duas tarefas → cada um tem vantagem comparativa em uma; quem tem menor "
               "custo de oportunidade numa tem maior na outra."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Reescreve a definição de vantagem comparativa "
                       "com nomes trocados. O contraintuitivo é aceitar que o “pior” baterista tem o menor custo "
                       "de oportunidade na bateria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O custo de oportunidade relativo de Carlos ser baterista é menor que o de João, pois Carlos toca "
            "bateria melhor.”</i> → ERRADO (confunde desempenho com custo de oportunidade)",
            "<i>“O custo de oportunidade relativo de Carlos ser guitarrista é menor que o de João ser "
            "guitarrista.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Muitos comentários pelo CERTO (Carlos perderia a guitarra; João não abre mão de nada "
                             "relevante); um deles argumenta, sem base, que o item seria incorreto por falta de "
                             "informação sobre João na guitarra; citação do curso do Natale sobre custo de "
                             "oportunidade."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0793
    {
        "id": "ECO-E1-0793-1", "fonte_ref": "E1-0793", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": CMD_BANDA,
        "excerto": EXC_BANDA,
        "rotulo_item": "Item",
        "assertiva": ("O custo de oportunidade relativo de João ser guitarrista é menor que o custo de custo de "
                      "oportunidade relativo de Carlos ser guitarrista."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("O custo de oportunidade relativo de João ser guitarrista é menor que o ")
                    + vm("custo de custo de oportunidade") + az(" relativo de Carlos ser guitarrista.")),
        "poucas": ("Pelo conteúdo, seria " + vd("ERRADO") + " (Carlos tem o menor custo de oportunidade na "
                   "guitarra), mas o erro de redação “custo de custo de oportunidade” tornou o item ambíguo e a "
                   "banca o anulou."),
        "condicionais": [
            ("⚠️ Gabarito contestável",
             "Item anulado. O gabarito preliminar era ERRADO, coerente com o caso: na guitarra, o menor custo de "
             "oportunidade é o de Carlos, e o de João é maior (ele teria de deixar a bateria, sua única função "
             "útil, para render pouco na guitarra). A expressão duplicada impediu o julgamento objetivo."),
            ("🏛️ Justificativa da banca",
             cz("Deferido com anulação. O emprego da expressão “o custo do custo de oportunidade” prejudicou o "
                "julgamento objetivo do item.")),
        ],
        "destrinchando": [
            "Com dois agentes e duas tarefas, os custos de oportunidade são recíprocos: o custo de João na "
            "guitarra é o inverso do seu custo na bateria. Se João tem o menor custo de oportunidade na "
            + azb("bateria") + ", tem o maior na " + azb("guitarra") + ".",
            "Exemplo: Carlos gera 100 na guitarra e 60 na bateria; João, 20 e 50. Custo da guitarra: Carlos "
            + vd("60/100 = 0,6") + " de bateria; João " + vd("50/20 = 2,5") + ". Carlos tem vantagem comparativa "
            "na guitarra.",
            "Com o mesmo enunciado, a banca cobrou um conjunto coerente: Carlos tem vantagem comparativa na "
            "guitarra (CERTO); João não tem vantagem absoluta na guitarra (a afirmação de que teria é ERRADO); o "
            "custo de oportunidade de João na bateria é menor que o de Carlos (CERTO); e o deste item seria "
            "ERRADO.",
            "Lição para recurso: erro material que muda o objeto da comparação (aqui, “custo do custo”) é "
            "fundamento clássico de anulação no " + azb("CEBRASPE") + ", mesmo quando a intenção do examinador é "
            "clara.",
            vm("Regra-âncora: quem tem vantagem comparativa numa tarefa tem desvantagem comparativa na outra."),
        ],
        "dissecando": (cz("[outro: erro material de redação · inversão]") + " Pretendia-se testar a inversão do "
                       "item sobre a bateria (trocando “baterista” por “guitarrista”, o “menor” fica falso). O "
                       "erro de digitação gerou a anulação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O custo de oportunidade relativo de João ser guitarrista é maior que o custo de oportunidade "
            "relativo de Carlos ser guitarrista.”</i> → CERTO",
            "<i>“João tem vantagem comparativa em ser guitarrista.”</i> → ERRADO (troca de ator: é Carlos)",
        ])],
        "tipo_erro": ["OUTRO", "INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Anotação “ERRADO > ANULADA”, com o motivo oficial (expressão “o custo do custo de "
                             "oportunidade”) e dois comentários curtos: o custo de oportunidade de João na guitarra "
                             "é maior que o de Carlos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: assertiva mantida com o erro “custo de custo de oportunidade”, que é o motivo da "
                    "anulação"],
    },
    # ------------------------------------------------------------------ E1-0859
    {
        "id": "ECO-E1-0859-1", "fonte_ref": "E1-0859", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Maio/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("No que diz respeito à Teoria do Comércio Internacional, julgue certo ou errado (C ou E) o item "
                    "a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A teoria neoclássica do comércio internacional, conhecida como Teorema de Hecksher-Ohlin, "
                      "demonstra como a oferta relativa de fatores de produção e o emprego desses fatores em "
                      "diferentes intensidades na produção explicam os padrões de especialização e as "
                      "possibilidades do comércio internacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria neoclássica do comércio internacional, conhecida como Teorema de Hecksher-Ohlin, "
                      "demonstra como a <u>oferta relativa de fatores</u> de produção e o emprego desses fatores em "
                      "<u>diferentes intensidades</u> na produção explicam os padrões de especialização e as "
                      "possibilidades do comércio internacional."),
        "poucas": ("O H-O assenta-se em dois pilares: " + azb("dotação relativa de fatores") + " (abundância × "
                   "escassez) e " + azb("intensidade fatorial") + " dos bens. Da combinação sai o padrão de "
                   "comércio: exporta-se o bem intensivo no fator abundante."),
        "destrinchando": [
            "Modelo de " + oc("Heckscher") + " (1919) e " + oc("Ohlin") + " (1933), formalizado por "
            + oc("Samuelson") + ": 2 países, 2 bens, 2 fatores (trabalho e capital), mesma tecnologia nos dois "
            "países, fatores móveis entre setores e imóveis entre países, concorrência perfeita.",
            "Como a tecnologia é igual, a diferença de custos — e portanto a vantagem comparativa — vem das "
            + azb("dotações relativas") + ": no país abundante em capital, o capital é relativamente barato, e "
            "o bem intensivo em capital sai mais barato antes do comércio.",
            "Teoremas derivados: " + azb("Heckscher-Ohlin") + " (padrão de comércio), " + azb("Stolper-"
            "Samuelson") + " (preços dos bens → remuneração dos fatores), " + azb("Rybczynski") + " (aumento de "
            "um fator → expansão do setor que o usa intensivamente) e " + azb("equalização dos preços dos "
            "fatores") + ".",
            "Contraste com " + oc("Ricardo") + ": lá a vantagem comparativa nasce de diferenças de "
            "<b>produtividade</b> (tecnologia) com um só fator; no H-O, de diferenças de <b>dotação</b> com "
            "tecnologia igual.",
            "Teste empírico famoso: o " + azb("paradoxo de Leontief") + " (1953), que encontrou exportações "
            "americanas relativamente intensivas em trabalho, apesar da abundância de capital dos EUA.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, com os dois pilares certos. A banca costuma "
                       "errar o item trocando “dotação relativa” por “produtividade do trabalho” (que é Ricardo) "
                       "ou “abundante” por “escasso” no padrão de exportação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O teorema de Heckscher-Ohlin explica o comércio pelas diferenças de produtividade do trabalho "
            "entre os países.”</i> → ERRADO (troca de conceito: isso é Ricardo)",
            "<i>“Pelo modelo H-O, o país exporta o bem intensivo no fator relativamente escasso.”</i> → ERRADO "
            "(inversão)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentário curto e correto: H-O vincula vantagem comparativa à dotação relativa e à "
                             "intensidade fatorial; exporta-se o bem intensivo no fator abundante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: retirado o número do item (“Questão 214:”)",
                    "quase_duplicata: ECO-E1-0894-1 (mesma definição de H-O, outra fonte)"],
    },
    # ------------------------------------------------------------------ E1-0893
    {
        "id": "ECO-E1-0893-1", "fonte_ref": "E1-0893", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("David Ricardo aperfeiçoou as ideias de Adam Smith e desenvolveu a chamada Teoria das Vantagens "
                      "Comparativas. No livro Sobre os Princípios da Economia Política e da Tributação, Ricardo "
                      "defende que o comércio internacional é benéfico a todos os países que mantêm vínculos "
                      "comerciais entre si, pois o importante, segundo ele, são as vantagens comparativas, não as "
                      "absolutas, de todos os fatores de produção de uma economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("David Ricardo aperfeiçoou as ideias de Adam Smith e desenvolveu a chamada Teoria das "
                       "Vantagens Comparativas. No livro Sobre os Princípios da Economia Política e da Tributação, "
                       "Ricardo defende que o comércio internacional é benéfico a todos os países que mantêm "
                       "vínculos comerciais entre si, pois o importante, segundo ele, são as vantagens comparativas, "
                       "não as absolutas, ") + vm("de todos os fatores de produção de uma economia") + az(".")),
        "poucas": ("O modelo de " + oc("Ricardo") + " usa " + vm("um único fator, o trabalho") + ", e a vantagem "
                   "comparativa se refere a <b>bens</b> (custo de oportunidade de produzi-los), não a “todos os "
                   "fatores de produção”."),
        "destrinchando": [
            "Em " + oc("Ricardo") + " (<i>Princípios de Economia Política e Tributação</i>, 1817, cap. 7, o "
            "exemplo de vinho e tecido entre Portugal e Inglaterra), o custo de cada bem é medido em "
            + azb("horas de trabalho") + ": é a teoria do valor-trabalho aplicada ao comércio.",
            "A vantagem comparativa compara, dentro de cada país, o custo relativo de dois <b>bens</b>. Portugal "
            "produzia vinho e tecido com menos horas que a Inglaterra (vantagem absoluta em ambos), mas sua "
            "vantagem relativa era maior no vinho; a Inglaterra, menos ineficiente em tecido, especializou-se "
            "nele.",
            "Consequência lógica: nenhum país tem vantagem comparativa em <b>todos</b> os bens — com dois bens e "
            "dois países, a vantagem comparativa de um num bem implica a do outro no outro bem.",
            "Múltiplos fatores de produção entram só na teoria neoclássica (" + azb("Heckscher-Ohlin") + "), "
            "que explica a vantagem comparativa pelas dotações relativas de trabalho, capital e terra.",
            "O restante do item está correto: Ricardo refina a ideia de " + oc("Adam Smith") + " (vantagem "
            "absoluta) e conclui que o comércio pode beneficiar todos os parceiros.",
        ],
        "dissecando": (cz("[anacronismo · troca de conceito]") + " Quatro afirmações verdadeiras abrem caminho "
                       "para o erro no fim: “de todos os fatores de produção” enxerta em Ricardo um elemento "
                       "neoclássico (H-O). Itens longos e corretos no começo costumam esconder o erro no "
                       "complemento final."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, as vantagens comparativas decorrem das diferenças de produtividade do "
            "trabalho entre os países.”</i> → CERTO",
            "<i>“Para Ricardo, um país pode ter vantagem comparativa na produção de todos os bens.”</i> → ERRADO "
            "(impossível: a vantagem comparativa é relativa)",
        ])],
        "reescrita": ("[…] pois o importante, segundo ele, são as vantagens comparativas, não as absolutas, "
                      + hl("na produção dos bens, medidas pela produtividade do trabalho, único fator de produção "
                           "do modelo") + "."),
        "tipo_erro": ["ANACRONISMO", "TROCA_CONCEITO"], "moduladores": ["todos"], "dificuldade": 2,
        "comentario_fonte": ("Vários comentários (IDEG, Prof. Jetro Coutinho, alunos, trecho do Manual do Candidato "
                             "de Economia da FUNAG, 2016): Ricardo considera só o trabalho; vantagem comparativa é "
                             "entre produtos, não fatores; não há vantagem comparativa em todos os bens. Um "
                             "comentário afirma que Ricardo “rejeita” Smith e que o comércio seria benéfico mesmo a "
                             "quem não troca (impreciso)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: a fonte não traz órgão nem prova, só o ano (2016)"],
    },
    # ------------------------------------------------------------------ E1-0894
    {
        "id": "ECO-E1-0894-1", "fonte_ref": "E1-0894", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria neoclássica do comércio internacional, também conhecida como Teorema de "
                      "Hecksher-Ohlin, o comércio internacional resulta de dotações distintas dos fatores de "
                      "produção entre os países, e a vantagem comparativa é determinada pela escassez relativa "
                      "desses fatores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a teoria neoclássica do comércio internacional, também conhecida como Teorema de "
                      "Hecksher-Ohlin, o comércio internacional resulta de <u>dotações distintas</u> dos fatores de "
                      "produção entre os países, e a vantagem comparativa é determinada pela <u>escassez "
                      "relativa</u> desses fatores."),
        "poucas": ("No H-O, a vantagem comparativa vem das " + azb("dotações relativas") + ": cada fator é barato "
                   "onde é abundante e caro onde é " + azb("escasso") + ". Escassez e abundância relativas são "
                   "as duas faces do mesmo critério."),
        "destrinchando": [
            "Com tecnologias iguais entre países, o que diferencia os custos é o preço relativo dos fatores, "
            "determinado pela " + azb("escassez relativa") + ": se o capital é escasso (e o trabalho abundante), "
            "o salário relativo é baixo e os bens intensivos em trabalho saem baratos.",
            "Daí o padrão: o país " + vd("exporta") + " o bem intensivo no fator abundante e " + vd("importa")
            + " o bem intensivo no fator escasso. Dizer que a vantagem comparativa é determinada pela escassez "
            "relativa é dizer o mesmo pelo outro lado.",
            "A abundância relativa pode ser definida por quantidades (K/L do país maior que o do parceiro) ou por "
            "preços (r/w menor). As definições coincidem se a demanda for semelhante entre países.",
            "Erro comum (inclusive em comentários de cursinho): tratar o H-O como “mera formalização” de "
            + oc("Ricardo") + ". Os modelos explicam a vantagem comparativa por causas distintas — tecnologia em "
            "Ricardo, dotações no H-O — e só o H-O tem efeitos distributivos internos (Stolper-Samuelson).",
            vm("Regra-âncora: H-O = tecnologia igual + dotações diferentes → exporta-se o fator abundante "
               "“embutido” nos bens."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " O item usa “escassez relativa” onde o manual costuma "
                       "dizer “abundância relativa”, e isso assusta. Mas a dotação relativa é um só critério: o "
                       "que é abundante num país é escasso no outro. Erraria se dissesse que o país "
                       "<b>exporta</b> o bem intensivo no fator escasso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…e cada país exporta o bem intensivo no fator de produção relativamente escasso.”</i> → ERRADO "
            "(inversão)",
            "<i>“…o comércio resulta de diferenças tecnológicas entre os países.”</i> → ERRADO (troca de "
            "conceito: isso é Ricardo)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Comentário curto e equivocado: chama o H-O de “mera formalização da teoria ricardiana” "
                             "e diz que países que não usam vantagens comparativas têm piores resultados."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0859-1 (mesma definição de H-O, outra fonte)"],
    },
    # ------------------------------------------------------------------ E1-0895
    {
        "id": "ECO-E1-0895-1", "fonte_ref": "E1-0895", "destino": "73", "subtema": H2["ho"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("Segundo uma vertente da teoria neoclássica de comércio internacional, conhecida como Teorema "
                      "Heckscher-Ohlin-Samuelson, a eliminação das barreiras ao comércio entre dois países resulta "
                      "na convergência dos preços de seus fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo uma vertente da teoria neoclássica de comércio internacional, conhecida como Teorema "
                      "Heckscher-Ohlin-Samuelson, a eliminação das barreiras ao comércio entre dois países resulta "
                      "na <u>convergência</u> dos preços de seus fatores de produção."),
        "poucas": ("É o " + azb("teorema da equalização dos preços dos fatores") + " (" + oc("Samuelson")
                   + ", 1948–49): o comércio de <b>bens</b> iguala os preços dos bens e, com eles, salários e "
                   "rendas do capital — mesmo com os fatores imóveis entre países."),
        "destrinchando": [
            "Mecanismo: com o comércio, o país abundante em trabalho expande o setor intensivo em trabalho; a "
            "demanda por trabalho sobe e o salário relativo, antes baixo, aumenta. No país abundante em capital, "
            "ocorre o inverso. Os preços relativos dos fatores " + vd("convergem") + ".",
            "Ponto central: no H-O os fatores são " + azb("imóveis entre países") + ". O comércio de bens "
            "funciona como <b>substituto</b> da migração de fatores: exportar bens intensivos em trabalho é "
            "“exportar trabalho embutido”.",
            "Condições para a equalização plena: mesma tecnologia, sem especialização completa, sem custos de "
            "transporte e barreiras, concorrência perfeita, mesmo número de bens e fatores. Na prática, há "
            "convergência parcial, não igualdade.",
            "Correção da fonte: a convergência <b>não</b> decorre de capitais e trabalhadores migrarem em busca "
            "de melhores rendimentos — isso seria mobilidade de fatores, hipótese que o modelo exclui.",
            vm("Regra-âncora: no HOS, comércio de bens substitui a mobilidade de fatores e tende a igualar seus "
               "preços."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item de definição, com “convergência” "
                       "(mais seguro que “igualdade”). A pegadinha possível seria atribuir o resultado à "
                       "mobilidade internacional de fatores ou dizer que a equalização é sempre completa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo teorema HOS, a equalização dos preços dos fatores decorre da livre migração de trabalhadores "
            "e capitais entre os países.”</i> → ERRADO (nexo indevido: os fatores são imóveis no modelo)",
            "<i>“O livre comércio sempre iguala completamente os salários reais entre os países.”</i> → ERRADO "
            "(modulador absoluto)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentário que atribui a equalização à mobilidade internacional de capitais e "
                             "trabalhadores e discute políticas anti-imigração (mecanismo errado para o modelo)."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0897
    {
        "id": "ECO-E1-0897-1", "fonte_ref": "E1-0897", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de vantagens comparativas de David Ricardo somente é capaz de explicar ganhos de "
                      "comércio sob uma situação de especialização completa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo de vantagens comparativas de David Ricardo ") + vm("somente")
                    + az(" é capaz de explicar ganhos de comércio ") + vm("sob")
                    + az(" uma situação de especialização completa.")),
        "poucas": ("O modelo ricardiano admite ganhos de comércio " + azb("sem especialização completa de ambos")
                   + ": no caso do país grande, este segue produzindo os dois bens, e o parceiro pequeno, que se "
                   "especializa, colhe os ganhos."),
        "destrinchando": [
            "No Ricardo com custos constantes (FPP linear), o país que comercia a um preço diferente do de "
            "autarquia especializa-se por inteiro: a especialização completa é o resultado <b>típico</b>, mas "
            "não condição para explicar ganhos.",
            "Caso do " + azb("país grande") + " (" + oc("Krugman e Obstfeld") + "): se a demanda mundial pelo "
            "bem exceder o que o país pequeno consegue produzir, o preço internacional fica igual ao preço de "
            "autarquia do país grande. Ele continua produzindo os dois bens (" + vd("especialização "
            "incompleta") + ") e não ganha; o país pequeno se especializa e fica com " + vd("todo o ganho") + ".",
            "Com muitos bens (modelo de " + oc("Dornbusch, Fischer e Samuelson") + ", 1977), cada país produz "
            "uma <b>faixa</b> de bens definida pelos salários relativos — não um único bem.",
            "Com custos de oportunidade crescentes (FPP côncava), o caso usual é a " + azb("especialização "
            "parcial") + ", e os ganhos de comércio continuam existindo.",
            vm("Regra-âncora: ganho de comércio exige preço internacional diferente do preço de autarquia, não "
               "especialização completa de todos."),
        ],
        "dissecando": (cz("[restrição indevida]") + " O “somente” transforma o resultado mais comum do modelo "
                       "num requisito. 🔥 Itens com “somente”, “apenas” e “exclusivamente” sobre modelos "
                       "teóricos tendem a ERRADO quando o manual traz um caso-limite."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo ricardiano, um país grande pode não se especializar completamente e, nesse caso, não "
            "obtém ganhos de comércio.”</i> → CERTO",
            "<i>“No modelo ricardiano, os ganhos de comércio dependem de um país ter vantagem absoluta.”</i> → "
            "ERRADO (troca de conceito: basta a vantagem comparativa)",
        ])],
        "reescrita": ("O modelo de vantagens comparativas de David Ricardo " + hl("também") + " é capaz de explicar "
                      "ganhos de comércio " + hl("fora de") + " uma situação de especialização completa"
                      + hl(", como no caso do país grande") + "."),
        "tipo_erro": ["RESTRICAO"], "moduladores": ["somente"], "dificuldade": 3,
        "comentario_fonte": ("Comentário que fala em “mix de produtos” com características semelhantes "
                             "(commodities, microeletrônicos) para negar a solução de canto — argumento que não "
                             "corresponde ao modelo ricardiano."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0899
    {
        "id": "ECO-E1-0899-1", "fonte_ref": "E1-0899", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de comércio de David Ricardo descreve como é possível alcançar pontos acima e à "
                      "direita na fronteira de possibilidades de consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O modelo de comércio de David Ricardo descreve como é possível alcançar pontos <u>acima e à "
                      "direita</u> na <u>fronteira de possibilidades de consumo</u>."),
        "poucas": ("Com especialização e troca, o país passa a consumir sobre a " + azb("fronteira de "
                   "possibilidades de consumo") + " (a linha de troca), que fica " + azb("acima e à direita")
                   + " da sua FPP: mais dos dois bens do que conseguiria sozinho."),
        "destrinchando": [
            "Em autarquia, o país só consome o que produz: o consumo fica <b>sobre a FPP</b>, cuja inclinação "
            "é o custo de oportunidade doméstico.",
            "Com o comércio, ele se especializa no bem de vantagem comparativa (ponto P da FPP) e troca ao "
            + azb("preço relativo internacional") + ". A reta que sai de P com essa inclinação é a fronteira de "
            "possibilidades de consumo: como o preço mundial é melhor que o custo doméstico, ela fica "
            + vd("fora da FPP") + ".",
            "Resultado: pontos inalcançáveis em autarquia (C, à direita e acima de A) tornam-se possíveis — é o "
            + azb("ganho de comércio") + " de " + oc("Ricardo") + ", visto no gráfico. Quanto mais o preço "
            "mundial se afasta do custo doméstico, maior o ganho.",
            "Ressalva: o ganho é do país como um todo; no modelo de um só fator (trabalho), não há perdedores "
            "internos — conflitos distributivos aparecem nos modelos com mais fatores.",
        ],
        "grafico_verso": "ECO-E1-0899-1-V1",
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A redação é truncada (“pontos acima e à direita na "
                       "fronteira de possibilidades de consumo”), mas descreve o resultado gráfico clássico. "
                       "Seria ERRADO se dissesse que o comércio permite <b>produzir</b> além da FPP."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de Ricardo mostra que o comércio permite ao país produzir em pontos além da sua fronteira "
            "de possibilidades de produção.”</i> → ERRADO (troca de conceito: consome além; produz na FPP)",
            "<i>“No modelo de Ricardo, o comércio permite consumir combinações de bens inalcançáveis em "
            "autarquia.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Comentário curto: especializando-se, o país “vive além de suas possibilidades” "
                             "isoladas; o comércio melhora a vida de todos os envolvidos."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0900
    {
        "id": "ECO-E1-0900-1", "fonte_ref": "E1-0900", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("Na teoria clássica de comércio, as vantagens comparativas são explicadas por funções de "
                      "produção diferentes dos dois países."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na teoria clássica de comércio, as vantagens comparativas são explicadas por <u>funções de "
                      "produção diferentes</u> dos dois países."),
        "poucas": ("No modelo de " + oc("Ricardo") + ", a vantagem comparativa nasce de diferenças de "
                   + azb("tecnologia") + " (produtividade do trabalho), isto é, de funções de produção distintas "
                   "— e não de dotações de fatores, como no H-O."),
        "destrinchando": [
            "Teoria clássica (" + oc("Smith") + ", " + oc("Ricardo") + "): um só fator, o trabalho, com "
            + azb("coeficientes técnicos") + " (horas por unidade) diferentes entre países. Cada país tem sua "
            "própria função de produção para cada bem.",
            "Funções de produção diferentes → FPPs com " + vd("inclinações diferentes") + " → custos de "
            "oportunidade diferentes. O país em que o bem custa menos em termos do outro bem tem vantagem "
            "comparativa nele.",
            "Teoria neoclássica (" + azb("Heckscher-Ohlin") + "): o oposto — funções de produção " + vd("iguais")
            + " entre países, vantagem comparativa explicada pelas dotações relativas de fatores. É a "
            "distinção que as bancas mais cobram entre os dois modelos.",
            "Origem histórica das diferenças tecnológicas no modelo ricardiano: clima, solo, habilidades, "
            "técnica — no exemplo de Ricardo, Portugal fazia vinho com menos trabalho que a Inglaterra.",
        ],
        "grafico_verso": "ECO-E1-0900-1-V1",
        "dissecando": (cz("[literalidade]") + " Item de definição. O risco é confundir com o H-O e pensar que "
                       "“funções de produção iguais” é a hipótese clássica. Ricardo = tecnologia diferente; "
                       "H-O = tecnologia igual, dotação diferente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Heckscher-Ohlin, as vantagens comparativas são explicadas por funções de produção "
            "diferentes entre os países.”</i> → ERRADO (troca de conceito: no H-O as tecnologias são iguais)",
            "<i>“Na teoria clássica, as vantagens comparativas decorrem das diferentes dotações de capital dos "
            "países.”</i> → ERRADO (anacronismo: dotações são o critério neoclássico)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentário curto com exemplo de FPPs (país A com vantagem comparativa em soja, país B "
                             "em chips de computador) e uma figura não preservada."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "00044.jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E1-0900-1-V1, FPPs de A e B com valores ilustrativos)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0901
    {
        "id": "ECO-E1-0901-1", "fonte_ref": "E1-0901", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2013, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("As teorias clássicas do comércio internacional baseiam-se na produtividade relativa da mão de "
                      "obra, e a teoria neoclássica do comércio internacional, na diferença relativa de dotação dos "
                      "fatores de produção."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As teorias clássicas do comércio internacional baseiam-se na <u>produtividade relativa da "
                      "mão de obra</u>, e a teoria neoclássica do comércio internacional, na <u>diferença relativa "
                      "de dotação dos fatores</u> de produção."),
        "poucas": ("É a divisão de manual: clássicos (" + oc("Smith") + ", " + oc("Ricardo") + ") → "
                   + azb("produtividade do trabalho") + "; neoclássicos (" + oc("Heckscher") + ", "
                   + oc("Ohlin") + ", " + oc("Samuelson") + ") → " + azb("dotações relativas de fatores") + "."),
        "destrinchando": [
            "<b>Clássica</b>: valor-trabalho, um só fator. " + oc("Smith") + " (1776) compara produtividades "
            "absolutas; " + oc("Ricardo") + " (1817), relativas — daí “produtividade relativa da mão de obra”.",
            "<b>Neoclássica</b>: dois ou mais fatores, tecnologia igual entre países. A vantagem comparativa vem "
            "da " + azb("abundância relativa") + ": o país rico em capital exporta bens intensivos em capital.",
            "Diferenças de consequência: no Ricardo, o comércio beneficia o país como um todo, sem perdedores "
            "internos; no H-O, há " + azb("efeitos distributivos") + " (Stolper-Samuelson: ganha o fator "
            "abundante, perde o escasso).",
            "Correção da fonte: a teoria neoclássica <b>não</b> se estrutura em torno de Ricardo nem explica o "
            "comércio pela produtividade — esse é justamente o traço clássico que o H-O substitui pelas "
            "dotações.",
            vm("Regra-âncora: clássico = produtividade (tecnologia); neoclássico = dotação de fatores."),
        ],
        "dissecando": (cz("[literalidade]") + " Item-síntese que só exige associar cada escola ao seu critério. "
                       "A banca erra o item trocando os critérios entre as escolas ou falando em produtividade "
                       "“absoluta” para Ricardo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A teoria neoclássica do comércio baseia-se na produtividade relativa da mão de obra.”</i> → "
            "ERRADO (troca de conceito)",
            "<i>“Para Ricardo, o padrão de comércio é determinado pela produtividade absoluta do trabalho.”</i> → "
            "ERRADO (absoluta é Smith)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Comentário que diz que a teoria neoclássica “se estrutura em torno da análise de "
                             "David Ricardo” e mistura o critério de produtividade com o de dotação."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0905
    {
        "id": "ECO-E1-0905-1", "fonte_ref": "E1-0905", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o princípio das vantagens comparativas, a produção mundial total será maximizada "
                      "se cada bem for produzido pelo país capaz de fazê-lo com os menores custos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com o princípio das vantagens comparativas, a produção mundial total será "
                       "maximizada se cada bem for produzido pelo país capaz de fazê-lo com ")
                    + vm("os menores custos") + az(".")),
        "poucas": ("“Menores custos” (absolutos) é o critério de " + oc("Smith") + ". Pelo princípio de "
                   + oc("Ricardo") + ", cada bem deve ser produzido pelo país com o " + vm("menor custo de "
                   "oportunidade") + " — mesmo que outro país o faça com menos recursos."),
        "destrinchando": [
            "Exemplo: o país A produz 2 máquinas ou 5 t de alimento por dia; o B, 1 máquina ou 4 t. A tem menor "
            "custo absoluto nos dois bens. Se “cada bem fosse produzido por quem tem menor custo”, A faria tudo e "
            "B ficaria ocioso — a produção mundial não seria máxima.",
            "Custos de oportunidade: em A, 1 máquina = " + vd("2,5 t") + "; em B, " + vd("4 t") + ". A tem "
            "vantagem comparativa em máquinas; B, em alimentos (1 t custa 0,25 máquina em B contra 0,4 em A). "
            "Com essa especialização, a produção conjunta dos dois bens aumenta.",
            "O princípio ricardiano afirma, sim, que a especialização pela vantagem comparativa " + vd("eleva a "
            "produção mundial") + " (com os recursos dados) e permite que todos ganhem com a troca — o erro do "
            "item está só no critério.",
            vm("Regra-âncora: especialização eficiente segue o custo de oportunidade, não o custo absoluto."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item cita o “princípio das vantagens comparativas” e "
                       "entrega o critério das <b>absolutas</b>. Pista: “menores custos” sem “de "
                       "oportunidade” ou “relativos”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com o princípio das vantagens comparativas, a produção mundial total será maximizada se "
            "cada bem for produzido pelo país com o menor custo de oportunidade.”</i> → CERTO",
            "<i>“Segundo Ricardo, um país sem vantagem absoluta em nenhum bem não ganha com o comércio.”</i> → "
            "ERRADO (é justamente o caso que Ricardo resolve)",
        ])],
        "reescrita": ("De acordo com o princípio das vantagens comparativas, a produção mundial total será maximizada "
                      "se cada bem for produzido pelo país capaz de fazê-lo com " + hl("o menor custo de "
                      "oportunidade") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Comentário confuso: nega que o princípio trate da maximização da produção mundial e "
                             "fala em “custo absoluto + custo de oportunidade”; afinal admite que a especialização "
                             "aumenta a produção."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0908
    {
        "id": "ECO-E1-0908-1", "fonte_ref": "E1-0908", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("O modelo clássico de comércio internacional, formulado no começo do século XIX, não pode ser "
                      "aplicado ao comércio de serviços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo clássico de comércio internacional, formulado no começo do século XIX, ")
                    + vm("não pode") + az(" ser aplicado ao comércio de serviços.")),
        "poucas": ("A lógica do " + azb("custo de oportunidade") + " vale para qualquer coisa que se produza e se "
                   "troque, inclusive serviços transacionáveis (transporte, seguros, software, turismo). O limite "
                   "é a transacionabilidade, não o modelo."),
        "destrinchando": [
            "O modelo de " + oc("Ricardo") + " (1817) foi formulado com bens (vinho e tecido), mas seus "
            "pressupostos — produtividades diferentes, custo de oportunidade, troca — não dependem da natureza "
            "física do produto.",
            "Serviços transacionáveis: fretes e seguros (historicamente centrais no comércio britânico), "
            "serviços financeiros, turismo, consultoria, tecnologia da informação. A " + azb("Índia") + " em "
            "software e serviços de TI é o exemplo moderno de vantagem comparativa em serviços.",
            "Limite real: serviços que exigem presença física simultânea (cabeleireiro, construção civil) são "
            + azb("não transacionáveis") + " — não por falha do modelo, mas porque não entram no comércio "
            "internacional (ou só entram via movimento de pessoas).",
            "No sistema multilateral, os serviços passaram a ter regras próprias com o " + azb("GATS") + " "
            "(Acordo Geral sobre Comércio de Serviços), criado na Rodada Uruguai com a " + vd("OMC (1995)")
            + ".",
            vm("Regra-âncora: vantagem comparativa se aplica a todo produto transacionável, bem ou serviço."),
        ],
        "dissecando": (cz("[restrição indevida · anacronismo]") + " O item usa a data de formulação (“começo do "
                       "século XIX”) para sugerir que o modelo ficou preso aos bens da época. A teoria é "
                       "abstrata: vale para serviços transacionáveis."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo ricardiano pode explicar o comércio de serviços transacionáveis, como os de tecnologia "
            "da informação.”</i> → CERTO",
            "<i>“Todos os serviços podem ser objeto de comércio internacional.”</i> → ERRADO (modulador absoluto: "
            "há não transacionáveis)",
        ])],
        "reescrita": ("O modelo clássico de comércio internacional, formulado no começo do século XIX, "
                      + hl("também pode") + " ser aplicado ao comércio de serviços" + hl(" transacionáveis") + "."),
        "tipo_erro": ["RESTRICAO", "ANACRONISMO"], "moduladores": ["não pode"], "dificuldade": 1,
        "comentario_fonte": ("Comentário correto no essencial: o modelo se aplica a serviços como transporte, seguro "
                             "e educação; serviços com barreiras geográficas não são transacionáveis. Condiciona a "
                             "aplicação à “mobilidade de fatores”, o que não procede."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0914
    {
        "id": "ECO-E1-0914-1", "fonte_ref": "E1-0914", "destino": "73", "subtema": H2["vant"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_COM,
        "rotulo_item": "Item",
        "assertiva": ("O modelo de vantagens comparativas sustenta que todos os participantes do comércio "
                      "internacional apresentam ganhos equivalentes ao participar do comércio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O modelo de vantagens comparativas sustenta que todos os participantes do comércio "
                       "internacional apresentam ganhos ") + vm("equivalentes") + az(" ao participar do comércio.")),
        "poucas": ("O modelo garante que todos <b>podem</b> ganhar, mas não que ganhem o mesmo: a divisão dos "
                   "ganhos depende dos " + azb("termos de troca") + " — quem negocia a um preço mais distante do "
                   "seu custo de autarquia ganha mais."),
        "destrinchando": [
            "No modelo de " + oc("Ricardo") + ", há ganho mútuo se os termos de troca ficarem " + vd("entre os "
            "custos de oportunidade") + " dos dois países. Onde o preço se fixa dentro desse intervalo decide "
            "quem fica com a maior fatia.",
            "Caso extremo: o " + azb("país grande") + " que não se especializa por completo comercia ao próprio "
            "preço de autarquia e " + vd("não ganha nada") + "; o país pequeno fica com todo o ganho. Ganhos "
            "“equivalentes” seriam coincidência, não resultado do modelo.",
            "Dentro de cada país, a questão é outra: com um só fator (trabalho), o Ricardo não tem perdedores "
            "internos; já nos modelos com mais fatores (" + azb("Heckscher-Ohlin") + ", fatores específicos), o "
            "comércio cria ganhadores e perdedores, e os ganhos agregados permitem, em tese, compensar os "
            "perdedores.",
            "Ponte com a " + azb("CEPAL") + ": a discussão sobre a repartição dos ganhos dialoga com a crítica"
            + " de " + oc("Prebisch") + ", para quem a deterioração dos termos de troca deixava à periferia a "
            "menor parte dos ganhos.",
            vm("Regra-âncora: vantagem comparativa garante ganho possível para todos, não ganho igual."),
        ],
        "dissecando": (cz("[extrapolação · modulador absoluto]") + " “Todos ganham” é tese ricardiana; o "
                       "examinador acrescentou “equivalentes”, que o modelo não sustenta. Desconfie de adjetivos "
                       "de igualdade (iguais, equivalentes, proporcionais) colados a resultados de ganho mútuo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O modelo de vantagens comparativas sustenta que todos os participantes podem ganhar com o "
            "comércio, e a divisão dos ganhos depende dos termos de troca.”</i> → CERTO",
            "<i>“No modelo ricardiano, o país grande sempre se apropria da maior parte dos ganhos de "
            "comércio.”</i> → ERRADO (inversão: tende a ganhar menos)",
        ])],
        "reescrita": ("O modelo de vantagens comparativas sustenta que todos os participantes do comércio "
                      "internacional apresentam ganhos " + hl("— não necessariamente equivalentes, pois sua divisão "
                      "depende dos termos de troca —") + " ao participar do comércio."),
        "tipo_erro": ["EXTRAPOLACAO", "GENERALIZACAO"], "moduladores": ["todos", "equivalentes"], "dificuldade": 1,
        "comentario_fonte": ("Comentário longo de IA: o modelo não garante ganhos iguais; explora efeitos "
                             "distributivos entre fatores e setores dentro de cada país (próprios do H-O, não do "
                             "Ricardo de um fator) e não menciona os termos de troca."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: frente em forma de pergunta (“É correto afirmar que ‘…’?”) convertida na "
                    "assertiva entre aspas"],
    },
]
