"""Cards do lote de redação 12 — ECO, passada 03 (nota 70: modelo IS-LM-BP / Mundell-Fleming)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "bp": "📍 Curva BP e mobilidade de capital",
    "fixo": "🔒 Câmbio fixo",
    "flut": "🌊 Câmbio flutuante",
}

CMD_NAB_MA = "Em relação à macroeconomia aberta, julgue o item a seguir."

CMD_NAB_AGREG = ("Considerando a teoria macroeconômica e os principais agregados macroeconômicos, julgue o item a "
                 "seguir.")

CMD_NAB_COM = "Sobre teorias do comércio e macroeconomia aberta, julgue o item a seguir."

CMD_NAB_CONC = "A respeito dos conceitos de macroeconomia aberta, julgue o item a seguir."

CMD_NAB_ISLMBP = "Com base no modelo IS-LM-BP, julgue o item a seguir."

CMD_RT_A = "Julgue o item a seguir, acerca dos modelos IS-LM e IS-LM-BP."

CMD_RT_PAND = ("Durante a pandemia, o Banco Central conduziu as taxas de juros frente às mudanças da conjuntura da "
               "inflação, da atividade e da taxa de câmbio. Avalie a proposição a seguir como verdadeira ou falsa.")

CMD_RT_B = ("O modelo IS-LM-BP permite analisar os efeitos de políticas econômicas numa economia aberta. Sobre este "
            "tema, julgue o item a seguir.")

CMD_RT_C = ("Sobre a teoria da política econômica numa economia aberta (modelo Mundell-Fleming), o modelo de oferta "
            "e demanda agregadas e a curva de Phillips, julgue o item a seguir.")

CMD_RT_D = ("Desde o início da pandemia, houve uso intenso de políticas econômicas visando a recuperação da "
            "atividade em diversas economias. Sobre as políticas econômicas em pequenas economias abertas e "
            "mobilidade imperfeita de capitais, julgue o item a seguir.")

REGRA_MF = vm("Regra-âncora (mobilidade perfeita): câmbio fixo → fiscal eficaz, monetária ineficaz; câmbio "
              "flutuante → monetária eficaz, fiscal ineficaz.")


def corte(ref, desc):
    return {"ref": ref, "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": f"cortada ({desc}; absorvida no 📖)"}


def redes(ref, fid, desc):
    return {"ref": ref, "tipo_fonte": "GRÁFICO", "lado": "verso", "acao": f"redesenhada em {fid} ({desc})"}


CARDS = [
    # ------------------------------------------------------------------ E2-L00903
    {
        "id": "ECO-E2-L00903-1", "fonte_ref": "E2-L00903", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_MA,
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo IS-LM-BP, numa economia com mobilidade perfeita de capital e câmbio "
                      "fixo, se o governo expande os gastos públicos, a renda aumenta, com juros subindo acima dos "
                      "juros externos, gerando entrada de capitais, expandindo o estoque monetário e, assim, "
                      "elevando mais ainda a renda de equilíbrio."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando o modelo IS-LM-BP, numa economia com mobilidade perfeita de capital e câmbio "
                      "fixo, se o governo expande os gastos públicos, a renda aumenta, com juros subindo <u>acima "
                      "dos juros externos</u>, gerando <u>entrada de capitais</u>, <u>expandindo o estoque "
                      "monetário</u> e, assim, elevando <u>mais ainda</u> a renda de equilíbrio."),
        "poucas": ("É a sequência canônica do Mundell-Fleming: G ↑ → i &gt; i* → entrada de capitais → o Banco "
                   "Central compra divisas para segurar o câmbio → " + azb("a moeda se expande sozinha") + " → a LM "
                   "vai para a direita e a renda sobe ainda mais. No câmbio fixo, a política fiscal tem "
                   + vd("eficácia máxima") + "."),
        "destrinchando": [
            "Com " + azb("mobilidade perfeita de capital") + ", a curva " + azb("BP") + " é horizontal em "
            + vd("i = i*") + ": qualquer juro doméstico acima do externo atrai capital sem limite; abaixo dele, "
            "expulsa capital sem limite. O equilíbrio de longo prazo precisa estar sobre essa reta.",
            "Passo 1 — a expansão de G desloca a IS para a direita: renda e juros sobem (ponto E′, acima da BP). "
            "Passo 2 — com i &gt; i*, entra capital e o mercado de câmbio pressiona pela " + azb("apreciação")
            + ". Passo 3 — para manter a paridade, o Banco Central " + vd("compra moeda estrangeira")
            + " emitindo moeda doméstica: reservas e base monetária crescem, e a LM se desloca para a direita.",
            "Passo 4 — o ajuste para quando o juro volta a i*. No equilíbrio final (E″), a renda subiu mais do que "
            "subiria numa economia fechada, porque " + azb("não há crowding-out") + ": o juro não fica mais "
            "alto e o câmbio não se aprecia.",
            "Por isso se diz que, no câmbio fixo, a " + azb("oferta de moeda é endógena") + ": quem a determina "
            "é o balanço de pagamentos, não o Banco Central. A política monetária vira refém da paridade.",
            REGRA_MF,
        ],
        "grafico_verso": "ECO-E2-L00903-1-V1",
        "dissecando": (cz("[literalidade · detalhe]") + " O item narra o mecanismo passo a passo, e a única dúvida "
                       "plausível é o “juros subindo acima dos juros externos”: isso vale para o "
                       "<b>momento intermediário</b> (E′), não para o equilíbrio final. Como o item descreve o "
                       "processo, ele está certo. 🔥 A banca alterna esta versão (processo) com a versão sobre o "
                       "equilíbrio final, em que “juros maiores” é ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a renda aumenta e a taxa de juros de equilíbrio final permanece acima da taxa externa…”</i> → "
            "ERRADO (no equilíbrio final, i = i*)",
            "<i>“…gerando entrada de capitais, que obriga o Banco Central a vender reservas, contraindo o estoque "
            "monetário…”</i> → ERRADO (inversão: o Banco Central compra divisas e a moeda se expande)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["mais ainda"], "dificuldade": 1,
        "comentario_fonte": "Verso só com a descrição de um gráfico IS-LM-BP (BP horizontal; IS para a direita, "
                            "E → E′; compra de divisas, LM para a direita, E″) e a conclusão: política fiscal eficaz "
                            "com câmbio fixo.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [redes("IMAGEM 148", "ECO-E2-L00903-1-V1", "expansão fiscal com câmbio fixo")],
        "alertas": ["quase_duplicata: ECO-E2-L00904-1, ECO-E2-L01241-1 (mesmo mecanismo: expansão fiscal no câmbio "
                    "fixo com mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L00904
    {
        "id": "ECO-E2-L00904-1", "fonte_ref": "E2-L00904", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_MA,
        "rotulo_item": "Item",
        "assertiva": ("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                      "câmbio fixo, a partir do equilíbrio dos mercados, uma política fiscal expansionista gera "
                      "aumento da renda real e da taxa de juros de equilíbrio."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                       "câmbio fixo, a partir do equilíbrio dos mercados, uma política fiscal expansionista gera "
                       "aumento da renda real") + vm(" e da") + az(" taxa de juros de equilíbrio.")),
        "poucas": ("A renda de equilíbrio sobe, mas os juros " + vm("voltam a i*") + ": com mobilidade perfeita, "
                   "o equilíbrio final está sempre sobre a BP horizontal. O aumento dos juros é só "
                   "intermediário."),
        "destrinchando": [
            "Com perfeita mobilidade, a " + azb("paridade descoberta de juros") + " (sem risco nem expectativa de "
            "desvalorização) impõe " + vd("i = i*") + " no equilíbrio: é isso que a BP horizontal representa. "
            "Qualquer desvio é eliminado pelo fluxo de capitais.",
            "A expansão fiscal desloca a IS para a direita e, num primeiro momento, eleva Y e i (ponto acima da "
            "BP). A entrada de capitais pressiona o câmbio para baixo; o Banco Central compra divisas, a base "
            "monetária cresce e a LM se desloca para a direita até que o juro volte a i*.",
            "Resultado final: " + vd("Y ↑↑") + ", " + vd("i = i*") + " (inalterado), " + vd("reservas ↑")
            + " e oferta monetária ↑. O efeito sobre a renda é o do " + azb("multiplicador keynesiano "
            "simples") + " (como se a LM fosse horizontal), sem crowding-out.",
            "Contraste com a economia fechada: lá, a mesma expansão fiscal eleva Y <b>e</b> i, e o juro maior "
            "expulsa parte do investimento. Aqui, quem “acomoda” a política fiscal é a expansão monetária "
            "induzida pela defesa do câmbio.",
            REGRA_MF,
        ],
        "dissecando": (cz("[meia-verdade]") + " A primeira metade (renda maior) é verdadeira; o erro "
                       "foi enxertado nos juros, que só sobem no <b>meio do ajuste</b>. A pista está em “de "
                       "equilíbrio”: o item pede o resultado final, e com mobilidade perfeita o juro final é "
                       "sempre o externo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…gera aumento da renda real e de reservas internacionais, mantendo a taxa de juros de equilíbrio "
            "igual à externa.”</i> → CERTO",
            "<i>“…com câmbio flutuante, a política fiscal expansionista gera aumento da renda real.”</i> → ERRADO "
            "(troca de regime: no flutuante, a renda não muda)",
        ])],
        "reescrita": ("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                      "câmbio fixo, a partir do equilíbrio dos mercados, uma política fiscal expansionista gera "
                      "aumento da renda real" + hl(", mas mantém inalterada a") + " taxa de juros de equilíbrio"
                      + hl(", igual à externa") + "."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "No equilíbrio final, a renda aumenta, porém a taxa de juros retorna ao nível inicial, "
                            "igual à taxa de juros mundial (com descrição do gráfico E → E′ → E″).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 149", "expansão fiscal com câmbio fixo")],
        "alertas": ["quase_duplicata: ECO-E2-L00903-1, ECO-E2-L01241-1"],
    },
    # ------------------------------------------------------------------ E2-L00905
    {
        "id": "ECO-E2-L00905-1", "fonte_ref": "E2-L00905", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_MA,
        "rotulo_item": "Item",
        "assertiva": ("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                      "câmbio fixo, a partir do equilíbrio dos mercados, uma política monetária contracionista e "
                      "uma expansionista não impactam o nível de equilíbrio da renda real da economia e nem o "
                      "montante de reservas do BACEN."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                       "câmbio fixo, a partir do equilíbrio dos mercados, uma política monetária contracionista e "
                       "uma expansionista não impactam o nível de equilíbrio da renda real da economia")
                    + vm(" e nem") + az(" o montante de reservas do BACEN.")),
        "poucas": ("A renda de equilíbrio de fato não muda, mas " + vm("as reservas mudam") + ": é justamente a "
                   "compra ou venda de divisas pelo Banco Central que desfaz a política monetária."),
        "destrinchando": [
            "Expansão monetária: a LM vai para a direita, o juro cai abaixo de i* e o capital sai. Para impedir a "
            "desvalorização, o Banco Central " + vd("vende reservas") + " e recolhe moeda doméstica; a base "
            "monetária encolhe e a LM volta ao ponto de partida. Saldo: " + vd("Y igual, reservas ↓") + ".",
            "Contração monetária: a LM vai para a esquerda, o juro sobe acima de i* e o capital entra. Para "
            "impedir a apreciação, o Banco Central " + vd("compra divisas") + " emitindo moeda; a LM volta. "
            "Saldo: " + vd("Y igual, reservas ↑") + ".",
            "Na prática, o que muda é a <b>composição</b> da base monetária: o Banco Central troca crédito "
            "doméstico (títulos) por ativos externos (reservas), ou vice-versa. A quantidade total de moeda é "
            "ditada pela necessidade de manter i = i* e o câmbio na paridade.",
            "É a " + azb("trindade impossível") + " em ação: com câmbio fixo e livre mobilidade de capitais, "
            "abre-se mão da autonomia monetária. Uma expansão grande demais esgota as reservas e termina em "
            "crise cambial.",
            REGRA_MF,
        ],
        "grafico_verso": "ECO-E2-L00905-1-V1",
        "dissecando": (cz("[meia-verdade]") + " A primeira parte (renda inalterada nos dois casos) é o resultado "
                       "clássico e induz a marcar CERTO; o erro foi acrescentado no “e nem o montante de "
                       "reservas”. Pista: a ineficácia só acontece <b>porque</b> o Banco Central intervém no "
                       "câmbio — e intervir é mexer nas reservas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política monetária expansionista não altera a renda de equilíbrio, mas reduz as reservas "
            "internacionais.”</i> → CERTO",
            "<i>“…uma política monetária contracionista reduz a renda de equilíbrio e eleva as reservas.”</i> → "
            "ERRADO (a renda não muda)",
        ])],
        "reescrita": ("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                      "câmbio fixo, a partir do equilíbrio dos mercados, uma política monetária contracionista e "
                      "uma expansionista não impactam o nível de equilíbrio da renda real da economia"
                      + hl(", mas alteram") + " o montante de reservas do BACEN."),
        "tipo_erro": ["MEIA_VERDADE"], "moduladores": ["nem"], "dificuldade": 1,
        "comentario_fonte": "Política monetária ineficaz no câmbio fixo com mobilidade perfeita: não altera a renda, "
                            "mas altera as reservas (venda de reservas na expansão, compra na contração).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [redes("IMAGEM 150", "ECO-E2-L00905-1-V1", "expansão monetária com câmbio fixo")],
        "alertas": ["quase_duplicata: ECO-E2-L01630-1, ECO-E2-L01486-1 (política monetária ineficaz no câmbio fixo "
                    "com mobilidade alta)"],
    },
    # ------------------------------------------------------------------ E2-L00906
    {
        "id": "ECO-E2-L00906-1", "fonte_ref": "E2-L00906", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_MA,
        "rotulo_item": "Item",
        "assertiva": ("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                      "câmbio flutuante, a partir do equilíbrio dos mercados, uma política fiscal expansionista tem "
                      "impacto nulo na renda real de equilíbrio e gera valorização da moeda nacional, reduzindo o "
                      "saldo da balança comercial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em relação ao modelo IS-LM-BP, em um país com perfeita mobilidade de capitais e regime de "
                      "câmbio flutuante, a partir do equilíbrio dos mercados, uma política fiscal expansionista tem "
                      "<u>impacto nulo</u> na renda real de equilíbrio e gera <u>valorização</u> da moeda nacional, "
                      "reduzindo o saldo da balança comercial."),
        "poucas": ("No flutuante com mobilidade perfeita, a expansão fiscal atrai capital, " + azb("aprecia o "
                   "câmbio") + " e derruba as exportações líquidas até a IS voltar ao lugar: " + vd("ΔY = 0")
                   + ", e o gasto público apenas substitui exportações líquidas."),
        "destrinchando": [
            "G ↑ desloca a IS para a direita: no primeiro momento, Y e i sobem. Com i &gt; i*, entra capital; "
            "como o câmbio flutua, a moeda nacional se " + azb("valoriza") + ".",
            "A apreciação encarece as exportações e barateia as importações: " + vd("NX ↓") + ", e a IS volta "
            "para a esquerda. O processo só termina quando o juro retorna a i*. Como a LM não se moveu, a única "
            "renda compatível com i = i* sobre a LM original é a renda inicial.",
            "Esse é o " + azb("crowding-out externo completo") + " (ou via câmbio): ΔG é compensado exatamente "
            "por ΔNX negativo. Em economia fechada, o crowding-out se dá via juros e atinge o investimento; aqui, "
            "via câmbio, atinge o setor externo.",
            "Leitura histórica: é o mecanismo dos “" + azb("déficits gêmeos") + "” dos EUA nos anos 1980 — "
            "expansão fiscal, juros altos, dólar forte e déficit comercial crescente.",
            REGRA_MF,
        ],
        "grafico_verso": "ECO-E2-L00906-1-V1",
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O item reúne as três consequências do caso — "
                       "renda inalterada, apreciação, piora comercial — e todas estão certas. A armadilha é a "
                       "intuição keynesiana de que gasto público sempre eleva a renda. 🔥 A banca costuma trocar "
                       "“valorização” por “desvalorização” ou o regime cambial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…tem impacto nulo na renda real de equilíbrio e gera desvalorização da moeda nacional…”</i> → "
            "ERRADO (inversão: entra capital e a moeda se valoriza)",
            "<i>“…em regime de câmbio fixo, a política fiscal expansionista tem impacto nulo na renda.”</i> → "
            "ERRADO (troca de regime: no fixo, a fiscal tem eficácia máxima)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "IS para a direita, juros sobem, entrada de capitais, apreciação, NX caem, IS volta: "
                            "impacto nulo na renda; política fiscal ineficaz no câmbio flutuante com mobilidade "
                            "perfeita.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [redes("IMAGEM 151", "ECO-E2-L00906-1-V1", "expansão fiscal com câmbio flexível")],
        "alertas": ["quase_duplicata: ECO-E2-L01024-1, ECO-E2-L01513-1 (política fiscal ineficaz no flutuante com "
                    "mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L00978
    {
        "id": "ECO-E2-L00978-1", "fonte_ref": "E2-L00978", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_AGREG,
        "rotulo_item": "Item",
        "assertiva": ("Considere uma economia grande com mobilidade imperfeita de capital e sob regime de câmbio "
                      "fixo. No caso de uma política monetária expansionista, geram-se nível de renda constante e "
                      "taxa de juros constante. No caso de uma política fiscal expansionista, geram-se nível de "
                      "renda maior e taxa de juros maior."),
        "gabarito": "CERTO", "gabarito_origem": "resolvido", "status": "normal",
        "anotada": az("Considere uma economia grande com mobilidade imperfeita de capital e sob regime de câmbio "
                      "fixo. No caso de uma política monetária expansionista, geram-se nível de renda "
                      "<u>constante</u> e taxa de juros <u>constante</u>. No caso de uma política fiscal "
                      "expansionista, geram-se nível de renda <u>maior</u> e taxa de juros <u>maior</u>."),
        "poucas": ("Com " + azb("BP positivamente inclinada") + " (mobilidade imperfeita) e câmbio fixo, a "
                   "monetária é desfeita pela perda de reservas (Y e i voltam ao início), e a fiscal termina com "
                   + vd("Y ↑ e i ↑") + ", num ponto mais alto da BP."),
        "destrinchando": [
            "Com " + azb("mobilidade imperfeita") + ", a BP é crescente: renda maior piora a balança comercial "
            "(mais importações), e só um juro maior atrai o capital que fecha o balanço. O equilíbrio externo "
            "admite, portanto, combinações diferentes de Y e i — e não apenas i = i*.",
            "Política monetária: a LM vai para a direita, o juro cai, a renda sobe — os dois efeitos pioram o "
            "balanço de pagamentos. O Banco Central vende reservas, a base monetária encolhe e a LM volta. "
            "Como a IS e a BP não se moveram, o único equilíbrio possível é o inicial: " + vd("Y e i "
            "constantes") + ", com reservas menores.",
            "Política fiscal: a IS vai para a direita. O ajuste da LM (para a direita se surgir superávit, para "
            "a esquerda se surgir déficit) termina na interseção da nova IS com a BP original, que fica mais "
            "acima e mais à direita. Resultado: " + vd("Y ↑ e i ↑") + " em qualquer caso. O tamanho do ganho "
            "depende de a BP ser mais ou menos inclinada que a LM.",
            "Regra geral: sob câmbio fixo, a " + azb("política monetária é ineficaz") + " em qualquer grau de "
            "mobilidade (salvo controle total e esterilização duradoura), e a fiscal é eficaz, mais ainda quanto "
            "maior a mobilidade.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item é a tabela de resultados da mobilidade imperfeita "
                       "no câmbio fixo. O “economia grande” é ruído: o raciocínio usa a BP crescente, sem que o "
                       "país altere o juro externo. A diferença para a mobilidade perfeita está no juro final da "
                       "fiscal: aqui, <b>maior</b>; lá, igual a i*."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com mobilidade perfeita, a política fiscal expansionista gera renda maior e taxa de juros "
            "maior.”</i> → ERRADO (com BP horizontal, o juro final é i*)",
            "<i>“…a política monetária expansionista gera renda constante e reservas internacionais "
            "constantes.”</i> → ERRADO (as reservas caem)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Verso só com uma imagem-resumo (quadro de eficácia das políticas monetária e fiscal "
                            "sob câmbio fixo e flutuante, com e sem mobilidade perfeita); sem gabarito explícito.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [{"ref": "IMAGEM 163", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quadro-resumo de eficácia; conteúdo no 📖)"}],
        "alertas": ["nota_redacao: gabarito resolvido (fonte sem gabarito); a menção a “economia grande” não altera "
                    "o resultado no modelo IS-LM-BP padrão"],
    },
    # ------------------------------------------------------------------ E2-L01024
    {
        "id": "ECO-E2-L01024-1", "fonte_ref": "E2-L01024", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_COM,
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo Mundell-Fleming, se o governo opera com câmbio flexível e plena "
                      "mobilidade de capitais, uma expansão fiscal não produz impacto positivo no produto e gera "
                      "como resultado a queda das exportações líquidas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando o modelo Mundell-Fleming, se o governo opera com câmbio flexível e plena "
                      "mobilidade de capitais, uma expansão fiscal <u>não produz impacto positivo</u> no produto e "
                      "gera como resultado a <u>queda das exportações líquidas</u>."),
        "poucas": ("Câmbio flexível + mobilidade plena: a expansão fiscal atrai capital, aprecia a moeda e reduz "
                   "as exportações líquidas na mesma medida do gasto extra. " + vd("Y não muda") + "; muda a "
                   + azb("composição da demanda") + " (mais G, menos NX)."),
        "destrinchando": [
            "Mecanismo: G ↑ → IS para a direita → i tende a subir acima de i* → entrada de capitais → "
            + vd("apreciação cambial") + " → exportações caem e importações sobem → IS volta à posição "
            "inicial.",
            "Por que a renda volta exatamente ao ponto de partida? Porque a LM não se moveu e o juro de "
            "equilíbrio precisa ser i*: só existe uma renda sobre a LM original com i = i* — a inicial. "
            "Se a renda não muda, e G subiu, alguma outra parcela da demanda caiu na mesma medida: "
            + vd("ΔNX = −ΔG") + ".",
            "É o " + azb("crowding-out completo via câmbio") + ". Na economia fechada, o crowding-out vem do "
            "juro e costuma ser parcial; aqui, o juro fica preso em i* e quem cede é o setor exportador.",
            "Política alternativa no mesmo cenário: a monetária, que deprecia o câmbio e eleva NX e Y. Daí a "
            "recomendação de usar a monetária para estabilizar a renda quando o câmbio flutua.",
            REGRA_MF,
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Reproduz o resultado do manual com duas partes "
                       "certas. O “não produz impacto positivo” assusta quem raciocina com o multiplicador da "
                       "economia fechada. 🔥 Versões erradas trocam o regime (fixo) ou dizem que as exportações "
                       "líquidas <b>sobem</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma expansão fiscal não produz impacto no produto e eleva as exportações líquidas.”</i> → "
            "ERRADO (inversão: a apreciação reduz NX)",
            "<i>“…se o governo opera com câmbio fixo e plena mobilidade de capitais, uma expansão fiscal não "
            "produz impacto positivo no produto.”</i> → ERRADO (troca de regime)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Política fiscal ineficaz com câmbio flexível e plena mobilidade: IS para a direita, "
                            "juros sobem, entra capital, moeda aprecia, NX caem, IS volta; produto igual, composição "
                            "diferente.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00906-1, ECO-E2-L01513-1"],
    },
    # ------------------------------------------------------------------ E2-L01025
    {
        "id": "ECO-E2-L01025-1", "fonte_ref": "E2-L01025", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_COM,
        "rotulo_item": "Item",
        "assertiva": ("Considerando o modelo de Mundell-Fleming, em uma pequena economia aberta com perfeita "
                      "mobilidade de capitais e regime de câmbio flutuante, a adoção de uma política monetária "
                      "contracionista resultaria no aumento do volume de exportações líquidas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Considerando o modelo de Mundell-Fleming, em uma pequena economia aberta com perfeita "
                       "mobilidade de capitais e regime de câmbio flutuante, a adoção de uma política monetária "
                       "contracionista resultaria ") + vm("no aumento") + az(" do volume de exportações "
                                                                             "líquidas.")),
        "poucas": ("A contração monetária eleva o juro, atrai capital e " + azb("aprecia a moeda") + ": as "
                   "exportações líquidas " + vm("caem") + ", e a renda cai junto."),
        "destrinchando": [
            "Sequência: M ↓ → LM para a esquerda → i sobe acima de i* → entrada de capitais → "
            + vd("apreciação") + " → exportações mais caras, importações mais baratas → " + vd("NX ↓")
            + " → IS para a esquerda.",
            "Equilíbrio final: juro de volta a i*, renda " + vd("menor") + " (é a nova LM que define a renda "
            "compatível com i*), câmbio mais apreciado e saldo comercial pior. A política monetária é "
            + azb("eficaz") + " — para contrair, neste caso.",
            "O canal cambial é o que torna a monetária tão potente no câmbio flutuante: em vez de agir só pelo "
            "investimento (economia fechada), ela age também pelo setor externo, e os dois efeitos vão na mesma "
            "direção.",
            "Exemplo brasileiro ⏳ (out/2026): ciclos de alta forte da Selic costumam vir acompanhados de "
            "entrada de capitais de curto prazo (operações de " + azb("carry trade") + ") e apreciação do real, "
            "um dos canais pelos quais o aperto monetário reduz a inflação.",
            vm("Regra-âncora: no flutuante, juro sobe → câmbio aprecia → NX cai; juro cai → câmbio deprecia → NX "
               "sobe."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o efeito final sobre o setor externo. Quem pensa só na "
                       "renda (contração → menos importações → saldo melhor) cai na pegadinha; o canal "
                       "dominante no Mundell-Fleming é o <b>câmbio</b>, que se aprecia."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a adoção de uma política monetária contracionista resultaria em apreciação cambial e queda do "
            "produto.”</i> → CERTO",
            "<i>“…com câmbio fixo, a política monetária contracionista reduziria o produto.”</i> → ERRADO (no "
            "fixo, a monetária é ineficaz)",
        ])],
        "reescrita": ("Considerando o modelo de Mundell-Fleming, em uma pequena economia aberta com perfeita "
                      "mobilidade de capitais e regime de câmbio flutuante, a adoção de uma política monetária "
                      "contracionista resultaria " + hl("na redução") + " do volume de exportações líquidas."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Contração monetária eleva os juros, atrai capital, superávit no BP; a moeda aprecia e "
                            "as exportações líquidas caem.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01242-1 (contração monetária no flutuante: apreciação e queda do "
                    "produto)"],
    },
    # ------------------------------------------------------------------ E2-L01046
    {
        "id": "ECO-E2-L01046-1", "fonte_ref": "E2-L01046", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_MA,
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de câmbio flutuante com perfeita mobilidade de capital, o aumento das tarifas de "
                      "importação leva a um novo equilíbrio com maiores níveis de exportações líquidas e da renda "
                      "agregada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um regime de câmbio flutuante com perfeita mobilidade de capital, o aumento das tarifas "
                       "de importação leva a um novo equilíbrio com ") + vm("maiores") + az(" níveis de "
                       "exportações líquidas e da renda agregada.")),
        "poucas": ("A tarifa eleva NX e desloca a IS, mas o juro maior atrai capital e " + azb("aprecia o "
                   "câmbio") + ", o que derruba NX de volta. No equilíbrio final, " + vm("NX e renda ficam "
                   "iguais") + "; só o câmbio mudou."),
        "destrinchando": [
            "Tarifa ou cota reduz importações → NX ↑ → IS para a direita → Y e i sobem → com i &gt; i*, entra "
            "capital → câmbio se " + vd("aprecia") + " → exportações caem e importações (de outros bens) sobem "
            "→ NX ↓ → IS volta para a esquerda.",
            "O ajuste acaba quando o juro retorna a i*: como a LM não se moveu, a renda volta à inicial. Se Y, "
            "C, I e G são os mesmos, " + vd("NX também é o mesmo") + ": a restrição às importações " + azb("não "
            "melhora o saldo comercial") + ". O comércio encolhe dos dois lados (menos importações, menos "
            "exportações).",
            "É o mesmo resultado da política fiscal no câmbio flutuante: no Mundell-Fleming com BP horizontal, "
            + azb("choques reais de demanda não alteram a renda") + " sob câmbio flexível — o câmbio absorve "
            "tudo.",
            "Contraste: no " + azb("câmbio fixo") + ", a mesma tarifa eleva a renda (o Banco Central acomoda com "
            "expansão monetária) e melhora o saldo comercial — por isso o protecionismo foi tão usado em "
            "regimes de paridade fixa.",
            vm("Regra-âncora: câmbio flutuante + mobilidade perfeita → política comercial não move a renda nem "
               "o saldo comercial."),
        ],
        "dissecando": (cz("[extrapolação · troca de conceito]") + " O item descreve o <b>efeito de impacto</b> "
                       "(NX e Y sobem) como se fosse o equilíbrio final. A pista é “novo equilíbrio”: depois da "
                       "apreciação, NX e renda voltam ao nível inicial. 🔥 Tarifa no Mundell-Fleming é tema "
                       "recorrente e funciona como política fiscal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o aumento das tarifas de importação aprecia a moeda nacional e não altera a renda de "
            "equilíbrio.”</i> → CERTO",
            "<i>“Em regime de câmbio fixo com perfeita mobilidade de capital, o aumento das tarifas de importação "
            "eleva a renda.”</i> → CERTO",
        ])],
        "reescrita": ("Em um regime de câmbio flutuante com perfeita mobilidade de capital, o aumento das tarifas de "
                      "importação leva a um novo equilíbrio com " + hl("os mesmos") + " níveis de exportações "
                      "líquidas e da renda agregada" + hl(", com moeda nacional mais apreciada") + "."),
        "tipo_erro": ["EXTRAPOLACAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Tarifa reduz importações, IS para a direita, juros sobem, entra capital, moeda aprecia, "
                            "NX caem, IS volta; restrições às importações não aumentam NX; política comercial "
                            "ineficaz com câmbio flexível.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 182", "IS → IS′ com retorno ao equilíbrio inicial")],
        "alertas": ["quase_duplicata: ECO-E2-L01244-1 (tarifa no câmbio flutuante)"],
    },
    # ------------------------------------------------------------------ E2-L01238
    {
        "id": "ECO-E2-L01238-1", "fonte_ref": "E2-L01238", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_CONC,
        "rotulo_item": "Item",
        "assertiva": "Com o uso de controle de capitais, é possível um governo controlar o câmbio e os juros simultaneamente.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com o uso de <u>controle de capitais</u>, <u>é possível</u> um governo controlar o câmbio e "
                      "os juros simultaneamente."),
        "poucas": ("Pela " + azb("trindade impossível") + ", só se escolhem dois de três: câmbio fixo, autonomia "
                   "monetária e livre mobilidade de capitais. Abrindo mão da mobilidade (controles), o governo "
                   "pode fixar o câmbio e conduzir os juros."),
        "destrinchando": [
            "O " + azb("trilema") + " decorre do " + oc("modelo Mundell-Fleming") + ": com capital livre, o juro "
            "doméstico é amarrado ao externo (i = i* + prêmio de risco + expectativa de desvalorização). Se o "
            "câmbio também é fixo, o Banco Central não tem como escolher o juro.",
            "As três combinações possíveis: (1) " + vd("câmbio fixo + mobilidade") + " → sem política "
            "monetária própria (padrão-ouro, currency boards, países da zona do euro em relação ao BCE); (2) "
            + vd("câmbio flutuante + mobilidade") + " → política monetária autônoma (" + rx("Brasil")
            + " desde 1999, com metas de inflação); (3) " + vd("câmbio fixo + controles de capital") + " → "
            "autonomia monetária com paridade (Bretton Woods, 1944–1971; China por décadas).",
            "O controle de capitais quebra o elo entre o juro doméstico e o externo: diferenças de juros já não "
            "provocam fluxos ilimitados, e o Banco Central pode fixar o juro sem perder reservas em ritmo "
            "insustentável. A eficácia prática depende de os controles não serem contornados (subfaturamento, "
            "triangulação).",
            "O FMI passou a admitir, desde 2012, o uso de " + azb("medidas de gestão de fluxos de capital")
            + " em certas circunstâncias (a chamada “visão institucional”), o que deu respaldo a experiências "
            "como o IOF sobre capital estrangeiro no " + rx("Brasil") + " em 2009–2013.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item direto sobre o trilema, protegido pelo "
                       "“é possível”. A armadilha seria lembrar só do slogan “não dá para ter câmbio e juros "
                       "sob controle” e esquecer a condição: isso vale com <b>livre</b> mobilidade de capitais."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com livre mobilidade de capitais, é possível um governo controlar o câmbio e os juros "
            "simultaneamente.”</i> → ERRADO (viola o trilema)",
            "<i>“Com câmbio flutuante e livre mobilidade de capitais, o Banco Central preserva a autonomia da "
            "política monetária.”</i> → CERTO",
        ]), ("🃏 Carta na manga", [
            "O trilema ajuda a ler a história monetária brasileira: a âncora cambial do Real (1994–1999) exigiu "
            "juros altíssimos para atrair capital; a flutuação de 1999 devolveu ao Banco Central o comando dos "
            "juros, base do tripé macroeconômico."])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["é possível"], "dificuldade": 1,
        "comentario_fonte": "Trindade impossível: não é possível conciliar mobilidade perfeita, câmbio fixo e "
                            "política monetária independente; controles de capitais permitem manter câmbio fixo e "
                            "soberania monetária.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01241
    {
        "id": "ECO-E2-L01241-1", "fonte_ref": "E2-L01241", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("Uma política fiscal expansionista sob um regime de câmbio fixo com perfeita mobilidade de "
                      "capitais eleva o produto, mas gera um efeito de deslocamento (crowding-out)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma política fiscal expansionista sob um regime de câmbio fixo com perfeita mobilidade de "
                       "capitais eleva o produto") + vm(", mas gera um") + az(" efeito de deslocamento "
                                                                              "(crowding-out).")),
        "poucas": ("No câmbio fixo com mobilidade perfeita, o juro final é i* e o câmbio não se mexe: nada expulsa "
                   "o investimento nem as exportações líquidas. A fiscal eleva o produto " + vm("sem "
                   "crowding-out") + "."),
        "destrinchando": [
            azb("Crowding-out") + " (efeito deslocamento) é a redução de algum gasto privado provocada pela "
            "expansão do gasto público. Pode vir pelo " + vd("juro") + " (o investimento cai, na economia "
            "fechada) ou pelo " + vd("câmbio") + " (as exportações líquidas caem, no Mundell-Fleming com "
            "câmbio flutuante).",
            "No câmbio fixo com mobilidade perfeita, a expansão fiscal eleva o juro só por um instante; a entrada "
            "de capitais obriga o Banco Central a comprar divisas, a moeda se expande (LM para a direita) e o "
            "juro volta a " + vd("i*") + ". O câmbio, por definição, não muda.",
            "Sem juro maior e sem câmbio apreciado, o investimento e as exportações líquidas ficam onde estavam: "
            "o efeito sobre o produto é o " + azb("multiplicador pleno") + ". É o caso de " + vd("máxima "
            "eficácia") + " da política fiscal no modelo.",
            "Compare: economia fechada → crowding-out parcial (via juro); câmbio flutuante com mobilidade "
            "perfeita → crowding-out total (via câmbio); câmbio fixo com mobilidade perfeita → crowding-out nulo.",
            REGRA_MF,
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " “Eleva o produto” está certo; o erro foi "
                       "enxertado com o “mas”, importando o crowding-out da economia fechada (ou do câmbio "
                       "flutuante) para o único caso em que ele não existe. Pista: no câmbio fixo, o Banco "
                       "Central acomoda a expansão fiscal com moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…sob um regime de câmbio flutuante com perfeita mobilidade de capitais, gera crowding-out total "
            "via apreciação cambial.”</i> → CERTO",
            "<i>“…sob câmbio fixo com perfeita mobilidade de capitais, eleva o produto e a taxa de juros de "
            "equilíbrio.”</i> → ERRADO (o juro final é i*)",
        ])],
        "reescrita": ("Uma política fiscal expansionista sob um regime de câmbio fixo com perfeita mobilidade de "
                      "capitais eleva o produto" + hl(" e não gera") + " efeito de deslocamento (crowding-out)."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "IS para a direita, superávit no BP, Banco Central compra divisas e expande a moeda (LM "
                            "para a direita); produto aumenta sem crowding-out: juros e câmbio inalterados.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 220", "IS-LM-BP com E → E′ → E″")],
        "alertas": ["quase_duplicata: ECO-E2-L00903-1, ECO-E2-L00904-1"],
    },
    # ------------------------------------------------------------------ E2-L01242
    {
        "id": "ECO-E2-L01242-1", "fonte_ref": "E2-L01242", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("Uma contração monetária sob um regime de câmbio flutuante e mobilidade perfeita de capitais "
                      "resultará em uma apreciação do câmbio e uma queda do produto."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma contração monetária sob um regime de câmbio flutuante e mobilidade perfeita de capitais "
                      "resultará em uma <u>apreciação</u> do câmbio e uma <u>queda do produto</u>."),
        "poucas": ("No flutuante, a monetária é " + azb("eficaz") + ": a contração eleva o juro, atrai capital, "
                   + vd("aprecia o câmbio") + ", reduz NX e leva o produto para baixo."),
        "destrinchando": [
            "M ↓ → LM para a esquerda → i acima de i* (superávit no BP) → como o câmbio flutua, o excesso de "
            "divisas " + vd("aprecia a moeda") + " → NX ↓ → IS para a esquerda.",
            "No equilíbrio final, o juro volta a i* e a renda é a que a nova LM permite com i = i*: "
            + vd("menor") + ". Os dois canais (investimento e setor externo) somam efeitos na mesma direção.",
            "Diferença para o câmbio fixo: lá, a entrada de capitais obrigaria o Banco Central a comprar divisas, "
            "desfazendo a contração; a renda não mudaria e as reservas subiriam.",
            "Aplicação ⏳ (out/2026): em regimes de metas de inflação com câmbio flutuante, como o "
            + rx("brasileiro") + ", a apreciação provocada pela alta de juros é um dos canais de desinflação "
            "(barateia importados e reduz a demanda por bens domésticos).",
            REGRA_MF,
        ],
        "dissecando": (cz("[literalidade]") + " Resultado-padrão do modelo, com sinais corretos para câmbio e "
                       "produto. As variações erradas mais comuns trocam “apreciação” por “depreciação” ou o "
                       "regime para fixo (produto inalterado)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…resultará em uma depreciação do câmbio e uma queda do produto.”</i> → ERRADO (inversão: juro "
            "maior atrai capital e aprecia)",
            "<i>“Uma contração monetária sob câmbio fixo e mobilidade perfeita resultará em queda do "
            "produto.”</i> → ERRADO (no fixo, a monetária é ineficaz)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "LM para a esquerda, superávit no BP, apreciação, NX caem, IS para a esquerda; produto "
                            "menor no novo equilíbrio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01025-1"],
    },
    # ------------------------------------------------------------------ E2-L01244
    {
        "id": "ECO-E2-L01244-1", "fonte_ref": "E2-L01244", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("Um aumento de tarifas para importação tem efeito positivo sobre o produto em uma economia com "
                      "regime de câmbio flutuante."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um aumento de tarifas para importação ") + vm("tem efeito positivo") + az(" sobre o "
                       "produto em uma economia com regime de câmbio flutuante.")),
        "poucas": ("No Mundell-Fleming (pequena economia, mobilidade perfeita), a tarifa desloca a IS, mas a "
                   + azb("apreciação cambial") + " reduz NX e devolve a IS ao lugar: " + vm("o produto não se "
                   "altera") + "."),
        "destrinchando": [
            "A tarifa reduz importações e eleva NX: a IS vai para a direita e, no impacto, Y e i sobem. O juro "
            "acima de i* gera superávit no balanço de pagamentos; com câmbio flutuante, a moeda " + vd("se "
            "valoriza") + ".",
            "A valorização reduz exportações e estimula importações dos bens não tarifados: NX volta ao nível "
            "inicial e a IS retorna. Como a LM está parada e o juro tem de ser i*, a renda final é a mesma.",
            "Premissa do resultado: " + azb("BP horizontal") + " (pequena economia com mobilidade perfeita), "
            "que é a hipótese-padrão do Mundell-Fleming. Com mobilidade imperfeita, a análise fica menos "
            "nítida e depende das inclinações de BP e LM.",
            "Implicação de política: no câmbio flutuante, protecionismo não estimula a atividade nem corrige o "
            "saldo comercial; apenas reduz o volume de comércio e muda o preço relativo da moeda. No câmbio "
            "fixo, a mesma tarifa seria expansionista.",
            vm("Regra-âncora: câmbio flutuante + mobilidade perfeita → tarifa = política fiscal → ineficaz sobre "
               "a renda."),
        ],
        "dissecando": (cz("[nexo indevido · troca de conceito]") + " O item aposta no raciocínio de impacto "
                       "(menos importações = mais produto) e omite a reação do câmbio. Não menciona a mobilidade "
                       "de capitais: a banca assume o padrão do modelo (pequena economia, BP horizontal). "
                       "🔥 Tarifa no flutuante = ERRADO quando se fala em efeito sobre renda ou saldo comercial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um aumento de tarifas para importação tem efeito positivo sobre o produto em uma economia com "
            "câmbio fixo e perfeita mobilidade de capitais.”</i> → CERTO",
            "<i>“…em regime de câmbio flutuante, o aumento de tarifas melhora o saldo da balança "
            "comercial.”</i> → ERRADO (a apreciação anula o efeito)",
        ])],
        "reescrita": ("Um aumento de tarifas para importação " + hl("não tem efeito") + " sobre o produto em uma "
                      "economia com regime de câmbio flutuante" + hl(" e perfeita mobilidade de capitais") + "."),
        "tipo_erro": ["NEXO_INDEVIDO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Tarifa eleva NX e desloca a IS; superávit no BP; câmbio valoriza; NX caem; IS volta e "
                            "o produto não se altera (BP horizontal da pequena economia do Mundell-Fleming).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 222", "IS → IS′, E → E′")],
        "alertas": ["quase_duplicata: ECO-E2-L01046-1"],
    },
    # ------------------------------------------------------------------ E2-L01445
    {
        "id": "ECO-E2-L01445-1", "fonte_ref": "E2-L01445", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_A,
        "rotulo_item": "Item",
        "assertiva": ("Se o Brasil tem perfeita mobilidade de capitais e um regime de câmbio flutuante, a redução de "
                      "juros pelo Banco Central terá mais eficácia em combater os impactos da pandemia do que a "
                      "expansão de gastos do governo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o Brasil tem perfeita mobilidade de capitais e um regime de câmbio flutuante, a "
                      "<u>redução de juros</u> pelo Banco Central terá <u>mais eficácia</u> em combater os impactos "
                      "da pandemia do que a expansão de gastos do governo."),
        "poucas": ("No Mundell-Fleming com câmbio flutuante e mobilidade perfeita, a " + azb("monetária") + " é "
                   "eficaz (juro ↓ → depreciação → NX ↑) e a " + azb("fiscal") + " é ineficaz (apreciação → NX ↓). "
                   "Logo, cortar juros estimula mais a demanda do que gastar."),
        "destrinchando": [
            "Corte de juros: LM para a direita → i abaixo de i* → saída de capitais → " + vd("depreciação")
            + " → exportações mais competitivas, importações mais caras → NX ↑ → IS também para a direita. "
            "Os canais doméstico (investimento, consumo) e externo se somam.",
            "Expansão de gastos: IS para a direita → i acima de i* → entrada de capitais → " + vd("apreciação")
            + " → NX ↓ → IS volta. Com mobilidade perfeita, o efeito sobre a renda é " + vd("nulo") + ": "
            "crowding-out completo via câmbio.",
            "O item é julgado <b>dentro do modelo</b>. Na pandemia real, havia ressalvas: o choque era também "
            "de oferta, a Selic chegou a " + vd("2% a.a.") + " em 2020 (perto do limite inferior) e boa parte "
            "do gasto público tinha função de proteção de renda (auxílio emergencial), não de estímulo "
            "keynesiano clássico. Nada disso muda o gabarito, que pede a conclusão teórica.",
            "A mesma lógica explica a recomendação usual para economias com câmbio flutuante e conta de capital "
            "aberta: usar a política monetária como instrumento principal de estabilização da demanda.",
            REGRA_MF,
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O contexto da pandemia é distrator: puxa para a "
                       "intuição de que gasto público é o remédio óbvio. Mas as premissas dadas (mobilidade "
                       "perfeita + câmbio flutuante) definem o resultado do modelo. 🔥 Itens desse professor "
                       "embrulham o Mundell-Fleming em conjuntura brasileira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se o Brasil tem perfeita mobilidade de capitais e câmbio fixo, a redução de juros terá mais "
            "eficácia do que a expansão de gastos.”</i> → ERRADO (troca de regime: no fixo, só a fiscal é "
            "eficaz)",
            "<i>“…a redução de juros terá mais eficácia porque provoca apreciação do real e barateia "
            "importações.”</i> → ERRADO (inversão: o corte de juros deprecia o real)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Monetária eficaz e fiscal ineficaz com câmbio flutuante e mobilidade perfeita "
                            "(vários comentários de IA convergentes, com ressalvas sobre a pandemia).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 343", "expansão fiscal no flutuante: IS vai e volta")],
        "alertas": ["quase_duplicata: ECO-E2-L01584-1 (monetária no flutuante com mobilidade alta)"],
    },
    # ------------------------------------------------------------------ E2-L01446
    {
        "id": "ECO-E2-L01446-1", "fonte_ref": "E2-L01446", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_A,
        "excerto": ("<p><i>Proposição anterior, à qual o item se refere: “Se o Brasil tem perfeita mobilidade de "
                    "capitais e um regime de câmbio flutuante, a redução de juros pelo Banco Central terá mais "
                    "eficácia em combater os impactos da pandemia do que a expansão de gastos do governo.”</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("Na situação do item anterior, se o governo proíbe os fluxos de capital, a política fiscal será "
                      "eficaz e a política monetária ineficaz para estimular a economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na situação do item anterior, se o governo proíbe os fluxos de capital, a política fiscal "
                       "será eficaz e a política monetária ") + vm("ineficaz") + az(" para estimular a "
                                                                                    "economia.")),
        "poucas": ("Sem mobilidade de capital e com câmbio flutuante, a BP é vertical e o câmbio ajusta a balança "
                   "comercial: " + azb("as duas políticas são eficazes") + ", ambas reforçadas pela "
                   "depreciação. A monetária não fica ineficaz."),
        "destrinchando": [
            "Proibir fluxos de capital torna a " + azb("BP vertical") + ": o balanço de pagamentos se reduz à "
            "balança comercial, que só depende da renda (importações) e do câmbio. O juro deixa de afetar o "
            "equilíbrio externo.",
            "Política monetária: LM para a direita → i ↓, Y ↑ → importações sobem → déficit comercial → "
            "com câmbio flutuante, " + vd("depreciação") + " → NX ↑ → IS e BP para a direita → Y sobe ainda "
            "mais. " + vd("Eficaz") + ".",
            "Política fiscal: IS para a direita → Y ↑ → déficit comercial → depreciação → IS e BP para a "
            "direita. Também " + vd("eficaz") + " — e, sem a entrada de capitais, não há apreciação para "
            "anulá-la, como havia com mobilidade perfeita.",
            "Pela " + azb("trindade impossível") + ", abrir mão da mobilidade de capitais devolve graus de "
            "liberdade; com o câmbio também flutuando, o país tem autonomia monetária plena. Ineficácia da "
            "monetária é marca do <b>câmbio fixo</b>, não da falta de mobilidade.",
            vm("Regra-âncora: câmbio flutuante → a monetária é eficaz em qualquer grau de mobilidade de capital."),
        ],
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A primeira parte (fiscal eficaz) é verdadeira "
                       "e dá credibilidade ao item; o erro está no “ineficaz”, que pertence ao câmbio fixo. A "
                       "pista: o regime continua flutuante — e câmbio flutuante nunca anula a política "
                       "monetária no modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…se o governo proíbe os fluxos de capital e fixa o câmbio, a política monetária torna-se "
            "ineficaz para estimular a economia.”</i> → CERTO",
            "<i>“…se o governo proíbe os fluxos de capital, mantido o câmbio flutuante, ambas as políticas "
            "elevam a renda, acompanhadas de depreciação cambial.”</i> → CERTO",
        ])],
        "reescrita": ("Na situação do item anterior, se o governo proíbe os fluxos de capital, a política fiscal será "
                      "eficaz e a política monetária " + hl("também eficaz") + " para estimular a economia."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Sem mobilidade de capitais e com câmbio flutuante, ambas as políticas são eficazes (BP "
                            "vertical; depreciação reforça); vários comentários de IA, um deles dizendo que a "
                            "monetária “perde o canal cambial”, o que é impreciso.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [corte("IMAGEM 343", "expansão fiscal no flutuante com mobilidade perfeita"),
                          corte("IMAGEM 344", "expansão fiscal no flutuante sem mobilidade de capital")],
        "alertas": ["qualidade_fonte: um dos comentários de IA dizia que, sem mobilidade, a monetária perde o canal "
                    "cambial; na verdade, com BP vertical e câmbio flutuante, a depreciação reforça a expansão "
                    "monetária"],
    },
    # ------------------------------------------------------------------ E2-L01486
    {
        "id": "ECO-E2-L01486-1", "fonte_ref": "E2-L01486", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_PAND,
        "rotulo_item": "Item",
        "assertiva": ("Supondo que o Brasil tem alta mobilidade de capitais, e que o BC quisesse manter o câmbio "
                      "fixo, não deixando a moeda se depreciar, esta política de redução de juros seria ineficaz em "
                      "estimular a atividade econômica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Supondo que o Brasil tem <u>alta mobilidade de capitais</u>, e que o BC quisesse manter o "
                      "<u>câmbio fixo</u>, não deixando a moeda se depreciar, esta política de redução de juros "
                      "seria <u>ineficaz</u> em estimular a atividade econômica."),
        "poucas": ("Câmbio fixo + mobilidade alta: o corte de juros provoca saída de capitais; para segurar o "
                   "câmbio, o BC " + vd("vende reservas") + " e recolhe a moeda que tinha emitido. A LM volta e a "
                   "atividade não reage: " + azb("política monetária ineficaz") + "."),
        "destrinchando": [
            "Mecanismo: redução de juros (LM para a direita) → i abaixo de i* + prêmio de risco → saída de "
            "capitais → pressão de " + azb("depreciação") + ". Para manter a paridade, o BC vende moeda "
            "estrangeira e compra reais: a base monetária encolhe e a LM retorna à posição inicial.",
            "Resultado: " + vd("renda e juros iguais aos iniciais") + ", reservas menores. A tentativa de baixar "
            "juros apenas troca reservas internacionais por títulos na carteira do BC.",
            "É a " + azb("trindade impossível") + ": câmbio fixo + mobilidade de capitais = sem autonomia "
            "monetária. Com reservas finitas, insistir na expansão termina em crise cambial — o que aconteceu "
            "com várias âncoras cambiais nos anos 1990.",
            "Conexão histórica: em janeiro de 1999, o " + rx("Brasil") + " abandonou a banda cambial depois de "
            "perder reservas em sequência; a flutuação devolveu ao Banco Central a capacidade de usar os juros "
            "para metas domésticas (adoção do regime de metas de inflação em junho de 1999).",
            REGRA_MF,
        ],
        "dissecando": (cz("[literalidade]") + " Aplicação direta do trilema, vestida de conjuntura. A expressão "
                       "“não deixando a moeda se depreciar” é a chave: o BC compromete a política monetária com "
                       "a paridade, e a redução de juros é desfeita pela venda de reservas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…esta política de redução de juros seria eficaz, pois a saída de capitais elevaria as "
            "exportações líquidas.”</i> → ERRADO (com câmbio fixo, não há depreciação)",
            "<i>“…se o BC deixasse o câmbio flutuar, a redução de juros estimularia a atividade via depreciação "
            "cambial.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Com câmbio fixo e alta mobilidade, a política monetária é ineficaz (trilema): a saída de "
                            "capitais obriga o BC a vender reservas e contrair a base, anulando o estímulo.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00905-1, ECO-E2-L01630-1"],
    },
    # ------------------------------------------------------------------ E2-L01487
    {
        "id": "ECO-E2-L01487-1", "fonte_ref": "E2-L01487", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_PAND,
        "excerto": ("<p><i>Proposição anterior, à qual o item se refere: “Supondo que o Brasil tem alta mobilidade "
                    "de capitais, e que o BC quisesse manter o câmbio fixo, não deixando a moeda se depreciar, esta "
                    "política de redução de juros seria ineficaz em estimular a atividade econômica.”</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("No caso do item anterior, se o Brasil aplicasse controles proibindo a mobilidade de capital, "
                      "com câmbio fixo, a política de redução de juros seria eficaz em expandir a renda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No caso do item anterior, se o Brasil aplicasse controles proibindo a mobilidade de "
                       "capital, com câmbio fixo, a política de redução de juros seria ") + vm("eficaz")
                    + az(" em expandir a renda.")),
        "poucas": ("Mesmo sem mobilidade de capital, o câmbio fixo anula a monetária: a renda maior eleva as "
                   "importações, surge " + azb("déficit comercial") + ", o BC vende reservas e a moeda volta a "
                   "encolher. A renda retorna ao nível inicial."),
        "destrinchando": [
            "Sem mobilidade, a " + azb("BP é vertical") + " no nível de renda que equilibra a balança comercial "
            "(Y₀). Não há fuga de capitais quando o juro cai — esse canal some.",
            "Mas há outro: a expansão monetária (LM para a direita) reduz o juro e eleva a renda para Y₁ &gt; Y₀. "
            "Com mais renda, as importações sobem e aparece " + vd("déficit no balanço de pagamentos") + " "
            "(excesso de demanda por divisas).",
            "Para manter o câmbio fixo, o BC " + vd("vende reservas") + ", contraindo a oferta monetária; a LM "
            "volta até a renda coincidir de novo com Y₀. No equilíbrio final, só caíram as reservas.",
            "O ajuste é mais lento que com mobilidade perfeita (passa pela balança comercial, não por fluxos "
            "financeiros instantâneos), e um BC com muitas reservas pode sustentar o estímulo por algum tempo. "
            "No modelo, porém, o resultado de equilíbrio é a " + azb("ineficácia") + ".",
            vm("Regra-âncora: câmbio fixo → política monetária ineficaz em qualquer grau de mobilidade; o que "
               "muda com a mobilidade é a velocidade da perda de reservas."),
        ],
        "dissecando": (cz("[nexo indevido · extrapolação]") + " O item supõe que, eliminada a fuga de capitais, "
                       "acaba o problema; esquece o canal comercial. É o erro de tratar o trilema como se só "
                       "falasse de capitais: no modelo, o câmbio fixo amarra a moeda ao balanço de pagamentos "
                       "inteiro. Quem pensa no curto prazo (antes da perda de reservas) tende a marcar CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com controles de capital e câmbio flutuante, a política de redução de juros seria eficaz em "
            "expandir a renda.”</i> → CERTO",
            "<i>“…com controles de capital e câmbio fixo, a política fiscal expansionista seria eficaz em "
            "expandir a renda.”</i> → ERRADO (com BP vertical e câmbio fixo, a fiscal também é ineficaz)",
        ])],
        "reescrita": ("No caso do item anterior, se o Brasil aplicasse controles proibindo a mobilidade de capital, "
                      "com câmbio fixo, a política de redução de juros seria " + hl("ineficaz") + " em expandir a "
                      "renda."),
        "tipo_erro": ["NEXO_INDEVIDO", "EXTRAPOLACAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Mesmo com controles de capital, sob câmbio fixo, o aumento da renda gera déficit "
                            "comercial e perda de reservas; o BC contrai a moeda e a LM volta (gráfico IS-LM-BP com "
                            "BP vertical, A → B → A).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 380", "expansão monetária com câmbio fixo sem mobilidade, A → B → A")],
        "alertas": ["quase_duplicata: ECO-E2-L01586-1 (monetária no câmbio fixo com baixa mobilidade)"],
    },
    # ------------------------------------------------------------------ E2-L01513
    {
        "id": "ECO-E2-L01513-1", "fonte_ref": "E2-L01513", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_B,
        "rotulo_item": "Item",
        "assertiva": ("Num regime de câmbio flexível e perfeita mobilidade de capitais, a política fiscal será "
                      "ineficaz em expandir a demanda agregada, devido à apreciação cambial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Num regime de câmbio flexível e perfeita mobilidade de capitais, a política fiscal será "
                      "<u>ineficaz</u> em expandir a demanda agregada, devido à <u>apreciação cambial</u>."),
        "poucas": ("É o caso clássico: expansão fiscal → juro acima de i* → entrada de capitais → "
                   + azb("apreciação") + " → NX caem exatamente o que G subiu. A demanda agregada (e a renda) não "
                   "muda."),
        "destrinchando": [
            "A IS desloca-se para a direita com o gasto maior. O juro tende a subir; com mobilidade perfeita, "
            "basta um diferencial mínimo em relação a i* para atrair capital em grande volume, e o câmbio "
            "flexível se " + vd("aprecia") + ".",
            "Apreciação → exportações caem, importações sobem → " + vd("NX ↓") + " → IS volta à posição "
            "inicial. Equilíbrio final: mesmo Y, mesmo i (= i*), câmbio mais apreciado, " + vd("ΔNX = −ΔG")
            + ".",
            "“Demanda agregada” aqui é a demanda total por bens domésticos (C + I + G + NX), que no equilíbrio "
            "do IS-LM coincide com a renda. Ela não se expande porque a perda no setor externo compensa o "
            "gasto público: muda a composição, não o total.",
            "O mesmo raciocínio vale ao contrário: uma " + azb("contração fiscal") + " deprecia o câmbio, eleva "
            "NX e também não altera a renda.",
            REGRA_MF,
        ],
        "dissecando": (cz("[literalidade]") + " Enunciado do resultado-padrão, com o mecanismo correto (apreciação). "
                       "Pegadinhas habituais: trocar “apreciação” por “depreciação”, ou atribuir a ineficácia à "
                       "alta dos juros (que, no equilíbrio final, não ocorre)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a política fiscal será ineficaz em expandir a demanda agregada, devido à elevação permanente "
            "da taxa de juros doméstica.”</i> → ERRADO (o juro final é i*; o canal é o câmbio)",
            "<i>“Num regime de câmbio fixo e perfeita mobilidade de capitais, a política fiscal será ineficaz "
            "devido à apreciação cambial.”</i> → ERRADO (troca de regime)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Expansão fiscal eleva os juros, atrai capital, aprecia a moeda e reduz NX; a IS volta: "
                            "crowding-out externo, política fiscal ineficaz.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 393", "três diagramas IS-LM-BP de expansão fiscal")],
        "alertas": ["quase_duplicata: ECO-E2-L00906-1, ECO-E2-L01024-1"],
    },
    # ------------------------------------------------------------------ E2-L01514
    {
        "id": "ECO-E2-L01514-1", "fonte_ref": "E2-L01514", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_B,
        "rotulo_item": "Item",
        "assertiva": ("Num regime de câmbio fixo e sem mobilidade de capital, a política fiscal expansionista levará "
                      "a um superávit comercial e terá máxima eficácia em expandir o produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Num regime de câmbio fixo e sem mobilidade de capital, a política fiscal expansionista "
                       "levará a um ") + vm("superávit") + az(" comercial e ") + vm("terá máxima eficácia")
                    + az(" em expandir o produto.")),
        "poucas": ("Dois erros: a expansão fiscal gera " + vm("déficit") + " comercial (mais renda, mais "
                   "importações), e a defesa do câmbio contrai a moeda até a renda voltar ao nível de equilíbrio "
                   "externo. Com BP vertical, a fiscal é " + vm("ineficaz") + "."),
        "destrinchando": [
            "Sem mobilidade de capital, a " + azb("BP é vertical") + ": existe um único nível de renda (Y₁) que "
            "equilibra a balança comercial ao câmbio fixado. Qualquer renda maior gera déficit.",
            "G ↑ → IS para a direita → Y e i sobem (ponto à direita da BP) → importações sobem → "
            + vd("déficit comercial") + " → excesso de demanda por divisas. Juro maior não atrai capital (não "
            "há mobilidade), então nada compensa o déficit.",
            "Para manter a paridade, o BC " + vd("vende reservas") + " e a oferta de moeda cai: a LM se desloca "
            "para a esquerda até cruzar a nova IS sobre a BP. Equilíbrio final: " + vd("renda igual a Y₁")
            + ", juro maior, reservas menores. O gasto público expulsou investimento na mesma medida "
            "(" + azb("crowding-out total via juros") + ").",
            "Onde está a “máxima eficácia”? No câmbio fixo com <b>mobilidade perfeita</b>: lá, o juro maior atrai "
            "capital, o BC compra divisas e a moeda se expande junto. O item trocou o grau de mobilidade.",
            vm("Regra-âncora (câmbio fixo): a eficácia da fiscal cresce com a mobilidade de capital — nula sem "
               "mobilidade, máxima com mobilidade perfeita."),
        ],
        "grafico_verso": "ECO-E2-L01514-1-V1",
        "dissecando": (cz("[inversão · troca de conceito]") + " Dois erros empilhados: o sinal do saldo comercial "
                       "(superávit × déficit) e o caso de mobilidade (a “máxima eficácia” é da mobilidade "
                       "perfeita). Muitos comentários tratam a fiscal como “eficaz” nesse caso e só apontam o "
                       "superávit; no equilíbrio do modelo, ela é ineficaz. Basta o primeiro erro para marcar "
                       "ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Num regime de câmbio fixo e com perfeita mobilidade de capital, a política fiscal expansionista "
            "terá máxima eficácia em expandir o produto.”</i> → CERTO",
            "<i>“…sem mobilidade de capital, a política fiscal expansionista provocará perda de reservas e "
            "aumento da taxa de juros, sem alterar o produto de equilíbrio.”</i> → CERTO",
        ])],
        "reescrita": ("Num regime de câmbio fixo e sem mobilidade de capital, a política fiscal expansionista levará "
                      "a um " + hl("déficit") + " comercial" + hl(" transitório") + " e " + hl("será ineficaz")
                      + " em expandir o produto."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": ["máxima"], "dificuldade": 2,
        "comentario_fonte": "Expansão fiscal com câmbio fixo e sem mobilidade gera déficit comercial, não superávit; "
                            "comentários divergem sobre a eficácia (um diz “eficaz”; as figuras e a análise fundida "
                            "da linha duplicada concluem “política fiscal ineficaz”, com retorno da renda ao nível "
                            "inicial).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [redes("IMAGEM 394", "ECO-E2-L01514-1-V1", "fiscal com câmbio fixo sem mobilidade"),
                          {"ref": "IMAGEM 469 (linha E2-L01629)", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (mesmo mecanismo; absorvida no 📖)"}],
        "alertas": ["duplicata: E2-L01629 (mesma assertiva, mesma prova) fundida neste card",
                    "qualidade_fonte: o primeiro comentário da fonte dava a política fiscal como “eficaz” nesse "
                    "caso; com BP vertical e câmbio fixo, a renda de equilíbrio volta ao nível inicial"],
    },
    # ------------------------------------------------------------------ E2-L01515
    {
        "id": "ECO-E2-L01515-1", "fonte_ref": "E2-L01515", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_B,
        "rotulo_item": "Item",
        "assertiva": ("Numa economia aberta ao comércio porém sem mobilidade de capital, uma política monetária "
                      "expansionista será menos eficaz em expandir o produto do que numa economia fechada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Numa economia aberta ao comércio porém sem mobilidade de capital, uma política monetária "
                       "expansionista será ") + vm("menos") + az(" eficaz em expandir o produto do que numa "
                                                                 "economia fechada.")),
        "poucas": ("Com câmbio flexível (a leitura da fonte), a expansão monetária gera déficit comercial, o câmbio "
                   "se " + azb("deprecia") + ", NX sobe e a renda cresce " + vm("mais") + " do que numa economia "
                   "fechada."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O item não informa o regime cambial. A fonte dá ERRADO supondo câmbio flexível, em que "
                          "a abertura comercial amplia a eficácia monetária. Mas, com " + azb("câmbio fixo")
                          + " e sem mobilidade, a monetária é ineficaz (o BC perde reservas e a LM volta), e aí "
                          "ela seria, sim, " + vm("menos eficaz") + " que numa economia fechada. A leitura mais "
                          "defensável exige especificar o regime; mantido o gabarito da fonte.")],
        "destrinchando": [
            "Economia fechada: M ↑ → LM para a direita → i ↓ → I ↑ → Y ↑. Só o canal dos juros.",
            "Economia aberta, sem mobilidade, " + vd("câmbio flexível") + ": a renda maior eleva as importações; "
            "sem fluxos de capital, o déficit comercial " + vd("deprecia o câmbio") + "; NX ↑ desloca a IS (e a "
            "BP vertical) para a direita. Ao canal dos juros soma-se o canal cambial: " + vd("mais eficaz")
            + " que na economia fechada.",
            "Economia aberta, sem mobilidade, " + vd("câmbio fixo") + ": o déficit comercial obriga o BC a vender "
            "reservas; a moeda encolhe e a renda volta ao nível que equilibra a balança comercial. "
            + vd("Ineficaz") + ".",
            "Moral: a comparação “aberta × fechada” depende do regime. No câmbio flexível, a abertura reforça a "
            "monetária e enfraquece a fiscal (quando há mobilidade de capital); no câmbio fixo, faz o contrário.",
            vm("Regra-âncora: câmbio flexível → a abertura comercial amplia a eficácia da política monetária."),
        ],
        "dissecando": (cz("[inversão · extrapolação]") + " O item inverte a comparação (“menos” no lugar de “mais”) "
                       "para o caso de câmbio flexível, que é o que a fonte tem em mente. A omissão do regime "
                       "cambial abre margem a recurso: com câmbio fixo, a afirmação se sustentaria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Numa economia aberta sem mobilidade de capital e com câmbio flexível, a política monetária "
            "expansionista será mais eficaz do que numa economia fechada.”</i> → CERTO",
            "<i>“…com câmbio fixo e sem mobilidade de capital, a política monetária expansionista será mais "
            "eficaz do que numa economia fechada.”</i> → ERRADO (no fixo, ela é ineficaz)",
        ])],
        "reescrita": ("Numa economia aberta ao comércio porém sem mobilidade de capital, uma política monetária "
                      "expansionista será " + hl("mais") + " eficaz em expandir o produto do que numa economia "
                      "fechada" + hl(", se o câmbio for flexível") + "."),
        "tipo_erro": ["INVERSAO", "EXTRAPOLACAO"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": "Com câmbio flexível, a depreciação potencializa a monetária (mais eficaz que na economia "
                            "fechada); com câmbio fixo, ela seria ineficaz; a fonte considera a assertiva errada "
                            "pela possibilidade de maior eficácia.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 395", "aumento do risco-país com câmbio flexível"),
                          corte("IMAGEM 396", "expansão monetária com câmbio fixo sem mobilidade")],
        "alertas": ["contestavel: o item não especifica o regime cambial; com câmbio fixo e sem mobilidade, a "
                    "política monetária é ineficaz e a afirmação seria verdadeira; gabarito da fonte (ERRADO) "
                    "mantido, na leitura de câmbio flexível"],
    },
    # ------------------------------------------------------------------ E2-L01516
    {
        "id": "ECO-E2-L01516-1", "fonte_ref": "E2-L01516", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_B,
        "rotulo_item": "Item",
        "assertiva": ("Com perfeita mobilidade de capital, países com regimes cambiais flexíveis tendem a ter menores "
                      "perdas, em termos de produto e emprego, do que países com regimes de câmbio fixo, ao serem "
                      "acometidos por fugas de capital."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com perfeita mobilidade de capital, países com regimes cambiais <u>flexíveis</u> tendem a ter "
                      "<u>menores perdas</u>, em termos de produto e emprego, do que países com regimes de câmbio "
                      "fixo, ao serem acometidos por fugas de capital."),
        "poucas": ("Na fuga de capitais, o câmbio flexível " + azb("deprecia") + " e estimula as exportações "
                   "líquidas (amortecedor); o câmbio fixo exige " + vd("venda de reservas") + " e contração "
                   "monetária, com juros mais altos e recessão."),
        "destrinchando": [
            "Uma fuga de capitais (alta do risco-país, alta de i*, expectativa de desvalorização) eleva o juro "
            "que o país precisa pagar para reter capital: a " + azb("BP horizontal sobe") + " (i = i* + prêmio "
            "de risco + desvalorização esperada).",
            vd("Câmbio fixo") + ": para defender a paridade, o BC vende reservas e recolhe moeda doméstica; a LM "
            "se desloca para a esquerda até o juro doméstico alcançar o novo patamar. Juros maiores, "
            + vd("produto e emprego menores") + ". O ajuste é todo pela recessão.",
            vd("Câmbio flexível") + ": a saída de capitais deprecia a moeda; exportações líquidas sobem e a IS "
            "vai para a direita. No modelo-padrão, o produto até " + vd("aumenta") + " (o juro sobe pela maior "
            "demanda por moeda, com a mesma oferta). O câmbio funciona como " + azb("amortecedor de "
            "choques") + ".",
            "Na prática ⏳ (out/2026), a depreciação forte tem custos que o modelo ignora: repasse para a "
            "inflação e efeito patrimonial sobre empresas endividadas em dólar. Mesmo assim, a experiência das "
            "crises dos anos 1990 (México 1994, Ásia 1997, Rússia 1998, " + rx("Brasil") + " 1999) é "
            "frequentemente citada a favor da flexibilidade.",
            vm("Regra-âncora: choque financeiro externo → câmbio fixo amplifica a recessão; câmbio flexível a "
               "amortece."),
        ],
        "grafico_verso": "ECO-E2-L01516-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " Item comparativo protegido por “tendem a”. "
                       "O raciocínio-chave é que, no câmbio fixo, a defesa da paridade transforma a fuga de "
                       "capitais em contração monetária. 🔥 A versão errada costuma inverter os regimes "
                       "(“maiores perdas” no flexível)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…países com regimes cambiais flexíveis tendem a ter maiores perdas, em termos de produto e "
            "emprego, do que países com câmbio fixo, diante de fugas de capital.”</i> → ERRADO (inversão)",
            "<i>“Sob câmbio fixo, uma fuga de capitais obriga o Banco Central a vender reservas, reduzindo a "
            "oferta monetária e o produto.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tendem a"], "dificuldade": 2,
        "comentario_fonte": "Câmbio fixo: venda de reservas, contração monetária, juros maiores, recessão. Câmbio "
                            "flexível: depreciação, NX ↑, IS para a direita, amortecendo ou compensando a perda.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [redes("IMAGEM 397", "ECO-E2-L01516-1-V1", "fuga de capitais com câmbio fixo"),
                          redes("IMAGEM 395", "ECO-E2-L01516-1-V1", "fuga de capitais com câmbio flexível")],
        "alertas": ["quase_duplicata: ECO-E2-L01631-1 (mesmo item sem “e emprego”)"],
    },
    # ------------------------------------------------------------------ E2-L01550
    {
        "id": "ECO-E2-L01550-1", "fonte_ref": "E2-L01550", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_C,
        "rotulo_item": "Item",
        "assertiva": ("Considere que um país esteja com economia muito aquecida, com pressões inflacionárias, e que o "
                      "governo deseja implementar uma política de retração da demanda agregada. Um aumento do "
                      "resultado fiscal do governo, num contexto de câmbio flexível e perfeita mobilidade de "
                      "capitais, vai levar à depreciação cambial e aumento do saldo comercial, mas não será eficaz "
                      "em reduzir a demanda agregada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere que um país esteja com economia muito aquecida, com pressões inflacionárias, e que "
                      "o governo deseja implementar uma política de retração da demanda agregada. Um <u>aumento do "
                      "resultado fiscal</u> do governo, num contexto de câmbio flexível e perfeita mobilidade de "
                      "capitais, vai levar à <u>depreciação</u> cambial e aumento do saldo comercial, mas <u>não "
                      "será eficaz</u> em reduzir a demanda agregada."),
        "poucas": ("“Aumento do resultado fiscal” = " + azb("contração fiscal") + ". No flutuante com mobilidade "
                   "perfeita, ela reduz o juro, provoca saída de capitais, " + vd("deprecia") + " o câmbio e eleva "
                   "NX na mesma medida do corte de gasto: a demanda agregada não cai."),
        "destrinchando": [
            "Vocabulário: elevar o " + azb("resultado fiscal") + " (primário) é cortar gastos ou aumentar "
            "impostos — política fiscal contracionista. A IS vai para a esquerda.",
            "Mecanismo: IS ← → i tende a cair abaixo de i* → saída de capitais → " + vd("depreciação") + " → "
            "exportações sobem, importações caem → " + vd("NX ↑") + " → IS volta à posição inicial.",
            "Equilíbrio final: renda e demanda agregada inalteradas; menos G (ou mais T) e mais NX: o saldo "
            "comercial melhora. É o espelho do crowding-out externo da expansão fiscal.",
            "Implicação para a estabilização: para esfriar a economia nesse regime, o instrumento eficaz é a "
            + azb("política monetária contracionista") + " (juro ↑ → apreciação → NX ↓, reforçando a queda da "
            "demanda). A contração fiscal serve a outros fins — por exemplo, a sustentabilidade da dívida ou a "
            "melhora das contas externas.",
            REGRA_MF,
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O item exige duas traduções: “aumento do "
                       "resultado fiscal” = contração, e o resultado do flutuante com mobilidade perfeita = "
                       "fiscal ineficaz. A narrativa de economia superaquecida empurra para a intuição de que "
                       "cortar gastos esfria a demanda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…um aumento do resultado fiscal vai levar à apreciação cambial e à redução do saldo "
            "comercial.”</i> → ERRADO (inversão: a contração fiscal deprecia)",
            "<i>“…num contexto de câmbio fixo e perfeita mobilidade de capitais, um aumento do resultado fiscal "
            "será eficaz em reduzir a demanda agregada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Contração fiscal com câmbio flexível e mobilidade perfeita: juros caem, saída de "
                            "capitais, depreciação, saldo comercial maior; demanda agregada inalterada (vários "
                            "comentários de IA; um falava em compensação “parcial”).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 419", "IS-LM-BP com BP horizontal em i = i*")],
        "alertas": ["quase_duplicata: ECO-E2-L01628-1 (contração fiscal no flutuante com mobilidade perfeita)"],
    },
    # ------------------------------------------------------------------ E2-L01551
    {
        "id": "ECO-E2-L01551-1", "fonte_ref": "E2-L01551", "destino": "70", "subtema": H2["bp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_C,
        "rotulo_item": "Item",
        "assertiva": ("Uma política fiscal expansionista leva a um superávit temporário do saldo do balanço de "
                      "pagamentos (BP), se houver baixa mobilidade de capital, e a um déficit temporário do BP, se a "
                      "mobilidade de capitais for alta."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma política fiscal expansionista leva a um ") + vm("superávit") + az(" temporário do saldo "
                       "do balanço de pagamentos (BP), se houver baixa mobilidade de capital, e a um ")
                    + vm("déficit") + az(" temporário do BP, se a mobilidade de capitais for alta.")),
        "poucas": ("Está invertido. Com " + azb("baixa mobilidade") + ", domina o efeito renda (mais importações): "
                   + vd("déficit") + ". Com " + azb("alta mobilidade") + ", domina o efeito juros (entrada de "
                   "capitais): " + vd("superávit") + "."),
        "destrinchando": [
            "A expansão fiscal mexe no balanço de pagamentos por dois canais opostos: a " + vd("renda maior")
            + " eleva as importações e piora a conta corrente; o " + vd("juro maior") + " atrai capital e "
            "melhora a conta financeira. Qual prevalece depende da mobilidade de capital.",
            "Critério gráfico: compara-se a inclinação da BP com a da LM. " + azb("BP mais inclinada que a LM")
            + " (baixa mobilidade): o novo ponto IS × LM fica abaixo/à direita da BP → " + vd("déficit")
            + ". " + azb("BP menos inclinada que a LM") + " (alta mobilidade): o ponto fica acima/à esquerda "
            "→ " + vd("superávit") + ".",
            "Por que “temporário”? Porque o desequilíbrio desencadeia um ajuste. No câmbio fixo: déficit → "
            "venda de reservas → LM para a esquerda; superávit → compra de reservas → LM para a direita. No "
            "câmbio flutuante: déficit → depreciação; superávit → apreciação, com deslocamento de IS e BP.",
            "Por isso, no câmbio fixo, a eficácia da fiscal cresce com a mobilidade (o superávit expande a "
            "moeda), e no flutuante ela diminui com a mobilidade (o superávit aprecia o câmbio e reduz NX).",
        ],
        "grafico_verso": "ECO-E2-L01551-1-V1",
        "dissecando": (cz("[inversão]") + " Os dois casos existem, mas com os resultados trocados. A pergunta "
                       "certa é “qual efeito domina?”: pouca mobilidade → o capital mal reage ao juro, sobra o "
                       "efeito importações (déficit); muita mobilidade → o capital inunda o país (superávit)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…leva a um déficit temporário do BP se a curva BP for mais inclinada que a LM.”</i> → CERTO",
            "<i>“…com perfeita mobilidade de capitais, a política fiscal expansionista leva a um déficit "
            "temporário do BP.”</i> → ERRADO (com BP horizontal, surge superávit)",
        ])],
        "reescrita": ("Uma política fiscal expansionista leva a um " + hl("déficit") + " temporário do saldo do "
                      "balanço de pagamentos (BP), se houver baixa mobilidade de capital, e a um "
                      + hl("superávit") + " temporário do BP, se a mobilidade de capitais for alta."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["temporário"], "dificuldade": 2,
        "comentario_fonte": "Relação invertida: baixa mobilidade → déficit (importações); alta mobilidade → "
                            "superávit (entrada de capitais). Um comentário trata o caso de baixa mobilidade como "
                            "“ambíguo”.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 420", "monetária expansionista com câmbio fixo e mobilidade perfeita; não "
                                              "corresponde ao item")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01552
    {
        "id": "ECO-E2-L01552-1", "fonte_ref": "E2-L01552", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_C,
        "rotulo_item": "Item",
        "assertiva": ("Uma política monetária expansionista num regime de câmbio flexível e perfeita mobilidade de "
                      "capitais terá eficácia em expandir a demanda agregada, porém será ineficaz para expandir o "
                      "produto e reduzir o desemprego no longo prazo, se prevalecer a versão de Friedman da curva de "
                      "Phillips com expectativas adaptativas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma política monetária expansionista num regime de câmbio flexível e perfeita mobilidade de "
                      "capitais terá <u>eficácia em expandir a demanda agregada</u>, porém será <u>ineficaz</u> para "
                      "expandir o produto e reduzir o desemprego <u>no longo prazo</u>, se prevalecer a versão de "
                      "Friedman da curva de Phillips com expectativas adaptativas."),
        "poucas": ("Duas teorias encadeadas: no " + azb("Mundell-Fleming") + " (curto prazo, preços rígidos), a "
                   "monetária expande a demanda via juros e depreciação; na " + azb("curva de Phillips "
                   "aceleracionista") + " de " + oc("Friedman") + ", as expectativas se ajustam e o desemprego "
                   "volta à taxa natural no longo prazo."),
        "destrinchando": [
            "Curto prazo: M ↑ → LM para a direita → i ↓ → saída de capitais → " + vd("depreciação") + " → NX ↑ "
            "→ IS para a direita. Demanda agregada e produto sobem; o desemprego cai abaixo da taxa natural.",
            "Longo prazo: com desemprego abaixo da " + azb("taxa natural") + ", a inflação sobe. Com "
            + azb("expectativas adaptativas") + " (π<sup>e</sup> segue a inflação passada), trabalhadores e "
            "empresas incorporam a inflação maior aos contratos; a curva de Phillips de curto prazo se desloca "
            "para cima e o desemprego volta à taxa natural, com inflação mais alta.",
            "A curva de Phillips de " + vd("longo prazo é vertical") + " na taxa natural: a moeda é "
            + azb("neutra") + " no longo prazo. Manter o desemprego abaixo da taxa natural exigiria inflação "
            "sempre crescente — daí o nome “aceleracionista”. A crítica é de " + oc("Friedman") + " (1968) e "
            + oc("Phelps") + " (1967–1968).",
            "Contraste com " + oc("Lucas") + " e as " + azb("expectativas racionais") + ": se a política for "
            "antecipada, ela é ineficaz até no curto prazo (proposição da ineficácia de Sargent e Wallace). Com "
            "expectativas adaptativas, há efeito real <b>transitório</b>.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item junta duas teorias e só fica certo porque separa "
                       "os horizontes: eficácia no curto prazo (Mundell-Fleming) e neutralidade no longo "
                       "(Friedman). A pegadinha seria dizer “ineficaz também no curto prazo” com expectativas "
                       "adaptativas, o que só valeria com expectativas racionais e política antecipada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com expectativas adaptativas, a política monetária expansionista é ineficaz para reduzir o "
            "desemprego mesmo no curto prazo.”</i> → ERRADO (isso é com expectativas racionais e política "
            "antecipada)",
            "<i>“…na versão de Friedman, a curva de Phillips de longo prazo é vertical na taxa natural de "
            "desemprego.”</i> → CERTO",
        ]), ("📚 Autores e teses", [
            oc("Milton Friedman") + ", discurso presidencial à American Economic Association (dez./1967), "
            "publicado como “The Role of Monetary Policy” (1968): taxa natural de desemprego e trade-off apenas transitório.",
            oc("Robert Mundell") + " e " + oc("Marcus Fleming") + " (início dos anos 1960): eficácia das políticas "
            "conforme o regime cambial e a mobilidade de capital.",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["no longo prazo"], "dificuldade": 2,
        "comentario_fonte": "Monetária eficaz no curto prazo via depreciação; no longo prazo, com expectativas "
                            "adaptativas (Friedman), retorno à taxa natural com inflação maior (vários comentários "
                            "de IA convergentes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [corte("IMAGEM 420", "monetária com câmbio fixo; não corresponde ao item"),
                          corte("IMAGEM 421", "OA de longo prazo vertical × DA")],
        "alertas": ["texto_corrigido: “curva de Philips” corrigido para “curva de Phillips” na assertiva"],
    },
    # ------------------------------------------------------------------ E2-L01583
    {
        "id": "ECO-E2-L01583-1", "fonte_ref": "E2-L01583", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_D,
        "rotulo_item": "Item",
        "assertiva": ("Uma política fiscal expansionista num país com alta mobilidade de capitais e câmbio flexível "
                      "terá eficácia em expandir o produto, mas esta eficácia será reduzida pela redução das "
                      "exportações líquidas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma política fiscal expansionista num país com <u>alta</u> mobilidade de capitais e câmbio "
                      "flexível <u>terá eficácia</u> em expandir o produto, mas esta eficácia será <u>reduzida</u> "
                      "pela redução das exportações líquidas."),
        "poucas": ("Mobilidade " + azb("alta, porém imperfeita") + " (o contexto é de mobilidade imperfeita): a "
                   "expansão fiscal gera superávit no BP, o câmbio se aprecia e NX cai, mas a IS só recua "
                   + vd("em parte") + ". A fiscal é eficaz, com eficácia reduzida."),
        "destrinchando": [
            "Com mobilidade alta mas imperfeita, a " + azb("BP é crescente e menos inclinada que a LM") + ". A "
            "expansão fiscal (IS para a direita) leva a economia a um ponto acima da BP: o juro maior atrai mais "
            "capital do que as importações extras drenam → " + vd("superávit") + ".",
            "Com câmbio flexível, o superávit " + vd("aprecia") + " a moeda: NX cai, a IS recua e a BP se "
            "desloca para cima. Como a mobilidade não é perfeita, o juro doméstico pode ficar acima do externo "
            "no novo equilíbrio, e a renda final fica " + vd("acima da inicial") + ", embora abaixo do impacto.",
            "Gradação da eficácia da fiscal no câmbio flexível: " + vd("máxima") + " com mobilidade baixa (o "
            "déficit deprecia o câmbio e a reforça); " + vd("reduzida") + " com mobilidade alta (o superávit "
            "aprecia o câmbio); " + vd("nula") + " com mobilidade perfeita (crowding-out externo completo).",
            "Atenção: um dos comentários da fonte atribuía a perda de eficácia ao aumento das importações pela "
            "renda maior. O canal que <b>reduz</b> a eficácia aqui é a " + azb("apreciação cambial") + "; o "
            "efeito renda sobre as importações vale em qualquer economia aberta e já está embutido no "
            "multiplicador.",
        ],
        "grafico_verso": "ECO-E2-L01583-1-V1",
        "dissecando": (cz("[modulador relativo · detalhe]") + " A palavra decisiva é “alta”, não “perfeita”: no "
                       "comando, a mobilidade é imperfeita. Quem aplica direto a tabela do Mundell-Fleming "
                       "(fiscal ineficaz no flutuante) marca ERRADO. 🔥 O professor cobra a gradação "
                       "nula/reduzida/ampliada conforme a mobilidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…num país com perfeita mobilidade de capitais e câmbio flexível, terá eficácia reduzida, mas "
            "positiva, em expandir o produto.”</i> → ERRADO (com mobilidade perfeita, a eficácia é nula)",
            "<i>“…com baixa mobilidade de capitais e câmbio flexível, terá eficácia ampliada pela depreciação "
            "cambial.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["alta"], "dificuldade": 2,
        "comentario_fonte": "Fiscal com alta mobilidade e câmbio flexível: IS para a direita, juros sobem, entra "
                            "capital, moeda aprecia, NX caem e a IS volta parcialmente; eficácia reduzida (um "
                            "comentário atribuía a redução ao déficit comercial causado pela renda maior).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [redes("IMAGEM 438", "ECO-E2-L01583-1-V1", "fiscal com câmbio flexível e alta "
                                                                   "mobilidade")],
        "alertas": ["qualidade_fonte: o primeiro comentário atribuía a perda de eficácia ao déficit comercial pela "
                    "renda maior; o canal relevante é a apreciação cambial"],
    },
    # ------------------------------------------------------------------ E2-L01584
    {
        "id": "ECO-E2-L01584-1", "fonte_ref": "E2-L01584", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_D,
        "rotulo_item": "Item",
        "assertiva": ("A redução dos juros pelo Banco Central numa situação de alta mobilidade de capitais e câmbio "
                      "flexível, terá eficácia em elevar a renda, mas esta eficácia será reduzida pela apreciação "
                      "cambial resultante."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A redução dos juros pelo Banco Central numa situação de alta mobilidade de capitais e câmbio "
                       "flexível, terá eficácia em elevar a renda, ") + vm("mas") + az(" esta eficácia será ")
                    + vm("reduzida") + az(" pela ") + vm("apreciação") + az(" cambial resultante.")),
        "poucas": ("Juro menor provoca " + vm("saída") + " de capitais e " + vm("depreciação") + ", não "
                   "apreciação; a depreciação eleva NX e " + azb("amplia") + " a eficácia da política monetária."),
        "destrinchando": [
            "Corte de juros (LM para a direita) → i abaixo do externo → saída de capitais → déficit no BP → "
            "com câmbio flexível, " + vd("depreciação") + " → exportações sobem, importações caem → NX ↑ → IS "
            "para a direita.",
            "Os dois canais se somam: o doméstico (juro ↓ → investimento ↑) e o externo (câmbio ↑ → NX ↑). Por "
            "isso a monetária é " + azb("mais eficaz") + " no câmbio flexível do que numa economia fechada, e "
            "tanto mais quanto maior a mobilidade de capital.",
            "A apreciação cambial que o item menciona é o que acontece com a " + azb("política fiscal "
            "expansionista") + " no mesmo regime (juro ↑ → entrada de capitais). O item transplantou o "
            "mecanismo da fiscal para a monetária.",
            "Exemplo ⏳ (out/2026): o ciclo de cortes da Selic em 2020, até " + vd("2% a.a.") + ", veio "
            "acompanhado de forte depreciação do real — coerente com o canal descrito, somado ao aumento do "
            "risco fiscal.",
            vm("Regra-âncora: no câmbio flexível, juro ↓ → depreciação → NX ↑ (reforça); gasto ↑ → apreciação → "
               "NX ↓ (enfraquece)."),
        ],
        "grafico_verso": "ECO-E2-L01584-1-V1",
        "dissecando": (cz("[inversão · troca de conceito]") + " A primeira parte (eficácia em elevar a renda) "
                       "está certa; o erro inverte o sentido do câmbio e, com isso, o efeito sobre a eficácia. "
                       "Pista: juro menor nunca atrai capital. 🔥 É o par exato do item sobre a fiscal "
                       "(“eficácia reduzida pela redução das exportações líquidas”), que é CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…terá eficácia em elevar a renda, ampliada pela depreciação cambial resultante.”</i> → CERTO",
            "<i>“A redução dos juros numa situação de alta mobilidade de capitais e câmbio fixo terá eficácia "
            "ampliada pela depreciação cambial.”</i> → ERRADO (no fixo não há depreciação e a monetária é "
            "ineficaz)",
        ])],
        "reescrita": ("A redução dos juros pelo Banco Central numa situação de alta mobilidade de capitais e câmbio "
                      "flexível, terá eficácia em elevar a renda, " + hl("e") + " esta eficácia será "
                      + hl("ampliada") + " pela " + hl("depreciação") + " cambial resultante."),
        "tipo_erro": ["INVERSAO", "TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Redução dos juros causa saída de capitais e depreciação, que amplia a eficácia; o erro "
                            "está em “reduzida pela apreciação cambial” (um comentário de IA chegou a validar a "
                            "parte da apreciação antes de se corrigir).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [redes("IMAGEM 439", "ECO-E2-L01584-1-V1", "monetária com câmbio flexível")],
        "alertas": ["quase_duplicata: ECO-E2-L01445-1"],
    },
    # ------------------------------------------------------------------ E2-L01585
    {
        "id": "ECO-E2-L01585-1", "fonte_ref": "E2-L01585", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_D,
        "rotulo_item": "Item",
        "assertiva": ("Caso haja baixa mobilidade de capitais e câmbio flexível, a política fiscal será eficaz em "
                      "expandir a renda e terá eficácia ampliada pela depreciação cambial resultante que elevará as "
                      "exportações líquidas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Caso haja <u>baixa</u> mobilidade de capitais e câmbio flexível, a política fiscal será "
                      "eficaz em expandir a renda e terá eficácia <u>ampliada</u> pela <u>depreciação</u> cambial "
                      "resultante que elevará as exportações líquidas."),
        "poucas": ("Com " + azb("baixa mobilidade") + ", o efeito renda (mais importações) supera o efeito juros "
                   "(pouco capital entra): surge " + vd("déficit") + " no BP, o câmbio se deprecia, NX sobe e a IS "
                   "avança ainda mais."),
        "destrinchando": [
            "Baixa mobilidade = " + azb("BP mais inclinada que a LM") + ". A expansão fiscal leva a economia a um "
            "ponto abaixo/à direita da BP: déficit, porque a entrada de capital atraída pelo juro maior não "
            "cobre o aumento das importações.",
            "No câmbio flexível, o déficit " + vd("deprecia") + " a moeda: exportações sobem, importações caem, "
            "NX ↑. A IS se desloca outra vez para a direita (e a BP também), e o novo equilíbrio tem " + vd("renda "
            "maior") + " do que o ponto de impacto.",
            "Contraste: com mobilidade alta, o resultado inverte-se (superávit → apreciação → eficácia "
            "reduzida); com mobilidade perfeita, a eficácia é nula. No câmbio flexível, a fiscal é tanto mais "
            "eficaz quanto <b>menor</b> a mobilidade — o oposto do câmbio fixo.",
            "Leitura prática: em economias com controles de capital e câmbio flutuante, estímulos fiscais tendem "
            "a vir acompanhados de desvalorização e de melhora das exportações, e não de apreciação.",
            vm("Regra-âncora (câmbio flexível): mobilidade baixa → fiscal ampliada; alta → reduzida; perfeita → "
               "nula."),
        ],
        "grafico_verso": "ECO-E2-L01585-1-V1",
        "dissecando": (cz("[contraintuitivo · detalhe]") + " Quem memorizou “fiscal é ineficaz no câmbio flexível” "
                       "erra: a tabela vale para mobilidade <b>perfeita</b>. O gatilho é “baixa mobilidade”, que "
                       "inverte o sinal do desequilíbrio do BP (déficit) e, com ele, o sentido do câmbio "
                       "(depreciação)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Caso haja alta mobilidade de capitais e câmbio flexível, a política fiscal terá eficácia "
            "ampliada pela depreciação cambial.”</i> → ERRADO (com alta mobilidade há apreciação)",
            "<i>“Caso haja baixa mobilidade de capitais e câmbio fixo, a política fiscal expansionista provocará "
            "perda de reservas.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "DETALHE"], "moduladores": ["baixa"], "dificuldade": 2,
        "comentario_fonte": "Com baixa mobilidade (BP mais inclinada que a LM), o efeito renda domina, surge déficit "
                            "no BP, o câmbio deprecia, NX sobe e a IS se desloca ainda mais (vários comentários de "
                            "IA convergentes).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [redes("IMAGEM 440", "ECO-E2-L01585-1-V1", "fiscal com câmbio flexível e baixa "
                                                                   "mobilidade")],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01586
    {
        "id": "ECO-E2-L01586-1", "fonte_ref": "E2-L01586", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_D,
        "rotulo_item": "Item",
        "assertiva": ("Mesmo com câmbio sendo fixo, a política monetária terá eficácia em expandir a renda se a "
                      "mobilidade de capital for baixa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (vm("Mesmo com") + az(" câmbio sendo fixo, a política monetária ") + vm("terá eficácia")
                    + az(" em expandir a renda se a mobilidade de capital for baixa.")),
        "poucas": ("No câmbio fixo, a monetária é " + vm("ineficaz") + " em qualquer grau de mobilidade: a "
                   "expansão gera déficit no BP, o BC vende reservas e a " + azb("LM é endógena") + " — volta ao "
                   "ponto de partida. A baixa mobilidade só torna o ajuste mais lento."),
        "destrinchando": [
            "Expansão monetária (LM para a direita): o juro cai e a renda sobe. Os dois movimentos pioram o "
            "balanço de pagamentos — a renda maior eleva importações; o juro menor, mesmo com pouca mobilidade, "
            "reduz a entrada de capital.",
            "Para manter a paridade, o BC " + vd("vende reservas") + " e retira moeda de circulação; a LM volta "
            "até a interseção original de IS e BP, que não se moveram. Resultado: " + vd("Y e i iguais") + ", "
            "reservas menores.",
            "O papel da mobilidade é a <b>velocidade</b>: com mobilidade alta, a perda de reservas é imediata "
            "(fluxos financeiros); com mobilidade baixa, vem aos poucos, pela balança comercial. Um BC com "
            "muitas reservas, ou que " + azb("esterilize") + " as perdas, sustenta algum efeito por um tempo — "
            "daí a impressão de “eficácia de curto prazo” —, mas no equilíbrio do modelo a política não move "
            "a renda.",
            "Isso não contradiz o trilema: o trilema diz que, com câmbio fixo, só há autonomia monetária com "
            "<b>controle total</b> dos capitais e sem restrição de reservas; no IS-LM-BP, mesmo sem fluxo "
            "financeiro algum, o déficit comercial já basta para desfazer a expansão.",
            vm("Regra-âncora: câmbio fixo → oferta de moeda endógena → política monetária ineficaz, qualquer que "
               "seja a mobilidade."),
        ],
        "dissecando": (cz("[restrição indevida · nexo indevido]") + " O item sugere que a ineficácia da monetária "
                       "no câmbio fixo é problema só de mobilidade alta e abre uma exceção (“mesmo com… se… "
                       "baixa”). A exceção não existe no modelo. Vários comentários de IA caíram na armadilha e "
                       "julgaram CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Mesmo com baixa mobilidade de capital, sob câmbio fixo a política monetária expansionista "
            "provocará perda de reservas e não alterará a renda de equilíbrio.”</i> → CERTO",
            "<i>“Com câmbio flexível, a política monetária terá eficácia em expandir a renda se a mobilidade "
            "de capital for baixa.”</i> → CERTO",
        ])],
        "reescrita": (hl("Com") + " câmbio sendo fixo, a política monetária " + hl("não terá eficácia") + " em "
                      "expandir a renda" + " se a mobilidade de capital for baixa" + hl(" (nem se for alta)") + "."),
        "tipo_erro": ["RESTRICAO", "NEXO_INDEVIDO"], "moduladores": ["mesmo", "se"], "dificuldade": 2,
        "comentario_fonte": "Câmbio fixo: perde-se o controle da política monetária; com baixa mobilidade, pode haver "
                            "alguma eficácia no começo, mas ela desaparece. Gabarito E; dois comentários de IA "
                            "julgaram a assertiva correta.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [corte("IMAGEM 441", "monetária com câmbio fixo e baixa mobilidade: LM endógena")],
        "alertas": ["qualidade_fonte: dois comentários de IA do verso julgavam a assertiva correta; descartados por "
                    "contrariarem o gabarito e o modelo",
                    "quase_duplicata: ECO-E2-L01487-1"],
    },
    # ------------------------------------------------------------------ E2-L01628
    {
        "id": "ECO-E2-L01628-1", "fonte_ref": "E2-L01628", "destino": "70", "subtema": H2["flut"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_B,
        "rotulo_item": "Item",
        "assertiva": ("Num regime de câmbio flexível e perfeita mobilidade de capitais, a política fiscal "
                      "contracionista não terá efeito sobre o produto, mas levará a um aumento do saldo "
                      "comercial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Num regime de câmbio flexível e perfeita mobilidade de capitais, a política fiscal "
                      "<u>contracionista</u> não terá efeito sobre o produto, mas levará a um <u>aumento</u> do saldo "
                      "comercial."),
        "poucas": ("Espelho da expansão: a contração fiscal reduz o juro, provoca saída de capitais, "
                   + vd("deprecia") + " o câmbio e eleva NX exatamente o que G caiu. Produto igual, saldo "
                   "comercial maior."),
        "destrinchando": [
            "Contração fiscal → IS para a esquerda → juro tende a cair abaixo de i* → saída de capitais → "
            + vd("depreciação") + " → NX ↑ → IS volta à posição original.",
            "Como a LM não se moveu e o juro final é i*, a renda final é a inicial: " + vd("ΔY = 0") + ". A "
            "composição muda: " + vd("ΔNX = −ΔG") + " (ou o equivalente com impostos). O saldo comercial sobe.",
            "Atenção ao mecanismo: um dos comentários da fonte atribuía a melhora comercial à queda das "
            "importações por menor renda. Mas a renda não cai no equilíbrio final; o saldo melhora pela "
            + azb("depreciação cambial") + ".",
            "Aplicação: ajustes fiscais em países com câmbio flutuante e conta de capital aberta tendem a ter "
            "custo recessivo menor do que no câmbio fixo, porque a depreciação compensa a queda da demanda "
            "interna — argumento usado em debates sobre consolidação fiscal.",
            REGRA_MF,
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " Versão “ao contrário” do caso clássico: a "
                       "banca troca expansão por contração para testar se o candidato entendeu o mecanismo, e "
                       "não só decorou a frase. Pista: no flutuante com mobilidade perfeita, nenhum choque "
                       "fiscal move a renda; muda só o câmbio e o saldo comercial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a política fiscal contracionista não terá efeito sobre o produto, mas levará a uma redução do "
            "saldo comercial.”</i> → ERRADO (inversão: a depreciação eleva o saldo)",
            "<i>“Num regime de câmbio fixo e perfeita mobilidade de capitais, a política fiscal contracionista "
            "reduzirá o produto.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Contração fiscal: IS para a esquerda, juros caem, saída de capital, depreciação, NX ↑, "
                            "IS volta; produto inalterado e saldo comercial maior (um comentário atribuía a melhora "
                            "à menor demanda por importações).",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [corte("IMAGEM 468", "IS-LM-BP com BP horizontal em i*")],
        "alertas": ["quase_duplicata: ECO-E2-L01550-1",
                    "qualidade_fonte: um comentário atribuía a melhora do saldo à queda das importações por menor "
                    "renda; no equilíbrio final a renda não cai e o canal é a depreciação"],
    },
    # ------------------------------------------------------------------ E2-L01630
    {
        "id": "ECO-E2-L01630-1", "fonte_ref": "E2-L01630", "destino": "70", "subtema": H2["fixo"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_B,
        "rotulo_item": "Item",
        "assertiva": ("Numa economia com perfeita mobilidade de capital e câmbio fixo, uma política monetária "
                      "contracionista levará à redução do produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Numa economia com perfeita mobilidade de capital e câmbio fixo, uma política monetária "
                       "contracionista ") + vm("levará à redução do") + az(" produto.")),
        "poucas": ("Câmbio fixo + mobilidade perfeita: a contração eleva o juro, atrai capital, e o BC precisa "
                   + vd("comprar divisas") + " emitindo moeda — a contração se desfaz. " + vm("O produto não "
                   "muda") + "; as reservas sobem."),
        "destrinchando": [
            "Venda de títulos (ou redução de M) → LM para a esquerda → juro acima de i* → entrada maciça de "
            "capitais → pressão de " + azb("apreciação") + ".",
            "Para manter a paridade, o BC compra moeda estrangeira e paga com moeda doméstica: a base monetária "
            "volta a crescer e a LM retorna. Equilíbrio final: " + vd("Y e i iguais aos iniciais") + ", "
            + vd("reservas ↑") + ".",
            "O BC não controla a quantidade de moeda: ela é " + azb("endógena") + ", determinada pela "
            "necessidade de manter i = i*. Tentar esterilizar a compra de divisas (vendendo títulos de novo) "
            "só realimenta a entrada de capitais, com custo fiscal crescente (o BC paga i e recebe i* nas "
            "reservas).",
            "É o mesmo resultado da expansão monetária, com sinais trocados: em qualquer direção, a política "
            "monetária é ineficaz neste regime; a fiscal é que tem eficácia máxima.",
            REGRA_MF,
        ],
        "dissecando": (cz("[nexo indevido]") + " O item aplica o raciocínio da economia fechada (juro ↑ → "
                       "investimento ↓ → produto ↓), que vale apenas no instante inicial. Pista: “câmbio fixo” "
                       "+ “perfeita mobilidade” é a combinação em que a monetária sempre perde."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…uma política monetária contracionista elevará as reservas internacionais sem alterar o "
            "produto.”</i> → CERTO",
            "<i>“Numa economia com perfeita mobilidade de capital e câmbio flutuante, uma política monetária "
            "contracionista levará à redução do produto.”</i> → CERTO",
        ])],
        "reescrita": ("Numa economia com perfeita mobilidade de capital e câmbio fixo, uma política monetária "
                      "contracionista " + hl("não alterará o") + " produto" + hl(", apenas elevará as "
                                                                                "reservas") + "."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Com câmbio fixo e mobilidade perfeita, a política monetária é ineficaz: a contração "
                            "atrai capital, o BC compra divisas e expande a base, anulando a contração; o produto "
                            "não se altera.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00905-1, ECO-E2-L01486-1"],
    },
]
