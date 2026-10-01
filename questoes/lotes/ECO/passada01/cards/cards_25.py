"""Cards da passada 01 de ECO — lote de redação 25 (nota 12: externalidades, bens públicos e comuns, informação)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl  # noqa: F401

H2 = {
    "ext": "🌫️ Externalidades e Coase",
    "bens": "🏞️ Bens públicos e comuns",
    "info": "🕵️ Informação assimétrica",
}

CMD_NIDI = "Julgue o item a seguir, relativo às externalidades e à tributação corretiva."
CMD_BOZAN = ("Sobre as falhas de mercado e as intervenções governamentais para corrigir essas falhas, julgue as "
             "assertivas a seguir.")
CMD_ARM = "Julgue o item a seguir, relativo às falhas de mercado."
CMD_NAB26A = "A respeito de falhas de mercado, julgue (C ou E) os itens a seguir."
CMD_NAB26B = "Sobre externalidades e bens públicos, julgue (C ou E) os seguintes itens."
CMD_NAB_EST = "Em relação às estruturas de mercado e às falhas de mercado, julgue (C ou E) os seguintes itens."
CMD_NAB_FALHAS = "Em relação às falhas de mercado e aos diferentes tipos de bens, julgue (C ou E) os itens que se seguem."
CMD_NAB_TIPOS = "Em relação aos diferentes tipos de bens, julgue (C ou E) os itens que se seguem."
CMD_NAB_MICRO = ("Em relação à microeconomia e à teoria do comércio internacional, julgue (C ou E) os seguintes "
                 "itens.")
CMD_NAB_CONS = "No que se refere à teoria do consumidor e às falhas de mercado, julgue (C ou E) os seguintes itens."
CMD_NAB_EXT = ("Em relação aos conceitos de externalidades, bens públicos e recursos comuns, julgue (C ou E) os "
               "itens a seguir.")
CMD_NAB_COASE = "Com referência ao teorema de Coase, julgue (C ou E) os itens a seguir."

CARDS = [
    # ------------------------------------------------------------------ E1-0954
    {
        "id": "ECO-E1-0954-1", "fonte_ref": "E1-0954", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI,
        "rotulo_item": "Item",
        "assertiva": ("O Imposto pigouviano é uma das ferramentas utilizadas pelo Estado para correção de "
                      "externalidades negativas. Este é o caso da taxação do combustível, utilizada com a "
                      "finalidade de reduzir a poluição do ar. O imposto pode ser aplicado tanto às indústrias, "
                      "incentivando a redução da oferta do bem gerador da externalidade negativa, quanto sobre o "
                      "bem final, incentivando uma redução no consumo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Imposto pigouviano é uma das ferramentas utilizadas pelo Estado para correção de "
                      "externalidades negativas. Este é o caso da taxação do combustível, utilizada com a "
                      "finalidade de reduzir a poluição do ar. O imposto pode ser aplicado <u>tanto às "
                      "indústrias</u>, incentivando a redução da oferta do bem gerador da externalidade negativa, "
                      "<u>quanto sobre o bem final</u>, incentivando uma redução no consumo."),
        "poucas": ("O " + azb("imposto pigouviano") + " cobra de quem gera a externalidade negativa um valor "
                   "igual ao dano marginal, fazendo o preço refletir o " + azb("custo social") + ". Pode incidir "
                   "na produção ou no consumo: nos dois casos, a quantidade do bem poluidor cai."),
        "destrinchando": [
            azb("Externalidade") + " é o efeito da produção ou do consumo sobre terceiros que não passa pelo "
            "sistema de preços. Negativa (poluição, fumo passivo, congestionamento) → o mercado produz "
            "<b>demais</b>; positiva (vacina, pesquisa, educação) → produz <b>de menos</b>.",
            "A solução de " + oc("Arthur C. Pigou") + " (<i>The Economics of Welfare</i>, 1920) é "
            + azb("internalizar") + " o custo externo: um tributo por unidade igual ao custo externo marginal "
            "no nível ótimo. O agente passa a decidir com o custo social na conta, e o mercado converge ao "
            "ótimo sem que o governo precise dizer quanto cada um deve produzir.",
            "Onde o imposto incide legalmente não muda o resultado econômico: tributar a refinaria (a oferta "
            "recua) ou o consumidor de gasolina (a demanda recua) abre a mesma " + azb("cunha") + " entre o "
            "preço pago e o recebido. Quem arca com o ônus é decidido pelas " + azb("elasticidades") + ", não "
            "pela lei.",
            "O imposto sobre combustíveis é o exemplo clássico de " + oc("Mankiw") + ": corrige poluição e "
            "congestionamento ao mesmo tempo. Destinar a receita a reparar o dano (o imposto sobre cigarro "
            "custeando saúde) é opção política, não condição do imposto pigouviano: ele corrige pelo "
            "<b>incentivo</b>, e não pelo uso da arrecadação.",
            vm("Regra-âncora: externalidade negativa → imposto pigouviano = custo externo marginal no ótimo."),
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " Item conceitual sem armadilha de sinal; o risco está "
                       "no “tanto às indústrias quanto sobre o bem final”, que tenta fazer o candidato achar que "
                       "o imposto só vale num dos lados. 🔥 A banca adora a equivalência da incidência legal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O imposto pigouviano só é eficaz se a receita arrecadada for aplicada na reparação do dano "
            "ambiental.”</i> → ERRADO (restrição indevida: corrige pelo incentivo)",
            "<i>“O imposto pigouviano, ao contrário dos demais tributos, pode elevar a eficiência "
            "econômica.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": ["pode", "tanto … quanto"], "dificuldade": 1,
        "comentario_fonte": ("Imposto pigouviano penaliza externalidades negativas e as internaliza; externalidade "
                             "é efeito não precificado, positivo ou negativo; exemplos de tributo sobre poluição "
                             "de rio e cigarro com receita aplicada no SUS; resposta de IA reforça a incidência "
                             "na indústria ou no consumidor final."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (316).png", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "irrecuperavel (não preservada; o texto que a acompanha foi absorvido no 📖)"}],
        "alertas": ["texto_corrigido: “quando sobre o bem final” → “quanto sobre o bem final” (correlação "
                    "tanto … quanto)"],
    },
]
