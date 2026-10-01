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
    # ------------------------------------------------------------------ E1-0145
    card(
        "E1-0145", "efi", COM_PARETO,
        assertiva=("O ótimo de Pareto é caracterizado por uma “alocação eficiente” ou “Pareto ótima” se ela está "
                   "na fronteira de Pareto (caso contrário, ela é ineficiente)."),
        gabarito="CERTO",
        anotada=az("O ótimo de Pareto é caracterizado por uma “alocação eficiente” ou “Pareto ótima” se ela está "
                   "<u>na fronteira de Pareto</u> (caso contrário, ela é ineficiente)."),
        poucas=("A " + azb("fronteira de Pareto") + " é o conjunto das alocações eficientes: sobre ela, "
                "melhorar alguém exige piorar outro; fora dela, ainda há " + vd("trocas mutuamente "
                "vantajosas") + "."),
        destrinchando=[
            "Quatro formulações equivalentes de alocação Pareto-eficiente: (1) não é possível que todos "
            "melhorem; (2) não é possível melhorar alguém sem piorar outro; (3) os ganhos de troca se "
            "esgotaram; (4) não restam trocas mutuamente vantajosas.",
            "Na " + azb("caixa de Edgeworth") + ", a fronteira de Pareto aparece como a " + azb("curva de "
            "contrato") + " (pontos de tangência entre as curvas de indiferença dos dois consumidores). No "
            "espaço das utilidades (U<sub>A</sub> × U<sub>B</sub>), aparece como a " + azb("fronteira de "
            "possibilidades de utilidade") + ", negativamente inclinada.",
            "Partindo de uma dotação fora da curva de contrato, as curvas de indiferença que passam por ela "
            "se cruzam e formam uma <b>lente</b>: toda alocação dentro da lente melhora os dois. As trocas "
            "levam a economia até o trecho da curva de contrato dentro da lente (o " + azb("núcleo") + ").",
            "Nos mercados, a mesma ideia: eficiente é o nível de produção em que a disposição marginal a "
            "pagar iguala o custo marginal de produzir — nem mais, nem menos.",
            vm("Regra-âncora: sobre a fronteira → eficiente (toda melhora tem custo para alguém); dentro dela → "
               "ineficiente (existe melhora gratuita)."),
        ],
        grafico_verso="ECO-E1-0145-1-V1",
        dissecando=(cz("[paráfrase fiel]") + " Redação truncada (“o ótimo de Pareto é caracterizado por uma "
                    "alocação eficiente… se ela está na fronteira”), mas o conteúdo é a definição correta. A "
                    "armadilha é o candidato rejeitar o item pela forma; julgue o conteúdo."),
        modulos=[("😈 Para dificultar", [
            "<i>“Todo ponto sobre a fronteira de Pareto é preferido por ambos os consumidores a qualquer ponto "
            "fora dela.”</i> → ERRADO (modulador absoluto: só os pontos dentro da lente melhoram os dois)",
            "<i>“Uma alocação no interior da fronteira de possibilidades de utilidade admite melhoria de "
            "Pareto.”</i> → CERTO",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], dificuldade=1,
        comentario_fonte=("CERTO. Alocação no ótimo de Pareto está sobre a fronteira; fora dela há ineficiência. "
                          "Eficiente: disposição marginal a comprar = disposição marginal a vender; quatro "
                          "formulações equivalentes de eficiência. Caixa de Edgeworth: área sombreada = trocas "
                          "mutuamente vantajosas; TMS de Ana e Bruno dão as tangentes no ponto A. [imagem]"),
        qualidade_fonte="bom",
        figuras_fonte=[{"ref": "Untitled (36).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                        "acao": "irrecuperavel (imagem não preservada; o texto descreve uma caixa de Edgeworth com "
                                "a lente de trocas vantajosas — mecanismo redesenhado em ECO-E1-0145-1-V1)"}],
    ),
    # ------------------------------------------------------------------ E1-0146
    card(
        "E1-0146", "efi", COM_PARETO,
        assertiva=("Uma característica de um ponto da curva de contrato é que ela pertence ao conjunto de Pareto, "
                   "independente da dotação inicial."),
        gabarito="CERTO",
        anotada=az("Uma característica de um ponto da curva de contrato é que ela pertence ao conjunto de Pareto, "
                   "<u>independente da dotação inicial</u>."),
        poucas=("A " + azb("curva de contrato") + " é, por construção, o conjunto de " + vd("todas") + " as "
                "alocações Pareto-eficientes. A dotação inicial só decide em <b>qual</b> ponto dela as trocas "
                "terminam."),
        destrinchando=[
            "Na caixa de Edgeworth, a curva de contrato reúne os pontos em que as curvas de indiferença dos dois "
            "consumidores são " + azb("tangentes") + ": " + vd("TMS<sub>A</sub> = TMS<sub>B</sub>") + ". Em "
            "cada um deles, qualquer movimento melhora um e piora o outro.",
            "A eficiência de um ponto depende só das preferências e das quantidades totais (o tamanho da "
            "caixa) — não de onde a economia começou. Por isso “independente da dotação inicial” está certo.",
            "O que a dotação muda é o <b>resultado</b>: partindo de ω, as trocas voluntárias levam a algum ponto "
            "da curva de contrato dentro da lente de ω (o " + azb("núcleo") + "); outra dotação leva a outro "
            "trecho. Uma dotação muito desigual gera um ponto eficiente e muito desigual.",
            "Daí o " + azb("2º Teorema do Bem-Estar") + ": para chegar a um ponto eficiente específico da "
            "curva, redistribui-se a dotação e deixa-se o mercado agir.",
            vm("Regra-âncora: a dotação escolhe o ponto; a curva de contrato garante a eficiência."),
        ],
        grafico_verso="ECO-E1-0146-1-V1",
        dissecando=(cz("[detalhe · contraintuitivo]") + " A cláusula final (“independente da dotação "
                    "inicial”) parece exagero e induz ao ERRADO; mas ela fala da <b>eficiência</b> de cada "
                    "ponto, que de fato não depende da dotação. O que dependeria é o ponto alcançado."),
        modulos=[("😈 Para dificultar", [
            "<i>“A partir de qualquer dotação inicial, as trocas voluntárias podem levar a qualquer ponto da "
            "curva de contrato.”</i> → ERRADO (generalização: só aos pontos dentro da lente da dotação)",
            "<i>“Ao longo da curva de contrato, as taxas marginais de substituição dos dois consumidores são "
            "iguais.”</i> → CERTO",
        ])],
        tipo_erro=["DETALHE", "CONTRAINTUITIVO"], dificuldade=2,
        comentario_fonte=("CERTO. Todo ponto na curva de contrato é eficiente no sentido de Pareto, e essa curva "
                          "representa o conjunto das alocações Pareto eficientes, independentemente da dotação "
                          "inicial. A curva de contrato contém todas as alocações em que as curvas de indiferença "
                          "são tangentes. [imagem]"),
        qualidade_fonte="bom",
        figuras_fonte=[{"ref": "Untitled (37).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                        "acao": "irrecuperavel (imagem não preservada; o texto descreve a curva de contrato — "
                                "mecanismo redesenhado em ECO-E1-0146-1-V1)"}],
    ),
    # ------------------------------------------------------------------ E1-0147
    card(
        "E1-0147", "efi", COM_PARETO,
        assertiva=("A eficiência máxima na alocação de recursos, equivalente ao Ótimo de Pareto, é atingida "
                   "quando todos usufruem de um nível satisfatório de bem-estar."),
        gabarito="ERRADO",
        anotada=(az("A eficiência máxima na alocação de recursos, equivalente ao Ótimo de Pareto, é atingida "
                    "quando ") + vm("todos usufruem de um nível satisfatório de bem-estar") + az(".")),
        poucas=("O " + azb("ótimo de Pareto") + " não fixa nenhum piso de bem-estar: é atingido quando "
                + vd("não se pode melhorar ninguém sem piorar outro") + " — mesmo que alguns estejam na "
                "miséria."),
        destrinchando=[
            "Pareto é um critério de " + azb("eficiência") + ", não de " + azb("justiça") + " nem de "
            "suficiência. Ele compara situações apenas pela possibilidade de ganhos sem perdedores.",
            "Exemplo-limite: uma economia em que uma pessoa detém todos os recursos e as demais nada têm é "
            "Pareto-eficiente — qualquer transferência piora o dono. Ninguém diria que todos “usufruem de nível "
            "satisfatório”.",
            "Inversamente, uma situação em que todos estão razoavelmente bem pode ser ineficiente, se houver "
            "recursos ociosos ou trocas vantajosas não realizadas.",
            "Critérios que incorporam distribuição exigem uma " + azb("função de bem-estar social") + ": "
            "utilitarista (soma das utilidades, " + oc("Bentham") + "), rawlsiana (maximizar o bem-estar do "
            "mais pobre, " + oc("Rawls") + "), ou intermediárias. Elas escolhem <b>um</b> ponto da fronteira "
            "de Pareto.",
            vm("Regra-âncora: Pareto mede desperdício, não suficiência nem igualdade."),
        ],
        dissecando=(cz("[troca de conceito]") + " O item substitui o critério de Pareto (impossibilidade de "
                    "melhora sem perdedor) por um critério normativo de bem-estar mínimo. O adjetivo "
                    "“satisfatório” é vago e valorativo — sinal de que não pertence a uma definição de "
                    "eficiência."),
        modulos=[("😈 Para dificultar", [
            "<i>“Uma alocação extremamente desigual pode ser eficiente no sentido de Pareto.”</i> → CERTO",
            "<i>“O ótimo de Pareto corresponde ao ponto da fronteira de utilidades que maximiza o bem-estar do "
            "indivíduo mais pobre.”</i> → ERRADO (troca de conceito: esse é o critério rawlsiano, um ponto "
            "específico entre muitos ótimos de Pareto)",
        ])],
        reescrita=("A eficiência máxima na alocação de recursos, equivalente ao Ótimo de Pareto, é atingida "
                   "quando " + hl("não é possível melhorar o bem-estar de alguém sem reduzir o de outro") + "."),
        tipo_erro=["TROCA_CONCEITO"], dificuldade=1,
        comentario_fonte=("ERRADO. A eficiência de Pareto não considera igualdade ou bem-estar mínimo (ou, "
                          "meramente “satisfatório”); apenas considera se é possível melhorar alguém sem "
                          "prejudicar outro."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0148
    card(
        "E1-0148", "efi", COM_TEOREMAS,
        assertiva=("O primeiro teorema do Bem-Estar determina que todo equilíbrio de mercado competitivo é "
                   "eficiente no sentido de Pareto."),
        gabarito="CERTO",
        anotada=az("O primeiro teorema do Bem-Estar determina que todo equilíbrio de mercado "
                   "<u>competitivo</u> é eficiente no sentido de Pareto."),
        poucas=("É o " + azb("1º Teorema do Bem-Estar") + ": sob concorrência perfeita, mercados completos e "
                "sem externalidades, o equilíbrio competitivo é " + vd("Pareto-eficiente") + " — a versão "
                "formal da “mão invisível”."),
        destrinchando=[
            "Mecanismo: em concorrência, todos enfrentam os <b>mesmos preços</b>. Cada consumidor iguala sua "
            "TMS à razão de preços; cada firma iguala a TMST à razão dos preços dos fatores e o custo "
            "marginal ao preço. Logo as TMS de todos se igualam (eficiência na troca), as TMST também "
            "(eficiência na produção) e TMS = taxa marginal de transformação (eficiência no mix).",
            "Hipóteses: " + vd("mercados completos") + ", agentes tomadores de preço, " + vd("ausência de "
            "externalidades") + " e de bens públicos, informação perfeita e não saciedade local. "
            "<b>Não</b> exige preferências convexas (essa é hipótese do 2º).",
            "É a formalização da “mão invisível” de " + oc("Adam Smith") + ", feita por " + oc("Arrow")
            + " e " + oc("Debreu") + " nos anos 1950.",
            "O que o teorema <b>não</b> diz: que o equilíbrio é justo. Ele parte das dotações iniciais, "
            "quaisquer que sejam; a eficiência pode conviver com enorme desigualdade.",
            "Cada hipótese violada abre uma " + azb("falha de mercado") + " (monopólio, externalidade, bem "
            "público, assimetria de informação) — e com ela a justificativa econômica para intervir.",
        ],
        dissecando=(cz("[literalidade]") + " Enunciado-padrão do 1º Teorema, sem as hipóteses explícitas — a "
                    "banca considera implícitas as condições do modelo competitivo. O adjetivo decisivo é "
                    "“competitivo”: o item irmão troca por “não competitivo” e vira ERRADO."),
        modulos=[("😈 Para dificultar", [
            "<i>“O primeiro teorema do bem-estar garante que o equilíbrio competitivo é eficiente mesmo na "
            "presença de externalidades.”</i> → ERRADO (hipótese violada: exige ausência de externalidades)",
            "<i>“Segundo o primeiro teorema do bem-estar, o equilíbrio competitivo é eficiente, mas não "
            "necessariamente equitativo.”</i> → CERTO",
        ])],
        tipo_erro=["LITERAL"], dificuldade=1,
        comentario_fonte=("CERTO. Enunciado clássico do 1º Teorema do Bem-Estar: todo equilíbrio competitivo (em "
                          "mercados completos e com preferências bem-comportadas) é eficiente de Pareto. [imagem]"),
        qualidade_fonte="com_erro",
        figuras_fonte=[img_verso("Untitled (42).jpeg")],
        alertas=["qualidade_fonte: o comentário de origem inclui “preferências bem-comportadas” entre as "
                 "hipóteses do 1º Teorema; a convexidade é exigida pelo 2º — o 1º só requer não saciedade "
                 "local (corrigido no 📖)"],
    ),
    # ------------------------------------------------------------------ E1-0149
    card(
        "E1-0149", "efi", COM_TEOREMAS,
        assertiva=("O primeiro teorema do Bem-Estar determina que todo equilíbrio de mercado não competitivo é "
                   "eficiente no sentido de Pareto."),
        gabarito="ERRADO",
        anotada=(az("O primeiro teorema do Bem-Estar determina que todo equilíbrio de mercado ")
                 + vm("não competitivo") + az(" é eficiente no sentido de Pareto.")),
        poucas=("O 1º Teorema vale para o equilíbrio " + azb("competitivo") + ". Com " + azb("poder de "
                "mercado") + ", o preço fica acima do custo marginal, a quantidade cai e surge " + vd("peso "
                "morto") + "."),
        destrinchando=[
            "A peça-chave do 1º Teorema é que todos são <b>tomadores de preço</b>: p = CMg na produção e "
            "TMS = razão de preços no consumo. Isso garante que a última unidade produzida vale, para o "
            "consumidor, exatamente o que custa.",
            "No " + azb("monopólio") + ", a firma produz onde RMg = CMg e cobra p > RMg = CMg. Há consumidores "
            "dispostos a pagar mais que o custo marginal que ficam sem o bem: é o " + azb("peso morto do "
            "monopólio") + ". Raciocínio análogo vale para oligopólios e concorrência monopolística (preço "
            "com markup).",
            "Exceção que confirma a regra: o monopolista que pratica " + azb("discriminação perfeita de "
            "preços") + " (1º grau) produz a quantidade eficiente — não há peso morto, mas todo o excedente "
            "vai para ele. Ainda assim, nenhum teorema afirma que “todo” equilíbrio não competitivo é "
            "eficiente.",
            "Concorrência imperfeita é uma das " + azb("falhas de mercado") + " que justificam defesa da "
            "concorrência e regulação (ex.: " + rx("CADE") + " e agências reguladoras no " + rx("Brasil")
            + ").",
        ],
        dissecando=(cz("[troca de conceito]") + " Item gêmeo do enunciado correto, com um só termo trocado "
                    "(“competitivo” → “não competitivo”). 🔥 Em blocos de itens irmãos, compare palavra por "
                    "palavra: a banca muda um adjetivo e inverte o gabarito."),
        modulos=[("😈 Para dificultar", [
            "<i>“O monopólio com discriminação perfeita de preços produz a quantidade socialmente "
            "eficiente.”</i> → CERTO",
            "<i>“Em um monopólio sem discriminação de preços, o preço é igual ao custo marginal.”</i> → ERRADO "
            "(troca de conceito: p > CMg; é a RMg que iguala o CMg)",
        ])],
        reescrita=("O primeiro teorema do Bem-Estar determina que todo equilíbrio de mercado "
                   + hl("competitivo") + " é eficiente no sentido de Pareto."),
        tipo_erro=["TROCA_CONCEITO"], dificuldade=1,
        comentario_fonte=("ERRADO. Mercados não competitivos (como monopólios ou oligopólios) geralmente não são "
                          "eficientes de Pareto, pois distorcem preços e quantidades."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0150
    card(
        "E1-0150", "efi", COM_TEOREMAS,
        assertiva=("O Primeiro Teorema do Bem-Estar determina que toda alocação eficiente de Pareto é uma "
                   "alocação de equilíbrio de mercado para uma redistribuição de dotações e preferências "
                   "convexas."),
        gabarito="ERRADO",
        anotada=(az("O ") + vm("Primeiro") + az(" Teorema do Bem-Estar determina que toda alocação eficiente "
                 "de Pareto é uma alocação de equilíbrio de mercado para uma redistribuição de dotações e "
                 "preferências convexas.")),
        poucas=("O conteúdo descrito (eficiente → equilíbrio, com redistribuição de dotações e preferências "
                "convexas) é o " + azb("2º Teorema") + ". O 1º vai no sentido inverso: " + vd("equilíbrio "
                "competitivo → eficiente") + "."),
        destrinchando=[
            "Como separar os dois pela <b>direção da implicação</b>: " + azb("1º Teorema") + " — parte do "
            "mercado (equilíbrio competitivo) e conclui eficiência. " + azb("2º Teorema") + " — parte de uma "
            "alocação eficiente qualquer e conclui que o mercado pode alcançá-la.",
            "Como separar pelas <b>hipóteses</b>: só o 2º menciona " + vd("redistribuição de dotações") + " e "
            + vd("preferências convexas") + ". Se essas expressões aparecem, o teorema é o 2º.",
            "Como separar pela <b>mensagem</b>: o 1º justifica a confiança no mercado (mão invisível); o 2º "
            "separa eficiência de distribuição (a equidade se busca redistribuindo riqueza, não controlando "
            "preços).",
            vm("Regra-âncora: 1º = mercado ⇒ eficiência; 2º = eficiência ⇒ mercado (após redistribuir)."),
        ],
        dissecando=(cz("[troca de conceito]") + " Enunciado correto do 2º Teorema com o rótulo trocado. Pista "
                    "infalível: “redistribuição de dotações” e “preferências convexas” só aparecem no 2º."),
        modulos=[("🧠 Mnemônico", ["<b>1º</b>: do mercado <b>para</b> a eficiência (ida). <b>2º</b>: da "
                                   "eficiência <b>de volta</b> ao mercado (volta, com a mala da "
                                   "redistribuição)."]),
                 ("😈 Para dificultar", [
                     "<i>“O Segundo Teorema do Bem-Estar determina que toda alocação eficiente de Pareto pode "
                     "ser obtida como equilíbrio de mercado, mediante redistribuição de dotações, se as "
                     "preferências forem convexas.”</i> → CERTO",
                 ])],
        reescrita=("O " + hl("Segundo") + " Teorema do Bem-Estar determina que toda alocação eficiente de "
                   "Pareto é uma alocação de equilíbrio de mercado para uma redistribuição de dotações e "
                   "preferências convexas."),
        tipo_erro=["TROCA_CONCEITO"], dificuldade=1,
        comentario_fonte="ERRADO. Isso descreve o Segundo Teorema do Bem-Estar, e não o primeiro.",
        qualidade_fonte="raso",
    ),
    # ------------------------------------------------------------------ E1-0151
    card(
        "E1-0151", "efi", COM_TEOREMAS,
        assertiva=("O Primeiro Teorema do Bem-Estar determina que toda alocação eficiente de Pareto é uma "
                   "alocação de equilíbrio de mercado para uma redistribuição de dotações e preferências não "
                   "convexas."),
        gabarito="ERRADO",
        anotada=(az("O ") + vm("Primeiro") + az(" Teorema do Bem-Estar determina que toda alocação eficiente "
                 "de Pareto é uma alocação de equilíbrio de mercado para uma redistribuição de dotações e "
                 "preferências ") + vm("não convexas") + az(".")),
        poucas=("Dois erros: o enunciado é o do " + azb("2º Teorema") + " (não do 1º), e o 2º exige "
                "preferências " + vd("convexas") + ", não “não convexas”."),
        destrinchando=[
            "O 2º Teorema afirma que toda alocação Pareto-eficiente pode ser obtida como equilíbrio "
            "competitivo após redistribuição das dotações — desde que as preferências (e tecnologias) sejam "
            + azb("convexas") + ".",
            "Por que a convexidade importa: com curvas de indiferença convexas, a reta de preços tangente no "
            "ponto eficiente deixa cada consumidor escolhendo exatamente aquela cesta. Com curvas não "
            "convexas, o consumidor pode preferir outro ponto da mesma reta, e o ótimo não se sustenta como "
            "equilíbrio.",
            "Hipóteses gerais dos teoremas: mercados completos e competitivos, informação perfeita, ausência "
            "de externalidades e de bens públicos, não saciedade local; para o 2º, ainda " + vd("convexidade")
            + " e transferências de montante fixo.",
            "Atenção: a convexidade <b>não</b> é exigida pelo 1º Teorema. Listas de “hipóteses necessárias” que "
            "misturam os dois teoremas são fonte frequente de erro.",
        ],
        dissecando=(cz("[troca de conceito · inversão]") + " Item construído sobre o irmão (que já trocava 1º "
                    "por 2º), acrescentando a inversão da hipótese (convexas → não convexas). Basta um dos "
                    "erros para o ERRADO; a reescrita precisa corrigir os dois."),
        modulos=[("😈 Para dificultar", [
            "<i>“Com preferências não convexas, o Segundo Teorema do Bem-Estar pode falhar.”</i> → CERTO",
            "<i>“O Primeiro Teorema do Bem-Estar exige preferências convexas.”</i> → ERRADO (troca de teorema: "
            "o 1º só exige não saciedade local; a convexidade é do 2º)",
        ])],
        reescrita=("O " + hl("Segundo") + " Teorema do Bem-Estar determina que toda alocação eficiente de "
                   "Pareto é uma alocação de equilíbrio de mercado para uma redistribuição de dotações e "
                   "preferências " + hl("convexas") + "."),
        tipo_erro=["TROCA_CONCEITO", "INVERSAO"], dificuldade=1,
        comentario_fonte=("ERRADO. Além de confundir com o segundo teorema, a afirmação menciona preferências não "
                          "convexas, o que viola as hipóteses necessárias (preferências convexas; mercados "
                          "perfeitamente competitivos; racionalidade; informação perfeita; ausência de "
                          "externalidades)."),
        qualidade_fonte="com_erro",
        alertas=["qualidade_fonte: o comentário de origem lista as “hipóteses necessárias” sem distinguir os "
                 "teoremas; a convexidade é exigida só pelo 2º (precisado no 📖)"],
    ),
    # ------------------------------------------------------------------ E1-0152
    card(
        "E1-0152", "efi", COM_PARETO,
        assertiva=("No ótimo de Pareto, a economia está na fronteira de possibilidades de produção e na fronteira "
                   "de possibilidades de utilidade, simultaneamente, pois os preços funcionam como sinal de "
                   "escassez para as empresas e de utilidade social para os consumidores."),
        gabarito="CERTO",
        anotada=az("No ótimo de Pareto, a economia está na fronteira de possibilidades de produção <u>e</u> na "
                   "fronteira de possibilidades de utilidade, <u>simultaneamente</u>, pois os preços funcionam "
                   "como sinal de escassez para as empresas e de utilidade social para os consumidores."),
        poucas=("O ótimo de Pareto em " + azb("equilíbrio geral") + " exige eficiência na produção (estar na "
                + azb("FPP") + ") e na distribuição dos bens (estar na " + azb("FPU") + "); em concorrência, "
                "os " + vd("preços relativos") + " coordenam as duas coisas ao mesmo tempo."),
        destrinchando=[
            "Três condições de eficiência em equilíbrio geral: (1) <b>produção</b> — TMST entre capital e "
            "trabalho igual em todas as indústrias → economia sobre a " + azb("fronteira de possibilidades de "
            "produção") + "; (2) <b>troca</b> — TMS entre os bens igual para todos os consumidores → sobre a "
            "curva de contrato; (3) <b>mix de produtos</b> — " + vd("TMS = TMT") + " (taxa marginal de "
            "transformação, a inclinação da FPP).",
            "Satisfeitas as três, a economia está na " + azb("fronteira de possibilidades de utilidade") + " "
            "“grande”: não dá para elevar a utilidade de alguém sem reduzir a de outro, nem reorganizando a "
            "produção, nem redistribuindo os bens.",
            "O “pois” do item remete ao " + azb("1º Teorema do Bem-Estar") + ": em concorrência perfeita, as "
            "firmas igualam a TMT à razão de preços (p = CMg) e os consumidores igualam a TMS à mesma razão. "
            "Os preços transmitem, de um lado, o custo de oportunidade (escassez) e, do outro, a valoração "
            "marginal dos consumidores — e as três condições se cumprem sem planejador central.",
            "Estar na FPP é necessário, mas não suficiente: pode-se produzir eficientemente a cesta errada "
            "(TMS ≠ TMT) ou distribuí-la mal entre consumidores.",
        ],
        dissecando=(cz("[detalhe · paráfrase fiel]") + " Item longo, com duas afirmações encadeadas por "
                    "“pois”. A primeira (FPP e FPU simultaneamente) é a definição; a segunda explica o "
                    "mecanismo competitivo que leva até lá. O risco é desconfiar do “simultaneamente” ou do "
                    "nexo causal — ambos corretos no modelo competitivo."),
        modulos=[("😈 Para dificultar", [
            "<i>“Basta que a economia esteja sobre a fronteira de possibilidades de produção para que se "
            "alcance o ótimo de Pareto.”</i> → ERRADO (restrição indevida: falta a eficiência na troca e no "
            "mix, TMS = TMT)",
            "<i>“No ótimo de Pareto, a taxa marginal de substituição dos consumidores iguala a taxa marginal "
            "de transformação da economia.”</i> → CERTO",
        ])],
        tipo_erro=["DETALHE", "PARAFRASE_FIEL"], dificuldade=2,
        comentario_fonte=("CERTO. No ótimo de Pareto em equilíbrio geral, a economia atinge eficiência na produção "
                          "(FPP) e na alocação dos bens entre os consumidores (FPU). Os preços relativos orientam "
                          "a produção (escassez) e as escolhas dos consumidores (preferências e utilidade "
                          "marginal)."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0153
    card(
        "E1-0153", "efi", COM_PARETO,
        assertiva="A alocação eficiente dos recursos produtivos garante maior equidade social.",
        gabarito="ERRADO",
        anotada=(az("A alocação eficiente dos recursos produtivos ") + vm("garante maior equidade social")
                 + az(".")),
        poucas=(azb("Eficiência") + " e " + azb("equidade") + " são critérios independentes: uma alocação "
                "pode ser Pareto-eficiente e " + vd("extremamente desigual") + ". Eficiência não garante "
                "justiça distributiva."),
        destrinchando=[
            "Eficiência alocativa (ótimo de Pareto) responde à pergunta “há desperdício?”. Equidade responde "
            "a “a distribuição é justa?”. A primeira é positiva; a segunda depende de um juízo de valor "
            "(critério distributivo).",
            "Toda a curva de contrato é eficiente — inclusive os pontos próximos das origens, em que um "
            "consumidor fica com quase tudo. O mercado competitivo leva a um ponto eficiente que reflete a "
            "<b>dotação inicial</b>: se ela é desigual, o resultado também será.",
            "O " + azb("2º Teorema do Bem-Estar") + " sugere o caminho para conciliar os dois: redistribuir as "
            "dotações (idealmente com transferências de montante fixo) e deixar o mercado operar. Na prática, "
            "tributos e transferências reais alteram incentivos, e surge o " + azb("trade-off entre "
            "equidade e eficiência") + " — o “grande dilema” de " + oc("Arthur Okun") + " (<i>Equality and "
            "Efficiency: The Big Tradeoff</i>, 1975).",
            "Por isso a política pública trata as duas dimensões com instrumentos diferentes: concorrência e "
            "correção de falhas de mercado para a eficiência; tributação progressiva e transferências para a "
            "equidade.",
            vm("Regra-âncora: eficiência diz se o bolo é o maior possível; equidade, como ele é repartido."),
        ],
        dissecando=(cz("[nexo indevido]") + " O item cria uma relação causal entre dois conceitos que a teoria "
                    "separa. O verbo “garante” agrava: nem uma relação de tendência seria correta."),
        modulos=[("😈 Para dificultar", [
            "<i>“Uma alocação Pareto-eficiente pode ser socialmente indesejável do ponto de vista "
            "distributivo.”</i> → CERTO",
            "<i>“Toda redistribuição de renda reduz a eficiência econômica.”</i> → ERRADO (modulador absoluto: "
            "transferências de montante fixo não distorcem)",
        ])],
        reescrita=("A alocação eficiente dos recursos produtivos " + hl("não garante, por si só,")
                   + " maior equidade social."),
        tipo_erro=["NEXO_INDEVIDO"], dificuldade=1,
        comentario_fonte=("ERRADO. A eficiência alocativa diz respeito ao uso mais produtivo possível dos "
                          "recursos, mas não garante equidade. É possível ter uma alocação altamente desigual e "
                          "ainda assim eficiente de Pareto; a equidade depende de critérios distributivos, "
                          "normativos."),
        qualidade_fonte="bom",
    ),
    # ------------------------------------------------------------------ E1-0154
    card(
        "E1-0154", "efi", COM_PARETO,
        assertiva=("Com a eficiência de Pareto não há como melhorar o bem-estar de ambos os indivíduos: se "
                   "melhorar a condição de um, será à custa do outro."),
        gabarito="CERTO",
        anotada=az("Com a eficiência de Pareto não há como melhorar o bem-estar de ambos os indivíduos: <u>se "
                   "melhorar a condição de um, será à custa do outro</u>."),
        poucas=("Na alocação " + azb("Pareto-eficiente") + " (de dois indivíduos, como na caixa de "
                "Edgeworth), as trocas vantajosas se esgotaram: qualquer ganho de um " + vd("exige a perda") + " "
                "do outro."),
        destrinchando=[
            "O item descreve o caso de dois agentes (“ambos”), típico da " + azb("caixa de Edgeworth") + ". "
            "Num ponto da curva de contrato, as curvas de indiferença são tangentes: mover-se para melhorar A "
            "leva B para uma curva de indiferença inferior.",
            "Nas duas metades da frase estão as duas formulações equivalentes: (1) não dá para melhorar "
            "todos ao mesmo tempo; (2) melhorar um exige piorar outro.",
            "No espaço das utilidades, a " + azb("fronteira de possibilidades de utilidade") + " é "
            "negativamente inclinada justamente por isso: ao longo dela, U<sub>A</sub> só sobe se "
            "U<sub>B</sub> cair.",
            "O conceito é <b>local à alocação</b>: dizer que uma alocação é eficiente não diz nada sobre "
            "outras. A partir de uma alocação ineficiente, ambos podem melhorar — e é isso que as trocas "
            "voluntárias fazem até atingir a curva de contrato.",
        ],
        dissecando=(cz("[paráfrase fiel]") + " Reformulação coloquial da definição. Quem pensa em “trocas "
                    "ganha-ganha” pode marcar ERRADO por intuição; o ganha-ganha existe só <b>antes</b> de se "
                    "alcançar a eficiência."),
        modulos=[("😈 Para dificultar", [
            "<i>“Em uma alocação eficiente de Pareto, ainda é possível que ambos os indivíduos melhorem por "
            "meio de trocas voluntárias.”</i> → ERRADO (contradição: isso caracteriza a alocação "
            "ineficiente)",
            "<i>“Ao longo da fronteira de possibilidades de utilidade, o aumento da utilidade de um indivíduo "
            "implica redução da do outro.”</i> → CERTO",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], dificuldade=1,
        comentario_fonte=("CERTO. Em uma alocação eficiente de Pareto, ninguém consegue aumentar o próprio "
                          "bem-estar sem reduzir o bem-estar de outra pessoa. [imagem]"),
        qualidade_fonte="raso",
        figuras_fonte=[img_verso("Untitled (33).jpeg")],
    ),
    # ------------------------------------------------------------------ E1-0155
    card(
        "E1-0155", "efi", COM_TEOREMAS,
        assertiva=("O Primeiro Teorema do Bem-Estar explica que, em um mercado onde todos competem justamente, "
                   "as trocas que beneficiam ambas as partes vão acontecer até não ser possível fazer mais "
                   "nenhuma troca vantajosa."),
        gabarito="CERTO",
        anotada=az("O Primeiro Teorema do Bem-Estar explica que, em um mercado onde todos competem justamente, "
                   "as trocas que beneficiam ambas as partes vão acontecer <u>até não ser possível fazer mais "
                   "nenhuma troca vantajosa</u>."),
        poucas=("É a intuição do " + azb("1º Teorema") + ": em concorrência, as trocas voluntárias prosseguem "
                "até se esgotarem os ganhos mútuos — e a alocação resultante é " + vd("Pareto-eficiente")
                + "."),
        destrinchando=[
            "Toda troca voluntária é uma pequena melhoria de Pareto: só acontece se as duas partes ganham (ou "
            "ao menos uma ganha e a outra não perde). Enquanto houver diferenças entre as TMS dos agentes, "
            "existe troca vantajosa a fazer.",
            "Em concorrência perfeita, todos enfrentam os mesmos preços e ajustam suas TMS à mesma razão de "
            "preços. Quando o mercado se equilibra, as TMS estão igualadas e não sobra ganho de troca: a "
            "alocação está na " + azb("curva de contrato") + ".",
            "“Competem justamente” é forma coloquial de dizer " + azb("concorrência perfeita") + ": muitos "
            "agentes tomadores de preço, sem poder de mercado, com informação perfeita e mercados completos.",
            "O resultado é eficiente, mas não necessariamente equitativo: o ponto da curva de contrato "
            "atingido depende da dotação inicial. Corrigir a distribuição é tarefa do " + azb("2º Teorema")
            + " (redistribuir dotações).",
        ],
        dissecando=(cz("[paráfrase fiel]") + " Versão em linguagem leiga do 1º Teorema. O “justamente” pode "
                    "soar como juízo de valor e assustar; no contexto, significa concorrência sem poder de "
                    "mercado, não justiça distributiva."),
        modulos=[("😈 Para dificultar", [
            "<i>“O Primeiro Teorema do Bem-Estar garante que, em concorrência perfeita, o resultado das trocas "
            "será equitativo.”</i> → ERRADO (troca de conceito: eficiente, não equitativo)",
            "<i>“Em concorrência perfeita, as trocas cessam quando as taxas marginais de substituição dos "
            "agentes se igualam.”</i> → CERTO",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], dificuldade=1,
        comentario_fonte=("CERTO. O resultado final é que os recursos são distribuídos de maneira eficiente, de "
                          "acordo com o critério de Pareto, em que não se pode melhorar a situação de alguém sem "
                          "piorar a de outra pessoa. [imagens]"),
        qualidade_fonte="raso",
        figuras_fonte=[img_verso("Untitled (47).jpeg"), img_verso("Untitled (34).jpeg")],
    ),
    # ------------------------------------------------------------------ E1-0156
    card(
        "E1-0156", "efi", COM_TEOREMAS,
        assertiva=("O Segundo Teorema do Bem-Estar sugere que é possível redistribuir a riqueza de forma a manter "
                   "o mesmo nível de satisfação geral que havia antes da redistribuição."),
        gabarito="CERTO", status="contestavel",
        anotada=az("O Segundo Teorema do Bem-Estar sugere que <u>é possível</u> redistribuir a riqueza de forma "
                   "a manter o mesmo nível de <u>satisfação geral</u> que havia antes da redistribuição."),
        poucas=("Na leitura que sustenta o gabarito, o " + azb("2º Teorema") + " mostra que se pode "
                "redistribuir riqueza " + vd("sem perder eficiência") + ": a economia muda de ponto, mas "
                "continua na fronteira de Pareto."),
        condicionais=[("⚠️ Gabarito contestável",
                       "A redação é imprecisa. Se “satisfação geral” for lida como <b>eficiência</b> (permanecer "
                       "na fronteira de possibilidades de utilidade), o item é CERTO. Se for lida como “cada um "
                       "fica tão bem quanto antes”, é ERRADO: redistribuir move a economia <b>ao longo</b> da "
                       "fronteira, e quem perde riqueza fica pior. A leitura de eficiência é a mais defensável "
                       "e a que sustenta o gabarito.")],
        destrinchando=[
            "Enunciado do " + azb("2º Teorema do Bem-Estar") + ": sob preferências convexas e as demais "
            "hipóteses do modelo competitivo, " + vd("toda") + " alocação Pareto-eficiente pode ser alcançada "
            "como equilíbrio competitivo, desde que as dotações iniciais sejam redistribuídas adequadamente.",
            "Implicação: a sociedade pode escolher a distribuição que julgar justa e chegar a ela "
            "redistribuindo riqueza por " + azb("transferências de montante fixo") + " (lump-sum) e deixando "
            "o mercado operar. Não há perda de eficiência — o “bolo” continua do tamanho máximo, só que "
            "repartido de outro modo.",
            "O que o teorema <b>não</b> diz: que todos ficam tão bem quanto antes. Mover-se ao longo da "
            "fronteira de Pareto melhora uns e piora outros, por definição. A afirmação do comentário de "
            "origem de que “todos ficam tão bem quanto estavam” está errada.",
            "Contraste com o caminho alternativo — controlar preços (tabelamentos, subsídios cruzados) para "
            "redistribuir: isso gera " + azb("peso morto") + " e tira a economia da fronteira. O 2º Teorema "
            "recomenda mexer nas dotações, não nos preços.",
            "Limite prático: tributos reais (sobre renda, consumo) alteram incentivos; transferências "
            "verdadeiramente lump-sum são raras.",
        ],
        dissecando=(cz("[modulador relativo]") + " O “sugere que é possível” suaviza a afirmação, e a "
                    "expressão vaga “satisfação geral” abre duas leituras. A banca pensou em eficiência "
                    "agregada; o candidato que lê “cada um fica igual” tende a marcar ERRADO. Diante de "
                    "redação ambígua, prefira a leitura que corresponde ao enunciado de manual."),
        modulos=[("😈 Para dificultar", [
            "<i>“O Segundo Teorema do Bem-Estar mostra que é possível redistribuir a riqueza sem que nenhum "
            "indivíduo tenha seu bem-estar reduzido.”</i> → ERRADO (generalização: redistribuir piora quem "
            "perde dotação)",
            "<i>“Segundo o Segundo Teorema do Bem-Estar, questões distributivas podem ser tratadas por "
            "redistribuição de dotações, sem necessidade de distorcer os preços.”</i> → CERTO",
        ])],
        tipo_erro=["MODULADOR_RELATIVO"], dificuldade=3,
        comentario_fonte=("CERTO. O 2º Teorema mostra que, sob certas circunstâncias, qualquer alocação ótima de "
                          "Pareto pode se basear no mecanismo de livre mercado. Por meio do livre mercado, as "
                          "redistribuições de riqueza podem ser feitas de maneira que todos fiquem tão bem quanto "
                          "estavam anteriormente. [imagem]"),
        qualidade_fonte="com_erro",
        figuras_fonte=[img_verso("Untitled (35).jpeg")],
        alertas=["contestavel: redação ambígua (“mesmo nível de satisfação geral”); gabarito CERTO mantido na "
                 "leitura de eficiência — na leitura literal (todos tão bem quanto antes), seria ERRADO",
                 "qualidade_fonte: o comentário de origem afirma que a redistribuição deixa “todos tão bem "
                 "quanto estavam anteriormente”, o que é falso — corrigido no 📖"],
    ),
    # ------------------------------------------------------------------ E1-0157
    card(
        "E1-0157", "trib", COM_TRIB,
        assertiva="A tributação afeta diretamente a eficiência de Pareto porque altera os incentivos de mercado.",
        gabarito="CERTO",
        anotada=az("A tributação <u>afeta</u> diretamente a eficiência de Pareto porque altera os incentivos de "
                   "mercado."),
        poucas=("Tributos sobre bens, renda ou produção criam uma " + azb("cunha") + " entre o preço pago pelo "
                "comprador e o recebido pelo vendedor; os agentes reagem, trocas vantajosas deixam de ocorrer "
                "e surge " + vd("peso morto") + "."),
        destrinchando=[
            "Com um imposto, o comprador paga pc e o vendedor recebe pv < pc. O comprador ajusta sua TMS a pc, "
            "o vendedor ajusta o custo marginal a pv: as condições de eficiência (TMS = TMT, p = CMg) deixam "
            "de valer. A quantidade cai abaixo da eficiente — é o " + azb("peso morto") + " (ou "
            + azb("excesso de carga") + ").",
            "A distorção cresce com as elasticidades (mais reação dos agentes) e, aproximadamente, com o "
            + vd("quadrado da alíquota") + ".",
            "Exceções que testam o item: (1) " + azb("tributo de montante fixo") + " (lump-sum), que não "
            "depende de nenhuma decisão do contribuinte e por isso não altera incentivos na margem — é o "
            "instrumento ideal do 2º Teorema; (2) " + azb("tributo pigouviano") + " (" + oc("Pigou")
            + ", 1920), que incide sobre uma externalidade negativa e <b>melhora</b> a eficiência, porque "
            "corrige um preço que estava errado.",
            "Por isso o verbo “afeta” é o adequado: a tributação, em regra, reduz a eficiência; a pigouviana "
            "a aumenta; a lump-sum a preserva. Em todos os casos, o canal é o mesmo — os incentivos.",
        ],
        dissecando=(cz("[modulador relativo]") + " O verbo neutro “afeta” (e não “reduz”) salva o item das "
                    "exceções. Se a banca escrevesse “toda tributação reduz a eficiência”, a pigouviana e a "
                    "lump-sum o tornariam ERRADO."),
        modulos=[("😈 Para dificultar", [
            "<i>“Todo tributo reduz a eficiência de Pareto, pois altera os incentivos de mercado.”</i> → ERRADO "
            "(modulador absoluto: lump-sum não distorce e o pigouviano corrige externalidade)",
            "<i>“Um tributo de montante fixo, por não depender das decisões dos agentes, não gera peso "
            "morto.”</i> → CERTO",
        ])],
        tipo_erro=["MODULADOR_RELATIVO"], dificuldade=2,
        comentario_fonte=("CERTO. Impostos sobre bens, serviços, renda ou produção modificam os preços relativos, "
                          "e isso pode afastar consumidores e produtores de suas escolhas ótimas."),
        qualidade_fonte="raso",
    ),
]
