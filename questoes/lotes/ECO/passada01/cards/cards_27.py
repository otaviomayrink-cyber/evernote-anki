"""Cards da passada 01 de ECO — lote de redação 27 (cadernos E1 e E3, nota 16)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "agr": "🧭 Agregados e conceitos básicos",
}

CMD_FLUXO = "Julgue o item a seguir, relativo ao fluxo circular da renda."
CMD_AGR = "Julgue o item a seguir, relativo aos conceitos básicos da teoria macroeconômica."
CMD_NIDI = ("A compreensão da macroeconomia e dos seus agregados depende de algumas variáveis-chave, em especial, "
            "depende daquilo que alguns autores chamam de preços fundamentais, dentre os quais encontramos: i) a "
            "taxa de câmbio, o preço da moeda nacional em termos de moedas estrangeiras, ii) a taxa de juros, o "
            "preço intertemporal da moeda nacional em termos da própria moeda nacional, a iii) a taxa de lucro e "
            "outros. A respeito da taxa de câmbio e taxa de juros, julgue os itens a seguir (C ou E).")

CARDS = [
    # ------------------------------------------------------------------ E1-0396
    {
        "id": "ECO-E1-0396-1", "fonte_ref": "E1-0396", "destino": "16", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FLUXO,
        "rotulo_item": "Item",
        "assertiva": ("No fluxo de renda de uma economia, a organização do processo de produção que cria bens e "
                      "serviços é atribuída às famílias."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No fluxo de renda de uma economia, a organização do processo de produção que cria bens e "
                       "serviços é atribuída às ") + vm("famílias") + az(".")),
        "poucas": ("No fluxo circular, quem organiza a produção são as " + azb("empresas") + ". As "
                   + azb("famílias") + " são proprietárias dos fatores de produção e os oferecem às empresas, "
                   "recebendo em troca a renda com que consomem."),
        "destrinchando": [
            "O " + azb("fluxo circular da renda") + " é o modelo mais simples da economia: dois agentes "
            "(famílias e empresas) e dois mercados (de bens e serviços e de fatores de produção), ligados por "
            "dois fluxos em sentidos opostos.",
            azb("Fluxo real") + ": as famílias fornecem trabalho, capital e terra; as empresas combinam esses "
            "fatores e devolvem bens e serviços. " + azb("Fluxo monetário") + ": as empresas pagam salários, "
            "juros, aluguéis e lucros (a renda das famílias); as famílias gastam essa renda comprando a produção.",
            "Repartição de papéis: famílias = <b>donas</b> dos fatores e <b>consumidoras</b>; empresas = "
            "<b>organizadoras da produção</b> e <b>demandantes</b> de fatores. O lucro remunera justamente a "
            "capacidade empresarial, isto é, a função de organizar a produção e assumir seus riscos.",
            "Daí sai a igualdade que funda as contas nacionais: " + vd("produto = renda = despesa") + ". O valor "
            "do que as empresas produzem vira renda das famílias, que volta às empresas como despesa.",
            vm("Regra-âncora: famílias ofertam fatores e demandam bens; empresas demandam fatores e ofertam bens."),
        ],
        "dissecando": (cz("[troca de ator]") + " A definição da função (organizar a produção) está certa; o "
                       "item só trocou o agente. É a forma mais comum de cobrar o fluxo circular: inverter "
                       "quem oferta e quem demanda em cada mercado. Pista: “organizar a produção” é função "
                       "empresarial, remunerada pelo lucro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No fluxo circular, as famílias ofertam fatores de produção e demandam bens e serviços.”</i> → "
            "CERTO",
            "<i>“No fluxo circular, as empresas são as proprietárias dos fatores de produção que remuneram com "
            "salários, juros e aluguéis.”</i> → ERRADO (troca de ator: os fatores pertencem às famílias)",
        ])],
        "reescrita": ("No fluxo de renda de uma economia, a organização do processo de produção que cria bens e "
                      "serviços é atribuída às " + hl("empresas") + "."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. As famílias são, no fluxo circular da renda, fornecedoras de fatores de "
                             "produção (como trabalho, capital e terra), mas não organizam o processo produtivo."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0397-1 traz a mesma assertiva com “empresas” no lugar de “famílias” "
                    "(gabarito CERTO); mantidos os dois"],
    },
    # ------------------------------------------------------------------ E1-0397
    {
        "id": "ECO-E1-0397-1", "fonte_ref": "E1-0397", "destino": "16", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FLUXO,
        "rotulo_item": "Item",
        "assertiva": ("No fluxo de renda de uma economia, a organização do processo de produção que cria bens e "
                      "serviços é atribuída às empresas."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No fluxo de renda de uma economia, a organização do processo de produção que cria bens e "
                      "serviços é atribuída às <u>empresas</u>."),
        "poucas": ("As " + azb("empresas") + " contratam os fatores fornecidos pelas famílias, combinam-nos e "
                   "produzem bens e serviços: organizar a produção é a função delas no fluxo circular."),
        "destrinchando": [
            "No " + azb("mercado de fatores") + ", as empresas são demandantes (contratam trabalho, capital e "
            "terra) e as famílias, ofertantes. No " + azb("mercado de bens e serviços") + ", os papéis se "
            "invertem: empresas ofertam, famílias demandam.",
            "Cada fator recebe sua remuneração: trabalho → " + vd("salário") + "; capital → " + vd("juros")
            + "; terra → " + vd("aluguel") + "; capacidade empresarial → " + vd("lucro") + ". A soma dessas "
            "remunerações é a renda das famílias, que retorna às empresas como despesa de consumo.",
            "A expressão “empresa” no modelo é funcional: designa a unidade que decide o que, como e quanto "
            "produzir. Um trabalhador autônomo, nesse papel, age como empresa; na hora de consumir, como família.",
            "Ampliações do modelo acrescentam o " + azb("governo") + " (tributos e gastos), o "
            + azb("setor financeiro") + " (poupança e investimento) e o " + azb("setor externo")
            + " (exportações e importações) — vazamentos e injeções que levam ao Y = C + I + G + (X − M).",
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual, sem modulador. O risco está no item "
                       "espelho, com “famílias”, que circula na mesma bateria: decore o par “empresas "
                       "organizam / famílias fornecem fatores”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a organização do processo de produção é atribuída às famílias, proprietárias dos fatores.”</i> "
            "→ ERRADO (troca de ator: famílias fornecem fatores, não organizam a produção)",
            "<i>“No mercado de fatores de produção, as empresas atuam como demandantes.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. As empresas são as responsáveis por organizar o processo produtivo, "
                             "utilizando os fatores de produção fornecidos pelas famílias para produzir bens e "
                             "serviços."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0396-1 traz a mesma assertiva com “famílias” (gabarito ERRADO); "
                    "mantidos os dois"],
    },
    # ------------------------------------------------------------------ E1-0402
    {
        "id": "ECO-E1-0402-1", "fonte_ref": "E1-0402", "destino": "16", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_FLUXO,
        "rotulo_item": "Item",
        "assertiva": ("Uma forma de compreendermos o funcionamento de uma economia se dá por meio do chamado "
                      "“fluxo circular da renda”, em que os entes da sociedade se organizam como produtores e "
                      "como consumidores."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma forma de compreendermos o funcionamento de uma economia se dá por meio do chamado "
                      "“fluxo circular da renda”, em que os entes da sociedade se organizam <u>como produtores e "
                      "como consumidores</u>."),
        "poucas": ("O " + azb("fluxo circular da renda") + " é um modelo simplificado da economia em que os "
                   "agentes aparecem em dois papéis interdependentes: produtores (empresas) e consumidores "
                   "(famílias), ligados pelos mercados de bens e de fatores."),
        "destrinchando": [
            "Como todo modelo, o fluxo circular simplifica: na versão básica há só famílias e empresas, sem "
            "governo, sem setor externo e sem poupança. Tudo o que se produz é vendido, e toda a renda é gasta.",
            "Os dois circuitos correm em sentidos opostos: o " + azb("real") + " (fatores → empresas; bens e "
            "serviços → famílias) e o " + azb("monetário") + " (renda → famílias; gasto de consumo → "
            "empresas). Cada fluxo monetário paga um fluxo real.",
            "O papel do mesmo agente muda conforme o mercado: a família é <b>ofertante</b> no mercado de "
            "fatores e <b>demandante</b> no de bens; a empresa, o inverso. Por isso o item fala em entes que "
            "“se organizam como produtores e como consumidores”.",
            "A lição macroeconômica é a " + azb("interdependência") + ": o gasto de um agente é a renda de "
            "outro. Daí a identidade " + vd("produto ≡ renda ≡ despesa") + " e a intuição keynesiana de que "
            "uma queda do gasto reduz a renda e realimenta a queda do gasto.",
            "Ampliado, o modelo ganha " + azb("vazamentos") + " (poupança, tributos, importações) e "
            + azb("injeções") + " (investimento, gastos do governo, exportações); no equilíbrio, vazamentos = "
            "injeções.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Definição genérica, sem modulador restritivo. A expressão "
                       "“uma forma de compreendermos” relativiza o modelo, o que protege o item. O erro, quando "
                       "a banca quer, costuma vir na troca de papéis (empresas consumindo fatores × famílias "
                       "organizando a produção) ou na omissão de um dos fluxos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No fluxo circular da renda, o fluxo monetário e o fluxo real correm no mesmo sentido.”</i> → "
            "ERRADO (inversão: correm em sentidos opostos)",
            "<i>“No modelo básico do fluxo circular, a renda das famílias corresponde ao valor da produção das "
            "empresas.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("CERTO. No modelo do fluxo circular da renda, os agentes econômicos (famílias e "
                             "empresas) atuam de forma interdependente: as famílias consomem bens e serviços e "
                             "oferecem fatores de produção, enquanto as empresas produzem e demandam os fatores."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0413
    {
        "id": "ECO-E1-0413-1", "fonte_ref": "E1-0413", "destino": "16", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_AGR,
        "rotulo_item": "Item",
        "assertiva": ("Despesa agregada ou demanda agregada é o total de gastos realizados por todos os agentes "
                      "econômicos (famílias, empresas, governo e setor externo) em uma economia durante um "
                      "determinado período de tempo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Despesa agregada ou demanda agregada é o total de gastos realizados por <u>todos os agentes "
                      "econômicos (famílias, empresas, governo e setor externo)</u> em uma economia durante um "
                      "determinado período de tempo."),
        "poucas": ("A " + azb("despesa (demanda) agregada") + " soma os gastos dos quatro setores com bens e "
                   "serviços produzidos no país num período: " + vd("DA = C + I + G + (X − M)") + "."),
        "destrinchando": [
            "Cada agente responde por um componente: " + azb("famílias") + " → consumo (C); "
            + azb("empresas") + " → investimento (I: máquinas, construções, variação de estoques); "
            + azb("governo") + " → gastos com bens e serviços (G); " + azb("setor externo") + " → exportações "
            "(X), das quais se subtraem as importações (M).",
            "Por que subtrair M? Parte de C, I e G é gasto com bens estrangeiros, que não remunera produção "
            "doméstica. Ao descontar M, a despesa agregada mede só a demanda dirigida ao produto do país.",
            "Ficam de fora as " + azb("transferências") + " (aposentadorias, Bolsa Família, juros da dívida): "
            "elas mudam a renda disponível, mas não são compra de bens e serviços — por isso não entram em G.",
            "É uma variável " + azb("fluxo") + " (medida num intervalo: trimestre, ano), não estoque. Na "
            "contabilidade nacional, despesa agregada = produto (identidade ex post); no modelo keynesiano, a "
            "despesa <b>planejada</b> determina o produto de equilíbrio (cruz keynesiana).",
            vm("Regra-âncora: DA = C + I + G + X − M — gasto em bens e serviços finais, nunca transferências."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição de manual. O “todos os agentes” poderia soar como "
                       "modulador absoluto, mas é exato: a despesa agregada inclui de fato os quatro setores. "
                       "Para virar ERRADO, a banca costuma excluir um setor, somar as importações em vez de "
                       "subtraí-las ou incluir transferências em G."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A demanda agregada corresponde à soma do consumo, do investimento, dos gastos do governo, das "
            "exportações e das importações.”</i> → ERRADO (sinal trocado: as importações são subtraídas)",
            "<i>“As transferências de renda do governo às famílias integram diretamente a variável G da "
            "demanda agregada.”</i> → ERRADO (troca de conceito: transferência não é compra de bem ou serviço)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["todos"], "dificuldade": 1,
        "comentario_fonte": ("CERTO. A demanda agregada representa a soma dos gastos de consumo das famílias (C), "
                             "investimentos das empresas (I), gastos do governo (G) e saldo do setor externo "
                             "(X − M). A equação é: DA = C + I + G + (X − M)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0503
    {
        "id": "ECO-E1-0503-1", "fonte_ref": "E1-0503", "destino": "16", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Clio", "prova": "04/2022", "ano": 2022, "cacd": False, "errei": False,
        "comando": CMD_AGR,
        "rotulo_item": "Item",
        "assertiva": ("A elevação do Hiato do Produto significa que o PIB de uma economia está se distanciando de "
                      "seu PIB de pleno emprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("A <u>elevação</u> do Hiato do Produto significa que o PIB de uma economia está se "
                      "distanciando de seu PIB de pleno emprego."),
        "poucas": ("O " + azb("hiato do produto") + " é a distância entre o PIB efetivo e o "
                   + azb("PIB potencial") + " (o de pleno emprego dos fatores, sem pressão inflacionária). Hiato "
                   "maior = PIB mais longe do potencial."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O item é CERTO se “elevação” significar aumento do <b>tamanho</b> do hiato (em módulo). "
                          "Com o hiato medido com sinal, (Y − Y*)/Y*, um hiato negativo que “se eleva” de −3% "
                          "para −1% indica PIB se <b>aproximando</b> do potencial. A banca adotou a leitura em "
                          "módulo; mantém-se o CERTO.")],
        "destrinchando": [
            "Definição usual: " + vd("hiato = (Y − Y*) / Y*") + ", em que Y é o PIB efetivo e Y* o "
            + azb("PIB potencial") + " — o máximo que a economia produz de forma sustentada, com os fatores "
            "plenamente empregados e sem acelerar a inflação.",
            azb("Hiato negativo") + " (Y < Y*): ociosidade, desemprego acima do natural, pressão "
            "desinflacionária — espaço para política expansionista. " + azb("Hiato positivo")
            + " (Y > Y*): economia “superaquecida”, mercado de trabalho apertado, pressão inflacionária — "
            "indicação de aperto monetário.",
            "Por isso o hiato entra nas regras de política monetária: na " + azb("regra de Taylor") + " ("
            + oc("John Taylor") + ", 1993), os juros sobem com a inflação acima da meta e com o hiato positivo. "
            + rx("O Banco Central do Brasil") + " estima o hiato e o usa nas projeções do Copom.",
            "O PIB potencial <b>não é observável</b>: é estimado por filtros estatísticos ou função de "
            "produção, e as estimativas são revistas. Por isso o hiato é sempre uma medida incerta.",
            "A relação entre hiato e desemprego é a " + azb("lei de Okun") + " (" + oc("Arthur Okun")
            + "): o desemprego cai quando o produto cresce acima do potencial.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A banca define o hiato pelo afastamento e usa "
                       "“PIB de pleno emprego” como sinônimo de PIB potencial — aceitável em prova. O risco "
                       "está no sinal: quem pensa no hiato negativo “subindo” rumo a zero marca ERRADO. Leia "
                       "“elevação do hiato” como hiato maior em módulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um hiato do produto positivo indica capacidade ociosa e pressão desinflacionária.”</i> → "
            "ERRADO (inversão: isso descreve o hiato negativo)",
            "<i>“O PIB potencial é diretamente observado nas contas nacionais trimestrais do IBGE.”</i> → "
            "ERRADO (o potencial é estimado, não observado)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("CERTO. Hiato do produto é a diferença entre o PIB corrente e o PIB potencial; pode "
                             "ser positivo ou negativo e indica pressões inflacionárias. O item é correto desde "
                             "que o hiato seja positivo; se negativo, há ociosidade."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: “elevação do hiato” só significa afastamento do potencial se o hiato for lido "
                    "em módulo ou for positivo; com hiato negativo, elevação = aproximação. Gabarito da fonte "
                    "(CERTO) mantido",
                    "texto_corrigido: a frente vinha em forma de pergunta (“É correto afirmar que …?”); a "
                    "assertiva foi extraída das aspas"],
    },
    # ------------------------------------------------------------------ E3-L00314
    {
        "id": "ECO-E3-L00314-1", "fonte_ref": "E3-L00314", "destino": "16", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("A taxa de juros nominal é diferente da taxa de juros real, na medida em que se desconta a "
                      "taxa de inflação da primeira para chegarmos à segunda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A taxa de juros nominal é diferente da taxa de juros real, na medida em que <u>se desconta "
                      "a taxa de inflação da primeira para chegarmos à segunda</u>."),
        "poucas": ("Juro " + azb("real") + " = juro " + azb("nominal") + " descontada a inflação. Pela "
                   + azb("equação de Fisher") + ", " + vd("i ≈ r + π") + ", logo " + vd("r ≈ i − π") + "."),
        "destrinchando": [
            "O " + azb("juro nominal") + " (i) é o contratado em moeda: quanto o credor recebe a mais em reais. "
            "O " + azb("juro real") + " (r) mede o ganho de <b>poder de compra</b>: quanto a mais de bens o "
            "credor poderá comprar.",
            "Forma exata (" + oc("Irving Fisher") + "): " + vd("(1 + i) = (1 + r)(1 + π)") + ". A aproximação "
            + vd("i ≈ r + π") + " só vale bem para taxas baixas. Ex.: i = 15% e π = 5% → r exato = 1,15/1,05 − 1 "
            "≈ " + vd("9,5%") + " (a aproximação dá 10%).",
            azb("Ex ante × ex post") + ": o juro real esperado usa a inflação esperada (i − π<sup>e</sup>) e "
            "guia decisões de investimento e poupança; o realizado usa a inflação efetiva. Se a inflação "
            "surpreende para cima, o devedor ganha e o credor perde.",
            azb("Efeito Fisher") + ": no longo prazo, uma alta de 1 ponto na inflação esperada tende a elevar "
            "o juro nominal em 1 ponto, deixando o real inalterado.",
            "No " + rx("Brasil") + ", o juro real ex ante costuma ser medido pela taxa do swap pré-DI de 360 "
            "dias deflacionada pela inflação esperada do Boletim Focus.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item descreve em palavras a equação de Fisher, sem se "
                       "comprometer com a forma exata ou aproximada (“desconta” cobre as duas). O ERRADO "
                       "viria invertendo o sentido (descontar a inflação do juro real para chegar ao nominal) "
                       "ou somando a inflação ao nominal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para obter a taxa de juros nominal, desconta-se a inflação da taxa de juros real.”</i> → "
            "ERRADO (inversão: o nominal é o real acrescido da inflação)",
            "<i>“Se a inflação efetiva superar a esperada, os devedores com contratos prefixados são "
            "beneficiados.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "CERTO. Fórmula em imagem: i = r + π (i = juros nominais; r = juros reais; π = inflação).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 442", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": ["texto_corrigido: a transcrição da IMAGEM 442 traz “i = r + 7” e “7 = inflação”; o “7” é "
                    "erro de OCR para π"],
    },
    # ------------------------------------------------------------------ E3-L00315
    {
        "id": "ECO-E3-L00315-1", "fonte_ref": "E3-L00315", "destino": "16", "subtema": H2["agr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("Ao avaliarmos a equação do PIB de uma economia com governo e comércio internacional, "
                      "Y = C + I + G + (X - M), o principal efeito das variações taxa de câmbio é sentido na "
                      "variável de investimento agregado (I) e nos gastos do governo (G)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Ao avaliarmos a equação do PIB de uma economia com governo e comércio internacional, "
                       "Y = C + I + G + (X - M), o principal efeito das variações taxa de câmbio é sentido ")
                    + vm("na variável de investimento agregado (I) e nos gastos do governo (G)") + az(".")),
        "poucas": ("O câmbio é o preço relativo entre bens nacionais e estrangeiros: seu efeito direto e "
                   "principal recai sobre as " + azb("exportações líquidas (X − M)") + ". Em I e G, os efeitos "
                   "são indiretos e secundários."),
        "destrinchando": [
            "No modelo de economia aberta, cada componente tem seu determinante principal: C depende da renda "
            "disponível, " + vd("C = c₀ + c(Y − T)") + "; I, dos juros, " + vd("I = I₀ − b·i") + "; G é "
            "decisão de política fiscal (exógeno); e as exportações líquidas dependem da renda doméstica, da "
            "renda externa e do câmbio real: " + vd("NX = f(Y, Y*, e)") + ".",
            azb("Depreciação real") + " (moeda nacional mais fraca): o produto nacional fica mais barato lá "
            "fora (X ↑) e o importado fica mais caro aqui (M ↓) → NX ↑ → demanda agregada ↑ (a IS se desloca "
            "para a direita). " + azb("Apreciação") + ": o inverso.",
            "Duas ressalvas de prova: a " + azb("condição de Marshall-Lerner") + " (a desvalorização só "
            "melhora o saldo se a soma das elasticidades-preço de exportações e importações, em módulo, for "
            "maior que 1) e a " + azb("curva J") + " (no curtíssimo prazo o saldo piora, porque as quantidades "
            "contratadas demoram a reagir enquanto o importado já ficou mais caro).",
            "Os canais sobre I e G existem, mas são de segunda ordem: a depreciação encarece máquinas "
            "importadas e pode levar o banco central a subir juros contra a inflação (afetando I); pode "
            "encarecer a dívida pública em moeda estrangeira ou as compras externas do governo (afetando G "
            "só se o orçamento reagir). Nenhum é automático como o efeito sobre X e M.",
            vm("Regra-âncora: câmbio → exportações líquidas (X − M); juros → investimento (I); orçamento → G."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A identidade Y = C + I + G + (X − M) está certa; o item "
                       "troca o canal de transmissão do câmbio, atribuindo a I e G o que pertence a X − M. A "
                       "pista é a própria definição do comando: câmbio é “o preço da moeda nacional em termos "
                       "de moedas estrangeiras”, ou seja, mexe no que se troca com o exterior."),
        "modulos": [
            ("😈 Para dificultar", [
                "<i>“…o principal efeito das variações da taxa de câmbio é sentido nas exportações líquidas "
                "(X − M).”</i> → CERTO",
                "<i>“Uma depreciação cambial sempre melhora imediatamente o saldo comercial.”</i> → ERRADO "
                "(modulador absoluto: curva J e condição de Marshall-Lerner)",
            ]),
            ("🃏 Carta na manga", [
                "Em regime de câmbio flutuante (adotado pelo " + rx("Brasil") + " desde janeiro de 1999), o "
                "câmbio é o principal mecanismo de ajuste externo: ao depreciar, desloca demanda para o "
                "produto doméstico e corrige o saldo comercial.",
            ]),
        ],
        "reescrita": ("Ao avaliarmos a equação do PIB de uma economia com governo e comércio internacional, "
                      "Y = C + I + G + (X - M), o principal efeito das variações taxa de câmbio é sentido "
                      + hl("nas exportações líquidas (X − M)") + "."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["principal"], "dificuldade": 1,
        "comentario_fonte": ("ERRADO. Quatro respostas de IA concordantes: o câmbio altera preços relativos e "
                             "afeta direta e principalmente X e M (exportações líquidas); efeitos em I e G são "
                             "indiretos (custo de bens de capital importados, juros, dívida externa). Menções a "
                             "Marshall-Lerner, curva J e Mundell-Fleming."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 443", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": ["qualidade_fonte: uma das respostas da fonte atribui a Harrod e Domar a adaptação de "
                    "Y = C + I + G + (X − M) à economia aberta e traz percentuais do FMI e do BCB sem fonte "
                    "verificável; descartados",
                    "texto_corrigido: a transcrição da IMAGEM 443 está truncada (“Y=C+HI+G”, “J=] — bi”); "
                    "lidas como Y = C + I + G + (X − M) e I = I₀ − b·i"],
    },
]
