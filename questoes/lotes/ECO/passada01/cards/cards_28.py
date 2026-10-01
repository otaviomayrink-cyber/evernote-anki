"""Card faltante da passada 01 (item E1-0260, omitido no lote 03)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

CARDS = [
    {
        "id": "ECO-E1-0260-1", "fonte_ref": "E1-0260", "destino": "01",
        "subtema": "⚖️ Equilíbrio e estática comparativa",
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False, "errei": False,
        "comando": "Acerca do funcionamento dos mercados competitivos e do sistema de preços, julgue o item.",
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia operando sob concorrência perfeita, sem governo nem comércio exterior, os preços "
                      "são uma medida da escassez dos produtos, tendendo à alta sempre que houver uma eventual redução "
                      "na oferta desses bens, mantidos todos os demais fatores e relações constantes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia operando sob concorrência perfeita, sem governo nem comércio exterior, os preços "
                      "são uma medida da escassez dos produtos, tendendo à alta sempre que houver uma eventual "
                      "<u>redução na oferta</u> desses bens, <u>mantidos todos os demais fatores e relações "
                      "constantes</u>."),
        "poucas": ("No mercado competitivo o preço é um " + azb("sinal de escassez relativa") + ": se a oferta "
                   "cai e a demanda fica parada (" + azb("ceteris paribus") + "), o equilíbrio se desloca para "
                   "preço " + vd("maior") + " e quantidade " + vd("menor") + "."),
        "destrinchando": [
            "Escassez, em Economia, não é “pouca quantidade” em termos absolutos, mas pouca quantidade " +
            "<b>relativamente ao que se deseja</b> a cada preço. O preço de equilíbrio resume essa relação: sobe "
            "quando o bem fica mais escasso e cai quando fica mais abundante.",
            "Redução da oferta = deslocamento da curva de oferta para a esquerda (quebra de safra, alta de custo "
            "de insumo, saída de firmas). Ao preço antigo surge " + azb("excesso de demanda") + "; a "
            "concorrência entre compradores empurra o preço para cima até o novo equilíbrio, com p ↑ e q ↓.",
            "É a ideia da " + azb("mão invisível") + " de " + oc("Adam Smith") + " e do preço como portador de "
            "informação de " + oc("Hayek") + " (“O uso do conhecimento na sociedade”, 1945): o preço transmite a "
            "todos, sem planejamento central, que o bem ficou mais escasso — e induz a economizá-lo e a "
            "produzi-lo mais.",
            "As cláusulas do item fazem trabalho: “concorrência perfeita” afasta poder de mercado (o preço não é "
            "fixado por um monopolista); “sem governo” afasta tabelamento, que impediria a alta e geraria "
            "escassez com fila; “ceteris paribus” afasta uma queda simultânea da demanda que pudesse anular o "
            "efeito.",
            vm("Regra-âncora: oferta ↓ com demanda constante → preço ↑ e quantidade ↓."),
        ],
        "grafico_verso": "ECO-E1-0260-1-V1",
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O item repete a definição de manual do "
                       "sistema de preços. O risco está no “sempre que”, que soa absoluto, mas vem protegido por "
                       "“mantidos todos os demais fatores e relações constantes” e pelo “tendendo à alta”. Sem "
                       "essas cláusulas, um choque simultâneo de demanda poderia tornar o item discutível."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…os preços tendem à baixa sempre que houver redução na oferta…”</i> → ERRADO (inversão: menos "
            "oferta eleva o preço)",
            "<i>“…a redução da oferta eleva o preço e a quantidade transacionada…”</i> → ERRADO (a quantidade "
            "cai)",
            "<i>“Com tabelamento de preços pelo governo, a redução da oferta se traduz em filas e "
            "desabastecimento, e não em alta de preço.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["sempre que", "tendendo",
                                                                            "mantidos todos os demais"],
        "dificuldade": 1,
        "comentario_fonte": "Em concorrência perfeita o preço sinaliza escassez; redução da oferta ceteris "
                            "paribus eleva o preço.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "Untitled (53).jpeg", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "irrecuperavel (redesenhada em ECO-E1-0260-1-V1)"}],
        "alertas": ["nota_redacao: card escrito na montagem (item omitido no lote 03)"],
    },
]
