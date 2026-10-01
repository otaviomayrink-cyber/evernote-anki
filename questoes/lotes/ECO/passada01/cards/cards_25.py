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
    # ------------------------------------------------------------------ E2-L00045
    {
        "id": "ECO-E2-L00045-1", "fonte_ref": "E2-L00045", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Externalidades são impactos econômicos que fogem ao controle de quem os gera. Por exemplo, "
                      "quando uma empresa desenvolve uma tecnologia inovadora, invariavelmente, causa esforços "
                      "adicionais em outras empresas do setor para se adaptarem à nova tecnologia, caracterizando "
                      "uma externalidade negativa."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Externalidades são impactos econômicos que fogem ao controle de quem os gera. Por "
                       "exemplo, quando uma empresa desenvolve uma tecnologia inovadora, ")
                    + vm("invariavelmente, causa esforços adicionais em outras empresas do setor para se "
                         "adaptarem à nova tecnologia")
                    + az(", caracterizando uma externalidade ") + vm("negativa") + az(".")),
        "poucas": ("A inovação que se difunde pelo setor é o exemplo-padrão de " + azb("externalidade "
                   "positiva") + " (transbordamento de conhecimento). O custo de adaptação imposto pela "
                   "concorrência atua via mercado e não configura externalidade negativa."),
        "destrinchando": [
            azb("Externalidade") + " = efeito da ação de um agente sobre o bem-estar de terceiros que <b>não é "
            "compensado pelo preço</b>. O que a define não é “fugir ao controle”, mas ficar fora do sistema "
            "de preços: quem gera não paga (se negativa) nem recebe (se positiva).",
            "Inovação → " + azb("spillover tecnológico") + ": outras firmas imitam, aprendem e adaptam a ideia "
            "sem pagar ao inovador. O benefício social supera o privado, e por isso o mercado investe "
            "<b>menos</b> do que o ótimo em P&amp;D. Daí patentes, subsídios à pesquisa e financiamento público "
            "de ciência básica (" + rx("no Brasil, Finep, CNPq e a Lei do Bem") + ").",
            "Os concorrentes que precisam se adaptar ou perdem mercado sofrem uma "
            + azb("externalidade pecuniária") + ": o efeito passa por preços e quantidades (a nova tecnologia "
            "baixa o preço de mercado). Ela redistribui renda, mas não gera ineficiência nem justifica "
            "correção — é a “destruição criadora” de " + oc("Schumpeter") + ".",
            "Externalidade " + azb("tecnológica") + " (real) é a que altera diretamente a função de produção "
            "ou de utilidade de terceiros: poluição, ruído, polinização, conhecimento que vaza.",
            vm("Regra-âncora: inovação que se difunde = externalidade positiva → subinvestimento privado."),
        ],
        "dissecando": (cz("[troca de conceito · modulador absoluto]") + " A definição inicial é frouxa, mas "
                       "aceitável; o erro está na classificação (negativa no lugar de positiva) e no "
                       "“invariavelmente”, que transforma um efeito possível de concorrência em regra. Pista: "
                       "o “dano” descrito passa pelo mercado, não por fora dele."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os gastos privados em pesquisa e desenvolvimento tendem a ficar abaixo do nível socialmente "
            "ótimo, pois parte do benefício é apropriada por outras empresas.”</i> → CERTO",
            "<i>“A queda de lucros de concorrentes provocada por uma inovação constitui externalidade negativa "
            "que justifica imposto pigouviano.”</i> → ERRADO (externalidade pecuniária não exige correção)",
        ])],
        "reescrita": ("Externalidades são impactos econômicos que fogem ao controle de quem os gera. Por exemplo, "
                      "quando uma empresa desenvolve uma tecnologia inovadora, " + hl("o conhecimento tende a "
                      "transbordar para outras empresas do setor, que se beneficiam dele sem pagar")
                      + ", caracterizando uma externalidade " + hl("positiva") + "."),
        "tipo_erro": ["TROCA_CONCEITO", "GENERALIZACAO"], "moduladores": ["invariavelmente"], "dificuldade": 1,
        "comentario_fonte": ("Definição de externalidade correta; erro ao classificar a inovação tecnológica como "
                             "externalidade negativa: a disseminação de tecnologia é externalidade positiva."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00046
    {
        "id": "ECO-E2-L00046-1", "fonte_ref": "E2-L00046", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("O teorema de Coase sugere que, para resolver externalidades negativas, deve-se evitar "
                      "intervenções diretas do governo, como impostos ou licenças para poluir. Em vez disso, é "
                      "preferível uma solução privada, em que as partes envolvidas negociem entre si, podendo o "
                      "governo atuar como mediador para facilitar um acordo que maximize os benefícios sociais."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "contestavel",
        "anotada": az("O teorema de Coase sugere que, para resolver externalidades negativas, deve-se evitar "
                      "intervenções diretas do governo, como impostos ou <u>licenças para poluir</u>. Em vez "
                      "disso, é preferível uma <u>solução privada</u>, em que as partes envolvidas negociem entre "
                      "si, podendo o governo atuar como mediador para facilitar um acordo que maximize os "
                      "benefícios sociais."),
        "poucas": ("Pelo " + azb("teorema de Coase") + ", com direitos de propriedade definidos e custos de "
                   "transação nulos, a " + azb("negociação privada") + " já leva ao resultado eficiente, sem "
                   "imposto nem regulação; ao Estado basta definir direitos e facilitar o acordo."),
        "condicionais": [("⚠️ Gabarito contestável",
                          "o teorema é uma proposição <b>condicional</b> (vale se os custos de transação forem "
                          "nulos), não uma recomendação de política. O próprio " + oc("Coase") + " insistia que, "
                          "no mundo real, esses custos são altos — e então impostos e regulação podem ser a "
                          "melhor opção. Além disso, as " + azb("licenças negociáveis para poluir") + " são "
                          "justamente a aplicação da lógica coasiana (criar um direito de propriedade e deixá-lo "
                          "ser trocado), e não o seu oposto. O CERTO só se sustenta na leitura escolar “Coase = "
                          "solução privada, Pigou = solução pública”.")],
        "destrinchando": [
            oc("Ronald Coase") + ", “The Problem of Social Cost” (" + vd("1960") + "; Nobel de " + vd("1991")
            + "): se os " + azb("direitos de propriedade") + " estão bem definidos e os "
            + azb("custos de transação") + " são nulos, as partes negociam até a alocação eficiente, seja quem "
            "for o titular do direito.",
            "Exemplo: uma fábrica lucra 100 poluindo e causa dano de 150 a pescadores. Se os pescadores têm o "
            "direito, a fábrica não consegue comprá-lo (paga no máximo 100). Se o direito é da fábrica, os "
            "pescadores lhe pagam entre 100 e 150 para parar. Nos dois casos a poluição cessa; muda só "
            "<b>quem paga a quem</b>.",
            "Contraste com " + oc("Pigou") + ": a solução pigouviana exige que o Estado conheça o dano marginal "
            "e o tribute; a coasiana exige apenas direitos claros e um ambiente de negociação barato. O papel "
            "do governo, em Coase, é definir e fazer valer direitos (Judiciário, registros) e reduzir custos de "
            "transação.",
            "Limites práticos: muitas partes (poluição do ar de uma metrópole), "
            + azb("free-riding") + " entre as vítimas, comportamento estratégico (holdout) e informação "
            "assimétrica sobre lucros e danos tornam a negociação inviável.",
        ],
        "dissecando": (cz("[paráfrase fiel · modulador relativo]") + " A banca resume Coase como “solução "
                       "privada em vez de intervenção”, com o governo como “mediador”. Quem conhece a crítica "
                       "às licenças hesita; o gabarito segue a leitura de manual. Em C/E de cursinho, “Coase → "
                       "negociação privada” costuma ser CERTO."),
        "modulos": [("😈 Para dificultar", [
            "<i>“O teorema de Coase garante a solução privada eficiente mesmo quando os custos de transação "
            "forem elevados.”</i> → ERRADO (ignora a condição de custos nulos)",
            "<i>“Os mercados de licenças negociáveis de emissão aplicam a ideia de criar direitos de "
            "propriedade sobre o recurso poluído.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL", "MODULADOR_RELATIVO"], "moduladores": ["deve-se", "podendo"],
        "dificuldade": 2,
        "comentario_fonte": ("Com direitos bem definidos e sem custos de transação, as partes negociam e resolvem "
                             "a externalidade sem intervenção direta do governo, que agiria apenas como "
                             "mediador."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["contestavel: Coase não condena licenças para poluir (são aplicação da sua lógica) e o "
                    "teorema é condicional a custos de transação nulos; gabarito CERTO mantido pela leitura de "
                    "manual"],
    },
    # ------------------------------------------------------------------ E2-L00047
    {
        "id": "ECO-E2-L00047-1", "fonte_ref": "E2-L00047", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "IDEG – Prof. Bozan", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_BOZAN,
        "rotulo_item": "Item",
        "assertiva": ("Bens públicos são caracterizados por serem não-excludentes e não-rivais, tornando inviável "
                      "precificá-los no mercado, uma vez que seu consumo não pode ser restringido a pagantes, e "
                      "seu uso por um indivíduo não impede o uso simultâneo por outro."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Bens públicos são caracterizados por serem <u>não-excludentes e não-rivais</u>, tornando "
                      "inviável precificá-los no mercado, uma vez que seu consumo não pode ser restringido a "
                      "pagantes, e seu uso por um indivíduo não impede o uso simultâneo por outro."),
        "poucas": ("Definição exata de " + azb("bem público puro") + ": não exclusão (não dá para barrar quem "
                   "não paga) + não rivalidade (o uso de um não reduz o do outro). Sem exclusão, não há como "
                   "cobrar preço."),
        "destrinchando": [
            "Os dois critérios de classificação (" + oc("Samuelson") + ", 1954; " + oc("Musgrave")
            + "): " + azb("exclusão") + " — é possível impedir o consumo de quem não paga? — e "
            + azb("rivalidade") + " — o consumo de um reduz o que sobra para os outros?",
            "Quadro completo: excludente e rival → " + azb("bem privado") + " (sorvete); excludente e não "
            "rival → " + azb("bem de clube") + " ou monopólio natural (TV a cabo, parque com ingresso); não "
            "excludente e rival → " + azb("recurso comum") + " (peixes no mar); não excludente e não rival → "
            + azb("bem público") + " (defesa nacional, farol, iluminação pública).",
            "A não exclusão gera o " + azb("carona (free-rider)") + ": ninguém revela quanto valoriza o bem, "
            "porque usufrui dele de qualquer forma. A não rivalidade torna o custo marginal de mais um usuário "
            "nulo — então, mesmo que se pudesse excluir, cobrar preço positivo afastaria usuários sem "
            "economizar recurso algum.",
            "Resultado: subprovisão privada e financiamento por " + azb("tributos") + ". Bem público é conceito "
            "econômico, não jurídico: o que importa são as duas propriedades, e não quem produz ou é dono.",
        ],
        "dissecando": (cz("[literalidade]") + " O item reproduz a definição de manual e explica cada adjetivo "
                       "corretamente (excludente → restringir a pagantes; rival → uso simultâneo). O risco é a "
                       "troca dos conceitos — “não rival” associado a pagamento —, o que não ocorre aqui."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Bens públicos são não rivais, pois seu consumo não pode ser restringido a pagantes.”</i> → "
            "ERRADO (troca de conceito: isso é a não exclusão)",
            "<i>“Recursos comuns compartilham com os bens públicos a não exclusão, mas são rivais.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Bens públicos não são rivais nem excludentes; precificação individual inviável; "
                             "financiamento por tributos; exemplo da iluminação pública."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00331
    {
        "id": "ECO-E2-L00331-1", "fonte_ref": "E2-L00331", "destino": "12", "subtema": H2["info"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("O fenômeno da seleção adversa ocorre em situações de informação oculta pré-contratual, "
                      "podendo levar ao colapso do mercado (como no modelo de “Lemons” de Akerlof), enquanto o "
                      "risco moral (moral hazard) está associado a ações ocultas pós-contratuais, onde o "
                      "monitoramento do comportamento do agente é imperfeito."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O fenômeno da seleção adversa ocorre em situações de <u>informação oculta "
                      "pré-contratual</u>, podendo levar ao colapso do mercado (como no modelo de “Lemons” de "
                      "Akerlof), enquanto o risco moral (moral hazard) está associado a <u>ações ocultas "
                      "pós-contratuais</u>, onde o monitoramento do comportamento do agente é imperfeito."),
        "poucas": (azb("Seleção adversa") + " = informação oculta <b>antes</b> do contrato (tipo, qualidade); "
                   + azb("risco moral") + " = ação oculta <b>depois</b> do contrato (esforço, cuidado). O item "
                   "acerta as duas datas e os dois exemplos."),
        "destrinchando": [
            oc("George Akerlof") + ", “The Market for ‘Lemons’” (" + vd("1970") + "): no mercado de carros "
            "usados, o vendedor sabe a qualidade e o comprador não. O comprador paga só a qualidade "
            "<b>média</b>; os donos de carros bons se retiram, a média cai, o preço cai de novo… No limite, só "
            "os “limões” são negociados — o mercado pode " + azb("colapsar") + ".",
            "Seleção adversa em seguros: a seguradora não distingue riscos; o prêmio médio afasta os de baixo "
            "risco e atrai os de alto. Remédios: " + azb("sinalização") + " (" + oc("Spence") + ": diploma, "
            "garantia), " + azb("triagem/screening") + " (" + oc("Stiglitz") + ": menu de contratos, "
            "questionário médico), seguro obrigatório. Os três dividiram o Nobel de " + vd("2001") + ".",
            azb("Risco moral") + ": depois de segurado, o motorista se descuida; depois de contratado, o "
            "empregado se esforça menos. É o " + azb("problema agente-principal") + ": o principal não observa "
            "a ação do agente. Remédios: franquia e coparticipação, bônus por desempenho, salário de "
            "eficiência, monitoramento.",
            vm("Regra-âncora: antes do contrato → seleção adversa (tipo oculto); depois → risco moral (ação "
               "oculta)."),
        ],
        "dissecando": (cz("[literalidade]") + " Definições de manual, corretamente datadas. A banca costuma "
                       "inverter os momentos (seleção adversa “pós-contratual”) ou os exemplos (franquia "
                       "contra seleção adversa); conferir a âncora antes/depois resolve."),
        "modulos": [("😈 Para dificultar", [
            "<i>“A exigência de franquia nos contratos de seguro de automóvel visa mitigar a seleção "
            "adversa.”</i> → ERRADO (troca de conceito: franquia combate o risco moral)",
            "<i>“O diploma universitário pode funcionar como sinal de produtividade, mesmo que não a aumente, "
            "atenuando a seleção adversa no mercado de trabalho.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["podendo"], "dificuldade": 1,
        "comentario_fonte": ("Seleção adversa: informação oculta ex ante (carros usados, seguros); risco moral: "
                             "ação oculta ex post (motorista que dirige pior após o seguro)."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00333
    {
        "id": "ECO-E2-L00333-1", "fonte_ref": "E2-L00333", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Armstrong", "prova": "Pré-TPS/2026", "ano": 2026, "cacd": False,
        "errei": False,
        "comando": CMD_ARM,
        "rotulo_item": "Item",
        "assertiva": ("De acordo com o Teorema de Coase, se os custos de transação forem nulos e os direitos de "
                      "propriedade forem bem definidos, a alocação de recursos resultante da negociação entre as "
                      "partes será eficiente, independentemente de como os direitos de propriedade foram "
                      "distribuídos inicialmente, embora a distribuição de riqueza final entre as partes possa "
                      "ser afetada."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("De acordo com o Teorema de Coase, se os custos de transação forem nulos e os direitos de "
                      "propriedade forem bem definidos, a alocação de recursos resultante da negociação entre as "
                      "partes será eficiente, independentemente de como os direitos de propriedade foram "
                      "distribuídos inicialmente, <u>embora a distribuição de riqueza final entre as partes "
                      "possa ser afetada</u>."),
        "poucas": ("A " + azb("eficiência") + " não depende de quem recebe o direito; a "
                   + azb("distribuição") + " depende: o titular do direito é quem recebe o pagamento na "
                   "negociação."),
        "destrinchando": [
            "Enunciado completo do " + azb("teorema de Coase") + " (" + oc("Ronald Coase") + ", " + vd("1960")
            + "): direitos de propriedade bem definidos + custos de transação nulos → negociação privada leva "
            "à alocação eficiente (ótimo de Pareto), qualquer que seja a atribuição inicial do direito.",
            "Por que a distribuição muda: imagine um pecuarista cujo gado destrói 60 da lavoura vizinha e uma "
            "cerca que custa 40. Se o agricultor tem o direito a não ser prejudicado, o pecuarista constrói a "
            "cerca e arca com 40. Se o pecuarista tem o direito de deixar o gado solto, o agricultor paga a "
            "cerca (ou paga ao pecuarista para cercar). A cerca sai nos dois casos (alocação eficiente); "
            + vd("quem gasta os 40") + " muda (distribuição).",
            "Ressalva técnica: a invariância da alocação pressupõe ausência de " + azb("efeitos-renda")
            + " relevantes. Se a riqueza recebida altera a disposição a pagar das partes, a quantidade "
            "eficiente pode variar com a atribuição — detalhe raro em prova.",
            "Lição de política: a ineficiência das externalidades vem da <b>falta de direitos definidos</b> ou "
            "de custos de transação altos — o que justifica, por exemplo, mercados de licenças de emissão.",
        ],
        "dissecando": (cz("[literalidade · detalhe]") + " Versão completa do teorema, com o adendo "
                       "distributivo. O “embora … possa ser afetada” é o detalhe que derruba quem acha que "
                       "Coase torna a atribuição de direitos irrelevante em tudo. Ver também ECO-E2-L00517-1 e "
                       "ECO-E2-L00680-1."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Pelo teorema de Coase, a atribuição inicial dos direitos de propriedade é irrelevante tanto "
            "para a eficiência quanto para a distribuição de renda.”</i> → ERRADO (a distribuição muda)",
            "<i>“O teorema de Coase dispensa a definição dos direitos de propriedade.”</i> → ERRADO (é uma das "
            "duas condições)",
        ])],
        "tipo_erro": ["LITERAL", "DETALHE"], "moduladores": ["possa"], "dificuldade": 1,
        "comentario_fonte": ("Coase (1960): custos de transação nulos e direitos bem definidos → negociação "
                             "eficiente, independentemente de quem detém o direito inicial; intervenção "
                             "governamental desnecessária."),
        "qualidade_fonte": "raso",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00517-1 e ECO-E2-L00680-1 cobram o mesmo enunciado do teorema, "
                    "sem o adendo distributivo (outra fonte)"],
    },
    # ------------------------------------------------------------------ E2-L00515
    {
        "id": "ECO-E2-L00515-1", "fonte_ref": "E2-L00515", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26A,
        "rotulo_item": "Item",
        "assertiva": ("Um subsídio pigouviano é o instrumento correto para internalizar uma externalidade "
                      "negativa, pois ao subsidiar o produtor, o governo o incentiva a reduzir a atividade que "
                      "gera o dano social."),
        "gabarito": "ERRADO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": (az("Um ") + vm("subsídio") + az(" pigouviano é o instrumento correto para internalizar uma "
                                                    "externalidade negativa, pois ao ")
                    + vm("subsidiar") + az(" o produtor, o governo o incentiva a reduzir a atividade que gera o "
                                           "dano social.")),
        "poucas": ("Externalidade negativa pede " + azb("imposto pigouviano") + " (encarece a atividade "
                   "danosa); o " + azb("subsídio pigouviano") + " é o remédio da externalidade "
                   "<b>positiva</b> (barateia a atividade benéfica)."),
        "destrinchando": [
            "Lógica de " + oc("Pigou") + ": aproximar o custo ou benefício privado do social. Externalidade "
            "negativa → CMg social > CMg privado → o mercado produz demais → " + vd("imposto = custo externo "
            "marginal") + " no ótimo. Externalidade positiva → benefício social > privado → produz de menos → "
            + vd("subsídio = benefício externo marginal") + ".",
            "Subsidiar o produtor reduz o seu custo e o estimula a produzir <b>mais</b> — exatamente o "
            "contrário do que se quer com uma atividade poluidora. Subsídio pigouviano típico: vacinação, "
            "pesquisa e desenvolvimento, educação básica, reflorestamento.",
            "Nuance de finanças públicas: pagar ao poluidor <b>por unidade de poluição evitada</b> (subsídio ao "
            "abatimento) cria o mesmo incentivo marginal que o imposto. Mas, como eleva os lucros do setor, "
            "atrai novas firmas e pode aumentar a poluição total no longo prazo (" + oc("Baumol e Oates")
            + "). Por isso o manual associa externalidade negativa a imposto, e não a subsídio.",
            "Outros instrumentos para a negativa: padrões e limites (regulação de comando e controle), "
            + azb("licenças negociáveis") + " de emissão (sistema europeu de comércio de emissões; "
            + rx("no Brasil, o SBCE, criado pela Lei 15.042/2024") + ") e a negociação coasiana.",
        ],
        "dissecando": (cz("[troca de conceito]") + " O item troca o instrumento (subsídio no lugar de imposto) e "
                       "constrói uma justificativa que não fecha: subsidiar não incentiva a reduzir. Pista: o "
                       "verbo “reduzir” combina com “encarecer”, não com “subsidiar”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Um subsídio pigouviano é instrumento adequado para corrigir a subprodução de bens com "
            "externalidades positivas, como a vacinação.”</i> → CERTO",
            "<i>“O imposto pigouviano ótimo iguala o custo externo marginal no nível de produção de "
            "mercado.”</i> → ERRADO (é no nível socialmente ótimo)",
        ])],
        "reescrita": ("Um " + hl("imposto") + " pigouviano é o instrumento correto para internalizar uma "
                      "externalidade negativa, pois ao " + hl("tributar") + " o produtor, o governo o incentiva "
                      "a reduzir a atividade que gera o dano social."),
        "tipo_erro": ["TROCA_CONCEITO"], "moduladores": [], "dificuldade": 1,
        "comentario_fonte": ("Para externalidade negativa, imposto pigouviano, não subsídio; subsídio pigouviano "
                             "serve à externalidade positiva (ex.: P&amp;D)."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00516
    {
        "id": "ECO-E2-L00516-1", "fonte_ref": "E2-L00516", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26A,
        "rotulo_item": "Item",
        "assertiva": ("A vacinação em massa gera uma externalidade positiva, pois além de proteger o indivíduo "
                      "vacinado, reduz a probabilidade de contágio para toda a comunidade. Devido a essa "
                      "externalidade, a provisão de vacinas pelo mercado privado tende a ser inferior à "
                      "socialmente ótima."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("A vacinação em massa gera uma externalidade <u>positiva</u>, pois além de proteger o "
                      "indivíduo vacinado, reduz a probabilidade de contágio para toda a comunidade. Devido a "
                      "essa externalidade, a provisão de vacinas pelo mercado privado tende a ser "
                      "<u>inferior</u> à socialmente ótima."),
        "poucas": ("Quem se vacina considera só o " + azb("benefício privado") + "; o benefício para os outros "
                   "(menos contágio) fica fora da decisão. Com benefício social > privado, o mercado "
                   + vd("subprovê") + " vacinas."),
        "destrinchando": [
            azb("Externalidade positiva no consumo") + ": benefício marginal social (BMgS) = benefício "
            "marginal privado (BMgP, a demanda) + benefício externo marginal. O mercado iguala BMgP ao custo "
            "marginal e para em Qₘ; o ótimo social está em Q*, onde BMgS = CMg, com " + vd("Q* > Qₘ") + ".",
            "Entre Qₘ e Q*, cada dose a mais gera benefício social acima do custo, mas ninguém a compra: é o "
            + azb("peso morto") + " da subprovisão.",
            "Vacinação tem ainda o efeito de " + azb("imunidade de rebanho") + ": acima de certa cobertura, até "
            "os não vacinados ficam protegidos — o que estimula o comportamento de carona (“se todos se "
            "vacinam, eu não preciso”).",
            "Correções: " + azb("subsídio pigouviano") + " igual ao benefício externo marginal, provisão "
            "pública gratuita, obrigatoriedade. " + rx("O Programa Nacional de Imunizações (PNI, 1973) e a "
            "vacinação gratuita pelo SUS") + " são a resposta brasileira.",
            vm("Regra-âncora: externalidade positiva → mercado produz de menos → subsídio; negativa → produz "
               "demais → imposto."),
        ],
        "grafico_verso": "ECO-E2-L00516-1-V1",
        "dissecando": (cz("[paráfrase fiel]") + " Item de manual (é o exemplo de " + oc("Mankiw") + "), com "
                       "causa e efeito na ordem certa. A banca costuma inverter o sentido do desvio (“superior "
                       "à socialmente ótima”) ou o sinal da externalidade."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Por gerar externalidade positiva, a vacinação tende a ser ofertada pelo mercado em quantidade "
            "superior à socialmente ótima.”</i> → ERRADO (inversão: subprovisão)",
            "<i>“O subsídio ótimo à vacinação corresponde ao benefício externo marginal no nível socialmente "
            "ótimo de vacinas.”</i> → CERTO",
        ])],
        "tipo_erro": ["PARAFRASE_FIEL"], "moduladores": ["tende a"], "dificuldade": 1,
        "comentario_fonte": ("Benefício da vacina se estende à comunidade; o mercado só precifica o benefício "
                             "privado; quantidade de mercado menor que a socialmente ótima."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": [],
    },
    # ------------------------------------------------------------------ E2-L00517
    {
        "id": "ECO-E2-L00517-1", "fonte_ref": "E2-L00517", "destino": "12", "subtema": H2["ext"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26A,
        "rotulo_item": "Item",
        "assertiva": ("O Teorema de Coase postula que, na ausência de custos de transação e com direitos de "
                      "propriedade bem definidos, as partes envolvidas em uma externalidade podem negociar "
                      "privadamente e alcançar uma solução eficiente, independentemente de a quem o direito de "
                      "propriedade foi inicialmente alocado."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("O Teorema de Coase postula que, <u>na ausência de custos de transação e com direitos de "
                      "propriedade bem definidos</u>, as partes envolvidas em uma externalidade podem negociar "
                      "privadamente e alcançar uma solução eficiente, <u>independentemente</u> de a quem o "
                      "direito de propriedade foi inicialmente alocado."),
        "poucas": ("Enunciado-padrão do " + azb("teorema de Coase") + ", com as duas condições (custos de "
                   "transação nulos, direitos definidos) e a conclusão (eficiência qualquer que seja o titular "
                   "do direito)."),
        "destrinchando": [
            oc("Ronald Coase") + " (“The Problem of Social Cost”, " + vd("1960") + ") mostrou que a "
            "externalidade é um problema <b>recíproco</b>: o vizinho que reclama da fumaça também “impõe” "
            "custo à fábrica ao exigir que ela pare. Definido quem tem o direito, os dois negociam.",
            "As duas condições, uma a uma: (1) " + azb("direitos de propriedade bem definidos") + " — sem "
            "saber quem tem o direito, não há o que negociar; (2) " + azb("custos de transação nulos") + " — "
            "localizar as partes, medir o dano, redigir e fiscalizar o acordo não custam nada.",
            "O que o teorema <b>não</b> diz: que a distribuição de renda é a mesma (quem tem o direito recebe "
            "o pagamento), nem que funciona com muitas partes ou com informação assimétrica. O próprio Coase "
            "usou o teorema para mostrar o contrário: como os custos de transação são positivos no mundo real, "
            "as <b>instituições</b> (direito, firmas, contratos) importam.",
            "Aplicação: o comércio de licenças de emissão cria direitos de poluir negociáveis — a lógica "
            "coasiana operando com o Estado apenas definindo o teto e os direitos.",
            vm("Regra-âncora: Coase = direitos definidos + custo de transação zero → eficiência, seja quem for o "
               "titular."),
        ],
        "dissecando": (cz("[literalidade]") + " Enunciado completo, sem enxerto. As versões erradas costumam "
                       "tirar uma das condições, trocar “independentemente” por “desde que o direito seja de "
                       "X” (ECO-E2-L00852-1) ou fazer a eficiência “depender apenas” da distribuição "
                       "(ECO-E2-L01179-1)."),
        "modulos": [("😈 Para dificultar", [
            "<i>“…as partes podem negociar e alcançar uma solução eficiente, desde que o direito de "
            "propriedade seja atribuído a quem sofre a externalidade.”</i> → ERRADO (restrição indevida)",
            "<i>“O teorema de Coase supõe custos de transação positivos, porém baixos.”</i> → ERRADO (supõe "
            "custos nulos)",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["podem"], "dificuldade": 1,
        "comentario_fonte": ("Sem custos de transação, com informação perfeita e direitos claros, a negociação "
                             "privada alcança a alocação eficiente, independentemente do titular inicial."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00680-1 (mesmo curso, outra lista) e ECO-E2-L00333-1 cobram o "
                    "mesmo enunciado com outra redação"],
    },
    # ------------------------------------------------------------------ E2-L00518
    {
        "id": "ECO-E2-L00518-1", "fonte_ref": "E2-L00518", "destino": "12", "subtema": H2["bens"],
        "tipo": "C/E", "banca": "Nabuco", "prova": "", "ano": 2026, "cacd": False, "errei": False,
        "comando": CMD_NAB26A,
        "rotulo_item": "Item",
        "assertiva": ("Recursos comuns, como os cardumes de peixes em alto-mar, são bens rivais mas não "
                      "excludentes, o que pode levar à sua superexploração no fenômeno conhecido como “Tragédia "
                      "dos Comuns”."),
        "gabarito": "CERTO", "gabarito_origem": "fonte", "status": "normal",
        "anotada": az("Recursos comuns, como os cardumes de peixes em alto-mar, são bens <u>rivais mas não "
                      "excludentes</u>, o que pode levar à sua superexploração no fenômeno conhecido como "
                      "“Tragédia dos Comuns”."),
        "poucas": (azb("Recurso comum") + " = rival + não excludente. Ninguém pode ser impedido de pescar, mas "
                   "cada peixe pescado é um peixe a menos para os outros: o incentivo é pescar demais."),
        "destrinchando": [
            "Na matriz exclusão × rivalidade, o recurso comum divide com o bem público a " + azb("não "
            "exclusão") + " e com o bem privado a " + azb("rivalidade") + ". Exemplos: peixes em alto-mar, "
            "pastagens abertas, aquíferos, ar limpo, estradas congestionadas sem pedágio.",
            oc("Garrett Hardin") + ", “The Tragedy of the Commons” (<i>Science</i>, " + vd("1968") + "): cada "
            "pastor acrescenta ovelhas ao pasto comum porque fica com todo o ganho e divide a perda com os "
            "demais. Racional para cada um, ruinoso para o conjunto: o pasto se esgota.",
            "Em termos econômicos, é uma " + azb("externalidade negativa") + ": quem pesca reduz o estoque "
            "disponível para os outros e não paga por isso; o custo marginal privado fica abaixo do social.",
            "Saídas: cotas de captura (inclusive cotas individuais transferíveis), defeso, licenças, "
            "privatização ou definição de direitos. " + oc("Elinor Ostrom") + " (<i>Governing the Commons</i>, "
            + vd("1990") + "; Nobel de " + vd("2009") + ") mostrou que comunidades também gerem bem os comuns "
            "com regras próprias, sem Estado nem mercado.",
        ],
        "dissecando": (cz("[literalidade]") + " Definição correta, exemplo correto e consequência com "
                       "modulador relativo (“pode levar”). A troca habitual da banca é chamar o recurso comum "
                       "de “não rival” ou de “excludente”."),
        "modulos": [("😈 Para dificultar", [
            "<i>“Os cardumes de peixes em alto-mar são bens não rivais e não excludentes, o que caracteriza "
            "bens públicos puros.”</i> → ERRADO (troca de conceito: são rivais)",
            "<i>“A fixação de cotas de pesca é uma forma de mitigar a tragédia dos comuns.”</i> → CERTO",
        ])],
        "tipo_erro": ["LITERAL"], "moduladores": ["pode"], "dificuldade": 1,
        "comentario_fonte": ("Recursos comuns: rivais e não excludentes; cada indivíduo explora em excesso porque "
                             "os custos são dispersos e os benefícios, privados."),
        "qualidade_fonte": "bom",
        "figuras_fonte": [],
        "alertas": ["quase_duplicata: ECO-E2-L00682-1 cobra a mesma definição de tragédia dos comuns (mesmo "
                    "curso, outra lista)"],
    },
]
