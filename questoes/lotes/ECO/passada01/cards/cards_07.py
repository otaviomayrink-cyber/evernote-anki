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
]
