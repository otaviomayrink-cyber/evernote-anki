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
                       "aumento da renda real ") + vm("e da taxa de juros") + az(" de equilíbrio.")),
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
                      "aumento da renda real" + hl(", mas mantém inalterada a taxa de juros") + " de equilíbrio"
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
                       "uma expansionista não impactam o nível de equilíbrio da renda real da economia ")
                    + vm("e nem o montante de reservas do BACEN") + az(".")),
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
                       "contracionista resultaria no ") + vm("aumento") + az(" do volume de exportações "
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
                      "contracionista resultaria na " + hl("redução") + " do volume de exportações líquidas."),
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
