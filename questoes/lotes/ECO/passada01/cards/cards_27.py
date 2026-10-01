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
]
