"""Cards do lote de redação 19 — ECO, passada 02 (notas 36 a 40: política monetária, inflação, metas,
dominância fiscal, políticas não convencionais e crises)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "instr": "🛠️ Instrumentos de política monetária",
    "infl": "🔥 Tipos e teorias da inflação",
    "metas": "🎯 Metas de inflação e regras",
    "dom": "🐉 Dominância fiscal",
    "crise": "💥 Crises financeiras",
    "qe": "🖨️ QE, tapering e QT",
}

CMD_JB = ("A respeito dos efeitos que alterações na política monetária ou a flutuação do mercado cambial produzem "
          "sobre a base monetária e a liquidez do sistema financeiro nacional, julgue certo ou errado (C ou E) os "
          "itens a seguir.")

CMD_NIDI26 = "Sobre os instrumentos de política monetária e o papel do Banco Central do Brasil, julgue o item a seguir."

CMD_ANOS80 = ("A respeito do período de hiperinflação dos anos 1980 e dos correspondentes planos de combate à "
              "inflação, julgue (C ou E) o item a seguir.")

CMD_METAS_BR = ("Considerando que a economia brasileira mantém o regime de metas de inflação, julgue o item a "
                "seguir.")

CMD_NAB_MON = "Em relação ao sistema monetário e à política monetária, julgue (C ou E) o item a seguir."

CMD_NAB_MF = "Em relação às políticas monetária e fiscal, julgue (C ou E) o item a seguir."

CMD_TPS25 = "Acerca das políticas monetárias convencionais e não convencionais, julgue o item a seguir."

ALERTA_TPS25 = ("texto_parcial: o comando original (“A partir do texto apresentado”) remete a um texto-base que não "
                "veio na fonte; comando neutralizado, e o item se julga sem o texto")


def img_texto(*refs):
    return [{"ref": r, "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida (conteúdo levado ao 📖)"}
            for r in refs]


def img_e1(ref):
    return [{"ref": ref, "tipo_fonte": "IMAGEM", "lado": "verso",
             "acao": "cortada (imagem do verso não preservada; conteúdo absorvido no 📖)"}]


CARDS = [
    # ------------------------------------------------------------------ E3-L00419
    {
        "id": "ECO-E3-L00419-1", "fonte_ref": "E3-L00419", "destino": "36", "subtema": H2["instr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": True,
        "comando": CMD_JB,
        "rotulo_item": "Item",
        "assertiva": ("As operações de mercado aberto objetivam primordialmente contribuir para a aproximação entre "
                      "a taxa de juros do mercado de reservas bancárias e a taxa básica de juros anunciada pelas "
                      "autoridades monetárias, evitando que excesso ou falta de liquidez afaste a taxa básica "
                      "anunciada da taxa de mercado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("As operações de mercado aberto objetivam <u>primordialmente</u> contribuir para a "
                      "aproximação entre a <u>taxa de juros do mercado de reservas bancárias</u> e a <u>taxa básica "
                      "de juros anunciada</u> pelas autoridades monetárias, evitando que excesso ou falta de "
                      "liquidez afaste a taxa básica anunciada da taxa de mercado."),
        "poucas": ("O " + azb("open market") + " é a “sintonia fina” da política monetária: o BC compra ou vende "
                   "títulos todo dia para que a " + azb("Selic efetiva") + " (taxa do mercado de reservas) fique "
                   "colada na " + azb("meta da Selic") + " fixada pelo Copom."),
        "destrinchando": [
            "O Copom <b>anuncia</b> uma meta para a taxa básica, mas não a decreta: os bancos negociam reservas "
            "entre si no " + azb("mercado de reservas bancárias") + " (empréstimos de um dia, lastreados em "
            "títulos públicos), e a taxa média ponderada dessas operações é a " + azb("Selic efetiva (over)")
            + ". A política só funciona se essa taxa de mercado seguir a meta.",
            "Excesso de liquidez (pagamentos do Tesouro, compra de dólares pelo BC) → a taxa de mercado tende a "
            "<b>cair</b> abaixo da meta → o BC <b>vende</b> títulos (ou faz compromissadas de venda) e enxuga "
            "reservas. Falta de liquidez (recolhimento de tributos, saída de divisas) → a taxa tende a "
            "<b>subir</b> → o BC <b>compra</b> títulos e injeta reservas.",
            "No dia a dia brasileiro, a maior parte do ajuste se faz por " + azb("operações compromissadas")
            + " (compra ou venda com recompra/revenda marcada), de prazo curto, conduzidas pela mesa de mercado "
            "aberto do BC.",
            "Funções secundárias do open market — sinalização, apoio à gestão da dívida, provisão de liquidez em "
            "crises — existem, mas a função <b>operacional</b> é a do item. Por isso o “primordialmente” não o "
            "torna falso.",
            vm("Regra-âncora: o Copom fixa a meta; o open market faz a taxa de mercado obedecer à meta."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O item descreve a função operacional clássica do open "
                       "market. O risco está no vocabulário: quem não distingue taxa “anunciada” (meta) de taxa "
                       "“de mercado” (efetiva) estranha a frase e tende a marcar ERRADO; e o “primordialmente” "
                       "parece exagero, mas é exatamente a função central do instrumento."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quando há excesso de liquidez e a taxa de mercado cai abaixo da meta, o BC compra títulos "
            "públicos.”</i> → ERRADO (inversão: vende títulos para enxugar)",
            "<i>“A meta para a taxa Selic é fixada pelo Conselho Monetário Nacional.”</i> → ERRADO (troca de "
            "ator: é o Copom; o CMN fixa a meta de inflação)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["primordialmente"], "dificuldade": 2,
        "comentario_fonte": ("Open market é a sintonia fina: o BC compra ou vende títulos diariamente para que a "
                             "Selic efetiva convirja para a meta do Copom; vende títulos no excesso de liquidez e "
                             "compra na falta."),
        "qualidade_fonte": "bom",
        "figuras_fonte": img_texto("IMAGEM 593", "IMAGEM 594", "IMAGEM 595"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00421
    {
        "id": "ECO-E3-L00421-1", "fonte_ref": "E3-L00421", "destino": "36", "subtema": H2["instr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": CMD_JB,
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central realiza operações de mercado aberto vendendo títulos públicos quando deseja "
                      "aumentar a liquidez do sistema bancário."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Banco Central realiza operações de mercado aberto ") + vm("vendendo")
                    + az(" títulos públicos quando deseja aumentar a liquidez do sistema bancário.")),
        "poucas": ("Vender títulos <b>retira</b> reservas: os bancos pagam o papel com moeda, que volta ao BC. "
                   "Para " + azb("aumentar a liquidez") + ", o BC <b>compra</b> títulos e paga creditando reservas."),
        "destrinchando": [
            "O BC troca papel por dinheiro. Na " + azb("venda") + ", entrega título e recebe reservas → a base "
            "monetária encolhe, a liquidez cai e os juros de curtíssimo prazo sobem (política "
            + azb("contracionista") + "). Na " + azb("compra") + ", recebe título e cria reservas → a base "
            "cresce, a liquidez aumenta e os juros caem (política " + azb("expansionista") + ").",
            "No balanço do BC: a compra aumenta o ativo (títulos) e o passivo monetário (reservas) no mesmo "
            "montante; a venda reduz os dois.",
            "No " + rx("Brasil") + ", quase todo o ajuste diário é feito por " + azb("operações compromissadas")
            + ": o BC vende com compromisso de recompra para enxugar sobras de reservas por poucos dias, ou "
            "compra com compromisso de revenda para suprir faltas.",
            "Os outros dois instrumentos clássicos seguem a mesma lógica: reduzir o " + azb("compulsório")
            + " ou baratear o " + azb("redesconto") + " também injeta liquidez; elevá-los a retira.",
            vm("Regra-âncora: BC compra título = injeta reservas; BC vende título = enxuga reservas."),
        ],
        "dissecando": (cz("[inversão]") + " Troca simples de sentido: a ação (vender) é a do aperto, e o "
                       "objetivo (aumentar a liquidez) é o do afrouxamento. Basta perguntar “para onde vai o "
                       "dinheiro?”: na venda, sai dos bancos e entra no BC. 🔥 Inversão compra × venda é das "
                       "pegadinhas mais repetidas em open market."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Banco Central realiza operações compromissadas de venda de títulos quando deseja reduzir "
            "temporariamente a liquidez do sistema bancário.”</i> → CERTO",
            "<i>“A compra de títulos pelo Banco Central reduz a base monetária.”</i> → ERRADO (inversão: "
            "amplia a base)",
        ])],
        "reescrita": ("O Banco Central realiza operações de mercado aberto " + hl("comprando")
                      + " títulos públicos quando deseja aumentar a liquidez do sistema bancário."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Lógica invertida: vender títulos retira dinheiro do mercado e contrai a liquidez; "
                             "para aumentá-la, o BC compra títulos. BC comprador = expansão; vendedor = contração."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00442
    {
        "id": "ECO-E3-L00442-1", "fonte_ref": "E3-L00442", "destino": "36", "subtema": H2["instr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NIDI26,
        "rotulo_item": "Item",
        "assertiva": ("Se os bancos comerciais têm acesso irrestrito à janela de redesconto do Banco Central, a taxa "
                      "de redesconto estabelece um limite máximo à taxa de juros do mercado de reservas bancárias."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se os bancos comerciais têm <u>acesso irrestrito</u> à janela de redesconto do Banco "
                      "Central, a taxa de redesconto estabelece um <u>limite máximo</u> à taxa de juros do mercado "
                      "de reservas bancárias."),
        "poucas": ("É " + azb("arbitragem") + ": se qualquer banco pode tomar no BC quanto quiser à taxa de "
                   "redesconto, nenhum pagará mais do que isso a outro banco. O redesconto vira o " + vd("teto")
                   + " da taxa interbancária."),
        "destrinchando": [
            "O " + azb("redesconto") + " é o empréstimo do BC aos bancos (assistência de liquidez), cobrado à "
            "taxa de redesconto. O " + azb("mercado de reservas") + " é onde os bancos com sobra emprestam aos "
            "bancos com falta, de um dia para o outro.",
            "Se a taxa interbancária (i) superasse a de redesconto (r), os bancos deficitários iriam todos ao "
            "BC, e os superavitários teriam de baixar o preço para emprestar: i volta para baixo de r. Se i < r, "
            "ninguém usa o redesconto, salvo falta generalizada de liquidez.",
            "O detalhe decisivo é o <b>acesso irrestrito</b>: com cotas, exigências de garantia muito duras ou "
            "estigma, a janela deixa de ser alternativa perfeita e a taxa de mercado pode furar o teto "
            "(foi o que se viu em crises, quando bancos evitavam o redesconto para não sinalizar fragilidade).",
            "Generalização moderna: o " + azb("corredor de juros") + ". A facilidade de empréstimo (redesconto) "
            "dá o teto; a facilidade de depósito (remuneração das reservas excedentes) dá o piso; a meta fica "
            "no meio. É o desenho do BCE e de vários BCs.",
            vm("Regra-âncora: redesconto ilimitado = teto da taxa interbancária; remuneração de reservas = piso."),
        ],
        "grafico_verso": "ECO-E3-L00442-1-V1",
        "dissecando": (cz("[detalhe · literalidade]") + " O item é a definição de manual, protegida pela "
                       "condicional “se … acesso irrestrito”. O risco é confundir teto com piso: quem pensa "
                       "“o BC cobra caro no redesconto, então os juros de mercado ficam acima” marca ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…a taxa de redesconto estabelece um limite mínimo à taxa de juros do mercado de reservas.”</i> "
            "→ ERRADO (inversão: é limite máximo; o piso viria da remuneração das reservas)",
            "<i>“Ainda que o acesso ao redesconto seja limitado por cotas, a taxa de redesconto funciona como "
            "teto rígido da taxa interbancária.”</i> → ERRADO (modulador absoluto: sem acesso irrestrito, a "
            "arbitragem falha)",
        ])],
        "tipo_erro": ["DETALHE", "LITERAL"], "moduladores": ["se", "irrestrito"], "dificuldade": 2,
        "comentario_fonte": ("Com acesso irrestrito ao redesconto, nenhum banco paga no interbancário mais que a "
                             "taxa de redesconto, pois pode tomar diretamente no BC; a taxa funciona como teto, à "
                             "semelhança do corredor de juros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": img_texto("IMAGEM 615", "IMAGEM 616", "IMAGEM 617"),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E3-L00445
    {
        "id": "ECO-E3-L00445-1", "fonte_ref": "E3-L00445", "destino": "36", "subtema": H2["instr"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Fevereiro/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_NIDI26,
        "rotulo_item": "Item",
        "assertiva": ("Uma operação de mercado aberto, na qual o Banco Central compra títulos da dívida e emite "
                      "moeda, aumenta os ativos e os passivos do balancete do Banco Central no mesmo montante."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma operação de mercado aberto, na qual o Banco Central compra títulos da dívida e emite "
                      "moeda, aumenta os ativos e os passivos do balancete do Banco Central <u>no mesmo "
                      "montante</u>."),
        "poucas": ("Partidas dobradas: o título comprado entra no " + azb("ativo") + " pelo preço pago, e a "
                   "moeda emitida para pagá-lo entra no " + azb("passivo monetário") + " (base monetária) pelo "
                   "mesmo valor."),
        "destrinchando": [
            "Balancete sintético do BC — <b>ativo</b>: reservas internacionais, redescontos, créditos ao governo, "
            "títulos públicos federais; <b>passivo</b>: a " + azb("base monetária") + " (papel-moeda emitido + "
            "reservas bancárias) e os passivos não monetários (compulsórios em espécie, conta única do Tesouro, "
            "obrigações externas, recursos próprios).",
            "Compra de títulos por R$ 100: títulos + " + vd("100") + " no ativo; reservas (ou papel-moeda) + "
            + vd("100") + " no passivo. A base cresce 100, e o balanço “incha” dos dois lados. A venda faz o "
            "caminho inverso.",
            "Variação da base = variação do ativo − variação dos passivos não monetários. Por isso a compra "
            "<b>expande</b> a base, salvo se outra operação a " + azb("esterilizar") + " (por exemplo, uma "
            "compromissada de venda no mesmo valor).",
            "Dúvida comum: “o título vale mais no vencimento”. O registro inicial é pelo " + azb("custo de "
            "aquisição") + " (o que se pagou, ex.: R$ 950), não pelo valor de face (R$ 1.000). O deságio vira "
            "receita de juros apropriada ao longo do prazo, sem quebrar a simetria do lançamento.",
            "A mesma lógica explica o " + azb("quantitative easing") + ": compras maciças de ativos expandem o "
            "balanço do BC, e a " + azb("QT") + " o contrai.",
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O item é contabilidade de manual. A armadilha "
                       "é a de quem pensa em valor futuro do título ou acha que “emitir moeda” não cria passivo "
                       "(cria: a moeda é dívida monetária do BC). “No mesmo montante” é a palavra-chave, e está "
                       "certa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A compra de títulos pelo Banco Central aumenta seu ativo e reduz seu passivo no mesmo "
            "montante.”</i> → ERRADO (sinal trocado: o passivo também aumenta)",
            "<i>“Uma compra de títulos acompanhada de compromissada de venda no mesmo valor deixa a base "
            "monetária inalterada.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Na compra de títulos, o ativo do BC cresce pelos títulos e o passivo pela moeda "
                             "emitida, no mesmo valor; o registro é pelo preço de aquisição, não pelo valor de face, "
                             "e o deságio é apropriado como juros ao longo do tempo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": (img_texto("IMAGEM 626")
                          + [{"ref": r, "tipo_fonte": "TABELA", "lado": "verso",
                              "acao": "absorvida (balancete sintético resumido no 📖)"}
                             for r in ("IMAGEM 627", "IMAGEM 628")]
                          + img_texto("IMAGEM 629")),
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0456
    {
        "id": "ECO-E1-0456-1", "fonte_ref": "E1-0456", "destino": "37", "subtema": H2["infl"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Clipping", "ano": 2025, "cacd": False,
        "errei": False,
        "comando": ("A década de 1980 ficou marcada por instabilidade econômica, aceleração inflacionária e "
                    "sucessivos planos de ajuste. Considerando esse contexto, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Os planos de combate à inflação nesse período frequentemente baseavam-se em congelamentos de "
                      "preços e salários, refletindo a crença na predominância da inflação de custos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("Os planos de combate à inflação nesse período <u>frequentemente</u> baseavam-se em "
                      "congelamentos de preços e salários, refletindo a crença na predominância da <u>inflação de "
                      "custos</u>."),
        "poucas": ("Os " + azb("choques heterodoxos") + " (Cruzado, Bresser, Verão) congelaram preços e salários "
                   "porque o diagnóstico era de inflação <b>não de demanda</b> — inercial, alimentada pela "
                   "indexação e pelo conflito distributivo —, que a banca enquadra na família da inflação de "
                   "custos."),
        "condicionais": [("⚠️ Gabarito contestável", "O rótulo mais preciso para o diagnóstico dos planos é "
                          + azb("inflação inercial") + ", não “de custos”. O CERTO se sustenta porque a "
                          "literatura de manual agrupa inércia, custos e conflito distributivo como inflações "
                          "<b>de oferta</b>, opostas à de demanda; numa prova que exigisse a distinção fina, "
                          "o item poderia ser lido como ERRADO.")],
        "destrinchando": [
            "Planos com congelamento: " + vd("Cruzado (fev./1986)") + ", " + vd("Bresser (jun./1987)") + " e "
            + vd("Verão (jan./1989)") + ", no governo " + rx("Sarney") + "; o " + vd("Collor I (1990)")
            + " também congelou preços, somado ao bloqueio de ativos financeiros.",
            "Diagnóstico de fundo: com a indexação generalizada, a inflação de hoje repetia a de ontem "
            "(" + azb("inércia") + "). Cada grupo reajustava preços e salários para recompor o pico de renda "
            "real — o " + azb("conflito distributivo") + ". Choques de custos (petróleo, maxidesvalorização de "
            "1983) elevavam o patamar, e a indexação o perpetuava.",
            "Daí a receita: se a inflação não vem do excesso de demanda, apertar moeda e gasto só gera recessão; "
            "melhor “zerar a memória” com congelamento e regras de conversão (tablitas, gatilho salarial).",
            "Por que falharam: o congelamento não tratava o desequilíbrio fiscal nem a demanda aquecida (o "
            "Cruzado gerou desabastecimento e ágio), e os preços relativos ficavam desalinhados no dia do "
            "congelamento. O " + rx("Plano Real") + " (1993–1994) resolveu a inércia sem congelar, pela "
            + azb("URV") + ", com ajuste fiscal prévio.",
            "Contraste: a visão " + azb("ortodoxa") + " lia a inflação como de demanda (déficit financiado por "
            "emissão), e propunha aperto fiscal e monetário.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " O “frequentemente” protege o item (nem "
                       "todo plano congelou). O risco é a etiqueta “inflação de custos”: quem domina a palavra "
                       "“inercial” desconfia, mas a banca usa “custos” em sentido amplo, de inflação que não nasce "
                       "da demanda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os planos da década de 1980 partiam do diagnóstico de inflação de demanda e, por isso, "
            "concentravam-se no corte do gasto público.”</i> → ERRADO (troca de conceito: diagnóstico inercial)",
            "<i>“O Plano Real repetiu o congelamento de preços e salários dos planos anteriores.”</i> → ERRADO "
            "(extrapolação: usou a URV, sem congelamento)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["frequentemente"],
        "dificuldade": 2,
        "comentario_fonte": ("Cruzado, Bresser e Verão partiram do diagnóstico de inflação majoritariamente "
                             "inercial (ou de custos), repassada pela indexação; o congelamento visava quebrar a "
                             "inércia."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: o diagnóstico dos planos era de inflação inercial; o gabarito CERTO depende de "
                    "ler “inflação de custos” em sentido amplo (inflação de oferta)"],
    },
    # ------------------------------------------------------------------ E1-0802
    {
        "id": "ECO-E1-0802-1", "fonte_ref": "E1-0802", "destino": "37", "subtema": H2["infl"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True,
        "errei": False,
        "comando": CMD_ANOS80,
        "rotulo_item": "Item",
        "assertiva": ("O chamado conflito distributivo se incluía entre as hipóteses levantadas para explicar a "
                      "continuidade da inflação como o resultado de uma tentativa constante de apropriação de uma "
                      "fatia maior da renda por cada grupo de interesse — por exemplo, trabalhadores buscavam "
                      "aumentos de salários, enquanto empresários buscavam reajustar os preços de seus produtos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O chamado conflito distributivo <u>se incluía entre as hipóteses</u> levantadas para "
                      "explicar a continuidade da inflação como o resultado de uma tentativa constante de "
                      "apropriação de uma fatia maior da renda por cada grupo de interesse — por exemplo, "
                      "trabalhadores buscavam aumentos de salários, enquanto empresários buscavam reajustar os "
                      "preços de seus produtos."),
        "poucas": ("No " + azb("conflito distributivo") + ", as pretensões de renda dos grupos somam mais que a "
                   "renda disponível: salários sobem, empresas repassam aos preços, salários reagem — e a inflação "
                   "se perpetua. Foi uma das explicações da inflação brasileira dos anos 1980."),
        "destrinchando": [
            "Mecanismo: trabalhadores querem um salário real w/p; empresários querem uma margem (mark-up) sobre "
            "os custos. Se as duas metas são <b>incompatíveis</b> com a produtividade, cada reajuste de um lado "
            "corrói o ganho do outro, que reage. A inflação é o resultado da disputa, não do excesso de demanda.",
            "Com " + azb("indexação") + " formal e informal, a disputa ganhava regularidade: cada grupo reajustava "
            "pelo pico de renda real anterior, e a inflação passada se transmitia à futura. Por isso conflito "
            "distributivo e " + azb("inércia") + " andam juntos no debate brasileiro.",
            "No " + rx("Brasil") + ", " + oc("Bresser-Pereira") + " e " + oc("Yoshiaki Nakano") + " "
            "distinguiram fatores " + azb("aceleradores") + " (choques de custos, de câmbio, de demanda), "
            + azb("mantenedores") + " (o conflito distributivo indexado) e " + azb("sancionadores")
            + " (a moeda, que valida a alta). Os " + oc("inercialistas da PUC-Rio") + " (" + oc("Francisco Lopes")
            + ", " + oc("Pérsio Arida") + ", " + oc("André Lara Resende") + ") deram a versão inercial.",
            "Política derivada: congelamento ou " + azb("pacto social") + " para coordenar a parada simultânea "
            "dos reajustes (Plano Bresser, 1987, tinha esse viés), em vez de recessão.",
            "Raiz teórica fora do Brasil: a inflação de conflito de " + oc("Rowthorn") + " (1977) e a tradição "
            "pós-keynesiana e estruturalista latino-americana.",
        ],
        "dissecando": (cz("[paráfrase fiel · literalidade]") + " Reproduz a definição de manual com o exemplo "
                       "típico salário × preço. Note o modulador: “se incluía entre as hipóteses”, sem dizer que "
                       "era a única explicação — o que tornaria o item atacável."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O conflito distributivo era a única explicação aceita para a inflação brasileira dos anos "
            "1980.”</i> → ERRADO (restrição indevida: convivia com a inércia e com a tese fiscal)",
            "<i>“Na tese do conflito distributivo, a inflação resulta essencialmente do excesso de demanda "
            "agregada.”</i> → ERRADO (troca de conceito: é disputa por renda)",
        ]), ("🃏 Carta na manga", [
            "A inflação brasileira dos anos 1980 foi lida como fenômeno de " + azb("coordenação") + ": com "
            "indexação e conflito distributivo, nenhum agente tinha incentivo a parar de reajustar sozinho — "
            "daí a busca por mecanismos de desindexação simultânea, do congelamento à URV.",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "LITERAL"], "moduladores": ["se incluía entre as hipóteses"],
        "dificuldade": 1,
        "comentario_fonte": ("Inflação como disputa entre trabalhadores e empresários por fatia maior da renda; "
                             "defendida por Bresser-Pereira e Nakano; relacionada à indexação e à inércia; base de "
                             "propostas de pacto social e do Plano Bresser."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0863
    {
        "id": "ECO-E1-0863-1", "fonte_ref": "E1-0863", "destino": "37", "subtema": H2["infl"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2016, "cacd": False,
        "errei": False,
        "comando": ("O diplomata responsável pelo setor econômico da embaixada brasileira em determinado país "
                    "elaborou e enviou à Secretaria de Estado um relatório sobre a situação econômica desse país. "
                    "Considerando o fato de que uma das funções do diplomata é manter o governo brasileiro "
                    "informado a respeito do contexto político, econômico e cultural do país onde ele esteja "
                    "temporariamente vivendo, julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Considere que, no referido país, os níveis de inflação sejam elevados e o regime de câmbio "
                      "seja fixo. Nesse caso, é correto afirmar que a inflação alta provoca, geralmente, efeitos "
                      "nocivos sobre a economia, uma vez que reduz o poder de compra dos indivíduos, tende a gerar "
                      "concentração de renda e pode contribuir para aumentar os déficits na balança comercial do "
                      "balanço de pagamentos."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Considere que, no referido país, os níveis de inflação sejam elevados e o regime de câmbio "
                      "seja <u>fixo</u>. Nesse caso, é correto afirmar que a inflação alta provoca, "
                      "<u>geralmente</u>, efeitos nocivos sobre a economia, uma vez que reduz o poder de compra dos "
                      "indivíduos, <u>tende a</u> gerar concentração de renda e <u>pode</u> contribuir para "
                      "aumentar os déficits na balança comercial do balanço de pagamentos."),
        "poucas": ("Os três efeitos valem: inflação corrói salários, pesa mais sobre quem não se protege e, "
                   "com " + azb("câmbio fixo") + ", aprecia o " + azb("câmbio real") + " — exporta-se menos, "
                   "importa-se mais."),
        "destrinchando": [
            "<b>Poder de compra</b>: renda nominal reajustada com atraso perde valor real entre um reajuste e "
            "outro; quanto maior a inflação, maior a perda média do período.",
            "<b>Concentração de renda</b>: os mais pobres gastam toda a renda e guardam moeda, sem acesso a "
            "ativos indexados ou a contas remuneradas; os mais ricos se protegem com aplicações, imóveis e "
            "ativos reais. O " + azb("imposto inflacionário") + " é regressivo.",
            "<b>Balança comercial</b>: câmbio real = E·P*/P. Com E fixo e P subindo mais que P*, o câmbio real "
            + azb("aprecia") + ": o produto nacional encarece lá fora e o importado barateia aqui. O saldo "
            "comercial piora, e a sustentação da paridade exige reservas — caminho clássico de crise cambial "
            "(" + rx("Brasil") + " em " + vd("1998–1999") + ", após anos de âncora cambial).",
            "Com câmbio flutuante, a própria depreciação nominal tende a compensar o diferencial de inflação "
            "(paridade do poder de compra relativa), e o efeito sobre a balança é menor.",
            "Outros custos que a banca cita: custo de " + azb("sola de sapato") + ", custo de " + azb("menu")
            + ", ruído nos preços relativos (pior alocação), encurtamento de contratos e o " + azb("efeito "
            "Olivera-Tanzi") + " (a arrecadação perde valor real entre fato gerador e recolhimento).",
        ],
        "dissecando": (cz("[modulador relativo · detalhe]") + " Três efeitos verdadeiros, todos protegidos por "
                       "moduladores (“geralmente”, “tende a”, “pode”). A pista é o “câmbio fixo”: é ele que liga a "
                       "inflação ao déficit comercial; quem ignora o regime pensa em depreciação compensatória e "
                       "erra."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…com câmbio fixo, a inflação alta tende a melhorar a balança comercial, pois barateia as "
            "exportações.”</i> → ERRADO (inversão: aprecia o câmbio real e encarece as exportações)",
            "<i>“…a inflação alta tende a gerar desconcentração de renda, pois reduz o valor real das "
            "dívidas.”</i> → ERRADO (nexo indevido: o efeito líquido dominante é regressivo)",
        ])],
        "tipo_erro": ["MODULADOR_RELATIVO", "DETALHE"], "moduladores": ["geralmente", "tende a", "pode"],
        "dificuldade": 1,
        "comentario_fonte": ("Inflação reduz o poder de compra; concentra renda porque os pobres não se protegem e "
                             "os reajustes salariais vêm depois; com câmbio fixo, valoriza o câmbio real e piora a "
                             "balança comercial."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["banca_provavel: enquadramento do diplomata e marcação de 2016 sugerem CACD 2016 (CEBRASPE); a "
                    "fonte não confirma"],
    },
    # ------------------------------------------------------------------ E2-L00310
    {
        "id": "ECO-E2-L00310-1", "fonte_ref": "E2-L00310", "destino": "37", "subtema": H2["infl"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca das teorias da inflação, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Segundo a visão keynesiana, a inflação por conflito distributivo só emerge após a economia "
                      "atingir o pleno emprego, momento em que maiores salários reais necessariamente reduzem o "
                      "lucro, elevando os preços."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a visão keynesiana, a inflação por conflito distributivo ")
                    + vm("só emerge após") + az(" a economia atingir o pleno emprego, ")
                    + vm("momento em que maiores salários reais necessariamente reduzem o lucro")
                    + az(", elevando os preços.")),
        "poucas": ("O conflito distributivo " + azb("não depende do pleno emprego") + ": basta que as "
                   "pretensões de salário real e de margem de lucro sejam incompatíveis. Perto do pleno emprego o "
                   "poder de barganha cresce e o conflito se intensifica, mas não é condição necessária."),
        "destrinchando": [
            "Na leitura " + oc("keynesiana") + " e " + oc("pós-keynesiana") + ", os preços são formados por "
            + azb("mark-up") + " sobre custos, sobretudo salários. Se os trabalhadores obtêm reajuste nominal "
            "acima da produtividade, as empresas repassam para manter a margem; os salários reais voltam para "
            "trás, e a disputa recomeça. É um processo de custos, não de demanda.",
            "Já " + oc("Keynes") + " (<i>Teoria Geral</i>, cap. 21) admitia alta de preços <b>antes</b> do pleno "
            "emprego, por gargalos setoriais e pressões salariais à medida que o desemprego "
            "cai; a “inflação verdadeira” (<i>true inflation</i>) seria a do pleno emprego, quando mais demanda não gera mais produto.",
            "O desemprego modera o conflito (enfraquece sindicatos), mas não o elimina: a inflação brasileira dos "
            "anos 1980 conviveu com recessão e alta capacidade ociosa, e foi lida justamente como conflito "
            "distributivo indexado.",
            "O “necessariamente” também falha: com ganho de produtividade, salário real maior não exige lucro "
            "menor; e o repasse aos preços é justamente a forma de a empresa <b>não</b> perder margem.",
            vm("Regra-âncora: inflação de conflito é inflação de custos e pode ocorrer com desemprego; não "
               "precisa de pleno emprego."),
        ],
        "dissecando": (cz("[restrição indevida · troca de conceito]") + " O “só … após o pleno emprego” "
                       "transporta para o conflito distributivo a condição típica da " + azb("inflação de "
                       "demanda") + " keynesiana (hiato inflacionário). O “necessariamente” empilha uma segunda "
                       "generalização."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Na visão keynesiana, a inflação de demanda manifesta-se plenamente quando a economia atinge o "
            "pleno emprego e o aumento do gasto não amplia o produto.”</i> → CERTO",
            "<i>“A inflação por conflito distributivo é incompatível com desemprego elevado.”</i> → ERRADO "
            "(modulador absoluto: ocorreu no Brasil com recessão)",
        ])],
        "reescrita": ("Segundo a visão keynesiana, a inflação por conflito distributivo " + hl("pode emergir antes de")
                      + " a economia atingir o pleno emprego, "
                      + hl("sempre que as pretensões de salário real e de lucro forem incompatíveis")
                      + ", elevando os preços."),
        "tipo_erro": ["RESTRICAO", "TROCA_CONCEITO"], "moduladores": ["só", "necessariamente"], "dificuldade": 2,
        "comentario_fonte": ("A inflação por conflito distributivo pode ocorrer antes do pleno emprego, pois "
                             "decorre de pressões salariais e margens de lucro que disputam a renda; o pleno emprego "
                             "a intensifica, mas não é condição necessária."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01433
    {
        "id": "ECO-E2-L01433-1", "fonte_ref": "E2-L01433", "destino": "37", "subtema": H2["infl"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("Julgue o item seguinte, a respeito da política monetária em diferentes períodos da economia "
                    "brasileira."),
        "rotulo_item": "Item",
        "assertiva": ("No governo Sarney, o diagnóstico da inflação elevada era de que seu determinante principal "
                      "era a inércia inflacionária e a solução ortodoxa levaria a uma enorme recessão sem ter "
                      "impactos significativos em reduzir seu patamar."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No governo Sarney, o diagnóstico da inflação elevada era de que seu determinante "
                      "<u>principal</u> era a <u>inércia inflacionária</u> e a solução ortodoxa levaria a uma "
                      "enorme recessão sem ter impactos significativos em reduzir seu patamar."),
        "poucas": ("O diagnóstico " + azb("inercialista") + " dominou a equipe do Cruzado: com indexação, a "
                   "inflação passada vira piso da futura, e a recessão ortodoxa custaria caro sem quebrar essa "
                   "memória. Daí o " + azb("choque heterodoxo") + "."),
        "destrinchando": [
            "Teoria da " + azb("inflação inercial") + ": numa economia indexada, π<sub>t</sub> ≈ π<sub>t−1</sub> "
            "+ choques. A demanda deixa de ser o motor; os contratos repetem a inflação passada, e choques "
            "(petróleo, câmbio, safra) mudam o patamar, que depois se perpetua.",
            "Autores: " + oc("Francisco Lopes") + " (choque heterodoxo: congelamento para zerar a inércia) e "
            + oc("Pérsio Arida") + " e " + oc("André Lara Resende") + " (proposta “Larida”: moeda indexada "
            "convivendo com o cruzeiro, ideia que antecipou a " + rx("URV") + " de 1994).",
            "Por que a ortodoxia falharia: em 1981–1983, os ajustes recessivos (a partir de 1983, sob acordo com o FMI) derrubaram o PIB e a "
            "inflação <b>não caiu</b> — subiu de cerca de " + vd("100%") + " para mais de " + vd("200%")
            + " ao ano. Era a evidência usada pelos inercialistas.",
            "Aplicação: " + rx("Plano Cruzado") + " (" + vd("fev./1986") + ") — troca de moeda, congelamento, "
            "fim da correção monetária, gatilho salarial. Deu certo por meses e ruiu com o excesso de demanda e "
            "os preços relativos desalinhados; seguiram-se Bresser (1987) e Verão (1989).",
            "Contraponto ortodoxo da época: o déficit público financiado por emissão seria a causa primária; sem "
            "ajuste fiscal, o congelamento só represaria preços.",
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item resume o diagnóstico da equipe econômica de 1985–1986. "
                       "A tentação de marcar ERRADO vem do tom forte (“enorme recessão”, “sem impactos "
                       "significativos”), mas é exatamente o argumento dos inercialistas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No governo Sarney, o diagnóstico dominante atribuía a inflação ao excesso de demanda, o que "
            "levou a um severo aperto monetário no Plano Cruzado.”</i> → ERRADO (troca de conceito: diagnóstico "
            "inercial, choque heterodoxo)",
            "<i>“O Plano Cruzado eliminou a correção monetária e congelou preços.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["principal"], "dificuldade": 1,
        "comentario_fonte": ("No governo Sarney predominava o diagnóstico de inflação inercial, propagada pela "
                             "indexação; políticas ortodoxas teriam alto custo recessivo sem quebrar a inércia, o "
                             "que justificou os planos heterodoxos (Lopes, Arida, Lara Resende)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0560
    {
        "id": "ECO-E1-0560-1", "fonte_ref": "E1-0560", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_METAS_BR,
        "rotulo_item": "Item",
        "assertiva": ("As medidas públicas que busquem afetar as expectativas dos agentes econômicos não são "
                      "efetivas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("As medidas públicas que busquem afetar as expectativas dos agentes econômicos ")
                    + vm("não são efetivas") + az(".")),
        "poucas": ("O regime de metas é, antes de tudo, um regime de " + azb("gestão de expectativas") + ": "
                   "meta anunciada, comunicação do BC e credibilidade são justamente os instrumentos que fazem a "
                   "inflação esperada convergir para a meta."),
        "destrinchando": [
            "Por que as expectativas importam: preços e salários são fixados olhando a inflação <b>futura</b>. "
            "Na " + azb("curva de Phillips com expectativas") + ", π = π<sup>e</sup> − β(u − u<sub>n</sub>) + "
            "choque; se π<sup>e</sup> está ancorada na meta, o BC precisa de menos juros e menos desemprego "
            "para levar a inflação até ela.",
            "Medidas que atuam sobre expectativas: anúncio de uma " + azb("meta numérica") + " (no " + rx("Brasil")
            + ", fixada pelo CMN), atas e comunicados do " + azb("Copom") + ", Relatório de Política Monetária, "
            + azb("forward guidance") + ", carta aberta quando a meta é descumprida e a "
            + azb("autonomia do BC") + " (" + vd("LC 179/2021") + ").",
            "O BC acompanha as expectativas pelo " + azb("Boletim Focus") + " e as usa como variável de "
            "decisão: desancoragem pede juros mais altos.",
            "Contraste: no modelo novo-clássico, só a política <b>não antecipada</b> afeta o produto; ainda "
            "assim, a política anunciada e crível afeta as expectativas de inflação — que é o ponto do item.",
            vm("Regra-âncora: em metas de inflação, ancorar expectativas é o canal central, não um acessório."),
        ],
        "dissecando": (cz("[contradição · modulador absoluto]") + " Nega o pilar do regime. A negação seca "
                       "(“não são efetivas”) é o sinal: em metas de inflação, credibilidade e comunicação são a "
                       "própria engrenagem da política."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de metas, a credibilidade do BC reduz o custo, em termos de produto, de levar a "
            "inflação à meta.”</i> → CERTO",
            "<i>“No regime de metas, o BC age apenas sobre a inflação corrente, sendo irrelevantes as "
            "expectativas.”</i> → ERRADO (restrição indevida)",
        ])],
        "reescrita": ("As medidas públicas que busquem afetar as expectativas dos agentes econômicos "
                      + hl("são efetivas") + "."),
        "tipo_erro": ["CONTRADICAO", "GENERALIZACAO"], "moduladores": ["não"], "dificuldade": 1,
        "comentario_fonte": ("No regime de metas, as expectativas são fundamentais; definição da meta e "
                             "comunicação do BC influenciam diretamente as expectativas de inflação."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0561
    {
        "id": "ECO-E1-0561-1", "fonte_ref": "E1-0561", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_METAS_BR,
        "rotulo_item": "Item",
        "assertiva": ("O compromisso do Banco Central com o combate à inflação tem impacto nulo na formação de "
                      "expectativas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O compromisso do Banco Central com o combate à inflação tem ") + vm("impacto nulo")
                    + az(" na formação de expectativas.")),
        "poucas": ("O compromisso crível do BC é o que " + azb("ancora as expectativas") + ": se o público "
                   "acredita que o BC fará o necessário, passa a esperar inflação na meta e fixa preços e "
                   "salários de acordo."),
        "destrinchando": [
            azb("Credibilidade") + " = probabilidade, atribuída pelo público, de que o BC cumpra o que anuncia. "
            "Ela se constrói com histórico (cumprir metas), instituições (mandato claro, autonomia, diretores "
            "com mandato fixo) e transparência (atas, relatórios, cartas abertas).",
            "Efeito prático: com expectativas ancoradas, choques de oferta passam pela inflação corrente sem "
            "contaminar a futura (menos efeitos de segunda ordem), e a " + azb("taxa de sacrifício")
            + " — produto perdido por ponto de desinflação — cai.",
            "Base teórica: " + oc("Kydland e Prescott") + " (1977) e " + oc("Barro e Gordon") + " (1983) "
            "mostraram que um BC sem compromisso tem incentivo a surpreender com inflação; o público antecipa "
            "e o resultado é inflação mais alta sem ganho de emprego. Compromisso e regras eliminam esse "
            + azb("viés inflacionário") + ".",
            "No " + rx("Brasil") + ", a " + vd("LC 179/2021") + " deu mandatos fixos e não coincidentes à "
            "diretoria do BC, reforçando o compromisso institucional com a meta.",
        ],
        "dissecando": (cz("[contradição · modulador absoluto]") + " “Impacto nulo” é absoluto e contraria o "
                       "núcleo do regime. Itens que zeram a importância de credibilidade ou expectativas em "
                       "metas de inflação são quase sempre ERRADOS."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Quanto maior a credibilidade do Banco Central, menor tende a ser a taxa de sacrifício da "
            "desinflação.”</i> → CERTO",
            "<i>“A credibilidade depende exclusivamente da independência formal do Banco Central.”</i> → ERRADO "
            "(modulador absoluto: depende também de histórico e transparência)",
        ])],
        "reescrita": ("O compromisso do Banco Central com o combate à inflação tem " + hl("impacto decisivo")
                      + " na formação de expectativas."),
        "tipo_erro": ["CONTRADICAO", "GENERALIZACAO"], "moduladores": ["nulo"], "dificuldade": 1,
        "comentario_fonte": ("A credibilidade do BC e seu compromisso com a meta são determinantes para a "
                             "ancoragem das expectativas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0562
    {
        "id": "ECO-E1-0562-1", "fonte_ref": "E1-0562", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": None, "cacd": False,
        "errei": False,
        "comando": CMD_METAS_BR,
        "rotulo_item": "Item",
        "assertiva": ("A redução do horizonte de segurança para o planejamento dos agentes econômicos contribui para "
                      "reforçar a crença nas expectativas geradas pelas autoridades."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A ") + vm("redução") + az(" do horizonte de segurança para o planejamento dos agentes "
                                                   "econômicos contribui para reforçar a crença nas expectativas "
                                                   "geradas pelas autoridades.")),
        "poucas": ("O regime de metas busca o contrário: " + azb("ampliar") + " o horizonte em que os agentes "
                   "planejam com segurança. Previsibilidade longa reforça a credibilidade; horizonte encurtado é "
                   "sinal de incerteza."),
        "destrinchando": [
            "Um dos ganhos esperados do regime de metas é a " + azb("previsibilidade") + ": meta conhecida com "
            "antecedência (no " + rx("Brasil") + ", fixada pelo CMN para anos à frente; desde " + vd("2025")
            + ", meta contínua de " + vd("3%") + " ⏳ (out/2026)), comunicação regular e coerência das decisões.",
            "Com horizonte longo e seguro, empresas e famílias firmam contratos mais longos, indexam menos e "
            "investem mais — e as expectativas convergem para o que a autoridade anuncia.",
            "Encurtar o horizonte é o sintoma das economias instáveis: na alta inflação brasileira, contratos "
            "eram curtíssimos, a indexação era quase diária, e ninguém acreditava nos anúncios oficiais.",
            "O item inverte o vínculo: menos segurança no planejamento <b>enfraquece</b> a crença nas "
            "expectativas oficiais.",
            vm("Regra-âncora: credibilidade cresce com previsibilidade — horizonte mais longo, não mais curto."),
        ],
        "dissecando": (cz("[inversão]") + " A frase é a versão espelhada da correta (“a ampliação do horizonte "
                       "de segurança … contribui para reforçar a crença”). Troca de uma palavra só; ler devagar "
                       "o substantivo que abre o item resolve."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A ampliação do horizonte de segurança para o planejamento dos agentes contribui para reforçar a "
            "crença nas expectativas geradas pelas autoridades.”</i> → CERTO",
            "<i>“Contratos mais curtos e indexação mais frequente indicam maior credibilidade da política "
            "monetária.”</i> → ERRADO (inversão: indicam desconfiança)",
        ])],
        "reescrita": ("A " + hl("ampliação") + " do horizonte de segurança para o planejamento dos agentes "
                      "econômicos contribui para reforçar a crença nas expectativas geradas pelas autoridades."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Reduzir o horizonte de planejamento gera incerteza; o que fortalece a ancoragem é "
                             "transparência, previsibilidade e compromisso com as metas."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0666
    {
        "id": "ECO-E1-0666-1", "fonte_ref": "E1-0666", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True,
        "errei": False,
        "comando": CMD_TPS25,
        "rotulo_item": "Item",
        "assertiva": ("Voltada a influenciar as expectativas de mercado em momentos de instabilidade, a Orientação "
                      "Futura (FG Forward Guidance) é uma estratégia de comunicação e uma ferramenta de política "
                      "monetária não convencional pela qual o banco central fornece informações acerca de suas "
                      "intenções em relação à política monetária."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Voltada a influenciar as expectativas de mercado em momentos de instabilidade, a Orientação "
                      "Futura (FG Forward Guidance) é uma <u>estratégia de comunicação</u> e uma ferramenta de "
                      "política monetária <u>não convencional</u> pela qual o banco central fornece informações "
                      "acerca de suas intenções em relação à política monetária."),
        "poucas": ("O " + azb("forward guidance") + " é o BC anunciando o caminho futuro dos juros para mover "
                   "hoje as expectativas e as taxas longas. Ganhou status de instrumento não convencional quando "
                   "os juros bateram no " + azb("limite inferior zero") + " após 2008."),
        "destrinchando": [
            "Mecanismo: os juros longos refletem a média dos juros curtos esperados (+ prêmio). Se o BC convence "
            "o mercado de que manterá a taxa básica baixa por muito tempo, os juros longos caem já, mesmo sem "
            "novo corte — estímulo pela " + azb("curva de juros") + ".",
            "Formas: " + azb("qualitativa/aberta") + " (“por um período prolongado”), " + azb("por data")
            + " (o Fed, em " + vd("ago./2011") + ", indicou juros mínimos “pelo menos até meados de 2013”) e "
            + azb("por condição") + " (em " + vd("dez./2012") + ", o Fed vinculou a alta de juros a desemprego "
            "abaixo de " + vd("6,5%") + ").",
            "Na tipologia de " + oc("Campbell e outros") + " (2012): FG " + azb("délfica") + " (previsão, "
            "sem compromisso) × " + azb("odisseica") + " (compromisso, como Ulisses amarrado ao mastro).",
            "No " + rx("Brasil") + ", o Copom adotou forward guidance em " + vd("ago./2020") + ", na pandemia, "
            "condicionado a expectativas de inflação abaixo da meta e ao regime fiscal; foi retirado em "
            + vd("jan./2021") + ", pouco antes do início do ciclo de alta dos juros.",
            "Limite: o FG depende de " + azb("credibilidade") + "; se o cenário muda e o BC rompe o anúncio, "
            "perde reputação — por isso a preferência por guias condicionais.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Definição de manual. As duas etiquetas "
                       "(“estratégia de comunicação” e “não convencional”) são verdadeiras ao mesmo tempo; o "
                       "candidato pode estranhar chamar comunicação de “ferramenta”, mas desde 2008 é "
                       "exatamente isso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O forward guidance exige a compra de ativos pelo banco central para produzir efeito sobre os "
            "juros longos.”</i> → ERRADO (troca de conceito: isso é QE; o FG age só pela comunicação)",
            "<i>“O forward guidance pode ser condicionado ao comportamento de variáveis como desemprego e "
            "inflação.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("FG é ferramenta não convencional de comunicação usada sobretudo com juros perto de "
                             "zero; anúncio de intenções futuras (Fed pós-2008, BCE, BCB na pandemia) que ancora "
                             "expectativas e estimula sem mexer de imediato nos juros."),
        "qualidade_fonte": "bom",
        "figuras_fonte": img_e1("image (204).png"),
        "alertas": [ALERTA_TPS25],
    },
    # ------------------------------------------------------------------ E1-0702
    {
        "id": "ECO-E1-0702-1", "fonte_ref": "E1-0702", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca do regime de metas de inflação, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em regimes de metas de inflação, a política monetária atua principalmente por meio da "
                      "manipulação da taxa de juros de curto prazo, influenciando expectativas de inflação e "
                      "decisões de consumo e investimento."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em regimes de metas de inflação, a política monetária atua <u>principalmente</u> por meio "
                      "da manipulação da <u>taxa de juros de curto prazo</u>, influenciando expectativas de "
                      "inflação e decisões de consumo e investimento."),
        "poucas": ("O instrumento do regime de metas é a " + azb("taxa básica de juros") + " de curto prazo (no "
                   + rx("Brasil") + ", a meta da Selic). Dela partem os " + azb("canais de transmissão")
                   + " que chegam à demanda e aos preços."),
        "destrinchando": [
            "Canais de transmissão da Selic: " + azb("juros/custo de capital") + " (consumo e investimento), "
            + azb("crédito") + " (oferta e custo dos empréstimos), " + azb("preços de ativos")
            + " (efeito riqueza), " + azb("câmbio") + " (juros altos atraem capital, apreciam o real e barateiam "
            "importados) e " + azb("expectativas") + ".",
            "Defasagem: a política monetária leva vários trimestres para afetar a atividade e ainda mais "
            "para a inflação; por isso o BC decide olhando o " + azb("horizonte relevante") + " (cerca de 18 "
            "meses à frente), não a inflação do mês.",
            "Os agregados monetários (M1, M2) viram variáveis <b>endógenas</b>: o BC fixa o preço (juros) e "
            "deixa a quantidade de moeda se ajustar, porque a demanda por moeda é instável.",
            "O open market é o meio operacional de fazer a Selic efetiva bater a meta; compulsório e redesconto "
            "são acessórios, usados mais para estabilidade financeira.",
            vm("Regra-âncora: metas de inflação = juros como instrumento, inflação esperada como meta "
               "intermediária implícita."),
        ],
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de manual com o modulador "
                       "“principalmente”, que admite outros instrumentos. O item seria ERRADO se trocasse juros "
                       "por “controle dos agregados monetários”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regimes de metas de inflação, a política monetária atua principalmente pelo controle da base "
            "monetária.”</i> → ERRADO (troca de conceito: isso é o regime de metas monetárias)",
            "<i>“Os efeitos de uma alta de juros sobre a inflação manifestam-se com defasagem.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["principalmente"], "dificuldade": 1,
        "comentario_fonte": ("No regime de metas, a taxa de juros de curto prazo (Selic) é o principal "
                             "instrumento; transmite-se por crédito, expectativas, preços de ativos e câmbio."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00312
    {
        "id": "ECO-E2-L00312-1", "fonte_ref": "E2-L00312", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": ("Acerca do regime de metas de inflação e dos canais de transmissão da política monetária, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("No regime de metas de inflação, choques cambiais têm impacto apenas indireto sobre a "
                      "inflação, pois o canal de câmbio influencia apenas exportações líquidas, sem afetar "
                      "diretamente preços domésticos."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime de metas de inflação, choques cambiais têm impacto ") + vm("apenas indireto")
                    + az(" sobre a inflação, pois o canal de câmbio influencia ") + vm("apenas")
                    + az(" exportações líquidas, ") + vm("sem afetar") + az(" diretamente preços domésticos.")),
        "poucas": ("O câmbio age por duas vias: a " + azb("direta") + " — o " + azb("repasse cambial")
                   + " (pass-through) aos preços de importados e insumos — e a " + azb("indireta")
                   + ", pela demanda agregada via exportações líquidas."),
        "destrinchando": [
            "<b>Efeito direto</b>: uma depreciação encarece em reais tudo o que é importado ou cotado em "
            "dólar — combustíveis, trigo, fertilizantes, eletrônicos, commodities agrícolas exportáveis. Os "
            "índices de preços sobem em semanas, sem passar pela demanda.",
            "<b>Efeito indireto</b>: o real mais fraco torna exportações mais competitivas e importações mais "
            "caras → exportações líquidas e demanda agregada sobem → pressão sobre o hiato e a inflação, com "
            "defasagem maior.",
            "O tamanho do " + azb("pass-through") + " depende do grau de abertura, da composição do índice "
            "(peso de comercializáveis), do estado do ciclo e da " + azb("credibilidade") + " do BC: com "
            "expectativas ancoradas, o repasse é menor e mais curto.",
            "No " + rx("Brasil") + ", o canal cambial é dos mais rápidos e potentes; foi decisivo em "
            + vd("2002") + " (depreciação forte e IPCA de " + vd("12,5%") + ") e em " + vd("2015") + ".",
            "Ligação com os juros: alta da Selic atrai capital, aprecia o real e derruba a inflação pelo canal "
            "direto — por isso o câmbio é visto como um dos canais de transmissão mais eficazes da política "
            "monetária em economias emergentes.",
        ],
        "dissecando": (cz("[restrição indevida · meia-verdade]") + " O efeito via exportações líquidas existe "
                       "(é a parte verdadeira), mas os dois “apenas” cortam fora o repasse direto, que é o canal "
                       "mais rápido. Item com dois “apenas” num tema de transmissão costuma ser ERRADO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O repasse cambial tende a ser menor quando as expectativas de inflação estão ancoradas.”</i> → "
            "CERTO",
            "<i>“Uma apreciação cambial pressiona a inflação para cima pelo canal direto.”</i> → ERRADO "
            "(inversão: barateia importados e reduz a inflação)",
        ])],
        "reescrita": ("No regime de metas de inflação, choques cambiais têm impacto " + hl("direto e indireto")
                      + " sobre a inflação, pois o canal de câmbio influencia " + hl("não só")
                      + " exportações líquidas, " + hl("mas também") + " diretamente preços domésticos."),
        "tipo_erro": ["RESTRICAO", "MEIA_VERDADE"], "moduladores": ["apenas"], "dificuldade": 1,
        "comentario_fonte": ("O canal cambial tem impactos diretos (preço de importados e insumos) e indiretos "
                             "(demanda agregada via exportações líquidas)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00317
    {
        "id": "ECO-E2-L00317-1", "fonte_ref": "E2-L00317", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca das políticas monetárias não convencionais, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A “orientação futura” (forward guidance) é classificada como política não convencional "
                      "porque visa afetar expectativas sobre juros futuros, alterando juros de longo prazo mesmo "
                      "sem necessidade de expansão do balanço do banco central."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A “orientação futura” (forward guidance) é classificada como política não convencional "
                      "porque visa afetar <u>expectativas sobre juros futuros</u>, alterando juros de longo prazo "
                      "<u>mesmo sem necessidade de expansão do balanço</u> do banco central."),
        "poucas": ("O " + azb("forward guidance") + " é só comunicação: ao prometer juros curtos baixos por mais "
                   "tempo, derruba os juros longos esperados. Diferente do " + azb("QE") + ", não exige comprar "
                   "ativos nem inchar o balanço."),
        "destrinchando": [
            "Pela " + azb("hipótese das expectativas") + " da estrutura a termo, a taxa longa ≈ média das curtas "
            "esperadas + prêmio de prazo. O FG atua na <b>média esperada</b>; o QE atua sobretudo no "
            "<b>prêmio</b>, retirando duration do mercado.",
            "Por que “não convencional”: a política convencional mexe na taxa curta <b>de hoje</b>. Quando ela "
            "chega a zero (" + azb("zero lower bound") + "), o BC passa a mexer na trajetória <b>esperada</b> — "
            "o FG — ou no próprio balanço — o QE.",
            "Os instrumentos se combinam: o Fed usou FG e QE juntos de " + vd("2008") + " a " + vd("2014")
            + "; o BCE adotou FG em " + vd("jul./2013") + " e QE em " + vd("2015") + ".",
            "Ressalva: hoje muitos BCs fazem comunicação prospectiva também em tempos normais, o que borra a "
            "fronteira; mas a classificação de manual, nascida da crise de 2008, é a do item.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " O detalhe “sem expansão do balanço” é o que distingue "
                       "FG de QE e é verdadeiro. A banca trocaria um pelo outro para fabricar o erro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O forward guidance atua por meio da compra de títulos longos, reduzindo o prêmio de "
            "prazo.”</i> → ERRADO (troca de conceito: isso é QE)",
            "<i>“O forward guidance é tanto mais eficaz quanto maior a credibilidade do banco central.”</i> → "
            "CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["mesmo sem"], "dificuldade": 1,
        "comentario_fonte": "Forward guidance tornou-se ferramenta não convencional após 2008, com o Fed e o BCE.",
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00385
    {
        "id": "ECO-E2-L00385-1", "fonte_ref": "E2-L00385", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca de regras e discricionariedade na política monetária, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("No modelo de inconsistência temporal de Kydland e Prescott (e Barro-Gordon), a autoridade "
                      "monetária que opera com discricionariedade tende a gerar um viés inflacionário positivo, pois "
                      "tenta explorar a Curva de Phillips de curto prazo para reduzir o desemprego abaixo da taxa "
                      "natural. A solução proposta para eliminar esse viés é o comprometimento via regras ou a "
                      "delegação da política a um Banco Central conservador e independente."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("No modelo de inconsistência temporal de Kydland e Prescott (e Barro-Gordon), a autoridade "
                      "monetária que opera com <u>discricionariedade</u> tende a gerar um <u>viés inflacionário "
                      "positivo</u>, pois tenta explorar a Curva de Phillips de curto prazo para reduzir o "
                      "desemprego abaixo da taxa natural. A solução proposta para eliminar esse viés é o "
                      "comprometimento via regras ou a delegação da política a um Banco Central conservador e "
                      "independente."),
        "poucas": ("Com discricionariedade, o BC tem incentivo a surpreender com inflação para baixar o "
                   "desemprego; o público, racional, antecipa. Resultado: " + azb("inflação mais alta")
                   + " e desemprego na taxa natural. Regras ou BC independente e conservador eliminam o viés."),
        "destrinchando": [
            azb("Inconsistência temporal") + " (" + oc("Kydland e Prescott") + ", " + vd("1977") + "): o plano "
            "ótimo anunciado hoje (inflação baixa) deixa de ser ótimo amanhã, depois que as expectativas se "
            "fixaram — aí vale a pena surpreender. Como o público sabe disso, não acredita no anúncio.",
            "Versão de " + oc("Barro e Gordon") + " (" + vd("1983") + "): o BC quer desemprego abaixo da taxa "
            "natural (meta ambiciosa). No equilíbrio discricionário, a inflação sobe até o ponto em que o custo "
            "marginal de mais inflação iguala o ganho de surpreender; como não há surpresa, o desemprego fica "
            "em u<sub>n</sub> e sobra só o " + azb("viés inflacionário") + ".",
            "Soluções: (1) " + azb("regras") + " críveis com custo de abandono (reputação, regime de metas); (2) "
            + azb("banqueiro central conservador") + " (" + oc("Rogoff") + ", " + vd("1985") + "), que pesa "
            "mais a inflação que a sociedade; (3) " + azb("independência") + " legal, que isola o BC do ciclo "
            "eleitoral; (4) contratos de desempenho (" + oc("Walsh") + ").",
            "Reconhecimento: Kydland e Prescott receberam o " + vd("Nobel de 2004") + ". A tese embasou a onda "
            "de independência de BCs nos anos 1990 e, no " + rx("Brasil") + ", a autonomia formal pela "
            + vd("LC 179/2021") + ".",
            "Custo da solução de Rogoff: um BC muito conservador estabiliza menos o produto diante de choques "
            "de oferta — troca-se viés por menos flexibilidade.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Síntese fiel da literatura. Item longo, "
                       "com quatro afirmações verificáveis (discricionariedade, viés positivo, motivo, solução); "
                       "a banca costuma errar trocando “regras” por “discricionariedade” ou dizendo que o "
                       "desemprego cai de forma permanente."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No modelo de Barro-Gordon, a discricionariedade gera inflação mais alta, mas reduz "
            "permanentemente o desemprego abaixo da taxa natural.”</i> → ERRADO (nexo indevido: com expectativas "
            "racionais, não há ganho de emprego)",
            "<i>“Segundo Rogoff, a sociedade ganha ao delegar a política a um banqueiro central mais avesso à "
            "inflação que ela própria.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": ["tende a"], "dificuldade": 2,
        "comentario_fonte": ("Inconsistência temporal: BCs discricionários geram inflação sem ganho de emprego no "
                             "longo prazo, pois as expectativas racionais antecipam a inflação; solução é amarrar "
                             "as mãos do BC (regras ou independência)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00386
    {
        "id": "ECO-E2-L00386-1", "fonte_ref": "E2-L00386", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Acerca do regime de metas de inflação, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de Metas de Inflação, quando ocorre um choque de oferta negativo e persistente "
                      "(como um aumento estrutural no preço do petróleo), a resposta ótima do Banco Central, "
                      "visando minimizar a volatilidade do produto e da inflação, é acomodar integralmente o choque "
                      "no primeiro momento, alterando a meta de inflação para cima, a fim de evitar qualquer custo "
                      "em termos de hiato do produto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em um regime de Metas de Inflação, quando ocorre um choque de oferta negativo e persistente "
                       "(como um aumento estrutural no preço do petróleo), a resposta ótima do Banco Central, "
                       "visando minimizar a volatilidade do produto e da inflação, é ")
                    + vm("acomodar integralmente o choque no primeiro momento, alterando a meta de inflação para "
                         "cima, a fim de evitar qualquer custo") + az(" em termos de hiato do produto.")),
        "poucas": ("A resposta de manual é " + azb("acomodar os efeitos primários") + " e " + azb("combater os "
                   "secundários") + ", mantendo a meta e alongando o prazo de convergência. Mudar a meta para "
                   "cima destrói credibilidade, e nenhum caminho zera o custo em produto."),
        "destrinchando": [
            "O choque de oferta negativo cria um " + azb("dilema") + ": inflação sobe e produto cai ao mesmo "
            "tempo. Combater tudo de imediato aprofunda a recessão; acomodar tudo deixa a inflação contaminar "
            "expectativas e salários.",
            azb("Efeitos primários") + " (de 1ª ordem): a alta direta do preço do petróleo e dos derivados — "
            "o BC pode deixá-los passar, porque são mudança de preço relativo. " + azb("Efeitos secundários")
            + " (de 2ª ordem): o contágio a outros preços, salários e expectativas — estes o BC combate com "
            "juros.",
            "Instrumento de flexibilidade: o " + azb("horizonte de convergência") + ". No " + rx("Brasil")
            + ", o BC já usou trajetórias ajustadas e prazos mais longos (2003, por exemplo); desde "
            + vd("2025") + ", com a " + azb("meta contínua") + ", o descumprimento é aferido quando a inflação "
            "fica fora do intervalo por seis meses seguidos, e o BC explica em nota e carta aberta como "
            "voltará à meta ⏳ (out/2026).",
            "Alterar a meta em reação a choque é o pior caminho: sinaliza que a meta é negociável, desancora "
            "expectativas e eleva o custo de toda desinflação futura.",
            vm("Regra-âncora: choque de oferta → acomoda o efeito direto, combate o contágio; a meta fica onde "
               "está."),
        ],
        "dissecando": (cz("[meia-verdade · modulador absoluto]") + " Começa certo (há trade-off, o objetivo é "
                       "minimizar volatilidade) e enxerta três erros na receita: “integralmente”, “alterando a "
                       "meta” e “qualquer custo”. Absolutos em resposta “ótima” a choque de oferta são o sinal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Diante de choque de oferta, o BC pode acomodar os efeitos primários sobre os preços, mas deve "
            "combater os efeitos secundários.”</i> → CERTO",
            "<i>“Diante de choque de oferta negativo, o BC deve trazer a inflação à meta no mesmo ano, "
            "qualquer que seja o custo em produto.”</i> → ERRADO (modulador absoluto: ignora a "
            "flexibilidade do horizonte)",
        ])],
        "reescrita": ("Em um regime de Metas de Inflação, quando ocorre um choque de oferta negativo e persistente "
                      "(como um aumento estrutural no preço do petróleo), a resposta ótima do Banco Central, "
                      "visando minimizar a volatilidade do produto e da inflação, é "
                      + hl("acomodar apenas os efeitos primários do choque e combater os secundários, mantendo a "
                           "meta e alongando o prazo de convergência, aceitando algum custo")
                      + " em termos de hiato do produto."),
        "tipo_erro": ["MEIA_VERDADE", "GENERALIZACAO"], "moduladores": ["integralmente", "qualquer"],
        "dificuldade": 2,
        "comentario_fonte": ("Diante de choque de oferta há trade-off; a resposta ótima é a convergência gradual "
                             "ou o alongamento do horizonte, não a mudança da meta para cima nem a acomodação "
                             "total imediata."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00614
    {
        "id": "ECO-E2-L00614-1", "fonte_ref": "E2-L00614", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_NAB_MON,
        "rotulo_item": "Item",
        "assertiva": ("A adoção do regime de metas de inflação pressupõe controle direto da quantidade de moeda em "
                      "circulação como instrumento central de política monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A adoção do regime de metas de inflação pressupõe ")
                    + vm("controle direto da quantidade de moeda em circulação")
                    + az(" como instrumento central de política monetária.")),
        "poucas": ("O instrumento central das metas de inflação é a " + azb("taxa de juros de curto prazo")
                   + " (a Selic). Controlar a quantidade de moeda é a marca do regime de " + azb("metas "
                   "monetárias") + ", abandonado pela instabilidade da demanda por moeda."),
        "destrinchando": [
            "Três âncoras nominais clássicas: " + azb("metas monetárias") + " (crescimento de M fixado; "
            + oc("Friedman") + "), " + azb("âncora cambial") + " (paridade fixa ou administrada) e "
            + azb("metas de inflação") + " (a própria inflação é a meta; os juros são o instrumento).",
            "Por que os agregados saíram de cena: inovação financeira e mudanças de portfólio tornaram a "
            + azb("velocidade da moeda") + " instável nos anos 1980; cumprir a meta de M deixou de garantir a "
            "inflação. A Nova Zelândia inaugurou as metas de inflação em " + vd("1990") + "; o " + rx("Brasil")
            + " as adotou em " + vd("jun./1999") + " (Decreto 3.088), após a flutuação do real.",
            "Com juros como instrumento, a oferta de moeda vira " + azb("endógena") + ": o BC provê as reservas "
            "que os bancos demandam à taxa-meta, via open market.",
            "Pegadinha vizinha: “metas de inflação usam a taxa de câmbio como âncora” — também ERRADO; o "
            "câmbio flutua (com intervenções pontuais).",
            vm("Regra-âncora: metas de inflação → preço do dinheiro (juros); metas monetárias → quantidade "
               "(agregados)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Atribui ao regime de metas de inflação o instrumento do "
                       "regime de metas monetárias. A pista é “controle direto da quantidade de moeda”: em metas "
                       "de inflação o BC controla o preço (juros), não a quantidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de metas de inflação, os agregados monetários tornam-se variáveis endógenas, "
            "ajustando-se à taxa de juros fixada.”</i> → CERTO",
            "<i>“O regime de metas de inflação exige câmbio fixo como âncora nominal.”</i> → ERRADO (troca de "
            "conceito: âncora cambial)",
        ])],
        "reescrita": ("A adoção do regime de metas de inflação pressupõe "
                      + hl("a fixação da taxa de juros de curto prazo")
                      + " como instrumento central de política monetária."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Metas de inflação usam a taxa de juros de curto prazo (Selic) como instrumento; "
                             "controle de agregados é próprio do regime de metas monetárias, abandonado pela baixa "
                             "eficácia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01039
    {
        "id": "ECO-E2-L01039-1", "fonte_ref": "E2-L01039", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_NAB_MF,
        "rotulo_item": "Item",
        "assertiva": ("Em relação ao sistema de metas de inflação adotado no Brasil em 1999, a função básica do "
                      "BACEN e da política monetária passa a ser o cumprimento da meta estipulada pelo COPOM."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Em relação ao sistema de metas de inflação adotado no Brasil em 1999, a função básica do "
                       "BACEN e da política monetária passa a ser o cumprimento da meta estipulada pelo ")
                    + vm("COPOM") + az(".")),
        "poucas": ("Quem fixa a " + azb("meta de inflação") + " é o " + vd("CMN") + "; o " + azb("Copom")
                   + ", órgão do BC, fixa a " + azb("meta da Selic") + " para cumprir a meta do CMN."),
        "destrinchando": [
            "Divisão de tarefas no " + rx("Brasil") + " (" + vd("Decreto 3.088/1999") + ", hoje " + vd("Decreto "
            "12.079/2024") + "): o " + azb("Conselho Monetário Nacional") + " — Ministro da Fazenda, Ministro "
            "do Planejamento e Presidente do BC — define a meta e o intervalo de tolerância; o "
            + azb("Banco Central") + " executa a política para cumpri-la.",
            "O " + azb("Copom") + " (Presidente e diretores do BC) reúne-se " + vd("8 vezes por ano")
            + " (a cada 45 dias, aproximadamente) e fixa a meta da Selic. Ele escolhe o <b>instrumento</b>, "
            "não o <b>objetivo</b>: é a distinção entre " + azb("independência de instrumento") + " (o BC "
            "tem) e independência de objetivo (o BC não tem; a meta é do governo, via CMN).",
            "Índice de referência: " + azb("IPCA") + " (IBGE). Meta atual: " + vd("3%") + ", com tolerância "
            "de ±" + vd("1,5 p.p.") + ", em regime de " + azb("meta contínua") + " desde " + vd("2025")
            + " ⏳ (out/2026).",
            "A " + vd("LC 179/2021") + " (autonomia do BC) manteve essa arquitetura: objetivo fundamental de "
            "estabilidade de preços, com metas fixadas pelo CMN.",
            vm("Regra-âncora: CMN fixa a meta de inflação; Copom fixa a Selic para atingi-la."),
        ],
        "dissecando": (cz("[troca de ator]") + " Tudo certo, salvo o órgão: troca o CMN pelo Copom, vizinho "
                       "institucional que também decide “metas” — mas a da Selic. 🔥 Troca CMN × Copom é "
                       "recorrente em itens sobre o regime brasileiro."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime brasileiro de metas, o Copom fixa a meta para a taxa Selic com vistas a cumprir a "
            "meta de inflação definida pelo CMN.”</i> → CERTO",
            "<i>“O CMN é composto pelo Presidente do Banco Central e por seus diretores.”</i> → ERRADO (troca de "
            "ator: essa é a composição do Copom)",
        ])],
        "reescrita": ("Em relação ao sistema de metas de inflação adotado no Brasil em 1999, a função básica do "
                      "BACEN e da política monetária passa a ser o cumprimento da meta estipulada pelo "
                      + hl("CMN") + "."),
        "tipo_erro": ["TROCA_ATOR"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A meta de inflação é definida pelo CMN e cabe ao BC alcançá-la; o Copom define a "
                             "Selic a cada 45 dias visando à meta do CMN."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01040
    {
        "id": "ECO-E2-L01040-1", "fonte_ref": "E2-L01040", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_NAB_MF,
        "rotulo_item": "Item",
        "assertiva": ("O instrumento para alcance da meta de inflação é a taxa referencial de juros e as operações "
                      "de mercado aberto."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O instrumento para alcance da meta de inflação é a taxa ") + vm("referencial")
                    + az(" de juros ") + vm("e as") + az(" operações de mercado aberto.")),
        "poucas": ("O instrumento é a " + azb("taxa básica de juros (Selic)") + ". A " + azb("Taxa Referencial "
                   "(TR)") + " é outra coisa, e o open market não é instrumento paralelo: é o meio operacional "
                   "que mantém a Selic na meta."),
        "destrinchando": [
            "Hierarquia: <b>objetivo</b> = meta de inflação (CMN) → <b>instrumento</b> = meta da Selic (Copom) "
            "→ <b>operação</b> = compra e venda de títulos públicos no open market (mesa do BC), que faz a "
            + azb("Selic efetiva") + " bater a meta.",
            "A " + azb("Selic") + " é a taxa média dos financiamentos de um dia lastreados em títulos federais "
            "registrados no " + azb("Sistema Especial de Liquidação e de Custódia") + " — daí o nome.",
            "A " + azb("TR") + " foi criada pela " + vd("MP 294/1991") + " (Plano Collor II) para substituir "
            "índices de correção; hoje corrige poupança e FGTS e passou anos zerada. Não é instrumento de "
            "política monetária.",
            "Somar “e as operações de mercado aberto” ao instrumento confunde nível operacional e nível de "
            "política: o open market existia também nas metas monetárias, com outro alvo.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O erro decisivo é “taxa referencial”, que remete à TR, e não "
                       "à taxa básica; a soma com o open market reforça a confusão entre instrumento e "
                       "operação. Leitura caridosa (“referencial” = “de referência”) tornaria o item defensável, "
                       "mas a fonte o dá como ERRADO pelo termo técnico."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O Banco Central utiliza operações de mercado aberto para manter a taxa Selic efetiva próxima "
            "da meta definida pelo Copom.”</i> → CERTO",
            "<i>“A Taxa Referencial é o principal instrumento do regime de metas de inflação.”</i> → ERRADO "
            "(troca de conceito: é a Selic)",
        ])],
        "reescrita": ("O instrumento para alcance da meta de inflação é a taxa " + hl("básica") + " de juros "
                      + hl("(Selic), que o BC mantém na meta por meio das") + " operações de mercado aberto."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Definida a Selic, o BC atua diariamente com operações de mercado aberto para mantê-la "
                             "próxima da meta; a TR, criada pela MP 294/1991 (Collor II), corrige poupança e FGTS."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: gabarito ERRADO depende de ler “taxa referencial” como a TR; o comentário "
                    "registra a leitura alternativa"],
    },
    # ------------------------------------------------------------------ E2-L01230
    {
        "id": "ECO-E2-L01230-1", "fonte_ref": "E2-L01230", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_NAB_MON,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a regra de política monetária proposta por John B. Taylor, conhecida como "
                      "“regra de Taylor”, se o hiato do produto é zero e a taxa de inflação sobe 1 ponto "
                      "percentual, o Banco Central deve aumentar a taxa nominal de juros em mais do que 1 ponto "
                      "percentual."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a regra de política monetária proposta por John B. Taylor, conhecida como "
                      "“regra de Taylor”, se o hiato do produto é zero e a taxa de inflação sobe 1 ponto "
                      "percentual, o Banco Central deve aumentar a taxa nominal de juros em <u>mais do que 1 ponto "
                      "percentual</u>."),
        "poucas": ("É o " + azb("princípio de Taylor") + ": a taxa nominal deve subir mais que a inflação, para "
                   "que a " + azb("taxa real") + " suba e contenha a demanda. Na regra original, a resposta é "
                   + vd("1,5 p.p.") + " por ponto de inflação."),
        "destrinchando": [
            "Regra original (" + oc("John B. Taylor") + ", " + vd("1993") + "): i = π + 0,5·(π − 2%) + 0,5·hiato "
            "+ 2%. Com hiato zero, ∂i/∂π = 1 + 0,5 = " + vd("1,5") + ".",
            "Lógica: a demanda depende do juro <b>real</b> (r = i − π). Se a inflação sobe 1 p.p. e o juro "
            "nominal sobe só 1 p.p., o juro real fica igual e nada freia a inflação; se sobe menos de 1, o juro "
            "real <b>cai</b> e a política fica mais frouxa justamente quando deveria apertar — instabilidade.",
            "Evidência: " + oc("Clarida, Galí e Gertler") + " (2000) estimaram que o Fed respondia com "
            "coeficiente menor que 1 nos anos 1970 (grande inflação) e maior que 1 na era " + oc("Volcker")
            + "–" + oc("Greenspan") + " (estabilidade).",
            "A regra é descritiva e normativa ao mesmo tempo: aproxima o comportamento observado dos BCs e "
            "serve de referência para avaliar se a política está apertada ou frouxa.",
            vm("Regra-âncora: coeficiente da inflação > 1 na regra de Taylor = juro real sobe quando a inflação "
               "sobe."),
        ],
        "dissecando": (cz("[detalhe · contraintuitivo]") + " Quem lê “inflação sobe 1, juro sobe 1” como "
                       "resposta “proporcional” acha que mais que 1 é exagero. O detalhe decisivo é o juro "
                       "real: só a resposta mais que proporcional o eleva."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela regra de Taylor, se a inflação sobe 1 p.p. com hiato nulo, o BC deve elevar a taxa nominal "
            "em exatamente 1 p.p., mantendo constante a taxa real.”</i> → ERRADO (dado alterado: mais que 1)",
            "<i>“Na regra de Taylor, com inflação na meta, um hiato do produto positivo pede elevação dos "
            "juros.”</i> → CERTO",
        ])],
        "tipo_erro": ["DETALHE", "CONTRAINTUITIVO"], "moduladores": ["mais do que"], "dificuldade": 2,
        "comentario_fonte": ("Regra de Taylor: r − r* = a(p − p*) + b(y − y*); o princípio de Taylor manda elevar "
                             "o juro nominal mais que proporcionalmente à inflação, elevando o juro real; caso "
                             "contrário, a inflação não converge."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01231
    {
        "id": "ECO-E2-L01231-1", "fonte_ref": "E2-L01231", "destino": "38", "subtema": H2["metas"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False,
        "errei": False,
        "comando": CMD_NAB_MON,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a regra de política monetária conhecida como Regra de Taylor, o Banco Central "
                      "deve alterar a taxa de juros nominal em resposta ao desvio da taxa de inflação em relação à "
                      "meta de inflação e em resposta ao desvio da taxa de desemprego (corrente) em relação à taxa "
                      "natural de desemprego (ou em resposta ao desvio do produto corrente em relação ao produto "
                      "potencial)."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a regra de política monetária conhecida como Regra de Taylor, o Banco Central "
                      "deve alterar a taxa de juros nominal em resposta ao <u>desvio da taxa de inflação em "
                      "relação à meta</u> de inflação e em resposta ao <u>desvio da taxa de desemprego</u> "
                      "(corrente) em relação à taxa natural de desemprego (ou em resposta ao desvio do produto "
                      "corrente em relação ao produto potencial)."),
        "poucas": ("A regra de Taylor tem " + azb("dois gatilhos") + ": o " + azb("hiato de inflação")
                   + " (π − π*) e o " + azb("hiato do produto") + " (ou, equivalentemente pela lei de Okun, o "
                   "desvio do desemprego da taxa natural)."),
        "destrinchando": [
            "Versão de " + oc("Blanchard") + ": i<sub>t</sub> = i* + a(π<sub>t</sub> − π*) − b(u<sub>t</sub> − "
            "u<sub>n</sub>), com a, b > 0. Inflação acima da meta → juros sobem; desemprego acima da taxa natural "
            "→ juros caem (por isso o sinal negativo).",
            "Versão com produto: i = r* + π + a(π − π*) + b(y − y*). Os dois formatos se equivalem pela "
            + azb("lei de Okun") + ": hiato do produto positivo ↔ desemprego abaixo do natural.",
            "Os pesos a e b medem as preferências do BC: a grande = foco na inflação; b grande = mais atenção à "
            "atividade. Um BC de " + azb("meta flexível") + " tem b > 0; uma meta “estrita” teria b ≈ 0.",
            "Leitura prática: o termo constante (i* ou r* + π*) é a " + azb("taxa neutra") + " — a que vigora "
            "com inflação na meta e economia no potencial. Política contracionista = juro acima do neutro.",
        ],
        "dissecando": (cz("[literalidade · paráfrase fiel]") + " Descrição completa da regra, inclusive com a "
                       "equivalência desemprego × produto entre parênteses. A banca costuma errar retirando um "
                       "dos dois hiatos (“apenas ao desvio da inflação”) ou invertendo o sinal da resposta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pela regra de Taylor, o BC deve reagir exclusivamente ao desvio da inflação em relação à "
            "meta.”</i> → ERRADO (restrição indevida: há também o hiato do produto)",
            "<i>“Pela regra de Taylor, desemprego acima da taxa natural pede elevação dos juros.”</i> → ERRADO "
            "(inversão: pede redução)",
        ])],
        "tipo_erro": ["LITERAL", "PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Regra de Taylor: i = i* + a(π − π*) − b(u − uₙ); i* é a taxa nominal associada à "
                             "meta; o último termo é o desvio do desemprego da taxa natural."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 212", "tipo_fonte": "FÓRMULA", "lado": "verso",
                           "acao": "texto (fórmula transcrita no 📖)"}],
        "alertas": [],
    },
]
