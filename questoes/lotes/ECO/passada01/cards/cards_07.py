"""Cards do lote de redação 07 — ECO, passada 01 (caderno E1, linhas 0135–0168).

Nota de destino: 03 — Intervenções do Estado na economia e economia do bem-estar.
"""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "efi": "😊 Excedentes e eficiência",
    "trib": "💸 Tributos: incidência e peso morto",
    "sub": "🧾 Subsídios",
    "teto": "🚧 Preços máximos e mínimos",
}

COM_PARETO = "Julgue o item a seguir, relativo à eficiência de Pareto e à economia do bem-estar."
COM_TEOREMAS = "Julgue o item a seguir, relativo aos teoremas fundamentais da economia do bem-estar."
COM_HIPOTESES = "Julgue o item a seguir, acerca das hipóteses do Segundo Teorema do Bem-Estar."
COM_TRIB = "Julgue o item a seguir, relativo à incidência de tributos e ao peso morto."


def card(rid, h2, comando, **kw):
    """Campos comuns do lote (caderno E1, banca não identificada, sem órgão nem ano)."""
    base = {
        "id": f"ECO-{rid}-1", "fonte_ref": rid, "destino": "03", "subtema": H2[h2],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False, "comando": comando, "rotulo_item": "Item",
        "gabarito_origem": "fonte", "status": "normal", "modulos": [], "moduladores": [],
        "figuras_fonte": [], "alertas": [],
    }
    base.update(kw)
    return base


def img_verso(ref, nota=""):
    return {"ref": ref, "tipo_fonte": "desconhecido", "lado": "verso",
            "acao": "irrecuperavel" + (f" ({nota})" if nota else " (imagem do verso não preservada no caderno E1)")}


