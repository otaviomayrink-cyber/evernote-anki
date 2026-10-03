"""Cards do lote de redação 08 — ECO, passada 02 (nota 19: resultados fiscais/NFSP; nota 25: modelo clássico e TQM)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "nfsp": "💰 Resultados fiscais (NFSP)",
    "cla": "⚙️ Modelo clássico",
    "tqm": "💵 Teoria quantitativa da moeda",
}

CMD_NAB_CF = ("Julgue (C ou E) os itens a seguir, relativos a conceitos básicos de contabilidade fiscal e "
              "sustentabilidade do endividamento público.")

CMD_NAB_DD = "No que se refere aos conceitos de déficit público e de dívida pública, julgue (C ou E) o item a seguir."

CMD_RT_FISC = "A respeito da política fiscal e da dívida pública, julgue o item a seguir."

CMD_RT_FE = "Acerca do mercado de fundos emprestáveis, julgue o item a seguir (C ou E)."

CMD_RT_CLA = "A respeito do modelo clássico, julgue o item a seguir (C ou E)."

FIG_E1 = lambda ref: [{"ref": ref, "tipo_fonte": "GRÁFICO", "lado": "verso",
                       "acao": "cortada (imagem do verso não preservada; mecanismo redesenhado no 📈)"}]

CARDS = [
    # ------------------------------------------------------------------ E2-L00948
    {
        "id": "ECO-E2-L00948-1", "fonte_ref": "E2-L00948", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_CF,
        "rotulo_item": "Item",
        "assertiva": ("A respeito da contabilidade fiscal, considerando os conceitos de necessidade de financiamento "
                      "do setor público, a diferença entre resultado nominal e resultado primário, refere-se à "
                      "variação da inflação no período de apuração."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A respeito da contabilidade fiscal, considerando os conceitos de necessidade de financiamento "
                       "do setor público, a diferença entre resultado nominal e resultado primário, refere-se ")
                    + vm("à variação da inflação") + az(" no período de apuração.")),
        "poucas": ("O que separa o nominal do primário são os " + azb("juros nominais") + " da dívida (juros reais "
                   "+ atualização monetária). A inflação só entra indiretamente, como parte desses juros."),
        "destrinchando": [
            "As três medidas das " + azb("NFSP") + " (necessidades de financiamento do setor público) se "
            "encaixam como camadas: " + vd("nominal = primário + juros nominais") + "; " + vd("operacional = "
            "primário + juros reais") + ". Logo, nominal − primário = juros nominais, e nominal − operacional = "
            "atualização monetária (e cambial) da dívida.",
            azb("Resultado primário") + ": receitas menos despesas não financeiras — o esforço fiscal do período, "
            "sem o custo da dívida herdada.",
            azb("Juros nominais") + " = juros reais + correção monetária do estoque. Com inflação de 10% e dívida "
            "de 100 corrigida por ela, cerca de 10 dos juros pagos apenas repõem o valor real do principal.",
            "A inflação, portanto, não é “a diferença” entre os conceitos: é só um componente dela. Com inflação "
            "nula, nominal − primário continuaria positivo, igual aos juros reais.",
            vm("Regra-âncora: nominal − primário = juros nominais; nominal − operacional = correção monetária."),
        ],
        "dissecando": (cz("[troca de conceito · meia-verdade]") + " O item troca o componente inteiro (juros "
                       "nominais) por uma de suas parcelas (a atualização monetária ligada à inflação), que é, na "
                       "verdade, o que separa o nominal do <b>operacional</b>. 🔥 A banca alterna as três "
                       "diferenças entre nominal, primário e operacional; monte a escada antes de julgar."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A diferença entre os resultados nominal e operacional corresponde à atualização monetária da "
            "dívida.”</i> → CERTO",
            "<i>“A diferença entre os resultados operacional e primário corresponde aos juros nominais.”</i> → "
            "ERRADO (são os juros reais)",
        ])],
        "reescrita": ("A respeito da contabilidade fiscal, considerando os conceitos de necessidade de financiamento "
                      "do setor público, a diferença entre resultado nominal e resultado primário, refere-se "
                      + hl("aos juros nominais (juros reais mais atualização monetária) da dívida")
                      + " no período de apuração."),
        "tipo_erro": ["TROCA_CONCEITO", "MEIA_VERDADE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A diferença entre nominal e primário são os juros nominais (juros reais + atualização "
                            "monetária); o nominal abrange atualização monetária, juros reais e primário.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: “A respeito na contabilidade fiscal” → “A respeito da contabilidade "
                    "fiscal” (erro evidente de digitação)"],
    },
    # ------------------------------------------------------------------ E2-L00949
    {
        "id": "ECO-E2-L00949-1", "fonte_ref": "E2-L00949", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": CMD_NAB_CF,
        "rotulo_item": "Item",
        "assertiva": ("Considerando uma situação hipotética de inflação nula, o valor das necessidades de "
                      "financiamento do setor público - conceito operacional corresponderá ao mesmo valor do "
                      "conceito nominal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considerando uma situação hipotética de <u>inflação nula</u>, o valor das necessidades de "
                      "financiamento do setor público - conceito operacional corresponderá ao mesmo valor do "
                      "conceito nominal."),
        "poucas": ("O operacional é o nominal " + azb("sem a atualização monetária") + " da dívida. Se a inflação "
                   "é zero, essa correção é zero e os dois conceitos coincidem."),
        "destrinchando": [
            "Escada das NFSP: " + vd("nominal = primário + juros nominais") + "; " + vd("operacional = primário "
            "+ juros reais") + ". A distância entre os dois é a parcela dos juros que apenas corrige o valor do "
            "estoque pela inflação (e, na dívida em moeda estrangeira, pela variação cambial).",
            "Com inflação nula, juros nominais = juros reais (pela relação de " + oc("Fisher") + ", i ≈ r + π, "
            "com π = 0). Sem correção a descontar, operacional = nominal.",
            "Por que o conceito existe: em alta inflação, boa parte dos juros nominais só repõe o principal, e o "
            "déficit nominal “incha” sem que o desequilíbrio real tenha mudado. O " + azb("conceito operacional")
            + " foi muito usado no " + rx("Brasil") + " dos anos 1980 e início dos 1990, inclusive nos acordos "
            "com o FMI, justamente para limpar esse efeito.",
            "Com inflação baixa e estável (pós-Real), os dois conceitos ficam próximos, e o acompanhamento passou "
            "a privilegiar o primário (meta) e o nominal (dívida).",
        ],
        "dissecando": (cz("[detalhe]") + " Item de dedução: basta lembrar o que o operacional exclui. A banca "
                       "aposta na confusão operacional × primário — quem pensa que o operacional exclui todos os "
                       "juros marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Com inflação nula, as NFSP no conceito primário corresponderão às do conceito nominal.”</i> → "
            "ERRADO (ainda restam os juros reais)",
            "<i>“Quanto maior a inflação, maior tende a ser a diferença entre os conceitos nominal e "
            "operacional.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Operacional = primário + juros reais (nominal menos atualização monetária). Com "
                            "inflação nula, a correção é zero e o nominal iguala o operacional.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00977
    {
        "id": "ECO-E2-L00977-1", "fonte_ref": "E2-L00977", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": ("Considerando a teoria macroeconômica e os principais agregados macroeconômicos, julgue (C ou E) "
                    "o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A NFSP no conceito primário é obtida pela diferença entre as NFSP no conceito nominal e as "
                      "despesas de juros nominais incidentes sobre a DLSP, calculadas pelo critério de competência e "
                      "descontada a receita de juros relativa à aplicação das reservas internacionais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A NFSP no conceito primário é obtida pela diferença entre as NFSP no conceito nominal e as "
                      "despesas de <u>juros nominais</u> incidentes sobre a DLSP, calculadas pelo critério de "
                      "<u>competência</u> e <u>descontada a receita de juros</u> relativa à aplicação das reservas "
                      "internacionais."),
        "poucas": ("É a definição do " + rx("Banco Central") + ": " + vd("primário = nominal − juros nominais "
                   "líquidos") + ", apropriados por competência e já descontados os juros que o setor público "
                   "recebe, inclusive sobre as reservas."),
        "destrinchando": [
            "A " + azb("DLSP") + " (dívida líquida do setor público) é passivo menos ativo financeiro. Por isso os "
            "juros que entram na conta também são <b>líquidos</b>: juros pagos sobre a dívida menos juros "
            "recebidos sobre os ativos.",
            "As " + azb("reservas internacionais") + " são ativo do Banco Central, que integra o setor público "
            "consolidado. A remuneração delas reduz os juros líquidos — daí o “descontada a receita de juros” do "
            "item.",
            azb("Critério de competência") + ": os juros são apropriados quando incorrem (dia a dia, sobre o "
            "estoque), não quando são pagos. Um título que só paga no vencimento gera despesa de juros todo mês.",
            "Fechando a escada: " + vd("nominal = primário + juros nominais líquidos") + "; operacional = primário "
            "+ juros reais. Isolar o primário mostra o esforço fiscal sem o peso da dívida herdada e da política "
            "monetária.",
            "Leitura brasileira: com dívida elevada e Selic alta, os juros nominais costumam ficar entre "
            + vd("5% e 8% do PIB") + " ⏳ (out/2026), de modo que um primário próximo de zero convive com déficit "
            "nominal grande.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item reproduz a nota metodológica do Banco Central, "
                       "carregada de qualificadores (“competência”, “descontada a receita”, “reservas”) para "
                       "assustar. Nenhum deles está errado: os juros da DLSP são líquidos e apropriados por "
                       "competência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as despesas de juros reais incidentes sobre a DLSP…”</i> → ERRADO (com juros reais sai o "
            "operacional, não o primário)",
            "<i>“…calculadas pelo critério de caixa…”</i> → ERRADO (critério trocado: é competência)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Primário = nominal menos juros nominais líquidos, descontadas as receitas de juros de "
                            "ativos do setor público, inclusive reservas (o BC integra o setor público consolidado).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01029
    {
        "id": "ECO-E2-L01029-1", "fonte_ref": "E2-L01029", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Em relação aos modelos macroeconômicos, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em economias de inflação elevada, o resultado nominal das necessidades de financiamento do "
                      "setor público tende a superestimar o desequilíbrio orçamentário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em economias de <u>inflação elevada</u>, o resultado nominal das necessidades de "
                      "financiamento do setor público <u>tende a superestimar</u> o desequilíbrio orçamentário."),
        "poucas": ("Com inflação alta, grande parte dos juros nominais é só " + azb("correção monetária")
                   + " do estoque da dívida: o déficit nominal “incha” sem que o desequilíbrio real tenha crescido."),
        "destrinchando": [
            "Juros nominais = juros reais + atualização monetária. A atualização não é gasto novo: apenas repõe o "
            "valor real do principal que a inflação corroeu. Em termos reais, a dívida não aumenta por causa dela.",
            "Exemplo: dívida de 100, juro real de 5% e inflação de 40%. Juros nominais ≈ " + vd("45") + " (i ≈ r "
            "+ π), dos quais " + vd("40") + " são correção. Com primário zero, o déficit nominal é 45; o "
            + azb("operacional") + ", que mede o desequilíbrio real, é só " + vd("5") + ".",
            "Por isso, em contextos de alta inflação usa-se o " + azb("conceito operacional") + " (primário + "
            "juros reais). Foi o caso do " + rx("Brasil") + " nos anos 1980 e no início dos 1990: o déficit "
            "nominal chegava a dezenas de pontos do PIB, enquanto o operacional era muito menor.",
            "O mesmo raciocínio vale ao contrário: se a inflação cai, o déficit nominal despenca sem que nenhum "
            "ajuste fiscal tenha sido feito.",
            "Com inflação baixa, nominal e operacional ficam próximos, e a distorção some.",
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " Item verdadeiro, protegido pelo “tende a”. Quem "
                       "associa “nominal” a “medida mais completa” pode achar que ele é sempre o retrato fiel; o "
                       "ponto é que, com inflação alta, ele mistura déficit real com mera correção do estoque."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em economias de inflação elevada, o resultado nominal tende a subestimar o desequilíbrio "
            "orçamentário.”</i> → ERRADO (inversão: superestima)",
            "<i>“Em contextos de inflação elevada, o resultado operacional é a medida mais adequada do "
            "desequilíbrio fiscal corrente.”</i> → CERTO",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": "Com inflação alta, a correção monetária da dívida infla os juros nominais; o "
                            "operacional, que a exclui, mede melhor o desequilíbrio. Com inflação baixa, nominal e "
                            "operacional ficam próximos.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01273
    {
        "id": "ECO-E2-L01273-1", "fonte_ref": "E2-L01273", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_DD,
        "rotulo_item": "Item",
        "assertiva": ("A diferença entre resultado primário e resultado nominal indica a despesa com os juros reais "
                      "incidentes sobre a dívida líquida do setor público."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A diferença entre resultado primário e resultado nominal indica a despesa com os juros ")
                    + vm("reais") + az(" incidentes sobre a dívida líquida do setor público.")),
        "poucas": ("Entre primário e nominal estão os juros " + azb("nominais") + ". Os juros " + azb("reais")
                   + " são a distância entre primário e <b>operacional</b>."),
        "destrinchando": [
            "Escada das NFSP: " + vd("nominal = primário + juros nominais") + " · " + vd("operacional = "
            "primário + juros reais") + " · nominal − operacional = atualização monetária e cambial da dívida.",
            "Juros nominais = juros reais + correção monetária. A correção apenas repõe o valor que a inflação "
            "tirou do estoque; os juros reais são o custo efetivo da dívida.",
            "Exemplo: primário zero, DLSP de 1.000, juros nominais de 12% e inflação de 4%. Nominal ≈ " + vd("120")
            + "; operacional ≈ " + vd("80") + " (juros reais de cerca de 8%). A diferença primário–nominal é 120, "
            "não 80.",
            "Os juros são líquidos: pagos sobre a dívida menos recebidos sobre os ativos (como as reservas), "
            "porque a base é a dívida <b>líquida</b>.",
            vm("Regra-âncora: primário → nominal: juros nominais; primário → operacional: juros reais."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Uma palavra muda o gabarito: “reais” no lugar de "
                       "“nominais”. O resto da frase é a definição correta. 🔥 A banca troca os pares da escada "
                       "(primário, operacional, nominal) e os tipos de juros; confira sempre qual degrau o item "
                       "liga a qual."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A diferença entre resultado primário e resultado operacional indica a despesa com os juros reais "
            "incidentes sobre a dívida líquida.”</i> → CERTO",
            "<i>“A diferença entre resultado nominal e operacional indica a despesa com os juros reais.”</i> → "
            "ERRADO (é a correção monetária)",
        ])],
        "reescrita": ("A diferença entre resultado primário e resultado nominal indica a despesa com os juros "
                      + hl("nominais") + " incidentes sobre a dívida líquida do setor público."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Déficit nominal = déficit primário + juros nominais líquidos.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01275
    {
        "id": "ECO-E2-L01275-1", "fonte_ref": "E2-L01275", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_DD,
        "rotulo_item": "Item",
        "assertiva": ("O resultado nominal medido pela variação da dívida fiscal líquida é um conceito fiscal "
                      "restrito que não está relacionado à necessidade de financiamento do setor público (NFSP)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O resultado nominal medido pela variação da dívida fiscal líquida ")
                    + vm("é um conceito fiscal restrito que não está relacionado") + az(" à necessidade de "
                    "financiamento do setor público (NFSP).")),
        "poucas": ("A variação da " + azb("dívida fiscal líquida") + " é justamente como o Banco Central mede as "
                   + vd("NFSP no conceito nominal") + ", pelo critério abaixo da linha."),
        "destrinchando": [
            "O " + rx("Banco Central") + " apura o resultado fiscal pelo lado do financiamento: se a dívida "
            "líquida do setor público cresceu, o setor público precisou se financiar (déficit); se caiu, houve "
            "superávit. É o " + azb("critério abaixo da linha") + ".",
            "Mas a DLSP também varia por fatores que não são déficit: privatizações, reconhecimento de dívidas "
            "antigas (os “esqueletos”), variação cambial sobre ativos e passivos em moeda estrangeira. Retirados "
            "esses " + azb("ajustes patrimoniais e metodológicos") + ", obtém-se a " + azb("dívida fiscal "
            "líquida") + ".",
            vd("NFSP nominal = Δ dívida fiscal líquida") + ". Do nominal derivam os demais: tira-se a correção "
            "monetária → operacional; tiram-se os juros nominais → primário.",
            "Logo o resultado nominal não é “restrito”: é o conceito <b>mais amplo</b> da família NFSP, e a DFL "
            "existe exatamente para medi-lo.",
        ],
        "dissecando": (cz("[contradição]") + " O item nega a identidade que define o conceito: a variação da DFL "
                       "<b>é</b> a NFSP nominal. O adjetivo “restrito” agrava o erro, pois o nominal é o conceito "
                       "mais abrangente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“As NFSP no conceito nominal correspondem à variação da DLSP, sem qualquer ajuste.”</i> → ERRADO "
            "(excluem-se os ajustes patrimoniais e metodológicos: usa-se a DFL)",
            "<i>“O resultado nominal apurado abaixo da linha corresponde à variação da dívida fiscal líquida.”</i> "
            "→ CERTO",
        ])],
        "reescrita": ("O resultado nominal medido pela variação da dívida fiscal líquida " + hl("corresponde")
                      + " à necessidade de financiamento do setor público (NFSP)" + hl(" no conceito nominal")
                      + "."),
        "tipo_erro": ["CONTRADICAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "NFSP nominal = variação da dívida fiscal líquida; é a medida do déficit nominal pelo "
                            "método abaixo da linha.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01276
    {
        "id": "ECO-E2-L01276-1", "fonte_ref": "E2-L01276", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_DD,
        "rotulo_item": "Item",
        "assertiva": ("As Necessidades de Financiamento do Setor Público são calculadas a partir da variação da "
                      "Dívida Fiscal Líquida, utilizando o critério conhecido como “acima da linha”."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As Necessidades de Financiamento do Setor Público são calculadas a partir da variação da "
                       "Dívida Fiscal Líquida, utilizando o critério conhecido como “") + vm("acima") + az(" da "
                       "linha”.")),
        "poucas": ("Medir o resultado pela variação da dívida é o critério " + azb("abaixo da linha")
                   + " (Banco Central). “Acima da linha” é o cotejo de receitas e despesas (Tesouro)."),
        "destrinchando": [
            "A imagem vem da demonstração contábil em que uma linha separa os fluxos de receitas e despesas "
            "(em cima) das fontes de financiamento (embaixo). O saldo de cima tem de ser igual ao financiamento "
            "de baixo.",
            azb("Acima da linha") + ": soma receitas e subtrai despesas, item a item — é como a "
            + rx("Secretaria do Tesouro Nacional") + " apura o resultado do governo central. Mostra a "
            "<b>composição</b> do resultado (onde se gastou, o que se arrecadou).",
            azb("Abaixo da linha") + ": olha quanto a dívida líquida variou, descontados os ajustes patrimoniais "
            "e metodológicos — é a " + azb("dívida fiscal líquida") + ". É como o " + rx("Banco Central")
            + " calcula as NFSP. Mostra o <b>tamanho</b> do resultado, sem detalhar sua origem.",
            "Em tese os dois coincidem; na prática diferem por defasagens de registro e lançamentos, e a diferença "
            "aparece como " + azb("discrepância estatística") + ". O resultado oficial para aferir as metas "
            "fiscais tem sido o do Banco Central.",
            vm("Regra-âncora: variação de dívida = abaixo da linha = BC; receita − despesa = acima da linha = "
               "Tesouro."),
        ],
        "dissecando": (cz("[troca de conceito]") + " A primeira parte do item é a definição exata das NFSP; o "
                       "erro está só no rótulo do critério, trocado pelo vizinho. Pista: “a partir da variação da "
                       "dívida” já descreve o lado do financiamento, isto é, abaixo da linha."),
        "modulos": [("🧠 Mnemônico", ["<b>Abaixo</b> fica o que <b>banca</b> o déficit (dívida, BC); "
                                      "<b>acima</b>, a conta de <b>arrecadação</b> e gasto (Tesouro)."])],
        "reescrita": ("As Necessidades de Financiamento do Setor Público são calculadas a partir da variação da "
                      "Dívida Fiscal Líquida, utilizando o critério conhecido como “" + hl("abaixo") + " da linha”."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "NFSP nominal = variação da dívida fiscal líquida; método abaixo da linha.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01517
    {
        "id": "ECO-E2-L01517-1", "fonte_ref": "E2-L01517", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_FISC,
        "rotulo_item": "Item",
        "assertiva": ("O resultado primário do setor público, por não incluir o pagamento de juros sobre a dívida "
                      "pública, não reflete o crescimento do estoque da dívida, o que é feito pelo conceito de "
                      "resultado nominal."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O resultado primário do setor público, por <u>não incluir o pagamento de juros</u> sobre a "
                      "dívida pública, não reflete o crescimento do estoque da dívida, o que é feito pelo conceito "
                      "de <u>resultado nominal</u>."),
        "poucas": ("A dívida cresce pelo " + azb("déficit nominal") + " (primário + juros). O primário deixa de "
                   "fora os juros e, por isso, mostra o esforço fiscal, não a variação do endividamento."),
        "destrinchando": [
            azb("Resultado primário") + " = receitas não financeiras − despesas não financeiras. Mede o que o "
            "governo controla no ano (arrecadação, custeio, investimento, benefícios) e é a base das metas fiscais "
            "brasileiras.",
            azb("Resultado nominal") + " = primário − juros nominais. Um déficit nominal precisa ser financiado: "
            "é a " + azb("NFSP") + ", que corresponde ao acréscimo da dívida fiscal líquida no período.",
            "Consequência clássica: superávit primário com déficit nominal. Foi o padrão do " + rx("Brasil")
            + " entre 1999 e 2008 — primários acima de " + vd("3% do PIB") + " e, mesmo assim, déficits "
            "nominais, porque a conta de juros era maior.",
            "O primário importa para a dívida, mas como <b>componente</b>: a dívida/PIB se estabiliza quando o "
            "primário cobre o diferencial entre juros reais e crescimento, " + vd("s* = d·(r − g)/(1 + g)")
            + ". Sozinho, porém, ele não diz quanto a dívida variou.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item é a definição comentada dos dois conceitos. A armadilha "
                       "é o “não reflete”: quem lembra que o primário <b>afeta</b> a dívida pode achar o item "
                       "absoluto demais. Mas “refletir o crescimento do estoque” é medir a variação toda — tarefa "
                       "do nominal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um superávit primário garante a redução do estoque da dívida pública.”</i> → ERRADO (os juros "
            "podem superá-lo e gerar déficit nominal)",
            "<i>“É possível que o setor público registre superávit primário e, simultaneamente, déficit "
            "nominal.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O primário exclui juros e mede o esforço fiscal; o nominal (primário menos juros) "
                            "reflete a variação da dívida e corresponde às NFSP.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01519
    {
        "id": "ECO-E2-L01519-1", "fonte_ref": "E2-L01519", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_FISC,
        "rotulo_item": "Item",
        "assertiva": ("O resultado fiscal acima da linha, calculado pelo Tesouro Nacional por meio do saldo de "
                      "receitas e despesas, não reflete adequadamente a evolução do endividamento do governo, "
                      "melhor captado pelo resultado abaixo da linha, calculado pelo Banco Central, que calcula o "
                      "resultado pela variação do estoque da dívida pública."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O resultado fiscal acima da linha, calculado pelo Tesouro Nacional por meio do saldo de "
                      "receitas e despesas, <u>não reflete adequadamente</u> a evolução do endividamento do governo, "
                      "melhor captado pelo resultado <u>abaixo da linha</u>, calculado pelo Banco Central, que "
                      "calcula o resultado pela variação do estoque da dívida pública."),
        "poucas": ("Quem mede a dívida mede o endividamento: o resultado " + azb("abaixo da linha") + " (Banco "
                   "Central) parte da variação da dívida; o " + azb("acima da linha") + " (Tesouro) soma fluxos "
                   "de receita e despesa e pode não bater com ela."),
        "destrinchando": [
            "<b>Acima da linha</b> (" + rx("Tesouro Nacional") + "): receita − despesa, linha a linha. Vantagem: "
            "mostra a <b>composição</b> do resultado — onde se arrecadou e onde se gastou. Limite: depende do "
            "registro correto e tempestivo de cada fluxo.",
            "<b>Abaixo da linha</b> (" + rx("Banco Central") + "): quanto o setor público precisou se financiar, "
            "medido pela variação da " + azb("dívida fiscal líquida") + " (a DLSP sem ajustes patrimoniais e "
            "metodológicos). Vantagem: captura todo fluxo que efetivamente gerou dívida, inclusive o que escapou "
            "do registro orçamentário. É a base das " + azb("NFSP") + " e da aferição das metas.",
            "A diferença entre as duas apurações aparece como " + azb("discrepância estatística") + ": defasagens "
            "de registro, diferenças de cobertura (estatais, entes subnacionais) e operações que não transitam "
            "pela despesa. Discrepância grande e persistente é sinal de registro incompleto acima da linha.",
            "Nuance: a variação <b>bruta</b> da DLSP inclui câmbio, privatizações e reconhecimento de esqueletos; "
            "por isso o BC usa a dívida fiscal líquida para chegar ao resultado do período.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item compara as duas óticas e atribui cada uma ao órgão "
                       "certo. Quem conhece o primário do Tesouro como “a” referência fiscal tende a marcar ERRADO; "
                       "mas o item fala de <b>endividamento</b>, e para isso a ótica do financiamento é a "
                       "adequada. 🔥 A banca também cobra a versão invertida (“o acima da linha reflete mais "
                       "precisamente a dívida”), que é ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado acima da linha permite identificar a composição do resultado fiscal, o que o abaixo "
            "da linha não oferece.”</i> → CERTO",
            "<i>“O Banco Central calcula as NFSP pelo critério acima da linha.”</i> → ERRADO (critério trocado: "
            "abaixo da linha)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": "Acima da linha (Tesouro) = receitas − despesas; abaixo da linha (BC) = variação da "
                            "dívida líquida, mais abrangente e precisa para medir o endividamento, captando "
                            "esqueletos e passivos não registrados no orçamento.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L01777 (mesmo item, sem a oração final “que calcula o resultado pela variação do "
                    "estoque da dívida pública”) fundido neste card"],
    },
    # ------------------------------------------------------------------ E2-L01634
    {
        "id": "ECO-E2-L01634-1", "fonte_ref": "E2-L01634", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_FISC,
        "rotulo_item": "Item",
        "assertiva": ("O resultado fiscal acima da linha, calculado pelo Tesouro Nacional por meio do saldo de "
                      "receitas e despesas, é o que reflete mais precisamente a evolução da dívida pública, se "
                      "comparado ao resultado abaixo da linha, calculado pelo Banco Central."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O resultado fiscal acima da linha, calculado pelo Tesouro Nacional por meio do saldo de "
                       "receitas e despesas, ") + vm("é o que reflete mais precisamente") + az(" a evolução da "
                       "dívida pública, se comparado ao resultado abaixo da linha, calculado pelo Banco Central.")),
        "poucas": ("É o contrário: o resultado " + azb("abaixo da linha") + " é calculado <b>a partir</b> da "
                   "variação da dívida e, por construção, é o que melhor reflete a sua evolução."),
        "destrinchando": [
            azb("Acima da linha") + " (" + rx("Tesouro") + "): fluxo de receitas menos despesas. Mede o esforço "
            "fiscal e mostra a composição do resultado, mas só enxerga o que foi registrado como receita ou "
            "despesa.",
            azb("Abaixo da linha") + " (" + rx("Banco Central") + "): variação da " + azb("dívida fiscal líquida")
            + ", isto é, quanto o setor público efetivamente se financiou. É a base das NFSP e capta também o que "
            "não passou pelo orçamento — atrasos de pagamento a bancos públicos, passivos reconhecidos, "
            "operações de estatais.",
            "As duas apurações deveriam coincidir; a diferença (" + azb("discrepância estatística") + ") revela "
            "defasagens de registro ou operações “fora do orçamento”.",
            "Para ir do resultado à dívida total ainda faltam os " + azb("ajustes patrimoniais") + " (câmbio, "
            "privatizações, esqueletos), que mexem na DLSP sem ser déficit do período.",
            vm("Regra-âncora: para acompanhar a dívida, use a ótica do financiamento (abaixo da linha)."),
        ],
        "dissecando": (cz("[inversão]") + " O item atribui ao acima da linha a virtude do abaixo da linha. A "
                       "descrição de cada método está certa; o erro está no juízo comparativo “mais "
                       "precisamente”. Pista: o método que <b>parte</b> da dívida não pode refleti-la pior do que "
                       "um que a infere pelos fluxos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado acima da linha não reflete adequadamente a evolução do endividamento, melhor captado "
            "pelo resultado abaixo da linha.”</i> → CERTO",
            "<i>“Os resultados acima e abaixo da linha são idênticos por definição, sem discrepância.”</i> → "
            "ERRADO (na prática há discrepância estatística)",
        ])],
        "reescrita": ("O resultado fiscal acima da linha, calculado pelo Tesouro Nacional por meio do saldo de "
                      "receitas e despesas, " + hl("reflete com menos precisão") + " a evolução da dívida pública, "
                      "se comparado ao resultado abaixo da linha, calculado pelo Banco Central."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["mais precisamente"], "dificuldade": 1,
        "comentario_fonte": "O abaixo da linha (variação da dívida) reflete melhor a evolução do estoque; o acima da "
                            "linha é fluxo (receitas − despesas) e não capta ajustes, esqueletos e câmbio.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00207
    {
        "id": "ECO-E3-L00207-1", "fonte_ref": "E3-L00207", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Abril/2025", "ano": 2025,
        "cacd": False, "errei": False,
        "comando": "Acerca dos indicadores orçamentários do setor público, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O déficit primário do setor público é igual ao déficit nominal menos os juros nominais pagos "
                      "sobre a dívida pública."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O déficit primário do setor público é igual ao déficit nominal menos os juros "
                      "<u>nominais</u> pagos sobre a dívida pública."),
        "poucas": ("Identidade de base: " + vd("déficit nominal = déficit primário + juros nominais") + ". Isolando "
                   "o primário, chega-se exatamente à frase do item."),
        "destrinchando": [
            azb("Resultado primário") + ": receitas menos despesas <b>não financeiras</b> (pessoal, custeio, "
            "investimento, benefícios). Mede o esforço fiscal corrente, sem o custo da dívida herdada.",
            azb("Resultado nominal") + ": primário mais a conta de juros nominais (líquidos dos juros recebidos). "
            "É o que precisa ser financiado no período — as " + azb("NFSP") + " — e o que faz a dívida variar.",
            "Exemplo: déficit nominal de " + vd("100") + " com juros de " + vd("60") + " → déficit primário de "
            + vd("40") + ". Se o nominal fosse 20 com os mesmos juros, o primário seria −40, isto é, "
            "<b>superávit</b> primário de 40 insuficiente para cobrir os juros.",
            "No " + rx("Brasil") + ", essa separação ganhou peso a partir de 1999, quando as metas fiscais passaram "
            "a ser de superávit primário: o governo controla receitas e gastos primários, mas não a Selic que "
            "move a conta de juros.",
            "Terceiro degrau: o " + azb("operacional") + " = primário + juros <b>reais</b>, útil com inflação alta, "
            "porque retira a mera correção monetária da dívida.",
        ],
        "dissecando": (cz("[literalidade]") + " É a identidade contábil reescrita com a subtração. A dificuldade é "
                       "só de sinal: com “déficit” positivo, primário = nominal − juros; com “resultado” (superávit "
                       "positivo), resultado nominal = primário − juros. A banca troca “nominais” por “reais” para "
                       "fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O déficit primário é igual ao déficit nominal menos os juros reais.”</i> → ERRADO (assim se "
            "obtém o operacional, não o primário)",
            "<i>“O déficit operacional é igual ao déficit primário mais os juros reais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Nominal = primário + juros; o primário exclui o custo financeiro da dívida. Os "
                            "comentários de IA da fonte rotulam o primário como “acima da linha” e o nominal como "
                            "“abaixo da linha”, o que confunde conceito com critério de apuração.",
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 289-292", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (fórmulas e quadro-resumo no 📖)"}],
        "alertas": ["qualidade_fonte: o verso associa primário a “acima da linha” e nominal a “abaixo da linha”; "
                    "acima/abaixo da linha são critérios de apuração (Tesouro × BC), não conceitos de resultado. "
                    "Também atribui ao primário a função de limpar a inflação, que é do conceito operacional"],
    },
    # ------------------------------------------------------------------ E3-L00383
    {
        "id": "ECO-E3-L00383-1", "fonte_ref": "E3-L00383", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Novembro/2024", "ano": 2024,
        "cacd": False, "errei": False,
        "comando": ("A análise das contas públicas é um elemento importante da macroeconomia. A esse respeito, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O conceito de dívida líquida acima da linha representa o cotejo das receitas e despesas "
                      "primárias, isto é, os recursos associados às funções econômicas do Estado, tais como definidas "
                      "na Constituição Federal de 1988 e sem incluir receitas e despesas financeiras associadas ao "
                      "estoque de dívida pública."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O conceito de <u>dívida líquida acima da linha</u> representa o cotejo das receitas e "
                      "despesas primárias, isto é, os recursos associados às funções econômicas do Estado, tais como "
                      "definidas na Constituição Federal de 1988 e <u>sem incluir receitas e despesas "
                      "financeiras</u> associadas ao estoque de dívida pública."),
        "poucas": ("O que o item descreve é o " + azb("resultado primário apurado acima da linha") + ": receitas "
                   "menos despesas não financeiras, sem os juros. O conteúdo está certo; o rótulo “dívida "
                   "líquida” é impróprio."),
        "condicionais": [("⚠️ Gabarito contestável",
                          azb("Dívida líquida") + " é <b>estoque</b> (passivos menos ativos financeiros) e se mede "
                          "<b>abaixo</b> da linha; “acima da linha” é critério de apuração de <b>fluxos</b>. Rigor "
                          "terminológico levaria ao ERRADO. O gabarito CERTO se sustenta pela descrição, que é a do "
                          "resultado primário; o examinador parece ter usado “dívida líquida” como atalho para o "
                          "resultado fiscal.")],
        "destrinchando": [
            azb("Acima da linha") + " (" + rx("Tesouro Nacional") + "): cotejo direto de receitas e despesas. No "
            "conceito primário, ficam de fora as receitas e despesas financeiras — juros pagos e recebidos, "
            "amortizações —, e o saldo mostra se a arrecadação cobre os gastos com as funções do Estado (saúde, "
            "educação, previdência, infraestrutura).",
            azb("Abaixo da linha") + " (" + rx("Banco Central") + "): variação da dívida fiscal líquida no "
            "período, isto é, o financiamento. É assim que se apuram as NFSP.",
            azb("DLSP") + " = dívida bruta do setor público não financeiro e do BC menos seus ativos financeiros "
            "(reservas, créditos com bancos públicos, disponibilidades). É uma fotografia em uma data; o "
            "resultado fiscal é o filme que a altera.",
            "A ponte entre os dois mundos: " + vd("Δ DLSP ≈ NFSP nominal + ajustes patrimoniais e "
            "metodológicos") + " (câmbio, privatizações, reconhecimento de passivos).",
            "Ao excluir os juros, o primário isola o que o governo decide no ano; os juros dependem da Selic e do "
            "estoque herdado. Por isso a meta fiscal brasileira é de resultado primário.",
        ],
        "dissecando": (cz("[paráfrase fiel · detalhe]") + " A descrição é a do resultado primário; o item embrulha "
                       "o conceito num rótulo híbrido (“dívida líquida acima da linha”) que mistura estoque com "
                       "critério de fluxo. Em prova, se o restante da frase descreve com exatidão o primário, a "
                       "banca tende a manter o CERTO; se o rótulo fosse o centro do item, o julgamento mudaria."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O resultado primário apurado acima da linha exclui as receitas e despesas financeiras "
            "associadas ao estoque da dívida.”</i> → CERTO",
            "<i>“A dívida líquida do setor público é uma variável de fluxo, apurada pelo Tesouro Nacional.”</i> → "
            "ERRADO (é estoque, apurado pelo Banco Central)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "DETALHE"], "moduladores": [], "dificuldade": 3,
        "comentario_fonte": "Gabarito CERTO: o acima da linha é o cotejo de receitas e despesas primárias, sem juros. "
                            "As respostas de IA do verso apontam a imprecisão de “dívida líquida acima da linha” "
                            "(dívida é estoque, apurado abaixo da linha).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 556-558", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (quadros acima × abaixo da linha no 📖)"}],
        "alertas": ["contestavel: “dívida líquida acima da linha” mistura estoque (dívida) com critério de apuração "
                    "de fluxo; a descrição é a do resultado primário. Gabarito CERTO da fonte mantido"],
    },
    # ------------------------------------------------------------------ E3-L00457
    {
        "id": "ECO-E3-L00457-1", "fonte_ref": "E3-L00457", "destino": "19", "subtema": H2["nfsp"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Com relação ao papel historicamente desempenhado pelo Estado na economia brasileira, julgue o "
                    "item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Metas de superávit nominal das contas públicas foram estabelecidas, a partir de 1999, com o "
                      "objetivo de estabilizar ou reduzir a razão da dívida pública em relação ao Produto Interno "
                      "Bruto (Dívida pública/PIB)."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Metas de superávit ") + vm("nominal") + az(" das contas públicas foram estabelecidas, a "
                       "partir de 1999, com o objetivo de estabilizar ou reduzir a razão da dívida pública em "
                       "relação ao Produto Interno Bruto (Dívida pública/PIB).")),
        "poucas": ("A âncora fiscal criada em 1999 foi a meta de " + azb("superávit primário") + " (antes dos "
                   "juros), não nominal. O objetivo — estabilizar a dívida/PIB — está correto."),
        "destrinchando": [
            "Contexto: após a crise russa (1998), o " + rx("Brasil") + " fechou acordo com o " + azb("FMI")
            + " no fim de 1998 e, em janeiro de 1999, abandonou a âncora cambial. O novo regime ficou conhecido "
            "como " + azb("tripé macroeconômico") + ": câmbio flutuante (jan/1999), metas de inflação (jun/1999) e "
            "metas de " + vd("superávit primário") + " (a partir de 1999, da ordem de 3% do PIB).",
            "Por que primário: é a parte do resultado que o governo controla com receitas e gastos. A conta de "
            "juros depende da Selic e do estoque herdado — em 1999, com juros altíssimos, um superávit "
            "<b>nominal</b> seria inalcançável.",
            "Por que estabiliza a dívida: a relação d = dívida/PIB evolui como " + vd("Δd ≈ (r − g)·d − s")
            + ", com s = superávit primário/PIB. Basta s cobrir o diferencial juros reais − crescimento para d "
            "parar de subir.",
            "A " + azb("Lei de Responsabilidade Fiscal") + " (" + vd("LC 101/2000") + ") institucionalizou o "
            "regime: o Anexo de Metas Fiscais da LDO traz metas de resultado primário <b>e</b> nominal e de dívida, "
            "mas a meta efetivamente perseguida e cobrada sempre foi a do primário.",
            "⏳ (out/2026) O primário continua sendo a variável-meta no regime fiscal sustentável de 2023 "
            "(LC 200/2023), combinado com um limite de crescimento real das despesas.",
        ],
        "dissecando": (cz("[troca de conceito]") + " Uma palavra: “nominal” no lugar de “primário”. Data (1999) e "
                       "objetivo (dívida/PIB) estão certos, o que dá credibilidade à frase. 🔥 Tripé de 1999 é "
                       "tema recorrente; a banca troca o tipo de meta fiscal ou a data das metas de inflação."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A partir de 1999, a política fiscal brasileira passou a ser ancorada em metas de superávit "
            "primário, compondo o tripé com o câmbio flutuante e as metas de inflação.”</i> → CERTO",
            "<i>“As metas de superávit primário foram introduzidas pela LRF em 2000.”</i> → ERRADO (já vigoravam "
            "desde 1999, com o acordo com o FMI; a LRF as institucionalizou)",
        ])],
        "reescrita": ("Metas de superávit " + hl("primário") + " das contas públicas foram estabelecidas, a partir de "
                      "1999, com o objetivo de estabilizar ou reduzir a razão da dívida pública em relação ao "
                      "Produto Interno Bruto (Dívida pública/PIB)."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "As metas de 1999 (acordo com o FMI, tripé) foram de superávit primário, não nominal; "
                            "superávit nominal com juros altíssimos seria irreal.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 662", "tipo_fonte": "TEXTO", "lado": "verso",
                           "acao": "absorvida (tripé e definições no 📖)"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0315
    {
        "id": "ECO-E1-0315-1", "fonte_ref": "E1-0315", "destino": "25", "subtema": H2["tqm"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2020, "cacd": False, "errei": False,
        "comando": "Julgue o item a seguir, relativo à teoria quantitativa da moeda.",
        "rotulo_item": "Item",
        "assertiva": ("Sob as premissas da Teoria Quantitativa da Moeda, a moeda é apenas meio de troca, de modo "
                      "que não há interdependência entre o mercado monetário e o mercado de bens e serviços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Sob as premissas da Teoria Quantitativa da Moeda, a moeda é <u>apenas meio de troca</u>, de "
                      "modo que não há interdependência entre o mercado monetário e o mercado de bens e serviços."),
        "poucas": ("Na " + azb("TQM") + " a moeda só serve para transacionar: ninguém a retém como reserva de "
                   "valor. Ela fixa o nível de preços, mas não afeta produto, emprego nem juros — é a "
                   + azb("dicotomia clássica") + "."),
        "destrinchando": [
            "Equação de trocas de " + oc("Irving Fisher") + ": " + vd("MV = PY") + ". Com V fixada por hábitos e "
            "instituições de pagamento e Y fixado no pleno emprego pelo lado real, M determina P.",
            "Se a moeda é só meio de troca, demanda-se moeda na proporção das transações (versão de Cambridge: "
            "M = kPY, com k = 1/V). Não há " + azb("demanda especulativa") + ": a demanda por moeda não depende "
            "dos juros.",
            "Daí a separação: o lado real (produção, mercado de trabalho, fundos emprestáveis) determina Y, "
            "emprego, salário real e juros reais; o lado monetário só converte tudo em preços nominais. Moeda é "
            "um “véu” — " + azb("neutralidade da moeda") + ".",
            "Quem quebra a separação é " + oc("Keynes") + ": com a " + azb("preferência pela liquidez") + ", a "
            "moeda vira reserva de valor, a demanda por moeda passa a depender dos juros, e o mercado monetário "
            "interfere no de bens via taxa de juros (o IS-LM é justamente essa interdependência).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item une a premissa (moeda só como meio de troca) à "
                       "consequência (dicotomia). O “apenas” e o “não há interdependência” soam absolutos, mas "
                       "estão corretos <b>dentro</b> das premissas da TQM, que o item delimita logo no início."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Sob a TQM, a demanda por moeda depende inversamente da taxa de juros.”</i> → ERRADO (troca de "
            "escola: é a preferência pela liquidez keynesiana)",
            "<i>“Na TQM, a velocidade de circulação é estável, e variações de M afetam apenas o nível de "
            "preços.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": "Na TQM a moeda é meio de troca, sem valor intrínseco; não há motivo para retê-la como "
                            "bem em si.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0446
    {
        "id": "ECO-E1-0446-1", "fonte_ref": "E1-0446", "destino": "25", "subtema": H2["tqm"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Clipping", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("A política monetária moderna combina instrumentos de controle da oferta de moeda com metas de "
                    "inflação, buscando estabilidade econômica. Com base nesse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A teoria quantitativa da moeda, em sua versão clássica, assume que a velocidade de "
                      "circulação da moeda é constante, implicando que aumentos na oferta monetária resultam "
                      "proporcionalmente em aumento do nível de preços."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria quantitativa da moeda, em sua <u>versão clássica</u>, assume que a velocidade de "
                      "circulação da moeda é constante, implicando que aumentos na oferta monetária resultam "
                      "<u>proporcionalmente</u> em aumento do nível de preços."),
        "poucas": ("Em " + vd("MV = PY") + ", com V constante e Y no pleno emprego, P varia na mesma proporção que "
                   "M: dobrar a moeda dobra os preços."),
        "destrinchando": [
            "Em taxas de variação: " + vd("%ΔM + %ΔV = %ΔP + %ΔY") + ". Com %ΔV = 0 e %ΔY dado pelo lado real, "
            "%ΔP = %ΔM − %ΔY. Se o produto não cresce, a inflação é igual à expansão monetária.",
            "Duas hipóteses sustentam a proporcionalidade: " + azb("V estável") + " (depende de hábitos de "
            "pagamento e do sistema financeiro, que mudam devagar) e " + azb("Y independente da moeda") + " (fixado "
            "por trabalho, capital e tecnologia — dicotomia clássica).",
            "Consequência: " + azb("neutralidade da moeda") + " e a máxima de " + oc("Milton Friedman") + ", "
            "“a inflação é sempre e em toda parte um fenômeno monetário”. O monetarismo relaxou a hipótese: V não "
            "precisa ser constante, basta ser previsível.",
            "Na prática, a velocidade se mostrou instável a partir dos anos 1980 (inovação financeira), o que "
            "levou os bancos centrais a abandonar metas de agregados monetários e adotar " + azb("metas de "
            "inflação") + " com a taxa de juros como instrumento — o " + rx("Brasil") + " adotou o regime em 1999.",
        ],
        "dissecando": (cz("[literalidade]") + " Item de manual. A palavra de risco é “proporcionalmente”, que só "
                       "vale com V e Y constantes; o item dá a hipótese de V e o “versão clássica” garante a de Y. "
                       "🔥 A banca costuma inverter: “a TQM supõe velocidade variável” ou “a moeda afeta o produto "
                       "no longo prazo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na versão clássica da TQM, um aumento de 10% da oferta monetária eleva o produto real em "
            "10%.”</i> → ERRADO (troca de variável: eleva P, não Y)",
            "<i>“Se a velocidade da moeda cair na mesma proporção em que M aumenta, o nível de preços fica "
            "inalterado.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["proporcionalmente"], "dificuldade": 1,
        "comentario_fonte": "MV = PY; na versão clássica V e Y são constantes, e a variação de M gera variação "
                            "proporcional de P.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E1-0548 (mesmo item e mesmo comentário) fundido neste card"],
    },
    # ------------------------------------------------------------------ E1-0462
    {
        "id": "ECO-E1-0462-1", "fonte_ref": "E1-0462", "destino": "25", "subtema": H2["tqm"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 5", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_CLA,
        "rotulo_item": "Item",
        "assertiva": ("A teoria quantitativa da moeda representa o lado monetário, que não tem qualquer conexão com "
                      "o lado real da economia, o que é conhecido como dicotomia clássica."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A teoria quantitativa da moeda representa o lado monetário, que <u>não tem qualquer "
                      "conexão</u> com o lado real da economia, o que é conhecido como dicotomia clássica."),
        "poucas": ("No modelo clássico, o " + azb("lado real") + " determina produto, emprego, salário real e "
                   "juros; a " + azb("TQM") + " só determina o nível de preços. Essa separação é a "
                   + azb("dicotomia clássica") + "."),
        "destrinchando": [
            "Lado real, em sequência: o mercado de trabalho (com salários flexíveis) fixa emprego e salário real; "
            "a função de produção dá o produto de pleno emprego; os fundos emprestáveis (poupança × investimento) "
            "fixam a taxa de juros real e a composição do produto.",
            "Lado monetário: " + vd("MV = PY") + ". Com Y já dado e V estável, a oferta de moeda determina P. "
            "Funciona como a " + azb("demanda agregada") + " do modelo: uma hipérbole PY = MV, que, cruzada com a "
            "oferta agregada vertical, só move preços.",
            "Consequência: " + azb("neutralidade da moeda") + " — mais moeda eleva P e salários nominais na "
            "mesma proporção, sem alterar nenhuma variável real.",
            "Contraponto: " + oc("Keynes") + " rompe a dicotomia com a " + azb("preferência pela liquidez")
            + " (juros determinados no mercado monetário) e com a rigidez de salários nominais; nesse caso, a "
            "moeda afeta juros, investimento e produto.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O “não tem qualquer conexão” parece absoluto demais, mas é a "
                       "definição exata da dicotomia: dentro do modelo clássico, a separação é total. Absolutos "
                       "que descrevem a hipótese de um modelo nomeado costumam ser CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, a taxa de juros é determinada pela oferta e pela demanda de moeda.”</i> → "
            "ERRADO (troca de escola: é a visão de Keynes; nos clássicos, poupança × investimento)",
            "<i>“A dicotomia clássica implica a neutralidade da moeda.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["qualquer"], "dificuldade": 1,
        "comentario_fonte": "Para os clássicos, o lado monetário é separado do real; a TQM representa o lado "
                            "monetário (e da demanda).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0390
    {
        "id": "ECO-E1-0390-1", "fonte_ref": "E1-0390", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 2", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_FE,
        "rotulo_item": "Item",
        "assertiva": ("A redução do imposto de renda sobre aplicações financeiras teria como efeito a elevação da "
                      "poupança e, consequentemente, do investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A redução do imposto de renda sobre <u>aplicações financeiras</u> teria como efeito a "
                      "elevação da poupança e, consequentemente, do investimento."),
        "poucas": ("Menos imposto sobre o rendimento eleva o retorno líquido de poupar: a " + azb("oferta de fundos")
                   + " se desloca para a direita, os juros caem e poupança e investimento sobem."),
        "destrinchando": [
            "No " + azb("mercado de fundos emprestáveis") + ", a oferta vem da poupança (cresce com o juro real) e "
            "a demanda vem do investimento (cai com o juro real). O equilíbrio fixa o juro real e o volume de "
            "fundos, com " + vd("S = I") + ".",
            "Tributar aplicações financeiras reduz o rendimento que o poupador efetivamente recebe. Cortar esse "
            "imposto aumenta a poupança a <b>cada</b> taxa de juros de mercado: a curva de oferta se desloca para "
            "a direita.",
            "Novo equilíbrio: " + vd("r ↓") + " e " + vd("F ↑") + ". O investimento sobe ao longo da curva de "
            "demanda, porque o crédito ficou mais barato — por isso o “consequentemente”.",
            "Ressalva de manual (" + oc("Mankiw") + "): o efeito sobre a poupança supõe que o " + azb("efeito "
            "substituição") + " (poupar rende mais, vale adiar consumo) supere o " + azb("efeito renda") + " (com "
            "mais rendimento, alcança-se a mesma meta poupando menos). A evidência é controversa, mas o modelo "
            "padrão adota a oferta crescente.",
            "Contraste: um incentivo fiscal ao <b>investimento</b> desloca a demanda, e aí os juros sobem.",
        ],
        "grafico_verso": "ECO-E1-0390-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " Item de mecanismo: identificar qual curva se move. Imposto sobre "
                       "o rendimento da poupança mexe na <b>oferta</b>; o “consequentemente” é movimento ao longo "
                       "da demanda. O condicional “teria” deixa o item no plano do modelo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução do imposto sobre aplicações financeiras elevaria a taxa de juros de equilíbrio.”</i> "
            "→ ERRADO (inversão: oferta à direita derruba os juros)",
            "<i>“Um crédito tributário ao investimento elevaria a taxa de juros e a quantidade de fundos "
            "emprestados.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["teria"], "dificuldade": 1,
        "comentario_fonte": "Gabarito CERTO; o verso trazia só um gráfico (não preservado).",
        "qualidade_fonte": "ausente",
        "figuras_fonte": FIG_E1("image (135).png"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0391
    {
        "id": "ECO-E1-0391-1", "fonte_ref": "E1-0391", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 2", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_FE,
        "rotulo_item": "Item",
        "assertiva": ("Um ajuste fiscal, por meio da redução do gasto público, teria como efeito a redução da taxa de "
                      "juros e também do investimento, e portanto não seria uma boa opção para tirar a economia de "
                      "uma recessão."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um ajuste fiscal, por meio da redução do gasto público, teria como efeito a redução da taxa "
                       "de juros e ") + vm("também") + az(" do investimento") + vm(", e portanto não seria uma boa "
                       "opção para tirar a economia de uma recessão") + az(".")),
        "poucas": ("Cortar gasto eleva a " + azb("poupança pública") + ": a oferta de fundos vai para a direita, os "
                   "juros caem e o investimento <b>sobe</b> — é o crowding out ao contrário."),
        "destrinchando": [
            "Poupança nacional = poupança privada + " + azb("poupança pública") + " (T − G). Reduzir G, com T "
            "dado, diminui o déficit (ou amplia o superávit) e aumenta a poupança nacional.",
            "No " + azb("mercado de fundos emprestáveis") + ", isso desloca a oferta para a direita: " + vd("r ↓")
            + " e " + vd("I ↑") + ". O investimento privado ocupa o espaço que o governo deixou de tomar — o "
            "chamado " + azb("crowding in") + ".",
            "O item acerta a queda dos juros, mas erra o investimento: com crédito mais barato e a demanda por "
            "investimento parada, a quantidade investida só pode subir.",
            "A conclusão também cai. No modelo clássico de fundos emprestáveis, a economia está no pleno emprego "
            "e o ajuste muda a <b>composição</b> do produto (menos G, mais I), favorecendo o crescimento futuro. "
            "A objeção a ajustes em recessão vem de outro arcabouço — o " + oc("keynesiano") + ", em que o corte de "
            "G reduz a demanda agregada pelo multiplicador —, não do argumento de que o investimento cairia.",
            vm("Regra-âncora: déficit maior → juros sobem e I cai (crowding out); ajuste fiscal → juros caem e I "
               "sobe."),
        ],
        "grafico_verso": "ECO-E1-0391-1-V1",
        "dissecando": (cz("[meia-verdade · nexo indevido]") + " Começa certo (juros caem) e enxerta o erro no "
                       "“também”, que arrasta o investimento junto. A conclusão sobre a recessão é tirada da "
                       "premissa falsa. Pista: no mesmo mercado, preço e quantidade do crédito só caem juntos se "
                       "a <b>demanda</b> se desloca — e o ajuste mexe na oferta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um ajuste fiscal, por meio da redução do gasto público, reduziria a taxa de juros e elevaria o "
            "investimento privado.”</i> → CERTO",
            "<i>“Um aumento do déficit público desloca para a esquerda a demanda por fundos emprestáveis.”</i> → "
            "ERRADO (curva trocada: reduz a oferta de fundos)",
        ])],
        "reescrita": ("Um ajuste fiscal, por meio da redução do gasto público, teria como efeito a redução da taxa de "
                      "juros e " + hl("o aumento") + " do investimento<s>, e portanto não seria uma boa opção para "
                      "tirar a economia de uma recessão</s>."),
        "tipo_erro": ["MEIA_VERDADE", "NEXO_INDEVIDO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "O investimento iria aumentar (o verso trazia ainda um gráfico, não preservado).",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("image (137).png"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0392
    {
        "id": "ECO-E1-0392-1", "fonte_ref": "E1-0392", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 2", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_FE,
        "rotulo_item": "Item",
        "assertiva": ("Uma desoneração fiscal na compra de bens de capital deslocaria para baixo e para esquerda a "
                      "curva de demanda por fundos emprestáveis, levando a uma redução dos juros e aumento dos "
                      "investimentos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma desoneração fiscal na compra de bens de capital deslocaria para ")
                    + vm("baixo e para esquerda") + az(" a curva de demanda por fundos emprestáveis, levando a ")
                    + vm("uma redução") + az(" dos juros e aumento dos investimentos.")),
        "poucas": ("Investir fica mais barato e rentável: a " + azb("demanda por fundos") + " vai para cima e para a "
                   "direita. Os juros <b>sobem</b> e o investimento aumenta."),
        "destrinchando": [
            "A demanda por fundos emprestáveis é a demanda por investimento: cada ponto mostra quanto as firmas "
            "querem tomar emprestado a cada juro real. Ela se desloca quando muda a rentabilidade esperada dos "
            "projetos.",
            "Uma desoneração (crédito tributário, depreciação acelerada, isenção de IPI sobre máquinas) reduz o "
            "custo do bem de capital e eleva o retorno líquido de cada projeto. Mais projetos passam a valer a "
            "pena a qualquer juro: a curva se desloca para a <b>direita</b>.",
            "Novo equilíbrio: " + vd("r ↑") + " (as firmas disputam a poupança disponível) e " + vd("F ↑")
            + " (mais poupança atraída pelo juro maior). Poupança e investimento sobem juntos.",
            "Compare com o incentivo à <b>poupança</b> (menos imposto sobre aplicações): ali se move a oferta, e os "
            "juros caem. Saber qual curva o incentivo atinge decide o sinal dos juros.",
            "O item acerta o objetivo da política (mais investimento), mas erra a direção da curva e, com ela, o "
            "efeito sobre os juros.",
        ],
        "grafico_verso": "ECO-E1-0392-1-V1",
        "dissecando": (cz("[inversão]") + " O item inverte o deslocamento e, por coerência, os juros; só o "
                       "investimento sobrevive certo. Armadilha: associar “desoneração” a “custo menor” e daí a "
                       "“curva para baixo”. Custo menor do bem de capital significa <b>mais</b> demanda por fundos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um crédito tributário ao investimento eleva a taxa de juros real e a quantidade de poupança e "
            "investimento.”</i> → CERTO",
            "<i>“Uma desoneração na compra de bens de capital deslocaria a oferta de fundos para a direita.”</i> → "
            "ERRADO (curva trocada: é a demanda)",
        ])],
        "reescrita": ("Uma desoneração fiscal na compra de bens de capital deslocaria para "
                      + hl("cima e para a direita") + " a curva de demanda por fundos emprestáveis, levando a "
                      + hl("uma elevação") + " dos juros e aumento dos investimentos."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "A desoneração eleva a rentabilidade do investimento e desloca a demanda por fundos para "
                            "cima e para a direita; juros e investimento sobem. Exemplos: FINAME, depreciação "
                            "acelerada.",
        "qualidade_fonte": "bom",
        "figuras_fonte": FIG_E1("image (141).png"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0393
    {
        "id": "ECO-E1-0393-1", "fonte_ref": "E1-0393", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 2", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_FE,
        "rotulo_item": "Item",
        "assertiva": ("Um tabelamento de juros, com o governo estabelecendo uma taxa máxima de juros abaixo da taxa "
                      "de equilíbrio, pode ser eficaz em aumentar o investimento da economia, dado que os empresários "
                      "poderiam financiar as compras de bens de capital a um custo mais baixo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um tabelamento de juros, com o governo estabelecendo uma taxa máxima de juros abaixo da taxa "
                       "de equilíbrio, ") + vm("pode ser eficaz em aumentar") + az(" o investimento da economia, ")
                    + vm("dado que") + az(" os empresários ") + vm("poderiam") + az(" financiar as compras de bens "
                    "de capital a um custo mais baixo.")),
        "poucas": ("Teto abaixo do equilíbrio reduz a " + azb("oferta de fundos") + ": vale o lado curto do "
                   "mercado, e o volume de crédito — logo, o investimento — <b>cai</b>, com racionamento."),
        "destrinchando": [
            "É um " + azb("preço máximo") + " aplicado ao crédito. Abaixo do equilíbrio, os tomadores querem mais "
            "fundos (Fᴰ) e os poupadores ofertam menos (Fˢ). Sem preço para equilibrar, transaciona-se a menor "
            "das duas quantidades: " + vd("Fˢ < F*") + ".",
            "Quem obtém crédito paga menos, de fato; mas o investimento total é limitado pela poupança "
            "disponível, que encolheu. O meio verdadeiro do item (custo mais baixo) não sustenta a conclusão.",
            "O excesso de demanda gera " + azb("racionamento de crédito") + ": filas, critérios políticos ou de "
            "relacionamento, exigência de garantias, mercado paralelo a juros maiores. Projetos rentáveis ficam de "
            "fora e o capital se aloca pior.",
            "Experiência histórica: a " + rx("Constituição de 1988") + " trazia um teto de juros reais de 12% ao ano "
            "(art. 192, § 3º), nunca regulamentado e revogado pela " + vd("EC 40/2003") + " — exemplo clássico de "
            "tabelamento inaplicável.",
            vm("Regra-âncora: teto abaixo do equilíbrio → manda a oferta (o lado curto): quantidade cai."),
        ],
        "grafico_verso": "ECO-E1-0393-1-V1",
        "dissecando": (cz("[nexo indevido · inversão]") + " O item parte de uma verdade parcial (o crédito fica "
                       "mais barato para quem o obtém) e conclui o oposto do efeito agregado. Toda questão de "
                       "tabelamento pede o mesmo teste: qual lado do mercado fica curto?"),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um teto de juros acima da taxa de equilíbrio não altera o investimento.”</i> → CERTO",
            "<i>“Um teto de juros abaixo do equilíbrio gera excesso de oferta de fundos.”</i> → ERRADO (inversão: "
            "gera excesso de demanda)",
        ])],
        "reescrita": ("Um tabelamento de juros, com o governo estabelecendo uma taxa máxima de juros abaixo da taxa "
                      "de equilíbrio, " + hl("tende a reduzir") + " o investimento da economia, " + hl("ainda que")
                      + " os empresários " + hl("que obtêm crédito possam") + " financiar as compras de bens de "
                      "capital a um custo mais baixo."),
        "tipo_erro": ["NEXO_INDEVIDO", "INVERSAO"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Teto de juros abaixo do equilíbrio diminuiria o investimento, porque desincentiva a "
                            "oferta de crédito.",
        "qualidade_fonte": "raso",
        "figuras_fonte": FIG_E1("image (139).png"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0460
    {
        "id": "ECO-E1-0460-1", "fonte_ref": "E1-0460", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 5", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_CLA,
        "rotulo_item": "Item",
        "assertiva": ("O produto e nível de emprego da economia são determinados pelo lado da demanda. Desta forma, "
                      "uma política fiscal expansionista pode trazer maior crescimento econômico."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O produto e nível de emprego da economia são determinados pelo lado da ") + vm("demanda")
                    + az(". Desta forma, uma política fiscal expansionista ") + vm("pode") + az(" trazer maior "
                    "crescimento econômico.")),
        "poucas": ("No modelo clássico, produto e emprego vêm do " + azb("lado da oferta") + " (trabalho, capital, "
                   "tecnologia). A expansão fiscal só muda a composição do produto, via juros: "
                   + azb("crowding out") + " total."),
        "destrinchando": [
            "Sequência clássica: com salários flexíveis, o mercado de trabalho fixa o emprego de pleno emprego; a "
            "função de produção converte esse emprego em produto. A " + azb("oferta agregada") + " é vertical: a "
            "demanda não tem como alterar Y.",
            azb("Lei de Say") + " (" + oc("Jean-Baptiste Say") + "): a oferta cria sua própria demanda. Toda renda "
            "gerada é gasta, diretamente ou via poupança que vira investimento pelo ajuste dos juros.",
            "Expansão fiscal: mais G (ou menos T) reduz a poupança nacional, a oferta de fundos emprestáveis cai, "
            "os juros sobem e o investimento privado cai na mesma medida — " + vd("ΔI = −ΔG") + ". O produto não "
            "muda; muda quem o usa.",
            "Pior para o crescimento: menos investimento hoje significa menos capital amanhã. A política fiscal "
            "clássica que eleva o produto é a que mexe na <b>oferta</b> (infraestrutura, educação, incentivos).",
            "A frase do item descreve " + oc("Keynes") + ": demanda efetiva determina produto e emprego, e o "
            "gasto público pode tirar a economia do desemprego pelo multiplicador.",
        ],
        "dissecando": (cz("[troca de conceito · troca de ator]") + " O item atribui ao modelo clássico a tese "
                       "central keynesiana (demanda determina o produto) e tira dela a conclusão keynesiana. Pista: "
                       "o comando fixa o modelo clássico; qualquer frase com “determinado pela demanda” já cai."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, uma política fiscal expansionista eleva a taxa de juros e reduz o "
            "investimento na mesma magnitude.”</i> → CERTO",
            "<i>“No modelo clássico, a política monetária expansionista eleva o produto no curto prazo.”</i> → "
            "ERRADO (neutralidade: só eleva preços)",
        ])],
        "reescrita": ("O produto e nível de emprego da economia são determinados pelo lado da " + hl("oferta")
                      + ". Desta forma, uma política fiscal expansionista " + hl("não pode") + " trazer maior "
                      "crescimento econômico."),
        "tipo_erro": ["TROCA_CONCEITO", "TROCA_ATOR"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": "Para os clássicos, produto e emprego são determinados exclusivamente pela oferta; a "
                            "assertiva descreve a visão keynesiana.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0461
    {
        "id": "ECO-E1-0461-1", "fonte_ref": "E1-0461", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 5", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_CLA,
        "rotulo_item": "Item",
        "assertiva": ("Não existe desemprego involuntário, isto é, trabalhadores buscando emprego ao nível de salário "
                      "real vigente que não encontram emprego, pois os preços e salários são perfeitamente "
                      "flexíveis."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Não existe <u>desemprego involuntário</u>, isto é, trabalhadores buscando emprego ao nível de "
                      "salário real vigente que não encontram emprego, pois os preços e salários são "
                      "<u>perfeitamente flexíveis</u>."),
        "poucas": ("Com salários flexíveis, qualquer excesso de oferta de trabalho derruba o " + azb("salário real")
                   + " até que todos os que querem trabalhar a esse salário estejam empregados."),
        "destrinchando": [
            "Mercado de trabalho clássico: demanda das firmas (" + vd("w/P = PMgL") + ", decrescente) e oferta das "
            "famílias (crescente no salário real). O salário real se ajusta até igualar as duas: é o "
            + azb("pleno emprego") + ".",
            azb("Desemprego involuntário") + " (definição de " + oc("Keynes") + "): gente disposta a trabalhar pelo "
            "salário real vigente, ou até por menos, sem encontrar vaga. Exige salário acima do equilíbrio que não "
            "cai — rigidez que o modelo clássico exclui por hipótese.",
            "O que sobra no pleno emprego clássico: " + azb("desemprego voluntário") + " (quem não aceita o salário "
            "vigente) e " + azb("friccional") + " (tempo de busca entre empregos). Ambos compatíveis com a "
            "taxa natural.",
            "Keynes contesta em duas frentes: salários nominais rígidos para baixo e, mesmo que caíssem, a queda "
            "reduziria a renda e a demanda efetiva sem garantir o pleno emprego.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item define o conceito e dá a causa correta da sua ausência. "
                       "O absoluto “não existe” é a hipótese do modelo, delimitado pelo comando. A banca costuma "
                       "trocar “involuntário” por “friccional” ou “voluntário”, que existem mesmo no modelo "
                       "clássico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, não existe desemprego friccional, pois os salários são flexíveis.”</i> → "
            "ERRADO (o friccional persiste: é tempo de busca)",
            "<i>“Para os clássicos, todo desemprego observado no equilíbrio é voluntário ou friccional.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["perfeitamente"], "dificuldade": 1,
        "comentario_fonte": "Para os clássicos, com salários flexíveis, não há desemprego involuntário: quem quer "
                            "trabalhar, trabalha.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0463
    {
        "id": "ECO-E1-0463-1", "fonte_ref": "E1-0463", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Macro – Aula 5", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_RT_CLA,
        "rotulo_item": "Item",
        "assertiva": ("A economia sempre estará no pleno emprego, exceto se houver incerteza com relação ao futuro que "
                      "faça os empresários demitirem trabalhadores e não realizarem investimentos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A economia sempre estará no pleno emprego") + vm(", exceto se houver incerteza com relação "
                       "ao futuro que faça os empresários demitirem trabalhadores e não realizarem investimentos")
                    + az(".")),
        "poucas": ("A ressalva é " + oc("keynesiana") + ": incerteza radical e expectativas instáveis derrubando "
                   "investimento e emprego. No modelo clássico, o pleno emprego não tem essa exceção."),
        "destrinchando": [
            "Clássicos: salários e preços flexíveis garantem pleno emprego; a " + azb("Lei de Say") + " impede "
            "insuficiência de demanda; e a taxa de juros iguala poupança e investimento. Se o investimento cai, "
            "o juro cai e o consumo ou outro investimento ocupa o espaço.",
            "Os agentes clássicos têm informação suficiente para formar planos coerentes; o futuro não aparece "
            "como fonte de crises de demanda.",
            oc("Keynes") + " (<i>Teoria Geral</i>, 1936): o investimento depende da " + azb("eficiência marginal "
            "do capital") + ", isto é, de expectativas sobre um futuro incerto e não calculável. Os "
            + azb("“espíritos animais”") + " oscilam, o investimento despenca, a demanda efetiva cai e o "
            "desemprego involuntário pode persistir.",
            "A incerteza também alimenta a " + azb("preferência pela liquidez") + ": reter moeda é proteção contra "
            "o desconhecido, o que eleva os juros e reforça a queda do investimento.",
            vm("Regra-âncora: incerteza, expectativas e demanda efetiva = Keynes; flexibilidade e Lei de Say = "
               "clássicos."),
        ],
        "dissecando": (cz("[troca de ator · meia-verdade]") + " A 1ª oração é a tese clássica; a exceção enxertada "
                       "é argumento de Keynes. 🔥 Itens sobre escolas costumam colar a tese de uma escola ao "
                       "mecanismo de outra: pergunte sempre “quem diria isso?”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para Keynes, a incerteza quanto ao futuro pode deprimir o investimento e gerar desemprego "
            "involuntário persistente.”</i> → CERTO",
            "<i>“Para os clássicos, a queda do investimento gera desemprego até que o governo eleve seus "
            "gastos.”</i> → ERRADO (o ajuste é pelos juros, sem intervenção)",
        ])],
        "reescrita": ("A economia sempre estará no pleno emprego<s>, exceto se houver incerteza com relação ao futuro "
                      "que faça os empresários demitirem trabalhadores e não realizarem investimentos</s>"
                      + hl(", pois a flexibilidade de preços, salários e juros reabsorve qualquer queda de "
                           "investimento") + "."),
        "tipo_erro": ["TROCA_ATOR", "MEIA_VERDADE"], "moduladores": ["sempre", "exceto"], "dificuldade": 1,
        "comentario_fonte": "A incerteza sobre o futuro como causa do comportamento empresarial é argumento de "
                            "Keynes; para os clássicos, há pleno emprego e vale a Lei de Say.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0816
    {
        "id": "ECO-E1-0816-1", "fonte_ref": "E1-0816", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": ("Considere uma economia descrita pelo sistema de equações a seguir, em tempo contínuo. A respeito "
                    "dessa economia, julgue o item que se segue."),
        "excerto": (
            "<p>Função de produção agregada: Y = F(K, N), com F<sub>K</sub> &gt; 0, F<sub>N</sub> &gt; 0, "
            "F<sub>KN</sub> &gt; 0, F<sub>NN</sub> &lt; 0 e F<sub>KK</sub> &lt; 0, em que F<sub>i</sub> é a "
            "primeira derivada da função de produção com relação ao insumo i, e F<sub>ii</sub> é a segunda "
            "derivada da função de produção com relação ao insumo i</p>"
            "<p>Demanda de trabalho em termos reais: w/P = F<sub>N</sub>(K, N)</p>"
            "<p>Função investimento: I = I(q(K, N, r − π) − 1), I′ &lt; 0, em que I′ é a derivada do investimento "
            "em relação à taxa de juros</p>"
            "<p>Função consumo: C = C(Y − T), 0 &lt; C′ &lt; 1, em que C′ é a derivada do consumo em relação à "
            "renda disponível</p>"
            "<p>Equilíbrio no mercado de bens: Y = C + I + G + δK (5)</p>"
            "<p>Equilíbrio monetário: M/P = m(Y, r) (6)</p>"
            "<p>Em que Y é o produto, N o emprego, K o estoque de capital, w o salário nominal, P o nível geral de "
            "preços, I o investimento, q o Q de Tobin, r a taxa nominal de juros, π a taxa de inflação, C o "
            "consumo, T os tributos autônomos, G os gastos autônomos do governo, m(Y, r) a demanda real por moeda, "
            "M o estoque nominal de moeda e δK a taxa de depreciação do estoque de capital.</p>"
            "<p>Considere, ainda, um regime em que: o governo (via Banco Central) controla exogenamente a quantidade "
            "de moeda M; o estoque de capital é constante no tempo.</p>"),
        "rotulo_item": "Item",
        "assertiva": ("O sistema exibe a chamada dicotomia clássica: com o estoque de capital (K) dado, as variáveis "
                      "reais (Y, L, w/P, r − π, C, I) são determinadas exclusivamente pelo bloco real (função de "
                      "produção, mercado de trabalho, comportamento de consumo e investimento e política fiscal), "
                      "sendo o nível de preços P ajustado de forma a compatibilizar o equilíbrio monetário "
                      "M / P = m(Y, r), para um dado M."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O sistema ") + vm("exibe") + az(" a chamada dicotomia clássica: com o estoque de capital (K) "
                       "dado, as variáveis reais (Y, L, w/P, r − π, C, I) ") + vm("são determinadas exclusivamente")
                    + az(" pelo bloco real (função de produção, mercado de trabalho, comportamento de consumo e "
                         "investimento e política fiscal), ")
                    + vm("sendo o nível de preços P ajustado de forma a compatibilizar o equilíbrio monetário "
                         "M / P = m(Y, r), para um dado M") + az(".")),
        "poucas": ("O modelo só tem a <b>demanda</b> de trabalho, com " + azb("salário nominal w dado") + ". Então "
                   "P altera w/P, o emprego e o produto: preços e moeda afetam variáveis reais, e não há "
                   + azb("dicotomia clássica") + "."),
        "destrinchando": [
            "Conte as peças. Não há oferta de trabalho: a única equação do mercado de trabalho é " + vd("w/P = "
            "F<sub>N</sub>(K, N)") + ", e w é um parâmetro. Dado w, cada nível de preços P fixa um salário real, "
            "um emprego N e um produto Y = F(K, N). Isso é uma " + azb("oferta agregada positivamente inclinada")
            + ": P ↑ → w/P ↓ → N ↑ → Y ↑.",
            "As demais equações formam um " + azb("IS-LM") + ": consumo, investimento e equilíbrio de bens dão a "
            "IS; M/P = m(Y, r) dá a LM. Com a OA, são três relações para três incógnitas (Y, r, P), resolvidas "
            "<b>simultaneamente</b>. O lado real não se fecha sozinho.",
            "Teste da moeda: ↑M desloca a LM e a demanda agregada; P sobe, w/P cai, as firmas contratam mais e Y "
            "aumenta. A moeda <b>não é neutra</b> — exatamente o que a dicotomia nega.",
            "Para haver dicotomia faltaria uma " + azb("oferta de trabalho") + " N<sup>s</sup>(w/P) com w "
            "flexível: o mercado de trabalho fixaria w/P e N; a função de produção, Y; o mercado de bens, o juro "
            "real; e só então a equação monetária determinaria P. É o modelo clássico de manual.",
            "O item ainda menciona “mercado de trabalho” no bloco real, mas o sistema só especifica a demanda das "
            "firmas — o lado que poderia fechar o bloco real não existe.",
            vm("Regra-âncora: salário nominal dado + só demanda de trabalho = OA inclinada = moeda não neutra."),
        ],
        "dissecando": (cz("[troca de conceito · extrapolação]") + " O item descreve com perfeição a dicotomia de "
                       "manual e a aplica a um sistema que não tem a peça que a sustenta (oferta de trabalho com "
                       "salário flexível). O trabalho do candidato é inventariar as equações: w aparece como dado, "
                       "e P entra no salário real. 🔥 O bloco de 2026 explorou o mesmo sistema em vários itens "
                       "(neutralidade da moeda, choque de salário nominal, crowding out)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Como o modelo especifica apenas a demanda de trabalho, com salário nominal dado, variações do "
            "nível de preços alteram o emprego e o produto no curto prazo.”</i> → CERTO",
            "<i>“Um aumento permanente de M, com salário nominal dado, eleva apenas P, sem alterar Y nem N.”</i> → "
            "ERRADO (a queda de w/P eleva N e Y)",
            "<i>“Um aumento do salário nominal eleva P e reduz a renda de equilíbrio.”</i> → CERTO",
        ])],
        "reescrita": ("O sistema " + hl("não exibe") + " a chamada dicotomia clássica: com o estoque de capital (K) "
                      "dado, as variáveis reais (Y, L, w/P, r − π, C, I) " + hl("não são determinadas "
                      "exclusivamente") + " pelo bloco real (função de produção, mercado de trabalho, comportamento "
                      "de consumo e investimento e política fiscal), " + hl("porque, com o salário nominal w dado, "
                      "o nível de preços P — determinado em conjunto com o equilíbrio monetário M / P = m(Y, r) — "
                      "altera o salário real, o emprego e o produto") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "EXTRAPOLACAO"], "moduladores": ["exclusivamente"], "dificuldade": 3,
        "comentario_fonte": "",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: a equação da demanda de trabalho (w/P = F_N(K, N)) faltava na frente da fonte; "
                    "restaurada a partir do enunciado de outro item do mesmo bloco da prova, que a reproduz",
                    "nota_redacao: verso da fonte só com o gabarito; comentário redigido a partir do sistema de "
                    "equações e dos gabaritos dos demais itens do bloco"],
    },
    # ------------------------------------------------------------------ E2-L00081
    {
        "id": "ECO-E2-L00081-1", "fonte_ref": "E2-L00081", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Julgue o item a seguir como certo ou errado, com base nos conceitos de política econômica e de "
                    "intervenção governamental nos contextos keynesiano e clássico."),
        "rotulo_item": "Item",
        "assertiva": ("Na teoria clássica, a flexibilidade dos preços e dos salários garante que uma economia se "
                      "reequilibre de forma natural, sem necessidade de intervenção estatal, mesmo em tempos de "
                      "crise, visto que essa flexibilidade impulsiona os ajustes necessários para alcançar o pleno "
                      "emprego."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Na teoria clássica, a <u>flexibilidade dos preços e dos salários</u> garante que uma economia "
                      "se reequilibre de forma natural, sem necessidade de intervenção estatal, <u>mesmo em tempos "
                      "de crise</u>, visto que essa flexibilidade impulsiona os ajustes necessários para alcançar o "
                      "pleno emprego."),
        "poucas": ("É o " + azb("autoajuste") + " clássico: salários, preços e juros flexíveis eliminam excessos de "
                   "oferta e de demanda e levam a economia de volta ao pleno emprego, sem o Estado."),
        "destrinchando": [
            "Três mercados, três preços que se ajustam: no de trabalho, o " + azb("salário real") + " (desemprego "
            "→ salário cai → contratações sobem); no de fundos emprestáveis, a " + azb("taxa de juros") + " (queda "
            "do investimento → juro cai → poupança e investimento se igualam); no de bens, os " + azb("preços")
            + " (excesso de oferta → preços caem).",
            "Juntos, garantem a " + azb("Lei de Say") + ": não há insuficiência geral de demanda, e crises são "
            "desajustes temporários que o próprio mercado corrige.",
            "Daí o papel mínimo do Estado (laissez-faire): política fiscal só desloca investimento privado "
            "(crowding out) e política monetária só mexe em preços (neutralidade).",
            "A crítica de " + oc("Keynes") + " (1936) atacou essa premissa após a Grande Depressão: salários "
            "nominais são rígidos para baixo; e, mesmo que caíssem, a deflação reduziria renda e demanda, podendo "
            "aprofundar a crise. Daí a defesa de política fiscal ativa.",
            "Herdeiros da tese clássica: monetaristas (" + oc("Friedman") + ") e novos clássicos (" + oc("Lucas")
            + "), com expectativas racionais, retomam a ideia de que a economia tende ao produto natural.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " Retrato fiel do pensamento clássico. O “mesmo em tempos de "
                       "crise” e o “garante” parecem fortes, mas são a tese da escola, delimitada pelo “na teoria "
                       "clássica”. A banca fabrica o ERRADO trocando o ator (“na teoria keynesiana…”) ou incluindo "
                       "a necessidade de estímulo estatal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na teoria keynesiana, a flexibilidade de preços e salários garante o retorno ao pleno emprego sem "
            "intervenção estatal.”</i> → ERRADO (troca de ator: é a tese clássica)",
            "<i>“Para os clássicos, em crises, a política fiscal expansionista é necessária para restaurar o pleno "
            "emprego.”</i> → ERRADO (contradiz o autoajuste)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["garante", "mesmo"], "dificuldade": 1,
        "comentario_fonte": "Na teoria clássica, a flexibilidade de preços e salários garante o autoajuste da "
                            "economia ao pleno emprego, sem intervenção estatal.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00292
    {
        "id": "ECO-E2-L00292-1", "fonte_ref": "E2-L00292", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Acerca do modelo clássico de determinação da renda, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo clássico, caracterizado pela flexibilidade de preços e salários, a curva de Oferta "
                      "Agregada é vertical no nível de pleno emprego. Consequentemente, políticas fiscais "
                      "expansionistas resultam apenas em aumento do nível de preços e da taxa de juros (crowding out "
                      "total), sem afetar o produto real."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo clássico, caracterizado pela flexibilidade de preços e salários, a curva de Oferta "
                      "Agregada é <u>vertical</u> no nível de pleno emprego. Consequentemente, políticas fiscais "
                      "expansionistas resultam <u>apenas</u> em aumento do nível de preços e da taxa de juros "
                      "(crowding out total), sem afetar o produto real."),
        "poucas": ("Com a " + azb("OA vertical") + ", deslocar a demanda só move preços; nos fundos emprestáveis, os "
                   "juros sobem até o investimento privado cair o mesmo que o gasto público subiu: "
                   + azb("crowding out total") + "."),
        "destrinchando": [
            "Por que a OA é vertical: o produto depende só de trabalho, capital e tecnologia. Se P sobe, w sobe na "
            "mesma proporção (salários flexíveis), w/P não muda, e o emprego e o produto também não.",
            "Expansão fiscal: no mercado de bens, a demanda agregada se desloca para a direita e, com OA vertical, "
            "só o nível de preços sobe. Nos fundos emprestáveis, o governo absorve poupança, o juro sobe e o "
            "investimento privado cai: " + vd("ΔI = −ΔG") + ".",
            "Resultado: Y inalterado, composição do produto alterada (mais G, menos I) e menor acumulação de "
            "capital no futuro.",
            "Nuance de modelo: na versão estrita, em que a demanda agregada é só a TQM (PY = MV), G nem desloca a "
            "DA e o ajuste se dá todo pelos juros. A alta de P aparece quando a DA vem do IS-LM (ou quando V "
            "responde aos juros). Nas duas leituras, o produto real não muda.",
            "Contraste: com OA horizontal (keynesiano extremo), a expansão fiscal eleva Y sem pressão de preços; "
            "com OA positivamente inclinada (curto prazo), divide-se entre Y e P.",
        ],
        "grafico_verso": "ECO-E2-L00292-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " O item encadeia hipótese (flexibilidade), forma da OA (vertical) "
                       "e consequência (crowding out total) sem erro. O “apenas” assusta, mas é exatamente o que a "
                       "OA vertical implica. 🔥 A banca troca “vertical” por “horizontal” ou “crowding out total” "
                       "por “parcial” para fabricar o ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, a política fiscal expansionista eleva o produto, ainda que com crowding out "
            "parcial.”</i> → ERRADO (o crowding out é total)",
            "<i>“No modelo clássico, a política monetária expansionista eleva apenas o nível de preços.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": "O produto é determinado por fatores reais e a OA é vertical; a expansão fiscal eleva a "
                            "DA, o ajuste ocorre via preços, e os juros sobem reduzindo o investimento na mesma "
                            "proporção do gasto (crowding out).",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00455
    {
        "id": "ECO-E2-L00455-1", "fonte_ref": "E2-L00455", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": "Em relação à teoria macroeconômica, julgue (C ou E) o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A taxa de juros, para o modelo clássico, é determinada pela produtividade marginal do capital e "
                      "pela preferência intertemporal dos indivíduos; tal análise difere da perspectiva de Keynes, que "
                      "analisa a taxa de juros como resultante da preferência por liquidez, dada a oferta de moeda."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A taxa de juros, para o modelo clássico, é determinada pela <u>produtividade marginal do "
                      "capital</u> e pela <u>preferência intertemporal</u> dos indivíduos; tal análise difere da "
                      "perspectiva de Keynes, que analisa a taxa de juros como resultante da <u>preferência por "
                      "liquidez</u>, dada a oferta de moeda."),
        "poucas": ("Clássicos: juro é variável <b>real</b>, fixada por investimento (" + azb("produtividade do "
                   "capital") + ") e poupança (" + azb("paciência") + "). Keynes: juro é fenômeno <b>monetário</b>, "
                   "fixado pela demanda e oferta de moeda."),
        "destrinchando": [
            "Visão clássica (" + oc("Fisher") + ", " + oc("Böhm-Bawerk") + "): no mercado de fundos emprestáveis, "
            "a <b>demanda</b> vem do investimento, que depende da produtividade marginal do capital; a "
            "<b>oferta</b> vem da poupança, que remunera quem adia consumo (" + azb("preferência intertemporal")
            + "). O juro é o preço que iguala " + vd("S = I") + " — a recompensa pela espera.",
            "Visão de " + oc("Keynes") + " (<i>Teoria Geral</i>, 1936): o juro é a recompensa por abrir mão da "
            + azb("liquidez") + ", não por poupar. A demanda por moeda tem motivos transação, precaução e "
            "especulação; dada a oferta de moeda (decidida pelo banco central), o juro iguala as duas.",
            "Consequências: nos clássicos, poupança e investimento se igualam pelo juro, e a moeda é neutra. Em "
            "Keynes, o juro vem do mercado monetário; S e I se igualam pela variação da <b>renda</b>, e a política "
            "monetária afeta o lado real.",
            "Síntese posterior: o " + azb("IS-LM") + " (" + oc("Hicks") + ", 1937) junta os dois lados — o juro sai "
            "da interação entre o mercado de bens (IS) e o monetário (LM).",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item contrapõe corretamente as duas teorias. O risco é a troca "
                       "de atores: a banca costuma atribuir a preferência pela liquidez aos clássicos ou a "
                       "determinação real do juro a Keynes. Associe: <b>real</b> = clássico; <b>monetário</b> = "
                       "Keynes."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para os clássicos, a taxa de juros é determinada pela oferta e pela demanda de moeda.”</i> → "
            "ERRADO (troca de ator: é Keynes)",
            "<i>“Para Keynes, a igualdade entre poupança e investimento é garantida por variações na renda, e não "
            "na taxa de juros.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Clássicos: juro real fixado nos fundos emprestáveis por poupança (preferência "
                            "intertemporal) e investimento (produtividade marginal do capital). Keynes: juro "
                            "monetário, fixado por oferta de moeda e preferência pela liquidez.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["duplicata: E2-L00635 (mesmo item, mesma banca e ano, outro comando) fundido neste card"],
    },
    # ------------------------------------------------------------------ E2-L00923
    {
        "id": "ECO-E2-L00923-1", "fonte_ref": "E2-L00923", "destino": "25", "subtema": H2["cla"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2024", "ano": 2024, "cacd": False, "errei": False,
        "comando": ("Acerca dos indicadores do mercado de trabalho, conceitos e tipos de desemprego, julgue o item a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("O pagamento de um salário real de equilíbrio no modelo macroeconômico clássico permite afirmar "
                      "que a economia continua em pleno emprego, isso é possível mesmo quando ocorre uma demora na "
                      "aquisição de um novo emprego ou mesmo quando algumas pessoas preferem ficar desempregadas ao "
                      "nível de salário vigente. Nessas condições pode-se afirmar que, para o modelo clássico, o "
                      "mercado de trabalho garante o pleno emprego, mesmo com desemprego friccional e voluntário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O pagamento de um salário real de equilíbrio no modelo macroeconômico clássico permite afirmar "
                      "que a economia continua em pleno emprego, isso é possível mesmo quando ocorre uma demora na "
                      "aquisição de um novo emprego ou mesmo quando algumas pessoas preferem ficar desempregadas ao "
                      "nível de salário vigente. Nessas condições pode-se afirmar que, para o modelo clássico, o "
                      "mercado de trabalho garante o pleno emprego, <u>mesmo com desemprego friccional e "
                      "voluntário</u>."),
        "poucas": (azb("Pleno emprego") + " não é desemprego zero: é ausência de desemprego " + azb("involuntário")
                   + ". O friccional (busca) e o voluntário (recusa do salário vigente) convivem com ele."),
        "destrinchando": [
            "No modelo clássico, o salário real flexível iguala oferta e demanda de trabalho. Todos os que querem "
            "trabalhar a esse salário estão empregados — essa é a definição de pleno emprego.",
            azb("Desemprego friccional") + ": tempo de procura e de casamento entre vagas e trabalhadores (quem "
            "mudou de cidade, quem acabou de se formar). Existe mesmo com o mercado em equilíbrio.",
            azb("Desemprego voluntário") + ": quem não aceita trabalhar ao salário vigente. Não é falha do "
            "mercado; é escolha.",
            "Somados ao estrutural, compõem a " + azb("taxa natural de desemprego") + " (" + oc("Friedman") + ", "
            "1968), compatível com o pleno emprego. O que fica de fora é o " + azb("desemprego cíclico") + " (ou "
            "involuntário, na terminologia de " + oc("Keynes") + "), associado a recessões e a salários acima do "
            "equilíbrio.",
            "Ordem de grandeza " + rx("brasileira") + ": a taxa de desemprego da PNAD Contínua desceu para perto de "
            + vd("6%") + " em 2025, mínima da série iniciada em 2012 — um mercado de trabalho próximo ou abaixo "
            "das estimativas de taxa natural ⏳ (out/2026).",
        ],
        "dissecando": (cz("[contraintuitivo]") + " Parece contraditório “pleno emprego com desemprego”, e é nisso "
                       "que o item aposta. A chave é a definição: pleno emprego exclui só o involuntário. A banca "
                       "fabrica o ERRADO incluindo o involuntário ou dizendo que pleno emprego exige desemprego "
                       "nulo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo clássico, pleno emprego significa taxa de desemprego igual a zero.”</i> → ERRADO "
            "(friccional e voluntário persistem)",
            "<i>“Para o modelo clássico, o mercado de trabalho garante o pleno emprego, mesmo com desemprego "
            "involuntário.”</i> → ERRADO (troca de conceito: o involuntário é justamente o que a flexibilidade "
            "elimina)",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO"], "moduladores": ["mesmo"], "dificuldade": 2,
        "comentario_fonte": "Pleno emprego: todos que desejam trabalhar ao salário real de equilíbrio encontram "
                            "emprego, com a taxa natural (friccional e estrutural), sem desemprego cíclico.",
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
]
