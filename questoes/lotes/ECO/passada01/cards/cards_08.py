"""Cards do lote de redação 08 — ECO, passada 01 (nota 03: intervenções do Estado e bem-estar)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "exc": "😊 Excedentes e eficiência",
    "trib": "💸 Tributos: incidência e peso morto",
    "sub": "🧾 Subsídios",
    "piso": "🚧 Preços máximos e mínimos",
}

CMD_INC = "Julgue o item a seguir, relativo à incidência de tributos em mercados competitivos."

CMD_2013 = ("Supondo que o governo adote um novo imposto específico sobre a venda de um bem em um mercado de "
            "concorrência perfeita e considerando a distribuição da incidência tributária entre vendedores e "
            "consumidores, julgue o item a seguir.")

CMD_BOZAN = "Julgue o item a seguir, sobre políticas de preço mínimo e suas implicações econômicas."

CMD_NAB_EQ = ("Em um mercado competitivo, as curvas de demanda e de oferta de um produto são Qᴰ = 300 − 30p e "
              "Qˢ = 10p + 20, em que p é o preço do produto, em reais. Julgue o item.")

CMD_NAB_4 = "Considerando os conceitos de microeconomia, julgue o item a seguir."

FIG_E1 = lambda ref: [{"ref": ref, "tipo_fonte": "GRÁFICO", "lado": "verso",
                       "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}]

CARDS = [
    # ------------------------------------------------------------------ E1-0173
    {
        "id": "ECO-E1-0173-1", "fonte_ref": "E1-0173", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INC,
        "rotulo_item": "Item",
        "assertiva": ("A incidência de um imposto sobre vendas em um mercado de concorrência perfeita é "
                      "integralmente suportada pelos consumidores, independentemente da elasticidade-preço da "
                      "demanda do bem."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A incidência de um imposto sobre vendas em um mercado de concorrência perfeita é ")
                    + vm("integralmente suportada pelos consumidores, independentemente da elasticidade-preço da "
                         "demanda do bem") + az(".")),
        "poucas": ("A " + azb("incidência econômica") + " de um imposto se reparte entre compradores e vendedores "
                   "conforme as " + azb("elasticidades") + " da demanda e da oferta; o repasse integral ao "
                   "consumidor é caso-limite, não regra."),
        "destrinchando": [
            "Um imposto sobre vendas abre uma " + azb("cunha") + " entre o preço pago pelo comprador (pc) e o "
            "recebido pelo vendedor (pv): pc − pv = t. A pergunta da incidência é quanto de t vem de alta de pc e "
            "quanto vem de queda de pv.",
            "Fórmula de bolso: fração paga pelo consumidor = " + vd("εˢ / (εˢ + |εᴰ|)") + "; fração paga pelo "
            "produtor = " + vd("|εᴰ| / (εˢ + |εᴰ|)") + ". Quem é <b>menos elástico</b> arca com mais.",
            "Os únicos casos de repasse integral ao consumidor são os extremos: " + vd("|εᴰ| = 0") + " (demanda "
            "vertical) ou " + vd("εˢ = ∞") + " (oferta horizontal). No extremo oposto — demanda infinitamente "
            "elástica — o consumidor não paga nada.",
            "A incidência <b>legal</b> (quem recolhe o tributo ao fisco) não decide nada: cobrado do vendedor ou do "
            "comprador, o equilíbrio final é o mesmo.",
            vm("Regra-âncora: o ônus do imposto cai sobre o lado menos elástico do mercado."),
        ],
        "dissecando": (cz("[modulador absoluto · contradição]") + " Dois absolutos empilhados — "
                       "“integralmente” e “independentemente da elasticidade” — negam justamente a variável que "
                       "decide a incidência. Em itens de tributo, “independentemente da elasticidade” é quase "
                       "sempre o sinal do erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…é integralmente suportada pelos consumidores se a demanda do bem for perfeitamente "
            "inelástica.”</i> → CERTO",
            "<i>“…é integralmente suportada pelos consumidores se a demanda for infinitamente elástica.”</i> → "
            "ERRADO (inversão: nesse caso quem paga tudo é o vendedor)",
        ])],
        "reescrita": ("A incidência de um imposto sobre vendas em um mercado de concorrência perfeita é "
                      + hl("repartida entre consumidores e vendedores, conforme as elasticidades-preço da demanda "
                           "e da oferta") + " do bem."),
        "tipo_erro": ["GENERALIZACAO", "CONTRADICAO"], "moduladores": ["integralmente", "independentemente"],
        "dificuldade": 1,
        "comentario_fonte": "A incidência depende das elasticidades da demanda e da oferta; o lado menos elástico "
                            "suporta a maior parte; não há repasse integral automático.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0177
    {
        "id": "ECO-E1-0177-1", "fonte_ref": "E1-0177", "destino": "03", "subtema": H2["trib"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_INC,
        "rotulo_item": "Item",
        "assertiva": ("Com relação à incidência de um imposto sobre vendas de um bem X num mercado em concorrência "
                      "perfeita, é correto afirmar que o ônus do imposto recai mais fortemente sobre os vendedores "
                      "ou consumidores dependendo do valor das respectivas elasticidades-preço."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Com relação à incidência de um imposto sobre vendas de um bem X num mercado em concorrência "
                      "perfeita, é correto afirmar que o ônus do imposto recai <u>mais fortemente</u> sobre os "
                      "vendedores ou consumidores <u>dependendo do valor das respectivas elasticidades-preço</u>."),
        "poucas": ("É a regra geral da incidência: o ônus pesa mais sobre o lado " + azb("menos elástico")
                   + " — vendedores, se a oferta for mais rígida; consumidores, se a demanda for."),
        "destrinchando": [
            "Com o imposto t, o preço pago sobe e o recebido cai; a soma das duas variações é t. A divisão "
            "depende da capacidade de cada lado de <b>fugir</b> do mercado: quem tem alternativas (substitutos, "
            "outros usos para os fatores) reduz a quantidade e empurra o ônus para o outro.",
            "Em fórmula: parcela do consumidor = " + vd("εˢ / (εˢ + |εᴰ|)") + ". Se |εᴰ| < εˢ, o consumidor "
            "paga mais da metade; se |εᴰ| > εˢ, o vendedor paga mais.",
            "Exemplos típicos: combustíveis e cigarros (demanda inelástica) → a maior parte vai para o "
            "consumidor; produtos agrícolas já plantados ou imóveis (oferta rígida no curto prazo) → a maior "
            "parte vai para o produtor.",
            "Por isso a incidência legal é irrelevante: o que importa são as inclinações das curvas, não quem "
            "assina a guia de recolhimento.",
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz a regra do manual. O "
                       "“mais fortemente” protege o item: não diz que um lado paga tudo, só que pesa mais sobre um "
                       "deles conforme as elasticidades."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o ônus recai mais fortemente sobre o lado de maior elasticidade-preço.”</i> → ERRADO "
            "(inversão: recai sobre o de menor elasticidade)",
            "<i>“…o ônus recai mais fortemente sobre quem recolhe o imposto ao fisco.”</i> → ERRADO (troca de "
            "conceito: incidência legal × econômica)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["mais fortemente", "dependendo"],
        "dificuldade": 1,
        "comentario_fonte": "O ônus depende das elasticidades relativas; o lado mais inelástico suporta a maior "
                            "parte.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
]
