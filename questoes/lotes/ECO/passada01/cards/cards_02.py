"""Cards da passada 01 de ECO — lote de redação 02 (E1-0051 a E1-0082)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "fund": "🧭 Fundamentos e escassez",
    "dem": "📈 Demanda: determinantes e deslocamentos",
    "of": "🏭 Oferta: determinantes e deslocamentos",
    "bens": "🏷️ Classificação dos bens",
    "eq": "⚖️ Equilíbrio e estática comparativa",
}

CMD_OD = "Julgue o item a seguir, relativo à demanda, à oferta e ao equilíbrio de mercado."
CMD_BENS = "Julgue o item a seguir, relativo à classificação dos bens e aos determinantes da demanda."
CMD_FUND = "Julgue o item a seguir, relativo aos conceitos fundamentais da economia."

BASE = {"destino": "01", "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None,
        "cacd": False, "errei": False, "rotulo_item": "Item", "gabarito_origem": "fonte", "status": "normal"}


def card(**kw):
    d = dict(BASE)
    d.update(kw)
    return d


def img_perdida(ref, desenho=None):
    acao = "irrecuperavel" if not desenho else f"irrecuperavel (substituída pelo gráfico didático {desenho})"
    return {"ref": ref, "tipo_fonte": "não identificado (imagem do caderno E1 não preservada)", "lado": "verso",
            "acao": acao}


CARDS = [
    # ------------------------------------------------------------------ E1-0051
    card(
        id="ECO-E1-0051-1", fonte_ref="E1-0051", subtema=H2["dem"], comando=CMD_OD,
        assertiva=("Uma campanha midiática anuncia as vantagens de um determinado bem normal X. É de se esperar que "
                   "o volume de negócios de curto prazo no mercado aumente porque haverá um deslocamento, para a "
                   "direita, da curva de demanda."),
        gabarito="CERTO",
        anotada=az("Uma campanha midiática anuncia as vantagens de um determinado bem normal X. É de se esperar que "
                   "o volume de negócios de curto prazo no mercado <u>aumente</u> porque haverá um "
                   "<u>deslocamento, para a direita, da curva de demanda</u>."),
        poucas=("A campanha muda as " + azb("preferências") + " a favor de X: a demanda se desloca para a direita "
                "e, com a oferta inalterada, sobem o preço e a " + vd("quantidade transacionada") + " — o volume "
                "de negócios aumenta."),
        destrinchando=[
            "Propaganda não mexe no preço de X: mexe nos " + azb("gostos e preferências") + ", um dos "
            "determinantes da demanda que ficam no “tudo o mais constante” da curva. Mudou o determinante, a "
            "curva inteira se desloca — aqui, para a direita (mais quantidade desejada a cada preço).",
            "Efeito no mercado, com oferta positivamente inclinada e parada: o novo equilíbrio tem " + vd("p ↑")
            + " e " + vd("q ↑") + ". “Volume de negócios” pode ser lido como quantidade transacionada ou como "
            "valor transacionado (p × q); como p e q sobem juntos, os dois aumentam e o item vale em qualquer "
            "leitura.",
            "“Curto prazo” não muda a conclusão: só limita o tamanho da resposta da quantidade (oferta mais "
            "inclinada no curto prazo → mais efeito no preço, menos na quantidade). Só uma oferta perfeitamente "
            "inelástica (vertical) faria a quantidade ficar parada.",
            "O “bem normal” é um dado decorativo: a campanha desloca a demanda de qualquer bem, normal ou "
            "inferior. A classificação pela renda só importaria se o choque fosse de renda.",
            vm("Regra-âncora: demanda para a direita com oferta constante → preço e quantidade sobem juntos."),
        ],
        grafico_verso="ECO-E1-0051-1-V1",
        dissecando=(cz("[paráfrase fiel · detalhe]") + " O item encadeia causa (preferências) → deslocamento → "
                    "resultado de mercado, e tudo está certo. Os riscos são o ruído: “bem normal” (que tenta "
                    "puxar para efeito-renda) e “curto prazo” (que sugere que nada mudaria)."),
        modulos=[("😈 Para dificultar", [
            "<i>“…o volume de negócios aumenta, mas o preço de equilíbrio permanece inalterado.”</i> → ERRADO "
            "(com oferta inclinada o preço também sobe)",
            "<i>“…haverá um movimento ao longo da curva de demanda, em razão da redução do preço de X.”</i> → "
            "ERRADO (troca de conceito: propaganda desloca a curva)",
        ])],
        tipo_erro=["PARAFRASE_FIEL", "DETALHE"], moduladores=["é de se esperar"], dificuldade=1,
        comentario_fonte="CERTO. A campanha gera aumento na preferência, deslocando a curva de demanda para a "
                         "direita.",
        qualidade_fonte="raso",
        figuras_fonte=[img_perdida("Untitled (4).jpeg", "ECO-E1-0051-1-V1")],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0052
    card(
        id="ECO-E1-0052-1", fonte_ref="E1-0052", subtema=H2["dem"], comando=CMD_OD,
        assertiva=("O aluguel médio de imóveis poderá cair quando há mudança na preferência dos usuários em face "
                   "da desvalorização de uma região."),
        gabarito="CERTO",
        anotada=az("O aluguel médio de imóveis <u>poderá cair</u> quando há mudança na preferência dos usuários "
                   "em face da desvalorização de uma região."),
        poucas=("A região perde atratividade: a " + azb("demanda") + " por imóveis ali se desloca para a "
                "<b>esquerda</b> e, com a oferta de imóveis dada, o preço do serviço de moradia — o "
                + vd("aluguel") + " — cai."),
        destrinchando=[
            "O aluguel é o <b>preço</b> do serviço de moradia. A desvalorização da região (violência, perda de "
            "infraestrutura, mudança de fluxo comercial) altera as " + azb("preferências") + " dos inquilinos: "
            "a cada aluguel, menos gente quer morar ali. É um deslocamento da curva, não um movimento ao longo "
            "dela.",
            "O estoque de imóveis é muito " + azb("inelástico no curto prazo") + " (não se “desconstrói” "
            "prédio): a oferta é quase vertical. Por isso a queda de demanda recai quase toda sobre o "
            + vd("preço") + ", e pouco sobre a quantidade de imóveis alugados.",
            "Exemplo e contraexemplo: a chegada de uma estação de metrô valoriza a região → demanda para a "
            "direita → aluguel sobe; a instalação de um lixão ao lado → demanda para a esquerda → aluguel cai.",
            "O raciocínio é o mesmo para o preço de venda dos imóveis, que embute o valor presente dos aluguéis "
            "futuros.",
        ],
        dissecando=(cz("[modulador relativo]") + " O “poderá” protege o item: a queda é o efeito esperado "
                    "<i>ceteris paribus</i>, ainda que outro choque simultâneo (alta de juros, nova lei) pudesse "
                    "compensá-lo. A banca usa linguagem do cotidiano (“usuários”, “aluguel médio”) para "
                    "esconder um caso simples de deslocamento da demanda."),
        modulos=[("😈 Para dificultar", [
            "<i>“…a desvalorização da região reduz a quantidade demandada de imóveis por meio de movimento ao "
            "longo da curva de demanda.”</i> → ERRADO (troca de conceito: é deslocamento da curva)",
            "<i>“…o aluguel médio necessariamente cairá na mesma proporção da queda da demanda.”</i> → ERRADO "
            "(modulador absoluto; a proporção depende das elasticidades)",
        ])],
        tipo_erro=["MODULADOR_RELATIVO"], moduladores=["poderá"], dificuldade=1,
        comentario_fonte="CERTO. A mudança na preferência reduz a demanda, baixando os preços.",
        qualidade_fonte="raso",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0054
    card(
        id="ECO-E1-0054-1", fonte_ref="E1-0054", subtema=H2["dem"], comando=CMD_OD,
        assertiva="O aumento do preço dos carros levará a uma queda na demanda por motocicleta.",
        gabarito="ERRADO",
        anotada=az("O aumento do preço dos carros levará a ") + vm("uma queda") + az(" na demanda por "
                                                                                    "motocicleta."),
        poucas=("Carro e motocicleta são " + azb("substitutos") + " (atendem à mesma necessidade de transporte "
                "individual): encarecer o carro <b>eleva</b> a demanda por motos."),
        destrinchando=[
            "Bens " + azb("substitutos") + " concorrem pela mesma necessidade. Se o carro fica mais caro, parte "
            "dos consumidores migra para a alternativa — a demanda por motocicletas se desloca para a "
            "<b>direita</b> (mais motos desejadas a cada preço de moto).",
            "Formalmente: " + azb("elasticidade-preço cruzada") + " ε<sub>moto, carro</sub> = %Δq<sub>moto</sub> "
            "/ %Δp<sub>carro</sub> " + vd("> 0") + ". Com bens " + azb("complementares") + " (carro e "
            "gasolina) o sinal é negativo: encarecer um reduz a demanda do outro.",
            "Note o objeto: no gráfico da moto, o preço do carro é <b>deslocador</b> da curva; no gráfico do "
            "carro, o mesmo aumento é só movimento ao longo da curva (cai a quantidade demandada de carros).",
            "A queda que o item descreve seria correta se os bens fossem complementares, ou se a pergunta fosse "
            "sobre a quantidade demandada de <b>carros</b>.",
            vm("Regra-âncora: ↑p de substituto → ↑demanda do outro; ↑p de complementar → ↓demanda do outro."),
        ],
        dissecando=(cz("[inversão · troca de conceito]") + " O item aplica a regra dos complementares a um "
                    "par de substitutos e inverte o sentido do efeito. Pista: perguntar “compro um <i>no lugar</i> "
                    "do outro ou <i>junto com</i> o outro?” — moto e carro são “no lugar”."),
        modulos=[("😈 Para dificultar", [
            "<i>“O aumento do preço dos carros levará a uma queda na demanda por gasolina.”</i> → CERTO",
            "<i>“O aumento do preço dos carros levará a um aumento da quantidade demandada de carros.”</i> → "
            "ERRADO (inversão: a quantidade demandada do próprio bem cai)",
        ])],
        reescrita=("O aumento do preço dos carros levará a " + hl("um aumento") + " na demanda por "
                   "motocicleta."),
        tipo_erro=["INVERSAO", "TROCA_CONCEITO"], moduladores=[], dificuldade=1,
        comentario_fonte="ERRADO. Aumento no preço de um substituto (carros) tende a aumentar a demanda por "
                         "motocicletas pois são bens, em tese, substitutos.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=["texto_corrigido: “um queda” corrigido para “uma queda” (erro evidente)"],
    ),
    # ------------------------------------------------------------------ E1-0055
    card(
        id="ECO-E1-0055-1", fonte_ref="E1-0055", subtema=H2["dem"], comando=CMD_OD,
        assertiva="A mudança no preço das bicicletas não levará a um deslocamento da curva de demanda por elas.",
        gabarito="CERTO",
        anotada=az("A mudança no preço <u>das bicicletas</u> <u>não</u> levará a um deslocamento da curva de "
                   "demanda por elas."),
        poucas=("O preço do <b>próprio</b> bem está no eixo do gráfico: alterá-lo provoca "
                + azb("movimento ao longo") + " da curva de demanda, nunca deslocamento dela."),
        destrinchando=[
            "A curva de demanda das bicicletas é q<sub>d</sub> = f(p<sub>bicicleta</sub>), mantidos constantes "
            "renda, gostos, preços de outros bens, expectativas e número de compradores. Como o preço da "
            "bicicleta já é uma das variáveis do gráfico, sua variação só leva o consumidor a outro ponto da "
            "mesma curva.",
            "Vocabulário que a banca cobra: " + azb("variação da quantidade demandada") + " (movimento ao "
            "longo; causa: preço do próprio bem) × " + azb("variação da demanda") + " (deslocamento; causa: "
            "qualquer outro determinante).",
            "Exemplos de deslocamento da demanda por bicicletas: alta da gasolina (substituto mais caro → "
            "direita), construção de ciclovias (preferências → direita), queda do preço dos patinetes "
            "elétricos (substituto mais barato → esquerda).",
            "Cuidado com a outra ponta: a mudança no preço das bicicletas <b>desloca</b> a demanda de bens "
            "relacionados a elas — capacetes (complementares) ou passes de ônibus (substitutos).",
            vm("Regra-âncora: preço do próprio bem → anda na curva; qualquer outra causa → a curva anda."),
        ],
        dissecando=(cz("[literalidade]") + " Item-espelho do clássico “deslocamento × movimento”: verdadeiro "
                    "pela própria definição de curva de demanda. A negação (“não levará”) é posta para quem "
                    "associa automaticamente “mudança de preço” a “mudança de demanda”."),
        modulos=[("😈 Para dificultar", [
            "<i>“A redução do preço das bicicletas desloca para a direita a curva de demanda por bicicletas.”</i>"
            " → ERRADO (troca de conceito: aumenta a quantidade demandada, ao longo da curva)",
            "<i>“A redução do preço das bicicletas desloca para a direita a curva de demanda por capacetes.”</i>"
            " → CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=["não"], dificuldade=1,
        comentario_fonte="CERTO. Mudança no preço provoca movimento ao longo da curva, não deslocamento da curva "
                         "de demanda.",
        qualidade_fonte="bom",
        figuras_fonte=[img_perdida("Untitled (3).jpeg")],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0056
    card(
        id="ECO-E1-0056-1", fonte_ref="E1-0056", subtema=H2["of"], comando=CMD_OD,
        assertiva=("A quantidade ofertada aumenta com o aumento de preços porque os produtores passam a "
                   "considerar mais lucrativo produzir o bem."),
        gabarito="CERTO",
        anotada=az("A quantidade ofertada aumenta com o aumento de preços <u>porque</u> os produtores passam a "
                   "considerar mais lucrativo produzir o bem."),
        poucas=("É a " + azb("lei da oferta") + ": preço maior torna a produção mais lucrativa (e cobre custos "
                "marginais mais altos), e as firmas oferecem mais — movimento <b>ao longo</b> da curva de oferta."),
        destrinchando=[
            "A curva de oferta relaciona preço do bem e " + azb("quantidade ofertada") + ", tudo o mais "
            "constante (custos dos insumos, tecnologia, preços de bens relacionados na produção, expectativas, "
            "número de vendedores). Inclinação " + vd("positiva") + ": mais preço, mais quantidade.",
            "Por que positiva: (1) cada unidade passa a render mais, então produzir fica mais " + azb("lucrativo")
            + " — o nexo do item; (2) na firma competitiva, a oferta é a curva de " + azb("custo marginal")
            + " (acima do CVMe mínimo), e o CMg costuma crescer por " + azb("rendimentos decrescentes")
            + "; só um preço maior paga as unidades mais caras; (3) preço alto atrai novas firmas.",
            "Termo exato: preço do próprio bem muda a <b>quantidade ofertada</b> (movimento ao longo). Mudança "
            "de custo de insumo ou de tecnologia muda a <b>oferta</b> (desloca a curva).",
            "Simetria com a demanda: lá a relação preço–quantidade é negativa; aqui, positiva. A banca costuma "
            "trocar os sinais.",
        ],
        dissecando=(cz("[paráfrase fiel]") + " O item dá a lei e a justificativa econômica corretas. O nexo "
                    "“porque” é o que se testa — e ele é legítimo: lucratividade é a explicação intuitiva da "
                    "inclinação positiva. Atenção ao termo “quantidade ofertada”, aqui usado com precisão."),
        modulos=[("😈 Para dificultar", [
            "<i>“A oferta aumenta (a curva se desloca para a direita) com o aumento do preço do bem.”</i> → "
            "ERRADO (troca de conceito: é a quantidade ofertada, ao longo da curva)",
            "<i>“A quantidade ofertada aumenta com o preço porque o custo marginal de produção diminui.”</i> → "
            "ERRADO (nexo indevido: o CMg tipicamente cresce)",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], moduladores=["porque"], dificuldade=1,
        comentario_fonte="CERTO. O aumento do preço torna a produção mais atraente, incentivando o aumento da "
                         "quantidade ofertada.",
        qualidade_fonte="raso",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0057
    card(
        id="ECO-E1-0057-1", fonte_ref="E1-0057", subtema=H2["dem"], comando=CMD_OD,
        assertiva="De acordo com a lei da demanda, existe uma relação positiva entre quantidade demandada e preço.",
        gabarito="ERRADO",
        anotada=az("De acordo com a lei da demanda, existe uma relação ") + vm("positiva")
                + az(" entre quantidade demandada e preço."),
        poucas=("A " + azb("lei da demanda") + " estabelece relação <b>negativa</b> (inversa): tudo o mais "
                "constante, preço maior → quantidade demandada menor. Relação positiva é a lei da "
                + azb("oferta") + "."),
        destrinchando=[
            "Enunciado da lei: <i>ceteris paribus</i>, quando o preço de um bem sobe, a quantidade demandada "
            "cai; quando cai, ela sobe. No gráfico, a curva de demanda é " + vd("negativamente inclinada") + ".",
            "Fundamentos: " + azb("efeito substituição") + " (o bem fica relativamente mais caro e o consumidor "
            "troca por outros) e " + azb("efeito renda") + " (o poder de compra cai). Para bens normais os dois "
            "atuam no mesmo sentido; soma-se a utilidade marginal decrescente.",
            "Exceções clássicas, que a banca adora: " + azb("bem de Giffen") + " (inferior, com efeito renda "
            "que supera o substituição — a curva sobe) e " + azb("bem de Veblen") + " (ostentação: o preço alto "
            "é parte do valor). São exceções, não a regra.",
            "Quem tem relação <b>positiva</b> com o preço é a quantidade <b>ofertada</b>: o item troca as duas "
            "leis.",
            vm("Regra-âncora: demanda — preço e quantidade em sentidos opostos; oferta — no mesmo sentido."),
        ],
        dissecando=(cz("[inversão]") + " Troca de uma única palavra (negativa → positiva), que transforma a "
                    "lei da demanda na lei da oferta. A banca costuma apresentar o mesmo item nas duas versões "
                    "seguidas para testar a atenção ao sinal."),
        modulos=[("😈 Para dificultar", [
            "<i>“De acordo com a lei da demanda, existe uma relação negativa entre quantidade demandada e "
            "preço.”</i> → CERTO",
            "<i>“Para um bem de Giffen, a relação entre preço e quantidade demandada é positiva.”</i> → CERTO",
        ])],
        reescrita=("De acordo com a lei da demanda, existe uma relação " + hl("negativa") + " entre quantidade "
                   "demandada e preço."),
        tipo_erro=["INVERSAO"], moduladores=[], dificuldade=1,
        comentario_fonte="ERRADO. A lei da demanda afirma que existe uma relação negativa entre preço e quantidade "
                         "demandada.",
        qualidade_fonte="bom",
        figuras_fonte=[img_perdida("Untitled (1).jpeg")],
        alertas=["texto_corrigido: “quantidade demanda” corrigido para “quantidade demandada” (erro evidente)",
                 "par_espelho: ECO-E1-0058-1 traz o mesmo item com “negativa” (CERTO)"],
    ),
    # ------------------------------------------------------------------ E1-0058
    card(
        id="ECO-E1-0058-1", fonte_ref="E1-0058", subtema=H2["dem"], comando=CMD_OD,
        assertiva="De acordo com a lei da demanda, existe uma relação negativa entre quantidade demandada e preço.",
        gabarito="CERTO",
        anotada=az("De acordo com a lei da demanda, existe uma relação <u>negativa</u> entre quantidade demandada "
                   "e preço."),
        poucas=("Correto: <i>ceteris paribus</i>, preço e " + azb("quantidade demandada") + " andam em sentidos "
                "<b>opostos</b> — por isso a curva de demanda é negativamente inclinada."),
        destrinchando=[
            "A " + azb("lei da demanda") + " é uma relação de " + vd("q<sub>d</sub> = f(p)") + " com "
            "derivada negativa: se o preço cai, compra-se mais; se sobe, compra-se menos, mantidos renda, "
            "gostos, preços de outros bens e expectativas.",
            "Três justificativas que costumam aparecer em prova: (1) " + azb("efeito substituição") + " — o bem "
            "fica relativamente mais barato e “rouba” consumo de outros; (2) " + azb("efeito renda") + " — a "
            "queda de preço aumenta o poder de compra; (3) " + azb("utilidade marginal decrescente") + " — só "
            "se compra uma unidade extra se ela custar menos, porque vale menos que a anterior.",
            "Exceções: " + azb("bem de Giffen") + " (inferior, com efeito renda negativo maior que o efeito "
            "substituição) e " + azb("bem de Veblen") + " (consumo de ostentação). Bens especulativos, comprados "
            "na expectativa de alta, também parecem contrariar a lei, mas aí o que muda é a expectativa — um "
            "deslocador da curva.",
            "Precisão de vocabulário: a lei fala de <b>quantidade demandada</b> (ponto da curva), não de "
            "“demanda” (a curva inteira).",
        ],
        dissecando=(cz("[literalidade]") + " Definição de manual, sem armadilha interna. A dificuldade está "
                    "fora do item: a banca costuma aplicar a mesma frase com “positiva” (ERRADO) ou com “oferta” "
                    "no lugar de “demanda”, e quem lê depressa não percebe a troca."),
        modulos=[("😈 Para dificultar", [
            "<i>“De acordo com a lei da demanda, existe uma relação positiva entre quantidade demandada e "
            "preço.”</i> → ERRADO (inversão: positiva é a relação da oferta)",
            "<i>“A lei da demanda vale para todos os bens, sem exceção.”</i> → ERRADO (modulador absoluto: "
            "Giffen e Veblen)",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. A lei da demanda define a relação inversa entre preço e quantidade demandada.",
        qualidade_fonte="raso",
        figuras_fonte=[img_perdida("Untitled (10).jpeg")],
        alertas=["par_espelho: ECO-E1-0057-1 traz o mesmo item com “positiva” (ERRADO)"],
    ),
    # ------------------------------------------------------------------ E1-0059
    card(
        id="ECO-E1-0059-1", fonte_ref="E1-0059", subtema=H2["eq"], comando=CMD_OD,
        assertiva=("Um acontecimento que reduza a quantidade ofertada desloca a curva de oferta para a esquerda, "
                   "ocasionando a elevação do preço de equilíbrio e da quantidade de equilíbrio."),
        gabarito="ERRADO",
        anotada=az("Um acontecimento que reduza a quantidade ofertada desloca a curva de oferta para a esquerda, "
                   "ocasionando a elevação do preço de equilíbrio ") + vm("e da quantidade de equilíbrio")
                + az("."),
        poucas=("Oferta para a esquerda com demanda constante: o preço " + vd("sobe") + ", mas a quantidade de "
                "equilíbrio " + vd("cai") + ". Preço e quantidade andam em sentidos opostos nos choques de "
                "oferta."),
        destrinchando=[
            "Choques que deslocam a oferta para a esquerda: alta no custo de insumos (salários, energia), "
            "quebra de safra, tributo sobre o produtor, saída de firmas do mercado, piora tecnológica.",
            "Na estática comparativa, o novo equilíbrio é achado <b>sobre a curva que não se mexeu</b>. A "
            "demanda ficou parada; subindo ao longo dela, preço maior vem com quantidade menor: "
            + vd("p ↑, q ↓") + ".",
            "Quadro de quatro casos (curva que se desloca, a outra constante): D → direita: p ↑, q ↑; "
            "D → esquerda: p ↓, q ↓; O → direita: p ↓, q ↑; O → esquerda: " + vd("p ↑, q ↓") + ". Nos choques "
            "de demanda, p e q andam juntos; nos de oferta, em sentidos opostos.",
            "Nota de vocabulário: a rigor, um choque que reduz a oferta a cada preço reduz a <b>oferta</b>; "
            "“quantidade ofertada” é o nome do movimento ao longo da curva. O item usa o termo de forma frouxa, "
            "mas o gabarito decorre da quantidade de equilíbrio.",
            vm("Regra-âncora: choque de oferta → preço e quantidade em sentidos opostos."),
        ],
        grafico_verso="ECO-E1-0059-1-V1",
        dissecando=(cz("[meia-verdade]") + " Tudo é verdadeiro até “elevação do preço de equilíbrio”; o erro "
                    "foi enxertado no final, colando a quantidade ao preço como se andassem juntos — o padrão "
                    "dos choques de <b>demanda</b>. Pista: em choque de oferta, desconfie de “ambos sobem”."),
        modulos=[("😈 Para dificultar", [
            "<i>“…desloca a curva de oferta para a esquerda, elevando o preço e reduzindo a quantidade de "
            "equilíbrio.”</i> → CERTO",
            "<i>“…desloca a curva de oferta para a direita, ocasionando a elevação do preço de equilíbrio.”</i> → "
            "ERRADO (sentido trocado: oferta menor vai para a esquerda)",
        ])],
        reescrita=("Um acontecimento que reduza a quantidade ofertada desloca a curva de oferta para a esquerda, "
                   "ocasionando a elevação do preço de equilíbrio e " + hl("a redução") + " da quantidade de "
                   "equilíbrio."),
        tipo_erro=["MEIA_VERDADE"], moduladores=[], dificuldade=1,
        comentario_fonte="ERRADO. A oferta menor desloca a curva de oferta para a esquerda, eleva o preço de "
                         "equilíbrio, mas reduz a quantidade de equilíbrio.",
        qualidade_fonte="bom",
        figuras_fonte=[img_perdida("Untitled (2).jpeg", "ECO-E1-0059-1-V1")],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0060
    card(
        id="ECO-E1-0060-1", fonte_ref="E1-0060", subtema=H2["bens"], comando=CMD_BENS,
        assertiva=("Substitutos são bens que atendem à mesma necessidade; o aumento do preço de um eleva a demanda "
                   "do outro."),
        gabarito="CERTO",
        anotada=az("Substitutos são bens que <u>atendem à mesma necessidade</u>; o aumento do preço de um "
                   "<u>eleva</u> a demanda do outro."),
        poucas=("Definição correta: bens " + azb("substitutos") + " concorrem pela mesma necessidade; se um "
                "encarece, o consumo migra para o outro, cuja demanda se desloca para a " + vd("direita") + "."),
        destrinchando=[
            "Medida: " + azb("elasticidade-preço cruzada") + " ε<sub>xy</sub> = %Δq<sub>x</sub> / "
            "%Δp<sub>y</sub>. Substitutos → " + vd("ε > 0") + "; complementares → " + vd("ε < 0") + "; "
            "independentes → ε = 0. Quanto maior ε, mais próximos os substitutos.",
            "Exemplo brasileiro: " + rx("gasolina e etanol") + " para os carros flex. Se a gasolina sobe, a "
            "demanda por etanol vai para a direita: mais etanol a cada preço do etanol (e, no novo equilíbrio, "
            "o preço do etanol também tende a subir).",
            "Dois planos que não se misturam: no mercado da gasolina, a alta do preço é <b>movimento ao "
            "longo</b> da curva (cai a quantidade demandada de gasolina); no mercado do etanol, é "
            "<b>deslocamento</b> da curva.",
            "Contraponto: " + azb("complementares") + " são consumidos juntos (carro e gasolina, café e "
            "açúcar); encarecer um reduz a demanda do outro.",
        ],
        dissecando=(cz("[paráfrase fiel]") + " Definição e consequência corretas, encadeadas por ponto e "
                    "vírgula. A banca costuma trocar “eleva” por “reduz” ou “substitutos” por “complementares” "
                    "— o item certo é a régua para reconhecer essas versões."),
        modulos=[("😈 Para dificultar", [
            "<i>“Substitutos são bens consumidos conjuntamente; o aumento do preço de um reduz a demanda do "
            "outro.”</i> → ERRADO (troca de conceito: isso define complementares)",
            "<i>“Entre bens substitutos, a elasticidade-preço cruzada da demanda é negativa.”</i> → ERRADO "
            "(sinal trocado: é positiva)",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Exemplo: se o preço da gasolina sobe, as pessoas procuram mais o etanol, e a "
                         "demanda por etanol aumenta (a curva se desloca para a direita e para cima).",
        qualidade_fonte="bom",
        figuras_fonte=[img_perdida("Untitled (7).jpeg")],
        alertas=["quase_duplicata: ECO-E1-0073-1 cobra a mesma definição com outra redação (mesma fonte)"],
    ),
    # ------------------------------------------------------------------ E1-0061
    card(
        id="ECO-E1-0061-1", fonte_ref="E1-0061", subtema=H2["bens"], comando=CMD_BENS,
        assertiva="Bens inferiores são aqueles cuja demanda cai quando a renda aumenta.",
        gabarito="CERTO",
        anotada=az("Bens inferiores são aqueles cuja demanda <u>cai</u> quando a renda <u>aumenta</u>."),
        poucas=("Correto: no " + azb("bem inferior") + " renda e demanda andam em sentidos opostos — renda ↑ "
                "desloca a curva para a " + vd("esquerda") + "; renda ↓, para a " + vd("direita") + "."),
        destrinchando=[
            "Classificação pela " + azb("elasticidade-renda da demanda") + " (ε<sub>R</sub> = %Δq / %Δrenda): "
            "inferior → " + vd("ε<sub>R</sub> < 0") + "; normal → ε<sub>R</sub> > 0 (necessário entre 0 e 1, "
            "superior ou de luxo acima de 1).",
            "Mecanismo: com mais renda, o consumidor troca o bem por versões que prefere e antes não podia "
            "pagar (transporte coletivo → carro próprio; carne de segunda → cortes nobres). Com menos renda, "
            "volta ao bem inferior — a demanda dele cresce na recessão.",
            "No gráfico: a mudança de renda <b>desloca</b> a curva de demanda (não é movimento ao longo dela, "
            "porque o preço do bem não mudou). O que diminui é a <b>demanda</b>, isto é, a quantidade desejada a "
            "cada preço.",
            "Inferioridade não é propriedade física do bem: depende da faixa de renda e do consumidor. O mesmo "
            "produto pode ser normal para os mais pobres e inferior para a classe média.",
            "Elo com outro tema: todo " + azb("bem de Giffen") + " é inferior, mas nem todo inferior é Giffen.",
        ],
        dissecando=(cz("[literalidade]") + " Definição de manual. A armadilha usual é a inversão (“aumenta "
                    "quando a renda aumenta”, que define o bem normal) ou a confusão entre inferior e Giffen."),
        modulos=[("😈 Para dificultar", [
            "<i>“Todo bem inferior apresenta curva de demanda positivamente inclinada.”</i> → ERRADO "
            "(generalização: só o de Giffen)",
            "<i>“A elasticidade-renda da demanda de um bem inferior é negativa.”</i> → CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Aumento de renda reduz o consumo do bem inferior e desloca a demanda para a "
                         "esquerda; queda de renda desloca para a direita. A fonte fala em “retração na "
                         "quantidade demandada”, termo impróprio para deslocamento da curva.",
        qualidade_fonte="com_erro",
        figuras_fonte=[img_perdida("Untitled (6).jpeg"), img_perdida("Untitled (8).jpeg")],
        alertas=["qualidade_fonte: o comentário de origem chama de “retração na quantidade demandada” o "
                 "deslocamento da curva (é redução da demanda)",
                 "quase_duplicata: ECO-E1-0072-1 cobra a mesma definição com outra redação (mesma fonte)"],
    ),
    # ------------------------------------------------------------------ E1-0062
    card(
        id="ECO-E1-0062-1", fonte_ref="E1-0062", subtema=H2["bens"], comando=CMD_BENS,
        assertiva="Se dois bens são consumidos juntos, tais bens são denominados substitutos.",
        gabarito="ERRADO",
        anotada=az("Se dois bens são consumidos juntos, tais bens são denominados ") + vm("substitutos")
                + az("."),
        poucas=("Bens consumidos juntos são " + azb("complementares") + " (carro e gasolina, pão e manteiga). "
                + azb("Substitutos") + " são consumidos <b>um no lugar do outro</b>."),
        destrinchando=[
            azb("Complementares") + ": a utilidade de um depende do outro. Encarecer um reduz a demanda do "
            "outro; " + azb("elasticidade-preço cruzada") + " " + vd("negativa") + ". Exemplos: impressora e "
            "cartucho, carne e carvão, celular e plano de dados.",
            azb("Substitutos") + ": satisfazem a mesma necessidade. Encarecer um eleva a demanda do outro; "
            "elasticidade cruzada " + vd("positiva") + ". Exemplos: manteiga e margarina, ônibus e metrô, "
            "gasolina e etanol.",
            "Casos-limite: " + azb("complementares perfeitos") + " (pé direito e pé esquerdo do sapato: curvas "
            "de indiferença em L) e " + azb("substitutos perfeitos") + " (duas marcas idênticas: curvas de "
            "indiferença retas).",
            "Teste rápido: “compro <i>junto com</i>” → complementar; “compro <i>em vez de</i>” → substituto.",
            vm("Regra-âncora: juntos = complementares (ε cruzada < 0); no lugar = substitutos (ε cruzada > 0)."),
        ],
        dissecando=(cz("[troca de conceito]") + " Condição verdadeira (“consumidos juntos”) com o rótulo do "
                    "conceito vizinho. Item de uma palavra: basta trocar o nome da classe."),
        modulos=[("😈 Para dificultar", [
            "<i>“Se dois bens são consumidos juntos, a elevação do preço de um tende a reduzir a demanda do "
            "outro.”</i> → CERTO",
            "<i>“Se dois bens são complementares, sua elasticidade-preço cruzada é positiva.”</i> → ERRADO "
            "(sinal trocado: é negativa)",
        ])],
        reescrita=("Se dois bens são consumidos juntos, tais bens são denominados " + hl("complementares") + "."),
        tipo_erro=["TROCA_CONCEITO"], moduladores=[], dificuldade=1,
        comentario_fonte="ERRADO. Substitutos são bens que atendem à mesma necessidade; o aumento do preço de um "
                         "eleva a demanda do outro.",
        qualidade_fonte="raso",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0063
    card(
        id="ECO-E1-0063-1", fonte_ref="E1-0063", subtema=H2["eq"], comando=CMD_OD,
        assertiva=("Uma queda em ambos – preço e quantidade – é devido à queda da demanda, com a oferta "
                   "constante."),
        gabarito="CERTO",
        anotada=az("Uma queda em <u>ambos</u> – preço e quantidade – é devido à queda da demanda, <u>com a "
                   "oferta constante</u>."),
        poucas=("Com a oferta parada, a demanda para a " + vd("esquerda") + " leva o equilíbrio para baixo ao "
                "longo da oferta: " + vd("p ↓ e q ↓") + " — a assinatura de um choque negativo de demanda."),
        destrinchando=[
            "Estática comparativa: o novo equilíbrio fica sobre a curva que não se mexeu. Se a oferta está "
            "constante e positivamente inclinada, descer por ela significa preço menor <b>e</b> quantidade "
            "menor.",
            "Leitura inversa (diagnóstico): observar p e q caindo juntos aponta para queda de demanda; "
            "p subindo com q caindo aponta para queda de oferta. Choques de demanda movem p e q no mesmo "
            "sentido; choques de oferta, em sentidos opostos.",
            "Causas típicas da queda de demanda: queda de renda (bem normal), barateamento de um substituto, "
            "encarecimento de um complementar, mudança de gostos, expectativa de preço menor no futuro.",
            "A ressalva “com a oferta constante” é essencial: se as duas curvas se movem, o resultado pode ser "
            "ambíguo (ex.: demanda e oferta caem juntas → q cai, p indeterminado).",
            "O ajuste dos vendedores — oferecer menos porque o preço caiu — é <b>movimento ao longo</b> da "
            "oferta, não deslocamento dela.",
        ],
        grafico_verso="ECO-E1-0063-1-V1",
        dissecando=(cz("[paráfrase fiel]") + " O item descreve o resultado (p e q caem) e atribui a causa "
                    "correta, com a cláusula que fecha as outras explicações (“oferta constante”). A banca "
                    "inverte trocando “demanda” por “oferta” ou tirando a cláusula."),
        modulos=[("😈 Para dificultar", [
            "<i>“Uma queda em ambos – preço e quantidade – é devida ao aumento da oferta, com a demanda "
            "constante.”</i> → ERRADO (aumento de oferta reduz p mas eleva q)",
            "<i>“Queda simultânea de demanda e de oferta reduz necessariamente o preço de equilíbrio.”</i> → "
            "ERRADO (o preço fica indeterminado)",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], moduladores=["com a oferta constante"], dificuldade=1,
        comentario_fonte="CERTO. A queda da demanda reduz o preço e a quantidade de equilíbrio; exemplo de "
                         "restaurantes que baixam preços e reduzem a produção diante de menos clientes.",
        qualidade_fonte="bom",
        figuras_fonte=[img_perdida("Untitled (5).jpeg", "ECO-E1-0063-1-V1")],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0064
    card(
        id="ECO-E1-0064-1", fonte_ref="E1-0064", subtema=H2["dem"], comando=CMD_OD,
        assertiva=("Um aumento do gasto com propaganda e marketing tende a deslocar a curva de demanda para a "
                   "direita, aumentando a demanda do bem."),
        gabarito="CERTO",
        anotada=az("Um aumento do gasto com propaganda e marketing <u>tende a</u> deslocar a curva de demanda "
                   "para a direita, aumentando a demanda do bem."),
        poucas=("Propaganda atua sobre " + azb("gostos e preferências") + ": mais consumidores querem o bem a "
                "cada preço, e a curva de demanda se desloca para a " + vd("direita") + "."),
        destrinchando=[
            "Determinantes da demanda além do preço do próprio bem: renda, preços de substitutos e "
            "complementares, " + azb("preferências") + ", expectativas e número de consumidores. Propaganda e "
            "marketing são a forma deliberada de a empresa mexer no terceiro.",
            "Efeito: a curva inteira vai para a direita (" + azb("aumento da demanda") + "). Com a oferta "
            "constante, sobem preço e quantidade de equilíbrio.",
            "Segundo objetivo frequente: tornar a demanda " + azb("menos elástica") + ", criando fidelidade à "
            "marca e diferenciação. É o terreno da " + azb("concorrência monopolística") + " (" + oc("Chamberlin")
            + ", 1933), em que a firma tem algum poder de preço justamente por diferenciar o produto.",
            "O “tende a” é a ressalva adequada: a campanha pode fracassar, ou o efeito ser anulado por choque "
            "contrário; mas o efeito esperado, <i>ceteris paribus</i>, é deslocar a curva para a direita.",
        ],
        dissecando=(cz("[modulador relativo · paráfrase fiel]") + " “Tende a” torna o item seguro. A frase "
                    "usa “demanda” no sentido técnico correto (curva), e é aí que a banca costuma errar de "
                    "propósito, trocando por “quantidade demandada”."),
        modulos=[("😈 Para dificultar", [
            "<i>“Um aumento do gasto com propaganda eleva a quantidade demandada, por movimento ao longo da "
            "curva de demanda.”</i> → ERRADO (troca de conceito: desloca a curva)",
            "<i>“Um aumento do gasto com propaganda desloca a curva de oferta do bem para a direita.”</i> → "
            "ERRADO (troca de curva: é a demanda)",
        ])],
        tipo_erro=["MODULADOR_RELATIVO", "PARAFRASE_FIEL"], moduladores=["tende a"], dificuldade=1,
        comentario_fonte="CERTO. Propaganda eficaz desloca a curva de demanda para a direita, elevando a demanda.",
        qualidade_fonte="raso",
        figuras_fonte=[img_perdida("Untitled (9).jpeg")],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0065
    card(
        id="ECO-E1-0065-1", fonte_ref="E1-0065", subtema=H2["fund"], comando=CMD_FUND,
        assertiva=("O custo de oportunidade de alguma coisa é a alternativa que tem de ser sacrificada a fim de se "
                   "obter alguma outra coisa."),
        gabarito="CERTO",
        anotada=az("O custo de oportunidade de alguma coisa é a <u>alternativa que tem de ser sacrificada</u> a "
                   "fim de se obter alguma outra coisa."),
        poucas=("Definição clássica: " + azb("custo de oportunidade") + " é aquilo de que se abre mão — a "
                "melhor alternativa sacrificada — para obter algo, consequência direta da " + azb("escassez") + "."),
        destrinchando=[
            "Como os recursos (tempo, dinheiro, fatores de produção) são escassos, toda escolha implica "
            "renúncia. O custo econômico de uma decisão é o valor da " + vd("melhor alternativa preterida")
            + ", não a soma de todas as alternativas possíveis.",
            "É um dos princípios de " + oc("Mankiw") + " (<i>Introdução à Economia</i>): “o custo de alguma "
            "coisa é aquilo de que você desiste para obtê-la”. Exemplo clássico: o custo de cursar a faculdade "
            "inclui o salário que se deixa de ganhar, não só mensalidades.",
            "Custo de oportunidade inclui " + azb("custos implícitos") + " (sem desembolso). Por isso o "
            + azb("lucro econômico") + " (receita − custos explícitos − implícitos) é menor que o lucro contábil; "
            "lucro econômico zero significa que o empresário ganha exatamente o que ganharia na melhor "
            "alternativa.",
            "No gráfico: a " + azb("curva de possibilidades de produção") + " mostra o custo de oportunidade "
            "como inclinação; côncava → custo de oportunidade crescente, porque os recursos não são igualmente "
            "aptos para os dois bens.",
            "É também a base da " + azb("vantagem comparativa") + " (" + oc("David Ricardo") + "): especializa-se "
            "quem tem o menor custo de oportunidade.",
        ],
        dissecando=(cz("[literalidade]") + " Definição de manual. Itens errados sobre o tema costumam dizer "
                    "que o custo de oportunidade é a soma de todas as alternativas, que só existe com "
                    "desembolso de dinheiro ou que “custos afundados” devem entrar na decisão."),
        modulos=[("😈 Para dificultar", [
            "<i>“O custo de oportunidade corresponde à soma de todas as alternativas abandonadas.”</i> → "
            "ERRADO (é só a melhor alternativa sacrificada)",
            "<i>“Só há custo de oportunidade quando a escolha envolve desembolso monetário.”</i> → ERRADO "
            "(restrição indevida: inclui custos implícitos, como o tempo)",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Exemplo: escolher entre um curso gratuito de um dia e um dia de descanso; o "
                         "custo de oportunidade de cada escolha é o benefício da opção abandonada.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0066
    card(
        id="ECO-E1-0066-1", fonte_ref="E1-0066", subtema=H2["fund"], comando=CMD_FUND,
        assertiva=("Os termos oferta e demanda referem-se ao comportamento dos agentes da economia à medida que "
                   "interagem entre si em mercados competitivos (onde há muitos compradores e vendedores, cada um "
                   "dos quais com pouca ou nenhuma influência sobre os preços de mercado)."),
        gabarito="CERTO",
        anotada=az("Os termos oferta e demanda referem-se ao comportamento dos agentes da economia à medida que "
                   "interagem entre si em mercados competitivos (onde há <u>muitos compradores e vendedores</u>, "
                   "cada um dos quais com <u>pouca ou nenhuma influência</u> sobre os preços de mercado)."),
        poucas=("É a abertura do capítulo de oferta e demanda de " + oc("Mankiw") + ": o modelo descreve "
                "compradores (demanda) e vendedores (oferta) em " + azb("mercados competitivos") + ", nos quais "
                "cada agente é " + azb("tomador de preço") + "."),
        destrinchando=[
            "Demanda = comportamento dos compradores; oferta = comportamento dos vendedores. Da interação dos "
            "dois lados saem o " + vd("preço") + " e a " + vd("quantidade de equilíbrio") + ".",
            azb("Mercado competitivo") + ": tantos compradores e vendedores que nenhum, isoladamente, move o "
            "preço. O caso extremo é a " + azb("concorrência perfeita") + ", que exige ainda produto homogêneo, "
            "livre entrada e saída e informação perfeita; nela a curva de demanda da firma individual é "
            "horizontal ao preço de mercado.",
            "Por que a hipótese importa: só com tomadores de preço faz sentido falar em uma <b>curva de "
            "oferta</b> independente da demanda. No monopólio, a firma escolhe preço e quantidade olhando a "
            "demanda (RMg = CMg) e não existe curva de oferta no sentido usual.",
            "Exemplos próximos do modelo: commodities agrícolas (soja, café) e mercados financeiros líquidos. "
            "Distantes: telefonia, aviação, sistemas operacionais.",
        ],
        dissecando=(cz("[literalidade]") + " Paráfrase quase literal do manual. A banca costuma alterar o "
                    "parêntese (“poucos vendedores”, “influência decisiva sobre os preços”), que descreveria "
                    "oligopólio ou monopólio."),
        modulos=[("😈 Para dificultar", [
            "<i>“…em mercados competitivos, nos quais cada vendedor fixa o preço de seu produto acima do custo "
            "marginal.”</i> → ERRADO (isso é poder de mercado; na competição, p = CMg)",
            "<i>“Em concorrência perfeita, a curva de demanda com que se depara cada empresa é horizontal.”</i> "
            "→ CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=["pouca ou nenhuma"], dificuldade=1,
        comentario_fonte="CERTO. Em mercados competitivos, compradores e vendedores são tomadores de preço; a "
                         "demanda representa os consumidores e a oferta, os produtores, que interagem para "
                         "determinar preço e quantidade de equilíbrio.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0067
    card(
        id="ECO-E1-0067-1", fonte_ref="E1-0067", subtema=H2["dem"], comando=CMD_OD,
        assertiva=("A demanda (ou procura) representa aquilo que o consumidor deseja adquirir, o que significa que "
                   "ele vai necessariamente adquirir/consumir."),
        gabarito="ERRADO",
        anotada=az("A demanda (ou procura) representa aquilo que o consumidor deseja adquirir, ")
                + vm("o que significa que ele vai necessariamente adquirir/consumir") + az("."),
        poucas=("Demanda é um " + azb("desejo ou plano de compra") + " a cada preço, não a compra realizada. "
                "Desejar não garante adquirir — o “necessariamente” derruba o item."),
        destrinchando=[
            "A curva de demanda é uma lista de intenções: “a este preço, eu compraria tanto”. É um conceito "
            + azb("ex ante") + " — descreve o que os consumidores estão dispostos e são capazes de comprar, "
            "não o que efetivamente compram.",
            "O que se transaciona de fato é a quantidade de equilíbrio, que depende também da oferta. Fora do "
            "equilíbrio, o desejo não se realiza: com um " + azb("preço máximo") + " abaixo do equilíbrio, há "
            "consumidores que querem comprar e não encontram o produto (escassez, filas).",
            "Desejo, para a teoria, não é vontade solta: precisa ser " + azb("demanda solvável") + ", isto é, "
            "apoiada em renda (disposição <b>e</b> capacidade de pagar). Ainda assim, é plano, não ato.",
            "O mesmo vale para a oferta: é intenção de venda, não venda concretizada.",
            "Cuidado com o termo “demanda efetiva”: em " + oc("Keynes") + ", ele designa a demanda agregada "
            "esperada que determina o nível de produção e emprego — outro conceito, de macroeconomia.",
        ],
        dissecando=(cz("[modulador absoluto · meia-verdade]") + " A 1ª oração é a definição correta; o erro "
                    "está na conclusão enxertada com “necessariamente”, que converte intenção em fato. Pista: "
                    "advérbio absoluto colado a uma definição econômica costuma ser o ponto de quebra."),
        modulos=[("😈 Para dificultar", [
            "<i>“Assim como a demanda, a oferta representa uma intenção de venda, e não a concretização da "
            "venda.”</i> → CERTO",
            "<i>“A quantidade demandada a cada preço corresponde sempre à quantidade efetivamente vendida "
            "nesse mercado.”</i> → ERRADO (modulador absoluto; fora do equilíbrio elas diferem)",
        ])],
        reescrita=("A demanda (ou procura) representa aquilo que o consumidor deseja adquirir, o que "
                   + hl("não significa que ele vá") + " necessariamente adquirir/consumir."),
        tipo_erro=["GENERALIZACAO", "MEIA_VERDADE"], moduladores=["necessariamente"], dificuldade=1,
        comentario_fonte="ERRADO. A demanda é a intenção de compra, condicionada ao preço, à renda e às "
                         "preferências; não garante a compra. A fonte chama de “demanda efetiva” o que o "
                         "consumidor de fato adquire.",
        qualidade_fonte="com_erro",
        figuras_fonte=[img_perdida("Untitled.jpeg")],
        alertas=["qualidade_fonte: o comentário de origem chama de “demanda efetiva” a compra realizada; o "
                 "termo tem sentido próprio em Keynes (demanda agregada esperada) — não reproduzido"],
    ),
    # ------------------------------------------------------------------ E1-0068
    card(
        id="ECO-E1-0068-1", fonte_ref="E1-0068", subtema=H2["dem"], comando=CMD_OD,
        assertiva="São muitos os fatores que alteram a demanda, mas o fator central é a quantidade.",
        gabarito="ERRADO",
        anotada=az("São muitos os fatores que alteram a demanda, mas o fator central é ") + vm("a quantidade")
                + az("."),
        poucas=("O determinante central da quantidade demandada é o " + azb("preço") + " do próprio bem: "
                + vd("Q<sub>d</sub> = f(P)") + ". A quantidade é a variável <b>explicada</b>, não o fator que "
                "explica."),
        destrinchando=[
            "Função demanda completa: Q<sub>d</sub> = f(P<sub>x</sub>, R, P<sub>s</sub>, P<sub>c</sub>, "
            "gostos, expectativas, nº de consumidores). O manual destaca o " + vd("preço do próprio bem")
            + " porque é a variável posta no eixo; as demais ficam “constantes” e, quando mudam, deslocam a "
            "curva.",
            "A quantidade demandada é o <b>resultado</b> (variável dependente). Dizer que ela é o fator central "
            "da demanda inverte causa e efeito: é como dizer que a temperatura é causada pela leitura do "
            "termômetro.",
            "Por que o preço é central: é a única variável que, sozinha, percorre a curva inteira (lei da "
            "demanda), e é por meio dele que o mercado se ajusta ao equilíbrio.",
            "Mesma lógica na oferta: Q<sub>s</sub> = g(P<sub>x</sub>, custos, tecnologia, …), com o preço como "
            "variável central.",
        ],
        dissecando=(cz("[troca de conceito · inversão]") + " O item troca a variável independente (preço) "
                    "pela dependente (quantidade). A 1ª oração (“muitos fatores”) é verdadeira e serve de "
                    "isca."),
        modulos=[("😈 Para dificultar", [
            "<i>“São muitos os fatores que alteram a quantidade demandada, mas o fator central é o preço do "
            "próprio bem.”</i> → CERTO",
            "<i>“Uma variação no preço do próprio bem desloca a curva de demanda.”</i> → ERRADO (troca de "
            "conceito: movimento ao longo da curva)",
        ])],
        reescrita=("São muitos os fatores que alteram a demanda, mas o fator central é " + hl("o preço")
                   + "."),
        tipo_erro=["TROCA_CONCEITO", "INVERSAO"], moduladores=[], dificuldade=1,
        comentario_fonte="ERRADO. O fator central é o preço: Qd = f(P), a quantidade demandada é função do preço.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0069
    card(
        id="ECO-E1-0069-1", fonte_ref="E1-0069", subtema=H2["dem"], comando=CMD_OD,
        assertiva=("A curva de demanda tem inclinação negativa, demonstrando que os consumidores estão dispostos a "
                   "comprar mais a um preço mais baixo, à medida que o produto se torna relativamente mais barato "
                   "e a renda real do consumidor aumenta."),
        gabarito="CERTO",
        anotada=az("A curva de demanda tem inclinação negativa, demonstrando que os consumidores estão dispostos a "
                   "comprar mais a um preço mais baixo, à medida que o produto se torna <u>relativamente mais "
                   "barato</u> e a <u>renda real</u> do consumidor aumenta."),
        poucas=("O item resume os dois efeitos da queda de preço: " + azb("efeito substituição") + " (o bem fica "
                "relativamente mais barato) e " + azb("efeito renda") + " (o poder de compra aumenta)."),
        destrinchando=[
            azb("Efeito substituição") + ": com a queda de p<sub>x</sub>, x fica mais barato em relação aos "
            "outros bens, e o consumidor troca parte do consumo a favor dele. Sempre aumenta a quantidade "
            "demandada de x.",
            azb("Efeito renda") + ": com a mesma renda nominal, pode-se comprar mais de tudo — a " + vd("renda "
            "real") + " subiu. Para um bem normal, isso aumenta o consumo de x; os dois efeitos se somam e a "
            "curva é negativamente inclinada.",
            "Bem inferior: o efeito renda atua contra o substituição, mas costuma ser menor — a curva continua "
            "negativa. Se o efeito renda for maior, temos o " + azb("bem de Giffen") + ", com curva "
            "positivamente inclinada.",
            "A decomposição é de " + oc("Slutsky") + " e de " + oc("Hicks") + " (formalização na teoria do "
            "consumidor).",
            vm("Regra-âncora: substituição sempre a favor do bem que barateou; renda depende de ser normal ou "
            "inferior."),
        ],
        dissecando=(cz("[paráfrase fiel · detalhe]") + " A frase longa embute a decomposição "
                    "substituição + renda sem nomeá-la. Quem não reconhece “relativamente mais barato” e "
                    "“renda real” como os dois efeitos pode estranhar a justificativa e marcar ERRADO."),
        modulos=[("😈 Para dificultar", [
            "<i>“…à medida que o produto se torna relativamente mais caro e a renda nominal do consumidor "
            "aumenta.”</i> → ERRADO (inversão: relativamente mais barato; e é a renda real)",
            "<i>“Para todo bem inferior, o efeito renda supera o efeito substituição.”</i> → ERRADO "
            "(generalização: isso define só o bem de Giffen)",
        ])],
        tipo_erro=["PARAFRASE_FIEL", "DETALHE"], moduladores=[], dificuldade=2,
        comentario_fonte="CERTO. Quando o preço diminui, a quantidade aumenta.",
        qualidade_fonte="raso",
        figuras_fonte=[img_perdida("Untitled (14).jpeg")],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0070
    card(
        id="ECO-E1-0070-1", fonte_ref="E1-0070", subtema=H2["bens"], comando=CMD_BENS,
        assertiva="Bem normal é aquele cuja demanda cresce à medida que a renda do consumidor aumenta.",
        gabarito="CERTO",
        anotada=az("Bem normal é aquele cuja demanda <u>cresce</u> à medida que a renda do consumidor "
                   "<u>aumenta</u>."),
        poucas=("Definição correta: no " + azb("bem normal") + " renda e demanda andam no mesmo sentido — "
                "elasticidade-renda " + vd("positiva") + "."),
        destrinchando=[
            azb("Elasticidade-renda da demanda") + ": ε<sub>R</sub> = %Δq / %Δrenda. Bem normal → "
            + vd("ε<sub>R</sub> > 0") + "; bem inferior → ε<sub>R</sub> < 0.",
            "Dentro dos normais: " + azb("bem necessário ou essencial") + " (0 < ε<sub>R</sub> < 1: a demanda "
            "cresce menos que a renda — alimentos básicos) e " + azb("bem superior ou de luxo") + " "
            "(ε<sub>R</sub> > 1: cresce mais que a renda — viagens internacionais, automóveis de alto padrão).",
            "Gráfico: aumento de renda desloca a demanda de um bem normal para a direita; o equilíbrio vai para "
            "preço e quantidade maiores.",
            "Regularidade empírica: " + oc("Engel") + " (século XIX) observou que a parcela da renda gasta com "
            "alimentação cai quando a renda sobe — os alimentos são normais, mas necessários (ε<sub>R</sub> < 1).",
        ],
        dissecando=(cz("[literalidade]") + " Definição de manual. A pegadinha usual é a inversão (bem normal "
                    "com demanda que cai) ou a confusão entre normal (ε > 0) e de luxo (ε > 1)."),
        modulos=[("😈 Para dificultar", [
            "<i>“Bem normal é aquele cuja demanda cresce mais que proporcionalmente ao aumento da renda.”</i> → "
            "ERRADO (restrição indevida: isso define o bem de luxo)",
            "<i>“Um aumento na renda desloca a demanda de um bem normal para a direita.”</i> → CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Exemplos: viagens, automóveis e vestuário.",
        qualidade_fonte="raso",
        figuras_fonte=[],
        alertas=["quase_duplicata: ECO-E1-0081-1 cobra a mesma definição com outra redação (mesma fonte)"],
    ),
    # ------------------------------------------------------------------ E1-0071
    card(
        id="ECO-E1-0071-1", fonte_ref="E1-0071", subtema=H2["bens"], comando=CMD_BENS,
        assertiva=("Bens essenciais é categoria de bens normais caracterizada por um aumento moderado na demanda "
                   "em resposta a um aumento na renda do consumidor."),
        gabarito="CERTO",
        anotada=az("Bens essenciais é categoria de <u>bens normais</u> caracterizada por um aumento "
                   "<u>moderado</u> na demanda em resposta a um aumento na renda do consumidor."),
        poucas=("Bens " + azb("essenciais (necessários)") + " são normais com elasticidade-renda entre "
                + vd("0 e 1") + ": a demanda cresce com a renda, mas menos que proporcionalmente."),
        destrinchando=[
            "Mapa da elasticidade-renda (ε<sub>R</sub>): " + vd("ε<sub>R</sub> < 0") + " → inferior; "
            + vd("0 < ε<sub>R</sub> < 1") + " → normal essencial; " + vd("ε<sub>R</sub> > 1") + " → normal "
            "superior (de luxo). O “aumento moderado” do item é o intervalo entre 0 e 1.",
            "Intuição: a necessidade é atendida mesmo com renda baixa e satura rápido — com mais renda, "
            "ninguém triplica o consumo de sal, arroz ou energia elétrica residencial. O consumo cresce pouco, "
            "e a <b>parcela da renda</b> gasta com esses bens cai.",
            "Consequência econômica: setores de bens essenciais são menos sensíveis ao ciclo (vendem de forma "
            "estável na recessão); setores de luxo oscilam mais que a renda.",
            "Não confundir com a " + azb("elasticidade-preço") + ": bens essenciais também costumam ter demanda "
            "preço-inelástica (poucos substitutos), mas são conceitos distintos.",
        ],
        dissecando=(cz("[paráfrase fiel]") + " “Aumento moderado” é a tradução verbal de 0 < ε<sub>R</sub> < 1. "
                    "A banca costuma trocar “normais” por “inferiores” ou “moderado” por “mais que "
                    "proporcional”."),
        modulos=[("😈 Para dificultar", [
            "<i>“Bens essenciais são bens inferiores, pois sua demanda cresce menos que a renda.”</i> → ERRADO "
            "(troca de conceito: crescer menos ainda é crescer, ε<sub>R</sub> > 0)",
            "<i>“Bens de luxo apresentam elasticidade-renda da demanda superior à unidade.”</i> → CERTO",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], moduladores=["moderado"], dificuldade=1,
        comentario_fonte="CERTO. A demanda por bens essenciais cresce de forma contida com a renda; ter mais "
                         "dinheiro não faz alguém consumir muito mais arroz ou feijão.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=["texto_corrigido: “Ben essenciais” corrigido para “Bens essenciais” (erro evidente)"],
    ),
    # ------------------------------------------------------------------ E1-0072
    card(
        id="ECO-E1-0072-1", fonte_ref="E1-0072", subtema=H2["bens"], comando=CMD_BENS,
        assertiva="Bem inferior é um tipo de bem cuja demanda diminui à medida que a renda das pessoas aumenta.",
        gabarito="CERTO",
        anotada=az("Bem inferior é um tipo de bem cuja demanda <u>diminui</u> à medida que a renda das pessoas "
                   "aumenta."),
        poucas=("Correto: " + azb("bem inferior") + " tem elasticidade-renda " + vd("negativa") + " — com mais "
                "renda, o consumidor o troca por alternativas preferidas."),
        destrinchando=[
            "Exemplos típicos: passagens de ônibus (trocadas por carro ou aplicativo), cortes de carne menos "
            "nobres, marcas populares, produtos usados. O “inferior” não é juízo de qualidade: indica só o "
            "sinal da resposta à renda.",
            "Gráfico: renda ↑ → demanda do bem inferior se desloca para a " + vd("esquerda") + "; renda ↓ "
            "(recessão) → para a " + vd("direita") + ". É um bem anticíclico.",
            "Relação com a " + azb("lei da demanda") + ": no bem inferior, o efeito renda de uma queda de preço "
            "<b>reduz</b> o consumo, contra o efeito substituição. Em geral o substituição vence e a curva "
            "continua negativa. Se o efeito renda vencer, é um " + azb("bem de Giffen") + " (curva positiva) — "
            "todo Giffen é inferior, mas não o contrário.",
            "Caráter relativo: o mesmo bem pode ser inferior para uma faixa de renda e normal para outra.",
        ],
        dissecando=(cz("[literalidade]") + " Definição direta. Armadilhas frequentes: “bem inferior é o de "
                    "baixa qualidade” (juízo indevido) ou “todo bem inferior contraria a lei da demanda” "
                    "(confusão com Giffen)."),
        modulos=[("😈 Para dificultar", [
            "<i>“Todo bem inferior é um bem de Giffen.”</i> → ERRADO (inversão: todo Giffen é inferior, não o "
            "contrário)",
            "<i>“Em uma recessão, a demanda por bens inferiores tende a aumentar.”</i> → CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Exemplos: passagens de ônibus e carnes menos nobres.",
        qualidade_fonte="raso",
        figuras_fonte=[],
        alertas=["quase_duplicata: ECO-E1-0061-1 cobra a mesma definição com outra redação (mesma fonte)"],
    ),
    # ------------------------------------------------------------------ E1-0073
    card(
        id="ECO-E1-0073-1", fonte_ref="E1-0073", subtema=H2["bens"], comando=CMD_BENS,
        assertiva=("Bens substitutos são tipos de bens em que o aumento no preço de um leva a um aumento na "
                   "demanda por outro."),
        gabarito="CERTO",
        anotada=az("Bens substitutos são tipos de bens em que o <u>aumento</u> no preço de um leva a um "
                   "<u>aumento</u> na demanda por outro."),
        poucas=("Definição pelo efeito: entre " + azb("substitutos") + ", preço de um e demanda do outro andam no "
                + vd("mesmo sentido") + " — elasticidade-preço cruzada positiva."),
        destrinchando=[
            "Exemplo brasileiro clássico: " + rx("etanol × gasolina") + " nos carros flex. Quando a gasolina "
            "sobe, o motorista reduz a quantidade de gasolina (movimento ao longo da curva dela) e procura "
            "mais etanol (deslocamento da demanda de etanol para a direita).",
            "Regra prática difundida no " + rx("Brasil") + ": o etanol compensa quando custa até cerca de "
            + vd("70%") + " do preço da gasolina, porque rende menos por litro. É a substituição guiada pelo "
            "preço relativo — e mostra que a substitutibilidade depende de custo por quilômetro, não só de "
            "preço por litro.",
            "Grau de substituição: quanto mais próximos os substitutos, maior a " + azb("elasticidade cruzada")
            + " e maior a " + azb("elasticidade-preço") + " da demanda de cada bem (é fácil fugir para o "
            "outro). Bem sem substitutos próximos tem demanda inelástica.",
            "O efeito é sobre a <b>demanda</b> (curva inteira) do outro bem; no mercado do bem que encareceu, "
            "cai só a quantidade demandada.",
        ],
        dissecando=(cz("[literalidade]") + " Definição operacional, sem modulador. Armadilhas usuais: trocar "
                    "o segundo “aumento” por “redução” (isso define complementares) ou trocar “demanda” por "
                    "“quantidade demandada” no bem que não teve o preço alterado."),
        modulos=[("😈 Para dificultar", [
            "<i>“Bens substitutos são aqueles em que o aumento no preço de um leva à redução da demanda pelo "
            "outro.”</i> → ERRADO (troca de conceito: isso define complementares)",
            "<i>“Quanto mais substitutos próximos um bem tiver, mais elástica tende a ser sua demanda.”</i> → "
            "CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Exemplo: com a gasolina mais cara, as pessoas reduzem seu consumo e procuram mais "
                         "o etanol, e a demanda por etanol aumenta.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=["quase_duplicata: ECO-E1-0060-1 cobra a mesma definição com outra redação (mesma fonte)",
                 "dado_aproximado: regra dos 70% (etanol/gasolina) citada como regra prática, sem fonte oficial "
                 "no lote"],
    ),
    # ------------------------------------------------------------------ E1-0074
    card(
        id="ECO-E1-0074-1", fonte_ref="E1-0074", subtema=H2["bens"], comando=CMD_BENS,
        assertiva=("Os bens são complementares quando o aumento no preço de um leva à diminuição na demanda do "
                   "outro."),
        gabarito="CERTO",
        anotada=az("Os bens são complementares quando o <u>aumento</u> no preço de um leva à <u>diminuição</u> "
                   "na demanda do outro."),
        poucas=("Definição correta: " + azb("complementares") + " são consumidos juntos; encarecer um encarece "
                "o “pacote” e reduz a demanda do outro — elasticidade cruzada " + vd("negativa") + "."),
        destrinchando=[
            "Exemplo: carne e carvão. Se a carne sobe, o churrasco fica mais caro como um todo; faz-se menos "
            "churrasco e a demanda por carvão se desloca para a " + vd("esquerda") + ", mesmo sem mudança no "
            "preço do carvão.",
            "Atenção ao mecanismo em dois mercados: no da carne, cai a <b>quantidade demandada</b> (movimento "
            "ao longo da curva); no do carvão, cai a <b>demanda</b> (deslocamento da curva).",
            azb("Elasticidade-preço cruzada") + " ε<sub>carvão, carne</sub> = %Δq<sub>carvão</sub> / "
            "%Δp<sub>carne</sub> " + vd("< 0") + ". Para substitutos, > 0.",
            "Leitura simétrica: a <b>queda</b> no preço de um complementar <b>aumenta</b> a demanda do outro "
            "(impressora barata → mais demanda por cartuchos — a estratégia de vender barato o aparelho e caro "
            "o insumo).",
            "Caso-limite: " + azb("complementares perfeitos") + " (Leontief), consumidos em proporção fixa.",
        ],
        dissecando=(cz("[literalidade]") + " Definição pelo efeito, correta. A banca a inverte trocando o "
                    "sentido (“aumento na demanda”) ou apresenta a versão simétrica com redução de preço, que "
                    "exige atenção dupla aos sinais."),
        modulos=[("😈 Para dificultar", [
            "<i>“Os bens são complementares quando a redução no preço de um leva à diminuição na demanda do "
            "outro.”</i> → ERRADO (inversão: a demanda do outro aumentaria)",
            "<i>“Entre bens complementares, a elasticidade-preço cruzada da demanda é negativa.”</i> → CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Exemplo: carne e carvão; se a carne encarece, o churrasco fica mais caro e cai a "
                         "demanda por carvão, mesmo sem mudança no preço do carvão.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0075
    card(
        id="ECO-E1-0075-1", fonte_ref="E1-0075", subtema=H2["bens"], comando=CMD_BENS,
        assertiva=("Bem de Veblen é aquele que quanto mais caro mais a pessoa quer comprar, ou seja, o consumidor "
                   "tem um comportamento exibicionista. Neste caso, a quantidade demandada é deslocada no mesmo "
                   "sentido do preço."),
        gabarito="CERTO",
        anotada=az("Bem de Veblen é aquele que <u>quanto mais caro mais a pessoa quer comprar</u>, ou seja, o "
                   "consumidor tem um comportamento <u>exibicionista</u>. Neste caso, a quantidade demandada é "
                   "deslocada no mesmo sentido do preço."),
        poucas=("No " + azb("bem de Veblen") + " o preço alto é parte do valor (sinal de status): o preço sobe e "
                "a quantidade demandada também — relação " + vd("positiva") + ", exceção à lei da demanda."),
        destrinchando=[
            "Origem: " + oc("Thorstein Veblen") + ", <i>A Teoria da Classe Ociosa</i> (1899), cunhou o "
            + azb("consumo conspícuo") + ": consumir para exibir riqueza. Para o consumidor de ostentação, uma "
            "bolsa de grife mais barata vale menos, porque sinaliza menos.",
            "Por isso a curva de demanda pode ter trecho " + vd("positivamente inclinado") + ". Exemplos: "
            "superesportivos, joias, relógios e vinhos de luxo.",
            "Diferença para o " + azb("bem de Giffen") + ": Giffen é um bem <b>inferior</b>, consumido por "
            "pobres, com efeito renda que supera o efeito substituição (mecanismo de renda). Veblen é bem de "
            "<b>luxo</b>, e o mecanismo é de preferências — o preço entra na própria utilidade.",
            "Muitos autores tratam o Veblen como exceção “imprópria”: o efeito é de comportamento individual "
            "de exibição, ligado a mudança de percepção, e não se sustenta para o mercado todo em qualquer "
            "faixa de preço.",
            "Nota de vocabulário: “deslocada”, no item, é uso frouxo; tecnicamente a quantidade demandada "
            "<b>varia</b> ao longo da curva, que tem inclinação positiva.",
        ],
        dissecando=(cz("[exceção]") + " O item cobra a exceção à lei da demanda, com linguagem coloquial "
                    "(“exibicionista”). O risco é o reflexo de marcar ERRADO por “relação positiva entre preço "
                    "e quantidade”, ou confundir com Giffen."),
        modulos=[("😈 Para dificultar", [
            "<i>“O bem de Veblen é um bem inferior em que o efeito renda supera o efeito substituição.”</i> → "
            "ERRADO (troca de conceito: isso descreve o bem de Giffen)",
            "<i>“O bem de Veblen está associado ao consumo conspícuo.”</i> → CERTO",
        ])],
        tipo_erro=["EXCECAO"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Exceção à lei da demanda, embora não legítima: é bem superior e o comportamento "
                         "é individual, não coletivo. Exemplo: uma Ferrari.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0076
    card(
        id="ECO-E1-0076-1", fonte_ref="E1-0076", subtema=H2["bens"], comando=CMD_BENS,
        assertiva=("Bens para especulação são aqueles em que o consumidor os adquire a um valor esperando que este "
                   "valor se eleve ainda mais no futuro e, ao se desfazer do bem, procurará garantir ganhos."),
        gabarito="CERTO",
        anotada=az("Bens para especulação são aqueles em que o consumidor os adquire a um valor <u>esperando que "
                   "este valor se eleve</u> ainda mais no futuro e, ao se desfazer do bem, procurará garantir "
                   "ganhos."),
        poucas=("Correto: o bem de " + azb("especulação") + " é comprado como " + azb("ativo") + ", pela "
                "expectativa de revenda com lucro, não pelo uso imediato."),
        destrinchando=[
            "Exemplos: ações, imóveis, ouro, obras de arte, criptoativos. O que move a compra é o "
            + azb("ganho de capital esperado") + " (preço futuro − preço de compra).",
            "Por que aparece ao lado de Giffen e Veblen: num mercado especulativo, a alta de preço pode "
            "<b>aumentar</b> a procura, porque alimenta a expectativa de novas altas. A rigor, porém, o que "
            "muda é a " + azb("expectativa de preço futuro") + " — um determinante da demanda que <b>desloca</b> "
            "a curva para a direita, e não um trecho positivamente inclinado.",
            "Esse circuito (preço sobe → expectativa sobe → demanda sobe → preço sobe) é o motor das "
            + azb("bolhas especulativas") + ": tulipas holandesas (século XVII), ações da internet (2000), "
            "imóveis nos EUA (2008).",
            "Ponto do item: a definição se apoia na expectativa de valorização e na intenção de revenda — os "
            "dois traços que distinguem especulação de consumo.",
        ],
        dissecando=(cz("[paráfrase fiel]") + " Definição descritiva, sem modulador perigoso. Versões erradas "
                    "costumam afirmar que o especulador compra para consumo próprio ou que esses bens violam "
                    "sempre a lei da demanda."),
        modulos=[("😈 Para dificultar", [
            "<i>“Nos bens de especulação, a expectativa de alta futura do preço desloca a demanda presente para "
            "a direita.”</i> → CERTO",
            "<i>“Bens de especulação são adquiridos prioritariamente para consumo imediato.”</i> → ERRADO "
            "(contradição: o objetivo é a revenda com ganho)",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. São adquiridos para lucro futuro, não para consumo imediato; o comprador espera "
                         "valorização e revenda. Exemplos: ações, imóveis, obras de arte.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0078
    card(
        id="ECO-E1-0078-1", fonte_ref="E1-0078", subtema=H2["of"], comando=CMD_OD,
        assertiva=("Assim como a demanda, a oferta representa uma intenção da venda e não a concretização da "
                   "venda."),
        gabarito="CERTO",
        anotada=az("Assim como a demanda, a oferta representa uma <u>intenção</u> da venda e não a concretização "
                   "da venda."),
        poucas=("A " + azb("oferta") + " mostra quanto os vendedores estão " + vd("dispostos a vender") + " a "
                "cada preço — um plano, não a venda realizada, que depende também dos compradores."),
        destrinchando=[
            "Curva de oferta: Q<sub>s</sub> = g(P), tudo o mais constante (custos de insumos, tecnologia, "
            "preços de bens relacionados na produção, expectativas, número de firmas). Como a de demanda, é "
            "uma lista de intenções a cada preço possível.",
            "A venda efetiva só ocorre quando há comprador. No equilíbrio, intenção de vender e intenção de "
            "comprar coincidem; fora dele, uma das intenções se frustra.",
            "Exemplo: com um " + azb("preço mínimo") + " acima do equilíbrio (salário mínimo no modelo "
            "competitivo, preço mínimo agrícola), a quantidade ofertada supera a demandada — há produtores "
            "que querem vender e não conseguem (excedente de oferta).",
            "O determinante central da oferta é o " + vd("preço do próprio bem") + ", com relação positiva "
            "(lei da oferta).",
        ],
        dissecando=(cz("[paráfrase fiel]") + " Item-espelho da definição de demanda como intenção. A "
                    "comparação “assim como” é verdadeira; a armadilha seria trocar por “ao contrário da "
                    "demanda, a oferta representa a venda efetivamente realizada”."),
        modulos=[("😈 Para dificultar", [
            "<i>“Ao contrário da demanda, a oferta corresponde à quantidade efetivamente vendida no "
            "mercado.”</i> → ERRADO (as duas são intenções)",
            "<i>“Com preço mínimo acima do equilíbrio, a quantidade ofertada supera a quantidade "
            "demandada.”</i> → CERTO",
        ])],
        tipo_erro=["PARAFRASE_FIEL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. A oferta descreve quanto os vendedores estariam dispostos a vender a um preço; "
                         "o principal determinante é o preço.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=["texto_fonte: “intenção da venda” mantido como na fonte (provável “intenção de venda”)"],
    ),
    # ------------------------------------------------------------------ E1-0079
    card(
        id="ECO-E1-0079-1", fonte_ref="E1-0079", subtema=H2["dem"], comando=CMD_OD,
        assertiva=("Tudo o mais permanecendo constante, o deslocamento de uma curva de demanda para a direita é "
                   "resultante de uma redução na renda."),
        gabarito="ERRADO",
        anotada=az("Tudo o mais permanecendo constante, o deslocamento de uma curva de demanda para a direita é "
                   "resultante de uma ") + vm("redução") + az(" na renda."),
        poucas=("Para o caso geral (" + azb("bem normal") + "), redução de renda desloca a demanda para a "
                "<b>esquerda</b>. Para a direita, seria preciso um " + vd("aumento") + " de renda."),
        destrinchando=[
            "Renda é deslocador da demanda. O sentido depende do tipo de bem: " + azb("normal") + " "
            "(ε<sub>R</sub> > 0) → renda ↓, demanda para a esquerda; " + azb("inferior") + " "
            "(ε<sub>R</sub> < 0) → renda ↓, demanda para a direita.",
            "O item não especifica o bem e afirma a relação como regra. Sem menção a bem inferior, vale o "
            "caso-padrão dos manuais (bem normal), em que a afirmação é falsa.",
            "O “tudo o mais permanecendo constante” isola a renda como única causa do deslocamento: a questão "
            "passa a ser apenas o sinal da resposta da demanda à renda — positivo no bem normal.",
            "Outras causas de deslocamento para a direita: aumento de renda (normal), alta do preço de "
            "substitutos, queda do preço de complementares, preferências favoráveis, expectativa de alta "
            "de preço, mais consumidores.",
        ],
        dissecando=(cz("[inversão]") + " Inverte o sentido da renda para o caso usual. A banca aposta que o "
                    "candidato pense só em bem inferior e marque CERTO; sem a ressalva expressa no item, "
                    "prevalece o bem normal."),
        modulos=[("😈 Para dificultar", [
            "<i>“…o deslocamento de uma curva de demanda de um bem inferior para a direita pode resultar de "
            "uma redução na renda.”</i> → CERTO",
            "<i>“…o deslocamento da curva de demanda de um bem normal para a direita pode resultar de uma "
            "queda no preço do próprio bem.”</i> → ERRADO (troca de conceito: isso é movimento ao longo da "
            "curva)",
        ])],
        reescrita=("Tudo o mais permanecendo constante, o deslocamento de uma curva de demanda para a direita é "
                   "resultante de um " + hl("aumento") + " na renda."),
        tipo_erro=["INVERSAO"], moduladores=["tudo o mais permanecendo constante"], dificuldade=1,
        comentario_fonte="ERRADO. A redução na renda geralmente desloca a curva de demanda para a esquerda, "
                         "exceto no caso de bens inferiores.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0080
    card(
        id="ECO-E1-0080-1", fonte_ref="E1-0080", subtema=H2["bens"], comando=CMD_BENS,
        assertiva=("A redução da demanda de um bem quando ocorre a redução do preço de um outro bem pode indicar "
                   "que eles são complementares."),
        gabarito="ERRADO",
        anotada=az("A redução da demanda de um bem quando ocorre a redução do preço de um outro bem pode indicar "
                   "que eles são ") + vm("complementares") + az("."),
        poucas=("Preço de y ↓ e demanda de x ↓: sinais no " + vd("mesmo sentido") + " → elasticidade cruzada "
                "positiva → " + azb("substitutos") + ". Com complementares, a demanda de x aumentaria."),
        destrinchando=[
            "Regra dos sinais (" + azb("elasticidade-preço cruzada") + "): se preço de y e demanda de x andam "
            "juntos (ambos ↑ ou ambos ↓), ε > 0 → " + vd("substitutos") + "; se andam em sentidos opostos, "
            "ε < 0 → " + vd("complementares") + ".",
            "Intuição para substitutos: o ônibus fica mais barato e menos gente usa aplicativo de transporte — "
            "a demanda pelo aplicativo cai.",
            "Intuição para complementares: o carro fica mais barato e mais gente compra carro — a demanda por "
            "gasolina <b>sobe</b>, não cai.",
            "O “pode indicar” não salva o item: o sinal observado é <b>incompatível</b> com a "
            "complementaridade, logo não pode indicá-la.",
            vm("Regra-âncora: mesmo sentido = substitutos; sentidos opostos = complementares."),
        ],
        dissecando=(cz("[troca de conceito]") + " A banca usa a versão com <b>redução</b> de preço para "
                    "embaralhar os sinais e o “pode” para dar aparência de cautela. Faça a conta de sinal: "
                    "(−)/(−) = (+) → substitutos."),
        modulos=[("😈 Para dificultar", [
            "<i>“A redução da demanda de um bem quando ocorre a redução do preço de um outro bem pode indicar "
            "que eles são substitutos.”</i> → CERTO",
            "<i>“O aumento da demanda de um bem quando ocorre a redução do preço de outro indica que eles são "
            "substitutos.”</i> → ERRADO (sinais opostos indicam complementares)",
        ])],
        reescrita=("A redução da demanda de um bem quando ocorre a redução do preço de um outro bem pode indicar "
                   "que eles são " + hl("substitutos") + "."),
        tipo_erro=["TROCA_CONCEITO"], moduladores=["pode"], dificuldade=1,
        comentario_fonte="ERRADO. Quando o preço de um bem complementar cai, a demanda do outro bem aumenta, e não "
                         "diminui.",
        qualidade_fonte="bom",
        figuras_fonte=[img_perdida("Untitled (11).jpeg")],
        alertas=[],
    ),
    # ------------------------------------------------------------------ E1-0081
    card(
        id="ECO-E1-0081-1", fonte_ref="E1-0081", subtema=H2["bens"], comando=CMD_BENS,
        assertiva="Um bem normal é aquele cuja demanda aumenta quando a renda aumenta.",
        gabarito="CERTO",
        anotada=az("Um bem normal é aquele cuja demanda <u>aumenta</u> quando a renda <u>aumenta</u>."),
        poucas=("Correto: " + azb("bem normal") + " tem elasticidade-renda " + vd("positiva") + "; renda maior "
                "desloca sua curva de demanda para a direita."),
        destrinchando=[
            "Exemplos: viagens, automóveis, vestuário, serviços de lazer — a maioria dos bens é normal, daí o "
            "nome.",
            "A definição exige só que a demanda <b>aumente</b>, qualquer que seja a intensidade: "
            "0 < ε<sub>R</sub> < 1 → " + azb("essencial") + " (cresce menos que a renda); ε<sub>R</sub> > 1 → "
            + azb("de luxo ou superior") + " (cresce mais que a renda).",
            "Uso macroeconômico: como a maioria dos bens é normal, o crescimento da renda puxa a demanda; e "
            "bens de luxo, com ε<sub>R</sub> alta, sofrem mais nas recessões.",
            "Contraponto: " + azb("bem inferior") + " (ε<sub>R</sub> < 0), cuja demanda cai quando a renda "
            "sobe. Bem com ε<sub>R</sub> = 0 é chamado de " + azb("bem de consumo saciado") + " (a renda não "
            "altera a demanda).",
        ],
        dissecando=(cz("[literalidade]") + " Definição sem modulador. O erro típico em outras versões é exigir "
                    "crescimento “mais que proporcional” (luxo) ou inverter o sentido (inferior)."),
        modulos=[("😈 Para dificultar", [
            "<i>“Um bem normal é aquele cuja demanda aumenta mais que proporcionalmente ao aumento da "
            "renda.”</i> → ERRADO (restrição indevida: isso define bem de luxo)",
            "<i>“Todo bem de luxo é normal, mas nem todo bem normal é de luxo.”</i> → CERTO",
        ])],
        tipo_erro=["LITERAL"], moduladores=[], dificuldade=1,
        comentario_fonte="CERTO. Bens normais têm demanda crescente com o aumento da renda. Exemplos: viagens, "
                         "automóveis e vestuário.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=["quase_duplicata: ECO-E1-0070-1 cobra a mesma definição com outra redação (mesma fonte)"],
    ),
    # ------------------------------------------------------------------ E1-0082
    card(
        id="ECO-E1-0082-1", fonte_ref="E1-0082", subtema=H2["of"], comando=CMD_OD,
        assertiva=("O deslocamento para a esquerda da curva de oferta de um bem pode ser ocasionado por um aumento "
                   "do preço do bem complementar."),
        gabarito="ERRADO",
        anotada=az("O deslocamento para a esquerda da curva ") + vm("de oferta") + az(" de um bem pode ser "
                                                                                     "ocasionado por um aumento do preço do bem complementar."),
        poucas=("Complementaridade no consumo é determinante da " + azb("demanda") + ": encarecer o complementar "
                "desloca para a esquerda a curva de <b>demanda</b> do bem, não a de oferta."),
        destrinchando=[
            "Determinantes da " + azb("oferta") + ": preço dos insumos, tecnologia, preços de bens "
            "relacionados <b>na produção</b>, expectativas, número de vendedores, tributos e subsídios. "
            "Preferências e preços de bens relacionados <b>no consumo</b> (substitutos e complementares) mexem "
            "na demanda.",
            "Com complementares no consumo (carne e carvão): carne mais cara → demanda por carvão para a "
            + vd("esquerda") + " → preço e quantidade do carvão caem. A oferta de carvão não se moveu; os "
            "produtores apenas descem ao longo dela.",
            "Na produção, a relação relevante é outra. " + azb("Substitutos na produção") + " (soja × milho na "
            "mesma terra): soja mais cara → produtor migra → oferta de milho para a esquerda. "
            + azb("Produtos conjuntos") + " (carne × couro): carne mais cara → abate maior → oferta de couro "
            "para a <b>direita</b>. Nos dois casos, “complementar” não descreve a relação que desloca a oferta "
            "para a esquerda.",
            vm("Regra-âncora: bens relacionados no consumo → demanda; bens relacionados na produção → oferta."),
        ],
        dissecando=(cz("[troca de conceito]") + " O item cola um determinante de demanda na curva de oferta. "
                    "O sentido (esquerda) está certo para a demanda, o que dá ao item cara de verdadeiro. "
                    "Pergunta-teste: o choque muda o <b>custo</b> de quem produz ou a <b>vontade</b> de quem "
                    "compra?"),
        modulos=[("😈 Para dificultar", [
            "<i>“O deslocamento para a esquerda da curva de oferta de um bem pode ser ocasionado por um aumento "
            "do preço de um insumo usado em sua produção.”</i> → CERTO",
            "<i>“O deslocamento para a esquerda da curva de demanda de um bem pode ser ocasionado por uma queda "
            "do preço do bem complementar.”</i> → ERRADO (inversão: complementar mais barato desloca para a "
            "direita)",
        ])],
        reescrita=("O deslocamento para a esquerda da curva " + hl("de demanda") + " de um bem pode ser "
                   "ocasionado por um aumento do preço do bem complementar."),
        tipo_erro=["TROCA_CONCEITO"], moduladores=["pode"], dificuldade=2,
        comentario_fonte="ERRADO. Complementariedade entre bens influencia a demanda, não a oferta do bem "
                         "diretamente.",
        qualidade_fonte="bom",
        figuras_fonte=[],
        alertas=[],
    ),
]