CARDS = [
    # ------------------------------------------------------------------ E1-0135
    card(
        "E1-0135", "efi", "Julgue o item a seguir, relativo a excedentes e eficiência de mercado.",
        assertiva=("O peso morto faz com que a quantidade transacionada seja maior que a quantidade esperada "
                   "para se obter o ótimo social."),
        gabarito="ERRADO",
        anotada=(az("O peso morto ") + vm("faz com que") + az(" a quantidade transacionada seja ") + vm("maior")
                 + az(" que a quantidade esperada para se obter o ótimo social.")),
        poucas=("O " + azb("peso morto") + " é a <b>consequência</b> de transacionar uma quantidade diferente "
                "da ótima — e, no caso típico (tributo, monopólio, tabelamento), uma quantidade " + vd("menor")
                + " que a do ótimo social, não maior."),
        destrinchando=[
            azb("Peso morto") + " (<i>deadweight loss</i>) = perda líquida de excedente total (consumidor + "
            "produtor + governo) em relação ao equilíbrio eficiente. São as trocas mutuamente vantajosas que "
            "deixam de acontecer — ou as que acontecem sem valer o que custam.",
            "O ótimo social está onde o benefício marginal (demanda) iguala o custo marginal (oferta): "
            + vd("q*") + ". Qualquer distorção que afaste a quantidade de q* gera peso morto.",
            "Caso clássico — " + azb("subprodução") + ": tributo, monopólio, preço máximo ou mínimo efetivo, "
            "cota. Transaciona-se <b>menos</b> que q*: unidades cujo valor para o comprador supera o custo do "
            "vendedor deixam de ser trocadas (triângulo entre as curvas, à esquerda de q*).",
            "Caso espelho — " + azb("superprodução") + ": subsídio ou externalidade negativa não corrigida. "
            "Transaciona-se <b>mais</b> que q*: unidades custam mais do que valem, e o peso morto fica à "
            "direita de q*. Por isso não é exato dizer que peso morto “só” existe com subprodução.",
            "Note a ordem causal: a distorção (imposto, poder de mercado) altera a quantidade, e a perda de "
            "eficiência resulta disso. O peso morto não “faz” a quantidade mudar; ele <b>mede</b> o custo dessa "
            "mudança.",
            vm("Regra-âncora: peso morto = excedente perdido por afastar-se de q*; no tributo e no monopólio, "
               "q < q*."),
        ],
        dissecando=(cz("[inversão · nexo indevido]") + " Duas trocas empilhadas: o sentido da distorção "
                    "(“maior” no lugar de “menor”, no caso típico) e a causalidade (o peso morto apresentado como "
                    "causa da quantidade, quando é seu efeito). Pista: o item fala em peso morto em abstrato — a "
                    "referência implícita é o tributo, em que a quantidade cai."),
        modulos=[("😈 Para dificultar", [
            "<i>“Um subsídio gera peso morto ao elevar a quantidade transacionada acima do ótimo social.”</i> → "
            "CERTO",
            "<i>“O peso morto de um tributo corresponde à receita arrecadada pelo governo.”</i> → ERRADO (a "
            "receita é transferência; o peso morto é o triângulo que ninguém recebe)",
        ])],
        reescrita=("O peso morto " + hl("resulta de") + " a quantidade transacionada " + hl("ser menor")
                   + " que a quantidade esperada para se obter o ótimo social" + hl(", como ocorre com "
                   "tributos e monopólio") + "."),
        tipo_erro=["INVERSAO", "NEXO_INDEVIDO"], dificuldade=1,
        comentario_fonte=("ERRADO. O peso morto ocorre quando há subprodução, ou seja, a quantidade transacionada "
                          "é menor que a do ótimo social."),
        qualidade_fonte="com_erro",
        alertas=["qualidade_fonte: o comentário de origem restringe o peso morto à subprodução; subsídios e "
                 "externalidades negativas geram peso morto com superprodução — corrigido no 📖"],
    ),
    # ------------------------------------------------------------------ E1-0136
    card(
        "E1-0136", "efi", COM_PARETO,
        assertiva=("Em teoria, se for possível uma combinação de fatores de produção de forma a melhorar a "
                   "situação de vários indivíduos, mesmo que isso implique em piorar, concomitante, uma "
                   "quantidade menor de outros indivíduos, tem-se uma melhoria de Pareto."),
        gabarito="ERRADO",
        anotada=(az("Em teoria, se for possível uma combinação de fatores de produção de forma a melhorar a "
                    "situação de vários indivíduos, ") + vm("mesmo que isso implique em piorar, concomitante, "
                    "uma quantidade menor de outros indivíduos") + az(", tem-se uma melhoria de Pareto.")),
        poucas=("Uma " + azb("melhoria de Pareto") + " exige que " + vd("ninguém piore") + ". Se alguém "
                "perde — por menor que seja o grupo —, a mudança pode até ser desejável por outro critério, "
                "mas não é Pareto."),
        destrinchando=[
            azb("Melhoria de Pareto") + ": mudança que melhora pelo menos um indivíduo sem piorar nenhum. "
            + azb("Eficiência (ótimo) de Pareto") + ": situação em que não resta nenhuma melhoria de Pareto "
            "possível.",
            "O critério é deliberadamente <b>fraco</b> e <b>unânime</b>: não pesa ganhos contra perdas nem conta "
            "cabeças. Basta um perdedor para que a mudança deixe de ser melhoria de Pareto — não importa se os "
            "ganhadores são a maioria ou se ganham muito mais do que o perdedor perde.",
            "Para comparar mudanças com ganhadores e perdedores existe o " + azb("critério de compensação de "
            "Kaldor-Hicks") + " (" + oc("Kaldor") + " e " + oc("Hicks") + ", 1939): a mudança é eficiente se os "
            "ganhadores <i>pudessem</i> compensar os perdedores e ainda sair ganhando — mesmo que a "
            "compensação não seja paga. É a lógica da análise custo-benefício.",
            "Exemplo: abrir um mercado à importação barateia o bem para milhões de consumidores e prejudica "
            "alguns produtores domésticos. Pode passar no teste de Kaldor-Hicks; não é melhoria de Pareto.",
            vm("Regra-âncora: melhoria de Pareto = alguém melhora e ninguém piora. Um perdedor basta para "
               "descaracterizá-la."),
        ],
        dissecando=(cz("[meia-verdade · troca de conceito]") + " A primeira parte (melhorar vários "
                    "indivíduos) é compatível com Pareto; o erro foi enxertado na concessiva “mesmo que isso "
                    "implique em piorar”. O “quantidade menor de outros” tenta seduzir com a lógica da maioria "
                    "— que é Kaldor-Hicks ou utilitarismo, não Pareto."),
        modulos=[("😈 Para dificultar", [
            "<i>“Uma mudança que beneficia a maioria e prejudica uma minoria pode ser eficiente pelo critério "
            "de Kaldor-Hicks, mas não constitui melhoria de Pareto.”</i> → CERTO",
            "<i>“Uma melhoria de Pareto exige que todos os indivíduos melhorem.”</i> → ERRADO (basta um "
            "melhorar sem que ninguém piore)",
        ])],
        reescrita=("Em teoria, se for possível uma combinação de fatores de produção de forma a melhorar a "
                   "situação de vários indivíduos, " + hl("sem piorar a de nenhum outro") + ", tem-se uma "
                   "melhoria de Pareto."),
        tipo_erro=["MEIA_VERDADE", "TROCA_CONCEITO"], dificuldade=1,
        comentario_fonte=("ERRADO. A melhoria de Pareto ocorre somente quando alguém melhora sem que ninguém "
                          "piore. Se alguém é prejudicado, mesmo que outros ganhem, não se trata de uma melhoria "
                          "de Pareto."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0137
    card(
        "E1-0137", "efi", COM_PARETO,
        assertiva=("Se uma alocação de fatores de produção permitir uma melhoria de Pareto, então ela é "
                   "eficiente no sentido de Pareto."),
        gabarito="ERRADO",
        anotada=(az("Se uma alocação de fatores de produção permitir uma melhoria de Pareto, então ela ")
                 + vm("é eficiente") + az(" no sentido de Pareto.")),
        poucas=("É o contrário: se ainda cabe uma " + azb("melhoria de Pareto") + ", há ganho desperdiçado e a "
                "alocação é " + vd("ineficiente") + ". Eficiente é a alocação que não admite mais nenhuma."),
        destrinchando=[
            "Os dois conceitos se definem um pelo outro: uma alocação é " + azb("Pareto-eficiente") + " se e "
            "somente se <b>não existe</b> melhoria de Pareto a partir dela. Logo, “permite melhoria de Pareto” "
            "é exatamente a definição de " + azb("Pareto-ineficiente") + ".",
            "Na produção, a eficiência de Pareto significa estar sobre a " + azb("fronteira de possibilidades "
            "de produção") + ": não dá para produzir mais de um bem sem produzir menos de outro. Um ponto "
            "<b>dentro</b> da fronteira (fatores ociosos ou mal combinados) permite produzir mais de tudo — há "
            "melhoria de Pareto, e ele é ineficiente.",
            "Condição técnica correspondente: a " + azb("taxa marginal de substituição técnica") + " entre "
            "capital e trabalho deve ser igual em todas as indústrias (pontos da curva de contrato na caixa de "
            "Edgeworth da produção).",
            "Ideia útil para itens de pegadinha: eficiência é um conceito de <b>ausência</b> (não há mais o que "
            "melhorar sem custo para alguém). Tudo o que “ainda permite” ganho é, por definição, ineficiente.",
        ],
        dissecando=(cz("[inversão]") + " O item inverte a relação lógica entre os conceitos: “permite "
                    "melhoria” → “é eficiente”, quando permitir melhoria é o próprio critério de "
                    "ineficiência. Pista: o “se…, então…” liga uma condição à classificação errada."),
        modulos=[("😈 Para dificultar", [
            "<i>“Se nenhuma realocação dos fatores de produção permite aumentar a produção de um bem sem "
            "reduzir a de outro, a alocação é eficiente no sentido de Pareto.”</i> → CERTO",
            "<i>“Um ponto no interior da fronteira de possibilidades de produção é Pareto-eficiente, pois é "
            "factível.”</i> → ERRADO (factível não é eficiente: dentro da fronteira há melhoria possível)",
        ])],
        reescrita=("Se uma alocação de fatores de produção permitir uma melhoria de Pareto, então ela "
                   + hl("não é eficiente") + " no sentido de Pareto."),
        tipo_erro=["INVERSAO"], dificuldade=1,
        comentario_fonte=("ERRADO. Se ainda é possível uma melhoria de Pareto, a alocação não é eficiente. A "
                          "eficiência de Pareto ocorre quando não é mais possível beneficiar alguém sem "
                          "prejudicar outro."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0138
    card(
        "E1-0138", "efi", COM_PARETO,
        assertiva=("Uma alocação ineficiente no sentido de Pareto tem a característica indesejável de que não há "
                   "qualquer possibilidade de melhorar a situação de alguém sem prejudicar ninguém mais."),
        gabarito="ERRADO",
        anotada=(az("Uma alocação ineficiente no sentido de Pareto tem a característica indesejável de que ")
                 + vm("não há qualquer possibilidade") + az(" de melhorar a situação de alguém sem prejudicar "
                 "ninguém mais.")),
        poucas=("O item descreve a alocação " + azb("eficiente") + ". Na " + azb("ineficiente") + ", "
                + vd("existe") + " ao menos um modo de melhorar alguém sem prejudicar ninguém — é isso que a "
                "torna ineficiente."),
        destrinchando=[
            "Definições espelhadas: " + azb("Pareto-eficiente") + " → não há como melhorar alguém sem piorar "
            "outro. " + azb("Pareto-ineficiente") + " → há pelo menos uma realocação que melhora alguém sem "
            "piorar ninguém (uma melhoria de Pareto disponível).",
            "O “característica indesejável” também é pista falsa: o indesejável na ineficiência é justamente "
            "<b>haver</b> ganho sem custo sendo desperdiçado — dinheiro deixado na mesa.",
            "Exemplos de ineficiência: desemprego involuntário (fatores ociosos), trocas mutuamente vantajosas "
            "impedidas por um tributo (peso morto), produção dentro da fronteira de possibilidades de produção, "
            "dois consumidores com taxas marginais de substituição diferentes que ainda não trocaram entre si.",
            "Em geral há <b>infinitas</b> alocações eficientes (toda a curva de contrato), algumas muito "
            "desiguais. Eficiência não diz qual delas é a melhor socialmente.",
        ],
        dissecando=(cz("[troca de conceito]") + " O item cola a definição de eficiência no rótulo de "
                    "ineficiência. A negação dupla (“não há qualquer possibilidade… sem prejudicar ninguém”) "
                    "embaralha a leitura: reescreva em positivo antes de julgar."),
        modulos=[("😈 Para dificultar", [
            "<i>“Em uma alocação Pareto-ineficiente, existe ao menos uma realocação que melhora a situação de "
            "alguém sem piorar a de ninguém.”</i> → CERTO",
            "<i>“Em uma alocação Pareto-ineficiente, qualquer realocação que melhore alguém necessariamente "
            "piora outro.”</i> → ERRADO (descreve a alocação eficiente)",
        ])],
        reescrita=("Uma alocação ineficiente no sentido de Pareto tem a característica indesejável de que "
                   + hl("há ao menos uma possibilidade") + " de melhorar a situação de alguém sem prejudicar "
                   "ninguém mais."),
        tipo_erro=["TROCA_CONCEITO"], dificuldade=1,
        comentario_fonte=("ERRADO. Isso descreve a eficiência, e não a ineficiência. Uma alocação ineficiente de "
                          "Pareto é justamente aquela em que ainda há espaço para melhorar alguém sem piorar "
                          "ninguém."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0139
    card(
        "E1-0139", "efi", COM_PARETO,
        assertiva=("Na economia das trocas, a alocação eficiente de Pareto é a situação em que ninguém consegue "
                   "aumentar o próprio bem-estar sem reduzir o bem-estar de outra pessoa."),
        gabarito="CERTO",
        anotada=az("Na economia das trocas, a alocação eficiente de Pareto é a situação em que ninguém consegue "
                   "aumentar o próprio bem-estar <u>sem reduzir o bem-estar de outra pessoa</u>."),
        poucas=("É a definição de " + azb("eficiência de Pareto") + " aplicada à troca: esgotadas as trocas "
                "mutuamente vantajosas, qualquer ganho de um passa a custar a outro."),
        destrinchando=[
            "Na " + azb("economia de trocas pura") + " não há produção: dois consumidores dividem quantidades "
            "fixas de dois bens. O instrumento é a " + azb("caixa de Edgeworth") + ", com a origem de um "
            "consumidor no canto inferior esquerdo e a do outro no superior direito.",
            "Condição de eficiência na troca: " + vd("TMS<sub>A</sub> = TMS<sub>B</sub>") + " (curvas de "
            "indiferença tangentes). Se as taxas diferem, cada um valoriza mais o bem que o outro valoriza "
            "menos — há troca que melhora os dois.",
            "O conjunto de todas as alocações eficientes é a " + azb("curva de contrato") + ". Sobre ela, "
            "mover-se em direção à origem de B melhora A e piora B, e vice-versa.",
            "Eficiência é um dos três “andares” do ótimo de Pareto em equilíbrio geral: eficiência na "
            "<b>troca</b> (TMS iguais entre consumidores), na <b>produção</b> (TMST iguais entre indústrias) e "
            "no <b>mix de produtos</b> (TMS = taxa marginal de transformação).",
        ],
        dissecando=(cz("[literalidade]") + " Reprodução quase literal da definição de manual (" + oc("Pindyck")
                    + " e " + oc("Rubinfeld") + ", capítulo de equilíbrio geral). O risco é o leitor achar que eficiência exige que "
                    "<i>ninguém</i> possa melhorar de forma alguma — a cláusula decisiva é “sem reduzir o "
                    "bem-estar de outra pessoa”."),
        modulos=[("😈 Para dificultar", [
            "<i>“Na economia das trocas, a alocação eficiente de Pareto é aquela em que as taxas marginais de "
            "substituição dos consumidores entre os dois bens são iguais.”</i> → CERTO",
            "<i>“Na economia das trocas, a alocação eficiente de Pareto é única e corresponde à divisão "
            "igualitária dos bens.”</i> → ERRADO (há infinitas, sobre toda a curva de contrato)",
        ])],
        tipo_erro=["LITERAL"], dificuldade=1,
        comentario_fonte=("CERTO. Essa é a definição clássica de eficiência de Pareto: um estado em que não é "
                          "possível melhorar alguém sem piorar outra pessoa. [imagem]"),
        qualidade_fonte="raso",
        figuras_fonte=[img_verso("Untitled (32).jpeg")],
    ),
    # ------------------------------------------------------------------ E1-0140
    card(
        "E1-0140", "efi", COM_TEOREMAS,
        assertiva=("O Segundo Teorema do Bem-Estar estabelece que para toda alocação eficiente de Pareto existem "
                   "um vetor de preços e um vetor de dotações iniciais tal que essa alocação também é um "
                   "equilíbrio competitivo."),
        gabarito="CERTO",
        anotada=az("O Segundo Teorema do Bem-Estar estabelece que para <u>toda alocação eficiente de Pareto</u> "
                   "existem um vetor de preços e um vetor de dotações iniciais tal que essa alocação também é "
                   "um equilíbrio competitivo."),
        poucas=("É o enunciado do " + azb("2º Teorema") + ": qualquer ótimo de Pareto pode ser "
                "<b>descentralizado</b> pelo mercado, desde que se redistribuam as dotações iniciais e se deixem "
                "os preços operar (sob preferências convexas)."),
        destrinchando=[
            azb("1º Teorema do Bem-Estar") + ": equilíbrio competitivo ⇒ Pareto-eficiente (mercado → "
            "eficiência). " + azb("2º Teorema") + ": Pareto-eficiente ⇒ alcançável como equilíbrio "
            "competitivo, com redistribuição prévia das dotações (eficiência → mercado). São recíprocos, mas "
            "não simétricos nas hipóteses.",
            "Hipóteses do 2º: preferências (e tecnologias) " + vd("convexas") + ", não saciedade local, "
            "mercados completos, ausência de externalidades, informação perfeita e possibilidade de "
            + azb("transferências lump-sum") + " (de montante fixo, que não distorcem incentivos).",
            "Mensagem de política: separa <b>eficiência</b> de <b>distribuição</b>. Se a sociedade prefere outra "
            "distribuição, não precisa controlar preços (o que geraria peso morto): basta redistribuir riqueza "
            "e deixar o mercado alcançar o ótimo correspondente.",
            "Limite prático: transferências lump-sum puras quase não existem — os tributos reais incidem sobre "
            "renda, consumo ou propriedade e alteram incentivos. Daí o dilema entre equidade e eficiência na "
            "tributação ótima.",
            "Base teórica: " + oc("Arrow") + " e " + oc("Debreu") + " deram a formalização moderna dos dois "
            "teoremas no modelo de equilíbrio geral (anos 1950).",
        ],
        dissecando=(cz("[literalidade · detalhe]") + " Enunciado formal, com “vetor de preços” e “vetor de "
                    "dotações iniciais”. O risco é a troca de teoremas: se o item partisse do equilíbrio "
                    "competitivo e concluísse eficiência, seria o 1º. A direção (eficiente → equilíbrio, com "
                    "dotações ajustadas) identifica o 2º."),
        modulos=[("😈 Para dificultar", [
            "<i>“O Segundo Teorema do Bem-Estar estabelece que todo equilíbrio competitivo é eficiente no "
            "sentido de Pareto.”</i> → ERRADO (esse é o 1º Teorema)",
            "<i>“Segundo o Segundo Teorema do Bem-Estar, qualquer alocação eficiente pode ser obtida pelo "
            "mercado, desde que as dotações sejam redistribuídas por transferências de montante fixo.”</i> → "
            "CERTO",
        ])],
        tipo_erro=["LITERAL", "DETALHE"], dificuldade=2,
        comentario_fonte=("CERTO. Esse é exatamente o enunciado do Segundo Teorema do Bem-Estar: qualquer "
                          "alocação eficiente de Pareto pode ser alcançada como equilíbrio competitivo, desde que "
                          "haja redistribuição adequada das dotações iniciais."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0141
    card(
        "E1-0141", "efi",
        "Com relação aos conceitos de eficiência técnica e de eficiência de Pareto, julgue o item.",
        assertiva="Alocações são consideradas “ineficientes” se melhorias inequívocas forem possíveis.",
        gabarito="CERTO",
        anotada=az("Alocações são consideradas “ineficientes” se <u>melhorias inequívocas</u> forem possíveis."),
        poucas=("“" + azb("Melhoria inequívoca") + "” é outro nome da " + azb("melhoria de Pareto") + " — "
                "alguém ganha e ninguém perde. Se ela é possível, a alocação é " + vd("ineficiente") + "."),
        destrinchando=[
            "Uma melhoria é “inequívoca” quando não exige comparar ganhos e perdas entre pessoas: como ninguém "
            "piora, qualquer critério de bem-estar razoável a aprova. É exatamente a melhoria de Pareto.",
            azb("Eficiência de Pareto") + " = não restam melhorias inequívocas. " + azb("Ineficiência")
            + " = ainda resta ao menos uma.",
            azb("Eficiência técnica") + " (ou produtiva) é conceito mais estreito: produzir o máximo possível "
            "com os insumos dados (estar sobre a função de produção ou a isoquanta, sem desperdício físico). "
            "É necessária, mas não suficiente, para a eficiência de Pareto, que exige também alocar bem os "
            "fatores entre indústrias e os bens entre consumidores.",
            "Exemplo: uma fábrica tecnicamente eficiente que produz um bem que ninguém quer, em vez de outro "
            "mais valorizado, está tecnicamente eficiente e alocativamente ineficiente.",
        ],
        dissecando=(cz("[paráfrase fiel]") + " A banca troca o termo técnico (“melhoria de Pareto”) por um "
                    "sinônimo menos usual (“melhoria inequívoca”) para testar se o candidato reconhece o "
                    "conceito. As aspas em “ineficientes” sinalizam o sentido técnico, não o coloquial."),
        modulos=[("😈 Para dificultar", [
            "<i>“Alocações tecnicamente eficientes são necessariamente eficientes no sentido de Pareto.”</i> → "
            "ERRADO (eficiência técnica é necessária, não suficiente)",
            "<i>“Alocações são consideradas eficientes se não houver melhorias inequívocas possíveis.”</i> → "
            "CERTO",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], dificuldade=1,
        comentario_fonte=("CERTO. Por definição, uma alocação é ineficiente no sentido de Pareto se for possível "
                          "melhorar alguém sem prejudicar ninguém, ou seja, se melhorias inequívocas forem "
                          "possíveis."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0142
    card(
        "E1-0142", "efi", COM_HIPOTESES,
        assertiva=("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que as "
                   "preferências sejam convexas."),
        gabarito="CERTO",
        anotada=az("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que as "
                   "preferências sejam <u>convexas</u>."),
        poucas=("Sim: a " + azb("convexidade") + " das preferências é a hipótese que distingue o 2º Teorema "
                "do 1º. Sem ela, um ótimo de Pareto pode não ser sustentável por nenhum sistema de preços."),
        destrinchando=[
            azb("Preferências convexas") + " = médias são preferidas a extremos; curvas de indiferença "
            "convexas em relação à origem (TMS decrescente).",
            "Por que o 2º Teorema precisa dela: para “descentralizar” um ótimo de Pareto, é preciso uma reta "
            "de preços que, passando pelo ponto, deixe cada consumidor escolhendo exatamente aquela cesta. "
            "Com curvas convexas, a reta tangente comum (TMS<sub>A</sub> = TMS<sub>B</sub>) separa as cestas "
            "preferidas das demais. Com curvas não convexas, o consumidor pode preferir outra cesta sobre a "
            "mesma reta, e o ótimo não vira equilíbrio.",
            "O " + azb("1º Teorema") + " <b>não</b> precisa de convexidade: basta " + vd("não saciedade "
            "local") + " (sempre haver uma cesta próxima melhor), mercados completos e ausência de "
            "externalidades.",
            "Demais hipóteses do 2º: mercados completos e competitivos, informação perfeita (simétrica), "
            "ausência de externalidades e de bens públicos, e transferências de montante fixo para "
            "redistribuir as dotações.",
        ],
        dissecando=(cz("[literalidade · detalhe]") + " Item de lista de hipóteses, em bloco com variantes "
                    "falsas (informação assimétrica, mercados incompletos). 🔥 A banca costuma cobrar a "
                    "convexidade justamente para separar os dois teoremas."),
        modulos=[("😈 Para dificultar", [
            "<i>“Uma das hipóteses para que o 1º Teorema do Bem-Estar seja válido é que as preferências sejam "
            "convexas.”</i> → ERRADO (o 1º só exige não saciedade local)",
            "<i>“Com preferências não convexas, nem toda alocação eficiente de Pareto pode ser sustentada como "
            "equilíbrio competitivo.”</i> → CERTO",
        ])],
        tipo_erro=["LITERAL", "DETALHE"], dificuldade=2,
        comentario_fonte=("CERTO. O 2º Teorema do Bem-Estar Social exige que as preferências dos consumidores "
                          "sejam convexas (bem-comportadas), o que garante a possibilidade de se alcançar qualquer "
                          "alocação eficiente de Pareto como um equilíbrio competitivo após redistribuição "
                          "adequada das dotações iniciais. [imagem]"),
        qualidade_fonte="bom",
        figuras_fonte=[img_verso("Untitled (31).jpeg")],
    ),
    # ------------------------------------------------------------------ E1-0143
    card(
        "E1-0143", "efi", COM_HIPOTESES,
        assertiva=("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que a informação "
                   "seja assimétrica."),
        gabarito="ERRADO",
        anotada=(az("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que a informação "
                    "seja ") + vm("assimétrica") + az(".")),
        poucas=("Os teoremas do bem-estar supõem " + azb("informação perfeita e simétrica") + ". A "
                + azb("assimetria de informação") + " é uma " + vd("falha de mercado") + " que derruba as "
                "conclusões, não uma hipótese delas."),
        destrinchando=[
            "No modelo de equilíbrio geral de " + oc("Arrow") + "-" + oc("Debreu") + ", todos conhecem preços, "
            "qualidades e características dos bens. Os preços resumem toda a informação relevante.",
            "Com " + azb("informação assimétrica") + ", uma parte sabe mais que a outra e surgem "
            + azb("seleção adversa") + " (antes do contrato: " + oc("Akerlof") + ", “mercado de limões”, 1970) "
            "e " + azb("risco moral") + " (depois do contrato: o segurado relaxa os cuidados). Mercados "
            "encolhem ou desaparecem, e o equilíbrio deixa de ser eficiente.",
            oc("Greenwald") + " e " + oc("Stiglitz") + " (1986) mostraram que, com informação imperfeita, o "
            "equilíbrio competitivo em geral não é sequer eficiente “restrito” — há intervenções que melhoram "
            "todos.",
            "Por isso a assimetria de informação aparece na lista de " + azb("falhas de mercado") + ", ao lado "
            "de externalidades, bens públicos e poder de mercado: são justamente as violações das hipóteses "
            "dos teoremas.",
        ],
        dissecando=(cz("[inversão]") + " O item transforma uma falha de mercado em hipótese do teorema. "
                    "Itens irmãos do mesmo bloco trocam outras hipóteses pelo seu oposto (convexas × não "
                    "convexas; completos × incompletos): basta lembrar que a hipótese é sempre o “mundo "
                    "ideal”."),
        modulos=[("😈 Para dificultar", [
            "<i>“A existência de informação assimétrica entre compradores e vendedores pode impedir que o "
            "equilíbrio competitivo seja eficiente no sentido de Pareto.”</i> → CERTO",
            "<i>“A seleção adversa decorre de ações ocultas tomadas após a assinatura do contrato.”</i> → "
            "ERRADO (troca de conceito: isso é risco moral)",
        ])],
        reescrita=("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que a informação "
                   "seja " + hl("simétrica (perfeita)") + "."),
        tipo_erro=["INVERSAO"], dificuldade=1,
        comentario_fonte=("ERRADO. O teorema assume informação perfeita e simétrica entre os agentes. A "
                          "informação assimétrica compromete a validade do teorema."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0144
    card(
        "E1-0144", "efi", COM_HIPOTESES,
        assertiva=("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que os mercados "
                   "sejam incompletos."),
        gabarito="ERRADO",
        anotada=(az("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que os mercados "
                    "sejam ") + vm("incompletos") + az(".")),
        poucas=("O teorema exige " + azb("mercados completos") + ": um mercado (e um preço) para cada bem, em "
                "cada data e em cada estado da natureza. Mercados incompletos são falha de mercado."),
        destrinchando=[
            azb("Mercados completos") + " (" + oc("Arrow") + "-" + oc("Debreu") + "): existe mercado para "
            "todo bem que afete utilidade ou produção, inclusive " + azb("bens contingentes") + " (entregues só "
            "em determinado estado do mundo) e entregas futuras. Assim, todo risco pode ser negociado e todo "
            "efeito passa pelo sistema de preços.",
            "Mercado incompleto = há algo que importa e não tem preço: seguros inexistentes (riscos não "
            "seguráveis), crédito racionado, ausência de mercados futuros de longo prazo, efeitos sem mercado "
            "(as " + azb("externalidades") + " são, no fundo, mercados ausentes).",
            "Sem preço, o mercado não consegue implementar todas as alocações eficientes — e nem o 1º "
            "Teorema vale em geral (equilíbrios com mercados incompletos costumam ser ineficientes).",
            "Leitura de política: completar mercados (criar seguros, direitos de propriedade, mercados de "
            "carbono) é uma das respostas clássicas às falhas de mercado; " + oc("Coase") + " vai na mesma "
            "linha ao propor definir direitos para que a negociação resolva a externalidade.",
        ],
        dissecando=(cz("[inversão]") + " Mesmo padrão do bloco: a hipótese verdadeira (mercados completos) é "
                    "trocada pela falha correspondente. Regra prática: a hipótese de um teorema de eficiência "
                    "nunca é uma falha de mercado."),
        modulos=[("😈 Para dificultar", [
            "<i>“A ausência de mercados para certos riscos é uma das razões pelas quais o equilíbrio de mercado "
            "pode não ser eficiente.”</i> → CERTO",
            "<i>“Os teoremas do bem-estar dispensam a existência de mercados para bens futuros e "
            "contingentes.”</i> → ERRADO (exigem mercados completos, inclusive esses)",
        ])],
        reescrita=("Uma das hipóteses para que o 2º Teorema do Bem-Estar Social seja válido é que os mercados "
                   "sejam " + hl("completos") + "."),
        tipo_erro=["INVERSAO"], dificuldade=1,
        comentario_fonte=("ERRADO. O 2º Teorema requer mercados completos. Mercados incompletos impedem que todas "
                          "as alocações eficientes sejam implementadas via preços."),
        qualidade_fonte="bom",
    ),
]
