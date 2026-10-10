"""Cards do lote de redação 08 — ECO, passada 03 (notas 66: câmbio e política cambial; 67: reservas)."""
from marcacao import az, vm, azb, vd, oc, rx, cz, hl

H2 = {
    "reg": "💱 Regimes cambiais",
    "ppc": "📏 Câmbio nominal × real e PPC",
    "det": "📈 Determinantes do câmbio",
    "res": "📘 Reservas e intervenção",
}

CMD_RT_ABERTA = "A respeito dos conceitos e teorias da macroeconomia aberta, julgue o item a seguir."

CMD_RT_ECO_ABERTA = "Sobre os conceitos e teorias da economia aberta, julgue o item a seguir."

CMD_NAB_ABERTA = "A respeito dos conceitos de macroeconomia aberta, julgue o item a seguir."

CMD_NIDI_25 = ("A globalização do espaço econômico torna o estudo da economia internacional cada vez mais relevante "
               "para o entendimento das relações de comércio entre as nações. A esse respeito, julgue o item a "
               "seguir.")

CMD_TPS25 = "Acerca de regimes cambiais e da atuação do Banco Central no mercado de câmbio, julgue o item a seguir."

ALERTA_TPS25 = ("texto_parcial: o comando original (“A partir do texto apresentado”) remete a um texto-base que não "
                "veio na fonte; comando neutralizado, e o item se julga sem o texto")

CMD_CLIP = "Acerca de regimes cambiais e do uso das reservas internacionais, julgue o item a seguir."

