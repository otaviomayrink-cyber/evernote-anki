"""Cards da redação ECO — passada 01 — lote 22 (notas 09 — Concorrência monopolística e 10 — Oligopólios)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "cham": "🧩 Modelo de Chamberlin",
    "cb": "🧮 Cournot e Bertrand",
    "stack": "🥇 Stackelberg e liderança",
    "cartel": "🤝 Cartel e conluio",
    "conc": "📏 Concentração e outras teorias",
}

COM_RT_MICRO = "A respeito dos conceitos e teorias da microeconomia, julgue os itens a seguir."
COM_RT_FIRMA = "A respeito da teoria da firma, julgue os itens a seguir."
COM_RT_ESTR = "Sobre as diferentes estruturas de mercado, julgue as afirmações a seguir."
COM_ARM = "Acerca dos modelos de oligopólio, julgue o item a seguir."
COM_NAB_OLIG = "Em relação aos modelos de oligopólio, julgue (C ou E) os seguintes itens."
COM_NAB_ESTR_1 = "Em relação às estruturas de mercado, julgue (C ou E) os seguintes itens."
COM_E1_OLIG = "Acerca das estruturas de mercado oligopolistas e da defesa da concorrência, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01658
    {
        "id": "ECO-E2-L01658-1", "fonte_ref": "E2-L01658", "destino": "09", "subtema": H2["cham"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": COM_RT_MICRO,
        "rotulo_item": "Item",
        "assertiva": ("O equilíbrio de competição monopolística no longo prazo caracteriza-se por produção abaixo da "
                      "escala eficiente, porém a livre entrada e saída de firmas levará ao resultado idêntico ao da "
                      "competição perfeita, com preço igual ao custo marginal."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O equilíbrio de competição monopolística no longo prazo caracteriza-se por produção abaixo da "
                      "escala eficiente, porém a livre entrada e saída de firmas levará ao ")
                   + vm("resultado idêntico ao da competição perfeita, com preço igual ao custo marginal") + az("."),
        "poucas": ("A livre entrada zera o " + azb("lucro econômico") + " (P = CMe), como na concorrência perfeita, "
                   "mas não iguala preço e custo marginal: com demanda inclinada, " + vd("P > RMg = CMg") + "."),
        "destrinchando": [
            "No modelo de " + oc("Chamberlin") + " (<i>The Theory of Monopolistic Competition</i>, 1933), cada "
            "firma vende um produto " + azb("diferenciado") + " e enfrenta demanda negativamente inclinada; por "
            "isso a receita marginal fica abaixo do preço (RMg < P), como no monopólio.",
            "Curto prazo: a firma produz onde RMg = CMg e pode ter lucro. Longo prazo: o lucro atrai entrantes "
            "com substitutos próximos, a demanda de cada firma recua até ficar " + azb("tangente ao CMe")
            + ". No ponto de tangência, " + vd("P = CMe") + " (lucro zero) e, como a firma continua "
            "maximizando lucro, RMg = CMg < P.",
            "Consequências que distinguem as duas estruturas: (1) " + azb("ineficiência alocativa") + " — P > CMg, "
            "há um <i>markup</i> e um pequeno peso morto; (2) " + azb("excesso de capacidade") + " — a tangência "
            "ocorre no trecho <b>descendente</b> do CMe, à esquerda do custo médio mínimo (a parte do item que "
            "está certa).",
            "Na concorrência perfeita de longo prazo vale a tripla igualdade " + vd("P = CMg = CMe mínimo")
            + ": eficiência alocativa e produtiva ao mesmo tempo. Na monopolística, só sobra a igualdade P = CMe.",
            "Contrapartida usual: a ineficiência é o “preço” da " + azb("variedade") + " de produtos que o "
            "consumidor valoriza.",
            vm("Regra-âncora: concorrência monopolística no longo prazo = lucro zero (P = CMe) com P > CMg e "
               "capacidade ociosa."),
        ],
        "grafico_verso": "ECO-E2-L01658-1-V1",
        "dissecando": (cz("[meia-verdade · troca de conceito]") + " A 1ª oração (produção abaixo da escala "
                       "eficiente) é verdadeira e dá confiança; depois do “porém”, o item transporta para a "
                       "monopolística a condição P = CMg, que é exclusiva da concorrência perfeita. Pista: lucro "
                       "zero (P = CMe) não implica P = CMg. 🔥 A banca alterna “lucro zero” (CERTO) e “P = CMg” "
                       "(ERRADO) no mesmo bloco."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, a livre entrada leva as firmas monopolisticamente competitivas ao lucro econômico "
            "nulo, como na concorrência perfeita.”</i> → CERTO",
            "<i>“No longo prazo, a firma em competição monopolística produz no ponto mínimo do custo médio.”</i> → "
            "ERRADO (a tangência ocorre no trecho descendente do CMe)",
        ])],
        "reescrita": ("O equilíbrio de competição monopolística no longo prazo caracteriza-se por produção abaixo da "
                      "escala eficiente, porém a livre entrada e saída de firmas levará ao " + hl("lucro econômico "
                      "nulo, como na competição perfeita, mas com preço superior ao custo marginal") + "."),
        "tipo_erro": ["MEIA_VERDADE", "TROCA_CONCEITO"], "moduladores": ["idêntico"], "dificuldade": 2,
        "comentario_fonte": ("Três explicações convergentes: lucro zero com P = CMe e tangência no trecho "
                             "descendente do CMe; porém P > CMg por causa da demanda inclinada; quadro comparativo "
                             "concorrência perfeita × monopolística."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 483", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "cortada (gráfico de terceiros; mecanismo redesenhado em ECO-E2-L01658-1-V1)"}],
        "alertas": [],
    },
]
