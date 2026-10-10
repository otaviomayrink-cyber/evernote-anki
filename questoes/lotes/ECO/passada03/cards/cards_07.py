"""Cards do lote de redação 07 — ECO, passada 03 (nota 66: câmbio e política cambial)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "reg": "💱 Regimes cambiais",
    "ppc": "📏 Câmbio nominal × real e PPC",
    "det": "📈 Determinantes do câmbio",
}

CMD_BZ_INTERV = ("Sobre o equilíbrio de mercado e as intervenções no mercado cambial, julgue a assertiva a "
                 "seguir.")
CMD_BZ_AGENTES = ("Considere o funcionamento do mercado cambial e a interação de seus principais agentes. Julgue a "
                  "assertiva a seguir como certa ou errada.")
CMD_BZ_REGIMES = "Considerando os diversos regimes cambiais e intervenções, julgue a assertiva a seguir."
CMD_BZ_ISLMBP = ("Considerando o modelo IS-LM-BP e as inter-relações entre os mercados de bens, monetário e "
                 "cambial, julgue a assertiva a seguir.")
CMD_BZ_PPC = ("Sobre a paridade do poder de compra internacional (PPC), julgue a assertiva a seguir como certa ou "
              "errada.")
CMD_BZ_DIN = ("Julgue a assertiva a seguir, sobre a dinâmica dos mercados de bens, monetário e cambial no contexto "
              "de economias internacionais.")
CMD_NAB_SMI = "Acerca de macroeconomia aberta e sistema monetário internacional, julgue (C ou E) o item a seguir."
CMD_NAB_MA = "Em relação à macroeconomia aberta, julgue (C ou E) o item a seguir."
CMD_NAB_EI = "Em relação à economia internacional, julgue (C ou E) o item a seguir."
CMD_NAB_PC = ("A respeito dos instrumentos de política comercial e dos regimes cambiais, julgue (C ou E) o item a "
              "seguir.")

CARDS = []

CARDS += [
    # ------------------------------------------------------------------ E1-0887
    {
        "id": "ECO-E1-0887-1", "fonte_ref": "E1-0887", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": "Acerca da escolha do regime cambial, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Na presença de uma crise interna com deterioração fiscal a inexistência de reservas cambiais "
                      "sinaliza a conveniência de se adotar o regime de câmbio fixo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Na presença de uma crise interna com deterioração fiscal a inexistência de reservas "
                       "cambiais sinaliza a ") + vm("conveniência") + az(" de se adotar o regime de câmbio fixo.")),
        "poucas": ("Câmbio fixo se sustenta com " + azb("reservas") + ": é com elas que o Banco Central compra a "
                   "própria moeda quando há fuga de divisas. Sem reservas e com crise fiscal, fixar o câmbio é "
                   "convidar um " + azb("ataque especulativo") + "."),
        "destrinchando": [
            "No " + azb("câmbio fixo") + ", o Banco Central se compromete a comprar e vender divisas à paridade "
            "anunciada. Quando há pressão de desvalorização (saída de capitais, déficit externo), ele precisa "
            + vd("vender reservas") + " e recolher moeda doméstica. Sem estoque de reservas, a promessa não tem "
            "como ser cumprida.",
            "A crise fiscal agrava o quadro: o mercado antecipa que o governo acabará financiando o déficit com "
            "emissão de moeda, o que é incompatível com a paridade. É a lógica dos " + azb("modelos de crise "
            "cambial de primeira geração") + " (" + oc("Krugman") + ", 1979): fundamentos fiscais frouxos + "
            "reservas finitas → ataque especulativo e colapso da âncora.",
            "Nessa situação, o regime mais prudente é o " + azb("flutuante") + ": o câmbio absorve o choque, o "
            "Banco Central não queima reservas que não tem e preserva-se a política monetária para conter o "
            "repasse inflacionário.",
            rx("Brasil") + ": a crise de " + vd("janeiro de 1999") + " — déficit fiscal elevado, perda acelerada "
            "de reservas após as crises asiática e russa — levou ao abandono das bandas cambiais e à adoção do "
            "câmbio flutuante, depois combinado com metas de inflação e metas de superávit primário.",
            vm("Regra-âncora: câmbio fixo exige reservas e disciplina fiscal; sem elas, o regime não para em pé."),
        ],
        "dissecando": (cz("[inversão]") + " O item inverte a conclusão: as duas premissas (crise fiscal e falta "
                       "de reservas) são exatamente as que <b>desaconselham</b> o câmbio fixo. Pista: “inexistência "
                       "de reservas” combinada com regime que vive de intervenção."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A manutenção de um regime de câmbio fixo requer volume de reservas internacionais suficiente para "
            "defender a paridade.”</i> → CERTO",
            "<i>“Em regime de câmbio flutuante, a acumulação de reservas é condição necessária para que a taxa de "
            "câmbio se equilibre.”</i> → ERRADO (troca de regime: quem depende de reservas é o fixo)",
        ])],
        "reescrita": ("Na presença de uma crise interna com deterioração fiscal a inexistência de reservas cambiais "
                      "sinaliza a " + hl("inconveniência") + " de se adotar o regime de câmbio fixo."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A ausência de reservas torna inviável sustentar um câmbio fixo, pois o governo não "
                            "terá como intervir no mercado de câmbio para manter a paridade.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0907
    {
        "id": "ECO-E1-0907-1", "fonte_ref": "E1-0907", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2010, "cacd": False,
        "errei": False,
        "comando": "Acerca da teoria da paridade do poder de compra, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Consoante a teoria da paridade do poder de compra, país cuja taxa de inflação é mais elevada "
                      "que a que prevalece nas demais nações enfrenta pressões para apreciar a moeda nacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Consoante a teoria da paridade do poder de compra, país cuja taxa de inflação é mais "
                       "elevada que a que prevalece nas demais nações enfrenta pressões para ") + vm("apreciar")
                    + az(" a moeda nacional.")),
        "poucas": ("Pela " + azb("PPC relativa") + ", a moeda do país com inflação mais alta tende a se "
                   + vd("depreciar") + " na medida do diferencial de inflação: %ΔE ≈ π − π*."),
        "destrinchando": [
            azb("Paridade do poder de compra") + " (PPC): no longo prazo, o câmbio nominal se ajusta para que uma "
            "mesma cesta custe o mesmo nos dois países, quando expressa na mesma moeda. Versão absoluta: "
            + vd("E = P / P*") + ". Versão relativa: " + vd("%ΔE ≈ π − π*") + " (E = preço da moeda estrangeira "
            "em moeda nacional).",
            "Intuição: se os preços internos sobem mais que os externos e o câmbio não se mexe, os bens nacionais "
            "ficam caros lá fora (exportações caem) e os importados ficam baratos aqui (importações sobem). A "
            "demanda por divisas aumenta e a oferta diminui: o preço da divisa sobe, isto é, a moeda nacional "
            + vd("deprecia") + ".",
            "Exemplo: inflação interna de 10% e externa de 2% → a PPC prevê depreciação nominal de cerca de "
            + vd("8%") + ", o que mantém constante o câmbio real (q = E·P*/P).",
            "Se, ao contrário, a moeda se apreciasse, o país perderia competitividade duas vezes (preços maiores e "
            "câmbio mais forte): é a " + azb("apreciação real") + " típica de planos de estabilização com âncora "
            "cambial, que a PPC prevê não ser sustentável no longo prazo.",
            vm("Regra-âncora: mais inflação → moeda mais fraca (depreciação), na proporção do diferencial."),
        ],
        "dissecando": (cz("[inversão]") + " Troca o sentido do ajuste: “apreciar” no lugar de “depreciar”. O "
                       "resto do item é a premissa correta da PPC relativa, o que dá credibilidade à frase. "
                       "Teste rápido: inflação maior = moeda que compra menos = moeda mais fraca."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a PPC relativa, a depreciação nominal da moeda de um país tende a igualar o excesso de sua "
            "inflação sobre a inflação externa.”</i> → CERTO",
            "<i>“Segundo a PPC, a moeda do país de inflação mais alta se deprecia em termos reais.”</i> → ERRADO "
            "(sob PPC, o câmbio real fica constante; a depreciação é nominal)",
        ])],
        "reescrita": ("Consoante a teoria da paridade do poder de compra, país cuja taxa de inflação é mais elevada "
                      "que a que prevalece nas demais nações enfrenta pressões para " + hl("depreciar")
                      + " a moeda nacional."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Inflação eleva o custo de vida e a demanda por bens comercializáveis do exterior; "
                            "nada sugere valorização; a PPC apenas pondera indicadores pelo custo de vida.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem reduz a PPC a um “ponderador” de indicadores de custo "
                    "de vida e não diz que a moeda se deprecia; corrigido no 📖"],
    },
    # ------------------------------------------------------------------ E1-0945
    {
        "id": "ECO-E1-0945-1", "fonte_ref": "E1-0945", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2011, "cacd": False,
        "errei": False,
        "comando": "Acerca da determinação da taxa de câmbio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a teoria cambial básica, com taxas flutuantes e mercado similar ao de "
                      "concorrência perfeita, os déficits no balanço de pagamentos provocariam apreciação real da "
                      "taxa de câmbio, e os superávits, depreciação, o que conduziria ao equilíbrio do balanço de "
                      "pagamentos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("De acordo com a teoria cambial básica, com taxas flutuantes e mercado similar ao de "
                       "concorrência perfeita, os déficits no balanço de pagamentos provocariam ")
                    + vm("apreciação") + az(" real da taxa de câmbio, e os superávits, ") + vm("depreciação")
                    + az(", o que conduziria ao equilíbrio do balanço de pagamentos.")),
        "poucas": ("Déficit externo = " + azb("excesso de demanda por divisas") + ": com câmbio flutuante, o preço "
                   "da divisa sobe e a moeda nacional se " + vd("deprecia") + ". O superávit faz o inverso. Os "
                   "sentidos estão trocados."),
        "destrinchando": [
            "No mercado de câmbio, quem " + azb("demanda divisas") + " são importadores, quem remete renda e quem "
            "aplica no exterior; quem " + azb("oferta") + " são exportadores e investidores estrangeiros que "
            "trazem recursos. Um déficit no balanço de pagamentos significa que a demanda por divisas supera a "
            "oferta ao câmbio vigente.",
            "Com câmbio " + azb("flutuante") + ", o excesso de demanda eleva o preço da divisa: E (R$/US$) sobe = "
            + vd("depreciação") + " da moeda nacional. Com preços internos e externos dados no curto prazo, a "
            "depreciação nominal é também " + vd("real") + " (q = E·P*/P sobe).",
            "O mecanismo autocorretivo é justamente esse: a depreciação barateia as exportações e encarece as "
            "importações, o saldo melhora e o déficit se fecha (se valer a condição de " + oc("Marshall-Lerner")
            + "). No superávit, a apreciação faz o caminho inverso.",
            "Se os déficits provocassem apreciação, o desequilíbrio se <b>agravaria</b> — o item afirma o "
            "contrário do ajuste e, mesmo assim, conclui pelo equilíbrio, o que é incoerente.",
            vm("Regra-âncora: câmbio flutuante — déficit externo deprecia; superávit aprecia."),
        ],
        "dissecando": (cz("[inversão]") + " Inversão dupla e simétrica (déficit ↔ superávit, apreciação ↔ "
                       "depreciação), preservando a conclusão verdadeira (“conduziria ao equilíbrio”). Pista: o "
                       "ajuste só leva ao equilíbrio se a moeda enfraquece quando falta divisa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com câmbio flutuante, um superávit no balanço de pagamentos tende a apreciar a moeda "
            "nacional.”</i> → CERTO",
            "<i>“Com câmbio fixo, o déficit no balanço de pagamentos é corrigido pela depreciação da moeda.”</i> → "
            "ERRADO (troca de regime: no fixo, o déficit consome reservas)",
        ])],
        "reescrita": ("De acordo com a teoria cambial básica, com taxas flutuantes e mercado similar ao de "
                      "concorrência perfeita, os déficits no balanço de pagamentos provocariam " + hl("depreciação")
                      + " real da taxa de câmbio, e os superávits, " + hl("apreciação") + ", o que conduziria ao "
                      "equilíbrio do balanço de pagamentos."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O déficit comercial tende a elevar a taxa de câmbio nominal e, com preços constantes, "
                            "a real; no superávit ocorre o inverso.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00103
    {
        "id": "ECO-E2-L00103-1", "fonte_ref": "E2-L00103", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_INTERV,
        "rotulo_item": "Item",
        "assertiva": ("No mercado cambial, tomando como referência a cotação cambial do “incerto”, quando há uma "
                      "queda na taxa de câmbio, significa que a moeda nacional se desvalorizou em relação ao dólar, "
                      "pois a distância entre os valores das moedas aumentou, refletindo uma moeda nacional menos "
                      "valorizada."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No mercado cambial, tomando como referência a cotação cambial do “incerto”, quando há uma "
                       "queda na taxa de câmbio, significa que a moeda nacional se ") + vm("desvalorizou")
                    + az(" em relação ao dólar, pois a distância entre os valores das moedas ") + vm("aumentou")
                    + az(", refletindo uma moeda nacional ") + vm("menos") + az(" valorizada.")),
        "poucas": ("Na cotação do " + azb("incerto") + " (R$ por US$), a taxa cai quando são necessários "
                   + vd("menos reais") + " por dólar: a moeda nacional se " + vd("valorizou") + "."),
        "destrinchando": [
            "Há duas formas de cotar: " + azb("cotação do incerto") + " (direta) — preço de 1 unidade de moeda "
            "estrangeira em moeda nacional (ex.: " + vd("R$ 5,40/US$") + "); a moeda nacional é a parte “incerta”, "
            "que varia. " + azb("Cotação do certo") + " (indireta) — quantas unidades de moeda estrangeira compra "
            "1 unidade nacional (US$ 0,185/R$). O " + rx("Brasil") + " usa a do incerto.",
            "Na cotação do incerto: E ↓ (de 5,40 para 5,00) → cada dólar custa menos reais → "
            + vd("apreciação/valorização") + " do real. E ↑ → " + vd("depreciação/desvalorização") + ". Na "
            "cotação do certo, a leitura se inverte — por isso o item faz questão de fixar a convenção.",
            "A metáfora da “distância” usada em aula: quanto mais perto de 1 está a cotação R$/US$, menor a "
            "distância entre as moedas e mais valorizado o real. Uma queda da taxa <b>reduz</b> essa distância.",
            "Vocabulário: “desvalorização” e “valorização” são usadas em regime fixo (decisão oficial); "
            "“depreciação” e “apreciação”, em regime flutuante (mercado). Em prova, costumam ser tratadas como "
            "sinônimos.",
            vm("Regra-âncora: cotação do incerto — taxa sobe, real desvaloriza; taxa cai, real valoriza."),
        ],
        "dissecando": (cz("[inversão]") + " O item fixa corretamente a convenção (“incerto”) e a queda da taxa, e "
                       "inverte todas as consequências de forma coerente entre si (desvalorizou, distância "
                       "aumentou, menos valorizada). A coerência interna é a isca; o teste é perguntar: caiu o "
                       "número de reais por dólar? Então o real ficou mais forte."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na cotação do certo, uma queda na taxa de câmbio indica desvalorização da moeda "
            "nacional.”</i> → CERTO",
            "<i>“Na cotação do incerto, uma alta da taxa de câmbio indica valorização da moeda nacional.”</i> → "
            "ERRADO (inversão: alta = desvalorização)",
        ])],
        "reescrita": ("No mercado cambial, tomando como referência a cotação cambial do “incerto”, quando há uma "
                      "queda na taxa de câmbio, significa que a moeda nacional se " + hl("valorizou") + " em "
                      "relação ao dólar, pois a distância entre os valores das moedas " + hl("diminuiu")
                      + ", refletindo uma moeda nacional " + hl("mais") + " valorizada."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Queda na taxa de câmbio indica valorização da moeda nacional: o real se aproxima do "
                            "valor do dólar.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00118-1 (mesma convenção: alta da taxa = desvalorização)"],
    },
    # ------------------------------------------------------------------ E2-L00105
    {
        "id": "ECO-E2-L00105-1", "fonte_ref": "E2-L00105", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_INTERV,
        "rotulo_item": "Item",
        "assertiva": ("O mecanismo das bandas cambiais permite que o valor do câmbio flutue livremente até certo "
                      "ponto, dentro de limites superiores e inferiores estabelecidos. Apenas quando o câmbio "
                      "ultrapassa esses limites, o Banco Central intervém, ajustando a quantidade de moeda "
                      "estrangeira para trazer o câmbio de volta aos limites aceitáveis."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O mecanismo das bandas cambiais permite que o valor do câmbio <u>flutue livremente até "
                      "certo ponto</u>, dentro de limites superiores e inferiores estabelecidos. <u>Apenas</u> "
                      "quando o câmbio ultrapassa esses limites, o Banco Central intervém, ajustando a quantidade "
                      "de moeda estrangeira para trazer o câmbio de volta aos limites aceitáveis."),
        "poucas": ("É a definição de " + azb("banda cambial") + ": flutuação de mercado entre um piso e um teto, "
                   "com o Banco Central comprando ou vendendo divisas só quando o câmbio chega aos limites."),
        "destrinchando": [
            "A " + azb("banda cambial") + " é um regime intermediário: combina a flexibilidade do flutuante "
            "(dentro da faixa) com a âncora do fixo (nos limites). O Banco Central anuncia um " + vd("piso")
            + " e um " + vd("teto") + " para a taxa de câmbio.",
            "Mecânica: câmbio encostando no teto (moeda nacional fraca) → o BC " + vd("vende divisas") + ", "
            "aumentando a oferta de dólares e puxando E para baixo; câmbio no piso (moeda forte) → o BC "
            + vd("compra divisas") + " e acumula reservas.",
            "Variantes: bandas " + azb("horizontais") + " (limites fixos) e bandas " + azb("deslizantes/"
            "inclinadas") + " (crawling bands: os limites são reajustados periodicamente, em geral pelo "
            "diferencial de inflação). Bandas largas aproximam-se do flutuante; estreitas, do fixo.",
            rx("Brasil") + ": entre " + vd("1995 e 1999") + " vigorou um sistema de bandas (com minibandas, ou "
            "“intrabandas”, em que o BC também atuava dentro da faixa), abandonado na crise de janeiro de 1999.",
            "Nuance: na prática, muitos bancos centrais fazem também intervenções “intramarginais”, antes de o "
            "câmbio tocar o limite, para não deixar a defesa da banda para a última hora — a definição de manual, "
            "porém, é a do item.",
        ],
        "grafico_verso": "ECO-E2-L00799-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de aula. O “até certo ponto” "
                       "protege o “livremente”, e o “apenas” é correto porque descreve a regra do regime. A banca "
                       "costuma errar o item trocando “flutue” por “permaneça constante” dentro da banda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de bandas cambiais, a taxa de câmbio é mantida constante dentro dos limites "
            "estabelecidos.”</i> → ERRADO (troca de conceito: dentro da banda o câmbio flutua)",
            "<i>“Nas bandas deslizantes, os limites da banda são reajustados periodicamente.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["apenas", "até certo ponto"],
        "dificuldade": 1,
        "comentario_fonte": "Só quando o valor ultrapassa as bandas o BC intervém, vendendo ou comprando dólares; "
                            "flutuação controlada que evita grandes oscilações.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00799-1 (bandas: câmbio flutua dentro dos limites; compartilha o "
                    "gráfico de verso)"],
    },
]

CARDS += [
    # ------------------------------------------------------------------ E2-L00106
    {
        "id": "ECO-E2-L00106-1", "fonte_ref": "E2-L00106", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BZ_INTERV,
        "rotulo_item": "Item",
        "assertiva": ("No regime de <i>currency board</i>, o Banco Central tem liberdade para imprimir moeda "
                      "nacional sempre que necessário, desde que mantenha a paridade cambial fixa com uma moeda "
                      "estrangeira forte, como o dólar, o que expande a quantidade de moeda em circulação sem "
                      "comprometer o equilíbrio estabelecido."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime de <i>currency board</i>, o Banco Central ")
                    + vm("tem liberdade para imprimir moeda nacional sempre que necessário, desde que mantenha")
                    + az(" a paridade cambial fixa com uma moeda estrangeira forte, como o dólar, o que ")
                    + vm("expande a quantidade de moeda em circulação sem comprometer o equilíbrio estabelecido")
                    + az(".")),
        "poucas": ("No " + azb("currency board") + " (caixa de conversão), cada unidade de moeda nacional precisa "
                   "de " + vd("lastro em reservas") + " na moeda-âncora: não há emissão discricionária. A base "
                   "monetária só cresce quando entram divisas."),
        "destrinchando": [
            "O " + azb("currency board") + " é a forma mais rígida de câmbio fixo que ainda preserva moeda "
            "nacional: (1) paridade fixada por lei; (2) conversibilidade plena à taxa fixa; (3) emissão "
            + vd("integralmente lastreada") + " em reservas na moeda-âncora. A autoridade monetária vira, na "
            "prática, uma casa de câmbio: troca moeda nacional por divisa e vice-versa.",
            "Consequência: a oferta de moeda torna-se " + azb("endógena ao balanço de pagamentos") + ". Entram "
            "dólares → reservas sobem → a base monetária se expande; saem dólares → a base se contrai "
            "automaticamente, e os juros sobem. Não há política monetária autônoma nem, em regra, "
            + azb("emprestador de última instância") + " para o sistema bancário.",
            "Emitir sem lastro, como sugere o item, quebraria a credibilidade do arranjo: o público passaria a "
            "duvidar da conversibilidade, trocaria moeda nacional por dólares, as reservas cairiam e o regime "
            "poderia colapsar — o oposto de “sem comprometer o equilíbrio”.",
            "Casos: " + vd("Argentina, 1991–2001") + " (Lei de Conversibilidade, 1 peso = 1 dólar): derrubou a "
            "hiperinflação, mas a rigidez diante dos choques de 1994–1999 terminou em recessão, corralito e "
            "colapso em 2001–2002. " + vd("Hong Kong, desde 1983") + " ⏳ (out/2026), atrelado ao dólar; "
            + vd("Estônia, 1992–2010") + ", até a adoção do euro em 2011.",
            "Escala de rigidez: dolarização/união monetária (sem moeda própria) > currency board > câmbio fixo "
            "convencional > bandas e crawling peg > flutuação administrada > flutuação livre.",
            vm("Regra-âncora: currency board = emissão presa às reservas; zero discricionariedade monetária."),
        ],
        "dissecando": (cz("[inversão · nexo indevido]") + " O item atribui ao regime mais rígido a característica "
                       "do mais livre (“liberdade para imprimir sempre que necessário”) e amarra a isso uma "
                       "conclusão tranquilizadora (“sem comprometer o equilíbrio”). Pista: quem fixa o câmbio e "
                       "promete conversibilidade plena não pode criar moeda à vontade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No currency board, a base monetária se contrai automaticamente quando há saída líquida de "
            "divisas.”</i> → CERTO",
            "<i>“No currency board, o Banco Central preserva plenamente a função de emprestador de última "
            "instância.”</i> → ERRADO (sem lastro não pode socorrer bancos emitindo moeda)",
            "<i>“Na dolarização oficial, o país mantém moeda própria lastreada em dólares.”</i> → ERRADO (troca "
            "de conceito: isso é o currency board)",
        ])],
        "reescrita": ("No regime de <i>currency board</i>, o Banco Central " + hl("só pode emitir moeda nacional "
                      "com lastro em reservas, para manter") + " a paridade cambial fixa com uma moeda estrangeira "
                      "forte, como o dólar, o que " + hl("subordina a quantidade de moeda em circulação ao fluxo "
                      "de divisas") + "."),
        "tipo_erro": ["INVERSAO", "NEXO_INDEVIDO"], "moduladores": ["sempre que necessário"], "dificuldade": 1,
        "comentario_fonte": "Currency board: paridade rígida, emissão restrita às reservas, perda de autonomia "
                            "monetária; vários comentários empilhados com tipologia de regimes do FMI e casos "
                            "(Argentina, Hong Kong, Estônia, Bulgária).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_parcial: o verso da fonte foi truncado em 20.000 caracteres (no meio de uma tipologia "
                    "de regimes cambiais); o trecho perdido não interfere no julgamento"],
    },
    # ------------------------------------------------------------------ E2-L00116
    {
        "id": "ECO-E2-L00116-1", "fonte_ref": "E2-L00116", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_AGENTES,
        "rotulo_item": "Item",
        "assertiva": ("As divisas internacionais são moedas que possuem curso forçado na economia nacional, e, "
                      "portanto, são utilizadas amplamente para transações econômicas cotidianas dentro do "
                      "território brasileiro, sem restrições específicas exigidas pelas autoridades."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As divisas internacionais são moedas que ") + vm("possuem") + az(" curso forçado na "
                       "economia nacional, e, portanto, ") + vm("são utilizadas amplamente") + az(" para "
                       "transações econômicas cotidianas dentro do território brasileiro, ")
                    + vm("sem restrições específicas exigidas") + az(" pelas autoridades.")),
        "poucas": ("No " + rx("Brasil") + ", só o " + azb("real") + " tem curso legal e forçado: é a única moeda "
                   "que não se pode recusar em pagamento. Divisas circulam apenas nas operações de câmbio e nas "
                   "hipóteses admitidas pela regulação."),
        "destrinchando": [
            azb("Curso legal") + ": a moeda é meio de pagamento reconhecido pelo Estado e extingue obrigações. "
            + azb("Curso forçado") + ": ninguém pode recusá-la em pagamento, e ela não é conversível por "
            "obrigação do emissor (em ouro, por exemplo). No Brasil, o real tem curso legal em todo o território "
            "desde o " + vd("Plano Real (1994)") + ".",
            azb("Divisas") + " são meios de pagamento internacionais (moeda estrangeira, depósitos no exterior, "
            "ordens de pagamento). Internamente, são mercadoria negociada no " + azb("mercado de câmbio") + ", "
            "por instituições autorizadas pelo " + rx("Banco Central") + ", e servem para comércio exterior, "
            "turismo, remessas e investimentos.",
            "Base normativa: o " + vd("Código Civil, art. 318") + ", torna nulas as convenções de pagamento em "
            "ouro ou em moeda estrangeira, salvo os casos da legislação especial; a " + vd("Lei 14.286/2021")
            + " (novo marco cambial) lista as hipóteses em que se admite estipular pagamento em moeda "
            "estrangeira em obrigações exequíveis no país (ex.: contratos ligados a exportação e importação).",
            "Logo, o dólar não é usado “amplamente” nem “sem restrições” no cotidiano brasileiro — diferente de "
            "economias dolarizadas (Equador, Panamá, El Salvador), em que o dólar é a própria moeda de curso "
            "legal.",
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " O item atribui à divisa o atributo "
                       "exclusivo da moeda nacional (curso forçado) e, a partir daí, generaliza (“amplamente”, "
                       "“sem restrições”). Pista: se a divisa tivesse curso forçado, não existiria mercado de "
                       "câmbio regulado."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No Brasil, as divisas são negociadas no mercado de câmbio por instituições autorizadas pelo "
            "Banco Central.”</i> → CERTO",
            "<i>“Por ter curso forçado, o real pode ser recusado em pagamentos no território nacional apenas se o "
            "credor preferir dólares.”</i> → ERRADO (curso forçado = não pode ser recusado)",
        ])],
        "reescrita": ("As divisas internacionais são moedas que " + hl("não possuem") + " curso forçado na "
                      "economia nacional, e, portanto, " + hl("não são utilizadas") + " para transações "
                      "econômicas cotidianas dentro do território brasileiro, " + hl("salvo nas hipóteses "
                      "admitidas") + " pelas autoridades."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["amplamente", "sem restrições"],
        "dificuldade": 1,
        "comentario_fonte": "Divisas não têm curso forçado; no Brasil só o real o tem. Divisas sujeitas a "
                            "regulamentação, usadas em transações autorizadas, geralmente de comércio exterior.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00117
    {
        "id": "ECO-E2-L00117-1", "fonte_ref": "E2-L00117", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_AGENTES,
        "rotulo_item": "Item",
        "assertiva": ("No mercado cambial brasileiro, os importadores são considerados demandantes de divisas "
                      "internacionais, pois precisam de moeda estrangeira para realizar transações comerciais fora "
                      "do país, remunerando suas compras em moeda estrangeira."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No mercado cambial brasileiro, os importadores são considerados <u>demandantes</u> de "
                      "divisas internacionais, pois precisam de moeda estrangeira para realizar transações "
                      "comerciais fora do país, remunerando suas compras em moeda estrangeira."),
        "poucas": ("Importador paga o fornecedor estrangeiro em divisa: precisa " + azb("comprar dólares")
                   + " com reais. Por isso está do lado da " + vd("demanda") + " no mercado de câmbio."),
        "destrinchando": [
            "O mercado de câmbio é um mercado como outro qualquer: o “bem” é a divisa e o “preço” é a taxa de "
            "câmbio E (R$/US$). Quem precisa pagar algo no exterior " + azb("demanda") + " divisas; quem recebe "
            "do exterior e converte em reais " + azb("oferta") + ".",
            "Lado da " + vd("demanda") + ": importadores, turistas brasileiros no exterior, quem remete lucros, "
            "dividendos e juros para fora, residentes que investem no exterior, quem amortiza dívida externa.",
            "Lado da " + vd("oferta") + ": exportadores, turistas estrangeiros no Brasil, investimento "
            "estrangeiro direto e em carteira, empréstimos externos que ingressam.",
            "Daí a ligação com o balanço de pagamentos: cada lançamento de crédito (exportação, ingresso de "
            "capital) gera oferta de divisas; cada débito (importação, remessa), demanda. A demanda por divisas "
            "é negativamente inclinada em E: com o dólar mais caro, importa-se menos.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de definição, verdadeiro sem ressalvas. O risco é só de "
                       "leitura apressada — confundir o lado do mercado (quem compra divisa é o importador; quem "
                       "vende é o exportador)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No mercado cambial, os exportadores são demandantes de divisas, pois recebem em moeda "
            "estrangeira.”</i> → ERRADO (troca de ator: exportadores ofertam divisas)",
            "<i>“A remessa de lucros de multinacionais para suas matrizes aumenta a demanda por divisas.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Importadores demandam divisas para pagar produtos e serviços adquiridos no exterior.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00118
    {
        "id": "ECO-E2-L00118-1", "fonte_ref": "E2-L00118", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_AGENTES,
        "rotulo_item": "Item",
        "assertiva": ("A taxa de câmbio pode ser definida como a referência de comparação de valor entre a moeda "
                      "nacional e uma referência externa, geralmente o dólar norte-americano. Uma elevação na taxa "
                      "de câmbio indica valorização da moeda doméstica em comparação com a referência."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A taxa de câmbio pode ser definida como a referência de comparação de valor entre a moeda "
                       "nacional e uma referência externa, geralmente o dólar norte-americano. Uma elevação na "
                       "taxa de câmbio indica ") + vm("valorização") + az(" da moeda doméstica em comparação com "
                                                                         "a referência.")),
        "poucas": ("Na convenção brasileira (R$ por US$), a taxa sobe quando são precisos " + vd("mais reais")
                   + " para comprar um dólar: é " + azb("desvalorização") + " do real, não valorização."),
        "destrinchando": [
            "A primeira frase é a definição correta: a " + azb("taxa de câmbio nominal") + " é o preço de uma "
            "moeda em termos de outra; no " + rx("Brasil") + ", cotada pelo “incerto” — reais por unidade de "
            "moeda estrangeira, tendo o dólar como referência principal.",
            "Com essa convenção: E de " + vd("R$ 5,00") + " para " + vd("R$ 5,50") + " por dólar → o real "
            "compra menos dólares → " + vd("desvalorização/depreciação") + " do real. E em queda → "
            "valorização.",
            "Efeitos típicos da desvalorização: exportações mais competitivas, importados mais caros, pressão "
            "inflacionária (" + azb("repasse cambial") + " ou pass-through) e aumento do peso, em reais, da "
            "dívida em moeda estrangeira.",
            "Cuidado com a cotação do “certo” (US$ por R$), usada por exemplo no Reino Unido para a libra: ali a "
            "leitura se inverte. Sem indicação contrária, a banca adota a convenção brasileira.",
        ],
        "dissecando": (cz("[inversão]") + " Primeira frase verdadeira, para ganhar a confiança; o erro está na "
                       "última palavra-chave (“valorização”). Pista: “taxa de câmbio sobe” é a manchete do dia em "
                       "que o real perde valor."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma elevação da taxa de câmbio R$/US$ tende a estimular as exportações brasileiras.”</i> → CERTO",
            "<i>“Uma queda da taxa de câmbio R$/US$ encarece as importações brasileiras.”</i> → ERRADO (queda = "
            "real valorizado = importações mais baratas)",
        ])],
        "reescrita": ("A taxa de câmbio pode ser definida como a referência de comparação de valor entre a moeda "
                      "nacional e uma referência externa, geralmente o dólar norte-americano. Uma elevação na taxa "
                      "de câmbio indica " + hl("desvalorização") + " da moeda doméstica em comparação com a "
                      "referência."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A elevação da taxa de câmbio simboliza desvalorização: são necessários mais reais "
                            "para adquirir um dólar.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00103-1 (mesma convenção, com a queda da taxa)"],
    },
    # ------------------------------------------------------------------ E2-L00119
    {
        "id": "ECO-E2-L00119-1", "fonte_ref": "E2-L00119", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_AGENTES,
        "rotulo_item": "Item",
        "assertiva": ("No equilíbrio do mercado cambial, a oferta de divisas pelos exportadores iguala a demanda "
                      "feita pelos importadores, resultando em uma taxa de câmbio que não requer intervenção "
                      "governamental para sua estabilização em condições normais de mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No equilíbrio do mercado cambial, a oferta de divisas pelos exportadores iguala a demanda "
                      "feita pelos importadores, resultando em uma taxa de câmbio que não requer intervenção "
                      "governamental para sua estabilização <u>em condições normais de mercado</u>."),
        "poucas": ("No modelo básico, a taxa de câmbio de " + azb("equilíbrio") + " é a que iguala oferta de "
                   "divisas (exportadores) e demanda (importadores); ali não há excesso a ser corrigido, e o "
                   "governo não precisa intervir."),
        "destrinchando": [
            "Modelo de aula do mercado de câmbio: curva de " + azb("oferta de divisas") + " crescente em E "
            "(dólar mais caro estimula exportar) e curva de " + azb("demanda") + " decrescente (dólar mais caro "
            "desestimula importar). O cruzamento define E* e o volume transacionado.",
            "Fora do equilíbrio, o próprio preço corrige: com E acima de E*, sobram divisas e o câmbio cai; "
            "abaixo, faltam divisas e ele sobe. Num regime flutuante, esse ajuste dispensa o Banco Central.",
            "O item é uma simplificação: na economia real, a maior parte do giro cambial vem da " + azb("conta "
            "financeira") + " (investimentos, empréstimos, remessas), não só do comércio. Mas a lógica de "
            "equilíbrio é a mesma — basta somar esses fluxos às curvas.",
            "“Em condições normais” é a ressalva que salva o item: em choques (fuga de capitais, crises), mesmo "
            "regimes flutuantes intervêm para conter volatilidade excessiva — é a " + azb("flutuação suja")
            + ".",
        ],
        "dissecando": (cz("[modulador relativo · literalidade]") + " O item simplifica o mercado a exportadores × "
                       "importadores, como na aula, e se protege com “em condições normais de mercado”. Itens "
                       "assim só ficam ERRADOS se tirarem a ressalva (“jamais requer intervenção”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No equilíbrio do mercado cambial, a taxa de câmbio jamais requer intervenção do Banco Central, "
            "mesmo em crises de balanço de pagamentos.”</i> → ERRADO (modulador absoluto)",
            "<i>“Se a taxa de câmbio estiver acima da de equilíbrio, haverá excesso de oferta de divisas.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "LITERAL"], "moduladores": ["em condições normais"], "dificuldade": 1,
        "comentario_fonte": "Equilíbrio cambial quando a oferta de divisas dos exportadores iguala a demanda dos "
                            "importadores; a taxa se ajusta sem intervenção estatal constante.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]

CARDS += [
    # ------------------------------------------------------------------ E2-L00120
    {
        "id": "ECO-E2-L00120-1", "fonte_ref": "E2-L00120", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_REGIMES,
        "rotulo_item": "Item",
        "assertiva": ("No regime de câmbio livre, o FMI estabelece que intervenções do Banco Central são permitidas "
                      "de forma ilimitada, podendo durar por tempo indeterminado, desde que visem corrigir "
                      "distorções cambiais graves, como as causadas por crises econômicas globais."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime de câmbio livre, o FMI estabelece que intervenções do Banco Central são "
                       "permitidas ") + vm("de forma ilimitada, podendo durar por tempo indeterminado")
                    + az(", desde que visem corrigir distorções cambiais graves, como as causadas por crises "
                         "econômicas globais.")),
        "poucas": ("Na classificação do " + azb("FMI") + ", flutuação livre admite intervenção só "
                   + vd("excepcional") + ": no máximo " + vd("3 episódios em 6 meses") + ", cada um de até "
                   + vd("3 dias úteis") + ". Intervir sem limite tira o país dessa categoria."),
        "destrinchando": [
            "O FMI classifica os regimes de facto no relatório anual " + azb("AREAER") + " (Annual Report on "
            "Exchange Arrangements and Exchange Restrictions). Entre os regimes flutuantes, distingue "
            + azb("free floating") + " (flutuação livre) de " + azb("floating") + " (flutuação, na prática "
            "administrada).",
            "Critério da " + vd("flutuação livre") + ": a intervenção ocorre apenas excepcionalmente, para "
            "conter condições desordenadas de mercado, e o país informa os dados ao FMI comprovando que houve "
            "no máximo " + vd("três intervenções nos últimos seis meses") + ", cada uma com duração de até "
            + vd("três dias úteis") + ".",
            "Quem intervém além disso — com frequência, para suavizar o câmbio, mas sem trajetória "
            "predeterminada — é classificado como " + vd("flutuação (managed floating)") + ". Se a intervenção "
            "sustenta um nível ou uma trilha, o regime vira “arranjo estabilizado” ou “crawl-like”.",
            "Por isso o item se contradiz: intervenção ilimitada e por tempo indeterminado é incompatível com "
            "a própria definição de câmbio livre. A finalidade (crises globais) não muda a classificação.",
            rx("Brasil") + " ⏳ (out/2026): o FMI enquadra o real como " + vd("floating") + ", e não como "
            "free floating, porque o Banco Central intervém com leilões de dólar à vista, linhas e swaps "
            "cambiais com frequência maior que a admitida na flutuação livre.",
        ],
        "dissecando": (cz("[modulador absoluto · troca de conceito]") + " “Ilimitada” e “tempo indeterminado” "
                       "são os gatilhos: o câmbio livre é justamente o regime com intervenção mínima e "
                       "quantificada. O item aplica ao free float o que caberia, no máximo, à flutuação "
                       "administrada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na classificação do FMI, um país em flutuação livre pode intervir excepcionalmente para conter "
            "condições desordenadas de mercado.”</i> → CERTO",
            "<i>“Para o FMI, qualquer intervenção do Banco Central no mercado de câmbio descaracteriza a flutuação "
            "livre.”</i> → ERRADO (modulador absoluto: intervenções excepcionais são admitidas)",
        ])],
        "reescrita": ("No regime de câmbio livre, o FMI estabelece que intervenções do Banco Central são "
                      "permitidas " + hl("apenas excepcionalmente, no máximo três em seis meses, cada uma com até "
                      "três dias úteis") + ", desde que visem corrigir distorções cambiais graves, como as "
                      "causadas por crises econômicas globais."),
        "tipo_erro": ["GENERALIZACAO", "TROCA_CONCEITO"], "moduladores": ["ilimitada", "tempo indeterminado"],
        "dificuldade": 2,
        "comentario_fonte": "O FMI limita intervenções no câmbio livre a situações graves: no máximo três em seis "
                            "meses, cada uma de até três dias.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00121
    {
        "id": "ECO-E2-L00121-1", "fonte_ref": "E2-L00121", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BZ_REGIMES,
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de flutuação administrada, o Banco Central pode intervir no mercado cambial "
                      "quantas vezes considerar necessário para corrigir rotas de política econômica, mesmo que a "
                      "intervenção se torne frequente e constante no tempo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": (az("Em um regime de flutuação administrada, o Banco Central pode intervir no mercado cambial ")
                    + vm("quantas vezes considerar necessário") + az(" para corrigir rotas de política econômica, ")
                    + vm("mesmo que") + az(" a intervenção se torne frequente e constante no tempo.")),
        "poucas": ("Para o gabarito, a " + azb("flutuação administrada") + " admite intervenções "
                   + vd("pontuais") + ": o câmbio continua formado pelo mercado. Intervenção constante "
                   "descaracterizaria a flutuação."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá ERRADO, coerente com a aula (flutuação administrada = intervenções pontuais "
                          "e de curta duração). Mas, na classificação do " + azb("FMI") + ", o que separa a "
                          "flutuação administrada (" + vd("floating") + ") da livre é justamente a "
                          + vm("frequência") + ": quem intervém mais de três vezes em seis meses deixa de ser "
                          "free floating e passa a floating, sem teto de intervenções. O regime só muda de "
                          "categoria se a intervenção sustentar um nível ou uma trilha para o câmbio. Uma banca "
                          "que adote o critério do FMI poderia dar CERTO; em prova, siga a leitura de que a "
                          "intervenção “constante” desfigura a flutuação.")],
        "destrinchando": [
            azb("Flutuação administrada") + " (managed floating, ou " + azb("flutuação suja") + "): o câmbio é "
            "determinado pelo mercado, mas o Banco Central entra comprando ou vendendo divisas (ou swaps) para "
            "suavizar volatilidade, recompor reservas ou evitar desalinhamentos, sem se comprometer com um "
            "nível ou trajetória.",
            "Na leitura da aula, a intervenção é " + vd("pontual e de curta duração") + ": se passa a ser "
            "frequente e constante, quem fixa o preço é o governo, e o regime se aproxima de um câmbio "
            "administrado com trajetória (bandas, crawling peg, arranjo estabilizado).",
            "Espectro: " + vd("free floating") + " (no máximo 3 intervenções em 6 meses, até 3 dias úteis cada) "
            "→ " + vd("floating") + " (intervenções mais frequentes, sem trilha) → arranjos estabilizados e "
            "crawl-like (intervenção que sustenta nível ou tendência) → fixos.",
            rx("Brasil") + " ⏳ (out/2026): flutuação desde " + vd("1999") + ", com intervenções do Banco "
            "Central por leilões de dólar à vista, linhas com recompra e swaps cambiais em momentos de estresse; "
            "o FMI classifica o regime brasileiro como " + vd("floating") + ".",
            "“Corrigir rotas de política econômica” também pesa contra o item: na flutuação suja o objetivo "
            "declarado é conter volatilidade, não conduzir o câmbio a um alvo de política.",
        ],
        "dissecando": (cz("[modulador absoluto · extrapolação]") + " O gabarito apoia-se em “quantas vezes "
                       "considerar necessário” e no “mesmo que… frequente e constante”, que estendem a "
                       "discricionariedade além do que a aula admite. A fragilidade é que o critério oficial do "
                       "FMI não limita a frequência na flutuação administrada."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na flutuação administrada, o Banco Central intervém pontualmente para conter volatilidade "
            "excessiva, sem compromisso com um nível de câmbio.”</i> → CERTO",
            "<i>“Na flutuação administrada, o Banco Central anuncia e defende uma paridade fixa.”</i> → ERRADO "
            "(troca de conceito: isso é câmbio fixo)",
        ])],
        "reescrita": ("Em um regime de flutuação administrada, o Banco Central pode intervir no mercado cambial "
                      + hl("pontualmente") + " para corrigir rotas de política econômica, " + hl("sem que")
                      + " a intervenção se torne frequente e constante no tempo."),
        "tipo_erro": ["GENERALIZACAO", "EXTRAPOLACAO"],
        "moduladores": ["quantas vezes considerar necessário", "mesmo que"], "dificuldade": 3,
        "comentario_fonte": "Na flutuação administrada, as intervenções são pontuais, sobretudo em pressões "
                            "inflacionárias; não podem ser constantes ou frequentes.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: pelo critério do FMI (AREAER), a flutuação administrada (floating) não tem teto "
                    "de frequência de intervenções; o ERRADO da fonte segue a definição de aula (intervenções "
                    "pontuais). Mantido o gabarito da fonte",
                    "quase_duplicata: ECO-E2-L00798-1 (flutuação suja com intervenções eventuais, CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L00122
    {
        "id": "ECO-E2-L00122-1", "fonte_ref": "E2-L00122", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_REGIMES,
        "rotulo_item": "Item",
        "assertiva": ("Uma das principais características do câmbio administrado com regras é a intervenção do "
                      "Banco Central para ajustes pontuais, sem a necessidade de mudança de rota cambial, enquanto "
                      "no câmbio administrado sem regras, a política econômica pode alterar de forma significativa "
                      "a trajetória cambial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma das principais características do câmbio administrado <u>com regras</u> é a "
                      "intervenção do Banco Central para ajustes pontuais, sem a necessidade de mudança de rota "
                      "cambial, enquanto no câmbio administrado <u>sem regras</u>, a política econômica pode "
                      "alterar de forma significativa a trajetória cambial."),
        "poucas": ("Com " + azb("regras") + " anunciadas, o Banco Central só faz correções pontuais em torno da "
                   "trajetória prevista; " + azb("sem regras") + " (discricionário), a política econômica pode "
                   "mudar o rumo do câmbio de forma relevante."),
        "destrinchando": [
            "A distinção é entre " + azb("regra × discricionariedade") + " na administração do câmbio. No câmbio "
            "administrado <b>com regras</b>, o mercado conhece de antemão o critério: uma banda, uma paridade "
            "deslizante (" + azb("crawling peg") + ") reajustada por fórmula, uma meta de reservas. O BC atua "
            "para manter o câmbio dentro do combinado — ajustes pontuais, sem mudar a rota.",
            "No câmbio administrado <b>sem regras</b> (flutuação administrada discricionária), não há trilha "
            "anunciada: o governo intervém conforme seus objetivos do momento (competitividade, inflação, "
            "reservas) e pode alterar significativamente a trajetória do câmbio.",
            "Trade-off clássico: regras dão " + vd("previsibilidade e credibilidade") + ", mas podem ser alvo "
            "de ataques se ficarem desalinhadas; a discricionariedade dá " + vd("flexibilidade") + ", ao custo "
            "de incerteza sobre o “jogo” do BC.",
            rx("Brasil") + ": as minidesvalorizações de " + vd("1968") + " em diante (crawling peg, regra de "
            "acompanhar o diferencial de inflação) e as bandas de 1995–1999 são exemplos de câmbio administrado "
            "com regras.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Item de taxonomia de aula: o contraste "
                       "regras × sem regras está corretamente atribuído. A versão ERRADA típica inverte os "
                       "dois polos (“com regras, a política pode alterar significativamente a trajetória”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No câmbio administrado com regras, o Banco Central pode alterar livremente a trajetória cambial, "
            "enquanto no administrado sem regras ele só faz ajustes pontuais.”</i> → ERRADO (inversão dos polos)",
            "<i>“O crawling peg é exemplo de câmbio administrado com regras.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["pode"], "dificuldade": 2,
        "comentario_fonte": "Com regras, o BC intervém para correções de rota sem alterar a trajetória; sem regras, "
                            "pode usar políticas amplas para modificar a rota cambial.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: “câmbio administrado com regras × sem regras” é terminologia do curso, não "
                    "categoria literal do FMI; comentário construído pela distinção regra × discricionariedade"],
    },
    # ------------------------------------------------------------------ E2-L00123
    {
        "id": "ECO-E2-L00123-1", "fonte_ref": "E2-L00123", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_REGIMES,
        "rotulo_item": "Item",
        "assertiva": ("Os regimes de bandas cambiais podem ser caracterizados por bandas horizontais, que se ajustam "
                      "de acordo com variações pré-estabelecidas e não revelam tendência de política cambial, ou "
                      "por bandas transversais, que implicam ajustes graduais na taxa de câmbio, indicando um "
                      "direcionamento de política cambial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Os regimes de bandas cambiais podem ser caracterizados por bandas <u>horizontais</u>, que se "
                      "ajustam de acordo com variações pré-estabelecidas e <u>não revelam tendência</u> de política "
                      "cambial, ou por bandas <u>transversais</u>, que implicam ajustes graduais na taxa de câmbio, "
                      "<u>indicando um direcionamento</u> de política cambial."),
        "poucas": ("Banda " + azb("horizontal") + ": piso e teto fixos, câmbio oscilando em torno de um centro "
                   "estável — sem tendência. Banda " + azb("transversal") + " (inclinada, deslizante): os limites "
                   "se movem no tempo e conduzem o câmbio a um novo patamar."),
        "destrinchando": [
            "Desenhe no tempo: a " + azb("banda horizontal") + " são duas retas paralelas ao eixo do tempo "
            "(ex.: câmbio entre " + vd("R$ 4,90 e R$ 5,10") + "); o câmbio varia dentro da faixa de amplitude "
            "pré-fixada (por exemplo, ±2% em torno da paridade central), sem sinalizar direção — o objetivo é "
            "estabilidade.",
            "A " + azb("banda transversal") + " (inclinada, ou " + azb("crawling band") + ") tem limites que "
            "sobem (ou descem) periodicamente, em geral pelo diferencial de inflação ou por meta de "
            "competitividade. A inclinação revela a intenção: levar o câmbio, aos poucos, a outro patamar sem "
            "choque abrupto.",
            "Parentes: o " + azb("crawling peg") + " faz o mesmo com uma paridade única (sem faixa); a banda "
            "transversal soma a faixa de flutuação ao deslizamento.",
            "Literatura: as " + azb("target zones") + " (zonas-alvo) de " + oc("Paul Krugman") + " (1991) "
            "mostram que uma banda crível estabiliza o câmbio mesmo dentro da faixa, porque o mercado antecipa "
            "a defesa dos limites.",
            rx("Brasil") + ": as bandas de " + vd("1995–1999") + " foram reajustadas periodicamente, com "
            "desvalorização gradual do real — exemplo de banda deslizante.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item usa o vocabulário da aula (“transversais” = "
                       "inclinadas) e atribui corretamente a cada tipo a presença ou ausência de tendência. A "
                       "redação “que se ajustam de acordo com variações pré-estabelecidas” refere-se à amplitude "
                       "fixa da faixa, não a limites móveis — leitura apressada poderia ver aí uma contradição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As bandas horizontais indicam um direcionamento da política cambial, pois deslocam o câmbio "
            "gradualmente para novo patamar.”</i> → ERRADO (troca de conceito: isso é a banda transversal)",
            "<i>“Na banda transversal, os limites são reajustados periodicamente.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["podem"], "dificuldade": 2,
        "comentario_fonte": "Bandas horizontais: ajustes pré-determinados (até 2%), sem mudança de política; "
                            "transversais: conduzem gradualmente o câmbio a novo patamar.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00105-1 e ECO-E2-L00799-1 (bandas cambiais)"],
    },
    # ------------------------------------------------------------------ E2-L00142
    {
        "id": "ECO-E2-L00142-1", "fonte_ref": "E2-L00142", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_ISLMBP,
        "rotulo_item": "Item",
        "assertiva": ("No mercado cambial, a elevação da taxa de juros leva a uma desvalorização da moeda nacional, "
                      "causando uma diminuição na taxa de câmbio, já que a moeda se torna mais abundante e seu "
                      "valor se distancia de um parâmetro internacional."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No mercado cambial, a elevação da taxa de juros leva a uma ") + vm("desvalorização")
                    + az(" da moeda nacional, causando uma diminuição na taxa de câmbio, já que a moeda se torna "
                         "mais ") + vm("abundante") + az(" e seu valor se ") + vm("distancia")
                    + az(" de um parâmetro internacional.")),
        "poucas": ("Juros mais altos atraem capital e tornam a moeda nacional mais " + azb("escassa") + ": ela se "
                   + vd("valoriza") + " e a taxa de câmbio (R$/US$) " + vd("cai") + ". A “diminuição da taxa” "
                   "está certa; o resto está invertido."),
        "destrinchando": [
            "Dois canais levam ao mesmo resultado. " + azb("Canal financeiro") + ": com i doméstico maior, "
            "aplicar no país rende mais que lá fora (" + azb("paridade de juros") + ": i = i* + depreciação "
            "esperada + risco); investidores trazem dólares, a oferta de divisas cresce e E cai.",
            azb("Canal monetário") + ": a alta dos juros vem de política monetária contracionista — o BC enxuga "
            "liquidez, o crédito encarece e a moeda nacional fica menos abundante. Moeda mais escassa vale "
            "mais.",
            "Resultado na cotação do incerto: E ↓ = " + vd("valorização/apreciação") + " do real. A queda da "
            "taxa de câmbio é coerente com valorização, não com desvalorização — o item combina efeitos que "
            "não podem ocorrer juntos.",
            "No " + azb("IS-LM-BP") + " com mobilidade de capitais: a alta de juros desloca a BP e, sob câmbio "
            "flutuante, aprecia a moeda, o que reduz exportações líquidas e reforça a contração da demanda — é "
            "um dos canais de transmissão da política monetária (canal do câmbio).",
            vm("Regra-âncora: juros ↑ → entrada de capital → moeda nacional ↑ (valoriza) → E ↓."),
        ],
        "dissecando": (cz("[inversão · contradição]") + " O item inverte o efeito dos juros e a justificativa "
                       "(“mais abundante”, “se distancia”), mas mantém a “diminuição na taxa de câmbio”, que só "
                       "combina com valorização. Pista: desvalorização e queda de E, na mesma frase, se "
                       "contradizem na convenção brasileira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma redução da taxa de juros doméstica, tudo o mais constante, tende a depreciar a moeda "
            "nacional.”</i> → CERTO",
            "<i>“A elevação da taxa de juros externa tende a valorizar a moeda nacional.”</i> → ERRADO (o "
            "capital sai: a moeda nacional se deprecia)",
        ])],
        "reescrita": ("No mercado cambial, a elevação da taxa de juros leva a uma " + hl("valorização") + " da "
                      "moeda nacional, causando uma diminuição na taxa de câmbio, já que a moeda se torna mais "
                      + hl("escassa") + " e seu valor se " + hl("aproxima") + " de um parâmetro internacional."),
        "tipo_erro": ["INVERSAO", "CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A alta de juros valoriza a moeda nacional (menos moeda em circulação, capital "
                            "estrangeiro atraído); a taxa de câmbio cai.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]

CARDS += [
    # ------------------------------------------------------------------ E2-L00191
    {
        "id": "ECO-E2-L00191-1", "fonte_ref": "E2-L00191", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_PPC,
        "rotulo_item": "Item",
        "assertiva": "A PPC estará garantida se a lei do preço único for válida.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A PPC estará garantida <u>se</u> a lei do preço único for válida."),
        "poucas": ("A " + azb("PPC") + " é a " + azb("lei do preço único") + " aplicada a uma cesta: se cada bem "
                   "custa o mesmo nos dois países (em moeda comum), a cesta também custa — e E = P/P*."),
        "destrinchando": [
            azb("Lei do preço único") + " (LPU): sem custos de transporte, barreiras ou diferenças de qualidade, a "
            "arbitragem faz um bem idêntico ter o mesmo preço em qualquer lugar, expresso na mesma moeda: "
            + vd("pᵢ = E · pᵢ*") + ". Se o trigo custa US$ 200 lá fora e E = 5, custa R$ 1.000 aqui.",
            azb("PPC absoluta") + ": vale para o nível geral de preços — " + vd("P = E · P*") + ", ou "
            + vd("E = P/P*") + ". Se a LPU vale para todos os bens da cesta (e as cestas têm a mesma "
            "composição), basta somar as igualdades: a PPC sai como consequência.",
            "A recíproca não é verdadeira: a PPC pode valer “em média” para a cesta mesmo com desvios da LPU em "
            "bens específicos que se compensem. Por isso a LPU é condição <b>suficiente</b>, não necessária.",
            "Por que a PPC falha na prática: bens " + azb("não comercializáveis") + " (serviços, aluguel), "
            "custos de transporte e tarifas, concorrência imperfeita, cestas diferentes entre países e preços "
            "rígidos no curto prazo. O efeito " + oc("Balassa-Samuelson") + " explica por que países ricos têm "
            "nível de preços mais alto.",
            "Origem: a ideia é antiga (Escola de Salamanca), mas a formulação moderna é de " + oc("Gustav Cassel")
            + ", no contexto do pós-Primeira Guerra.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Condicional correta (LPU ⇒ PPC). A banca erraria o item "
                       "invertendo a implicação (“a LPU só vale se a PPC estiver garantida”) ou trocando "
                       "“garantida” por “desmentida”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a PPC absoluta for válida, a lei do preço único necessariamente vale para cada bem "
            "individual.”</i> → ERRADO (inversão da implicação: desvios podem se compensar na cesta)",
            "<i>“A existência de bens não comercializáveis é uma das razões para o descumprimento da PPC.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["se"], "dificuldade": 2,
        "comentario_fonte": "A PPC decorre da lei do preço único aplicada a uma cesta de comercializáveis: com "
                            "arbitragem sem custos, o câmbio nominal se ajusta ao diferencial de níveis de preços.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00192
    {
        "id": "ECO-E2-L00192-1", "fonte_ref": "E2-L00192", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BZ_PPC,
        "rotulo_item": "Item",
        "assertiva": "Se a PPC estiver garantida, as taxas de câmbio real e nominal serão iguais.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Se a PPC estiver garantida, as taxas de câmbio real e nominal <u>serão iguais</u>."),
        "poucas": ("Com " + azb("PPC absoluta") + ", E = P/P* e o câmbio real q = E·P*/P = " + vd("1") + ": não há "
                   "distorção real, e o câmbio nominal reflete só os preços. A banca lê isso como “real e nominal "
                   "iguais”."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá CERTO, e o próprio comentário de origem admite a imprecisão. Em sentido "
                          "estrito, sob PPC absoluta o câmbio " + vm("real é igual a 1") + " (adimensional), "
                          "enquanto o nominal é P/P* (ex.: R$ 5,00/US$) — não são numericamente iguais. A "
                          "igualdade só vale com índices de preço normalizados na mesma base (P = P* = 1 no "
                          "período-base). A leitura mais defensável seria ERRADO; o curso adota a leitura "
                          "“funcional” (o câmbio real não se afasta da paridade).")],
        "destrinchando": [
            azb("Câmbio nominal") + " (E): preço da moeda estrangeira em moeda nacional (R$/US$). "
            + azb("Câmbio real") + " (q): quantas cestas nacionais custa uma cesta estrangeira — "
            + vd("q = E · P*/P") + ". É o que importa para a competitividade.",
            "Sob " + azb("PPC absoluta") + ", E = P/P*. Substituindo: q = (P/P*) · (P*/P) = " + vd("1")
            + ". Uma cesta compra exatamente uma cesta equivalente no exterior. Sob " + azb("PPC relativa")
            + ", %ΔE = π − π*, e o câmbio real fica " + vd("constante") + " (não necessariamente igual a 1).",
            "Exemplo: cesta de " + vd("R$ 500") + " no Brasil e " + vd("US$ 100") + " nos EUA. PPC → E = 5,00 e "
            "q = 5 × 100/500 = 1. Se o mercado cotar E = 4,00, q = 0,80: o real está " + azb("sobrevalorizado")
            + " (lá fora tudo parece barato), o que estimula importações e prejudica exportadores.",
            "Por que a PPC não vale no curto prazo: preços rígidos e câmbio volátil — o " + azb("overshooting")
            + " de " + oc("Dornbusch") + " (1976) —, bens não comercializáveis (efeito " + oc("Balassa-Samuelson")
            + "), custos de transporte e barreiras.",
            vm("Regra-âncora: PPC absoluta ⇒ q = 1; PPC relativa ⇒ q constante."),
        ],
        "dissecando": (cz("[detalhe · literalidade]") + " Item que mede a convenção do curso, não a álgebra: "
                       "“iguais” deve ser lido como “o câmbio real não destoa do nominal”. Na dúvida, guarde a "
                       "conta q = 1 e saiba que bancas rigorosas podem tratar a igualdade literal como erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se a PPC absoluta for válida, a taxa de câmbio real será igual a 1.”</i> → CERTO",
            "<i>“Se a PPC relativa for válida, a taxa de câmbio real se depreciará na medida do diferencial de "
            "inflação.”</i> → ERRADO (quem se ajusta é o nominal; o real fica constante)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": ["se"], "dificuldade": 3,
        "comentario_fonte": "Com PPC válida, q = E·P*/P constante e, na absoluta, q = 1. Longa exposição com "
                            "exemplo numérico (cesta de R$ 500 e US$ 100), Cassel, Balassa-Samuelson, "
                            "Dornbusch; reconhece que “iguais” é impreciso em sentido literal.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 014", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 015", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 016", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 017", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 018", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["contestavel: sob PPC absoluta o câmbio real é 1 e o nominal é P/P*; a igualdade literal só "
                    "vale com índices normalizados. Mantido o CERTO da fonte",
                    "quase_duplicata: ECO-E2-L00220-1 (mesma tese de equiparação nominal = real) e "
                    "ECO-E2-L01043-1 (PPC compatível com câmbio real constante)"],
    },
    # ------------------------------------------------------------------ E2-L00220
    {
        "id": "ECO-E2-L00220-1", "fonte_ref": "E2-L00220", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BZ_DIN,
        "rotulo_item": "Item",
        "assertiva": ("A teoria da paridade do poder de compra sugere que a inflação interna de um país exerce "
                      "efeitos diretos sobre a igualdade de preços domésticos e internacionais, influenciando, "
                      "assim, a estabilização cambial no longo prazo. Essa estabilização, por sua vez, promove a "
                      "equiparação da taxa de câmbio nominal à taxa de câmbio real, permitindo que o poder "
                      "econômico de diferentes países se iguale, independentemente das variações inflacionárias."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A teoria da paridade do poder de compra sugere que a inflação interna de um país exerce "
                      "efeitos diretos sobre a igualdade de preços domésticos e internacionais, influenciando, "
                      "assim, a estabilização cambial no longo prazo. Essa estabilização, por sua vez, promove a "
                      "<u>equiparação da taxa de câmbio nominal à taxa de câmbio real</u>, permitindo que o "
                      "<u>poder econômico</u> de diferentes países se iguale, independentemente das variações "
                      "inflacionárias."),
        "poucas": ("No longo prazo, a " + azb("PPC") + " faz o câmbio nominal compensar o diferencial de inflação: "
                   "o câmbio real se estabiliza e o " + vd("poder de compra") + " das moedas se equaliza, seja "
                   "qual for a inflação de cada país."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "A fonte dá CERTO, na linha do curso (sob PPC, “nominal = real”). Há duas "
                          "imprecisões: (1) sob PPC absoluta o câmbio " + vm("real vale 1") + " e o nominal vale "
                          "P/P* — não são iguais em sentido literal; (2) “poder econômico” só faz sentido lido "
                          "como " + azb("poder de compra") + " das moedas — o poder econômico dos países (renda, "
                          "produto) não se iguala por efeito do câmbio. Uma banca rigorosa poderia dar ERRADO.")],
        "destrinchando": [
            "Mecanismo: se a inflação interna supera a externa e o câmbio não muda, os bens nacionais ficam "
            "caros em relação aos estrangeiros. A arbitragem (mais importação, menos exportação) pressiona a "
            "moeda nacional para baixo até que " + vd("%ΔE ≈ π − π*") + " (" + azb("PPC relativa") + ").",
            "Com esse ajuste, o " + azb("câmbio real") + " q = E·P*/P fica " + vd("constante") + " — e, na PPC "
            "absoluta, igual a 1. É isso que a assertiva chama de “estabilização cambial no longo prazo” e de "
            "“equiparação” entre nominal e real.",
            "“Independentemente das variações inflacionárias”: o país pode ter inflação alta ou baixa; se a PPC "
            "vale, a variação nominal neutraliza o diferencial, e o poder de compra relativo das moedas se "
            "mantém. Ex.: π = " + vd("7%") + ", π* = " + vd("2%") + " → depreciação de cerca de " + vd("5%")
            + " e q inalterado.",
            "Limites: a PPC é teoria de " + vd("longo prazo") + "; no curto prazo, preços rígidos e fluxos "
            "financeiros afastam o câmbio da paridade, e os desvios são persistentes (meia-vida de vários anos "
            "nos estudos empíricos).",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Redação longa e vaga, que parafraseia a aula "
                       "(“equiparação nominal-real”, “poder econômico”). O julgamento depende de aceitar a "
                       "convenção do curso; o candidato que conhece a álgebra (q = 1 ≠ E) tende a desconfiar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela PPC relativa, o câmbio nominal varia de modo a compensar o diferencial de inflação, "
            "mantendo constante o câmbio real.”</i> → CERTO",
            "<i>“Pela PPC, a inflação interna mais alta provoca apreciação real permanente da moeda.”</i> → ERRADO "
            "(sob PPC o câmbio real fica constante)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["sugere"], "dificuldade": 3,
        "comentario_fonte": "A PPC integra preços e câmbio; inflação controlada e equalizada estabiliza o câmbio "
                            "no longo prazo e alinha o nominal ao real, levando à paridade do poder econômico.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: “equiparação do câmbio nominal ao real” é imprecisa (sob PPC absoluta q = 1) e "
                    "“poder econômico” só se sustenta lido como poder de compra. Mantido o CERTO da fonte",
                    "quase_duplicata: ECO-E2-L00192-1 (mesma tese, CERTO)"],
    },
    # ------------------------------------------------------------------ E2-L00222
    {
        "id": "ECO-E2-L00222-1", "fonte_ref": "E2-L00222", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_BZ_DIN,
        "rotulo_item": "Item",
        "assertiva": ("A lei do preço único postula que, no cenário de um mercado internacional perfeito, os preços "
                      "dos bens devem ser homogêneos entre diferentes países. Isso implica que mesmo com a ausência "
                      "de inflação igualitária entre nações, o mercado cambial, por si só, ajusta automaticamente "
                      "as taxas de câmbio para corrigir disparidades de preços, de modo que as diferenças de poder "
                      "aquisitivo entre países se tornam irrelevantes."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A lei do preço único postula que, no cenário de um mercado internacional perfeito, os "
                       "preços dos bens devem ser homogêneos entre diferentes países. Isso implica que mesmo com a "
                       "ausência de inflação igualitária entre nações, ")
                    + vm("o mercado cambial, por si só, ajusta automaticamente")
                    + az(" as taxas de câmbio para corrigir disparidades de preços, de modo que as diferenças de "
                         "poder aquisitivo entre países ") + vm("se tornam irrelevantes") + az(".")),
        "poucas": ("A homogeneidade de preços da " + azb("lei do preço único") + " resulta da " + azb("arbitragem "
                   "nos mercados de bens") + ", com ajuste conjunto de preços e câmbio, e só no longo prazo — não "
                   "de um ajuste automático do mercado cambial “por si só”."),
        "destrinchando": [
            "A primeira frase está certa: com mercado perfeito (sem transporte, tarifas ou diferenças de "
            "qualidade), a arbitragem iguala o preço de um bem idêntico em moeda comum — " + vd("p = E · p*")
            + ".",
            "O erro está no mecanismo. Quem iguala os preços é a " + azb("arbitragem de bens") + ": compra-se "
            "onde é barato, vende-se onde é caro. Esse movimento pressiona os preços dos bens <b>e</b> o "
            "câmbio. O ajuste é do conjunto (mercados de bens, monetário e cambial), não do mercado cambial "
            "isolado e instantâneo.",
            "No curto prazo, o câmbio é guiado sobretudo por fluxos financeiros (juros, risco, expectativas), "
            "não por diferenciais de preços de bens. Por isso pode se afastar muito da paridade — o "
            + azb("overshooting") + " de " + oc("Dornbusch") + " — e os desvios da PPC são persistentes.",
            "Por fim, as diferenças de poder aquisitivo não se tornam “irrelevantes”: bens não comercializáveis, "
            "custos de transação e cestas distintas mantêm níveis de preços diferentes entre países (o PIB "
            "medido em PPC difere do PIB a câmbio de mercado justamente por isso).",
            vm("Regra-âncora: LPU/PPC = tendência de longo prazo via arbitragem de bens, não ajuste cambial "
               "automático."),
        ],
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " Primeira frase é a definição da LPU; o erro "
                       "foi enxertado na consequência, com moduladores fortes (“por si só”, “automaticamente”, "
                       "“irrelevantes”). Pista: teorias de paridade descrevem tendências sob hipóteses ideais, "
                       "nunca ajustes automáticos e isolados."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A lei do preço único pressupõe a ausência de custos de transporte e de barreiras comerciais.”</i> "
            "→ CERTO",
            "<i>“Pela PPC, o câmbio corrige instantaneamente qualquer diferencial de inflação entre os "
            "países.”</i> → ERRADO (modulador absoluto: é tendência de longo prazo)",
        ])],
        "reescrita": ("A lei do preço único postula que, no cenário de um mercado internacional perfeito, os preços "
                      "dos bens devem ser homogêneos entre diferentes países. Isso implica que mesmo com a ausência "
                      "de inflação igualitária entre nações, " + hl("a arbitragem nos mercados de bens, com o "
                      "ajuste conjunto de preços e câmbio, tende a ajustar no longo prazo") + " as taxas de câmbio "
                      "para corrigir disparidades de preços, de modo que as diferenças de poder aquisitivo entre "
                      "países " + hl("tendem a se reduzir") + "."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["por si só", "automaticamente",
                                                                        "irrelevantes"],
        "dificuldade": 2,
        "comentario_fonte": "A homogeneidade de preços não é consequência apenas de flutuações cambiais, mas da "
                            "estabilização geral dos mercados cambial, monetário e de bens.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00487
    {
        "id": "ECO-E2-L00487-1", "fonte_ref": "E2-L00487", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_SMI,
        "rotulo_item": "Item",
        "assertiva": ("Suponha que a inflação no Brasil seja igual a 5% e que a inflação externa seja igual a 1%. "
                      "Considerando a versão relativa da paridade do poder de compra e que essas variações são "
                      "pequenas, para que a taxa real de câmbio se mantenha em equilíbrio e constante, a variação "
                      "da taxa de câmbio nominal deve ser igual a – 4%."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Suponha que a inflação no Brasil seja igual a 5% e que a inflação externa seja igual a "
                       "1%. Considerando a versão relativa da paridade do poder de compra e que essas variações "
                       "são pequenas, para que a taxa real de câmbio se mantenha em equilíbrio e constante, a "
                       "variação da taxa de câmbio nominal deve ser igual a ") + vm("– 4%") + az(".")),
        "poucas": ("PPC relativa: " + vd("%ΔE ≈ π − π* = 5% − 1% = +4%") + ". A moeda do país com mais inflação "
                   "precisa se " + azb("depreciar") + " (E sobe), não se apreciar."),
        "destrinchando": [
            "Câmbio real: " + vd("q = E · P*/P") + ". Em variações pequenas, %Δq ≈ %ΔE + π* − π. Para q "
            "constante (%Δq = 0): " + vd("%ΔE = π − π*") + " — é a " + azb("PPC relativa") + ".",
            "Com os dados: %ΔE = 5% − 1% = " + vd("+4%") + ". O real deve perder cerca de 4% de valor frente "
            "à moeda externa (ex.: de R$ 5,00 para R$ 5,20 por dólar) para compensar o fato de os preços "
            "brasileiros subirem 4 pontos a mais.",
            "Se E caísse 4% (o −4% do item), o efeito seria dobrado na direção errada: %Δq ≈ −4% + 1% − 5% = "
            + vd("−8%") + " — " + azb("apreciação real") + " de cerca de 8%, com perda de competitividade.",
            "Atenção ao sinal conforme a convenção: com E = R$/US$ (cotação do incerto, padrão no Brasil), "
            "depreciação é variação <b>positiva</b>. A conta exata (sem aproximação) seria (1,05/1,01) − 1 ≈ "
            "3,96%; o enunciado autoriza a aproximação ao dizer que as variações são pequenas.",
            vm("Regra-âncora: mais inflação em casa → E sobe na medida do diferencial (%ΔE = π − π*)."),
        ],
        "dissecando": (cz("[dado alterado · inversão]") + " Número certo, sinal trocado: a banca aposta em quem "
                       "faz π* − π ou confunde depreciação com variação negativa. Pista: o país com inflação "
                       "maior nunca vê sua moeda se fortalecer sob PPC."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a variação da taxa de câmbio nominal deve ser de aproximadamente +4%, o que corresponde a uma "
            "depreciação nominal do real.”</i> → CERTO",
            "<i>“…a taxa real de câmbio deve se depreciar 4%.”</i> → ERRADO (sob PPC o real fica constante; quem "
            "varia é o nominal)",
        ])],
        "reescrita": ("Suponha que a inflação no Brasil seja igual a 5% e que a inflação externa seja igual a 1%. "
                      "Considerando a versão relativa da paridade do poder de compra e que essas variações são "
                      "pequenas, para que a taxa real de câmbio se mantenha em equilíbrio e constante, a variação "
                      "da taxa de câmbio nominal deve ser igual a " + hl("+ 4%") + "."),
        "tipo_erro": ["DADO_ALTERADO", "INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Δe ≈ π − π* = 5% − 1% = +4%: a moeda doméstica precisa se desvalorizar 4%. Duplicata "
                            "(lista de 2023) traz a dedução %e = %E + %P* − %P = 0 ⇒ %E = %P − %P*.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 180", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (verso da duplicata E2-L01045)"},
                          {"ref": "IMAGEM 181", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (verso da duplicata E2-L01045)"}],
        "alertas": ["duplicata: E2-L01045 (mesma assertiva, mesma banca Nabuco, lista de 24/07/2023) fundida "
                    "neste card; comentários unidos"],
    },
]

CARDS += [
    # ------------------------------------------------------------------ E2-L00488
    {
        "id": "ECO-E2-L00488-1", "fonte_ref": "E2-L00488", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_SMI,
        "rotulo_item": "Item",
        "assertiva": ("Um regime de taxa de câmbio fixa busca manter a taxa de câmbio real constante no longo "
                      "prazo, horizonte temporal este em que se admite que os preços domésticos e internacionais "
                      "sejam flexíveis."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um regime de taxa de câmbio fixa busca manter a taxa de câmbio ") + vm("real")
                    + az(" constante no longo prazo, horizonte temporal este em que se admite que os preços "
                         "domésticos e internacionais sejam flexíveis.")),
        "poucas": ("O câmbio fixo fixa o " + azb("nominal") + " (E). Com preços flexíveis, o " + azb("real")
                   + " (q = E·P*/P) varia com o diferencial de inflação — fixar o nominal não segura o real."),
        "destrinchando": [
            "O Banco Central só controla diretamente o preço da moeda: a paridade " + vd("E") + " (ex.: 1 peso "
            "= 1 dólar). O câmbio real depende também de P e P*, que o regime cambial não fixa.",
            "Com E fixo: " + vd("%Δq ≈ π* − π") + ". Se a inflação interna supera a externa, q cai — "
            + azb("apreciação real") + ", perda de competitividade, déficit externo crescente. Foi o que ocorreu "
            "com as âncoras cambiais da Argentina (1991–2001) e do " + rx("Brasil") + " (1994–1998).",
            "No longo prazo, com preços flexíveis, o ajuste do câmbio real ocorre pelos <b>preços</b>: deflação "
            "(ou inflação menor) no país com câmbio sobrevalorizado, o que costuma ser lento e recessivo. Ou, "
            "se a pressão vence, pela " + azb("desvalorização") + " da paridade.",
            "Quem busca câmbio real constante é uma regra de " + azb("crawling peg") + " indexada à inflação "
            "(minidesvalorizações pelo diferencial π − π*), como no Brasil de 1968 em diante — não o câmbio "
            "fixo.",
            vm("Regra-âncora: regime cambial fixa o nominal; o real depende de E, P e P*."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca nominal por real e acrescenta um contexto verdadeiro "
                       "(preços flexíveis no longo prazo) que, na verdade, é o motivo pelo qual o real <b>não</b> "
                       "fica constante. Pista: governo nenhum fixa nível de preços por decreto cambial."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob câmbio fixo, inflação doméstica superior à externa provoca apreciação real da moeda "
            "nacional.”</i> → CERTO",
            "<i>“Sob câmbio fixo, o câmbio real só pode variar por meio de desvalorizações oficiais.”</i> → ERRADO "
            "(restrição indevida: também varia com os preços)",
        ])],
        "reescrita": ("Um regime de taxa de câmbio fixa busca manter a taxa de câmbio " + hl("nominal")
                      + " constante no longo prazo, horizonte temporal este em que se admite que os preços "
                      "domésticos e internacionais sejam flexíveis."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Câmbio fixo mantém o nominal, não o real; com inflação diferente, o câmbio real varia "
                            "(inflação maior → valorização real).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00639
    {
        "id": "ECO-E2-L00639-1", "fonte_ref": "E2-L00639", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_MA,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a curva J, uma depreciação real da moeda doméstica provoca, inicialmente, uma "
                      "deterioração na balança comercial do próprio país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a curva J, uma depreciação real da moeda doméstica provoca, "
                      "<u>inicialmente</u>, uma <u>deterioração</u> na balança comercial do próprio país."),
        "poucas": ("No curto prazo, as quantidades exportadas e importadas quase não mudam, mas cada importação "
                   "fica mais cara em moeda doméstica: o saldo " + vd("piora") + ". Só depois, com o ajuste das "
                   "quantidades, melhora — o desenho do " + azb("J") + "."),
        "destrinchando": [
            "Saldo comercial em moeda doméstica: " + vd("BC = X − q·M") + " (q = câmbio real). Uma "
            "depreciação real tem dois efeitos: " + azb("efeito preço") + " (q ↑ encarece cada unidade "
            "importada — piora o saldo de imediato) e " + azb("efeito volume") + " (X ↑ e M ↓ — melhora o "
            "saldo, mas com defasagem).",
            "Por que o volume demora: contratos já fechados em moeda estrangeira, prazos de entrega, tempo para "
            "o consumidor trocar de fornecedor e para o exportador ampliar capacidade. No curto prazo as "
            "elasticidades são baixas; o efeito preço domina e o saldo cai.",
            "No médio e longo prazo, as elasticidades crescem. Se vale a condição de " + oc("Marshall-Lerner")
            + " — " + vd("|η_X| + |η_M| > 1") + " —, o efeito volume supera o efeito preço e o saldo termina "
            "acima do inicial.",
            "A curva J explica por que desvalorizações não melhoram a balança comercial “no dia seguinte” e por "
            "que governos podem ser tentados a abandonar o ajuste cedo demais.",
            vm("Regra-âncora: depreciação real → saldo piora primeiro (preço) e melhora depois (volume, se "
               "Marshall-Lerner)."),
        ],
        "grafico_verso": "ECO-E2-L00639-1-V1",
        "dissecando": (cz("[contraintuitivo · literalidade]") + " Verdadeiro, mas contraria a intuição de que "
                       "depreciar sempre melhora a balança. O “inicialmente” é a palavra que salva o item; a "
                       "versão ERRADA típica diz que a piora é permanente ou que a melhora é imediata."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com a curva J, uma depreciação real melhora imediatamente a balança comercial, que "
            "depois se deteriora.”</i> → ERRADO (inversão da ordem temporal)",
            "<i>“A melhora da balança comercial após a depreciação real requer que a soma das elasticidades-preço "
            "das exportações e importações seja maior que 1.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "LITERAL"], "moduladores": ["inicialmente"], "dificuldade": 1,
        "comentario_fonte": "Curto prazo: volumes inelásticos (contratos), preço das importações sobe; o saldo "
                            "piora antes de melhorar (Marshall-Lerner).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00659
    {
        "id": "ECO-E2-L00659-1", "fonte_ref": "E2-L00659", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_EI,
        "rotulo_item": "Item",
        "assertiva": ("Se os preços domésticos aumentam, mantendo-se constante o câmbio nominal e o nível de preços "
                      "internacionais, a taxa real de câmbio se deprecia, o que favorece as exportações líquidas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se os preços domésticos aumentam, mantendo-se constante o câmbio nominal e o nível de "
                       "preços internacionais, a taxa real de câmbio se ") + vm("deprecia") + az(", o que ")
                    + vm("favorece") + az(" as exportações líquidas.")),
        "poucas": ("Com " + vd("q = E·P*/P") + ", P ↑ (E e P* dados) faz q " + vd("cair") + ": "
                   + azb("apreciação real") + ". Os bens nacionais ficam relativamente mais caros, e as "
                   "exportações líquidas pioram."),
        "destrinchando": [
            azb("Câmbio real") + ": " + vd("q = E · P*/P") + " = preço da cesta estrangeira em cestas "
            "nacionais. q ↑ = depreciação real (o estrangeiro fica caro, ganha-se competitividade); q ↓ = "
            "apreciação real.",
            "No item, só P sobe: o denominador aumenta, q cai. O real compra a mesma quantidade de dólares, mas "
            "os produtos brasileiros encareceram — " + vd("apreciação real") + " mesmo sem nenhum movimento do "
            "câmbio nominal.",
            "Efeito sobre a demanda: exportações caem (bens nacionais mais caros lá fora) e importações sobem "
            "(estrangeiros relativamente baratos). As " + azb("exportações líquidas") + " NX(q) "
            + vd("diminuem") + ".",
            "Esse é o problema clássico de câmbio nominal fixo com inflação alta: a moeda se aprecia em termos "
            "reais “por dentro”, pelo lado dos preços. Para manter q constante, E teria de subir na mesma "
            "proporção que P/P* (PPC relativa).",
            vm("Regra-âncora: preços internos ↑ com E e P* constantes → q ↓ (apreciação real) → NX ↓."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sentido do câmbio real e, coerentemente, a consequência. "
                       "Quem confunde “preços sobem” com “moeda perde valor externo” cai. Pista: com o nominal "
                       "parado, o único que mudou foi o preço do produto nacional — ele ficou mais caro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se os preços internacionais aumentam, com câmbio nominal e preços domésticos constantes, a taxa "
            "real de câmbio se deprecia.”</i> → CERTO",
            "<i>“Uma depreciação nominal acompanhada de inflação doméstica de igual proporção eleva o câmbio "
            "real.”</i> → ERRADO (efeitos se anulam: q constante)",
        ])],
        "reescrita": ("Se os preços domésticos aumentam, mantendo-se constante o câmbio nominal e o nível de preços "
                      "internacionais, a taxa real de câmbio se " + hl("aprecia") + ", o que " + hl("prejudica")
                      + " as exportações líquidas."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "ε = E·P_ext/P_dom; P_dom ↑ → taxa real cai (apreciação real), prejudicando as "
                            "exportações líquidas.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 102", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00660
    {
        "id": "ECO-E2-L00660-1", "fonte_ref": "E2-L00660", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_EI,
        "rotulo_item": "Item",
        "assertiva": ("A adoção de um regime de câmbio flutuante, típico de economias com mobilidade de capitais e "
                      "autonomia monetária, elimina as incertezas para exportadores e importadores, tornando "
                      "dispensável o uso de mecanismos de hedge e proteção financeira."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A adoção de um regime de câmbio flutuante, típico de economias com mobilidade de capitais "
                       "e autonomia monetária, ") + vm("elimina") + az(" as incertezas para exportadores e "
                                                                       "importadores, tornando ")
                    + vm("dispensável") + az(" o uso de mecanismos de hedge e proteção financeira.")),
        "poucas": ("Câmbio " + azb("flutuante") + " = câmbio volátil: o preço da divisa muda todo dia. Isso "
                   + vd("aumenta") + " a incerteza de quem recebe ou paga em moeda estrangeira e torna o "
                   + azb("hedge") + " necessário."),
        "destrinchando": [
            "A primeira parte é correta e remete ao " + azb("trilema") + ": quem tem livre mobilidade de "
            "capitais e quer política monetária autônoma precisa abrir mão do câmbio fixo — daí o flutuante.",
            "O custo do flutuante é a " + vd("volatilidade") + ": o exportador que fecha uma venda hoje, para "
            "receber em 90 dias, não sabe quantos reais receberá; o importador não sabe quanto pagará. A "
            "incerteza cresce, não some.",
            azb("Hedge cambial") + " é a proteção contra essa incerteza: contratos a termo (NDF), futuros de "
            "dólar na B3, opções e swaps. O agente trava hoje a taxa futura, pagando um custo ou abrindo mão do "
            "ganho caso o câmbio se mova a seu favor.",
            "No câmbio fixo (crível), a incerteza cambial do dia a dia é menor — por isso a demanda por hedge "
            "também é menor. Mas há o risco de " + azb("desvalorização abrupta") + " se a paridade cair, como "
            "em 1999 no " + rx("Brasil") + ".",
            "Os " + rx("swaps cambiais") + " do Banco Central do Brasil oferecem justamente hedge ao mercado em "
            "momentos de estresse, sem queimar reservas à vista.",
        ],
        "dissecando": (cz("[inversão · modulador absoluto]") + " O item começa com uma descrição correta do "
                       "regime (trilema) e inverte o efeito sobre o risco, com verbos absolutos (“elimina”, "
                       "“dispensável”). Pista: “flutuante” e “sem incerteza” são termos incompatíveis."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O regime de câmbio flutuante aumenta a demanda por instrumentos de proteção cambial, como "
            "contratos a termo e futuros.”</i> → CERTO",
            "<i>“O câmbio flutuante é incompatível com a livre mobilidade de capitais.”</i> → ERRADO (é o fixo que "
            "conflita com mobilidade e autonomia monetária)",
        ])],
        "reescrita": ("A adoção de um regime de câmbio flutuante, típico de economias com mobilidade de capitais e "
                      "autonomia monetária, " + hl("aumenta") + " as incertezas para exportadores e importadores, "
                      "tornando " + hl("necessário") + " o uso de mecanismos de hedge e proteção financeira."),
        "tipo_erro": ["INVERSAO", "GENERALIZACAO"], "moduladores": ["elimina", "dispensável"], "dificuldade": 1,
        "comentario_fonte": "O câmbio flutuante introduz volatilidade e incerteza sobre recebimentos e pagamentos "
                            "em moeda estrangeira, tornando o hedge essencial.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00703
    {
        "id": "ECO-E2-L00703-1", "fonte_ref": "E2-L00703", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB_PC,
        "rotulo_item": "Item",
        "assertiva": ("A “Trindade Impossível” postula que um país não pode manter simultaneamente câmbio flutuante, "
                      "livre mobilidade de capitais e política monetária independente."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A “Trindade Impossível” postula que um país não pode manter simultaneamente câmbio ")
                    + vm("flutuante") + az(", livre mobilidade de capitais e política monetária independente.")),
        "poucas": ("O " + azb("trilema") + " impede a combinação de câmbio " + vd("fixo") + " + livre mobilidade "
                   "de capitais + política monetária autônoma. Com câmbio flutuante, as outras duas convivem — "
                   "é o caso de Brasil e EUA."),
        "destrinchando": [
            azb("Trindade impossível") + " (trilema da economia aberta), derivada do modelo " + oc("Mundell-"
            "Fleming") + ": dos três objetivos — " + vd("câmbio fixo") + ", " + vd("livre mobilidade de "
            "capitais") + " e " + vd("autonomia monetária") + " —, só dois podem ser obtidos ao mesmo tempo.",
            "Por quê: com capital livre e câmbio fixo, a paridade de juros obriga i = i*. Se o BC tentar baixar "
            "os juros, o capital sai, pressiona o câmbio, e o BC precisa vender reservas e recolher moeda até "
            "os juros voltarem a i*. A política monetária fica amarrada à do país-âncora.",
            "As três combinações possíveis: (1) fixo + mobilidade, sem autonomia — currency board, zona do "
            "euro, padrão-ouro; (2) " + vd("flutuante + mobilidade + autonomia") + " — EUA, " + rx("Brasil")
            + " pós-1999; (3) fixo + autonomia, com controles de capital — Bretton Woods, China por longos "
            "períodos.",
            "Leitura moderna: " + oc("Hélène Rey") + " (2013) argumenta que o ciclo financeiro global reduz a "
            "autonomia monetária mesmo sob câmbio flutuante (“dilema” em vez de trilema) — ponto bom para "
            "discursiva, mas não altera o gabarito de manual.",
            vm("Regra-âncora: o elemento “proibido” do trilema é o câmbio FIXO, não o flutuante."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca uma única palavra (fixo → flutuante). Pista: o câmbio "
                       "flutuante é justamente a válvula que permite combinar mobilidade de capitais e autonomia "
                       "monetária."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo trilema, um país com câmbio fixo e controles de capital pode conduzir política monetária "
            "autônoma.”</i> → CERTO",
            "<i>“Na zona do euro, cada país-membro mantém política monetária independente e livre mobilidade de "
            "capitais.”</i> → ERRADO (a política monetária é do BCE)",
        ]), ("🃏 Carta na manga", [
            "A escolha brasileira de 1999 — câmbio flutuante, metas de inflação e conta de capital aberta — é a "
            "aplicação direta do trilema: abrir mão da âncora cambial para recuperar a autonomia monetária."])],
        "reescrita": ("A “Trindade Impossível” postula que um país não pode manter simultaneamente câmbio "
                      + hl("fixo") + ", livre mobilidade de capitais e política monetária independente."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["simultaneamente"], "dificuldade": 1,
        "comentario_fonte": "O trilema envolve câmbio fixo; câmbio flutuante, mobilidade e política independente "
                            "são compatíveis (Brasil, EUA).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