CARDS = [
    # ------------------------------------------------------------------ E2-L01157
    {
        "id": "ECO-E2-L01157-1", "fonte_ref": "E2-L01157", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": ("Com relação ao comércio internacional e aos instrumentos de política comercial, julgue o item "
                    "a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("A recente valorização do real frente ao dólar, com a melhora da percepção de risco do país, é "
                      "benéfica para a indústria local, já que encarece as importações e torna mais competitivos os "
                      "produtos brasileiros no exterior."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A recente valorização do real frente ao dólar, com a melhora da percepção de risco do país, "
                       "é ") + vm("benéfica para a") + az(" indústria local, já que ") + vm("encarece")
                    + az(" as importações e torna ") + vm("mais") + az(" competitivos os produtos brasileiros no "
                                                                        "exterior.")),
        "poucas": ("Real valorizado = " + azb("dólar mais barato") + ": importados ficam mais baratos e os "
                   "produtos brasileiros ficam mais caros lá fora. A indústria que compete com importações e a que "
                   "exporta <b>perdem</b> competitividade."),
        "destrinchando": [
            "Convenção brasileira: a taxa de câmbio nominal é cotada em " + vd("R$ por US$") + ". "
            + azb("Valorização (apreciação)") + " do real = a taxa <b>cai</b> (ex.: de R$ 5,50 para R$ 5,00 por "
            "dólar); " + azb("desvalorização (depreciação)") + " = a taxa <b>sobe</b>.",
            "Efeito sobre preços relativos: um bem importado de US$ 100 custava R$ 550 e passa a custar R$ 500 — "
            "a importação <b>barateia</b>. Um bem exportado de R$ 550 custava US$ 100 lá fora e passa a custar "
            "US$ 110 — o produto nacional <b>encarece</b> no exterior.",
            "Para a indústria de transformação, que concorre com importados no mercado interno e disputa mercados "
            "externos, a apreciação é, em geral, " + vm("prejudicial") + ": perde mercado aqui e lá fora. O "
            "argumento aparece no debate sobre " + azb("desindustrialização") + " e “doença holandesa” (câmbio "
            "apreciado por boom de commodities).",
            "Quem ganha com a apreciação: consumidores de importados, empresas que importam insumos e máquinas e "
            "devedores em dólar; ela também ajuda a conter a inflação (bens comercializáveis mais baratos).",
            "Por que o real se valoriza quando o risco cai: menor " + azb("prêmio de risco") + " atrai capital "
            "financeiro, aumenta a oferta de dólares no mercado e derruba a cotação.",
            vm("Regra-âncora: real valorizado → importação barata e exportação cara; real desvalorizado → o "
               "contrário."),
        ],
        "dissecando": (cz("[inversão]") + " O item acerta a causa (menor risco valoriza o real) e inverte todos os "
                       "efeitos, descrevendo o que ocorreria numa <b>desvalorização</b>. A conta coerente "
                       "(“encarece importações” + “mais competitivos”) seduz; basta testar com R$/US$ caindo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A desvalorização do real frente ao dólar tende a beneficiar a indústria local, pois encarece as "
            "importações e torna mais competitivos os produtos brasileiros no exterior.”</i> → CERTO",
            "<i>“A valorização do real tende a reduzir a inflação, ao baratear os bens comercializáveis.”</i> → "
            "CERTO",
            "<i>“A valorização do real eleva a receita em reais dos exportadores.”</i> → ERRADO (inversão: cada "
            "dólar exportado rende menos reais)",
        ])],
        "reescrita": ("A recente valorização do real frente ao dólar, com a melhora da percepção de risco do país, é "
                      + hl("prejudicial à") + " indústria local, já que " + hl("barateia") + " as importações e "
                      "torna " + hl("menos") + " competitivos os produtos brasileiros no exterior."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Valorização do real (queda da taxa R$/US$) significa dólar mais barato: importados mais "
                             "baratos e exportados brasileiros mais caros em dólar."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01235
    {
        "id": "ECO-E2-L01235-1", "fonte_ref": "E2-L01235", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": "Com base nos conceitos de macroeconomia aberta, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("De acordo com a curva J, uma depreciação real da moeda doméstica provoca, inicialmente, uma "
                      "deterioração na balança comercial do próprio país."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com a curva J, uma depreciação real da moeda doméstica provoca, "
                      "<u>inicialmente</u>, uma <u>deterioração</u> na balança comercial do próprio país."),
        "poucas": ("É a definição da " + azb("curva J") + ": logo após a depreciação, o efeito-preço (importações "
                   "mais caras em moeda nacional) domina e o saldo piora; só depois os volumes reagem e o saldo "
                   "melhora."),
        "destrinchando": [
            "Saldo comercial em moeda nacional: NX = X − q·M, em que q é o câmbio real. A depreciação tem dois "
            "efeitos: " + azb("efeito-preço") + " (cada unidade importada custa mais em moeda nacional — imediato) "
            "e " + azb("efeito-volume") + " (exporta-se mais e importa-se menos — lento).",
            "Por que o volume demora: contratos de comércio já fechados em preço e quantidade, prazos de entrega, "
            "custo de trocar de fornecedor, tempo para conquistar clientes no exterior. No curto prazo as "
            "elasticidades são <b>baixas</b>.",
            "Resultado: o saldo cai primeiro e sobe depois — o traçado lembra a letra J ao longo do tempo. A "
            "recuperação exige a " + azb("condição de Marshall-Lerner") + ": " + vd("|ε<sub>X</sub>| + "
            "|ε<sub>M</sub>| > 1") + " (soma das elasticidades-preço, em módulo, maior que 1, partindo de "
            "comércio equilibrado).",
            "Leitura conjunta: no curto prazo Marshall-Lerner costuma <b>não</b> valer (elasticidades baixas) e "
            "no médio prazo passa a valer — é isso que gera o J.",
            vm("Regra-âncora: curva J = piora antes, melhora depois; Marshall-Lerner = condição para a melhora."),
        ],
        "dissecando": (cz("[literalidade]") + " O item reproduz a definição de manual. O risco está em quem acha "
                       "que depreciação “sempre melhora” o saldo e marca ERRADO por ver “deterioração”. A palavra "
                       "que salva é “inicialmente”. 🔥 Curva J e Marshall-Lerner aparecem quase sempre juntas."),
        "modulos": [("😈 Para dificultar", [
            "<i>“De acordo com a curva J, uma depreciação real provoca deterioração permanente da balança "
            "comercial.”</i> → ERRADO (a piora é só inicial)",
            "<i>“A curva J decorre de as elasticidades-preço do comércio serem maiores no curto prazo do que no "
            "longo prazo.”</i> → ERRADO (inversão: são menores no curto prazo)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["inicialmente"], "dificuldade": 1,
        "comentario_fonte": ("Saldo cai inicialmente e depois melhora, valendo Marshall-Lerner; as trocas não são "
                             "perfeitamente flexíveis (contratos geram rigidez)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01626-1, ECO-E2-L01766-1 (curva J)"],
    },
    # ------------------------------------------------------------------ E2-L01237
    {
        "id": "ECO-E2-L01237-1", "fonte_ref": "E2-L01237", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Para manter a taxa de câmbio real constante, a variação da taxa de juros nominal precisa "
                      "igualar a diferença entre a taxa de inflação doméstica e a taxa de inflação externa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Para manter a taxa de câmbio real constante, a variação da taxa ") + vm("de juros")
                    + az(" nominal precisa igualar a diferença entre a taxa de inflação doméstica e a taxa de "
                         "inflação externa.")),
        "poucas": ("Quem precisa variar pelo diferencial de inflação é a taxa de " + azb("câmbio nominal")
                   + ", não a de juros: q = E·P*/P fica constante se " + vd("%ΔE = π − π*") + "."),
        "destrinchando": [
            azb("Câmbio real") + ": " + vd("q = E·P*/P") + " (E em moeda doméstica por estrangeira; P* preços "
            "externos; P preços internos). Mede quantas cestas domésticas valem uma cesta estrangeira — o "
            "<b>preço relativo</b> entre os bens dos dois países.",
            "Em taxas de variação: " + vd("%Δq ≈ %ΔE + π* − π") + ". Para q constante (%Δq = 0), é preciso "
            + vd("%ΔE = π − π*") + ": a moeda doméstica se deprecia exatamente o excesso de inflação interna. É a "
            "lógica da " + azb("PPC relativa") + ".",
            "Exemplo: inflação de 10% no Brasil e 3% nos EUA → o real precisa se depreciar cerca de 7% para que "
            "os produtos brasileiros não percam competitividade.",
            "A taxa de juros aparece em outra paridade: a " + azb("paridade de juros") + " (i = i* + depreciação "
            "esperada) e, com a equação de " + oc("Fisher") + " (i = r + π), juros reais iguais implicam "
            "diferencial de juros nominais igual ao de inflação. O item trocou a variável da PPC pela da "
            "paridade de juros.",
            vm("Regra-âncora: câmbio real constante ⇔ câmbio nominal varia pelo diferencial de inflação."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Uma única palavra trocada (“juros” no lugar de “câmbio”) "
                       "numa fórmula correta. A frase soa familiar porque diferencial de juros e de inflação "
                       "andam juntos em Fisher e na paridade de juros; a pista é que o câmbio real nem contém "
                       "juros na definição."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Para manter a taxa de câmbio real constante, a taxa de câmbio nominal deve se depreciar à "
            "diferença entre a inflação doméstica e a externa.”</i> → CERTO",
            "<i>“Com câmbio nominal fixo e inflação doméstica acima da externa, o câmbio real se deprecia.”</i> → "
            "ERRADO (inversão: aprecia)",
        ])],
        "reescrita": ("Para manter a taxa de câmbio real constante, a variação da taxa " + hl("de câmbio")
                      + " nominal precisa igualar a diferença entre a taxa de inflação doméstica e a taxa de "
                      "inflação externa."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": "Taxa de câmbio real = câmbio nominal × preço externo / preço interno (eP*/P).",
        "qualidade_fonte": "raso",
        "figuras_fonte": [{"ref": "IMAGEM 215", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01240
    {
        "id": "ECO-E2-L01240-1", "fonte_ref": "E2-L01240", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "Pré-TPS/2023", "ano": 2023, "cacd": False, "errei": False,
        "comando": CMD_NAB_ABERTA,
        "rotulo_item": "Item",
        "assertiva": "A paridade do poder de compra na sua versão relativa implica que a taxa de câmbio real é igual a 1.",
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A paridade do poder de compra na sua versão ") + vm("relativa")
                    + az(" implica que a taxa de câmbio real é igual a 1.")),
        "poucas": ("Câmbio real " + vd("= 1") + " é a " + azb("PPC absoluta") + " (E·P* = P). A relativa só exige "
                   "que o câmbio real seja " + azb("constante") + ", em qualquer nível."),
        "destrinchando": [
            azb("PPC absoluta") + ": a mesma cesta custa o mesmo nos dois países quando convertida — "
            + vd("E·P* = P") + ", ou E = P/P*. Substituindo em q = E·P*/P, obtém-se " + vd("q = 1") + ". É a "
            + azb("lei do preço único") + " aplicada a toda a cesta.",
            azb("PPC relativa") + ": trabalha com variações — " + vd("%ΔE = π − π*") + ". Logo %Δq = 0: o câmbio "
            "real é <b>constante</b>, mas pode ser 0,8, 1,3 ou qualquer outro valor, porque custos de transporte, "
            "tarifas e bens não comercializáveis criam diferenças de nível estáveis.",
            "Hierarquia lógica: a absoluta implica a relativa (se q = 1 sempre, q também é constante), mas a "
            "relativa não implica a absoluta.",
            "Evidência: a PPC funciona mal no curto prazo e razoavelmente no longo prazo e em economias de "
            "inflação alta, em que o diferencial de preços domina o movimento do câmbio. O " + azb("efeito "
            "Balassa-Samuelson") + " explica por que países ricos têm níveis de preços mais altos (q ≠ 1 de "
            "forma persistente).",
            vm("Regra-âncora: absoluta → q = 1 (níveis); relativa → q constante (variações)."),
        ],
        "dissecando": (cz("[troca de conceito]") + " O item atribui à versão relativa a implicação da absoluta. "
                       "🔥 A banca alterna as duas versões: “nível” e “= 1” apontam para a absoluta; “variação”, "
                       "“diferencial de inflação” e “constante”, para a relativa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A paridade do poder de compra na sua versão relativa implica que a taxa de câmbio real é "
            "constante.”</i> → CERTO",
            "<i>“Se vale a PPC relativa, vale necessariamente a PPC absoluta.”</i> → ERRADO (inversão: a absoluta "
            "implica a relativa, não o contrário)",
        ])],
        "reescrita": ("A paridade do poder de compra na sua versão " + hl("absoluta") + " implica que a taxa de "
                      "câmbio real é igual a 1."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A PPC absoluta (eP* = P) implica câmbio real igual a 1; a relativa diz que a variação "
                             "do câmbio iguala o diferencial de inflação, com câmbio real constante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 217", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 218", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 219", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01484
    {
        "id": "ECO-E2-L01484-1", "fonte_ref": "E2-L01484", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("Durante a pandemia, o Banco Central conduziu as taxas de juros frente às mudanças da conjuntura "
                    "da inflação, da atividade e da taxa de câmbio. Avalie a proposição a seguir como verdadeira ou "
                    "falsa."),
        "rotulo_item": "Item",
        "assertiva": ("A redução da taxa de juros no início da pandemia, bem como o déficit público elevando o risco, "
                      "são fatores que atuaram em favor da desvalorização do real."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A redução da taxa de juros no início da pandemia, bem como o déficit público elevando o "
                      "risco, são fatores que atuaram em favor da <u>desvalorização</u> do real."),
        "poucas": ("Juros menores reduzem o " + azb("diferencial de juros") + " e o déficit maior eleva o "
                   + azb("prêmio de risco") + ": os dois estimulam saída de capital e depreciam o real."),
        "destrinchando": [
            "Regra de curto prazo, pela " + azb("paridade descoberta de juros") + " com prêmio de risco: se "
            + vd("i > i* + depreciação esperada + PR") + ", entra capital e o câmbio se aprecia; se i for menor "
            "que esse lado direito, sai capital e o câmbio se deprecia.",
            "Juros: o " + rx("Banco Central do Brasil") + " cortou a Selic até o então piso histórico de "
            + vd("2% ao ano") + " (agosto de 2020). Com i menor e i* também baixo, o ganho de aplicar em reais "
            "(o “carry trade”) encolheu e parte do capital saiu.",
            "Risco: os gastos emergenciais (auxílio emergencial, socorro a estados e empresas) levaram o déficit "
            "nominal do setor público a " + vd("cerca de 13–14% do PIB em 2020") + " e a dívida bruta para perto "
            "de 90% do PIB. A dúvida sobre a sustentabilidade fiscal eleva o PR e exige retorno maior para "
            "manter o capital no país.",
            "Os dois choques atuaram na mesma direção: o real foi uma das moedas que mais se depreciaram em "
            "2020 — o dólar, que começara o ano perto de " + vd("R$ 4,00") + ", superou " + vd("R$ 5,80")
            + " em maio. Juros baixos e câmbio depreciado ajudam a explicar a inflação de 2021 e o ciclo de alta "
            "da Selic que se seguiu.",
            vm("Regra-âncora: ↓ juros internos ou ↑ risco-país → saída de capital → depreciação."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item junta dois determinantes de curto prazo e afirma que "
                       "ambos “atuaram em favor” da desvalorização. A armadilha seria achar que déficit "
                       "público “aquece” a economia e atrai capital; na prática, risco fiscal afasta. Nenhum "
                       "modulador absoluto: o item só diz que os fatores contribuíram."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A redução da taxa de juros no início da pandemia atuou em favor da valorização do real, ao "
            "estimular o investimento.”</i> → ERRADO (inversão: juros menores afastam capital e depreciam)",
            "<i>“A posterior elevação da Selic, a partir de 2021, tendeu a apreciar o real, tudo o mais "
            "constante.”</i> → CERTO",
        ]), ("🃏 Carta na manga", [
            "2020 ilustra o “trilema” na prática: com câmbio flutuante e capital móvel, o Banco Central usou os "
            "juros para a atividade e deixou o câmbio absorver o choque — com repasse inflacionário depois."
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Redução de juros diminui a atratividade de capitais e o déficit eleva o risco-país, "
                             "pressionando a desvalorização; vários comentários com contexto da Selic a 2% e do "
                             "déficit de 2020."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 378", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["dado_aproximado: déficit nominal de 2020 e cotação de pico do dólar citados em ordem de "
                    "grandeza"],
    },
    # ------------------------------------------------------------------ E2-L01509
    {
        "id": "ECO-E2-L01509-1", "fonte_ref": "E2-L01509", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Um país com inflação mais elevada do que seus parceiros comerciais e regime de câmbio fixo "
                      "tende a apresentar redução na competitividade das suas exportações."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um país com inflação mais elevada do que seus parceiros comerciais e regime de câmbio "
                      "<u>fixo</u> <u>tende</u> a apresentar redução na competitividade das suas exportações."),
        "poucas": ("Com E fixo e P subindo mais que P*, o " + azb("câmbio real") + " q = E·P*/P cai — "
                   + azb("apreciação real") + ": os bens do país encarecem em relação aos estrangeiros."),
        "destrinchando": [
            "O que importa para a competitividade é o câmbio <b>real</b>, não o nominal. Em variações: "
            + vd("%Δq ≈ %ΔE + π* − π") + ". Com câmbio fixo, %ΔE = 0; se π > π*, %Δq &lt; 0.",
            "Exemplo: inflação de 12% em casa e 2% fora, câmbio travado. Em um ano, os produtos nacionais ficam "
            "cerca de 10% mais caros em moeda estrangeira; os importados, relativamente mais baratos. "
            "Exportações perdem mercado e importações ganham.",
            "Sob câmbio flutuante, a PPC relativa preveria depreciação nominal de cerca de 10%, neutralizando a "
            "perda. Com câmbio fixo, esse ajuste não acontece, e a apreciação real se acumula.",
            rx("Brasil") + ": foi o caso do " + azb("Plano Real") + " entre 1994 e 1999 — âncora cambial, "
            "inflação residual acima da americana e apreciação real crescente, com déficits em conta corrente "
            "que só se reverteram depois da flutuação de 1999. Mesma lógica na Argentina da conversibilidade "
            "(1991–2001).",
            vm("Regra-âncora: câmbio fixo + inflação acima dos parceiros → apreciação real → perda de "
               "competitividade."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Quem pensa em câmbio “fixo” acha que nada "
                       "muda e marca ERRADO; o câmbio nominal está parado, mas o real se move com a inflação. "
                       "O “tende a” afasta qualquer objeção sobre produtividade ou qualidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um país com inflação mais elevada que a dos parceiros e câmbio fixo tem depreciação real da "
            "moeda.”</i> → ERRADO (inversão: aprecia)",
            "<i>“Com câmbio flutuante, a PPC relativa prevê depreciação nominal que compensa o diferencial de "
            "inflação.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Com câmbio fixo e inflação superior à dos parceiros, há apreciação real: produtos "
                             "domésticos ficam mais caros, exportações perdem competitividade e importações "
                             "são estimuladas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 390", "tipo_fonte": "FÓRMULA", "lado": "verso", "acao": "texto"},
                          {"ref": "IMAGEM 391", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01697-1 (câmbio fixo e diferencial de inflação, com o sinal "
                    "invertido)"],
    },
    # ------------------------------------------------------------------ E2-L01512
    {
        "id": "ECO-E2-L01512-1", "fonte_ref": "E2-L01512", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a condição de Marshall-Lerner, para que uma desvalorização cambial leve a um aumento "
                      "do saldo das exportações líquidas, a soma das elasticidades (em módulo) das exportações e "
                      "importações à taxa de câmbio deve ser maior que 1."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a condição de Marshall-Lerner, para que uma desvalorização cambial leve a um "
                      "aumento do saldo das exportações líquidas, a <u>soma</u> das elasticidades (em módulo) das "
                      "exportações e importações à taxa de câmbio deve ser <u>maior que 1</u>."),
        "poucas": ("É o enunciado da condição: " + vd("|ε<sub>X</sub>| + |ε<sub>M</sub>| > 1") + ". Se a soma "
                   "for menor que 1, o efeito-preço domina e a desvalorização <b>piora</b> o saldo."),
        "destrinchando": [
            "A desvalorização mexe no saldo por dois canais: o " + azb("efeito-volume") + " (exporta-se mais, "
            "importa-se menos — melhora) e o " + azb("efeito-preço") + " (cada unidade importada custa mais em "
            "moeda nacional — piora).",
            "A condição de " + oc("Marshall-Lerner") + " diz quando o volume vence o preço: partindo de comércio "
            "equilibrado, a soma das elasticidades-preço da demanda por exportações e por importações, em "
            "valor absoluto, precisa superar 1.",
            "Exemplo: |ε<sub>X</sub>| = 0,6 e |ε<sub>M</sub>| = 0,7 → soma 1,3 > 1 → a desvalorização melhora o "
            "saldo. Com 0,3 e 0,4 (soma 0,7), piora.",
            "Ligação com a " + azb("curva J") + ": no curto prazo as elasticidades são baixas e a condição "
            "costuma falhar (o saldo cai); com o tempo elas crescem, a condição passa a valer e o saldo "
            "melhora.",
            "Limites da formulação: supõe ofertas infinitamente elásticas e saldo inicial nulo; com déficit "
            "inicial grande, exige-se soma maior que 1.",
            vm("Regra-âncora: soma das elasticidades (em módulo) maior que 1 → desvalorização melhora o saldo."),
        ],
        "dissecando": (cz("[literalidade]") + " Reproduz a condição de manual. As versões erradas costumam trocar "
                       "“soma” por “produto”, “maior” por “menor”, ou exigir que <b>cada</b> elasticidade "
                       "supere 1 — confira esses três pontos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…cada uma das elasticidades das exportações e das importações deve ser maior que 1.”</i> → "
            "ERRADO (exigência indevida: basta a soma)",
            "<i>“…a soma das elasticidades deve ser menor que 1.”</i> → ERRADO (inversão: menor que 1 o saldo "
            "piora)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("A desvalorização melhora o saldo comercial se |εx| + |εm| > 1; com demandas muito "
                             "inelásticas, o efeito-preço domina e o saldo pode piorar."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 392", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01555
    {
        "id": "ECO-E2-L01555-1", "fonte_ref": "E2-L01555", "destino": "66", "subtema": H2["reg"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("Com base na equação de paridade descoberta da taxa de juros, avalie a afirmativa a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Em uma economia com taxa de câmbio fixa, mesmo que o governo não tenha intenção de promover "
                      "uma desvalorização, esta pode ocorrer pela simples mudança de expectativas dos agentes."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em uma economia com taxa de câmbio fixa, mesmo que o governo não tenha intenção de "
                      "promover uma desvalorização, esta <u>pode</u> ocorrer pela simples mudança de expectativas "
                      "dos agentes."),
        "poucas": ("Se os agentes passam a esperar desvalorização, a " + azb("paridade de juros") + " exige juros "
                   "maiores; sem eles, há fuga de capital e perda de reservas — o " + azb("ataque especulativo")
                   + " pode forçar a desvalorização."),
        "destrinchando": [
            "Paridade descoberta: " + vd("i = i* + (E<sup>e</sup> − E)/E") + ". Com câmbio fixo crível, a "
            "depreciação esperada é zero e i = i*. Se o mercado passa a esperar desvalorização, o lado direito "
            "sobe: para segurar o capital, o Banco Central precisa elevar i.",
            "Se não eleva (ou não consegue, porque juros altos derrubam a atividade e pioram a dívida), os "
            "agentes trocam moeda doméstica por divisas; o Banco Central vende reservas para defender a "
            "paridade até elas acabarem — e aí a desvalorização vem de qualquer forma.",
            azb("Crises de 2ª geração") + " (" + oc("Obstfeld") + "): o governo pondera o custo de defender a "
            "paridade; se o mercado acredita que ele desistirá, o custo de defesa sobe e a desistência se torna "
            "racional — a crise é " + azb("autorrealizável") + ". Nas " + azb("de 1ª geração") + " ("
            + oc("Krugman") + ", 1979), a causa é o fundamento ruim (déficit monetizado) que esgota reservas.",
            "Casos: libra esterlina e o Sistema Monetário Europeu (1992), México (1994), " + rx("Brasil")
            + " (janeiro de 1999), Argentina (2001–2002).",
            vm("Regra-âncora: câmbio fixo só sobrevive enquanto é crível; expectativa de desvalorização pode "
               "produzi-la."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Parece que só o governo decide uma "
                       "desvalorização sob câmbio fixo; o item cobra que as expectativas, sozinhas, podem "
                       "forçá-la. O “pode” deixa o item à prova de exceções (Banco Central com reservas enormes)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio fixo, a desvalorização depende exclusivamente de decisão do governo.”</i> → "
            "ERRADO (modulador absoluto)",
            "<i>“Se os agentes passam a esperar desvalorização, a manutenção da paridade exige elevação dos juros "
            "domésticos.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode", "simples"],
        "dificuldade": 2,
        "comentario_fonte": ("Expectativas de desvalorização levam a ataques especulativos que esgotam reservas e "
                             "forçam a desvalorização mesmo sem intenção inicial do governo (crises de 2ª "
                             "geração)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01624
    {
        "id": "ECO-E2-L01624-1", "fonte_ref": "E2-L01624", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria da paridade do poder de compra, a arbitragem tende a fazer a taxa nominal de "
                      "câmbio ficar constante entre os países."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a teoria da paridade do poder de compra, a arbitragem tende a fazer a taxa ")
                    + vm("nominal") + az(" de câmbio ficar constante entre os países.")),
        "poucas": ("A arbitragem de bens tende a estabilizar o câmbio " + azb("real") + "; o " + azb("nominal")
                   + " precisa <b>variar</b> para compensar os diferenciais de inflação."),
        "destrinchando": [
            "Base da PPC: a " + azb("lei do preço único") + " — sem custos de transporte nem barreiras, o mesmo "
            "bem deve custar o mesmo em qualquer país quando convertido à mesma moeda. Se a soja é mais barata "
            "no Brasil, compra-se aqui e vende-se lá até os preços se igualarem.",
            "Em nível (" + azb("PPC absoluta") + "): " + vd("E = P/P*") + ". Se P sobe mais que P*, E tem de "
            "subir (depreciação nominal). Logo o câmbio nominal acompanha os preços e não fica parado.",
            "Em variação (" + azb("PPC relativa") + "): " + vd("%ΔE = π − π*") + ". O que fica constante é o "
            "câmbio real q = E·P*/P (igual a 1, na absoluta).",
            "O câmbio nominal só ficaria constante no caso particular de inflações iguais nos dois países.",
            vm("Regra-âncora: PPC → câmbio real estável; câmbio nominal se move com o diferencial de inflação."),
        ],
        "dissecando": (cz("[troca de conceito]") + " Troca “real” por “nominal”. O raciocínio da arbitragem está "
                       "certo; o que ela estabiliza é o preço relativo dos bens (câmbio real). Pista: se a "
                       "inflação brasileira é maior que a americana, um câmbio nominal parado contradiz a "
                       "própria PPC."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a PPC, a arbitragem tende a manter constante a taxa real de câmbio.”</i> → CERTO",
            "<i>“Segundo a PPC, a taxa nominal de câmbio permanece constante quando as inflações doméstica e "
            "externa são iguais.”</i> → CERTO",
        ])],
        "reescrita": ("Segundo a teoria da paridade do poder de compra, a arbitragem tende a fazer a taxa "
                      + hl("real") + " de câmbio ficar constante entre os países."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("A PPC implica que a taxa nominal se ajusta para refletir diferenças de preços; com "
                             "inflação maior, a moeda se deprecia; o câmbio nominal não fica constante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 465", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_corrigido: “um a arbitragem” → “a arbitragem”; numeração “1” retirada"],
    },
    # ------------------------------------------------------------------ E2-L01626
    {
        "id": "ECO-E2-L01626-1", "fonte_ref": "E2-L01626", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": "A curva J mostra que o efeito imediato de uma depreciação cambial pode ser a redução do saldo comercial.",
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A curva J mostra que o efeito <u>imediato</u> de uma depreciação cambial <u>pode</u> ser a "
                      "redução do saldo comercial."),
        "poucas": ("No curto prazo os volumes de comércio quase não reagem, mas as importações ficam "
                   "imediatamente mais caras em moeda nacional: o " + azb("efeito-preço") + " domina e o saldo "
                   "cai antes de subir."),
        "destrinchando": [
            "Saldo em moeda nacional: NX = X − q·M. A depreciação eleva q de imediato; X e M (volumes) estão "
            "presos a contratos e pedidos já feitos. Resultado: q·M sobe mais do que X — o saldo " + vd("cai")
            + ".",
            "Com o tempo, exportadores ganham clientes, importadores trocam fornecedores estrangeiros por "
            "nacionais e os volumes respondem: o " + azb("efeito-volume") + " passa a dominar e o saldo sobe, "
            "terminando acima do ponto de partida.",
            "A melhora final depende da " + azb("condição de Marshall-Lerner") + " (soma das elasticidades, em "
            "módulo, maior que 1). No curto prazo as elasticidades são baixas e a condição costuma falhar — é "
            "isso que produz o trecho descendente do J.",
            "Evidência clássica: a desvalorização do dólar após o Acordo do Plaza (1985) — o déficit comercial "
            "americano continuou crescendo até 1987 antes de cair.",
            vm("Regra-âncora: depreciação → saldo cai no impacto e melhora depois (se valer Marshall-Lerner)."),
        ],
        "grafico_verso": "ECO-E2-L01626-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " Definição de manual, protegida por “pode”. "
                       "Quem lembra só que depreciação “melhora” o saldo marca ERRADO. 🔥 A palavra-chave é "
                       "temporal: “imediato”, “inicialmente”, “no curto prazo”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A curva J mostra que o efeito imediato de uma depreciação é o aumento do saldo comercial, que "
            "depois se reverte.”</i> → ERRADO (inversão: cai primeiro, sobe depois)",
            "<i>“O formato da curva J decorre de as quantidades exportadas e importadas reagirem com defasagem à "
            "mudança do câmbio.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["pode", "imediato"], "dificuldade": 1,
        "comentario_fonte": ("No curto prazo os volumes não se ajustam (contratos, inelasticidade) e o valor das "
                             "importações em moeda local sobe; o saldo piora e depois melhora, formando o J."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 467", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01626-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01235-1, ECO-E2-L01766-1 (curva J)"],
    },
    # ------------------------------------------------------------------ E2-L01627
    {
        "id": "ECO-E2-L01627-1", "fonte_ref": "E2-L01627", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": True,
        "comando": CMD_RT_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria da paridade do poder de compra, países com inflação elevada tendem a "
                      "apresentar apreciação da taxa de câmbio nominal no longo prazo."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a teoria da paridade do poder de compra, países com inflação elevada tendem a "
                       "apresentar ") + vm("apreciação") + az(" da taxa de câmbio nominal no longo prazo.")),
        "poucas": ("Pela " + azb("PPC relativa") + ", " + vd("%ΔE = π − π*") + ": inflação acima da dos parceiros "
                   "leva a " + azb("depreciação") + " nominal, não a apreciação."),
        "destrinchando": [
            "Intuição: se a moeda perde poder de compra dentro do país (inflação alta), também perde valor fora "
            "dele. Quem compra reais para adquirir bens brasileiros precisa de mais reais por dólar.",
            "Exemplo: inflação de 20% no país e 0% fora. Uma saca de R$ 100 vai a R$ 120; para continuar valendo "
            "US$ 20, o câmbio deve passar de R$ 5,00 para " + vd("R$ 6,00") + " por dólar — depreciação de 20%.",
            "Se, ao contrário, a moeda se apreciasse, o país ficaria cada vez mais caro em moeda estrangeira, "
            "acumulando déficits — situação que não se sustenta no longo prazo.",
            "Evidência: economias de inflação alta (" + rx("Brasil") + " antes do Plano Real, Argentina, "
            "Turquia) exibem depreciação nominal contínua; é justamente onde a PPC funciona melhor, porque o "
            "diferencial de inflação domina os demais determinantes.",
            vm("Regra-âncora: mais inflação → depreciação nominal (PPC relativa)."),
        ],
        "dissecando": (cz("[inversão]") + " Troca depreciação por apreciação, mantendo o resto do enunciado "
                       "exato. O “no longo prazo” é correto — é o horizonte em que a PPC vale. Confusão "
                       "comum: inflação alta aprecia o câmbio <b>real</b> quando o nominal está fixo; o item fala "
                       "do nominal."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a PPC, países com inflação elevada tendem a apresentar depreciação da taxa de câmbio "
            "nominal no longo prazo.”</i> → CERTO",
            "<i>“Com câmbio nominal fixo, inflação elevada provoca apreciação real.”</i> → CERTO",
        ])],
        "reescrita": ("Segundo a teoria da paridade do poder de compra, países com inflação elevada tendem a "
                      "apresentar " + hl("depreciação") + " da taxa de câmbio nominal no longo prazo."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tendem a"], "dificuldade": 1,
        "comentario_fonte": ("Pela PPC relativa, o país com inflação maior tem depreciação nominal no longo prazo "
                             "para manter o poder de compra relativo."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L01767-1 (mesma prova, mesma tese com outra redação)",
                    "texto_corrigido: numeração “4” retirada"],
    },
    # ------------------------------------------------------------------ E2-L01696
    {
        "id": "ECO-E2-L01696-1", "fonte_ref": "E2-L01696", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ECO_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria clássica e a paridade do poder de compra, países com oferta de moeda "
                      "crescendo mais rápido que seus parceiros comerciais apresentarão depreciação nominal de suas "
                      "moedas no longo prazo."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Segundo a teoria clássica e a paridade do poder de compra, países com oferta de moeda "
                      "crescendo mais rápido que seus parceiros comerciais apresentarão depreciação nominal de "
                      "suas moedas <u>no longo prazo</u>."),
        "poucas": ("Duas peças encadeadas: " + azb("teoria quantitativa") + " (mais moeda → mais inflação) e "
                   + azb("PPC relativa") + " (mais inflação → depreciação nominal)."),
        "destrinchando": [
            "Teoria quantitativa: " + vd("MV = PY") + ". Em taxas, com V estável: " + vd("π ≈ μ − g") + " "
            "(crescimento da moeda menos crescimento do produto). No longo prazo, a moeda é neutra: "
            "expandi-la mais depressa só eleva preços.",
            "PPC relativa: " + vd("%ΔE = π − π*") + ". Juntando as duas: %ΔE ≈ (μ − μ*) − (g − g*). Com "
            "crescimentos reais parecidos, o país que emite moeda mais rápido vê sua moeda se depreciar "
            "aproximadamente na diferença das taxas de expansão monetária.",
            "É o núcleo da " + azb("abordagem monetária do câmbio") + ": o câmbio é o preço relativo de duas "
            "moedas e, como qualquer preço, cai (a moeda perde valor) quando a oferta cresce mais que a "
            "demanda.",
            "O resultado é de <b>longo prazo</b>. No curto prazo, preços rígidos permitem que a expansão "
            "monetária reduza juros e provoque " + azb("overshooting") + " (" + oc("Dornbusch") + ", 1976): o "
            "câmbio deprecia além do valor de longo prazo e depois se aprecia parcialmente.",
            vm("Regra-âncora: moeda cresce mais rápido → inflação maior → depreciação nominal no longo prazo."),
        ],
        "dissecando": (cz("[paráfrase fiel]") + " O item encadeia neutralidade da moeda e PPC. O “apresentarão” "
                       "soa determinista, mas vem ancorado em “no longo prazo” e no arcabouço clássico, em que a "
                       "conclusão é dedutiva."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…países com oferta de moeda crescendo mais rápido apresentarão apreciação real permanente de "
            "suas moedas.”</i> → ERRADO (no longo prazo a moeda é neutra para o câmbio real)",
            "<i>“No modelo de Dornbusch, uma expansão monetária faz o câmbio depreciar no curto prazo além do "
            "seu nível de longo prazo.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["no longo prazo"], "dificuldade": 1,
        "comentario_fonte": ("Maior crescimento monetário gera inflação maior e, pela PPC, depreciação nominal no "
                             "longo prazo (abordagem monetária do câmbio)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 500", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01697
    {
        "id": "ECO-E2-L01697-1", "fonte_ref": "E2-L01697", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": CMD_RT_ECO_ABERTA,
        "rotulo_item": "Item",
        "assertiva": ("Se um país com regime de câmbio fixo tem inflação mais baixa que seus parceiros comerciais, a "
                      "taxa de câmbio real se aprecia, levando à perda de competitividade e redução do saldo "
                      "comercial."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se um país com regime de câmbio fixo tem inflação mais baixa que seus parceiros comerciais, "
                       "a taxa de câmbio real se ") + vm("aprecia") + az(", levando ") + vm("à perda")
                    + az(" de competitividade e ") + vm("redução") + az(" do saldo comercial.")),
        "poucas": ("Com E fixo e P subindo <b>menos</b> que P*, q = E·P*/P <b>sobe</b>: " + azb("depreciação "
                   "real") + ". O país fica relativamente mais barato e ganha competitividade."),
        "destrinchando": [
            "Em variações: " + vd("%Δq ≈ %ΔE + π* − π") + ". Câmbio fixo → %ΔE = 0. Se π &lt; π*, então "
            "%Δq > 0: o câmbio real se " + azb("deprecia") + ".",
            "Exemplo: inflação de 2% em casa e 6% nos parceiros, câmbio travado. Em um ano, os bens nacionais "
            "ficam cerca de 4% mais baratos em relação aos estrangeiros: exportações ganham mercado, "
            "importações perdem.",
            "Efeito no saldo: tende a melhorar, desde que valha a " + azb("condição de Marshall-Lerner") + " "
            "(soma das elasticidades-preço, em módulo, maior que 1).",
            "O caso espelhado é o que costuma cair: câmbio fixo com inflação <b>acima</b> dos parceiros → "
            "apreciação real → perda de competitividade (o " + rx("Brasil") + " de 1994–1998). O item pega a "
            "conclusão desse caso e a aplica ao caso oposto.",
            "Exemplo real do caso do item: a Alemanha na zona do euro, com inflação abaixo da média dos "
            "parceiros na década de 2000, ganhou competitividade real dentro da união monetária e acumulou "
            "grandes superávits.",
            vm("Regra-âncora: câmbio fixo + inflação abaixo dos parceiros → depreciação real → ganho de "
               "competitividade."),
        ],
        "dissecando": (cz("[inversão]") + " O item descreve com coerência interna o caso de inflação "
                       "<b>maior</b> e o atribui à inflação menor. Teste rápido: preços internos crescendo menos "
                       "= produtos nacionais relativamente mais baratos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se um país com câmbio fixo tem inflação mais alta que seus parceiros, a taxa de câmbio real se "
            "aprecia, com perda de competitividade.”</i> → CERTO",
            "<i>“Com câmbio fixo, diferenciais de inflação não afetam a competitividade, pois o câmbio não "
            "varia.”</i> → ERRADO (confunde câmbio nominal com real)",
        ])],
        "reescrita": ("Se um país com regime de câmbio fixo tem inflação mais baixa que seus parceiros comerciais, "
                      "a taxa de câmbio real se " + hl("deprecia") + ", levando " + hl("a ganho") + " de "
                      "competitividade e " + hl("aumento") + " do saldo comercial."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 2,
        "comentario_fonte": ("Respostas contraditórias: uma afirma apreciação real e sugere gabarito C; outra diz "
                             "que o erro está em afirmar redução do saldo de forma determinística; outra aponta "
                             "depreciação real com ganho de competitividade."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: parte dos comentários de origem afirma que inflação mais baixa com câmbio fixo "
                    "causa apreciação real e sugere erro de gabarito; o correto é depreciação real, o que confirma "
                    "o ERRADO da fonte",
                    "quase_duplicata: ECO-E2-L01509-1 (caso espelhado, inflação mais alta)"],
    },
    # ------------------------------------------------------------------ E2-L01766
    {
        "id": "ECO-E2-L01766-1", "fonte_ref": "E2-L01766", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "A respeito da teoria do comércio internacional, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Uma desvalorização cambial, segundo a curva J, leva a uma redução inicial do saldo comercial, "
                      "que tende a ser revertida ao longo do tempo, se for válida a condição de Marshall-Lerner."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Uma desvalorização cambial, segundo a curva J, leva a uma redução <u>inicial</u> do saldo "
                      "comercial, que tende a ser revertida ao longo do tempo, <u>se for válida a condição de "
                      "Marshall-Lerner</u>."),
        "poucas": ("O item junta as duas peças: a " + azb("curva J") + " (piora no impacto, melhora depois) e a "
                   + azb("condição de Marshall-Lerner") + " (a melhora só vem se a soma das elasticidades, em "
                   "módulo, superar 1)."),
        "destrinchando": [
            "Impacto: importações e exportações estão contratadas em volume e preço; a desvalorização encarece "
            "de imediato, em moeda nacional, o que se importa. O " + azb("efeito-preço") + " domina e o saldo "
            "cai.",
            "Ajuste: com o tempo, os volumes respondem ao novo preço relativo — exporta-se mais e importa-se "
            "menos. Se " + vd("|ε<sub>X</sub>| + |ε<sub>M</sub>| > 1") + ", o " + azb("efeito-volume")
            + " supera o efeito-preço e o saldo termina acima do inicial.",
            "Sem Marshall-Lerner, a trajetória não vira J: o saldo cai e permanece abaixo do nível de partida — a "
            "desvalorização não corrige o déficit.",
            "Por isso a condição é o “se” do item: as elasticidades costumam ser baixas no curto prazo e maiores "
            "no médio prazo, o que explica tanto a queda inicial quanto a recuperação.",
            vm("Regra-âncora: curva J = trajetória; Marshall-Lerner = condição para que ela termine acima do ponto "
               "de partida."),
        ],
        "grafico_verso": "ECO-E2-L01766-1-V1",
        "dissecando": (cz("[literalidade · modulador relativo]") + " Reproduz o manual, com dupla proteção: "
                       "“tende a” e a condicional “se for válida”. Versões erradas trocam a condição (“se a soma "
                       "for menor que 1”) ou a ordem temporal (“aumento inicial”)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…que tende a ser revertida ao longo do tempo, se a soma das elasticidades-preço das exportações e "
            "importações, em módulo, for inferior a 1.”</i> → ERRADO (inversão da condição)",
            "<i>“A curva J implica que a desvalorização melhora o saldo comercial já no curto prazo.”</i> → "
            "ERRADO (inversão temporal)",
        ])],
        "tipo_erro": ["LITERAL", "MODULADOR_RELATIVO"], "moduladores": ["tende a", "se"], "dificuldade": 1,
        "comentario_fonte": ("A curva J descreve a trajetória do saldo após a desvalorização: piora inicialmente "
                             "(contratos firmados) e melhora depois, se valer Marshall-Lerner."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 529", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"},
                          {"ref": "IMAGEM 530", "tipo_fonte": "GRÁFICO", "lado": "verso",
                           "acao": "redesenhada (ECO-E2-L01766-1-V1)"}],
        "alertas": ["quase_duplicata: ECO-E2-L01235-1, ECO-E2-L01626-1 (curva J)"],
    },
    # ------------------------------------------------------------------ E2-L01767
    {
        "id": "ECO-E2-L01767-1", "fonte_ref": "E2-L01767", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": ("A respeito dos conceitos de taxa de câmbio e das relações entre câmbio, juros e inflação, "
                    "julgue o item a seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Segundo a teoria da paridade do poder de compra, um país com inflação mais elevada do que seus "
                      "parceiros comerciais tende, no longo prazo, a verificar uma apreciação nominal da sua "
                      "moeda."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Segundo a teoria da paridade do poder de compra, um país com inflação mais elevada do que "
                       "seus parceiros comerciais tende, no longo prazo, a verificar uma ") + vm("apreciação")
                    + az(" nominal da sua moeda.")),
        "poucas": ("A " + azb("PPC relativa") + " prevê " + azb("depreciação") + " nominal igual ao diferencial de "
                   "inflação (" + vd("%ΔE = π − π*") + "), para que o câmbio real fique estável."),
        "destrinchando": [
            "Ponto de partida: q = E·P*/P (E em moeda doméstica por estrangeira). Se P cresce mais que P*, q "
            "cairia (apreciação real, perda de competitividade). Para q voltar ao nível de equilíbrio, E precisa "
            "<b>subir</b>: a moeda doméstica se deprecia em termos nominais.",
            "Conta: inflação de 9% no país e 3% fora → depreciação nominal de cerca de " + vd("6%") + " ao ano "
            "no longo prazo.",
            "Mecanismo: com a moeda doméstica perdendo poder de compra, os produtos do país encarecem; a "
            "demanda por eles (e pela moeda que os paga) cai, e a oferta da moeda para comprar importados sobe. "
            "O mercado de câmbio reflete essa corrosão.",
            "Atenção a duas confusões: (1) com câmbio <b>fixo</b>, inflação alta produz apreciação <b>real</b> "
            "(o nominal não se move); (2) no curto prazo, juros altos para combater a inflação podem até "
            "apreciar a moeda — mas a PPC é uma tese de longo prazo.",
            vm("Regra-âncora: inflação acima dos parceiros → depreciação nominal no longo prazo."),
        ],
        "dissecando": (cz("[inversão]") + " Só uma palavra trocada: apreciação no lugar de depreciação. O resto "
                       "(“no longo prazo”, “paridade do poder de compra”) está correto e dá ao item cara de "
                       "verdadeiro. 🔥 Tema muito repetido nos simulados — a banca alterna as duas palavras."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Segundo a PPC, o país com inflação mais elevada tende, no longo prazo, a verificar depreciação "
            "nominal da sua moeda.”</i> → CERTO",
            "<i>“Segundo a PPC, diferenciais de inflação não afetam a taxa nominal de câmbio no longo prazo.”</i> "
            "→ ERRADO (é justamente o que a determina)",
        ])],
        "reescrita": ("Segundo a teoria da paridade do poder de compra, um país com inflação mais elevada do que "
                      "seus parceiros comerciais tende, no longo prazo, a verificar uma " + hl("depreciação")
                      + " nominal da sua moeda."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["tende"], "dificuldade": 1,
        "comentario_fonte": ("Pela PPC, a moeda do país com inflação maior tende a se depreciar nominalmente, e não "
                             "a se apreciar, mantendo o preço real dos bens entre os países."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 531", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["quase_duplicata: ECO-E2-L01627-1 (mesma prova, mesma tese com outra redação)"],
    },
    # ------------------------------------------------------------------ E3-L00029
    {
        "id": "ECO-E3-L00029-1", "fonte_ref": "E3-L00029", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "TJ/PA/2025", "ano": 2025, "cacd": False, "errei": False,
        "comando": ("Considere a situação hipotética a seguir e julgue o item, em relação aos efeitos "
                    "macroeconômicos de choques salariais e fiscais, e de movimentos nos preços internos."),
        "excerto": ("<p><i>Uma economia nacional opera com capital fixo no curto prazo e está sujeita a variações "
                    "nominais de salários, preços internos e políticas fiscais expansionistas. O país adota um "
                    "regime de taxa de câmbio fixa e mantém constante o nível de preços internacionais.</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("Se os preços domésticos aumentam, mantendo-se constante o câmbio nominal e o nível de preços "
                      "internacionais, a taxa real de câmbio se deprecia, o que favorece as exportações líquidas."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Se os preços domésticos aumentam, mantendo-se constante o câmbio nominal e o nível de preços "
                       "internacionais, a taxa real de câmbio se ") + vm("deprecia") + az(", o que ")
                    + vm("favorece") + az(" as exportações líquidas.")),
        "poucas": ("Com E e P* fixos, P maior derruba q = E·P*/P: é " + azb("apreciação real") + ". Os bens "
                   "nacionais ficam relativamente mais caros e as exportações líquidas " + vm("caem") + "."),
        "destrinchando": [
            azb("Câmbio real") + ": " + vd("q = E·P*/P") + " — quantas cestas domésticas compram uma cesta "
            "estrangeira. P está no <b>denominador</b>: se ele sobe com E e P* parados, q cai.",
            "q menor = " + azb("apreciação real") + ": a mesma cesta estrangeira vale menos cestas nacionais, "
            "ou seja, os produtos do país ficaram relativamente caros. Exportar fica mais difícil e importar, "
            "mais atraente: " + vd("NX ↓") + ".",
            "É o que acontece num regime de câmbio fixo quando salários e preços internos sobem (o cenário do "
            "enunciado): sem ajuste do câmbio nominal, a inflação doméstica corrói a competitividade.",
            "Caminhos de correção sob câmbio fixo: desvalorização da paridade (ajuste nominal) ou queda relativa "
            "de preços e salários internos (" + azb("desvalorização interna") + ", lenta e recessiva — o caso "
            "dos países periféricos da zona do euro depois de 2010).",
            vm("Regra-âncora: P ↑ com E e P* constantes → q ↓ (apreciação real) → NX ↓."),
        ],
        "dissecando": (cz("[inversão]") + " Inverte o sentido do câmbio real e, por coerência, o efeito sobre as "
                       "exportações líquidas. O enunciado ajuda: “preços domésticos aumentam” com tudo o mais "
                       "fixo só pode encarecer o país. 🔥 CEBRASPE cobra a fórmula do câmbio real em quase toda "
                       "prova de macro aberta."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Se os preços internacionais aumentam, mantendo-se constantes o câmbio nominal e os preços "
            "domésticos, a taxa real de câmbio se deprecia, o que favorece as exportações líquidas.”</i> → CERTO",
            "<i>“Uma desvalorização do câmbio nominal acompanhada de inflação doméstica de igual magnitude deprecia "
            "o câmbio real.”</i> → ERRADO (os efeitos se anulam: q fica constante)",
        ])],
        "reescrita": ("Se os preços domésticos aumentam, mantendo-se constante o câmbio nominal e o nível de preços "
                      "internacionais, a taxa real de câmbio se " + hl("aprecia") + ", o que "
                      + hl("desfavorece") + " as exportações líquidas."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("q = e·P*/P; se P sobe com e e P* constantes, q cai (apreciação real), prejudicando "
                             "exportações e estimulando importações. Várias respostas convergentes, com "
                             "reescritas."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["texto_corrigido: numeração “73” retirada"],
    },
    # ------------------------------------------------------------------ E3-L00108
    {
        "id": "ECO-E3-L00108-1", "fonte_ref": "E3-L00108", "destino": "66", "subtema": H2["ppc"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_25,
        "rotulo_item": "Item",
        "assertiva": ("Consoante a teoria da paridade do poder de compra, o país cuja taxa de inflação é mais elevada "
                      "que a que prevalece nas demais nações enfrenta pressões para depreciar a moeda nacional."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Consoante a teoria da paridade do poder de compra, o país cuja taxa de inflação é mais "
                      "elevada que a que prevalece nas demais nações enfrenta <u>pressões para depreciar</u> a "
                      "moeda nacional."),
        "poucas": ("É a " + azb("PPC relativa") + ": " + vd("%ΔE ≈ π − π*") + ". Inflação acima da externa → a "
                   "moeda nacional tende a se depreciar para manter o câmbio real estável."),
        "destrinchando": [
            azb("PPC absoluta") + ": " + vd("E = P/P*") + " — a mesma cesta custa o mesmo nos dois países, "
            "convertida pelo câmbio (cesta de R$ 500 aqui e US$ 100 lá → E “justo” de R$ 5,00). Raramente vale "
            "em nível, por causa de custos de transporte, tarifas e bens não comercializáveis.",
            azb("PPC relativa") + ": olha as variações — a depreciação nominal iguala o diferencial de inflação. "
            "Exemplo: inflação de 20% no Brasil e 0% nos EUA; a saca de soja vai de R$ 100 para R$ 120; para "
            "continuar custando US$ 20, o câmbio passa de " + vd("R$ 5,00 para R$ 6,00") + " por dólar.",
            "Por que “pressões”: sem a depreciação, o país perde exportações e ganha importações, e a demanda "
            "por divisas supera a oferta — o próprio mercado empurra o câmbio para cima.",
            "Limites: no curto prazo, fluxos financeiros (juros, risco) dominam o câmbio; serviços não "
            "comercializáveis não arbitram; o " + azb("efeito Balassa-Samuelson") + " faz países de alta "
            "produtividade terem níveis de preços persistentemente mais altos.",
            vm("Regra-âncora: inflação acima dos parceiros → pressão de depreciação nominal."),
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " Paráfrase da PPC relativa, suavizada por "
                       "“enfrenta pressões” — não diz que a depreciação ocorre sempre nem no curto prazo. A "
                       "armadilha é confundir com o caso de câmbio fixo, em que a inflação alta aprecia o câmbio "
                       "<b>real</b>."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…o país cuja taxa de inflação é mais elevada enfrenta pressões para apreciar a moeda "
            "nacional.”</i> → ERRADO (inversão)",
            "<i>“A PPC absoluta costuma valer no curto prazo, mesmo com bens não comercializáveis.”</i> → ERRADO "
            "(funciona mal no curto prazo)",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["pressões"], "dificuldade": 1,
        "comentario_fonte": ("Versão relativa da PPC: o câmbio nominal se ajusta ao diferencial de inflação; "
                             "exemplo numérico Brasil × EUA; limitações (não comercializáveis, custos, fluxos "
                             "financeiros, Balassa-Samuelson)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 83–89", "tipo_fonte": "FÓRMULA/TEXTO", "lado": "verso",
                           "acao": "absorvida (fórmulas da PPC no 📖)"}],
        "alertas": ["texto_corrigido: numeração “226.” retirada"],
    },
    # ------------------------------------------------------------------ E3-L00110
    {
        "id": "ECO-E3-L00110-1", "fonte_ref": "E3-L00110", "destino": "66", "subtema": H2["det"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Junho/2025", "ano": 2025,
        "cacd": False, "errei": True,
        "comando": CMD_NIDI_25,
        "rotulo_item": "Item",
        "assertiva": ("No longo prazo, a adoção de barreiras comerciais, como, por exemplo, tarifas e quotas à "
                      "importação, conduz ao aumento da taxa de câmbio real, o que favorece o aumento das "
                      "exportações líquidas da economia e a redução do déficit em conta corrente na economia."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No longo prazo, a adoção de barreiras comerciais, como, por exemplo, tarifas e quotas à "
                       "importação, conduz ao aumento da taxa de câmbio real, o que ")
                    + vm("favorece o aumento das exportações líquidas da economia e a redução do déficit")
                    + az(" em conta corrente na economia.")),
        "poucas": ("No longo prazo, " + vd("NX = S − I") + ", e tarifas não mudam nem S nem I. A proteção "
                   + azb("aprecia") + " o câmbio real o bastante para anular a queda das importações: o comércio "
                   "encolhe, mas o saldo fica igual."),
        "destrinchando": [
            "Modelo de economia aberta de longo prazo (" + oc("Mankiw") + "): a saída líquida de capital, "
            + vd("S − I") + ", é dada pela poupança e pelo investimento e não depende do câmbio. As exportações "
            "líquidas precisam igualá-la: " + vd("NX = S − I") + ".",
            "Tarifa ou cota: a cada câmbio, importa-se menos → a curva de demanda por exportações líquidas se "
            "desloca para a direita. Como a oferta de moeda para o exterior (S − I) não se mexe, o ajuste é todo "
            "de preço: a moeda doméstica se " + azb("aprecia em termos reais") + ".",
            "A apreciação reduz exportações e devolve parte das importações até NX voltar ao nível inicial. "
            "Resultado: " + vd("menos comércio nos dois sentidos, mesmo saldo") + ". Exportadores perdem, "
            "setores protegidos ganham, e há perda de eficiência.",
            "Convenção de sinal: em Mankiw, o câmbio real é ε = e·P/P* (bens estrangeiros por bem doméstico), e "
            "“aumento” significa apreciação — por isso a primeira metade do item é coerente com o modelo. Na "
            "convenção brasileira (q = E·P*/P, R$ por US$), apreciação é <b>queda</b> de q. Em qualquer "
            "convenção, a conclusão sobre o saldo está errada.",
            "Para reduzir o déficit em conta corrente de forma duradoura, é preciso elevar S (por exemplo, "
            "consolidação fiscal) ou reduzir I — não proteger.",
            vm("Regra-âncora: no longo prazo, protecionismo aprecia o câmbio real e não altera NX = S − I."),
        ],
        "dissecando": (cz("[nexo indevido · meia-verdade]") + " A primeira parte (câmbio real sobe, isto é, "
                       "aprecia, na convenção de Mankiw) está certa; o erro é o nexo com o saldo. Intuição "
                       "mercantilista (“importar menos melhora as contas”) contra a identidade macro. Pista: o "
                       "“no longo prazo” chama a identidade S − I."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No longo prazo, tarifas à importação apreciam o câmbio real e deixam inalteradas as exportações "
            "líquidas.”</i> → CERTO",
            "<i>“No longo prazo, um aumento do déficit público reduz a poupança nacional, aprecia o câmbio real e "
            "reduz as exportações líquidas.”</i> → CERTO",
            "<i>“Tarifas reduzem as importações e, por isso, aumentam a poupança nacional.”</i> → ERRADO (nexo "
            "indevido: S não depende da política comercial)",
        ])],
        "reescrita": ("No longo prazo, a adoção de barreiras comerciais, como, por exemplo, tarifas e quotas à "
                      "importação, conduz ao aumento da taxa de câmbio real, o que " + hl("reduz as exportações e "
                      "anula a queda das importações, sem alterar as exportações líquidas da economia nem o "
                      "déficit") + " em conta corrente na economia."),
        "tipo_erro": ["NEXO_INDEVIDO", "MEIA_VERDADE"], "moduladores": ["no longo prazo"], "dificuldade": 3,
        "comentario_fonte": ("Tarifas reduzem importações e apreciam o câmbio real; a apreciação prejudica as "
                             "exportações e NX volta ao nível dado por S − I. Alguns comentários tratam “aumento da "
                             "taxa de câmbio real” como depreciação e o apontam como erro."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [{"ref": "IMAGEM 92–94", "tipo_fonte": "TEXTO", "lado": "verso", "acao": "absorvida"}],
        "alertas": ["texto_corrigido: “déficit de contracorrente” → “déficit em conta corrente”; numeração “228.” "
                    "retirada",
                    "qualidade_fonte: parte dos comentários lê “aumento da taxa de câmbio real” como depreciação; no "
                    "modelo de Mankiw, que o item segue, aumento de ε é apreciação — o erro do item está só na "
                    "conclusão sobre o saldo"],
    },
    # ------------------------------------------------------------------ E1-0669
    {
        "id": "ECO-E1-0669-1", "fonte_ref": "E1-0669", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_TPS25,
        "rotulo_item": "Item",
        "assertiva": ("No regime de câmbio flutuante, o valor da moeda é determinado pela oferta e demanda no "
                      "mercado, por isso o Banco Central do Brasil não pode intervir no mercado para evitar "
                      "movimentos desordenados da taxa de câmbio que ocorrem em momentos de instabilidade."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("No regime de câmbio flutuante, o valor da moeda é determinado pela oferta e demanda no "
                       "mercado, ") + vm("por isso o Banco Central do Brasil não pode intervir")
                    + az(" no mercado para evitar movimentos desordenados da taxa de câmbio que ocorrem em momentos "
                         "de instabilidade.")),
        "poucas": ("Câmbio flutuante não proíbe intervenção. O " + rx("Brasil") + " pratica "
                   + azb("flutuação administrada (suja)") + ": o Banco Central atua para conter "
                   + vd("disfuncionalidades") + " e volatilidade excessiva, sem fixar um nível."),
        "destrinchando": [
            "No câmbio flutuante, o preço da divisa sai do mercado: demandam dólares importadores e quem remete "
            "recursos ao exterior; ofertam exportadores e quem recebe recursos de fora.",
            azb("Flutuação limpa") + ": nenhuma intervenção (caso teórico, próximo de poucos países). "
            + azb("Flutuação suja ou administrada") + ": o banco central intervém pontualmente — sem meta de "
            "taxa — para suavizar movimentos bruscos e preservar o funcionamento do mercado.",
            "Instrumentos do " + rx("Banco Central do Brasil") + ": leilões de venda à vista (spot), "
            + azb("swaps cambiais") + " (dão proteção cambial sem gastar reservas, liquidados em reais), leilões "
            "de linha (venda com compromisso de recompra). Exemplos: crise de 2008, 2013 (programa de swaps), "
            "pandemia em 2020 e dezembro de 2024.",
            "Por que importa: oscilações bruscas afetam inflação (repasse cambial), balanços de empresas "
            "endividadas em dólar e a estabilidade financeira. Para intervir com credibilidade, é preciso "
            + azb("reservas") + " adequadas — o " + rx("Brasil") + " mantém cerca de " + vd("US$ 340–360 "
            "bilhões") + " ⏳ (out/2026).",
            vm("Regra-âncora: flutuante ≠ proibido intervir; o BC não persegue nível, mas pode conter "
               "disfuncionalidades."),
        ],
        "dissecando": (cz("[nexo indevido · restrição indevida]") + " A primeira oração é a definição correta; o "
                       "“por isso” fabrica uma consequência que não decorre dela e o “não pode” cria uma "
                       "proibição inexistente. 🔥 No CACD, “câmbio flutuante” costuma vir com a ressalva da "
                       "flutuação suja brasileira."),
        "modulos": [("😈 Para dificultar", [
            "<i>“No regime de câmbio flutuante, o Banco Central do Brasil pode intervir no mercado para conter "
            "movimentos desordenados, sem fixar um nível para a taxa.”</i> → CERTO",
            "<i>“As intervenções por swaps cambiais reduzem diretamente o estoque de reservas internacionais.”</i> "
            "→ ERRADO (swaps são liquidados em reais e não consomem reservas)",
        ])],
        "reescrita": ("No regime de câmbio flutuante, o valor da moeda é determinado pela oferta e demanda no "
                      "mercado, " + hl("mas isso não impede que o Banco Central do Brasil intervenha") + " no "
                      "mercado para evitar movimentos desordenados da taxa de câmbio que ocorrem em momentos de "
                      "instabilidade."),
        "tipo_erro": ["NEXO_INDEVIDO", "RESTRICAO"], "moduladores": ["não pode"], "dificuldade": 1,
        "comentario_fonte": ("No câmbio flutuante a taxa é de mercado, mas na flutuação suja o BC pode intervir "
                             "para evitar movimentos desordenados (leilões, swaps), o que exige reservas. Um "
                             "comentário de leitor sugere ambiguidade (flutuação pura × suja)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_TPS25,
                    "dado_aproximado: nível das reservas brasileiras em ordem de grandeza ⏳ (out/2026)"],
    },
    # ------------------------------------------------------------------ E1-0671
    {
        "id": "ECO-E1-0671-1", "fonte_ref": "E1-0671", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2025", "ano": 2025, "cacd": True, "errei": False,
        "comando": CMD_TPS25,
        "rotulo_item": "Item",
        "assertiva": ("Em um regime de câmbio fixo, que estabelece uma taxa de câmbio específica para uma moeda em "
                      "relação a outra, é indispensável, para a condução da política cambial, avaliar o volume de "
                      "reservas internacionais adequado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Em um regime de câmbio fixo, que estabelece uma taxa de câmbio específica para uma moeda em "
                      "relação a outra, é <u>indispensável</u>, para a condução da política cambial, avaliar o "
                      "volume de reservas internacionais adequado."),
        "poucas": ("Para sustentar a paridade, o banco central precisa comprar e vender divisas sempre que houver "
                   "pressão; sem " + azb("reservas") + " suficientes, o regime se torna vulnerável a "
                   + azb("ataques especulativos") + "."),
        "destrinchando": [
            "No câmbio fixo, o banco central se compromete a trocar moeda doméstica por estrangeira à taxa "
            "anunciada. Pressão de desvalorização → ele <b>vende</b> divisas (reservas caem); pressão de "
            "valorização → <b>compra</b> divisas (reservas sobem).",
            "Por isso a capacidade de defesa da paridade é limitada pelo estoque de reservas: o banco central "
            "emite a própria moeda, mas não emite dólares.",
            azb("Trilema de Mundell-Fleming") + ": não se têm, ao mesmo tempo, câmbio fixo, livre mobilidade "
            "de capitais e política monetária autônoma. Com capital móvel, fixar o câmbio subordina os juros "
            "à defesa da paridade.",
            "Quando as reservas se mostram insuficientes, o mercado antecipa a desvalorização e ataca a moeda: "
            "México (1994), crise asiática (1997), Rússia (1998), " + rx("Brasil") + " (janeiro de 1999), "
            "Argentina (2001–2002).",
            "Critérios de adequação usados na prática: meses de importação, cobertura da dívida externa de curto "
            "prazo (regra de " + oc("Guidotti-Greenspan") + ") e a métrica ARA do FMI.",
            vm("Regra-âncora: câmbio fixo exige reservas; sem elas, a paridade cai."),
        ],
        "dissecando": (cz("[literalidade · contraintuitivo]") + " O “indispensável” parece exagero e convida a "
                       "marcar ERRADO, mas aqui é verdadeiro: sem reservas não há como cumprir o compromisso de "
                       "troca à taxa fixada. Absolutos não são sempre falsos — teste o conteúdo."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Em regime de câmbio flutuante puro, o banco central não precisa de reservas para fixar a "
            "taxa.”</i> → CERTO",
            "<i>“Em regime de câmbio fixo com livre mobilidade de capitais, o banco central mantém plena autonomia "
            "para fixar os juros.”</i> → ERRADO (trilema: perde a autonomia monetária)",
        ])],
        "tipo_erro": ["LITERAL", "CONTRAINTUITIVO"], "moduladores": ["indispensável"], "dificuldade": 1,
        "comentario_fonte": ("A paridade é mantida por compra e venda de divisas com reservas; trilema de "
                             "Mundell-Fleming; reservas insuficientes levam a desvalorização ou mudança de regime "
                             "(México 1994, Brasil 1999)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [ALERTA_TPS25, "quase_duplicata: ECO-E1-0695-1 (mesma tese, outra prova)"],
    },
    # ------------------------------------------------------------------ E1-0695
    {
        "id": "ECO-E1-0695-1", "fonte_ref": "E1-0695", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_CLIP,
        "rotulo_item": "Item",
        "assertiva": ("Um regime de câmbio fixo exige que o banco central mantenha reservas internacionais "
                      "suficientes para sustentar a paridade da moeda doméstica frente a uma moeda estrangeira de "
                      "referência, comprando ou vendendo divisas conforme necessário."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Um regime de câmbio fixo <u>exige</u> que o banco central mantenha reservas internacionais "
                      "suficientes para sustentar a paridade da moeda doméstica frente a uma moeda estrangeira de "
                      "referência, comprando ou vendendo divisas conforme necessário."),
        "poucas": ("O compromisso de trocar moedas a um preço fixo só é crível se o banco central tiver "
                   + azb("divisas") + " para atender aos excessos de demanda do mercado."),
        "destrinchando": [
            "Mecânica (" + oc("Blanchard") + ", " + oc("Krugman") + "): à taxa fixada, o mercado de divisas "
            "raramente se equilibra sozinho. O banco central cobre a diferença: compra o excesso de oferta de "
            "divisas (acumula reservas, emite moeda doméstica) ou vende para atender ao excesso de demanda "
            "(perde reservas, recolhe moeda doméstica).",
            "Assimetria decisiva: defender a moeda contra a <b>valorização</b> é sempre possível (basta emitir "
            "moeda doméstica para comprar divisas); defendê-la contra a <b>desvalorização</b> esgota "
            "reservas, que são finitas.",
            "Efeito monetário: cada intervenção altera a " + azb("base monetária") + ". Para evitar isso, o banco "
            "central pode " + azb("esterilizar") + " com operações de mercado aberto — o que tem custo fiscal "
            "quando os juros domésticos superam o rendimento das reservas.",
            "Variante extrema: o " + azb("currency board") + " (Argentina 1991–2001, Hong Kong) exige cobertura "
            "integral da base monetária em divisas.",
            vm("Regra-âncora: câmbio fixo = compromisso de compra e venda de divisas; reservas são a munição."),
        ],
        "dissecando": (cz("[literalidade]") + " Definição operacional do regime. O verbo “exige” poderia parecer "
                       "forte, mas é exatamente a condição de funcionamento. Itens errados sobre o tema dizem que o "
                       "câmbio fixo “dispensa” reservas ou “preserva a autonomia monetária”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Num regime de câmbio fixo, o banco central só precisa de reservas para conter pressões de "
            "valorização da moeda doméstica.”</i> → ERRADO (inversão: é contra a desvalorização que as reservas "
            "se esgotam)",
            "<i>“No currency board, a base monetária deve ser integralmente lastreada em moeda estrangeira.”</i> "
            "→ CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["exige"], "dificuldade": 1,
        "comentario_fonte": ("Blanchard e Krugman: manter a taxa fixa exige que o BC troque moeda doméstica por "
                             "estrangeira ao preço estipulado, com estoque de reservas para acomodar excessos de "
                             "oferta ou demanda."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E1-0671-1 (mesma tese, outra prova)"],
    },
    # ------------------------------------------------------------------ E1-0696
    {
        "id": "ECO-E1-0696-1", "fonte_ref": "E1-0696", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "Clipping", "prova": "Simuladão Março/2026", "ano": 2026, "cacd": False,
        "errei": True,
        "comando": CMD_CLIP,
        "rotulo_item": "Item",
        "assertiva": ("Reduzir reservas internacionais sem ajustar a taxa de câmbio constitui um instrumento limitado "
                      "de política cambial contracionista, pois pode impactar negativamente a confiança de "
                      "investidores e gerar instabilidade financeira."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Reduzir reservas internacionais sem ajustar a taxa de câmbio constitui um instrumento "
                      "<u>limitado</u> de política cambial contracionista, pois <u>pode</u> impactar negativamente a "
                      "confiança de investidores e gerar instabilidade financeira."),
        "poucas": ("Vender reservas para segurar o câmbio recolhe moeda doméstica (efeito " + azb("contracionista")
                   + ") e tem limite: reservas são finitas, e a perda contínua delas sinaliza fragilidade e "
                   "convida a " + azb("ataques especulativos") + "."),
        "destrinchando": [
            "A operação: para impedir a depreciação, o banco central vende dólares das reservas. Recebe reais em "
            "troca, que saem de circulação — a " + azb("base monetária") + " cai (se não houver esterilização). "
            "Daí o caráter contracionista.",
            "Por que “limitado”: o banco central emite reais, não dólares. Cada venda reduz um estoque finito; a "
            "capacidade de defesa tem prazo de validade.",
            "Por que afeta a confiança: reservas funcionam como " + azb("colchão de segurança") + " — garantem "
            "pagamento da dívida externa e saída de capitais. Ver esse colchão encolher mês a mês faz o "
            "investidor antecipar o fim da defesa: “melhor comprar dólar agora, enquanto está barato”. A corrida "
            "acelera a perda de reservas e pode forçar a desvalorização abrupta.",
            "O paradoxo: <b>ter</b> reservas dá confiança; <b>queimá-las</b> para segurar a cotação a tira. "
            + rx("Brasil") + " em 1998–1999: as reservas caíram de " + vd("mais de US$ 70 bilhões") + " (abril "
            "de 1998) para algo em torno de " + vd("US$ 40 bilhões") + " na virada para 1999, apesar do acordo "
            "com o FMI, e o real passou a flutuar em janeiro de 1999.",
            vm("Regra-âncora: reserva parada dá confiança; reserva queimada para segurar câmbio a corrói."),
        ],
        "dissecando": (cz("[contraintuitivo · modulador relativo]") + " Quem pensa em reservas só como proteção "
                       "acha que usá-las gera confiança e marca ERRADO. O ponto está no verbo “reduzir” e no "
                       "“sem ajustar a taxa”: é a defesa de uma paridade que o mercado já questiona. O “pode” "
                       "protege o item."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A venda de reservas para defender a taxa de câmbio, se não esterilizada, expande a base "
            "monetária.”</i> → ERRADO (inversão: contrai)",
            "<i>“Um nível elevado de reservas tende a reduzir a percepção de risco do país.”</i> → CERTO",
        ])],
        "tipo_erro": ["CONTRAINTUITIVO", "MODULADOR_RELATIVO"], "moduladores": ["pode", "limitado"],
        "dificuldade": 2,
        "comentario_fonte": ("Vender reservas para defender o câmbio retira moeda nacional (contracionista se não "
                             "esterilizado); o instrumento é limitado pelo estoque finito e a queda contínua das "
                             "reservas mina a credibilidade, incentivando ataques especulativos (Brasil 1999)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (206).png", "tipo_fonte": "não informado", "lado": "verso",
                           "acao": "irrecuperavel"}],
        "alertas": ["dado_aproximado: trajetória das reservas brasileiras em 1998 citada em ordem de grandeza"],
    },
    # ------------------------------------------------------------------ E1-0751
    {
        "id": "ECO-E1-0751-1", "fonte_ref": "E1-0751", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "Banca não identificada", "prova": "", "ano": 2019, "cacd": False,
        "errei": False,
        "comando": "Acerca das intervenções do Banco Central no mercado de câmbio, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Ao alienar reservas em moeda estrangeira, o Banco Central reduz a oferta de moeda doméstica "
                      "disponível. Na ausência de operações de esterilização compensatórias, essa transação poderia "
                      "ter como resultado a depreciação da moeda doméstica."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Ao alienar reservas em moeda estrangeira, o Banco Central reduz a oferta de moeda doméstica "
                       "disponível. Na ausência de operações de esterilização compensatórias, essa transação "
                       "poderia ter como resultado a ") + vm("depreciação") + az(" da moeda doméstica.")),
        "poucas": ("Vender divisas aumenta a oferta de dólares e recolhe moeda doméstica: os dois efeitos "
                   "apontam para a " + azb("apreciação") + " da moeda nacional, não para a depreciação."),
        "destrinchando": [
            "Balanço do banco central: ao vender US$ 1 bilhão das reservas, o " + azb("ativo") + " (reservas) "
            "cai, e o banco central recebe moeda doméstica em troca, que deixa de circular — o " + azb("passivo "
            "monetário") + " (base monetária) cai na mesma medida. A primeira frase do item está correta.",
            "Efeito no câmbio, canal direto: mais dólares ofertados no mercado → a cotação (moeda doméstica por "
            "dólar) cai → " + vd("apreciação") + ".",
            "Canal monetário (sem esterilização): menos moeda doméstica → juros internos sobem → entra capital → "
            "reforço da " + vd("apreciação") + ".",
            "Esterilização: para que a base monetária não caia, o banco central compraria títulos no mercado "
            "aberto (ou reduziria compromissadas), devolvendo a liquidez. A operação vira só uma troca de "
            "composição — ainda aprecia pela via direta, mas sem o efeito sobre os juros.",
            "Espelho: comprar divisas expande a base e tende a depreciar a moeda doméstica; para evitar a "
            "pressão inflacionária, o banco central esteriliza vendendo títulos.",
            vm("Regra-âncora: BC vende reservas → base ↓ e oferta de dólares ↑ → moeda doméstica se aprecia."),
        ],
        "dissecando": (cz("[inversão]") + " A primeira frase (base cai) está certa e dá credibilidade ao item; o "
                       "erro está na consequência, invertida. Pista: menos moeda doméstica em circulação a torna "
                       "mais escassa — e, portanto, mais valiosa."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao adquirir reservas em moeda estrangeira, o Banco Central expande a base monetária; sem "
            "esterilização, a transação tende a depreciar a moeda doméstica.”</i> → CERTO",
            "<i>“A venda de reservas esterilizada reduz a base monetária.”</i> → ERRADO (a esterilização "
            "justamente a mantém)",
        ])],
        "reescrita": ("Ao alienar reservas em moeda estrangeira, o Banco Central reduz a oferta de moeda doméstica "
                      "disponível. Na ausência de operações de esterilização compensatórias, essa transação poderia "
                      "ter como resultado a " + hl("apreciação") + " da moeda doméstica."),
        "tipo_erro": ["INVERSAO"], "moduladores": ["poderia"], "dificuldade": 2,
        "comentario_fonte": ("Comentário trata da aquisição (e não da alienação) de divisas: compra eleva o ativo e "
                             "a base monetária, e a liquidez adicional pressionaria a cotação e os preços."),
        "qualidade_fonte": "com_erro",
        "figuras_fonte": [],
        "alertas": ["qualidade_fonte: o comentário de origem descreve a compra de divisas, enquanto o item trata da "
                    "venda (alienação); explicação refeita para a operação do item"],
    },
    # ------------------------------------------------------------------ E1-0778
    {
        "id": "ECO-E1-0778-1", "fonte_ref": "E1-0778", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": False,
        "comando": "Acerca da gestão das reservas internacionais pela autoridade monetária, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("A gestão da autoridade monetária sobre os investimentos das reservas internacionais não é "
                      "afetada pelos níveis de juros nem pelas paridades das moedas de investimento contra a moeda "
                      "numerário de reserva de valor."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("A gestão da autoridade monetária sobre os investimentos das reservas internacionais ")
                    + vm("não é afetada") + az(" pelos níveis de juros ") + vm("nem") + az(" pelas paridades das "
                    "moedas de investimento contra a moeda numerário de reserva de valor.")),
        "poucas": ("Reservas são uma " + azb("carteira de investimentos") + ": o retorno depende dos " + vd("juros")
                   + " (títulos soberanos) e das " + vd("paridades") + " entre as moedas da carteira e a moeda "
                   "numerário (o dólar). Ambos afetam a gestão."),
        "destrinchando": [
            "O " + rx("Banco Central do Brasil") + " administra as reservas segundo três critérios, nessa ordem: "
            + azb("liquidez, segurança e rentabilidade") + ". A carteira concentra-se em títulos soberanos de "
            "alta qualidade, sobretudo americanos, com parcelas em outras moedas e em ouro.",
            azb("Juros") + ": determinam o rendimento dos títulos (“carregamento”) e o valor de mercado deles — "
            "alta de juros reduz o preço dos títulos já em carteira (marcação a mercado). Juros americanos "
            "altos elevam o ganho de carregamento.",
            azb("Paridades") + ": o desempenho é medido em dólar (a " + azb("moeda numerário") + "). Ativos em "
            "euro, libra, iene ou yuan ganham ou perdem valor conforme essas moedas se movem contra o dólar; "
            "uma valorização do dólar gera resultado negativo na parcela em outras moedas.",
            "Por isso o banco central define uma " + azb("carteira de referência") + " (benchmark), com metas de "
            "composição por moeda e de prazo médio (duration), e divulga relatórios anuais de gestão das "
            "reservas explicando o resultado por juros e por paridades.",
            "Distinção útil: em reais, as reservas também variam com o câmbio R$/US$ — o que afeta o resultado "
            "cambial do banco central e as transferências ao Tesouro — mas isso é efeito de valoração, não "
            "decisão de gestão da carteira.",
            vm("Regra-âncora: reservas = carteira em moeda forte; juros e paridades definem o retorno e orientam a "
               "gestão."),
        ],
        "dissecando": (cz("[inversão · modulador absoluto]") + " Nega as duas variáveis que mais pesam na gestão "
                       "(“não é afetada… nem…”). O jargão (“moeda numerário de reserva de valor”) intimida, mas "
                       "basta pensar nas reservas como uma aplicação financeira: nenhuma aplicação ignora juros "
                       "e câmbio."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A política de investimento das reservas pelo Banco Central do Brasil obedece aos critérios de "
            "liquidez, segurança e rentabilidade.”</i> → CERTO",
            "<i>“A valorização do dólar frente às demais moedas da carteira eleva o retorno das reservas medido em "
            "dólar.”</i> → ERRADO (inversão: reduz o valor dos ativos em outras moedas)",
        ])],
        "reescrita": ("A gestão da autoridade monetária sobre os investimentos das reservas internacionais "
                      + hl("é afetada") + " pelos níveis de juros " + hl("e") + " pelas paridades das moedas de "
                      "investimento contra a moeda numerário de reserva de valor."),
        "tipo_erro": ["INVERSAO", "GENERALIZACAO"], "moduladores": ["não", "nem"], "dificuldade": 2,
        "comentario_fonte": ("Juros e paridades influenciam o valor das carteiras: juros altos geram ganho de "
                             "carregamento e a valorização do dólar gera resultado negativo; um comentário "
                             "confunde a gestão com fluxos de divisas na economia."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0795
    {
        "id": "ECO-E1-0795-1", "fonte_ref": "E1-0795", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2024", "ano": 2024, "cacd": True, "errei": True,
        "comando": ("Em relação à macroeconomia internacional dos fluxos de bens e de capital, julgue o item a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Um superávit comercial produz aumento no passivo da autoridade monetária, como um banco "
                      "central, por exemplo, uma vez que as reservas cambiais são incluídas na base monetária do "
                      "país."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um superávit comercial ") + vm("produz") + az(" aumento no passivo da autoridade monetária, "
                    "como um banco central, por exemplo, ") + vm("uma vez que as reservas cambiais são incluídas "
                    "na base monetária") + az(" do país.")),
        "poucas": ("Reservas cambiais estão no " + azb("ativo") + " do banco central; a " + azb("base monetária")
                   + " está no passivo. Se o banco central compra as divisas e emite moeda, os dois lados crescem "
                   "— mas as reservas não “entram” na base."),
        "destrinchando": [
            "Balanço simplificado do banco central: " + vd("ativo") + " = reservas internacionais + títulos "
            "públicos + crédito a bancos; " + vd("passivo") + " = base monetária (papel-moeda emitido + reservas "
            "bancárias) + depósitos do Tesouro + compromissadas.",
            "Superávit comercial: exportadores recebem dólares e os vendem aos bancos. Só se o " + azb("banco "
            "central comprar") + " essas divisas é que as reservas sobem (ativo) e, como contrapartida, ele "
            "paga em reais recém-emitidos — a base monetária sobe (passivo). Sob câmbio flutuante sem "
            "intervenção, o dólar pode ficar no setor privado e o balanço do banco central não se altera.",
            "Mesmo quando há compra, o aumento do passivo pode ser neutralizado: na " + azb("esterilização") + ", "
            "o banco central vende títulos (compromissadas), trocando base monetária por outro passivo "
            "não monetário.",
            "Logo há dois erros: a automaticidade (“produz”) e a justificativa (as reservas seriam parte da "
            "base). As reservas são o lastro do lado do ativo; a moeda emitida para comprá-las é que integra a "
            "base.",
            vm("Regra-âncora: reservas = ativo do BC; base monetária = passivo do BC."),
        ],
        "dissecando": (cz("[troca de conceito · nexo indevido]") + " Mistura as duas pontas do balanço: a "
                       "contrapartida (moeda emitida) é que vai para a base, não as reservas. Quem lembra que "
                       "“reservas sobem e base sobe juntas” marca CERTO sem ler o “uma vez que”. 🔥 O CACD "
                       "cobra contabilidade do banco central com frequência."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A compra de divisas pelo banco central, sem esterilização, eleva simultaneamente as reservas "
            "internacionais, no ativo, e a base monetária, no passivo.”</i> → CERTO",
            "<i>“A esterilização de uma compra de divisas mantém a base monetária e reduz as reservas "
            "internacionais.”</i> → ERRADO (as reservas permanecem maiores; muda só a composição do passivo)",
        ])],
        "reescrita": ("Um superávit comercial " + hl("pode produzir") + " aumento no passivo da autoridade "
                      "monetária, como um banco central, por exemplo, " + hl("quando este compra as divisas e emite "
                      "moeda; as reservas cambiais, porém, são registradas no ativo, e não na base monetária")
                      + " do país."),
        "tipo_erro": ["TROCA_CONCEITO", "NEXO_INDEVIDO"], "moduladores": ["uma vez que"], "dificuldade": 2,
        "comentario_fonte": ("Reservas são ativo do Bacen; a base monetária é passivo. Com a compra de divisas sem "
                             "esterilização, a base cresce na mesma proporção, mas as reservas não são incluídas "
                             "nela. Inclui revisão longa do balanço de pagamentos."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "image (272).png", "tipo_fonte": "não informado", "lado": "verso",
                           "acao": "irrecuperavel"},
                          {"ref": "41c9ffda-ec50-4fe0-b718-b85c018e22e6", "tipo_fonte": "não informado",
                           "lado": "verso", "acao": "irrecuperavel"}],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E1-0820
    {
        "id": "ECO-E1-0820-1", "fonte_ref": "E1-0820", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "CEBRASPE", "prova": "IRBr/CACD/2026", "ano": 2026, "cacd": True, "errei": False,
        "comando": ("Acerca de macroeconomia aberta, regime cambial e determinação da taxa de câmbio, julgue o item "
                    "subsequente, considerando o texto a seguir."),
        "excerto": ("<p><i>Em economias abertas, choques de confiança e alterações no prêmio de risco podem afetar "
                    "fluxos de capitais e pressionar a taxa de câmbio. A resposta de política econômica — "
                    "incluindo-se o uso de juros, intervenção e reservas — depende, entre outros fatores, do regime "
                    "cambial vigente e das restrições impostas pelo grau de mobilidade de capitais. Ademais, "
                    "distinções conceituais entre taxa de câmbio nominal e taxa de câmbio real são relevantes para "
                    "analisar preços relativos e competitividade, assim como para discutir mecanismos de "
                    "transmissão do câmbio para a inflação.</i></p>"),
        "rotulo_item": "Item",
        "assertiva": ("São trade-offs típicos da política cambial tanto a escolha entre suavizar oscilações do câmbio "
                      "e preservar reservas internacionais quanto o dilema entre manter a atividade econômica em "
                      "sua meta e conter a inflação doméstica."),
        "gabarito": "ANULADO", "gabarito_origem": "fonte", "status": "anulado",
        "anotada": (az("São trade-offs típicos da política cambial tanto a escolha entre suavizar oscilações do "
                       "câmbio e preservar reservas internacionais quanto ")
                    + vm("o dilema entre manter a atividade econômica em sua meta e conter a inflação doméstica")
                    + az(".")),
        "poucas": ("O primeiro dilema (intervir × preservar reservas) é tipicamente " + azb("cambial") + "; o "
                   "segundo (atividade × inflação) é o dilema clássico da " + azb("política monetária") + ", mas "
                   "também passa pelo câmbio. A ambiguidade derrubou o gabarito preliminar (ERRADO)."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "O gabarito preliminar era " + vm("ERRADO") + " e o item foi " + vd("anulado") + ". A "
                          "fonte não traz a justificativa da banca. Motivo provável: a leitura que sustentava o "
                          "ERRADO — atividade × inflação seria trade-off da política monetária, não da cambial — "
                          "é discutível, porque o câmbio afeta as duas variáveis (exportações líquidas e repasse "
                          "cambial) e a política cambial enfrenta, sim, esse dilema, sobretudo em regimes de câmbio "
                          "fixo ou administrado. A redação admite as duas respostas.")],
        "destrinchando": [
            azb("Suavizar o câmbio × preservar reservas") + ": cada leilão de venda à vista reduz o estoque de "
            "reservas, que é finito e serve de seguro contra crises. Intervir demais enfraquece o colchão e pode "
            "até alimentar ataques especulativos; intervir de menos deixa a volatilidade contaminar inflação e "
            "balanços. Os " + azb("swaps cambiais") + " do " + rx("Banco Central do Brasil") + " foram a "
            "resposta a esse dilema: oferecem proteção sem gastar reservas.",
            azb("Atividade × inflação") + ": é o dilema canônico da política monetária (curva de " + oc("Phillips")
            + ", regra de " + oc("Taylor") + "). Em economia aberta, ele aparece também no câmbio: depreciar "
            "estimula exportações e atividade, mas eleva a inflação pelo " + azb("repasse cambial") + "; "
            "apreciar ajuda a desinflação, mas tira competitividade.",
            "Outros trade-offs da política cambial: competitividade × estabilidade de preços; acumular reservas × "
            "custo fiscal de carregá-las (esterilização com juros domésticos acima dos externos); câmbio fixo × "
            "autonomia monetária (o " + azb("trilema") + ").",
            "Sob metas de inflação e câmbio flutuante (o arranjo brasileiro desde 1999), o câmbio não é meta: "
            "entra na política monetária como canal de transmissão. Isso reforça a leitura de que "
            "atividade × inflação é, antes de tudo, dilema monetário — e explica a escolha preliminar da banca.",
            vm("Regra-âncora: intervir × preservar reservas = dilema cambial típico; atividade × inflação = dilema "
               "monetário que o câmbio também transmite."),
        ],
        "dissecando": (cz("[outro: ambiguidade de enquadramento]") + " O item soma um trade-off "
                       "inequivocamente cambial a um que é primariamente monetário. A banca apostou que o "
                       "candidato rejeitaria o segundo (ERRADO), mas a fronteira entre política cambial e "
                       "monetária é porosa em economia aberta — e a anulação reconheceu isso."),
        "modulos": [("😈 Para dificultar", [
            "<i>“É trade-off típico da política cambial a escolha entre suavizar oscilações do câmbio e preservar "
            "reservas internacionais.”</i> → CERTO",
            "<i>“Intervenções por swaps cambiais consomem diretamente as reservas internacionais.”</i> → ERRADO "
            "(são liquidadas em reais)",
        ])],
        "tipo_erro": ["OUTRO"], "moduladores": ["típicos", "tanto… quanto"], "dificuldade": 3,
        "comentario_fonte": "Apenas a anotação “ERRADO > ANULADA”, sem comentário.",
        "qualidade_fonte": "ausente",
        "figuras_fonte": [],
        "alertas": ["nota_redacao: gabarito preliminar ERRADO, alterado para ANULADO; a fonte não traz a "
                    "justificativa da banca — motivo da anulação inferido e marcado como provável no card"],
    },
    # ------------------------------------------------------------------ E1-0870
    {
        "id": "ECO-E1-0870-1", "fonte_ref": "E1-0870", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Simulado Julho/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "Acerca da política cambial e das operações de esterilização, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Se o objetivo de uma política cambial é promover a valorização da taxa de câmbio sem alterar o "
                      "nível de liquidez da economia em moeda nacional, um mecanismo eficiente seria a venda de "
                      "determinado montante das reservas cambiais pelo Banco Central e a compra do montante "
                      "equivalente em moeda nacional, realizando ainda uma ação esterilizante de compra de títulos "
                      "no mercado interno em valor correspondente à operação cambial."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Se o objetivo de uma política cambial é promover a valorização da taxa de câmbio sem alterar "
                      "o nível de liquidez da economia em moeda nacional, um mecanismo eficiente seria a "
                      "<u>venda</u> de determinado montante das reservas cambiais pelo Banco Central e a compra do "
                      "montante equivalente em moeda nacional, realizando ainda uma ação esterilizante de "
                      "<u>compra de títulos</u> no mercado interno em valor correspondente à operação cambial."),
        "poucas": ("Vender divisas valoriza a moeda nacional, mas recolhe liquidez; comprar títulos no mesmo valor "
                   "devolve a liquidez. É a " + azb("intervenção esterilizada") + ": muda o câmbio sem mudar a "
                   "base monetária."),
        "destrinchando": [
            "Passo 1 — venda de reservas: o banco central oferta dólares e recebe moeda nacional. Mais dólares "
            "no mercado → " + vd("valorização") + " da moeda doméstica. Efeito colateral: a base monetária cai "
            "(liquidez ↓, juros ↑).",
            "Passo 2 — esterilização: o banco central " + azb("compra títulos") + " no mercado aberto pagando "
            "com moeda nova, no mesmo valor. A base volta ao nível inicial. No balanço: reservas ↓ e títulos ↑ "
            "no ativo; o passivo monetário fica igual.",
            "Regra de sinal da esterilização: compra de divisas (injeta liquidez) → esteriliza-se " + vm("vendendo")
            + " títulos; venda de divisas (enxuga liquidez) → esteriliza-se " + vm("comprando") + " títulos. O "
            "item traz a combinação correta.",
            "Eficácia: com mobilidade perfeita de capitais e ativos domésticos e externos substitutos perfeitos, "
            "a intervenção esterilizada perde força — sem mudar os juros, o câmbio tende a voltar. Ela funciona "
            "melhor pelo " + azb("canal de portfólio") + " (ativos imperfeitamente substitutos) e pelo "
            + azb("canal de sinalização") + " (indica a intenção do banco central).",
            vm("Regra-âncora: intervenção esterilizada = operação cambial + operação de mercado aberto de sinal "
               "oposto sobre a liquidez."),
        ],
        "dissecando": (cz("[detalhe]") + " O item é longo para esconder a direção de duas operações. Teste: a "
                       "venda de divisas enxuga reais, então a esterilização precisa injetá-los — compra de "
                       "títulos. A versão errada típica troca para “venda de títulos”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…realizando ainda uma ação esterilizante de venda de títulos no mercado interno em valor "
            "correspondente à operação cambial.”</i> → ERRADO (sinal trocado: enxugaria ainda mais a liquidez)",
            "<i>“Com mobilidade perfeita de capitais e substituição perfeita entre ativos, a intervenção "
            "esterilizada tem efeito duradouro sobre o câmbio.”</i> → ERRADO (perde eficácia)",
        ])],
        "tipo_erro": ["DETALHE"], "moduladores": ["eficiente"], "dificuldade": 2,
        "comentario_fonte": ("Repete o enunciado e define política esterilizante como a que reverte o impacto da "
                             "operação sobre outros segmentos da economia."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00104
    {
        "id": "ECO-E2-L00104-1", "fonte_ref": "E2-L00104", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": "Sobre o equilíbrio de mercado e as intervenções no mercado cambial, julgue a assertiva a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("O Banco Central tem a possibilidade de adotar políticas cambiais para ajustar a quantidade de "
                      "moeda nacional e estrangeira dentro do sistema. Ao vender dólares no mercado, o Banco Central "
                      "retira moeda estrangeira do sistema, o que leva à desvalorização do real."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("O Banco Central tem a possibilidade de adotar políticas cambiais para ajustar a quantidade "
                       "de moeda nacional e estrangeira dentro do sistema. Ao vender dólares no mercado, o Banco "
                       "Central ") + vm("retira") + az(" moeda estrangeira ") + vm("do") + az(" sistema, o que leva "
                       "à ") + vm("desvalorização") + az(" do real.")),
        "poucas": ("Vender dólares " + azb("injeta") + " moeda estrangeira no mercado (e retira reais): o dólar "
                   "fica mais abundante e o real se " + azb("valoriza") + "."),
        "destrinchando": [
            "Quem vende dólares os <b>entrega</b> ao mercado. O Banco Central tira dólares das reservas e os "
            "coloca nas mãos de bancos e empresas — a oferta de divisas aumenta.",
            "No mercado de câmbio, mais oferta de dólares com a mesma demanda → a cotação (R$/US$) " + vd("cai")
            + " → o real se " + vd("valoriza") + ". É o que o Banco Central faz em momentos de depreciação "
            "brusca, por leilões à vista ou de linha.",
            "Do outro lado, o Banco Central recebe reais: a base monetária cai (se não houver esterilização), o "
            "que também puxa para a valorização via juros.",
            "Operação inversa: comprar dólares retira divisas do mercado e injeta reais — a cotação sobe e o "
            "real se desvaloriza. Foi o que o Brasil fez entre 2006 e 2012 para acumular reservas e conter a "
            "apreciação.",
            vm("Regra-âncora: BC vende dólar → oferta de US$ ↑ → real se valoriza; BC compra dólar → real se "
               "desvaloriza."),
        ],
        "grafico_verso": "ECO-E2-L00104-1-V1",
        "dissecando": (cz("[inversão]") + " Inverte o sentido do fluxo (vender = “retirar”) e, por coerência, o "
                       "efeito. Teste do bom senso: o comprador dos dólares vendidos pelo Banco Central é o "
                       "mercado, que passa a ter mais divisas, não menos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Ao comprar dólares no mercado, o Banco Central retira moeda estrangeira do sistema, o que tende "
            "a desvalorizar o real.”</i> → CERTO",
            "<i>“Ao vender dólares, o Banco Central expande a base monetária.”</i> → ERRADO (inversão: recebe "
            "reais e contrai a base)",
        ])],
        "reescrita": ("O Banco Central tem a possibilidade de adotar políticas cambiais para ajustar a quantidade de "
                      "moeda nacional e estrangeira dentro do sistema. Ao vender dólares no mercado, o Banco Central "
                      + hl("injeta") + " moeda estrangeira " + hl("no") + " sistema, o que leva à "
                      + hl("valorização") + " do real."),
        "tipo_erro": ["INVERSAO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Vender dólares torna-os menos escassos e valoriza o real; a intervenção serve para "
                             "controlar a desvalorização tornando o dólar mais abundante."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L01746
    {
        "id": "ECO-E2-L01746-1", "fonte_ref": "E2-L01746", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "Prof. Rodrigo Teixeira", "prova": "Intensivo Pré-TPS/2023", "ano": 2023,
        "cacd": False, "errei": False,
        "comando": "A respeito do processo de oferta de moeda, julgue o item a seguir.",
        "rotulo_item": "Item",
        "assertiva": ("Tudo o mais constante, há um aumento da base monetária quando o Banco Central compra dólares "
                      "dos bancos, elevando as reservas internacionais, de maneira que para manter a liquidez "
                      "constante, a autoridade monetária deve simultaneamente vender títulos do Tesouro no mercado "
                      "aberto, o que eleva a dívida pública."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Tudo o mais constante, há um aumento da base monetária quando o Banco Central compra dólares "
                      "dos bancos, elevando as reservas internacionais, de maneira que para manter a liquidez "
                      "constante, a autoridade monetária deve simultaneamente <u>vender</u> títulos do Tesouro no "
                      "mercado aberto, o que <u>eleva a dívida pública</u>."),
        "poucas": ("É a " + azb("esterilização") + " de compras de divisas: a compra de dólares expande a base; a "
                   "venda de títulos a recolhe — e os títulos em poder do mercado aumentam a " + vd("dívida "
                   "bruta") + "."),
        "destrinchando": [
            "Compra de dólares: o Banco Central paga em reais novos — reservas ↑ (ativo) e " + azb("base "
            "monetária") + " ↑ (passivo). Mais liquidez pressiona os juros para baixo e a inflação para cima.",
            "Esterilização: para manter a meta de juros, o Banco Central vende títulos (no " + rx("Brasil")
            + ", por " + azb("operações compromissadas") + " com títulos do Tesouro de sua carteira). Os reais "
            "voltam ao Banco Central; a base retorna ao nível inicial.",
            "Efeito fiscal: os títulos que passam ao mercado elevam a " + vd("dívida bruta do governo geral") + " "
            "(o BCB inclui as compromissadas na DBGG). A " + azb("dívida líquida") + " não sobe na mesma medida, "
            "porque as reservas são um ativo do setor público.",
            "Custo de carregamento: o setor público paga juros domésticos (Selic) sobre a dívida e recebe juros "
            "externos baixos sobre as reservas. Esse diferencial foi o “custo das reservas” no período de "
            "acumulação acelerada (2006–2012), quando as reservas passaram de cerca de " + vd("US$ 50 bi") + " "
            "para mais de " + vd("US$ 370 bi") + ".",
            vm("Regra-âncora: compra de divisas + esterilização = reservas ↑, base estável, dívida bruta ↑."),
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Descrição correta, passo a passo, da esterilização. "
                       "O detalhe que derruba candidatos é a última oração: parece que a operação é neutra, mas "
                       "ela aumenta a dívida bruta. Versões erradas trocam “vender” por “comprar” títulos."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…para manter a liquidez constante, a autoridade monetária deve comprar títulos no mercado "
            "aberto.”</i> → ERRADO (sinal trocado: comprar títulos injetaria mais liquidez)",
            "<i>“A esterilização de compras de divisas tem custo fiscal quando a taxa de juros doméstica supera a "
            "remuneração das reservas.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["tudo o mais constante", "deve"], "dificuldade": 2,
        "comentario_fonte": ("Compra de dólares expande a base; o BC vende títulos para retirar o excesso de "
                             "liquidez, o que aumenta a dívida pública mobiliária em poder do mercado (custo fiscal "
                             "da esterilização)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["dado_aproximado: evolução das reservas entre 2006 e 2012 em ordem de grandeza"],
    },
    # ------------------------------------------------------------------ E3-L00418
    {
        "id": "ECO-E3-L00418-1", "fonte_ref": "E3-L00418", "destino": "67", "subtema": H2["res"],
        "tipo": "C/E", "banca": "Nidi/Jacqueline Bueno", "prova": "Outubro/2024", "ano": 2024, "cacd": False,
        "errei": False,
        "comando": ("A respeito dos efeitos que alterações na política monetária ou a flutuação do mercado cambial "
                    "produzem sobre a base monetária e a liquidez do sistema financeiro nacional, julgue o item a "
                    "seguir."),
        "rotulo_item": "Item",
        "assertiva": ("Uma desvalorização cambial tende a elevar o valor das reservas internacionais em moeda "
                      "doméstica. Sendo assim, em resposta a uma desvalorização da moeda doméstica, haverá uma "
                      "expansão da base monetária."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Uma desvalorização cambial tende a elevar o valor das reservas internacionais em moeda "
                       "doméstica. ") + vm("Sendo assim") + az(", em resposta a uma desvalorização da moeda "
                       "doméstica, ") + vm("haverá uma") + az(" expansão da base monetária.")),
        "poucas": ("A desvalorização gera um " + azb("ganho contábil") + " nas reservas medidas em reais, mas não "
                   "cria moeda: a base monetária só se expande se o Banco Central " + azb("comprar ativos") + " ou "
                   "emitir moeda de fato."),
        "destrinchando": [
            "Primeira frase, correta: US$ 100 bilhões de reservas valem R$ 500 bilhões a R$ 5,00/US$ e "
            + vd("R$ 600 bilhões") + " a R$ 6,00/US$. É uma " + azb("reavaliação") + " do ativo do Banco "
            "Central.",
            "A base monetária (papel-moeda emitido + reservas bancárias) só cresce quando o Banco Central põe "
            "moeda em circulação: comprando divisas ou títulos, concedendo redesconto, ou quando o Tesouro gasta "
            "recursos da Conta Única. Reavaliar um ativo não move nenhum real para fora do Banco Central.",
            "Onde o ganho vai parar: no " + azb("resultado cambial") + " do Banco Central. No " + rx("Brasil")
            + ", a Lei nº " + vd("13.820/2019") + " separa esse resultado do operacional: o ganho cambial "
            "positivo forma reserva de resultado, e a transferência ao Tesouro só ocorre em situações "
            "previstas (como grave restrição de liquidez da dívida), para evitar monetização indireta.",
            "Canal indireto possível: se o ganho fosse transferido ao Tesouro e gasto, a base se expandiria — "
            "mas isso exige decisões e, mesmo assim, pode ser esterilizado por compromissadas. Não há relação "
            "automática.",
            vm("Regra-âncora: valorizar reservas em reais ≠ emitir moeda; base monetária só muda com operação "
               "efetiva."),
        ],
        "dissecando": (cz("[nexo indevido]") + " Duas afirmações ligadas por um “sendo assim” que fabrica "
                       "causalidade: a primeira é verdadeira; a segunda não decorre dela. O “haverá” "
                       "(certeza) reforça o erro. Pista: reavaliação contábil é efeito de estoque, base monetária "
                       "é fluxo de moeda."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Uma desvalorização cambial eleva o valor em reais das reservas internacionais, gerando resultado "
            "cambial positivo para o Banco Central.”</i> → CERTO",
            "<i>“A compra de divisas pelo Banco Central, sem esterilização, expande a base monetária.”</i> → "
            "CERTO",
        ])],
        "reescrita": ("Uma desvalorização cambial tende a elevar o valor das reservas internacionais em moeda "
                      "doméstica. " + hl("Ainda assim") + ", em resposta a uma desvalorização da moeda doméstica, "
                      + hl("não haverá, por si só,") + " expansão da base monetária."),
        "tipo_erro": ["NEXO_INDEVIDO"], "moduladores": ["sendo assim", "haverá"], "dificuldade": 2,
        "comentario_fonte": ("A desvalorização eleva o valor contábil das reservas, mas o ganho patrimonial não cria "
                             "moeda nova; a base só se expande com ação ativa do BC (compra de divisas, menos "
                             "esterilização, monetização)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [{"ref": "IMAGEM 587–592", "tipo_fonte": "TEXTO/DIAGRAMA", "lado": "verso",
                           "acao": "absorvida"}],
        "alertas": [],
    },
]
